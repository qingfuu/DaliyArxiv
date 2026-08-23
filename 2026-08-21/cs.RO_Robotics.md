# cs.RO | Robotics | 2026-08-21

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/强化学习/Video2DoorTraversal_Push_Door_Traversal_via_Simulated_Door_Twins|Video2DoorTraversal: Push Door Traversal via Simulated Door Twins]]

![[assets/2608.20251_figure.png|800]]

- **arXiv**: [2608.20251](https://arxiv.org/abs/2608.20251)
- **PDF**: https://arxiv.org/pdf/2608.20251
- **详细分析**: [[20_Research/Papers/强化学习/Video2DoorTraversal_Push_Door_Traversal_via_Simulated_Door_Twins|Video2DoorTraversal: Push Door Traversal via Simulated Door Twins]]
- **作者**: Xincheng Tang, Yiji Chen, Youhan Xie, Wanyu Li, Zhengjie Shu, Lai Jiang, Wenkang Hu, Yitong Li, Jinchuang Zhang, Xibin Song, Ruigang Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Video2DoorTraversal: Push Door Traversal via Simulated Door Twins》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DoorGym, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Door opening and traversal is a long-horizon loco-manipulation task that requires precise handle interaction and coordinated base-arm control. We present Video2DoorTraversal, a single-video real-to-sim-to-real framework for wheel-legged mobile manipulators. Given one RGB video of a real door, DoorTwin reconstructs an instance-aligned, articulated, and simulation-ready door twin with realistic geometry and appearance. A simulation-in-the-loop agent converts the recovered articulation into a parameterized skill program and iteratively refines failed rollouts to generate physically executable demonstrations. These demonstrations are used to train ArticuACT, a dual-depth policy that predicts coordinated base, arm, and gripper commands using robot-centric camera conditioning and interaction-aware supervision. With all perception and policy inference running onboard, the system achieves a 96.57% average success rate across five real doors and an 80.95% zero-shot success rate on structurally similar unseen doors, while completing the full approach, opening, and traversal sequence in approximately 13s on average. Project Page: https://video2doortraversal.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Planning-Oriented_End-to-End_Autonomous_Driving_Architectures,_Evaluation,_and_Emerging_Paradigms|Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms]]

![[assets/2608.20111_figure.png|800]]

- **arXiv**: [2608.20111](https://arxiv.org/abs/2608.20111)
- **PDF**: https://arxiv.org/pdf/2608.20111
- **详细分析**: [[20_Research/Papers/具身智能/Planning-Oriented_End-to-End_Autonomous_Driving_Architectures,_Evaluation,_and_Emerging_Paradigms|Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms]]
- **作者**: Yanchen Guan, Xingcheng Liu, Bin Rao, Chengyue Wang, Guofa Li, Yunjian Li, Lishengsa Yue, Zhiyong Cui, Chengzhong Xu, Zhenning Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Planning-Oriented End-to-End Autonomous Driving: Architectures, Evaluation, and Emerging Paradigms》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PilotNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end autonomous driving has evolved from camera-to-control regression toward planning-oriented systems that use structured representations, trajectory-level outputs, and increasingly realistic evaluation protocols. This survey reviews this transition across behavior cloning, conditional imitation learning, privileged distillation, BEV and vectorized planning, unified perception-prediction-planning architectures, world-model-based planners, and vision-language-action systems. We argue that the key distinction in modern end-to-end driving is not whether intermediate representations are used, but whether they are learned, supervised, and evaluated to support safe, feasible, and route-compliant planning. To organize the literature, we synthesize existing methods along four axes: input representation, planning output, supervision signal, and evaluation protocol. We further examine the benchmark shift from open-loop trajectory matching to closed-loop simulation, non-reactive real-log evaluation, long-tail testing, and human-preference-aware metrics. Our analysis highlights that architectural progress is difficult to interpret without benchmark-consistent evaluation, and that displacement-based open-loop metrics alone provide limited evidence for safe and human-aligned driving. We conclude with open challenges in uncertainty-aware planning, learner-expert mismatch, runtime safety assurance, language-action grounding, world-model validation, and reproducible benchmarking.

</details>

---

### [[20_Research/Papers/机器人/Wave-Based_Bilateral_Teleoperation_between_Nonlinear_Manipulators_with_Direct_Contact_Force_Feedback|Wave-Based Bilateral Teleoperation between Nonlinear Manipulators with Direct Contact Force Feedback]]

![[assets/2608.20043_first_page.png|800]]

- **arXiv**: [2608.20043](https://arxiv.org/abs/2608.20043)
- **PDF**: https://arxiv.org/pdf/2608.20043
- **详细分析**: [[20_Research/Papers/机器人/Wave-Based_Bilateral_Teleoperation_between_Nonlinear_Manipulators_with_Direct_Contact_Force_Feedback|Wave-Based Bilateral Teleoperation between Nonlinear Manipulators with Direct Contact Force Feedback]]
- **作者**: G. Q. Bao Tran, Takanori Miyoshi, Ho Duc Tho
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Wave-Based Bilateral Teleoperation between Nonlinear Manipulators with Direct Contact Force Feedback》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study bilateral teleoperation between nonlinear, multi-DOF robotic manipulators in the presence of constant communication delays. Unlike classical wave-transformation architectures that transmit a coordinating force, we consider the case where the environmental force is reflected to the master side to enhance teleoperation transparency. Since direct contact force feedback might destabilize the closed-loop system, we first develop a passivity-shortage characterization for the Euler--Lagrange remote system using a linear matrix inequality (LMI) approach. An upper strictly passive communication law is then employed to compensate for the computed passivity shortage so that the closed-loop stability under delays as well as position and force synchronization are preserved under appropriate conditions. Simulations with nonlinear 2-DOF robotic manipulators in different settings illustrate our approach.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Highly_Dynamic_Skills_Transition_for_Quadruped_Jumping_Through_Constrained_Space|Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space]]

![[assets/2608.19977_figure.png|800]]

- **arXiv**: [2608.19977](https://arxiv.org/abs/2608.19977)
- **PDF**: https://arxiv.org/pdf/2608.19977
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Highly_Dynamic_Skills_Transition_for_Quadruped_Jumping_Through_Constrained_Space|Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space]]
- **作者**: Zeren Luo, Jiahui Zhang, Yimin Han, Ji Ma, Minghao Lu, Ioannis Havoutis, Peng Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.6（加权：具身智能 1.5，强化学习 0.2，机器人 0.9）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Learning Highly Dynamic Skills Transition for Quadruped Jumping Through Constrained Space》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although legged animals are capable of performing explosive motions while traversing confined spaces, replicating this behavior in quadrupedal robots has been a longstanding challenge. Here, we propose a hierarchical reinforcement learning pipeline that empowers the robots to perform aggressive locomotion through constrained obstacles--a narrow gate. The imitation learning technique is used to train the low-level policy, which mimics the behaviors of real animals and forms a set of diverse skills. The high-level controller, having an awareness of the capability of low-level skills and acquiring the gate information via vision-based detection, determines the suitable maneuvers with collision-free trajectories to traverse it dynamically. Notably, we also verify that this framework can be extended to other highly dynamic tasks. This is one of the first works that perform autonomous and agile aerial gate traversal tasks on ground-walking robots, extending the lifelike agility of legged robots to match that of their biological counterparts.

</details>

---

### [[20_Research/Papers/具身智能/MILD_Tractable_Terrain_Modeling_for_Learning_Improved_Bipedal_Locomotion_on_Deformable_Surfaces|MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces]]

![[assets/2608.19955_figure.png|800]]

- **arXiv**: [2608.19955](https://arxiv.org/abs/2608.19955)
- **PDF**: https://arxiv.org/pdf/2608.19955
- **详细分析**: [[20_Research/Papers/具身智能/MILD_Tractable_Terrain_Modeling_for_Learning_Improved_Bipedal_Locomotion_on_Deformable_Surfaces|MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces]]
- **作者**: Zeren Luo, Jiahui Zhang, Zhe Xu, Wanyue Li, Xinqi Li, Xuechao Chen, Zhangguo Yu, Annan Tang, Peng Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.4，机器人 0.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《MILD: Tractable Terrain Modeling for Learning Improved Bipedal Locomotion on Deformable Surfaces》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enabling robots to walk on yielding terrain is vital for applications ranging from disaster response to planetary exploration. While bipedal robots hold immense potential, their locomotion on deformable surfaces remains limited as current simulators fail to capture the spatiotemporal heterogeneity of such yielding substrates. We present MILD, featuring a physics-grounded discrete-element contact solver that accurately simulates spatially varying foot-terrain interactions. Complementing this model, we train a terrain-aware locomotion controller via deep reinforcement learning with latent modulation and proprioceptive estimation. Quantitative comparisons against state-of-the-art methods show our approach generates more diverse and realistic contact scenarios during training, resulting in controllers that exhibit natural adaptation on real deformable surfaces. Through hardware experiments, we demonstrate the system's capability for online terrain identification and adaptation across a wide range of surface stiffness.

</details>

---

### [[20_Research/Papers/机器人/Keeping_the_Franka_Emika_Panda_alive_a_ROS_2_stack_with_a_reliable_position_interface|Keeping the Franka Emika Panda alive: a ROS 2 stack with a reliable position interface]]

![[assets/2608.19740_figure.png|800]]

- **arXiv**: [2608.19740](https://arxiv.org/abs/2608.19740)
- **PDF**: https://arxiv.org/pdf/2608.19740
- **详细分析**: [[20_Research/Papers/机器人/Keeping_the_Franka_Emika_Panda_alive_a_ROS_2_stack_with_a_reliable_position_interface|Keeping the Franka Emika Panda alive: a ROS 2 stack with a reliable position interface]]
- **作者**: Antonio Langella, Davide Risi, Vincenzo Petrone, Enrico Ferrentino, Pasquale Chiacchio
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Keeping the Franka Emika Panda alive: a ROS 2 stack with a reliable position interface》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an open-source software stack that restores ROS 2 support for the Franka Emika Panda robot while resolving the long-standing unreliability of its external position control interface. We first analyze the root causes of unstable position control and show that the observed vibrations and protective stops arise from the timing of the external control loop and sampling jitter, rather than from limitations of the robot itself. Building on this analysis, we introduce an asynchronous hardware interface that decouples real-time communication from the ROS 2 control loop, a rate-matching mechanism for slower command sources, and a position-domain reference generation strategy that produces reliable, smooth position commands. Experimental validation shows that the proposed architecture reliably tracks velocity references by reducing motion artifacts introduced by the official implementation, and the stack is validated across motion planning, compliance control, position-controlled manipulation, and haptic teleoperation on two independent Panda platforms. By restoring a modern, reliable, and open ROS 2 ecosystem for the Panda, this work lowers the barrier to developing safe, responsive, and reproducible human-robot collaboration applications that integrate planning, perception, interaction, and shared autonomy. Code and videos are available on our website at https://sites.google.com/view/fer-ros2/.

</details>

---

### [[20_Research/Papers/具身智能/World-Model-Grounded_LLM_Planning_for_AUV_and_ASV_Navigation_Near_Offshore_Wind_Farms|World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms]]

![[assets/2608.19661_figure.png|800]]

- **arXiv**: [2608.19661](https://arxiv.org/abs/2608.19661)
- **PDF**: https://arxiv.org/pdf/2608.19661
- **详细分析**: [[20_Research/Papers/具身智能/World-Model-Grounded_LLM_Planning_for_AUV_and_ASV_Navigation_Near_Offshore_Wind_Farms|World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms]]
- **作者**: Markus Buchholz, Ignacio Carlucho, Yvan R. Petillot
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.6，世界模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《World-Model-Grounded LLM Planning for AUV and ASV Navigation Near Offshore Wind Farms》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GazeboSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can turn a natural-language mission into a sequence of robot actions, but they do not have a sense of physics: they cannot judge how long a command should run, or whether it will make the robot drift into an obstacle. We proposed the use of a world model to expand the capabilities of Large Language model-based planners. Our method has three components: a physics-grounded neural world model, a three-phase gradient-based trajectory optimizer, and a Model Predictive Controller (MPC)-style closed-loop replanner with a trust-region guard. The language model decides what to do, and the world model decides how long, whether that means driving eight thrusters through 6 DOF or two differential thrusters through 3 DOF. We evaluate two marine vehicle classes operating near offshore wind infrastructure: a 6-DOF Autonomous Underwater Vehicle (AUV) and a 3-DOF differential-drive Autonomous Surface Vehicle (ASV). In five benchmark missions per platform, both vehicles reach every goal with zero predicted collisions, and both transfer to GazeboSim under ocean current, waves, and thruster dynamics, remaining collision-free and cutting GazeboSim goal-distance error versus the ungrounded baseline by 70-82% (ASV) and roughly 93% (AUV), after a residual fine-tuning pass that separately reduces surrogate rollout Root Mean Square Error (RMSE) by 60% (AUV) and 69% (ASV). For the ASV we further demonstrate a Vision language model (VLM)-assisted semantic-mapping pipeline that extracts obstacles and environmental context from satellite imagery, nautical charts, and forecast Application Programming Interface (API) instead of onboard sensors, reaching 96% navigability accuracy as a drop-in replacement for hand-specified obstacle geometry.

</details>

---

### [[20_Research/Papers/机器人/Magnetically_Self-Sealed_MR_Haptic_Actuator_With_PWM-Based_Excitation_and_High-Fidelity_Torque_Control|Magnetically Self-Sealed MR Haptic Actuator With PWM-Based Excitation and High-Fidelity Torque Control]]

![[assets/2608.19635_figure.png|800]]

- **arXiv**: [2608.19635](https://arxiv.org/abs/2608.19635)
- **PDF**: https://arxiv.org/pdf/2608.19635
- **详细分析**: [[20_Research/Papers/机器人/Magnetically_Self-Sealed_MR_Haptic_Actuator_With_PWM-Based_Excitation_and_High-Fidelity_Torque_Control|Magnetically Self-Sealed MR Haptic Actuator With PWM-Based Excitation and High-Fidelity Torque Control]]
- **作者**: Dong Qiang, Tian Yuan, Song Yang, Kequan Xia, Thomas Reddyhoff, Yikun Zhang, Cheng Cheng, Min Yu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Magnetically Self-Sealed MR Haptic Actuator With PWM-Based Excitation and High-Fidelity Torque Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate and stable torque rendering is essential for safe and perceptive human--machine interaction. Magnetorheological fluid (MRF)-based actuators offer a compact and rapidly controllable solution for haptic feedback, but their practical implementation requires reliable fluid sealing, low-hysteresis excitation, accurate torque control, and stable long-duration operation. This article presents an integrated MRF haptic system featuring a compact magnetically self-sealed rotary actuator, low-hysteresis PWM operation, high-fidelity model-based torque rendering, and stable performance during long-time operation. Magnetostatic simulation guides the arrangement of magnetic and nonmagnetic materials to focus flux in the multidisk torque and permanent-magnet sealing regions, enabling a maximum 600 N$\cdot$mm/A output. Experiments show that higher PWM frequencies reduce hysteresis and improve repeatability. At 10 kHz, the response is represented by a nonlinear model that varies with the direction and speed of torque change. The real-time controller combines feedforward, hysteresis compensation, PI feedback, and sliding-mode correction. Compared with PID, it reduces square-wave overshoot, undershoot, and steady-state RMSE by 77.4\%, 61.9\%, and 68.3\%, respectively. It tracks sinusoidal and biomechanics-model-based references, and a 1.5-h test shows only a 2.5 $^\circ$C rise near the coil with no clear tracking loss. This high-fidelity torque rendering will fundamentally transform human--robot collaboration by making interactions safer, more efficient, and more intuitive.

</details>

---

### [[20_Research/Papers/具身智能/HiTac-WAM_A_Hierarchical_Tactile_World_Action_Model_for_Contact-Rich_Robot_Manipulation|HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation]]

![[assets/2608.19574_figure.png|800]]

- **arXiv**: [2608.19574](https://arxiv.org/abs/2608.19574)
- **PDF**: https://arxiv.org/pdf/2608.19574
- **详细分析**: [[20_Research/Papers/具身智能/HiTac-WAM_A_Hierarchical_Tactile_World_Action_Model_for_Contact-Rich_Robot_Manipulation|HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation]]
- **作者**: Chao Xue, Chaofan Zhang, Wenxuan Ma, Guocai Yao, Shaowei Cui, Shuo Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《HiTac-WAM: A Hierarchical Tactile World Action Model for Contact-Rich Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：UniTacVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World action models jointly predict future visual observations and actions, whereas existing tactile-aware variants typically represent future touch as an image or latent stream without modeling the physical dependencies that organize tactile states hierarchically. We present HiTac-WAM, a hierarchical tactile world action model that forecasts a sequence of future tactile states for each candidate action chunk before execution. The forecast factorizes into contact state, a 3D deformation field, and slip risk, organized as a directed hierarchy in which each downstream stage is conditioned on stop-gradient signals from preceding stages. A directed attention mask allows tactile queries to attend to the video-action context of each candidate while preventing video and action queries from attending to tactile tokens. For planning, HiTac-WAM ranks candidate action chunks using tactile forecasts and task-progress estimates. For execution, the selected tactile forecast is retained as a reference; persistent discrepancies between predicted and observed tactile states trigger corrective replanning. HiTac-WAM achieves a mean contact F1 of 0.921; under matched training budgets, the directed hierarchy reduces 3D displacement L2 error by 17.6% relative to the deformation-only predictor and improves slip AUPRC by 60.4% relative to the slip-only predictor. Across chip grasping, blackboard erasing, and USB insertion, selection guided by the hierarchical forecasts increases the average real-robot success rate from 31.1% to 61.1%, while the full system attains 72.2%.

</details>

---

### [[20_Research/Papers/机器人/When_Automata_Meet_Streams_Temporal_Logic_Compilation_for_Stream-Based_Robotics_Task_and_Motion_Planning|When Automata Meet Streams: Temporal Logic Compilation for Stream-Based Robotics Task and Motion Planning]]

![[assets/2608.19453_figure.png|800]]

- **arXiv**: [2608.19453](https://arxiv.org/abs/2608.19453)
- **PDF**: https://arxiv.org/pdf/2608.19453
- **详细分析**: [[20_Research/Papers/机器人/When_Automata_Meet_Streams_Temporal_Logic_Compilation_for_Stream-Based_Robotics_Task_and_Motion_Planning|When Automata Meet Streams: Temporal Logic Compilation for Stream-Based Robotics Task and Motion Planning]]
- **作者**: Sayem Nazmuz Zaman, Cyrus Neary
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《When Automata Meet Streams: Temporal Logic Compilation for Stream-Based Robotics Task and Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stream-based robotics Task and Motion Planning (TAMP) integrates discrete symbolic planning with dynamically generated continuous geometric parameters, such as poses, grasps, and trajectories. However, stream-based planners typically reason only about goal reachability, whereas long-horizon tasks also demand adherence to temporal specifications, such as safety-critical ordering, invariance, and liveness constraints. No methods currently exist to enforce such temporal constraints for stream-based solvers because streams generate an expanding geometric object set via iterative stream refinement loops during planning, rendering existing temporal-logic compilation techniques incompatible. We therefore present Synchronous Action Monitoring with Token Destruction (SAM-TD), a compilation method that enforces arbitrary Linear Temporal Logic over finite traces ($\textrm{LTL}_f$) specifications in stream-based TAMP. SAM-TD translates arbitrary $\textrm{LTL}_f$ constraints into automata and embeds regressed automaton guards into action schemas, which are pre-specified before planning begins. By doing so, SAM-TD can handle objects generated by streams during planning, thus circumventing the need to enumerate a fixed object set or modify the underlying planner. During search, SAM-TD synchronously updates automaton states and uses a validity token shared across all automata to prune constraint-violating branches. We show that SAM-TD supports dynamically generated stream objects from iterative stream refinements during plan search. Experimental results provide the first ever demonstration of stream-based TAMP under $\textrm{LTL}_f$ constraints in three robotics PDDLStream environments. Furthermore, on standard discrete PDDL benchmarks, SAM-TD is competitive with state-of-the-art temporal-constraint compilation methods.

</details>

---

### [[20_Research/Papers/具身智能/Hybrid_Feedback_Sampling_for_Sample-Efficient_Model_Predictive_Control|Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control]]

![[assets/2608.19443_figure.png|800]]

- **arXiv**: [2608.19443](https://arxiv.org/abs/2608.19443)
- **PDF**: https://arxiv.org/pdf/2608.19443
- **详细分析**: [[20_Research/Papers/具身智能/Hybrid_Feedback_Sampling_for_Sample-Efficient_Model_Predictive_Control|Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control]]
- **作者**: Chaoyi Pan, Zeji Yi, John Zhang, Zachary Manchester, Guannan Qu, Guanya Shi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Hybrid Feedback Sampling for Sample-Efficient Model Predictive Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Thanks to its parallelizability and flexibility, sampling-based Model Predictive Control (MPC) has become widely popular for controlling real-world robotic systems. However, for high-dimensional and open-loop unstable dynamical systems, the required number of samples to improve the control sequence will grow exponentially with the horizon, leading to poor sample efficiency and numerical instability. This paper investigates the instability of shooting methods in sampling-based MPC and shows that the optimal sampling proposal distribution can be realized by sampling with an optimized feedback policy. We refer to this algorithm as Feedback Sampling MPC (FS-MPC). FS-MPC involves a hybrid sampling design which balances local and global search based on the system stability and the available computation budget. Our theoretical analysis shows that our hybrid sampling approach achieves faster convergence than standard MPPI and better optimality than standard feedback sampling. Empirically, in diverse contact-rich control tasks like humanoid loco-manipulation and dexterous manipulation, we show that FS-MPC successfully tackles dynamically unstable tasks where standard sample-based approaches struggle, and strictly outperforms feedback policies alone. Finally, we validate our method on humanoid robot locomotion and manipulation tasks in the real world.

</details>

---

### [[20_Research/Papers/具身智能/Learning_the_Right_Abstraction_Neural_Reduced_Dynamics_for_Complex_Robot_Control|Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control]]

![[assets/2608.19375_first_page.png|800]]

- **arXiv**: [2608.19375](https://arxiv.org/abs/2608.19375)
- **PDF**: https://arxiv.org/pdf/2608.19375
- **详细分析**: [[20_Research/Papers/具身智能/Learning_the_Right_Abstraction_Neural_Reduced_Dynamics_for_Complex_Robot_Control|Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control]]
- **作者**: Harry Zhang, Dan Negrut
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 2.6（加权：具身智能 0.9，强化学习 0.2，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning the Right Abstraction: Neural Reduced Dynamics for Complex Robot Control》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-fidelity embodied AI simulators provide realistic evaluation of complex robotic systems, but their computational cost limits their direct use for large-scale reinforcement learning campaigns. We advocate the use of less accurate but more expeditious simulations, which might draw on data-driven, e.g., neural dynamics, models. This contribution argues that the practical value of a neural dynamics model for complex robot control lies in learning the \emph{right abstraction}: a reduced state that preserves the control-relevant physics of the high-fidelity system while enabling high-throughput policy learning. We develop a neural reduced dynamics (NRD) framework that separates the state the model propagates from what can be supplied as an input or recovered analytically, trains policies entirely inside the frozen learned model, and validates them back in the high-fidelity simulator. Two case studies instantiate it across three control tasks: terrain-aware HMMWV trajectory tracking on rigid, bumpy and deformable Continuum Representation Model (CRM) terrain; and goal reaching for a stock tracked vehicle and its front-mounted articulated arm. Every policy transfers back to the high-fidelity simulator. A single policy trained inside the terrain-conditioned dynamics model, and given no terrain input of its own, attains lower median and mean tracking error than both single-terrain specialists on all three terrains, including zero-shot bumpy terrain. Quantitatively, the tracked vehicle reaches 100 of 100 goals and the arm 97 of 100, with zero contacts or joint-limit violations. The NRD models advance roughly four orders of magnitude faster in simulated time than the high-fidelity simulator scenes they replace, making iterative on-policy learning practical and supporting neural reduced dynamics as a bridge between accurate but expensive physics simulation and scalable robot learning.

</details>

---

### [[20_Research/Papers/机器人/The_Missing_Touch_Spatially_Distributed_Tactile_Feedback_Brings_Teleoperation_Closer_to_Human_Dexterity|The Missing Touch: Spatially Distributed Tactile Feedback Brings Teleoperation Closer to Human Dexterity]]

![[assets/2608.19372_figure.png|800]]

- **arXiv**: [2608.19372](https://arxiv.org/abs/2608.19372)
- **PDF**: https://arxiv.org/pdf/2608.19372
- **详细分析**: [[20_Research/Papers/机器人/The_Missing_Touch_Spatially_Distributed_Tactile_Feedback_Brings_Teleoperation_Closer_to_Human_Dexterity|The Missing Touch: Spatially Distributed Tactile Feedback Brings Teleoperation Closer to Human Dexterity]]
- **作者**: Rohan Kota, Gregory Reardon, J. Edward Colgate
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《The Missing Touch: Spatially Distributed Tactile Feedback Brings Teleoperation Closer to Human Dexterity》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A fundamental challenge in robotic teleoperation is enabling an operator to control a remote robot as effortlessly and intuitively as their own hands. Despite the growing use of teleoperation to collect demonstration data for training autonomous robot policies, teleoperated robot performance still falls significantly short of human dexterity, even for basic tasks. Here, we present evidence that a key factor contributing to this performance gap is the absence of spatially distributed tactile feedback. Using a two-degree-of-freedom (DoF) bilateral force-feedback telemanipulator paired with a 32-DoF tactile fingertip display, we show that operator performance improves significantly when localized deformations on the remote manipulator are faithfully reproduced on the operator's fingertip. In a series of teleoperation tasks, reproducing distributed contact information not only accelerated task performance but also brought teleoperated movements closer to natural human behavior by minimizing corrective actions and task completion steps, thereby reducing the deviation between teleoperated and natural trajectories by 29$\unicode{x2013}$79%. Furthermore, we found that increasing the resolution of the tactile feedback$\unicode{x2014}$by refining how finely the measured displacements were quantized for reproduction$\unicode{x2014}$compressed the state-space distribution of teleoperated motions, which has been associated with improved training outcomes for autonomous robot policies. Together, these results suggest that spatially distributed tactile feedback is essential for closing the gap between human and teleoperated dexterity and training the next generation of autonomous robots.

</details>

---

### [[20_Research/Papers/机器人/Multi-Tool_Robotics_Enables_In-Situ_Sample_Manipulation_for_Time-Resolved_Synchrotron_Measurements|Multi-Tool Robotics Enables In-Situ Sample Manipulation for Time-Resolved Synchrotron Measurements]]

![[assets/2608.19280_figure.png|800]]

- **arXiv**: [2608.19280](https://arxiv.org/abs/2608.19280)
- **PDF**: https://arxiv.org/pdf/2608.19280
- **详细分析**: [[20_Research/Papers/机器人/Multi-Tool_Robotics_Enables_In-Situ_Sample_Manipulation_for_Time-Resolved_Synchrotron_Measurements|Multi-Tool Robotics Enables In-Situ Sample Manipulation for Time-Resolved Synchrotron Measurements]]
- **作者**: Aditya Bondada, Elizabeth M. Wall, Eric Yuan Xiao, Quinn C. Burlingame, Yueh-Lin Loo, Esther H. R. Tsai, Ruipeng Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Multi-Tool Robotics Enables In-Situ Sample Manipulation for Time-Resolved Synchrotron Measurements》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The high photon flux at synchrotron beamlines allows for the measurement of fast dynamical processes. However, beamline radiation-safety protocols prohibit human intervention during X-ray experiments, limiting the ability to perform versatile real-time sample manipulations during continuous data acquisition. Here we present a robotic platform at an X-ray scattering beamline to enable real-time sample handling and processing in the experimental hutch, revealing previously inaccessible transient in-situ dynamics in perovskite thin films. This modular multi-tool robotic architecture enables in-hutch sample manipulation beyond human-access constraints, establishing a foundation for automated and autonomous synchrotron experimentation.

</details>

---
