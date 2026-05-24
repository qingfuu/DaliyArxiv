#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate an Obsidian-friendly daily arXiv CS report.

Workflow:
- Collect papers from selected Computer Science subcategories on the target arXiv date.
- Organize papers by official arXiv cs.* subcategory.
- Extract 2-3 related-field keywords per paper.
- Write one folder per day, one Markdown file per subcategory, plus one keyword-focused summary.
- If the target date has no CS papers, write a status note only. Do not backfill older days.
"""

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET


ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_USER_AGENT = "OpenClaw arxiv daily bot (contact: local user)"
ROOT_DIR = os.path.dirname(__file__)
HTTP_CACHE_DIR = os.path.join(ROOT_DIR, "99_System", "Cache", "http")
ANALYSIS_CACHE_DIR = os.path.join(ROOT_DIR, "99_System", "Cache", "analysis")
ARXIV_MIN_INTERVAL_SECONDS = 1.2  # conservative but not painfully slow; arXiv may still rate-limit
MONTHLY_LIST_SHOW = 2000
RECENT_LIST_SHOW = 2000
_LAST_ARXIV_REQUEST_AT = 0.0
MINIMAX_API_URL = "https://api.minimaxi.chat/v1/text/chatcompletion_v2"
MINIMAX_MODEL = "MiniMax-M2.7"
OPENAI_CHAT_API_URL = "https://api.openai.com/v1/chat/completions"
OPENAI_MODEL = os.environ.get("DAILY_ARXIV_OPENAI_MODEL", "gpt-4.1-mini")
POE_CHAT_API_URL = "https://api.poe.com/v1/chat/completions"
POE_MODEL = os.environ.get("DAILY_ARXIV_POE_MODEL", "gpt-5.4-mini")
ANALYSIS_PROMPT_VERSION = "daily-cn-v3"

ALL_CS_CATEGORIES = {
    "cs.AI": "Artificial Intelligence",
    "cs.AR": "Hardware Architecture",
    "cs.CC": "Computational Complexity",
    "cs.CE": "Computational Engineering, Finance, and Science",
    "cs.CG": "Computational Geometry",
    "cs.CL": "Computation and Language",
    "cs.CR": "Cryptography and Security",
    "cs.CV": "Computer Vision and Pattern Recognition",
    "cs.CY": "Computers and Society",
    "cs.DB": "Databases",
    "cs.DC": "Distributed, Parallel, and Cluster Computing",
    "cs.DL": "Digital Libraries",
    "cs.DM": "Discrete Mathematics",
    "cs.DS": "Data Structures and Algorithms",
    "cs.ET": "Emerging Technologies",
    "cs.FL": "Formal Languages and Automata Theory",
    "cs.GL": "General Literature",
    "cs.GR": "Graphics",
    "cs.GT": "Computer Science and Game Theory",
    "cs.HC": "Human-Computer Interaction",
    "cs.IR": "Information Retrieval",
    "cs.IT": "Information Theory",
    "cs.LG": "Machine Learning",
    "cs.LO": "Logic in Computer Science",
    "cs.MA": "Multiagent Systems",
    "cs.MM": "Multimedia",
    "cs.MS": "Mathematical Software",
    "cs.NA": "Numerical Analysis",
    "cs.NE": "Neural and Evolutionary Computing",
    "cs.NI": "Networking and Internet Architecture",
    "cs.OH": "Other Computer Science",
    "cs.OS": "Operating Systems",
    "cs.PF": "Performance",
    "cs.PL": "Programming Languages",
    "cs.RO": "Robotics",
    "cs.SC": "Symbolic Computation",
    "cs.SD": "Sound",
    "cs.SE": "Software Engineering",
    "cs.SI": "Social and Information Networks",
    "cs.SY": "Systems and Control",
}

# Broaden the monitored CS categories to avoid missing relevant papers when they are
# primarily filed under adjacent cs.* areas (e.g., systems/IR/HCI/security).
# We still apply a strict relevance filter afterwards.
TARGET_CS_CATEGORIES = [
    "cs.AI", "cs.LG", "cs.CL", "cs.CV", "cs.RO",
    "cs.GR", "cs.SY",
    "cs.IR", "cs.HC", "cs.SE", "cs.CR",
    "cs.NI", "cs.DC", "cs.DS", "cs.IT",
    "cs.NE", "cs.CY",
]
CS_CATEGORIES = {category: ALL_CS_CATEGORIES[category] for category in TARGET_CS_CATEGORIES}
MAX_DAILY_PAPERS = 100
REPORT_DOMAIN_WEIGHTS = {
    "具身智能": 0.3,
    "大模型": 0.1,
    "强化学习": 0.2,
    "世界模型": 0.2,
    "机器人": 0.2,
}
REPORT_DOMAINS = list(REPORT_DOMAIN_WEIGHTS)

FOCUS_KEYWORDS = {
    "大模型": [
        "large language model", "large multimodal model", "vision-language model",
        "llm", "vlm", "foundation model", "language model", "multimodal",
        "instruction tuning", "prompting", "rag", "retrieval-augmented",
        "agent", "agents",
    ],
    "具身智能": [
        "embodied ai", "embodied", "vision-language-action", "vla",
        "robot manipulation", "robotic manipulation", "dexterous", "grasping",
        "object navigation", "robot navigation", "locomotion", "sim-to-real",
        "humanoid", "quadruped",
    ],
    "强化学习": [
        "reinforcement learning", "deep reinforcement learning", "offline rl",
        "policy gradient", "actor-critic", "q-learning", "mdp", "pomdp",
        "reward model", "policy optimization",
    ],
    "世界模型": [
        "world model", "world models", "latent dynamics", "dynamics model",
        "model-based reinforcement learning", "dreamer", "transition model",
    ],
    "机器人": [
        "robot", "robotics", "robotic", "humanoid", "quadruped", "uav",
        "drone", "motion planning", "path planning", "slam", "ros",
    ],
}

REPORT_DOMAIN_KEYWORDS = {domain: FOCUS_KEYWORDS[domain] for domain in REPORT_DOMAINS}
REPORT_DOMAIN_KEYWORDS["大模型"] = REPORT_DOMAIN_KEYWORDS["大模型"] + [
    "large vision-language model", "large multimodal model", "mllm",
    "diffusion language model", "reasoning model",
]

ANALYSIS_OUTPUT_REQUIREMENTS = {
    "研究背景与动机": "说明具体任务、现有方法或系统瓶颈、论文为什么要解决这个问题，避免只写“存在挑战”。",
    "方法概述和架构": "说明核心方法名称、主要模块/训练或推理流程、关键机制之间如何连接，必要时点出输入输出。",
    "实验结果分析": "说明实验对象/数据集/基线/指标，以及论文报告的关键效果；如果摘要或正文片段未给出数字，要明确写“未在可见文本中给出具体数值”。",
}

RELATED_KEYWORDS = {
    "LLM": ["llm", "large language model", "language model", "foundation model"],
    "Multimodal": ["multimodal", "vision-language", "vlm", "vla", "clip"],
    "Agent": ["agent", "agents", "planning", "tool use", "tree search"],
    "Robotics": ["robot", "robotics", "robotic", "manipulation", "locomotion"],
    "EmbodiedAI": ["embodied", "dexterous", "grasping", "navigation"],
    "RL": ["reinforcement learning", "policy", "reward", "actor-critic", "q-learning", "mdp", "pomdp"],
    "WorldModel": ["world model", "latent dynamics", "dynamics model", "transition model"],
    "ComputerVision": ["computer vision", "image", "video", "3d", "segmentation", "detection"],
    "Security": ["security", "privacy", "attack", "adversarial", "cryptography"],
    "Systems": ["system", "distributed", "network", "database", "operating"],
}

ANALYSIS_DOMAIN_TERMS = {
    "具身智能": ["embodied", "vision-language-action", "vla", "robot manipulation", "robotic manipulation", "navigation", "locomotion", "grasping"],
    "大模型": ["large language model", "llm", "language model", "foundation model", "moe", "rag", "vision-language model", "multimodal"],
    "强化学习": ["reinforcement learning", "rl", "policy", "reward", "actor-critic", "q-learning", "mdp", "grpo"],
    "世界模型": ["world model", "world models", "latent dynamics", "dynamics model", "video generation"],
    "机器人": ["robot", "robotics", "robotic", "humanoid", "uav", "slam", "motion planning", "path planning"],
}

IMG_RE = re.compile(r"<img[^>]+src=\"([^\"]+)\"", re.IGNORECASE)
FIGURE_RE = re.compile(r"<figure[\s\S]{0,5000}?</figure>", re.IGNORECASE)


def cache_path_for_url(url: str) -> str:
    digest = hashlib.sha256(url.encode("utf-8")).hexdigest()
    return os.path.join(HTTP_CACHE_DIR, f"{digest}.bin")


def http_get(
    url: str,
    timeout: int = 30,
    max_retries: int = 6,
    *,
    cache: bool = False,
    refresh_cache: bool = False,
    polite_arxiv: bool = True,
) -> bytes:
    if cache:
        cpath = cache_path_for_url(url)
        if os.path.exists(cpath) and not refresh_cache:
            print(f"[http] cache hit {os.path.basename(cpath)}", file=sys.stderr, flush=True)
            with open(cpath, "rb") as f:
                return f.read()

    req = urllib.request.Request(url, headers={"User-Agent": ARXIV_USER_AGENT})
    last_err = None
    for attempt in range(max_retries):
        try:
            if polite_arxiv and "arxiv.org" in urllib.parse.urlparse(url).netloc:
                global _LAST_ARXIV_REQUEST_AT
                elapsed = time.monotonic() - _LAST_ARXIV_REQUEST_AT
                if elapsed < ARXIV_MIN_INTERVAL_SECONDS:
                    wait_s = ARXIV_MIN_INTERVAL_SECONDS - elapsed
                    print(f"[http] arXiv polite wait {wait_s:.1f}s", file=sys.stderr, flush=True)
                    time.sleep(wait_s)
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                data = resp.read()
            if polite_arxiv and "arxiv.org" in urllib.parse.urlparse(url).netloc:
                _LAST_ARXIV_REQUEST_AT = time.monotonic()
            if cache:
                os.makedirs(HTTP_CACHE_DIR, exist_ok=True)
                with open(cache_path_for_url(url), "wb") as f:
                    f.write(data)
            return data
        except urllib.error.HTTPError as e:
            last_err = e
            transient = e.code == 429 or 500 <= e.code <= 599
            if attempt >= max_retries - 1 or not transient:
                break
            retry_after = e.headers.get("Retry-After")
            wait_s = int(retry_after) if retry_after and retry_after.isdigit() else min(60 * (2 ** attempt), 900)
            print(f"[http] HTTP {e.code}; retry in {wait_s}s...", file=sys.stderr, flush=True)
            time.sleep(wait_s)
        except Exception as e:
            last_err = e
            msg = str(e)
            transient = (
                "429" in msg
                or "UNEXPECTED_EOF" in msg
                or "timed out" in msg.lower()
                or "connection reset" in msg.lower()
                or any(code in msg for code in [" 500", " 502", " 503", " 504"])
            )
            if attempt >= max_retries - 1 or not transient:
                break
            wait_s = min(60 * (2 ** attempt), 900)
            print(f"[http] transient error ({msg}); retry in {wait_s}s...", file=sys.stderr, flush=True)
            time.sleep(wait_s)
    raise last_err


def strip_tags(fragment: str) -> str:
    text = re.sub(r"<[^>]+>", " ", fragment)
    return re.sub(r"\s+", " ", html.unescape(text)).strip()


def parse_arxiv_date(date_text: str) -> str:
    try:
        return dt.datetime.strptime(date_text.strip(), "%d %b %Y").date().isoformat()
    except Exception:
        return ""


def term_in_text(term: str, text: str) -> bool:
    escaped = re.escape(term.lower()).replace(r"\ ", r"\s+")
    return re.search(rf"(?<![a-z0-9]){escaped}(?![a-z0-9])", text.lower()) is not None


def safe_filename(s: str, limit: int = 120) -> str:
    s = re.sub(r"[\s/\\:*?\"<>|]+", "_", s).strip("_")
    return s[:limit] if len(s) > limit else s


def analysis_domain_for_paper(paper: dict) -> str:
    text = f"{paper.get('title', '')} {paper.get('summary', '')}".lower()
    for domain, terms in ANALYSIS_DOMAIN_TERMS.items():
        if any(term_in_text(term, text) for term in terms):
            return domain
    categories = set(paper.get("categories", []))
    if "cs.RO" in categories:
        return "机器人"
    if "cs.CL" in categories:
        return "大模型"
    if "cs.CV" in categories:
        return "多模态技术"
    if "cs.LG" in categories:
        return "强化学习" if "reinforcement" in text else "大模型"
    return "其他"


def analysis_note_link(paper: dict) -> str:
    domain = analysis_domain_for_paper(paper)
    filename = safe_filename(paper.get("title", paper.get("id", "untitled")), limit=140)
    return f"[[20_Research/Papers/{domain}/{filename}|{paper.get('title', paper.get('id', 'untitled'))}]]"


def month_for_target(target_date: str) -> str:
    return target_date[:7]


def arxiv_heading_for_date(target_date: str) -> str:
    d = dt.date.fromisoformat(target_date)
    return f"{d.strftime('%a')}, {d.day} {d.strftime('%b')} {d.year}"


def ids_for_heading(text: str, heading: str) -> list[str]:
    ids, seen = [], set()
    h3_matches = list(re.finditer(r"<h3>(.*?)</h3>", text, re.S))
    for idx, h3_m in enumerate(h3_matches):
        label = strip_tags(h3_m.group(1))
        if heading not in label:
            continue
        start = h3_m.end()
        end = h3_matches[idx + 1].start() if idx + 1 < len(h3_matches) else len(text)
        section = text[start:end]
        for arxiv_id in re.findall(r"arXiv:((?:\d{4}\.\d{4,5})(?:v\d+)?)", section):
            base_id = arxiv_id.split("v", 1)[0]
            if base_id not in seen:
                seen.add(base_id)
                ids.append(base_id)
    return ids


def fetch_recent_cs_ids(target_date: str, refresh_cache: bool = False) -> list[str]:
    """Fetch ids from selected cs.* recent pages for exactly target_date."""
    heading = arxiv_heading_for_date(target_date)
    ids, seen = [], set()
    for category in TARGET_CS_CATEGORIES:
        for skip in range(0, 6000, RECENT_LIST_SHOW):
            url = f"https://arxiv.org/list/{category}/recent?skip={skip}&show={RECENT_LIST_SHOW}"
            print(f"[browse] fetching recent {category} for {target_date} skip={skip}", file=sys.stderr, flush=True)
            # arXiv list pages are mutable daily feeds. Do not reuse cached copies,
            # or a morning run can miss the newest announcement section.
            text = http_get(url, timeout=120, cache=False, refresh_cache=refresh_cache).decode("utf-8", errors="ignore")
            page_ids = ids_for_heading(text, heading)
            for arxiv_id in page_ids:
                if arxiv_id not in seen:
                    seen.add(arxiv_id)
                    ids.append(arxiv_id)
            labels = [strip_tags(m.group(1)) for m in re.finditer(r"<h3>(.*?)</h3>", text, re.S)]
            if page_ids or not any(heading in label for label in labels):
                break
            if not labels:
                break
        time.sleep(1)
    if ids:
        print(f"[browse] selected recent sections {heading}: {len(ids)} ids", file=sys.stderr, flush=True)
    else:
        print(f"[browse] no selected cs.* recent section for {heading}", file=sys.stderr, flush=True)
    return ids


def fetch_cs_new_ids(refresh_cache: bool = False) -> list[str]:
    """Fetch arXiv ids from the global CS new submissions page.

    This is used as a robust fallback when the export API date filters are flaky.
    """
    url = "https://arxiv.org/list/cs/new"
    print(f"[browse] fetching cs/new", file=sys.stderr, flush=True)
    text = http_get(url, timeout=120, cache=False, refresh_cache=refresh_cache).decode("utf-8", errors="ignore")
    ids = re.findall(r"/abs/(\d{4}\.\d{4,5})", text)
    uniq, seen = [], set()
    for arxiv_id in ids:
        if arxiv_id not in seen:
            seen.add(arxiv_id)
            uniq.append(arxiv_id)
    print(f"[browse] cs/new contains {len(uniq)} ids", file=sys.stderr, flush=True)
    return uniq


def fetch_month_category_ids(category: str, target_date: str, refresh_cache: bool = False) -> list[str]:
    month = month_for_target(target_date)
    url = f"https://arxiv.org/list/{category}/{month}?skip=0&show={MONTHLY_LIST_SHOW}"
    print(f"[browse] fetching monthly list {category} {month}", file=sys.stderr, flush=True)
    # Monthly listings are also mutable during the month; always fetch live.
    data = http_get(url, timeout=90, cache=False, refresh_cache=refresh_cache)
    text = data.decode("utf-8", errors="ignore")
    ids = re.findall(r"arXiv:((?:\d{4}\.\d{4,5})(?:v\d+)?)", text)
    uniq, seen = [], set()
    for arxiv_id in ids:
        base_id = arxiv_id.split("v", 1)[0]
        if base_id not in seen:
            seen.add(base_id)
            uniq.append(base_id)
    return uniq


def fetch_month_cs_ids(target_date: str, refresh_cache: bool = False, page_size: int = 2000) -> list[str]:
    """Fetch monthly ids newest-first from selected cs.* listings."""
    ids, seen = [], set()
    for category in TARGET_CS_CATEGORIES:
        try:
            for arxiv_id in reversed(fetch_month_category_ids(category, target_date, refresh_cache=refresh_cache)):
                if arxiv_id not in seen:
                    seen.add(arxiv_id)
                    ids.append(arxiv_id)
            time.sleep(1)
        except Exception as e:
            print(f"[browse] monthly list failed for {category}: {e}", file=sys.stderr, flush=True)
    return ids


def parse_abs_page(arxiv_id: str, html_text: str) -> dict:
    title_m = re.search(r'<h1 class="title[^"]*">\s*<span class="descriptor">Title:</span>(.*?)</h1>', html_text, re.S)
    authors_m = re.search(r'<div class="authors">\s*<span class="descriptor">Authors:</span>(.*?)</div>', html_text, re.S)
    abstract_m = re.search(r'<blockquote class="abstract[^"]*">\s*<span class="descriptor">Abstract:</span>(.*?)</blockquote>', html_text, re.S)
    date_m = re.search(r"\[Submitted on ([^\]]+)\]", html_text)
    subjects_m = re.search(r'<td class="tablecell subjects">(.*?)</td>', html_text, re.S)

    subjects = strip_tags(subjects_m.group(1)) if subjects_m else ""
    categories = re.findall(r"\(([a-z]{2}\.[A-Z]{2})\)", subjects)

    return {
        "id": arxiv_id,
        "title": strip_tags(title_m.group(1)) if title_m else arxiv_id,
        "summary": strip_tags(abstract_m.group(1)) if abstract_m else "",
        "published": parse_arxiv_date(date_m.group(1)) if date_m else "",
        "authors": [strip_tags(a) for a in re.findall(r"<a [^>]*>(.*?)</a>", authors_m.group(1), re.S)] if authors_m else [],
        "abs": f"https://arxiv.org/abs/{arxiv_id}",
        "pdf": f"https://arxiv.org/pdf/{arxiv_id}",
        "categories": categories,
    }


def fetch_abs_paper(arxiv_id: str, refresh_cache: bool = False) -> dict:
    url = f"https://arxiv.org/abs/{arxiv_id}"
    data = http_get(url, timeout=90, cache=True, refresh_cache=refresh_cache)
    return parse_abs_page(arxiv_id, data.decode("utf-8", errors="ignore"))


def parse_api_datetime(value: str) -> str:
    if not value:
        return ""
    try:
        return dt.datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return ""


def parse_api_entry(entry: ET.Element) -> dict:
    atom = "{http://www.w3.org/2005/Atom}"
    arxiv_ns = "{http://arxiv.org/schemas/atom}"

    def find_text(name: str) -> str:
        found = entry.find(f"{atom}{name}")
        return re.sub(r"\s+", " ", found.text or "").strip() if found is not None else ""

    raw_id = find_text("id").rsplit("/", 1)[-1]
    base_id = raw_id.split("v", 1)[0]
    categories = [
        c.attrib.get("term", "")
        for c in entry.findall(f"{atom}category")
        if c.attrib.get("term", "") in CS_CATEGORIES
    ]
    primary = entry.find(f"{arxiv_ns}primary_category")
    primary_term = primary.attrib.get("term", "") if primary is not None else ""
    if primary_term in CS_CATEGORIES and primary_term not in categories:
        categories.insert(0, primary_term)

    pdf_url = f"https://arxiv.org/pdf/{base_id}"
    for link in entry.findall(f"{atom}link"):
        if link.attrib.get("title") == "pdf" or link.attrib.get("type") == "application/pdf":
            pdf_url = link.attrib.get("href", pdf_url).replace(raw_id, base_id)
            break

    return {
        "id": base_id,
        "title": find_text("title") or base_id,
        "summary": find_text("summary"),
        "published": parse_api_datetime(find_text("published")),
        "authors": [find_text_from(author, "name", atom) for author in entry.findall(f"{atom}author")],
        "abs": f"https://arxiv.org/abs/{base_id}",
        "pdf": pdf_url,
        "categories": sorted(set(categories)),
    }


def find_text_from(parent: ET.Element, name: str, namespace: str) -> str:
    found = parent.find(f"{namespace}{name}")
    return re.sub(r"\s+", " ", found.text or "").strip() if found is not None else ""


def fetch_api_papers(arxiv_ids: list[str], refresh_cache: bool = False, chunk_size: int = 50) -> list[dict]:
    """Fetch metadata via arXiv API with conservative pacing + on-disk progress.

    - Smaller chunk_size reduces burstiness.
    - Cache is enabled at HTTP layer.
    - We also persist per-chunk parsed results so a later retry doesn't restart from 1/N.
    """
    os.makedirs(ANALYSIS_CACHE_DIR, exist_ok=True)
    progress_key = hashlib.sha256(("arxiv_api_progress|" + "|".join(arxiv_ids)).encode("utf-8")).hexdigest()[:16]
    progress_path = os.path.join(ANALYSIS_CACHE_DIR, f"api_papers_{progress_key}.jsonl")

    papers: list[dict] = []
    done_ids: set[str] = set()

    if os.path.exists(progress_path) and not refresh_cache:
        try:
            with open(progress_path, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    obj = json.loads(line)
                    pid = obj.get("id")
                    if pid and pid not in done_ids:
                        papers.append(obj)
                        done_ids.add(pid)
            if papers:
                print(f"[api] resume from progress cache: {len(papers)} papers", file=sys.stderr, flush=True)
        except Exception as e:
            print(f"[api] progress cache read failed; ignore: {e}", file=sys.stderr, flush=True)

    # Only fetch ids not yet recovered from progress
    remaining_ids = [pid for pid in arxiv_ids if pid not in done_ids]

    for start in range(0, len(remaining_ids), chunk_size):
        chunk = remaining_ids[start:start + chunk_size]
        params = urllib.parse.urlencode({
            "id_list": ",".join(chunk),
            "max_results": len(chunk),
        })
        url = f"{ARXIV_API}?{params}"
        print(f"[api] fetching metadata {start + 1}-{start + len(chunk)} of {len(remaining_ids)} (remaining)", file=sys.stderr, flush=True)
        data = http_get(url, timeout=120, cache=True, refresh_cache=refresh_cache)
        root = ET.fromstring(data)

        new_chunk_papers: list[dict] = []
        for entry in root.findall("{http://www.w3.org/2005/Atom}entry"):
            paper = parse_api_entry(entry)
            if paper.get("id") and paper["id"] not in done_ids:
                new_chunk_papers.append(paper)
                done_ids.add(paper["id"])

        if new_chunk_papers:
            with open(progress_path, "a", encoding="utf-8") as f:
                for p in new_chunk_papers:
                    f.write(json.dumps(p, ensure_ascii=False) + "\n")
            papers.extend(new_chunk_papers)

        # extra pacing between API calls to reduce 429 chance
        time.sleep(2)

    return papers


def numeric_arxiv_id(arxiv_id: str) -> tuple[int, int]:
    m = re.match(r"(\d{4})\.(\d+)", arxiv_id)
    return (int(m.group(1)), int(m.group(2))) if m else (0, 0)


def collect_cs_papers(target_date: str, refresh_cache: bool = False, max_abs_pages: int = 2000) -> list[dict]:
    candidate_ids = fetch_recent_cs_ids(target_date, refresh_cache=refresh_cache)
    from_recent = bool(candidate_ids)
    if not candidate_ids:
        # If the date has rolled out of /recent, use the monthly list but still only keep exact target-date papers.
        candidate_ids = fetch_month_cs_ids(target_date, refresh_cache=refresh_cache)
    print(f"[browse] discovered {len(candidate_ids)} CS candidate ids", file=sys.stderr, flush=True)
    if len(candidate_ids) > max_abs_pages:
        candidate_ids = candidate_ids[:max_abs_pages]
        print(f"[browse] stopped after {max_abs_pages} candidate ids", file=sys.stderr, flush=True)

    try:
        fetched = fetch_api_papers(candidate_ids, refresh_cache=refresh_cache)
    except Exception as e:
        print(f"[api] metadata fetch failed; falling back to abs pages: {e}", file=sys.stderr, flush=True)
        fetched = []
        for arxiv_id in candidate_ids:
            try:
                fetched.append(fetch_abs_paper(arxiv_id, refresh_cache=refresh_cache))
            except Exception as abs_e:
                print(f"[browse] abs failed for {arxiv_id}: {abs_e}", file=sys.stderr, flush=True)
                continue
            time.sleep(1)

    # If export API is flaky and we ended up with 0 for the day, try a more robust
    # fallback: take ids from the CS new submissions page and filter by the actual
    # "Submitted on" date parsed from /abs.
    if not fetched:
        try:
            fallback_ids = fetch_cs_new_ids(refresh_cache=refresh_cache)
            # keep the run bounded
            fallback_ids = fallback_ids[:400]
            print(f"[fallback] trying abs parse on {len(fallback_ids)} ids from cs/new", file=sys.stderr, flush=True)
            for arxiv_id in fallback_ids:
                try:
                    fetched.append(fetch_abs_paper(arxiv_id, refresh_cache=refresh_cache))
                except Exception:
                    continue
                time.sleep(0.05)
        except Exception as fb_e:
            print(f"[fallback] cs/new fallback failed: {fb_e}", file=sys.stderr, flush=True)

    papers = []
    for paper in fetched:
        published = paper.get("published", "")
        if from_recent or published == target_date:
            paper["categories"] = sorted(set(c for c in paper.get("categories", []) if c in CS_CATEGORIES))
            paper["primary_cs_category"] = primary_cs_category(paper)
            paper["related_keywords"] = extract_related_keywords(paper)
            papers.append(paper)

    papers = apply_relevance_filter(papers)
    papers.sort(key=lambda p: numeric_arxiv_id(p["id"]), reverse=True)
    print(f"[browse] matched {len(papers)} relevant CS papers submitted on {target_date}", file=sys.stderr, flush=True)
    return papers


def primary_cs_category(paper: dict) -> str:
    for category in paper.get("categories", []):
        if category in CS_CATEGORIES:
            return category
    return "cs.OH"


def extract_related_keywords(paper: dict, limit: int = 3) -> list[str]:
    text = f"{paper.get('title', '')} {paper.get('summary', '')}".lower()
    hits = []
    for keyword, terms in RELATED_KEYWORDS.items():
        if any(term_in_text(term, text) for term in terms):
            hits.append(keyword)
    if not hits:
        for category in paper.get("categories", []):
            if category in CS_CATEGORIES:
                hits.append(category)
                break
    return hits[:limit]


def domain_relevance_scores(paper: dict) -> dict[str, float]:
    title = paper.get("title", "")
    summary = paper.get("summary", "")
    title_l = title.lower()
    summary_l = summary.lower()
    raw_scores: dict[str, float] = {}
    for domain, terms in REPORT_DOMAIN_KEYWORDS.items():
        score = 0.0
        for term in terms:
            if term_in_text(term, title_l):
                score += 3.0
            if term_in_text(term, summary_l):
                score += 1.0
        raw_scores[domain] = score

    categories = set(paper.get("categories", []))
    if "cs.RO" in categories and (raw_scores.get("具身智能", 0) > 0 or raw_scores.get("机器人", 0) > 0):
        raw_scores["具身智能"] += 1.0
        raw_scores["机器人"] += 1.5
    if "cs.CL" in categories and raw_scores.get("大模型", 0) > 0:
        raw_scores["大模型"] += 1.5
    if "cs.LG" in categories and (raw_scores.get("强化学习", 0) > 0 or raw_scores.get("世界模型", 0) > 0):
        raw_scores["强化学习"] += 0.8
        raw_scores["世界模型"] += 0.8

    weighted_scores = {
        domain: raw_scores[domain] * REPORT_DOMAIN_WEIGHTS[domain]
        for domain in REPORT_DOMAINS
        if raw_scores.get(domain, 0) > 0
    }
    paper["domain_raw_scores"] = {domain: round(raw_scores[domain], 3) for domain in weighted_scores}
    paper["domain_weighted_scores"] = {domain: round(score, 3) for domain, score in weighted_scores.items()}
    return weighted_scores


def apply_relevance_filter(papers: list[dict], max_papers: int = MAX_DAILY_PAPERS) -> list[dict]:
    selected = []
    for paper in papers:
        scores = domain_relevance_scores(paper)
        if not scores:
            continue
        ranked = sorted(scores.items(), key=lambda kv: kv[1], reverse=True)
        paper["focus_domains"] = [domain for domain, _ in ranked]
        paper["primary_focus_domain"] = ranked[0][0]
        paper["relevance_score"] = round(sum(scores.values()), 3)
        selected.append(paper)
    selected.sort(key=lambda p: (p.get("relevance_score", 0), numeric_arxiv_id(p["id"])), reverse=True)
    if len(selected) > max_papers:
        print(f"[filter] kept top {max_papers} of {len(selected)} relevant papers", file=sys.stderr, flush=True)
    else:
        print(f"[filter] kept {len(selected)} relevant papers", file=sys.stderr, flush=True)
    return selected[:max_papers]


def focus_matches(paper: dict) -> list[str]:
    text = f"{paper.get('title', '')} {paper.get('summary', '')}".lower()
    matches = []
    for keyword, terms in REPORT_DOMAIN_KEYWORDS.items():
        if any(term_in_text(term, text) for term in terms):
            matches.append(keyword)
    return matches


def split_sentences(text: str) -> list[str]:
    if not text:
        return []
    parts = re.split(r"(?<=[.!?])\s+(?=[A-Z0-9])", re.sub(r"\s+", " ", text).strip())
    return [p.strip() for p in parts if p.strip()]


from typing import Optional, Set

def pick_sentence(sentences: list[str], needles: list[str], default_index: int = 0, avoid: Optional[Set[str]] = None) -> str:
    avoid = avoid or set()
    for sentence in sentences:
        if sentence in avoid:
            continue
        low = sentence.lower()
        if any(needle in low for needle in needles):
            return sentence
    for sentence in sentences:
        if sentence not in avoid:
            return sentence
    if not sentences:
        return ""
    return sentences[min(max(default_index, 0), len(sentences) - 1)]


def fetch_paper_fulltext_excerpt(paper_id: str, max_chars: int = 18000) -> str:
    try:
        html_text = http_get(
            f"https://arxiv.org/html/{paper_id}",
            timeout=45,
            max_retries=1,
            cache=True,
        ).decode("utf-8", errors="ignore")
    except Exception:
        return ""
    html_text = re.sub(r"<(script|style)[\s\S]*?</\1>", " ", html_text, flags=re.I)
    text = strip_tags(html_text)
    return text[:max_chars]


def analysis_cache_path(paper: dict) -> str:
    key = "|".join([
        ANALYSIS_PROMPT_VERSION,
        paper.get("id", ""),
        paper.get("updated", ""),
        paper.get("title", ""),
    ])
    digest = hashlib.sha256(key.encode("utf-8")).hexdigest()
    return os.path.join(ANALYSIS_CACHE_DIR, f"{digest}.json")


def parse_json_object(text: str) -> dict:
    match = re.search(r"~~~json\s*(\{[\s\S]*?\})\s*~~~", text)
    if match:
        text = match.group(1)
    else:
        start = text.find("{")
        end = text.rfind("}")
        text = text[start:end + 1] if start >= 0 and end > start else text
    try:
        data = json.loads(text)
        return data if isinstance(data, dict) else {}
    except json.JSONDecodeError:
        return {}


def daily_analysis_prompt(paper: dict, fulltext_excerpt: str) -> str:
    return f"""你是科研助理，正在为中文 arXiv 日报撰写论文分析。请基于论文标题、摘要和正文节选，输出适合直接放入日报的中文分析。

论文信息：
- arXiv ID: {paper.get('id', '')}
- 标题: {paper.get('title', '')}
- 作者: {', '.join(paper.get('authors', [])[:12])}
- 关注领域: {', '.join(paper.get('focus_domains', []))}
- arXiv 分类: {', '.join(paper.get('categories', []))}

英文摘要：
{paper.get('summary', '')}

正文节选：
{fulltext_excerpt[:18000] or '未获取到正文节选，只能依据摘要分析。'}

请只输出 JSON，不要加 Markdown 代码块。字段固定为：
背景与动机, 研究方法, 主要结果, abstract_cn

写作要求：
1. 全文使用中文。除模型名、数据集名、算法名、指标缩写、论文标题外，不要直接粘贴英文句子；英文摘要内容需要转述或翻译成中文。
2. 背景与动机：2-4 句，说明具体任务、应用场景、现有瓶颈、为什么这篇论文值得关注。
3. 研究方法：3-6 句，说明方法名称、核心模块、输入输出、训练/推理流程、模块之间如何连接；不要只写“提出框架/提升性能”。
4. 主要结果：2-4 句，说明实验环境/数据集/基线/指标/主要结论/消融或泛化发现。若节选中没有明确数值，写“可见文本未给出具体数值”，不能编造。
5. abstract_cn：完整摘要的中文翻译，保留必要术语但不要删减关键信息。
"""


def valid_analysis(data: dict) -> bool:
    return all(isinstance(data.get(k), str) and data[k].strip() for k in ["背景与动机", "研究方法", "主要结果"])


def has_llm_provider() -> bool:
    return any(os.environ.get(name) for name in ["MINIMAX_API_KEY", "POE_API_KEY", "OPENAI_API_KEY"])


def write_analysis_cache(cpath: str, data: dict) -> None:
    os.makedirs(ANALYSIS_CACHE_DIR, exist_ok=True)
    with open(cpath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def openai_daily_analysis(paper: dict, fulltext_excerpt: str, cpath: str) -> dict:
    api_key = os.environ.get("OPENAI_API_KEY", "")
    if not api_key:
        return {}
    payload = {
        "model": OPENAI_MODEL,
        "temperature": 0.2,
        "response_format": {"type": "json_object"},
        "messages": [{"role": "user", "content": daily_analysis_prompt(paper, fulltext_excerpt)}],
    }
    req = urllib.request.Request(
        OPENAI_CHAT_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        parsed = parse_json_object(content)
        if valid_analysis(parsed):
            parsed["provider"] = "openai"
            write_analysis_cache(cpath, parsed)
            return parsed
    except Exception as e:
        print(f"[analysis] openai failed for {paper.get('id')}: {e}", file=sys.stderr, flush=True)
    return {}


def poe_daily_analysis(paper: dict, fulltext_excerpt: str, cpath: str) -> dict:
    api_key = os.environ.get("POE_API_KEY", "")
    if not api_key:
        return {}
    payload = {
        "model": POE_MODEL,
        "max_tokens": 3500,
        "temperature": 0.2,
        "messages": [{"role": "user", "content": daily_analysis_prompt(paper, fulltext_excerpt)}],
    }
    req = urllib.request.Request(
        POE_CHAT_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        content = data.get("choices", [{}])[0].get("message", {}).get("content", "")
        parsed = parse_json_object(content)
        if valid_analysis(parsed):
            parsed["provider"] = "poe"
            write_analysis_cache(cpath, parsed)
            return parsed
    except Exception as e:
        print(f"[analysis] poe failed for {paper.get('id')}: {e}", file=sys.stderr, flush=True)
    return {}


def minimax_daily_analysis(paper: dict, fulltext_excerpt: str, mode: str = "auto") -> dict:
    if mode == "heuristic":
        return {}

    cpath = analysis_cache_path(paper)
    if os.path.exists(cpath):
        try:
            with open(cpath, "r", encoding="utf-8") as f:
                cached = json.load(f)
            if valid_analysis(cached):
                return cached
        except Exception:
            pass

    prompt = daily_analysis_prompt(paper, fulltext_excerpt)
    api_key = os.environ.get("MINIMAX_API_KEY", "")
    if not api_key:
        return poe_daily_analysis(paper, fulltext_excerpt, cpath) or openai_daily_analysis(paper, fulltext_excerpt, cpath)
    payload = {
        "model": MINIMAX_MODEL,
        "max_tokens": 3500,
        "messages": [{"role": "user", "content": prompt}],
    }
    req = urllib.request.Request(
        MINIMAX_API_URL,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    )
    try:
        with urllib.request.urlopen(req, timeout=180) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        blocks = data.get("content", [])
        content = "\n".join(
            block.get("text", "")
            for block in blocks
            if isinstance(block, dict) and block.get("type") == "text"
        ).strip()
        if not content and blocks and isinstance(blocks[0], dict):
            content = blocks[0].get("text", "")
        parsed = parse_json_object(content)
        if valid_analysis(parsed):
            parsed["provider"] = "minimax"
            write_analysis_cache(cpath, parsed)
            return parsed
    except Exception as e:
        print(f"[analysis] llm failed for {paper.get('id')}: {e}", file=sys.stderr, flush=True)
    return poe_daily_analysis(paper, fulltext_excerpt, cpath) or openai_daily_analysis(paper, fulltext_excerpt, cpath)


def evidence_sentence(sentences: list[str], needles: list[str], fallback_index: int = 0) -> str:
    sentence = pick_sentence(sentences, needles, fallback_index)
    if len(sentence) > 380:
        sentence = sentence[:380].rsplit(" ", 1)[0] + "..."
    return sentence


def cn_brief(paper: dict, fulltext_excerpt: str = "") -> dict:
    abstract = re.sub(r"\s+", " ", paper.get("summary", "")).strip()
    analysis_text = re.sub(r"\s+", " ", f"{abstract} {fulltext_excerpt}").strip()
    low = analysis_text.lower()
    title = paper.get("title", "该论文")
    category = paper.get("primary_cs_category") or primary_cs_category(paper)
    category_name = CS_CATEGORIES.get(category, category)
    domains = "、".join(paper.get("focus_domains", [])[:3])
    keywords = domains or "、".join(paper.get("related_keywords", [])[:3]) or category_name
    sentences = split_sentences(analysis_text)
    abstract_sentences = split_sentences(abstract)

    pain_points = []
    for term, zh in [
        ("challenge", "现有方法仍面临挑战"),
        ("difficult", "任务本身具有较高难度"),
        ("limited", "现有方法存在能力或适用范围限制"),
        ("lack", "相关基准、数据或方法仍不充分"),
        ("cost", "系统成本或推理开销是关键约束"),
        ("real-time", "实时应用对效率提出要求"),
        ("robust", "鲁棒性和泛化能力是核心问题"),
    ]:
        if term in low:
            pain_points.append(zh)
    if not pain_points:
        pain_points.append(f"该工作聚焦 {category_name} 方向中的具体问题")
    problem_evidence = evidence_sentence(
        abstract_sentences or sentences,
        ["challenge", "limited", "lack", "bottleneck", "difficult", "however", "remain", "struggle"],
        0,
    )

    method_bits = []
    for term, zh in [
        ("benchmark", "构建或使用基准评测体系"),
        ("dataset", "引入数据集或数据收集流程"),
        ("we propose", "提出新的模型、框架或算法"),
        ("we present", "给出系统化方法或工具"),
        ("framework", "设计端到端框架"),
        ("transformer", "使用 Transformer/基础模型结构"),
        ("agent", "引入智能体式建模或搜索"),
        ("policy", "围绕策略学习或控制策略展开"),
        ("optimization", "使用优化建模或搜索过程"),
    ]:
        if term in low:
            method_bits.append(zh)
    if not method_bits:
        method_bits.append("围绕论文提出的建模、算法或系统设计进行实验验证")
    method_evidence = evidence_sentence(
        sentences,
        ["we propose", "we present", "introduce", "framework", "model", "method", "architecture", "training", "optimization"],
        1 if len(sentences) > 1 else 0,
    )

    result_bits = []
    for term, zh in [
        ("outperform", "相对已有方法取得更好表现"),
        ("improve", "在目标指标上带来改进"),
        ("achieve", "达到作者报告的目标性能"),
        ("show", "实验或分析展示了方法有效性"),
        ("demonstrate", "结果验证了方案可行性"),
        ("evaluate", "通过评测分析了方法表现"),
        ("robust", "关注鲁棒性或泛化表现"),
    ]:
        if term in low:
            result_bits.append(zh)
    if not result_bits:
        result_bits.append("可见文本中未给出明确实验数字或完整对比表")
    result_evidence = evidence_sentence(
        sentences,
        ["outperform", "improve", "achieve", "show", "demonstrate", "evaluate", "benchmark", "result", "%", "accuracy", "performance"],
        max(len(abstract_sentences) - 1, 0),
    )

    datasets = sorted(set(re.findall(r"\b[A-Z][A-Za-z0-9_-]*(?:Bench|Set|Net|World|Gym|Sim|QA|Eval|VLA|RL|DROID|Habitat|Meta-World|CALVIN|LIBERO)\b", analysis_text)))
    dataset_text = f" 可见文本中出现的评测对象/数据集包括：{', '.join(datasets[:6])}。" if datasets else " 可见文本未明确列出完整数据集名称。"

    return {
        "背景与动机": (
            f"《{title}》归入 {keywords} 方向。该论文围绕 {category_name} 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。"
            f"从摘要和可见正文判断，研究动机主要来自：{dedupe_join(pain_points)}。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。"
        ),
        "研究方法": (
            f"方法上，论文主要涉及：{dedupe_join(method_bits)}。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，"
            f"以及这些模块如何服务于 {keywords} 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。"
        ),
        "主要结果": (
            f"实验结果方面，可见文本显示：{dedupe_join(result_bits)}。{dataset_text} "
            f"如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。"
        ),
        "abstract": abstract,
    }


def dedupe_join(items: list[str]) -> str:
    uniq = []
    for item in items:
        if item not in uniq:
            uniq.append(item)
    return "；".join(uniq[:3])


def try_fetch_main_figure(assets_dir: str, paper_id: str) -> str:
    try:
        html_url = f"https://arxiv.org/html/{paper_id}"
        html_text = http_get(html_url, timeout=45, max_retries=1, cache=True).decode("utf-8", errors="ignore")
        src = ""
        for figure_m in FIGURE_RE.finditer(html_text):
            img_m = IMG_RE.search(figure_m.group(0))
            if img_m:
                src = img_m.group(1)
                break
        if not src:
            return fetch_first_page_image(assets_dir, paper_id)
        if src.startswith("//"):
            src = "https:" + src
        elif src.startswith("/"):
            src = "https://arxiv.org" + src
        elif not src.startswith("http"):
            src = f"https://arxiv.org/html/{src}"
        ext = os.path.splitext(urllib.parse.urlparse(src).path)[1] or ".jpg"
        fname = f"{paper_id.replace('/', '_')}_figure{ext}"
        os.makedirs(assets_dir, exist_ok=True)
        out_path = os.path.join(assets_dir, fname)
        if not os.path.exists(out_path):
            data = http_get(src, timeout=45, max_retries=1, cache=True)
            with open(out_path, "wb") as f:
                f.write(data)
        return os.path.join("assets", fname)
    except Exception:
        return fetch_first_page_image(assets_dir, paper_id)


def fetch_first_page_image(assets_dir: str, paper_id: str) -> str:
    try:
        import fitz  # type: ignore

        os.makedirs(assets_dir, exist_ok=True)
        fname = f"{paper_id.replace('/', '_')}_first_page.png"
        out_path = os.path.join(assets_dir, fname)
        if not os.path.exists(out_path):
            data = http_get(f"https://arxiv.org/pdf/{paper_id}", timeout=60, max_retries=1, cache=True)
            doc = fitz.open(stream=data, filetype="pdf")
            try:
                page = doc[0]
                pix = page.get_pixmap(matrix=fitz.Matrix(1.5, 1.5), alpha=False)
                pix.save(out_path)
            finally:
                doc.close()
        return os.path.join("assets", fname)
    except Exception:
        return ""


def paper_lines(paper: dict, daily_dir: str, max_figures: int, figure_state: dict, analysis_mode: str) -> list[str]:
    fulltext_excerpt = fetch_paper_fulltext_excerpt(paper["id"])
    brief = minimax_daily_analysis(paper, fulltext_excerpt, analysis_mode) or cn_brief(paper, fulltext_excerpt)
    fig_rel = ""
    if max_figures < 0 or figure_state["count"] < max_figures:
        fig_rel = try_fetch_main_figure(os.path.join(daily_dir, "assets"), paper["id"])
        figure_state["count"] += 1
    abstract_text = brief.get("abstract_cn") or brief.get("abstract") or paper.get("summary", "")
    escaped_abstract = html.escape(abstract_text, quote=False)
    domains = paper.get("focus_domains", [])
    primary_domain = paper.get("primary_focus_domain") or (domains[0] if domains else "未标注")
    weighted_scores = paper.get("domain_weighted_scores", {})
    weighted_text = "，".join(
        f"{domain} {weighted_scores[domain]:.2f}".rstrip("0").rstrip(".")
        for domain in REPORT_DOMAINS
        if weighted_scores.get(domain, 0) > 0
    ) or "无"

    lines = [
        f"### {analysis_note_link(paper)}",
        "",
    ]
    if fig_rel:
        lines.extend([f"![[{fig_rel}|800]]", ""])
    else:
        lines.extend(["> 主图未能自动提取，需后续人工补图。", ""])
    lines.extend([
        f"- **arXiv**: [{paper['id']}]({paper['abs']})",
        f"- **PDF**: {paper['pdf']}",
        f"- **详细分析**: {analysis_note_link(paper)}",
        f"- **作者**: {', '.join(paper.get('authors', [])[:12])}{'...' if len(paper.get('authors', [])) > 12 else ''}",
        f"- **cs 子类**: {', '.join(paper.get('categories', []))}",
        f"- **归属领域**: {primary_domain}",
        f"- **相关领域**: {', '.join(domains) if domains else '未标注'}",
        f"- **相关性评分**: {paper.get('relevance_score', 0)}（加权：{weighted_text}）",
        f"- **关联关键词**: {', '.join(paper.get('related_keywords', [])) or '未提取到'}",
        "",
        "#### 研究背景与动机",
        "",
        brief["背景与动机"],
        "",
        "#### 方法概述和架构",
        "",
        brief["研究方法"],
        "",
        "#### 实验结果分析",
        "",
        brief["主要结果"],
        "",
        "<details>",
        "<summary>完整摘要</summary>",
        "",
        escaped_abstract,
        "",
        "</details>",
        "",
    ])
    return lines


def write_markdown(path: str, lines: list[str]) -> None:
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines).rstrip() + "\n")


def write_papers_json(daily_dir: str, target_date: str, papers: list[dict]) -> str:
    path = os.path.join(daily_dir, f"papers_{target_date}.json")
    payload = {
        "date": target_date,
        "generated_at": dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).isoformat(),
        "count": len(papers),
        "papers": papers,
    }
    os.makedirs(daily_dir, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=2)
    return path


def write_empty_report(daily_dir: str, target_date: str) -> str:
    path = os.path.join(daily_dir, f"Daily_arxiv_report_{target_date}.md")
    lines = [
        f"# 每日 arXiv CS 论文简报 | {target_date}",
        "",
        "#arxiv #daily #ComputerScience",
        "",
        f"**生成时间**: {dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')}（Asia/Shanghai）",
        "",
        "## 情况说明",
        "",
        f"- 未检索到 {target_date} 在目标领域（{', '.join(REPORT_DOMAINS)}）中的高相关新增论文。",
        "- 按当前规则不保留完全不相关论文，也不回填更早日期论文，因此本日只生成情况说明。",
        "",
    ]
    write_markdown(path, lines)
    return path


def build_reports(target_date: str, papers: list[dict], out_dir: str, max_figures: int, analysis_mode: str) -> str:
    daily_dir = os.path.join(out_dir, "10_Daily", target_date)
    os.makedirs(daily_dir, exist_ok=True)
    write_papers_json(daily_dir, target_date, papers)
    if not papers:
        return write_empty_report(daily_dir, target_date)

    by_category: dict[str, list[dict]] = {}
    for paper in papers:
        by_category.setdefault(paper["primary_cs_category"], []).append(paper)

    figure_state = {"count": 0}
    index_lines = [
        f"# 每日 arXiv CS 论文简报 | {target_date}",
        "",
        "#arxiv #daily #ComputerScience",
        "",
        f"**生成时间**: {dt.datetime.now(dt.timezone(dt.timedelta(hours=8))).strftime('%Y-%m-%d %H:%M')}（Asia/Shanghai）",
        f"**论文总数**: {len(papers)}",
        "",
        "## cs 子分类文件",
        "",
    ]

    for category in sorted(by_category):
        plist = by_category[category]
        filename = f"{category}_{safe_filename(CS_CATEGORIES.get(category, category))}.md"
        index_lines.append(f"- [[{filename[:-3]}|{category} {CS_CATEGORIES.get(category, '')}]]：{len(plist)} 篇")
        lines = [
            f"# {category} | {CS_CATEGORIES.get(category, category)} | {target_date}",
            "",
            "#arxiv #ComputerScience",
            "",
            f"**论文数**: {len(plist)}",
            "",
        ]
        for paper in plist:
            lines.extend(paper_lines(paper, daily_dir, max_figures, figure_state, analysis_mode))
            lines.append("---")
            lines.append("")
        write_markdown(os.path.join(daily_dir, filename), lines)

    index_lines.extend(["", "## 关键词专题", "", "- [[重点关键词论文汇总|重点关键词论文汇总]]", ""])
    index_path = os.path.join(daily_dir, f"Daily_arxiv_report_{target_date}.md")
    write_markdown(index_path, index_lines)
    write_focus_report(daily_dir, target_date, papers, max_figures, figure_state, analysis_mode)
    return index_path


def write_focus_report(daily_dir: str, target_date: str, papers: list[dict], max_figures: int, figure_state: dict, analysis_mode: str) -> None:
    matches: dict[str, list[dict]] = {k: [] for k in REPORT_DOMAINS}
    for paper in papers:
        domain = paper.get("primary_focus_domain") or (paper.get("focus_domains") or [""])[0]
        if domain in matches:
            matches[domain].append(paper)

    lines = [
        f"# 重点关键词论文汇总 | {target_date}",
        "",
        "#arxiv #daily #重点论文",
        "",
        "覆盖关键词：大模型、具身智能、强化学习、世界模型、机器人。",
        "",
        "说明：每篇论文只归入加权分最高的一个领域，避免跨领域重复收录；其他命中领域保留在论文条目的“相关领域”字段中。",
        "",
    ]
    if not any(matches.values()):
        lines.extend(["## 情况说明", "", "- 今日 CS 新增论文中未检索到与指定关键词强相关的论文。", ""])
    for keyword, plist in matches.items():
        lines.extend([f"## {keyword}（{len(plist)}篇）", ""])
        if not plist:
            lines.extend(["- 未检索到强相关论文。", ""])
            continue
        for paper in plist:
            lines.extend(paper_lines(paper, daily_dir, max_figures, figure_state, analysis_mode))
            lines.append("---")
            lines.append("")
    write_markdown(os.path.join(daily_dir, "重点关键词论文汇总.md"), lines)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--date", help="target arXiv submission date YYYY-MM-DD (default: yesterday Beijing date)")
    ap.add_argument("--out", default=ROOT_DIR, help="output root")
    ap.add_argument("--refresh-cache", action="store_true", help="ignore cached arXiv HTML responses")
    ap.add_argument("--max-abs-pages", type=int, default=2000, help="max abs pages to inspect")
    ap.add_argument("--max-figures", type=int, default=-1, help="max figures to fetch; -1 means all included papers, 0 skips")
    ap.add_argument(
        "--analysis-mode",
        choices=["auto", "llm", "heuristic"],
        default=os.environ.get("DAILY_ARXIV_ANALYSIS_MODE", "auto"),
        help="auto uses MiniMax when MINIMAX_API_KEY is available; heuristic never calls LLM",
    )
    args = ap.parse_args()

    bj_tz = dt.timezone(dt.timedelta(hours=8))
    target_date = args.date or (dt.datetime.now(bj_tz).date() - dt.timedelta(days=1)).isoformat()
    print(f"[arxiv] target arXiv CS announcement date {target_date}", file=sys.stderr, flush=True)

    papers = collect_cs_papers(target_date, refresh_cache=args.refresh_cache, max_abs_pages=args.max_abs_pages)
    if args.analysis_mode in {"auto", "llm"} and not has_llm_provider():
        print("[analysis] no LLM API key found; falling back to heuristic Chinese summaries", file=sys.stderr, flush=True)
    report_path = build_reports(target_date, papers, args.out, args.max_figures, args.analysis_mode)
    print(f"[arxiv] wrote {len(papers)} papers", file=sys.stderr, flush=True)
    print(report_path)


if __name__ == "__main__":
    main()
