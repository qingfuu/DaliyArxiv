# cs.AI | Artificial Intelligence | 2026-05-22

#arxiv #ComputerScience

**论文数**: 45

### [[20_Research/Papers/大模型/Vector_Policy_Optimization_Training_for_Diversity_Improves_Test-Time_Search|Vector Policy Optimization: Training for Diversity Improves Test-Time Search]]

![[assets/2605.22817_figure.png|800]]

- **arXiv**: [2605.22817](https://arxiv.org/abs/2605.22817)
- **PDF**: https://arxiv.org/pdf/2605.22817
- **详细分析**: [[20_Research/Papers/大模型/Vector_Policy_Optimization_Training_for_Diversity_Improves_Test-Time_Search|Vector Policy Optimization: Training for Diversity Improves Test-Time Search]]
- **作者**: Ryan Bahlous-Boldi, Isha Puri, Idan Shenfeld, Akarsh Kumar, Mehul Damani, Sebastian Risi, Omar Khattab, Zhang-Wei Hong, Pulkit Agrawal
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.25，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Vector Policy Optimization: Training for Diversity Improves Test-Time Search》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EUREQA, LiveCodeBench, ToolRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language models must now generalize out of the box to novel environments and work inside inference-scaling search procedures, such as AlphaEvolve, that select rollouts with a variety of task-specific reward functions. Unfortunately, the standard paradigm of LLM post-training optimizes a pre-specified scalar reward, often leading current LLMs to produce low-entropy response distributions and thus to struggle at displaying the diversity that inference-time search will require. We propose Vector Policy Optimization (VPO), an RL algorithm that explicitly trains policies to anticipate diverse downstream reward functions and to produce diverse solutions. VPO exploits that rewards are often vector-valued in practice, like per-test-case correctness in code generation or, say, multiple different user personas or reward models. VPO is essentially a drop-in replacement for the GRPO advantage estimator, but it trains the LLM to output a set of solutions where individual solutions specialize to different trade-offs in the vector reward space. Across four tasks, VPO matches or beats the strongest scalar RL baselines on test-time search (e.g. pass@k and best@k), with the gap widening as the search budget grows. For evolutionary search, VPO models unlock problems that GRPO models cannot solve at all. As test-time search becomes more standardized, optimizing for diversity may need to become the default post-training objective.

</details>

---

### [[20_Research/Papers/大模型/LCGuard_Latent_Communication_Guard_for_Safe_KV_Sharing_in_Multi-Agent_Systems|LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems]]

![[assets/2605.22786_figure.png|800]]

- **arXiv**: [2605.22786](https://arxiv.org/abs/2605.22786)
- **PDF**: https://arxiv.org/pdf/2605.22786
- **详细分析**: [[20_Research/Papers/大模型/LCGuard_Latent_Communication_Guard_for_Safe_KV_Sharing_in_Multi-Agent_Systems|LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems]]
- **作者**: Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Prasanna Sattigeri, Karthikeyan Natesan Ramamurthy
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based multi-agent systems increasingly rely on intermediate communication to coordinate complex tasks. While most existing systems communicate through natural language, recent work shows that latent communication, particularly through transformer key-value (KV) caches, can improve efficiency and preserve richer task-relevant information. However, KV caches also encode contextual inputs, intermediate reasoning states, and agent-specific information, creating an opaque channel through which sensitive content may propagate across agents without explicit textual disclosure. To address this, we introduce \textbf{LCGuard} (Latent Communication Guard), a framework for safe KV-based latent communication in multi-agent LLM systems. LCGuard treats shared KV caches as latent working memory and learns representation-level transformations before cache artifacts are transmitted across agents. We formalize representation-level sensitive information leakage operationally through reconstruction: a shared cache artifact is unsafe if an adversarial decoder can recover agent-specific sensitive inputs from it. This leads to an adversarial training formulation in which the adversary learns to reconstruct sensitive inputs, while LCGuard learns transformations that preserve task-relevant semantics and reduce reconstructable information. Empirical evaluations across multiple model families and multi-agent benchmarks show that LCGuard consistently reduces reconstruction-based leakage and attack success rates while maintaining competitive task performance compared to standard KV-sharing baselines.

</details>

---

### [[20_Research/Papers/大模型/DeltaBox_Scaling_Stateful_AI_Agents_with_Millisecond-Level_Sandbox_Checkpoint_Rollback|DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback]]

![[assets/2605.22781_figure.png|800]]

- **arXiv**: [2605.22781](https://arxiv.org/abs/2605.22781)
- **PDF**: https://arxiv.org/pdf/2605.22781
- **详细分析**: [[20_Research/Papers/大模型/DeltaBox_Scaling_Stateful_AI_Agents_with_Millisecond-Level_Sandbox_Checkpoint_Rollback|DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback]]
- **作者**: Yunpeng Dong, Jingkai He, Yuze Hou, Dong Du, Zhonghu Xu, Si Yu, Yubin Xia, Haibo Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《DeltaBox: Scaling Stateful AI Agents with Millisecond-Level Sandbox Checkpoint/Rollback》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, HotPotQA, OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-powered AI agents require high-frequency state exploration (e.g., test-time tree search and reinforcement learning), relying on rapid checkpoint and rollback (C/R) of the complete sandbox state, including files and process state (e.g., memory, contexts, etc.). Existing mechanisms duplicate the entire state, causing hundreds of milliseconds to seconds of latency per C/R, which severely bottlenecks deep search and large-scale fan-outs. This paper observes that subsequent checkpoints in AI agents are highly similar. Therefore, instead of full duplication, a sandbox should only duplicate the changes between consecutive checkpoints (Key Insight). However, it is non-trivial to realize the idea, mainly due to the missing OS supports. This paper proposes a new OS-level abstraction, DeltaState, to enable the change-based transactional C/R for AI agents with two co-designed OS mechanisms. First, DeltaFS enables change-based filesystem C/R by organizing the file states into layers and dynamically freezing the writable layer and inserting a new one during checkpoint, reducing file updates to copy-on-write, and making rollback a simple layer switch. Second, DeltaCR enables change-based process state C/R using incremental dumps, and accelerates rollback by bypassing traditional pipelines to directly fork() from a frozen template process. We then present DeltaBox, a novel agent sandbox achieving millisecond level C/R through the two new mechanisms. Evaluations on SWE-bench and RL micro-benchmarks show DeltaBox completes checkpoint and rollback in millisecond-level latency (14ms and 5ms, respectively), empowering agents to explore substantially more nodes under fixed time budgets.

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Flexible_Job_Shop_Scheduling_with_Random_Job_Arrivals|Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals]]

![[assets/2605.22773_figure.png|800]]

- **arXiv**: [2605.22773](https://arxiv.org/abs/2605.22773)
- **PDF**: https://arxiv.org/pdf/2605.22773
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Flexible_Job_Shop_Scheduling_with_Random_Job_Arrivals|Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals]]
- **作者**: Yu Tang, Muhammad Zakwan, Efe Balta, John Lygeros, Alisa Rupenyan
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.1，强化学习 1.4）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Deep Reinforcement Learning for Flexible Job Shop Scheduling with Random Job Arrivals》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Flexible Job Shop Scheduling Problem (FJSP) is the optimal allocation of a set of jobs to machines. Two primary challenges persist in FJSP: the unpredictable arrival of future jobs and the combinatorial complexity of the problem, rendering it intractable for conventional mixed-integer linear programming solvers. This paper proposes an event-based \gls{DRL} approach to solve FJSP with random job arrivals. Specifically, we employ the Proximal Policy Optimization algorithm and use lightweight Multi-Layer Perceptrons to train the \gls{DRL} agent for minimizing the total completion time of all jobs. We design the state representation to be directly accessible from the environment, and limit the learning agent to selecting from among a set of well-established dispatching rules. Simulations show that our \gls{DRL} approach outperforms any of the individual dispatching rules on datasets with varying heterogeneity and job arrival rates. We benchmark our \gls{DRL} against an arrival-triggered mixed-integer linear programming solution and show that our method achieves good performance especially when the datasets are heterogeneous.

</details>

---

### [[20_Research/Papers/强化学习/Superhuman_Safe_and_Agile_Racing_through_Multi-Agent_Reinforcement_Learning|Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning]]

![[assets/2605.22748_figure.png|800]]

- **arXiv**: [2605.22748](https://arxiv.org/abs/2605.22748)
- **PDF**: https://arxiv.org/pdf/2605.22748
- **详细分析**: [[20_Research/Papers/强化学习/Superhuman_Safe_and_Agile_Racing_through_Multi-Agent_Reinforcement_Learning|Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning]]
- **作者**: Ismail Geles, Leonard Bauersfeld, Markus Wulfmeier, Davide Scaramuzza
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人, 具身智能, 世界模型
- **相关性评分**: 2.42（加权：具身智能 0.3，大模型 0.5，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Superhuman Safe and Agile Racing through Multi-Agent Reinforcement Learning》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems have achieved superhuman performance in isolation or simulation, yet they remain brittle in shared, dynamic real-world spaces. This failure stems from the dominant single-agent paradigm for physical applications, where other actors are ignored or treated as environmental noise, preventing effective coordination. Here we show that multi-agent reinforcement learning provides the essential safety scaffolding required for real-world interaction. Using high-speed quadrotor racing as a high-stakes testbed, we train agents to navigate complex aerodynamic interactions and strategic maneuvering with a variable number of racers. Through league-based self-play, agents evolve sophisticated anticipatory behaviors, including proactive collision avoidance, overtaking, and handling multi-agent physical interactions, including aerodynamic downwash. Our agents outperform a champion-level human pilot in multi-player races at speeds exceeding 22 m/s, while simultaneously reducing collision rates by 50 % compared to state-of-the-art single-agent baselines. Crucially, training with diverse artificial agents enables zero-shot generalization to safer human interaction. These results suggest that the path to robust robotic co-existence lies not in isolated safety constraints, but in the rigorous demands of multi-agent interaction. Multimedia materials are available at: https://rpg.ifi.uzh.ch/marl

</details>

---

### [[20_Research/Papers/大模型/Beyond_Acoustic_Emotion_Recognition_Multimodal_Pathos_Analysis_in_Political_Speech_Using_LLM-Based_and_Acoustic_Emotion_Models|Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models]]

![[assets/2605.22732_first_page.png|800]]

- **arXiv**: [2605.22732](https://arxiv.org/abs/2605.22732)
- **PDF**: https://arxiv.org/pdf/2605.22732
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Acoustic_Emotion_Recognition_Multimodal_Pathos_Analysis_in_Political_Speech_Using_LLM-Based_and_Acoustic_Emotion_Models|Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models]]
- **作者**: Juergen Dietrich
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Beyond Acoustic Emotion Recognition: Multimodal Pathos Analysis in Political Speech Using LLM-Based and Acoustic Emotion Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate whether acoustic emotion recognition models can serve as proxies for the Pathos dimension in political speech analysis, as operationalised by the TRUST multi-agent large language model (LLM) pipeline. Using a Bundestag plenary speech by Felix Banaszak (51 segments, 245 s) as a case study, we compare three analysis modalities: (1) emotion2vec_plus_large, an acoustic speech emotion recognition (SER) model whose continuous Arousal and Valence values are derived via post-hoc Russell Circumplex projection; (2) Gemini 2.5 Flash, an LLM analysing the full speech audio together with its transcript in an open-ended, context-aware fashion; and (3) TRUST-Pathos scores from a three-advocate LLM supervisor ensemble. Spearman rank correlations reveal that Gemini Valence correlates strongly with TRUST-Pathos (rho = +0.664, p &lt; 0.001), whereas emotion2vec Valence does not (rho = +0.097, p = 0.499). We further demonstrate, via a systematic quality evaluation of the Berlin Database of Emotional Speech (EMO-DB) using Gemini in an open-ended annotation paradigm, that standard SER benchmark corpora suffer from acted speech, cultural bias, and category incompatibility. Our results suggest that LLM-based multimodal analysis captures semantically defined political emotion substantially better than acoustic models alone, while acoustic features remain informative for low-level Arousal estimation. Future work will extend this approach to video-based analysis incorporating facial expression and gaze.

</details>

---

### [[20_Research/Papers/大模型/Post-Training_is_About_States,_Not_Tokens_A_State_Distribution_View_of_SFT,_RL,_and_On-Policy_Distillation|Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation]]

![[assets/2605.22731_first_page.png|800]]

- **arXiv**: [2605.22731](https://arxiv.org/abs/2605.22731)
- **PDF**: https://arxiv.org/pdf/2605.22731
- **详细分析**: [[20_Research/Papers/大模型/Post-Training_is_About_States,_Not_Tokens_A_State_Distribution_View_of_SFT,_RL,_and_On-Policy_Distillation|Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation]]
- **作者**: Dong Nie
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Post-Training is About States, Not Tokens: A State Distribution View of SFT, RL, and On-Policy Distillation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TruthfulQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model post-training methods such as supervised fine-tuning (SFT), reinforcement learning (RL), and distillation are often analyzed through their loss functions: maximum likelihood, policy gradients, forward KL, reverse KL, or related objective-level variants. We study a complementary factor: the state distribution on which supervision is applied. For an autoregressive policy, a state is a prompt plus generated prefix. SFT trains on fixed dataset states, while RL and on-policy distillation (OPD) train on states induced by the current learner. We formalize post-training as state-distribution shaping and run a controlled smallscale study using Qwen3-0.6B-Base on GSM8K, with TruthfulQA and MMLU as retention evaluations. Our results show three phenomena. First, a mild SFT run improves GSM8K with little forgetting, while a stress SFT run causes substantial retention loss. Second, OPD from a degraded SFT teacher surpasses that teacher on GSM8K, TruthfulQA, and MMLU, despite using the teacher as its only supervision source. Third, a lightweight on-policy RL run improves GSM8K while preserving retention. These results support a state-centric view of post-training: the source and locality of training states can be as important as the form of the supervision signal.

</details>

---

### [[20_Research/Papers/强化学习/Abstraction_for_Offline_Goal-Conditioned_Reinforcement_Learning|Abstraction for Offline Goal-Conditioned Reinforcement Learning]]

![[assets/2605.22711_figure.png|800]]

- **arXiv**: [2605.22711](https://arxiv.org/abs/2605.22711)
- **PDF**: https://arxiv.org/pdf/2605.22711
- **详细分析**: [[20_Research/Papers/强化学习/Abstraction_for_Offline_Goal-Conditioned_Reinforcement_Learning|Abstraction for Offline Goal-Conditioned Reinforcement Learning]]
- **作者**: Clarisse Wibault, Alexander Goldie, Antonio Villares, Maike Osborne, Jakob Foerster
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Abstraction for Offline Goal-Conditioned Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARL, GCRL, SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Markov Decision Processes (MDPs) often exhibit significant redundancy due to symmetries and shared structure across state-goal pairs in real-world Goal-Conditioned Reinforcement Learning (GCRL). While hierarchical policies have been motivated for horizon reduction via temporal abstraction in offline GCRL, we demonstrate that hierarchy also enables absolute abstraction. By introducing relativised options as well as distinct representations for different levels of the hierarchy, we demonstrate how an agent can reuse experience across similar contexts of the state-space. Based on this framework, we introduce two simple algorithms for learning relativised options and abstracting from the absolute frame of reference. Our experiments show that such inductive biases significantly improve performance in offline GCRL.

</details>

---

### [[20_Research/Papers/具身智能/Scout-Assisted_Planning_for_Heterogeneous_Robot_Teams_under_Partially_Known_Environments|Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments]]

![[assets/2605.22693_figure.jpg|800]]

- **arXiv**: [2605.22693](https://arxiv.org/abs/2605.22693)
- **PDF**: https://arxiv.org/pdf/2605.22693
- **详细分析**: [[20_Research/Papers/具身智能/Scout-Assisted_Planning_for_Heterogeneous_Robot_Teams_under_Partially_Known_Environments|Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments]]
- **作者**: Hoang-Dung Bui, Abhish Khanal, Raihan Islam Arnob, Gregory J. Stein
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Scout-Assisted Planning for Heterogeneous Robot Teams under Partially Known Environments》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robot teams navigating partially known environments face costly backtracking when ground robots encounter blocked roads that are only revealed upon physical traversal. We address this with Scout-Assisted Planning, a heterogeneous planning framework in which scouting Unmanned Aerial Vehicles proactively gather environmental information to improve Unmanned Ground Vehicle navigation. To focus scouting on the most consequential edges, we propose Information Gain-based Action Pruning, which scores candidate scouting actions by their expected impact on ground robot behavior. Since exact Information Gain-based Action Pruning computation is prohibitively expensive, we develop a Graph Neural Network based model that predicts information gain values directly from graph structure and belief state, reducing planning time to real-time levels without sacrificing solution quality. Experiments across three environment types show that SAP with Information Gain Action Pruning reduces ground robot travel cost by 31.9--37.7% over the Canadian Traveler Problem baseline, and outperforms proximity-based scouting guidance by an additional 8--14%, confirming that principled information-gain-guided scouting is both more effective and computationally feasible for real-world deployment

</details>

---

### [[20_Research/Papers/大模型/WorkstreamBench_Evaluating_LLM_Agents_on_End-to-End_Spreadsheet_Tasks_in_Finance|WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance]]

![[assets/2605.22664_figure.png|800]]

- **arXiv**: [2605.22664](https://arxiv.org/abs/2605.22664)
- **PDF**: https://arxiv.org/pdf/2605.22664
- **详细分析**: [[20_Research/Papers/大模型/WorkstreamBench_Evaluating_LLM_Agents_on_End-to-End_Spreadsheet_Tasks_in_Finance|WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance]]
- **作者**: Thomson Yen, Julian Poeltl, Harshith Srinivas Gear, Yilin Meng, Joshua Fan, Adam Shen, Yili Liu, Ali Bauyrzhan, Siri Du, Haoyang Liu, Daniel Guetta, Hongseok Namkoong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《WorkstreamBench: Evaluating LLM Agents on End-to-End Spreadsheet Tasks in Finance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SpreadsheetBench, WorkstreamBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly expected to carry out end-to-end workflows, producing complete artifacts from high-level user instructions. To meet enterprise needs, frontier AI labs have developed agents that can construct entire spreadsheets from scratch. This is especially relevant in finance, where core workflows such as financial modeling, forecasting, and scenario analysis are commonly conducted through spreadsheets. Yet, existing spreadsheet benchmarks do not measure this advanced capability, focusing instead on question-answering or single-formula edits. To address this gap, we provide one of the first evaluations of agents on end-to-end spreadsheet tasks, focusing on economically critical financial workflows such as modeling and scenario analysis. Since deliverables therein are routinely reviewed and revised by multiple stakeholders, judging their quality necessarily involves high-level criteria such as readability or ease of modification. To reflect the multidimensional nature of solution quality, we develop an evaluation taxonomy comprising three dimensions: Accuracy, Formula, and Format, each comprising fine-grained criteria that reflect professional standards. The Claude family leads the benchmark and produces the most professional-looking outputs in our qualitative review, but even the strongest agents frequently fall short of professional finance standards and degrade sharply as the difficulty increases beyond a few chained calculations. This suggests that current agents are not yet able to reliably produce professional-quality spreadsheets at the level of complexity real-world workflows demand.

</details>

---

### [[20_Research/Papers/大模型/Spreadsheet-RL_Advancing_Large_Language_Model_Agents_on_Realistic_Spreadsheet_Tasks_via_Reinforcement_Learning|Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning]]

![[assets/2605.22642_figure.png|800]]

- **arXiv**: [2605.22642](https://arxiv.org/abs/2605.22642)
- **PDF**: https://arxiv.org/pdf/2605.22642
- **详细分析**: [[20_Research/Papers/大模型/Spreadsheet-RL_Advancing_Large_Language_Model_Agents_on_Realistic_Spreadsheet_Tasks_via_Reinforcement_Learning|Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning]]
- **作者**: Banghao Chi, Yining Xie, Mingyuan Wu, Jingcheng Yang, Jize Jiang, Zhaoheng Li, Shengyi Qian, Minjia Zhang, Klara Nahrstedt, Rui Hou, Xiangjun Fan, Hanchao Yu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 2.1（加权：大模型 1.3，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Spreadsheet-RL: Advancing Large Language Model Agents on Realistic Spreadsheet Tasks via Reinforcement Learning》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Post-RL, Pre-RL, Spreadsheet-RL, SpreadsheetBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spreadsheet systems (e.g., Microsoft Excel, Google Sheets) play a central role in modern data-centric workflows. As AI agents grow increasingly capable of automating complex tasks, such as controlling computers and generating presentations, building an AI-driven spreadsheet agent has emerged as a promising research direction. Most existing spreadsheet agents rely on specialized prompting over general-purpose LLMs; while this design has potentials on simple spreadsheet operations, it struggles to manage the complex, multi-step workflows typical of real-world applications. We introduce Spreadsheet-RL, a reinforcement learning (RL) fine-tuning framework designed to train specialized spreadsheet agents within a realistic Microsoft Excel environment. Spreadsheet-RL features an automated pipeline for scalable collection of paired start-goal spreadsheets from online forums, as well as domain-specific evaluation tasks in areas such as finance and supply chain management, which we compile into the new Domain-Spreadsheet benchmark dataset. It also includes a Spreadsheet Gym environment designed for multi-turn RL: Spreadsheet Gym exposes extensive Excel functionality through a Python sandbox, along with a refined harness that incorporates a comprehensive tool set and carefully designed tool-routing rules for spreadsheet tasks. Through comprehensive experiments, we show that Spreadsheet-RL substantially enhances AI agent's performance on both general and domain-specific spreadsheet tasks: it improves Qwen3-4B-Thinking-2507's Pass@1 on SpreadsheetBench from 12.0% to 23.4%, and raises Pass@1 from 8.4% to 17.2% on our curated Domain-Spreadsheet dataset. These results highlight Spreadsheet-RL's strong potential for generalization and real-world adoption in spreadsheet automation, and broadly, its promise for advancing LLM-based interactions with data interfaces in everyday work.

</details>

---

### [[20_Research/Papers/大模型/Agentic_CLEAR_Automating_Multi-Level_Evaluation_of_LLM_Agents|Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents]]

![[assets/2605.22608_first_page.png|800]]

- **arXiv**: [2605.22608](https://arxiv.org/abs/2605.22608)
- **PDF**: https://arxiv.org/pdf/2605.22608
- **详细分析**: [[20_Research/Papers/大模型/Agentic_CLEAR_Automating_Multi-Level_Evaluation_of_LLM_Agents|Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents]]
- **作者**: Asaf Yehudai, Lilach Eden, Michal Shmueli-Scheuer
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agentic CLEAR: Automating Multi-Level Evaluation of LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AppWorld, SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic systems are becoming more capable: agents define strategies, take actions, and interact with different environments. This autonomy poses serious challenges for overseeing and assessing agent behavior. Most current tools are limited, focusing on observability with basic evaluation capabilities or imposing static, hand-crafted error taxonomies that cannot adapt to new domains. To address this gap, we present Agentic CLEAR, an automatic, dynamic, and easy-to-use evaluation framework. It produces textual insights into the agent behavior on three levels of granularity: system, trace, and node. Agentic CLEAR operates above the observability layer, enabling seamless integration and featuring an intuitive UI that makes agent evaluation highly accessible. In our experiments on four benchmarks, seven agentic settings, and tens of thousands of LLM calls, we show that Agentic CLEAR produces high-quality, data-driven, insightful feedback. Our analysis shows strong alignment with human-annotated errors and the ability to predict task success rate.

</details>

---

### [[20_Research/Papers/具身智能/MoSA_Motion-constrained_Stress_Adaptation_for_Mitigating_Real-to-Sim_Gap_in_Continuum_Dynamics_via_Learning_Residual_Anisotropy|MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy]]

![[assets/2605.22597_figure.png|800]]

- **arXiv**: [2605.22597](https://arxiv.org/abs/2605.22597)
- **PDF**: https://arxiv.org/pdf/2605.22597
- **详细分析**: [[20_Research/Papers/具身智能/MoSA_Motion-constrained_Stress_Adaptation_for_Mitigating_Real-to-Sim_Gap_in_Continuum_Dynamics_via_Learning_Residual_Anisotropy|MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy]]
- **作者**: Jiaxu Wang, Junhao He, Jingkai Sun, Yi Gu, Yunyang Mo, Jiahang Cao, Qiang Zhang, Renjing Xu
- **cs 子类**: cs.AI, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《MoSA: Motion-constrained Stress Adaptation for Mitigating Real-to-Sim Gap in Continuum Dynamics via Learning Residual Anisotropy》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, Real-to-Sim, Vid2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning real-world dynamics from visual observations is crucial for various domains. A common strategy is to calibrate simulators by estimating physical parameters, yet accuracy is ultimately bounded by the underlying physical models, which often assume materials are homogeneous and isotropic. Even if reasonable, real-world objects typically exhibit mild anisotropy and heterogeneity. After the near-isotropic backbone is well calibrated, these residual effects become the key bottleneck for further closing the real-to-sim gap. Although neural networks can fit dynamics end-to-end, such black-box modeling discards strong physical priors, leading to poor data efficiency and overfitting. Therefore, we propose MoSA, a motion-constrained stress adaptation framework that targets these residual effects to further improve real-to-sim dynamics learning. MoSA uses an isotropic model as a physics prior and learns residual stress operators to capture mild anisotropy and heterogeneity. It progressively adapts stresses via microplane-constrained redistribution in a physics-informed cascaded network. We further impose motion constraints by supervising temporal and spatial derivatives of the deformation field. Experimentally, our learned dynamics achieves superior accuracy, generalization, and robustness, while learning physically meaningful residual anisotropy. Finally, we validate MoSA in a robot manipulation setting, showing that better real-to-sim dynamics modeling translates into more reliable sim-to-real transfer. Project Page is available at https://mercerai.github.io/MoSA/.

</details>

---

### [[20_Research/Papers/大模型/Understanding_Multimodal_Failure_in_Action-Chunking_Behavioral_Cloning|Understanding Multimodal Failure in Action-Chunking Behavioral Cloning]]

![[assets/2605.22493_figure.png|800]]

- **arXiv**: [2605.22493](https://arxiv.org/abs/2605.22493)
- **PDF**: https://arxiv.org/pdf/2605.22493
- **详细分析**: [[20_Research/Papers/大模型/Understanding_Multimodal_Failure_in_Action-Chunking_Behavioral_Cloning|Understanding Multimodal Failure in Action-Chunking Behavioral Cloning]]
- **作者**: Lorenzo Mazza, Massimiliano Datres, Ariel Rodriguez, Sebastian Bodenstedt, Gitta Kutyniok, Stefanie Speidel
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Understanding Multimodal Failure in Action-Chunking Behavioral Cloning》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavioral cloning becomes difficult when the same observation admits several valid actions. We study this problem for action-chunking policies and show that different multimodal parameterizations fail in different ways. For latent-variable policies, posterior-prior regularization makes deployment-time sampling more reliable, but excessive regularization removes the action-conditioned information needed to distinguish demonstrated modes. Reducing this regularization can preserve mode information, but then success depends on whether the prior covers the relevant latent regions. For action-space generative policies, multimodality is constrained by the smoothness of the base-to-action transport: a map with small Lipschitz constant cannot assign substantial probability to many well-separated modes. Covering many modes therefore requires either sharp transitions in base space or off-support bridge regions in action space. Experiments on synthetic multimodal tasks and robotic simulation benchmarks support these mechanisms.

</details>

---

### [[20_Research/Papers/强化学习/Don't_Forget_the_Critic_Value-Based_Data_Rehearsal_for_Multi-Cyclic_Continual_Reinforcement_Learning|Don't Forget the Critic: Value-Based Data Rehearsal for Multi-Cyclic Continual Reinforcement Learning]]

![[assets/2605.22454_first_page.png|800]]

- **arXiv**: [2605.22454](https://arxiv.org/abs/2605.22454)
- **PDF**: https://arxiv.org/pdf/2605.22454
- **详细分析**: [[20_Research/Papers/强化学习/Don't_Forget_the_Critic_Value-Based_Data_Rehearsal_for_Multi-Cyclic_Continual_Reinforcement_Learning|Don't Forget the Critic: Value-Based Data Rehearsal for Multi-Cyclic Continual Reinforcement Learning]]
- **作者**: Benjamin Poole, Andrew Quinn, Li Yang, Minwoo Lee
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Don't Forget the Critic: Value-Based Data Rehearsal for Multi-Cyclic Continual Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Data rehearsal has emerged as a leading approach for mitigating catastrophic forgetting in Continual Reinforcement Learning (CRL). However, existing work remains confined to policy gradient frameworks, regularizing only actors due to the performance degradation incurred by critic regularization. This actor-centric approach overlooks the potential of data rehearsal for value function approximation. Moreover, existing evaluations in CRL rarely consider multi-cyclic environments where task sequences repeat, a critical real-world scenario that exacerbates forgetting and plasticity. We investigate data rehearsal for Deep Q-Networks using Q-value regularization in multi-cyclic settings and propose Qreg+NWLU which introduces two simple modifications: (1) continuous data rehearsal that dynamically collects and updates stored Q-values throughout training, and (2) "No-Wait" regularization that applies immediately rather than after the first task. Together, these modifications yield improvements in learning efficiency, forgetting mitigation, and knowledge transfer over Qreg and conventional CRL methods within value function approximation settings.

</details>

---

### [[20_Research/Papers/具身智能/Pre-VLA_Preemptive_Runtime_Verification_for_Reliable_Vision-Language-Action_and_World-Model_Rollouts|Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts]]

![[assets/2605.22446_figure.png|800]]

- **arXiv**: [2605.22446](https://arxiv.org/abs/2605.22446)
- **PDF**: https://arxiv.org/pdf/2605.22446
- **详细分析**: [[20_Research/Papers/具身智能/Pre-VLA_Preemptive_Runtime_Verification_for_Reliable_Vision-Language-Action_and_World-Model_Rollouts|Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts]]
- **作者**: Zhen Sun, Yongjian Guo, Haoran Sun, Luqiao Wang, Wei Lu, Jiachi Ji, Shengzhe Ji, Junwu Xiong, Zhijun Meng
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 3.6（加权：具身智能 3，大模型 0.1，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Pre-VLA: Preemptive Runtime Verification for Reliable Vision-Language-Action and World-Model Rollouts》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CTRL-World, OpenVLA, Pre-VLA, RynnVLA, World-VLA, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While large vision-language-action (VLA) models and generative world models (WM) have advanced long-horizon embodied intelligence, their practical deployment remains challenged by uncertainty in learning-based action generation. Low-quality actions may cause physical failures during execution or lead to misleading world-model rollouts with redundant rendering costs. To address this issue, we propose Pre-VLA, a unified runtime verification architecture that performs preemptive action validity assessment before physical execution or world-model imagination. Pre-VLA leverages an efficient multimodal backbone with modality-aware pooling and a lightweight dual-branch head to predict both safety confidence and critic-derived advantage scores for candidate action chunks. To handle severe class imbalance and unstable boundary decisions, we train Pre-VLA with a multi-task objective combining Focal classification, advantage regression, and soft-threshold calibration. During deployment, a dual-mode preemptive resampling scheduler filters low-quality actions and triggers adaptive resampling under a limited computation budget. Experiments on the LIBERO benchmark show that Pre-VLA improves the average closed-loop success rate across four suites from 30.79\% to 37.62\% over RynnVLA-002, reduces task execution steps, achieves 183.9 ms average forward verification time per action chunk, and mitigates error accumulation in world-model rollouts.

</details>

---

### [[20_Research/Papers/大模型/DeferMem_Query-Time_Evidence_Distillation_via_Reinforcement_Learning_for_Long-Term_Memory_QA|DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA]]

![[assets/2605.22411_figure.png|800]]

- **arXiv**: [2605.22411](https://arxiv.org/abs/2605.22411)
- **PDF**: https://arxiv.org/pdf/2605.22411
- **详细分析**: [[20_Research/Papers/大模型/DeferMem_Query-Time_Evidence_Distillation_via_Reinforcement_Learning_for_Long-Term_Memory_QA|DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA]]
- **作者**: Jianing Yin, Tan Tang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《DeferMem: Query-Time Evidence Distillation via Reinforcement Learning for Long-Term Memory QA》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents still struggle with long-term memory question answering, where answer-supporting evidence is often scattered across long conversational histories and buried in substantial irrelevant content. Existing memory systems typically process memory before future queries are known, then retrieve the resulting units based on similarity rather than their utility for answering the query. This workflow leaves downstream answerers to denoise retrieved candidates and reconstruct query-specific evidence. We present DeferMem, a long-term memory framework that decouples this problem into high-recall candidate retrieval and query-conditioned evidence distillation. DeferMem uses a lightweight segment-link structure to organize raw history and retrieve broad candidates at query time. It then applies a memory distiller trained with DistillPO, our reinforcement learning algorithm for distilling the high-recall but highly noisy candidates into a set of faithful, self-contained, and query-conditioned evidence. DistillPO formulates post-retrieval evidence distillation as a structured action comprising message selection and evidence rewriting. It optimizes this action with a decomposed-and-gated reward pipeline and structure-aligned advantage assignment, gating reward components from validity to quality checks while exposing task-level correctness feedback early and assigning each reward to its responsible output span. On LoCoMo and LongMemEval-S, DeferMem surpasses strong baselines in QA accuracy and memory-system efficiency, achieving the highest QA accuracy with the fastest runtime and zero commercial-API token cost for memory operations.

</details>

---

### [[20_Research/Papers/强化学习/Incentive-Aligned_Vehicle-to-Vehicle_Energy_Trading_via_Nash-Integrated_Multi-Agent_Reinforcement_Learning|Incentive-Aligned Vehicle-to-Vehicle Energy Trading via Nash-Integrated Multi-Agent Reinforcement Learning]]

![[assets/2605.22363_figure.png|800]]

- **arXiv**: [2605.22363](https://arxiv.org/abs/2605.22363)
- **PDF**: https://arxiv.org/pdf/2605.22363
- **详细分析**: [[20_Research/Papers/强化学习/Incentive-Aligned_Vehicle-to-Vehicle_Energy_Trading_via_Nash-Integrated_Multi-Agent_Reinforcement_Learning|Incentive-Aligned Vehicle-to-Vehicle Energy Trading via Nash-Integrated Multi-Agent Reinforcement Learning]]
- **作者**: Yujin Lin, Yue Yang, Hao Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Incentive-Aligned Vehicle-to-Vehicle Energy Trading via Nash-Integrated Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vehicle-to-vehicle (V2V) energy trading enables decentralized peer-to-peer energy exchange among electric vehicles (EVs), reducing grid dependency while monetizing surplus capacity. However, coordinating self-interested EV agents with diverse charging needs and uncertain arrival-departure schedules remains challenging. Existing approaches either require centralized optimization with computational limitations or lack fairness guarantees. This paper integrates Nash Bargaining Solution into Multi-Agent Deep Deterministic Policy Gradient, namely Nash-MADDPG, for incentive-aligned V2V energy trading. Nash bargaining determines efficient bilateral pricing, while Nash-guided price proximity rewards align agent learning toward bargaining-optimal strategies. Evaluation over 30-day continuous operation demonstrates an improvement of 61.6% in social welfare and 62.9% improvement in trading volume over Double Auction, while achieving superior fairness, such as 40.1% improvement in Jain's index. Testing across 6-100 agents over a 30-day horizon with continuous vehicle turnover confirms scalability across population size and empirically stable pricing near the Nash Bargaining benchmark.

</details>

---

### [[20_Research/Papers/强化学习/ACCoRD_Actor-Critic_Conflict_Resolution_with_Deep_learning_for_O-RAN_xApps|ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps]]

![[assets/2605.22306_first_page.png|800]]

- **arXiv**: [2605.22306](https://arxiv.org/abs/2605.22306)
- **PDF**: https://arxiv.org/pdf/2605.22306
- **详细分析**: [[20_Research/Papers/强化学习/ACCoRD_Actor-Critic_Conflict_Resolution_with_Deep_learning_for_O-RAN_xApps|ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps]]
- **作者**: Cezary Adamczyk, Adrian Kliks
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《ACCoRD: Actor-Critic Conflict Resolution with Deep learning for O-RAN xApps》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conflict Mitigation (ConMit) is a crucial part of intelligent network control in Open Radio Access Networks (O-RAN). In this paper, we propose a method named ACCoRD to resolve detected control conflicts in Near-Real Time RAN Intelligent Controller using a Conflict Resolution (CR) Agent with an Artificial Neural Network (ANN) trained with a reinforcement learning algorithm PPO-Clip. The implemented ANN analyzes data about the network and conflicting control decisions to infer optimal CR actions. The CR Agent gathers feedback from the network after each resolved conflict to assess its efficiency and adjust the ANN's weights during batch training. The evaluation of the proposed approach is based on simulation data. A new methodology for evaluating CR solutions is proposed. Results show that the proposed ANN-based method improves on the efficiency of rule-based approaches by significantly reducing negative network events caused by conflicting control decisions in medium and high traffic scenarios.

</details>

---

### [[20_Research/Papers/具身智能/Action_with_Visual_Primitives|Action with Visual Primitives]]

![[assets/2605.22183_figure.png|800]]

- **arXiv**: [2605.22183](https://arxiv.org/abs/2605.22183)
- **PDF**: https://arxiv.org/pdf/2605.22183
- **详细分析**: [[20_Research/Papers/具身智能/Action_with_Visual_Primitives|Action with Visual Primitives]]
- **作者**: Weilong Guo, Yuchen Wang, Renping Zhou, Yunfeng Zhang, Rui Fang, Yue Meng, Wenda Xu, Yuan He, Gao Huang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Action with Visual Primitives》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Point-VLA, PointVLA, TraceVLA, VP-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for generalist robotic manipulation. A common design in current architectures maps language instructions and visual observations to actions in a single forward pass. While conceptually simple, this formulation entangles instruction comprehension, spatial scene understanding, and motor control within a single learning objective. As a result, the action expert must implicitly relearn cognitive and perceptual capabilities already present in the pretrained VLM, which can limit both learning efficiency and generalization. We introduce AVP (Action with Visual Primitives), an end-to-end architecture that implements this visual-primitive-centric interface: the VLM infers the next-stage target and emits visual-primitive tokens that condition a flow-matching action expert, with supervision derived from end-effector kinematics. Real-robot experiments on general pick-and-place tasks show that AVP improves the success rate by 27.61% over pi_0.5 and outperforms other recent methods, with consistent gains in data efficiency, spatial-compositional generalization, and object-level transfer.

</details>

---

### [[20_Research/Papers/大模型/LLM-Metrics_Measuring_Research_Impact_Through_Large_Language_Model_Memory|LLM-Metrics: Measuring Research Impact Through Large Language Model Memory]]

![[assets/2605.22176_figure.png|800]]

- **arXiv**: [2605.22176](https://arxiv.org/abs/2605.22176)
- **PDF**: https://arxiv.org/pdf/2605.22176
- **详细分析**: [[20_Research/Papers/大模型/LLM-Metrics_Measuring_Research_Impact_Through_Large_Language_Model_Memory|LLM-Metrics: Measuring Research Impact Through Large Language Model Memory]]
- **作者**: Si Shen, Wenhua Zhao, Danhao Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM

#### 研究背景与动机

《LLM-Metrics: Measuring Research Impact Through Large Language Model Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Citation counts remain the dominant metric for assessing research impact, yet they suffer from well-documented limitations: temporal lag, disciplinary bias, and Matthew effects. Here we propose LLM-Metrics, a research-impact assessment metric derived from the parametric memory of large language models (LLMs). The central hypothesis is that high-impact papers receive greater exposure in the academic community, that this exposure enters LLM training data in textual form, and that models consequently form stronger parametric memory of these papers. We designed four types of multiple-choice probes, covering title recognition, author recognition, method recognition, and venue recognition, and evaluated 549 computer science papers published in 2023-2024 across 17 LLMs spanning 0.5B to 72B parameters from six vendors. Of the 17 models, 15 produced positive predictions, 9 of which were significant at p less than 0.05, with an overall Spearman correlation of rho = 0.1495 and p = 0.0004 against citation counts. Three additional findings support the proposed mechanism. First, the predictive signal was stronger for 2024 papers, rho = 0.1880, whose citation counts were near zero at model-training time, reducing the plausibility of a simple reverse-causality explanation. Second, author-recognition probes showed the strongest discriminative power, consistent with an exposure-driven memory mechanism. Third, model scale and predictive power were non-monotonic: a 3B-parameter model, Llama-3.2-3B-Instruct, with rho = 0.1829, outperformed most larger models, supporting a selective-memory hypothesis in which the limited capacity of smaller models can serve as an effective information filter. LLM-Metrics offers a real-time, cross-disciplinary, citation-independent paradigm for research assessment.

</details>

---

### [[20_Research/Papers/大模型/Adapting_the_Interface,_Not_the_Model_Runtime_Harness_Adaptation_for_Deterministic_LLM_Agents|Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents]]

![[assets/2605.22166_figure.png|800]]

- **arXiv**: [2605.22166](https://arxiv.org/abs/2605.22166)
- **PDF**: https://arxiv.org/pdf/2605.22166
- **详细分析**: [[20_Research/Papers/大模型/Adapting_the_Interface,_Not_the_Model_Runtime_Harness_Adaptation_for_Deterministic_LLM_Agents|Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents]]
- **作者**: Tianshi Xu, Huifeng Wen, Meng Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, AgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are shaped not only by their language models, but also by the runtime harness that mediates observation, tool use, action execution, feedback interpretation, and trajectory control. While existing agent adaptation methods mainly update model parameters, many failures in deterministic, rule-governed domains stem from mismatches at the model--environment interface. We propose Life-Harness, a lifecycle-aware runtime harness that improves frozen LLM agents without changing model weights or evaluation environments. Life-Harness evolves from training trajectories by converting recurring interaction failures into reusable interventions across environment contracts, procedural skills, action realization, and trajectory regulation, and remains fixed during held-out evaluation. On seven deterministic environments from $τ$-bench, $τ^2$-bench, and AgentBench, Life-Harness improves 116 out of 126 model--environment settings across 18 model backbones, with an average relative improvement of 88.5%. Harnesses evolved only from Qwen3-4B-Instruct trajectories transfer to 17 other models, showing that Life-Harness captures reusable environment-side structure rather than model-specific behavior. These results position runtime interface adaptation as a complementary alternative to model-centric agent training. Code is available at GitHub.

</details>

---

### [[20_Research/Papers/强化学习/One-Way_Policy_Optimization_for_Self-Evolving_LLMs|One-Way Policy Optimization for Self-Evolving LLMs]]

![[assets/2605.22156_figure.png|800]]

- **arXiv**: [2605.22156](https://arxiv.org/abs/2605.22156)
- **PDF**: https://arxiv.org/pdf/2605.22156
- **详细分析**: [[20_Research/Papers/强化学习/One-Way_Policy_Optimization_for_Self-Evolving_LLMs|One-Way Policy Optimization for Self-Evolving LLMs]]
- **作者**: Shuo Yang, Jinda Lu, Kexin Huang, Chiyu Ma, Shaohang Wei, Yuyang Liu, Guoyin Wang, Jingren Zhou, Li Yuan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《One-Way Policy Optimization for Self-Evolving LLMs》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) has become a promising paradigm for scaling reasoning capabilities of Large Language Models (LLMs). However, the sparsity of binary verifier rewards often leads to low efficiency and optimization instability. To stabilize training, existing methods typically impose token-level constraints relative to a reference policy. We identify that such constraints penalize deviations indiscriminately; this can flip verifier-determined direction when the policy attempts to outperform the reference, thereby suppressing gains. To resolve this, we propose One-Way Policy Optimization (OWPO), a method based on the principle of decoupling optimization direction from update magnitude. In OWPO, the verifier dictates the update direction, while the reference policy serves only to adjust the magnitude. Specifically, OWPO applies asymmetric reweighting: it performs Accelerated Alignment for inferior deviations (where the policy lags behind the reference) and Gain Locking for superior deviations (where the policy surpasses the reference). Furthermore, by incorporating iterative reference updates, OWPO creates a ``Ratchet Effect'' that continuously consolidates gains. Experimental results demonstrate that OWPO outperforms strong baselines, including DAPO, OPD, and MOPD, breaking the bottleneck of fixed priors to enable continuous self-evolution without reliance on external reference models.

</details>

---

### [[20_Research/Papers/大模型/IdleSpec_Exploiting_Idle_Time_via_Speculative_Planning_for_LLM_Agents|IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents]]

![[assets/2605.22154_figure.png|800]]

- **arXiv**: [2605.22154](https://arxiv.org/abs/2605.22154)
- **PDF**: https://arxiv.org/pdf/2605.22154
- **详细分析**: [[20_Research/Papers/大模型/IdleSpec_Exploiting_Idle_Time_via_Speculative_Planning_for_LLM_Agents|IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents]]
- **作者**: Daewon Choi, Kyunghyun Park, Woomin Song, Saket Dingliwal, Sai Muralidhar Jayanthi, Jinwoo Shin, Aram Galstyan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《IdleSpec: Exploiting Idle Time via Speculative Planning for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MLE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based agents solve complex tasks by leveraging multi-step reasoning with iterative tool calls and environment interactions, which incur idle time while waiting for observations. Despite the prevalence of idle time in most agentic scenarios, existing works treat it as an unavoidable overhead or propose restricted solutions that overlook varying computational budgets across different tool calls and future observation uncertainty, thereby leading to suboptimal utilization of idle time. In this paper, we introduce IdleSpec, a scalable and generic inference approach that leverages idle-time computation to improve agent performance while minimizing latency overhead. Specifically, IdleSpec iteratively generates plan candidates during idle periods and, once observations become available, aggregates them to guide the next reasoning step. For effective plan generation under observation uncertainty, IdleSpec samples between complementary drafting strategies (i.e., progressive and recovery) from a learned distribution that is updated via posterior feedback. Our experiments demonstrate that IdleSpec significantly improves agent performance in various agentic scenarios by effectively utilizing idle time. In particular, on the GAIA and FRAMES, IdleSpec achieves 55.6% average accuracy with Gemini-2.5-Flash, surpassing the vanilla baseline without idle-time usage by 5.1%. Furthermore, for MLE-Bench, which involves substantial delay from code executions, IdleSpec achieves performance gains of up to 9.1% on the Any Medal rate, highlighting its generalizability to long-horizon tasks.

</details>

---

### [[20_Research/Papers/大模型/Ratchet_A_Minimal_Hygiene_Recipe_for_Self-Evolving_LLM_Agents|Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents]]

![[assets/2605.22148_figure.png|800]]

- **arXiv**: [2605.22148](https://arxiv.org/abs/2605.22148)
- **PDF**: https://arxiv.org/pdf/2605.22148
- **详细分析**: [[20_Research/Papers/大模型/Ratchet_A_Minimal_Hygiene_Recipe_for_Self-Evolving_LLM_Agents|Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents]]
- **作者**: Xing Zhang, Yanwei Cui, Guanghui Wang, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Ratchet: A Minimal Hygiene Recipe for Self-Evolving LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillRL, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving skill libraries, pioneered by Voyager, let frozen LLM agents accumulate reusable knowledge without weight updates, yet recent evaluation shows that LLM-authored skills deliver $+0.0$pp over no-skill baselines while human-curated ones deliver $+16.2$pp: the bottleneck is not skill authoring but lifecycle management. We introduce \textbf{Ratchet}, a single-agent loop in which a frozen LLM writes, retrieves, curates, and retires its own natural-language skills. Ratchet integrates four candidate hygiene mechanisms: outcome-driven retirement, a bounded active-cap, meta-skill authoring guidance, and pattern canonicalisation. On MBPP+ hard-100 with Claude Opus 4.7, Ratchet lifts held-out pass@1 from a $0.258 \pm 0.047$ baseline to a late-window rolling mean of $0.584$ (peak $0.658 \pm 0.042$) across 100 rounds and 3 seeds, a $+0.328 \pm 0.018$ rolling-mean gain where the no-skill control drifts at $+0.002 \pm 0.005$; the same recipe transfers to an agentic solver on SWE-bench Verified ($+0.22$ peak lift over 20 rounds). Eight ablations (A1--A8) reveal that the minimal working recipe is smaller than our design suggests: retirement and the meta-skill authoring prior are load-bearing, while explicit deduplication (canonicalisation, cover-guard) is subsumed by the meta-skill itself. A non-divergence proposition shows that bounded cap and retirement threshold together prevent expected performance from drifting below the no-skills floor.

</details>

---

### [[20_Research/Papers/具身智能/Short-Term-to-Long-Term_Memory_Transfer_for_Knowledge_Graphs_under_Partial_Observability|Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability]]

![[assets/2605.22142_figure.png|800]]

- **arXiv**: [2605.22142](https://arxiv.org/abs/2605.22142)
- **PDF**: https://arxiv.org/pdf/2605.22142
- **详细分析**: [[20_Research/Papers/具身智能/Short-Term-to-Long-Term_Memory_Transfer_for_Knowledge_Graphs_under_Partial_Observability|Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability]]
- **作者**: Taewoon Kim, Vincent François-Lavet, Michael Cochez
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Short-Term-to-Long-Term Memory Transfer for Knowledge Graphs under Partial Observability》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning under partial observability requires deciding what information to retain, yet most memory-based approaches do not explicitly model short-term-to-long-term transfer of symbolic observations. We study this transfer process in a temporal knowledge-graph memory setting and cast it as a neuro-symbolic value-based decision problem: for each observed triple, the agent chooses whether to keep or drop it before long-term insertion. To handle variable-sized short-term buffers, we use a per-item Q-learning design with shared parameters and a practical temporal-difference update over matched items across consecutive steps. On the RoomKG benchmark at long-term memory capacity 128, learned transfer decisions outperform symbolic and neural baselines, including symbolic baselines with temporal annotations and history-based LSTM/Transformer baselines. Across transfer-policy ablations, a lightweight local short-term-only variant performs best, and step-level behavior shows that the policy keeps navigation- and query-relevant facts while discarding lower-value candidate facts, supporting explicit and interpretable memory decisions under memory constraints.

</details>

---

### [[20_Research/Papers/大模型/Efficient_Agentic_Reasoning_Through_Self-Regulated_Simulative_Planning|Efficient Agentic Reasoning Through Self-Regulated Simulative Planning]]

![[assets/2605.22138_figure.png|800]]

- **arXiv**: [2605.22138](https://arxiv.org/abs/2605.22138)
- **PDF**: https://arxiv.org/pdf/2605.22138
- **详细分析**: [[20_Research/Papers/大模型/Efficient_Agentic_Reasoning_Through_Self-Regulated_Simulative_Planning|Efficient Agentic Reasoning Through Self-Regulated Simulative Planning]]
- **作者**: Mingkai Deng, Jinyu Hou, Lara Sá Neves, Varad Pimpalkhute, Taylor W. Killian, Zhengzhong Liu, Eric P. Xing
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.45，强化学习 0.36，世界模型 0.36）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Efficient Agentic Reasoning Through Self-Regulated Simulative Planning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How should an agent decide when and how to plan? A dominant approach builds agents as reactive policies with adaptive computation (e.g., chain-of-thought), trained end-to-end expecting planning to emerge implicitly. Without control over the presence, structure, or horizon of planning, these systems dramatically increase reasoning length, yielding inefficient token use without reliable accuracy gains. We argue efficient agentic reasoning benefits from decomposing decision-making into three systems: simulative reasoning (System II) grounding deliberation in future-state prediction via a world model; self-regulation (System III) deciding when and how deeply to plan via a learned configurator; and reactive execution (System I) handling fine-grained action. Simulative reasoning provides unified planning across diverse tasks without per-domain engineering, while self-regulation ensures the planner is invoked only when needed. To test this, we develop SR$^2$AM (Self-Regulated Simulative Reasoning Agentic LLM), realizing both as distinct stages within an LLM's chain-of-thought, with the LLM as world model. We explore two instantiations: recording decisions from a prompted multi-module system (v0.1) and reconstructing structured plans from traces of pretrained reasoning LLMs (v1.0), trained via supervised then reinforcement learning (RL). Across math, science, tabular analysis, and web information seeking, v0.1-8B and v1.0-30B achieve Pass@1 competitive with 120-355B and 685B-1T parameter systems respectively, while v1.0-30B uses 25.8-95.3% fewer reasoning tokens than comparable agentic LLMs. RL increases average planning horizon by 22.8% while planning frequency grows only 2.0%, showing it learns to plan further ahead rather than more often. More broadly, learned self-regulation instantiates a principle we expect to extend beyond planning to how agents govern their own learning and adaptation.

</details>

---

### [[20_Research/Papers/具身智能/LVDrive_Latent_Visual_Representation_Enhanced_Vision-Language-Action_Autonomous_Driving_Model|LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model]]

![[assets/2605.22089_figure.png|800]]

- **arXiv**: [2605.22089](https://arxiv.org/abs/2605.22089)
- **PDF**: https://arxiv.org/pdf/2605.22089
- **详细分析**: [[20_Research/Papers/具身智能/LVDrive_Latent_Visual_Representation_Enhanced_Vision-Language-Action_Autonomous_Driving_Model|LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model]]
- **作者**: Xiaodong Mei, Diankun Zhang, Hongwei Xie, Guang Chen, Hangjun Ye, Dan Xu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 1.7（加权：具身智能 1.5，世界模型 0.2）
- **关联关键词**: Multimodal, WorldModel, ComputerVision

#### 研究背景与动机

《LVDrive: Latent Visual Representation Enhanced Vision-Language-Action Autonomous Driving Model》归入 具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a promising framework for end-to-end autonomous driving. However, existing VLAs typically rely on sparse action supervision, which underutilizes their powerful scene understanding and reasoning capabilities. Recent attempts to incorporate dense visual supervision via world modeling often overemphasize pixel-level image reconstruction, neglecting semantically meaningful scene representation learning. In this work, we propose LVDrive, a Latent Visual representation enhanced VLA framework for autonomous driving. LVDrive introduces a future scene prediction task into the VLA paradigm, where future representations are learned entirely in a high-level latent space under auxiliary supervision from a pretrained vision backbone. Departing from inefficient autoregressive generation, we jointly model future scene and motion prediction within a unified embedding space, processed in a single forward pass to conduct the future-aware reasoning. We further design a two-stage trajectory decoding strategy that explicitly leverages the learned latent future representations to refine trajectory generation. Extensive experiments on the challenging Bench2Drive benchmark demonstrate that LVDrive achieves significant improvements in closed-loop driving performance, outperforming both action supervised methods and image-reconstruction-based world model approaches.

</details>

---

### [[20_Research/Papers/大模型/From_Reasoning_Chains_to_Verifiable_Subproblems_Curriculum_Reinforcement_Learning_Enables_Credit_Assignment_for_LLM_Reasoning|From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning]]

![[assets/2605.22074_figure.png|800]]

- **arXiv**: [2605.22074](https://arxiv.org/abs/2605.22074)
- **PDF**: https://arxiv.org/pdf/2605.22074
- **详细分析**: [[20_Research/Papers/大模型/From_Reasoning_Chains_to_Verifiable_Subproblems_Curriculum_Reinforcement_Learning_Enables_Credit_Assignment_for_LLM_Reasoning|From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning]]
- **作者**: Xitai Jiang, Zihan Tang, Wenze Lin, Yang Yue, Shenzhi Wang, Gao Huang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《From Reasoning Chains to Verifiable Subproblems: Curriculum Reinforcement Learning Enables Credit Assignment for LLM Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IMO-Bench, NuRL, SCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning from verifiable rewards (RLVR) has shown strong promise for LLM reasoning, but outcome-based RLVR remains inefficient on hard problems because correct final-answer rollouts are rare and sample-level credit assignment cannot use partial progress in failed attempts. We introduce SCRL (Subproblem Curriculum Reinforcement Learning), a curriculum RL framework that derives verifiable subproblems from reference reasoning chains and fixes the final subproblem as the original problem. This turns partial progress on hard problems into verifiable learning signals. Algorithmically, SCRL uses subproblem-level normalization, which normalizes rewards independently at each subproblem position and assigns the resulting advantages to the corresponding answer spans, enabling finer-grained credit assignment without external rubrics or reward models. Our analysis shows that subproblem curricula lift hard problems out of gradient dead zones, with larger relative gains as the original problem becomes harder. Across seven mathematical reasoning benchmarks, SCRL outperforms strong curriculum-learning baselines, improving average accuracy over GRPO by +4.1 points on Qwen3-4B-Base and +1.9 points on Qwen3-14B-Base. On AIME24, AIME25, and IMO-Bench, SCRL further improves pass@1 by +3.7 points and pass@64 by +4.6 points on Qwen3-4B-Base, indicating better exploration on hard reasoning problems.

</details>

---

### [[20_Research/Papers/机器人/FRED_A_Multi-Modal_Autonomous_Driving_Dataset_for_Flooded_Road_Environments|FRED: A Multi-Modal Autonomous Driving Dataset for Flooded Road Environments]]

![[assets/2605.22018_figure.png|800]]

- **arXiv**: [2605.22018](https://arxiv.org/abs/2605.22018)
- **PDF**: https://arxiv.org/pdf/2605.22018
- **详细分析**: [[20_Research/Papers/机器人/FRED_A_Multi-Modal_Autonomous_Driving_Dataset_for_Flooded_Road_Environments|FRED: A Multi-Modal Autonomous Driving Dataset for Flooded Road Environments]]
- **作者**: Connor Malone, Sebastien Demmel, Sebastien Glaser
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《FRED: A Multi-Modal Autonomous Driving Dataset for Flooded Road Environments》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Flooded Road Environments Dataset (FRED) is, to our knowledge, the first multi-modal autonomous driving dataset specifically targeting the collection of data from scenarios involving water hazards on the road. The dataset contains images from a 2.3 MP FLIR Blackfly USB3 camera, 64-beam 360$^\circ$ point clouds from an Ouster OS1-64 LiDAR, and data from an iXblue ATLANS-C IMU corrected by a Geoflex RTK GNSS, from five separate locations captured both during and after flooding events. The data has been released in two formats: a KITTI-style format for easy integration with existing data tools, and the RTMaps format for direct replay of the vehicle's data capture. We provide semantic labels to enable the training and evaluation of both single-sensor and sensor-fusion methods for water hazard detection. Position and velocity, as well as data captured under dry conditions, are provided to enable the development of location-based detection methods that may incorporate maps, and to evaluate other tasks such as localisation and SLAM.

</details>

---

### [[20_Research/Papers/大模型/Blind_Spots_in_the_Guard_How_Domain-Camouflaged_Injection_Attacks_Evade_Detection_in_Multi-Agent_LLM_Systems|Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems]]

![[assets/2605.22001_first_page.png|800]]

- **arXiv**: [2605.22001](https://arxiv.org/abs/2605.22001)
- **PDF**: https://arxiv.org/pdf/2605.22001
- **详细分析**: [[20_Research/Papers/大模型/Blind_Spots_in_the_Guard_How_Domain-Camouflaged_Injection_Attacks_Evade_Detection_in_Multi-Agent_LLM_Systems|Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems]]
- **作者**: Aaditya Pai
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Blind Spots in the Guard: How Domain-Camouflaged Injection Attacks Evade Detection in Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Injection detectors deployed to protect LLM agents are calibrated on static, template-based payloads that announce themselves as override directives. We identify a systematic blind spot: when payloads are generated to mimic the domain vocabulary and authority structures of the target document, what we call domain camouflaged injection, standard detectors fail to flag them, with detection rates dropping from 93.8% to 9.7% on Llama 3.1 8B and from 100% to 55.6% on Gemini 2.0 Flash. We formalize this as the Camouflage Detection Gap (CDG), the difference in injection detection rate between static and camouflaged payloads. Across 45 tasks spanning three domains and two model families, CDG is large and statistically significant (chi^2 = 38.03, p &lt; 0.001 for Llama; chi^2 = 17.05, p &lt; 0.001 for Gemini), with zero reverse discordant pairs in either case. We additionally evaluate Llama Guard 3, a production safety classifier, which detects zero camouflage payloads (IDRcamouflage = 0.000), confirming that the blind spot extends beyond few-shot detectors to dedicated safety classifiers. We further show that multi-agent debate architectures amplify static injection attacks by up to 9.9x on smaller models, while stronger models show collective resistance. Targeted detector augmentation provides only partial remediation (10.2% improvement on Llama, 78.7% on Gemini), suggesting the vulnerability is architectural rather than incidental for weaker models. Our framework, task bank, and payload generator are released publicly.

</details>

---

### [[20_Research/Papers/强化学习/ECPO_Evidence-Coupled_Policy_Optimization_for_Evidence-Certified_Candidate_Ranking|ECPO: Evidence-Coupled Policy Optimization for Evidence-Certified Candidate Ranking]]

![[assets/2605.21993_first_page.png|800]]

- **arXiv**: [2605.21993](https://arxiv.org/abs/2605.21993)
- **PDF**: https://arxiv.org/pdf/2605.21993
- **详细分析**: [[20_Research/Papers/强化学习/ECPO_Evidence-Coupled_Policy_Optimization_for_Evidence-Certified_Candidate_Ranking|ECPO: Evidence-Coupled Policy Optimization for Evidence-Certified Candidate Ranking]]
- **作者**: Miaobo Hu, Shuhao Hu, BoKun Wang, Yina Sa, Xin Wang, Xiaobo Guo, Daren Zha, Jun Xiao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《ECPO: Evidence-Coupled Policy Optimization for Evidence-Certified Candidate Ranking》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ranking systems used in decision-support settings should not only order candidates but also expose evidence that can be independently checked. We study evidence-certified candidate ranking: given an intent_id, a predefined plan skeleton, a window-local candidate roster, and text-derived candidate trajectories with span provenance, a system must output a Top-K list together with doc_id:span evidence certificates whose cited spans are sufficient to recover the decision. We instantiate this task on MAVEN-ERE and RAMS with fixed upstream extraction, window-local randomized candidate identifiers, skeleton-aligned trajectory supervision, hard negatives, and audit references. We introduce Evidence-Coupled Policy Optimization (ECPO), a listwise policy-optimization objective whose action is the joint object of ranking and evidence certificate. ECPO first learns an interpretable trajectory reward from skeleton alignment, argument consistency, and optional graph features; it then optimizes a constrained policy with three coupled rewards: listwise ranking utility, span-level certificate validity, and an evidence-cycle reward computed by a label-free deterministic verifier that reconstructs candidate support from claim-stripped cited spans. This reframes the goal from maximizing ordinary NDCG alone to maximizing CertNDCG and decision-evidence coupling. The evaluation compares ECPO against zero-shot, SFT, and GRPO policies, RM-only scoring with deterministic evidence attachment, grammar/JSON-constrained decoding, validator retry, best-of-N RM selection, and post-hoc evidence rationalization under closed-roster, predicted-roster, and hybrid-roster settings.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Spatiotemporal_Sensitivity_in_Video_LLMs_via_Counterfactual_Reinforcement_Learning|Learning Spatiotemporal Sensitivity in Video LLMs via Counterfactual Reinforcement Learning]]

![[assets/2605.21988_figure.png|800]]

- **arXiv**: [2605.21988](https://arxiv.org/abs/2605.21988)
- **PDF**: https://arxiv.org/pdf/2605.21988
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Spatiotemporal_Sensitivity_in_Video_LLMs_via_Counterfactual_Reinforcement_Learning|Learning Spatiotemporal Sensitivity in Video LLMs via Counterfactual Reinforcement Learning]]
- **作者**: Dazhao Du, Jian Liu, Jialong Qin, Tao Han, Bohai Gu, Fangqi Zhu, Yujia Zhang, Eric Liu, Xi Chen, Song Guo
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Learning Spatiotemporal Sensitivity in Video LLMs via Counterfactual Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ArrowRL, DyBench, MHBench, MVBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video large language models (Video LLMs) achieve strong benchmark accuracy, yet often answer video questions through shortcuts such as single-frame cues and language priors rather than by tracking spatiotemporal dynamics. This issue is exacerbated in RL post-training, where correctness-only rewards can further reinforce shortcut policies that obtain high reward without tracking video dynamics. We address this by asking a controlled counterfactual question: if the visual world changed while the question remained fixed, should the answer change or stay the same? Based on this view, we propose \textbf{Counterfactual Relational Policy Optimization (CRPO)}, a dual-branch RL framework for improving \emph{spatiotemporal sensitivity}. CRPO constructs counterfactual videos through horizontal flips and temporal reversals, trains on both original and counterfactual branches, and introduces a \textbf{Counterfactual Relation Reward (CRR)} between their answers. CRR encourages answers to change for dynamic questions and remain unchanged for static questions. This cross-branch constraint makes it difficult for shortcut policies to be consistently rewarded across both branches. To evaluate this property, we introduce \textbf{DyBench}, a paired counterfactual video benchmark with 3,014 videos covering reversible dynamics, moving direction, and event sequence, together with a strict pair-accuracy metric that prevents fixed-answer shortcuts from inflating scores. Experiments show that CRPO outperforms prior RL methods on spatiotemporal-sensitive evaluations while maintaining competitive general video performance. On Qwen3-VL-8B, CRPO improves DyBench P-Acc by +7.7 and TimeBlind I-Acc by +8.2 over the base model, indicating improved spatiotemporal sensitivity rather than stronger reliance on static shortcuts. The project website can be found at https://ddz16.github.io/crpo.github.io/ .

</details>

---

### [[20_Research/Papers/世界模型/ChronoMedicalWorld_A_Medical_World_Model_for_Learning_Patient_Trajectories_from_Longitudinal_Care_Data|ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data]]

![[assets/2605.21963_first_page.png|800]]

- **arXiv**: [2605.21963](https://arxiv.org/abs/2605.21963)
- **PDF**: https://arxiv.org/pdf/2605.21963
- **详细分析**: [[20_Research/Papers/世界模型/ChronoMedicalWorld_A_Medical_World_Model_for_Learning_Patient_Trajectories_from_Longitudinal_Care_Data|ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data]]
- **作者**: Jiangyuan Wang, Xuyong Chen, Junwei He, Xu Xu, Shasha Xie, Fuman Han
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.02（加权：大模型 0.1，强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

《ChronoMedicalWorld: A Medical World Model for Learning Patient Trajectories from Longitudinal Care Data》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ChronoMedicalWorld, EHRWorld, PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon clinical simulation -- predicting how a patient's physiology evolves over years under specified interventions -- is central to chronic-disease care, yet existing electronic health record (EHR) models are predominantly discriminative, and general-purpose large language models drift under repeated interventions. We propose the \textbf{ChronoMedicalWorld Model (CMWM)}, an action-conditioned latent world-model framework for learning patient trajectories from longitudinal care data. CMWM couples a joint-embedding state encoder with a wide action encoder that admits both structured intervention indicators and free-text communication embeddings, and trains a recurrent latent transition module under a six-term objective: next-observation supervision, next-latent prediction, SIGReg latent regularisation, and three physiology-aware shape priors (slope, continuity, large-jump penalty). A closed-loop rollout-prefix protocol matches training to deployment, so the model is optimised against the same multi-step error it exhibits at inference. As a concrete case study, we instantiate CMWM for annual estimated glomerular filtration rate (eGFR) trajectory forecasting in chronic kidney disease (CKD). On a 2{,}232-patient nephrology cohort, the CKD instantiation achieves a dynamic-50\% history rollout test mean absolute error (MAE) of 7.384 and root-mean-square error (RMSE) of 10.256, against 7.964 and 11.069 for a tuned GPT-5.5 structured-prompting baseline ($-7.28\%$ MAE, $-7.35\%$ RMSE), with the gain dominated by the dialogue portion of patient--health-coach communication. The framework is not CKD-specific: its architecture, loss design, and training protocol apply to any chronic condition that can be cast as periodic clinical state interleaved with structured and conversational interventions.

</details>

---

### [[20_Research/Papers/具身智能/EvoScene-VLA_Evolving_Scene_Beliefs_Inside_the_Action_Decoder_for_Chunked_Robot_Control|EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control]]

![[assets/2605.21862_figure.png|800]]

- **arXiv**: [2605.21862](https://arxiv.org/abs/2605.21862)
- **PDF**: https://arxiv.org/pdf/2605.21862
- **详细分析**: [[20_Research/Papers/具身智能/EvoScene-VLA_Evolving_Scene_Beliefs_Inside_the_Action_Decoder_for_Chunked_Robot_Control|EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control]]
- **作者**: Chushan Zhang, Ruihan Lu, Jinguang Tong, Xuesong Li, Yikai Wang, Hongdong Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《EvoScene-VLA: Evolving Scene Beliefs Inside the Action Decoder for Chunked Robot Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AVA-VLA, EvoScene-VLA, HiF-VLA, LingBot-VLA, MemoryVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Chunked vision-language-action (VLA) policies predict multi-step robot controls, conditioning each update on the current visual observation alone. Yet robot actions cause contact, occlusion, and object motion, and the geometry that later decisions depend on can change before the next visual update arrives. Spatial VLAs improve current-frame geometry. Temporal VLAs aggregate past frames. Neither maintains an action-updated scene prior across chunks. We argue for a persistent action-updated scene state across control calls, and introduce EvoScene-VLA. Its recurrent scene prefix carries a geometry-aware scene state across chunks. At each vision-language model (VLM) call, the VLM combines scene information from the current observation with the action-updated prior from the previous chunk; the action decoder outputs both the next action chunk and a compact scene update. This update becomes the next prior, which the VLM corrects against the new observation when the next call arrives. Each control call therefore starts from a scene prior that reflects both recent actions and fresh visual evidence. During training, \textbf{Scene Predictor} supplies future scene-token targets, and Geometric Anchor aligns scene slots with frozen depth and 3D teachers. We discard both modules at deployment. On 31 RoboTwin tasks, EvoScene-VLA raises average success from 87.2% to 89.1% in fixed evaluation and from 86.1% to 88.5% in randomized evaluation. On the Galaxea R1-Lite real robot, EvoScene-VLA outperforms all baselines.

</details>

---

### [[20_Research/Papers/具身智能/CrossVLA_Cross-Paradigm_Post-Training_and_Inference_Optimization_for_Vision-Language-Action_Models|CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models]]

![[assets/2605.21854_figure.png|800]]

- **arXiv**: [2605.21854](https://arxiv.org/abs/2605.21854)
- **PDF**: https://arxiv.org/pdf/2605.21854
- **详细分析**: [[20_Research/Papers/具身智能/CrossVLA_Cross-Paradigm_Post-Training_and_Inference_Optimization_for_Vision-Language-Action_Models|CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models]]
- **作者**: Zhi Liu
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal

#### 研究背景与动机

《CrossVLA: Cross-Paradigm Post-Training and Inference Optimization for Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ChatVLA, CoT-VLA, CrossVLA, DoRA-on-VLA, FPC-VLA, MT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have rapidly converged on a small set of architectural patterns: discrete-token autoregression (e.g. OpenVLA) and continuous-action flow-matching (e.g. pi-0.5). Yet preference alignment via Direct Preference Optimisation (DPO) -- the de-facto post-training step in language models -- has been studied almost exclusively on autoregressive VLAs. We present CrossVLA, an empirical study of cross-paradigm VLA post-training. Three contributions: (i) a surrogate flow-matching log-probability estimator that lets DPO operate on continuous-action backbones without probability-flow ODE integration; (ii) a head-to-head comparison of LoRA and DoRA as the parameter-efficient layer for VLA DPO, finding DoRA improves over OpenVLA SFT by a mean +10.4 pp across LIBERO 4-suite (600 trials, 3 seeds) -- per-suite +20.0 Object, +11.0 Long-horizon, +8.0 Goal, +2.7 Spatial -- with zero seed variance on Object (38/50 on each of 3 seeds); (iii) an inference-time anatomy showing the denoise loop dominates 78.6% of sample_actions latency and prefix-K/V caching a la VLA-Cache caps at a 21% acceleration ceiling -- both chunk-level and token-level cache strategies degrade success rate to 0-80% in our benchmarks. We further pretrain a multi-view + temporal projection head on 6000 LIBERO frames, achieving 99.5% k-NN recall@1 for same-task retrieval (36x over random), available as a downstream initialisation. All code, ckpts, training logs, and reproduction scripts are open at https://github.com/lz-googlefycy/vla-lab.

</details>

---

### [[20_Research/Papers/大模型/OPPO_Bayesian_Value_Recursion_for_Token-Level_Credit_Assignment_in_LLM_Reasoning|OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning]]

![[assets/2605.21851_figure.png|800]]

- **arXiv**: [2605.21851](https://arxiv.org/abs/2605.21851)
- **PDF**: https://arxiv.org/pdf/2605.21851
- **详细分析**: [[20_Research/Papers/大模型/OPPO_Bayesian_Value_Recursion_for_Token-Level_Credit_Assignment_in_LLM_Reasoning|OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning]]
- **作者**: Yu Li, Rui Miao, Tian Lan, Zhengling Qi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《OPPO: Bayesian Value Recursion for Token-Level Credit Assignment in LLM Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TreeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards has become the standard recipe for improving LLM reasoning, but the dominant algorithm GRPO assigns a single trajectory-level advantage to every token, diluting the signal at pivotal reasoning steps and injecting noise at uninformative ones. Critic-free alternatives derived from on-policy distillation supply per-token signals through oracle-conditioned likelihood ratios, yet apply each signal in isolation from the trajectory-level evidence accumulated up to that position. We propose Oracle-Prompted Policy Optimization (OPPO), which rests on a single observation: the oracle signal used by prior distillation-style methods for local discrimination is also the natural Bayesian update of the model's belief about eventual success. Accumulating the signal along a trajectory yields, in closed form and at the cost of one extra forward pass, a running estimate of the success probability at every position, together with a token-level advantage that requires no learned value network and no additional rollouts. A first-order analysis factorizes the advantage into the per-token discrimination signal used by distillation methods modulated by a state weight that concentrates credit on genuinely pivotal tokens, with a directional variance-reduction guarantee. The framework admits two estimators differing only in which model scores the evidence: a \textit{self-oracle} that reuses the student and recovers the on-policy distillation reward as a strict special case, and a \textit{teacher-oracle} that delegates scoring to a stronger frozen model. On two base LLMs across seven mathematics, science, and code reasoning benchmarks, OPPO improves over GRPO, DAPO, and SDPO by up to $+6.0$ points on AMC'23 and $+5.2$ points on AIME'24, with gains that widen monotonically with response length.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Altruistic_Collaboration_in_Heterogeneous_Multi-Team_Systems|Learning Altruistic Collaboration in Heterogeneous Multi-Team Systems]]

![[assets/2605.21723_figure.png|800]]

- **arXiv**: [2605.21723](https://arxiv.org/abs/2605.21723)
- **PDF**: https://arxiv.org/pdf/2605.21723
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Altruistic_Collaboration_in_Heterogeneous_Multi-Team_Systems|Learning Altruistic Collaboration in Heterogeneous Multi-Team Systems]]
- **作者**: Riwa Karam, Ruoyu Lin, Brooks A. Butler, Magnus Egerstedt
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Learning Altruistic Collaboration in Heterogeneous Multi-Team Systems》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies heterogeneous multi-team collaboration through dynamic robot allocation, where robots are treated as transferable resources. Leveraging Hamilton's rule from ecology as an altruistic decision-making mechanism, we propose a multi-team collaborative resource allocation framework with heterogeneous capabilities, transfer costs, and capability-dependent contributions. The resulting allocation problem is combinatorial and is shown to be NP-hard. To address scalability, we develop a graph neural network policy under centralized training and decentralized execution that approximates the altruistic allocations based on Hamilton's rule. The model operates over the team interaction graph and predicts robot-level transfer decisions and next robot-to-team assignments. The proposed approach is validated in a firefighting scenario through simulations and experiments, demonstrating that the learned policy achieves near-optimal performance while scaling to larger systems.

</details>

---

### [[20_Research/Papers/大模型/Value-Gradient_Hypothesis_of_RL_for_LLMs|Value-Gradient Hypothesis of RL for LLMs]]

![[assets/2605.21654_figure.png|800]]

- **arXiv**: [2605.21654](https://arxiv.org/abs/2605.21654)
- **PDF**: https://arxiv.org/pdf/2605.21654
- **详细分析**: [[20_Research/Papers/大模型/Value-Gradient_Hypothesis_of_RL_for_LLMs|Value-Gradient Hypothesis of RL for LLMs]]
- **作者**: Arip Asadulaev, Daniil Ognev, Karim Salta, Martin Takac
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Value-Gradient Hypothesis of RL for LLMs》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning substantially improves pretrained language models, but it remains understudied why critic-free methods such as PPO and GRPO work as well as they do, and when they should provide the largest gains. We develop a value-gradient perspective of critic-free RL for LLM post-training. First, under a differentiable rollout and additive-noise parameterization, we show that the actor update is value-gradient-like in expectation: the backward pass propagates costates whose conditional expectation equals the value gradient. Second, for discrete transformer policies, we show that autodifferentiation through attention produces empirical costates that approximate this value signal, with an error controlled by the sampling gap and policy entropy. These results motivate a decomposition of RL impact into value gradient signal and reachable reward headroom, yielding a criterion for when RL should be most effective along a pretraining trajectory.

</details>

---

### [[20_Research/Papers/其他/TO-Agents_A_Multi-Agent_AI_Pipeline_for_Preference-Guided_Topology_Optimization|TO-Agents: A Multi-Agent AI Pipeline for Preference-Guided Topology Optimization]]

![[assets/2605.21622_figure.png|800]]

- **arXiv**: [2605.21622](https://arxiv.org/abs/2605.21622)
- **PDF**: https://arxiv.org/pdf/2605.21622
- **详细分析**: [[20_Research/Papers/其他/TO-Agents_A_Multi-Agent_AI_Pipeline_for_Preference-Guided_Topology_Optimization|TO-Agents: A Multi-Agent AI Pipeline for Preference-Guided Topology Optimization]]
- **作者**: Isabella A. Stewart, Hongrui Chen, Faez Ahmed
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《TO-Agents: A Multi-Agent AI Pipeline for Preference-Guided Topology Optimization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Topology optimization can generate efficient structures, but designers often must manually translate qualitative intent, such as desired visual style, product experience, or manufacturability into solver settings that are not directly tied to those preferences. We present TO-Agents, a multi-agent AI framework that connects natural-language design intent with iterative topology optimization. The framework converts a human-provided problem description into validated solver inputs, runs a topology optimization solver, renders the resulting 3D topology, and uses multi-view vision-language reasoning with an independent judge agent to critique each result and revise solver parameters. We evaluate the framework on two long-horizon design tasks: a cantilever beam benchmark and a phone-stand product design. In both tasks, the designer specifies an aesthetic preference for hierarchically branched structures inspired by natural tree morphologies, and the system performs four revision cycles across ten independent replicates. TO-Agents produces at least one preference-aligned design in 60% of trials for each case study, corresponding to up to 6x more successful trials than an ablated pipeline without visual or historical feedback. Judge scores and human evaluations show that the pipeline can identify effective parameter levers, recover from poor revisions, and expand design exploration. A manufacturing agent further post-processes top-ranked designs for additive manufacturing, enabling end-to-end intent-to-prototype design. We also identify failure modes, including overshooting, selective memory, misplaced tools, and incorrect parameter reasoning. These results suggest that agentic topology optimization can shift designers from low-level parameter tuning toward higher-level specification of form and function, while highlighting safeguards needed for reliable autonomous engineering design.

</details>

---

### [[20_Research/Papers/强化学习/Scalable_On-Policy_Reinforcement_Learning_via_Adaptive_Batch_Scaling|Scalable On-Policy Reinforcement Learning via Adaptive Batch Scaling]]

![[assets/2605.21557_figure.png|800]]

- **arXiv**: [2605.21557](https://arxiv.org/abs/2605.21557)
- **PDF**: https://arxiv.org/pdf/2605.21557
- **详细分析**: [[20_Research/Papers/强化学习/Scalable_On-Policy_Reinforcement_Learning_via_Adaptive_Batch_Scaling|Scalable On-Policy Reinforcement Learning via Adaptive Batch Scaling]]
- **作者**: Jongchan Park
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Scalable On-Policy Reinforcement Learning via Adaptive Batch Scaling》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventional wisdom holds that large-batch training is fundamentally incompatible with Reinforcement Learning (RL) - beyond a modest threshold, increasing batch sizes typically yields diminishing returns or performance degradation due to the inherent non-stationarity of the data distribution. We challenge this view by observing that non-stationarity is not a fixed property of RL, but evolves throughout training: early stages exhibit rapid behavioral shifts that demand small batches for plasticity, whereas late stages approach a quasi-stationary regime where large batches enable precise convergence. Motivated by this observation, we propose Adaptive Batch Scaling (ABS), that dynamically adjusts the effective batch size according to the stability of the learning policy. Central to ABS is Behavioral Divergence, a novel metric that quantifies policy non-stationarity by measuring action-level shifts between consecutive updates, which we use to scale batch size inversely to policy volatility. Integrated with the Parallelised Q-Network (PQN) algorithm and evaluated on the ALE benchmark, ABS seamlessly reconciles early-stage plasticity with late-stage stable convergence. Strikingly, contrary to conventional wisdom, our results reveal that the combination of larger networks and larger batch sizes achieves the best performance - a scaling behavior previously thought to be unattainable in RL, now unlocked through adaptive batch control.

</details>

---

### [[20_Research/Papers/大模型/Autonomous_LLM_Agents_&_CTFs_A_Second_Look|Autonomous LLM Agents & CTFs: A Second Look]]

![[assets/2605.21497_figure.png|800]]

- **arXiv**: [2605.21497](https://arxiv.org/abs/2605.21497)
- **PDF**: https://arxiv.org/pdf/2605.21497
- **详细分析**: [[20_Research/Papers/大模型/Autonomous_LLM_Agents_&_CTFs_A_Second_Look|Autonomous LLM Agents & CTFs: A Second Look]]
- **作者**: Youness Bouchari, Matteo Boffa, Marco Mellia, Idilio Drago, Thanh Minh Bui, Dario Rossi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Autonomous LLM Agents & CTFs: A Second Look》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents are increasingly proposed to automate offensive security tasks, with recent studies reporting near human-level success rates in Capture-the-Flag (CTF) challenges. We here revisit these results, providing a second look at these claims. We engineer different agent architectures of increasing complexity and modularity on 30 web-based CTFs challenges spanning 14 vulnerability classes. We instantiate these agents with multiple LLM backbones, and compare them with claude-code, a general-purpose agent that automatically determines its internal architecture. Our evaluation yields three main findings. First, claude-code achieves performance comparable to the engineered architectures (19/30 solved tasks), suggesting that general-purpose agents are strong baselines for offensive security tasks. Second, both our architectures and claude-code struggle in the same challenge categories, revealing persistent barriers that keep current agents below human-level capability. Third, by leveraging our manually designed architectures we can systematically measure the impact of additional components, finding that structured orchestration of specialized roles outperforms monolithic designs, improving run-to-run consistency, and reducing execution costs.

</details>

---

### [[20_Research/Papers/大模型/HealthCraft_A_Reinforcement_Learning_Safety_Environment_for_Emergency_Medicine|HealthCraft: A Reinforcement Learning Safety Environment for Emergency Medicine]]

![[assets/2605.21496_figure.png|800]]

- **arXiv**: [2605.21496](https://arxiv.org/abs/2605.21496)
- **PDF**: https://arxiv.org/pdf/2605.21496
- **详细分析**: [[20_Research/Papers/大模型/HealthCraft_A_Reinforcement_Learning_Safety_Environment_for_Emergency_Medicine|HealthCraft: A Reinforcement Learning Safety Environment for Emergency Medicine]]
- **作者**: Brandon Dent
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.25，强化学习 0.76，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《HealthCraft: A Reinforcement Learning Safety Environment for Emergency Medicine》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HealthBench, MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier language models are being deployed into clinical workflows faster than the infrastructure to evaluate them safely. Static medical-QA benchmarks miss the failure modes that matter in emergency medicine: trajectory-level safety collapse, tool misuse, and capitulation under sustained clinical pressure. We present HealthCraft, the first public reinforcement-learning environment that rewards trajectory-level safety under realistic emergency-medicine conditions, adapted from Corecraft. It is built on a FHIR R4 world state with 14 entity types and 3,987 seed entities, exposes 24 MCP tools, and defines a dual-layer rubric that zeroes reward whenever any safety-critical criterion is violated. We release 195 tasks across six categories, graded against 2,255 binary criteria (515 safety-critical); a post-hoc 10-task negative-class slate extends this to 205 tasks and 2,337 criteria. V8 results on two frontier models show Claude Opus 4.6 at Pass@1 24.8% [21.5-28.4] and GPT-5.4 at 12.6% [10.2-15.6], with safety-failure rates of 27.5% and 34.0%. On multi-step workflows - the closest proxy to real emergency care - performance collapses to near zero (Claude 1.0%, GPT-5.4 0.0%) despite partial competence on individual steps. Six infrastructure bugs fixed between pilots v2 and v8 re-ordered which model "looks stronger," evidence that infrastructure fidelity is part of the measurement. A deterministic LLM-judge overlay bounds evaluator noise, and a 60-run negative-class smoke pilot shows the reward signal is not drop-in training-safe: restraint criteria pass at 0.929 prevalence, a gameability an eval harness can tolerate but a training reward cannot. We scaffold coupling to a Megatron+SGLang+GRPO loop per Corecraft Section 5.2 and leave training-reward ablations as future work. Environment, tasks, rubrics, and harness are released under Apache 2.0.

</details>

---

### [[20_Research/Papers/强化学习/Memory-Induced_Supra-Competitive_Outcomes_Between_Deep_Reinforcement_Learning_Agents_in_Optimal_Trade_Execution|Memory-Induced Supra-Competitive Outcomes Between Deep Reinforcement Learning Agents in Optimal Trade Execution]]

![[assets/2605.20348_figure.png|800]]

- **arXiv**: [2605.20348](https://arxiv.org/abs/2605.20348)
- **PDF**: https://arxiv.org/pdf/2605.20348
- **详细分析**: [[20_Research/Papers/强化学习/Memory-Induced_Supra-Competitive_Outcomes_Between_Deep_Reinforcement_Learning_Agents_in_Optimal_Trade_Execution|Memory-Induced Supra-Competitive Outcomes Between Deep Reinforcement Learning Agents in Optimal Trade Execution]]
- **作者**: Christos Spyridon Koulouris, Carlo Campajola
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.7（加权：大模型 0.5，强化学习 1.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Memory-Induced Supra-Competitive Outcomes Between Deep Reinforcement Learning Agents in Optimal Trade Execution》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we investigate whether deep reinforcement-learning agents interacting in a shared optimal-execution environment can sustain supra-competitive outcomes, in the sense of achieving lower implementation shortfalls than the relevant game-theoretical competitive benchmark. We study a two-agent Almgren-Chriss liquidation game and examine how learned behavior depends on intra-episode environment feedback, the ability to interpret the mid-price and the agent's knoledge of the past. We first use ex-ante schedule-learning agents to remove intra-episode feedback and isolate what can arise when agents commit to complete liquidation trajectories before execution begins. We then allow agents to condition on the evolving state using a variety of DDQN architectures. We find that, when agents are given access to intra-episode history, especially recent prices and own past actions, supra-competitive outcomes become substantially more frequent and more persistent. These findings indicate that supra-competitive behavior in this execution game is driven not by multi-agent learning or by current price observation alone, but by feedback, memory, and state-contingent interaction along the realized execution path.

</details>

---

### [[20_Research/Papers/强化学习/Recursive_Entropic_Risk_Optimization_in_Discounted_MDPs_Sample_Complexity_Bounds_with_a_Generative_Model|Recursive Entropic Risk Optimization in Discounted MDPs: Sample Complexity Bounds with a Generative Model]]

![[assets/2506.00286_figure.png|800]]

- **arXiv**: [2506.00286](https://arxiv.org/abs/2506.00286)
- **PDF**: https://arxiv.org/pdf/2506.00286
- **详细分析**: [[20_Research/Papers/强化学习/Recursive_Entropic_Risk_Optimization_in_Discounted_MDPs_Sample_Complexity_Bounds_with_a_Generative_Model|Recursive Entropic Risk Optimization in Discounted MDPs: Sample Complexity Bounds with a Generative Model]]
- **作者**: Oliver Mortensen, Mohammad Sadegh Talebi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Recursive Entropic Risk Optimization in Discounted MDPs: Sample Complexity Bounds with a Generative Model》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study risk-sensitive reinforcement learning in finite discounted MDPs with recursive entropic risk measures (ERM), where the risk parameter $β\neq 0$ controls the agent's risk attitude: $β&gt;0$ for risk-averse and $β&lt;0$ for risk-seeking behavior. A generative model of the MDP is assumed to be available. Our focus is on the sample complexities of learning the optimal state-action value function (value learning) and an optimal policy (policy learning) under recursive ERM. We introduce a model-based algorithm, called Model-Based ERM $Q$-Value Iteration (MB-RS-QVI), and derive PAC-type bounds on its sample complexity for both value and policy learning. Both PAC bounds scale exponentially with $|β|/(1-γ)$, where $γ$ is the discount factor. We also establish corresponding lower bounds for both value and policy learning, showing that exponential dependence on $|β|/(1-γ)$ is unavoidable in the worst case. The bounds are tight in the number of states and actions ($S$ and $A$), providing the first rigorous sample complexity guarantees for recursive ERM across both risk-averse and risk-seeking regimes.

</details>

---
