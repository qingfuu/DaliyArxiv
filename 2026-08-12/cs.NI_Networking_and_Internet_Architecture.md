# cs.NI | Networking and Internet Architecture | 2026-08-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Multi-UAV_Tracking_Evaluation_Using_5G_Uplink_Signals_on_an_O-RAN_ISAC_Simulation_Testbed|Multi-UAV Tracking Evaluation Using 5G Uplink Signals on an O-RAN ISAC Simulation Testbed]]

![[assets/2608.10784_figure.png|800]]

- **arXiv**: [2608.10784](https://arxiv.org/abs/2608.10784)
- **PDF**: https://arxiv.org/pdf/2608.10784
- **详细分析**: [[20_Research/Papers/机器人/Multi-UAV_Tracking_Evaluation_Using_5G_Uplink_Signals_on_an_O-RAN_ISAC_Simulation_Testbed|Multi-UAV Tracking Evaluation Using 5G Uplink Signals on an O-RAN ISAC Simulation Testbed]]
- **作者**: Arun K. Gurung, Satha K. Sathananthan
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.6（加权：机器人 0.6）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Multi-UAV Tracking Evaluation Using 5G Uplink Signals on an O-RAN ISAC Simulation Testbed》归入 机器人 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We evaluate multi-target detection, association and tracking end to end on an O-RAN simulation testbed built from OpenAirInterface, FlexRIC and Sionna RT that repurposes the 5G NR uplink sounding reference signal as a passive radar waveform, and against what a counter-UAS command-and- control (C2) consumer requires rather than by detection alone. Three UAVs differing in altitude, velocity and radar cross section (-8 to -20 dBsm) fly one bistatic pair with an 8-element planar receive array. Once every target is detected the binding limit is contention, not sensitivity - two targets share one nearest detection in about 74% of coherent processing intervals, and targets are detected far more often than they are tracked. Elevation from that array cannot separate targets sharing a range-Doppler cell, but it decides association in 58% of intervals. Concurrent tracks are exported from the RAN Intelligent Controller (RIC) xApp to a C2 fusion node over a SAPIENT interface carrying a calibrated detection confidence, validated at schema level against a mock fusion node. The evaluation is emulation-only on one geometry with 10 noise seeds, the mechanisms are characterized and analyzed to identify the key factors influencing multi-target tracking performance.

</details>

---
