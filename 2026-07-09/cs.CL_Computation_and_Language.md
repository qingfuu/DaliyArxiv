# cs.CL | Computation and Language | 2026-07-09

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/From_Noisy_Traces_to_Root_Causes_Structural_Trajectory_Analysis_and_Causal_Extraction_for_Agent_Optimization|From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization]]

![[assets/2607.07702_figure.jpg|800]]

- **arXiv**: [2607.07702](https://arxiv.org/abs/2607.07702)
- **PDF**: https://arxiv.org/pdf/2607.07702
- **详细分析**: [[20_Research/Papers/大模型/From_Noisy_Traces_to_Root_Causes_Structural_Trajectory_Analysis_and_Causal_Extraction_for_Agent_Optimization|From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization]]
- **作者**: Ying Chang, Jiahang Xu, Xuan Feng, Chenyuan Yang, Peng Cheng, Yuqing Yang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Noisy Traces to Root Causes: Structural Trajectory Analysis and Causal Extraction for Agent Optimization》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA, VeruSAGE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The optimization of long-horizon agents increasingly relies on reflection-based mechanisms, where a large language model (LLM) acts as an optimizer to diagnose agent failures and improve agent policies. However, real execution traces are difficult to use directly for optimization: large trace collections are often redundant and heterogeneous, making optimization inefficient and prone to overfitting to low-value failures; meanwhile, each individual trajectory also contains many irrelevant steps, while naive context reduction methods such as truncation or sliding windows can discard causally important evidence and produce misleading optimization signals. To resolve this dilemma, we introduce STRACE (Structural TRajectory Analysis and Causal Extraction), a framework that constructs high signal-noise optimization contexts for more precise and effective optimization. At the batch level, STRACE mines failure patterns to filter redundant traces and retain representative failures; within each selected trace, it performs causal localization over a textual dependency graph to remove non-causal steps and identify the true root-cause module for optimization. Empirical results demonstrate that STRACE significantly outperforms standard context-filtering baselines. Notably, on a challenging formal verification task (VeruSAGE-Bench), it successfully optimizes human-expert designed agents, delivering $1.4\times$ success-rate improvement (42.5% to 58.5%). The code is available at https://github.com/moomight/STRACE .

</details>

---

### [[20_Research/Papers/大模型/Think_Big,_Search_Small_Where_Capacity_Matters_in_Hierarchical_Search_Agents|Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?]]

![[assets/2607.07548_figure.png|800]]

- **arXiv**: [2607.07548](https://arxiv.org/abs/2607.07548)
- **PDF**: https://arxiv.org/pdf/2607.07548
- **详细分析**: [[20_Research/Papers/大模型/Think_Big,_Search_Small_Where_Capacity_Matters_in_Hierarchical_Search_Agents|Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?]]
- **作者**: Qinnan Cai, Yibo Zhao, Xiang Li
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Think Big, Search Small: Where Capacity Matters in Hierarchical Search Agents?》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model based search agents increasingly adopt multi-agent architectures in which a main agent decomposes a complex question into sub-queries and dispatches them to parallel sub-agents. However, existing systems instantiate all roles from a single model of identical scale, leaving open how model capacity should be distributed across roles. We factorize hierarchical search into three roles: a delegation role responsible for task decomposition, an execution role responsible for retrieval and evidence extraction, and an answer generation role held fixed as a confound control. We then conduct controlled capacity sweeps along the delegation and execution axes on five multi-hop QA benchmarks. The experiments yield three findings. First, role factorization consistently outperforms a single-agent baseline, improving exact match from 4.5 to 8.6 points across six model scales. Second, capacity sensitivity is asymmetric: scaling the delegation backbone improves EM by ~11 points, whereas scaling the execution sub-agent moves EM by only ~2.6 points, identifying decomposition as the capability bottleneck. Third, a 1.7B-parameter executor trained via quality-filtered trajectory distillation matches a frontier sub-agent in accuracy while consuming 37% fewer sub-agent tokens, advancing the Pareto frontier. These results suggest a concrete recipe for building hierarchical search agents: concentrate capacity at delegation and downsize execution without sacrificing accuracy. Our code is available at https://github.com/QinnanCai0115/role-factorized-search.

</details>

---
