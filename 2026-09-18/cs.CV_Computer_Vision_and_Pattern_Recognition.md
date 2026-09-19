# cs.CV | Computer Vision and Pattern Recognition | 2026-09-18

#arxiv #ComputerScience

**论文数**: 14

### [[20_Research/Papers/具身智能/DexTouch-WM_Learning_Action-Conditioned_Tactile_World_Models_from_Human_Touch_for_Dexterous_Robot_Manipulation|DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation]]

![[assets/2609.20649_figure.png|800]]

- **arXiv**: [2609.20649](https://arxiv.org/abs/2609.20649)
- **PDF**: https://arxiv.org/pdf/2609.20649
- **详细分析**: [[20_Research/Papers/具身智能/DexTouch-WM_Learning_Action-Conditioned_Tactile_World_Models_from_Human_Touch_for_Dexterous_Robot_Manipulation|DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation]]
- **作者**: Yan Qin, Yue Chen, Wenwei Lin, Shujia Liu, Chuqiao Lyu, Kailun Su, Chenze Yu, Ping Luo, Wenbo Ding, Tianxing Chen, Renjing Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 5.0（加权：具身智能 2.7，世界模型 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexTouch-WM: Learning Action-Conditioned Tactile World Models from Human Touch for Dexterous Robot Manipulation》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FeelWorld, TouchWorld, ViTacWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning predictive models of contact-rich dexterous manipulation requires dense tactile interaction, but such data are costly to scale on real robots and remain tied to embodiment-specific sensors. We introduce DexTouch-WM, an action-conditioned world model that learns from scalable human touch to jointly predict future RGB observations and bilateral tactile dynamics. Our insight is that human and robot manipulation share transferable contact dynamics when their tactile observations and action spaces are made compatible. We deploy flexible piezoresistive arrays with a shared sensing layout on both human and dexterous robot hands, and retarget human motion into the robot action space so that human interaction can supervise the same dynamics model used for real-robot prediction. DexTouch-WM couples a pretrained video expert with a lightweight tactile expert using anatomy-aware tactile tokens and aligned action conditioning. In human-to-robot scaling experiments, we keep five hours of real-robot supervision fixed while increasing human interaction from 0 to 100 hours, and observe substantial improvements in held-out robot-domain visual, geometric, and contact prediction despite disjoint human and robot task sets. Beyond prediction, we evaluate the world models as surrogate environments for policy evaluation and as generators of synthetic trajectories for real-robot policy learning, showing that scalable human interaction provides a complementary data axis for learning dexterous robot world models.

</details>

---

### [[20_Research/Papers/强化学习/INSPECT_Learning_Robot_View_Selection_from_Assistant_Use|INSPECT: Learning Robot View Selection from Assistant Use]]

![[assets/2609.20615_figure.jpg|800]]

- **arXiv**: [2609.20615](https://arxiv.org/abs/2609.20615)
- **PDF**: https://arxiv.org/pdf/2609.20615
- **详细分析**: [[20_Research/Papers/强化学习/INSPECT_Learning_Robot_View_Selection_from_Assistant_Use|INSPECT: Learning Robot View Selection from Assistant Use]]
- **作者**: Di Wen, Kailun Yang, Wenhao Guo, Yitian Shi, Junwei Zheng, Yufan Chen, Ruiping Liu, Jiale Wei, Rania Rayyes, Kunyu Peng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《INSPECT: Learning Robot View Selection from Assistant Use》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ActiveVLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots inspecting an assembly must determine which parts are present and whether they are correctly installed. During egocentric assembly assistance, head motion and workpiece handling reveal evidence for these checks, while spoken state confirmations link observations to procedural outcomes. We introduce INSPECT, which learns robot view preferences from records of a smart-glasses assistant that answers part queries and provides next-step guidance. Presence-Invariant TwinSwap (PI-TwinSwap) calibrates object evidence through paired identity interventions. Claim-indexed supervision separates evidence requirements from camera-reproducible observation changes. Object-centered calibration adapts relative view preferences to robot poses, while clause-level screening checks predicted evidence. The robot selects views using only its current observation and known poses, without candidate images. Evaluation uses annotated assistant-video replay to simulate state feedback, without target-domain view labels for policy training. On images of physical gearbox assemblies, INSPECT achieves the highest view utility among the compared non-oracle policies and raises human-rated full verifiability from 34.8% to 41.7% compared with keeping the current view. On commercial angle-grinder recordings in IMPACT, the transferred relative-view selector increases the correct decision rate from 50.6% to 54.3% with a frozen perception head. The source code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/CoRef-GS_Cooperative_Referring_Gaussian_Splatting_for_Multi-Agent_Scene_Understanding|CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding]]

![[assets/2609.20586_figure.png|800]]

- **arXiv**: [2609.20586](https://arxiv.org/abs/2609.20586)
- **PDF**: https://arxiv.org/pdf/2609.20586
- **详细分析**: [[20_Research/Papers/具身智能/CoRef-GS_Cooperative_Referring_Gaussian_Splatting_for_Multi-Agent_Scene_Understanding|CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding]]
- **作者**: Zhikun Zhou, Kunyu Peng, Runyi Yang, Junhao Cai, Di Wen, Ruiping Liu, Danda Pani Paudel, Yi Zhou, Luc Van Gool, Kailun Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.9，大模型 0.4，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《CoRef-GS: Cooperative Referring Gaussian Splatting for Multi-Agent Scene Understanding》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Referring scene understanding for embodied robots requires grounding object- and relation-centric language queries from a designated viewpoint. While a local semantic Gaussian map can support such grounding within one agent's observations, cooperative settings require this ability to remain effective after independently reconstructed maps are aligned and fused. In this setting, the referred target or its contextual landmark may come from another agent's observations, while spatial relations must still be interpreted from the querying robot's viewpoint. We formulate this problem as cooperative referring Gaussian grounding over fused maps, which requires geometric alignability, instance-level semantic comparability, and view-conditioned relation reasoning. Existing language-aware Gaussian methods mainly focus on single-map querying, whereas Gaussian registration methods optimize geometric or photometric alignment without preserving language-grounding-oriented semantic compatibility. We propose CoRef-GS, a cooperative referring Gaussian splatting framework. CoRef-GS constructs local open-vocabulary instance-aware Gaussian maps, then aligns partially overlapping maps with a cross-agent alignment module by geometric and semantic consistency, and grounds queries using a view-conditioned mask relation graph. We further introduce CoQuad-Ref, a dual-quadruped benchmark spanning both real-world and simulated indoor scenes. Experiments show that, on simulated scenes, CoRef-GS reduces the rotation error from 2.58° after coarse initialization to 0.15° after refinement, and improves real-world referring mIoU over ReferSplat from 52.6% to 68.8%. The established benchmark and source code will be publicly released at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/OmniMimic_Dynamics-completed_Motion_Augmentation_for_Multi-style_Omnidirectional_Quadruped_Locomotion|OmniMimic: Dynamics-completed Motion Augmentation for Multi-style Omnidirectional Quadruped Locomotion]]

![[assets/2609.20566_figure.png|800]]

- **arXiv**: [2609.20566](https://arxiv.org/abs/2609.20566)
- **PDF**: https://arxiv.org/pdf/2609.20566
- **详细分析**: [[20_Research/Papers/具身智能/OmniMimic_Dynamics-completed_Motion_Augmentation_for_Multi-style_Omnidirectional_Quadruped_Locomotion|OmniMimic: Dynamics-completed Motion Augmentation for Multi-style Omnidirectional Quadruped Locomotion]]
- **作者**: Sheng Wu, Guoqiang Zhao, Zhe Yang, Fei Teng, Zhikun Zhou, Yanlin Yang, Zheng Fang, Hong Zheng, Yaonan Wang, Kailun Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.0（加权：具身智能 2.7，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《OmniMimic: Dynamics-completed Motion Augmentation for Multi-style Omnidirectional Quadruped Locomotion》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：APT-RL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Animal demonstrations provide quadruped robots with natural and distinctive gait styles that are difficult to specify through hand-crafted rewards. However, their narrow directional coverage leaves little style-consistent supervision for backward, lateral, and turning commands. We present OmniMimic, a training framework that turns directionally limited animal demonstrations into a single multi-gait policy over target per-axis velocity ranges. OmniMimic first combines temporal reversal, constrained dynamics completion, and sagittal reflection to construct robot-specific kinematic and physical supervision beyond the observed directions. It then expands commands progressively from the demonstrated velocity distribution toward the target per-axis bounds, and uses a shared actor with soft-gated, gait-specialized residual experts to balance reusable locomotion skills with gait-specific corrections. Across four gaits in simulation, OmniMimic reduces mean foot-position RMSE at forward and backward reference velocities by 12.9% and velocity-tracking RMSE on a uniform Cartesian command grid by 63.1%, compared with the matched APEX baseline. The project page is at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Navi-Agent_Unlocalized_Monocular_Navigation_Agent|Navi-Agent: Unlocalized Monocular Navigation Agent]]

![[assets/2609.20388_figure.png|800]]

- **arXiv**: [2609.20388](https://arxiv.org/abs/2609.20388)
- **PDF**: https://arxiv.org/pdf/2609.20388
- **详细分析**: [[20_Research/Papers/具身智能/Navi-Agent_Unlocalized_Monocular_Navigation_Agent|Navi-Agent: Unlocalized Monocular Navigation Agent]]
- **作者**: Wenyuan Xie, Mengyang Hong, Yongzhong Wang, Yanbiao Ji, Yijin Zhou, Shaokai Wu, Shalayiding Sirejiding, Huayi Zhou, Yi-Chao Chen, Ma Ling, Yue Ding, Hongtao Lu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Navi-Agent: Unlocalized Monocular Navigation Agent》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ActionSet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Navigation in Continuous Environments (VLN-CE) requires an embodied agent to execute long-horizon instructions in unknown environments. Existing zero-shot VLN-CE systems typically maintain spatial states through geometric localization or coordinate-based representations. Recent geometry-constrained navigation removes depth and globally consistent coordinates, but maintaining persistent spatial awareness for place confirmation, progress verification, and recovery remains challenging. We present Navi-Agent, a zero-shot VLN-CE agent that constructs a coordinate-free spatial state from visual observations and executed motion histories. Navi-Agent organizes this state as a navigation topology, where nodes represent visual places and edges represent motion transitions. This representation enables observation-based approximate self-localization, task progress verification, and visual revisitation-based recovery. Navi-Agent performs closed-loop navigation by decomposing instructions into sub-goals, executing local visual navigation, and verifying visited places through the constructed spatial state. Experiments on zero-shot VLN-CE benchmark and real-world robot platforms show that Navi-Agent achieves state-of-the-art performance among geometry-constrained methods while remaining competitive with approaches relying on geometric localization.

</details>

---

### [[20_Research/Papers/具身智能/BinoGen_Scaling_egocentric_binocular_data_for_embodied_visual_perception_and_learning|BinoGen: Scaling egocentric binocular data for embodied visual perception and learning]]

![[assets/2609.19881_figure.png|800]]

- **arXiv**: [2609.19881](https://arxiv.org/abs/2609.19881)
- **PDF**: https://arxiv.org/pdf/2609.19881
- **详细分析**: [[20_Research/Papers/具身智能/BinoGen_Scaling_egocentric_binocular_data_for_embodied_visual_perception_and_learning|BinoGen: Scaling egocentric binocular data for embodied visual perception and learning]]
- **作者**: Chunpeng Li, Ya-tang Li
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《BinoGen: Scaling egocentric binocular data for embodied visual perception and learning》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ImageNet, LEGO-Net, ModelNet, ScanNet, SceneNet, ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied visual perception relies on temporally coherent visual experience accumulated through continuous engagement with the environment. However, collecting large-scale egocentric binocular observations together with dense annotations remains costly and difficult. Moreover, visual experience is shaped not only by the environment but also by the embodiment of the observer, including viewing height, field of view, binocular geometry, and motion through the scene. To address these challenges, we present BinoGen, an automated framework for generating large-scale, embodiment-aware egocentric binocular visual experiences in indoor environments. BinoGen jointly models environmental and observer variation through generative scene synthesis, probabilistic object instantiation, appearance randomization, stochastic trajectory generation, and configurable binocular camera setups. The framework produces synchronized binocular videos together with dense multimodal supervision, including depth maps, optical flow, surface normals, semantic maps, object coordinates, and camera poses. Using BinoGen, we construct a dataset comprising more than 20 million annotated images for supervised learning. We demonstrate two complementary utilities of BinoGen. First, incorporating BinoGen data consistently improves real-world visual perception, including depth estimation, object detection, and video object tracking. Second, paired human-inspired and mouse-inspired observations from the same environments enable controlled investigation of how observer embodiment affects perceptual learning. Embodiment-specific adaptation substantially improves performance, while joint training enables a single model to perform competitively across both embodiments. Together, these results demonstrate that large-scale, controllable visual experience can improve embodied perception...

</details>

---

### [[20_Research/Papers/具身智能/Feeling_Terrain_Before_Crossing_World_Models_for_Off-Road_Navigation|Feeling Terrain Before Crossing: World Models for Off-Road Navigation]]

![[assets/2609.19863_figure.png|800]]

- **arXiv**: [2609.19863](https://arxiv.org/abs/2609.19863)
- **PDF**: https://arxiv.org/pdf/2609.19863
- **详细分析**: [[20_Research/Papers/具身智能/Feeling_Terrain_Before_Crossing_World_Models_for_Off-Road_Navigation|Feeling Terrain Before Crossing: World Models for Off-Road Navigation]]
- **作者**: E-In Son, Dong-Wook Kim, Ji-Hoon Hwang, Kangsun Lee, Jisung Bae, Jung-Taak Kim, Seung-Woo Seo
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Feeling Terrain Before Crossing: World Models for Off-Road Navigation》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AstraNav-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigation world models plan by foresight, predicting the future that each candidate action sequence produces and selecting the best, rather than mapping observations to actions directly. Unlike urban settings where a predicted scene is a sufficient proxy, off-road navigation hinges on the robot--terrain interaction, so the prediction must cover not only what the camera will see but what the robot will feel. However, existing scene-focused models do not predict how much the robot will slip, tilt or shake along a planned trajectory. Proprioception captures these dynamics directly and, when used as input, improves the prediction of the physical future. We present Feel-WM, the first off-road navigation world model that conditions on proprioception and predicts what the robot will feel alongside what the camera will see. The physical future takes the form of a future proprioceptive state and a failure risk, both learned from the robot's own experience without human labels. The planner rolls out the physical future alongside the scene and weighs the predicted failure risk against goal similarity in a separable score. Experiments on real off-road data and in simulation demonstrate that Feel-WM outperforms visual-only navigation world models in open-loop planning and closed-loop rough-terrain navigation across wheeled and legged platforms. Deployed on a Husky on mountain trails, Feel-WM plans onboard, predicts rough ground ahead and steers around it, completing courses that an end-to-end policy fails.

</details>

---

### [[20_Research/Papers/强化学习/Region-Level_Policy_Optimization_for_Fine-grained_MLLM_Perception|Region-Level Policy Optimization for Fine-grained MLLM Perception]]

![[assets/2609.19745_figure.png|800]]

- **arXiv**: [2609.19745](https://arxiv.org/abs/2609.19745)
- **PDF**: https://arxiv.org/pdf/2609.19745
- **详细分析**: [[20_Research/Papers/强化学习/Region-Level_Policy_Optimization_for_Fine-grained_MLLM_Perception|Region-Level Policy Optimization for Fine-grained MLLM Perception]]
- **作者**: Yuheng Shi, Xiaohuan Pei, Minjing Dong, Chang Xu
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Region-Level Policy Optimization for Fine-grained MLLM Perception》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL, VQA, Vision-RL, ZoomBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-grained visual perception in MLLMs is commonly improved by raising the resolution, but the added visual tokens inflate vision-encoding and language-model prefilling costs. We show that the two operations underlying fine-grained perception, localizing the region of interest (RoI) and recognizing its content, have different resolution requirements. In a controlled diagnostic, localization tolerates roughly 3 to 4 times stronger token compression than recognition, which motivates localizing from a coarse view and concentrating resolution on the selected evidence. Decoding coordinates with the MLLM can be trained end-to-end from answers, but costs a full model pass per query and depends on grounding ability. A lightweight proposal network distilled from the model's attention is fast, but inherits the noise of its attention targets. The RoI from the proposal network reaches the answer through a discrete region choice, so its faithfulness to the answer cannot supervise the network. We therefore optimize the proposal network with region-level reinforcement learning, which we call Vision-RL2. It treats coherent regions as actions, and a frozen MLLM reader scores each one by how its removal changes the answer likelihood. Complementary subtractive and additive objectives suppress distracting proposals and recover missing evidence, updating only the predictor without region annotations, response sampling, or reasoning trajectories. The refined proposal further enables a sparse encoding that magnifies evidence and excludes background tokens. Across six fine-grained benchmarks and four MLLM backbones, Vision-RL2 improves accuracy over the base model at every token budget and surpasses its largest-budget accuracy with about 4 times fewer visual tokens. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Patch_Removal_Persistent_Adversarial_Effects_in_Vision-Language-Action_Policies|Beyond Patch Removal: Persistent Adversarial Effects in Vision-Language-Action Policies]]

![[assets/2609.19669_figure.png|800]]

- **arXiv**: [2609.19669](https://arxiv.org/abs/2609.19669)
- **PDF**: https://arxiv.org/pdf/2609.19669
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Patch_Removal_Persistent_Adversarial_Effects_in_Vision-Language-Action_Policies|Beyond Patch Removal: Persistent Adversarial Effects in Vision-Language-Action Policies]]
- **作者**: Enhao Wu, Fusen Guo, Yuxin Cao, Ziyang Lyu, Lin Li, Wei Song
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Security

#### 研究背景与动机

《Beyond Patch Removal: Persistent Adversarial Effects in Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adversarial patches to Vision-Language-Action (VLA) policies can cause both immediate action corruption and persistent state effects that remain after the patch is removed. Existing evaluations largely focus on continuous attacks and do not separate these two effects. We introduce a state-restoration protocol that removes the patch at matched action-chunk boundaries and measures subsequent recoverability under the same remaining step budget. Clean, random-patch, deviation-matched, and fixed-direction controls distinguish adversarial effects from occlusion, action-error magnitude, and directional persistence. We also evaluate a recovery adapter trained on attack-induced states under controlled intervention latency. On OpenVLA-OFT with EDPA attacks, only 36.2% of LIBERO-Long episodes remain recoverable after five chunks, compared with 89.9% and 87.0% for the deviation-matched and fixed-direction controls. Similar persistent effects are observed on autoregressive OpenVLA. The recovery adapter improves recovery from 7.7% to 47.4% at one-chunk latency, but its benefit decreases substantially with delayed intervention. These results show that adversarial effects can persist after patch removal and that timely intervention is critical for recovery.

</details>

---

### [[20_Research/Papers/机器人/Selective_Cotton_Boll_Localization_for_Robotic_Harvesting_Evaluation_of_Deep_Learning_Vision_Models_Under_Field_Conditions|Selective Cotton Boll Localization for Robotic Harvesting: Evaluation of Deep Learning Vision Models Under Field Conditions]]

![[assets/2609.19592_figure.png|800]]

- **arXiv**: [2609.19592](https://arxiv.org/abs/2609.19592)
- **PDF**: https://arxiv.org/pdf/2609.19592
- **详细分析**: [[20_Research/Papers/机器人/Selective_Cotton_Boll_Localization_for_Robotic_Harvesting_Evaluation_of_Deep_Learning_Vision_Models_Under_Field_Conditions|Selective Cotton Boll Localization for Robotic Harvesting: Evaluation of Deep Learning Vision Models Under Field Conditions]]
- **作者**: Thevathayarajh Thayananthan, Xin Zhang, Isuru Laddusinghe Badu, Jonathan Harjono, Glen C. Rains, Beiwen Li, Leonardo M. Bastos, Nuwan K. Wijewardane, Vitor S. Martins
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Selective Cotton Boll Localization for Robotic Harvesting: Evaluation of Deep Learning Vision Models Under Field Conditions》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study developed and evaluated a deep-learning-based perception framework for selective robotic cotton picking. The dataset contained 1,008 annotated field images collected using three cameras under varying natural lighting and weather conditions. Object-detection models from the YOLOv8 through YOLOv13 families were evaluated using their default configurations, while segmentation performance was assessed using YOLOv8-seg, YOLOv11-seg, YOLOv12-seg, the Segment Anything Model (SAM), SAMv2.1, FastSAM, and Grounded-SAM with the Recognize Anything Model (RAM). Among the detection models, GELAN-s achieved the most favorable balance between mean average precision (mAP) and inference speed, obtaining an mAP of 86.1%, precision of 81.6%, recall of 76.6%, and an F1-score of 79.0%, with an average inference time of 42.3 ms per image. Among the direct segmentation models, YOLOv12-m-seg provided the most favorable balance between AP@0.5 and FPS, achieving a segmentation AP@0.5 of 83.7% with an inference time of 20.4 ms per image. In the detection-prompted segmentation approach, bounding-box prompts generated by GELAN-s improved the localization of cotton bolls for SAM and SAMv2.1, while SAMv2.1 Tiny consistently outperformed FastSAM and Grounded-SAM with RAM. In the area-based evaluation against manually annotated segmentation masks, YOLOv12-m-seg achieved an $R^2$ value of 0.966, compared with 0.860 for GELAN-s + SAMv2.1 Tiny. Field experiments conducted using a UR5e robotic manipulator, a custom end-effector, and a ZED2i stereo camera further validated the effectiveness of the YOLOv12-m-seg model for real-time cotton boll detection, segmentation, and selective picking under varying confidence levels. These results demonstrate that YOLOv12-m-seg provides an efficient perception model for robotic cotton harvesting and has strong potential for field deployment.

</details>

---

### [[20_Research/Papers/具身智能/VABench_Measuring_Embodied_Spatial_Intelligence_through_Visual_Demonstrations,_Active_Perception,_and_Metric_Control|VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control]]

![[assets/2609.19554_figure.png|800]]

- **arXiv**: [2609.19554](https://arxiv.org/abs/2609.19554)
- **PDF**: https://arxiv.org/pdf/2609.19554
- **详细分析**: [[20_Research/Papers/具身智能/VABench_Measuring_Embodied_Spatial_Intelligence_through_Visual_Demonstrations,_Active_Perception,_and_Metric_Control|VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control]]
- **作者**: Zhongbo Zhang, Jiayi Jin, Yifan Wang, Zaibin Zhang, Haiwen Diao, Lijun Wang, Huchuan Lu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《VABench: Measuring Embodied Spatial Intelligence through Visual Demonstrations, Active Perception, and Metric Control》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CV-Bench, ESI-Bench, EmbodiedBench, GQA, IMBench, ManipBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial intelligence requires more than describing object locations. Under incomplete observation, models must identify and acquire missing evidence, interpret it in a common spatial frame, and act on it. We introduce VA-Bench to evaluate the complete observe-reason-act-revise loop. General-purpose MLLMs learn procedural context from RGB-only demonstrations, actively select camera viewpoints, issue metric Cartesian commands, and revise them from execution feedback. Models receive no privileged object poses, oracle trajectories, or learned action heads. A fixed model-agnostic controller executes only model-specified targets. VA-Bench contains 14 base task families (11 single-arm and three dual-arm), seven held-out geometry/layout variants, and a long-horizon five-object composition track. We evaluate 12 primary model conditions in three independent runs over the same 20 physically verified seeds per base task, reporting terminal success, nine trajectory-level behavioral diagnostics, and subtask progress. First, the best-performing model scores 100.0% on target localization and 78.9% on spatial relations in the annotated run. Its three-run macro-average task success is only 53.93+/-3.17%. Second, active camera control significantly improves task success over passive multi-view observation. In one matched comparison, success rises from 27.86% to 57.50%. Third, held-out geometric transfer can reduce task success by over 30 percentage points. No model completes a strict long-horizon episode, despite substantial partial progress. VA-Bench thus tests whether general-purpose MLLMs can turn visual demonstrations and actively acquired evidence into successful embodied action.

</details>

---

### [[20_Research/Papers/机器人/PerSeM_Persistent_Semantic_Memory_for_Long-Horizon_Open-Vocabulary_UAV_Mapping|PerSeM: Persistent Semantic Memory for Long-Horizon Open-Vocabulary UAV Mapping]]

![[assets/2609.19542_figure.png|800]]

- **arXiv**: [2609.19542](https://arxiv.org/abs/2609.19542)
- **PDF**: https://arxiv.org/pdf/2609.19542
- **详细分析**: [[20_Research/Papers/机器人/PerSeM_Persistent_Semantic_Memory_for_Long-Horizon_Open-Vocabulary_UAV_Mapping|PerSeM: Persistent Semantic Memory for Long-Horizon Open-Vocabulary UAV Mapping]]
- **作者**: Saurbh Singh Jamwal, Ganesh Ramakrishnan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《PerSeM: Persistent Semantic Memory for Long-Horizon Open-Vocabulary UAV Mapping》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：K-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-vocabulary segmentation enables rich semantic perception for UAVs, but frame-wise predictions can remain temporally inconsistent across repeated observations and changing viewpoints. We present PerSeM, a training-free persistent semantic memory framework for long-horizon open-vocabulary UAV mapping. PerSeM associates frame-wise semantic observations with persistent world-space voxels and constructs a majority-based semantic memory, which is conservatively refined through history-preserving spatial refinement, trust-aware replay, and context-guided verification. Experiments on the Forest and UAVScenes benchmarks show that persistent 3D memory provides substantial gains in semantic correctness and temporal stability over frame-wise predictions. Beyond this strong persistent-memory baseline, PerSeM provides consistent additional improvements, improving both semantic accuracy and temporal stability across all five evaluated UAVScenes sequences. Analysis using regions identified independently of the final PerSeM predictions further shows that these gains are concentrated in semantically difficult and temporally unstable regions, where majority-based memory is most likely to remain uncertain. These results demonstrate that persistent 3D aggregation provides a strong foundation for long-horizon semantic mapping, while conservative refinement of uncertain memory states can provide additional improvements without retraining or additional neural-network inference.

</details>

---

### [[20_Research/Papers/机器人/AMB3R-SLAM_Kilometer-scale_SLAM_with_Hierarchical_Backend|AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend]]

![[assets/2609.19518_figure.png|800]]

- **arXiv**: [2609.19518](https://arxiv.org/abs/2609.19518)
- **PDF**: https://arxiv.org/pdf/2609.19518
- **详细分析**: [[20_Research/Papers/机器人/AMB3R-SLAM_Kilometer-scale_SLAM_with_Hierarchical_Backend|AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend]]
- **作者**: Hengyi Wang, Lourdes Agapito
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《AMB3R-SLAM: Kilometer-scale SLAM with Hierarchical Backend》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present AMB3R-SLAM, a real-time monocular SLAM system capable of reconstructing kilometer-scale trajectories over 10k frames on a single consumer-grade GPU. Our model couples a lightweight front-end for low-latency online tracking with a hierarchical backend that progressively enforces local, mid-level, and global consistency. By avoiding bundle adjustment that relies on the static world assumption, our system naturally handles complex dynamic scenes out of the box. Furthermore, we demonstrate that our method can be extended to leverage stereo, RGB-D, and LiDAR as additional inputs. AMB3R-SLAM achieves strong camera tracking performance across 9 datasets, reducing the absolute trajectory error (ATE) of previous state-of-the-art methods on VBR and Oxford Spires by over 70%. With additional LiDAR input, our model further reduces ATE to sub-meter level on KITTI and VBR datasets.

</details>

---

### [[20_Research/Papers/大模型/SCOUT_Sim-to-Real_Text-Based_Person_Retrieval_by_Embedding-Space_Prediction_over_Frozen_Video_Features|SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features]]

![[assets/2609.19483_figure.jpg|800]]

- **arXiv**: [2609.19483](https://arxiv.org/abs/2609.19483)
- **PDF**: https://arxiv.org/pdf/2609.19483
- **详细分析**: [[20_Research/Papers/大模型/SCOUT_Sim-to-Real_Text-Based_Person_Retrieval_by_Embedding-Space_Prediction_over_Frozen_Video_Features|SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features]]
- **作者**: Abdarahmane Traoré, Andy Couturier, Éric Hervet
- **cs 子类**: cs.CV, cs.IR
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 1.2，大模型 0.3）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《SCOUT: Sim-to-Real Text-Based Person Retrieval by Embedding-Space Prediction over Frozen Video Features》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-based person retrieval under a sim-to-real gap (synthetic training data, a real-image gallery) is usually tackled with costly fine-tuned cross-encoders. We ask whether a frozen-encoder system can compete. We present SCOUT, which casts cross-modal retrieval as prediction in embedding space. A trainable predictor maps the patch tokens of a frozen video encoder into the embedding space of a frozen text encoder under a bidirectional InfoNCE objective, and no encoder is fine-tuned in the base model. The video encoder is V-JEPA, the text encoder is EmbeddingGemma, and the predictor is initialized from a Qwen3.5-0.8B decoder. We make three findings. First, the best frozen text encoder is simply the one whose geometry best matches the video features. A training-free alignment score ranks three candidate text encoders in the same order as their retrieval accuracy on our held-out split (Spearman $\rho = 1.0$); a fourth, LLM-based encoder shows the rule is metric-dependent, holding for a neighborhood-overlap score ($\rho = 0.8$) but not for a linear probe ($\rho = -0.2$). Second, two precision-targeted levers, parameter-efficient ExPLoRA adaptation of the video encoder and a training-free attribute-decomposed reranker built on a vision-language model, improve the top-rank precision that otherwise limits the frozen system, adding 2.2 points of leaderboard R@1. Third, a local-versus-public calibration study explains which interventions transfer to the real domain. On AI City Challenge 2026 Track 4 the full retrieve-fuse-rerank system reaches 84.25 mAP@10 on the final leaderboard, while a single frozen model submitted alone reaches 60.63. Our trained components cost about 95 GPU-hours. CMP, the dataset authors' fine-tuned cross-encoder that trains for sixteen GPU-days, is one fusion member of the full system, not an alternative. Code and annotations: this https URL

</details>

---
