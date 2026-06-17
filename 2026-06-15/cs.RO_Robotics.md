# cs.RO | Robotics | 2026-06-15

#arxiv #ComputerScience

**论文数**: 24

### [[20_Research/Papers/强化学习/EgoGuide_Egocentric_Guidance_for_Efficient_Robot-Free_Demonstration_Collection_and_Learning|EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning]]

![[assets/2606.14665_figure.png|800]]

- **arXiv**: [2606.14665](https://arxiv.org/abs/2606.14665)
- **PDF**: https://arxiv.org/pdf/2606.14665
- **详细分析**: [[20_Research/Papers/强化学习/EgoGuide_Egocentric_Guidance_for_Efficient_Robot-Free_Demonstration_Collection_and_Learning|EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning]]
- **作者**: Yue Xu, Mingtao Nie, Tianle Li, Hong Li, Yibo Luo, Siyuan Huang, Yong-Lu Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《EgoGuide: Egocentric Guidance for Efficient Robot-Free Demonstration Collection and Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RoboNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot learning from real-world demonstrations is currently constrained by data scaling. Universal Manipulation Interface (UMI) provides an efficient robot-free data collection interface, yet current UMI-style pipelines often collect redundant demonstrations and lack global scene context. To improve data efficiency, we present EgoGuide, a collection interface that records synchronized wrist and head/egocentric observations and couples them with online visual-geometric data quality guidance. We also introduce a Gated Egocentric Residual Policy for robust learning from a viewpoint-varying egocentric camera, allowing head/egocentric context to correct ambiguous local observations while preserving stable wrist-view control. Real-world experiments show that EgoGuide reduces the required number of data episodes and improves data efficiency. The residual policy further improves robustness under visual occlusion. Project Page: https://silicx.github.io/EgoGuide

</details>

---

### [[20_Research/Papers/具身智能/Whole-Body_Impedance_Model_Predictive_Control_for_Safe_Physical_Human--Robot_Interaction_on_Floating-Base_Platforms|Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms]]

![[assets/2606.14617_figure.png|800]]

- **arXiv**: [2606.14617](https://arxiv.org/abs/2606.14617)
- **PDF**: https://arxiv.org/pdf/2606.14617
- **详细分析**: [[20_Research/Papers/具身智能/Whole-Body_Impedance_Model_Predictive_Control_for_Safe_Physical_Human--Robot_Interaction_on_Floating-Base_Platforms|Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms]]
- **作者**: Yongyan Cao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Whole-Body Impedance Model Predictive Control for Safe Physical Human--Robot Interaction on Floating-Base Platforms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Floating-base robots must balance under rigid contact constraints while interacting safely with humans. Existing whole-body control~(WBC) frameworks allocate the full joint space to locomotion or rely on fixed-gain impedance feedback that accumulates steady-state error under sustained physical human--robot interaction~(pHRI) forces. This paper extends the authors' fixed-base two-layer Impedance MPC to floating-base platforms through a three-level architecture: a centroidal MPC plans contact forces over a 500\,ms horizon; a priority-driven WBC layer resolves balance into joint torques through contact-consistent null-space projection; and the residual null space is governed by a receding-horizon quadratic program~(QP) that predicts and rejects pHRI disturbances using a Kalman-augmented state. A contact-consistent feedback linearization reduces the arm end-effector plant to a double integrator with a \emph{constant} state matrix within each contact mode, enabling offline precomputation of the QP cost and ${\geq}1$\,kHz operation. A covariance-inflation protocol preserves the disturbance estimate across contact-mode switches, guaranteeing zero steady-state error under bounded constant pHRI loads, and an Impedance Equivalence Theorem shows the infinite-horizon limit recovers a classical task-space impedance law whose effective mass, damping, and stiffness adapt to posture and contact configuration. Simulations on a 17-DOF biped and the Unitree G1 humanoid validate the design.

</details>

---

### [[20_Research/Papers/大模型/Safe_Reinforcement_Learning_of_Autonomous_Highway_Driving_A_Unified_Framework_for_Safety_and_Efficiency|Safe Reinforcement Learning of Autonomous Highway Driving: A Unified Framework for Safety and Efficiency]]

![[assets/2606.14609_figure.png|800]]

- **arXiv**: [2606.14609](https://arxiv.org/abs/2606.14609)
- **PDF**: https://arxiv.org/pdf/2606.14609
- **详细分析**: [[20_Research/Papers/大模型/Safe_Reinforcement_Learning_of_Autonomous_Highway_Driving_A_Unified_Framework_for_Safety_and_Efficiency|Safe Reinforcement Learning of Autonomous Highway Driving: A Unified Framework for Safety and Efficiency]]
- **作者**: Chufei Yan, Zhihao Cui, Yiyan Lv, Taojie Chen, Ning Bian, Yulei Wang
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Safe Reinforcement Learning of Autonomous Highway Driving: A Unified Framework for Safety and Efficiency》归入 强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MOE-RM-SRL, MoE-RM-SRL, RM-DRL, SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) offers a compelling route to decision-making for advanced autonomous vehicles (AVs), yet its trial-and-error nature makes it difficult to guarantee safety during training and to achieve both safety and efficiency at deployment. We propose a unified safe reinforcement learning (SRL) framework that integrates safe distance (SD), reward machines (RM), and mixture-of-experts (MoE), termed MoE-RM-SRL. For deployment, SD and RM jointly shape a rule-aware reward that encodes highway traffic regulations and stage-wise objectives, enabling safe and reliable behavior without sacrificing efficiency. For training, we introduce a sparsely gated MoE layer comprising up to 11 deep Q-networks (DQNs); an SD-based gating rule activates a minimal set of experts for lane-keeping and lane-changing, mitigating the instability, discontinuities, and impulsive transients commonly induced by switching between heterogeneous controllers (e.g., MPC/rule-based modules and learned policies). We implement the proposed architecture in CARLA and integrate it with a 6-DoF driver-in-the-loop virtual-reality (DiL-VR) platform. Experiments in stochastic two-lane traffic show that MoE-RM-SRL substantially improves safety and efficiency over state-of-the-art baselines, and the framework naturally extends to multi-lane driving as well as on-ramp merging and exiting scenarios.

</details>

---

### [[20_Research/Papers/机器人/Impedance_MPC_with_Disturbance_Estimation_for_Dexterous_Hand_Control|Impedance MPC with Disturbance Estimation for Dexterous Hand Control]]

![[assets/2606.14606_figure.png|800]]

- **arXiv**: [2606.14606](https://arxiv.org/abs/2606.14606)
- **PDF**: https://arxiv.org/pdf/2606.14606
- **详细分析**: [[20_Research/Papers/机器人/Impedance_MPC_with_Disturbance_Estimation_for_Dexterous_Hand_Control|Impedance MPC with Disturbance Estimation for Dexterous Hand Control]]
- **作者**: Yongyan Cao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Impedance MPC with Disturbance Estimation for Dexterous Hand Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous hands must simultaneously track precise finger trajectories and maintain safe, compliant contact -- objectives in tension for any fixed-gain controller. We present an actuator-agnostic Impedance Model Predictive Control (Impedance MPC) framework for dexterous fingers, instantiating the constant-$A_d$ offset-free architecture established for physical human-robot interaction (pHRI); its stability, recursive-feasibility, and input-to-state-stability guarantees are inherited by preserving the architectural assumptions. An algebraic feedforward reduces the tendon transmission -- hydraulic, cable, pneumatic, twisted-string, or series-elastic -- to a constant-coefficient double integrator, so the QP cost inverse is precomputed offline and a 10-step receding-horizon quadratic program runs at 500\,Hz while enforcing hard constraints on contact force (ISO/TS 15066), actuation limits, and jerk. An encoder-only augmented-Kalman disturbance state drives steady-state error to zero under any constant contact load. On a hydraulically actuated finger -- the worked example platform, adding pressure and cavitation constraints -- the 500\,Hz Kalman MPC attains 0.5\,mrad RMS, 0.1\,mrad steady-state, and 6.6\,mrad peak deflection under 1.5\,Nm contact: 183$\times$, 1500$\times$, and 23$\times$ better than classical impedance. The realized first-move stiffness (18$\to$323\,Nm/rad with update rate) is independently verified. The architecture scales to a 16-DOF LEAP Hand MuJoCo simulation, recovering from 2.5\,N grasp-load disturbances within 0.7\,s.

</details>

---

### [[20_Research/Papers/机器人/What_Robots_Do_Matters_More_Than_What_They_Look_Like_Task_Context_Shapes_Trust_in_Educational_HRI|What Robots Do Matters More Than What They Look Like: Task Context Shapes Trust in Educational HRI]]

![[assets/2606.14602_first_page.png|800]]

- **arXiv**: [2606.14602](https://arxiv.org/abs/2606.14602)
- **PDF**: https://arxiv.org/pdf/2606.14602
- **详细分析**: [[20_Research/Papers/机器人/What_Robots_Do_Matters_More_Than_What_They_Look_Like_Task_Context_Shapes_Trust_in_Educational_HRI|What Robots Do Matters More Than What They Look Like: Task Context Shapes Trust in Educational HRI]]
- **作者**: Anna-Maria Velentza, Konstantina Nikou, Anne-Gwenn Bosser, Nikolaos Fachantidis
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《What Robots Do Matters More Than What They Look Like: Task Context Shapes Trust in Educational HRI》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Socially assistive robots (SARs) are increasingly deployed in educational and information-sharing contexts, supported by advances in large language models that enable fluent real-time interaction. Despite the growing diversity of robot embodiments, it remains unclear whether a single robot appearance is appropriate across different interaction tasks or whether trust depends primarily on contextual factors. In this study, we examine how robot appearance and task type jointly influence trust in robots. Using a within-subjects video-based experiment (N = 81), participants evaluated three robots with distinct appearances while performing three educationally relevant tasks: teaching, procedural instruction, and personal-information discussion. Results from repeated-measures analyses show a strong main effect of task on trust, with participants reporting the highest trust during instructional guidance, moderate trust during teaching activities, and significantly lower trust when robots requested personal information. In contrast, robot appearance showed no significant main effect, and the interaction between appearance and task was marginal. These findings suggest that trust in human-robot interaction is shaped more strongly by task context than by physical embodiment alone. By focusing on future educators as end users, this work contributes empirical evidence toward task-aware robot deployment in educational environments and highlights the importance of aligning robot roles and behaviors with interaction goals rather than relying solely on anthropomorphic design.

</details>

---

### [[20_Research/Papers/具身智能/Kine2Go_Kinematic_dataset_for_the_Unitree_Go2_robot_with_diverse_gaits_and_motions|Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions]]

![[assets/2606.14433_figure.png|800]]

- **arXiv**: [2606.14433](https://arxiv.org/abs/2606.14433)
- **PDF**: https://arxiv.org/pdf/2606.14433
- **详细分析**: [[20_Research/Papers/具身智能/Kine2Go_Kinematic_dataset_for_the_Unitree_Go2_robot_with_diverse_gaits_and_motions|Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions]]
- **作者**: Władysław Pałucki, Paweł Siwak, Krzysztof Ciebiera, Marek Cygan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.8（加权：具身智能 0.9，强化学习 0.2，机器人 1.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Kine2Go: Kinematic dataset for the Unitree Go2 robot with diverse gaits and motions》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RSL-RL, RoboNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The recent popularity of robotics, combined with the steadily decreasing cost of robotic hardware, has lowered the entry barrier to robotics research and enabled rapid advancements in the field. One of the primary examples is the Unitree Go2 quadruped robot, which is often used by researchers in the areas of locomotion, navigation, control, and others. Many researchers use the Go2 robot in combination with techniques like imitation learning, reinforcement learning, and behavioral cloning to allow machine learning systems to take full control of the robot. At the same time, many of those techniques require demonstration data consisting of the robot's kinematics information and actions applied to the motors. Obtaining such data is difficult, requires building complex pipelines, and can take significant time. To aid in those kinds of efforts, we present Kine2Go - a dataset with 800 diverse gait kinematics trajectory motion data for the Unitree Go2 robot, derived from 40 distinct policies. Our pipeline accepts data from various quadruped morphologies and translates them to a Go2-compatible format. Then we use Reinforcement Learning to train policies following a given motion, and finally we gather data from those policies, which grants robust, perturbed kinematic data with corresponding motor-level actions.

</details>

---

### [[20_Research/Papers/具身智能/FloVerse_Floor_Plan-Guided_Multi-Modal_Navigation|FloVerse: Floor Plan-Guided Multi-Modal Navigation]]

![[assets/2606.14267_figure.png|800]]

- **arXiv**: [2606.14267](https://arxiv.org/abs/2606.14267)
- **PDF**: https://arxiv.org/pdf/2606.14267
- **详细分析**: [[20_Research/Papers/具身智能/FloVerse_Floor_Plan-Guided_Multi-Modal_Navigation|FloVerse: Floor Plan-Guided Multi-Modal Navigation]]
- **作者**: Weiqi Huang, Shuangyi Dong, Jiaxin Li, Yifei Guo, Zan Wang, Wei Liang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《FloVerse: Floor Plan-Guided Multi-Modal Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Goat-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Floor plans encapsulate compact spatial priors, enabling agents to navigate unseen scenes more efficiently. While prior work has explored floor plan-guided navigation, it has focused mainly on PointNav and a limited set of environments. To bridge this gap, we introduce FloVerse, a new task for floor plan-guided embodied navigation that unifies PointNav, ObjectNav, and ImageNav. To support FloVerse, we assemble FloVerse-1.6K, a large-scale dataset of 1.6K scenes from HM3D and Gibson 4+, paired with corresponding floor plans, comprising 240K expert trajectories and 12M RGBD frames. We further propose ThreeDiff, a two-stage imitation learning policy comprising a planner, a diffusion-based multimodal goal-reasoning module trained via masked-modality modeling, and a refiner, a depth-based trajectory-refinement module for safe execution. Extensive experiments demonstrate that (1) floor-plan priors improve navigation performance across all goal modalities, and (2) ThreeDiff implicitly captures spatial information from floor plans. These results underscore the effectiveness of spatial priors and validate our proposed unified approach for floor plan-guided embodied navigation.

</details>

---

### [[20_Research/Papers/具身智能/ReactVLA_Fast_and_Lightweight_Reactive_Robot_Manipulation_via_Improved_Mean_Flow_Action_Generation|ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation]]

![[assets/2606.14255_figure.png|800]]

- **arXiv**: [2606.14255](https://arxiv.org/abs/2606.14255)
- **PDF**: https://arxiv.org/pdf/2606.14255
- **详细分析**: [[20_Research/Papers/具身智能/ReactVLA_Fast_and_Lightweight_Reactive_Robot_Manipulation_via_Improved_Mean_Flow_Action_Generation|ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation]]
- **作者**: Yanzhao Guo, Wenkai Chen, Jianwei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.8（加权：具身智能 2.4，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ReactVLA: Fast and Lightweight Reactive Robot Manipulation via Improved Mean Flow Action Generation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ReactVLA, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based Vision-Language-Action (VLA) policies have demonstrated strong capability in modeling expressive and multimodal action distributions. However, their reliance on iterative sampling introduces substantial inference latency, which limits their applicability to reactive closed-loop robot manipulation. To address this limitation, we propose \texttt{ReactVLA}, a lightweight and low-latency VLA framework for real-time robotic manipulation. \texttt{ReactVLA} combines two complementary designs: (1) an improved Mean Flow (iMF) action generator that reduces expensive multi-step diffusion sampling to one-to-few-step action generation, and (2) Attention Residuals (AttnRes), a dynamic depth-wise feature routing mechanism that replaces uniform residual accumulation to better preserve task-relevant multimodal representations. We evaluate \texttt{ReactVLA} on large-scale simulation benchmarks, including LIBERO and RoboIMI, as well as real-world robotic manipulation tasks. Experimental results show that \texttt{ReactVLA} consistently outperforms similarly sized VLA baselines, including SmolVLA and $π_0$. On challenging precision manipulation tasks, \texttt{ReactVLA} achieves up to a 1.65$\times$ improvement in task performance while providing more than a 4$\times$ increase in inference speed compared with leading VLA models. Finally, it reduces real-world policy latency to below 38.6 ms, enabling fast reactive control on physical robot platforms. Please check out our project website at: https://game-loader.github.io/ReactVLA/.

</details>

---

### [[20_Research/Papers/大模型/Optimality-Preserving_Decomposition_for_Scalable_QAOA_in_Natural-Language-Guided_Multi-Drone_Assignment|Optimality-Preserving Decomposition for Scalable QAOA in Natural-Language-Guided Multi-Drone Assignment]]

![[assets/2606.14252_first_page.png|800]]

- **arXiv**: [2606.14252](https://arxiv.org/abs/2606.14252)
- **PDF**: https://arxiv.org/pdf/2606.14252
- **详细分析**: [[20_Research/Papers/大模型/Optimality-Preserving_Decomposition_for_Scalable_QAOA_in_Natural-Language-Guided_Multi-Drone_Assignment|Optimality-Preserving Decomposition for Scalable QAOA in Natural-Language-Guided Multi-Drone Assignment]]
- **作者**: Junyeop Bang, Byongho Lee, Dohyun An, Hwangnam Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM

#### 研究背景与动机

《Optimality-Preserving Decomposition for Scalable QAOA in Natural-Language-Guided Multi-Drone Assignment》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As multi-drone fleets scale, zone assignment rapidly evolves into an intractable NP-hard combinatorial problem that overwhelms classical exhaustive search. While quantum optimization promises to shatter these classical bottlenecks, mapping complex spatial tasks from human intent to restricted quantum hardware remains a severe challenge. To bridge this gap, we present an end-to-end framework integrating a fine-tuned Large Language Model (LLM) front-end with a highly scalable, domain-specific quantum-classical backend. The front-end utilizes Supervised Fine-Tuning (SFT) and Direct Preference Optimization (DPO) to translate free-form natural language instructions into structurally robust Quadratic Unconstrained Binary Optimization (QUBO) constraints without false negatives. To overcome the strict qubit limits of near-term quantum devices, our framework features a novel constraint-preserving graph partitioner and a compressed separator-based dynamic programming (DP) merge. By structurally encoding constraints via W-state initialization and XY-mixers in Conditional Value-at-Risk Quantum Approximate Optimization (CVaR-QAOA), the pipeline stays highly compact. Empirical results demonstrate that this architecture circumvents classical scaling walls, recovering the global optimum on 100% of idealized oracle cases and 96.3% under real QAOA sampling, enabling natural-language-guided task allocation at previously intractable scales.

</details>

---

### [[20_Research/Papers/具身智能/SyLink_Hand_A_Synergy-Inspired_Linkage-Driven_Anthropomorphic_Hand_for_Human-Like_Dexterity|SyLink Hand: A Synergy-Inspired Linkage-Driven Anthropomorphic Hand for Human-Like Dexterity]]

![[assets/2606.14250_figure.png|800]]

- **arXiv**: [2606.14250](https://arxiv.org/abs/2606.14250)
- **PDF**: https://arxiv.org/pdf/2606.14250
- **详细分析**: [[20_Research/Papers/具身智能/SyLink_Hand_A_Synergy-Inspired_Linkage-Driven_Anthropomorphic_Hand_for_Human-Like_Dexterity|SyLink Hand: A Synergy-Inspired Linkage-Driven Anthropomorphic Hand for Human-Like Dexterity]]
- **作者**: Hao Wu, Yanzhe Wang, Yu Feng, Yitong Li, Jingxiang Guo, Jian Liu, Jianshu Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《SyLink Hand: A Synergy-Inspired Linkage-Driven Anthropomorphic Hand for Human-Like Dexterity》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing anthropomorphic robotic hands that balance functional dexterity with mechanical simplicity remains a significant challenge. Inspired by human hand synergies, this paper presents the SyLink Hand, an anthropomorphic dexterous hand that integrates biomechanical synergy principles with linkage-driven transmission mechanisms to achieve a high degree of anthropomorphism in appearance, kinematics, and functionality within a compact and cost-effective architecture. Biomechanical analysis of natural hand motions using motion capture gloves reveals strong kinematic correlations among hand joints, providing the basis for a simplified yet functional degree-of-freedom (DOF) configuration. Guided by these synergistic characteristics, optimized linkage mechanisms are employed to coordinate multiple joint motions and reproduce natural finger trajectories. A novel spherical four-bar linkage is further proposed to achieve decoupled flexion/extension (Flex/Ext) and abduction/adduction (Abd/Add) at the metacarpophalangeal joint within a compact form factor. The resulting prototype integrates 19 joints driven by 11 actuators, with a total mass of 520g and a manufacturing cost of approximately USD 400. Experimental evaluations demonstrate its human-like kinematic performance, high load-bearing capability, and versatile grasping and manipulation skills. These results validate that the synergy-inspired, linkage-based design effectively balances anthropomorphism, mechanical simplicity, and functional versatility, highlighting its potential for practical deployment in dexterity-demanding robotic applications.

</details>

---

### [[20_Research/Papers/机器人/Short-Horizon_Position_Accuracy_of_Single-Track_Models_Implications_for_Motion_Planning_of_Autonomous_Vehicles|Short-Horizon Position Accuracy of Single-Track Models: Implications for Motion Planning of Autonomous Vehicles]]

![[assets/2606.14216_figure.png|800]]

- **arXiv**: [2606.14216](https://arxiv.org/abs/2606.14216)
- **PDF**: https://arxiv.org/pdf/2606.14216
- **详细分析**: [[20_Research/Papers/机器人/Short-Horizon_Position_Accuracy_of_Single-Track_Models_Implications_for_Motion_Planning_of_Autonomous_Vehicles|Short-Horizon Position Accuracy of Single-Track Models: Implications for Motion Planning of Autonomous Vehicles]]
- **作者**: Aron J. Aertssen, Lars A. T. H. van Alen, Igo J. M. Besselink, Rudolf G. M. Huisman, René M. J. G. van de Molengraft
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Short-Horizon Position Accuracy of Single-Track Models: Implications for Motion Planning of Autonomous Vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate and computationally efficient vehicle models are essential for motion planning of autonomous vehicles, where positional accuracy directly affects trajectory feasibility and safety. However, the positional accuracy has not been systematically evaluated against real measurements. Therefore, this paper compares the short-horizon positional accuracy of three single-track vehicle models against vehicle measurements across various driving maneuvers. Model parameters are identified through dedicated experiments with the instrumented test vehicle. Rather than identifying a single best model, this work aims to provide insight into the trade-offs between model complexity, parameterization quality, and positional accuracy for informed model selection in Model Predictive Control applications.

</details>

---

### [[20_Research/Papers/机器人/GAIT_Legged_Robot_Proprioceptive_State_Estimation_with_Attention_over_Inertial-Leg_Tokens|GAIT: Legged Robot Proprioceptive State Estimation with Attention over Inertial-Leg Tokens]]

![[assets/2606.14160_figure.png|800]]

- **arXiv**: [2606.14160](https://arxiv.org/abs/2606.14160)
- **PDF**: https://arxiv.org/pdf/2606.14160
- **详细分析**: [[20_Research/Papers/机器人/GAIT_Legged_Robot_Proprioceptive_State_Estimation_with_Attention_over_Inertial-Leg_Tokens|GAIT: Legged Robot Proprioceptive State Estimation with Attention over Inertial-Leg Tokens]]
- **作者**: Young-Rang Seo, Hajun Kim, Sangmin Kim, Dongyun Kang, Hae-Won Park
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《GAIT: Legged Robot Proprioceptive State Estimation with Attention over Inertial-Leg Tokens》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose a method that applies Inertial-Leg (IL) tokenization to an attention-based network for proprioceptive state estimation in legged robots. Unlike existing learning-based state estimators that concatenate all sensor measurements into a single flat vector, the proposed architecture represents inertial measurements and leg-wise measurements as individual tokens and uses an attention mechanism to learn the relative importance of each measurement.This design allows the network to reweight each measurement according to the current contact condition, reflecting the fact that the reliability of forward kinematic measurements depends on whether the corresponding foot is in contact. Unlike conventional contact-aided estimators, however, the proposed method learns this behavior without relying on an explicit contact estimator or on explicit measurement updates based on a stationary contact assumption. To validate the proposed method, we conducted experiments on a Unitree Go1 robot, including debris terrain not modeled in simulation and gait patterns not seen during training. Experimental results show that the proposed method achieves better estimation performance than existing learning-based state estimators under unseen gait patterns and also improves performance over contact-aided model-based methods.

</details>

---

### [[20_Research/Papers/强化学习/A_Modular_Dual-Arm_Apple_Harvesting_Robot_with_Enhanced_Field_Performance|A Modular Dual-Arm Apple Harvesting Robot with Enhanced Field Performance]]

![[assets/2606.14089_figure.png|800]]

- **arXiv**: [2606.14089](https://arxiv.org/abs/2606.14089)
- **PDF**: https://arxiv.org/pdf/2606.14089
- **详细分析**: [[20_Research/Papers/强化学习/A_Modular_Dual-Arm_Apple_Harvesting_Robot_with_Enhanced_Field_Performance|A Modular Dual-Arm Apple Harvesting Robot with Enhanced Field Performance]]
- **作者**: Keyi Zhu, Kyle Lammers, Chaaran Arunachalam, Kaixiang Zhang, Renfu Lu, Zhaojian Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《A Modular Dual-Arm Apple Harvesting Robot with Enhanced Field Performance》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic apple harvesting offers a promising solution to labor shortages in commercial orchards, but low throughput and poor performance in orchard environments hinder its commercial adoption. This paper presents a modular dual-arm apple harvesting robot that uses a vertically stacked arms to enable simultaneous operation in the upper and lower zones of a single tree, simplifying platform positioning from multi-tree lateral repositioning to single-tree stops. Compared to our prior horizontal dual-arm system, the platform integrates 5 advances: (1)a foundation-model-based perception pipeline combining Grounding-DINO and EfficientViT-SAM for robust fruit localization in unstructured outdoor environments; (2)7th-order jerk-bounded trajectory generation paired with a Control Barrier Function safety filter to achieve fast yet safe arm motions; (3)a linear sweep harvesting strategy with a 10cm approach buffer and rotational detachment that improves picking reliability; (4)a temporal-logic-based dual-arm coordination policy with vision-arm async scheduling that maximizes usage of a shared vacuum source; and (5)field validation in 2 commercial orchards covering different apple varieties and tree architectures during the 2025 harvest season. Across the 1738 arm cycles collected in these field trials, the system achieved an 80.0% per-attempt success rate and a mean per-arm cycle time of 7.53s. Fruit damage assessments confirmed that 91.2% of robotically harvested fruit retained the highest USDA grade (Extra Fancy), with bruise rates between 2.4% and 4.9%. With further improvements in the picking cycle time and handling of heavy foliage occlusions, this new modular robot design holds promise for commercial harvesting of apples.

</details>

---

### [[20_Research/Papers/具身智能/Self-Improving_VLA_Policies_Selected_Diffusion_Noise_for_Spurious-Robust_Action_Smoothing|Self-Improving VLA Policies: Selected Diffusion Noise for Spurious-Robust Action Smoothing]]

![[assets/2606.14084_figure.png|800]]

- **arXiv**: [2606.14084](https://arxiv.org/abs/2606.14084)
- **PDF**: https://arxiv.org/pdf/2606.14084
- **详细分析**: [[20_Research/Papers/具身智能/Self-Improving_VLA_Policies_Selected_Diffusion_Noise_for_Spurious-Robust_Action_Smoothing|Self-Improving VLA Policies: Selected Diffusion Noise for Spurious-Robust Action Smoothing]]
- **作者**: Duc Minh Nguyen, Bao-Ngoc Dao, Tung M. Luu, Binh Gia Nguyen, Vinh Tong, Anji Liu, Vu N. Duong, Dung D. Le, Daniel Sonntag, Trung Le, Ngan Le, Jan Peter...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Self-Improving VLA Policies: Selected Diffusion Noise for Spurious-Robust Action Smoothing》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based Vision-Language-Action (VLA) policies enable strong generalization in robotic manipulation, but remain sensitive to spurious visual correlations and noisy action generation, leading to brittle behavior under perturbations. We introduce Selected Diffusion Noise (SDN), a simple, training-free test-time method that improves both robustness and success rate by leveraging the diffusion noise space as a controllable degree of freedom. SDN dynamically samples noise vectors that are maximally separated from a reference set to mitigate reliance on spurious cues, while selecting candidates that yield more coherent action trajectories. This dual objective encourages stable behavior even under object-masked observations and reduces action jitter without modifying model parameters. We evaluate SDN on two simulation benchmarks (Google Robot, Widow-X) and two real-world robotic datasets across multiple VLA policies, including pi_0, Groot-N1.5, and Groot-N1.6. SDN consistently improves success rates by +8% in simulation and +10% in real-world settings, while producing smoother and more stable actions. Our results highlight that diffusion noise selection can serve as an effective and general mechanism for enhancing VLA policies at test time.

</details>

---

### [[20_Research/Papers/机器人/The_N2D_Haptic_Glove_A_Multi-Finger_Glove_for_2D_Directional_Force_Feedback_for_Contact_Rich_Manipulation|The N2D Haptic Glove: A Multi-Finger Glove for 2D Directional Force Feedback for Contact Rich Manipulation]]

![[assets/2606.14083_figure.jpg|800]]

- **arXiv**: [2606.14083](https://arxiv.org/abs/2606.14083)
- **PDF**: https://arxiv.org/pdf/2606.14083
- **详细分析**: [[20_Research/Papers/机器人/The_N2D_Haptic_Glove_A_Multi-Finger_Glove_for_2D_Directional_Force_Feedback_for_Contact_Rich_Manipulation|The N2D Haptic Glove: A Multi-Finger Glove for 2D Directional Force Feedback for Contact Rich Manipulation]]
- **作者**: Yao-Ting Huang, Jake Honma, Omar Hernandez, Logan Li, Kaitlin Calimbahin, Bryce Hackel, Michael C. Yip
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《The N2D Haptic Glove: A Multi-Finger Glove for 2D Directional Force Feedback for Contact Rich Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans rely on directional fingertip forces to probe and regulate contact during manipulation, yet most wearable haptic gloves render only vibration or single-axis force, leaving force direction ambiguous. Without directional cues, users must infer contact force from vision alone, often leading to over-pressing, inconsistent control, and reduced precision in robotic teleoperation. We present the N2D Haptic Glove, a multi-finger wearable device that renders planar flexion-extension fingertip forces using capstan-drive transmissions for high-transparency force feedback. Through benchtop validations and a user study involving haptic teleoperation of a robotic arm and hand, we demonstrate that compared to visual-only and single-axis haptic baselines, planar fingertip feedback significantly reduces contact force error during precise manipulation, improves trial-to-trial consistency, and enhances overall user experience in axial probing tasks. These findings establish the N2D Haptic Glove and directional finger-based haptics devices as a promising modality for contact-rich teleoperation, immersive virtual reality simulations, and robot learning from demonstrations. N2D Haptic Glove's hardware and software system will be fully open-sourced at \href{https://ucsdarclab.github.io/n2d-glove/}{this https URL}.

</details>

---

### [[20_Research/Papers/机器人/Development_of_a_3_in_Sewer_Pipe_Inspection_Robot_with_an_Articulated_Differential_Mechanism_using_X-shaped_Linkages|Development of a 3 in Sewer Pipe Inspection Robot with an Articulated Differential Mechanism using X-shaped Linkages]]

![[assets/2606.14070_figure.png|800]]

- **arXiv**: [2606.14070](https://arxiv.org/abs/2606.14070)
- **PDF**: https://arxiv.org/pdf/2606.14070
- **详细分析**: [[20_Research/Papers/机器人/Development_of_a_3_in_Sewer_Pipe_Inspection_Robot_with_an_Articulated_Differential_Mechanism_using_X-shaped_Linkages|Development of a 3 in Sewer Pipe Inspection Robot with an Articulated Differential Mechanism using X-shaped Linkages]]
- **作者**: Shoya Umemura, Ryota Taniguchi, Atsushi Kakogawa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Development of a 3 in Sewer Pipe Inspection Robot with an Articulated Differential Mechanism using X-shaped Linkages》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes, an improved version of the 3 in sewer pipe inspection robot equipped with an emergency evacuation mechanism. The low traction force and poor stepover capability, which were challenges of the first version, have been improved by simply connecting the propulsion units. The coupled propulsion units feature a differential mechanism capable of posture changes via a single wire, enabling adaptation to pipe diameter variations. To traverse obstacles like pipe joints, a control method was devised that detects obstacle contact through current load on the drive wheel motors and slackens the wire. This method was verified through simulated pipe experiments. Load comparisons were made using current waveforms applied to the drive wheels. Our proposed control method significantly improved the step-over capability of the new articulated robots.

</details>

---

### [[20_Research/Papers/机器人/Semidefinite_Relaxations_for_Collision-Free_Motion_Planning|Semidefinite Relaxations for Collision-Free Motion Planning]]

![[assets/2606.14063_figure.png|800]]

- **arXiv**: [2606.14063](https://arxiv.org/abs/2606.14063)
- **PDF**: https://arxiv.org/pdf/2606.14063
- **详细分析**: [[20_Research/Papers/机器人/Semidefinite_Relaxations_for_Collision-Free_Motion_Planning|Semidefinite Relaxations for Collision-Free Motion Planning]]
- **作者**: Bernhard Paus Graesdal, Alexandre Amice, Pablo A. Parrilo, Russ Tedrake
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Semidefinite Relaxations for Collision-Free Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study semidefinite relaxations for collision-free motion planning. We focus on a point robot moving from start to goal through spherical obstacles in $\mathbb{R}^n$, subject to path continuity constraints and squared derivative costs; a setting that is conceptually simple yet captures the hardness of collision-free motion planning. We formulate this problem exactly as a nonconvex problem over polynomial curves, and present a natural semidefinite relaxation. We contribute two key theoretical insights; to our knowledge this is the first theoretical analysis of semidefinite relaxations for collision-free motion planning. First, we show that solving the convex relaxation is equivalent to solving, to global optimality, a related motion planning problem in a potentially higher-dimensional space. This geometric interpretation yields necessary and sufficient conditions for tightness, and a clear intuition for when the relaxation is loose. Second, we show that the relaxation admits a symmetry reduction that makes it significantly smaller than one might expect, with positive semidefinite cone sizes that scale linearly with the polynomial degree and are independent of the ambient dimension. The resulting relaxation is 10 to 100 times faster than direct nonlinear programming transcriptions solved with SNOPT and IPOPT, exhibits significantly lower variance in solve times, and reliably finds a locally optimal path for the original problem. We demonstrate its effectiveness as a convex steering function in an RRT planner for minimum-snap quadrotor planning with $C^4$ continuous trajectories.

</details>

---

### [[20_Research/Papers/世界模型/ReactSim-Bench_Benchmarking_Reactive_Behavior_World_Model_Simulation_in_Autonomous_Driving|ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving]]

![[assets/2606.14058_figure.png|800]]

- **arXiv**: [2606.14058](https://arxiv.org/abs/2606.14058)
- **PDF**: https://arxiv.org/pdf/2606.14058
- **详细分析**: [[20_Research/Papers/世界模型/ReactSim-Bench_Benchmarking_Reactive_Behavior_World_Model_Simulation_in_Autonomous_Driving|ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving]]
- **作者**: Zhiyuan Zhang, Yanlun Peng, Jianing Zhang, Xianda Guo, Zehan Huang, Haoran Liu, Qifeng Li, Shaofeng Zhang, Xiaosong Jia, Junchi Yan
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《ReactSim-Bench: Benchmarking Reactive Behavior World Model Simulation in Autonomous Driving》归入 世界模型、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ReactSim-Bench, TrafficSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reactive capability is a key property of data-driven behavior world model simulators for autonomous driving simulation systems. With this capability, simulated world agents can respond feasibly to autonomous vehicle (AV) behaviors that differ from the log. However, existing behavior simulation benchmarks do not directly measure reactive capability. They often let the simulator jointly control the AV and surrounding agents and evaluate realism through log similarity or open-loop prediction metrics. In this work, we introduce ReactSim-Bench for evaluating the reactive capability of behavior world model simulation in autonomous driving. We decouple the control of agents and the AV, using AV behaviors that differ from the log and require agents to respond as independent AV inputs. To obtain these AV behaviors, we construct a pipeline that uses an AV planner model to generate candidate behaviors and filters the data using rules and manual verification. Collision metrics, map-based metrics, and kinematic feasibility metrics are used to evaluate the safety and rule compliance of reactive responses. We construct 2,636 test scenarios with three categories and conduct a systematic evaluation of state-of-the-art models across multiple architectures, including Transformer-based, diffusion-based, and next-token-prediction-based models. We further analyze how replan frequency affects performance and provide insights for future studies.

</details>

---

### [[20_Research/Papers/具身智能/SplatlessDF_Continuous_Distance_Field_Mapping_with_Non-Splatting_Gaussians|SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians]]

![[assets/2606.13990_figure.png|800]]

- **arXiv**: [2606.13990](https://arxiv.org/abs/2606.13990)
- **PDF**: https://arxiv.org/pdf/2606.13990
- **详细分析**: [[20_Research/Papers/具身智能/SplatlessDF_Continuous_Distance_Field_Mapping_with_Non-Splatting_Gaussians|SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians]]
- **作者**: Monisha Mushtary Uttsha, Lan Wu, Teresa Vidal-Calleja
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《SplatlessDF: Continuous Distance Field Mapping with Non-Splatting Gaussians》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent Gaussian splatting (GS) methods have shown that scenes can be represented efficiently with optimisable Gaussians for high-quality reconstruction and rendering. In this paper, building on this principle, we introduce SplatlessDF, a continuous distance field (DF) mapping framework that uses anisotropic Gaussian elements from a spatial rather than photometric perspective. SplatlessDF directly parameterises the Gaussians and optimises to recover a differentiable DF, enabling distances and gradients to be queried in the spatial domain for downstream robotic tasks such as navigation. Furthermore, SplatlessDF can be coupled with 2D Gaussian splatting (2DGS), providing a unified framework based solely on Gaussian primitives that can learn continuous DF and surface models and supports photometric rendering. We consider two settings: a standalone DF-only formulation and a joint DF-rendering formulation coupled with 2DGS. Experiments show that the standalone formulation provides efficient and accurate distance and gradient queries, while the joint formulation improves rendering geometry and simultaneously models a continuous DF. These results highlight the potential of GS-style representations not only for surface modelling and rendering but also for mapping representations suited to robotic navigation.

</details>

---

### [[20_Research/Papers/具身智能/Guided_Diffusion_with_Distilled_Vision-Language_Reliability_for_Aerial_Navigation|Guided Diffusion with Distilled Vision-Language Reliability for Aerial Navigation]]

![[assets/2606.13883_figure.jpg|800]]

- **arXiv**: [2606.13883](https://arxiv.org/abs/2606.13883)
- **PDF**: https://arxiv.org/pdf/2606.13883
- **详细分析**: [[20_Research/Papers/具身智能/Guided_Diffusion_with_Distilled_Vision-Language_Reliability_for_Aerial_Navigation|Guided Diffusion with Distilled Vision-Language Reliability for Aerial Navigation]]
- **作者**: Ivan Valuev, Iana Zhura, Valerii Serpiva, Didar Seyidov, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Guided Diffusion with Distilled Vision-Language Reliability for Aerial Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous UAV navigation is conventionally solved by pipelines that separate perception, mapping, and planning into distinct stages, which propagates errors, accumulates latency, and requires environment-specific retuning. End-to-end generative models remove these interfaces by mapping raw observations directly to trajectories, but inherit a subtle failure mode: trained on clean data, they cannot recognise when an observation is unreliable, and treat degraded regions such as glass, mirrors, and overexposed surfaces as valid evidence for planning. We present a reliability-aware diffusion planner for 3D UAV navigation. It conditions trajectory generation on the observation together with a scene-level reliability heatmap that marks where perception cannot be trusted, produced by a lightweight network that distils the open-vocabulary reasoning of a vision-language model within the real-time planning budget. To generalise to unseen environments without retraining, we steer the denoising process with a differentiable two-stage ESDF cost that treats physical obstacles from depth and virtual obstacles from highly unreliable regions on equal footing. In simulation and on a real quadrotor, our planner produces markedly safer trajectories than a state-of-the-art diffusion baseline, reducing the obstacle-violation rate from 40.3% to 9.6% and raising the mean reliability of traversed regions from 0.588 to 0.925. Ablating the reliability term alone drops mean reliability from 0.898 to 0.783, confirming it as the decisive component, while distillation runs the framework up to 2 times faster than the full vision-language model.

</details>

---

### [[20_Research/Papers/具身智能/AnyGoal_Vision-Language_Guided_Multi-Agent_Exploration_for_Training-Free_Lifelong_Navigation|AnyGoal: Vision-Language Guided Multi-Agent Exploration for Training-Free Lifelong Navigation]]

![[assets/2606.13878_figure.png|800]]

- **arXiv**: [2606.13878](https://arxiv.org/abs/2606.13878)
- **PDF**: https://arxiv.org/pdf/2606.13878
- **详细分析**: [[20_Research/Papers/具身智能/AnyGoal_Vision-Language_Guided_Multi-Agent_Exploration_for_Training-Free_Lifelong_Navigation|AnyGoal: Vision-Language Guided Multi-Agent Exploration for Training-Free Lifelong Navigation]]
- **作者**: MoniJesu James, Marcelino Julio Fernando, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.8，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《AnyGoal: Vision-Language Guided Multi-Agent Exploration for Training-Free Lifelong Navigation》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, MARL, Real-World, YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end navigation policies trained on large simulation corpora degrade sharply when transferred to out-of-distribution scenes, categories, or goal modalities. Modular pipelines such as Modular GOAT are bottlenecked by closed-set object detection recall, while 3D snapshot-memory systems (e.g. 3D-Mem) accumulate dense, view-dependent representations that are heavy to maintain. We present AnyGoal, a training-free multi-robot architecture that places a Vision-Language Model (VLM) at the core of frontier-based exploration and coordinates agents through a shared 2D Gaussian Bayesian Value Map (BVM). The BVM maintains a per-pixel (mu, sigma^2) posterior over goal relevance, updated via precision-weighted fusion of VLM scores through a depth-cone mask, and is never reset between subtasks, yielding lifelong evidence accumulation. Frontiers are ranked by a convex blend of a VLM-as-judge softmax and a Bayesian UCB term on the BVM. A greedy allocator with spatial-separation penalty and commitment hysteresis distributes frontiers across agents without a centralized controller. On the full GOAT-Bench val unseen split (360 episodes, 2,669 subtasks), our dual-agent system achieves 52.4% Subtask SR at 12.7% SPL--state of the art under the strict physical regime (discrete 0.25 m steps, no teleportation, 42 deg HFOV) and a +27.5 pp improvement over Modular GOAT (24.9%). Single-agent AnyGoal achieves 41.9% Subtask SR, showing gains arise from the decision architecture. A four-way perception ablation shows that open-vocabulary detectors shift the dominant failure mode from exploration to goal verification.

</details>

---

### [[20_Research/Papers/具身智能/ContactWorld_What_Matters_in_Vision-Tactile_World_Models_for_Contact-Rich_Manipulation|ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation]]

![[assets/2606.13877_figure.png|800]]

- **arXiv**: [2606.13877](https://arxiv.org/abs/2606.13877)
- **PDF**: https://arxiv.org/pdf/2606.13877
- **详细分析**: [[20_Research/Papers/具身智能/ContactWorld_What_Matters_in_Vision-Tactile_World_Models_for_Contact-Rich_Manipulation|ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation]]
- **作者**: Zhiyuan Zhang, Pokuang Zhou, Kaidi Zhang, Adeesh Desai, Temitope Amosa, Davood Soleymanzadeh, Jiuzhou Lei, Minghui Zheng, Yu She
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，世界模型 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ContactWorld: What Matters in Vision-Tactile World Models for Contact-Rich Manipulation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ContactWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation requires world models to reason over complex contact dynamics from multimodal sensory observations. However, it remains unclear which representation properties fundamentally support stable long-horizon planning in contact-rich settings. In this paper, we present ContactWorld, a benchmark and systematic empirical study of vision-tactile world models spanning 12 contact-rich manipulation tasks, including insertion, disassembly, screwing, and exploratory interaction. Across extensive experiments, we find that representations that are both spatially structured and temporally continuous consistently achieve the strongest planning performance. In particular, point-cloud observations improve average planning success rates from 20.7% with wrist-view observations and 22.0% with front-view observations to 32.1%. We further find that the effectiveness of tactile sensing depends critically on cross-modal representation compatibility rather than modality scaling alone. Combining point-cloud observations with tactile force-field representations, which preserve richer spatial structure and interaction dynamics, further improves performance to 36.1%, yielding the strongest overall planning performance across all evaluated tasks. Moreover, tactile sensing becomes increasingly important under long-horizon planning objectives, where compounding prediction errors and contact uncertainty accumulate over time. Together, these findings highlight the importance of representation structure, multimodal compatibility, and long-horizon robustness in vision-tactile world models for contact-rich robotic manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Output-Level_Regularization_Eliminates_the_Seed_Lottery_in_Single-GPU_VLA_Fine-Tuning|Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning]]

![[assets/2606.13856_figure.png|800]]

- **arXiv**: [2606.13856](https://arxiv.org/abs/2606.13856)
- **PDF**: https://arxiv.org/pdf/2606.13856
- **详细分析**: [[20_Research/Papers/具身智能/Output-Level_Regularization_Eliminates_the_Seed_Lottery_in_Single-GPU_VLA_Fine-Tuning|Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning]]
- **作者**: Jeffrin Sam, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Output-Level Regularization Eliminates the Seed Lottery in Single-GPU VLA Fine-Tuning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：JEPA-VLA, OpenVLA, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-tuning a vision-language-action model (VLA-JEPA) on a single GPU should be simple: load a pretrained checkpoint, run training, deploy. There is a hidden danger. Run the same fine-tuning code thirteen times -- same data, same architecture, different random seed -- and twelve runs produce a robot succeeding 91--94% of the time, while one run silently degrades to 65.2%: a 29 pp gap with no error message, no warning, and no way to predict which seed will fail. We call this the seed lottery. We trace the cause to output collapse: the action predictor quietly learns to produce nearly identical outputs regardless of what the robot sees. Existing weight-level methods (L2, EWC) are structurally blind to this collapse -- they penalize weight changes, but collapse occurs in directions weights can move freely without affecting outputs, a gap we formalize via the Jacobian null-space. Across 7 methods x up to 13 seeds x 3 LIBERO benchmarks, three output-level regularizers -- VICReg (n=12 seeds), Dropout (n=4), and a halved learning rate (n=5) -- each eliminate every catastrophic seed (0/21 combined collapses vs. 1/13 Baseline; F(12,11)=28.7, p&lt;0.001), while weight-level methods (L2, EWC) preserve the lottery. The simplest fix is changing one number in your optimizer config.

</details>

---

### [[20_Research/Papers/强化学习/Efficient_Domain-Adaptive_Policy_Learning_via_Kernel_Representation_with_Application_to_Quadrotor_Control_under_Non-Stationary_Disturbances|Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances]]

![[assets/2606.13842_figure.jpg|800]]

- **arXiv**: [2606.13842](https://arxiv.org/abs/2606.13842)
- **PDF**: https://arxiv.org/pdf/2606.13842
- **详细分析**: [[20_Research/Papers/强化学习/Efficient_Domain-Adaptive_Policy_Learning_via_Kernel_Representation_with_Application_to_Quadrotor_Control_under_Non-Stationary_Disturbances|Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances]]
- **作者**: Hongyu Zhou, Mingtian Tan, Vasileios Tzoumas
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: RL

#### 研究背景与动机

《Efficient Domain-Adaptive Policy Learning via Kernel Representation with Application to Quadrotor Control under Non-Stationary Disturbances》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present an algorithm for efficient domain-adaptive policy learning via kernel representations. Learning domain-adaptive policies is challenging since it requires an environment representation that is both sufficiently expressive to model complex sim-to-real gaps during offline training, and computationally efficient enough to support rapid online adaptation during deployment. For instance, a quadrotor may encounter time-varying, non-stationary disturbances, such as sudden gusts of wind, payload shifts, or transitions between distinct flight regimes with and without ground effects. To address these challenges, we model unknown disturbances using a differentiable kernel approximation based on random Fourier features. During the offline training phase, we randomly sample kernel coefficients and bandwidth parameters to generate a rich diversity of disturbance profiles. We then optimize the control policy via differentiable simulation with analytical gradients, a process that takes only 50 seconds of training time on an RTX 4090 GPU. During hardware deployment, the policy adapts to non-stationary environments in real time by updating both the kernel coefficients and bandwidth through online least-squares estimation. We evaluate our method on quadrotor trajectory tracking tasks across high-fidelity numerical simulations and hardware experiments using Crazyflie, subjected to various disturbances, including complex aerodynamic effects, wind, ground effects, and payload fluctuations.

</details>

---
