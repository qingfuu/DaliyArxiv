# cs.AI | Artificial Intelligence | 2026-08-19

#arxiv #ComputerScience

**论文数**: 37

### [[20_Research/Papers/大模型/On_the_Fragility_of_Self-Improving_Agents_Variance,_Task_Order,_and_Underspecification|On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification]]

![[assets/2608.18066_first_page.png|800]]

- **arXiv**: [2608.18066](https://arxiv.org/abs/2608.18066)
- **PDF**: https://arxiv.org/pdf/2608.18066
- **详细分析**: [[20_Research/Papers/大模型/On_the_Fragility_of_Self-Improving_Agents_Variance,_Task_Order,_and_Underspecification|On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification]]
- **作者**: Qinyuan Ye, Yu Li, Yada Pruksachatkun, Jiaxin Zhang, Chien-Sheng Wu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《On the Fragility of Self-Improving Agents: Variance, Task Order, and Underspecification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-based self-improving agents--those that learn from an online stream of tasks and improve over time by maintaining a textual memory bank--have shown great promise in recent literature. However, the reliability aspects of these methods have been critically overlooked. In this work, we conduct a comprehensive re-evaluation of two memory-based methods, broadening the scope of evaluation along two axes: (1) including multiple runs to quantify variance, and (2) randomly shuffling the tasks to investigate the effect of task order. Through these experiments, we make two observations that expose the fragility of current methods: First, agent evaluation is inherently noisy in complex environments and on multi-step tasks, and stacking a self-improving loop on top can further amplify this noise. Second, the agent's improvement is highly dependent on task order. Prior works often adopt default orderings that impose an implicit curriculum, acting as a hidden prerequisite for success. To better understand this fragility, we manually examine the agents' memory and hypothesize that task and environment underspecification contribute to this fragility. We validate this hypothesis by incorporating information that enables better specification, such as detailed rubrics and environment feedback, into the memory construction process. While this added information partially closes the performance degradation in previous experiments, significant gaps still remain, suggesting that other uncharacterized factors contribute to this fragility. Looking ahead, our work advocates for more rigorous evaluation protocols for self-improving agents by reporting results across multiple runs and stress-testing them under challenging conditions. Moreover, our findings on underspecification call for systems and interfaces that enable effective human oversight, preventing agents from failing in unforeseeable ways.

</details>

---

### [[20_Research/Papers/大模型/Policy-Invariant_Reward_Shaping_from_LLM_Feedback_A_Framework_for_Hybrid_RL_Agents|Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents]]

![[assets/2608.18008_first_page.png|800]]

- **arXiv**: [2608.18008](https://arxiv.org/abs/2608.18008)
- **PDF**: https://arxiv.org/pdf/2608.18008
- **详细分析**: [[20_Research/Papers/大模型/Policy-Invariant_Reward_Shaping_from_LLM_Feedback_A_Framework_for_Hybrid_RL_Agents|Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents]]
- **作者**: Christophe D. Hounwanou, John Emeka Eze, Yaé U. Gaba
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.7，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Policy-Invariant Reward Shaping from LLM Feedback: A Framework for Hybrid RL Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Combining large language models with reinforcement learning is increasingly explored, yet the theoretical status of LLM-derived reward signals is often left implicit. We formalize the hybrid LLM-planner and RL-controller architecture as a Goal-Augmented Markov Decision Process and show that when the LLM per-state progress score is used as a bounded potential function, the resulting shaping term preserves the optimal policy set even when the LLM scores are inaccurate. This guarantee is stronger than what general LLM-as-reward approaches provide. We verify the result numerically on a small MDP under four potential configurations, including an adversarial one scaled to twenty times the base reward magnitude.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Zero-Shot_Task_Transfer_with_Neurosymbolic_World_Models|Towards Zero-Shot Task Transfer with Neurosymbolic World Models]]

![[assets/2608.17959_figure.png|800]]

- **arXiv**: [2608.17959](https://arxiv.org/abs/2608.17959)
- **PDF**: https://arxiv.org/pdf/2608.17959
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Zero-Shot_Task_Transfer_with_Neurosymbolic_World_Models|Towards Zero-Shot Task Transfer with Neurosymbolic World Models]]
- **作者**: Isidoro Tamassia, Lennert De Smet, Giuseppe Marra
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.72（加权：强化学习 0.36，世界模型 1.36）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Towards Zero-Shot Task Transfer with Neurosymbolic World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GCRL, MBRL, MiniWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

State-of-the-art model-based reinforcement learning methods learn neural world models that allow policy improvement by planning in a latent space, without assumptions on the structure of the underlying environment. While expressive, these models are generally task-dependent: they learn uninterpretable latent representations that are tied to the training task and thus hard to generalize to new tasks. In this work, we present a novel world model formulation where the reward prediction only depends on a subset of structured, symbolic components of the whole latent state. Decoupling observation reconstruction and reward prediction allows us to learn world models that can adapt zero-shot, i.e. without further environment interactions, to new reward functions defined over the same symbolic state space. We discuss the main advantages and challenges of learning these neurosymbolic world models and demonstrate the strong generalisation properties of our approach over purely neural methods.

</details>

---

### [[20_Research/Papers/大模型/An_Omitted_Mode_Is_a_Rare_Rule_The_Sampling-Verification_Danger_Law_in_Continuous_Code_World_Models|An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models]]

![[assets/2608.17956_first_page.png|800]]

- **arXiv**: [2608.17956](https://arxiv.org/abs/2608.17956)
- **PDF**: https://arxiv.org/pdf/2608.17956
- **详细分析**: [[20_Research/Papers/大模型/An_Omitted_Mode_Is_a_Rare_Rule_The_Sampling-Verification_Danger_Law_in_Continuous_Code_World_Models|An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models]]
- **作者**: Javier Aguilar Martín
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.16，世界模型 0.96）
- **关联关键词**: LLM, WorldModel

#### 研究背景与动机

《An Omitted Mode Is a Rare Rule: The Sampling-Verification Danger Law in Continuous Code World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the Code World Model paradigm an LLM synthesizes an executable world model that a classical planner searches, and the model is accepted when it reproduces sampled transitions. We ask what that acceptance certifies in continuous control. We define the pipeline's danger as an expected risk and isolate its exact factor: the probability that N i.i.d. gate rollouts all miss a critical event of probability r is exactly (1-r)^N; an independent acceptance sample adds its budget to the exponent. On three hybrid instruments the accepted mode-blind model is exploited: the planner is pinned at the mode boundary at a regret of nearly the whole attainable return. We prove a localization budget, valid at boundary points: models with Lipschitz constant at most L differing by eta at a point disagree above tolerance eps on a region of volume at least kappa((eta-eps)/L)^(d+m); the discontinuous reset modes studied pay no such budget. With real LLM synthesis, GPT-5.x repairs an omitted 1D clamp in 105 of 111 mode-containing draws -- every attempt exact on 50 of 56 instrument-stream blocks (95% CI [0.781, 0.960]). On 2D regions no artifact recovers the rule (0/156); eight targeted interventions leave the failure in place, and positive controls locate it: a located rule is not induced, while given form and location the constants follow exactly. A version-space certificate proves identification is class-relative: at the widest dose the declared fit succeeds in 20/20 blocks and every sample-consistent circle is within tolerance in 18/20. We prove a class of entry rules exactly consistent with every sample yet harmless at play, so identifiability is a measurable property of the instrument. Re-scoring all 1034 artifacts on independent samples confirms acceptance certifies sample consistency and no more: where the gate is provably informative it covers about two percent of the exploited planner's queries.

</details>

---

### [[20_Research/Papers/强化学习/Efficient_RLVR_Scheduling_via_Graph-Structured_Online_Difficulty_Estimation|Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation]]

![[assets/2608.17941_figure.png|800]]

- **arXiv**: [2608.17941](https://arxiv.org/abs/2608.17941)
- **PDF**: https://arxiv.org/pdf/2608.17941
- **详细分析**: [[20_Research/Papers/强化学习/Efficient_RLVR_Scheduling_via_Graph-Structured_Online_Difficulty_Estimation|Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation]]
- **作者**: Zhizhao Liu, Zhiliang Tian, Xi Wang, Zhihua Wen, Yihang Xiong, Zhiquan Lai, Dongsheng Li
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Efficient RLVR Scheduling via Graph-Structured Online Difficulty Estimation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OlympiadBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) improves the reasoning capabilities of large language models but relies on costly rollout exploration. Assigning the same exploration budget to samples with different difficulty levels is inefficient: easy samples may receive redundant rollouts, whereas difficult but learnable samples may receive too little exploration. Existing adaptive schedulers address this mismatch through curriculum-based sample selection or non-uniform rollout allocation based on estimated sample difficulty. However, obtaining reliable online difficulty estimates remains challenging: dedicated probing adds substantial generation overhead, whereas history-based estimators face a cold start with no initial observations and stale feedback, and typically ignore relations among samples. To address these limitations, we propose a plug-and-play graph-based online difficulty estimator that shares rollout feedback across related samples and continuously updates their difficulty estimates, mitigating cold start and staleness without dedicated probing. Specifically, we first construct a difficulty-aware sample graph based on semantic and reasoning similarities. Based on this graph, we introduce latent difficulty states and use a Potts prior to encourage neighboring samples to share the same state. We then employ a state-level Beta-Binomial model to aggregate the rollout outcomes associated with each state. Finally, we use an online mean-field variational algorithm to continuously update the latent-state assignments and state-level difficulty as new feedback arrives. Our framework can be integrated into sample-selection and rollout-allocation schedulers, enabling difficulty-adaptive exploration without dedicated probing. Experiments across multiple base models, RL schedulers, and benchmarks demonstrate that our framework achieves better performance.

</details>

---

### [[20_Research/Papers/大模型/EvoTS-Agent_A_Self-Evolving_LLM_Agent_for_Financial_Time_Series_Change_Point_Detection|EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection]]

![[assets/2608.17933_figure.png|800]]

- **arXiv**: [2608.17933](https://arxiv.org/abs/2608.17933)
- **PDF**: https://arxiv.org/pdf/2608.17933
- **详细分析**: [[20_Research/Papers/大模型/EvoTS-Agent_A_Self-Evolving_LLM_Agent_for_Financial_Time_Series_Change_Point_Detection|EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection]]
- **作者**: Lei Jiang, Ye Wei, Xinyu Xi, Jordan Langham-Lopez, Yifan Bao, Raad Khraishi, Yihao Ang, Anthony K. H. Tung, Lukasz Szpruch, Hao Ni
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《EvoTS-Agent: A Self-Evolving LLM Agent for Financial Time Series Change Point Detection》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Financial time series exhibit non-stationary and heterogeneous statistical properties, making change-point detection challenging because no single unsupervised algorithm performs consistently across assets and market regimes. Conventional workflows consequently depend heavily on expert-driven model selection, feature design, and hyperparameter tuning, limiting their scalability and adaptability. We propose EvoTS-Agent, a validation-guided self-evolving LLM agent for autonomous financial time-series change-point detection. EvoTS-Agent first performs curated exploratory data analysis to characterize dataset properties and initialize candidate detection models. It then evolves executable experiment trajectories through three complementary operators: \textit{Revision} exploits the current best solution, \textit{Alternative Strategy} explores fundamentally different modeling directions when progress stagnates, and \textit{Recombination} synthesizes complementary evidence from high-performing trajectories. Validation feedback guides trajectory evolution throughout the search, enabling the agent to adapt its detection pipeline to the statistical characteristics of each dataset while preserving reliable optimization. Experiments across four benchmark datasets demonstrate that EvoTS-Agent consistently outperforms existing LLM-based agents while maintaining a 100\% execution success rate across all evaluated backbone LLMs.

</details>

---

### [[20_Research/Papers/大模型/BEAR-Bench_A_Bilingual_Enterprise_and_Academic_Reasoning_Benchmark_for_Multimodal_Models|BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models]]

![[assets/2608.17895_figure.png|800]]

- **arXiv**: [2608.17895](https://arxiv.org/abs/2608.17895)
- **PDF**: https://arxiv.org/pdf/2608.17895
- **详细分析**: [[20_Research/Papers/大模型/BEAR-Bench_A_Bilingual_Enterprise_and_Academic_Reasoning_Benchmark_for_Multimodal_Models|BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models]]
- **作者**: Liubov Chubarova, Alexandra Kuleshova, Daniil Volkov, Kirill Sultanov, Alexey Zaytsev
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《BEAR-Bench: A Bilingual Enterprise and Academic Reasoning Benchmark for Multimodal Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BEAR-Bench, ChartQA, DocVQA, LabTabVQA, MTVQA, OCRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Multimodal Large Language Models (MLLMs) have made significant strides in visual comprehension, their ability to reason about text-dense, professional documents remains incompletely evaluated. Existing benchmarks emphasize information extraction, require external domain knowledge, or cover professional documents only as one of many settings. They are also largely English- or Chinese-centric, leaving other languages and Russian, in particular, substantially underrepresented. To address these limitations, we introduce BEAR-Bench (Bilingual Enterprise and Academic Reasoning), a self-contained, complex English-and-Russian benchmark comprising 1000 human-annotated questions based on text-rich business and scientific documents. We evaluate 16 proprietary and open-weight MLLMs, including Gemini 3.1 Pro and Qwen3.5-397B, on BEAR-Bench and observe clear headroom even for the strongest systems. Finally, we use the resulting model outputs to compare existing hallucination detection methods, evaluating not only how often models fail on BEAR-Bench but also how reliably those failures can be identified.

</details>

---

### [[20_Research/Papers/机器人/Training_with_synthetic_data_for_drone_detection_in_thermal_imagery|Training with synthetic data for drone detection in thermal imagery]]

![[assets/2608.17799_first_page.png|800]]

- **arXiv**: [2608.17799](https://arxiv.org/abs/2608.17799)
- **PDF**: https://arxiv.org/pdf/2608.17799
- **详细分析**: [[20_Research/Papers/机器人/Training_with_synthetic_data_for_drone_detection_in_thermal_imagery|Training with synthetic data for drone detection in thermal imagery]]
- **作者**: Tanel Liiv, Sander Soodla, Nzamba Bignoumba, Alma M. Liezenga, Toomas Pruuden
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Training with synthetic data for drone detection in thermal imagery》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ground-to-Air (G2A) drone detection in medium- and long-wave infrared (MWIR/LWIR) imagery is challenging due to reduced texture information, sensor noise, weak thermal contrast, and the scarcity of annotated data. This work investigates a synthetic-first training strategy that combines synthetic scene generation with fine-tuning on real data. We show that synthetic data provides an effective basis for learning initial object representations, while real in-domain thermal imagery is still essential for reliable deployment. Even small amounts of real IR data substantially reduce domain gaps. Our experiments indicate that dataset alignment has a stronger impact on performance than model scale. Finally, our analysis of the dataset suggests that semantic alignment in feature space is the strongest predictor of model performance, while radiometric properties such as entropy and dynamic range also contribute to detection robustness. This work provides a foundation for combining synthetic and real IR data for effective G2A drone detection.

</details>

---

### [[20_Research/Papers/大模型/What_Aggregate_Scores_Miss_Measuring_Item-Level_Regressions_in_Commercial_LLM_API_Migrations|What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations]]

![[assets/2608.17719_first_page.png|800]]

- **arXiv**: [2608.17719](https://arxiv.org/abs/2608.17719)
- **PDF**: https://arxiv.org/pdf/2608.17719
- **详细分析**: [[20_Research/Papers/大模型/What_Aggregate_Scores_Miss_Measuring_Item-Level_Regressions_in_Commercial_LLM_API_Migrations|What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations]]
- **作者**: Xiaonan Xu, Wenjing Wu
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《What Aggregate Scores Miss: Measuring Item-Level Regressions in Commercial LLM API Migrations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GPQA, IFBench, IFEval, SuperGPQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Context: Software systems that depend on commercial large language model APIs must migrate to successor versions when vendors deprecate older models. Migration decisions typically rely on aggregate benchmark scores, which compress heterogeneous item-level behaviour into a single net figure. Objective: We measure what that compression conceals. Method: On three pairwise upgrades in the GPT-5.4 to GPT-5.6 Sol product sequence, we query 900 public benchmark items (graduate-level knowledge, olympiad mathematics, instruction following) 50 times per item per model, classify each item as reliably improved, reliably regressed, practically equivalent, or inconclusive under false-discovery-rate control and a practical-significance threshold, and calibrate the results against a label-permutation null. Results: Across all nine migration-benchmark cells, reliable improvements and reliable regressions coexist. Edges with aggregate gains of up to 7.3 percentage points contain up to 8.3% reliably regressed items; edges with aggregate losses contain up to 10.7% reliably improved items. On the instruction-following benchmark, the gap between strict and loose scoring widens by 3.9 percentage points on the latest migration: a 3.9-point regression under strict scoring shrinks to 0.04 points under loose scoring. Conclusion: Migration decisions based on aggregate scores alone miss substantial bidirectional item-level change. The complete response-level archive and per-item scoring outputs are released.

</details>

---

### [[20_Research/Papers/具身智能/Dijkstra_as_an_Oracle_for_Online_Stochastic_Shortest_Path_Navigation_with_Provable_Guarantees|Dijkstra as an Oracle for Online Stochastic Shortest Path Navigation with Provable Guarantees]]

![[assets/2608.17703_figure.png|800]]

- **arXiv**: [2608.17703](https://arxiv.org/abs/2608.17703)
- **PDF**: https://arxiv.org/pdf/2608.17703
- **详细分析**: [[20_Research/Papers/具身智能/Dijkstra_as_an_Oracle_for_Online_Stochastic_Shortest_Path_Navigation_with_Provable_Guarantees|Dijkstra as an Oracle for Online Stochastic Shortest Path Navigation with Provable Guarantees]]
- **作者**: Mansur M. Arief, Ali Akarma, Ahmad Alfan Alfian Irfan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Dijkstra as an Oracle for Online Stochastic Shortest Path Navigation with Provable Guarantees》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robots that operate in side by side with humans and critical facilities must reach their goals at low cost, despite often unknown true traversal costs of the map apriori and imperfect actuation. Planners that solve the underlying stochastic shortest path problem exactly, such as value iteration, require computation that grows with the diameter of the map, whereas Dijkstra's algorithm is fast but is usually considered inexact once transitions are stochastic. This study shows that Dijkstra's algorithm can remain an exact planning engine under a condition that is much weaker than the causality condition often invoked in the literature, namely nonnegativity of a reduced cost defined on the determinized map. Building on this characterization, an online learner DORA (Dijkstra Oracle Reduced-cost Algorithm) is proposed for robot navigation that calls a shortest path oracle a fixed number of times per episode, never estimates a transition kernel, and adds a logarithmic survival weight when the probability of contact with a dynamic obstacle must stay within a budget. In the numerical experiments involving three other benchmarks that cover grid world navigation, directional drilling, and drone surveillance, the learner matches optimistic value iteration that is given the true transition kernel while performing 4.5 to 19.3 times less planner work, reduces contacts during learning by a factor of seventeen relative to determinize and replan, and keeps the contact rate within budgets that span two orders of magnitude. These results indicate that shortest path search supports safe and efficient online navigation and path planning tasks.

</details>

---

### [[20_Research/Papers/大模型/GraphWake_Group_Polarization_via_Memory-Mediated_Polarization_Cascade_in_LLM-Agent_Communities|GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities]]

![[assets/2608.17665_figure.png|800]]

- **arXiv**: [2608.17665](https://arxiv.org/abs/2608.17665)
- **PDF**: https://arxiv.org/pdf/2608.17665
- **详细分析**: [[20_Research/Papers/大模型/GraphWake_Group_Polarization_via_Memory-Mediated_Polarization_Cascade_in_LLM-Agent_Communities|GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities]]
- **作者**: Haoran Bu, Zejian Chen, Litian Zhang, Xi Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《GraphWake: Group Polarization via Memory-Mediated Polarization Cascade in LLM-Agent Communities》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-driven agents can autonomously exchange opinions on online platforms and form communities. Such agent-operated social platforms raise a new security concern: attackers may manipulate agents to induce group polarization. Existing methods manipulate agent prompts or construct echo chambers, both of which are difficult to realize in practice. We therefore formulate a new threat, Memory-Mediated Polarization Cascade, which uses agent memory as a persistence channel and public discussion as a propagation channel. This threat contains three stages. During exposure and memory retention, the attacker exposes a small set of target agents to arguments that reinforce their respective stated stances. The targets' memory systems then process and retain these arguments. During retrieval and reproduction, a shared stance-neutral discussion cues the targets to retrieve and reproduce their respective retained arguments. During iterative propagation, untreated agents influenced by the reproduced arguments restate and spread them. We instantiate this threat in GraphWake with three components: (i) stance-support argumentation knowledge graphs construct knowledge-based arguments; (ii) axiom-oriented triple selection distills them for reliable retention and reproduction; and (iii) stance-neutral memory cueing triggers concurrent retrieval and reproduction, initiating propagation. Experiments across multiple discussions and memory systems show that GraphWake substantially increases group polarization. These findings reveal a community-level polarization risk.

</details>

---

### [[20_Research/Papers/大模型/LLM-Derived_Preference_Judgments_Are_Not_Self-Consistent|LLM-Derived Preference Judgments Are Not Self-Consistent]]

![[assets/2608.17644_figure.png|800]]

- **arXiv**: [2608.17644](https://arxiv.org/abs/2608.17644)
- **PDF**: https://arxiv.org/pdf/2608.17644
- **详细分析**: [[20_Research/Papers/大模型/LLM-Derived_Preference_Judgments_Are_Not_Self-Consistent|LLM-Derived Preference Judgments Are Not Self-Consistent]]
- **作者**: Matthew T. Ford, Francis Bahk, Jingjing Wang, Adam S. Jovine, Tinghan Ye, David B. Shmoys, Peter I. Frazier
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM-Derived Preference Judgments Are Not Self-Consistent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agents increasingly interpret a person's natural-language preferences by querying an LLM for numerical preference judgments, e.g., by asking how much the person would be willing to pay for an item. A growing body of work estimates a utility function from these judgments and then chooses actions based on their estimated utility. This pipeline assumes the judgments are approximately self-consistent: that a single utility function can reproduce them. But are they? To study this question, we measure the self-consistency of cardinal LLM preference judgments. For example, the difference in stated willingness-to-pay between two items should match the stated payment that makes a person indifferent to exchanging them. We develop statistical tests and interpretable measures of how far observed responses depart from the best-fitting self-consistent utility function. Experiments with flight, apartment, and hotel examples across six LLMs reveal large persistent inconsistencies. This suggests that LLM-derived preference judgments cannot be faithfully summarized by a single utility function.

</details>

---

### [[20_Research/Papers/具身智能/Iterative_Grasp_Pose_Refinement_A_Deep_Reinforcement_Learning_Approach_for_2D_Vision|Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision]]

![[assets/2608.17628_figure.png|800]]

- **arXiv**: [2608.17628](https://arxiv.org/abs/2608.17628)
- **PDF**: https://arxiv.org/pdf/2608.17628
- **详细分析**: [[20_Research/Papers/具身智能/Iterative_Grasp_Pose_Refinement_A_Deep_Reinforcement_Learning_Approach_for_2D_Vision|Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision]]
- **作者**: Amir Arsalan Nematollahi, Shayan Ahmadi, Mehdi Tale Masouleh, Ahmad Kalhor
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 3.32（加权：具身智能 0.9，强化学习 1.56，世界模型 0.16，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Iterative Grasp Pose Refinement: A Deep Reinforcement Learning Approach for 2D Vision》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoppeliaSim, Dex-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Developing robots capable of understanding and manipulating objects requires compact, interpretable, and generalizable representations. This work proposes a reinforcement learning-based framework for robotic grasp refinement, integrating keypoint-based object representations with a Deep Q-Network (DQN). Using 2D overhead images captured in a simulated environment, a geometric-based algorithm generates initial grasp candidates, which are iteratively refined by the proposed framework, transforming failed grasps into successful ones. Experiments conducted on 300 objects from the Dex-Net dataset using a UR5 manipulator demonstrate the framework's effectiveness, achieving a 100% success rate on objects previously deemed ungraspable by geometrical methods. The framework's sim-to-real transferability is further validated through physical experiments on a Delta parallel robot, where a refined grasp successfully manipulates an object that was previously ungraspable. The findings underscore the effectiveness of reinforcement learning in addressing challenges in robotic grasping, offering a scalable and adaptable solution for contact-rich manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/Validated_Adaptation_for_Aerial_Crowd_Monitoring_at_Mass_Gathering_Scale_A_Deployment_Protocol,_a_Severity_Law,_and_a_Diagnostic_for_Label-F|Validated Adaptation for Aerial Crowd Monitoring at Mass Gathering Scale: A Deployment Protocol, a Severity Law, and a Diagnostic for Label-Free Drone Crowd Counting, Toward the FIFA World Cup 2034 (Saudi Arabia)]]

![[assets/2608.17625_figure.jpg|800]]

- **arXiv**: [2608.17625](https://arxiv.org/abs/2608.17625)
- **PDF**: https://arxiv.org/pdf/2608.17625
- **详细分析**: [[20_Research/Papers/强化学习/Validated_Adaptation_for_Aerial_Crowd_Monitoring_at_Mass_Gathering_Scale_A_Deployment_Protocol,_a_Severity_Law,_and_a_Diagnostic_for_Label-F|Validated Adaptation for Aerial Crowd Monitoring at Mass Gathering Scale: A Deployment Protocol, a Severity Law, and a Diagnostic for Label-Free Drone Crowd Counting, Toward the FIFA World Cup 2034 (Saudi Arabia)]]
- **作者**: AlAnoud AllGhayth, AlJawharh AlOtaibi, Jude AlSubaie
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Validated Adaptation for Aerial Crowd Monitoring at Mass Gathering Scale: A Deployment Protocol, a Severity Law, and a Diagnostic for Label-Free Drone Crowd Counting, Toward the FIFA World Cup 2034 (Saudi Arabia)》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CSRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Saudi Arabia will host the 2034 FIFA World Cup and already operates crowd management at Hajj scale. Drone-based counting must hold accuracy on footage unlike anything in its training corpus, without labels, and must warn of dangerous inflow before a crush forms. We deliver a validated answer built on 525 controlled runs, a full-resolution corpus study, five falsification ablations, and a five-condition safety-interlock evaluation. Label-free adaptation recovers 31-49% of shift-induced error across four corruptions and five severities, with the strongest method gaining 41.8 MAE over the frozen source (95% CI [34.1, 49.6], p=7.5x10^-10, d=2.52). We establish a severity law separating methods with a constant absolute margin from the one whose margin grows, and a stability budget identifying which configuration is safe to fly. On a full-resolution corpus carrying a genuine +48 MAE aerial gap (source retrained to 14.6 validation MAE, a 34% improvement), adaptation repairs the dense-scene undercounting that would otherwise under-report a forming crush, and the flux-based risk module fires on real congestion episodes in 2 of 6 full-length clips. We localise the recoverable error: in a regime built to favor a physics-informed conservation prior (300-frame clips at 200ms spacing, five times wider than standard), the adaptation signal is normalisation-driven, not flow-driven; the continuity residual is invariant to the proportional counting errors domain shift produces, confirmed by four on/off ablations correlated at r=0.999 and a 40% input corruption moving accuracy by only 0.05 MAE. A label-free shift gate shows shift magnitude and accuracy damage are rank-independent (Spearman rho=0.20; rho=-0.60 among genuine shifts), quantifying the 58% of headroom a magnitude gate forgoes. We establish unconditional adaptation with tail monitoring as policy, closing with a six-point protocol.

</details>

---

### [[20_Research/Papers/大模型/Multi-turn_Conversational_AI_from_Text_to_Multimodal_Interaction_Data,_Models,_Evaluation,_and_Open_Challenges|Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges]]

![[assets/2608.17605_first_page.png|800]]

- **arXiv**: [2608.17605](https://arxiv.org/abs/2608.17605)
- **PDF**: https://arxiv.org/pdf/2608.17605
- **详细分析**: [[20_Research/Papers/大模型/Multi-turn_Conversational_AI_from_Text_to_Multimodal_Interaction_Data,_Models,_Evaluation,_and_Open_Challenges|Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges]]
- **作者**: Syeda Faiza Ahmed, Zien Sheikh Ali, Hunzalah Hassan Bhatti, Firoj Alam, Shammur Absar Chowdhury
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Multi-turn Conversational AI from Text to Multimodal Interaction: Data, Models, Evaluation, and Open Challenges》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conversational AI is moving beyond isolated text prompts toward sustained, multimodal interaction. In real conversations, users clarify goals, revise requests, interrupt responses, switch topics, and introduce new evidence while expecting systems to preserve context across turns. This makes multi-turn dialogue a distinct challenge requiring systems to maintain and update memory, ground responses across modalities, tools, and external knowledge, and adapt across languages and cultures. This study reviews multi-turn conversational AI across text-only dialogue, AudioLLMs and speech-native systems, multimodal and omni-modal systems, and tool-augmented agents. We organize the literature around datasets and benchmarks, modeling paradigms, training strategies, evaluation setups, and cross-cutting challenges. Our analysis shows that support for multiple modalities has advanced faster than the ability to sustain coherent interaction across a session. Despite stronger capabilities to perceive, speak, and act across modalities, current systems still struggle with persistent memory, cross-turn grounding, full-duplex interaction, robust evaluation, and cultural alignment. We conclude with a research agenda for systems that can remember, revise, ground, speak, listen, act, and adapt across turns, modalities, and cultures. (https://github.com/faiza-sfa/multiturn-conversational-ai-survey)

</details>

---

### [[20_Research/Papers/强化学习/No_Gaussian_Required_Contrastive_Inverse_Dynamics_for_JEPA_World_Models|No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models]]

![[assets/2608.17542_figure.png|800]]

- **arXiv**: [2608.17542](https://arxiv.org/abs/2608.17542)
- **PDF**: https://arxiv.org/pdf/2608.17542
- **详细分析**: [[20_Research/Papers/强化学习/No_Gaussian_Required_Contrastive_Inverse_Dynamics_for_JEPA_World_Models|No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models]]
- **作者**: Jack Boylan, Chris Hokamp
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《No Gaussian Required: Contrastive Inverse Dynamics for JEPA World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn world models by predicting future embeddings, but the objective admits a trivial solution of a constant encoder, so every practical system adds an anti-collapse mechanism (LeCun, 2022; Assran et al., 2023; Bardes et al., 2022; 2024). LeWorldModel (LeWM) prevents collapse with SIGReg, a regularizer that forces the latent distribution to match an isotropic Gaussian: the representation is stabilized by prescribing what it must look like, independently of the environment it models. We argue that the anti-collapse pressure can instead come from the transition data itself. Action-Contrastive Masked Transition Modeling (AC-MTM) keeps LeWM's forward latent-prediction objective and adds a training-only inverse-dynamics head trained with Action-NCE: each latent transition must identify the action that produced it among the other actions in the batch, a discrimination task that a collapsed encoder provably fails. The inverse branch is discarded after training, leaving test-time encoding, forward prediction, planning, and compute identical to LeWM. On four standard pixel-control tasks under a matched planning protocol, AC-MTM trains stably from scratch and matches SIGReg on average. On the harder multi-object OGBench Visual Scene task, results are consistent with the prescribed geometry becoming a bottleneck: AC-MTM reaches 80.0$\pm$2.0% success versus 58.0$\pm$2.0% for SIGReg, improving by 20-24 points in each training seed. A single 50-episode random-policy run gives a 52% baseline estimate. Contrastive inverse dynamics thus provides a distribution-free anti-collapse signal that requires no target network, stop-gradient, pretrained encoder, or reconstruction objective, and we characterize the action-space and observability assumptions under which it holds. We make our code available at https://github.com/jackboyla/action-contrastive-jepa

</details>

---

### [[20_Research/Papers/大模型/CoAL-RAG_A_Complexity-Aware_Legal_Retrieval-Augmented_Generation_Method|CoAL-RAG: A Complexity-Aware Legal Retrieval-Augmented Generation Method]]

![[assets/2608.17536_figure.png|800]]

- **arXiv**: [2608.17536](https://arxiv.org/abs/2608.17536)
- **PDF**: https://arxiv.org/pdf/2608.17536
- **详细分析**: [[20_Research/Papers/大模型/CoAL-RAG_A_Complexity-Aware_Legal_Retrieval-Augmented_Generation_Method|CoAL-RAG: A Complexity-Aware Legal Retrieval-Augmented Generation Method]]
- **作者**: Jin Su, Zhuofeng Zhao, Huanhuan Wang, Hao Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Systems

#### 研究背景与动机

《CoAL-RAG: A Complexity-Aware Legal Retrieval-Augmented Generation Method》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LawBench, SocialLawQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legal consultation questions exhibit multi-level complexity. A single retrieval strategy often leads to over-reasoning for simple questions and poor interpretability for complex ones, making it difficult to meet the requirements for both answer quality and efficiency in high-risk scenarios. To address this issue, this paper proposes CoAL-RAG, a complexity-aware legal retrieval-augmented generation method, which constructs a multi-dimensional evaluation mechanism based on ``question essence'' and ``retrieval consistency'' to enable adaptive routing of retrieval strategies. First, the reasoning demand is quantified according to the logical structure of the question. Then, the discrepancy between semantic retrieval and keyword retrieval is utilized to indirectly reflect problem complexity, thereby selecting the most appropriate retrieval strategy and dynamically filtering contextual information. Experimental results demonstrate that the proposed method significantly outperforms baseline models not only on Chinese legal benchmarks (SocialLawQA, LawBench) but also demonstrates strong cross-jurisdictional generalization on English datasets (LexGLUE, CaseHold). Specifically, on Chinese datasets, the BLEU score improves by 42.5\% and ROUGE-L reaches 3.6 times that of knowledge graph-based methods. On English benchmarks, CoAL-RAG maintains highly competitive accuracy, achieving an optimal balance between generation quality, deep logical reasoning, and system efficiency across different legal systems.

</details>

---

### [[20_Research/Papers/大模型/Agent_Lightning_v1.0_Towards_Harnessed_Agentic_RL|Agent Lightning v1.0: Towards Harnessed Agentic RL]]

![[assets/2608.17528_figure.png|800]]

- **arXiv**: [2608.17528](https://arxiv.org/abs/2608.17528)
- **PDF**: https://arxiv.org/pdf/2608.17528
- **详细分析**: [[20_Research/Papers/大模型/Agent_Lightning_v1.0_Towards_Harnessed_Agentic_RL|Agent Lightning v1.0: Towards Harnessed Agentic RL]]
- **作者**: Zhiyuan He, Siwei Zhang, Zhiwen Zhou, Yuqing Yang, Yu Kang, Yuge Zhang, Luna K. Qiu, Tin Yan Tsui, Jiahang Xu, Chong Luo
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agent Lightning v1.0: Towards Harnessed Agentic RL》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern agents operate inside agent harnesses that manage tools, context, and control flow, making the harness a critical part of the agent system. Our original Agent Lightning introduced a disaggregated architecture that connects arbitrary agents to RL training through an LLM endpoint proxy, an approach later adopted by frameworks such as verl Uni-Agent, AReaL 2.0, slime, and Polar. We refer to this paradigm as harnessed agentic RL, where the deploy-time harness directly participates in model post-training. Harnessed agentic RL differs fundamentally from traditional agentic RL: the harness, rather than the training engine, owns the environment interaction loop, while the trainer observes only sequences of LLM request-response pairs. This introduces challenges in retokenization, sample merging, advantage calculation, loss normalization, and backend scheduling, which can substantially affect training stability and effectiveness. We present Agent Lightning v1.0, a lightweight framework for harnessed agentic RL implemented in approximately 3,500 lines of code. It supports arbitrary agent harnesses and serves as a practical testbed for studying these challenges. We evaluate it on instruction-following, search, and coding agents, and provide a complete reproducible pipeline for coding-agent RL. Using only 6K training examples and modest compute, RL improves Qwen3.5-9B on SWE-bench Verified from 41.8% to 56.4%, a 14.6-point absolute gain. We release the complete workflow and training scripts to facilitate reproducible research on harnessed agentic RL.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Better_Agents_for_Multi-Turn_User_Interaction_The_Next_User_Turn_Is_More_Than_Context|Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context]]

![[assets/2608.17499_figure.png|800]]

- **arXiv**: [2608.17499](https://arxiv.org/abs/2608.17499)
- **PDF**: https://arxiv.org/pdf/2608.17499
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Better_Agents_for_Multi-Turn_User_Interaction_The_Next_User_Turn_Is_More_Than_Context|Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context]]
- **作者**: Yiwen Zhao, Zhihao Wen, Yuchen Mao, Mingxuan Jiang, Yihao Hu, Pan Wang, Xin Zhang, Wei Wu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Towards Better Agents for Multi-Turn User Interaction: The Next User Turn Is More Than Context》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Co-Gym, MUA-RL, Pare-Bench, Simia-RL, UserRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

User-facing tool agents must coordinate dialogue and tool use as user goals unfold over multiple turns. Yet interactive reinforcement learning typically reduces each rollout to a terminal reward, assigning the same credit to effective elicitation, errors, and later repair. The next user turn is more than context: it also provides noisy, temporally local evidence about the preceding user-to-user segment. We introduce \textbf{F}eedback-\textbf{A}ware \textbf{C}redit \textbf{A}ssignment (\textsc{FACA}), which aligns each reaction with that segment, derives a locally normalized reaction advantage, and adds it to verified terminal outcome advantage without an extra critic or rollout. Against an outcome-only Interactive GRPO control matched in simulator, visible dialogue, initialization, rollout, and optimization, \textsc{FACA} improves the nine-domain $τ$-family average across three independently trained runs by 5.91 and 10.22 percentage points at 8B and 14B, respectively. Gains concentrate in Telecom; at 8B, randomizing reaction polarity removes the Telecom gain. The same ordering holds zero-shot on Pare-Bench and Co-Gym. These results demonstrate that next-turn user reactions provide actionable local credit for improving multi-turn user-interacting agents.

</details>

---

### [[20_Research/Papers/大模型/Task-Aware_Harness_Provisioning_for_LLM_Agents_in_Mission-Critical_Infrastructure_Operations|Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations]]

![[assets/2608.17433_figure.png|800]]

- **arXiv**: [2608.17433](https://arxiv.org/abs/2608.17433)
- **PDF**: https://arxiv.org/pdf/2608.17433
- **详细分析**: [[20_Research/Papers/大模型/Task-Aware_Harness_Provisioning_for_LLM_Agents_in_Mission-Critical_Infrastructure_Operations|Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations]]
- **作者**: Liangtao Lin, Qingang Zhang, Zhaomeng Zhu, Tianwei Zhang, Yonggang Wen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Task-Aware Harness Provisioning for LLM Agents in Mission-Critical Infrastructure Operations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AssetOpsBench, Harness-Bench, ToolPrivBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents have been widely adopted to operate mission-critical infrastructure (MCI). These agents normally rely on a harness that determines what information they can access, which tools they can use, and what actions they can take. Existing systems often expose the same comprehensive harness to every task, which may not be necessary and cause resource wastes. In this paper, we focus on the identification of optimal harness configurations, and view it as a resource-matching problem between what each task requires and what the harness provides. To measure this match, we classify MCI tasks based on the mathematical representation of the underlying system and rank harness configurations by the amount and type of information they provide. We then construct task-to-harness mappings from two sources: mining research literature and measuring controlled agent execution. Leveraging the measured mapping, we propose a new harness provisioning algorithm: map-guided escalation. It begins with a task-specific harness and expands to full provision only after a failed self-check. We evaluate our method in two representative MCI tasks: in liquid cooling, it improves the agent accuracy from 0.652 under full provision to 0.715 and achieves accuracy comparable to Reflexion with 48% fewer tokens; In power grids, full provision remains accuracy-optimal, while map-based provisioning offers lower-cost alternatives. These findings show that harness provisioning follows a domain-dependent accuracy-cost Pareto frontier rather than a universal optimum.

</details>

---

### [[20_Research/Papers/大模型/LEGO-RL_Harness-Native_Reinforcement_Learning_for_Coding_Agents|LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents]]

![[assets/2608.17393_figure.png|800]]

- **arXiv**: [2608.17393](https://arxiv.org/abs/2608.17393)
- **PDF**: https://arxiv.org/pdf/2608.17393
- **详细分析**: [[20_Research/Papers/大模型/LEGO-RL_Harness-Native_Reinforcement_Learning_for_Coding_Agents|LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents]]
- **作者**: Yiming Du, Yuxin Jiang, Tao Yuan, Jianbo Dai, Shaowei Wang, Jierun Chen, Chaofan Tao, Xianzhi Yu, Lifeng Shang, Kam-Fai Wong, Xiaohui Li, Haoli Bai
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《LEGO-RL: Harness-Native Reinforcement Learning for Coding Agents》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LEGO-RL, LLM-RL, Lego-RL, OpenForgeRL, R2E-Gym, SWE-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning for coding agents increasingly relies on long-running agent harnesses to manage tool integration, repository contexts, and execution feedback. However, the native execution environments of these harnesses are inherently misaligned with policy-gradient training: environmental crashes and reward hacking corrupt outcome signals, while train-inference discrepancies decouple rollout behavior from policy updates. To address this, we present LEGO-RL, a framework that bridges native coding-agent harnesses with scalable policy-gradient optimization without modifying their internal control flow. LEGO-RL is built upon three pillars: (1) faithful optimization via in-process LLM proxying that captures raw generation streams for token-level alignment and robust trainer-side log-probability recomputation, even under harness-side compaction or re-serialization; (2) reliable execution via scalable sandbox orchestration featuring image caching and stage-wise defenses to mitigate reward hacking; and (3) observable training through an integrated plugin that automates validation and monitoring, paired with a Live UI for granular trajectory diagnostics. We evaluate LEGO-RL by training the sparse MoE model Qwen3.5-35B-A3B with GSPO across three native coding-agent harnesses. LEGO-RL improves Qwen3.5-35B-A3B across OpenHands SDK (64.0% to 70.4%), Claude Code (62.4% to 68.2%), and OpenCode (57.2% to 66.6%) on SWE-bench Verified, while maintaining a rollout-training probability correlation above 0.99.

</details>

---

### [[20_Research/Papers/强化学习/Integrating_Novelty_and_Surprise_for_Experience_Prioritization_and_Exploration_in_Image-Based_Reinforcement_Learning|Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning]]

![[assets/2608.17373_figure.png|800]]

- **arXiv**: [2608.17373](https://arxiv.org/abs/2608.17373)
- **PDF**: https://arxiv.org/pdf/2608.17373
- **详细分析**: [[20_Research/Papers/强化学习/Integrating_Novelty_and_Surprise_for_Experience_Prioritization_and_Exploration_in_Image-Based_Reinforcement_Learning|Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning]]
- **作者**: Hoda Yamani, Henry Williams, Bruce A. MacDonald
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Integrating Novelty and Surprise for Experience Prioritization and Exploration in Image-Based Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sample efficiency is a central challenge in reinforcement learning (RL), particularly in image-based domains where agents must learn from high-dimensional visual inputs. Traditional sampling often relies on random or suboptimal experience selection, leading to redundant updates and slow learning. Improving efficiency requires mechanisms that prioritize informative experiences while also encouraging effective exploration. Prioritized Experience Replay (PER) addresses part of this challenge by reusing high-value transitions, while intrinsic rewards promote the exploration of novel or uncertain states. However, their integration has not been extensively studied. This paper introduces Novelty and Surprise Prioritized Experience Replay (NSPER), which uses novelty to capture underrepresented states and surprise to expose gaps in the agent's understanding of the environment. We further extend this with NSPER+R, integrating these signals as intrinsic rewards to jointly improve replay quality and exploration. Experiments on DeepMind Control Suite tasks show that NSPER and NSPER+R improve training efficiency and convergence speed compared to existing methods in image-based RL.

</details>

---

### [[20_Research/Papers/具身智能/ORPA_Online_Residual_Policy_Adaptation_for_Robot_Manipulation_Control_with_Human_Feedback|ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback]]

![[assets/2608.17323_figure.png|800]]

- **arXiv**: [2608.17323](https://arxiv.org/abs/2608.17323)
- **PDF**: https://arxiv.org/pdf/2608.17323
- **详细分析**: [[20_Research/Papers/具身智能/ORPA_Online_Residual_Policy_Adaptation_for_Robot_Manipulation_Control_with_Human_Feedback|ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback]]
- **作者**: Muhammad A. Muttaqien, Tomohiro Motoda, Ryo Hanai, Yukiyasu Domae
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《ORPA: Online Residual Policy Adaptation for Robot Manipulation Control with Human Feedback》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation policies trained via imitation learning, such as Action Chunking with Transformers (ACT), can achieve strong performance under ideal conditions but often remain sensitive to small execution errors and distribution shifts. Correcting these failures typically requires dataset aggregation and full-policy retraining, which is computationally expensive and unsuitable for real-time deployment. In this work, we propose Online Residual Policy Adaptation (ORPA), a framework that enables immediate, feedback-driven correction of robot actions without modifying the underlying policy parameters. ORPA augments a pretrained control policy with a lightweight, feedback-conditioned module that predicts residual adjustments directly in joint space, allowing the system to adapt its behavior at runtime. We evaluate ORPA on a set of precision-sensitive manipulation tasks using the ALOHA platform, demonstrating improvements in success rate and recovery from small perturbations compared to baseline control policies and rule-based inverse kinematics corrections.

</details>

---

### [[20_Research/Papers/强化学习/Wuying-Browser-Agent_Real-World_Centric_Fundamental_Long-Horizon_Browser_Agents|Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents]]

![[assets/2608.17319_figure.png|800]]

- **arXiv**: [2608.17319](https://arxiv.org/abs/2608.17319)
- **PDF**: https://arxiv.org/pdf/2608.17319
- **详细分析**: [[20_Research/Papers/强化学习/Wuying-Browser-Agent_Real-World_Centric_Fundamental_Long-Horizon_Browser_Agents|Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents]]
- **作者**: AIMAE Team, Tianxiang Chen, Yan Cheng, Zhangye Han, Xiaowei Li, Chang Liu, Cheng Liu, Zhongqiang Ma, Long Peng, Xiaobing Tu, Yinggui Wang, Hongliang Wei...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Wuying-Browser-Agent: Real-World Centric Fundamental Long-Horizon Browser Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentRL, BrowserBench, Claw-Eval, OpenWebRL, Real-World, Tau2-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Browser agents perform well on short, clean demonstrations, but real deployment is fundamentally different: agents must sustain dozens of decisions on live websites while recovering from mistakes and navigating complex UIs. We argue that closing this gap requires alignment at every level of the pipeline, including execution, supervision, optimization, and evaluation, rather than scale alone. We present Wuying-Browser-Agent, a unified framework that addresses each of these levels. A structured browser harness provides stable execution primitives and decision-oriented context management. Reflection and UI-specialized Curriculum SFT (RUIC-SFT) explicitly trains on recovery trajectories and complex-UI interactions. Divergence-Aware Online GRPO (DAO-GRPO) improves long-horizon credit assignment through potential-based reward shaping and divergence-aware step weighting. Finally, we introduce BrowserBench, a bilingual real-web benchmark of 350 tasks averaging 37.9 steps, because most existing benchmarks are too short to expose long-horizon failure modes. Wuying-Browser-Agent-27B achieves 80.6\% on WebVoyager, 66.7\% on Online-Mind2Web, and 65.1\% on BrowserBench, establishing a new open-source state of the art on browser-use benchmarks. The same pipeline also transfers beyond browser use, demonstrating strong general agentic ability and reaching an average score of 73.8 on Tau2-Bench, Claw-Eval, and BFCL-v4.

</details>

---

### [[20_Research/Papers/强化学习/PlanPO_Group_Planning-Aware_Policy_Optimization_for_Multi-Turn_Agentic_LLMs|PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs]]

![[assets/2608.17289_figure.png|800]]

- **arXiv**: [2608.17289](https://arxiv.org/abs/2608.17289)
- **PDF**: https://arxiv.org/pdf/2608.17289
- **详细分析**: [[20_Research/Papers/强化学习/PlanPO_Group_Planning-Aware_Policy_Optimization_for_Multi-Turn_Agentic_LLMs|PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs]]
- **作者**: Dayang Liang, Liyuan He, Xuan Feng, Shuxin Li, Bo An, Yunlong Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《PlanPO: Group Planning-Aware Policy Optimization for Multi-Turn Agentic LLMs》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, SciWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group-relative policy optimization has emerged as a key paradigm for training agentic large language models (LLMs) on multi-turn interactive tasks. However, most existing variants fail to distinguish advantages among successful trajectories even when these trajectories differ substantially in their interaction efficiency. For instance, circuitous successes are often assigned the identical outcome reward, causing advantage collapse and severe performance bottlenecks. To this end, we propose Group Planning-aware Policy Optimization (PlanPO), a simple yet effective RL method for learning generalizable planning abilities beyond task-specific high-quality behavior patterns. Specifically, PlanPO introduces coarse-to-fine advantage signals, which capture the relative differences in trajectory-level lengths and turn-level response lengths conditioned on successful trajectories sampled for the same task. Within the group-relative optimization structure, this enables agents to actively learn generalizable and deliberate behaviors spanning interaction planning and textual generation from high-quality rollouts, without degenerating into vanilla length minimization. Experimentally, PlanPO improves over GRPO by 27.2\% on average across the challenging multi-turn benchmarks ALFWorld, WebShop, and SciWorld, outperforming recent powerful baselines while incurring negligible additional training cost.

</details>

---

### [[20_Research/Papers/大模型/Co-RL_Unsupervised_Reasoning_Emerges_from_Diverse_Cohort_in_Multi-agent_RL|Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL]]

![[assets/2608.17253_first_page.png|800]]

- **arXiv**: [2608.17253](https://arxiv.org/abs/2608.17253)
- **PDF**: https://arxiv.org/pdf/2608.17253
- **详细分析**: [[20_Research/Papers/大模型/Co-RL_Unsupervised_Reasoning_Emerges_from_Diverse_Cohort_in_Multi-agent_RL|Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL]]
- **作者**: Yunhao Yang, Yuexin Bian, Yunjie Tian, Di Fu, Tianjin Huang, Yuanyuan Shi, Ziang Xiao, Nuno Vasconcelos, Yijiang Li
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Co-RL: Unsupervised Reasoning Emerges from Diverse Cohort in Multi-agent RL》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Co-RL, MAPoRL, TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has emerged as a powerful approach for improving reasoning in language and vision-language models, yet its strongest successes still depend heavily on ground-truth supervision (e.g., verifiable reward). Such annotations are costly to obtain and become increasingly scarce as reasoning capabilities advance beyond what humans can reliably evaluate. Self-rewarding RL reduces this dependence by enabling models to derive reward signals from their own completions. However, training solely on self-generated feedback can reinforce existing biases and suboptimal behaviors, reduce response diversity, and ultimately lead to homogenized responses and training collapse. In this work, we show that unsupervised reasoning can emerge through cooperative multi-agent training. We introduce Co-RL, a framework in which multiple decoupled models, sharing no parameters, are simultaneously optimized through RL using rewards derived from their peers. We further show that increasing cohort diversity, through heterogeneous model families, sizes, and rephrased training samples, reduces the correlated errors that drive self-reinforcing feedback loops. This diversity consistently improves reasoning performance, maintains behavioral diversity, and mitigates training collapse. Across text-only and multimodal domains, Co-RL consistently outperforms the base models and prior label-free approaches, while matching or surpassing supervised methods, without access to any ground-truth labels. Concretely, Co-RL yields average gains of 3.0-8.6% across seven text-only benchmarks for LLMs and 2.3-7.2% across four multimodal benchmarks for VLMs. Code is available at https://github.com/DrStranded/Co-RL.

</details>

---

### [[20_Research/Papers/大模型/PACE_Policy-Attested_Contract_Execution_for_Safe_AI_Agents_in_Decentralized_Finance|PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance]]

![[assets/2608.17220_first_page.png|800]]

- **arXiv**: [2608.17220](https://arxiv.org/abs/2608.17220)
- **PDF**: https://arxiv.org/pdf/2608.17220
- **详细分析**: [[20_Research/Papers/大模型/PACE_Policy-Attested_Contract_Execution_for_Safe_AI_Agents_in_Decentralized_Finance|PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance]]
- **作者**: Rabimba Karanjai, Yang Lu, Richard Williamson, Hemanth Hm, Prakhar Mehrotra, Lei Xu, Weidong, Shi
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《PACE: Policy-Attested Contract Execution for Safe AI Agents in Decentralized Finance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous AI agents are emerging as interfaces for decentralized finance (DeFi) actions such as swaps, lending operations, and yield management. Because these agents rely on large language models (LLMs) to plan transactions, they inherit the LLM's susceptibility to prompt injection and lack of mechanisms to bind a verifier's approval to the exact transaction ultimately submitted on-chain. We present PACE (Policy-Attested Contract Execution), a transaction-level authorization framework that interposes between an LLM-based agent and on-chain execution. PACE introduces typed transaction intents, a deterministic policy verifier, and signed Policy Decision Records (PDRs) that cryptographically bind the approved intent, policy, and simulation report to the exact execution bytes, with replay and expiration protection. A Solidity smart account enforces PDR signatures on-chain with a measured overhead of 29,826-31,822 gas. We evaluate PACE against six baselines on 40 tasks spanning four attack categories plus benign utility (2,800 trials, 10 seeds). In our deterministic sandbox, PACE achieves a 0.00 unsafe execution rate and 0.00 false-positive rate on benign tasks, compared to 0.80 for the unguarded baseline. Ablation studies identify permissive policy settings (+57.5 pp) and the touched-contract allowlist (+12.5 pp) as the dominant safety components. To test whether the same deterministic floor holds for real model outputs, the artifact additionally provides a three-model live-LLM evaluation over the full task suite with repeated runs. A mainnet-fork harness is included for archive-RPC deployments, but fork results are reported only when the corresponding artifacts are generated. These auxiliary studies are separate from, and never substitute for, the deterministic benchmark. We frame our claims as logic-level safety within a reproducible benchmark rather than deployment-ready DeFi security.

</details>

---

### [[20_Research/Papers/具身智能/Teach_and_Grow_An_Agent-Centered_Architecture_for_General_Robot_Learning|Teach and Grow: An Agent-Centered Architecture for General Robot Learning]]

![[assets/2608.17209_first_page.png|800]]

- **arXiv**: [2608.17209](https://arxiv.org/abs/2608.17209)
- **PDF**: https://arxiv.org/pdf/2608.17209
- **详细分析**: [[20_Research/Papers/具身智能/Teach_and_Grow_An_Agent-Centered_Architecture_for_General_Robot_Learning|Teach and Grow: An Agent-Centered Architecture for General Robot Learning]]
- **作者**: Chang Nie, Zhe Liu, Hesheng Wang
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.2，大模型 0.5，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Teach and Grow: An Agent-Centered Architecture for General Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end vision-language-action (VLA) and world-action models offer an elegant route to general-purpose robotics, but their reliability is bounded by validated physical coverage. When an unfamiliar object, sensor, embodiment, or contact falls outside that coverage and no validated fallback exists, correcting the failure requires new robot data, a policy update, and regression testing. This recurring burden is the retraining tax. Unlike text, embodied data must often be created by operating machines. We present Teach-and-Grow Learning (TGL), an agent-centered architecture for general robot learning. In its general form, a multimodal agent turns a few successful demonstrations into reusable Skill Blocks: closed-loop behaviors for meaningful subgoals. In a new scene, the agent grounds and composes these blocks, selects learned or geometric tools, observes the physical outcome, and revises the route when execution departs from intent. A Skill Library stores executable behavior, while structured Experience Memory carries forward success, failure, and repair. New tasks are acquired without task-specific policy retraining. Our LIBERO evaluation attains state-of-the-art performance; controlled studies expose skill induction, persistent reuse, and agent-directed adaptation. Finally, we propose the Teach-and-Grow scaling-law hypothesis: if X denotes effective reusable experience, future-task error and teaching demand should approach irreducible floors as power laws in X. The architecture therefore treats deployment as a period of continued learning, in which one task can make the next easier.

</details>

---

### [[20_Research/Papers/大模型/Token_Optimization_and_Context_Window_Management_in_Multi-Agent_AI_Workflows|Token Optimization and Context Window Management in Multi-Agent AI Workflows]]

![[assets/2608.17188_first_page.png|800]]

- **arXiv**: [2608.17188](https://arxiv.org/abs/2608.17188)
- **PDF**: https://arxiv.org/pdf/2608.17188
- **详细分析**: [[20_Research/Papers/大模型/Token_Optimization_and_Context_Window_Management_in_Multi-Agent_AI_Workflows|Token Optimization and Context Window Management in Multi-Agent AI Workflows]]
- **作者**: Dvir Shamay
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent

#### 研究背景与动机

《Token Optimization and Context Window Management in Multi-Agent AI Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent AI workflows are limited not only by model quality but by token cost, latency, and context-window quality. This paper presents a practitioner framework for token optimization and context-window management, grounded in an internal production dashboard that extracts structured work items from meetings, email, and chat with LLMs and routes summaries across workstreams. Six patterns are described: context stratification, fetch-once/process-locally architecture, schema-contracted prompts, token-aware fallback chains, semantic caching, and inter-agent communication compression. In production they cut measured cold-load latency to 61-116 seconds (six timed runs) from an operational baseline of roughly 3.5-10.5 minutes, with an estimated 60-70% token reduction. It also reports a controlled context-composition study: 2,420 confirmatory trials across 11 model configurations, using 661 anonymized workplace items scored for relevance. Holding the prompt at a fixed ten items, replacing some high-relevance items with same-domain low-relevance items improves the model's relevance-score concordance on the target items, versus high-relevance items only; we call this relevance-contrast context. In the all-11 paired analysis, the 50:50 signal/noise condition improved relevance accuracy by +0.077 over the 100% condition (naive 95% CI [+0.056, +0.098], Cohen's d = 0.49, Holm-adjusted p &lt; .001, n = 220). These cells are not independent; by the nine model families the effect is +0.084 (95% interval [+0.064, +0.103]), reported as a within-corpus descriptive comparison, not a population inference. A Fusion-of-N follow-up found that learned synthesis did not beat the mechanical set union of item IDs. The contribution is a measured engineering layer between model research and production agent practice: repeatable patterns and evaluation methods for faster, cheaper, more reliable workflows.

</details>

---

### [[20_Research/Papers/大模型/Task_Specialization_Fine-Tuning_for_Contextual_Reinforcement_Learning|Task Specialization Fine-Tuning for Contextual Reinforcement Learning]]

![[assets/2608.17180_figure.png|800]]

- **arXiv**: [2608.17180](https://arxiv.org/abs/2608.17180)
- **PDF**: https://arxiv.org/pdf/2608.17180
- **详细分析**: [[20_Research/Papers/大模型/Task_Specialization_Fine-Tuning_for_Contextual_Reinforcement_Learning|Task Specialization Fine-Tuning for Contextual Reinforcement Learning]]
- **作者**: Jianan Zhou, Jung-Hoon Cho, Tianyue Zhou, Han Zheng, Jie Zhang, Roy Dong, Yining Ma, Cathy Wu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Task Specialization Fine-Tuning for Contextual Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CRL, PEARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contextual Reinforcement Learning (CRL) seeks to generalize classical RL by maximizing task coverage across a context space of related tasks. While prior works often train from scratch and rely on either multi-task learning for a single policy or strategically training multiple policies, we advocate for a unified alternative: pretraining a single policy with good initial performance, followed by fine-tuning multiple policies for task specialization. This new paradigm, however, introduces unique challenges, such as heterogeneous marginal returns and sample inefficiency. This raises a critical research question: given a pretrained policy and a constrained budget, how much fine-tuning should each task region receive to enable sample-efficient CRL? To this end, we propose Task Specialization Fine-Tuning (TSFT), an online framework that predicts fine-tuning performance with a simple parametric model and exactly solves the resulting discrete budget allocation problem via integer linear programming. Extensive experiments across diverse decision domains, including combinatorial optimization, continuous control, and LLM fine-tuning, demonstrate that TSFT significantly outperforms baselines in task coverage and approaches oracle performance. Our work charts a new direction for model-based CRL, aligning with the modern pretrain-finetune era.

</details>

---

### [[20_Research/Papers/具身智能/Q-Learning_With_World_Models|Q-Learning With World Models]]

![[assets/2608.17163_figure.png|800]]

- **arXiv**: [2608.17163](https://arxiv.org/abs/2608.17163)
- **PDF**: https://arxiv.org/pdf/2608.17163
- **详细分析**: [[20_Research/Papers/具身智能/Q-Learning_With_World_Models|Q-Learning With World Models]]
- **作者**: Perry Dong, Yueru Jia, Chelsea Finn, Dorsa Sadigh
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 具身智能, 机器人
- **相关性评分**: 2.62（加权：具身智能 0.3，强化学习 1.16，世界模型 0.96，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Q-Learning With World Models》归入 强化学习、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：World-VLA, World4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Off-policy reinforcement learning (RL) has become increasingly sample-efficient, enabling applications such as RL fine-tuning of Vision-Language-Action models into reliable, high-performing policies. World models offer a further lever for sample efficiency, as they predict state changes rather than actions alone, but their success has largely been confined to supervised policy learning. Prior model-based RL methods often optimize the policy or value function directly on imagined rollouts, which is prone to compounding bias and struggles to scale to large, high-dimensional problems such as real-world robotics, a problem that worsens with task horizon and visual complexity. In this work, we instead ask whether we can leverage world models directly on top of standard Q-learning to improve performance, while remaining trained and grounded in the real, online setting. We propose QWM, a framework that leverages world models to perform test-time search over imagined trajectories on top of Q-learning to select high-value actions during both online rollouts and evaluation. Since the policy and value function are trained only on real transitions, QWM avoids compounding model bias while still gaining the sample-efficiency benefits of predictive search. On challenging manipulation benchmarks Robomimic and LIBERO, QWM significantly outperforms strong prior state-of-the-art methods on both sample efficiency and performance.

</details>

---

### [[20_Research/Papers/大模型/Institution-Specific_LLM_Prompting_Recovers_PHI_That_De-identification_Systems_and_Their_Gold_Standards_Both_Miss|Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss]]

![[assets/2608.17051_figure.png|800]]

- **arXiv**: [2608.17051](https://arxiv.org/abs/2608.17051)
- **PDF**: https://arxiv.org/pdf/2608.17051
- **详细分析**: [[20_Research/Papers/大模型/Institution-Specific_LLM_Prompting_Recovers_PHI_That_De-identification_Systems_and_Their_Gold_Standards_Both_Miss|Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss]]
- **作者**: Daniel Palacios, Matthew Brady Neeley, Angel Adetomike Otto, Shalini Dhamodharan, John P. Woodhouse, Chi-fan Lin, Mark Zobeck, Zhandong Liu, Hyun-Hwan Jeong
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Institution-Specific LLM Prompting Recovers PHI That De-identification Systems and Their Gold Standards Both Miss》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Secondary use of electronic health records requires de-identification, yet existing systems miss \emph{institutionally situated} protected health information (PHI) such as hospital abbreviations, building names, and internal codes whose status is locally determined. We ask whether large language models (LLMs) with in-context learning (ICL) can close this gap and control the precision--recall trade-off. On 100 annotated pediatric oncology notes (5,322 PHI spans) from Texas Children's Hospital, we benchmarked eight LLMs against two purpose-built systems (Stanford TiDE, OpenMed PII) and two pattern-based baselines. Each LLM ran under three prompts of increasing specificity: (1) a HIPAA-aligned baseline, (2) baseline plus the institutional PHI categories it missed, and (3) prompt 2 plus instructions against over-redacting clinical content. We then compared 14~multi-agent and ensemble configurations against the best single prompt, with recall the primary safety metric. LLMs outperformed the purpose-built systems (best F1=0.918$\pm$0.001 vs.\ TiDE 0.779), with advantages concentrated in contextual categories. Naming the missed categories recovered 79\% (48/61) of them, and discouraging over-redaction restored precision. No agentic architecture beat calibrated single-pass prompting (F1 0.906--0.907), but LLM outputs surfaced 414~candidate annotation gaps; re-annotation confirmed 227~PHI spans, against which the final prompt reached recall=0.981 (F1=0.907$\pm$0.002). Well-calibrated ICL resolves both the institutional PHI gap and the precision--recall trade-off in one LLM call per note. LLMs cost more to run than traditional methods, but that cost buys a way to audit the reference standard. LLMs are a legitimate, adaptable alternative to purpose-built de-identification systems; institution-specific prompt development should be the primary adaptation strategy.

</details>

---

### [[20_Research/Papers/大模型/WIP_LLM_Odyssey_A_Game-Based_Platform_for_Teaching_LLM_Engineering_Concepts|WIP: LLM Odyssey: A Game-Based Platform for Teaching LLM Engineering Concepts]]

![[assets/2608.16924_figure.png|800]]

- **arXiv**: [2608.16924](https://arxiv.org/abs/2608.16924)
- **PDF**: https://arxiv.org/pdf/2608.16924
- **详细分析**: [[20_Research/Papers/大模型/WIP_LLM_Odyssey_A_Game-Based_Platform_for_Teaching_LLM_Engineering_Concepts|WIP: LLM Odyssey: A Game-Based Platform for Teaching LLM Engineering Concepts]]
- **作者**: Priyamvada Tripathi
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《WIP: LLM Odyssey: A Game-Based Platform for Teaching LLM Engineering Concepts》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work-in-progress (WIP) innovative practice category paper presents LLM Odyssey, an open source, browser-based serious gaming platform comprising 13 interactive games for teaching Large Language Model (LLM) engineering concepts. Topics such as tokenization, transformer architecture, prompt engineering, retrieval augmented generation (RAG), and production deployment are underrepresented in computer science curricula. Existing interactive tools address individual concepts but lack pedagogical scaffolding or structured learning pathways. LLM Odyssey addresses this gap through three learning tiers aligned with Bloom's revised taxonomy: Cognitive Core (7 foundational games), Systems Forge (5 production engineering games), and Foundry Arena (capstone challenges). Each game incorporates five pedagogical strategies drawn from the literature: immediate formative feedback, scaffolded hints grounded in the Zone of Proximal Development, progressive difficulty informed by flow theory, worked examples to manage cognitive load, and authentic scenarios drawn from production practice. The platform was deployed in Winter 2026 semester at a Canadian college for an initial review. Feedback confirmed functional requirements and identified adaptive difficulty as a priority for future development. A formal mixed methods evaluation protocol (N=50) has been designed, comprising pre and post knowledge tests, validated surveys, engagement analytics, and interviews, and is documented here to enable future evaluation studies with the publicly available platform.

</details>

---

### [[20_Research/Papers/大模型/Effective_Personalized_AI_Tutors_via_LLM-Guided_Reinforcement_Learning|Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning]]

![[assets/2608.16907_figure.png|800]]

- **arXiv**: [2608.16907](https://arxiv.org/abs/2608.16907)
- **PDF**: https://arxiv.org/pdf/2608.16907
- **详细分析**: [[20_Research/Papers/大模型/Effective_Personalized_AI_Tutors_via_LLM-Guided_Reinforcement_Learning|Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning]]
- **作者**: Angel Tsai-Hsuan Chung, Botong Zhang, Ling-Chieh Kung, Hamsa Bastani, Osbert Bastani
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Effective Personalized AI Tutors via LLM-Guided Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative AI (GenAI) is rapidly reshaping education by unlocking the potential for personalized tutoring. Yet, emerging platforms largely focus on GenAI chatbot tutors that reactively answer student questions. We hypothesize that the efficacy of GenAI chatbot tutors can be substantially improved by proactively guiding student learning. To test this, we design a novel tutoring platform that tightly integrates a carefully-designed GenAI chatbot with a reinforcement learning algorithm for sequencing practice problems. Critically, this algorithm leverages rich signals from student-chatbot interactions to adaptively select practice problems of an appropriate difficulty level. In partnership with the Taipei City Government and American Institute in Taiwan, we deployed our tutoring platform in conjunction with a five-month course to teach Python to students across ten high schools. We randomized students between a fixed practice problem sequence and our adaptive sequencing algorithm. We find that adaptive sequencing increased unassisted final exam performance by 0.15 standard deviations (equivalent to 6-9 months of schooling by some estimates); mediation analysis suggests that gains were driven by increased engagement. Our work provides large-scale field evidence that student-chatbot interactions provide valuable signals for proactively optimizing and personalizing student learning.

</details>

---

### [[20_Research/Papers/大模型/CityReal_Human-Aligned_Urban_Behavior_and_City_Dynamics_Simulation_with_Large-Scale_LLM_Agents|CityReal: Human-Aligned Urban Behavior and City Dynamics Simulation with Large-Scale LLM Agents]]

![[assets/2608.16897_figure.png|800]]

- **arXiv**: [2608.16897](https://arxiv.org/abs/2608.16897)
- **PDF**: https://arxiv.org/pdf/2608.16897
- **详细分析**: [[20_Research/Papers/大模型/CityReal_Human-Aligned_Urban_Behavior_and_City_Dynamics_Simulation_with_Large-Scale_LLM_Agents|CityReal: Human-Aligned Urban Behavior and City Dynamics Simulation with Large-Scale LLM Agents]]
- **作者**: Nicolas Bougie, Xiaotong Ye, Narimasa Watanabe
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CityReal: Human-Aligned Urban Behavior and City Dynamics Simulation with Large-Scale LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CityBench, CitySim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale urban simulation plays a pivotal role in social science, traffic safety, and transportation policy. Recent work has shown that large language models, when prompted as agents, can generate lifelike daily routines at city scale. Yet these methods typically rely on few-shot prompting, causing agents to reproduce the LLM's behavioral priors rather than the target population. We introduce CityReal, a modular framework for human-aligned urban simulation. CityReal models agents as intention-driven decision makers that pursue coherent mobility and activity plans rather than isolated step-by-step choices. They adapt over time by learning habits and preferences based on experience and constraints. To improve population-level realism, we learn textual adapters for behavior modules that align agent decisions with observed population statistics. Experiments show that CityReal improves alignment with real-world human behavior at both micro and macro levels. Scaling to tens of thousands of agents, it supports analysis of crowd density, place popularity, mobility flows, and well-being under different urban scenarios, offering a scalable testbed for urban simulation and forecasting.

</details>

---

### [[20_Research/Papers/大模型/GxP-Agent_Process-DAG_Topology_for_Reliable_Clinical_Trial_Programming_with_LLM_Agents|GxP-Agent: Process-DAG Topology for Reliable Clinical Trial Programming with LLM Agents]]

![[assets/2608.16890_first_page.png|800]]

- **arXiv**: [2608.16890](https://arxiv.org/abs/2608.16890)
- **PDF**: https://arxiv.org/pdf/2608.16890
- **详细分析**: [[20_Research/Papers/大模型/GxP-Agent_Process-DAG_Topology_for_Reliable_Clinical_Trial_Programming_with_LLM_Agents|GxP-Agent: Process-DAG Topology for Reliable Clinical Trial Programming with LLM Agents]]
- **作者**: Jaime Yan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《GxP-Agent: Process-DAG Topology for Reliable Clinical Trial Programming with LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CDISC-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clinical trial programming -- transforming study protocols into analysis-ready datasets under CDISC standards -- is a bottleneck in regulatory submissions, yet LLM-based code generation fails catastrophically on this task: across 11 single-shot attempts with five frontier models, none produces a valid subject-level analysis dataset. We introduce GxP-Agent, a multi-agent system that encodes regulatory process ordering as a directed acyclic graph (DAG), decomposing monolithic dataset generation into 15 domain-specific nodes executed by worker agents with pharmaverse skill context, validation gates, and conditional retry. On CDISC-Bench, a new execution-based benchmark built from the FDA pilot submission CDISCPilot01 (254 subjects, 49 ground-truth ADSL variables), GxP-Agent with Claude Sonnet 4.6 achieves 100% structural match (49/49 variables, 254 correct records) across three independent runs, compared to 59.2% for the best retrieval-augmented baseline and 0% for all single-agent and flat multi-agent approaches. The DAG topology also enables weaker models: GPT-4.1 achieves 59.2% mean structural match under the same DAG, where it scores 0% under every other architecture. The approach generalizes to ADAE (adverse events; 9-node branching DAG, 55 variables, 1,191 records), achieving 100% structural match on the first attempt. These results demonstrate that encoding domain process knowledge as graph topology -- rather than relying on LLM reasoning alone -- is a key enabler for reliable, GxP-compliant clinical trial programming.

</details>

---

### [[20_Research/Papers/大模型/Intent-Driven_Dynamic_Chunking_Segmenting_Documents_to_Reflect_Predicted_Information_Needs|Intent-Driven Dynamic Chunking: Segmenting Documents to Reflect Predicted Information Needs]]

![[assets/2602.14784_figure.png|800]]

- **arXiv**: [2602.14784](https://arxiv.org/abs/2602.14784)
- **PDF**: https://arxiv.org/pdf/2602.14784
- **详细分析**: [[20_Research/Papers/大模型/Intent-Driven_Dynamic_Chunking_Segmenting_Documents_to_Reflect_Predicted_Information_Needs|Intent-Driven Dynamic Chunking: Segmenting Documents to Reflect Predicted Information Needs]]
- **作者**: Christos Koutsiaris
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Intent-Driven Dynamic Chunking: Segmenting Documents to Reflect Predicted Information Needs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：NewsQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Breaking long documents into smaller segments is a fundamental challenge in information retrieval. Whether for search engines, question-answering systems, or retrieval-augmented generation (RAG), effective segmentation determines how well systems can locate and return relevant information. However, traditional methods, such as fixed-length or coherence-based segmentation, ignore user intent, leading to chunks that split answers or contain irrelevant noise. We introduce Intent-Driven Dynamic Chunking (IDC), a novel approach that uses predicted user queries to guide document segmentation. IDC leverages a Large Language Model to generate likely user intents for a document and then employs a dynamic programming algorithm to find the globally optimal chunk boundaries. This represents a novel application of DP to intent-aware segmentation that avoids greedy pitfalls. We evaluated IDC on six diverse question-answering datasets, including news articles, Wikipedia, academic papers, and technical documentation. IDC outperformed traditional chunking strategies on five datasets, improving top-1 retrieval accuracy by 5% to 67%, and matched the best baseline on the sixth. Additionally, IDC produced 40-60% fewer chunks than baseline methods while achieving 93-100% answer coverage. These results demonstrate that aligning document structure with anticipated information needs significantly boosts retrieval performance, particularly for long and heterogeneous documents.

</details>

---
