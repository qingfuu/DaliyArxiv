# cs.LG | Machine Learning | 2026-08-21

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/世界模型/Orthogonal_JEPA_Factorized_Predictive_States_for_Latent_World_Models|Orthogonal JEPA: Factorized Predictive States for Latent World Models]]

![[assets/2608.20065_first_page.png|800]]

- **arXiv**: [2608.20065](https://arxiv.org/abs/2608.20065)
- **PDF**: https://arxiv.org/pdf/2608.20065
- **详细分析**: [[20_Research/Papers/世界模型/Orthogonal_JEPA_Factorized_Predictive_States_for_Latent_World_Models|Orthogonal JEPA: Factorized Predictive States for Latent World Models]]
- **作者**: Taoyong Cui, Pheng Ann Heng, Wanli Ouyang
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Orthogonal JEPA: Factorized Predictive States for Latent World Models》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models construct latent states that support prediction, planning, and reasoning about an underlying system. Joint-embedding predictive architectures (JEPAs) offer a direct way to learn such states by predicting targets in representation space instead of reconstructing every detail of the observation. Standard JEPAs, however, organize all predictable content through one target embedding and one prediction pathway. In complex systems, this monolithic state can allocate redundant capacity to dominant signals while providing weak or conflicting gradients to less dominant predictive structure. We introduce \method, a latent world-modeling framework based on orthogonal predictive factorization. Learned basis matrices analyze each target state into multiple components, and a dedicated prediction branch estimates each component from a shared context representation. Predictive regression preserves the factor magnitudes required for state synthesis, an orthogonality objective discourages repeated directions, factor-activity regularization maintains variation in projected targets, and online variance regularization discourages coordinate-wise encoder collapse. Predicted components are synthesized into a complete latent state that can be used by a readout, decoder, planner, or autoregressive rollout. The same predictive-state mechanism applies when the target is temporally future, spatially hidden, or another partial observation of the same system. Experiments on controlled vision, single-cell transcriptomics, longitudinal health records, continuous control, and molecular dynamics evaluate representation quality, forecasting, planning, and long-horizon stability.

</details>

---

### [[20_Research/Papers/强化学习/End-to-end_Early_Classification_of_Time_Series_in_Non-Stationary_Environments|End-to-end Early Classification of Time Series in Non-Stationary Environments]]

![[assets/2608.20044_figure.png|800]]

- **arXiv**: [2608.20044](https://arxiv.org/abs/2608.20044)
- **PDF**: https://arxiv.org/pdf/2608.20044
- **详细分析**: [[20_Research/Papers/强化学习/End-to-end_Early_Classification_of_Time_Series_in_Non-Stationary_Environments|End-to-end Early Classification of Time Series in Non-Stationary Environments]]
- **作者**: Aurélien Renault, Alexis Bondu, Antoine Cornuéjols, Vincent Lemaire
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《End-to-end Early Classification of Time Series in Non-Stationary Environments》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Early Classification of Time Series (ECTS) requires making accurate decisions as early as possible in inherently online and evolving environments. Yet, most existing methods assume stationarity and rely on separable designs, where classification and triggering are optimized independently, an assumption that fundamentally limits their adaptability under drift. In this work, we challenge this paradigm and study ECTS under non-stationary conditions. We provide the first systematic comparison between separable and end-to-end approaches across controlled drifting scenarios. Building on Reinforcement Learning, we introduce DQeND, a unified architecture that jointly learns representation, classification, and triggering decisions, while remaining directly comparable to state-of-the-art separable baselines. Across a wide range of drifts, DQeND demonstrates strong robustness across various non-stationary scenarios, consistently outperforming separable baselines. An ablation study further highlights that jointly updating representation and decision modules is critical to these gains. Overall, our results indicate that end-to-end learning can offer improved adaptation capabilities for ECTS in dynamic environments, and motivate further investigation of alternatives to separable designs.

</details>

---

### [[20_Research/Papers/大模型/G-MARK_Grounded_Multi-Agent_Reasoning_for_Cooperative_Driving_via_Knowledge_Graphs|G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs]]

![[assets/2608.19964_figure.png|800]]

- **arXiv**: [2608.19964](https://arxiv.org/abs/2608.19964)
- **PDF**: https://arxiv.org/pdf/2608.19964
- **详细分析**: [[20_Research/Papers/大模型/G-MARK_Grounded_Multi-Agent_Reasoning_for_Cooperative_Driving_via_Knowledge_Graphs|G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs]]
- **作者**: Bhavya Gupta, Onat Gungor, Tajana Rosing
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《G-MARK: Grounded Multi-Agent Reasoning for Cooperative Driving via Knowledge Graphs》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：V2V-GoT-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous driving systems must operate under partial observability, where safety-critical objects may be occluded or visible only to neighboring connected vehicles. Vehicle-to-vehicle cooperation can reduce this uncertainty, but existing cooperative driving methods often compress multi-agent evidence into latent features or hidden multimodal states. As a result, they obscure which agent observed each object, whether the object is visible to the ego vehicle, and how conflicting evidence affects downstream decisions. We propose G-MARK, a grounded multi-agent reasoning framework that converts cooperative object-centric observations into explicit provenance-aware knowledge graphs (KGs). The resulting KGs preserve object hypotheses together with their source attribution, ego-versus-partner visibility, uncertainty, conflicts, spatial relations, and planning-relevant context. G-MARK then derives a shared feature representation from these KGs, enabling lightweight task heads to support object reasoning, motion prediction, control selection, and trajectory forecasting. Compared with the state-of-the-art baseline, GMARK improves occlusion reasoning accuracy by 42.2%, reduces control-selection error by 13.1%, and achieves comparable trajectory-planning accuracy with a 25.6x smaller structured communication payload. Our code is available at https://github.com/bhavyagupta98/g-mark.

</details>

---

### [[20_Research/Papers/强化学习/Unregularized_Convergence_of_Single-Loop,_Entropy-Regularized_Natural_Actor-Critic|Unregularized Convergence of Single-Loop, Entropy-Regularized Natural Actor-Critic]]

![[assets/2608.19587_first_page.png|800]]

- **arXiv**: [2608.19587](https://arxiv.org/abs/2608.19587)
- **PDF**: https://arxiv.org/pdf/2608.19587
- **详细分析**: [[20_Research/Papers/强化学习/Unregularized_Convergence_of_Single-Loop,_Entropy-Regularized_Natural_Actor-Critic|Unregularized Convergence of Single-Loop, Entropy-Regularized Natural Actor-Critic]]
- **作者**: Zhiqiang Tan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Unregularized Convergence of Single-Loop, Entropy-Regularized Natural Actor-Critic》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While entropy regularization is widely used to stabilize and accelerate Natural Policy Gradient methods, its ability to yield faster convergence rates for the unregularized objective remains underexplored. Existing analyses often rely on double-loop architectures and invoke a linear entropy penalty. To bridge the gap between theory and practice, we analyze a single-loop, entropy-regularized Natural Actor-Critic algorithm under compatible linear function approximation. By training an uncentered critic, our critic tracking can remain stable even as the training policy approaches determinism and the Fisher information matrix degenerates. We focus on two primary regimes for the optimization landscape: a Stochastic Regime, where we fuse coupled actor-critic updates into a joint Lyapunov recurrence, and a Deterministic Regime, where we pivot to a Policy Mirror Descent framework to circumvent the collapse of Euclidean geometry. By exploiting a positive Minimal Action Gap in the unregularized Markov decision process, we introduce an Exponential Translation mechanism that maps the regularized gap to the unregularized one up to an exponentially decaying tail. By tuning the fixed temperature, our algorithm achieves accelerated unregularized convergence rates, up to approximation-error terms: $\tilde{\mathcal{O}}(T_{total}^{-1})$ in the Stochastic Regime, and $\tilde{\mathcal{O}}(T_{total}^{-2/3})$ for the average iterate alongside $\tilde{\mathcal{O}}(T_{total}^{-1/3})$ for the last iterate in the Deterministic Regime. Here, $T_{total}$ denotes the total number of stochastic critic updates (or Monte Carlo rollouts). Furthermore, in the tabular setting, our positive-action-gap analysis yields a $\tilde{\mathcal{O}}(T_{total}^{-2/3})$ average-iterate rate, surpassing the $\mathcal{O}(T_{total}^{-1/2})$ worst-case statistical barrier that applies without a positive action margin.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Multimodal_Alignment_Certifying_Physical_Language_through_Response_Substitution_and_Ordered_Execution|Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution]]

![[assets/2608.19492_first_page.png|800]]

- **arXiv**: [2608.19492](https://arxiv.org/abs/2608.19492)
- **PDF**: https://arxiv.org/pdf/2608.19492
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Multimodal_Alignment_Certifying_Physical_Language_through_Response_Substitution_and_Ordered_Execution|Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution]]
- **作者**: Kaizhen Tan, Xin Xu, Siru Tao, Yixiao Li, Hanzhe Hong, Yang Feng, Heqing Du
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.16，世界模型 0.36）
- **关联关键词**: Multimodal, Systems

#### 研究背景与动机

《Beyond Multimodal Alignment: Certifying Physical Language through Response Substitution and Ordered Execution》归入 大模型、世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models increasingly treat compact multimodal representations as interfaces between perception and physical interaction, yet existing probes do not establish whether different sensors carry the same executable meaning or whether that meaning survives a new action composition. We introduce an operational capability hierarchy and the Disjoint-Bridge Operator-Substitution Certificate (DBOSC), which asks whether independently trained modality compilers enter a frozen response chart interchangeably on evidence outside their training panels. On Cluster Haptic, audio and acceleration representations of the same unseen surface are 4.5x closer in response space than wrong-surface pairings, with the gap holding for all 19 held-out surfaces; unsealing withheld responses confirms that every branch predicts the physics better than the population chart. We then test ordered execution in a controlled elastoplastic system with complementary modality blind spots. At the pre-registered budget, the prerequisite refuses the stack because the frozen executor cannot advance even an exact chart coordinate through a held-out program. At a converged budget, the same rank-three chart executes those programs (oracle NMSE 0.18), fusion improves on both modalities, and 14 of 16 registered checks pass; the two failures arise because a diagonal restriction of the fused information matrix performs as well as the full one. Clearing the gate is a property of the executor, not the chart: an executor emitting whole programs instead of shared per-step dynamics is 38x worse than an entity-blind predictor on the same chart. A matching non-identifiability result explains why compression and fusion alone cannot determine an unseen composition law. These results separate attribute access, response substitution, fusion closure, and ordered execution into distinct, separately testable achievements.

</details>

---

### [[20_Research/Papers/强化学习/Demons_on_a_Budget_Adaptive_Measurement_Placement_at_the_Entanglement_Phase_Transition|Demons on a Budget: Adaptive Measurement Placement at the Entanglement Phase Transition]]

![[assets/2608.19248_figure.png|800]]

- **arXiv**: [2608.19248](https://arxiv.org/abs/2608.19248)
- **PDF**: https://arxiv.org/pdf/2608.19248
- **详细分析**: [[20_Research/Papers/强化学习/Demons_on_a_Budget_Adaptive_Measurement_Placement_at_the_Entanglement_Phase_Transition|Demons on a Budget: Adaptive Measurement Placement at the Entanglement Phase Transition]]
- **作者**: Rohan Pandey
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Demons on a Budget: Adaptive Measurement Placement at the Entanglement Phase Transition》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monitored quantum circuits exhibit a measurement-induced phase transition between volume-law and area-law entanglement as a function of the measurement rate $p$. Prior work places measurements at random locations and treats the rate as the control parameter. We instead fix the measurement budget and vary the placement process, comparing random placement against hand-designed and learned policies in brickwork random Clifford circuits at matched budget. First, placement geometry matters more than placement information. A deterministic contiguous sweep cuts the half-cut entropy by a factor of 3.4 relative to random placement, while equal-coverage unstructured placement and a greedy policy with full state access do far worse. The effect is carried by spatial order alone: measuring the $k$ least recently measured sites gives $4.14 \pm 0.06$ bits with random tie-breaking and $1.29 \pm 0.04$ bits with position-ordered tie-breaking. Second, the sweep eliminates the transition rather than shifting it. Tripartite mutual information crossings recede as $p^* \propto 1/L$, the steady-state entropy saturates at an $L$-independent ceiling near $0.46/p$, and data for $64 \le L \le 512$ collapse onto the form $S = p^{-1} f(pL)$ predicted by a ballistic regrowth argument. Third, in stabilizer dynamics every outcome is deterministic or a fair coin flip, so the record's Shannon entropy is exactly countable; the sweep dominates the entropy-versus-record-cost frontier while paying the same roughly one bit per measurement as random placement. Policies trained by cross-entropy and proximal policy optimization do not find the sweep: score-based policies parameterize which sites to measure, not the order in which degenerate scores are resolved, and the effect lives in that order. The phase diagram of monitored dynamics is a property of the placement process, not only of the measurement rate.

</details>

---
