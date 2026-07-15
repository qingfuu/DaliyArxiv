# cs.CR | Cryptography and Security | 2026-07-13

#arxiv #ComputerScience

**论文数**: 5

### [[20_Research/Papers/大模型/SherAgent_Scaling_Attack_Investigation_in_the_Wild_via_LLM-Empowered_Iterative_Query-Filter_Backtracking|SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking]]

![[assets/2607.09176_figure.png|800]]

- **arXiv**: [2607.09176](https://arxiv.org/abs/2607.09176)
- **PDF**: https://arxiv.org/pdf/2607.09176
- **详细分析**: [[20_Research/Papers/大模型/SherAgent_Scaling_Attack_Investigation_in_the_Wild_via_LLM-Empowered_Iterative_Query-Filter_Backtracking|SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking]]
- **作者**: Zhenyuan Li, Zhengkai Wang, Ling Jiang, Xiangmin Shen, Ruixiao Lin, Sen Nie, Shi Wu, Shouling Ji
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《SherAgent: Scaling Attack Investigation in the Wild via LLM-Empowered Iterative Query-Filter Backtracking》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Provenance-based attack investigation enables viable automation by standardizing data and query logic; however, it is critically hindered in practice by dependency explosions and fragmented causal chains in the wild. Towards designing a robust and automated investigation tool, we collaborated with the SOC of a major Internet corporation serving billions of users. By engaging in real-world incident response, we are able to evaluate and refine their existing LLM-based investigation workflows, which processes tens of thousands of raw alerts daily, leaving thousands for manual triage, to find out the root causes of investigation failures and major challenges in their existing tools. Motivated by these findings, we propose SherAgent, an LLM-empowered automated investigation system. Operating on an iterative ``query-filter'' backtracking paradigm over provenance graphs, SherAgent leverages the semantic reasoning capabilities of LLMs to process unstructured data, such as investigation context and threat intelligence. To overcome fragmented causal chains caused by missing events, the system dynamically calibrates query conditions to broaden the search scope. Concurrently, it performs precision result filtering and strategic nodes selection for subsequent exploration, thereby mitigating dependency explosions. Extensive evaluations in the wild demonstrate that SherAgent improves the end-to-end investigation success rate by 31.1% and 63.7% compared to both legacy enterprise baselines and SOTA approaches, respectively. Furthermore, it operates with remarkable efficiency, incurring under $0.10 in API costs and requiring less than 4 minutes per investigation. Finally, our user study confirms that SherAgent provides accurate and clear insights, significantly reducing the analytical overhead for security experts.

</details>

---

### [[20_Research/Papers/大模型/SLBench_Evaluating_How_LLM_Agents_Follow_Logical_Relations_in_Skills|SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills]]

![[assets/2607.09016_figure.png|800]]

- **arXiv**: [2607.09016](https://arxiv.org/abs/2607.09016)
- **PDF**: https://arxiv.org/pdf/2607.09016
- **详细分析**: [[20_Research/Papers/大模型/SLBench_Evaluating_How_LLM_Agents_Follow_Logical_Relations_in_Skills|SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills]]
- **作者**: Xuan Chen, Chengpeng Wang, Lu Yan, Xiangyu Zhang
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《SLBench: Evaluating How LLM Agents Follow Logical Relations in Skills》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SLBench, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent skills extend LLM agents with reusable procedures, tools, and domain-specific workflows, but their safety depends on resolving dependencies among interacting instructions. We introduce SkillLogic, a framework for analyzing logical relations in skill files and constructing executable tests from them. Our taxonomy covers eight relation types, including preconditions that gate valid actions, constraints that limit how allowed actions may be performed, and fallbacks that specify recovery behavior after failure. Using SkillLogic, we scan over 5000 public skills and find that 70% contain at least one logical relation. We then construct SLBench, an 86-case executable benchmark from high-confidence, high-impact, and locally testable relations. Evaluating Codex and Claude Code across six LLM backbones shows unsafe rates up to 70%, with violations leading to privacy leaks, unsafe configuration changes, and incomplete cleanup. The human audit attributes failures to both agent capability gaps and low-salience skill text. We further show that SLGuard, a lightweight inference-time scaffold, reduces violations by 63% on targeted cases. Our results establish logical-relation following as a distinct reliability challenge for skill-guided agents.

</details>

---

### [[20_Research/Papers/大模型/Secret_Scanner_Agent_Extracting_Secrets_and_Access_Context_from_Unstructured_Documents|Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents]]

![[assets/2607.09011_figure.png|800]]

- **arXiv**: [2607.09011](https://arxiv.org/abs/2607.09011)
- **PDF**: https://arxiv.org/pdf/2607.09011
- **详细分析**: [[20_Research/Papers/大模型/Secret_Scanner_Agent_Extracting_Secrets_and_Access_Context_from_Unstructured_Documents|Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents]]
- **作者**: Zixiao Chen, Mariko Wakabayashi, Charlotte Siska
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Secret Scanner Agent: Extracting Secrets and Access Context from Unstructured Documents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exposed documents such as emails, chat threads, tickets, and incident notes routinely leak credentials, but during incident response a leaked secret is only half the story. Responders also need to identify the ``door'' the secret opens: the account, tenant, endpoint, database, cloud resource, or other system that the credential could allow an attacker to access. Traditional secret scanners rely on regular expressions or trained classifiers which work well on well-formatted code, yet they struggle when a credential is fragmented, reformatted, or far from the resource it unlocks, and they report the secret string without naming what it opens. We present Secret Scanner Agent (SSA), a multi-agent large-language-model system that extracts both the secret and its associated door, together with supporting evidence, from unstructured exposed documents. SSA pairs a detection agent that favors recall with a review agent that filters false positives and recovers missing context. Because real credential data is sensitive, we evaluate SSA on synthetic benchmarks we generated that span 23 secret types and multiple document formats, scored with a three-step pipeline of programmatic matching, an LLM judge, and human review. Across six models, multi-agent SSA improves extraction precision over a single-agent variant, with the largest gains on door extraction, by up to 16 percentage points. SSA matches a regular-expression scanner's precision while more than tripling its recall, and against thirteen security analysts it is more precise, recovers nearly twice as many secret--door pairs, and runs five to seventeen times faster. By returning the secret, its door, and supporting evidence in one result, SSA turns credential detection into an actionable finding for triage and remediation.

</details>

---

### [[20_Research/Papers/大模型/SeedSmith_LLM-Driven_Seed_Synthesis_for_Directed_Fuzzing|SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing]]

![[assets/2607.08949_figure.png|800]]

- **arXiv**: [2607.08949](https://arxiv.org/abs/2607.08949)
- **PDF**: https://arxiv.org/pdf/2607.08949
- **详细分析**: [[20_Research/Papers/大模型/SeedSmith_LLM-Driven_Seed_Synthesis_for_Directed_Fuzzing|SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing]]
- **作者**: Junmin Zhu, Siyu Liu, Jie Hu, Fabio Gritti, Ati Priya Bajaj, Hulin Wang, Wenbo Guo, Tiffany Bao, Christopher Kruegel, Giovanni Vigna
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《SeedSmith: LLM-Driven Seed Synthesis for Directed Fuzzing》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Directed fuzzing steers fuzzers toward user-defined sink functions to identify vulnerabilities, but it frequently fails to trigger crashes even after long campaigns. We identify two challenges that prevent directed fuzzers from exposing crashes: incomplete static analysis of indirect calls, which leaves reachable paths invisible to distance-based guidance, and lack of semantic guidance for crash preconditions, which blind mutation cannot satisfy within practical time budgets. A natural intervention point is the initial seed corpus: seeds that encode the right control-flow path and satisfy key crash preconditions shift fuzzing from blind exploration to local refinement. Existing seed generation approaches address neither: grammar-based and format-driven methods produce structurally valid inputs with no sink awareness, while LLM-based methods either lack sink targeting or inherit static analysis limitations through one-shot prompting. We present SeedSmith, an agentic LLM pipeline that replicates a security analyst's workflow: starting from a sink, it iteratively explores the codebase, resolves indirect calls, identifies crash preconditions, and synthesizes concrete inputs that satisfy them. Because SeedSmith operates as a seed generation front-end, its seeds are fuzzer-agnostic and improve any downstream mutation-based fuzzer without modification. On Magma, fuzzers using SeedSmith seeds achieve geometric mean crash-time speedups of 11.51 times (AFL++) to 14.66 times (AFLGo) over default seeds. On ARVO, SeedSmith enables fuzzers to trigger 16 previously unreachable bugs spanning 10 projects with diverse input formats.

</details>

---

### [[20_Research/Papers/其他/Proof-of-Continuity_A_Temporal_Model_for_Authority_Propagation_in_Distributed_Systems_and_AI_Agents|Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents]]

![[assets/2607.08906_first_page.png|800]]

- **arXiv**: [2607.08906](https://arxiv.org/abs/2607.08906)
- **PDF**: https://arxiv.org/pdf/2607.08906
- **详细分析**: [[20_Research/Papers/其他/Proof-of-Continuity_A_Temporal_Model_for_Authority_Propagation_in_Distributed_Systems_and_AI_Agents|Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents]]
- **作者**: Nicola Gallo
- **cs 子类**: cs.CR, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Proof-of-Continuity: A Temporal Model for Authority Propagation in Distributed Systems and AI Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proof-of-Possession authorization models derive authority from the possession of artifacts such as tokens, credentials, or capabilities. This paper argues that possession is insufficient for discrete execution chains, whether they span multiple services or occur as separated steps within the same machine, because it does not guarantee preservation of the causal relationship between the origin of a request and the authority exercised at later steps. We introduce Proof-of-Continuity, a minimal authority-propagation discipline for the Provenance Identity Continuity (PIC) model, in which each execution step must be causally linked to the previous step and may only propagate a non-expansive subset of the authority received from the origin. It introduces Proof of Relationship, a single-hop causal primitive whose transitive composition is Proof-of-Continuity; these complement Proof-of-Possession rather than replace it. Under this model, the confused deputy condition cannot be satisfied as valid model behavior: any privilege exercised at a later step must already be present in the origin authority context. This is directly relevant to distributed systems and AI agents, where executors invoke tools and downstream services while holding multiple authority sources, so that the same authority/causality mismatch recurs across service boundaries. Under Proof-of-Continuity these sources may be carried together but are never merged into a combined authority, since each step is authorized only against the authority context of the lineage that caused it. This paper concerns authorization propagation rather than authentication: identity and authentication mechanisms such as OIDC, verifiable credentials, wallets, and workload identity remain complementary mechanisms for establishing the origin, while Proof-of-Continuity addresses how authority propagates after that origin exists.

</details>

---
