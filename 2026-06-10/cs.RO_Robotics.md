# cs.RO | Robotics | 2026-06-10

#arxiv #ComputerScience

**论文数**: 26

### [[20_Research/Papers/强化学习/TacForeSight_Force-Guided_Tactile_World_Model_for_Contact-Rich_Manipulation|TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation]]

![[assets/2606.11184_figure.png|800]]

- **arXiv**: [2606.11184](https://arxiv.org/abs/2606.11184)
- **PDF**: https://arxiv.org/pdf/2606.11184
- **详细分析**: [[20_Research/Papers/强化学习/TacForeSight_Force-Guided_Tactile_World_Model_for_Contact-Rich_Manipulation|TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation]]
- **作者**: Yujie Zang, Yuhang Zheng, Xian Nie, Yupeng Zheng, Shuai Tian, Songen Gu, Chen Gao, Zining Wang, Shuicheng Yan, Wenchao Ding
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 1，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《TacForeSight: Force-Guided Tactile World Model for Contact-Rich Manipulation》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TacVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation requires robots to continuously perceive and regulate evolving physical interactions under dynamic contact transitions or complex surface geometries. Recent imitation learning methods improve contact-aware control by incorporating tactile or force feedback, but they rarely model the asymmetric spatiotemporal roles of global force and local tactile sensing. To address this, we propose TacForeSight, a lightweight force-conditioned tactile foresight framework for real-time manipulation. The core component is TacForceWM, a tactile world model that predicts short-horizon tactile latent dynamics from dual-finger tactile observations conditioned on high-frequency wrist force and torque signals. Another key component, the Predictive Tactile-Conditioned Policy, leverages the predicted latents as anticipatory contact priors, models the current-to-future tactile evolution via cross-attention, and adaptively fuses visuo-tactile features through a tactile-guided gating module. By forecasting purely within a compact latent space, TacForeSight enables proactive contact reasoning with efficient real-time inference suitable for high-frequency manipulation control. Real-robot experiments on five representative tasks and three in-process perturbation settings show that TacForeSight consistently outperforms existing baselines, particularly under dynamic contact disturbances. All models and datasets will be made publicly available on the project website at https://tacforesight.github.io/ProjectPage.

</details>

---

### [[20_Research/Papers/具身智能/JOIN_Anchor-Grasp-Conditioned_Joining_via_Opposition,_Inference,_and_Navigation_for_Bimanual_Assistive_Manipulation|JOIN: Anchor-Grasp-Conditioned Joining via Opposition, Inference, and Navigation for Bimanual Assistive Manipulation]]

![[assets/2606.11151_figure.png|800]]

- **arXiv**: [2606.11151](https://arxiv.org/abs/2606.11151)
- **PDF**: https://arxiv.org/pdf/2606.11151
- **详细分析**: [[20_Research/Papers/具身智能/JOIN_Anchor-Grasp-Conditioned_Joining_via_Opposition,_Inference,_and_Navigation_for_Bimanual_Assistive_Manipulation|JOIN: Anchor-Grasp-Conditioned Joining via Opposition, Inference, and Navigation for Bimanual Assistive Manipulation]]
- **作者**: Drake Moore, Matt Cheng, Xiang Zhi Tan, Taşkın Padır
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《JOIN: Anchor-Grasp-Conditioned Joining via Opposition, Inference, and Navigation for Bimanual Assistive Manipulation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assistive mobility and manipulation platforms have received increasing attention as a means of restoring independence to individuals with disabilities. While effective for many basic activities of daily living (ADLs), a significant percentage of everyday tasks such as opening a jar, pouring a liquid, lifting a tray, or basic meal preparation, is fundamentally bimanual and remains out of reach for any single-arm system. Adding a second arm to a wheelchair is impractical, due to the additional power draw, cost, and the loss of space required for transfers and mobility. We instead propose a heterogeneous, on-demand bimanual system, in which a wheelchair-mounted anchor arm is joined when needed by a summoned mobile manipulator that serves as a complement arm. The central technical problem, which we call bimanual joining, is conditional: the anchor has already committed to a grasp, and the complement arm must choose where to stand and what to grasp to complete the task. We formulate bimanual joining as a three-phase decomposition (plan, drive, grasp) and show that a vision-language model (VLM), coupled with standard geometric tools, provides task-level knowledge sufficient to solve a representative class of bimanual ADLs. Our system JOIN, contributes (i) a wheelchair-referenced opposition score, and (ii) task-conditioned directional manipulability. We evaluate JOIN on a Kinova Gen3 anchor and a Hello Robot Stretch~3 complement on representative same-object and different-object tasks. JOIN accomplished more attempts (19/20) than state-of-the-art methods (14/20) and required markedly less correction by the operator.

</details>

---

### [[20_Research/Papers/具身智能/EM-Fall_Embodied_mmWave_Sensing_for_Day-and-Night_Fall_Detection_on_Humanoid_Robots|EM-Fall: Embodied mmWave Sensing for Day-and-Night Fall Detection on Humanoid Robots]]

![[assets/2606.11109_figure.png|800]]

- **arXiv**: [2606.11109](https://arxiv.org/abs/2606.11109)
- **PDF**: https://arxiv.org/pdf/2606.11109
- **详细分析**: [[20_Research/Papers/具身智能/EM-Fall_Embodied_mmWave_Sensing_for_Day-and-Night_Fall_Detection_on_Humanoid_Robots|EM-Fall: Embodied mmWave Sensing for Day-and-Night Fall Detection on Humanoid Robots]]
- **作者**: Yanshuo Lu, Yuxuan Hu, Shenghai Yuan, Xinyu Zhou, Kuangji Zuo, Bofan Lyu, XiChen Yuan, Jianfei Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.2（加权：具身智能 2.7，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《EM-Fall: Embodied mmWave Sensing for Day-and-Night Fall Detection on Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Falls are one of the leading causes of injury and hospitalization among elderly individuals, making reliable fall awareness an essential capability for safety monitoring in residential environments. However, existing fall detection systems often rely on wearable devices or fixed sensing installations, which may suffer from low user compliance, limited spatial coverage, or degraded performance under occlusion and poor lighting conditions. In this work, we propose \textbf{EM-Fall}, an embodied fall detection framework deployed on a mobile humanoid robot. The system integrates millimeter-wave (mmWave) sensing with robotic mobility, allowing the robot to actively adjust its sensing viewpoint and maintain target observability across rooms and under occlusion. To address interference in complex residential environments, including pet motion and multipath artifacts, we design a human-centered perception pipeline combined with lightweight temporal modeling to capture motion evolution before, during, and after fall events. We evaluate the proposed system across eight real indoor environments with four participants and construct an in-home mmWave fall detection dataset. Experimental results show that the embodied mobile sensing paradigm improves monitoring continuity and maintains robust fall detection performance under diverse environmental conditions. The proposed framework provides a practical solution for robot-assisted safety monitoring in home environments.

</details>

---

### [[20_Research/Papers/机器人/Generation_of_Diverse_and_Functional_Robot_Designs_using_Superquadrics_Parametrisation_and_Quality-Diversity|Generation of Diverse and Functional Robot Designs using Superquadrics Parametrisation and Quality-Diversity]]

![[assets/2606.11037_figure.png|800]]

- **arXiv**: [2606.11037](https://arxiv.org/abs/2606.11037)
- **PDF**: https://arxiv.org/pdf/2606.11037
- **详细分析**: [[20_Research/Papers/机器人/Generation_of_Diverse_and_Functional_Robot_Designs_using_Superquadrics_Parametrisation_and_Quality-Diversity|Generation of Diverse and Functional Robot Designs using Superquadrics Parametrisation and Quality-Diversity]]
- **作者**: Leni Le Goff, Simon Smith, Emma Hart
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Generation of Diverse and Functional Robot Designs using Superquadrics Parametrisation and Quality-Diversity》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative design of robots requires navigating a vast search-space, encompassing physical configurations and behavioural parameters. Evolutionary Algorithms (EAs) have shown promising results, but often converge prematurely to a small set of sub-optimal designs. Most EAs fail to maintain sufficient diversity in the population that would allow the discovery of distinct functional robots. To counter premature convergence, we introduce a superquadrics-based representation (SQs) for robot bodies. SQs are interpretable, compact and computationally efficient mathematical representations of 3D geometrical shapes that can be tuned to specific design-spaces. To encourage morphological diversity, we combine this representation with a quality-diversity (QD) algorithm (MAP-Elites). We compare SQs and Compositional Pattern Producing Networks representations as generators of morphologies, combining them with standard EAs and MAP-Elites. In two test environments, we find that using SQs to generate morphology in conjunction with the MAP-Elites algorithm reaches the highest QD-score across both environments, maximising diversity of design and functionality of generated robots. The findings highlight the benefits of using a compact and interpretable geometric representation for exploring a complex design-space and suggest that combining SQs with an explicit diversity mechanism increases the quality and number of designs generated.

</details>

---

### [[20_Research/Papers/机器人/Multi-UAV_Active_Sensing_with_Information_Gain-based_Planning_and_Belief_Fusion|Multi-UAV Active Sensing with Information Gain-based Planning and Belief Fusion]]

![[assets/2606.10986_figure.png|800]]

- **arXiv**: [2606.10986](https://arxiv.org/abs/2606.10986)
- **PDF**: https://arxiv.org/pdf/2606.10986
- **详细分析**: [[20_Research/Papers/机器人/Multi-UAV_Active_Sensing_with_Information_Gain-based_Planning_and_Belief_Fusion|Multi-UAV Active Sensing with Information Gain-based Planning and Belief Fusion]]
- **作者**: S. Habibi, L. Marques
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Multi-UAV Active Sensing with Information Gain-based Planning and Belief Fusion》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicles (UAVs) are increasingly used for active sensing and information gathering in spatially distributed environments. Their performance, however, is constrained by limited flight time, sensing uncertainty, and the trade-off between spatial coverage and observation accuracy. This paper presents a real-world validation of a multi-UAV active sensing framework for probabilistic binary terrain mapping, with precision agriculture used as the application case. The environment is represented as a probabilistic belief map, where spatial dependencies are modeled through a factor-graph formulation. UAV decision making is guided by Information Gain based Informative Path Planning (IGbIPP), and the approach is compared with Random Walk and Sweep coverage path planning baselines using both synthetic terrains and real UAV-derived agricultural imagery. The study also evaluates spatial correlation weights and several probabilistic belief-fusion rules for multi-UAV information sharing. Results show that IGbIPP reduces entropy and mapping error more effectively than the baselines, while a wider field of view improves real-world coverage and map accuracy. The results further show that simple equal or biased spatial weights can be more robust than adaptive weights, and that Bayesian, log-odds, and Dempster--Shafer fusion achieve the best cooperative mapping performance. These findings highlight the importance of uncertainty-driven planning, sensing geometry, spatial modeling, and probabilistic fusion for real-world UAV-based active sensing.

</details>

---

### [[20_Research/Papers/具身智能/AllDayNav_Lifelong_Navigation_via_Real-World_Reinforcement_Learning|AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning]]

![[assets/2606.10927_figure.png|800]]

- **arXiv**: [2606.10927](https://arxiv.org/abs/2606.10927)
- **PDF**: https://arxiv.org/pdf/2606.10927
- **详细分析**: [[20_Research/Papers/具身智能/AllDayNav_Lifelong_Navigation_via_Real-World_Reinforcement_Learning|AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning]]
- **作者**: Hang Yin, Yinan Liang, Jiazhao Zhang, Jiahang Liu, Minghan Li, Zhizheng Zhang, He Wang
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.6，大模型 0.2，强化学习 0.8，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《AllDayNav: Lifelong Navigation via Real-World Reinforcement Learning》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, SERL, SimpleVLA-RL, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lifelong embodied navigation in dynamic environments requires robots to form persistent scene understanding from fragmentary observations, which remains difficult for existing methods that rely on explicit maps or scene graphs and struggle to generalize beyond structured settings. We propose AllDayNav, a lifelong self-learning navigation framework that implicitly encodes scene dynamics into the billion-scale parameters of a large model via reinforcement learning, powered by a self-evolving multimodal memory that maintains and updates visual keyframes, semantic descriptions, and temporal context while autonomously generating open-vocabulary instructions, image goals, and structured rewards. Experiments in both synthetic and real-world environments across cross-room, cross-episode, and cross-task scenarios show that AllDayNav achieves success rates approaching $100\%$ and consistently surpasses strong map-based, VLM, and RL baselines in path efficiency and robustness, demonstrating implicit, memory-driven reinforcement learning as a scalable alternative to explicit mapping for reliable lifelong navigation.

</details>

---

### [[20_Research/Papers/具身智能/AgniNav_Configuration-Driven_Cross-Embodiment_Local_Planning_for_Robot_Navigation|AgniNav: Configuration-Driven Cross-Embodiment Local Planning for Robot Navigation]]

![[assets/2606.10903_figure.png|800]]

- **arXiv**: [2606.10903](https://arxiv.org/abs/2606.10903)
- **PDF**: https://arxiv.org/pdf/2606.10903
- **详细分析**: [[20_Research/Papers/具身智能/AgniNav_Configuration-Driven_Cross-Embodiment_Local_Planning_for_Robot_Navigation|AgniNav: Configuration-Driven Cross-Embodiment Local Planning for Robot Navigation]]
- **作者**: Tianhao Zang, Siwei Cheng, Haidong Huang, Shanze Wang, Wei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.3（加权：具身智能 1.8，机器人 1.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《AgniNav: Configuration-Driven Cross-Embodiment Local Planning for Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular local navigation is attractive for lightweight robots, but existing vision-based policies often couple perception to a specific body, camera height, and footprint, making transfer from wheeled bases to legged platforms dependent on retraining or active depth hardware. This paper introduces AgniNav, a configuration-driven local navigation framework that standardizes cross-embodiment transfer at the collision-envelope level. Each robot is specified by a measurable four-parameter safety envelope: collision-relevant height, front length, rear length, and half width. The height parameter conditions an image-to-scan network to predict a one-dimensional, collision-relevant pseudo-laserscan from a monocular color image, while the remaining footprint parameters configure a dimension-aware local planner for collision checking. Training uses height-conditioned column-minimum scan labels generated from paired color-depth data, allowing the same image to supervise different safety envelopes without collecting robot-specific data. To the best of our knowledge, AgniNav is the first monocular local-navigation framework that jointly conditions perception and planning on a shared collision-envelope configuration for zero-retraining deployment across wheeled, quadruped, and humanoid platforms. Real-robot experiments on a Turtlebot2, Unitree Go2, and Accelerated Evolution K1 achieve 39/40, 18/20, and 18/20 successes with 0/40, 1/20, and 2/20 collisions, respectively, while running at 30 Hz on Jetson Orin.

</details>

---

### [[20_Research/Papers/具身智能/MV-Actor_Aligning_Multi-View_Semantics_and_Spatial_Awareness_for_Bimanual_Manipulation|MV-Actor: Aligning Multi-View Semantics and Spatial Awareness for Bimanual Manipulation]]

![[assets/2606.10899_figure.png|800]]

- **arXiv**: [2606.10899](https://arxiv.org/abs/2606.10899)
- **PDF**: https://arxiv.org/pdf/2606.10899
- **详细分析**: [[20_Research/Papers/具身智能/MV-Actor_Aligning_Multi-View_Semantics_and_Spatial_Awareness_for_Bimanual_Manipulation|MV-Actor: Aligning Multi-View Semantics and Spatial Awareness for Bimanual Manipulation]]
- **作者**: Yinchen Tian, Huan Li, Muyao Peng, Xi Wang, Yan Wang, You Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《MV-Actor: Aligning Multi-View Semantics and Spatial Awareness for Bimanual Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation has been widely applied in industrial scenarios. Compared with single-arm manipulation, bimanual manipulation is equipped with multiple cameras to capture information from different viewpoints. However, existing multi-view policies encode each view independently or fuse view features shallowly, resulting in limited sharing semantic perception and unreliable spatial awareness. In this paper, we propose \textbf{MV-Actor}, a multi-view perception framework that builds a unified semantic-spatial representation for bimanual manipulation. First, MV-Actor performs Multi-view Semantic Interaction to share semantic perception across views. Then it uses Semantic-Spatial Token Interaction to ground visual semantics with feed-forward reconstruction model features and acquire reliable spatial awareness. Finally, a Guided Metric Depth Repair module refines degraded sensor depth to provide more reliable metric anchors under consumer-grade depth noise. In simulation experiments conducted on the PerAct2 bimanual benchmark, MV-Actor achieves a state-of-the-art average success rate of 87.8\%. In real-world evaluations with more frequent viewpoint changes and unstable consumer-grade depth, MV-Actor outperforms both RGB and RGB-D baselines, further demonstrating the benefit of sharing semantic perception and reliable spatial awareness for bimanual manipulation.

</details>

---

### [[20_Research/Papers/具身智能/GUIDE_Goal-Initialized_Directional_Understanding_for_End-to-End_Visual_Navigation|GUIDE: Goal-Initialized Directional Understanding for End-to-End Visual Navigation]]

![[assets/2606.10832_figure.png|800]]

- **arXiv**: [2606.10832](https://arxiv.org/abs/2606.10832)
- **PDF**: https://arxiv.org/pdf/2606.10832
- **详细分析**: [[20_Research/Papers/具身智能/GUIDE_Goal-Initialized_Directional_Understanding_for_End-to-End_Visual_Navigation|GUIDE: Goal-Initialized Directional Understanding for End-to-End Visual Navigation]]
- **作者**: Liang Wang, Jin Jin, KanZhong Yao, YiBin Wu, Fangqiang Ding, Jin Wang, Jun Wu, Zhe Sun, Qiuguo Zhu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《GUIDE: Goal-Initialized Directional Understanding for End-to-End Visual Navigation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning-based visual navigation for legged robots typically relies on continuous goal updates from hierarchical state estimation to provide a persistent directional reference. This reliance incurs additional sensory and computational overhead and deviates from fully end-to-end mobile autonomy. Furthermore, under partial observability, policies are prone to learn myopic behaviors, easily becoming trapped in dead ends and complex structural layouts. To address these limitations, we investigate a goal-initialized navigation setting, where the target is provided only once at the beginning of an episode, requiring the robot to operate based on intrinsic spatial memory without subsequent goal updates from external modules. In this work, we propose GUIDE, a fully end-to-end reinforcement learning framework designed to cultivate internal directional awareness. Specifically, GUIDE incorporates a spatial anchor predictor that leverages multi-frequency proprioceptive history to extract egomotion representations, thereby maintaining a persistent long-horizon spatial context for navigation. Concurrently, it utilizes raw depth streams to perceive local environmental geometry. We evaluate the proposed framework across both simulation and real-world scenarios on a quadruped robot. Experiments show that GUIDE learns reliable egomotion and directional awareness, enabling a fully end-to-end deployed policy to safely navigate through dense clutter and structured mazes without subsequent goal guidance or prior maps.

</details>

---

### [[20_Research/Papers/大模型/Bridging_Semantics_and_Physical_Execution_A_Neuro-Symbolic_Framework_for_Multi-Pair_Robotic_Assembly|Bridging Semantics and Physical Execution: A Neuro-Symbolic Framework for Multi-Pair Robotic Assembly]]

![[assets/2606.10808_figure.png|800]]

- **arXiv**: [2606.10808](https://arxiv.org/abs/2606.10808)
- **PDF**: https://arxiv.org/pdf/2606.10808
- **详细分析**: [[20_Research/Papers/大模型/Bridging_Semantics_and_Physical_Execution_A_Neuro-Symbolic_Framework_for_Multi-Pair_Robotic_Assembly|Bridging Semantics and Physical Execution: A Neuro-Symbolic Framework for Multi-Pair Robotic Assembly]]
- **作者**: Xinyi Li, Aiguo Song, Linhu Wei, Huijun Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Bridging Semantics and Physical Execution: A Neuro-Symbolic Framework for Multi-Pair Robotic Assembly》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL, PEARL, SHaRe-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-pair robotic assembly in unstructured environments faces spatial interference and contact uncertainties. Existing paradigms fail to bridge cognitive decision-making and physical execution, as they either encounter state-space explosion and knowledge bottlenecks or suffer from logical hallucinations and topological conflicts. We propose an end-to-end neuro-symbolic framework that solves the challenge hierarchically: generating optimal subgraphs for each pair, decoupling generality from edge cases, and then resolving cross-pair interferences. Given an eye-on-hand RGB-D assembly scene, the framework extracts semantic instance identity and state while quantifying the scene for divergence calculation. For each pair, optimal subgraph is generated via LLM using barely basic actions to mitigate hallucinations. Supportive actions for edge cases are reasoned and inserted with a lightweight discriminator. Driven by the divergence between the quantified baseline and current scene, it is easily extensible at low cost. Augmented subgraphs are topologically coordinated into global sequences while preserving internal behavioral coherence. Dynamic behavior trees embedding atomic skills close the force-aware execution loop. Offline evaluation on 100 real-world scenes achieves 97.00% global executability, outperforming classical and state-of-the-art planners. Real-robot deployment on a UR3 arm attains 90% success rate with 0.5 mm tolerance under strong interference, demonstrating a unified and verifiable solution for complex autonomous assembly.

</details>

---

### [[20_Research/Papers/机器人/ros2probe_Non-intrusive,_Kernel-selective_Observability_for_Robot_Operating_System_2_Middleware|ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware]]

![[assets/2606.10746_figure.png|800]]

- **arXiv**: [2606.10746](https://arxiv.org/abs/2606.10746)
- **PDF**: https://arxiv.org/pdf/2606.10746
- **详细分析**: [[20_Research/Papers/机器人/ros2probe_Non-intrusive,_Kernel-selective_Observability_for_Robot_Operating_System_2_Middleware|ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware]]
- **作者**: Jisang Yu, Sanghoon Lee, Yeonwoo Choi, Kyung-Joon Park
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《ros2probe: Non-intrusive, Kernel-selective Observability for Robot Operating System 2 Middleware》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot Operating System 2 (ROS 2), the de facto standard middleware framework for robots, runs each robot as a graph of nodes communicating over the Data Distribution Service (DDS), a publish/subscribe substrate. Observing this inter-node communication in real time is essential to robot development, yet it has a price. A tool can receive data only by joining the DDS domain as a subscriber that discovery has matched to the publisher, so observing folds the tool into the system it measures and perturbs it. We define this protocol-inherent perturbation as the observer's probe effect. It inflates the discovery plane, adds deserialization cost on the observer, makes the loss it reports diverge from what the subscriber actually received, and near saturation displaces the subscriber's messages. The only escape, capturing all wire traffic passively, discards ROS 2 message semantics and scales with total traffic, not what is observed. We present ros2probe, a non-intrusive observation framework that removes the probe effect. It reconstructs the full ROS 2 communication state from the domain's discovery packets at no bandwidth cost, then drives an in-kernel filter restricted to the topics the user asks for, lifting only those packets at minimal cost and observing what the real subscriber receives. Its interfaces and recordings match the standard ROS 2 tools. Across three hardware platforms (laptop, Jetson, and Raspberry Pi), two DDS implementations, and seven robot-operation workloads, ros2probe holds the discovery graph within 0.5% of an unobserved system, whereas domain-joining tools inflate discovery up to 2.6$\times$ and drop 38.5% of the subscriber's messages at saturation while ros2probe drops none. It reports loss with a recall of 1.0, cuts observer CPU and memory by up to 7$\times$ and 28$\times$, and stays practical on the embedded robots where existing tools overload the system.

</details>

---

### [[20_Research/Papers/机器人/Hand-centric_Human-to-Robot_Trajectory_Transfer_from_Video_Demonstrations_via_Open-World_Contact_Localization|Hand-centric Human-to-Robot Trajectory Transfer from Video Demonstrations via Open-World Contact Localization]]

![[assets/2606.10743_figure.png|800]]

- **arXiv**: [2606.10743](https://arxiv.org/abs/2606.10743)
- **PDF**: https://arxiv.org/pdf/2606.10743
- **详细分析**: [[20_Research/Papers/机器人/Hand-centric_Human-to-Robot_Trajectory_Transfer_from_Video_Demonstrations_via_Open-World_Contact_Localization|Hand-centric Human-to-Robot Trajectory Transfer from Video Demonstrations via Open-World Contact Localization]]
- **作者**: Yitian Shi, Di Wen, Zhengqi Han, Zicheng Guo, Yu Hu, Edgar Welte, Kunyu Peng, Rainer Stiefelhagen, Rania Rayyes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Hand-centric Human-to-Robot Trajectory Transfer from Video Demonstrations via Open-World Contact Localization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from human video demonstrations remains challenging due to noisy hand-object interactions, unseen objects with partial observation, and cross-embodiment discrepancy. To address these challenges, we present \textit{HOWTransfer} (\emph{H}and-\emph{O}bject \emph{O}pen-\emph{W}orld Transfer), a hand-centric framework that distills human demonstrations into contact-aware, taxonomy-informed, and diverse robotic trajectories. Instead of relying on object-specific descriptions, vision-language queries, or explicit object-state tracking, \emph{HOWTransfer} recovers temporally consistent 3D hand motion and localizes temporal contact intervals by reasoning over observed hand-object interaction cues. The localized contact onsets are then used to retarget human grasp intent into multi-modal parallel-jaw grasp hypotheses, which are propagated along the recovered wrist trajectory to generate robot-executable motions. Finally, a trajectory editing stage refines contact alignment and produces diverse executable variants from a single demonstration. Experiments across diverse manipulation tasks show that \emph{HOWTransfer} enables accurate contact localization and high-quality robot motion retargeting with $86\%$ success, which is preferred over teleoperated trajectories in a blinded preference study.

</details>

---

### [[20_Research/Papers/机器人/LieIPM_Lie_Group_Interior_Point_Method_for_Direct_Trajectory_Optimization_of_Rigid_Bodies|LieIPM: Lie Group Interior Point Method for Direct Trajectory Optimization of Rigid Bodies]]

![[assets/2606.10579_figure.jpg|800]]

- **arXiv**: [2606.10579](https://arxiv.org/abs/2606.10579)
- **PDF**: https://arxiv.org/pdf/2606.10579
- **详细分析**: [[20_Research/Papers/机器人/LieIPM_Lie_Group_Interior_Point_Method_for_Direct_Trajectory_Optimization_of_Rigid_Bodies|LieIPM: Lie Group Interior Point Method for Direct Trajectory Optimization of Rigid Bodies]]
- **作者**: Sangli Teng, Ruiqi Zhang, Tzu-Yuan Lin, William A Clark, Mark Mueller, Ram Vasudevan, Maani Ghaffari, Koushil Sreenath
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《LieIPM: Lie Group Interior Point Method for Direct Trajectory Optimization of Rigid Bodies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing dynamically feasible trajectories for rigid bodies is a fundamental problem in robotics. While direct methods are widely used, the existing constrained optimizers typically operate in Euclidean space and ignore the manifold structure of rigid body motions. This mismatch may introduce singularities or lead to poorly conditioned optimization problems. To bridge this gap, we develop a structure-aware framework for constrained trajectory optimization directly on matrix Lie groups. Our approach is based on the second-order rigid body models utilizing Lie group structures, which enables efficient Newton-type updates while preserving the underlying geometry. Building on this model, we propose a line-search Lie Group Interior Point Method (LieIPM) to handle constraints on the manifolds. We instantiate the framework for rigid body motion planning using Lie group variational integrators and derive closed-form intrinsic derivatives that exploit group symmetries. The LieIPM preserves the topology of rotation motions by construction and avoids singularities. Numerical results demonstrate superior robustness and faster convergence compared to general-purpose solvers and structure-exploiting optimal control methods.

</details>

---

### [[20_Research/Papers/具身智能/VeriSpace_Spatially_Grounded_Action_Verification_for_Vision-Language-Action_Models|VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models]]

![[assets/2606.10568_figure.png|800]]

- **arXiv**: [2606.10568](https://arxiv.org/abs/2606.10568)
- **PDF**: https://arxiv.org/pdf/2606.10568
- **详细分析**: [[20_Research/Papers/具身智能/VeriSpace_Spatially_Grounded_Action_Verification_for_Vision-Language-Action_Models|VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models]]
- **作者**: Guiyu Zhao, Longteng Guo, Junyou Zhu, Jun Fu, Yanghong Mei, Bin Cao, Jie Jiang, Xingjian He, Jing Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《VeriSpace: Spatially Grounded Action Verification for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have shown strong promise for robotic manipulation, but their reliability at test time remains limited by one-shot action prediction, where even small action errors can cause grasp failure, collision, or incorrect task progression. A natural alternative is to equip VLA systems with test-time verification, allowing multiple candidate actions to be proposed and evaluated before execution. However, reliable action verification is challenging because it requires not only distinguishing subtle geometric differences between candidate actions, but also assessing whether an action makes meaningful progress toward the task goal. We present VeriSpace, a 3D-aware action verifier for test-time action selection in VLA systems. VeriSpace evaluates candidate actions through two key components: Dual-Path 3D-Injected Scene Encoding, which constructs a scene representation that jointly preserves visual semantics and explicit 3D geometry, and Spatially-Grounded Action Reasoning, which evaluates each action by reasoning over task-relevant spatial relations, geometric validity, and expected goal progress. Together, these components enable more reliable discrimination between subtle yet outcome-critical action candidates while remaining fully compatible with existing VLA policies. Experiments on public benchmarks and real-world robotic manipulation tasks show that VeriSpace consistently improves decision reliability over both underlying VLA policies and prior verification-based methods, yielding substantial gains in both in-distribution and out-of-distribution settings.

</details>

---

### [[20_Research/Papers/具身智能/Uncovering_Vulnerability_of_Vision-Language-Action_Models_under_Joint-Level_Physical_Faults|Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults]]

![[assets/2606.10501_figure.png|800]]

- **arXiv**: [2606.10501](https://arxiv.org/abs/2606.10501)
- **PDF**: https://arxiv.org/pdf/2606.10501
- **详细分析**: [[20_Research/Papers/具身智能/Uncovering_Vulnerability_of_Vision-Language-Action_Models_under_Joint-Level_Physical_Faults|Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults]]
- **作者**: Minsoo Jo, Taeju Kwon, Junha Chun, Youngjoon Jeong, Taesup Kim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Uncovering Vulnerability of Vision-Language-Action Models under Joint-Level Physical Faults》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, RobustVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying Vision-Language-Action (VLA) models in real robotic systems requires robustness not only to semantic and perceptual variations, but also to embodiment-side faults that change how actions are physically realized. Real robots can experience joint-level changes caused by actuator degradation, hardware faults, safety limits, collision damage, or wear-induced friction. These faults are critical because they alter the action-to-motion interface of a policy, disrupting the learned closed-loop relationship between commanded actions, realized motion, and subsequent observations. In this work, we study realistic joint-level physical faults and show that VLA models are vulnerable when predicted actions are executed through a perturbed robot body. Our analysis reveals joint-dependent effects, with heterogeneous degradation in task success across affected joints. We also show that performance drops cannot be attributed solely to physical infeasibility, since feasible faults such as increased joint friction can still substantially reduce success rates and induce closed-loop execution mismatch. Motivated by these findings, we propose Joint-level Physical-fault Aware Residual Calibrator (J-PARC), a lightweight residual calibration framework built on top of a frozen VLA policy. J-PARC infers a latent joint-fault regime from recent joint dynamics and conditions a shared residual calibrator on this regime, enabling adaptive action correction across faulty joints. Experiments show that J-PARC improves robustness under joint-level faults while preserving fault-free environment performance.

</details>

---

### [[20_Research/Papers/具身智能/Act_on_What_You_See_Unlocking_Safe_Social_Navigation_in_Vision-Language-Action_Models|Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models]]

![[assets/2606.10495_figure.png|800]]

- **arXiv**: [2606.10495](https://arxiv.org/abs/2606.10495)
- **PDF**: https://arxiv.org/pdf/2606.10495
- **详细分析**: [[20_Research/Papers/具身智能/Act_on_What_You_See_Unlocking_Safe_Social_Navigation_in_Vision-Language-Action_Models|Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models]]
- **作者**: Qingzi Wang, Xiyang Wu, Guangyao Shi, Dianwei Chen, Xianfeng Yang, Dinesh Manocha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Act on What You See: Unlocking Safe Social Navigation in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe social navigation requires robots to distinguish people from ordinary obstacles and to react before danger becomes imminent. We show that pretrained Vision-Language-Action (VLA) models already encode pedestrian-object distinctions and future collision signals in their internal representations, but behavior cloning fails to translate these signals into socially appropriate actions. To address this mismatch, we propose SALSA, a two-stage annotation-free post-training framework: (1) social behavioral alignment bridges intermediate-layer social features to the action head and trains on counterfactual human-object scene pairs to break visual saliency shortcuts; (2) temporal safety alignment provides automatically generated future-risk supervision to enable anticipatory collision avoidance. On SCAND and real-world deployment, SALSA reduces near-collisions by 86.4% and improves social counterfactual accuracy from 53% to 93%, demonstrating that safer social navigation can be achieved by teaching VLA policies to act on representations they already possess. These results show that pretrained VLA policies can be adapted for safer social navigation by better aligning their latent representations with action generation.

</details>

---

### [[20_Research/Papers/具身智能/GuideWalk_Learning_Unified_Autonomous_Navigation_and_Locomotion_for_Humanoid_Robots_across_Versatile_Terrains|GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains]]

![[assets/2606.10449_figure.png|800]]

- **arXiv**: [2606.10449](https://arxiv.org/abs/2606.10449)
- **PDF**: https://arxiv.org/pdf/2606.10449
- **详细分析**: [[20_Research/Papers/具身智能/GuideWalk_Learning_Unified_Autonomous_Navigation_and_Locomotion_for_Humanoid_Robots_across_Versatile_Terrains|GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains]]
- **作者**: Haoxuan Han, Chen Chen, Linao Gong, Xin Yang, Hao Hu, Junhong Guo, Zhicheng He, Yao Su, Fenghua He
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.0（加权：具身智能 2.7，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots have achieved strong locomotion capabilities, but reliable navigation on versatile terrains remains challenging because obstacle avoidance must be coordinated with dynamically feasible motion. In this work, we present GuideWalk, a unified end-to-end framework that integrates traversability-aware navigation guidance with terrain-adaptive locomotion teacher for humanoid navigation. Specifically, we introduce a navigation module that provides explicit velocity guidance, decoupling obstacle avoidance from terrain conditions to enable robust planning across diverse environments. We propose a composite teacher distillation scheme, where goal-directed commands and dynamically consistent actions are aggregated and distilled into a single policy. To further improve robustness, the distilled policy is refined with reinforcement learning and an auxiliary behavior cloning objective, which promotes exploration while preserving desirable teacher behaviors. Experiments demonstrate that GuideWalk achieves stable and effective navigation while maintaining stable humanoid locomotion.

</details>

---

### [[20_Research/Papers/具身智能/UMI-Bench_1.0_An_Open_and_Reproducible_Real-World_Benchmark_for_Tabletop_Robotic_Manipulation_with_UMI_Data|UMI-Bench 1.0: An Open and Reproducible Real-World Benchmark for Tabletop Robotic Manipulation with UMI Data]]

![[assets/2606.10382_figure.png|800]]

- **arXiv**: [2606.10382](https://arxiv.org/abs/2606.10382)
- **PDF**: https://arxiv.org/pdf/2606.10382
- **详细分析**: [[20_Research/Papers/具身智能/UMI-Bench_1.0_An_Open_and_Reproducible_Real-World_Benchmark_for_Tabletop_Robotic_Manipulation_with_UMI_Data|UMI-Bench 1.0: An Open and Reproducible Real-World Benchmark for Tabletop Robotic Manipulation with UMI Data]]
- **作者**: Shi Jin, Yuntian Wang, Yuhui Duan, Di Wu, Gaoqi Dong, Xiaohang Liu, Xiaotong Li, Hongfei Jia, Zehao Zhang, Tianyu Wang, Zhongjie Jia, Yuanqi Yao...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《UMI-Bench 1.0: An Open and Reproducible Real-World Benchmark for Tabletop Robotic Manipulation with UMI Data》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World, UMI-Bench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-robot evaluation is essential for understanding whether learned manipulation policies can operate reliably outside curated demonstrations. This need is particularly pressing for Universal Manipulation Interface (UMI)-style policies, whose performance depends on the coupling between wrist-view observations, action representation, data collection, and physical deployment. Existing real-world benchmarks have made important progress, but they are not designed around this UMI data-to-deployment setting. We present UMI-Bench 1.0, a local-first real-robot benchmark for standardized evaluation of UMI-style manipulation policies. To the best of our knowledge, this is the first benchmark dedicated to real-world evaluation of UMI-based manipulation models. UMI-Bench aligns data collection, scene reset, policy execution, result logging, and task-factor analysis within a unified protocol. By making the full evaluation process reproducible and auditable, UMI-Bench provides a practical testbed for measuring how UMI-trained policies generalize to real physical manipulation.

</details>

---

### [[20_Research/Papers/具身智能/HiMem-WAM_Hierarchical_Memory-Gated_World_Action_Models_for_Robotic_Manipulation|HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation]]

![[assets/2606.10363_figure.png|800]]

- **arXiv**: [2606.10363](https://arxiv.org/abs/2606.10363)
- **PDF**: https://arxiv.org/pdf/2606.10363
- **详细分析**: [[20_Research/Papers/具身智能/HiMem-WAM_Hierarchical_Memory-Gated_World_Action_Models_for_Robotic_Manipulation|HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation]]
- **作者**: Xiaoquan Sun, Ruijian Zhang, Chen Cao, Yihan Sun, Jiahui Chen, Zetian Xu, Bo Chen, Haijier Chen, Zhen Yang, Jiarun Zhu, Yijun Hong, JingZhe Xu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《HiMem-WAM: Hierarchical Memory-Gated World Action Models for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CronusVLA, MemoryVLA, RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) have emerged as a new powerful paradigm for embodied intelligence, learning action-relevant visual dynamics that significantly enhance generalization and robustness. However, existing WAMs still struggle with task-relevant memory in long-horizon robotic manipulation. To address this, we present HiMem-WAM, a Hierarchical Memory-Gated WAM that integrates motion-centric latent actions, high-level skill latents, and boundary-triggered memory updates. Specifically, we develop a hierarchical latent action framework that jointly learns low-level motion and high-level skill latents, providing structured temporal abstraction. Meanwhile, a boundary-aware memory gate writes compact task states at predicted skill transitions, enabling causal inference without test-time generation of future video or optical flow estimation. Evaluated on LIBERO, LIBERO-PLUS, RMBench and real-world tasks, HiMem-WAM shows that hierarchical latents improve robustness under deployment perturbations, and the memory module substantially benefits memory-dependent long-horizon manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Rethinking_Embodied_Navigation_via_Relational_Inductive_Bias|Rethinking Embodied Navigation via Relational Inductive Bias]]

![[assets/2606.10348_figure.png|800]]

- **arXiv**: [2606.10348](https://arxiv.org/abs/2606.10348)
- **PDF**: https://arxiv.org/pdf/2606.10348
- **详细分析**: [[20_Research/Papers/具身智能/Rethinking_Embodied_Navigation_via_Relational_Inductive_Bias|Rethinking Embodied Navigation via Relational Inductive Bias]]
- **作者**: Weitao An, Chenghao Xu, Xu Yang, Cheng Deng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Rethinking Embodied Navigation via Relational Inductive Bias》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object navigation requires an agent to locate a target in an unknown environment through visual observations. Existing methods typically rely on open-vocabulary detectors or vision-language models (VLMs) to answer where to search, but often overlook what not to trust - which semantic cues are unreliable. Open-vocabulary perception is prone to systematic misleading evidence: false positives, outdated static priors, and repeated failed exploration due to lack of embodied verification, which contaminates mapping and decision-making. Such errors are rooted in structured object relations in real-world scenes. To address this, we propose DB-Nav, a framework that reshapes the search space via dual relational biases. It factorizes target-centric relations into an Activation Bias (propagates contextual evidence) and an Inhibition Bias (suppresses unreliable regions via perceptual confusion and action-level falsification). These biases are unified into a Relational Activation-Inhibition Exploration Graph that modulates frontier exploration values using online observations and failed accesses. Experiments on ObjectNav benchmarks show that DB-Nav significantly outperforms existing methods in success rate (SR) and Success weighted by Path Length (SPL), offering a lightweight, interpretable, and robust navigation framework without costly online VLM reasoning.

</details>

---

### [[20_Research/Papers/强化学习/OMG_Omni-Modal_Motion_Generation_for_Generalist_Humanoid_Control|OMG: Omni-Modal Motion Generation for Generalist Humanoid Control]]

![[assets/2606.10340_figure.png|800]]

- **arXiv**: [2606.10340](https://arxiv.org/abs/2606.10340)
- **PDF**: https://arxiv.org/pdf/2606.10340
- **详细分析**: [[20_Research/Papers/强化学习/OMG_Omni-Modal_Motion_Generation_for_Generalist_Humanoid_Control|OMG: Omni-Modal Motion Generation for Generalist Humanoid Control]]
- **作者**: Siqiao Huang, Kun-Ying Lee, Dongming Qiao, Guanqi He, Zhenyu Wang, Yitang Li, Shaoting Zhu, Hang Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《OMG: Omni-Modal Motion Generation for Generalist Humanoid Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid whole-body control has made significant progress in recent years, yet existing approaches remain limited to few-skill policies with heavy reward engineering, or motion trackers that are difficult to extend to new input modalities. We argue that the key to general-purpose humanoid control is to build a scalable brain, a module capable of reasoning with diverse conditioning modalities, atop a reactive motion tracking cerebellum, mirroring the hierarchical structure of biological motor systems. Two challenges arise in realizing this vision: acquiring a vast amount of high-quality data to achieve general purpose control, and equipping the generator with the capability to condition on compositional, extensible multi-modal inputs. We present OMG, which addresses these challenges with a meticulous data curation, filtering and labeling pipeline, as well as a diffusion-based motion generation backbone that conditions on language, audio, and human reference motions. Extensive experiments validate OMG as an omni-modal whole-body controller exhibiting state-of-the-art performance, model scaling behavior and efficient adaptation to new distributions and modalities, marking a concrete step toward foundation models for humanoid robots.

</details>

---

### [[20_Research/Papers/具身智能/SARM2_Multi-Task_Stage_Aware_Reward_Modeling_for_Self_Improving_Robotic_Manipulation|SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation]]

![[assets/2606.10305_figure.png|800]]

- **arXiv**: [2606.10305](https://arxiv.org/abs/2606.10305)
- **PDF**: https://arxiv.org/pdf/2606.10305
- **详细分析**: [[20_Research/Papers/具身智能/SARM2_Multi-Task_Stage_Aware_Reward_Modeling_for_Self_Improving_Robotic_Manipulation|SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation]]
- **作者**: Qianzhong Chen, Hau Zheng, Justin Yu, Suning Huang, Jiankai Sun, Ken Goldberg, Chuan Wen, Pieter Abbeel, Yide Shentu, Philipp Wu, Mac Schwager
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.4（加权：具身智能 1.8，大模型 0.1，强化学习 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SARM2: Multi-Task Stage Aware Reward Modeling for Self Improving Robotic Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DICE-RL, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-tuning vision-language-action (VLA) policies for long-horizon manipulation still relies heavily on behavior cloning, which requires costly high-quality demonstrations and keeps policies near the demonstration distribution. Reward models can reduce this dependence by reweighting demonstrations and providing dense supervision for on-robot reinforcement learning (RL), but they must be dense, accurate, and general. Existing methods fall short: task-specific stage-aware models are accurate but require per-task annotations, while general vision-language-model (VLM) reward models are broadly applicable but too coarse for fine-grained long-horizon progress. We introduce RM, a multi-task stage-aware reward model that combines an action-primitive-based stage estimator with a multi-gate Mixture-of-Experts (MMoE) value head to produce dense per-step rewards across manipulation tasks. Building on RM, we further propose SPIRAL (Self-Policy Improvement via Reward-Aligned Learning), an on-policy reward-guided framework that improves VLA policies from cheap autonomous rollouts. On a 10-task benchmark, RM reduces value-estimation MSE by 80% over the strongest baselines; when used in SPIRAL, it improves task success from around 50% to near-perfect performance on Folding Shorts (58% to 100%) and Cleaning Whiteboard (50% to 90%), showing that high-quality dense rewards are key to a stable robot data flywheel. Project website: https://qianzhong-chen.github.io/sarm2.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/MARCH_Model-Assisted_Reinforcement_Learning_for_the_Perceptive_Control_of_Humanoids_over_Sparse_Footholds|MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds]]

![[assets/2606.10288_figure.png|800]]

- **arXiv**: [2606.10288](https://arxiv.org/abs/2606.10288)
- **PDF**: https://arxiv.org/pdf/2606.10288
- **详细分析**: [[20_Research/Papers/具身智能/MARCH_Model-Assisted_Reinforcement_Learning_for_the_Perceptive_Control_of_Humanoids_over_Sparse_Footholds|MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds]]
- **作者**: Codrin Crismariu, Ryan K. Cosner
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.4（加权：具身智能 0.9，强化学习 0.8，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《MARCH: Model-Assisted Reinforcement Learning for the Perceptive Control of Humanoids over Sparse Footholds》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CLF-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perceptive bipedal locomotion over sparse terrain remains a difficult challenge: model-based methods are precise but brittle to uncertainty, while model-free methods are robust but struggle to discover the precise, constrained motions required for safety-critical locomotion where small errors can cause catastrophic failures. We propose a model-assisted reinforcement learning (RL) framework that combines both perspectives in three steps: (1) generate a safe reference trajectory using simplified models; (2) train a privileged teacher policy guided by a control Lyapunov function (CLF) reward built around the safe reference trajectory; and (3) distill the teacher into a vision-based student policy. We show that this model-assistance procedure produces physically grounded locomotion, improving sample efficiency, reducing the need for a complex learning curriculum, and achieving smoother locomotion behavior alongside stepping stone performance comparable to model-free baselines. We validate our approach in simulation and demonstrate successful deployment on a Unitree G1 humanoid robot navigating sparse footholds with lateral constraints.

</details>

---

### [[20_Research/Papers/具身智能/Locomotion_analysis_of_a_quadruped_interacting_with_the_lunar_granular_surface|Locomotion analysis of a quadruped interacting with the lunar granular surface]]

![[assets/2606.10273_figure.png|800]]

- **arXiv**: [2606.10273](https://arxiv.org/abs/2606.10273)
- **PDF**: https://arxiv.org/pdf/2606.10273
- **详细分析**: [[20_Research/Papers/具身智能/Locomotion_analysis_of_a_quadruped_interacting_with_the_lunar_granular_surface|Locomotion analysis of a quadruped interacting with the lunar granular surface]]
- **作者**: Yash J Vyas
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.7（加权：具身智能 2.4，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Locomotion analysis of a quadruped interacting with the lunar granular surface》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying legged robots in extra-terrestrial environments includes many challenges due to complex terrain interactions, energy, and thermal constraints. For effective mechanical design of a lunar exploration quadrupedal robot, careful consideration of motor torques, energy expenditure, and cost of transport is required. The lunar surface is composed of granular regolith, which impacts the locomotion of legged robots and their performance. Locomotion algorithms trained with rigid contact assumptions are also ineffective when applied to environments with soft contacts, such as granular surfaces, which can result in instability and poor tracking. In this report, the physical modelling of the granular lunar surface-robot foot contacts is applied to a simulation environment with locomotion trained using Reinforcement Learning. A comparison is conducted between the policy trained on rigid contact and soft contact environments, analysing the gait and locomotion performance metrics. The analysis demonstrates that soft contacts simulating regolith surfaces pose additional challenges for Reinforcement Learning based training, result in a qualitatively different gait, and increase the overall energy expenditure.

</details>

---

### [[20_Research/Papers/具身智能/Efficient-WAM_A_1B-Parameter_World-Action_Model_with_Low-Cost_Future_Imagination|Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination]]

![[assets/2606.10040_figure.png|800]]

- **arXiv**: [2606.10040](https://arxiv.org/abs/2606.10040)
- **PDF**: https://arxiv.org/pdf/2606.10040
- **详细分析**: [[20_Research/Papers/具身智能/Efficient-WAM_A_1B-Parameter_World-Action_Model_with_Low-Cost_Future_Imagination|Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination]]
- **作者**: Jiajun Li, Tiecheng Guo, Yifan Ye, Rongyu Zhang, Xiaowei Chi, Qianpu Sun, Ying Li, Yunfan Lou, Yan Huang, Zhihe Lu, Meng Guo, Shanghang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Efficient-WAM: A 1B-Parameter World-Action Model with Low-Cost Future Imagination》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-Action Models (WAMs) have emerged as a promising paradigm for embodied control by coupling future visual prediction with action generation. However, most existing WAMs rely on photorealistic future prediction, which incurs high inference latency and makes real-time robot deployment difficult. This motivates a more efficient WAM design that preserves the control benefits of future visual prediction while reducing its inference cost. We introduce Efficient-WAM, a World-Action Model that reduces the cost of future imagination while preserving its control benefit. Efficient-WAM improves inference efficiency via a compact video expert transferred from WAN-2.2-5B, token-sparse video latents, and asymmetric video-action denoising that allocates fewer sampling steps to video than to actions. Instead of optimizing the future branch for visual fidelity, Efficient-WAM treats future video prediction as a compact guidance signal for action generation. Comprehensive experiments on RoboTwin 2.0 and real-world manipulation tasks show that Efficient-WAM maintains strong action performance despite visibly coarse future predictions. While maintaining competitive control capabilities, our 1B-parameter model can reduce per-chunk latency to around 100 ms during physical deployment, achieving a 30x speedup over existing WAMs.

</details>

---

### [[20_Research/Papers/机器人/Robotic_Nonprehensile_Object_Transportation_with_a_Hanging_Tray|Robotic Nonprehensile Object Transportation with a Hanging Tray]]

![[assets/2606.10039_figure.jpg|800]]

- **arXiv**: [2606.10039](https://arxiv.org/abs/2606.10039)
- **PDF**: https://arxiv.org/pdf/2606.10039
- **详细分析**: [[20_Research/Papers/机器人/Robotic_Nonprehensile_Object_Transportation_with_a_Hanging_Tray|Robotic Nonprehensile Object Transportation with a Hanging Tray]]
- **作者**: Adam Heins, Angela P. Schoellig
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Robotic Nonprehensile Object Transportation with a Hanging Tray》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the nonprehensile object transportation task known as the waiter's problem, in which a robot must move an object balanced on a tray from one location to another. In contrast to prior works on the robotic waiter's problem, which make the robot tilt a tray rigidly held by its end effector (EE), we use a tray suspended from the EE by ropes, such that it behaves like a three-dimensional pendulum. Some prior works have actuated the robot so that the EE simulates the behavior of a pendulum, because pendular motion reduces the shear forces acting on the transported objects, minimizing the sliding of rigid objects and sloshing in containers of liquid. In contrast, our use of a real hanging tray allows us to obtain the benefits of pendular motion while only actuating a 3 degree-of-freedom (DOF) mobile base, rather than requiring a full 6-DOF manipulator arm. Our experiments in simulation and on real hardware show that the hanging tray substantially reduces both sliding and sloshing compared to a static, rigidly-grasped tray. Furthermore, we integrate the hanging tray into an interactive robot waiter demonstration, which uses computer vision to identify people with a raised hand and visual servoing to steer toward them and allow them to access the tray.

</details>

---
