# cs.CL | Computation and Language | 2026-06-29

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/HPRO_Hierarchical_Progressive_Reward_Optimization_via_Preference_Extraction_for_Emotional_Text-to-Speech|HPRO: Hierarchical Progressive Reward Optimization via Preference Extraction for Emotional Text-to-Speech]]

![[assets/2606.28249_figure.png|800]]

- **arXiv**: [2606.28249](https://arxiv.org/abs/2606.28249)
- **PDF**: https://arxiv.org/pdf/2606.28249
- **详细分析**: [[20_Research/Papers/大模型/HPRO_Hierarchical_Progressive_Reward_Optimization_via_Preference_Extraction_for_Emotional_Text-to-Speech|HPRO: Hierarchical Progressive Reward Optimization via Preference Extraction for Emotional Text-to-Speech]]
- **作者**: Sihang Nie, Xiaofen Xing, Rui Xing, Haoming Li, Ruitong Xiao, Jingyuan Xing, Baiji Liu, Xiangmin Xu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.65（加权：大模型 0.45，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《HPRO: Hierarchical Progressive Reward Optimization via Preference Extraction for Emotional Text-to-Speech》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, Large Language Model (LLM)-based Text-to-Speech (TTS) models have achieved remarkable naturalness. However, the standard Supervised Fine-Tuning paradigm often converges to statistically averaged prosody, limiting emotional expressiveness. While preference-driven optimization offers a promising alternative, existing approaches suffer from two structural mismatches: information conflict, where content and emotion in a shared latent space produce conflicting gradients, leading to reward hacking and semantic degradation; and scale gap, where sparse sentence-level rewards struggle to guide dense frame-level generation. To overcome these challenges, we propose HPRO, a hierarchical progressive reward optimization framework. Within HPRO, we introduce the HD-Emo codec as a novel differentiable reward model to resolve the information conflict. It extracts speech into distinct content and style preference tokens, structurally isolating emotional optimization from semantic content. Building upon this structured preference space, HPRO bridges the scale gap by progressively aligning frame-, word- and sentence-level objectives. Experiments demonstrate that HPRO significantly enhances emotional expressiveness, while effectively preserving linguistic intelligibility. The code and audio samples are publicly available at https://xxh333.github.io/hpro-demo/.

</details>

---

### [[20_Research/Papers/大模型/Mechanism-Driven_Monitors_for_Preemptive_Detection_of_LLM_Training_Instability|Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability]]

![[assets/2606.28116_figure.png|800]]

- **arXiv**: [2606.28116](https://arxiv.org/abs/2606.28116)
- **PDF**: https://arxiv.org/pdf/2606.28116
- **详细分析**: [[20_Research/Papers/大模型/Mechanism-Driven_Monitors_for_Preemptive_Detection_of_LLM_Training_Instability|Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability]]
- **作者**: Ruixuan Huang, Yipei Wang, Wenyi Fang, Hantao Huang, Yifan Huang, Ansheng You, Zhenxing Zhang, Shuai Wang, Fan Wu, Yang Zheng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Mechanism-Driven Monitors for Preemptive Detection of LLM Training Instability》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier large language model training consumes massive accelerator fleets and long wall-clock computation, making stability failures costly when they occur. After a numerical or a hyperparameter fault has already destabilized the training dynamics, it may continue for thousands of steps while loss and gradient norms still appear normal. We study mechanism-driven detection of training instability by deriving internal monitors from the functional role of each critical module and from the earliest computational sites where failures are expected to produce measurable signatures. For low-precision flash attention, we monitor the spectral entropy of a QK bilinear decomposition, whose first-order term becomes abnormal before the loss fully collapses. For MoE routers, we derive indicators from their role in expert selection. Our fault-injection experiments on low-precision attention, large learning-rate, and combined faults show that these signals provide distinct signatures for different failures, triggering thousands of steps before loss divergence.

</details>

---

### [[20_Research/Papers/大模型/Scaling_limit_of_the_Random_Language_Model|Scaling limit of the Random Language Model]]

![[assets/2606.28105_figure.png|800]]

- **arXiv**: [2606.28105](https://arxiv.org/abs/2606.28105)
- **PDF**: https://arxiv.org/pdf/2606.28105
- **详细分析**: [[20_Research/Papers/大模型/Scaling_limit_of_the_Random_Language_Model|Scaling limit of the Random Language Model]]
- **作者**: Eric De Giuli
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Scaling limit of the Random Language Model》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We develop a quantitative theory of the Random Language Model (RLM), an ensemble of stochastic context-free grammars, in a scaling limit where the number of hidden symbols $N \to \infty$ while the grammar temperature $\tildeε_d \to 0$ at fixed $x = {\tildeε}_d \log N$. In this limit, the model admits a controlled description based on a large-deviation principle over rule-usage patterns. A semi-annealed approximation maps the problem to a class of Random Energy Models with nontrivial combinatorics. We show that the RLM exhibits a condensation transition at a critical value $x_c=1/8$, below which rule usage concentrates and language statistics acquire a nontrivial dependence on corpus length. A second characteristic scale at $x=1/2$ marks the onset of entropy reduction from its maximal value. Across these regimes, we derive explicit scaling laws for the number of distinct rules, entropy, and related observables, identifying distinct scaling, saturation, and critical regimes controlled by the interplay of grammar size, corpus length, and temperature. The theory resolves previous ambiguities regarding the existence of a thermodynamic transition and explains the slow approach to the large-$N$ limit as a consequence of the dependence on $\log N$. It further provides a unified framework in which universal statistical properties of language emerge from typical realizations of generative grammars, with implications for both natural language statistics and the behavior of large language models.

</details>

---

### [[20_Research/Papers/大模型/Textual_Belief_States_for_World_Models_Identifiable_Representation_Learning_Under_Strict_Mediation|Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation]]

![[assets/2606.27681_figure.png|800]]

- **arXiv**: [2606.27681](https://arxiv.org/abs/2606.27681)
- **PDF**: https://arxiv.org/pdf/2606.27681
- **详细分析**: [[20_Research/Papers/大模型/Textual_Belief_States_for_World_Models_Identifiable_Representation_Learning_Under_Strict_Mediation|Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation]]
- **作者**: Xiang Gao, Kaiwen Dong, Yuguang Yao, Padmaja Jonnalagedda, Kamalika Das
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.57（加权：大模型 0.25，强化学习 0.36，世界模型 0.96）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Textual Belief States for World Models: Identifiable Representation Learning Under Strict Mediation》归入 世界模型、强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ScienceWorld, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models in partially observed environments rely on latent representations that summarize interaction history, but in many modern LLM-based architectures predictive performance fails to reflect representation quality due to history bypass, rendering the latent state unidentifiable. Strict latent state mediation, requiring predictions to depend only on the latent state and action, is a classical principle that resolves this, but enforcing it in text-based settings is an open challenge: textual latent states are discrete and non-differentiable, precluding variational training, and expressive LLM decoders readily ignore the bottleneck. We show how to make strict mediation work in the text domain. We formalize why it is necessary, showing that strict mediation makes representation quality empirically testable while history-leaky architectures break this connection. We then introduce textual latent states, which are discrete, interpretable, and variable-length, and factorized GRPO (fGRPO), a tree-structured reinforcement learning method that enforces strict mediation during training. Experiments on TextWorld and ScienceWorld show preserved one-step prediction accuracy alongside up to 57\% gains in representation quality and 98\% improvements in rollout performance, increasing with task complexity and horizon.

</details>

---

### [[20_Research/Papers/大模型/When_Search_Agents_Should_Ask_DiscoBench_for_Clarification-Aware_Deep_Search|When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search]]

![[assets/2606.27669_figure.png|800]]

- **arXiv**: [2606.27669](https://arxiv.org/abs/2606.27669)
- **PDF**: https://arxiv.org/pdf/2606.27669
- **详细分析**: [[20_Research/Papers/大模型/When_Search_Agents_Should_Ask_DiscoBench_for_Clarification-Aware_Deep_Search|When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search]]
- **作者**: Yiling Tao, Shihan Deng, Meiling Tao, Pengzhi Wei, Zhichao Hu, Zhihao Zhu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《When Search Agents Should Ask: DiscoBench for Clarification-Aware Deep Search》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ASQA, Abg-CoQA, AgentBench, AmbigQA, ColBench, CondAmbigQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Search agents powered by large language models (LLMs) are increasingly used to solve complex information-seeking tasks, requiring multi-step retrieval and reasoning to fulfill user goals. However, existing benchmarks often assume that user queries are complete and explicit, overlooking the fact that real-world search requests are frequently vague, underspecified, or even factually incorrect. In deep search scenarios, such ambiguity can propagate along multi-step reasoning chains and lead agents toward incorrect search trajectories. To address this gap, we introduce DiscoBench, a benchmark for clarification-aware deep search, designed to evaluate whether search agents can proactively identify ambiguity, ask effective clarification questions, and recover correct reasoning paths through user interaction. DiscoBench contains 211 samples and 463 ambiguity instances across 11 real-world domains, covering four ambiguity types. We further design a user simulator for multi-turn interaction and evaluate model performance from four perspectives: task utility, ambiguity detection, interaction strategy, and cost efficiency. Experiments on representative LLMs show that ambiguity detection and effective clarification are distinct capabilities, and that repeatedly searching instead of asking for clarification often performs worse than direct guessing, highlighting a critical gap between retrieval ability and interactive problem-solving in current search agents.

</details>

---

### [[20_Research/Papers/大模型/Yuvion_LLM_An_Adversarially-Aware_Large_Language_Model_for_Content_And_AI_Safety|Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety]]

![[assets/2606.27632_figure.png|800]]

- **arXiv**: [2606.27632](https://arxiv.org/abs/2606.27632)
- **PDF**: https://arxiv.org/pdf/2606.27632
- **详细分析**: [[20_Research/Papers/大模型/Yuvion_LLM_An_Adversarially-Aware_Large_Language_Model_for_Content_And_AI_Safety|Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety]]
- **作者**: Ting Ma, Xiufeng Huang, Benlei Cui, Xiaowen Xu, Shikai Qiu, Ruijie Jian, Hongxing Li, Guanghui Wang, Longtao Huang, Haiwen Hong, Haolei Xu, Wenjing Jiang...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.75（加权：大模型 1.35，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Yuvion LLM: An Adversarially-Aware Large Language Model for Content And AI Safety》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RiskEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language models are increasingly deployed in real-world systems, safety failures can still lead to harmful outputs and dangerous misuse. We argue that the essence of safety is adversarial: many failures arise not from natural inputs alone, but from strategic attempts to evade model policies and safeguards. However, existing general-purpose model development largely overlook this adversarial nature, and often remain insufficient for realistic safety scenarios involving planning, tool use, and multi-step reasoning, causing measured safety performance to overestimate real deployment robustness. To address this gap, we present Yuvion LLM, a large language model built for adversarially robust content safety and broader AI safety. Yuvion LLM treats adversarial robustness and agentic capability as first-class objectives. Its pipeline combines adversarially aware data construction, knowledge-enhanced continued pretraining, and policy-grounded multi-task safety post-training, including risk-aware supervised fine-tuning and reinforcement learning-based policy optimization, together with safety-aware agentic reinforcement learning for tool use and multi-step reasoning in complex safety scenarios. We further introduce the Yuvion LLM RiskEval (YLRE), a collection of 93 benchmarks across four evaluation categories, covering diverse open and internal evaluations with a focus on safety, adversarial robustness, and real-world capability requirements. Across these evaluations, Yuvion LLM demonstrates clear advantages on safety-focused benchmarks and particularly strong robustness under adversarial conditions, while maintaining solid overall capability. Notably, Yuvion-8B outperforms most state-of-the-art baselines, including substantially larger models such as GPT-5.4 and Qwen3-MAX, on several safety tasks.

</details>

---

### [[20_Research/Papers/大模型/Ko-WideSearch_A_Korean_Breadth-Search_Benchmark_for_Exhaustive_Set_Enumeration_by_Web_Agents|Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents]]

![[assets/2606.27595_figure.png|800]]

- **arXiv**: [2606.27595](https://arxiv.org/abs/2606.27595)
- **PDF**: https://arxiv.org/pdf/2606.27595
- **详细分析**: [[20_Research/Papers/大模型/Ko-WideSearch_A_Korean_Breadth-Search_Benchmark_for_Exhaustive_Set_Enumeration_by_Web_Agents|Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents]]
- **作者**: Minbyul Jeong
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Ko-WideSearch: A Korean Breadth-Search Benchmark for Exhaustive Set Enumeration by Web Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, AssistantBench, HotpotQA, TriviaQA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web-agent benchmarks overwhelmingly measure depth -- pinning one obscure answer behind a chain of constraints -- while breadth, exhaustively enumerating a closed set and filling each item's attributes, is barely evaluated, especially outside English. Breadth is also hard to build: certifying that a gold set is complete and every cell correct is far costlier than checking a single answer. I introduce \textsc{Ko-WideSearch}, a Korean breadth-search benchmark built by an automated synthesize-and-verify pipeline. Each task names a set-parent entity -- a TV season, a dynasty, a league, an administrative region, an election -- and asks for its full membership plus a per-item attribute table, graded by Item-, Column-, and Row-F1. It spans 228 tables over 190 entities and sixteen categories across three difficulty tiers, set by two structural knobs I dial independently -- table width and a 2-D composite key -- so cross-product membership climbs from 0\% to 100\% across the tiers. A single normalization-aware comparator is shared between gold construction and grading, so stable date and count columns are not over-dropped on formatting alone. Across twenty web agents, the failure is consistent: agents recover the set but not the rows (e.g.\ Item-F1 92.8 against Row-F1 53.7), accuracy falls steadily as the knobs harden, and neither more search nor more spend closes the gap. Broken down by cell, the hard part is finding the right value, not formatting it: open-ended free-text cells fail most, while cells with a standard answer such as a date or a name usually come out right.

</details>

---

### [[20_Research/Papers/大模型/EntMTP_Accelerating_LLM_Inference_with_Entropy_Guided_Multi_Token_Prediction|EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction]]

![[assets/2606.27550_figure.png|800]]

- **arXiv**: [2606.27550](https://arxiv.org/abs/2606.27550)
- **PDF**: https://arxiv.org/pdf/2606.27550
- **详细分析**: [[20_Research/Papers/大模型/EntMTP_Accelerating_LLM_Inference_with_Entropy_Guided_Multi_Token_Prediction|EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction]]
- **作者**: Carrie Chen
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM

#### 研究背景与动机

《EntMTP: Accelerating LLM Inference with Entropy Guided Multi Token Prediction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-token prediction has been shown to increase data density during training, improve downstream text-generation quality, and serves as the defacto approach for self-speculative decoding. Existing foundation and open source models that use MTP heads commit to a static tree-based attention topology throughout the entire generation sequence, meaning the speculation depth, and thus the compute required during verification, stays constant regardless of the context. This is fundamentally misaligned with the entropy patterns of natural language where low-entropy regions often support reliable multi-step drafting, while high-entropy regions require more conservative speculation. To address this, we propose Entropy-guided Multi-Token Prediction (EntMTP), a training-free scheduler that toggles between tree-based attention topologies from a set of task-specific pareto-optimal trees conditioned on a running estimate of local generation entropy. By matching speculation depth to context predictability, EntMTP maximizes expected accepted-token throughput across the full distribution of generated text without sacrificing generation quality. When evaluated across Humaneval, ShareGPT, GSM8k, and Litbench benchmarks, EntMTP consistently achieves a 1.15x speedup against Hydra and peak speedup of 1.36x against Medusa baselines respectively.

</details>

---

### [[20_Research/Papers/大模型/Cluster,_Route,_Escalate_Cascaded_Framework_for_Cost-Aware_LLM_Serving|Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving]]

![[assets/2606.27457_first_page.png|800]]

- **arXiv**: [2606.27457](https://arxiv.org/abs/2606.27457)
- **PDF**: https://arxiv.org/pdf/2606.27457
- **详细分析**: [[20_Research/Papers/大模型/Cluster,_Route,_Escalate_Cascaded_Framework_for_Cost-Aware_LLM_Serving|Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving]]
- **作者**: Yasmin Moslem, Magdalena Kacmajor, Vasudevan Nedumpozhimana, Ammar Abbas, Solmaz Panahi, David Lynch, Zhuangzhuang Nie, Alexandros Agapitos, Aleksandar Milenovic, Hongmeng Song, Yucheng Shi, Yue Pan...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient deployment of large language models (LLMs) in production forces a trade-off between accuracy and cost. Operators often default to a single model that is either expensive for easy queries or insufficient for hard ones. To address this challenge, we propose a two-stage cascaded solution. Stage 1 clusters incoming queries and assigns each cluster to its most cost-effective model. The cost budget for this routing process is set by an interpretable hyperparameter, tuned offline. Stage 2 adds a quality estimation (QE) cascade; when an output from Stage 1 is judged low-quality, the query is escalated to a stronger model. This ensures only hard or low-confidence cases reach the expensive models. On the test datasets, the cascaded system retains 97-99% of the strongest model's accuracy while reducing Time Per Output Token (TPOT). It requires only task-correctness labels and adapts to changes in the model pool without manual reconfiguration.

</details>

---

### [[20_Research/Papers/大模型/Delayed_Verification_Destabilizes_Multi-Agent_LLM_Belief_Instability_Thresholds_and_Optimal_Corrector_Placement|Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement]]

![[assets/2606.27409_figure.png|800]]

- **arXiv**: [2606.27409](https://arxiv.org/abs/2606.27409)
- **PDF**: https://arxiv.org/pdf/2606.27409
- **详细分析**: [[20_Research/Papers/大模型/Delayed_Verification_Destabilizes_Multi-Agent_LLM_Belief_Instability_Thresholds_and_Optimal_Corrector_Placement|Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement]]
- **作者**: Igor Itkin
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Delayed Verification Destabilizes Multi-Agent LLM Belief: Instability Thresholds and Optimal Corrector Placement》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent large language model (LLM) systems often rely on verifier and critic agents to suppress hallucinations, but verification is delayed. During this delay, false claims can propagate through the agent network. We model this process as delayed consensus on a graph with grounded corrector nodes. Spectral decomposition by the grounded Laplacian yields a closed-form stability threshold for the verification dose: correction that is too strong or too delayed can turn consensus into oscillation. The most unstable regime occurs when the communication and verification delays coincide; for delay two, the threshold is the inverse golden ratio. The same framework gives a supermodular placement objective and a greedy (1-1/e)-approximation rule for assigning a limited corrector budget to influential nodes. Experiments across five open models confirm the predicted dose-delay oscillations. By contrast, grounded factual answering makes truth an absorbing boundary and eliminates the effect, suggesting that the instability is specific to signed-belief tasks while grounded verification remains stabilizing

</details>

---
