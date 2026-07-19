# cs.OH | cs.OH | 2026-07-17

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/LIVE-RIS_Real-Time_In-Flight_Actuation_of_UAV-Mounted_RIS|LIVE-RIS: Real-Time In-Flight Actuation of UAV-Mounted RIS]]

![[assets/2607.14851_figure.png|800]]

- **arXiv**: [2607.14851](https://arxiv.org/abs/2607.14851)
- **PDF**: https://arxiv.org/pdf/2607.14851
- **详细分析**: [[20_Research/Papers/机器人/LIVE-RIS_Real-Time_In-Flight_Actuation_of_UAV-Mounted_RIS|LIVE-RIS: Real-Time In-Flight Actuation of UAV-Mounted RIS]]
- **作者**: David Müller, Kevin Weinberger, Aydin Sezgin, Martin Mönnigmann
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: 未提取到

#### 研究背景与动机

《LIVE-RIS: Real-Time In-Flight Actuation of UAV-Mounted RIS》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reconfigurable intelligent surfaces (RIS) are emerging as a key technology for sixth-generation (6G) wireless networks due to their ability to dynamically control the propagation environment. To ensure favorable Line-of-Sight (LoS) conditions in real-world applications, the RIS is mounted on an unmanned aerial vehicle (UAV). While the potential of UAV-mounted RIS has been extensively studied in theoretical works, experimental validation with real-world data remains limited. Such validation is particularly important, as UAV motion and disturbances may degrade the performance of the RIS-enabled link. In this paper, we present the first fully functional, real-time capable UAV-mounted RIS prototype and validate its performance through experimental measurements under realistic disturbances and hardware constraints. We show that the RIS pose can be predicted based on the UAV's extended Kalman filter (EKF) and onboard sensors. By utilizing this estimation, we demonstrate that the RIS can be reconfigured in real time, effectively mitigating disturbance effects and preserving the performance gains of the RIS-enabled link. Furthermore, we systematically evaluate different deployment locations to provide insights into RIS performance in real-world scenarios.

</details>

---

### [[20_Research/Papers/强化学习/Consistent_Variance_Estimation_for_Q-Function_Estimators_in_Finite-Horizon_MDP_Tree_Search|Consistent Variance Estimation for Q-Function Estimators in Finite-Horizon MDP Tree Search]]

![[assets/2607.14555_figure.png|800]]

- **arXiv**: [2607.14555](https://arxiv.org/abs/2607.14555)
- **PDF**: https://arxiv.org/pdf/2607.14555
- **详细分析**: [[20_Research/Papers/强化学习/Consistent_Variance_Estimation_for_Q-Function_Estimators_in_Finite-Horizon_MDP_Tree_Search|Consistent Variance Estimation for Q-Function Estimators in Finite-Horizon MDP Tree Search]]
- **作者**: Zhenyu Yue, Jie Xu, Chun-Hung Chen, Hadi El-Amine, Michael C. Fu
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Consistent Variance Estimation for Q-Function Estimators in Finite-Horizon MDP Tree Search》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study the variance of Q-function estimators in finite-horizon, finite-state Markov decision process (MDP) tree search. We show that the variance decomposes into three components attributed to the immediate reward collected, probabilistic state transitions, and uncertainty in future state value function estimates. Using this decomposition, we show that the sample variance estimator based on the assumption of i.i.d. paths is biased, underestimating the true variance, and the bias does not vanish in the limit. We then propose a recursive variance estimator that is consistent. To enable efficient storage and computation, we derive an equivalent implementation of the recursive estimator using only node-local statistics that can be iteratively updated. This consistent variance estimator is integrated into two Monte Carlo Tree Search (MCTS) sampling procedures for finite-horizon MDPs. In numerical examples from inventory control and kidney paired donation matching, the new estimator improves the performance of the MCTS algorithm relative to a baseline that uses the i.i.d.-based sample variance estimator.

</details>

---
