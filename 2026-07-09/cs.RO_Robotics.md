# cs.RO | Robotics | 2026-07-09

#arxiv #ComputerScience

**论文数**: 22

### [[20_Research/Papers/具身智能/Continuous_and_large-scale_ELEANOR,_the_soft_architected_arm_inspired_by_the_elephant_trunk|Continuous and large-scale: ELEANOR, the soft architected arm inspired by the elephant trunk]]

![[assets/2607.07622_first_page.png|800]]

- **arXiv**: [2607.07622](https://arxiv.org/abs/2607.07622)
- **PDF**: https://arxiv.org/pdf/2607.07622
- **详细分析**: [[20_Research/Papers/具身智能/Continuous_and_large-scale_ELEANOR,_the_soft_architected_arm_inspired_by_the_elephant_trunk|Continuous and large-scale: ELEANOR, the soft architected arm inspired by the elephant trunk]]
- **作者**: Giovanna A. Naselli, Anderson B. Nardin, Seonggun Joe, Ryan Drinkwater, Enrico Donato, Diego Bianchi, Egidio Falotico, Michel C. Milinkovitch, Lucia Beccai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Continuous and large-scale: ELEANOR, the soft architected arm inspired by the elephant trunk》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The elephant trunk is a dexterous and versatile manipulator whose performance is still unmatched in robotics. In previous works, modularity was prioritized and relatively small-scale continuum robots were built. We take the natural proboscis of the *Loxodonta africana* species as a model and propose a different design approach which favors structural continuity and dynamic properties that plausibly emulate those of the natural trunk, while conferring high adaptability to the environment and humans. Instead of targeting prescribed behaviors, we show that a biomimetic design based on the macroscopic properties of the natural system enables elephant-like movements and grasping. We build by 3D printing an 85 cm long, compliant, tapered, volumetrically tessellated continuum arm, which is combined with tendon-driven actuation mimicking the longitudinal and oblique muscles of the natural model. We demonstrate whole-body grasping of objects having different shapes and dimensions and discuss a comparison to the biological trunk highlighting aspects of both biology and robotics.

</details>

---

### [[20_Research/Papers/机器人/Context-Aware_Force_Estimation_for_Deformable_Tool_Manipulation_in_Robotic_Environmental_Swabbing_via_Few-Shot_Continual_Adaptation|Context-Aware Force Estimation for Deformable Tool Manipulation in Robotic Environmental Swabbing via Few-Shot Continual Adaptation]]

![[assets/2607.07574_figure.png|800]]

- **arXiv**: [2607.07574](https://arxiv.org/abs/2607.07574)
- **PDF**: https://arxiv.org/pdf/2607.07574
- **详细分析**: [[20_Research/Papers/机器人/Context-Aware_Force_Estimation_for_Deformable_Tool_Manipulation_in_Robotic_Environmental_Swabbing_via_Few-Shot_Continual_Adaptation|Context-Aware Force Estimation for Deformable Tool Manipulation in Robotic Environmental Swabbing via Few-Shot Continual Adaptation]]
- **作者**: Siavash Mahmoudi, Chaitainya Kuppar Reddy, Yang Tian, Dongyi Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Context-Aware Force Estimation for Deformable Tool Manipulation in Robotic Environmental Swabbing via Few-Shot Continual Adaptation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic surface swabbing requires sustained interaction between a compliant tool and heterogeneous environments, where accurate estimation of tip-level contact force is critical for consistent sampling performance. However, deformable tool dynamics introduce nonlinear viscoelastic hysteresis that decouples wrist-mounted force measurements from true contact forces, while tool-integrated sensors are impractical for deployment due to sterility and disposability constraints. This paper presents a data-driven framework for contact force estimation in Deformable Tool Manipulation (DTM) that leverages proprioceptive sensing without requiring explicit physical models or permanent embedded sensing hardware at the tool tip. A recurrent architecture is first identified through a comparative evaluation of temporal models, where a compact LSTM achieves the lowest estimation error and sub-millisecond inference latency. To address generalization across unseen surfaces and tool compliance conditions, we introduce a parameter-isolated few-shot adaptation strategy that augments a frozen recurrent backbone with low-dimensional context embeddings using feature-wise linear modulation (FiLM). Experiments on a UR5e platform across nine tool-surface interaction regimes demonstrate that the proposed approach significantly improves robustness under domain shift, reducing zero-shot estimation error by up to 63\% while preserving baseline performance without catastrophic forgetting. These results show that separating shared deformation-history dynamics from domain-specific conditioning enables reliable force estimation for DTM in non-stationary environments.

</details>

---

### [[20_Research/Papers/具身智能/Smooth_Operator_A_Real-Time_Sampling-Based_Algorithm_for_Kinematic_Hand_Retargeting|Smooth Operator: A Real-Time Sampling-Based Algorithm for Kinematic Hand Retargeting]]

![[assets/2607.07491_figure.png|800]]

- **arXiv**: [2607.07491](https://arxiv.org/abs/2607.07491)
- **PDF**: https://arxiv.org/pdf/2607.07491
- **详细分析**: [[20_Research/Papers/具身智能/Smooth_Operator_A_Real-Time_Sampling-Based_Algorithm_for_Kinematic_Hand_Retargeting|Smooth Operator: A Real-Time Sampling-Based Algorithm for Kinematic Hand Retargeting]]
- **作者**: Robert Jomar Malate, Erik Bauer, Norica Bacuieti, Stefanos Charalambous, Elvis Nava, Robert K. Katzschmann, Benedek Forrai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Smooth Operator: A Real-Time Sampling-Based Algorithm for Kinematic Hand Retargeting》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Advances in learning-based robotic manipulation, such as Vision-Language-Action (VLA) models and Video Action Models (VAMs), heavily rely on high-quality teleoperation data. Their capabilities are strictly upper-bounded by the quality of the underlying human demonstrations. Current gradient-based retargeting algorithms often converge to different local minima, resulting in jitter that affects data quality and teleoperation experience. To address this, we introduce the Sampling-Based Retargeter (SBR), a novel gradient-free retargeting method drawn from the rich literature of sampling-based control and explicitly designed for low-jitter, real-time kinematic retargeting. We evaluate SBR both in simulation and through a rigorous real-world user study involving 18 participants performing 3 complex manipulation tasks. Compared to gradient-based baselines, SBR achieved the highest overall task success rate (54.1%) while significantly reducing operator cognitive fatigue, recording the lowest NASA-TLX workload score (36.4 out of 100). Ultimately, we establish SBR as a highly effective, intuitive retargeter for dexterous manipulation, providing the community with a rigorous benchmarking methodology to guide future retargeting research.

</details>

---

### [[20_Research/Papers/机器人/Agent-Exploitation_Affordances_From_Basic_to_Complex_Representation_Patterns|Agent-Exploitation Affordances: From Basic to Complex Representation Patterns]]

![[assets/2607.07475_first_page.png|800]]

- **arXiv**: [2607.07475](https://arxiv.org/abs/2607.07475)
- **PDF**: https://arxiv.org/pdf/2607.07475
- **详细分析**: [[20_Research/Papers/机器人/Agent-Exploitation_Affordances_From_Basic_to_Complex_Representation_Patterns|Agent-Exploitation Affordances: From Basic to Complex Representation Patterns]]
- **作者**: Bastien Dussard, Aurélie Clodic, Guillaume Sarthou
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Agent-Exploitation Affordances: From Basic to Complex Representation Patterns》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotics, the capability of an artificial agent to represent the range of its action possibilities, i.e. affordances, is crucial to understand how it can act on its environment. While functional affordances, which refer to the use of tools and objects, have been broadly studied in knowledge representation, the implications of a social context and the presence of other agents have remained unexplored in this field. Consequently, in the field of social robotics, a multi-agent context enables the agents to engage in new actions that are potentially complementary to their individual capabilities, leading to the perspective of agentexploitation. This work focuses on the concept of cooperative affordance within the realm of social affordances. Cooperative affordances refer to situations where agents interact with each other to extend their action possibilities range. From this definition, this paper proposes a tractable ontological representation of this concept with the aim of making it usable by an artificial agent. Expanding on those elementary patterns, we illustrate the effectiveness of these representations by combining them to depict a diverse range of scenarios.

</details>

---

### [[20_Research/Papers/具身智能/GeoGS-SLAM_Geometry-Only_Gaussian_Splatting_for_Dense_Monocular_SLAM|GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM]]

![[assets/2607.07452_figure.png|800]]

- **arXiv**: [2607.07452](https://arxiv.org/abs/2607.07452)
- **PDF**: https://arxiv.org/pdf/2607.07452
- **详细分析**: [[20_Research/Papers/具身智能/GeoGS-SLAM_Geometry-Only_Gaussian_Splatting_for_Dense_Monocular_SLAM|GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM]]
- **作者**: Lipu Zhou, Yaoyun Kang, Junxiang Pang, Shengkai Sun, Tingting Bao, Kehan Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《GeoGS-SLAM: Geometry-Only Gaussian Splatting for Dense Monocular SLAM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dense visual SLAM is a fundamental problem in robotics. Recent advances in 3DGS have demonstrated its potential for dense SLAM. Existing 3DGS frameworks focus on both appearance and geometry modeling. However, scene geometry is typically more critical for SLAM than novel view synthesis because downstream robotic tasks, such as navigation and obstacle avoidance, rely primarily on accurate spatial geometry rather than photorealistic rendering. This observation raises a natural question: Is it feasible for 3DGS to perform 3D reconstruction without scene appearance modeling? Motivated by this, we propose Geometry-only Gaussian Splatting (GeoGS), which directly reconstructs scene geometry, and further present GeoGS-SLAM, a dense visual SLAM system built upon this representation. Specifically, GeoGS retains only spatial parameters to reduce the number of per-primitive parameters by over 80%. In contrast to existing 3DGS methods, GeoGS focuses solely on geometric reconstruction, which significantly reduces the number of Gaussian primitives, accelerates geometric convergence, and enhances robustness to illumination variations. In addition, we present an effective training framework that optimizes the Gaussian primitives via single-view and multi-view geometric and photometric supervision, and speeds up geometry convergence with a local-plane driven initialization that better aligns primitives with local structures. Furthermore, we introduce a map update strategy for loop closure that globally transforms the Gaussian map to align it with the corrected pose estimates, thereby preventing map tearing caused by inconsistent per-viewpoint pose corrections in existing methods. Extensive experiments on synthetic and real-world benchmarks demonstrate that our method outperforms SOTA methods in terms of online mapping efficiency and geometric reconstruction quality.

</details>

---

### [[20_Research/Papers/具身智能/Immersive_Social_Interaction_with_VR_and_LLM-Assisted_Humanoids|Immersive Social Interaction with VR and LLM-Assisted Humanoids]]

![[assets/2607.07430_figure.png|800]]

- **arXiv**: [2607.07430](https://arxiv.org/abs/2607.07430)
- **PDF**: https://arxiv.org/pdf/2607.07430
- **详细分析**: [[20_Research/Papers/具身智能/Immersive_Social_Interaction_with_VR_and_LLM-Assisted_Humanoids|Immersive Social Interaction with VR and LLM-Assisted Humanoids]]
- **作者**: Niraj Pudasaini, Geeta Chandra Raju Bethala, Pranav Doma, Anthony Tzes, Yi Fang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.5，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Immersive Social Interaction with VR and LLM-Assisted Humanoids》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots can extend human presence to remote, constrained, or hazardous environments, but existing teleoperation interfaces often require physically demanding motion tracking or cognitively demanding low-level control. This paper presents an immersive teleoperation framework that integrates voice-controlled locomotion, VR-based manipulation, and bidirectional social interaction for whole-body humanoid control. Using Apple Vision Pro, the operator receives egocentric visual feedback, issues natural-language locomotion commands, and teleoperates the robot's arms and dexterous hands through wrist and finger tracking. An LLM-assisted voice-control module converts spoken instructions into high-level locomotion commands, while the manipulation module retargets human hand motions to the robot through inverse kinematics and PD control. The system also records multimodal data, including egocentric RGB observations, voice/text commands, joint states, hand motions, and eye-gaze signals, supporting future imitation learning and autonomy. We evaluate the framework on a Unitree H1 humanoid equipped with dexterous hands in manipulation and social interaction tasks. Results show that novice users can successfully operate the system after brief familiarization, achieving 80\% success in object manipulation and 70\% success in a social cube-passing task. These results demonstrate the potential of immersive, language-assisted teleoperation as an accessible interface for humanoid interaction, remote assistance, and multimodal data collection.

</details>

---

### [[20_Research/Papers/具身智能/Multi-Agent_Robotic_Control_with_Onboard_Vision-Language_Models|Multi-Agent Robotic Control with Onboard Vision-Language Models]]

![[assets/2607.07403_figure.png|800]]

- **arXiv**: [2607.07403](https://arxiv.org/abs/2607.07403)
- **PDF**: https://arxiv.org/pdf/2607.07403
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Agent_Robotic_Control_with_Onboard_Vision-Language_Models|Multi-Agent Robotic Control with Onboard Vision-Language Models]]
- **作者**: Kajetan Rachwał, Maciej Majek, Bartłomiej Boczek, Jakub Matejczyk, Dominik Matejkowski, Adam Dąbrowski, Tim Seyde, Alexander Amini, Maria Ganzha
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Multi-Agent Robotic Control with Onboard Vision-Language Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision Language Models (VLMs) and Vision Language Action (VLA) models have shown promise in robotic control. Yet, they face significant challenges regarding explainability, generalization, and compute requirements. This paper presents a Multi-Agent System (MAS) architecture that addresses these limitations by deploying specialized agents on onboard hardware - eliminating dependence on external compute. The system controls a multi-purpose autonomous mobile manipulator in a simulated industrial warehouse, fulfilling five task categories: safety inspection, warehouse maintenance, warehouse search, package quality verification, and responding to human requests. Compact VLMs (3-20B parameters) are used throughout, with fine-tuning applied to improve package inspection accuracy. A novel "Megamind" orchestration agent mitigates context retention issues inherent to long-horizon planning with smaller models. The system was validated in a hardware-in-the-loop simulation using an AMD Ryzen(TM) AI mini PC. Results demonstrate that a fully onboard MAS architecture is a viable, cost-efficient alternative to cloud-dependent deployments, with strong potential for real-world transfer. The simulation environment has been released as open source under the Apache 2.0 licence.

</details>

---

### [[20_Research/Papers/机器人/PLED-VINS_A_Point-Line_Event-Based_Visual_Inertial_SLAM_for_Dynamic_Environments|PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments]]

![[assets/2607.07374_figure.png|800]]

- **arXiv**: [2607.07374](https://arxiv.org/abs/2607.07374)
- **PDF**: https://arxiv.org/pdf/2607.07374
- **详细分析**: [[20_Research/Papers/机器人/PLED-VINS_A_Point-Line_Event-Based_Visual_Inertial_SLAM_for_Dynamic_Environments|PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments]]
- **作者**: Seunghun Lee, Jihun Nam, Dong-Uk Seo, Hyun Myung
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《PLED-VINS: A Point-Line Event-Based Visual Inertial SLAM for Dynamic Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SegNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic environments remain a fundamental challenge for visual SLAM, where unreliable observations from moving objects and rapid motion degrade state estimation accuracy. Although event cameras preserve fine-grained spatio-temporal information, most existing event-based SLAM frameworks still assume static scenes and lack approaches to estimate the reliability of features. To this end, we propose PLED-VINS, a monocular event camera-based visual-inertial SLAM framework that enables robust state estimation in dynamic environments. We propose an entropy-recency score map to characterize the temporal reliability of both point and line features based on event temporal statistics. Concurrently, geometric reliability is estimated via a unified point-line robust bundle adjustment. Building upon these, we design an adaptive weighting strategy that fuses temporal and geometric reliability, including motion-conditioned reliability modeling for line features, to suppress unreliable observations. Experimental results demonstrate that PLED-VINS improves state estimation on the evaluated dynamic sequences with moving objects.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Reliable_Aerial_Ground_Vehicle_Collaboration_An_Integrated_Planning_and_Autonomy_Framework_for_Field_Deployment|Towards Reliable Aerial Ground Vehicle Collaboration: An Integrated Planning and Autonomy Framework for Field Deployment]]

![[assets/2607.07350_figure.png|800]]

- **arXiv**: [2607.07350](https://arxiv.org/abs/2607.07350)
- **PDF**: https://arxiv.org/pdf/2607.07350
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Reliable_Aerial_Ground_Vehicle_Collaboration_An_Integrated_Planning_and_Autonomy_Framework_for_Field_Deployment|Towards Reliable Aerial Ground Vehicle Collaboration: An Integrated Planning and Autonomy Framework for Field Deployment]]
- **作者**: Md Safwan Mondal, Luca Russo, James D. Humann, James M. Dotterweich, Pranav Bhounsule
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，强化学习 0.4，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Towards Reliable Aerial Ground Vehicle Collaboration: An Integrated Planning and Autonomy Framework for Field Deployment》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Limited flight endurance significantly restricts the operational range of unmanned aerial vehicles (UAVs) in long duration missions such as surveillance and inspection, where multiple spatially distributed Areas of Interest (AOIs) must be visited. These tasks require efficient routing determining the sequence of visits which directly impacts mission time, energy consumption, and overall feasibility. Pairing UAVs with unmanned ground vehicles (UGVs) for mobile recharging offers a promising solution, but introduces a tightly coupled cooperative routing problem involving UAV route planning, UGV road constrained movement, energy management, and rendezvous scheduling under uncertainty. In this work, we present an integrated planning and autonomy framework for reliable field deployment. We formulate the problem as an energy constrained cooperative routing task and solve it using a Deep Reinforcement Learning (DRL) based planner that jointly optimizes the UAV visitation sequence and rendezvous locations with the UGV, outperforming baseline heuristics in minimizing total mission time. To bridge the gap between planning and execution, we introduce a standardized two layer YAML based mission API that captures environment states and structures lightweight, synchronized action sequences. This framework is supported by a complete autonomy stack using PX4/MAVSDK for UAV control and ROS 2/Nav2 for UGV navigation. Furthermore, we propose a lightweight Rendezvous Aware Replanner (RARP) that operates online to handle environmental uncertainties, reducing energy margin violations from 83.33% to 20.00%. The full system is validated through outdoor field experiments, demonstrating robust cooperative navigation and adaptability in dynamic tasks, including a search and rescue scenario with vision language model (VLM) based hazard detection

</details>

---

### [[20_Research/Papers/具身智能/TouchWorld_A_Predictive_and_Reactive_Tactile_Foundation_Model_for_Dexterous_Manipulation|TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation]]

![[assets/2607.07287_figure.png|800]]

- **arXiv**: [2607.07287](https://arxiv.org/abs/2607.07287)
- **PDF**: https://arxiv.org/pdf/2607.07287
- **详细分析**: [[20_Research/Papers/具身智能/TouchWorld_A_Predictive_and_Reactive_Tactile_Foundation_Model_for_Dexterous_Manipulation|TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation]]
- **作者**: Jianyi Zhou, Feiyang Hong, Yunhao Li, Yicheng Zhao, Yongjue Cen, Zirui Liu, Jiakang Huang, Zirui Chen, Ruiyang Zhang, Weizhuo Zhu, Xuhua Song, Shuo Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 2.1，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《TouchWorld: A Predictive and Reactive Tactile Foundation Model for Dexterous Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：TouchWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation in everyday environments requires both anticipation and reaction: a robot must predict how contact should evolve while rapidly correcting local errors caused by slip, misalignment, unstable grasping, or force mismatch. Vision and language provide semantic and geometric guidance, but they cannot reliably reveal hidden contact states such as force, slip, and contact stability. Although tactile sensing exposes these physical cues, most existing policies treat touch as a low-frequency observation stream within a monolithic action model, coupling slow task reasoning, action generation, and fast contact feedback in a single loop. We introduce TouchWorld, a predictive-and-reactive tactile foundation model for dexterous manipulation. TouchWorld uses a hierarchical policy that separates vision-language subtask planning, tactile world-model prediction, visuo-tactile goal-conditioned action generation, and high-frequency tactile residual refinement. A High-Level Planning Layer produces executable subtasks and predicts tactile subgoals; a Visuo-Tactile Goal-Conditioned Policy generates nominal action chunks; and a Tactile-Conditioned Refinement Policy performs online residual correction using recent tactile and proprioceptive feedback. By using touch as both a predictive contact reference and a fast feedback signal, TouchWorld preserves the semantic generalization of vision-language-action policies while improving local contact adaptation. Across six long-horizon and contact-rich dexterous manipulation tasks, TouchWorld achieves 65.0% success in the clean setting and 53.7% success under human perturbations, outperforming the strongest baseline by 15.7 and 18.5 percentage points, respectively.

</details>

---

### [[20_Research/Papers/机器人/Programmable_Synchronization_Graphs_for_Adaptive_and_Fault-Tolerant_Modular_Miniature_Robots|Programmable Synchronization Graphs for Adaptive and Fault-Tolerant Modular Miniature Robots]]

![[assets/2607.07281_first_page.png|800]]

- **arXiv**: [2607.07281](https://arxiv.org/abs/2607.07281)
- **PDF**: https://arxiv.org/pdf/2607.07281
- **详细分析**: [[20_Research/Papers/机器人/Programmable_Synchronization_Graphs_for_Adaptive_and_Fault-Tolerant_Modular_Miniature_Robots|Programmable Synchronization Graphs for Adaptive and Fault-Tolerant Modular Miniature Robots]]
- **作者**: Okan Kulekcioglu, Arqam Bin Ahmad, Ines Garcia, Filipe Serra Alves, Onur Ozcan, M. Selim Hanay
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Programmable Synchronization Graphs for Adaptive and Fault-Tolerant Modular Miniature Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modular miniature robots could provide scalable function in constrained environments, but coordinating many imperfect modules remains difficult when computation, communication and reliability are limited. A central robotics challenge is to coordinate many actuator-sensor modules without assigning a privileged leader, prescribing a fixed gait template, or relying on dense communication. Here we introduce a programmable synchronization-graph framework for modular miniature robots in which each actuator-sensor pair is represented as a network node and locomotor coordination is encoded through graph coupling. Fixed intra-subgraph links synchronize heterogeneous actuator groups, whereas a small number of signed inter-subgraph links program phase relationships between groups. In physical robot collectives with up to nine modules, graph coupling drives the emergence of synchronization, signed links tune the phase difference from in-phase to out-of-phase motion, and floor experiments produce gallop-like and trot-like contact patterns in a five-module robot assembly. Replacing dense all-to-all coupling with sparse d-regular topologies preserves synchronization while reducing the coupling burden. The same graph representation also captures fault tolerance: increasing graph degree increases the number of module deactivations tolerated before desynchronization. Finally, an upper-confidence-bound edge-selection algorithm learns inter-subgraph links that drive the system toward target phase states. In a separate deactivation benchmark, the graph-based controller avoids the leader-specific failure mode observed in centralized leader-follower control and reduces worst-case phase error by about threefold. These results establish programmable network topology as a compact control layer for gait phase programming, online adaptation and robustness to unit loss in modular miniature robots.

</details>

---

### [[20_Research/Papers/具身智能/Manual,_Joystick,_or_Haptic_Control_An_In_Vitro_Comparison_of_Navigation_Strategies_for_Robotic_Interventional_Neuroradiology_Procedures|Manual, Joystick, or Haptic Control? An In Vitro Comparison of Navigation Strategies for Robotic Interventional Neuroradiology Procedures]]

![[assets/2607.07253_figure.png|800]]

- **arXiv**: [2607.07253](https://arxiv.org/abs/2607.07253)
- **PDF**: https://arxiv.org/pdf/2607.07253
- **详细分析**: [[20_Research/Papers/具身智能/Manual,_Joystick,_or_Haptic_Control_An_In_Vitro_Comparison_of_Navigation_Strategies_for_Robotic_Interventional_Neuroradiology_Procedures|Manual, Joystick, or Haptic Control? An In Vitro Comparison of Navigation Strategies for Robotic Interventional Neuroradiology Procedures]]
- **作者**: Benjamin Jackson, Nikola Fischer, Harry Robershaw, Xingyu Chen, S. H. Hadi Sadati, Yang Li, Jeremy Lynch, Nasr Abdelsalam, Jonathon Buwanabala, Matthew Benger, Sara Sciacca, Naga Kandasamy...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Manual, Joystick, or Haptic Control? An In Vitro Comparison of Navigation Strategies for Robotic Interventional Neuroradiology Procedures》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Objective: To evaluate robotic controller interfaces for interventional neuroradiology procedures in-vitro incorporating a force-sensing platform to assess safety. Methods: A custom endovascular robot, device-mimicking controller, and sensorized neurovascular phantom were developed. Ten interventional neuroradiologists (4 novices, 6 experts) performed simulated navigations using four control modalities: device-mimicking controllers with and without haptic feedback, joystick-based input, and manual navigation. Navigation time, peak vessel-wall forces, incorrect catheterisations, and prolapse events were assessed, alongside user analyses. Results: Manual navigation was fastest (mean 47.7 s) compared to haptic-on (248.7 s), haptic-off (314.7 s), and joystick (392.6 s) modalities (p&lt;0.001). Regardless of controller type, vessel-wall forces were below the 0.70 N puncture threshold; therefore all modalities were considered safe. Joystick produced significantly more prolapse events than manual control (1.56 vs 0.13; p=0.018). Operator experience was relevant to performance: experts made fewer incorrect catheterisations than novices (0.25 vs 0.62; p=0.035) and applied less vessel-wall force (p&lt;0.0005); these effects were sustained across controllers but accentuated when haptics were on. Users perceived haptic on and haptic off as similarly intuitive, and more intuitive than joystick (p=0.033). Conclusion: Device-mimicking robotic controllers outperform joystick interfaces on most metrics; haptic feedback shows promising but non-significant performance benefits.

</details>

---

### [[20_Research/Papers/机器人/Disturbance-aware_Motion_Planning_for_Over-actuated_Underwater_Vehicles_Exploiting_Actuation_Redundancy_for_High-fidelity_3D_Reconstruction|Disturbance-aware Motion Planning for Over-actuated Underwater Vehicles Exploiting Actuation Redundancy for High-fidelity 3D Reconstruction]]

![[assets/2607.07139_figure.png|800]]

- **arXiv**: [2607.07139](https://arxiv.org/abs/2607.07139)
- **PDF**: https://arxiv.org/pdf/2607.07139
- **详细分析**: [[20_Research/Papers/机器人/Disturbance-aware_Motion_Planning_for_Over-actuated_Underwater_Vehicles_Exploiting_Actuation_Redundancy_for_High-fidelity_3D_Reconstruction|Disturbance-aware Motion Planning for Over-actuated Underwater Vehicles Exploiting Actuation Redundancy for High-fidelity 3D Reconstruction]]
- **作者**: Yuer Gao, Tongqing Xu, Qingyang Liu, Yi Cai
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Disturbance-aware Motion Planning for Over-actuated Underwater Vehicles Exploiting Actuation Redundancy for High-fidelity 3D Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underwater robots often operate near delicate targets where high-power thrusters resuspend sediments and induce turbulence, degrading image quality at the sensor input. Conventional controllers optimize vehicle-centric objectives, such as tracking and stability, without accounting for the impact of actuation on sensing. We address this actuation-to-perception coupling by exploiting redundancy in over-actuated platforms. For an eight-thruster ROV, multiple thrust allocations can yield the same motion; we search this null space to minimize predicted disturbance in a task-relevant target region while enforcing motion constraints. Our method uses a control-oriented thruster-wake proxy derived from actuator-disk theory with directional attenuation and validated by PIV ($R^2 = 0.99$ near the wake axis; $R^2 &gt; 0.82$ in the primary wake region), together with a real-time redundancy-resolving allocator running at 10 Hz (45 ms/solve). Across 440 trials, the approach reduces target-region particle velocity by 67% ($p &lt; 0.001$), improves 3D reconstruction RMSE by 55% versus a disturbance-unaware baseline ($1.9 \pm 0.4$ mm vs. $4.3 \pm 1.8$ mm), and achieves a 98.5% reconstruction success rate. The framework supports autonomous scanning, which is quantitatively evaluated, and operator-assisted inspection, which is demonstrated in the supplementary materials.

</details>

---

### [[20_Research/Papers/大模型/Compositional_Motion_Generation_from_Demonstration_with_Object-Centric_Neural_Fields|Compositional Motion Generation from Demonstration with Object-Centric Neural Fields]]

![[assets/2607.07129_figure.png|800]]

- **arXiv**: [2607.07129](https://arxiv.org/abs/2607.07129)
- **PDF**: https://arxiv.org/pdf/2607.07129
- **详细分析**: [[20_Research/Papers/大模型/Compositional_Motion_Generation_from_Demonstration_with_Object-Centric_Neural_Fields|Compositional Motion Generation from Demonstration with Object-Centric Neural Fields]]
- **作者**: Ahmet Ercan Tekden, Yasemin Bekiroglu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Compositional Motion Generation from Demonstration with Object-Centric Neural Fields》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compositionality, by organizing complex behavior as combinations of simpler elements, enables robot learning that is scalable and data efficient. Leveraging this principle, we propose a generative learning-from-demonstration framework that enables compositional modeling of robotic behavior by connecting perception and motion through shared object-level representations. We render scenes from object-centric neural representations that integrate canonical neural fields with latent-conditioned deformations, capturing positional and geometric variations in a smooth, consistent, and interpretable way. For motion generation, a temporal mixture-of-experts (MoE) employs a gating mechanism to combine object-conditioned movement primitives over time, producing complete trajectories. This spatial-temporal compositionality maintains the data efficiency of movement primitives while grounding motion in visual structure, enabling systematic generalization across diverse scene configurations. In simulation, long-horizon manipulation tasks are successfully completed using the proposed model, which requires significantly less training data than other image-based baselines. Real-world experiments further demonstrate the method's robustness to noise, its ability to generalize at the category level through language-based segmentation models, and its capacity to operate directly on 3D scene representations.

</details>

---

### [[20_Research/Papers/具身智能/PriGo_Test-Time_Primitive_Guidance_to_Diffusion_and_Flow_Policies_for_Adaptive_Robotic_Manipulation|PriGo: Test-Time Primitive Guidance to Diffusion and Flow Policies for Adaptive Robotic Manipulation]]

![[assets/2607.07076_figure.png|800]]

- **arXiv**: [2607.07076](https://arxiv.org/abs/2607.07076)
- **PDF**: https://arxiv.org/pdf/2607.07076
- **详细分析**: [[20_Research/Papers/具身智能/PriGo_Test-Time_Primitive_Guidance_to_Diffusion_and_Flow_Policies_for_Adaptive_Robotic_Manipulation|PriGo: Test-Time Primitive Guidance to Diffusion and Flow Policies for Adaptive Robotic Manipulation]]
- **作者**: Zezeng Li, Enda Xiang, Thuy Tran, Di Huang, Momath Thiam, Liming Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《PriGo: Test-Time Primitive Guidance to Diffusion and Flow Policies for Adaptive Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GraspVLA, PANet, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning has enabled remarkable progress in robotic manipulation, especially with diffusion and flow-based policies that generate complex visuomotor behaviors directly from demonstrations. Yet, despite their strong performance, these policies often fail to generalize across tasks and environments. A key reason is that existing policies tend to imitate superficial action correlations rather than the underlying intent. Inspired by the compositional structure of human behaviors, we propose PriGo, a primitive-guided test-time adaptive framework for robust robotic manipulation. PriGo introduces PANet, a lightweight primitive prediction module that infers primitive distributions directly from observations. We further propose a differentiable primitive guidance mechanism that refines generated actions during inference, steering trajectories toward semantically consistent behaviors. Unlike prior primitive-conditioned approaches, PriGo operates entirely at test time and can be seamlessly integrated into pretrained diffusion and flow policies without retraining. Extensive experiments on LIBERO, CALVIN, SIMPLER, and real-world robotic tasks demonstrate that PriGo consistently improves robustness, long-horizon execution, and generalization ability across both diffusion and flow-based policies.

</details>

---

### [[20_Research/Papers/具身智能/A_Closed-Loop_Multi-Agent_Framework_for_Robust_Multi-Robot_Manipulation|A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation]]

![[assets/2607.06990_figure.png|800]]

- **arXiv**: [2607.06990](https://arxiv.org/abs/2607.06990)
- **PDF**: https://arxiv.org/pdf/2607.06990
- **详细分析**: [[20_Research/Papers/具身智能/A_Closed-Loop_Multi-Agent_Framework_for_Robust_Multi-Robot_Manipulation|A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation]]
- **作者**: Yi-Xiang He, Lan Wei, Haoming Cen, Jian-Jian Jiang, Zhuohao Li, Guanxing Lu, Yihan Yang, Dandan Zhang, Wei-Shi Zheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.5，大模型 0.6，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《A Closed-Loop Multi-Agent Framework for Robust Multi-Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot systems provide the parallelism and redundancy necessary for long-horizon tasks, while Large Language Models (LLMs) offer the reasoning capabilities to decompose these objectives into actionable plans. However, effectively grounding this high-level reasoning in physical multi-robot execution remains an open challenge. Existing LLM-based approaches fall mainly into two categories: Single-robot methods achieve robust contact-rich manipulation but lack the coordination mechanisms required for tasks spanning multiple workspaces. Current multi-robot frameworks focus on high-level planning, often treating manipulation as an idealized primitive that fails to account for real-world execution uncertainties. To address this, we propose a hierarchical closed-loop agentic LLM-based framework to ensure robust multi-robot manipulation. Our system consists of three specialized agents: the Planning Agent decomposes instructions into allocated sub-tasks, the Manipulation Agent for each robot executes actions via adaptive tool use, and the Verification Agent closes the loop by monitoring physical outcomes and feeding back semantic corrections. Extensive real-world experiments demonstrate that our framework achieves superior success rates, ensures robust adaptability ranging from single to cross workspace manipulation, and offers a generalizable approach for diverse manipulation tasks.

</details>

---

### [[20_Research/Papers/机器人/Ace!_Motion_Planning_of_Professional-Level_Table_Tennis_Serves_with_a_Robot_Arm|Ace! Motion Planning of Professional-Level Table Tennis Serves with a Robot Arm]]

![[assets/2607.06989_figure.png|800]]

- **arXiv**: [2607.06989](https://arxiv.org/abs/2607.06989)
- **PDF**: https://arxiv.org/pdf/2607.06989
- **详细分析**: [[20_Research/Papers/机器人/Ace!_Motion_Planning_of_Professional-Level_Table_Tennis_Serves_with_a_Robot_Arm|Ace! Motion Planning of Professional-Level Table Tennis Serves with a Robot Arm]]
- **作者**: Guillem Torrente, Guilherme Jorge Maeda, Divij Grover, Megumu Tsukamoto, Hamdi Sahloul, Peter Dürr
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，机器人 2.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Ace! Motion Planning of Professional-Level Table Tennis Serves with a Robot Arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Table tennis, a dynamic, compact, and popular sport, has received significant attention as a robotics benchmark over the last decades. Most of the research has focused on the rally aspect - returning an incoming ball - requiring high-speed vision, agile motion planning, and tight closed-loop control. However, the other component of table tennis gameplay - the serve - is comparatively a quite unexplored research problem, that in fact requires pushing physics modeling and control to the extremes. Achieving competitive serves with a robot presents domain-specific challenges, such as high-spin generation from a spinless ball, precise aiming, or multi-objective optimization. In this work, we present a novel approach for generating official rule-compliant serves by combining motion primitives, Model Predictive Control, and Bayesian Optimization. Serves generated in this way offer a wide and controllable variation of spins of up to 550 rad/s, and speeds of up to 6.7 m/s, matching and even surpassing those of elite table tennis players.

</details>

---

### [[20_Research/Papers/机器人/SPECTRA_Context-Conditioned_Spectral_Movement_Primitives_for_Robot_Skill_Generalization|SPECTRA: Context-Conditioned Spectral Movement Primitives for Robot Skill Generalization]]

![[assets/2607.06978_figure.png|800]]

- **arXiv**: [2607.06978](https://arxiv.org/abs/2607.06978)
- **PDF**: https://arxiv.org/pdf/2607.06978
- **详细分析**: [[20_Research/Papers/机器人/SPECTRA_Context-Conditioned_Spectral_Movement_Primitives_for_Robot_Skill_Generalization|SPECTRA: Context-Conditioned Spectral Movement Primitives for Robot Skill Generalization]]
- **作者**: Boxuan Zhang, Sheng Liu, Chenglin Ming, Ahmed Abdelrahman
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《SPECTRA: Context-Conditioned Spectral Movement Primitives for Robot Skill Generalization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot imitation learning for manipulation should preserve demonstrated task geometry while producing dynamically admissible robot motions. Existing pipelines often learn task-dependent trajectories and impose execution limits afterward through filtering, smoothing, clipping, or time scaling, which may distort task-critical end-effector paths. We propose the Spectral Movement Primitive (SMP), a frequency-domain imitation learning framework that couples task-space skill generation with joint-space execution regulation. Demonstrations are represented by truncated finite-horizon Fourier coefficients. An empirically selected low-frequency task band captures the dominant motion geometry, while higher harmonics contribute disproportionately to derivative growth. A frame-aware context-conditioned GMM/GMR prior predicts the task-band coefficients in a canonical task frame, and the resulting Cartesian trajectory is mapped to joint space through sequential inverse kinematics. A phase-coupled regulator then limits the requested phase progression without modifying the spectral coefficients, thereby enforcing joint velocity and acceleration limits while preserving the represented path. Experiments evaluate task-band reconstruction, robustness to composite demonstration corruption, out-of-distribution cross-board generalization, joint-space dynamic admissibility, end-effector path preservation, and deployment on a Franka Panda robot. Results show compact geometric reconstruction, consistent transfer across unseen task frames, substantial reductions in dynamic violations and jerk, and preservation of the intended end-effector path during phase regulation.

</details>

---

### [[20_Research/Papers/具身智能/EvoPlan_Evolutionary_Neuro-Symbolic_Robot_Planning_with_Spatio-Temporal_Guarantees|EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees]]

![[assets/2607.06724_figure.png|800]]

- **arXiv**: [2607.06724](https://arxiv.org/abs/2607.06724)
- **PDF**: https://arxiv.org/pdf/2607.06724
- **详细分析**: [[20_Research/Papers/具身智能/EvoPlan_Evolutionary_Neuro-Symbolic_Robot_Planning_with_Spatio-Temporal_Guarantees|EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees]]
- **作者**: Bhavya Sai Nukapotula, Samin Moosavi, Haoze Wang, Luke Duncan, Diya Shakkottai, Varun Murali, Srinivas Shakkottai
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《EvoPlan: Evolutionary Neuro-Symbolic Robot Planning with Spatio-Temporal Guarantees》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based robot planners are fluent but cannot guarantee that their plans are executable or safe. Classical PDDL planners can guarantee these properties, but only after the problem is fully specified, and they make poor use of an LLM's ability to read context and repair plans. This paper presents a neuro-symbolic framework with three parts. All LLM calls use a locally-hosted open-weight model, so the pipeline can be deployed on-robot with no cloud dependency. First, an offline procedure that mines a single global Signal Temporal Logic (STL) constraint on mobility from demonstration data. The procedure recovers codified rules (e.g., stopping at red lights, mined from nuPlan driving logs) or population preferences (e.g., social-navigation comfort, mined from SCAND teleoperation), depending on what the demonstrations encode. Because the demonstrations are a one-class signal, we generate the missing negatives with counterfactual perturbations and an LLM violation generator and then fit the constraint by evolutionary search. We use the mined constraint to shield a vision-language driving policy on Bench2Drive and two discrete-action navigation policies on HA-VLN-CE. Second, an evolutionary PDDL planner: an LLM proposes and repairs plans, programmatic validators decide which ones survive, and the validated portion of the plan grows over iterations. We test the planner on the open-world ALFWorld Text benchmark, where it beats strong baselines and stays robust when the goal vocabulary does not match the action-model vocabulary. Third, a constrained execution loop: the planner's plan is compiled into waypoints, the waypoints are checked against the mined constraint, and the planner re-plans on a violation. We illustrate the full pipeline via demonstrations using the Gazebo simulator.

</details>

---

### [[20_Research/Papers/大模型/CILC_Cryptographically-secure_Inter-agent_Loop_Closure_Candidate_Detection_for_Multi-Agent_Collaborative_SLAM|CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM]]

![[assets/2607.06700_figure.png|800]]

- **arXiv**: [2607.06700](https://arxiv.org/abs/2607.06700)
- **PDF**: https://arxiv.org/pdf/2607.06700
- **详细分析**: [[20_Research/Papers/大模型/CILC_Cryptographically-secure_Inter-agent_Loop_Closure_Candidate_Detection_for_Multi-Agent_Collaborative_SLAM|CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM]]
- **作者**: Andrew Fishberg, Yixuan Jia, Jonathan P. How
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《CILC: Cryptographically-secure Inter-agent Loop Closure Candidate Detection for Multi-Agent Collaborative SLAM》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent Simultaneous Localization and Mapping (SLAM) and collaborative SLAM (CSLAM) require robots to continuously exchange global descriptors (GDs) to detect inter-agent loop closures (ILCs). While encrypted radios protect this traffic from external eavesdroppers, they offer no protection against a compromised swarm member. We show this threat is concrete by demonstrating how a corrupted agent can reconstruct approximations of an honest agent's imagery and trajectory from its public GD broadcasts. To address this, we propose CILC (Cryptographically-secure Inter-agent Loop Closure candidate detection), a first-of-its-kind system leveraging Secure Multi-Party Computation (SMPC) to detect ILC candidates without exchanging GDs in the clear. Rather than securing the entire CSLAM pipeline, we apply SMPC only to ILC candidate detection (i.e., GD similarity comparison), a privacy-sensitive yet computationally lightweight step, yielding an advantageous privacy-to-overhead trade-off. We validate in both simulation and hardware experiments that CILC remains real-time and communication-feasible across multimodal GDs (visual and LiDAR), while mitigating information leakage to a compromised swarm agent.

</details>

---

### [[20_Research/Papers/强化学习/RoboSnap_One-Shot_Real-to-Sim_Scene_Generation_for_Generalizable_Robot_Learning_and_Evaluation|RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation]]

![[assets/2607.06699_figure.png|800]]

- **arXiv**: [2607.06699](https://arxiv.org/abs/2607.06699)
- **PDF**: https://arxiv.org/pdf/2607.06699
- **详细分析**: [[20_Research/Papers/强化学习/RoboSnap_One-Shot_Real-to-Sim_Scene_Generation_for_Generalizable_Robot_Learning_and_Evaluation|RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation]]
- **作者**: Shujie Zhang, Jingkun Yi, Weipeng Zhong, Zirui Zhou, Yangkun Zhu, Hanqing Wang, Xudong Xu, Weinan Zhang, Chunhua Shen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《RoboSnap: One-Shot Real-to-Sim Scene Generation for Generalizable Robot Learning and Evaluation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DROID-Sim, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recovering real-world scenes as interactive simulation environments can enable generalizable robot learning and reproducible policy evaluation. However, constructing scenes that are both physically stable and visually faithful remains slow and expensive. In this work, we present RoboSnap, a real-to-sim framework that turns a single RGB image into a simulation-ready scene. The key idea is a layered design that separates the physics-critical interaction area from the surrounding visual context: collision-aware foreground assets are refined for stable robot interaction, while a 3D Gaussian splatting visual layer preserves faithful background appearance under novel views. Experiments on DROID scenes and real-robot tasks show that RoboSnap achieves reliable trajectory replay in the recovered scenes, supports task-specific synthetic data generation for policy training, and yields meaningful sim-real correlation for policy evaluation. To further support real-to-sim research, we introduce DROID-Sim, a real-to-sim companion dataset constructed from 564 real-world scenes in DROID. Extensive experiments suggest that the value of real-to-sim methods lies not only in high-fidelity visual reconstruction, but in turning real environments into reusable infrastructure for robot learning and evaluation.

</details>

---

### [[20_Research/Papers/具身智能/NativeMEM_Native_Memory_Compression_for_Long-Horizon_Robotic_Manipulation|NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation]]

![[assets/2607.06678_figure.png|800]]

- **arXiv**: [2607.06678](https://arxiv.org/abs/2607.06678)
- **PDF**: https://arxiv.org/pdf/2607.06678
- **详细分析**: [[20_Research/Papers/具身智能/NativeMEM_Native_Memory_Compression_for_Long-Horizon_Robotic_Manipulation|NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation]]
- **作者**: Ziye Wang, Modi Shi, Chaojun Ni, Jiazhi Yang, Mengdi Li, Zhizhong Su, Tianwei Lin, Hongyang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《NativeMEM: Native Memory Compression for Long-Horizon Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MAP-VLA, MemoryVLA, OpenVLA, ReMem-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How can pretrained Vision-Language-Action (VLA) models retain long-horizon visual histories with high-frequency updates without sacrificing efficiency? Existing approaches rely on external memory management, which restrains either the memory horizon or the reactiveness of pretrained policies. To this end, we present NativeMEM, a VLA policy that features long-term and real-time updated memory. At its core is an efficient memory encoding scheme, Native Memory Compression, which repurposes the VLA's own vision encoder to compress each historical frame from each camera view into a single token. Appended to the input sequence, these memory tokens enable the pretrained VLA to attend over long-term history with negligible latency overhead, requiring neither an external planner nor a freshly initialized memory module. To align the memory tokens with the pretrained policy, we first develop a generic memory tokenizer under the supervision of a frozen VLA on memory-demanding data, and then unfreeze the VLA for task-specific fine-tuning. NativeMEM consistently outperforms prior methods, boosting success rates from 32.4% to 84.0% in simulation and up to 98.7% on real robots, while maintaining low inference latency and GPU memory usage. Notably, NativeMEM exhibits high data efficiency by achieving competitive results with prior arts using only 20% of the training data.

</details>

---
