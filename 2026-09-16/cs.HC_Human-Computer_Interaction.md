# cs.HC | Human-Computer Interaction | 2026-09-16

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/机器人/Beyond_Gestures_Estimating_Full_Hand_Pose_and_Contact_Forces_from_Wrist-Worn_Pressure_Sensor_Array|Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array]]

![[assets/2609.16518_figure.jpg|800]]

- **arXiv**: [2609.16518](https://arxiv.org/abs/2609.16518)
- **PDF**: https://arxiv.org/pdf/2609.16518
- **详细分析**: [[20_Research/Papers/机器人/Beyond_Gestures_Estimating_Full_Hand_Pose_and_Contact_Forces_from_Wrist-Worn_Pressure_Sensor_Array|Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array]]
- **作者**: Svetoslav Kolev, Lingni Ma, Michael Goesele, Renzo De Nardi, Jakob Engel, Richard Newcombe
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Beyond Gestures: Estimating Full Hand Pose and Contact Forces from Wrist-Worn Pressure Sensor Array》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Capturing hand motion and interaction forces is critical for interactive computing, VR, and high-fidelity tactile demonstrations for robot learning. We introduce a wrist-worn pressure-sensing wristband that recovers continuous full-hand pose and distributed contact force on a single wearable. The system consists of flexible capacitive sensor arrays around the wrist, which require no electrical skin contact, and a recurrent network that maps the resulting pressure signal to hand state. Our key insight is that muscle contraction and tendon displacement produce pressure patterns, which correlate strongly with hand pose and interaction force. To validate this, we collect synchronized recordings of wrist pressure, optical motion-capture hand pose, and tactile-glove interaction force, covering isolated finger motion, fingertip-force stress tests, and natural hand-object manipulation. On isolated single-user motion the wristband attains $4.6^\circ$ mean finger-joint MAE, and across four users manipulating everyday objects it estimates per-finger contact force at $R^2=0.57$, which an external pose signal brings up to $0.75$. We see the wristband as one node in a constellation of everyday wearables -- e.g. paired with an egocentric camera -- adding the contact force that vision cannot observe and taking over when the hand is occluded.

</details>

---

### [[20_Research/Papers/具身智能/XRoboToolKit-T_Teleoperation_with_High_Stability_and_Precision_with_Tactile_Sensing_for_Contact-rich_Manipulation|XRoboToolKit-T: Teleoperation with High Stability and Precision with Tactile Sensing for Contact-rich Manipulation]]

![[assets/2609.16437_figure.png|800]]

- **arXiv**: [2609.16437](https://arxiv.org/abs/2609.16437)
- **PDF**: https://arxiv.org/pdf/2609.16437
- **详细分析**: [[20_Research/Papers/具身智能/XRoboToolKit-T_Teleoperation_with_High_Stability_and_Precision_with_Tactile_Sensing_for_Contact-rich_Manipulation|XRoboToolKit-T: Teleoperation with High Stability and Precision with Tactile Sensing for Contact-rich Manipulation]]
- **作者**: Xiwen Dengxiong, Xueting Wang, Ke Jing, Rui Li, Yunbo Zhang
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《XRoboToolKit-T: Teleoperation with High Stability and Precision with Tactile Sensing for Contact-rich Manipulation》归入 具身智能、机器人 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting high-quality robot data for contact-rich manipulation tasks is essential for enabling robots to acquire real-world skills. However, existing data collection solutions often lack the capability to obtain stable and high-frequency tactile feedback, limiting their effectiveness in contact-rich manipulation scenarios. In this work, we propose a versatile teleoperation system with tactile-driven assistance to enable high-frequency and stable contact-rich manipulation. The proposed XRoboToolKit-T teleoperation system incorporates a tactile-informed force control architecture, designed to ensure both stable and precise force control in contact-rich manipulation during teleoperation. The stabilizer haptic module rapidly analyzes the normal force distribution and infers pseudo shear force, enabling real-time tactile-based assistance during manipulation. The refiner haptic module integrates a vision-language-action model to predict and refine manipulation actions based on tactile sensing data and task descriptions. We apply the proposed teleoperation system to challenging contact-rich manipulation tasks, including grasping a deformable rubber pipette for liquid transfer and inserting a medical syringe into a vascular training pad, to demonstrate the effectiveness of tactile-informed force control. Furthermore, the system achieves higher data collection efficiency and improved manipulation stability compared to state-of-the-art teleoperation without tactile assistance.

</details>

---

### [[20_Research/Papers/大模型/SuperSenseDoctor_A_Multimodal_and_Contactless_Agent_for_Health_Tracking|SuperSenseDoctor: A Multimodal and Contactless Agent for Health Tracking]]

![[assets/2609.16257_figure.png|800]]

- **arXiv**: [2609.16257](https://arxiv.org/abs/2609.16257)
- **PDF**: https://arxiv.org/pdf/2609.16257
- **详细分析**: [[20_Research/Papers/大模型/SuperSenseDoctor_A_Multimodal_and_Contactless_Agent_for_Health_Tracking|SuperSenseDoctor: A Multimodal and Contactless Agent for Health Tracking]]
- **作者**: Xuwen Zhang, Zijian Lu, Yicheng Lei, Rui Qiu, Jiale Li, Yiping Zuo, Weibei Fan, Fu Xiao
- **cs 子类**: cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, Security

#### 研究背景与动机

《SuperSenseDoctor: A Multimodal and Contactless Agent for Health Tracking》归入 大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Population aging is increasing the need to monitor older adults safely and independently at home. However, cameras, wearables, and manual checks often introduce privacy, adherence, and attention burdens that hinder sustained health monitoring. This paper presents SuperSenseDoctor, a multimodal contactless agent architecture for long-term home health tracking. The system transforms WiFi, mmWave radar, and surface temperature into a persistent human health state. The system relies on fixed decision rules to conduct continuous daily monitoring and respond to pre-defined hazards. When abnormal signals appear, event-driven reasoning analyzes only standardized evidence to produce traceable care-support measures. In this manner, SuperSenseDoctor integrates sensing, temporal state, reasoning, and action into a unified and auditable loop. The calibrated multimodal pipeline achieves 1.994 bpm mean absolute error (MAE) and 3.142 bpm root mean square deviation (RMSD) for heart rate, 0.197 bpm MAE and 0.263 bpm RMSD for respiratory rate, and 96.5% fall-recognition accuracy. The evaluation also covers 2686 one-second states across 9 chronological intervals and reaches a 96.7% criterion-level Agent checklist pass rate. These results demonstrate the feasibility of a stateful contactless sensing-to-action architecture for long-term home health monitoring.

</details>

---
