# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Multi-UAV_Data_Harvesting_Under_Variable_Team_Sizes_and_Agent_Loss|Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss]]

![[assets/2611.34818_figure.png|800]]

- **arXiv**: [2611.34818](https://arxiv.org/abs/2611.34818)
- **PDF**: https://arxiv.org/pdf/2611.34818
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Multi-UAV_Data_Harvesting_Under_Variable_Team_Sizes_and_Agent_Loss|Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss]]
- **作者**: Thiago de Souza Lamenza, Bruno José Olivieri de Souza, Markus Endler
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型, 世界模型
- **相关性评分**: 3.22（加权：大模型 0.5，强化学习 1.76，世界模型 0.16，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Deep Reinforcement Learning for Multi-UAV Data Harvesting Under Variable Team Sizes and Agent Loss》归入 强化学习、机器人、大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting data from wireless sensors can be challenging when limited communication infrastructure prevents them from offloading their measurements. In such settings, unmanned aerial vehicles (UAVs) can exploit their mobility to harvest data locally, while coordinated UAV teams can provide efficient and redundant coverage of remote areas. Multi-agent reinforcement learning (MARL) enables such teams to learn decentralized coordination policies. However, training separate policies for different team and sensor populations is costly, and fixed-population policies may be vulnerable to agent failures. This work proposes F-MADDPG, a flexible variant of Multi-Agent Deep Deterministic Policy Gradient (MADDPG) that supports data harvesting with varying numbers of wireless sensors and UAVs. The framework also accommodates unexpected catastrophic failures that permanently remove agents during a mission. We compare F-MADDPG with a MADDPG baseline that uses multilayer perceptrons (MLPs) and evaluate training strategies based on team-size sampling and exposure to agent terminations. The results show that F-MADDPG learns across the evaluated population sizes, completes missions faster than the baseline on average, benefits from inverse-cardinality team-size sampling compared with uniform sampling, remains effective after permanent agent losses, and gains no consistent benefit from exposure to failures during training.

</details>

---
