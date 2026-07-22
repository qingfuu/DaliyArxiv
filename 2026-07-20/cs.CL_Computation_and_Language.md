# cs.CL | Computation and Language | 2026-07-20

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/From_Plausible_to_Actionable_A_Position_on_LLM_Self-Explanations|From Plausible to Actionable: A Position on LLM Self-Explanations]]

![[assets/2607.15957_first_page.png|800]]

- **arXiv**: [2607.15957](https://arxiv.org/abs/2607.15957)
- **PDF**: https://arxiv.org/pdf/2607.15957
- **详细分析**: [[20_Research/Papers/大模型/From_Plausible_to_Actionable_A_Position_on_LLM_Self-Explanations|From Plausible to Actionable: A Position on LLM Self-Explanations]]
- **作者**: Elize Herrewijnen, Benedetta Muscato, Gizem Gezici, Fosca Giannotti
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《From Plausible to Actionable: A Position on LLM Self-Explanations》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) can generate natural language explanations that rationalize their own decisions, a phenomenon commonly referred to as self-explanations.Such explanations have emerged as a promising direction for explainable artificial intelligence (XAI), particularly for interpreting LLM behavior.However, while self-explanations often appear plausible, whether they faithfully reflect a model's underlying reasoning process remains an open question. In this opinion paper, we argue that self-explanations can be highly plausible, questionably faithful, and yet highly actionable. From a traditional XAI perspective, we identify the limitations of standard evaluation protocols for LLM-generated self-explanations and propose practical guidelines for assessing their plausibility and faithfulness. Moreover, we argue that evaluation should extend beyond these criteria to actionability, highlighting applications of LLM rationalization capabilities that support informed decision-making and appropriate action across diverse stakeholders.

</details>

---

### [[20_Research/Papers/大模型/SkillCorpus_Consolidating_and_Evaluating_the_Open_Skill_Ecosystem_for_Real-World_LLM_Agents|SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents]]

![[assets/2607.15557_figure.png|800]]

- **arXiv**: [2607.15557](https://arxiv.org/abs/2607.15557)
- **PDF**: https://arxiv.org/pdf/2607.15557
- **详细分析**: [[20_Research/Papers/大模型/SkillCorpus_Consolidating_and_Evaluating_the_Open_Skill_Ecosystem_for_Real-World_LLM_Agents|SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents]]
- **作者**: Yanze Wang, Pengfei Yao, Tianyi Sun, Chuanrui Hu, Yan Xiao, Yunyun Han, Jun Sun, Yafeng Deng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SkillCorpus: Consolidating and Evaluating the Open Skill Ecosystem for Real-World LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：QwenClawBench, Real-World, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent skills, SKILL.md files that package reusable procedural knowledge for an LLM agent, are a popular mechanism for extending agent capabilities. Public repositories now host them in large and growing numbers, yet these artifacts are fragmented, redundant, and uneven in quality, and their value in practice is unclear. A core question remains open, namely how to consolidate this open-source SKILL.md ecosystem into a single usable corpus, and what bounds its benefit on real-world agent tasks. We present SkillCorpus, a framework that aggregates, curates, matches, and evaluates the open skill ecosystem at scale. It filters ~821,000 crawled skills through a multi-stage pipeline into 96,401 skills organised by a 16-class taxonomy and three quality facets (utility, robustness, safety), and pairs them with a fine-tuned retrieval-and-selection stack that matches task-relevant skills. We evaluate end-to-end across three benchmarks (SkillsBench, GDPVal, QwenClawBench), two harnesses, and two open backbones with a frontier robustness check. Integrating SkillCorpus yields consistent gains across all three benchmarks, largest on SkillsBench (+7.5 pp). An operational analysis traces the gains to a coverage boundary and a harness boundary. SkillCorpus is, to our knowledge, the first end-to-end account of when a curated, retrieval-served community corpus improves real agent tasks, and where it does not. The dataset, models, and code will be released upon acceptance.

</details>

---

### [[20_Research/Papers/大模型/VarRate_Training-Free_Variable-Rate_KV_Cache_Compression_for_Long-Context_LLMs|VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs]]

![[assets/2607.15498_figure.png|800]]

- **arXiv**: [2607.15498](https://arxiv.org/abs/2607.15498)
- **PDF**: https://arxiv.org/pdf/2607.15498
- **详细分析**: [[20_Research/Papers/大模型/VarRate_Training-Free_Variable-Rate_KV_Cache_Compression_for_Long-Context_LLMs|VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs]]
- **作者**: Shahrzad Esmat, Dhawal Shah, Ali Jannesari
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM

#### 研究背景与动机

《VarRate: Training-Free Variable-Rate KV Cache Compression for Long-Context LLMs》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GQA, LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The key-value (KV) cache is the main memory bottleneck in long-context large language model (LLM) inference. Two leading training-free families are both structurally limited: token-selection methods (SnapKV, Ada-KV) score importance from an observation window and evict low-scoring tokens, but eviction is irreversible -- so when the importance signal degrades under query-agnostic reuse, accuracy collapses by 11-15 points; uniform low-rank coding keeps every token but spends equal rank everywhere, wasting budget. We observe that both failures share one cure: rank should be allocated, not evicted. We present VarRate, a training-free KV codec that assigns each token a variable low-rank budget by its query salience, keeping every token at a nonzero rank. Comparable adaptive-rank codecs reach this allocation only through training; VarRate requires none. Because no token is dropped, it degrades by only 3.5-5.5 points where query-aware selection collapses. At a matched 20% budget on LongBench (16 tasks), VarRate stays within 0.8 points of the uncompressed model on both Llama-3.1-8B and Qwen2.5-7B. Averaged over the two, it is the strongest matched-memory compressor. It significantly beats its uniform-rank ablation on both models. Against KVzip, a method purpose-built for query-agnostic reuse, it is accuracy-equivalent in three of four settings and within a point overall, at about one-eighth the prefill overhead.

</details>

---
