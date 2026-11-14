# cs.CV | Computer Vision and Pattern Recognition | 2026-11-13

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/具身智能/ProtoVis-Nav_Prototypical_Visual_Imagination_for_Visual-Spatial_Aligned_UAV_Navigation|ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation]]

![[assets/2611.17330_figure.jpg|800]]

- **arXiv**: [2611.17330](https://arxiv.org/abs/2611.17330)
- **PDF**: https://arxiv.org/pdf/2611.17330
- **详细分析**: [[20_Research/Papers/具身智能/ProtoVis-Nav_Prototypical_Visual_Imagination_for_Visual-Spatial_Aligned_UAV_Navigation|ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation]]
- **作者**: Guangyuan Sui, Yunzhong Hou, Chi Harold Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《ProtoVis-Nav: Prototypical Visual Imagination for Visual-Spatial Aligned UAV Navigation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DriveVLA, HUGE-Bench, ReconVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision language navigation (VLN) is very challenging for Unmanned Aerial Vehicles (UAVs) since small errors in 3D motion prediction can lead to navigation errors and collisions. Unable to fathom execution outcomes in 3D environments, existing methods often struggle to predict accurate navigation waypoints from language instructions. To solve this, we introduce the Prototypical Visual Imagination framework, shortened as ProtoVis-Nav, which forces the model to imagine an outcome-associated local visual representation for the intended next UAV movement. Specifically, we predict feature prototypes and use their linear combination to estimate the visual feature of the target region. In this manner, the VLN model first imagines the local visual representation of the next intended location, and then uses predicted prototypes as context for generating the final action, promoting alignment between visual context and waypoint outputs. Extensive experiments demonstrate the effectiveness of the ProtoVis-Nav framework and show substantial improvements over existing baselines.

</details>

---

### [[20_Research/Papers/具身智能/UAV-Flow++_A_Unified_Suite_for_Benchmarking_and_Learning_Language-Guided_UAV_Flight|UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight]]

![[assets/2611.17163_figure.png|800]]

- **arXiv**: [2611.17163](https://arxiv.org/abs/2611.17163)
- **PDF**: https://arxiv.org/pdf/2611.17163
- **详细分析**: [[20_Research/Papers/具身智能/UAV-Flow++_A_Unified_Suite_for_Benchmarking_and_Learning_Language-Guided_UAV_Flight|UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight]]
- **作者**: Donglin Yang, Xiangyu Wang, Yantong Zhong, Wenhao Zheng, Zihan Ding, Yue Liao, Hongsheng Li, Ke Xu, Si Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《UAV-Flow++: A Unified Suite for Benchmarking and Learning Language-Guided UAV Flight》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirVLA, FlowVLA, HUGE-Bench, OpenVLA, RIPT-VLA, RaceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-guided UAV navigation has largely focused on long-horizon route planning, leaving short-range, object-relative flight maneuvers underexplored. To address this gap, we formulate Flying-on-a-Word (Flow), a task requiring a UAV to convert concise natural-language instruction, egocentric visual observation, and current state dynamics into continuous flight actions. Flow encompasses both primitive motion commands and complex object-interactive behaviors, assessing motion intent comprehension and spatial context grounding. To enable policy learning and closed-loop evaluation, we introduce UAV-Flow, a comprehensive dataset comprising 30,692 expert-piloted real-world trajectories across eight distinct motion categories, alongside 10,109 simulation trajectories in the UAV-Flow-Sim environment equipped with task-specific completion criteria. Furthermore, we develop FlowVLA, which undergoes imitation pretraining on mixed real-sim demonstrations and online post-training via Tail-Aware GRPO (TGRPO). By leveraging group reward distributions, TGRPO effectively reinforces high-reward action sequences. Evaluated on 273 held-out UAV-Flow-Sim episodes, pretrained FlowVLA achieves a mean success rate of 75.58%, outperforming the strongest baseline by 6.72 percentage points, which TGRPO post-training further elevates to 93.16% with superior sample efficiency. Physical UAV experiments demonstrate robust execution of object-relative commands in both indoor and outdoor real-world scenes. Together, Flow establishes a novel benchmark and learning framework for language-conditioned flight maneuvers.

</details>

---

### [[20_Research/Papers/具身智能/I_See_What_You_Want_Decoding_Hierarchical_Operator_Intent_from_Visual_Teleoperation_History|I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History]]

![[assets/2611.16419_figure.png|800]]

- **arXiv**: [2611.16419](https://arxiv.org/abs/2611.16419)
- **PDF**: https://arxiv.org/pdf/2611.16419
- **详细分析**: [[20_Research/Papers/具身智能/I_See_What_You_Want_Decoding_Hierarchical_Operator_Intent_from_Visual_Teleoperation_History|I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History]]
- **作者**: Xiangyi Jia, Kaixian Qu, Shengzhi Wang, Chenyu Yang, Robert Katzschmann, Marco Hutter
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《I See What You Want: Decoding Hierarchical Operator Intent from Visual Teleoperation History》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AliasBench, IntentVLA, Real-World, RoboVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) have become a powerful foundation for robotic scene understanding, task planning, and language-conditioned control. A natural question follows: can these models also decode what a human operator intends while teleoperating a robot, without any explicit instruction? We formulate this as hierarchical intent prediction, jointly inferring the ongoing atomic action and the broader mission it serves from a short visual teleoperation history. To study this, we introduce VI AMO (Vision Intention Action and Mission Ongoing), a dataset of 6,600 episodes from eleven robot sources with 13,653 temporally aligned action annotations and 9,702 mission annotations. Large proprietary models struggle with this problem: on held-out episodes, GPT-4o reaches Sentence-BERT similarities of only 0.563 and 0.470 for action and mission, and GPT-5.6 Luna achieves only 0.581 and 0.554. Fine-tuning a VLM on VI AMO yields our Vision-Intention Model (VIM), which raises these scores to 0.825 and 0.821 and still reaches 0.726 and 0.717 on the 35.4% of test actions with both labels absent from training. Finally, as a downstream application, VIM's predicted mission enables a vision-language-action (VLA) policy to take over from the operator mid-task in a real-world environment unseen during VIM fine-tuning, reducing human teleoperation time by 34.6% relative to GPT-4o and 39.8% relative to GPT-5.6 Luna, while cutting intent-prediction latency by roughly 70% on average.

</details>

---

### [[20_Research/Papers/具身智能/MOSAIC_Modular_Obstacle_and_Spatial-Aware_Framework_for_Manipulation_In_Cluttered_Scenes|MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes]]

![[assets/2611.15937_figure.png|800]]

- **arXiv**: [2611.15937](https://arxiv.org/abs/2611.15937)
- **PDF**: https://arxiv.org/pdf/2611.15937
- **详细分析**: [[20_Research/Papers/具身智能/MOSAIC_Modular_Obstacle_and_Spatial-Aware_Framework_for_Manipulation_In_Cluttered_Scenes|MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes]]
- **作者**: Richard Shi, Mohammad Mahdavian, Mehrdad Momeni Zadeh, Mohammed Elmahgiubi, Amir Rasouli
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《MOSAIC: Modular Obstacle and Spatial-Aware Framework for Manipulation In Cluttered Scenes》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GeoVLA, OBEYED-VLA, PointVLA, SAM3D-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have demonstrated strong performance in robotic manipulation, yet most rely primarily on 2D visual observations and language instructions, leaving scene geometry and obstacle relationships to be inferred implicitly. This limitation is particularly problematic in cluttered environments, where small spatial errors can lead to unintended contacts or collisions. We propose MOSAIC, a modular spatial- and obstacle-aware framework that can be integrated with pretrained VLA policies to improve object-level scene understanding and action generation. Our method augments the VLA backbone with an auxiliary semantic grounding task that predicts role-specific masks for the target object, destination region, and surrounding obstacles. We further combine the target and destination masks with depth estimated from 3D scene reconstruction to construct role-specific geometric tokens that are injected directly into the action expert. In addition, we propose obstacle-aware attention supervision that emphasizes obstacles near the robot body during task execution. The resulting attention features are subsequently injected into later action-expert layers to further guide action generation. Together, these components provide explicit semantic, geometric, and obstacle-aware cues while preserving the underlying pretrained VLA architecture. We evaluate our framework on pretrained VLA model using the RoboPRO benchmark, including visual perturbation tests, and further validate it on real-world manipulation tasks. MOSAIC improves the success rate by 5.1% in cluttered scenes, and by 9.7% under visual perturbations, with gains of up to 25.0% in the most challenging environment. We will release our code and dataset upon acceptance at the following Github page: https://mmahdavian.github.io/MOSAIC/

</details>

---

### [[20_Research/Papers/机器人/Reading_the_Table_Sim-to-Real_Game_State_Detection_for_the_Chef's_Hat_Card_Game|Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game]]

![[assets/2611.15524_figure.png|800]]

- **arXiv**: [2611.15524](https://arxiv.org/abs/2611.15524)
- **PDF**: https://arxiv.org/pdf/2611.15524
- **详细分析**: [[20_Research/Papers/机器人/Reading_the_Table_Sim-to-Real_Game_State_Detection_for_the_Chef's_Hat_Card_Game|Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game]]
- **作者**: Connor Gäde, Matthias Kerzel, Hauke Bünning, Jan-Gerrit Habekost, Mariana Barros, Stefan Wermter
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Reading the Table: Sim-to-Real Game State Detection for the Chef's Hat Card Game》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoppeliaSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tabletop games offer a compelling scenario to study the interaction between artificial and human agents, combining social interaction with game state tracking and physical manipulation. To assess the game state, a robot needs to precisely detect closely related game objects, such as different card designs, requiring dedicated training data that is costly to annotate in the real world. Instead, we develop a fully automated synthetic data collection pipeline, using re-projection of known 3D coordinates to generate labels automatically and domain randomization to bridge the reality gap. This approach is used to collect a dataset of 25413 samples to finetune an object detection and a segmentation model, which are combined to assign detected cards to game-relevant zones and infer the game state. When evaluated on a real NICO humanoid robot, our pipeline achieves an F1-score of 0.906 for card-to-zone assignment, thus providing the perceptual foundation for a robot that can autonomously play Chef's Hat against human players.

</details>

---

### [[20_Research/Papers/具身智能/What_Makes_a_VLA_Reactive_A_Study_of_Execution_Strategies_for_Dynamic_Manipulation|What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation]]

![[assets/2611.15491_figure.jpg|800]]

- **arXiv**: [2611.15491](https://arxiv.org/abs/2611.15491)
- **PDF**: https://arxiv.org/pdf/2611.15491
- **详细分析**: [[20_Research/Papers/具身智能/What_Makes_a_VLA_Reactive_A_Study_of_Execution_Strategies_for_Dynamic_Manipulation|What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation]]
- **作者**: Zhuoyue Li, Zhendong Han, Pankhuri Vanjani, Wenting Li, Rudolf Lioutikov
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 2.82（加权：具身智能 1.8，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《What Makes a VLA Reactive? A Study of Execution Strategies for Dynamic Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL, DynamicVLA, IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models predict chunks of future actions, and when objects move, those chunks go stale before they are executed. We study what makes a pretrained VLA reactive, using \pihalf{} on two dynamic simulation benchmarks and three real-robot tasks. We vary the prediction and execution horizons, compare synchronous and asynchronous inference, test methods that deliver actions sooner or keep successive chunks continuous, and adapt the policy with motion cues and latent-space reinforcement learning. The best prediction horizon is about one second, and the best execution horizon depends on the checkpoint. Short horizons help more with asynchronous execution, and methods that keep the trajectory continuous outperform those that only reduce latency. Adapting the policy repairs targeted failures, but on the conveyor task changing the execution horizon gained as much. Reactivity depends on the execution pipeline as much as on the policy, so both should be evaluated together.

</details>

---

### [[20_Research/Papers/世界模型/Prediction_or_Persistence_What_Future-Prediction_Scores_Miss_About_World_Models|Prediction or Persistence? What Future-Prediction Scores Miss About World Models]]

![[assets/2611.15082_figure.png|800]]

- **arXiv**: [2611.15082](https://arxiv.org/abs/2611.15082)
- **PDF**: https://arxiv.org/pdf/2611.15082
- **详细分析**: [[20_Research/Papers/世界模型/Prediction_or_Persistence_What_Future-Prediction_Scores_Miss_About_World_Models|Prediction or Persistence? What Future-Prediction Scores Miss About World Models]]
- **作者**: Animesh Maheshwari
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Prediction or Persistence? What Future-Prediction Scores Miss About World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained video world models are compared and chosen as components for robot learning largely by future-prediction scores. On its own, such a score cannot be read as evidence of prediction, because it mixes encoder quality, the near future's resemblance to the recent past, and the predictor's own contribution. We separate the three with a matched control. On 27,000 future-retrieval trials from household egocentric video, a model must pick the true continuation of a clip among eleven candidates from the same video (chance 0.091), ranked zero-shot by its own training criterion. Each model is paired with a persistence control, an identical copy whose predictor is never invoked, so the paired difference isolates the predictor. Score and contribution dissociate within the native-video V-JEPA family alone: the predictor adds +0.291 top-1 for V-JEPA 2.1 but +0.03 to +0.04 for V-JEPA 2 on the identical trials. Across five models the contribution ranges from +0.291 to negative, and it is negative only for the two action-conditioned models, which we evaluate outside their training regime. Persistence alone recovers the encoder ordering expected from pretraining, a sign that the probe tracks real signal. We suggest reporting each future-prediction score together with its persistence baseline. The gap between them, not the score, is what makes the number interpretable: a necessary check costing one forward pass. Establishing downstream usefulness is a separate matter, for a planning or control evaluation.

</details>

---

### [[20_Research/Papers/大模型/Adapting_Monocular_Depth_Estimation_in_Novel_Scenes_through_Disparity_Refinement_and_Robot_Ego-Motion|Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion]]

![[assets/2611.14958_figure.png|800]]

- **arXiv**: [2611.14958](https://arxiv.org/abs/2611.14958)
- **PDF**: https://arxiv.org/pdf/2611.14958
- **详细分析**: [[20_Research/Papers/大模型/Adapting_Monocular_Depth_Estimation_in_Novel_Scenes_through_Disparity_Refinement_and_Robot_Ego-Motion|Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion]]
- **作者**: Dimitrios Chatziparaschis, Georgios Georgakis, Adnan I. Ansar, Shehryar Khattak, Konstantinos Karydis
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Adapting Monocular Depth Estimation in Novel Scenes through Disparity Refinement and Robot Ego-Motion》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The geometric understanding of a scene is a crucial component for safe and efficient robotic operations in novel and unstructured environments. The recent emergence of foundation models for Monocular Depth Estimation (MDE) has provided an opportunity to enrich robotic perception capabilities with dense long-range depth predictions, replacing expensive onboard hardware (e.g., LiDARs and stereo cameras). However, these offline models are primarily trained on affine-invariant depth representations, and their generalization to novel scenes remains unclear. In this work we present EM-ViT, a monocular depth estimation model that learns to adapt online relative depth inputs from a foundation model prior to the metric scale with observations collected during robotic operations. Motivated by the stereo camera parameterization, our method decomposes depth prediction via dense disparity refinement to recover the scene's relative structure and an effective baseline scalar prediction to determine the missing metric scale. The learning process leverages sparse LiDAR points and, optionally, the robot's Ego-Motion (EM) to rapidly train a lightweight Vision Transformer (ViT), while an internal gradient matching loss preserves the fine-grained semantic structure of the input disparity in real-time. We demonstrate the efficacy of our method on publicly available sequences, such as KITTI, and show that our online learning pipeline can adapt to novel scenes faster and with higher accuracy than existing MDE foundation models. The code and supplementary materials will be publicly available at https://emvit-mde.github.io.

</details>

---

### [[20_Research/Papers/具身智能/RSLiveBench-UAV_A_Continually_Evolving_Vision-Language_Benchmark_for_Aerial_Spatial_Intelligence|RSLiveBench-UAV: A Continually Evolving Vision-Language Benchmark for Aerial Spatial Intelligence]]

![[assets/2611.14953_figure.png|800]]

- **arXiv**: [2611.14953](https://arxiv.org/abs/2611.14953)
- **PDF**: https://arxiv.org/pdf/2611.14953
- **详细分析**: [[20_Research/Papers/具身智能/RSLiveBench-UAV_A_Continually_Evolving_Vision-Language_Benchmark_for_Aerial_Spatial_Intelligence|RSLiveBench-UAV: A Continually Evolving Vision-Language Benchmark for Aerial Spatial Intelligence]]
- **作者**: Yue Zhou, Jiawei Liu, Jue Chen, Ziyang Gong, Haojia Wei, Jingxiang Li, Xue Jiang, Zhihang Zhong, Pai Peng, Xue Yang, Yansheng Li, Jonathan Li
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，机器人 0.8）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《RSLiveBench-UAV: A Continually Evolving Vision-Language Benchmark for Aerial Spatial Intelligence》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ChatEarthBench, Geo3DVQA, LiveBench, LiveCodeBench, MMBench, MMSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial spatial intelligence (ASI) requires models to understand objects and spatial relationships across changing viewpoints and scales. Evaluating these abilities as models evolve calls for fresh physical observations, yet producing new aerial spatial questions requires repeatedly establishing entity identities, geometric references, and cross-view correspondences. We introduce \textbf{RSLiveBench-UAV}, a continually evolving vision-language benchmark driven by recurring acquisition of real UAV imagery. Its update protocol admits images captured after the preceding release and delays answer disclosure. An entity-centered production workflow uses geometry-assisted association to link repeated observations of physical vehicles, reuse human-verified attributes, and combine them with view-specific annotations and spatial references for traceable question generation. All tasks use deterministic scoring without model judges. We evaluate 30 general-purpose, remote-sensing, and embodied models on 35,491 question records from ten scenes, covering 17 tasks across 2D perception, 3D perception, cross-view perception, and reasoning. All 18 tested embodied models outperform the three selected remote-sensing comparators in Overall, although the strongest embodied model scores 43.29 versus 59.88 for GPT-6-Astra. Fine-grained vehicle recognition remains challenging, and performance varies across heights and camera pitches. Retrospective scene-group comparisons and rolling-window replay characterize score-pattern consistency under scene renewal. RSLiveBench-UAV connects fresh physical observations, entity-centered answer production, and systematic model evaluation to support continual assessment of ASI. Benchmark will release at https://rslivebench.space

</details>

---
