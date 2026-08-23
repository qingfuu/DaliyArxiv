# cs.AI | Artificial Intelligence | 2026-08-21

#arxiv #ComputerScience

**论文数**: 42

### [[20_Research/Papers/大模型/An_Agentic_Approach_for_Active_Data_Collection,_Travel_Behavior_Modeling,_and_Weather-Sensitive_Demand_Prediction|An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction]]

![[assets/2608.20320_figure.png|800]]

- **arXiv**: [2608.20320](https://arxiv.org/abs/2608.20320)
- **PDF**: https://arxiv.org/pdf/2608.20320
- **详细分析**: [[20_Research/Papers/大模型/An_Agentic_Approach_for_Active_Data_Collection,_Travel_Behavior_Modeling,_and_Weather-Sensitive_Demand_Prediction|An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction]]
- **作者**: Narges Ahmadi, Yubo Jiao, Jônatas Augusto Manzolli, Jiangbo Yu, Luis Miranda-Moreno
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《An Agentic Approach for Active Data Collection, Travel Behavior Modeling, and Weather-Sensitive Demand Prediction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Travel behavior research increasingly combines digital data collection with predictive modeling, yet these stages are often developed and evaluated separately. This study proposes a three-agent workflow integrating conversational data collection, structured data processing, and behavioral prediction. A chatbot-administered, image-augmented stated-preference survey collected mode choices from student commuters across five predefined weather scenarios, yielding 454 respondent-scenario observations. Weather-related associations were analyzed using a multinomial logit model, while logistic regression and random forest provided machine-learning benchmarks. Nine locally deployed large language models (LLMs), ranging from 2 to 35 billion parameters, were evaluated across four zero-shot prompt-and-context conditions and extended through persona, few-shot, and vision-based configurations. Random forest achieved 69.6% five-class accuracy, while the best text-only zero-shot LLM reached 69.9% without task-specific fitting. Habitual travel information produced the most consistent gains, Expert framing generally outperformed Role-Play, and persona information was most useful when habitual travel information was unavailable. Few-shot prompting improved prediction for several models, with gains stabilizing after a small number of examples. Using the same weather images shown to respondents, the best vision-based configuration reached 71.5% five-class accuracy, indicating that visual context may provide additional predictive information for selected models. Overall, the study shows how conversational surveys, structured data processing, conventional behavioral modeling, machine learning, and multimodal LLM prediction can be coordinated within an auditable multi-agent workflow.

</details>

---

### [[20_Research/Papers/大模型/AI4AI-Bench_Benchmarking_LLM_Agents_in_Algorithmic_Design_for_Recursive_Self-Improvement|AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement]]

![[assets/2608.20318_first_page.png|800]]

- **arXiv**: [2608.20318](https://arxiv.org/abs/2608.20318)
- **PDF**: https://arxiv.org/pdf/2608.20318
- **详细分析**: [[20_Research/Papers/大模型/AI4AI-Bench_Benchmarking_LLM_Agents_in_Algorithmic_Design_for_Recursive_Self-Improvement|AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement]]
- **作者**: Yizhe Chi, Wenyi Li, Deyao Hong, Xiaoqiu Wang, Mingju Gao, Kaisen Yang, Bingxiang He, Youjie Zheng, Calvin Xiao, Qinhuai Na
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AI4AI-Bench: Benchmarking LLM Agents in Algorithmic Design for Recursive Self-Improvement》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AI4AI-Bench, IFEval, ImageNet, LiveCodeBench, MLS-Bench, PostTrainBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recursive self-improvement (RSI) asks whether an AI system can improve the process that produces AI systems, so that the next system inherits the improvement. That process is the training algorithm: a better objective or update rule improves the compute\mbox{-}capability exchange rate for every subsequent run, including the one that produces the next agent. Whether RSI is feasible therefore turns on whether an agent can design training algorithms. No benchmark isolates that ability: existing suites are won by collecting data or by tuning hyperparameters, and none tells a change to how a run is executed apart from a change to how the model learns. We present AI4AI\mbox{-}Bench, 10 frozen research repositories spanning 10 training algorithm families. In each task, an agent has 4 hours on one B300 to rewrite the training algorithm; its code is then rerun from scratch for up to 12 hours and scored by a fixed evaluator hidden from the agent, against the repository's original algorithm under the same procedure. Because the 10 metrics are incommensurable, every task is mapped onto one scale on which $0$ is an uninformative model, $0.1$ is the algorithm the repository ships, and $1.0$ is the task optimum. Across 29 configurations of 6 systems on all 10 tasks the mean score is $0.166$, and the best system reaches $0.250$: even the strongest closes under a fifth of the distance between the algorithm that was already there and the optimum. The submissions show where that distance went: most never change how the model learns at all, and the minority that do average $0.226$ against $0.126$ for the rest. More reasoning effort mostly buys the willingness to go there, taking that minority from $8\%$ of submissions to $64\%$ and the mean score from $0.094$ to $0.196$. We release the task suite, the evaluators and every scored submission, so that the measurement can be repeated as these systems change.

</details>

---

### [[20_Research/Papers/大模型/Break_It_Down,_Pass_It_On_Cross-Task_Skill_Transfer_in_LLM_Agents|Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents]]

![[assets/2608.20274_figure.png|800]]

- **arXiv**: [2608.20274](https://arxiv.org/abs/2608.20274)
- **PDF**: https://arxiv.org/pdf/2608.20274
- **详细分析**: [[20_Research/Papers/大模型/Break_It_Down,_Pass_It_On_Cross-Task_Skill_Transfer_in_LLM_Agents|Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents]]
- **作者**: Yiyang Feng, Biddut Sarker Bijoy, Niranjan Balasubramanian, Jiawei Zhou
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents can induce skills from completed tasks and reuse them later to grow more capable with experience. In practice, induced skills may transfer unreliably and can even harm the agent that retrieves them. When agent-induced skills transfer reliably across tasks remains an open question. We conduct a comprehensive and controlled study of how the way skills are induced shapes their transfer across tasks. Specifically, we compare task-level with subtask-level skill induction and text with code skill formats, the two axes along which existing methods differ. Task-level skills mostly reduce the agent's performance below its no-memory baseline while subtask-level skills raise it above on average, and text skills transfer better than code skills. To further understand our findings, we examine two complementary properties of the induced skills: specificity, which measures how closely a skill matches real tasks, and abstractness, which measures how evenly its relevance spreads across tasks. Neither property alone predicts task success, but their combined effect does, which we propose as a skill utility score. The score correlates consistently with task success when skills are transferred, and subtask-level and text skills score higher. Computing skill utility only needs the skills and task descriptions but not any task execution, so our score serves as a practical diagnostic of a skill memory before any new task runs.

</details>

---

### [[20_Research/Papers/强化学习/Learning_When_to_Think_Adaptive_Reasoning_for_Test-Time_Compute_Allocation|Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation]]

![[assets/2608.20256_first_page.png|800]]

- **arXiv**: [2608.20256](https://arxiv.org/abs/2608.20256)
- **PDF**: https://arxiv.org/pdf/2608.20256
- **详细分析**: [[20_Research/Papers/强化学习/Learning_When_to_Think_Adaptive_Reasoning_for_Test-Time_Compute_Allocation|Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation]]
- **作者**: Gijs Kassenaar, Zhao Yang, Vincent François-Lavet
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，强化学习 0.4）
- **关联关键词**: RL

#### 研究背景与动机

《Learning When to Think: Adaptive Reasoning for Test-Time Compute Allocation》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning language models trained with reinforcement learning typically operate under a fixed token budget rather than an explicitly adaptive one, which can lead to over-computation on easy problems and insufficient computation on difficult ones. We study whether a model can learn to allocate its own reasoning effort by choosing, as the first token of its response, one of three modes: \textsc{NoThink} (answer as quickly as possible), \textsc{Short} (brief reasoning), or \textsc{Long} (extended reasoning). The choice is learned inside Group Relative Policy Optimization (GRPO) with no separate router, through a shaped reward that makes each mode worthwhile at a different response length, together with hard per-mode token caps that keep the modes distinct. On a 1.5B distilled model trained on MATH, the three modes emerge without collapsing to a single choice, and the brief modes end up more accurate than \textsc{Long}, which shows that the router sorts problems by difficulty rather than at random. Averaged over three seeds, the resulting policy stays close to the base model's accuracy on the held-out MATH500 ($0.782$ vs.\ $0.796$) while cutting the mean response length from $4{,}796$ to $2{,}811$ tokens (a $41\%$ reduction). Interestingly, it also transfers to other benchmarks without retraining, with the largest savings where problems are easier, with for instance 76\% token reduction on GSM8K and at higher accuracy than the baselines at similar response length. In short, we build a reasoning model that adaptively chooses how much to reason for each problem.

</details>

---

### [[20_Research/Papers/其他/From_Agent_Behaviour_to_Agent-Friendly_Documentation_An_Empirical_Study_of_How_Coding_Agents_Discover,_Read,_and_Write_Technical_Documentati|From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of How Coding Agents Discover, Read, and Write Technical Documentation]]

![[assets/2608.20195_figure.png|800]]

- **arXiv**: [2608.20195](https://arxiv.org/abs/2608.20195)
- **PDF**: https://arxiv.org/pdf/2608.20195
- **详细分析**: [[20_Research/Papers/其他/From_Agent_Behaviour_to_Agent-Friendly_Documentation_An_Empirical_Study_of_How_Coding_Agents_Discover,_Read,_and_Write_Technical_Documentati|From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of How Coding Agents Discover, Read, and Write Technical Documentation]]
- **作者**: Zhijun Gao, Jing Chen
- **cs 子类**: cs.AI, cs.HC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《From Agent Behaviour to Agent-Friendly Documentation: An Empirical Study of How Coding Agents Discover, Read, and Write Technical Documentation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Technical documentation is written for human developers, but an increasing share of software changes is now authored by autonomous coding agents. Which documents they consult, when, and what follows remain unknown. We conduct a behaviour-grounded study of agent-documentation interaction across two public datasets: 557 agentic coding sessions from SWE-chat, yielding 94,813 development events including 3,033 documentation interactions; and 33,097 agentic pull requests from AIDev, with 690,260 classified file-level change records. Four findings challenge current documentation practice. First, agents' documentation work is dominated by agent-facing artefacts: instruction files and working notes account for 60.5% of all documentation interactions, versus 10.6% for classical technical documentation and 1.3% for API references. Second, the link between consultation and code editing is unresolved: the adjacent transition probability is 0.002 and the unadjusted three-event lift 1.05, whereas a stage-adjusted model places it above unity (OR 1.33 [1.09, 1.62]); documentation creation is elevated unadjusted (lift 1.67) but its adjusted interval includes unity. Third, no explicit documentation-based validation sequence was observed, and consultation is associated with less immediate testing (lift 0.23, cluster CI 0.08-0.45; adjusted OR 0.39 [0.25, 0.60]). Fourth, consultation is self-initiated (70.2%) far more often than failure-driven (7.5%), and documentation trails code: among multi-commit pull requests changing both, code is touched first 4.7x more often. From these traces we derive a descriptive model of agent-documentation interaction as a two-lobed cycle rather than a linear journey, and show that two widely assumed properties of "agent-friendly" documentation - actionability and verifiability - lack consistent behavioural support. We release our pipeline, coding scheme, and event-level data.

</details>

---

### [[20_Research/Papers/大模型/DARS_Dual-Level_Credit_Assignment_RL_with_Structured_Reasoning_for_Instruction-Based_Image_Editing|DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing]]

![[assets/2608.20161_figure.png|800]]

- **arXiv**: [2608.20161](https://arxiv.org/abs/2608.20161)
- **PDF**: https://arxiv.org/pdf/2608.20161
- **详细分析**: [[20_Research/Papers/大模型/DARS_Dual-Level_Credit_Assignment_RL_with_Structured_Reasoning_for_Instruction-Based_Image_Editing|DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing]]
- **作者**: Haoxiang Cao, Jiajiong Cao, Xuanpu Zhang, Changqian Yu, Chaoqun Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.7（加权：大模型 0.3，强化学习 0.4）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based Image Editing》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GEdit-Bench, ImgEdit-Bench, KRIS-Bench, PICA-Bench, PromptRL, RISE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Instruction-based image editing uses a planner-renderer pipeline: a vision-language model (VLM) first converts the instruction into an edit plan, and a diffusion model then executes that plan. Training such systems with only final-image rewards is inefficient because a poor edit does not reveal whether additional optimization should place more emphasis on the planner or the renderer, and even planner-dominant cases remain difficult to localize within a free-form reasoning trace. We present DARS, a reinforcement learning framework for dual-level credit assignment in this two-stage setting. Across modules, multi-plan multi-render rollouts estimate between-plan and within-plan reward variability for soft module routing, while rollout mean rewards provide hardness estimates for an adaptive curriculum. Within the planner, a four-field structured reasoning output enables a prefix-gated reward and token-level advantage reweighting, turning outcome-level feedback into localized supervision. Experiments on five benchmarks show that DARS outperforms a Joint~RL baseline with the same backbone, data, reward model, and rollout budget, with the largest gains on reasoning-intensive edits.

</details>

---

### [[20_Research/Papers/具身智能/DECOWAM_Decoupled_Whole-Body_World-Action_Model_for_Legged_Mobile_Manipulation|DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation]]

![[assets/2608.20114_figure.png|800]]

- **arXiv**: [2608.20114](https://arxiv.org/abs/2608.20114)
- **PDF**: https://arxiv.org/pdf/2608.20114
- **详细分析**: [[20_Research/Papers/具身智能/DECOWAM_Decoupled_Whole-Body_World-Action_Model_for_Legged_Mobile_Manipulation|DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation]]
- **作者**: Siyuan Ma, Boshi Zhang, Yutian Zhang, Qinglian Wu, Jiaqi Zhai, Dong Wei, Qiaojun Yu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《DECOWAM: Decoupled Whole-Body World-Action Model for Legged Mobile Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GRL, OpenVLA, RLBench, RoboNet, UniSim, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile manipulation requires a robot to predict how locomotion and arm motion jointly alter future observations and control. Existing world-action models, developed largely for fixed-base platforms, do not explicitly distinguish camera ego-motion from base and arm actions. Here we introduce DECOWAM, a whole-body world-action model that separates these factors through dedicated conditional interfaces. DECOWAM freezes an adapted FastWAM backbone and trains residual adapters, an action-equivalent future bottleneck distilled from privileged observations, adversarially separated base and arm latents, and base-velocity conditioning for video prediction. We further introduce ARMDOG, a real-robot dataset that synchronizes video, whole-body state and action, and language. On a fixed replay protocol, DECOWAM improved both future-video and action prediction over FastWAM, reducing action MSE by 21.7% with 25.95M trainable adaptation parameters. Across 79 closed-loop trials per method, it achieved the highest observed whole-body coordination and base-displacement robustness among the compared systems, while task completion remained comparable to the strongest baseline. These results show that embodiment-aware factorization can support parameter-efficient joint visual prediction and whole-body control under moving viewpoints.

</details>

---

### [[20_Research/Papers/机器人/Towards_Professional_Tennis_Styles_for_Humanoid_Robots_with_Adaptive_Motion_Planning_and_Tracking|Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking]]

![[assets/2608.20087_figure.png|800]]

- **arXiv**: [2608.20087](https://arxiv.org/abs/2608.20087)
- **PDF**: https://arxiv.org/pdf/2608.20087
- **详细分析**: [[20_Research/Papers/机器人/Towards_Professional_Tennis_Styles_for_Humanoid_Robots_with_Adaptive_Motion_Planning_and_Tracking|Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking]]
- **作者**: Tao Huang, Ruofei Liu, Xuchen Tang, Xinyin Zhang, Junli Ren, Huayi Wang, Feiyu Jia, Yukai Qi, Kangning Yin, Weishuai Zeng, Lipeng Chen, Xi Li...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.9（加权：具身智能 1.8，机器人 2.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Towards Professional Tennis Styles for Humanoid Robots with Adaptive Motion Planning and Tracking》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots have recently demonstrated promising capabilities in real-world ball sports. However, achieving professional motion styles while maintaining strong task performance remains challenging. In this work, we propose AdaPT, an Adaptive Motion Planning and Tracking framework that learns professional tennis serving and rally styles directly from broadcast videos. This hierarchical design is motivated by the key insight that the planner generates stylistic kinematic motions, while the tracker executes them with minimal interference with planning. Despite its effectiveness in simulation, a substantial sim-to-real gap emerges: tracking performance inevitably degrades on real robots, and this degradation is partially overlooked by autoregressive planning and further compounded by noisy perception. To address these issues, our adaptation mechanism improves tracking robustness by learning to track randomized execution speeds, while conditioning the planner on a learned motion-speed adapter to mitigate compounding errors. Real-world experiments on the Unitree G1 demonstrate the effectiveness of our adaptation mechanism in bridging the sim-to-real gap. We further deploy AdaPT policies on the full-size Dobot Atom humanoid robot (1.7m) and demonstrate in-the-wild serving without motion capture. Beyond these results, our real-world experiments reveal both algorithmic and engineering insights for future humanoid ball-sports systems. Videos and code are available on our \href{https://humanoidtennis.github.io/AdaPT/}{project website}.

</details>

---

### [[20_Research/Papers/机器人/Evidence-Gated_Task_and_Motion_Planning_with_Vision-Language_Models|Evidence-Gated Task and Motion Planning with Vision-Language Models]]

![[assets/2608.20084_figure.png|800]]

- **arXiv**: [2608.20084](https://arxiv.org/abs/2608.20084)
- **PDF**: https://arxiv.org/pdf/2608.20084
- **详细分析**: [[20_Research/Papers/机器人/Evidence-Gated_Task_and_Motion_Planning_with_Vision-Language_Models|Evidence-Gated Task and Motion Planning with Vision-Language Models]]
- **作者**: Tsunehiko Tanaka, Matthew Stephenson, Alistair Macvicar, Edgar Simo-Serra
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Evidence-Gated Task and Motion Planning with Vision-Language Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots executing long-horizon manipulation tasks from natural-language instructions must reason about both semantic task structure and geometric feasibility. However, under partial observability, the availability of goal-relevant objects may be uncertain. In such cases, approaches that combine Vision-Language Models (VLMs) with Task and Motion Planning (TAMP) may generate subgoals that rely on the VLM's prior knowledge without observational support, leading to execution failures or unintended outcomes. We propose Evidence Acquisition and Feasibility Gating (EAFG), a framework that acquires visual evidence through VLM-generated exploratory subgoals and TAMP-based execution. EAFG then applies a feasibility gate to decide whether to proceed with task planning, acquire further evidence, or halt. Our experiments show that, in cooking tasks with ambiguous object use, EAFG improves recipe completion by discovering task-relevant objects before planning. For instructions requiring an absent object, EAFG promotes appropriate halt decisions and reduces repeated attempts to manipulate that object.

</details>

---

### [[20_Research/Papers/大模型/Optimal_Skill_Selection_for_LLM_Agents_with_Provable_Bicriteria_Guarantees|Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees]]

![[assets/2608.19993_figure.png|800]]

- **arXiv**: [2608.19993](https://arxiv.org/abs/2608.19993)
- **PDF**: https://arxiv.org/pdf/2608.19993
- **详细分析**: [[20_Research/Papers/大模型/Optimal_Skill_Selection_for_LLM_Agents_with_Provable_Bicriteria_Guarantees|Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees]]
- **作者**: Yu Chen, Ruishuo Chen, Xun Wang, Zhuoran Li, Longbo Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Optimal Skill Selection for LLM Agents with Provable Bicriteria Guarantees》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BigCodeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Loading reusable skill documents into a bounded context window is now the primary way large language model (LLM) agents acquire task-specific capabilities, which makes skill selection a first-order determinant of task performance and token cost. Yet current agents score skills independently by semantic relevance and assemble the set by top-$k$ or greedy packing, with no quality guarantee or cost awareness on the selected set. As a result, redundant or poorly chosen skills waste scarce context tokens and can even degrade performance. We give the first model of how the selected skill set shapes execution outcomes and cast skill selection as an optimization problem: choose a skill set under a hard token budget to maximize a monotone submodular benefit minus context penalty. For this problem, we develop Best Prefix Selection (BPS), a polynomial-time algorithm, and prove, to our knowledge, the first performance guarantee for skill selection: a bicriteria $(1-1/e,1)$ approximation whose benefit coefficient is optimal in polynomial time. On a contamination-controlled BigCodeBench variant, BPS outperforms all the baselines, reaching $0.73$ measured task success versus $0.20$--$0.52$ for released skill routers, text retrievers, and the executor's own selection, on $28\%$ fewer tokens than the strongest released router.

</details>

---

### [[20_Research/Papers/大模型/ReguSim_Evaluating_LLM_Agent_Rule_Grounding_in_Financial_Compliance|ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance]]

![[assets/2608.19974_figure.png|800]]

- **arXiv**: [2608.19974](https://arxiv.org/abs/2608.19974)
- **PDF**: https://arxiv.org/pdf/2608.19974
- **详细分析**: [[20_Research/Papers/大模型/ReguSim_Evaluating_LLM_Agent_Rule_Grounding_in_Financial_Compliance|ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance]]
- **作者**: Yiyang Luo, Yihang Jiang, Qijun Xie, Liang Lan, Lin Willian Cong, Anyi Rao, Yunya Song
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ReguSim: Evaluating LLM Agent Rule Grounding in Financial Compliance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LegalBench, LexEval, ReguBench, ReguSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents in financial markets may cite rules yet still submit orders that violate executable constraints or misread surveillance evidence. We introduce ReguSim, a controlled financial-compliance environment, and ReguBench, a target-marked monitoring benchmark, to separate four artifacts: stated reasoning, attempted action, execution enforcement, and monitor evidence. In trader runs with DeepSeek V4 Pro and Gemini 3.5 Flash, visible rules reduce but do not eliminate rejected actions, and incentive or persona framing shifts behavior. A bridge study shows that trader rationales can mislead an independent monitor unless enforcement evidence is shown. In monitoring, simple structured baselines either match or exceed prompt-only LLMs. The results frame financial compliance evaluation as an audit of rule-grounded actions and evidence use, rather than a single compliance score.

</details>

---

### [[20_Research/Papers/大模型/MaliciousSkillBench_A_Comprehensive_Benchmark_for_Malicious_Agent_Skill_Detection|MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection]]

![[assets/2608.19901_figure.png|800]]

- **arXiv**: [2608.19901](https://arxiv.org/abs/2608.19901)
- **PDF**: https://arxiv.org/pdf/2608.19901
- **详细分析**: [[20_Research/Papers/大模型/MaliciousSkillBench_A_Comprehensive_Benchmark_for_Malicious_Agent_Skill_Detection|MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection]]
- **作者**: Yue Wang, Yi Liu, Gelei Deng, Ying Zhang, Yuekang Li, Zhenyu Chen, Leo Zhang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《MaliciousSkillBench: A Comprehensive Benchmark for Malicious Agent Skill Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MalSkillBench, MaliciousSkillBench, SkillFortifyBench, SkillSafetyBench, SkillTrustBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent Skills extend LLM agents with reusable instruction packages that may also include scripts, resources, and service configuration. This creates a direct distribution channel for malicious behavior, yet existing malicious-Skill datasets are fragmented across sources, artifact formats, evidence regimes, and benign coverage; duplicated and structurally related content further complicates direct aggregation and evaluation. We present MaliciousSkillBench, a comprehensive benchmark for malicious Agent Skill detection. We consolidate 13 public sources, 11 of which contribute Core malicious artifacts, and reduce 8,414 raw malicious records to 7,539 normalized-unique identities in 4,588 operational structural families. After conservative cross-label conflict exclusion, the primary benchmark contains 9,740 Skills: 7,505 malicious and 2,235 benign. To characterize its coverage, we harmonize 11 attack categories for 4,983 malicious identities with supported source-native mappings and find substantial differences in threat composition across sources. We then evaluate three learned text detectors and three off-the-shelf Skill scanners. Learned detectors achieve 0.882-0.932 Random Macro-F1 but only 0.653-0.665 under Source-Disjoint evaluation; the strongest word TF-IDF SVM scores 0.932/0.916/0.665 on Random/structural-disjoint/Source-Disjoint while retaining 95.6% malicious recall but producing 62.4% benign FPR on held-out sources. Off-the-shelf scanners occupy different but also unsatisfactory operating regimes, reducing false positives only at the cost of sharply lower malicious recall. Together, these results show that reliable malicious-Skill detection requires both broader cross-source benchmark coverage and evaluation that jointly measures attack detection and benign over-flagging.

</details>

---

### [[20_Research/Papers/具身智能/EXIMO_VLM_Guided_Exploration_of_VLA_Policies|EXIMO: VLM Guided Exploration of VLA Policies]]

![[assets/2608.19891_first_page.png|800]]

- **arXiv**: [2608.19891](https://arxiv.org/abs/2608.19891)
- **PDF**: https://arxiv.org/pdf/2608.19891
- **详细分析**: [[20_Research/Papers/具身智能/EXIMO_VLM_Guided_Exploration_of_VLA_Policies|EXIMO: VLM Guided Exploration of VLA Policies]]
- **作者**: Bhavya Sukhija, Oliver Groth, Mohit Shridhar, Tim Hertweck, Michael Bloesch, Markus Wulfmeier, Abbas Abdolmaleki, Martin Riedmiller
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 强化学习
- **相关性评分**: 2.9（加权：具身智能 1.8，大模型 0.5，强化学习 0.2，机器人 0.4）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《EXIMO: VLM Guided Exploration of VLA Policies》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How to efficiently finetune robot policies to learn new tasks on the fly? State of the art robotic manipulation policies are based on behaviour cloning of large vision-language-action (VLA) models with billions of parameters on huge teleoperation datasets. While this simple approach has enabled significant advances for robotic manipulation, finetuning of VLA policies for learning new tasks still remains an open problem. In particular, collecting teleoperation datasets requires hundreds of hours of expensive human labour and the alternative, reinforcement learning (RL), can be notoriously sample-inefficient especially for long-horizon tasks. In addition, RL with VLAs imposes several challenges due to the model's size and architectural design. In this work, we propose EXIMO, an efficient algorithm for finetuning of VLA policies. EXIMO operates in three stages: explore, imitate, and optimize. During the explore phase, EXIMO equips the VLA with a vision language model (VLM) that acts as a planner. The VLM thinks and breaks down challenging long-horizon problems into shorter ones for the VLA. The VLM, together with the VLA, is used to collect an orchestrated dataset on new tasks. During the imitate phase, the VLA is finetuned with the orchestrated data. Finally, during the optimize stage, we use residual off-policy RL to further finetune the policy. In our experiments, we ablate all three stages of EXIMO and show that it outperforms existing approaches significantly in terms of sample-efficiency and final performance.

</details>

---

### [[20_Research/Papers/大模型/EnvHarness_Awakening_Static_Worlds_for_Agent_Learning|EnvHarness: Awakening Static Worlds for Agent Learning]]

![[assets/2608.19880_first_page.png|800]]

- **arXiv**: [2608.19880](https://arxiv.org/abs/2608.19880)
- **PDF**: https://arxiv.org/pdf/2608.19880
- **详细分析**: [[20_Research/Papers/大模型/EnvHarness_Awakening_Static_Worlds_for_Agent_Learning|EnvHarness: Awakening Static Worlds for Agent Learning]]
- **作者**: Chengsong Huang, Zifeng Wang, Rujun Han, Jun Yan, Yanfei Chen, Zoey CuiZhu, Ke Jiang, Peng Xia, Han Yu, Yufan Zhuang, Yifei Ming, Jiaqi Pan...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.27（加权：大模型 0.75，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EnvHarness: Awakening Static Worlds for Agent Learning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents learn by interacting with environments, yet these environments are hand-built and static: blind to an agent's weaknesses, and quickly left behind as it improves. While recent environment generation methods attempt to address this, they require domain-specific pipelines, rely on expensive or unreliable verifiers, and still produce static environments. To alleviate the engineering burden of rebuilding environments from scratch, we propose Environment Harness (EnvHarness), a programmable layer of plug-in components that wraps a static environment to reshape its behavior without modifying the underlying logic. Operating through standard interfaces, EnvHarness applies across diverse domains while ensuring every reshaped environment retains its original verifier. To automate this process, we introduce EnvRigger, which treats the target policy as a black box, observing its execution trajectories to synthesize EnvHarness components targeting diagnosed flaws, and validating them via fresh rollouts. Across five benchmarks in four domains, EnvHarness outperforms both original environments and domain-specific environment generation pipelines, achieving up to a 9.0-point improvement on held-out instances with 9.8% fewer execution steps. Furthermore, EnvHarness provides a superior optimization signal for reinforcement learning, enabling continuous, targeted co-evolution of the policy and its environment.

</details>

---

### [[20_Research/Papers/大模型/PolicyGuide_From_Guarding_One_Action_to_Guiding_the_Whole_Workflow_for_Policy-Compliant_LLM_Agents|PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents]]

![[assets/2608.19861_figure.png|800]]

- **arXiv**: [2608.19861](https://arxiv.org/abs/2608.19861)
- **PDF**: https://arxiv.org/pdf/2608.19861
- **详细分析**: [[20_Research/Papers/大模型/PolicyGuide_From_Guarding_One_Action_to_Guiding_the_Whole_Workflow_for_Policy-Compliant_LLM_Agents|PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents]]
- **作者**: Seongjae Kang, Taehyung Yu, Sung Ju Hwang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《PolicyGuide: From Guarding One Action to Guiding the Whole Workflow for Policy-Compliant LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentRewardBench, FlowBench, JourneyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Customer-service LLM agents must follow organizational policy when acting on a user's behalf. Compliance failures arise from either forbidden actions, such as granting an ineligible change, or omitted procedural requirements, such as identification or confirmation. Runtime safeguards can intervene on risky actions, but action-local checks do not guide an agent through a multi-step procedure. Workflow-following systems support prescribed process execution, but primarily target workflow completion rather than safeguarding agent behavior. PolicyGuide instead compiles each domain policy into a workflow graph and invokes a proactive verifier at user-turn boundaries. From persisted graph state, the verifier reconciles open requests and returns step-specific remediation along a policy-compliant path. Across the $τ^2$-bench airline, retail, and telecom domains with a GPT-5.4 agent and verifier, PolicyGuide raises mean $\mathrm{Pass}^4$ from $0.42$ to $0.62$, with the largest gain on telecom ($0.19$ to $0.61$), the most workflow-structured domain. The same workflows transfer to Claude Sonnet 4.6 and Gemini 2.5 Pro agents. Complementary evaluations find the lowest observed attack-success rate under adversarial users and the strongest procedural compliance in an author-designed workflow-level validation.

</details>

---

### [[20_Research/Papers/强化学习/SAPO_Single-Rollout_Autoregressive_Policy_Optimization_for_Agentic_Reinforcement_Learning|SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning]]

![[assets/2608.19842_figure.png|800]]

- **arXiv**: [2608.19842](https://arxiv.org/abs/2608.19842)
- **PDF**: https://arxiv.org/pdf/2608.19842
- **详细分析**: [[20_Research/Papers/强化学习/SAPO_Single-Rollout_Autoregressive_Policy_Optimization_for_Agentic_Reinforcement_Learning|SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning]]
- **作者**: Dayang Liang, Lang Feng, Bo An, Yunlong Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL

#### 研究背景与动机

《SAPO: Single-Rollout Autoregressive Policy Optimization for Agentic Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, AgentGym-RL, ToRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning (RL) has become a critical stage in the post-training of large language models. Existing critic-free, group-relative methods estimate policy advantages from multiple rollouts, avoiding the substantial memory overhead of conventional proximal policy optimization (PPO) and achieving strong performance on long-horizon interactive tasks. Despite their success, recent studies revealed three limitations: (1) Lack explicit value generalization and effective temporal credit assignment; (2) Suffer from potential advantage collapse in long-horizon complex tasks; (3) Require a costly trade-off between sampling budget and policy performance. In this work, we propose Single-rollout Autoregressive Policy Optimization (SAPO), a low-memory and compute-efficient framework in which the policy and value functions share a single autoregressive backbone. SAPO exploits the autoregressive structure of LLMs to produce policy and value predictions at distinct causal boundaries with shared parameters, while independently optimizing the PPO objectives and auxiliary on-policy SARSA objectives. To robustly estimate the contribution of each turn, we further introduce a trajectory-level generalized advantage estimator that combines lambda-returns with batch normalization. Experiments across ALFWorld and WebShop with Qwen2.5-1.5B/7B show that SAPO trains stably and outperforms PPO and GRPO by mean +15.1 and +12.1 percentage points, respectively, while eliminating the memory cost of a separate critic model and reducing per-iteration runtime by 33.2% over PPO.

</details>

---

### [[20_Research/Papers/强化学习/Adaptive_Probabilistic_Shielding_by_Learning_MDPs_for_Safe_Reinforcement_Learning|Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning]]

![[assets/2608.19836_figure.png|800]]

- **arXiv**: [2608.19836](https://arxiv.org/abs/2608.19836)
- **PDF**: https://arxiv.org/pdf/2608.19836
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Probabilistic_Shielding_by_Learning_MDPs_for_Safe_Reinforcement_Learning|Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning]]
- **作者**: Astrid Horn Brorholt, Maris F. L. Galesloot, Nils Jansen, Kim Guldstrand Larsen, Christian Schilling
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Adaptive Probabilistic Shielding by Learning MDPs for Safe Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Probabilistic shielding is a technique for safe reinforcement learning (RL). Typically, a static observer -- called the shield -- constrains the learning agent's actions to those for which acting safely remains feasible. Traditionally, the shield is computed from the transition probabilities of the underlying Markov decision process (MDP). Thus, this technique is not applicable when the MDP model is not given a priori, which, unfortunately, is the case in typical RL applications. In this paper, we study the problem of computing a shield in the setting where the transition graph of the MDP is known, but the transition probabilities are unknown. Our approach integrates probabilistic shielding with online model learning: as the RL agent explores the environment, we estimate the transition probabilities. From this estimate, we compute a shield. While the shield may be conservative initially, it adapts as the model estimate becomes more precise. Thus, the shield improves in tandem with the RL agent. This paradigm of adaptive probabilistic shielding raises a number of challenges, such as when to recompute the shield and how to balance between exploration and safety during learning. We empirically evaluate multiple variants of this paradigm across several environments.

</details>

---

### [[20_Research/Papers/强化学习/ADAPT_Physics-Aware_Diffusion-based_World_Models_for_Adaptive_Predictive_Transferable_HVAC_Control|ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control]]

![[assets/2608.19804_first_page.png|800]]

- **arXiv**: [2608.19804](https://arxiv.org/abs/2608.19804)
- **PDF**: https://arxiv.org/pdf/2608.19804
- **详细分析**: [[20_Research/Papers/强化学习/ADAPT_Physics-Aware_Diffusion-based_World_Models_for_Adaptive_Predictive_Transferable_HVAC_Control|ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control]]
- **作者**: Xu Yang, Kailai Sun, Dianyu Zhong, Qianchuan Zhao
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，世界模型 0.8）
- **关联关键词**: RL, WorldModel, Security

#### 研究背景与动机

《ADAPT: Physics-Aware Diffusion-based World Models for Adaptive Predictive Transferable HVAC Control》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：SemibuildingSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Buildings account for roughly one-third of global energy consumption and CO$_2$ emissions. Optimizing indoor climate systems plays a critical role for urban climate mitigation aligned with UN Sustainable Development Goals 11 and 13. However, indoor delayed thermodynamic responses and partial observability severely hinder existing methods, which are primarily limited by implicit thermal inertia, occupancy dynamic prediction, and cumulative prediction errors, especially for out-of-distribution environments. In practice, these challenges are further exacerbated by the high cost and privacy burden of dense indoor sensing, forcing operators to collect only limited data in a single operating regime while expecting controllers to generalize reliably across unseen seasons and climate regions. To address this problem, we propose ADAPT, a physics-aware conditional diffusion indoor environmental world model for HVAC control. The model predicts a short-horizon held-action thermal baseline to capture the latent thermal inertia of the buildings. The diffusion backbone utilizes the robustness of generative models, while a learnable multi-zone heat-balance regularizer constrains generated trajectories to satisfy transferable building thermodynamics without requiring known building geometry or manually calibrated thermal parameters. A credit assignment is then design for the downstream reinforcement learning. Extensive experiments on SemibuildingSim and Sinergym demonstrate that ADAPT reduces HVAC energy consumption by 7.3\% and occupant discomfort by 30.2\% compared with state-of-the-art baselines under IID control. Under OOD control scenarios spanning unseen seasons and climate regions, ADAPT maintains robust performance with only marginal degradation relative to its IID performance, substantially outperforming existing methods in transfer robustness.

</details>

---

### [[20_Research/Papers/大模型/MileGPO_Milestone_Inference_with_Local_Evidence_for_Graph-Based_Policy_Optimization_of_Long-Horizon_LLM_Agents|MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents]]

![[assets/2608.19803_figure.png|800]]

- **arXiv**: [2608.19803](https://arxiv.org/abs/2608.19803)
- **PDF**: https://arxiv.org/pdf/2608.19803
- **详细分析**: [[20_Research/Papers/大模型/MileGPO_Milestone_Inference_with_Local_Evidence_for_Graph-Based_Policy_Optimization_of_Long-Horizon_LLM_Agents|MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents]]
- **作者**: Bo Qian, Yuting Wu, Shuang Zeng, Huaiyu Wan, Dalin Zhang, Jiqiang Liu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.07（加权：大模型 0.75，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《MileGPO: Milestone Inference with Local Evidence for Graph-Based Policy Optimization of Long-Horizon LLM Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, TreeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Credit assignment is challenging in long-horizon agentic reinforcement learning, where supervision often comes only from final rewards. Existing methods refine trajectory-level signals into step-level credits through step grouping or graph-based advantage estimation, but can overlook meaningful intermediate milestones. We propose MileGPO (Milestone Inference with Local Evidence for Graph-Based Policy Optimization), which derives process-level credit from grouped on-policy rollouts through three designs. Milestone Discovery identifies candidate milestones on successful rollouts and recurring traps on failed ones. Reliability-Calibrated Shaping (RCS) weights these candidates by outcome-based confidence, strengthening reliable milestones and traps while down-weighting uncertain ones. Progress-Contrastive Calibration (PCC) further tests whether a candidate reflects local progress and whether its incoming ansition outperforms observed alternatives from the same state.MileGPO requires neither auxiliary models nor additional environment interaction. Experiments on ALFWorld and WebShop show state-of-the-art performance and a small in-distribution to out-of-distribution gap on ALFWorld. Ablations and credit diagnostics indicate that reliability weighting, local progress, and same-state branch evidence complement milestone discovery and resolve ambiguous intermediate credit.

</details>

---

### [[20_Research/Papers/具身智能/Towards_general_embodied_intelligence_integrating_large_language_models,_knowledge_bases,_and_reasoning_capabilities_to_build_the_next_gener|Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents]]

![[assets/2608.19794_figure.png|800]]

- **arXiv**: [2608.19794](https://arxiv.org/abs/2608.19794)
- **PDF**: https://arxiv.org/pdf/2608.19794
- **详细分析**: [[20_Research/Papers/具身智能/Towards_general_embodied_intelligence_integrating_large_language_models,_knowledge_bases,_and_reasoning_capabilities_to_build_the_next_gener|Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents]]
- **作者**: Fujiang Yuan, Xia Huang, Lusheng Wang, Jun Ding, Zhen Tian, Yuxin Wang, Shaojie Gu, Yuki Funabora, Yanhong Peng, Zebing Mao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，大模型 0.6，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Towards general embodied intelligence: integrating large language models, knowledge bases, and reasoning capabilities to build the next generation of AI agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The convergence of large language models (LLMs), structured knowledge bases (KBs), and reasoning ability (RA) presents a promising trajectory toward general embodied intelligence (GEI). This paper reviews the evolution of LLM-centered intelligent systems, emphasising their integration with knowledge representation, logical reasoning, and physical embodiment. We analyse LLM architectures, pre-training methods, and inference mechanisms, along with their interaction with external knowledge sources and structured reasoning frameworks. Furthermore, we examine embodied intelligence (EI) paradigms wherein agents learn and act in physical environments. To synthesise these dimensions, we present a conceptual framework that illustrates the synergy among LLMs, KBs, RA, and embodiment, serving as a guiding model for perception, reasoning, and action rather than an implemented engineering architecture. To advance toward GEI, we identify five key challenges: efficient LLM deployment, closed-loop knowledge integration, hybrid symbolic-neural reasoning, perception-action grounding, and continual learning. This survey provides a comprehensive roadmap for developing adaptive, multimodal agents capable of operating in complex, dynamic settings.

</details>

---

### [[20_Research/Papers/强化学习/An_Irreducible_Quantum_Advantage_in_Aligning_World_Models_with_Reality|An Irreducible Quantum Advantage in Aligning World Models with Reality]]

![[assets/2608.19779_figure.png|800]]

- **arXiv**: [2608.19779](https://arxiv.org/abs/2608.19779)
- **PDF**: https://arxiv.org/pdf/2608.19779
- **详细分析**: [[20_Research/Papers/强化学习/An_Irreducible_Quantum_Advantage_in_Aligning_World_Models_with_Reality|An Irreducible Quantum Advantage in Aligning World Models with Reality]]
- **作者**: Josep Lumbreras, Hailan Ma, Jayne Thompson, Mile Gu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《An Irreducible Quantum Advantage in Aligning World Models with Reality》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models provide digital simulacra of the true world, allowing agents to be trained and tested before costly real-world deployment. At each time step, they receive an action and generate an observation and reward matching the statistics of the true world. In complex environments where present outcomes depend on events far in the past, this requires memory. One might expect that, by increasing memory, we can always build a model accurately enough to align the optimal agent policies of the real and virtual worlds. We show that this is false for classical world models, even when the true world itself is classical. We construct true worlds for which every finite classical model fails along the same possible trajectory: it either loses the ability to distinguish actions when the true world clearly prefers one, or repeatedly assigns the highest expected reward to suboptimal actions. Its expected-reward estimates also retain a nonvanishing average error. In contrast, each such true world admits a quantum world model using a single qutrit that reproduces it exactly: its reward estimates and preferred actions always match those of the true world, ensuring that the optimal policies of the real and virtual worlds remain perfectly aligned.

</details>

---

### [[20_Research/Papers/大模型/Distilling_Aggregate_Mobility_Statistics_into_a_Language_Model_Policy_for_Post-Event_Crowd_Simulation|Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation]]

![[assets/2608.19778_figure.png|800]]

- **arXiv**: [2608.19778](https://arxiv.org/abs/2608.19778)
- **PDF**: https://arxiv.org/pdf/2608.19778
- **详细分析**: [[20_Research/Papers/大模型/Distilling_Aggregate_Mobility_Statistics_into_a_Language_Model_Policy_for_Post-Event_Crowd_Simulation|Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation]]
- **作者**: Tatsuya Amano, Hirozumi Yamaguchi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Distilling Aggregate Mobility Statistics into a Language Model Policy for Post-Event Crowd Simulation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pedestrian simulators need a behaviour rule for every agent, but privacy usually limits the data for setting one to aggregate statistics, namely zone-level device counts and origin-to-destination (OD) flows, with no individual trajectories. Such aggregates under-determine individual behaviour, because many different sets of decisions reproduce the same counts. We fine-tune a language model crowd agent so that the simulated population matches the observed destination composition, the fraction of the departing crowd heading to each point of interest. We read this target from the OD flow and reweight the model's own destination distribution onto it by iterative proportional fitting. Because fine-tuning inflates the dominant destination class, we fit the low-rank adapter to trajectories resampled to a corrected training composition that reaches the target after this inflation. On mobile network counts from two baseball games the fine-tuned agent runs without inference-time correction, cutting the destination-share error by 25%, while the grid correlation remains similar across policies.

</details>

---

### [[20_Research/Papers/机器人/CoToGrasp_Contact-Topology-Conditioned_Dexterous_Grasp_Synthesis_via_Canonical_Workspace_Learning|CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning]]

![[assets/2608.19776_figure.png|800]]

- **arXiv**: [2608.19776](https://arxiv.org/abs/2608.19776)
- **PDF**: https://arxiv.org/pdf/2608.19776
- **详细分析**: [[20_Research/Papers/机器人/CoToGrasp_Contact-Topology-Conditioned_Dexterous_Grasp_Synthesis_via_Canonical_Workspace_Learning|CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning]]
- **作者**: Julien Merand, Boris Meden, Liming Chen, Mathieu Grossard
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《CoToGrasp: Contact-Topology-Conditioned Dexterous Grasp Synthesis via Canonical Workspace Learning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DexGraspNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current dexterous grasp planners primarily optimize for physical stability, focusing on whether an object can be grasped rather than how it should be grasped to support downstream functional tasks. However, conditioning grasp synthesis on specific human grasp taxonomies typically requires prohibitively expensive, object-annotated datasets. To address these limitations, we propose CoToGrasp, a novel generative framework that synthesizes diverse, stable grasps strictly conditioned on specific contact topologies. To bypass the data collection bottleneck, CoToGrasp is trained entirely in an object-agnostic manner. We introduce a feature-based canonical workspace that projects local object features into a unified gripper-centric domain, effectively decoupling the semantic functional intent from the arbitrary object geometry. By learning the intrinsic contact manifold of the gripper within this workspace, our model achieves zero-shot generalization to unseen objects at inference. Extensive evaluations on the large-scale DexGraspNet dataset demonstrate that CoToGrasp achieves state-of-the-art performance, outperforming existing taxonomy-guided planners. Finally, we demonstrate the physical viability and kinematic feasibility of our synthesized contact topologies on a physical robot platform. Code is available on our project website https://cea-list.github.io/cotograspweb/ .

</details>

---

### [[20_Research/Papers/大模型/Credit_Without_Ground_Truth_Auditing_Step-Level_Credit_Assignment_in_LLM_Agents_Against_Executed_Replay|Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay]]

![[assets/2608.19760_first_page.png|800]]

- **arXiv**: [2608.19760](https://arxiv.org/abs/2608.19760)
- **PDF**: https://arxiv.org/pdf/2608.19760
- **详细分析**: [[20_Research/Papers/大模型/Credit_Without_Ground_Truth_Auditing_Step-Level_Credit_Assignment_in_LLM_Agents_Against_Executed_Replay|Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay]]
- **作者**: Haiyue Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Credit Without Ground Truth: Auditing Step-Level Credit Assignment in LLM Agents Against Executed Replay》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, CARL, TARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Audited against causal ground truth from executed replay in a single-agent tool environment (ALFWorld), none of the step-level credit signals used to train LLM agents -- LLM-judge scores, outcome-conditioned logprob ratios, or the policy's own confidence -- identifies which steps causally matter better than chance. Existing evaluations grade these signals against annotated step *correctness*; we audit them against step *contribution* -- what re-sampling the policy's own alternatives at each decision point and rolling forward actually changes about the outcome -- and the two come apart. The ground truth itself is structured: causal contribution is sparse (30.5% of decision points where ground truth is defined carry measurable effect), and measurability is model-dependent -- the fraction of points with no policy-supported counterfactual differs by a factor of two (13.1% vs. 26.8%) between two similar-scale policies. The failure mode is identifiable: implicit credit echoes the policy's fluency (median rank correlation +0.75, replicating at +0.70 in a second family under a corrected instrument), while conditioning on the outcome adds no causal information (partial correlation -0.004, Qwen). A confidence-only router recovers pivotal steps at chance level, but cuts judge cost by 13.1% per turn (14.0% per trajectory). In a seven-arm pre-registered training experiment, no arm reliably outperforms the untrained policy, and the checkpoints' apparent instrument signature is fully explained by training dose -- sparser credit retains fewer examples, an order-of-magnitude spread in optimizer steps -- not credit content. Comparisons of credit rules must therefore match effective sample size, or they measure dose, not credit.

</details>

---

### [[20_Research/Papers/具身智能/GOAG_Generative_and_Object-Agnostic_Grasp_Planner_for_Dexterous_Robotic_Manipulation|GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation]]

![[assets/2608.19759_figure.png|800]]

- **arXiv**: [2608.19759](https://arxiv.org/abs/2608.19759)
- **PDF**: https://arxiv.org/pdf/2608.19759
- **详细分析**: [[20_Research/Papers/具身智能/GOAG_Generative_and_Object-Agnostic_Grasp_Planner_for_Dexterous_Robotic_Manipulation|GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation]]
- **作者**: Julien Merand, Boris Meden, Mathieu Grossard, Liming Chen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.1（加权：具身智能 3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multifingered grasping is a crucial robotic skill, but current deep-learning grasp planners often struggle to generalize to new objects because they are trained on limited, object-specific datasets. We introduce a fundamentally different approach, grounded in the observation that the gripper and the object share identical surface geometry at their mutual contact points. We propose GOAG: Generative and Object-Agnostic Grasp Planner for Dexterous Robotic Manipulation, a novel deep generative model that learns a compact latent representation of a specific gripper's contact surface distribution, enabling the efficient sampling of valid grasp configurations without relying on object-specific training data. We show that by introducing object features only at inference time, our model can effectively retrieve admissible contact areas that are compatible with the gripper's capabilities. We validate our approach through extensive experiments on established grasp protocols in both simulated and real-world scenarios, demonstrating its effectiveness with different grippers from the literature. Our method delivers state-of-the-art results on the objects from the MultiDex dataset, achieving an average success rate of 86.93%. It offers significantly faster processing when generating numerous grasps, while matching the performance of leading approaches specifically trained on this dataset. Unlike these methods, our approach does not rely on object-specific training data, highlighting the advantages of object-agnostic learning. It effectively addresses the generalization challenges faced by traditional data-driven grasp planners. Code and videos are available on our project website https://cea-list.github.io/goagweb/ .

</details>

---

### [[20_Research/Papers/强化学习/Truncate_Bad,_Upweight_Good_BoN-Style_Distillation_via_Rank-Based_Classification|Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification]]

![[assets/2608.19748_figure.png|800]]

- **arXiv**: [2608.19748](https://arxiv.org/abs/2608.19748)
- **PDF**: https://arxiv.org/pdf/2608.19748
- **详细分析**: [[20_Research/Papers/强化学习/Truncate_Bad,_Upweight_Good_BoN-Style_Distillation_via_Rank-Based_Classification|Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification]]
- **作者**: Yarin Bar, Yaniv Romano
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Truncate Bad, Upweight Good: BoN-Style Distillation via Rank-Based Classification》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AlpacaEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inference-time selection methods, such as Best-of-N, improve generation by sampling a pool of candidates and selecting the top-ranked completion according to a reward model. Distillation seeks to amortize this procedure into a single policy by replacing raw rewards with in-pool ranks and learning a policy that upweights higher-ranked completions. However, existing rank-based policies typically use smooth full-support reweighting, so low-ranked completions receive less mass but remain in the target support. Although a sharper reweighting reduces lower-tail mass, it also increases reliance on brittle ranking at the top made by a single reward model. We propose TUP: a Truncate-bad, Upweight-good Policy that removes low-ranked completions from the support and reweights only the retained upper tail with a tunable sharpness. TUP admits a closed-form, prompt-independent normalization and can be trained fully offline via binary cross-entropy, using shifted-truncated win-rates as soft labels and distilled-to-reference log-likelihood ratios as logits. Theoretically, under certain assumptions, we show that for any unknown oracle reward, the best monotone rank-reweighting can be matched by a lower-tail truncation rule, providing formal support for removing the lower tail rather than merely downweighting it. Empirically, we show that TUP is competitive with strong offline alignment baselines.

</details>

---

### [[20_Research/Papers/大模型/Question-Guided_Evidence_Acquisition_for_Multimodal_Visual_Question_Answering|Question-Guided Evidence Acquisition for Multimodal Visual Question Answering]]

![[assets/2608.19739_figure.png|800]]

- **arXiv**: [2608.19739](https://arxiv.org/abs/2608.19739)
- **PDF**: https://arxiv.org/pdf/2608.19739
- **详细分析**: [[20_Research/Papers/大模型/Question-Guided_Evidence_Acquisition_for_Multimodal_Visual_Question_Answering|Question-Guided Evidence Acquisition for Multimodal Visual Question Answering]]
- **作者**: Alin-Ionut Popa
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Question-Guided Evidence Acquisition for Multimodal Visual Question Answering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal LLMs can see a document, but they often can't read it reliably. Small text, tables, visual cues, and topological elements still trip them up under direct visual inference, even when the page is already sitting in the model's context. Most document-VQA systems treat perception as fixed: they encode the page once, ask the question, and answer from whatever the model happened to extract in that single fast pass. We think document VQA needs slower, more deliberate perception: rather than answering from one fixed encoding, the model should spend a bit of extra compute at inference time working out what to look at next, and only then answer. We build this into \textbf{Q-Guide}, a small agent that reads a question, works out what evidence it is still missing, and calls targeted tool(s) to recover it---reading text where text is needed, zooming in where detail is needed, or grounding a region where position matters. On DocVQA2026 and Manga109, Q-Guide outperforms both direct prompting and recent multi-agent document systems ($65.0\%$ vs.\ $40.0\%$ on DocVQA2026, $32.4\%$ vs.\ $24.4\%$ on Manga109), and the improvement holds across three Claude backbones (Opus 4.6, Sonnet 4.6, and Opus 4.5). We find that accuracy scales with the perception budget---most of the gain appears within two to three deliberate rounds---and that the gain comes from directing perception to the right place, not from complex control logic: adding planners, routers, or multiple collaborating agents does not help.

</details>

---

### [[20_Research/Papers/具身智能/SafeBranch_Branch-Pair_Safety_Alignment_for_Embodied_Agents|SafeBranch: Branch-Pair Safety Alignment for Embodied Agents]]

![[assets/2608.19729_figure.png|800]]

- **arXiv**: [2608.19729](https://arxiv.org/abs/2608.19729)
- **PDF**: https://arxiv.org/pdf/2608.19729
- **详细分析**: [[20_Research/Papers/具身智能/SafeBranch_Branch-Pair_Safety_Alignment_for_Embodied_Agents|SafeBranch: Branch-Pair Safety Alignment for Embodied Agents]]
- **作者**: Hyunse Lee, Jiwoo Jeong, Haneul Lee, Kyochul Jang, Youngjae Yu, Woojin Lee
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《SafeBranch: Branch-Pair Safety Alignment for Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IS-Bench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-model-based embodied agents can complete instructed tasks but often violate safety constraints in the process, a problem recently framed as interactive safety. Training such agents to act safely is difficult, since safety and task success are distinct objectives, and safety arises only at a small number of safety-critical steps within a trajectory. Standard supervision is insufficient: imitating safe trajectories teaches behavior without explaining why it is safe, and contrasting arbitrary safe and unsafe trajectories mixes the safety signal with unrelated differences. We propose SafeBranch, a framework that aligns an embodied actor on safety through branch pairs constructed from the actor's own unsafe rollouts via environment rollback. SafeBranch rolls each unsafe rollout back to the safety-critical step that caused the violation, queries the actor for a safe alternative, and pairs the original action with the alternative so that the two branches differ only at that step. The trained actor acts safely at deployment with no critic in the loop. On IS-Bench, SafetyALFRED, and out-of-distribution variants with unseen tasks and objects, it handles safety reliably without sacrificing task success, achieving roughly ten times more safe successes than the untrained baseline on the unseen-object variant.

</details>

---

### [[20_Research/Papers/大模型/Robust_Cross-Modal_Foundation_Model_Perception_for_Underwater_Robots_under_Degraded_Visual_Conditions|Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions]]

![[assets/2608.19710_figure.png|800]]

- **arXiv**: [2608.19710](https://arxiv.org/abs/2608.19710)
- **PDF**: https://arxiv.org/pdf/2608.19710
- **详细分析**: [[20_Research/Papers/大模型/Robust_Cross-Modal_Foundation_Model_Perception_for_Underwater_Robots_under_Degraded_Visual_Conditions|Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions]]
- **作者**: Mohammad Arif Ul Alam
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.6（加权：大模型 0.4，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Robust Cross-Modal Foundation Model Perception for Underwater Robots under Degraded Visual Conditions》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable underwater robotic perception remains difficult because optical imagery degrades under turbidity, wavelength-dependent attenuation, low illumination, scattering, and blur. Although sonar provides complementary information that is less affected by optical visibility, prior visual-sonar research has largely focused on feature alignment and nominal detection performance. We investigate cross-modal robustness as visual reliability deteriorates and assess whether pretrained visual foundation-model representations can be complemented by sonar under severe degradation. We use frozen DINOv2 as the visual encoder and construct a controlled five-level benchmark ranging from clean to extreme visual conditions. We compare conventional visual detection, frozen foundation-model representations, sonar context, fixed multimodal fusion, clean-trained adaptive gating, and degradation-aware gated fusion. Our method trains the fusion mechanism across the full range of degradation while keeping the visual and sonar encoders frozen, allowing modality contributions to adapt without fine-tuning the pretrained backbone. Under extreme combined degradation, the DINOv2 baseline achieves 0.4610 balanced accuracy, while degradation-aware visual-sonar fusion reaches 0.6152, a 33.5% relative improvement. The learned sonar contribution increases from 14.2% under clean conditions to 41.3% under extreme degradation, demonstrating adaptive redistribution of cross-modal reliance. Fusion provides the largest gains under severe turbidity and blur, whereas color attenuation alone yields little additional benefit. These results show that foundation-model representations remain valuable but insufficient under severe information loss, and that explicitly adapting fusion to modality reliability can improve robust underwater multimodal perception.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Memory_Majority_Latent-Source_Reasoning_for_Multi-Agent_Memory_Arbitration|Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration]]

![[assets/2608.19701_figure.png|800]]

- **arXiv**: [2608.19701](https://arxiv.org/abs/2608.19701)
- **PDF**: https://arxiv.org/pdf/2608.19701
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Memory_Majority_Latent-Source_Reasoning_for_Multi-Agent_Memory_Arbitration|Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration]]
- **作者**: Chenchen Lin, Wenhao Yuan, Xuehe Wang, Edith Cheuk Han Ngai
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Beyond Memory Majority: Latent-Source Reasoning for Multi-Agent Memory Arbitration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term multi-agent systems continuously accumulate the memories produced by different agents. Existing memory methods typically treat retrieved memories as independent evidence and combine them through voting or weighting. However, this independence assumption often fails in multi-agent settings: memories written by different agents may inherit the same upstream source or shared bias, causing correlated evidence to be repeatedly counted and creating a false majority. We term this failure mode \textit{Memory Correlation Bias}. To address the issue, we propose the \textbf{C}orrelation-\textbf{A}ware \textbf{M}emory \textbf{A}rbitration (CAMA) framework that jointly decouples retrieved memories and recovers missing independent evidence. We model the retrieved memories as query-conditioned evidence groups and combine neural dependency inference with provenance-based symbolic priors to estimate the effective number of independent evidence sources, thereby preventing correlated memories from forming a false majority. Since critical independent evidence may be absent from the initial retrieval set, \textsc{CAMA} further learns a sequential recovery policy that actively retrieves alternative evidence or traces upstream sources before making the final decision, aiming to recover sufficient independent evidence for reliable arbitration while minimizing retrieval cost. Experiments on multiple benchmarks demonstrate the superiority of our method over the state-of-the-art baseline methods, suppressing false majorities induced by correlated memories.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Hierarchical_Skill_Policies_with_Offline_Quality-Diversity_Reinforcement_Learning|Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning]]

![[assets/2608.19684_figure.png|800]]

- **arXiv**: [2608.19684](https://arxiv.org/abs/2608.19684)
- **PDF**: https://arxiv.org/pdf/2608.19684
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Hierarchical_Skill_Policies_with_Offline_Quality-Diversity_Reinforcement_Learning|Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning]]
- **作者**: Tanachai Anakewat, Takayuki Osa, Tatsuya Harada
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 1.82（加权：具身智能 0.6，强化学习 0.76，世界模型 0.16，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Hierarchical Skill Policies with Offline Quality-Diversity Reinforcement Learning》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SPiRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent studies investigate how to leverage pre-collected datasets to improve the policy performance and sample efficiency of RL. One promising approach to achieve this goal is to employ a two-stage strategy: In the first stage, diverse skills are extracted as a low-level policy from a given dataset, and a high-level policy is trained to solve a specific task in the second stage. Typically, extraction of the low-level policy is performed based on unsupervised learning such as trajectory VAE. However, a limitation of this approach is that the quality of the low-level policy highly depends on the quality of the dataset. To address this issue, we introduce QDOS (Quality-Diversity Offline Skill learning), a unified pipeline for robust offline-to-online learning. Our approach incorporates an Advantage-Weighted Quality-Diversity pretraining objective, which weights the skill extraction and diversity objectives by the estimated advantage of each trajectory segment. This approach allows the model to extract diverse and high-value skills. By providing robust and task-relevant skill representations, QDOS significantly improves the quality of the embedded skill space used by the low-level policy. We further integrate this with a dual dataset reuse strategy, where offline data is used both for skill pretraining and for populating the online replay buffer via pseudo-labeling. Experiments demonstrate that QDOS significantly outperforms strong baselines in structured manipulation tasks and unstructured locomotion tasks, confirming its ability to accelerate exploration and improve final returns in challenging sparse-reward domains.

</details>

---

### [[20_Research/Papers/大模型/DeltaML-Bench_Evaluating_Machine_Learning_Agents_on_Real-World_Research_Repositories|DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories]]

![[assets/2608.19653_figure.png|800]]

- **arXiv**: [2608.19653](https://arxiv.org/abs/2608.19653)
- **PDF**: https://arxiv.org/pdf/2608.19653
- **详细分析**: [[20_Research/Papers/大模型/DeltaML-Bench_Evaluating_Machine_Learning_Agents_on_Real-World_Research_Repositories|DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories]]
- **作者**: Josias Moukpe, Priyanka Aryal, Matthew Kenney
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《DeltaML-Bench: Evaluating Machine Learning Agents on Real-World Research Repositories》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CTRL, DSBench, DeltaML-Bench, ML-Bench, MLAgentBench, NewtonBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous agents for machine learning experimentation must navigate heterogeneous repositories, repair training pipelines, and evaluate candidate improvements under realistic compute constraints. Existing benchmarks only partially capture these conditions. We introduce DeltaML-Bench, a benchmark comprising 48 tasks sourced from research papers that require agents to improve published baselines within imperfect, open-source repositories. We evaluate GPT-5 and Claude Sonnet 4 with a standard Modular agent and a search-based ARG scaffolding. In the 4 x 6h allocation, ARG raises GPT-5's per-run success rate from 9.4% to 33.9%; in the 2 x 12h allocation, GPT-5 ARG reaches 49.0%. Modular configurations exhibit specification gaming rates as high as 47.9%, while no gaming is observed in the evaluated ARG configurations. These results indicate that scaffolding design and integrity checks are important considerations when deploying agents for autonomous ML experimentation.

</details>

---

### [[20_Research/Papers/大模型/Can_Agent_Memory_Systems_Track_Evolving_State|Can Agent Memory Systems Track Evolving State?]]

![[assets/2608.19652_figure.png|800]]

- **arXiv**: [2608.19652](https://arxiv.org/abs/2608.19652)
- **PDF**: https://arxiv.org/pdf/2608.19652
- **详细分析**: [[20_Research/Papers/大模型/Can_Agent_Memory_Systems_Track_Evolving_State|Can Agent Memory Systems Track Evolving State?]]
- **作者**: Xinyi Fan, Miri Liu, Ruozhen Yang, Siru Ouyang, Jiawei Han
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Can Agent Memory Systems Track Evolving State?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench, STATE-Bench, StateMemBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As LLM-based agents are deployed for longer and higher-stakes tasks, their memory systems continue to have crucial gaps. While existing memory benchmarks focus largely on recall-shaped tasks, we argue an effective memory system must track the evolving state of the world; as facts, constraints, and decisions are revised over a long interaction, answers must reflect the current state and not a superseded one. We define this capability as state tracking and instantiate it in StateMemBench, a benchmark of 234 multi-session scenarios spanning two conversation-length regimes. Its closed-pool grading scores whether an answer reflects the current state, the superseded state, or fails otherwise, separating state-tracking failures from other errors by construction. Our analysis shows that this task is challenging for existing memory systems, retrieval-augmented baselines, and long-context baselines. We then present StateMem, a state-first memory method that explicitly tracks supersession and relational dependencies, and show it improves current-state accuracy over the strongest same-backbone baseline by 1.8x (0.205 -&gt; 0.363) on DeepSeek-V4-Flash and over the strongest memory system by 1.6x (0.149 -&gt; 0.233) on Qwen-3.5-9B, while remaining competitive with the long-context baselines. Finally, we show the same state approach can be applied as a lightweight single-call wrapper over existing memory systems, lifting current-state accuracy by +32 to +67 points on StateMemBench across six memory and retrieval backends. A length- and cost-matched control attributes +15 to +32 of those points to state structure rather than added context.

</details>

---

### [[20_Research/Papers/其他/Scientific_Data_Skills_Enabling_Agent-Ready_Scientific_Data_Services_at_Scale|Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale]]

![[assets/2608.19625_figure.png|800]]

- **arXiv**: [2608.19625](https://arxiv.org/abs/2608.19625)
- **PDF**: https://arxiv.org/pdf/2608.19625
- **详细分析**: [[20_Research/Papers/其他/Scientific_Data_Skills_Enabling_Agent-Ready_Scientific_Data_Services_at_Scale|Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale]]
- **作者**: Xiaohan Huang, Qingqing Long, Xiaolei Du, Siyu Pu, Jiawen Xu, Haotian Chen, Chenyang Zhao, Jinbiao Liu, Xuezhi Wang, Hao Wang, Hengshu Zhu, Yuanchun Zhou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Scientific Data Skills: Enabling Agent-Ready Scientific Data Services at Scale》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific data are increasingly used by AI agents, yet existing dataset representations provide limited support for autonomous discovery, interpretation, and invocation. This limitation stems from the fragmentation of scientific data across heterogeneous repositories and from dataset representations designed primarily for human use. To address this limitation, we introduce the Scientific Data Skill (SciDSK), an agent-ready representation that packages dataset-specific knowledge and operational guidance as a reusable agent skill. A SciDSK integrates dataset descriptions, scientific context, file organization, usage procedures, quality checks, and provenance information while retaining the underlying data in its original repository. We define a structured SciDSK specification and develop a systematic construction pipeline that grounds each SciDSK in authoritative dataset records and associated supporting materials. We further establish the Scientific Data Skill Bank, a unified platform that publishes SciDSK resources across six scientific disciplines and supports package access, persistent identification, and traceability to source datasets. We evaluate SciDSK through a retrieval benchmark for dataset discovery and controlled cases for dataset interpretation. The results show that SciDSK improves agent-driven dataset discovery and provides more precise and actionable support for dataset interpretation. These findings support the value of organizing dataset-specific knowledge in an agent-ready representation.

</details>

---

### [[20_Research/Papers/大模型/From_Retrieved_Context_to_Runtime_Control_Adaptive_Compression_for_Edge-based_RAG|From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG]]

![[assets/2608.19535_figure.png|800]]

- **arXiv**: [2608.19535](https://arxiv.org/abs/2608.19535)
- **PDF**: https://arxiv.org/pdf/2608.19535
- **详细分析**: [[20_Research/Papers/大模型/From_Retrieved_Context_to_Runtime_Control_Adaptive_Compression_for_Edge-based_RAG|From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG]]
- **作者**: Zlatan Feric, Amir Taherin, Yanzhi Wang, David Kaeli
- **cs 子类**: cs.AI, cs.CL, cs.DC, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Systems

#### 研究背景与动机

《From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) improves language-model responses by grounding generation in external passages, which comes with overhead: retrieved context lengthens the prompt, increasing prefill work, KV-cache footprint, memory traffic, latency, and energy. Context compression offers a natural remedy by pruning retrieved text before generation. However, state-of-the-art context-compression methods are typically used with a fixed compression budget, or with the rate selected offline and then applied at inference time. This static view ignores both workload variation and the live state of the edge device. On an edge SoC, compression is not free: the compressor itself runs on the same SoC and consumes latency and energy that can offset any generation savings. This paper proposes a vision for telemetry-informed adaptive compression in edge RAG, grounded in experimental evidence. We characterize the compression tradeoff on the NVIDIA Jetson AGX Thor using Llama and Qwen generators, Natural Questions and HotpotQA datasets, and LLMLingua-2 compression. Our measurements show that generation dominates the RAG budget for larger models, reaching roughly 90% of per-query latency and 91% of GPU energy for 7B-8B generators. Exploring the impact of the compression rate reveals an adaptive operating region: mild compression can miss energy opportunities, and overly aggressive compression can hurt inference quality. Intermediate compression can reduce GPU energy by up to 53.2%, and SoC energy by up to 48.2%, with negligible quality loss. We argue for runtime policies that dynamically manage compression, guided by workload features and edge telemetry.

</details>

---

### [[20_Research/Papers/大模型/Automated_Summarization_of_Financial_News_Using_Large_Language_Models_and_Retrieval-Augmented_Generation_An_Early_Empirical_Study_(Fall_2023|Automated Summarization of Financial News Using Large Language Models and Retrieval-Augmented Generation: An Early Empirical Study (Fall 2023)]]

![[assets/2608.19526_first_page.png|800]]

- **arXiv**: [2608.19526](https://arxiv.org/abs/2608.19526)
- **PDF**: https://arxiv.org/pdf/2608.19526
- **详细分析**: [[20_Research/Papers/大模型/Automated_Summarization_of_Financial_News_Using_Large_Language_Models_and_Retrieval-Augmented_Generation_An_Early_Empirical_Study_(Fall_2023|Automated Summarization of Financial News Using Large Language Models and Retrieval-Augmented Generation: An Early Empirical Study (Fall 2023)]]
- **作者**: Pranav Chandaliya
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Automated Summarization of Financial News Using Large Language Models and Retrieval-Augmented Generation: An Early Empirical Study (Fall 2023)》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stock market analysts and investors face a daily challenge: too much financial news, too little time. Manually reading and synthesizing hundreds of company-specific articles is impractical, yet missing key information can directly affect investment decisions. This project, conducted at George Washington University in Fall 2023, explores whether Large Language Models can automate this process reliably. We built a pipeline that pulls news articles from the News API, company background from Wikipedia, and stock price data from Yahoo Finance for ten major companies (AAPL, MSFT, GOOGL, AMZN, META, TSLA, JPM, NVDA, WMT, DIS). Because LLMs cannot directly process numerical tables, we developed a simple but effective template that converts stock data into natural language narratives. We then tested two summarization approaches (Summarize Chains and Retrieval-Augmented Generation with FAISS) across three open-source models (Falcon-7B-Instruct, DistilBART-CNN-12-6, BART-Large-XSum) for news, and GPT (text-davinci-003) for stock summaries. Falcon-7B with Summarize Chains gave the best results, covering all news events accurately and coherently. RAG, while promising in theory, caused severe repetition in Falcon and hallucinated facts in BART-Large when k was large. Both LLM-based approaches outperformed a simple Lead-3 baseline on ROUGE-1. We also built a Streamlit dashboard for interactive stock visualization. The work was done in Fall 2023, before RAG-based financial tools became widespread, and the failure modes we document, particularly hallucination under RAG in smaller models, remain relevant today.

</details>

---

### [[20_Research/Papers/强化学习/SCAPE_Scenario-Conditioned_Simulation-Augmented_Policy_Evaluation|SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation]]

![[assets/2608.19425_figure.png|800]]

- **arXiv**: [2608.19425](https://arxiv.org/abs/2608.19425)
- **PDF**: https://arxiv.org/pdf/2608.19425
- **详细分析**: [[20_Research/Papers/强化学习/SCAPE_Scenario-Conditioned_Simulation-Augmented_Policy_Evaluation|SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation]]
- **作者**: Dijie Zhu, Seunghun Oh, Ruopeng Huang, Zhiyu Huang, Jiaqi Ma, Chen Tang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SCAPE: Scenario-Conditioned Simulation-Augmented Policy Evaluation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IsaacGym, SureSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable performance evaluation is a central bottleneck for deploying robot-learning policies in real-world conditions. Real-world testing is faithful but costly and difficult to scale, whereas simulation-based testing scales easily but is inevitably biased by the sim-to-real gap. Existing simulation-augmented methods combine limited real-world rollouts with abundant simulation proxies, but focus on performance averaged over initial conditions and deployment settings. Such population-level averages obscure scenario-specific variation and provide limited guidance about when and where a policy can be safely deployed. We propose SCAPE, a scenario-conditioned simulation-augmented policy evaluation framework that predicts scenario-conditioned real-world policy performance using limited paired sim-and-real samples and large-scale simulation rollouts. SCAPE corrects sim-to-real bias in simulation labels before training the prediction model and calibrates prediction uncertainty through conformal prediction. We validate SCAPE on autonomous driving and quadruped velocity tracking. In sim-to-sim studies, SCAPE reduces scenario-level prediction error by 4.9%/34.7% (driving) and 14.5%/27.7% (quadruped) relative to scene-conditioned neural and aggregate statistical baselines on average. We further evaluate a velocity-tracking policy deployed on a physical Unitree Go2. SCAPE also improves testing sample efficiency, produces narrower calibrated prediction intervals, generalizes better to out-of-distribution scenarios, and enables fine-grained deployment strategies.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Imitation_Filtering_On-Policy_Distillation_by_Reasoning_Progress|Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress]]

![[assets/2608.19408_figure.png|800]]

- **arXiv**: [2608.19408](https://arxiv.org/abs/2608.19408)
- **PDF**: https://arxiv.org/pdf/2608.19408
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Imitation_Filtering_On-Policy_Distillation_by_Reasoning_Progress|Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress]]
- **作者**: Chen Yang, Haiyuan Wan, Rengrong Xiong, Yize Chen, Danny H. K. Tsang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Beyond Imitation: Filtering On-Policy Distillation by Reasoning Progress》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy distillation (OPD) has emerged as an effective framework for post-training language models by pairing student-generated trajectories with dense token-level supervision from a teacher. However, OPD implicitly assumes that teacher-derived rewards are an appropriate proxy for reasoning progress, and therefore treats all teacher feedback equally during policy optimization. While in practice, this assumption does not always hold. We observe that teacher-derived rewards often conflict with genuine reasoning progress, as reasoning steps with clear reasoning advancement may still receive lower distillation rewards, simply due to deviation from teacher's outputs. To address this mismatch, we propose Reasoning-Progress-Aware Reward Filtering for On-Policy Distillation (R2-OPD), which constructs two within-trajectory rankings of reasoning spans, one from teacher-derived rewards and the other from independently estimated progress reward. Distillation rewards are selectively suppressed whenever the two rankings disagree, reducing supervision that conflicts with reasoning progress while preserving effective teacher guidance. Our approach shows consistent improvement over standard OPD especially regarding reasoning performances.

</details>

---

### [[20_Research/Papers/强化学习/Concentrated_Liquidity_Provision_a_Reinforcement_Learning_Perspective|Concentrated Liquidity Provision: a Reinforcement Learning Perspective]]

![[assets/2608.19389_figure.png|800]]

- **arXiv**: [2608.19389](https://arxiv.org/abs/2608.19389)
- **PDF**: https://arxiv.org/pdf/2608.19389
- **详细分析**: [[20_Research/Papers/强化学习/Concentrated_Liquidity_Provision_a_Reinforcement_Learning_Perspective|Concentrated Liquidity Provision: a Reinforcement Learning Perspective]]
- **作者**: Georgios Chionas, Charalampos Kleitsikas, Stefanos Leonardos, Leandro Sánchez-Betancourt, Carmine Ventre
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Concentrated Liquidity Provision: a Reinforcement Learning Perspective》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated market makers (AMMs) are a cornerstone of decentralised finance (DeFi). Constant product markets with concentrated liquidity, such as UniswapV3, are now a well-established design. In these markets, liquidity providers (LPs) face a sequential decision problem: they must decide when to rebalance their positions and which price ranges to allocate capital to as market conditions evolve. We formulate dynamic liquidity provision as a stochastic impulse control problem and use reinforcement learning (RL) to solve it, focusing on providing interpretable solutions. We show that learned policies exhibit rich state-dependent behaviour, allocating liquidity according to mispricing, rebalancing costs, uncertainty, inventory exposure, and heterogeneous risk preferences. These behaviours help compress the left tail of the Profit and Loss (PnL) distribution and avoid catastrophic outcomes under high uncertainty. Finally, we benchmark the RL agents against baseline and sophisticated agents from the AMM microstructure literature and analyse their performance.

</details>

---

### [[20_Research/Papers/大模型/Time-Series_Retrieval_for_Grounding_Multimodal_Language_Models_in_Remaining_Useful_Life|Time-Series Retrieval for Grounding Multimodal Language Models in Remaining Useful Life]]

![[assets/2608.19218_figure.png|800]]

- **arXiv**: [2608.19218](https://arxiv.org/abs/2608.19218)
- **PDF**: https://arxiv.org/pdf/2608.19218
- **详细分析**: [[20_Research/Papers/大模型/Time-Series_Retrieval_for_Grounding_Multimodal_Language_Models_in_Remaining_Useful_Life|Time-Series Retrieval for Grounding Multimodal Language Models in Remaining Useful Life]]
- **作者**: Valeriu Dimidov, Raphaël Frank
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Time-Series Retrieval for Grounding Multimodal Language Models in Remaining Useful Life》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) and agentic AI systems are increasingly being explored for domain-specific maintenance and prognostics tasks, raising the question of whether they can effectively support prognostics and health management (PHM). In this paper, we investigate remaining useful life (RUL) estimation with multimodal large language models (MLLMs) grounded through time-series retrieval. We propose a framework in which historically similar degradation segments are retrieved from the training set and, together with the test trajectory, transformed into a visual comparison artifact that is processed by the MLLM through a structured multimodal prompt. The approach is evaluated on the FD001 partition of the C-MAPSS benchmark under repeated experiments comparing retrieval-based inference against a non-retrieval baseline based on random reference selection. The results show that time-series retrieval consistently improves MLLM-based RUL prediction across the evaluated models, yielding lower error and more stable performance. At the same time, the magnitude of the benefit depends on model capacity, indicating that retrieval is most effective when the underlying MLLM is able to exploit the retrieved evidence. Overall, the study shows that time-series RAG is a promising mechanism for improving multimodal prognostic reasoning, while also highlighting the current limitations of MLLM-based RUL estimation in practical PHM settings.

</details>

---

### [[20_Research/Papers/大模型/Hallucination_as_a_Feature,_not_a_Defect_Evaluating_a_multi-agent_architecture_to_transform_speculative_language-model_outputs_into_testable|Hallucination as a Feature, not a Defect: Evaluating a multi-agent architecture to transform speculative language-model outputs into testable scientific hypotheses]]

![[assets/2608.19206_figure.png|800]]

- **arXiv**: [2608.19206](https://arxiv.org/abs/2608.19206)
- **PDF**: https://arxiv.org/pdf/2608.19206
- **详细分析**: [[20_Research/Papers/大模型/Hallucination_as_a_Feature,_not_a_Defect_Evaluating_a_multi-agent_architecture_to_transform_speculative_language-model_outputs_into_testable|Hallucination as a Feature, not a Defect: Evaluating a multi-agent architecture to transform speculative language-model outputs into testable scientific hypotheses]]
- **作者**: Nicolas Rodriguez-Alvarez
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Hallucination as a Feature, not a Defect: Evaluating a multi-agent architecture to transform speculative language-model outputs into testable scientific hypotheses》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LiveIdeaBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contemporary Large Language Models (LLMs) are increasingly aligned to suppress hallucinations, prioritizing factual retrieval over combinatorial creativity. While crucial for mitigating misinformation, this alignment may also restrict speculative Research and Development (R&amp;D) by encouraging what this work operationally treats as semantic overfitting and diversity collapse. In this paper, we propose a Rust-based multi-agent orchestration that uses the contrast between narrative daydreaming and executive control as a functional analogy, not as a neurocognitive claim. The system instigates an Epistemological Friction loop between a high-entropy generating agent and a web-grounded evaluating agent, mediated by a low-entropy semantic bottleneck intended to reduce noise and repetition. Initial experiments generated diverse, viability-rated hypotheses across physical and social-science domains. We additionally report an exploratory paired baseline and ablation study comparing the full system against direct prompting, self-reflection, removal of the semantic filter, removal of search grounding, and removal of lateral lenses. The results place direct prompting among the weakest conditions across most observed metrics, but they do not show a general superiority of the full system over simple self-reflection. Instead, they suggest that each architecture shifts the balance between originality, feasibility, diversity, and empirical grounding in different ways, and that the full system provides its main advantages when hypotheses must survive strong physical, empirical, or institutional constraints. These findings do not show that hallucination is useful in isolation; they suggest that speculative generation gains value only when constrained by architecture, empirical grounding, and explicit evaluation.

</details>

---

### [[20_Research/Papers/大模型/Active_Inference_as_Context_Acquisition_for_AI_Agents|Active Inference as Context Acquisition for AI Agents]]

![[assets/2608.19202_figure.png|800]]

- **arXiv**: [2608.19202](https://arxiv.org/abs/2608.19202)
- **PDF**: https://arxiv.org/pdf/2608.19202
- **详细分析**: [[20_Research/Papers/大模型/Active_Inference_as_Context_Acquisition_for_AI_Agents|Active Inference as Context Acquisition for AI Agents]]
- **作者**: Sanchayan Dutta, Sai Niranjan Ramachandran, Suvrit Sra
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Active Inference as Context Acquisition for AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive AI agents must acquire the right context as efficiently as possible. When a user omits a constraint, preference, file, or task variable, an agent can proceed with a default assumption or spend tokens on a clarifying question, retrieval call, tool call, or prompt trial. We formulate this tradeoff as active inference for context acquisition. An inner inference step updates beliefs over a latent task state, and an outer decision selects the next context action, task action, or stop action to minimize expected free energy under cost. In deterministic settings, the epistemic term reduces to expected information gain, optionally normalized by token cost. We instantiate the framework in Optimal Question Asking (OQA), with exact posteriors and a dynamic programming oracle, and benchmark frontier language models on binary and multiway categorical tasks from 25 to 300 candidates. We also study clarification before generation and automated prompt optimization under token budgets. The formulation is model-agnostic and views active inference as a design principle for the context-acquisition layer of AI agents.

</details>

---
