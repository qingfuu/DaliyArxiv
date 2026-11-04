# cs.OH | cs.OH | 2026-11-02

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Preference-Conditioned_Group-Relative_Policy_Optimization_for_Terminally_Constrained_Multi-Objective_Control|Preference-Conditioned Group-Relative Policy Optimization for Terminally Constrained Multi-Objective Control]]

![[assets/2610.41884_figure.png|800]]

- **arXiv**: [2610.41884](https://arxiv.org/abs/2610.41884)
- **PDF**: https://arxiv.org/pdf/2610.41884
- **详细分析**: [[20_Research/Papers/强化学习/Preference-Conditioned_Group-Relative_Policy_Optimization_for_Terminally_Constrained_Multi-Objective_Control|Preference-Conditioned Group-Relative Policy Optimization for Terminally Constrained Multi-Objective Control]]
- **作者**: Md Ragib Rownak, Sidra Ghayour Bhatti, Qadeer Ahmed
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Preference-Conditioned Group-Relative Policy Optimization for Terminally Constrained Multi-Objective Control》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-objective optimal control is commonly addressed by reinforcement learning with fixed scalarization weights, requiring a separate training run and constraint enforcement for each trade-off. This letter extends critic-free group-relative policy optimization to terminally constrained multi-objective control: a single preference-conditioned policy is trained over random preferences and returns a feasible approximation of the Pareto front in one run. Three structural results are established. Group normalization after scalarization preserves the prescribed preference, whereas per-objective normalization induces policy-dependent distortion; with pairwise distinct normalization scales, only single-objective preferences remain unchanged. A positive floor prevents the terminal-constraint multiplier from vanishing and renders the penalty exact when the floor exceeds a geometric multiplier. Deterministic terminal violation is bounded by expected stochastic violation plus a term depending on terminal-state curvature and action variance, so stochastic feasibility alone does not certify deterministic execution. On a heavy-duty range-extender powertrain with six stage costs and a terminal state-of-charge band, a representative training run places all 32 preference-grid solutions in band on six cycles inside and outside the training pool. Averaged over ten runs, the method yields more in-band solutions under deterministic execution than a critic-based conditioned baseline with the same terminal-constraint handling.

</details>

---
