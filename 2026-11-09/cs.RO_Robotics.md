# cs.RO | Robotics | 2026-11-09

#arxiv #ComputerScience

**论文数**: 30

### [[20_Research/Papers/机器人/Locating_Contact_on_Tendon-Driven_Continuum_Robots_From_Tendon_Measurements_Alone_via_Constrained_Moving_Horizon_Estimation|Locating Contact on Tendon-Driven Continuum Robots From Tendon Measurements Alone via Constrained Moving Horizon Estimation]]

![[assets/2611.09877_figure.png|800]]

- **arXiv**: [2611.09877](https://arxiv.org/abs/2611.09877)
- **PDF**: https://arxiv.org/pdf/2611.09877
- **详细分析**: [[20_Research/Papers/机器人/Locating_Contact_on_Tendon-Driven_Continuum_Robots_From_Tendon_Measurements_Alone_via_Constrained_Moving_Horizon_Estimation|Locating Contact on Tendon-Driven Continuum Robots From Tendon Measurements Alone via Constrained Moving Horizon Estimation]]
- **作者**: Haitham El-Hussieny
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Locating Contact on Tendon-Driven Continuum Robots From Tendon Measurements Alone via Constrained Moving Horizon Estimation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tendon-driven continuum robots can reach through constrained spaces, but contact along their bodies is invisible to the sensors at their motors. We show that this is a structural limitation rather than a tuning problem: the map from contact forces to tendon measurements has a null space of dimension at least seven, so no estimator that leaves the contact support free can locate contact. When the obstacle geometry is known, however, non-penetration and complementarity make the contact force locally identifiable, and we prove that the resulting system with unknown contact inputs is locally exponentially strongly detectable. We present a constrained moving horizon estimator (MHE) that encodes these conditions and runs in real time as one quadratic program per sample, and we give a local, mode-wise robust stability result for it. In a finite- element benchmark of a two-section robot pressing and sliding on a wall, the estimator located contact to 0.9 mm and estimated contact force to 0.22 N, compared with 65 mm and 0.72 N for a tuned extended Kalman filter (EKF) with state projection. The estimator tolerated millimeter- level errors in the obstacle position and unmodeled wall friction, under which the projected EKF failed. Under randomized model mismatch over 40 trials, including unmodeled tendon friction, it remained better in force and location in every trial. Without contact, the MHE offered no advantage over the EKF, which confirms that its benefit comes from the contact constraints. This report extends a letter submitted to IEEE Control Systems Letters with complete proofs and additional experiments.

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_Whole-body_Loco-manipulation_Using_a_Snake_Robot|Autonomous Whole-body Loco-manipulation Using a Snake Robot]]

![[assets/2611.09777_figure.png|800]]

- **arXiv**: [2611.09777](https://arxiv.org/abs/2611.09777)
- **PDF**: https://arxiv.org/pdf/2611.09777
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_Whole-body_Loco-manipulation_Using_a_Snake_Robot|Autonomous Whole-body Loco-manipulation Using a Snake Robot]]
- **作者**: Adarsh Salagame, Henry Noyes, Haroon Hublikar, Alireza Ramezani
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Autonomous Whole-body Loco-manipulation Using a Snake Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Snake robots can leverage their hyper-redundant morphology for both locomotion and manipulation through distributed body contact but whole-body loco-manipulation is particularly challenging since the entire body serves simultaneously as propulsive mechanism and manipulation tool Prior work on wheeled legged and snake robot platforms has decoupled these functions through dedicated appendages body segmentation or grippers We present closed-loop loco-manipulation with our snake robot COBRA without this distinction such that any part of the body may make contact We develop a contact-implicit dynamic model unifying robot-ground robot-object and object-ground interactions within a Moreau-Jean time-stepping framework and formulate a trajectory optimization over the full-order dynamics guided by a geometric planner and nominal proportional controller to autonomously push an object to a goal location during sidewinding We validate the planner and controller on hardware across varied configurations and present simulation results for a simplified trajectory optimization that resolves robot-object and object-ground contacts

</details>

---

### [[20_Research/Papers/机器人/A_wearable_input_output_interface_learns_personalized_models_of_haptic_perception|A wearable input/output interface learns personalized models of haptic perception]]

![[assets/2611.09708_first_page.png|800]]

- **arXiv**: [2611.09708](https://arxiv.org/abs/2611.09708)
- **PDF**: https://arxiv.org/pdf/2611.09708
- **详细分析**: [[20_Research/Papers/机器人/A_wearable_input_output_interface_learns_personalized_models_of_haptic_perception|A wearable input/output interface learns personalized models of haptic perception]]
- **作者**: Wen Li, E. Magnus Adams, Zijie Xu, Jiawen Yao, Aybala Esmer, Xiaoyue Ni, Bozhi Tian, Pedro Lopes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《A wearable input/output interface learns personalized models of haptic perception》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wearable haptic interfaces deliver physical stimuli to the skin, yet perceived locations vary widely across users and diverge from actuator locations, particularly for emergent tactile-feedback techniques. We developed a wearable haptic input/output (I/O) device integrating a 36-channel electrotactile array with capacitive touch sensing, enabling stimulation and user-reported percept locations to be registered within the same body-referenced coordinate frame. In 24 participants, the device revealed electrotactile and referred-thermal perceptual maps with notable interparticipant variability. Despite this variability, both modalities retained electrode-pair-specific spatial structure across participants. Tactile and thermal percepts also showed spatial correspondence, whose strength varied across participants. These findings motivated our human-in-the-loop calibration framework, which adapts a forward-prediction strategy to individual users and generates personalized perceptual models. These models enabled inverse rendering by selecting stimulation patterns predicted to generate a target percept for a specific user. Using these models, we demonstrate personalized haptic rendering in haptic-guided robot teleoperation, visual-to-haptic sensory substitution, interpersonal haptic communication, and virtual reality (VR). Together, this platform provides a route toward adaptive haptic interfaces that measure, model, and render according to each user's perception.

</details>

---

### [[20_Research/Papers/具身智能/ODEAction_From_Predicting_Chunks_to_Evolving_Actions|ODEAction: From Predicting Chunks to Evolving Actions]]

![[assets/2611.09672_figure.png|800]]

- **arXiv**: [2611.09672](https://arxiv.org/abs/2611.09672)
- **PDF**: https://arxiv.org/pdf/2611.09672
- **详细分析**: [[20_Research/Papers/具身智能/ODEAction_From_Predicting_Chunks_to_Evolving_Actions|ODEAction: From Predicting Chunks to Evolving Actions]]
- **作者**: Qishen Wang, Pengxiang Ding, Shifeng Bao, Mingyang Sun, Hengtao Li, Yi Gao, Baohua Yin, Yang Liu, Jiajun Fu, Jiacheng Liu, Changjing He, Peiyang Li...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《ODEAction: From Predicting Chunks to Evolving Actions》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EBench, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models typically generate actions in chunks, organizing continuous robot execution into separately predicted segments and thus introducing potential discontinuities at action-chunk transitions. We propose ODEAction, a chunk-free action generation paradigm that replaces action-chunk prediction with Continuous Action Evolution. Given visual observations, language instructions, and robot proprioceptive information, ODEAction learns an action transition field defined over action space, where a transition vector characterizes the evolution rate of the current action with respect to evolution time. During execution, the model takes the current action as its initial condition and integrates the learned field using an ordinary differential equation (ODE), recursively generating subsequent actions with explicit dependencies. ODEAction is implemented as an action head and does not depend on a specific vision-language backbone architecture. Experiments on LIBERO, EBench, RoboTwin, and real robots show that ODEAction improves both task performance and trajectory quality over matched action-chunking baselines, with particularly pronounced gains on fine manipulation tasks.

</details>

---

### [[20_Research/Papers/机器人/LACART_Lookahead-Augmented_Collision_Avoidance_and_Reference_Tracking_Strategies_for_Safety-Critical_Robots|LACART: Lookahead-Augmented Collision Avoidance and Reference Tracking Strategies for Safety-Critical Robots]]

![[assets/2611.09640_figure.png|800]]

- **arXiv**: [2611.09640](https://arxiv.org/abs/2611.09640)
- **PDF**: https://arxiv.org/pdf/2611.09640
- **详细分析**: [[20_Research/Papers/机器人/LACART_Lookahead-Augmented_Collision_Avoidance_and_Reference_Tracking_Strategies_for_Safety-Critical_Robots|LACART: Lookahead-Augmented Collision Avoidance and Reference Tracking Strategies for Safety-Critical Robots]]
- **作者**: Pedro Lopes, Amit Shivam, Luis Tiago Paiva
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《LACART: Lookahead-Augmented Collision Avoidance and Reference Tracking Strategies for Safety-Critical Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous racing provides a demanding testbed for collision avoidance under tight geometric and computational constraints. Building on a recent conference contribution and a master's dissertation, LACART combines lookahead-based control barrier functions (CBFs), a relaxed control Lyapunov function (CLF), and quadratic programming (QP) to modify nominal vehicle commands for obstacle avoidance and reference tracking. The method handles circular obstacles and track boundaries in a common optimisation layer. Comparative simulation results against Huang \emph{et al.} \cite{r9} show similar full-track paths and lower median computation times: 0.31 versus 0.33 ms per step and 0.023 versus 0.025 ms per QP solve. The dissertation further demonstrates a 1:43-scale vehicle with camera-based estimation and wireless actuation at a reported 25 Hz control rate. We identify the conditions linking lookahead-point clearance to body clearance, illustrate hardware limitations, and propose a recorded demonstration of safety intervention and recovery. The contribution targets ground-robot collision avoidance and real-time safety monitoring.

</details>

---

### [[20_Research/Papers/强化学习/DKWBC_Decoupling_Motion_Tracking_and_Balancing_for_Humanoid_Whole-Body_Control|DKWBC: Decoupling Motion Tracking and Balancing for Humanoid Whole-Body Control]]

![[assets/2611.09605_figure.png|800]]

- **arXiv**: [2611.09605](https://arxiv.org/abs/2611.09605)
- **PDF**: https://arxiv.org/pdf/2611.09605
- **详细分析**: [[20_Research/Papers/强化学习/DKWBC_Decoupling_Motion_Tracking_and_Balancing_for_Humanoid_Whole-Body_Control|DKWBC: Decoupling Motion Tracking and Balancing for Humanoid Whole-Body Control]]
- **作者**: Dingkun Wei, Zehong Shen, Huaijin Pi, Xueyang Wang, Xing Zhu, Hujun Bao, Yujun Shen, Xiaowei Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《DKWBC: Decoupling Motion Tracking and Balancing for Humanoid Whole-Body Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid whole-body control requires a robot to track diverse reference motions while maintaining balance under gravity, torque limits, contact switching, and external disturbances. Existing reinforcement-learning-based trackers typically learn control outputs that jointly address motion tracking and balance. However, similar reference poses can correspond to substantially different dynamic demands, requiring a unified policy to learn motion-dependent control requirements alongside balance corrections. This can complicate learning and lead to high-frequency fluctuations in control outputs. We propose DKWBC, a dynamics-informed whole-body control framework that combines explicit model-based tracking with a learned balancing residual. Inspired by the model-based and environmental-wrench contributions to joint torques in floating-base dynamics, DKWBC uses inverse-dynamics feedforward and joint PD feedback to supply tracking torques, while a residual policy learns additional joint-torque corrections for balanced execution. By explicitly accounting for motion-dependent torque demands, this structure simplifies the policy's learning task. Experiments in simulation and on real hardware demonstrate that a single learned balancing policy generalizes across motion datasets while maintaining accurate motion tracking and balance across ground support, attached payloads, and physical interaction. Project page: https://robbyant-research.github.io/DKWBC/.

</details>

---

### [[20_Research/Papers/机器人/Extended_Model-Based_Learned_Inertial_Odometry|Extended Model-Based Learned Inertial Odometry]]

![[assets/2611.09584_figure.png|800]]

- **arXiv**: [2611.09584](https://arxiv.org/abs/2611.09584)
- **PDF**: https://arxiv.org/pdf/2611.09584
- **详细分析**: [[20_Research/Papers/机器人/Extended_Model-Based_Learned_Inertial_Odometry|Extended Model-Based Learned Inertial Odometry]]
- **作者**: Sasanka Kuruppu Arachchige, Joni-Kristian Kämäräinen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Extended Model-Based Learned Inertial Odometry》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IONet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inertial odometry is a compelling approach to state estimation for agile quadrotor flight due to its affordability, low weight, and robustness to perceptual degradation. However, relying only on integrated inertial measurements is impractical, as sensor errors and time-varying biases lead to significant pose drift. Although recent advances have enabled inertial odometry for drone racing, existing approaches show limited generalization to trajectories not seen during training. This work improves generalization by adopting a body-frame representation and incorporating body-frame torque dynamics into the learning pipeline. The learned model predicts short-horizon relative displacements, which are fused with IMU measurements in an Extended Kalman Filter. Experimental results show that the proposed method outperforms the previous state-of-the-art learned inertial odometry approach for quadrotor pose estimation on unseen trajectories. An additional evaluation on four public quadrotor datasets, with whole trajectory shapes held out of training, confirms a lower velocity error on every held-out set and shows that the torque input is most informative when it is derived from the rotor signals. Code, data pipeline and trained models are publicly available.

</details>

---

### [[20_Research/Papers/具身智能/Lightweight_Path-Aware_Frontier_Re-ranking_for_LiDAR-Based_UAV_Exploration|Lightweight Path-Aware Frontier Re-ranking for LiDAR-Based UAV Exploration]]

![[assets/2611.09561_figure.png|800]]

- **arXiv**: [2611.09561](https://arxiv.org/abs/2611.09561)
- **PDF**: https://arxiv.org/pdf/2611.09561
- **详细分析**: [[20_Research/Papers/具身智能/Lightweight_Path-Aware_Frontier_Re-ranking_for_LiDAR-Based_UAV_Exploration|Lightweight Path-Aware Frontier Re-ranking for LiDAR-Based UAV Exploration]]
- **作者**: Duc Manh Do, Thanh Nguyen Canh, Ngoc Minh Do, Mai Thanh Thai, Xiem HoangVan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Lightweight Path-Aware Frontier Re-ranking for LiDAR-Based UAV Exploration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous 3D exploration with UAVs requires efficient target selection under limited flight time and onboard computation. In conventional Euclidean-distance-based frontier pipelines, geometric distance may poorly represent the actual collision-free travel cost in cluttered environments, leading to inefficient frontier choices. This paper presents a lightweight path-aware frontier re-ranking method for LiDAR-based UAV exploration. The method first retains a small top-N set of promising frontier candidates using a lightweight utility function and then applies time-bounded RRT* planning to estimate their feasible path costs for re-ranking. The path generated for the selected frontier is further reused for navigation to reduce redundant global planning. Experiments in three warehouse-like environments show that the proposed method consistently produces shorter exploration trajectories than conventional frontier baselines, with traveled-distance reductions of up to 14.1%, while reducing exploration time by up to 9.5% in two environments and remaining competitive in the third. The method maintains map detail comparable to the conventional OctoMap-based baseline, demonstrating an effective trade-off between exploration efficiency and mapping quality.

</details>

---

### [[20_Research/Papers/机器人/Mechanical_Interaction_Sensing_for_Robotic_Kiwifruit_Handling_with_an_Optoelectronic_Soft_Suction_Cup|Mechanical Interaction Sensing for Robotic Kiwifruit Handling with an Optoelectronic Soft Suction Cup]]

![[assets/2611.09468_figure.png|800]]

- **arXiv**: [2611.09468](https://arxiv.org/abs/2611.09468)
- **PDF**: https://arxiv.org/pdf/2611.09468
- **详细分析**: [[20_Research/Papers/机器人/Mechanical_Interaction_Sensing_for_Robotic_Kiwifruit_Handling_with_an_Optoelectronic_Soft_Suction_Cup|Mechanical Interaction Sensing for Robotic Kiwifruit Handling with an Optoelectronic Soft Suction Cup]]
- **作者**: Romina Adhami, Ebrahim Shahabi, Alessio Mondini, Samuel M. Youssef, Cosimo Della Santina, Gualtiero Volpe, Barbara Mazzolai
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Mechanical Interaction Sensing for Robotic Kiwifruit Handling with an Optoelectronic Soft Suction Cup》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic handling of delicate fruit benefits from compliant contact and quantitative sensing of the mechanical interaction at the end-effector. This study investigates an optoelectronic soft suction cup with a kiwifruit-specific bicomponent design for estimating interaction forces during contact with real fruit. During known-contact intervals, the optical signals accurately estimate interaction force on fruits excluded from model training: the best shallow network achieves grouped out-of-fold pooled R-squared = 0.968 +/- 0.005 (MAE = 0.138 N), with a median per-fruit held-out R-squared = 0.973 (MAE = 0.134 N). A simple monotonic mapping from the mean optical response alone achieves R-squared = 0.925 +/- 0.005, showing that substantial force-related information is already present in the optical response. Leave-one-collection-day-out validation remains strong (R-squared = 0.955 +/- 0.031), supporting robustness across acquisition sessions. As an exploratory secondary analysis, binary Soft/Firm classification from compression-test reference labels achieves moderate balanced accuracy (approximately 0.705) under grouped held-out-fruit validation, while finer three-class grading shows limited performance.

</details>

---

### [[20_Research/Papers/强化学习/Horizon-Coupled_Obstacle_Guidance_for_Relative-Action_Diffusion_Policies|Horizon-Coupled Obstacle Guidance for Relative-Action Diffusion Policies]]

![[assets/2611.09340_figure.png|800]]

- **arXiv**: [2611.09340](https://arxiv.org/abs/2611.09340)
- **PDF**: https://arxiv.org/pdf/2611.09340
- **详细分析**: [[20_Research/Papers/强化学习/Horizon-Coupled_Obstacle_Guidance_for_Relative-Action_Diffusion_Policies|Horizon-Coupled Obstacle Guidance for Relative-Action Diffusion Policies]]
- **作者**: Guangyuan Wang, Haishan Xia, Zitao Zhang, Kejia Chen, Yuanchen Sun, Zhenguo Sun, Donghao Zhang, Yu Zhang, Alois Knoll
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Horizon-Coupled Obstacle Guidance for Relative-Action Diffusion Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world robot deployment requires adapting learned policies to unseen obstacles without collecting new demonstrations or retraining. Existing policy-level guidance often applies obstacle corrections independently at individual horizon steps, which may address local obstacle violations but fail to coordinate the action sequence into a complete, task-directed detour. How obstacle responses should be propagated across the action horizon to coordinate complete, task-directed avoidance motion remains underexplored. We introduce an inferencetime obstacle-guidance framework for pretrained relative-action diffusion policies. It rolls out cumulative relative actions into a workspace trajectory, evaluates obstacle interactions along the trajectory with an SDF-based obstacle model, and propagates each obstacle response to all contributing action increments during denoising. Real-robot experiments across seven obstacleconstrained scenarios spanning four manipulation tasks show that our method achieves 105/140 (75.0%) collision-free task successes, compared with 8/140 (5.7%) for absolute-action pointwise guidance. Ablations show that the relative-action horizoncoupled formulation provides the larger observed improvement across both obstacle models.

</details>

---

### [[20_Research/Papers/具身智能/MDF++_Visuo-Tactile_World_Action_Model_with_End-to-end_Representation_Learning|MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning]]

![[assets/2611.09293_figure.png|800]]

- **arXiv**: [2611.09293](https://arxiv.org/abs/2611.09293)
- **PDF**: https://arxiv.org/pdf/2611.09293
- **详细分析**: [[20_Research/Papers/具身智能/MDF++_Visuo-Tactile_World_Action_Model_with_End-to-end_Representation_Learning|MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning]]
- **作者**: Zixuan Huang, Jinhao Yu, Zachary Charlick, Dmitry Berenson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《MDF++: Visuo-Tactile World Action Model with End-to-end Representation Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, world-action models (WAMs) have emerged as a powerful framework for robot manipulation. By jointly modeling action generation and future observation prediction, WAMs can act and anticipate the outcomes of the actions. However, existing WAMs typically rely on frozen pretrained encoders trained with reconstruction, which may not produce representations well suited for robot control. In this paper, we tackle the problem of learning physicallygrounded, control-relevant representations for WAMs. We propose MDF++, a visuo-tactile world-action model that learns latent representations of multisensory observations end-to-end with a diffusion backbone. While naive joint training can lead to feature collapse, MDF++ introduces a multi-task learning strategy that leverages cross-modal correlations to learn task-relevant representations. We evaluate MDF++ on a suite of contact-rich manipulation tasks, including realworld bolt screwing and nut mating, and show that it outperforms WAMs built on frozen pretrained representations by up to 50%. Additional videos are available on our website: jointmdf.github.io.

</details>

---

### [[20_Research/Papers/强化学习/SUGARv2_Learning_Diverse_Visual_Humanoid_Loco-Manipulation_Skills_from_Synthesized_Interaction_References|SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References]]

![[assets/2611.09266_figure.png|800]]

- **arXiv**: [2611.09266](https://arxiv.org/abs/2611.09266)
- **PDF**: https://arxiv.org/pdf/2611.09266
- **详细分析**: [[20_Research/Papers/强化学习/SUGARv2_Learning_Diverse_Visual_Humanoid_Loco-Manipulation_Skills_from_Synthesized_Interaction_References|SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References]]
- **作者**: Tianshu Wu, Tianxiang Gui, Yue Chen, Tingxu Liu, Ziye Peng, Guangjie Yang, Xiangqi Kong, Ye Shi, Jingya Wang, Hao Dong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SUGARv2: Learning Diverse Visual Humanoid Loco-Manipulation Skills from Synthesized Interaction References》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling up visual humanoid loco-manipulation skill acquisition requires reducing the human effort needed as tasks and spatial configurations expand, particularly in demonstration collection and task-specific training design. We present SUGARv2, a unified framework for learning diverse visual humanoid loco-manipulation skills through interaction reference synthesis and a shared training pipeline. To obtain diverse references at low cost, we adapt reusable task templates to different spatial configurations, synthesizing coordinated robot and object motions. To reduce task-specific reward design and training effort, we use reference-based imitation as a common learning objective across tasks. We first train privileged teachers to execute these references, then train visual policies through teacher distillation and reinforcement learning with the same reference-based mimic rewards, using diverse object instances and visual domain randomization to support visual generalization and sim-to-real transfer. Across five humanoid loco-manipulation tasks, SUGARv2 achieves a mean success rate of 91.0% in simulation. Deployment on a real humanoid robot further demonstrates successful sim-to-real transfer for whole-body manipulation. These results demonstrate the framework's potential for learning diverse visual humanoid loco-manipulation skills.

</details>

---

### [[20_Research/Papers/机器人/TPS-A_Path_Planning_for_Any-Shape_Vehicles_with_Certified_Collision_Checking_in_Trajectory_Parameter_Space|TPS-A*: Path Planning for Any-Shape Vehicles with Certified Collision Checking in Trajectory Parameter Space]]

![[assets/2611.09210_figure.jpg|800]]

- **arXiv**: [2611.09210](https://arxiv.org/abs/2611.09210)
- **PDF**: https://arxiv.org/pdf/2611.09210
- **详细分析**: [[20_Research/Papers/机器人/TPS-A_Path_Planning_for_Any-Shape_Vehicles_with_Certified_Collision_Checking_in_Trajectory_Parameter_Space|TPS-A*: Path Planning for Any-Shape Vehicles with Certified Collision Checking in Trajectory Parameter Space]]
- **作者**: Jose Luis Blanco-Claraco, Shravan S. Rai, Fernando Cañadas-Aránega, José Luis Torres-Moreno, José Carlos Moreno-Úbeda
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《TPS-A*: Path Planning for Any-Shape Vehicles with Certified Collision Checking in Trajectory Parameter Space》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Global planners for ground vehicles usually approximate the vehicle by a disk, trading safety against conservativeness, while exact-footprint checking pays for every candidate motion, pose, and footprint edge. We present TPS-A*, a lattice planner whose edges are kinematically feasible trajectories from parameterized trajectory generators, built on certified collision checking in trajectory parameter space. A grid precomputed per footprint returns, in one pass over the local obstacles, a certified free distance along every candidate trajectory, so the per-node collision cost is independent of footprint complexity and trajectory count. We prove that this grid never overestimates the free distance of the continuously swept, possibly non-convex footprint, and state the planner's guarantees: collision-free paths and bounded suboptimality relative to its lattice abstraction. Goals with or without heading are reached exactly by Reeds-Shepp shots certified as trajectories of the same generators. An exact independent test finds no collision in its paths. On 300 cluttered worlds, with the true footprint and the same goal pose for all planners, it solves every query with a collision-free goal pose in a median of three milliseconds on an AMD Ryzen 7 2700X, on par with hybrid A*, 45\% of whose paths overlap obstacles, and nearly sixty times faster than a state-lattice planner, the only other collision-free one; with position goals, eighty-nine times faster than hybrid A*. It matches hybrid A* in automated parking and on narrow doorways, docks a non-convex fork footprint that no convex model admits, and drove a real robot across a university campus among people.

</details>

---

### [[20_Research/Papers/机器人/Auditing_Grasp_Feasibility_Predictors_with_Planner-Verified_Counterfactuals|Auditing Grasp Feasibility Predictors with Planner-Verified Counterfactuals]]

![[assets/2611.09130_figure.png|800]]

- **arXiv**: [2611.09130](https://arxiv.org/abs/2611.09130)
- **PDF**: https://arxiv.org/pdf/2611.09130
- **详细分析**: [[20_Research/Papers/机器人/Auditing_Grasp_Feasibility_Predictors_with_Planner-Verified_Counterfactuals|Auditing Grasp Feasibility Predictors with Planner-Verified Counterfactuals]]
- **作者**: Sajid Ansari, Antony Thomas, Girish Varma
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Auditing Grasp Feasibility Predictors with Planner-Verified Counterfactuals》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AGFP-Net, ClearanceNet, GraspFC-NNet, GraspNet, PIGINet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Grasp-feasibility predictors report near-perfect accuracy on Task and Motion Planning benchmarks, but high accuracy on these benchmarks does not verify that a predictor uses the collision geometry that the motion planner checks. We propose a planner-verified counterfactual (CF) test: holding the grasp pose fixed, we insert a solid obstacle into the approach corridor, add its points to the model input, and let a planner re-derive the label, which flips from feasible to infeasible. Across eight predictors spanning point clouds, voxels, depth, and object tokens, CF-pair AUROC falls from high natural AUROC (0.920-0.996) to chance (0.470-0.504), and the flip holds across four planners, two arms, and a real-object obstacle. Predictors fail at different resolutions, from a bounding box to a 12.5 cm voxel. In the point-cloud models we dissect, the obstacle either moves the representation in a direction unrelated to whether it blocks the grasp or is not registered at all. A clearance-aware read of the corridor points, trained on the unmodified benchmark with no counterfactual scenes, reaches 0.983 CF-pair AUROC, but it remains bound to its trained obstacle placements; a placement-invariant clearance representation is still open. We release the counterfactual labels, metrics, datasheet, and relabeling pipeline at https://github.com/codewithsajid/graspfc-cf.

</details>

---

### [[20_Research/Papers/具身智能/Toward_the_Era_of_Agentic_Embodied_Intelligence|Toward the Era of Agentic Embodied Intelligence]]

![[assets/2611.09124_figure.png|800]]

- **arXiv**: [2611.09124](https://arxiv.org/abs/2611.09124)
- **PDF**: https://arxiv.org/pdf/2611.09124
- **详细分析**: [[20_Research/Papers/具身智能/Toward_the_Era_of_Agentic_Embodied_Intelligence|Toward the Era of Agentic Embodied Intelligence]]
- **作者**: Chao Liang, Ke Chen, Fengxiaoxiao Li, Shibo Huang, Yufeng Sun, Zhaokai Yin, Jianhuan Lai, Haozhe Feng, Chenghuan Jia, Zhipeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.1，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Toward the Era of Agentic Embodied Intelligence》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models increasingly guide robot actions, yet sustained autonomy requires efficient control and failure recovery. We introduce A2-MEAS, an embodied multi-agent framework built around code as a scaling interface. Learned correction codes combine corrective language, spatial evidence, execution history, and action proposals. MetaBrain provides training supervision and runtime guidance. A correction encoder and adapter absorb this knowledge into policy weights during training, while fresh codes adapt behavior with frozen weights at deployment. The action model, A2-WLA, adds motion-aware history and a latent world model to a vision-language-action policy. Surprisingly, this simple design with action pretraining and task specialization reaches 0.5755 Q-score on the 50-task BEHAVIOR 2026 public subset before online correction, 2.21x the 2025 winner's reported 0.2605 across different benchmark editions and training configurations. On all 100 BEHAVIOR 2026 public tasks, A2-MEAS achieves 0.6411 Q-score and 45.40% task success. On RoboTwin 2.0, A2-WLA achieves 93.98% average success, rising to 95.05% with the complete system. Across 12 real-robot tasks in five household settings, A2-WLA achieves 57.92% average success versus 26.67% for pi0.5. In long-horizon pour-over coffee preparation, a history-conditioned adapter raises post-failure completion at two filter-handling steps from 14% to 94% and from 8% to 82%, compared with A2-WLA retries. Our training infrastructure delivers 427.1 samples per second, 4.03x the throughput of a pi0.5 reference implementation on matched hardware. We will release the system, models, training scripts, and infrastructure to support efficient embodied learning.

</details>

---

### [[20_Research/Papers/机器人/Safe_Circumnavigation_on_Heterogeneous_Orbits_A_Range-Only_HOCBF-QP_Framework_for_Nonholonomic_Multi-Agent_Systems|Safe Circumnavigation on Heterogeneous Orbits: A Range-Only HOCBF-QP Framework for Nonholonomic Multi-Agent Systems]]

![[assets/2611.09112_first_page.png|800]]

- **arXiv**: [2611.09112](https://arxiv.org/abs/2611.09112)
- **PDF**: https://arxiv.org/pdf/2611.09112
- **详细分析**: [[20_Research/Papers/机器人/Safe_Circumnavigation_on_Heterogeneous_Orbits_A_Range-Only_HOCBF-QP_Framework_for_Nonholonomic_Multi-Agent_Systems|Safe Circumnavigation on Heterogeneous Orbits: A Range-Only HOCBF-QP Framework for Nonholonomic Multi-Agent Systems]]
- **作者**: Shubham Singh, Anand Singh, Anjali Tiwari, Lara Briñón-Arranz, Katsuki Fujisawa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Safe Circumnavigation on Heterogeneous Orbits: A Range-Only HOCBF-QP Framework for Nonholonomic Multi-Agent Systems》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Circumnavigating a stationary target with a team of robots requires each robot to hold its own standoff distance, to stay evenly spaced from its neighbours, and to avoid collisions with the target and with each other at every instant. The task becomes arduous when the robots are assigned different orbital radii, as their sensors or roles may demand. This paper presents a safety-critical control framework for this problem. Each robot commands both its acceleration and its turn-rate, measures only its distance to the target, and exchanges information only with its two ring neighbours. The design has three features. First, a structural property of the model lets one control law serve every robot regardless of its assigned radius. Second, the acceleration drives each radius exactly to its target, while the turn-rate balances the formation with the neighbours. Third, a higher-order control-barrier-function quadratic program enforces target, geofence, and inter-robot safety on both inputs at once; it leaves the nominal controller untouched away from the constraints and stays valid while the unmeasured range rate is still being estimated. Simulations confirm these guarantees. In a comparison, the closest existing multi-orbit design, even with full state information, violates both the target standoff and the inter-robot margin, whereas the proposed controller does not.

</details>

---

### [[20_Research/Papers/机器人/Robust_Readout_of_Cross-Point_Resistive_Arrays_via_Time-Domain_Optimization|Robust Readout of Cross-Point Resistive Arrays via Time-Domain Optimization]]

![[assets/2611.09059_figure.png|800]]

- **arXiv**: [2611.09059](https://arxiv.org/abs/2611.09059)
- **PDF**: https://arxiv.org/pdf/2611.09059
- **详细分析**: [[20_Research/Papers/机器人/Robust_Readout_of_Cross-Point_Resistive_Arrays_via_Time-Domain_Optimization|Robust Readout of Cross-Point Resistive Arrays via Time-Domain Optimization]]
- **作者**: Taro Tako, Hiroshi Kaminaga, Taisuke Kobayashi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Robust Readout of Cross-Point Resistive Arrays via Time-Domain Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL, JRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-point resistive arrays are attractive for high-density tactile sensing because they reduce wiring complexity. However, conventional frequency-based readout methods can become inaccurate in robotic sensing environments, where long interconnects and measurement and environmental noise degrade the observed signals. We propose a time-domain optimization method for robust readout of cross-point resistive arrays. The method determines resistance values by fitting a time-domain observation model to the measured waveform over the interval, rather than relying solely on spectral amplitudes. By exploiting the full waveform, the proposed method improves robustness under noisy observation conditions. In simulations of a 16 x 16 array, the proposed method reduced the mean readout error by 20% compared with the baseline method. Furthermore, validation over 1,000 trials showed that the proposed method achieves more robust estimation than the conventional method, reducing the mean error and standard deviation by 24.6% and 77.6%, respectively. The improvement was also confirmed in cross-point array simulations with resistance distributions emulating tactile sensor responses.

</details>

---

### [[20_Research/Papers/机器人/When_to_Trust_the_BIM_Identifiability-Aware_LiDAR-Inertial--BIM_Fusion_under_As-Built_Deviations|When to Trust the BIM: Identifiability-Aware LiDAR-Inertial--BIM Fusion under As-Built Deviations]]

![[assets/2611.09045_figure.png|800]]

- **arXiv**: [2611.09045](https://arxiv.org/abs/2611.09045)
- **PDF**: https://arxiv.org/pdf/2611.09045
- **详细分析**: [[20_Research/Papers/机器人/When_to_Trust_the_BIM_Identifiability-Aware_LiDAR-Inertial--BIM_Fusion_under_As-Built_Deviations|When to Trust the BIM: Identifiability-Aware LiDAR-Inertial--BIM Fusion under As-Built Deviations]]
- **作者**: Yujie Zhang, Yuxuan Guo, Xinbao Sun, Chunlei Zhao, Langqi Miao, Xiaohui Jia, Jinyue Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《When to Trust the BIM: Identifiability-Aware LiDAR-Inertial--BIM Fusion under As-Built Deviations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building information models (BIM) can provide a global geometric reference for robot localization with LiDAR-inertial odometry (LIO). However, as-built deviations from the as-designed model mean that a disagreement between a scan and the BIM may arise from a pose error, an offset wall surface (an as-built deviation or an unmodeled object in front of the wall), or a shifted room, and in some geometries these explanations produce identical observations. In this paper, we formalize this attribution problem as fault identification over three fault classes and derive a geometric criterion for when attribution is possible. Building on it, we propose an identifiability-aware method that reports an attribution only when the fault is attributable; otherwise, it retains the candidates, defers BIM updates and BIM-based pose corrections in the ambiguous directions, and recovers once new references arrive. In the pre-registered two-dimensional study, on cases whose fault is detectable but not attributable, the method's conditional error rate was 0.83%, against 31.67% for a baseline with uncertainty-based abstention at the same answer rate. On the 5,600 attributable cases, the method reported a unique attribution 5,574 times, with no incorrect attributions. In paired fault injections in a laboratory room with its IFC model and on three floors of the SLABIM dataset, it raised no off-target attribution (0 of 168 conditions in the laboratory; 0 of 1,302 on SLABIM) and attributed all eight laboratory faults predicted to be attributable, whereas both reproduced baselines raised off-target structural flags in every setting.

</details>

---

### [[20_Research/Papers/具身智能/FASTFUNNELS_Agile_Multi_Robot_Navigation_in_Narrow_Spaces_via_Adaptive_Dynamic_Funnels|FASTFUNNELS: Agile Multi Robot Navigation in Narrow Spaces via Adaptive Dynamic Funnels]]

![[assets/2611.09005_figure.png|800]]

- **arXiv**: [2611.09005](https://arxiv.org/abs/2611.09005)
- **PDF**: https://arxiv.org/pdf/2611.09005
- **详细分析**: [[20_Research/Papers/具身智能/FASTFUNNELS_Agile_Multi_Robot_Navigation_in_Narrow_Spaces_via_Adaptive_Dynamic_Funnels|FASTFUNNELS: Agile Multi Robot Navigation in Narrow Spaces via Adaptive Dynamic Funnels]]
- **作者**: Vignesh Rajagopal, Rohan Chandra
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《FASTFUNNELS: Agile Multi Robot Navigation in Narrow Spaces via Adaptive Dynamic Funnels》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We focus on the problem of high-speed multi-robot navigation in cluttered spaces with tight spatial constraints. A key challenge is balancing safety with agility, as existing methods often trade one for the other (slowing down near a bottleneck to avoid collisions versus failing to swerve in time at high speeds), especially for car-like systems. Our approach belongs to the family of formation control methods, in which Ackermann-steering agents coordinate while navigating tight spaces. However, current formation control techniques rely on rigid, pre-defined shapes and transitions that depend on initial conditions, the environment, and vehicle dynamics, and are impractical to maintain at high speeds. For example, agents passing through a small gap must first form a square, transform into a line using analytical equations, and then return to a square. In contrast, our approach is inspired by a droplet of water that continuously adapts its shape to the space it flows through without slowing down. We propose a hierarchical algorithm in which, at the high level, a reinforcement learning policy produces a dynamic, blob-like elliptical patch that morphs its shape in real time, squeezing, stretching, and orienting itself around obstacles and through tight spaces. At the low level, the robots are controlled via distributed model predictive control (DMPC) to stay inside the patch, which acts as a soft forcing function, while avoiding collisions with each other. We evaluate our approach, FastFunnels, on simulated F1TENTH racing cars across 14 scenarios with N=1 to N=6 robots, averaged over 20 trials each. FastFunnels achieves an 89% completion rate at 7.73 m/s, while all baselines either fail to complete the track or succeed only at very low speeds (0.07-1.79 m/s, about 40% completion rate).

</details>

---

### [[20_Research/Papers/具身智能/RevoSim_Scalable_Multimodal_Tactile_Simulation_for_Dexterous_Manipulation|RevoSim: Scalable Multimodal Tactile Simulation for Dexterous Manipulation]]

![[assets/2611.08939_figure.png|800]]

- **arXiv**: [2611.08939](https://arxiv.org/abs/2611.08939)
- **PDF**: https://arxiv.org/pdf/2611.08939
- **详细分析**: [[20_Research/Papers/具身智能/RevoSim_Scalable_Multimodal_Tactile_Simulation_for_Dexterous_Manipulation|RevoSim: Scalable Multimodal Tactile Simulation for Dexterous Manipulation]]
- **作者**: Ke Zhang, Lixin Xu, Ziyi Wang, Xiyue Dong, Jie Tan, Lianghu Shao, Xianpeng Wang, Chuanyu Li, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，大模型 0.4，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《RevoSim: Scalable Multimodal Tactile Simulation for Dexterous Manipulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RevoSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present RevoSim, a scalable and high-fidelity multimodal tactile simulator for the BrainCo Revo3 hand that jointly models 285 piezoresistive taxels and five visuotactile fingertips. RevoSim efficiently generates synchronized pressure, depth, RGB, and marker-displacement observations; on a single RTX 5090, its depth-conditioned marker-displacement configuration supports up to 4,096 parallel environments. We train in-hand manipulation and grasping policies entirely in simulation, establishing a foundation for future sim-to-real transfer. Project page: https://braincotech.github.io/RevoSim-web/.

</details>

---

### [[20_Research/Papers/机器人/Wellness_Robots_and_the_Path_to_Full_Autonomy|Wellness Robots and the Path to Full Autonomy]]

![[assets/2611.08930_first_page.png|800]]

- **arXiv**: [2611.08930](https://arxiv.org/abs/2611.08930)
- **PDF**: https://arxiv.org/pdf/2611.08930
- **详细分析**: [[20_Research/Papers/机器人/Wellness_Robots_and_the_Path_to_Full_Autonomy|Wellness Robots and the Path to Full Autonomy]]
- **作者**: Mohammad H. Mahoor, Matthew Hessler, Lombe Chileshe, Ola Alsaadi, Eshrat Emamian, Kerstin S. Haring, Richard M. Voyles
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Wellness Robots and the Path to Full Autonomy》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces the autonomous wellness robot as a distinct category of socially assistive system, defined by its capacity to continuously assess and respond across the seven ICAA dimensions of wellness (see Figure 2). We propose the Care Robot Autonomy Scale (CRAS): a six-level taxonomy (L0-L5) modeled on the automotive automation standard SAE J3016 and evaluated across four wellness-aligned dimensions. We present Ryan, developed initially at the University of Denver and commercialized by DreamFace Technologies, as a case study. NIH/NIA-funded longitudinal evidence (N = 18; 887 hours) shows statistically significant cognitive improvement (SLUMS +2.61, p = 0.015) and a clinically meaningful directional reduction in depressive symptoms (PHQ-9 -2.50, p = 0.073), with no novelty effect. We position Ryan today at CRAS Level 1-2, with emerging Level 3 capabilities in some dimensions, and outline a three-phase roadmap to L5 (full autonomy) by the early 2030s.

</details>

---

### [[20_Research/Papers/机器人/HOC2R_Hand-Object_Contact_Trajectories_for_Human-to-Robot_Motion_Transfer|HOC2R: Hand-Object Contact Trajectories for Human-to-Robot Motion Transfer]]

![[assets/2611.08920_figure.png|800]]

- **arXiv**: [2611.08920](https://arxiv.org/abs/2611.08920)
- **PDF**: https://arxiv.org/pdf/2611.08920
- **详细分析**: [[20_Research/Papers/机器人/HOC2R_Hand-Object_Contact_Trajectories_for_Human-to-Robot_Motion_Transfer|HOC2R: Hand-Object Contact Trajectories for Human-to-Robot Motion Transfer]]
- **作者**: Hongkun Yu, Francisco M. López, Francisco Cruz
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《HOC2R: Hand-Object Contact Trajectories for Human-to-Robot Motion Transfer》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AffordanceNet, ImitationNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human videos contain abundant object-manipulation demonstrations, but they do not directly provide motion cues that a robot can follow. We present HOC2R, a Hand-Object Contact trajectory extractor for Robot motion that combines frozen DINOv3 and SAM 2.1 features with learned heads for hand-object association and contact localization. HOC2R supports two modes: count-aware automation that detects, counts, and localizes visible contacts in untrimmed videos, and fixed-two localization for two-finger grippers when contact frames are known. On a 30-task point-annotated benchmark, count-aware automation improves contact-count accuracy from 58.1% to 71.4% and reduces mean localization distance from 19.81 to 10.46 pixels relative to an adapted VRB2 baseline. On seven unseen RGB-D rollouts, a five-task fixed-two checkpoint reduces mean localization distance from 67.67 to 27.02 pixels. Across six robot evaluation sequences, the 30-task fixed-two checkpoint produces four feasible trajectories and succeeds on three tasks, compared with two feasible trajectories and one successful task for each adapted baseline. HOC2R is competitive in the evaluated single-hand scenes, robust to the hand-color shift, and strongest in the evaluated multi-hand scenes. These results support HOC2R as a practical pseudo-labeling method for extracting robot-usable contact trajectories from human demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/PRISM_Primitive_Routing_via_In-context_Skill_Mixing_for_Retentive_VLA_Adaptation|PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation]]

![[assets/2611.08917_figure.png|800]]

- **arXiv**: [2611.08917](https://arxiv.org/abs/2611.08917)
- **PDF**: https://arxiv.org/pdf/2611.08917
- **详细分析**: [[20_Research/Papers/具身智能/PRISM_Primitive_Routing_via_In-context_Skill_Mixing_for_Retentive_VLA_Adaptation|PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation]]
- **作者**: Jiachen Tao, Gengyu Zhang, Haoxuan Wang, Bing Liu, Yan Yan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PRISM: Primitive Routing via In-context Skill Mixing for Retentive VLA Adaptation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AtomicVLA, SkillVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models promise a single language-conditioned policy adaptable to many manipulation behaviors, yet deployment additionally requires skill retention and long-horizon composition: a policy must retain previously acquired skills and reuse them inside composite tasks whose behavior changes across phases. The standard recipe absorbs every new task into one shared update, which provides neither a parameter-level locus for reusable skills nor a mechanism for invoking each skill along the trajectory. We observe that this missing structure is latent rather than absent: per-skill low-rank updates of a pretrained VLA occupy a robustly distinguishable, low-dimensional subspace, and a single composite-task LoRA concentrates roughly half of its Frobenius energy in this subspace, against a near-zero matched random-rotation control. Building on this geometry, we introduce PRISM, which represents reusable skills as parameter-level primitives: each skill family is stored as a dedicated low-rank action-expert adapter in a primitive bank, primitives are augmented with skill-specific low-rank residuals and composed at inference by a per-chunk VLM-conditioned router that reads the prefix representation to track task progress, and the router is supervised by per-chunk labels from a deterministic, task-conditioned, action-derived oracle. During composite training, the vision encoder, the language LoRA, the skill residuals, the router, and the shared action projections and time MLP are updated; every primitive is held frozen, so the base per-skill action-expert adapters are preserved by construction. On RoboCasa365, PRISM achieves 56.43% atomic-skill success and reaches 20.00% on long-horizon composite tasks, while a standard $π_{0.5}$-LoRA two-stage fine-tune reaches 17.86% atomic and 17.50% composite success. We additionally validate PRISM on an AgileX PIPER real-robot setup.

</details>

---

### [[20_Research/Papers/具身智能/Polarization_calibration_of_fisheye_cameras_using_skylight_in_the_wild|Polarization calibration of fisheye cameras using skylight in the wild]]

![[assets/2611.08911_figure.png|800]]

- **arXiv**: [2611.08911](https://arxiv.org/abs/2611.08911)
- **PDF**: https://arxiv.org/pdf/2611.08911
- **详细分析**: [[20_Research/Papers/具身智能/Polarization_calibration_of_fisheye_cameras_using_skylight_in_the_wild|Polarization calibration of fisheye cameras using skylight in the wild]]
- **作者**: Shuo Wang, Shiqi Che, Dianze Dong, Wenxin Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Polarization calibration of fisheye cameras using skylight in the wild》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skylight polarization provides directional cues for robotic navigation, but fisheye lens effects and analyzer imperfections can degrade polarization measurements across the field of view. We present a joint lens-analyzer calibration method that explicitly models incidence-dependent lens transmission together with analyzer gains and angular offsets in a unified eight-parameter formulation. Given known geometric calibration, rotations between camera frames can be estimated using visual features and cross-frame directional polarized light consistency can be used for polarization calibration. Therefore, our calibration approach requires only a short handheld outdoor sequence under natural skylight, without dedicated polarization calibration equipment or a predefined sky polarization model. On real-world outdoor sequences, the proposed method achieves a weighted cross-frame angle-of-linear-polarization (AoLP) mean absolute error below 0.5° across all incidence angles, with a 73.4% reduction in the 80°-90° incidence angle region, and generalizes to an independent sequence with an overall mean absolute error of 0.466° without refitting. Preliminary solar-azimuth experiments using a camera mounted on a quadruped robot further show improved alignment with the visible solar center, supporting the potential of calibrated AoLP measurements for relative-heading estimation and future polarization--inertial navigation. The calibration software tool will be released upon acceptance of this paper.

</details>

---

### [[20_Research/Papers/具身智能/Localizing_and_Editing_the_Goal_Representation_of_a_Vision-Language-Action_Model|Localizing and Editing the Goal Representation of a Vision-Language-Action Model]]

![[assets/2611.08895_first_page.png|800]]

- **arXiv**: [2611.08895](https://arxiv.org/abs/2611.08895)
- **PDF**: https://arxiv.org/pdf/2611.08895
- **详细分析**: [[20_Research/Papers/具身智能/Localizing_and_Editing_the_Goal_Representation_of_a_Vision-Language-Action_Model|Localizing and Editing the Goal Representation of a Vision-Language-Action Model]]
- **作者**: Sudhanshu Srivastava, Faisal Aqlan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Localizing and Editing the Goal Representation of a Vision-Language-Action Model》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Operators can state safety constraints for robots as prohibitions such as "do not put the bowl on the stove". We study whether OpenVLA follows such prohibitions and where it represents the goal it executes. The 10 tasks of LIBEROGoal share one scene, so we can label the goal that each rollout executes. We combine closed-loop rollouts with activation patching, linear probes, activation steering and runtime monitors. On LIBERO-Goal, negation had no detectable effect on which task OpenVLA executed. The model executed the forbidden task in 79% of negated rollouts and completed 78% of plain tasks. A goal probe gives similar read-outs under "not X" and "X". Activation patching shows that the first action depends mostly on the instruction tokens before layer 12 and on the last prompt token from layer 16 onward. A fixed steering vector at the instruction tokens at layer 8 redirected 12 of 18 rollouts. Fixed vectors and prefill patches at layers 12 to 20 redirected none of 158. From layer 16, only patches at every decoded action token redirected the robot (15 of 18 rollouts at layer 24). When the instruction changes during a rollout, the layer-32 goal read-out detects non-compliance better than failure detectors, and an external probe on image and instruction features performs comparably. These results support enforcing prohibitions outside the instruction and monitoring goal read-outs against the specification. Goal edits in OpenVLA should act before layer 12 or patch every action token.

</details>

---

### [[20_Research/Papers/强化学习/Lodos_A_Lightweight_Simulator_Designed_for_Contact-Rich_Interactions_with_Detailed_Meshes|Lodos: A Lightweight Simulator Designed for Contact-Rich Interactions with Detailed Meshes]]

![[assets/2611.08872_figure.jpg|800]]

- **arXiv**: [2611.08872](https://arxiv.org/abs/2611.08872)
- **PDF**: https://arxiv.org/pdf/2611.08872
- **详细分析**: [[20_Research/Papers/强化学习/Lodos_A_Lightweight_Simulator_Designed_for_Contact-Rich_Interactions_with_Detailed_Meshes|Lodos: A Lightweight Simulator Designed for Contact-Rich Interactions with Detailed Meshes]]
- **作者**: Onur Beker, Andreas René Geist, Georg Martius
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Lodos: A Lightweight Simulator Designed for Contact-Rich Interactions with Detailed Meshes》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IsaacGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, massively parallelized rigid-body simulation has played a central role in robotics research, enabling rapid progress in areas such as reinforcement learning, stochastic optimal control, and randomized smoothing-based trajectory optimization. Particularly in contact-rich settings, the scalability of such simulations in large part depends on well-optimized representations of collision geometry, often requiring a coarse approximation of the underlying surfaces using primitives such as spheres, capsules, cylinders, and boxes. Whenever the complexity of the surfaces or the precision demands of the application render such approximations insufficient, it is instead necessary to employ mesh-mesh collisions, which impose a significant reduction in throughput. This paper proposes a simulation framework designed from scratch to address this bottleneck, with novel routines for broadphase and narrowphase collision detection as well as the subsequent contact dynamics computation. As experimentally validated, the framework matches existing well-established simulators in terms of physical faithfulness, and can achieve approximately an order of magnitude higher throughput in the detailed mesh-mesh collision setting that it specializes in. The source code is available at https://github.com/martius-lab/lodos.

</details>

---

### [[20_Research/Papers/具身智能/ActPrune_Action-Grounded_Visual_Token_Pruning_for_Efficient_Vision-Language-Action_Models|ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models]]

![[assets/2611.08827_figure.png|800]]

- **arXiv**: [2611.08827](https://arxiv.org/abs/2611.08827)
- **PDF**: https://arxiv.org/pdf/2611.08827
- **详细分析**: [[20_Research/Papers/具身智能/ActPrune_Action-Grounded_Visual_Token_Pruning_for_Efficient_Vision-Language-Action_Models|ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models]]
- **作者**: Sungwon Moon, Minji Kim, Hyemin Boo, Daeun Song, Jiyoung Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《ActPrune: Action-Grounded Visual Token Pruning for Efficient Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SpecPrune-VLA, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models perform versatile manipulation tasks from language instructions, but their inference cost limits how fast a robot can respond in closed-loop control. Visual token pruning reduces this cost; however, prior methods estimate token redundancy from encoded visual embeddings or attention, only after the visual encoder has processed the entire observation. We propose \ours, a training-free token pruning method that moves the pruning decision ahead of the vision encoder by grounding it in a geometric prior derived from the robot's own action. The action chunk predicted at the previous control step is already available before the current observation is encoded, and it specifies the end-effector and camera motion between consecutive observations. The same action affects the two standard camera views asymmetrically: in the fixed third-person view, \ours retains patches along the projected end-effector trajectory together with semantic anchors, while in the wrist view, it prunes patches that remain unchanged after compensating for the action-induced camera motion. Extensive experiments on two simulation environments (LIBERO and VLABench) and four real-robot tasks demonstrate that \ours achieves up to 1.61 $\times$ speedup and 59.5\% FLOPs reduction with negligible degradation in success rates.

</details>

---

### [[20_Research/Papers/强化学习/It_Takes_Two_to_Tangram_Multi-Agent_Object_Centric_Reinforcement_Learning_for_Assembly|It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly]]

![[assets/2611.08814_figure.png|800]]

- **arXiv**: [2611.08814](https://arxiv.org/abs/2611.08814)
- **PDF**: https://arxiv.org/pdf/2611.08814
- **详细分析**: [[20_Research/Papers/强化学习/It_Takes_Two_to_Tangram_Multi-Agent_Object_Centric_Reinforcement_Learning_for_Assembly|It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly]]
- **作者**: Paul Knaußt, Kay Pompetzki, Nico Bohlinger, Niklas Funk, Cristiana de Farias, Rolf Findeisen, Jan Peters
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.4，强化学习 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《It Takes Two to Tangram: Multi-Agent Object Centric Reinforcement Learning for Assembly》归入 强化学习、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：InforMARL, TangramBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geometric assembly requires fine spatiotemporal coordination to place parts without causing collisions or deadlocks under tight clearances. To address this, we present an object-centric reinforcement learning framework that treats each part as an agent and learns a shared policy for continuous assembly control. A graph neural network represents the pieces, their target poses, and their spatial relationships, and predicts translational and angular velocities for each component. Per-agent proximal policy optimization with a centralized graph critic directly learns motion and temporal coordination within a single feedback policy. We study this formulation through planar Tangram assembly, where pieces must slide and rotate into a given configuration while remaining on the assembly surface. Procedural generation of target configurations and randomized initial arrangements support training and evaluation across diverse assembly problems. Our experiments isolate the roles of relational structure and multi-agent optimization, and compare learned control with sampling-based planning. We demonstrate concurrent assembly in simulation and transfer the policy to sequential execution on a real robot, as our object-centric formulation decouples learned assembly coordination from low-level physical control. Project page: https://tangrambench.org/

</details>

---

### [[20_Research/Papers/具身智能/VICTR_Value-Informed_In-Context_Learning_for_Vision-Language-Action_Models|VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models]]

![[assets/2611.08698_figure.png|800]]

- **arXiv**: [2611.08698](https://arxiv.org/abs/2611.08698)
- **PDF**: https://arxiv.org/pdf/2611.08698
- **详细分析**: [[20_Research/Papers/具身智能/VICTR_Value-Informed_In-Context_Learning_for_Vision-Language-Action_Models|VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models]]
- **作者**: Luca Macesanu, Tianluo Zhang, Aditya Patil, Archit Sharma, Kevin Angers, Christopher M. Clark, Chen Feng, Juexiao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VICTR: Value-Informed In-Context Learning for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IC-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in robot foundation models have highlighted the potential of in-context learning (ICL) for adapting robot behavior from demonstrations without further fine-tuning. Previous work has used retrieval-based post-training to equip pretrained vision-language-action (VLA) models with the capability for ICL by teaching them to condition action predictions on retrieved visually-relevant demonstration chunks. However, the effectiveness of retrieval hinges on selecting context relevant to the current execution stage, which visual similarity alone may not capture. We introduce VICTR, a framework enabling in-context learning in VLAs via progress-informed context retrieval built around an In-Context Value Function Estimator (IC-VFE). IC-VFE conditions on a reference demonstration video, a language instruction and the current observation to estimate task-relative progress. By conditioning progress estimation on a reference demonstration, IC-VFE can align the current state with a demonstrated execution even for tasks unseen during training. VICTR uses the estimated progress to select demonstration chunks at corresponding stages of execution and supplies them to a $π_{0.5}$ policy post-trained for in-context action generation. On unseen out-of-domain real-world manipulation tasks, VICTR raises the success rate from 6.2% for a fine-tuned $π_{0.5}$ baseline to 23.8% and more than doubles the task progress rate, from 28.9% to 55.5%. Project page with code, data and videos: https://ai4ce.github.io/VICTR/

</details>

---

### [[20_Research/Papers/具身智能/ForPC_Force-Aware_Whole-Body_Control_for_Precise_Humanoid_Cart_Pushing|ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing]]

![[assets/2611.08664_figure.png|800]]

- **arXiv**: [2611.08664](https://arxiv.org/abs/2611.08664)
- **PDF**: https://arxiv.org/pdf/2611.08664
- **详细分析**: [[20_Research/Papers/具身智能/ForPC_Force-Aware_Whole-Body_Control_for_Precise_Humanoid_Cart_Pushing|ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing]]
- **作者**: ZhenYu Zou, Xing Liu, ShiChuang Wang, YunLong Dong, LiNan Deng, Feng Hua, Jun Wan, Cheng Cheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《ForPC: Force-Aware Whole-Body Control for Precise Humanoid Cart Pushing》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots are expected to take over strenuous material handling in manufacturing, logistics, and healthcare, where operating existing wheeled carts would let them move heavy loads without modifying the workplace. However, humanoid cart pushing remains challenging because the bimanual grasp closes a force-coupled loop in which the contact wrenches that drive the cart also disturb the robot's balance, and payload changes alter the coupled dynamics. We propose ForPC, a force-aware whole-body control framework that regulates cart velocity through two-stage reinforcement learning. A locomotion prior is first trained under varied hand loads and upper-body postures to provide balance support. A force latent and a state latent are then inferred from onboard observations, without external force sensors, and fed to a residual policy that coordinates bounded arm, waist, and leg adjustments with base-velocity commands. Multi-objective rewards penalize bimanual internal opposition, grasp slip, and actuator saturation, encouraging the policy to apply contact force on demand without human demonstrations. Sim-to-sim experiments show that ForPC reduces cart-velocity RMSE by up to 68.2% relative to a locomotion-only baseline (Loco-only) and cross-track RMSE by up to 74.2% on the multi-bend route. Trained solely in simulation, the policy also transfers to a physical Unitree G1 without real-world training or fine-tuning and, with no payload-specific adjustment, pushes a cart carrying up to 30 kg at 0.5 m/s. These results suggest that humanoid robots could eventually replace humans for efficient material handling in daily life.

</details>

---
