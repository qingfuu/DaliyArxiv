# cs.HC | Human-Computer Interaction | 2026-11-06

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/Transformer-Based_Trajectory_Prescription_for_sEMG-Optimizing_Robot-Mediated_Rehabilitation|Transformer-Based Trajectory Prescription for sEMG-Optimizing Robot-Mediated Rehabilitation]]

![[assets/2611.08295_figure.png|800]]

- **arXiv**: [2611.08295](https://arxiv.org/abs/2611.08295)
- **PDF**: https://arxiv.org/pdf/2611.08295
- **详细分析**: [[20_Research/Papers/机器人/Transformer-Based_Trajectory_Prescription_for_sEMG-Optimizing_Robot-Mediated_Rehabilitation|Transformer-Based Trajectory Prescription for sEMG-Optimizing Robot-Mediated Rehabilitation]]
- **作者**: Gabriel Parra, Kimia Khoshnami, Daniel S. Brown, Laura A. Hallock
- **cs 子类**: cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Transformer-Based Trajectory Prescription for sEMG-Optimizing Robot-Mediated Rehabilitation》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-mediated rehabilitation has the potential to deliver high-intensity, individualized therapy, but existing systems (which have not consistently improved outcomes) typically prescribe kinematic trajectories rather than explicitly targeting the neuromotor activations thought to support recovery. To address this gap, and ultimately enable activation-optimizing rehabilitation robot behavior, we present a personalizable transformer-based model mapping individuals' muscle activations (as measured via surface electromyography) to prescribed contact force trajectories when interacting with an end-effector rehabilitation robot. The model uses a transformer encoder-decoder leveraging rotary positional embeddings (RoPE) to generate a latent representation of trajectory-relevant and user-specific neuromotor factors, and augments trajectory prediction with flow matching to produce a distribution over plausible prescriptions biased toward the training distribution. Using data from 16 healthy participants completing 15 isometric trajectory tracking tasks, we evaluate generalization across held-out tasks and users, as well as the feasibility of user-specific fine-tuning within a therapy-session timescale. The model achieves mean trajectory prediction errors of &lt;8% on held out tasks and users, with effectively instantaneous deterministic inference and sub-second sampling of trajectory distributions. An initial test using the model during live rehabilitation tasks demonstrates that, on average, participants reach the target neuromotor activations with just 15% error accumulated throughout the task. These results provide a proof of concept for data-driven, activation-targeted trajectory prescription in robot-mediated rehabilitation and establish a foundation for future validation in clinical populations. Data and code have been open-sourced as part of the OpenRobotRehab project on SimTK.

</details>

---

### [[20_Research/Papers/具身智能/VREgo_Consumer_VR_Headsets_for_Learning_Robot_Manipulation_from_Egocentric_Demonstrations|VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations]]

![[assets/2611.07272_figure.png|800]]

- **arXiv**: [2611.07272](https://arxiv.org/abs/2611.07272)
- **PDF**: https://arxiv.org/pdf/2611.07272
- **详细分析**: [[20_Research/Papers/具身智能/VREgo_Consumer_VR_Headsets_for_Learning_Robot_Manipulation_from_Egocentric_Demonstrations|VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations]]
- **作者**: Liuchuan Yu
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《VREgo: Consumer VR Headsets for Learning Robot Manipulation from Egocentric Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EgoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

VREgo trains manipulation policies from demonstrations recorded on consumer VR headsets; we instantiate it with EgoKit on one such headset, the PICO 4 Ultra. On-device head and hand tracking and stereo object localisation allow the operator to begin a demonstration at the table. We adapt HumanEgo's preprocessing to estimate grasp thresholds per recording, update object positions after release, and propagate segmentation masks between keyframes. We evaluate policies in simulation on two tabletop tasks recorded by one operator. For cube placement, we compare PICO and Project Aria recordings of the same 41 layouts. With 40 training demonstrations, the PICO policies placed the cube on the tray in 67, 74, and 60 of 100 evaluation layouts across three training seeds. The corresponding Aria results were 73, 78, and 0. For a two-stage stacking task recorded with the PICO alone, the baseline placed the block on the tray in 94 of 100 layouts and met the end-of-episode criterion for both placements in two. In one diagnostic episode, repeated replanning deferred release beyond the eight executed steps. Demonstration replays also showed that the open gripper could displace the cube before grasping it. After adapting the training trajectories and adding task-specific execution rules that use simulator object positions, the system met both placement criteria in 93.8% of episodes across four evaluation noise seeds. The same 100 layouts informed rule development and evaluation. VREgo is available at https://vrego.chuange.org/.

</details>

---
