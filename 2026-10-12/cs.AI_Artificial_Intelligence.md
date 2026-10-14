# cs.AI | Artificial Intelligence | 2026-10-12

#arxiv #ComputerScience

**论文数**: 28

### [[20_Research/Papers/具身智能/MC-EvoBench_Auditing_Experience-Driven_Self-Improvement_in_Minecraft_Agents|MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents]]

![[assets/2610.13829_figure.png|800]]

- **arXiv**: [2610.13829](https://arxiv.org/abs/2610.13829)
- **PDF**: https://arxiv.org/pdf/2610.13829
- **详细分析**: [[20_Research/Papers/具身智能/MC-EvoBench_Auditing_Experience-Driven_Self-Improvement_in_Minecraft_Agents|MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents]]
- **作者**: Jingwei Song, Zhisheng Chen, Bingfan Zeng, Jing Tang, Yubo Hou, Jinhao Jing, Zhengwei Xie, Linfeng Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.5，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《MC-EvoBench: Auditing Experience-Driven Self-Improvement in Minecraft Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EvoAgentBench, LifelongAgentBench, MC-EvoBench, MineRL, PAST-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A central challenge in embodied recursive self-improvement is enabling agents to convert interaction history into capabilities that persist beyond one world and transfer to later tasks. A saved memory or successful final action does not by itself establish that a reusable capability was acquired; evaluation must separate capability change from carried-over resources, unequal source exposure, and early execution failures. We construct MC-EvoBench as a controlled Minecraft benchmark with a fixed catalog of 19 registered evolution chains, including 12 primary evaluation chains and seven calibration or probe chains, together with three graph-aligned paired probe families for transfer. The benchmark represents each task as a task-state graph, defines stage-level environment verifiers, assigns matched source and target roles, resets the target world, and permits only a declared agent artifact to cross the source-target boundary. For each probe, no-prior, related, unrelated, and shuffled source conditions are evaluated under matched environment-step budgets and five seeds; we report TSR, WGP, and VMP and retain provenance records. The benchmark reveals a consistent direct-capability gap between controller and planner-backed variants, while related experience yields no stable transfer: it does not improve either tool probe, its small wood-species gain hinges on one seed, and all intervals include zero. Stage audits further show that early wood-collection and crafting bottlenecks often leave later capabilities unobserved. MC-EvoBench thus offers a controlled testbed for durable, transferable embodied capabilities. Code and data are available at https://github.com/xzw-ustc/mc-bench-open-source

</details>

---

### [[20_Research/Papers/大模型/Matched-Context_Group_Policy_Optimization_for_LLM_Agent_Training|Matched-Context Group Policy Optimization for LLM Agent Training]]

![[assets/2610.13755_figure.png|800]]

- **arXiv**: [2610.13755](https://arxiv.org/abs/2610.13755)
- **PDF**: https://arxiv.org/pdf/2610.13755
- **详细分析**: [[20_Research/Papers/大模型/Matched-Context_Group_Policy_Optimization_for_LLM_Agent_Training|Matched-Context Group Policy Optimization for LLM Agent Training]]
- **作者**: Chenxu Zhang, Yaorui Shi, Wenlong Zhang, Jianchao Tan, Zihan Wang, Yiming Cheng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.92（加权：大模型 0.8，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Matched-Context Group Policy Optimization for LLM Agent Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training long-horizon language model agents requires assigning credit to intermediate decisions from sparse terminal feedback. Within a finite group of sibling rollouts, useful action comparisons depend on their context, evidence for both alternatives, and how that evidence enters learning. We propose Matched-Context Group Policy Optimization (MCGPO), a procedure for constructing weighted action preferences from already collected trajectories. MCGPO defines comparison contexts with pre-action state summaries and observed rubric progress, annotated by task rules. Two-action support selects among ordered exact and coarse matching rules. Fixed folds separate candidate decisions from the terminal outcomes used to orient their preferences, and support-dependent evidence weights scale an auxiliary pairwise objective alongside shared GraphGPO task learning. MCGPO reuses rollout data and each response's original history, preserving critic-free training. Across six environment-backbone settings with three training seeds each, MCGPO improves mean success over matched GraphGPO: by 0.47-1.46 percentage points on ALFWorld and WebShop with Qwen2.5-1.5B and 7B, and by 3.96 and 5.16 points on WebShop with Qwen3-4B and 8B. The ALFWorld gains build on baseline success above 92%, where remaining headroom is limited. Integrated success improves in three of four Qwen2.5 settings. Three-seed factorial controls support opposite-fold evidence and evidence weighting; joint state-rubric matching achieves the highest mean in all four representation-control settings.

</details>

---

### [[20_Research/Papers/具身智能/SafeDiSTL_Decomposing_Joint_Constraints_for_Safe_Multi-Agent_Reinforcement_Learning|SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning]]

![[assets/2610.13737_figure.png|800]]

- **arXiv**: [2610.13737](https://arxiv.org/abs/2610.13737)
- **PDF**: https://arxiv.org/pdf/2610.13737
- **详细分析**: [[20_Research/Papers/具身智能/SafeDiSTL_Decomposing_Joint_Constraints_for_Safe_Multi-Agent_Reinforcement_Learning|SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning]]
- **作者**: Hongrui Zheng, Aditya Singh, Rahul Mangharam
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《SafeDiSTL: Decomposing Joint Constraints for Safe Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL, SafeMARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-agent tasks often impose constraints on a shared objective or collective safety. A team level violation cost function can measure this constraint outcome, but does not distinguish which agents' actions most strongly influence that violation. We present SafeDiSTL, a constrained multi-agent reinforcement learning framework that allows for credit assignment even with joint constraint measurements. We use Signal Temporal Logic (STL) robustness to measure episode-level violation through running-maximum cost increments. Smooth full-episode robustness and differentiable dynamics provide action sensitivities, which allocate each cost increment across agents at the same decision time. These sensitivities account for delayed effects when weighting agents' shares of each cost increment. We study the framework in cooperative payload transport, connected navigation, and networked traffic control tasks. SafeDiSTL achieves 1.6-5.1x the safe-success rate in transport, improves navigation safe-success by 11.1%, and delivers 50-68% more throughput in traffic when compared to constrained baselines. Results demonstrate a strong improvement of the learned policy in dealing with shared constraint while retaining the performance of unconstrained policies.

</details>

---

### [[20_Research/Papers/具身智能/LAPT-Scale_Scaling_Embodied_Policies_with_Latent_Action_Pre-Training_on_Human_Videos|LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos]]

![[assets/2610.13732_figure.png|800]]

- **arXiv**: [2610.13732](https://arxiv.org/abs/2610.13732)
- **PDF**: https://arxiv.org/pdf/2610.13732
- **详细分析**: [[20_Research/Papers/具身智能/LAPT-Scale_Scaling_Embodied_Policies_with_Latent_Action_Pre-Training_on_Human_Videos|LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos]]
- **作者**: Zhiyuan Xiang, Peidong Liu, Mingyang Li, Jiawei Li, Wenhow Li, Wenbo Ding, Xiang Deng
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LAPT-Scale: Scaling Embodied Policies with Latent Action Pre-Training on Human Videos》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling generalist robotic policies is limited by the high cost of collecting embodied interaction data. Large-scale egocentric human videos offer a rich alternative, but they lack robot action labels, and existing action annotation methods are often noisy under real-world visual complexity and diverse manipulation dynamics. We introduce LAPT-Scale, a scalable latent action pre-training paradigm with two components: LAPT-Scale-LAM learns continuous latent actions by explaining frame-to-frame visual transitions in human videos and uses them as human-derived supervision, while LAPT-Scale-Policy trains a VLA policy through human-video latent-action pre-training, target-robot embodiment alignment, and task-specific post-training. Unlike prior vector-quantized LAMs, LAPT-Scale-LAM uses a continuous latent space to preserve fine-grained motion and interaction dynamics. We further combine perceptual, semantic, and optical-flow alignment signals to improve transition-level supervision beyond pixel reconstruction. Trained on 23.3K hours of egocentric video, LAPT-Scale-LAM provides implicit action supervision for policy pre-training, yielding consistent scaling gains and improving real-robot success from 63.3% to 85.0% as annotated human video scales from 1K to 5K hours. The learned policy also generalizes to unseen visual conditions.

</details>

---

### [[20_Research/Papers/强化学习/Variance-Reduced_Policy_Gradient_is_Nearly_Minimax-Optimal|Variance-Reduced Policy Gradient is Nearly Minimax-Optimal]]

![[assets/2610.13692_first_page.png|800]]

- **arXiv**: [2610.13692](https://arxiv.org/abs/2610.13692)
- **PDF**: https://arxiv.org/pdf/2610.13692
- **详细分析**: [[20_Research/Papers/强化学习/Variance-Reduced_Policy_Gradient_is_Nearly_Minimax-Optimal|Variance-Reduced Policy Gradient is Nearly Minimax-Optimal]]
- **作者**: Leonardo Cesani, Matteo Papini, Marcello Restelli
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Variance-Reduced Policy Gradient is Nearly Minimax-Optimal》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Standard Policy Gradient (PG) algorithms suffer from high estimation variance because they rely on Monte Carlo updates. While off-policy variance reduction mitigates this problem, establishing optimal sample complexity currently requires either restrictive assumptions, such as uniformly bounded importance weights, or impractical second-order operations. In this work, we introduce Loopless Variance-Reduced PG (LVR-PG), a unified theoretical framework that abstracts a class of first-order estimators that integrate recursive updates with defensive importance sampling, including known estimators such as PAGE-PG and STORM-PG. We prove that this algorithmic class achieves $\tilde{\mathcal{O}}(ε^{-2})$ last-iterate global convergence under weak gradient domination for general parametric policies. We establish this guarantee using purely first-order updates, with minimal assumptions and without gradient preconditioners. By extending state-of-the-art lower bounds to continuous parametric policies, we establish an $Ω(ε^{-2})$ sample complexity limit, confirming our framework is minimax-optimal up to logarithmic factors and horizon terms.

</details>

---

### [[20_Research/Papers/大模型/A_Multi-Agent_LLM_System_for_Automated_Tuning_of_Specialized_Neural_Network_Models|A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models]]

![[assets/2610.13663_figure.png|800]]

- **arXiv**: [2610.13663](https://arxiv.org/abs/2610.13663)
- **PDF**: https://arxiv.org/pdf/2610.13663
- **详细分析**: [[20_Research/Papers/大模型/A_Multi-Agent_LLM_System_for_Automated_Tuning_of_Specialized_Neural_Network_Models|A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models]]
- **作者**: Ivan Moloshnikov, Dmitry Kunitsyn, Alexander Sboev, Maksim Skorokhodov, Roman Rybka, Yuanchao Liu
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《A Multi-Agent LLM System for Automated Tuning of Specialized Neural Network Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MLE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many machine learning approaches are two-level: an expert selects a class of methods, within this class the choice of key components is critical and usually manual. This paper addresses the automatic tuning of these components and proposes a framework transferable across models of different nature. The multi-agent large language model (LLM) framework has three roles---analyst, coder, and recorder~---with an experiment log and a sandboxed execution environment. Unlike systems that optimize the entire ML script or search architectures in a discrete space, the framework operates over an open but semantically narrow space: the agent generates code only for the specified components, leaving the overall network structure unchanged. The approach is validated in two directions: tuning a classification spiking neural network with correlation learning, and solving high-order differential equations with Physics-Informed Neural Networks (PINN). Across five tasks---spiking classification on MNIST and Digits, and boundary-value problems for the generalized nonlinear Schrödinger equation (GNLSE) and Kuramoto--Sivashinsky (KS) equations---the agent outperforms the baselines: classification accuracy is 13 percentage points (MNIST) and 6 percentage points (Digits) higher; the error against the analytical single-soliton solution is reduced approximately 2491-fold; the invariant-preservation error drops approximately 325-fold in the selected GNLSE run with a Gaussian perturbation and by more than 100-fold on average over repeated initializations; and the mass drift drops 14-fold for the KS problem with a Gaussian perturbation. The framework thus tunes key components on tasks of different nature without changing its internal structure.

</details>

---

### [[20_Research/Papers/具身智能/MAGMA-Bench_Evaluating_Long-Horizon_Embodied_Agents_under_Dynamic_Tasks_and_Execution_Failures|MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures]]

![[assets/2610.13534_first_page.png|800]]

- **arXiv**: [2610.13534](https://arxiv.org/abs/2610.13534)
- **PDF**: https://arxiv.org/pdf/2610.13534
- **详细分析**: [[20_Research/Papers/具身智能/MAGMA-Bench_Evaluating_Long-Horizon_Embodied_Agents_under_Dynamic_Tasks_and_Execution_Failures|MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures]]
- **作者**: Loan Bernat, Matthieu Grard, Ariane Herbulot, Florent Lamiraux
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《MAGMA-Bench: Evaluating Long-Horizon Embodied Agents under Dynamic Tasks and Execution Failures》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MAGMA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon embodied agents must maintain task-relevant information, coordinate heterogeneous robots, and adapt their decisions as execution unfolds. Existing benchmarks investigate dynamic task execution and embodied multi-agent coordination, but provide limited evaluation of their intersection. We introduce MAGMA-Bench, an architecture-agnostic benchmark for persistent task reasoning in dynamic multi-robot environments. MAGMA-Bench evaluates agents across increasing task horizons and controlled online perturbations, including execution failures, task interruptions, and mission updates, with scenarios requiring coordination across robots with heterogeneous capabilities. It uses a structured skill-level interface to separate task-level reasoning from perception and low-level control. We evaluate locally deployable open-weight planners, multi-agent state-tracking strategies, and frontier models. Even the strongest evaluated models fail on a substantial fraction of clean episodes, and their success rates decrease further under online perturbations. Supervised adaptation greatly improves a small model, but performance remains substantially lower on longer and multi-robot missions. We release the benchmark, 261,646 task-level training examples, and an architecture-agnostic expert-trace generation pipeline.

</details>

---

### [[20_Research/Papers/具身智能/RESCUE_Is_This_Alarm_Worth_Acting_On_Counterfactual_Evaluation_of_VLA_Runtime_Monitors|RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors]]

![[assets/2610.13516_figure.png|800]]

- **arXiv**: [2610.13516](https://arxiv.org/abs/2610.13516)
- **PDF**: https://arxiv.org/pdf/2610.13516
- **详细分析**: [[20_Research/Papers/具身智能/RESCUE_Is_This_Alarm_Worth_Acting_On_Counterfactual_Evaluation_of_VLA_Runtime_Monitors|RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors]]
- **作者**: David Ahmedt-Aristizabal, Abdelwahed Khamis, Mohammad Ali Armin, Lars Petersson
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RESCUE: Is This Alarm Worth Acting On? Counterfactual Evaluation of VLA Runtime Monitors》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CheckVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Runtime failure monitors for robot policies are typically evaluated by how accurately they distinguish failed from successful executions. Yet an accurate alarm may arrive too late for recovery, while an unnecessary intervention may disrupt an execution that would otherwise succeed. We introduce RESCUE, a counterfactual framework for evaluating whether a monitor's alarms enable useful interventions. By restoring simulator and policy states at execution checkpoints, RESCUE compares alternative actions, identifies the latest checkpoint satisfying a specified recovery criterion, and evaluates whether acting on alarms reduces expected task-completion cost. We evaluate RESCUE with OpenVLA-OFT and $π_{0.5}$ over LIBERO-Spatial and LIBERO-Plus using 128,340 counterfactual branches. Recoverability depends on the state--intervention pair rather than on robot state alone: at $τ=0.5$, 14 of 66 OpenVLA-OFT/LIBERO-Plus failures contain a recoverable checkpoint under continuation, compared with 34 of 66 under continuation or scripted recovery, while recovery reduces recoverability in other conditions. On the primary strong-policy conditions, favourable detection scores do not establish lower intervention cost. Under the evaluated stop-and-reset model, even an idealised detector can afford only a 2.0--3.3% false-alarm rate before unnecessary resets outweigh the savings from stopping failures early. These results show that monitor value depends jointly on the intervention available and the workload in which it is deployed.

</details>

---

### [[20_Research/Papers/大模型/Retrieval-Augmented_Multimodal_Language_Model_with_Heterogeneous_Evidence_Integration_for_Clinical_Prognosis|Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis]]

![[assets/2610.13510_figure.png|800]]

- **arXiv**: [2610.13510](https://arxiv.org/abs/2610.13510)
- **PDF**: https://arxiv.org/pdf/2610.13510
- **详细分析**: [[20_Research/Papers/大模型/Retrieval-Augmented_Multimodal_Language_Model_with_Heterogeneous_Evidence_Integration_for_Clinical_Prognosis|Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis]]
- **作者**: Hamza Shafiq, Jialu Tang, Ting Dang, Jun Hu, Aaqib Saeed
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Retrieval-Augmented Multimodal Language Model with Heterogeneous Evidence Integration for Clinical Prognosis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clinical prognosis requires integrating structured measurements, physiological waveforms, longitudinal history, and population context. We introduce PRISM (Population-Retrieved Inference for Structured Multimodal Prognosis), a multimodal language model that combines per-feature numerical tokenization, recency-weighted aggregation of longitudinal ECGs, and a dual-modality population memory bank. Retrieval operates in representation space: the model receives mean-pooled embeddings of similar training-cohort encounters, while no individual retrieved record enters the prompt. On the 1,443-task MDS-ED benchmark, PRISM achieves AUROCs of 86.2% for diagnosis, 93.1% for deterioration, 91.8% for ICU admission, and 92.8% for mortality. These results use a 96-hour pre-arrival window unavailable to reported baselines. With benchmark-window inputs only, PRISM reaches 0.8895 AUROC, compared with 0.8937 for UniPACT and 0.8889 for MDS-ED. A matched-input compact fusion model using the same five evidence streams and frozen encoders reaches 0.7652 AUROC, versus 0.9092 for PRISM. Replacing numerical EHR encoding with text serialization reduces AUROC by 3.66 points; removing pre-arrival history reduces it by 1.97 points; and zeroing retrieval reduces it by 0.99 points. Genuine retrieval outperforms random-neighbor retrieval by 0.97 macro-average points, although a paired task-level sign test does not establish a uniform advantage (p=0.067). On the external MC-MED cohort, supervised fine-tuning reaches 0.8611 AUROC, compared with 0.8227 for locally trained gradient boosting and 0.7841 for source-only PRISM. These results support structure-aware multimodal integration and supervised external adaptation.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Temporal_Proximity_Explanatory_World_Models_for_Credit_Assignment_in_Reinforcement_Learning|Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning]]

![[assets/2610.13504_figure.png|800]]

- **arXiv**: [2610.13504](https://arxiv.org/abs/2610.13504)
- **PDF**: https://arxiv.org/pdf/2610.13504
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Temporal_Proximity_Explanatory_World_Models_for_Credit_Assignment_in_Reinforcement_Learning|Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning]]
- **作者**: Oriol Corcoll, Qiyao Wei, Ciarán Mark Gilligan-Lee
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 0.96，世界模型 0.96）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Beyond Temporal Proximity: Explanatory World Models for Credit Assignment in Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative Recommenders increasingly use Reinforcement Learning (RL) to optimize outcomes that may appear hundreds or thousands of interactions after a decision. Standard RL propagates reward according to temporal proximity rather than explicit relevance, attenuating the signal assigned to distant but important actions and creating a source of sample inefficiency. We introduce Explanatory World Models (EWM), an attribution framework that uses explanations to identify the earlier events that plausibly contributed to a realized outcome. We instantiate EWM with a frontier language model and use its explanations as learning signals using a conservative hierarchical operator that recursively redistributes reward while preserving the undiscounted episode return. To investigate what constitutes a useful explanation, we operationalize three complementary variants inspired by Halpern's actual causation, Lombrozo's explanatory simplicity, and Deutsch's hard-to-vary explanations. We evaluate EWM on two controlled long-horizon RL benchmarks, a public sequential-recommendation benchmark, and an industry-scale generative recommender. On Crafter and WordCraft, EWM substantially outperforms PPO and LaRe, with its largest gains when rewards are most delayed. On KuaiRand, EWM outperforms SFT and LaRe offline and A2C online. Finally, in an offline evaluation of an industry generative recommender, EWM considerably improves Recall and increases behavioral proxies. These results suggest that explanations can provide structured and reusable credit for learning from delayed outcomes.

</details>

---

### [[20_Research/Papers/大模型/Humanize_MLE_Agents_Multi-Agent_Session_Alternation_Beyond_Single-Agent_Limits|Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits]]

![[assets/2610.13494_figure.png|800]]

- **arXiv**: [2610.13494](https://arxiv.org/abs/2610.13494)
- **PDF**: https://arxiv.org/pdf/2610.13494
- **详细分析**: [[20_Research/Papers/大模型/Humanize_MLE_Agents_Multi-Agent_Session_Alternation_Beyond_Single-Agent_Limits|Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits]]
- **作者**: Changye Li, Zijian Zhang, Muheng Li, Yiduo Pang, Tingjun Wu, Menghan Li, Yitong Liu, Hongkai Guo, Mengchi Chen, Chenyu He, Kaisheng Ma, Wei Xu...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Humanize MLE Agents: Multi-Agent Session Alternation Beyond Single-Agent Limits》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing LLM-based agent approaches for long-horizon machine learning engineering (MLE) often use context engineering, implemented through custom harnesses that manage tools, skills, and accumulated experience. However, we find that as single-session execution lengthens, the agent's reasoning intensity declines alongside slowing progress, summarized as long-horizon deceleration, and the benefits of these custom harnesses vanish as the underlying model improves, summarized as harness staleness. These findings suggest that their benefits may not persist across versions, which motivates a workflow-level approach in which agents build on one another's work across sessions. We model these alternating agent sessions as a context-reset semi-Markov decision process (CR-SMDP) and establish sufficient conditions for alternation to exceed single-agent reference limits, derive an explicit experiment-budget bound, and characterize when session caps preserve this advantage. Guided by this analysis, we introduce Humanize MLE Agents (HMA), which alternates two agents on a shared workspace, limits each session to at most k experiments and resets the context between sessions, without additional task-specific harness or prior knowledge supplements. Across 75 Kaggle tasks in MLE-bench, HMA reaches a state-of-the-art any-medal rate of 78.2%, exceeding the strongest open-source baseline by 8.0 points with a quarter of its time budget. Moreover, among six configurations spanning five heterogeneous agent pairs, HMA improves any-medal rate over the constituent baselines by 6.4 points on average, demonstrating cross-pair generality. A supplementary case on kernel optimization reaches 878 cycles, within 1.6% of the community leaderboard leader, demonstrating applicability beyond MLE.

</details>

---

### [[20_Research/Papers/大模型/Rollout-Time_Intervention_Unlocking_Agentic_Reinforcement_Learning_Beyond_Policy_Limits|Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits]]

![[assets/2610.13438_figure.png|800]]

- **arXiv**: [2610.13438](https://arxiv.org/abs/2610.13438)
- **PDF**: https://arxiv.org/pdf/2610.13438
- **详细分析**: [[20_Research/Papers/大模型/Rollout-Time_Intervention_Unlocking_Agentic_Reinforcement_Learning_Beyond_Policy_Limits|Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits]]
- **作者**: Chen Xi, Ding Ruixue, Wang Zhigaoyuan, Zhang Fanrui, Zhang Qiang, Chen Boli, Wang Shihang, Wang Tianfu, Ren Ailin, Wang Pengyong, Xie Pengjun, Xiong Hui
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Rollout-Time Intervention: Unlocking Agentic Reinforcement Learning Beyond Policy Limits》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Claw-Eval, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has emerged as a key paradigm for improving large language model (LLM) agents, enabling stronger reasoning, planning, and tool-use in interactive environments. However, existing agent RL methods remain fundamentally constrained by an on-policy reasoning bottleneck: when tasks exceed the model's current capability boundary, effective trajectories become extremely sparse and training often collapses. We introduce Rollout-Time Intervention (RTI), a technique designed to elicit successful trajectories beyond the policy's intrinsic exploration capacity. RTI operates by leveraging reward-side evidence (i.e., evaluation rubrics) during rollout to convert erroneous trajectories into successful ones, providing effective learning signals for tasks that the policy rarely solves on its own. Although intervention trajectories are inherently off-policy, we find that they can effectively guide policy optimization when trajectories with excessive distributional shifts are filtered out. Extensive experiments across five benchmarks demonstrate that RTI consistently outperforms RL baselines, enabling the post-trained policy to approach the performance of substantially stronger contemporary LLMs and, more importantly, transcend its original capability boundary. The code is available at https://github.com/Alibaba-NLP/qqr.

</details>

---

### [[20_Research/Papers/具身智能/AlphaNIST_Emergent_Assembly_Skills_from_Binary_Task_Rewards|AlphaNIST: Emergent Assembly Skills from Binary Task Rewards]]

![[assets/2610.13354_figure.png|800]]

- **arXiv**: [2610.13354](https://arxiv.org/abs/2610.13354)
- **PDF**: https://arxiv.org/pdf/2610.13354
- **详细分析**: [[20_Research/Papers/具身智能/AlphaNIST_Emergent_Assembly_Skills_from_Binary_Task_Rewards|AlphaNIST: Emergent Assembly Skills from Binary Task Rewards]]
- **作者**: Octi Zhang, Iretiayo Akinola, Rosario Scalise, Mateo Guaman Castro, Patrick Yin, Tobias Widmer, Miles Macklin, Chris Amevor, Dylan Turpin, Dirk Van Gelder, Jan Carius, Ankur Handa...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《AlphaNIST: Emergent Assembly Skills from Binary Task Rewards》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The NIST Assembly Task Board #1 remains a challenging benchmark for learning-based methods in robotic manipulation. Over short horizons, it demands precise, contact-rich control of small, tight-fitting parts. Over long horizons, it requires recovery and coordination across extended action sequences. Demonstrations, task decomposition, and dense progress rewards have enabled research advances by providing guidance on how to assemble. But how much of the strategy must be specified? The progression from AlphaGo to AlphaGo Zero showed that RL at scale can discover superhuman strategies without prescribing how to win. AlphaNIST asks whether a sparse binary task reward and task diversity admitted by this task-agnostic reward can similarly let a robot discover how to assemble. In simulation, we train a single policy from scratch across all 20 assembly tasks on the NIST Assembly Task Board #1, reaching 98.2% overall training success without demonstrations, progress shaping, scripted primitives, or per-task tuning. The framework also trains policies to complete ten assembly pairs in a single episode without a prescribed order, with task success rewarded only when all ten pairs are simultaneously complete. The learned policies discover dexterous and planning-like behaviors: choosing grasps for later assembly, using surrounding geometry to reorient parts, and preparing one part, assembling another, then returning to finish the first without an explicit planner. For videos, see our website: https://alpha-nist.github.io/

</details>

---

### [[20_Research/Papers/大模型/Forgetting_is_Not_Always_Bad_A_Neuro-Inspired_Memory_Repair_Mechanism_for_Poisoned_LLM_Agents|Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents]]

![[assets/2610.13267_figure.png|800]]

- **arXiv**: [2610.13267](https://arxiv.org/abs/2610.13267)
- **PDF**: https://arxiv.org/pdf/2610.13267
- **详细分析**: [[20_Research/Papers/大模型/Forgetting_is_Not_Always_Bad_A_Neuro-Inspired_Memory_Repair_Mechanism_for_Poisoned_LLM_Agents|Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents]]
- **作者**: Lei Liu, Yunji Liang, Xiaowen Zhang, Jingqi Liu, Qi Li, Bin Guo, Zhiwen Yu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Forgetting is Not Always Bad: A Neuro-Inspired Memory Repair Mechanism for Poisoned LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ReAct-StrategyQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are highly vulnerable to memory-poisoning attacks. Existing defenses primarily rely on external modules for either static memory isolation or continuous online auditing, resulting in low memory efficiency and high computational overhead. To address these limitations, inspired by neuroscientific mechanisms that weak reactivation can destabilize memories and induce decay in the absence of reinforcement, we propose an agent-intrinsic training-free memory repair framework, DREAM (Dynamic Reactivation for Engram Attenuation in Memory), that enables selective functional forgetting of poisoned memories. Specifically, DREAM implements a three-stage pipeline: perturbation-induced implicit reactivation to reveal the structural fragility of malicious memories, adaptive anomaly diagnosis based on multi-dimensional activation patterns to detect topological anomalies, and a dynamic memory repair module that selectively suppresses harmful memories while reinforcing benign ones. Extensive experiments across diverse attackers and real-world tasks demonstrate that DREAM reduces attack success rates by over 95\% against backdoor poisoning while preserving strong benign utility. DREAM also achieves competitive robustness against injection attacks. In terms of runtime and token consumption, DREAM achieves up to a 2.13$\times$ speedup and a 37.7\% reduction in token consumption compared with A-MemGuard. Furthermore, DREAM also achieves a task success rate of 92.96\% on poisoned multi-agent systems.

</details>

---

### [[20_Research/Papers/具身智能/Beyond_Actions_Learning_Future_Operation_Targets_for_Vision-Language-Action_Models|Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models]]

![[assets/2610.13212_figure.png|800]]

- **arXiv**: [2610.13212](https://arxiv.org/abs/2610.13212)
- **PDF**: https://arxiv.org/pdf/2610.13212
- **详细分析**: [[20_Research/Papers/具身智能/Beyond_Actions_Learning_Future_Operation_Targets_for_Vision-Language-Action_Models|Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models]]
- **作者**: Min Lin, Bokai Zhou, Jianqi Lin, Kaiyuan Yang, Yicheng Chang, Junjie Yu, Xiaofan Liu, Jianhua Han, Rui Li, Shen Zhao, Xiaodan Liang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Beyond Actions: Learning Future Operation Targets for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FutureVLA, OpenVLA, UniVLA, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actions specify what a robot should execute, but do not describe what those commands will achieve. Vision-language-action (VLA) policies nevertheless learn primarily by predicting action chunks from images, language, and state. We introduce Action--Future Coupled Effect Learning (AFCE), which makes a future-grounded physical Effect the policy's primary prediction target. An offline tokenizer constructs temporally ordered Effect tokens from demonstrated actions, realized robot responses, and sparse visual transitions. Reconstruction objectives encourage the representation to retain executable detail and observed physical change. A flow-matching VLA predicts Effects from current images, instruction, and robot state, while a state-conditioned decoder converts them into action chunks. Embodiment-specific interfaces allow single- and dual-arm tasks to share the Effect model. On DexJoCo, AFCE achieves $50.97\%$ overall success, improving over $π_{0.5}$ and UVT by 11.82 and 15.21 percentage points, respectively. It leads on all five bimanual tasks, highlighting the value of Effect supervision for coordinated dexterous manipulation. The project page is available at https://afceproject.github.io/AFCE-Web/.

</details>

---

### [[20_Research/Papers/世界模型/JANUS_Enhancing_Long-Horizon_Autonomous_Research_with_Co-Evolving_World_Models|JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models]]

![[assets/2610.13194_figure.png|800]]

- **arXiv**: [2610.13194](https://arxiv.org/abs/2610.13194)
- **PDF**: https://arxiv.org/pdf/2610.13194
- **详细分析**: [[20_Research/Papers/世界模型/JANUS_Enhancing_Long-Horizon_Autonomous_Research_with_Co-Evolving_World_Models|JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models]]
- **作者**: Mengdi Liu, Chenghao Jia, Hong Chang, Mingjie He, Shiguang Shan, Xilin Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《JANUS: Enhancing Long-Horizon Autonomous Research with Co-Evolving World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MLS-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon autonomous research has shown promise in accelerating scientific progress through sustained cycles of hypothesis generation, implementation, and validation. However, this Generate-Execute-Feedback paradigm relies on reactive trial-and-error, where costly and time-consuming executions introduce severe feedback delays, throttling evolutionary progress under explosively expanding search space. To address this challenge, we propose JANUS, a framework that unifies future outcomes forecasting and past experience reflection through a Predict-Verify-Evolve loop driven by a co-evolving world model. Within an evolving graph, the research agent proposes candidates while world model scores them by forecasting value improvement, information gain, and exploration utility, then accordingly selects, refines, or prunes branches prior to execution. After receiving ground-truth feedback, JANUS distills experience into evolving skills: hierarchical skills for research agent, exploration-strategy skills for world model, and their coordination protocols. This mechanism enables continual co-evolution: the research agent sharpens candidate generation while the world model refines its predictive judgment over extended horizons. Extensive evaluations on MLS-Bench-Lite and real research tasks demonstrate that JANUS significantly outperforms state-of-the-art baselines, achieving both higher evolving efficiency and ceiling.

</details>

---

### [[20_Research/Papers/大模型/Locate,_Judge,_Read_Role-Specialized_Tool_Agents_over_a_Knowledge-Point_Index_for_Open-Domain_Multimodal_Document_QA|Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA]]

![[assets/2610.13128_first_page.png|800]]

- **arXiv**: [2610.13128](https://arxiv.org/abs/2610.13128)
- **PDF**: https://arxiv.org/pdf/2610.13128
- **详细分析**: [[20_Research/Papers/大模型/Locate,_Judge,_Read_Role-Specialized_Tool_Agents_over_a_Knowledge-Point_Index_for_Open-Domain_Multimodal_Document_QA|Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA]]
- **作者**: Wenlin Lin, Fanzhe Wei
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《Locate, Judge, Read: Role-Specialized Tool Agents over a Knowledge-Point Index for Open-Domain Multimodal Document QA》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：M3DocVQA, MMLongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Question answering over large heterogeneous document collections requires first finding the right passages and then reading them, yet current retrieval-augmented agents give one model both kinds of tools and let it schedule itself. We present KnowForge, a pipeline separated by job: a hybrid-retrieval knowledge-point index; a Locator agent that can only search; a code-scheduled bridge judge that forces the missing second hop; a typed, size-bounded evidence pool that merges every search's ranking; a Deep Reader agent that can only read text, images and tables; and a synthesizer with a format checker. With a self-hosted Qwen3.6-35B-A3B (3B active), KnowForge reaches F1 47.5 on the full open-domain M3DocVQA (2,441 questions, 3,368 PDFs), +11.0 over the published M3DocRAG system and +7.1 over one-shot retrieve-and-answer on the same index and model, and 53.5 with DeepSeek-V4-Flash. On MultiHop-RAG it reaches 73.5 accuracy, above the strongest published RAG and GraphRAG results (71.2); on the single-document MMLongBench-Doc it lifts the same model from 34.8 to 47.0, level with GPT-4o reading page images (46.3). Per-job ablations on the full benchmarks attribute the gain: the Deep Reader is worth 3.8, 9.8 and 0 points on the three corpora, tracking how visual each is; merging both agents into one with all tools and twice the rounds loses 1.9 F1 because it keeps searching instead of reading; a round-budget sweep shows a step at four Locator rounds and a plateau beyond; query latency scales with model calls rather than corpus size. We serve the three indexed benchmarks as read-only knowledge bases (free registration) and release all prompts and the runner code: https://github.com/metask-ai/knowforge-bench

</details>

---

### [[20_Research/Papers/具身智能/When_Faster_Decisions_Do_Not_Make_Better_Agents_An_Empirical_Study_of_Jev_in_Agent_Workflows|When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows]]

![[assets/2610.13092_figure.png|800]]

- **arXiv**: [2610.13092](https://arxiv.org/abs/2610.13092)
- **PDF**: https://arxiv.org/pdf/2610.13092
- **详细分析**: [[20_Research/Papers/具身智能/When_Faster_Decisions_Do_Not_Make_Better_Agents_An_Empirical_Study_of_Jev_in_Agent_Workflows|When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows]]
- **作者**: Yuchen Ling, Shengcheng Yu, Zhenyu Chen, Chunrong Fang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.8）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《When Faster Decisions Do Not Make Better Agents: An Empirical Study of Jev in Agent Workflows》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, AndroidWorld, S1-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents depend on repeated decisions to accomplish tasks, with large language models (LLMs) commonly serving as their core decision makers. The recent emergence of Jev offers an opportunity to make these decisions faster and at lower cost. However, it remains unclear whether such local savings can be translated into efficient and reliable task completion. In this paper, we investigate this efficiency transfer across five agents in two representative application settings, embodied tasks in ALFWorld and mobile app use in AndroidWorld. Across 4,500 task executions, we jointly evaluate task effectiveness, decision-level and task-level resource use, and execution behavior. Experimental results show that Jev integration substantially reduces decision cost and latency across all five agents, with task-level gains varying by workflow. Task success remains close to baseline levels on ALFWorld and declines more substantially in two mobile agents. Auxiliary reasoning and additional interactions absorb decision savings, while failed recovery and premature completion limit successful delivery. Mean cost per successful outcome increases in one agent even as spending per attempt falls. These findings highlight the importance of preserving progress, supporting recovery, and verifying completion when integrating efficient decision models into agent workflows. Their practical value should be assessed through successful task delivery, recovery behavior, and resources per delivered outcome.

</details>

---

### [[20_Research/Papers/大模型/Travel_Back_To_Move_Forward_Retrospective_Exploration_and_Evolving_for_Long_Horizon_Agents|Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents]]

![[assets/2610.13058_figure.png|800]]

- **arXiv**: [2610.13058](https://arxiv.org/abs/2610.13058)
- **PDF**: https://arxiv.org/pdf/2610.13058
- **详细分析**: [[20_Research/Papers/大模型/Travel_Back_To_Move_Forward_Retrospective_Exploration_and_Evolving_for_Long_Horizon_Agents|Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents]]
- **作者**: Ziang Ye, Wentao Shi, Lei Chen, Zhengzhou Cai, Yu Wang, Zhiyuan Yao, Zihan Wang, Xierui Song, Fuli Feng, Yixin Cao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Travel Back To Move Forward: Retrospective Exploration and Evolving for Long Horizon Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents increasingly operate in long-horizon environments where early mistakes can trigger cascading failures and trap agents in dead-end trajectories. Agents must therefore be able to proactively recover from such states and turn their exploratory experience into guidance for subsequent decisions. We introduce ReTRAIL, a framework that enables agents to rewind the environment to earlier states while preserving valid progress and carrying forward knowledge learned from abandoned exploration. The environment state moves backward while the agent's knowledge continues to move forward. ReTRAIL trains a shared policy with two complementary signals: State-Anchored GRPO compares alternative continuations from revisited states to improve execution, while a branch-advancement reward guides reflection through the progress of subsequent exploration. Experiments across four interactive benchmark MineSweeper, Sokoban, ALFWorld and ScienceWorld show that simply adding a rewind primitive provides limited benefit and can even degrade performance. In contrast, ReTRAIL enables agents to rewind from unproductive states and use insights from abandoned branches to guide subsequent exploration. These results demonstrate the value of coupling environment rewinding with experience reuse within an ongoing task for long-horizon task solving. The code is available at https://github.com/whi497/ReTRAIL.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedCLBench_Evaluating_Continual_Learning_for_Self-Evolving_Embodied_Agents|EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents]]

![[assets/2610.13021_figure.png|800]]

- **arXiv**: [2610.13021](https://arxiv.org/abs/2610.13021)
- **PDF**: https://arxiv.org/pdf/2610.13021
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedCLBench_Evaluating_Continual_Learning_for_Self-Evolving_Embodied_Agents|EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents]]
- **作者**: Jie Huang, Yanan Chen, Ruixun Liu, Kaichen He, Xinyi He, Rui Huang, Zilong Zheng, Zhenliang Zhang, Yiwu Zhong
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.85（加权：具身智能 1.2，大模型 0.65）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《EmbodiedCLBench: Evaluating Continual Learning for Self-Evolving Embodied Agents》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EmbodiedCLBench, TongSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual learning requires models to accumulate past experience and transfer it to new tasks. Despite substantial research on continual learning, existing work remains largely confined to non-embodied settings, without extending to embodied environments. To address this gap, we introduce EmbodiedCLBench, the first benchmark in embodied simulation for evaluating the continual learning capability of self-evolving agents. With compositional generalization as the core evaluation principle, our benchmark evaluates whether agents can first learn from basic tasks and then recombine the acquired skills to solve complex, unseen advanced tasks. Based on EmbodiedCLBench, we conduct extensive experiments across multiple agent harnesses and learning methods, revealing consistent limitations and distinctive behaviors. Our results show that while advanced tasks can be hardly solved under zero-shot setting, the experience from basic tasks enables consistent improvement. Such benefit from the experience remains stable even if the task complexity increases. However, this improvement does not scale accordingly with the number of learning samples, and current agents cannot extract meaningful information from additional experience. Collectively, our findings highlight continual learning as a fundamental yet underexplored capability, and our benchmark offers valuable resources for designing effective self-evolving agents in embodied environments. Our code and dataset are available at https://pku-value-lab.github.io/EmbodiedCLBench-homepage.

</details>

---

### [[20_Research/Papers/大模型/Generalized_Proximal_Policy_Optimization_Unifying_LLM_RL_Algorithms_from_the_Perspective_of_Divergence|Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence]]

![[assets/2610.13015_figure.png|800]]

- **arXiv**: [2610.13015](https://arxiv.org/abs/2610.13015)
- **PDF**: https://arxiv.org/pdf/2610.13015
- **详细分析**: [[20_Research/Papers/大模型/Generalized_Proximal_Policy_Optimization_Unifying_LLM_RL_Algorithms_from_the_Perspective_of_Divergence|Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence]]
- **作者**: Zhicheng Cai, Xinyuan Guo, Hanlin Wu, Weinan Dai, Yuyan Zhou, Wei-Ying Ma, Ya-Qin Zhang, Hao Zhou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has become the foundational paradigm for enhancing the reasoning capabilities of LLMs. Yet the dominant approach, Proximal Policy Optimization (PPO), relies on a geometrically degenerate clipping proxy that cannot adapt its resistance to policy shifts, leading to premature clipping and degraded exploration. Subsequent variants alleviate these issues through fragmented and heuristic modifications. We propose Generalized Proximal Policy Optimization (GPPO), a principled and unified framework for understanding and designing LLM RL algorithms through the lens of divergence. We establish a generalized $f$-divergence trust-region theory with a monotonic performance improvement guarantee, and show that different $f$-divergences induce distinct geometries and policy update dynamics. We further introduce novel estimator topologies that provide more faithful divergence estimates than the conventional single-sample Monte Carlo estimation. Under this framework, PPO and recent variants such as DAPO, DPPO, and RIPO emerge as special cases, establishing a principled two-dimensional design space of {Divergence $\times$ Estimator}. Extensive experiments on eight competition-level math and coding benchmarks show that both dimensions are critical. The best-performing GPPO instantiation surpasses standard GRPO by up to 50% and 14% on math and coding, delivering SOTA performance.

</details>

---

### [[20_Research/Papers/大模型/SmartSalesBench_A_Resistance-Aware_Multi-Turn_Benchmark_for_Evaluating_LLM_Sales_Agents|SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents]]

![[assets/2610.12975_figure.png|800]]

- **arXiv**: [2610.12975](https://arxiv.org/abs/2610.12975)
- **PDF**: https://arxiv.org/pdf/2610.12975
- **详细分析**: [[20_Research/Papers/大模型/SmartSalesBench_A_Resistance-Aware_Multi-Turn_Benchmark_for_Evaluating_LLM_Sales_Agents|SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents]]
- **作者**: P N Bhargav Teja, Velpula Lokesh Reddy, Madhu Basumata, Susen Sarkar, Rajasekhara Reddy Duvvuru Muni
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.45（加权：大模型 1.45）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SmartSalesBench: A Resistance-Aware Multi-Turn Benchmark for Evaluating LLM Sales Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CharacterEval, PersonaGym, RetailBench, RetailSim, SmartSalesBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present SmartSalesBench, the first multi-turn conversational benchmark explicitly designed to evaluate large language model (LLM) sales agents against psychologically grounded, resistant buyer personas. Existing task-oriented dialogue benchmarks assume cooperative users and measure task completion; SmartSalesBench inverts this assumption, placing agents against personas programmed to resist and challenge across conversations of up to twenty turns. The benchmark includes five agent profiles, twelve buyer personas, fifteen smartphone products across six price tiers, and four controlled experiments with 3 iterations totaling 13,680 sessions. Both sales-agent and buyer persona generations are grounded through retrieval-augmented generation (RAG). We introduce nine evaluation metrics grouped into three tiers: primary outcome metrics (CR, BRS, RIR), secondary quality metrics (SMS, PFS, ETI), and exploratory metrics planned for future reporting (ITS, ARI, SPI). Our evaluation combines automated LLM-as-judge scoring with internal human assessment (n = 50, \k{appa} = 0.71, Pearson r = 0.81 with BRS).

</details>

---

### [[20_Research/Papers/具身智能/JoyInside-VLM-Agent_Product-Conditioned_Multimodal_Policy_Learning_for_Embodied_Agents|JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents]]

![[assets/2610.12957_figure.png|800]]

- **arXiv**: [2610.12957](https://arxiv.org/abs/2610.12957)
- **PDF**: https://arxiv.org/pdf/2610.12957
- **详细分析**: [[20_Research/Papers/具身智能/JoyInside-VLM-Agent_Product-Conditioned_Multimodal_Policy_Learning_for_Embodied_Agents|JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents]]
- **作者**: Gangyi Li, LuYao Wang, Jingfu Sun, Jingyi Yuan, Hang Liu, Hao Zong, Yujia Hu, Tingting Gao, Jianyong Wang, Xu Yang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.82（加权：具身智能 1.8，大模型 1.6，强化学习 0.36，世界模型 0.16，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《JoyInside-VLM-Agent: Product-Conditioned Multimodal Policy Learning for Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, WildToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents must translate multimodal observations and user requests into executable actions while adapting to product constraints, changing goals, and execution feedback. We present JoyInside-VLM-Agent, a ReAct-style multimodal agent developed through product-conditioned trajectory construction and staged policy learning for robotic platforms and smart hardware. A closed-loop sandbox generates multimodal interaction trajectories covering goal revisions and failure recovery, which are checked against execution outcomes and semantic criteria. Supervised fine-tuning and multi-teacher on-policy distillation precede reinforcement learning with DPER (Dual-Source Privileged On-Policy Self-Distillation with Token-Level Evidence Routing). DPER routes token-level evidence between a frozen privileged teacher and a privileged student sharing the rollout policy's parameters, modulating reward-derived token advantages while preserving their signs. Training rewards combine generative process evaluation, multi-judge rankings, and task-queue consistency. JoyInside-VLM-Agent achieves a BFCL v4 overall score of 77.44, exceeding the evaluated baselines; results on the other public benchmarks are mixed. On JoyInside-Devices and JoyInside-Robotics, the evaluated system, which includes domain-specific skill refinement, leads the baselines on all reported metrics. Two real-world quadruped case studies illustrate visually grounded search, replanning after execution failure, and explicit failure reporting.

</details>

---

### [[20_Research/Papers/具身智能/OGPO_Offline_Goal-conditioned_Policy_Optimization_for_Recoverable_Vision-Language-Action_Models|OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models]]

![[assets/2610.12914_figure.png|800]]

- **arXiv**: [2610.12914](https://arxiv.org/abs/2610.12914)
- **PDF**: https://arxiv.org/pdf/2610.12914
- **详细分析**: [[20_Research/Papers/具身智能/OGPO_Offline_Goal-conditioned_Policy_Optimization_for_Recoverable_Vision-Language-Action_Models|OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models]]
- **作者**: Xule Gao, Xi Wang, Zehua Zang, Rui Wang, Changwen Zheng, Chuxiong Sun
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.0（加权：具身智能 1.8，强化学习 0.8，机器人 0.4）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《OGPO: Offline Goal-conditioned Policy Optimization for Recoverable Vision-Language-Action Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MetaWorld, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have shown strong promise in robotic manipulation, yet their post-training still predominantly relies on trajectory-level supervised imitation over robot demonstrations. While effective for learning feasible actions, this paradigm supervises policies to reproduce expert actions at each step, biasing them toward demonstration-specific action paths and providing limited guidance for recovering toward task-progress states once execution deviates from demonstrated trajectories. To address this limitation, we propose OGPO, an Offline Goal-conditioned Policy Optimization framework for recoverable VLA post-training. Instead of treating offline demonstrations merely as step-wise action labels, OGPO adaptively relabels trajectories with semantic key states and constructs goal-conditioned process rewards to optimize the policy for reaching these task-progress states. In this way, OGPO shifts VLA post-training from trajectory-level action imitation to key-state reachability learning, enabling policies to acquire a more robust ability to complete goal states from feasible off-demonstration states without requiring additional online interaction. Experiments on LIBERO and MetaWorld show that OGPO consistently improves VLA policy performance over standard supervised fine-tuning. Moreover, evaluations on LIBERO-Plus and our proposed LIBERO-ReAct, a mid-execution perturbation benchmark, further demonstrate that OGPO achieves stronger robustness and goal-directed recoverability under distribution shifts and recoverable off-demonstration states.

</details>

---

### [[20_Research/Papers/大模型/VEPA_Verified_Evolving_Formal_Policy_for_Lifelong_LLM_Agent_Guardrails|VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails]]

![[assets/2610.12813_figure.png|800]]

- **arXiv**: [2610.12813](https://arxiv.org/abs/2610.12813)
- **PDF**: https://arxiv.org/pdf/2610.12813
- **详细分析**: [[20_Research/Papers/大模型/VEPA_Verified_Evolving_Formal_Policy_for_Lifelong_LLM_Agent_Guardrails|VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails]]
- **作者**: Duy Nguyen, Lesly Miculicich, Bhavana Dalvi Mishra, Shuo Li, Krishnamurthy Dj Dvijotham, Mohit Bansal, Tomas Pfister, Long T. Le
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《VEPA: Verified Evolving Formal Policy for Lifelong LLM Agent Guardrails》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ASSEBench, ATBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly operate over sensitive resources, such as private documents and mutable system states, which can create serious safety and security risks. Runtime guardrails should therefore make inspectable, reproducible, and deterministic allow or refuse decisions before potentially irreversible agent actions are executed. However, safety and security requirements are rarely complete before deployment, so guardrails need to keep adapting as new risks emerge. Existing adaptive guardrails learn from deployment experience, but they usually apply safety policies through LLM inference, which can lead to inconsistent decisions and ambiguous policy interpretations. Formal guardrails, on the other hand, enforce policies deterministically, but they usually rely on pre-deployment or task-specific policies and have no mechanism to adapt to newly observed risks. We introduce VEPA, a framework for the verified evolution of formal agent guardrails. VEPA represents the guardrail as a formal policy of executable symbolic rules over typed agent events. During deployment, we use an LLM guided by deployment feedback to propose policy patches that fix newly observed failures while preserving previously correct behavior. Then, a deterministic verifier only accepts policies that are structurally valid and conflict-free. Finally, an evidence-aware authority layer activates a verified rule only when it has enough supporting evidence, so uncertain updates cannot directly affect guardrail decisions. Across ASSEBench-Safety, ASSEBench-Security, and ATBench, VEPA consistently outperforms baselines while expanding the scope of deterministic formal-policy enforcement. These gains also hold under more challenging deployment conditions, including mixed streams, corrupted feedback, and longer horizons.

</details>

---

### [[20_Research/Papers/大模型/Efficient_Audio-Visual_Speech_Enhancement_via_Reinforcement_Learning-Based_Neural_Architecture_Search|Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search]]

![[assets/2610.12796_first_page.png|800]]

- **arXiv**: [2610.12796](https://arxiv.org/abs/2610.12796)
- **PDF**: https://arxiv.org/pdf/2610.12796
- **详细分析**: [[20_Research/Papers/大模型/Efficient_Audio-Visual_Speech_Enhancement_via_Reinforcement_Learning-Based_Neural_Architecture_Search|Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search]]
- **作者**: Khubaib Ahmed, Ahsan Adeel, Nasir Saleem, Kia Dashtipour, Ahsan Ulhaq, Amir Hussain
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Efficient Audio-Visual Speech Enhancement via Reinforcement Learning-Based Neural Architecture Search》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Conv-TasNet, LipNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Audio-visual speech enhancement (AVSE) improves speech intelligibility in noisy environments but often relies on computationally expensive models unsuitable for resource-constrained edge devices. This paper introduces a reinforcement learning-driven neural architecture search (RL-NAS) framework to discover compact, efficient AVSE architectures. The search space preserves temporal alignment between audio and visual streams, while a novel reward function jointly optimises speech enhancement performance, measured by SI-SNR improvement, and model compactness. Using proximal policy optimisation with constraint-aware action masking, the framework evaluates only 35 candidate architectures and identifies a model with 2.9 million parameters, compared with 22 million in the baseline. The proposed architecture achieves a 14.5 dB SI-SNR improvement, only 0.7 dB below the baseline, while reducing model size by approximately nine-fold. Evaluation on commercial mobile CPUs demonstrates a 4.3-fold reduction in real-time factor, supporting practical on-device deployment. Compared with random search, RL-NAS achieves 92% higher search efficiency. Architectural analysis reveals that shallower but wider temporal convolutional blocks and aggressive visual pathway pruning can maintain enhancement performance while substantially reducing computational requirements. These findings demonstrate the potential of reinforcement learning-guided architecture search for developing lightweight, efficient and deployable multimodal speech enhancement systems.

</details>

---

### [[20_Research/Papers/大模型/EvoBelief_Falsifiable_World_Models_for_Self-Improving_LLM_Agents|EvoBelief: Falsifiable World Models for Self-Improving LLM Agents]]

![[assets/2610.12789_figure.png|800]]

- **arXiv**: [2610.12789](https://arxiv.org/abs/2610.12789)
- **PDF**: https://arxiv.org/pdf/2610.12789
- **详细分析**: [[20_Research/Papers/大模型/EvoBelief_Falsifiable_World_Models_for_Self-Improving_LLM_Agents|EvoBelief: Falsifiable World Models for Self-Improving LLM Agents]]
- **作者**: Janet Wang, Jiang Guo, Yi Xiang, Jiaqing Yuan, Mingwen Dong, Hideo Kobayashi, Shuaichen Chang, Chandan K. Reddy, Jiarong Jiang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 1.7（加权：大模型 0.9，世界模型 0.8）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《EvoBelief: Falsifiable World Models for Self-Improving LLM Agents》归入 大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, DiscoveryWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving LLM agents typically improve how they act through accumulated experience, reflection, or skills. Yet even procedurally capable agents can fail when their beliefs about environment dynamics are incomplete, incorrect, or outdated. We study a complementary axis of self-evolution: evolving those beliefs during deployment. Such beliefs can support multiple tasks, but incorrect ones can also propagate across them. We introduce EvoBelief, a self-evolving world model that represents environment knowledge as falsifiable hypotheses. Unexpected outcomes and decision-relevant unknowns trigger hypothesis formation. Later observations and controlled experiments provide independent validation before a rule can guide predictions or plans within its supported scope. Counterexamples narrow or retire rules as the environment changes. The language model remains frozen, and each rule remains linked to its evidence and the decisions it changes. Across four benchmarks spanning static dynamics, hidden drift, and scientific discovery, EvoBelief improves task performance and reuses learned rules across tasks. On ALFWorld without actor-side transition memory, it improves success over the matched Frozen World Model by 23.9% and 31.3% with Claude Haiku 4.5 and GPT-5.4, respectively. On MiniGrid, it revises stale rules and recovers after unannounced dynamics changes. In DiscoveryWorld's Reactor Lab, it discovers and validates quantitative laws, completing 83.3% of Normal-tier and 58.3% of Challenge-tier instances, versus 0% for each evaluated baseline. These results demonstrate self-improvement through testable, revisable environment knowledge rather than model-parameter updates.

</details>

---

### [[20_Research/Papers/具身智能/Imagine_the_Future,_Internalize_the_Gist_Efficient_VLA_Reasoning_via_Internalized_Spatiotemporal_Imagination|Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination]]

![[assets/2610.02626_figure.png|800]]

- **arXiv**: [2610.02626](https://arxiv.org/abs/2610.02626)
- **PDF**: https://arxiv.org/pdf/2610.02626
- **详细分析**: [[20_Research/Papers/具身智能/Imagine_the_Future,_Internalize_the_Gist_Efficient_VLA_Reasoning_via_Internalized_Spatiotemporal_Imagination|Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination]]
- **作者**: Shenglan Li, Zhendong Mi, Hengyi Zhu, Jingwu Luo, Chun Kit Chan, Geng Yuan, Yanzhi Wang, Pu Zhao, Shaoyi Huang
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Imagine the Future, Internalize the Gist: Efficient VLA Reasoning via Internalized Spatiotemporal Imagination》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, IG-VLA, OpenVLA, Real-World, TraceVLA, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models increasingly incorporate intermediate reasoning to improve robotic manipulation, yet existing approaches primarily reason about observed states without explicitly anticipating future scene evolution. Extending such reasoning to explicit future rollouts at every inference step, however, introduces substantial computational overhead. We propose IG-VLA, a VLA reasoning framework that enables models to imagine the future and internalize the gist. Our Latent Spatiotemporal Reasoning learns to imagine task-relevant future scene evolution directly in visual representation space, guiding action prediction without costly pixel-level video generation. To further reduce inference overhead, we introduce Scene Gist Memory, which internalizes reasoning-derived scene-behavior associations into a compact Scene Gist Token, preserving the benefits of future reasoning while bypassing explicit future imagination at inference. Extensive experiments on LIBERO, LIBERO-Plus, and VLABench demonstrate the effectiveness and efficiency of IG-VLA. On the LIBERO-Plus Language suite, both the reasoning and gist policies outperform the strongest baseline by nearly 6% in success rate. The gist policy also achieves up to 6.38x speedup over baselines, reducing inference latency from 1081ms to 169.5ms per action chunk on a single NVIDIA A6000 GPU. These results demonstrate that future spatiotemporal reasoning can be effectively internalized for efficient VLA deployment.

</details>

---
