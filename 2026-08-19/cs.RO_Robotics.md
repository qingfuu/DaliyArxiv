# cs.RO | Robotics | 2026-08-19

#arxiv #ComputerScience

**论文数**: 22

### [[20_Research/Papers/强化学习/Hydra-0_Action_Flow_for_Generalist_World_Modeling_and_Control|Hydra-0: Action Flow for Generalist World Modeling and Control]]

![[assets/2608.18077_figure.png|800]]

- **arXiv**: [2608.18077](https://arxiv.org/abs/2608.18077)
- **PDF**: https://arxiv.org/pdf/2608.18077
- **详细分析**: [[20_Research/Papers/强化学习/Hydra-0_Action_Flow_for_Generalist_World_Modeling_and_Control|Hydra-0: Action Flow for Generalist World Modeling and Control]]
- **作者**: Hongyu Li, Bowen Wen, Xinghao Zhu, Yixuan Wang, Yilun Du, Yunzhu Li, George Konidaris, Stan Birchfield, Soha Pouya, Chenran Li, Yan Chang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.0（加权：具身智能 0.3，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Hydra-0: Action Flow for Generalist World Modeling and Control》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Hydra-0, a generalist world model conditioned on action flow, which represents robot actions as pixel motion. This shared visual interface enables generalist world modeling and control by learning action consequences across embodiments, tasks, environments, and video-generation backbones. Our best configuration achieves 90.4% lower robot-motion error and 60.2% lower object-motion error than our action-conditioned baseline, while supporting zero-shot composition and data-efficient adaptation. On the RoboLab benchmark, Hydra-0 achieves a Pearson correlation of r=0.96 between replayed and reference success rates. Finally, we uncover an emergent inverse mode of this interface: a world action model that predicts compatible robot motion from desired object flow transferred from a human demonstration. A trained action head maps the resulting latent features to executable actions without requiring task-specific expert robot demonstrations. Together, these results demonstrate the potential of action flow as a shared control interface connecting heterogeneous training data, open-loop policy evaluation, and robot control.

</details>

---

### [[20_Research/Papers/大模型/PRISM_Precision_and_contact-rich_Real-world_Industrial_Skill_dataset_with_Multimodal_sensing|PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing]]

![[assets/2608.17962_figure.png|800]]

- **arXiv**: [2608.17962](https://arxiv.org/abs/2608.17962)
- **PDF**: https://arxiv.org/pdf/2608.17962
- **详细分析**: [[20_Research/Papers/大模型/PRISM_Precision_and_contact-rich_Real-world_Industrial_Skill_dataset_with_Multimodal_sensing|PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing]]
- **作者**: Tengbo Yu, Jiahao Wu, Hanning Wang, Rui Chen, Chuanhou Liu, Chuang Sun, Hangxin Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《PRISM: Precision and contact-rich Real-world Industrial Skill dataset with Multimodal sensing》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FurnitureBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent progress in robotic learning has been fueled by large-scale datasets collected in everyday environments. However, most existing datasets emphasize short-horizon, low-contact tasks such as pick-and-place, and therefore do not capture the precision control, force/torque or tactile regulation, and multimodal feedback required for industrial assembly. To address this gap, we introduce PRISM, a large-scale multimodal dataset for contact-rich industrial operations. The dataset spans more than 25 manipulation tasks (e.g., electronic components plug/unplug, conveyor-based sorting) and covers diverse mechanical constraints. PRISM includes more than 5,000 trajectories totaling 45 hours of teleoperated demonstrations, recorded using synchronized multi-view RGB-D, force/torque, tactile, and robot-state measurements. In contrast to datasets collected in household or laboratory settings, PRISM provides a realistic benchmark for multimodal perception and control under high-precision industrial constraints, and serves as a foundation for contact-rich, generalizable manipulation in real-world manufacturing environments. The dataset is open-sourced at: https://tengbo-yu.github.io/PRISM/

</details>

---

### [[20_Research/Papers/机器人/Jetson-ORB-SLAM3_Accuracy-Preserving_GPU_Implementation_for_Edge_Computing_Devices|Jetson-ORB-SLAM3: Accuracy-Preserving GPU Implementation for Edge Computing Devices]]

![[assets/2608.17874_figure.png|800]]

- **arXiv**: [2608.17874](https://arxiv.org/abs/2608.17874)
- **PDF**: https://arxiv.org/pdf/2608.17874
- **详细分析**: [[20_Research/Papers/机器人/Jetson-ORB-SLAM3_Accuracy-Preserving_GPU_Implementation_for_Edge_Computing_Devices|Jetson-ORB-SLAM3: Accuracy-Preserving GPU Implementation for Edge Computing Devices]]
- **作者**: Rajat Roy, Aditya Arun Kumar Yadav, Hardik Jain
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Systems

#### 研究背景与动机

《Jetson-ORB-SLAM3: Accuracy-Preserving GPU Implementation for Edge Computing Devices》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual-inertial SLAM on low-power edge platforms is constrained by the cost of dense feature extraction and loop closure. Prior GPU ports of ORB-SLAM trade accuracy for speed by approximating the ORB detector, altering the feature set and therefore the estimated trajectory. We present an accuracy-preserving GPU implementation of ORB-SLAM3 for the NVIDIA Jetson Orin Nano, whose GPU ORB front end reproduces the reference CPU detector algorithmically to 94.7% exact keypoint agreement and 99.9% descriptor bit agreement. This work also makes CNN-based loop closure edge-viable through native TensorRT. The visual front end (feature extraction) is offloaded to the GPU while the mapping and optimization back end is kept on the CPU, matching each computation to the hardware it suits. The accuracy is verified by comparing four configurations: the GPU pipeline and the unmodified CPU reference, each run on both the Jetson Orin Nano and a desktop. On EuRoC dataset, all four agree to within 0.10cm in mean absolute trajectory error (SE(3)), so neither the GPU port nor the change of hardware shifts the estimated trajectory. The GPU-versus-CPU comparison is reproducible on TUM-VI and KITTI datasets, so the acceleration is accuracy-preserving rather than approximate. The proposed implementation is competitive with published ORB-SLAM3 on EuRoC, attains sub-centimeter accuracy on five of the six TUM-VI room sequences, and reaches sub-1% relative translation error on nine of eleven KITTI sequences. For loop closure, the generic ONNX-Runtime CUDA/TensorRT execution providers are unusable with our CosPlace ResNet-50 on the embedded platform, whereas a native libnvinfer FP16 engine reduces per-query inference to 2.2ms, a 180x speedup. Learned place recognition therefore runs concurrently with tracking on a 7W device. In monocular-inertial mode the system sustains 32FPS mean over the eleven EuRoC sequences.

</details>

---

### [[20_Research/Papers/机器人/Effector-Centric_NMPC_of_Tiltable-Multirotors_for_Offset-Free_Omnidirectional_Aerial_Manipulation|Effector-Centric NMPC of Tiltable-Multirotors for Offset-Free Omnidirectional Aerial Manipulation]]

![[assets/2608.17819_first_page.png|800]]

- **arXiv**: [2608.17819](https://arxiv.org/abs/2608.17819)
- **PDF**: https://arxiv.org/pdf/2608.17819
- **详细分析**: [[20_Research/Papers/机器人/Effector-Centric_NMPC_of_Tiltable-Multirotors_for_Offset-Free_Omnidirectional_Aerial_Manipulation|Effector-Centric NMPC of Tiltable-Multirotors for Offset-Free Omnidirectional Aerial Manipulation]]
- **作者**: Jinjie Li, Yicheng Chen, Johannes Kübel, Haokun Liu, Junichiro Sugihara, Moju Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Effector-Centric NMPC of Tiltable-Multirotors for Offset-Free Omnidirectional Aerial Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial manipulation extends robotic operations to previously inaccessible aerial environments. Unlike arm-equipped aerial systems, tiltable-multirotors can directly generate six-degree-of-freedom wrenches through their flight bases, enabling both efficient movement and omnidirectional operation by tilting the thrust direction. This work presents a design analysis and a wrench-based control framework for tiltable-multirotors in aerial manipulation. We show that a four-rotor tiltable configuration provides a balance between interference-free propeller sizing and hovering efficiency across different attitudes, and its null-space redundancy is crucial for traversing singular configurations under physical constraints. We further show that an upward end-effector placement yields a favorable trade-off between geometric clearance and available wrench. To address disturbances, we propose a dual strategy consisting of a modified integral term for model error and an acceleration-based estimator for external wrenches. Building on these insights, we develop an effector-centric nonlinear model predictive control (NMPC) framework that integrates design choices, singularity handling, and disturbance compensation into a unified formulation. The proposed framework runs fully onboard at 100 Hz on a custom-built tiltable-quadrotor. Real-world experiments, including a 90-deg step cartwheel rotation, whiteboard pushing, and continuous 360-deg valve turning, demonstrate the feasibility of wrench-based omnidirectional manipulation with singularity traversal on a one-DoF-per-arm tiltable-quadrotor.

</details>

---

### [[20_Research/Papers/具身智能/CompCPZ_Preserving_Multi-Modal_Intent_in_Language-Guided_Robot_Manipulation|CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation]]

![[assets/2608.17717_figure.png|800]]

- **arXiv**: [2608.17717](https://arxiv.org/abs/2608.17717)
- **PDF**: https://arxiv.org/pdf/2608.17717
- **详细分析**: [[20_Research/Papers/具身智能/CompCPZ_Preserving_Multi-Modal_Intent_in_Language-Guided_Robot_Manipulation|CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation]]
- **作者**: Zhen Zhang, Ahmad Hafez, Peng Xie, Yanliang Huang, Wenyuan Wu, Amr Alanwar
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《CompCPZ: Preserving Multi-Modal Intent in Language-Guided Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot asked to "place the cup near the red plate or the blue plate" may reach the centroid between them and appear geometrically successful, while satisfying neither disjunct of the instruction. This silent semantic failure exposes a structural limitation of language-conditioned robot policies: representations that collapse a disjunctive instruction into a single connected set cannot preserve all feasible modes, and planners that commit to one action degrade under run-time mode uncertainty. We address this limitation with CompCPZ, a sound algebraic layer that language-conditioned learning systems wrap to recover multi-modal disjunctive representation, recursively composing per-primitive constrained polynomial zonotope enclosures along the language parse tree with distribution-free conformal coverage and sub-millisecond runtime. On a closed-loop ManiSkill3 tabletop-manipulation benchmark, CompCPZ outperforms convex set baselines, multi-peak decoders, and a zero-shot vision-language-action model (1,900/1,918 paired wins, p &lt;&lt; 10^(-30)); the same compiler also transfers without retuning to planar real-robot trials on a Unitree Go2 quadruped under motion capture. These results suggest that compositional language grounding should be evaluated not only by reaching a decoded target, but by whether the represented feasibility set preserves the connected-component structure of the user's intent.

</details>

---

### [[20_Research/Papers/机器人/Force-Based_Offset_Estimation_for_Keyed_Peg-in-Hole_Assembly_Using_Local_Gaussian_Process_Regression|Force-Based Offset Estimation for Keyed Peg-in-Hole Assembly Using Local Gaussian Process Regression]]

![[assets/2608.17691_figure.png|800]]

- **arXiv**: [2608.17691](https://arxiv.org/abs/2608.17691)
- **PDF**: https://arxiv.org/pdf/2608.17691
- **详细分析**: [[20_Research/Papers/机器人/Force-Based_Offset_Estimation_for_Keyed_Peg-in-Hole_Assembly_Using_Local_Gaussian_Process_Regression|Force-Based Offset Estimation for Keyed Peg-in-Hole Assembly Using Local Gaussian Process Regression]]
- **作者**: Chandra Yuvesh Aubeeluck, Abilash Philip Madavath, Augustin Raju, Nicolas Pyschny, Felix Hackelöer, Florian Zwanzig
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Force-Based Offset Estimation for Keyed Peg-in-Hole Assembly Using Local Gaussian Process Regression》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Key-keyway assembly tasks impose strict geometric constraints and are highly sensitive to grasp pose deviations in uncertain environments. This work presents a force-based offset estimation method for keyed peg-in-hole assembly, embedded within a perception-validation-insertion pipeline. Residual misalignment is estimated directly from wrist force/torque measurements using a local KNN-Gaussian Process hybrid regressor. The framework distinguishes between two contact regimes, hard collision and guided chamfer insertion, and routes inference to a dedicated model for each. Regime classification is achieved via a contact-window duration threshold. KNN combined with a deterministic search using the results of a post-grasp monocular visual validation contributes to an increased accuracy of the regressor model. This approach achieves accurate radial offset estimation in chamfered peg insertion, during a keypoint detection-based pick and place application. Experiments using the integrated force/torque sensor of a collaborative robot arm showed an increase in insertion success rate from 67% to 87% after the pipeline was applied.

</details>

---

### [[20_Research/Papers/机器人/Collective_Ranking_of_Environmental_Signals_through_Gaussian_Belief_Propagation_in_a_Patrolling_Robot_Swarm|Collective Ranking of Environmental Signals through Gaussian Belief Propagation in a Patrolling Robot Swarm]]

![[assets/2608.17690_figure.png|800]]

- **arXiv**: [2608.17690](https://arxiv.org/abs/2608.17690)
- **PDF**: https://arxiv.org/pdf/2608.17690
- **详细分析**: [[20_Research/Papers/机器人/Collective_Ranking_of_Environmental_Signals_through_Gaussian_Belief_Propagation_in_a_Patrolling_Robot_Swarm|Collective Ranking of Environmental Signals through Gaussian Belief Propagation in a Patrolling Robot Swarm]]
- **作者**: Zachary R. Madin, Connor York, Jonathan Lawry, Edmund R. Hunt
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, Security

#### 研究背景与动机

《Collective Ranking of Environmental Signals through Gaussian Belief Propagation in a Patrolling Robot Swarm》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot patrolling requires a team to visit all areas of an environment at regular intervals, typically minimising idleness. A practical extension, motivated by security and environmental monitoring, is to additionally form a collective ranking of all patrol locations by some measured signal, a generalisation of the best-of-n problem to the many-option, continuous-valued regime. We observe that the patrol graph admits a natural dual interpretation: it is simultaneously the topology that dictates agent movement and a factor graph over which spatial beliefs can be propagated. Exploiting this equivalence, we apply Gaussian Belief Propagation (GBP), a graph-based algorithm, to collective ranking using unary measurement factors at visited nodes and pairwise smoothness factors along patrol edges. We compare GBP against simple and visit-count-weighted averaging across a range of sensor-noise conditions in simulation, and validate the approach on four Leo Rovers tracking a propagating radio signal in an office lobby. GBP outperforms both baselines on ranking accuracy, mean squared error, and time to consensus. We find that as noise increases and the task becomes harder, GBP degrades gracefully in simulation while both averaging methods degrade substantially. Hardware trials reproduce the same performance ordering on a real propagating radio signal, supporting the practical relevance of the simulated results.

</details>

---

### [[20_Research/Papers/具身智能/OVIP-SG_Open-Vocabulary_Instance-Preserving_Scene_Graphs_for_Mapping_and_Retrieval_of_Small,_Fine-Grained_Objects|OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects]]

![[assets/2608.17633_figure.png|800]]

- **arXiv**: [2608.17633](https://arxiv.org/abs/2608.17633)
- **PDF**: https://arxiv.org/pdf/2608.17633
- **详细分析**: [[20_Research/Papers/具身智能/OVIP-SG_Open-Vocabulary_Instance-Preserving_Scene_Graphs_for_Mapping_and_Retrieval_of_Small,_Fine-Grained_Objects|OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects]]
- **作者**: Tianjing Hao, Haiyu Lan, Angsong Li, Cheng Chen, Enyu Li, Jiarui Yang, Yuning Su, Peiwen Lin, Wang Chuang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《OVIP-SG: Open-Vocabulary Instance-Preserving Scene Graphs for Mapping and Retrieval of Small, Fine-Grained Objects》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Integrating open-vocabulary perception into object-level 3D scene graphs is a double-edged sword. While vision-language detectors recover long-tail categories and small, fine-grained objects overlooked by closed-set models, they also tend to fragment large surfaces and merge small objects into larger neighboring objects, compromising instance-level consistency and undermining mapping fidelity. Moreover, existing methods struggle to retrieve previously unmapped targets or determine whether a queried object is absent, hindering robust embodied open-world navigation and exploration. We present OVIP-SG, a unified framework for instance-preserving semantic mapping, functional scene partitioning, and language-guided small, fine-grained object retrieval. OVIP-SG uses a vision-language model (VLM) to enumerate scene-specific categories for robust open-world detection. Symmetric 3D Intersection over Union (IoU) association and area-weighted feature fusion preserve small independent instances, while VLM-inferred object functions partition scenes into compact functional search regions. A four-stage cascaded retrieval pipeline further incorporates voxel voting and determines target absence from exploration coverage. Under a unified evaluation protocol on Replica, OVIP-SG outperforms ConceptGraphs by 6.31 points in class-mean accuracy (mAcc) and 5.15 points in frequency-weighted mIoU (F-mIoU) while achieving a class-agnostic native-instance Panoptic Quality (PQ) of 0.398. It reduces the search area to 21.8% of the indoor floor space and reaches 0.773 balanced accuracy for object-presence classification. Real-world robotic experiments further demonstrate its practical effectiveness.

</details>

---

### [[20_Research/Papers/具身智能/LIBERO-VIFO_Benchmarking_the_Capability_and_Safety_of_Visual_Cue_Following_in_Vision-Language-Action_Models|LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models]]

![[assets/2608.17600_figure.png|800]]

- **arXiv**: [2608.17600](https://arxiv.org/abs/2608.17600)
- **PDF**: https://arxiv.org/pdf/2608.17600
- **详细分析**: [[20_Research/Papers/具身智能/LIBERO-VIFO_Benchmarking_the_Capability_and_Safety_of_Visual_Cue_Following_in_Vision-Language-Action_Models|LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models]]
- **作者**: Zhengyan Qian, Rui Yan, Alex Jinpeng Wang, Jinhui Tang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《LIBERO-VIFO: Benchmarking the Capability and Safety of Visual Cue Following in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：InstructVLA, InternVLA, OpenVLA, Real-World, TraceVLA, VP-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual cues are increasingly adopted to guide robot learning, but whether Vision-Language-Action (VLA) models can reliably follow authorized cues while disregarding unauthorized ones remains unclear. Existing work covers only a narrow range of cue forms and focuses on final task success, providing only a coarse assessment of cue-following capability. Treating all visual cues as authorized also leaves safety risks of unauthorized following unexplored. To address these gaps, we introduce LIBERO-VIFO, a benchmark to evaluate both the capability and safety of visual cue following in VLA models. LIBERO-VIFO defines eight visual cue families spanning diverse forms. A total of four protocols in two parts are defined: Part I tests cue understanding and authorized following, while Part II evaluates unauthorized visual cue following under language-cue conflict and empty language conditions. Evaluating seven VLA models reveals that although visual cue understanding does not reliably translate into execution, current VLAs are able to execute cue-indicated tasks without language instruction, exposing an emerging risk of unauthorized visual cue following. Extended experiments on scene-instantiated cues, safety-critical settings, and real-robot deployment corroborate these findings. LIBERO-VIFO brings both the capability and safety of visual cue following into systematic evaluation, establishing visual-centric safety as a new perspective for the VLA community.

</details>

---

### [[20_Research/Papers/具身智能/HODAgent_Towards_On-Demand,_Responsive_Humanoids_for_Physical_World_Human_Interaction|HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction]]

![[assets/2608.17584_figure.png|800]]

- **arXiv**: [2608.17584](https://arxiv.org/abs/2608.17584)
- **PDF**: https://arxiv.org/pdf/2608.17584
- **详细分析**: [[20_Research/Papers/具身智能/HODAgent_Towards_On-Demand,_Responsive_Humanoids_for_Physical_World_Human_Interaction|HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction]]
- **作者**: Wang Warren Chen, Jiahao Zhang, Zhenjiang Li, Mingxu Wang, Lei Yi, Yuchen Kang, Shuo Sun, Ziping Chen, Jie Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.9，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《HODAgent: Towards On-Demand, Responsive Humanoids for Physical World Human Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EgoBench, EmbodiedBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose HODAgent, a System-2 embodied agent for humanoid robots in service settings, addressing situated intent, responsive execution, task revision, and outcome verification. Its semi-duplex architecture integrates an Env-Interactor, Planner, Executor, and hierarchical Memory to maintain coherent interaction, planning, and task state during service episodes. This allows handling new requests during motion, retaining progress, revising actions, and grounding closure in execution outcomes. A shared interface connects simulation and physical robots (Unitree G1), isolating platform-specific control. In an interactive simulation with 164 cases, HODAgent achieves 84.8% and 91.5% Joint Success under two VLM backbones, outperforming baselines by 9.8 and 18.9 points. On physical robots, pass rates are 92% (atomic), 72% (composite), and 63.3% (complete tasks). On multiple embodied benchmarks, it improves over baselines by 0.7-9.0 points. Results show a unified System-2 agent enables adaptive humanoid service across simulation and reality.

</details>

---

### [[20_Research/Papers/机器人/Scalix_Uncertainty-Aware_Scale-Consistent_Monocular_SLAM|Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM]]

![[assets/2608.17553_figure.png|800]]

- **arXiv**: [2608.17553](https://arxiv.org/abs/2608.17553)
- **PDF**: https://arxiv.org/pdf/2608.17553
- **详细分析**: [[20_Research/Papers/机器人/Scalix_Uncertainty-Aware_Scale-Consistent_Monocular_SLAM|Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM]]
- **作者**: Sebastian Barbas Laina, Tianyi Zhang, Panagiotis Petropoulakis, Simon Schaefer, Simon Boche, Jaehyung Jung, Cedric Le Gentil, Stefan Leutenegger
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Scalix: Uncertainty-Aware Scale-Consistent Monocular SLAM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cameras are ubiquitous sensors in robotics due to their compact form factor and the perceptual richness captured through visual information. Monocular SLAM enables robots to understand the environment with a minimum setup, however, it inherently suffers from scale ambiguity. A common solution is to provide multi-modal sensor configurations, such as visual-inertial systems, where scale is observable unless the robot navigates under a constant-velocity motion, a common scenario in mobile robotics. With the advent of deep-learning, geometric foundation models have been used to address this problem, but the depths maps are often noisy and scale-inconsistent across frames. In this paper, we propose Scalix, a real-time monocular SLAM framework that achieves metric-scale state estimation by integrating learned depth cues into a probabilistic factor-graph formulation. By augmenting existing monocular depth models with both per-pixel depth uncertainty and per-frame scale uncertainty, Scalix treats scale predictions as independent measurements within its optimization, leading to improved scale consistency through multi-view data associations. Experiments in large-scale outdoor and indoor environments demonstrate state-of-the-art performance on both metric and up-to-scale benchmarks while maintaining real-time operation and generalization.

</details>

---

### [[20_Research/Papers/具身智能/Embodied-Navigator_Point,_Think,_Memorize,_and_Align_for_Efficient_Navigation|Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation]]

![[assets/2608.17512_figure.png|800]]

- **arXiv**: [2608.17512](https://arxiv.org/abs/2608.17512)
- **PDF**: https://arxiv.org/pdf/2608.17512
- **详细分析**: [[20_Research/Papers/具身智能/Embodied-Navigator_Point,_Think,_Memorize,_and_Align_for_Efficient_Navigation|Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation]]
- **作者**: Hongyan Feng, Sunlai Chen, Xuanyu Liu, Miao Pan, Yangfan Xie, Yuxiang Cui, Zhongxiang Zhou, Rong Xiong, Wenqi Zhang, Jianwei Yin, Yueting Zhuang, Xuhong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Embodied-Navigator: Point, Think, Memorize, and Align for Efficient Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although Large Vision-Language Models (VLMs) have significantly advanced embodied navigation, their direct deployment remains challenging, as existing methods often force VLMs into unnatural action spaces that misalign with their 2D pre-training priors, compounded by rigid reasoning schedules and inefficient memory management. To overcome these limitations, we propose TAMP-Nav, a unified framework for efficient embodied navigation. First, we introduce a Pixel-to-3D Action Formulation (Point) that reformulates navigation into 2D visual prompting. Specifically, the VLM merely selects 2D pixels, which are then projected into 3D coordinates for a low-level SLAM controller. This design naturally aligns embodied execution with the VLM's inherent 2D visual capabilities. Second, we propose an integrated Selective Reasoning and Anchor-Trajectory Memory mechanism (Think and Memorize), which dynamically triggers Chain-of-Thought and retains high-fidelity memory only at critical nodes, compressing redundant trajectories into lightweight Space-Time Indicators, thereby preserving critical historical information and enhancing spatio-temporal perception. Finally, we design an efficient Two-Level Alignment Paradigm (Align) via Group Relative Policy Optimization (GRPO). By superimposing global outcome rewards with fine-grained process rewards, this dense supervision tightly aligns the agent's cognitive planning with physical environmental feedback, endowing the model with adaptive reasoning capabilities. Experiments demonstrate that TAMP-Nav achieves state-of-the-art performance (e.g., 66.2% SR on R2R-CE) with high runtime and sample efficiency (requiring only 90k training trajectories).

</details>

---

### [[20_Research/Papers/具身智能/Calibrated_Predictive_Safety_for_Heterogeneous_Robots_An_Action-Conditioned_JEPA_Framework_with_Model-Based_Safety_Shields|Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields]]

![[assets/2608.17496_first_page.png|800]]

- **arXiv**: [2608.17496](https://arxiv.org/abs/2608.17496)
- **PDF**: https://arxiv.org/pdf/2608.17496
- **详细分析**: [[20_Research/Papers/具身智能/Calibrated_Predictive_Safety_for_Heterogeneous_Robots_An_Action-Conditioned_JEPA_Framework_with_Model-Based_Safety_Shields|Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields]]
- **作者**: Kaiming Zhong, Tianhua Liu, Yue Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.3（加权：具身智能 0.6，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《Calibrated Predictive Safety for Heterogeneous Robots: An Action-Conditioned JEPA Framework with Model-Based Safety Shields》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action policies generalize broadly but provide no execution-time guarantees; classical model-based planners respect kinematic and geometric constraints but generalize poorly. We study whether an action-conditioned Joint-Embedding Predictive Architecture (JEPA) world model can predict, before execution, both task progress and physical risk for candidate action chunks, and whether coupling these predictions to an embodiment-specific model-based safety shield yields a deployable pipeline for heterogeneous robots. We propose a receding-horizon decision pipeline: (1) a proposer produces K candidate action chunks; (2) an action-conditioned JEPA rolls each candidate forward in a frozen-encoder latent space conditioned on an embodiment embedding; (3) calibrated risk and progress heads score each rollout and report uncertainty; (4) a deterministic per-embodiment safety shield filters inadmissible candidates; (5) a fallback ladder handles empty-admissible-set cases. The learned ranking only reorders admissible candidates; enforcement guarantees come from the deterministic shield and fallback ladder. We evaluate with a pre-registered protocol in simulation (LIBERO-Long). In 600-episode configurations the full framework improved success over a shield-only baseline and reduced collision false negatives at matched recall. Deployment-efficiency measurements on target on-robot and edge accelerators are included. Real-robot experiments and an offline reranking significance test remain future work; see the paper for disclosures.

</details>

---

### [[20_Research/Papers/具身智能/Reuse_Before_You_Retrieve_Diagnosing_Headroom_and_Complementarity_for_Test-Time_Augmentation_of_Embodied_Multimodal_Policies|Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies]]

![[assets/2608.17484_first_page.png|800]]

- **arXiv**: [2608.17484](https://arxiv.org/abs/2608.17484)
- **PDF**: https://arxiv.org/pdf/2608.17484
- **详细分析**: [[20_Research/Papers/具身智能/Reuse_Before_You_Retrieve_Diagnosing_Headroom_and_Complementarity_for_Test-Time_Augmentation_of_Embodied_Multimodal_Policies|Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies]]
- **作者**: Yuhwan Jeong, Kuk-Jin Yoon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Reuse Before You Retrieve: Diagnosing Headroom and Complementarity for Test-Time Augmentation of Embodied Multimodal Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frozen vision-language-action (VLA) policies are increasingly improved at test time by sampling additional policy behaviors or introducing external demonstrations. Yet there is little guidance for deciding which intervention a deployed policy actually needs. Additional sampling is useful only when better behavior already exists within the policy's stochastic rollouts and can be identified, whereas retrieval is most useful when the relevant action prior is not reliably represented by the policy. We study this decision through two measurable factors, recoverable headroom and retrieval complementarity, which characterize how much useful behavior is already available to recover and whether an external action prior fills a measurable gap. We evaluate an episode-level retry selector under retryable or parallel execution, together with retrieval across multiple frozen VLA policies and environments. The selector consistently recovers substantial latent capability across all tested VLA backbones on LIBERO, with gains of up to 21.0 success-rate points that closely track recoverable headroom. It also transfers to a different robot and simulator and remains effective under degraded observations, while experiments with autoregressive OpenVLA illustrate the distinction between available headroom and the ability to rank candidate rollouts. Retrieval behaves differently, improving the policy with the largest measured action-prior gap and providing further gains when combined with selection. Together, these results provide an empirical basis for characterizing test-time augmentation opportunities by separating capability that can be recovered from the frozen policy from behavioral priors that may need to be introduced externally.

</details>

---

### [[20_Research/Papers/具身智能/Optimal_control_of_a_swimming_robot_based_on_Purcell's_microswimmer_model|Optimal control of a swimming robot based on Purcell's microswimmer model]]

![[assets/2608.17455_figure.png|800]]

- **arXiv**: [2608.17455](https://arxiv.org/abs/2608.17455)
- **PDF**: https://arxiv.org/pdf/2608.17455
- **详细分析**: [[20_Research/Papers/具身智能/Optimal_control_of_a_swimming_robot_based_on_Purcell's_microswimmer_model|Optimal control of a swimming robot based on Purcell's microswimmer model]]
- **作者**: Noam Berkovich Lahav, Oren Wiezel, Yizhar Or
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Optimal control of a swimming robot based on Purcell's microswimmer model》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Purcell's swimmer is a well-known planar model of a swimming microorganism, governed by low Reynolds number hydrodynamics, which is comprised of three rigid links connected by actuated rotary joints. This model has been analyzed as a robotic locomotion system governed by first-order nonlinear dynamics with a periodic input (gait) of the two joint angles. In this work, we present a robotic macro-scale realization of this three-link swimmer moving in a highly viscous fluid. We propose a simple variant of Purcell's theoretical model with non-slender links and a central rigid sphere which represents the added drag of the robot's central flotation block, and calibrate the model's parameters to fit experimental measurements. Next, we apply optimal control formulation based on Pontryagin's Maximum Principle (PMP) in order to find optimal gaits that maximize the displacement per cycle under bounds on the joint angles. Employing a differential geometric method that transforms the problem to area integral enclosed by the gait trajectory in the plane of joint angles, enables visual interpretation which explains topological changes in displacement-optimal gaits upon varying the bound on the joint angles. We then apply PMP formulation to the problem of maximizing Lighthill's energy efficiency in order to obtain a boundary value problem (BVP) whose solution gives efficiency-optimal gaits for Purcell's swimmer model, as well as its variant with a central sphere. Finally, we utilize numerical methods such as parameterizing the input gait as a truncated Fourier series, as well as GPOPS-II solver, to produce sufficient initial guess values for solving the BVPs and obtaining efficiency-optimal gaits.

</details>

---

### [[20_Research/Papers/具身智能/EATR-Stereo_Embodiment-Aware_Routing_of_Paired_Stereo_Evidence_for_Humanoid_Vision-Language-Action_Control|EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control]]

![[assets/2608.17453_figure.png|800]]

- **arXiv**: [2608.17453](https://arxiv.org/abs/2608.17453)
- **PDF**: https://arxiv.org/pdf/2608.17453
- **详细分析**: [[20_Research/Papers/具身智能/EATR-Stereo_Embodiment-Aware_Routing_of_Paired_Stereo_Evidence_for_Humanoid_Vision-Language-Action_Control|EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control]]
- **作者**: Songwei Wu, Rui Zhao, Fan Yang, Zhongqiang Nie, Zhiduo Jiang, Wandong Sun, Yuwei Li, Yang Liu, Hong Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.1（加权：具身智能 2.7，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《EATR-Stereo: Embodiment-Aware Routing of Paired Stereo Evidence for Humanoid Vision-Language-Action Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, OpenVLA, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon humanoid vision--language--action (VLA) control with head-mounted stereo cameras requires visual interfaces that can exploit complementary views while maintaining compatibility with pretrained representations. Existing interfaces often discard complementary stereo evidence or fuse additional observations without preserving the native primary-view pathway and adapting auxiliary information to robot embodiment. We present EATR-Stereo, an embodiment-aware token-routing framework that retains primary-view tokens and constructs primary-aligned Cross-View Auxiliary Tokens (CVATs) by querying the synchronized auxiliary-view token sequence. A body-segmented proprioceptive encoder further conditions token-wise auxiliary usage on robot configuration history, enabling selective incorporation of stereo evidence during action generation. The routed auxiliary stream augments the language and primary-visual context of a pretrained VLA while keeping its vision--language model frozen. On a 33-DoF physical humanoid with a 37-D proprioceptive state, we evaluate nine configurations in over-100-s search--approach--grasp--place--return tasks. EATR-Stereo achieves 60.0% full-task success, 100.0% grasp success, and 80.0% stage success. Under severe asymmetric occlusion, it improves recovery to 80% compared with 30% for CVAT alone. Ablation studies further show the importance of preserving primary tokens and combining cross-view auxiliary features with structured proprioceptive routing. These results demonstrate that selectively routed paired stereo evidence improves spatial grounding for reliable long-horizon humanoid VLA control.

</details>

---

### [[20_Research/Papers/机器人/Bi-Layer_Ant_Colony_Optimization_for_Multi-Robot_Task_Allocation_and_Routing_in_Delivery_Applications|Bi-Layer Ant Colony Optimization for Multi-Robot Task Allocation and Routing in Delivery Applications]]

![[assets/2608.17416_figure.png|800]]

- **arXiv**: [2608.17416](https://arxiv.org/abs/2608.17416)
- **PDF**: https://arxiv.org/pdf/2608.17416
- **详细分析**: [[20_Research/Papers/机器人/Bi-Layer_Ant_Colony_Optimization_for_Multi-Robot_Task_Allocation_and_Routing_in_Delivery_Applications|Bi-Layer Ant Colony Optimization for Multi-Robot Task Allocation and Routing in Delivery Applications]]
- **作者**: Le Na Nguyen, Thanh Long Nguyen, Thanh Thao Ton Nu, Quan Le, Manh Duong Phung
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Bi-Layer Ant Colony Optimization for Multi-Robot Task Allocation and Routing in Delivery Applications》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper addresses the multi-robot task allocation (MRTA) problem, which is essential for delivery and logistics applications. Our approach first defines a new cost function that transforms the MRTA into a unified optimization problem capturing both task assignment and routing. A bi-layer ant colony optimization (ACO) algorithm is then introduced, integrating two interdependent decision layers within a single colony process to solve the problem. This hierarchical framework enables simultaneous optimization of task allocation and route planning across multiple robots. Comparative experiments with mixed-integer linear programming (MILP) and particle swarm optimization (PSO) demonstrate that the proposed bi-layer ACO achieves the shortest total travel distance and fastest completion time across all task sizes. Specifically, it reduces total travel distance by up to 17.7% and completion time by nearly 20% compared with baseline methods. These results confirm the efficiency, scalability, and reliability of the proposed bi-layer ACO for multi-robot delivery tasks.

</details>

---

### [[20_Research/Papers/具身智能/MANIGUARD_A_Benchmark_and_Data_Suite_for_Specification-Grounded_Safety_Evaluation_and_Improvement_of_Robotic_Manipulation|MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation]]

![[assets/2608.17386_figure.png|800]]

- **arXiv**: [2608.17386](https://arxiv.org/abs/2608.17386)
- **PDF**: https://arxiv.org/pdf/2608.17386
- **详细分析**: [[20_Research/Papers/具身智能/MANIGUARD_A_Benchmark_and_Data_Suite_for_Specification-Grounded_Safety_Evaluation_and_Improvement_of_Robotic_Manipulation|MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation]]
- **作者**: Yiyan Peng, Philip Wang, Simon Sinong Zhan, Yiqi Lyu, Zhenyang Ni, Jixin Yan, Fiorelli Wong, Ruochen Jiao, Hang Yin, Xinyu Cao, Huajie Shao, Manling Li...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《MANIGUARD: A Benchmark and Data Suite for Specification-Grounded Safety Evaluation and Improvement of Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EARBench, ISBench, ManiGuard-Bench, RedVLA, SafeLIBERO。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation-model policies for robotic manipulation are advancing rapidly on task success, but rigorous evaluation of whether they succeed safely is still lacking. We introduce ManiGuard, a specification-grounded framework for evaluating and improving the safety of foundation-model manipulation, comprising the ManiGuard-Bench task suite and a paired safety-annotated trajectory-generation pipeline. ManiGuard-Bench organizes six contact-rich household task families into 200 locked base tasks along a skill $\times$ constraint taxonomy, with safety specified independently of task success. Each task is evaluated under one in-distribution and four single-axis out-of-distribution perturbations that hold the safety specification fixed, giving 1,000 locked scenarios. Every rollout is runtime-checked by LTL$_f$-grounded automaton monitors over physics-grounded predicates rather than learned classifiers or LLM judges, in simulation and on a physical Franka platform. The pipeline pairs an automated motion-planning generator with human teleoperation, annotated by the same per-step monitor, and directly supports safety-aware fine-tuning; we release 8,000 safety-annotated demonstrations, 40 per base task. Benchmarking zero-shot and fine-tuned VLAs across more than 23,000 rollouts, we find: (i) safety must be evaluated independently of task success, as 6-21% of successful rollouts violate the specification; (ii) fine-tuning on our suite raises safe task completion from near zero to 7.5-29.8% and engaged-and-safe behavior from 16-40% to 51-72%; but (iii) a gap remains that scaling demonstrations does not close, with 21-42% of engaged rollouts still violating, two of six families below 2% safe success for every policy, and these failures persisting under distribution shift and on hardware.

</details>

---

### [[20_Research/Papers/具身智能/Robust_Brachiation_on_a_Life-Sized_Dual-Arm_Robot_Using_Waypoint-Guided_Reinforcement_Learning|Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning]]

![[assets/2608.17320_figure.png|800]]

- **arXiv**: [2608.17320](https://arxiv.org/abs/2608.17320)
- **PDF**: https://arxiv.org/pdf/2608.17320
- **详细分析**: [[20_Research/Papers/具身智能/Robust_Brachiation_on_a_Life-Sized_Dual-Arm_Robot_Using_Waypoint-Guided_Reinforcement_Learning|Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning]]
- **作者**: Ayumu Iwata, Kento Kawaharazuka, Keita Yoneda, Takahiro Hattori, Kei Okada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.2，强化学习 0.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Robust Brachiation on a Life-Sized Dual-Arm Robot Using Waypoint-Guided Reinforcement Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Sim-to-Sim, WGRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Brachiation is a form of locomotion in which primates move primarily using their arms, enabling traversal in environments without footholds. However, this motion requires highly coordinated whole-body movement and precise timing control for bar grasping and release. As a result, achieving robust behavior on life-sized robotic platforms remains challenging. In this study, we present a reinforcement learning-based method to realize brachiation on a life-sized dual-arm robot. The core of the proposed approach is Waypoint-Guided Reinforcement Learning (WGRL), a learning framework for inducing non-linear and complex motions. For high-difficulty tasks where imitation learning data are unavailable, WGRL guides behavior acquisition by sparsely specifying waypoints for the end-effector trajectory, while whole-body motion is generated through reinforcement learning. In addition, by integrating the waypoint-following guidance with rewards based on task success and mechanical energy, and training in an environment designed for Sim-to-Real transfer, the proposed method achieves both forward progression and motion stability. The acquired behavior is evaluated through Sim-to-Sim experiments under monkey-bar environments with geometric variations and hardware experiments, confirming robust brachiation including failure recovery behavior. This study provides effective learning design guidelines for realizing arm-based locomotion on life-sized robotic hardware and expanding the traversable workspace of robots.

</details>

---

### [[20_Research/Papers/具身智能/PDDL-ART_Autonomous_Symbolic_Abstraction_From_Demonstration_For_Long-Horizon_Robotic_Manipulation_Using_Vision-Language_Models|PDDL-ART: Autonomous Symbolic Abstraction From Demonstration For Long-Horizon Robotic Manipulation Using Vision-Language Models]]

![[assets/2608.17146_figure.png|800]]

- **arXiv**: [2608.17146](https://arxiv.org/abs/2608.17146)
- **PDF**: https://arxiv.org/pdf/2608.17146
- **详细分析**: [[20_Research/Papers/具身智能/PDDL-ART_Autonomous_Symbolic_Abstraction_From_Demonstration_For_Long-Horizon_Robotic_Manipulation_Using_Vision-Language_Models|PDDL-ART: Autonomous Symbolic Abstraction From Demonstration For Long-Horizon Robotic Manipulation Using Vision-Language Models]]
- **作者**: Disha Kamale, Dmitry Berenson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PDDL-ART: Autonomous Symbolic Abstraction From Demonstration For Long-Horizon Robotic Manipulation Using Vision-Language Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Symbolic planning with PDDL offers a principled framework for long-horizon robot manipulation, but constructing accurate PDDL domain and problem descriptions remains a significant bottleneck, typically requiring substantial domain expertise. We present a Vision-Language Model (VLM)-based approach called PDDL-ART, a framework that autonomously generates task-specific PDDL domain and problem descriptions from a single expert demonstration, a natural language task description, and a library of available high-level action names. PDDL-ART does not require any domain templates, action signatures, or fine-tuning. To ensure the generated descriptions are not only syntactically valid but semantically aligned with the demonstrated task, PDDL-ART introduces a multi-stage correction pipeline operating at syntactic, semantic, and execution levels. A key component of execution-guided correction is symbolic predicate grounding. Instead of relying solely on visual observations, PDDL-ART leverages the tool-use capabilities of modern VLMs to incorporate geometric and temporal reasoning for evaluating relational predicates that are not directly discernible from images alone. Critically, the model autonomously determines when to invoke these tools and how to interpret their outputs. We evaluate PDDL-ART on challenging manipulation tasks in engine maintenance and household domains, including tasks that require memory, abstract predicate inference, and goal states that are visually indistinguishable from the initial state. PDDL-ART achieves an average success rate of 93.3%, compared to 78.3% for a baseline VLM-based planner.

</details>

---

### [[20_Research/Papers/具身智能/Terrain-Aware_Local_Path_Planning_with_Global_DEM_Data_Integration_for_Autonomous_UGV_Navigation|Terrain-Aware Local Path Planning with Global DEM Data Integration for Autonomous UGV Navigation]]

![[assets/2608.17038_figure.png|800]]

- **arXiv**: [2608.17038](https://arxiv.org/abs/2608.17038)
- **PDF**: https://arxiv.org/pdf/2608.17038
- **详细分析**: [[20_Research/Papers/具身智能/Terrain-Aware_Local_Path_Planning_with_Global_DEM_Data_Integration_for_Autonomous_UGV_Navigation|Terrain-Aware Local Path Planning with Global DEM Data Integration for Autonomous UGV Navigation]]
- **作者**: Devender Singh, Issah Nazif Suleiman, Paul Mitten, Glenn Cutler, Vinicius Prado da Fonseca, Matthew Hamilton
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Terrain-Aware Local Path Planning with Global DEM Data Integration for Autonomous UGV Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous navigation in complex outdoor terrains presents critical challenges for unmanned ground vehicles (UGVs) due to the inherent disconnect between global mapping and real-time sensor feedback. This work proposes a hybrid framework that integrates low-resolution Digital Elevation Model (DEM) data with real-time LiDAR-based obstacle detection and terrain analysis for efficient path planning. A global path is initially computed using a preprocessed DEM-based A* algorithm. Subsequently, local sensor data drives adaptive path correction, enabling the UGV to negotiate sudden environmental changes while maintaining safety and efficiency. Simulation results in Gazebo demonstrate significant improvements over a baseline approach, achieving a 95\% obstacle avoidance rate and reducing the average encountered slope from $8^\circ$ to $2.7^\circ$ in custom terrain. This integration enhances path efficiency and terrain traversability and supports robust real-time adaptation, paving the way for more reliable autonomous navigation in dynamic outdoor environments.

</details>

---

### [[20_Research/Papers/具身智能/FetchMan_Learning_Visual_Humanoid_Loco-Manipulation_Policies_from_Simulated_Experiences|FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences]]

![[assets/2608.17027_figure.jpg|800]]

- **arXiv**: [2608.17027](https://arxiv.org/abs/2608.17027)
- **PDF**: https://arxiv.org/pdf/2608.17027
- **详细分析**: [[20_Research/Papers/具身智能/FetchMan_Learning_Visual_Humanoid_Loco-Manipulation_Policies_from_Simulated_Experiences|FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences]]
- **作者**: Omar Rayyan, Zhi Li, Max Argus, Yuxin Jiang, Chang Yu, Chenfanfu Jiang, Yuchen Cui
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《FetchMan: Learning Visual Humanoid Loco-Manipulation Policies from Simulated Experiences》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FetchMan-Bench, GraspVLA, Humanoid-VLA, InternVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual loco-manipulation policies that can generalize to novel scenes and objects have long been a goal of robotics research. However, today's data-hungry algorithms make collecting sufficient demonstrations a struggle for tabletop manipulation, and even more so for humanoids that must also walk and balance. Learning from simulated data and transferring that behavior to the real world, as is commonly done in locomotion, sidesteps this struggle, so we replicate that recipe for loco-manipulation. In doing so, we find that cloning synthetic demonstrations results in a low performance ceiling no matter the amount of training data. Reinforcement learning breaks through it, and refining the cloned policy with Flow-GRPO on a single sparse reward yields performance that synthetic behavior cloning cannot match. Together, these stages form our end-to-end sim-to-real pipeline spanning more than 150,000 scenes, which we use to train FetchMan. We evaluate it on FetchMan-Bench, a simulation benchmark we release, and deploy it zero-shot on a real Unitree G1, where our single-object reach-and-pick policy walks to and grasps a target across unseen scenes at 73.3% success. Finally, we extend this recipe to multi-object training, a first step toward loco-manipulation generalist policies at this data scale.

</details>

---
