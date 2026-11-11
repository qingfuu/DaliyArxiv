# cs.RO | Robotics | 2026-11-10

#arxiv #ComputerScience

**论文数**: 38

### [[20_Research/Papers/强化学习/DreamLander_A_6-DOF_World_Model_based_Reinforcement_Learning_Planetary_Lander|DreamLander: A 6-DOF World Model based Reinforcement Learning Planetary Lander]]

![[assets/2611.12824_figure.png|800]]

- **arXiv**: [2611.12824](https://arxiv.org/abs/2611.12824)
- **PDF**: https://arxiv.org/pdf/2611.12824
- **详细分析**: [[20_Research/Papers/强化学习/DreamLander_A_6-DOF_World_Model_based_Reinforcement_Learning_Planetary_Lander|DreamLander: A 6-DOF World Model based Reinforcement Learning Planetary Lander]]
- **作者**: George Nehma, Patrick Quinn, Madhur Tiwari, Camilo Riano-Rios
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.4（加权：强化学习 0.8，世界模型 0.6）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《DreamLander: A 6-DOF World Model based Reinforcement Learning Planetary Lander》归入 强化学习、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft powered descent landings are becoming evermore important in the field of space exploration and scientific advancement, because of their ability to deliver mission critical payloads, both highly accurately and safely. The high efficiency restriction on planetary landings due to the severely limited fuel supply results in the need for optimal guidance trajectories and control. Model based reinforcement learning is proving to be an important tool in simplifying the highly complex process of generating optimal guidance trajectories and control. In this work, we present DreamLander, a state of the art model based reinforcement learning algorithm based on DreamerV3, to generate optimal guidance and control for a realistic 6 degree of freedom entry descent landing problem. The model based approach creates a sample efficient and highly generalizable model that can be applied to a variety of scenarios whilst maintaining a high degree of accuracy, landing within 2 meters of the designated landing zone, and with velocity norm less than 0.3 meters per second. DreamLander makes use of state sensor observations, making progress toward End-to-End solutions of the Entry Descent Landing problem.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Heterogeneous_Tactile_Representation_for_General_Dexterous_Manipulation|Learning Heterogeneous Tactile Representation for General Dexterous Manipulation]]

![[assets/2611.12806_first_page.png|800]]

- **arXiv**: [2611.12806](https://arxiv.org/abs/2611.12806)
- **PDF**: https://arxiv.org/pdf/2611.12806
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Heterogeneous_Tactile_Representation_for_General_Dexterous_Manipulation|Learning Heterogeneous Tactile Representation for General Dexterous Manipulation]]
- **作者**: Bing Han, Yichuan Peng, Haoyu Dong, Yuanmeng Hu, Yongyi Jia, Fangjing Wang, Kecheng Zheng, Yiming Zhang, Yanhong Zeng, Xiaoqing Zhang, Chen Song, Rundong Zou...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 2.4，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Learning Heterogeneous Tactile Representation for General Dexterous Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LingBot-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing is an indispensable modality for contact-rich dexterous manipulation, a capability that hints at the ultimate frontiers of embodied intelligence. However, commercially available tactile sensors are still at a relatively early stage of development, with each type of sensor offering irreplaceable strengths alongside its own drawbacks. A key challenge is thus to free tactile understanding from sensor-specific physics, so that embodied models can effectively leverage heterogeneous tactile data. To this end, we develop LingBot-Touch, a tactile foundation model characterized by the following properties. (i) Our model yields a unified representation across different tactile sensors (i.e., piezoresistive, magnetic, and visuotactile sensors), and is easily extensible to new sensor types. (ii) The resulting tactile tokens are plug-and-play: they can be seamlessly integrated into policy models across paradigms, from diffusion policy to vision-language-action (VLA) models such as $π_{0.5}$ and LingBot-VLA, consistently enhancing manipulation dexterity. (iii) Extensive experiments, spanning simulation and real-robot deployments across multiple hardware platforms, demonstrate that our tactile representation substantially benefits complex manipulation tasks while maintaining strong computational efficiency. We believe the findings in this work demonstrate the potential of leveraging cross-sensor data to scale tactile learning, and offer encouraging insights for the design of future hardware and embodied models.

</details>

---

### [[20_Research/Papers/具身智能/Benchmarking_Real-World_Robotic_Manipulation_through_Stochastic_Challenges|Benchmarking Real-World Robotic Manipulation through Stochastic Challenges]]

![[assets/2611.12804_figure.png|800]]

- **arXiv**: [2611.12804](https://arxiv.org/abs/2611.12804)
- **PDF**: https://arxiv.org/pdf/2611.12804
- **详细分析**: [[20_Research/Papers/具身智能/Benchmarking_Real-World_Robotic_Manipulation_through_Stochastic_Challenges|Benchmarking Real-World Robotic Manipulation through Stochastic Challenges]]
- **作者**: Elias Gläßer, Gülhan Şikaroğlu, Pavlo Kupyn, Marc Pollefeys, Zuria Bauer, Hermann Blum
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Benchmarking Real-World Robotic Manipulation through Stochastic Challenges》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FurnitureBench, ManipulationNet, RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A challenging bottleneck in manipulation research is reproducibility and comparability of methods in real-world environments. Since manipulation is an interactive task, it cannot be evaluated on a static dataset of observations. Benchmarking in simulation is a common remedy, but cannot cover the whole complexity of real-world tests. This paper proposes a new paradigm of stochastic challenges. Like the well-known YCB objects, it is based on reproducible real-world scenes and therefore allows system-level innovation and comparability between different platforms. Due to their stochastic nature, our challenges however, mimic the rigor and surprise of hidden test sets. To this end, we show how different robots in different labs can be compared based on their success rate over different random task samples, if these samples come from the same distribution. We propose stochastic challenges as a general paradigm for robot benchmarking and implement this paradigm in a novel benchmark for mobile manipulation, on which we compare two robots tested in two different labs.

</details>

---

### [[20_Research/Papers/机器人/Sliding_into_Balance_Benefits_of_a_Sliding_Payload_for_Load_Distribution_and_Disturbance_Rejection_in_Dual-UAV_Transportation|Sliding into Balance: Benefits of a Sliding Payload for Load Distribution and Disturbance Rejection in Dual-UAV Transportation]]

![[assets/2611.12754_figure.png|800]]

- **arXiv**: [2611.12754](https://arxiv.org/abs/2611.12754)
- **PDF**: https://arxiv.org/pdf/2611.12754
- **详细分析**: [[20_Research/Papers/机器人/Sliding_into_Balance_Benefits_of_a_Sliding_Payload_for_Load_Distribution_and_Disturbance_Rejection_in_Dual-UAV_Transportation|Sliding into Balance: Benefits of a Sliding Payload for Load Distribution and Disturbance Rejection in Dual-UAV Transportation]]
- **作者**: Jorge Vicente-Martinez, Francisco José Mañas-Álvarez, Edgar Ramirez-Laboreo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Sliding into Balance: Benefits of a Sliding Payload for Load Distribution and Disturbance Rejection in Dual-UAV Transportation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper analyzes the cooperative transportation of a payload suspended from two drones in which, instead of being attached to two independent ropes, the payload is allowed to slide along a single rope connecting both UAVs. First, a planar nondimensional dynamical model of the sliding motion with viscous friction is presented. Then, considering stationary drones, this configuration is compared with a fixed payload with the same total rope length, both at equilibrium and under disturbances. The analytical results show that the sliding payload equalizes the tension in both rope segments for any relative position of the drones, so that no rope loses tension at equilibrium; it doubles the region reachable by the payload and, except for low friction combined with a large drone separation, it enlarges the set of admissible disturbances. Finally, a dynamic simulation also shows that under realistic gusty wind profiles, the average tension imbalance between the drones is reduced with respect to the fixed-payload solution.

</details>

---

### [[20_Research/Papers/机器人/Correctness_Boundaries_of_Typed_Plans_for_Natural-Language_Robot_Fleet_Control|Correctness Boundaries of Typed Plans for Natural-Language Robot Fleet Control]]

![[assets/2611.12654_first_page.png|800]]

- **arXiv**: [2611.12654](https://arxiv.org/abs/2611.12654)
- **PDF**: https://arxiv.org/pdf/2611.12654
- **详细分析**: [[20_Research/Papers/机器人/Correctness_Boundaries_of_Typed_Plans_for_Natural-Language_Robot_Fleet_Control|Correctness Boundaries of Typed Plans for Natural-Language Robot Fleet Control]]
- **作者**: Artem Tuzov, Dmitrii Vizitei, Evgenii Shlomov, Senya Belykh, Anastasia Malakhova, Alexander Maloletov
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Correctness Boundaries of Typed Plans for Natural-Language Robot Fleet Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PlanBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We examine what plan validation and execution reports establish in natural-language robot fleet control. Commands are traced through typed plans, deterministic corrections, fleet coordination and outcome checks in a three-level Robot Operating System 2 implementation with twenty simulated robots. An offline benchmark of 44 cases checks plan structure and selected command requirements. Across five local configurations without a response schema, 70.0-87.3% of responses pass. All runs in a selected 18-run simulation series meet their pose-based task conditions. This series includes two successful repeats that replaced incomplete runs after a software change. Saved plans and logs document duplicate pickup assignments and goal adjustments within the original task zones. Separate formation traces show a structurally accepted plan with the wrong formation shape and a rejected route, and an arrival report that omitted a requested robot after replanning. Carry completion records pickup and subsequent drop-off zone presence for the same robot. The cases distinguish changes to executable actions from changes to the requirements covered by a completion report. They motivate checking the effective assignments, goals and reported outcome against the original command.

</details>

---

### [[20_Research/Papers/具身智能/PCTac_Mechanochromic_Photonic-Crystal_Tactile_Sensor_for_Dexterous_Manipulation|PCTac: Mechanochromic Photonic-Crystal Tactile Sensor for Dexterous Manipulation]]

![[assets/2611.12383_figure.png|800]]

- **arXiv**: [2611.12383](https://arxiv.org/abs/2611.12383)
- **PDF**: https://arxiv.org/pdf/2611.12383
- **详细分析**: [[20_Research/Papers/具身智能/PCTac_Mechanochromic_Photonic-Crystal_Tactile_Sensor_for_Dexterous_Manipulation|PCTac: Mechanochromic Photonic-Crystal Tactile Sensor for Dexterous Manipulation]]
- **作者**: Ruilin Zhang, Xuanshuo Liu, Junzhe Dai, Kefei Wu, Xuhao Qin, Ziyuan Jiao, Wanlin Li, Yurui Qu, Chenxi Xiao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PCTac: Mechanochromic Photonic-Crystal Tactile Sensor for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern visuotactile sensors primarily sense contact by imaging the deformation of a compliant interface. Using techniques such as photometric stereo, they can recover detailed contact geometry, often represented as surface normals or depth. However, force-related information typically still needs to be inferred indirectly through calibration, geometric reconstruction, or learned mappings. Mechanochromic photonic-crystal (PC) materials offer an alternative physical encoding mechanism: contact loading changes their periodic microstructure and spectral response, directly transforming local stress into a spatially resolved structural-color field. Despite this potential, PC materials have rarely been explored as visuotactile sensors for closed-loop robot learning. We present PCTac, an open-source mechanochromic PC fingertip that uses a dense hue field as its tactile observation. Loading characterization demonstrates a repeatable relationship between the applied normal load and the observed hue response. We further integrate this representation directly into a Diffusion Policy and evaluate it on three real-robot manipulation tasks. Across 90 physical rollouts, PCTac Hue achieves 68 successes (75.6\%), compared with 60 (66.7\%) for PCTac RGB, 57 (63.3\%) for Wedge RGB, and 29 (32.2\%) for vision-only. PCTac Hue also achieves the highest observed success rate on each evaluated task, including Perturbed Test-Tube Insertion, where it achieves 16/30 successes versus 13/30 for tactile RGB baselines and 1/30 for vision-only. These results demonstrate the potential of mechanochromic structural color as a compact, load-sensitive tactile representation for robot learning and closed-loop manipulation. Project page: https://bey0ndt1me.github.io/PCTac-page/.

</details>

---

### [[20_Research/Papers/机器人/ExoStack_A_Modular_and_Reconfigurable_Software_Framework_for_Wearable_Robotics_Using_ROS_2|ExoStack: A Modular and Reconfigurable Software Framework for Wearable Robotics Using ROS 2]]

![[assets/2611.12306_first_page.png|800]]

- **arXiv**: [2611.12306](https://arxiv.org/abs/2611.12306)
- **PDF**: https://arxiv.org/pdf/2611.12306
- **详细分析**: [[20_Research/Papers/机器人/ExoStack_A_Modular_and_Reconfigurable_Software_Framework_for_Wearable_Robotics_Using_ROS_2|ExoStack: A Modular and Reconfigurable Software Framework for Wearable Robotics Using ROS 2]]
- **作者**: Debadrata Sarkar, Upamanyu Ray, Soumen Sen, Aman Arora
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《ExoStack: A Modular and Reconfigurable Software Framework for Wearable Robotics Using ROS 2》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wearable robots depend on a software chain that links body-worn sensing to gait interpretation, assistance generation, and actuation. Personalization further requires each measured response to remain associated with the assistance parameters that generated it. This paper presents ExoStack, a modular ROS 2 framework for implementing that chain across embedded hubs and a host computer. Its Embedded Sensing and Actuation (ESA) library configures ESP32 boards as microROS sensing and actuation hubs. ExoCore supplies multi-hub synchronization, gait-event detection, profile generation, motion planning, cost evaluation, and human-in-the-loop (HIL) optimization as configuration-instantiated nodes. The PASE desktop application edits configurations, launches the processing stages, and visualizes ROS 2 topics. Hardware drivers and algorithm plugins can be added through defined interfaces without modifying the generic processing nodes. We characterize hub and planner timing on three embedded computers and demonstrate reuse on two pneumatic exosuits.

</details>

---

### [[20_Research/Papers/机器人/BioMARS_2.0_a_robotic_biologist_for_formulating_and_adapting_biological_experiments|BioMARS 2.0: a robotic biologist for formulating and adapting biological experiments]]

![[assets/2611.12139_figure.png|800]]

- **arXiv**: [2611.12139](https://arxiv.org/abs/2611.12139)
- **PDF**: https://arxiv.org/pdf/2611.12139
- **详细分析**: [[20_Research/Papers/机器人/BioMARS_2.0_a_robotic_biologist_for_formulating_and_adapting_biological_experiments|BioMARS 2.0: a robotic biologist for formulating and adapting biological experiments]]
- **作者**: Yibo Qiu, Zan Huang, Yilin Qiao, Ziyang Ling, Yi Wang, Zhengyang Lu, Hangke Peng, Haoliang Ye, Ao Tian, Shu'ang Sun, Handi Liu, Yuqing Long...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《BioMARS 2.0: a robotic biologist for formulating and adapting biological experiments》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biological experimentation is not reducible to a single optimization problem, but requires decisions at multiple levels of abstraction: translating scientific knowledge into experimental procedures, adapting culture conditions to measured phenotypes and selecting interventions that test biological hypotheses. Automating experimental execution does not, by itself, determine which experiments should be performed next or how they should change in response to biological feedback. Here we introduce BioMARS, a human-in-the-loop multi-agent robotic system that connects knowledge-guided experimental decision-making with robotic execution and biological feedback. At the procedural level, BioMARS generated literature-grounded protocols and traceable action plans, improving expert-reviewed protocol quality scores across four model backends. At the parametric level, BioMARS used image-derived phenotypes from robotic retinal organoid culture to select subsequent experimental conditions, with higher reported scores in later rounds of the three-round experiment. At the intervention level, BioMARS nominated drug-repurposing candidates from biomedical evidence and advanced six candidates to wet-lab testing by researchers. Together, these studies demonstrate feedback-driven robotic biological experimentation within a framework that supports decisions about experimental procedures, culture conditions and biological interventions.

</details>

---

### [[20_Research/Papers/机器人/GAP_Generalized_Adaptation_Prior_for_Dexterous_Piano_Playing|GAP: Generalized Adaptation Prior for Dexterous Piano Playing]]

![[assets/2611.12111_figure.png|800]]

- **arXiv**: [2611.12111](https://arxiv.org/abs/2611.12111)
- **PDF**: https://arxiv.org/pdf/2611.12111
- **详细分析**: [[20_Research/Papers/机器人/GAP_Generalized_Adaptation_Prior_for_Dexterous_Piano_Playing|GAP: Generalized Adaptation Prior for Dexterous Piano Playing]]
- **作者**: Jinyi Chen, Hongyi Li, Lei Jiang, Xianwei Liu, Yanhong Liang, Yulin Chen, Yucheng Tao, Yongbin Jin, Hongtao Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《GAP: Generalized Adaptation Prior for Dexterous Piano Playing》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, Sim2Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous hands enable versatile manipulation, but policies trained in simulation often degrade on hardware owing to non-idealities, and the high-dimensional action space makes real-world adaptation costly. Piano playing, which requires precise and coordinated multifinger motion, offers a representative testbed. We propose GAP (Generalized Adaptation Prior for Dexterous Piano Playing), a sample-efficient adaptation framework that learns how to adapt, rather than how to act, during simulation pretraining and transfers this adaptation prior to hardware. Between repeated executions, GAP uses feedback to adjust the actions of the next one: a gradient guidance network learns from paired executions how adjusting actions affects playing performance, and its gradients guide these adjustments. In simulation, GAP yields approximately 2.4 times the F1 scores improvement of the existing fast-adaptation baseline for dexterous piano playing under the same interaction budget. The learned prior also generalizes to musical pieces held out from pretraining. On a physical dexterous hand, the same simulation-pretrained prior improves F1 scores by 3.6%-23% across three pieces of varying difficulty after approximately 7 min of adaptation each. These results suggest a practical route to reduce the real-world interaction needed to deploy dexterous hands.

</details>

---

### [[20_Research/Papers/具身智能/OASIS_Optimization-Aware_Subgoal_Inference_with_Safety_Constraints_for_Autonomous_Mobile_Robot_Navigation|OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation]]

![[assets/2611.11996_figure.png|800]]

- **arXiv**: [2611.11996](https://arxiv.org/abs/2611.11996)
- **PDF**: https://arxiv.org/pdf/2611.11996
- **详细分析**: [[20_Research/Papers/具身智能/OASIS_Optimization-Aware_Subgoal_Inference_with_Safety_Constraints_for_Autonomous_Mobile_Robot_Navigation|OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation]]
- **作者**: Arian Hajizadeha, Javad Pourrafia, Negar Shenavara, Sana Bashiria, Seyed Majid Esmailzadeh
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.2，强化学习 0.2，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《OASIS: Optimization-Aware Subgoal Inference with Safety Constraints for Autonomous Mobile Robot Navigation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigation in dynamic environments requires mobile robots to make progress toward their goals while respecting motion limits and avoiding surrounding obstacles. Learned subgoal policies can guide model predictive control beyond its local prediction horizon, but a geometrically suitable subgoal does not necessarily lead to a successfully solved control problem. This paper proposes OASIS, a hierarchical navigation framework that incorporates recent optimization outcomes into reinforcement learning-based subgoal generation. A high-level policy trained using Soft Actor--Critic generates local subgoals, while a nonlinear model predictive controller tracks them subject to motion limits, geometric collision-avoidance constraints, and embedded high-order control barrier function constraints. The outcomes of controller optimizations over each subgoal interval are summarized and provided to the policy at its next decision, without requiring additional optimization calls. The framework is evaluated in five navigation scenarios with static and moving obstacles, including dense interactions and sensing uncertainty. Comparisons with hierarchical and direct-goal control variants show that OASIS achieves the highest aggregate navigation success. Matched comparisons across three training seeds further show a consistent success advantage over the otherwise identical hierarchy without optimization-status input. The selected-policy comparison also shows fewer primary optimization failures with similar mean controller time.

</details>

---

### [[20_Research/Papers/具身智能/Flip_Anything_with_Agentic_Robotics_Self-Learning|Flip Anything with Agentic Robotics Self-Learning]]

![[assets/2611.11941_figure.png|800]]

- **arXiv**: [2611.11941](https://arxiv.org/abs/2611.11941)
- **PDF**: https://arxiv.org/pdf/2611.11941
- **详细分析**: [[20_Research/Papers/具身智能/Flip_Anything_with_Agentic_Robotics_Self-Learning|Flip Anything with Agentic Robotics Self-Learning]]
- **作者**: Shuangyu Xie, Kaiyuan Chen, Ken Goldberg
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Flip Anything with Agentic Robotics Self-Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flipping is a fundamental robotic manipulation skill that requires reorienting a target object in a stable pose on a planar support surface by rotating it 180$^\circ$ about an axis parallel to the support surface -- think of flipping a coin from heads to tails. Although flipping is a common objective in industrial tasks such as parts inspection, mechanical assembly, and tool use, coding a bimanual robot with grippers to flip diverse objects is a significant challenge. In this paper, we show that a coding agent can autonomously develop and refine object-flipping strategies through iterative learning in physics simulations across diverse object geometries. Progressive skill acquisition, from basic handover to toppling and pushing, robust grasping and sensing, and thin-object manipulation with recovery, improves task success from 24.7% to 95.0%. The resulting graph-based code integrates high-level strategy selection with reactive control, enabling multi-stage flipping on physical robots.

</details>

---

### [[20_Research/Papers/世界模型/Action_Representation_for_Spatial_Generalization_in_Robot_World_Models|Action Representation for Spatial Generalization in Robot World Models]]

![[assets/2611.11869_first_page.png|800]]

- **arXiv**: [2611.11869](https://arxiv.org/abs/2611.11869)
- **PDF**: https://arxiv.org/pdf/2611.11869
- **详细分析**: [[20_Research/Papers/世界模型/Action_Representation_for_Spatial_Generalization_in_Robot_World_Models|Action Representation for Spatial Generalization in Robot World Models]]
- **作者**: Yuhang Sun
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，世界模型 0.8，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Action Representation for Spatial Generalization in Robot World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial generalization in robot world models depends on whether action representations capture the physical relationships that remain valid across changing spatial configurations. Yet different coordinates can describe the same interaction, whereas similar motions can produce different outcomes when local physical conditions change. How these distinctions affect learned prediction remains insufficiently understood. This study evaluates matched action representations defined in world, object, and surface coordinate frames using a controlled robotic peeling benchmark. Global pose and contact relocation experiments reveal a cost associated with limited training data when equivalent interactions receive different spatial descriptions. Removing information about peel thickness creates an irreducible ambiguity because identical predictive inputs can correspond to different material removal outcomes. Coordinates defined relative to the surface improve consequence prediction and counterfactual action selection under accurate local observations, but learned predictors remain vulnerable to uncertainty in the coordinate frame. Joint centering of the surface and tool removes sensitivity to translation of their common origin, whereas incorrect contact geometry and actual execution deviations introduce different failure mechanisms. These results show that effective spatial generalization depends on preserving the relationships between actions and states that determine physical consequences, rather than simply minimizing coordinate variation. This perspective provides a principled basis for designing robot world models that reuse physical knowledge across spatial configurations while retaining the distinctions essential to prediction and planning.

</details>

---

### [[20_Research/Papers/具身智能/PAIR_Proprioception-Aligned_Image-Ray_Representations_for_Viewpoint-Robust_Manipulation|PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation]]

![[assets/2611.11798_figure.png|800]]

- **arXiv**: [2611.11798](https://arxiv.org/abs/2611.11798)
- **PDF**: https://arxiv.org/pdf/2611.11798
- **详细分析**: [[20_Research/Papers/具身智能/PAIR_Proprioception-Aligned_Image-Ray_Representations_for_Viewpoint-Robust_Manipulation|PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation]]
- **作者**: Sung-Wook Lee, Xuhui Kang, Dylan Losey, Yen-Ling Kuo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PAIR: Proprioception-Aligned Image-Ray Representations for Viewpoint-Robust Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlohaGym, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While imitation learning has made substantial progress toward generalizable robot manipulation through scaling, viewpoint robustness remains a major bottleneck. Visuomotor policies rely heavily on visual inputs, yet images provide an inherently ambiguous signal under viewpoint change: similar scenes may appear markedly different across viewpoints, while distinct states may share certain visual overlaps. A policy must therefore infer not only the task-relevant state, but also how it is visually projected under a particular camera configuration. This entanglement of viewpoint-dependent appearance and task-relevant state can make learning inefficient and limit generalization to unseen viewpoints. Recent work has begun to address this challenge through camera-ray conditioning and representation learning using geometric cues to induce invariance. However, providing camera information as additional context does not by itself ground visual representations in how the task scene is visually projected, while geometric alignment without camera context can introduce spurious correspondences by ignoring viewpoint-dependent projection. We propose PAIR, a contrastive learning framework that aligns joint image-ray representations using robot proprioception. PAIR encourages observations with similar robot states to remain close in representation space across viewpoints, providing a structured grounding signal for learning viewpoint-robust features. PAIR is a highly adaptable framework: it can be used to train Diffusion Policy (DP) or post-train vision-language-action (VLA) models. In simulated and real-world manipulation benchmarks with camera variation, PAIR consistently outperforms the behavior cloning baseline without ray conditioning by 12.7% and 26.7% points, respectively, demonstrating stronger generalization to unseen viewpoints. Project website: PAIRrobot.github.io.

</details>

---

### [[20_Research/Papers/机器人/Graph-Sparse_Distributed_Predictive_Control_for_Multi-Robot_Motion_Planning_vianEdge-Consensus_ADMM|Graph-Sparse Distributed Predictive Control for Multi-Robot Motion Planning vianEdge-Consensus ADMM]]

![[assets/2611.11755_figure.jpg|800]]

- **arXiv**: [2611.11755](https://arxiv.org/abs/2611.11755)
- **PDF**: https://arxiv.org/pdf/2611.11755
- **详细分析**: [[20_Research/Papers/机器人/Graph-Sparse_Distributed_Predictive_Control_for_Multi-Robot_Motion_Planning_vianEdge-Consensus_ADMM|Graph-Sparse Distributed Predictive Control for Multi-Robot Motion Planning vianEdge-Consensus ADMM]]
- **作者**: Josep Borras-Borras, Pablo Segovia, Carlos Ocampo-Martinez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Graph-Sparse Distributed Predictive Control for Multi-Robot Motion Planning vianEdge-Consensus ADMM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a distributed model predictive control (MPC) architecture for collision-avoiding motion planning of planar robots with double-integrator dynamics. To reduce coordination demands, a time-varying predicted conflict graph selects relevant pairwise interactions. The associated collision-avoidance constraints are convexified once per MPC update using warm-start trajectories, yielding a fixed convex quadratic program (QP). The resulting QP is then decomposed using an edge-consensus formulation of the alternating direction method of multipliers (ADMM), enabling parallel robot-local optimization and independent closed-form projections onto separating half-spaces. Execution is selectively supervised by a centralized high-order control barrier function (HOCBF) QP when the distributed candidate does not satisfy the direct-execution conditions. Evaluated in C++ simulations involving 8, 16, and 32 robots, the proposed architecture achieves collision-free execution and substantially improves computational scalability while maintaining task-level performance comparable to a centralized complete-graph baseline.

</details>

---

### [[20_Research/Papers/机器人/Compute_Regeneration_through_Re-Productization_Reorganizing_Retired_Edge_AI_Silicon_into_a_Delivered_Multilingual_Service_Robot|Compute Regeneration through Re-Productization: Reorganizing Retired Edge AI Silicon into a Delivered Multilingual Service Robot]]

![[assets/2611.11698_first_page.png|800]]

- **arXiv**: [2611.11698](https://arxiv.org/abs/2611.11698)
- **PDF**: https://arxiv.org/pdf/2611.11698
- **详细分析**: [[20_Research/Papers/机器人/Compute_Regeneration_through_Re-Productization_Reorganizing_Retired_Edge_AI_Silicon_into_a_Delivered_Multilingual_Service_Robot|Compute Regeneration through Re-Productization: Reorganizing Retired Edge AI Silicon into a Delivered Multilingual Service Robot]]
- **作者**: Hongyu Luo, Sun Tie, John Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Compute Regeneration through Re-Productization: Reorganizing Retired Edge AI Silicon into a Delivered Multilingual Service Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Useful edge hardware can lose product support while retaining substantial computation. We treat this as systems design: compute regeneration here means re-productization, retaining the compute module while redesigning the surrounding product organization. Our case is GEdgeBot, a multilingual service robot built around a retired 32 GB Jetson AGX Xavier. A source-grounded inventory shows the box alone supplies inference, while the combined system exposes five on-device AI services, a seven-language speech chain, three sensing domains, and one deterministic seven-byte control boundary. AI and orchestration stay on the Xavier; finite motor-pulse generation on an STM32F407. Audits cover the six-mode control state machine, readiness barriers and sound orientation. Historical single-prototype measurements report 1,782 MB GPU memory with YOLO, Whisper-small, and NLLB-200 resident, a direct-control p99 deviation rising from 0.24 to 49.93 ms under concurrent AI load, and six of six trigger-to-follow demonstrations at 4.35 s mean latency, with conversational voice unavailable. A November campaign restores an isolated inference stack, re-measures AI workloads, and repeats control-frame runs. Driving two execution organisations with the same 6,000 measured 50 ms frame intervals shows the finite-pulse boundary removes host jitter from the pulse train but not the command start phase; its stopping bound is host-enforced, while the MCU 16-bit pulse field is unclamped. A six-check static audit exposes a host--MCU queue mismatch, and a 14-scenario replay executes the audited main() dispatcher across six modes with zero physical device opens and 54 contract-checked frames. Results support an existence claim and a reproducible architectural hypothesis, not fleet-level reliability. The 208 direct-control ratio remains unreplicated; MCU waveform capture and on-site fault injection remain open.

</details>

---

### [[20_Research/Papers/具身智能/HINT-VLM_Humanoid_Interactive_Navigation_over_Rough_Terrain_with_Embodiment-Grounded_Vision-Language_Model|HINT-VLM: Humanoid Interactive Navigation over Rough Terrain with Embodiment-Grounded Vision-Language Model]]

![[assets/2611.11665_figure.png|800]]

- **arXiv**: [2611.11665](https://arxiv.org/abs/2611.11665)
- **PDF**: https://arxiv.org/pdf/2611.11665
- **详细分析**: [[20_Research/Papers/具身智能/HINT-VLM_Humanoid_Interactive_Navigation_over_Rough_Terrain_with_Embodiment-Grounded_Vision-Language_Model|HINT-VLM: Humanoid Interactive Navigation over Rough Terrain with Embodiment-Grounded Vision-Language Model]]
- **作者**: Ziwon Yoon, Seok Hwan Kim, Yiyu Chen, Quan Nguyen, Lu Gan, Ye Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.6（加权：具身智能 2.1，大模型 1.2，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《HINT-VLM: Humanoid Interactive Navigation over Rough Terrain with Embodiment-Grounded Vision-Language Model》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IsaacSim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots have achieved significant progress in locomotion and manipulation, enabling traversal over rough terrain and richer interaction with the environment, such as moving obstacles. However, most traditional navigation methods assume non-interactive environments and focus only on traversal. While Navigation Among Movable Obstacles (NAMO) approaches relax this assumption, prior efforts have largely focused on flat environments and reactive interaction, rather than predicting object movability and planning ahead. These limitations become critical in outdoor rough-terrain scenarios, where robots must jointly reason about terrain traversability and object movability. In this work, we address NAMO for humanoid robots in cluttered outdoor rough terrain by proposing a hybrid planning framework that combines semantic priors from a Vision-Language Model (VLM) with embodied robot interaction data through a Gaussian process (GP) residual model. The GP corrects the VLM-derived movability prior to produce embodiment-grounded probabilistic movability estimates, which are then incorporated into hierarchical uncertainty-aware planning. The proposed approach allows humanoids to jointly leverage locomotion and manipulation for efficient and safe navigation, representing the first solution to NAMO in rough terrain through predictive movability reasoning and probabilistic VLM integration.

</details>

---

### [[20_Research/Papers/具身智能/FlowEval_How_Much_Adaptation_Does_an_Embodied_Foundation_Model_Need_at_Deployment|FlowEval: How Much Adaptation Does an Embodied Foundation Model Need at Deployment?]]

![[assets/2611.11650_first_page.png|800]]

- **arXiv**: [2611.11650](https://arxiv.org/abs/2611.11650)
- **PDF**: https://arxiv.org/pdf/2611.11650
- **详细分析**: [[20_Research/Papers/具身智能/FlowEval_How_Much_Adaptation_Does_an_Embodied_Foundation_Model_Need_at_Deployment|FlowEval: How Much Adaptation Does an Embodied Foundation Model Need at Deployment?]]
- **作者**: Zhang Xi-Jia, Roman Yakunin, Shivang Chopra, Chengyue Huang, Che Chen, Siddharth Karamcheti, Zsolt Kira
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《FlowEval: How Much Adaptation Does an Embodied Foundation Model Need at Deployment?》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DreamZero-DROID, FlowEval, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale pretraining is reducing the amount of adaptation required to deploy embodied foundation models, but it is not guaranteed that a pretrained model already provide the level of performance required in every deployment. Practitioners therefore need to understand how well a pretrained model matches a target deployment and how much adaptation data is left to be collected. We study whether a small set of successful target-domain demonstrations can reveal whether and how much target-domain data will be required before any adaptation. We introduce FlowEval, a set of training-free metrics that use the flow-matching objective to probe an embodied foundation model with a set of demonstrations. FlowEval quantifies predictive disagreement on successful target demonstrations to assess how well a pretrained model fits a target deployment. Across four embodied foundation model families: Pi-0.5, MolmoAct2, GR00T, and DreamZero, FlowEval distinguishes seen from unseen deployments across real-world and simulated manipulation. Further, by finetuning Pi-0.5 and GR00T on 17 RoboCasa365 manipulation tasks, we showed that FlowEval correlates with how success rate improves as additional adaptation data is provided. Together, these results suggest that FlowEval can serve as a lightweight, training-free diagnostic of how much model--deployment adaptation may be required.

</details>

---

### [[20_Research/Papers/机器人/Kinora_A_Versioned_Workflow_for_Text-to-Motion_Generation,_Robot_Retargeting,_and_Interactive_Validation|Kinora: A Versioned Workflow for Text-to-Motion Generation, Robot Retargeting, and Interactive Validation]]

![[assets/2611.11601_first_page.png|800]]

- **arXiv**: [2611.11601](https://arxiv.org/abs/2611.11601)
- **PDF**: https://arxiv.org/pdf/2611.11601
- **详细分析**: [[20_Research/Papers/机器人/Kinora_A_Versioned_Workflow_for_Text-to-Motion_Generation,_Robot_Retargeting,_and_Interactive_Validation|Kinora: A Versioned Workflow for Text-to-Motion Generation, Robot Retargeting, and Interactive Validation]]
- **作者**: Fangcheng Jin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Kinora: A Versioned Workflow for Text-to-Motion Generation, Robot Retargeting, and Interactive Validation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion generation tools produce candidate trajectories, but interactive robot authoring also requires recoverable execution, traceable edits, explicit geometry, and model-specific validation. We present Kinora, a system that connects text-to-motion generation, a motion library, local agent tools, robot retargeting, and trajectory refinement through versioned artifacts. The current release uses an independently specified 52-joint authoring rig and procedural skeleton previews, separating the distributed human geometry from externally installed generation models and robot assets. Human-motion edits preserve frames outside a selected interval, while robot edits create immutable candidates whose reports govern acceptance and export. We evaluate server 0.5.1 and Gadget 0.15.2 with 156 core regression test executions, 49 Gadget executions, four CUDA generation/editing cases, a 30-frame G1 retargeting check, and a 3,600-frame synthetic G1 fixture paired with a suspended negative control. All four CUDA cases passed their numerical gates; the turning splice nevertheless retained a 14.3 cm support-foot drift proxy warning. The G1 positive fixture completed bounded simulation replay, whereas the suspended control was quarantined before replay. These results support selected integration and preservation contracts. They do not establish semantic-quality improvements, population-level feasibility, or hardware safety.

</details>

---

### [[20_Research/Papers/世界模型/DeepSoMo_Deformable_Object_Motion_Estimation_under_Proprioceptive_Partial_Observability_via_Predictive_Latent_Dynamics|DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics]]

![[assets/2611.11242_figure.png|800]]

- **arXiv**: [2611.11242](https://arxiv.org/abs/2611.11242)
- **PDF**: https://arxiv.org/pdf/2611.11242
- **详细分析**: [[20_Research/Papers/世界模型/DeepSoMo_Deformable_Object_Motion_Estimation_under_Proprioceptive_Partial_Observability_via_Predictive_Latent_Dynamics|DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics]]
- **作者**: Hanwen Zhao, Weicheng Dai, Luoyao Chen, Chen Feng
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《DeepSoMo: Deformable Object Motion Estimation under Proprioceptive Partial Observability via Predictive Latent Dynamics》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FoldingNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Estimating the motion of deformable bodies in soft robotics from proprioceptive sensing is challenging due to partial observability, as internal observations provide only indirect access to global motion, contact, and shape evolution. In such settings, instantaneous observations are insufficient, and accurate estimation requires temporally consistent latent representations. This paper studies deformable motion estimation under proprioceptive partial observability from a latent dynamics perspective. We argue that a key requirement for long-horizon estimation is latent temporal consistency, where latent states remain predictive of future observations. To this end, we present DeepSoMo, a learning-based framework that enforces predictive structure in latent dynamics through a self-supervised latent prediction constraint. We evaluate the approach in a canonical deformable dynamics setting using high-fidelity finite-element simulation as a controlled source of ground truth. Results demonstrate consistent improvements in trajectory estimation, orientation recovery, shape reconstruction, and contact inference over architecture-matched recurrent baselines.

</details>

---

### [[20_Research/Papers/强化学习/DexForesight_Grounding_Dexterous_Policies_with_Implicit_Spatial_Foresight|DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight]]

![[assets/2611.11166_figure.png|800]]

- **arXiv**: [2611.11166](https://arxiv.org/abs/2611.11166)
- **PDF**: https://arxiv.org/pdf/2611.11166
- **详细分析**: [[20_Research/Papers/强化学习/DexForesight_Grounding_Dexterous_Policies_with_Implicit_Spatial_Foresight|DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight]]
- **作者**: Zhongxi Chen, Yi Yang, Xinyi Chen, Mingzhe Ye, Yaping Li, Zhihong Liu, Congsheng Xu, Haonan Wang, Zhijie Deng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.2（加权：具身智能 1.5，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexForesight: Grounding Dexterous Policies with Implicit Spatial Foresight》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ReconVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation requires rich spatial foresight over both the surrounding scene and the robot hand. Existing world-action models often acquire such predictive knowledge through explicit future prediction. We introduce DexForesight, a framework that learns spatial foresight implicitly by injecting dynamics-aware world representations into the latent space of a dexterous policy. During training, DexForesight learns an action-conditioned spatial world model from offline scene depth, kinematic hand geometry, and demonstration trajectories. The world model predicts 3D hand-point motion and visual feature changes, capturing both articulated hand dynamics and scene changes under demonstrated actions, including the motion of fingers occluded from the cameras. We then freeze the world model and align policy queries with its predictive world queries, transferring the learned spatial dynamics into policy latents and using them to condition action generation. At deployment, only the policy is retained, operating on RGB observations, language, and robot state without depth input or explicit future prediction. On 11 DexJoCo simulation tasks, DexForesight improves the overall success rate of the base policy from 49.4% to 60.5%. On three real-robot dexterous manipulation tasks, DexForesight achieves 58.3% success, compared with 50.0% for the strongest baseline.Project page https://dexforesight.github.io/

</details>

---

### [[20_Research/Papers/强化学习/From_Festival_Video_to_the_Stage_A_Sim-to-Real_Ladder_for_Long-Horizon_Expressive_Whole-Body_Dance_on_a_Commercial_Humanoid|From Festival Video to the Stage: A Sim-to-Real Ladder for Long-Horizon Expressive Whole-Body Dance on a Commercial Humanoid]]

![[assets/2611.11127_figure.png|800]]

- **arXiv**: [2611.11127](https://arxiv.org/abs/2611.11127)
- **PDF**: https://arxiv.org/pdf/2611.11127
- **详细分析**: [[20_Research/Papers/强化学习/From_Festival_Video_to_the_Stage_A_Sim-to-Real_Ladder_for_Long-Horizon_Expressive_Whole-Body_Dance_on_a_Commercial_Humanoid|From Festival Video to the Stage: A Sim-to-Real Ladder for Long-Horizon Expressive Whole-Body Dance on a Commercial Humanoid]]
- **作者**: Hesham Shehata
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.9（加权：具身智能 2.4，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《From Festival Video to the Stage: A Sim-to-Real Ladder for Long-Horizon Expressive Whole-Body Dance on a Commercial Humanoid》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PoseHRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a pipeline for transferring Awa Odori, a traditional Japanese festival dance, from monocular video to a commercial Unitree G1 EDU humanoid. The pipeline combines human mesh recovery, kinematic retargeting, reinforcement learning for motion tracking in simulation, and onboard deployment via ONNX. Training ran on a single RTX 5070 GPU. An eleven-version deployment ladder evaluated on hardware examines three interventions. We detect and repair silent corruption of deployment artifacts, model state-estimator drift during training, and edit the reference motion to support stable execution and a controlled ending. The final policies achieved three consecutive rope-free completions of a 43-second routine, a 46-second performance with automatic handoff, and a continuous 9.7-minute rope-free performance composed from the captured motion. In a live handover, a single remote request let the robot start from and return to the manufacturer's walking controller on stage, with a measured torque-free window of 45-140 ms. We report the training dynamics and hardware outcomes and discuss failure boundaries involving compliant flooring and occlusion in monocular capture.

</details>

---

### [[20_Research/Papers/具身智能/Efficient_VLA_Inference_via_Retrieval-Based_Speculation_and_Hardware_Acceleration|Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration]]

![[assets/2611.11098_figure.png|800]]

- **arXiv**: [2611.11098](https://arxiv.org/abs/2611.11098)
- **PDF**: https://arxiv.org/pdf/2611.11098
- **详细分析**: [[20_Research/Papers/具身智能/Efficient_VLA_Inference_via_Retrieval-Based_Speculation_and_Hardware_Acceleration|Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration]]
- **作者**: Zhengyang Cheng, He Zhu, Zeyu Guo, Zihan Liu, Anbang Wu, Yiming Gan, Jingwen Leng, Yu Feng, Minyi Guo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.8，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Efficient VLA Inference via Retrieval-Based Speculation and Hardware Acceleration》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models enable robots to understand and execute complex instructions, but their autoregressive (AR) action generation introduces significant latency on resource-constrained robotic platforms. Speculative decoding can accelerate AR-based inference by parallelizing action generation and verification; however, existing approaches rely on costly draft models, which are inefficient on edge platforms. In this paper, we propose Zora, a hardware-software co-design framework for accelerating AR-based VLA inference. Specifically, Zora introduces a lightweight retrieval-augmented generation (RAG)-based draft model that exploits robotic dynamics without additional neural draft models. We further reduce batch verification overhead through a kinematics-guided action-acceptance strategy and a KV-cache-sharing attention mechanism. To address the retrieval overhead introduced by RAG-based drafting, we co-design dedicated hardware support, Zora core, to address the memory irregularity in RAG-based drafting. We evaluate Zora on four VLA models with the LIBERO benchmark. Zora retains comparable accuracy while achieving up to 3.4$\times$ speedup with software-only optimization and up to 7.6$\times$ speedup with hardware support over GPUs.

</details>

---

### [[20_Research/Papers/机器人/Large-Scale_Hierarchical_Decision-Making_in_Robot_Control_via_ADMM|Large-Scale Hierarchical Decision-Making in Robot Control via ADMM]]

![[assets/2611.11090_figure.png|800]]

- **arXiv**: [2611.11090](https://arxiv.org/abs/2611.11090)
- **PDF**: https://arxiv.org/pdf/2611.11090
- **详细分析**: [[20_Research/Papers/机器人/Large-Scale_Hierarchical_Decision-Making_in_Robot_Control_via_ADMM|Large-Scale Hierarchical Decision-Making in Robot Control via ADMM]]
- **作者**: Kai Pfeiffer, Jia Wang, Gordon Owusu Boateng, Yuquan Wang, Vincent Bonnet, Abderrahmane Kheddar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Large-Scale Hierarchical Decision-Making in Robot Control via ADMM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sparse hierarchical nonlinear programming (SH-NLP) based on the $\ell_0$-norm provides a powerful framework for integrated, efficient hierarchical decision-making in robot kinematic control, for example in the presence of a large set of possible end-effector candidate locations. While Sequential Sparse Hierarchical Quadratic Programming (S-SHQP) with interior-point method based SHQP sub-problem solvers exploit the hierarchical, sparse structure of such problems, they are less amenable to effective warm-starting between subsequent, coherent control steps. In this work, we formulate an Alternating Direction Method of Multipliers (ADMM) to efficiently solve related SHQP sub-problems. We introduce efficient substitutions for auxiliary variables representing $\ell_0$-norm surrogates. The solver efficiently handles separable decision functions by evaluating linear algebra expressions in the appropriate order. Results in large-scale kinematic and dynamic control show reduced computation times of up to 23.5% compared with a structure-exploiting interior-point method in low- to moderate-accuracy regimes. Furthermore, hierarchical decision-making is extended to whole-body dynamic control for humanoid walking, where the need for high-accuracy solutions is highlighted.

</details>

---

### [[20_Research/Papers/具身智能/ObjectWorld_Scaling_Object-Centric_World_Models_with_A_Large-Scale_3D_Full-Object_Flow_Dataset|ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset]]

![[assets/2611.11085_figure.png|800]]

- **arXiv**: [2611.11085](https://arxiv.org/abs/2611.11085)
- **PDF**: https://arxiv.org/pdf/2611.11085
- **详细分析**: [[20_Research/Papers/具身智能/ObjectWorld_Scaling_Object-Centric_World_Models_with_A_Large-Scale_3D_Full-Object_Flow_Dataset|ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset]]
- **作者**: Haonan Chen, Sicheng Isabella Lu, Haitian Li, Jiajin Wu, Hexiang Wei, Jiawei Zhang, Xin Fei, Yiwen Hou, Chenrui Tie, Chongkai Gao, Sheng Wang, Lin Shao
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 0.6，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《ObjectWorld: Scaling Object-Centric World Models with A Large-Scale 3D Full-Object Flow Dataset》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World, ObjectWorld, PointWorld, RLBench, Real-World, Track4World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative world modeling from large-scale visual data offers a promising path toward scalable robot manipulation. This calls for an intermediate representation that can be supervised at scale and remains actionable for downstream control. We propose 3D full-object flow, an object-centric motion representation that assigns dense 3D trajectories to points across the complete surface of a target object, including its occluded regions. By extending visible-surface object flow to the full object geometry, this representation makes complete object motion explicit and applies uniformly to both rigid and deformable objects. To realize the potential of this representation at scale, we introduce a 1210-hour full-object flow dataset that addresses the scarcity of large-scale supervision for complete 3D object motion. The dataset integrates diverse real-world videos and physical simulations, with a scalable annotation pipeline for recovering full-object motion from real-world observations and quality metrics for systematically assessing annotation quality. We then train a world model that takes an image and a task description as input and predicts dense full-object flow over the reconstructed object geometry. Experiments show reliable annotation quality, data-scalable flow prediction, and effective downstream manipulation across novel scenes and robot embodiments. Project website with additional results and videos: https://nus-lins-lab.github.io/ObjectWorld/.

</details>

---

### [[20_Research/Papers/具身智能/RoboMoCap_A_Large-Scale_Whole-Body_Motion_Capture_Dataset_with_Egocentric_Vision_for_Robot_Learning|RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning]]

![[assets/2611.10994_figure.png|800]]

- **arXiv**: [2611.10994](https://arxiv.org/abs/2611.10994)
- **PDF**: https://arxiv.org/pdf/2611.10994
- **详细分析**: [[20_Research/Papers/具身智能/RoboMoCap_A_Large-Scale_Whole-Body_Motion_Capture_Dataset_with_Egocentric_Vision_for_Robot_Learning|RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning]]
- **作者**: Mayur Deshmukh, Aaron Tung, Junyi Li, Nikash Bhardwaj, Ademi Adeniji, Vincent Liu, Michael Cho, Jiafei Duan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.9，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《RoboMoCap: A Large-Scale Whole-Body Motion Capture Dataset with Egocentric Vision for Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EgoSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots must coordinate locomotion and manipulation to navigate complex environments and perform everyday tasks. Learning such behaviours from human demonstrations requires accurate whole-body motion paired with egocentric vision, particularly for lower-body movements and foot placements that are frequently invisible from a first-person perspective. However, existing egocentric datasets often lack high-fidelity optical motion capture or systematic coverage of diverse loco-manipulation behaviours. To address this gap, we introduce RoboMoCap, a large-scale multimodal dataset combining egocentric vision with marker-based optical motion capture, specifically designed for locomotion-centric humanoid learning. RoboMoCap comprises over 200 hours of recordings from 14 participants, featuring six head-mounted cameras, wrist-mounted visual and inertial sensing, and optical full-body motion capture at 120 Hz. The dataset systematically covers diverse locomotion primitives, dynamic whole-body movements, and loco-manipulation tasks, including variable-speed walking, turning, constrained navigation, terrain traversal, object transportation, and manipulation during locomotion. It provides temporally aligned multimodal observations and metric whole-body motion representations, enabling the study of human movement beyond directly observable body regions. We systematically evaluate existing methods on three benchmark tasks: egocentric full-body motion reconstruction, foot contact and placement estimation, and human-to-humanoid motion retargeting. By pairing egocentric vision with high-fidelity human motion across diverse locomotion and interaction scenarios, RoboMoCap provides a foundation for egocentric motion understanding and humanoid learning from human demonstrations.

</details>

---

### [[20_Research/Papers/大模型/BAT-WAM_Bridging_Action_and_Touch_in_World-Action_Models_for_Dexterous_Hands|BAT-WAM: Bridging Action and Touch in World-Action Models for Dexterous Hands]]

![[assets/2611.10967_figure.png|800]]

- **arXiv**: [2611.10967](https://arxiv.org/abs/2611.10967)
- **PDF**: https://arxiv.org/pdf/2611.10967
- **详细分析**: [[20_Research/Papers/大模型/BAT-WAM_Bridging_Action_and_Touch_in_World-Action_Models_for_Dexterous_Hands|BAT-WAM: Bridging Action and Touch in World-Action Models for Dexterous Hands]]
- **作者**: Dong Fang, Feixuan Huang, Yuanxin Zhong, Yuxiang Gao, Qi Song, Yunlong Wang, Xiaosong Jia, Yu-Gang Jiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《BAT-WAM: Bridging Action and Touch in World-Action Models for Dexterous Hands》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DreamTacVLA, HT-Bench, HTBench, Real-World, Tactile-VLA, TouchWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation with world action models (WAMs) relies on hand configuration and contact information, yet joint-state and whole-hand tactile observations may be partially or entirely missing. RGB images provide scene context and hand-object geometry but are insufficient to reliably recover these missing modalities. We further observe a correlation between hand state and tactile information. Motivated by this observation, we introduce BAT-WAM, a framework that bridges visual, joint-state, and tactile representations for WAMs. BAT-WAM learns separate codebooks and decoders for the tactile and action streams. An RGB-conditioned continuous latent bridge connects the two streams for bidirectional learning, while visual information serves as continuous context. Under the HTBench evaluation protocol, BAT-WAM reduces the root mean squared error (RMSE) of tactile reconstruction by 34.73% under fully masked conditions and 38.84% under partially masked conditions, relative to an image-conditioned HandTouch checkpoint. For future tactile prediction conditioned on target-time RGB and historical actions, it reduces mean RMSE by 85.56% relative to OpenWAM with HandTouch. Real-robot experiments further show that BAT-WAM consistently outperforms related WAM baselines in dexterous manipulation. Generalization experiments on unseen objects and scenes also demonstrate substantial improvements over baseline models. These findings support joint modeling of visual context, hand state, and touch as a representation approach for multimodal WAMs.

</details>

---

### [[20_Research/Papers/具身智能/DreamVLA_From_Generated_Human_Motions_to_Humanoid_Vision-Language-Action_Policies|DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies]]

![[assets/2611.10872_figure.png|800]]

- **arXiv**: [2611.10872](https://arxiv.org/abs/2611.10872)
- **PDF**: https://arxiv.org/pdf/2611.10872
- **详细分析**: [[20_Research/Papers/具身智能/DreamVLA_From_Generated_Human_Motions_to_Humanoid_Vision-Language-Action_Policies|DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies]]
- **作者**: Kevin Park, Izat Rasyad, Dvij Kalaria, Shankar Sastry
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.5（加权：具身智能 3，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DreamVLA: From Generated Human Motions to Humanoid Vision-Language-Action Policies》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DreamVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training vision-language-action (VLA) policies typically depends on substantial robot demonstration data, making human teleoperation a costly and cumbersome bottleneck, particularly for whole-body humanoid interaction. Reinforcement learning in simulation offers an alternative for scaling this data, but designing task-specific rewards remains challenging. To address this, we propose DreamVLA, which uses generated motion trajectories to guide reinforcement learning (RL) in simulation, converting them into reliable task execution trajectories. These trajectories train VLA models in simulation without new task-specific teleoperation data. Our central contribution is a reference-conditioned DAgger distillation procedure: after a failed learner rollout, we restart the RL expert from a sampled learner state with the same reference suffix and aggregate successful corrective trajectories, addressing the distribution shift left by offline imitation. We evaluate picking from a platform, opening a drawer, pressing a button, and walking and picking from a platform, with ablations of DAgger iterations, residual RL, and generated dataset scale. Project website: ember-center-berkeley.github.io/DreamVLA.

</details>

---

### [[20_Research/Papers/具身智能/Which_Taxels,_Not_How_Many_Tactile_Sensor_Placement_for_Dexterous_Policies|Which Taxels, Not How Many: Tactile Sensor Placement for Dexterous Policies]]

![[assets/2611.10647_figure.png|800]]

- **arXiv**: [2611.10647](https://arxiv.org/abs/2611.10647)
- **PDF**: https://arxiv.org/pdf/2611.10647
- **详细分析**: [[20_Research/Papers/具身智能/Which_Taxels,_Not_How_Many_Tactile_Sensor_Placement_for_Dexterous_Policies|Which Taxels, Not How Many: Tactile Sensor Placement for Dexterous Policies]]
- **作者**: Taeyun Kim, Jinsoo Shin, Taehwa Kim, Taeyoon Kim, Jinyoung Choi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Which Taxels, Not How Many: Tactile Sensor Placement for Dexterous Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policies for dexterous manipulation depend on design choices made before training: which sensors enter the observation, where they are placed, and how their readings are arranged for the encoder. These choices are rarely examined. For tactile sensing, simulation studies place taxels uniformly over the hand, and this placement has become a default without being tested. We test this default under a single controlled protocol. The protocol holds the teacher, the training procedure, and the candidate taxels fixed and varies only the sensor configuration and the representation. We evaluate it on in-palm rotation and grasping with three robot hands. A small set of taxels selected from contact statistics matches a far larger uniform set. Taxels at rarely contacted sites are equivalent to no tactile input. With all candidate taxels, their layout in the input tensor does not affect performance, even for a convolutional encoder. Uniform placement therefore overestimates the number of taxels a task requires. We distill these results into lessons for designing tactile policies and into a minimal set of design choices that a tactile policy study should report.

</details>

---

### [[20_Research/Papers/具身智能/ReSkill_Selective_Self-Improvement_for_Robot_Manipulation|ReSkill: Selective Self-Improvement for Robot Manipulation]]

![[assets/2611.10510_figure.png|800]]

- **arXiv**: [2611.10510](https://arxiv.org/abs/2611.10510)
- **PDF**: https://arxiv.org/pdf/2611.10510
- **详细分析**: [[20_Research/Papers/具身智能/ReSkill_Selective_Self-Improvement_for_Robot_Manipulation|ReSkill: Selective Self-Improvement for Robot Manipulation]]
- **作者**: Zheng Sun, Zhihao Li, Zhuo Li, Wenrui Liu, Xin Wang, Fei Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《ReSkill: Selective Self-Improvement for Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-improvement on compositional manipulation tasks requires deciding what to reuse, where to improve, and which changes to retain. We present ReSkill, a selective self-improvement framework that concentrates revision on capability gaps. A coding agent constructs an object-centric task graph from an instruction and a skill library, then uses node-level execution records to locate failures. At the task level, it revises stage organization, hand-off conditions, and recovery routes; at the skill level, it strengthens perception, motion, manipulation, and verification capabilities that repeatedly fail. Candidate revisions undergo full-task evaluation and paired comparisons before adoption, allowing local changes to accumulate into validated skills and an independently executable policy. The agent participates only during development; the deployed policy calls the retained skills without invoking the agent at run time. On the same development set, average success across ten RoboDojo tasks rises from 30.0% for the initial versions to 86.2% for the final adopted programs; retained programs achieve 83.6% in recorded robustness and model-selection evaluations. Across eight real-world tasks, ReSkill succeeds in 72 of 80 rebuilt-simulation trials and 62 of 80 real-robot trials (77.5%). The median revision changes only three functions, approximately 0.5% of a program, while 39% of task-specific functions in later-added tasks directly reuse existing implementations. These results show how locating local deficiencies, validating candidate changes, and accumulating reusable skills can improve execution of compositional manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/Grip,_Trace,_Write_Force-Aware_Imitation_and_Reinforcement_Learning_for_High-DoF_Robotic_Handwriting|Grip, Trace, Write: Force-Aware Imitation and Reinforcement Learning for High-DoF Robotic Handwriting]]

![[assets/2611.10451_figure.png|800]]

- **arXiv**: [2611.10451](https://arxiv.org/abs/2611.10451)
- **PDF**: https://arxiv.org/pdf/2611.10451
- **详细分析**: [[20_Research/Papers/强化学习/Grip,_Trace,_Write_Force-Aware_Imitation_and_Reinforcement_Learning_for_High-DoF_Robotic_Handwriting|Grip, Trace, Write: Force-Aware Imitation and Reinforcement Learning for High-DoF Robotic Handwriting]]
- **作者**: Rongqian Chen, Yiding Chen, Jijie Zhou, Tom Z. Jiahao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，强化学习 0.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Grip, Trace, Write: Force-Aware Imitation and Reinforcement Learning for High-DoF Robotic Handwriting》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most robotic handwriting rigidly mounts the pen and reduces writing to trajectory tracking. A freely held pen instead couples grasp stability, tip motion, and contact force. We present Grip, Trace, Write, a force-aware simulation environment and learning framework for high-DoF handwriting. A two-branch actor separates pen retention from arm-wrist writing while preserving their closed-loop coupling. Training learns a grasp controller, initializes writing from inverse-kinematics demonstrations by behavior cloning, and improves writing through reinforcement learning with rewards on ink, force, time, and retention. Across diverse tasks, the policy improves completion, precision, force regulation, and efficiency over behavior cloning and inverse kinematics, and generalizes without fine-tuning to unseen English and Chinese content. These results establish force-aware handwriting as a testbed for dexterous tool use.

</details>

---

### [[20_Research/Papers/具身智能/Spatial_Representation_Distillation_and_Knowledge_Routing_for_Vision-Language-Action_Models|Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models]]

![[assets/2611.10443_figure.png|800]]

- **arXiv**: [2611.10443](https://arxiv.org/abs/2611.10443)
- **PDF**: https://arxiv.org/pdf/2611.10443
- **详细分析**: [[20_Research/Papers/具身智能/Spatial_Representation_Distillation_and_Knowledge_Routing_for_Vision-Language-Action_Models|Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models]]
- **作者**: Jungin Park, Chaoran Zhu, Changjae Oh, Kwanghoon Sohn
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Spatial Representation Distillation and Knowledge Routing for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, SPARK-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding three-dimensional physical structure has become essential for vision-language-action models (VLAs). However, existing approaches either rely on explicit geometric inputs at inference time or adopt a single visual pathway, potentially compromising the visual-semantic knowledge inherited from pre-trained models. We present SPARK-VLA, Spatial Representation distillation and Knowledge routing for VLAs, a preserve-specialize-route framework for spatially adapting VLAs without requiring external 3D inputs or experts at inference. SPARK-VLA consists of two key components: (1) spatial representation distillation, which transfers 3D understanding from a frozen 3D expert to a LoRA-adapted visual branch by aligning attention responses while preserving the original visual pathway, and (2) a lightweight knowledge router, which selectively forwards action-relevant visual tokens to the language model using routing supervision derived from action-loss gradients. Across LIBERO, LIBERO-Plus, CALVIN, and real-world manipulation, SPARK-VLA achieves strong performance with only a 0.5B language backbone and approximately 53M trainable parameters, providing an effective and parameter-efficient approach to 3D-aware VLA learning. Code is available at https://github.com/park-jungin/spark-vla.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Objective_Adaptation_After_Deployment_A_Position_on_World_Models_for_Remote_Robot_Teams|Multi-Objective Adaptation After Deployment: A Position on World Models for Remote Robot Teams]]

![[assets/2611.10435_figure.png|800]]

- **arXiv**: [2611.10435](https://arxiv.org/abs/2611.10435)
- **PDF**: https://arxiv.org/pdf/2611.10435
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Objective_Adaptation_After_Deployment_A_Position_on_World_Models_for_Remote_Robot_Teams|Multi-Objective Adaptation After Deployment: A Position on World Models for Remote Robot Teams]]
- **作者**: Jamie Santos, Kagan Tumer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Multi-Objective Adaptation After Deployment: A Position on World Models for Remote Robot Teams》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robot teams deployed in remote, unstructured environments may face changes in the environment, hardware, and team composition that degrade previously effective policies. Shifting mission objectives can be handled by selecting a different solution from an existing Pareto set, but shifting deployment conditions can reorder the set itself, making previously dominated policies competitive or new policies necessary. However, evaluating these policies in new contexts while minimizing risk to the hardware remains an open problem. We argue that, although largely untested in this domain, world models merit investigation for post-deployment multi-objective adaptation. By predicting policy outcomes under updated estimates of current conditions, world models could enable teams to re-evaluate existing policies without physically executing each candidate, provided predicted performance changes reflect those realized on deployed systems. We identify research priorities for model-based policy re-evaluation, validation of predicted against realized performance, and incorporating shared information into world models to support coordinated team adaptation.

</details>

---

### [[20_Research/Papers/具身智能/SimDuoReal_Object-Centric_Bimanual_Policy_for_Emergent_Dexterity|SimDuoReal: Object-Centric Bimanual Policy for Emergent Dexterity]]

![[assets/2611.10410_figure.png|800]]

- **arXiv**: [2611.10410](https://arxiv.org/abs/2611.10410)
- **PDF**: https://arxiv.org/pdf/2611.10410
- **详细分析**: [[20_Research/Papers/具身智能/SimDuoReal_Object-Centric_Bimanual_Policy_for_Emergent_Dexterity|SimDuoReal: Object-Centric Bimanual Policy for Emergent Dexterity]]
- **作者**: Qiyang Yan, Yulin Liu, Akash Sharma, Haozhi Qi, Guanya Shi, C. Karen Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.9，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《SimDuoReal: Object-Centric Bimanual Policy for Emergent Dexterity》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual dexterous manipulation requires coordinated arm and hand control, yet specifying such coordination manually is challenging and often task-specific. In this work, we explore whether complex bimanual dexterity can emerge from a simple object-centric learning objective. We train reinforcement learning policies under a shared object-centric reward, varying their training environments rather than tuning separate rewards for each behavior. We find that the policies discover pre-grasp manipulation, grasping and regrasping, in-hand adjustment and handover to reach object-pose goals without hand-designed motion sequences. We then refine the experts on transition states and use DAgger and reinforcement learning to distill them into a single policy that composes these behaviors for diverse bimanual tasks. On real hardware, the same policy succeeds in 61 of 80 trials (76.3\%) across four tasks with unseen objects and no task-specific fine-tuning. In simulated barcode scanning, our policy achieves 85.0\% success, compared with 60.4\% for two single-arm policies without handover. These results suggest that this objective provides a simple and scalable interface for learning general bimanual dexterity, shifting the burden from manually designing robot coordination to specifying what should happen to the object.

</details>

---

### [[20_Research/Papers/具身智能/Detecting_and_Explaining_Robot_Policy_Failures_from_Sparse_Internal_Features|Detecting and Explaining Robot Policy Failures from Sparse Internal Features]]

![[assets/2611.10400_figure.png|800]]

- **arXiv**: [2611.10400](https://arxiv.org/abs/2611.10400)
- **PDF**: https://arxiv.org/pdf/2611.10400
- **详细分析**: [[20_Research/Papers/具身智能/Detecting_and_Explaining_Robot_Policy_Failures_from_Sparse_Internal_Features|Detecting and Explaining Robot Policy Failures from Sparse Internal Features]]
- **作者**: Riad Ahmed, Sujosh Nag, Moniruzzaman Akash, Momotaz Begum
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Detecting and Explaining Robot Policy Failures from Sparse Internal Features》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CARL, LingBot-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor policies can handle many robot manipulation tasks, but understanding their failures remains difficult. Unfamiliar conditions and small action errors can lead to failure, yet watching the robot alone tells us little about what went wrong inside the policy. We introduce MIND (Mechanistic Interpretability for Neural Diagnosis), a method that looks inside a trained policy to detect failures during execution and identify the internal concepts involved. MIND uses a sparse autoencoder to break down the policy's internal activations into features that can be studied individually. We give meaning to these features by linking their activity to the robot's position, movement, and surroundings, and by steering their activations to examine how they affect the robot's actions. From successful and failed executions, we learn how the features behave on the way to a failure. During execution, MIND flags deviations from these patterns and uses the meaningful features contributing most to the change to describe the problem. Experiments in simulation and on a physical robot show that changes in these internal features help detect and explain failures. By using the same features for detection and diagnosis, MIND connects failure signals to understandable changes inside the policy.

</details>

---

### [[20_Research/Papers/大模型/GUARD_Anomaly-Informed_Q-Steering_for_Generative_Robot_Policies_in_Dexterous_Manipulation|GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation]]

![[assets/2611.10343_figure.png|800]]

- **arXiv**: [2611.10343](https://arxiv.org/abs/2611.10343)
- **PDF**: https://arxiv.org/pdf/2611.10343
- **详细分析**: [[20_Research/Papers/大模型/GUARD_Anomaly-Informed_Q-Steering_for_Generative_Robot_Policies_in_Dexterous_Manipulation|GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation]]
- **作者**: Aryaman Gupta, Xiaoyue Wu, Rana Soltani Zarrin, Mark Van der Merwe
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《GUARD: Anomaly-Informed Q-Steering for Generative Robot Policies in Dexterous Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative robot policies based on diffusion and flow matching can model complex, multimodal behaviors, but remain susceptible to covariate shift during closed-loop execution. Existing approaches mitigate such failures through additional demonstrations, policy fine-tuning, or test-time guidance, but often require human intervention, engineered rewards, or other task-specific signals. We introduce GUARD, an anomaly-informed Q-steering framework that leverages the policy's training distribution to construct a dense, failure-anticipatory steering signal. GUARD pairs sparse task rewards with dense anomaly scores learned from policy training data and propagates both through a learned Q-function. Its gradients then steer the denoising process toward actions that improve task return while preventing trajectories from entering poorly supported regions, without directly modifying the pretrained policy. Across four Adroit dexterous manipulation tasks, GUARD achieves average success rates of $96.0\%$ and $80.0\%$ under nominal and perturbed dynamics, outperforming the strongest baseline by $21.0$ and $20.0$ percentage points while maintaining the lowest anomaly score. GUARD further demonstrates direct sim-to-real transfer on in-hand screwdriver rotation and reorientation tasks, achieving $40$ and $25$ percentage-point gains in success rate. These results demonstrate that anomaly signals can serve not only for failure monitoring but also to complement sparse task rewards as effective supervision for robust policy steering.

</details>

---

### [[20_Research/Papers/具身智能/Capturability-Aware_Footstep_Planning_in_Cluttered_Environments_A_Recursively_Feasible_Sequential_MPC_on_Axis-Aligned_Safe_Corridors|Capturability-Aware Footstep Planning in Cluttered Environments: A Recursively Feasible Sequential MPC on Axis-Aligned Safe Corridors]]

![[assets/2611.10169_figure.png|800]]

- **arXiv**: [2611.10169](https://arxiv.org/abs/2611.10169)
- **PDF**: https://arxiv.org/pdf/2611.10169
- **详细分析**: [[20_Research/Papers/具身智能/Capturability-Aware_Footstep_Planning_in_Cluttered_Environments_A_Recursively_Feasible_Sequential_MPC_on_Axis-Aligned_Safe_Corridors|Capturability-Aware Footstep Planning in Cluttered Environments: A Recursively Feasible Sequential MPC on Axis-Aligned Safe Corridors]]
- **作者**: Athanasios Kyriakopoulos, Shubham S. Kumbhar, Kunal S. Narkhede, Abhijeet M. Kulkarni, Ioannis Poulakakis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Capturability-Aware Footstep Planning in Cluttered Environments: A Recursively Feasible Sequential MPC on Axis-Aligned Safe Corridors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A fundamental aspect of humanoid footstep planning is to jointly guarantee obstacle avoidance and locomotion stability. This paper presents a capturability-aware sequential Model Predictive Control (MPC) framework for Linear Inverted Pendulum (LIP)-based humanoid footstep planning in the presence of obstacles. The proposed method combines obstacle avoidance with capturability constraints through safe corridors constructed as sequences of intersecting rectangles, yielding a sequential MPC framework with recursive feasibility guarantees for the LIP-based planning layer. The planner autonomously adapts to constrained scenarios, switching to in-place walking when obstructions---such as doors assumed to be open during planning but unexpectedly found to be closed during execution---block forward motion. Performance is largely independent of the prediction horizon, allowing high success rates while keeping the computational cost low. The approach is validated in high-fidelity simulations with the humanoid robot Digit, demonstrating a practical solution for capturable humanoid footstep planning in cluttered environments.

</details>

---

### [[20_Research/Papers/机器人/A_Unified_Inertial_Encoder_for_Human_and_Humanoid_Motion|A Unified Inertial Encoder for Human and Humanoid Motion]]

![[assets/2611.10137_figure.png|800]]

- **arXiv**: [2611.10137](https://arxiv.org/abs/2611.10137)
- **PDF**: https://arxiv.org/pdf/2611.10137
- **详细分析**: [[20_Research/Papers/机器人/A_Unified_Inertial_Encoder_for_Human_and_Humanoid_Motion|A Unified Inertial Encoder for Human and Humanoid Motion]]
- **作者**: Yutian Chen, Shibo Zhao, Rocky Duan, Karen Liu, Carmelo Sferrazza, Guanya Shi, Yuheng Qiu, Koushil Sreenath
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Unified Inertial Encoder for Human and Humanoid Motion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IONet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning humanoid state estimation and language-grounded motion understanding from robot recordings ties training coverage to the robot's motion repertoire. Human motion datasets offer broader coverage, yet transferring this knowledge requires overcoming differences in body geometry, sensing, and physical disturbances. To enable this transfer, we propose a unified inertial encoder whose shared inertial interface uses kinematic IMU synthesis to represent human and humanoid motion at corresponding body sites. Within this common input space, joint training on human and kinematically retargeted humanoid motion combines velocity estimation and motion--text alignment with continuous-time encoding and sensor and motion randomization. The resulting model transfers zero-shot to a physical Unitree G1 without physics simulation, real-robot training trajectories, or fine-tuning, achieving the lowest velocity error among evaluated methods across five datasets, including 0.099m/s on real G1. Its motion-description retrieval also extends to retargeted G1 motion categories observed only in human training, demonstrating how human motion knowledge can support the generalization of humanoid inertial odometry and language-grounded motion understanding.

</details>

---

### [[20_Research/Papers/机器人/Global_Path_Planner_with_Multi-Model_Switching|Global Path Planner with Multi-Model Switching]]

![[assets/2609.13015_figure.png|800]]

- **arXiv**: [2609.13015](https://arxiv.org/abs/2609.13015)
- **PDF**: https://arxiv.org/pdf/2609.13015
- **详细分析**: [[20_Research/Papers/机器人/Global_Path_Planner_with_Multi-Model_Switching|Global Path Planner with Multi-Model Switching]]
- **作者**: Pietro Gori, Francesco Iotti, Eduard Zelenay, Rastislav Marko, Michele Pierallini, Franco Angelini, Gabriele Pannocchia, Manolo Garabini
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Global Path Planner with Multi-Model Switching》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work enhances global path planning via a pure-pursuit controller with multi-model kinematic switching that sustains plan fidelity across diverse terrains. The system includes a traversability graph for terrain analysis, a Heading-Aware A* algorithm for generating feasible paths, and a multi-model Pure Pursuit controller for dynamic tracking. A core innovation is adaptive kinematic modeling, enabling real-time switching between kinematic models based on terrain features and robot states. This adaptability optimizes path efficiency and energy use in challenging scenarios. We validate the approach in simulation on different platforms, namely the Artaban quadruped and the X3 quadrotor drone, showcasing improved performance, robustness, and adaptability over standard baselines.

</details>

---
