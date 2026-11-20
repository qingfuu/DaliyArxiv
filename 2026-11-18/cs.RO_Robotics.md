# cs.RO | Robotics | 2026-11-18

#arxiv #ComputerScience

**论文数**: 29

### [[20_Research/Papers/机器人/Pressure_Drop_Gravity_Vector_Estimation_from_a_Distributed_Barometric_Pressure_Sensor_Array|Pressure Drop: Gravity Vector Estimation from a Distributed Barometric Pressure Sensor Array]]

![[assets/2611.23120_figure.png|800]]

- **arXiv**: [2611.23120](https://arxiv.org/abs/2611.23120)
- **PDF**: https://arxiv.org/pdf/2611.23120
- **详细分析**: [[20_Research/Papers/机器人/Pressure_Drop_Gravity_Vector_Estimation_from_a_Distributed_Barometric_Pressure_Sensor_Array|Pressure Drop: Gravity Vector Estimation from a Distributed Barometric Pressure Sensor Array]]
- **作者**: William Dubois, Nicolas Lauzon, Johann Laconte, François Pomerleau
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Pressure Drop: Gravity Vector Estimation from a Distributed Barometric Pressure Sensor Array》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While gravity is often used in mobile robotics as a global constraint for Simultaneous Localization and Mapping (SLAM) algorithms, most estimation methods rely on indirect observation of the gravity vector. In this paper, we propose the use of altimeter measurements to directly observe the direction of the gravity vector. We provide a theoretical evaluation of the estimation noise and validate it through extensive experimental data, along with an evaluation of the impact of intersensor distance on our gravity vector estimates. Experimental results demonstrate that a median error of $0.87^\circ$ on the tilt estimation can be achieved with our system in semi-static scenarios. Furthermore, we demonstrate the potential of this approach by comparing it with state-of-the-art methods based on Inertial Measurement Units (IMUs). We highlight that we achieve similar performance to that of IMU-based systems in highly dynamic scenarios and even outperform in specific cases of accelerometer measurement saturation. Finally, an additional experiment shows the potential use within a robotic system through the integration into an Iterative Closest Point (ICP) algorithm.

</details>

---

### [[20_Research/Papers/具身智能/CADENCE_Learning_Acyclic_Gaits_for_Model-Based_Quadruped_Locomotion|CADENCE: Learning Acyclic Gaits for Model-Based Quadruped Locomotion]]

![[assets/2611.23102_figure.png|800]]

- **arXiv**: [2611.23102](https://arxiv.org/abs/2611.23102)
- **PDF**: https://arxiv.org/pdf/2611.23102
- **详细分析**: [[20_Research/Papers/具身智能/CADENCE_Learning_Acyclic_Gaits_for_Model-Based_Quadruped_Locomotion|CADENCE: Learning Acyclic Gaits for Model-Based Quadruped Locomotion]]
- **作者**: Owen Sullivan, Sourav Selvaraj, Mahdi Agheli
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.7（加权：具身智能 2.4，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CADENCE: Learning Acyclic Gaits for Model-Based Quadruped Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ContactNet, GaitNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based quadruped controllers usually step on a cyclic gait, which lifts the legs in a fixed order on a fixed period, wherever the safe footholds are. We present CADENCE, a learned step planner with a small action space. Every 40 ms, it picks one of at most 65 discrete choices: no step, or one leg's step to a safe foothold. It also predicts a swing time. We train CADENCE by reinforcement learning on top of a convex model predictive controller (MPC). Nothing prescribes a gait: there is no gait schedule, and the reward has no gait term, only a cost per step. The one structural constraint is that at most two legs may swing at once. The policy we analyzed developed an acyclic gait, with no fixed period or stepping order, yet it still paired diagonal legs. An inverse footstep model (IFM), fitted on a controller's logged steps, turns each foothold into a command. With only the IFM refitted, on fewer than 20,000 steps, CADENCE ran frozen on OCS2's nonlinear MPC. In simulated trials on a range of terrains (26% to 49% voids) and speeds (0.1 m/s and 0.2 m/s), it succeeded in 85.1% (mean of five seeds), against 67.8% for OCS2-Trot, 65.5% for OCS2-Single, and 39.6% in a static walk ablation of CADENCE. At 49% voids, it succeeded in 72.9%, against 43.0% for OCS2-Trot.

</details>

---

### [[20_Research/Papers/具身智能/PAIR_Bringing_Household_Robots_into_the_Smart_Home|PAIR: Bringing Household Robots into the Smart Home]]

![[assets/2611.23070_figure.png|800]]

- **arXiv**: [2611.23070](https://arxiv.org/abs/2611.23070)
- **PDF**: https://arxiv.org/pdf/2611.23070
- **详细分析**: [[20_Research/Papers/具身智能/PAIR_Bringing_Household_Robots_into_the_Smart_Home|PAIR: Bringing Household Robots into the Smart Home]]
- **作者**: Junseong Pyo, Hyeongjin Kim, Jongwook Han, Seungwon Kook, Sungjib Lim, Yohan Jo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《PAIR: Bringing Household Robots into the Smart Home》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Household robots often need to operate appliances, and smart appliances offer both control panels and device APIs. Existing embodied AI simulation environments, however, model appliances solely as physical objects. We introduce PAIR, a smart-home simulation environment grounded in the Matter protocol~\footnote{https://csa-iot.org/all-solutions/matter/}, the industry standard for smart-home devices. PAIR provides 84 smart-device assets whose functional control panels and APIs act on a shared device state, with ambient conditions that evolve in response to both. From a survey of 1,443 requests, we construct a benchmark of 40 tasks that all require object manipulation yet remain solvable without API access, with 340 human demonstrations for policy training. Whether run alone, with a high-level planner, or with an API-enabled planner, two fine-tuned VLA policies complete none of the 120 evaluation episodes. Robots rarely get far enough to use the API: even with oracle plans and API access, over 90\% of failed rollouts stall at navigating, grasping, or operating a door. With a perfect oracle in place of the robot's body, the best planner still gets through only 57.3\% of its plan. When choosing between pressing a button and calling an API, several planners go by whether they can read the panel, not by API latency.\footnote{We will release our code and data upon publication.}

</details>

---

### [[20_Research/Papers/具身智能/Physics-Informed_Tactile-based_Shape_Estimation_of_Deformable_Linear_Objects|Physics-Informed Tactile-based Shape Estimation of Deformable Linear Objects]]

![[assets/2611.22990_figure.png|800]]

- **arXiv**: [2611.22990](https://arxiv.org/abs/2611.22990)
- **PDF**: https://arxiv.org/pdf/2611.22990
- **详细分析**: [[20_Research/Papers/具身智能/Physics-Informed_Tactile-based_Shape_Estimation_of_Deformable_Linear_Objects|Physics-Informed Tactile-based Shape Estimation of Deformable Linear Objects]]
- **作者**: Rotem Atari, Stav Ashur, Avishai Sintov
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Physics-Informed Tactile-based Shape Estimation of Deformable Linear Objects》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate shape estimation of Deformable Linear Objects (DLOs) is a fundamental challenge in robotic manipulation, often hindered by visual occlusions and the high-dimensional configuration space of flexible materials. While Force/Torque (F/T) and vision-centric methods have been proposed, they frequently struggle with grasp-site ambiguities and environmental interference. In this letter, we investigate the hypothesis that global shape estimation can be achieved through tactile sensing and proprioception, without any visual perception. We contend that dense, high-resolution tactile imprints capture critical boundary conditions and contact gradients that are sufficient to resolve the high-dimensional configuration of the DLO. To prove this, we introduce a Physics-Informed Vision Transformer (ViT) framework that maps tactile images to a 3D vertex chain. By leveraging self-attention mechanisms and a physics-weighted loss function, our model enforces structural priors to ensure that the predicted geometry adheres to the object's physical manifold. Experimental results demonstrate that our tactile-based approach achieves superior reconstruction accuracy across Euclidean and Chamfer metrics. Furthermore, we demonstrate the efficiency of this modality, achieving model transfer to novel DLO materials and geometries. Our findings suggest that tactile feedback provides a robust and computationally efficient alternative for DLO state estimation in visually degraded or occluded environments.

</details>

---

### [[20_Research/Papers/强化学习/Sim2CBF_From_Forward_Simulations_to_Implicit_Control_Barrier_Function_Safety_Filtering_without_Model_Derivatives|Sim2CBF: From Forward Simulations to Implicit Control Barrier Function Safety Filtering without Model Derivatives]]

![[assets/2611.22954_figure.png|800]]

- **arXiv**: [2611.22954](https://arxiv.org/abs/2611.22954)
- **PDF**: https://arxiv.org/pdf/2611.22954
- **详细分析**: [[20_Research/Papers/强化学习/Sim2CBF_From_Forward_Simulations_to_Implicit_Control_Barrier_Function_Safety_Filtering_without_Model_Derivatives|Sim2CBF: From Forward Simulations to Implicit Control Barrier Function Safety Filtering without Model Derivatives]]
- **作者**: Luzia Knoedler, Yihan Liu, Shaohang Han, Yifei Dong, Jana Tumova
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.0（加权：具身智能 0.3，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Sim2CBF: From Forward Simulations to Implicit Control Barrier Function Safety Filtering without Model Derivatives》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Failure avoidance in complex robot-environment interactions is challenging because the underlying dynamics are difficult to model accurately, and available predictive models may not provide reliable derivatives. We present Sim2CBF, a failure-avoidance framework that solves the Control Barrier Function (CBF)-Safety Filter (SF) optimization problem using only forward-model evaluations, thereby avoiding differentiation of the predictive model. Specifically, we approximate the CBF constraint using finite differences and local linear interpolation over sampled control inputs while preserving failure-avoidance guarantees. The underlying CBF is implicit and constructed from backup-policy rollouts, enabling the use of expressive predictive models such as physics-based simulators and learned world models. Compared with purely sampling-based SFs, our formulation requires fewer control samples and yields less conservative behavior than direct nominal-backup blending. We evaluate Sim2CBF in simulation, hardware box-toppling, and vision-based control tasks, demonstrating its applicability to contact-rich and learned dynamics, as well as its adaptability to changes in the predictive model.

</details>

---

### [[20_Research/Papers/机器人/Arboreus_A_Realistic_Boreal_Forest_Simulator_with_Topographic_Terrain_and_Satellite-Informed_Parametric_Tree_Distributions|Arboreus: A Realistic Boreal Forest Simulator with Topographic Terrain and Satellite-Informed Parametric Tree Distributions]]

![[assets/2611.22908_figure.jpg|800]]

- **arXiv**: [2611.22908](https://arxiv.org/abs/2611.22908)
- **PDF**: https://arxiv.org/pdf/2611.22908
- **详细分析**: [[20_Research/Papers/机器人/Arboreus_A_Realistic_Boreal_Forest_Simulator_with_Topographic_Terrain_and_Satellite-Informed_Parametric_Tree_Distributions|Arboreus: A Realistic Boreal Forest Simulator with Topographic Terrain and Satellite-Informed Parametric Tree Distributions]]
- **作者**: F. Labra Caso, A. Saradagi, A. Koval, G. Nikolakopoulos
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Arboreus: A Realistic Boreal Forest Simulator with Topographic Terrain and Satellite-Informed Parametric Tree Distributions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim, GazeboSim, IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work presents Arboreus, a realistic Boreal forest simulator, developed to support statistical validation of robotic autonomy algorithms in Boreal forest environments. Arboreus presents an automated methodology for synthesizing large-scale, data-informed, plausible forest worlds from parametric trees, height-variant terrain, and satellite-informed tree density distributions. The parametric generation of dominant Boreal tree species such as Birch, Spruce, and Pine is guided by trunk, canopy, and foliage parameters, extracted from growth studies in the Nordic areas. Tree distribution in an area of interest is guided by the Copernicus satellite dataset, which provides tree cover density and dominant species type at up to 10m raster resolution. The forest floor generation is guided by topographic data from the Swedish cadastral agency to produce realistic data-informed terrains. Given coordinates and extents of forested areas of interest, Arboreus synthesizes data-informed plausible forests, while offering flexibility to inject user observations of real forests (detail, age, dimensionality and tree count), which is critical for realistic synthetic data generation and for the testing of feature-sensitive autonomy algorithms. The applicability of Arboreus for benchmarking and validation of robot autonomy for different robot mobilities is demonstrated in Gazebosim, Unreal Engine, and Isaac Sim physics engines. The applicability of Arboreus as a source of synthetic forest data and its potential to support downstream forest resource mapping research (volume estimation, tree instance segmentation and stem attribute estimation) is also demonstrated. Arboreus has been open-sourced along with a dataset comprising 25 Boreal forest worlds of size 1000m2 corresponding to three real forest sites.

</details>

---

### [[20_Research/Papers/具身智能/Fly_as_Instructed_Refining_World-Action_Policies_for_UAV_Vision-Language_Navigation|Fly as Instructed: Refining World-Action Policies for UAV Vision-Language Navigation]]

![[assets/2611.22883_figure.png|800]]

- **arXiv**: [2611.22883](https://arxiv.org/abs/2611.22883)
- **PDF**: https://arxiv.org/pdf/2611.22883
- **详细分析**: [[20_Research/Papers/具身智能/Fly_as_Instructed_Refining_World-Action_Policies_for_UAV_Vision-Language_Navigation|Fly as Instructed: Refining World-Action Policies for UAV Vision-Language Navigation]]
- **作者**: Zhexuan Zhou, Yanke Sun, Yuhan Zong, Youmin Gong, Jie Mei
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Fly as Instructed: Refining World-Action Policies for UAV Vision-Language Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FlowVLA, HUGE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural language-guided UAV navigation enables intuitive human-robot interaction and flexible autonomous flight in complex environments. However, reliable navigation requires accurate instruction following, continuous task progress tracking, and safe obstacle avoidance, which remain challenging for existing world-action models that primarily focus on action prediction. To address these limitations, we propose a world-action learning framework that integrates three complementary mechanisms: a language-conditioned action interface with targeted post-training for instruction-responsive motion, recurrent instruction-consumption prediction to track task progress and determine termination, and Gaussian-scene post-training to enhance obstacle avoidance through trajectory imitation and differentiable geometric feedback. Closed-loop evaluations and ablation studies demonstrate improvements in sequential task completion, safe goal reaching, and timely termination. Furthermore, direct one-step denoising reduces inference overhead, and real-world indoor and outdoor flights validate the framework's effectiveness.

</details>

---

### [[20_Research/Papers/具身智能/Zero-Shot_Compositional_Generalization_for_Embodied_Manipulation|Zero-Shot Compositional Generalization for Embodied Manipulation]]

![[assets/2611.22797_figure.png|800]]

- **arXiv**: [2611.22797](https://arxiv.org/abs/2611.22797)
- **PDF**: https://arxiv.org/pdf/2611.22797
- **详细分析**: [[20_Research/Papers/具身智能/Zero-Shot_Compositional_Generalization_for_Embodied_Manipulation|Zero-Shot Compositional Generalization for Embodied Manipulation]]
- **作者**: Baicheng Li, Wenkang Qin, Youqi Pan, Dongxiao Mao, Yukun Zhou, Chuanfu Shen, Dong Wu, Shunkai Zhou, Zike Yan, Wei Sui, Hongbin Zha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Zero-Shot Compositional Generalization for Embodied Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, UniVLA, X-VLA, XL-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot demonstrations are collected on different embodiments, leaving many robot-skill combinations unobserved. Pooling these data shares visual knowledge, while joint labels remain tied to the demonstrating kinematic chain. We propose a geometry-supervised training framework for zero-shot composition of familiar robots and skills. The central insight is that a demonstrated command provides a tool-space target for every robot that can realize it. Calibrated forward kinematics supplies this supervision to foreign native action interfaces without their joint labels for that skill. Native reconstruction retains demonstrated configurations, and positive reachability checks select targets for cross-robot supervision. A visual policy learns to predict shared actions and executes through the target robot's native decoder. During policy learning, one prediction receives geometric supervision through both source and foreign native realizations. Matched supervision controls, repeated policy training and evaluations across three backbones and two simulators demonstrate improved transfer to missing robot-task combinations.

</details>

---

### [[20_Research/Papers/具身智能/Body_Schema_Policy_Body_as_the_Vision-Action_Interface_for_Efficient_Robot_Loco-Manipulation|Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation]]

![[assets/2611.22713_figure.png|800]]

- **arXiv**: [2611.22713](https://arxiv.org/abs/2611.22713)
- **PDF**: https://arxiv.org/pdf/2611.22713
- **详细分析**: [[20_Research/Papers/具身智能/Body_Schema_Policy_Body_as_the_Vision-Action_Interface_for_Efficient_Robot_Loco-Manipulation|Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation]]
- **作者**: Lechen Zhang, Chenyuan Chen, Muxin Zhou, Zewen He, Yoshihiko Nakamura
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《Body Schema Policy: Body as the Vision-Action Interface for Efficient Robot Loco-Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AVA-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Currently, robots can learn whole-body loco-manipulation through scale: the strongest policies have billions of parameters and still need task-specific fine-tuning. Humans have limited processing capacity, yet learn and act efficiently through a body schema that organizes what they see and how they move. We introduce Body Schema Policy (BSP), an imitation learning policy that builds such a schema into the vision-action interface. Its latent body schema places joint and link tokens on the robot's kinematic tree, where learned screw motions carry features between links. Through body-queried vision, each body part retrieves its own visual evidence, which conditions the denoising of its actions. With this inductive bias, BSP returns an action chunk faster than any policy we compare. Compact, body-specific visual readouts also emerge without spatial supervision: manipulation commands depend strongly on task objects, while locomotion commands respond more broadly to the scene. On nine simulated Unitree G1 whole-body tasks, BSP matches the $Ψ_0$ humanoid foundation model with $75\times$ fewer parameters and nearly doubles Diffusion Policy's success. The same holds on a real G1 and a Fetch mobile manipulator.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Accurate_End-Effector_Trajectory_Tracking_with_Inertial_Feedback_for_a_Quadruped_Manipulator|Learning Accurate End-Effector Trajectory Tracking with Inertial Feedback for a Quadruped Manipulator]]

![[assets/2611.22695_figure.png|800]]

- **arXiv**: [2611.22695](https://arxiv.org/abs/2611.22695)
- **PDF**: https://arxiv.org/pdf/2611.22695
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Accurate_End-Effector_Trajectory_Tracking_with_Inertial_Feedback_for_a_Quadruped_Manipulator|Learning Accurate End-Effector Trajectory Tracking with Inertial Feedback for a Quadruped Manipulator]]
- **作者**: Dohyeon Kim, Seungyong Han, Yeongtae Jung
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Learning Accurate End-Effector Trajectory Tracking with Inertial Feedback for a Quadruped Manipulator》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate end-effector trajectory tracking on quadruped manipulators is challenging because uncertainties in actuators, foot-ground contact, and geometric errors are propagated through the leg-arm kinematic chain. Detecting such errors requires sensing beyond joint encoders that can capture the effects of these uncertainties on the robot's motion, since joint encoders only provide measurements at the actuated joints and cannot fully observe mechanical errors such as backlash, dimensional inaccuracies, or structural deformation. This work addresses these challenges using a reinforcement learning framework with end-effector (EE) inertial feedback, targeting local high-accuracy manipulation while maintaining a nominal body pose and support configuration without intentional body motion or foot repositioning. The learned policy uses EE inertial measurements to compensate for tracking errors induced by uncertainties throughout the leg-arm system that cannot be fully inferred from proprioception alone. Simulation and real-world experiments on continuous EE trajectory tracking show overall improvements relative to nominal and proprioception-only baselines. In real-world experiments, the proposed policy reduces the MoCap-based RMSE by 17.3% and 28.0% relative to the nominal baseline under the two in-distribution (ID) command conditions, respectively, and by an additional 12.6% and 15.9% relative to the proprioception-only baseline. Furthermore, the trajectory-wise RMSE between FK-reconstructed and motion-capture-measured end-effector positions averaged 12.61+-2.15mm (mean+-standard deviation) across 24 controller-trajectory combinations, revealing a substantial discrepancy between nominal kinematic reconstruction and measured end-effector motion.

</details>

---

### [[20_Research/Papers/具身智能/VLM-guided_Grounding_Expert_for_Generalised_Referring_Expression_Comprehension|VLM-guided Grounding Expert for Generalised Referring Expression Comprehension]]

![[assets/2611.22625_figure.png|800]]

- **arXiv**: [2611.22625](https://arxiv.org/abs/2611.22625)
- **PDF**: https://arxiv.org/pdf/2611.22625
- **详细分析**: [[20_Research/Papers/具身智能/VLM-guided_Grounding_Expert_for_Generalised_Referring_Expression_Comprehension|VLM-guided Grounding Expert for Generalised Referring Expression Comprehension]]
- **作者**: Mingcheng Zhu, Wentian Xu, Tao Lin, Shiying Duan, Ziyun Liang, Xuecheng Qi, Junyang Chen, Kuo Li, Zhifan Wan, Dong Wang, Richard Wang, Yang Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.5，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VLM-guided Grounding Expert for Generalised Referring Expression Comprehension》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalised referring expression comprehension (GREC) aims to identify and localise the zero, one or multiple objects referred to by a language expression. In robotic manipulation, grounding also needs to remain accurate when requests for the same objects are paraphrased or embedded in additional context in robotics. However, grounding expert models are sensitive to instruction variation, while generative vision--language models (VLMs) struggle with complete target recovery and rejection of absent targets. These complementary limitations motivate combining the contextual representations of VLMs with the direct spatial prediction capabilities of grounding experts. We therefore introduce VLM-guided Grounding Expert (VGE), which combines a frozen VLM with a trainable grounding expert through layerwise joint attention and text-conditioned instance scoring. These interfaces leverage multimodal understanding of the VLM to guide object-query refinement and candidate selection while retaining direct bounding-box prediction. Across three datasets, VGE achieves the highest averaged F1 score among the evaluated methods on all five test splits, with differences of at most 1.2 percentage points across instruction conditions within each split. On the dataset with robotic scenes, VGE also achieves the highest F1 across instruction variants and no-target, single-target and multiple-target cases. VGE provides a $5.3$--$13.0\times$ inference speedup over the baseline with the same VLM base model. These results support combining VLM context with specialised spatial prediction to address both grounding challenges, with particularly strong performance in robotic scenes. Code will be released upon publication.

</details>

---

### [[20_Research/Papers/具身智能/InteractVLA_Turning_VLAs_into_Interactive_Tools_for_Agentic_Robotic_Manipulation|InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation]]

![[assets/2611.22584_figure.png|800]]

- **arXiv**: [2611.22584](https://arxiv.org/abs/2611.22584)
- **PDF**: https://arxiv.org/pdf/2611.22584
- **详细分析**: [[20_Research/Papers/具身智能/InteractVLA_Turning_VLAs_into_Interactive_Tools_for_Agentic_Robotic_Manipulation|InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation]]
- **作者**: Chen Zhao, Zipeng Ye, Shifeng Bao, Yihan Lin, Haitao Shen, Yining Luo, Yuchen Xie, Jing Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.8，大模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《InteractVLA: Turning VLAs into Interactive Tools for Agentic Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：InteractVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing agentic manipulation systems treat pretrained vision-language-action (VLA) policies as opaque, language-only primitives: when a policy call fails under unfamiliar instructions or scene perturbations, the agent cannot steer its behavior and is forced into futile retries or costly manual takeover. We present InteractVLA, a framework that turns pretrained flow-based VLAs into geometrically steerable and inspectable tools through a bidirectional geometric interface with vision-language agents. In the forward direction, test-time geometric guidance translates an agent-specified end-effector target into input gradients through the action expert via a differentiable command-to-pose mapping, while soft-time target alignment treats arrival time as a latent execution index to match the target pose without distorting the policy's approach motion. In the reverse direction, action-informed agentic refinement exposes generated action chunks and calibrated camera reprojections back to the agent, allowing it to diagnose spatial discrepancies, revise targets for subsequent VLA calls, or locally adjust motion segments on top of the guided trajectory. Making the VLA controllable not only boosts online agentic tool use, but also unlocks effective recursive self-improvement (RSI), achieving state-of-the-art performance of 99.4\% on LIBERO-Plus, 48.62\% on RoboDojo, and 89.4\% on RoboCasa365. Project page: https://lingwupro.github.io/InteractVLA/.

</details>

---

### [[20_Research/Papers/具身智能/Progress_Predicts_Policy|Progress Predicts Policy]]

![[assets/2611.22491_figure.png|800]]

- **arXiv**: [2611.22491](https://arxiv.org/abs/2611.22491)
- **PDF**: https://arxiv.org/pdf/2611.22491
- **详细分析**: [[20_Research/Papers/具身智能/Progress_Predicts_Policy|Progress Predicts Policy]]
- **作者**: Licheng Zhong, Gim Hee Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.3（加权：具身智能 0.6，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Progress Predicts Policy》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ProgressVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A task specifies how the world should change, while a policy specifies what the robot should do. We introduce Progress Predicts Policy (PPP), which learns a language-conditioned scalar field through the commands induced by its differential. We obtain action conditioning by composing a latent progress field with a shared world model and read its action gradient at a fixed reference command. Continuous commands scale this gradient by a learned positive gain, while discrete commands use finite differences of the same scalar. This yields a hybrid policy without a separate action head or iterative search. Fitting demonstration progress values alone does not ensure that action gradients align with expert commands. PPP trains the induced commands by imitation and uses double backpropagation for the continuous gradient readout to shape the field's local control geometry. Demonstration timing calibrates field values on observed states without additional annotation. The continuous readout remains learnable without progress labels but these timing-derived targets support progress monitoring during execution. Experiments in simulated and real robot manipulation show that PPP outperforms behavioral cloning under a shared architecture.

</details>

---

### [[20_Research/Papers/具身智能/VoxelSBFL_Voxel-Level_Spectrum-Based_Failure_Prediction_for_Vision-Language-Action_Models|VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models]]

![[assets/2611.22453_figure.png|800]]

- **arXiv**: [2611.22453](https://arxiv.org/abs/2611.22453)
- **PDF**: https://arxiv.org/pdf/2611.22453
- **详细分析**: [[20_Research/Papers/具身智能/VoxelSBFL_Voxel-Level_Spectrum-Based_Failure_Prediction_for_Vision-Language-Action_Models|VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models]]
- **作者**: Arusa Kanwal, Pablo Valle, Paola Roggero, Miren Illarramendi, Shaukat Ali, Aitor Arrieta
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《VoxelSBFL: Voxel-Level Spectrum-Based Failure Prediction for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models integrate visual perception, language understanding, and action generation to control robots. Testing these systems produces trajectories and task outcomes, but existing approaches provide limited guidance on using these recorded trajectories to assess subsequent executions or inform policy repair. We conjecture that, for a given policy and task, traversing certain workspace regions is associated with a higher likelihood of failure. To investigate this conjecture, we propose VoxelSBFL, a black-box adaptation of Spectrum-Based Fault Localization (SBFL) in which workspace voxels replace program elements as units of analysis. Recorded tool-center-point (TCP) trajectories provide binary voxel coverage, which is combined with execution outcomes to construct suspiciousness maps using established SBFL formulas. These maps identify failure-associated regions and score unseen trajectories without requiring internal model access. We evaluate 34 spectrum-based techniques across four VLA models using 96,000 Pick-Up trajectories in simulation and compare the leading techniques against eight action- and trajectory-based metrics. VoxelSBFL obtains an overall macro ROC-AUC of 0.704, significantly outperforming state-of-the art baselines. Sensitivity analyses show that performance varies with spatial granularity and training-set size. These findings support spatial spectra for VLA execution assessment and motivate future research on runtime monitoring, self-healing and targeted policy improvement.

</details>

---

### [[20_Research/Papers/强化学习/Autonomous_Track_Racing_with_a_Commercially_Available_Humanoid_System_Design_and_Real-World_Deployment|Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment]]

![[assets/2611.22445_first_page.png|800]]

- **arXiv**: [2611.22445](https://arxiv.org/abs/2611.22445)
- **PDF**: https://arxiv.org/pdf/2611.22445
- **详细分析**: [[20_Research/Papers/强化学习/Autonomous_Track_Racing_with_a_Commercially_Available_Humanoid_System_Design_and_Real-World_Deployment|Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment]]
- **作者**: Koki Inami, Takashi Sato, Hiroyuki Oka, Shota Takizawa, Yuya Takahashi, Amon Suzuki, Hayato Ono, Kohtaro Ihara, Yuki Noka, Shohei Matsugu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Autonomous Track Racing with a Commercially Available Humanoid: System Design and Real-World Deployment》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：BezierLaneNet, CLRerNet, GANet, Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-based methods now let humanoids run robustly, and they have begun to compete in athletic events. Yet few reports describe a complete autonomous humanoid running system in an actual race, where the robot must follow a lane at a new venue, pace itself within hardware limits, and finish without intervention. We report such a system deployed on the Unitree G1, a commercially available general-purpose humanoid, in the 100 m, 400 m, and 1500 m events of the World Humanoid Robot Games 2026. The system integrates vision-based lane perception, path tracking, and a running policy trained by reinforcement learning with a human motion prior. To address the challenges of humanoid running, we stabilize head-camera images against body motion and use IMU-assisted leg odometry to bridge flight phases. To manage motor heating, we penalize hip-pitch torque during training, add heat-dissipation plates, and apply temperature-based speed limiting with event-specific pacing. The robot placed 13th of 74 in the 100 m, 10th of 44 in the 400 m first round before falling in the semifinal, and seventh of 35 in the 1500 m. In this deployment, thermal margin set the pace in every event, and the semifinal fall followed a lane-detection error.

</details>

---

### [[20_Research/Papers/机器人/BehaVerify_A_Formal_Verification_Tool_for_Behavior_Trees|BehaVerify: A Formal Verification Tool for Behavior Trees]]

![[assets/2611.22403_first_page.png|800]]

- **arXiv**: [2611.22403](https://arxiv.org/abs/2611.22403)
- **PDF**: https://arxiv.org/pdf/2611.22403
- **详细分析**: [[20_Research/Papers/机器人/BehaVerify_A_Formal_Verification_Tool_for_Behavior_Trees|BehaVerify: A Formal Verification Tool for Behavior Trees]]
- **作者**: Serena S. Serbinowska, Ben Wooding, Diego Manzanas Lopez, Luke Nam, Anne M. Tumlin, Nicholas K. Potteiger, Hongchao Zhang, Taylor T. Johnson
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《BehaVerify: A Formal Verification Tool for Behavior Trees》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents BehaVerify, a verification toolbox for behavior trees (BTs) and Neuro-Symbolic BTs. BTs are a graphical language for planning and sequencing behaviors - similar to extended state machines - and are increasingly used in safety-critical domains. BehaVerify enables users to specify a BT using a Domain Specific Language (DSL) with formal syntax and semantics. This language further includes Linear Temporal Logic and Computation Tree Logic specifications. BehaVerify uses an efficient encoding into nuXmv, called fastforwarding, to quickly verify if a specification holds over the BT. Additionally, BehaVerify can generate implementations of the BT in Python and Haskell. Through Python, BehaVerify has been integrated with PyTrees and Robot Operating System (ROS) and has been deployed to several autonomous robotic systems, including for verifying runtime monitors. While prior works have developed the underlying theory, this manuscript focuses on the toolbox usage, functionality and implementation. BehaVerify is open source: https://github.com/verivital/behaverify

</details>

---

### [[20_Research/Papers/机器人/SkiNet-Sim_Simulating_Petri_Nets_with_Data_for_the_Verification_and_Validation_of_Controllers_for_Autonomous_Systems|SkiNet-Sim: Simulating Petri Nets with Data for the Verification and Validation of Controllers for Autonomous Systems]]

![[assets/2611.22397_first_page.png|800]]

- **arXiv**: [2611.22397](https://arxiv.org/abs/2611.22397)
- **PDF**: https://arxiv.org/pdf/2611.22397
- **详细分析**: [[20_Research/Papers/机器人/SkiNet-Sim_Simulating_Petri_Nets_with_Data_for_the_Verification_and_Validation_of_Controllers_for_Autonomous_Systems|SkiNet-Sim: Simulating Petri Nets with Data for the Verification and Validation of Controllers for Autonomous Systems]]
- **作者**: Baptiste Pelletier, Karen Godary
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《SkiNet-Sim: Simulating Petri Nets with Data for the Verification and Validation of Controllers for Autonomous Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A large amount of high-level Petri net formalisms has been investigated and deployed in academic settings over the past decades, but these deployments fail to reach practical applications, despite the strong guarantees they can bring to stakeholders. In particular, the lack of direct benefits from end-users reduces the appeal of Petri nets, both due to the overly simple classical Petri net formalism, and the overly specialized high-level formalisms, on top of state-space explosion issues. In this work, we investigate how a middle-ground could be reached, by separating the implementation-specific aspects of software or hardware behaviors, from the classical Petri net semantics. The goal is to benefit from the sought-after aspects of Petri nets, namely their simple firing semantic and model-checking capabilities, while still being able to augment their behavior to best reflect the modelled system. We present a formal model of Interpreted Petri nets with data-aware transitions and tokens. We illustrate this formalism by modelling the executive layer of a robotic system, and provide a lightweight tool to augment classical Petri nets for general purpose applications, as well as data-aware state-space exploration for model-checking. Their specialization in the context of autonomous robotics is showcased, with a complete industrial inspection mission use-case, to compare simulation and model-checking results between the classical and the new data-aware Petri net semantic.

</details>

---

### [[20_Research/Papers/强化学习/Hidden_Variables_Behind_Real-Robot_Data_Quality_Lessons_from_Hundreds_of_Thousands_of_Hours|Hidden Variables Behind Real-Robot Data Quality: Lessons from Hundreds of Thousands of Hours]]

![[assets/2611.22388_figure.png|800]]

- **arXiv**: [2611.22388](https://arxiv.org/abs/2611.22388)
- **PDF**: https://arxiv.org/pdf/2611.22388
- **详细分析**: [[20_Research/Papers/强化学习/Hidden_Variables_Behind_Real-Robot_Data_Quality_Lessons_from_Hundreds_of_Thousands_of_Hours|Hidden Variables Behind Real-Robot Data Quality: Lessons from Hundreds of Thousands of Hours]]
- **作者**: Maniformer Real-World Manipulation Team, Che Tsang Calvin, Xingyu Chen, Bowen Jiang, Naixiang Gao, Xiongfeng Cai, Enlin Gu, Ruiying Li, Peize Li, Mianrui Zhu, Haomiao Zhang, Xin He...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Hidden Variables Behind Real-Robot Data Quality: Lessons from Hundreds of Thousands of Hours》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As real-robot data collection scales, collection-system design shapes both operator efficiency and the behaviors learned by robot policies. Workspace limitations, control-interface friction, and latency can introduce pauses, detours, and corrective motions into otherwise successful demonstrations. We investigate these effects across embodiment, teleoperation control, and data consistency, combining a kinematic study of 25 dual-arm robots, controlled teleoperation experiments, and real-robot evaluation of fine-tuned $π_{0.5}$ policies. The embodiment study shows that positional reachability overstates orientation-aware task coverage and that modest shoulder motion can substantially expand the effective workspace. Teleoperation experiments show that parallelizing body-part control reduces task completion time by 43-53%, while compliant control improves success and reduces peak contact forces on constrained and contact-rich tasks. Policy-learning experiments show that demonstrations must capture the visual information underlying action choices: active-search demonstrations improve arm-selection accuracy from chance (50%) to 100%. Calibration experiments reveal that mixed-calibration training data remain usable in our tested configurations when an inference-aligned subset is retained, whereas inference-time miscalibration causes all 30 trials to fail. Policies also retain approximately 90% of the extra path length in detour-contaminated demonstrations, showing how inefficient operator motions persist in learned behavior. Together, these findings connect collection-system design to demonstration quality and downstream policy execution. They motivate evaluating effective workspace, control efficiency, observation completeness, calibration alignment, and motion quality before scaling collection, and addressing system-induced compensations at their source.

</details>

---

### [[20_Research/Papers/具身智能/SR-VLA_Stall-Reduced_VLA_Execution_via_Predicted-Input_Lookahead_and_Selective_KV_Cache_Repair|SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair]]

![[assets/2611.22356_figure.png|800]]

- **arXiv**: [2611.22356](https://arxiv.org/abs/2611.22356)
- **PDF**: https://arxiv.org/pdf/2611.22356
- **详细分析**: [[20_Research/Papers/具身智能/SR-VLA_Stall-Reduced_VLA_Execution_via_Predicted-Input_Lookahead_and_Selective_KV_Cache_Repair|SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair]]
- **作者**: Tao Zhang, Yi Zhong, Jinhao Ruan, Yipeng Gao, Linfeng Zhong, Youming Yang, Yuan Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《SR-VLA: Stall-Reduced VLA Execution via Predicted-Input Lookahead and Selective KV Cache Repair》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SR-VLA, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies incur control stalls when inference blocks the next action chunk. Asynchronous early inference can hide latency, but its results may be inconsistent with the arriving actual inputs. Unconditional reuse risks acting on mismatched inputs, whereas full recomputation discards useful precomputation. We propose SR-VLA, combining predicted-input lookahead with selective KV cache repair. During current chunk execution, a lightweight action-conditioned predictor generates next-boundary visual observations and proprioceptive state. These predictions, together with the task instruction, drive the frozen VLA to precompute a speculative KV cache and action chunk. After real inputs are available to VLA, predicted--real differences and task conditions determine whether to accept the action chunk or trigger selective KV repair. On LIBERO, SR-VLA achieves $2.67\times$ and $1.27\times$ query speedups over the respective synchronous $π_{0.5}$ and OpenVLA-OFT baselines, while maintaining competitive average task success rates. Under target-motion perturbation, success remains baseline-comparable, with $1.52\times$--$1.93\times$ query speedup.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Episodic_Recall_Experience-to-Knowledge_Evolution_for_Lifelong_Embodied_Navigation|Beyond Episodic Recall: Experience-to-Knowledge Evolution for Lifelong Embodied Navigation]]

![[assets/2611.22321_figure.png|800]]

- **arXiv**: [2611.22321](https://arxiv.org/abs/2611.22321)
- **PDF**: https://arxiv.org/pdf/2611.22321
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Episodic_Recall_Experience-to-Knowledge_Evolution_for_Lifelong_Embodied_Navigation|Beyond Episodic Recall: Experience-to-Knowledge Evolution for Lifelong Embodied Navigation]]
- **作者**: Weitao An, Chenghao Xu, Xu Yang, Cheng Deng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Beyond Episodic Recall: Experience-to-Knowledge Evolution for Lifelong Embodied Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, LMEE-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lifelong embodied navigation requires agents to accumulate experience through continuous interaction and reuse it for subsequent goal searches. Existing memory-enhanced methods typically retain historical observations or construct structured scene representations. However, storing observations or high-dimensional semantic embeddings incurs growing storage costs. Meanwhile, structured representations support retrieval and semantic reasoning but do not explicitly evolve accumulated experience into environment-specific knowledge. To address these limitations, we propose Experience-Evolving Memory (EvoNav), a novel two-timescale memory framework. It organizes semantic observations, spatial relations, and task-feedback cues into sparse experience atoms. During online operation, experience atoms continually consolidate repeated observations and form dynamic links based on transitions. At the slower timescale, EvoNav distills accumulated category co-occurrences and feedback signals into environment-specific structural knowledge without relying on predefined object--room relations. For each new goal, EvoNav combines direct goal evidence from experience atoms with learned structural knowledge to guide goal-directed search on the current traversability map. Experiments on single-goal, sequential multi-floor, and multimodal navigation demonstrate effective experience reuse and improved path efficiency with compact persistent memory, together with successful transfer to a real robot.

</details>

---

### [[20_Research/Papers/强化学习/Where_Do_Human-to-Robot_Transfer_Gains_Come_From|Where Do Human-to-Robot Transfer Gains Come From?]]

![[assets/2611.22302_figure.png|800]]

- **arXiv**: [2611.22302](https://arxiv.org/abs/2611.22302)
- **PDF**: https://arxiv.org/pdf/2611.22302
- **详细分析**: [[20_Research/Papers/强化学习/Where_Do_Human-to-Robot_Transfer_Gains_Come_From|Where Do Human-to-Robot Transfer Gains Come From?]]
- **作者**: Jiachen Li, Shihao Li, Soovadeep Bakshi, Longteng Fan, Dongmei Chen, Long Chen, Zhuo Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Where Do Human-to-Robot Transfer Gains Come From?》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ImageNet, Meta-World, MetaWorld, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human data can support robot policy pretraining, but gains attributed to a data recipe may also reflect subset size, training variability, or downstream adaptation. In an HPT implementation on a 20-task MetaWorld suite with three training blocks, a constrained random 5,000-recording subset matches most of the task-informed subset's gain over the 40,000-recording pool at 20,000 updates (3.69 of 4.29 percentage points), leaving equal-size selection differences of 0.60 points at 5,000 recordings and 0.45 points at 1,250 recordings, with wide paired intervals. Across 12 comparisons, task orderings repeat across seeds for several contrasts, but a fixed predictor built from the other two seeds trails the mean or difficulty reference in at least one held-out fold for every comparison. Neither mechanism probe shows its predicted positive interaction: task-slot mismatch yields an interaction of $-0.0347$ points after adaptation, and in a six-task observation experiment the observation-by-pretraining interaction changes sign between seeds ($-18.29$ and $+1.04$ points) while full-state pretraining gains are positive in both ($+6.37$ and $+2.31$ points). This retrospective study shows how equal-size and capacity controls, seed-level reporting, and targeted interventions change the interpretation of apparent transfer gains.

</details>

---

### [[20_Research/Papers/机器人/ALERT_Extending_Humanoid_Motion_Trackers_with_a_General_and_Lightweight_Human_Avoidance_Pipeline|ALERT: Extending Humanoid Motion Trackers with a General and Lightweight Human Avoidance Pipeline]]

![[assets/2611.22258_figure.png|800]]

- **arXiv**: [2611.22258](https://arxiv.org/abs/2611.22258)
- **PDF**: https://arxiv.org/pdf/2611.22258
- **详细分析**: [[20_Research/Papers/机器人/ALERT_Extending_Humanoid_Motion_Trackers_with_a_General_and_Lightweight_Human_Avoidance_Pipeline|ALERT: Extending Humanoid Motion Trackers with a General and Lightweight Human Avoidance Pipeline]]
- **作者**: Zhaoyang Li, Chiyu Zhang, Chengxin Xu, Peng Yang, Zhonghao Guo, Wanting Li, Ziyu Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《ALERT: Extending Humanoid Motion Trackers with a General and Lightweight Human Avoidance Pipeline》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Person-MinkUNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body motion tracking has enabled humanoid dancing, athletic motions, and teleoperation, providing a foundation for capability demonstrations and manipulation data collection. However, existing tracking policies lack awareness of nearby humans and proactive avoidance capabilities, while motion substitution and local constraint-based corrections may compromise reference motion integrity and tracking continuity. We propose ALERT, a general lightweight pipeline for extending motion tracking to shared human-robot environments. Through lightweight adaptation, it integrates human perception and proactive avoidance into pretrained tracking policies, balancing avoidance demands with reference motion tracking while preserving existing motion capabilities. Simulation and real-world experiments across tracking backbones demonstrate reliable collision-free execution through localized human avoidance, preserving whole-body coordination and enabling rapid recovery of reference tracking, while retaining the ability of pretrained policies to track unseen motions.

</details>

---

### [[20_Research/Papers/机器人/HandUMI_A_Modular_Hand-Worn_Parallel-Jaw_Interface_for_Robot-Free_Bimanual_Data_Capture|HandUMI: A Modular Hand-Worn Parallel-Jaw Interface for Robot-Free Bimanual Data Capture]]

![[assets/2611.22146_figure.png|800]]

- **arXiv**: [2611.22146](https://arxiv.org/abs/2611.22146)
- **PDF**: https://arxiv.org/pdf/2611.22146
- **详细分析**: [[20_Research/Papers/机器人/HandUMI_A_Modular_Hand-Worn_Parallel-Jaw_Interface_for_Robot-Free_Bimanual_Data_Capture|HandUMI: A Modular Hand-Worn Parallel-Jaw Interface for Robot-Free Bimanual Data Capture]]
- **作者**: Brik Meza, Leonardo Perez, Alvaro Mendoza-Li, Aniela Ubillus, Mitshell Ramos, Raul Bastidas, Mauricio Olivera, Bryan Bastidas
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《HandUMI: A Modular Hand-Worn Parallel-Jaw Interface for Robot-Free Bimanual Data Capture》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

HandUMI captures robot-free bimanual demonstrations with a hand-worn parallel-jaw interface. Swappable fingertips match the robot's installed gripper; Quest/PICO controllers track hands and encoders measure aperture. Robot-agnostic recordings are retargeted by inverse kinematics to seven simulated bimanual arms (median position error $\leq 1.2$ mm; $\leq 4.7$% of episodes rejected). On bimanual towel folding, 562 robot-free demonstrations train policies on real PiPER arms: ACT succeeds in 12/20 attempts and fine-tuned $π_{0.5}$ in 7/20; ACT on the first 101 and base $π_{0.5}$ each succeed in 0/20. Hardware and software are open source (Apache-2.0), and a pair costs USD 557 with Quest 3S, excluding the optional ZED Mini and host computer. Project website: https://murobotics.ai/research/handumi.

</details>

---

### [[20_Research/Papers/机器人/Low-speed_Limit_Cycle_Walking_of_Planar_X-shaped_Bipedal_Robot_with_Special_Properties|Low-speed Limit Cycle Walking of Planar X-shaped Bipedal Robot with Special Properties]]

![[assets/2611.22122_figure.png|800]]

- **arXiv**: [2611.22122](https://arxiv.org/abs/2611.22122)
- **PDF**: https://arxiv.org/pdf/2611.22122
- **详细分析**: [[20_Research/Papers/机器人/Low-speed_Limit_Cycle_Walking_of_Planar_X-shaped_Bipedal_Robot_with_Special_Properties|Low-speed Limit Cycle Walking of Planar X-shaped Bipedal Robot with Special Properties]]
- **作者**: Fumihiko Asano, Cong Yan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Low-speed Limit Cycle Walking of Planar X-shaped Bipedal Robot with Special Properties》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes a novel planar semicircular-footed X-shaped bipedal robot in which the center of mass of each leg link is at the same position as the hip joint, and discusses a method for generating a stable limit cycle gait on level ground. First, we outline the assumptions of the robot model with four degrees of freedom, and develop the mathematical equations of motion and collision. Second, we set the relative hip-joint angle as a control output and design a control system to follow it to the desired trajectory specified as a fifth-order function of time. Third, we mathematically show that there are special properties: the angular velocity of the swing leg does not change before and after the collision, and the time-integral of the control input becomes zero in a steady gait. We also mathematically show that the model has the feature that approximate linearization is effective and the antigravity effect of semicircular feet can be utilized. Through numerical simulations, we verify the validity of the theoretical results, and analyze some fundamental gait properties such as convergence speed and mechanical energy restoration.

</details>

---

### [[20_Research/Papers/大模型/ReLAP_Latent_Action_Pretraining_through_Recurrent_Video_Prediction_in_JEPA_Space|ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space]]

![[assets/2611.22077_figure.png|800]]

- **arXiv**: [2611.22077](https://arxiv.org/abs/2611.22077)
- **PDF**: https://arxiv.org/pdf/2611.22077
- **详细分析**: [[20_Research/Papers/大模型/ReLAP_Latent_Action_Pretraining_through_Recurrent_Video_Prediction_in_JEPA_Space|ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space]]
- **作者**: R. Gnana Praveen, Ali Rouzbayani, Zhiying Jiang, Bidhan Roy
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 大模型, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.3，世界模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《ReLAP: Latent Action Pretraining through Recurrent Video Prediction in JEPA Space》归入 机器人、世界模型、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoLA-World, RotVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Videos provide a rich source of physical interaction for learning robot behavior without action annotations, yet effective latent actions must capture not only local transitions but also how those transitions evolve over time. We introduce ReLAP, a latent-action pretraining framework that couples local transition learning with recurrent multi-step prediction in a frozen JEPA representation space. A shared inverse dynamics model infers compact continuous latent actions from adjacent observations, while a latent world model recurrently predicts the future JEPA features. Because each predicted feature becomes the context for the next transition, errors at later steps backpropagate through the rollout to earlier latent actions, encouraging temporally coherent dynamics beyond pairwise reconstruction. We transfer this representation to a vision-language model using two complementary objectives: latent distillation from the frozen inverse teacher and recurrent future-feature prediction through the frozen latent world model. The resulting policy is then adapted to robot demonstrations with action flow matching. At deployment, the explicit latent-action and world-model branches are removed, and the fine-tuned VLM predicts physical actions directly, reducing inference complexity. With only 11M pretraining samples and 1.06B trainable parameters, ReLAP achieves 97.9% on standard LIBERO and 70.0% over zero-shot LIBERO-Plus perturbations. On the LARY latent-action benchmark, ReLAP ranks second in both mean regression error and mean classification accuracy among the compared methods. These results demonstrate that recurrent action-free latent action pretraining can learn compact, temporally structured, and transferable representations for downstream robot control.

</details>

---

### [[20_Research/Papers/具身智能/DreamFAR_Real-Time_and_Long-Horizon_Interaction_with_Diverse_Objects|DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects]]

![[assets/2611.22001_figure.png|800]]

- **arXiv**: [2611.22001](https://arxiv.org/abs/2611.22001)
- **PDF**: https://arxiv.org/pdf/2611.22001
- **详细分析**: [[20_Research/Papers/具身智能/DreamFAR_Real-Time_and_Long-Horizon_Interaction_with_Diverse_Objects|DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects]]
- **作者**: Yiming Dou, Botao He, Antonio Loquercio, Andrew Owens, Jitendra Malik, Sumedh Anand Sontakke, Ruoshi Liu
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.6，世界模型 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《DreamFAR: Real-Time and Long-Horizon Interaction with Diverse Objects》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Ctrl-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models have shown great potential in serving as a simulator for robot manipulation. However, existing models are either fit to a single environment or lack ability to simulate long-horizon contact-rich events. We present DreamFAR, a world model whose dynamics model is trained from scratch on a large robot-native teleoperation dataset, with no internet-video pretraining. We present an architecture and learning recipe designed for training on robot-native data. DreamFAR is significantly smaller than the high-performance video generation models, yet shows better understanding of contact and causality, and runs 10 FPS on a commercial GPU. Experimentally, DreamFAR significantly outperforms existing models in predicting the long-horizon future. We further demonstrate various applications where DreamFAR can be used, including policy evaluation and mixed-data co-training. Project page: https://www.yimingdou.com/DreamFAR/

</details>

---

### [[20_Research/Papers/强化学习/From_Human_Videos_to_Bimanual_Dexterous_Manipulation_Data_Confidence-Guided_RL_Refinement_of_Video_Priors|From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors]]

![[assets/2611.21908_figure.png|800]]

- **arXiv**: [2611.21908](https://arxiv.org/abs/2611.21908)
- **PDF**: https://arxiv.org/pdf/2611.21908
- **详细分析**: [[20_Research/Papers/强化学习/From_Human_Videos_to_Bimanual_Dexterous_Manipulation_Data_Confidence-Guided_RL_Refinement_of_Video_Priors|From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors]]
- **作者**: Yanghong Liu, Yang Chen, Kailang Xu, Bang Du, Feiyang Yang, Jiawei Xia, Zhengtao Yao, Yubiao Zhang, Masayoshi Tomizuka, Ruihai Wu, Wei Zhan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《From Human Videos to Bimanual Dexterous Manipulation Data: Confidence-Guided RL Refinement of Video Priors》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting demonstrations for bimanual dexterous manipulation is costly, motivating the use of human videos as a source of robot training data. However, uncertainty in video-derived motion estimates and differences between human and robot embodiments make direct motion transfer challenging. In this work, we introduce PriDex, a framework that transforms human-video Priors into executable robot Dexterous manipulation demonstrations through reinforcement learning in simulation. PriDex preserves task-relevant interaction structure while allowing embodiment-specific behavior to be regenerated for the robot. Human-object interactions provide affordance cues for selecting task-relevant, robot-specific grasps from geometry-based candidates. For motion refinement, object trajectories provide a task-level reference, while relative bimanual wrist trajectories offer complementary guidance for coordinated motion. Since object-motion estimates can become unreliable under occlusion or visual ambiguity, PriDex uses object-motion confidence to adaptively balance these two priors, emphasizing object-level guidance when confidence is high and increasing the contribution of wrist-level guidance as confidence decreases. Reinforcement learning refines these video-derived priors under the robot's kinematic and physical constraints, and the resulting policies are rolled out to generate robot demonstrations for training a vision-based diffusion policy. We evaluate PriDex on four bimanual dexterous manipulation tasks, including pouring, sweeping into a dustpan, bottle-cap unscrewing, and plate cleaning, assessing both simulation-based robot data generation and downstream visuomotor policy learning.

</details>

---

### [[20_Research/Papers/世界模型/ASTRA_ASV_Simulator_for_Transferable_Realistic_Autonomy|ASTRA: ASV Simulator for Transferable Realistic Autonomy]]

![[assets/2611.21789_figure.png|800]]

- **arXiv**: [2611.21789](https://arxiv.org/abs/2611.21789)
- **PDF**: https://arxiv.org/pdf/2611.21789
- **详细分析**: [[20_Research/Papers/世界模型/ASTRA_ASV_Simulator_for_Transferable_Realistic_Autonomy|ASTRA: ASV Simulator for Transferable Realistic Autonomy]]
- **作者**: Tsimafei Lazouski, Cody Sheltraw, Alan Papalia, Maani Ghaffari
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.7（加权：具身智能 0.6，世界模型 0.2，机器人 0.9）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《ASTRA: ASV Simulator for Transferable Realistic Autonomy》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ASVSim, AirSim, MarineGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomy development for marine autonomous surface vehicles (ASVs) remains challenging because field testing is costly and difficult to reproduce. Existing marine simulation tools provide mature capabilities in vessel dynamics, robotics integration, and visual rendering, but these strengths are emphasized differently across platforms. This paper presents ASTRA, an ASV simulation framework built in NVIDIA Isaac Sim that combines marine vehicle dynamics, photorealistic perception, and Robot Operating System (ROS 2) autonomy interfaces within a common environment. ASTRA incorporates a Fossen-style marine dynamics model together with geometry-based buoyancy and programmable spectral wave disturbances, enabling non-planar hydrostatic and wave-induced motion. The simulator reproduces the sensor configuration of a physical BlueBoat testbed, including GPS, IMU, LiDAR, and RGB-D sensing exposed through ROS 2. This allows localization, perception, planning, and control software to be developed against interfaces consistent with the physical platform. The BlueBoat's existing ROS 2 localization and perception modules were ported directly into ASTRA, while targeted zero-propulsion experiments were used to verify the implemented wave-body coupling. The simulated roll response was consistent with the expected non-oscillatory hydrostatic behavior, and heave remained highly coherent with the generated wave field, with approximately unity gain at the dominant wave frequency in the tested sea states. ASTRA is intended as an open-source testbed for marine autonomy development, simulation-based benchmarking, and sim-to-real experimentation.

</details>

---

### [[20_Research/Papers/机器人/An_Open-Source_da_Vinci_X_Xi_Instrument_Module_for_Laparoscopic_Surgery_Research|An Open-Source da Vinci X/Xi Instrument Module for Laparoscopic Surgery Research]]

![[assets/2611.21771_first_page.png|800]]

- **arXiv**: [2611.21771](https://arxiv.org/abs/2611.21771)
- **PDF**: https://arxiv.org/pdf/2611.21771
- **详细分析**: [[20_Research/Papers/机器人/An_Open-Source_da_Vinci_X_Xi_Instrument_Module_for_Laparoscopic_Surgery_Research|An Open-Source da Vinci X/Xi Instrument Module for Laparoscopic Surgery Research]]
- **作者**: Douglas McDonough, Justin Liao, Jiawei Ge, Antony Goldenberg, Yvonne Zhang, Mackenzie A Eagleson, Ravi Prakash, Axel Krieger, Chunwoo Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《An Open-Source da Vinci X/Xi Instrument Module for Laparoscopic Surgery Research》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Studying electrosurgical tasks on a research robot requires control of both instrument motion and energy activation, along with a record of when each action occurs. This paper presents an open-source module for da Vinci X/Xi instruments on a UR5/UR5e robotic arm. Five motors transmit torque through timing belts to spring-loaded drive discs. An electrosurgical interposer accepts software commands, gives the surgeon's foot pedals priority, and records the source of each activation request. In bench testing, the interposer recorded all 12 activation and deactivation events from six pedal presses. Ex vivo demonstrations included monopolar and bipolar coagulation of splenic tissue and monopolar cutting during gallbladder dissection. Optical tracking of the Fenestrated Bipolar Forceps showed that calibration brought pitch and yaw gains from 0.904 and 1.14 to 1.00 and 1.02, respectively. The module enables researchers to record instrument motion, video, and the timing and source of electrosurgical commands during laparoscopic tasks.

</details>

---
