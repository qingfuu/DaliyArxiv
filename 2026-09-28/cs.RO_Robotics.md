# cs.RO | Robotics | 2026-09-28

#arxiv #ComputerScience

**论文数**: 48

### [[20_Research/Papers/强化学习/Learning_Robot_Policies_from_Sparse_Success_Signals_via_STL-Guided_Stein_Variational_Policy_Gradient|Learning Robot Policies from Sparse Success Signals via STL-Guided Stein Variational Policy Gradient]]

![[assets/2609.31606_figure.png|800]]

- **arXiv**: [2609.31606](https://arxiv.org/abs/2609.31606)
- **PDF**: https://arxiv.org/pdf/2609.31606
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Robot_Policies_from_Sparse_Success_Signals_via_STL-Guided_Stein_Variational_Policy_Gradient|Learning Robot Policies from Sparse Success Signals via STL-Guided Stein Variational Policy Gradient]]
- **作者**: Hongrui Zheng, Cristian Ioan Vasile, Antonio Loquercio, Rahul Mangharam
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Robot Policies from Sparse Success Signals via STL-Guided Stein Variational Policy Gradient》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning robot policies for tasks with sparse success signals is challenging when completion depends on coordinated actions, precise contact outcomes, or satisfying several conditions together. Intricate physical interactions with the world further complicate these requirements. Prior work using conventional reward shaping mechanisms provides dense feedback but local progress might not translate into eventual task completion. We present Signal Temporal Logic-guided Stein Variational Policy Gradient (STL-SVPG), a population-based method that uses smooth STL robustness as a trajectory-level training objective. Differentiating this objective through the dynamics assigns credit to policy actions according to their effect on the complete task specification, rather than local progress alone. We evaluate the approach on six quadcopter and manipulator tasks that involves event-triggered responses, strictly ordered behavior, responses within specified deadlines, and physical interaction with the world. STL-SVPG achieves the highest mean success rate among the compared methods on five of six benchmarks. Simulation-trained policies trained in simulation transfer temporal and contact task behavior to the real world.

</details>

---

### [[20_Research/Papers/具身智能/Generate,_Track,_Improve_Perceptive_Multi-Skill_Humanoid_Locomotion_with_RL-Fine-Tuned_Motion_Generators|Generate, Track, Improve: Perceptive Multi-Skill Humanoid Locomotion with RL-Fine-Tuned Motion Generators]]

![[assets/2609.31577_figure.png|800]]

- **arXiv**: [2609.31577](https://arxiv.org/abs/2609.31577)
- **PDF**: https://arxiv.org/pdf/2609.31577
- **详细分析**: [[20_Research/Papers/具身智能/Generate,_Track,_Improve_Perceptive_Multi-Skill_Humanoid_Locomotion_with_RL-Fine-Tuned_Motion_Generators|Generate, Track, Improve: Perceptive Multi-Skill Humanoid Locomotion with RL-Fine-Tuned Motion Generators]]
- **作者**: Zachary Olkin, William D. Compton, Aaron D. Ames
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Generate, Track, Improve: Perceptive Multi-Skill Humanoid Locomotion with RL-Fine-Tuned Motion Generators》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CLF-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General purpose humanoids require locomotion controllers that are multi-skill, perceptive, dynamic, and robust enough to go anywhere humans can. In this work, we present a two layer locomotion architecture: (1) a perceptive flow matching motion generator plans whole body trajectories from raw depth images while a (2) perceptive tracking policy trained with control-guided RL follows these motions. Both policies are trained on a library of terrain consistent motion clips created with dynamically optimized human data which yields both accurate velocity tracking and terrain consistent references. Our central contribution is a simple yet effective off-policy RL fine tuning loop that improves the motion generator. A structured search method is used with the generator to gather data for advantage weighted regression. This off-policy loop is much more sample efficient than on-policy residual fine tuning and improves terrain consistency on unseen geometries and skill compositions. We find that successful terrain traversals increased by up to 25 percentage points and skill selection improved by up to 80 percentage points. By using raw depth images to perceive the environment no odometry or height maps are needed, and outdoor deployment is easy. With two cameras, the policy can see terrain coming from further away and adjust its velocity regardless of the commanded speed so it can traverse the terrain. A single policy pair enables a Unitree G1 humanoid to walk, run, stand, jump on and off of boxes, and traverse stairs in outdoor environments. Project page: https://zolkin1.github.io/generate-track-improve/

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Leverage_Compliance_A_Policy-Admittance_Learning_Framework_for_Robotic_Insertion|Learning to Leverage Compliance: A Policy-Admittance Learning Framework for Robotic Insertion]]

![[assets/2609.31439_figure.png|800]]

- **arXiv**: [2609.31439](https://arxiv.org/abs/2609.31439)
- **PDF**: https://arxiv.org/pdf/2609.31439
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Leverage_Compliance_A_Policy-Admittance_Learning_Framework_for_Robotic_Insertion|Learning to Leverage Compliance: A Policy-Admittance Learning Framework for Robotic Insertion]]
- **作者**: Chongren Wang, Minghe Li, Honghua Dai, Zhicheng Lin, Shiyang Wei, Xiaokui Yue
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning to Leverage Compliance: A Policy-Admittance Learning Framework for Robotic Insertion》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HIL-SERL, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policy learning and compliant control offer a promising route to reliable autonomous assembly under pose errors and contact uncertainty. However, combining them does not ensure coordination: the policy may continue pushing against contact while the controller yields, producing sustained loading with limited progress. To address this problem, we propose LeCo (Leverage Compliance), a policy-admittance learning framework that guides a visual policy through execution-time interaction under fixed admittance. A multirate feedback mechanism aggregates high-rate contact-interaction records into policy-transition rewards. An integrated conflict cost then characterizes sustained policy-loading/controller-unloading opposition, while a directional high-force tail cost captures continued-loading events within a transition. Together with task completion, these costs encourage the policy to leverage compliance with less unproductive loading. We evaluate LeCo on four real connector-assembly tasks, obtaining an aggregate success rate of 94%. Across tasks, mean successful-trial resultant-force and torque peaks decrease by approximately 30% and 64% relative to the comparison baseline. Reward ablation further shows that adding conflict shaping reduces median successful-trial contact-conditioned conflict density by approximately 53%. These results support learning to leverage fixed compliance by turning multirate policy-admittance interaction into complementary reward signals for effective, lower-load insertion.

</details>

---

### [[20_Research/Papers/具身智能/ExoLaN_Physics-Consistent_Context-Aware_Dynamics_Learning_for_Exoskeletons|ExoLaN: Physics-Consistent Context-Aware Dynamics Learning for Exoskeletons]]

![[assets/2609.31434_first_page.png|800]]

- **arXiv**: [2609.31434](https://arxiv.org/abs/2609.31434)
- **PDF**: https://arxiv.org/pdf/2609.31434
- **详细分析**: [[20_Research/Papers/具身智能/ExoLaN_Physics-Consistent_Context-Aware_Dynamics_Learning_for_Exoskeletons|ExoLaN: Physics-Consistent Context-Aware Dynamics Learning for Exoskeletons]]
- **作者**: Lucas Schulze, Maximilian Schwarz, Jona Hoppe, Jan Peters, Oleg Arenz
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.1（加权：具身智能 0.6，世界模型 0.2，机器人 0.3）
- **关联关键词**: Robotics, WorldModel, Systems

#### 研究背景与动机

《ExoLaN: Physics-Consistent Context-Aware Dynamics Learning for Exoskeletons》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task-agnostic assistive exoskeleton control based on human intention offers greater flexibility than conventional approaches that rely on predefined tasks or motion patterns. Human joint torque estimation enables task-agnostic assistance by characterizing user actions. Physics-consistent methods such as Deep Lagrangian Networks (DeLaN) have been applied to estimate the human torques in multi-user settings, but existing approaches cannot adapt to a specific user without retraining, and do not account for intermittent contacts during locomotion. We propose ExoLaN, a Context-Aware DeLaN for human-exoskeleton interaction that learns the full coupled system dynamics while adapting to changes in interaction context. ExoLaN combines temporal context with partial contact-force measurements from force-sensitive insoles to infer latent dynamics embeddings and estimate generalized contact torques. On seven unseen users performing 21 unseen tasks, ExoLaN reduces torque estimation MSE by 7% compared to a black-box baseline. Beyond inverse dynamics, ExoLaN serves as a unified model that also enables accurate forward prediction: training with a multi-step prediction loss reduces acceleration MSE by 59% and long-horizon position and velocity errors by 60% and 93%, respectively, compared with a single-step loss. Moreover, the learned latent context captures task information without explicit task labels, making it a promising signal for task-aware assistive control.

</details>

---

### [[20_Research/Papers/具身智能/CognitiveReality_Robot-Agnostic_Semantic_Gaussian_Mapping_with_an_LLM_Agent_for_Immersive_Collaborative_VR_Teleoperation|CognitiveReality: Robot-Agnostic Semantic Gaussian Mapping with an LLM Agent for Immersive Collaborative VR Teleoperation]]

![[assets/2609.31418_figure.png|800]]

- **arXiv**: [2609.31418](https://arxiv.org/abs/2609.31418)
- **PDF**: https://arxiv.org/pdf/2609.31418
- **详细分析**: [[20_Research/Papers/具身智能/CognitiveReality_Robot-Agnostic_Semantic_Gaussian_Mapping_with_an_LLM_Agent_for_Immersive_Collaborative_VR_Teleoperation|CognitiveReality: Robot-Agnostic Semantic Gaussian Mapping with an LLM Agent for Immersive Collaborative VR Teleoperation]]
- **作者**: Timofei Kozlov, Dmitrii Maliukov, Andrey Marchenko, Dmitrii Plotnikov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.7，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《CognitiveReality: Robot-Agnostic Semantic Gaussian Mapping with an LLM Agent for Immersive Collaborative VR Teleoperation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Agent-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A photorealistic 3D view tells a teleoperator where a robot is, but not what the scene contains, how well each object has been observed, or how to turn pointing and speech into robot action. CognitiveReality turns a robot's RGB-D stream into a live, semantically indexed Gaussian-TSDF map shared by an operator in virtual reality and a tool-using language agent. One mapper binary serves any platform through configuration alone: it ingests poses from robot SLAM, joint kinematics, motion capture or an inline visual tracker, bridges localization outages with a shadow tracker and keyframe-anchored PnP, and maintains open-vocabulary instance identities with per-object quality at 2 Hz. Speech and controller rays are grounded against persistent scene objects through validated typed tools and operator-confirmed robot actions. In the controlled agent evaluation, the deployed local Qwen3-VL-8B router reaches 81.24\% tool exact match, while merge-aware replay correctly redirects 101 absorbed object identifiers. On robot data CognitiveReality exceeds a Gaussian-plus-SDF baseline by 2-8 dB; pose error through 5-40 s SLAM outages stays within 1-8 cm. Deployed live on two quadrupeds, the agent executed 26 of 30 navigation requests and 20 of 20 re-observation requests, raising object quality by 2-5 dB.

</details>

---

### [[20_Research/Papers/机器人/dRVG_Quadtree-Guided,_Resolution-Complete_Online_Motion_Planning_for_Polygonal_Robots_in_Unknown_Environments|dRVG: Quadtree-Guided, Resolution-Complete Online Motion Planning for Polygonal Robots in Unknown Environments]]

![[assets/2609.31412_figure.png|800]]

- **arXiv**: [2609.31412](https://arxiv.org/abs/2609.31412)
- **PDF**: https://arxiv.org/pdf/2609.31412
- **详细分析**: [[20_Research/Papers/机器人/dRVG_Quadtree-Guided,_Resolution-Complete_Online_Motion_Planning_for_Polygonal_Robots_in_Unknown_Environments|dRVG: Quadtree-Guided, Resolution-Complete Online Motion Planning for Polygonal Robots in Unknown Environments]]
- **作者**: Duo Zhang, Hechen Zhang, Junshan Huang, Jingjin Yu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《dRVG: Quadtree-Guided, Resolution-Complete Online Motion Planning for Polygonal Robots in Unknown Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present the dynamic rotation-stacked visibility graph (dRVG), an online motion planner that guides polygonal robots to specified goals in initially unknown, static environ- ments. It merges local roadmaps from successive observations to plan collision-free translations and rotations without a uniform position grid. A spatial quadtree schedules sensing goals across regions to reduce repeated visits while retaining all orientation configurations for routing. Under exact sensing and geometric computation and star-shaped robot and envelope assumptions, dRVG with center scans is resolution-complete relative to full- map RVG at the same angular resolution. In experiments using footprint scans, dRVG solves all 140 cases across 20 difficult maps and seven angular resolutions within a 20 s planning budget, with a median planning time of 1.18 s at 360 orientation layers. Six microMVP demonstrations illustrate the complete online planning loop on a physical robot.

</details>

---

### [[20_Research/Papers/机器人/Augmented_Reality_Interfaces_for_Human-Robot_Collaboration_Development_of_a_ROS_2-Based_Sensor_Streaming_Framework_and_Validation_via_SLAM_A|Augmented Reality Interfaces for Human-Robot Collaboration: Development of a ROS 2-Based Sensor Streaming Framework and Validation via SLAM Algorithms]]

![[assets/2609.31396_figure.jpg|800]]

- **arXiv**: [2609.31396](https://arxiv.org/abs/2609.31396)
- **PDF**: https://arxiv.org/pdf/2609.31396
- **详细分析**: [[20_Research/Papers/机器人/Augmented_Reality_Interfaces_for_Human-Robot_Collaboration_Development_of_a_ROS_2-Based_Sensor_Streaming_Framework_and_Validation_via_SLAM_A|Augmented Reality Interfaces for Human-Robot Collaboration: Development of a ROS 2-Based Sensor Streaming Framework and Validation via SLAM Algorithms]]
- **作者**: Alessandro Rubert, Stefano Ghidoni, Matteo Terreran
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 0.3，机器人 3.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Augmented Reality Interfaces for Human-Robot Collaboration: Development of a ROS 2-Based Sensor Streaming Framework and Validation via SLAM Algorithms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, Human-Robot Collaboration (HRC) has taken on a central role in Industry 4.0 and collaborative robotics, demanding communication channels that are increasingly bidirectional, intuitive, and efficient. In this context, Augmented Reality (AR) presents itself as a fundamental enabling technology, capable of both displaying information to the operator and gathering spatial data about the surrounding environment. This thesis presents the development of a sensor streaming framework that connects the Magic Leap 2 AR headset with the ROS 2 (Robot Operating System) ecosystem. Using the Unity development environment and the ROSTCP-Connector package, an on-board application for the headset was developed, capable of acquiring real-time data from the integrated sensors (pose tracking, cameras, and environmental sensors) and publishing it to dedicated ROS 2 topics. In order to test the accuracy, latency, and robustness of the generated data stream, the framework was validated using SLAM (Simultaneous Localization and Mapping) algorithms known in the literature. The experimental results demonstrate that the proposed architecture ensures stable data transmission, laying the groundwork for safe real-time interaction and shared spatial awareness, and opening up new perspectives for the control and supervision of robotic systems in complex HRC scenarios.

</details>

---

### [[20_Research/Papers/机器人/Transformer-based_Monte_Carlo_Localization_in_Construction_Meshes|Transformer-based Monte Carlo Localization in Construction Meshes]]

![[assets/2609.31357_figure.jpg|800]]

- **arXiv**: [2609.31357](https://arxiv.org/abs/2609.31357)
- **PDF**: https://arxiv.org/pdf/2609.31357
- **详细分析**: [[20_Research/Papers/机器人/Transformer-based_Monte_Carlo_Localization_in_Construction_Meshes|Transformer-based Monte Carlo Localization in Construction Meshes]]
- **作者**: Linus Kramer, William Talbot, Olga Vysotska, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Transformer-based Monte Carlo Localization in Construction Meshes》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OverlapNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To be able to perform inspection or digitization tasks, mobile robots on construction sites must be able to localize themselves reliably with respect to a global reference frame that is shared with a building map. Similar room layouts and low-texture surfaces pose a challenge for existing LiDAR- and vision-based localization methods. We approach this problem with a LiDAR-based global relocalization system that estimates the robot's pose relative to a building mesh and combines a PointNet++ encoder with a place recognition decoder, whose outputs serve as a learned observation model within a Monte Carlo Localization (MCL) framework. The pipeline is trained exclusively on synthetic LiDAR scans obtained by simulating the robot's sensors inside the building mesh. Our approach is robust in ambiguous environments due to an uncertainty-aware decoder that scales positional likelihoods and a resampling strategy that injects model hypotheses into the particle set, enabling recovery from potential particle depletion. Evaluations on real-world datasets show that our method outperforms both diffusion-based and ScanContext++ baselines while maintaining fast inference (18 ms per call), demonstrating the practicality of synthetic-data training for mesh-referenced global localization in construction robotics.

</details>

---

### [[20_Research/Papers/具身智能/Representation-Guided_Generation_and_Integration_of_Executable_Programs_for_Robot_Manipulation|Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation]]

![[assets/2609.31337_figure.png|800]]

- **arXiv**: [2609.31337](https://arxiv.org/abs/2609.31337)
- **PDF**: https://arxiv.org/pdf/2609.31337
- **详细分析**: [[20_Research/Papers/具身智能/Representation-Guided_Generation_and_Integration_of_Executable_Programs_for_Robot_Manipulation|Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation]]
- **作者**: Ruixiao Yang, Mingxin Yu, Chuchu Fan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Representation-Guided Generation and Integration of Executable Programs for Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building a robotic manipulation system requires connecting perception, planning, and control through carefully designed representations and interfaces. VLM code generation offers a way to automate this construction, but independently generated components may operate on incompatible geometric and task-level information. We present Representation-guided Integration of VLM-generated Executable Task programs (RIVET), a framework for generating complete manipulation systems around a shared object-centric representation. The representation combines per-object 6D poses, which preserve the metric information required for action grounding, with a relation graph that exposes the task-level structure required for planning. Guided by this representation, a VLM generates cooperating perception, rendering, relation-inference, and planning programs, each combining task-specific computation with available packages where useful. The resulting programs are authored once for a manipulation domain and reused on unseen start and goal configurations without code regeneration. We evaluate RIVET on cube stacking, tangram rearrangement, and three-dimensional assembly in simulation and on a physical robot, where we achieve 83% overall success rate in the real world by reusing offline-generated systems. Our results demonstrate that representation-guided program generation can adapt a common manipulation framework to tasks with different geometric, relational, and sequential requirements.

</details>

---

### [[20_Research/Papers/具身智能/See_to_Reach,_Feel_to_Grasp_Learning_A_Blind_Grasp_Reflex_for_Anthropomorphic_Robotic_Hands|See to Reach, Feel to Grasp: Learning A Blind Grasp Reflex for Anthropomorphic Robotic Hands]]

![[assets/2609.31323_figure.png|800]]

- **arXiv**: [2609.31323](https://arxiv.org/abs/2609.31323)
- **PDF**: https://arxiv.org/pdf/2609.31323
- **详细分析**: [[20_Research/Papers/具身智能/See_to_Reach,_Feel_to_Grasp_Learning_A_Blind_Grasp_Reflex_for_Anthropomorphic_Robotic_Hands|See to Reach, Feel to Grasp: Learning A Blind Grasp Reflex for Anthropomorphic Robotic Hands]]
- **作者**: Alexander Alexiev, Tzu-Yuan Lin, Sang Min Kim, Ho Jae Lee, Yonghyeon Lee, Sangbae Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.2（加权：具身智能 0.9，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《See to Reach, Feel to Grasp: Learning A Blind Grasp Reflex for Anthropomorphic Robotic Hands》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work we study if a robotic hand using proprioception alone can grasp diverse objects with no visual observation. We present a modular dexterous grasping architecture that separates global arm motion from local contact control. An independently controlled arm guides the hand toward the object, while a reinforcement learning policy grasps and stabilizes it using only hand proprioceptive feedback. We call this \textit{a blind grasp reflex}: grasping without images, object poses, or geometric observations. A learned stable-grasp score determines when the object is securely held, allowing the arm to begin post-grasp manipulation. This separation makes grasping a reusable hand-level skill that can be combined with independently designed arm controllers for various manipulation tasks. Experiments in simulation and on hardware demonstrate robust blind grasping across diverse objects and seamless composition with a range of arm controllers. Moreover, despite never observing contact geometry, the learned grasp score closely aligns with an independent physics-based measure of grasp stability. The resulting approach follows a simple principle: see to reach, feel to grasp. Project page: https://blindgraspreflex.github.io.

</details>

---

### [[20_Research/Papers/具身智能/Cybflight_An_Embedded_Rust_Autopilot_for_Aerial_Robotics_Research|Cybflight: An Embedded Rust Autopilot for Aerial Robotics Research]]

![[assets/2609.31232_figure.jpg|800]]

- **arXiv**: [2609.31232](https://arxiv.org/abs/2609.31232)
- **PDF**: https://arxiv.org/pdf/2609.31232
- **详细分析**: [[20_Research/Papers/具身智能/Cybflight_An_Embedded_Rust_Autopilot_for_Aerial_Robotics_Research|Cybflight: An Embedded Rust Autopilot for Aerial Robotics Research]]
- **作者**: Yifan Lin, Chao Qin, H S Helson Go, Hugh H. -T. Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Cybflight: An Embedded Rust Autopilot for Aerial Robotics Research》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bringing an aerial robotics method from simulation to flight should not require rebuilding a mature autopilot or adding a companion computer. Cybflight is an open-source embedded Rust research autopilot whose typed, replaceable interfaces connect hardware access, perception, state estimation, trajectory planning, and control. This modular development and compile-time optimization workflow is demonstrated with replaceable Rust implementations of model predictive contour-tracking control (MPCTC) and incremental nonlinear dynamic inversion (INDI) running on one STM32H743 without a companion computer. Using this configuration, the vehicle reaches 12.38 m/s during indoor flight, while an outdoor flight using global navigation satellite system (GNSS) position updates reaches 31.4 m/s. These flights show that running demanding estimation and nonlinear control entirely on a flight-controller microcontroller need not come at the expense of a modular autopilot structure.

</details>

---

### [[20_Research/Papers/机器人/CoralPlan_Observation_Skill_Selection_and_Execution_for_Underwater_Robotic_Inspection|CoralPlan: Observation Skill Selection and Execution for Underwater Robotic Inspection]]

![[assets/2609.31211_figure.jpg|800]]

- **arXiv**: [2609.31211](https://arxiv.org/abs/2609.31211)
- **PDF**: https://arxiv.org/pdf/2609.31211
- **详细分析**: [[20_Research/Papers/机器人/CoralPlan_Observation_Skill_Selection_and_Execution_for_Underwater_Robotic_Inspection|CoralPlan: Observation Skill Selection and Execution for Underwater Robotic Inspection]]
- **作者**: Yuer Gao, Yu Zhao, Yi Cai
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《CoralPlan: Observation Skill Selection and Execution for Underwater Robotic Inspection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OceanSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underwater robotic inspection depends on acquiring views that reveal task-relevant structure. For a structurally complex coral colony, recognising the target is only the starting point: the robot must select and execute a viewing motion suited to the inspection task. We present CoralPlan, a vision-language system that selects an observation skill from a current camera image and task text supplied by an episode manifest. A shared motion interface executes orbit, patch, or survey as target-relative trajectories; the remaining plan fields provide operator guidance. Observation completion requires target keeping and primitive-specific coverage, while joint success also requires selection to match the recorded reference. We evaluate this interface in 144 simulated episodes and 36 matched simulation-hardware pairs. In a clear-water pool with external target-reference poses, hardware observation completion reaches 77.8% and joint success reaches 63.9%. The experiments identify both reference-mismatched completions and incomplete observations after a matching skill selection. These results connect observation-skill choice to measurable underwater execution outcomes and identify where task-directed acquisition succeeds or fails.

</details>

---

### [[20_Research/Papers/机器人/Onboard_Wind-Preview_Model_Predictive_Control_Using_Pitot-Static_Sensing_for_Multirotor_UAVs|Onboard Wind-Preview Model Predictive Control Using Pitot-Static Sensing for Multirotor UAVs]]

![[assets/2609.31185_figure.jpg|800]]

- **arXiv**: [2609.31185](https://arxiv.org/abs/2609.31185)
- **PDF**: https://arxiv.org/pdf/2609.31185
- **详细分析**: [[20_Research/Papers/机器人/Onboard_Wind-Preview_Model_Predictive_Control_Using_Pitot-Static_Sensing_for_Multirotor_UAVs|Onboard Wind-Preview Model Predictive Control Using Pitot-Static Sensing for Multirotor UAVs]]
- **作者**: Bas Meere, Eline Wisse, Laurens Vousten, Sander Doodeman, Elena Torta, Paula Chanfreut, Duarte Antunes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Onboard Wind-Preview Model Predictive Control Using Pitot-Static Sensing for Multirotor UAVs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective wind gust rejection and stable hovering are critical for the outdoor operation of autonomous drones. However, existing gust rejection methods are primarily reactive, inferring the disturbance from the resulting motion or measuring it at the airframe. Either way, the wind has already begun to act before it can be compensated. In this work, we anticipate the gust instead by measuring the wind ahead of the drone with a low-cost, low-weight pitot-static sensor mounted on a boom. The resulting wind preview is incorporated into a nonlinear model predictive controller (MPC), which optimizes the drone motion while anticipating wind disturbances. A longer boom offers more preview time but adds inertia and degrades flight performance. We characterize this trade-off in simulation and show that the optimal preview distance is not a fixed property of the platform, but shifts with the wind speed and with how quickly the drone can respond. Indoor hardware experiments confirm the trend and show that the proposed controller substantially improves hover performance against a PX4 baseline and an otherwise identical wind-unaware MPC. Outdoor experiments show that the error along the wind direction is reduced by 54 percent with respect to the baseline, demonstrating that a single wind-aligned sensor can significantly improve hovering performance.

</details>

---

### [[20_Research/Papers/具身智能/DualManip_Agentic_Dynamic_Manipulation_via_Dual-Path_Semantic_Reasoning_and_Geometric_Adaptation|DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation]]

![[assets/2609.31112_figure.png|800]]

- **arXiv**: [2609.31112](https://arxiv.org/abs/2609.31112)
- **PDF**: https://arxiv.org/pdf/2609.31112
- **详细分析**: [[20_Research/Papers/具身智能/DualManip_Agentic_Dynamic_Manipulation_via_Dual-Path_Semantic_Reasoning_and_Geometric_Adaptation|DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation]]
- **作者**: Chengxi Li, Yan Di, Yingyue Li, Ruida Zhang, Mingyang Li, Xiangyang Ji
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《DualManip: Agentic Dynamic Manipulation via Dual-Path Semantic Reasoning and Geometric Adaptation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) enable open-vocabulary reasoning for robot manipulation, but their high inference latency limits responsiveness in dynamic scenes. Many scene changes, however, alter object geometry without invalidating task intent. We present DualManip, a dual-path framework that decouples infrequent semantic reasoning from responsive geometric adaptation. The semantic path decomposes the task and grounds task-relevant interactions, followed by a constraint-solving module for pose optimization. During execution, the geometric path continuously updates template-to-observation correspondences from live RGB-D observations via a shape-adaptive network. These correspondences transfer task-relevant grasp contacts across observations, enabling online grasp reconstruction under object motion and non-rigid deformation. The Information Interaction Module bridges the two paths by initializing task-relevant grasps from semantic grounding, validating geometric updates, and triggering semantic replanning upon update failures. Real-world evaluation spans six manipulation tasks covering non-rigid deformation, articulated reconfiguration, rigid motion, and high-precision assembly across three settings: static, single-change, and continuous dynamic. DualManip demonstrates superior manipulation robustness, particularly under continuous scene changes, while achieving geometric adaptation approximately 46$\times$ faster than agentic verification and semantic replanning. Our project page: https://lichengxi1.github.io/Dualmanip.

</details>

---

### [[20_Research/Papers/具身智能/Kintsugi-VLA_Turning_Failed_Robot_Rollouts_into_Recovery_Data_through_Interventional_Recoverability|Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability]]

![[assets/2609.31048_figure.png|800]]

- **arXiv**: [2609.31048](https://arxiv.org/abs/2609.31048)
- **PDF**: https://arxiv.org/pdf/2609.31048
- **详细分析**: [[20_Research/Papers/具身智能/Kintsugi-VLA_Turning_Failed_Robot_Rollouts_into_Recovery_Data_through_Interventional_Recoverability|Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability]]
- **作者**: Ivan Snegirev, Elizaveta Semenyakina, Dmitrii Maliukov, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Kintsugi-VLA: Turning Failed Robot Rollouts into Recovery Data through Interventional Recoverability》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Kintsugi-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation enables scalable training of Vision-Language-Action policies by using privileged experts to generate visual demonstrations without requiring every trajectory to be collected through manual teleoperation. However, such pipelines typically retain successful demonstrations while failed rollouts are discarded, even though they expose precisely the off-nominal states from which recovery must be learned. We introduce Kintsugi-VLA, a framework for converting failed rollouts into targeted synthetic recovery data by exploiting exact state restoration and branching in simulation. For a fixed privileged expert, we define interventional recoverability as the probability of completing the original task after the simulator is restored to a given state, estimate it using adaptive Monte Carlo continuations with pointwise Wilson intervals, and characterize its non-monotonic evolution along failed trajectories. These estimates identify an observed terminal low-recoverability frontier-the point after which measured recoverability remains below a threshold-which is then used to select informative recovery starting states. In a simulated Franka manipulation task, targeted recovery data yield aggregate SmolVLA recovery success of 34.6\% and 38.4\% under difficulty- and frame-budget matching, respectively, 5.8 and 6.7 percentage points above uniform sampling within the same recovery window. The same ordering is observed under disturbed end-to-end execution and shifted clutter and physics conditions, while clean-task success decreases from 76.8\% to 74.7\%. Kintsugi-VLA demonstrates how failed simulator rollouts can be transformed from discarded experience into structured recovery-training data through direct interventional measurement.

</details>

---

### [[20_Research/Papers/机器人/Compact_Force_Sensor_for_Dual-UAV_Cable-Suspended_Payload_Transport_with_Tension-Aware_Outer-Loop_Control|Compact Force Sensor for Dual-UAV Cable-Suspended Payload Transport with Tension-Aware Outer-Loop Control]]

![[assets/2609.31035_figure.jpg|800]]

- **arXiv**: [2609.31035](https://arxiv.org/abs/2609.31035)
- **PDF**: https://arxiv.org/pdf/2609.31035
- **详细分析**: [[20_Research/Papers/机器人/Compact_Force_Sensor_for_Dual-UAV_Cable-Suspended_Payload_Transport_with_Tension-Aware_Outer-Loop_Control|Compact Force Sensor for Dual-UAV Cable-Suspended Payload Transport with Tension-Aware Outer-Loop Control]]
- **作者**: Andrea Delbene, Giorgio Cannata, Giorgio Carlini, Filippo Sante, Marco Baglietto
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Compact Force Sensor for Dual-UAV Cable-Suspended Payload Transport with Tension-Aware Outer-Loop Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative payload transportation using multiple \textit{Unmanned Aerial Vehicles} (UAVs) poses challenges in stability, coordination, and robustness, especially under external disturbances and unmodeled dynamics. This work proposes a dual-UAV payload transportation framework supported by a compact, custom-designed force sensor measuring the interaction force at the UAV cable anchor point. The sensor design and mathematical model are presented, and its performance is characterized through static and dynamic tests evaluating linearity, hysteresis, repeatability, and crossload. The control architecture follows a cascade structure: fast inner loops handle vehicle stabilization, while outer loops are designed to compensate for the measured forces. The approach is validated through simulations and indoor experiments under position uncertainty. Payload-drop and constrained-space tests assess the proposed sensing and control architecture against literature-based distributed references, showing improved stabilization, coordination, and disturbance rejection. A video of the experiments is available at: https://youtu.be/rIw9-fvV8Qw.

</details>

---

### [[20_Research/Papers/具身智能/Co-design_of_trajectory_and_morphology_for_a_vertical_jump-climbing_robot|Co-design of trajectory and morphology for a vertical jump-climbing robot]]

![[assets/2609.31014_figure.jpg|800]]

- **arXiv**: [2609.31014](https://arxiv.org/abs/2609.31014)
- **PDF**: https://arxiv.org/pdf/2609.31014
- **详细分析**: [[20_Research/Papers/具身智能/Co-design_of_trajectory_and_morphology_for_a_vertical_jump-climbing_robot|Co-design of trajectory and morphology for a vertical jump-climbing robot]]
- **作者**: Christopher Y. Xu, Elliot W. Hawkes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Co-design of trajectory and morphology for a vertical jump-climbing robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Animals such as squirrels and even bears have adapted to rapidly climb up trees and other complex vertical terrain, but achieving comparable agility has been a challenge for climbing robots. Existing robots often use walking gaits and move conservatively to stay in contact with the surface, which limits the range of dynamic maneuvers. In this paper we present a 290 g robot that, to our knowledge, is the first to climb vertically by bounding (with an aerial phase). We leverage a co-design workflow, in which the morphology and trajectory are jointly optimized for fast locomotion, subject to adhesion force limitations seen in spined grippers. The resulting trajectory includes a rapid maneuver that launches the robot vertically, and an aerial reorientation that brings the front grippers back to the surface using the rear leg as an inertial tail. We evaluate the resulting jump forces in 2D force space and demonstrate that the optimized morphology is capable of continuous climbing at a speed of 0.375 m/s (1.97 body lengths/s), and can also achieve ground locomotion and transition to a vertical surface. Our work proposes design insights for the jump-climbing maneuver and serves as an important step toward creating climbing robots with agility on par with that of animals.

</details>

---

### [[20_Research/Papers/具身智能/Quadruped_Obstacle_Avoidance_and_Footstep_Planning_with_Distributed_Low-cost_Time-of-Flight_Sensors|Quadruped Obstacle Avoidance and Footstep Planning with Distributed Low-cost Time-of-Flight Sensors]]

![[assets/2609.31008_figure.jpg|800]]

- **arXiv**: [2609.31008](https://arxiv.org/abs/2609.31008)
- **PDF**: https://arxiv.org/pdf/2609.31008
- **详细分析**: [[20_Research/Papers/具身智能/Quadruped_Obstacle_Avoidance_and_Footstep_Planning_with_Distributed_Low-cost_Time-of-Flight_Sensors|Quadruped Obstacle Avoidance and Footstep Planning with Distributed Low-cost Time-of-Flight Sensors]]
- **作者**: Giammarco Caroleo, Timothée Mahamoodally, Matteo Manzardo, Jin Jin, Marco Pontin, Matias Mattamala, Renato Vidoni, Perla Maiolino, Maurice Fallon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Quadruped Obstacle Avoidance and Footstep Planning with Distributed Low-cost Time-of-Flight Sensors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots typically rely on depth cameras and LiDAR sensors to map their local environment. However, these sensors have limited close-range coverage, are relatively expensive, and consume significant power. This study investigates whether distributed Time-of-Flight (ToF) sensors can serve as a low-cost alternative to depth cameras for near-field terrain mapping for locomotion and local navigation. We designed a distributed ToF sensing architecture for the ANYbotics ANYmal quadruped, assessed its environment reconstruction accuracy, and benchmarked it against depth cameras for terrain mapping and obstacle avoidance. Distributing these sensors around the robot can also avoid the blind spots of traditional sensors. Our results show that, despite their low resolution and higher measurement noise, distributed ToF sensors can support reliable perceptual locomotion with centimeter-level local mapping accuracy. The proposed sensing strategy provides sufficient geometric information for near-field obstacle avoidance and footstep planning, at substantially lower cost, energy consumption, and system complexity than depth cameras.

</details>

---

### [[20_Research/Papers/具身智能/TACTIC_Understanding_Tactile_Encoders_and_Conditioning_for_Contact-rich_Robot_Manipulation_Policies|TACTIC: Understanding Tactile Encoders and Conditioning for Contact-rich Robot Manipulation Policies]]

![[assets/2609.30969_figure.png|800]]

- **arXiv**: [2609.30969](https://arxiv.org/abs/2609.30969)
- **PDF**: https://arxiv.org/pdf/2609.30969
- **详细分析**: [[20_Research/Papers/具身智能/TACTIC_Understanding_Tactile_Encoders_and_Conditioning_for_Contact-rich_Robot_Manipulation_Policies|TACTIC: Understanding Tactile Encoders and Conditioning for Contact-rich Robot Manipulation Policies]]
- **作者**: Seongjin Bien, Débora Oliveira Makowski, Carlo Kneissl, Reihaneh Mirjalili, Pankhuri Vanjani, Rudolf Lioutikov, Gitta Kutyniok, Florian Walter, Wolfram Burgard
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《TACTIC: Understanding Tactile Encoders and Conditioning for Contact-rich Robot Manipulation Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet, SARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile information is essential for contact-rich manipulation tasks in robotics. Vision-based tactile sensors make it particularly easy to design end-to-end manipulation policies with tactile sensing, as they enable the use of existing encoders from computer vision. However, this has led to a huge variety of architectures, training datasets, and evaluation protocols, making it difficult to determine which design choices best encode touch. In this work, we address this gap and present a comprehensive study of tactile encoders and fusion strategies across various contact-rich manipulation tasks in real-world experiments. To enable a controlled comparison, we train and evaluate all models under the same pipeline and experimental setup, comprising more than 2000 real-world rollouts. Our results go beyond other studies that only compare simulation performance, which does not necessarily translate to real-world settings, where large-scale evaluations are needed to obtain reliable statistics. Our key finding is that there is no universally optimal representation or fusion strategy for encoding visual-tactile. Instead, the best encoder backbone and fusion scheme depend strongly on the task.

</details>

---

### [[20_Research/Papers/具身智能/FRAM_Trajectory-Guided_Visual_Feature_Selection_for_Compact_Language-Conditioned_Robot_Manipulation|FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation]]

![[assets/2609.30965_figure.png|800]]

- **arXiv**: [2609.30965](https://arxiv.org/abs/2609.30965)
- **PDF**: https://arxiv.org/pdf/2609.30965
- **详细分析**: [[20_Research/Papers/具身智能/FRAM_Trajectory-Guided_Visual_Feature_Selection_for_Compact_Language-Conditioned_Robot_Manipulation|FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation]]
- **作者**: Hiroshi Ito, Hyogo Hiruma, Yoshiki Kanai, Takahiro Yoshida, Akira Kanazawa, Hiroki Yamada
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《FRAM: Trajectory-Guided Visual Feature Selection for Compact Language-Conditioned Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, ImageNet, OpenVLA, RIPT-VLA, ResNet, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models achieve strong performance in robot manipulation, but often require large numbers of parameters. In this work, we propose the Future Representation Action Model (FRAM), a small policy that explicitly links the future end-effector trajectory to the current visual input. FRAM uses the image coordinates of the predicted trajectory as spatial pointers and reads local visual features related to the motion from the current image. This organizes the information for action generation into the reference position (Where), the visual state (What), and the future motion (Future). Trajectory labels are generated automatically from demonstrations and camera geometry, so no manual annotation is needed. With 138.7M parameters, including a frozen language encoder, FRAM reaches an average success rate of 92.2% over the four standard LIBERO suites, close to the 94.2% of $π_0$ with 3.3B parameters. Without extra training, it also reaches an average of 67.3% on LIBERO-Plus. Ablations confirm that both the future trajectory and the local visual features improve performance and robustness. On a real dual-arm UR5e, FRAM stacks cups using only wrist cameras, including choosing and switching between the left and right arms. These results show that selecting visual information based on future motion is an effective way to obtain both high performance and robustness in a small robot policy.

</details>

---

### [[20_Research/Papers/大模型/VisTacAlign_Co-Training_Dexterous_Policies_on_Tactile_Human_and_Robot_Demonstrations|VisTacAlign: Co-Training Dexterous Policies on Tactile Human and Robot Demonstrations]]

![[assets/2609.30959_figure.png|800]]

- **arXiv**: [2609.30959](https://arxiv.org/abs/2609.30959)
- **PDF**: https://arxiv.org/pdf/2609.30959
- **详细分析**: [[20_Research/Papers/大模型/VisTacAlign_Co-Training_Dexterous_Policies_on_Tactile_Human_and_Robot_Demonstrations|VisTacAlign: Co-Training Dexterous Policies on Tactile Human and Robot Demonstrations]]
- **作者**: Julien Poffet, Matthew Strong, Ankush Dhawan, Baiyu Shi, Shalika Neelaveni, Yujia Yuan, Zhenan Bao, Monroe Kennedy
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《VisTacAlign: Co-Training Dexterous Policies on Tactile Human and Robot Demonstrations》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human demonstrations are a cheap source of data for dexterous manipulation, but co-training a robot policy on them requires closing the human--robot gap in every modality the policy consumes. We present VisTacAlign, a framework for co-training 3D-visual-tactile dexterous policies on human and robot demonstrations. Glove-tracked human hand motion is retargeted to a 17-DoF tactile robot hand with a one-time fingertip correction. The human hand is then erased from both stereo views and replaced by a posed robot-hand mesh painted with pixels from robot recordings, and a real-time stereo foundation model is re-run on the composite, so the human point clouds carry the same stereo errors and visibility as the robot ones. Finally, a capacitive tactile glove is aligned to the robot's fingertip sensors in its signal space, giving one interpretable per-finger force representation. A diffusion transformer consumes point-cloud, proprioceptive, and per-finger tactile tokens. On three real-world tasks requiring precise force -- Lego assembly, plucking strawberries of varying size, and activating and lifting a power drill -- adding aligned human demonstrations to existing robot data improves over robot-only policies, and ablations show that both tactile input and visual alignment are necessary. Project page: https://vis-tac-align.github.io

</details>

---

### [[20_Research/Papers/强化学习/Bundled_Contact_Gradients_Stabilizing_Differentiable_Simulation_for_Deployable_Dynamic_Tasks|Bundled Contact Gradients: Stabilizing Differentiable Simulation for Deployable Dynamic Tasks]]

![[assets/2609.30951_figure.png|800]]

- **arXiv**: [2609.30951](https://arxiv.org/abs/2609.30951)
- **PDF**: https://arxiv.org/pdf/2609.30951
- **详细分析**: [[20_Research/Papers/强化学习/Bundled_Contact_Gradients_Stabilizing_Differentiable_Simulation_for_Deployable_Dynamic_Tasks|Bundled Contact Gradients: Stabilizing Differentiable Simulation for Deployable Dynamic Tasks]]
- **作者**: Dyuman Aditya, Jin Cheng, Clemens Schwarke, Quan Nguyen, Gaurav Sukhatme, Stelian Coros, Gabriele Fadini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Bundled Contact Gradients: Stabilizing Differentiable Simulation for Deployable Dynamic Tasks》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Differentiable simulation provides analytic gradients of robot dynamics, enabling fast and sample-efficient first-order policy optimization. However, obtaining smooth and informative gradients through rigid-body contact typically requires softened contact models, often at the expense of physical fidelity and thereby limiting learned policies largely to simulation. This trade-off becomes particularly consequential for dynamic humanoid motions, where accurate contact dynamics are critical for transferring policies to the real world. Increasing contact stiffness in rigid-body simulation improves the fidelity of interactions, but also makes the dynamics increasingly sensitive to small state perturbations, producing high-variance gradients that can destabilize first-order policy learning. To address this, we propose \emph{Bundled Contact Gradients (BCG)}, a contact-local randomized smoothing framework for differentiable policy learning. When stiff contact is detected, our method evaluates a local bundle of randomized perturbation rollouts around the stiff contact configuration and aggregates their gradient signal thereby reducing gradient variance. We demonstrate the effectiveness of our method by successfully training and transferring dynamic motions zero-shot onto a real-world Unitree G1 humanoid platform. Videos and supplementary information can be found at https://bundledcontactgradients.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Causeway_Restoring_Task_Accessibility_for_Instruction_Switching_in_VLA_Policies|Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies]]

![[assets/2609.30913_figure.png|800]]

- **arXiv**: [2609.30913](https://arxiv.org/abs/2609.30913)
- **PDF**: https://arxiv.org/pdf/2609.30913
- **详细分析**: [[20_Research/Papers/具身智能/Causeway_Restoring_Task_Accessibility_for_Instruction_Switching_in_VLA_Policies|Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies]]
- **作者**: Qingzi Wang, Kaixi Feng, Guangyao Shi, Xiyang Wu, Ang Li, Dinesh Manocha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Causeway: Restoring Task Accessibility for Instruction Switching in VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, SwitchVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies can execute many tasks from standard initial states, yet a new instruction may fail after another task has altered the robot's physical state. We study instruction switching, where a new task is issued during or after the execution of a different one. We observe that a target task that is reliably completed from its standard initial states can become inaccessible from states produced by a preceding task. We call such states task islands. We propose Causeway, a training-free inference-time intervention. Given the current state and a re-entry pose for the target task, Causeway back-propagates through the frozen decoding computation and applies a state-directed write within the action-stream representation. The VLA decodes the return motion itself, without parameter updates, a new action head, or external action generation. Across 71 cross-object pairs, three switch timings, and three VLA architectures on LIBERO-Goal, Causeway raises bare-switch success from 3-26% to 47-65% and increases the rate of reaching the handoff neighborhood by 42-72 percentage points across models. Additional experiments on LIBERO-Object and a real xArm platform show that the recovery extends beyond the main LIBERO-Goal setting, both in simulation and on a robot.

</details>

---

### [[20_Research/Papers/大模型/PHASE_Compliance-Enabled_Tactile_Phase_Retrieval_for_Few-Shot_Insertion_Learning|PHASE: Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning]]

![[assets/2609.30889_figure.png|800]]

- **arXiv**: [2609.30889](https://arxiv.org/abs/2609.30889)
- **PDF**: https://arxiv.org/pdf/2609.30889
- **详细分析**: [[20_Research/Papers/大模型/PHASE_Compliance-Enabled_Tactile_Phase_Retrieval_for_Few-Shot_Insertion_Learning|PHASE: Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning]]
- **作者**: Jeremy Siburian, Cristian C. Beltran-Hernandez, Tatsuya Matsushima, Yusuke Iwasawa, Masashi Hamaya, Mai Nishimura
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PHASE: Compliance-Enabled Tactile Phase Retrieval for Few-Shot Insertion Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich assembly tasks such as peg-in-hole insertion remain difficult to learn from limited demonstrations. While retrieval-augmented imitation learning, which augments target demonstrations with relevant prior data, offers a promising direction, its applicability to contact-rich manipulation remains largely unexplored. Contact-rich insertion unfolds over multiple phases from search to insert, and retrieving phase-specific experience from prior data in principled ways remains an open question. Our key insight is that a compliant wrist enables the robot to sustain contact throughout execution, producing rich tactile and force signals that naturally reveal the phase structure of insertion and inform what should be retrieved. Based on this insight, we present PHASE (PHase-Aware Segmentation and REtrieval), a framework for compliance-enabled tactile phase retrieval that integrates multimodal contact-aware representation learning, variable-length phase segmentation from tactile signals, and phase-consistent retrieval for policy learning. We evaluate PHASE on real-world peg-in-hole insertion across five peg geometries, comparing against retrieval strategies drawn from state-of-the-art methods under a shared policy architecture. PHASE improves the overall success rate by 13 percentage points over the strongest non-phase-aware baseline, and improves performance under unseen initial positions by 30 percentage points. These results demonstrate that aligning retrieval with interaction-defined contact phases substantially improves robustness in few-shot insertion learning.

</details>

---

### [[20_Research/Papers/具身智能/VLaRL_Augmenting_Vision-Language-Action_Models_with_Simulation-Trained_Latent-Conditioned_Residual_RL|VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL]]

![[assets/2609.30868_figure.png|800]]

- **arXiv**: [2609.30868](https://arxiv.org/abs/2609.30868)
- **PDF**: https://arxiv.org/pdf/2609.30868
- **详细分析**: [[20_Research/Papers/具身智能/VLaRL_Augmenting_Vision-Language-Action_Models_with_Simulation-Trained_Latent-Conditioned_Residual_RL|VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL]]
- **作者**: Namiko Saito, Kinam Kim, Heecheol Kim, Katsushi Ikeuchi, Yasuyuki Matsushita
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 2.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VLaRL: Augmenting Vision-Language-Action Models with Simulation-Trained Latent-Conditioned Residual RL》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, VLaRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models provide broad, instruction-conditioned manipulation behaviors, but their physical execution can remain imprecise during contact-rich interaction. Residual reinforcement learning (RL) can correct such errors while keeping the VLA frozen, but real-robot RL is costly and safety-critical. We propose VLA Latent-Conditioned RL (VLaRL), which enables residual RL for frozen VLAs to be trained in simulation and deployed on real robots without real-world RL or online adaptation. The key challenge is transferring the learned residual policy despite the visual gap between simulation and reality. Rather than requiring pixel-level visual correspondence, VLaRL uses the VLA's internal vision-language latent representation to condition residual control and as the sim-to-real transfer interface, and learns a lightweight mapper that transforms simulation-derived latents toward the real latent distribution. Across four contact-rich manipulation tasks and two VLA backbones, VLaRL improves real-world success in all task-backbone combinations, while controlled ablations demonstrate the importance of both latent conditioning and latent alignment for transferring simulation-trained residual control.

</details>

---

### [[20_Research/Papers/具身智能/Impedance_Cloning_Learning_Equilibrium_Point_Parameters_for_Contact-Rich_Manipulation|Impedance Cloning: Learning Equilibrium Point Parameters for Contact-Rich Manipulation]]

![[assets/2609.30842_figure.png|800]]

- **arXiv**: [2609.30842](https://arxiv.org/abs/2609.30842)
- **PDF**: https://arxiv.org/pdf/2609.30842
- **详细分析**: [[20_Research/Papers/具身智能/Impedance_Cloning_Learning_Equilibrium_Point_Parameters_for_Contact-Rich_Manipulation|Impedance Cloning: Learning Equilibrium Point Parameters for Contact-Rich Manipulation]]
- **作者**: Hayato Takahashi, Ryoga Oishi, Yuki Kasuga, Toshiaki Tsuji
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Impedance Cloning: Learning Equilibrium Point Parameters for Contact-Rich Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation requires robots to regulate force against surfaces whose geometry deviates unpredictably from training conditions. Trajectory-based imitation learning, which reproduces observable outputs, breaks down under such shifts. We propose Impedance Cloning, which instead imitates the biomechanical priors that generate motion -- the stiffness and equilibrium point -- and thereby passively absorbs contact uncertainty. Because these parameters encode intent rather than outcome, they generalize across surface geometries where trajectory reproduction does not. We extract them from bilateral teleoperation demonstrations via a particle filter without force/torque sensors and evaluate the framework on two CRANE-X7 manipulators. In a wiping task with joint-space actions, the trajectory-based baseline loses contact below -6 cm, whereas the proposed method maintains a consistent 4-5 N contact force above -6 cm, with a gradual decrease below; with Cartesian-space actions, its force-height slope over 0 to +8 cm is 0.13 +/- 0.03 N/cm, versus 0.34-0.83 N/cm for fixed-impedance baselines. In a pick-and-place task with 10 diverse cups (100 trials), the proposed method succeeds in 84 trials, outperforming the fixed-impedance baseline (74/100) and performing comparably to a variable impedance control baseline (82/100) with one demonstration instead of ten. In a grasping task, the representation reduces torque tracking error with both ILBiT and Mamba backbones, confirming its generality across architectures.

</details>

---

### [[20_Research/Papers/具身智能/Fast_Plans,_Faithful_Actions_Closing_the_Planning-Execution_Gap_in_Hierarchical_Vision-Language-Action_Models|Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models]]

![[assets/2609.30833_figure.png|800]]

- **arXiv**: [2609.30833](https://arxiv.org/abs/2609.30833)
- **PDF**: https://arxiv.org/pdf/2609.30833
- **详细分析**: [[20_Research/Papers/具身智能/Fast_Plans,_Faithful_Actions_Closing_the_Planning-Execution_Gap_in_Hierarchical_Vision-Language-Action_Models|Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models]]
- **作者**: Chuanliang Xie, Boyu Ma, Gen Li, Yizhou Liu, Houwang Chen, Xinyu Zhou, Jianfei Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Fast Plans, Faithful Actions: Closing the Planning-Execution Gap in Hierarchical Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FiS-VLA, NoTVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical vision-language-action (VLA) systems consist of a high-level vision-language planner and a low-level action expert that generates continuous actions. This hierarchical design has practical value only if the planner can generate plans fast enough to meet real-time control requirements, and the resulting plans actually contribute to the generation of action. We study one such system, a waypoint hierarchy pipeline adapted from $π_{0.5}$, and find that neither requirement is satisfied. This baseline relies on token-level autoregressive decoding (Token-AR) to generate a waypoint plan, requiring 57 very expensive vision-language model (VLM) forward passes. However, we find that erasing the waypoint endpoints has little effect on task success. Two findings reveal the misalignment of planner-executor: the planner generates outputs at an excessively fine granularity, and the executor underuses plans as a control condition. We address the latency issue with waypoint-aligned block-autoregressive decoding (Block-AR), and plan underuse issue with normalized goal modulation (NGM), a layer-wise goal path constrained by phase gating and anti-shortcut training so that the waypoint influences action generation maintaining other signals. Our method reduces the maximum number of VLM forward passes from 57 to 8 on LIBERO, including one prefix prefill, and achieves an $8.7\times$ reduction in planning latency on a Rokae dual-arm robot. With normalized goal modulation and anti-shortcut training, Block-AR's success rate on LIBERO-Long increases from 91.0% to 96.2%, while its average success rate across the four suites increases from 95.85% to 98.45%. On three bimanual tasks with this robot, success rates remain comparable across methods.

</details>

---

### [[20_Research/Papers/机器人/HIRE_History-Conditioned_Interaction_Reasoning_and_High-Rate_Execution_for_Visually_Aliased_Precision_Manipulation|HIRE: History-Conditioned Interaction Reasoning and High-Rate Execution for Visually Aliased Precision Manipulation]]

![[assets/2609.30828_figure.png|800]]

- **arXiv**: [2609.30828](https://arxiv.org/abs/2609.30828)
- **PDF**: https://arxiv.org/pdf/2609.30828
- **详细分析**: [[20_Research/Papers/机器人/HIRE_History-Conditioned_Interaction_Reasoning_and_High-Rate_Execution_for_Visually_Aliased_Precision_Manipulation|HIRE: History-Conditioned Interaction Reasoning and High-Rate Execution for Visually Aliased Precision Manipulation]]
- **作者**: Rongji Li, Wenhao He, Cewu Lu, Xingyu Chen, Xu-Yao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《HIRE: History-Conditioned Interaction Reasoning and High-Rate Execution for Visually Aliased Precision Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precision manipulation with contact-critical interactions is often history-dependent: visually similar observations can correspond to different latent interaction states and therefore require different actions, while small execution errors can alter task outcomes. Policies relying on the current visual observation alone cannot resolve such ambiguity; force-aware and memory-augmented methods enrich physical or temporal context, while reactive high-rate policies improve local contact response, yet long-horizon temporal reasoning and precision execution remain largely decoupled in existing methods, limiting reliable progression in visually aliased precision manipulation. To bridge this gap, we introduce History-Conditioned Interaction Reasoning and Execution (HIRE), a cross-rate framework comprising a history-conditioned Interaction-State Reasoner (ISR) and a high-rate Interaction-Manifold Executor (IME). ISR encodes ordered wrench history with a temporal wrench encoder and Force Perceiver as persistent physical evidence for state-consistent action generation, while IME structures contact-critical motion into intrinsic progress and transverse correction for precise execution; their cross-rate loop allows the resulting physical traces to inform subsequent reasoning. In real-robot experiments across surface, insertion, and rotational interactions, HIRE achieves at least 90% completion across all evaluated task stages while improving interaction-state disambiguation, execution precision, and generalization. More broadly, HIRE provides a unified reasoning--execution perspective on precision manipulation under history-dependent partial observability, where physical interaction both realizes task intent and reveals latent-state evidence for future decisions. Code will be released upon publication.

</details>

---

### [[20_Research/Papers/具身智能/Design_and_Characterization_of_a_Variable-Length_Continuum_Mechanism_with_Force_Locking|Design and Characterization of a Variable-Length Continuum Mechanism with Force Locking]]

![[assets/2609.30759_figure.png|800]]

- **arXiv**: [2609.30759](https://arxiv.org/abs/2609.30759)
- **PDF**: https://arxiv.org/pdf/2609.30759
- **详细分析**: [[20_Research/Papers/具身智能/Design_and_Characterization_of_a_Variable-Length_Continuum_Mechanism_with_Force_Locking|Design and Characterization of a Variable-Length Continuum Mechanism with Force Locking]]
- **作者**: Katelyn King, Veronica Fish, Allison M. Okamura
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Design and Characterization of a Variable-Length Continuum Mechanism with Force Locking》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The utility of flexible continuum mechanisms for dexterous navigation is often impaired by their low stiffness, making them ineffective at manipulation in high-force scenarios. To address this challenge, we propose a novel continuum mechanism that achieves both flexible and rigid behavior by antagonistic extension and contraction of a rod-driven continuum helical structure. The helical design combines variable-length capacity with force locking for workspace and stiffness enhancement. In this article, we present the detailed design of the proposed mechanism and characterize its performance through experiments that quantify bending and stiffness. The results demonstrate 180 degree bending range of motion with an average distal positioning error of &lt;10%. Further tests demonstrate that force locking directly improves axial stiffness and thus indirectly increases bending stiffness anisotropically, with maximum bending stiffness along load paths with a large axial component. Tensioning the driving rods provides additional stiffness tunability in the force-locked state, where increasing rod tension proportionally increases bending stiffness with a dimensionless gain of 0.56.

</details>

---

### [[20_Research/Papers/具身智能/Praxis_Distilling_Physical_Interaction_Priors_from_Egocentric_Videos_for_Generalizable_Whole-Body_Manipulation|Praxis: Distilling Physical Interaction Priors from Egocentric Videos for Generalizable Whole-Body Manipulation]]

![[assets/2609.30735_figure.png|800]]

- **arXiv**: [2609.30735](https://arxiv.org/abs/2609.30735)
- **PDF**: https://arxiv.org/pdf/2609.30735
- **详细分析**: [[20_Research/Papers/具身智能/Praxis_Distilling_Physical_Interaction_Priors_from_Egocentric_Videos_for_Generalizable_Whole-Body_Manipulation|Praxis: Distilling Physical Interaction Priors from Egocentric Videos for Generalizable Whole-Body Manipulation]]
- **作者**: Shuliang He, Ruiyan Xu, Bo Yue, Hengming Zhang, Huayi Zhou, Shuai Wang, Wei-Shi Zheng, Guiliang Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Praxis: Distilling Physical Interaction Priors from Egocentric Videos for Generalizable Whole-Body Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile humanoid manipulation requires both reaching a usable workspace and preserving precise hand-object interactions as object poses and contact conditions change. Learning these behaviors from limited task-specific data remains challenging. To bridge this gap, we introduce Praxis, a whole-body manipulation framework that combines physical interaction priors from one-shot egocentric video demonstrations with closed-loop posture calibration and online perception. The framework coordinates three stages: vision-language-guided navigation toward target objects, closed-loop posture calibration to align the arm-hand workspace, and dexterous manipulation with synchronized upper- and lower-body control. Online visual feedback re-grounds demonstrated interaction geometry under new object poses and scene configurations, while tactile feedback adapts hand motions to actual contact conditions. Each manipulation skill is specified by one human demonstration, without task-specific manipulation-policy retraining. Experiments across five long-horizon manipulation tasks demonstrate spatial, visual, and cross-object generalization, as well as recovery from external physical disturbances across all three stages.

</details>

---

### [[20_Research/Papers/强化学习/RoboMonitor_Label-Efficient_Runtime_Monitoring_of_Robot_Task_Execution_via_Predictive_Representation_Learning|RoboMonitor: Label-Efficient Runtime Monitoring of Robot Task Execution via Predictive Representation Learning]]

![[assets/2609.30715_figure.png|800]]

- **arXiv**: [2609.30715](https://arxiv.org/abs/2609.30715)
- **PDF**: https://arxiv.org/pdf/2609.30715
- **详细分析**: [[20_Research/Papers/强化学习/RoboMonitor_Label-Efficient_Runtime_Monitoring_of_Robot_Task_Execution_via_Predictive_Representation_Learning|RoboMonitor: Label-Efficient Runtime Monitoring of Robot Task Execution via Predictive Representation Learning]]
- **作者**: Abhiroop Ajith, Gokul Narayanan, Kyle Coelho, Tingji Zhao, Yash Shahapurkar, Brian Zhu, Melih Erdogan, Ted Krubasik, Constantinos Chamzas, Eugen Solowjow
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《RoboMonitor: Label-Efficient Runtime Monitoring of Robot Task Execution via Predictive Representation Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned robot policies produce actions, but their outputs alone do not establish whether execution is progressing as intended. Robot execution monitoring requires identifying the current execution phase, detecting failures, and recognizing task completion from observations available during execution. Training such monitors requires annotations that are scarce in datasets collected for robot-policy learning. We present RoboMonitor, a label-efficient vision--language execution monitor that learns from these datasets before introducing monitoring supervision. We pre-train on 25 hours of multi-camera trajectories spanning 12 manipulation tasks and two robot embodiments, using action-conditioned future-feature prediction, inverse dynamics, and masked-present prediction. We then transfer the learned visual and context encoders to a causal monitor and apply temporal supervised fine-tuning (Temporal SFT), which combines supervision throughout each observation window with consistency objectives within and across overlapping windows. At deployment, RoboMonitor requires only the task instruction and camera observations. On a four-task monitoring benchmark, RoboMonitor trained with 52 labeled episodes achieves 93.1% mean phase accuracy and 85.9% macro recall over two fine-tuning seeds, exceeding Qwen3-VL and Robometer trained with the same monitoring supervision. Its phase accuracy also exceeds that of both Qwen3-VL and Robometer trained with 100 episodes. A Qwen3-VL ablation shows that Temporal SFT reduces mean spurious phase switching from 15.23% to 4.95%. In closed-loop deployment, the integrated system completes 39 of 40 simulated Toolbox Sorting trials and 35 of 40 real-world Reel Packing trials, with no false recovery triggers observed.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Vision-Based_Agile_Gap_Traversal_Differentiable_Simulation_with_a_Warm-Started_Critic|Learning Vision-Based Agile Gap Traversal: Differentiable Simulation with a Warm-Started Critic]]

![[assets/2609.30696_figure.png|800]]

- **arXiv**: [2609.30696](https://arxiv.org/abs/2609.30696)
- **PDF**: https://arxiv.org/pdf/2609.30696
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Vision-Based_Agile_Gap_Traversal_Differentiable_Simulation_with_a_Warm-Started_Critic|Learning Vision-Based Agile Gap Traversal: Differentiable Simulation with a Warm-Started Critic]]
- **作者**: Nuthasith Gerdpratoom, Tianchen Sun, Yichao Gao, Lin Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Learning Vision-Based Agile Gap Traversal: Differentiable Simulation with a Warm-Started Critic》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traversing narrow gaps is challenging for autonomous quadrotors, especially when control commands come directly from high-dimensional visual observations. Existing end-to-end methods often rely on behavior cloning or full-rollout backpropagation through time (BPTT) via differentiable simulation, which can limit policy performance or incur high training costs. We propose a two-stage reinforcement learning framework for more efficient ego-centric visuomotor gap-traversal policy training, leveraging quasi-analytical policy gradients (QPG) via differentiable simulation and critic warm-starting. The framework utilizes QPG to avoid backpropagation through visual rendering, reducing computation and memory costs while improving sample efficiency. In the first stage, an expert actor and critic are trained using privileged observations, including gap geometry. Unlike prior gap-traversal approaches, our training utilizing QPG does not require resetting the agent along optimized reference trajectories. In the second stage, a visual policy is trained using binary gap masks from two ego-centric cameras and low-dimensional observations, while its privileged critic is warm-started from the first stage. This substantially improves training efficiency and traversal success compared with cold-starting the critic or using full-rollout BPTT. Our framework does not require retraining the expert actor when system parameters change, enabling more efficient generalization across drone platforms than state-of-the-art visual gap-traversal methods based on action supervision. The learned visual policy also generalizes to gaps with unseen shapes. Extensive real-world experiments further demonstrate robust gap traversal using binary masks rendered online. Beyond gap traversal, the proposed framework is generic and can be extended to other visuomotor robot learning tasks.

</details>

---

### [[20_Research/Papers/强化学习/Can_a_Robot_Read_Braille_-_Learning_to_Adapt_Contact_via_Imitation_Learning_for_Tactile_Braille_Recognition|Can a Robot Read Braille? - Learning to Adapt Contact via Imitation Learning for Tactile Braille Recognition]]

![[assets/2609.30676_figure.png|800]]

- **arXiv**: [2609.30676](https://arxiv.org/abs/2609.30676)
- **PDF**: https://arxiv.org/pdf/2609.30676
- **详细分析**: [[20_Research/Papers/强化学习/Can_a_Robot_Read_Braille_-_Learning_to_Adapt_Contact_via_Imitation_Learning_for_Tactile_Braille_Recognition|Can a Robot Read Braille? - Learning to Adapt Contact via Imitation Learning for Tactile Braille Recognition]]
- **作者**: Xi Chen, Yunlong Shan, Sihan Chen, Jun Hu, Zhongxuan Li, Shiyao Zhang, Sichao Liu, Zhong Zhao, Kosta Jovanovic, Peng Zhou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Can a Robot Read Braille? - Learning to Adapt Contact via Imitation Learning for Tactile Braille Recognition》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For people who are blind, touch provides an essen-tial channel for accessing written information through Braille. Bringing a similar capability to robots requires them not only to recognize tactile patterns, but also to actively establish physical contact that makes those patterns readable. Yet existing robotic Braille readers largely focus on recognition after contact, leaving contact establishment itself insufficiently addressed. We present an adaptive-contact framework for robotic tactile Braille reading that assesses contact quality and physically corrects unsuitable contact before recognition and reconstruc-tion. Multi-Head Policy Learning uses expert-guided contact-adjustment demonstrations to jointly learn contact acceptability and pose corrections. During deployment, the robot iteratively evaluates and re-establishes contact, retaining reliable tactile observations for pose-aware fusion and Braille reconstruction. Across 20 physical Braille plates used for learning and eval-uation, the proposed approach achieves 94.0% tactile quality and 88.6% tactile reconstruction on the ten online-evaluation plates. These results demonstrate the importance of actively establishing readable contact, rather than relying solely on recognition under imperfect tactile observations, for reliable robotic Braille reading.

</details>

---

### [[20_Research/Papers/机器人/MR._POP_Multi-Robot_Parallel_Optimizing_Planner_for_Almost-Surely_Asymptotically_Optimal_Planning|MR. POP: Multi-Robot Parallel Optimizing Planner for Almost-Surely Asymptotically Optimal Planning]]

![[assets/2609.30644_figure.png|800]]

- **arXiv**: [2609.30644](https://arxiv.org/abs/2609.30644)
- **PDF**: https://arxiv.org/pdf/2609.30644
- **详细分析**: [[20_Research/Papers/机器人/MR._POP_Multi-Robot_Parallel_Optimizing_Planner_for_Almost-Surely_Asymptotically_Optimal_Planning|MR. POP: Multi-Robot Parallel Optimizing Planner for Almost-Surely Asymptotically Optimal Planning]]
- **作者**: Chih H. Huang, Roy Xing, Brian Plancher, Zachary Kingston
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《MR. POP: Multi-Robot Parallel Optimizing Planner for Almost-Surely Asymptotically Optimal Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Finding globally optimal paths remains a fundamental challenge in multi-robot motion planning. Despite acceleration of almost-surely asymptotically optimal (a.s.a.o.) planners via CPU-based parallelism, achieving both probabilistic convergence guarantees and strong computational performance, these algorithms still struggle to scale to multi-robot settings. As such, we introduce MR. POP, a GPU-based a.s.a.o. multi-robot planner based on dRRT and the AO-x meta-algorithm. MR. POP uses large-scale GPU-based SIMT-parallelism to simultaneously run hundreds of roadmap construction and tree search iterations with underlying parallel nearest neighbor search and collision checking operations. We show that this enables MR. POP to become the only planner achieving a 100% solve rate while being faster than state-of-the-art a.s.a.o. planners in multi-robot systems up to 35-DOF. MR. POP also raises the success rate of downstream motion optimizers (e.g., from 4% to 72%), by creating high-quality, diverse seeds that help avoid local minima.

</details>

---

### [[20_Research/Papers/机器人/Learning-Accelerated_Narrow-Phase_Collision_Detection_via_Check_Ordering_for_Sampling-Based_Motion_Planning|Learning-Accelerated Narrow-Phase Collision Detection via Check Ordering for Sampling-Based Motion Planning]]

![[assets/2609.30599_figure.png|800]]

- **arXiv**: [2609.30599](https://arxiv.org/abs/2609.30599)
- **PDF**: https://arxiv.org/pdf/2609.30599
- **详细分析**: [[20_Research/Papers/机器人/Learning-Accelerated_Narrow-Phase_Collision_Detection_via_Check_Ordering_for_Sampling-Based_Motion_Planning|Learning-Accelerated Narrow-Phase Collision Detection via Check Ordering for Sampling-Based Motion Planning]]
- **作者**: Hao Jiang, Yinghan Wang, Jianping He, Xiaoming Duan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Learning-Accelerated Narrow-Phase Collision Detection via Check Ordering for Sampling-Based Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collision detection is critical for ensuring the safety of planned paths. However, it imposes a non-negligible computational burden on motion planners, motivating extensive studies on collision-detection acceleration. In commonly used phase-based collision-detection methods, the broad phase employs hierarchical structures to rapidly discard object pairs that are clearly collision-free, while the subsequent narrow phase performs detailed collision checks on the remaining object pairs whose collision status cannot be determined by the broad phase. Although these methods effectively reduce the number of detailed checks through broad-phase pruning, the narrow phase is usually executed in the default order returned by the broad phase, with little explicit optimization of the check order. This leaves room for further acceleration, especially in cluttered environments where many object pairs may remain after the broad phase and the narrow phase can account for a significant portion of the total detection time. In this work, we propose a learning-based method to accelerate phase-based collision detection by optimizing the check order in the narrow phase. We first formulate the expected time cost of the narrow phase and derive an optimal check-ordering criterion that minimizes this expectation. Since the priors required by this criterion are difficult to obtain in advance, we design a hypernetwork-based model to predict collision probabilities, which are then used to approximate the optimal check order. The resulting order guides the execution of exact mesh checks in the narrow phase, thereby reducing detection time without replacing the underlying geometric collision checker. Simulation results show that our method effectively accelerates phase-based collision detection and improves the efficiency and success rate of sampling-based motion planning, especially in cluttered environments.

</details>

---

### [[20_Research/Papers/具身智能/HuGo_LLMs_as_Whole-Body_Policy_Code_Designers_for_Humanoid_Loco-Manipulation|HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation]]

![[assets/2609.30594_figure.png|800]]

- **arXiv**: [2609.30594](https://arxiv.org/abs/2609.30594)
- **PDF**: https://arxiv.org/pdf/2609.30594
- **详细分析**: [[20_Research/Papers/具身智能/HuGo_LLMs_as_Whole-Body_Policy_Code_Designers_for_Humanoid_Loco-Manipulation|HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation]]
- **作者**: Seoyeon Choi, Shizhao Ye, Nicholas Bui, Aayushi Shrivastava, Kanghyun Ryu, Dhruva Tirumala, Markus Wulfmeier, Negar Mehr
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 3.4（加权：具身智能 1.8，大模型 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《HuGo: LLMs as Whole-Body Policy Code Designers for Humanoid Loco-Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For humanoids to be useful in everyday environments, they must perform a wide range of tasks that couple locomotion and manipulation. Existing approaches commonly acquire a loco-manipulation policy through reward engineering or demonstrations followed by task-specific training, making it costly to scale to new tasks. In this work, we propose a hierarchical approach to humanoid loco-manipulation that eliminates these per-task requirements. HuGo, Humanoid policy code Generation, uses a Large Language Model (LLM) to generate executable, closed-loop high-level policy code from a task description on top of a frozen low-level whole-body policy. Given the task, observation, and command specifications, the LLM constructs the task logic in code. HuGo then refines the policy from its rollouts using numerical trajectories and selected video frames to produce feedback and targeted code updates. Across five simulation tasks, using two different low-level policies, HuGo substantially outperforms a high-level reinforcement learning baseline and approaches the performance of a demonstration-based baseline. We achieve this level of performance without task-specific reward design or demonstration collection. We further demonstrate zero-shot transfer of simulation-generated policies to hardware and show that applying the same refinement loop to real-world rollouts can further improve transfer performance without expert demonstrations or policy retraining. Project website is https://iconlab.negarmehr.com/HuGo/

</details>

---

### [[20_Research/Papers/强化学习/MOCHA_Multi-Objective_Co-Design_using_Hypernetwork_Architectures|MOCHA: Multi-Objective Co-Design using Hypernetwork Architectures]]

![[assets/2609.30570_figure.png|800]]

- **arXiv**: [2609.30570](https://arxiv.org/abs/2609.30570)
- **PDF**: https://arxiv.org/pdf/2609.30570
- **详细分析**: [[20_Research/Papers/强化学习/MOCHA_Multi-Objective_Co-Design_using_Hypernetwork_Architectures|MOCHA: Multi-Objective Co-Design using Hypernetwork Architectures]]
- **作者**: Varun Madabushi, Neil Janwani, Maegan Tucker
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《MOCHA: Multi-Objective Co-Design using Hypernetwork Architectures》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HYPER-MORL, MORL, Meta-RL, PD-MORL, PSL-MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we present MOCHA, the first, to our knowledge, reinforcement learning based approach to computing a family of Pareto-optimal policies across the design space of a robot using a single network. Specifically, MOCHA leverages the hypernetwork architecture to learn a network that produces specialized network parameters optimized for a given objective and parameterized robot design; we term this a multi-objective design hypernetwork (MDH). We demonstrate the capabilities of MDHs to represent a complex family of design-dependent strategies on two distinct robot morphologies, each with six design dimensions and across 2-3 objectives. Moreover, we propose an approach for efficiently producing a Design Pareto set using evolutionary search of the learned policy network, generating the optimal design-policy combination for each objective prioritization. Lastly, we provide an efficient method for computing generalist robot designs which achieve the best cumulative performance across the entire set of objectives.

</details>

---

### [[20_Research/Papers/具身智能/SoGuDiff_Socially_Guided_Diffusion_for_Steerable,_Norm-Grounded_Robot_Navigation|SoGuDiff: Socially Guided Diffusion for Steerable, Norm-Grounded Robot Navigation]]

![[assets/2609.30560_figure.png|800]]

- **arXiv**: [2609.30560](https://arxiv.org/abs/2609.30560)
- **PDF**: https://arxiv.org/pdf/2609.30560
- **详细分析**: [[20_Research/Papers/具身智能/SoGuDiff_Socially_Guided_Diffusion_for_Steerable,_Norm-Grounded_Robot_Navigation|SoGuDiff: Socially Guided Diffusion for Steerable, Norm-Grounded Robot Navigation]]
- **作者**: Christian Schaible, Haoran Ji, Yash Vardhan Pant, Stephen L. Smith
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《SoGuDiff: Socially Guided Diffusion for Steerable, Norm-Grounded Robot Navigation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HuNavSim, Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Beyond collision avoidance, socially competent robot navigation requires adherence to implicit social conventions that vary across contexts, cultures, and deployment requirements. Many conventional navigation policies learn a single normative behavior, either through reinforcement learning against a fixed reward function or imitation of human demonstrations, exposing no interface for adjusting that conduct at runtime. We present a diffusion-based navigation framework whose social behavior can be tuned at deployment: a desired style is specified, such as how closely the robot passes, which side it yields to, or how much it defers to groups, and the planner adapts accordingly. Continuous style axes can be followed independently or composed, spanning a behavioral space rather than discrete, primitive-based specifications. A feasibility projection layer separates learned social behavior from kinematic feasibility and collision avoidance. A single-axis sweep illustrates a tradeoff curve that strictly dominates the evaluated fixed-behavior baseline configurations, and stylistic differences are replicated in real-world demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/Privacy-Preserving_Prompted_Policy_Search_for_Robotic_Control|Privacy-Preserving Prompted Policy Search for Robotic Control]]

![[assets/2609.30554_figure.png|800]]

- **arXiv**: [2609.30554](https://arxiv.org/abs/2609.30554)
- **PDF**: https://arxiv.org/pdf/2609.30554
- **详细分析**: [[20_Research/Papers/具身智能/Privacy-Preserving_Prompted_Policy_Search_for_Robotic_Control|Privacy-Preserving Prompted Policy Search for Robotic Control]]
- **作者**: Ali Irshayyid, Feng Lin, Chong Li, Jun Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.1，强化学习 0.4，机器人 1.1）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《Privacy-Preserving Prompted Policy Search for Robotic Control》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have recently demonstrated promising capabilities as in-context policy optimizers for Reinforcement Learning (RL), enabling policy search driven by both numerical reward signals and natural language reasoning. However, deploying such methods in practice requires transmitting raw policy parameters and rewards history to cloud-based LLM APIs, exposing proprietary control strategies to third-party service providers. To address this issue, this paper introduces Privacy-Preserving Prompted Policy Search (PP-ProPS), a framework that enables LLM-guided policy optimization while keeping policy and environmental parameters confidential. PP-ProPS encodes policy parameters and reward values using secret client-side transformations before they are included in each API request, ensuring that the LLM provider observes only encoded policy parameters and scaled reward information. Furthermore, unlike Vanilla ProPS, the proposed framework does not require the true optimal episodic return to be known or disclosed to the LLM. Beyond protecting the optimization data, PP-ProPS improves the search process in two ways. First, it provides the LLM with individual reward components instead of only a single total return, offering more informative feedback about each candidate policy. Second, it uses a bounded history that prevents the prompt from growing indefinitely, improving search with high-dimensional policies and supporting the use of open-weight LLMs. The proposed PP-ProPS is evaluated on both continuous and discrete control problems spanning Multi-Joint dynamics with Contact (MuJoCo) locomotion, classic control, highway driving, and robotic arm manipulation. Compared to Vanilla ProPS, the proposed PP-ProPS outperforms ProPS in seven of the ten evaluated tasks, and surpasses conventional RL methods including PPO, SAC, and TRPO, in five of the six tasks.

</details>

---

### [[20_Research/Papers/具身智能/GraspTwin_Zero-Shot_Task-Oriented_Grasp_Optimization_via_a_Digital_Twin|GraspTwin: Zero-Shot Task-Oriented Grasp Optimization via a Digital Twin]]

![[assets/2609.30543_figure.png|800]]

- **arXiv**: [2609.30543](https://arxiv.org/abs/2609.30543)
- **PDF**: https://arxiv.org/pdf/2609.30543
- **详细分析**: [[20_Research/Papers/具身智能/GraspTwin_Zero-Shot_Task-Oriented_Grasp_Optimization_via_a_Digital_Twin|GraspTwin: Zero-Shot Task-Oriented Grasp Optimization via a Digital Twin]]
- **作者**: Daniel J. Evans, Yinlong Dai, Simon Stepputtis, Dylan P. Losey
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《GraspTwin: Zero-Shot Task-Oriented Grasp Optimization via a Digital Twin》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, GraspNet, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As robots transition from structured factory settings into homes, they are required to interact with an ever-increasing variety of objects. Many tasks require grasping, and often it is not sufficient to just pick up the target object. Consider a task like "pouring coffee" --- to facilitate the subsequent pouring, the robot should grasp the mug by its handle. Existing learning-based approaches for grasping either find robust and collision-free grasps that are largely agnostic to the task (e.g., picking up the mug by its rim), or leverage foundation models to propose task-appropriate grasp locations that lack fine-grained physical grounding (e.g., reaching for and missing the handle). In this work, we bridge these approaches with a real-to-sim-to-real framework. Based on a single RGB-D observation, we construct a digital twin of the environment, query a large foundation model to propose grasps that align with the object's affordances and task description, and then optimize the proposals to ensure robustness and plausibility before executing the result on the real robot. Our key insight is that the grasp proposals of the foundation model should be regarded as semantic priors that serve as seeds for local, gradient-free optimization. We leverage Bayesian optimization with Thompson sampling to draw batches of nearby poses, which are subsequently evaluated in parallel under domain-randomized physics rollouts. The resulting grasp is both task-oriented and physically feasible for execution by the robot arm. Our full zero-shot real-world transfer only takes a few minutes and improves task-oriented grasping success by up to 33% as compared to other state-of-the-art pipelines. Our code is available here: https://github.com/VT-Collab/GraspTwin/

</details>

---

### [[20_Research/Papers/机器人/A_Long-Legged,_Direct-Drive_Monopedal_Robot_Achieves_Exceptional_Jump_Height|A Long-Legged, Direct-Drive Monopedal Robot Achieves Exceptional Jump Height]]

![[assets/2609.30530_figure.jpg|800]]

- **arXiv**: [2609.30530](https://arxiv.org/abs/2609.30530)
- **PDF**: https://arxiv.org/pdf/2609.30530
- **详细分析**: [[20_Research/Papers/机器人/A_Long-Legged,_Direct-Drive_Monopedal_Robot_Achieves_Exceptional_Jump_Height|A Long-Legged, Direct-Drive Monopedal Robot Achieves Exceptional Jump Height]]
- **作者**: Gihyeok Na, Justin K. Yim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Long-Legged, Direct-Drive Monopedal Robot Achieves Exceptional Jump Height》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We demonstrate a jumping robot that reaches high (7.6 m) and fast (190 ms stance time) jumps from a single long leg driven by a direct-drive transmission, without elastic energy storage. At 281 g, it achieves the highest jump yet reported for an electrically actuated, spring-free system. The leg uses a new fabric-wrap transmission that provides a variable mechanical advantage, keeping a small electric motor near its peak power output through the stroke while bracing the long, lightweight leg against buckling. A balancing module at the top of the leg uses small propellers to control the leg's orientation on the ground and in the air, where the long leg provides a large moment arm for the control torques. The robot is validated outdoors with vertical jumps, attitude control on the ground and in flight, and tilted jumps.

</details>

---

### [[20_Research/Papers/大模型/Containing_Behavioral_Cascades_from_Manipulated_Claims_in_LLM-Powered_Multi-Robot_Systems|Containing Behavioral Cascades from Manipulated Claims in LLM-Powered Multi-Robot Systems]]

![[assets/2609.30523_figure.png|800]]

- **arXiv**: [2609.30523](https://arxiv.org/abs/2609.30523)
- **PDF**: https://arxiv.org/pdf/2609.30523
- **详细分析**: [[20_Research/Papers/大模型/Containing_Behavioral_Cascades_from_Manipulated_Claims_in_LLM-Powered_Multi-Robot_Systems|Containing Behavioral Cascades from Manipulated Claims in LLM-Powered Multi-Robot Systems]]
- **作者**: Waleed Bin Khalid, Byung-Cheol Min
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.6，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Containing Behavioral Cascades from Manipulated Claims in LLM-Powered Multi-Robot Systems》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-powered multi-robot systems are vulnerable to semantic manipulation: an accepted false world-state claim can trigger a fleet-wide behavioral cascade, causing unnecessary replanning, increased path costs, congestion, or apparent mission infeasibility. Conditioning on a successful manipulation, we propose an active verification framework that contains its downstream effects before they propagate across the fleet. A dedicated verification module generates a structured Verify-Adapt-Hold plan: selected robots inspect consequential regions, a limited subset provisionally adapts when necessary, and the remaining robots retain their trusted plans. We evaluate the framework in a multi-robot transportation environment using injected false obstacle claims across different impacts and team sizes. Evaluation measures cascade containment, Sum-of-Costs, makespan, and coverage ratio. Results show that treating post-compromise verification as a team-level planning problem, rather than a binary trust decision, effectively limits the cascading physical consequences of semantic manipulation.

</details>

---

### [[20_Research/Papers/机器人/Tactile_Sensing_Array_for_Multi-Phalanx_Sensing_in_Humanoid_Hands|Tactile Sensing Array for Multi-Phalanx Sensing in Humanoid Hands]]

![[assets/2609.30506_figure.png|800]]

- **arXiv**: [2609.30506](https://arxiv.org/abs/2609.30506)
- **PDF**: https://arxiv.org/pdf/2609.30506
- **详细分析**: [[20_Research/Papers/机器人/Tactile_Sensing_Array_for_Multi-Phalanx_Sensing_in_Humanoid_Hands|Tactile Sensing Array for Multi-Phalanx Sensing in Humanoid Hands]]
- **作者**: Neel Adwani, Muhaiminul Islam Akash, Rituja Bhattacharya, Cong Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Tactile Sensing Array for Multi-Phalanx Sensing in Humanoid Hands》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid hands require tactile feedback across the whole finger, not just the fingertip, to grasp and manipulate objects properly. Vision and proprioception alone cannot reliably provide this information, particularly when the hand's own fingers occlude the camera's view of the grasp. We present a low-cost tactile array for a humanoid finger, made from Velostat and conductive tape. The fingertip carries seven contact points including a 2x3 matrix wrapped across its front, left, and right faces, and a separate contact point at the tip. The proximal and middle phalanges each carry a single front-facing contact line. We measure the sensor's hysteresis and recovery time after release, through repeated loading and press-release tests. We also test a compliant, 3D-printed contact structure with a gap and a bump, inspired by similar designs in prior work, and show it cuts recovery time by 74% compared to a flush-contact baseline. We then show the sensor can produce distinct activation patterns for different contact geometries (flat, edge, corner) at the fingertip, and that it registers contact across all three phalanges during a grip. Finally, we discuss the limits of our fabrication changes and point to software-based compensation as a promising way to more directly fix the remaining hysteresis in the future.

</details>

---

### [[20_Research/Papers/机器人/Learning-Based_Pressure_Predictive_Control_of_a_Vertebraic_Soft_Robotic_Tail|Learning-Based Pressure Predictive Control of a Vertebraic Soft Robotic Tail]]

![[assets/2609.30479_first_page.png|800]]

- **arXiv**: [2609.30479](https://arxiv.org/abs/2609.30479)
- **PDF**: https://arxiv.org/pdf/2609.30479
- **详细分析**: [[20_Research/Papers/机器人/Learning-Based_Pressure_Predictive_Control_of_a_Vertebraic_Soft_Robotic_Tail|Learning-Based Pressure Predictive Control of a Vertebraic Soft Robotic Tail]]
- **作者**: Wenjian Yang, Nan Huang, Yukang Nie, Fang Chen, Wanchao Chi, Jiansheng Dai, Sicong Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Learning-Based Pressure Predictive Control of a Vertebraic Soft Robotic Tail》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft robots have attracted much attention for their safe human-robot interaction and flexibility, but the typical continuum structure and nonlinear material behavior make the kinematics modelling complex, especially in non-static motions. In this work, we proposed an LSTM-based pressure predictive control (PPC) for the motion control of a vertebraic soft robotic tail and the coordination with a quadruped robot. The PPC consists of an inverse kinematics (IK) model, a forward kinematics (FK) model and a pressure compensation (P-comp) model, and achieves non-static and quasi-static motion control of the tail. Compared with the IK-only model, the average RMSE of the PPC's simulation trajectories reduces by 69.8%, when executing target trajectories. In the coordinated motions of the soft tail quadruped, using a prediction data set to train the PPC enables next-moment action prediction and reduces computation time by 60.9%, which enhances the real-time response of the tail to match the quadruped torso's moving rate. The PPC provides a simple and effective method to model the soft tail for both non-static and quasi-static motion control, and grants the soft tail quadruped with the functionality of interacting with the environment.

</details>

---

### [[20_Research/Papers/大模型/Policy-Calibrated_DAgger_Offline_Calibrated_Noise_Injection_for_Imitation_Learning|Policy-Calibrated DAgger: Offline Calibrated Noise Injection for Imitation Learning]]

![[assets/2609.30462_figure.png|800]]

- **arXiv**: [2609.30462](https://arxiv.org/abs/2609.30462)
- **PDF**: https://arxiv.org/pdf/2609.30462
- **详细分析**: [[20_Research/Papers/大模型/Policy-Calibrated_DAgger_Offline_Calibrated_Noise_Injection_for_Imitation_Learning|Policy-Calibrated DAgger: Offline Calibrated Noise Injection for Imitation Learning]]
- **作者**: Jenny Wang, George Kantor
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Policy-Calibrated DAgger: Offline Calibrated Noise Injection for Imitation Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Policies trained with imitation learning can accumulate errors over time, causing the robot to drift outside the training distribution. Existing methods mitigate this covariate shift by collecting additional data where the policy fails or is likely to fail. The first places the robot in unsafe conditions and the second requires choosing an appropriate noise distribution to collect new expert demonstrations under that noise. We propose Policy-Calibrated DAgger, a method that makes use of the properties of recent generative policies to estimate the policy's noise offline by using its own predicted action distribution. We measure a diffusion policy's spread of predicted actions at observations along the expert trajectory and measure its closed-loop error relative to a recorded trajectory. To address issues with measuring error in a multimodal action space, we guide the policy towards the trajectory during closed-loop control through partial denoising, and use properties of a diffusion model to unnormalize the measured error as if we did not guide it. We experiment in a scenario where a robot is tasked to reach an engine lever in a cluttered and narrow environment and show results in a 3D photorealistic simulator and a 2D planar reacher environment. We show that our method surpasses policies trained with dataset aggregation without noising and matches the performance of the best noise level in hindsight, without requiring a sweep over noise levels.

</details>

---

### [[20_Research/Papers/具身智能/DGT-Map_Directional_Global_Traversability_Mapping_Utilizing_Multi-Task_Learning_for_Heterogeneous_Vehicles|DGT-Map: Directional Global Traversability Mapping Utilizing Multi-Task Learning for Heterogeneous Vehicles]]

![[assets/2609.30461_figure.png|800]]

- **arXiv**: [2609.30461](https://arxiv.org/abs/2609.30461)
- **PDF**: https://arxiv.org/pdf/2609.30461
- **详细分析**: [[20_Research/Papers/具身智能/DGT-Map_Directional_Global_Traversability_Mapping_Utilizing_Multi-Task_Learning_for_Heterogeneous_Vehicles|DGT-Map: Directional Global Traversability Mapping Utilizing Multi-Task Learning for Heterogeneous Vehicles]]
- **作者**: Jaskrit Singh, Kashif K. Noori, Jing Xiao, Constantinos Chamzas
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《DGT-Map: Directional Global Traversability Mapping Utilizing Multi-Task Learning for Heterogeneous Vehicles》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Off-road traversability is direction-dependent and vehicle specific, yet most global maps assign a single isotropic cost to each location. Existing learned estimators are also commonly trained independently for each vehicle; this preserves vehicle-specific behavior but prevents vehicles from sharing common terrain representations. DGT-MAP addresses both limitations through a self-supervised framework that learns global, directional, and vehicle-conditioned traversability costmaps from RGB-D observations and locomotion signals. A shared multi-task backbone learns common terrain features across training vehicles while vehicle-specific prediction heads preserve platform-dependent responses. At inference, DGT-MAP produces a heading-indexed costmap that can be used by a direction-aware planner. We evaluate DGT-MAP in simulation by integrating it into a Hybrid A* navigation stack and measuring downstream task success on challenging terrains, including slopes that are traversable downhill but not uphill and a ridge obstacle that is traversable by some vehicles, but not by others. Across evaluated tasks, DGT-MAP achieves the highest or tied-highest navigation success rate when compared against geometric, binary, and learned direction-agnostic baselines.

</details>

---

### [[20_Research/Papers/机器人/Realizability_Is_Not_Enough_Encoding,_Liveness,_and_Auditing_of_Synthesized_Robot_Supervisors|Realizability Is Not Enough: Encoding, Liveness, and Auditing of Synthesized Robot Supervisors]]

![[assets/2609.30460_figure.jpg|800]]

- **arXiv**: [2609.30460](https://arxiv.org/abs/2609.30460)
- **PDF**: https://arxiv.org/pdf/2609.30460
- **详细分析**: [[20_Research/Papers/机器人/Realizability_Is_Not_Enough_Encoding,_Liveness,_and_Auditing_of_Synthesized_Robot_Supervisors|Realizability Is Not Enough: Encoding, Liveness, and Auditing of Synthesized Robot Supervisors]]
- **作者**: David C. Conner, Joshua Luzier, William J. Doyle, Emma R. Faith, Aubrie B. Kooiker, Andrew J. Farney, Sebastian Fox, Evangelina Grimes, Ian G. Conner, Kyle Bloom
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Realizability Is Not Enough: Encoding, Liveness, and Auditing of Synthesized Robot Supervisors》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PyRoboSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-level robotic supervisors coordinate capabilities whose reported outcomes determine the robot's next action. Reactive synthesis can generate such supervisors with formal guarantees, but deployment requires more than proving a Generalized Reactivity (1) (GR(1)) specification realizable. Designers must encode failure-prone capabilities, choose liveness assumptions that match retry intent, audit strategies, and translate them into robot software. We present an open-source pipeline for Robot Operating System (ROS) 2 Flexible Behavior Engine (FlexBE) supervisors that generates capability-based GR(1) specifications, analyzes assumptions before synthesis, audits strategies, reduces states with a behavior-preservation proof, and emits executable state machines. Across four case studies (six comparisons), including hardware on two quadcopter platforms, we compare enumerated and one-hot encodings and two liveness formulations. Under the tested backend, enumerated encoding usually synthesizes faster, although fewer propositions do not reliably predict smaller controllers or lower symbolic cost. System-Goal without pending memory is the only liveness treatment confirmed to yield executable controllers under both encodings across the reported grid; Fair-Outcome can permit realizable cycles without designer-intended completion. For this backend and model, we recommend enumerated encoding with System-Goal and auditing every realized strategy, since proposition count and realizability do not measure deployability. The auditor is sound and complete for four structural defect classes (protocol violations, deadlocks, bounded-failure violations, goal-unreachable traps) but is not a general liveness verifier, and the reduction preserves capability-level behavior. Together, these stages narrow the gap between formal realizability and controllers that pass protocol and structural-progress checks.

</details>

---

### [[20_Research/Papers/大模型/POIL_Point-based_One-Shot_Imitation_Learning_with_Stable_Dynamical_Systems|POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems]]

![[assets/2609.30404_figure.png|800]]

- **arXiv**: [2609.30404](https://arxiv.org/abs/2609.30404)
- **PDF**: https://arxiv.org/pdf/2609.30404
- **详细分析**: [[20_Research/Papers/大模型/POIL_Point-based_One-Shot_Imitation_Learning_with_Stable_Dynamical_Systems|POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems]]
- **作者**: Sang Min Kim, Jinwoo Seo, Hyeongjun Heo, Junho Lee, Yonghyeon Lee, Young Min Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《POIL: Point-based One-Shot Imitation Learning with Stable Dynamical Systems》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present POIL, a point-based one-shot imitation learning framework with stable dynamical systems. While one-shot imitation avoids collecting extensive demonstrations, successful one-shot manipulation requires not only transferring a demonstrated trajectory to a novel object but also executing it robustly under changing scene conditions, grasp configurations, and external disturbances. POIL addresses both problems through a shared representation: a set of 3D points on the object's functional part, used jointly for trajectory transfer and closed-loop execution. The one-shot transfer from the demonstrated trajectory is enabled with point correspondences. POIL grounds the shared functional part with a multi-modal large language model, and transfers the trajectory across viewpoint, pose, and object category changes. During execution, multi-view tracking observes the same points online, and Point-set BCSDM drives them in closed loop by projecting per-point velocities onto a single rigid-body twist computed from the tracked points alone. This extends stable dynamical models from an SE(3) pose to a point set without requiring a known 3D model or pose estimator. We show that at the goal the controller becomes a gradient flow on the classical SO(3) potential, so its terminal phase inherits the almost-global convergence of that potential under a rigid-object assumption. Across simulation and real-robot experiments, POIL transfers a single demonstration across object category, grasp pose, and goal geometry, while recovering from external disturbances during execution. Project page: https://sangminkim-99.github.io/poil

</details>

---
