# cs.LG | Machine Learning | 2026-07-24

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/大模型/The_Dark_Room_in_the_Reward_Channel_Dense_Prediction_Rewards_Collapse_GRPO-Trained_LLM_Agents_--_and_What_Actually_Works|The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works]]

![[assets/2607.21273_figure.png|800]]

- **arXiv**: [2607.21273](https://arxiv.org/abs/2607.21273)
- **PDF**: https://arxiv.org/pdf/2607.21273
- **详细分析**: [[20_Research/Papers/大模型/The_Dark_Room_in_the_Reward_Channel_Dense_Prediction_Rewards_Collapse_GRPO-Trained_LLM_Agents_--_and_What_Actually_Works|The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works]]
- **作者**: Yu Wang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《The Dark Room in the Reward Channel: Dense Prediction Rewards Collapse GRPO-Trained LLM Agents -- and What Actually Works》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, HiddenRule-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dense per-step supervision is an appealing remedy for sparse-reward, long-horizon LLM agents: reward the agent for predicting its next observation, and memory should follow. We show that under group-normalized RL (GRPO), this recipe does not merely fail -- it destroys the policy. Across Qwen3-1.7B/4B/8B on ALFWorld, a potential-based prediction reward drives every run into a degenerate absorbing state (prediction accuracy -&gt; 1.0, task success -&gt; 0,episode length pinned at the horizon): the "dark room" pathology, built automatically by the optimizer. A single-factor ablation localizes the cause -- removing only GRPO's std normalization turns the same reward from catastrophic (0%) into baseline parity -- and a two-line proposition explains why: in all-fail groups the z-scored advantage is invariant to the shaping coefficient, so bounded rewards become unbounded pressure and annealing cannot help. Our central insight generalizes this: what z-scoring amplifies is a dense signal's within-group variance while all-fail groups dominate, so signals whose variance decays by mastery are structurally amplifier-safe.This variance-profile criterion retrodicts our collapses, carries preregistered predictions for arms that had not yet run, and is consistent with published reward-channel successes (a compatibility check, not an independent test). Finally, a controlled signal-delivery matrix (identical signal, varying only the consumption mechanism) shows the reward channel is at best neutral while the auxiliary-loss channel gains ~20 points -- and a shuffled-gold placebo matches the true-gold arm, so the gap survives without correct labels. Endpoints are single-seed; seed replication and group-size controls are preregistered and in progress.

</details>

---

### [[20_Research/Papers/强化学习/Approximate_Quantum_State_Preparation_Through_Proximal_Policy_Optimization|Approximate Quantum State Preparation Through Proximal Policy Optimization]]

![[assets/2607.21121_figure.png|800]]

- **arXiv**: [2607.21121](https://arxiv.org/abs/2607.21121)
- **PDF**: https://arxiv.org/pdf/2607.21121
- **详细分析**: [[20_Research/Papers/强化学习/Approximate_Quantum_State_Preparation_Through_Proximal_Policy_Optimization|Approximate Quantum State Preparation Through Proximal Policy Optimization]]
- **作者**: Marco Mordacci, Michele Amoretti
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Approximate Quantum State Preparation Through Proximal Policy Optimization》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, a quantum architecture search framework for approximate quantum state preparation (QSP) is proposed. QSP is a challenging task, since the search space grows exponentially with the number of qubits, making the identification of the optimal circuit non-trivial. To address this problem, deep reinforcement learning is employed through an agent based on proximal policy optimization. The objective of the agent is to identify the best possible approximation of the target state while simultaneously minimizing the number of gates used. At each step, the agent appends a new gate to the circuit and recomputes the fidelity between the approximated state and the target states. Various experiments have been performed from 2 to 5 qubits. Both predefined states, such as Bell, GHZ, W, and Dicke states, and completely random states are considered. The proposed framework is able to achieve approximation errors of $10^{-14}$.

</details>

---

### [[20_Research/Papers/具身智能/Offline_RL_with_Hierarchical_Action_Chunking|Offline RL with Hierarchical Action Chunking]]

![[assets/2607.20834_figure.png|800]]

- **arXiv**: [2607.20834](https://arxiv.org/abs/2607.20834)
- **PDF**: https://arxiv.org/pdf/2607.20834
- **详细分析**: [[20_Research/Papers/具身智能/Offline_RL_with_Hierarchical_Action_Chunking|Offline RL with Hierarchical Action Chunking]]
- **作者**: Ahad Jawaid
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 1.62（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 0.2）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Offline RL with Hierarchical Action Chunking》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning (RL) holds the promise of learning general-purpose policies from static datasets. However, scaling these methods to long-horizon tasks remains a challenge due to the curse of horizon, where value estimation errors can compound through long chains of bootstrapped Bellman backups. Existing hierarchical approaches mitigate this by decomposing tasks into subgoals, yet they often rely on low-level controllers that suffer from myopic execution and biased value estimates. In this work, we propose Hierarchical Implicit Q-Chunking (HiQC), an offline goal-conditioned RL algorithm that combines high-level latent planning with low-level action chunking. By conditioning the low-level critic on temporally extended action sequences, HiQC enables unbiased k-step value backups, compressing the horizon at both the planning and execution levels. We theoretically demonstrate that this dual decomposition results in a tighter bound on value error under a bounded per-backup error model compared to standard hierarchy or flat chunking alone. Empirically, HiQC achieves the highest aggregate performance among the compared methods on the OGBench suite, with its largest gains on long-horizon navigation tasks such as humanoid-giant.

</details>

---

### [[20_Research/Papers/强化学习/Robust_Asynchronous_Q-Learning_under_Reward_and_State_Corruption_via_Batching|Robust Asynchronous Q-Learning under Reward and State Corruption via Batching]]

![[assets/2607.20822_figure.png|800]]

- **arXiv**: [2607.20822](https://arxiv.org/abs/2607.20822)
- **PDF**: https://arxiv.org/pdf/2607.20822
- **详细分析**: [[20_Research/Papers/强化学习/Robust_Asynchronous_Q-Learning_under_Reward_and_State_Corruption_via_Batching|Robust Asynchronous Q-Learning under Reward and State Corruption via Batching]]
- **作者**: Sreejeet Maity, Aritra Mitra
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Robust Asynchronous Q-Learning under Reward and State Corruption via Batching》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motivated by reinforcement learning in harsh environments, we consider the problem of learning an optimal policy subject to adversarially corrupted feedback. Specifically, at each time-step, an adversary can perturb both the reward and state observations of the learner following the Huber contamination model. To defend against such data corruption, we propose {\texttt{BR-Async-Q}}: a novel, epoch-based, robust \(Q\)-learning algorithm built upon two key ideas: (i) partitioning the online data stream into batches to reduce variance, and (ii) constructing robust estimates of the Bellman optimality operator using such batched data. We prove a high-probability $\ell_\infty$ error bound for {\texttt{BR-Async-Q}} that matches that for vanilla \(Q\)-learning, up to a small additive term that scales with the fraction of corrupted samples. To our knowledge, this provides the first robustness guarantee for asynchronous \(Q\)-learning subject to both reward and state corruption. Furthermore, when only rewards are corrupted, the dependence of our algorithm's bound on the corruption fraction is minimax optimal.

</details>

---

### [[20_Research/Papers/强化学习/Perspective_Latents_as_an_Architectural_Condition_for_Causal_Emergence_in_Active_Inference_Agents|Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents]]

![[assets/2607.20708_figure.png|800]]

- **arXiv**: [2607.20708](https://arxiv.org/abs/2607.20708)
- **PDF**: https://arxiv.org/pdf/2607.20708
- **详细分析**: [[20_Research/Papers/强化学习/Perspective_Latents_as_an_Architectural_Condition_for_Causal_Emergence_in_Active_Inference_Agents|Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents]]
- **作者**: Hongju Pae
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Perspective Latents as an Architectural Condition for Causal Emergence in Active Inference Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A recent line of work measures causal emergence in reinforcement learning agents through Integrated Information Decomposition, reporting that $Φ_r$ grows with training and tracks reward improvement. For active inference, this raises the question of how reward-free predictive organization relates to such information-theoretic signatures. I test this within an active inference agent whose architecture separates a fast perception latent $z$ from a slow global latent $g$, where $g$ is driven by prediction error and structurally decoupled from policy gradients. In a reward-free environmental regime-switching protocol, $Φ_r$ concentrates in $g$; its aggregate magnitude is largely architectural and decreases with training. The substantive effect of learning becomes legible only at the atom-compositional level: decoupling flips sign from negative to positive and becomes regime-invariant under environmental change, while downward causation carries the regime-dependent adjustment. These results identify $g$ as the architectural locus of $Φ_r$-relevant temporal organization in an active inference agent, and argue against reading scalar $Φ_r$ as a direct index of learned integration.

</details>

---

### [[20_Research/Papers/大模型/Chronofy_A_Temporal-Logical_Decay_Architecture_for_Information_Validity_in_Time-Aware_Retrieval-Augmented_Generation|Chronofy: A Temporal-Logical Decay Architecture for Information Validity in Time-Aware Retrieval-Augmented Generation]]

![[assets/2607.20560_first_page.png|800]]

- **arXiv**: [2607.20560](https://arxiv.org/abs/2607.20560)
- **PDF**: https://arxiv.org/pdf/2607.20560
- **详细分析**: [[20_Research/Papers/大模型/Chronofy_A_Temporal-Logical_Decay_Architecture_for_Information_Validity_in_Time-Aware_Retrieval-Augmented_Generation|Chronofy: A Temporal-Logical Decay Architecture for Information Validity in Time-Aware Retrieval-Augmented Generation]]
- **作者**: Muntaser Syed, Marius Silaghi, Sheikh Abujar, Sharun Akter
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM

#### 研究背景与动机

《Chronofy: A Temporal-Logical Decay Architecture for Information Validity in Time-Aware Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HiTANet, TIMER-Bench, TMRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) systems retrieve and integrate external knowledge to ground large language model (LLM) outputs. However, current RAG architectures treat all retrieved facts as equally valid regardless of temporal provenance, leading to temporal hallucination, where plausible but obsolete facts corrupt the output. A clinical lab reading from yesterday is actionable; the same reading from six months ago is noise. We present Chronofy, a three-layer neuro-symbolic framework implementing the Temporal-Logical Decay Architecture (TLDA) that embeds temporal validity directly into the representation, retrieval, and reasoning layers of RAG systems. Layer 1 reserves a dedicated temporal subspace within Matryoshka embeddings to make fact age structurally irremovable from the representation. Layer 2 integrates learnable exponential decay functions into graph-based retrieval, where the decay coefficient $β_j$ is grounded in Bayesian decision theory as an approximation of twice the latent process mean-reversion rate. Layer 3 applies Signal Temporal Logic (STL) robustness functions to evaluate the temporal validity of retrieved knowledge, not LLM output confidence, and enforces the possibilistic weakest-link principle to bound output confidence by the most decayed evidence in the reasoning chain. We evaluate Chronofy on temporal knowledge graph forecasting benchmarks, the TimE temporal QA benchmark, and a domain-specific sensitivity analysis, demonstrating that explicit temporal decay modeling improves retrieval precision, reduces temporal hallucination, and enables principled data re-acquisition triggers when temporal context is insufficient.

</details>

---

### [[20_Research/Papers/强化学习/Conflict_Resolution_under_Degraded_Surveillance_in_Air_Corridors_Using_Multi-Agent_Reinforcement_Learning|Conflict Resolution under Degraded Surveillance in Air Corridors Using Multi-Agent Reinforcement Learning]]

![[assets/2607.20547_figure.png|800]]

- **arXiv**: [2607.20547](https://arxiv.org/abs/2607.20547)
- **PDF**: https://arxiv.org/pdf/2607.20547
- **详细分析**: [[20_Research/Papers/强化学习/Conflict_Resolution_under_Degraded_Surveillance_in_Air_Corridors_Using_Multi-Agent_Reinforcement_Learning|Conflict Resolution under Degraded Surveillance in Air Corridors Using Multi-Agent Reinforcement Learning]]
- **作者**: Esrat Farhana Dulia, Syed Arbab Mohd Shihab, Caleb Adams, Ruben Del Rosario
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Conflict Resolution under Degraded Surveillance in Air Corridors Using Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe Advanced Air Mobility operations require aircraft to maintain separation when surveillance information is noisy, delayed, incomplete, or temporarily unavailable. This study develops a Deep Q-Network-based Multi-Agent Reinforcement Learning framework for decentralized conflict resolution among heterogeneous small unmanned aerial vehicles and electric vertical takeoff and landing aircraft operating within a structured three-dimensional corridor. Separate policies are trained for the two aircraft categories using local observations and a 14-action space that includes maintaining course, turning, vertical maneuvering, landing, and speed control. The simulation incorporates aircraft-specific dynamics, energy use, corridor constraints, observation noise, communication delay, information dropout, wind disturbance, actuator uncertainty, and model uncertainty. The trained policies are evaluated across 90 combinations of traffic density and minimum separation thresholds. Loss-of-separation frequency and duration generally increase with traffic density and separation requirements, although most events are resolved within 1s. Under safe conditions, agents maintain their motion approximately 79% of the time. During conflicts, turning accounts for 33% of actions, followed by maintaining motion at 29%, speed control at 25%, and vertical maneuvers at 13%. Six Pareto-optimal configurations reveal trade-offs between safety and corridor capacity. The framework supports the simulation-based evaluation of safer AAM conflict-resolution strategies under degraded surveillance conditions.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_CoLRAG-TF_Triple-Filtered_Retrieval_for_Complex_PDFs|Multimodal CoLRAG-TF: Triple-Filtered Retrieval for Complex PDFs]]

![[assets/2607.20517_figure.png|800]]

- **arXiv**: [2607.20517](https://arxiv.org/abs/2607.20517)
- **PDF**: https://arxiv.org/pdf/2607.20517
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_CoLRAG-TF_Triple-Filtered_Retrieval_for_Complex_PDFs|Multimodal CoLRAG-TF: Triple-Filtered Retrieval for Complex PDFs]]
- **作者**: Takato Yasuno
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Multimodal CoLRAG-TF: Triple-Filtered Retrieval for Complex PDFs》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) over heterogeneous PDF collections remains challenging due to multimodal content, domain-specific terminology, and the need for multi-hop reasoning across dispersed evidence. We present Multimodal CoLRAG-TF, a four-axis fusion architecture that integrates dense text embeddings, BM25 keyword matching, knowledge-graph triple filtering, and image-based similarity for robust retrieval over complex documents. Our system constructs a multimodal index of 2,403 blocks extracted from 43 Japanese disaster lesson PDFs, supported by a hybrid OCR pipeline and LLM-based caption generation. To enhance compositional reasoning, we extract 11,414 OpenIE triples and index them with FAISS, enabling sub-second triple lookup and hierarchical propagation of relevance signals. A HippoRAG2-inspired coarse-to-fine retriever (volume $\to$ chapter $\to$ block) narrows the search space before final fusion scoring. Bayesian optimization over fusion weights reveals that the triple axis must dominate ($α_\text{triple} = 0.44$) to counteract lexical bias and sustain multi-hop retrieval quality. Evaluated on a 457-pair benchmark, Multimodal CoLRAG-TF achieves a Retrieval Recall of 0.9909 and a 71.6$\%$ improvement in multi-hop answer similarity over single-hop queries. An image-to-lesson pipeline using a vision LLM further demonstrates the applicability of the approach to visual inputs. These results show that triple-filtered multimodal fusion is essential for structured reasoning over noisy, heterogeneous PDFs and provides a general framework applicable beyond the disaster domain.

</details>

---
