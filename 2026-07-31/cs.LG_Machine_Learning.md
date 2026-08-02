# cs.LG | Machine Learning | 2026-07-31

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/$β$-OPSD_Deriving_with_Policy_Optimization,_Training_with_Self-Distillation|$β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation]]

![[assets/2607.28582_figure.png|800]]

- **arXiv**: [2607.28582](https://arxiv.org/abs/2607.28582)
- **PDF**: https://arxiv.org/pdf/2607.28582
- **详细分析**: [[20_Research/Papers/强化学习/$β$-OPSD_Deriving_with_Policy_Optimization,_Training_with_Self-Distillation|$β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation]]
- **作者**: Jiawei Xu, Minghui Liu, Juzheng Zhang, Tom Goldstein, Furong Huang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《$β$-OPSD: Deriving with Policy Optimization, Training with Self-Distillation》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy self-distillation (OPSD) is a promising approach to improve reasoning language models, but it remains brittle in practice: making it work reliably often requires substantial engineering effort. We identify a structural source of this difficulty: vanilla OPSD is precisely the $β=1$ member of a broader policy-optimization family, where $β$ weights the KL penalty anchoring the student to a reference policy. This equivalence turns $β$ from an implicit value fixed at one into a controllable regularization parameter, yielding a more general formulation that trades off proximity to a reference policy against privileged teacher guidance. We introduce $β$-OPSD and derive its optimal policy as a geometric interpolation between the reference policy and the privileged teacher. Directly optimizing this objective with reinforcement learning, however, would be costly and high-variance. Rather than optimize the RL objective directly, we turn its closed-form solution into a distillation target. Each value of $β$ selects a target along the reference-to-teacher path, which we implement efficiently by mixing their token-level logits. In this way, inexpensive distillation approximates the solution of expensive policy optimization. Return-to-go credit assignment further aligns token updates with the sequence-level objective while retaining the simplicity of OPSD. Experiments on mathematical reasoning benchmarks show that $β$-OPSD consistently outperforms vanilla OPSD, improving optimization stability and downstream reasoning performance. Our results provide a principled route from self-distillation to policy optimization and back without sacrificing the efficiency that makes OPSD practical.

</details>

---

### [[20_Research/Papers/强化学习/Hierarchical_Multilevel_Monte_Carlo_for_Order-Optimal_Neural_Actor-Critic_in_Average-Reward_CMDPs|Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs]]

![[assets/2607.28390_first_page.png|800]]

- **arXiv**: [2607.28390](https://arxiv.org/abs/2607.28390)
- **PDF**: https://arxiv.org/pdf/2607.28390
- **详细分析**: [[20_Research/Papers/强化学习/Hierarchical_Multilevel_Monte_Carlo_for_Order-Optimal_Neural_Actor-Critic_in_Average-Reward_CMDPs|Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs]]
- **作者**: Ankur Naskar, Vaneet Aggarwal
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Constrained Markov Decision Processes (CMDPs) provide a natural framework for reinforcement learning in safety-critical applications, where agents maximize long-term reward while satisfying long-term constraints. Although primal-dual actor-critic methods with linear critics are well understood, extending order-optimal convergence guarantees to neural critics in average-reward CMDPs has remained open. The main challenge is a fundamental bias-cost trade-off in neural critic estimation: under Neural Tangent Kernel (NTK) analysis, reducing critic bias substantially increases critic optimization cost, preventing order-optimal convergence in the primal-dual framework. We resolve this bottleneck by introducing a hierarchical Multilevel Monte Carlo (MLMC) neural critic that performs debiasing simultaneously across trajectory sampling and critic optimization. The resulting estimator attains the bias of a long critic optimization run with only logarithmic expected sample cost. Building on this estimator, we develop a primal-dual Natural Actor-Critic algorithm that achieves both an optimality gap and a constraint violation of order $\tilde{O}(T^{-1/2})$. This establishes the first order-optimal convergence guarantees for infinite-horizon average-reward CMDPs with general policy parameterization and neural critics, while eliminating the need to know the underlying mixing time. Our results are novel even in the unconstrained setting.

</details>

---

### [[20_Research/Papers/大模型/LEDGERMIND_Provenance-Constrained_Multimodal_Agentic_Reasoning_with_a_Structured_Evidence_Ledger|LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger]]

![[assets/2607.28374_figure.png|800]]

- **arXiv**: [2607.28374](https://arxiv.org/abs/2607.28374)
- **PDF**: https://arxiv.org/pdf/2607.28374
- **详细分析**: [[20_Research/Papers/大模型/LEDGERMIND_Provenance-Constrained_Multimodal_Agentic_Reasoning_with_a_Structured_Evidence_Ledger|LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger]]
- **作者**: Enjun Du, Hange Zhou, Chenxu Du, Siyi Liu, Zirong Chen, Ziyu Zheng, Yongqi Zhang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《LEDGERMIND: Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：TIR-Bench, VTC-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal agents for visual question answering increasingly operate as multi-step trajectories that interleave perception, retrieval, and reasoning, yet evaluation still largely reduces to final-answer accuracy. This aggregate signal cannot tell whether a correct answer was reached through grounded evidence, language priors, or accidental error cancellation. We propose to treat a multimodal agent trajectory as a provenance-constrained state machine: tool outputs are normalized into a Structured Evidence Ledger that serves as the trajectory state, downstream reasoning and decision claims may cite only active ledger entries, grounding is checked at the entity and numeric level, and repair is realized as typed state transitions that cannot introduce content without tool-produced provenance. We instantiate this design as LedgerMind (Provenance-Constrained Multimodal Agentic Reasoning with a Structured Evidence Ledger), augmented by a Three-Layer Grounding Protocol, an Adaptive Dual-Path Dispatcher that matches reasoning depth to question complexity, and an Event-Triggered Verification-and-Repair engine with a formal provenance non-amplification guarantee. We use LedgerMind to target four recurring failure patterns that final-answer accuracy tends to obscure: unsupported intermediate reasoning, citation-backed entity hallucination (Phantom Grounding), over-reasoning on simple queries, and repair-time amplification. Experiments across multiple multimodal reasoning benchmarks and backbone MLLMs show that LedgerMind improves both answer accuracy and trajectory-level faithfulness.

</details>

---

### [[20_Research/Papers/强化学习/Contrastive_Reinforced_Policy_Optimization_via_Privileged_Self-Distillation|Contrastive Reinforced Policy Optimization via Privileged Self-Distillation]]

![[assets/2607.28026_figure.png|800]]

- **arXiv**: [2607.28026](https://arxiv.org/abs/2607.28026)
- **PDF**: https://arxiv.org/pdf/2607.28026
- **详细分析**: [[20_Research/Papers/强化学习/Contrastive_Reinforced_Policy_Optimization_via_Privileged_Self-Distillation|Contrastive Reinforced Policy Optimization via Privileged Self-Distillation]]
- **作者**: Xingjian Wu, Junlin Liu, Xingchen Liu, Xuhang Zhu, Jianing Wang, Linsen Guo, Xiaoyu Li, Xuezhi Cao, Xunliang Cai
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Contrastive Reinforced Policy Optimization via Privileged Self-Distillation》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in post-training Large Language Models (LLMs) increasingly rely on Reinforcement Learning with Verifiable Rewards (RLVR) or On-Policy Self-Distillation (OPSD). While OPSD provides dense, logit-level supervision, it inherently suffers from exposure bias due to the privileged information of the self-teacher. In multi-turn agentic settings, this leads to reasoning route convergence and the loss of clear optimization directions. To tackle these challenges, we introduce Contrastive Reinforced Policy Optimization (CRPO), which reformulates agentic OPSD from a contrastive learning perspective. By leveraging predictive entropy to distinguish between positive positions (reflective exploration) and negative positions (exposure bias), CRPO conducts group-wise contrast to preserve reliable, fine-grained optimization signals. Extensive evaluations across 13 challenging reasoning and deep-search benchmarks demonstrate that CRPO consistently outperforms existing reinforcement learning and self-distillation baselines, significantly enhancing training stability and generalization in long-horizon interactions.

</details>

---

### [[20_Research/Papers/大模型/AutoPref_Automatic_Discovery_of_Task-Specific_Preference_Objectives_for_Neural_Combinatorial_Optimization|AutoPref: Automatic Discovery of Task-Specific Preference Objectives for Neural Combinatorial Optimization]]

![[assets/2607.27953_figure.png|800]]

- **arXiv**: [2607.27953](https://arxiv.org/abs/2607.27953)
- **PDF**: https://arxiv.org/pdf/2607.27953
- **详细分析**: [[20_Research/Papers/大模型/AutoPref_Automatic_Discovery_of_Task-Specific_Preference_Objectives_for_Neural_Combinatorial_Optimization|AutoPref: Automatic Discovery of Task-Specific Preference Objectives for Neural Combinatorial Optimization]]
- **作者**: Shengda Gu, Kai Li, Xinyi Ke, Haobo Fu, Yifan Zhang, Jian Cheng
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《AutoPref: Automatic Discovery of Task-Specific Preference Objectives for Neural Combinatorial Optimization》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Combinatorial optimization problems (COPs) underpin many real-world decisions, but their exponentially large search spaces make high-quality solutions costly to obtain. Neural combinatorial optimization (NCO) learns fast construction policies, typically with reinforcement learning (RL), while preference-based NCO improves sample efficiency by learning from relative solution quality. However, existing preference objectives combine two distinct design choices in manually specified, one-size-fits-all formulations: what learning signal to extract from each solution pair and how to weight each pair relative to the sampled set. We present AutoPref, the first LLM-guided framework for automated preference-objective discovery in NCO. AutoPref factorizes the objective into a pairwise loss program, which defines the learning signal, and a set-aware weighting program, which determines each pair's relative contribution. Their composition forms a unified programmatic objective space containing existing preference objectives as special cases. To make its search tractable, we introduce a staged conditional search strategy with behavioral gates that filter inadmissible programs before short-horizon training and evaluation. Across TSP, CVRP, FFSP, and JSSP, AutoPref consistently outperforms strong hand-designed baselines across problem scales, demonstrating the benefits and scalability of automated objective discovery for NCO.

</details>

---

### [[20_Research/Papers/大模型/Exact_Action_Values_Are_Not_Enough_Rollout-Verified_Reinforcement_Fine-Tuning_of_a_Reasoning_Model_for_Multi-Zone_VAV_Control|Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control]]

![[assets/2607.27914_figure.png|800]]

- **arXiv**: [2607.27914](https://arxiv.org/abs/2607.27914)
- **PDF**: https://arxiv.org/pdf/2607.27914
- **详细分析**: [[20_Research/Papers/大模型/Exact_Action_Values_Are_Not_Enough_Rollout-Verified_Reinforcement_Fine-Tuning_of_a_Reasoning_Model_for_Multi-Zone_VAV_Control|Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control]]
- **作者**: Takumi Shioda, Kohei Terashima, Tatsuo Nagai
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Exact Action Values Are Not Enough: Rollout-Verified Reinforcement Fine-Tuning of a Reasoning Model for Multi-Zone VAV Control》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-zone variable-air-volume control must balance thermal comfort, indoor air quality, and electricity use across several continuous actuators. Model predictive control and reinforcement learning are widely studied, but deployment typically requires building-specific modeling or training, limiting scalability. We first test whether a frontier reasoning model (an LLM trained to use additional inference-time computation) can achieve competitive VAV control from text without building-specific training. With that capability established, we then test whether TD3-guided reinforcement fine-tuning (RFT) can transfer control knowledge into a locally deployable open-weight model. Five controllers are evaluated over three summer days in a physics-based four-zone emulator. Relative to a Guideline 36-based baseline, TD3 reduced HVAC electricity by 4.5% while improving temperature and CO$_2$ compliance. Without building-specific training, GPT-5 achieved the largest reduction (6.2%) but reduced the ventilation margin. For RFT, deterministic rollouts restore a saved state, apply one candidate, and follow TD3 to score each action. Auditing a learned critic against these rollouts exposed a failure hidden by its near-perfect across-time correlation ($r=0.9998$): within-state ranking was unreliable; the critic selected the rollout-best candidate in only 5 of 10 states. Even with the rollout verifier, 200 RFT steps produced no sustained improvement in sampled-action return; the open-weight controller used more electricity than the baseline before and after training, and its five-minute predictions remained worse than persistence. GPT-5 predicted transitions far better. Exact rollout scores rank sampled actions but reveal neither next-state effects nor an improvement direction. The unchanged transition errors motivate transition-focused supervised fine-tuning before value-based RFT.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_the_Best_Teacher_Expanding_and_Compressing_the_Reasoning_Solution_Manifold|Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold]]

![[assets/2607.27770_figure.png|800]]

- **arXiv**: [2607.27770](https://arxiv.org/abs/2607.27770)
- **PDF**: https://arxiv.org/pdf/2607.27770
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_the_Best_Teacher_Expanding_and_Compressing_the_Reasoning_Solution_Manifold|Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold]]
- **作者**: Songshuo Lu, Zhi Chen, Yaohua Tang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Beyond the Best Teacher: Expanding and Compressing the Reasoning Solution Manifold》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A single reinforcement-learning run can produce a strong reasoner yet an incomplete teacher: it often amplifies only a subset of the valid solution modes. We argue that reinforcement learning (RL)-trained policies should therefore be viewed as local probes of a multi-basin reasoning solution manifold, rather than as globally reliable supervisors. Based on this view, we propose an expand-then-compress framework that couples teacher construction with multi-teacher policy distillation. In the expansion stage, Residual Group Relative Policy Optimization (RGRPO) trains a sequence of teachers from a common initialization and redirects each later round toward examples not yet covered by the accumulated teacher union. In the compression stage, reliability-gated Teacher-Union On-policy Distillation (TU-OPD) lets the student learn from its own response prefixes. For each example, only reliable teachers contribute, and their sampled-token OPD losses are weighted by their per-example quality. We further introduce Consensus-Residual Decomposition, which preserves a winner teacher's excess token preferences over its reliable peers, preventing specialist behavior from being suppressed during teacher aggregation. Experiments on mathematical reasoning, code generation, and instruction following show that the resulting Qwen3-1.7B student consistently outperforms the strongest individual teacher across all three domains, yielding relative improvements of 2.0%, 8.3%, and 6.9%, respectively, while retaining single-model inference. These results establish a simple but powerful principle: stronger students can be obtained not by selecting a single better teacher, but by deliberately constructing and compressing a complementary teacher union.

</details>

---

### [[20_Research/Papers/大模型/LightRot_A_Light-Weighted_Rotation_Scheme_and_Architecture_for_Accurate_Low-Bit_Large_Language_Model_Inference|LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference]]

![[assets/2607.27704_figure.png|800]]

- **arXiv**: [2607.27704](https://arxiv.org/abs/2607.27704)
- **PDF**: https://arxiv.org/pdf/2607.27704
- **详细分析**: [[20_Research/Papers/大模型/LightRot_A_Light-Weighted_Rotation_Scheme_and_Architecture_for_Accurate_Low-Bit_Large_Language_Model_Inference|LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference]]
- **作者**: Sangjin Kim, Yuseon Choi, Jungjun Oh, Byeongcheol Kim, Hoi-Jun Yoo
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《LightRot: A Light-Weighted Rotation Scheme and Architecture for Accurate Low-Bit Large Language Model Inference》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language models (LLMs) continue to demonstrate exceptional capabilities across various domains, the challenge of achieving energy-efficient and accurate inference becomes increasingly critical. This work presents LightRot, a lightweight rotation scheme and dedicated hardware accelerator designed for low-bit LLM inference. The proposed architecture integrates Grouped Local Rotation (GLR) and Outlier Direction Aligning (ODA) algorithms with a hierarchical Fast Hadamard Transform (FHT)-based rotation unit to address key challenges in low-bit quantization, including the energy overhead of rotation operations. The proposed accelerator, implemented in a 28nm CMOS process, achieves a peak energy efficiency of 27.4 TOPS/W for 4-bit inference, surpassing prior state-of-the-art designs. Unlike conventional approaches that rely on higher-precision inference or evaluate on basic language modeling tasks like GPT-2, LightRot is optimized for advanced models such as LLaMA2-13B and LLaMA3-8B. Its performance is further validated on MT-Bench, demonstrating robust applicability to real-world conversational scenarios and redefining benchmarks for chat-based AI systems. By synergizing algorithmic innovations and hardware efficiency, this work sets a new paradigm for scalable, low-bit LLM inference, paving the way for sustainable AI advancements.

</details>

---

### [[20_Research/Papers/强化学习/Real-Time_Hard_Peak_Age-of-Information_Safety_with_No-Regret_Learning|Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning]]

![[assets/2607.27626_figure.png|800]]

- **arXiv**: [2607.27626](https://arxiv.org/abs/2607.27626)
- **PDF**: https://arxiv.org/pdf/2607.27626
- **详细分析**: [[20_Research/Papers/强化学习/Real-Time_Hard_Peak_Age-of-Information_Safety_with_No-Regret_Learning|Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning]]
- **作者**: Wentao Zhang, Wentao Mo
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Real-Time Hard Peak Age-of-Information Safety with No-Regret Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety-critical IoT systems such as industrial closed-loop control, V2X coordination, and remote teleoperation require every sensor's peak Age of Information (peak AoI, also abbreviated PAoI) to stay below a hard per-slot deadline, not merely an average bound. Existing approaches meet this requirement only under restrictive assumptions: stochastic channels for Whittle-index AoI, simulator rollouts for deep reinforcement learning, or sublinear cumulative violation for long-term constrained online convex optimization. Under adversarial coefficients, OCO-PAoI-Hard guarantees zero per-slot violation of the modeled AoI state under one-step viability and O(sqrt(T)) regret against any static safe comparator; packet-level safety requires stronger service assumptions. Our key observation is that the fractional peak-AoI deadline collapses exactly to an affine half-space constraint on the resource-allocation vector, turning hard real-time scheduling into time-varying constrained online convex optimization over a polyhedral safe set. A strictly causal proposal-shield-update loop enforces feasibility through one Euclidean projection per slot, the gradient step preserves no-regret behavior, and the classical virtual queue is reduced to an a-posteriori certificate. We establish closed-form static and dynamic regret bounds, a matching Omega(sqrt(T)) minimax lower bound, a margin-safe variant against execution noise, and a deadline-induced competitive ratio. On a four-sensor adversarial fluid-model trap channel, OCO-PAoI-Hard attains zero modeled-state deadline violations across all ten seeds, while four representative baselines miss between 1.65 percent and 64.0 percent of slots, and the empirical normalized regret stays below the theoretical envelope across two orders of magnitude in T.

</details>

---

### [[20_Research/Papers/强化学习/Policy_Gradient_Steering_Interventions_from_Behavioral_Objectives|Policy Gradient Steering: Interventions from Behavioral Objectives]]

![[assets/2607.27574_figure.png|800]]

- **arXiv**: [2607.27574](https://arxiv.org/abs/2607.27574)
- **PDF**: https://arxiv.org/pdf/2607.27574
- **详细分析**: [[20_Research/Papers/强化学习/Policy_Gradient_Steering_Interventions_from_Behavioral_Objectives|Policy Gradient Steering: Interventions from Behavioral Objectives]]
- **作者**: Yoann Poupart, Aurélie Beynier, Nicolas Maudet
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Policy Gradient Steering: Interventions from Behavioral Objectives》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Activation steering has emerged in large language models as a lightweight alternative for dynamically changing a model's behavior at inference time. However, we show that existing steering methods fail to steer even a simple policy in a two-route gridworld environment. To address this limitation, we propose Policy Gradient Steering (PGS), which formulates steering as a reinforcement learning problem. PGS accumulates gradients of a temporary behavioral objective over a small set of rollouts or demonstrations to construct a removable task vector. We first demonstrate the calibration and reversibility of PGS in a two-route gridworld environment. Using chess puzzles, we then evaluate independently fitted PGS vectors both in isolation and in combination, finding that compatible tactical objectives accumulate constructively. Finally, in competitive football, we show that PGS can alter specific team behaviors and that its effects transfer across opponents. Together, these results show that policy gradients provide a natural interface for constructing temporary and composable behavioral adaptations across diverse decision-making domains.

</details>

---

### [[20_Research/Papers/强化学习/RLPF_Reinforcement_Learning_from_Performance_Feedback_for_Code_Generation|RLPF: Reinforcement Learning from Performance Feedback for Code Generation]]

![[assets/2607.27271_figure.png|800]]

- **arXiv**: [2607.27271](https://arxiv.org/abs/2607.27271)
- **PDF**: https://arxiv.org/pdf/2607.27271
- **详细分析**: [[20_Research/Papers/强化学习/RLPF_Reinforcement_Learning_from_Performance_Feedback_for_Code_Generation|RLPF: Reinforcement Learning from Performance Feedback for Code Generation]]
- **作者**: Huihao Jing, Haozhe Cui, Wenbin Hu, Shaojin Chen, Haochen Shi, Changxuan Fan, Yuxuan Liu, Hanyu Yang, Sirui Zhang, Ziyi Chen, Haoran Li, Yangqiu Song
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《RLPF: Reinforcement Learning from Performance Feedback for Code Generation》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CodeRL, DevBench, EffiBench, HumanEval, LiveCodeBench, PerfCodeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code models are increasingly trained with execution feedback, but most training signals still stop at correctness. This leaves an important gap for systems code: two programs can pass the same tests while differing greatly in runtime. We study how to train code agents to prefer faster correct implementations, rather than treating efficiency only as an evaluation metric. The key difficulty is that runtime is a fragile reward. It is meaningful only after a program is correct, varies across tasks, and gives little guidance when most sampled programs fail to compile or run. We propose \textbf{RLPF}, reinforcement learning from performance feedback, which turns execution outcomes into a staged reward. Failed programs are ordered by execution progress, while correct programs are ranked by their relative improvement from the baseline toward the expert reference. This gives useful feedback before correctness and performance-sensitive feedback after correctness. Fine-tuning Qwen3-32B with RLPF on PerfCodeBench raises correct-and-runnable solutions from $11.1\%$ to $54.6\%$ and improves relative efficiency from $8.1\%$ to $38.6\%$. The trained model becomes competitive with stronger open-weight systems, and its optimization behavior transfers modestly to EffiBench-X. Additional studies show that model-generated references provide useful but weaker supervision, and that the full composite reward is more reliable than correctness-only or runtime-only baselines. These results suggest that code agents can be trained not only to pass tests, but also to optimize the programs they write.

</details>

---
