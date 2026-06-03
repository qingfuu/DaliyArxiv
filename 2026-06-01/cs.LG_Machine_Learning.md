# cs.LG | Machine Learning | 2026-06-01

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/具身智能/Constrained_Multi-Objective_Reinforcement_Learning_with_Max-Min_Criterion|Constrained Multi-Objective Reinforcement Learning with Max-Min Criterion]]

![[assets/2605.31388_first_page.png|800]]

- **arXiv**: [2605.31388](https://arxiv.org/abs/2605.31388)
- **PDF**: https://arxiv.org/pdf/2605.31388
- **详细分析**: [[20_Research/Papers/具身智能/Constrained_Multi-Objective_Reinforcement_Learning_with_Max-Min_Criterion|Constrained Multi-Objective Reinforcement Learning with Max-Min Criterion]]
- **作者**: Giseung Park, Hyunyoung Nam, Woohyeon Byeon, Amir Leshem, Youngchul Sung
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Constrained Multi-Objective Reinforcement Learning with Max-Min Criterion》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Objective Reinforcement Learning (MORL) extends standard RL by optimizing policies with respect to multiple, often conflicting, objectives. While max-min MORL has emerged as an effective approach for promoting fairness, its applicability remains limited, particularly when constraints must be incorporated. In this paper, we propose a MORL framework that integrates the max-min criterion with explicit constraint satisfaction. We establish a theoretical foundation for the proposed framework and validate the resulting algorithm through convergence analysis and experiments in tabular settings. We further demonstrate the practical relevance of our approach in simulated building thermal control, multi-objective locomotion control, and greenhouse-gas-emission-aware traffic management. Across these domains, our method effectively balances fairness and constraint satisfaction in multi-objective decision-making.

</details>

---

### [[20_Research/Papers/强化学习/Generalized_Intention_Modeling_in_Multi-Agent_Reinforcement_Learning|Generalized Intention Modeling in Multi-Agent Reinforcement Learning]]

![[assets/2605.31318_figure.png|800]]

- **arXiv**: [2605.31318](https://arxiv.org/abs/2605.31318)
- **PDF**: https://arxiv.org/pdf/2605.31318
- **详细分析**: [[20_Research/Papers/强化学习/Generalized_Intention_Modeling_in_Multi-Agent_Reinforcement_Learning|Generalized Intention Modeling in Multi-Agent Reinforcement Learning]]
- **作者**: Mateusz Odrowaz-Sypniewski, Jasmine Bayrooti, Ajay Shankar, Amanda Prorok
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Generalized Intention Modeling in Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modeling an opponent's intent is critical for effective decision-making in non-cooperative, competitive, and general-sum multi-agent reinforcement learning. Existing opponent modeling methods encode intent using an embedding derived from episode information chosen a priori, such as the opponent's next action or a future environment state, and use this to guide the ego-agent's behavior. These approaches assume that the chosen information is universally representative of intent; however, we show empirically that this is not the case as intentions are often task- and environment-dependent. To address this, we introduce a task-adaptive opponent modeling framework that learns a performance-driven mixture of multiple intent representations. We further introduce a new intention representation that maximizes mutual information with the ego-agent's future returns, thereby capturing opponent information that is most directly relevant to performance. Our approach consistently matches or exceeds the performance of state-of-the-art baselines across diverse tasks and yields insights into when and why different opponent modeling strategies succeed.

</details>

---

### [[20_Research/Papers/具身智能/Survival_Reinforcement_Learning_Toward_Scalable_Self-Supervised_RL|Survival Reinforcement Learning: Toward Scalable Self-Supervised RL]]

![[assets/2605.31273_figure.png|800]]

- **arXiv**: [2605.31273](https://arxiv.org/abs/2605.31273)
- **PDF**: https://arxiv.org/pdf/2605.31273
- **详细分析**: [[20_Research/Papers/具身智能/Survival_Reinforcement_Learning_Toward_Scalable_Self-Supervised_RL|Survival Reinforcement Learning: Toward Scalable Self-Supervised RL]]
- **作者**: Franki Nguimatsia-Tiofack, Fabian Schramm, Théotime Le Hellard, Justin Carpentier
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 1.72（加权：具身智能 0.3，大模型 0.1，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Survival Reinforcement Learning: Toward Scalable Self-Supervised RL》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CRL, GCRL, JaxGCRL, SRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While self-supervised Contrastive Reinforcement Learning (CRL) has shown remarkable depth-scaling capabilities, successfully using networks over 64 layers, scaled CRL still struggles with long-horizon goal-conditioned planning due to the uniformity-tolerance dilemma inherent in contrastive losses. We introduce Survival Reinforcement Learning (SRL), an online classification-based alternative that extends the survival value learning framework by maximizing the agent's dwell time at target goals. SRL bypasses the structural constraints of CRL and mitigates the "bang-bang" control solutions inherent to survival frameworks, which often induce undesirable behavior in complex dynamical systems. Evaluated across diverse robotic benchmarks, scaled SRL matches state-of-the-art CRL on manipulation tasks and outperforms it by 2x to 8x on stable, long-horizon locomotion tasks. Our results provide strong additional evidence that classification-based methods may serve as a key primitive in the broader effort to scale reinforcement learning.

</details>

---

### [[20_Research/Papers/强化学习/Multivariate_Distributional_Reinforcement_Learning_Using_Sliced_Divergences|Multivariate Distributional Reinforcement Learning Using Sliced Divergences]]

![[assets/2605.31222_figure.png|800]]

- **arXiv**: [2605.31222](https://arxiv.org/abs/2605.31222)
- **PDF**: https://arxiv.org/pdf/2605.31222
- **详细分析**: [[20_Research/Papers/强化学习/Multivariate_Distributional_Reinforcement_Learning_Using_Sliced_Divergences|Multivariate Distributional Reinforcement Learning Using Sliced Divergences]]
- **作者**: Baptiste Debes, Tinne Tuytelaars
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Multivariate Distributional Reinforcement Learning Using Sliced Divergences》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL, MSDRL, SDRL, SlicedDistributionalRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distributional reinforcement learning (DRL) models the full return distribution rather than expectations, but extending it to multivariate settings remains challenging. Many common metrics do not naturally generalize beyond one dimension or lose computational tractability, and the multivariate case introduces additional difficulties such as general matrix discounting, for which no contraction results are available. We introduce Sliced Distributional Reinforcement Learning (SDRL), which lifts tractable one-dimensional divergences to multivariate return distributions via projections. We prove Bellman contraction for uniform slicing under shared scalar discounting, and introduce a maximum-slicing variant with contraction under general dense discount matrices. SDRL supports a broad class of base divergences; we analyze Wasserstein, Cramér, and Maximum Mean Discrepancy (MMD), and characterize which SDRL variants suit the standard single-sample Bellman update used in distributional RL. We evaluate SDRL on a toy chain problem and a gridworld image-based environment as well as a subset of Atari games.

</details>

---

### [[20_Research/Papers/强化学习/Convergence_of_Two-Timescale_Markovian_Stochastic_Approximations_with_Applications_in_Reinforcement_Learning|Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning]]

![[assets/2605.31172_first_page.png|800]]

- **arXiv**: [2605.31172](https://arxiv.org/abs/2605.31172)
- **PDF**: https://arxiv.org/pdf/2605.31172
- **详细分析**: [[20_Research/Papers/强化学习/Convergence_of_Two-Timescale_Markovian_Stochastic_Approximations_with_Applications_in_Reinforcement_Learning|Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning]]
- **作者**: Vagul Mahadevan, Claire Chen, Shuze Daniel Liu, Shangtong Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Convergence of Two-Timescale Markovian Stochastic Approximations with Applications in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work studies the convergence of two-timescale stochastic approximations (SA), a class of iterative algorithms that update two sets of parameters in fast and slow timescales respectively. Notable examples of two-timescale SA in reinforcement learning (RL) include temporal difference learning with gradient correction (TDC) and actor-critic methods. Previously, the stability (i.e., boundedness) and convergence of two-timescale SA were only established under i.i.d. noise. This work instead establishes the stability and convergence of two-timescale SA under Markovian noise, a setup that is more realistic in RL. Notably, we do not need to use any projection operator and the noise does not need to live in a compact space. Our key technical novelty is to control the fast timescale parameter with the running max of the slow timescale parameter, instead of with the current slow timescale parameter, as most prior works do. As a key application, we establish the first almost sure convergence of TDC with eligibility traces under off-policy learning with linear function approximation.

</details>

---

### [[20_Research/Papers/具身智能/Don't_Fool_Me_Twice_Adapting_to_Adversity_in_the_Wild_with_Experience-Driven_Reasoning|Don't Fool Me Twice: Adapting to Adversity in the Wild with Experience-Driven Reasoning]]

![[assets/2605.31119_figure.png|800]]

- **arXiv**: [2605.31119](https://arxiv.org/abs/2605.31119)
- **PDF**: https://arxiv.org/pdf/2605.31119
- **详细分析**: [[20_Research/Papers/具身智能/Don't_Fool_Me_Twice_Adapting_to_Adversity_in_the_Wild_with_Experience-Driven_Reasoning|Don't Fool Me Twice: Adapting to Adversity in the Wild with Experience-Driven Reasoning]]
- **作者**: Navin Sriram Ravie, Andrew Jong, Krrish Jain, John Liu, Omar Alama, Bijo Sebastian, Sebastian Scherer
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Don't Fool Me Twice: Adapting to Adversity in the Wild with Experience-Driven Reasoning》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotics, dangers and adversity modes are often embodiment-specific and relative to each agent. A frontier of autonomous mobile robotics is to enable agents to operate effectively in the wild in unseen unstructured environments. A significant challenge in unseen unstructured environments is that it may not be possible to predict all the dangers to the specific robot. Although recent work has used large foundation vision-language models (VLMs) to preemptively predict an exhaustive list of common-sense dangers, it remains difficult to capture possible interaction and embodiment-dependent adversities. We propose a continual learning framework for a mobile embodied agent to learn online from disturbances and attribute anomalous behaviours to causes through semantics, enabling better prediction and planning of the world in the future. Our framework, "Don't Fool Me Twice", first observes disturbances and describes their effects on the robot; this description is augmented with visual context to query a VLM to predict possible causes; the local disturbance is characterized using kernel regression, which allows for efficient, few-shot modeling of transient anomalies. We leverage semantic voxel-centric modeling to estimate epistemic uncertainty, enabling richer downstream recovery by treating interaction-driven disturbances as learnable spatial behaviors. We present four hypotheses and validate them in simulation and on hardware across embodiments and adversity modes.

</details>

---

### [[20_Research/Papers/世界模型/Subspace-Decomposed_JEPAs_Disentangling_Progression_and_Content_in_Latent_World_Models|Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models]]

![[assets/2605.31111_figure.png|800]]

- **arXiv**: [2605.31111](https://arxiv.org/abs/2605.31111)
- **PDF**: https://arxiv.org/pdf/2605.31111
- **详细分析**: [[20_Research/Papers/世界模型/Subspace-Decomposed_JEPAs_Disentangling_Progression_and_Content_in_Latent_World_Models|Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models]]
- **作者**: Lucas Thil, Jesse Read, Rim Kaddah, Guillaume Doquet
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent

#### 研究背景与动机

《Subspace-Decomposed JEPAs: Disentangling Progression and Content in Latent World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-Embedding Predictive Architectures (JEPAs) learn compact latent world models by predicting future embeddings, but no single coordinate of the latent is designated to encode task progression. We carve the JEPA latent into two orthogonal subspaces with disjoint roles: a low-dimensional progression subspace shaped by a cosine-margin triplet loss, and a high-dimensional content subspace regularised by the existing SIGReg objective of LeWM. We prove that the two anti-collapse forces act on disjoint coordinates, so they compose additively rather than competing on the same dimensions. Our method, SD-JEPA improves over the LeWM baseline on the majority of its control benchmarks at matched compute, and outperforms the strongest non-LeWM JEPA baseline on Push-T; a subspace-ablation falsifier confirms the split is the load-bearing ingredient. Beyond planning, the resulting 1-D angular progression coordinate functions as a scene-aware compass on the latent. It advances with task progress, regresses when the agent backtracks, and under controlled perturbations both spikes and relocalises to a semantically appropriate new task-phase sector, separating the moment of surprise from its meaning in a way that prediction-error scalars cannot. Three quantitative tests back this up: $|Δθ_t|$ outperforms the standard latent-prediction-error surprise at localising semantic events on 40 held-out cube episodes by up to +0.18 pooled AUROC (97.5% per-episode win rate at $\pm 1$-step tolerance); a within-episode linear probe across all four environments (40 episodes per env) shows the 8-dimensional progression subspace (4.2% of the latent) explains 72-95% of task-progress variance..

</details>

---

### [[20_Research/Papers/强化学习/The_Challenges_of_Using_Reinforcement_Learning_for_Controlling_Industrial_Energy_Systems|The Challenges of Using Reinforcement Learning for Controlling Industrial Energy Systems]]

![[assets/2605.31044_figure.png|800]]

- **arXiv**: [2605.31044](https://arxiv.org/abs/2605.31044)
- **PDF**: https://arxiv.org/pdf/2605.31044
- **详细分析**: [[20_Research/Papers/强化学习/The_Challenges_of_Using_Reinforcement_Learning_for_Controlling_Industrial_Energy_Systems|The Challenges of Using Reinforcement Learning for Controlling Industrial Energy Systems]]
- **作者**: Tobias Lademann, Théo Vincent, Jan Peters, Matthias Weigold
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《The Challenges of Using Reinforcement Learning for Controlling Industrial Energy Systems》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has shown promising results for optimizing the control of industrial energy systems, yet most existing studies remain limited to the application in simulation environments. We investigate the challenges of deploying reinforcement learning in a real-world industrial energy system, considering a thermal heating network as a use case. We formulate the task as a Markov Decision Process and systematically analyze the associated challenges along the structure of the formal description, including partial observability, action space design, reward design, and the simulation-to-reality gap. The challenges are grounded in an existing real-world deployment, where reinforcement learning achieves operational stability but shows a significant performance gap compared to simulation.

</details>

---

### [[20_Research/Papers/强化学习/SDM-Q_Cost-Aware_Staged_Decision-Making_for_Multi-Omics_Classification_with_Deep_Q-Learning|SDM-Q: Cost-Aware Staged Decision-Making for Multi-Omics Classification with Deep Q-Learning]]

![[assets/2605.31014_figure.png|800]]

- **arXiv**: [2605.31014](https://arxiv.org/abs/2605.31014)
- **PDF**: https://arxiv.org/pdf/2605.31014
- **详细分析**: [[20_Research/Papers/强化学习/SDM-Q_Cost-Aware_Staged_Decision-Making_for_Multi-Omics_Classification_with_Deep_Q-Learning|SDM-Q: Cost-Aware Staged Decision-Making for Multi-Omics Classification with Deep Q-Learning]]
- **作者**: Nan Mu, Xiaoyang Fan, Chen Zhao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《SDM-Q: Cost-Aware Staged Decision-Making for Multi-Omics Classification with Deep Q-Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BranchyNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-omics data provide complementary molecular characterizations of disease phenotypes and play an important role in disease diagnosis and subtype classification in precision medicine. However, acquiring complete multi-omics profiles is expensive and time-consuming, while most existing deep learning methods assume full modality availability during inference, resulting in substantial redundancy and limited practicality in clinical settings. To address this issue, we propose SDM-Q, a reinforcement learning framework for adaptive and cost-aware multi-omics classification. Specifically, multi-omics diagnosis is reformulated as a finite-horizon sequential decision problem, where the currently acquired omics modalities define the diagnostic state at each stage. An action--value function determines whether to acquire an additional modality or terminate the decision process and output the final prediction. To balance diagnostic utility and acquisition cost, the reward is defined only at the terminal stage and jointly determined by classification correctness and cumulative modality acquisition cost. A backward stage-wise optimization strategy is introduced to improve policy consistency and training stability. Experiments on four public multi-omics datasets, including ROSMAP, LGG, BRCA, and KIPAN, demonstrate that SDM-Q effectively reduces redundant modality acquisition while maintaining competitive classification performance compared with methods using complete multi-omics inputs. In the BRCA and KIPAN datasets, more than 99\% and 95\% of subjects, respectively, achieve accurate classification using only a single omics modality, while the average number of acquired modalities remains below two for ROSMAP and LGG. These results suggest that cost-aware sequential decision-making provides an effective paradigm for improving the efficiency of precision medicine workflows.

</details>

---

### [[20_Research/Papers/强化学习/Revisiting_Zeroth-Order_Hessian_Approximation_A_Single-Step_Policy_Optimization_Lens|Revisiting Zeroth-Order Hessian Approximation: A Single-Step Policy Optimization Lens]]

![[assets/2605.30960_figure.png|800]]

- **arXiv**: [2605.30960](https://arxiv.org/abs/2605.30960)
- **PDF**: https://arxiv.org/pdf/2605.30960
- **详细分析**: [[20_Research/Papers/强化学习/Revisiting_Zeroth-Order_Hessian_Approximation_A_Single-Step_Policy_Optimization_Lens|Revisiting Zeroth-Order Hessian Approximation: A Single-Step Policy Optimization Lens]]
- **作者**: Junbin Qiu, Zhaowei Hong, Renzhe Xu, Yao Shu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Revisiting Zeroth-Order Hessian Approximation: A Single-Step Policy Optimization Lens》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate Zeroth-Order (ZO) Hessian estimation is a cornerstone of derivative-free methods, essential for tasks such as bilevel optimization, Bayesian inference, and uncertainty quantification. However, obtaining a complete suite of low-variance estimators for the Hessian and its inverse in high-dimensional settings remains a significant challenge. To address this, we propose a unified framework that reinterprets ZO Hessian approximation through the lens of single-step Policy Optimization (PO). This perspective establishes a theoretical equivalence between general ZO Hessian estimators and the Hessian of a smoothed PO objective, unifying distinct classical randomized estimators as specific instances of baseline selection. Building on this foundation, we introduce ZoVH, a comprehensive suite of variance-reduced estimators for the full Hessian matrix, its regularized inverse, and the bias-corrected inverse Hessian-gradient product. ZoVH leverages two key techniques: (1) a unique optimal baseline derived to provably minimize variance, and (2) a query reuse strategy that incorporates historical function queries to enhance sample efficiency without inflating costs. Our rigorous theoretical analysis confirms the unbiasedness of the Hessian estimator, validates the variance optimality of our baseline, provides error bounds for the entire ZoVH suite, and establishes convergence guarantees for the resulting curvature-aware ZO algorithm. Extensive empirical results validate our theoretical findings, demonstrating that ZoVH achieves superior estimation accuracy and convergence performance in real-world applications. Code is available at https://github.com/Qjbtiger/ZoVH

</details>

---

### [[20_Research/Papers/大模型/Automating_Formal_Verification_with_Reinforcement_Learning_and_Recursive_Inference|Automating Formal Verification with Reinforcement Learning and Recursive Inference]]

![[assets/2605.30914_figure.png|800]]

- **arXiv**: [2605.30914](https://arxiv.org/abs/2605.30914)
- **PDF**: https://arxiv.org/pdf/2605.30914
- **详细分析**: [[20_Research/Papers/大模型/Automating_Formal_Verification_with_Reinforcement_Learning_and_Recursive_Inference|Automating Formal Verification with Reinforcement Learning and Recursive Inference]]
- **作者**: Max Tan
- **cs 子类**: cs.LG, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Automating Formal Verification with Reinforcement Learning and Recursive Inference》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Dalek-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated formal verification remains challenging for large language models because data for proof assistants and verification-aware languages is scarce, and correctness depends on satisfying precise machine-checkable specifications rather than producing plausible code. This thesis studies how verifier environments can improve LLM generation of verified programs and proofs through reinforcement learning from verifiable rewards (RLVR) and verifier-guided inference-time search. First, we train open-source models in Dafny with RLVR using Group Relative Policy Optimization (GRPO) and related variants, assembling generated candidates into complete programs and scoring them with compiler and verifier outcomes. Initial experiments on an APPS-derived Dafny dataset increased verified reward from 2.2% to 58.1%, but revealed specification hacking, where models exploit weak formal specifications instead of implementing the intended solutions. After filtering underspecified and vulnerable tasks, multi-turn RLVR on the refined benchmark improves the verified pass rate from 9.7% to 31.1%. Second, we develop a verifier-guided inference scaffold in Lean that treats proof generation as structured search over decomposed subgoals, verifier feedback, diagnostics, and repair. With a fixed base model, the full scaffold with proof reviser improves pass rate on an initial VeriCoding pilot set from 46.2% under direct repair to 69.2%. On the larger VERINA dataset, whole-task decomposition plus proof reviser solves 7 of 42 previously unsolved tasks. We also introduce Dalek-Bench, a repository-scale Lean benchmark derived from the Rust $\texttt{curve25519-dalek}$ verification project; preliminary results remain weak, indicating that stronger progress evaluation and task-specific tool-use policies are still needed.

</details>

---

### [[20_Research/Papers/强化学习/Zero_Collapse_A_Failure_Mode_of_Policy_Gradient_Methods_in_Discontinuous_Reward_Environments|Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments]]

![[assets/2605.30896_figure.png|800]]

- **arXiv**: [2605.30896](https://arxiv.org/abs/2605.30896)
- **PDF**: https://arxiv.org/pdf/2605.30896
- **详细分析**: [[20_Research/Papers/强化学习/Zero_Collapse_A_Failure_Mode_of_Policy_Gradient_Methods_in_Discontinuous_Reward_Environments|Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments]]
- **作者**: Nishant Kumar, Enrique Areyan Viqueira, Amy Greenwald
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Zero Collapse: A Failure Mode of Policy Gradient Methods in Discontinuous Reward Environments》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bidding in repeated auctions is a central challenge for reinforcement learning (RL), combining continuous control with the strategic complexities of digital advertising. While policy gradient and value-based methods seem well-suited for these settings, they often struggle with the discontinuous, "cliff-like" nature of auction reward landscapes. In a first-price auction, for example, a bidder receives zero reward until they cross a specific threshold, after which the reward decreases as the bid increases. This creates a landscape of flat, zero-reward regions separated by sharp boundaries. We identify a fundamental failure mode in this setting termed "zero collapse." We show that stochastic exploration and gradient-based updates can cause policies to overshoot optimal high-reward regions and enter flat, zero-reward regimes. Once there, the lack of an informative gradient signal makes recovery extremely sample-inefficient, effectively trapping the agent. We find that actor-critic methods are particularly susceptible, as biased value estimates can accelerate this movement toward unstable regions. Our contributions include: (1) a mechanistic explanation of how discontinuous rewards lead to vanishing signals and zero collapse; (2) an analysis of the interaction between policy stochasticity and step size; and (3) an empirical demonstration of this phenomenon across REINFORCE and actor-critic variants. We propose practical mitigation strategies involving initialization and architectural choices to improve stability. Finally, we introduce a formal RL framework for auction environments highlighting their unique structural properties.

</details>

---

### [[20_Research/Papers/强化学习/A_Lecture_Note_on_Offline_RL_and_IRL,_Part_II_Foundations_of_Inverse_Reinforcement_Learning_and_Dynamic_Discrete_Choice_Models|A Lecture Note on Offline RL and IRL, Part II: Foundations of Inverse Reinforcement Learning and Dynamic Discrete Choice Models]]

![[assets/2605.30843_first_page.png|800]]

- **arXiv**: [2605.30843](https://arxiv.org/abs/2605.30843)
- **PDF**: https://arxiv.org/pdf/2605.30843
- **详细分析**: [[20_Research/Papers/强化学习/A_Lecture_Note_on_Offline_RL_and_IRL,_Part_II_Foundations_of_Inverse_Reinforcement_Learning_and_Dynamic_Discrete_Choice_Models|A Lecture Note on Offline RL and IRL, Part II: Foundations of Inverse Reinforcement Learning and Dynamic Discrete Choice Models]]
- **作者**: Enoch Hyunwook Kang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL, Security

#### 研究背景与动机

《A Lecture Note on Offline RL and IRL, Part II: Foundations of Inverse Reinforcement Learning and Dynamic Discrete Choice Models》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AIRL, Adversarial-IRL, IRL, ML-IRL, MaxEnt-IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the forward reinforcement-learning problem, the reward is fixed and known; the learner is asked to find a good policy or value function. Here we turn the question around. Given offline data generated by an expert, can we recover the reward the expert was optimizing? This is the inverse reinforcement learning problem, and remarkably, two communities, structural econometricians studying dynamic discrete choice (DDC) and machine learners studying entropy-regularized IRL, have been working on exactly the same probabilistic model under different names. We begin by proving their equivalence. We then develop the classical identification result of Magnac and Thesmar and the classical computational paradigms that grew out of it: Rust's nested fixed-point algorithm, the conditional-choice-probability approach of Hotz and Miller, and the two temporal-difference approaches of Adusumilli and Eckardt: linear semi-gradient TD and approximate value iteration. Each route has its limits: dimensionality, transition-kernel estimation, the deadly triad, or projected fixed-point bias. We then walk through the modern ML/IRL strand: adversarial IRL, occupancy matching, IQ-Learn, and offline ML-IRL, deriving each method's actual objective and stating precisely what it does and does not identify. We close with the empirical-risk-minimization framework of Kang et al., which yields a gradient-based estimator for offline IRL/DDC.

</details>

---

### [[20_Research/Papers/强化学习/Efficient_and_Uncertainty-Aware_Diffusion_Framework_for_Offline-to-Online_Reinforcement_Learning|Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning]]

![[assets/2605.30776_figure.png|800]]

- **arXiv**: [2605.30776](https://arxiv.org/abs/2605.30776)
- **PDF**: https://arxiv.org/pdf/2605.30776
- **详细分析**: [[20_Research/Papers/强化学习/Efficient_and_Uncertainty-Aware_Diffusion_Framework_for_Offline-to-Online_Reinforcement_Learning|Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning]]
- **作者**: Ha Manh Bui, Metod Jazbec, Eric Nalisnick, Anqi Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.36）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《Efficient and Uncertainty-Aware Diffusion Framework for Offline-to-Online Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：O2O-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline-to-Online Reinforcement Learning (O2O-RL) leverages an offline, pre-trained policy to minimize costly online interactions. Although data-efficient, O2O-RL is susceptible to shifts between offline and online distributions. Existing work aims to mitigate the harm of this shift by finetuning the policy on trajectory data sampled from a diffusion model. Inspired by this line of work, we propose DUAL: an efficient \textbf{D}iffusion \textbf{U}ncertainty-\textbf{A}ware framework for offline-to-online reinforcement \textbf{L}earning. DUAL utilizes the prior knowledge of the diffusion model to distill a fast-sampling diffusion actor policy and transition model in the offline phase. DUAL also employs a Laplace approximation and distance transition-state-shift detection, thereby using uncertainty quantification to improve exploration versus exploitation in the online phase. We formally show that our actor loss with the Laplace approximation provides a proxy for a principled estimate of epistemic uncertainty. Empirically, DUAL improves the online expected return over O2O-RL baselines across multiple settings and environments.

</details>

---

### [[20_Research/Papers/具身智能/BOKBO_(Best_of_K_Bad_Options)_Calibrated_Abstention_for_VLA_Policies|BOKBO (Best of K Bad Options): Calibrated Abstention for VLA Policies]]

![[assets/2605.30660_first_page.png|800]]

- **arXiv**: [2605.30660](https://arxiv.org/abs/2605.30660)
- **PDF**: https://arxiv.org/pdf/2605.30660
- **详细分析**: [[20_Research/Papers/具身智能/BOKBO_(Best_of_K_Bad_Options)_Calibrated_Abstention_for_VLA_Policies|BOKBO (Best of K Bad Options): Calibrated Abstention for VLA Policies]]
- **作者**: Anya Singh, Cabrel Happi, Jai Relan, Varun Nair, Vidyut Baradwaj
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《BOKBO (Best of K Bad Options): Calibrated Abstention for VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time scaling for vision-language-action (VLA) policies, methods such as RoboMonkey, SEAL, MG-Select, and V-GPS, samples K candidate action chunks at inference and executes the verifier-best. When all K candidates are unsafe, the system executes a violating action with no warning. We propose BOKBO, the first conformal abstention layer for K-sample VLA inference, providing finite-sample distribution-free guarantees on executed-violation rate. We provide both global and per-task (Mondrian) variants, with the per-task variant closing the conditional gap on the hardest tasks. Our analysis exposes a structural failure of policy-internal nonconformity scores under perturbation-based K-sampling: the base-policy confidence proxy and K-sample disagreement correlate at 0.98 with the action-noise hyperparameter $σ$, while correlating at the noise floor with actual safety violations. We test the failure's scope by replicating the analysis under token-level temperature sampling and find the failure is mechanism-specific and partially mitigated under policy-stochasticity-based sampling. A learned violation predictor conditioned on semantic visual features and task identity supports tight calibration: at $ε$ = 0.05 on libero_object_temp_x0.1 with OpenVLA-OFT, the conditional CRC bound holds on 86% of bootstrap splits with 78% coverage and 70% net task success. Mondrian-BOKBO raises the minimum per-task conditional hold fraction from 0.71 to 0.93. Results are stable across 5 training seeds, replicate within bootstrap noise on $π_0$-FAST, hold on libero_spatial_temp_x0.1 as a co-equal benchmark, and survive four within-suite distribution shifts. We additionally identify and correct a methodological pitfall: globally-set force thresholds well below expert-typical manipulation forces conflate unsafe behavior with normal manipulation, inflating violation rates by $5\times$.

</details>

---

### [[20_Research/Papers/强化学习/ZAPS-DA_Zero-Phase_Action_Policy_Smoothing_with_Decoupled_Actor_for_Continuous_Control_in_Reinforcement_Learning|ZAPS-DA: Zero-Phase Action Policy Smoothing with Decoupled Actor for Continuous Control in Reinforcement Learning]]

![[assets/2605.30612_figure.png|800]]

- **arXiv**: [2605.30612](https://arxiv.org/abs/2605.30612)
- **PDF**: https://arxiv.org/pdf/2605.30612
- **详细分析**: [[20_Research/Papers/强化学习/ZAPS-DA_Zero-Phase_Action_Policy_Smoothing_with_Decoupled_Actor_for_Continuous_Control_in_Reinforcement_Learning|ZAPS-DA: Zero-Phase Action Policy Smoothing with Decoupled Actor for Continuous Control in Reinforcement Learning]]
- **作者**: Faiq Shamass
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《ZAPS-DA: Zero-Phase Action Policy Smoothing with Decoupled Actor for Continuous Control in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous control policies trained with off-policy reinforcement learning frequently exhibit high-frequency action jitter, rendering direct deployment on physical actuators impractical. Post-hoc filtering attenuates jitter but introduces phase lag; embedding smoothness penalties in the actor's loss couples them with the RL gradient and conflates reward regression with over-aggressive smoothing. We present ZAPS-DA, a framework that reduces action jitter at deployment with negligible phase lag and no post-processing. ZAPS-DA pairs an unmodified main actor (trained by the base RL loss) with a separate decoupled actor trained via supervised imitation of zero-phase filtered targets stored in the replay buffer. The deployed policy is the decoupled actor: a feed-forward map from the current observation to a smooth action, with no inference-time filter and no action-history input -- a mechanism we term causal distillation of a non-causal filter. A magnitude-matched MSE loss provides zero-hyperparameter portability across optimizer classes. Validated with Soft Actor-Critic and a Savitzky--Golay filter in two driving simulators using paired n=150 evaluation protocols: on MetaDrive, ZAPS-DA reduces steering jitter by 14--21x and throttle jitter by 3--5x (all $p &lt; 10^{-4}$, Bonferroni-corrected) while matching task-completion (p=0.28 success, p=0.31 crash) at a 6.3% reward cost; on a custom Webots adaptive cruise control environment, the same SG configuration produces a Pareto improvement -- reward parity (p=0.121), 8--45x steering jitter reduction, and total task-failure rate reduced from 2.0% to 0.7%.

</details>

---
