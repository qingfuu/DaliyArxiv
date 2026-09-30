# cs.CL | Computation and Language | 2026-09-28

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/ToolSearcher_Optimizing_Tool_Selection_at_Scale_via_Reinforcement_Learning|ToolSearcher: Optimizing Tool Selection at Scale via Reinforcement Learning]]

![[assets/2609.30906_first_page.png|800]]

- **arXiv**: [2609.30906](https://arxiv.org/abs/2609.30906)
- **PDF**: https://arxiv.org/pdf/2609.30906
- **详细分析**: [[20_Research/Papers/强化学习/ToolSearcher_Optimizing_Tool_Selection_at_Scale_via_Reinforcement_Learning|ToolSearcher: Optimizing Tool Selection at Scale via Reinforcement Learning]]
- **作者**: Zhenlong Dai, Xujie Song, Zitong Wang, Tong Niu, Jian liu, Weiqiang Wang, Xiu Tang, Sai Wu, Chang Yao, Jingyuan Chen
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《ToolSearcher: Optimizing Tool Selection at Scale via Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) excel at natural language processing but struggle to interact with external environments. Tool learning provides a promising way to extend LLMs into actionable agents, where tool selection is a critical prerequisite for successful tool use. Existing work often assumes a small or predefined set of tools, leaving large-scale tool selection underexplored. Real-world repositories contain a vast and diverse array of tools, making it difficult for LLMs to effectively search, distinguish, and compose tools under context-length constraints. We identify large-scale tool selection as a new challenge for agentic reinforcement learning, highlighting that existing RL methods for knowledge-based question answering are inadequate for selecting tools while considering compatibility. To address this challenge, we propose ToolSearcher, a novel RL framework for effective multi-turn search and fine-grained optimization in large-scale tool selection. Specifically, we introduce category-constrained tool discrimination to improve the model's ability to distinguish functionally similar tools, event-level search modeling to explicitly optimize the discovery of target tools during multi-turn search, and trajectory-aligned credit allocation to provide fine-grained reward signals for different stages of the search-selection process. Extensive experiments on large-scale tool selection benchmarks demonstrate that ToolSearcher consistently outperforms a set of strong baselines in challenging settings involving iterative search and complex tool composition.

</details>

---

### [[20_Research/Papers/大模型/Not_All_Memories_Are_Equal_Hierarchical_Collaborative_Memory_for_Validity-Aware_Retrieval_in_LLM_Agents|Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents]]

![[assets/2609.30289_figure.png|800]]

- **arXiv**: [2609.30289](https://arxiv.org/abs/2609.30289)
- **PDF**: https://arxiv.org/pdf/2609.30289
- **详细分析**: [[20_Research/Papers/大模型/Not_All_Memories_Are_Equal_Hierarchical_Collaborative_Memory_for_Validity-Aware_Retrieval_in_LLM_Agents|Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents]]
- **作者**: Yufei Shi, Rujing Yao, Ang Li, Yang Wu, Zhuoren Jiang, Xiaozhong Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Not All Memories Are Equal: Hierarchical Collaborative Memory for Validity-Aware Retrieval in LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In team collaboration scenarios, memory is heterogeneous and continually evolving. Team memories capture collective decisions, protocols, and current consensus, while individual memories preserve member-specific observations, execution traces, and intermediate progress. Existing memory-augmented systems typically retrieve from all stored memories as a flat pool, ranking them by semantic relevance, importance, or recency without modeling hierarchical structure or evolving validity. As a result, they often surface semantically relevant but outdated or conflicting memories, especially individual memories that no longer align with current team consensus, instead of prioritizing currently valid memories. This is particularly problematic when collaborative LLM agents answer user questions, since their responses should be grounded in valid memories. We propose HiCoMER, a framework for hierarchical collaborative memory management and validity-aware retrieval in LLM agents. HiCoMER first maintains the validity of team and individual memories and then retrieves memories that remain valid, rather than retrieving directly from all stored memories. It consists of three components: a Hierarchical Memory Conflict Updater, a Validity-Aware Memory Retriever, and a Memory-Grounded Answer Generator. To evaluate HiCoMER, we construct two new datasets for memory-grounded question answering in collaborative settings. Experiments on both datasets show that HiCoMER consistently outperforms strong baselines by reducing outdated retrieval, preserving current team consensus, and improving downstream QA quality.

</details>

---
