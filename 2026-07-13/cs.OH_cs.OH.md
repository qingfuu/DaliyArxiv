# cs.OH | cs.OH | 2026-07-13

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/An_Improved_Deep_Reinforcement_Learning_Control_Strategy_for_Traction_Dual_Rectifiers_in_EMUs|An Improved Deep Reinforcement Learning Control Strategy for Traction Dual Rectifiers in EMUs]]

![[assets/2607.09276_figure.jpg|800]]

- **arXiv**: [2607.09276](https://arxiv.org/abs/2607.09276)
- **PDF**: https://arxiv.org/pdf/2607.09276
- **详细分析**: [[20_Research/Papers/强化学习/An_Improved_Deep_Reinforcement_Learning_Control_Strategy_for_Traction_Dual_Rectifiers_in_EMUs|An Improved Deep Reinforcement Learning Control Strategy for Traction Dual Rectifiers in EMUs]]
- **作者**: Zhigang Liu, Mingwei Tang, Xiangyu Meng, Hui Wang, Qiao Zhang, Haoyu Wang, Mengru Li
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.1，强化学习 1.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《An Improved Deep Reinforcement Learning Control Strategy for Traction Dual Rectifiers in EMUs》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Due to the use of PI-based d q current decoupling in the pulse rectifier of CRH5 high-speed trains, the PI parameters directly affect the traction system's control performance. Linearized control may have issues with reference trajectory changes or model mismatches, leading to a decrease in system performance, while nonlinear control may have problems with jitter and poor steady-state accuracy. This paper proposes a new control strategy that replaces all PI in the d q current decoupling control with a single intelligent agent. This method based on Deep Reinforcement Learning (DRL) can avoid various drawbacks of linearization and nonlinear control and ensure the stability of intermediate DC voltage. However, when EMUs are in different working conditions and switching, the Twin Delayed Deep Deterministic Policy Gradient (TD3) algorithm used in traction dual rectifiers does not have a good control effect. Focusing on the issue, Reward Shaping (RS) is added to re-design a nonlinear reward function, which can be combined with Prioritized Experience Replay (PER) to increase the convergence speed of the episode reward. The simulation results show that the improved control strategy can be effectively applied to EMUs working in multiple conditions. Finally, the stability analysis is carried out using Lyapunov's second method and the verification results of the hardware-in-the-loop (HIL) simulation platform show that the DRL control has a good effect.

</details>

---

### [[20_Research/Papers/具身智能/Can_the_Cloud_Drive_Infrastructure_Feasibility_of_Offloading_Autonomous_Driving_Across_5G_and_6G|Can the Cloud Drive? Infrastructure Feasibility of Offloading Autonomous Driving Across 5G and 6G]]

![[assets/2607.09045_figure.png|800]]

- **arXiv**: [2607.09045](https://arxiv.org/abs/2607.09045)
- **PDF**: https://arxiv.org/pdf/2607.09045
- **详细分析**: [[20_Research/Papers/具身智能/Can_the_Cloud_Drive_Infrastructure_Feasibility_of_Offloading_Autonomous_Driving_Across_5G_and_6G|Can the Cloud Drive? Infrastructure Feasibility of Offloading Autonomous Driving Across 5G and 6G]]
- **作者**: Pouya Parsa, Kawon Han, Seongjin Choi
- **cs 子类**: 
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.6（加权：具身智能 0.6）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Can the Cloud Drive? Infrastructure Feasibility of Offloading Autonomous Driving Across 5G and 6G》归入 具身智能 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier autonomous-driving models -- especially vision-language-action (VLA) models, whose forward pass approaches $\sim$60~TFLOPs -- are outgrowing economical onboard deployment, since peak hardware sits idle most of the day. Cloud inference can instead share GPUs across active vehicles, but the vehicle must upload through a capacity-limited uplink, reach a GPU without queueing, and return a decision within the closed-loop budget. This paper asks: can the cloud drive? We answer with an analytical framework coupling communication limits, a roofline GPU service model, stochastic latency, and utilization-aware cost across three model classes, three offloading strategies, and three communication generations, applied to New York City. Separating a reactive 100~ms budget from a 300~ms deliberative tier (presuming an onboard reactive fallback), we find three \emph{nested} binding regimes. Communication binds first in dense cells: 5G fails early, 5G-Advanced is the practical threshold for feature-level offloading, and 6G adds headroom. Compute binds next under the reactive budget: near-term VLA is latency-infeasible regardless of bandwidth, because autoregressive FP16 decode is memory-bandwidth-bound (~114 ms on 2025 hardware). Its floor clears 100 ms around 2027; 6G then admits feature-level VLA by ~2028, 5G-Advanced only at light loading and not the dense corridor, and the deliberative tier from 2026. Cost binds last: once admissible, utilization-pooled cloud GPUs undercut onboard hardware for VLA, whose baseline (up to \$8,500 per vehicle-year) is expensive and idle; feature-level offloading (S2) is where the VLA cost crossover concentrates. Latency decides which model is admissible in which year; cost decides whether it is economical.

</details>

---
