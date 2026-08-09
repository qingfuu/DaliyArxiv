# cs.HC | Human-Computer Interaction | 2026-08-07

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/机器人/Robot_Learning_from_Human_Demonstrations_Handwritten_Alphabet_Trajectories_and_Human-Likeness_Evaluation|Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation]]

![[assets/2608.06221_figure.png|800]]

- **arXiv**: [2608.06221](https://arxiv.org/abs/2608.06221)
- **PDF**: https://arxiv.org/pdf/2608.06221
- **详细分析**: [[20_Research/Papers/机器人/Robot_Learning_from_Human_Demonstrations_Handwritten_Alphabet_Trajectories_and_Human-Likeness_Evaluation|Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation]]
- **作者**: Alperen Kenan, Paul Bremner, Manuel Giuliani
- **cs 子类**: cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Robot Learning from Human Demonstrations: Handwritten Alphabet Trajectories and Human-Likeness Evaluation》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from demonstration (LfD) provides a developmental framework through which robots can develop motor skills by observing and imitating human dynamics, reducing reliance on explicit programming to teach a skill to a robot. The resulting human-like robot motion is recognised as a key factor in building trust and enabling natural collaboration in human-robot interaction. This paper presents a framework for learning human-like robot motion from demonstration, including data collection, probabilistic trajectory learning, and perceptual user evaluation. A dataset of 3,142 handwriting demonstrations was collected from 22 participants across all 52 Latin alphabet character-case combinations via a touchscreen teleoperation interface, capturing planar position, contact force, and timing. Building on the widely used Gaussian Mixture Model and Gaussian Mixture Regression approach for learning from demonstration, the framework is extended in this work by incorporating force and normalised time dimensions to enable richer representation of human dynamics, and adapting it to handle non-continuous, multi-segment trajectories, enabling generalisation across demonstrations. A user study with 21 participants evaluated the perceived human-likeness of the generated trajectories using a continuous scale anchored between robotic and human-like motion, normalised to 0-100 where 50 represents the neutral midpoint. The generated trajectories achieved an overall human-likeness score of 71.50 (SD=22.56), indicating that the majority of trajectories were perceived as more human-like. Participants identified geometric positioning and trajectory sequence as the most influential perceptual factors, and reported positive attitudes toward human-like robot behaviour. The datasets are released as open-source, providing a reproducible benchmark for developing and evaluating human-like robot motion methods.

</details>

---

### [[20_Research/Papers/机器人/Design_and_Evaluation_of_a_Touchscreen-Based_Teleoperation_Interface_for_Robotic_Manipulators|Design and Evaluation of a Touchscreen-Based Teleoperation Interface for Robotic Manipulators]]

![[assets/2608.06219_figure.jpg|800]]

- **arXiv**: [2608.06219](https://arxiv.org/abs/2608.06219)
- **PDF**: https://arxiv.org/pdf/2608.06219
- **详细分析**: [[20_Research/Papers/机器人/Design_and_Evaluation_of_a_Touchscreen-Based_Teleoperation_Interface_for_Robotic_Manipulators|Design and Evaluation of a Touchscreen-Based Teleoperation Interface for Robotic Manipulators]]
- **作者**: Juan José García Cárdenas, Alperen Kenan, Hamidreza Raei, Paul Bremner, Manuel Giuliani, Arash Ajoudani, Adriana Tapus
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Design and Evaluation of a Touchscreen-Based Teleoperation Interface for Robotic Manipulators》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Intuitive teleoperation interfaces are crucial for the safe and effective operation of robotic manipulators in challenging environments. In the nuclear industry, surface contact tasks such as swab sampling require precise path and force tracking, obstacle avoidance, and sustained operator attention, which conventional joystick interfaces struggle to support effectively. This study designs and evaluates a novel touchscreen teleoperation interface that maps continuous finger movements directly to robotic manipulator motions, provides finer velocity control, and integrates control with visualization, enabling more natural, precise, and intuitive surface interaction than conventional controllers. A comparative user study with 20 participants evaluated task performance and workload using the proposed touchscreen, a conventional joystick, and a single-click autonomous mode. Tasks simulated realistic surface manipulation using a Franka Emika Panda arm, remotely controlled from another country. Kinematic, physiological, and behavioral data were recorded to comprehensively assess task performance, cognitive load, and operator trust across each control condition. Participants completed teleoperation tasks more efficiently and accurately with the touchscreen interface, achieving a 53.5% reduction in completion time (median: 2.50 vs. 5.38 min), higher in-area coverage on the sinusoidal path (90.7% vs. 84.1%), and lower overshoot on both path geometries compared with the joystick. Cognitive load, quantified via NASA-TLX (0-100), decreased from joystick to touchscreen (mean TLX 52 to 43; -9 points, -17.3%) and was lowest under the autonomous one-click mode (31; -21 points vs. joystick, -40.4%; -12 vs. touchscreen, -27.9%). This research presents an easy-to-implement touchscreen interface that improves performance in teleoperated surface tasks while reducing cognitive load.

</details>

---

### [[20_Research/Papers/大模型/OneEmo_A_Unified_Multimodal_Reasoning_Model_for_Emotion_Perception,_Understanding,_and_Interaction|OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understanding, and Interaction]]

![[assets/2608.06013_figure.png|800]]

- **arXiv**: [2608.06013](https://arxiv.org/abs/2608.06013)
- **PDF**: https://arxiv.org/pdf/2608.06013
- **详细分析**: [[20_Research/Papers/大模型/OneEmo_A_Unified_Multimodal_Reasoning_Model_for_Emotion_Perception,_Understanding,_and_Interaction|OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understanding, and Interaction]]
- **作者**: Jiahao Huang, Zheng Lian, Jingyi Zhang, Zhide Chen, Xiaojiang Peng, Shaonan Wang
- **cs 子类**: cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《OneEmo: A Unified Multimodal Reasoning Model for Emotion Perception, Understanding, and Interaction》归入 大模型、强化学习 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EmoWorld, EmpRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Models (MLLMs) have demonstrated remarkable capabilities in emotional intelligence. However, prevailing research predominantly focuses on task-specific specialization, often neglecting inter-task synergy and leaving latent reasoning potential underexplored. To bridge this gap, we introduce OneEmo, a unified affective generalist capable of mastering emotion perception, comprehension, and interaction. For this purpose, we first construct EmoWorld-130K, a comprehensive dataset that distills specialized affective knowledge into explicit reasoning trajectories via a human-in-the-loop workflow. Supervised fine-tuning on this corpus reveals significant mutual benefits derived from multi-task learning. Second, to fully unlock the latent reasoning potential, we propose Emo-Chord, a novel reinforcement learning strategy that stabilizes optimization through unified multi-task reward allocation. Extensive experiments demonstrate that OneEmo achieves state-of-the-art performance against similarly sized baselines across most benchmarks. Notably, despite having significantly fewer parameters than commercial models, OneEmo delivers highly competitive results. This paper paves the way for more reliable and interpretable affective computing. The code is available at https://github.com/waHAHJIAHAO/OneEmo.

</details>

---

### [[20_Research/Papers/具身智能/SpaceVLA_Spatially_Grounded_VLA_for_Robotic_Manipulation_with_User-Authored_Grasp_and_Place_Anchors|SpaceVLA: Spatially Grounded VLA for Robotic Manipulation with User-Authored Grasp and Place Anchors]]

![[assets/2608.05730_figure.png|800]]

- **arXiv**: [2608.05730](https://arxiv.org/abs/2608.05730)
- **PDF**: https://arxiv.org/pdf/2608.05730
- **详细分析**: [[20_Research/Papers/具身智能/SpaceVLA_Spatially_Grounded_VLA_for_Robotic_Manipulation_with_User-Authored_Grasp_and_Place_Anchors|SpaceVLA: Spatially Grounded VLA for Robotic Manipulation with User-Authored Grasp and Place Anchors]]
- **作者**: Daniia Zinniatullina, Iaroslav Kolomiets, Mikhail Konenkov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.HC
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 2.4，机器人 0.6）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SpaceVLA: Spatially Grounded VLA for Robotic Manipulation with User-Authored Grasp and Place Anchors》归入 具身智能、机器人 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Bi-VLA, HapticVLA, OpenVLA, PointVLA, Shake-VLA, SpaceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models follow language commands but often lack explicit spatial intent for manipulation. We present Visual Intent Anchors, an XR pipeline that lets users specify grasp and placement regions and renders them as image-space overlays for VLA control. We collect 200 Unity pick-and-place demonstrations and fine-tune OpenVLA-7B with LoRA on temporally subsampled annotated observations. The policy predicts tokenized 7-DoF incremental actions from marked RGB observations and language. We evaluate the policy in closed-loop Unity trials, achieving a grasp success rate of 91.25% and mean grasp and placement errors of 0.5 cm and 0.7 cm, respectively.

</details>

---
