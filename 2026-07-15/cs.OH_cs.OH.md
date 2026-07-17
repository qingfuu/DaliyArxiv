# cs.OH | cs.OH | 2026-07-15

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Fuse-then-Detect_for_Passive_UAV_Localization_Using_Multi-UE_5G_Uplink_Signals|Fuse-then-Detect for Passive UAV Localization Using Multi-UE 5G Uplink Signals]]

![[assets/2607.11955_figure.png|800]]

- **arXiv**: [2607.11955](https://arxiv.org/abs/2607.11955)
- **PDF**: https://arxiv.org/pdf/2607.11955
- **详细分析**: [[20_Research/Papers/机器人/Fuse-then-Detect_for_Passive_UAV_Localization_Using_Multi-UE_5G_Uplink_Signals|Fuse-then-Detect for Passive UAV Localization Using Multi-UE 5G Uplink Signals]]
- **作者**: Wenyu Huang, Nuria González-Prelcic, Vishnu Ratnam, Murat Bayraktar, Charlie Jianzhong Zhang
- **cs 子类**: 
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Security

#### 研究背景与动机

《Fuse-then-Detect for Passive UAV Localization Using Multi-UE 5G Uplink Signals》归入 机器人 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-altitude uncrewed aerial vehicles (UAVs) can pose growing risks to airspace safety, security, and privacy. Cellular infrastructure can passively sense them without dedicated radar hardware by exploiting integrated sensing and communication (ISAC) technology. Most prior work exploits monostatic sensing or bistatic/multistatic configurations based on downlink measurements. To the best of our knowledge, this paper presents the first uplink framework, where multiple user equipments (UEs) transmit sounding reference signal (SRS) pilots and the base station (BS) receives the UAV-scattered echoes. Sensing from uplink SRS, however, introduces new challenges. Each UE has its own oscillator and timing loop, so the channel estimate at the BS carries residual timing, frequency, and amplitude impairments that corrupt the UAV delay and Doppler. Moreover, the UAV echo is weaker than both the line-of-sight (LOS) path and urban clutter, so detection from a single UE transmission is not reliable. We address these challenges by designing a LOS-referenced synchronization scheme and a joint detector. The synchronization reuses the existing timing advance (TA) command and an adjacent-occasion conjugate product to remove the residuals without additional signaling. Then the detector searches a shared 3D state space and accumulates evidence across UEs. It leverages a normalized contrast that exploits the bistatic geometry. We evaluate the framework in a cluttered urban scene at frequency range 1 (FR1) with four pedestrian UEs and a 100 MHz 5G New Radio (NR) waveform. The proposed pipeline achieves sub-nanosecond synchronization and a 4.84 m median 3D position error.

</details>

---
