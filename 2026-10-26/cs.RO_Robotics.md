# cs.RO | Robotics | 2026-10-26

#arxiv #ComputerScience

**论文数**: 32

### [[20_Research/Papers/具身智能/RynnUnify_Towards_Unified_Embodied_Brain|RynnUnify: Towards Unified Embodied Brain]]

![[assets/2610.32965_figure.png|800]]

- **arXiv**: [2610.32965](https://arxiv.org/abs/2610.32965)
- **PDF**: https://arxiv.org/pdf/2610.32965
- **详细分析**: [[20_Research/Papers/具身智能/RynnUnify_Towards_Unified_Embodied_Brain|RynnUnify: Towards Unified Embodied Brain]]
- **作者**: Minghao Zhu, Bohan Hou, Kun Xiang, Zixuan Wang, Yinzhou Tang, Yifei Yang, Zhikai Wang, Tianyi Zhang, Kehan Li, Haoyu Zhao, Siteng Huang, Leigang Qu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RynnUnify: Towards Unified Embodied Brain》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce RynnUnify, a 16B unified embodied model that combines strong embodied understanding with long-horizon visual planning through interleaved video--language reasoning. With capabilities spanning spatial reasoning, physical prediction, and grounding, RynnUnify connects an understanding of the physical world with visual anticipation of how it evolves across successive subtasks. Building on these capabilities, we further develop an agentic extension through reinforcement learning to selectively use video predictions for reasoning about unobserved states and interaction outcomes. We also develop a world-action extension of the full RynnUnify model, translating its understanding and prediction capabilities into robot control. To evaluate these capabilities, we introduce Rynn-VP and Rynn-GEU for long-horizon visual planning and anticipatory reasoning. Experiments show that RynnUnify achieves the highest average embodied understanding score among the evaluated unified multimodal models and improves the Rynn-VP overall score by 9.75 points over Cosmos 3 Nano. Its agentic extension improves the Rynn-GEU average by 6.0 points over direct reasoning, while the world-action extension achieves 51.5\% success on 20 selected composite RoboCasa365 tasks and 46.7\% average success across three real-robot tasks. Together, these results establish RynnUnify as a shared foundation for embodied understanding, visual planning, and robot control, taking a step toward a unified embodied brain.

</details>

---

### [[20_Research/Papers/机器人/Robotic_Optical_Coherence_Tomography-Guided_Geometric_Modeling_of_Soft_Tissue_3D_Representations_for_Data-Driven_Closed-Loop_Shape_Control|Robotic Optical Coherence Tomography-Guided Geometric Modeling of Soft Tissue: 3D Representations for Data-Driven Closed-Loop Shape Control]]

![[assets/2610.32961_figure.jpg|800]]

- **arXiv**: [2610.32961](https://arxiv.org/abs/2610.32961)
- **PDF**: https://arxiv.org/pdf/2610.32961
- **详细分析**: [[20_Research/Papers/机器人/Robotic_Optical_Coherence_Tomography-Guided_Geometric_Modeling_of_Soft_Tissue_3D_Representations_for_Data-Driven_Closed-Loop_Shape_Control|Robotic Optical Coherence Tomography-Guided Geometric Modeling of Soft Tissue: 3D Representations for Data-Driven Closed-Loop Shape Control]]
- **作者**: Chaoyu Zhang, Guangshen Ma, Mark Draelos
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Robotic Optical Coherence Tomography-Guided Geometric Modeling of Soft Tissue: 3D Representations for Data-Driven Closed-Loop Shape Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：C2P-Net, DefGoalNet, DeformerNet, OCT-DeformNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In medical robotics, data-driven soft-tissue shape control requires deforming tissue toward desired morphologies through sequential physical interactions. This challenge is particularly important in microscale manipulation, where localized deformation is difficult to observe, represent, and control, while physics-based models can be computationally expensive and difficult to adapt to realistic environments. Optical coherence tomography (OCT) provides high-resolution volumetric perception of tissue deformation, but target-conditioned control requires effective representations of both observed and desired tissue states. In this work, we introduce an OCT-guided data-driven framework for tissue shape control, learned from user-guided demonstrations and executed with closed-loop OCT feedback. We study full-volume, tissue-masked sparse-volume, and voxelized point-cloud representations, with or without residual conditioning, using deterministic (Explicit) and generative diffusion (Diffusion) policies. Across 12 configurations and 576 phantom rollouts on 3-DoF depth and 6-DoF directional tasks, OCT-derived 3D representations support both Explicit and Diffusion policies, with performance depending on representation and residual conditioning. Residual conditioning reduces directional Shape RMSE from 0.748 to 0.555 mm for full-volume Diffusion, while voxelized point-cloud Explicit with residuals achieves 0.534 mm for depth and 0.443 mm for directional control, with comparable accuracy at intermediate unseen targets and consistent performance across deployments. We further evaluate the framework in 60 ex vivo porcine rollouts, extending to biological tissue with final geometric errors comparable to human demonstrations. These results establish volumetric OCT as current and goal representations for learned closed-loop tissue shape control across deterministic and generative action models.

</details>

---

### [[20_Research/Papers/强化学习/HoloBoxing_A_Simple_Recipe_for_Humanoid_Boxing_with_7_Minutes_of_Single-GPU_Training|HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training]]

![[assets/2610.32909_figure.png|800]]

- **arXiv**: [2610.32909](https://arxiv.org/abs/2610.32909)
- **PDF**: https://arxiv.org/pdf/2610.32909
- **详细分析**: [[20_Research/Papers/强化学习/HoloBoxing_A_Simple_Recipe_for_Humanoid_Boxing_with_7_Minutes_of_Single-GPU_Training|HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training]]
- **作者**: Xihan Ma, Bo Zhang, Boxiong Li, Yuhan Bao, Ziyue Liu, Yucheng Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《HoloBoxing: A Simple Recipe for Humanoid Boxing with 7 Minutes of Single-GPU Training》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

HoloBoxing presents a simple recipe for learning humanoid boxing by building on a pretrained whole-body controller. The recipe separates reusable motor skills from task decisions: a compact planner requests future body-point targets, while the frozen controller handles joint-level execution. A learned decoder maps 32-dimensional actions to structured target windows, and measured-state imitation initializes the planner before reinforcement learning. Task learning then refines interaction behavior while reusing the decoder and controller, avoiding the need to relearn whole-body control. This combination keeps task optimization focused on a compact upper policy and supplies an initial behavior before reward-driven exploration. Starting from that available controller, the recipe accounts for about seven minutes of additional training, including reused representation fitting and a single-GPU task run. This excludes controller pretraining, data preparation, evaluation, and search. Simulated boxing experiments and component controls evaluate the resulting behavior and the roles of imitation initialization and the target representation.

</details>

---

### [[20_Research/Papers/具身智能/Predictive_Long-Horizon_Progress_Modeling_with_Action-Aware_Quantification|Predictive Long-Horizon Progress Modeling with Action-Aware Quantification]]

![[assets/2610.32776_figure.png|800]]

- **arXiv**: [2610.32776](https://arxiv.org/abs/2610.32776)
- **PDF**: https://arxiv.org/pdf/2610.32776
- **详细分析**: [[20_Research/Papers/具身智能/Predictive_Long-Horizon_Progress_Modeling_with_Action-Aware_Quantification|Predictive Long-Horizon Progress Modeling with Action-Aware Quantification]]
- **作者**: Tianchi Xu, Yalin Zheng, Yangxin Zhu, Ruonan Ren, Zheng Fu, Yunlong Wang, Yuanxin Zhong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Predictive Long-Horizon Progress Modeling with Action-Aware Quantification》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantitative and dense task progress feedback is essential for robotic manipulation across data curation, policy evaluation, and reinforcement learning. Existing progress annotations often rely on sparse keyframe markings derived from subjective manual judgments, limiting their scalability and cross-task consistency, particularly in long-horizon manipulation. To overcome these challenges, we propose action-aware quantification, a unified progress specification that decomposes long-horizon trajectories into object-level subtasks via a vision-language model (VLM) and assigns weighted action credits to capture fine-grained execution dynamics. Using VLM auto-labeling and human calibration, we construct an 800+ hour training video dataset and LOOM, a long-horizon progress benchmark containing 19,618 human-calibrated evaluation frames. To model these dense progress dynamics, we introduce NimCritic, a predictive progress critic trained via Joint Video-Progress Learning. We further incorporate Historical Progress Perturbation to mitigate sequential drift, and design a contrastive Video-Progress Alignment objective that bridges asymmetric expert streams by mutually grounding intermediate visual dynamics and denoised progress trajectories. NimCritic matches or outperforms state-of-the-art process reward models (PRMs) on the established Video Progress Benchmark (VPB) and LOOM, surpassing GVL (GPT-6-Sol) on VPB by about 65% in terminal success accuracy (TSA). On the large-scale RoboArena policy evaluation benchmark, it also retrieves human-selected successful rollouts with about 97% overall recall. These results establish action-aware quantification as a scalable foundation for dense progress feedback in robotic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Monte_Carlo-Based_Indoor_UAV_Localization_in_Dynamic_Environments_Using_Only_Four_Onboard_Range_Sensors|Monte Carlo-Based Indoor UAV Localization in Dynamic Environments Using Only Four Onboard Range Sensors]]

![[assets/2610.32645_figure.png|800]]

- **arXiv**: [2610.32645](https://arxiv.org/abs/2610.32645)
- **PDF**: https://arxiv.org/pdf/2610.32645
- **详细分析**: [[20_Research/Papers/机器人/Monte_Carlo-Based_Indoor_UAV_Localization_in_Dynamic_Environments_Using_Only_Four_Onboard_Range_Sensors|Monte Carlo-Based Indoor UAV Localization in Dynamic Environments Using Only Four Onboard Range Sensors]]
- **作者**: Mohammad Reza Ranjbar Divkoti, A. Pedro Aguiar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Monte Carlo-Based Indoor UAV Localization in Dynamic Environments Using Only Four Onboard Range Sensors》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Indoor UAV localization with minimal onboard sensing remains challenging, particularly in dynamic environments. We propose augmented filtered Monte Carlo localization (AF-MCL) for 2D localization using only four single-point range sensors and measured heading. AF-MCL rejects range measurements inconsistent with the known static map and adaptively injects particles to recover from localization divergence and kidnapping. Beam classification is performed only at the previous position estimate, making its ray-casting cost independent of the particle count. The particle distribution additionally provides an online measure of localization uncertainty. Real-world experiments in a 2.10x1.63 m environment yield mean position errors of 6.4-7.7 cm under static and dynamic conditions. Simulations in 6x6 m and 10x10 m environments yield 4.5-5.2 cm mean errors; under dynamic obstacles, standard MCL reaches 12.3 cm and reliable MCL 7.7 cm. The results show that robust indoor localization under dynamic obstacles is achievable with only four single-point range measurements and heading.

</details>

---

### [[20_Research/Papers/具身智能/Natural-Language_to_Nav2_Operational_Policies_for_Costmap-Based_Navigation|Natural-Language to Nav2: Operational Policies for Costmap-Based Navigation]]

![[assets/2610.32633_figure.png|800]]

- **arXiv**: [2610.32633](https://arxiv.org/abs/2610.32633)
- **PDF**: https://arxiv.org/pdf/2610.32633
- **详细分析**: [[20_Research/Papers/具身智能/Natural-Language_to_Nav2_Operational_Policies_for_Costmap-Based_Navigation|Natural-Language to Nav2: Operational Policies for Costmap-Based Navigation]]
- **作者**: Jiyeong Chae, Hyunkyo Seo, Heonjae Lee, Kyung-Joon Park
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.2，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Natural-Language to Nav2: Operational Policies for Costmap-Based Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous mobile robots support material transport in warehouses and industrial facilities, where navigation must adapt to changing operating conditions. Sensor observations reveal physical obstacles, but do not by themselves specify temporary access rules, route preferences, or exceptions known to operators. This paper presents a natural-language policy interface that brings this knowledge into ROS 2 Nav2. A local large language model converts instructions into JSON policies specifying destinations, spatial constraints, and temporal or event conditions. Deterministic checks govern mission acceptance, and three costmap adapters project accepted policies into the existing navigation stack without changing its planner or controller. On 150 researcher-authored English commands, four local models produce 107-142 correct accepted policies, compared with 44 for a rule-based parser, with 3-20 incorrect acceptances per model. Fault injection records rejection of eight endpoint/JSON faults and 29 validator-stage faults. Navigation experiments use correct task policies to evaluate keepouts, zone costs, person-dependent regions, and event-conditioned passage in simulation and on a TurtleBot3. For Tasks 1-3, mean travel times are 18.4-24.5% lower in simulation and 23.1-35.0% lower on the physical testbed than with the baseline lacking those policies. A native KeepoutFilter comparison and two-robot demonstrations examine basic keepout behavior and shared policy projection. The interface connects operator instructions to explicit navigation policies while retaining Nav2's planning and control components.

</details>

---

### [[20_Research/Papers/大模型/UAV-SwarmAgent_Scalable_Multi-UAV_Reconnaissance_and_Task_Allocation_via_Code_Generation_and_Vision-Language_Reasoning|UAV-SwarmAgent: Scalable Multi-UAV Reconnaissance and Task Allocation via Code Generation and Vision-Language Reasoning]]

![[assets/2610.32559_figure.png|800]]

- **arXiv**: [2610.32559](https://arxiv.org/abs/2610.32559)
- **PDF**: https://arxiv.org/pdf/2610.32559
- **详细分析**: [[20_Research/Papers/大模型/UAV-SwarmAgent_Scalable_Multi-UAV_Reconnaissance_and_Task_Allocation_via_Code_Generation_and_Vision-Language_Reasoning|UAV-SwarmAgent: Scalable Multi-UAV Reconnaissance and Task Allocation via Code Generation and Vision-Language Reasoning]]
- **作者**: Oleg Sautenkov, Yasheerah Yaqoot, Muhammad Ahsan Mustafa, Grigorii Kalinin, Chih-Yung Wen, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《UAV-SwarmAgent: Scalable Multi-UAV Reconnaissance and Task Allocation via Code Generation and Vision-Language Reasoning》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：UAV-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Supervising a multi-UAV reconnaissance mission usually means plotting waypoints and watching every drone. We present UAV SwarmAgent, a hierarchical multi-agent system in which an operator states the mission in one natural-language sentence and a ground-station agent writes and executes code that turns it into per-UAV routes. The agent grounds inspection targets in an aerial map with a vision-language model, splits them among N UAVs by balancing route length, and dispatches worker agents that verify incidents with a compact onboard decision model. In simulation over 4 incident types and 3 foundation models, the swarm located the incident in 244 of 255 missions (95.7%). A paired scaling study with one to 5 UAVs shows that flight time follows an Amdahl-type law. The second UAV delivers half of the attainable saving and the speedup is bounded at 1.52x. We discuss what this predictability, and the false alarms we observed, imply for an operator who supervises the swarm, and outline the user study needed to test it.

</details>

---

### [[20_Research/Papers/具身智能/HGWM_Hierarchical_Graph-Guided_World_Model_for_Zero-Shot_Object_Navigation_via_Graph_Matching|HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching]]

![[assets/2610.32554_figure.jpg|800]]

- **arXiv**: [2610.32554](https://arxiv.org/abs/2610.32554)
- **PDF**: https://arxiv.org/pdf/2610.32554
- **详细分析**: [[20_Research/Papers/具身智能/HGWM_Hierarchical_Graph-Guided_World_Model_for_Zero-Shot_Object_Navigation_via_Graph_Matching|HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching]]
- **作者**: I-tak Ieong, Hao Tang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.8，大模型 0.2，世界模型 0.6，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《HGWM: Hierarchical Graph-Guided World Model for Zero-Shot Object Navigation via Graph Matching》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OVRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-shot object navigation requires an embodied agent to choose where to search while retaining evidence from previous observations. HGWM couples an LLM-generated room-anchor prior with persistent spatial-semantic memory. A coarse stage assigns visual-semantic scores to candidate headings on a 0-10 scale; a fine stage measures symbolic compatibility between observed objects, room context, and the goal prior. Phase-dependent fusion combines these scores with an LLM direction recommendation before local action selection. On HM3D v0.1, the reported HGWM configuration achieves 62.6% success rate (SR) and 31.5% success weighted by path length (SPL), compared with 58.1% and 31.2% for WMNav. On MP3D, the corresponding values are 46.8% and 17.9%, compared with 45.4% and 17.2%. The results indicate higher success point estimates and modest path-efficiency gains. On HM3D v0.2, the full model obtains 74.4% SR and 31.9% SPL. Additional component ablations reduce SR by 0.9-2.3 percentage points and SPL by 0.6-1.5 points. These are author-reported aggregate measurements. The accompanying implementation repairs pass offline tests; episode-level rerun records are not available. Evaluation is confined to simulation.

</details>

---

### [[20_Research/Papers/强化学习/Optimization,_Optimal_Control,_and_Reinforcement_Learning_for_Robotics|Optimization, Optimal Control, and Reinforcement Learning for Robotics]]

![[assets/2610.32538_first_page.png|800]]

- **arXiv**: [2610.32538](https://arxiv.org/abs/2610.32538)
- **PDF**: https://arxiv.org/pdf/2610.32538
- **详细分析**: [[20_Research/Papers/强化学习/Optimization,_Optimal_Control,_and_Reinforcement_Learning_for_Robotics|Optimization, Optimal Control, and Reinforcement Learning for Robotics]]
- **作者**: Yonghyeon Lee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Optimization, Optimal Control, and Reinforcement Learning for Robotics》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

These lecture notes provide an introduction to optimization, optimal control, and reinforcement learning for robotics, emphasizing their mathematical connections and practical relevance. They present established material compiled and edited by Yonghyeon Lee, rather than new research results. The notes were developed through a human and AI collaborative writing process, with AI assistance in drafting, organizing, and refining the exposition. This first version is a preliminary collection of notes, not yet a fully developed textbook, and currently contains no figures or graphs. The notes may be revised, corrected, and expanded in future versions.

</details>

---

### [[20_Research/Papers/机器人/Facultative_Swarming_A_Capability,_Not_a_Category,_for_Multi-Robot_Systems|Facultative Swarming: A Capability, Not a Category, for Multi-Robot Systems]]

![[assets/2610.32526_figure.png|800]]

- **arXiv**: [2610.32526](https://arxiv.org/abs/2610.32526)
- **PDF**: https://arxiv.org/pdf/2610.32526
- **详细分析**: [[20_Research/Papers/机器人/Facultative_Swarming_A_Capability,_Not_a_Category,_for_Multi-Robot_Systems|Facultative Swarming: A Capability, Not a Category, for Multi-Robot Systems]]
- **作者**: Ning Zhou, Edmund R. Hunt
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Facultative Swarming: A Capability, Not a Category, for Multi-Robot Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collective robotics is split by a long-standing but increasingly artificial boundary between centralised multi-robot systems that prioritise optimality and decentralised swarms that prioritise robustness and adaptivity. We propose a unified control framework, shifting from `obligate' swarms---systems constrained to pure self-organisation---to facultatively swarming systems: hybrid architectures that operate as centrally planned systems under permissive conditions yet degrade gracefully into decentralised swarming under environmental stress. By reframing swarming as a dynamic capability, rather than a rigid system category, we outline a pathway towards collective robotic systems that benefit from centralised optimality when conditions permit and from the flexibility of self-organisation when they do not.

</details>

---

### [[20_Research/Papers/具身智能/From_Freehand_Demonstrations_to_Autonomous_Robotic_Ultrasound_An_Anatomy-Anchored_Learning_Framework|From Freehand Demonstrations to Autonomous Robotic Ultrasound: An Anatomy-Anchored Learning Framework]]

![[assets/2610.32525_figure.png|800]]

- **arXiv**: [2610.32525](https://arxiv.org/abs/2610.32525)
- **PDF**: https://arxiv.org/pdf/2610.32525
- **详细分析**: [[20_Research/Papers/具身智能/From_Freehand_Demonstrations_to_Autonomous_Robotic_Ultrasound_An_Anatomy-Anchored_Learning_Framework|From Freehand Demonstrations to Autonomous Robotic Ultrasound: An Anatomy-Anchored Learning Framework]]
- **作者**: Yuan Bi, Fangxu Han, Ye Su, Yiping Zhou, Zhongliang Jiang, Nassir Navab
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《From Freehand Demonstrations to Autonomous Robotic Ultrasound: An Anatomy-Anchored Learning Framework》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ultrasound imaging is highly operator-dependent, motivating robotic systems that reproduce expert scanning skills consistently. These skills involve coordinated interpretation of anatomical landmarks, ultrasound images, and probe-tissue interactions that are difficult to encode in hand-designed control strategies. Imitation learning offers an alternative, but its observation and action representations should reflect the anatomically structured nature of scanning. We propose an anatomy-anchored imitation-learning framework that combines anatomy-guided probe placement with learned ultrasound navigation. The placement module identifies a task-specific anatomical starting point from external visual observations and establishes the initial probe pose as the reference frame for scanning. A flow-based policy then generates scanning motions from anchor-relative probe poses, ultrasound images, probe-mounted camera views, and contact forces, while a termination head predicts task completion. This avoids continuous reliance on third-person vision and reduces dependence on the robot-patient configuration. A handheld acquisition platform enables multimodal demonstrations to be collected during natural freehand scanning without a robot. On 16 unseen participants, task success reaches 96%, 94%, 88%, and 94% for kidney, gallbladder, and liver standard-plane acquisition and radial artery sweeping, respectively. Compared with a fine-tuned pi_0 model, success on the abdominal tasks improves by 10-42 percentage points, with lower time-to-target, peak contact force, and trajectory jerk. Ablations support the complementary roles of anatomical anchoring, egocentric vision, and force feedback. End-to-end trials with automatic placement achieve 90-100% success, and the policies transfer without retraining to a second robot with 83-100% success.

</details>

---

### [[20_Research/Papers/机器人/CoCarry_Contact-Support-Structured_Retargeting_for_Dual-Humanoid_Cooperative_Carrying|CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying]]

![[assets/2610.32460_figure.png|800]]

- **arXiv**: [2610.32460](https://arxiv.org/abs/2610.32460)
- **PDF**: https://arxiv.org/pdf/2610.32460
- **详细分析**: [[20_Research/Papers/机器人/CoCarry_Contact-Support-Structured_Retargeting_for_Dual-Humanoid_Cooperative_Carrying|CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying]]
- **作者**: Ziyu Lin, Shihang Du, Tianhang Wang, Xiaodong Liu, Runze Zhang, Zongyou Yu, Haodong Zhang, Alois Knoll, Guang Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《CoCarry: Contact-Support-Structured Retargeting for Dual-Humanoid Cooperative Carrying》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large-scale human motion data, motion retargeting, and motion imitation have enabled increasingly capable whole-body control for individual humanoids. Cooperative carrying is more challenging because successful coordination requires not only plausible individual motions, but also consistent cross-agent and agent-object relations, including shared grasp, relative configuration, and whole-body support. We introduce CoCarry, a cooperative-carrying dataset containing 220 synchronized two-person sequences across 21 task schemes, five shared-object geometries, four terrain types, and approximately 61 minutes of motion. We further propose Contact-Support-Structured Retargeting, which starts from nominal individual motions and jointly refines both humanoids around the same prescribed object trajectory. Cooperation-aware object-local hand anchors preserve compatible four-hand grasp relations, while complementary upper object-interaction and lower support structures retain object-relative geometry and coordinated support. Across all 220 CoCarry sequences retargeted to two A3 humanoids, our method achieves 0.9995 contact preservation, reduces penetration duration by 67.0% and 71.0% relative to GMR and OmniRetarget, respectively, and maintains a 100% retargeting success rate. On CORE4D with Unitree G1 humanoids, it achieves 0.9906 contact preservation with zero measured sliding. We further validate the generated references through physics simulation and multiple real-world cooperative carrying experiments on two physical A3 humanoids, demonstrating their usability for downstream dual-humanoid control.

</details>

---

### [[20_Research/Papers/大模型/$R^2E_$_A_Role-driven_Reward_Evolutionary_Framework_for_Automated_Reward_Function_Design|$R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design]]

![[assets/2610.32439_figure.png|800]]

- **arXiv**: [2610.32439](https://arxiv.org/abs/2610.32439)
- **PDF**: https://arxiv.org/pdf/2610.32439
- **详细分析**: [[20_Research/Papers/大模型/$R^2E_$_A_Role-driven_Reward_Evolutionary_Framework_for_Automated_Reward_Function_Design|$R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design]]
- **作者**: Shouhao Chang, Xuan Liu, Hongye Zhu, Xinning Chen, Shigeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《$R^2E:$ A Role-driven Reward Evolutionary Framework for Automated Reward Function Design》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IRL, IsaacGym, PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing effective reward functions is a critical challenge in Reinforcement Learning (RL), which traditionally requires costly manual trial-and-error. While Large Language Model (LLM)-based methods have shown promise in reward design, undifferentiated sampling and limited use of historical feedback often lead to insufficient exploration of the reward space and optimization instability. To address these challenges, we propose $R^2E$, a Role-driven Reward Evolutionary framework for automated reward function design that structures the process through explicit role specialization. $R^2E$ employs multiple LLM roles with complementary objectives: an Explorer that promotes novelty to expand the search space, a Guardian that performs conservative refinements to improve training stability, and an Evolver that recombines high-performing rewards via crossover and mutation to integrate effective structures. A dynamic scheduling strategy coordinates these roles, progressively shifting the search from broad exploration to focused exploitation. To mitigate optimization instability and provide a medium for cross-role collaboration, $R^2E$ incorporates a Global Elite Pool that retains the best-performing rewards to guide subsequent generations, thereby enabling coordinated interaction among roles and ensuring a reliable and consistent refinement process. Extensive experiments on multiple robotic tasks demonstrate the effectiveness of our method.

</details>

---

### [[20_Research/Papers/机器人/Graphs_of_Trajectory_Bundles_for_Nonlinear_Motion_Planning|Graphs of Trajectory Bundles for Nonlinear Motion Planning]]

![[assets/2610.32365_figure.png|800]]

- **arXiv**: [2610.32365](https://arxiv.org/abs/2610.32365)
- **PDF**: https://arxiv.org/pdf/2610.32365
- **详细分析**: [[20_Research/Papers/机器人/Graphs_of_Trajectory_Bundles_for_Nonlinear_Motion_Planning|Graphs of Trajectory Bundles for Nonlinear Motion Planning]]
- **作者**: Joris Verhagen, Jon Arrizabalaga, Jana Tumova, Zachary Manchester
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Graphs of Trajectory Bundles for Nonlinear Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present the Graphs of Trajectory Bundles (GTB) method for motion planning of systems with nonlinear and black-box dynamics, combining sampling-based motion planning with trajectory optimization and graph search. Based on a graph-of-convex-sets decomposition of the workspace, GTB iteratively constructs a graph of trajectory bundles that captures the local dynamics of the system at any vertex. By solving a shortest-path problem on this graph, we find maximally dynamically feasible iterates that satisfy the system's dynamics in the limit and any constraints such as collision avoidance or additional safety or specification constraints by construction of the underlying graph. As a result, GTB can handle highly nonlinear, unstable, and even black-box dynamics with complex collision and specification constraints, making it a powerful tool for motion planning of complex systems.

</details>

---

### [[20_Research/Papers/机器人/LogLook_Execution-Grounded_Memory_for_Frontier-Model_Robot_Planners|LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners]]

![[assets/2610.32348_figure.png|800]]

- **arXiv**: [2610.32348](https://arxiv.org/abs/2610.32348)
- **PDF**: https://arxiv.org/pdf/2610.32348
- **详细分析**: [[20_Research/Papers/机器人/LogLook_Execution-Grounded_Memory_for_Frontier-Model_Robot_Planners|LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners]]
- **作者**: Tianyi Jiang, Tianyao Tong, Zhenshan Bing
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《LogLook: Execution-Grounded Memory for Frontier-Model Robot Planners》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EvoMem-VLA, MemoryVLA, OpenVLA, RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many manipulation tasks require a robot to remember what it has done and what it has seen. Frontier vision-language models can plan such tasks without task-specific training, but how such a planner should remember an episode is an open question. We argue that its memory must keep track of what the planner has done and learned, and must let the planner choose what to look at, since every frame costs tokens; a note rewritten at every step meets both poorly. We propose LogLook, whose execution-grounded memory lets the system keep the record, an execution log and the model's earlier notes, while the model decides where to look: frames are returned only where it expects a change, and demonstrations are skimmed before it inspects the parts it chooses. Measured with the benchmark's motion planner, LogLook matches the success of a note-only memory with 43% fewer tokens and less than half the images, and fails far fewer episodes through what it remembered or saw. With direct control, LogLook solves 93.5% of the RoboMME test set.

</details>

---

### [[20_Research/Papers/具身智能/DynaSlots_Slot-Centric_3D_Dynamics_Pretraining_for_Robot_Manipulation|DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation]]

![[assets/2610.32330_figure.png|800]]

- **arXiv**: [2610.32330](https://arxiv.org/abs/2610.32330)
- **PDF**: https://arxiv.org/pdf/2610.32330
- **详细分析**: [[20_Research/Papers/具身智能/DynaSlots_Slot-Centric_3D_Dynamics_Pretraining_for_Robot_Manipulation|DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation]]
- **作者**: Meng Li, Lijiang Chen, Qi Zhao, Jun Jiang, Longhao Zou, Shuchang Lyu, Guangliang Cheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.8（加权：具身智能 1.5，世界模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《DynaSlots: Slot-Centric 3D Dynamics Pretraining for Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation involves localized changes: picking up a cup moves the cup while leaving the surrounding scene largely unchanged. Yet existing 3D visual pretraining methods, including recent dynamics-aware variants, model state transitions at the scene level, compressing the motion of everything in a scene into a single global latent action. This conflates semantically distinct transitions in scenes with multiple moving parts, obscures dependencies between changing regions, and leaves the learned representation vulnerable to task-irrelevant scene content. We introduce DynaSlots, an action-free, label-free pretraining framework that decomposes each point cloud frame into a small set of temporally consistent slots and models dynamics at this per-slot level rather than the scene level. A temporal slot propagation module promotes consistent slot assignments across frames; an inverse dynamics model then extracts one latent action per slot from feature differences, and a diffusion-based forward dynamics model, paired with a self-supervised interaction head, predicts each slot's future state while learning pairwise proximity-and-motion relations. Experiments on Meta-World, Adroit, and a RealMan RM65-B robot demonstrate that DynaSlots outperforms prior scene-level baselines. It achieves superior success rates in simulation and exhibits strong robustness to scene clutter and unseen objects in real-world manipulation. Code is available at \href{https://zhucezhanghao12345-source.github.io/DynaSlots-Anonymous/}{https://zhucezhanghao12345-source.github.io/DynaSlots-Anonymous/}.

</details>

---

### [[20_Research/Papers/具身智能/MAST-VLA_Skill-Conditioned_Adaptation_with_Trajectory-Affordance_Priors_for_Multi-Skill_Robot_Manipulation|MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation]]

![[assets/2610.32312_figure.png|800]]

- **arXiv**: [2610.32312](https://arxiv.org/abs/2610.32312)
- **PDF**: https://arxiv.org/pdf/2610.32312
- **详细分析**: [[20_Research/Papers/具身智能/MAST-VLA_Skill-Conditioned_Adaptation_with_Trajectory-Affordance_Priors_for_Multi-Skill_Robot_Manipulation|MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation]]
- **作者**: Jiachi Yang, Zhiyi Xu, Hongquan Zhang, Xin Tan, Zhizhong Zhang, Jingyu Gong, Yuan Xie
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.2（加权：具身智能 3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《MAST-VLA: Skill-Conditioned Adaptation with Trajectory-Affordance Priors for Multi-Skill Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MAST-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot manipulation requires a single vision-language-action (VLA) policy to execute diverse skills across scenes and instructions. However, current multi-skill VLA policies often leave two aspects of an instruction insufficiently modeled: which primitive skill to execute and where/how to contact and move objects. We propose MAST-VLA (Multi-skill Adaptation with Skill-conditioned experts and Trajectory-affordance priors), a dual-conditioning framework for robot manipulation. MAST-VLA introduces skill-conditioned LoRA Mixture-of-Experts (LoRA-MoE) adapters in the LLM backbone, where skill-query tokens and routing biases guide low-rank expert specialization, and converts a predicted affordance heatmap into a patch-level trajectory-affordance spatial prior for the action head. On the CALVIN ABC$\rightarrow$D long-horizon multi-skill cross-scene generalization setting, MAST-VLA achieves state-of-the-art performance, reaching an Avg. Len of 4.65 over five-subtask evaluation sequences. Real-robot multi-skill sequence experiments further validate its deployability under real perception and control noise.

</details>

---

### [[20_Research/Papers/具身智能/Delay_Randomization_Widens_the_Delay_Margin_of_Learned_Humanoid_Motion_Trackers|Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers]]

![[assets/2610.32277_first_page.png|800]]

- **arXiv**: [2610.32277](https://arxiv.org/abs/2610.32277)
- **PDF**: https://arxiv.org/pdf/2610.32277
- **详细分析**: [[20_Research/Papers/具身智能/Delay_Randomization_Widens_the_Delay_Margin_of_Learned_Humanoid_Motion_Trackers|Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers]]
- **作者**: Shaoqin Li, Yi Sun
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Delay Randomization Widens the Delay Margin of Learned Humanoid Motion Trackers》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Humanoid-Gym, PolySim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned humanoid controllers are usually trained in one simulator and then checked in a second one before they go near hardware. We ask what that check says about command delay. We train motion-tracking policies for a 24-joint humanoid on five motions taken from monocular video and test them in an independent CPU MuJoCo harness, which we first verify against the training model. Every policy completes its motion in at least 26 of 30 episodes under the training randomization. With 40 ms of constant command delay, however, survival drops to 15% on average (0% - 45%), and the delay margin is only 20 - 30 ms. Randomizing the delay during training (0 - 50 ms) lifts survival at 40 ms to 95% on average (75% - 100%) and moves the margin to 50 - 70 ms. A control arm trained for the same number of extra iterations without delay does not improve, so the gain comes from the randomization itself. This holds for all five motions with three training seeds each, and a policy trained in PhysX behaves the same way. The price is slightly looser tracking (0.02 - 0.06 rad on four motions) and, for the most dynamic motion, less robustness to other perturbations. We also show that the first sim-to-sim gap we saw came from the harness, a missing floor and a wrong timestep, and not from the physics engines. The 0 - 20 ms delay ranges common in locomotion training lie inside the margin an unrandomized tracker already has. The benefit comes from randomizing beyond it, so the range should be set from the robot's measured latency, and delay margin belongs next to other sim-to-sim metrics.

</details>

---

### [[20_Research/Papers/具身智能/From_Tabletop_to_Walking_Bot_Deploying_a_VLA_Model_on_a_Legged_Manipulator_Robot|From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot]]

![[assets/2610.32271_first_page.png|800]]

- **arXiv**: [2610.32271](https://arxiv.org/abs/2610.32271)
- **PDF**: https://arxiv.org/pdf/2610.32271
- **详细分析**: [[20_Research/Papers/具身智能/From_Tabletop_to_Walking_Bot_Deploying_a_VLA_Model_on_a_Legged_Manipulator_Robot|From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot]]
- **作者**: Giovanni Minelli, Antonio Langella, Giovanni B. Dessy, Lorenzo Amatucci, Giulio Turrisi, Victor Barasuol, Claudio Semini
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 2.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《From Tabletop to Walking Bot: Deploying a VLA Model on a Legged Manipulator Robot》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are typically pretrained on broad, diverse datasets and subsequently fine-tuned on a comparatively small dataset tailored to a specific target robot. Such adaptation recipe is now widely established, achieving its most mature results on fixed-base arms due to their static base dynamics and consistent reference frame. Mounting the same arm on a quadruped extends the workspace to the entire floor, but fundamentally changes the embodiment: rather than controlling the arm in isolation, the policy must jointly coordinate base navigation, body posture, and end-effector motion. In this work, we study the practical demands of this embodiment change across data collection, model adaptation, and inference design to achieve closed-loop loco-manipulation on a Unitree Go2 with an AgileX Piper arm. We report the choices that made this real-robot deployment feasible, namely model variant, action horizon, and demonstration conventions, together with a study tailored to a pick-and-place task, separating data coverage from model capacity. We show that expanding demonstration coverage reduces held-out end-effector error by 30%, and incorporating secondary skills (such as pushing rather than grasping) introduces new behavioral modes without degrading baseline performance. Finally, closed-loop real-world experiments show how dataset composition shapes success and failure, validating the pipeline for more complex loco-manipulation.

</details>

---

### [[20_Research/Papers/机器人/RAISE-Vision_An_Automated_Contact_Angle_Measurement_Platform_for_Contact_Lens_Wettability_Characterization|RAISE-Vision: An Automated Contact Angle Measurement Platform for Contact Lens Wettability Characterization]]

![[assets/2610.32188_first_page.png|800]]

- **arXiv**: [2610.32188](https://arxiv.org/abs/2610.32188)
- **PDF**: https://arxiv.org/pdf/2610.32188
- **详细分析**: [[20_Research/Papers/机器人/RAISE-Vision_An_Automated_Contact_Angle_Measurement_Platform_for_Contact_Lens_Wettability_Characterization|RAISE-Vision: An Automated Contact Angle Measurement Platform for Contact Lens Wettability Characterization]]
- **作者**: Erin Ng, Mohammad Nazeri, Julie S Liu, Tithi Choksi, Lyndon Jones, Frank Gu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《RAISE-Vision: An Automated Contact Angle Measurement Platform for Contact Lens Wettability Characterization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact angle (CA) is a common parameter measured in the development of novel contact lens materials and surface coating technologies. Existing literature on in vitro CA of contact lenses via the sessile drop method is hindered in repeatability, reliability, and comparability due to inter-laboratory and inter-operator protocol variation. In this work, the Robotic Autonomous Imaging Surface Evaluator for vision applications (RAISE-Vision) is introduced as an automated platform for CA measurement on curved hydrogel surfaces, with specific application to in vitro contact lens wettability analysis throughout air exposure. Customized 3D printed hardware, such as lens mounts, camera holders and drying apparatuses, was designed to facilitate an automated repeated sessile drop workflow within a liquid handler. Collected images were directly fed to a custom open-source image processing script for CA determination on a curved surface that combines the elliptical fit and tangent methods to allow for variations in droplet shape. The CA of senofilcon A contact lenses measured using the RAISE-Vision platform increased from $62.6 \pm 5.5^\circ$ to $83.4 \pm 2.1^\circ$ over 10 sequential measurements in air and was able to replicate results obtained using an analogous manual protocol ($p = 0.470$). The custom image processing script was also separately demonstrated to generate comparable results to a commercially available CA determination software ($p = 0.343$). Aside from minimizing operator variability for CA measurement, RAISE-Vision provides a platform for standardized in vitro contact lens wettability analysis and understanding of surface wetting behaviour during air exposure.

</details>

---

### [[20_Research/Papers/强化学习/Geometry-Aware_Reinforcement_Learning_for_Close-Fitting_Wearable_Insertion|Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion]]

![[assets/2610.32143_figure.jpg|800]]

- **arXiv**: [2610.32143](https://arxiv.org/abs/2610.32143)
- **PDF**: https://arxiv.org/pdf/2610.32143
- **详细分析**: [[20_Research/Papers/强化学习/Geometry-Aware_Reinforcement_Learning_for_Close-Fitting_Wearable_Insertion|Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion]]
- **作者**: Takuma Tsukakoshi, Elle Miller, Tamon Miyake, Namiko Saito, Yushi Wang, Shigeki Sugano, Tetsuya Ogata, Sethu Vijayakumar
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.8，机器人 0.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Geometry-Aware Reinforcement Learning for Close-Fitting Wearable Insertion》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RCareWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot-assisted dressing is particularly challenging due to narrow openings and articulated body parts. Even small errors in the relative pose between the body part and garment opening can cause snagging, missed insertion, or incomplete dressing. To address these challenges, we formulate dressing as a geometry-aware insertion problem that represents task-relevant spatial relationships between the body part and object opening, rather than relying on the full deformable-object state. Based on this formulation, we propose a Reinforcement Learning (RL) framework combining a staged curriculum, which progressively guides the policy from coarse alignment to insertion and final placement, with a finger-wise insertion soft gate that provides continuous feedback on individual finger insertion progress and helps suppress premature insertion. We evaluate the framework on rigid and deformable bracelet dressing tasks through component ablations, systematic variations in the initial hand pose, and closed-loop execution of the learned policies on a real robotic system. On the post-training deformable evaluation, the full method reaches 84.7 +- 1.2% success. The insertion gate accounts for the largest gain, and adding the curriculum on top of that gate reaches the top score. On a mannequin hand the same full policy succeeds on 15/20 real-robot trials.

</details>

---

### [[20_Research/Papers/具身智能/TravSUITE_Traversability_via_Self-Supervised,_Uncertainty-Aware_IRL_and_Terrain_Estimation|TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation]]

![[assets/2610.32130_figure.png|800]]

- **arXiv**: [2610.32130](https://arxiv.org/abs/2610.32130)
- **PDF**: https://arxiv.org/pdf/2610.32130
- **详细分析**: [[20_Research/Papers/具身智能/TravSUITE_Traversability_via_Self-Supervised,_Uncertainty-Aware_IRL_and_Terrain_Estimation|TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation]]
- **作者**: Samuel Triest, Amirreza Shaban, David D. Fan, Wenshan Wang, Sebastian Scherer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《TravSUITE: Traversability via Self-Supervised, Uncertainty-Aware IRL and Terrain Estimation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traversability analysis in off-road settings remains a fundamental challenge for mobile robots. Key difficulties include constructing an accurate and expressive local map from multimodal sensor data, and using the map to design traversability rules that yield desirable navigation behavior. Importantly, this system must be resilient to the limited sensing regime brought about by complex environments and high speeds. In this paper, we present TravSUITE, a traversability system suitable for high-speed navigation in off-road environments. TravSUITE consists of two major components: 1) an efficient voxel mapper that leverages visual foundation models (VFMs) to build a rich geometric-semantic local map from streams of on-board sensor data, and 2) a unified neural network that jointly predicts traversability-relevant quantities in bird's eye view (BEV), including geometry, semantics, speed and cost. Our training strategy is entirely annotation-free and self-supervised, leveraging tasks such as map inpainting and inverse reinforcement learning (IRL) to learn both map representations and traversability. We perform a thorough ablation study and comparison to state-of-the-art approaches, and the results indicate that cost learning and auxiliary inpainting each contribute significantly to planning quality, and their combination is critical for achieving state-of-the-art performance in off-road path planning. We also design a simple risk adaptation mechanism to leverage our method's uncertainty estimates at deploy-time, and demonstrate that a combination of inpainting and risk estimation can result in 80% fewer navigation errors and 5% faster autonomous traversal speeds in real-world hardware experiments.

</details>

---

### [[20_Research/Papers/具身智能/Coupling_Execution_Horizon_and_Sampling_Depth_in_Flow-Matching_VLA_Policies|Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies]]

![[assets/2610.32102_figure.png|800]]

- **arXiv**: [2610.32102](https://arxiv.org/abs/2610.32102)
- **PDF**: https://arxiv.org/pdf/2610.32102
- **详细分析**: [[20_Research/Papers/具身智能/Coupling_Execution_Horizon_and_Sampling_Depth_in_Flow-Matching_VLA_Policies|Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies]]
- **作者**: Jiabing Yang, Yuan Xu, Yixiang Chen, Qisen Ma, Peiyan Li, Kai Wang, Chenhang Cui, Tao Yu, Zichen Wen, Wen Ye, Bowen Fang, Ziheng He...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Coupling Execution Horizon and Sampling Depth in Flow-Matching VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EQRL, Horizon-Depth-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching Vision-Language-Action (VLA) models generate expressive continuous trajectories for robotic manipulation, yet balancing real-time responsiveness with execution stability remains a persistent challenge. Standard deployment workflows typically treat numerical solver depth and execution horizon as decoupled choices. The horizon amortizes inference latency, while solver depth is kept high to preserve integration fidelity. In this paper, we reveal a fundamental compute-execution coupling in flow-matching VLAs governed by a systematic sign reversal. While coarse numerical integration degrades precision under rapid replanning, it markedly improves task performance under extended open-loop commitment. Geometrically, numerical truncation contracts lateral action dispersion around an invariant trajectory centroid, serving as an implicit regularizer that suppresses compounding open-loop drift. Across LIBERO, RoboTwin 2.0, and real-world Franka manipulation on representative VLA backbones including $π_0$, $π_{0.5}$, and GR00T, exploiting this joint coupling consistently achieves superior task success while drastically lowering inference latency, entirely training-free and without architectural modifications. These findings establish numerical sampling depth as an operational variance regulator, shifting its role from a static precision budget to an active deployment knob in robot learning. Project page: https://jiabingyang01.github.io/Horizon-Depth-VLA/

</details>

---

### [[20_Research/Papers/具身智能/DiscoDemo_Discovering_Efficient_and_Diverse_Robot_Demonstrations_for_Imitation_Learning|DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning]]

![[assets/2610.32093_figure.png|800]]

- **arXiv**: [2610.32093](https://arxiv.org/abs/2610.32093)
- **PDF**: https://arxiv.org/pdf/2610.32093
- **详细分析**: [[20_Research/Papers/具身智能/DiscoDemo_Discovering_Efficient_and_Diverse_Robot_Demonstrations_for_Imitation_Learning|DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning]]
- **作者**: Minho Park, Kinam Kim, Donghu Kim, Byungkun Lee, Dongyoon Hwang, Yongjae Shin, Junha Hyung, Hojoon Lee, Jaegul Choo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.6（加权：具身智能 0.9，强化学习 0.2，机器人 1.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DiscoDemo: Discovering Efficient and Diverse Robot Demonstrations for Imitation Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SMERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavior cloning for robotic manipulation is highly sensitive to the coverage of its training data, yet collecting diverse successful demonstrations remains costly. We study reinforcement learning (RL) not as a deployable controller, but as a data generator for downstream visuomotor imitation learning. Our key premise is that multiple successful solution modes cover a broader range of successful trajectories than repeatedly collecting a single narrow solution. We introduce DiscoDemo, which trains a privileged latent-conditioned RL generator with a parallel reverse curriculum and a success-gated diversity objective to discover diverse solutions while preserving task success. The trained generator produces multiple successful closed-loop behaviors, which are safety-filtered and exported as a static dataset for downstream imitation learning. Across four manipulation tasks, DiscoDemo produces broader successful-state coverage and improves downstream visuomotor policies in both simulation and the real world. Averaged across tasks, downstream success increases to 62% from 40% for the strongest baseline in simulation, and to 78% from 39% on the real robot, respectively. These results suggest that successful solution diversity improves imitation learning for a pretrained flow-matching VLA and remains complementary to corrective data collection. Project page: https://davian-robotics.github.io/DiscoDemo

</details>

---

### [[20_Research/Papers/机器人/Robotic_Budding_From_Homogeneous_Cells_to_Diverse_Morphologies_in_Physical_Self-Reproduction|Robotic Budding: From Homogeneous Cells to Diverse Morphologies in Physical Self-Reproduction]]

![[assets/2610.31929_figure.png|800]]

- **arXiv**: [2610.31929](https://arxiv.org/abs/2610.31929)
- **PDF**: https://arxiv.org/pdf/2610.31929
- **详细分析**: [[20_Research/Papers/机器人/Robotic_Budding_From_Homogeneous_Cells_to_Diverse_Morphologies_in_Physical_Self-Reproduction|Robotic Budding: From Homogeneous Cells to Diverse Morphologies in Physical Self-Reproduction]]
- **作者**: Siyuan Zhang, Junyan Liu, Wanglin He, Hod Lipson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Robotic Budding: From Homogeneous Cells to Diverse Morphologies in Physical Self-Reproduction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical self-reproduction in modular robots remains difficult because a robot must not only move, but also collect, align, dock, and separate modules reliably in hardware. Taking inspiration from how genetically identical cells form the varied tissues of an organism, we introduce a single standardized robotic module that combines a magnetic docking interface with two actuated joints and folds from a flat, two-dimensional configuration into three-dimensional structures. Modules of this single design can be assembled into two morphologies: a three-module "trilobite" and a five-module "seal". Using a small set of discrete motion commands, a human operator steers an assembled parent robot to dock magnetically with a sequence of spare modules, which are assembled into a second, structurally identical individual that then separates from the parent. Because the parent retains all of its original modules, this is a budding-style form of physical reproduction. Here, we report preliminary hardware demonstrations of this full process on both morphologies. We discuss the current scope of the system, including its present reliance on direct human teleoperation rather than autonomous control, and outline directions toward autonomous execution of this process and repeated validation across a larger number of independent trials.

</details>

---

### [[20_Research/Papers/强化学习/Move,_don't_think_sample-efficient_collision_avoidance_with_lossy_proximity_sensors|Move, don't think: sample-efficient collision avoidance with lossy proximity sensors]]

![[assets/2610.31891_figure.png|800]]

- **arXiv**: [2610.31891](https://arxiv.org/abs/2610.31891)
- **PDF**: https://arxiv.org/pdf/2610.31891
- **详细分析**: [[20_Research/Papers/强化学习/Move,_don't_think_sample-efficient_collision_avoidance_with_lossy_proximity_sensors|Move, don't think: sample-efficient collision avoidance with lossy proximity sensors]]
- **作者**: Carson Kohlbrenner, Niraj Pudasaini, William Xie, Naren Sivagnanadasan, Nikolaus Correll, Alessandro Roncone
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Move, don't think: sample-efficient collision avoidance with lossy proximity sensors》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data-driven robots must learn to avoid collisions with as few demonstrations as possible to avoid collecting large datasets of destructive collision examples. We explore whole-body proximity sensors as inductive biases for learning reflexive collision-dodging behavior and find that lossy sensors with low resolution were stronger biases than high-resolution coverage. We also found that, perhaps unintuitively, anticipating when and where contact happens on the body of a robot reduced its learning sample efficiency. We investigated eight candidate representations in a reinforcement learning environment, which included latent compression, future contact anticipation, lossy corruption, and privileged state estimation. The candidate representations were tested by training over 200 humanoid robots to play a simplified version of dodgeball end-to-end under an intentionally constrained sample and compute budget.

</details>

---

### [[20_Research/Papers/强化学习/Emergent_Cooperative_Thermoregulation_in_Lunar_Swarm_Robotics|Emergent Cooperative Thermoregulation in Lunar Swarm Robotics]]

![[assets/2610.31868_figure.png|800]]

- **arXiv**: [2610.31868](https://arxiv.org/abs/2610.31868)
- **PDF**: https://arxiv.org/pdf/2610.31868
- **详细分析**: [[20_Research/Papers/强化学习/Emergent_Cooperative_Thermoregulation_in_Lunar_Swarm_Robotics|Emergent Cooperative Thermoregulation in Lunar Swarm Robotics]]
- **作者**: Anais Jeger, Harry Holt, Lennart Puck
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Emergent Cooperative Thermoregulation in Lunar Swarm Robotics》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Swarms of small robots are an attractive way to survey lunar caves and lava tubes. Missions such as NASA's CADRE will fly cooperating rovers for distributed mapping, but only in daylight. The 354 h lunar night drops the surface towards 95 K, and the radioisotope heaters that let single rovers survive it cannot be supplied at swarm scale. In this study we investigate whether a swarm can instead use its own members as thermal shielding. We train one policy, shared by all twenty robots, by reinforcement learning with an evolution-strategies estimator. The policy receives a single reward, once, at the end of the night: the mean temperature of the five coldest robots. Nothing in that reward refers to position, spacing, exposure or motion. Two behaviors nonetheless emerge. The swarm aggregates, and robots circulate between the sheltered core and the exposed rim, the same pair of behaviors with which emperor penguins survive the Antarctic winter. We measure the survival threshold, the smallest stored energy per robot at which every robot is still alive at sunrise. Across ten runs it is 155.6 +/- 1.3 pcm-h, where one pcm-h is 7.2 kJ of stored heat. That is 37% below a motionless huddle and within 13% of a physics-based lower bound, and at a budget where the motionless huddle loses six robots, every robot survives. The behavior needs no shared spatial reference and no robot-robot contact, and transfers from twenty robots to forty without retraining.

</details>

---

### [[20_Research/Papers/具身智能/Full-Weight_VLA_Fine-Tuning_Without_an_fp32_Master_Copy_Silently_Erases_Most_Updates|Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates]]

![[assets/2610.31859_first_page.png|800]]

- **arXiv**: [2610.31859](https://arxiv.org/abs/2610.31859)
- **PDF**: https://arxiv.org/pdf/2610.31859
- **详细分析**: [[20_Research/Papers/具身智能/Full-Weight_VLA_Fine-Tuning_Without_an_fp32_Master_Copy_Silently_Erases_Most_Updates|Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates]]
- **作者**: Shubham Singh
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Full-Weight VLA Fine-Tuning Without an fp32 Master Copy Silently Erases Most Updates》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HuggingFaceVLA, MiniVLA, OpenVLA, SimpleVLA-RL, SmolVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a vision-language-action (VLA) model is fine-tuned with its trainable weights in bfloat16 (bf16) and no fp32 master copy, AdamW writes each update straight into bf16, silently rounding away any update smaller than 1/512 of a weight. In 9 of 12 open VLA codebases a default or documented recipe trains this way, 4 on full weight matrices, including LeRobot's SmolVLA default and its $π_0$/$π_{0.5}$ guides. In our LIBERO runs without the copy, a probe every 100 steps finds at least 79% of updates to bf16 weights erased. On the Hugging Face Hub, 99% of sampled full-weight SmolVLA fine-tunes store the action expert in bf16, and 84% of recent $π_{0.5}$ fine-tunes with a training configuration set the bf16 flag. On LIBERO-Object, with rules fixed in advance, an fp32 copy raises success over LeRobot's storage from 4.3% to 49.3% for SmolVLA and from 5.1% to 80.9% for $π_{0.5}$ at a ten-times lower learning rate, where both models are undertrained, and from 89.0% to 97.7% for $π_{0.5}$ at its default rate. For SmolVLA at its default rate it adds 10.2 points with open-loop 50-action chunks but only 4.2 when re-planning every 10 actions. In these five comparisons and two more against SmolVLA with every trainable weight in bf16, every run with the copy beats every run without it (p &lt; 0.05); all gaps but the 8.7- and 4.2-point ones clear our 10-point threshold. The fix is to keep the trainable weights in fp32 during training, a one-line change for SmolVLA in LeRobot.

</details>

---

### [[20_Research/Papers/具身智能/FORCA_A_Force-Aware_Coding_Agent_for_Contact-Rich_Robot_Manipulation|FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation]]

![[assets/2610.31841_figure.png|800]]

- **arXiv**: [2610.31841](https://arxiv.org/abs/2610.31841)
- **PDF**: https://arxiv.org/pdf/2610.31841
- **详细分析**: [[20_Research/Papers/具身智能/FORCA_A_Force-Aware_Coding_Agent_for_Contact-Rich_Robot_Manipulation|FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation]]
- **作者**: Xiao Tan, Yixuan Wang, Zhexi Wang, Wenzhen Yuan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.2，大模型 0.5，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《FORCA: A Force-Aware Coding Agent for Contact-Rich Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents can translate language instructions into robot programs. For contact-rich manipulation, a key challenge is to generate and refine control logic that responds to physical interaction. We present FORCA, a coding agent that takes visual observations and wrist force/torque (F/T) measurements as input to write Python programs for contact probing and force-responsive motion. Between executions, the agent inspects force records alongside visual outcomes to diagnose failures and revise both motion and force-feedback control logic. FORCA requires no demonstrations, task-specific training, or simulation. Across five real-robot tasks, we demonstrate its effectiveness in three forms of contact-rich manipulation: improving manipulation accuracy, adapting to changes in object or surface properties, and regulating contact under surface variation and object motion. Compared with a vision-only variant of the same agent, FORCA improves grasp accuracy and task success and reduces contact loss in wiping and peeling.

</details>

---

### [[20_Research/Papers/大模型/KiRoSe_Using_Kinematic_Data_for_Efficient_Segmentation_of_Robot_Demonstrations|KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations]]

![[assets/2610.31801_figure.png|800]]

- **arXiv**: [2610.31801](https://arxiv.org/abs/2610.31801)
- **PDF**: https://arxiv.org/pdf/2610.31801
- **详细分析**: [[20_Research/Papers/大模型/KiRoSe_Using_Kinematic_Data_for_Efficient_Segmentation_of_Robot_Demonstrations|KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations]]
- **作者**: Shuangyu Xie, Kaiyuan Chen, Muhammad Zubair Irshad, Richard Cheng, Sergey Zakharov, Ken Goldberg
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《KiRoSe: Using Kinematic Data for Efficient Segmentation of Robot Demonstrations》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RoboSegNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Segmenting robot demonstration data into disjoint temporal and semantic subsegments is valuable for learning, cleaning, retrieval, and analysis. Segmentation is often performed manually in a tedious and error prone process. Multimodal Large Language Models (MLLMs) have the potential for automating this process, but directly ingesting raw multi camera video streams into MLLMs can be costly and can quickly exhaust context windows. In this paper, we introduce KiRoSe (Kinematics for Robot Segmentation), a novel framework that focuses on the companion stream of robot kinematic data. Inspired by the principle of classical entropy coding, such as Huffman coding, where frequently occurring symbols are represented more compactly, we propose Sparse Motion Tokens (SMTs), a discrete kinematic vocabulary designed to compactly represent recurring, temporally localized motion patterns, which we refer to as kinematic events. SMTs are learned by encoding kinematic trajectories with temporal segment supervision and quantizing the resulting features. We use increasingly available robot demonstration subtask annotations to supervise an open language model to interpret the resulting token sequences. Evaluation against human labeled segmentation shows that KiRoSe can substantially outperform baseline segmentation methods in F1 quality and transfers zero shot to unseen robot embodiments and egocentric human motion, while preserving the language models open vocabulary knowledge. Beyond segmentation, KiRoSe tracks task progress on an unseen robot and detects when an action is being reversed.(website: https://berkeleyautomation.github.io/kirose/)

</details>

---

### [[20_Research/Papers/强化学习/FLORA_An_Open_Model_Suite_for_Scaling_Robotics_Data_Engines|FLORA: An Open Model Suite for Scaling Robotics Data Engines]]

![[assets/2610.31779_figure.png|800]]

- **arXiv**: [2610.31779](https://arxiv.org/abs/2610.31779)
- **PDF**: https://arxiv.org/pdf/2610.31779
- **详细分析**: [[20_Research/Papers/强化学习/FLORA_An_Open_Model_Suite_for_Scaling_Robotics_Data_Engines|FLORA: An Open Model Suite for Scaling Robotics Data Engines]]
- **作者**: Sicong Leng, Yunze Man, Zhiqi Li, Jing Wang, Yuhe Zhang, Ryan Punamiya, Siddharth Patki, Kaiyuan Zheng, Zi-ang Cao, Zhiding Yu, Sifei Liu, Danfei Xu...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《FLORA: An Open Model Suite for Scaling Robotics Data Engines》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DenseCaptionBench, DenseRewardBench, RoboRewardBench, RobometerBench, RubricBench, WGO-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The life-cycle of robotics foundation models crucially depends on data labels. Outcome reward labels are needed for monitoring real-world deployments. Process reward labels are needed during RL post-training. Timestamped captions are needed for filtering and balancing pretraining data. We present Flora, an industrial-quality data engine used for training GR00T models, that simultaneously covers these capabilities. Flora achieves SOTA scores on the captioning benchmark WGO-Bench and reward benchmarks RoboReward and Robometer. On internal benchmarks it is competitive with GPT-6 Astra while beating other frontier models. The model is substantially cheaper than API-based alternatives, roughly 125 times cheaper than GPT-6 Astra. Florais battle tested at scale, labeling 200,000 hours of data per day across 512 GB300s. By open-sourcing our data engine, we enable researchers to scale custom robotics datasets and explore emerging applications such as physical auto-research and human-to-robot transfer.

</details>

---

### [[20_Research/Papers/具身智能/The_effect_of_limb_kinematics_on_the_speed_of_a_legged_robot_on_granular_media|The effect of limb kinematics on the speed of a legged robot on granular media]]

![[assets/1303.7276_figure.jpg|800]]

- **arXiv**: [1303.7276](https://arxiv.org/abs/1303.7276)
- **PDF**: https://arxiv.org/pdf/1303.7276
- **详细分析**: [[20_Research/Papers/具身智能/The_effect_of_limb_kinematics_on_the_speed_of_a_legged_robot_on_granular_media|The effect of limb kinematics on the speed of a legged robot on granular media]]
- **作者**: Chen Li, Paul B. Umbanhowar, Haldun Komsuoglu, Daniel I. Goldman
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《The effect of limb kinematics on the speed of a legged robot on granular media》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving effective locomotion on diverse terrestrial substrates can require subtle changes of limb kinematics. Biologically inspired legged robots (physical models of organisms) have shown impressive mobility on hard ground but suffer performance loss on unconsolidated granular materials like sand. Because comprehensive limb-ground interaction models are lacking, optimal gaits on complex yielding terrain have been determined empirically. To develop predictive models for legged devices and to provide hypotheses for biological locomotors, we systematically study the performance of SandBot, a small legged robot, on granular media as a function of gait parameters. High performance occurs only in a small region of parameter space. A previously introduced kinematic model of the robot combined with a new anisotropic granular penetration force law predicts the speed. Performance on granular media is maximized when gait parameters minimize body acceleration and limb interference, and utilize solidification features of granular media.

</details>

---
