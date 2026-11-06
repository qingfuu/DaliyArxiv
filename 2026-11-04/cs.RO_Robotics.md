# cs.RO | Robotics | 2026-11-04

#arxiv #ComputerScience

**论文数**: 30

### [[20_Research/Papers/机器人/PACT_Pose-Robust_Actuation_Co-Design_for_Tendon-Driven_Robotic_Hands|PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands]]

![[assets/2611.05302_figure.png|800]]

- **arXiv**: [2611.05302](https://arxiv.org/abs/2611.05302)
- **PDF**: https://arxiv.org/pdf/2611.05302
- **详细分析**: [[20_Research/Papers/机器人/PACT_Pose-Robust_Actuation_Co-Design_for_Tendon-Driven_Robotic_Hands|PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands]]
- **作者**: Prashant Kumar, Rachael Granberry, Taylor Niehues, Andrew A. Stanley, Gabe Pirie
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Force-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robotic hands must provide sufficient force, speed, and backdrivability within a human-scale envelope. Tendon-driven transmissions address this challenge by relocating actuators to the palm and forearm, but routing paths, moment arms, and capstan dimensions jointly determine both force capability and joint speed, so selecting them sequentially satisfies one requirement at the expense of the other. This paper presents a pose-robust actuation co-design for tendon-driven robot hands (PACT) framework that optimizes tendon routing, moment arms, and capstan dimensions under pose-dependent force requirements and drivetrain-bandwidth constraints. A feasible-force formulation enforces actuator bounds and equilibrium at all joints, while a max-min objective maximizes task-force coverage at the weakest pose. Applied to a four-degree-of-freedom finger, the framework produces an asymmetric N + 1 tendon topology using quasi-direct-drive actuators. Across eight poses, the design achieves task-force coverage of 0.88-1.00 and a predicted 5 Hz minimum isolated-joint flexion/extension bandwidth within a 70th-percentile human-size envelope. Prototype measurements deviate from predictions by up to 24.5%, primarily due to unmodeled transmission losses. These results indicate that co-designing routing with the drivetrain can meet pose-dependent force requirements without relaxing the bandwidth constraint, paving the way for human-sized robotic hands with human-level performance.

</details>

---

### [[20_Research/Papers/具身智能/Should_the_Action_Expert_Train_the_VLM_Action-Token_Supervision_and_Gradient_Routing_in_Mixture-of-Transformer_VLAs|Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs]]

![[assets/2611.05249_figure.png|800]]

- **arXiv**: [2611.05249](https://arxiv.org/abs/2611.05249)
- **PDF**: https://arxiv.org/pdf/2611.05249
- **详细分析**: [[20_Research/Papers/具身智能/Should_the_Action_Expert_Train_the_VLM_Action-Token_Supervision_and_Gradient_Routing_in_Mixture-of-Transformer_VLAs|Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs]]
- **作者**: Asher James Hancock, Boyi Li, Yuxiao Chen, Shuhan Tan, Wenhao Ding, Thomas Tian, Yan Wang, Boris Ivanovic, Marco Pavone
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Should the Action Expert Train the VLM? Action-Token Supervision and Gradient Routing in Mixture-of-Transformer VLAs》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutoVLA, DexVLA, HybridVLA, OpenDriveVLA, OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models increasingly pair a pre-trained vision-language model (VLM) with a flow-matching expert that conditions its action predictions on the VLM's key-value representations. Those representations must carry information useful for control, yet the VLM was never trained for the action expert's flow-matching objective. Two signals can address this: gradients backpropagated from the expert's loss (coupling), or VLM supervision to predict discrete tokens encoding the same target actions. Prominent training recipes forgo the first, blocking expert-to-VLM gradients (insulation) to protect the VLM's existing capabilities, while also supervising it on vision-language data and action tokens. Because vision-language co-training also aims to preserve those capabilities, the additional protection provided by insulation is unclear. At the same time, insulation removes a direct signal about which features continuous action prediction requires. On the other hand, action-token supervision offers an alternative way to learn action-relevant representations, which may explain why insulation succeeds in practice. We disentangle these factors in autonomous driving and manipulation by independently varying action-token supervision and whether the expert's loss updates the VLM. In open-loop driving, insulation is competitive with coupling when action tokens are supervised; without them, coupling reduces trajectory-prediction error by roughly 25%. When both components are trained jointly from the outset, coupling increases closed-loop driving route progress by approximately 17% with action-token supervision and 40% without it, and similarly improves robot manipulation performance under both settings. These findings show that the value of gradient insulation depends on the VLM's action supervision and the evaluation setting, challenging insulation as a default VLA training recipe.

</details>

---

### [[20_Research/Papers/机器人/Reality_and_Perceptual_Gaps_in_Expressive_Swarm_Robotics|Reality and Perceptual Gaps in Expressive Swarm Robotics]]

![[assets/2611.05244_figure.jpg|800]]

- **arXiv**: [2611.05244](https://arxiv.org/abs/2611.05244)
- **PDF**: https://arxiv.org/pdf/2611.05244
- **详细分析**: [[20_Research/Papers/机器人/Reality_and_Perceptual_Gaps_in_Expressive_Swarm_Robotics|Reality and Perceptual Gaps in Expressive Swarm Robotics]]
- **作者**: Ali Imran, Abdalwhab Bakheet Mohammed Abdalwhab, Rafael Gomes Braga, Hélène Duval, Audrey Rochette, Vivek Shankar Varadhajan, Yann Bouteiller, Jean Mazerolle, Giovanni Beltrame, David St-Onge
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Reality and Perceptual Gaps in Expressive Swarm Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Moving robot swarms from simulation into the physical world can be difficult because small discrepancies in hardware, timing and communication can cascade across interacting robots and alter group behaviour. This challenge is known as the reality gap. When swarms operate in human environments, a second challenge emerges: a perceptual gap between what the swarm physically does and what human onlookers actually perceive. This study examines the same decentralised coordination code deployed across three robotic swarms-tabletop, aerial and human-scale mobile manipulators-during live artistic performances. We find that while the underlying algorithms executed reliably on all three platforms, physical embodiment drastically altered visible motion-distorting execution timescales by more than a factor of three and reshaping trajectory geometry. More importantly, audience surveys revealed that human interpretation does not mirror technical success: how observers attribute meaning (perceived purpose) and how they react emotionally (comfort versus threat) depend heavily on physical form. Meaning attribution and emotional responses did not vary together. Our results demonstrate that successfully transferring swarm software to physical hardware is insufficient for real-world deployment. Addressing the reality gap does not guarantee that the resulting collective motion will be readily interpreted by human observers. Swarms destined for human environments must be engineered not only for decentralised stability but also for the expressive physical dynamics through which humans interpret collective motion.

</details>

---

### [[20_Research/Papers/具身智能/WayTrace_A_Map-to-Language-to-Trace_Hierarchy_for_Embodied_Urban_Navigation|WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation]]

![[assets/2611.05129_figure.png|800]]

- **arXiv**: [2611.05129](https://arxiv.org/abs/2611.05129)
- **PDF**: https://arxiv.org/pdf/2611.05129
- **详细分析**: [[20_Research/Papers/具身智能/WayTrace_A_Map-to-Language-to-Trace_Hierarchy_for_Embodied_Urban_Navigation|WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation]]
- **作者**: Manthan Patel, Jonas Frey, Pascal Roth, Marco Hutter, Cesar Cadena
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《WayTrace: A Map-to-Language-to-Trace Hierarchy for Embodied Urban Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AsyncVLA, Real-World, TIC-VLA, UrbanVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web services provide walking directions for nearly every city, but following them reliably over long routes remains challenging for autonomous robots. Point-goal navigation policies rely heavily on accurate GNSS, while most vision-language navigation models struggle to execute even short instructions outdoors. We present WayTrace, a hierarchical system that connects web-map directions to robot motion through language. An off-the-shelf orchestrator vision-language model reads the turn-by-turn directions, a satellite map and recent camera images, and issues one atomic language command at a time, such as "cross the road to the left". An onboard trace predictor, trained on over one million automatically labelled samples from street-level images, draws the path for this command in the image, and a reinforcement learning policy tracks it. In long-range simulated missions, WayTrace remains robust to GNSS noise and rarely leaves crosswalks or sidewalks, while point-goal baselines degrade sharply with about ten times more violations. Deployed on a wheeled-legged robot, WayTrace completes real-world missions of up to 1.37 km at about 1.1 m/s through a busy city centre, rural trails and a university campus, handling crosswalks, staircases and construction sites. Project page: https://way-trace.github.io

</details>

---

### [[20_Research/Papers/强化学习/DexHOT_Learning_Hand-Object_Configuration_Transfer_for_Dexterous_Manipulation|DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation]]

![[assets/2611.05119_figure.png|800]]

- **arXiv**: [2611.05119](https://arxiv.org/abs/2611.05119)
- **PDF**: https://arxiv.org/pdf/2611.05119
- **详细分析**: [[20_Research/Papers/强化学习/DexHOT_Learning_Hand-Object_Configuration_Transfer_for_Dexterous_Manipulation|DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation]]
- **作者**: Zhewei Gui, Anthony Bolton, Jiyao Zhang, Zeyuan Chen, Qiyang Yan, Tianyu Wang, Hao Dong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexHOT: Learning Hand-Object Configuration Transfer for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DexHOTBench, DexRepNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation involves not only moving objects, but also arranging the hand around them to maintain useful contacts and enable subsequent actions. Yet many learning-based systems specify goals primarily through object poses or trajectories, leaving hand-object configurations to emerge implicitly. We introduce DexHOT, which formulates dexterous manipulation as hand-object configuration transfer: moving between feasible configurations that jointly specify hand articulation and object pose relative to the wrist. DexHOT learns a reusable relation-conditioned transfer primitive from synthetic feasible configuration pairs, without human reference motions, and composes long-horizon behaviors through closed-loop tracking of configuration subgoals. On DexHOTBench with 120 objects, a single policy achieves 80.5% transfer success on seen objects and 69.4% on unseen objects; on a real dexterous hand, it achieves 61.5% success over 200 real-robot transfers and 90% task success across six demonstration-guided tasks. These results show that explicit hand-object goals provide an expressive and composable interface for dexterous manipulation. More details and videos are available at https://dex-hot.github.io/.

</details>

---

### [[20_Research/Papers/强化学习/HLO-AMP_Hierarchical_Loco-Manipulation_from_Object-Aware_Motion_Priors|HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors]]

![[assets/2611.05113_figure.png|800]]

- **arXiv**: [2611.05113](https://arxiv.org/abs/2611.05113)
- **PDF**: https://arxiv.org/pdf/2611.05113
- **详细分析**: [[20_Research/Papers/强化学习/HLO-AMP_Hierarchical_Loco-Manipulation_from_Object-Aware_Motion_Priors|HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors]]
- **作者**: Jean-Pierre Sleiman, Bilal Hammoud, He Li, Jonathan Foster, Sylvain Bertrand, Jessica K. Hodgins, Farbod Farshidian
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《HLO-AMP: Hierarchical Loco-Manipulation from Object-Aware Motion Priors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical pipelines for humanoid loco-manipulation typically pair a task-agnostic whole-body controller (WBC) with a downstream task policy. Such WBCs are often trained through manual reward shaping, which yields visibly machine-like motions; more consequentially, they are trained without the manipulated object in the scene. Object dynamics are instead approximated through randomized end-effector force disturbances, a proxy that fails to reproduce the distributed multi-contact wrench a real payload applies across the arms and torso, with the gap becoming critical near the platform's payload limit. In this work, we train the low-level (LL) controller itself as an object-aware motion prior: a single policy trained via motion imitation on retargeted motion-capture (MoCap) references that span the core motion primitives of the downstream task, with the manipulated object physically present in the scene. This single stage inherits natural human-like coordination from the references and absorbs the realistic contact wrench at its source, while exposing the same compact task-space command interface used by command-tracking WBCs. A reference-free high-level (HL) policy is then trained on top, with its action channel anchored to the empirical envelope of the low-level training data so that it generalizes the priors to a long-horizon multi-stage task while structurally preventing queries that would push the low level off-distribution. We instantiate the framework on a Unitree G1 for bimanual box pick-and-place: the same deployed policy generalizes across object masses and dimensions, initial and goal poses, and reactively recovers from intentional drops mid-carry. Video: https://youtu.be/viR_ULnRDQQ.

</details>

---

### [[20_Research/Papers/具身智能/LoopQ_Fair,_Closed-Loop_Evaluation_of_Quantized_Vision-Language-Action_Models|LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models]]

![[assets/2611.05093_figure.png|800]]

- **arXiv**: [2611.05093](https://arxiv.org/abs/2611.05093)
- **PDF**: https://arxiv.org/pdf/2611.05093
- **详细分析**: [[20_Research/Papers/具身智能/LoopQ_Fair,_Closed-Loop_Evaluation_of_Quantized_Vision-Language-Action_Models|LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models]]
- **作者**: Syed Umer Bukhari, Magnus Almgren, Ahmed Ali-Eldin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《LoopQ: Fair, Closed-Loop Evaluation of Quantized Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HoloQ-VLA, OpenVLA, QVLA, QuantVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training quantization (PTQ) for vision-language-action (VLA) models promises smaller and faster VLA deployments. However, when analyzing existing VLA quantization works, we realised that it is hard to reason about the performance of the suggested quantization method compared to existing, similar, or in many cases, simpler PTQ methods. We present LoopQ, a closed-loop benchmark that compares multiple quantization policies on the same checkpoint, layers and engine, varying only the method and the kernels. We evaluate RTN, AWQ, GPTQ, ActQuant and QuantVLA on four VLAs with more than 180,000 episodes of LIBERO and LIBERO-plus, compare against QVLA's reported results on the same layers, and benchmark whether the four public VLA-quantization releases can be reproduced. We benchmark the methods on an NVIDIA H100, an L4, and a Jetson AGX Thor. Our results show that while quantization reliably saves memory, 2-3x for real low-bit models, VLA-specific PTQ methods underperform compared to simpler generic baselines. At 4 bits, RTN, AWQ and GPTQ match or exceed ActQuant and QuantVLA, plain RTN matches the calibrated methods, and plain AWQ matches the success QVLA reports for itself. Standard LIBERO hides the losses that do exist: configurations with no significant LIBERO loss lose 1.5-4.3 points under paired LIBERO-plus perturbations. Speed is a weaker story. At batch 1 on the H100, no quantized pi0.5 or OpenVLA-OFT configuration is faster than its 16-bit model (1.06-1.58x slower on library kernels); only the L4 with int8 kernels gains (4-14%), the Thor is slower on every 4-bit configuration, and the engine alone changes latency by 2.1x. Profiling explains why: pi0.5's quantized backbone is compute-bound, while its memory-bound action expert, 63% of GPU time and 13% of the parameters, stays in 16 bits.

</details>

---

### [[20_Research/Papers/机器人/Nested_Field-of-View_Barriers_for_Teleoperated_Multi-Robot_Relay_Chains|Nested Field-of-View Barriers for Teleoperated Multi-Robot Relay Chains]]

![[assets/2611.05074_figure.png|800]]

- **arXiv**: [2611.05074](https://arxiv.org/abs/2611.05074)
- **PDF**: https://arxiv.org/pdf/2611.05074
- **详细分析**: [[20_Research/Papers/机器人/Nested_Field-of-View_Barriers_for_Teleoperated_Multi-Robot_Relay_Chains|Nested Field-of-View Barriers for Teleoperated Multi-Robot Relay Chains]]
- **作者**: Arthur Vangasse, Theo Cruz, Thales Soares, André Cid, Vinícius Gonçalves, Gustavo Freitas, Luciano Pimenta
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Nested Field-of-View Barriers for Teleoperated Multi-Robot Relay Chains》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teleoperation of mobile robots in communication-denied environments requires maintaining a communication link while allowing the operator to maneuver freely. We propose a shared-autonomy framework in which a teleoperated leader is followed by a chain of autonomous robots that relays a line of sight to a fixed base station, a geometric proxy for the link. Connectivity is enforced geometrically through visibility-based Control Barrier Functions (CBFs), with each agent computing its control input locally through a quadratic program. A strict visibility constraint guarantees connectivity, but a follower with no independent motion objective remains stationary, stalling the leader at the boundary of the safe set. Relaxing it preserves mobility at the cost of the guarantee. Our framework resolves this conflict through nested hard-soft visibility constraints: a full field-of-view (FoV) constraint enforced strictly to guarantee connectivity and a contracted FoV constraint imposed on each follower as a relaxed behavioral objective that drives it inward before the connectivity boundary is reached. We prove feasibility of the local quadratic programs and forward invariance of the connected, collision-free set under the resulting distributed controller. The contraction parameter shapes follower behavior without affecting the guarantee, which follows from the strict constraint alone. The framework is evaluated in confined and cluttered environments on two simulated systems: a kinematic integrator and software-in-the-loop Crazyflie quadrotors. Compared with a baseline tuned to reach the goal in comparable time, the framework keeps the links far closer to the connected set and moves the followers less.

</details>

---

### [[20_Research/Papers/具身智能/HiLo-WAM_Decoupling_Long-Horizon_Task_Evolution_and_Local_Dynamics_in_World_Action_Models|HiLo-WAM: Decoupling Long-Horizon Task Evolution and Local Dynamics in World Action Models]]

![[assets/2611.05023_figure.png|800]]

- **arXiv**: [2611.05023](https://arxiv.org/abs/2611.05023)
- **PDF**: https://arxiv.org/pdf/2611.05023
- **详细分析**: [[20_Research/Papers/具身智能/HiLo-WAM_Decoupling_Long-Horizon_Task_Evolution_and_Local_Dynamics_in_World_Action_Models|HiLo-WAM: Decoupling Long-Horizon Task Evolution and Local Dynamics in World Action Models]]
- **作者**: Xingyu Wang, Yanjiang Guo, Zhijing Ding, Jiaxin Fang, Zeyu Lai, Jiayu Dong, Weikang Wan, Jianyu Chen, Yuxiang Gao, Mengdi Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《HiLo-WAM: Decoupling Long-Horizon Task Evolution and Local Dynamics in World Action Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) improve robotic manipulation by jointly modeling visual dynamics and robot actions. However, most existing WAMs model dense short-horizon visual dynamics, capturing local interactions but providing limited long-range task context. Extending prediction horizons increases uncertainty and computation while entangling task-level evolution with fine-grained local dynamics, obscuring their dependencies and distinct roles in action generation. We propose HiLo-WAM, which decouples long-horizon task evolution from local visual dynamics while jointly modeling their interaction with robot actions. A sparse long-horizon visual stream captures historical task context and future evolution, while a dense local dynamics visual stream models short-horizon robot-object interactions. The two streams operate at different temporal scales within a unified dual-DiT architecture and guide actions through structured cross-stream attention. Progressive inference further reduces unnecessary computation through stream-wise partial denoising, joint denoising, and dynamic skipping. Experiments demonstrate strong long-horizon manipulation performance: HiLo-WAM achieves a 93.70% average success rate on RoboTwin 2.0 and a 17.43 progress score on RoboDojo long-horizon tasks, with robust in-domain and OOD performance on the Fourier GR-3 robot. Ablations confirm the complementary contributions of long-horizon task evolution and local interaction dynamics, while temporal-scale analyses highlight the importance of balancing temporal coverage and resolution. Progressive inference further achieves a 2.93x speedup while improving performance.

</details>

---

### [[20_Research/Papers/具身智能/Caging_Vision-Language_Navigation_for_Legged_Robots_via_Barrier-Certified_Safety_Architecture|Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture]]

![[assets/2611.04972_figure.png|800]]

- **arXiv**: [2611.04972](https://arxiv.org/abs/2611.04972)
- **PDF**: https://arxiv.org/pdf/2611.04972
- **详细分析**: [[20_Research/Papers/具身智能/Caging_Vision-Language_Navigation_for_Legged_Robots_via_Barrier-Certified_Safety_Architecture|Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture]]
- **作者**: Abhijeet M. Kulkarni, Saimouli Katragadda, Yuze Du, Zijun Sha, Guoquan Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Caging Vision-Language Navigation for Legged Robots via Barrier-Certified Safety Architecture》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：QUAR-VLA, SafeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

By harnessing the inherent commonsense capabilities of pretrained Large Language Models (LLMs) and Vision-Language Models (VLMs), current Vision-Language Action(VLA) models for legged robots excel at interpreting language-based navigation commands but lack the physical grounding and explicit safety assurance required for real-world operation. Therefore, this paper aims to cage Legged-Vision-Language Navigation (VLN) through a safety architecture that provides physical grounding and ensures navigation safety. The key idea is not to abandon the powerful capabilities of end-to-end VLA planning, but rather to augment and cage them. In particular, we integrate a high-level VLA planner with a low-level physical-grounding layer that leverages efficient state estimation, in-situ 3D spatial perception, and an Signed Distance Field (SDF) representation to generate executable trajectories. We provide a navigation planner with provable collision-avoidance guarantees under the stated assumptions by combining a low-dimensional Bezier-parameterized MPPI planner with Discrete Exponential Barrier Function (dEBF) constraints. The proposed Legged-VLN system is modular, making it compatible with various VLM/VLA models and agnostic to the robot platform. The proposed system is validated with extensive real-world experiments on humanoid and quadrupedal robots, demonstrating versatile, efficient, and safe vision-language driven navigation capabilities.

</details>

---

### [[20_Research/Papers/强化学习/Safeguarding_Multi-Agent_Reinforcement_Learning_for_Connected_and_Automated_Vehicles_with_Recursively_Feasible_Control_Barrier_Functions|Safeguarding Multi-Agent Reinforcement Learning for Connected and Automated Vehicles with Recursively Feasible Control Barrier Functions]]

![[assets/2611.04957_figure.png|800]]

- **arXiv**: [2611.04957](https://arxiv.org/abs/2611.04957)
- **PDF**: https://arxiv.org/pdf/2611.04957
- **详细分析**: [[20_Research/Papers/强化学习/Safeguarding_Multi-Agent_Reinforcement_Learning_for_Connected_and_Automated_Vehicles_with_Recursively_Feasible_Control_Barrier_Functions|Safeguarding Multi-Agent Reinforcement Learning for Connected and Automated Vehicles with Recursively Feasible Control Barrier Functions]]
- **作者**: Jianye Xu, Yousef Sayed, Bassam Alrifaee
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Safeguarding Multi-Agent Reinforcement Learning for Connected and Automated Vehicles with Recursively Feasible Control Barrier Functions》归入 强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Agent Reinforcement Learning (MARL) shows promise in coordinating connected and automated vehicles but offers no safety guarantee. Although Control Barrier Functions (CBFs) can add this guarantee, their optimization problem can become infeasible in practice due to control bounds. Moreover, they often overapproximate vehicle and road geometry, which makes them conservative. This paper proposes the Backup-Horizon CBF (BH-CBF), which evaluates safety along a horizon until all vehicles stop. BH-CBF is recursively feasible under control bounds, and it considers the exact vehicle and road geometry. Based on BH-CBF, we derive a fully decentralized safety filter that only needs a single broadcast of vehicle states and routes per step and stays real-time in dense traffic. We use BH-CBF to safeguard a MARL policy over its life cycle: as a reward during pre-training, as a run-time filter at deployment, and as a filter in the training loop that keeps fine-tuning on unseen maps collision-free. In simulations on real-world maps of a roundabout and an intersection, BH-CBF avoids all collisions of unsafe MARL policies and keeps its safety guarantee at every step. Existing filters either collide, lose the guarantee, or fall back to full braking far more often. In recorded roundabout traffic with 1264 human-driven vehicles over 115 km, our safeguarded policies shorten the median travel time by 14% compared with the human drivers, without any collision.

</details>

---

### [[20_Research/Papers/强化学习/PrimeSim_A_Generalist_World_Model_Simulator_from_Large-Scale_Cross-Embodiment_Demonstrations|PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations]]

![[assets/2611.04870_figure.png|800]]

- **arXiv**: [2611.04870](https://arxiv.org/abs/2611.04870)
- **PDF**: https://arxiv.org/pdf/2611.04870
- **详细分析**: [[20_Research/Papers/强化学习/PrimeSim_A_Generalist_World_Model_Simulator_from_Large-Scale_Cross-Embodiment_Demonstrations|PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations]]
- **作者**: Travis Davies, Wentao Ma, Lihao Guo, Tengfei Ma, Xiaowen Chang, Jiafeng Xu, Shilong Wang, Yiqi Deng, Shaowen He, Xiaoqi Li, Qian Zhu, Ran Cheng...
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.0（加权：具身智能 0.3，强化学习 0.2，世界模型 1，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《PrimeSim: A Generalist World Model Simulator from Large-Scale Cross-Embodiment Demonstrations》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, EWMBench, GE-Sim, PrimeSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot world model that serves as a simulator must do more than generate plausible videos: it must faithfully follow commanded actions, maintain consistency across camera views, and sustain coherent long-horizon rollouts. We present PrimeSim, an action-conditioned, multiview world model simulator that addresses these challenges through progressive midtraining and posttraining. Starting from a pretrained video generator, we midtrain on 30,110 hours of robot demonstrations spanning 22 platforms. To improve action following, we introduce a unified cross-embodiment action representation and frame-aligned dual-path conditioning to strengthen action-frame correspondence. To maintain multiview consistency, we develop view-aware interleaved attention with explicit camera identities, enabling cross-view information exchange while preserving view-specific representations. We further introduce a fast-video, slow-memory posttraining framework that transforms the bidirectional video generator into an efficient autoregressive simulator. By combining fast causal generation, self-rollout training, and hierarchical temporal memory, PrimeSim mitigates error accumulation from self-generated histories and supports coherent long-horizon simulation. PrimeSim runs at 10.1 FPS, remains stable over long-horizon rollouts on rigid and deformable manipulation tasks, and transfers to held-out platforms within 100 to 200 gradient steps where the pretrained backbone does not. Against five open-source action-conditioned world models it leads four of the five WorldSimProbe suites and posts the best overall EWMBench score, while fine-grained local calibration still trails the field; its rollouts are faithful enough to support GRPO-based policy optimization. We release the model weights, inference code, and training code.

</details>

---

### [[20_Research/Papers/机器人/Coordinating_Humanoid_Loco-Manipulation_through_Action-Conditioned_Latent_Foresight|Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight]]

![[assets/2611.04839_figure.png|800]]

- **arXiv**: [2611.04839](https://arxiv.org/abs/2611.04839)
- **PDF**: https://arxiv.org/pdf/2611.04839
- **详细分析**: [[20_Research/Papers/机器人/Coordinating_Humanoid_Loco-Manipulation_through_Action-Conditioned_Latent_Foresight|Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight]]
- **作者**: Ju Dong, Xinyu Xiao, Yiming Zhou, Tianshuo Yang, Xuerong Liu, Lei Zhang, Jian Chen, Haocheng Zhao, Yu Fu, Yujie Wei, Diwen Zheng, Alois Christian Knoll...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Coordinating Humanoid Loco-Manipulation through Action-Conditioned Latent Foresight》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EgoVLA, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation requires coordinated body motion and hand interaction over time, and a plausible-looking command sequence can still drop a held object or leave an interaction incomplete. We present action-conditioned latent foresight, a latent world-action model (WAM) that evaluates proposed command sequences before execution. An action generator proposes joint motion-hand command sequences from vision, language, and the robot state. An action-conditioned endpoint predictor estimates the visual features each sequence prefix reaches and measures progress toward a demonstration-derived subgoal, while a joint temporal prior scores temporal consistency given the robot state and preceding commands. The robot executes the first commands of the best-scoring sequence and replans from the next observation. During training, action consistency regularization reconstructs the first demonstrated command from observed and predicted feature changes, encouraging the predictor to retain action-relevant information. On ten tasks in the humanoid loco-manipulation simulation benchmark SIMPLE, our method achieves 89.7% average success, compared with 73.7% for Psi-Zero and 82.0% for DiT4DiT. On seven real-robot tasks, it achieves 85.7% under standard conditions and 65.7% under unseen object configurations, while GR00T N1.7 achieves 70.0% and 48.6%, respectively. Project page: https://ju6276.github.io/Action-Grounded-Foresight/

</details>

---

### [[20_Research/Papers/具身智能/Action_Intent_as_a_Bridge_Transferring_Manipulation_Knowledge_from_Human-Centric_Videos_to_Robots|Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots]]

![[assets/2611.04522_figure.png|800]]

- **arXiv**: [2611.04522](https://arxiv.org/abs/2611.04522)
- **PDF**: https://arxiv.org/pdf/2611.04522
- **详细分析**: [[20_Research/Papers/具身智能/Action_Intent_as_a_Bridge_Transferring_Manipulation_Knowledge_from_Human-Centric_Videos_to_Robots|Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots]]
- **作者**: Zhiqian Xia, Lianyang Ma, Haifeng Xia, Siyu Xia, Wei Wang, Xiaochun Cao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Action Intent as a Bridge: Transferring Manipulation Knowledge from Human-Centric Videos to Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have achieved promising performance for generalized robotic manipulation, yet their reliance on expensive real-robot data remains a fundamental bottleneck. A scalable alternative is to transfer knowledge from off-the-shelf human-centric videos. However, existing methods extract latent action representations that are entangled with scene-specific noise, diluting the transferred knowledge. Motivated by this limitation, we propose Action-Intent Transfer (AIT), a two-stage method that transfers knowledge through a clean action representation shared across humans and robots. In the first stage, AIT extracts explicit action intents and disentangles the implicit action intent from manipulation videos. In the second stage, AIT aligns the human and robot domains within this shared intent space and decodes the intent into executable robot actions. Extensive experiments in both simulation and real-world environments demonstrate that AIT transfers human knowledge more effectively and consistently outperforms prior baselines.

</details>

---

### [[20_Research/Papers/大模型/LLM-Assisted_Planning_with_Distributed_Onboard_Behaviour_Tree_Execution_for_Multi-AUV_Missions|LLM-Assisted Planning with Distributed Onboard Behaviour Tree Execution for Multi-AUV Missions]]

![[assets/2611.04518_figure.png|800]]

- **arXiv**: [2611.04518](https://arxiv.org/abs/2611.04518)
- **PDF**: https://arxiv.org/pdf/2611.04518
- **详细分析**: [[20_Research/Papers/大模型/LLM-Assisted_Planning_with_Distributed_Onboard_Behaviour_Tree_Execution_for_Multi-AUV_Missions|LLM-Assisted Planning with Distributed Onboard Behaviour Tree Execution for Multi-AUV Missions]]
- **作者**: Ehsan Khorrambakht, Cristiano Caissutti, Andrea Munafo, Andrea Caiti
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.7，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《LLM-Assisted Planning with Distributed Onboard Behaviour Tree Execution for Multi-AUV Missions》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coordinating autonomous underwater vehicles requires translating operator intent into feasible assignments while preserving autonomous execution when communication is limited. We present a hierarchical framework that couples Large Language Model (LLM) interpretation of natural-language mission instructions with Mixed-Integer Linear Programming (MILP) and distributed Behaviour Tree (BT) execution. The LLM extracts assignment and ordering constraints, which the MILP optimizer combines with vehicle capabilities and temporal requirements. A BT-LLM Bridge distributes the resulting allocations to onboard BT Mission Managers. Per-vehicle Robotic Agents assess local faults and request selective replanning, allowing unaffected vehicles to continue their assigned tasks. Evaluation in a ROS-based AUV simulator compares Qwen-3-8B and Llama-3.1-8B on constraint extraction and tests recovery from sensor degradation and critical vehicle faults. Qwen-3-8B provides more accurate constraint extraction, and all tasks are completed in the tested failure scenarios. These simulation results support the feasibility of combining language-based mission specification with structured allocation and distributed execution.

</details>

---

### [[20_Research/Papers/具身智能/Physical_Diffusion_Policy_via_MPM-Guided_3D_Gaussian_Simulation|Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation]]

![[assets/2611.04493_figure.png|800]]

- **arXiv**: [2611.04493](https://arxiv.org/abs/2611.04493)
- **PDF**: https://arxiv.org/pdf/2611.04493
- **详细分析**: [[20_Research/Papers/具身智能/Physical_Diffusion_Policy_via_MPM-Guided_3D_Gaussian_Simulation|Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation]]
- **作者**: Can Wang, Qiyuan Qiao, Lei Liu, Ge Yuan, Xinhui Liu, Dong Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Physical Diffusion Policy via MPM-Guided 3D Gaussian Simulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning robust manipulation policies for diverse everyday objects remains challenging because objects with different materials exhibit distinct deformation and contact dynamics. While diffusion policies provide a powerful framework for modeling multimodal manipulation behaviors, they typically lack explicit physical reasoning and may produce averaged actions when facing heterogeneous objects. We present a physics-aware diffusion policy that augments visual imitation learning with object physical understanding. Our framework recovers material properties from visual demonstrations by coupling 3D Gaussian Splatting with differentiable Material Point Method simulation, where video guidance and particle-level constraints enable accurate physical parameter estimation. The estimated physics conditions are further integrated into a material-aware Mixture-of-Experts diffusion policy, allowing adaptive behavior generation across different physical regimes. For practical deployment, we introduce a physics memory bank that provides efficient physical retrieval without requiring online simulation optimization. Experiments on a wide range of simulated and real-world objects demonstrate improved manipulation success and generalization over existing diffusion-based approaches. These results show that incorporating physical knowledge is critical for scalable robot manipulation in diverse environments.

</details>

---

### [[20_Research/Papers/具身智能/All-For-One_Distilling_Visual_Foundation_Models_to_a_Fast,_Memory-Efficient_Visuomotor_Policy|All-For-One: Distilling Visual Foundation Models to a Fast, Memory-Efficient Visuomotor Policy]]

![[assets/2611.04485_figure.png|800]]

- **arXiv**: [2611.04485](https://arxiv.org/abs/2611.04485)
- **PDF**: https://arxiv.org/pdf/2611.04485
- **详细分析**: [[20_Research/Papers/具身智能/All-For-One_Distilling_Visual_Foundation_Models_to_a_Fast,_Memory-Efficient_Visuomotor_Policy|All-For-One: Distilling Visual Foundation Models to a Fast, Memory-Efficient Visuomotor Policy]]
- **作者**: Byungkun Lee, Minho Park, Hojoon Lee, Dongyoon Hwang, Donghu Kim, Hyunseung Kim, Kyungmin Lee, Yunho Kim, Jaegul Choo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《All-For-One: Distilling Visual Foundation Models to a Fast, Memory-Efficient Visuomotor Policy》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, MetaWorld, Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual Foundation Models (VFMs) provide semantic cues such as depth and segmentation useful for robotic manipulation, but directly deploying them in closed-loop control is impractical due to high computational cost, temporal inconsistency, and distribution shift between static internet images and egocentric robot observations. We propose All-For-One (AFO), a two-stage distillation framework that leverages VFMs strictly as privileged information during training, using downstream robotic data. Following the privileged learning paradigm, AFO decouples semantic representation learning from inference-time policy execution. In the All stage, a teacher policy fuses RGB observations with outputs from multiple VFMs to learn a semantically enriched representation. In the For-One stage, this knowledge is distilled in-distribution into a lightweight RGB-only student policy. Evaluated on two Adroit tasks and five MetaWorld tasks in simulation, as well as three real-world manipulation tasks, AFO outperforms prior foundation-model-based approaches while using over 30x fewer parameters than VFM-based encoders and 50x lower latency than its own teacher in simulation benchmarks, providing an efficient pathway for transferring foundation-model knowledge to robotic control.

</details>

---

### [[20_Research/Papers/具身智能/Spectrally_Routed_Diffusion_Policy_for_Multi-Task_Robotic_Manipulation|Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation]]

![[assets/2611.04477_figure.png|800]]

- **arXiv**: [2611.04477](https://arxiv.org/abs/2611.04477)
- **PDF**: https://arxiv.org/pdf/2611.04477
- **详细分析**: [[20_Research/Papers/具身智能/Spectrally_Routed_Diffusion_Policy_for_Multi-Task_Robotic_Manipulation|Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation]]
- **作者**: Mingcong Li, Yihan Zhou, Jiayu Qu, Xueyang Guo, Yilin Mo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Spectrally Routed Diffusion Policy for Multi-Task Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based policies have achieved strong performance on single-task robotic manipulation. However, a single model trained jointly on multiple tasks consistently underperforms the per-task specialists trained on the same demonstrations. We focus on two challenges. First, the convolutional encoders commonly used in diffusion-based policies produce visual conditions that are not discriminative enough. Second, gradients from incompatible action modes update the shared denoiser's dense parameters along the same directions, causing destructive interference during joint training. To address both, we propose SR-DP (Spectrally Routed Diffusion Policy). A frozen VGGT encoder with a spatial-compression adapter produces compact multi-scale semantic-geometric tokens, a task-discriminative visual condition for tasks that share a workspace. We first train the denoiser as a standard diffusion policy, then decompose selected linear layers by SVD into a frozen basis of orthogonal rank-one experts, adapted through spectral routing and Householder input rotations. On six RoboTwin tasks, SR-DP averages a 68.4% success rate, surpassing multi-task VO-DP by 21.8 points and the strongest per-task baseline by 3.8 points. On four real-world bimanual tasks, Stage 2 reaches a 43.0% average success rate and improves over Stage 1 by 19.0 points.

</details>

---

### [[20_Research/Papers/强化学习/ReflexArc_Bottom-Up_Integration_of_Instantaneous_Tactile_Reflexes_into_Whole-Body_Humanoid_Control|ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2611.04424](https://arxiv.org/abs/2611.04424)
- **PDF**: https://arxiv.org/pdf/2611.04424
- **详细分析**: [[20_Research/Papers/强化学习/ReflexArc_Bottom-Up_Integration_of_Instantaneous_Tactile_Reflexes_into_Whole-Body_Humanoid_Control|ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control]]
- **作者**: Mingyu Wang, Si Li, Ziqing Chen, He Wang, Li Yi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《ReflexArc: Bottom-Up Integration of Instantaneous Tactile Reflexes into Whole-Body Humanoid Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots operating in cluttered environments must react to unexpected contacts before the first impact peak, which arrives within tens of milliseconds. Learned whole-body policies running at 50 Hz introduce a policy-cycle delay and may suppress a protective withdrawal as a tracking error. To address these challenges, we propose ARC (Ascending Reflex Control), a bottom-up framework that integrates instantaneous tactile reflexes with learned whole-body control. ARC consists of two components: an instantaneous reflex pathway and bottom-up reflex integration. The reflex pathway detects hazardous contacts from full-body tactile sensing, solves a whole-body withdrawal pose, and delivers it directly to the motors within 10 ms. Bottom-up reflex integration combines reflex-in-the-loop policy learning, reflex-transparent policy alignment, and reflex-informed policy adaptation to sustain the withdrawal, maintain balance, and complete longer-horizon recovery. We deploy ARC on a Unitree G1 and evaluate three categories of hazardous contact. Compared with an otherwise identical reflex delayed by 20 ms, ARC reduces the first force peak by 34.1% and reduces the contact impulse from 0.2632 N s to 0.1225 N s (a 2.15x ratio). We further demonstrate protected motion tracking, teleoperation, and vision-free obstacle traversal guided by foot tactile sensing. Project page: https://minusmodulo.github.io/reflexarc-website/

</details>

---

### [[20_Research/Papers/机器人/RAIPAL_A_Powerful_and_Agile_Humanoid_Arm_for_Human_Tasks|RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks]]

![[assets/2611.04334_figure.png|800]]

- **arXiv**: [2611.04334](https://arxiv.org/abs/2611.04334)
- **PDF**: https://arxiv.org/pdf/2611.04334
- **详细分析**: [[20_Research/Papers/机器人/RAIPAL_A_Powerful_and_Agile_Humanoid_Arm_for_Human_Tasks|RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks]]
- **作者**: Donggeon Kim, Hyungho Chris Choi, Donghyuk Choi, Jeongsoo Park, Choongin Lee, Chan Park, Jemin Hwangbo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《RAIPAL: A Powerful and Agile Humanoid Arm for Human Tasks》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents humanoid manipulator hardware designed specifically for human-level performance throughout its broad domain of tasks, from heavy payloads to highly dynamic motions. Unlike conventional designs targeting uniform workspace capability, the proposed approach derives force, speed, and endurance targets from published measurements of task-relevant human upper-limb performance. These targets guide the actuator, mechanism, and thermal design toward torque transparency and sustained operation. The platform integrates force-oriented upper-arm components, speed-oriented forearm components, and a posture-dependent elbow mechanism that shifts its torque-speed behavior. These components are driven by planetary actuators and compact actuator-embedded electronics. Experimental results validate broad task capability, demonstrating a peak payload of 20 kg (2.25x its own mass), an endpoint speed of 20.6 m/s, and continued operation under repeated hammering impacts. Thermal analysis further confirms that the robot's sustained operation capability exceeds the published human load--duration boundary across nearly the entire load spectrum. These findings show that hardware targets derived from human-task measurements narrow the human-to-humanoid capability gap. A supplementary video is available at https://youtu.be/xVUWFICD5G0

</details>

---

### [[20_Research/Papers/具身智能/ActOR_Ambient_AI-Based_Agentic_Orchestration_for_Humanoid_Autonomy_in_Operating_Rooms|ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms]]

![[assets/2611.04255_figure.png|800]]

- **arXiv**: [2611.04255](https://arxiv.org/abs/2611.04255)
- **PDF**: https://arxiv.org/pdf/2611.04255
- **详细分析**: [[20_Research/Papers/具身智能/ActOR_Ambient_AI-Based_Agentic_Orchestration_for_Humanoid_Autonomy_in_Operating_Rooms|ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms]]
- **作者**: Han Zhang, Sicheng Lu, Aleks Santari, Jeffrey K. Jopling, Masaru Ishii, Mathias Unberath
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.6（加权：具身智能 1.8，大模型 0.3，机器人 1.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《ActOR: Ambient AI-Based Agentic Orchestration for Humanoid Autonomy in Operating Rooms》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Operating rooms (ORs) increasingly contain ambient sensing infrastructure to enable AI-based optimization of workflows and utilization. We pursue an alternative path: using ambient AI to guide robot action and optimize utilization. Deploying humanoids in the OR without ambient AI is severely limited by cumbersome de novo orientation and planning due to partial onboard observations. We posit that this can be achieved by coupling an ambient AI-based agentic orchestrator with the humanoid robotic actor, providing shared perception and execution feedback for humanoid autonomy in the OR. ActOR fuses a wall-mounted ambient camera and the robot's head-mounted camera into a shared object-level digital twin (DT). A large language model agent plans over the DT using pre-programmed locomotion and manipulation skills without task-specific training. During execution, DT updates and execution outcomes inform retries, alternative approaches, or replanning. We evaluated ActOR in simulated and physical environments. Across three tasks in two simulated ORs reconstructed from real rooms, ambient perception reduced exploration from 1.05 to 0.12 Explore calls per trial when targets were initially outside the robot's view. Closed-loop feedback increased success from 46.7% to 83.3% under nominal execution and from 8.3% to 51.7% under injected navigation, object-relocation, and grasp perturbations. In a physical mock OR with a humanoid, ActOR completed 14 of 20 single-object disposal trials and demonstrated replanning after scene changes. Ambient AI-based observations provide scene state that improves robot action planning, increasing success and reducing exploration compared with robot-only observations. Feeding skill outcomes and DT updates back to the planner improves multi-step task success. Our results show the feasibility of humanoid task autonomy for multi-step disposal tasks in a mock OR.

</details>

---

### [[20_Research/Papers/具身智能/Online_iLQR-MPC_with_Whole-Body_Control_for_Robust_Humanoid_Locomotion|Online iLQR-MPC with Whole-Body Control for Robust Humanoid Locomotion]]

![[assets/2611.04204_figure.png|800]]

- **arXiv**: [2611.04204](https://arxiv.org/abs/2611.04204)
- **PDF**: https://arxiv.org/pdf/2611.04204
- **详细分析**: [[20_Research/Papers/具身智能/Online_iLQR-MPC_with_Whole-Body_Control_for_Robust_Humanoid_Locomotion|Online iLQR-MPC with Whole-Body Control for Robust Humanoid Locomotion]]
- **作者**: Xiang Li, Linlin Ou, Ruihan Wu, Xinyi Yu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Online iLQR-MPC with Whole-Body Control for Robust Humanoid Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid locomotion requires deciding where to step and how to distribute contact forces. However, a disturbance can invalidate the nominal plan, requiring coordinated revision under constraints that switch with every footfall. To solve this online, the proposed approach employs the single-rigid-body model, which retains attitude dynamics and the full contact wrench. An iterative linear-quadratic-regulator MPC (iLQR-MPC) then jointly optimizes contact forces and footstep locations in a single receding-horizon problem, without a separate step planner. Specifically, contact and motion constraints are incorporated into the backward pass through augmented-Lagrangian and relaxed-barrier penalties. A whole-body controller subsequently maps the plan to joint torques at 500 Hz while preserving contact feasibility. The model-based formulation makes disturbance responses interpretable through explicit costs and constraints, and requires no platform-specific policy training. In MuJoCo simulations, the iLQR-MPC replans at 100 Hz (mean solve time 8.9 ms); the Unitree G1 sustains steady-state walking and recovers from impulsive 245 N forward and 175 N lateral pushes.

</details>

---

### [[20_Research/Papers/具身智能/Grasping_and_Stabilizing_Tumbling_Objects_with_Rotating-Base_Multi-Arm_Space_Manipulators|Grasping and Stabilizing Tumbling Objects with Rotating-Base Multi-Arm Space Manipulators]]

![[assets/2611.04176_figure.png|800]]

- **arXiv**: [2611.04176](https://arxiv.org/abs/2611.04176)
- **PDF**: https://arxiv.org/pdf/2611.04176
- **详细分析**: [[20_Research/Papers/具身智能/Grasping_and_Stabilizing_Tumbling_Objects_with_Rotating-Base_Multi-Arm_Space_Manipulators|Grasping and Stabilizing Tumbling Objects with Rotating-Base Multi-Arm Space Manipulators]]
- **作者**: Farhad Aghili
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Grasping and Stabilizing Tumbling Objects with Rotating-Base Multi-Arm Space Manipulators》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an innovative guidance and control method for a space manipulator that actively maneuvers its base to hold a tumbling object stationary relative to the base during proximity operations. This simplifies motion planning, reduces collision risk, and enables impact-free capture using single- or multi-arm configurations, with or without predefined grasping interfaces. The proposed approach involves two phases. In the pre-grasping phase, a synchronization control aligns the target's center of mass (CoM) with the system's instantaneous center of rotation (ICR), virtually rigidizing the target-servicer system to keep the object stationary for reliable grasping. In the post grasping phase, a control strategy based on Hamiltonian dynamics and optimal control stabilizes the combined system by minimizing time, fuel, or energy, while respecting base torque limits and multiple grasping constraints. For structured targets, applied forces and torques stay within their bounds; for unstructured ones, friction constraints prevent slipping. A case study demonstrates the method's effectiveness in enabling both the subsequent grasping and detumbling phases.

</details>

---

### [[20_Research/Papers/具身智能/Online_Hamilton-Jacobi_Reachability_Onboard_the_Robot_Control_Loop_A_Real-Time_GPU_Solver_for_Safety-Critical_Autonomy|Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy]]

![[assets/2611.04096_figure.png|800]]

- **arXiv**: [2611.04096](https://arxiv.org/abs/2611.04096)
- **PDF**: https://arxiv.org/pdf/2611.04096
- **详细分析**: [[20_Research/Papers/具身智能/Online_Hamilton-Jacobi_Reachability_Onboard_the_Robot_Control_Loop_A_Real-Time_GPU_Solver_for_Safety-Critical_Autonomy|Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy]]
- **作者**: Kevin Weekly, Alexandre M. Bayen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.9，大模型 0.1，机器人 1.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Online Hamilton-Jacobi Reachability Onboard the Robot Control Loop: A Real-Time GPU Solver for Safety-Critical Autonomy》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hamilton-Jacobi (HJ) reachability provides certified backward reachable tubes (BRTs) for safety-critical robotic systems, but the level-set computation scales exponentially in the state dimension and has historically been performed offline. As autonomy stacks (ADAS/AV, humanoid robotics, and vision-language-action models) increasingly rely on black-box, probabilistic policies, a deterministic safety layer with formal guarantees is an essential complement. We present a CUDA implementation of the canonical WENO5 + TVD-RK3 + Lax-Friedrichs level-set Hamilton-Jacobi-Isaacs solver for 2D, 3D, and 4D dynamics that is fast enough to run inside a robot's control loop. In 32-bit floating point (FP32) on a single workstation GPU (NVIDIA RTX 4000 Ada), it computes the 3D Air3D BRT at 112 Hz, a 4D pursuit-evasion BRT at 61 Hz, and a 2D wind-affected drifter BRT at 74-147 Hz, 5.9-17.5x faster than the JAX reference hj_reachability at matched precision and 1.7-16x faster than a torch.compile reimplementation of the same scheme. In 64-bit floating point (FP64) it agrees with hj_reachability on eight benchmark cases, reproduces Mitchell's Air3D BRT to within 0.04% of the reference cell count, and runs 2.0-4.6x faster. On an embedded NVIDIA Jetson AGX Thor it computes Air3D at 66 Hz (N=41) and the 2D drifter at 54 Hz, 3.8-8.9x faster than hj_reachability on the same device. As a multi-agent application, an in-kernel label-propagation extension recovers the K-agent capture-basin Voronoi tessellation from a single combined HJ solve, independent of fleet size; it runs at 4.0 ms per tick in a closed-loop wildfire-response simulation of six quadcopters under time-varying, non-uniform wind.

</details>

---

### [[20_Research/Papers/机器人/FEIJOA_Task-Driven_Grounding_and_Execution_for_Mobile_Manipulation|FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation]]

![[assets/2611.04080_figure.png|800]]

- **arXiv**: [2611.04080](https://arxiv.org/abs/2611.04080)
- **PDF**: https://arxiv.org/pdf/2611.04080
- **详细分析**: [[20_Research/Papers/机器人/FEIJOA_Task-Driven_Grounding_and_Execution_for_Mobile_Manipulation|FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation]]
- **作者**: Aditya Agarwal, William Shen, Sahit Chintalapudi, Lucy Cai, Nishanth Kumar, Aidan Curtis, Travis Manderson, Tomás Lozano-Pérez, Leslie Pack Kaelbling
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《FEIJOA: Task-Driven Grounding and Execution for Mobile Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A mobile manipulator asked to "put the toys away in the toy box" must decide which objects are toys and which container the user means, then find base poses, grasps, and placements it can execute. Because a scene representation is built before the instruction is known, it may lack the attributes, affordances, or concepts needed to resolve the task. We present FEIJOA, a language-model agent that grounds the instruction at test time. It queries a grounding tool over a posed RGB-D scan, inspects the returned candidates, and refines its queries until they resolve the instruction. An embodiment-aware harness checks each skill's preconditions, samples base poses from which the target is reachable, and verifies the skill's effect from observations before and after execution. On 103 open-ended grounding queries, FEIJOA resolves 94.2% exactly, compared with 68.0% for the best prebuilt representation. Over 50 real-world trials on Spot, it completes 35 tasks; 17 of these successes follow recovery from a failed tool call or verification check. Of the 15 failed trials, 13 were caused by the robot's physical skills, and only 2 by grounding or the agent's reasoning. Project website: https://williamshen-nz.github.io/feijoa/.

</details>

---

### [[20_Research/Papers/具身智能/Physical_Experience_Builds_Continual_Spatial_World_Models|Physical Experience Builds Continual Spatial World Models]]

![[assets/2611.04016_figure.png|800]]

- **arXiv**: [2611.04016](https://arxiv.org/abs/2611.04016)
- **PDF**: https://arxiv.org/pdf/2611.04016
- **详细分析**: [[20_Research/Papers/具身智能/Physical_Experience_Builds_Continual_Spatial_World_Models|Physical Experience Builds Continual Spatial World Models]]
- **作者**: Yuhang Sun
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.6，大模型 0.2，世界模型 1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, WorldModel

#### 研究背景与动机

《Physical Experience Builds Continual Spatial World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are increasingly used to support prediction and planning in embodied agents, but the knowledge is usually established before deployment and then carried into later encounters. Continual operation faces a different problem. A familiar environment may change, and the agent must use previous experience without allowing old expectations to override current physical evidence. This study asks what repeated physical experience must contribute for a spatial world model to become progressively more useful rather than simply more persistent. A physics-grounded dynamic maze separates recurring spatial change from the continuous consequences of action. Cross-episode Spatial Change Memory learns relations among environmental transformations, while state-action-outcome experience refines predictions of motion. Structured experience progressively reduces the need for future route correction and transfers to spatial transitions not encountered during learning. The advantage disappears when past changes contain no information about future ones. Continuous navigation further shows that predictive memory changes behavior when a previous decision becomes invalid but leaves behavior unchanged when the decision remains correct. Physical tests expose a complementary limit: correct topology does not guarantee correct action prediction, and accumulated physical experience reduces this mismatch within the modeled dynamics. The results characterize continual world knowledge as experience that improves future prediction and action beyond stored episodes while remaining revisable by the physical outcomes it is intended to predict.

</details>

---

### [[20_Research/Papers/机器人/Self-governed_access_control_in_open_robot_swarms_using_a_blockchain-based_DAO|Self-governed access control in open robot swarms using a blockchain-based DAO]]

![[assets/2611.03975_figure.png|800]]

- **arXiv**: [2611.03975](https://arxiv.org/abs/2611.03975)
- **PDF**: https://arxiv.org/pdf/2611.03975
- **详细分析**: [[20_Research/Papers/机器人/Self-governed_access_control_in_open_robot_swarms_using_a_blockchain-based_DAO|Self-governed access control in open robot swarms using a blockchain-based DAO]]
- **作者**: Raina Zakir, Alexandre Pacheco, Andreagiovanni Reina, Marco Dorigo, Volker Strobel
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Self-governed access control in open robot swarms using a blockchain-based DAO》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot swarms harness simple, local interactions among many individually limited robots to produce complex, coordinated collective behavior, making them valuable across domains from agriculture to disaster response. We envision the next frontier for such swarms as open swarms, in which robots join or leave the swarm dynamically at runtime. The ability to dynamically adjust swarm size has been shown to be beneficial, for instance by reducing inconsistencies and network partitioning, especially under sparse connectivity or in complex environments, ultimately improving task performance. For practical deployment, however, open swarms requires governance, particularly protection against Byzantine behavior (i.e., faulty or malicious robots), since allowing robots to join freely also makes the swarm easier to infiltrate. Blockchain technology has recently been incorporated into robot swarms, offering secure, decentralized coordination and improved resilience, though largely in closed settings with a fixed, predetermined membership. In this work, we extend these benefits to open swarms by introducing robot swarms governed by a blockchain-based decentralized autonomous organization (DAO), in which the swarm regulates itself using autonomous rules encoded in smart contracts. We outline several DAO-based governance mechanisms for robot swarms, depending on the needs of the application, and present a proof-of-concept implementation of a simple DAO that regulates swarm membership and prevents Byzantine infiltration. Our simulation results and real-robot validations show that DAO-governed access control and robot removal can maintain proper swarm functioning while keeping the number of Byzantine robots within acceptable limits.

</details>

---

### [[20_Research/Papers/机器人/h-NESDF_An_Infinitely_Differentiable_Signed_Distance_Between_Two_Sets_with_Robotic_Applications|h-NESDF: An Infinitely Differentiable Signed Distance Between Two Sets with Robotic Applications]]

![[assets/2611.03944_figure.png|800]]

- **arXiv**: [2611.03944](https://arxiv.org/abs/2611.03944)
- **PDF**: https://arxiv.org/pdf/2611.03944
- **详细分析**: [[20_Research/Papers/机器人/h-NESDF_An_Infinitely_Differentiable_Signed_Distance_Between_Two_Sets_with_Robotic_Applications|h-NESDF: An Infinitely Differentiable Signed Distance Between Two Sets with Robotic Applications]]
- **作者**: Vinicius Mariano Gonçalves, Pedro Antonio de Souza Campos Rodrigues
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《h-NESDF: An Infinitely Differentiable Signed Distance Between Two Sets with Robotic Applications》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computing distances between sets is important in many robotic applications, such as motion planning and control. In many applications, derivatives of the distance are needed as well. It is well known that the Euclidean distance is not always differentiable, which create issues to algorithms that need a derivative. In this paper, we introduce NESDF, the Normal Euclidean Signed Distance Function between two general (with mild regularity assumptions but possibly non-convex) sets. This metric is still not differentiable, but it allows us to introduce a generalization, $h$-NESDF, which has a smoothing parameter $h$ such that the metric is infinitely differentiable for all $h&gt;0$ and that reduces to the NESDF when $h$ goes to $0$. The metric is amenable to GPU parallelization, and thus can be computed efficiently. We show extensive simulation results to evaluate its viability in motion planning.

</details>

---

### [[20_Research/Papers/机器人/A_Tutorial_on_Shape_Servoing_of_Deformable_Objects-Part_II_Advanced_Concepts|A Tutorial on Shape Servoing of Deformable Objects-Part II: Advanced Concepts]]

![[assets/2611.03825_figure.png|800]]

- **arXiv**: [2611.03825](https://arxiv.org/abs/2611.03825)
- **PDF**: https://arxiv.org/pdf/2611.03825
- **详细分析**: [[20_Research/Papers/机器人/A_Tutorial_on_Shape_Servoing_of_Deformable_Objects-Part_II_Advanced_Concepts|A Tutorial on Shape Servoing of Deformable Objects-Part II: Advanced Concepts]]
- **作者**: Ignacio Cuiral-Zueco, Alessio Caporali, Miguel Aranda, Gianluca Palli, Gonzalo López-Nicolás, Youcef Mezouar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Tutorial on Shape Servoing of Deformable Objects-Part II: Advanced Concepts》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotics, shape control, or shape servoing, refers to the automatic manipulation of a deformable object toward a desired shape. This article is the second of a two-part tutorial on data-driven, Jacobian-based shape control, in which the deformation Jacobian, a local model of how robot motion changes the measured shape, is estimated from measurements. Part I built the shape-servoing loop and derived a local stability condition. This paper starts by using the singular value decomposition of the deformation Jacobian to identify shape changes that can be produced by small robot motions, those that require large robot motions, and those that are locally unavailable. It then analyses how the choice of shape features determines how the controller regulates the object's shape and, therefore, how much the object deforms on its way to the target. It then describes three ways in which the shape control loop can fail: loss of controllability, loss of observability, and occurrence of mechanical instabilities. It closes with shape-control extensions to time-varying targets, secondary tasks, and three-dimensional objects.

</details>

---

### [[20_Research/Papers/机器人/Robot-Matched_Soft_Fingers_for_UMI_Data_Collection_Lessons_from_100_Hours_of_Pick_and_Place|Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place]]

![[assets/2611.03779_figure.jpg|800]]

- **arXiv**: [2611.03779](https://arxiv.org/abs/2611.03779)
- **PDF**: https://arxiv.org/pdf/2611.03779
- **详细分析**: [[20_Research/Papers/机器人/Robot-Matched_Soft_Fingers_for_UMI_Data_Collection_Lessons_from_100_Hours_of_Pick_and_Place|Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place]]
- **作者**: Kobi Kelemen, Tomasz Niedziałkowski, Marcin Paszczak, Victoriano Montesinos
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Robot-Matched Soft Fingers for UMI Data Collection: Lessons from 100 Hours of Pick and Place》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training robot policies for multi-task pick and place requires demonstrations on many objects, which handheld Universal Manipulation Interfaces (UMIs) can collect quickly and cheaply. However, existing UMIs depend on external base stations, use rigid fingers that give no signal about contact forces, or use parallel-jaw fingers that limit grip strength. We present a battery-powered handheld interface, built on YUBI, whose soft, angled fingers wrap around objects, deform visibly under load as a visual proxy for force, and match the grippers of the robot. With it, we collect a 99.7-hour dataset over 53 objects, train $π_{0.5}$ policies on 49 of them, and hold out the other 4 as unseen objects. We find that a top camera raises success by 13 points even when only about half of the data includes it, and that mid-training on our multi-task data raises success after fine-tuning on unseen objects from 35% to 57%. Finger design, dataset, and data processing code: https://lute-corp.github.io/soft-yubi-site/

</details>

---
