# cs.RO | Robotics | 2026-07-13

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/具身智能/B-spline_Policy_Accelerating_Manipulation_Policies_via_B-spline_Action_Representations|B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations]]

![[assets/2607.09648_figure.png|800]]

- **arXiv**: [2607.09648](https://arxiv.org/abs/2607.09648)
- **PDF**: https://arxiv.org/pdf/2607.09648
- **详细分析**: [[20_Research/Papers/具身智能/B-spline_Policy_Accelerating_Manipulation_Policies_via_B-spline_Action_Representations|B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations]]
- **作者**: Xiaoshen Han, Haoyu Xiong, Haonan Chen, Chaoqi Liu, Antonio Torralba, Yuke Zhu, Yilun Du
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《B-spline Policy: Accelerating Manipulation Policies via B-spline Action Representations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we present B-spline Policy (BSP), an action representation designed for accelerating robot manipulation policies. Rather than predicting discrete-time action chunks, BSP parameterizes actions as continuous B-spline curves defined by a set of knots and control points. This representation yields smooth, time-continuous trajectories that can be temporally scaled and executed by low-level controllers at higher frequencies and speeds. We show that B-spline-parameterized actions can be seamlessly integrated into standard policy learning pipelines by directly predicting B-spline parameters. Experiments on simulated and real-world tasks demonstrate that BSP significantly reduces task completion time, achieving substantial improvements over baseline methods while maintaining strong success rates. More results: https://b-spline-policy.github.io

</details>

---

### [[20_Research/Papers/强化学习/CoDiMAD_Diffusion-Based_Privileged_Distillation_for_Communication-Free_Multi-Robot_Coordination|CoDiMAD: Diffusion-Based Privileged Distillation for Communication-Free Multi-Robot Coordination]]

![[assets/2607.09587_figure.png|800]]

- **arXiv**: [2607.09587](https://arxiv.org/abs/2607.09587)
- **PDF**: https://arxiv.org/pdf/2607.09587
- **详细分析**: [[20_Research/Papers/强化学习/CoDiMAD_Diffusion-Based_Privileged_Distillation_for_Communication-Free_Multi-Robot_Coordination|CoDiMAD: Diffusion-Based Privileged Distillation for Communication-Free Multi-Robot Coordination]]
- **作者**: Jiyue Tao, Shunheng Xin, Tongsheng Shen, Dexin Zhao, Feitian Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《CoDiMAD: Diffusion-Based Privileged Distillation for Communication-Free Multi-Robot Coordination》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decentralized multi-robot coordination under partial observability remains challenging, especially in communication-free settings where agents must act solely from local sensor observations. Privileged policy distillation provides a promising approach by transferring knowledge from a globally informed oracle to sensor-constrained students. However, in multi-agent systems, the same local observation may correspond to multiple global configurations requiring qualitatively different cooperative actions, making the conditional action distribution inherently multi-modal. Standard deterministic distillation collapses these modes to their mean, often yielding invalid or hesitant actions. To address this issue, we propose CoDiMAD, a three-stage framework that trains a privileged oracle with MAPPO, constructs an offline dataset of local-observation-oracle-action pairs, and distills the oracle into decentralized students parameterized as conditional denoising diffusion probabilistic models. By approximating the conditional oracle-action distribution through the diffusion reverse process, CoDiMAD samples decisive actions from coherent coordination modes rather than averaging across them. Theoretical analysis characterizes the mode-averaging failure of deterministic distillation and the distributional recovery property of diffusion-based distillation. Experiments on three cooperative tasks show that CoDiMAD consistently outperforms direct local MARL and deterministic distillation baselines. The source code will be made publicly available upon acceptance.

</details>

---

### [[20_Research/Papers/强化学习/CORAL-AUV_CFD_Oriented_Reinforcement_Learning_for_Autonomous_Underwater_Vehicles|CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles]]

![[assets/2607.09557_figure.png|800]]

- **arXiv**: [2607.09557](https://arxiv.org/abs/2607.09557)
- **PDF**: https://arxiv.org/pdf/2607.09557
- **详细分析**: [[20_Research/Papers/强化学习/CORAL-AUV_CFD_Oriented_Reinforcement_Learning_for_Autonomous_Underwater_Vehicles|CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles]]
- **作者**: Steven Roche, Milo Van Mooy, Nathan McGuire, Levi Cai, Jonathan P. How, Yogesh Girdhar
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.6，强化学习 0.8，机器人 0.3）
- **关联关键词**: RL

#### 研究背景与动机

《CORAL-AUV: CFD Oriented Reinforcement Learning for Autonomous Underwater Vehicles》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FishGym, IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine grain control and positioning of autonomous underwater vehicles (AUVs) is critical for sampling, maintenance, and survey applications. Traditional control methods for AUVs are labor intensive and are not robust to changes in the vehicle configuration or environmental conditions. Reinforcement learning (RL) promises rapid controller development while handling a range of deployment parameters via domain randomization (DR). However, DR is still limited by the capacity of the underlying simulation to model real physics. In particular, drag physics are difficult to model and are a large contributor to sim-to-real gaps. Meanwhile, computational fluid dynamics (CFD) provides high fidelity drag models but is challenging to leverage within reinforcement learning frameworks due to its computational overhead. Thus, in this paper we exploit the idea of training surrogate approximations of CFD models of a given vehicle, enabling fast inference within RL pipelines. We are the first to successfully deploy a zero-shot RL policy on a 6-DOF AUV in which policy training is performed on surrogate drag models (SDMs) trained on CFD data. We find 31% lower energy usage compared to a controller using simplified physics while traversing between waypoints 11% faster with 19% less error. Our SDM based RL controller better predicts zero-shot transfer and is more robust across reward shaping design choices. When using DR to complete a task with perturbed parameters, we find that the CFD policy is the only controller that successfully transfers. The policies are evaluated in a controlled tank environment and in the field providing extensive testing of the policies' capabilities.

</details>

---

### [[20_Research/Papers/强化学习/DemoBridge_A_Simulation-in-the-Loop_Toolkit_for_Single-View_Human_Demonstration_Retargeting|DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting]]

![[assets/2607.09519_figure.png|800]]

- **arXiv**: [2607.09519](https://arxiv.org/abs/2607.09519)
- **PDF**: https://arxiv.org/pdf/2607.09519
- **详细分析**: [[20_Research/Papers/强化学习/DemoBridge_A_Simulation-in-the-Loop_Toolkit_for_Single-View_Human_Demonstration_Retargeting|DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting]]
- **作者**: Zehao Wang, Fabien Despinoy, Sergey Zakharov, Tinne Tuytelaars, Rahaf Aljundi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《DemoBridge: A Simulation-in-the-Loop Toolkit for Single-View Human Demonstration Retargeting》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present DemoBridge, an toolkit that turns a single-view RGB stereo recording of a human hand demonstration into an executable, physics-validated robot-arm trajectory. Retargeting across the embodiment gap is hard. A robot arm reaches a target with a long, articulated body whose links carry far more collision volume than a hand. Solving inverse kinematics for the mapped end-effector pose often yields no collision-free solution, and a trajectory imposes this at every waypoint. A single view adds noise, leaving the demonstrated reference inaccurate. At the core of DemoBridge is a single collision-aware planner. It optimizes the whole joint trajectory at once, reasoning jointly over alternative grasp poses, whole-arm and grasped-object collision, and fidelity to the demonstrated path. A physics simulator runs in the loop. It validates each phase as it is produced and backtracks on failure, so a demonstration that cannot be reproduced as given is re-planned rather than discarded. The resulting action sequence is dynamically stable and faithful to the demonstrated manipulation. It also doubles as a ready-to-use simulation rollout for policy learning. Grasp timing is inferred automatically, and the perception backends, robot, and pipeline stages are swappable from configuration. We evaluate whole-pipeline retargeting on three real-demonstration tasks and the planner on a controlled synthetic benchmark. Our code is available at https://gitlab.kuleuven.be/u0123974/demo-bridge/ .

</details>

---

### [[20_Research/Papers/具身智能/One-Shot_Multimodal_Learning_from_Demonstration_with_Force-Constrained_Elastic_Maps|One-Shot Multimodal Learning from Demonstration with Force-Constrained Elastic Maps]]

![[assets/2607.09515_first_page.png|800]]

- **arXiv**: [2607.09515](https://arxiv.org/abs/2607.09515)
- **PDF**: https://arxiv.org/pdf/2607.09515
- **详细分析**: [[20_Research/Papers/具身智能/One-Shot_Multimodal_Learning_from_Demonstration_with_Force-Constrained_Elastic_Maps|One-Shot Multimodal Learning from Demonstration with Force-Constrained Elastic Maps]]
- **作者**: Brendan Hertel, Jonathan Spanos, Navya Garg, Reza Azadeh
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《One-Shot Multimodal Learning from Demonstration with Force-Constrained Elastic Maps》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation tasks often require simultaneous reasoning over motion and contact forces, yet most Learning from Demonstration (LfD) methods model only spatial trajectories and neglect force interactions with the environment. This limitation reduces robustness and can lead to unsafe or inconsistent task reproduction in force-constrained settings. We propose a novel one-shot multimodal LfD framework for the segmentation, encoding, and reproduction of force-inclusive demonstrations. First, we introduce a multimodal probabilistic segmentation method that adaptively weighs spatial and force modalities over time, enabling the automatic extraction of force-aware motion primitives. Second, we extend the elastic maps representation to incorporate external force constraints during skill encoding and formulate a convex optimization procedure for learning force-consistent trajectory models. The resulting skills reproduce both motion and contact characteristics from a single demonstration while promoting safer execution by accounting for demonstrated force profiles. We validate our approach on five real-world manipulation tasks across two distinct force-sensing configurations: wrist force sensing on a UR5e with a Robotiq 2f-85 gripper and finger force sensing on a Kinova Gen3 with an Openhand Model O gripper. Experimental results demonstrate robust multimodal segmentation, accurate force-aware reproduction, and cross-platform generality.

</details>

---

### [[20_Research/Papers/具身智能/PhysV2A_Reachability-Gated_and_Semantic-Mask-Constrained_Feasibility_Completion_for_Video-to-Robot_Manipulation|PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation]]

![[assets/2607.09365_figure.png|800]]

- **arXiv**: [2607.09365](https://arxiv.org/abs/2607.09365)
- **PDF**: https://arxiv.org/pdf/2607.09365
- **详细分析**: [[20_Research/Papers/具身智能/PhysV2A_Reachability-Gated_and_Semantic-Mask-Constrained_Feasibility_Completion_for_Video-to-Robot_Manipulation|PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation]]
- **作者**: Haohui Huang, Junda Duan, Tao Teng, Chenguang Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《PhysV2A: Reachability-Gated and Semantic-Mask-Constrained Feasibility Completion for Video-to-Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video-based manipulation provides object-centric motion priors from human demonstrations, generated videos, or RGB-D observations, but such priors are typically embodiment-agnostic and cannot be directly executed by a specific robot. This paper presents \textbf{PhysV2A}, a reachability-gated and semantic-mask-constrained feasibility-completion framework for converting video-derived 6D object motion into robot-executable manipulation trajectories. The key idea is to treat grasp feasibility as trajectory-conditioned rather than local: each RGB-D-generated 6-DoF grasp candidate is rigidly coupled with the recovered object motion to form a grasp-conditioned TCP trajectory hypothesis. PhysV2A then performs hierarchical reachability-gated selection, where infeasible grasp--trajectory pairs are rejected by robot-centric kinematic checks and surviving candidates are ranked by downstream execution suitability. For the selected reachable trajectory, a VLM-assisted and rule-validated S-Mask identifies task-critical and relaxable Cartesian components, enabling semantic-mask-constrained manipulability refinement through redundancy-first optimization and bounded Cartesian relaxation. Real-robot experiments on four tabletop manipulation tasks show that PhysV2A improves task success over representative video-prior and IK-only baselines, reduces kinematic-feasibility failures, and produces better-conditioned trajectories with bounded semantic deviations.

</details>

---

### [[20_Research/Papers/具身智能/Effects_of_Robotic_Touch_on_Older_Users_During_Walking_Guidance_by_a_Humanoid_Robot|Effects of Robotic Touch on Older Users During Walking Guidance by a Humanoid Robot]]

![[assets/2607.09323_figure.png|800]]

- **arXiv**: [2607.09323](https://arxiv.org/abs/2607.09323)
- **PDF**: https://arxiv.org/pdf/2607.09323
- **详细分析**: [[20_Research/Papers/具身智能/Effects_of_Robotic_Touch_on_Older_Users_During_Walking_Guidance_by_a_Humanoid_Robot|Effects of Robotic Touch on Older Users During Walking Guidance by a Humanoid Robot]]
- **作者**: Leonie Leven, Marko Ackermann, Christian Werner, Melina Schmetterer, Theresa Buchner, Monika Eckstein, Katja Mombaur
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.8（加权：具身智能 1.2，大模型 0.1，机器人 2.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Effects of Robotic Touch on Older Users During Walking Guidance by a Humanoid Robot》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The shortage of healthcare staff is a challenge in geriatric care. To address this, robots can be integrated into care settings to provide assistance and emotional support. A promising application is walking guidance, particularly benefiting older adults as navigation skills deteriorate with aging. As walking guidance involves direct contact, the aim of this study is to understand how older adults perceive and respond to different touch modes during guided walking. 24 older adults (68 - 88 yrs.) walked four times a ten-meter trajectory guided by the robot TIAGo Pro in four contact conditions: no physical contact (NC); physical contact through holding the robot's wrist with the hand (HH); physical interaction through linking arms with the robot (LA); and physical contact through resting the forearm on the robots forearm (FC). A multimodal assessment approach included electrocardiogram, electrodermal activity, contact force, distance to robot, and questionnaires. Physiological results reveal a slight increase in stress levels during robot interaction. Behavioural and subjective measures, however, show overall acceptance of robotic touch. The two conditions corresponding to larger interaction forces (HH and FC) were associated with lower relative distances between participant and robot, indicating a higher trust and confidence. Questionnaire responses supported these findings, evidencing greater perceived safety, trust and comfort in these conditions. This study provides insights for the design of robotic walking guidance assistance, indicating that gentle, stable touch is preferred by older adults in comparison to contactless interaction.

</details>

---

### [[20_Research/Papers/具身智能/Differential_Analysis_of_Multispectral_Images_for_Terrain_Identification|Differential Analysis of Multispectral Images for Terrain Identification]]

![[assets/2607.09319_figure.png|800]]

- **arXiv**: [2607.09319](https://arxiv.org/abs/2607.09319)
- **PDF**: https://arxiv.org/pdf/2607.09319
- **详细分析**: [[20_Research/Papers/具身智能/Differential_Analysis_of_Multispectral_Images_for_Terrain_Identification|Differential Analysis of Multispectral Images for Terrain Identification]]
- **作者**: Omar Kashmar, Hemendra Arya, Fulvio Mastrogiovanni
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Differential Analysis of Multispectral Images for Terrain Identification》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FuseNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable terrain understanding is a prerequisite for autonomous robot navigation. Yet, the widespread RGB-based perception can fail under low illumination, shadows, and material ambiguities. In this work we propose DRIFT, a lightweight multispectral framework that combines raw spectral bands and illumination-tolerant band-ratio representations through a dual-stream residual architecture and a differential fusion branch. Band ratios attenuate multiplicative acquisition effects (illumination/sensor gains), while the differential fusion explicitly highlights discrepancies between absolute-band and ratio-derived cues, which improves the robustness to noisy or partially unreliable spectral measurements. In the paper (i) we evaluate DRIFT on a new oil-on-soil multispectral dataset acquired using a MicaSense RedEdge-P camera mounted on an Unmanned Aerial Vehicle, and (ii) we provide an additional controlled study on water-on-grass under varying illumination and thermal perturbations (hot/cold water) to analyze NIR-sensitive effects. DRIFT consistently improves over strong baselines, while remaining compatible with edge deployment.

</details>

---

### [[20_Research/Papers/具身智能/Robot_Trajectron_V3_A_Probabilistic_Shared_Control_Framework_for_SE(3)_Manipulation|Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation]]

![[assets/2607.09315_figure.png|800]]

- **arXiv**: [2607.09315](https://arxiv.org/abs/2607.09315)
- **PDF**: https://arxiv.org/pdf/2607.09315
- **详细分析**: [[20_Research/Papers/具身智能/Robot_Trajectron_V3_A_Probabilistic_Shared_Control_Framework_for_SE(3)_Manipulation|Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation]]
- **作者**: Pinhao Song, Zhongxi Li, Ze Fu, Federico Ulloa Rios, Renaud Detry
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Robot Trajectron V3: A Probabilistic Shared Control Framework for SE(3) Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IRL, PointNet, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We aim to address the challenge of teleoperating robotic arms for high-degree-of-freedom (high-DoF) manipulation tasks, which is cognitively demanding and error-prone, particularly when relying on low-bandwidth interfaces. We propose Robot Trajectron V3 (RT-V3), a probabilistic shared control framework designed for $SE(3)$ grasping tasks. RT-V3 formulates shared control as Bayesian inference by learning a prior over user intent and combining it with real-time user commands to estimate the posterior intent distribution. The prior models user intent as a distribution over future trajectories conditioned on past robot dynamics and visual scene context. The intent prior is parameterized by a transformer-based conditional generative model that reasons over point clouds and candidate grasp poses, together with a factorized translation-rotation representation that improves learning efficiency in high-dimensional action spaces. During execution, RT-V3 continuously estimates the posterior distribution over future trajectories by combining the learned intent prior with a user-command likelihood derived from the observed control input, enabling continuous intent refinement and shared assistance. Comprehensive experiments demonstrate that RT-V3 achieves high accuracy in trajectory prediction and competitive performance in reactive planning. Furthermore, real-world user studies indicate that RT-V3 significantly outperforms baseline methods in terms of success rate and efficiency, while substantially reducing the user's physical and mental workload.

</details>

---

### [[20_Research/Papers/具身智能/Validating_Virtual_Reality_for_Studying_Multimodal_Human-Robot_Interaction_in_Socially_Aware_Robot_Navigation|Validating Virtual Reality for Studying Multimodal Human-Robot Interaction in Socially Aware Robot Navigation]]

![[assets/2607.09261_figure.png|800]]

- **arXiv**: [2607.09261](https://arxiv.org/abs/2607.09261)
- **PDF**: https://arxiv.org/pdf/2607.09261
- **详细分析**: [[20_Research/Papers/具身智能/Validating_Virtual_Reality_for_Studying_Multimodal_Human-Robot_Interaction_in_Socially_Aware_Robot_Navigation|Validating Virtual Reality for Studying Multimodal Human-Robot Interaction in Socially Aware Robot Navigation]]
- **作者**: Hariharan Arunachalam, Phani Teja Singamaneni, Rachid Alami
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.5，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Validating Virtual Reality for Studying Multimodal Human-Robot Interaction in Socially Aware Robot Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HuNavSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Virtual Reality (VR) offers a flexible and controllable platform for studying human-robot interaction. Prior work has explored VR for socially aware robot navigation. However, whether VR captures the multimodal interaction dynamics observed in real-world human-robot co-navigation remains insufficiently understood. In this work, we present a VR prototype and evaluate its suitability for studying multimodal human-robot interaction (HRI) in socially aware navigation. Specifically, we investigate whether VR preserves the multimodal interaction dynamics observed in real-world human-robot co-navigation. We conducted a within-subjects study (N = 21) in which participants interacted with a PR2 mobile manipulator robot in both a motion capture equipped arena and its virtual replica in an immersive VR environment. Two common co-navigation scenarios were examined : orthogonal crossing and pass-by interactions. Participants evaluated the robot's perceived social awareness and interaction comfort, while trajectory and head-orientation data were analysed to examine behavioral responses during the interaction. Our results show that participants perceive the robot's socially aware navigation similarly in VR and in the real world. Furthermore, VR captures human interaction behaviors in ways consistent with real-world observations. These findings suggest that VR can be a reliable and flexible platform for studying richer multimodal behaviors in social navigation and HRI.

</details>

---

### [[20_Research/Papers/机器人/Implicit-Behavior_Coordination_from_Unlabeled_Sub-Task_Demonstrations_for_Rearrangement_Tasks|Implicit-Behavior Coordination from Unlabeled Sub-Task Demonstrations for Rearrangement Tasks]]

![[assets/2607.09234_figure.jpg|800]]

- **arXiv**: [2607.09234](https://arxiv.org/abs/2607.09234)
- **PDF**: https://arxiv.org/pdf/2607.09234
- **详细分析**: [[20_Research/Papers/机器人/Implicit-Behavior_Coordination_from_Unlabeled_Sub-Task_Demonstrations_for_Rearrangement_Tasks|Implicit-Behavior Coordination from Unlabeled Sub-Task Demonstrations for Rearrangement Tasks]]
- **作者**: Ahmed Shokry, Usama Ahmed Siddiquie, Sicong Pan, Maren Bennewitz
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Implicit-Behavior Coordination from Unlabeled Sub-Task Demonstrations for Rearrangement Tasks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robotic rearrangement tasks are often treated as skill sequencing problems, requiring predefined skills, skill labels, or boundaries, and task-specific switching logic. Although effective, such explicit skill abstractions can become difficult to scale as the number of behaviors and the task horizon increase. We instead formulate rearrangement as implicit-behavior coordination from unlabeled sub-task demonstrations, where skill-like behaviors are learned directly from mixed behavior data and coordinated through value-guided action selection. Experiments in Habitat rearrangement tasks support this formulation in three ways. First, our method outperforms task-specific imitation baselines on more complex rearrangement tasks and approaches an oracle-planner baseline with behavior-cloned skills, while using no oracle task plan or skill-labeled full-task demonstrations. Second, ablations show that reliable critic-guided candidate selection is essential for coordinating multi-modal behaviors. Third, scaling experiments show that the method handles larger behavior repertoires and maintains stronger performance than task-specific imitation baselines as chained targets extend the horizon. These results suggest that explicit skill abstraction is not a prerequisite for long-horizon rearrangement, and that implicit-behavior coordination offers a promising data-driven alternative to explicit skill-based pipelines.

</details>

---

### [[20_Research/Papers/具身智能/Empirical_Pedestrian_Safety_Assessment_in_a_Mobile_Robot_Using_a_Predictive_Social_Force_Model|Empirical Pedestrian Safety Assessment in a Mobile Robot Using a Predictive Social Force Model]]

![[assets/2607.09192_figure.png|800]]

- **arXiv**: [2607.09192](https://arxiv.org/abs/2607.09192)
- **PDF**: https://arxiv.org/pdf/2607.09192
- **详细分析**: [[20_Research/Papers/具身智能/Empirical_Pedestrian_Safety_Assessment_in_a_Mobile_Robot_Using_a_Predictive_Social_Force_Model|Empirical Pedestrian Safety Assessment in a Mobile Robot Using a Predictive Social Force Model]]
- **作者**: Alireza Jafari, Yun-Hao Tsai, Yen-Chen Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Empirical Pedestrian Safety Assessment in a Mobile Robot Using a Predictive Social Force Model》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robots are going to share the sidewalks with pedestrians. They must ensure their objective safety and respect the walkers' subjective safety/comfort. Computationally efficient Social Force Models (SFM) present interpretable solutions for real-time robot navigation in dynamic crowds. Recent explorations of Projected Time-to-collision (PTTC) integration into SFM variants, for example, PTTC-based SFM (TSFM), improve safety metrics. But the effect of predictive variants is unclear. We introduce Predictive SFM (PSFM) and Predictive TSFM (PTSFM) by integrating predicted social force vectors over a finite time horizon. The paper implements SFM, TSFM, PSFM, and PTSFM on a nonholonomic mobile robot and performs experimental trials with volunteers attending a facing scenario. We systematically study objective and subjective safety across the variants. Minimum PTTC, average speed, minimum distance, lateral distance, and the maximum trajectory curvature benchmark the objective safety. Likert scale post-interaction surveys assess subjective safety by marking comfort, smoothness, distance appropriateness, and speed suitability. We confirm that PTTC integration improves safety metrics. The prediction contribution is limited and occasionally visible in some of the sub-metrics. Some participants perceive smoother movements and safer speed behavior with predictive methods, but Mann-Whitney tests reveal no significant differences in subjective ratings. Therefore, PTTC-based navigation enhances safety, whereas the formulated prediction offers limited additional benefits in single-pedestrian scenarios.

</details>

---

### [[20_Research/Papers/强化学习/TactiDex_A_Real-World_Tactile-Guided_Benchmark_for_Human-Like_Dexterous_Manipulation|TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation]]

![[assets/2607.09190_figure.png|800]]

- **arXiv**: [2607.09190](https://arxiv.org/abs/2607.09190)
- **PDF**: https://arxiv.org/pdf/2607.09190
- **详细分析**: [[20_Research/Papers/强化学习/TactiDex_A_Real-World_Tactile-Guided_Benchmark_for_Human-Like_Dexterous_Manipulation|TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation]]
- **作者**: Suting Ni, Hanbing Zhang, Zhenyu Wei, Guo Chen, Chixuan Zhang, Ye Shi, Jingya Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《TactiDex: A Real-World Tactile-Guided Benchmark for Human-Like Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile feedback is fundamental to Hand-Object Interaction (HOI), governing contact formation, force regulation, and stable manipulation, making it essential for achieving true human-like dexterous manipulation. Yet, current human-to-robot dexterous transfer pipelines primarily rely on kinematic trajectories, resulting in motion imitation without physically grounded interaction. To address this, we introduce TactiDex, a real-world tactile-guided benchmark specifically designed to move dexterous manipulation beyond kinematic mimicry toward contact-level human-likeness. TactiDex provides a comprehensive dataset that elegantly aligns whole-hand tactile signals with multi-granularity kinematic and object states, coupled with standardized evaluation metrics. Building upon this data paradigm, we propose a tactile-driven transfer framework that effectively translates human demonstrations into physically plausible robotic execution. We introduce TactiSkill, a framework built upon a novel tri-component tactile reward that innovatively uses tactile signals as structured supervision. This reward unifies guidance, human-like alignment, and contact constraints into a single objective. Through comprehensive experiments on both single and bimanual tasks, we demonstrate that TactiSkill achieves superior performance in manipulation success and physical realism. This work lays a crucial foundation for advancing tactile-aware dexterous manipulation. Our project page at https://tactidex.github.io/.

</details>

---

### [[20_Research/Papers/机器人/Residual_Physics-Informed_Neural_Networks_for_High-Fidelity_BLDC_Motor_Modeling|Residual Physics-Informed Neural Networks for High-Fidelity BLDC Motor Modeling]]

![[assets/2607.09136_figure.png|800]]

- **arXiv**: [2607.09136](https://arxiv.org/abs/2607.09136)
- **PDF**: https://arxiv.org/pdf/2607.09136
- **详细分析**: [[20_Research/Papers/机器人/Residual_Physics-Informed_Neural_Networks_for_High-Fidelity_BLDC_Motor_Modeling|Residual Physics-Informed Neural Networks for High-Fidelity BLDC Motor Modeling]]
- **作者**: Haitham El-Hussieny
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Residual Physics-Informed Neural Networks for High-Fidelity BLDC Motor Modeling》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate dynamics modeling of Brushless DC (BLDC) motors is fundamental to high-performance robotic joint control. This paper presents a Physics-Informed Neural Network (PINN) with a deep residual (ResNet) backbone that learns a continuous-time surrogate of the full six-state BLDC motor dynamics. Given simulation time, applied three-phase voltages, and excitation parameters as inputs, the network directly predicts all motor state variables -- rotor angle, angular velocity, three-phase currents, and winding temperature -- while simultaneously satisfying the governing electromechanical and thermal ODEs through a composite physics-data loss. A curriculum scheduling strategy gradually activates the physics penalty to prevent premature convergence. Training runs are completed in under two minutes on a standard CPU. Crucially, once trained, PINN inference achieves latencies of 0.1--22, mu s per query, up to 118x faster than conventional ODE solvers, making it suitable for real-time observer and control applications.

</details>

---

### [[20_Research/Papers/具身智能/Vascular_Geometry_Characterization_for_AI-Based_Endovascular_Navigation|Vascular Geometry Characterization for AI-Based Endovascular Navigation]]

![[assets/2607.09130_figure.png|800]]

- **arXiv**: [2607.09130](https://arxiv.org/abs/2607.09130)
- **PDF**: https://arxiv.org/pdf/2607.09130
- **详细分析**: [[20_Research/Papers/具身智能/Vascular_Geometry_Characterization_for_AI-Based_Endovascular_Navigation|Vascular Geometry Characterization for AI-Based Endovascular Navigation]]
- **作者**: Han-Ru Wu, Harry Robertshaw, Lisa Dwyer-Joyce, Thomas C Booth, Alejandro Granados
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，强化学习 0.4）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Vascular Geometry Characterization for AI-Based Endovascular Navigation》归入 强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mechanical thrombectomy (MT) is a time-critical intervention for acute ischemic stroke; however, access remains limited due to a shortage of neuroradiologists and specialized centers. Reinforcement learning (RL) offers potential to automate endovascular navigation and improve accessibility, yet current models lack standardized frameworks to assess navigation difficulty for model training and evaluation. This study aims to identify vascular metrics associated with navigation difficulty and to develop an automated pipeline for quantitative vascular feature extraction, enabling future complexity grading. Vascular trees were segmented from computed tomography angiograms from 61 patients, and vascular metrics including aortic arch type, presence of bovine arch, vessel length, tortuosity, take-off angle, number of reverse curves, were measured using a custom pipeline. A Soft Actor-Critic RL algorithm was used for 120 s autonomous navigation. Outcomes were analyzed using both mixed effects linear and logistic regression. On the left side, the presence of a bovine arch and aortic arch type II/III increased navigation time by 30.19 s and 37.92 s, respectively, while greater tortuosity (\b{eta} = 118.20) further prolonged the procedure and reduced success probability. On the right side, type II/III arches extended procedure time by 45.94 s, while each additional reverse curve was associated with 3.96 s longer navigation time and lower probability of success. These findings demonstrate for the first time that MT agent navigation difficulty is strongly influenced by vascular geometry. The proposed automated pipeline enables objective and quantitative characterization of vascular features, providing a foundation for future development of standardized complexity grading and RL model evaluation, without aiming to demonstrate clinically generalizable autonomous navigation.

</details>

---

### [[20_Research/Papers/机器人/Dec-MARVEL_Decentralized_Multi-Agent_Exploration_without_Communication_under_Budget_Constraints|Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints]]

![[assets/2607.09060_figure.png|800]]

- **arXiv**: [2607.09060](https://arxiv.org/abs/2607.09060)
- **PDF**: https://arxiv.org/pdf/2607.09060
- **详细分析**: [[20_Research/Papers/机器人/Dec-MARVEL_Decentralized_Multi-Agent_Exploration_without_Communication_under_Budget_Constraints|Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints]]
- **作者**: Janghyun Cho, Jimmy Chiun, Guillaume Sartoretti, Changjoo Nam
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Dec-MARVEL: Decentralized Multi-Agent Exploration without Communication under Budget Constraints》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-UAV exploration is often constrained by unreliable communication, limited field-of-view sensing (e.g., lightweight onboard camera), and finite travel budgets that require each robot to reserve enough budget to return to its base. We present Dec-MARVEL, a decentralized budget-aware exploration framework for communication-free teams with directional sensing. Rather than exchanging maps, goals, or messages, each robot coordinates through its incidental observations: any teammate trajectory within its field of view serves as a coordination signal. A graph-attention actor fuses local frontier geometry, teammate motion, and budget features to select return-feasible waypoint-heading actions. The actor is trained with phase-conditioned critics, a training-only task-oriented privileged critic, and a mixture-based budget curriculum. Across 900 held-out trials spanning three team sizes (2, 4, 8 robots) and three travel budgets (720, 800, 1024 meters) against four baselines, Dec-MARVEL achieves the highest or tied-highest exploration rate and lowest sensing overlap across all nine team-size budget configurations. Under our tightest 720m budget, it reaches 53%, 94%, and 100% success for 2, 4, and 8 robots, versus 37%, 83%, and 99% for the strongest baseline. Physical-robot experiments demonstrate successful sim-to-real transfer and real-world deployment of Dec-MARVEL.

</details>

---

### [[20_Research/Papers/具身智能/Impedance-Guided_Programmable_Transmission_of_Localized_Deformation_in_Modular_Soft_Metamaterials|Impedance-Guided Programmable Transmission of Localized Deformation in Modular Soft Metamaterials]]

![[assets/2607.08966_first_page.png|800]]

- **arXiv**: [2607.08966](https://arxiv.org/abs/2607.08966)
- **PDF**: https://arxiv.org/pdf/2607.08966
- **详细分析**: [[20_Research/Papers/具身智能/Impedance-Guided_Programmable_Transmission_of_Localized_Deformation_in_Modular_Soft_Metamaterials|Impedance-Guided Programmable Transmission of Localized Deformation in Modular Soft Metamaterials]]
- **作者**: Weiyun Xu, Daewon Hong, Zhi Zhao, Rahul Dev Kundu, Xiaojia Shelly Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Impedance-Guided Programmable Transmission of Localized Deformation in Modular Soft Metamaterials》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft metamaterials provide a promising platform for robotics, biomedical devices, and flexible electronics. The localized mechanical responses by nonuniform excitation are ubiquitous in soft materials, yet their controlled transmission across assemblies remains largely overlooked in metamaterial design, which critically constrains nontrivial functionalities with end-to-end and long-range deformation transmission. Here, we introduce an impedance-guided design framework that enables programmable transmission of localized deformation in modular soft metamaterials, achieving behaviors unattainable by intuitive design. By establishing a nonlinear model considering position-dependent interactions and integrating the concept of mechanical impedance within metamaterials, we regulate assembly-level transmission solely through unit-cell topology optimization. The resulting framework enables effective synthesis of module families, allowing both homogeneous and heterogeneous assemblies to be custom-built with markedly enhanced transmission characteristics. Leveraging the highly combinatorial and extensible design space, we physically realize diverse on-demand displacement manipulation architectures, including obstacle-bypassing modular soft-metamaterial assemblies, defect-tolerant soft gripping, and embodied signal processing. Beyond deformation programming, the reconfigurability and reassemblability of these soft modules can embed electric logic signals, enabling energy-efficient and low-latency information processing through compliant-switch-controlled mechanical LED displays and wearable finger-motion-sensing controllers. Our method provides fundamental insights into localized deformation transmission in modular soft metamaterials and establishes a scalable route toward embodied-intelligence material systems, particularly for soft-metamaterial-centric actuation, sensing, and collective computing.

</details>

---

### [[20_Research/Papers/强化学习/AgenticFocus_Object-Preserving_Mixed_Reality_Synthesis_from_Human_FPV_Video_for_Dexterous_Humanoid_Learning|AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning]]

![[assets/2607.08857_figure.png|800]]

- **arXiv**: [2607.08857](https://arxiv.org/abs/2607.08857)
- **PDF**: https://arxiv.org/pdf/2607.08857
- **详细分析**: [[20_Research/Papers/强化学习/AgenticFocus_Object-Preserving_Mixed_Reality_Synthesis_from_Human_FPV_Video_for_Dexterous_Humanoid_Learning|AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning]]
- **作者**: Iaroslav Kolomiets, Miguel Altamirano Cabrera, Artem Lykov, Jeffrin Sam, Dmitrii Iarchuk, Yara Mahmoud, Daniia Zinniatullina, Mikhail Konenkov, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 2.4，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《AgenticFocus: Object-Preserving Mixed Reality Synthesis from Human FPV Video for Dexterous Humanoid Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human egocentric video is a scalable supervision source for humanoid policy learning, but current pipelines struggle with hand-object occlusion, oversimplified motion, or specialized capture hardware. We introduce AgenticFocus, a Mixed Reality synthesis pipeline that converts ordinary first-person-view human videos into robot-trainable demonstrations by restoring occluded object geometry, reconstructing full-hand motion, and retargeting it to a humanoid embodiment through camera-relative alignment and layered compositing. The resulting dataset pairs focused visual observations with synchronized robot actions and states. AgenticFocus achieves lower trajectory error and smoother wrist motion than cross-embodiment baselines, with SPARC scores of -5.18 versus -5.56 and -6.05.

</details>

---
