# cs.RO | Robotics | 2026-10-28

#arxiv #ComputerScience

**论文数**: 31

### [[20_Research/Papers/强化学习/EgoThumb_A_Vision-Driven_Supernumerary_Robotic_Thumb_for_Autonomous_Grasp_and_Holding_Assistance|EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance]]

![[assets/2610.37582_figure.png|800]]

- **arXiv**: [2610.37582](https://arxiv.org/abs/2610.37582)
- **PDF**: https://arxiv.org/pdf/2610.37582
- **详细分析**: [[20_Research/Papers/强化学习/EgoThumb_A_Vision-Driven_Supernumerary_Robotic_Thumb_for_Autonomous_Grasp_and_Holding_Assistance|EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance]]
- **作者**: Jianyu Hou, Jiawei Fu, Weikang Wan, Minghui Jiang, Jiajun Li, Hao Su
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《EgoThumb: A Vision-Driven Supernumerary Robotic Thumb for Autonomous Grasp and Holding Assistance》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Supernumerary robotic fingers augment human dexterity by enabling a single hand to perform complex "hold-and-manipulate" tasks that typically require bimanual coordination. However, existing devices are often hindered by bulky hardware that limits interaction to large objects and rely on explicit hand motion triggers that lack environmental context. To address these challenges, we present EgoThumb, a fully open-source, vision-driven supernumerary robotic thumb. EgoThumb features a compact, dual tendon-driven finger whose actuation is relocated to the forearm, reducing distal weight while enabling precise active joint control. The system utilizes a visual imitation learning policy that maps egocentric images from a palm-facing camera directly to continuous joint positions. By implicitly decoding human intent from visual cues capturing both the hand and the object of interest, EgoThumb achieves robust autonomous manipulation and strong generalization across diverse users and environments. All hardware designs and software implementations are fully open-sourced at https://ego-thumb.github.io.

</details>

---

### [[20_Research/Papers/具身智能/Rendering-Free_Event_Frame_Simulation_for_Fast_Reinforcement_Learning_of_Autonomous_Robot_Navigation|Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation]]

![[assets/2610.37543_figure.png|800]]

- **arXiv**: [2610.37543](https://arxiv.org/abs/2610.37543)
- **PDF**: https://arxiv.org/pdf/2610.37543
- **详细分析**: [[20_Research/Papers/具身智能/Rendering-Free_Event_Frame_Simulation_for_Fast_Reinforcement_Learning_of_Autonomous_Robot_Navigation|Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation]]
- **作者**: Dequan Ou, Austin Lopez, Quentin Missinne, Christophe De Wagter, Guido C. H. E. de Croon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.9（加权：具身智能 1.2，强化学习 0.8，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Rendering-Free Event Frame Simulation for Fast Reinforcement Learning of Autonomous Robot Navigation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MAVRL, NanoFlowNet, PULP-DroNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Event cameras offer low latency, high dynamic range, and milliwatt-level power consumption, making them ideal for agile robots such as tiny drones navigating through cluttered environments. However, existing simulators generally render photorealistic images before converting them into events, making large-scale reinforcement learning prohibitively slow. We propose an analytic event simulator that exploits what event cameras fundamentally measure - moving contrast edges - to synthesize event streams directly from scene geometry and ego-motion without visual rendering. Our simulator generates a 64x64 event observation in 17 microseconds on a single GPU - over 400x faster than a state-of-the-art rendering pipeline - enabling end-to-end reinforcement learning for goal-directed obstacle avoidance to converge in under 30 minutes - three orders of magnitude faster than training on rendered events. Policies transfer zero-shot to physically based event simulations (ray-traced Isaac Sim). Our policy reaches 83% success in cluttered courses unseen during training (mid-difficulty, traversability probability approx. 0.57), at 2.4 m/s average goal velocity, and retains 70% in a simulated texture-dense indoor hall. Furthermore, we quantized the policy to a 1.2 MB int8 network running fully onboard a 56-gram Crazyflie equipped with a Prophesee GenX320 event camera and an OpenMV N6 microcontroller board. Without any fine-tuning, external processing, or positioning, the policy achieves an average success rate of 82% (5/5, 5/6, 4/6 flights) across three real-world obstacle courses of increasing difficulty. Code: https://github.com/tudelft/rendering-free-event-nav

</details>

---

### [[20_Research/Papers/强化学习/Predict_the_Swing,_Match_the_Speed_Robotic_Pipe_Stabbing_With_Learned_Stereo_Vision_and_Residual_Reinforcement_Learning|Predict the Swing, Match the Speed: Robotic Pipe Stabbing With Learned Stereo Vision and Residual Reinforcement Learning]]

![[assets/2610.37535_figure.jpg|800]]

- **arXiv**: [2610.37535](https://arxiv.org/abs/2610.37535)
- **PDF**: https://arxiv.org/pdf/2610.37535
- **详细分析**: [[20_Research/Papers/强化学习/Predict_the_Swing,_Match_the_Speed_Robotic_Pipe_Stabbing_With_Learned_Stereo_Vision_and_Residual_Reinforcement_Learning|Predict the Swing, Match the Speed: Robotic Pipe Stabbing With Learned Stereo Vision and Residual Reinforcement Learning]]
- **作者**: Mohamed Ashraf Mostafa, Taher El-Fakharany, Samir Khaled
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，强化学习 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Predict the Swing, Match the Speed: Robotic Pipe Stabbing With Learned Stereo Vision and Residual Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A joint of pipe run into the hole swings from the elevator over the well and strikes a fixed stabbing guide at whatever speed the swing has. StabBot, a robotic stabbing system, predicts the swing and meets the pipe at its own speed. A pendulum Kalman filter tuned from the pipe tally tracks the joint in stereo images. A six-axis arm with an open V-shaped roller head closes in at matched velocity, confirms the last millimetres by touch, aims the pin over the box when the elevator hangs off centre, and follows the block down with lateral compliance. A ResNet-18 keypoint network locates the pipe, pin nose and box mouth in 3-D, and a residual reinforcement-learning policy refines the capture. On 200 paired random jobs with nine sizes from 2-3/8-in. tubing to 20-in. casing, StabBot seated every joint with the pipe touching only rollers, against 74% for a conventional fixed guide. Median contact speed fell from 18.4 to 2.3 cm/s and median peak head-pipe force from 11.3 to 1.4 kN, and the force was lower in all 200 jobs (Wilcoxon $p &lt; 10^{-30}$). The network locates the pipe with 0.4-mm median error in 2.3 ms per stereo pair. With the network in the loop, success stayed at 100% under 20 mm of added noise, 300-ms delay, 85% frame loss, 20-mm calibration offset, 20-cm elevator offset and 40-cm swings. All results come from a 1:4 Froude-scaled MuJoCo model and are reported at full scale.

</details>

---

### [[20_Research/Papers/机器人/Leveraging_Distributed_Sensing_and_Hyperdimensional_Computing_for_Non-Line-of-Sight_Passive_Object_Sensing|Leveraging Distributed Sensing and Hyperdimensional Computing for Non-Line-of-Sight Passive Object Sensing]]

![[assets/2610.37519_figure.png|800]]

- **arXiv**: [2610.37519](https://arxiv.org/abs/2610.37519)
- **PDF**: https://arxiv.org/pdf/2610.37519
- **详细分析**: [[20_Research/Papers/机器人/Leveraging_Distributed_Sensing_and_Hyperdimensional_Computing_for_Non-Line-of-Sight_Passive_Object_Sensing|Leveraging Distributed Sensing and Hyperdimensional Computing for Non-Line-of-Sight Passive Object Sensing]]
- **作者**: Placido Mursia, Marco Rossanese, Francesco Devoti, Adrian Lendinez Ibanez, Lanfranco Zanzi, Xi Li, Xavier Costa-Perez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Leveraging Distributed Sensing and Hyperdimensional Computing for Non-Line-of-Sight Passive Object Sensing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In smart factory environments, passive entities such as humans and movable obstacles may interfere with autonomous robot operations, posing significant safety risks. Detecting potential conflicts between robots and entities outside their field-of-view (FoV) is therefore of paramount importance. However, conventional passive object detection systems rely on sensors such as LiDAR, radar, or cameras, which operate under direct line-of-sight (LoS) and are limited by obstacles and occlusions. To overcome these limitations, integrated sensing and communication (ISAC) enables environmental perception via the communication infrastructure thanks to cooperation among distributed wireless devices. In this paper, we propose a framework for passive entity sensing beyond the robot's FoV that relies solely on distributed channel measurements from the communication infrastructure to perform risk-aware classification. These measurements are embedded into high-dimensional representations using hyperdimensional computing (HDC), enabling robust and scalable learning without explicit channel reconstruction. Numerical simulations based on a commercial ray tracer and ROS-based validation in realistic smart factory scenarios demonstrate improved safety and enhanced path planning with up to 89% accuracy under severe occlusions, while maintaining low computational complexity.

</details>

---

### [[20_Research/Papers/具身智能/World_Dreamer_v5-lite_A_Multi-Robot_World_Action_Model_with_One_Dreamer|World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer]]

![[assets/2610.37518_figure.png|800]]

- **arXiv**: [2610.37518](https://arxiv.org/abs/2610.37518)
- **PDF**: https://arxiv.org/pdf/2610.37518
- **详细分析**: [[20_Research/Papers/具身智能/World_Dreamer_v5-lite_A_Multi-Robot_World_Action_Model_with_One_Dreamer|World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer]]
- **作者**: Guoning Wu, Zijian Cai, Yuhang Zhang, Ying Liu, Yongbin Zheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 大模型
- **相关性评分**: 2.7（加权：具身智能 0.6，大模型 0.2，世界模型 0.8，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《World Dreamer v5-lite: A Multi-Robot World Action Model with One Dreamer》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GigaWorld, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot control requires integrating distributed camera views while predicting separate action sequences. Most vision-language-action and world-action models target one robot. Combining multiple views alone does not establish spatial correspondence between them. World Dreamer v5-lite is a multi-robot world-action model built around a shared world state for robot-specific action prediction. Calibrated features from a pretrained video encoder populate this state in workspace coordinates; its spatial size remains fixed as views are added. A vision-language model provides scene context and one query per robot. The queries read the shared state and exchange pose-aware information, while their action streams remain separate. Masked-view cooperative training withholds selected camera views from both visual branches while retaining all action targets. This encourages the use of observations shared by other robots. Pretraining uses more than 10,000 hours of trajectories from 20 simulated robot types, RoboFactory, and real robots. On RoboFactory, World Dreamer v5-lite achieves 74.0% mean success, 23.7 percentage points above the strongest evaluated baseline. Across four real-robot tasks, it reaches 78.8% mean success, a margin of 13.8 points. It also reaches 58.08% overall on RoboCasa365.

</details>

---

### [[20_Research/Papers/具身智能/Ego-CEVR_Learning_Cross-Embodiment_Visual_Representations_from_Human_Egocentric_Videos|Ego-CEVR: Learning Cross-Embodiment Visual Representations from Human Egocentric Videos]]

![[assets/2610.37509_figure.png|800]]

- **arXiv**: [2610.37509](https://arxiv.org/abs/2610.37509)
- **PDF**: https://arxiv.org/pdf/2610.37509
- **详细分析**: [[20_Research/Papers/具身智能/Ego-CEVR_Learning_Cross-Embodiment_Visual_Representations_from_Human_Egocentric_Videos|Ego-CEVR: Learning Cross-Embodiment Visual Representations from Human Egocentric Videos]]
- **作者**: Keru Zhou, Zhirui Fang, Xinrun Xu, Yaopeng Lou, Zeyuan He, Zihao Zhu, Xinze Niu, Chen Wang, Tianfu Li, Samith Va, Bin Qian, Junwei Li...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Ego-CEVR: Learning Cross-Embodiment Visual Representations from Human Egocentric Videos》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As egocentric video becomes increasingly available for embodied learning, an important research question is how to turn this low-cost, scalable source of data into robot manipulation capabilities. Egocentric videos naturally provide rich context for high-level task understanding, while real-robot demonstrations with wrist observations and action annotations provide supervision for fine-grained action alignment. We present Ego-CEVR, a data-native framework for hierarchical visual representation learning that assigns distinct learning objectives to global and interaction representations. The global module learns object relations, task state, and temporal progress through future prediction on egocentric video. The Interaction module interprets wrist observations in global context and learns local alignment and contact cues through robot action supervision. Separate residual paths expose both representations to the action policy, preserving direct access to task context alongside fine-grained execution information. Ego-CEVR supports independent pretraining of its global video module on large-scale human egocentric videos and videos from diverse robot embodiments, without requiring robot action labels or paired wrist observations.

</details>

---

### [[20_Research/Papers/具身智能/VLA-Stem_A_Lightweight_Safety_Mechanism_for_Vision-Language-Action_Models_via_Reinforcement_Learning|VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning]]

![[assets/2610.37378_figure.png|800]]

- **arXiv**: [2610.37378](https://arxiv.org/abs/2610.37378)
- **PDF**: https://arxiv.org/pdf/2610.37378
- **详细分析**: [[20_Research/Papers/具身智能/VLA-Stem_A_Lightweight_Safety_Mechanism_for_Vision-Language-Action_Models_via_Reinforcement_Learning|VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning]]
- **作者**: Bojun Zou, Wenhao Yu, Jiaohao Li, Jiaxuan Lin, Guanting Ye, Haohan Geng, Weihao Yu, Yanyong Zhang, Jianmin Ji
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.0（加权：具身智能 2.7，强化学习 0.6，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VLA-Stem: A Lightweight Safety Mechanism for Vision-Language-Action Models via Reinforcement Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, SafeVLA, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models integrate high-level reasoning with low-level action execution for end-to-end robotic control. However, most VLA models target static manipulation in unconstrained environments, overlooking spatial constraints and dynamic obstacles. Fine-tuning VLAs on obstacle-avoidance data is a straightforward solution, but collecting such data is costly, especially for dynamic scenarios, and may degrade their original task capabilities. To address these limitations, we propose VLA-Stem, a lightweight, reinforcement-learning-based safety mechanism for VLA systems. Without fine-tuning the underlying VLA policy, VLA-Stem converts its action chunks into motion references and uses trajectory-level guidance to preserve their spatial intent while allowing flexible motion and timing adjustments. Conditioned on these references, robot proprioception, and local obstacle information, the Stem policy adaptively modifies execution at inference time, preserving the original task intent while enabling responsive adaptation to spatial constraints and dynamic obstacles. For robust and sample-efficient training, we combine teacher-student distillation with curriculum learning. We evaluate VLA-Stem on reference following, static spatial constraints, and dynamic obstacle avoidance. Across six constrained simulation settings, VLA-Stem achieves 52.8% average collision-free task success versus 23.7% for the strongest safety baseline, while preserving base-policy performance in obstacle-free settings; real-world experiments further show consistent collision reductions under static and dynamic obstacles. These results demonstrate that VLA-Stem couples high-level VLA task intent with rapid, reflex-like responses to immediate physical risks, providing a brainstem-inspired mechanism for robust robot execution.

</details>

---

### [[20_Research/Papers/机器人/Generalizable_Target-Less_Joint_Intrinsic-Extrinsic_Camera-LiDAR_Calibration_using_Deep_Pixel-Point_Correspondences|Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences]]

![[assets/2610.37350_figure.png|800]]

- **arXiv**: [2610.37350](https://arxiv.org/abs/2610.37350)
- **PDF**: https://arxiv.org/pdf/2610.37350
- **详细分析**: [[20_Research/Papers/机器人/Generalizable_Target-Less_Joint_Intrinsic-Extrinsic_Camera-LiDAR_Calibration_using_Deep_Pixel-Point_Correspondences|Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences]]
- **作者**: Simon Bultmann, Daniele Cattaneo, Abhinav Valada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Generalizable Target-Less Joint Intrinsic-Extrinsic Camera-LiDAR Calibration using Deep Pixel-Point Correspondences》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CalibNet, LCCNet, RegNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate camera-LiDAR calibration is an essential prerequisite for robust multi-modal perception in robotics. Recent target-less methods based on learned pixel-point correspondences achieve high extrinsic calibration accuracy and generalize across environments. However, they operate on rectified images with known camera intrinsics, restricting their applicability to systems whose cameras have already been individually calibrated. We present a fully automatic, target-less framework that jointly estimates camera intrinsics, radial-tangential distortion, and camera-LiDAR extrinsics from raw images and LiDAR scans. Our method generalizes deep correspondence-based calibration from rectified images to raw cameras through intrinsic- and distortion-aware correspondence learning via synthetic augmentations. During calibration, we iteratively couple correspondence prediction and nonlinear optimization to jointly refine the camera parameters and relative sensor transformation. We evaluate our approach on an unseen camera-LiDAR configuration from the KITTI dataset and on three real robotic platforms in a zero-shot manner. The results demonstrate that joint calibration with our generalized pixel-point correspondence network improves extrinsic accuracy over correspondence-based methods using pre-calibrated cameras, while additionally recovering accurate intrinsics.

</details>

---

### [[20_Research/Papers/具身智能/Tokens_of_Motion_Primitive_Motion_Learning_for_Human-Humanoid_Skill_Transfer|Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer]]

![[assets/2610.37330_figure.png|800]]

- **arXiv**: [2610.37330](https://arxiv.org/abs/2610.37330)
- **PDF**: https://arxiv.org/pdf/2610.37330
- **详细分析**: [[20_Research/Papers/具身智能/Tokens_of_Motion_Primitive_Motion_Learning_for_Human-Humanoid_Skill_Transfer|Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer]]
- **作者**: Hanwen Ren, Meng Zheng, Wenzhe Cui, Benjamin Planche, Zhongpai Gao, Anwesa Choudhuri, Terrence Chen, Ziyan Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Tokens of Motion: Primitive Motion Learning for Human-Humanoid Skill Transfer》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SPiRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models provide a promising paradigm for scalable robotic manipulation, yet their reliance on success-only behavioral cloning leaves them brittle; lacking corrective training signals, minor execution errors rapidly compound into unrecoverable, out-of-distribution failures. To address this limitation, we propose Adaptive Failure-Informed Learning (AFIL), an end-to-end framework that leverages failure trajectories as adaptive negative guidance for diffusion- and flow-based VLA policies. AFIL uses a pretrained VLA to generate failure rollouts online, avoiding the need for handcrafted failure-mode design or human-in-the-loop recovery. It then jointly trains Dual Action Generators (DAGs) for successful and failed behaviors while sharing a common vision-language backbone, enabling efficient failure-aware policy learning with limited parameter overhead. During sampling, the failure generator adaptively steers action generation away from failure-prone regions and toward more reliable success modes, with guidance strength determined by the per-diffusion-step distance between success and failure distributions. Experiments across in-domain and out-of-domain robotic manipulation tasks, covering both short- and long-horizon settings, show that AFIL consistently improves task success rates and robustness over existing VLA baselines, demonstrating its effectiveness, efficiency, and generality.

</details>

---

### [[20_Research/Papers/具身智能/Remember_Where_You_Walk_Learning_Spatial_Memory_for_End-to-End_Legged_Robot_Exploration|Remember Where You Walk: Learning Spatial Memory for End-to-End Legged Robot Exploration]]

![[assets/2610.37203_figure.png|800]]

- **arXiv**: [2610.37203](https://arxiv.org/abs/2610.37203)
- **PDF**: https://arxiv.org/pdf/2610.37203
- **详细分析**: [[20_Research/Papers/具身智能/Remember_Where_You_Walk_Learning_Spatial_Memory_for_End-to-End_Legged_Robot_Exploration|Remember Where You Walk: Learning Spatial Memory for End-to-End Legged Robot Exploration]]
- **作者**: Leon Magnus, Nico Bohlinger, Jan Peters, Oleg Arenz
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Remember Where You Walk: Learning Spatial Memory for End-to-End Legged Robot Exploration》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DRL, MapNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoids and other legged robots operating in complex environments must remember information that leaves their field of view and only becomes relevant much later. Reinforcement learning policies address this using memory networks such as LSTMs that are trained end-to-end with the policy to memorize such task-relevant aspects. Yet, such architectures often fail to preserve sufficient information over long horizons. In this work, we propose a network architecture based on Hadamard memory that specifically targets robot navigation. Our Local Spatial Matrix Memory (LSMM) enables RL agents to store generic task-relevant information at specific, position-based memory cells, enabling flexible and spatially grounded memorization. We evaluate LSMM on the task of autonomous maze exploration, where it matches the maze coverage of strong recurrent and finite-history baselines while being the only architecture that remembers the maze layout, reducing the reconstruction error threefold.

</details>

---

### [[20_Research/Papers/具身智能/From_12_to_200_Demonstrations_How_ACT,_Diffusion_Policy,_SmolVLA_and_$π_{0.5}$_Scale_on_a_Low-Cost_Arm|From 12 to 200 Demonstrations: How ACT, Diffusion Policy, SmolVLA and $π_{0.5}$ Scale on a Low-Cost Arm]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2610.37170](https://arxiv.org/abs/2610.37170)
- **PDF**: https://arxiv.org/pdf/2610.37170
- **详细分析**: [[20_Research/Papers/具身智能/From_12_to_200_Demonstrations_How_ACT,_Diffusion_Policy,_SmolVLA_and_$π_{0.5}$_Scale_on_a_Low-Cost_Arm|From 12 to 200 Demonstrations: How ACT, Diffusion Policy, SmolVLA and $π_{0.5}$ Scale on a Low-Cost Arm]]
- **作者**: Simon Cowling
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《From 12 to 200 Demonstrations: How ACT, Diffusion Policy, SmolVLA and $π_{0.5}$ Scale on a Low-Cost Arm》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We trained four widely used imitation-learning policies, ACT, Diffusion Policy, SmolVLA and $π_{0.5}$, on nested subsets of 12, 25, 50, 100 and 200 teleoperated demonstrations of one pick-and-place task with distractor objects, using one fixed training recipe per policy. Every trained model was then run on a physical SO-101 arm on a fixed set of object placements: 1,340 scored episodes in 126 blocks. ACT, trained from scratch, rose from 1 success in 40 episodes at 12 demonstrations to 37 in 40 at 100. $π_{0.5}$ with its action expert fine-tuned was the best policy when data was scarce (16 of 40 at 12 demonstrations, 28 of 40 at 25) and then stayed near 70%; from 100 demonstrations ACT was ahead, by a margin this study does not fully resolve. SmolVLA and Diffusion Policy peaked near 50%, and both were affected by a failure to start: SmolVLA's arm never started moving in 47% of episodes, and Diffusion Policy hardly ever started until an idle lead-in was trimmed from the demonstrations. For $π_{0.5}$ the fine-tuning recipe mattered more than the amount of data: low-rank adaptation succeeded in 4 of 110 episodes, against 130 of 200 for action-expert fine-tuning. From the joint and camera recordings we place every episode on a four-stage ladder (started, reached the ball, carried it, delivered it) and show that for ACT more data moves failures from reaching, to grasping, to none, while the failures $π_{0.5}$ retains are in grasping. We also measure how weak a ten-episode block is as a measurement (the same checkpoint tested twice differs by 2 successes in 10 on average), separate seed-to-seed variation from that noise, and audit the human scoring against the recordings. Training length was fixed within each recipe, so the amount of data and the number of times it was seen change together; we state which conclusions survive that confound and which do not.

</details>

---

### [[20_Research/Papers/具身智能/RAVEN_A_Unified_Active_SLAM_System_for_Rapid_Autonomous_Visual_Exploration_with_Aerial_Robots_under_Localization_Uncertainty|RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty]]

![[assets/2610.37111_figure.png|800]]

- **arXiv**: [2610.37111](https://arxiv.org/abs/2610.37111)
- **PDF**: https://arxiv.org/pdf/2610.37111
- **详细分析**: [[20_Research/Papers/具身智能/RAVEN_A_Unified_Active_SLAM_System_for_Rapid_Autonomous_Visual_Exploration_with_Aerial_Robots_under_Localization_Uncertainty|RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty]]
- **作者**: Xinyi Chen, Yichen Zhang, Chenxing Jiang, Shaojie Shen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《RAVEN: A Unified Active SLAM System for Rapid Autonomous Visual Exploration with Aerial Robots under Localization Uncertainty》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Active simultaneous localization and mapping (SLAM) addresses the problem of planning robot motion to build complete and accurate maps of unknown environments through efficient exploration while maintaining high localization accuracy. This raises a dilemma between exploring unknown spaces to expand coverage and exploiting visited regions to perform active loop closures. Despite numerous prior works on ground robots, aerial robots with high agility and constrained sensor suites face more significant localization drift and thereby demand dedicated active SLAM planning. Moreover, a unified strategy that adapts performance based on task-specific priorities remains an open question. In this article, we introduce RAVEN, a unified active SLAM framework for Rapid Autonomous Visual ExploratioN using quadrotors, which systematically accounts for localization uncertainty. The framework starts with identifying frontiers and active loop closure candidates, from which global tour candidates are generated. These candidates are evaluated using a utility vector that separately quantifies exploration efficiency and localization accuracy, and the final tour is selected according to a prioritization parameter ranging from $[0,1]$. Finally, a perception-aware navigation planner generates smooth execution trajectories that minimize visual state estimation error based on the online Fisher information field that provides visual localization information in real-time. Benchmark evaluations demonstrate that RAVEN outperforms state-of-the-art active SLAM methods, highlighting its advantages in producing a spectrum of performance across prioritizations. Fully onboard field experiments with a customized stereo-inertial quadrotor further validate its practical applicability in challenging environments. The source code will be released to benefit the community.

</details>

---

### [[20_Research/Papers/具身智能/GAWM_A_Compact_Latent_World-Action_Model_for_Multi-Task_Robot_Manipulation|GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation]]

![[assets/2610.37091_figure.png|800]]

- **arXiv**: [2610.37091](https://arxiv.org/abs/2610.37091)
- **PDF**: https://arxiv.org/pdf/2610.37091
- **详细分析**: [[20_Research/Papers/具身智能/GAWM_A_Compact_Latent_World-Action_Model_for_Multi-Task_Robot_Manipulation|GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation]]
- **作者**: Yang Liu, Xiaoli Liu, Liuzhao Li, Yuduo Song, Muyuan Liu, Xiang Gao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.8（加权：具身智能 1.5，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GAWM: A Compact Latent World-Action Model for Multi-Task Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DreamVLA, PLaW-VLA, TurboVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models (WAMs) incorporate the prediction of future observations into robot policy learning. However, most WAMs build on billion-parameter vision-language or video-generation backbones, which incur high training cost and inference latency. In this letter, we present GAWM (Geometry-Aware World Model), a compact multi-task WAM that predicts future observations in the latent space of a frozen DINOv3 encoder. GAWM compresses the features of each camera view into a small set of tokens. A lightweight predictor, conditioned on the task rather than on actions, forecasts these tokens at two future horizons. The forecast is supervised with the dense patch features of future frames, which requires it to encode the spatial layout of the future scene. An action decoder directly regresses a chunk of future actions from the current and predicted tokens. With fewer than 100M parameters and no robot or video pretraining, GAWM outperforms billion-parameter WAMs on RoboTwin 2.0 and performs comparably to billion-parameter VLAs on LIBERO. On a dual-arm robot, it achieves lower action-prediction error on held-out demonstrations than a fine-tuned billion-parameter VLA, with substantially lower inference latency. Ablation studies show that the latent world model substantially improves performance when training data or training time is limited. Code is available at https://github.com/gaoxiang12/ga-wm.

</details>

---

### [[20_Research/Papers/机器人/State_estimation_for_a_hybrid_rigid-continuum_space_manipulator_system|State estimation for a hybrid rigid-continuum space manipulator system]]

![[assets/2610.37043_figure.png|800]]

- **arXiv**: [2610.37043](https://arxiv.org/abs/2610.37043)
- **PDF**: https://arxiv.org/pdf/2610.37043
- **详细分析**: [[20_Research/Papers/机器人/State_estimation_for_a_hybrid_rigid-continuum_space_manipulator_system|State estimation for a hybrid rigid-continuum space manipulator system]]
- **作者**: Lorenzo Ticozzi, Patricio A. Vela, Panagiotis Tsiotras
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《State estimation for a hybrid rigid-continuum space manipulator system》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spacecraft-mounted robotic manipulators can support long-term operability of orbiting assets by conducting tasks such as on-orbit assembly, repair, upgrade, and refueling. In this context, the integration of continuum/soft robotic mechanisms into space manipulator designs promises to reduce stowage volume and mass, as well as to improve operational safety through the inherent mechanical compliance of soft structures. This work presents a novel state reconstruction pipeline for a hybrid soft-rigid space manipulator, in which the distal link is a tendon-driven continuum robot. The estimation problem is formulated as a maximum a posteriori (MAP) inference problem over the hybrid manipulator's configuration, conditioned on discrete, noisy measurements from joint encoders and a vision-based sensing pipeline. The resulting soft-constrained optimization problem is transcribed as a factor graph, providing a compact representation for fusing heterogeneous measurements with the rigid-soft kinematic model. Furthermore, the adoption of the Geometric Variable Strain (GVS) approach yields a minimum-order parameterization of the configuration, a property expected to facilitate model-based feedback control design in future work. The proposed implementation is validated in simulation on a closed-loop trajectory where, for better realism, position measurements for the continuum link are obtained by means of a simulated visual pipeline leveraging synthetic photorealistic images. The state reconstruction accuracy and computational performance confirm the potential of the proposed framework for hybrid soft-rigid robotic applications in orbit.

</details>

---

### [[20_Research/Papers/机器人/Structure-Actuation_Co-Design_of_All-Electric_Heavy-Duty_Robotic_Manipulators|Structure-Actuation Co-Design of All-Electric Heavy-Duty Robotic Manipulators]]

![[assets/2610.36996_figure.png|800]]

- **arXiv**: [2610.36996](https://arxiv.org/abs/2610.36996)
- **PDF**: https://arxiv.org/pdf/2610.36996
- **详细分析**: [[20_Research/Papers/机器人/Structure-Actuation_Co-Design_of_All-Electric_Heavy-Duty_Robotic_Manipulators|Structure-Actuation Co-Design of All-Electric Heavy-Duty Robotic Manipulators]]
- **作者**: Mohammad Bahari, Amir Hossein Barjini, Jouni Mattila
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Structure-Actuation Co-Design of All-Electric Heavy-Duty Robotic Manipulators》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a mixed discrete-continuous multiobjective bilevel framework for the structure-actuation co-design of all-electric heavy-duty robotic manipulators. The upper level optimizes manipulator geometry and actuation topology, while joint-specific lower-level searches construct feasible archives of discrete motor, gearbox, and screw configurations. A system-level coordinator selects actuator packages according to hardware mass, co-design cost, and loss-aware supply energy, and the resulting actuator masses are fed back to the robot model until a mass-consistent fixed point is obtained. Evaluation on a full-pose SE(3) benchmark with a 100-kg tool payload yields eight feasible nondominated designs, all satisfying the 12 prescribed poses. Actuator-mass coupling converges in three iterations for every reported design. A fixed-design ablation shows that one-pass sequential sizing changes hardware mass by up to 2.13%, co-design cost by 10.20%, and supply energy by 9.40% in magnitude. Payload screening further reveals increasing mass-cost-energy demand and changes in competitive mechanism topology with carried load.

</details>

---

### [[20_Research/Papers/具身智能/Omni-IGN_Onboard_Image-Goal_Navigation_for_Drones_with_Omnidirectional_Vision|Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision]]

![[assets/2610.36968_figure.png|800]]

- **arXiv**: [2610.36968](https://arxiv.org/abs/2610.36968)
- **PDF**: https://arxiv.org/pdf/2610.36968
- **详细分析**: [[20_Research/Papers/具身智能/Omni-IGN_Onboard_Image-Goal_Navigation_for_Drones_with_Omnidirectional_Vision|Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision]]
- **作者**: Zichen Yan, Rui Huang, Shenao Wang, Yucong Wang, Nuthasith Gerdpratoom, Lin Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Omni-IGN: Onboard Image-Goal Navigation for Drones with Omnidirectional Vision》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IsaacSim, OMNI-DRL, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Image-goal navigation (ImageNav) requires an agent to reach a location specified by a goal image in an unknown environment. For drones, this task demands exploration, goal- directed navigation, and collision avoidance under limited onboard computing resources. Existing aerial ImageNav methods are built on single-view observations, requiring additional rotation and exploration to search for goal-relevant cues outside the field of view. In this paper, we present Omni-IGN, a fully onboard ImageNav system that integrates quad-fisheye perception, an attention-based reinforcement learning (RL) policy, and a collision-aware safety layer. The policy adaptively fuses goal-relevant features across multiple views to provide directional guidance for continuous navigation. The quad-fisheye RGB images support both ImageNav and obstacle avoidance without a dedicated depth sensor. On Habitat benchmarks, Omni-IGN achieves the best performance among continuous-action baselines. Moreover, flight tests in IsaacSim validate the effectiveness of integrating learning-based depth estimation with the action safety layer for collision avoidance. Finally, real-world experiments demonstrate zero-shot sim-to-real transfer without any fine-tuning or external localization. The code and model checkpoints will be released upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/When_Black-Box_Robot_Policies_Fail_Online_Sensor_Diagnosis_and_Repair_with_a_Transparent_Surrogate|When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate]]

![[assets/2610.36852_figure.png|800]]

- **arXiv**: [2610.36852](https://arxiv.org/abs/2610.36852)
- **PDF**: https://arxiv.org/pdf/2610.36852
- **详细分析**: [[20_Research/Papers/具身智能/When_Black-Box_Robot_Policies_Fail_Online_Sensor_Diagnosis_and_Repair_with_a_Transparent_Surrogate|When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate]]
- **作者**: Marc Ziegler, Batu Özen, Sami Mentes, Thomas Waschulzik, Alois Knoll
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《When Black-Box Robot Policies Fail: Online Sensor Diagnosis and Repair with a Transparent Surrogate》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot foundation models may generalize across tasks and embodiments, but their actions still depend on sensors that can fail. When the policy is frozen or inaccessible, can an external monitor diagnose and repair corrupted inputs without access to its internals? We test a structured surrogate that separates periodic gait from sensor-dependent corrections to guide input repair around a frozen locomotion policy. On simulated Go2, offline diagnosis raises walking success from 259/640 to 429/640 episodes; online repair reaches 382/640, with no triggers in 64 held-out fault-free episodes. A matched boosted-tree surrogate predicts clean actions similarly well but yields no detected repair improvement over no repair. Separate fits improve walking on Go1 and ANYmal C, although phase-aware gradients perform better. Evidence remains limited to one policy and a partly screened simulated fault suite; robot foundation model and hardware validation remain open.

</details>

---

### [[20_Research/Papers/具身智能/HC2Robot_Hyper-Connection_Transformers_with_Predicted_Foresight_for_Multi-Terrain_Humanoid_Parkour|HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour]]

![[assets/2610.36825_figure.png|800]]

- **arXiv**: [2610.36825](https://arxiv.org/abs/2610.36825)
- **PDF**: https://arxiv.org/pdf/2610.36825
- **详细分析**: [[20_Research/Papers/具身智能/HC2Robot_Hyper-Connection_Transformers_with_Predicted_Foresight_for_Multi-Terrain_Humanoid_Parkour|HC2Robot: Hyper-Connection Transformers with Predicted Foresight for Multi-Terrain Humanoid Parkour]]
- **作者**: Wenhao Xu, Yanheng Mai, Yifei Fu, Nan Zheng, Yanbo Zhou, Zirui Huang, Mingsheng Ling, Xinjue Wang, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

人形机器人越障跑酷需要在楼梯、缺口、高台和斜坡等高度不连续地形上，提前判断未来落脚点并协调全身运动，这对感知、时序推理和接触时机控制都提出了很高要求。现有基于非对称 actor-critic 的感知式运动方法，训练时往往依赖仿真器中的特权信息，而部署时只能使用机载感知，导致训练与部署之间存在明显的信息鸿沟。本文关注的关键问题不是把特权信息直接暴露给 actor，而是学习一个可部署的近似表示来弥合这一鸿沟，因此具有较强的现实部署价值。

#### 方法概述和架构

论文提出 HC2Robot，由 Predicted Foresight Module（PFM）和 Hyper-Connection（HC）Transformer 组成，用于多地形人形跑酷。PFM 只基于可部署的深度图与本体感知，预测每只脚下一次落脚事件的时间、位置以及支撑质量，把原本只能在训练中利用的特权监督转化为一个可部署的潜在预测表示。HC Transformer 则在时序主干中引入多流路由与可学习的跨层聚合/混合机制，以增强对历史信息的复用和未来相关依赖的建模能力。训练阶段，critic 仍可接收仿真器中的特权状态，而 actor 仅接收机载深度与本体感知，再融合 PFM 的落脚预测与短时未来运动先验；推理阶段不需要任何特权传感。整体上，方法通过“预测未来接触事件 + 多流时序建模 + 训练时特权、部署时可用”的设计，缩小了训练与真实部署之间的感知差距。

#### 实验结果分析

作者在楼梯、缺口、高平台和斜坡等四类挑战地形上进行了实验，并与强基线感知运动方法比较。结果显示，HC2Robot 在仿真中的平均通过成功率达到 97.60%，且安全落脚率持续优于对比方法，说明其不仅能更稳定地完成越障，也能提升几何支撑质量。节选内容还提到作者做了辅助诊断与消融实验，以及真实机器人部署验证；但可见文本未给出这些部分的具体数值。

<details>
<summary>完整摘要</summary>

人形跑酷要求机器人在高度不连续的地形上推理未来落脚点以及全身运动。我们重新审视感知式人形运动中非对称 actor-critic 学习的信息不对称问题：critic 在训练时使用特权的仿真器信号，而可部署的 actor 只能依赖机载感知。我们认为，关键并不是把特权信息直接暴露给 actor，而是学习一个可部署的近似表示，以缩小训练与部署之间的信息差距。为此，我们提出 HC2Robot，这是一种可部署的感知式人形跑酷框架，由 Predicted Foresight Module（PFM）和 Hyper-Connection（HC）Transformer 组成。PFM 从可部署观测中预测每只脚下一次落脚事件的策略条件化时间、位置和支撑质量，将特权监督转换为一个可部署的潜在表示，从而在不使用特权运行时感知的情况下，为 actor 提供预测的落脚信息。HC Transformer 通过可学习的多流路由进一步增强时序推理能力，同时引入一个未来运动预测头，提供短时运动先验用于正则化。在楼梯、缺口、高平台和斜坡等场景中，HC2Robot 实现了 97.60% 的仿真平均通过成功率，并且在安全落脚率上持续优于强感知运动基线，表明其在可部署感知条件下能够提升越障性能和几何支撑能力。

</details>

---

### [[20_Research/Papers/强化学习/RynnWorld-Latent_A_Cross-Embodiment_World_Model_Conditioned_on_Universal_Latent_Actions|RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions]]

![[assets/2610.36791_figure.png|800]]

- **arXiv**: [2610.36791](https://arxiv.org/abs/2610.36791)
- **PDF**: https://arxiv.org/pdf/2610.36791
- **详细分析**: [[20_Research/Papers/强化学习/RynnWorld-Latent_A_Cross-Embodiment_World_Model_Conditioned_on_Universal_Latent_Actions|RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions]]
- **作者**: Haoyu Zhao, Yinzhou Tang, Zixuan Wang, Minghao Zhu, Dongchi Huang, Xingyue Zhao, Qin Zhao, Kehan Li, Siteng Huang, Xin Li, Zhenyu Zeng, Mingxiu Chen...
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《RynnWorld-Latent: A Cross-Embodiment World Model Conditioned on Universal Latent Actions》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, RynnVLA, RynnWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning controllable world dynamics from heterogeneous interaction videos is challenging because robot embodiments use incompatible action spaces, while human videos lack native control labels. We present RynnWorld-Latent, a cross-embodiment video world model that uses the 3D-grounded latent actions introduced by RynnLAM as a shared conditioning interface. This representation enables joint pretraining on human interaction videos, robot demonstrations, and simulation rollouts without requiring a common native action space. Built on a pretrained video transformer, RynnWorld-Latent combines global action tokens with an identity-initialized local pathway that aligns actions with future video latents. We pretrain on 23 datasets comprising approximately 553.5M frames and adapt the model to target robots through post-training. The framework supports two data-generation routes: digital teleoperation uses target robot commands to generate action-video demonstrations, while latent-action synthesis transfers source motion to an edited initial frame and pairs the resulting rollout with retargeted pseudo robot actions. Experiments show improved video prediction metrics on public benchmarks and two real-robot platforms, alongside qualitative action following when different action sequences share the same initial observation. Synthetic mid-training improves policy success rates on LIBERO and LIBERO-Plus, and both generation routes improve real-world policy success rates over real-demonstration-only training in the evaluated settings. These results support universal latent actions as a scalable interface for learning controllable visual dynamics across heterogeneous embodiments.

</details>

---

### [[20_Research/Papers/具身智能/A_fully_articulated_humanoid_dexterous_hand_with_human-level_joint_structure_enabled_by_linkage-based_actuation|A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation]]

![[assets/2610.36789_first_page.png|800]]

- **arXiv**: [2610.36789](https://arxiv.org/abs/2610.36789)
- **PDF**: https://arxiv.org/pdf/2610.36789
- **详细分析**: [[20_Research/Papers/具身智能/A_fully_articulated_humanoid_dexterous_hand_with_human-level_joint_structure_enabled_by_linkage-based_actuation|A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation]]
- **作者**: Jihao Li, Jianguo Wang, Haotian Guo, Yanzhe Wang, Guodong Lu, Huixu Dong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.6（加权：具身智能 3.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《A fully articulated humanoid dexterous hand with human-level joint structure enabled by linkage-based actuation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid dexterous hands are a core component of embodied intelligence, enabling robots to translate high-level intent into rich and adaptive physical interaction. However, existing designs remain constrained by a persistent trade-off among anthropomorphic kinematic complexity, mechanical robustness, load capacity and control simplicity, limiting dexterous manipulation in unstructured environments. Here we present Torch-Hand, a fully articulated humanoid dexterous hand that replicates the joint structure and motion hierarchy of the human hand with 21 degrees of freedom (DOF), comprising a highly articulated five-DOF thumb and four DOF in each of the remaining fingers. The differentiated thumb integrates multi-axis CMC motion to provide broad opposition and flexible contact orientation relative to the four fingers. Unlike tendon-driven or hybrid actuation approaches, Torch-Hand adopts an entirely linkage-based transmission architecture. By integrating screw-linkage actuation, the hand achieves high grasping force and substantial payload capacity while maintaining a compact anthropomorphic form. Its actuation architecture is optimized for control tractability, with all actuators integrated within the palm and arranged in a serial-robot-like configuration that establishes a direct correspondence between motor motion and joint kinematics. This architecture mechanically decouples functional DOF to reduce unintended inter-joint motion propagation, while allowing independently addressable DOF to be actively coordinated into coupled multi-joint motion patterns during complex manipulation. Comprehensive experiments assess reachable workspace, coordinated fingertip trajectories, thumb opposition, 33-grasp taxonomy coverage, grasping force, payload capacity and task-level manipulation. These results establish Torch-Hand as a robust hardware foundation for dexterous embodied manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Side-by-Side_Navigation_for_Personal_Mobility_Vehicles_from_Human_Drivers|Learning Side-by-Side Navigation for Personal Mobility Vehicles from Human Drivers]]

![[assets/2610.36726_figure.png|800]]

- **arXiv**: [2610.36726](https://arxiv.org/abs/2610.36726)
- **PDF**: https://arxiv.org/pdf/2610.36726
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Side-by-Side_Navigation_for_Personal_Mobility_Vehicles_from_Human_Drivers|Learning Side-by-Side Navigation for Personal Mobility Vehicles from Human Drivers]]
- **作者**: Luis Yoichi Morales, Florent Ferreri
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Learning Side-by-Side Navigation for Personal Mobility Vehicles from Human Drivers》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an approach to achieve side-by-side autonomous motion with a pair of personal mobility vehicles (PMVs). Given a global path, two PMVs plan cooperatively so as to hold a social formation that lets the passengers hold a conversation, while keeping the ride safe and smooth. Each vehicle runs its own sampling-based model-predictive planner; the planners exchange nothing but the odometry each vehicle could observe of the other, and the joint decision is expressed as a pair of utility matrices over pairs of candidate trajectories, resolved by a common rule. The behavioural parameters are fitted by inverse reinforcement learning from 409 minutes of driving by ten pairs of people in human-driven PMVs in an indoor environment, and the lanes the pair can use are derived offline from the corridor itself rather than fixed by hand. A safety layer the cost cannot override executes a move only if the vehicle can still brake clear, measured from its whole body, and a vehicle that is stuck reverses along its own path and continues. In closed-loop simulation over 24 runs in the conditions the drivers were recorded in and 24 in four generated obstacle layouts, no vehicle entered a wall or a cone. The pair holds conversational formation for 60.5 and 68.9 percent of the time among obstacles (anticlockwise and clockwise) and 81.2 and 91.5 percent in a clear aisle, against the drivers' 34.0 and 36.0 percent, and 52.9 and 56.0 percent, and it matches their speed. It keeps one lateral formation where the drivers alternated between a close diagonal and a wide abreast one, and it varies far less. Experimental results are based on a differential drive kinematic simulator running on ROS 2.

</details>

---

### [[20_Research/Papers/具身智能/RoboSTD_Zero-Shot_Single-to-Dual_Transfer_via_Sagittal_Mirroring_for_Bimanual_Learning|RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning]]

![[assets/2610.36685_figure.png|800]]

- **arXiv**: [2610.36685](https://arxiv.org/abs/2610.36685)
- **PDF**: https://arxiv.org/pdf/2610.36685
- **详细分析**: [[20_Research/Papers/具身智能/RoboSTD_Zero-Shot_Single-to-Dual_Transfer_via_Sagittal_Mirroring_for_Bimanual_Learning|RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning]]
- **作者**: Hongyu Wu, Chong Liu, Shaoxuan Xie, Shaqi Luo, Hanyu Feng, Shihan Wu, Guocai Yao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《RoboSTD: Zero-Shot Single-to-Dual Transfer via Sagittal Mirroring for Bimanual Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual robot manipulation plays an important role in real-world robotic applications, but the high cost of collecting bimanual demonstrations limits the scalable development of bimanual policy learning. Meanwhile, existing single-arm manipulation data are difficult to directly transfer to bimanual systems due to the Single-to-Dual gap in action spaces, coordination requirements, and arm-side spatial preference. To address this issue, we propose RoboSTD, a zero-shot Single-to-Dual data construction method for bimanual robot learning. RoboSTD first applies sagittal-plane mirroring to observations, proprioception, and actions to construct executable contralateral pseudo-demonstrations. It then uses an LLM to generate structured spatio-temporal coordination constraints that guide the reconstruction of pseudo-bimanual supervision across workspace regions and task stages. We evaluate RoboSTD on the AgileX ALOHA platform in both RoboTwin simulation and real-world settings. Experiments demonstrate the effectiveness of RoboSTD for bimanual policy learning. Without requiring additional bimanual demonstrations, RoboSTD increases the average number of collected cups to 2.11x that of the single-arm baseline in the cup collection task. Project page: https://huahungy.github.io/RoboSTD/

</details>

---

### [[20_Research/Papers/机器人/Mimetic_Embodiment_Transfer_of_Human-Humanoid_Interaction_from_In-the-Wild_Videos|Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos]]

![[assets/2610.36615_figure.png|800]]

- **arXiv**: [2610.36615](https://arxiv.org/abs/2610.36615)
- **PDF**: https://arxiv.org/pdf/2610.36615
- **详细分析**: [[20_Research/Papers/机器人/Mimetic_Embodiment_Transfer_of_Human-Humanoid_Interaction_from_In-the-Wild_Videos|Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos]]
- **作者**: Nghia Le, Khang Nguyen, Ba Long Tran, Thi Quynh Nhu Pham, Binh Nguyen, Tuong Do, Erman Tjiputra, Hoan Nguyen, Tung D. Ta, Baoru Huang, Hai-Nguyen, Nguyen...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Mimetic Embodiment Transfer of Human-Humanoid Interaction from In-the-Wild Videos》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enabling a humanoid to interact naturally with human partners requires preserving not only individual motions but also the spatial, semantic, and contact relationships underlying the interaction (i.e., hugging, dancing, hand-shaking, etc.). Furthermore, a practical solution should generalize across various humanoid embodiments with distinct morphologies and kinematic constraints. To tackle this challenge, we propose HumiTransfer, a mimetic embodiment transfer framework that converts in-the-wild human-human interaction videos into physically plausible human-humanoid interactions. HumiTransfer first reconstructs 3D human motion with consistent foot-ground contact, then transfers one participant to a target humanoid embodiment via interaction modeling, using weighted joint-relative directions and anatomical offsets to prioritize interaction-critical inter-body relationships, while post-retargeting optimization enforces balance, contact, and collision avoidance. Subsequently, we apply HumiTransfer to 1,200 in-the-wild videos, producing approximately 500,000 frames of diverse interactions for the 26-DoF Unitree R1 Edu and the 23-DoF HighTorque Mini-hi humanoid robot, resulting in our HumiMimic dataset. Across both robots, HumiTransfer achieves superior motion fidelity, preserves inter-body relationships, and maintains contact accuracy compared with existing baselines. Moreover, we demonstrate that HumiMimic supports motion generation methods for synthesizing interactive humanoid motions following a human partner. Finally, our real robot deployments confirm the physical executability of the transferred motions in real-world settings.

</details>

---

### [[20_Research/Papers/机器人/CARD_Contact-Anchored_Retargeting_for_Dexterous_Manipulation|CARD: Contact-Anchored Retargeting for Dexterous Manipulation]]

![[assets/2610.36539_figure.png|800]]

- **arXiv**: [2610.36539](https://arxiv.org/abs/2610.36539)
- **PDF**: https://arxiv.org/pdf/2610.36539
- **详细分析**: [[20_Research/Papers/机器人/CARD_Contact-Anchored_Retargeting_for_Dexterous_Manipulation|CARD: Contact-Anchored Retargeting for Dexterous Manipulation]]
- **作者**: Cunxi Dai, Botao He, Francois R Hogan, Wei Pan, Rao Fu, Wen-Han Hsieh, Ruoshi Liu, Jitendra Malik, Guanya Shi, Akash Sharma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《CARD: Contact-Anchored Retargeting for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans are dexterous, but traditional data collection paradigms such as teleoperation, kinesthetic teaching, and wearable exoskeletons force humans to act through the robot embodiment, bottlenecking their dexterity. Retargeting can avoid this. However, existing methods purely translate kinematics and ignore the real-world contact dynamics essential for task success. We present CARD: Contact-Anchored Retargeting for Dexterous Manipulation, a simulator and object-free framework that retargets human demonstrations to robot actions by explicitly preserving contact force targets. CARD unifies human data sources including video, motion capture, and tactile gloves via a shared hand--contact representation and generates explicit contact force targets in addition to kinematics. To maintain these contact targets during hardware open-loop replay, CARD also introduces a tactile tracking controller. For video which does not contain an explicit tactile source, we present Vid-HACO, our video-to-contact model that sets a new state of the art. Across our video, glove, motion-capture data and the GRAB dataset, CARD maintains contact on $43$--$78\%$ of contact frames, while kinematic and object-aware retargeting methods maintain contact on $&lt;10\%$ and $22.5\%$ of the frames respectively. Further, integrating our formulation into physics-based retargeting improves strict task success from 12\% to 32\% on GRAB dataset. Finally, we show that our tactile tracker is critical to reproduce demonstrated forces during hardware replay. These results establish that contact preservation via CARD is a scalable interface for transferring human dexterity to robots.

</details>

---

### [[20_Research/Papers/具身智能/A_Trainable_CPG_Framework_for_Quadruped_Locomotion|A Trainable CPG Framework for Quadruped Locomotion]]

![[assets/2610.36537_figure.png|800]]

- **arXiv**: [2610.36537](https://arxiv.org/abs/2610.36537)
- **PDF**: https://arxiv.org/pdf/2610.36537
- **详细分析**: [[20_Research/Papers/具身智能/A_Trainable_CPG_Framework_for_Quadruped_Locomotion|A Trainable CPG Framework for Quadruped Locomotion]]
- **作者**: Xiyan Liu, Yide Liu, Guoyong Mao, Shaoxing Qu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《A Trainable CPG Framework for Quadruped Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CPG-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present CPG-ENN, a trainable quadruped locomotion framework that combines explicit neural coordination with learned motion realization. A symmetry-based eight-neuron central pattern generator (CPG) supplies gait rhythms, while a pretrained, leg-shared execution neural network (ENN) maps rhythmic signals and trajectory parameters to joint-angle references without online inverse kinematics. A single feedback policy modulates six physically interpretable trajectory variables. The controller tracks planar velocity and yaw-rate commands across walk, trot, pace, bound, and pronk without gait-specific learned controllers or transitionspecific rewards. Simulation yields 99.39% transition success across all 20 directed gait pairs and all source-target speed combinations from {0.5, 1.0, 1.5, 2.0} m/s. Ablations show high cross-gait transition feasibility without transition exposure; exposure mainly refines gait acquisition and velocity transients. Comparisons with AllGaits and Walk These Ways demonstrate accurate gait-speed regulation, and Unitree Go2 experiments validate five gaits and their transitions.

</details>

---

### [[20_Research/Papers/具身智能/GRAFT_Geometry-Aware_Residual_Adaptation_for_Foundation_Trackers|GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers]]

![[assets/2610.36507_figure.png|800]]

- **arXiv**: [2610.36507](https://arxiv.org/abs/2610.36507)
- **PDF**: https://arxiv.org/pdf/2610.36507
- **详细分析**: [[20_Research/Papers/具身智能/GRAFT_Geometry-Aware_Residual_Adaptation_for_Foundation_Trackers|GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers]]
- **作者**: Liang Li, Guoyao Zhang, Xingyu Chen, Sikai Wu, Qianyang Wu, Yuhang Lin, Renjing Xu, Mingliang Zhou, Diyun Xiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《GRAFT: Geometry-Aware Residual Adaptation for Foundation Trackers》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid behavior foundation models (BFMs) provide reusable whole-body motion priors: given a kinematic reference, they generate coordinated joint commands for motion replay, teleoperation, and VLA control. However, trained primarily on flat-ground motion, BFMs lack an explicit mechanism to adapt foot placement, swing clearance, and contact timing to local terrain. Many terrain-aware BFM approaches address this limitation by retraining or fine-tuning the tracker together with perception, incurring substantial data and computation costs while coupling ordinary tracking to the perception pathway. To bridge this gap, we propose GRAFT, a geometry-aware residual adaptation framework for frozen behavior trackers. GRAFT preserves the BFM parameters and motion-reference interface, while a lightweight adapter adds terrain-conditioned corrections only to lower-body execution targets. The adapter is trained with task and foot-geometry rewards, regularized to suppress unnecessary corrections on flat ground, and distilled from privileged terrain observations to onboard depth. Because the frozen BFM already provides whole-body reference tracking and nominal locomotion, GRAFT reduces terrain learning to a focused execution-adaptation problem. We instantiate the framework on four frozen trackers and evaluate stairs, gaps, and platforms in simulation. We further validate it through real-world deployment on a Unitree G1, where the adapted SONIC tracker traverses terrain with onboard depth and unmodified references.

</details>

---

### [[20_Research/Papers/具身智能/SG^2SLAM_Spatial_Geometry-Informed_3D_Gaussian_Splatting_SLAM_for_Monocular_Outdoor_Navigation|SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation]]

![[assets/2610.36312_figure.png|800]]

- **arXiv**: [2610.36312](https://arxiv.org/abs/2610.36312)
- **PDF**: https://arxiv.org/pdf/2610.36312
- **详细分析**: [[20_Research/Papers/具身智能/SG^2SLAM_Spatial_Geometry-Informed_3D_Gaussian_Splatting_SLAM_for_Monocular_Outdoor_Navigation|SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation]]
- **作者**: Ziang Guo, Didar Seyidov, Yixiao Zhou, Xuefeng Zhang, Ali Alridha Abdulkarim, Chen Min, Zufeng Zhang, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: EmbodiedAI, ComputerVision, Systems

#### 研究背景与动机

《SG^2SLAM: Spatial Geometry-Informed 3D Gaussian Splatting SLAM for Monocular Outdoor Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular outdoor navigation requires robust camera motion estimation and a dense, navigable map, where 3D Gaussian Splatting SLAM serves this task through an explicit differentiable parameterization and closed-form projection. However, typically, the geometry is recovered by associating 2D pixels with 3D points, so a modular SLAM system absorbs tracking error into the map, leading to cascading degradation. To address these gaps, we present SG^2SLAM, which couples streaming spatial geometry with a ray-conditioned 3DGS kernel. Streaming spatial geometry replaces the per- frame cross-dimensional correspondence with a chunk-level metric prior that supervises tracking and mapping from one source. A ray-conditioned kernel extends each primitive with a viewing-direction subspace that senses the monocular camera viewpoints. The joint optimization over spatial geometry and poses ensures a globally consistent map and trajectory outcome. Experiments on the KITTI and Waymo Open datasets show that our SG^2SLAM surpasses the per-frame association baselines in the monocular outdoor navigation task. Code will be made publicly available upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/ASPEN_Adaptive_Semantic_Reasoning_via_Command_Persistence_Prediction_for_Efficient_Navigation_VLAs|ASPEN: Adaptive Semantic Reasoning via Command Persistence Prediction for Efficient Navigation VLAs]]

![[assets/2610.36285_figure.png|800]]

- **arXiv**: [2610.36285](https://arxiv.org/abs/2610.36285)
- **PDF**: https://arxiv.org/pdf/2610.36285
- **详细分析**: [[20_Research/Papers/具身智能/ASPEN_Adaptive_Semantic_Reasoning_via_Command_Persistence_Prediction_for_Efficient_Navigation_VLAs|ASPEN: Adaptive Semantic Reasoning via Command Persistence Prediction for Efficient Navigation VLAs]]
- **作者**: Vieri N. Akustia, Bin Hu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《ASPEN: Adaptive Semantic Reasoning via Command Persistence Prediction for Efficient Navigation VLAs》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FlashVLA, OpenVLA, SP-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigation vision-language-action (VLA) policies repeatedly invoke costly semantic reasoning even when the next command remains unchanged. Command reuse can reduce computation but risks missing instruction-dependent turns or stops. We introduce ASPEN, an event-triggered scheduler based on command persistence prediction: estimating whether the frozen base policy would reissue its previous command. A lightweight multimodal predictor combines temporal observations, language instructions, execution history, and cached VLA confidence. At eligible command boundaries, sufficient predicted persistence permits command reuse. Otherwise, ASPEN triggers fresh semantic reasoning from the VLA. Evaluated with frozen NaVILA on cross-dataset RxR-CE val-unseen, ASPEN reduces VLA calls by 9.5% and estimated inference time by 8.1%, including scheduling overhead. It maintains comparable navigation performance and preserves identical baseline action sequences on 92.1% of episodes.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Multi-Phase_Robot_Loco-Manipulation_via_Phase-Conditioned_Policy_Optimization|Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization]]

![[assets/2610.36270_figure.png|800]]

- **arXiv**: [2610.36270](https://arxiv.org/abs/2610.36270)
- **PDF**: https://arxiv.org/pdf/2610.36270
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Multi-Phase_Robot_Loco-Manipulation_via_Phase-Conditioned_Policy_Optimization|Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization]]
- **作者**: Simone Manni, Annika Wollschläger, Dario Bellicoso, Abel Gawel, Marco Hutter, Simon Le Cleac'h, Jan Brüdigam
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.2，强化学习 0.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Complex whole-body loco-manipulation requires executing diverse maneuvers, such as crouching, grasping, and locomotion, within a single long-horizon task. While performing simple pick-and-place behaviors is well-established, scaling to complex, long-horizon tasks remains difficult. Currently, this challenge is addressed by relying on human motion data and correspondingly humanoid platforms, which limits platform independence and introduces substantial data processing overhead. Instead, we extend proximal policy optimization (PPO) to train a single policy for multi-phase tasks across diverse robotic hardware, leveraging prior task structure to shape behavior. Our method adapts PPO using a phase-conditioned critic, phase-gated reward functions, and a multi-phase reset curriculum to guide exploration. To support varied hardware, we employ a decoupled hierarchical control architecture that separates lower-level balancing dynamics from high-level phase execution. We demonstrate multi-stage loco-manipulation skills on hardware on both the Unitree G1 and a Boston Dynamics Spot equipped with a manipulator arm, and validate our design choices through ablations. Our approach enables the acquisition of complex loco-manipulation behaviors purely through environment interaction while directly incorporating high-level task structure into policy learning.

</details>

---

### [[20_Research/Papers/具身智能/Program-Level_Adversarial_Co-Adaptive_Self-Play_for_Robotic_Security|Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security]]

![[assets/2610.36143_figure.png|800]]

- **arXiv**: [2610.36143](https://arxiv.org/abs/2610.36143)
- **PDF**: https://arxiv.org/pdf/2610.36143
- **详细分析**: [[20_Research/Papers/具身智能/Program-Level_Adversarial_Co-Adaptive_Self-Play_for_Robotic_Security|Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security]]
- **作者**: Leo Benaharon, Chi Zhang, Wei Zheng, Weifan Zhang, Yifan Wei
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, Security

#### 研究背景与动机

《Program-Level Adversarial Co-Adaptive Self-Play for Robotic Security》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents can adapt robotic software by revising executable programs, but successful responses to an evolving opponent may not remain effective. We present a framework for program-level adversarial co-adaptive self-play in which coding agents generate attacks and defenses from tested opponent code and mission feedback, without model fine-tuning. Environment-specific interfaces support external programs for autonomous driving and SDK-level defenses for humanoid locomotion. Two eight-generation case studies reveal concrete software responses: a driving defender introduces direct-actuation recovery, while a humanoid defender revises incoming-state validation. These responses provide local task recovery but do not establish sustained robustness. The framework makes such adaptation and limitations observable through executable artifacts and task-level evidence.

</details>

---

### [[20_Research/Papers/具身智能/E0.5_From_Reconstructive_to_Future-Predictive_3D_Foundations_for_Robotic_World-Action_Modeling|E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling]]

![[assets/2610.36011_figure.png|800]]

- **arXiv**: [2610.36011](https://arxiv.org/abs/2610.36011)
- **PDF**: https://arxiv.org/pdf/2610.36011
- **详细分析**: [[20_Research/Papers/具身智能/E0.5_From_Reconstructive_to_Future-Predictive_3D_Foundations_for_Robotic_World-Action_Modeling|E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling]]
- **作者**: X-Era AI Lab Team, :, Jianhao Lai, Zhihao Zhan, Zhiquan Liao, Qichang Li, Shubin Chen, Zhiyuan Liu, Hongsen Lei, Jianman Lin, Xiaoxin Lin, Ke Gong...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.6，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《E0.5: From Reconstructive to Future-Predictive 3D Foundations for Robotic World-Action Modeling》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgiBotWorld, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models (WAMs) offer a promising framework for embodied intelligence, yet mainstream approaches remain centered on video foundation models or vision-language models. Even when geometric features extracted by 3D models such as VGGT are incorporated, they are typically passed into a video model or VLM that serves as the primary backbone, leaving 3D geometry as an auxiliary input or prediction target rather than the native foundation for world modeling. We present E0.5, a geometry-native world-action model built directly on 3D foundation models. E0.5 introduces two key innovations. First, it adopts a 3D foundation model as the primary backbone, making 3D geometry the native representation for both world modeling and action prediction. Second, it explicitly predicts future 3D states together with actions, enabling the model to capture geometric world dynamics beyond action-only modeling or future video prediction. Experiments on RoboTwin 2.0 first demonstrate the effectiveness of E0.5 without embodied-data pretraining, achieving success rates of 89.90\% and 50.09\% under clean and randomized settings, respectively. Building on these results, we further pretrain E0.5 on more than 160k robot trajectories from AgiBotWorld-Beta, jointly learning robot actions and future geometry within the pretrained 3D foundation. This embodied pretraining improves mean real-world manipulation success rates by approximately 15 and 7 percentage points on AgileX Piper and Zerith H1, respectively. Together, these results demonstrate the potential of geometry-native foundations to acquire robot interaction knowledge and transfer it to physical manipulation. E0.5 embodies this geometry-native approach as a member of the VWA family of world-action models.

</details>

---
