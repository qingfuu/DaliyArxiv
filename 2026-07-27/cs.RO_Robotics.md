# cs.RO | Robotics | 2026-07-27

#arxiv #ComputerScience

**论文数**: 17

### [[20_Research/Papers/具身智能/ViTacWorld_Scaling_Visuo-Tactile_World_Models_for_Contact-Rich_Robot_Manipulation|ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation]]

![[assets/2607.22530_figure.png|800]]

- **arXiv**: [2607.22530](https://arxiv.org/abs/2607.22530)
- **PDF**: https://arxiv.org/pdf/2607.22530
- **详细分析**: [[20_Research/Papers/具身智能/ViTacWorld_Scaling_Visuo-Tactile_World_Models_for_Contact-Rich_Robot_Manipulation|ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation]]
- **作者**: Yunao Huang, Shiyu Sang, Haotao Lu, Suting Ni, Shijie Wu, Ziyang Guo, Ye Shi, Jingya Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.4（加权：具身智能 1.5，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《ViTacWorld: Scaling Visuo-Tactile World Models for Contact-Rich Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DreamTacVLA, ForceVLA, Tactile-VLA, TouchWorld, ViTacWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich robot manipulation requires physical interaction cues that are often invisible to cameras, making tactile sensing essential for robust control. However, scaling visuo-tactile robot learning remains difficult because real tactile interaction data are expensive to collect, hardware-dependent, and limited in task and scene diversity. We present ViTacWorld, an action-conditioned visuo-tactile world model for scalable contact-rich robot manipulation. ViTacWorld leverages public real tactile datasets and a constructed simulation environment to scale visuo-tactile-action data, exploiting the fact that tactile signals are directly grounded in physical contact and can exhibit a smaller simulation-to-real gap than purely visual observations. The model is first pretrained with large-scale real and simulated visuo-tactile trajectories, and then finetuned with real-world policy rollouts to better match downstream manipulation behaviors. Given robot actions, ViTacWorld predicts temporally aligned visual observations and tactile feedback, enabling visuo-tactile-action rollout generation. To the best of our knowledge, ViTacWorld is the first framework that uses a world model for robot visuo-tactile-action trajectory generation and policy evaluation. It serves two roles: synthesizing rollouts to improve downstream tactile policies, and evaluating policies by predicting action-conditioned visuo-tactile outcomes under controlled action sequences. Experiments on contact-rich manipulation tasks show that ViTacWorld generates physically meaningful rollouts, improves policy performance through scalable data augmentation, and enables action-conditioned policy evaluation. Project page: https://vitacworld.github.io/

</details>

---

### [[20_Research/Papers/机器人/Plug,_Play,_and_Comply_A_Modular_Framework_for_Online_Variable_Impedance_with_Arbitrarily_Oriented_Compliance_Axes|Plug, Play, and Comply: A Modular Framework for Online Variable Impedance with Arbitrarily Oriented Compliance Axes]]

![[assets/2607.22483_figure.png|800]]

- **arXiv**: [2607.22483](https://arxiv.org/abs/2607.22483)
- **PDF**: https://arxiv.org/pdf/2607.22483
- **详细分析**: [[20_Research/Papers/机器人/Plug,_Play,_and_Comply_A_Modular_Framework_for_Online_Variable_Impedance_with_Arbitrarily_Oriented_Compliance_Axes|Plug, Play, and Comply: A Modular Framework for Online Variable Impedance with Arbitrarily Oriented Compliance Axes]]
- **作者**: Mihael Simonič, Xiaocong Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Plug, Play, and Comply: A Modular Framework for Online Variable Impedance with Arbitrarily Oriented Compliance Axes》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The paper proposes a robot-agnostic compliant-control framework that extends the ROS control ecosystem with standardized joint and Cartesian command interfaces. It addresses a key limitation of existing control software: no reusable infrastructure for implementing compliant-control algorithms across different manipulators while preserving a common interface to higher-level applications. A plugin-based architecture separates controller infrastructure from control-law implementation. Generic wrappers use existing hardware abstractions to interface with different manipulators, while runtime-loaded plugins implement only the control law. Command interfaces support joint- and Cartesian-space references, stiffness and damping gains, nullspace targets, and feedforward terms, enabling variable impedance and diverse compliant-control formulations. Robot kinematics and dynamics are computed from URDF models using Pinocchio. The architecture facilitates the development of compliant-control strategies and enables the same implementation to be deployed across platforms unchanged. The complete framework, including reference controllers, high-level task interfaces, and example configurations for various manipulators, is open-sourced. The reference Cartesian impedance controller supports task-dependent compliance by rotating translational and rotational stiffness and damping, allowing the principal compliance directions to be updated online according to local task geometry rather than remaining fixed in the robot base or TCP frame. This is particularly important in contact-rich manipulation, where the desired directions of motion, constraints, and compliance directions may vary throughout task execution. Real-robot experiments demonstrate task-dependent compliance in contact-rich manipulation, while simulations show portability across manipulators with distinct kinematic and dynamic characteristics.

</details>

---

### [[20_Research/Papers/强化学习/Conformal_Constraint_Tightening_for_Chance-Constrained_Motion_Planning_with_Unknown_Dynamics|Conformal Constraint Tightening for Chance-Constrained Motion Planning with Unknown Dynamics]]

![[assets/2607.22409_figure.png|800]]

- **arXiv**: [2607.22409](https://arxiv.org/abs/2607.22409)
- **PDF**: https://arxiv.org/pdf/2607.22409
- **详细分析**: [[20_Research/Papers/强化学习/Conformal_Constraint_Tightening_for_Chance-Constrained_Motion_Planning_with_Unknown_Dynamics|Conformal Constraint Tightening for Chance-Constrained Motion Planning with Unknown Dynamics]]
- **作者**: Shubham Natraj, Bruno Sinopoli, Yiannis Kantaros
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.4，机器人 1.1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Conformal Constraint Tightening for Chance-Constrained Motion Planning with Unknown Dynamics》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion planning algorithms compute control sequences that drive autonomous robots to goal regions while avoiding unsafe states. Existing methods, from sampling-based planning to deep reinforcement learning, typically provide task-completion guarantees only with respect to a nominal model or simulator, which may be invalidated when the true dynamics are unknown or difficult to model accurately. This letter addresses this limitation for systems with unknown dynamics and an available approximate nominal model, contributing a planner-agnostic constraint-tightening procedure that equips existing planners with a probabilistic task-completion guarantee on the true system. We leverage conformal prediction to provide a probabilistic bound on the nominal-to-true trajectory deviation over a distribution of planning problems. We tighten the planning constraints using that bound, and show that solving the tightened problem under the nominal model is a sufficient condition for solving the original problem on the true system with a prescribed probability. We validate the theoretical guarantees empirically and demonstrate substantially improved task completion relative to nominal-model planning.

</details>

---

### [[20_Research/Papers/具身智能/A_Monolithic_Hand_with_Asymmetric_Origami_Bending_and_Dual-chamber_Actuators|A Monolithic Hand with Asymmetric Origami Bending and Dual-chamber Actuators]]

![[assets/2607.22320_first_page.png|800]]

- **arXiv**: [2607.22320](https://arxiv.org/abs/2607.22320)
- **PDF**: https://arxiv.org/pdf/2607.22320
- **详细分析**: [[20_Research/Papers/具身智能/A_Monolithic_Hand_with_Asymmetric_Origami_Bending_and_Dual-chamber_Actuators|A Monolithic Hand with Asymmetric Origami Bending and Dual-chamber Actuators]]
- **作者**: Nan Huang, Yuming Zhu, Zicong Zhang, Jianhui Liu, Xiaohuang Liu, Dihan Liu, Jiansheng Dai, Sicong Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《A Monolithic Hand with Asymmetric Origami Bending and Dual-chamber Actuators》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The passive adaptability inherent in soft robotic hands affords them advantages in applications that require safe and compliant interaction. However, existing soft robotic hands often struggle to simultaneously achieve adequate output performance and easy manufacturing due to their complicated structures. In this paper, we introduce the asymmetric origami bending (AOB) pattern for generating bending motion and the asymmetric dual-chamber (ADC) design for obtaining multifunction capability. The AOB single (AOB-S) chamber and AOB dual-chamber (AOB-D) units are designed and constitute the finger and palm actuators of the proposed Origami-inspired SOft Robotic (OSOR) hand. The OSOR hand achieves bio-inspired fingers-palm motions and adequate output performance within a monolithic structure that significantly simplifies the manufacturing process. By defining the asymmetric ratio to characterize the geometric asymmetry of the unit, the analytical models of the AOB and ADC structures are proposed. The Finite Element Analysis tool for the design of AOB actuators is obtained by geometric analysis. The asymmetric origami design grants the integrated manufacturing of the OSOR hand through a Selective Laser Sintering printing process with a single thermoplastic polyurethane material. The model and simulations are validated by experimental results. Experiments show the finger and palm maximum bending motion range of 203° and 40°, respectively, with output forces of 6.3 N and 16 N. The OSOR hand is capable of pinching a piece of tissue, stably grasping water bottles with two fingers, palm-only grasping, and completing the power grasps in the taxonomy of manufacturing grasps. The compactness, performance, and easy manufacturing of the proposed hand benefit the development of the soft robotic hand with new possibilities.

</details>

---

### [[20_Research/Papers/机器人/Design_and_Human_Evaluation_of_Tactile_Withdrawal_Reflexes_for_a_Skin-Covered_Robot_Arm|Design and Human Evaluation of Tactile Withdrawal Reflexes for a Skin-Covered Robot Arm]]

![[assets/2607.22249_figure.png|800]]

- **arXiv**: [2607.22249](https://arxiv.org/abs/2607.22249)
- **PDF**: https://arxiv.org/pdf/2607.22249
- **详细分析**: [[20_Research/Papers/机器人/Design_and_Human_Evaluation_of_Tactile_Withdrawal_Reflexes_for_a_Skin-Covered_Robot_Arm|Design and Human Evaluation of Tactile Withdrawal Reflexes for a Skin-Covered Robot Arm]]
- **作者**: Laura Babayeva, Lukas Rustler, Matej Hoffmann
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Design and Human Evaluation of Tactile Withdrawal Reflexes for a Skin-Covered Robot Arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Nociception is a protective biological mechanism that links harmful stimulation to a reaction. This paper investigates artificial nociception for a robotic arm with whole-body tactile sensing. We present a complete pipeline that maps pressure changes from sensitive skin on a robot manipulator to bio-inspired withdrawal motions. The system first converts skin pressure into a scalar pain gain using a nonlinear continuous model. We compare three reflexes: (i) uniform reflex moves four robot joints by a fixed amount, whereby the withdrawal is approximated by a movement of the arm "toward the base", independent of where the robot was touched; (ii) biologically motivated location-dependent joint-space withdrawal derived from human withdrawal reflex characteristics; (iii) Cartesian space withdrawal along the surface normal of the contacted skin pad. All behaviors are integrated in a reflex controller that interrupts the task, executes the withdrawal, and returns to a pre-contact pose. A user study with 15 participants compared the strategies using Godspeed questionnaire subscales, custom perceived-naturalness and safety items, forced-choice comparisons, and qualitative feedback. Interestingly, participants rated more highly the uniform reflex behavior over one or both competitors on the anthropomorphism, animacy, and likeability Godspeed subscales and on the Naturalness and Realism custom scale. When asked to compare the conditions, the uniform reflex was scored best in "felt safest", "most human-like", and "most natural". This suggests that predictability of the robot behavior is key for user acceptance. The Cartesian reflex was judged the most appropriate reaction to touch. The bio-inspired reflex did not lead any evaluated measure. This may be partly attributed to the embodiment gap between the robot arm and human arm and participants having different expectations from a robot manipulator.

</details>

---

### [[20_Research/Papers/具身智能/Offline_Vision-Language_Navigation_with_Geometric_Goal_Localization_for_Outdoor_Environments|Offline Vision-Language Navigation with Geometric Goal Localization for Outdoor Environments]]

![[assets/2607.22226_first_page.png|800]]

- **arXiv**: [2607.22226](https://arxiv.org/abs/2607.22226)
- **PDF**: https://arxiv.org/pdf/2607.22226
- **详细分析**: [[20_Research/Papers/具身智能/Offline_Vision-Language_Navigation_with_Geometric_Goal_Localization_for_Outdoor_Environments|Offline Vision-Language Navigation with Geometric Goal Localization for Outdoor Environments]]
- **作者**: Ali Salmasi, Xianjia Yu, Tomi Westerlund
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Offline Vision-Language Navigation with Geometric Goal Localization for Outdoor Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation-model-based vision-language navigation (VLN) has advanced autonomous robot navigation by enabling robots to interpret natural-language instructions, identify semantic goals, and follow user-specified behavioral rules. However, existing VLN systems rely heavily on cloud-hosted foundation models for language understanding and semantic grounding, limiting their applicability where network connectivity is unavailable and reliable metric goal localization is required. Although recent small language models (SLMs) enable fully onboard inference, their suitability for navigation instruction decomposition has not been systematically evaluated. This paper makes three contributions toward fully onboard VLN for outdoor environments. First, we present the first systematic benchmark of 17 edge-deployable SLMs against 4 online APIs for robotic navigation instruction decomposition, evaluating accuracy and latency on human-annotated instructions across three computing platforms and providing practical guidance for selecting onboard language models. Second, we propose a lightweight hybrid semantic-geometric goal localization framework that combines open-vocabulary object detection, prompted segmentation, and LiDAR geometry to estimate metric goals, while maintaining visual bearing guidance when reliable geometric observations are unavailable. Third, we integrate these advances into Edge-BehAV, a fully onboard extension of the BehAV architecture that enables cloud-independent behavior-guided navigation. Experimental results show that the best offline SLM matches the instruction decomposition performance of the strongest cloud API while running approximately 9x faster and without network connectivity. The proposed goal localization framework reduces mean goal-distance error from 2.05 m to 0.20 m at lower computational cost, and the complete system succeeds in 31 of 32 closed-loop outdoor trials.

</details>

---

### [[20_Research/Papers/具身智能/Safe_Learning_Predictive_Control_for_Ego-World_Robotic_Systems|Safe Learning Predictive Control for Ego-World Robotic Systems]]

![[assets/2607.22225_figure.png|800]]

- **arXiv**: [2607.22225](https://arxiv.org/abs/2607.22225)
- **PDF**: https://arxiv.org/pdf/2607.22225
- **详细分析**: [[20_Research/Papers/具身智能/Safe_Learning_Predictive_Control_for_Ego-World_Robotic_Systems|Safe Learning Predictive Control for Ego-World Robotic Systems]]
- **作者**: Davide Valenti, Giuseppe Notarstefano
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Safe Learning Predictive Control for Ego-World Robotic Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Ego-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe autonomous navigation in shared environments requires the ability to anticipate and react to the latent behaviors of surrounding robots. In this paper, we propose SOWL-MPC, a safe learning-based predictive control strategy for a novel scenario, which we name ego-world robotic framework. In this setting, the control policy of the world robot is unknown and the ego exploits data to learn it and perform safe maneuvers. The proposed architecture combines an online learning mechanism based on Sparse Variational Gaussian Processes (SVGPs) with a receding-horizon control scheme. Relying solely on noisy state measurements, our approach infers a posterior distribution over the latent world policy, which is updated on streaming data via Online Variational Conditioning (OVC). The learned policy is propagated through the nonlinear world dynamics using an approximate moment propagation scheme, and fed to an uncertainty-aware Model Predictive Control (MPC), thus enabling safe maneuvering of the ego robot. The real-time feasibility and safety guarantees of SOWL-MPC are demonstrated through extensive Monte Carlo virtual experiments in ROS 2, and validated on real-world robotic hardware in an indoor arena.

</details>

---

### [[20_Research/Papers/机器人/Flight-Ready_LiDAR-Inertial_Odometry_for_Embedded_Drone_Platforms|Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms]]

![[assets/2607.22145_figure.jpg|800]]

- **arXiv**: [2607.22145](https://arxiv.org/abs/2607.22145)
- **PDF**: https://arxiv.org/pdf/2607.22145
- **详细分析**: [[20_Research/Papers/机器人/Flight-Ready_LiDAR-Inertial_Odometry_for_Embedded_Drone_Platforms|Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms]]
- **作者**: Alvaro J. Gaona, David Perez-Saura, Francisco J. Anguita, Pascual Campoy
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《Flight-Ready LiDAR-Inertial Odometry for Embedded Drone Platforms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-source LiDAR-inertial odometry (LIO) systems have achieved remarkable benchmark accuracy, yet current state-of-the-art implementations are primarily optimized for evaluation performance rather than the requirements of real-time closed-loop aerial control. When deployed onboard UAVs, this can introduce limitations that degrade flight performance. In this work, we identify five architectural deficiencies in a representative tightly coupled IESKF-based LIO implementation: odometry publishing tied to the LiDAR rate (10 Hz instead of the IMU's 200 Hz), missing velocity outputs, execution bottlenecks that block IMU processing, mutex contention, and synchronization race conditions. We introduce corresponding modifications including IMU-rate forward propagation, direct body-frame velocity publishing, SLERP-based smoothing, dual-executor isolation, and explicit synchronization protection. The resulting system increases odometry output from ~10 Hz to a stable 200 Hz, provides a complete Twist state at every IMU sample, and preserves continuity during transient LiDAR loss. Experiments on a Livox Mid-360 / Pixhawk 4 Mini autonomous UAV with motion-capture ground truth validate the approach. Since the underlying estimator (IESKF + ikd-Tree) remains unchanged, the proposed improvements can be directly applied to FAST-LIO2-derived implementations.

</details>

---

### [[20_Research/Papers/机器人/DB-VIO_Dual-Branch_Visual_Inertial_Odometry_with_Enhanced_Visual-Inertial_Representation|DB-VIO: Dual-Branch Visual Inertial Odometry with Enhanced Visual-Inertial Representation]]

![[assets/2607.22123_figure.png|800]]

- **arXiv**: [2607.22123](https://arxiv.org/abs/2607.22123)
- **PDF**: https://arxiv.org/pdf/2607.22123
- **详细分析**: [[20_Research/Papers/机器人/DB-VIO_Dual-Branch_Visual_Inertial_Odometry_with_Enhanced_Visual-Inertial_Representation|DB-VIO: Dual-Branch Visual Inertial Odometry with Enhanced Visual-Inertial Representation]]
- **作者**: Ziyu Wan, Lin Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《DB-VIO: Dual-Branch Visual Inertial Odometry with Enhanced Visual-Inertial Representation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FlowNet, VINet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual inertial odometry (VIO) is essential for accurate 6-DoF motion estimation in mobile robotic systems. Recent learning-based VIO methods have shown promising progress, but they often rely on unified visual--inertial representations and a single temporal model for full-pose estimation, limiting their ability to capture the heterogeneous dynamics of rotation and translation. Moreover, monocular visual features often lack explicit geometric structure, while raw inertial encoding leaves the underlying rotational kinematics implicit, weakening the rotation-related cues in IMU features. To address these issues, we propose DB-VIO, a dual-branch visual inertial odometry framework with enhanced visual--inertial representation. DB-VIO incorporates depth cues to improve monocular visual perception, injects an explicit integrated-attitude prior to strengthen rotation-aware inertial representation, and decouples pose estimation into dedicated rotational and translational branches for motion-specific temporal modeling. Experiments on autonomous driving and aerial robot benchmarks show that DB-VIO achieves state-of-the-art performance, improving the corresponding baselines by 20\% on KITTI and 33\% on EuRoC. Notably, under the more agile motion patterns of EuRoC, DB-VIO improves the rotational metric by 65.7\% over prior methods. These results demonstrate the effectiveness and generalization of DB-VIO across different platforms and motion scenarios.

</details>

---

### [[20_Research/Papers/强化学习/Constraint-Driven_Synthesis_of_Hyper_Petri_Nets|Constraint-Driven Synthesis of Hyper Petri Nets]]

![[assets/2607.22062_figure.png|800]]

- **arXiv**: [2607.22062](https://arxiv.org/abs/2607.22062)
- **PDF**: https://arxiv.org/pdf/2607.22062
- **详细分析**: [[20_Research/Papers/强化学习/Constraint-Driven_Synthesis_of_Hyper_Petri_Nets|Constraint-Driven Synthesis of Hyper Petri Nets]]
- **作者**: Maksym Figat, Alessandro Pinto
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Constraint-Driven Synthesis of Hyper Petri Nets》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper addresses the modeling and synthesis of constrained robotic system behaviors using Petri nets (PNs). It investigates how to construct models in which all observable system states satisfy given logical constraints while remaining consistent with executable transition semantics. To answer this, we introduce the Hyper Petri Net (HyPN) approach, which synthesizes Petri nets from Boolean specifications while explicitly distinguishing between observable markings and underlying Petri net execution. The proposed method introduces an explicit execution semantics over observable states, induced by admissible (atomic) firing sequences, ensuring by construction that all observable markings satisfy the constraints and revealing a fundamental mismatch between logical feasibility and executable behavior. This is demonstrated in two scenarios inspired by a lunar rover system. These results are particularly relevant for the design of robotic and autonomous systems, as they provide a structured way to ensure correct system configurations while explicitly accounting for execution constraints. The proposed framework further suggests new research directions in execution abstraction, admissible transition systems, and policy selection for navigating between constraint-satisfying states.

</details>

---

### [[20_Research/Papers/强化学习/Embodying_Multi-Hand_Manipulation_Policies_by_Searching_the_Assignment_and_Null_Spaces|Embodying Multi-Hand Manipulation Policies by Searching the Assignment and Null Spaces]]

![[assets/2607.22020_figure.png|800]]

- **arXiv**: [2607.22020](https://arxiv.org/abs/2607.22020)
- **PDF**: https://arxiv.org/pdf/2607.22020
- **详细分析**: [[20_Research/Papers/强化学习/Embodying_Multi-Hand_Manipulation_Policies_by_Searching_the_Assignment_and_Null_Spaces|Embodying Multi-Hand Manipulation Policies by Searching the Assignment and Null Spaces]]
- **作者**: Yorai Shaoul, Jiaoyang Li, Maxim Likhachev
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Embodying Multi-Hand Manipulation Policies by Searching the Assignment and Null Spaces》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned manipulation policies increasingly predict motions for abstract "hands" and are attractive in practice because they rely on easily collected demonstrations and transfer across robot platforms. Executing these trajectories on multi-arm robots, however, is not trivial. Multi-hand policy outputs must be assigned to physical arms, each arm must realize a configuration-space motion that tracks its prescribed end-effector trajectory, and all arms must respect kinematic limits and avoid collisions. In the absence of algorithms that directly address this problem, practitioners typically extend single-arm inverse-kinematics (IK) pipelines in an ad hoc way, with no guarantees of feasibility or safety. In this work, we close this execution gap with a search-based framework that is theoretically complete for grounding policy-generated multi-hand trajectories onto physical multi-arm systems. Building on Conflict-Based Search, our method explicitly searches over both the discrete assignment of trajectories to arms and the continuous Jacobian null spaces of redundant manipulators, using redundancy to avoid inter-arm collisions while tracking the prescribed motions. This unified treatment of assignment and null-space motion yields a practically efficient planner that safely realizes coordinated manipulation-policy outputs on multi-arm robots. See omcbsa.github.io for more.

</details>

---

### [[20_Research/Papers/机器人/Mag4D-SLAM_Dataset_A_Repeated-Traversal_Multi-Modal_4D_Geomagnetic_Dataset_for_Localization_and_Mapping|Mag4D-SLAM Dataset: A Repeated-Traversal Multi-Modal 4D Geomagnetic Dataset for Localization and Mapping]]

![[assets/2607.21986_figure.png|800]]

- **arXiv**: [2607.21986](https://arxiv.org/abs/2607.21986)
- **PDF**: https://arxiv.org/pdf/2607.21986
- **详细分析**: [[20_Research/Papers/机器人/Mag4D-SLAM_Dataset_A_Repeated-Traversal_Multi-Modal_4D_Geomagnetic_Dataset_for_Localization_and_Mapping|Mag4D-SLAM Dataset: A Repeated-Traversal Multi-Modal 4D Geomagnetic Dataset for Localization and Mapping]]
- **作者**: Bibhutibhusan Nayak, Hyoseok Ju, Giseop Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Mag4D-SLAM Dataset: A Repeated-Traversal Multi-Modal 4D Geomagnetic Dataset for Localization and Mapping》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geomagnetic sensing offers an infrastructure-free, absolute orientation reference that is robust to GNSS denial and visual degradation, yet no large-scale outdoor robotics dataset supports its systematic study in SLAM. Existing magnetic datasets are confined to small-scale indoor environments and lack the synchronized multi-modal sensing, repeated-traversal structure, and high-precision 6-DoF ground truth required for geomagnetic SLAM research. We present Mag4D-SLAM, the first large-scale outdoor geomagnetic SLAM dataset. It comprises 14 sequences totaling over 18 km of synchronized LiDAR, camera, IMU, tri-axis magnetometer, and GNSS measurements with SE(3) ground-truth poses, collected along structured campus trajectories under paired day/night conditions in both forward and reverse directions. Through repeated-traversal experiments, we analyze three core properties: magnetic field repeatability across different recording sessions (daytime and nighttime), drift-free global heading estimation, and location-discriminative magnetic signatures for cross-session place recognition. Mag4D-SLAM is designed to support research on yaw drift mitigation, magnetic loop closure, and long-term localization and to open new research questions on how geomagnetic sensing can complement visual and LiDAR modalities or provide a fallback cue under illumination changes, structural repetition, and GNSS-denied long-term operation.

</details>

---

### [[20_Research/Papers/具身智能/Adaptive_Undulatory_Locomotion_of_Snake-like_Robots_in_Dynamic_Viscous_Environments_via_Deep_Reinforcement_Learning|Adaptive Undulatory Locomotion of Snake-like Robots in Dynamic Viscous Environments via Deep Reinforcement Learning]]

![[assets/2607.21960_figure.png|800]]

- **arXiv**: [2607.21960](https://arxiv.org/abs/2607.21960)
- **PDF**: https://arxiv.org/pdf/2607.21960
- **详细分析**: [[20_Research/Papers/具身智能/Adaptive_Undulatory_Locomotion_of_Snake-like_Robots_in_Dynamic_Viscous_Environments_via_Deep_Reinforcement_Learning|Adaptive Undulatory Locomotion of Snake-like Robots in Dynamic Viscous Environments via Deep Reinforcement Learning]]
- **作者**: Tsuyoshi Kimoto, Akio Yamano, Kohei Honda, Takashi Iwasa
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 大模型
- **相关性评分**: 3.7（加权：具身智能 1.5，大模型 0.1，强化学习 1.8，机器人 0.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Adaptive Undulatory Locomotion of Snake-like Robots in Dynamic Viscous Environments via Deep Reinforcement Learning》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper demonstrates how deep reinforcement learning (DRL) enables adaptive locomotion of snake-like robots in dynamically changing viscous environments, overcoming the inherent performance limitations of classical predefined control methods. The lack of direct onboard sensors for fluid properties necessitates formulating this task as a partially observable Markov decision process. By employing an asymmetric actor-critic framework, a teacher policy trained using privileged information available only in the physics simulator distills its knowledge into a student policy that relies solely on proprioceptive sensor information. Simulation results across a wide range of dynamic viscosity changes ($10^{-7}$ to $10^{-2} m^2/s$) reveal that the DRL agent autonomously acquires non-sinusoidal adaptive gaits. These gaits improve propulsion velocity and transport efficiency, breaking the inherent limits of conventional sinusoidal and kinematic control. The findings establish that implicit environment inference via privileged information distillation is an effective approach to bypass the constraints of classical models under unpredictable fluid dynamics.

</details>

---

### [[20_Research/Papers/具身智能/Action-Conditioned_World_Model_for_Goal_Plane_Probe_Guidance_in_Robotic_Ultrasound|Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound]]

![[assets/2607.21918_figure.png|800]]

- **arXiv**: [2607.21918](https://arxiv.org/abs/2607.21918)
- **PDF**: https://arxiv.org/pdf/2607.21918
- **详细分析**: [[20_Research/Papers/具身智能/Action-Conditioned_World_Model_for_Goal_Plane_Probe_Guidance_in_Robotic_Ultrasound|Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound]]
- **作者**: Siqi Fan, Mingcong Chen, Ran Liu, Zixuan Yang, Xiaoyu Fu, Xiaoqing Gao, Yunhui Liu, Hongbin Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Action-Conditioned World Model for Goal Plane Probe Guidance in Robotic Ultrasound》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EchoWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present an action-conditioned world model framework for goal plane probe guidance in robotic ultrasound, with a focus on neck ultrasound scanning. Autonomous ultrasound tasks often require large numbers of probe-motion trajectories for training, but collecting high-quality demonstrations is labor-intensive and explicit simulators are difficult to build because ultrasound appearance depends on contact, tissue deformation, and view-dependent acoustic artifacts. We address this problem with a two-stage model-based learning pipeline. First, a latent conditional diffusion world model predicts future ultrasound observations from recent context frames, probe motions and temporal offset. Second, a goal-conditioned temporal transformer predicts ordered probe motions and is fine-tuned using rewards from the frozen world model. Experiments on the self-collected dataset show that the world model preserves action-dependent anatomical structure on target-directed scans. In real-world closed loop experiments, the framework achieves success rates of 70.0\% for carotid guidance and 65.0\% for thyroid guidance. These results demonstrate the potential of learned ultrasound dynamics for training goal-directed robotic probe navigation.

</details>

---

### [[20_Research/Papers/具身智能/Addressing_the_Orchestration_Gap_in_Generalist_Robots_via_Physical_Agency|Addressing the Orchestration Gap in Generalist Robots via Physical Agency]]

![[assets/2607.21725_figure.png|800]]

- **arXiv**: [2607.21725](https://arxiv.org/abs/2607.21725)
- **PDF**: https://arxiv.org/pdf/2607.21725
- **详细分析**: [[20_Research/Papers/具身智能/Addressing_the_Orchestration_Gap_in_Generalist_Robots_via_Physical_Agency|Addressing the Orchestration Gap in Generalist Robots via Physical Agency]]
- **作者**: Liane Galanti, Dhruv Shah, Tri Dao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Addressing the Orchestration Gap in Generalist Robots via Physical Agency》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robots need to reason about their actions, combining perception, world knowledge, planning, success detection, recovery, and low-level control. Today's state-of-the-art models attempt to combine all these capabilities into the learned policy via large-scale pre-training. Instead, we show that these capabilities can be decomposed into a general language-conditioned policy/control agent and a high-level agent manager/orchestrator. Rather than training policies to reason via pre-training, we build a closed-loop physical agent orchestrator that can do high-level planning, decompose the goal into achievable subgoals, command low-level motor commands, track and verify the outcome from low-level observations, and recover from failures. Our Physical Agency orchestrator (Pigey) can control existing vision-language-action (VLA) policies as well as parametrized skills to solve complex reasoning tasks in the real world, without any additional data collection or post-training. We evaluate Pigey extensively across simulation benchmarks and challenging real-world robotic manipulation tasks, and demonstrate significant performance improvements over existing generalist policies. On LIBERO-PRO, Pigey advances the state-of-the-art by over 4x (12.8% -&gt; 53.3%) with no task-specific fine-tuning. On a real robot, Pigey lifts the frozen policy from near-zero to over 90% on reasoning-limited tasks. We call the difference between what frozen motor skills achieve alone and inside the agentic loop the orchestration gap.

</details>

---

### [[20_Research/Papers/大模型/GRACE_Gradient-Free_Robot_Action_Generation_via_Combined_Diffusion-MPPI_Posterior_Mean_Estimation|GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation]]

![[assets/2607.21661_figure.png|800]]

- **arXiv**: [2607.21661](https://arxiv.org/abs/2607.21661)
- **PDF**: https://arxiv.org/pdf/2607.21661
- **详细分析**: [[20_Research/Papers/大模型/GRACE_Gradient-Free_Robot_Action_Generation_via_Combined_Diffusion-MPPI_Posterior_Mean_Estimation|GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation]]
- **作者**: Leesai Park, Jiho HOng, Sanghyun Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GRACE: Gradient-Free Robot Action Generation via Combined Diffusion-MPPI Posterior Mean Estimation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion policies generate multimodal robot action sequences from demonstrations, but steering them toward deployment-time constraints typically relies on differentiable guidance costs. This excludes many practical safety constraints, such as binary collision checks, joint limits, and black-box rollout costs that are nondifferentiable. We propose Gradient-free Robot Action generation via Combined diffusion-MPPI posterior mean Estimation (GRACE), which guides a pretrained diffusion policy with Model Predictive Path Integral (MPPI) control using only forward cost evaluations. Building on the common score-ascent structure of diffusion and MPPI, GRACE constructs a cost-conditioned guidance posterior at each reverse step and estimates its mean with a single MPPI update centered at the diffusion reverse mean. For differentiable costs, GRACE recovers conventional gradient guidance under a first-order, matched-covariance approximation. GRACE attains higher success rates than diffusion-based and sampling-based baselines in simulation. On a real 7-DoF manipulator, GRACE avoids a deployment-time obstacle that the unguided prior collides with in every trial. Code and experiment videos are available at https://anonymous.4open.science/w/grace-70BB/.

</details>

---

### [[20_Research/Papers/机器人/Learning_Diverse_Humanoid_Tasks_via_Synthetic_Video_Scenarios_without_Real_World_Data|Learning Diverse Humanoid Tasks via Synthetic Video Scenarios without Real World Data]]

![[assets/2607.21648_figure.png|800]]

- **arXiv**: [2607.21648](https://arxiv.org/abs/2607.21648)
- **PDF**: https://arxiv.org/pdf/2607.21648
- **详细分析**: [[20_Research/Papers/机器人/Learning_Diverse_Humanoid_Tasks_via_Synthetic_Video_Scenarios_without_Real_World_Data|Learning Diverse Humanoid Tasks via Synthetic Video Scenarios without Real World Data]]
- **作者**: Yun-Hao Tsai, Cong-Thanh Vu, Yen-Chen Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Learning Diverse Humanoid Tasks via Synthetic Video Scenarios without Real World Data》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The human-like morphology of humanoid robots grants them exceptional potential for agile and versatile motor capabilities, but it also introduces significant challenges in acquiring complex skills. Traditional Learning-from-Demonstrations methods are often constrained by the high cost of collecting real-world data, the difficulty of capturing motion-specific behaviors, and the limited diversity of demonstrations across individuals. Moreover, even for the same task, humans may execute the motion in multiple distinct ways. In this paper, we propose a new framework that leverages the power of Generative AI to convert textual prompts into realistic and diverse sequences of human body movements, enabling the robot to observe multiple variations of how a single task can be performed. These synthetic demonstrations are then used as a training resource, allowing the robot to learn a broad range of task-execution styles without requiring direct human intervention. We evaluate the proposed method across four simulation scenarios. Experimental results show that the robot not only completes the tasks successfully but also demonstrates strong adaptability to complex variations in motion.

</details>

---
