# cs.RO | Robotics | 2026-08-14

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/具身智能/Decoding_Task_Progress_from_VLA_Representations|Decoding Task Progress from VLA Representations]]

![[assets/2608.13474_figure.png|800]]

- **arXiv**: [2608.13474](https://arxiv.org/abs/2608.13474)
- **PDF**: https://arxiv.org/pdf/2608.13474
- **详细分析**: [[20_Research/Papers/具身智能/Decoding_Task_Progress_from_VLA_Representations|Decoding Task Progress from VLA Representations]]
- **作者**: Atiksh Bhardwaj, Edward Weiyi Duan, Prithwish Dan, Wei-Chiu Ma, Preston Culbertson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Decoding Task Progress from VLA Representations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) are moving rapidly towards deployment as general-purpose manipulation policies, but we currently lack basic tools for understanding what these models represent internally or for monitoring them at runtime. Leveraging ideas from mechanistic interpretability, we probe the residual stream of $π_{0.5}$ and find that task progress, the normalized time remaining in a trajectory, is linearly readable from the activations. We find that this signal is present in the pretrained PaliGemma backbone prior to training on any robot-specific data. A single linear probe generalizes to unseen tasks and varies under language counterfactuals when trained on multi-prompt data, but does not enable meaningful steering of the policy. These properties make the signal directly useful for instrumenting deployed VLAs. We use the probe as a simple label-free OOD detector, which detects stalled task progress, and find it competitive with state-of-the-art methods. Our results suggest that VLAs have rich, linearly readable internal representations of semantic quantities like task progress, and that learning to read these signals offers a lightweight, interpretable path toward monitoring deployed visuomotor policies.

</details>

---

### [[20_Research/Papers/机器人/Mind_the_Context_Continual_Learning_of_Socially_Appropriate_Robot_Actions_via_Environmental-Social_Disentanglement|Mind the Context: Continual Learning of Socially Appropriate Robot Actions via Environmental-Social Disentanglement]]

![[assets/2608.13448_figure.png|800]]

- **arXiv**: [2608.13448](https://arxiv.org/abs/2608.13448)
- **PDF**: https://arxiv.org/pdf/2608.13448
- **详细分析**: [[20_Research/Papers/机器人/Mind_the_Context_Continual_Learning_of_Socially_Appropriate_Robot_Actions_via_Environmental-Social_Disentanglement|Mind the Context: Continual Learning of Socially Appropriate Robot Actions via Environmental-Social Disentanglement]]
- **作者**: Rafal Robert Karpinski, Fethiye Irmak Dogan, Nikhil Churamani, Yiming Luo, Maartje M. A. de Graaf, Davide Dell'Anna, Hatice Gunes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Mind the Context: Continual Learning of Socially Appropriate Robot Actions via Environmental-Social Disentanglement》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social robots are expected to operate across diverse environments, where similar arrangements can imply different socially appropriate actions, e.g., starting a conversation may be acceptable in a crowded home but disruptive in an office meeting. Because such norms and environments cannot all be anticipated in advance, robots require continual learning (CL) to adapt from sequential experience while retaining previously acquired knowledge. Prior work has studied CL for generating socially appropriate robot actions, but it has not addressed domain-incremental settings in which the robot incrementally encounters diverse contexts (e.g., living room, meeting room, office, hallway), where both environmental (e.g., whether the space is open or cluttered with furniture) and social cues (e.g., how people or other agents are positioned around the robot) jointly shape the appropriateness of robot actions. We address this gap with the Explicit Disentanglement Dual-Branch (EDD) framework. EDD explicitly separates environmental and social-agent related knowledge and uses replay-based rehearsal to mitigate forgetting while learning the appropriateness of robot actions (e.g., cleaning, serving, starting a conversation) across several indoor domains. Experiments show that EDD outperforms several state-of-the-art baselines, and ablation studies further evaluate different disentanglement strategies and the sensitivity to domain ordering. Our code is publicly available at https://github.com/Cambridge-AFAR/Mind-the-Context.git.

</details>

---

### [[20_Research/Papers/机器人/Capstan-driven_Continuum_Surgical_Robot_Design,_Modeling,_and_Perception|Capstan-driven Continuum Surgical Robot: Design, Modeling, and Perception]]

![[assets/2608.13396_figure.png|800]]

- **arXiv**: [2608.13396](https://arxiv.org/abs/2608.13396)
- **PDF**: https://arxiv.org/pdf/2608.13396
- **详细分析**: [[20_Research/Papers/机器人/Capstan-driven_Continuum_Surgical_Robot_Design,_Modeling,_and_Perception|Capstan-driven Continuum Surgical Robot: Design, Modeling, and Perception]]
- **作者**: Gang Zhang, Yufu Qiu, Junyan Yan, Wenhui Zeng, Wenlong Lu, Shing Shin Cheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Capstan-driven Continuum Surgical Robot: Design, Modeling, and Perception》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Shape and force sensing have long been critical bottlenecks in the development of compact capstan-driven continuum surgical robots, primarily due to the difficulty of obtaining cable tension information within the confined capstan assembly. To overcome these challenges, this paper presents an integrated design-modeling-sensing approach based on the concept of actuation-perception co-design. A compliant element is introduced into the motor mounting bracket of the drive system, enabling micro-deformation under the cable reaction force and thereby allowing real-time cable tension measurement without occupying the compact capstan space. To address the modeling complexity arising from unconventional joint configurations introduced by the spatial cable routing strategy, a parallel computation framework based on a multibody short-thick-beam model is proposed, which captures shear effects in short beam segments and synergistic multi-cable interactions while achieving real-time performance. Building on this framework, stable shape and force sensing is achieved by incorporating a proximal multi-axis force/torque sensor as an additional measurement anchor. Following this design-modeling-sensing framework, capstan-driven continuum surgical robots with single- and dual-segment configurations are developed. Experimental results validate the proposed framework in both single- and dual-segment continuum robots, demonstrating real-time tip pose estimation together with contact force and location perception. By enabling cable tension feedback without compromising the compact capstan architecture, the proposed framework makes integrated perception feasible for capstan-driven continuum surgical robots.

</details>

---

### [[20_Research/Papers/具身智能/FIRE-VLA_Failure-Informed_Self-Evolution_for_Vision-Language-Action_Models_in_Autonomous_Driving|FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving]]

![[assets/2608.13395_figure.png|800]]

- **arXiv**: [2608.13395](https://arxiv.org/abs/2608.13395)
- **PDF**: https://arxiv.org/pdf/2608.13395
- **详细分析**: [[20_Research/Papers/具身智能/FIRE-VLA_Failure-Informed_Self-Evolution_for_Vision-Language-Action_Models_in_Autonomous_Driving|FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving]]
- **作者**: Hao Dou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，强化学习 0.4，机器人 0.3）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《FIRE-VLA: Failure-Informed Self-Evolution for Vision-Language-Action Models in Autonomous Driving》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoVLA, ELF-VLA, FIRE-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning improves autonomous-driving vision-language-action (VLA) models by evaluating trajectories sampled from the current policy. Group relative policy optimization (GRPO) learns from reward differences within each rollout group. When all sampled trajectories are poor, this relative signal can rank failures without identifying behavior outside the failed region. We introduce FIRE-VLA, a failure-informed self-evolution framework that converts such unresolved failures into privileged supervision for the next policy. Low-reward, low-diversity groups trigger self-distillation from a frozen round-start copy of the same model. Teacher and student have the same parameter scale, but only the teacher observes the hidden future trajectory. Supervision follows the student's generated prefix and is restricted to answer tokens, while GRPO remains active for every group. The updated policy supplies the teacher for the next round, allowing the routed failure distribution to change with the policy without requiring a larger external teacher. Starting from the same Qwen2.5-VL-3B SFT checkpoint, the comparison matches student rollout and policy-update counts. On 6,019 examples from 150 held-out nuScenes scenes, FIRE-VLA retains comparable single-sample planning, reduces G=4 mean L2 from 1.848 to 1.500 m, and lowers evaluation-persistent failure prevalence from 13.03% to 11.20%. The reduction in mean error arises mainly from rare severe rollouts rather than uniform improvement across ordinary trajectories.

</details>

---

### [[20_Research/Papers/强化学习/NestDex_Nested_Policy_Learning_with_Copilot_Assisted_Teleoperation_for_Dexterous_Manipulation|NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation]]

![[assets/2608.13362_figure.png|800]]

- **arXiv**: [2608.13362](https://arxiv.org/abs/2608.13362)
- **PDF**: https://arxiv.org/pdf/2608.13362
- **详细分析**: [[20_Research/Papers/强化学习/NestDex_Nested_Policy_Learning_with_Copilot_Assisted_Teleoperation_for_Dexterous_Manipulation|NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation]]
- **作者**: James Zhao, Jinhe Tang, Mingyuan Ba, Weiming Zhi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《NestDex: Nested Policy Learning with Copilot Assisted Teleoperation for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation promises substantially richer robot interaction with the physical world, but learning these behaviours remains constrained by the difficulty of collecting consistent, complete-task demonstrations. Unlike parallel-jaw manipulation, dexterous tasks require the operator to coordinate arm motion with precise, contact-rich finger behaviour throughout the task. We introduce NestDex, a nested policy-learning framework that reduces this burden by using learned hand skills to assist demonstration collection. The operator controls the arm and regulates the active hand skill through a single-DoF clutch, rather than directly specifying the full finger trajectory. The inner hand policy adapts its motion from the latest proprioceptive history, while a vision-language selector activates the appropriate skill for each task stage. The resulting demonstrations train a separate outer visuomotor policy that controls both the arm and hand without the inner policies at deployment. A hand-action variational autoencoder provides compact hand-action targets while retaining arm commands in joint space. Across real-world dexterous manipulation experiments, NestDex improves demonstration reliability and efficiency, and the resulting empirical evaluations support effective autonomous policy learning. Video Demo are available at project website https://aus.bot/research/nestdex.

</details>

---

### [[20_Research/Papers/机器人/Predictive_Relative-Velocity_Steering_for_Safe_Robotic_Manipulator_Teleoperation_in_Dynamic_Environments|Predictive Relative-Velocity Steering for Safe Robotic Manipulator Teleoperation in Dynamic Environments]]

![[assets/2608.13284_figure.png|800]]

- **arXiv**: [2608.13284](https://arxiv.org/abs/2608.13284)
- **PDF**: https://arxiv.org/pdf/2608.13284
- **详细分析**: [[20_Research/Papers/机器人/Predictive_Relative-Velocity_Steering_for_Safe_Robotic_Manipulator_Teleoperation_in_Dynamic_Environments|Predictive Relative-Velocity Steering for Safe Robotic Manipulator Teleoperation in Dynamic Environments]]
- **作者**: Changhao Hu, Zeyi Liu, Songqiao Hu, Shuang Liu, Zihan Meng, Xiao He
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Predictive Relative-Velocity Steering for Safe Robotic Manipulator Teleoperation in Dynamic Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in teleoperation have enabled robotic manipulators to perform dexterous, human-arm-like motions. However, human operators may fail to avoid suddenly appearing obstacles promptly and effectively, particularly under network latency or limited attention, thereby creating safety risks. To address this issue, we propose a lightweight and modular framework for proactive collision avoidance, operating directly at the end-effector velocity-command level. After preprocessing the point cloud, the framework first predicts potential collisions based on time-to-collision (TTC) with integrated overshoot protection, and subsequently rotates the relative-velocity vector using Rodrigues' rotation formula. The deflection changes only the direction of the relative velocity while preserving its magnitude, thereby mitigating the deadlock problem commonly encountered by conventional artificial potential field (APF) methods. The prediction module compensates for point-cloud processing latency introduced by complex teleoperation pipelines, while the lightweight design enables the high-frequency control required for teleoperation. Simulations across diverse scenarios show that the proposed method achieves a higher end-effector collision avoidance rate than the baseline methods. Experiments on a physical robotic system further validate its collision-avoidance effectiveness.

</details>

---

### [[20_Research/Papers/机器人/Manufacturing_Complex_Airtight_Soft_Pneumatic_Actuators_for_Soft_Robotics_Process_Evaluation_and_Optimization|Manufacturing Complex Airtight Soft Pneumatic Actuators for Soft Robotics: Process Evaluation and Optimization]]

![[assets/2608.13233_first_page.png|800]]

- **arXiv**: [2608.13233](https://arxiv.org/abs/2608.13233)
- **PDF**: https://arxiv.org/pdf/2608.13233
- **详细分析**: [[20_Research/Papers/机器人/Manufacturing_Complex_Airtight_Soft_Pneumatic_Actuators_for_Soft_Robotics_Process_Evaluation_and_Optimization|Manufacturing Complex Airtight Soft Pneumatic Actuators for Soft Robotics: Process Evaluation and Optimization]]
- **作者**: Mohammed Abboodi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Manufacturing Complex Airtight Soft Pneumatic Actuators for Soft Robotics: Process Evaluation and Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manufacturing complex soft pneumatic actuators remains challenging because geometric fidelity, compliance, structural integrity, and airtightness must be achieved simultaneously. This study presents a manufacturing-focused evaluation of several fabrication routes for complex pneumatic structures, including heat-shrink forming, silicone casting, powder- and liquid-based additive manufacturing, and fused deposition modeling (FDM). The processes were assessed through process screening, baseline fabrication, failure analysis, and process improvement to distinguish inherent process limitations from correctable manufacturing defects. Heat-shrink forming was limited by geometric conformity, casting by mold accessibility and bonded interfaces, powder-based methods by residual material trapped within enclosed passages, and digital light processing by the material properties and post-processing requirements of the investigated system. FDM provided the most adaptable route because its dominant defects could be progressively reduced through process optimization. The results further showed that airtightness depends not only on nominal wall thickness but also on extrusion-path architecture, while support-free geometry is important when access for internal post-processing is limited. These findings establish a practical design-for-manufacturing approach in which process selection is guided by the compatibility between actuator architecture and manufacturing constraints. The proposed approach provides practical guidance for developing complex, flexible, and airtight soft pneumatic actuators for soft robotic applications

</details>

---

### [[20_Research/Papers/具身智能/S2-HWM_Sparse_Event-Structured_Hierarchical_World_Model_for_Long-Horizon_Surgical_Robot_Manipulation|S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation]]

![[assets/2608.13103_figure.png|800]]

- **arXiv**: [2608.13103](https://arxiv.org/abs/2608.13103)
- **PDF**: https://arxiv.org/pdf/2608.13103
- **详细分析**: [[20_Research/Papers/具身智能/S2-HWM_Sparse_Event-Structured_Hierarchical_World_Model_for_Long-Horizon_Surgical_Robot_Manipulation|S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation]]
- **作者**: Shuzhe Zhang, Xin Zhu, Yinling Qian, Qiong Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习, 大模型
- **相关性评分**: 3.9（加权：具身智能 1.5，大模型 0.1，强化学习 0.2，世界模型 1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《S2-HWM: Sparse Event-Structured Hierarchical World Model for Long-Horizon Surgical Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon surgical robot manipulation is challenging because task rewards are sparse, while meaningful interaction changes occur at irregular intervals. Existing world-model agents typically imagine at primitive-step resolution, leaving variable-duration task progress implicit. Manually specified stages can provide intermediate structure, but their task specific boundaries are difficult to align with state-dependent interaction transitions. We propose S2-HWM, a Sparse Event-Structured Hierarchical World Model that learns sparse event evidence from primitive latent trajectories to coordinate an event-level manager and a primitive-step worker. The event evidence schedules manager goal updates, and each selected latent goal conditions the worker's primitive actions until the next update. The learned event evidence also forms variable-duration segments for an Event Transition Model (ETM), which predicts the next?boundary stochastic state, segment duration, and accumulated segment reward. Chaining these event-level predictions provides a variable-duration continuation beyond the primitive imagination horizon for manager learning, while the worker retains primitive-step actor-critic learning. On a SurRoL-based PegTransfer task, S2-HWM achieves a success rate of 98.7%, outperforming the flat GAS DreamerV3 baseline by 22.7 percentage points.

</details>

---

### [[20_Research/Papers/具身智能/Temporal_GRPO_Beyond_Trajectory-Level_Credit_in_Vision-Language-Action_Reinforcement_Learning|Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning]]

![[assets/2608.13026_figure.png|800]]

- **arXiv**: [2608.13026](https://arxiv.org/abs/2608.13026)
- **PDF**: https://arxiv.org/pdf/2608.13026
- **详细分析**: [[20_Research/Papers/具身智能/Temporal_GRPO_Beyond_Trajectory-Level_Credit_in_Vision-Language-Action_Reinforcement_Learning|Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning]]
- **作者**: Yao Zhou, Hang Gao, Fengge Wu, Changwen Zheng, Wenwen Qiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，强化学习 0.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Temporal GRPO: Beyond Trajectory-Level Credit in Vision-Language-Action Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Outcome-driven reinforcement learning offers a scalable way to post-train vision-language-action (VLA) policies from sparse task-success feedback. In common GRPO-based VLA post-training, one rollout-level advantage is applied to every action in the trajectory. A rollout that completes several valid stages but fails later can therefore penalize the actions that produced its earlier progress. We call this trajectory-level credit aliasing. Temporal GRPO addresses this problem by constructing detectable task stages, aligning each rollout with stage-specific action intervals, and comparing only rollouts that have entered the same stage. The resulting stage advantages are applied to their corresponding intervals in a single policy update. On RoboTwin 2.0, Temporal GRPO improves task success and sample efficiency, with consistent gains across task horizons. Controlled updates on LIBERO-Long preserve shared prerequisite stages and concentrate improvement at the first stage where rollout outcomes diverge.

</details>

---

### [[20_Research/Papers/机器人/AMR-Pose_An_Active_LED_Marker-Based_Relative_Pose_Estimation_Framework_With_Probabilistic_Switching_PnP_for_Cooperative_AUVs|AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs]]

![[assets/2608.12866_figure.png|800]]

- **arXiv**: [2608.12866](https://arxiv.org/abs/2608.12866)
- **PDF**: https://arxiv.org/pdf/2608.12866
- **详细分析**: [[20_Research/Papers/机器人/AMR-Pose_An_Active_LED_Marker-Based_Relative_Pose_Estimation_Framework_With_Probabilistic_Switching_PnP_for_Cooperative_AUVs|AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs]]
- **作者**: Zeyu Sha, Xiaorui Wang, Mingyang Yang, Feitian Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《AMR-Pose: An Active LED Marker-Based Relative Pose Estimation Framework With Probabilistic Switching PnP for Cooperative AUVs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable relative pose estimation between autonomous underwater vehicles (AUVs) is critical for cooperative ocean exploration, sampling, and multi-robot coordination. However, achieving robust vision-based relative localization in underwater environments remains challenging due to severe optical degradation, including turbidity, illumination variations, reflections, and intermittent feature occlusions. This paper presents AMR-Pose, an active LED marker-based relative pose estimation framework for cooperative AUVs. A compact marker module consisting of one red central LED and three blue peripheral LEDs is developed and integrated onto the leader AUV to provide distinctive visual features under complex underwater conditions. Building upon the detected marker observations, a probabilistic switching Perspective-n-Point estimator (PSwPnP) is developed by combining Lie-group pose propagation on $SE(3)$, probabilistic marker association, and visibility-adaptive measurement fusion for robust six-degree-of-freedom relative pose estimation. The proposed framework dynamically adapts the estimation process according to marker visibility, maintaining geometric consistency and temporal stability during partial observations and visibility transitions. Extensive water-tank experiments with motion-capture ground truth validate that AMR-Pose achieves accurate, smooth, and robust relative pose estimation under challenging underwater conditions. Closed-loop leader-follower experiments further demonstrate its feasibility for real-time relative pose feedback in cooperative underwater robotics.

</details>

---

### [[20_Research/Papers/具身智能/HumanoidVLN_A_Physics-Grounded_Simulator_and_Benchmark_for_Vision-Language_Navigation_Across_Diverse_Humanoid_Embodiments|HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments]]

![[assets/2608.12860_figure.png|800]]

- **arXiv**: [2608.12860](https://arxiv.org/abs/2608.12860)
- **PDF**: https://arxiv.org/pdf/2608.12860
- **详细分析**: [[20_Research/Papers/具身智能/HumanoidVLN_A_Physics-Grounded_Simulator_and_Benchmark_for_Vision-Language_Navigation_Across_Diverse_Humanoid_Embodiments|HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments]]
- **作者**: Quan-Dung Pham, Anh Dao, The-Anh Nguyen, Minh Nguyen-Dinh, Phuong Nam Dang, Tri Pham, Hung Tran, Bach Dao, Tuyen P. Le, Truong Nguyen, Quan Nguyen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 3.6（加权：具身智能 2.1，大模型 0.2，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HumanoidVLN: A Physics-Grounded Simulator and Benchmark for Vision-Language Navigation Across Diverse Humanoid Embodiments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim, Habitat-Sim, Real-World, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Navigation (VLN) for humanoid robots poses challenges existing benchmarks fail to address: bipedal locomotion imposes physical constraints absent from wheeled agents, humanoid morphologies vary across platforms, and egocentric observations are distorted by locomotion-induced camera dynamics. We present HumanoidVLN, a physics-grounded simulator and benchmark for VLN across diverse humanoid embodiments. Built on NVIDIA Isaac Sim, our platform supports an extensible set of humanoid configurations, demonstrated on four robots (Unitree G1, Unitree H1, Internal-A, Internal-B) spanning 10-12 lower-body DoF and heights from 1.17m to 1.80m, via a hierarchical control stack combining a reinforcement learning locomotion policy with interchangeable PD or MPC path trackers. New robots and VLN models integrate with minimal effort; we demonstrate compatibility with NaVILA, DualVLN, StreamVLN, and JanusVLN. Environments are drawn from artist-designed scenes and 3D Gaussian Splatting reconstructions, filtered for navigable areas exceeding 100 square meters. Instructions are generated by a dual generator-reviewer plus paraphraser multi-agent pipeline with human-in-the-loop verification, yielding 933 collision-aware reference episodes, each paired with one fine-grained instruction and three coarse-grained stylistic variants (formal, natural, casual). Across four models and four embodiments, JanusVLN achieves the highest mean success rate of 43.55% and nDTW of 48.38. In a 20-episode sim-to-real pilot with DualVLN and the Unitree G1, navigation errors correlate strongly (r=0.935), with a mean absolute difference of 0.68m and mean trajectory similarity of 0.782 (+/-0.188) nDTW. These results highlight the interaction between VLN models, controllers, and humanoid embodiments under physical execution. Code, benchmark, and data will be released upon acceptance at https://humanoid-vln.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/AirForesight_Current-to-Future_Spatial_Map_Imagination_with_Cross-Space_Planning_Consistency_for_UAV-VLN|AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN]]

![[assets/2608.12835_figure.png|800]]

- **arXiv**: [2608.12835](https://arxiv.org/abs/2608.12835)
- **PDF**: https://arxiv.org/pdf/2608.12835
- **详细分析**: [[20_Research/Papers/具身智能/AirForesight_Current-to-Future_Spatial_Map_Imagination_with_Cross-Space_Planning_Consistency_for_UAV-VLN|AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN]]
- **作者**: Yutong Liu, Xiaojie Li, Mingzhu Xu, Jianlong Wu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《AirForesight: Current-to-Future Spatial Map Imagination with Cross-Space Planning Consistency for UAV-VLN》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned Aerial Vehicle Vision-Language Navigation (UAV-VLN) requires agents to follow language instructions, infer spatial structure from sparse multi-view observations, and execute feasible 3D motion in complex outdoor environments. Despite recent progress with large language models, most existing methods still map vision-language inputs directly to actions, providing limited explicit scene grounding and future-aware spatial reasoning. We propose AirForesight, a current-to-future spatial map imagination framework for UAV-VLN. AirForesight first learns a structured current-map representation from multi-view observations. This representation is jointly supervised by current-map reconstruction and future-trajectory prediction, encouraging it to encode both present scene structure and future motion intent. Under structured causal attention, the current spatial knowledge is propagated to future-map reasoning, and the resulting current and future representations are aggregated to predict the next 3D waypoint. To make spatial imagination more relevant to navigation, we introduce a cross-space planning consistency loss that encourages directional agreement between the predicted map-space trajectory and the expert action direction derived from the ground-truth waypoint displacement. Experiments on OpenUAV and AerialVLN-S, together with extensive ablations, demonstrate strong performance and support the effectiveness and stability of the proposed framework.

</details>

---

### [[20_Research/Papers/机器人/Genetic_Fuzzy_System-Based_Multi-Robot_Coordination_for_Planetary_Missions|Genetic Fuzzy System-Based Multi-Robot Coordination for Planetary Missions]]

![[assets/2608.12755_figure.png|800]]

- **arXiv**: [2608.12755](https://arxiv.org/abs/2608.12755)
- **PDF**: https://arxiv.org/pdf/2608.12755
- **详细分析**: [[20_Research/Papers/机器人/Genetic_Fuzzy_System-Based_Multi-Robot_Coordination_for_Planetary_Missions|Genetic Fuzzy System-Based Multi-Robot Coordination for Planetary Missions]]
- **作者**: Daegyun Choi, Donghoon Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Genetic Fuzzy System-Based Multi-Robot Coordination for Planetary Missions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes a decentralized approach for a multi-robot system (MRS) using a genetic fuzzy system to perform a collaborative object transportation task that minimizes the total path length of the MRS in unstructured environment while avoiding obstacles. For an environment given by an elevation map, terrain traversability analysis with respect to the slope is performed to reduce the dimension and identify non-traversable areas that can be considered as obstacles, and the given map is converted into a traversability map in two dimensional space. In the training process, proposed fuzzy inference systems (FISs) to generate the MRS's velocity for transporting an object to a target position are optimized by a genetic algorithm with several scenarios, such as a local minima, a target that is close to an obstacle, and a cluttered environment. The trained FIS models are applied to the testing environment, which is the converted traversability map, and validated using multiple scenarios.

</details>

---

### [[20_Research/Papers/具身智能/SAP-Nav_Spatial_Semantic_Representation_Meets_Active_Perception_for_Hierarchical_Open-Vocabulary_Object_Navigation|SAP-Nav: Spatial Semantic Representation Meets Active Perception for Hierarchical Open-Vocabulary Object Navigation]]

![[assets/2608.12707_figure.png|800]]

- **arXiv**: [2608.12707](https://arxiv.org/abs/2608.12707)
- **PDF**: https://arxiv.org/pdf/2608.12707
- **详细分析**: [[20_Research/Papers/具身智能/SAP-Nav_Spatial_Semantic_Representation_Meets_Active_Perception_for_Hierarchical_Open-Vocabulary_Object_Navigation|SAP-Nav: Spatial Semantic Representation Meets Active Perception for Hierarchical Open-Vocabulary Object Navigation]]
- **作者**: Xuetong Pei, Jian Liu, Vidura Munasinghe, Bo Miao, U-Xuan Tan, Wenrui Ding, Na Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SAP-Nav: Spatial Semantic Representation Meets Active Perception for Hierarchical Open-Vocabulary Object Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical open-vocabulary object navigation (OVON) requires agents to follow free-form instructions that may specify targets through scene-, room-, region-, and instance-level cues in unseen environments. Although recent work LangMap has formalized this setting, reliably solving it under partial observations remains challenging: spatial grounding requires persistent environment-level evidence, whereas target verification requires clear and discriminative candidate views. We present SAP-Nav, a fully online, zero-shot framework that addresses both requirements through active perception. SAP-Nav incrementally constructs a Queryable Spatial-Semantic Representation from actively acquired room views, enabling spatial semantic queries from any explored location. It further employs Active Viewpoint Verification to assess whether the current observation provides sufficient evidence and, when necessary, reposition the agent to a more informative viewpoint before verifying candidates against category and attribute constraints. Although designed for hierarchical OVON, SAP-Nav supports both hierarchical and standard category-level OVON without task-specific training or precomputed scene maps. Experiments on LangMap and HM3D-OVON show that SAP-Nav achieves the overall best performance, including a 12.2% improvement in SR over training-based methods on region-level navigation. Real-world robot experiments further demonstrate its practical feasibility. Code will be made publicly available upon acceptance.

</details>

---

### [[20_Research/Papers/大模型/Do_LLMs_Beat_Nash_Testing_Decentralized_Coordination_in_Self-Play_Multi-Agent_Games|Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games]]

![[assets/2608.12547_figure.png|800]]

- **arXiv**: [2608.12547](https://arxiv.org/abs/2608.12547)
- **PDF**: https://arxiv.org/pdf/2608.12547
- **详细分析**: [[20_Research/Papers/大模型/Do_LLMs_Beat_Nash_Testing_Decentralized_Coordination_in_Self-Play_Multi-Agent_Games|Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games]]
- **作者**: Deborah Sinishaw, Qile Zhu, Edwin Meriaux, Gregory Dudek
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Do LLMs Beat Nash? Testing Decentralized Coordination in Self-Play Multi-Agent Games》归入 大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents deployed without a central controller are often assumed to require communication to coordinate their actions. We ask what remains possible without it: when independent instances of the same model cannot communicate, can they still reason about their counterparts well enough to exceed the standard game-theoretic baseline for uncoordinated play? We introduce a benchmark of one-shot, no-communication games in which each of thirteen language models is told only that its counterparts are running the same model and is evaluated against the Nash equilibrium of the underlying game. In two-player matrix games spanning seven archetypes and two to ten actions per player, two frontier-hosted models consistently exceed their Nash benchmark, approaching the optimal joint outcome in several archetypes, while most open-weight models achieve only partial gains that vary sharply by game structure. Performance degrades substantially in team-based games with four or more interchangeable agents, particularly as the action space grows, suggesting that whatever capability drives self-play gains in dyadic games does not transfer to larger multi-agent teams.

</details>

---

### [[20_Research/Papers/强化学习/Entropy-Augmented_Multi-Objective_Policy_Optimization_in_Multiagent_Systems|Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems]]

![[assets/2608.12534_figure.png|800]]

- **arXiv**: [2608.12534](https://arxiv.org/abs/2608.12534)
- **PDF**: https://arxiv.org/pdf/2608.12534
- **详细分析**: [[20_Research/Papers/强化学习/Entropy-Augmented_Multi-Objective_Policy_Optimization_in_Multiagent_Systems|Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems]]
- **作者**: Jamie Santos, Ayhan Alp Aydeniz, Raghav Thakar, Kagan Tumer
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.7（加权：大模型 0.1，强化学习 0.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Entropy-Augmented Multi-Objective Policy Optimization in Multiagent Systems》归入 强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous agent teams deployed in settings such as marine and extraterrestrial outposts must coordinate actions to achieve optimal outcomes across multiple competing objectives. Multi-objective evolutionary algorithms such as NSGA-II optimize for diversity in the objective space, but neglect diversity in the behavior space, possibly leading to premature convergence and a collapse in behaviors that may differentiate policies in different external conditions. To address this, we introduce an entropy-augmented policy evaluation strategy that incorporates an entropy bonus into agent fitness scores, discouraging behavioral homogeneity across the evolving population. By augmenting policy evaluation with a behavior-space diversity signal while preserving the underlying Pareto optimization framework, our method is designed to encourage exploration of behaviorally distinct policies in multiagent domains. We evaluate our approach across rover-domain experiments with qualitatively distinct reward structures and observe hypervolume improvements of up to 48% relative to the NSGA-II baseline, suggesting that behavioral diversity is a promising and underexplored direction for improving multi-objective multiagent evolutionary optimization.

</details>

---

### [[20_Research/Papers/机器人/Excitation-Supervised_Closed-Loop_Self-Calibration_and_Target_Seeking_for_an_Unknown-Pose_Range-Bearing_Relay|Excitation-Supervised Closed-Loop Self-Calibration and Target Seeking for an Unknown-Pose Range-Bearing Relay]]

![[assets/2608.12528_first_page.png|800]]

- **arXiv**: [2608.12528](https://arxiv.org/abs/2608.12528)
- **PDF**: https://arxiv.org/pdf/2608.12528
- **详细分析**: [[20_Research/Papers/机器人/Excitation-Supervised_Closed-Loop_Self-Calibration_and_Target_Seeking_for_an_Unknown-Pose_Range-Bearing_Relay|Excitation-Supervised Closed-Loop Self-Calibration and Target Seeking for an Unknown-Pose Range-Bearing Relay]]
- **作者**: Yash Bagla
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Excitation-Supervised Closed-Loop Self-Calibration and Target Seeking for an Unknown-Pose Range-Bearing Relay》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A vehicle seeking a hidden target through a range-bearing relay of unknown position and yaw must decide, online, whether its own motion has already made the relay calibration trustworthy, and what to do when it has not. Two distinct vehicle-relative observations are known to remove the calibration gauge and make the target's relay-local packet globally actionable (arXiv:2608.09464), but that statement is static: it classifies a stored window only after the fact. This paper supplies the closed-loop layer: we show that the trajectory-spread margin $S_v$ that governs identifiability is simultaneously a finite-noise seed-accuracy bound, a local-vector variance decomposition, and a circle-geometry excitation budget, and we use it to supervise an excitation-reset controller. An excitation-supervised algorithm retriggers exploratory motion whenever the spread certificate is insufficient, projecting the target-seeking input away from the excitation's push, and otherwise proceeds to unrestricted target seeking. Under explicit sampling assumptions the supervision rule provably acquires any required excitation in finite time; in the noiseless local regime with positive excitation decay, estimator convergence yields target-seeking convergence after certification; and the threshold is selected from a desired calibration-accuracy level rather than chosen heuristically. Closed-loop simulation, paired Monte Carlo comparisons, a spread-threshold ablation, and a ROS 2/Gazebo software-in-the-loop experiment with sensing delay validate the approach. A decay-rate sweep shows that supervision matters when a fixed schedule's decay outruns the unknown time-to-adequate-excitation: over 100 paired trials the fixed baseline's yaw RMSE rises from 0.010 to 0.065 rad and success falls to 56%, while target-tracking error remains insensitive; supervision keeps yaw RMSE between 0.0095 and 0.0191 rad with 100% success.

</details>

---

### [[20_Research/Papers/具身智能/RoboSynChallenge_Mastering_Real-World_Dexterity_via_Generalizing_Synthesized_Manipulation_Skills|RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills]]

![[assets/2608.12416_figure.png|800]]

- **arXiv**: [2608.12416](https://arxiv.org/abs/2608.12416)
- **PDF**: https://arxiv.org/pdf/2608.12416
- **详细分析**: [[20_Research/Papers/具身智能/RoboSynChallenge_Mastering_Real-World_Dexterity_via_Generalizing_Synthesized_Manipulation_Skills|RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills]]
- **作者**: Runyi Zhao, Ruixin Wu, Chengkun Li, Hongrui Zhang, Ang Li, Ruixing Jin, Yueci Deng, Yingying Guo, Lihe Ding, Shaocong Dong, Tianfan Xue, Yanjun Gao...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《RoboSynChallenge: Mastering Real-World Dexterity via Generalizing Synthesized Manipulation Skills》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ManipulationNet, RLBench, Real-World, Sim2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving generalizable robotic manipulation remains a central challenge in embodied intelligence. Despite rapid advances in model architectures and learning algorithms, progress is often limited by the scarcity and narrow diversity of real-world data. The RoboSynChallenge competition introduces a unified benchmark to evaluate and advance the generalizability of manipulation policies across a spectrum of tasks, environments, and difficulty levels. To alleviate the shortage of realistic data, the challenge integrates large-scale synthetic data generation with standardized real-world robotic evaluation. Participants are encouraged to leverage synthesized state-action trials to improve general-purpose policy learning, while final assessments are conducted exclusively on unseen real-world manipulation environments. Baseline implementations, including Transformer-, Diffusion-, Vision-Language-Action, and World-Action-Model-based policies, are provided to ensure reproducibility and comparability. By coupling scalable simulation-based training with rigorous real-world validation, RoboSynChallenge aims to foster the development of broadly capable, data-efficient, and adaptable manipulation systems, thereby paving the way toward truly general robotic intelligence.

</details>

---
