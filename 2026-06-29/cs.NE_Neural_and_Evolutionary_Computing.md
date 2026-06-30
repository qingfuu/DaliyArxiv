# cs.NE | Neural and Evolutionary Computing | 2026-06-29

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/其他/MMAO_A_Metabolic_Multi-Agent_Optimizer_with_Endogenous_Resource_Allocation_for_Continuous_and_Discrete_Optimization|MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization]]

![[assets/2606.28109_figure.png|800]]

- **arXiv**: [2606.28109](https://arxiv.org/abs/2606.28109)
- **PDF**: https://arxiv.org/pdf/2606.28109
- **详细分析**: [[20_Research/Papers/其他/MMAO_A_Metabolic_Multi-Agent_Optimizer_with_Endogenous_Resource_Allocation_for_Continuous_and_Discrete_Optimization|MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization]]
- **作者**: Jinliang Xu, Liping Ma
- **cs 子类**: cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: Agent

#### 研究背景与动机

《MMAO: A Metabolic Multi-Agent Optimizer with Endogenous Resource Allocation for Continuous and Discrete Optimization》归入 大模型 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional meta-heuristics often rely on fixed population sizes, manually chosen search scales, and externally attached parameter-control modules. This paper presents the \textit{Metabolic Multi-Agent Optimizer} (MMAO), a cross-domain optimization framework in which adaptation is derived endogenously from a private-public metabolic resource loop. Each agent carries internal energy, a continuous role state, motion or structural memory, and local search history, while the population shares a communal resource pool. Fitness improvements are converted into normalized metabolic gains through a robust progress scale and a recent success statistic; the same closed loop then regulates sensing intensity, search amplitude, role drift, branching, pruning, respawning, and elite reinvestment. In the continuous setting, MMAO uses energy-regulated symmetric zero-order probing and role-interpolated motion. In the discrete setting, the same control law is instantiated through structural sensing, local route improvement, guided perturbation, and energy-weighted edge reuse. The paper combines an implementation-faithful formulation with a reproducible experimental study on a CEC2017 subset (10D/30D, 20 seeds) and five TSPLIB instances (100 discrete runs in total). The current evidence supports MMAO primarily as a parameter-light, self-calibrating optimization framework whose main validated originality lies in metabolically endogenous resource allocation across heterogeneous search behaviors, rather than as a universally superior optimizer.

</details>

---
