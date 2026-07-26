# cs.RO | Robotics | 2026-07-24

#arxiv #ComputerScience

**论文数**: 17

### [[20_Research/Papers/具身智能/AXIS_A_Growable_Community-Driven_Data_Engine_for_Scalable_Robot_Manipulation|AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation]]

![[assets/2607.21588_figure.png|800]]

- **arXiv**: [2607.21588](https://arxiv.org/abs/2607.21588)
- **PDF**: https://arxiv.org/pdf/2607.21588
- **详细分析**: [[20_Research/Papers/具身智能/AXIS_A_Growable_Community-Driven_Data_Engine_for_Scalable_Robot_Manipulation|AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation]]
- **作者**: Mengfei Zhao, Dihong Huang, Yikai Tang, Peihao Li, Mingxuan Yan, Ruiqi Zhuang, Yanjia Huang, Jie Wang, Hai Zhai, Tony Zhou, Rui Zhang, Zhexi Luo...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《AXIS: A Growable Community-Driven Data Engine for Scalable Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IsaacSim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning effective robot manipulation policies requires diverse, high-quality demonstrations, yet existing data pipelines are often difficult to scale because they rely on specialized hardware, centralized operators, or fixed task suites. We present AXIS, a growable community-driven data engine and benchmark for scalable robot learning, which enables browser-based teleoperation for large-scale demonstration collection, automatically generates and validates new manipulation tasks, and transforms community-collected demonstrations into training-ready data through automated success checking, quality filtering, trajectory smoothing, and visual and physics-based augmentation. The AXIS dataset currently contains 207 diverse tasks and 50K+ trajectories. Meanwhile, AXIS organizes data into task snapshots and evaluates policies with a systematic held-out protocol. We compare vision-language-action (VLA) policies under a unified AXIS evaluation suite and analyze scaling behavior across different data volumes. Continual pretraining on AXIS substantially improves the overall success rate of $π_{0.5}$ by 5.8%, outperforms the model pretrained on RoboCasa365 by 37.3%, and exhibits consistent scaling with increasing data volume, with the largest gains observed under layout, sensor-noise, and camera perturbations.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Episodic_Evaluation_Memory_Architectural_Bottlenecks_in_Sequential_Embodied_Question_Answering|Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering]]

![[assets/2607.21571_figure.png|800]]

- **arXiv**: [2607.21571](https://arxiv.org/abs/2607.21571)
- **PDF**: https://arxiv.org/pdf/2607.21571
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Episodic_Evaluation_Memory_Architectural_Bottlenecks_in_Sequential_Embodied_Question_Answering|Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering]]
- **作者**: Zikui Cai, Kaushal Janga, Tan Dat Dao, Seungjae Lee, Shivin Dass, Mingyo Seo, Kaiyu Yue, Mintong Kang, Nandhu Pillai, Monte Hoover, Aadi Palnitkar, Ruchit Rawal...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Beyond Episodic Evaluation: Memory Architectural Bottlenecks in Sequential Embodied Question Answering》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EQA, ExploreEQA, GOAT-Bench, OpenEQA, Sequential-EQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied question answering (EQA) is traditionally evaluated under an episodic formulation, where agents solve each task independently and reset internal state between episodes. However, real-world robots operate continuously and must accumulate, retain, and selectively reuse information acquired from prior interactions. Despite this practical requirement, the architectural mechanisms needed to support sequential memory in EQA remain underexplored. In this work, we investigate how different memory architectures behave when EQA agents are evaluated sequentially, with multiple questions answered in the same scene while memory is carried forward across queries. We find that simply preserving existing memory is often insufficient. Agents that retain only traversability information, such as 2D occupancy maps, remember where the robot has explored but not the visual-semantic evidence needed for later questions. Agents trained on short-horizon episodic data face a different challenge: when exposed to continuous, multi-query histories, their inherited context suffers from severe temporal mismatch, rather than forming a reusable scene representation. To overcome this architectural bottleneck, we highlight the necessity of structured, spatially grounded memory: architectures that map persistent visual observations onto metric 3D geometry preserve visual-semantic evidence in a coherent scene representation. Extensive experiments in simulated environments reveal that this form of memory breaks the accuracy-efficiency tradeoff in sequential settings, simultaneously achieving higher answer accuracy and lower navigation costs. We further validate these findings on a real-world mobile robot, demonstrating that spatially grounded visual memory is critical for enabling continuous, intelligent operation in physical environments.

</details>

---

### [[20_Research/Papers/机器人/Grasp,_Handover,_Rotate_Bimanual_Object_Reorientation_via_Compositional_Diffusion_and_Energy-Based_Optimization|Grasp, Handover, Rotate: Bimanual Object Reorientation via Compositional Diffusion and Energy-Based Optimization]]

![[assets/2607.21341_figure.png|800]]

- **arXiv**: [2607.21341](https://arxiv.org/abs/2607.21341)
- **PDF**: https://arxiv.org/pdf/2607.21341
- **详细分析**: [[20_Research/Papers/机器人/Grasp,_Handover,_Rotate_Bimanual_Object_Reorientation_via_Compositional_Diffusion_and_Energy-Based_Optimization|Grasp, Handover, Rotate: Bimanual Object Reorientation via Compositional Diffusion and Energy-Based Optimization]]
- **作者**: Wun Lam Yeung, Wenjun Liu, Yui Cheung Yu, Zhengyan Lambo Qin, Qijin She, Heng Li, Ziqi Wang, Ping Tan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Grasp, Handover, Rotate: Bimanual Object Reorientation via Compositional Diffusion and Energy-Based Optimization》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual object reorientation - picking an object, handing it over between two arms, and placing it in a desired target pose - is valuable when direct placement from the initial grasp is infeasible due to collisions, kinematic constraints, or poor final orientation. However, achieving this under multiple competing objectives remains challenging. We introduce BiCompoDiff, a compositional diffusion and energy-based framework that jointly optimizes grasp selection, handover, regrasp, and motion planning under multiple constraints. By combining a pretrained grasp diffusion model with bimanual planning energy-based models (EBMs), our method injects gradient guidance during reverse diffusion to enforce collision avoidance, trajectory smoothness (via differentiable inverse kinematics), handover feasibility, and regrasp safety. Annealed MCMC sampling further refines grasp poses over the composite energy landscape. Experiments across diverse simulated household reorientation tasks demonstrate that BiCompoDiff achieves over 20% higher success rates and up to 37% smoother trajectories (measured by joint displacement) compared to strong sampling-based baselines. Real-world validation confirms effective sim-to-real transfer and robust performance on challenging scenes.

</details>

---

### [[20_Research/Papers/具身智能/Factorized_Spatio-Temporal_Convolutions_for_Human_Pose_Estimation_from_Planar_Lidar|Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar]]

![[assets/2607.21309_figure.png|800]]

- **arXiv**: [2607.21309](https://arxiv.org/abs/2607.21309)
- **PDF**: https://arxiv.org/pdf/2607.21309
- **详细分析**: [[20_Research/Papers/具身智能/Factorized_Spatio-Temporal_Convolutions_for_Human_Pose_Estimation_from_Planar_Lidar|Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar]]
- **作者**: Simone Arreghini, Mirko Nava, Nicholas Carlotti, Antonio Paolillo, Alessandro Giusti
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Factorized Spatio-Temporal Convolutions for Human Pose Estimation from Planar Lidar》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Localizing nearby humans and estimating their facing direction are key capabilities for safe navigation and socially aware human-robot interaction. Many pose-estimation pipelines target cameras and 3D LiDAR or assume GPU-class compute, whereas service robots are often equipped only with omnidirectional planar LiDARs and modest onboard processors. We address omnidirectional human detection and relative 2D pose estimation from planar LiDAR sequences with a lightweight network based on Space-Time Blocks, which explicitly separate spatial processing along scan rays from temporal aggregation across scans. Our network processes 360° LiDAR sequences to output per-ray human presence, distance, and relative orientation. We train it via cross-modal self-supervision from a narrow RGB-D body tracker in the sensors' overlap region, removing the need for manual LiDAR labels. Quantitative experiments show that our approach consistently outperforms a parameter-matched baseline model, reducing errors in distance (-38%), position (-28%), and orientation (-15%). We further benchmark on the public FROG dataset, report real-time CPU inference on a service robot, and validate with in-field demonstrations, supporting its suitability for spatial perception on computationally constrained service robots.

</details>

---

### [[20_Research/Papers/大模型/FORGE-plus_Force-Budgeted_Recovery_for_Contact-Rich_Assembly_with_a_Frozen_LLM_Supervisor|FORGE-plus: Force-Budgeted Recovery for Contact-Rich Assembly with a Frozen LLM Supervisor]]

![[assets/2607.21227_figure.png|800]]

- **arXiv**: [2607.21227](https://arxiv.org/abs/2607.21227)
- **PDF**: https://arxiv.org/pdf/2607.21227
- **详细分析**: [[20_Research/Papers/大模型/FORGE-plus_Force-Budgeted_Recovery_for_Contact-Rich_Assembly_with_a_Frozen_LLM_Supervisor|FORGE-plus: Force-Budgeted Recovery for Contact-Rich Assembly with a Frozen LLM Supervisor]]
- **作者**: Kyupaeck Jeff Rah, Midum Oh
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 1.7（加权：具身智能 0.6，大模型 0.6，强化学习 0.2，机器人 0.3）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《FORGE-plus: Force-Budgeted Recovery for Contact-Rich Assembly with a Frozen LLM Supervisor》归入 大模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CompliantVLA, ForceVLA, PaCo-VLA, Tactile-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Force-conditioned reinforcement learning (RL) enables tight-clearance assembly under a commanded force ceiling, but practical deployment requires determining an appropriate force limit for each object and recovering from insertion failures without exceeding it. We present a two-layer framework in which a frozen, text-only large language model (LLM) assigns a per-object force ceiling before execution and selects recovery maneuvers from a fixed action menu using compact textual force signatures. The LLM never controls force directly: a low-level controller enforces the force ceiling, the recovery policy cannot increase it, and the hidden breaking-force threshold is known only to the evaluator. We evaluate the framework on fragile bottle placement and 0.4 mm diametral-clearance gear insertion using two grippers (Robotiq 2F-140 and Franka Panda hand). A single policy passes 256/256 evaluation episodes on both fragile and robust objects without breakage, correctly predicts release timing, and completes a full table-pick-and-insert pipeline with a mean peak force of 5.4 N. Under injected in-grip slip, the force-signature recovery strategy resolves 40% and 64% of failures on the two grippers, whereas a press-harder baseline is either ineffective or causes frequent breakage. We also report negative results, including the failure of PPO to solve the task under strict force constraints and unsuccessful learned release strategies. All experiments are conducted in rigid-body simulation with hidden force-threshold breakage; no sim-to-real claim is made.

</details>

---

### [[20_Research/Papers/大模型/RL-MACRO_A_Cybernetic_Closed-Loop_Intelligence_Framework_for_Multimodal_Adaptive_Robotic_Craniotomy|RL-MACRO: A Cybernetic Closed-Loop Intelligence Framework for Multimodal Adaptive Robotic Craniotomy]]

![[assets/2607.21113_figure.png|800]]

- **arXiv**: [2607.21113](https://arxiv.org/abs/2607.21113)
- **PDF**: https://arxiv.org/pdf/2607.21113
- **详细分析**: [[20_Research/Papers/大模型/RL-MACRO_A_Cybernetic_Closed-Loop_Intelligence_Framework_for_Multimodal_Adaptive_Robotic_Craniotomy|RL-MACRO: A Cybernetic Closed-Loop Intelligence Framework for Multimodal Adaptive Robotic Craniotomy]]
- **作者**: Xiao Zhang, Jiaxuan Li, Renzhen Le, Di Wu, Chao Sun, Jiachen Zhu, Haoyuan Zhang, Xiang Li, Jian Liu, Zhenzhi Ying, Pengfei Zhang, Liming Shu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能, 强化学习
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.4，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RL-MACRO: A Cybernetic Closed-Loop Intelligence Framework for Multimodal Adaptive Robotic Craniotomy》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robotic craniotomy requires continuous regulation of tool-tissue interactions to mitigate mechanical overload and thermal damage while maintaining surgical efficiency. However, this process is inherently partially observable due to unknown, time-varying tissue properties and the inability to directly measure cutting temperatures under physical occlusion. To address these challenges, we propose RL-MACRO, a cybernetic closed-loop intelligence framework that couples multimodal perception, adaptive decision-making, and robotic execution. This framework empowers the surgical robot to autonomously perceive inaccessible states from partial sensory feedback and dynamically optimize its behaviors under uncertain environment. A CNN-LSTM observer first fuses force and sound feedback to reconstruct the hidden temperature state (R^2=0.939, MAE = 1.717 deg C). This reconstructed temperature, alongside multi-sensor features, forms the belief state for an offline Implicit Q-Learning (IQL) policy. A novel dual-head Actor dynamically coordinates the feed rate, spindle speed, and cutting depth to optimize efficiency within strict safety bounds. These decisions are seamlessly translated into spatial motions via online trajectory re-planning and velocity servoing. Experiments on bovine ribs and six ex vivo goat skulls validate the system's robust perception, adaptive recovery from force/temperature excursions, and smooth execution on irregular surfaces, establishing a data-driven cybernetic paradigm for safe and efficient autonomous bone cutting.

</details>

---

### [[20_Research/Papers/大模型/Human-Inspired_Framework_for_Robotic_Craniotomy_Integrating_Multimodal_Fusion_and_Adaptive_Trajectory_Adjustment|Human-Inspired Framework for Robotic Craniotomy: Integrating Multimodal Fusion and Adaptive Trajectory Adjustment]]

![[assets/2607.21058_figure.png|800]]

- **arXiv**: [2607.21058](https://arxiv.org/abs/2607.21058)
- **PDF**: https://arxiv.org/pdf/2607.21058
- **详细分析**: [[20_Research/Papers/大模型/Human-Inspired_Framework_for_Robotic_Craniotomy_Integrating_Multimodal_Fusion_and_Adaptive_Trajectory_Adjustment|Human-Inspired Framework for Robotic Craniotomy: Integrating Multimodal Fusion and Adaptive Trajectory Adjustment]]
- **作者**: Renzhen Le, Xiao Zhang, Di Wu, Yuanyu Wei, Jiachen Zhu, Zhenzhi Ying, Pengfei Zhang, Liming Shu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Human-Inspired Framework for Robotic Craniotomy: Integrating Multimodal Fusion and Adaptive Trajectory Adjustment》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manual craniotomy is a high-risk, skill-dependent procedure associated with surgeon fatigue and potential dural injury. While robotic approaches have improved safety, existing open-loop systems rely solely on preoperative images and cannot compensate for intraoperative registration errors or tissue deformation. To address this, we propose a human-inspired closed-loop robotic craniotomy framework that intelligently integrates preoperative planning with intraoperative execution. An adaptive dual-contour fusion algorithm is employed to generate trajectories that conform to complex cranial geometries while maintaining a consistent tool-bone relative pose. For intraoperative perception, a multimodal two-stage cross-modal attention block (CMA)-temporal convolutional network (TCN)-Transformer network combined with an adaptive Bayesian filter fuses force and acoustic signals to achieve robust breakthrough detection under varying bone conditions. Upon detection, an in-situ projection-based trajectory adjustment strategy dynamically compensates for depth deviations, enabling safe residual bone isolation. Experiments on bovine ribs show a breakthrough prediction accuracy of 97%, a detection latency of 0.048 +/- 0.097 s, and a maximum overshoot of 0.29 mm. All four ex vivo cranial experiments were successfully completed without dural injury. These results demonstrate that the proposed cybernetic framework enables safe and autonomous craniotomy with highly effective closed-loop control.

</details>

---

### [[20_Research/Papers/具身智能/GuidedAttention_Interpretable_and_Correctable_Visual_Attention_for_OOD-Robust_Robot_Manipulation_via_Imitation_Learning|GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning]]

![[assets/2607.21049_figure.jpg|800]]

- **arXiv**: [2607.21049](https://arxiv.org/abs/2607.21049)
- **PDF**: https://arxiv.org/pdf/2607.21049
- **详细分析**: [[20_Research/Papers/具身智能/GuidedAttention_Interpretable_and_Correctable_Visual_Attention_for_OOD-Robust_Robot_Manipulation_via_Imitation_Learning|GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning]]
- **作者**: Masaki Murooka, Ryoichi Nakajo, Keisuke Shirai, Tomohiro Motoda, Hanbit Oh, Ryo Hanai, Yukiyasu Domae
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《GuidedAttention: Interpretable and Correctable Visual Attention for OOD-Robust Robot Manipulation via Imitation Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IRL, JRL, Real-World, ResNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end visuomotor policies provide little opportunity for humans to understand or correct the policy's visual attention. We propose GuidedAttention, a visuomotor imitation learning framework that introduces interpretable and correctable visual attention as an explicit intermediate representation. Task-relevant attention keypoints are predicted from camera images and condition a diffusion-based action policy. Users can inspect and optionally correct selected keypoints once at rollout initialization, after which the corrected attention is automatically propagated throughout execution by a tracking module. Experiments in simulation and the real world demonstrate that GuidedAttention consistently improves robot manipulation performance, particularly under positional and appearance out-of-distribution (OOD) conditions.

</details>

---

### [[20_Research/Papers/具身智能/ZONDA_Zero-shot_Object_Navigation_with_Dynamic_Avoidance_in_Multi-floor_Environments|ZONDA: Zero-shot Object Navigation with Dynamic Avoidance in Multi-floor Environments]]

![[assets/2607.21025_figure.png|800]]

- **arXiv**: [2607.21025](https://arxiv.org/abs/2607.21025)
- **PDF**: https://arxiv.org/pdf/2607.21025
- **详细分析**: [[20_Research/Papers/具身智能/ZONDA_Zero-shot_Object_Navigation_with_Dynamic_Avoidance_in_Multi-floor_Environments|ZONDA: Zero-shot Object Navigation with Dynamic Avoidance in Multi-floor Environments]]
- **作者**: Shaomin Liang, Xuanhong Liao, Shiyao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《ZONDA: Zero-shot Object Navigation with Dynamic Avoidance in Multi-floor Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OVRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In Object Goal Navigation task, existing methods are typically restricted to static and single-floor environments, ignoring cross-floor topologies and dynamic pedestrian, which limits their real-world deployment. To address these limitations, we propose ZONDA, a zero-shot object navigation with dynamic avoidance framework. In particular, ZONDA integrates three core components: (i) Heuristic multi-floor planning: from height-difference traversable maps, enables stair traversal and cross-floor exploration without a platform-specific learned controller; (ii) Multi-view target verification: cross-checks multi-scale observations with a vision-language model, significantly reducing false positives; and (iii) Dynamic pedestrian avoidance: explicitly tracks and predicts moving pedestrians to generate anticipatory behaviors. Evaluated on a real Direct Drive Tech TITA biped robot and extensive simulations on HM3D and MP3D, ZONDA achieves significantly improved results. Moreover, ZONDA can maintain robust navigation on the dynamic benchmark HM3D-DYNA compared to the existing baseline.

</details>

---

### [[20_Research/Papers/具身智能/TableVerse_A_Large-scale_Tabletop_Dataset_with_Real-world_Grounded_Layouts_for_Generalizable_Manipulation|TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation]]

![[assets/2607.21017_figure.png|800]]

- **arXiv**: [2607.21017](https://arxiv.org/abs/2607.21017)
- **PDF**: https://arxiv.org/pdf/2607.21017
- **详细分析**: [[20_Research/Papers/具身智能/TableVerse_A_Large-scale_Tabletop_Dataset_with_Real-world_Grounded_Layouts_for_Generalizable_Manipulation|TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation]]
- **作者**: Boyuan Wang, Yue Zhang, Xutao Xue, Xueyu Song, Yu Sun
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《TableVerse: A Large-scale Tabletop Dataset with Real-world Grounded Layouts for Generalizable Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The development of generalizable robotic manipulation policies is inherently bounded by the availability of large-scale, high-fidelity scene data. While recent automated synthesis methods attempt to bridge this gap via text-to-layout hallucination or simplified procedural generation, they frequently suffer from physical implausibility and fail to capture the complex, dense clutter of actual human environments. In this paper, we introduce TableVerse, a fully automated Real2Sim pipeline that shifts the paradigm from imaginative layout generation to deterministic reconstruction from unstructured, in-the-wild image data. Our framework seamlessly processes unscripted internet media into high-fidelity, simulation-ready tabletop environments with accurate metric scales, authentic topologies, and verified mechanical stability. Furthermore, an automated task-conditioned trajectory generation framework is integrated to synthesize high-quality, collision-free pick-and-place demonstrations. Leveraging this complete pipeline, we construct the TableVerse-100K Dataset, a large-scale corpus comprising 100,000 unique, physically consistent environments paired with interactive manipulation trajectories. By capturing diverse asset compositions, realistic spatial distributions, and high-quality demonstrations, TableVerse-100K establishes a highly scalable and high-fidelity data foundation, providing significant value to facilitate future research in generalizable robotic manipulation tasks.

</details>

---

### [[20_Research/Papers/机器人/Distributed_Model-Based_Diffusion_For_Scalable_Multi-Robot_Trajectory_Optimization|Distributed Model-Based Diffusion For Scalable Multi-Robot Trajectory Optimization]]

![[assets/2607.20992_figure.png|800]]

- **arXiv**: [2607.20992](https://arxiv.org/abs/2607.20992)
- **PDF**: https://arxiv.org/pdf/2607.20992
- **详细分析**: [[20_Research/Papers/机器人/Distributed_Model-Based_Diffusion_For_Scalable_Multi-Robot_Trajectory_Optimization|Distributed Model-Based Diffusion For Scalable Multi-Robot Trajectory Optimization]]
- **作者**: Haejoon Lee, Xinyi Wang, Taekyung Kim, Dimitra Panagou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Distributed Model-Based Diffusion For Scalable Multi-Robot Trajectory Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Trajectory optimization for multi-robot systems remains a critical challenge, particularly when navigating highly non-convex, non-linear, and non-differentiable environments. While Model-Based Diffusion (MBD) has recently emerged as a promising sampling-based optimization paradigm for single-robot trajectory generation, extending it to multi-robot systems results in a centralized, high-dimensional inference problem that (i) suffers from poor sample efficiency due to the curse of dimensionality and (ii) requires global access to all robots' dynamics, constraints, and objectives. To address this, we propose Distributed Model-Based Diffusion (DMBD), a distributed server-robot framework that decomposes the reverse diffusion process into local conditional reverse diffusion processes. This decomposition enables each robot to iteratively perform denoising independently within its own control subspace while conditioning on the current trajectory estimates of the other robots that are aggregated and broadcast by the server. Extensive simulations in goal swapping, multi-floor coverage, parking, and rush-hour scenarios demonstrate that DMBD achieves strong scalability, solving many challenging coordination tasks in sub-seconds and significantly outperforming existing baselines.

</details>

---

### [[20_Research/Papers/大模型/URF_A_Unified_Robot_Control-Policy_Framework_for_Stable_Contact_Aware_Manipulation|URF: A Unified Robot Control-Policy Framework for Stable Contact Aware Manipulation]]

![[assets/2607.20912_figure.png|800]]

- **arXiv**: [2607.20912](https://arxiv.org/abs/2607.20912)
- **PDF**: https://arxiv.org/pdf/2607.20912
- **详细分析**: [[20_Research/Papers/大模型/URF_A_Unified_Robot_Control-Policy_Framework_for_Stable_Contact_Aware_Manipulation|URF: A Unified Robot Control-Policy Framework for Stable Contact Aware Manipulation]]
- **作者**: Jiyou Shin, Youngjin Seo, Jaeseog Won, Sungwon Seo, Hyunjun Kim, Seokmin Yoon, Tuan Luong, Hyungpil Moon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《URF: A Unified Robot Control-Policy Framework for Stable Contact Aware Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-based manipulation policies usually predict robot actions from sensory observations and leave their execution to a separate low-level controller. In rigid contact, this separation can be problematic: the same motion to a virtual target or compliant motion command can lead to unstable contact, tracking error, excessive loading, or tool damage, depending on the low-level controller. In this paper, we propose a \textit{Unified Robot Control-Policy Framework} (URF), which connects compliant action prediction with unified impedance-admittance control. Given multimodal observations, URF predicts a virtual target, a stiffness matrix, and an impedance-admittance switch ratio. The switch ratio determines when the controller should behave more like admittance control for accurate motion tracking and when it should move toward impedance control for safer rigid contact. Because demonstration data do not provide ground-truth environment stiffness, we construct switch-ratio labels from measured contact forces and use them to supervise controller-mode prediction. Across box-flipping and line-pressing tasks, URF achieves higher task success rates while reducing failure modes observed with admittance-only execution, including rapid force buildup, large force oscillations, tool breakage, and robot safety stops. These results suggest that contact-aware policies benefit from predicting not only compliant actions but also the controller behavior used to execute them. Project page: https://jiyou384.github.io/urf_project_page/

</details>

---

### [[20_Research/Papers/具身智能/Socially_Consistent_Multi-Robot_Navigation_Using_Decoupled_Planning_and_Trajectory_Coordination|Socially Consistent Multi-Robot Navigation Using Decoupled Planning and Trajectory Coordination]]

![[assets/2607.20772_first_page.png|800]]

- **arXiv**: [2607.20772](https://arxiv.org/abs/2607.20772)
- **PDF**: https://arxiv.org/pdf/2607.20772
- **详细分析**: [[20_Research/Papers/具身智能/Socially_Consistent_Multi-Robot_Navigation_Using_Decoupled_Planning_and_Trajectory_Coordination|Socially Consistent Multi-Robot Navigation Using Decoupled Planning and Trajectory Coordination]]
- **作者**: Matthew M. Sato, Kincho H. Law
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.5（加权：具身智能 1.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Socially Consistent Multi-Robot Navigation Using Decoupled Planning and Trajectory Coordination》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The successful integration of mobile robots in human-centric environments requires navigation that is not only safe and efficient, but also predictable and aligned with social conventions, key precursors for human comfort and acceptance. While significant research addresses short-term human-aware planning, these methods often lack mechanisms for ensuring consistent and predictable behaviors across long horizons. Without socially aware long-term planners, local planners are overburdened, resulting in inefficient and locally reactive movements that undermine predictability. This paper introduces a partially decentralized framework that generates predictable and socially consistent multi-robot motion by decoupling global path planning from trajectory coordination. First, we propose a modified A* planner that embeds macroscopic social norms into the planner cost function. Planned paths are shared across mobile robots to collaboratively build a social graph of established routes, which enforces path consistency and reduces future planning effort. Second, we leverage the emergent structure of the socially constrained paths to formulate the multi-robot trajectory coordination problem as a mixed-integer convex program. The convex program enables efficient computation of conflict- free trajectories, scaling effectively to large fleets and supporting dynamic task assignment. Our results demonstrate that enforcing social consistency at the path planning stage produces predictable, socially compliant mobile robot paths and simplifies the otherwise complex problem of multi-robot coordination.

</details>

---

### [[20_Research/Papers/机器人/Decentralized_UAV_Swarms_for_Ground_Target_Protection_in_GPS-_and_Communication-Denied_Environments|Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments]]

![[assets/2607.20710_figure.png|800]]

- **arXiv**: [2607.20710](https://arxiv.org/abs/2607.20710)
- **PDF**: https://arxiv.org/pdf/2607.20710
- **详细分析**: [[20_Research/Papers/机器人/Decentralized_UAV_Swarms_for_Ground_Target_Protection_in_GPS-_and_Communication-Denied_Environments|Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments]]
- **作者**: Dimitria Silveria, Paulo Ricardo Marques de Araujo, Tiago Nascimento, Sidney Givigi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Decentralized UAV Swarms for Ground Target Protection in GPS- and Communication-Denied Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The presence of UAVs in military operations has recently increased, also increasing the demand for defense systems against UAV attacks. UAVs can also be used as countermeasures. Most available methods rely on UAV-to-UAV communication and global positioning. However, such resources may not be available in modern warfare scenarios. To address these limitations, we propose a pipeline for ground-target protection against UAV attacks that employs autonomous swarms of UAVs. We assume a communication- and GPS-denied environment in which the UAVs use onboard sensors to track the target and coordinate as a swarm. We developed Kalman filters to estimate the states of unknown targets and the positions of UAVs in the swarm using only relative measurements. Also, our strategy is to encircle the target of interest to maximize coverage. To achieve that, we propose a decentralized swarm encirclement technique that adapts to the target's motion. Our approach was extensively validated using real robots, demonstrating its effectiveness in detecting, encircling, and intercepting hostile UAVs.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Capability-Aware_Traversability_Navigation_for_Unstructured_Environments|Towards Capability-Aware Traversability Navigation for Unstructured Environments]]

![[assets/2607.20679_figure.png|800]]

- **arXiv**: [2607.20679](https://arxiv.org/abs/2607.20679)
- **PDF**: https://arxiv.org/pdf/2607.20679
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Capability-Aware_Traversability_Navigation_for_Unstructured_Environments|Towards Capability-Aware Traversability Navigation for Unstructured Environments]]
- **作者**: Gianluca Capezzuto, Felipe Tommaselli, Matheus P. Angarola, Ricardo V. Godoy, Marcelo Becker
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Towards Capability-Aware Traversability Navigation for Unstructured Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Estimating traversability in unstructured environments requires conditioning on robot embodiment, as the same terrain can be traversable for one platform and unsafe for another. Existing methods often transfer predictions across morphologies through late-stage trajectory filtering rather than encoding platform constraints in the learned representation. We propose Capability-Aware Traversability (CAT), a framework that embeds physical limits directly into the spatial feature space. CAT grounds dense supervision masks in physical trajectories through an interactive annotation pipeline and modulates semantic terrain maps with robot-specific traversability vectors through Spatially-Adaptive Denormalization (SPADE) blocks. Across human-annotated and trajectory-aligned datasets, CAT leads all ranking-based metrics, improving AUROC by 11.0% on physically executed trajectories and AUPRC by 15.8% on human traces over the strongest baseline. Ablations show that spatial conditioning and per-robot prototypes produce capability sensitivity beyond generic path prediction. Deployments on a legged quadruped and a wheeled skid-steer demonstrate embodiment-aware obstacle avoidance on embedded hardware at 4.8 Hz.

</details>

---

### [[20_Research/Papers/强化学习/Safe_and_Scalable_Multi-Drone_Payload_Transport_via_CBF-based_Reinforcement_Learning_with_Zero-Shot_Sim-to-Real_Transfer|Safe and Scalable Multi-Drone Payload Transport via CBF-based Reinforcement Learning with Zero-Shot Sim-to-Real Transfer]]

![[assets/2607.20665_figure.png|800]]

- **arXiv**: [2607.20665](https://arxiv.org/abs/2607.20665)
- **PDF**: https://arxiv.org/pdf/2607.20665
- **详细分析**: [[20_Research/Papers/强化学习/Safe_and_Scalable_Multi-Drone_Payload_Transport_via_CBF-based_Reinforcement_Learning_with_Zero-Shot_Sim-to-Real_Transfer|Safe and Scalable Multi-Drone Payload Transport via CBF-based Reinforcement Learning with Zero-Shot Sim-to-Real Transfer]]
- **作者**: Jaeyoun Choi, Oswin So, Songyuan Zhang, Cooper Taylor, Chuchu Fan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.4（加权：具身智能 1.5，强化学习 0.8，机器人 1.1）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Safe and Scalable Multi-Drone Payload Transport via CBF-based Reinforcement Learning with Zero-Shot Sim-to-Real Transfer》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-drone payload transportation has emerged as a promising research paradigm with potential applications in construction, logistics, and disaster response. However, the complex coupled dynamics among drones, cables, and payloads pose significant challenges, and existing approaches remain limited in safety and scalability, particularly in dynamic and unstructured environments. In this work, we propose a learning-based framework for safe and scalable multi-drone cooperative payload transport. We introduce a minimal 2D abstraction that preserves the task-relevant drone-payload coupling required for coordination and safety, while remaining computationally efficient for large-scale learning. Using domain randomization over team size and physical parameters, we train a fully distributed policy via Discrete Graph Control Barrier Function Proximal Policy Optimization (DGPPO), enabling robust zero-shot sim-to-real transfer without fine-tuning. Extensive real-world evaluations demonstrate that a single learned policy generalizes across varying team sizes and task scenarios. Furthermore, multi-group hardware experiments show that the same policy can safely operate in dynamic environments, where other drone teams act as moving obstacles. These results indicate that the proposed framework enables efficient, safe, and scalable multi-drone payload transportation with strong generalization to complex real-world conditions.

</details>

---

### [[20_Research/Papers/机器人/Scalable_Low-Cost_Laboratory_Automation_A_Digital_Twin-Integrated_Robotic_Platform_for_Autonomous_Liquid_Handling_(RAINBOTTM)|Scalable Low-Cost Laboratory Automation: A Digital Twin-Integrated Robotic Platform for Autonomous Liquid Handling (RAINBOTTM)]]

![[assets/2607.20662_figure.jpg|800]]

- **arXiv**: [2607.20662](https://arxiv.org/abs/2607.20662)
- **PDF**: https://arxiv.org/pdf/2607.20662
- **详细分析**: [[20_Research/Papers/机器人/Scalable_Low-Cost_Laboratory_Automation_A_Digital_Twin-Integrated_Robotic_Platform_for_Autonomous_Liquid_Handling_(RAINBOTTM)|Scalable Low-Cost Laboratory Automation: A Digital Twin-Integrated Robotic Platform for Autonomous Liquid Handling (RAINBOTTM)]]
- **作者**: Mohamed Rami Ayeche, Souhil Sid, Ahyen Mostofa, Rehaan Hussain, Ali Shayesteh, Fadwa El Mellouhi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Scalable Low-Cost Laboratory Automation: A Digital Twin-Integrated Robotic Platform for Autonomous Liquid Handling (RAINBOTTM)》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Laboratory automation accelerates discovery, yet its adoption is constrained by the high cost, proprietary design, and limited remote supervisability of commercial liquid-handling systems. This work presents RAINBOT\textsuperscript{TM}, a low-cost, openly reproducible liquid-handling robot built by converting a consumer-grade Cartesian 3D printer (Elegoo Neptune 4 Max). The printer extruder is replaced by a precision single-channel pipette actuated through the printer's own G-code-driven X--Y--Z gantry, with plunger and tip-eject motions effected by two compact linear actuators under Python control. To make experiments transparent and remotely supervisable, a browser-based digital twin is implemented to synchronise bidirectionally with the physical platform, mirroring kinematics and pipetting states in real time and exposing remote monitoring, intervention, and an emergency stop from any web browser. As a proof of concept, RAINBOT\textsuperscript{TM} performed sequential exchanges of differently coloured aqueous solutions while an integrated colour sensor quantified the resulting mixtures; measured red, yellow, and blue (RYB) responses agreed with expected mixing behaviour to within a mean absolute error of two percentage points, validating correct execution and real-time tracking. Closing the loop, the platform is coupled to the CEID\textsuperscript{TM} (Cooperative Explorer for Inverse Design) framework, which recasts experimentation from iterative manual guessing into a goal-directed inverse-design search while keeping a human in the loop. The complete hardware costs under US\$1300, which is roughly an order of magnitude below entry-level commercial handlers, thereby establishing an accessible physical--virtual framework for self-driving laboratory automation.

</details>

---
