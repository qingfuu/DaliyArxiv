# cs.NI | Networking and Internet Architecture | 2026-08-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/5G_ISAC-Based_UAV_Detection_and_3-D_Tracking_Using_Uplink_Sounding_Reference_Signals_on_an_End-to-End_O-RAN_Simulation_Testbed|5G ISAC-Based UAV Detection and 3-D Tracking Using Uplink Sounding Reference Signals on an End-to-End O-RAN Simulation Testbed]]

![[assets/2608.05826_figure.png|800]]

- **arXiv**: [2608.05826](https://arxiv.org/abs/2608.05826)
- **PDF**: https://arxiv.org/pdf/2608.05826
- **详细分析**: [[20_Research/Papers/机器人/5G_ISAC-Based_UAV_Detection_and_3-D_Tracking_Using_Uplink_Sounding_Reference_Signals_on_an_End-to-End_O-RAN_Simulation_Testbed|5G ISAC-Based UAV Detection and 3-D Tracking Using Uplink Sounding Reference Signals on an End-to-End O-RAN Simulation Testbed]]
- **作者**: Arun K. Gurung, Satha K. Sathananthan, Shiva R. Pokhrel
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《5G ISAC-Based UAV Detection and 3-D Tracking Using Uplink Sounding Reference Signals on an End-to-End O-RAN Simulation Testbed》归入 机器人 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Integrated Sensing and Communication (ISAC) lets cellular infrastructure serve communication users and sense on the same waveform. We present an end-to-end O-RAN simulation testbed for 5G ISAC targeting low-altitude UAV detection and 3-D tracking, built from open-source components: OpenAirInterface, FlexRIC and Sionna RT, in which the NR Uplink Sounding Reference Signal is repurposed as a passive radar waveform: a PHY-layer sensing stage inside the gNB produces detections that reach an Extended Kalman Filter tracking xApp over a custom E2 service model, with no change to the NR standard and no dedicated sensing waveform. A single bistatic pair leaves elevation unobservable, so the tracker needs a height prior; we remove it two independent ways and measure both - a planar receive array supplying a vertical aperture, and a second transmitter supplying range diversity. Both live results corroborate an offline ray-traced study of the same estimator, which converges from a deliberately wrong initial altitude to 1.8 m RMSE at a consistent filter, so altitude observability is established both in the signal-processing chain and end to end through the live stack. Detection coverage is preserved under a concurrent 10 Mbps uplink communications load.

</details>

---
