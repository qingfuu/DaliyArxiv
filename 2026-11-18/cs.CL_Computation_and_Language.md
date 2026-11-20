# cs.CL | Computation and Language | 2026-11-18

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/LMMR_Learned_Multigranular_Memory_Retrieval_for_Small_Language_Model_Agents|LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents]]

![[assets/2611.22425_first_page.png|800]]

- **arXiv**: [2611.22425](https://arxiv.org/abs/2611.22425)
- **PDF**: https://arxiv.org/pdf/2611.22425
- **详细分析**: [[20_Research/Papers/大模型/LMMR_Learned_Multigranular_Memory_Retrieval_for_Small_Language_Model_Agents|LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents]]
- **作者**: Pengfeng Song, Yunkai Zhuang, Liye Shi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LMMR: Learned Multigranular Memory Retrieval for Small Language Model Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HotpotQA, LongBench, LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small language model agents have limited space to read the memory needed for multi-hop questions. Relevant facts are often scattered across records whose surrounding text consumes much of that space. We propose LMMR, a learned multigranular memory retrieval method that selects both the next source and how much of it to read. LMMR links paragraphs and sentence fragments to their original sources and pairs views that supply the same missing support during training. Relevant distractors and repeated information provide contrasting examples. At inference, the reranker scores what each candidate adds to an anchor passage, and a selector chooses the evidence within a token budget. On 22,398 official validation questions from HotpotQA, 2WikiMultihopQA, and MuSiQue, a frozen 2B answer model reaches 61.47, 43.26, and 30.58 F1 under a 400-token budget. The gains over query expansion are 3.06, 2.14, and 4.55 points, while memory input decreases by 23.1-26.9%. LMMR also uses 23.5-27.7% fewer input tokens than a coarse retriever trained on the same questions. Against that retriever followed by LLMLingua-2 at comparable input lengths, F1 gains reach 3.99 points and are significant on HotpotQA and 2WikiMultihopQA after Holm correction. All eight small answer models evaluated on HotpotQA improve over query expansion and MMR in both F1 and exact match.

</details>

---

### [[20_Research/Papers/具身智能/Bad_Apples_in_the_Kitchen_How_LLM_Teams_Detect,_Correct,_and_Calibrate_Against_Their_Misaligned_Members|Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members]]

![[assets/2611.22342_figure.png|800]]

- **arXiv**: [2611.22342](https://arxiv.org/abs/2611.22342)
- **PDF**: https://arxiv.org/pdf/2611.22342
- **详细分析**: [[20_Research/Papers/具身智能/Bad_Apples_in_the_Kitchen_How_LLM_Teams_Detect,_Correct,_and_Calibrate_Against_Their_Misaligned_Members|Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members]]
- **作者**: Dongseok Heo, Junghwan Kim, Bongwon Suh
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.15（加权：具身智能 0.3，大模型 0.85）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Bad Apples in the Kitchen: How LLM Teams Detect, Correct, and Calibrate Against Their Misaligned Members》归入 大模型、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

What protects an LLM team when one teammate quietly goes wrong? Most multi-agent LLM work assumes cooperative partners and inspects chat between turns before acting. Real-time embodied cooperation does not allow this pause: chat runs alongside action, so a teammate whose words stay cooperative while behavior diverges can cause damage faster than the team can name what is happening. We study this case by injecting three theory-grounded misaligned agents into a custom four-player Overcooked environment, each stressing a different joint-action layer (speech-action mismatch, role invasion, and aggregate-progress disruption), and decompose robustness into three sequential gates of detection, correction, and calibration through a 3x4x2 design (n=720 episodes). Nearly all trolls are eventually named, but recovery follows only when attribution and situational diagnosis appear in the same utterance; direct source-attribution prompting improves the hardest case only by degrading the troll-free baseline by 37.5%. Robustness, then, depends less on detection alone than on whether team chat combines attribution with diagnosis in a single utterance, suggesting that sensitivity to misalignment should be targeted rather than uniformly raised.

</details>

---
