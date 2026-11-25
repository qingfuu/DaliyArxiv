# cs.NI | Networking and Internet Architecture | 2026-11-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Path-Aware_Fusion_of_Infrastructure_RF_Sensing_and_Robot_Perception_in_a_Live_Robotic_Digital_Twin|Path-Aware Fusion of Infrastructure RF Sensing and Robot Perception in a Live Robotic Digital Twin]]

![[assets/2611.27497_figure.png|800]]

- **arXiv**: [2611.27497](https://arxiv.org/abs/2611.27497)
- **PDF**: https://arxiv.org/pdf/2611.27497
- **详细分析**: [[20_Research/Papers/机器人/Path-Aware_Fusion_of_Infrastructure_RF_Sensing_and_Robot_Perception_in_a_Live_Robotic_Digital_Twin|Path-Aware Fusion of Infrastructure RF Sensing and Robot Perception in a Live Robotic Digital Twin]]
- **作者**: Alberto Martínez Méndez, Antonio de la Oliva, Carlos J. Bernardos
- **cs 子类**: cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.6（加权：机器人 1.6）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Path-Aware Fusion of Infrastructure RF Sensing and Robot Perception in a Live Robotic Digital Twin》归入 机器人 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robots in industrial workspaces must react to people that their onboard sensors cannot yet observe. Communication infrastructure can fill part of this gap by acting as a sensor, but its observations differ from camera and LiDAR evidence in meaning, spatial support, and rate. We present a live robotic Digital Twin (DT) that integrates heterogeneous sensing branches, a commodity 60-GHz link, joint Wi-Fi/5G sensing, a fixed camera, and robot-borne LiDAR, as spatially grounded observations with explicit freshness, and that uses the robot's live pose and heading to decide whether evidence lies on the path the robot is about to sweep. We show that a 60-GHz link carrying near-gigabit traffic detects human presence through the phase signature of its antenna array (balanced accuracy 0.98 on unseen sessions and 0.999 from one day to the next in a first site), but that a second site with a different link geometry requires a site-specific model (0.98 on unseen sessions after retraining, 0.73 without). On a Unitree Go2 patrolling under the DT, every person entering the camera field or the 60-GHz link stopped the robot (20/20); for the camera, the median time from physical entry to standstill was 1.83 s, of which detection, DT update, and networking take about 0.15 s and the rest is the 0.5-s confirmation and the robot's braking. Path-aware gating removed all stops caused by off-path presence (5 stops versus 0 for the same scenario), stale branches stopped the robot in fail-safe mode (6/6) and were ignored otherwise (0/6), and five unattended laps produced no false stop.

</details>

---
