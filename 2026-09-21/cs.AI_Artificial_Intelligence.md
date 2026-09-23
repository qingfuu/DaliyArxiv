# cs.AI | Artificial Intelligence | 2026-09-21

#arxiv #ComputerScience

**论文数**: 19

### [[20_Research/Papers/大模型/Bayesian_Belief_Layer_for_Controllable_Opinion_Dynamics_in_LLM_Agents|Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents]]

![[assets/2609.21997_figure.png|800]]

- **arXiv**: [2609.21997](https://arxiv.org/abs/2609.21997)
- **PDF**: https://arxiv.org/pdf/2609.21997
- **详细分析**: [[20_Research/Papers/大模型/Bayesian_Belief_Layer_for_Controllable_Opinion_Dynamics_in_LLM_Agents|Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents]]
- **作者**: Hafsa Akbar, Daniel Platnick, Marjan Alirezaie, Hossein Rahnama
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Bayesian Belief Layer for Controllable Opinion Dynamics in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents in social simulation revise their opinions implicitly, in context: how open an agent is to persuasion can neither be specified nor verified, and collective outcomes inherit the model's training prior. We introduce Bayesian Chronicle Agents (BCA), a minimal belief layer separating \emph{what} an agent believes from \emph{how} it speaks. Each stance is a probability, updated by one Bayesian step per utterance heard. A single prior-strength parameter $\kappa$ encodes stubbornness, modeled after its role in Friedkin--Johnsen (FJ) opinion dynamics. We then sweep this parameter to yield three canonical regimes of opinion dynamics on demand (consensus, persistent disagreement, committed-minority influence), with persistent disagreement matching the FJ closed-form fixed points at $R^2\!=\!0.93$--$0.99$. We further show that prescribed $\kappa$ remains recoverable after the language round-trip, with perfect rank-order recovery across all four models. Explicit belief also makes simulation auditable: the layer surfaces systematic per-model stance biases that end-to-end simulation would silently absorb.

</details>

---

### [[20_Research/Papers/强化学习/When_Should_a_Failing_Robot_Ask_Initiating_Corrective_Human-Robot_Dialogue_from_Audited_Sensor_Evidence|When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence]]

![[assets/2609.21942_figure.png|800]]

- **arXiv**: [2609.21942](https://arxiv.org/abs/2609.21942)
- **PDF**: https://arxiv.org/pdf/2609.21942
- **详细分析**: [[20_Research/Papers/强化学习/When_Should_a_Failing_Robot_Ask_Initiating_Corrective_Human-Robot_Dialogue_from_Audited_Sensor_Evidence|When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence]]
- **作者**: Eshika Pathak, Leela Krishna
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《When Should a Failing Robot Ask? Initiating Corrective Human-Robot Dialogue from Audited Sensor Evidence》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot that fails at a task faces the first decision in corrective dialogue: act on its own diagnosis, consult another onboard sensor, or interrupt a person. Choosing well requires knowing how much the robot's sensors reveal about the cause and how reliable the robot's own diagnosis is. We build a simulated benchmark in which every failure's true cause is known, because we injected it, and measure what each sensor reveals, with explicit checks against data leakage. Some failures are diagnosable from camera images; others only from the robot's force data (0.99 from force data, no image method above 0.55). We then test six open vision-language models. Their behavior tracks the surface of the prompt, not the evidence: moving the refusal option from last to first in the answer list collapses refusal rates from 78-100% to 0-6% in three of the six swept model-and-family pairs. Accuracy from frames stays at or below a majority-class baseline under every prompt variant, with or without worked examples, and stated confidence carries no information about correctness. Handing the same models the force data as ten lines of text produces the first above-baseline diagnoses, in four of the six models: much of the failure reflects missing sensor data, not missing ability. We pose the choice as a three-action decision problem, act, consult your own sensors, or ask a human, whose optimal policy follows from measured accuracy. The models do not follow it, and their ask rates ignore a fourfold change in question cost. One question to a human still lifts them from that baseline to roughly the answerer's own reliability (0.70-0.81 when they ask). The decision to ask should be tied to measured accuracy and stated costs, not to the model's confidence.

</details>

---

### [[20_Research/Papers/具身智能/Touvigation_Embodied_Adaptive_Object_Acquisition_for_Blind_and_Low-Vision_Users_in_Unfamiliar_Indoor_Environments|Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments]]

![[assets/2609.21828_figure.png|800]]

- **arXiv**: [2609.21828](https://arxiv.org/abs/2609.21828)
- **PDF**: https://arxiv.org/pdf/2609.21828
- **详细分析**: [[20_Research/Papers/具身智能/Touvigation_Embodied_Adaptive_Object_Acquisition_for_Blind_and_Low-Vision_Users_in_Unfamiliar_Indoor_Environments|Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments]]
- **作者**: George Xi Wang, Xiangyu Li, Shaoyue Wen, Jiaqian Hu, Junan Xie, Yupeng Wang, Ziyue Shi, Qijun Chen, Maaike Bouwmeester, Yuhua Jin, Jing Qian
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Multimodal, EmbodiedAI, Systems

#### 研究背景与动机

《Touvigation: Embodied Adaptive Object Acquisition for Blind and Low-Vision Users in Unfamiliar Indoor Environments》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Blind and low-vision users often face challenges when locating and physically acquiring objects in unfamiliar indoor environments. Existing vision-language-model-based assistants can provide semantic descriptions but may introduce latency, hallucinations, and guidance that is poorly aligned with embodied action. We present Touvigation, a hands-free object acquisition system that combines vision-language understanding with persistent local spatial modeling to provide low-latency, body-relative guidance. Drawing on formative interviews with eight blind and low-vision participants, we design a multi-stage guidance framework that adapts spatial references as users transition from orienting, to walking, to reaching and tactile verification. We evaluated Touvigation with 12 blind and low-vision participants against a multimodal large-language-model assistant and unassisted search. Touvigation achieved 100% task success, compared with 58% for the multimodal assistant and 85% for unassisted search, while reducing completion time and cognitive workload. Our findings demonstrate how persistent spatial grounding and adaptive embodied guidance can improve object acquisition for blind and low-vision users.

</details>

---

### [[20_Research/Papers/具身智能/ForceTwin_Physics-informed_Digital_Twins_for_Robotic_Manipulation_from_Instrumented_Human_Interaction|ForceTwin: Physics-informed Digital Twins for Robotic Manipulation from Instrumented Human Interaction]]

![[assets/2609.21751_figure.png|800]]

- **arXiv**: [2609.21751](https://arxiv.org/abs/2609.21751)
- **PDF**: https://arxiv.org/pdf/2609.21751
- **详细分析**: [[20_Research/Papers/具身智能/ForceTwin_Physics-informed_Digital_Twins_for_Robotic_Manipulation_from_Instrumented_Human_Interaction|ForceTwin: Physics-informed Digital Twins for Robotic Manipulation from Instrumented Human Interaction]]
- **作者**: Tim Engelbracht, René Zurbrügg, Mayank Mittal, Marco Hutter, Marc Pollefeys, Hermann Blum, Zuria Bauer
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，世界模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《ForceTwin: Physics-informed Digital Twins for Robotic Manipulation from Instrumented Human Interaction》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-to-Sim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulating objects requires understanding not only their motion, but also the physical properties that determine it. For articulated objects, these include inertia, friction, and mechanisms such as springs or door closers, whose effects can vary with configuration and velocity. Such properties are not directly observable from appearance: visually identical doors may require very different effort to manipulate. Existing digital-twin pipelines recover primarily kinematics or assign static physical parameters from visual and language priors, which can yield physically implausible estimates. As a result, state-dependent mechanism dynamics remain unidentified and are not represented in standard asset formats. We present ForceTwin, a system for identifying physics-informed digital twins of articulated objects from instrumented human interaction. A person probes an object using a handheld force-sensing gripper, providing synchronized poses and interaction forces from which we estimate the articulation, parametric dynamics including inertia, Coulomb friction, viscous damping, and a structured neural residual capturing state-dependent mechanism forces. ForceTwin nearly halves the inertial-parameter error of a VLM prior. As a feedforward dynamics model for impedance control on a Spot and a Franka FR3, ForceTwin achieves 87% goal completion across nine object-embodiment pairs, compared with 60% using VLM-prior and 57% using kinematics-only twins, with the largest gains on objects whose strong mechanisms cause both baselines to stall. We further use the identified twins to train whole-body door-traversal policies and deploy them in the real world. Project Page: this https URL

</details>

---

### [[20_Research/Papers/具身智能/Outcome-Conditioned_End-Effector_Geometry_Across_Vision-Language-Action_Policies|Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies]]

![[assets/2609.21659_first_page.png|800]]

- **arXiv**: [2609.21659](https://arxiv.org/abs/2609.21659)
- **PDF**: https://arxiv.org/pdf/2609.21659
- **详细分析**: [[20_Research/Papers/具身智能/Outcome-Conditioned_End-Effector_Geometry_Across_Vision-Language-Action_Policies|Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies]]
- **作者**: Xingyu Lin, Zhuang Li, Zhongrun Wu, Shouquan Zhou, Dehui Du
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Outcome-Conditioned End-Effector Geometry Across Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, RoboEval, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies solve the same manipulation task through different action interfaces, but task success alone does not establish whether their physical executions agree. We study cross-policy end-effector geometry in 15,000 closed-loop LIBERO rollouts from four policies. The primary clean-condition analysis forms 3,600 configuration-matched, and therefore dependent, policy pairs. Both-success pairs have a median normalized dynamic time warping distance of 0.0120 m versus 0.0380 m when exactly one policy succeeds. This ordering holds in every task, every policy pair, and nine sampling and band-limited representations; however, the ratio varies severalfold across representations, so we report the direction rather than a fixed multiple. Both-failure pairs are more separated again but rest on thin, uneven support, so we report them as exploratory. Within successful executions, partner replacements separate more across tasks than across initial states. A matched baseline still reveals measurable, heterogeneous residual policy differences, so a low cross-policy distance does not imply interchangeability. Successful executions sit about as far from same-task demonstrations as those demonstrations sit from each other, compatible with task-associated geometry without separating training-data overlap from task constraints. A common 72-action window preserves the ordering but reduces its magnitude; endpoint and duration adjustment likewise leaves a positive mixed-outcome coefficient relative to both-success pairs, though its magnitude is specification-dependent. Under composite visual stress, policy rankings and pair composition change together.

</details>

---

### [[20_Research/Papers/具身智能/SynthDemo-RL_Breaking_the_Zero-Reward_Barrier_in_VLA_Adaptation_with_LLM-Guided_Synthetic_Demonstrations|SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations]]

![[assets/2609.21650_figure.png|800]]

- **arXiv**: [2609.21650](https://arxiv.org/abs/2609.21650)
- **PDF**: https://arxiv.org/pdf/2609.21650
- **详细分析**: [[20_Research/Papers/具身智能/SynthDemo-RL_Breaking_the_Zero-Reward_Barrier_in_VLA_Adaptation_with_LLM-Guided_Synthetic_Demonstrations|SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations]]
- **作者**: Hiroaki Kingetsu, Hiroaki Kurihara, Kaoru Yokoo, Kenji Fukumizu, Manohar Kaul
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.8，大模型 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《SynthDemo-RL: Breaking the Zero-Reward Barrier in VLA Adaptation with LLM-Guided Synthetic Demonstrations》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLinf-VLA, SimpleVLA-RL, SynthDemo-RL, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-tuning Vision-Language-Action (VLA) models commonly relies on human teleoperation demonstrations, while reinforcement learning (RL) with sparse binary rewards faces an exploration challenge when successful trajectories are rarely sampled. We propose SynthDemo-RL, a teacher-student framework in which an automated teacher converts simulator-privileged state into successful manipulation trajectories, a VLA student is distilled from them by supervised fine-tuning (SFT), and PPO with binary task-success rewards refines the student. We study reward coverage, the fraction of tasks for which at least one success is observed under the fixed evaluation protocol, as a complement to the average success rate. On LIBERO-PRO, a public benchmark of perturbed LIBERO tasks for which no demonstrations exist, 27 of 57 scored tasks are at exactly 0% success for a pi_0.5 policy fine-tuned on the original LIBERO tasks. Direct PPO from this policy, under the same PPO recipe and the same RL compute as SynthDemo-RL's refinement stage, rescues 10 of these 27 tasks and leaves 17 at 0%. SynthDemo-RL, with 50 synthesized trajectories per task and no new human demonstrations, rescues all 27 and reaches average success rates of 97.8% and 97.1% on the Position and Task axes of LIBERO-PRO, respectively. On standard LIBERO, the same pipeline reaches 96.0% with no human demonstrations, within 1.7 points of pi_0.5 trained on 50 human demonstrations per task. We further validate the pipeline on RoboTwin 2.0 and verify that trajectories from a policy trained in a MuJoCo twin execute open-loop on a physical robot.

</details>

---

### [[20_Research/Papers/具身智能/Potential-Field_Action_Representation_for_Reinforcement_Learning_in_Contact-Rich_Manipulation|Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2609.21609](https://arxiv.org/abs/2609.21609)
- **PDF**: https://arxiv.org/pdf/2609.21609
- **详细分析**: [[20_Research/Papers/具身智能/Potential-Field_Action_Representation_for_Reinforcement_Learning_in_Contact-Rich_Manipulation|Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation]]
- **作者**: Xinyu Liu, Gökhan Solak, Arash Ajoudani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.8，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Potential-Field Action Representation for Reinforcement Learning in Contact-Rich Manipulation》归入 强化学习、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-free reinforcement learning can acquire contact-rich robotic manipulation skills through trial-and-error interaction, but it often requires the policy to learn both task strategy and low-level motion generation. In this setting, the action representation is critical because it determines how policy outputs are converted into robot motion, shaping both exploration and physical execution. Direct Cartesian command interfaces require the policy to generate motion at every decision step, coupling task-level adaptation with continuous low-level control and increasing the learning burden. We propose PA-RL, a reinforcement-learning framework that uses artificial potential fields as the action representation. Instead of commanding motion directly, the policy adapts the parameters of an energy-like potential field, which generates a state-dependent guidance direction executed through a Cartesian impedance controller. We evaluate PA-RL on peg-in-hole insertion, a representative contact-rich task with nonlinear dynamics and discontinuous contact transitions. In simulation, PA-RL is compared with Cartesian velocity, Cartesian pose, and variable-impedance action spaces using the same RL algorithm. PA-RL is the only method to reach a 100% evaluation success rate within the allotted training time, while the best baseline reaches 92.6%. It also reduces joint-torque variation by 55.4% and Cartesian acceleration variation by 70.8% relative to the best baseline, without explicit motion-quality penalties in the reward. The simulation-trained policy further completes 9/9 real-robot insertions without fine-tuning, demonstrating the deployment feasibility of the learned potential-field interface.

</details>

---

### [[20_Research/Papers/大模型/OneBid_A_Unified_Auto-Bidding_Foundation_Model_for_Diverse_oCPX_Advertising_Scenarios|OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2609.21550](https://arxiv.org/abs/2609.21550)
- **PDF**: https://arxiv.org/pdf/2609.21550
- **详细分析**: [[20_Research/Papers/大模型/OneBid_A_Unified_Auto-Bidding_Foundation_Model_for_Diverse_oCPX_Advertising_Scenarios|OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios]]
- **作者**: Yewen Li, Peng Jiang, Yitian Li, Pengfei Lv, Xialong Liu, Peng Jiang, Qingpeng Cai
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《OneBid: A Unified Auto-Bidding Foundation Model for Diverse oCPX Advertising Scenarios》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Auto-bidding is central to computational advertising, where strategies must maximize advertisers' conversion value under economic constraints. It has evolved from rule-based controllers to reinforcement learning and generative methods such as Decision Transformer (DT). Yet these methods increasingly mismatch the prevailing optimized cost-per-X (oCPX) paradigm, which spans heterogeneous scenarios (e.g., registration, purchase), each served by a separate model, leading to fragmented pipelines and underexploring cross-scenario modeling. Inspired by foundation models like LLMs, unifying these oCPX scenarios into one model raises three challenges: multi-objective control, scalable capacity under strict latency, and safe offline policy improvement. We present OneBid, a unified auto-bidding foundation model that learns a reusable backbone from heterogeneous oCPX logs and adapts it to scenario-specific deployments via offline post-training. Building on DT, OneBid extends single Return-to-Go conditioning to two atomic signals, Return-to-Go for conversion value and Cost-to-Go for cost ratio, plus value-aware regularization on next-action prediction. To absorb distributional heterogeneity, we design a sequence-level Mixture-of-Experts architecture, where shared experts encode cross-scenario knowledge and sparsely-routed experts capture scenario-specific patterns at low latency, yielding consistent scaling with model size and data. During post-training, we align the backbone with scenario preferences via Critic-guided Relative Offline Policy optimization (CROP): a learned critic scores candidate actions group-relatively, avoiding the unsafe online exploration of GRPO-style fine-tuning while constraining policy shift to reduce OOD risk. Validated via online A/B tests and fully deployed at Kuaishou, OneBid delivers an overall +2.2% ADVV gain on oCPX Ads, peaking at +13.1% in the ROAS scenario.

</details>

---

### [[20_Research/Papers/强化学习/2nd_Place_Solution_to_the_HANDS_2026_Workshop_Challenge-Dexterous_Grasp_Motion_Track_Single-Shot_Trajectory_Warping_for_Grasp_Motion_Generat|2nd Place Solution to the HANDS 2026 Workshop Challenge-Dexterous Grasp Motion Track: Single-Shot Trajectory Warping for Grasp Motion Generation]]

![[assets/2609.21511_figure.png|800]]

- **arXiv**: [2609.21511](https://arxiv.org/abs/2609.21511)
- **PDF**: https://arxiv.org/pdf/2609.21511
- **详细分析**: [[20_Research/Papers/强化学习/2nd_Place_Solution_to_the_HANDS_2026_Workshop_Challenge-Dexterous_Grasp_Motion_Track_Single-Shot_Trajectory_Warping_for_Grasp_Motion_Generat|2nd Place Solution to the HANDS 2026 Workshop Challenge-Dexterous Grasp Motion Track: Single-Shot Trajectory Warping for Grasp Motion Generation]]
- **作者**: Muneeb A. Khan, Woojin Kim, Shinwoo Kim, Muhammad Munsif, Binod Bhattarai, Seungryul Baek
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《2nd Place Solution to the HANDS 2026 Workshop Challenge-Dexterous Grasp Motion Track: Single-Shot Trajectory Warping for Grasp Motion Generation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This report describes our 2nd place solution to the HANDS 2026 workshop challenge (Dexterous Grasp Motion track) in conjunction with ECCV 2026. In this challenge, we address grasp motion generation for the 12-DoF LinkerHand O6, aiming to produce physically plausible reach-and-lift trajectories for unseen objects from randomized initial hand poses in simulation. This task is particularly challenging because each grasp requires a per-step policy to make approximately $70$ twelve-dimensional decisions, with errors accumulating over time, while test objects and physical dynamics may differ from those encountered during training. To address these challenges, we propose editing a single successful GraspM3 demonstration instead of generating the motion step by step: a policy observes the object once and outputs a 12-D warp of the demonstration, which is then replayed open-loop. Moreover, we train the warp policy with one-step PPO over all $4{,}824$ training objects in parallel. As a result, our method achieved success rates of $94.61\%$ on the easy track, the highest of all submissions, and $57.18\%$ on the hard track of the private test set.

</details>

---

### [[20_Research/Papers/具身智能/AtomEgo_Exploring_Ego-Robot_Integration_for_Embodied_Foundation_Model_Pretraining|AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining]]

![[assets/2609.21461_figure.png|800]]

- **arXiv**: [2609.21461](https://arxiv.org/abs/2609.21461)
- **PDF**: https://arxiv.org/pdf/2609.21461
- **详细分析**: [[20_Research/Papers/具身智能/AtomEgo_Exploring_Ego-Robot_Integration_for_Embodied_Foundation_Model_Pretraining|AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining]]
- **作者**: Di Wu, Dongchen Zheng, Junhe Sheng, Zhongxing Wei, Songxin Zhang, Zejian Xie, Xiaoquan Sun, Junyang Zheng, Zhuoyang Song, Jiaxing Zhang, Jiayu Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 1.5，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《AtomEgo: Exploring Ego-Robot Integration for Embodied Foundation Model Pretraining》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied foundation models are constrained by the limited scale and diversity of robot demonstrations, motivating the use of large-scale egocentric human interaction data. However, how to effectively incorporate such data into embodied-model pre-training remains unclear because of substantial embodiment and action-space gaps between humans and robots. We present AtomEgo, a systematic study of ego--robot co-training supported by a curated corpus of approximately 2,659 hours and a scalable data processing pipeline. Across vision--language--action and world--action model architectures, we investigate three representative paradigms: joint co-training with domain-specific action heads, progressive ego-to-robot transfer through embodiment alignment, and joint video--action modeling. We evaluate these paradigms through multi-task real-robot experiments and language-conditioned cross-embodiment representation analysis. Our results reveal a simple principle: Data Scale * Alignment Quality --&gt; Capability Gain; egocentric data can improve generalization, but their value depends on how effectively they are aligned and utilized. This principle can provide practical guidance for scalable ego--robot pre-training.

</details>

---

### [[20_Research/Papers/大模型/GVPO++_Group_Variance_Policy_Optimization_for_LLM_Post-Training_and_On-Policy_Distillation|GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation]]

![[assets/2609.21432_figure.jpg|800]]

- **arXiv**: [2609.21432](https://arxiv.org/abs/2609.21432)
- **PDF**: https://arxiv.org/pdf/2609.21432
- **详细分析**: [[20_Research/Papers/大模型/GVPO++_Group_Variance_Policy_Optimization_for_LLM_Post-Training_and_On-Policy_Distillation|GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation]]
- **作者**: Kaichen Zhang, Yuzhong Hong, Junwei Bao, Hongfei Jiang, Yang Song, Dingqian Hong, Hui Xiong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《GVPO++: Group Variance Policy Optimization for LLM Post-Training and On-Policy Distillation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training plays a pivotal role in enhancing the reasoning capabilities and task-specific expertise of large language models (LLMs). Despite recent advances in post-training methods, such as Group Relative Policy Optimization (GRPO), their practical deployment remains impeded by training instability arising from the reliance on importance sampling. We introduce Group Variance Policy Optimization (GVPO), a novel post-training method that integrates the analytical solution of KL-constrained reward maximization into its gradient weighting scheme. This formulation provides an intuitive interpretation: GVPO's gradient corresponds to the mean squared error between the central distance of implicit rewards and that of actual rewards. GVPO offers two key advantages: (1) it guarantees a unique optimal solution, exactly to the KL-constrained reward maximization objective, and (2) it enables flexible sampling distributions without requiring importance sampling. Beyond general post-training, we show that GVPO naturally extends to on-policy distillation (OPD). Furthermore, GVPO enables the optimization of a broad family of extended OPD objectives, providing a principled foundation for diverse objective design. By unifying theoretical guarantees with practical adaptability, GVPO establishes a new paradigm for reliable and versatile LLM post-training and on-policy distillation.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_with_Buffered_Quantile_Objectives|Deep Reinforcement Learning with Buffered Quantile Objectives]]

![[assets/2609.21327_first_page.png|800]]

- **arXiv**: [2609.21327](https://arxiv.org/abs/2609.21327)
- **PDF**: https://arxiv.org/pdf/2609.21327
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_with_Buffered_Quantile_Objectives|Deep Reinforcement Learning with Buffered Quantile Objectives]]
- **作者**: Mohammad Alipour-vaezi, Sajad Khodadadian
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Deep Reinforcement Learning with Buffered Quantile Objectives》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BQRL, Deep-BQRL, UCB-BQRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantile-based reinforcement learning provides an interpretable approach to risk-sensitive decision-making by optimizing a prescribed quantile of the cumulative-return distribution. Despite this appeal, learning under a point quantile objective is challenging: quantiles can change abruptly under small perturbations of the return distribution, and exact quantile-sensitive planning requires computationally demanding distributional optimization. Lower-buffered quantiles alleviate the former difficulty by averaging neighboring quantiles immediately below the target level, providing a smoother surrogate while preserving the underlying point-quantile objective. Existing methods based on this principle, however, remain model-based and rely on explicit return-law planning, limiting their applicability beyond small tabular problems. We develop Deep-BQRL, a model-free distributional reinforcement-learning framework that extends buffered-quantile learning to neural function approximation. The method learns conditional return quantiles directly from sampled transitions, constructs buffered action scores from the relevant region of the learned quantile function, and uses ensemble disagreement to guide exploration. An augmented input representation allows the learned policy to respond to trajectory information without explicitly reproducing the quantile-state recursion required by exact planning. Experiments on an asset-selling optimal-stopping problem and slippery FrozenLake compare Deep-BQRL with model-based UCB-BQRL and tabular PPO and TRPO implementations. In asset selling, Deep-BQRL attains smaller mean cumulative point-quantile policy gaps than PPO and TRPO at the reported target levels, while UCB-BQRL retains the smallest gaps. The learned stopping decisions also vary with the target quantile, providing an interpretable illustration of the method's risk-sensitive behavior.

</details>

---

### [[20_Research/Papers/具身智能/VLA-Scope_Shift-Aware_Failure_Prediction_for_Vision-Language-Action_Models|VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models]]

![[assets/2609.21246_figure.png|800]]

- **arXiv**: [2609.21246](https://arxiv.org/abs/2609.21246)
- **PDF**: https://arxiv.org/pdf/2609.21246
- **详细分析**: [[20_Research/Papers/具身智能/VLA-Scope_Shift-Aware_Failure_Prediction_for_Vision-Language-Action_Models|VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models]]
- **作者**: Kaiwen Zhu, Dongfang Liu, Liangkai Liu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.7，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《VLA-Scope: Shift-Aware Failure Prediction for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models map visual observations and natural-language instructions to robotic actions, but distribution shifts can compromise their reliability. Because these models may still succeed under out-of-distribution (OOD) conditions, detecting OOD inputs alone is insufficient to predict execution failure. In this paper, we introduce VLA-Scope, a two-stage framework that combines input-shift characterization with execution history to predict failure during OOD rollouts. The first stage uses pooled image and language representations to detect OOD inputs and classify their shift categories. For inputs flagged as OOD, the second stage combines the predicted category, action-prefix features, and execution progress features. A logistic regression model shared across shift categories updates failure risk as execution proceeds. We evaluate the framework with OpenVLA on ten LIBERO-Spatial tasks using leave-one-group-out cross-validation. OOD detection achieves a ROC-AUC of 0.9454, and shift classification achieves 91% accuracy. Evaluated independently of the OOD gate on all 1,400 OOD rollouts, the failure predictor achieves a ROC-AUC of 0.8497 after 60 executed actions, compared with 0.7906 without execution progress features. It also achieves a higher ROC-AUC than the evaluated ActProbe and SAFE-MLP baselines. These results suggest that combining action features with temporally aggregated execution step representations improves failure prediction under input shifts.

</details>

---

### [[20_Research/Papers/具身智能/KnowDemo_Knowledge-Guided_Robot_Demonstration_Generation_from_Human_Videos|KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos]]

![[assets/2609.21229_figure.png|800]]

- **arXiv**: [2609.21229](https://arxiv.org/abs/2609.21229)
- **PDF**: https://arxiv.org/pdf/2609.21229
- **详细分析**: [[20_Research/Papers/具身智能/KnowDemo_Knowledge-Guided_Robot_Demonstration_Generation_from_Human_Videos|KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos]]
- **作者**: Zhiyuan Gao, Yanxiang Zhan, Mohammad Khoshnazar, Jeroen Schäfer, Michael Beetz
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.6（加权：具身智能 0.9，大模型 0.4，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《KnowDemo: Knowledge-Guided Robot Demonstration Generation from Human Videos》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World, SplatSim, URL, X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning robot manipulation policies typically requires substantial demonstration data, which are costly to collect on real robots. Recent methods generate robot demonstrations from human videos by adapting recovered motion and validating the resulting trajectories in simulation. However, methods centered on motion-reference adaptation can limit behavioral diversity by retaining the demonstrated contact strategies and subtask orders, while insufficient understanding of task requirements and scene relations can reduce demonstration generation efficiency by generating invalid candidates. To address these limitations, we propose KnowDemo, a framework that uses structured manipulation knowledge from human videos to generate diverse robot demonstrations for a target workspace. To distinguish task requirements from demonstration-specific choices, we develop a knowledge extraction and reasoning module based on a vision-language model (VLM) that associates object and action descriptions with inferred task conditions, demonstration references, and permissible execution variations. To translate this knowledge into executable demonstrations, we resolve the descriptions against target-scene entities and geometry to guide candidate generation and screening before motion planning and simulation. The resulting demonstrations exhibit multimodal behavior through alternative contact strategies and valid subtask orders, with structured execution labels. Experiments demonstrate additional verified execution modes beyond a reference-only configuration and improved candidate planning success through task-guided grasp sampling. To validate the generated data for policy learning, we fine-tune the pretrained $\pi_{0.5}$ model on simulation data, achieving sim-to-real transfer across three tasks. Project page: this https URL

</details>

---

### [[20_Research/Papers/具身智能/FOCAL-VLA_Subtask-Guided_Geometry_Distillation_and_Implicit_World_Modeling_for_Vision-Language-Action_Models|FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision-Language-Action Models]]

![[assets/2609.21228_figure.png|800]]

- **arXiv**: [2609.21228](https://arxiv.org/abs/2609.21228)
- **PDF**: https://arxiv.org/pdf/2609.21228
- **详细分析**: [[20_Research/Papers/具身智能/FOCAL-VLA_Subtask-Guided_Geometry_Distillation_and_Implicit_World_Modeling_for_Vision-Language-Action_Models|FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision-Language-Action Models]]
- **作者**: Zhiyuan Gao, Di Wen, Yanxiang Zhan, Mohammad Khoshnazar, Jeroen Schäfer, Kunyu Peng, Michael Beetz
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《FOCAL-VLA: Subtask-Guided Geometry Distillation and Implicit World Modeling for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, CoWVLA, DreamVLA, FOCAL-VLA, LingBot-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models built on pretrained vision-language models have demonstrated strong performance across diverse robotic manipulation tasks. However, VLA models that directly map current 2D observations to actions often lack sufficient spatial and temporal understanding, limiting their performance in precise and long-horizon manipulation. Recent methods enhance VLA models through geometric supervision and future-state prediction across the entire scene. However, these methods can suffer from redundant scene information, distracting the model from learning the geometry and dynamics relevant to the current interaction. To address this issue, we propose FOCAL-VLA, a framework that combines subtask-guided geometry distillation with implicit world modeling to learn representations of current spatial structure and future interaction dynamics. To focus geometric learning on the current subtask, we transfer geometric knowledge from VGGT to the VLA model by aligning geometry latents with features from subtask-relevant image regions. To capture the future 3D evolution of the current interaction, we incorporate implicit world modeling using Track4World features from current and future demonstration frames. The two complementary representations jointly guide action generation without running VGGT or Track4World at inference time. Experiments show that FOCAL-VLA outperforms baselines on both simulation benchmarks and real-world manipulation tasks. Project website: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Fewer_Steps,_Better_Actions_Rethinking_Flow-Matching_Inference_for_VLA_Policies|Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies]]

![[assets/2609.21216_figure.png|800]]

- **arXiv**: [2609.21216](https://arxiv.org/abs/2609.21216)
- **PDF**: https://arxiv.org/pdf/2609.21216
- **详细分析**: [[20_Research/Papers/具身智能/Fewer_Steps,_Better_Actions_Rethinking_Flow-Matching_Inference_for_VLA_Policies|Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies]]
- **作者**: Zhipeng Tang, Xinda Chen, Weining Rao, Xiao Li, Wenting Tan, Yuning Wang, Xiao Shi, Xiaofang Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Fewer Steps, Better Actions: Rethinking Flow-Matching Inference for VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, ResVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies based on flow matching generate action chunks through repeated evaluations of an action expert. Increasing the number of integration steps raises inference cost, but does not necessarily improve closed-loop success. We propose Coda, which reallocates part of this integration budget to a single learned endpoint correction. A frozen policy first completes a few-step noise-to-action trajectory; a lightweight Transformer then predicts a demonstration-supervised residual using the candidate action, source noise, and shared observation-prefix cache. Only the corrector is trained. On 50 RoboTwin Easy tasks, five-step Coda improves success from 71.64% to 74.68% over the matched five-step baseline, while reducing forward latency by 30.2% relative to the default ten-step policy. A two-step configuration achieves 71.88% success with a 2.12$\times$ speedup. An independent 13-task control shows a 5.69-percentage-point gain at nearly equal latency, supporting correction as an effective alternative to additional integration. The same design also improves frozen official SmolVLA, raising two-step success from 60.8% to 69.4%. These results show that endpoint correction improves the quality-latency trade-off of frozen flow-matching policies.

</details>

---

### [[20_Research/Papers/机器人/PlantShade_Predicting_Plant_Shadows_for_Lighting-Aware_Robotic_Agricultural_Operation|PlantShade: Predicting Plant Shadows for Lighting-Aware Robotic Agricultural Operation]]

![[assets/2609.21059_figure.png|800]]

- **arXiv**: [2609.21059](https://arxiv.org/abs/2609.21059)
- **PDF**: https://arxiv.org/pdf/2609.21059
- **详细分析**: [[20_Research/Papers/机器人/PlantShade_Predicting_Plant_Shadows_for_Lighting-Aware_Robotic_Agricultural_Operation|PlantShade: Predicting Plant Shadows for Lighting-Aware Robotic Agricultural Operation]]
- **作者**: Longchao Da, Xiaoou Liu, Xingjian Li, Lirong Xiang, Hua Wei
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《PlantShade: Predicting Plant Shadows for Lighting-Aware Robotic Agricultural Operation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Plant growth and agricultural production form the foundation of a country's sustainable development and directly impact human livelihoods. Recent advances in frontier artificial intelligence have enabled scientific agriculture with strong potential to improve crop productivity. In this paper, we identify the importance and inherent complexity of plant shade simulation, as shading is a critical factor influencing plant growth. To advance this field and promote broader societal benefits, we focus on two main contributions. First, we introduce a comprehensive plant growth and shade dataset covering four plant species, including soybean, tomato, sugarbeet, and strawberry. The dataset includes top-down viewpoints with a supplementary light along a circular trajectory, casting dynamic shadows across multiple growth stages and diverse observation complexities. Second, we propose generative shade simulation based on diffusion models, enabling realistic shade generation for unseen plants and supporting downstream robotic tasks such as perception, lighting control, and view planning. The model incorporates temporal conditioning to facilitate flexible shade simulation across different time stages. We conduct both quantitative and qualitative evaluations to assess model performance. This work provides a foundational study for plant-aware shade modeling and has meaningful implications for broader agricultural and robotic applications.

</details>

---

### [[20_Research/Papers/强化学习/BI-Agent_and_BI-Bench_Towards_Automating_End-to-End_Business_Intelligence|BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence]]

![[assets/2609.20886_figure.png|800]]

- **arXiv**: [2609.20886](https://arxiv.org/abs/2609.20886)
- **PDF**: https://arxiv.org/pdf/2609.20886
- **详细分析**: [[20_Research/Papers/强化学习/BI-Agent_and_BI-Bench_Towards_Automating_End-to-End_Business_Intelligence|BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence]]
- **作者**: Chuxuan Hu, Yeye He, Penny Zhou, Wee Hyong Tok, Daniel Kang, Surajit Chaudhuri
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《BI-Agent and BI-Bench: Towards Automating End-to-End Business Intelligence》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BI-Bench, DSBench, InfiAgent-DABench, KramaBench, REPRO-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Business intelligence (BI) is a cornerstone of enterprise decision-making and is widely used by enterprise users in software such as Power BI and Tableau. In traditional BI workflows, users need to prepare data by (1) identifying relevant tables, (2) performing data transformations, and (3) building join relationships, before they can (4) answer their business questions. These steps can be complex and time-consuming, making BI challenging. Given the strong capabilities of large language models (LLMs) in working with data, we study their ability to answer BI questions end-to-end, without requiring users to manually perform the tedious preparation steps. To do this, we harvest a large collection of real-world BI projects from public sources, and manually extract pairs of (questions, ground-truth answers) from real user dashboards. The resulting benchmark, BI-Bench, is the first benchmark to systematically study LLMs' ability on end-to-end BI. We find that even frontier LLMs perform poorly on BI-Bench, with less than 50% accuracy. To address their limitations, we design a tool-augmented BI-Agent that decomposes BI workflows into subtasks on structured data, such as search, join, and transform, and orchestrates specialized data management methods across BI stages. Furthermore, we develop a post-training framework that synthesizes training trajectories from real BI projects, enabling BI-Agent to be further post-trained using both supervised fine-tuning (SFT) and reinforcement learning (RL). BI-Agent achieves substantial accuracy gains of up to 40 percentage points with vanilla LLMs, and post-trained BI-Agent yields gains of up to 30 points. Our results highlight the importance of combining tool-augmented reasoning with domain-specific post-training in complex BI workflows, and point to promising directions for future research.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_learning_for_post-coronagraphic_wavefront_control|Reinforcement learning for post-coronagraphic wavefront control]]

![[assets/2609.20880_first_page.png|800]]

- **arXiv**: [2609.20880](https://arxiv.org/abs/2609.20880)
- **PDF**: https://arxiv.org/pdf/2609.20880
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_learning_for_post-coronagraphic_wavefront_control|Reinforcement learning for post-coronagraphic wavefront control]]
- **作者**: Manuela Castañeda-Medina, Yann Gutierrez, Johan Mazoyer, Baptiste Abeloos, Laurent Mugnier, Olivier Herscovici-Schiller
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Reinforcement learning for post-coronagraphic wavefront control》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Direct imaging of exoplanets is limited by the extreme contrast between the star and the planets, which is mitigated using a coronagraph. However, optical aberrations cause starlight leakage through the coronagraph, producing speckles that obscure the planetary signal. Achieving the required contrast levels demands wavefront control with subnanometric precision. Deep reinforcement learning offers a promising alternative to traditional focal-plane wavefront control techniques by enabling adaptive correction strategies learned directly from interaction with the system. In this work, we present a fully data-driven method for post-coronagraphic aberration correction in a simulated high-contrast imaging testbed. The agent controls a deformable mirror using observations consisting of focal-plane measurements (images) and physics-informed wavefront sensing information derived from these images. We evaluate different observation representations and control strategies, and the method is validated on simplified simulations of a high-contrast imaging testbed, where it successfully creates dark holes, i.e., regions of the focal plane in which residual starlight is strongly suppressed, while approaching the performance of conventional wavefront control methods.

</details>

---
