# cs.OH | cs.OH | 2026-06-15

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/TetraRL_A_Self-Adaptive_Runtime_for_On-Device_Deep_Reinforcement_Learning_Systems|TetraRL: A Self-Adaptive Runtime for On-Device Deep Reinforcement Learning Systems]]

![[assets/2606.13891_figure.png|800]]

- **arXiv**: [2606.13891](https://arxiv.org/abs/2606.13891)
- **PDF**: https://arxiv.org/pdf/2606.13891
- **详细分析**: [[20_Research/Papers/强化学习/TetraRL_A_Self-Adaptive_Runtime_for_On-Device_Deep_Reinforcement_Learning_Systems|TetraRL: A Self-Adaptive Runtime for On-Device Deep Reinforcement Learning Systems]]
- **作者**: Zexin Li, Soheil Shirvani, Cong Liu
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人
- **相关性评分**: 1.8（加权：强化学习 1.6，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TetraRL: A Self-Adaptive Runtime for On-Device Deep Reinforcement Learning Systems》归入 强化学习、机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MORL, TetraRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robotic systems, including autonomous vehicles, drones, and mobile robots, increasingly rely on on-device Deep Reinforcement Learning (DRL) to adapt to dynamic environments. Unlike cloud-based solutions, embedded DRL must perform training and inference directly on resource-constrained hardware while maintaining timely decision-making. This creates a fundamental challenge: balancing four tightly coupled objectives, real-time performance, task reward, memory utilization, and energy consumption. Optimizing these objectives independently often leads to suboptimal behavior, while conventional multi-objective methods may violate resource constraints and compromise reliability. This paper presents TetraRL, a self-adaptive runtime framework for tetra-objective on-device DRL. TetraRL formulates embedded DRL as a unified optimization problem over real-time, reward, RAM, and reserve (energy) objectives, and employs a preference-conditioned reinforcement learning controller to dynamically navigate the resulting trade-off space. The framework integrates a unified resource-management abstraction, hardware-aware DVFS control, and a runtime Override Layer for robust constraint enforcement. We implement TetraRL on NVIDIA Jetson AGX Orin and Orin Nano platforms and evaluate it across diverse DRL environments. Results show that TetraRL effectively balances all four objectives, achieves competitive trade-offs under varying runtime preferences, and incurs negligible overhead. Moreover, a single trained policy can support runtime-switchable optimization goals, providing a practical foundation for resource-aware and self-adaptive on-device DRL.

</details>

---
