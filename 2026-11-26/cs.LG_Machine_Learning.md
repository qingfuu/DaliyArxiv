# cs.LG | Machine Learning | 2026-11-26

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/Provably_Efficient_Offline_Discounted_Reinforcement_Learning_under_Recursive_Entropic_Risk|Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk]]

![[assets/2611.34840_first_page.png|800]]

- **arXiv**: [2611.34840](https://arxiv.org/abs/2611.34840)
- **PDF**: https://arxiv.org/pdf/2611.34840
- **详细分析**: [[20_Research/Papers/强化学习/Provably_Efficient_Offline_Discounted_Reinforcement_Learning_under_Recursive_Entropic_Risk|Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk]]
- **作者**: Amirparsa Bahrami, Oliver Mortensen, Mohammad Sadegh Talebi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Provably Efficient Offline Discounted Reinforcement Learning under Recursive Entropic Risk》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study risk-sensitive reinforcement learning in finite discounted infinite-horizon Markov Decision Processes with recursive entropic risk measures (ERM), parameterized by $β\neq 0$. We consider both risk-averse ($β&gt;0$) and risk-seeking ($β&lt;0$) settings. We consider the offline RL setting, where the agent is provided with a fixed dataset and wishes to learn a near-optimal policy using this dataset. We introduce a model-based algorithm, called ERM Value Iteration Lower Confidence Bound (ERM-VI-LCB) and derive a PAC-type bound on its sample complexity. We also establish a corresponding lower bound, demonstrating that exponential dependence on $|β|/(1-γ)$ asserted by the upper bound is unavoidable in the worst case. The presented bounds provide the first rigorous sample complexity guarantees for offline RL under recursive ERM across both risk-averse and risk-seeking regimes.

</details>

---

### [[20_Research/Papers/强化学习/Split-RL_Local_Conflict_Resolution_in_Reinforcement_Learning|Split-RL: Local Conflict Resolution in Reinforcement Learning]]

![[assets/2611.34799_figure.png|800]]

- **arXiv**: [2611.34799](https://arxiv.org/abs/2611.34799)
- **PDF**: https://arxiv.org/pdf/2611.34799
- **详细分析**: [[20_Research/Papers/强化学习/Split-RL_Local_Conflict_Resolution_in_Reinforcement_Learning|Split-RL: Local Conflict Resolution in Reinforcement Learning]]
- **作者**: Benjamin Fuhrer, Chen Tessler, Gal Dalal
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.16，世界模型 0.16，机器人 0.2）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Split-RL: Local Conflict Resolution in Reinforcement Learning》归入 强化学习、机器人、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Constrained-RL, GBRL, Offline-RL, SUMO-RL, Split-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) policies are often trained by mixing contradictory feedback that is localized in space and time. For example, a robot may prioritize speed in open areas versus precision in tight gaps. We introduce Split-RL, a Gradient Boosting Trees (GBT) algorithm that uses guidance labels to locally isolate these conflicting signals. Standard neural networks (NNs) lack the structural mechanism to do this, as their parameters share feedback from all sources. While GBT provides the inductive bias to explicitly partition the state-space per objective, standard tree-fitting procedures aggregate contradictory gradient signals before they reach the leaves. Split-RL leverages this bias to integrate guidance labels into tree construction, routing these updates into disjoint state-space regions and preventing signal interference. Such labels can arise from heuristics, sensor-derived events, or existing rule-based systems, allowing Split-RL to incorporate rule-derived structure while retaining a learned policy. We theoretically show how early gradient aggregation loses objective-specific information and characterize when the Split-RL score isolates conflicting updates. We focus on constrained RL and offline RL with mixed datasets, each balancing two objectives that conflict locally. Across domains with spatial, rare-event, and temporal conflicts, Split-RL consistently outperforms existing methods by meeting the episodic cost budget while maintaining competitive rewards. In offline settings, Split-RL localizes the tradeoff between imitation and policy improvement, outperforming other methods and achieving near-expert performance across varying dataset sizes.

</details>

---

### [[20_Research/Papers/强化学习/Provably_Efficient_Concave_Utility_Reinforcement_Learning_with_Linear_Function_Approximation|Provably Efficient Concave Utility Reinforcement Learning with Linear Function Approximation]]

![[assets/2611.34678_figure.png|800]]

- **arXiv**: [2611.34678](https://arxiv.org/abs/2611.34678)
- **PDF**: https://arxiv.org/pdf/2611.34678
- **详细分析**: [[20_Research/Papers/强化学习/Provably_Efficient_Concave_Utility_Reinforcement_Learning_with_Linear_Function_Approximation|Provably Efficient Concave Utility Reinforcement Learning with Linear Function Approximation]]
- **作者**: Max Qiushi Lin, Ahmed Magd, Sharan Vaswani
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.36，世界模型 0.36）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Provably Efficient Concave Utility Reinforcement Learning with Linear Function Approximation》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CURL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Concave utility reinforcement learning (CURL) unifies a diverse range of problems, including standard reinforcement learning (RL), imitation learning, and maximum entropy exploration. Unlike standard RL, CURL generally requires estimating high-dimensional state-action occupancy measures. Consequently, existing methods for CURL either sidestep the exploration problem, are restricted to the tabular setting, or lack computationally efficient policy optimization. To address this, we study CURL in finite-horizon episodic bilinear MDPs, where the transition model admits a low-dimensional representation in known feature spaces. We use the bilinear structure to efficiently estimate occupancy measures via low-dimensional feature expectations, and propose a model-based optimistic concave utility policy optimization (OCUPO) framework. We first instantiate OCUPO in the on-policy setting, where each iteration uses independent trajectories to estimate the concave utility policy gradient, and prove an $\widetilde{O}(ε^{-4})$ sample complexity. To improve sample efficiency, we then instantiate OCUPO in the off-policy setting. We propose a novel backward feature regression subroutine that reuses trajectories collected by past policies to estimate the occupancy measure of the current policy. Under suitable technical assumptions on the policy class (satisfied, e.g., by log-linear policies with sufficiently expressive features), we prove that the resulting algorithm achieves an $\widetilde{O}(ε^{-2})$ sample complexity, up to a controllable projection error. We further extend our framework to linear MDPs and show that the resulting off-policy algorithm retains the same sample complexity. In these settings, the dependence on $ε$ matches that for standard RL with linear function approximation. Moreover, our algorithms do not rely on the integral oracle required by prior work.

</details>

---

### [[20_Research/Papers/强化学习/Distractor-Robust_Reinforcement_Learning_via_Variational_Bisimulation|Distractor-Robust Reinforcement Learning via Variational Bisimulation]]

![[assets/2611.34641_figure.png|800]]

- **arXiv**: [2611.34641](https://arxiv.org/abs/2611.34641)
- **PDF**: https://arxiv.org/pdf/2611.34641
- **详细分析**: [[20_Research/Papers/强化学习/Distractor-Robust_Reinforcement_Learning_via_Variational_Bisimulation|Distractor-Robust Reinforcement Learning via Variational Bisimulation]]
- **作者**: Benjamin Freed, Vivaan Singh, Dean Zadok, Roberto Calandra, Jeff Schneider, Howie Choset
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 机器人
- **相关性评分**: 1.72（加权：强化学习 0.96，世界模型 0.56，机器人 0.2）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Distractor-Robust Reinforcement Learning via Variational Bisimulation》归入 强化学习、世界模型、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model-based reinforcement learning (MBRL) promises data efficiency and generalization, but typical reconstruction-based objectives encourage models to waste representational capacity on task-irrelevant distractors. We introduce VIBES (Variational Inference for Bisimulation-based Encoded States), a new objective that replaces pixel reconstruction with an adversarial term, which enforces that latent states suffice to predict both rewards and the next latent state. We show that this objective measures how far the encoder is from reward and dynamics sufficiency, and that whenever exact sufficiency is attainable, its global optima induce bisimulation relations on histories. Combined with a fixed-capacity latent bottleneck, this encourages latent states to retain task-relevant information while discarding irrelevant variation. Our method serves as a drop-in replacement for Dreamer's model-learning component, achieves state-of-the-art performance on the Distracting Control Suite, and extends to visually complex manipulation in Realistic ManiSkill. Unlike prior approaches, it does not rely on image-specific augmentations and applies equally well to high-dimensional vector-state tasks, demonstrated on a 100-link swimmer robot. Finally, latent-space analyses (UMAP embeddings and nearest-neighbor probes) confirm that the learned representations are sensitive to task-relevant structure while invariant to distractors.

</details>

---

### [[20_Research/Papers/强化学习/Kant-Q_A_Q-Learning_Algorithm_for_Kantian_Equilibrium_in_Symmetric_Markov_Games|Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games]]

![[assets/2611.34536_figure.png|800]]

- **arXiv**: [2611.34536](https://arxiv.org/abs/2611.34536)
- **PDF**: https://arxiv.org/pdf/2611.34536
- **详细分析**: [[20_Research/Papers/强化学习/Kant-Q_A_Q-Learning_Algorithm_for_Kantian_Equilibrium_in_Symmetric_Markov_Games|Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games]]
- **作者**: Rishi Bharadwaj, Sujit Gujar, Yadati Narahari
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.2，强化学习 1.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Kant-Q: A Q-Learning Algorithm for Kantian Equilibrium in Symmetric Markov Games》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GovSim, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents increasingly interact with one another, and many of these interactions are mixed-motive games, which have posed a persistent challenge for learning algorithms. Most multi-agent reinforcement learning (MARL) algorithms are designed to reach Nash equilibria, yet in many such games these equilibria are Pareto-inefficient. We instead study Kantian equilibria, an economic solution concept in which each agent plays the action it would want all agents to adopt. In symmetric games, this corresponds to an optimal common policy. We propose Kant-Q, a Q-learning algorithm in which each agent learns action profiles where all agents play the same action. Each update is then a sample from a single-agent MDP, so Kant-Q inherits the convergence guarantees of standard Q-learning. We show that every symmetric Markov game has a pure Kantian equilibrium. We also prove that all agents' Q-tables converge to the same limit, whose greedy policy is such an equilibrium, and that greedy play converges whenever the optimal common action is unique at every state. We further show that in a subclass of symmetric monotone games, the Kantian equilibrium is Pareto-efficient among pure strategy profiles and strictly individually rational. Empirically, on the iterated Prisoner's Dilemma and the GovSim fishery with up to 200 agents, Kant-Q learns the Kantian equilibrium, while the baselines underperform. Since copies of the same AI system naturally face one another in symmetric games, these results suggest universalization as a design principle for cooperative AI-AI interaction.

</details>

---

### [[20_Research/Papers/强化学习/Feasibility-Aware_Deep_Reinforcement_Learning_for_O-CU_and_O-DU_Mapping_in_6G_O-RAN|Feasibility-Aware Deep Reinforcement Learning for O-CU and O-DU Mapping in 6G O-RAN]]

![[assets/2611.34516_figure.JPG|800]]

- **arXiv**: [2611.34516](https://arxiv.org/abs/2611.34516)
- **PDF**: https://arxiv.org/pdf/2611.34516
- **详细分析**: [[20_Research/Papers/强化学习/Feasibility-Aware_Deep_Reinforcement_Learning_for_O-CU_and_O-DU_Mapping_in_6G_O-RAN|Feasibility-Aware Deep Reinforcement Learning for O-CU and O-DU Mapping in 6G O-RAN]]
- **作者**: Mohammad Asif Habibi, Xavier Costa-Perez, Hans D. Schotten
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Feasibility-Aware Deep Reinforcement Learning for O-CU and O-DU Mapping in 6G O-RAN》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies the mapping of the virtual network function components (VNFCs) of the O-RAN central unit (O-CU) and O-RAN distributed unit (O-DU) onto virtual machines (VMs) in sixth-generation (6G) open radio access networks (O-RAN). The problem is formulated as a feasibility-aware sequential decision process that maximizes the number of placed VNFCs and, secondarily, favors fewer active VMs and lower residual resource wastage. Although conventional optimization techniques can solve this problem, their computational cost becomes prohibitive for larger instances or when optimization must be repeated. To address this limitation, we explore two neural reinforcement learning (RL)-based methods: a deep $Q$-network (DQN) and a double deep $Q$-network (Double DQN). Whereas DQN uses the same target network to both select and evaluate the bootstrap action, Double DQN decouples these two operations to mitigate maximization-induced overestimation. We compare both methods against six baselines: random feasible placement, first-fit, first-fit decreasing, best-fit, a resource-wastage-aware heuristic, and a time-bounded mixed-integer linear programming (MILP) solver. We conduct a controlled experimental evaluation across four problem sizes with $30$ independent instances each, together with capacity-stress, distribution-shift, and reward-ablation experiments. For the $16 \times 8$ VNFC-to-VM scenario, DQN and Double DQN achieve mean placed-VNFC fractions of $0.990$ and $0.996$, respectively. However, first-fit decreasing and the resource-wastage-aware heuristic match this placement quality with lower efficiency cost and lower decision time, whereas the MILP attains the lowest efficiency cost at a much higher runtime. The results clarify the strengths and limitations of neural placement for this static problem, without establishing superiority over conventional methods.

</details>

---

### [[20_Research/Papers/强化学习/Normalizing_Flows_are_Capable_World_Models|Normalizing Flows are Capable World Models]]

![[assets/2611.33872_figure.png|800]]

- **arXiv**: [2611.33872](https://arxiv.org/abs/2611.33872)
- **PDF**: https://arxiv.org/pdf/2611.33872
- **详细分析**: [[20_Research/Papers/强化学习/Normalizing_Flows_are_Capable_World_Models|Normalizing Flows are Capable World Models]]
- **作者**: Zijia Li, Yong-Hyun Park, Shusheng Yang, Jiatao Gu
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Normalizing Flows are Capable World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A world model lets an agent anticipate the consequences of its actions and use imagined futures to make decisions. We introduce Normalizing-Flow World Model (NFWM), which pairs an invertible observation encoder with an action-conditioned probabilistic predictor. Because the encoder is invertible, the predicted distribution over latent states defines a distribution over future observations. Maximizing the exact conditional likelihood of those observations therefore trains the representation and dynamics jointly. An agent can plan directly in the learned latent space and decode sampled trajectories to inspect possible futures. On Teleport, these samples capture the two possible outcomes of the same action. In Flappy Bird, a world model trained by likelihood alone supports reward-based planning that reaches 100 pipes in all ten evaluated games. For goal-conditioned control, an auxiliary inverse-dynamics objective shapes the coordinates used to compare predicted states with a goal. On LIBERO, NFWM uses this distance to select successful action sequences more often than LeWM and SMWM. In Atari Boxing, training on imagined trajectories improves a policy beyond its behavior-cloned initialization. Together, these results establish normalizing flows as capable world models.

</details>

---

### [[20_Research/Papers/强化学习/Learning_a_Whole-Body_Pivot-Walking_Gait_for_Heavy-Box_Transport_with_a_Humanoid|Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid]]

![[assets/2611.33828_figure.png|800]]

- **arXiv**: [2611.33828](https://arxiv.org/abs/2611.33828)
- **PDF**: https://arxiv.org/pdf/2611.33828
- **详细分析**: [[20_Research/Papers/强化学习/Learning_a_Whole-Body_Pivot-Walking_Gait_for_Heavy-Box_Transport_with_a_Humanoid|Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid]]
- **作者**: Rikuto Hidaka, Tsung-Yuan Chen, Kento Kawaharazuka
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.32（加权：具身智能 1.5，强化学习 0.36，世界模型 0.16，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning a Whole-Body Pivot-Walking Gait for Heavy-Box Transport with a Humanoid》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Through pivot walking, humans can transport objects that are too heavy to lift. Previous humanoid studies have relied on planned sequences in which object manipulation and stepping are executed separately and the object is brought to rest between successive rotations. However, few studies have developed a single learned controller for humanoid pivot walking. In this paper, we propose a single reinforcement-learning policy that jointly coordinates stepping, balance control, and object manipulation. The policy is trained using rewards that promote alternating pivot motions and a phase reference that progresses according to the displacement of the object. In simulation, we confirmed that the humanoid can pivot a box. For deployment, we fine-tuned the policy into an object-blind version that follows a periodic clock instead of the progress reference. On the real robot, the deployed policy transported the box forward by more than 1 m in all five trials; each trial ended at a base-tilt safety stop. These results demonstrate that coordinated humanoid pivot walking can be learned with reinforcement learning and transferred to a physical humanoid robot without direct object-state sensing.

</details>

---

### [[20_Research/Papers/机器人/Model_Predictive_Control_of_a_Multirotor_UAV_with_a_Cable-Suspended_Payload_A_Comparison_of_Shifted_and_Transformer-Based_Warm_Starts|Model Predictive Control of a Multirotor UAV with a Cable-Suspended Payload: A Comparison of Shifted and Transformer-Based Warm Starts]]

![[assets/2611.33514_first_page.png|800]]

- **arXiv**: [2611.33514](https://arxiv.org/abs/2611.33514)
- **PDF**: https://arxiv.org/pdf/2611.33514
- **详细分析**: [[20_Research/Papers/机器人/Model_Predictive_Control_of_a_Multirotor_UAV_with_a_Cable-Suspended_Payload_A_Comparison_of_Shifted_and_Transformer-Based_Warm_Starts|Model Predictive Control of a Multirotor UAV with a Cable-Suspended Payload: A Comparison of Shifted and Transformer-Based Warm Starts]]
- **作者**: Athanasios Zeris
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: cs.LG

#### 研究背景与动机

《Model Predictive Control of a Multirotor UAV with a Cable-Suspended Payload: A Comparison of Shifted and Transformer-Based Warm Starts》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study investigates model predictive control (MPC) of a multirotor drone (unmanned aerial vehicle, UAV) carrying a cable-suspended payload, comparing conventional shifted initialization with Transformer-based warm starting of a sequential convex programming (SCP) optimizer. The controller uses a coupled mechanical model with an elastic cable and a double-pendulum representation of the suspended load. Its formulation includes move-blocked control inputs, finite-difference sensitivities, constrained quadratic subproblems, and input-feasibility projection. A Transformer trained on expert SCP solutions predicts an initial control sequence, which is subsequently refined by the same optimizer used for the conventional methods. Numerical experiments compare zero, shifted, and Transformer initialization under identical controller settings. For independently solved MPC problems, Transformer initialization reduces computation time relative to zero initialization. In sequential closed-loop simulations, however, shifting the preceding optimized control sequence provides the lowest computation time, while all three methods produce similar tracking behavior. These findings emphasize the importance of comparing learned warm starts with conventional initialization methods that reuse previous MPC solutions. The measured optimization times exceed the control sampling period; consequently, real-time implementation is not demonstrated. Keywords: Model predictive control; sequential convex programming; Transformer; warm start; cable-suspended payload; multirotor drone.

</details>

---

### [[20_Research/Papers/强化学习/Differentially_Private_Policy_Optimization_in_Linear_MDPs_with_Adversarial_Rewards|Differentially Private Policy Optimization in Linear MDPs with Adversarial Rewards]]

![[assets/2611.33469_first_page.png|800]]

- **arXiv**: [2611.33469](https://arxiv.org/abs/2611.33469)
- **PDF**: https://arxiv.org/pdf/2611.33469
- **详细分析**: [[20_Research/Papers/强化学习/Differentially_Private_Policy_Optimization_in_Linear_MDPs_with_Adversarial_Rewards|Differentially Private Policy Optimization in Linear MDPs with Adversarial Rewards]]
- **作者**: Yi He
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Differentially Private Policy Optimization in Linear MDPs with Adversarial Rewards》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) in personalized services often relies on sensitive interaction data. Motivated by the need to protect these data, we study differentially private (DP) policy optimization in episodic linear Markov decision processes (MDPs) with unknown transitions and adaptive adversarial linear rewards under full-information feedback. This setting poses two key challenges: past trajectories are repeatedly reused for policy evaluation, and reward choices may depend on previously released private statistics. The proposed algorithm combines batched proximal policy optimization (PPO) updates with optimistic policy evaluation, using private regression statistics and reward estimates to protect both trajectories and reward functions under joint differential privacy (JDP). With all other parameters fixed, our high-probability regret bound retains the same leading $\widetilde{O}\left(K^{3/4}\right)$ dependence on the number of episodes $K$ as the corresponding non-private bound for batched optimistic PPO. The additional privacy terms scale as $\widetilde{O} \left(K^{5/8}\right)$ and $\widetilde{O} \left(K^{1/2}\right)$. Thus, privacy incurs only lower-order additive costs in $K$, even under adaptive adversarial rewards.

</details>

---

### [[20_Research/Papers/具身智能/An_Adversarial_Multi-Agent_Pursuit_Game_for_Locomotor_Agility_Pretraining|An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining]]

![[assets/2611.33407_figure.png|800]]

- **arXiv**: [2611.33407](https://arxiv.org/abs/2611.33407)
- **PDF**: https://arxiv.org/pdf/2611.33407
- **详细分析**: [[20_Research/Papers/具身智能/An_Adversarial_Multi-Agent_Pursuit_Game_for_Locomotor_Agility_Pretraining|An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining]]
- **作者**: Nathan A. C. Hogg, Matt Hyatt, Neil Klingensmith, George K. Thiruvathukal
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《An Adversarial Multi-Agent Pursuit Game for Locomotor Agility Pretraining》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agile humanoid locomotion requires controllers that can adapt to rapidly changing motion demands while remaining stable and robust. Recent locomotion controllers are typically designed with either a dense reward that is carefully shaped to encourage steps and penalize falling, or by using a reference tracking reward which teaches the controller to follow predetermined motions. Once a behavior that maximizes the reward is discovered, the controller ceases to learn. While generally stable, reference tracking methods focus on motor control separately from motion generation. Self-play has been proven as an effective technique for superhuman performance on several multiagent games like Go, Starcraft, hide-and-seek, and capture-the-flag. We train neural networks to play the game of multiagent tag in a physics simulator to study if new motion generation and control strategies can emerge through sparse feedback and competitive self-play. We present MJTag, a task suite for role-conditioned locomotion during competitive pursuit-evasion. Our model is a role-conditioned policy for a low-level locomotion controller and optional planar velocity commands. MJTag's league-based play with sparse feedback enables a locomotion controller to adopt new strategies, including dodging, sprinting, and tackling.

</details>

---
