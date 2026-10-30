# cs.AI | Artificial Intelligence | 2026-10-28

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/具身智能/ThinkWorld_World_Imagination_Reinforces_Chain-of-Dynamics_Reasoning|ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning]]

![[assets/2610.37666_figure.png|800]]

- **arXiv**: [2610.37666](https://arxiv.org/abs/2610.37666)
- **PDF**: https://arxiv.org/pdf/2610.37666
- **详细分析**: [[20_Research/Papers/具身智能/ThinkWorld_World_Imagination_Reinforces_Chain-of-Dynamics_Reasoning|ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning]]
- **作者**: Chaehyun Kim, Chi-Pin Huang, Jisoo Kim, Min-Hung Chen, Yu-Chiang Frank Wang, Seungryong Kim, Fu-En Yang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.1（加权：具身智能 1.2，强化学习 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ThinkWorld: World Imagination Reinforces Chain-of-Dynamics Reasoning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ACoT-VLA, Real-World, ThinkWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have made substantial progress in robotic manipulation, but their generalization remains constrained by the diversity and coverage of action-labeled robot demonstrations. Human videos provide much broader behavioral and environmental experience, while learning from them faces a fundamental trade-off between scalable data and explicit action grounding. We introduce ThinkWorld, a VLA learning framework that grounds action reasoning in world dynamics and strengthens it through reinforcement learning with world imagination. ThinkWorld represents each action thought as a Chain-of-Dynamics (CoD), a sequence of discrete motion tokens that captures the intermediate dynamics connecting the current world to a future state and serves as a common action representation across embodiments. We first initialize CoD with action-labeled demonstrations, then predict the future induced by each CoD and reinforce those whose predictions better match the observed outcome. This enables videos without action annotations to provide direct supervision from observed state transitions, allowing human and robot experience to refine the same reasoning space. Experiments in simulation and on real robots demonstrate effective human-to-robot transfer and strong generalization to unseen tasks and environments.

</details>

---

### [[20_Research/Papers/世界模型/Understanding_the_limits_of_latent_world_models|Understanding the limits of latent world models]]

![[assets/2610.37588_figure.png|800]]

- **arXiv**: [2610.37588](https://arxiv.org/abs/2610.37588)
- **PDF**: https://arxiv.org/pdf/2610.37588
- **详细分析**: [[20_Research/Papers/世界模型/Understanding_the_limits_of_latent_world_models|Understanding the limits of latent world models]]
- **作者**: Rodrigo Gonzalez Laiz, Steffen Schneider
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Understanding the limits of latent world models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are widely proposed as core components for enabling agents to reason over long temporal and spatial horizons. Yet current evaluations often emphasize task performance while providing limited insight into whether learned world models acquire predictive latent dynamics that reflect the underlying structure of the environment. Here we introduce the concept of faithful latent world models as an equivariance condition between the environment's transition map and the learned latent dynamics. We propose latent rollout consistency (LRC) as a metric to evaluate action-conditioned latent prediction. Strikingly, we find that across the studied state of the art latent world models, none solves the task by actually faithfully modeling the dynamics of the environment.

</details>

---

### [[20_Research/Papers/强化学习/When,_Where,_and_What_to_Correct_Human-Guided_Adaptive_Residual_Correction_for_Robot_Policies|When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies]]

![[assets/2610.37547_figure.png|800]]

- **arXiv**: [2610.37547](https://arxiv.org/abs/2610.37547)
- **PDF**: https://arxiv.org/pdf/2610.37547
- **详细分析**: [[20_Research/Papers/强化学习/When,_Where,_and_What_to_Correct_Human-Guided_Adaptive_Residual_Correction_for_Robot_Policies|When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies]]
- **作者**: Anukriti Singh, Maxime Caniot, Pratap Tokekar, Firas Abi-Farraj
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《When, Where, and What to Correct: Human-Guided Adaptive Residual Correction for Robot Policies》归入 机器人、具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HIL-SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation policies that reliably execute most of a manipulation trajectory can still fail in localized regions requiring last-mile precision. Updating the full policy or exploring residual actions everywhere treats this local failure as a global learning problem. We introduce Adaptive Residual Correction (ARC), a lightweight post-training module that uses reinforcement learning (RL) to learn a residual correction on top of a frozen policy while using sparse human corrections to structure autonomous exploration. Rather than treating human corrections as imitation targets, ARC uses pre-intervention states to determine 'when' residual control should become active and correction geometry to determine 'where' in residual action space autonomous refinement should explore; task reward determines 'what' residual is ultimately executed. Across three precision-manipulation tasks on a real robot, ARC improves average task success from 33.3% to 75.0%. The human corrections define task-dependent 2-3 dimensional subspaces of the seven-joint residual space that retain 96.0-97.7% of squared correction magnitude. Together, these results show that sparse human corrections can localize and constrain autonomous post-training without requiring the observed correction itself to serve as the final action target.

</details>

---

### [[20_Research/Papers/具身智能/Which_Hand_Was_Late_Diagnosis_for_Robot_Failure_Recovery_in_Bimanual_Tool_Use|Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use]]

![[assets/2610.37533_figure.png|800]]

- **arXiv**: [2610.37533](https://arxiv.org/abs/2610.37533)
- **PDF**: https://arxiv.org/pdf/2610.37533
- **详细分析**: [[20_Research/Papers/具身智能/Which_Hand_Was_Late_Diagnosis_for_Robot_Failure_Recovery_in_Bimanual_Tool_Use|Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use]]
- **作者**: Baptiste Bonin, Caro Strickland, Audrey Durand
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Which Hand Was Late? Diagnosis for Robot Failure Recovery in Bimanual Tool Use》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Failure diagnosers for robot manipulation are increasingly vision--language models (VLMs), trained and evaluated on single-arm failures produced by perturbing a successful demonstration. Bimanual tool use adds failures of other kinds: a tool that slips out of its socket while still held, two correct gestures made at different times, and attempts that fail for two reasons at once. On a simulated bimanual tool-use task whose failure causes are read from the recorded trace, we measure what each sensing channel lets a diagnoser tell. The tool's slip is read on the tool hand; which hand was late is read on both arms, while a sensor on one hand reads its own hand's delay and at most part of the other's; and whether a late attempt was also pushed too weakly is not identifiable from passive sensing when the tool hand is late. Within two attempts, a repair policy that escalates when the cause is not identifiable repairs as many failures as one told the true cause. A VLM's internal state carries the late hand almost perfectly, along a direction no closer to the one its answer reads than a random one; whether the answer reports it depends on the wording of the question.

</details>

---

### [[20_Research/Papers/强化学习/Strategyproof_Deep_Reinforcement_Learning_for_Online_Resource_Allocation|Strategyproof Deep Reinforcement Learning for Online Resource Allocation]]

![[assets/2610.37504_first_page.png|800]]

- **arXiv**: [2610.37504](https://arxiv.org/abs/2610.37504)
- **PDF**: https://arxiv.org/pdf/2610.37504
- **详细分析**: [[20_Research/Papers/强化学习/Strategyproof_Deep_Reinforcement_Learning_for_Online_Resource_Allocation|Strategyproof Deep Reinforcement Learning for Online Resource Allocation]]
- **作者**: Fariba Dehghan, Sebastian Stein, Vahid Yazdanpanah, Stephanie Gauthier
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.1，强化学习 1.4）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Strategyproof Deep Reinforcement Learning for Online Resource Allocation》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online resource allocation faces two coupled challenges: (1) allocating scarce resources efficiently under uncertain future demand, and (2) ensuring that agents report task valuations and requirements truthfully (strategyproofness). Reinforcement Learning (RL) adapts allocation decisions through experience but does not necessarily ensure strategyproofness. Existing strategyproof RL uses a linear allocation rule, which limits the resource interactions it can represent. Neural mechanism design methods offer greater expressiveness, but provide only approximate incentive guarantees. Against this background, we introduce the first strategyproof deep RL mechanism for online resource allocation. It integrates three novel components: (i) a monotonic neural network that learns nonlinear interactions by construction (higher reported value cannot reduce acceptance, while a longer reported duration or larger resource requirement cannot increase it); (ii) a generalised critical payment: the lowest accepted value, with all other inputs fixed; and (iii) training by either RL or imitation of an existing rule. Together, monotonicity and the critical payment ensure strategyproofness and individual rationality, while the neural rule provides flexibility and imitation improves training efficiency. Empirically, on a four-resource stream with two partner pairs that a linear difference cannot represent, the neural rule achieves 97.8% of an offline welfare upper bound, compared with 93.8% for a linear learner and 89.0% for first-come, first-served, closing 65% and 80% of the remaining optimality gap, respectively. Moreover, imitation reaches 97.5% in only 261 seconds, about 89 times faster than RL.

</details>

---

### [[20_Research/Papers/强化学习/Autonomous_fixed-wing_interception_using_reinforcement_learning|Autonomous fixed-wing interception using reinforcement learning]]

![[assets/2610.37470_figure.jpeg|800]]

- **arXiv**: [2610.37470](https://arxiv.org/abs/2610.37470)
- **PDF**: https://arxiv.org/pdf/2610.37470
- **详细分析**: [[20_Research/Papers/强化学习/Autonomous_fixed-wing_interception_using_reinforcement_learning|Autonomous fixed-wing interception using reinforcement learning]]
- **作者**: Daan van Hamersveld, Ewoud Smeur, Iurii Kriachko
- **cs 子类**: cs.AI, cs.NE, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Autonomous fixed-wing interception using reinforcement learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medium altitude, long endurance unmanned aerial systems such as Shahed-type strike drones are an unanswered threat in modern conflicts. Conventional air defense systems are too expensive to provide a feasible large-scale solution. Quadcopter interceptors are a cheap, battle-proven alternative, but their extremely limited flight time restricts them to low altitude targets at short range, whereas fixed-wing platforms have the endurance to reach higher altitude targets from longer distances. However, such interceptors are still operated manually. Recent developments in learning-based controllers show potential for automation. In this work, a fixed-wing interceptor is presented that is controlled by a neural network that maps filtered monocular vision observations directly to actuator commands. The policy was trained in a custom Python environment using reinforcement learning and proximal policy optimization. The policy was then deployed on a fixed-wing platform and tested in real interception scenarios. As a baseline, two classical guidance controllers were also developed and tested in simulation. The policy is able to intercept targets both in simulation and in real flight. In simulation, the policy outperforms the classical controllers under most conditions. The interceptor was ultimately successfully validated in real flight by intercepting maneuvering fixed-wing targets. This novel system shows the potential of artificial intelligence for autonomous control of fixed-wing interceptor drones.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Quality-Controllable_Robot_Policies_with_Iterative_Hindsight_Relabeling|Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling]]

![[assets/2610.37393_figure.png|800]]

- **arXiv**: [2610.37393](https://arxiv.org/abs/2610.37393)
- **PDF**: https://arxiv.org/pdf/2610.37393
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Quality-Controllable_Robot_Policies_with_Iterative_Hindsight_Relabeling|Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling]]
- **作者**: Sinjae Kang, Dong Kyu Shin, Jaehong Kim, Kamin Lee, Hyoeun Kim, Kaixin Wang, Li Zhao, Seonghyeon Ye, Kimin Lee
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Quality-Controllable Robot Policies with Iterative Hindsight Relabeling》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSRL, RoboEval, SORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policy evaluation often relies on a binary success signal for task completion. In real-world deployment, however, desired execution behaviors are also defined by quality attributes such as execution speed and motion smoothness, which need to be dynamically controlled according to task requirements. To address this, we introduce Quality-Controllable Policy (QCP), a robot policy that enables inference-time control over both individual quality attributes and their combinations. To extend the controllable quality range beyond initial demonstrations, we further propose an iterative hindsight relabeling loop: QCP collects online rollouts under target quality labels, adds successful trajectories to the dataset, relabels the accumulated trajectories in hindsight according to their measured quality, and fine-tunes the policy. Experiments on Robomimic and RoboEval demonstrate that QCP consistently improves both task execution quality and success rates across iterations, producing successful rollouts that exceed the quality of the initial demonstrations. Finally, we validate QCP on real-world manipulation tasks, where controlling speed increases throughput in conveyor operations and controlling transport stability improves success when carrying wine glasses, demonstrating that quality-controllable policies yield practical gains in physical deployment.

</details>

---

### [[20_Research/Papers/大模型/AnalogScout_Simulation-Efficient_PVT-Aware_Analog_Sizing_with_LLM_Agents|AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents]]

![[assets/2610.37319_figure.png|800]]

- **arXiv**: [2610.37319](https://arxiv.org/abs/2610.37319)
- **PDF**: https://arxiv.org/pdf/2610.37319
- **详细分析**: [[20_Research/Papers/大模型/AnalogScout_Simulation-Efficient_PVT-Aware_Analog_Sizing_with_LLM_Agents|AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents]]
- **作者**: Yichen Long, Keren Zhu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AnalogScout: Simulation-Efficient PVT-Aware Analog Sizing with LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Analog device sizing must satisfy all specifications across process, voltage, and temperature (PVT) corners to ensure tape-out success, but simulating every candidate at all corners dominates the sizing time and slows design iteration. Conventional surrogate-based optimizers search the sizing space directly, while recent large language model (LLM) agents add circuit knowledge to designs but still delegate the sizes to global optimizers. Both learn the circuit response from repeated multi-corner SPICE simulations and optimize on top of it, which becomes expensive under a limited simulation budget. Providing an agent with reusable verified designs and sizing sub-blocks analytically could save most of this budget. We propose AnalogScout, a simulation-efficient PVT-aware sizing framework driven by an LLM agent. Combining elite-design reuse, analytic gm/Id local sizing and global refinement under full-corner verification, AnalogScout reduces power by 43.3% relative to the evolution strategy CMA-ES at an equal budget of 16k simulations on three SKY130 OTAs of increasing complexity, and reaches the final CMA-ES power after 7.0% of that budget. It also attains lower power than Bayesian optimization on all three OTAs and than two re-implemented LLM-driven flows on the two OTAs where they were tested.

</details>

---

### [[20_Research/Papers/大模型/Where_Should_the_Evaluation_Budget_Go_in_LLM-Driven_Agent_Scaffold_Evolution|Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?]]

![[assets/2610.37276_figure.png|800]]

- **arXiv**: [2610.37276](https://arxiv.org/abs/2610.37276)
- **PDF**: https://arxiv.org/pdf/2610.37276
- **详细分析**: [[20_Research/Papers/大模型/Where_Should_the_Evaluation_Budget_Go_in_LLM-Driven_Agent_Scaffold_Evolution|Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?]]
- **作者**: Sichun Luo, Yi Huang, Mukai Li, Haochen Luo, Guanzhi Deng, Haibo Wang, Jian Xu, Zefa Hu, Junlan Feng, Qi Liu
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Where Should the Evaluation Budget Go in LLM-Driven Agent Scaffold Evolution?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CollabEval, HotpotQA, IFBench, SparseEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-driven agent scaffold evolution improves agent workflows through iterative candidate generation and evaluation. Evaluation both guides subsequent search and determines the final scaffold, but evaluating every candidate on the full task set incurs substantial execution costs. We investigate how evaluation budgets can be allocated across these two roles. Our experiments show that sparse feedback can sustain productive evolution, while additional targeted evaluation improves final selection. Replay analyses further show that shared informative items and a common scoring reference support comparisons among closely matched candidates. Motivated by these findings, we propose \method, an evaluation allocation framework that combines sparse search-time feedback with targeted final confirmation. A short fully evaluated warm-up establishes a shared informative core and calibrates a response model whose item parameters remain fixed during search. After search, \method refits the model and applies paired successive halving, reusing accumulated observations and executing only missing evaluations. Across four benchmarks and two evolution frameworks, \method achieves higher mean performance than full evaluation in most settings while using approximately half as many evaluation cells.

</details>

---

### [[20_Research/Papers/大模型/Grounding_LLM_Agents_in_Business_Processes_Process-Aware_Knowledge_Graphs_for_Reliable_Multi-Step_Service_Invocation|Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation]]

![[assets/2610.37242_first_page.png|800]]

- **arXiv**: [2610.37242](https://arxiv.org/abs/2610.37242)
- **PDF**: https://arxiv.org/pdf/2610.37242
- **详细分析**: [[20_Research/Papers/大模型/Grounding_LLM_Agents_in_Business_Processes_Process-Aware_Knowledge_Graphs_for_Reliable_Multi-Step_Service_Invocation|Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation]]
- **作者**: Saiful Khan, Afrah Farea
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Grounding LLM Agents in Business Processes: Process-Aware Knowledge Graphs for Reliable Multi-Step Service Invocation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EntitySet, SOCBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents that call enterprise APIs must select the correct endpoints, follow process order, use valid payload keys, and choose coded values from predefined lists. However, current retrieval-augmented service discovery treats endpoints independently and therefore misses process and schema constraints. We address this limitation by integrating Open Data Protocol (OData) metadata and Business Process Model and Notation (BPMN) reference processes in a typed property graph. A hybrid retriever identifies candidate endpoints using dense embeddings and follows process edges to retrieve subsequent endpoints. We evaluate the method on 42 enterprise services with process-chain ground truth. For queries with low lexical overlap between the query and downstream entities, it improves Recall@3 by 5.7 points (n=74), with consistent gains across embedding models and cut-offs. It matches dense retrieval on other queries and provides no improvement on OpenAPI services without a process layer, indicating that the gains arise from process structure. We also evaluate an LLM agent on 81 multi-step queries. It completes 38.7% of tasks, compared with 10.3% for a chunk-based baseline. In an elicitation probe, providing valid code lists eliminates invented codes but leaves invalid keys in 46% of write runs. Full typed context reduces invalid calls to 3% (3 of 101 runs), with no invented codes. These results show that exposing process and schema constraints during retrieval improves the reliability of agent-driven API calls.

</details>

---

### [[20_Research/Papers/具身智能/Retrieve_to_Act_Motion_Primitive_Graph_Retrieval_for_Robust_VLA_Execution|Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution]]

![[assets/2610.37215_figure.png|800]]

- **arXiv**: [2610.37215](https://arxiv.org/abs/2610.37215)
- **PDF**: https://arxiv.org/pdf/2610.37215
- **详细分析**: [[20_Research/Papers/具身智能/Retrieve_to_Act_Motion_Primitive_Graph_Retrieval_for_Robust_VLA_Execution|Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution]]
- **作者**: Pham Tri Quang, Bao-Ngoc Dao, Minh Duc Nguyen, Duc-Duy Nguyen, Hung T. Ho, Linh Dang Le, Trong-Bao Ho, Thien-Loc Ha, Tan Q. Nguyen, Tuan Dam, Vu N. Duong, Daniel Sonntag...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Retrieve to Act: Motion Primitive Graph Retrieval for Robust VLA Execution》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BYOVLA, Real-World, StableVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies demonstrate remarkable semantic generalization, yet remain highly vulnerable to out-of-distribution (OOD) visual shifts during execution. While existing test-time methods attempt to suppress spurious visual cues, they fundamentally overlook the rich, uncorrupted kinematic priors embedded in the policy's own training experience. We introduce Retrieve to Act (R2A), a test-time scaling framework that formulates OOD robustness purely as a geometric motion primitive retrieval problem. R2A bypasses fragile visual features by structuring successful training demonstrations into an offline spatiotemporal motion primitive graph. During inference, a query-dependent Graph Neural Network dynamically localizes the robot's ongoing execution within this graph, retrieving structurally compatible future motion primitives. These retrieved geometric priors are then seamlessly harmonized with the frozen VLA's predicted actions via a learned, dimension-wise gating mechanism, adaptively rectifying erroneous spatial trajectories while preserving the policy's local reactivity. Extensive experiments across three state-of-the-art VLA architectures, GR00T N1.7, $π_{0.5}$, and StableVLA, demonstrate that R2A consistently and significantly enhances robustness against diverse contextual perturbations. R2A achieves absolute success rate improvements of up to +12% in simulation benchmarks (LIBERO-Plus, RoboTwin2.0-Plus) and +40% in real-world deployments, without requiring any finetuning of the base policies. Project page: https://retrieve2act.github.io/r2a/

</details>

---

### [[20_Research/Papers/强化学习/Action-Value_Calibration_via_Continuation_Sharing_for_Long-Horizon_Agentic_Reinforcement_Learning|Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning]]

![[assets/2610.37195_figure.png|800]]

- **arXiv**: [2610.37195](https://arxiv.org/abs/2610.37195)
- **PDF**: https://arxiv.org/pdf/2610.37195
- **详细分析**: [[20_Research/Papers/强化学习/Action-Value_Calibration_via_Continuation_Sharing_for_Long-Horizon_Agentic_Reinforcement_Learning|Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning]]
- **作者**: Yingjian Chen, Lang Zhou, Zixin Zhao, Pingfan Li, Weishi Zheng, Zhilin Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Action-Value Calibration via Continuation Sharing for Long-Horizon Agentic Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning for long-horizon agents relies on feedback from sequences of interactions, making credit assignment to individual actions difficult. Existing methods such as GiGPO compare actions at shared states to compute relative advantages, but estimate each action's value from a single sampled continuation. The resulting local credit remains sensitive to decisions made later in the trajectory. To address this problem, we propose ConCal (Continuation Calibration), a recursive continuation-value estimator that incorporates continuation evidence already present in a rollout batch. ConCal matches visits from the same task by their incoming state-action-state transitions, combines shared continuation evidence with each visit's own transition estimate, and propagates calibrated values backward to refine earlier action-value estimates. This reduces dependence on individual sampled continuations and mitigates local credit distortions without additional rollouts. Held-out return diagnostics show lower error in within-group value differences and higher agreement with reference action orderings than estimates based on individual continuations. With Qwen2.5-1.5B-Instruct, ConCal improves success rates over GiGPO by 3.39 and 5.86 percentage points on ALFWorld and WebShop, respectively. Our code is available at https://github.com/Yingjian-Chen/ConCal.

</details>

---

### [[20_Research/Papers/世界模型/MLE-World_Predicting_Machine_Learning_Experiment_Outcomes_with_a_Learned_World_Model|MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model]]

![[assets/2610.37175_first_page.png|800]]

- **arXiv**: [2610.37175](https://arxiv.org/abs/2610.37175)
- **PDF**: https://arxiv.org/pdf/2610.37175
- **详细分析**: [[20_Research/Papers/世界模型/MLE-World_Predicting_Machine_Learning_Experiment_Outcomes_with_a_Learned_World_Model|MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model]]
- **作者**: Brian Ko, Han Wang, Hejia Geng, Li Erran Li, Sherry Yang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《MLE-World: Predicting Machine Learning Experiment Outcomes with a Learned World Model》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DSWorld, MLE-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI research agents can propose, execute, and improve programs that solve machine learning tasks. However, executing each candidate program requires training and evaluating ML models, limiting how many candidates an agent can explore at each step. We introduce MLE-World, a world model finetuned from Qwen3.5-4B that predicts a program's terminal output (error traces, training logs, and validation scores) from its code and data description without executing it, together with a confidence score estimating the prediction's correctness. Because a prediction costs one inference call rather than a training run, MLE-World makes test time scaling (TTS) affordable for these agents. We build five TTS policies, guided by MLE-World, that compare several candidates per step by their predicted outputs: Sequential revision, Best-of-N, Pairwise judging, Fusion, and a UCB style rule that also adds an exploration bonus from this confidence score. Since predictions can be wrong, we run a candidate for real only when its confidence score is low. On 17 MLE-bench Lite tasks, MLE-World matches the real terminal output on 77.9% of held out programs, versus 41.1% for much larger prompted models. MLE-World guided TTS achieves up to 22.1% higher observed mean performance than the agent without a world model, with less real execution. Project webpage: https://mle-world.github.io/.

</details>

---

### [[20_Research/Papers/大模型/Blindfold_Keeping_the_Audit_Coin_Secret_from_LLM_Agents|Blindfold: Keeping the Audit Coin Secret from LLM Agents]]

![[assets/2610.37055_first_page.png|800]]

- **arXiv**: [2610.37055](https://arxiv.org/abs/2610.37055)
- **PDF**: https://arxiv.org/pdf/2610.37055
- **详细分析**: [[20_Research/Papers/大模型/Blindfold_Keeping_the_Audit_Coin_Secret_from_LLM_Agents|Blindfold: Keeping the Audit Coin Secret from LLM Agents]]
- **作者**: Wei Zhu, Meiyun Zuo, Huiping Sun
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Blindfold: Keeping the Audit Coin Secret from LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Audit-based certification bounds the violation rate of an LLM agent by auditing a random fraction $\varepsilon$ of actions and reweighting the audited labels; its validity is meant to rest only on the defender's audit coin. We show that it also rests on a confidentiality property: the coin must not interfere with the agent's view before the action commits, at a time the agent chooses. We call this pre-commit noninterference (PNI) and measure its violation by $D_{\mathrm{A}}$, the total-variation distance between the agent's views under the two coin values. PNI is necessary and sufficient for an unbiased certificate against adaptive agents, the worst-case bias is $(1-\varepsilon)D_{\mathrm{A}}$, and no procedure that sees only audited labels can pay less. Leakage composes across steps, a resource shared across episodes opens a channel of computable size, and raising the audit rate cannot restore validity. On a monitor we built, a silent audit changes no output but adds latency that tool timestamps expose, and the agent can enlarge it. A real LLM agent follows an injection that names a visible audit notice (generic, tool, and timing clauses have no effect); over that channel the plain certificate fails on measured labels and, by a post-hoc analysis, in a live run on a pre-registered schedule, while a silent audit restores it. A fresh coin per audited call closes the timing channel; padding only narrows it.

</details>

---

### [[20_Research/Papers/大模型/Guided-RLVR_Guided_Exploration_in_Reinforcement_Learning_with_Verifiable_Rewards|Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards]]

![[assets/2610.37041_figure.png|800]]

- **arXiv**: [2610.37041](https://arxiv.org/abs/2610.37041)
- **PDF**: https://arxiv.org/pdf/2610.37041
- **详细分析**: [[20_Research/Papers/大模型/Guided-RLVR_Guided_Exploration_in_Reinforcement_Learning_with_Verifiable_Rewards|Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards]]
- **作者**: Bo Yang, Zishuai Zhang, Weihua Li, Qinnan Zhang, Sijia Wen, Hainan Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Guided-RLVR: Guided Exploration in Reinforcement Learning with Verifiable Rewards》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has shown strong empirical gains in improving the reasoning ability of large language models (LLMs) on tasks such as mathematics and programming. However, recent studies have shown that RLVR rollouts often collapse onto a narrow set of reasoning trajectories, limiting the explored reasoning space. Motivated by findings that thinking tokens at critical steps serve as critical structural elements in LLM reasoning pathways, we propose Guided-RLVR, a novel approach that augments RLVR with a lightweight controller. The controller strategically injects semantically meaningful steering tokens into the sampling distribution, encouraging the model to approach problems from multiple reasoning perspectives and thereby expanding the exploration space. Experiments on mathematical reasoning and code generation benchmarks show that Guided-RLVR consistently outperforms existing RLVR methods while producing more diverse reasoning trajectories.

</details>

---

### [[20_Research/Papers/具身智能/Zooming_without_Zooming_v2_From_Seeing_Details_to_Connecting_Evidence_for_Generalizable_Multimodal_Perception|Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception]]

![[assets/2610.37037_figure.png|800]]

- **arXiv**: [2610.37037](https://arxiv.org/abs/2610.37037)
- **PDF**: https://arxiv.org/pdf/2610.37037
- **详细分析**: [[20_Research/Papers/具身智能/Zooming_without_Zooming_v2_From_Seeing_Details_to_Connecting_Evidence_for_Generalizable_Multimodal_Perception|Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception]]
- **作者**: Lai Wei, Yatai Li, Liangbo He, Jun Lan, Renjie Gu, Linhan Cao, Junkai Lin, Huijia Zhu, Weiqiang Wang, Linghe Kong, Yue Wang, Zhuosheng Zhang...
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.35（加权：具身智能 0.6，大模型 0.75）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Zooming without Zooming v2: From Seeing Details to Connecting Evidence for Generalizable Multimodal Perception》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MileBench, ReasonVQA, ViewSpatial-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal perception forms the foundation of multimodal intelligence. In particular, spatial perception and multimodal long-context understanding are two pivotal tasks that underpin embodied AI and multimodal agents. However, synthesizing targeted, high-quality training data for these tasks remains difficult and costly. Our key insight is that these tasks share an underlying capability, which we call connecting evidence: identifying relevant visual facts, binding them to the correct entities, recovering their relations, and composing them into an answer. Crucially, targeted training data are far easier to synthesize for this capability than for these tasks themselves. To strengthen this capability, we propose EvidenceConnect, an easy-to-implement data synthesis framework that uses zoomed views of related regions within a single image to generate questions requiring comparison, aggregation, or chaining of visual evidence. To ensure quality, a reference answer is retained only when independent VLMs agree on it, and region-ablation tests discard questions whose answer survives the removal of selected regions. We then train base VLMs on the resulting data with RLVR, obtaining Zooming without Zooming v2 (ZwZ2). Although the synthesized data are not tailored to any downstream benchmark, ZwZ2 improves fine-grained and spatial perception, with further gains on embodied spatial reasoning, multimodal long-context understanding, multimodal agent tasks, and general visual reasoning. These results establish EvidenceConnect as an effective framework for supervising evidence connection and suggest that strengthening this shared capability leads to more generalizable multimodal perception.

</details>

---

### [[20_Research/Papers/大模型/AutoVend_Benchmarking_LLM_Agents_on_Long-Horizon_Autonomous_Vending_Operations|AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations]]

![[assets/2610.36980_first_page.png|800]]

- **arXiv**: [2610.36980](https://arxiv.org/abs/2610.36980)
- **PDF**: https://arxiv.org/pdf/2610.36980
- **详细分析**: [[20_Research/Papers/大模型/AutoVend_Benchmarking_LLM_Agents_on_Long-Horizon_Autonomous_Vending_Operations|AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations]]
- **作者**: Qiming Shi, Yikun Li, Beidi Luan, Rui Sun, Yan Ma, Jing Li, Daxin Jiang, Zuo Bai
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AutoVend: Benchmarking LLM Agents on Long-Horizon Autonomous Vending Operations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are extending agent-mediated commerce on the Web from shopping for consumers to operating businesses for sellers. In online-to-offline (O2O) commerce, decisions are issued through Web-based platforms but realized through costly physical execution. Evaluating such agents requires going beyond individual transactions to ask whether decisions made online turn into sustained economic returns. We introduce AutoVend, a benchmark in which one LLM agent manages 20 vending machines across five site types through a Web-based operating interface for 180 simulated days. Its data-grounded simulator combines a shared warehouse, procurement lead times, paid replenishment, inventory expiration, and recurring operating costs. We evaluate five LLM agents against a rule-based inventory-control baseline and diagnose their site coordination, execution, and performance over time. Four of five evaluated LLM agents fall short of this baseline, and returns per dollar of inference cost rank models differently from returns alone. Operational analyses show that gains in individual metrics do not consistently yield stronger economic growth, as inventory and execution costs erode these gains. Trajectory analysis further reveals difficulties in grounding feasible actions, managing inventory commitments, and converting feedback into effective policy revisions.

</details>

---

### [[20_Research/Papers/强化学习/Vision-Language_Agents_Can_Learn_in_Their_Own_Latent_Worlds|Vision-Language Agents Can Learn in Their Own Latent Worlds]]

![[assets/2610.36925_figure.png|800]]

- **arXiv**: [2610.36925](https://arxiv.org/abs/2610.36925)
- **PDF**: https://arxiv.org/pdf/2610.36925
- **详细分析**: [[20_Research/Papers/强化学习/Vision-Language_Agents_Can_Learn_in_Their_Own_Latent_Worlds|Vision-Language Agents Can Learn in Their Own Latent Worlds]]
- **作者**: Haoxi Li, Sikai Bai, Jianfei Ma, Qinglin Hou, Xiaocheng Lu, Tao Han, Jie Zhang, Song Guo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.2，世界模型 0.6）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Vision-Language Agents Can Learn in Their Own Latent Worlds》归入 大模型、世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning from experience is essential for building the next generation of agents that continually expand their capabilities. Pretrained vision-language models (VLMs) already internalize rich world knowledge, yet this knowledge is rarely leveraged to drive policy improvement through online interaction. Realizing this potential efficiently remains challenging, as policy updates shift the agent's interaction distribution, requiring the world model to adapt accordingly, while continually updating large pretrained models is computationally expensive. To address this challenge, we introduce Dwell, a model-based reinforcement learning (RL) framework that reframes a VLM as a recurrent latent transition operator, endowing it with the ability to predict, adjust, and act in latent space. Leveraging the VLM's own representations and its dual role as both world model and policy, the agent continually learns from real interactions to anticipate and evaluate action outcomes, and from latent imagination to improve its behavior. Across five interactive visual environments, Dwell achieves the strongest overall performance among trainable methods while substantially reducing the compute required for imagination, showing that effective world models for VLM agents need not reconstruct the future; they need to predict futures that are useful for action. Our code is publicly available at https://github.com/Tom111-lhx/Dwell

</details>

---

### [[20_Research/Papers/强化学习/Noise_Steering_Exploiting_Wake_Steering_and_Acoustic_Directivity_for_Noise-Constrained_Wind_Farm_Control_via_Reinforcement_Learning|Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning]]

![[assets/2610.36888_figure.png|800]]

- **arXiv**: [2610.36888](https://arxiv.org/abs/2610.36888)
- **PDF**: https://arxiv.org/pdf/2610.36888
- **详细分析**: [[20_Research/Papers/强化学习/Noise_Steering_Exploiting_Wake_Steering_and_Acoustic_Directivity_for_Noise-Constrained_Wind_Farm_Control_via_Reinforcement_Learning|Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning]]
- **作者**: Martín de Frutos, Baptiste Corban, Claire Bizon Monroc, Ana Bušić, Donatien Dubuc, Jiamin Zhud, Esteban Ferrer
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Noise Steering: Exploiting Wake Steering and Acoustic Directivity for Noise-Constrained Wind Farm Control via Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：WFCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing noise mitigation strategies for wind farms usually consist in reducing turbines power output, without accounting for the wake interactions between them and the noise emission directivity. This leads to over-conservative policies and unexploited wind power. Yet, turbine yaw can simultaneously affect wake interactions and the direction of noise emission, offering an additional degree of freedom for farm-level noise control. We therefore propose Noise Steering, a model-free reinforcement learning (RL) strategy that jointly controls turbine yaw angles and power setpoints to maximise farm power while satisfying a local noise constraint in a defined region. To enable training at a reduced computational cost, a low-fidelity acoustic model is coupled with the steady-state FLORIS simulator. The RL agent effectively learns how to redirect wakes and noise directivity away from the protected region while redistributing power across the farm. On a six-turbine test farm, the policy satisfies the 40 dB noise constraint throughout the full range of turbulent winds, with an average power deficit of only 2% relative to greedy unimpeded control, and up to 7.7% at high wind speeds. In comparison, the industry-standard noise-reduced operation (NRO) baseline here generates an average power loss of 17%. When deployed in the higher-fidelity FAST.Farm simulator, the policy largely retains its performance under steady and turbulent inflow, despite differences in simulation fidelity. These results demonstrate the potential of combining yaw control and power derating through RL to improve the power-noise trade-off in wind farm operation.

</details>

---

### [[20_Research/Papers/大模型/GUI-JEPA_Candidate-Conditioned_JEPA_Latents_as_a_Fast_Action_Policy_for_Mobile_GUI_Agents|GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents]]

![[assets/2610.36877_figure.png|800]]

- **arXiv**: [2610.36877](https://arxiv.org/abs/2610.36877)
- **PDF**: https://arxiv.org/pdf/2610.36877
- **详细分析**: [[20_Research/Papers/大模型/GUI-JEPA_Candidate-Conditioned_JEPA_Latents_as_a_Fast_Action_Policy_for_Mobile_GUI_Agents|GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents]]
- **作者**: Bingchao Wang, Yongcheng Jing, Shunyu Liu, Chengyu Wang, Jun Huang, Jie Yang, Wei Liu, Dacheng Tao
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《GUI-JEPA: Candidate-Conditioned JEPA Latents as a Fast Action Policy for Mobile GUI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile GUI agents are typically fine-tuned 7B-scale vision-language models (VLMs) that generate each action as text. However, these VLMs decode every action token by token, and even agents that score candidate actions keep a large language model or VLM in the loop, making them slow and memory-hungry. To address these issues, we propose GUI-JEPA, to our knowledge the first decoder-free GUI agent policy built on a Joint-Embedding Predictive Architecture (JEPA), which selects actions in the latent space of a JEPA encoder pretrained on unlabelled GUI screenshots. Its action- and region-conditioned latent predictor turns the screen latent into one latent per candidate action, letting lightweight heads score all candidates against the instruction in a single batched pass, without decoding a token. We further show that the scorer relies on this latent pathway and that the predictor is trained for the decision itself: a randomly initialised predictor does just as well as one pretrained on screen dynamics. On AndroidControl, GUI-JEPA is 2.8-4.0x faster on the same GPU than a Qwen2.5-VL-7B agent we fine-tune with the same inputs, while reaching 86-92% of its in-distribution accuracy with 6% of its parameters. Code is available at https://github.com/bcwang-sjtu/GUI-JEPA

</details>

---

### [[20_Research/Papers/具身智能/ActiveAlign_Aligning_Egocentric_Manipulation_via_Active_Perception|ActiveAlign: Aligning Egocentric Manipulation via Active Perception]]

![[assets/2610.36859_figure.png|800]]

- **arXiv**: [2610.36859](https://arxiv.org/abs/2610.36859)
- **PDF**: https://arxiv.org/pdf/2610.36859
- **详细分析**: [[20_Research/Papers/具身智能/ActiveAlign_Aligning_Egocentric_Manipulation_via_Active_Perception|ActiveAlign: Aligning Egocentric Manipulation via Active Perception]]
- **作者**: Ri-Zhao Qiu, Bowen Wen, Yifeng Jiang, Chen Tessler, Eric Heiden, Xue Bin Peng, Xiaolong Wang, Stan Birchfield, Erwin Coumans
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《ActiveAlign: Aligning Egocentric Manipulation via Active Perception》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL, Real-to-Sim, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-to-Sim-to-Real (Real2Sim2Real) enables structured world representations for planning, interpretability, and safe execution. Most existing approaches rely on passive perception, which creates real2sim gaps due to imperfect observation. Inspired by how humans perceive actively through actions, we propose ActiveAlign, a framework that leverages active perception to align the Real2Sim2Real gap from interactions. ActiveAlign introduces two complementary modules: (i) ActiveAlign-Waving, which performs hand-eye calibration by exploiting active hand motions and differentiable rendering, and (ii) ActiveAlign-Touching, which refines object alignment through tactile feedback to achieve millimeter-level precision. Together, these capabilities enable strong real2sim alignment. We demonstrate that ActiveAlign-Waving can be used to curate simulation environments for open-sourced uncalibrated robot manipulation datasets, and demonstrate on a real Unitree G1 robot that ActiveAlign enables fine manipulation of millimeter-scale objects such as pressing buttons and moving sliders.

</details>

---

### [[20_Research/Papers/具身智能/Evolving_Agent_Teams|Evolving Agent Teams]]

![[assets/2610.36848_first_page.png|800]]

- **arXiv**: [2610.36848](https://arxiv.org/abs/2610.36848)
- **PDF**: https://arxiv.org/pdf/2610.36848
- **详细分析**: [[20_Research/Papers/具身智能/Evolving_Agent_Teams|Evolving Agent Teams]]
- **作者**: Shiyi Cao, Ziming Mao, Dacheng Li, Joseph E. Gonzalez, Ion Stoica
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.5，机器人 0.2）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Evolving Agent Teams》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FlashInfer-Bench, SWE-Gym, SkyRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid progress of software engineering agents drives interest in applying them to open-ended problems such as GPU kernel optimization. However, we find that existing coding agents converge to local optima on real-world, expert-written kernels (e.g., FlashInfer). We introduce Evolving Agent Teams, a multi-agent framework that escapes such local optima. It features (1) a central supervisor that diagnoses each local optimum and restructures a team of agents; and (2) a persistent file system that comprises a learning document, an evolution history, and per-team artifacts, grounding restructuring with accumulated experience. Under a matched token budget, Evolving Agent Teams consistently outperforms strong coding-agent baselines. With an extended token budget, Evolving Agent Teams generates a CUDA kernel that reaches 1.2x mean speedup over the production FlashInfer MLA paged decode kernel from scratch and wins on 36 of 47 production workloads from FlashInfer-Bench (0.86-0.99x on the remaining 11). It also demonstrates superior performance on tasks such as KDA prefill on AMD MI350X (3.01x over vLLM) and NVIDIA B200 (3.44x over FlashKDA), MoE expert-offload serving on Apple silicon (30.3 tokens/s decode for Qwen3.8-Flash-Next in MLX 4-bit on a 48 GB M4 Pro), and RoboDojo robot manipulation (62.1 on held-out seeds vs. 55.3 for the best leaderboard entry). Code is available at https://github.com/caoshiyi/EAT.

</details>

---

### [[20_Research/Papers/强化学习/TAPESTRY_A_Single_Backbone_for_Video_Generation_and_Robot_Control|TAPESTRY: A Single Backbone for Video Generation and Robot Control]]

![[assets/2610.36823_figure.png|800]]

- **arXiv**: [2610.36823](https://arxiv.org/abs/2610.36823)
- **PDF**: https://arxiv.org/pdf/2610.36823
- **详细分析**: [[20_Research/Papers/强化学习/TAPESTRY_A_Single_Backbone_for_Video_Generation_and_Robot_Control|TAPESTRY: A Single Backbone for Video Generation and Robot Control]]
- **作者**: Jeremy A. Collins, Seungjae Lee, Rachanon Wachakorn, Krishnan Srinivasan, Animesh Garg, Vitor Campagnolo Guizilini, Paarth Shah
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《TAPESTRY: A Single Backbone for Video Generation and Robot Control》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GigaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained video generation models encode rich priors about physical interactions, but leveraging them for robot control typically requires either resource-intensive video generation at test time or action heads trained from scratch that do not fully utilize the pretrained backbone. We introduce Tokenizing Actions as Video Patches in a Shared Transformer Policy (TAPESTRY), a world action model that repurposes a pretrained video diffusion transformer into a robotic policy without requiring video generation at inference. Our key idea is to treat robot actions as single-patch tokens in the video model's latent space. A lightweight linear projection maps each action timestep to the patch dimensions of the pretrained VAE, and the resulting tokens are processed by the same patchifying layers and transformer backbone used for video. The shared backbone is optimized through three diffusion objectives sampled per minibatch element: Video diffusion uses VAE latents from robot and human videos to establish dynamics priors. Joint video+action diffusion trains on robot demonstrations using a coupled diffusion timestep and an asymmetric attention mask. Action-only diffusion denoises actions conditioned on clean image latents. At test time, the model generates a compact action token sequence in a single DDIM step from pure noise, producing smooth action chunks at 84 ms per action chunk on consumer hardware and avoiding the cost of full video generation. Across simulation benchmarks and real-robot experiments, TAPESTRY achieves strong performance with substantially lower inference cost than comparable joint video--action policies. More information can be found at https://tapestry-wam.github.io.

</details>

---

### [[20_Research/Papers/强化学习/SetGRPO_Calibrating_Grader-Induced_Policy_Optimization|SetGRPO: Calibrating Grader-Induced Policy Optimization]]

![[assets/2610.36807_figure.png|800]]

- **arXiv**: [2610.36807](https://arxiv.org/abs/2610.36807)
- **PDF**: https://arxiv.org/pdf/2610.36807
- **详细分析**: [[20_Research/Papers/强化学习/SetGRPO_Calibrating_Grader-Induced_Policy_Optimization|SetGRPO: Calibrating Grader-Induced Policy Optimization]]
- **作者**: Jiale Huang, Zixu Li, Zhiwei Chen, Zhiheng Fu, Jinhe Bi, Yupeng Hu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SetGRPO: Calibrating Grader-Induced Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：G-Eval, MT-Bench, RewardBench, RuscaRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rubric-based reinforcement learning uses fine-grained grader feedback to train large language models on open-ended tasks, but grader randomness can alter GRPO updates in ways that score discrepancies alone cannot characterize. Because GRPO jointly normalizes rewards within each response group and combines the resulting training coefficients with response-level gradients, a scoring discrepancy can shift the coefficients of the entire group and induce policy-dependent update changes. Selective execution further affects the direction-reversal risk of retained updates. To address this, we propose Set-Valued Group Relative Policy Optimization (SetGRPO). It comprises three modules: (a) Joint Reward Set Calibration constructs a joint uncertainty set for the training coefficients; (b) Geometry-Guided Safe Recovery maps candidate coefficients into the current policy's local update geometry and determines the largest safe recovery ratio for each response group; and (c) Selective Risk-Gated Optimization selects a global threshold through independent risk calibration to control the conditional direction-reversal risk of accepted updates while preserving the original GRPO objective. Under exchangeability, SetGRPO provides finite-sample marginal coverage for the joint coefficient set and simultaneous risk control across candidate thresholds. On ten open-ended benchmarks spanning three domains, SetGRPO achieves the highest macro average among all compared training methods on both Qwen3.5 and Llama3.2 model families.

</details>

---

### [[20_Research/Papers/具身智能/Making_Self-Driving_Laboratories_Auditable_A_Unified_Framework_for_Hybrid_Actions,Measurements,_and_Safe_Execution|Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution]]

![[assets/2610.36761_figure.png|800]]

- **arXiv**: [2610.36761](https://arxiv.org/abs/2610.36761)
- **PDF**: https://arxiv.org/pdf/2610.36761
- **详细分析**: [[20_Research/Papers/具身智能/Making_Self-Driving_Laboratories_Auditable_A_Unified_Framework_for_Hybrid_Actions,Measurements,_and_Safe_Execution|Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution]]
- **作者**: Zihan Zhang, Zeyu Wu, Xin Zhang, Mingyu Luo, Haohui Que, Tong Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Making Self-Driving Laboratories Auditable:A Unified Framework for Hybrid Actions,Measurements, and Safe Execution》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：L3-Bench, LabVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-driving laboratories (SDLs) are laboratory systems that couple experimental planning, automated execution, and measurement feedback in a closed loop. Integrating flexible robot control with the typed application programming interfaces (APIs) and continuous measurements exposed by laboratory instruments remains an execution-interface challenge. To address this challenge, we propose a traceable framework comprising four components: LAM (Lab Action Model), OpenSDL, Safe-SDL, and L3-Bench. LAM is a proposed measurement-conditioned policy architecture that extends vision-language-action paradigms to generate both continuous robot trajectories and typed instrument API calls. OpenSDL is an execution substrate with an initial control implementation, designed to map role-level operations to heterogeneous devices, coordinate execution, and record timestamped causal events. The proposed Safe-SDL runtime gate combines pre-dispatch schema and resource checks with signal temporal logic monitoring during execution, including extended waiting periods. L3-Bench (Level-3 Laboratory Benchmark) specifies an episode-level evaluation protocol covering physical outcomes, timing, reproducibility, safety violations, and fault recovery. Together, these components provide an end-to-end design for linking hybrid action generation, monitored device execution, measurement feedback, and experimental evaluation, addressing coordination and traceability challenges in SDL workflows.

</details>

---

### [[20_Research/Papers/具身智能/TOPS_Reshaping_Flow_Source_and_Transport_for_Multi-Task_Robot_Manipulation|TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation]]

![[assets/2610.36694_figure.png|800]]

- **arXiv**: [2610.36694](https://arxiv.org/abs/2610.36694)
- **PDF**: https://arxiv.org/pdf/2610.36694
- **详细分析**: [[20_Research/Papers/具身智能/TOPS_Reshaping_Flow_Source_and_Transport_for_Multi-Task_Robot_Manipulation|TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation]]
- **作者**: Tuo An, Chuhao Zhou, Jiahua Dong, Jingliang Li, Jiaqi Bai, Jindou Jia, Jianfei Yang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TOPS: Reshaping Flow Source and Transport for Multi-Task Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based policies for language-conditioned multi-task manipulation commonly share a single $\textit{Gaussian}$ source prior and a common linear transport path across tasks. However, reliably executing multiple tasks with distinct motion requirements remains challenging for a shared policy. We introduce $\textbf{TOPS}$ ($\textbf{T}$ask-$\textbf{O}$riented $\textbf{P}$riors and $\textbf{S}$chedules), which adapts the flow source prior and interpolation schedule to each task without modifying the network architecture. TOPS first constructs multimodal task sources from reverse-mapped expert action sequences, allowing language instructions to select where generation begins. Guided by source-target covariance mismatch, it then slows the transition toward expert actions early in denoising and accelerates it later along directions requiring expansion. Under a $\textit{Gaussian}$ endpoint model, our analysis shows that this schedule adjustment can lower an upper bound on velocity-prediction risk. Experiments on LIBERO, LIBERO-Plus, and CALVIN demonstrate improved performance across in-distribution, perturbation and cross-environment settings, alongside better data efficiency. Using one integration step, TOPS raises LIBERO-10 success from $53.44\%$ to $69.67\%$ compared with ten-step Standard Flow Matching (FM), while reducing inference time to approximately one-sixth of the baseline. TOPS also yields consistent gains when transferred to the large-scale flow-based $π_{0.5}$ policy across all four evaluated settings. Real-world experiments further demonstrate improved task success, including an increase from $20\%$ with standard FM to $80\%$ with TOPS on the upper-drawer opening task.

</details>

---

### [[20_Research/Papers/具身智能/Adapting_Video_Models_for_Robot_Control_via_Motion-guided_Asymmetric_Prediction|Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction]]

![[assets/2610.36624_figure.png|800]]

- **arXiv**: [2610.36624](https://arxiv.org/abs/2610.36624)
- **PDF**: https://arxiv.org/pdf/2610.36624
- **详细分析**: [[20_Research/Papers/具身智能/Adapting_Video_Models_for_Robot_Control_via_Motion-guided_Asymmetric_Prediction|Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction]]
- **作者**: Taeyoung Kim, Junyoung Sung, Heeseung Kwon, Minseop Kim, Jinwoo Shin
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，机器人 1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Adapting Video Models for Robot Control via Motion-guided Asymmetric Prediction》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) leverage pretrained video generative models for robotic control by jointly predicting future visual observations and actions. The visual prediction objective plays a key role in adapting pretrained video representations to the target robot domain. Yet standard visual prediction inherited from video pretraining treats all visual regions uniformly, despite their differing relevance to robotic control. We therefore investigate the spatial allocation of visual supervision in WAMs and show that focusing supervision on dynamic regions can substantially improve policy performance. Building on this finding, we introduce Motion-Guided Asymmetric Prediction (MoGAP), which augments WAM training with motion-focused visual prediction. MoGAP allocates noise asymmetrically across regions, training the model to reconstruct more heavily corrupted dynamic regions using less corrupted static regions as context. MoGAP is trained alongside standard video-action prediction through a training-only auxiliary prediction path within the shared video diffusion backbone. It uses motion cues derived directly from training videos, requiring neither an external teacher nor additional modalities. Across robot manipulation benchmarks and WAM architectures, MoGAP consistently improves policy performance, increasing success rates on the GR-1 tabletop benchmark from 38.8% to 47.5% for Fast-WAM (Wan2.2-5B) and from 52.3% to 62.3% for Cosmos3-Nano.

</details>

---

### [[20_Research/Papers/大模型/Benchmarking_LLM_Agents_for_Behaviorally_Adequate_Test_Generation_from_Software_Requirements|Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements]]

![[assets/2610.36584_figure.png|800]]

- **arXiv**: [2610.36584](https://arxiv.org/abs/2610.36584)
- **PDF**: https://arxiv.org/pdf/2610.36584
- **详细分析**: [[20_Research/Papers/大模型/Benchmarking_LLM_Agents_for_Behaviorally_Adequate_Test_Generation_from_Software_Requirements|Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements]]
- **作者**: Binhang Qi, Yiming Liu, Yun Lin, Yangjie Zhou, Hailong Sun, Jin Song Dong
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Benchmarking LLM Agents for Behaviorally Adequate Test Generation from Software Requirements》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DevBench, Req2Test-Bench, SWT-Bench, TestBench, TestGenEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model agents increasingly compile natural-language requirements into repository-level code, requirement-to-test generation grows in importance to provide validation constraints (or harness) to guide code generation. Yet it remains unclear whether current agents can generate tests that validate the required behavior when the implementation of that behavior is withheld. Existing test-generation benchmarks mostly focus on white-box testing, whereas the requirement--test-related study usually requires evaluation on semantic alignment between the given documents and the generated tests. We introduce Req2Test-Bench, a benchmark containing 5,086 execution-validated instances recovered from developer-authored behavior-driven development (BDD) artifacts in 8 open-source projects, spanning 5 programming languages and 4 BDD frameworks. Each instance pairs a natural-language requirement in Gherkin with its developer-written Test Implementation. Given the requirement, target interfaces of the required behavior, an agent must generate a complete, potentially multi-file Test Implementation. Evaluation of 8 agent--model--reasoning configurations reveals a substantial gap between execution success and behavioral adequacy, which is measured strictly as kill-completeness: a kill-complete test kills every mutant that the ground-truth test kills. The best-performing configuration, Codex with DeepSeek-V4.1-Flash, produces passing tests for 82.8% of instances, yet only 33.8% are behaviorally adequate. We find that (1) scaling up agents yields sharply diminishing returns in behavioral adequacy relative to generation cost; (2) under-specified requirements cause the information gap, including ambiguous setup and implicit expected outcomes; and (3) requirement-grounded harnesses that steer agent non-determinism offer a promising direction for improvement.

</details>

---

### [[20_Research/Papers/具身智能/REACH_An_RL-based_Hierarchical_Humanoid_Crawling_Framework_for_Adaptable_Confined_Space_Traversal|REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal]]

![[assets/2610.36546_figure.png|800]]

- **arXiv**: [2610.36546](https://arxiv.org/abs/2610.36546)
- **PDF**: https://arxiv.org/pdf/2610.36546
- **详细分析**: [[20_Research/Papers/具身智能/REACH_An_RL-based_Hierarchical_Humanoid_Crawling_Framework_for_Adaptable_Confined_Space_Traversal|REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal]]
- **作者**: Shengzhang Xu, Yuning Guo, Weiyi Hu, Yifeng Xu, Zhongyu Li, He Kong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《REACH: An RL-based Hierarchical Humanoid Crawling Framework for Adaptable Confined Space Traversal》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid locomotion in confined spaces requires continuous height adaptation across multiple locomotion modes, yet most existing approaches remain limited to height-adjustable bipedal walking. We present REACH, an RL-based hierarchical framework that enables a Unitree G1 humanoid to traverse height-constrained environments through variable-height bipedal walking and crawling. The learned policies regulate body height over complementary command ranges of 1.27--0.50m in bipedal locomotion and 0.50--0.20m in crawling, extending traversal beyond the clearance limits of crouched walking. To address contact-rich crawling dynamics, we employ a history-conditioned latent representation that captures terrain and interaction context from proprioceptive observations. A bidirectional transition policy further connects crouched bipedal locomotion and crawling across large kinematic and contact discontinuities. These skills are integrated with a LiDAR-based planner that converts point clouds into collision-free three-dimensional paths and locomotion commands, including proactive height targets. Real-world experiments demonstrate accurate height and velocity tracking, robust terrain traversal, reliable mode transitions and confined-space traversal with the proposed pipeline. Code and videos are available at https://aislab-sustech.github.io/REACH/.

</details>

---

### [[20_Research/Papers/具身智能/RoboAuto_Autonomous_Robot_Program_Search_through_Multi-Level_Physical_Understanding|RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding]]

![[assets/2610.36533_figure.png|800]]

- **arXiv**: [2610.36533](https://arxiv.org/abs/2610.36533)
- **PDF**: https://arxiv.org/pdf/2610.36533
- **详细分析**: [[20_Research/Papers/具身智能/RoboAuto_Autonomous_Robot_Program_Search_through_Multi-Level_Physical_Understanding|RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding]]
- **作者**: Buzhao Liu, Jianing Ye, Xiu Yuan, Yangtong Feng, Chengsong Huang, Tyler Dinh, Yevgeniy Vorobeychik, Ning Zhang, Chongjie Zhang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.55（加权：具身智能 0.9，大模型 0.35，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《RoboAuto: Autonomous Robot Program Search through Multi-Level Physical Understanding》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, LLM-based autonomous agents have shown strong capabilities in iteratively generating, evaluating, and refining executable solutions. In robotic manipulation, Code-as-Policy lets these agents search over modular and editable robot programs. However, effective program search requires physical understanding: agents must understand how objects can be manipulated, how scene geometry constrains actions, and why interactions succeed or fail. Existing methods rely mainly on execution feedback for program refinement, often leaving these physical questions unresolved. We introduce RoboAuto, a framework for robot program search that explicitly organizes physical understanding at the object, scene, and interaction levels through three components. First, a hierarchical knowledge base combines executable skills with object-centric knowledge of affordances, spatial relations, and action effects, learned from embodied data and online task solving. Second, scene grounding connects this knowledge to the current environment by identifying relevant objects and resolving action-critical quantities. Third, multi-stage planning with self-designed experiments checks whether each stage produces its expected physical effects and actively tests competing hypotheses to resolve physical uncertainties. RoboAuto achieves superior performance across five benchmark families, attaining an 89.1% success rate on short-horizon LIBERO-PRO tasks and more than twice the mean success rate of ASPIRE on LIBERO-PRO Long and LIBERO-Plus. It also outperforms ASPIRE and $π_{0.5}$ on three challenging long-horizon real-robot tasks requiring precise manipulation. We further show that the knowledge base transfers across simulators and embodiments, and that program search performance scales with its size. Project page: https://roboauto-ai.github.io/

</details>

---

### [[20_Research/Papers/大模型/CogArena_Benchmarking_Multimodal_Agents_on_Interactive_Behavioral_Experiments|CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments]]

![[assets/2610.36484_first_page.png|800]]

- **arXiv**: [2610.36484](https://arxiv.org/abs/2610.36484)
- **PDF**: https://arxiv.org/pdf/2610.36484
- **详细分析**: [[20_Research/Papers/大模型/CogArena_Benchmarking_Multimodal_Agents_on_Interactive_Behavioral_Experiments|CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments]]
- **作者**: Kianté Fernandez, Caitlin Chen, Jialu Zhou, Bartek Sadowski, Anthony C. Miceli, Ian Krajbich
- **cs 子类**: cs.AI, cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《CogArena: Benchmarking Multimodal Agents on Interactive Behavioral Experiments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CogBench, GameWorld, TurkingBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Claims about the cognitive capabilities of large language models are typically tested by translating behavioral paradigms into text prompts, bypassing the visual interfaces and time pressure through which human participants actually engage with experiments. At the same time, AI agents can now complete online behavioral tasks and produce human-like data, which raises concerns that online datasets in the social and behavioral sciences are increasingly open to contamination. We introduce CogArena, a benchmark of ten experimental paradigms from the social and behavioral sciences. Agents complete the experiments through a standard web browser, working with the same visual stimuli and response interfaces that online participants use. A three-level scoring procedure evaluates whether the agent completed the task, how accurately it performed, and whether its data show the behavioral signatures each paradigm reliably produces in people. Across four multimodal models, each run ten times per task, we find that finishing an experiment and reproducing its signatures are different things. Many sessions did not finish, and those that did reproduced some signatures reliably and others not at all. CogArena provides the tasks, scoring code, and a public leaderboard for new submissions.

</details>

---

### [[20_Research/Papers/大模型/When_to_Intervene_An_Empirical_Study_of_Errors_and_Self-Recovery_in_LLM_Agents|When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents]]

![[assets/2610.36471_figure.png|800]]

- **arXiv**: [2610.36471](https://arxiv.org/abs/2610.36471)
- **PDF**: https://arxiv.org/pdf/2610.36471
- **详细分析**: [[20_Research/Papers/大模型/When_to_Intervene_An_Empirical_Study_of_Errors_and_Self-Recovery_in_LLM_Agents|When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents]]
- **作者**: Chiming Duan, Tong Jia, Yingxi Chen, Minghua He, Lingzhe Zhang, Ying Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When to Intervene? An Empirical Study of Errors and Self-Recovery in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OSWorld, ReInBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents interact with Web services to perform tasks on users' behalf. Errors during these interactions can disrupt execution and prevent task completion, motivating external intervention. However, agents may self-recover through continued execution, raising the question of when to intervene and when to wait for self-recovery. We present an empirical study of errors and self-recovery in LLM agents. We construct ReInBench, a dataset containing 1,259 agent traces and 1,403 error events across computer-use and Web tasks. Our study examines how often and how quickly agents self-recover, how self-recovery relates to subsequent execution and task completion, and whether self-recovery can be predicted when an error occurs. We find that 725 error events self-recover, often within a few steps, with self-recovery performance differing across Execution LLMs. Self-recovery can also help agents recover from subsequent errors of the same type and support overall task completion. Intervention should therefore prioritize errors unlikely to self-recover, while allowing agents to continue when self-recovery is likely. Building on these empirical findings, we propose ReCoF, a method that predicts whether an error will self-recover to inform whether additional intervention is needed. ReCoF achieves an average relative improvement of 9.02% in Macro-F1 over the strongest baseline on ReInBench. Our code and data can be found at https://method-notes.github.io/ReCoF/.

</details>

---

### [[20_Research/Papers/大模型/Correction_or_Manipulation_Measuring_Epistemic_Vigilance_in_LLM_Agents_Under_User_Pressure|Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure]]

![[assets/2610.36453_figure.png|800]]

- **arXiv**: [2610.36453](https://arxiv.org/abs/2610.36453)
- **PDF**: https://arxiv.org/pdf/2610.36453
- **详细分析**: [[20_Research/Papers/大模型/Correction_or_Manipulation_Measuring_Epistemic_Vigilance_in_LLM_Agents_Under_User_Pressure|Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure]]
- **作者**: Nardine Basta, Venus Haghighi, Dali Kaafar, Amin Beheshti
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Correction or Manipulation? Measuring Epistemic Vigilance in LLM Agents Under User Pressure》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents that answer questions and act on behalf of users must decide when to yield to a user who disagrees. Disagreement may correct a genuine error or may be an attempt at manipulation. Prior work shows that models frequently abandon correct answers when challenged by users, yet it remains unclear whether they distinguish correction from manipulation or merely differ in their propensity to concede. We examine this question across seven LLMs from four vendors in two studies, one on the answers agents give and one on the actions they take as customer-support agents whose policy permits account changes only for verified users. Simulated users push toward correct and incorrect answers with graded pressure. Following research on epistemic vigilance, the pressure either appeals to the source, such as claimed authority, or offers content the agent cannot verify, namely a cited source. Drawing on signal detection theory, we measure on a set of benchmark questions how much more readily each agent concedes to correction than to manipulation, separately from its overall propensity to concede. Citations made five of seven models readier to concede and four worse at discriminating, while stronger wording added little. In the agentic study, five models never violated the verification policy, including models that readily abandoned correct answers, so concession on answers did not predict violations of policy. Ministral 3B violated the policy mainly under claimed authority, and Ministral 8B reported changes it had not made. An instruction to revise only on verifiable evidence chiefly shifted propensity to concede rather than improving discrimination. Concession rates alone are therefore misleading, and agents should be evaluated on both their discrimination and the actions they take.

</details>

---

### [[20_Research/Papers/大模型/RouteDRAG_Learning_to_Route_and_Control_Agentic_Execution_for_Multimodal_Document_RAG|RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG]]

![[assets/2610.36444_figure.png|800]]

- **arXiv**: [2610.36444](https://arxiv.org/abs/2610.36444)
- **PDF**: https://arxiv.org/pdf/2610.36444
- **详细分析**: [[20_Research/Papers/大模型/RouteDRAG_Learning_to_Route_and_Control_Agentic_Execution_for_Multimodal_Document_RAG|RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG]]
- **作者**: Zekai Chen, Hao Zhu, Yu Liu, Xunkai Li, Zejian Kang, Rui Qian, Quanjiang Li, Rong-Hua Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《RouteDRAG: Learning to Route and Control Agentic Execution for Multimodal Document RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DocBench, MMLongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web-based applications increasingly rely on understanding long multimodal documents, where answering questions often requires combining information across pages, tables, and figures. Agentic retrieval-augmented generation addresses these tasks through iterative retrieval and reasoning. However, Agentic execution is not always necessary, introducing additional computation and potentially incorrect answers. Our empirical analysis reveals that Agentic execution provides query-dependent benefits, while additional operations may improve, preserve, or degrade answer accuracy. These findings motivate controlling both Agent invocation and subsequent execution. To address these challenges, we propose RouteDRAG, a learning-based framework comprising four components. Unified Document Index organizes multimodal content into a graph-backed index and derives query representations from initial retrieval. Adaptive Path Routing preserves exact answering and predicts the relative benefit of Agent over shorter execution paths. Dynamic Agent Execution maintains an evolving workspace and refines Planner proposals to control tool use and termination. Sequential Policy Learning first trains operation control from observed outcomes and then trains path routing using the resulting Agent's performance. Across two benchmarks, RouteDRAG achieves an average accuracy improvement of 3.47 percentage points over shorter-path-only execution while assigning only 79.3% of queries to Agent. Notably, it also surpasses uniform Agent execution on both benchmarks while requiring fewer answering calls. Our code is now available at https://github.com/Ereshkigal1/RouteDRAG.

</details>

---

### [[20_Research/Papers/大模型/LM-DSB_A_Lightweight_Multi-agent_System_for_Automated_Daily_Safety_Bulletin_Generation_in_Construction|LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction]]

![[assets/2610.36433_first_page.png|800]]

- **arXiv**: [2610.36433](https://arxiv.org/abs/2610.36433)
- **PDF**: https://arxiv.org/pdf/2610.36433
- **详细分析**: [[20_Research/Papers/大模型/LM-DSB_A_Lightweight_Multi-agent_System_for_Automated_Daily_Safety_Bulletin_Generation_in_Construction|LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction]]
- **作者**: Xianxiang Zhao, Advik Mehta, Falak Sethi, Brian Gue, Qipei Mei, Lingzi Wu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《LM-DSB: A Lightweight Multi-agent System for Automated Daily Safety Bulletin Generation in Construction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Construction safety management still struggles to produce daily safety bulletins (DSBs), structured daily communications that identify site-specific hazards, convey safety protocols, and set preventive measures for workers. Manual DSB creation takes 2-3 hours daily and yields inconsistent quality, with 25% of crews never conducting pretask planning (Olson et al., 2016), diverting safety personnel from field supervision. This study proposes the Lightweight Multi-Agent DSB System (LM-DSB), which integrates retrieval-augmented generation (RAG) with a locally deployable Large Language Model (LLM) to automate DSB generation on consumer-grade personal computers. LM-DSB coordinates specialized planner, researcher, and writer agents in a hierarchical architecture, enhanced by domain-specific fine-tuning on construction safety documentation and RAG grounding in 37 health, safety, and environment (HSE) documents. A two-phase validation assessed feasibility. Phase 1 comparative evaluation showed the multi-agent RAG system (Llama 3-8B) outperformed all alternative configurations, with strong lexical alignment and coherence (TF-IDF: 0.70, BLEU: 0.39, ROUGE-1: 0.66) and near-complete document generation (length ratio: 1.01 vs. 0.39 for single-agent RAG). Phase 2 expert evaluation (N=40) confirmed practical acceptability (mean scores 3.50-4.20 on a 5-point scale), particularly in regulatory compliance (4.20) and factual accuracy (4.10). The findings show that architectural design enables lightweight models to handle safety-critical documentation on consumer-grade hardware, advancing technology democratization in construction safety management. Limitations include knowledge base scope, language constraints, and lack of field deployment validation; future work should address multimodal integration and workflow adoption.

</details>

---

### [[20_Research/Papers/大模型/Repulsive_Population_Policy_Gradients_for_Behaviorally_Diverse_Reinforcement_Learning|Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning]]

![[assets/2610.36425_figure.png|800]]

- **arXiv**: [2610.36425](https://arxiv.org/abs/2610.36425)
- **PDF**: https://arxiv.org/pdf/2610.36425
- **详细分析**: [[20_Research/Papers/大模型/Repulsive_Population_Policy_Gradients_for_Behaviorally_Diverse_Reinforcement_Learning|Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning]]
- **作者**: Saeed Hedayatian, Harsh Shah, Celine Mneimneh, Stefanos Nikolaidis
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Repulsive Population Policy Gradients for Behaviorally Diverse Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DCRL, QD-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The goal of Quality-Diversity Reinforcement Learning (QD-RL) is to find a population of high-performing policies that solve a decision-making problem in diverse ways. Despite recent progress, QD-RL methods predominantly rely on evolutionary operators--including black-box optimizers, mutations, and crossovers--to facilitate exploration and induce diversity. Scaling these methods becomes increasingly costly as policies and behavior spaces grow larger. Building on the Soft QD view of quality-diversity optimization, we introduce \textbf{Re}pulsive \textbf{P}opulation \textbf{P}olicy \textbf{O}ptimization (\textbf{RePPO}), which adapts PPO to jointly optimize a compact population of diverse, high-quality policies using a population-dependent, dynamically shaped reward. On standard continuous-control tasks, RePPO achieves a strong quality-diversity tradeoff compared with state-of-the-art QD-RL methods. Ablations further characterize this tradeoff by examining how each component affects individual quality and collective diversity. To assess RePPO's scalability, we extend our evaluation to learning from pixels and fine-tuning large language models. In pixel-based tasks, where large policies make most traditional QD-RL methods infeasible, RePPO maintains quality on par with standard PPO while achieving substantially higher diversity. Its successful application to language model fine-tuning further demonstrates, for the first time, that QD-RL methods can scale to this domain. Together, these results show that directly optimizing compact populations with RePPO provides a scalable approach to QD-RL across increasingly complex domains.

</details>

---

### [[20_Research/Papers/大模型/HIDRA_Hierarchical_Dual-Routing_Attention_for_Replay-Free_Lifelong_Imitation_Learning|HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning]]

![[assets/2610.36374_figure.png|800]]

- **arXiv**: [2610.36374](https://arxiv.org/abs/2610.36374)
- **PDF**: https://arxiv.org/pdf/2610.36374
- **详细分析**: [[20_Research/Papers/大模型/HIDRA_Hierarchical_Dual-Routing_Attention_for_Replay-Free_Lifelong_Imitation_Learning|HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning]]
- **作者**: Fanqi Yu, Matteo Tiezzi, Cigdem Beyan, Tommaso Apicella, Vittorio Murino
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HIDRA: Hierarchical Dual-Routing Attention for Replay-Free Lifelong Imitation Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic agents operating in real-world environments must adapt continuously from a stream of multimodal demonstrations, often under constraints that preclude storing or revisiting past data. In this replay-free, single-pass lifelong imitation learning setting, sequential updates can progressively distort the representation space, making expert-based approaches particularly sensitive to routing interference, causing expert selection to degrade over time. We propose HIDRA, a structured routing framework that mitigates this issue through a hierarchical dual-attention mechanism, which decouples instruction-level expert retrieval from context-dependent refinement. To further stabilize routing under representation drift, HIDRA introduces a key-level geometric regularization that enforces both alignment within tasks and separation across tasks. The resulting approach enables reliable expert selection while supporting an expandable set of experts for continual adaptation. We evaluate HIDRA on several LIBERO benchmark suites, including more challenging variants with heterogeneous task sequences and paraphrased language instructions. Our approach consistently outperforms both replay-free and replay-based baselines, improving AUC and forward transfer while maintaining low forgetting, with stronger gains under high interference and language variation. The code is available at: https://github.com/yfqi/HIDRA.

</details>

---

### [[20_Research/Papers/大模型/OA-RAG_Ontology-based_Agentic_RAG_for_Faithful_LLM_Reasoning|OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning]]

![[assets/2610.36335_first_page.png|800]]

- **arXiv**: [2610.36335](https://arxiv.org/abs/2610.36335)
- **PDF**: https://arxiv.org/pdf/2610.36335
- **详细分析**: [[20_Research/Papers/大模型/OA-RAG_Ontology-based_Agentic_RAG_for_Faithful_LLM_Reasoning|OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning]]
- **作者**: Hui Yang, Jiaoyan Chen, Yongsheng Gao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《OA-RAG: Ontology-based Agentic RAG for Faithful LLM Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) perform well across many real-world tasks but remain prone to hallucination, limiting their reliability in domains such as biomedicine and healthcare, where answers must be grounded in established knowledge. Retrieval-augmented generation (RAG) mitigates this problem by incorporating external information, but often overlooks logical relationships and relies heavily on the LLM's own reasoning, which can compromise answer faithfulness. We propose OA-RAG, an agent that integrates formal reasoning with LLM reasoning, drawing on both the logical structure and informal annotations of domain ontologies. For each answer, OA-RAG reports the ontology observations used as evidence and a model-assessed grounding level (entailed, supported, related, or unrelated) that characterises the strength of that evidence. Across benchmarks derived from three large-scale ontologies and six real-world medical question-answering tasks, OA-RAG achieves the best overall performance among the evaluated ontology-fine-tuned and popular RAG methods, with particularly strong results on reasoning-intensive tasks. The reported grounding levels also offer a useful indication of answer reliability, with stronger grounding generally associated with higher accuracy. Finally, our results demonstrate the value of ontologies as knowledge sources: OA-RAG is competitive with, and sometimes outperforms, domain-specific RAG systems that draw on sources such as textbooks.

</details>

---

### [[20_Research/Papers/大模型/Context_Is_a_Pipeline,_Not_a_Window_Information_Attrition_in_LLM_Agent_Harnesses|Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses]]

![[assets/2610.36114_first_page.png|800]]

- **arXiv**: [2610.36114](https://arxiv.org/abs/2610.36114)
- **PDF**: https://arxiv.org/pdf/2610.36114
- **详细分析**: [[20_Research/Papers/大模型/Context_Is_a_Pipeline,_Not_a_Window_Information_Attrition_in_LLM_Agent_Harnesses|Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses]]
- **作者**: Yuvraj Sehgal, Mahsa Panahandeh, Naser Ezzati-Jivan
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Context Is a Pipeline, Not a Window: Information Attrition in LLM Agent Harnesses》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are judged by two numbers: the size of the context window, and how often the final answer is correct. Both numbers miss a third thing: how much of a tool's output is lost before the model ever sees it. We measured this loss in a real tool-using agent. The agent finds the cause of injected faults by reading Linux kernel traces. The context window was almost empty: across 720 runs, the single largest prompt used only 5.75% of it. Yet a third of all tool results (3,827 of 11,189) were cut before they reached the model, and every cut result became broken JSON. The harness cut each result by slicing its JSON text at a fixed length. This does not shorten a result evenly. It deletes whatever data sits near the end. One field reached the model in only 4.7% of calls. A second field, in the very same results, reached the model in 99.3% of calls. Which field held the fault's evidence depended on when the faulty process started: early or late in the trace. The agent's diagnosis accuracy matched this same split. So we ran controlled experiments to test one question: did the data loss cause the drop in accuracy? This paper makes four contributions. First, we model an agent's context as a five-stage pipeline, with a measured failure at each stage. Second, we replay 864 real tool results, including one from a production trace where the shipped cut deletes all 128 records of the fault's evidence. Third, a controlled experiment shows that the cut's real cost appears first as extra work, not as wrong answers: 43% more tool calls, twice the computation, and yield falling from 0.61 to 0.31. The agent still finds the right answer when it has another way to reach it. Fourth, a survey of seven agent frameworks finds two that cut tool output the same unsafe way. Whether the data cut truly causes the accuracy drop is still an open question.

</details>

---

### [[20_Research/Papers/具身智能/The_Trinity_Capability-Driven_Recursive_Self-Improvement_for_Multimodal_Agents|The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents]]

![[assets/2610.36077_figure.png|800]]

- **arXiv**: [2610.36077](https://arxiv.org/abs/2610.36077)
- **PDF**: https://arxiv.org/pdf/2610.36077
- **详细分析**: [[20_Research/Papers/具身智能/The_Trinity_Capability-Driven_Recursive_Self-Improvement_for_Multimodal_Agents|The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents]]
- **作者**: Weidong Tang, Ruiheng Wang, Jingxuan Zhang, Hexin Wang, Haoyuan Chen, Zhengfeiyang Zhang, Yixing Ma, Zichen Jiang, Ziyu Guo, Haodong Li, Zhengbo Jiao, Zhiqing Cui...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.8）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《The Trinity:Capability-Driven Recursive Self-Improvement for Multimodal Agents》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal intelligence can be viewed as human-guided co-evolution between worlds and agents through interaction. However, scaling this process faces two bottlenecks: constructing heterogeneous, verifiable environments is costly, and manual Harness iteration cannot keep pace with growing task diversity and complexity. A key insight is that tasks with different modalities and surface forms can share the same underlying capability requirements. We therefore introduce The Trinity, a recursive self-improvement framework coupling world generation with Harness evolution through three roles: Creator, Explorer, and Evolver. Drawing on verified execution trajectories, Evolver shifts the basis of task organization from surface categories to shared requirements, reorganizing the original task tree into a hierarchical capability tree. We introduce Capability-Driven Real2Sim2Real: for heterogeneous tasks at the same node, Creator abstracts their common requirements into simplified, verifiable simulated worlds for capability learning, while evaluation on original tasks measures transfer. Along this capability tree, Explorer progressively evolves reusable capability modules through selective inheritance, forming a Harness tree whose validated updates accumulate across iterations within a fixed topology. The resulting Harnesses specialize in different capabilities, motivating a Capability-Aware Harness Router that uses public task information to select compatible module configurations from the tree. Our evolved Harnesses improve mean performance by 34 points across 28 training benchmarks and 26 points across 18 unseen benchmarks, including two real-world embodied tasks.

</details>

---

### [[20_Research/Papers/强化学习/Rollback_Experience_Backtracking_in_World_Models_for_Policy_Improvement|Rollback: Experience Backtracking in World Models for Policy Improvement]]

![[assets/2610.36068_figure.png|800]]

- **arXiv**: [2610.36068](https://arxiv.org/abs/2610.36068)
- **PDF**: https://arxiv.org/pdf/2610.36068
- **详细分析**: [[20_Research/Papers/强化学习/Rollback_Experience_Backtracking_in_World_Models_for_Policy_Improvement|Rollback: Experience Backtracking in World Models for Policy Improvement]]
- **作者**: Jiayi Luo, Yang Zhang, Liliang Chen, Nan Wang, Chen Gao, Boxiang Qiu, Zhuoxuan Li, Baorui Peng, Chuankang Li, Yuxiang Yan, Si Liu, Qingyun Sun...
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 2.12（加权：具身智能 0.3，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Rollback: Experience Backtracking in World Models for Policy Improvement》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, IRASim, LingBot-World, OpenVLA, RIPT-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models offer a scalable alternative to costly real-world interaction for improving robot policies. However, existing world-model-based methods largely treat world models as forward-only surrogates of the physical environment, leaving untapped a capability no physical environment affords: rewinding to past decision points to explore counterfactual futures. We introduce Rollback, a policy improvement paradigm that turns world models from passive simulators into counterfactual engines: it rolls back to critical decision points, branches into alternative actions, and contrasts their outcomes to attribute success to individual decisions. This concentrates imagination where it matters most and distills counterfactual outcomes into fine-grained, action-level supervision without a separately learned value model. We build a scalable training system that unifies distributed world-model search with asynchronous real-robot execution, forming a self-reinforcing cycle: real-world experience continually sharpens the world model, and a sharper world model in turn drives further policy improvement. We term the world-model side of this cycle test-time physics grounding, a capability that hand-built physics simulators lack: while the world model serves as the training environment, real transitions from the policy it trains correct its dynamics through a lightweight LoRA pipeline. Experiments on three challenging real-world tasks show that Rollback improves success rates over the strongest baseline by an absolute 10.67%, 11.11%, and 11.85% on block extraction, ball tossing, and tabletop curling, respectively, while achieving more stable improvement throughout training. Although initialized from teleoperated demonstrations far below human level, Rollback surpasses the average success rate of human players on both ball tossing and tabletop curling within 8 hours of training.

</details>

---

### [[20_Research/Papers/具身智能/A_Hyper-Logical_View_on_Multi-Agent_Path_Planning|A Hyper-Logical View on Multi-Agent Path Planning]]

![[assets/2610.35964_first_page.png|800]]

- **arXiv**: [2610.35964](https://arxiv.org/abs/2610.35964)
- **PDF**: https://arxiv.org/pdf/2610.35964
- **详细分析**: [[20_Research/Papers/具身智能/A_Hyper-Logical_View_on_Multi-Agent_Path_Planning|A Hyper-Logical View on Multi-Agent Path Planning]]
- **作者**: Hadar Frenkel, Dor Atzmon
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，机器人 0.8）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《A Hyper-Logical View on Multi-Agent Path Planning》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Agent Path Planning (MAPP) requires collision-free paths for multiple agents. MAPP has numerous real-life applications, including the navigation of automated vehicles, and has therefore many variants considering different constraints, requirements, and objectives. For each such variant, a new algorithmic treatment is often developed. This paper takes a complementary, specification-centered view: we show that many MAPP variants can be modeled in HyperLTL, a temporal logic that reasons about multiple paths and their evolution through time, and in its omega-regular extension HyperQPTL. The contribution is not a claim that current hyperproperty model checkers replace specialized MAPP solvers. Rather, the hyper-logical view gives a unified language for comparing MAPP variants, adding cross-agent constraints, expressing optimality, and connecting MAPP to verification, explanation, and causality techniques for hyperproperties.

</details>

---

### [[20_Research/Papers/具身智能/Curriculum-Driven_Deep_Reinforcement_Learning_for_Autonomous_Far-Range_Rocket_Landing|Curriculum-Driven Deep Reinforcement Learning for Autonomous Far-Range Rocket Landing]]

![[assets/2610.35954_figure.jpg|800]]

- **arXiv**: [2610.35954](https://arxiv.org/abs/2610.35954)
- **PDF**: https://arxiv.org/pdf/2610.35954
- **详细分析**: [[20_Research/Papers/具身智能/Curriculum-Driven_Deep_Reinforcement_Learning_for_Autonomous_Far-Range_Rocket_Landing|Curriculum-Driven Deep Reinforcement Learning for Autonomous Far-Range Rocket Landing]]
- **作者**: Atin Chowdhury, Piyush Joshi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Curriculum-Driven Deep Reinforcement Learning for Autonomous Far-Range Rocket Landing》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous vertical landing of reusable launch vehicles is a critical yet formidable challenge in aerospace engineering, primarily due to highly nonlinear dynamics, stringent precision require- ments, and inherent environmental uncertainties. While reinforcement learning (RL) has emerged as a promising alternative to traditional model-based control, existing approaches frequently rely on flat training paradigms and highly simplified initial conditions, drastically limiting their real-world applicability. This paper proposes a comprehensive curriculum-driven deep reinforcement learning framework designed to master both far-range navigation and precision landing. By employing a three-stage curriculum augmented with a critic warm-up procedure and a rehearsal mechanism to prevent catastrophic forgetting, alongside a high-dimensional observation vector utilizing a full 3 X 3 rotation-matrix, the agent is trained to navigate from an initial horizontal distance of 1,000 to 1,500 units vastly farther than prior benchmarks before executing a soft touchdown. Crucially, we intro- duce a redesigned reward function that reduces unnecessary computational overhead and addresses limitations of earlier formulations, including poorly calibrated reward components and potentially conflicting optimization objectives. The redesigned function bounds the per-step reward magnitude by (O(1)), while its progress term accumulates the total distance closed over the trajectory. The available 100,000-episode results report a 99.98% success rate for the proposed policy and 68.31% for the baseline under the evaluation conditions. In the evaluation, the proposed policy retained 69.1% of its initial fuel capacity and achieved a mean final distance from the pad centre of 7.07 units, compared with 13.10 units for the baseline. Landing visualizations are available in Video 1 and Video 2.

</details>

---

### [[20_Research/Papers/具身智能/Task-Utility_IQA_Rethinking_Image_Quality_Assessment_in_Embodied_Tasks|Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks]]

![[assets/2610.35905_figure.png|800]]

- **arXiv**: [2610.35905](https://arxiv.org/abs/2610.35905)
- **PDF**: https://arxiv.org/pdf/2610.35905
- **详细分析**: [[20_Research/Papers/具身智能/Task-Utility_IQA_Rethinking_Image_Quality_Assessment_in_Embodied_Tasks|Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks]]
- **作者**: Jirong Zha, Yanwei Liao, Yemin Wang, Xiangmin Yi, Siqi Peng, Yingfeng Chen, Chen Gao, Xinlei Chen
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 1.2，大模型 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Task-Utility IQA: Rethinking Image Quality Assessment in Embodied Tasks》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Align-IQA, CLIP-IQA, DepictQA, Embodied-IQA, IQA, MICBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Image quality assessment (IQA) underpins embodied imaging pipelines by judging whether visual quality satisfies downstream tasks, yet most existing methods learn task-agnostic scores aligned with generic human ratings on static benchmarks. This objective mismatches embodied and interactive settings, where image adequacy depends on task goals, context, and action requirements that shape an agent's decisions. We argue that IQA should shift from score regression to goal-conditioned judgment defined by embodied task utility. To this end, we propose an MLLM-based embodied IQA agent framework that reasons about task requirements, grounds quality evidence, and produces decision-facing assessments. A compact VisDrone evidence study shows that conventional perceptual metrics and generic MLLM-based IQA scores are weak proxies for downstream VLM task success, while a task-conditioned utility score better predicts whether visual input supports the target task. These findings support a task-utility-oriented reframing of IQA for embodied, explainable, and decision-aware visual perception.

</details>

---
