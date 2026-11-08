# cs.AI | Artificial Intelligence | 2026-11-06

#arxiv #ComputerScience

**论文数**: 29

### [[20_Research/Papers/具身智能/Failure_Prediction_and_Classification_in_Vision-Language-Action_Models_Via_Calibrated_Latent_Probing|Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing]]

![[assets/2611.08425_figure.png|800]]

- **arXiv**: [2611.08425](https://arxiv.org/abs/2611.08425)
- **PDF**: https://arxiv.org/pdf/2611.08425
- **详细分析**: [[20_Research/Papers/具身智能/Failure_Prediction_and_Classification_in_Vision-Language-Action_Models_Via_Calibrated_Latent_Probing|Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing]]
- **作者**: Michal P. Podolinsky, Yunhao Yang, Daniel Little, Hong Lu, Rohan Siva, Olin Goudey, Neel P. Bhatt, Matthias Scheutz, Ufuk Topcu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Failure Prediction and Classification in Vision-Language-Action Models Via Calibrated Latent Probing》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SAE-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action models (VLAs) enable general-purpose embodied intelligence, but their performance is brittle under distribution shift, where unanticipated failures can damage equipment or endanger people. Deploying VLAs in real-world systems therefore requires a runtime monitor that is timely, calibrated, and informative while being efficient enough to run on the edge. Existing methods fail to fulfill these requirements. We present VLA-Tug, a lightweight probe over the latent layers of a VLA backbone that improves early failure detection and bounds the missed-detection and false-alarm rates, with minimal inference overhead. We show that supervising on the pre-failure segment of a trajectory increases early failure detection at matched false-positive rates by up to 30% over the strongest learned baseline. Under shift to unseen tasks, the bounds on missed-detection and false-alarm rates remain valid in up to 86% of runs, versus at most 21% for baselines. Unlike existing methods, VLA-Tug predicts the failure mode to enable corrective actions, raising top-3 accuracy on unseen tasks by up to 44% over a majority baseline. VLA-Tug enables real-time monitoring where the well-timed and informative probe supports lightweight steering that improves task success. We release a dataset of 3,180 annotated manipulation episodes to support future work on latent failure detection in VLAs at https://vla-tug.github.io.

</details>

---

### [[20_Research/Papers/强化学习/Learning_a_patient_world_model_for_health_system_simulation_in_intensive_care|Learning a patient world model for health system simulation in intensive care]]

![[assets/2611.08392_figure.png|800]]

- **arXiv**: [2611.08392](https://arxiv.org/abs/2611.08392)
- **PDF**: https://arxiv.org/pdf/2611.08392
- **详细分析**: [[20_Research/Papers/强化学习/Learning_a_patient_world_model_for_health_system_simulation_in_intensive_care|Learning a patient world model for health system simulation in intensive care]]
- **作者**: Yingtai Li, Ruoyan Wang, Yu Li, Shaohua Kevin Zhou
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《Learning a patient world model for health system simulation in intensive care》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing healthcare strategies requires anticipating their clinical and operational consequences before implementation, a task that often relies on health system simulation. Such a simulation necessitates modeling how patient states evolve and generate care demands. However, conventional approaches typically tailor compact state transitions to a single policy question and omit history-dependent dynamics, thus requiring the redefinition of states and transitions when there is a new question that entails different clinical information. We propose to learn a patient world model from longitudinal EHRs using a neural network to provide a shared clinical representation of patient trajectories that can serve simulation questions across scenarios. Taking ICU operations as an example, we train the model on MIMIC-IV, freeze it, and couple its time-queryable predictions to shared ICU calendars, resources, and queues via scenario-specific mappings, so that one model renders admission demand, care tasks, and discharge proposals across simulations evaluating ICU bed capacity, care dispatch, and post-ICU transfer capacity. Experiments show that our model matches Markov and semi-Markov comparators in aggregate occupancy and directional responses to capacity and dispatch policies. It also reproduces policy gains from replayed observed trajectories. For patients entering the same support state from different prior trajectories, the learned representation captures a 24-h recovery difference (-6.4 predicted versus -6.7 observed percentage points), a contrast missed by compact state models, which propagates into distinct simulated care demand, queue burden, and bed use. These results indicate that a learned world model of patient dynamics has the potential to replace question-specific state models, allowing new care policies to be evaluated by reconfiguring the scenario without model rebuilding.

</details>

---

### [[20_Research/Papers/具身智能/MOMASPLAT_Dynamic_Novel-View_Demonstration_Augmentation_for_Mobile_Manipulation|MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation]]

![[assets/2611.08372_figure.png|800]]

- **arXiv**: [2611.08372](https://arxiv.org/abs/2611.08372)
- **PDF**: https://arxiv.org/pdf/2611.08372
- **详细分析**: [[20_Research/Papers/具身智能/MOMASPLAT_Dynamic_Novel-View_Demonstration_Augmentation_for_Mobile_Manipulation|MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation]]
- **作者**: Sateesh Kumar, Arnav Balaji, Arpit Bahety, Skand Peri, Georgios Pavlakos, Roberto Martín-Martín
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MOMASPLAT: Dynamic Novel-View Demonstration Augmentation for Mobile Manipulation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor policies trained through imitation learning are highly sensitive to changes in camera viewpoint. This is particularly problematic for mobile manipulation (MoMa), where robots rarely execute manipulation from the exact same base pose used during demonstration collection due to navigation uncertainty, localization drift, and environmental constraints. Recent approaches use novel-view synthesis (NVS) to augment demonstrations with unseen viewpoints, but they assume static scenes and therefore fail to re-render the manipulated object during the post-contact interaction phase, leaving the most critical parts of the demonstration unaugmented. We present MOMASPLAT, a novel-view demonstration augmentation framework for mobile manipulation that synthesizes full manipulation trajectories from unseen robot base poses, including dynamic object interactions. Our key insight is that standard MoMa data collection naturally provides the multiview observations needed to reconstruct both the static scene and the manipulated object in 3D. MOMASPLAT combines 3D Gaussian Splatting, feed-forward 3D foundation models, and kinematics-based action retargeting to separately reconstruct the scene and manipulated object, render them from novel viewpoints, and generate geometrically consistent synthetic demonstrations paired with transformed actions. We evaluate MOMASPLAT on five real-world mobile manipulation tasks involving both rigid and articulated objects across three scenes, and validate the fidelity of its synthesized demonstrations against ground truth in simulation. MOMASPLAT substantially improves robustness to unseen base poses, more than doubling the average success rate of the strongest baseline and maintaining non-trivial success at large base displacements where all baselines fail, while reducing the need for largescale real-world data collection.

</details>

---

### [[20_Research/Papers/机器人/VisionSIM_Beyond_Idealized_Sensors_-_A_Multi-Modal_Simulator_for_Robot_Perception|VisionSIM: Beyond Idealized Sensors - A Multi-Modal Simulator for Robot Perception]]

![[assets/2611.08368_figure.png|800]]

- **arXiv**: [2611.08368](https://arxiv.org/abs/2611.08368)
- **PDF**: https://arxiv.org/pdf/2611.08368
- **详细分析**: [[20_Research/Papers/机器人/VisionSIM_Beyond_Idealized_Sensors_-_A_Multi-Modal_Simulator_for_Robot_Perception|VisionSIM: Beyond Idealized Sensors - A Multi-Modal Simulator for Robot Perception]]
- **作者**: Sacha Jungerman, Kaustubh Sadekar, Avery Gump, Sriram Narayanan, Shantanu Gupta, Bhuyashi Deka, Srinivasa Narasimhan, Atul Ingle, Mohit Gupta
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《VisionSIM: Beyond Idealized Sensors - A Multi-Modal Simulator for Robot Perception》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic perception increasingly relies on heterogeneous sensor suites combining cameras with emerging modalities (event, SPAD, iToF/dToF, and thermal). Yet existing simulators idealize these sensors, hiding critical modality-specific failure modes that limit real-world deployment. We present VisionSIM, a unified, physically grounded simulation platform that elevates sensor realism to a first-class concern by modeling the raw physical measurement process for diverse conventional and emerging modalities. We expose fine-grained control over physical sensor parameters, reproducing failure modes overlooked by general-purpose simulators: pileup and glare for LiDAR; phase wrapping, saturation, and motion artifacts for iToF; refractory drops for event cameras; and history-dependent emission for thermal cameras. This enables principled cross-modality comparison on identical scenes and trajectories. We release the platform and a large indoor dataset with synchronized raw measurements and rich ground-truth annotations.

</details>

---

### [[20_Research/Papers/具身智能/Learning_the_Task_or_Learning_the_Verifier_Rethinking_Criteria_Exposure_in_Embodied_Self-Improvement|Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement]]

![[assets/2611.08318_figure.png|800]]

- **arXiv**: [2611.08318](https://arxiv.org/abs/2611.08318)
- **PDF**: https://arxiv.org/pdf/2611.08318
- **详细分析**: [[20_Research/Papers/具身智能/Learning_the_Task_or_Learning_the_Verifier_Rethinking_Criteria_Exposure_in_Embodied_Self-Improvement|Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement]]
- **作者**: Wenbo Huang, Jianxin Bi, Shunyu Yang, Ruiyang Si, Rui Ni, Qiang Wang, Shulong Jiang, Yintianrun Zhang, Feixiang Ruan, Kewei Zhang, Ye Huang, Shukai Gong...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning the Task or Learning the Verifier? Rethinking Criteria Exposure in Embodied Self-Improvement》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-improving embodied agents are increasingly being developed and compared on robot simulation benchmarks. Several recent works expose the benchmark's success criteria to the learning agent, a practice we call Criteria Exposure (CE). These criteria, originally written to verify policies trained by imitation learning, often demand more than the corresponding language instructions, so a score from such a verifier may not faithfully reflect whether the instructed task was completed, especially for robot-control programs written by an agent. As embodied coding agents report ever higher benchmark scores, a natural question arises: when a coding agent is exposed to the benchmark's criteria, does it generate code that better performs the instructed task, or code that simply overfits to the verification criteria? We conduct controlled experiments with a self-improving agent with and without CE, and find that with CE the agent quickly produces code with a higher success rate under the given criteria, but this advantage disappears when the criteria are changed slightly without departing from the original instructions. More importantly, the skills the agent develops under CE transfer poorly across tasks. We further propose instruction-faithful criteria and show that they better reflect the performance of agent-generated programs.

</details>

---

### [[20_Research/Papers/具身智能/RM-VLM_From_Natural-Language_Task_Descriptions_to_Vision-Grounded_Reward_Machines|RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines]]

![[assets/2611.08308_first_page.png|800]]

- **arXiv**: [2611.08308](https://arxiv.org/abs/2611.08308)
- **PDF**: https://arxiv.org/pdf/2611.08308
- **详细分析**: [[20_Research/Papers/具身智能/RM-VLM_From_Natural-Language_Task_Descriptions_to_Vision-Grounded_Reward_Machines|RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines]]
- **作者**: Roko Parac, Christos Ziakas, Leo Ardon, Alessandra Russo
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，大模型 0.9，强化学习 0.36，世界模型 0.16，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《RM-VLM: From Natural-Language Task Descriptions to Vision-Grounded Reward Machines》归入 大模型、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward machines (RMs) have been proposed as a reward formulation in reinforcement learning (RL) to capture non-Markovian tasks where credit assignment depends on history. By representing reward functions as automata, RMs expose the task's temporal structure and allow such rewards to be handled within a Markovian framework. However, they assume a labelling function, a proposition-grounding oracle for observations, which must be manually engineered for each environment, limiting their wider applicability. In this work, we address this limitation by proposing RM-VLM, a novel approach in which a large language model (LLM) generates an RM from a natural-language task description, and a vision-language model (VLM) acts as the labelling function, grounding the RM's propositions over image-based observations during RM-guided policy learning. A VLM-based value function estimator is used to assess the agent's progress towards each RM transition and derive a dense reward signal. We evaluate RM-VLM on three domains covering non-Markovian grid-world navigation, robotic manipulation, and 3D object collection. Our experimental results show that RM-VLM consistently achieves higher task success rates than existing VLM-based reward methods across all tested domains.

</details>

---

### [[20_Research/Papers/具身智能/Aligning_Policy_Encoders_with_a_Shape_Teacher|Aligning Policy Encoders with a Shape Teacher]]

![[assets/2611.08275_figure.png|800]]

- **arXiv**: [2611.08275](https://arxiv.org/abs/2611.08275)
- **PDF**: https://arxiv.org/pdf/2611.08275
- **详细分析**: [[20_Research/Papers/具身智能/Aligning_Policy_Encoders_with_a_Shape_Teacher|Aligning Policy Encoders with a Shape Teacher]]
- **作者**: Madelon Bernardy, Mohammad Mahdi Derakhshani, David M Knigge, Riccardo Valperga, Artem Moskalev
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Aligning Policy Encoders with a Shape Teacher》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3D-aware representations can improve robotic manipulation by providing geometric information that is robust to changes in viewpoint, object position, and occlusion. However, using 3D inputs at deployment requires additional sensing and processing, making image-based policies more practical. We ask whether an image-based policy can acquire 3D shape information during training while retaining a purely image-based interface at deployment. We propose shape-teacher alignment, a training-time mechanism that uses a pretrained 3D shape representation as an alignment target for an image-based policy encoder. Specifically, we use Point-MAE features from individual objects as targets for corresponding image patches, transferring geometric structure to the policy without changing its deployment inputs or architecture. On LIBERO, shape-teacher alignment produces image representations that are more structured around object shape and corresponding parts, while substantially accelerating policy convergence and improving success rates. For pretrained policies, convergence is accelerated by 4.7x and 5.6x on the Object and Spatial suites, respectively, without requiring the shape teacher or depth input at deployment.

</details>

---

### [[20_Research/Papers/强化学习/Accelerating_Safe_Reinforcement_Learning_with_Massive_Parallelism|Accelerating Safe Reinforcement Learning with Massive Parallelism]]

![[assets/2611.08273_figure.png|800]]

- **arXiv**: [2611.08273](https://arxiv.org/abs/2611.08273)
- **PDF**: https://arxiv.org/pdf/2611.08273
- **详细分析**: [[20_Research/Papers/强化学习/Accelerating_Safe_Reinforcement_Learning_with_Massive_Parallelism|Accelerating Safe Reinforcement Learning with Massive Parallelism]]
- **作者**: Joonyoung Lim, Younghwan Yoo
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Accelerating Safe Reinforcement Learning with Massive Parallelism》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate the problem of scaling safe reinforcement learning (safe RL) to massively parallel training regimes, where a large number of environments are exe- cuted with short rollout horizons. Although this setting improves data throughput and wall-clock efficiency, it creates a mismatch with constrained Markov decision processes (CMDPs), whose safety constraints are defined over full-episode cost returns. We address this mismatch by analyzing staggered environment resets as a phase-mixture distribution over short trajectory segments. This analysis charac- terizes the bias induced by phase coverage and motivates a phase-aggregated cost estimator that reconstructs episode-level cost estimates from short rollout batches. We further incorporate finite-sample uncertainty and distribution mismatch into a constraint-tightening framework, yielding a scalable Safe RL method compatible with on-policy optimization. Using an MJX-based implementation of Safety Gym, our experiments show that the proposed method achieves performance comparable to non-massively parallel implementations while substantially reducing wall-clock training time.

</details>

---

### [[20_Research/Papers/大模型/The_Geometry_of_Simulated_Perspectives_Dissociating_Representation_and_Behaviour_in_a_Multimodal_Language_Model|The Geometry of Simulated Perspectives: Dissociating Representation and Behaviour in a Multimodal Language Model]]

![[assets/2611.08262_figure.png|800]]

- **arXiv**: [2611.08262](https://arxiv.org/abs/2611.08262)
- **PDF**: https://arxiv.org/pdf/2611.08262
- **详细分析**: [[20_Research/Papers/大模型/The_Geometry_of_Simulated_Perspectives_Dissociating_Representation_and_Behaviour_in_a_Multimodal_Language_Model|The Geometry of Simulated Perspectives: Dissociating Representation and Behaviour in a Multimodal Language Model]]
- **作者**: Mathis Immertreu, Fitim Abdullahu, Thomas Kinfe, Claus Metzner, Helmut Grabner, Patrick Krauss, Achim Schilling
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《The Geometry of Simulated Perspectives: Dissociating Representation and Behaviour in a Multimodal Language Model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal language models can simulate different observers, yet it remains unclear how assigned perspectives reshape their internal representations and whether these changes govern their judgements. Here, we investigate the representational geometry of persona-conditioned visual interestingness in Qwen3-VL-8B-Instruct. Across 100 images and 53 prompting conditions, we systematically vary persona content and the linguistic framing used to introduce it, while recording behavioural ratings and layer-wise hidden states. We observe a systematic reorganisation of representational geometry across processing depth: early layers primarily encode image identity, whereas persona-specific structures emerge in later layers. Strikingly, prompt framing reshapes internal representations more strongly than persona identity, whereas persona content has a greater impact on behavioural judgements. This dissociation is further illustrated by minimal identity statements that alter representations even without changing responses. These findings demonstrate that representational distance does not necessarily reflect behavioural relevance. More broadly, they reveal how simulated perspectives emerge as distinct structures within the representational space of artificial cognitive systems, highlighting a fundamental distinction between the geometry of internal representations and their functional consequences.

</details>

---

### [[20_Research/Papers/大模型/PCBRouteAgent_How_Close_Are_LLM_Agents_to_Becoming_PCB_Routing_Engineers|PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?]]

![[assets/2611.08175_figure.png|800]]

- **arXiv**: [2611.08175](https://arxiv.org/abs/2611.08175)
- **PDF**: https://arxiv.org/pdf/2611.08175
- **详细分析**: [[20_Research/Papers/大模型/PCBRouteAgent_How_Close_Are_LLM_Agents_to_Becoming_PCB_Routing_Engineers|PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?]]
- **作者**: Yue Zhang, Jilei Sun, Liqiang Jing, Yijie Wei, Ruohan Yang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PCBRouteAgent: How Close Are LLM Agents to Becoming PCB Routing Engineers?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FanoutNet, PCB-Bench, PCBWorld, PCBWorld-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automating printed circuit board (PCB) routing requires coordinating board-level connectivity decisions with geometric execution under strict design rules. Although recent agents can interact with native routing tools, reliable routing on complex boards remains challenging. We present PCBRouteAgent, a multimodal PCB routing agent inspired by how human engineers coordinate global strategy with local execution. A Global Routing Planner combines board images and structured electrical and geometric information to specify connection topology, routing order, corridors, and layer transitions. A Detailed Routing Executor realizes these guides through KiCad's native routing engine and performs bounded local recovery. Unresolved failures are returned as structured feedback, enabling targeted guide revisions while preserving accepted routes. We evaluate PCBRouteAgent on 247 synthetic and real-world boards from four PCBWorld-Bench test splits. It achieves clean-pass rates of 100%, 94.9%, 100%, and 40% on D2, D3-A, D3-B, and D3-C, respectively. On the three real-world subsets, PCBRouteAgent outperforms the best evaluated baseline in clean-pass rate by 13.9, 36, and 10 percentage points, respectively.

</details>

---

### [[20_Research/Papers/大模型/A_Generative_Foundation_Model_for_Multimodal_Tokamak_Tasks|A Generative Foundation Model for Multimodal Tokamak Tasks]]

![[assets/2611.08153_figure.png|800]]

- **arXiv**: [2611.08153](https://arxiv.org/abs/2611.08153)
- **PDF**: https://arxiv.org/pdf/2611.08153
- **详细分析**: [[20_Research/Papers/大模型/A_Generative_Foundation_Model_for_Multimodal_Tokamak_Tasks|A Generative Foundation Model for Multimodal Tokamak Tasks]]
- **作者**: Yingshuai Ji, Haodong Feng, Guohong Deng, Gelin Bian, Yue Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《A Generative Foundation Model for Multimodal Tokamak Tasks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tokamak experiments record diverse measurements, including waveforms, profiles, fields, and scalars, which are used to reconstruct the plasma, forecast its evolution, recover associated control signals, and estimate disruption risk. Most models are built separately for one task and a fixed set of inputs and outputs, and each relies on a prescribed subset of diagnostics rather than structuring the full multimodal observation set to extract global, cross-signal information about the discharge. These limitations motivate a reusable foundation model that adapts to each task's input-output schema and models heterogeneous target signals jointly, rather than retraining a separate model for every configuration. In this work, we extend the TokaMark benchmark with two groups of tasks for actuator action inversion and disruption prediction, yielding 20 MAST tasks in six groups with explicit schemas and evaluation protocols. Then, we introduce GenToka, a generative tokamak foundation model that jointly generates schema-selected targets through a shared conditional diffusion Transformer, with signal-specific codecs preserving native time series, profiles, fields, and scalars; foundation pretraining and task-specific adaptation transfer cross-signal structure across all six groups. Evaluation on MAST measurements shows that GenToka reduces macro-average normalized root mean squared error relative to TokaMind by 4.7% on Groups 1-4 and by 17.7% on Group 5, and improves macro-average window-level F1 on Group 6 by 8.4% at a common validation-selected threshold. GenToka provides a reusable, generative, and multimodal pathway for experimental tokamaks, linking plasma-state reconstruction, actuator inference, and disruption warning from shared measurements to support more integrated, data-driven fusion plasma prediction and control research.

</details>

---

### [[20_Research/Papers/大模型/NutriVisRAG_Multimodal_Exemplar_Grounding_for_Nutrient_Estimation_with_Vision-Language_Models|NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models]]

![[assets/2611.08054_figure.png|800]]

- **arXiv**: [2611.08054](https://arxiv.org/abs/2611.08054)
- **PDF**: https://arxiv.org/pdf/2611.08054
- **详细分析**: [[20_Research/Papers/大模型/NutriVisRAG_Multimodal_Exemplar_Grounding_for_Nutrient_Estimation_with_Vision-Language_Models|NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models]]
- **作者**: Lubnaa Abdur Rahman, Ioannis Papathanail, Maria Panagiotou, Nefeli Dimitropoulou, Margret Harðardóttir, Elisabeth J. den Brok, Bastiaan E. de Galan, Stavroula Georgia Mougiakakou
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《NutriVisRAG: Multimodal Exemplar Grounding for Nutrient Estimation with Vision-Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diet is a major determinant of health, yet accurate dietary assessment from free-living meal images remains challenging. Existing retrieval-based Vision-Language Model (VLM) approaches to nutrient estimation typically rely on textual food representations, while, to our knowledge, direct grounding on visually similar annotated meals has not been investigated. We present NutriVisRAG, a retrieval-augmented generation framework that uses a vision encoder to retrieve similar meals with known nutritional annotations and provide them as multimodal in-context exemplars for VLM nutrient estimation at inference time, without task-specific fine-tuning. We evaluate NutriVisRAG across four datasets, four VLMs, three retrieval encoders, and two prompting strategies, including free-living meals from adults with insulin-treated diabetes, where carbohydrate estimates are compared against two dietitians' annotations. Across all 96 configurations (4 datasets x 4 VLMs x 3 retrieval encoders x 2 prompting strategies), NutriVisRAG reduced the primary estimation error in 56, with improvements more frequent under whole-meal (35/48) than per-item prompting (21/48). Across the evaluated configurations, the lowest NutriVisRAG error was below the best Vanilla error in 13 of 16 VLM--dataset pairs. For GPT-5.4-mini, under whole-meal prompting, the best-performing retrieval encoder for each dataset reduced the primary error on all four datasets relative to Vanilla, with reductions of 1.7--35.7%. Overall, our results show that grounding in multimodal exemplars comprising images and respective annotations can improve nutrient estimation at inference time without task-specific fine-tuning, although the benefits remain configuration-dependent.

</details>

---

### [[20_Research/Papers/大模型/AttnSR_Attention_Step_Reward_for_Long-Horizon_Agentic_RL|AttnSR: Attention Step Reward for Long-Horizon Agentic RL]]

![[assets/2611.07932_figure.png|800]]

- **arXiv**: [2611.07932](https://arxiv.org/abs/2611.07932)
- **PDF**: https://arxiv.org/pdf/2611.07932
- **详细分析**: [[20_Research/Papers/大模型/AttnSR_Attention_Step_Reward_for_Long-Horizon_Agentic_RL|AttnSR: Attention Step Reward for Long-Horizon Agentic RL]]
- **作者**: Mengsong Wu, Tianchen Zhou, Zhaochen Su, Zhenhua Liu, Zhe Cui, Aimin Zhou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.2，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AttnSR: Attention Step Reward for Long-Horizon Agentic RL》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents make multi-step decisions, yet outcome-reward-only reinforcement learning provides little direct supervision for individual steps. We introduce AttnSR, a step-level reward augmentation method that derives reward allocations from policy attention extracted during training replay, without a separately trained reward model or additional rollouts. AttnSR traces backward through the policy model attention graph to estimate the relevance of earlier steps to the final response. The terminal step, measured relative to a running baseline, determines whether these rewards reinforce or penalize the selected steps. In a controlled Qwen2.5-7B-Instruct study, AttnSR consistently outperforms the PPO baseline across all evaluated checkpoints on ALFWorld, raising final held-out success from 91.2% to 97.1%. The ablation experiment shows that the benefit depends on how intermediate rewards are assigned, rather than simple accumulation of step rewards over time. AttnSR also improves ScienceWorld at every checkpoint while cutting environment interactions by 29.9%. These results support policy attention as a practical prior for step-level reward allocation in long-horizon agentic RL. Code is available at https://github.com/fairyshine/AttnSR .

</details>

---

### [[20_Research/Papers/大模型/ZeroRAG_Adaptive_Semantic_Peer_Routing_for_Decentralized_Retrieval-Augmented_Generation|ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation]]

![[assets/2611.07928_figure.png|800]]

- **arXiv**: [2611.07928](https://arxiv.org/abs/2611.07928)
- **PDF**: https://arxiv.org/pdf/2611.07928
- **详细分析**: [[20_Research/Papers/大模型/ZeroRAG_Adaptive_Semantic_Peer_Routing_for_Decentralized_Retrieval-Augmented_Generation|ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation]]
- **作者**: Petru Neague, Quinten Stokkink, Martijn de Vos, Rafael Pires, Mathis Randl, Anne-Marie Kermarrec, Johan Pouwelse
- **cs 子类**: cs.AI, cs.DC, cs.IR, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《ZeroRAG: Adaptive Semantic Peer Routing for Decentralized Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PubMedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) is a standard approach to enhance the reliability of large language model (LLM) outputs by retrieving documents relevant to a query and supplying them in the LLM prompt. Today's RAG systems collect, index, and serve these documents from centralized stores. In practice, however, documents are owned by organizations, devices, and individuals who cannot or will not surrender custody of them to a central party, e.g., because of privacy, copyright or regulatory compliance. Existing modern decentralized retrieval techniques either reintroduce a coordinating authority, or rely on a global data structure that requires continuous network-wide coordination (e.g., DHTs). We present ZeroRAG, a decentralized routing layer for document retrieval in RAG that performs semantic query routing across an overlay of peers with- out global data structures or centralized orchestration. Documents remain with the peers that own them, and each peer keeps only lightweight local state: a bounded set of neighbor advertisements and a cache of recently routed queries. Using these, ZeroRAG steers each query through a best-first walk that progressively rewires the overlay toward semantically relevant neighbors, so recall improves over time as the network self-organizes. We evaluate ZeroRAG using three real-world workloads and two decentralized baselines. We find that ZeroRAG outperforms baselines in terms of recall and required network messages, approaches the recall and LLM answer accuracy of a centralized document store, self-heals after catastrophic peer failures, and scales to 100 000 peers.

</details>

---

### [[20_Research/Papers/具身智能/Structure_from_Collision_via_Hypothesis-Space_Reasoning|Structure from Collision via Hypothesis-Space Reasoning]]

![[assets/2611.07900_figure.png|800]]

- **arXiv**: [2611.07900](https://arxiv.org/abs/2611.07900)
- **PDF**: https://arxiv.org/pdf/2611.07900
- **详细分析**: [[20_Research/Papers/具身智能/Structure_from_Collision_via_Hypothesis-Space_Reasoning|Structure from Collision via Hypothesis-Space Reasoning]]
- **作者**: Takuhiro Kaneko
- **cs 子类**: cs.AI, cs.CV, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Structure from Collision via Hypothesis-Space Reasoning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge of the hidden interior structure of an object, including the presence and location of cavities, is essential for predictive simulation, robotic manipulation, and nondestructive inspection. However, such cavities leave no direct signature on the static visible surface, making collision-induced deformation one of the few cues used to infer their presence. Structure from Collision (SfC) addresses this problem by recovering the hidden interior structure of an object from multiview observations of a collision event. SfC is challenging for two reasons: hidden cavities are only indirectly observable through surface motion, and voids correspond to the absence of material, making direct optimization using standard density representations difficult. The density-based SfC baseline inherits both difficulties. Surface-matching gradients do not directly indicate the cavity location, while density gradients can be weak or uninformative inside or near void regions. Therefore, we reformulate SfC as hypothesis-space reasoning, representing hidden cavities as explicit structural hypotheses whose variables encode available structural assumptions rather than relying on implicit density updates. A global stage performs gradient-free optimization over this hypothesis space using forward-only material point method (MPM) simulation. A local stage then refines the selected hypothesis as a Lagrangian particle system through gradient-based optimization using differentiable MPM simulation. On the SfC benchmark, our method improves hidden-structure reconstruction and future prediction over the density-based SfC baseline. Interior-topology stress tests and robustness analyses characterize its scope and limitations. The project page is available at https://www.kecl.ntt.co.jp/people/kaneko.takuhiro/projects/sfc-hypothesis/.

</details>

---

### [[20_Research/Papers/具身智能/Generate-then-Rank_Learning_Symbolic_Goal_Interpretation_for_Embodied_Agents|Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents]]

![[assets/2611.07825_figure.png|800]]

- **arXiv**: [2611.07825](https://arxiv.org/abs/2611.07825)
- **PDF**: https://arxiv.org/pdf/2611.07825
- **详细分析**: [[20_Research/Papers/具身智能/Generate-then-Rank_Learning_Symbolic_Goal_Interpretation_for_Embodied_Agents|Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents]]
- **作者**: Jisen Lei, Huizhi Liang
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.85（加权：具身智能 1.5，大模型 1.05，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Generate-then-Rank: Learning Symbolic Goal Interpretation for Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Goal interpretation is to translate a natural language instruction into a formal symbolic goal that a planner can execute. It is critical for embodied agents because any error here propagates to every downstream planning and action step. Doing it well requires both generating suitable candidates and reliably selecting among them. We present a two-stage generate-then-rank approach to Goal Interpretation in the Embodied Agent Interface (EAI). First, supervised fine-tuning adapts a Large Language Model (LLM) to EAI's output convention. Second, Candidate-Output Ranking from Errors (CORE) learns preferences over complete outputs from the model's own generated alternatives. We conducted experiments on the household scenes of the Embodied Agent Interface Benchmark. Multiple open source LLMs including DeepSeek-V3 chat, DeepSeek-Reasoner, and Qwen2.5-7B and Qwen2.5-72B were evaluated. The proposed method outperformed the baseline models including LLMs with simple prompting, chain-of-thought, and knowledge graph based approaches.

</details>

---

### [[20_Research/Papers/大模型/Who_Should_Know_What_Empirical_Information_Design_for_Multi-Agent_LLM_Economies|Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies]]

![[assets/2611.07667_figure.png|800]]

- **arXiv**: [2611.07667](https://arxiv.org/abs/2611.07667)
- **PDF**: https://arxiv.org/pdf/2611.07667
- **详细分析**: [[20_Research/Papers/大模型/Who_Should_Know_What_Empirical_Information_Design_for_Multi-Agent_LLM_Economies|Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies]]
- **作者**: Mete Erdogan, Mirac Suzgun, Aneesh Pappu, Guowei Xu, Batu El, Andrew A. Schoen, Furong Huang, John P. Dickerson, Mert Pilanci, James Zou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Who Should Know What? Empirical Information Design for Multi-Agent LLM Economies》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The performance of multi-agent LLM systems depends not only on the capabilities of the underlying models but also on information-sharing policies, which govern what information each agent observes and at what level of detail. But does providing AI agents with more detailed information always improve collective outcomes, or can transparency paradoxically degrade efficiency? To investigate this, we introduce empirical information design, an experimental framework that systematically compares disclosure policies across economic markets populated by LLM agents, while holding interaction rules and models fixed. We evaluate ten frontier LLMs in multi-resource trade, bilateral bargaining, and double auctions, using ground-truth utilities to decouple identified opportunities from realized outcomes. We find that finer information disclosure yields highly model-dependent results. In trade, revealing exact valuations rather than ordinal preference rankings reduces realized gains for GPT-6 Sol (from 98% to 91% of maximum) yet increases them for Claude Sonnet 5 (from 72% to 86%). In bargaining, exact information leads Grok 4.7 to produce less balanced agreements, whereas Claude Opus 5.5 divides gains symmetrically. In double auctions, full disclosure inflates price demands, triggering market breakdown and lowering welfare for Gemini 3.1 Pro (97% to 78%), Claude Opus 5.5 (94% to 64%), and Grok 4.7 (97% to 62%). Overall, these results suggest that model selection and information design must be co-optimized, as LLMs vary in how their strategic responses to information impact system objectives.

</details>

---

### [[20_Research/Papers/具身智能/Energy-Aware_Open-Vocabulary_Detection_Scheduling_for_Low-Power_Robotic_Autonomy|Energy-Aware Open-Vocabulary Detection Scheduling for Low-Power Robotic Autonomy]]

![[assets/2611.07663_figure.png|800]]

- **arXiv**: [2611.07663](https://arxiv.org/abs/2611.07663)
- **PDF**: https://arxiv.org/pdf/2611.07663
- **详细分析**: [[20_Research/Papers/具身智能/Energy-Aware_Open-Vocabulary_Detection_Scheduling_for_Low-Power_Robotic_Autonomy|Energy-Aware Open-Vocabulary Detection Scheduling for Low-Power Robotic Autonomy]]
- **作者**: Abdul Basit, Muhammad Shafique
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Energy-Aware Open-Vocabulary Detection Scheduling for Low-Power Robotic Autonomy》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-vocabulary object detection (OVD) lets robots search for run-time object queries, but fixed-rate inference spends embedded compute on low-value frames during idle motion, map revisits, or stable viewpoints. This paper presents an energy-aware OVD scheduler for low-power mobile robots. The scheduler uses odometry, map change, and detector confidence to switch among low-, mid-, and high-power YOLO-World-S modes on a Jetson Orin Nano. We evaluate the energy-quality trade-off on an AgileX LIMO using 40 real navigation trials: two target objects, five placements per target-policy pair, and four perception policies. Across bottle and cup trials, the scheduler records 8/10 mission success compared with 7/10 for each fixed-rate baseline, while reducing mean Jetson input power (a Jetson-side power-draw metric) by 5.2% relative to an 8 Hz high-rate baseline and lowering achieved OVD call rate by 34.0%. It does not minimize mission-window Jetson input energy because longer missions can erase instantaneous power savings. A separate 60 s stationary microbenchmark isolates the perception workload: the scheduler lowers mean power from 8.045 W to 7.301 W and energy from 484.7 J to 438.1 J relative to the 8 Hz baseline. These results support robot-state-aware OVD scheduling as a promising power-management mechanism with competitive task reliability, while showing that mission-window Jetson input energy must be read together with task progress and runtime.

</details>

---

### [[20_Research/Papers/具身智能/Don't_Prompt_Your_Agents._Equip_Them_Skillware_as_a_Modular_Standard_for_Sovereign,_Auditable,_and_Deterministic_Capability_Execution_for_Lo|Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems]]

![[assets/2611.07652_figure.png|800]]

- **arXiv**: [2611.07652](https://arxiv.org/abs/2611.07652)
- **PDF**: https://arxiv.org/pdf/2611.07652
- **详细分析**: [[20_Research/Papers/具身智能/Don't_Prompt_Your_Agents._Equip_Them_Skillware_as_a_Modular_Standard_for_Sovereign,_Auditable,_and_Deterministic_Capability_Execution_for_Lo|Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems]]
- **作者**: Vladimiros Peilivanidis
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.6，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Don't Prompt Your Agents. Equip Them: Skillware as a Modular Standard for Sovereign, Auditable, and Deterministic Capability Execution for Logical Systems》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Skillware-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current autonomous logical systems rely on a fragile assumption: that language models should dynamically write code, guess API payloads, and memorize operational constraints through prompt engineering. In practice, this burns massive context windows, inflates API bills, and produces brittle agents that fail unpredictably in production. In this work, we present Skillware, an open architectural framework and capability registry that formally separates what an agent wants to do from how that task is executed. Instead of prompting models with loose text instructions or markdown files baptized as 'skills', Skillware equips them with modular, versioned software capability bundles. Much like skill hotkeys in video games that execute deterministically under fixed world rules, each bundle combines a typed JSON input contract, deterministic Python code, task directives, bundled datasets, and automated unit tests. In-process adapters translate these capabilities into native tool declarations for any model, from frontier cloud APIs to local open-weight runtimes with zero network latency. Evaluating 23 frontier and open-weight models across 368 benchmark conditions, we show that small local models (3B to 8B parameters) equipped with Skillware consistently outperform unequipped frontier models on complex multi-step workflows. They cut token usage by up to 84.8%, slash inference costs by up to 97.3%, and eliminate parameter errors entirely. True agent reliability does not come from larger models or longer prompts, but from equipping logical systems with verified, deterministic software. Finally, we articulate the trajectory of capability bundles across an invariant continuum of information processing systems: from digital logical systems today, to IoT, drones, and embodied robotics tomorrow, establishing a foundation for auditable, real-time capability execution.

</details>

---

### [[20_Research/Papers/具身智能/GraspBench_Execution-Aware_Cross-Robot_Evaluation_of_6-DoF_Grasp_Generation_in_MuJoCo|GraspBench: Execution-Aware Cross-Robot Evaluation of 6-DoF Grasp Generation in MuJoCo]]

![[assets/2611.07651_figure.jpg|800]]

- **arXiv**: [2611.07651](https://arxiv.org/abs/2611.07651)
- **PDF**: https://arxiv.org/pdf/2611.07651
- **详细分析**: [[20_Research/Papers/具身智能/GraspBench_Execution-Aware_Cross-Robot_Evaluation_of_6-DoF_Grasp_Generation_in_MuJoCo|GraspBench: Execution-Aware Cross-Robot Evaluation of 6-DoF Grasp Generation in MuJoCo]]
- **作者**: Abdul Basit, Bibek Poudel, Muhammad Shafique
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《GraspBench: Execution-Aware Cross-Robot Evaluation of 6-DoF Grasp Generation in MuJoCo》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, Dex-Net, GraspBench, GraspNet, Meta-World, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern 6-DoF grasp generators are often evaluated using grasp scores, dataset-level metrics, or single-robot demonstrations, yet proposal quality alone does not determine whether a grasp is executable by a particular robot. We present GraspBench, a controlled MuJoCo protocol for evaluating complete grasp-generation pipelines after robot-specific inverse-kinematics filtering, motion planning, and fixed approach-close-lift execution. GraspBench evaluates six configured pipelines across four robot embodiments, five diagnostic objects, and a structured tabletop pose grid, yielding 540 scenarios per method and 3,240 method-scenario evaluations in total. Missing outputs are conservatively counted as failures, and success follows the binary lift criterion produced by each method's execution runner. GraspGen achieves the highest overall success rate (73.1%), followed by EconomicGrasp (63.5%), while robot- and object-conditioned analyses reveal substantial variation across embodiments and object geometries. GPG produces the largest native candidate sets but achieves 44.3% success, indicating that proposal volume alone does not guarantee robot-executable grasps. Cluster-aware paired intervals support the principal method differences while not estimating repeated-execution uncertainty. The results characterize complete configured pipelines on fixed scenarios rather than intrinsic model quality or stochastic repeatability, showing that grasping performance depends jointly on the generator, robot embodiment, scene, and execution protocol.

</details>

---

### [[20_Research/Papers/大模型/SKIM_Pruning_Large_Language_Model_Agents_via_Selective_Knowledge_Informed_Masking|SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking]]

![[assets/2611.07558_figure.png|800]]

- **arXiv**: [2611.07558](https://arxiv.org/abs/2611.07558)
- **PDF**: https://arxiv.org/pdf/2611.07558
- **详细分析**: [[20_Research/Papers/大模型/SKIM_Pruning_Large_Language_Model_Agents_via_Selective_Knowledge_Informed_Masking|SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking]]
- **作者**: Moonseok Choi, Jongwon Jeong, Minki Kang, Giung Nam, Juho Lee
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.55（加权：大模型 1.55）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SKIM: Pruning Large Language Model Agents via Selective Knowledge Informed Masking》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents are increasingly deployed under structured generation, where grammar constraints enforce output format at inference time. Whereas existing compression methods target unconstrained generation, we first identify a fundamental mismatch: under structured generation, grammar constraints reduce the model's output distribution to valid tokens, and the logits matter most at the small set of positions that decide the agent's action. Motivated by this finding, we propose SKIM (Selective Knowledge-Informed Masking), the first pruning and distillation framework for LLM agents under structured generation, with both stages guided by token role. SKIM partitions token positions into context, decision, and format categories, and this partition drives two complementary axes: (1) category-aware pruning saliency scores that preserve parameters most relevant for decision positions; and (2) an on-policy distillation objective that aligns student and teacher on valid tokens, paired with category-aware feature matching. We evaluate SKIM on tool-calling benchmarks and within multi-step agent loops, across multiple model scales and sparsity levels. SKIM consistently improves accuracy over baselines, with its superiority becoming most striking in high-sparsity regimes where conventional methods struggle, demonstrating the potential of category-aware compression for deployment-time grammar-constrained agents.

</details>

---

### [[20_Research/Papers/具身智能/Concertina_Embodying_Manipulation_and_Cognition_in_One_Diffusion_Vision-Language_Model|Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model]]

![[assets/2611.07513_figure.png|800]]

- **arXiv**: [2611.07513](https://arxiv.org/abs/2611.07513)
- **PDF**: https://arxiv.org/pdf/2611.07513
- **详细分析**: [[20_Research/Papers/具身智能/Concertina_Embodying_Manipulation_and_Cognition_in_One_Diffusion_Vision-Language_Model|Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model]]
- **作者**: Chengcheng Wang, Wei He, Wenhao Li, Hongguang Li, Kai Han, Jianyuan Guo, Chang Xu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.2，大模型 1，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Concertina: Embodying Manipulation and Cognition in One Diffusion Vision-Language Model》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BlockVLA, Dream-VLA, HybridVLA, MMaDA-VLA, OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most vision-language-action (VLA) policies decouple manipulation from cognition by bolting an external action mechanism onto a vision-language model (VLM)--either quantizing actions into discrete tokens whose errors bear no stable correspondence to physical displacements, or delegating continuous trajectory generation to a separate action expert whose gradients compete with or are blocked from updating the VLM backbone. We argue that manipulation and cognition should instead be embodied in the same model, shifting from a decoupled VLA to an Embodied Vision-Language Model (eVLM). We introduce Concertina, an eVLM that places continuous trajectory representation, blockwise generation, and physical-coordinate supervision directly on the computation and parameter path of a shared diffusion VLM backbone. Each control timestep is encoded as one continuous latent action token in the backbone hidden space, and the shared Transformer reconstructs temporally ordered action blocks via the same corrupt-and-reconstruct operator used for multimodal pretraining. Active action projections account for only 0.21% of parameters in the 4.46B model with zero separate action-generator layers, compared with 16.5%-35.1% dedicated action-expert capacity in representative continuous VLAs. Using our proposed Action Interface Audit, we confirm that cross-time trajectory coupling emerges in the middle and late layers of the shared backbone rather than at the action interfaces. On standard benchmarks, Concertina achieves 98.15% average success on regular LIBERO, 85.9% on the 10,030-task LIBERO-Plus benchmark, and 4.142 average completed chain length on CALVIN ABC-D. Code: https://github.com/lose4578/Concertina Hugging Face: https://huggingface.co/collections/Traly/concertina

</details>

---

### [[20_Research/Papers/强化学习/Permanent_and_Transient_Representations_for_Continual_Reinforcement_Learning|Permanent and Transient Representations for Continual Reinforcement Learning]]

![[assets/2611.07327_figure.png|800]]

- **arXiv**: [2611.07327](https://arxiv.org/abs/2611.07327)
- **PDF**: https://arxiv.org/pdf/2611.07327
- **详细分析**: [[20_Research/Papers/强化学习/Permanent_and_Transient_Representations_for_Continual_Reinforcement_Learning|Permanent and Transient Representations for Continual Reinforcement Learning]]
- **作者**: Nishanth Anand, Doina Precup
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Permanent and Transient Representations for Continual Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual Reinforcement Learning (CRL) agents struggle to adapt to new situations while retaining prior knowledge, leading to a stability-plasticity trade-off. One approach to solving this problem is by using complementary learning systems: one for slow, long-term learning and another for quick, transient adaptation. Anand &amp; Precup (2023) instantiated this idea using permanent and transient value functions, but used the same features in both systems. Intuitively, long-term learning should rely more on parametric representations for broad generalization, while transient learning would be best served by non-parametric representations for situation-specific adaptation. In this paper, we explore this idea both theoretically and empirically. By introducing a novel non-parametric approximation for estimating the transient value function in complex tasks, we demonstrate that our method enables online learning and outperforms competitive baselines on image-based tasks and Craftax-Classic, underscoring the effectiveness of our system-level decomposition.

</details>

---

### [[20_Research/Papers/具身智能/Efficient_Diffusion_Policy_Fine_Tuning_with_Latent_Noise_Representation_Bridging|Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging]]

![[assets/2611.07275_figure.png|800]]

- **arXiv**: [2611.07275](https://arxiv.org/abs/2611.07275)
- **PDF**: https://arxiv.org/pdf/2611.07275
- **详细分析**: [[20_Research/Papers/具身智能/Efficient_Diffusion_Policy_Fine_Tuning_with_Latent_Noise_Representation_Bridging|Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging]]
- **作者**: Yuanchu Liang, Yue Yang, An-Chi He, Hanna Kurniawati
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.7（加权：具身智能 0.6，强化学习 0.4，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Efficient Diffusion Policy Fine Tuning with Latent Noise Representation Bridging》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FineTuneRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pre-trained diffusion and flow policies have emerged as powerful backbones for robotics, yet adapting them to novel data via reinforcement learning (RL) remains computationally expensive, sample inefficient and lacks theoretical guarantees. Prior approaches that fine-tune the initial noise bypass costly backpropagation through time but struggle with the "noise aliasing" problem: there does not exista natural link between the noise space value and the action space value. This paper resolves these challenges by introducing the Latent Noise Linear Markov Decision Process (LNL-MDP). We derive the Bridge Equation for LNL-MDPs which eliminates the noise aliasing problem by aligning values with a shared representation between the noise and the action space. Furthermore, our LNL-MDP fine tuning framework falls under the FineTuneRL theory with near-optimal guarantee. Leveraging these insights, we propose Latent Representation Bridging for Diffusion (LARBRID), an algorithm that efficiently learns the representation to optimize the initial distribution that steers the pre-trained model to act optimally in the environment. It yields up to 2-3$\times$ performance increases on challenging control problems across a diverse suite of robotic locomotion and manipulation tasks. Code can be found at: github.com/Maincode-Research/LARBRID.git.

</details>

---

### [[20_Research/Papers/强化学习/MAC-v2_Long-horizon_model-based_value_expansion_from_pixels|MAC-v2: Long-horizon model-based value expansion from pixels]]

![[assets/2611.07245_first_page.png|800]]

- **arXiv**: [2611.07245](https://arxiv.org/abs/2611.07245)
- **PDF**: https://arxiv.org/pdf/2611.07245
- **详细分析**: [[20_Research/Papers/强化学习/MAC-v2_Long-horizon_model-based_value_expansion_from_pixels|MAC-v2: Long-horizon model-based value expansion from pixels]]
- **作者**: Kwanyoung Park, Sergey Levine
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.56，世界模型 0.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《MAC-v2: Long-horizon model-based value expansion from pixels》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study whether \emph{long-horizon model-based value expansion} can serve as an effective framework in pixel-based offline reinforcement learning (RL). Long-horizon model-based value expansion from pixels is substantially harder than state-based environments, as the agent must learn both the representation and its dynamics, and errors from either can accumulate recursively over imagined trajectories. We introduce MAC-v2, which enables long-horizon model-based expansion from pixels by training a reconstruction-free latent world model with action chunking. By learning representations from prediction and control objectives, MAC-v2 does not need to encode control-irrelevant visual details that can hinder the dynamics prediction. Action chunking further mitigates the prediction error by reducing the number of recursive model predictions required for value expansion. Across diverse visual benchmarks including visual OGBench, MMBench2, Robomimic, and LIBERO-10, MAC-v2 achieves strong performance against model-free and model-based offline RL baselines. Our analyses show that long-horizon model-based value expansion is critical for the performance of MAC-v2, and that both action chunking and latent learning objectives are essential for reliable long-horizon latent imagination.

</details>

---

### [[20_Research/Papers/大模型/More_Agents,_More_Reliable_System-Level_Reliability_of_Multi-Agent_LLMs_under_Operational-Profile_Uncertainty|More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty]]

![[assets/2611.07140_figure.png|800]]

- **arXiv**: [2611.07140](https://arxiv.org/abs/2611.07140)
- **PDF**: https://arxiv.org/pdf/2611.07140
- **详细分析**: [[20_Research/Papers/大模型/More_Agents,_More_Reliable_System-Level_Reliability_of_Multi-Agent_LLMs_under_Operational-Profile_Uncertainty|More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty]]
- **作者**: Burkay Tunçtürk, Koorosh Aslansefat, Yiannis Papadopoulos, Bao Nguyen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《More Agents, More Reliable? System-Level Reliability of Multi-Agent LLMs under Operational-Profile Uncertainty》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teams increasingly build software from cooperating large language model (LLM) agents, often assuming more agents mean more reliability. Yet the usual evidence, average benchmark accuracy, ignores the input mix a deployed system meets and the rule merging the agents' answers. Building on HIP-LLM, a hierarchical imprecise-probability assessment of single LLMs, we propose a framework combining it with a Bayesian network of the system's failure logic for multi-agent systems. Agent failure-probability intervals propagate through this network, where the combining rule can itself fail, into a reliability envelope showing which evidence limits it. In a pipeline extracting regulated chemical-hazard statements, majority voting over three models protected against the weakest but did not clearly exceed the best, and a voter failing on 5\% of demands would largely erase its advantage over the middle model. More agents yield a more defensible reliability claim, not automatically a more reliable system.

</details>

---

### [[20_Research/Papers/强化学习/Finite-Time_Convergence_and_Regret_Guarantees_for_Neural_Reinforcement_Learning_in_POMDPs|Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs]]

![[assets/2611.07069_first_page.png|800]]

- **arXiv**: [2611.07069](https://arxiv.org/abs/2611.07069)
- **PDF**: https://arxiv.org/pdf/2611.07069
- **详细分析**: [[20_Research/Papers/强化学习/Finite-Time_Convergence_and_Regret_Guarantees_for_Neural_Reinforcement_Learning_in_POMDPs|Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs]]
- **作者**: Jingjuan Huang, Zhiyao Zhang, Alvaro Velasquez, Nathaniel D. Bastian, Jia Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Finite-Time Convergence and Regret Guarantees for Neural Reinforcement Learning in POMDPs》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) in Partially Observable Markov Decision Processes (POMDPs) is computationally challenging due to the curse of long-range dependence on history. Fortunately, recent studies have shown that a range of POMDPs that satisfy the filter stability assumption can be well approximated by a superstate Markov Decision Process (MDP) based on a truncated history in a finite-memory window, with a value gap that decays with the window length. However, existing finite-time convergence analyses on such superstate MDP surrogates are either limited to over-simplified linear function approximation or rely on an i.i.d. sampling oracle that is violated by POMDP trajectories, both of which severely limit the applicability of these theoretical results in practice. This motivates us to bridge the gap by investigating RL in POMDPs with nonlinear neural value function approximation. Our main contributions are threefold: i) We first establish a new finite-state MDP point-wise approximation error bound, which lays the foundation for our RL algorithm design and analysis in POMDPs; ii) By applying Temporal-Difference (TD) learning to POMDP-generated superstate transitions and targeting the Bellman fixed point of the superstate MDP, we prove a finite-time critic error bound with nonlinear neural value function approximation; and iii) By combining the neural critic function approximation error bound with the policy mirror descent framework, we obtain a finite-time sublinear regret against the optimal POMDP value. To the best of our knowledge, such a finite-time sublinear regret based on neural function approximation is the first in the literature for finite-memory POMDPs. Our numerical experiments also verify our theoretical results.

</details>

---

### [[20_Research/Papers/强化学习/Cooperative_Multi-Agent_Reinforcement_Learning_via_Epigraph-Form_Guided_Exploration|Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration]]

![[assets/2611.07066_figure.png|800]]

- **arXiv**: [2611.07066](https://arxiv.org/abs/2611.07066)
- **PDF**: https://arxiv.org/pdf/2611.07066
- **详细分析**: [[20_Research/Papers/强化学习/Cooperative_Multi-Agent_Reinforcement_Learning_via_Epigraph-Form_Guided_Exploration|Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration]]
- **作者**: Sungil Son, Hoseong Jung, Dahyun Oh, H. Jin Kim
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Cooperative Multi-Agent Reinforcement Learning via Epigraph-Form Guided Exploration》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discovering cooperative behavior in multi-agent reinforcement learning (MARL) is challenging due to the combinatorial complexity of joint state-action spaces, which hinders the emergence of coordinated behaviors from trial-and-error alone. Intrinsic rewards are often used to aid discovery, but naively combining them with team objectives can distort the learning signal, compromising task performance. In this paper, we propose EFXPLORER, a constrained exploration framework that maximizes exploration objectives subject to a constraint that preserves established task performance. We solve the resulting problem using an epigraph reformulation that introduces adaptive exploration budgets. This approach separates intrinsic rewards from task objectives and regulates exploration through task feasibility. To further encourage diverse and temporally extended exploration, we incorporate a successor distance-based intrinsic reward that captures long-horizon dependencies. Empirically, our method outperforms strong baselines and induces novel cooperative strategies across SMAX, VMAS, and MPE benchmark suites.

</details>

---

### [[20_Research/Papers/强化学习/Resource-Efficient_Reinforcement_Learning_Post-Training_through_Elastic_Expert_Parallelism|Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism]]

![[assets/2611.06984_figure.png|800]]

- **arXiv**: [2611.06984](https://arxiv.org/abs/2611.06984)
- **PDF**: https://arxiv.org/pdf/2611.06984
- **详细分析**: [[20_Research/Papers/强化学习/Resource-Efficient_Reinforcement_Learning_Post-Training_through_Elastic_Expert_Parallelism|Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism]]
- **作者**: Jia Wei, Ziyi Qiu, Yi Xu, Xuehai Qian
- **cs 子类**: cs.AI, cs.DC
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Resource-Efficient Reinforcement Learning Post-Training through Elastic Expert Parallelism》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Full-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning post-training improves the capabilities of large language models, but generating training responses is a major computational bottleneck. In mixture-of-experts models, workers that finish their assigned responses may remain occupied because their experts are still needed by workers processing longer responses. Consequently, approximately one-third of occupied worker time in the baseline occurs after local response generation finishes. Here we present FlexFloor, a system that enables earlier resource release during synchronous response generation while preserving the expert computation required by ongoing responses. FlexFloor jointly adapts response scheduling and the active group of workers. It uses historical response lengths and memory constraints to guide batching and prompt placement, then progressively releases workers while maintaining expert availability and correct communication. Compared with the verl baseline, FlexFloor generates approximately 65.40% more response tokens per unit of occupied computing time and increases response generation throughput by 52.74%, with little observed variation in rollout reward. By making reinforcement learning post-training more efficient, FlexFloor supports faster development and iterative improvement of large language models and AI agents.

</details>

---
