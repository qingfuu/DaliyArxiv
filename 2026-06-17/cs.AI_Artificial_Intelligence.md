# cs.AI | Artificial Intelligence | 2026-06-17

#arxiv #ComputerScience

**论文数**: 37

### [[20_Research/Papers/强化学习/Visual_Verification_Enables_Inference-time_Steering_and_Autonomous_Policy_Improvement|Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement]]

![[assets/2606.18247_first_page.png|800]]

- **arXiv**: [2606.18247](https://arxiv.org/abs/2606.18247)
- **PDF**: https://arxiv.org/pdf/2606.18247
- **详细分析**: [[20_Research/Papers/强化学习/Visual_Verification_Enables_Inference-time_Steering_and_Autonomous_Policy_Improvement|Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement]]
- **作者**: Mingtong Zhang, Dhruv Shah
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Visual Verification Enables Inference-time Steering and Autonomous Policy Improvement》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots deployed in the real world should learn from their experience and improve over time. This requires a mechanism of practicing and learning from feedback. In this paper, we propose VERITAS, a generator-verifier framework for generalist robot policies for inference-time policy steering and self-improvement. We use a pre-trained generalist robot policy as a ``generator'' and pair it with a gradient-free ``visual verifier'' that evaluates actions at inference time. This framework enables inference-time steering that improves policy performance without additional training. We demonstrate that inference-time verification consistently outperforms vanilla generalists without training on additional demonstration data. Additionally, we demonstrate that the verified rollouts provide effective supervision for offline policy improvement: policies fine-tuned on verified self-generated trajectories achieve consistent performance gains. Notably, we find that post-training with verified rollouts achieves comparable efficiency to expert demonstrations, while requiring no human interventions. Our results highlight inference-time verification as a practical and scalable mechanism for improving robotic policies during deployment.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Red_Agent_Policy_from_Observations_for_Neurosymbolic_Autonomous_Cyber_Agents|Learning Red Agent Policy from Observations for Neurosymbolic Autonomous Cyber Agents]]

![[assets/2606.18223_figure.png|800]]

- **arXiv**: [2606.18223](https://arxiv.org/abs/2606.18223)
- **PDF**: https://arxiv.org/pdf/2606.18223
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Red_Agent_Policy_from_Observations_for_Neurosymbolic_Autonomous_Cyber_Agents|Learning Red Agent Policy from Observations for Neurosymbolic Autonomous Cyber Agents]]
- **作者**: Ankita Samaddar, Sandeep Neema, Daniel Balasubramanian, Xenofon Koutsoukos
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Learning Red Agent Policy from Observations for Neurosymbolic Autonomous Cyber Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With sophisticated cyber-attacks becoming increasingly prevalent, modern networks require intelligent autonomous cyber-defense agents trained via Reinforcement Learning (RL). These agents employ neurosymbolic approaches such as behavior trees with learning-enabled components (LECs) to learn, reason, adapt, and implement security rules while maintaining critical operations. However, these autonomous networks are partially observable systems, i.e., the cyber-attacker's (red agent's) actions are not observable, making it difficult for the defender to predict red actions, learn red policies, or assess the attacker's intrusion levels. To address this, we propose a Policy Learning Technique using imitation learning to learn policies for partially observable RL agents with discrete states and discrete actions. We apply this technique in an autonomous cyber environment to predict red agent's actions from network observations and defender actions. Integrated with a neurosymbolic cyber-defense agent, our method effectively handles different red policies and achieves high prediction accuracy across diverse simulated scenarios.

</details>

---

### [[20_Research/Papers/世界模型/Looped_World_Models|Looped World Models]]

![[assets/2606.18208_figure.png|800]]

- **arXiv**: [2606.18208](https://arxiv.org/abs/2606.18208)
- **PDF**: https://arxiv.org/pdf/2606.18208
- **详细分析**: [[20_Research/Papers/世界模型/Looped_World_Models|Looped World Models]]
- **作者**: Hongyuan Adam Lu, Z.L. Victor Wei, Qun Zhang, Jinrui Zeng, Bowen Cao, Lingwei Meng, Mocheng Li, Zezhong Wang, Haonan Yin, Naifu Xue, Minyu Chen, Cenyuan Zhang...
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: cs.AI

#### 研究背景与动机

《Looped World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AlfWorld, PlaNet, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current world models face a fundamental tension: faithful long-horizon simulation demands deep computation, but deeper models are expensive to deploy and prone to compounding errors. We resolve this by introducing Looped World Models (LoopWM), which are the first looped architectures for world modelling. Our method iteratively refines latent environment states through a parameter-shared transformer block. This yield up to 100x parameter efficiency over conventional approaches with adaptive computation that automatically scales depth to match the complexity of each prediction step. Orthogonal to scaling model size and training data, LoopWM establishes iterative latent depth as a new scaling axis for world simulation, which might significantly push the community forward.

</details>

---

### [[20_Research/Papers/大模型/RubricsTree_Scalable_and_Evolving_Open-Ended_Evaluation_of_Personal_Health_Agents_across_Health_Memory_and_Medical_Skills|RubricsTree: Scalable and Evolving Open-Ended Evaluation of Personal Health Agents across Health Memory and Medical Skills]]

![[assets/2606.18203_figure.png|800]]

- **arXiv**: [2606.18203](https://arxiv.org/abs/2606.18203)
- **PDF**: https://arxiv.org/pdf/2606.18203
- **详细分析**: [[20_Research/Papers/大模型/RubricsTree_Scalable_and_Evolving_Open-Ended_Evaluation_of_Personal_Health_Agents_across_Health_Memory_and_Medical_Skills|RubricsTree: Scalable and Evolving Open-Ended Evaluation of Personal Health Agents across Health Memory and Medical Skills]]
- **作者**: Weizhi Zhang, Zechen Li, Hamid Palangi, Ben Graef, A. Ali Heydari, Simon A. Lee, Salman Rahman, Ray Luo, Zeinab Esmaeilpour, Erik Schenck, Chloe Zhang, Yamin Li...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《RubricsTree: Scalable and Evolving Open-Ended Evaluation of Personal Health Agents across Health Memory and Medical Skills》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Auto-Eval, HealthBench, MedMCQA, MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The LLM-empowered personal health agents with user health (sensor) metrics have offered a promising pathway to alleviate global disparities in healthcare access. However, large-scale clinical deployment remains constrained by an open-ended evaluation bottleneck: physician annotation is reliable but costly and unscalable, while LLM-as-a-judge evaluators are scalable but subjective, inconsistent, and sometimes clinically misaligned. We introduce RubricsTree, a scalable evaluation framework with an expert-aligned hierarchical taxonomy of over 100 atomic, clinically-verifiable Boolean rubrics, evolving from the insights of 4,000 real user queries through an iterative human-in-the-loop curation protocol with an expertise panel led by an experienced physician. A context-aware adaptive router activates only the relevant auto-weighted rubric subset per query, providing the throughput needed for scalable evaluation with expert-aligned quality. Through a systematic meta-evaluation, we show that RubricsTree (i) substantially exceeds a strong large-scale evaluation baseline in expert alignment on challenging open-ended queries; (ii) reliably penalizes contextually degraded responses; and (iii) when used as structured instructions, text feedback, or training rewards for performance optimization, yields up to ~66% relative gains on HealthBench for Gemini, GPT, and Qwen model families. RubricsTree thus provides a scalable, auditable, and evolving evaluation infrastructure required for the continuous optimization of product-level personal healthcare AI.

</details>

---

### [[20_Research/Papers/具身智能/Memory_as_a_Wasting_Asset_Pricing_Flash_Endurance_for_Embodied_Agents,_and_the_Limits_of_Doing_So|Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So]]

![[assets/2606.18144_figure.png|800]]

- **arXiv**: [2606.18144](https://arxiv.org/abs/2606.18144)
- **PDF**: https://arxiv.org/pdf/2606.18144
- **详细分析**: [[20_Research/Papers/具身智能/Memory_as_a_Wasting_Asset_Pricing_Flash_Endurance_for_Embodied_Agents,_and_the_Limits_of_Doing_So|Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So]]
- **作者**: Josef Liyanjun Chen
- **cs 子类**: cs.AI, cs.CY, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Memory as a Wasting Asset: Pricing Flash Endurance for Embodied Agents, and the Limits of Doing So》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot's flash endurance is a non-renewable stock: every persisted write spends one of a few thousand program/erase cycles and never refills, yet no fielded robot memory system prices which memories are worth an erase cycle. We treat embodied memory as depreciating capital and price that stock with a single endurance shadow price $\eta$, which makes cost-minimizing placement across a RAM / on-board NVM / cloud hierarchy a threshold in a wear-augmented per-byte index. The index is cost-optimal whatever the sign of the value-write association $\chi$; only when $\chi &gt; 0$ does the optimum turn non-monotone, sending a robot's most valuable memories off its flash. The pivot is thus empirical, and we measure $\chi$ on real robot logs at a pre-specified gate: its sign is a property of the deployment regime -- positive on recurrent long-horizon manipulation ($\hat{\chi} \approx +1.0 \times 10^{-3}$, replicated at full power), null on a shorter-horizon suite, and negative on non-recurrent teleoperation. Two boundaries scope the result. The endurance budget is dormant on premium 3,000-P/E TLC at datasheet prices and binding on the commodity QLC/eMMC ($\sim$1,000 P/E) that cheaper edge robots run. And where it binds, a learned wear-aware controller only ties price-based routing on task value, because realized value is tier-invariant across RAM, NVM, and cloud: the rent governs device lifetime and cost, not task performance. Whether wear-aware placement improves task value remains open -- $\chi$ is measured against a value proxy, and the non-monotone optimum, while proven, is not yet observed in data.

</details>

---

### [[20_Research/Papers/大模型/Your_AI_Travel_Agent_Would_Book_You_a_Bullfight_An_Agentic_Benchmark_for_Implicit_Animal_Welfare_in_Frontier_AI_Models|Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models]]

![[assets/2606.18142_figure.png|800]]

- **arXiv**: [2606.18142](https://arxiv.org/abs/2606.18142)
- **PDF**: https://arxiv.org/pdf/2606.18142
- **详细分析**: [[20_Research/Papers/大模型/Your_AI_Travel_Agent_Would_Book_You_a_Bullfight_An_Agentic_Benchmark_for_Implicit_Animal_Welfare_in_Frontier_AI_Models|Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models]]
- **作者**: Jasmine Brazilek, Oliver Tulio, Joel Christoph, Miles Tidmarsh, Carol Kline, Arturs Kanepajs
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Your AI Travel Agent Would Book You a Bullfight: An Agentic Benchmark for Implicit Animal Welfare in Frontier AI Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：SpeciesismBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents are moving from advisors to actors, booking travel, planning menus, and running procurement on behalf of users. Existing benchmarks for AI and animal welfare evaluate model text responses to question-answer prompts, leaving open whether the welfare reasoning surfaced in those responses transfers to agentic deployment where the model must take actions with tools. We introduce TAC (Travel Agent Compassion), the first agentic benchmark measuring whether AI agents avoid options involving animal exploitation when acting on behalf of users. TAC presents an AI agent with twelve hand-authored travel booking scenarios across six categories of animal exploitation, augmented to forty-eight samples to control for price, rating, and position confounds. We evaluate seven frontier models from four labs. Every model scores below the chance level of sixty-four percent, with the best performer (Claude Opus 4.7) at fifty-three percent. A single welfare-aware sentence in the system prompt yields gains of forty-seven to sixty-three percentage points in Claude and GPT-5.5, twenty-six points in GPT-5.2, and under twelve points in DeepSeek and Gemini. An auxiliary Inspect Scout audit of 288 base-condition transcripts from the top two performers, using Gemini 2.5 Flash Lite as judge, flags zero transcripts for evaluation awareness, suggesting the below-chance rates do not stem from the models recognising the evaluation. We discuss implications for category-level variation across cultural domains, the limits of text-response welfare benchmarks, and the EU General-Purpose AI Code of Practice systemic risk framework.

</details>

---

### [[20_Research/Papers/具身智能/Knowledge_Reutilization_in_Meta-Reinforcement_Learning|Knowledge Reutilization in Meta-Reinforcement Learning]]

![[assets/2606.18132_first_page.png|800]]

- **arXiv**: [2606.18132](https://arxiv.org/abs/2606.18132)
- **PDF**: https://arxiv.org/pdf/2606.18132
- **详细分析**: [[20_Research/Papers/具身智能/Knowledge_Reutilization_in_Meta-Reinforcement_Learning|Knowledge Reutilization in Meta-Reinforcement Learning]]
- **作者**: Yuan Meng, Bo Wang, Juan de los Rios Ruiz, Xiangtong Yao, Zhenshan Bing, Fuchun Sun, Alois Knoll
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Knowledge Reutilization in Meta-Reinforcement Learning》归入 强化学习、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Meta-reinforcement learning enables fast adaptation by extracting shared structure from related tasks, but existing end-to-end methods often couple task inference with embodiment-specific control. This coupling can obscure non-parametric task semantics, reduce sample efficiency, and limit cross-agent reuse. We propose a meta-knowledge reutilization framework that learns task-level knowledge on a dynamics-simplified agent and transfers it to heterogeneous agents. The framework uses a Bayesian non-parametric prior to organize latent task modes and a high-level policy to generate task-level magnitude guidance. To bridge reusable task knowledge with different embodiments, we introduce a semantic-magnitude interface and a lightweight temporal adaptor, which convert frozen meta-knowledge into temporally aligned subgoals for embodiment-specific low-level controllers. Experiments on multiple locomotion agents show that our framework reduces final-step tracking error by 94.75% -- 99.79% compared with recent state-of-the-art baselines and achieves comparable deployment performance with about 23.8% of their interaction data.

</details>

---

### [[20_Research/Papers/大模型/Structural_Role_Injection_in_Handlebars-Templated_LLM_Prompts_Triple-Brace_Interpolation,_Delimiter_Family,_and_the_Limits_of_HTML_Auto-Esca|Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping]]

![[assets/2606.18120_figure.png|800]]

- **arXiv**: [2606.18120](https://arxiv.org/abs/2606.18120)
- **PDF**: https://arxiv.org/pdf/2606.18120
- **详细分析**: [[20_Research/Papers/大模型/Structural_Role_Injection_in_Handlebars-Templated_LLM_Prompts_Triple-Brace_Interpolation,_Delimiter_Family,_and_the_Limits_of_HTML_Auto-Esca|Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping]]
- **作者**: Mohammadreza Rashidi
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《Structural Role Injection in Handlebars-Templated LLM Prompts: Triple-Brace Interpolation, Delimiter Family, and the Limits of HTML Auto-Escaping》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model applications build prompts from templates, and Handlebars is a widely used templating engine and the default prompt-template format in Microsoft Semantic Kernel. Its double-brace {x} expression HTML-escapes the interpolated value and is documented as the safe default; its triple-brace {x} expression inserts the value raw. We show that this choice silently governs an application's exposure to structural role injection, where attacker-controlled data carries chat role delimiters that forge a higher-privilege turn. A model-free analysis establishes the mechanism: Handlebars escaping rewrites angle brackets but not square brackets, colons, or Markdown hashes, so it neutralises ChatML, Llama-3, and XML role delimiters (survival rate 0.00) while leaving Llama-2 [INST], legacy Human:/Assistant:, and Markdown ### delimiters intact (survival rate 1.00 for the last two). We then run 5760 trials across seven delimiter families, two attack objectives, and four models (GPT-3.5 Turbo, GPT-4o mini, GPT-4.1 mini, Claude Haiku 4.5) at a combined API cost of 1.63 USD. GPT-3.5 Turbo follows the task-hijack instruction in 97% of raw and 91% of escaped trials, with the escaping protection concentrated in the angle-bracket families and absent for the colon- and Markdown-based families; the harder secret-exfiltration objective, which does not saturate, exposes the same family interaction more cleanly. Claude Haiku 4.5 resists both objectives almost entirely. The escaped default protects only the delimiter schemes whose characters HTML escaping happens to cover, gives no protection for the rest, and cannot substitute for a structural separation of instruction and data.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Fair_Pareto-Optimal_Policies_in_Multi-Objective_Reinforcement_Learning|Learning Fair Pareto-Optimal Policies in Multi-Objective Reinforcement Learning]]

![[assets/2606.18111_figure.png|800]]

- **arXiv**: [2606.18111](https://arxiv.org/abs/2606.18111)
- **PDF**: https://arxiv.org/pdf/2606.18111
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Fair_Pareto-Optimal_Policies_in_Multi-Objective_Reinforcement_Learning|Learning Fair Pareto-Optimal Policies in Multi-Objective Reinforcement Learning]]
- **作者**: Umer Siddique, Peilang Li, Yongcan Cao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Learning Fair Pareto-Optimal Policies in Multi-Objective Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FPbRL, MARL, MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fairness is an important aspect of decision-making in multi-objective reinforcement learning (MORL), where policies must ensure both optimality and equity across multiple, potentially conflicting objectives. While single-policy MORL methods can learn fair policies for fixed user preferences using welfare functions such as the generalized Gini welfare function (GGF), they fail to provide the diverse set of policies necessary for dynamic or unknown user preferences. To address this limitation, we formalize the fair optimization problem in multi-policy MORL, where the goal is to learn a set of Pareto-optimal policies that ensure fairness across all possible user preferences. Our key technical contributions are threefold: (1) We show that for concave, piecewise-linear welfare functions (e.g., GGF), fair policies remain in the convex coverage set (CCS), which is an approximated Pareto front for linear scalarization. (2) We demonstrate that non-stationary policies, augmented with accrued reward histories, and stochastic policies improve fairness by dynamically adapting to historical inequities. (3) We propose three novel algorithms, which include integrating GGF with multi-policy multi-objective Q-Learning (MOQL), state-augmented multi-policy MOQL for learning non-statoinary policies, and its novel extension for learning stochastic policies. We evaluate our algorithms across various domains and compare our methods against the state-of-the-art MORL baselines. The empirical results show that our methods learn a set of fair policies that accommodate different user preferences.

</details>

---

### [[20_Research/Papers/机器人/EAGG_Embodiment-Aligned_Grasp_Generation_via_Geometry-Aware_Graph_Conditioning|EAGG: Embodiment-Aligned Grasp Generation via Geometry-Aware Graph Conditioning]]

![[assets/2606.18092_figure.jpg|800]]

- **arXiv**: [2606.18092](https://arxiv.org/abs/2606.18092)
- **PDF**: https://arxiv.org/pdf/2606.18092
- **详细分析**: [[20_Research/Papers/机器人/EAGG_Embodiment-Aligned_Grasp_Generation_via_Geometry-Aware_Graph_Conditioning|EAGG: Embodiment-Aligned Grasp Generation via Geometry-Aware Graph Conditioning]]
- **作者**: Wanhao Niu, Qiyan Ke, Yuan Sun, Hao Sun, Jie Xu, Muyuan Ma, Ruiqi Hu, Fuchun Sun
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《EAGG: Embodiment-Aligned Grasp Generation via Geometry-Aware Graph Conditioning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, Dex-Net, DexGraspNet, GraspNet, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-end-effector grasp generation seeks a unified model that generalizes across objects and across embodiments ranging from parallel grippers to dexterous end effectors. Existing grasp generators are typically designed for a fixed embodiment or encode embodiment identity with a static descriptor, which weakens transfer when topology, actuation coupling, and contact geometry differ substantially. We present EAGG, an embodiment-aligned grasp generator that represents each embodiment with a topology-aware end-effector graph and an embodiment-specific low-dimensional end-effector control space. A frozen end-effector-cognition backbone converts the current articulated state into geometry-aware tokens that act as a reusable morphology prior, and iterative geometry injection refreshes these tokens throughout sampling so that conditioning remains synchronized with the evolving end-effector geometry. On the MultiGripperGrasp benchmark, EAGG reaches 56.17% average success across six training end effectors, remaining within 1.10 percentage points of specialized training while preserving transfer to finetuning and zero-shot end effectors. Iterative geometry injection further reduces the pooled median contact distance from 0.239 cm to 0.189 cm. These results show that cross-end-effector grasp generation is strengthened by aligning embodiment structure inside a shared generator rather than suppressing embodiment differences. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/ProvenanceGuard_Source-Aware_Factuality_Verification_for_MCP-Based_LLM_Agents|ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents]]

![[assets/2606.18037_first_page.png|800]]

- **arXiv**: [2606.18037](https://arxiv.org/abs/2606.18037)
- **PDF**: https://arxiv.org/pdf/2606.18037
- **详细分析**: [[20_Research/Papers/大模型/ProvenanceGuard_Source-Aware_Factuality_Verification_for_MCP-Based_LLM_Agents|ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents]]
- **作者**: Ander Alvarez, Santhiya Rajan, Samuel Mugel, Román Orús
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ProvenanceGuard: Source-Aware Factuality Verification for MCP-Based LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AttributedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using LLM agents increasingly use the Model Context Protocol (MCP) to answer from heterogeneous evidence sources, including search, APIs, databases, clinical records, and formulary tools. Standard factuality metrics usually test whether an answer is supported by pooled evidence, missing a provenance-sensitive failure mode: a claim may be supported somewhere while being attributed to the wrong source. We call this cross-source conflation. We introduce ProvenanceGuard, a source-aware verifier for MCP-grounded answers. It consumes captured MCP traces with stable tool IDs, source IDs, and raw outputs; decomposes answers into atomic claims; routes claims to source-specific evidence; checks support with NLI and a token-alignment proxy; compares stated attribution with the routed source; and returns per-claim verdicts plus an answer-level allow/block decision. Blocked answers can be repaired with retrieval-augmented answer revision and re-verified. We evaluate on 281 medical-domain MCP-agent traces. A 266-trace adjudicated subset yields 2,325 LLM-assisted claim labels split by trace; 361 held-out labels are human-verified. On the 40-trace held-out split, ProvenanceGuard achieves block F1 0.802 and source accuracy 0.858 over 260 source-eligible claims, outperforming source-blind baselines that do not emit claim-to-source IDs. On a harder multi-source benchmark it reaches block F1 0.846, while source-plus-relation accuracy drops to 0.229, showing that exact source ownership remains difficult with semantically close sources. Repair-and-reverify resolves all blocked answers in the full trace set, often via conservative fallback. In 50 controlled clinical conflation probes, ProvenanceGuard detects all injected attribution swaps with no retained wrong attribution. These results show that source attribution is an independent axis for factuality verification in MCP-based agents.

</details>

---

### [[20_Research/Papers/具身智能/PearlVLA_Progressive_Embodied_Action-Plan_Refinement_in_Latent_Space|PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space]]

![[assets/2606.17924_figure.png|800]]

- **arXiv**: [2606.17924](https://arxiv.org/abs/2606.17924)
- **PDF**: https://arxiv.org/pdf/2606.17924
- **详细分析**: [[20_Research/Papers/具身智能/PearlVLA_Progressive_Embodied_Action-Plan_Refinement_in_Latent_Space|PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space]]
- **作者**: Bochen Yang, Lianlei Shan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 世界模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.3，世界模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PearlVLA: Progressive Embodied Action-Plan Refinement in Latent Space》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRG-PRL, OpenVLA, PearlVLA, RefineNet, TriVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current Vision-Language-Action (VLA) models face a trade-off between efficient action generation and explicit deliberation. Directly decoding actions from vision-language backbone representations enables low-latency control, whereas explicit reasoning through textual chains, pixel-level subgoals, or action search can improve planning but incurs substantial latency and computational cost. We propose PearlVLA, a VLA framework that moves deliberation into the latent space of a vision-language model (VLM). PearlVLA separates VLM meta-query representations into a fixed visual grounding branch and an iterative latent plan branch. At each refinement round, a plan-conditioned world query probes a lightweight frozen latent world model for an action-free future observation latent, which is fed back to guide plan refinement. A future-guided RefineNet then applies scheduled residual updates to progressively refine a coarse semantic draft into a fine-grained latent action plan. The refined plan after K rounds is then decoded in parallel into an action chunk for low-latency execution. We further introduce Causal Refinement-Grouped Process-Reward RL to optimize the latent refinement process with rewards from longer-horizon imagined futures induced by latent plan edits. Empirical evaluations on the LIBERO benchmark demonstrate that PearlVLA achieves state-of-the-art performance among existing methods.

</details>

---

### [[20_Research/Papers/大模型/Trustworthy_Self-Composable_Big-Data-as-a-Service_An_LLM-Orchestrated_Multi-Agent_Framework_for_Automated_Data_Engineering,_AutoML,_MLOps_De|Trustworthy Self-Composable Big-Data-as-a-Service: An LLM-Orchestrated Multi-Agent Framework for Automated Data Engineering, AutoML, MLOps Deployment, and Drift-Aware Lifecycle Optimization]]

![[assets/2606.17915_figure.png|800]]

- **arXiv**: [2606.17915](https://arxiv.org/abs/2606.17915)
- **PDF**: https://arxiv.org/pdf/2606.17915
- **详细分析**: [[20_Research/Papers/大模型/Trustworthy_Self-Composable_Big-Data-as-a-Service_An_LLM-Orchestrated_Multi-Agent_Framework_for_Automated_Data_Engineering,_AutoML,_MLOps_De|Trustworthy Self-Composable Big-Data-as-a-Service: An LLM-Orchestrated Multi-Agent Framework for Automated Data Engineering, AutoML, MLOps Deployment, and Drift-Aware Lifecycle Optimization]]
- **作者**: Aueaphum Aueawatthanaphisut, Badri Raj Lamichhane
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Trustworthy Self-Composable Big-Data-as-a-Service: An LLM-Orchestrated Multi-Agent Framework for Automated Data Engineering, AutoML, MLOps Deployment, and Drift-Aware Lifecycle Optimization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MLAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Big-Data-as-a-Service (BDaaS) platforms require re liable automation across data ingestion, cleaning, feature engi neering, model development, deployment, and post-deployment monitoring. However, existing LLM-based data science agents and AutoML systems mainly focus on isolated workflow stages, leaving limited support for lifecycle-level orchestration, artifact governance, human oversight, and drift-aware adaptation. This paper proposes a trustworthy self-composable BDaaS frame work based on LLM-orchestrated multi-agent collaboration. The proposed architecture decomposes the BDaaS lifecycle into specialized agents for data ingestion, data cleaning, feature engineering, AutoML training, model evaluation, MLOps de ployment, monitoring, and drift detection. A central LLM or chestration layer coordinates agent execution, validates interme diate outputs, manages workflow context, and enables dynamic workflow composition. The framework also incorporates shared artifact governance, reproducibility support, human-in-the-loop checkpoints, and drift-aware feedback loops. A prototype-based evaluation is conducted using controlled tabular benchmark datasets with missing values, categorical variables, outliers, class imbalance, and simulated covariate drift. Compared with manual ML, AutoML-only, and single-agent LLM baselines, the pro posed multi-agent BDaaS pipeline achieves competitive predictive performance while improving lifecycle-level reliability, including workflow completion, artifact traceability, deployment readiness, reproducibility, and drift recovery. The results suggest that LLM-orchestrated multi-agent systems can extend conventional AutoML toward trustworthy, adaptive, and production-oriented BDaaS lifecycle automation.

</details>

---

### [[20_Research/Papers/具身智能/Talking_to_Your_Data_Exploring_Embodied_Conversation_as_an_Interface_for_Personal_Health_Reflection|Talking to Your Data: Exploring Embodied Conversation as an Interface for Personal Health Reflection]]

![[assets/2606.17767_figure.png|800]]

- **arXiv**: [2606.17767](https://arxiv.org/abs/2606.17767)
- **PDF**: https://arxiv.org/pdf/2606.17767
- **详细分析**: [[20_Research/Papers/具身智能/Talking_to_Your_Data_Exploring_Embodied_Conversation_as_an_Interface_for_Personal_Health_Reflection|Talking to Your Data: Exploring Embodied Conversation as an Interface for Personal Health Reflection]]
- **作者**: Nikola Kovacevic, Bastien Husler, Di Zhuang, Rafael Wampfler, Barbara Solenthaler
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Talking to Your Data: Exploring Embodied Conversation as an Interface for Personal Health Reflection》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personal health data from wearables are typically presented through dashboards of charts and summary statistics, requiring users to actively interpret patterns and implications. We explore an alternative interaction paradigm: engaging with personal health data through an embodied conversational agent that facilitates objective data reflection in dialogue with the user. We present a system that combines lightweight preprocessing of wearable data with a Unity-based embodied character. Internally, the system follows a dual-agent design in which an Observer agent extracts descriptive statistics and temporal trends, and a Presenter agent communicates these findings through "spoken statistics," intentionally refraining from clinical advice to isolate the impact of the interaction modality. We evaluate this approach through a simulated-self user study (N=5) using a within-subject design. Participants adopted health personas and goals derived from the LifeSnaps dataset to compare traditional dashboard exploration with embodied conversational reflection. Our evaluation focuses on perceived understanding, the specificity of generated actions, and the cognitive shift from passive viewing to active sensemaking. The paper contributes a functional prototype, a design pattern for objective health data narrative generation, and early empirical insights into how embodiment affects the interpretation of personal health metrics.

</details>

---

### [[20_Research/Papers/机器人/ED3R_Energy-Aware_Distributed_Disaster_Detection_Enabled_by_Cooperative_Robotic_Agents|ED3R: Energy-Aware Distributed Disaster Detection Enabled by Cooperative Robotic Agents]]

![[assets/2606.17739_figure.png|800]]

- **arXiv**: [2606.17739](https://arxiv.org/abs/2606.17739)
- **PDF**: https://arxiv.org/pdf/2606.17739
- **详细分析**: [[20_Research/Papers/机器人/ED3R_Energy-Aware_Distributed_Disaster_Detection_Enabled_by_Cooperative_Robotic_Agents|ED3R: Energy-Aware Distributed Disaster Detection Enabled by Cooperative Robotic Agents]]
- **作者**: Lina Magoula, Nikolaos Koursioumpas, Nancy Alonistioti, Ramin Khalili
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.4，机器人 1.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《ED3R: Energy-Aware Distributed Disaster Detection Enabled by Cooperative Robotic Agents》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotics are expected to support environmental monitoring and natural disaster management, where decisions must be made under uncertainty, resource limitations, and strict operational constraints. In critical missions, such as wildfires, robotic agents must not only identify hazardous events with sufficient confidence, but also manage the energy cost and time until detection. This paper introduces ED3R, an energy-aware distributed framework for wildfire detection under uncertainty. ED3R enables hierarchical cooperative decision-making between a robot and a remote controller. The remote controller decides upon the robot's motion, while the robot senses the environment and decides where to execute the wildfire detection (onboard or remotely) and how. The common goal is to detect wildfires with a required confidence while minimizing the energy consumed by any robot operation. ED3R further integrates mechanisms to avoid nearby obstacles, prevent redundant exploration, enable adaptive early mission completion, and ensure feasibility through a custom penalty function. ED3R also introduces a forward-looking capability, enabled through distributed neural regression models that allow the agents to anticipate the future by evaluating candidate strategies before execution. The framework is evaluated through realistic robotics simulations, ablation studies, and baseline comparisons. Overall, ED3R achieves a mission success rate of up to 97.18%. Especially in the most demanding missions, it reduces energy consumption by up to 36.4% and detects wildfires up to 41% faster than baselines.

</details>

---

### [[20_Research/Papers/强化学习/Shattering_the_Autoregressive_Curse_Dynamic_Epistemic_Entropy_Orchestrated_Erasable_Reinforcement_Learning_for_LLMs|Shattering the Autoregressive Curse: Dynamic Epistemic Entropy Orchestrated Erasable Reinforcement Learning for LLMs]]

![[assets/2606.17735_figure.png|800]]

- **arXiv**: [2606.17735](https://arxiv.org/abs/2606.17735)
- **PDF**: https://arxiv.org/pdf/2606.17735
- **详细分析**: [[20_Research/Papers/强化学习/Shattering_the_Autoregressive_Curse_Dynamic_Epistemic_Entropy_Orchestrated_Erasable_Reinforcement_Learning_for_LLMs|Shattering the Autoregressive Curse: Dynamic Epistemic Entropy Orchestrated Erasable Reinforcement Learning for LLMs]]
- **作者**: Ziliang Wang, Kang An, Faqiang Qian, Jialu Cai, Cijun Ouyang, Yuhang Wang, Qibing Ren, Yichao Wu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Shattering the Autoregressive Curse: Dynamic Epistemic Entropy Orchestrated Erasable Reinforcement Learning for LLMs》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OlympiadBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although reinforcement learning (RL) has expanded the cognitive boundaries of large language models (LLMs), it often remains vulnerable to the autoregressive curse in long-horizon logical reasoning: small epistemic perturbations introduced early in generation can propagate irreversibly along the Markov decision process flow, triggering cascading failures that drive the reasoning trajectory toward collapse. To overcome this autoregressive cascade, in which a single early mistake can compromise all subsequent reasoning steps, we propose dynamic epistemic entropy orchestrated erasable reinforcement learning ($\text{E}^3\text{RL}$). $\text{E}^3\text{RL}$ eliminates reliance on external signals by grounding the model's endogenous local autoregressive cross-entropy as an intrinsic coordinate of epistemic uncertainty. By introducing segment-level adaptive dynamic thresholds and advantage allocation, $\text{E}^3\text{RL}$ enables the model to precisely excise localized logical defects while reusing historical key-value (KV) cache streams, thereby endowing the reasoning process with a self-healing capability. We train $\text{E}^3\text{RL}$ on the DeepMath-103k dataset. Experimental results show that $\text{E}^3\text{RL}$ reshapes the exploration efficiency of long-sequence reasoning and improves sample efficiency while maintaining linear memory overhead. On mathematical reasoning benchmarks such as AIME, $\text{E}^3\text{RL}$ achieves substantial performance gains, with the 4B and 8B parameter models surpassing previous state-of-the-art (SOTA) results by 5.349\% and 6.514\%, respectively. These findings suggest that $\text{E}^3\text{RL}$ shatters the autoregressive curse in long-sequence reasoning and establishes a theoretical and systems-level foundation for the next generation of self-healing artificial general intelligence (AGI).

</details>

---

### [[20_Research/Papers/大模型/SegTME-UNI2_A_Foundation_Model-Based_Framework_for_Generalisable_Multiclass_Cell_Segmentation_and_LLM-Driven_Tumour_Microenvironment_Charact|SegTME-UNI2: A Foundation Model-Based Framework for Generalisable Multiclass Cell Segmentation and LLM-Driven Tumour Microenvironment Characterisation in Histopathology]]

![[assets/2606.17702_figure.jpg|800]]

- **arXiv**: [2606.17702](https://arxiv.org/abs/2606.17702)
- **PDF**: https://arxiv.org/pdf/2606.17702
- **详细分析**: [[20_Research/Papers/大模型/SegTME-UNI2_A_Foundation_Model-Based_Framework_for_Generalisable_Multiclass_Cell_Segmentation_and_LLM-Driven_Tumour_Microenvironment_Charact|SegTME-UNI2: A Foundation Model-Based Framework for Generalisable Multiclass Cell Segmentation and LLM-Driven Tumour Microenvironment Characterisation in Histopathology]]
- **作者**: Wan Siti Halimatul Munirah Wan Ahmad, Faris Syahmi Samidi, Mohammad Badal Ahmmed, Vimal Angela Thiviyanathan, Selvam James Thavaraj, Anwar P.P. Abdul Majeed
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《SegTME-UNI2: A Foundation Model-Based Framework for Generalisable Multiclass Cell Segmentation and LLM-Driven Tumour Microenvironment Characterisation in Histopathology》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HoVer-Net, ResNet, UNet, UperNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Characterising the tumour microenvironment (TME) from routine H&amp;E-stained histology images requires simultaneous cell segmentation, feature extraction, and interpretable clinical reporting. We present SEGTME-UNI2, a unified framework addressing these requirements. Its core is UNI2-UPERHOVER, a dual-head segmentation model pairing the UNI2-H pathology foundation model (ViT-Giant, pretrained on &gt;100M tiles from 100K slides) with two parallel UperNet decoders: one for six-class semantic segmentation and one for horizontal-vertical gradient regression enabling watershed-based nuclear instance separation. To address the lack of pixel-level annotations in large real-world repositories, UNI2-UPERHOVER undergoes a three-stage progressive pseudo-label curriculum. Each stage trains a fresh model without weight transfer, driving improvement entirely via increased pseudo-label quality: Stage 1: Uses human-annotated PanNuke (7,901 images, 189,744 nuclei, 0.25 um/pixel). Stage 2: Uses entropy-filtered pseudo-labels from the Stage 1 model on 271,711 TCGA-UT scale-0 patches (0.5 um/pixel). Stage 3: Uses pseudo-labels from the Stage 2 model on all 1,608,060 TCGA-UT patches across six resolution scales (0.5-1.0 um/pixel). Segmentation outputs feed a structured TME feature extraction pipeline computing 20+ per-patch compositional, morphological, spatial entropy, and intercellular distance metrics. These are encoded as JSON and passed to a fine-tuned NVIDIA BioNeMo GPT model to generate clinically interpretable TME narratives. Preliminary validation on held-out PanNuke and TCGA-UT partitions demonstrates framework feasibility and internal consistency. The pseudo-labelled TCGA-UT dataset and UNI2-UPERHOVER checkpoint are publicly released to support large-scale TME profiling and spatial biology research.

</details>

---

### [[20_Research/Papers/大模型/EComAgentBench_Benchmarking_Shopping_Agents_on_Long-Horizon_Tasks_with_Distributed_Hidden_Intent|EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent]]

![[assets/2606.17698_figure.png|800]]

- **arXiv**: [2606.17698](https://arxiv.org/abs/2606.17698)
- **PDF**: https://arxiv.org/pdf/2606.17698
- **详细分析**: [[20_Research/Papers/大模型/EComAgentBench_Benchmarking_Shopping_Agents_on_Long-Horizon_Tasks_with_Distributed_Hidden_Intent|EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent]]
- **作者**: Zeyao Du, Tong Li, Haibo Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《EComAgentBench: Benchmarking Shopping Agents on Long-Horizon Tasks with Distributed Hidden Intent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AssistantBench, EComAgentBench, ShoppingBench, VitaBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As LLM-based shopping agents enter production, existing benchmarks fail to capture how a shopper's requirements arrive: stated implicitly in the query, recorded in a profile, or revealed only when the right question is asked. Benchmarks that expose full intent upfront and grade only the final choice can neither pose this long-horizon challenge nor explain which requirement an agent missed. To address this gap, we introduce EComAgentBench, a benchmark of 662 tasks grounded in real Amazon products and reviews. Each task scatters these requirements across a visible query, a tool-gated profile, and scripted clarification; an agent must uncover hidden intent, verify candidates against attributes and review evidence, and commit to a single product within 100 tool calls. Moreover, typed, source-tagged rubrics grade every task, attributing each failure to a requirement and its source. Construction is automated yet reliable, with every answer fixed in code before any text is generated and every sample validated. Our evaluation of seven models reveals that even the strongest attains only 57.1% overall accuracy, and rubric satisfaction degrades from visible to hidden sources. Overall, we believe EComAgentBench will serve as a reproducible foundation for moving shopping agents from single-query search toward dependable assistance over long horizons.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Domains_Reusing_Web_Skills_via_Transferable_Interaction_Patterns|Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns]]

![[assets/2606.17645_figure.png|800]]

- **arXiv**: [2606.17645](https://arxiv.org/abs/2606.17645)
- **PDF**: https://arxiv.org/pdf/2606.17645
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Domains_Reusing_Web_Skills_via_Transferable_Interaction_Patterns|Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns]]
- **作者**: Shiqi He, Yue Cui, Feijie Wu, Xinyu Ma, Jiaheng Lu, Yaliang Li, Bolin Ding, Mosharaf Chowdhury
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Beyond Domains: Reusing Web Skills via Transferable Interaction Patterns》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BrowserGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) web agents are usually deployed as tool callers: each turn, the model reads a fresh page observation and emits one structured tool action. When every action is a low-level primitive, horizons grow quickly and so do policy-facing LLM completions, dominating latency and cost on benchmarks such as Mind2Web and WebArena. Recent systems therefore wrap repeated interaction fragments as web skills: callable tools built from successful trajectories or induced programs, so one call can replace several primitives. However, prior skill libraries are still triggered mainly by instruction similarity or coarse site metadata, which yields low skill reuse on held-out sites and leaves much of the potential step and token reduction on the table. We present SkillMigrator, an agent that learns reusable web skills and transfers them across sites by matching layout structure rather than specific element references. Each induced skill is stored as a transferable interaction pattern (TIP): the skill paired with a structural sketch of the snapshot at induction time. At test time, SkillMigrator retrieves TIPs by layout similarity and grounds their references on the live page. The rest of the stack is standard: accessibility-snapshot observations with stable references, and fixed tool calling over primitives plus skill invocations. Compared with the state-of-the-art approaches, SkillMigrator reduces the average LLM-action count on successful trajectories by 8-10% across both WebArena and Mind2Web at matched success rate.

</details>

---

### [[20_Research/Papers/大模型/FinAcumen_Financial_Multimodal_Reasoning_via_Self-Evolving_Experience_Memory_Harness|FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness]]

![[assets/2606.17642_figure.png|800]]

- **arXiv**: [2606.17642](https://arxiv.org/abs/2606.17642)
- **PDF**: https://arxiv.org/pdf/2606.17642
- **详细分析**: [[20_Research/Papers/大模型/FinAcumen_Financial_Multimodal_Reasoning_via_Self-Evolving_Experience_Memory_Harness|FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness]]
- **作者**: Pianran Guo, Pengcheng Zhou, Yucheng Jian, Shuhua Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《FinAcumen: Financial Multimodal Reasoning via Self-Evolving Experience Memory Harness》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BizBench, FinTMMBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Financial multimodal reasoning requires agents to coordinate numerical computation, retrieval, visual interpretation, and temporal grounding across heterogeneous evidence sources. Existing tool-augmented agents improve execution fidelity, yet remain largely stateless across episodes, repeatedly rediscovering reasoning strategies and failure patterns. In high-stakes financial settings, this leads to unreliable tool routing, noisy retrieval, and hallucination-prone reasoning. We present FinAcumen, a financial reasoning agent framework centered on selective experience memory for tool-augmented multimodal reasoning. FinAcumen accumulates financially grounded reasoning experience from prior trajectories, distilling successful strategies and failure-derived cautionary rules into a persistent memory bank. During inference, retrieved experiences condition reasoning only when semantic relevance exceeds a calibrated threshold, while irrelevant memory is explicitly suppressed through a fallback mechanism. A deterministic financial tool environment further grounds numerical computation, retrieval, visual decoding, and answer this http URL four financial multimodal reasoning benchmarks, FinAcumen consistently improves a frozen 8B vision-language model over finance-specialized models and approaches leading proprietary general-purpose models. Further analysis shows that selective experience activation improves reasoning reliability under retrieval uncertainty. Our code is anonymously available at this https URL

</details>

---

### [[20_Research/Papers/大模型/Closing_the_Feedback_Loop_From_Experience_Extraction_to_Insight_Governance_in_Verbal_Reinforcement_Learning|Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning]]

![[assets/2606.17591_first_page.png|800]]

- **arXiv**: [2606.17591](https://arxiv.org/abs/2606.17591)
- **PDF**: https://arxiv.org/pdf/2606.17591
- **详细分析**: [[20_Research/Papers/大模型/Closing_the_Feedback_Loop_From_Experience_Extraction_to_Insight_Governance_in_Verbal_Reinforcement_Learning|Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning]]
- **作者**: Yanwei Cui, Xing Zhang, Yulong Zhang, Li Shao, Xiaofeng Shi, Guanghui Wang, Peiyang He
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Closing the Feedback Loop: From Experience Extraction to Insight Governance in Verbal Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training-free verbal reinforcement learning enables LLM agents to learn from world feedback -- objective signals such as dynamic task outcomes, market returns, or demand forecasts -- by extracting verbal rules from experience and injecting them as context, updating the agent's behavior without parameter changes. However, in non-stationary environments these agents face a retention-forgetting dilemma: retaining stale insights causes negative transfer, while discarding them causes catastrophic forgetting when conditions recur. We identify four requirements for navigating this dilemma -- outcome-driven evaluation, persistent structured evidence, non-monotonic knowledge lifecycle, and compositional governance -- and show that existing methods invest heavily in experience extraction while underinvesting in insight governance. We propose a three-layer architecture -- rules, evidence, and skills -- connected by a feedback-driven curation loop that closes the governance gap. Rules capture distilled experience from world outcomes; evidence logs track each rule's reliability across episodes; skills govern which rules to apply, how to resolve conflicts, and when to abstain. On financial forecasting as a case study, where world feedback is naturally abundant, noisy, and non-stationary, we show that the same accumulated experience either degrades performance below the zero-shot baseline or dramatically improves accuracy and risk-adjusted returns, depending on whether the curation loop is present.

</details>

---

### [[20_Research/Papers/具身智能/DeepInsight_A_Unified_Evaluation_Infrastructure_Across_the_Physical_AI_Stack|DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack]]

![[assets/2606.17574_figure.png|800]]

- **arXiv**: [2606.17574](https://arxiv.org/abs/2606.17574)
- **PDF**: https://arxiv.org/pdf/2606.17574
- **详细分析**: [[20_Research/Papers/具身智能/DeepInsight_A_Unified_Evaluation_Infrastructure_Across_the_Physical_AI_Stack|DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack]]
- **作者**: Siyi Li, Chunyu Sun, Jiahao Zhang, Yuchen Kang, Wuliang Wang, Yu Qiu, Rui Jiang, Haitao Cui, Jie Chen
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.1，机器人 0.2）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《DeepInsight: A Unified Evaluation Infrastructure Across the Physical AI Stack》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HumanEval, HumanoidBench, Meta-World, OSWorld, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating a Physical AI stack spans operators that differ by more than three orders of magnitude -- from a single foundation-model decoding step to thousands of physics ticks of whole-body control -- varying orthogonally in modality, reward semantics, and resource profile. No existing framework spans this range, so the stack is evaluated today by stitching together separate harnesses that share neither runtime nor scoring, preserving each segment's local validity but losing the shared identity needed to diagnose cross-layer regressions. We present DeepInsight, an evaluation infrastructure that serves this full spectrum on a single runtime. Rather than homogenize the regimes, it preserves their heterogeneity behind three narrow abstractions -- task, resource, and result -- each realized as one invariant shared by every subsystem: one episode driver, one resource-handle protocol implemented by every expensive backend (LLM inference and sandboxed runtimes alike), and one trace identity scheme under which every event is written. Deployed in production across all three layers of an embodied humanoid stack, this single set of invariants onboards new benchmarks largely by configuration. Where mature peer orchestrators exist -- at the foundation-model end -- it reproduces published references and peer-framework readings within their own spread, runs the same suites faster on a single node, and scales near-linearly across nodes. Its distinctive return is diagnostic: because every layer writes into one shared trace, a regression that begins in one layer and surfaces in another stays localizable on that trace -- a cross-layer payoff no federation of per-segment harnesses can reproduce.

</details>

---

### [[20_Research/Papers/强化学习/Reversal_Q-Learning|Reversal Q-Learning]]

![[assets/2606.17551_figure.png|800]]

- **arXiv**: [2606.17551](https://arxiv.org/abs/2606.17551)
- **PDF**: https://arxiv.org/pdf/2606.17551
- **详细分析**: [[20_Research/Papers/强化学习/Reversal_Q-Learning|Reversal Q-Learning]]
- **作者**: Aditya Oberai, Seohong Park, Sergey Levine
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.56，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Reversal Q-Learning》归入 强化学习、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Iterative generative modeling techniques, such as flow matching, provide powerful tools to model complex behaviors for effective offline reinforcement learning (RL). In this work, we propose a new off-policy RL algorithm that trains a flow policy based on prior data. Our idea starts from the "expanded" Markov decision process (MDP) framework, which treats individual flow refinement steps as separate actions in an MDP. To enable off-policy RL within this framework, we apply two techniques: we generate virtual on-policy trajectories (by "reversing" flows) to make this framework compatible with prior data, and we apply a bias-and-variance reduction technique to mitigate the curse of horizon in off-policy RL. We call the resulting algorithm Reversal Q-learning (RQL). RQL has several advantages over previous flow-based RL methods: it does not suffer from backpropagation through time, makes better use of the learned value function, and directly trains the full, expressive flow policy. Through our experiments on 50 challenging simulated robotic tasks, we show that RQL leads to the best average offline RL performance compared to state-of-the-art flow-based offline RL algorithms.

</details>

---

### [[20_Research/Papers/大模型/SEAGym_An_Evaluation_Environment_for_Self-Evolving_LLM_Agents|SEAGym: An Evaluation Environment for Self-Evolving LLM Agents]]

![[assets/2606.17546_figure.png|800]]

- **arXiv**: [2606.17546](https://arxiv.org/abs/2606.17546)
- **PDF**: https://arxiv.org/pdf/2606.17546
- **详细分析**: [[20_Research/Papers/大模型/SEAGym_An_Evaluation_Environment_for_Self-Evolving_LLM_Agents|SEAGym: An Evaluation Environment for Self-Evolving LLM Agents]]
- **作者**: Congjie Zheng, Chuanyi Xue, Bin Liang, Jun Yang, Changshui Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SEAGym: An Evaluation Environment for Self-Evolving LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LifelongAgentBench, SEA-Eval, SEAGym, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving LLM-based agents improve mainly by changing their agent harness: the structured execution layer around a base model, including prompts, memory, tools, middleware, runtime state, and the model-tool interaction loop. Existing evaluations often reduce this process to isolated task scores or a single sequential curve, obscuring whether an update produces reusable improvement, overfits recent tasks, increases cost, or harms older behavior. We introduce SEAGym, an evaluation environment for measuring agent harness updates across training, validation, test, replay, and cost records. SEAGym turns Harbor-compatible benchmarks into dynamic self-evolution task sources with train batches, frozen update-validation, held-out ID and OOD transfer views, replay diagnostics, and saved snapshot and metric records. Instantiating SEAGym on Terminal-Bench 2.0 and HLE, we compare ACE, TF-GRPO, and AHE under a shared epoch/batch protocol. The results show that these evaluation views provide complementary signals about the evolution process: frequent updates may fail to improve held-out performance, useful intermediate snapshots may collapse later, and source diversity and model backend can affect harness reliability.

</details>

---

### [[20_Research/Papers/大模型/OmniDrive_An_LLM-Choreographed_Multi-Agent_World_Model_with_Unified_Latent_Co-Compression_for_Multi-View_Driving_Video_Generation|OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation]]

![[assets/2606.17536_figure.png|800]]

- **arXiv**: [2606.17536](https://arxiv.org/abs/2606.17536)
- **PDF**: https://arxiv.org/pdf/2606.17536
- **详细分析**: [[20_Research/Papers/大模型/OmniDrive_An_LLM-Choreographed_Multi-Agent_World_Model_with_Unified_Latent_Co-Compression_for_Multi-View_Driving_Video_Generation|OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation]]
- **作者**: Zijie Meng, Yufei Liu, Chengqian Ma, Zhiyu Li, Jiyuan Liu, Wenhua Nie, Bingcai Wei, Shuqin Chen, Weichen Xu, Jiquan Yuan, Miao Zhang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.9（加权：大模型 0.9，世界模型 1）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《OmniDrive: An LLM-Choreographed Multi-Agent World Model with Unified Latent Co-Compression for Multi-View Driving Video Generation》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative world models for autonomous driving face two unresolved tensions: heterogeneous control injection, where free-form language, HD-maps, trajectories, and camera poses reside in incompatible representational spaces, and post-hoc cross-view fusion, where per-camera latents fail to encode global 3-D geometry. We trace both to a single root cause: the absence of a shared symbolic interlingua aligning language, geometry, and pixels at the latent-token level. We present DRIVE-CHOREO, an LLM-choreographed multi-agent world model that recasts controllable multi-view video generation as latent choreography. Three Qwen2.5-VL agents - a Director parsing user intent into a structured WorldScript, a Cartographer grounding it into spatially-anchored layout tokens, and an Auditor feeding cross-view critiques back as auxiliary supervision - jointly author a single position-aware token sequence. This sequence is co-compressed with the multi-view video via a view-time permutation that enforces inter-camera geometry within the convolutional receptive field of a 3-D VAE. On nuScenes, DRIVE-CHOREO sets new state-of-the-art multi-view consistency and BEV mAP (21.6) with competitive FVD (45.7); a detector trained purely on our synthetic data gains +2.4 NDS on the real validation split, validating downstream utility.

</details>

---

### [[20_Research/Papers/大模型/Scaling_Enterprise_Agent_Routing_Degradation,_Diagnosis,_and_Recovery|Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery]]

![[assets/2606.17519_figure.png|800]]

- **arXiv**: [2606.17519](https://arxiv.org/abs/2606.17519)
- **PDF**: https://arxiv.org/pdf/2606.17519
- **详细分析**: [[20_Research/Papers/大模型/Scaling_Enterprise_Agent_Routing_Degradation,_Diagnosis,_and_Recovery|Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery]]
- **作者**: Kellen Gillespie, Robyn Perry
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Scaling Enterprise Agent Routing: Degradation, Diagnosis, and Recovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LiveMCPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production LLM assistants route user requests to growing libraries of specialized tools, but how does routing accuracy degrade as the catalog scales? We study single-step routing on a 110-agent, 584-tool catalog from a deployed enterprise productivity assistant, evaluating three frontier models from 10 to 110 agents. Routing F1 on under-specified requests drops 16--23 percentage points across models. An oracle analysis decomposes the degradation into a \emph{retrieval} gap (the model cannot surface the right tool) and a \emph{confusion} gap (even with perfect retrieval, the oracle ceiling drops 10pp). Embedding-based shortlisting recovers +10--11pp F1 at full scale across all three models and two providers. A production annotation study (1,435 human-labeled utterances, three annotators) confirms the recovery on real traffic at +10--17pp despite 10--15pp lower absolute performance.

</details>

---

### [[20_Research/Papers/具身智能/MagicSim_A_Unified_Infrastructure_for_Executable_Embodied_Interaction|MagicSim: A Unified Infrastructure for Executable Embodied Interaction]]

![[assets/2606.17511_figure.png|800]]

- **arXiv**: [2606.17511](https://arxiv.org/abs/2606.17511)
- **PDF**: https://arxiv.org/pdf/2606.17511
- **详细分析**: [[20_Research/Papers/具身智能/MagicSim_A_Unified_Infrastructure_for_Executable_Embodied_Interaction|MagicSim: A Unified Infrastructure for Executable Embodied Interaction]]
- **作者**: Haoran Lu, Songling Liu, Yue Chen, Guo Ye, Mutian Shen, Shuyang Yu, Yu Xiao, Jihai Zhao, Shang Wu, Jianshu Zhang, Xiangtian Gui, Chuye Hong...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.4，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MagicSim: A Unified Infrastructure for Executable Embodied Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MagicSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot learning and embodied agents now require simulation to serve as a shared execution substrate linking control, skills, and planning, not only as a renderer, controller testbed, or fixed task environment. Existing pipelines split these layers with "magic" actions, disconnected training environments, or forward-only renders that cannot reproduce, evaluate, and annotate the same episode. We present MagicSim, an embodied interaction infrastructure built around one deterministic batched runtime and a shared Markov decision process (MDP). From YAML-first specifications that decouple contents, placement, behavior, and agent exposure, MagicSim constructs diverse executable worlds spanning task families, interaction regimes, physics, layouts, sensors, avatars, and robot embodiments in one reset-and-step loop. A common execution interface grounds high-level commands through controllers, atomicskills, planner primitives, and asynchronous planning, realizing them as robot actions rather than simulator-side state edits. One task definition supports three capabilities: benchmark and RL evaluation, an autocollect interface that automatically turns commands into grounded trajectories, and agent/VLM-facing interaction. For automatic execution, commands flow through a Command-&gt;Skill-&gt;Planner-&gt;Robot-&gt;Record pipeline, while per-environment command, skill, planning, retry, annotation, and episode states advance independently above the shared physics tick. Successful rollouts are saved as structured multimodal trajectories aligning language supervision, action representations, visual/geometric representations, and task-level status with the executed episode. MagicSim thus unifies diverse world construction, embodied execution, task evaluation, automatic rollout generation, and interactive agent interfaces in one planner-in-the-loop runtime.

</details>

---

### [[20_Research/Papers/大模型/MapSatisfyBench_Benchmarking_Satisfaction-Aware_Map_Agents_through_Behavior-Grounded_Implicit_Decision_Factors|MapSatisfyBench: Benchmarking Satisfaction-Aware Map Agents through Behavior-Grounded Implicit Decision Factors]]

![[assets/2606.17453_figure.png|800]]

- **arXiv**: [2606.17453](https://arxiv.org/abs/2606.17453)
- **PDF**: https://arxiv.org/pdf/2606.17453
- **详细分析**: [[20_Research/Papers/大模型/MapSatisfyBench_Benchmarking_Satisfaction-Aware_Map_Agents_through_Behavior-Grounded_Implicit_Decision_Factors|MapSatisfyBench: Benchmarking Satisfaction-Aware Map Agents through Behavior-Grounded Implicit Decision Factors]]
- **作者**: Lubin Bai, Mengyu Cao, Sixue Wang, Zhongwei Wan, Yue Pan, Jiale Hou, Xiang Li, Xiuyuan Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MapSatisfyBench: Benchmarking Satisfaction-Aware Map Agents through Behavior-Grounded Implicit Decision Factors》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LBS-IntentBench, LocalSearchBench, MT-Bench, MapSatisfyBench, MobilityBench, PrefEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents are increasingly integrated into map services. Since map services are embedded in everyday-life scenarios rather than professional task settings, users often express their needs informally, resulting in underspecified queries with many unspoken needs, namely, implicit decision factors that are critical for user satisfaction. Although clarification is an effective way to mitigate this issue, it increases user burden in daily interaction, and a capable agent should first proactively recover such factors from available information sources. However, evaluating this ability is challenging. The first challenge is to determine which implicit decision factors are suitable for evaluation. A factor is evaluable only if it affects user acceptance and can be recovered from information available to the agent before it responds. Second, user satisfaction cannot be reliably represented by a single reference answer, requiring a benchmark that converts satisfaction-relevant factors into objective and quantifiable evaluation targets. To address these challenges, we propose a restore-identify-filter framework that reconstructs complete user needs from behavior-chain evidence, identifies implicit decision factors, and retains only those supported by pre-query evidence. Building on this methodology, we construct MapSatisfyBench from large-scale, real-world anonymized user data and annotate ground truth from five dimensions and enables full-chain evaluation of satisfaction-aware map agents. Experiments show that current agents generally perform well on explicit task completion, but remain limited in satisfying implicit decision factors and proactively acquiring the evidence needed for satisfaction-aware decisions. These findings establish MapSatisfyBench as a benchmark for shifting map-agent evaluation from task completion toward satisfaction-aware spatial decision making.

</details>

---

### [[20_Research/Papers/大模型/MODE-RAG_Manifold_Outlier_Diagnosis_and_Energy-based_Retrieval-Augmented_Generation_Evaluation|MODE-RAG: Manifold Outlier Diagnosis and Energy-based Retrieval-Augmented Generation Evaluation]]

![[assets/2606.17449_figure.png|800]]

- **arXiv**: [2606.17449](https://arxiv.org/abs/2606.17449)
- **PDF**: https://arxiv.org/pdf/2606.17449
- **详细分析**: [[20_Research/Papers/大模型/MODE-RAG_Manifold_Outlier_Diagnosis_and_Energy-based_Retrieval-Augmented_Generation_Evaluation|MODE-RAG: Manifold Outlier Diagnosis and Energy-based Retrieval-Augmented Generation Evaluation]]
- **作者**: Zehang Wei, Jiaxin Dai, Jiamin Yan, Xiang Xiang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《MODE-RAG: Manifold Outlier Diagnosis and Energy-based Retrieval-Augmented Generation Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Multimodal Retrieval-Augmented Generation (M-RAG) enhances Large Vision-Language Models, it remains highly susceptible to cross-modal hallucinations, causal fabrications, and sycophancy. Furthermore, existing mitigation pipelines often face an intervention paradox: static rules tend to unnecessarily disrupt accurate generations, whereas leaving the multi-modal reasoning completely unguided allows existing mismatches to cascade into severe logical fabrications. To quantify and mitigate these hallucinations, we propose a Multi-Agent system, MODE-RAG, driven by Variational Free Energy (VFE) and internal attention states to dynamically gate interventions. High-risk queries are routed to five stage-specific agents, integrating Monte Carlo Tree Search (MCTS) for rigorous causal derivation and logit perturbations to penalize sycophancy. Dedicated Correction and Overseer agents ensure formatting stability and perform post-hoc factual verification. To objectively evaluate our approach, we introduce ModeVent, a challenging subset derived from the MultiVent dataset. Extensive experiments indicate that our system effectively reduces hallucination rates and logical fabrication, significantly improving the robustness of M-RAG systems.

</details>

---

### [[20_Research/Papers/世界模型/NarrativeWorldBench_A_Frontier-Saturated_Benchmark_and_a_Latent_World_Model_for_Long-Horizon_Co-Creative_Audio_Drama|NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama]]

![[assets/2606.17391_figure.png|800]]

- **arXiv**: [2606.17391](https://arxiv.org/abs/2606.17391)
- **PDF**: https://arxiv.org/pdf/2606.17391
- **详细分析**: [[20_Research/Papers/世界模型/NarrativeWorldBench_A_Frontier-Saturated_Benchmark_and_a_Latent_World_Model_for_Long-Horizon_Co-Creative_Audio_Drama|NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama]]
- **作者**: Logan Mann, Abdur Rahman, Mohammad Saifullah, Taaha Kazi, Vasu Sharma
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

《NarrativeWorldBench: A Frontier-Saturated Benchmark and a Latent World Model for Long-Horizon Co-Creative Audio Drama》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：InfinityBench, L-Eval, LongBench, NarrativeWorldBench, WritingBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-form serialized audio drama, with arcs that run for 200 to 800 episodes, is a major creative medium and a setting where frontier large language models (LLMs) fail. We benchmark 21 models, spanning classical, fine-tuned, open-frontier, closed-frontier, and reasoning tiers, on a uniform set of structural narrative metrics. All closed-frontier systems saturate at a plot-beat F1 in the band [0.78, 0.81] and collapse by about -0.20 F1 at horizon h=200. We introduce NarrativeWorldBench, an open benchmark of nine narrative-structure metrics evaluated across horizons h in {10, 20, 50, 100, 200}, with cross-lingual evaluation across four Indic languages (Hindi, Tamil, Telugu, Marathi). We introduce N-VSSM, a Narrative Variational State-Space Model that maintains a structured 256-dimensional latent world state over more than 200 episodes via a Mamba-2 backbone with an event-conditioned posterior and an 8B decoder. N-VSSM holds plot-beat F1 &gt;= 0.84 across all horizons at 4x lower compute than the closed-frontier band. A learned Cultural Transfer Function lifts cross-language fidelity by +0.20 to +0.23 Likert points. In a within-subjects writer study (n = 12 professional authors, 240 trials), N-VSSM is preferred over Claude Opus 4.5 on long-arc consistency 71% of the time and rated +1.3 Likert points higher on controllability.

</details>

---

### [[20_Research/Papers/强化学习/Model_Validation_of_Agentic_AI_Systems_A_POMDP-Based_Framework_for_Belief-State,_Forecast,_and_Policy_Validation|Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation]]

![[assets/2606.17383_figure.png|800]]

- **arXiv**: [2606.17383](https://arxiv.org/abs/2606.17383)
- **PDF**: https://arxiv.org/pdf/2606.17383
- **详细分析**: [[20_Research/Papers/强化学习/Model_Validation_of_Agentic_AI_Systems_A_POMDP-Based_Framework_for_Belief-State,_Forecast,_and_Policy_Validation|Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation]]
- **作者**: Matthew Francis Dixon
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Model Validation of Agentic AI Systems: A POMDP-Based Framework for Belief-State, Forecast, and Policy Validation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic artificial intelligence systems introduce a new class of model risk. Unlike traditional predictive models, autonomous agents continuously acquire information, form beliefs regarding latent states of the environment, generate forecasts, select actions, and adapt their behavior over time. Existing validation methodologies focus primarily on predictive accuracy and therefore provide limited insight into the quality of the underlying decision process. This paper proposes a model validation framework for agentic AI based on Partially Observable Markov Decision Processes (POMDPs). The framework decomposes autonomous decision making into information, beliefs, forecasts, actions, and utility, allowing each component to be validated independently. Large language models (LLMs) are formalized as approximate Bayesian filtering operators, and a model-risk taxonomy is developed encompassing state-space, filtering, forecast, policy, utility-specification, and parameter risks. The model risk validation methodology is demonstrated through a portfolio-management case study in which an agent infers latent market regimes from market and macroeconomic information, generates belief-conditioned forecasts, and constructs portfolios using a Black--Litterman framework. Empirical validation combines performance analysis, belief calibration diagnostics, coverage tests, ablation studies, and parameter-sensitivity analysis. The results indicate that latent-state inference contributes independently to decision quality and that the principal conclusions remain robust across a broad range of parameter values. The principal contribution of the paper is a practical framework for extending established model risk management concepts to autonomous AI systems and providing a rigorous foundation for their validation, governance, and monitoring.

</details>

---

### [[20_Research/Papers/机器人/Transformer-Based_Warm-Starting_for_Feasible_and_Optimal_Terminal_Approach_to_Tumbling_Objects_with_Space_Manipulators|Transformer-Based Warm-Starting for Feasible and Optimal Terminal Approach to Tumbling Objects with Space Manipulators]]

![[assets/2606.17317_figure.png|800]]

- **arXiv**: [2606.17317](https://arxiv.org/abs/2606.17317)
- **PDF**: https://arxiv.org/pdf/2606.17317
- **详细分析**: [[20_Research/Papers/机器人/Transformer-Based_Warm-Starting_for_Feasible_and_Optimal_Terminal_Approach_to_Tumbling_Objects_with_Space_Manipulators|Transformer-Based Warm-Starting for Feasible and Optimal Terminal Approach to Tumbling Objects with Space Manipulators]]
- **作者**: Yuji Takubo, Maximilian Adang, Mac Schwager, Simone D'Amico
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Transformer-Based Warm-Starting for Feasible and Optimal Terminal Approach to Tumbling Objects with Space Manipulators》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time trajectory generation for on-orbit robotic servicing is challenging due to the nonlinear coupling between spacecraft bus motion, manipulator dynamics, visibility cone, and trajectory-level safety constraints. This paper studies learning-based warm-starting for sequential convex programming (SCP) in the terminal approach of a space manipulator toward a tumbling target. The proposed framework decomposes the problem into a system center-of-mass translational planning stage and a coupled attitude--manipulator torque-allocation stage, and applies a causal transformer warm-start to the latter, which constitutes the dominant computational bottleneck. Linear and flow matching action decoders are compared under different action-chunking and training dataset sizes, and the resulting warm-starts are evaluated under both cost-optimal and feasibility projection using SCP. Across 300 held-out scenarios, the learned warm-start reduces the second-stage SCP iteration count by up to 28% and the runtime by 23% while preserving the final control-cost distribution. When the learned warm-starts are used for nonconvex feasibility projection, they nearly halve the runtime relative to cost-optimal SCP, while avoiding the catastrophic high-cost tail behavior observed when initialized heuristically. These results indicate that sequence-model warm-starts can improve both the computational efficiency and trajectory robustness of optimization-based terminal guidance for space manipulation.

</details>

---

### [[20_Research/Papers/其他/Graph_neural_networks_at_war_integrating_cybersecurity_and_drone_intelligence_in_the_Israeli-Iranian_conflict|Graph neural networks at war: integrating cybersecurity and drone intelligence in the Israeli-Iranian conflict]]

![[assets/2606.17119_first_page.png|800]]

- **arXiv**: [2606.17119](https://arxiv.org/abs/2606.17119)
- **PDF**: https://arxiv.org/pdf/2606.17119
- **详细分析**: [[20_Research/Papers/其他/Graph_neural_networks_at_war_integrating_cybersecurity_and_drone_intelligence_in_the_Israeli-Iranian_conflict|Graph neural networks at war: integrating cybersecurity and drone intelligence in the Israeli-Iranian conflict]]
- **作者**: Sozan Sulaiman Maghdid, Tarik Ahmed Rashid, Shavan Askar
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Graph neural networks at war: integrating cybersecurity and drone intelligence in the Israeli-Iranian conflict》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical cyber systems have brought about new threats and challenges in detection and immediate response. This study examines how Graph Neural Networks (GNNs) can be used to aid cybersecurity and drone management in a physical cyber system comprising of cyber intrusions and unmanned aerial vehicles (UAVs). By providing a bridge between structural understanding of graphical neural networks, this work has provided an integrated procedure that allows intrusion detection systems to educate on underlying network structures, identify malicious activity, and facilitates drone response measures. Based on an emulation-based case study, cyberattacks models were created to provoke the responses of the drones, which proved that graph-based learning can assist with the situational awareness, swarm coordination, and adaptive maneuver. According to the performance valuation, this method has a detection rate of 94.2, average area under the receiver operating characteristic (ROC) of 0.955 and an average response time of 1.4 seconds. Comparative experiments reveal that proposed GraphSAGE network is more effective than the Graphical Convolutional Networks (GCNs) and Graphical Attention Networks (GATs) in the identical situation. Such findings prove that graphical neural networks can be used to avert intrusion and response of dynamic cyber-physical systems.

</details>

---

### [[20_Research/Papers/大模型/Probing,_Fusion,_and_Trustworthiness_A_Systematic_Evaluation_of_Foundation_Model_Representations_for_Multimodal_Cancer_Analysis|Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis]]

![[assets/2606.17115_figure.png|800]]

- **arXiv**: [2606.17115](https://arxiv.org/abs/2606.17115)
- **PDF**: https://arxiv.org/pdf/2606.17115
- **详细分析**: [[20_Research/Papers/大模型/Probing,_Fusion,_and_Trustworthiness_A_Systematic_Evaluation_of_Foundation_Model_Representations_for_Multimodal_Cancer_Analysis|Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis]]
- **作者**: Jingyu Hu, Giuseppe Tripodi, Reed Naidoo, Sarah F. McGough, Tapabrata Chakraborti
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models (FMs) have emerged as powerful representation extractors for medical data, yet their generalizability to datasets under distribution shift remains underexplored. This work systematically evaluates FM-based representations on a suite of computational pathology tasks across two real-world commercial cohorts, IH-BC and IH-NSCLC, drawn from the licensed in-house (IH) oncology dataset. The analysis focuses on two modalities, whole-slide images and transcriptomic profiles, drawn from the IH multimodal data. We first benchmark unimodal probing performance across five FMs on eight downstream classification tasks, and find that image and omics representations carry complementary predictive signals. Then we investigate whether multimodal fusion can yield additional gains over unimodal baselines by comparing three image-omics fusion strategies built on paired representations. The trustworthiness of selected unimodal and multimodal pipelines is further assessed through conformal prediction. Our results show that FM representations achieve competitive performance on out-of-distribution data and that multimodal fusion helps mainly when no single modality dominates the signal. Conformal prediction reveals that in the majority of cases where a point prediction fails, the true diagnosis remains recoverable within the prediction set, reinforcing the value of uncertainty-aware inference for clinical support.

</details>

---

### [[20_Research/Papers/大模型/An_Evaluation_of_Data_Leakage_Risks_in_Tool-Using_LLM_Agents_in_Realistic_Scenarios|An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios]]

![[assets/2606.17114_figure.png|800]]

- **arXiv**: [2606.17114](https://arxiv.org/abs/2606.17114)
- **PDF**: https://arxiv.org/pdf/2606.17114
- **详细分析**: [[20_Research/Papers/大模型/An_Evaluation_of_Data_Leakage_Risks_in_Tool-Using_LLM_Agents_in_Realistic_Scenarios|An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios]]
- **作者**: Hankyul Baek, Jaewon Noh, Sang Seo, Yongsu Kim, Gabriel Waikin Loh Matienzo, Young Il Kim, Ee Wei Seah, Akriti Vij
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《An Evaluation of Data Leakage Risks in Tool-Using LLM Agents in Realistic Scenarios》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, AutoPatchBench, CyBench, SWE-Bench, Tau-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents are increasingly being adopted in enterprise and personal settings with access to emails, databases, documents, and other tools where they can read, update, and disseminate sensitive information. Much of prior research on data leakage risks in agents has focused on adversarial data exfiltration through prompt injections and jailbreaks. However, sensitive information may also be exposed during non-adversarial use, creating leakage risks even when users issue benign requests. We report a joint evaluation by the Singapore AI Safety Institute and the Korea AI Safety Institute examining agent data leakage in 12 realistic, non-adversarial tasks spanning customer support, DevOps, web automation, and enterprise and personal productivity. The evaluation covers five risk types: lack of data awareness, audience awareness, policy compliance, data minimization, and access-boundary awareness. Both institutes tested a common set of scenarios mirroring real-world deployments using independent testing environments and task-specific LLM-judge rubrics. Across the three tested agents, none achieved fully correct and fully safe execution across all scenarios. Successful task completion often coincided with data-handling failures such as accessing unnecessary information or disclosing information to inappropriate recipients, indicating that capability and data-handling safety should be evaluated separately. Qualitative review also revealed claim-action mismatches, simulation-aware behavior, user-simulator role reversal, and interpretation gaps in automated judging. Overall, the results indicate that operational data leakage is a first-order agent-safety concern distinct from adversarial exfiltration and provide a methodology for future evaluations of agent data-handling safety.

</details>

---

### [[20_Research/Papers/世界模型/Quantum_Cinema_An_Interactive_Cinematic_Exploration_of_Quantum_Computing_Hardware_via_Generative_World_Models|Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models]]

![[assets/2606.17102_figure.png|800]]

- **arXiv**: [2606.17102](https://arxiv.org/abs/2606.17102)
- **PDF**: https://arxiv.org/pdf/2606.17102
- **详细分析**: [[20_Research/Papers/世界模型/Quantum_Cinema_An_Interactive_Cinematic_Exploration_of_Quantum_Computing_Hardware_via_Generative_World_Models|Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models]]
- **作者**: Aoyu Zhang, Dongping Liu, Luyao Zhang
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision, Systems

#### 研究背景与动机

《Quantum Cinema: An Interactive Cinematic Exploration of Quantum Computing Hardware via Generative World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantum computing promises transformative advances across science and industry, yet the physical hardware that enables these computations remains invisible to the public: quantum processors operate inside sealed dilution refrigerators at temperatures near absolute zero, making direct observation impossible. This "imagination gap" between quantum computing's growing societal impact and the public's ability to visualize it represents a significant barrier to quantum literacy and workforce development. We present Quantum Cinema, an open-source, browser-based interactive application that closes this gap by transforming invisible quantum hardware into explorable, cinematic experiences using generative world models. Quantum Cinema guides users through a four-act narrative -- from the foundational Nobel Prize-winning science of quantum entanglement, through curated video introductions to three major quantum computing architectures (trapped-ion, neutral-atom, and superconducting systems), into immersive three-dimensional generative worlds that make invisible quantum phenomena observable, and finally to interactive radar-chart comparisons grounded in real quantum device specifications. All three-dimensional environments are generated using WorldLabs' generative world model platform and are scientifically grounded in curated metrics from Amazon Web Services (AWS) Braket quantum hardware. Quantum Cinema requires no installation, no specialized hardware, and no quantum computing background. It is designed to serve two distinct communities: scholars and developers seeking to replicate or extend the platform, and educators, researchers, and science communicators seeking an intuitive tool for explaining quantum hardware to diverse audiences. This paper describes the system architecture, the generative world model pipeline, use cases for both communities, and directions for future work.

</details>

---

### [[20_Research/Papers/具身智能/Extracting_Semantics_LLM-Guided_Automatic_Population_of_Robot_Ontology_from_URDF|Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF]]

![[assets/2606.17073_first_page.png|800]]

- **arXiv**: [2606.17073](https://arxiv.org/abs/2606.17073)
- **PDF**: https://arxiv.org/pdf/2606.17073
- **详细分析**: [[20_Research/Papers/具身智能/Extracting_Semantics_LLM-Guided_Automatic_Population_of_Robot_Ontology_from_URDF|Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF]]
- **作者**: Bastien Dussard, Guillaume Sarthou
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，大模型 0.6，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Extracting Semantics: LLM-Guided Automatic Population of Robot Ontology from URDF》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While commonsense knowledge may suffice for virtual agents, embodied robots interacting with humans require grounded and semantically rich representations of both their environment and their own physical embodiment. In cognitive robotics, ontologies are effective for integrating such heterogeneous knowledge to enable explainable reasoning, even during continuous knowledge updates. Yet, their manual construction remains a bottleneck. We present a preliminary approach for the automatic generation of robot semantic abstractions by transforming Unified Robot Description Format (URDF) models into populated ontologies. Although URDF files provide structural and kinematic descriptions, their identifiers often require commonsense interpretation to recover meaningful semantics, a task at which Large Language Models (LLMs) excel. Our pipeline leverages LLMs to infer semantic relationships by prompting them with concepts from an existing ontology, ensuring the final classification remains aligned with the formal model. To improve reliability, the pipeline combines majority voting across multiple LLM queries along with syntactic and schema-level validation to ensure that generated outputs conform to the expected representation format and ontology constraints. We evaluate the approach on multiple robot descriptions and discuss the generated abstractions. Initial results indicate that the proposed method can effectively bridge the gap between low-level robot descriptions and the structured, grounded knowledge representations required for human-robot interaction.

</details>

---
