# cs.IT | Information Theory | 2026-11-04

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Timely_Ground-Station_Status_Delivery_via_UAV-Assisted_Data_Collection_and_Hierarchical_RL|Timely Ground-Station Status Delivery via UAV-Assisted Data Collection and Hierarchical RL]]

![[assets/2611.03884_figure.png|800]]

- **arXiv**: [2611.03884](https://arxiv.org/abs/2611.03884)
- **PDF**: https://arxiv.org/pdf/2611.03884
- **详细分析**: [[20_Research/Papers/强化学习/Timely_Ground-Station_Status_Delivery_via_UAV-Assisted_Data_Collection_and_Hierarchical_RL|Timely Ground-Station Status Delivery via UAV-Assisted Data Collection and Hierarchical RL]]
- **作者**: Xiangjian Gao, Mohammad Moltafet, Hamid R. Sadjadpour
- **cs 子类**: cs.IT
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，机器人 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Timely Ground-Station Status Delivery via UAV-Assisted Data Collection and Hierarchical RL》归入 机器人、强化学习 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider a UAV-assisted status-update system in which a rotary-wing unmanned aerial vehicle (UAV) collects updates from multiple sensors, stores the newest update of each sensor, and forwards selected buffered updates to a ground station (GS). We minimize a weighted sum of the time-average GS-side age of information (AoI) and UAV energy consumption over a finite horizon. The optimization is subject to half-duplex operation, sensor and UAV energy-causality constraints, transmission-rate and power limits, and a terminal-location constraint. Because collection changes the information age at the UAV but does not reduce the GS-side AoI until the buffered update is forwarded, mobility, collection, and forwarding decisions are coupled over time. We use a hierarchical AoI-energy actor-critic (HAE-AC) controller in which a coarse-timescale actor selects return-feasible UAV movements, while a deterministic per-slot scheduler constructs feasible collection or forwarding sets and assigns the minimum transmit power required for each scheduled transmission. In a 100-sensor deployment, HAE-AC reduces the average GS-side AoI by about 22% relative to an adaptive staleness-gated benchmark. Compared with forward-upon-collection, selective buffered forwarding reduces the number of downlink bursts by roughly 30% while increasing the number of collections per sensor by more than 23%.

</details>

---
