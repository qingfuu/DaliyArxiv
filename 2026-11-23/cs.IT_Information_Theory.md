# cs.IT | Information Theory | 2026-11-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Dual-Agent_DRL_based_Cooperative_Beamforming_and_Trajectory_Optimization_for_UAV-ISAC_Networks|Dual-Agent DRL based Cooperative Beamforming and Trajectory Optimization for UAV-ISAC Networks]]

![[assets/2611.27346_figure.png|800]]

- **arXiv**: [2611.27346](https://arxiv.org/abs/2611.27346)
- **PDF**: https://arxiv.org/pdf/2611.27346
- **详细分析**: [[20_Research/Papers/强化学习/Dual-Agent_DRL_based_Cooperative_Beamforming_and_Trajectory_Optimization_for_UAV-ISAC_Networks|Dual-Agent DRL based Cooperative Beamforming and Trajectory Optimization for UAV-ISAC Networks]]
- **作者**: Kaijian Yang, Feng Wang, Guojun Han, Xin Wang, Vincent K. N. Lau
- **cs 子类**: cs.IT
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.5，强化学习 0.6，机器人 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Dual-Agent DRL based Cooperative Beamforming and Trajectory Optimization for UAV-ISAC Networks》归入 机器人、强化学习、大模型 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MADRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper considers a low-altitude unmanned aerial vehicle (UAV) network, where multiple ground base stations (BSs) provide integrated sensing and communication (ISAC) services for multiple communication UAVs (C-UAVs) and sensing UAVs (S-UAVs). With the objective of maximizing the average sum rate of C-UAVs over the entire flight episode, we jointly optimize the multi-BS multi-UAV ISAC beamforming and trajectory design, subject to the BS transmit power budget and the sensing signal-to-interference-plus-noise ratio (SINR) constraints of S-UAVs, as well as the flight mission and collision avoidance constraints of C-UAVs and S-UAVs. Based on the multi-agent deep reinforcement learning (MADRL) technique, we develop a dual-agent scheme, termed DeepDA-OPT, to solve the resulting constrained Markov decision process (MDP). In the proposed DeepDA-OPT scheme, two agents, i.e., Agent-B and Agent-T, are specifically deployed for learning the multi-BS ISAC transmit beamformers and the C-UAV/S-UAV trajectories, respectively, where the optimal BS receive beamformers for the sensing echo signals of S-UAVs are obtained in closed form by leveraging the generalized Rayleigh quotient theorem. To mitigate the overestimation of value functions, both Agent-B and Agent-T are trained based on the twin-delayed deep deterministic (TD3) policy-gradient algorithm. In addition, a constraint-aware noise exploration policy is employed, and the reward function is designed to incorporate a sensing penalty and a flight urgency penalty, thereby guiding the training of Agent-B and Agent-T. Numerical results show that, compared with the baseline schemes, the proposed DeepDA-OPT scheme achieves a higher average sum rate of C-UAVs, while the sensing SINR constraints are empirically well satisfied and no collision violation is observed under the evaluated settings.

</details>

---
