# cs.LG | Machine Learning | 2026-06-04

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Enhancing_the_MADDPG_Algorithm_for_Multi-Agent_Learning_via_Action_Inference_and_Importance_Sampling|Enhancing the MADDPG Algorithm for Multi-Agent Learning via Action Inference and Importance Sampling]]

![[assets/2606.05021_figure.png|800]]

- **arXiv**: [2606.05021](https://arxiv.org/abs/2606.05021)
- **PDF**: https://arxiv.org/pdf/2606.05021
- **详细分析**: [[20_Research/Papers/强化学习/Enhancing_the_MADDPG_Algorithm_for_Multi-Agent_Learning_via_Action_Inference_and_Importance_Sampling|Enhancing the MADDPG Algorithm for Multi-Agent Learning via Action Inference and Importance Sampling]]
- **作者**: Marc Walden, Jason Liu, Shaashwath Sivakumar, Ryan Liu, Hamza Khan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.42（加权：大模型 0.5，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Enhancing the MADDPG Algorithm for Multi-Agent Learning via Action Inference and Importance Sampling》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AI_Net, MARL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate multi-agent deep reinforcement learning and propose two enhancements to the Multi-Agent Deep Deterministic Policy Gradient (MADDPG) algorithm. First, we introduce a novel Action Inference mechanism that enables each agent to predict other agents' intended actions, thereby improving the accuracy and stability of its own policy. Second, we apply an importance sampling strategy, using geometric distribution, in the replay buffer to prioritize more recent and informative experiences, which helps mitigate the non-stationarity inherent in multi-agent environments. We evaluate both modifications on the discrete-action Predator-Prey task provided by the PettingZoo library, a flexible Python interface for general multi-agent reinforcement learning benchmarks. Our results indicate that Action Inference is effective in improving learning stability and inter-agent cooperation and that importance sampling using geometric distribution can lead to significant improvements in exploration efficiency over standard MADDPG. Code available at this https URL

</details>

---

### [[20_Research/Papers/具身智能/COP-Q_Safety-First_Reinforcement_Learning_for_Robot_Control_via_Cholesky-Ordered_Projection|COP-Q: Safety-First Reinforcement Learning for Robot Control via Cholesky-Ordered Projection]]

![[assets/2606.04749_figure.png|800]]

- **arXiv**: [2606.04749](https://arxiv.org/abs/2606.04749)
- **PDF**: https://arxiv.org/pdf/2606.04749
- **详细分析**: [[20_Research/Papers/具身智能/COP-Q_Safety-First_Reinforcement_Learning_for_Robot_Control_via_Cholesky-Ordered_Projection|COP-Q: Safety-First Reinforcement Learning for Robot Control via Cholesky-Ordered Projection]]
- **作者**: Guopeng Li, Moritz A. Zanger, Matthijs T. J. Spaan, Julian F. P. Kooij
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 3.02（加权：具身智能 0.6，强化学习 1.16，世界模型 0.16，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《COP-Q: Safety-First Reinforcement Learning for Robot Control via Cholesky-Ordered Projection》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL, MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe robot control requires maximizing return while satisfying safety constraints. In off-policy safe reinforcement learning, reward and safety Q-values are commonly learned by separate critic ensembles, with uncertainty handled independently for each objective. This objective-wise treatment neglects inter-objective correlation and can lead to overly conservative value estimates, thereby reducing sample efficiency. To address this issue, we propose Cholesky-Ordered Projection Q-learning (COP-Q), a safety-first method that incorporates inter-objective covariance into vector-valued Q-value estimation. COP-Q constructs a generalized confidence bound in the joint Q-value space and uses Cholesky factorization to encode objective priority in a sequential form. This preserves conservatism on safety while adaptively reducing excessive conservatism on the reward objective. The resulting estimate is used in both temporal-difference target computation and actor optimization. COP-Q incurs minimal computational overhead and is readily compatible with most existing deep Q-learning frameworks. Experiments on robot locomotion in Brax and safe navigation in Safety-Gymnasium, covering both hard- and soft-safety settings, demonstrate that COP-Q achieves strong safety performance together with competitive or improved sample efficiency relative to representative baselines.

</details>

---

### [[20_Research/Papers/强化学习/Explainably_Safe_Reinforcement_Learning|Explainably Safe Reinforcement Learning]]

![[assets/2606.04634_first_page.png|800]]

- **arXiv**: [2606.04634](https://arxiv.org/abs/2606.04634)
- **PDF**: https://arxiv.org/pdf/2606.04634
- **详细分析**: [[20_Research/Papers/强化学习/Explainably_Safe_Reinforcement_Learning|Explainably Safe Reinforcement Learning]]
- **作者**: Sabine Rieder, Stefan Pranger, Debraj Chakraborty, Jan Křetínský, Bettina Könighofer
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.36）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《Explainably Safe Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Trust in a decision-making system requires both safety guarantees and the ability to interpret and understand its behavior. This is particularly important for learned systems, whose decision-making processes are often highly opaque. Shielding is a prominent model-based technique for enforcing safety in reinforcement learning. However, because shields are automatically synthesized using rigorous formal methods, their decisions are often similarly difficult for humans to interpret. Recently, decision trees became customary to represent controllers and policies. However, since shields are inherently non-deterministic, their decision tree representations become too large to be explainable in practice. To address this challenge, we propose a novel approach for explainable safe RL that enhances trust by providing human-interpretable explanations of the shield's decisions. Our method represents the shielding policy as a hierarchy of decision trees, offering top-down, case-based explanations. At design time, we use a world model to analyze the safety risks of executing actions in given states. Based on this analysis, we construct both the shield and a high-level decision tree that classifies states into risk categories (safe, critical, dangerous, unsafe), explaining why a situation may be safety-critical. At runtime, we generate localized decision trees that explain which actions are allowed and why others are deemed unsafe. Our method facilitates explainability of the safety aspect in safe-by-shielding reinforcement learning, requires no additional information beyond what is already used for shielding, incurs minimal overhead, and integrates readily into existing shielded RL pipelines. In our experiments, we compute explanations using decision trees that are several orders of magnitude smaller than the original shield.

</details>

---

### [[20_Research/Papers/强化学习/Dynamic_Multi-Pair_Trading_Strategy_in_Cryptocurrency_Markets_with_Deep_Reinforcement_Learning|Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning]]

![[assets/2606.04574_figure.png|800]]

- **arXiv**: [2606.04574](https://arxiv.org/abs/2606.04574)
- **PDF**: https://arxiv.org/pdf/2606.04574
- **详细分析**: [[20_Research/Papers/强化学习/Dynamic_Multi-Pair_Trading_Strategy_in_Cryptocurrency_Markets_with_Deep_Reinforcement_Learning|Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning]]
- **作者**: Damian Lebiedź, Robert Ślepaczuk
- **cs 子类**: cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.22（加权：大模型 0.1，强化学习 1.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Dynamic Multi-Pair Trading Strategy in Cryptocurrency Markets with Deep Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study aims to determine whether the application of Deep Reinforcement Learning (DRL) as a specialized execution overlay can enhance pair trading in highly volatile cryptocurrency markets. Although classical implementations of the strategy have proven successful in traditional equities, they frequently exhibit rigidity and suffer from severe divergence risks when applied to high-variance environments. To address this need, this research introduces novel concepts. To construct a robust system, we developed a hierarchical "Filter-then-Rank" pair selection methodology and a proprietary "Fixed Risk, Adaptive Mean" execution model. The system employs a Proximal Policy Optimization (PPO) agent with a Long Short-Term Memory (LSTM) layer to govern execution decisions within strict deterministic risk management boundaries. Evaluated on 1-hour interval data from the Binance USD-M Futures market, the optimized RL policy achieved an out-of-sample performance that substantially outperformed the heuristic baseline. A stationary circular block bootstrap robustness check confirms that the agent's risk-adjusted outperformance is statistically significant at the 10 percent level. Although falling marginally short of the stricter 5 percent threshold, this result highlights the extreme idiosyncratic variance characteristic of digital assets. Ultimately, this thesis contributes to the quantitative finance literature by introducing a hybrid architecture that combines statistical arbitrage with DRL execution policies. Furthermore, it delivers a novel framework for safe reinforcement learning via deterministic shielding, proving that anchoring a neural policy to statistically robust boundaries successfully mitigates severe divergence risks.

</details>

---

### [[20_Research/Papers/强化学习/Episodic_Memory_Temporal_Consistency_for_Cooperative_Multi-Agent_Reinforcement_Learning|Episodic Memory Temporal Consistency for Cooperative Multi-Agent Reinforcement Learning]]

![[assets/2606.04492_figure.png|800]]

- **arXiv**: [2606.04492](https://arxiv.org/abs/2606.04492)
- **PDF**: https://arxiv.org/pdf/2606.04492
- **详细分析**: [[20_Research/Papers/强化学习/Episodic_Memory_Temporal_Consistency_for_Cooperative_Multi-Agent_Reinforcement_Learning|Episodic Memory Temporal Consistency for Cooperative Multi-Agent Reinforcement Learning]]
- **作者**: Zicheng Zhao, Yu Lan, Chengzhengxu Li, Zhaohan Zhang, Xiaoming Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Episodic Memory Temporal Consistency for Cooperative Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative Multi-Agent Reinforcement Learning (MARL) frequently suffers from severe reward sparsity and exploration bottlenecks. While episodic memory mechanisms mitigate these issues by reusing high-return trajectories, they often trap agents in local optima due to unconstrained incentive distribution and semantic representation collapse. To address this, we propose Episodic Memory Temporal Consistency (EMTC), a framework that robustly constructs and selectively leverages historical experiences. EMTC introduces two synergistic components: (1) a Temporally Consistent Semantic Embedder that integrates contrastive learning with time-conditioned state reconstruction, preventing representation collapse and enabling precise memory retrieval; and (2) a Temporal Consistency Gating Mechanism that dynamically modulates episodic incentives based on temporal consistency error. This adaptive gate filters misleading signals from pseudo-successful trajectories, effectively mitigating Q-value overestimation. We provide theoretical guarantees, establishing a strict error bound that directly links the observable temporal consistency error to the underlying trajectory optimality and representation quality. Extensive evaluations on the SMAC and GRF benchmarks demonstrate that EMTC consistently outperforms state-of-the-art baselines. Notably, compared to the strongest episodic baseline, EMTC achieves absolute win-rate improvements of up to 24% in super-hard SMAC scenarios and an average improvement of 28% across GRF tasks.

</details>

---

### [[20_Research/Papers/强化学习/Policy_Gradient_for_Continuous-Time_Robust_Markov_Decision_Processes|Policy Gradient for Continuous-Time Robust Markov Decision Processes]]

![[assets/2606.04335_figure.png|800]]

- **arXiv**: [2606.04335](https://arxiv.org/abs/2606.04335)
- **PDF**: https://arxiv.org/pdf/2606.04335
- **详细分析**: [[20_Research/Papers/强化学习/Policy_Gradient_for_Continuous-Time_Robust_Markov_Decision_Processes|Policy Gradient for Continuous-Time Robust Markov Decision Processes]]
- **作者**: Tanya Veeravalli, David M. Bossens, Atsushi Nitanda
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Policy Gradient for Continuous-Time Robust Markov Decision Processes》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The framework of robust Markov decision processes (RMDPs) allows the design of reinforcement learning agents that satisfy performance guarantees under worst-case transition dynamics. Traditional RMDPs consider discrete-time dynamics and recently, sample-efficient policy gradient algorithms have been considered in this context. This paper investigates policy gradient algorithms within a continuous-time RMDP framework. Policy gradients and adversarial gradients are derived using pathwise and adjoint-based formulas for stochastic and ordinary differential equations. We propose double-loop optimisers to obtain linear convergence in the oracle-based setting and an $\tilde{\mathcal{O}}(\frac{1}{\epsilon^2})$ sample complexity in the sample-based setting in an analysis which also derives novel tools for the framework of undiscounted total cost MDPs. Additionally, we propose mean-field optimisers as distributional optimisers with an $\tilde{\mathcal{O}}(\frac{1}{K})$ oracle-based convergence rate and an $\tilde{\mathcal{O}}(\frac{N^2}{\epsilon})$ sample complexity under $N$-particle approximation. The effectiveness of continuous-time policy gradient algorithms is confirmed for both optimisers on continuous-time RMDPs with neural ordinary differential equation dynamics.

</details>

---

### [[20_Research/Papers/大模型/RL_Excursions_during_Pre-Training_Re-examining_Policy_Optimization_for_LLM_training|RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training]]

![[assets/2606.04272_figure.png|800]]

- **arXiv**: [2606.04272](https://arxiv.org/abs/2606.04272)
- **PDF**: https://arxiv.org/pdf/2606.04272
- **详细分析**: [[20_Research/Papers/大模型/RL_Excursions_during_Pre-Training_Re-examining_Policy_Optimization_for_LLM_training|RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training]]
- **作者**: Rachit Bansal, Clara Mohri, Tian Qin, David Alvarez-Melis, Sham Kakade
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《RL Excursions during Pre-Training: Re-examining Policy Optimization for LLM training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The standard LLM training pipeline applies reinforcement learning (RL) only after pre-training and supervised fine-tuning (SFT). We question this status quo by training a LLM from scratch and applying RL, SFT, and SFT followed by RL directly to intermediate pre-training checkpoints. We find that RL is effective very early, and often matches the full SFT$\to$RL pipeline early as well. Through experiments on harder problems, we find that targeted pre-training data composition is a strong lever for RL effectiveness, even more so than model scale. Beyond reasoning accuracy, applying RL directly to base checkpoints expands the model's distribution; the sharpening effect reported in recent work arises only when RL follows SFT. The general capabilities of the model remain essentially unchanged by RL, while they degrade following SFT. Finally, we merge RL and SFT objectives by parallel averaging, which outperforms across all other training methods discussed, across metrics, while preserving general capabilities. Together, these results suggest that LLM training might benefit from an expanded use of RL.

</details>

---

### [[20_Research/Papers/大模型/Self-Distilled_Policy_Gradient|Self-Distilled Policy Gradient]]

![[assets/2606.04036_figure.png|800]]

- **arXiv**: [2606.04036](https://arxiv.org/abs/2606.04036)
- **PDF**: https://arxiv.org/pdf/2606.04036
- **详细分析**: [[20_Research/Papers/大模型/Self-Distilled_Policy_Gradient|Self-Distilled Policy Gradient]]
- **作者**: Yifeng Liu, Shiyuan Zhang, Yifan Zhang, Quanquan Gu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Self-Distilled Policy Gradient》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-policy self-distillation, where a language model conditions on privileged context to supervise its own generations, is a promising source of dense supervision for sparse-reward reinforcement learning. Actually, it can be instantiated as an auxiliary full-vocabulary student-to-teacher reverse Kullback-Leibler divergence loss. We therefore propose SDPG, a self-distilled policy-gradient framework that combines group-relative verifier advantages with normalized standard deviation, exact full-vocabulary on-policy self-distillation, as well as reference-policy KL regularization. Empirically, SDPG improves stability and performance over RLVR and self-distillation baselines. The code is available at this https URL .

</details>

---
