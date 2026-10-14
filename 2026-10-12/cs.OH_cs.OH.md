# cs.OH | cs.OH | 2026-10-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/ROAM_Reinforcement_Learning_Optimized_Adaptive_Moving_Target_Defense_for_Smart_Grid|ROAM: Reinforcement Learning Optimized Adaptive Moving Target Defense for Smart Grid]]

![[assets/2610.12730_figure.png|800]]

- **arXiv**: [2610.12730](https://arxiv.org/abs/2610.12730)
- **PDF**: https://arxiv.org/pdf/2610.12730
- **详细分析**: [[20_Research/Papers/强化学习/ROAM_Reinforcement_Learning_Optimized_Adaptive_Moving_Target_Defense_for_Smart_Grid|ROAM: Reinforcement Learning Optimized Adaptive Moving Target Defense for Smart Grid]]
- **作者**: Mohammad Zakaria Haider, Prabin Mali, Muhammad Nadeem, Sumit Paudyal, Fei Ding, Mohammad Ashiqur Rahman
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.1，强化学习 1.2）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《ROAM: Reinforcement Learning Optimized Adaptive Moving Target Defense for Smart Grid》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Smart grids rely on distributed phasor measurement units (PMUs) and wide-area communication networks whose data-acquisition pipelines are vulnerable to stealthy false data injection (FDI) attacks that evade conventional bad-data detection (BDD). Moving target defense (MTD) counters this exposure by continuously remapping sensor identities, but existing schemes apply static or pre-scheduled randomization and are each constrained by a single failure mode: seed-based methods are fast yet fragile to key compromise, while machine learning (ML) based prediction methods are resilient yet incur prohibitive latency. Neither adapts its randomization to live threat evidence. This paper presents ROAM, a deep reinforcement learning (DRL) driven MTD framework in which a deep Q-network (DQN) agent continuously re-optimizes the sensor-to-ID mapping at the aggregation layer. At each decision step, the agent selects the deception coverage, flags the specific sensors to remap, and sets the split of the remapped sensors between seed-based and ML-prediction-based recovery, without modifying PMU hardware and while preserving IEEE C37.118 compatibility. On held-out BDD-compliant FDI scenarios across the IEEE 14-, 57-, and 118- bus systems, ROAM keeps the percentage of stealthy attacks below 3% while sustaining detection rates above 93%. Against an adaptive soft actor-critic (SAC) attacker that observes the defender's configuration, ROAM keeps stealthy attacks below 2.6% with detection above 92%. Hardware-in-the-loop testing on an OPAL-RT platform confirms real-time feasibility, with sub-18ms average shuffle execution and an average reshuffle blind window of 2.6% of the 3-s decision cycle.

</details>

---
