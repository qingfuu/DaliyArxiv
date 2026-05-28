# cs.IT | Information Theory | 2026-05-26

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Integrated_Sensing,_Communication,_and_Computing_for_NR-V2X_A_Cross-Layer_Resource_Allocation_Framework_Using_Multi-Agent_Reinforcement_Lear|Integrated Sensing, Communication, and Computing for NR-V2X: A Cross-Layer Resource Allocation Framework Using Multi-Agent Reinforcement Learning]]

![[assets/2605.24972_figure.png|800]]

- **arXiv**: [2605.24972](https://arxiv.org/abs/2605.24972)
- **PDF**: https://arxiv.org/pdf/2605.24972
- **详细分析**: [[20_Research/Papers/强化学习/Integrated_Sensing,_Communication,_and_Computing_for_NR-V2X_A_Cross-Layer_Resource_Allocation_Framework_Using_Multi-Agent_Reinforcement_Lear|Integrated Sensing, Communication, and Computing for NR-V2X: A Cross-Layer Resource Allocation Framework Using Multi-Agent Reinforcement Learning]]
- **作者**: Indulekha K. P., T. G. Venkatesh
- **cs 子类**: cs.IT
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Integrated Sensing, Communication, and Computing for NR-V2X: A Cross-Layer Resource Allocation Framework Using Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Integrated sensing, communication, and computation (ISCC) is emerging as a unified design paradigm for future vehicular networks that require joint environment perception, safety-critical information exchange, and latency-sensitive task processing. In New Radio Vehicle-to-Everything (NR-V2X) Mode 2, autonomous resource selection is performed through sensing-based semi-persistent scheduling (SB-SPS), which is effective for distributed communication resource reservation but does not explicitly consider sensing-resource demand, task-induced computation workload, and the additional latency introduced by mobile edge computing (MEC) offloading. This paper develops multi-agent proximal policy optimization-based SB-SPS (MAPPO-SPS), an ISCC-aware cross-layer scheduler that jointly adapts SB-SPS reservation, radio-resource partitioning, and overflow-driven computation-offloading decisions at control epochs. The scheduling problem is formulated as a cooperative partially observable Markov game and solved using MAPPO with centralized training and decentralized execution (CTDE). Simulation results show that MAPPO-SPS achieves a balanced tradeoff among CRLB-based sensing accuracy, packet reception ratio (PRR), effective throughput, energy consumption, and end-to-end delay.

</details>

---

### [[20_Research/Papers/强化学习/Leveraging_Deep_Reinforcement_Learning_for_Clustered_Cell-Free_Networking_Over_User_Mobility|Leveraging Deep Reinforcement Learning for Clustered Cell-Free Networking Over User Mobility]]

![[assets/2605.17266_figure.png|800]]

- **arXiv**: [2605.17266](https://arxiv.org/abs/2605.17266)
- **PDF**: https://arxiv.org/pdf/2605.17266
- **详细分析**: [[20_Research/Papers/强化学习/Leveraging_Deep_Reinforcement_Learning_for_Clustered_Cell-Free_Networking_Over_User_Mobility|Leveraging Deep Reinforcement Learning for Clustered Cell-Free Networking Over User Mobility]]
- **作者**: Ouyang Zhou, Junyuan Wang, Bo Qian, Antonio Pérez Yuste, Yusheng Ji
- **cs 子类**: cs.IT
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.8（加权：强化学习 1.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Leveraging Deep Reinforcement Learning for Clustered Cell-Free Networking Over User Mobility》归入 强化学习 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clustered cell-free networking paves a new way for enabling scalable joint transmission among access points (APs) by partitioning the whole network into non-overlapping subnetworks. Previous works adopted clustering algorithms, graph partitioning methods or conventional continuous optimization theories to partition a network based on the channels between all users and all APs, resulting in huge channel measurement and computational costs. This makes these methods difficult to be implemented in practical systems since the optimal network partition could vary frequently due to user mobility. In addition, existing methods were usually designed for specific clustered cell-free networking problems with different optimization algorithms employed. In this paper, we leverage deep reinforcement learning (DRL) for clustered cell-free networking so as to rapidly adapt to user movements in dynamic environments, and propose a deep deterministic policy gradient based clustered cell-free networking (DDPG-C$^{2}$F) framework that can be adapted in various application scenarios. Moreover, in our framework, only one single channel needs to be estimated at each AP as the input of the neural network, which greatly reduces the channel measurement costs for clustered cell-free networking, and the training and inference costs of our framework. The proposed DDPG-C$^{2}$F framework is then applied to various clustered cell-free networking problems with different objectives and constraints to demonstrate its performance. Simulation results show that our framework outperforms existing baselines in all scenarios. Moreover, we show that the proposed framework can reduce the handover cost over user mobility, and is robust to dynamic scenarios with random user joining or leaving.

</details>

---
