# cs.IT | Information Theory | 2026-11-16

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/PF-Exec_Large-Scale_UAV_Relay_Load_Balancing_with_an_Anchored_Potential_Direction_Decider_and_a_Per-Dimension_Gain-Learning_Executor|PF-Exec: Large-Scale UAV Relay Load Balancing with an Anchored Potential Direction Decider and a Per-Dimension Gain-Learning Executor]]

![[assets/2611.17492_figure.png|800]]

- **arXiv**: [2611.17492](https://arxiv.org/abs/2611.17492)
- **PDF**: https://arxiv.org/pdf/2611.17492
- **详细分析**: [[20_Research/Papers/强化学习/PF-Exec_Large-Scale_UAV_Relay_Load_Balancing_with_an_Anchored_Potential_Direction_Decider_and_a_Per-Dimension_Gain-Learning_Executor|PF-Exec: Large-Scale UAV Relay Load Balancing with an Anchored Potential Direction Decider and a Per-Dimension Gain-Learning Executor]]
- **作者**: Liheng Zeng, Hanzhang Jia, Yiran Li, Yi Gao, Bo Ma
- **cs 子类**: cs.IT, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《PF-Exec: Large-Scale UAV Relay Load Balancing with an Anchored Potential Direction Decider and a Per-Dimension Gain-Learning Executor》归入 机器人 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Relay load balancing in large-scale UAV networks requires joint decisions on association, bandwidth, power and hovering position, while the dimension grows with the number of UAVs and each UAV sees only its local state. This paper splits the decision into two layers. An anchored potential direction decider emits a closed-form target at every instant and returns its direction only. A gain-learning executor maps a local observation into a positive gain per dimension, composes gain and target, and clips the action against the physical single-step bound; the two layers form PF-Exec. The unit gain is the default start, so the executor reduces to the pure potential policy before training. The load is first-order homogeneous in bandwidth, making the bandwidth target closed form, and the position target is the demand-weighted centroid of the served users. The system uses a two-hop access and millimetre-wave backhaul link with soft association, a 3GPP UMa-AV channel with two shadowing layers, an OU-type social-force crowd and a quadrotor physical layer. Evaluation spans all fleet sizes, two crowd scenarios, independent seeds, the published baselines in their own settings and a degraded-information line. In the highest-pressure burst setting the fixed-step comparison breaks down on part of the seeds, losing fairness and mean load at once, while PF-Exec holds fairness near one. Among the ten comparison methods only the greedy heuristic survives that setting; its load variance stays far higher. Under stale global state and position noise the fairness index stays high at both largest-scale scenarios. Flight energy is nearly identical between the learned and the fixed-step executor, and three constants are fixed once across all settings. The convergence properties of both layers, from the truncated gain iteration to the perturbed tracking bound, are proved in the companion analysis.

</details>

---
