# cs.CL | Computation and Language | 2026-10-30

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Agentic_LLM_reasoning_in_pediatric_diabetes_outcome_prediction_from_multimodal_medical_records|Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records]]

![[assets/2610.40379_first_page.png|800]]

- **arXiv**: [2610.40379](https://arxiv.org/abs/2610.40379)
- **PDF**: https://arxiv.org/pdf/2610.40379
- **详细分析**: [[20_Research/Papers/大模型/Agentic_LLM_reasoning_in_pediatric_diabetes_outcome_prediction_from_multimodal_medical_records|Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records]]
- **作者**: Daniel Palacios, Guantong Qi, Anna Kadi, Natali Borrego, Sukru Aras, Michael L. Ferm, Elizabeth Kubota-Mishra, Maria J. Redondo, Zhandong Liu, Mustafa Tosur, Hu Chen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Agentic LLM reasoning in pediatric diabetes outcome prediction from multimodal medical records》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are proposed for clinical prediction but are untested in pediatrics, where cohorts are small and outcomes are uncommon. Using records from 2,489 youth with type 2 diabetes (T2D) and 4,018 with type 1 diabetes (T1D), spanning structured data, note-derived social determinants and, in T1D, continuous glucose monitoring data, we predicted seven T2D outcomes, four also in T1D, at 24 months from 18 months of follow-up. CEDAR (Clinical Evidence-Driven Agent for Risk-prediction), an evidence-citing, self-auditing LLM pipeline, outperformed trained machine learning in both cohorts (pooled area under the receiver operating characteristic curve 0.815 versus 0.656 to 0.700 in T2D and 0.756 versus 0.603 to 0.631 in T1D), most on the sparsely screened outcomes. Only 4 of 70,246 values it cited did not match the chart. Reading only the evidence and reasoning cited by CEDAR, two pediatric endocrinologists reached the same prediction as CEDAR in about nine of ten cases, agreeing with each other on 90.5%.

</details>

---

### [[20_Research/Papers/大模型/Don't_Lose_the_Thread_Empowering_Long-Horizon_LLM_Agents_with_Cognitive_Resource_Self-Allocation|Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation]]

![[assets/2610.40350_first_page.png|800]]

- **arXiv**: [2610.40350](https://arxiv.org/abs/2610.40350)
- **PDF**: https://arxiv.org/pdf/2610.40350
- **详细分析**: [[20_Research/Papers/大模型/Don't_Lose_the_Thread_Empowering_Long-Horizon_LLM_Agents_with_Cognitive_Resource_Self-Allocation|Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation]]
- **作者**: Zheng Zhu, Xiaozhuan Liang, Xi Chen, Bei Yu, Jiaya Jia
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.25（加权：大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Don't Lose the Thread: Empowering Long-Horizon LLM Agents with Cognitive Resource Self-Allocation》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agents powered by large language models (LLMs) have demonstrated remarkable progress in solving complex reasoning tasks. However, LLM agents often falter on long-horizon tasks due to cognitive overload, as their working memory becomes cluttered with expanding and irrelevant information, which dilutes their attention and hinders effective planning and reasoning. To mitigate this challenge, we introduce Cognitive Resource Self-Allocation (CORAL), a novel reasoning paradigm that empowers agents to proactively optimize their context. Implemented as an agent-callable working memory management toolset, CORAL allows an agent to checkpoint its task progress and verified facts, and adaptively initiate a new problem-solving episode by resetting cluttered context while preserving only the checkpointed information, enabling it to resume reasoning from a clean state. We further enhance the agent's checkpointing capabilities using a Multi-episode Agentic Reinforced Policy Optimization algorithm. On the GAIA benchmark, CORAL with an 8B model achieves 42.8% average accuracy, with particularly strong gains on the most challenging long-horizon tasks (Level 2 and Level 3). Crucially, these gains come at a substantially lower inference cost: CORAL consumes 6-7$\times$ fewer input tokens than a ReAct agent. It also generalizes to multi-hop Knowledge QA benchmarks and to the considerably harder BrowseComp, where it improves a strong proprietary agent by 8.0 points.

</details>

---

### [[20_Research/Papers/大模型/Fu-TCM_a_multimodal_large_language_model_that_learns_traditional_Chinese_medicine_diagnostic_reasoning|Fu-TCM: a multimodal large language model that learns traditional Chinese medicine diagnostic reasoning]]

![[assets/2610.38333_figure.png|800]]

- **arXiv**: [2610.38333](https://arxiv.org/abs/2610.38333)
- **PDF**: https://arxiv.org/pdf/2610.38333
- **详细分析**: [[20_Research/Papers/大模型/Fu-TCM_a_multimodal_large_language_model_that_learns_traditional_Chinese_medicine_diagnostic_reasoning|Fu-TCM: a multimodal large language model that learns traditional Chinese medicine diagnostic reasoning]]
- **作者**: Jiahang Xie, Tong Jin, Lingfei Wu, Yaping You, Jie Huang, Yuanchang Jin, Weikang Gong, Wei Cheng, Jia You, Pan Sun, Jianfeng Feng, Hongcheng Guo
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.45（加权：大模型 1.25，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Fu-TCM: a multimodal large language model that learns traditional Chinese medicine diagnostic reasoning》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are advancing in multimodal understanding and reasoning, accelerating medical model development. Traditional Chinese medicine (TCM) uses evidence from the four examinations to determine disease location and nature, differentiate syndromes and guide treatment. This diagnostic process constitutes a complete chain of reasoning. We present Fu-TCM, a multimodal TCM LLM trained on data retained after cleaning and filtering an initial collection of approximately 7.12 million examples derived from classical texts, textbooks, medical images, clinical cases and publicly available datasets. The model was further optimized using Bianzheng-Grounded Policy Optimization (BGPO), which explicitly targets syndrome differentiation through rewards for response format, intermediate TCM reasoning fields and final syndrome predictions. Fu-TCM-27B led all six benchmarks spanning TCM reasoning, text and vision, achieving a macro-average accuracy of 81.01% and surpassing the strongest reference model with complete results across all six benchmarks by 7.13 percentage points. Its largest margin was 11.90 points on Fu-bianzheng. Case-level analyses further showed a positive association between intermediate-field accuracy and final syndrome-selection accuracy in most evaluated models. These findings suggest that TCM syndrome differentiation may be computationally learnable and that structured reasoning supervision can improve performance across TCM tasks.

</details>

---
