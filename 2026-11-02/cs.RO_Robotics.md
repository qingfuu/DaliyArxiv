# cs.RO | Robotics | 2026-11-02

#arxiv #ComputerScience

**论文数**: 39

### [[20_Research/Papers/强化学习/ROOF_Learning_Humanoid_Fall_Recovery_under_Overhead_Constraints|ROOF: Learning Humanoid Fall Recovery under Overhead Constraints]]

![[assets/2610.42097_first_page.png|800]]

- **arXiv**: [2610.42097](https://arxiv.org/abs/2610.42097)
- **PDF**: https://arxiv.org/pdf/2610.42097
- **详细分析**: [[20_Research/Papers/强化学习/ROOF_Learning_Humanoid_Fall_Recovery_under_Overhead_Constraints|ROOF: Learning Humanoid Fall Recovery under Overhead Constraints]]
- **作者**: Yidan Lu, Jiayuan Yu, Zongrui Cai, Jingwen Sun, Jinrui Han, Jing Wang, Ping Luo, Peng Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ROOF: Learning Humanoid Fall Recovery under Overhead Constraints》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FR-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A fallen humanoid beneath an overhead obstacle faces a coupled recovery problem. It must create clearance while organizing support for a stable rise, since attempting to stand before making room can further increase obstruction. We introduce a reinforcement learning method with contact-supported geometric escape guidance, which rewards incremental reduction of robot-obstacle overlap without prescribing an escape path. To achieve this, a learned motion prior, together with posture-dependent support and joint-stall costs, is proposed to shape a single policy that learns when to clear the obstacle, how to establish support, and when to complete the rise, all using proprioception alone. In simulation, it recovers in 88.5% of trials beneath plates that can only be lifted, compared with 18.9% without geometric guidance, and in 98.6% of trials beneath free plates with randomized size, mass and placement. On a Unitree G1, the deployed policy recovered in 95 of 150 attempts across seven real-world obstacle scenes, including furniture and multi-object arrangements absent from training. Project page: https://lu-yidan.github.io/ROOF/

</details>

---

### [[20_Research/Papers/具身智能/A_Hybrid_Path_Planning_Framework_for_Assistive_Wheelchair_Navigation_in_Dynamic_Pedestrian_Environments|A Hybrid Path Planning Framework for Assistive Wheelchair Navigation in Dynamic Pedestrian Environments]]

![[assets/2610.42049_figure.png|800]]

- **arXiv**: [2610.42049](https://arxiv.org/abs/2610.42049)
- **PDF**: https://arxiv.org/pdf/2610.42049
- **详细分析**: [[20_Research/Papers/具身智能/A_Hybrid_Path_Planning_Framework_for_Assistive_Wheelchair_Navigation_in_Dynamic_Pedestrian_Environments|A Hybrid Path Planning Framework for Assistive Wheelchair Navigation in Dynamic Pedestrian Environments]]
- **作者**: Damla Leblebicioğlu, Rachel Barume, Taşkın Padır
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《A Hybrid Path Planning Framework for Assistive Wheelchair Navigation in Dynamic Pedestrian Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous wheelchairs can improve the quality of life for individuals with mobility impairments by providing greater independence. However, reliable navigation especially in human environments is a major challenge due to factors such as dynamic obstacles, unpredictable pedestrian behavior, and the users' need to complete multiple stops along the way before reaching their final destination. This paper presents a hybrid path planning framework for multi-goal navigation in dynamic environments. The framework integrates the Traveling Salesman Problem (TSP) for global task ordering with the Potential Field (PF) method and heuristic local planners such as Rapidly-exploring Random Tree (RRT) and A-star (A*) to achieve collision-free navigation. Within this hybrid framework, TSP determines the visiting order of intermediate stations, PF transfers global path information, and local planners avoid obstacles while guiding the robot to the stations. The local planners generate feasible paths that allow the robot to follow the global trajectory and reroute to avoid static and dynamic obstacles. For this purpose, two algorithms have been developed: (i) TSP-PF-RRT and (ii) TSP-PF-A*. The performance of the proposed algorithms are evaluated using Monte Carlo simulations in crowded and extra-crowded scenarios that contain heterogeneous dynamic and static obstacles. Experimental results demonstrate that the proposed hybrid framework enables efficient multi-goal navigation while maintaining safe operation in dynamic environments with humans, with TSP-PF-RRT achieving fewer or no collisions and shorter travel distances.

</details>

---

### [[20_Research/Papers/具身智能/Nexus-VLA_Bridging_Human_and_Robot_Experiences_via_a_Shared_Hierarchical_Semantic_Latent_Space|Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space]]

![[assets/2610.42021_figure.png|800]]

- **arXiv**: [2610.42021](https://arxiv.org/abs/2610.42021)
- **PDF**: https://arxiv.org/pdf/2610.42021
- **详细分析**: [[20_Research/Papers/具身智能/Nexus-VLA_Bridging_Human_and_Robot_Experiences_via_a_Shared_Hierarchical_Semantic_Latent_Space|Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space]]
- **作者**: Biaoliang Guan, Tingyu Yuan, Wen Ye, Ziming Ji, Xu Yang, Yan Huang, Jihua Zhu, Chaoyang Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Nexus-VLA: Bridging Human and Robot Experiences via a Shared Hierarchical Semantic Latent Space》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Nexus-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale egocentric human videos provide rich and scalable manipulation experience for robot policy learning, yet substantial embodiment gaps in visual appearance, kinematic structure, and action spaces hinder effective knowledge transfer. Existing methods often decouple cross-embodiment knowledge alignment from robot policy learning, making it difficult for human manipulation knowledge to directly and fully contribute to robot action learning. To address this issue, we propose Nexus-VLA, a hybrid policy learning framework that enables cross-embodiment knowledge transfer through end-to-end human-robot joint training, allowing human manipulation experience to directly contribute to robot policy learning. We first introduce a hierarchical cross-embodiment semantic alignment paradigm that progressively establishes shared manipulation semantics from task intent to fine-grained interactions, enabling more complete use of the manipulation knowledge contained in human videos. Building on this hierarchy, we design a shared manipulation latent representation that jointly encodes multi-level shared knowledge into an internal representation directly used for continuous action generation, improving policy learning efficiency while effectively leveraging human knowledge. Across RoboCasa-GR1, OOD settings, and real-world robot experiments, Nexus-VLA achieves an 80.5% task success rate on RoboCasa-GR1 and demonstrates strong advantages in human-data utilization, learning efficiency, and cross-scenario generalization.

</details>

---

### [[20_Research/Papers/具身智能/Suspended-Fabric_Robotic_Manipulation_Surfaces_Modelling,_Design_Space,_and_Multimodular_Extensio|Suspended-Fabric Robotic Manipulation Surfaces: Modelling, Design Space, and Multimodular Extensio]]

![[assets/2610.41982_figure.png|800]]

- **arXiv**: [2610.41982](https://arxiv.org/abs/2610.41982)
- **PDF**: https://arxiv.org/pdf/2610.41982
- **详细分析**: [[20_Research/Papers/具身智能/Suspended-Fabric_Robotic_Manipulation_Surfaces_Modelling,_Design_Space,_and_Multimodular_Extensio|Suspended-Fabric Robotic Manipulation Surfaces: Modelling, Design Space, and Multimodular Extensio]]
- **作者**: Pratik Ingle, Jørn Lambertsen, Kasper Støy, Andres Faiña
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Suspended-Fabric Robotic Manipulation Surfaces: Modelling, Design Space, and Multimodular Extensio》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic Manipulation Surfaces (RMS) reposition objects by deforming the surface on which they rest. A recent class of RMS suspends a continuous fabric sheet from a sparse grid of vertical linear actuators lowering the actuator density of such surfaces but how to design such surfaces so that objects can be controlled everywhere on it, and how to extend it beyond a single module so that objects can pass between modules and achieve parallel, remain open. This paper presents a separable catenary model of the suspended sheet that is fast to compute and provides both the surface shape for given actuator heights and the actuator heights for a desired local slope. The closed form inverse lets a simple PID controller position objects on the sheet, and the model relates fabric length, module span and actuator stroke to the reachable workspace, yielding a minimum fabric length bound and design charts for these surfaces. The approach is then extended to a multimodular platform in which neighbouring modules share actuators. On a $2 \times 2$ prototype, we demonstrate that centimetre-scale objects are transferred between modules and positioned within 0.03 m over a $1 m^2$ workspace with only nine actuators, enabling multi-object manipulation and opening the way to parallel manipulation.

</details>

---

### [[20_Research/Papers/强化学习/Design_and_Validation_of_a_Robotic_Knee_Exoskeleton_with_Musculoskeletal_Simulation-Derived_Biological_Torque_Control|Design and Validation of a Robotic Knee Exoskeleton with Musculoskeletal Simulation-Derived Biological Torque Control]]

![[assets/2610.41981_figure.png|800]]

- **arXiv**: [2610.41981](https://arxiv.org/abs/2610.41981)
- **PDF**: https://arxiv.org/pdf/2610.41981
- **详细分析**: [[20_Research/Papers/强化学习/Design_and_Validation_of_a_Robotic_Knee_Exoskeleton_with_Musculoskeletal_Simulation-Derived_Biological_Torque_Control|Design and Validation of a Robotic Knee Exoskeleton with Musculoskeletal Simulation-Derived Biological Torque Control]]
- **作者**: Rajiv V. Joshi, Jimin An, Ilseung Park, Dawit Lee, Inseung Kang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Design and Validation of a Robotic Knee Exoskeleton with Musculoskeletal Simulation-Derived Biological Torque Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data-driven controllers have enabled lower-limb robotic exoskeletons to adapt assistance to the user across many tasks. A leading example is biological torque control, which estimates the user's own joint moment from onboard sensors and assists in proportion to that estimate. However, its estimators are trained on data recorded with the target device, so deploying the controller on new hardware requires collecting new data. Existing open-source efforts release hardware, software, or controllers separately, so this data collection must still be repeated on the assembled device. Here, we present an open-source knee exoskeleton, built from off-the-shelf components and widely available fabrication tools, with a biological torque controller derived entirely from simulation. A muscle-driven imitation policy reproduces squatting motions from an open biomechanics dataset, and the resulting knee moments are distilled into an estimator that uses only onboard sensors, so no training data are recorded on the device. In seven able-bodied participants, assistance reduced peak biological knee extension moment by 21.5% and peak vastus medialis activation by 26.7% during squatting, relative to squatting without the exoskeleton (p&lt;0.05). Our results demonstrate that a biological torque controller derived from simulation can transfer to physical hardware without device-specific data collection. Because the hardware and training pipeline are released together, research groups can train and compare knee exoskeleton controllers on shared hardware without additional data collection overhead.

</details>

---

### [[20_Research/Papers/具身智能/Online_Learning_of_Heterogeneous_Locomotion_Dynamics_under_Reinforcement_Learning_Policies_for_Precise_Loco-Manipulation|Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation]]

![[assets/2610.41892_figure.png|800]]

- **arXiv**: [2610.41892](https://arxiv.org/abs/2610.41892)
- **PDF**: https://arxiv.org/pdf/2610.41892
- **详细分析**: [[20_Research/Papers/具身智能/Online_Learning_of_Heterogeneous_Locomotion_Dynamics_under_Reinforcement_Learning_Policies_for_Precise_Loco-Manipulation|Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation]]
- **作者**: Tianlin Zhang, Weipeng Xia, Lingwei Zhang, Yiyang Shao, Zhongyu Li, Yun-Hui Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，强化学习 0.6，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Online Learning of Heterogeneous Locomotion Dynamics under Reinforcement Learning Policies for Precise Loco-Manipulation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How to reuse a pretrained locomotion policy for precise loco-manipulation is still an open problem. We propose an online method to learn the closed-loop dynamics under a frozen locomotion policy. The learned model predicts floating-base motion and improves loco-manipulation accuracy. However, unobserved latent conditions of the policy introduce heterogeneous responses, meaning that the same observed state will lead to different motions. Direct learning without accounting for this heterogeneity introduces bias and fluctuations into dynamics estimates, degrading floating-base prediction and end-effector tracking. To address this problem, a contaminated Gaussian model is proposed to approximate the effects of latent conditions. The model uses two Gaussian components to approximate predictable and unpredictable responses under the same observed state. Then, the contaminated Gaussian model is combined with a Gaussian process to construct an online learner using random Fourier features (RFFs). The learner estimates each response's probability of belonging to the predictable component and uses it to weight online updates, capturing predictable responses while reducing bias and fluctuations caused by heterogeneous observations. With consistent and unbiased dynamics estimates, model predictive control (MPC) predicts floating-base motion accurately and enables precise loco-manipulation. A finite-sample error bound is established to ensure uniform convergence in online learning. Simulation and hardware experiments demonstrate consistent end-effector tracking across different manipulator configurations and tasks, with errors of 0.01 m.

</details>

---

### [[20_Research/Papers/大模型/META-Robot_Self-Cognition_and_Capability_Scaling_in_Agentic_Robots|META-Robot: Self-Cognition and Capability Scaling in Agentic Robots]]

![[assets/2610.41868_figure.png|800]]

- **arXiv**: [2610.41868](https://arxiv.org/abs/2610.41868)
- **PDF**: https://arxiv.org/pdf/2610.41868
- **详细分析**: [[20_Research/Papers/大模型/META-Robot_Self-Cognition_and_Capability_Scaling_in_Agentic_Robots|META-Robot: Self-Cognition and Capability Scaling in Agentic Robots]]
- **作者**: Xuanzhi Feng, Zeyu Liu, Weiheng Gao, Xinchen Li, Jiankun Tang, Fangqi Zhu, Quanxin Shou, Hao Chen, Zhengyang Yan, Hualei Zhang, Junhao Li, Zhiyao Wu...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《META-Robot: Self-Cognition and Capability Scaling in Agentic Robots》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based robotic agent systems can generate programs for robot control, yet their generalization to new tasks often depends on elaborate scaffolding. Expanding their skill repertoires alone offers limited guidance on how to assess new capabilities or identify what remains beyond their reach. We introduce META-Robot, a framework that couples self cognition with capability scaling by expanding the criteria through which an agent evaluates and develops its skills. At its core, action-level predicates make execution outcomes explicit and available for LLM reasoning. The agent uses these assessments to identify its own limitations, extend relevant evaluation criteria, and guide the structured expansion of its skills. Proprioceptive feedback further grounds this process in the robot's physical state, enriching the evidence available for self-cognition. Experiments in simulation and on real robots demonstrate stronger overall task performance, generalization to new tasks, continued expansion of skills and evaluation criteria, and effective use of non-visual proprioceptive signals.

</details>

---

### [[20_Research/Papers/强化学习/When_the_Simulator_Fails,_Not_the_Policy_Auditing_Contact_Artifacts_in_Simulated_Robot_Benchmarks|When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks]]

![[assets/2610.41857_figure.png|800]]

- **arXiv**: [2610.41857](https://arxiv.org/abs/2610.41857)
- **PDF**: https://arxiv.org/pdf/2610.41857
- **详细分析**: [[20_Research/Papers/强化学习/When_the_Simulator_Fails,_Not_the_Policy_Auditing_Contact_Artifacts_in_Simulated_Robot_Benchmarks|When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks]]
- **作者**: Alex Zhou, Junhao Wu, Xueyang Zhou, Yixiao Huo, Hongcheng Gao, Di Zhu, Zhenghao Zhang, Yongchao Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《When the Simulator Fails, Not the Policy: Auditing Contact Artifacts in Simulated Robot Benchmarks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HyVLA, RoboEval, SafeVLA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation benchmarks score robot policies by success rate, and every failed episode counts against the policy. Many of these failures are the simulator's fault, not the policy's; we find the cause and fix it. Testing a vision language action model and a world action model in simulation, we find that the policy often places the object and the simulator then ejects it, and that the benchmark's own scripted demonstrations fail the same way. We present SimuGuard, an auditing plugin for LIBERO, RoboTwin, RoboCasa and RoboDojo. It leaves the evaluation unchanged. At every physics step, it records the state and flags an object that starts moving at a contact faster than the robot's contact or gravity account for. It replays a recorded episode bit for bit, and it reruns the episode with one simulation parameter changed. With it we trace these episodes on RoboTwin to the collision detection of the physics engine: for geometry one to two centimeters apart, the engine reports a penetration of about two centimeters, and the solver throws the object out at several meters per second. The cause is one constant: the distance algorithm discards triangles below a fixed area threshold, which valid triangles fall below at the centimeter scale. With that constant changed and nothing else, episodes with an artifact fall from 12 in 100 to none, and the success rate on five container tasks rises from 89% to 98%. Success rates in simulation thus count failures that the simulator causes. Benchmarks on PhysX 5.3.1 or earlier should rerun in a repaired engine. Where the engine cannot change, they should report the success rate together with the range it spans when every flagged episode fails or passes: 75.8% to 98.5% around a reported 83.1% for LingBot-VA.

</details>

---

### [[20_Research/Papers/具身智能/SketchMate_Agentic_Geometric_Reasoning_for_Zero-Shot_Precision_Insertion|SketchMate: Agentic Geometric Reasoning for Zero-Shot Precision Insertion]]

![[assets/2610.41844_figure.png|800]]

- **arXiv**: [2610.41844](https://arxiv.org/abs/2610.41844)
- **PDF**: https://arxiv.org/pdf/2610.41844
- **详细分析**: [[20_Research/Papers/具身智能/SketchMate_Agentic_Geometric_Reasoning_for_Zero-Shot_Precision_Insertion|SketchMate: Agentic Geometric Reasoning for Zero-Shot Precision Insertion]]
- **作者**: Jiaming Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SketchMate: Agentic Geometric Reasoning for Zero-Shot Precision Insertion》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inserting an unseen part requires sub-millimetre precision and the correct orientation of keyed features. Current zero-shot agentic manipulation methods built on vision-language models (VLMs) produce spatial outputs that are far too coarse for this. We propose to let a VLM build a sketch model of the task, i.e., a few geometric primitives and two mate frames, which a VLM agent measures with geometric tools in multi-view depth and which a standard planner and compliant controller execute. Because a sketch describes the parts independently of their placement, the robot needs to build it only once per task. A sketch memory stores each agent run and transfers the stored sketch to later placements by point-cloud registration, so that the VLM is called only for unfamiliar parts. After grasping the part, the robot inspects both mating faces at close range and corrects the sketch by shape matching. On 69 simulated insertion episodes, our method inserts 88% of the parts at the assembled pose in a strict kinematic test, while ReKep and MOKA with the same VLM insert none. On new placements of eight tasks, reusing one stored run inserts as many parts as calling the agent in each episode, and it produces the sketch in 3.4 s instead of about 90 s.

</details>

---

### [[20_Research/Papers/强化学习/Integrating_Low-Thrust_Transfer_Dynamics_into_POMDP_Planning_for_On-Orbit_Servicing|Integrating Low-Thrust Transfer Dynamics into POMDP Planning for On-Orbit Servicing]]

![[assets/2610.41839_first_page.png|800]]

- **arXiv**: [2610.41839](https://arxiv.org/abs/2610.41839)
- **PDF**: https://arxiv.org/pdf/2610.41839
- **详细分析**: [[20_Research/Papers/强化学习/Integrating_Low-Thrust_Transfer_Dynamics_into_POMDP_Planning_for_On-Orbit_Servicing|Integrating Low-Thrust Transfer Dynamics into POMDP Planning for On-Orbit Servicing]]
- **作者**: Susmitha Patnala, Vincent Mousseau, Adam Abdin
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Integrating Low-Thrust Transfer Dynamics into POMDP Planning for On-Orbit Servicing》归入 强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent developments in both high-thrust (HT) and low-thrust (LT) propulsion technologies broaden design options for on-orbit servicing (OOS) missions. However, incorporating LT transfers into OOS mission planning requires accounting for the trade-off between prescribed transfer duration and propellant consumption. Multi-servicing, multi-transfer OOS mission planning is inherently sequential and requires adaptive planning tools that account for propulsion-dependent transfer durations and mass-dependent propellant consumption. Thus, transfer dynamics must be integrated into mission planning and scheduling to increase flexibility and adaptability. In addition, the planning is often done with imperfect information about the system's state and stochastic service demands. This paper focuses on modeling orbital transfers, particularly LT transfers, within a Partially Observable Markov Decision Process (POMDP) framework for OOS mission planning. To enable offline policy computation, the transfer model must provide explicit state transitions and rewards for all admissible actions. The state space is therefore augmented with the servicing vehicle's remaining propellant to enable consistent mass updates. HT transfers are modeled using a precomputed transfer matrix that maps each transfer to the time of flight and propellant consumed. LT transfers are represented using an analytical GEO phasing model with prescribed transfer-duration alternatives. For each alternative, the model calculates propellant consumption and maneuver feasibility as functions of the required phase change and the current servicing-vehicle mass. The proposed modeling approach is evaluated on simplified OOS planning scenarios using circular phasing with HT and LT propulsion. The resulting POMDPs are solved using the Successive Approximations of the Reachable Space under Optimal Policies (SARSOP) algorithm, and the policies obtained under HT and LT are compared. This comparison provides a quantitative assessment of the feasibility and operational impact of LT options, particularly regarding the potential role of advanced electric propulsion in future servicing architectures.

</details>

---

### [[20_Research/Papers/机器人/Visual-Inertial_RGB-D_SLAM_with_Encoders_for_a_Differential_Wheeled_Robot|Visual-Inertial RGB-D SLAM with Encoders for a Differential Wheeled Robot]]

![[assets/2610.41768_first_page.png|800]]

- **arXiv**: [2610.41768](https://arxiv.org/abs/2610.41768)
- **PDF**: https://arxiv.org/pdf/2610.41768
- **详细分析**: [[20_Research/Papers/机器人/Visual-Inertial_RGB-D_SLAM_with_Encoders_for_a_Differential_Wheeled_Robot|Visual-Inertial RGB-D SLAM with Encoders for a Differential Wheeled Robot]]
- **作者**: Zhanghao Zhu, Yutaka Kaizu, Kenichi Furuhashi, Kenji Imou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Visual-Inertial RGB-D SLAM with Encoders for a Differential Wheeled Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent years have seen multiple impressive results in visual-inertial odometry (VIO) techniques, by which accurate state estimation can be achieved via the extended Kalman filter (EKF) or nonlinear optimization. However, these approaches are rarely open source, and they tend to fail in real experiments due to the temporary lack of feature points and fast motion. Therefore, in this study, we used encoders to overcome the temporary failure of purely vision-based simultaneous localization and mapping (SLAM). Here, we propose a generative measurement model for encoders and derive an expression for the maximum a posteriori (MAP) estimate and necessary Jacobians for optimization. We use our theory to present a novel tightly coupled visual-inertial encoder RGB-Depth (RGB-D) SLAM system. Tests on our system on an in-house dataset confirmed that our modeling effort led to accurate (with a root mean squared error (RMSE) of approximately 2-7 cm) and robust state estimation in real time. The source code and our dataset containing the encoder information have been published for verification.

</details>

---

### [[20_Research/Papers/具身智能/Flexibility-Aware_Robotic_Manipulation_Deformation_Estimation,_Kinematics,_and_Control_via_Distributed_Inertial_Measurement|Flexibility-Aware Robotic Manipulation: Deformation Estimation, Kinematics, and Control via Distributed Inertial Measurement]]

![[assets/2610.41702_figure.png|800]]

- **arXiv**: [2610.41702](https://arxiv.org/abs/2610.41702)
- **PDF**: https://arxiv.org/pdf/2610.41702
- **详细分析**: [[20_Research/Papers/具身智能/Flexibility-Aware_Robotic_Manipulation_Deformation_Estimation,_Kinematics,_and_Control_via_Distributed_Inertial_Measurement|Flexibility-Aware Robotic Manipulation: Deformation Estimation, Kinematics, and Control via Distributed Inertial Measurement]]
- **作者**: Amir Hossein Barjini, Sadeq Yaqubi, Pauli Mustalahti, Jouni Mattila
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Flexibility-Aware Robotic Manipulation: Deformation Estimation, Kinematics, and Control via Distributed Inertial Measurement》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flexible robot links challenge the rigid-body assumption, making joint measurements alone insufficient for accurate manipulation. This paper introduces a flexibility-aware manipulation framework that connects structural dynamics directly to sensing, kinematics, and control. Instead of prescribing a dense inertial measurement unit (IMU) network, the dominant vibration modes of each flexible link are first identified from response-convergence and excitation-bandwidth criteria. Under a full-rank modal observability condition, $m$ retained modes require only $m$ independent slope measurements and one reference IMU, defining the minimum observable IMU configuration. The resulting measurements are used to reconstruct the continuous link deformation, which is then incorporated into flexibility-aware forward kinematics and a deformation-informed partial differential equation-based controller. Experiments on hydraulic single- and double-link manipulators evaluate the framework. On the long-reach double-link platform, the proposed kinematics achieves end-effector root mean square errors of $0.0107$~m, $0.0194$~m, and $0.0102$~rad while using fewer sensors than the piecewise-rigid method. Closed-loop reaching experiments further demonstrate real-time integration of IMU-estimated joint states and reconstructed deformation into the proposed controller. The results show that dominant modal information can determine sensing requirements and enable real-time flexibility-aware robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Interaction-Aware_Sampling-Based_Motion_Planning_for_Autonomous_Surface_Vessels_in_Urban_Waterways|Interaction-Aware Sampling-Based Motion Planning for Autonomous Surface Vessels in Urban Waterways]]

![[assets/2610.41676_figure.png|800]]

- **arXiv**: [2610.41676](https://arxiv.org/abs/2610.41676)
- **PDF**: https://arxiv.org/pdf/2610.41676
- **详细分析**: [[20_Research/Papers/机器人/Interaction-Aware_Sampling-Based_Motion_Planning_for_Autonomous_Surface_Vessels_in_Urban_Waterways|Interaction-Aware Sampling-Based Motion Planning for Autonomous Surface Vessels in Urban Waterways]]
- **作者**: Elia Trevisan, Alejandro Gonzalez-Garcia, Jan Swevers, Javier Alonso-Mora
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Interaction-Aware Sampling-Based Motion Planning for Autonomous Surface Vessels in Urban Waterways》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DriveIRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous surface vessels operating in urban waterways must coordinate with other vessels in confined spaces while complying with traffic regulations, often without knowing their intentions. We present a decentralized motion planner based on model predictive path integral control, a sampling-based model predictive control scheme. The planner jointly computes a trajectory for the ego vessel and a prediction of the trajectories of the other vessels, and therefore accounts for their interaction. Traffic regulations are encoded as discontinuous costs, which the sampling-based formulation admits without a smooth approximation. We evaluate the method in maps taken from real sections of Amsterdam's canals, in encounters between two vessels and in scenarios with four interacting vessels. Across 780 randomized runs the method reaches every goal without collisions or deadlocks, and outperforms an optimization-based planner designed for the same domain, as well as a version of the proposed planner that does not account for the interaction. We further validate the planner on two scaled vessel prototypes in an outdoor environment, where planning and localization run onboard at 10 Hz, and head-on and crossing encounters are resolved without collisions or rule violations.

</details>

---

### [[20_Research/Papers/机器人/GPU-accelerated_Incremental_Euclidean_Distance_Transform_for_Online_Motion_Planning_of_Mobile_Robots|GPU-accelerated Incremental Euclidean Distance Transform for Online Motion Planning of Mobile Robots]]

![[assets/2610.41667_figure.png|800]]

- **arXiv**: [2610.41667](https://arxiv.org/abs/2610.41667)
- **PDF**: https://arxiv.org/pdf/2610.41667
- **详细分析**: [[20_Research/Papers/机器人/GPU-accelerated_Incremental_Euclidean_Distance_Transform_for_Online_Motion_Planning_of_Mobile_Robots|GPU-accelerated Incremental Euclidean Distance Transform for Online Motion Planning of Mobile Robots]]
- **作者**: Yizhou Chen, Shupeng Lai, Jinqiang Cui, Biao Wang, Ben M. Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《GPU-accelerated Incremental Euclidean Distance Transform for Online Motion Planning of Mobile Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this letter, we present a volumetric mapping system that effectively calculates Occupancy Grid Maps (OGMs) and Euclidean Distance Transforms (EDTs) with parallel computing. Unlike these mappers for high-precision structural reconstruction, our system incrementally constructs global EDT and outputs high-frequency local distance information for online robot motion planning. The proposed system constructs OGM with massive amount of data from multiple types of sensor inputs. Using GPU programming techniques, the system quickly computes EDT in parallel within local volume. The new observation is continuously integrated into the global EDT using the parallel wavefront algorithm while preserving the historical observations. Experiments with datasets have shown that our proposed approach outperforms existing state-of-the-art robot mapping systems and is particularly suitable for mapping unexplored areas. In its actual implementations on aerial and ground vehicles, the proposed system achieves real-time performance with limited onboard computational resources.

</details>

---

### [[20_Research/Papers/强化学习/ResMerge_Residual_Policy_Learning_and_Merging_for_Continual_Adaptation_of_Pre-trained_Robot_Policies|ResMerge: Residual Policy Learning and Merging for Continual Adaptation of Pre-trained Robot Policies]]

![[assets/2610.41663_figure.png|800]]

- **arXiv**: [2610.41663](https://arxiv.org/abs/2610.41663)
- **PDF**: https://arxiv.org/pdf/2610.41663
- **详细分析**: [[20_Research/Papers/强化学习/ResMerge_Residual_Policy_Learning_and_Merging_for_Continual_Adaptation_of_Pre-trained_Robot_Policies|ResMerge: Residual Policy Learning and Merging for Continual Adaptation of Pre-trained Robot Policies]]
- **作者**: Kefei Zhu, Lingyun Xu, Yue Xin, Xiaoqi Li, Caixin Guo, Xincheng Du, Yuanpei Chen, Yaodong Yang, Hao Dong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ResMerge: Residual Policy Learning and Merging for Continual Adaptation of Pre-trained Robot Policies》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, PackNet, Real-World, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual adaptation to new tasks is essential for robots deployed in the real world, but adapting pre-trained policies remains challenging due to parameter growth and the need for continual demonstration collection. Parameter-Efficient Continual Fine-Tuning (PECFT) isolates task-specific updates, but adapter-per-task designs require demonstrations and grow with the task set. We propose ResMerge, a two-stage framework that learns mergeable residual policies atop a frozen pre-trained policy: residual reinforcement learning (RL) acquires task-specific corrections without additional expert demonstrations during adaptation, and parameter-space merging consolidates compatible residuals to reduce stored parameters. We introduce Residual-Field Consistency (RFC), a simple, bounded, and interpretable metric that assesses compatibility in residual action-field space by comparing correction direction and magnitude. Experiments on LIBERO across two backbones and on a real-world Franka robot show improved continual learning performance over strong PECFT baselines, while selective merging reduces the residual-parameter footprint. Project website: https://resmerge.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/RTPolicy_Real-Time_(32.9_Hz)_Multi-View_Visuomotor_Policy_for_Robotic_Manipulation_on_Edge_Devices|RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices]]

![[assets/2610.41625_figure.png|800]]

- **arXiv**: [2610.41625](https://arxiv.org/abs/2610.41625)
- **PDF**: https://arxiv.org/pdf/2610.41625
- **详细分析**: [[20_Research/Papers/具身智能/RTPolicy_Real-Time_(32.9_Hz)_Multi-View_Visuomotor_Policy_for_Robotic_Manipulation_on_Edge_Devices|RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices]]
- **作者**: Xianbao Hou, Zehao Ni, Yonghao He, Lingfeng Qian, Xin Shi, Hu Su, Wei Sui, Cong Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 1.5，机器人 1.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《RTPolicy: Real-Time (32.9 Hz) Multi-View Visuomotor Policy for Robotic Manipulation on Edge Devices》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low inference latency is critical for closed-loop robotic manipulation, especially under asynchronous inference, where action chunks must be updated promptly to correct accumulated deviations. However, existing visuomotor policies rely on computationally expensive visual backbones, resulting in high inference latency and deployment overhead. In this paper, we propose RTPolicy, a multi-view visuomotor policy that attains accurate manipulation with high inference efficiency. Its core design combines view-aware feature fusion with visual compression to aggregate complementary information across camera views into a compact token representation. The representation conditions a flow-matching action generator with the robot state and flow time, reducing the cost of action generation. Extensive experiments demonstrate that this design reduces the computational cost of visual representation and action generation while preserving visual information required for manipulation. On the RoboTwin~2.0 single-task clean evaluation across 50 tasks, RTPolicy attains a mean success rate of 52.26\%, outperforming the strongest leaderboard baseline $π_0$ (46.4\%). We further evaluate RTPolicy under asynchronous streaming inference on a real bimanual platform, where RTPolicy attains a mean success rate of 72.0\% and sustains real-time inference at 30.35 ms (32.9 Hz) on the RDK S600 and 149.72 ms (6.7 Hz) on the RDK S100, both in INT16. Project Page: https://d-robotics-ai-lab.github.io/RTPolicy.project.

</details>

---

### [[20_Research/Papers/机器人/A_complete_analytical_characterization_of_optimal_collision-free_motion_for_two_robots|A complete analytical characterization of optimal collision-free motion for two robots]]

![[assets/2610.41558_figure.png|800]]

- **arXiv**: [2610.41558](https://arxiv.org/abs/2610.41558)
- **PDF**: https://arxiv.org/pdf/2610.41558
- **详细分析**: [[20_Research/Papers/机器人/A_complete_analytical_characterization_of_optimal_collision-free_motion_for_two_robots|A complete analytical characterization of optimal collision-free motion for two robots]]
- **作者**: Jan Kamm, Antonio Terpin, Raffaello D'Andrea
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《A complete analytical characterization of optimal collision-free motion for two robots》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collision-free motion planning for multi-agent robotic systems remains an active research area because of the complexity of coordinating robot trajectories, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. Importantly, the analytical difficulty of nonconvex collision-avoidance constraints has so far driven the development of exclusively numerical methods. We derive a complete analytical characterization of the optimal trajectories for two robots that start and end at rest, under double-integrator dynamics and a squared-acceleration objective. We prove that these trajectories belong to eight distinct contact families and determine which family applies for each configuration of initial and final positions. We analyze the geometrical properties of the optimal trajectories, provide a numerical algorithm for computing them, and discuss how these insights may improve the performance of existing numerical trajectory optimizers.

</details>

---

### [[20_Research/Papers/机器人/Contact-based_optimization_for_collision-free_motion_planning_for_a_million_robots|Contact-based optimization for collision-free motion planning for a million robots]]

![[assets/2610.41548_figure.png|800]]

- **arXiv**: [2610.41548](https://arxiv.org/abs/2610.41548)
- **PDF**: https://arxiv.org/pdf/2610.41548
- **详细分析**: [[20_Research/Papers/机器人/Contact-based_optimization_for_collision-free_motion_planning_for_a_million_robots|Contact-based optimization for collision-free motion planning for a million robots]]
- **作者**: Jan Kamm, Antonio Terpin, Raffaello D'Andrea
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.1，机器人 1.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Contact-based optimization for collision-free motion planning for a million robots》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent robotic systems have attracted growing interest in recent years, with applications ranging from coordinated drone shows to autonomous operations on land, in the air, and on water. At the planning level, robot motion is often modeled using double-integrator dynamics (with low-level controllers handling the physical dynamics during execution) with a minimum-energy objective subject to collision-avoidance constraints and limits on position, velocity, and acceleration. The complexity of the problem resides in the constraints, which couple the trajectories and make the optimization problem nonconvex. Existing numerical approaches typically discretize and optimize entire trajectories, which becomes expensive for large fleets. We exploit the structure of optimal trajectories by organizing optimization around contacts, at which robots reach the minimum allowed separation. We formulate a coupled algebraic system in contact variables and reconstruct trajectories analytically between contacts. Our algorithm, sequential contact insertion (SCI), starts from unconstrained trajectories, inserts contacts at separation violations, and jointly adjusts their times and states. Numerical experiments demonstrate planning for one million robots in minutes and thousands of robots in fractions of a second. On problems feasible for a fixed-grid sequential convex programming baseline, SCI achieves median speedups of several orders of magnitude at matching solution accuracy.

</details>

---

### [[20_Research/Papers/具身智能/AC-SMPC_Differentiable_Actor--Critic_MPC_with_State_Constraints_for_Safe_and_Fast_Robot_Navigation|AC-SMPC: Differentiable Actor--Critic MPC with State Constraints for Safe and Fast Robot Navigation]]

![[assets/2610.41477_figure.png|800]]

- **arXiv**: [2610.41477](https://arxiv.org/abs/2610.41477)
- **PDF**: https://arxiv.org/pdf/2610.41477
- **详细分析**: [[20_Research/Papers/具身智能/AC-SMPC_Differentiable_Actor--Critic_MPC_with_State_Constraints_for_Safe_and_Fast_Robot_Navigation|AC-SMPC: Differentiable Actor--Critic MPC with State Constraints for Safe and Fast Robot Navigation]]
- **作者**: Chaoran Wu, Jiayu Fan, Qichen Tan, Yuyi Liu, Jin Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《AC-SMPC: Differentiable Actor--Critic MPC with State Constraints for Safe and Fast Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving safe navigation in confined dynamic environments remains a challenging problem, as robots must balance navigation efficiency with safety. Existing actor--critic MPC architectures typically employ differentiable MPC layers, but this way cannot readily accommodate explicit state constraints, making it intractable to involve collision avoidance within learning-based planning. To address this issue, we propose an actor--critic model predictive control framework with state constraints. We first use vertices to represent the robot and obstacles, and half-spaces to represent the workspace. Based on these, the nonlinear robot dynamics is locally linearized and the hyperplane-based collision avoidance constraints are convexified into the differentiable MPC layer, and then the actor exploits closed-loop feedback to adjust the MPC objective parameters that shape local motion behavior, while the critic evaluates long-term task performance. We further relax the convexified constraints with bounded and penalized slack variables to form an elastic quadratic program, accommodating cases where the local constraint approximations cannot be satisfied simultaneously. Simulation tests and experiments, involving dynamic collision avoidance for multi-robot in narrow cases, illustrate the advantages of the proposed framework in adaptively adjusting the learned policy and improving navigation efficiency over existing approaches while maintaining the motion safety.

</details>

---

### [[20_Research/Papers/机器人/SAFARI_Semantic-_And_Frontier-driven_Autonomous_Risk_Inspection|SAFARI: Semantic- And Frontier-driven Autonomous Risk Inspection]]

![[assets/2610.41456_figure.png|800]]

- **arXiv**: [2610.41456](https://arxiv.org/abs/2610.41456)
- **PDF**: https://arxiv.org/pdf/2610.41456
- **详细分析**: [[20_Research/Papers/机器人/SAFARI_Semantic-_And_Frontier-driven_Autonomous_Risk_Inspection|SAFARI: Semantic- And Frontier-driven Autonomous Risk Inspection]]
- **作者**: Ugur Kafkasyali, Mihnea Toader, Julia Richter, Turcan Tuna, Cesar Cadena, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《SAFARI: Semantic- And Frontier-driven Autonomous Risk Inspection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic exploration can reduce human exposure to hazardous environments by autonomously searching unknown areas for objects of interest while constructing a complete, risk-aware map. However, existing autonomous exploration approaches typically prioritize geometric coverage or information gain, without explicitly coupling semantic object detection and the risk associated with operating near potentially hazardous objects. Moreover, many systems have been demonstrated primarily in simulation or controlled environments, leaving limited validation of risk-aware semantic exploration in complex, unstructured field settings. To address this gap, we propose SAFARI, a framework that treats object detection as a native channel of a unified probabilistic map, thereby jointly informing exploration and planning with both geometric and semantic evidence. We evaluated SAFARI in 11 missions across three field sites on a quadruped platform. The framework achieved an average coverage of 98.7% of the accessible mission area, without operator intervention for 97.6% of mission time, and detected objects with characteristic dimensions as small as 15cm. Lastly, through ablation studies and a detailed analysis of system behavior, we show that object-size awareness and safety-aware path planning are crucial for effective hazardous-object search.

</details>

---

### [[20_Research/Papers/机器人/Physically_Constrained_Kinematic_Calibration_for_High-Precision_Robotic_Needle_Guidance|Physically Constrained Kinematic Calibration for High-Precision Robotic Needle Guidance]]

![[assets/2610.41429_figure.png|800]]

- **arXiv**: [2610.41429](https://arxiv.org/abs/2610.41429)
- **PDF**: https://arxiv.org/pdf/2610.41429
- **详细分析**: [[20_Research/Papers/机器人/Physically_Constrained_Kinematic_Calibration_for_High-Precision_Robotic_Needle_Guidance|Physically Constrained Kinematic Calibration for High-Precision Robotic Needle Guidance]]
- **作者**: Prabhu Nithin Gollapudi, Andreas Maier, Franziska Mathis-Ullrich, Water Zhao, Jia Wang, Siming Bayer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Physically Constrained Kinematic Calibration for High-Precision Robotic Needle Guidance》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Percutaneous needle insertion is a common practice in minimally invasive procedures whose clinical success depends on accurate needle placement. However, achieving the necessary precision is a challenge for manual operators. Robotic assistance can improve targeting accuracy and reduce operator dependence, but residual millimeter-scale errors persist because nominal kinematic models do not fully represent the physical manipulator. This paper presents a robust bound-constrained kinematic calibration method designed to improve positional accuracy for a 6-Degree-of-Freedom (6-DoF) robotic needle-guidance manipulator. The approach uses physically plausible parameter ranges to regularize a compact 19-parameter geometric identification model. By treating these bounds as active optimization constraints rather than mere numerical safeguards, the framework effectively mitigates parameter coupling and overfitting, ensuring highly stable parameter identification. In simulation, the proposed method reduced end-effector Root Mean Square Error (RMSE) from 3.422 mm to 0.690 mm (a 79.8% improvement). In benchtop hardware experiments, the calibrated model achieved sub-millimeter validation accuracy, including 0.865 mm RMSE in experimental trajectory validation and 0.610 mm RMSE in a coordinate-lattice verification task. These results demonstrate that physically constrained kinematic calibration can enhance robotic needle-targeting accuracy, establishing a high-precision foundation for future clinical applications.

</details>

---

### [[20_Research/Papers/具身智能/BioAgent_Self-Directed_Skill_Acquisition_and_Capability_Growth_for_Long-Horizon_Laboratory_Protocols|BioAgent: Self-Directed Skill Acquisition and Capability Growth for Long-Horizon Laboratory Protocols]]

![[assets/2610.41383_figure.png|800]]

- **arXiv**: [2610.41383](https://arxiv.org/abs/2610.41383)
- **PDF**: https://arxiv.org/pdf/2610.41383
- **详细分析**: [[20_Research/Papers/具身智能/BioAgent_Self-Directed_Skill_Acquisition_and_Capability_Growth_for_Long-Horizon_Laboratory_Protocols|BioAgent: Self-Directed Skill Acquisition and Capability Growth for Long-Horizon Laboratory Protocols]]
- **作者**: Gaojing Zhang, Changwen Chen, Zichen Luo, Jialiang Li, Yuhan Wang, Yifei Xie, Wenzhao Lian
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《BioAgent: Self-Directed Skill Acquisition and Capability Growth for Long-Horizon Laboratory Protocols》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BioProVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Executing an unfamiliar laboratory protocol requires a robot to identify missing capabilities and determine whether each operation remains valid as the experiment progresses. This letter presents BioAgent, an embodied agent that addresses these coupled challenges of capability sufficiency and experimental validity. It matches human-reviewed requirements to validated skills and task packages, selects tool-based implementations for missing behaviors, and requests human teaching when needed during learning. Learned skills undergo sequential task-package validation to check outcomes and compatibility between successive operations. During execution, precondition, outcome, and experimental-state checks govern progression, autonomous recovery, or termination. Execution evidence guides tool selection, while accepted experience supports offline policy updates and task packaging. On the second task, BioAgent reuses 17 skill types unchanged, revises two existing implementations, and acquires five new types. On two dual-arm laboratory tasks with 20 and 31 ordered skill invocations, BioAgent achieves complete-task success rates of 66\% and 58\% with autonomous recovery over 50 runs per task. Across 25 atomic skills evaluated over 50 autonomous trials each with recovery disabled, success rates range from 84\% to 100\%, with 17 skills achieving 50/50.

</details>

---

### [[20_Research/Papers/具身智能/MolmoSpaces-CommonSense_Evaluating_Commonsense_in_Robotic_Manipulation_Policies|MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies]]

![[assets/2610.41377_figure.png|800]]

- **arXiv**: [2610.41377](https://arxiv.org/abs/2610.41377)
- **PDF**: https://arxiv.org/pdf/2610.41377
- **详细分析**: [[20_Research/Papers/具身智能/MolmoSpaces-CommonSense_Evaluating_Commonsense_in_Robotic_Manipulation_Policies|MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies]]
- **作者**: Arjun Guru, Max Argus, Jae Sung Park, Jiafei Duan, Ali Farhadi, Ranjay Krishna
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《MolmoSpaces-CommonSense: Evaluating Commonsense in Robotic Manipulation Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world robotic manipulation requires reasoning about cluttered scenes, partially observable or hidden objects, and semantically appropriate actions, in addition to low-level execution within those scenes. However, existing simulation benchmarks primarily test the latter and remain dominated by comparatively clean environments with limited clutter and narrowly scoped task structure, leaving many forms of commonsense reasoning untested. We address this by introducing a taxonomy of reasoning processes for robotic manipulation grounded in developmental cognitive science. We operationalize this taxonomy through a new benchmark of robot tasks, MolmoSpaces-CommonSense, that requires reasoning about occlusion, containment, support relations, semantically correct grasp points, spatial affordances, and hidden objects. These evaluations require policies not only to recognize relevant scene structure but also to execute correct actions in them. We evaluate several zero-shot generalist manipulation policies. Across model types and architectures, we observe consistent failures in commonsense reasoning: success rates in cluttered scenes drop by over 50% as distractors increase, policies act on incorrect objects in cluttered settings 30% of the time, and affordance-sensitive grasping remains unreliable even with highly specific language prompts, with correct object part selection happening only about 50% of the time. Further, VLM-based success estimation struggles to reliably evaluate rollouts in these settings, suggesting that the challenge extends beyond control to the broader perception-reasoning-action stack. Our results suggest that existing benchmarks may substantially overestimate zero-shot real-world readiness. Code and policy leaderboard link at https://github.com/allenai/molmospaces.

</details>

---

### [[20_Research/Papers/强化学习/DiffWBC_Unlocking_Steerable_General_Humanoid_Motion_Tracking_via_One-Step_Diffusion_Whole-Body_Control|DiffWBC: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control]]

![[assets/2610.41354_figure.png|800]]

- **arXiv**: [2610.41354](https://arxiv.org/abs/2610.41354)
- **PDF**: https://arxiv.org/pdf/2610.41354
- **详细分析**: [[20_Research/Papers/强化学习/DiffWBC_Unlocking_Steerable_General_Humanoid_Motion_Tracking_via_One-Step_Diffusion_Whole-Body_Control|DiffWBC: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control]]
- **作者**: Yifei Huang, Yazhao Yang, Weijia Li, Zhiheng Ma, Dian Shen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《DiffWBC: Unlocking Steerable General Humanoid Motion Tracking via One-Step Diffusion Whole-Body Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General humanoid motion trackers typically rely on deterministic policies that cannot adapt online without brittle reference editing or costly retraining. We present DiffWBC, shifting whole-body control to a generative paradigm via a one-step diffusion model. By modeling distributions over future trajectories, DiffWBC unifies general tracking, test-time steering, and simulation-free failure discovery within a single controller: (1) Generative general tracking: DiffWBC requires a single forward pass per 50 Hz control step and can be distilled from an RL teacher or trained from scratch via model-based RL, achieving the lowest local tracking error among six general trackers on held-out benchmarks (20.1 mm on BONES) and deploying on a physical Unitree G1. (2) Zero-shot test-time steering: differentiable cost gradients and body-group masks modulate the frozen controller online, substantially outperforming kinematic reference editing (0.84 clean pass at 1.25 m ceiling vs. 0.10) and zero-shot generalizing across hurdles, spatial reaching, actuator faults, and tray balancing. (3) Simulation-free failure discovery: plan dispersion across generation noise effectively identifies physical tracking failures (91% precision in top 2%) without physics simulations; targeted fine-tuning on flagged clips resolves 50% of failure cases. Videos and interactive demonstrations are available at https://diffwbc.github.io/#selfassess.

</details>

---

### [[20_Research/Papers/机器人/Geometry-Aware_Humanoid_Retargeting_via_Manifold_ODEs|Geometry-Aware Humanoid Retargeting via Manifold ODEs]]

![[assets/2610.41349_figure.png|800]]

- **arXiv**: [2610.41349](https://arxiv.org/abs/2610.41349)
- **PDF**: https://arxiv.org/pdf/2610.41349
- **详细分析**: [[20_Research/Papers/机器人/Geometry-Aware_Humanoid_Retargeting_via_Manifold_ODEs|Geometry-Aware Humanoid Retargeting via Manifold ODEs]]
- **作者**: Pengyu Zhu, Heye Wang, Xi Wang, Xuyang Wu, He Kong, Guodong Shi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Geometry-Aware Humanoid Retargeting via Manifold ODEs》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we focus on interaction-preserving motion retargeting, which transfers human demonstrations to humanoids while maintaining spatial relationships with objects and terrain. Previous work, such as OmniRetarget, addresses this task through temporally coupled constrained optimization, requiring repeated sequential quadratic programming (SQP) iterations at each frame. We study this problem from an ordinary differential equation (ODE) perspective by modeling the continuous-time limit of its framewise Karush-Kuhn-Tucker (KKT) conditions as an ODE on the robot configuration manifold. This viewpoint offers two benefits: (i) it connects OmniRetarget's SQP iterations to a backward discretization of the ODE, enabling us to establish their local convergence under suitable regularity assumptions; and (ii) it leads to TaSP-KKT (tangent-space parametrization for KKT flow), a new retargeting method based on a forward discretization of the KKT flow. The proposed method achieves the same first-order convergence to the ODE solution as the corresponding backward scheme while requiring only one weighted tangent-cone projection and a closed-form manifold update per step, thereby avoiding repeated inner SQP iterations. Numerical experiments show that TaSP-KKT achieves retargeting quality comparable to, though slightly lower than, that of OmniRetarget while running approximately twice as fast.

</details>

---

### [[20_Research/Papers/强化学习/HandMimicX_Learning_Human-Like_Dexterous_Manipulation_via_an_Object-Centric_Policy_from_Egocentric_Videos|HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos]]

![[assets/2610.41336_figure.jpg|800]]

- **arXiv**: [2610.41336](https://arxiv.org/abs/2610.41336)
- **PDF**: https://arxiv.org/pdf/2610.41336
- **详细分析**: [[20_Research/Papers/强化学习/HandMimicX_Learning_Human-Like_Dexterous_Manipulation_via_an_Object-Centric_Policy_from_Egocentric_Videos|HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos]]
- **作者**: Zihan Gao, Yufei Liu, Yuhong Zhang, Zhen Yu, Xinhao Huang, Zhinan You, Kai W. Ho, Zipeng Ye, Peng Jiao, Haoqian Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《HandMimicX: Learning Human-Like Dexterous Manipulation via an Object-Centric Policy from Egocentric Videos》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PointNet, Real-World, X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning dexterous manipulation from human videos remains an open challenge, particularly in the context of transferring a single demonstration into a spatially generalizable robotic skill and maintaining physically plausible human-like interactions. Unlike prior works that emphasize hand-motion imitation, we introduce an object-centric framework for acquiring dexterous skills from egocentric human RGB-D videos. Within our framework, we formulate the reinforcement learning (RL) objective in terms of object motion to decouple the underlying skill from the specific hand trajectory and impose constraints on hand-object interaction states to promote more anatomically natural hand configurations. Extensive experiments in simulation and on real robots demonstrate that our method enables efficient learning from human videos and generalizable skill transfer across novel spatial configurations.

</details>

---

### [[20_Research/Papers/机器人/HIPC_Humanoid_Iterative_Planning_and_Control_via_Goal-Conditioned_Motion_Closure|HIPC: Humanoid Iterative Planning and Control via Goal-Conditioned Motion Closure]]

![[assets/2610.41334_figure.png|800]]

- **arXiv**: [2610.41334](https://arxiv.org/abs/2610.41334)
- **PDF**: https://arxiv.org/pdf/2610.41334
- **详细分析**: [[20_Research/Papers/机器人/HIPC_Humanoid_Iterative_Planning_and_Control_via_Goal-Conditioned_Motion_Closure|HIPC: Humanoid Iterative Planning and Control via Goal-Conditioned Motion Closure]]
- **作者**: Yi Han, Xingyu Chen, Zixuan Lang, Qianyang Wu, Yuhang Lin, Ji Ma, Liang Li, Dongting Li, Xinpeng Liu, Ruoli Dai, Hesheng Wang, Renjing Xu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《HIPC: Humanoid Iterative Planning and Control via Goal-Conditioned Motion Closure》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent generative models are widely used to provide whole-body motion for humanoid tracking. Current methods combine motion generators with controllers in an open-loop paradigm, which leads to critical issues: tracking errors can accumulate into spatial drift, and the planner cannot adapt to unexpected physical disturbances without feedback from physical execution. However, directly feeding realized states back to the planner in a closed loop can cause discontinuities, resulting in physical jitter and even falls, since such states are out of distribution during training. To bridge this gap, we propose HIPC, a real-time Humanoid Iterative Planning and Control framework that couples a generative model with motion tracking into a unified planning-and-control paradigm. HIPC introduces a goal-conditioned motion planning trained with a canonical motion representation that avoids gimbal-lock singularities under extreme orientations and supports motion generation on diverse geometric and semantic conditions. Then, HIPC adopts two strategies, deviation-decayed recovery and history re-anchoring, to mitigate the out-of-distribution shift caused by realized-state feedback. Finally, HIPC operates a real-time asynchronous planning-and-control system, with latency compensation to reduce temporal mismatch for inference delay. Extensive experiments confirm the effectiveness of HIPC under switching and composition of diverse conditions. Results show that HIPC achieves state-of-the-art goal-reaching accuracy among existing methods while simultaneously demonstrating robustness to physical perturbations and the ability to recover from falls.

</details>

---

### [[20_Research/Papers/具身智能/Cross-Embodiment_Motion_Planning_by_Coupling_Body-Agnostic_World_Model_with_Differentiable_Ego-Dynamics|Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics]]

![[assets/2610.41330_figure.png|800]]

- **arXiv**: [2610.41330](https://arxiv.org/abs/2610.41330)
- **PDF**: https://arxiv.org/pdf/2610.41330
- **详细分析**: [[20_Research/Papers/具身智能/Cross-Embodiment_Motion_Planning_by_Coupling_Body-Agnostic_World_Model_with_Differentiable_Ego-Dynamics|Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics]]
- **作者**: Zhidong Wang, Zirui Li, Haoran Xu, Yujie Yan, Zitong Shan, Jingsong Liang, Han Yu, Chen Lv
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 3.1（加权：具身智能 0.6，世界模型 1.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Cross-Embodiment Motion Planning by Coupling Body-Agnostic World Model with Differentiable Ego-Dynamics》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion planning in clutter is embodiment-specific: the feasible free space and reachable commands depend on each robot's geometry and dynamics. Existing cross-embodiment policies output normalized commands that disregard these differences, or compensate through per-robot training and distillation. World models can in principle pool cross-embodiment data, yet command-conditioned models bind their latent dynamics to a single action space, while pose-conditioned models omit the mapping from commands to body-specific motion. On flat ground, however, embodiment affects the planner's observations only through the camera ego-motion. This letter proposes Hourglass, an hourglass-shaped architecture that factorizes cross-embodiment motion planning at this interface: a body-agnostic world model and each robot's differentiable ego-dynamics, which map commands to that ego-motion, are coupled only through it. The world model is trained on data pooled across embodiments and camera mounts; each robot's ego-dynamics is a reduced-order template with identified physical parameters. A generalist parameter-conditioned policy is learned once at this junction: each imagined step rolls out the template and then the world model, and imagination training through each robot's template makes the policy body-aware. On seven simulated robots of five locomotion types, the generalist policy outperforms imitation-learning and diffusion-policy baselines on the same world model by 3.8--10.6 percentage points in success rate and matches per-robot specialists without dedicated training, while approaching its parameter-conditioned MPPI teacher within 1.4--2.8 points without an online map. After three minutes of teleoperated driving for identification, the synthetic-data-trained model transfers zero-shot to a real skid-steer robot unseen in training, navigating unseen indoor scenes.

</details>

---

### [[20_Research/Papers/具身智能/Learning_from_Physical_Experience_Context-Space_Adaptation_for_Robotic_Manipulation|Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation]]

![[assets/2610.41320_figure.png|800]]

- **arXiv**: [2610.41320](https://arxiv.org/abs/2610.41320)
- **PDF**: https://arxiv.org/pdf/2610.41320
- **详细分析**: [[20_Research/Papers/具身智能/Learning_from_Physical_Experience_Context-Space_Adaptation_for_Robotic_Manipulation|Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation]]
- **作者**: Yihan Zeng, Yisu Li, Kaixin Huang, Marc WuDunn, Amelia Kovacs, Mikael Harseno, Kimmy Lin, Porter Hunley, Fred Shentu, Philipp Wu, Zhongyu Li, Zike Yan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Learning from Physical Experience:Context-Space Adaptation for Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent multimodal foundation models exhibit strong perception, reasoning, and in-context learning capabilities, but translating these capabilities into physical action remains challenging. Through real-world experiments across diverse manipulation tasks, we find that ChatGPT-6-Astra, a state-of-the-art general-purpose reasoner, can serve as a physically actionable, context-responsive manipulation policy, demonstrating effective fine manipulation and spatial reasoning. Building on these findings, we introduce LEXP, a harness for learning from physical experience through context-space adaptation. LEXP combines task-level planning with an experience module that interprets execution evidence, extracts and retains lessons with applicability conditions, and reuses relevant lessons to generate contextual feedback for subsequent actions. Model weights and the action interface remain fixed throughout. Across 12 real-world manipulation tasks, LEXP achieves $23/36$ successful trials (63.9\%), compared with $19/36$ (52.8\%) with memory alone and $2/36$ (5.6\%) for vanilla Astra. On three tasks, bread transfer, sort trash and toiletries, and retrieve drawer, removing planning reduces success from $7/9$ to $4/9$, while removing retained experience reduces it to $3/9$. Execution traces illustrate feedback-guided corrections and cross-episode reuse of an inspection strategy. Execution analyses illustrate how task structure and experience-derived feedback guide task progression, action correction, and experience reuse. These results support context-space adaptation as a practical mechanism for turning physical interaction into reusable guidance for robotic manipulation.

</details>

---

### [[20_Research/Papers/具身智能/TRACE_Target-State_Risk-Aligned_Conditional_Execution_for_Embodied_Tracking|TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking]]

![[assets/2610.41275_figure.png|800]]

- **arXiv**: [2610.41275](https://arxiv.org/abs/2610.41275)
- **PDF**: https://arxiv.org/pdf/2610.41275
- **详细分析**: [[20_Research/Papers/具身智能/TRACE_Target-State_Risk-Aligned_Conditional_Execution_for_Embodied_Tracking|TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking]]
- **作者**: Mingyang Lyu, Gongce Cao, Yiyang Jia, Lu Jia, Erliang Lin, Yuhao Zhang, Yinqian Sun, Pin Lyu, Feifei Zhao, Bo Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 2.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《TRACE: Target-State Risk-Aligned Conditional Execution for Embodied Tracking》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EVT-Bench, TrackVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied visual tracking requires a robot to follow a language-specified person under occlusion, look-alike distractors, and ambiguous instructions. We show that improving tracking persistence can simultaneously increase safety violations. Using a compact 0.6B vision-language-action (VLA) tracker with a frozen backbone, we update only the planner head with proximal policy optimization (PPO). PPO improves success and following rates across all three EVT-Bench settings, but increases the collision rate on distracted tracking because episodes that previously ended in target loss can instead end in contact. We introduce TRACE, an execution-time target-state risk gate that preserves the learned policy and intervenes selectively. A lightweight risk head processes 84 cues, including candidate boxes, identity margins, a learned range-and-bearing probe, and the policy's commands. When the calibrated risk exceeds a threshold, TRACE rescales the translational component of the next waypoint while leaving yaw unchanged. The executed action is identical to PPO's on more than 98% of steps. In paired evaluations on identical episodes, TRACE reduces the distracted-tracking collision rate by 3.96 percentage points, while further improving success and following rates. Matched slowdown controls without target-state timing do not reproduce this improvement. Concurrent evaluation reproduces a collision reduction of 3.77 points, compared with 0.29 points for identical-arm null pairs, indicating that the effect exceeds evaluation variability. These results show that target-state-aware execution can recover the safety cost of policy post-training with minimal intervention.

</details>

---

### [[20_Research/Papers/具身智能/CONSORT_Uncertainty-Constrained_Multi-Robot_Planning_for_Cooperative_Localization_in_GPS-Denied_Environments|CONSORT: Uncertainty-Constrained Multi-Robot Planning for Cooperative Localization in GPS-Denied Environments]]

![[assets/2610.41235_figure.png|800]]

- **arXiv**: [2610.41235](https://arxiv.org/abs/2610.41235)
- **PDF**: https://arxiv.org/pdf/2610.41235
- **详细分析**: [[20_Research/Papers/具身智能/CONSORT_Uncertainty-Constrained_Multi-Robot_Planning_for_Cooperative_Localization_in_GPS-Denied_Environments|CONSORT: Uncertainty-Constrained Multi-Robot Planning for Cooperative Localization in GPS-Denied Environments]]
- **作者**: Tony Zhang, Ryan Bartholomew, Kalliyan Velasco, Joshua Mangelson, Brady Moon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《CONSORT: Uncertainty-Constrained Multi-Robot Planning for Cooperative Localization in GPS-Denied Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Centralized multi-agent path planning with cooperative localization in GPS-denied environments is generally computationally intractable when formulated in full belief space due to tightly coupled uncertainty dynamics. Prior work typically approximates belief dynamics or restricts inter-agent coupling. This work examines a multi-agent planning problem in which a primary agent must reach a goal in minimum time subject to a chance-constrained collision-avoidance requirement and a terminal bound on localization uncertainty. We obtain a tractable surrogate of the underlying belief-space problem by optimizing over the mean-state trajectories of all agents and propagating covariance for terminal constraint evaluation only. We propose CONSORT (Cooperative Navigation with Support-Optimized Routing and Trajectories), a discrete-to-continuous pipeline combining hexagonal-grid joint search with spline-based trajectory refinement. Across 50 randomized scenarios, the planners separate as the terminal uncertainty bound tightens, with CONSORT solving 80% of scenarios where the strongest baseline solves 54%, at comparable path length. In marine simulations, with the plans executed under feedback control on an independently developed factor-graph estimate, the trajectories remain collision-free and their terminal uncertainty falls within 6% of the planner's prediction.

</details>

---

### [[20_Research/Papers/具身智能/Capability-Conditioned_Graph_Control_Barrier_Functions_for_Zero-Shot_Safe_Navigation_of_Heterogeneous_Mobile_Robot_Teams|Capability-Conditioned Graph Control Barrier Functions for Zero-Shot Safe Navigation of Heterogeneous Mobile Robot Teams]]

![[assets/2610.41214_figure.png|800]]

- **arXiv**: [2610.41214](https://arxiv.org/abs/2610.41214)
- **PDF**: https://arxiv.org/pdf/2610.41214
- **详细分析**: [[20_Research/Papers/具身智能/Capability-Conditioned_Graph_Control_Barrier_Functions_for_Zero-Shot_Safe_Navigation_of_Heterogeneous_Mobile_Robot_Teams|Capability-Conditioned Graph Control Barrier Functions for Zero-Shot Safe Navigation of Heterogeneous Mobile Robot Teams]]
- **作者**: Joonkyung Kim, Janghyun Cho, Jeehyun Lee, Changjoo Nam, Yiwei Lyu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Capability-Conditioned Graph Control Barrier Functions for Zero-Shot Safe Navigation of Heterogeneous Mobile Robot Teams》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot systems are increasingly deployed as heterogeneous fleets with diverse kinematic and actuation capabilities. While graph control barrier function (GCBF) methods provide a scalable framework for decentralized safe control, existing approaches typically assume homogeneous robot dynamics. Methods that directly encode robot classes can distinguish known types, but do not represent state-dependent motion capabilities or naturally transfer to unseen robot models. To address this challenge, we propose the Capability-Conditioned Heterogeneous Graph Control Barrier Function (CC-HGCBF), defined in a shared second-order reference-point operational space. This formulation provides a common geometric representation of safety across heterogeneous robots while retaining their model-specific dynamics and admissible control constraints. To enable zero-shot transfer, we introduce the Radial Capability Field (RCF), a compact, fixed-dimensional representation of each robot's state-dependent finite-horizon reachable velocity set. Conditioning the shared graph barrier and decentralized policy on the RCF enables them to adapt to changes in robot state, kinematic constraints, and control limits without relying on predefined robot identities. We jointly train the barrier and policy using proactive safety labeling and neural CBF-QP supervision, and evaluate them on mixed teams containing both seen and unseen robot models. Experiments demonstrate scalable safe coordination and zero-shot transfer to robot models and capability variations withheld during training. Physical-robot experiments further demonstrate zero-shot deployment to unseen kinematic models without retraining.

</details>

---

### [[20_Research/Papers/具身智能/A_Capability-Aware_Backup-Recoverability_Filter_for_Heterogeneous_Multi-Robot_Navigation|A Capability-Aware Backup-Recoverability Filter for Heterogeneous Multi-Robot Navigation]]

![[assets/2610.41188_figure.png|800]]

- **arXiv**: [2610.41188](https://arxiv.org/abs/2610.41188)
- **PDF**: https://arxiv.org/pdf/2610.41188
- **详细分析**: [[20_Research/Papers/具身智能/A_Capability-Aware_Backup-Recoverability_Filter_for_Heterogeneous_Multi-Robot_Navigation|A Capability-Aware Backup-Recoverability Filter for Heterogeneous Multi-Robot Navigation]]
- **作者**: Joonkyung Kim, Yanze Zhang, Wenhao Luo, Yiwei Lyu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《A Capability-Aware Backup-Recoverability Filter for Heterogeneous Multi-Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe navigation in heterogeneous multi-robot teams faces two coupled challenges: differences in robots' braking and turning capabilities limit how each robot can respond to an approaching neighbor, while simultaneous interactions require a single control action to satisfy multiple collision-avoidance constraints. Together, these challenges can make local safety constraints incompatible with a robot's admissible controls, leaving a decentralized safety controller without a feasible action. We propose a Capability-Aware Backup-Recoverability Filter (CA-BRF), based on the insight that navigation actions should preserve access to a certified recovery maneuver. First, we construct a backup-recoverable set in a shared Cartesian operational space by evaluating whether prescribed backup maneuvers maintain pairwise safety until the robots come to rest. Each maneuver respects the corresponding robot's kinematic and actuation constraints, making the recovery certificate capability-dependent. Second, CA-BRF filters candidate controls by selecting admissible interpolations between candidate and backup actions while coordinating the selection across simultaneous interactions. This preserves backup recoverability while retaining as much of the candidate action as possible and ensures that all pairwise recovery conditions are satisfied by a single executable control for each robot. Together, we establish recursive feasibility and safety for the discrete-time closed-loop system even when the nominal safety-constrained optimization becomes infeasible. The validity and effectiveness of the proposed CA-BRF are validated in simulations with up to 30 heterogeneous robots and experiments of robots with five different kinematic classes.

</details>

---

### [[20_Research/Papers/机器人/Veloxity_Towards_Memory-Safe_UAV_Embedded_Firmware_using_the_Rust_Programming_Language|Veloxity: Towards Memory-Safe UAV Embedded Firmware using the Rust Programming Language]]

![[assets/2610.41053_figure.png|800]]

- **arXiv**: [2610.41053](https://arxiv.org/abs/2610.41053)
- **PDF**: https://arxiv.org/pdf/2610.41053
- **详细分析**: [[20_Research/Papers/机器人/Veloxity_Towards_Memory-Safe_UAV_Embedded_Firmware_using_the_Rust_Programming_Language|Veloxity: Towards Memory-Safe UAV Embedded Firmware using the Rust Programming Language]]
- **作者**: Derek Ward, Brian Bascom, Tyler Larsen, James Usevitch, Phil Tokumaru, Tim McLain
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Veloxity: Towards Memory-Safe UAV Embedded Firmware using the Rust Programming Language》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent years have witnessed increased momentum towards memory-safe programming languages for safety-critical systems. Memory-safe languages can eliminate entire classes of common software errors that have historically required extensive analysis and expenditure to avoid. Nevertheless, memory-safe language adoption in aerospace remains fragmented and incomplete, particularly for unmanned aerial vehicles (UAVs). Recent Rust UAV projects either run only in simulation, are closed source, or have not been integrated with an established autonomy ecosystem and tested against existing C/C++ firmware. To address this gap, we present Veloxity: an open-source embedded UAV autopilot written in the memory-safe Rust programming language. Veloxity lowers the barrier to using memory-safe languages within modern ecosystems by providing a minimal, modular foundation for autonomous UAVs. We compare Veloxity to equivalent autopilots written in C++ in simulation, with hardware testbenches, and via outdoor waypoint-following flight tests, demonstrating functional parity with improved performance. These results indicate that modern memory-safe languages are a viable option for reliable and performant firmware for autonomous aerospace systems.

</details>

---

### [[20_Research/Papers/强化学习/Contact_Imitation_Interface_Transferring_Dexterous_Skills_by_Showing_How_Contact_Unfolds|Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds]]

![[assets/2610.41028_figure.png|800]]

- **arXiv**: [2610.41028](https://arxiv.org/abs/2610.41028)
- **PDF**: https://arxiv.org/pdf/2610.41028
- **详细分析**: [[20_Research/Papers/强化学习/Contact_Imitation_Interface_Transferring_Dexterous_Skills_by_Showing_How_Contact_Unfolds|Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds]]
- **作者**: Zhixuan Xu, Yichen Li, Bingchen Wu, Rui Wang, Yiwen Hou, Zixuan Liu, Tianyu Qiu, Lin Shao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Contact Imitation Interface: Transferring Dexterous Skills by Showing How Contact Unfolds》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-free human demonstrations offer a promising route to scaling dexterous manipulation data. The key challenge is to preserve the demonstrator's natural dexterity while producing contact-grounded observations and actions that transfer to robot hands. We present Contact Imitation Interface (CIMI), a framework with contact-grounded demonstration and learning interfaces. The demonstration interface combines shared contact geometry and fingertip RGB views with contact-alignment-first retargeting and reprojection of wider scene views. The learning interface introduces a hierarchical policy in which a contact-surface planner predicts relative contact-surface trajectories and a controller coordinates wrist and finger commands to improve contact alignment. CIMI combines contact-grounded observations, retargeting, and action representations, improving mean final-stage success by at least 50 percentage points over baseline policies across six hand-task pairs on LEAP and Wuji. Hardware designs and software are publicly available.

</details>

---

### [[20_Research/Papers/机器人/CuPIQP_A_Batched_and_Differentiable_QP_Solver_on_GPUs_for_Robot_Learning_and_Control|CuPIQP: A Batched and Differentiable QP Solver on GPUs for Robot Learning and Control]]

![[assets/2610.41021_first_page.png|800]]

- **arXiv**: [2610.41021](https://arxiv.org/abs/2610.41021)
- **PDF**: https://arxiv.org/pdf/2610.41021
- **详细分析**: [[20_Research/Papers/机器人/CuPIQP_A_Batched_and_Differentiable_QP_Solver_on_GPUs_for_Robot_Learning_and_Control|CuPIQP: A Batched and Differentiable QP Solver on GPUs for Robot Learning and Control]]
- **作者**: Fenglong Song, Roland Schwan, Yuwen Chen, Yuning Jiang, Colin N. Jones
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《CuPIQP: A Batched and Differentiable QP Solver on GPUs for Robot Learning and Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadratic programs (QPs) are fundamental building blocks of many robotic tasks such as inverse kinematics, whole-body control, and model predictive control. Extending these methods to large-scale robot learning and control requires solving many QPs concurrently and, for end-to-end learning, differentiating through their solutions. Efficient batched optimization is therefore essential to bringing established model-based methods into GPU-based robotics pipelines. We present \textsc{cuPIQP}, a batched and differentiable QP solver on GPUs based on a proximal interior-point method, with unified support for dense, sparse, and multistage problems. The solver exploits parallelism across independent QPs and their internal structure while preserving per-problem numerical updates and termination decisions. Benchmarks with up to 16384 QPs per batch demonstrate solve-time speedups of up to $18.8\times$ over \textsc{Moreau} and $4.26\times$ over eight-core \textsc{PIQP}. In an end-to-end learning task, \textsc{cuPIQP} accelerates training by $4.6\times$ over \textsc{QPAX} and $7.8\times$ over \textsc{Moreau}. By reducing the computational cost, \textsc{cuPIQP} provides efficient, reusable infrastructure for integrating model-based optimization into large-scale robot learning and control.

</details>

---

### [[20_Research/Papers/强化学习/FlapSim_A_Composable_MuJoCo_Simulation_Platform_and_Reduced-Order_Aerodynamic_Model_Hierarchy_for_Flapping-Wing_Robotics|FlapSim: A Composable MuJoCo Simulation Platform and Reduced-Order Aerodynamic Model Hierarchy for Flapping-Wing Robotics]]

![[assets/2610.40902_first_page.png|800]]

- **arXiv**: [2610.40902](https://arxiv.org/abs/2610.40902)
- **PDF**: https://arxiv.org/pdf/2610.40902
- **详细分析**: [[20_Research/Papers/强化学习/FlapSim_A_Composable_MuJoCo_Simulation_Platform_and_Reduced-Order_Aerodynamic_Model_Hierarchy_for_Flapping-Wing_Robotics|FlapSim: A Composable MuJoCo Simulation Platform and Reduced-Order Aerodynamic Model Hierarchy for Flapping-Wing Robotics]]
- **作者**: Mingshan He
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《FlapSim: A Composable MuJoCo Simulation Platform and Reduced-Order Aerodynamic Model Hierarchy for Flapping-Wing Robotics》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FlapSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flapping-wing simulation must reconcile high-frequency wingbeat aerodynamics with the slower dynamics relevant to flight control and reinforcement learning. We present FlapSim, a modular open-source MuJoCo simulation platform that combines robot descriptions, wing geometry, and composable aerodynamic models in a deterministic simulation pipeline. Across $48$ held-out scenarios spanning frequency, gimbal, wind, frequency-step, gust, and cross-robot flat-plate regimes, we compare five reduced-order configurations operating at $1\,\text{ms}$ with a $50\,μ\text{s}$ quasi-steady blade-element reference. The built-in hover cycle-averaged baseline achieves a $67.51\times$ CPU speedup but only $0.6593$ mean wrench fidelity. Combining multirate $21$-substep clock synchronization, three-dimensional linear/quadratic inflow and gust coupling, analytical blade-element geometry scaling, and phase-locked $1f\text{--}6f$ harmonics raises mean fidelity to $0.9646$ at a $65.19\times$ speedup in a five-block model. A streamlined four-block model without explicit step-transient lag states achieves $0.9662$ fidelity at a $67.98\times$ speedup. Controlled ablations show that stroke harmonics are particularly important during frequency transitions, improving held-out frequency-step fidelity by $+0.3176$. Transfer-function analysis explains this effect: fixed-window cycle averaging retains harmonic contributions when the wingbeat frequency changes, so within-cycle reconstruction also improves the filtered wrench. Once phase alignment and harmonic synthesis are included, explicit transient lag states provide no additional benefit in this benchmark. These results characterize the accuracy--computation tradeoff of the aerodynamic hierarchy and identify timing, inflow, geometry, and harmonic representation as central considerations for reduced-order flapping-wing simulation.

</details>

---

### [[20_Research/Papers/具身智能/CaPtain_A_Pipeline_for_Post-Training_Code-as-Policy_Robot_Agents|CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents]]

![[assets/2610.40799_figure.png|800]]

- **arXiv**: [2610.40799](https://arxiv.org/abs/2610.40799)
- **PDF**: https://arxiv.org/pdf/2610.40799
- **详细分析**: [[20_Research/Papers/具身智能/CaPtain_A_Pipeline_for_Post-Training_Code-as-Policy_Robot_Agents|CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents]]
- **作者**: Yijia Fan, Xilin He, Yilei Jiang, Dongming Wu, Jiaxu Wang, Xiangyu Yue
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.2，大模型 0.6，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CaPtain: A Pipeline for Post-Training Code-as-Policy Robot Agents》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgenticRoboRL, CaP-Bench, OpenVLA, RIPT-VLA, SFT-and-RL, SWEET-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Across coding, web, and tool-use tasks, language-model agents are now routinely trained with the same recipe: supervised fine-tuning (SFT) to learn the interface, then multi-turn reinforcement learning (RL) to master it. Code-as-policy (CaP) casts robot manipulation in the same form, as the policy writes code against robot APIs and reads back the results, so the same recipe should apply. Yet existing CaP agents sidestep training: they either prompt closed frontier models or delegate manipulation to pre-trained vision-language-action models (VLAs) and high-level skills, while small open vision-language models (VLMs) fail outright. We present CaPtain, an open post-training pipeline that turns a small open VLM into a capable CaP agent, with no VLA, frontier model, or privileged state at test time. CaPtain trains and deploys the policy inside CaPtain-Harness, which exposes low-level perception, geometry, and guarded-motion primitives across simulation and real hardware. We first align the base model via SFT on synthetic trajectories generated with GPT-6 Astra, then apply multi-turn RL. Multi-turn RL must credit tens of agent requests, whose physical effects often surface turns later, from a single end-of-episode outcome. We therefore introduce a physical critic that reads privileged simulator state, never seen by the policy, and credits each request by how much it changes the predicted chance of success. Starting from Qwen3.5-4B (0% zero-shot), CaPtain-4B reaches 55.4% held-out LIBERO success after SFT and 73.8% after RL. On LIBERO-PRO, it reaches 78.5%, surpassing several frontier-model agents, and its RL gains persist across three perturbation suites (+17.6 to +21.2 points). Without target-domain training, it attains 83.3% on SimplerEnv WidowX, exceeds frontier models on CaP-Bench, and runs on a real robot after simulation-only adaptation. We release all code, data, and model weights.

</details>

---

### [[20_Research/Papers/具身智能/WorldBridge_Bridging_Video_and_Action_for_Task_Generalization_in_World_Action_Models|WorldBridge: Bridging Video and Action for Task Generalization in World Action Models]]

![[assets/2610.40748_figure.png|800]]

- **arXiv**: [2610.40748](https://arxiv.org/abs/2610.40748)
- **PDF**: https://arxiv.org/pdf/2610.40748
- **详细分析**: [[20_Research/Papers/具身智能/WorldBridge_Bridging_Video_and_Action_for_Task_Generalization_in_World_Action_Models|WorldBridge: Bridging Video and Action for Task Generalization in World Action Models]]
- **作者**: Jun Cen, Yubo Guo, Hao Li, Liangkai Li, Yaoxu Lyu, Meng Wei, Zeqi Xiao, Sizhe Yang, Yuqiang Yang, Yifan Ye, Shanghang Zhang, Duo Zheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《WorldBridge: Bridging Video and Action for Task Generalization in World Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving the broad task generalization of embodied models in physical environments remains a central challenge in robot learning. We study this challenge in World Action Models (WAMs) through two complementary capabilities: video generalization, which predicts the visual evolution of new tasks, and action generalization, which translates these predictions into executable behavior through a video-to-action bridge. By varying video and action supervision for tasks outside an initial training set, we examine their respective contributions to task transfer. On RoboTwin 2.0, using only in-distribution video-action supervision yields a 25.07% success rate on out-of-distribution tasks. Introducing videos of these tasks without their action labels raises success to 55.90%, while adding just one action-labeled demonstration per task further improves it to 70.70%. These findings suggest that broader video coverage enables task transfer by leveraging existing inverse-dynamics capabilities, while even sparse action supervision further strengthens those capabilities. Guided by this perspective, we introduce WorldBridge, a WAM with separate video and action experts connected through structured attention and trained with joint flow matching. WorldBridge incorporates visual memory at two temporal scales and action forcing, alongside a unified data processing pipeline that standardizes and filters heterogeneous robot trajectories and egocentric hand-derived supervision. Across multiple manipulation benchmarks, WorldBridge achieves state-of-the-art performance among the compared methods, including 96.23% on RoboTwin 2.0 full data setting and 80.9% on clean to random setting, 82.8% on RoboCasa GR1 TableTop, and 57.6% on DOMINO Level-1. Our study highlights the complementary roles of video prediction and action grounding in developing robots that generalize across tasks.

</details>

---
