# cs.RO | Robotics | 2026-08-03

#arxiv #ComputerScience

**论文数**: 19

### [[20_Research/Papers/具身智能/Diagnosing_Compositional_Generalization_in_Sequential_Robot_Tasks|Diagnosing Compositional Generalization in Sequential Robot Tasks]]

![[assets/2607.29687_figure.png|800]]

- **arXiv**: [2607.29687](https://arxiv.org/abs/2607.29687)
- **PDF**: https://arxiv.org/pdf/2607.29687
- **详细分析**: [[20_Research/Papers/具身智能/Diagnosing_Compositional_Generalization_in_Sequential_Robot_Tasks|Diagnosing Compositional Generalization in Sequential Robot Tasks]]
- **作者**: Yixiao Wang, Cheng-En Wu, Lingfeng Sun, Pengcheng Wang, Xiang Ji, Boyuan Liang, Guojian Zhan, Masayoshi Tomizuka
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Diagnosing Compositional Generalization in Sequential Robot Tasks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Interleave-VLA, VIMA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sequential robot manipulation requires policies to execute novel combinations of familiar instruction components. However, collecting demonstrations for all possible instruction tuples is combinatorially expensive, while sparsely covered datasets often fail under out-of-distribution recombination. This paper studies compositional generalization through the lens of instruction-space coverage. We decompose the generalization gap into three sources: \textit{marginal instruction shift}, \textit{instruction-compositional shift}, and \textit{context--action shift}. This decomposition allows us to diagnose when sparse training coverage is sufficient, and what structure the training set must preserve for reliable action prediction. Our results show that exhaustive tuple enumeration is unnecessary: a structured subset, as small as one quarter of the full task space, can recover strong out-of-distribution performance when it covers action-relevant dependencies. We further find that sparse training often fails due to instruction steering rather than missing low-level skills; finetuning only one demonstration per task improves OOD success from \(0.4\%\) to \(54.7\%\). For semantically dependent tasks, effective coverage must capture relational structure rather than only factor diversity. These findings suggest that efficient robot data collection should prioritize dependency coverage in instruction space over exhaustive task expansion. More results are available in the supplementary material. Project website: https://yixiaowang7.github.io/Diagnosing_Compositional_Generalization_Robot_Page/.

</details>

---

### [[20_Research/Papers/机器人/Bootstrapping_Self-Supervised_Learning_of_Binary_Classification_Using_Error_Bounds_A_Case_Study_on_a_Robotic_Insertion_Task|Bootstrapping Self-Supervised Learning of Binary Classification Using Error Bounds: A Case Study on a Robotic Insertion Task]]

![[assets/2607.29640_figure.png|800]]

- **arXiv**: [2607.29640](https://arxiv.org/abs/2607.29640)
- **PDF**: https://arxiv.org/pdf/2607.29640
- **详细分析**: [[20_Research/Papers/机器人/Bootstrapping_Self-Supervised_Learning_of_Binary_Classification_Using_Error_Bounds_A_Case_Study_on_a_Robotic_Insertion_Task|Bootstrapping Self-Supervised Learning of Binary Classification Using Error Bounds: A Case Study on a Robotic Insertion Task]]
- **作者**: Zebin Duan, Norbert Krüger, Juan Heredia, Thorbjørn Mosekjær Iversen, Frederik Hagelskjær
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Bootstrapping Self-Supervised Learning of Binary Classification Using Error Bounds: A Case Study on a Robotic Insertion Task》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flexible manufacturing requires rapid deployment of solutions and minimal setup time to remain competitive. An essential attribute is the ability to control error levels, as failures can range from minor performance degradation to severe equipment damage. However, conventional deployment often involves extensive setup, data collection, model training or parameter tuning, and system testing, resulting in significant delays that hinder commercial feasibility. We propose a data engine which gathers data and improves its performance while executing the task. The data engine consists of two classifiers, a fast model prediction and expensive verification. First, a model prediction is performed and based on the confidence level of the prediction, the expensive verification can be used. By adjusting the confidence level, users can control the level of tolerable error. Our method is implemented on a real-world robotic insertion task, which uses force data for the model prediction. The system applies UMAP dimensionality reduction and uses Wilson-Score to compute the confidence bounds of the prediction. Results demonstrate the ability to learn and reduce the need for expensive verifications over time, while staying within the set error-rate. The results highlight the potential of confidence bounds in self-improving models to enhance reliability in robotic classification task.

</details>

---

### [[20_Research/Papers/机器人/Balancing_of_Humanoid_with_Object_Mass_Trade-off_Analyses_and_Lifting_Control|Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control]]

![[assets/2607.29625_first_page.png|800]]

- **arXiv**: [2607.29625](https://arxiv.org/abs/2607.29625)
- **PDF**: https://arxiv.org/pdf/2607.29625
- **详细分析**: [[20_Research/Papers/机器人/Balancing_of_Humanoid_with_Object_Mass_Trade-off_Analyses_and_Lifting_Control|Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control]]
- **作者**: Hyunjong Song, William Z. Peng, Joo H. Kim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The demand for humanoid loco-manipulation tasks with an object has recently increased, and most existing control approaches for stability in such tasks rely on heuristics or machine-learning techniques. This study rigorously analyzes and exploits the dynamic effects of the object mass on balance stability. By formulating the object mass parameters in the whole-body dynamics with distributed contact wrenches and centers of pressure at the stance contacts, their nonlinear effects on the system momenta and constraints are quantified. The dynamic models and constraints are incorporated into the construction of the balanced state basin/boundary (BSB), a partition of the center-of-mass state space for a biped system to maintain balance in its desired contacts. The implications of the BSB for prediction and control are highlighted using a humanoid robot and an analytically tractable reduced-order mechanism. The BSBs under different conditions of base of support, actuation capacity, and pose provide systematic analyses of the effects of object mass on the balancing capability of a system. In particular, the trade-off relationships between momentum regulation and limiting factors in balancing are characterized, introducing two key quantities of the object: the critical mass, at which the system's balancing capability is maximum, and the transition mass, which activates different limiting factors. In addition, sufficient conditions for imposing balanced states on a trajectory are established and implemented with BSBs as explicit threshold constraints in the whole-body trajectory optimization for stable object-lifting control of the humanoid, demonstrating the lift-and-hold and lift-and-release tasks with distinct mass properties in simulations and experiments.

</details>

---

### [[20_Research/Papers/具身智能/HAM-VLN_Harnessing_Hierarchical_Agentic_Memory_for_Zero-Shot_Vision-and-Language_Navigation|HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation]]

![[assets/2607.29600_figure.png|800]]

- **arXiv**: [2607.29600](https://arxiv.org/abs/2607.29600)
- **PDF**: https://arxiv.org/pdf/2607.29600
- **详细分析**: [[20_Research/Papers/具身智能/HAM-VLN_Harnessing_Hierarchical_Agentic_Memory_for_Zero-Shot_Vision-and-Language_Navigation|HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation]]
- **作者**: An Liu, Bingxi Liu, Hongyu Ding, Yixuan Jiang, Yaran Chen, Fulin Tang, Cong Leng, Hong Zhang, Jian Cheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《HAM-VLN: Harnessing Hierarchical Agentic Memory for Zero-Shot Vision-and-Language Navigation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-and-language navigation (VLN) enables robots to follow instructions in previously unseen environments. Recently, a training-free paradigm has emerged: the robot queries a multimodal LLM to understand its observations and plan the next action. However, long-horizon navigation based on either image streams or dense map inevitably introduces a growing memory and reasoning bottleneck. We present HAM-VLN, a decision-coupled, agent-authored memory that equips the robot with a persistent, depth-grounded world graph. In the same model call used to select the next action, HAM-VLN also records semantic and reflective information---including room type, objects, navigation progress, and failure notes. Recent waypoints remain verbatim within a bounded window, while older history re-enters the context only through retrieval scored by relevance, recency, and salience, together with one-hop topological expansion. This design requires no additional LLM calls beyond the per-waypoint decision. Compared to previous methods, HAM-VLN not only improves various navigation metrics but also reduces the context length by more than 65%. Specifically, HAM-VLN achieves 61.0% Success Rate (SR) on VLN-CE R2R, 52.7% SR on VLN-CE RxR, and 79.7% SR on HM3D-v2 ObjectNav without any training.

</details>

---

### [[20_Research/Papers/具身智能/Safe_Vision_Language_Action_Models_via_Barrier_Enhanced_Flow_Matching|Safe Vision Language Action Models via Barrier Enhanced Flow Matching]]

![[assets/2607.29569_figure.png|800]]

- **arXiv**: [2607.29569](https://arxiv.org/abs/2607.29569)
- **PDF**: https://arxiv.org/pdf/2607.29569
- **详细分析**: [[20_Research/Papers/具身智能/Safe_Vision_Language_Action_Models_via_Barrier_Enhanced_Flow_Matching|Safe Vision Language Action Models via Barrier Enhanced Flow Matching]]
- **作者**: Kasra Sinaei, Hung-Chieh Wu, Donald Ebeigbe
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Safe Vision Language Action Models via Barrier Enhanced Flow Matching》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This article presents a modular inference framework that integrates Flow Matching generative models with formal Control Barrier Function (CBF) safety guarantees. Unlike existing methods that apply external safety filters to a model's final output, our approach modifies the Flow Matching denoising process within the model to inherently generate safe trajectories. By employing a smooth Log-Sum-Exponential aggregate barrier, we enforce safety over entire action chunks. This aggregate barrier ensures a minimal increase in computational overhead and does not alter the semantic intent of the model. We show that, within the proposed framework, the 2-Wasserstein distance between the generated distribution and the target distribution remains bounded. Our method eliminates the need for safety-specific datasets or costly model retraining, providing a versatile solution for safe inference. We validate the approach on two robotic manipulation platforms and a 2D navigation benchmark, verifying that our framework achieves reliable safety without degrading the success rate of the model.

</details>

---

### [[20_Research/Papers/具身智能/TransGraspNet_Physically_and_Geometrically_Consistent_Manipulation_of_Transparent_Labware|TransGraspNet: Physically and Geometrically Consistent Manipulation of Transparent Labware]]

![[assets/2607.29567_figure.png|800]]

- **arXiv**: [2607.29567](https://arxiv.org/abs/2607.29567)
- **PDF**: https://arxiv.org/pdf/2607.29567
- **详细分析**: [[20_Research/Papers/具身智能/TransGraspNet_Physically_and_Geometrically_Consistent_Manipulation_of_Transparent_Labware|TransGraspNet: Physically and Geometrically Consistent Manipulation of Transparent Labware]]
- **作者**: Hailing Hu, Mingyi Zhu, Yiquan An, Yifei Tian, Tianyou Zuo, Lifeng Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《TransGraspNet: Physically and Geometrically Consistent Manipulation of Transparent Labware》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, Dex-Net, GraspNet, Real-World, ResNet, TDCNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulating transparent laboratory glassware that contains liquid is inherently safety-critical: even small geometric errors can cause unstable grasps and hazardous spillage. Although recent progress has been made in transparent object perception and robotic grasping, most existing systems optimize detection, depth reconstruction, and grasp planning independently, which leads to cross-stage inconsistency imperfect boundaries induce depth bleeding, distorted surfaces corrupt normal estimation, and task agnostic grasp scoring yields tilted or off-center grasps that fail under dynamic motion. In this paper, we propose TransGraspNet, a geometry physics consistent framework that explicitly enforces consistency from perception to execution through three coupled principles: boundary consistency to produce structurally reliable object contours as downstream priors, surface consistency to preserve geometric fidelity and surface normal accuracy during depth reconstruction, and physics consistency to refine grasp selection with centroid alignment and wrench-space stability for upright and dynamically robust manipulation. We evaluate TransGraspNet on public benchmarks, a dedicated transparent glassware dataset, and a real robotic platform. The results show improved boundary quality and surface normal fidelity, and demonstrate strong task-level performance in cluttered transparent scenes. Most importantly, the proposed system achieves reliable real-world operation, including high grasp success rates in clutter and zero spillage during high speed liquid transport, highlighting the effectiveness of our method.

</details>

---

### [[20_Research/Papers/机器人/Homotopy-Aware_Corridor_Generation_without_Predefined_Reference_Paths|Homotopy-Aware Corridor Generation without Predefined Reference Paths]]

![[assets/2607.29513_figure.png|800]]

- **arXiv**: [2607.29513](https://arxiv.org/abs/2607.29513)
- **PDF**: https://arxiv.org/pdf/2607.29513
- **详细分析**: [[20_Research/Papers/机器人/Homotopy-Aware_Corridor_Generation_without_Predefined_Reference_Paths|Homotopy-Aware Corridor Generation without Predefined Reference Paths]]
- **作者**: Haoze Dong, Minghan Li, Meng Guo, Zhongkui Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Homotopy-Aware Corridor Generation without Predefined Reference Paths》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating safe corridors is essential for collision-free robotic motion planning, yet most existing methods rely on predefined reference paths, which bias corridor geometry and implicitly limit the homotopy classes that can be explored. We propose a reference-path-free corridor generation framework on graphs of convex sets (GCS) that constructs corridors directly as sequences of convex sets, allowing corridor structure to emerge from the free-space representation rather than from a guiding path. To reason about similarity among corridors, we extend visibility-based deformation from paths to convex-set sequences, enabling the fusion of topologically redundant corridors while preserving distinct alternatives. To overcome the limited adaptability of existing GCS methods based on static global decompositions, we further develop an adaptive multi-scale GCS, in which a sampling-based fine-scale graph supports localized updates and a visibility-based coarse-scale graph enables compact global exploration. The two levels maintain topological consistency, allowing incremental updates without full graph reconstruction under environmental uncertainty. Numerical experiments characterize GCS construction, corridor generation, homotopy-aware exploration, and local updates, showing efficient graph construction, stable trajectory-level performance, and shorter-duration homotopy-aware trajectories than existing baselines. Hardware experiments on ground and aerial robots, including deployment with onboard localization, further validate the framework under translated and previously unknown obstacles.

</details>

---

### [[20_Research/Papers/机器人/Tri-Space_Operational_Control_of_Redundant_Multilink_and_Hybrid_Cable-Driven_Parallel_Robots_Using_an_Iterative-Learning_based_Reactive_Appr|Tri-Space Operational Control of Redundant Multilink and Hybrid Cable-Driven Parallel Robots Using an Iterative-Learning based Reactive Approach]]

![[assets/2607.29500_first_page.png|800]]

- **arXiv**: [2607.29500](https://arxiv.org/abs/2607.29500)
- **PDF**: https://arxiv.org/pdf/2607.29500
- **详细分析**: [[20_Research/Papers/机器人/Tri-Space_Operational_Control_of_Redundant_Multilink_and_Hybrid_Cable-Driven_Parallel_Robots_Using_an_Iterative-Learning_based_Reactive_Appr|Tri-Space Operational Control of Redundant Multilink and Hybrid Cable-Driven Parallel Robots Using an Iterative-Learning based Reactive Approach]]
- **作者**: Dipankar Bhattacharya, Yin Pok Chan, Siqi Shang, Yuen Shan Chan, Ying Tan, Darwin Lau
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Tri-Space Operational Control of Redundant Multilink and Hybrid Cable-Driven Parallel Robots Using an Iterative-Learning based Reactive Approach》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cable-Driven Parallel Robots (CDPRs) are a type of parallel mechanism in which cables are used as actuators. Due to the two levels of redundancy and numerous constraints within the CDPR actuation, joint and operational spaces (together known as the tri-space), tracking a given trajectory in the operational space while satisfying constraints in tri-space simultaneously is challenging. To the best of the authors' knowledge, there does not exist any tri-space control framework, which is robust, effective, and directly applicable to several architectures of redundantly actuated CDPRs. This paper proposes a tri-space control framework that combines Reactive Control (RC) and Iterative-Learning Control (ILC) to perform repetitive tasks in the operational space. The framework allows the tracking of operational space trajectories online with feasible cable forces, while avoiding undesirable situations such as cable-link interference, joint interference, and loss of manipulability. On the other hand, by finding an optimal parameter in the null space using a novel parameterization of a null space vector, the performance can be improved through ILC when the task is repeatedly executed. Simulation and hardware results on various Multilink Cable-Driven Robot (MCDRs) and Hybrid Cable-Driven Robots (HCDRs) show that the proposed tri-space control framework can be conveniently and effectively applied to the real-time control of different CDPRs.

</details>

---

### [[20_Research/Papers/大模型/Temporal_Policy_History-Initialized_Action_Generation_for_Robotic_Learning_from_Demonstration|Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration]]

![[assets/2607.29482_figure.png|800]]

- **arXiv**: [2607.29482](https://arxiv.org/abs/2607.29482)
- **PDF**: https://arxiv.org/pdf/2607.29482
- **详细分析**: [[20_Research/Papers/大模型/Temporal_Policy_History-Initialized_Action_Generation_for_Robotic_Learning_from_Demonstration|Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration]]
- **作者**: Dylan Miller, Martin Jagersand
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Temporal Policy: History-Initialized Action Generation for Robotic Learning from Demonstration》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

By relying on independent couplings from uninformative Gaussian priors, standard diffusion and flow matching models are forced to learn complex, high-cost vector fields to reach the physical action space. Generative models excel at capturing multimodal behaviors for robotic Learning from Demonstration (LfD), but often suffer from high inference cost. This paper introduces Temporal Policy, a generative framework based on stochastic interpolants that formulates action generation as a temporally coupled transport problem. By initializing the generative flow at the robot's recent history, we explicitly couple past states to future action sequences. This data-dependent coupling reduces transport cost and produces straight vector fields. We validate Temporal Policy across visuomotor simulation benchmarks and on a physical Barrett WAM 2x 7DoF teleoperation platform. Our approach reduces transport costs by nearly an order of magnitude compared to noise-initialized baselines, achieving a 19.1 ms inference latency on a single NVIDIA RTX 4080. Crucially, these geometric and computational efficiencies are achieved while matching the success rates of state-of-the-art baselines. This simplified transport geometry bypasses the computational bottleneck of independent Gaussian priors, helping enable high-frequency, closed-loop control. The code is publicly available at https://github.com/dmiller12/TemporalPolicy.

</details>

---

### [[20_Research/Papers/机器人/Automated_Straight-line_Sewing_of_Stretchable_Fabrics_with_Different_Lengths|Automated Straight-line Sewing of Stretchable Fabrics with Different Lengths]]

![[assets/2607.29464_figure.png|800]]

- **arXiv**: [2607.29464](https://arxiv.org/abs/2607.29464)
- **PDF**: https://arxiv.org/pdf/2607.29464
- **详细分析**: [[20_Research/Papers/机器人/Automated_Straight-line_Sewing_of_Stretchable_Fabrics_with_Different_Lengths|Automated Straight-line Sewing of Stretchable Fabrics with Different Lengths]]
- **作者**: Bingchen Jin, Akinari Kobayashi, Dipankar Bhattacharya, Akira Seino, Fuyuki Tokuda, Norman Chihnan Tien, Kazuhiro Kosuge
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Automated Straight-line Sewing of Stretchable Fabrics with Different Lengths》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Different Length Alignment Sewing (DLAS), which involves stretching the shorter fabric to match the longer one and sewing them together in a straight line, is a challenging task that needs to satisfy several requirements when automating the sewing process. To address the challenges, this research proposes a novel robotic sewing system, Different Length Robotic Sewing System (DLRoSS), which consists of a roller type end-effector, attached to a 6-DoF manipulator. The end-effector composed of active shorter and longer fabric rollers, and a passive press-roller attached to the shorter-fabric roller. Assuming that one end of the two fabric layers are initially positioned under the sewing machine's presser foot, the system automates DLAS by operating in four distinct phases. (P1) Fabric wrapping: Individual fabric layers are picked, held, and wrapped from the other end onto the feed rollers. (P2) Sewing: During the sewing, the shorter fabric is stretched and aligned with the longer fabric in real-time using roller velocity control based on the sewing speed and apriori known length ratio. (P3) Sewing completion: In the final sewing round on the fabric rollers, the press roller is engaged to prevent the stretched fabric from slipping off due to internal tension. (P4) Sewing fabric release: At the end of sewing, the fabric edge moves past the press roller, and the fabric releases from the rollers. Experimental results demonstrate that DLRoSS achieves consistent, high-quality sewing of stretchable fabrics of different materials and lengths.

</details>

---

### [[20_Research/Papers/大模型/AquaJEPA_Action-Conditioned_Multimodal_Predictive_Representations_for_Underwater_Robot_Dynamics|AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics]]

![[assets/2607.29393_figure.png|800]]

- **arXiv**: [2607.29393](https://arxiv.org/abs/2607.29393)
- **PDF**: https://arxiv.org/pdf/2607.29393
- **详细分析**: [[20_Research/Papers/大模型/AquaJEPA_Action-Conditioned_Multimodal_Predictive_Representations_for_Underwater_Robot_Dynamics|AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics]]
- **作者**: Alan-Barsag Gazzaev, Alexey Gavrilov, Sergey Muravyov
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能, 世界模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，世界模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《AquaJEPA: Action-Conditioned Multimodal Predictive Representations for Underwater Robot Dynamics》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underwater robots combine complementary sensors whose reliability changes abruptly with water visibility, viewpoint, and vehicle motion. We introduce AquaJEPA, an action-conditioned joint-embedding predictive model that fuses an RGB camera, forward-looking sonar, and proprioception with explicit sensor validity. It predicts a future latent target conditioned on eight-thruster commands and supplies velocity and sonar-profile predictions to a shared receding-horizon planner. We study the method in Stonefish against reactive, state-only, ordinary multimodal, supervised dynamics, and recurrent world-model baselines. We further isolate the EMA target, action margin, masks, and modality dropout. A preregistered 120-environment replication comprises five independent replicates of a grid crossing three unseen obstacle maps, four water-visibility coefficients, and nominal versus shifted dynamics, while intermittently removing DVL observations. In 120 fresh paired environments with scheduled DVL loss, AquaJEPA reaches 74 goals, versus 68 for both state-only and the recurrent world model, and attains the lowest mean final error (0.906 m). Paired final-error reductions relative to ordinary multimodal prediction, supervised dynamics, and the recurrent world model are 0.273 m (95% CI: 0.190-0.356), 0.364 m (0.260-0.468), and 0.106 m (0.025-0.187), respectively. AquaJEPA therefore achieves the best aggregate closed-loop performance and significantly outperforms three action-conditioned predictive baselines in paired final error; its advantage over state-only remains statistically unresolved.

</details>

---

### [[20_Research/Papers/大模型/SAGP_Semantic_Affordance-Guided_Grasp_Planning_via_Coarse-Zone_VLM_Reasoning|SAGP: Semantic Affordance-Guided Grasp Planning via Coarse-Zone VLM Reasoning]]

![[assets/2607.29374_figure.png|800]]

- **arXiv**: [2607.29374](https://arxiv.org/abs/2607.29374)
- **PDF**: https://arxiv.org/pdf/2607.29374
- **详细分析**: [[20_Research/Papers/大模型/SAGP_Semantic_Affordance-Guided_Grasp_Planning_via_Coarse-Zone_VLM_Reasoning|SAGP: Semantic Affordance-Guided Grasp Planning via Coarse-Zone VLM Reasoning]]
- **作者**: Muhayy Ud Din, Irfan Hussain
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《SAGP: Semantic Affordance-Guided Grasp Planning via Coarse-Zone VLM Reasoning》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, Dex-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geometry-based grasp planners ensure physically valid grasps but ignore functional semantics, often generating grasps that are antipodal and collision-free yet practically inappropriate, for example, gripping a mug by its rim, a knife by the blade, or a bottle near its cap. These inconsistencies cause the downstream task to fail even when traditional grasp metrics are met. Existing vision-language model (VLM) approaches either depend on fine-grained, category-specific part segmentation or attempt to directly infer grasp poses, with the latter prone to spatial hallucinations. As a result, no practical, training-free framework has yet been proposed that robustly links high-level semantic reasoning to geometric grasp planning. We introduce Semantic Affordance-Guided Grasp Planning (SAGP), a training-free pipeline built on a coarse-zone abstraction layer. The method first partitions the object point cloud into spatial regions (top, middle, bottom, lateral sides, and protrusions) by applying PCA-based alignment followed by distance-driven DBSCAN clustering, entirely bypassing learned segmentation. A pre-trained VLM then assesses the grasp quality of each region through a structured zero-shot query, and the resulting zone-wise scores are fused with geometric, reachability, and task-alignment signals to re-rank antipodal grasp candidates. Experiments on YCB objects in PyBullet with a Franka Panda robot show that SAGP preserves the high success rate of geometry-only planning while substantially improving the functional appropriateness of selected grasps, particularly on asymmetric, handle-bearing objects where geometry alone is uninformative. The introduced coarse-zone abstraction offers an effective, training-free bridge between VLM-based reasoning and geometric grasp planning, without the need for fine-grained part segmentation.

</details>

---

### [[20_Research/Papers/强化学习/TRACT_Temporally_Routed_Action_Chunks_with_Chronological_Phase_Authority_for_Contact-Rich_Manipulation|TRACT: Temporally Routed Action Chunks with Chronological Phase Authority for Contact-Rich Manipulation]]

![[assets/2607.29285_figure.png|800]]

- **arXiv**: [2607.29285](https://arxiv.org/abs/2607.29285)
- **PDF**: https://arxiv.org/pdf/2607.29285
- **详细分析**: [[20_Research/Papers/强化学习/TRACT_Temporally_Routed_Action_Chunks_with_Chronological_Phase_Authority_for_Contact-Rich_Manipulation|TRACT: Temporally Routed Action Chunks with Chronological Phase Authority for Contact-Rich Manipulation]]
- **作者**: Jiahao Liu, Kento Kawaharazuka, Tasuku Makabe, Kei Okada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TRACT: Temporally Routed Action Chunks with Chronological Phase Authority for Contact-Rich Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action chunking shortens the effective decision horizon of robot imitation learning by predicting multiple future actions, while conventional phase conditioning describes the current control instant. When a predicted horizon crosses a procedural boundary, assigning the current phase to the entire chunk creates a structural temporal mismatch. We present TRACT, which factorizes phase-structured action chunking into an accepted current phase and a single CURRENT-to-NEXT boundary inside the future horizon. A task-local graph constrains chronological phase authority, and a cumulative boundary distribution monotonically routes future queries through phase-specific query and action paths. For contact execution, a causal response-deficit integrator compares policy intent with ACK-eligible subsequent motion, accumulates arm compensation when directional response is suppressed, and decays after confirmed recovery. Across six real-robot variants with ten trials each, full TRACT achieves 10/10 full-sequence success, 99.00 [88.75, 100.00]% median [min, max] wipe completion, zero observed phase ambiguity, and zero stalls. Under the current complete method package and evaluation setting, the routed representation obtains better observed task results than the flat package (6/10 vs. 3/10 success; 77.08% vs. 8.03% median wipe completion). Chronological authority reduces observed phase ambiguity from 8/10 to 0/10, and response integration reduces stalls from 4/10 to 0/10. The package comparison does not isolate routing from other generator-package differences.

</details>

---

### [[20_Research/Papers/具身智能/TacPrint_A_Wearable_Fingertip_Tactile_Sensor_for_Human-to-Robot_Contact_Reproduction|TacPrint: A Wearable Fingertip Tactile Sensor for Human-to-Robot Contact Reproduction]]

![[assets/2607.29231_figure.png|800]]

- **arXiv**: [2607.29231](https://arxiv.org/abs/2607.29231)
- **PDF**: https://arxiv.org/pdf/2607.29231
- **详细分析**: [[20_Research/Papers/具身智能/TacPrint_A_Wearable_Fingertip_Tactile_Sensor_for_Human-to-Robot_Contact_Reproduction|TacPrint: A Wearable Fingertip Tactile Sensor for Human-to-Robot Contact Reproduction]]
- **作者**: Yongxi Liu, Chaofan Zhang, Xingyu Zhang, Xiangyin Bao, Boyue Zhang, Shaowei Cui, Shuo Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《TacPrint: A Wearable Fingertip Tactile Sensor for Human-to-Robot Contact Reproduction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-centric data collection is emerging as a significant paradigm for robot skill acquisition, but seamlessly integrating low-cost, scalable tactile sensing systems that capture fine-grained fingertip interactions without compromising natural operation remains a key challenge. This reduces the reliability of human-to-robot transfer in contact-rich tasks. In this work, we present TacPrint, a wearable fingertip tactile sensor, where protrusions on the inner surface of the silicone skin are aligned one-to-one with 24 capacitive taxels to enable localized capacitive responses. A real-to-sim-to-real pipeline estimates a 35 $\times$ 26 contact-depth map from 24-channel capacitive signals. Against simulation-generated labels, the model achieved a contact-region RMSE of 0.223 $\pm$ 0.161 mm, a weighted-centroid error of 1.213 $\pm$ 2.379 pixels, and an IoU of 0.829 $\pm$ 0.169. With measured capacitive inputs, the network-predicted depth evaluated at the guide-calibrated contact center showed a mean absolute error of 0.085 $\pm$ 0.057 mm across all 40 controlled trials, while the mean contact-position error was 0.250 $\pm$ 0.208 mm across the 37 trials whose reference contact regions were not truncated by the sensing boundary. In human-to-robot replay, tactile-guided compensation increased grasping and wiping success rates from 0% to 91.67% and 90%, respectively. In closed-loop grasping, dense-depth feedback achieved success rates of 87.5% over all tested positions and 85% under edge-contact conditions, compared with 67.5% and 45% for raw-taxel feedback.

</details>

---

### [[20_Research/Papers/机器人/Event-Based_Upper-Body_Humanoid_Teleoperation_Under_Challenging_Illumination|Event-Based Upper-Body Humanoid Teleoperation Under Challenging Illumination]]

![[assets/2607.29227_figure.png|800]]

- **arXiv**: [2607.29227](https://arxiv.org/abs/2607.29227)
- **PDF**: https://arxiv.org/pdf/2607.29227
- **详细分析**: [[20_Research/Papers/机器人/Event-Based_Upper-Body_Humanoid_Teleoperation_Under_Challenging_Illumination|Event-Based Upper-Body Humanoid Teleoperation Under Challenging Illumination]]
- **作者**: Haoyu Fu, Zhou Ge, Chengze Li, Chenzhao Sun, Ze Cui, Wenjing Zhou, Xulei Qin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《Event-Based Upper-Body Humanoid Teleoperation Under Challenging Illumination》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a real-time upper-body human-to-humanoid motion imitation framework driven by neuromorphic event-based vision. This work addresses practical perceptual bottlenecks of conventional frame-based RGB sensors, specifically their difficulty in high dynamic range (HDR) scenes and rapid motions due to fixed integration times. By leveraging the Prophesee EVK4 event camera, which operates asynchronously with high temporal resolution and a dynamic range exceeding 120 dB, our system supports stable tracking in conditions where standard vision pipelines degrade, such as severe backlighting and very low light environments below 5 lux. The architecture integrates a low-latency Perception Module, utilizing optimized event accumulation and gravity-aligned inertial fusion, with a causal Motion Module (TWIST) that performs online kinematic retargeting. We validate the system on an embedded NVIDIA Booster T1 platform and an 18-DoF humanoid upper-body setup, demonstrating an end-to-end photon-to-action latency of 23-34 ms and advantages over RGB baselines under our experimental setup. The results indicate a practical trade-off: events can be preferable for fast or poorly lit upper-body teleoperation, whereas well-lit static scenes may favor RGB or hybrid sensing.

</details>

---

### [[20_Research/Papers/机器人/MROPE_A_Multi-Robot_Safe_Cooperative_Strategy_via_combined_Predictive_Safety_Filters_and_Ellipse-based_Constraint_Compression|MROPE: A Multi-Robot Safe Cooperative Strategy via combined Predictive Safety Filters and Ellipse-based Constraint Compression]]

![[assets/2607.29203_figure.png|800]]

- **arXiv**: [2607.29203](https://arxiv.org/abs/2607.29203)
- **PDF**: https://arxiv.org/pdf/2607.29203
- **详细分析**: [[20_Research/Papers/机器人/MROPE_A_Multi-Robot_Safe_Cooperative_Strategy_via_combined_Predictive_Safety_Filters_and_Ellipse-based_Constraint_Compression|MROPE: A Multi-Robot Safe Cooperative Strategy via combined Predictive Safety Filters and Ellipse-based Constraint Compression]]
- **作者**: Alice Rosetti, Lorenzo Pichierri, Domenico Cappello, Fabrizio Schiano, Giuseppe Notarstefano
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《MROPE: A Multi-Robot Safe Cooperative Strategy via combined Predictive Safety Filters and Ellipse-based Constraint Compression》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying drone swarms to track a dynamic target in cluttered environments presents severe computational and safety challenges. We propose MROPE, a hierarchical strategy that decouples the cooperative monitoring mission from strict local safety requirements. To overcome the computational bottlenecks typical of dense spaces, our approach dynamically aggregates complex obstacle geometries into a single safe bounding ellipse for each drone. Methodologically, this architecture is realized by combining distributed aggregative optimization for high-level swarm coordination, a decentralized consensus scheme for the safe area computation, and local Predictive Safety Filters (PSF) for real-time collision avoidance. Virtual and real-world experiments validate the framework, demonstrating superior real-time efficiency and scalability compared to centralized approaches.

</details>

---

### [[20_Research/Papers/具身智能/D-VLC_Decentralized_Vision-Language_Collaboration_for_Heterogeneous_Embodied_Multi-Robot_Systems_in_Unknown_Environments|D-VLC: Decentralized Vision-Language Collaboration for Heterogeneous Embodied Multi-Robot Systems in Unknown Environments]]

![[assets/2607.29009_first_page.png|800]]

- **arXiv**: [2607.29009](https://arxiv.org/abs/2607.29009)
- **PDF**: https://arxiv.org/pdf/2607.29009
- **详细分析**: [[20_Research/Papers/具身智能/D-VLC_Decentralized_Vision-Language_Collaboration_for_Heterogeneous_Embodied_Multi-Robot_Systems_in_Unknown_Environments|D-VLC: Decentralized Vision-Language Collaboration for Heterogeneous Embodied Multi-Robot Systems in Unknown Environments]]
- **作者**: Yuan Zhou, Ruitong Lin, Shen Wang, Weiqi Gai, Mo zhu, Xin Zhou, Yuze Wu, Fei Gao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.2，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《D-VLC: Decentralized Vision-Language Collaboration for Heterogeneous Embodied Multi-Robot Systems in Unknown Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot systems, particularly heterogeneous robot swarms, can improve the efficiency of complex task execution through parallel collaboration and complementary capabilities. However, conventional rule-based methods rely on predefined task models and specialized decision making programs, making it difficult to understand complex semantic instructions and coordinate heterogeneous robots. LLMs introduce strong language understanding and task reasoning capabilities, allowing multi-robot systems to interpret instructions, decompose tasks, and assign roles according to task semantics. VLMs further incorporate visual perception, enabling robots to reason about objects, regions, and spatial relationships in physical environments. Nevertheless, existing LLM/VLM based methods often depend on known maps, centralized and synchronized decision making, limiting their generalization to heterogeneous robots and unseen tasks. We therefore propose a framework that combines decentralized asynchronous reasoning, lightweight information sharing, capability aware collaboration, and a unified action interface, enabling general purpose VLMs to generate robot specific actions executed by learning free experts without task or robot specific training. Experiments across diverse scenarios and multiple VLMs show success rates above 70\%, with completion time reduced by up to 55.8\% relative to the geometric greedy baseline.

</details>

---

### [[20_Research/Papers/机器人/Receding-Horizon_Next-Best-View_Planner_for_Autonomous_Leaf_Surface_Reconstruction|Receding-Horizon Next-Best-View Planner for Autonomous Leaf Surface Reconstruction]]

![[assets/2607.28995_figure.png|800]]

- **arXiv**: [2607.28995](https://arxiv.org/abs/2607.28995)
- **PDF**: https://arxiv.org/pdf/2607.28995
- **详细分析**: [[20_Research/Papers/机器人/Receding-Horizon_Next-Best-View_Planner_for_Autonomous_Leaf_Surface_Reconstruction|Receding-Horizon Next-Best-View Planner for Autonomous Leaf Surface Reconstruction]]
- **作者**: Arif Ahmed, Sajal K. Das, Parikshit Maini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Receding-Horizon Next-Best-View Planner for Autonomous Leaf Surface Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate plant leaf modeling is fundamental to downstream tasks such as plant growth monitoring, and phenotyping for yield estimation. Autonomous robotic reconstruction for large-scale field deployment must address limitations on robot planning budget and computation resources while optimizing viewpoint utility for leaf surface reconstruction. Existing approaches either focus on rigid objects, point-cloud coverage or plant reconstruction without fully addressing the system limitations or exploiting task-driven point cloud utility. In this work, we study next-best-view (NBV) planning for leaf surface reconstruction under travel constraints. We develop a novel Centroid-based Information Gain (CIG) function that measures the spatial distribution of observed points relative to the centroid of the existing point cloud to compute viewpoint utility. We also develop a receding-horizon variant that reasons over future viewpoints. To benchmark our work, we use the LAST-STRAW [1] public dataset that includes point clouds of strawberry plants over different growth stages and compare our method with attention-driven NBV [2] that uses a visibility-based information gain approach. The proposed receding-horizon approach consistently reduces surface reconstruction error and improves geometric fidelity across multiple growth stages, especially under increased inter-leaf occlusion. Results demonstrate that our approach is able to visit viewpoints that reduce surface reconstruction error and improves reconstruc-tion accuracy as compared to the baseline by upto 10%.

</details>

---

### [[20_Research/Papers/具身智能/Advances,_challenges,_and_opportunities_for_legged_robots|Advances, challenges, and opportunities for legged robots]]

![[assets/2607.28952_figure.png|800]]

- **arXiv**: [2607.28952](https://arxiv.org/abs/2607.28952)
- **PDF**: https://arxiv.org/pdf/2607.28952
- **详细分析**: [[20_Research/Papers/具身智能/Advances,_challenges,_and_opportunities_for_legged_robots|Advances, challenges, and opportunities for legged robots]]
- **作者**: Jonas Frey, Matías Mattamala, Hae-Won Park, Mayank Mittal, Georg Martius, Maike Osborne, Robert Sparrow, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Advances, challenges, and opportunities for legged robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid and quadrupedal robots have the potential to revolutionize the way we work, interact, and coexist with intelligent machines. To understand their effects on society and how they can enable scientific discovery, we assess the current capabilities of these systems along hardware, locomotion, autonomy, data, and applications. We identify recent advances and key open challenges that must be overcome to enable widespread adoption and new use cases for legged robots. Last, we provide an outlook on the future of legged robots, exploring their ethical considerations, economic potential, policy implications, and broader societal effects.

</details>

---
