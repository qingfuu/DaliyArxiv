# cs.NI | Networking and Internet Architecture | 2026-07-13

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_SLA-Aware_Network_Slicing_in_UAV-Enabled_MEC|Multi-Agent Reinforcement Learning for SLA-Aware Network Slicing in UAV-Enabled MEC]]

![[assets/2607.09295_figure.png|800]]

- **arXiv**: [2607.09295](https://arxiv.org/abs/2607.09295)
- **PDF**: https://arxiv.org/pdf/2607.09295
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_for_SLA-Aware_Network_Slicing_in_UAV-Enabled_MEC|Multi-Agent Reinforcement Learning for SLA-Aware Network Slicing in UAV-Enabled MEC]]
- **作者**: Mohammad Farhoudi, Zeinab Sasan, Masoud Shokrnezhad, Tarik Taleb
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型
- **相关性评分**: 2.3（加权：大模型 0.5，强化学习 1，机器人 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Multi-Agent Reinforcement Learning for SLA-Aware Network Slicing in UAV-Enabled MEC》归入 强化学习、机器人、大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned Aerial Vehicle (UAV)-enabled Mobile Edge Computing (MEC) offers flexible capacity provisioning for heterogeneous network slices, including Hyper-Reliable and Low-Latency Communication (HRLLC), Enhanced Mobile Broadband (eMBB), and Massive Machine-Type Communications (mMTC). However, guaranteeing slice-level Service-Level Agreements (SLAs) under dynamic user mobility, stochastic task arrivals, and constrained onboard energy and computing resources remains a fundamental challenge. This paper proposes a predictive multi-agent Reinforcement Learning (RL) framework that proactively maintains SLA stability in UAV-enabled MEC through coordinated trajectory control and computation resource allocation. A lightweight prediction module forecasts near-future user mobility, enabling UAVs to anticipate congestion and reposition before SLA violations occur. We design an SLA-aware reward function that explicitly penalizes both violation probability and duration across slices, alongside total energy consumption. UAV agents are trained using Multi-Agent Proximal Policy Optimization (MAPPO) with centralized training and decentralized execution, enabling scalable online decision-making. Event-driven simulations with realistic mobility traces demonstrate that the proposed framework significantly improves SLA stability compared with baselines while maintaining competitive energy efficiency and delay performance, approaching oracle-level performance with sufficiently accurate predictive information.

</details>

---
