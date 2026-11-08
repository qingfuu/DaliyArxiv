# cs.NI | Networking and Internet Architecture | 2026-11-06

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Deep_reinforcement_learning-based_optimization_of_multi-RAT_handovers|Deep reinforcement learning-based optimization of multi-RAT handovers]]

![[assets/2611.07390_figure.jpg|800]]

- **arXiv**: [2611.07390](https://arxiv.org/abs/2611.07390)
- **PDF**: https://arxiv.org/pdf/2611.07390
- **详细分析**: [[20_Research/Papers/强化学习/Deep_reinforcement_learning-based_optimization_of_multi-RAT_handovers|Deep reinforcement learning-based optimization of multi-RAT handovers]]
- **作者**: Pavan Kumar Mangipudi, Satya Krishna Pothapragada, Alina Zare, Janise McNair
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.7（加权：大模型 0.1，强化学习 1.6）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Deep reinforcement learning-based optimization of multi-RAT handovers》归入 强化学习、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A major evolutionary goal and challenge for next-generation wireless systems is seamless multiple radio access technology (multi-RAT) mobility. In a multi-RAT environment, handover decisions must account for both user quality of service and network priorities, including signal quality, resource availability, energy consumption, latency, and security. Although WiFi/cellular mobility is well explored in research and standardization, many conventional handover mechanisms continue to rely primarily on received signal strength. Such decisions may overlook link delay, congestion, and the distinct operating characteristics of heterogeneous RATs. In this work, we present the Reinforced Flexible Multi-RAT Selection framework (ReFlexMRS), a configurable Deep Reinforcement Learning (DRL)-based approach for multi-criteria handover target selection. ReFlexMRS is evaluated using an SDN-enabled multi-RAT testbed. The decision problem is formulated as a Markov Decision Process with a finite action space and is addressed using a Deep Q-Network (DQN) with convolutional layers that extract relationships among network measurement features. The agent is trained offline from collected network observations using reward guided Q-value updates, then used to select handover targets during inference. A 5G-WiFi case study demonstrates that ReFlexMRS can trade a small amount of throughput for substantial improvements in link delay, handover stability, and WiFi offloading. Compared with RSSI-based selection, the proposed formulations retain approximately 90-95% of the baseline throughput while reducing total handovers by up to 18% and WiFi-to-5G handovers by up to 13%, while maintaining the required RSSI levels.

</details>

---
