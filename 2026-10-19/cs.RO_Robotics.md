# cs.RO | Robotics | 2026-10-19

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/强化学习/Blind_Precise_Assembly_Proprioceptive_Sim-to-Real_Peg-in-Hole_for_Diverse_Parts|Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts]]

![[assets/2610.23849_figure.png|800]]

- **arXiv**: [2610.23849](https://arxiv.org/abs/2610.23849)
- **PDF**: https://arxiv.org/pdf/2610.23849
- **详细分析**: [[20_Research/Papers/强化学习/Blind_Precise_Assembly_Proprioceptive_Sim-to-Real_Peg-in-Hole_for_Diverse_Parts|Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts]]
- **作者**: Antonia Bronars, Younghyo Park, Kushal Kedia, Pulkit Agrawal
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.9（加权：具身智能 1.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Blind Precise Assembly: Proprioceptive Sim-to-Real Peg-in-Hole for Diverse Parts》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ProprioceptiveSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Every robot already carries high-resolution contact sensors: its own joints. Legged robots and humanoids exploit them to walk, run, and track whole-body motions without vision, but there the contacts are large and forceful. Is joint sensing also enough for precise, contact-rich assembly, where the robot must find a millimeter-scale opening, mesh gear teeth, or catch a thread through light contact? We study this question by training blind assembly policies that observe only a short history of joint positions, velocities, and their own actions, without visual, force, torque, or tactile sensing. The poses of both the fixture and the part are unknown to the policy, and the grasp is randomized substantially. The policy must therefore assemble the parts through contact, sensed exclusively through its own proprioception. Trained with reinforcement learning entirely in simulation over randomized parts, grasps, and contacts, such policies learn peg insertion, gear meshing, and nut threading. The peg insertion policy transfers zero-shot to the real world and inserts pegs of different shapes and sizes in 73% of trials. Controlled comparisons with matched visual policies in simulation show that blind policies generalize far better to unseen part shapes and sizes, though they can be slower. Training such policies needs thousands of different assemblies, each simulated with its clearance intact, so we also release an open-source generator that builds them procedurally from exact convex pieces for MuJoCo; it is more accurate and faster than convex decomposition or MuJoCo's signed-distance collision. Videos and interactive simulations are at https://younghyopark.me/blind-proprioceptive-assembly/.

</details>

---

### [[20_Research/Papers/具身智能/MOSS_Multimodal_Origami_Swamp_Robot_System|MOSS: Multimodal Origami Swamp Robot System]]

![[assets/2610.23813_figure.png|800]]

- **arXiv**: [2610.23813](https://arxiv.org/abs/2610.23813)
- **PDF**: https://arxiv.org/pdf/2610.23813
- **详细分析**: [[20_Research/Papers/具身智能/MOSS_Multimodal_Origami_Swamp_Robot_System|MOSS: Multimodal Origami Swamp Robot System]]
- **作者**: T. Lan, A. Babgei, L. Romanello, M. Kovac, S. F. Armanini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.6，大模型 0.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《MOSS: Multimodal Origami Swamp Robot System》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic systems for environmental monitoring and ecological surveying in wetlands and swamps must operate across diverse terrestrial and aquatic conditions. Conventional fixed-geometry wheels cannot adapt their contact geometry to these varying conditions. This work presents MOSS (Multimodal Origami Swamp Robot System), a compact amphibious robotic platform with 3D-printed origami wheels. The compact crank mechanism switches the wheel between contracted and expanded configurations, changing its width, body diameter, and fin orientation simultaneously. The contracted configuration is better suited to efficient rolling on firmer ground, whereas the expanded configuration provides greater contact and terrain engagement on softer surfaces. MOSS was evaluated on soil, sand, mud with varying water content, and water, in addition to in-motion morphing and terrestrial-aquatic transition tests. The more energy-efficient wheel configuration depended on terrain. The contracted configuration achieved a lower cost of transport on firmer soil and mud, whereas the expanded configuration performed better on wetter mud, sand, and water, reducing the cost of transport by up to 29%. Expanded wheels also reduced slip in wet mud and reduced both slip and hub sinkage in sand. MOSS successfully completed configuration changes in $1.95 \pm 0.11$ s and demonstrated continuous locomotion across soil-mud-water transitions. Outdoor trials further demonstrated operation across natural deformable terrain and water. These results show that adaptive wheel geometry provides terrain-dependent locomotion benefits and enables a single compact platform to traverse substantially different terrestrial and aquatic conditions.

</details>

---

### [[20_Research/Papers/具身智能/Not_All_Actions_Contribute_Equally_Learning_Precise_Progress_Estimation_from_Imprecise_Demonstrations|Not All Actions Contribute Equally: Learning Precise Progress Estimation from Imprecise Demonstrations]]

![[assets/2610.23769_figure.png|800]]

- **arXiv**: [2610.23769](https://arxiv.org/abs/2610.23769)
- **PDF**: https://arxiv.org/pdf/2610.23769
- **详细分析**: [[20_Research/Papers/具身智能/Not_All_Actions_Contribute_Equally_Learning_Precise_Progress_Estimation_from_Imprecise_Demonstrations|Not All Actions Contribute Equally: Learning Precise Progress Estimation from Imprecise Demonstrations]]
- **作者**: Huanqian Wang, Boshi Tang, Botong Xiao, Jie Zhang, Yang Yue, Danhua Tao, Shiji Song, Gao Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Not All Actions Contribute Equally: Learning Precise Progress Estimation from Imprecise Demonstrations》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Progress estimators play an essential role in providing dense reward signals for reinforcement learning in robotic manipulation, but accurately assessing task progress can be much challenging. Existing methods heavily rely on expert data and naively assume that all actions within a demonstration contribute to task success. This assumption often breaks down in real-world scenarios, especially in high-precision manipulation, where subtle geometric errors can lead to task failure. Therefore, these methods can erroneously interpret human mistakes as meaningful progress, further corrupting progress learning. We argue that a key limitation is the lack of a global prior regarding task evaluation criteria, which is crucial for distinguishing meaningful progress from human mistakes. To this end, we propose PRIME, a novel progress estimator capable of learning precise progress estimation from imprecise demonstrations by aggregating experience across trajectories. PRIME constructs a weighted graph over observed states, connecting states across trajectories based on spatial proximity and visual consistency. Edge weights encode spatial distances as transition costs, and shortest-path search approximates the geodesic distance to success. Changes in this distance naturally distinguish advancement, stagnation, and setbacks without assuming monotonic progress over time. Extensive experiments in both simulation and real world on precise manipulation tasks show that PRIME is consistently effective across diverse tasks, and robust to data with varying degrees of suboptimality. Notably, the advantage of PRIME gets more pronounced in higher-precision scenarios, yielding up to a \(5\times\) improvement in policy success rate over the SFT baselines on charger insertion.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Robot_Metareasoning_Adaptive_Computation_Budgets_for_Real-Time_Control|Learning Robot Metareasoning: Adaptive Computation Budgets for Real-Time Control]]

![[assets/2610.23662_figure.png|800]]

- **arXiv**: [2610.23662](https://arxiv.org/abs/2610.23662)
- **PDF**: https://arxiv.org/pdf/2610.23662
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Robot_Metareasoning_Adaptive_Computation_Budgets_for_Real-Time_Control|Learning Robot Metareasoning: Adaptive Computation Budgets for Real-Time Control]]
- **作者**: Lorenzo Magnino, Antonio Marino, Michael Amir, Daigo Shishika, Amanda Prorok
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning Robot Metareasoning: Adaptive Computation Budgets for Real-Time Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning while moving faces an historical trade-off between deliberation and reactivity. A planner running concurrently with execution needs time to compute, so the robot must commit to an open-loop action chunk for that duration: a longer commitment buys a better plan at the cost of feedback frequency. Existing controllers fix this action commitment, and consequently the computation budget, before deployment. However, the optimal computation time is highly state-dependent (due to factors such as unmodeled dynamics, safety constraints, and marginal optimisation gains), i.e. dynamic, therefore offline static tuning risks leaving systems blind during critical maneuvers or unable to find global effective solutions. We cast the identification of the optimal computation budget as a semi-Markov decision process (SMDP) in which a single decision defines both the robot action commitments and the time allocated to the solver. To solve this, we train a reinforcement-learning policy conditioned on the current state, the executing plan, and inexpensive planner statistics. Across ground-robot navigation, agile quadrotor flight, and contact-rich manipulation, the learned policy changes its budget with the demands of the scenario, discovering efficient reasoning patterns that outperform fixed-budget baselines. https://lorenzomagnino.github.io/learning-robot-metareasoning-review/

</details>

---

### [[20_Research/Papers/具身智能/Foundation-Model-Driven_3D_Scene_Graphs_for_Mobile_Manipulation|Foundation-Model-Driven 3D Scene Graphs for Mobile Manipulation]]

![[assets/2610.23622_figure.jpg|800]]

- **arXiv**: [2610.23622](https://arxiv.org/abs/2610.23622)
- **PDF**: https://arxiv.org/pdf/2610.23622
- **详细分析**: [[20_Research/Papers/具身智能/Foundation-Model-Driven_3D_Scene_Graphs_for_Mobile_Manipulation|Foundation-Model-Driven 3D Scene Graphs for Mobile Manipulation]]
- **作者**: Dominic Maggio, Lorenzo Shaikewitz, Aryan Naveen, Kris Hauser, Luca Carlone
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Foundation-Model-Driven 3D Scene Graphs for Mobile Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geometric and Semantic Foundation models are becoming increasingly popular tools for generating spatial maps for robots. Recent work (e.g., FOUND-IT) has leveraged these tools to construct real-time, task-driven, and open-set 3D scene graphs from a single uncalibrated camera. However, while classical robot mapping techniques have undergone extensive system demonstrations, limited work has been done to develop both the fundamental and the systems wide advancements needed to integrate these new types of robot spatial memory into a full, useable autonomy pipeline. In this paper, we bridge this gap, and in doing so we also evaluate the effectiveness and limitations of this type of 3D memory. Towards this end, we integrate FOUND-IT into a mobile manipulator platform and demonstrate it is well-suited to support multiple objectives such as object change detection, support for multiple mapping sessions, determination of navigable paths, and directly support object grasping for the task of scene re-arrangement. Furthermore, we provide nuanced insights into the effectiveness and limitations of a monocular, foundation-model-driven 3D scene graph construction system using observations from rigorous on-robot experiments. Code is available at https://github. com/MIT-SPARK/FOUND-IT.

</details>

---

### [[20_Research/Papers/具身智能/Enhancing_Visual_Task-Redirection_Attacks_on_Vision-Language-Action_Models_via_Closed-Loop_Optimization|Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization]]

![[assets/2610.23566_figure.png|800]]

- **arXiv**: [2610.23566](https://arxiv.org/abs/2610.23566)
- **PDF**: https://arxiv.org/pdf/2610.23566
- **详细分析**: [[20_Research/Papers/具身智能/Enhancing_Visual_Task-Redirection_Attacks_on_Vision-Language-Action_Models_via_Closed-Loop_Optimization|Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization]]
- **作者**: Chunjin Ye, Guanying Chen, Jianjie Huang, Jianhao Chen, Quanlin Chen, Hanjie Zhao, Haozhe Liang, Tieyun Qian, Xiaochun Cao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《Enhancing Visual Task-Redirection Attacks on Vision-Language-Action Models via Closed-Loop Optimization》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InstructVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models enable language-guided robot manipulation, but remain vulnerable to visual attacks that undermine user control over robot behavior. Prior studies optimize visual perturbations using fixed target supervision. However, the perturbation can change earlier actions and, in turn, the physical states reached later. As the attacked trajectory evolves, this supervision may no longer match the behavior needed at the states actually reached. Accurately matching these targets can therefore fail to advance the attacker-specified task. Even with suitable supervision, reducing average matching error does not ensure sustained task progress. The robot may still fail at a critical stage, and further updates can disrupt previously successful behavior. To address these limitations, we propose TRACO, a framework that enhances existing targeted visual attacks through closed-loop optimization. Its Execution-Driven Supervision rebuilds supervision for the states reached under attack to guide subsequent updates. Within this framework, Progress-Guided Selection focuses updates where progress stalls while maintaining supervision on the earlier behavior needed to reach that point. Experiments across VLA models and simulation environments show improved task-redirection success with TRACO, highlighting the security implications of closed-loop attack optimization.

</details>

---

### [[20_Research/Papers/机器人/Embodiment-Aware_Planning_for_Heterogeneous_Bimanual_Manipulation|Embodiment-Aware Planning for Heterogeneous Bimanual Manipulation]]

![[assets/2610.23551_figure.png|800]]

- **arXiv**: [2610.23551](https://arxiv.org/abs/2610.23551)
- **PDF**: https://arxiv.org/pdf/2610.23551
- **详细分析**: [[20_Research/Papers/机器人/Embodiment-Aware_Planning_for_Heterogeneous_Bimanual_Manipulation|Embodiment-Aware Planning for Heterogeneous Bimanual Manipulation]]
- **作者**: Sukhvansh Jain, Anurag Maurya, Shivam Vats, Narendra Kumar Dhar, Ravi Prakash
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodiment-Aware Planning for Heterogeneous Bimanual Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many manipulation tasks that are effortless for dexterous human hands remain challenging for robotic systems equipped with simple, task-specialized grippers. Industrial platforms commonly rely on end-effectors such as suction cups or parallel-jaw grippers, yet no single mode can reliably satisfy the diverse constraints encountered across different phases of complex manipulation tasks, including pickup, reorientation, insertion, and constrained placement. In this work, we investigate whether complementary simple grippers within a heterogeneous bimanual setup can collectively realize tasks that exceed the capability of any individual gripper alone. Given a single human demonstration specifying the desired object motion, we formulate embodiment-aware execution as a finite-horizon optimization over arm-trajectory assignments. At each segment, the planner determines whether single-arm manipulation or a coordinated dual arm handover is required, jointly reasoning over heterogeneous grasp feasibility, motion constraints, manipulability, and cross-gripper compatibility. Exploiting this formulation, we compute globally consistent assignments with explicit switching regularization. Experiments on a dual Franka FR3 platform equipped with suction and parallel-jaw grippers demonstrate improved feasibility and reliability in tasks that are infeasible under single-gripper execution.

</details>

---

### [[20_Research/Papers/具身智能/Reinforcement_Learning_Based_Multi-Terrain_Adaptive_Whole-Body_Control_for_a_Quadruped_Manipulator|Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator]]

![[assets/2610.23548_figure.jpg|800]]

- **arXiv**: [2610.23548](https://arxiv.org/abs/2610.23548)
- **PDF**: https://arxiv.org/pdf/2610.23548
- **详细分析**: [[20_Research/Papers/具身智能/Reinforcement_Learning_Based_Multi-Terrain_Adaptive_Whole-Body_Control_for_a_Quadruped_Manipulator|Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator]]
- **作者**: Yanzhou Jin, Fei Suo, Chang Liu, Yasuhisa Hasegawa, Liming Chen, Yusuke Iwasawa, Yutaka Matsuo, Yaonan Zhu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.5（加权：具身智能 1.8，强化学习 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped platforms. A reinforcement-learning based whole-body control framework is proposed for quadruped loco-manipulation on complex terrain. The proposed framework combines a hybrid task representation with task-prioritized whole-body learning to coordinate locomotion and manipulation while preserving task-consistent end-effector behavior. A lightweight quadruped manipulator platform is further developed to validate the proposed framework on a small-scale quadruped system. Real-world experiments demonstrate successful deployment on complex terrains such as slopes up to 30 degrees, stairs, and deformable terrain. These results demonstrate the feasibility of deploying learned whole-body control policy for quadruped loco-manipulation in real-world environments and highlight the importance of task-consistent whole-body coordination for terrain-adaptive loco-manipulation.

</details>

---

### [[20_Research/Papers/机器人/FLoTS-SLAM_Optical_Flow-Derived_Uncertainty_for_Monocular_Dynamic_SLAM_with_Two-Stage_Optimization|FLoTS-SLAM: Optical Flow-Derived Uncertainty for Monocular Dynamic SLAM with Two-Stage Optimization]]

![[assets/2610.23496_figure.jpg|800]]

- **arXiv**: [2610.23496](https://arxiv.org/abs/2610.23496)
- **PDF**: https://arxiv.org/pdf/2610.23496
- **详细分析**: [[20_Research/Papers/机器人/FLoTS-SLAM_Optical_Flow-Derived_Uncertainty_for_Monocular_Dynamic_SLAM_with_Two-Stage_Optimization|FLoTS-SLAM: Optical Flow-Derived Uncertainty for Monocular Dynamic SLAM with Two-Stage Optimization]]
- **作者**: Haorui Du, Lipu Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《FLoTS-SLAM: Optical Flow-Derived Uncertainty for Monocular Dynamic SLAM with Two-Stage Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular simultaneous localization and mapping (SLAM) remains challenging in dynamic environments. Real-time dynamic object identification in such environments is a critical problem. Recent approaches estimate per-pixel uncertainty from rendering residuals or multiview feature inconsistency to identify dynamic regions. These methods lack direct motion evidence, and their accuracy may degrade when reconstruction is inaccurate or features are ambiguous. In addition, such uncertainty merely downweights pixels in bundle adjustment (BA), so inaccurate uncertainty estimates can still impair camera pose estimation and 3D reconstruction. Accordingly, we present a monocular RGB SLAM system for dynamic scenes. Specifically, a motion uncertainty estimation method is proposed to derive uncertainty from the residual between optical flow and camera motion induced flow, directly reflecting object motion. The estimation varies with frame alignment accuracy, reducing false detections and yielding accurate pixel-level masks of dynamic regions. To make BA more robust, we estimate camera poses from high confidence pixels. These poses are then used to reproject dynamic pixels during joint refinement of poses and depth, reducing the influence of object motion on both pose and depth updates. Moreover, we provide a quantitative evaluation of dynamic masks and analyze how these masks affect the downstream tracking and reconstruction of dynamic objects. Our approach improves the mean dynamic mask IoU by 35\% over a state-of-the-art baseline on DAVIS, and reduces the average ATE by 59\% on Bonn and 19\% on TUM relative to the SLAM backbone used in our system. The source code will be made publicly available.

</details>

---

### [[20_Research/Papers/具身智能/HexaShell_A_Thin_Harness_for_Exploring_the_Limits_of_VLM_Agents_as_Robot_Coding_Agents|HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents]]

![[assets/2610.23479_figure.png|800]]

- **arXiv**: [2610.23479](https://arxiv.org/abs/2610.23479)
- **PDF**: https://arxiv.org/pdf/2610.23479
- **详细分析**: [[20_Research/Papers/具身智能/HexaShell_A_Thin_Harness_for_Exploring_the_Limits_of_VLM_Agents_as_Robot_Coding_Agents|HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents]]
- **作者**: Hongcheng Gao, Alex Zhou, Jay Zhu, Zelin Zheng, Shijia Ge, Xiping Li, Di Wu, Yazhe Wang, Jianshu Zeng, Xuan Shangguan, Yongli Wang, Yexing Wan...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，大模型 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HexaShell: A Thin Harness for Exploring the Limits of VLM Agents as Robot Coding Agents》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agents built on vision language models (VLMs) now compete with learned policies on robot manipulation leaderboards. We ask how far a coding agent can go when it controls a robot instead of a computer, and where it stops. Our system, HexaShell, keeps the harness thin: it only turns the agent's commands into robot motion. The agent drives a robot with two arms through one command line. It sees three RGB cameras and knows their calibration. After each failed attempt, the agent reads the log, finds the cause, and writes or fixes small programs called tools. In this way it keeps what it learns as code, as a coding agent does when it fixes a failing test. The tools may use only what the robot observes. They use triangulation to find where objects are, relative to each other and to the gripper. If two cameras see the same point, the point lies where the two camera rays meet. If a point lies on a known plane, such as the table or the top of a block, it lies where its ray meets that plane. When the head camera is not enough, the robot moves a wrist camera to get a second view. We build the tools on only ten layouts of one seed per task, then freeze them and test them on ten new layouts of the same seed. We use Codex with GPT-6-Astra at medium reasoning effort. On all 42 RoboDojo tasks, HexaShell reaches a success rate of 39.7% and a progress score of 48.0, averaged in the same way as the leaderboard. This is a new state of the art on RoboDojo. The limit is contact, not reasoning: pushing reaches 92.5% and memory tasks 65.0%, but tight insertion only 8.3%. When the agent fails, it usually sees the failure but cannot make the motion work. We open source the tools evolved so far at https://github.com/HexaFuture/HexaShell.

</details>

---

### [[20_Research/Papers/强化学习/No_Eyes,_No_Problem_What_Does_Touch_Contribute_to_Blind_Baoding_Ball_Manipulation|No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?]]

![[assets/2610.23438_figure.png|800]]

- **arXiv**: [2610.23438](https://arxiv.org/abs/2610.23438)
- **PDF**: https://arxiv.org/pdf/2610.23438
- **详细分析**: [[20_Research/Papers/强化学习/No_Eyes,_No_Problem_What_Does_Touch_Contribute_to_Blind_Baoding_Ball_Manipulation|No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?]]
- **作者**: Ayush Deshmukh, Nalin Agarwal, Elle Miller, Sethu Vijayakumar
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.4（加权：具身智能 0.9，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《No Eyes, No Problem: What Does Touch Contribute to Blind Baoding Ball Manipulation?》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans manipulate objects within their hands through touch alone with remarkable ease, but for robots, achieving sustained real-world manipulation without vision remains an open challenge. Although reinforcement learning (RL) can generate sophisticated blind manipulation policies in simulation, transferring them to a real dexterous hand remains hindered by continuously changing contacts, motion-induced tactile information drift, and the gap between simulated and physical dynamics. We study this problem through Baoding ball rotation on the Shadow Dexterous Hand Lite, using only proprioception and binary tactile feedback as observations. We achieve successful zero-shot transfer through a combination of a sensor-aligned, coupling-aware embodiment in simulation, tactile calibration, and two novel episodic domain randomisations: slew-rate action limits and STuck-AT Taxels. On the physical hand, the policy achieves sustained blind Baoding rotation, completing 225 consecutive $\mathbf{180^\circ}$ rotations (112.5 full rotations) at $\sim0.36 \;\text{rot/s}$ in a single continuous trial without any vision or object-state information. Furthermore, we evaluate the contribution of tactile sensing relative to proprioception alone and identify the hand regions where tactile information is most important. This is the strongest reported hardware result for Baoding ball manipulation in both rotation count and speed, irrespective of the sensing modality used. By effectively bridging the sim-to-real gap, our framework sets a new benchmark for sustained tactile-driven dexterous manipulation on physical hardware.

</details>

---

### [[20_Research/Papers/具身智能/Look_Before_You_Act_Bridging_Active_Perception_and_Vision-Language-Action_Models_via_Observation-Aligned_Data_Adaptation|Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation]]

![[assets/2610.23378_figure.png|800]]

- **arXiv**: [2610.23378](https://arxiv.org/abs/2610.23378)
- **PDF**: https://arxiv.org/pdf/2610.23378
- **详细分析**: [[20_Research/Papers/具身智能/Look_Before_You_Act_Bridging_Active_Perception_and_Vision-Language-Action_Models_via_Observation-Aligned_Data_Adaptation|Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation]]
- **作者**: Jiawei Geng, Zhenyang Liu, Yuzheng Wu, Yongchong Gu, Yanwei Fu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Look Before You Act: Bridging Active Perception and Vision-Language-Action Models via Observation-Aligned Data Adaptation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots manipulating objects in clutter must decide not only how to act, but also where to look. Although active camera motion can expose an occluded target, it may move the robot into an initial observation-state distribution that differs from the manipulation policy's training distribution. We identify this problem as first-frame distribution sensitivity: under perturbed starts in LIBERO, naively prepending camera repositioning to pi_0.5 reduces success from 46.3% to 11.5%. We introduce ActiveAlign, a data-adaptation framework that trains a Vision-Language-Action (VLA) policy from the states at which active perception terminates. A learned viewpoint module first generates a camera trajectory. Offline, ActiveAlign uses closed-loop alignment to connect the trajectory endpoint to an existing demonstration, replays the remaining manipulation trajectory, and retains successful continuations for fine-tuning. At deployment, the same viewpoint module precedes the adapted VLA without modifying its architecture. Across 40 LIBERO tasks, ActiveAlign achieves 70.7% success with pi_0 and 72.7% with pi_0.5, outperforming their standard-training baselines by 40.0% and 26.4% respectively. Matched-state and data-matched controls support gains beyond prefix shortening and generic viewpoint augmentation; OpenVLA and GR00T N1 also show the same trend. Success rate under physical occlusion in real world increases from 35/90 to 83/90. These results show that active perception benefits manipulation when policy training is aligned with the observation and robot-state distribution induced by viewpoint selection.

</details>

---

### [[20_Research/Papers/具身智能/LAW_Unifying_Language,_Action,_and_World_Modeling_for_Agentic_Physical_Intelligence|LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence]]

![[assets/2610.23334_figure.png|800]]

- **arXiv**: [2610.23334](https://arxiv.org/abs/2610.23334)
- **PDF**: https://arxiv.org/pdf/2610.23334
- **详细分析**: [[20_Research/Papers/具身智能/LAW_Unifying_Language,_Action,_and_World_Modeling_for_Agentic_Physical_Intelligence|LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence]]
- **作者**: Jiajun Cao, Kai Tang, Bohua Zhang, Zezhong Qian, Ying Li, Xiaozhu Ju, Xiaobao Wei, Jiaming Liu, Yang Ding, Sixiang Chen, Yiding Sun, Siyuan Qian...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《LAW: Unifying Language, Action, and World Modeling for Agentic Physical Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models jointly predict actions and future world states, but long-horizon manipulation further requires language reasoning to plan subtask objectives, assess execution progress, and guide action selection. We present LAW, a closed-loop VLM--WAM framework that unifies language reasoning, action generation, and world modeling through semantic subtask progress. Within the LAW agent, a hybrid-expert vision-language model plans the remaining subtasks, estimates the values of and fuses actions proposed by a world-action model, and asynchronously assesses execution status to support continued execution and subtask transitions. Within the world-action model, Mixture-of-Transformer Experts integrates modality-specific and shared computation for joint video--action modeling. Dual-stream hierarchical visual memory maintains temporal context for both models, while subtask-local value learning aligns action evaluation with semantic objectives and preserves supervision from successful prefixes of failed trajectories. LAW achieves 94.21% average success across 50 RoboTwin tasks. Replacing the WAM backbone with OpenWAM-$alpha$ further raises the average success rate to 95.56%, establishing a new open-source state of the art on RoboTwin. Despite having only 2B parameters, our VLM also outperforms variants using Embodied-R1.5 and GPT-5.5 High. On three long-horizon real-robot tasks, LAW achieves 65% average success, compared with 28.33% for $pi_{0.5}$ and 25% for Fast-WAM.

</details>

---

### [[20_Research/Papers/具身智能/From_Sliding_Windows_to_Self-evolving_Lifelong_Memory_A_Dual-perspective_Survey_of_Memory_Paradigms_for_Long-Horizon_Robotics_VLA_Models|From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models]]

![[assets/2610.23319_first_page.png|800]]

- **arXiv**: [2610.23319](https://arxiv.org/abs/2610.23319)
- **PDF**: https://arxiv.org/pdf/2610.23319
- **详细分析**: [[20_Research/Papers/具身智能/From_Sliding_Windows_to_Self-evolving_Lifelong_Memory_A_Dual-perspective_Survey_of_Memory_Paradigms_for_Long-Horizon_Robotics_VLA_Models|From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models]]
- **作者**: Yong Wang, Boyu Shen, Xinwei Zhang, Yizheng Li, Keyuan Luo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《From Sliding Windows to Self-evolving Lifelong Memory: A Dual-perspective Survey of Memory Paradigms for Long-Horizon Robotics VLA Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robotic tasks expose a fundamental limitation of current Vision-Language-Action (VLA) models because their restricted temporal context pre-vents effective accumulation and reuse of past experiences. As a result, memory has become a fundamental component for enabling embodied agents to perform long-horizon reasoning and adaptive decision-making. This survey presents a systematic taxonomy of VLA memory mechanisms based on memory scope and persistence, categorizing existing approaches into five representative paradigms and one emerging frontier. Based on this taxonomy, we compare representative VLA memory systems in terms of memory characteristics, architectural com-plexity, and open-source maturity, revealing a clear trade-off in which increasing architectural complexity is generally accompanied by decreasing open-source ma-turity. Finally, we discuss the key challenges in building full-lifecycle memory systems, including efficient memory management and lifelong knowledge evolu-tion. Overall, this survey provides a unified perspective on memory architectures for VLA agents and offers insights into the development of lifelong embodied in-telligence.

</details>

---

### [[20_Research/Papers/机器人/SkyAgent_Revisable_Target_Memory_for_Continuous_Aerial_Search|SkyAgent: Revisable Target Memory for Continuous Aerial Search]]

![[assets/2610.23293_figure.png|800]]

- **arXiv**: [2610.23293](https://arxiv.org/abs/2610.23293)
- **PDF**: https://arxiv.org/pdf/2610.23293
- **详细分析**: [[20_Research/Papers/机器人/SkyAgent_Revisable_Target_Memory_for_Continuous_Aerial_Search|SkyAgent: Revisable Target Memory for Continuous Aerial Search]]
- **作者**: Kaibo Yang, Xingyu Wu, Enze Zhu, Yajie Chai, Xuyang Li, Jiahui Cui, Xiaoxuan Liu, Lei Wang, Zhan Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: cs.RO

#### 研究背景与动机

《SkyAgent: Revisable Target Memory for Continuous Aerial Search》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GOAT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous aerial search builds target hypotheses from sparse, viewpoint-dependent observations. When later evidence contradicts a stored hypothesis, however, the candidate can remain available to the planner and continue triggering approach or verification actions. We call this trajectory-level failure false candidate persistence (FCP). We equip SkyAgent with Revisable Target Memory (RTM), which associates evidence with persistent candidates, discounts correlated views, and revises each candidate through Tentative, Confirmed, and Rejected states. The key interface binds every generated waypoint to its source candidate: rejection therefore invalidates stale goals, while conservative reactivation protects temporarily occluded targets. Across four splits from the CityAVOS, UAV-ON, and OpenUAV benchmarks, our SkyAgent equipped with RTM outperforms all competitors, improving SR by 2.90--6.31 points while substantially reducing Behavior-FCP and post-contradiction travel with a low false-rejection rate. Across 35 matched real-world DJI scenarios per method, RTM consistently improves task success and behavioral reliability, further validating its state-to-action correction under physical deployment conditions.

</details>

---

### [[20_Research/Papers/具身智能/CoEvolve_Self-Evolving_Code_Policies_from_Skills_to_Strategies_for_Humanoid_Robots|CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots]]

![[assets/2610.23288_figure.png|800]]

- **arXiv**: [2610.23288](https://arxiv.org/abs/2610.23288)
- **PDF**: https://arxiv.org/pdf/2610.23288
- **详细分析**: [[20_Research/Papers/具身智能/CoEvolve_Self-Evolving_Code_Policies_from_Skills_to_Strategies_for_Humanoid_Robots|CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots]]
- **作者**: Zicheng Liu, Haochen Wu, Jiawei He, Suyun Zhao, Huan Yang, Cheng Chi, Hao Tang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 1.8，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《CoEvolve: Self-Evolving Code Policies from Skills to Strategies for Humanoid Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in Vision-Language-Action (VLA) models and World Action Models (WAMs) have expanded the manipulation and whole body capabilities of individual robots. Yet a single robot remains limited by its embodiment, and many real world tasks require capabilities that can only emerge through cooperation. Existing multi robot frameworks largely emphasize task decomposition, allocation, and replanning, while providing limited support for adapting executable coordination when physical execution deviates from the intended behavior. We present CoEvolve, a framework that represents team coordination as executable code over fixed robot motor skills. CoEvolve introduces Verifier Guided Coordination Evolution, where a multimodal foundation model instantiates coordination strategies through motion primitives, semantic objectives, temporary robot roles, and bounded execution parameters. Physical verification evaluates each executed transition, rejected behaviors trigger structured coordination revision from an accepted checkpoint, and verified experience is retained to guide subsequent decisions. We evaluate CoEvolve with two simulated Unitree G1 humanoids transporting a freely supported rigid payload through constrained corridors. Across 15 base task runs with three multimodal backbone families, CoEvolve completes 8 tasks, with every backbone achieving end to end success. Additional evaluations yield verified placement on two additional corridor layouts and after both same-backbone and cross-backbone experience initialization, while exposing persistent limitations in motion precision and contact stability. These results support executable coordination as a practical interface for adapting long horizon multi robot collaboration under shared physical constraints.

</details>

---

### [[20_Research/Papers/强化学习/LY-GWM-RoboCasa-Human300_Prediction-Guided_Action_Selection_with_a_Graph_Dynamics_Model|LY-GWM-RoboCasa-Human300: Prediction-Guided Action Selection with a Graph Dynamics Model]]

![[assets/2610.23274_first_page.png|800]]

- **arXiv**: [2610.23274](https://arxiv.org/abs/2610.23274)
- **PDF**: https://arxiv.org/pdf/2610.23274
- **详细分析**: [[20_Research/Papers/强化学习/LY-GWM-RoboCasa-Human300_Prediction-Guided_Action_Selection_with_a_Graph_Dynamics_Model|LY-GWM-RoboCasa-Human300: Prediction-Guided Action Selection with a Graph Dynamics Model]]
- **作者**: TianLiang Ma, Ting Ma, ZhongYuan Ma
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《LY-GWM-RoboCasa-Human300: Prediction-Guided Action Selection with a Graph Dynamics Model》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present LY-GWM-RoboCasa-Human300, a policy that combines a Human300-fine-tuned GR00T-N1.5 action generator, an action-conditioned graph dynamics model, and a learned binary state-reward scorer. At inference, the policy samples four action chunks, predicts the future latent features and robot state for each, and executes the candidate with the highest predicted-state reward logit. Predictions therefore influence the actions sent to the environment. The evaluated system uses a 16-step prediction horizon and keeps all three components frozen during evaluation. In the local evaluation on 50 RoboCasa 1.0.1 tasks in the pretrain kitchen split, with 50 episodes per task, the system records 207/2,500 successes (8.28%), compared with 181/2,500 (7.24%) in the historical self-trained GR00T-N1.5 baseline. The observed difference is 26 successes, or 1.04 percentage points. The atomic group improves from 141/900 to 150/900. Separately, the RoboCasa maintainers re-evaluated the submission and reported 354/1,500 successes (23.6%) across 50 tasks, with leaderboard rates of 48.3%, 16.3%, and 3.1% for Atomic-Seen, Composite-Seen, and Composite-Unseen. The local and official results are reported separately; their difference is not attributed to a model improvement. Recorded local audits identify 212,700 changed environment-input chunks, including 28,223 in atomic tasks. We describe the actual training stages, implemented inference mechanism, evaluation provenance, and public reproduction entrypoints. These results document an active prediction-and-selection system and a positive historical difference.

</details>

---

### [[20_Research/Papers/具身智能/SimpleVLN_Towards_Simple_and_Frontier_Vision-Language_Navigation|SimpleVLN: Towards Simple and Frontier Vision-Language Navigation]]

![[assets/2610.23203_figure.png|800]]

- **arXiv**: [2610.23203](https://arxiv.org/abs/2610.23203)
- **PDF**: https://arxiv.org/pdf/2610.23203
- **详细分析**: [[20_Research/Papers/具身智能/SimpleVLN_Towards_Simple_and_Frontier_Vision-Language_Navigation|SimpleVLN: Towards Simple and Frontier Vision-Language Navigation]]
- **作者**: Lingyi Hong, Weiren Cai, Jiayu Chen, Xinyu Zhou, Bailin He, Yunfei Guo, Qiao Sun, Boyu Ma, Jianfei Yang, Wenqiang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 强化学习
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《SimpleVLN: Towards Simple and Frontier Vision-Language Navigation》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IL-DAgger-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-and-Language Navigation (VLN) requires embodied agents to ground language in visual observations and make long-horizon decisions. Existing methods often address these demands through task-specific architectures. As multimodal large language models (MLLMs) become increasingly capable, an important question remains: Have we truly unlocked the potential of native MLLMs for VLN before introducing task-specific architecture? We present SimpleVLN, an architecture-preserving framework developed through studies of navigation formulation, data construction, and optimization. At the formulation level, SimpleVLN combines single-turn decision inputs with fixed-budget global-local memory to efficiently use navigation history without unbounded context growth, while action chunks enable efficient output of multiple primitive actions per model invocation. For data construction, we combine expert demonstrations with policy-dependent DAgger experience and develop a scalable synthesis pipeline that generates large-scale tasks for reinforcement learning. At the optimization level, a progressive IL-DAgger-RL pipeline advances from action imitation to task-level outcome optimization. Comprehensive experiments validate the effectiveness of these three aspects. We instantiate SimpleVLN across multiple MLLM backbones and model sizes, demonstrating its generality. SimpleVLN achieves 76.7% and 80.1% success rates on the R2R-CE and RxR-CE splits, respectively, substantially outperforming existing methods. These results show that the navigation capabilities of native MLLMs can be effectively unlocked without task-specific architectural designs.

</details>

---

### [[20_Research/Papers/具身智能/ORD-WM_Learning_Object-Centric_Rigid_Dynamics_for_3D_World_Modeling_in_Robotic_Manipulation|ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation]]

![[assets/2610.23156_figure.png|800]]

- **arXiv**: [2610.23156](https://arxiv.org/abs/2610.23156)
- **PDF**: https://arxiv.org/pdf/2610.23156
- **详细分析**: [[20_Research/Papers/具身智能/ORD-WM_Learning_Object-Centric_Rigid_Dynamics_for_3D_World_Modeling_in_Robotic_Manipulation|ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation]]
- **作者**: Yueyang Weng, Xiaopeng Zhang, Yuxi Ou, Yongjin Mu, Chengzhi Zhao, Yanjie Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.2（加权：具身智能 1.5，世界模型 0.6，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《ORD-WM: Learning Object-Centric Rigid Dynamics for 3D World Modeling in Robotic Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VN-PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models provide robots with a predictive mechanism for reasoning about how actions change object states in manipulation tasks. However, existing image-based and dense 3D world models do not explicitly impose object-level rigid motion, leaving rigid-object geometry preservation to be learned implicitly and making multi-step rollouts susceptible to shape drift or object-level motion inconsistency. To address this, we propose ORD-WM, a 3D world model that learns object-centric rigid dynamics for robotic manipulation. ORD-WM learns a vector-neuron variational autoencoder supervised by signed distance fields, which encodes each object point cloud as a geometry-aware latent representation composed of 3D vector features, and uses an action-conditioned dynamics model to predict object-wise SE(3) motion increments. Rather than generating unconstrained next latent states, ORD-WM analytically applies predicted object-wise rigid transformations to the current latent states, separating persistent object geometry from pose changes. Experiments show that ORD-WM enables stable, geometry-preserving multi-step prediction and supports efficient real-time replanning for closed-loop model predictive control in simulated and real-world manipulation scenarios.

</details>

---

### [[20_Research/Papers/具身智能/SCOPE_Selective_Certification_of_Program_Edits_for_Embodied_Heuristic_Learning|SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning]]

![[assets/2610.23128_figure.png|800]]

- **arXiv**: [2610.23128](https://arxiv.org/abs/2610.23128)
- **PDF**: https://arxiv.org/pdf/2610.23128
- **详细分析**: [[20_Research/Papers/具身智能/SCOPE_Selective_Certification_of_Program_Edits_for_Embodied_Heuristic_Learning|SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning]]
- **作者**: Junyang Shu, Bingqing Wei, Jishuo Li, Zheqi He, Yongtao Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《SCOPE: Selective Certification of Program Edits for Embodied Heuristic Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied heuristic learning must balance strategic adaptation with the preservation of previously successful behavior. Local repairs may leave structural failures unresolved, whereas broader revisions can introduce regressions that are costly to detect through repeated environment interaction. We introduce SCOPE (Selective Certification Of Program Edits), which uses failed and successful executions as complementary evidence for program revision. Frontier-guided program search annotates a shared diagnostic graph with execution evidence to distinguish supported progress from unresolved checks. Selective behavioral certification uses stateful API replay to restore recorded responses and mutations, checking whether edits preserve selected historical successes. Diagnosis and certification feedback, supplemented by sparse environment diagnostics, guide consecutive repairs across configurations. SCOPE outperforms the strongest baseline in both simulation and real-world tasks. On LIBERO-PRO and Robosuite, it achieves mean success rates of 80.66% and 84.48%, with respective gains of 6.51 and 3.48 percentage points. Our code is available at https://github.com/VDIGPKU/SCOPE.

</details>

---

### [[20_Research/Papers/强化学习/BeJEPA_A_Goal-Conditioned_Humanoid_Behavior_World_Model_via_Unsupervised_RL|BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL]]

![[assets/2610.23127_figure.png|800]]

- **arXiv**: [2610.23127](https://arxiv.org/abs/2610.23127)
- **PDF**: https://arxiv.org/pdf/2610.23127
- **详细分析**: [[20_Research/Papers/强化学习/BeJEPA_A_Goal-Conditioned_Humanoid_Behavior_World_Model_via_Unsupervised_RL|BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL]]
- **作者**: Liyun Yan, Haoyang Li, Yang Zhang, Jialing Zhu, Zhanxiang Cao, Zihao Zhou, Keqi Zhu, Yizhi Chen, Huang Chuxuan, Shengcheng Fu, Zhong Jiangwei, Qiao Sun...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习
- **相关性评分**: 3.8（加权：具身智能 1.5，强化学习 0.2，世界模型 0.8，机器人 1.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《BeJEPA: A Goal-Conditioned Humanoid Behavior World Model via Unsupervised RL》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid control requires coordinating whole-body posture with position and heading in the world frame. Mainstream controllers imitate trajectories in the root frame, but struggle to regain the target world pose after displacement. We introduce BeJEPA, a goal-conditioned Behavior World Model learned through unsupervised reinforcement learning from human motion priors and robot interaction. BeJEPA learns a shared representation of body configuration and world placement through a joint-embedding predictive architecture (JEPA). A Dynamic Predictor predicts the next state embedding under an action, while a Successor Predictor summarizes a goal-conditioned policy's expected discounted future state embeddings in a single vector. During joint training, Dynamic grounds the initial representation in observed physical transitions, while Successor increasingly organizes it around long-term behavior. Their composition guides policy improvement through one physical prediction and one behavioral summary, without long imagined rollouts. In 20-second motion-tracking experiments, BeJEPA with online action refinement using Dynamic outperforms all evaluated baselines in global body-position error, reducing it on AMASS by 61.7% relative to BFM-Zero with world-pose inputs and 58.7% relative to SONIC. Physical deployment on a Unitree G1 demonstrates joint attainment of posture, world position, and heading goals, recovery from the ground, and closed-loop return after disturbances and goal changes. Project page: https://ylyem9x.github.io/BeJEPA-project.

</details>

---

### [[20_Research/Papers/具身智能/GRASP_Global-Local_Representation_Alignment_and_Spatial-Physical_Grounding_for_Bimanual_Robotic_Manipulation|GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation]]

![[assets/2610.23123_figure.png|800]]

- **arXiv**: [2610.23123](https://arxiv.org/abs/2610.23123)
- **PDF**: https://arxiv.org/pdf/2610.23123
- **详细分析**: [[20_Research/Papers/具身智能/GRASP_Global-Local_Representation_Alignment_and_Spatial-Physical_Grounding_for_Bimanual_Robotic_Manipulation|GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation]]
- **作者**: Zeyuan Ren, Guanxun Zhao, Qi Li, Hao Wang, Wenlong Liao, Keyi Luo, Xijing Zhang, Zhiyuan Zhang, Jingye Cui, Qibin Gu, Zhichen Wang, Yucheng Hu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GRASP: Global-Local Representation Alignment and Spatial-Physical Grounding for Bimanual Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models that directly regress joint-space actions avoid the deployment-time cost of inverse kinematics. However, their training objectives remain misaligned with task success, as joint-space losses ignore the unequal physical consequences of joint errors and visual conditioning lacks explicit focus on hand-object interaction regions. To address these issues, we propose a training-phase prior injection framework for fine-grained bimanual manipulation. First, a physics-grounded flow-matching loss maps the implicit clean-action estimate at every noise level through differentiable forward kinematics (FK) and supervises the resulting Tool Center Point (TCP) pose and inter-arm relative pose, with a bounded noise-level weighting that compensates gradient decay. Second, we introduce a global prediction query group distilled from a frozen DINOv3 teacher through future-frame feature prediction, together with a local interaction query supervised by Grounding DINO at the attention level. Both teachers are removed at inference, and the deployment pipeline is that of a standard joint-space flow policy, adding only the learned query pathway. Simulation and real-robot experiments on long-horizon bimanual tasks show that the two priors are complementary across different deployment settings. The full model excels in in-distribution deployment, while the distilled query branch is preferable under strong visual randomization.

</details>

---

### [[20_Research/Papers/大模型/InstAgent_A_Recursively_Self-Improving_Agent_Operating_System_for_Heterogeneous_Robot_Collaboration|InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration]]

![[assets/2610.23098_figure.png|800]]

- **arXiv**: [2610.23098](https://arxiv.org/abs/2610.23098)
- **PDF**: https://arxiv.org/pdf/2610.23098
- **详细分析**: [[20_Research/Papers/大模型/InstAgent_A_Recursively_Self-Improving_Agent_Operating_System_for_Heterogeneous_Robot_Collaboration|InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration]]
- **作者**: Haoyang Luo, Junhao Qin, Jingyan Cao, Yi Huang, Guangjie Yang, Xiaoyu Chen, Haotao Lu, Tianxiang Gui, Ye Shi, Jingya Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《InstAgent: A Recursively Self-Improving Agent Operating System for Heterogeneous Robot Collaboration》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RAVEN-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Heterogeneous robot teams enable complex, long-horizon tasks by combining complementary sensing, mobility, and manipulation capabilities across multiple embodiments. Yet existing systems struggle to retain execution-time corrections as reusable experience, maintain task-relevant context memory across space and time for reliable handoffs, and explicitly represent the inter-robot dependencies required for structured collaboration. In order to address these challenges, we present InstAgent, a recursively self-improving (RSI) Agent Operating System for heterogeneous robot collaboration. InstAgent organizes team behaviors as agentic behavior trees (BTs) that explicitly model capability assignment, inter-robot dependencies and handoff checks. The RSI mechanism updates these collaboration programs from execution feedback and preserves successful revisions for reuse in future tasks, while shared multimodal spatio-temporal memory provides context for planning and handoff validation. Experiments on 20 real-world multi-robot tasks with three high-level models show consistent gains in task success, first-attempt completion, and execution efficiency.

</details>

---

### [[20_Research/Papers/机器人/Foundation_Models_for_Autonomous_Space_Robotics_Architectures,_Physical_Adaptation,_and_Validation|Foundation Models for Autonomous Space Robotics: Architectures, Physical Adaptation, and Validation]]

![[assets/2610.23068_figure.png|800]]

- **arXiv**: [2610.23068](https://arxiv.org/abs/2610.23068)
- **PDF**: https://arxiv.org/pdf/2610.23068
- **详细分析**: [[20_Research/Papers/机器人/Foundation_Models_for_Autonomous_Space_Robotics_Architectures,_Physical_Adaptation,_and_Validation|Foundation Models for Autonomous Space Robotics: Architectures, Physical Adaptation, and Validation]]
- **作者**: Zizhe Wang, Jia Deng, Xin Lu, Zehao Jia, Yi Huang, Yao Zhu, Jianing Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Foundation Models for Autonomous Space Robotics: Architectures, Physical Adaptation, and Validation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Space robots must interpret tasks and act despite unfamiliar dynamics, difficult sensing conditions, and limited opportunities for human intervention. Foundation models offer reusable perceptual and behavioral knowledge, but their value depends on how that knowledge reaches physical execution. This critical review follows space-specific requirements through perception, prediction, planning, and action to deployment and validation, emphasizing orbital manipulation and proximity operations. Terrestrial comparisons establish benefits of particular pretraining stages and model interfaces; their transfer to space dynamics and constrained onboard operation remains insufficiently tested. Event cameras offer timely motion observations across strong illumination contrasts, while spiking neural networks provide possible routes to sparse local computation. We examine how sensor degradation, state estimation and computing choices affect feedback and recovery. Higher action throughput need not yield fresher feedback; lower processor power can also coexist with higher energy per inference. We organize validation as an iterative sim-to-ground-to-space pathway, connecting physical tests with telemetry-based diagnosis and closed-loop revalidation. A satellite-capture example links observations to approach, contact and recovery, while a corresponding protocol separates generalization from adaptation with limited target-domain interaction. These comparisons identify what models already contribute and the physical evidence needed to support autonomous space operation.

</details>

---

### [[20_Research/Papers/具身智能/PASS_A_Trustworthy_Precision_Approach_Simulation_System_for_CAT_III_Integrity_Algorithm_Development|PASS: A Trustworthy Precision Approach Simulation System for CAT III Integrity Algorithm Development]]

![[assets/2610.23019_figure.png|800]]

- **arXiv**: [2610.23019](https://arxiv.org/abs/2610.23019)
- **PDF**: https://arxiv.org/pdf/2610.23019
- **详细分析**: [[20_Research/Papers/具身智能/PASS_A_Trustworthy_Precision_Approach_Simulation_System_for_CAT_III_Integrity_Algorithm_Development|PASS: A Trustworthy Precision Approach Simulation System for CAT III Integrity Algorithm Development]]
- **作者**: Lang Zhu, Xin Zhang, Yulong Sun, Nan Liu, Jiahe Shen, Xiaodong Zhang, Xingqun Zhan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《PASS: A Trustworthy Precision Approach Simulation System for CAT III Integrity Algorithm Development》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For fixed-wing aircraft, reliable localization during approach and landing is critical to flight safety. Visual--inertial navigation is promising, but aircraft navigation also requires integrity: trustworthy outputs and timely warnings when they should not be used. Real approach data are costly to collect, while many visual errors and failures required for integrity algorithm development are difficult to reproduce safely. We present PASS, a trustworthy Precision Approach Simulation System for CAT III integrity algorithm development. In a unified temporal and geometric framework, PASS integrates configurable airport environments, prescribed trajectories, inertial simulation, calibrated stereo images, and continuous runway-relative ground truth. It supports navigation and integrity research through controllable sensor errors and environmental variations, computable visual projection errors, deterministic runway geometry priors, and condition-labeled data for statistical error modeling. We further propose Sim-to-Real Scene Trustworthiness (SRST), a measure based on DINOv2 feature distributions and UMAP, to quantify sim-to-real closeness. Experiments with representative stereo--inertial estimators demonstrate the usability of the generated sequences and quantify localization errors across algorithms and environments. PASS provides a controllable foundation for developing and evaluating visual--inertial navigation and integrity algorithms for fixed-wing precision approaches up to CAT III requirements.

</details>

---

### [[20_Research/Papers/具身智能/VLA-Fabric_Learning_Interaction_for_Composable_Multi-Arm_VLA_Agents|VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents]]

![[assets/2610.23018_figure.png|800]]

- **arXiv**: [2610.23018](https://arxiv.org/abs/2610.23018)
- **PDF**: https://arxiv.org/pdf/2610.23018
- **详细分析**: [[20_Research/Papers/具身智能/VLA-Fabric_Learning_Interaction_for_Composable_Multi-Arm_VLA_Agents|VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents]]
- **作者**: Chenglong Zhang, Shuaijun Liu, Feiyang You, Shuyang Hao, Chengyu Wu, Ningxin Su
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.3，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VLA-Fabric: Learning Interaction for Composable Multi-Arm VLA Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CommNet, ET-VLA, MA-VLA, Real-World, SingleVLA, TwinVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are rapidly expanding what individual robots can accomplish, yet many real-world manipulation settings require multiple arms to operate as a coordinated system. Existing approaches organize multi-arm coordination in different ways, including centralized joint policies, high-level task or role assignment, and locally executed policies that react to teammates. However, how complete action-producing VLAs should explicitly interact with one another during action generation remains largely unexplored. We introduce VLA-Fabric, which organizes one complete VLA per arm while preserving local perception and action ownership, and enables coordination through learned interaction across policy boundaries. We first systematically study where such interaction should occur, how peer information should be aggregated, and how the interaction should be learned, revealing complementary coordination functions spanning shared context, peer-specific latent information, and action-stage interaction. We then re-instantiate these functions in a structurally different VLA architecture, showing that the coordination principle is not tied to a particular tensor layout or backbone implementation. Finally, we compose teams of three and four arms and evaluate them in simulation and physical experiments. On all four physical tasks, Full interaction improves success over independently trained local policies by 16--40 percentage points. Together, these results suggest that explicit interaction among complete VLA policies offers a scalable path toward networked embodied intelligence.

</details>

---

### [[20_Research/Papers/强化学习/Robotic_Spatiotemporal_Editing_A_Unified_Interface_for_Controllable_Action_Generation_via_Masked_Action_Reconstruction|Robotic Spatiotemporal Editing: A Unified Interface for Controllable Action Generation via Masked Action Reconstruction]]

![[assets/2610.23002_figure.png|800]]

- **arXiv**: [2610.23002](https://arxiv.org/abs/2610.23002)
- **PDF**: https://arxiv.org/pdf/2610.23002
- **详细分析**: [[20_Research/Papers/强化学习/Robotic_Spatiotemporal_Editing_A_Unified_Interface_for_Controllable_Action_Generation_via_Masked_Action_Reconstruction|Robotic Spatiotemporal Editing: A Unified Interface for Controllable Action Generation via Masked Action Reconstruction]]
- **作者**: Yanbang Li, Bu He, Yi Tian, Yu-Chiao Huang, Chenyu Zhang, Ruoqu Chen, Yuanzhe Liu, Yuxiang Gao, Mengdi Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Robotic Spatiotemporal Editing: A Unified Interface for Controllable Action Generation via Masked Action Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative policies can synthesize robot behaviors, yet controlling and editing them through diverse spatiotemporal references remains challenging. In the real world, human intent requires robot behaviors that satisfy constraints on where, when, and how actions are executed. Our key insight is that spatiotemporal control references, such as keypoints, flows, orientations, and keyposes, can be viewed as partial specifications of the same temporal Cartesian action space. We introduce the MAP (Masked Action Space) interface to unify these action references and formulate controllable manipulation as an action inpainting problem. Our Inpainting Policy (IP) reconstructs missing action dimensions of the end-effector, combining progress-guided alignment with multi-mask training to support unseen action-constraint combinations. We further adopt a training-free RePaint variant that iteratively inpaints the action during denoising to reduce control error. On ManiSkill and LIBERO-10, our policy achieves average task success rates of 92.67% and 64.67%, respectively.Real-world experiments demonstrate spatiotemporal control with average positional and rotational errors of 44.3 mm and 7°, respectively, showing that our policy can use diverse references to guide executable robot behaviors.

</details>

---

### [[20_Research/Papers/具身智能/Ego2Contact_Predicting_Touch_from_Egocentric_Human_Video_for_Contact-Rich_Robot_Manipulation|Ego2Contact: Predicting Touch from Egocentric Human Video for Contact-Rich Robot Manipulation]]

![[assets/2610.22932_figure.png|800]]

- **arXiv**: [2610.22932](https://arxiv.org/abs/2610.22932)
- **PDF**: https://arxiv.org/pdf/2610.22932
- **详细分析**: [[20_Research/Papers/具身智能/Ego2Contact_Predicting_Touch_from_Egocentric_Human_Video_for_Contact-Rich_Robot_Manipulation|Ego2Contact: Predicting Touch from Egocentric Human Video for Contact-Rich Robot Manipulation]]
- **作者**: Qianqian Yang, Dayou Li, Bangya Liu, Zihao Zhu, Nuo Chen, Siyuan Xu, Hezhen Hu, Chen Yu, Rebecca Friesen, Minghui Zheng, Cynthia Hipwell, Xiaoning Qian...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Ego2Contact: Predicting Touch from Egocentric Human Video for Contact-Rich Robot Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ViTacWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact locations and interaction forces are critical for contact-rich robot manipulation but are often ambiguous from vision alone. Measuring them on robots requires specialized tactile hardware and platform-specific data collection, which keeps robot tactile data scarce. Human egocentric video is far easier to scale but lacks touch. Recent predictors trained on egocentric recordings paired with tactile-glove measurements can predict this missing signal from video alone. These predictors, however, remain confined to human hands, which differ from robot hands in appearance and tactile layout. We present Ego2Contact, which learns a visual-tactile prior from human interactions and transfers it to robot hands. Its predictor fuses temporal scene context with hand-local visual features to infer bimanual tactile fields from the RGB video. Anatomical region correspondences align varying robot tactile layouts with the predictor's canonical grid, turning robot measurements into fine-tuning targets and predictions into policy inputs. Ego2Contact outperforms prior tactile predictors on human data, including unseen objects, and on robot data after adaptation. The adapted predictor provides tactile inputs for both simulated reinforcement learning and real-robot policy post-training. In simulation, policies using predicted touch outperform non-tactile baselines and recover part of the benefit of ground-truth tactile sensing. These results show that human-learned tactile priors can supply touch when direct tactile sensing is limited.

</details>

---

### [[20_Research/Papers/具身智能/Pedicel-Targeted_Strawberry_Harvesting_via_Imitation_Learning_on_a_Low-Cost_Teleoperated_Robotic_Arm|Pedicel-Targeted Strawberry Harvesting via Imitation Learning on a Low-Cost Teleoperated Robotic Arm]]

![[assets/2610.22765_figure.png|800]]

- **arXiv**: [2610.22765](https://arxiv.org/abs/2610.22765)
- **PDF**: https://arxiv.org/pdf/2610.22765
- **详细分析**: [[20_Research/Papers/具身智能/Pedicel-Targeted_Strawberry_Harvesting_via_Imitation_Learning_on_a_Low-Cost_Teleoperated_Robotic_Arm|Pedicel-Targeted Strawberry Harvesting via Imitation Learning on a Low-Cost Teleoperated Robotic Arm]]
- **作者**: Nitin Rai, Won Suk Lee, Hongyoung Leon, Heping Zhu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Pedicel-Targeted Strawberry Harvesting via Imitation Learning on a Low-Cost Teleoperated Robotic Arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precise pedicel-targeted grasping in strawberry harvesting remains a critical bottleneck due to the pedicel's small diameter (1.3-3 mm), color similarity with surrounding foliage, and precise force control required for clean abscission zone detachment. As a market-grade crop, strawberry aesthetic value makes bruise-free pedicel detachment essential over direct fruit grasping. Classical approaches struggle to unify vision models, motion planning, and contact manipulation into a robust framework, particularly in occluded canopy environments. Therefore, this work presents a visuomotor imitation learning pipeline for pedicel-targeted strawberry harvesting that unifies perception, motion planning, and contact manipulation from collecting human teleoperation demonstrations, training an Action Chunking with Transformers (ACT) policy with a ResNet-50 visual backbone, and deploying the learned policy autonomously on a Jetson AGX Orin edge platform at 15 Hz. The trained policy achieved consistent loss convergence from 2.84 to 0.091 over 100K gradient steps on 130 demonstrations. We have also established a reproducible open-source pipeline with publicly released dataset and model weights for the agricultural robotics community. Full dataset is available at, https://huggingface.co/datasets/nitindominicrai/strawberry_pedicel_grasp_teleoperation and trained policy at, https://huggingface.co/nitindominicrai/act_strawberry_pedicel. To replicate this work, all code, configurations, and deployment instructions are publicly available at, https://github.com/nitin-dominic/autonomous_strawberry_pedicel_harvesting.

</details>

---

### [[20_Research/Papers/机器人/Task_Structure_and_Scalability_in_Multi-Robot_Authoring|Task Structure and Scalability in Multi-Robot Authoring]]

![[assets/2610.22670_figure.png|800]]

- **arXiv**: [2610.22670](https://arxiv.org/abs/2610.22670)
- **PDF**: https://arxiv.org/pdf/2610.22670
- **详细分析**: [[20_Research/Papers/机器人/Task_Structure_and_Scalability_in_Multi-Robot_Authoring|Task Structure and Scalability in Multi-Robot Authoring]]
- **作者**: Christian Marowski, Byung-Cheol Min
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Task Structure and Scalability in Multi-Robot Authoring》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot authoring can reduce completion time by distributing drawing work, but the resulting speedup depends on task structure and the allocation-routing pipeline. We investigate these relationships by representing drawings as geometric stroke graphs and comparing component-level (single-token) allocation with shared-token (decomposed) allocation, which permits multiple robots to work within a connected component. A simulation study of 385 drawings and teams of one to eight robots shows diminishing speedup gains under single-token allocation and larger mean speedups under the shared-token pipeline, each normalized by its own single-robot completion time. Shared-token execution also exhibits lower idle-time shares at larger team sizes, although it does not reduce completion time for every drawing. Comparisons across structural attribute groups reveal associations between structural descriptors and differences in scaling behavior, with greater separation between several attribute groups at larger team sizes. These findings characterize empirical scaling in the evaluated pipelines and highlight the importance of considering within-component workload and graph structure alongside component count. Additional materials are available at https://sites.google.com/view/multirobotauthoring/home.

</details>

---

### [[20_Research/Papers/具身智能/FCTS_Failure-Guided_Curriculum_Tree_Search_Over_Generated_Terrain_for_Legged_Parkour|FCTS: Failure-Guided Curriculum Tree Search Over Generated Terrain for Legged Parkour]]

![[assets/2610.22619_figure.png|800]]

- **arXiv**: [2610.22619](https://arxiv.org/abs/2610.22619)
- **PDF**: https://arxiv.org/pdf/2610.22619
- **详细分析**: [[20_Research/Papers/具身智能/FCTS_Failure-Guided_Curriculum_Tree_Search_Over_Generated_Terrain_for_Legged_Parkour|FCTS: Failure-Guided Curriculum Tree Search Over Generated Terrain for Legged Parkour]]
- **作者**: Narayanan Palghat Parameswaran, Dong-Ki Kim, Jay Patrikar, Santiago Gutierrez, Harshad Zade, Shayegan Omidshafiei, Harmish Khambhaita
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《FCTS: Failure-Guided Curriculum Tree Search Over Generated Terrain for Legged Parkour》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped parkour policies handle canonical obstacles well, but their training curricula often miss the irregular, compound geometry of industrial and disaster-response sites, where agile locomotion matters most. Such environments pose a hard generalization problem: even training directly on reconstructed geometry from the target site does not reliably yield policies that traverse it. Hand-designed curricula span only a few terrain families, and recent LLM-generated curricula offer little control over which policy weaknesses they target. We propose FCTS, a failure-conditioned terrain curriculum framework that uses localized traversal failures to automatically generate the terrains a policy should train on next. Each failure's location, termination mode, robot state, and surrounding terrain geometry condition this generation, and Monte Carlo Tree Search explores alternative curriculum trajectories under a fixed training budget. On terrains built from scanned real-world construction sites, FCTS raises success rate from 28.4% to 85.8% on a medium-difficulty course and from 14.9% to 44.7% on a hard course relative to the strongest parkour or LLM-curriculum baselines, and maintains higher progress on extreme terrains where full traversal is rare. Hardware experiments on a quadruped robot confirm that the learned FCTS policies transfer to the real world.

</details>

---

### [[20_Research/Papers/机器人/RTISSLAM-3D_Full_6-DoF_SLAM_With_an_In-Air_3D_Imaging_Sonar|RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar]]

![[assets/2610.22552_figure.png|800]]

- **arXiv**: [2610.22552](https://arxiv.org/abs/2610.22552)
- **PDF**: https://arxiv.org/pdf/2610.22552
- **详细分析**: [[20_Research/Papers/机器人/RTISSLAM-3D_Full_6-DoF_SLAM_With_an_In-Air_3D_Imaging_Sonar|RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar]]
- **作者**: Jan Steckel, Vincent Katter, Wouter Jansen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《RTISSLAM-3D: Full 6-DoF SLAM With an In-Air 3D Imaging Sonar》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Echolocating bats navigate dense forests using sonar alone, and in-air 3D imaging sonars now capture the entire frontal hemisphere with every pulse. Sonar SLAM, however, has so far been planar: current systems estimate a 2D trajectory and discard the elevation information in the sonar images, an assumption that does not hold on rough and sloped terrain such as a forest floor. In this paper, we introduce RTISSLAM-3D, a novel 6-DoF SLAM system for a wheeled robot that carries an in-air 3D imaging sonar, an IMU and wheel encoders. A CFAR detector on the sphere reduces every sonar image to a sparse set of 3D detections, which we use for a 3D acoustic odometry that models the shape of the sonar beam, for place recognition with polar submap descriptors, and for the verification of loop closures by 3D registration, all combined in a 6-DoF pose graph with attitude factors. We evaluated RTISSLAM-3D on a 545m drive through a forest, with a 3D lidar SLAM as reference. The loop closures reduced the horizontal error of the acoustic odometry from 1.74m to 0.28m, with a height error of 0.12m, and 94.6% of the resulting 3D sonar map lies within 0.3 m of the lidar map.

</details>

---

### [[20_Research/Papers/强化学习/Scaling_Online_Exploration_for_Robot_Agents|Scaling Online Exploration for Robot Agents]]

![[assets/2610.22496_figure.png|800]]

- **arXiv**: [2610.22496](https://arxiv.org/abs/2610.22496)
- **PDF**: https://arxiv.org/pdf/2610.22496
- **详细分析**: [[20_Research/Papers/强化学习/Scaling_Online_Exploration_for_Robot_Agents|Scaling Online Exploration for Robot Agents]]
- **作者**: Runhan Huang, Xiangcheng Zhang, Haoyu Chen, Yitong Li, Yen-Jen Wang, Bohan Lyu, Haotian Ye, Chuye Hong, Yixuan Wang, Chloe Su, Haoyu Xiong, Yangzhen Wu...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.9，大模型 0.5，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Scaling Online Exploration for Robot Agents》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ManipulationNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot learning has advanced by scaling demonstration datasets and model capacity; however, deploying a new robot embodiment or task typically necessitates a dedicated teleoperation corpus. The resulting policies remain bounded by their imitation distributions, limiting generalization and continual self-improvement. We introduce RAX (Robot Agent eXploration), an open-source framework for robot agents centered on scaling exploration: enabling agents to improve by acquiring online experience and synthesizing executable programs. In RAX, a general-purpose coding agent generates robot control code, operating without action demonstration data, hand-engineered action primitives, or value-function guidance. Through online exploration, the agent identifies decision sequences that achieve task goals and compiles them into modular programs encapsulating the full perception-planning-control loop. Using RAX, we present a systematic multi-embodiment study on scaling online exploration across precision and long-horizon manipulation tasks using single-arm, bimanual, dexterous, mobile, and humanoid systems in simulation and on real robots. Generalization performance on unseen environments improves consistently as exploration scales. In simulation, RAX outperforms top baseline models by +37.4% on average. On real robots, RAX autonomously learns memory-dependent, articulated, high-precision, deformable, and long-horizon mobile manipulation tasks without human demonstrations, continually improving performance by composing verified skills from prior exploration sessions. As exploration scales, we observe emergent capabilities including active perception, error recovery, safety guardrails, and human-robot collaboration. We open-source RAX as a generalist robot-agent platform in which new robot embodiments are integrated through their APIs alone, without teleoperated data collection or policy training.

</details>

---

### [[20_Research/Papers/具身智能/Mothership_A_Two_Tier_Autonomous_Refuse_Collection_System_for_Pedestrian_Campuses|Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses]]

![[assets/2610.22461_first_page.png|800]]

- **arXiv**: [2610.22461](https://arxiv.org/abs/2610.22461)
- **PDF**: https://arxiv.org/pdf/2610.22461
- **详细分析**: [[20_Research/Papers/具身智能/Mothership_A_Two_Tier_Autonomous_Refuse_Collection_System_for_Pedestrian_Campuses|Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses]]
- **作者**: Wei Wang, Yiru Veronika Wang, Yihan Wang, Zihao Li, Xiaohui Liang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Mothership: A Two Tier Autonomous Refuse Collection System for Pedestrian Campuses》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Refuse collection in pedestrian campuses, parks and mixed-use districts remains manual because compaction trucks cannot reach bins located on walkways, courtyards and building service doors. This paper presents Mothership, a two-tier autonomous refuse collection system in which an electric compaction truck (the mothership) carries two low-speed sidewalk robots (RoboCarts) that fetch standard two-wheel bins, deliver them to the truck, return the empty bins to their original positions and re-dock on the truck for charging. The architecture separates responsibilities by scale: the truck performs road driving, compaction, lifting and energy supply, while the carts perform only sidewalk transport and bin grasping. This split removes the lift-and-tip mechanism from the sidewalk vehicle, keeping it light and low, and relaxes cart-to-truck docking tolerance to the +/-100 mm capture window of a standard automated lifter. We describe the system architecture, the bin-handling and docking interfaces, and a mission-planning formulation that decomposes a route into truck stop points and cart tasks. A discrete-event simulation over synthetic campus layouts with 2-16 bins/ha quantifies throughput as a function of bin density, cart count and stop-point radius. A two-cart configuration serves 20-29 bins/h. Throughput is governed by an interaction between cart count and stop-point radius: a single cart performs best with many close stops, whereas three or four carts need wide stops (80 m) to stay busy, reaching 35-49 bins/h at moderate-to-high densities. The best stop radius therefore has to be chosen together with the fleet size, not fixed in advance.

</details>

---
