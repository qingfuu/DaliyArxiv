# cs.CR | Cryptography and Security | 2026-11-06

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/Stealthy_Malicious_Interference_Detection_in_UAV_Formations_A_Power-Domain_Signaling_Game_Approach|Stealthy Malicious Interference Detection in UAV Formations: A Power-Domain Signaling Game Approach]]

![[assets/2611.07977_figure.png|800]]

- **arXiv**: [2611.07977](https://arxiv.org/abs/2611.07977)
- **PDF**: https://arxiv.org/pdf/2611.07977
- **详细分析**: [[20_Research/Papers/机器人/Stealthy_Malicious_Interference_Detection_in_UAV_Formations_A_Power-Domain_Signaling_Game_Approach|Stealthy Malicious Interference Detection in UAV Formations: A Power-Domain Signaling Game Approach]]
- **作者**: Jianle Ba, Shaolong Guo, Yuntao Wang, Xin Wu, Zhou Su, Zhendong Li
- **cs 子类**: cs.CR, cs.IT
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Security

#### 研究背景与动机

《Stealthy Malicious Interference Detection in UAV Formations: A Power-Domain Signaling Game Approach》归入 机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable intra-swarm communication is fundamental to cooperative sensing, control, and mission execution in unmanned aerial vehicle (UAV) swarms. In open low-altitude shared-spectrum environments, coexisting UAVs may cause benign interference through spectrum reuse and signal leakage, while jamming UAVs may deliberately degrade critical intra-swarm links. Since a jamming UAV can adjust its transmit power to disguise signal-to-interference-plus-noise ratio (SINR) degradation as link fluctuation in benign interference, stealthy jammer UAV detection remains a challenge. In this paper, we propose a novel belief-driven stealthy jammer UAV detection scheme from the perspective of Bayesian security game. To capture stealthy interference in shared-spectrum UAV swarms, the interfering UAV is modeled as a hidden benign or jamming type, whose transmit power strategy induces the SINR observed by the defender. The defender updates its posterior belief from the observed SINR and decides whether to maintain normal operation or trigger defensive power boosting. We characterize pure-strategy perfect Bayesian equilibrium (PBE) conditions under separating structures with distinguishable type and pooling structures with indistinguishable observations. Numerical results show that the proposed scheme improves the defender's expected utility compared to the conventional schemes.

</details>

---

### [[20_Research/Papers/强化学习/Dynamic_Watermarking_and_Action-Conditioned_Latent_Dynamics_for_Secure_Vision-Based_Controllers|Dynamic Watermarking and Action-Conditioned Latent Dynamics for Secure Vision-Based Controllers]]

![[assets/2611.07403_first_page.png|800]]

- **arXiv**: [2611.07403](https://arxiv.org/abs/2611.07403)
- **PDF**: https://arxiv.org/pdf/2611.07403
- **详细分析**: [[20_Research/Papers/强化学习/Dynamic_Watermarking_and_Action-Conditioned_Latent_Dynamics_for_Secure_Vision-Based_Controllers|Dynamic Watermarking and Action-Conditioned Latent Dynamics for Secure Vision-Based Controllers]]
- **作者**: Aditya Parameshwaran, Navid Aftabi, Abhishek Hanchate, Satish T. S. Bukkapatnam, Dan Li, Yue Wang
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.2，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Dynamic Watermarking and Action-Conditioned Latent Dynamics for Secure Vision-Based Controllers》归入 世界模型、机器人、具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Replay attacks are difficult to detect in vision-based control systems because previously recorded observations can remain plausible while the physical system follows a different trajectory. This paper develops an adaptive dynamic-watermarking framework for detecting replay attacks against vision-based controllers. A private Gaussian watermark is added to the nominal control input, and a control input-conditioned latent dynamics network (LDN) predicts the corresponding evolution in a compact latent space learned from image observations. Attack evidence is obtained from the discrepancy between the predicted latent response and the latent representation of the received image observation. A reinforcement learning policy adjusts the watermark covariance using the latent state and detector confidence, thereby balancing attack detectability, watermark energy, and control distortion. A Lagrangian penalty on task-specific safety costs is included during training to limit the adverse effect of the excitation. The framework is evaluated on a vision-guided UR5 manipulation task in which the robot reaches a target while avoiding a moving human arm under nominal and replay-attacked observations.

</details>

---
