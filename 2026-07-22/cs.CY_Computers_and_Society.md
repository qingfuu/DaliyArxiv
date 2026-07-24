# cs.CY | Computers and Society | 2026-07-22

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Delivery_Drone-Based_Participatory_Sensing_in_Dynamic_Environments|Reinforcement Learning for Delivery Drone-Based Participatory Sensing in Dynamic Environments]]

![[assets/2607.18874_figure.png|800]]

- **arXiv**: [2607.18874](https://arxiv.org/abs/2607.18874)
- **PDF**: https://arxiv.org/pdf/2607.18874
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_Delivery_Drone-Based_Participatory_Sensing_in_Dynamic_Environments|Reinforcement Learning for Delivery Drone-Based Participatory Sensing in Dynamic Environments]]
- **作者**: Xin Ouyang, Songxin Lei, Xusen Guo, Yutian Jiang, Sijie Ruan, Yuxuan Liang
- **cs 子类**: cs.CY, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 世界模型
- **相关性评分**: 2.12（加权：强化学习 0.96，世界模型 0.16，机器人 1）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Reinforcement Learning for Delivery Drone-Based Participatory Sensing in Dynamic Environments》归入 机器人、强化学习、世界模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, TSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Using Unmanned Aerial Vehicle (UAV) for urban sensing has emerged as a powerful paradigm to monitor the status of the city, e.g., air quality and noise levels, through agile aerial crowdsourcing. Despite this potential, existing UAV-based sensing approaches overlook environmental disturbances like wind that drastically impact drone velocity and energy efficiency. Consequently, directly applying existing methods to this joint delivery and sensing paradigm in dynamic environments faces two severe challenges: (1) scalability bottlenecks as fleet sizes expand; and (2) multi-timescale decision heterogeneity between macro task dispatching and micro velocity control. To tackle these, we formalize the problem as SensUAV and propose a Two TimeScale Reinforcement Learning framework (TSRL). Specifically, TSRL separates decision-making into two cooperative layers. At the macro level, a task-embedding sensing dispatcher handles scalability by separately encoding distinct task features and sequentially evaluating UAV suitability before task selection. At the micro level, a wind-aware velocity controller learns fine-grained velocity scheduling to adapt to dynamic environmental variations. Extensive experiments on real-world datasets demonstrate that TSRL significantly outperforms baselines, achieving average system profit improvements of 20.1% in Hangzhou and 46.6% in Shanghai.

</details>

---
