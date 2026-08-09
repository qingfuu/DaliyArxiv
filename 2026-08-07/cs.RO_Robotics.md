# cs.RO | Robotics | 2026-08-07

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/具身智能/$ω$-0_A_Latent_Predictive_World_Action_Model_for_Concurrent_Humanoid_Loco-Manipulation|$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation]]

![[assets/2608.06375_figure.png|800]]

- **arXiv**: [2608.06375](https://arxiv.org/abs/2608.06375)
- **PDF**: https://arxiv.org/pdf/2608.06375
- **详细分析**: [[20_Research/Papers/具身智能/$ω$-0_A_Latent_Predictive_World_Action_Model_for_Concurrent_Humanoid_Loco-Manipulation|$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation]]
- **作者**: Zhe Li, Zhenzhe Zhang, Yangyang Wei, Wenjie Zhang, Xichen Yuan, Peiyuan Zhi, Gen Li, Xinying Guo, Fengjie Gao, Jianfei Yang, Shanghang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《$ω$-0: A Latent Predictive World Action Model for Concurrent Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EgoVLA, InternVLA, Real-World, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid household tasks often require concurrent loco-manipulation, where the robot must move, adjust posture, maintain balance, and manipulate objects as a single coordinated behavior. Yet existing humanoid policies typically decompose locomotion and manipulation, while recent world-action models remain either arm-centric or video-centered. We present $ω$-0, a latent predictive whole-body world-action model for real-world humanoid concurrent loco-manipulation. Given a language instruction, current visual observation, and robot proprioceptive state, $ω$-0 directly predicts controller-compatible whole-body action latents for real-robot execution. Rather than reconstructing future videos, $ω$-0 learns compact future observation embeddings as a lightweight predictive objective, coupling latent visual foresight with diffusion-based whole-body action generation. The model supports egocentric RGB, exocentric RGB, and exocentric depth inputs, and leverages controller-based simulation replay to ground human/public visual-motion priors into robot-executable action latents. We further collect $ω$-HOME, a 40+ hour real-world household humanoid dataset with synchronized multi-view observations, whole-body SMPL motions, robot states, and action latents. Real-world experiments on 11 household tasks demonstrate that a single $ω$-0 model can produce smooth manipulate-while-moving behaviors and consistently outperform representative imitation learning, VLA, humanoid, and WAM baselines.

</details>

---

### [[20_Research/Papers/具身智能/DyPES-VLA_Learning_Shared_Dynamics_Priors_and_Embodiment-Specific_Control_for_Cross-Embodiment_Manipulation|DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation]]

![[assets/2608.06374_figure.png|800]]

- **arXiv**: [2608.06374](https://arxiv.org/abs/2608.06374)
- **PDF**: https://arxiv.org/pdf/2608.06374
- **详细分析**: [[20_Research/Papers/具身智能/DyPES-VLA_Learning_Shared_Dynamics_Priors_and_Embodiment-Specific_Control_for_Cross-Embodiment_Manipulation|DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation]]
- **作者**: Junfeng Li, Junjie He, Zhide Zhong, Yangyang Zheng, Pingyue Sheng, Jiayu Dong, Ruixin Li, Haodong Yan, Jiaguan Zhu, Tianran Zhang, Runze Yu, Wen Chen...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《DyPES-VLA: Learning Shared Dynamics Priors and Embodiment-Specific Control for Cross-Embodiment Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DyPES-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have become a powerful paradigm for robot manipulation, but training a single generalist policy for heterogeneous robot embodiments remains an open problem. Existing methods have two main limitations. First, they underuse dynamics priors shared across diverse visual and interaction data, limiting cross-embodiment transfer. Second, they require extensive manual preprocessing to convert embodiment-specific actions into a common format. To overcome these limitations, we propose DyPES-VLA, a cross-embodiment VLA that learns shared Dynamics Priors and Embodiment-Specific control. First, we learn shared dynamics priors by training the vision-language model (VLM) with a future-prediction objective on cross-embodiment data, driving the shared query representation to capture object motion, contact, and interaction-induced scene changes. Second, an embodiment-specific Mixture-of-Experts (MoE) action head translates these shared dynamics priors into executable controls directly in each embodiment's native action space, without manually pre-aligning heterogeneous actions into a common format. This head shares attention layers to capture common temporal action structures, while its embodiment-specific feed-forward experts resolve the unique kinematic constraints and control semantics of distinct embodiments. As a generalist policy, our \ourmethod achieves state-of-the-art performance across simulation and real-world evaluations, reaching 98.0% success on LIBERO, 59.25% on RoboCasa-GR1, and 89.02% on RoboTwin~2.0.

</details>

---

### [[20_Research/Papers/大模型/A_Master-Salve_Robot_Manipulator_for_Needle-Based_Teleoperation_in_MRI_Chamber|A Master-Salve Robot Manipulator for Needle-Based Teleoperation in MRI Chamber]]

![[assets/2608.06354_figure.png|800]]

- **arXiv**: [2608.06354](https://arxiv.org/abs/2608.06354)
- **PDF**: https://arxiv.org/pdf/2608.06354
- **详细分析**: [[20_Research/Papers/大模型/A_Master-Salve_Robot_Manipulator_for_Needle-Based_Teleoperation_in_MRI_Chamber|A Master-Salve Robot Manipulator for Needle-Based Teleoperation in MRI Chamber]]
- **作者**: Omar Curiel, Jing-Yuan Huang, Po-Chih Chen, Ji Ma, Qing Dai, Wenqi Zhou, David Lu, Holden H. Wu, Tsu-Chin Tsao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《A Master-Salve Robot Manipulator for Needle-Based Teleoperation in MRI Chamber》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a MR safe, master-slave robot manipulator for abdominal interventions in the MRI chamber. A human operated 2+1-DoF master controller manipulator transmits motion and force to a 2+1-DoF slave manipulator via fluid transmission. Jointly, a digital master controller provides multimodal control capability beyond common split axis or mode switchable hybrid human-digital controller configurations found in previous studies. High input impedance, low-leakage, elastomeric fluid actuators are delegated to remote angulation control. Low-friction graphite piston cylinders are delegated to needle insertion axis remote actuation given the sub-newton force transparency and sub-millimeter motion transmission over bedside fluid piping lengths. The device enables real-time MRI guided interventions allowing manual, digital, hybrid, and collaborative control modes. Collaborative tasks such as assisted tissue penetration, fault-driven virtual fixture, and motion compensation through feedback control are presented in this paper. Preliminary MR scanner results demonstrate manipulator functional viability for an in-vivo pig experiment in bedside, manual control mode configuration.

</details>

---

### [[20_Research/Papers/具身智能/GeniWorld_A_Generalizable_Interactive_World_Model_for_Robotic_Manipulation_via_Visual_Actions|GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions]]

![[assets/2608.06332_figure.png|800]]

- **arXiv**: [2608.06332](https://arxiv.org/abs/2608.06332)
- **PDF**: https://arxiv.org/pdf/2608.06332
- **详细分析**: [[20_Research/Papers/具身智能/GeniWorld_A_Generalizable_Interactive_World_Model_for_Robotic_Manipulation_via_Visual_Actions|GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions]]
- **作者**: Chenghao Gu, Hanyang Yu, Jingbo Zhang, Haitao Lin, Wenyao Zhang, Jinghe Wang, Hanglei Jin, Shuzhao Xie, Jingyan Jiang, Zhi Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.3（加权：具身智能 1.2，世界模型 1，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《GeniWorld: A Generalizable Interactive World Model for Robotic Manipulation via Visual Actions》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet, Ctrl-World, GeniWorld, IRASim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies exhibit strong capabilities, but their robustness in complex and unseen environments remains limited. Scaling robot learning and evaluation in diverse real-world environments remains costly and challenging. Action-conditioned world models offer a promising alternative, but they often suffer from limited action controllability and poor generalization to out-of-distribution (OOD) scenarios. To this end, we present GeniWorld, an interactive world model for robots that generalizes robustly across unseen scenarios. Building on pretrained video generative models, we use URDF-based rendering to transform numerical actions into visual action representations, enabling spatially grounded action control. By explicitly decoupling embodiment kinematics from environmental dynamics, our model mitigates scene overfitting and facilitates modeling of robot-environment interactions. To achieve closed-loop control, we construct an autoregressive video prediction model integrated with high-frequency robot kinematic control, enabling interaction with both robot policies and human teleoperators. In our experiments, even when trained solely on limited fixed-scene data, our model achieves superior in-domain performance and robust zero-shot generalization to highly randomized, unseen environments. For downstream applications, GeniWorld serves as a scalable policy evaluator that remains reliable under environmental perturbations. Furthermore, even with limited real-world demonstrations, GeniWorld generates diverse manipulation trajectories within the world model, improving downstream policy performance and robustness in complex environments.

</details>

---

### [[20_Research/Papers/具身智能/VIDP_Variable_Impedance_Diffusion_Policy_for_Compliant_Robot_Manipulation_from_Diverse_Demonstrations|VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations]]

![[assets/2608.06210_first_page.png|800]]

- **arXiv**: [2608.06210](https://arxiv.org/abs/2608.06210)
- **PDF**: https://arxiv.org/pdf/2608.06210
- **详细分析**: [[20_Research/Papers/具身智能/VIDP_Variable_Impedance_Diffusion_Policy_for_Compliant_Robot_Manipulation_from_Diverse_Demonstrations|VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations]]
- **作者**: Hisham Khalil, Neil Fernandes, Thomas M. Kwok, Hsiu-Chin Lin, Yue Hu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，机器人 0.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《VIDP: Variable Impedance Diffusion Policy for Compliant Robot Manipulation from Diverse Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation requires precise tracking and mechanical compliance, where variable impedance control can improve robustness in task success, whereas static compliance cannot adapt to varying contact constraints. Variable impedance skills can be learned from demonstrations, avoiding complex modeling, but compliance is a hidden variable in force-agnostic kinematic data. While existing methods infer compliance from trajectory variations, these variations may reflect geometric adaptation and not intentional compliance when subject to changing spatial layouts. Therefore, this letter introduces Variable Impedance Diffusion Policy (VIDP), an imitation learning-based variable impedance control framework leveraging a Task-Parameterized Directionality-Aware Mixture Model (TP-DAMM) to extract physically consistent trajectory distributions from diverse demonstrations. By mapping distributions to stiffness profiles, VIDP jointly predicts pose actions and task compliance without force sensors. Real-world experiments show that VIDP significantly outperforms fixed-impedance baselines in task success rate while reducing interaction forces with respect to high stiffness controllers and tracking errors with respect to low stiffness baselines.

</details>

---

### [[20_Research/Papers/机器人/ErgoSurf_Ergodic_Control_for_the_Coverage_of_Unknown_Surfaces|ErgoSurf: Ergodic Control for the Coverage of Unknown Surfaces]]

![[assets/2608.06208_figure.png|800]]

- **arXiv**: [2608.06208](https://arxiv.org/abs/2608.06208)
- **PDF**: https://arxiv.org/pdf/2608.06208
- **详细分析**: [[20_Research/Papers/机器人/ErgoSurf_Ergodic_Control_for_the_Coverage_of_Unknown_Surfaces|ErgoSurf: Ergodic Control for the Coverage of Unknown Surfaces]]
- **作者**: Stefan Schneyer, Timo Bachmann, Maged Iskandar, Korbinian Nottensteiner, Alin Albu-Schäffer, Freek Stulp, João Silvério
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《ErgoSurf: Ergodic Control for the Coverage of Unknown Surfaces》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-centric tasks on surfaces, ranging from inspection and cleaning to sanding and polishing, require robots to systematically cover the surface while maintaining stable contact. Ergodic control generates trajectories that spend time at a location proportional to a desired, task-specific spatial distribution, enabling efficient information gathering and coverage. However, traditional ergodic control methods rely on prior knowledge of surface geometry or require a vision sensory input to scan the geometry beforehand, limiting their applicability in real-world scenarios with unknown or dynamic environments. This paper introduces a novel online ergodic control framework that achieves systematic surface coverage while simultaneously reconstructing unknown surface geometry. We employ a Gaussian Process Implicit Surface (GPIS) model that learns global surface geometry from intrinsic tactile sensing during execution. For efficient online planning, we approximate the surface locally using point clouds sampled from tangent planes at observed contact points and iteratively fit them to the Gaussian Process. This approximation simultaneously serves as the sampling domain for both the target and the coverage distributions. We employ a heat-diffusion analogy to compute potential fields that guide ergodic exploration, translating spatial coverage objectives into smooth robot trajectories. We demonstrate our framework through simulation and real-robot experiments, validating simultaneous ergodic coverage and online surface geometry learning with reconstruction errors approaching the ground truth.

</details>

---

### [[20_Research/Papers/具身智能/IcFuzz_Fuzzing_Isaac_Sim_with_Semantic_Stage_Guidance_and_Multi-level_Mutation|IcFuzz: Fuzzing Isaac Sim with Semantic Stage Guidance and Multi-level Mutation]]

![[assets/2608.06088_figure.png|800]]

- **arXiv**: [2608.06088](https://arxiv.org/abs/2608.06088)
- **PDF**: https://arxiv.org/pdf/2608.06088
- **详细分析**: [[20_Research/Papers/具身智能/IcFuzz_Fuzzing_Isaac_Sim_with_Semantic_Stage_Guidance_and_Multi-level_Mutation|IcFuzz: Fuzzing Isaac Sim with Semantic Stage Guidance and Multi-level Mutation]]
- **作者**: Zhixiang Chen, Zhuangbin Chen, Ruoxi Jia, Zeqin Liao, Wei Li, Jinyang Liu, Zibin Zheng
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《IcFuzz: Fuzzing Isaac Sim with Semantic Stage Guidance and Multi-level Mutation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IsaacSim, ZhouSXS0LYS24-AICPSwithIsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotics simulators serve as a foundational infrastructure for embodied AI, facilitating safe and scalable robotic system development. NVIDIA Isaac Sim has emerged as one of the most popular simulators, distinguished by its GPU-accelerated physics engine and photorealistic rendering, which enable high-fidelity modeling of complex environments. However, its inherent complexity inevitably introduces software bugs that can compromise simulation reliability. Existing fuzzing approaches struggle to test Isaac Sim effectively due to challenges of context-aware object semantics, hierarchical simulation control, and a vast simulation state space. In this paper, we propose IcFuzz, the first fuzzing approach for Isaac Sim. IcFuzz first performs an LLM-based semantic stage segmentation, decomposing simulation programs into structured stages that capture context-aware object semantics. Guided by this information, IcFuzz designs multi-level mutation operators to systematically exercise the simulator across hierarchical granularities. To efficiently navigate the vast simulation state space, IcFuzz employs a multi-armed bandit algorithm to adaptively schedule mutation operators. Experimental results show that IcFuzz outperforms the baselines in terms of both code coverage and bug detection. Specifically, IcFuzz achieves approximately 190\%--205\% of the code coverage of the baselines and detects an average of 3.7 unique crashes over three rounds of 12-hour tests, while no crashes are detected by the baselines. Moreover, IcFuzz has uncovered 11 bugs over approximately four months, 9 of which have been confirmed or fixed by the developers.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Flat_Policies_Hierarchical_Post-Training_for_Embodied_Agents_in_Robotic_Manipulation|Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation]]

![[assets/2608.05999_figure.png|800]]

- **arXiv**: [2608.05999](https://arxiv.org/abs/2608.05999)
- **PDF**: https://arxiv.org/pdf/2608.05999
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Flat_Policies_Hierarchical_Post-Training_for_Embodied_Agents_in_Robotic_Manipulation|Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation]]
- **作者**: He Kong, Zengjue Chen, Qi Wang, Qianli Xing, Runliang Niu, Peidong Liu, Jiawei Li, Shiqi Wang, Yi Chang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 4.6（加权：具身智能 3，大模型 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Beyond Flat Policies: Hierarchical Post-Training for Embodied Agents in Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CotVLA, OpenVLA, SimpleVLA-RL, VP-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have demonstrated remarkable capabilities in robotic manipulation by leveraging pretrained vision-language models. However, existing post-training methods predominantly optimize VLA models as flat policies, making it difficult to explicitly model task progression and perform robust long-horizon manipulation. Although hierarchical approaches introduce task decomposition, they mainly rely on supervised learning from offline demonstrations and cannot effectively improve execution through online interaction. To address this limitation, we propose Hierarchical Robotic Control (HiRoC), a hierarchical post-training framework that decouples high-level task planning from low-level action execution. The planner decomposes complex tasks into executable subgoals to provide explicit semantic guidance, while the executor continuously improves subgoal-conditioned action generation through reinforcement learning. To enable effective collaboration between the two modules, we further align the executor with planner-generated subgoals before reinforcement learning, mitigating the distribution misalignment between planning and execution. Extensive experiments across diverse robotic manipulation benchmarks demonstrate that HiRoC consistently outperforms strong baselines. Comprehensive analyses further validate the effectiveness of hierarchical post-training and the contribution of each key component.

</details>

---

### [[20_Research/Papers/机器人/Coordinated_Multi-Robot_Disassembly_for_Makespan_Optimization_of_Large-Scale_Assemblies|Coordinated Multi-Robot Disassembly for Makespan Optimization of Large-Scale Assemblies]]

![[assets/2608.05830_figure.png|800]]

- **arXiv**: [2608.05830](https://arxiv.org/abs/2608.05830)
- **PDF**: https://arxiv.org/pdf/2608.05830
- **详细分析**: [[20_Research/Papers/机器人/Coordinated_Multi-Robot_Disassembly_for_Makespan_Optimization_of_Large-Scale_Assemblies|Coordinated Multi-Robot Disassembly for Makespan Optimization of Large-Scale Assemblies]]
- **作者**: Niklas Hargus, Andreas Orthey, Marc Toussaint
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Coordinated Multi-Robot Disassembly for Makespan Optimization of Large-Scale Assemblies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot task and motion planning for disassembly tasks requires robots to operate in confined workspaces while coordinating their motions with other robots. To tackle this problem, we propose a planning method called coordinated multi-robot disassembly (CoMuDi). CoMuDi coordinates a team of robots for disassembly tasks. The input is a team of robots, an assembly of objects, and a dependency graph. Based on this information, we create compound tasks for pick, place, and exit motions. By propagating temporal constraints, we ensure that each robot can start and end their tasks as early as possible while avoiding collisions with nearby robots. By integrating the space-time RRT* planner (ST-RRT*) into CoMuDi, we ensure that individual tasks minimize arrival time and thereby help us minimize overall makespan. We compare the performance of CoMuDi using both ST-RRT* and RRT* planners with varying time bounds, demonstrating that the combination of CoMuDi and ST-RRT* leads to a higher success rate while minimizing makespan. Finally, we evaluate CoMuDi on six assemblies with up to 49 pieces and up to 9 robots. In those scenarios, we show that CoMuDi returns robot paths that exhibit low idle times, thereby demonstrating that CoMuDi can reliably solve large-scale assemblies.

</details>

---

### [[20_Research/Papers/具身智能/Acoustic-driven_millimetric_helical_robot_ultrasonic_synergistic_manipulation_in_confined_fluidic_environment|Acoustic-driven millimetric helical robot: ultrasonic synergistic manipulation in confined fluidic environment]]

![[assets/2608.05746_figure.png|800]]

- **arXiv**: [2608.05746](https://arxiv.org/abs/2608.05746)
- **PDF**: https://arxiv.org/pdf/2608.05746
- **详细分析**: [[20_Research/Papers/具身智能/Acoustic-driven_millimetric_helical_robot_ultrasonic_synergistic_manipulation_in_confined_fluidic_environment|Acoustic-driven millimetric helical robot: ultrasonic synergistic manipulation in confined fluidic environment]]
- **作者**: Hanlin Wang, Xin Wang, Xinwei Wei, Jiaxu Liu, Le Wang, Shengze Cai, Chao Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Acoustic-driven millimetric helical robot: ultrasonic synergistic manipulation in confined fluidic environment》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Acoustic field-driven manipulation provides a non-contact and non-invasive strategy for controlling microscale and nanoscale objects, yet its extension to millimeter-scale robots was limited by insufficient propulsion efficiency in confined biological environments. Here, a coordinated multi-acoustic-field approach is introduced, which harnesses the synergistic action of acoustic radiation forces and acoustic streaming flows to enable controlled locomotion of millimeter-scale helical robots and enhance propulsion. Multiphysics simulations captured the dynamics of millimeter-scale helical robots under combined acoustic fields, and experimental validation demonstrated their locomotion capabilities, including planar navigation, inclined climbing, and vertical motion. Semi-autonomous navigation experiments further confirmed that ultrasonic synergy substantially improved maneuverability. In vitro tests in porcine venous vessels demonstrated that coordinated acoustic fields supported both unidirectional and reciprocating motion under biologically relevant confinement. These findings provide mechanistic insight into scaling acoustic micromanipulation to the millimetre regime and support biomedical applications requiring versatile and controllable robotic mobility.

</details>

---

### [[20_Research/Papers/具身智能/In-Context_VLA_Endowing_Vision-Language-Action_Models_with_Language_via_In-Context_Post-Training_and_Agentic_Tool_Use|In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use]]

![[assets/2608.05738_figure.png|800]]

- **arXiv**: [2608.05738](https://arxiv.org/abs/2608.05738)
- **PDF**: https://arxiv.org/pdf/2608.05738
- **详细分析**: [[20_Research/Papers/具身智能/In-Context_VLA_Endowing_Vision-Language-Action_Models_with_Language_via_In-Context_Post-Training_and_Agentic_Tool_Use|In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use]]
- **作者**: Jiarui Yang, Wen Huang, Jiale Zhang, Maowei Hu, Hang Guo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.6（加权：具身智能 3，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《In-Context VLA: Endowing Vision-Language-Action Models with Language via In-Context Post-Training and Agentic Tool Use》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, Long-VLA, MemoryVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have become the dominant recipe for generalist manipulation, yet they are almost universally trained by behavior cloning: a policy imitates expert action chunks conditioned on a static image and a fixed instruction. A natural remedy is to inject explicit reasoning through textual chain-of-thought (CoT). We show, both empirically and analytically, that free-form textual CoT degrades low-level control: the reasoning it produces is ungrounded, its latency breaks closed-loop timing, and, crucially, the reasoning and action tokens are optimized against conflicting objectives so that the policy learns to narrate rather than to act. We argue that what a VLA needs is not the ability to generate language, but the ability to consume grounded language. To this end we introduce \textbf{\ourmethod{}}, a framework that endows a VLA with language competence through (i) in-context post-training, in which perceptual evidence is injected as structured context and the model is supervised only on actions, and (ii) an agentic tool-use interface, in which the policy queries open-vocabulary detectors, monocular depth, and a vision--language model to actively acquire task-relevant information. Rather than emitting a single templated caption, our data engine produces diverse, paraphrased, and evidence-conditioned spatial descriptions, so that the policy learns to interpret language it has never seen verbatim. Across the RoboCasa-GR1, SimplerEnv, and LIBERO simulation benchmarks, together with 8 real-world robot manipulation tasks, our method consistently achieves SOTA results in both performance and efficiency when compared with CoT-based approaches under matched configurations.

</details>

---

### [[20_Research/Papers/机器人/Near-sensor_Computing_for_Rapid_Visuotactile_Perception|Near-sensor Computing for Rapid Visuotactile Perception]]

![[assets/2608.05725_figure.png|800]]

- **arXiv**: [2608.05725](https://arxiv.org/abs/2608.05725)
- **PDF**: https://arxiv.org/pdf/2608.05725
- **详细分析**: [[20_Research/Papers/机器人/Near-sensor_Computing_for_Rapid_Visuotactile_Perception|Near-sensor Computing for Rapid Visuotactile Perception]]
- **作者**: Zhengying Zhu, Ruilin Zhang, Runze Hu, Chenxi Xiao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Near-sensor Computing for Rapid Visuotactile Perception》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuotactile sensors reconstruct dense contact geometry from measured surface gradients, but host-based processing increases power consumption and introduces data-transfer delays and variable scheduling latency, limiting the sensing and response speed of robotic systems. To address these limitations, we implement a near-sensor computing framework that includes a spectral Poisson solver as a fully streaming hardware pipeline. The computational core logic has an estimated power consumption of 347 mW and achieves high throughput without data-dependent branching or iterative convergence, thereby providing deterministic latency. Operating at 166 MHz, the pipeline produces the first depth value of each 128x128 frame 35,107 cycles after receiving the first input pixel, corresponding to a fixed latency of 0.211 ms. Across 15 contact geometries, the reconstructed depths differ from a double-precision reference by 0.17 % of the peak contact depth. On-chip decisions based on these reconstructions close a robot protective reflex loop in 28.3 +/- 4.9 ms, compared with 169.9 +/- 27.8 ms for an equivalent host-based loop using the same actuator. These results demonstrate that near-sensor reconstruction can provide accurate, energy-efficient, and deterministic tactile geometry on timescales suitable for rapid robotic contact responses.

</details>

---

### [[20_Research/Papers/具身智能/JoyAI-RA_0.5_Scaling_Robot_Manipulation_Learning_via_Dual_Action_Alignment|JoyAI-RA 0.5: Scaling Robot Manipulation Learning via Dual Action Alignment]]

![[assets/2608.05674_figure.png|800]]

- **arXiv**: [2608.05674](https://arxiv.org/abs/2608.05674)
- **PDF**: https://arxiv.org/pdf/2608.05674
- **详细分析**: [[20_Research/Papers/具身智能/JoyAI-RA_0.5_Scaling_Robot_Manipulation_Learning_via_Dual_Action_Alignment|JoyAI-RA 0.5: Scaling Robot Manipulation Learning via Dual Action Alignment]]
- **作者**: JoyAI-RA Team
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.5（加权：具身智能 1.2，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《JoyAI-RA 0.5: Scaling Robot Manipulation Learning via Dual Action Alignment》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World, Real-World, Vision-Language-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot data is scarce, so generalist policies need to learn from heterogeneous sources, including human egocentric video, simulation, and real robots, which differ in supervision and embodiment, with action labels missing or mutually incompatible. Human egocentric data scale best but sit farthest from robot data, and naive pooling causes negative transfer rather than knowledge sharing. We propose JoyAI-RA 0.5, a generalist Vision-Language-World-Action (VLWA) framework that couples physical world-dynamics priors with visual semantics and scales manipulation learning across such data via dual action alignment. Implicit action alignment infers latent actions from visual transitions, enabling action-free human, simulation, and robot data to guide a latent-action-conditioned world model in learning physical dynamics. Explicit alignment grounds reliable human and robot trajectories in a unified physical action space through a canonical action representation and camera-frame chunk-relative end-effector actions. An inner-outer-loop reinforcement stage then pairs efficient task adaptation with foundation-policy improvement. On a real-world AgiBot benchmark, JoyAI-RA performs strongly on both seen tasks and unseen variations. The task score improves consistently as the volume of human egocentric pretraining data increases and shows no sign of plateauing at our largest scale. This suggests that abundant but weakly labeled human experience can be converted into a transferable training signal, making human video not merely a weak auxiliary source but a primary axis along which manipulation capability can be scaled. Project page can be found at https://joyai-ra-05.github.io/.

</details>

---

### [[20_Research/Papers/大模型/KILVO_Kinematic-Inertial-LiDAR-Visual_Odometry_with_Robust_Multimodal_Adaptation_for_Humanoid_Robots|KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots]]

![[assets/2608.05647_figure.jpg|800]]

- **arXiv**: [2608.05647](https://arxiv.org/abs/2608.05647)
- **PDF**: https://arxiv.org/pdf/2608.05647
- **详细分析**: [[20_Research/Papers/大模型/KILVO_Kinematic-Inertial-LiDAR-Visual_Odometry_with_Robust_Multimodal_Adaptation_for_Humanoid_Robots|KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots]]
- **作者**: Jixin Gao, Fucheng Liu, Teng Zhang, Fusheng Zha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.5，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal

#### 研究背景与动机

《KILVO: Kinematic-Inertial-LiDAR-Visual Odometry with Robust Multimodal Adaptation for Humanoid Robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This article presents a kinematic-inertial-LiDAR-visual odometry for humanoid robots, called KILVO. Tailored to the platform features, requirements, and real-world complexity, it fully utilizes the sensors commonly equipped on humanoid robots, including joint encoders, IMU, LiDAR, and camera, within an asynchronous-sequential hybrid error-state iterated Kalman filter (ESIKF). Specifically, inertial data are used for prediction, leg kinematics are processed asynchronously at a high rate and provide proprioceptive constraints, while exteroception is updated sequentially, first by registering LiDAR points for geometric priors and then by updating the visual component via photometric errors. Moreover, the framework is elaborately designed with multimodal adaptation for resilience to sensor failures. A compact contact estimation module is also developed, sharing information with state estimation without additional sensors. Extensive experiments on public datasets and in the real world across multiple humanoid robots, gait patterns, and scenarios demonstrate that KILVO achieves highly competitive accuracy, efficiency, and output rates, with strong robustness against sensor degradation and failures, making it more suitable for humanoid robots than state-of-the-art fusion methods. Our code and datasets are released on GitHub.

</details>

---

### [[20_Research/Papers/机器人/Transcutaneous_Spinal_Cord_Stimulation_Disrupts_Conscious_Ankle_Proprioception_and_Produces_a_More_Constrained_Locomotor_Pattern_in_Unimpair|Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults]]

![[assets/2608.05635_first_page.png|800]]

- **arXiv**: [2608.05635](https://arxiv.org/abs/2608.05635)
- **PDF**: https://arxiv.org/pdf/2608.05635
- **详细分析**: [[20_Research/Papers/机器人/Transcutaneous_Spinal_Cord_Stimulation_Disrupts_Conscious_Ankle_Proprioception_and_Produces_a_More_Constrained_Locomotor_Pattern_in_Unimpair|Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults]]
- **作者**: Christopher A. Johnson, Andria J. Farrens, Parastoo Ali Pour, Arjan Gillan, Hui Zhong, David J. Reinkensmeyer, Alexandra S. Voloshina
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Transcutaneous Spinal Cord Stimulation Disrupts Conscious Ankle Proprioception and Produces a More Constrained Locomotor Pattern in Unimpaired Adults》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Transcutaneous spinal cord stimulation (tSCS) modulates spinal sensorimotor circuits primarily through activation of afferent networks. While prior work has emphasized locomotor performance and spinal excitability, how tSCS affects conscious proprioceptive perception and the extent to which such effects parallel changes in locomotor control remain unclear. We investigated the acute and training-related effects of tSCS on ankle proprioception and gait in unimpaired adults (n = 14), with an independent control group (n = 14) completing identical proprioceptive training without stimulation. Proprioception was quantified using a bilateral robotic assessment of dynamic ankle localization ability (Crisscross), gross motor output using maximum dorsiflexion strength, and gait during normal and tandem treadmill walking using spatiotemporal, trunk-sway, and mediolateral center-of-mass (CoM) excursion measures. Acute tSCS increased ankle proprioceptive error (p &lt; 0.001) while dorsiflexion strength was unchanged (p = 0.30). Gait shifted toward a modestly more constrained locomotor pattern, characterized by reduced step width and ML CoM excursion (p &lt; 0.05). With continued training under stimulation, proprioceptive error decreased and, unlike the control group, the tSCS group showed progressive improvement that persisted after stimulation ended. Sagittal-plane gait measures recovered toward or beyond baseline, whereas mediolateral measures remained constrained, revealing a direction-dependent reorganization of locomotor control. Together, these findings show that tSCS influences multiple aspects of the sensorimotor control loop, disrupting conscious proprioception while reshaping locomotor behavior, and that the nervous system can adapt to altered afferent input through training.

</details>

---

### [[20_Research/Papers/具身智能/PathCover_A_Fast_Convex_Decomposition_along_a_Path_via_Randomized_Iterative_Space_Partitioning_(RISP)_on_Point_Clouds|PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds]]

![[assets/2608.05586_figure.png|800]]

- **arXiv**: [2608.05586](https://arxiv.org/abs/2608.05586)
- **PDF**: https://arxiv.org/pdf/2608.05586
- **详细分析**: [[20_Research/Papers/具身智能/PathCover_A_Fast_Convex_Decomposition_along_a_Path_via_Randomized_Iterative_Space_Partitioning_(RISP)_on_Point_Clouds|PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds]]
- **作者**: Kunal S. Narkhede, Abhijeet M. Kulkarni, Guoquan Huang, Ioannis Poulakakis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《PathCover: A Fast Convex Decomposition along a Path via Randomized Iterative Space Partitioning (RISP) on Point Clouds》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robot navigation requires the rapid generation of obstacle-free regions for trajectory planning. However, existing corridor generators struggle to meet real-time, sensor-rate computational constraints. To resolve this bottleneck, we introduce PathCover, a framework driven by RISP; a novel randomized algorithm that constructs convex polytopes directly from raw point cloud data in expected linear time under a mild probabilistic elimination condition. PathCover generates sequences of overlapping, obstacle-free polytopes that safely constrain downstream MPC and trajectory optimization. We mathematically guarantee that the algorithm terminates in finite steps while ensuring continuous progress along any obstacle-free reference path. Extensive benchmarks on synthetic and real-world LiDAR datasets demonstrate an order-of-magnitude speedup over state-of-the-art methods while maintaining comparable corridor volumes. The complete pipeline is validated via high-fidelity quadrotor simulations and physical deployment on a quadrupedal robot navigating constrained environments using live LiDAR perception.

</details>

---

### [[20_Research/Papers/具身智能/ARGUS_Aligning_Robot_Scene_Geometry_Under_Shifting_Views_with_Large_3D_Vision_Models|ARGUS: Aligning Robot Scene Geometry Under Shifting Views with Large 3D Vision Models]]

![[assets/2608.05579_figure.png|800]]

- **arXiv**: [2608.05579](https://arxiv.org/abs/2608.05579)
- **PDF**: https://arxiv.org/pdf/2608.05579
- **详细分析**: [[20_Research/Papers/具身智能/ARGUS_Aligning_Robot_Scene_Geometry_Under_Shifting_Views_with_Large_3D_Vision_Models|ARGUS: Aligning Robot Scene Geometry Under Shifting Views with Large 3D Vision Models]]
- **作者**: Rishik Sathua, Haonan Chen, Katherine Driggs-Campbell
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《ARGUS: Aligning Robot Scene Geometry Under Shifting Views with Large 3D Vision Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale visuomotor policies have demonstrated impressive performance across a wide range of robot manipulation tasks. However, despite this success, manipulation polices often entangle scene geometry with the corresponding viewpoint, learning where objects lie in an image rather than where it lies in the task space. This entanglement inherently limits the corresponding policy's ability to learn from viewpoint-diverse datasets (ex. DROID, BridgeV2) and generalize beyond the viewpoints captured in their training data. In this work, we present ARGUS, an observation pre-processing pipeline that uses large-scale 3D vision models to align image observations from arbitrary camera viewpoints into a canonical viewpoint before passing it to downstream visuomotor policies. Experiments across training datasets with varying levels of viewpoint diversity, from fixed multi-view camera configurations to highly varied camera placements, show that our method consistently outperforms prior approaches across both limited-view and view-diverse training regimes. In efficiency comparisons, ARGUS demonstrates an ability to learn from view-diverse data, converging to high success rates 4-6x faster than previous methods by leveraging a simplified observation space. Overall, our findings show that leveraging large-scale 3D vision models reduces the learning burden on visuomotor policies, enabling more efficient learning from large-scale, viewpoint-diverse robot datasets.

</details>

---

### [[20_Research/Papers/机器人/Sliding_Sensors_Configurable_Confidence_in_State_Estimation_for_Continuum_Robots|Sliding Sensors: Configurable Confidence in State Estimation for Continuum Robots]]

![[assets/2608.05410_figure.png|800]]

- **arXiv**: [2608.05410](https://arxiv.org/abs/2608.05410)
- **PDF**: https://arxiv.org/pdf/2608.05410
- **详细分析**: [[20_Research/Papers/机器人/Sliding_Sensors_Configurable_Confidence_in_State_Estimation_for_Continuum_Robots|Sliding Sensors: Configurable Confidence in State Estimation for Continuum Robots]]
- **作者**: Ella Walsh, Spencer Teetaert, Eric Diller, Timothy D. Barfoot, Jessica Burgner-Kahrs
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Sliding Sensors: Configurable Confidence in State Estimation for Continuum Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuum robots often operate in uncertain environments, where accurate state estimation is essential for safe interactions. Estimate uncertainty is inherently spatially non-uniform: confidence varies depending on where measurements are available. Global estimation accuracy is not always the top priority, but rather achieving sufficient confidence at task-relevant locations along the robot. This extended abstract introduces mechanically reconfigurable sensing enabling uncertainty-shaping in state estimation for continuum robots. We present a concept hardware design demonstrating the feasibility of longitudinal translation of a sensor within a continuum robot. We demonstrate that state estimation confidence can be reconfigured by varying the sensor location, and show a reduction of full-body shape estimation errors when sliding the sensor back and forth over time, compared to a single fixed tip sensor.

</details>

---
