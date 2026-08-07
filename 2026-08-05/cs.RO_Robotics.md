# cs.RO | Robotics | 2026-08-05

#arxiv #ComputerScience

**论文数**: 25

### [[20_Research/Papers/强化学习/Stochastic_Multiple_Shooting_Trajectory_Optimization_via_Sequential_Local_Policy_Evaluation|Stochastic Multiple Shooting Trajectory Optimization via Sequential Local Policy Evaluation]]

![[assets/2608.03978_figure.png|800]]

- **arXiv**: [2608.03978](https://arxiv.org/abs/2608.03978)
- **PDF**: https://arxiv.org/pdf/2608.03978
- **详细分析**: [[20_Research/Papers/强化学习/Stochastic_Multiple_Shooting_Trajectory_Optimization_via_Sequential_Local_Policy_Evaluation|Stochastic Multiple Shooting Trajectory Optimization via Sequential Local Policy Evaluation]]
- **作者**: Ashwin Gupta, Joseph Moore
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 世界模型
- **相关性评分**: 1.2（加权：具身智能 0.3，强化学习 0.2，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《Stochastic Multiple Shooting Trajectory Optimization via Sequential Local Policy Evaluation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stochastic single shooting trajectory optimization methods such as Model Predictive Path Integral control (MPPI) have been widely adopted in robotics due to their ability to reason about probabilistic dynamics and provide solutions where model gradients are noisy, costly to evaluate, or unavailable. However, satisfaction of terminal constraints when shooting over long action sequences is often sample inefficient, requiring a large number of iterations for convergence. In this paper, we present a stochastic multiple shooting method that optimizes short control action sequences connected via local feedback policies to improve sample efficiency and convergence to a terminal set. Additionally, we show that we are able to synthesize approximate system Jacobians purely from rollouts, making the method suitable for model-based reinforcement learning with black-box dynamics. We demonstrate the algorithm has improved sample efficiency and terminal set convergence for three nonlinear, underactuated optimization problems: a classic cartpole swingup task with analytical dynamics, a cartpole swingup task with learned neural network dynamics, and a VTOL quadplane performing a high angle-of-attack, precision post-stall landing maneuver.

</details>

---

### [[20_Research/Papers/具身智能/ETA_A_New_Agentic_Paradigm_for_Embodied_Tasks|ETA: A New Agentic Paradigm for Embodied Tasks]]

![[assets/2608.03924_figure.png|800]]

- **arXiv**: [2608.03924](https://arxiv.org/abs/2608.03924)
- **PDF**: https://arxiv.org/pdf/2608.03924
- **详细分析**: [[20_Research/Papers/具身智能/ETA_A_New_Agentic_Paradigm_for_Embodied_Tasks|ETA: A New Agentic Paradigm for Embodied Tasks]]
- **作者**: Yitong Chen, Zezheng Huai, Sixian Li, Yubang Wang, Haozhe Zhang, Yifei Zhang, Hechang Chen, Jingjing Gong, Yu-Gang Jiang, Xipeng Qiu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ETA: A New Agentic Paradigm for Embodied Tasks》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoRE-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When will robots have their ChatGPT moment? Such a breakthrough requires a general-purpose robot that can handle unfamiliar tasks in unfamiliar environments, remain controllable over long interactions, and learn from experience. Today's embodied systems largely follow an end-to-end observation-to-action path. Despite rapid progress, they remain far from this goal: their generalization depends heavily on the coverage of robot training data, while long task execution remains difficult to control and inspect. To realize this goal, we introduce the Embodied Task Agent (ETA), a new paradigm for extending digital agents into the physical world, and release OpenETA as its open-source implementation. ETA centers the robot around a Planner that chooses one Tool call at a time, an Interface that controls execution, and a World that returns the result and a fresh observation. This loop allows the agent to verify outcomes, adapt its plan, and turn successful and failed interactions into reusable experience. OpenETA provides replaceable Planners, composable Tools and Skills, auditable memory, replayable trajectories, and common interfaces for simulation and real robots. For Codex, OpenETA can operate as a lightweight plugin that exposes only observe, mark_point, and move_to.

</details>

---

### [[20_Research/Papers/强化学习/EvoHIL_Self-Evolving_Reward_and_Flow-Matched_Policy_Optimization_for_Robust_Human-in-the-Loop_Reinforcement_Learning|EvoHIL: Self-Evolving Reward and Flow-Matched Policy Optimization for Robust Human-in-the-Loop Reinforcement Learning]]

![[assets/2608.03872_figure.png|800]]

- **arXiv**: [2608.03872](https://arxiv.org/abs/2608.03872)
- **PDF**: https://arxiv.org/pdf/2608.03872
- **详细分析**: [[20_Research/Papers/强化学习/EvoHIL_Self-Evolving_Reward_and_Flow-Matched_Policy_Optimization_for_Robust_Human-in-the-Loop_Reinforcement_Learning|EvoHIL: Self-Evolving Reward and Flow-Matched Policy Optimization for Robust Human-in-the-Loop Reinforcement Learning]]
- **作者**: Shuoqin Zhang, Tongtong Cheng, Xiru Gao, Jinzhuo Peng, Bin Zheng, Jiahao Tu, Ke Wang, Jia Pan, Zhe Hu, Kai Liu
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 2.6（加权：具身智能 0.3，强化学习 1.8，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《EvoHIL: Self-Evolving Reward and Flow-Matched Policy Optimization for Robust Human-in-the-Loop Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HIL-RL, HIL-SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-in-the-loop reinforcement learning (HIL-RL) enables robots to learn contact-rich manipulation from limited real-world interaction, but deployment exposes three coupled limitations: static visual reward models fail under scene changes; independently sampled actions cause temporally inconsistent motion; and vision-based policies remain sensitive to appearance shifts. We present EvoHIL, a unified framework that adapts the reward model, action generator, and visual do main within a staged human-in-the-loop learning process. First, self-evolving reward (SER) adapts the success classifier from human-confirmed positives and provisional weak negatives. Second, Action Flow Stabilization (AFS) generates temporally coherent action chunks through flow matching, grounding policy updates in executed action prefixes and demonstrated behavior. Third, retention-aware offline fine-tuning replays relit interaction data while anchoring the AFS actor-critic to prior behavior, adapting the visual domain without additional robot interaction. Across six manipulation tasks on Franka FR3 and SO-101 arms under a controlled lighting shift, EvoHIL improves task success, agreement with human-confirmation labels, motion smoothness, and completion time relative to human-in-the-loop and imitation baselines.Project page: https://anonymous4366.github.io/EvoHIL/

</details>

---

### [[20_Research/Papers/机器人/Designing_Social_Robots_for_Inclusive_Child_Wellbeing_Assessment_Insights_from_Communities_Supporting_Developmental_Language_Disorder_and_Fo|Designing Social Robots for Inclusive Child Wellbeing Assessment: Insights from Communities Supporting Developmental Language Disorder and Forced Migration]]

![[assets/2608.03820_figure.png|800]]

- **arXiv**: [2608.03820](https://arxiv.org/abs/2608.03820)
- **PDF**: https://arxiv.org/pdf/2608.03820
- **详细分析**: [[20_Research/Papers/机器人/Designing_Social_Robots_for_Inclusive_Child_Wellbeing_Assessment_Insights_from_Communities_Supporting_Developmental_Language_Disorder_and_Fo|Designing Social Robots for Inclusive Child Wellbeing Assessment: Insights from Communities Supporting Developmental Language Disorder and Forced Migration]]
- **作者**: Fethiye Irmak Dogan, Yue Lou, Alva Markelius, Emma Geijer-Simpson, Gustaf Gredebäck, Tamsin Jane Ford, Ginevra Castellano, Hatice Gunes, Georgina Warner, Jenny L. Gibson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Designing Social Robots for Inclusive Child Wellbeing Assessment: Insights from Communities Supporting Developmental Language Disorder and Forced Migration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assessing children's wellbeing and mental health can be particularly challenging for children experiencing communication barriers, such as children with Developmental Language Disorder (DLD) and children with forced migration backgrounds. During the assessment process, traditional self-report questionnaires place substantial demands on language comprehension and verbal expression. In this context, social robots have emerged as a promising tool for supporting wellbeing assessment without solely relying on self-report questionnaires, yet limited research has examined how such interactions can be designed to be inclusive, appropriate, and ethically acceptable for children with diverse communication needs. To address this gap, we created candidate child--robot interaction activities as design probes and conducted focus groups with parents and professionals supporting children with DLD and children with forced migration backgrounds. Through thematic analysis, we identified considerations relating to robot role and capabilities, interactional dynamics, individual differences, and child agency, alongside population-specific considerations shaped by children's communication needs and lived experiences. Based on these findings, we derive a set of ethical and inclusive design recommendations for robot-mediated wellbeing assessment. By foregrounding these considerations and recommendations, this work contributes design guidance for inclusive robot-mediated wellbeing assessments for children with diverse communication needs.

</details>

---

### [[20_Research/Papers/强化学习/GORDON_Graph-based_Object-centric_Rewards_for_Decomposition_of_Long-Horizon_Manipulation|GORDON: Graph-based Object-centric Rewards for Decomposition of Long-Horizon Manipulation]]

![[assets/2608.03753_figure.png|800]]

- **arXiv**: [2608.03753](https://arxiv.org/abs/2608.03753)
- **PDF**: https://arxiv.org/pdf/2608.03753
- **详细分析**: [[20_Research/Papers/强化学习/GORDON_Graph-based_Object-centric_Rewards_for_Decomposition_of_Long-Horizon_Manipulation|GORDON: Graph-based Object-centric Rewards for Decomposition of Long-Horizon Manipulation]]
- **作者**: Andrea Protopapa, Davide Buoso, Francesca Pistilli, Georgia Chalvatzaki, Giuseppe Averta
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《GORDON: Graph-based Object-centric Rewards for Decomposition of Long-Horizon Manipulation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GraphIRL, PEARL, XIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning long-horizon manipulation skills with reinforcement learning remains challenging due to the complexity of reward design, the limited guidance of sparse rewards, and the high cost of manual subtask annotation. Visual demonstrations can provide supervision for reward learning, but rewards learned from raw pixels can be brittle and sensitive to visual variation, background appearance, and robot motion. In this work, we propose GORDON, a graph-based object-centric reward learning framework that learns dense rewards from action-free video demonstrations. Each visual scene is represented as a graph of detected objects and spatial relations, and a graph neural network is trained in a self-supervised manner to embed these graphs into a task-aligned latent space. To align the representation with semantic task progress, we introduce an activity-aware weighted pooling mechanism that emphasizes task-relevant objects while masking robot-dominated motion. The dense reward is then computed as distances in the learned latent space of the current state to demonstrated goal configurations, providing a measure of task progress. In long-horizon tasks, the temporal profile of this reward reveals stage-wise object-state transitions, enabling automatic subtask discovery without manual segmentation. The discovered segments are then used to train subtask-specific rewards and specialized policies that are composed sequentially. Experiments on seven manipulation tasks on MAGICAL and ManiSkill3 benchmarks show that our object-centric reward improves reinforcement learning in short-horizon settings and enables successful policy learning in complex long-horizon tasks through automatic decomposition, achieving an average success rate of 74.4% across the long-horizon tasks (on average approximately +35 p.p. vs. best learned baseline and approximately +25 p.p. vs. oracle).

</details>

---

### [[20_Research/Papers/具身智能/Track4Action_Distilling_World-Centric_3D_Tracker_into_Vision-Language-Action_Policies|Track4Action: Distilling World-Centric 3D Tracker into Vision-Language-Action Policies]]

![[assets/2608.03727_figure.png|800]]

- **arXiv**: [2608.03727](https://arxiv.org/abs/2608.03727)
- **PDF**: https://arxiv.org/pdf/2608.03727
- **详细分析**: [[20_Research/Papers/具身智能/Track4Action_Distilling_World-Centric_3D_Tracker_into_Vision-Language-Action_Policies|Track4Action: Distilling World-Centric 3D Tracker into Vision-Language-Action Policies]]
- **作者**: Chenyi Wang, Xinkai Wang, Bokai Lin, Jialin Tian, Fucheng Zhang, Cewu Lu, Lixin Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Track4Action: Distilling World-Centric 3D Tracker into Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, Track4World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action labels tell a vision-language-action (VLA) policy which robot commands to imitate, but not how those commands change the 3D world. The aligned demonstration clip contains this missing supervision because its $K$ frame transitions record the geometry, motion, visibility, and camera change produced during the corresponding $K$ actions. We introduce Track4Action, a framework that distills this realized transition from a frozen world-centric 3D tracker into a current-observation VLA policy. During training, Track4World encodes the clip $V_{t:t+K}$ into a pooled tracker feature. Learnable track queries infer this feature from current VLA hidden states, match it in a shared space, and condition a flow-matching action head through a feature-wise gate. The tracker feature only defines the alignment target, so neither the clip nor the tracker is used at deployment. Track4Action reaches 82.3% on zero-shot LIBERO-Plus, improving the alignment-free variant by 7.6 points and LaMP by 3.0 points. It obtains 80.44% and 81.48% on the clean and randomized RoboTwin 2.0 splits, and 67.5% average success across four physical bimanual tasks, 25.0 points above the alignment-free variant. The gains across simulation and physical tasks support action-aligned 3D tracker features as privileged supervision for tracker-free VLA deployment. Our project page is available at https://wing0night.github.io/track4action-project-page.

</details>

---

### [[20_Research/Papers/机器人/Active_Stiffness_Control_of_a_Supportive_Continuum_Robot|Active Stiffness Control of a Supportive Continuum Robot]]

![[assets/2608.03677_figure.png|800]]

- **arXiv**: [2608.03677](https://arxiv.org/abs/2608.03677)
- **PDF**: https://arxiv.org/pdf/2608.03677
- **详细分析**: [[20_Research/Papers/机器人/Active_Stiffness_Control_of_a_Supportive_Continuum_Robot|Active Stiffness Control of a Supportive Continuum Robot]]
- **作者**: Rana Danesh, Farrokh Janabi-Sharifi, Farhad Aghili
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Active Stiffness Control of a Supportive Continuum Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Supportive continuum robots (SCRs) enhance the load-bearing capability of an operative continuum robot by mechanically coupling it with a supportive arm. However, their passive stiffness is determined by the mechanical configuration and cannot be adjusted online for varying payloads or interaction forces. Active stiffness control is therefore needed to regulate the load response and maintain positioning accuracy. Meanwhile, the closed-chain structure introduces kinematic constraints that complicate task-space regulation and stiffness control. This paper presents an active task-space stiffness control framework for a tendon-driven SCR. An existing geometric variable strain model describes the closed-chain dynamics, which are projected onto the constraint-consistent motion subspace. A projected sliding mode controller regulates the operative arm tip while preserving the constraints, and closed-loop stability is established through Lyapunov analysis. After position regulation, active apparent stiffness is introduced through a virtual Cartesian spring based on position-error feedback to shape the force--displacement response. The framework is evaluated in simulation and experimentally validated under prescribed external loads and different desired configurations. Results show that increasing the commanded stiffness gain reduces load-induced tip deflection and increases apparent directional stiffness, thereby improving load resistance and positioning robustness under external loading.

</details>

---

### [[20_Research/Papers/具身智能/Unified_Visuomotor_Targets_Supervising_VLAs_Beyond_Physical_Actions|Unified Visuomotor Targets: Supervising VLAs Beyond Physical Actions]]

![[assets/2608.03563_figure.png|800]]

- **arXiv**: [2608.03563](https://arxiv.org/abs/2608.03563)
- **PDF**: https://arxiv.org/pdf/2608.03563
- **详细分析**: [[20_Research/Papers/具身智能/Unified_Visuomotor_Targets_Supervising_VLAs_Beyond_Physical_Actions|Unified Visuomotor Targets: Supervising VLAs Beyond Physical Actions]]
- **作者**: Zhenyang Feng, Unnat Jain
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Unified Visuomotor Targets: Supervising VLAs Beyond Physical Actions》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, UniVLA, VQ-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

VLA models are trained to predict robot actions from visual and language observations. This is a natural choice, but it creates a mismatch: VLMs encode rich, high-level representations of scenes and goals, while robot actions are low-level signals with limited task structure. We ask whether changing what the policy is trained to predict, rather than how it is architecturally designed, can yield better and more efficiently trained policies. We propose UVT (Unified Visuomotor Target), a unified latent prediction target that jointly encodes motor control and visual scene transition information, requiring no architectural changes and no additional data. Applied to two representative VLA systems across simulation benchmarks and real bimanual manipulation tasks, UVT improves training efficiency, final task performance, and policy robustness, with particularly strong gains under limited training budgets and challenging environmental conditions. Rollout videos and additional qualitative results are available at our project webpage: https://unified-visuomotor-targets.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Human_Centric_Embodied_Intelligence_for_Soft_Wearable_Robotics|Human Centric Embodied Intelligence for Soft Wearable Robotics]]

![[assets/2608.03556_first_page.png|800]]

- **arXiv**: [2608.03556](https://arxiv.org/abs/2608.03556)
- **PDF**: https://arxiv.org/pdf/2608.03556
- **详细分析**: [[20_Research/Papers/具身智能/Human_Centric_Embodied_Intelligence_for_Soft_Wearable_Robotics|Human Centric Embodied Intelligence for Soft Wearable Robotics]]
- **作者**: Rainier Natividad, Raye Chen-Hua Yeow
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Human Centric Embodied Intelligence for Soft Wearable Robotics》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft wearable robots have evolved rapidly from proof-of-concept devices into promising platforms for rehabilitation, occupational assistance, and human augmentation. As the field matures, its central challenge extends beyond the development of softer materials and more capable actuators to the integration of sensing, intelligence, and human adaptation into systems that users can wear comfortably, trust, and benefit from over extended periods. This transition motivates the concept of Human-Centric Embodied Intelligence (HCEI), in which intelligence emerges from the coupled human-robot system through the interaction of morphology, multimodal sensing, adaptive cognition, compliant actuation, and the wearer's own physiological and behavioral adaptation. To organize this perspective, this review introduces the Perception-Cognition-Actuation-Augmentation (PCAA) framework, which positions perception and cognition as the primary drivers of design, shifting development beyond the conventional actuator-first paradigm. Using this framework, the review synthesizes advances in soft materials, wearable sensing, artificial intelligence, actuation, human-robot interaction, digital twins, clinical translation, manufacturing, regulation, and ethics, highlighting how these interdependent components collectively shape long-term personalization and real-world deployment. By providing a unified conceptual framework and design perspective, this review aims to guide future research, foster interdisciplinary collaboration, and accelerate the translation of next-generation soft wearable robots toward personalized, predictive, and human-centric wearable intelligence.

</details>

---

### [[20_Research/Papers/大模型/RoboReact_Agentic_Skill_Distillation_from_Generated_Egocentric_Videos_for_Generalizable_Whole-Body_Manipulation|RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation]]

![[assets/2608.03387_figure.png|800]]

- **arXiv**: [2608.03387](https://arxiv.org/abs/2608.03387)
- **PDF**: https://arxiv.org/pdf/2608.03387
- **详细分析**: [[20_Research/Papers/大模型/RoboReact_Agentic_Skill_Distillation_from_Generated_Egocentric_Videos_for_Generalizable_Whole-Body_Manipulation|RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation]]
- **作者**: Shuliang He, Shuai Wang, Bo Yue, Junchi Teng, Changyu Wang, Guiliang Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.9，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《RoboReact: Agentic Skill Distillation from Generated Egocentric Videos for Generalizable Whole-Body Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots have the potential to perform dexterous manipulation in human environments, yet acquiring diverse and generalizable skills remains costly due to expensive hardware data collection and labor-intensive annotation. Recent advances in video generative models provide a promising opportunity to synthesize rich manipulation experiences from visual observations, but transferring such imagined behaviors into executable whole-body humanoid skills remains largely unexplored. In this work, we present RoboReact, a framework that automatically synthesizes whole-body humanoid manipulation skills from a single egocentric RGB-D observation. RoboReact generates human manipulation videos, extracts geometry-preserving interaction keyframes through depth-aware 3D reconstruction, and retargets them to high-DoF humanoid platforms while preserving hand-object interaction geometry. To bridge the gap between imagined plans and physical execution, RoboReact performs online object-centric re-grounding and leverages a vision-language model-guided refinement loop to adapt skills under geometric mismatch and execution deviations. The refined skills are executed through a whole-body controller, enabling coordinated whole-body manipulation and dexterous interaction. Experiments on real humanoid robots demonstrate that RoboReact generalizes across diverse object configurations and robustly recovers from execution disturbances without requiring teleoperation or human demonstrations. These results highlight the potential of combining generative models, vision-language reasoning, and closed-loop control for scalable humanoid skill acquisition.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Context-Aware_Motion_Priors_for_Humanoid_Control|Learning Context-Aware Motion Priors for Humanoid Control]]

![[assets/2608.03234_figure.png|800]]

- **arXiv**: [2608.03234](https://arxiv.org/abs/2608.03234)
- **PDF**: https://arxiv.org/pdf/2608.03234
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Context-Aware_Motion_Priors_for_Humanoid_Control|Learning Context-Aware Motion Priors for Humanoid Control]]
- **作者**: Yunyang Mo, Yi Gu, Yangchen Zhou, Hanyang Cao, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Learning Context-Aware Motion Priors for Humanoid Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion priors provide powerful guidance for learning naturalistic humanoid behaviors. However, existing methods typically learn a general, task-agnostic prior from the entire reference dataset and apply it uniformly throughout policy training. As a result, the prior cannot distinguish which reference motions are relevant to the current task context, potentially providing irrelevant or conflicting guidance. We present Context-Aware Motion Priors (CMP), a framework that adapts a general motion prior to the current task context without manual skill labels, dataset partitioning, or a separate skill discovery stage. Specifically, CMP learns context-motion compatibility using high-advantage policy rollouts, while a demonstration-based objective keeps the learned relevance grounded in the reference distribution. The resulting relevance scores reweight reference supervision for training a lightweight context-conditioned adapter. To evaluate the effectiveness and generality of CMP, we instantiate it with both Adversarial Motion Priors and Score-Matching Motion Priors. Across five humanoid control tasks, CMP consistently improves task performance and sample efficiency, learns meaningful context-motion alignment, and remains robust to imbalanced reference distributions. These results show that adapting motion priors to task contexts provides more relevant guidance for humanoid policy learning.

</details>

---

### [[20_Research/Papers/强化学习/PFM-HR_Pose_Flow_Matching_for_Humanoid_Robots|PFM-HR: Pose Flow Matching for Humanoid Robots]]

![[assets/2608.03227_figure.png|800]]

- **arXiv**: [2608.03227](https://arxiv.org/abs/2608.03227)
- **PDF**: https://arxiv.org/pdf/2608.03227
- **详细分析**: [[20_Research/Papers/强化学习/PFM-HR_Pose_Flow_Matching_for_Humanoid_Robots|PFM-HR: Pose Flow Matching for Humanoid Robots]]
- **作者**: Yukang Gao, Yi Gu, Yangchen Zhou, Xingyu Chen, Zhaorui Wang, Fanghai Zhang, Hanyang Cao, Zhengyang Shen, Ji Ma, Runhan Zhang, Lei Han, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《PFM-HR: Pose Flow Matching for Humanoid Robots》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion priors improve reinforcement learning for physics-based humanoid tracking, but temporal priors require ordered motion clips, while pose priors provide limited guidance for policy-induced pose transitions. We present Pose Flow Matching for Humanoid Robots (PFM-HR), a reusable flow matching prior trained directly on large scale unordered pose data. PFM-HR introduces the Pose Geometry Score (PGS), which quantifies how joint coordinate changes during rollouts align with the local geometry of pose variation captured by the prior. Using PGS to modulate the tracking reward guides policy exploration toward structured pose changes while keeping the prior frozen across tracking tasks. Experiments demonstrate that PFM-HR improves both single motion and general motion tracking, especially for highly dynamic motions.

</details>

---

### [[20_Research/Papers/机器人/Accelerating_Human-Aware_Robot_Trajectory_Generation_via_Diffusion_and_Consistency_Distillation|Accelerating Human-Aware Robot Trajectory Generation via Diffusion and Consistency Distillation]]

![[assets/2608.03159_figure.png|800]]

- **arXiv**: [2608.03159](https://arxiv.org/abs/2608.03159)
- **PDF**: https://arxiv.org/pdf/2608.03159
- **详细分析**: [[20_Research/Papers/机器人/Accelerating_Human-Aware_Robot_Trajectory_Generation_via_Diffusion_and_Consistency_Distillation|Accelerating Human-Aware Robot Trajectory Generation via Diffusion and Consistency Distillation]]
- **作者**: Byeong-Il Ham, Hyun-Bin Kim, Kyung-Soo Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Accelerating Human-Aware Robot Trajectory Generation via Diffusion and Consistency Distillation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PointNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This research proposes a constrained motion planning framework for robot manipulators in human-robot interaction (HRI). For a non-redundant manipulator with a fully specified end-effector pose, additional requirements such as collision avoidance and self-collision avoidance are difficult to handle as simple null-space secondary tasks. This limitation makes it challenging to generate feasible joint-space trajectories in HRI environments where safety and kinematic constraints must be considered simultaneously. To address this limitation, collision- and self-collision-aware trajectories are generated using Rapidly-exploring Random Tree (RRT) and RRT* algorithms, and the resulting dataset is used to train a diffusion model that generates constraint-satisfying trajectories through guided sampling. To reduce the inference time required for iterative diffusion sampling, consistency distillation is applied, and a joint-weighted jerk regularization term is incorporated into the loss function to promote smoother trajectories by penalizing abrupt changes in joint acceleration. Simulation results show that the consistency model generates 150 trajectory candidates in less than 100 ms, maintains a high episode success rate, and substantially reduces joint and end-effector jerk when jerk regularization is applied.

</details>

---

### [[20_Research/Papers/强化学习/Shooting_for_Contact_Contact-Implicit_Multiple_Shooting_for_Dynamic_Motion_Retargeting|Shooting for Contact: Contact-Implicit Multiple Shooting for Dynamic Motion Retargeting]]

![[assets/2608.03116_figure.png|800]]

- **arXiv**: [2608.03116](https://arxiv.org/abs/2608.03116)
- **PDF**: https://arxiv.org/pdf/2608.03116
- **详细分析**: [[20_Research/Papers/强化学习/Shooting_for_Contact_Contact-Implicit_Multiple_Shooting_for_Dynamic_Motion_Retargeting|Shooting for Contact: Contact-Implicit Multiple Shooting for Dynamic Motion Retargeting]]
- **作者**: Sergio A. Esteban, Jason H. K. Siu, Derrick Mach, Junheng Li, Vince Kurtz, Joel W. Burdick, Aaron D. Ames
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.1（加权：具身智能 0.6，强化学习 0.2，机器人 0.3）
- **关联关键词**: RL

#### 研究背景与动机

《Shooting for Contact: Contact-Implicit Multiple Shooting for Dynamic Motion Retargeting》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion retargeting approaches often prioritize kinematic similarity over whole-body dynamics, contact consistency, and actuation limits, yielding references that are difficult for reinforcement learning (RL) policies to reproduce, particularly for contact-rich behaviors. We present a contact-implicit, direct simulation-based multiple shooting (DSMS) framework that transforms kinematically feasible references into dynamically feasible whole-body trajectories. By embedding a differentiable simulator within a nonlinear program, DSMS resolves contact, friction, impacts, self-collision, and joint limits internally while enforcing tracking, actuation, and task constraints without prescribing a contact schedule or introducing explicit contact constraints. Compared with existing retargeting methods, DSMS accelerates motion-imitation RL training and yields policies with high success rates and low tracking error. We further demonstrate zero-shot sim-to-real transfer on the Unitree G1 through command-conditioned contact-rich crawling and a highly dynamic 180-degree jump-turn.

</details>

---

### [[20_Research/Papers/具身智能/How_Should_Vision-Language-Action_Models_Use_Proprioceptive_State|How Should Vision-Language-Action Models Use Proprioceptive State?]]

![[assets/2608.03052_figure.png|800]]

- **arXiv**: [2608.03052](https://arxiv.org/abs/2608.03052)
- **PDF**: https://arxiv.org/pdf/2608.03052
- **详细分析**: [[20_Research/Papers/具身智能/How_Should_Vision-Language-Action_Models_Use_Proprioceptive_State|How Should Vision-Language-Action Models Use Proprioceptive State?]]
- **作者**: Yiren Zhao, Ziyang Chen, Ziyang Rao, Pengteng Li, He Zhang, Weiyu Guo, Yandong Guo, Rushi Dai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《How Should Vision-Language-Action Models Use Proprioceptive State?》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent Vision-Language-Action (VLA) models almost universally take robot proprioceptive state as input, yet wire it in incompatible ways -- serialized into text prompts, projected into the vision-language prefix, or fed directly to the action expert -- and almost always as a single current frame. Three questions remain open: (1) whether, and on which tasks, current state actually improves closed-loop control; (2) how much state history helps, and whether its benefit reflects genuine temporal variation rather than added conditioning capacity; and (3) where state should enter the model -- the vision-language backbone or the action-generation module. We answer these questions through controlled experiments on a flow-matching VLA, fixing the backbone, training data, action representation, and evaluation protocol throughout. We implement five representative interfaces -- discrete state prompt, VLM prefix, action prefix, state expert, and feature modulation -- under matched implementation details, and evaluate them on 45 atomic tasks spanning three task families plus 20 composite tasks; we then sweep the state-history length from 1 to 96 frames to examine how historical state information affects model performance. The experiments yield systematic answers to all three questions, distilled into testable design principles for state-aware VLAs.

</details>

---

### [[20_Research/Papers/机器人/Forbidden_Region_Dynamic_Active_Constraints_in_Robot-Assisted_Minimally_Invasive_Surgery|Forbidden Region Dynamic Active Constraints in Robot-Assisted Minimally Invasive Surgery]]

![[assets/2608.03010_figure.jpg|800]]

- **arXiv**: [2608.03010](https://arxiv.org/abs/2608.03010)
- **PDF**: https://arxiv.org/pdf/2608.03010
- **详细分析**: [[20_Research/Papers/机器人/Forbidden_Region_Dynamic_Active_Constraints_in_Robot-Assisted_Minimally_Invasive_Surgery|Forbidden Region Dynamic Active Constraints in Robot-Assisted Minimally Invasive Surgery]]
- **作者**: Zejian Cui, Ferdinando Rodriguez y Baena
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Forbidden Region Dynamic Active Constraints in Robot-Assisted Minimally Invasive Surgery》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robot-assisted surgery, Forbidden Region Active Constraints (FRAC) represent a control strategy that helps maintain task safety by generating anisotropic haptic guidance to surgeons. However, several challenges need to be overcome before FRAC can benefit teleoperative surgery in a clinical setting. These challenges include the ability to allow for dynamic tissue deformation, maintain energetic passivity, and speed of implementation, among others. In this study, we propose the pipeline design for an energy dissipative FRAC strategy, which accommodates the dynamic tissue deformation caused by respiratory movements, by utilizing a depth sensing camera. The proposed FRAC strategy adopts a fine mesh representation, with a total number of 122,806 polygons in the case study presented, while running at 43.48Hz. We designed in vitro trajectory tracking experiments conducted by a "virtual" surgeon to aid quantitative assessment of the method, including its effectiveness in maintaining task safety, which was confirmed by successfully maintaining a pre-defined safety distance across all trials. We also conducted comparative studies to investigate the robustness and time-efficiency of our method against other FRAC methods that rely on simple geometry AC representations. We demonstrate that our method provides a more robust and effective guidance overall, while maintaining comparable, if not lower, time costs.

</details>

---

### [[20_Research/Papers/具身智能/A_Wearable_Stiffness-Rendering_Haptic_Device_with_a_Honeycomb_Jamming_Mechanism_for_Bilateral_Teleoperation|A Wearable Stiffness-Rendering Haptic Device with a Honeycomb Jamming Mechanism for Bilateral Teleoperation]]

![[assets/2608.03002_first_page.png|800]]

- **arXiv**: [2608.03002](https://arxiv.org/abs/2608.03002)
- **PDF**: https://arxiv.org/pdf/2608.03002
- **详细分析**: [[20_Research/Papers/具身智能/A_Wearable_Stiffness-Rendering_Haptic_Device_with_a_Honeycomb_Jamming_Mechanism_for_Bilateral_Teleoperation|A Wearable Stiffness-Rendering Haptic Device with a Honeycomb Jamming Mechanism for Bilateral Teleoperation]]
- **作者**: Thomas M. Kwok, Bohan Zhang, Wai Tuck Chow
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《A Wearable Stiffness-Rendering Haptic Device with a Honeycomb Jamming Mechanism for Bilateral Teleoperation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper addresses the challenge of providing kinesthetic feedback in bilateral teleoperation by designing a wearable, lightweight (20 g), and compact haptic device, the HJ-Haptic, utilizing a honeycomb jamming mechanism for object stiffness rendering. The HJ-Haptic device can vary its stiffness, from 1.15 N/mm to 2.64 N/mm, using a 30 kPa vacuum pressure. We demonstrate its implementation in a teleoperation framework, enabling operators to adjust grip force based on a reliable haptic feedback on object stiffness. A three-point flexural test on the honeycomb jamming mechanism and teleoperated object-grasping tasks were conducted to evaluate the device's functionality. Our experiments demonstrated a small RMSE and strong correlations in teleoperated motion, stiffness rendering, and interaction force feedback. The HJ-Haptic effectively adjusts its stiffness in response to real-time gripper feedback, mimicking the sensation of direct object grasping with hands. The device's use of vacuum pressure ensures operator safety by preventing dangerous outcomes in case of gas leakage or material failure. Incorporating the HJ-Haptic into the teleoperation framework provided the reliable perception of object stiffness and stable teleoperation. This study highlights the potential of the honeycomb jamming mechanism for enhancing haptic feedback in various applications, including teleoperation scenarios, as well as interactions with extended-reality environments.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedVAE_Disentangled_Video_VAE_for_Efficient_and_Controllable_Embodied_Manipulation|EmbodiedVAE: Disentangled Video VAE for Efficient and Controllable Embodied Manipulation]]

![[assets/2608.02990_figure.png|800]]

- **arXiv**: [2608.02990](https://arxiv.org/abs/2608.02990)
- **PDF**: https://arxiv.org/pdf/2608.02990
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedVAE_Disentangled_Video_VAE_for_Efficient_and_Controllable_Embodied_Manipulation|EmbodiedVAE: Disentangled Video VAE for Efficient and Controllable Embodied Manipulation]]
- **作者**: Jiayi Luo, Hanxin Zhu, Chen Gao, Jiankun Wang, Cong Wang, Tianyu He, Jianxin Li, Zhibo Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.7（加权：具身智能 1.8，世界模型 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《EmbodiedVAE: Disentangled Video VAE for Efficient and Controllable Embodied Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRASim, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent diffusion models (LDMs) have recently significantly advanced embodied learning in constructing powerful embodied manipulation world models. However, despite the remarkable performance, existing LDMs predominantly rely on Variational Autoencoders (VAEs) optimized for natural scenes while failing to account for the unique characteristics of embodied manipulation scenarios, yielding latent representations that are neither compact nor controllable, thereby hindering efficient training of LDMs and precise robotic control. To solve this problem, we present EmbodiedVAE, a novel video VAE that provides compact yet controllable latent representations tailored for the robotic manipulation world models. Specifically, EmbodiedVAE adopts a dual-encoder, single-decoder architecture with an asymmetric spatio-temporal compression module, which automatically disentangles the robot arm's motion from background environment, resulting in overall compactness while providing explicit embodied latent to support fine-grained action control. To further preserve the temporal consistency of learned robotic motion latent, we introduce an optimal-transport-based consistency module that explicitly enforces motion fidelity and inter-frame coherence. Extensive experiments demonstrate that our proposed EmbodiedVAE achieves superior reconstruction quality with high compression rate, while enabling more precise action control in robotic manipulation scenarios with an average of 2dB PSNR improvement over state-of-the-art video VAEs.

</details>

---

### [[20_Research/Papers/机器人/DeRP_An_Algorithm_for_Self-Assembly_of_Power-Delivery_Networks_using_Recursive_Branching_in_Information-Limited_Environments|DeRP: An Algorithm for Self-Assembly of Power-Delivery Networks using Recursive Branching in Information-Limited Environments]]

![[assets/2608.02904_figure.png|800]]

- **arXiv**: [2608.02904](https://arxiv.org/abs/2608.02904)
- **PDF**: https://arxiv.org/pdf/2608.02904
- **详细分析**: [[20_Research/Papers/机器人/DeRP_An_Algorithm_for_Self-Assembly_of_Power-Delivery_Networks_using_Recursive_Branching_in_Information-Limited_Environments|DeRP: An Algorithm for Self-Assembly of Power-Delivery Networks using Recursive Branching in Information-Limited Environments]]
- **作者**: Mohammadali Rashidioun, Sangwoo Park, Petras Swissler
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《DeRP: An Algorithm for Self-Assembly of Power-Delivery Networks using Recursive Branching in Information-Limited Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Delivering sustained power to distributed equipment in unstructured field environments using pre-planned wired networks or battery-based solutions presents significant infrastructure and logistics challenges. This paper presents Dendritic Recursive Pivoting (DeRP), a decentralized framework for multi-target network formation in robot swarms based solely on local communication and bearing-based sensing toward sinks. We envision a system in which robots, acting as a conduit, self-assemble a power network from a common source, forming branches at locally selected pivot points that approximate the Steiner points of Steiner trees to efficiently route to multiple Sinks. This branching operation is performed recursively to enable scalable and adaptive network formation without global planning. The proposed method is evaluated in terms of the total network length and estimated power loss, and is quantitatively compared against global baselines such as the Minimum Spanning Tree and Steiner tree solutions (GeoSteiner), which require complete knowledge of Sink locations. Specifically, we found that the networks formed by DeRP asymptotically form approximately 125\% of the global minimum length while reducing power losses to 65\% relative to Euclidean Steiner trees. In addition, we empirically characterize scaling behavior by measuring simulation completion time as the number of Sinks and robots increases, and find that this scaling was sub-linear for up to 100 sinks. The proposed approach enables resilient, adaptive power delivery in environments where deployment of traditional infrastructure is challenging.

</details>

---

### [[20_Research/Papers/机器人/Contact-Driven_Localization_in_a_Freeform_Robotic_Self-Assembled_Structure|Contact-Driven Localization in a Freeform Robotic Self-Assembled Structure]]

![[assets/2608.02895_figure.png|800]]

- **arXiv**: [2608.02895](https://arxiv.org/abs/2608.02895)
- **PDF**: https://arxiv.org/pdf/2608.02895
- **详细分析**: [[20_Research/Papers/机器人/Contact-Driven_Localization_in_a_Freeform_Robotic_Self-Assembled_Structure|Contact-Driven Localization in a Freeform Robotic Self-Assembled Structure]]
- **作者**: Mohammadali Rashidioun, Michael Sosa, Petras Swissler
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Contact-Driven Localization in a Freeform Robotic Self-Assembled Structure》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate localization remains a key challenge in swarm robotics, particularly for self-reconfigurable systems that must identify relative positions to form diverse structures. Most existing approaches rely on external tracking infrastructure or high-cost sensors, which limit scalability and deployment in unstructured environments. In this paper, we propose a novel contact-driven localization method for modular robots that leverages only local communication through binary contact information (whether two robots are physically connected or not). To exploit these contact cues, we introduce a virtual-force framework in which robots iteratively refine their poses attracting toward dock-connected neighbors and repelling from non-connected ones. The method requires no external infrastructure and relies only on minimal onboard sensing. Simulations show effective localization during the assembly of towers and cantilevers, enabling accurate, scalable, free-form self-assembly.

</details>

---

### [[20_Research/Papers/具身智能/Control_Barrier_Functions_via_Minkowski_Operations_for_Safe_Navigation_among_Polytopes|Control Barrier Functions via Minkowski Operations for Safe Navigation among Polytopes]]

![[assets/2608.02886_figure.png|800]]

- **arXiv**: [2608.02886](https://arxiv.org/abs/2608.02886)
- **PDF**: https://arxiv.org/pdf/2608.02886
- **详细分析**: [[20_Research/Papers/具身智能/Control_Barrier_Functions_via_Minkowski_Operations_for_Safe_Navigation_among_Polytopes|Control Barrier Functions via Minkowski Operations for Safe Navigation among Polytopes]]
- **作者**: Yi-Hsuan Chen, Shuo Liu, Wei Xiao, Calin Belta, Michael Otte
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Control Barrier Functions via Minkowski Operations for Safe Navigation among Polytopes》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safely navigating polytopic environments while respecting the dynamics, control, and exact geometry of the underlying system is a challenge in robotics. Control barrier functions (CBFs) synthesize safe control policies by rendering the safe set forward invariant, but many existing CBF-based methods approximate polytopes using conservative smooth shapes, such as spheres or ellipsoids, to obtain explicit differentiable distance functions. In this article, we propose an exact Signed Distance Function (SDF) formulation for a {\it polytopic} robot and {\it polytopic} obstacles and integrate it with nonsmooth CBFs. Leveraging Minkowski operations, the proposed method computes the exact SDF via companion convex programs in both the collision-free (positive-sign) and in-collision (negative-sign) cases. Furthermore, by exploiting the convenient geometric properties of 2D Minkowski operations and the optimality conditions of the two companion convex programs, we derive a unified analytical expression for the gradient of the exact SDF via sensitivity analysis. The exact rotational gradient further reveals a previously masked class of local minima induced by the coupling between geometry and nonholonomic kinematics. We demonstrate the effectiveness of the proposed framework through a pure-translation case and three scenarios with unicycle models involving recovery from an unsafe initialization and single- and multiple-obstacle avoidance. Comparisons with baseline methods highlight how the proposed framework enables non-conservative maneuvers and safety recovery.

</details>

---

### [[20_Research/Papers/具身智能/Biconvex_Optimization_for_Smooth_Minimum-Time_Trajectories_around_Convex_Obstacles|Biconvex Optimization for Smooth Minimum-Time Trajectories around Convex Obstacles]]

![[assets/2608.02834_figure.png|800]]

- **arXiv**: [2608.02834](https://arxiv.org/abs/2608.02834)
- **PDF**: https://arxiv.org/pdf/2608.02834
- **详细分析**: [[20_Research/Papers/具身智能/Biconvex_Optimization_for_Smooth_Minimum-Time_Trajectories_around_Convex_Obstacles|Biconvex Optimization for Smooth Minimum-Time Trajectories around Convex Obstacles]]
- **作者**: Peter Werner, Tobia Marcucci, Daniela Rus
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Biconvex Optimization for Smooth Minimum-Time Trajectories around Convex Obstacles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a biconvex approach for minimum-time motion planning around convex obstacles that is guaranteed to converge, is anytime, and supports derivative constraints to arbitrary order. We jointly convexify the minimum-time objective and all derivative constraints through a change of variables, and handle collision avoidance via time-varying separating planes, reducing the problem to a biconvex program. This program is solved by alternating between computing maximum-margin separating planes and optimizing the trajectory. By only adding planes for obstacles that the current iterate collides with, the trajectory can jump around obstacles and escape local minima. The method is guaranteed to converge starting from a simple collision-free polygonal curve. In our experiments on drone navigation and dual-arm bin unloading, we find that the proposed method reliably produces high-quality trajectories with computation times comparable to state-of-the-art decomposition-based motion planners, while handling a larger class of problems and being substantially more robust to bad initialization. Project page:https://wernerpe.github.io/bmtp-website/

</details>

---

### [[20_Research/Papers/具身智能/Staying_on_Spec_Real-Time_Monitoring_under_Uncertainty_with_a_Maritime_Case_Study|Staying on Spec: Real-Time Monitoring under Uncertainty with a Maritime Case Study]]

![[assets/2608.02811_first_page.png|800]]

- **arXiv**: [2608.02811](https://arxiv.org/abs/2608.02811)
- **PDF**: https://arxiv.org/pdf/2608.02811
- **详细分析**: [[20_Research/Papers/具身智能/Staying_on_Spec_Real-Time_Monitoring_under_Uncertainty_with_a_Maritime_Case_Study|Staying on Spec: Real-Time Monitoring under Uncertainty with a Maritime Case Study]]
- **作者**: Elizabeth Dietrich, Hanna Krasowski, Emir Cem Gezer, Roger Skjetne, Asgeir Johan Sørensen, Murat Arcak
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Staying on Spec: Real-Time Monitoring under Uncertainty with a Maritime Case Study》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic systems must operate under uncertainty while satisfying complex task and safety specifications. Monitoring such specifications under uncertainty remains challenging, as existing formulations typically require extensive data or explicit uncertainty distributions. In this paper, we propose a real-time monitoring framework that reduces data requirements by leveraging data-driven reachable sets for specification evaluation. We instantiate the framework for maritime navigation, where complex specifications arise from traffic rules. We develop a data-efficient pipeline for constructing reachable sets and derive a monitoring formulation suitable for real-time deployment. Simulation and hardware experiments demonstrate robust monitoring under realistic disturbances, achieving improved risk detection compared to state-of-the-art metrics.

</details>

---

### [[20_Research/Papers/具身智能/Toward_Certified_Functional_Safety_for_Industrial_Humanoid_Robots_The_Fail-Passive_Gap_and_a_Feasibility_Study|Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study]]

![[assets/2608.02809_figure.png|800]]

- **arXiv**: [2608.02809](https://arxiv.org/abs/2608.02809)
- **PDF**: https://arxiv.org/pdf/2608.02809
- **详细分析**: [[20_Research/Papers/具身智能/Toward_Certified_Functional_Safety_for_Industrial_Humanoid_Robots_The_Fail-Passive_Gap_and_a_Feasibility_Study|Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study]]
- **作者**: Caiwu Ding, Tao Cui, Lingyun Wang, Chengtao Wen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Toward Certified Functional Safety for Industrial Humanoid Robots: The Fail-Passive Gap and a Feasibility Study》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial humanoid robots are constrained less by locomotion or manipulation capability than by the immaturity of functional safety certification for legged platforms. The root difficulty is that the safe state of a legged robot is an actively-controlled state, which violates the fail-passive assumption underlying ISO~13849-1 / EN~60204-1: removing power from a walking biped causes an uncontrolled fall, so classical de-energization is itself a hazard. We term this the fail-passive gap and use a certified external safety chain (light curtain, emergency stop, fail-safe input, fail-safe PLC, and wireless PROFIsafe) as an instrument to locate it precisely: because the external chain is closed and quantifiable with established methods (PFHD, DC, CCF, PL/SILCL), the residual uncertifiable element is pinpointed to the robot-side reaction chain. Using a Siemens fail-safe S7-1500 emergency-stop reference, we show its certifiable Reaction subsystem is contactor-based power removal (Stop Category~0)---exactly the element a balancing humanoid cannot have. We deliberately do not claim end-to-end certified PL~e / SIL~3. We validate the approach on a Unitree G1 EDU pick-and-place cell in a 3m x 1.5m semi-enclosed workspace, and contribute a humanoid-specific analysis of the active safe state (fall-as-hazard, single-support stop bounds, balancing-policy residual risk, ISO~13855 separation) and a provenance-labeled timing budget. Hosting an industrial software-defined automation (SDA) controller on the robot, co-located with the balancing policy, moves robot-side PROFINET/PROFIsafe reception onto a standardized IEC~61131-3 interface; because the G1's onboard compute is not safety-rated hardware, this endpoint is not a certified safety runtime, which reinforces rather than resolves the fail-passive gap and localizes it to the SDA-to-balancing-policy interface.

</details>

---

### [[20_Research/Papers/具身智能/Light-Loco-Parkour_Versatile_Perceptive_Whole-Body_Locomotion_via_Multi-Skill_Distillation|Light-Loco-Parkour: Versatile Perceptive Whole-Body Locomotion via Multi-Skill Distillation]]

![[assets/2608.02653_figure.jpg|800]]

- **arXiv**: [2608.02653](https://arxiv.org/abs/2608.02653)
- **PDF**: https://arxiv.org/pdf/2608.02653
- **详细分析**: [[20_Research/Papers/具身智能/Light-Loco-Parkour_Versatile_Perceptive_Whole-Body_Locomotion_via_Multi-Skill_Distillation|Light-Loco-Parkour: Versatile Perceptive Whole-Body Locomotion via Multi-Skill Distillation]]
- **作者**: Hongming Chen, Zhuoran Li, Hongxi Wang, Jiangpeng Hu, Ziliang Li, Peize Liu, QingRui Zhao, Xuhao Liu, Liang Pan, Ximin Lyu, Yuntao Ma, Tingxiang Fan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Light-Loco-Parkour: Versatile Perceptive Whole-Body Locomotion via Multi-Skill Distillation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing humanoid whole-body control systems still fall short of the way humans move through cluttered terrain: they either track expressive whole-body references without terrain generalization, or react to terrain online while leaving the arms, torso, and knees largely unused. We present \texttt{Light-Loco-Parkour} (LLP), an end-to-end perceptive whole-body locomotion system that closes this gap with a single deployable policy. Conditioned only on onboard depth and a velocity command, the policy decides when to walk, balance, climb, step down, or vault, with no reference input, skill label, hand-coded gate, or runtime motion graph. Compared with prior humanoid systems, LLP makes three contributions. First, it introduces a whole-body perceptive-control pipeline that extends an RL-trained, velocity-tracking locomotion policy with parkour skills learned from object-interacting motions, so the same policy tracks velocity in open terrain, executes whole-body traversal at obstacles, and resumes locomotion afterward. Second, it acquires terrain-conditioned skills from sparse seeds by expanding a single motion into dynamically feasible, terrain-paired references across obstacle geometry, rather than relying on a large motion corpus. Third, it learns autonomous skill transitions from reward, letting the policy decide when and which whole-body skill to invoke from depth and command alone, with no one-hot skill label, hand-coded state machine, or runtime motion generator. Simulation and real-world experiments show high success across both benchmarked terrains and unseen obstacle variations, and the same policy transfers zero-shot to indoor and outdoor hardware experiments. These results demonstrate autonomous perceptive whole-body locomotion on a humanoid in outdoor settings, using only onboard sensing and a single deployable policy.

</details>

---
