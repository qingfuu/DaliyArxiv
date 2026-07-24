# cs.OH | cs.OH | 2026-07-22

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/强化学习/Forecast-Assisted_Deep_Reinforcement_Learning_for_Energy_Management_of_Hydrogen-Enabled_Community_Microgrids|Forecast-Assisted Deep Reinforcement Learning for Energy Management of Hydrogen-Enabled Community Microgrids]]

![[assets/2607.18903_figure.png|800]]

- **arXiv**: [2607.18903](https://arxiv.org/abs/2607.18903)
- **PDF**: https://arxiv.org/pdf/2607.18903
- **详细分析**: [[20_Research/Papers/强化学习/Forecast-Assisted_Deep_Reinforcement_Learning_for_Energy_Management_of_Hydrogen-Enabled_Community_Microgrids|Forecast-Assisted Deep Reinforcement Learning for Energy Management of Hydrogen-Enabled Community Microgrids]]
- **作者**: Mohamed Atef, Sanath Alahakoon, Umme Mumtahina, Peter Wolfs, Tamer Khatib, Moslem Uddin
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.4（加权：强化学习 1.4）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Forecast-Assisted Deep Reinforcement Learning for Energy Management of Hydrogen-Enabled Community Microgrids》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hydrogen-enabled community microgrids can improve renewable energy utilization and local resilience, but their operation is complicated by uncertain residential demand, variable renewable generation, dynamic electricity prices, and the coupled dynamics of battery and hydrogen storage. This paper extends a previously developed proximal policy optimization (PPO) energy management system by adding multi-horizon community-load forecasts to the controller state. The framework is evaluated for a 1,000-household residential microgrid in Rockhampton, Australia. Forecast accuracy is mixed: the 1-h model achieves an RMSE of 239.32 kW and an R2 of 0.201, whereas the 6-h and 12-h horizons produce negative R2 values; the 24-h forecast achieves an RMSE of 249.79 kW, a MAPE of 62.52%, and an R2 of 0.126. Despite this limited predictive accuracy, the forecast-enriched PPO converges approximately 14.3% earlier than the non-predictive controller and increases the final reward by 8.3%. Annual savings rise from A$2,439.86 without forecasts to A$2,765.83 with forecasts, an incremental gain of A$325.97 (13.4%), while renewable utilization increases from 35.3% to 36.4%. Grid imports fall to 58,147.49 kWh. Resilience tests show a 20.1% battery protection value during grid outages, but no measurable forecast-specific resilience improvement. The results demonstrate that even imperfect forecasts can improve learning and economic dispatch while also showing that forecast calibration, common test conditions, and longer-duration outage studies are necessary before broader deployment claims can be made.

</details>

---

### [[20_Research/Papers/机器人/Rethinking_Joint_UAV_Placement_and_Beamforming_A_Correlation-Aware_Geometric_Approach|Rethinking Joint UAV Placement and Beamforming: A Correlation-Aware Geometric Approach]]

![[assets/2607.18668_figure.png|800]]

- **arXiv**: [2607.18668](https://arxiv.org/abs/2607.18668)
- **PDF**: https://arxiv.org/pdf/2607.18668
- **详细分析**: [[20_Research/Papers/机器人/Rethinking_Joint_UAV_Placement_and_Beamforming_A_Correlation-Aware_Geometric_Approach|Rethinking Joint UAV Placement and Beamforming: A Correlation-Aware Geometric Approach]]
- **作者**: Chaeyeon Kim, Kisong Lee
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: 未提取到

#### 研究背景与动机

《Rethinking Joint UAV Placement and Beamforming: A Correlation-Aware Geometric Approach》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In multiuser unmanned aerial vehicle (UAV)-assisted downlink communications, UAV placement and transmit beamforming are inherently coupled through the propagation geometry. However, fully joint design based on instantaneous channel state information (CSI) is impractical, because the small-scale fading depends on the UAV location to be optimized and thus is unavailable a priori. Moreover, existing joint placement and beamforming methods do not explicitly optimize the UAV position with respect to the geometry-dependent multiuser interference induced by inter-user steering correlation. To address this issue, we propose a correlation-aware geometric framework for joint UAV placement and beamforming. Specifically, the UAV position is first optimized based on long-term channel statistics, where the steering-vector correlation is incorporated into the placement design through a conservative Gaussian surrogate that avoids interference underestimation. The resulting nonconvex positioning problem is then handled using successive convex approximation, auxiliary-variable decoupling, and quadratic transform techniques. For the obtained UAV location, the transmit beamformer is then optimized using instantaneous CSI. Simulation results show that the proposed framework significantly improves the minimum user spectral efficiency by enhancing angular separability among users and reducing inter-user interference. These results demonstrate that UAV placement should be designed not only for desired-link enhancement but also for interference mitigation through geometry-aware user separation.

</details>

---
