# cs.RO | Robotics | 2026-11-23

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/强化学习/Task2Hand_A_Contact-Grounded_Skill_for_Parametric_Dexterous-Hand_Morphology_Design|Task2Hand: A Contact-Grounded Skill for Parametric Dexterous-Hand Morphology Design]]

![[assets/2611.27967_figure.jpg|800]]

- **arXiv**: [2611.27967](https://arxiv.org/abs/2611.27967)
- **PDF**: https://arxiv.org/pdf/2611.27967
- **详细分析**: [[20_Research/Papers/强化学习/Task2Hand_A_Contact-Grounded_Skill_for_Parametric_Dexterous-Hand_Morphology_Design|Task2Hand: A Contact-Grounded Skill for Parametric Dexterous-Hand Morphology Design]]
- **作者**: Haoyang Wang, Weibo Gao, Zhengxiong Li, Lingfeng Tao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Task2Hand: A Contact-Grounded Skill for Parametric Dexterous-Hand Morphology Design》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous hand design demands repeated expert work across geometry, robot-description code, collision debugging, grasp initialization, and policy training. We present Task2Hand, a Skill: a specification package that turns a functional manipulation brief into a parameterized hand model and routes every candidate through cost-ordered contact, dynamics, and learning gates. Each gate returns a status and an evidence record; on failure, the Skill records the earliest blocker, revises one bounded parameter group, and reruns the cheaper gates. The agent generates, validates, and trains autonomously within declared bounds, and escalates trade-offs, plateaus, and conflicting evidence to a human who sets the next design direction. An evidence-driven design trajectory for bidirectional in-hand manipulation yielded SAGE Hand (Skill-Aware Generative Embodiment): four fingers, 16 actuated DoF, an integrated guiding palm, compact roots, cylindrical tips, and a collision-cleared opposable thumb. Under a matched training protocol, SAGE Hand reaches 45.6% task success on a hexagonal prism against 37.3% for the LEAP hand, and 70.8% on a bicolor cylinder against 51.6%. Dense simulated tactile input more than halves the cylinder drop rate. In a controlled iteration study, the Skill path preserves capture at 164/165 trials while the path without the Skill degrades to 14/165, confirming that the gates act as a regression guard during refinement. Accepted candidates pack with URDF/MJCF, metrics, checkpoints, and a provenance manifest.

</details>

---

### [[20_Research/Papers/大模型/Real-time_neuromorphic_audio_and_vision_perception_for_autonomous_robotic_applications_Integration_and_experimental_evaluation_on_a_rover_pl|Real-time neuromorphic audio and vision perception for autonomous robotic applications: Integration and experimental evaluation on a rover platform]]

![[assets/2611.27953_figure.png|800]]

- **arXiv**: [2611.27953](https://arxiv.org/abs/2611.27953)
- **PDF**: https://arxiv.org/pdf/2611.27953
- **详细分析**: [[20_Research/Papers/大模型/Real-time_neuromorphic_audio_and_vision_perception_for_autonomous_robotic_applications_Integration_and_experimental_evaluation_on_a_rover_pl|Real-time neuromorphic audio and vision perception for autonomous robotic applications: Integration and experimental evaluation on a rover platform]]
- **作者**: Guillem Fustier-Castillo, Ruben Ribes-Serrano, Javier Naranjo-Alcazar, Vicent Ortiz-Castello, Pedro Zuccarello
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.1，机器人 1.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Real-time neuromorphic audio and vision perception for autonomous robotic applications: Integration and experimental evaluation on a rover platform》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AudioSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Neuromorphic sensing and computing offer a promising alternative to conventional deep learning pipelines for mobile robots, where perception must run continuously under tight latency and energy constraints. However, most neuromorphic solutions are still evaluated offline or on isolated benchmarks, and their integration into complete robotic systems remains largely unexplored. In this technical report, a four-wheel rover platform is presented that combines three real-time perception pipelines: a classical audio tagging pipeline based on Pretrained Audio Neural Networks (PANNs) running on an NVIDIA Jetson GPU, a neuromorphic audio pipeline in which a spiking neural network (SNN) is deployed on the SynSense Xylo Audio~2 chip, and a neuromorphic vision pipeline in which events from an event-based camera are processed by the SpikeYOLO spiking detector for traffic cone detection. On the Xylo chip, the whole processing chain---from the microphone signal to the classification of low- and high-pitched sounds---is performed on-chip, while the host only configures the device and reads the output neurons. All models are deployed as containerised services and integrated through ROS~2, and a configurable action dispatcher maps the detected classes to robot behaviours, closing the loop between perception and actuation. The platform is demonstrated in a proof-of-concept scenario in which the robot reacts to sound classes detected by both audio pipelines and detects traffic cones with the event camera, showing the feasibility of integrating neuromorphic hardware into a multimodal robotic platform operating in real time.

</details>

---

### [[20_Research/Papers/强化学习/What_Must_a_Model_Tell_a_Planner_Outcome_Interfaces_for_Risk-Aware_Planning_After_Robot_Damage|What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage]]

![[assets/2611.27939_figure.png|800]]

- **arXiv**: [2611.27939](https://arxiv.org/abs/2611.27939)
- **PDF**: https://arxiv.org/pdf/2611.27939
- **详细分析**: [[20_Research/Papers/强化学习/What_Must_a_Model_Tell_a_Planner_Outcome_Interfaces_for_Risk-Aware_Planning_After_Robot_Damage|What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage]]
- **作者**: Hassan Iqbal, Krishna Kumar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《What Must a Model Tell a Planner? Outcome Interfaces for Risk-Aware Planning After Robot Damage》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a robot is damaged, it must decide which routes it can still afford, and the amount of risk it may accept can change from one mission to the next. We argue that whether a learned model helps such a robot depends on its decision interface, that is, on what the model hands to the planner. A decision policy tells the planner what to do, whereas an outcome model, a kind of world model, predicts the consequences of each route. We study simulated Unitree Go2 quadrupeds and H1 humanoids with weakened motors, added payloads, or reduced foot friction. We compare four interfaces. The first is a decision policy, and the second is the same policy trained with fixed penalties for infeasible routes. The third is an outcome model that predicts the feasibility and travel time of each route. The fourth, which we call a capability contract, is an outcome model that predicts the chance of success and the travel time of the robot on each terrain and composes them along a route. All share the same collected experience, matched tuning and risk calibration, and an uncertainty guard. Two comparatively low-risk probes let the capability contract rank hazardous terrains about as well as four new trials on every hazard. At a calibrated 5% limit on selecting empirically infeasible routes, outcome models cut declined missions from about 32% to 7-8% on Go2 and from 57% to 35-36% on H1 compared with the plain policy. Fixed penalties narrow this gap, but the best penalty changes with the risk target. Predicting outcomes lets the planner preserve missions by changing routes as risk requirements tighten.

</details>

---

### [[20_Research/Papers/机器人/Humanoid_robots_for_safety-critical_electrical_switching_A_perception-informed_runtime_constraint_filter|Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter]]

![[assets/2611.27845_figure.jpg|800]]

- **arXiv**: [2611.27845](https://arxiv.org/abs/2611.27845)
- **PDF**: https://arxiv.org/pdf/2611.27845
- **详细分析**: [[20_Research/Papers/机器人/Humanoid_robots_for_safety-critical_electrical_switching_A_perception-informed_runtime_constraint_filter|Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter]]
- **作者**: Songyang Liu, Yu Hou, Yuqing Hu, Shuai Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Humanoid robots for safety-critical electrical switching: A perception-informed runtime constraint filter》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots can reduce personnel exposure in electrical switching, but safe control is challenging because the tool must reach a target switch next to similar devices, where an imprecise operator command can contact a non-target switch. This study proposes a runtime safety filter that checks each operator command during virtual-reality teleoperation of a humanoid robot. The filter integrates a scene model estimated from the robot head camera and a target-conditioned control barrier function quadratic program that keeps the tool away from the non-target switch while passing safe commands unchanged. In real-world experiments on a Unitree G1 humanoid robot, with six rounds at each of two standing positions, target operations succeed in all ten rounds with an unchanged target and no non-target actuation. A simulation study achieves 9/9 safe completions, compared with 5/9 for raw teleoperation, demonstrating the feasibility of the method for humanoid switching operations.

</details>

---

### [[20_Research/Papers/具身智能/BRINA_Bottom-Referenced_Inertial_Navigation_with_AKAZE,_a_Sonar_SLAM_for_Autonomous_Marine_Vehicles|BRINA: Bottom-Referenced Inertial Navigation with AKAZE, a Sonar SLAM for Autonomous Marine Vehicles]]

![[assets/2611.27817_figure.png|800]]

- **arXiv**: [2611.27817](https://arxiv.org/abs/2611.27817)
- **PDF**: https://arxiv.org/pdf/2611.27817
- **详细分析**: [[20_Research/Papers/具身智能/BRINA_Bottom-Referenced_Inertial_Navigation_with_AKAZE,_a_Sonar_SLAM_for_Autonomous_Marine_Vehicles|BRINA: Bottom-Referenced Inertial Navigation with AKAZE, a Sonar SLAM for Autonomous Marine Vehicles]]
- **作者**: Adolfo Damiano Cafaro, Patrizio Mariani, Roberto Galeazzi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《BRINA: Bottom-Referenced Inertial Navigation with AKAZE, a Sonar SLAM for Autonomous Marine Vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forward-looking sonar (FLS) provides reliable underwater perception where optical sensing is limited, but its use for navigation is hindered by the unobserved elevation of each return. As a result, motion estimated directly from sonar images suffers from an unknown metric scale that is commonly resolved using a Doppler velocity log (DVL). We present BRINA (Bottom-Referenced Inertial Navigation with AKAZE), a sonar-inertial SLAM system for marine vehicles that uses the FLS as its only exteroceptive sensor. BRINA estimates the sonar altitude from the first seabed return in each beam and uses it to project matched features onto the seabed, providing metric odometry without a DVL. We further derive a bound relating the remaining scale error to seabed tilt and slope variability. The method is evaluated in simulation with an autonomous underwater vehicle, and in field experiments with uncrewed surface vehicles over ten missions, using two FLS systems under different operating conditions.

</details>

---

### [[20_Research/Papers/具身智能/EvoTER_Evolving_Embodied_Agents_via_Tool-Use_Experience_and_Reflection|EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection]]

![[assets/2611.27797_figure.png|800]]

- **arXiv**: [2611.27797](https://arxiv.org/abs/2611.27797)
- **PDF**: https://arxiv.org/pdf/2611.27797
- **详细分析**: [[20_Research/Papers/具身智能/EvoTER_Evolving_Embodied_Agents_via_Tool-Use_Experience_and_Reflection|EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection]]
- **作者**: Yingting Zhou, Yuyin Zhou, Yongliang Wang, Haoran Li, Dongbin Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.5，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《EvoTER: Evolving Embodied Agents via Tool-Use Experience and Reflection》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CheckVLA, ProactiveVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon embodied tasks require agents to ground instructions in changing observations, coordinate heterogeneous tools, and recover from failures that can propagate through downstream operations. Although existing LLM-based agents retain experience and refine reusable skills, successful local repairs do not by themselves establish complete-task gains over the current shared procedure library. We present EvoTER, an experience-driven framework that enables embodied agents to self-evolve tool-use skills without updating model parameters. EvoTER operates through a three-role evolution loop: Explorer records tool-use trajectories; Diagnoser distills successful and failed executions into skills for tool selection, parameter computation, postcondition checks, and recovery; and Validator retains candidate revisions only when they improve complete-task success in fresh sessions. In simulation, EvoTER improves overall task success from a pre-evolution baseline of 53.60% to 80.40%. In real-world experiments, simulation initialization reduces the attempts required to acquire short-horizon skills, while continued real-world evolution improves long-horizon success from 20% to 80%-100% across tasks and enables the evolving skill library to incorporate new tool functionality introduced after simulation development. Project page: https://evoter-project.github.io/

</details>

---

### [[20_Research/Papers/具身智能/An_Autonomous_Adaptive_Learning_System_for_Robotic_Grasping_in_the_Circular_Factory|An Autonomous Adaptive Learning System for Robotic Grasping in the Circular Factory]]

![[assets/2611.27782_first_page.png|800]]

- **arXiv**: [2611.27782](https://arxiv.org/abs/2611.27782)
- **PDF**: https://arxiv.org/pdf/2611.27782
- **详细分析**: [[20_Research/Papers/具身智能/An_Autonomous_Adaptive_Learning_System_for_Robotic_Grasping_in_the_Circular_Factory|An Autonomous Adaptive Learning System for Robotic Grasping in the Circular Factory]]
- **作者**: Yitian Shi, Rosa Wolf, Rania Rayyes
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《An Autonomous Adaptive Learning System for Robotic Grasping in the Circular Factory》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Linear manufacturing typically operates in highly structured settings with standardized objects, allowing robots to execute pre-programmed motions based on precise models. In contrast, circular manufacturing involves dynamic and less controlled environments, where product components can vary due to appearance and physical changes across different product generations. In this context, uncertainty arises from both the unknown or partially observed states of components (e.g., damaged surfaces, altered shapes) and the unstructured disassembly environment, often characterized by heavy clutter, occlusions, and limited sensing viewpoints. This demands a flexible and adaptable robotic grasping system that can cope with unexpected object changes. To address these challenges, this paper proposes an autonomous grasp learning framework designed for highly uncertain and variable conditions. The framework explicitly distinguishes between uncertainty due to noisy or incomplete sensory observations (aleatoric uncertainty) and uncertainty due to limited knowledge and distribution shift (epistemic uncertainty). Moreover, the framework employs an active perception strategy to reduce visual ambiguity: semantic and spatial scene understanding is achieved using vision language models (VLMs), while view planning enables the robot to adjust its viewpoint to improve observability. In addition, the approach leverages large-scale human demonstration data to learn interaction patterns, which are then transferred to robotic end-effectors, enabling robust manipulation in these variable settings. Quantitative validation, including the utility of active vision on disassembled components in practice, is expected to form an important part of future work.

</details>

---

### [[20_Research/Papers/强化学习/Trust_What_Repeats_Capped_World-Model_Policy_Gradients_for_Humanoid_Motion_Tracking|Trust What Repeats: Capped World-Model Policy Gradients for Humanoid Motion Tracking]]

![[assets/2611.27648_figure.png|800]]

- **arXiv**: [2611.27648](https://arxiv.org/abs/2611.27648)
- **PDF**: https://arxiv.org/pdf/2611.27648
- **详细分析**: [[20_Research/Papers/强化学习/Trust_What_Repeats_Capped_World-Model_Policy_Gradients_for_Humanoid_Motion_Tracking|Trust What Repeats: Capped World-Model Policy Gradients for Humanoid Motion Tracking]]
- **作者**: Xuzhe Dang, Stefan Edelkamp
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，世界模型 0.2，机器人 1.1）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Trust What Repeats: Capped World-Model Policy Gradients for Humanoid Motion Tracking》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ProCuRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training a humanoid motion tracker by backpropagating imagined returns through a learned world model is fast, because the model gives a first-order policy gradient. We ask how much of that gradient holds in the simulator. On a tracker for the Unitree G1, the $0.5\%$ of imagined rollouts with the largest gradients carry $22\%$ of the summed gradient norm, yet neither a second rollout from the same state nor the simulator confirms them. When the actions are moved along the model's gradient, the simulator returns 94% of the predicted change in return where the gradient norm is below the batch median, 48% between 3 and 10 times the median, and 1% above 30 times; the part of a gradient that either check confirms stops growing at a few times the median. We therefore cap each rollout's action-gradient norm at 10 times the batch median, draw imagination starts in proportion to their predicted gradient norm so that the cap removes less, and reset episodes where the world model and critic predict the lowest return. Trained on 223 hours of motion and tested on 353 motions that no actor performed in training, the method raises the normalized return of SuperMimic, the baseline it builds on, from 0.953 to 0.967 and the lowest $1\%$ of test clips from 0.65 to 0.76, halves the test clips that fall persistently, from 15--18 to 7--10, and reaches the baseline's final return in 40% of the baseline's iterations and half its training time. On LAFAN1, trained and evaluated on the same clips as prior work, it reaches 0.935 against 0.906.

</details>

---

### [[20_Research/Papers/机器人/Adesktop_learning_factory_for_smart_and_resilient_manufacturing_based_on_digital_twin_and_AI|Adesktop learning factory for smart and resilient manufacturing based on digital twin and AI]]

![[assets/2611.27579_figure.png|800]]

- **arXiv**: [2611.27579](https://arxiv.org/abs/2611.27579)
- **PDF**: https://arxiv.org/pdf/2611.27579
- **详细分析**: [[20_Research/Papers/机器人/Adesktop_learning_factory_for_smart_and_resilient_manufacturing_based_on_digital_twin_and_AI|Adesktop learning factory for smart and resilient manufacturing based on digital twin and AI]]
- **作者**: Wenxuan Hu, Zhuoxuan Cao, Achraf El Messaoudi, Peilin Li, Zhiguo Zeng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Adesktop learning factory for smart and resilient manufacturing based on digital twin and AI》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning factories have been increasingly applied in engineering research and education. In this paper, we develop a small-scale, low-cost, fully open-sourced learning factory that leverages AI and digital twins to demonstrate smart and resilient manufacturing. The learning factory consists of an AGV, three robots, two conveyors and their digital twins. Three typical use cases are designed to demonstrate the capabilities of the learning factory, i.e., material sorting through computer vision-based robot control, coordinating AGV, robots and conveyors for assembly, and digital twin-driven predictive maintenance. The results show that the developed learning factory can adequately support the teaching and research activities on digital twins and AI on manufacturing. Its fully open-source architecture and relatively low deployment cost make it an ideal solution for universities and research institutions.

</details>

---

### [[20_Research/Papers/大模型/S-BFM_A_Behavioral_Foundation_Model_for_Humanoid_Control_from_Sparse_Spatiotemporal_Goals|S-BFM: A Behavioral Foundation Model for Humanoid Control from Sparse Spatiotemporal Goals]]

![[assets/2611.27552_figure.png|800]]

- **arXiv**: [2611.27552](https://arxiv.org/abs/2611.27552)
- **PDF**: https://arxiv.org/pdf/2611.27552
- **详细分析**: [[20_Research/Papers/大模型/S-BFM_A_Behavioral_Foundation_Model_for_Humanoid_Control_from_Sparse_Spatiotemporal_Goals|S-BFM: A Behavioral Foundation Model for Humanoid Control from Sparse Spatiotemporal Goals]]
- **作者**: Kun Yang, Xuanyu Chen, Jing Tan, Yanjing Liu, Yubo Zhao, Renjing Xu, Addison Lin Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.5，大模型 0.4，机器人 1.3）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《S-BFM: A Behavioral Foundation Model for Humanoid Control from Sparse Spatiotemporal Goals》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose whole-body trackers can execute diverse humanoid motions, but they require dense reference trajectories. However, tasks usually specify only where, in which posture, and when the robot should arrive, leaving the motion in between to a separate planner. Inspired by human motor coordination, our key idea is that a low-level controller can organize the intervening motion and its pace by itself from sparse goals with arrival times. In this paper, we propose S-BFM, a novel behavioral foundation model superior in its autonomy: it generates whole-body transitions from target postures, poses, and arrival times alone. Specifically, we first introduce Spatial Grounding, which adds world-frame position and heading to a forward-backward behavior representation through spatial reconstruction. Then, Time-Conditioned Distillation is designed to learn transitions and pace from real motion through closed-loop imitation of a dense-reference teacher. Lastly, Generative Fine-Tuning is introduced to broaden the covered distances and arrival times with a distilled motion generator. In simulation, S-BFM lowers global joint-position error by over 32% relative to the best baseline under fixed and mixed horizons, and raises fixed-goal reach from 43.5% to 74.6% while cutting terminal position error from 1.67 to 0.26 m. We further deploy S-BFM on the full-size AGIBOT A3 humanoid. Sparse spatiotemporal goals thus suffice for natural, well-timed whole-body motion.

</details>

---

### [[20_Research/Papers/机器人/Where_Delay_Compensation_Belongs_in_a_Decentralized_Mean-Field-Game_Swarm_with_a_Control-Barrier_Safety_Filter|Where Delay Compensation Belongs in a Decentralized Mean-Field-Game Swarm with a Control-Barrier Safety Filter]]

![[assets/2611.27540_first_page.png|800]]

- **arXiv**: [2611.27540](https://arxiv.org/abs/2611.27540)
- **PDF**: https://arxiv.org/pdf/2611.27540
- **详细分析**: [[20_Research/Papers/机器人/Where_Delay_Compensation_Belongs_in_a_Decentralized_Mean-Field-Game_Swarm_with_a_Control-Barrier_Safety_Filter|Where Delay Compensation Belongs in a Decentralized Mean-Field-Game Swarm with a Control-Barrier Safety Filter]]
- **作者**: Jan Mikołajczyk, Igor Rostkowski, Bartosz Ogórkiewicz, Szymon Skierski, Sylwia Opat, Wojciech Rybak, Mikołaj Sczogiel, Radosław Pałys, Jan Gogulski, Bartosz Kościołek, Andrzej Pijanowski, Szymon Kowalski...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Where Delay Compensation Belongs in a Decentralized Mean-Field-Game Swarm with a Control-Barrier Safety Filter》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large robot teams are often run as a plan-then-execute stack. We study a decentralized instance for drone swarms, a mean-field-game (MFG) routing field with a per-agent control-barrier-function (CBF) safety filter, when communication is limited by a shared TDMA channel. Neighbors are known only through noisy range and bearing measurements exchanged in round-robin slots, so the frame, and with it the age of every estimate, grows with swarm size. In simulation this delay reaches both layers but breaks only the safety layer. Without delay, swarms of up to 100 agents do not collide, even with each measurement's noise held for a whole frame; with it, stale estimates at the CBF cause collisions beyond a frame period of 125 to 175 ms, or 75 to 100 ms at 100 agents with held noise, and swarm size sets where that limit lies and how steeply collisions rise. At the MFG, staleness makes the local density noisier without biasing it, and throughput drops by at most a tenth. We then compensate with lightweight on-board predictors, from constant-velocity fits to a small learned network, that estimate each neighbor's position from its last broadcasts. A layer-split experiment shows where prediction is needed: at the CBF it restores safety and extends the tolerated frame period by 1.4 to 1.7 times with an untrained constant-velocity fit and about 2.3 with the learned network when the noise is redrawn each step; with noise held for a frame the two extend it about equally, while at the MFG it only refines the congestion correction. A constant wider safety margin, the simplest alternative, makes collisions more frequent in a bottleneck. With the routing solved offline, that layer is robust to the delay because it sees neighbors only through a crowd average; compensation belongs in the safety filter, switched on only above the uncompensated limit, since below it the predictor's own error adds collisions.

</details>

---

### [[20_Research/Papers/具身智能/Ego4Gen_Generating_Geometry-Grounded_Motion_Tokens_as_a_World-Action_Interface|Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface]]

![[assets/2611.27513_figure.png|800]]

- **arXiv**: [2611.27513](https://arxiv.org/abs/2611.27513)
- **PDF**: https://arxiv.org/pdf/2611.27513
- **详细分析**: [[20_Research/Papers/具身智能/Ego4Gen_Generating_Geometry-Grounded_Motion_Tokens_as_a_World-Action_Interface|Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface]]
- **作者**: Yang Liu, Chao Ye, Jiahao Zhang, Zeyuan Hou, Ruijie Fang, Xiyin Ni, Xinyang Ren, Weiyang Lin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.5（加权：具身智能 0.6，世界模型 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Ego4Gen: Generating Geometry-Grounded Motion Tokens as a World-Action Interface》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Ego4Gen (Egocentric 4D Future Generation), a world model for 4D future generation in robotic manipu lation. Given a single egocentric image and a text prompt, Ego4Gen jointly generates temporally aligned RGB frames, dense point maps, and dense scene flow, explicitly pre dicting the evolution of scene appearance, spatial struc ture, and motion. Built on Cosmos3-Nano, Ego4Gen ex tends the pretrained generative backbone through modality routed LoRA and asymmetric attention, using geometric pseudo-labels from MotionCrafter to learn to predict future geometry and motion latents. These latents can either be decoded into explicit 3D structure and motion or mapped to robot actions. To this end, we also introduce FlowIn verse, a lightweight inverse dynamics network trained in two stages to translate predicted 4D latents into robot ac tions. Experiments show that these geometry and motion latents outperform the evaluated latent-action and video latent baselines in out-of-distribution settings. Closed loop policy evaluations further demonstrate their utility for translating predicted 4D futures into robot control. To gether, these results support geometry-grounded motion to kens as a world-action interface, connecting 4D future gen eration with robotic manipulation and suggesting a path to ward reduced reliance on action-labeled data.

</details>

---

### [[20_Research/Papers/具身智能/NavRSI_Recursive_Harness_Self-Improvement_for_Vision-and-Language_Navigation|NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation]]

![[assets/2611.27499_figure.png|800]]

- **arXiv**: [2611.27499](https://arxiv.org/abs/2611.27499)
- **PDF**: https://arxiv.org/pdf/2611.27499
- **详细分析**: [[20_Research/Papers/具身智能/NavRSI_Recursive_Harness_Self-Improvement_for_Vision-and-Language_Navigation|NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation]]
- **作者**: Guangzhao Dai, Guoxin Lian, Shuo Wang, Shengbin Yue, Qianru Sun, Xiangbo Shu, Bin Zhu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.2，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《NavRSI: Recursive Harness Self-Improvement for Vision-and-Language Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier large language models (LLMs) have enabled vision-and-language navigation (VLN) through direct closed-loop perception and action. However, navigation performance depends strongly on the harness governing LLM-environment interactions, while existing harnesses largely rely on manually designed navigation tools, memory, and agent roles. We introduce NavRSI, a harness-centric recursive self-improvement framework that optimizes the navigation behavior of frozen LLMs through closed-loop experience. In each round, NavRSI iteratively collects navigation trajectories and failure diagnostics, employs a designer agent to rewrite the harness, and retains the revisions that prove effective, while the designer accumulates experience from previous revisions so that the harness and this experience co-evolve. Privileged simulator diagnostics guide only the designer and remain inaccessible to the navigating LLM, enabling deployment with a single RGB camera and primitive actions, without task-specific model training or additional navigation tools. Experiments demonstrate consistent improvements across LLMs from four vendors, with 85.64% success rate on the full R2R-CE val-unseen split with GPT-6-Astra, surpassing the previously reported best by 4.13%. Evaluations on RxR-CE, NavRAG-CE, and a real humanoid robot further demonstrate its generalizability.

</details>

---

### [[20_Research/Papers/具身智能/GenPA_Image_Generators_as_Efficient_Robot_Policies|GenPA: Image Generators as Efficient Robot Policies]]

![[assets/2611.27446_figure.png|800]]

- **arXiv**: [2611.27446](https://arxiv.org/abs/2611.27446)
- **PDF**: https://arxiv.org/pdf/2611.27446
- **详细分析**: [[20_Research/Papers/具身智能/GenPA_Image_Generators_as_Efficient_Robot_Policies|GenPA: Image Generators as Efficient Robot Policies]]
- **作者**: Zian Deng, Tianyi Zhang, Zilong Zheng, Ziyu Liu, Tao Zhang, Yao Lyu, Shengbo Eben Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GenPA: Image Generators as Efficient Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained visual generation models have shown great promise in robotic manipulation. However, a representative line of work still treats future visual prediction as the central link between visual generative pretraining and action learning, retaining it as a training objective even when future scenes are no longer generated at inference time. We argue that the instruction-following, spatial understanding, and visual imagination capabilities acquired through image generation pretraining can support control without future visual prediction: image generation models themselves can be directly adapted into powerful action learners. Building on this perspective, we propose GenPA, which fine-tunes an image generation backbone with a lightweight 19M-parameter action regression adapter and reuses its native generative objective for perception co-training. The native image-editing interface accommodates different visual targets without task-specific perception heads, enabling comparisons of current-scene perception, future prediction, and their combinations within a common policy architecture. At deployment, GenPA requires only a single backbone forward pass and action regression, without visual generation or iterative action denoising. Without additional large-scale robot-data pretraining, GenPA demonstrates strong control performance and robustness to perturbations across simulation benchmarks (99.10% success on LIBERO and 83.79% on LIBERO-Plus) and real-world manipulation tasks. Under compiled inference, GenPA takes 20.9 ms per action chunk on a single H100 GPU, achieving 1.7-3.4x speedups over strong VLA and WAM baselines. Our latency analysis further highlights architectural advantages of visual generation backbones for efficient robot control. Ablations across visual tasks and their combinations identify current-depth supervision as a simple, effective training recipe.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Future_Views_Exploring_Future-State_World_Models_for_Vision-Language_Navigation|Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation]]

![[assets/2611.27418_figure.png|800]]

- **arXiv**: [2611.27418](https://arxiv.org/abs/2611.27418)
- **PDF**: https://arxiv.org/pdf/2611.27418
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Future_Views_Exploring_Future-State_World_Models_for_Vision-Language_Navigation|Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation]]
- **作者**: Kangyi Wu, Pengna Li, Yucheng Wang, Yance Fang, Xihan Ma, Zhizhong Su, Yang Wu, Ye Deng, Jinjun Wang, Jianyi Liu
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.6，大模型 0.2，世界模型 0.8，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Beyond Future Views: Exploring Future-State World Models for Vision-Language Navigation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Navigation(VLN) requires an embodied agent to follow language instructions through unseen 3D environments, where the target spaces often lie beyond the current observation. Navigation world models address this challenge by predicting future views either as pixels or latent representations, providing valuable look-ahead information for action decision. Both paradigms define the future primarily through what the agent may observe, raising a fundamental question: is predicting future views the ultimate form to represent the future for VLN? Cognitive studies show that the human hippocampus prospectively represents both future goals and intervening locations along planned routes. Inspired by this predictive-map view, we organize the navigation-relevant future around goal-directed spatial states and route structure. We instantiate this perspective with two complementary abstractions: a short-horizon waypoint that specifies the next local state to reach, and a mid-horizon corridor that captures the spatial support of the upcoming route. Based on this design, we propose FS-Nav, a future-state world modeling framework that predicts waypoint-corridor states from spatial memory and language instructions, and communicates them to a VLM navigator through top-down and first-person interfaces. Experiments on standard VLN benchmarks demonstrate that FS-Nav achieves state-of-the-art performance. This highlights navigation-relevant future-state modeling as a promising direction for representing the future in VLN.

</details>

---

### [[20_Research/Papers/强化学习/AnyBodyCodec_A_Shared_Native_Interface_for_Body-Model_Conversion,_Extension,_and_Humanoid_Control|AnyBodyCodec: A Shared Native Interface for Body-Model Conversion, Extension, and Humanoid Control]]

![[assets/2611.27397_figure.png|800]]

- **arXiv**: [2611.27397](https://arxiv.org/abs/2611.27397)
- **PDF**: https://arxiv.org/pdf/2611.27397
- **详细分析**: [[20_Research/Papers/强化学习/AnyBodyCodec_A_Shared_Native_Interface_for_Body-Model_Conversion,_Extension,_and_Humanoid_Control|AnyBodyCodec: A Shared Native Interface for Body-Model Conversion, Extension, and Humanoid Control]]
- **作者**: Qianxing Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《AnyBodyCodec: A Shared Native Interface for Body-Model Conversion, Extension, and Humanoid Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Parametric body models expose incompatible pose and shape controls, tying humanoid policies to particular input formats. AnyBodyCodec learns a shared representation through native conversion, then reuses it for new body models and control with its core frozen. Encoders map MHR, SMPL-X, and SOMA to aligned slots; native decoders recover target controls. The 1.090M-parameter converter covers nine routes and reaches 16.801 mm input-reference MPJPE across six cross routes: the 2.887M Transformer bank reaches 16.390 mm and its parameter-matched version 18.866 mm. Three measured routes take 7.43-7.67 ms on an RTX 4090. Adding ANNY shows that comparable conversion accuracy can accompany different action consistency under one frozen controller. Under a matched PPO budget, aligned slots support 60.78% full-action success across three formats. Separate 160-hour training reaches 66.10% source-weighted validation success, and the controller is deployed qualitatively on a physical G1 through three visual front ends. Together, these results establish reuse through both native geometric fidelity and downstream policy compatibility.

</details>

---

### [[20_Research/Papers/机器人/GeoSDF-Diff_Geometry-Aware_Diffusion_Planning_for_Collision-Free_Trajectories|GeoSDF-Diff: Geometry-Aware Diffusion Planning for Collision-Free Trajectories]]

![[assets/2611.27373_figure.png|800]]

- **arXiv**: [2611.27373](https://arxiv.org/abs/2611.27373)
- **PDF**: https://arxiv.org/pdf/2611.27373
- **详细分析**: [[20_Research/Papers/机器人/GeoSDF-Diff_Geometry-Aware_Diffusion_Planning_for_Collision-Free_Trajectories|GeoSDF-Diff: Geometry-Aware Diffusion Planning for Collision-Free Trajectories]]
- **作者**: Yueming Li, Zhanjiang Yang, Yang Shen, Meng Li, Lijun Sun
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《GeoSDF-Diff: Geometry-Aware Diffusion Planning for Collision-Free Trajectories》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion models have recently attracted increasing attention in motion planning due to their ability to model high-dimensional and multi-modal trajectory distributions. However, existing diffusion-based planners still struggle to reliably satisfy geometric feasibility in unseen cluttered environments with complex obstacle layouts. To address this challenge, we propose GeoSDF-Diff, a geometry-aware diffusion planner that incorporates multi-scale SDF conditioning into trajectory denoising. The key idea is to provide the denoiser with both route-level geometric context and fine local clearance evidence, enabling generated trajectories to better adapt to unseen complex obstacle layouts. Specifically, a Geometric Encoder extracts multi-scale SDF features and injects them into a DiT-X denoiser through cross-attention. We further introduce a trajectory-level training objective that combines SDF clearance, violation emphasis, smoothness, and path-length regularization, so that local infeasibilities are penalized during training rather than corrected only at inference time. Experiments on held-out cluttered environments show that, without post-hoc trajectory repair or sampling-time guidance, GeoSDF-Diff achieves a 65.2% average success rate across diverse test scenarios, outperforming strong diffusion baselines by 25.4% to 28.5%.

</details>

---

### [[20_Research/Papers/机器人/NormFlowSDE_Normalizing_Flows_for_Amortized_Bayesian_State_Estimation|NormFlowSDE: Normalizing Flows for Amortized Bayesian State Estimation]]

![[assets/2611.27362_first_page.png|800]]

- **arXiv**: [2611.27362](https://arxiv.org/abs/2611.27362)
- **PDF**: https://arxiv.org/pdf/2611.27362
- **详细分析**: [[20_Research/Papers/机器人/NormFlowSDE_Normalizing_Flows_for_Amortized_Bayesian_State_Estimation|NormFlowSDE: Normalizing Flows for Amortized Bayesian State Estimation]]
- **作者**: Yi Zhang, Lars Mikelsons
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《NormFlowSDE: Normalizing Flows for Amortized Bayesian State Estimation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bayesian state estimators, such as Kalman filters, estimate states from noisy observations based on dynamical models. However, obtaining accurate models can be challenging when the system involves effects that are difficult to model faithfully, such as friction, impacts, and deformation in contact-rich manipulation. Uncertainty in system parameters, inputs, and disturbances, together with simplified noise models, can further introduce simulation-to-reality mismatch and degrade estimation accuracy. These limitations motivate learning a distribution over state trajectories conditioned on observations and controls without explicitly specifying the underlying physical models. We introduce NormFlowSDE, an amortized Bayesian state estimator that learns a distribution over state trajectories by combining neural stochastic differential equations with conditional normalizing flows. Its key design choice is to utilize the capability of normalizing flows to learn stochastic behavior of variables, while leveraging the continuous-time dynamics of SDEs to model the evolution of states over time. Once trained, the model draws state paths for new measurement sequences without per-sequence optimization. In addition, we connect NormFlowSDE to stochastic continuous-time dynamics by proving weak convergence of a mean-centered, drift-corrected inference scheme to an Itô diffusion under stated assumptions. Finally, we benchmark NormFlowSDE against direct estimators and learned particle filters based on normalizing flows on partially observed dynamical systems, including simulated systems and real-world robot datasets. The results show that NormFlowSDE attains the lowest estimation error with calibrated uncertainty intervals on both robot datasets and filters four times faster than the fastest particle filter on every dataset.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Interaction_Policy_A_Unified_Model_for_Full-Duplex_Human-Robot_Interaction|Embodied Interaction Policy: A Unified Model for Full-Duplex Human-Robot Interaction]]

![[assets/2611.27327_figure.png|800]]

- **arXiv**: [2611.27327](https://arxiv.org/abs/2611.27327)
- **PDF**: https://arxiv.org/pdf/2611.27327
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Interaction_Policy_A_Unified_Model_for_Full-Duplex_Human-Robot_Interaction|Embodied Interaction Policy: A Unified Model for Full-Duplex Human-Robot Interaction]]
- **作者**: Youqiang Gui, Yunfei Liu, Lijian Lin, Ye Zhu, Jianan Wang, Cheng Peng, Yu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Interaction Policy: A Unified Model for Full-Duplex Human-Robot Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time human-robot social interaction requires continuous coordination between speech and physical behavior. Existing systems often separate interaction agents from motion generation, complicating coordination as conversational states change. We propose \textbf{Embodied Interaction Policy (EIP)}, a unified streaming framework that couples an Audio-Interaction expert with a motion expert through layer-wise joint attention. This allows motion generation to directly access the evolving interaction context. A chunk-wise causal mask prevents access to future context, while a vocal token encodes speaking state and the semantic emotion of the response. We construct \textbf{Embodied Interaction Dataset (EI-Data)} from co-speech and dyadic interaction data and train our model in two stages to learn state-adaptive and emotion-conditioned behavior. Combined with the frozen interaction expert, EIP supports continuous robot motion during proactive responses and interruption-aware turn-taking. Quantitative evaluations demonstrate improved motion quality over representative gesture-generation baselines. Compared with a representative cascaded system, EIP achieves higher interaction success and reduces warm-start latency by 64\%. Physical deployment and user studies further demonstrate improved motion naturalness and interaction comfort.

</details>

---

### [[20_Research/Papers/机器人/Frontier_Voltage_Boost_Laplacian_Path_Planning|Frontier Voltage Boost Laplacian Path Planning]]

![[assets/2611.27308_figure.png|800]]

- **arXiv**: [2611.27308](https://arxiv.org/abs/2611.27308)
- **PDF**: https://arxiv.org/pdf/2611.27308
- **详细分析**: [[20_Research/Papers/机器人/Frontier_Voltage_Boost_Laplacian_Path_Planning|Frontier Voltage Boost Laplacian Path Planning]]
- **作者**: Vinay Pritamani, Rishabh Jain, Jack Lowry, Joshua Smith
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Frontier Voltage Boost Laplacian Path Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper introduces Frontier Voltage Boost Laplacian path planning. The method inherits many of the attractive features of earlier Harmonic Potential Field planning methods, including absence of local minima and smooth paths, while improving the original. The piecewise approach we introduce is able to solve larger maps and handle narrow passages more quickly than earlier Harmonic Potential Field methods. After explaining the algorithm, we experimentally characterize its cor- rectness, performance, and path smoothness as a function of map size. Code is available at https://github.com/vpritamani/FrontierVoltageBoostLaplacianPathPlanning

</details>

---

### [[20_Research/Papers/具身智能/ManipScope_A_Diagnostic_Benchmark_for_Instruction_Following_and_Generalization_in_Robotic_Manipulation|ManipScope: A Diagnostic Benchmark for Instruction Following and Generalization in Robotic Manipulation]]

![[assets/2611.27305_figure.png|800]]

- **arXiv**: [2611.27305](https://arxiv.org/abs/2611.27305)
- **PDF**: https://arxiv.org/pdf/2611.27305
- **详细分析**: [[20_Research/Papers/具身智能/ManipScope_A_Diagnostic_Benchmark_for_Instruction_Following_and_Generalization_in_Robotic_Manipulation|ManipScope: A Diagnostic Benchmark for Instruction Following and Generalization in Robotic Manipulation]]
- **作者**: Jiacheng Li, Yaping Li, Congsheng Xu, Qingchen Liu, Haonan Wang, Zhijie Deng, Jiahu Qin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.2，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《ManipScope: A Diagnostic Benchmark for Instruction Following and Generalization in Robotic Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ATOM-Bench, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Completing a manipulation task does not establish that a robot follows the requested goal rather than a familiar routine. ManipScope is an evaluation-only diagnostic benchmark for robotic instruction following under changed task requirements. Built on RoboTwin 2.0's simulation resources, it specifies 48 held-out scenes across six task families with explicit source-task links; policies are trained on unmodified RoboTwin 2.0 demonstrations, and no demonstrations of the scenes are provided, so success requires reusing skills under a changed request rather than fitting supplied examples. Beyond task success, ManipScope provides a chain of diagnostics in which each step tests one explanation of a failure. For twelve policy checkpoints, 84.6% of failures in 13,200 episodes on eleven selection scenes displace a distractor, and gripper records show that failed episodes usually grasp a non-target. When the target is reassigned among the candidates on identical initial states, ten checkpoints follow every instruction on 3.9% of 1,000 states, below the 16% of an instruction-blind chooser, while a GPT-6 agent run as positive control reaches 88%. The failure recurs on unmodified training tasks and is not explained by missing manipulation skills, so success in these scenes largely reflects instruction-independent preferences; two checkpoints trained on the same data nevertheless follow color instructions. In a feasibility test, letting an agent select the target and the policy execute partly restores instruction following. Case studies with future-video and internal-intervention probes further show that forecasts and execution can agree on the wrong target and that action changes need not transfer the goal. Success, consistency, and sensitivity must each be checked against the requested goal.

</details>

---

### [[20_Research/Papers/机器人/HermiteTwin_Bicubic_Hermite_Shell_Digital_Twins_for_Contact-Rich_Deformable_Manipulation|HermiteTwin: Bicubic Hermite Shell Digital Twins for Contact-Rich Deformable Manipulation]]

![[assets/2611.27282_figure.png|800]]

- **arXiv**: [2611.27282](https://arxiv.org/abs/2611.27282)
- **PDF**: https://arxiv.org/pdf/2611.27282
- **详细分析**: [[20_Research/Papers/机器人/HermiteTwin_Bicubic_Hermite_Shell_Digital_Twins_for_Contact-Rich_Deformable_Manipulation|HermiteTwin: Bicubic Hermite Shell Digital Twins for Contact-Rich Deformable Manipulation]]
- **作者**: Kangrui Zhang, Mu Huang, Xing Shen, Tiantian Liu, Bo Ren
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《HermiteTwin: Bicubic Hermite Shell Digital Twins for Contact-Rich Deformable Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GauSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While existing methods for reconstructing deformable object manipulation have made impressive progress, they typically represent a thin object with a single particle set that must serve two purposes at once: modeling bending, and resolving contact with the robot. To bridge this gap, we present HermiteTwin, a framework that reconstructs a physical digital twin of a thin deformable object from multiview video of a robot manipulating it. Our key idea is to represent deformation and contact separately, each at its own resolution. The object is simulated as a bicubic Hermite shell, a coarse grid of $C^1$ elements whose nodal positions and derivatives define a smooth surface with Kirchhoff--Love bending, while the gripper acts through dense samples in material space that are captured, clamped, and released, and whose attachment forces reach the shell through the Hermite basis. This decoupling keeps the physical state compact while contact stays fine-grained. We identify effective material and contact parameters with CMA-ES followed by adjoint-based refinement, and drive a reconstructed Gaussian appearance model with the simulated shell. In experiments on real cloth and foam manipulation, HermiteTwin outperforms the state-of-the-art spring--mass twin across reconstruction, resimulation, and future prediction.

</details>

---

### [[20_Research/Papers/机器人/AELF_Active_Terrain-Aware_UAV_Exploration_Using_a_Lightweight_Framework|AELF: Active Terrain-Aware UAV Exploration Using a Lightweight Framework]]

![[assets/2611.27263_figure.png|800]]

- **arXiv**: [2611.27263](https://arxiv.org/abs/2611.27263)
- **PDF**: https://arxiv.org/pdf/2611.27263
- **详细分析**: [[20_Research/Papers/机器人/AELF_Active_Terrain-Aware_UAV_Exploration_Using_a_Lightweight_Framework|AELF: Active Terrain-Aware UAV Exploration Using a Lightweight Framework]]
- **作者**: Mingyang Li, Xiao Cao, Yi Luo, Yuting Tao, Hongjie Huang, Bowen Xu, Peng Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《AELF: Active Terrain-Aware UAV Exploration Using a Lightweight Framework》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an efficient and robust approach for autonomous aerial exploration in complex environments. Instead of relying on conventional 3D voxel-based maps for exploration, we utilize a lightweight 2.5D map framework that reduces computational overhead while preserving essential topographic information. More importantly, this representation systematically eliminates the blind voxel problem commonly encountered in voxel-based exploration due to occlusions and limited visibility. Unlike previous methods that rely on a fixed altitude scale for exploration, our approach requires no prior height information and actively adapts to terrain elevation changes during exploration. To further enhance exploration efficiency while preserving the generality of 3D exploration, we perform 2D path planning on the 2.5D map framework, which is then lifted to 3D to evaluate the cost between viewpoints by taking into account terrain traversability, thereby reducing frequent altitude changes and enabling smoother exploration. Extensive experiments conducted in both simulated and real-world environments demonstrate the effectiveness and advantages of our approach over existing solutions. Our approach demonstrates fast exploration of over 2000~$\text{m}^2$ of cluttered forest and sloped mountainous terrain with elevation changes of up to 10~m, reaching a maximum speed of 5~m/s in real-world tests.

</details>

---

### [[20_Research/Papers/具身智能/Learning_from_Incomplete_Actions_Interval_Motion_Supervision_for_Vision-Language-Action_Policies|Learning from Incomplete Actions: Interval Motion Supervision for Vision-Language-Action Policies]]

![[assets/2611.27171_figure.png|800]]

- **arXiv**: [2611.27171](https://arxiv.org/abs/2611.27171)
- **PDF**: https://arxiv.org/pdf/2611.27171
- **详细分析**: [[20_Research/Papers/具身智能/Learning_from_Incomplete_Actions_Interval_Motion_Supervision_for_Vision-Language-Action_Policies|Learning from Incomplete Actions: Interval Motion Supervision for Vision-Language-Action Policies]]
- **作者**: Yunpeng Mei, Chenyu Wang, Xiaowen Zhu, Chenbo Xin, Hongjie Cao, Yiyuan Li, Chengye Zhang, YuAn Wang, Gang Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Learning from Incomplete Actions: Interval Motion Supervision for Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual labeling of egocentric demonstrations often leaves contiguous gaps in action supervision. Reliable poses around a gap still provide its net translation and rotation. We use this information to train vision-language-action policies while preserving ordinary flow matching on reliable local actions. A composition objective constrains the aggregate motion of missing-action estimates, combining multiple fixed windows when a gap exceeds the policy horizon. A shared interval branch learns from reliable endpoints and supplies the composition target. On LIBERO with 20% of demonstrations and 70.5% missing actions, the main method achieves 87.9% mean success over three training runs. In one paired comparison with matched observation exposure and training cost, its advantage over masking is 10.5%. On Ego-informed RoboTwin gaps, success is 45.4%, versus 40.3% for masking. On five real-robot tasks, mean success is 59.6%, versus 54.8% for interval flow matching alone and 48.8% for masking.

</details>

---

### [[20_Research/Papers/机器人/Simulation-Based_Testing_of_RCM-Constrained_Robotic_Software_via_Task_Manifolds|Simulation-Based Testing of RCM-Constrained Robotic Software via Task Manifolds]]

![[assets/2611.27144_figure.png|800]]

- **arXiv**: [2611.27144](https://arxiv.org/abs/2611.27144)
- **PDF**: https://arxiv.org/pdf/2611.27144
- **详细分析**: [[20_Research/Papers/机器人/Simulation-Based_Testing_of_RCM-Constrained_Robotic_Software_via_Task_Manifolds|Simulation-Based Testing of RCM-Constrained Robotic Software via Task Manifolds]]
- **作者**: Zhenyu Jiang, Yanlin Li, Rongjie Yan, Rihui Song, Kai Huang
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Simulation-Based Testing of RCM-Constrained Robotic Software via Task Manifolds》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

System-level testing of surgical robots requires generating executable test scenarios that exercise diverse, safety-critical behaviors. However, remote-center-of-motion (RCM) surgical manipulators operate within tightly constrained workspaces governed by coupled task geometry, inverse kinematics, and motor limits. Direct sampling in motor-command or Cartesian spaces frequently wastes testing budgets on physically unfeasible configurations. To address this limitation, we present a manifold-centered testing framework that decouples feasible test-domain construction from downstream test-generation strategies. Candidate inputs are generated directly within this constructed feasible domain and mapped to lower-level joint commands for simulation execution. Offline trajectory safety oracles and a spatial reference grid then evaluate failure yield and coverage. We compare our task-manifold representation against Cartesian XYZ and principal component analysis (PCA) under random testing, systematic traversal, and genetic search strategies. Results demonstrate that the feasible task domain improves test-generation efficiency and enables systematic reference-cell coverage. Crucially, random and genetic search strategies detect a broader spectrum of failure patterns than baseline representations, revealing that complete reference-cell coverage alone does not exhaust intra-cell behavioral dynamics. Furthermore, differential testing between defective and patched controller versions reveals that targeted evolutionary search detects aggregate failure-rate shifts from software repairs. Finally, a cross-platform study on a 7-DoF Kinova Gen3 arm in MoveIt 2 confirms workflow transferability to kinematically redundant manipulators. Together, these findings highlight the necessity of combining feasibility-aware domain modeling with complementary search strategies for systematic testing of robot software.

</details>

---

### [[20_Research/Papers/具身智能/Opto-Electronic_Hybrid_Reinforcement_Learning_Based_on_MZI_for_Robotic_Manipulator_Control|Opto-Electronic Hybrid Reinforcement Learning Based on MZI for Robotic Manipulator Control]]

![[assets/2611.27129_first_page.png|800]]

- **arXiv**: [2611.27129](https://arxiv.org/abs/2611.27129)
- **PDF**: https://arxiv.org/pdf/2611.27129
- **详细分析**: [[20_Research/Papers/具身智能/Opto-Electronic_Hybrid_Reinforcement_Learning_Based_on_MZI_for_Robotic_Manipulator_Control|Opto-Electronic Hybrid Reinforcement Learning Based on MZI for Robotic Manipulator Control]]
- **作者**: Mengting Yu, Shuiying Xiang, Changjian Xie, Yonghang Chen, Haowen Zhao, Xingxing Guo, Zhijian Hao, Yahui Zhang, Yanan Han, Yue Hao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 3.0（加权：具身智能 0.9，强化学习 1，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Opto-Electronic Hybrid Reinforcement Learning Based on MZI for Robotic Manipulator Control》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precise motion control for autonomous robots is a core technical enabler for the large-scale deployment of embodied intelligence. In particular, basic manipulation tasks, such as point-to-point reaching and target grasping with robotic manipulators, impose stringent requirements on control accuracy, real-time response, and energy efficiency for edge deployment. As a prevailing end-to-end control paradigm, reinforcement learning (RL) has demonstrated remarkable capabilities in autonomous learning and generalization for decision-making in continuous action spaces. Nevertheless, constrained by electronic computing architectures, it generally suffers from substantial computing overhead, high inference latency and limited energy efficiency, making low-power edge deployment challenging. Optical computing, benefiting from its high-speed parallelism, offers a promising route to break energy-efficiency bottlenecks; however, research on the integration of optical computing and RL remains at an early stage. In this work, we propose a Mach-Zehnder Interferometer (MZI)-based opto-electronic hybrid RL architecture. We adopted two algorithm structures: Deep Deterministic Policy Gradient combined with Hindsight Experience Replay (DDPG-HER) and Twin Delayed Deep Deterministic Policy Gradient combined with HER (TD3-HER). We implemented the key layer linear computation of the spiking neural network (SNN) Actor on an optical MZI chip for the reaching task of a Franka Emika Panda robotic manipulator. The architecture is evaluated in the PyBullet simulation environment. Experimental results demonstrate that the proposed architecture achieves an energy efficiency of 1.39 TOPS/W and an inference latency of 120ps while maintaining control accuracy, which provide a feasible pathway toward energy-efficient and precise control for robots.

</details>

---

### [[20_Research/Papers/具身智能/BeyondEgo_Learning_to_Act_Beyond_Egocentric_Perception_via_Humanoid_Ego-Exo_Foresight|BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight]]

![[assets/2611.27047_figure.png|800]]

- **arXiv**: [2611.27047](https://arxiv.org/abs/2611.27047)
- **PDF**: https://arxiv.org/pdf/2611.27047
- **详细分析**: [[20_Research/Papers/具身智能/BeyondEgo_Learning_to_Act_Beyond_Egocentric_Perception_via_Humanoid_Ego-Exo_Foresight|BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight]]
- **作者**: Zhaoshan Yang, Chenglei Li, Haoyu Lei, Yutao Zhang, Yuyu Yang, Zhuo Chen, Ling Ding, Zhongxing Ren, Yi Gu, Heyang Zhang, Peng Su, Jin Pan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《BeyondEgo: Learning to Act Beyond Egocentric Perception via Humanoid Ego-Exo Foresight》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation requires coordinating whole-body motion to perform manipulation tasks in complex environments. Yet egocentric vision-language-action (VLA) policies can miss critical body--scene relationships, and action imitation alone provides no explicit supervision for future scene evolution. We propose BeyondEgo to extend VLA perception in space and time. Spatially, we encode a synchronized exocentric view with frozen DINOv3 and concatenate the resulting tokens with egocentric VLM tokens to condition the action expert. Temporally, we use future observations from both views as privileged supervision for a residual adapter on task-conditioned VLM features. A foresight expert regresses DINOv3 representations of both views 0.6s ahead. At deployment, the foresight expert is discarded and the 4.2M-parameter adapter is retained. We also introduce HELM, to our knowledge, the first closed-loop humanoid loco-manipulation benchmark with synchronized egocentric and exocentric views across five whole-body tasks.On HELM, BeyondEgo improves success from 48.0% to 92.0% in distribution and from 23.5% to 65.0% on 200 held-out scenes with layout, asset, material, and lighting shifts. Ablations show that dual-view DINOv3 foresight yields the best transfer results.

</details>

---

### [[20_Research/Papers/具身智能/RoboColiseum_Co-evolution_of_Simulation,_Evaluation,_and_Models|RoboColiseum: Co-evolution of Simulation, Evaluation, and Models]]

![[assets/2611.27042_figure.png|800]]

- **arXiv**: [2611.27042](https://arxiv.org/abs/2611.27042)
- **PDF**: https://arxiv.org/pdf/2611.27042
- **详细分析**: [[20_Research/Papers/具身智能/RoboColiseum_Co-evolution_of_Simulation,_Evaluation,_and_Models|RoboColiseum: Co-evolution of Simulation, Evaluation, and Models]]
- **作者**: Chenghao Yin, Da Huang, Di Yang, Jichao Wang, Junhui Wu, Nanshu Zhao, Tong Ran, Zhijun Li, Gang Zhao, Linting Guo, Rui Feng, Sheng Zhang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboColiseum: Co-evolution of Simulation, Evaluation, and Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, EmbodiedEval, Real2Sim, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation-based evaluation of embodied models requires calibrated interactions, diverse tasks, and explicit execution constraints. We present RoboColiseum, a platform combining system identification, composable physics and rendering, and multidimensional benchmarking. Recorded-command replay characterizes robot dynamics and object interactions, while a shared interface connects rigid and deformable simulation to rendering. Across 22 paired real--simulation robot--task configurations, task scores have a reported Pearson correlation of 0.9686. Eight evaluation tracks span instruction following, spatial reasoning, general manipulation, robustness, dexterous manipulation, precision manipulation, whole-body coordination, and execution across robot embodiments. Budget-aware scoring combines task progress, resource use, and completion rewards. We report 12 selected Season~I policies and all 11 systems on the public Season~II leaderboard, comprising eight Agent systems and three VLA policies. Agent2Act connects language models to robot-control execution; the VLA study uses mixed-task supervised fine-tuning. The results reveal substantial variation across tracks within each evaluation category. RoboColiseum connects simulation development with capability-oriented evaluation and provides a foundation for extending robot interactions and model assessment.

</details>

---

### [[20_Research/Papers/机器人/PonderPounce-WM_When_Does_Predicting_the_Future_Help_Context-Dependent_Robot_Control|PonderPounce-WM: When Does Predicting the Future Help Context-Dependent Robot Control?]]

![[assets/2611.26996_figure.png|800]]

- **arXiv**: [2611.26996](https://arxiv.org/abs/2611.26996)
- **PDF**: https://arxiv.org/pdf/2611.26996
- **详细分析**: [[20_Research/Papers/机器人/PonderPounce-WM_When_Does_Predicting_the_Future_Help_Context-Dependent_Robot_Control|PonderPounce-WM: When Does Predicting the Future Help Context-Dependent Robot Control?]]
- **作者**: Jaeyoon Jung, Suhwan Choi, Yunsung Lee, Youngjae Yu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《PonderPounce-WM: When Does Predicting the Future Help Context-Dependent Robot Control?》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How does future prediction affect context-dependent robot control? We introduce PonderPounce-WM, extending PonderPounce with three future tokens supervised to predict visual-feature changes. Its pretrained MLLM, Ponder, integrates history and demonstrations into continuous cognition for the action model, Pounce. We investigate token ordering and delivery to distinguish predictive supervision from direct future conditioning. On RoboMME, cognition-first ordering with cognition-only delivery improves success from 60.83% to 67.42%. With the same ordering, direct future-token delivery yields 64.00% success. Probes show increased future information in cognition while the tested past-event attributes remain largely decodable. Across four real-robot tasks, PonderPounce-WM achieves 67.44% mean success under asynchronous execution, compared with 60.98% for PonderPounce. These results suggest that future prediction can improve context-dependent control through auxiliary supervision without delivering future tokens to the action model.

</details>

---

### [[20_Research/Papers/具身智能/RoboDyna_A_Benchmark_for_Evaluating_Robotic_Manipulation_under_Physically_Grounded_Dynamics|RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics]]

![[assets/2611.26969_figure.png|800]]

- **arXiv**: [2611.26969](https://arxiv.org/abs/2611.26969)
- **PDF**: https://arxiv.org/pdf/2611.26969
- **详细分析**: [[20_Research/Papers/具身智能/RoboDyna_A_Benchmark_for_Evaluating_Robotic_Manipulation_under_Physically_Grounded_Dynamics|RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics]]
- **作者**: Zhiyuan Li, Rui Heng Yang, Xuan Zhao, Amir Rasouli
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《RoboDyna: A Benchmark for Evaluating Robotic Manipulation under Physically Grounded Dynamics》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ReflexBench, World-in-World, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object manipulation in the dynamic real world requires understanding how the environment functions and evolves, and acting accordingly. Existing benchmarks, however, do not adequately address these needs. Physics-oriented benchmarks evaluate predictive fidelity but not closed-loop action. Dynamic robotic manipulation benchmarks often use simplified, physically implausible object motions, limiting evaluation of reasoning and action under realistic dynamics. Evaluation is also typically synchronized, freezing the environment during inference and making computation time irrelevant to task outcomes. To this end, we propose RoboDyna, a benchmark for evaluating the physical understanding and action capabilities of manipulation policies in dynamic scenes. RoboDyna comprises 20 conceptual dynamic tasks spanning five capability categories, with simple objects and minimal scene clutter, under a two-factor difficulty design, and 10 household tasks that instantiate the same capabilities in visually and semantically richer simulated real-world environments. RoboDyna provides 3,500 expert demonstrations, paired synchronous and asynchronous evaluation protocols, metrics for task success and partial completion, and interactive tools for human baseline evaluation. Evaluating vision-language-action models and a world-action model across 5.4K episodes, we find that all policies achieve success rates below 20%, revealing substantial limitations in dynamic manipulation. The world-action model captures simple physical dynamics but struggles with complex interactions, and its prediction fidelity does not consistently align with task success. Sync-async comparisons show that inference latency flips 5-12% of episode outcomes while changing average success rates by at most 3%. Human baselines substantially outperform all policies under matched conditions. Project page: https://robodyna.github.io/robodyna/

</details>

---

### [[20_Research/Papers/机器人/RoboCap-10k_A_Metrically_Accurate_Egocentric_Dataset_for_Robot_Learning|RoboCap-10k: A Metrically Accurate Egocentric Dataset for Robot Learning]]

![[assets/2611.26916_figure.jpg|800]]

- **arXiv**: [2611.26916](https://arxiv.org/abs/2611.26916)
- **PDF**: https://arxiv.org/pdf/2611.26916
- **详细分析**: [[20_Research/Papers/机器人/RoboCap-10k_A_Metrically_Accurate_Egocentric_Dataset_for_Robot_Learning|RoboCap-10k: A Metrically Accurate Egocentric Dataset for Robot Learning]]
- **作者**: Kheri Hughes, Qasim Ali, Nikash Bhardwaj, Owen Akhibi, Niresh Dravin, Vivek Sharma, Sam Cho, Ethan Lee, Paul Luo, Sunny Yu, Jonathan Victor, Amanda Young...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《RoboCap-10k: A Metrically Accurate Egocentric Dataset for Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HumanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric video is the most scalable source of manipulation data for robot learning, but its difficulty lies in producing high-quality supervision. Existing large corpora lack metric 3D labels or rely on heterogeneous devices, motion-capture labs, or a headset's built-in real-time tracker, whose accuracy is not reported for the released data. We introduce RoboCap-10k: 10,000 curated hours of unscripted manipulation recorded during workers' paid shifts in 11 countries, spanning 18 task families, 200 task types, and 2,000 tasks. Every hour is captured on one device, the RoboCap, a 250 g hat with six synchronized global-shutter cameras and dual IMUs. Online calibration brings every device below 1 px of epipolar error, visual-inertial SLAM yields gravity-aligned 6-DoF head trajectories, and a multi-view hand tracker yields metric cm-precise hand poses. Each episode is annotated with task and sub-task language captions. Project page: https://robocap10k.com

</details>

---

### [[20_Research/Papers/大模型/Staleness_Deadlines_for_Motion_Plans_during_Onboard_Reasoning|Staleness Deadlines for Motion Plans during Onboard Reasoning]]

![[assets/2611.26858_first_page.png|800]]

- **arXiv**: [2611.26858](https://arxiv.org/abs/2611.26858)
- **PDF**: https://arxiv.org/pdf/2611.26858
- **详细分析**: [[20_Research/Papers/大模型/Staleness_Deadlines_for_Motion_Plans_during_Onboard_Reasoning|Staleness Deadlines for Motion Plans during Onboard Reasoning]]
- **作者**: Hassan Iqbal
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Staleness Deadlines for Motion Plans during Onboard Reasoning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language models may enable general autonomy in robot planning, but onboard their reasoning can run for most of a minute while the robot and nearby pedestrians keep moving. The robot must then decide how long to follow a plan that the pending answer may overturn. Here we present staleness deadlines, which hand that decision to the robot's clock. Calibrated prediction regions for pedestrians and deviation tubes for the robot set the deadline. When the language model answers, a graph planner rebuilds the route, which the robot adopts only after it passes the same clearance check against walls and predicted pedestrians. Exact binomial tests determine which prespecified budget-selection policies keep close calls, wrong decisions and late arrivals below their targets at each inference profile. Candidate policies either fix one budget or set each query's budget from how long the robot can continue its plan before it must brake. We study corridor signs that close routes and delivery requests whose destination the language model must infer. In 81,000 simulated missions with recorded Qwen3-4B answers, full reasoning cuts wrong decisions about twentyfold, and tracking until the deadline cuts late arrivals by up to 64%. The robot never collides while it moves, although pedestrians who never yield still walk into the stopped robot in 23% of offline and 32% of live missions. On a Jetson AGX Orin under perception load, short budgets fail the wrong-decision target, and full reasoning the lateness target. Between these extremes, a fixed-budget policy passes for corridor signs and per-query policies pass for deliveries. Live Orin runs match offline replay on all three losses in 24 of the 32 missions where either run records a loss. The deadline turns slower reasoning into measurable mission outcomes, which let designers test how much reasoning each inference profile can support.

</details>

---

### [[20_Research/Papers/强化学习/Search-Informed_MPPI_for_Kinodynamic_Motion_Planning_via_Monte_Carlo_Tree_Expansion|Search-Informed MPPI for Kinodynamic Motion Planning via Monte Carlo Tree Expansion]]

![[assets/2611.26763_figure.png|800]]

- **arXiv**: [2611.26763](https://arxiv.org/abs/2611.26763)
- **PDF**: https://arxiv.org/pdf/2611.26763
- **详细分析**: [[20_Research/Papers/强化学习/Search-Informed_MPPI_for_Kinodynamic_Motion_Planning_via_Monte_Carlo_Tree_Expansion|Search-Informed MPPI for Kinodynamic Motion Planning via Monte Carlo Tree Expansion]]
- **作者**: Ihab S. Mohamed, Lantao Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Search-Informed MPPI for Kinodynamic Motion Planning via Monte Carlo Tree Expansion》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MPNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Kinodynamic motion planning in large-scale, cluttered environments remains challenging, as dynamically feasible, collision-free trajectories must be computed efficiently over long horizons. Monte Carlo Tree Search (MCTS) can strategically explore long-horizon alternatives but faces large branching factors in continuous control spaces and often relies on random default-policy rollouts, whereas Model Predictive Path Integral (MPPI) efficiently optimizes local trajectories yet remains susceptible to obstacle-induced local minima. To overcome these challenges, we propose Search-Informed MPPI (SI-MPPI), a unified framework that embeds MPPI trajectory optimization within MCTS-based tree search. The core concept is to fuse the expansion and default-policy simulation stages of MCTS into a single MPPI expansion stage guided by structured intermediate targets, termed baits. During each expansion, an adaptive bait-handling rule retains geometrically valid baits as local targets for GPU-batched MPPI optimizations that generate dynamically feasible candidate motion segments. Feasibility gating then checks these candidates for collision safety and sufficient progress, and top-$k$ selection admits the lowest-cost accepted candidates as tree edges, yielding sparse, directed tree growth; thereafter, effective sample size (ESS)-guided adaptation warm-starts subsequent expansions, while cost-based backpropagation updates tree statistics. Extensive simulations across four large-scale, cluttered 2D occupancy-grid maps demonstrate that SI-MPPI consistently produces the smallest search trees and smoothest angular control profiles compared with three kinodynamic baselines, while maintaining competitive planning times and path lengths. Ablation results further highlight the importance of GPU batching, adaptive bait handling, and retaining multiple expansion candidates for planning efficiency and robustness.

</details>

---

### [[20_Research/Papers/具身智能/FORTH_Grounding_Tactile_VLA_Execution_via_Forward-Only_Proxy-Control_Pairing|FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing]]

![[assets/2611.26744_figure.png|800]]

- **arXiv**: [2611.26744](https://arxiv.org/abs/2611.26744)
- **PDF**: https://arxiv.org/pdf/2611.26744
- **详细分析**: [[20_Research/Papers/具身智能/FORTH_Grounding_Tactile_VLA_Execution_via_Forward-Only_Proxy-Control_Pairing|FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing]]
- **作者**: Junde Li, Wei-Han Yu, Xiangyi Chu, Yaoxin Li, Jiawei Xu, Ka-Fai Un, Pui-In Mak
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Systems

#### 研究背景与动机

《FORTH: Grounding Tactile VLA Execution via Forward-Only Proxy-Control Pairing》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies are widely credited with force control, operating on the unverified assumption that proxy loss minimization implies physical force grounding. In this work, we demonstrate that this assumption breaks down at three core deployment levels: frozen visual backbones discard contact geometry, downstream losses mask token-level gradient alignment, and discrete indicators trigger optimization collapse. To address these disconnections, we present FORTH, a forward-only measurement harness and execution framework that explicitly pairs the optimization objective at each level with its physical control observable. FORTH incorporates three grounded pillars: a layer-local, forward-only tactile encoder that preserves spatial contact geometry without backpropagation, a token-parallel zeroth-order adapter enabling activation-space updates, and SlipGuard, a continuous tactile verification gate that fires on incipient slip. On an elasto-plastic structural shell, FORTH's closed-loop gate peaks at 29 times lower grip force than a monotone reflex ramp, preventing structural crush where the baseline leaves permanent deformation. Furthermore, FORTH matches state-of-the-art execution performance with a 97.6% average success rate across three evaluated LIBERO suites, while reducing peak activation memory by 7.12 times compared to a backpropagated step on the same backbone. Enhanced perception enables deeper physical intelligence.

</details>

---
