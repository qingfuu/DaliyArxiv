# cs.LG | Machine Learning | 2026-08-05

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Robust_General_Utility_for_Reinforcement_Learning|Robust General Utility for Reinforcement Learning]]

![[assets/2608.03562_figure.png|800]]

- **arXiv**: [2608.03562](https://arxiv.org/abs/2608.03562)
- **PDF**: https://arxiv.org/pdf/2608.03562
- **详细分析**: [[20_Research/Papers/大模型/Robust_General_Utility_for_Reinforcement_Learning|Robust General Utility for Reinforcement Learning]]
- **作者**: Zixuan Liu, Fangzheng Wu, Brian Summa, Zizhan Zheng
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Robust General Utility for Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) with general utility extends classic RL by optimizing an arbitrary utility functional of the policy-induced occupancy measure, thereby enabling a broader range of applications. However, previous work on general utility RL typically assumes the evaluation utility is fixed and correctly specified. In practice, the utility used at deployment can deviate from the training one, creating a robustness gap that prior work does not address. Motivated by this, we propose robust general-utility RL, a minimax learning framework that trains policies against utility misspecification within a prescribed uncertainty set. Our framework strictly generalizes standard general-utility RL while also providing a unified view of many existing RL frameworks, including reward-robust RL and constrained RL, through appropriate choices of the utility uncertainty set. We further develop provably convergent stochastic algorithms for two regimes. For concave utilities, we develop a projected stochastic gradient descent-ascent method and establish stationarity guarantees. For the more challenging nonconcave regime, we propose a stochastic prox-extragradient algorithm that mitigates ill-posed behavior induced by nonconcavity, with convergence guarantees to approximate first-order stationarity. Experiments on LLM safety alignment and exploration maximization tasks further corroborate the convergence behavior consistent with our theory.

</details>

---

### [[20_Research/Papers/大模型/TimeRLM_Recursive_Language_Models_Enable_Precise_Anomaly_Localization_in_Long-Context_Time-Series|TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series]]

![[assets/2608.03391_figure.png|800]]

- **arXiv**: [2608.03391](https://arxiv.org/abs/2608.03391)
- **PDF**: https://arxiv.org/pdf/2608.03391
- **详细分析**: [[20_Research/Papers/大模型/TimeRLM_Recursive_Language_Models_Enable_Precise_Anomaly_Localization_in_Long-Context_Time-Series|TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series]]
- **作者**: Nicolas Zumarraga, Lorenzo Steno, Ning Wang, Max Rosenblattl, Thomas Kaar, Maxwell A. Xu, Kevin O'Sullivan, Markus Kreft, Elgar Fleisch, Paul Schmiedmayer, Patrick Langer, Robert Jakob
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TimeRLM: Recursive Language Models Enable Precise Anomaly Localization in Long-Context Time-Series》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARFBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precise anomaly localization over long-context time series is a crucial task in monitoring applications across clinical care, industrial operations, financial services, and logistics, where brief evidence may hide inside long spans of high-frequency data. Time-Series Language Models (TSLMs) are able to ingest time series data and verbalize findings on anomalies in natural language; however, recent benchmarks report a decrease in retrieval performance at long contexts, mirroring failure modes in text, vision, and audio. In the text domain, Recursive Language Models (RLMs) can recover much of this lost performance by keeping context external to the large language model (LLM), allowing the model to query it through code. We present TimeRLM, an RLM formulation for time-series that sequentially manipulates the signal using code and vision capabilities. We further introduce AnomalyXL, a synthetic long-context anomaly localization benchmark with programmatically injected anomalies that require precise retrieval. We implement five different task categories and two variants: AnomalyXL-MCQ and AnomalyXL-Localize. TimeRLM outperforms every evaluated TSLM and single-pass baseline on four of the five AnomalyXL-Localize tasks, reaching 0.682 IoU on localization and 0.745 on classify-with-evidence, versus at most 0.329 and 0.072 across all baselines. We post-train TimeRLM using reinforcement learning. The resulting model further improves performance and requires approximately one-third as many agent interaction turns as its untrained base model to produce a final answer. On unseen real-world ECG, sleep and software observability recordings, the post-trained TimeRLM retains or improves performance, surpassing TSLMs despite being trained exclusively on synthetic data. Our findings suggest recursive interaction with time-series is an effective approach for long-horizon retrieval.

</details>

---

### [[20_Research/Papers/强化学习/Revisiting_TD_Target_Aggregation_under_Uncertainty_in_Q-Learning|Revisiting TD Target Aggregation under Uncertainty in Q-Learning]]

![[assets/2608.03069_figure.png|800]]

- **arXiv**: [2608.03069](https://arxiv.org/abs/2608.03069)
- **PDF**: https://arxiv.org/pdf/2608.03069
- **详细分析**: [[20_Research/Papers/强化学习/Revisiting_TD_Target_Aggregation_under_Uncertainty_in_Q-Learning|Revisiting TD Target Aggregation under Uncertainty in Q-Learning]]
- **作者**: Lipeng Zu, Xiaonan Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 0.96，世界模型 0.36）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《Revisiting TD Target Aggregation under Uncertainty in Q-Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep Q-Networks (DQNs) learn value functions through bootstrapped temporal-difference updates, where future returns are approximated using a greedy maximization over next-state action values. While effective, this aggregation rule is inherently sensitive to estimation noise: when Q-values are uncertain, the maximization operator deterministically favors the largest estimate, regardless of its reliability, leading to amplified errors through bootstrapping. In this work, we propose the \textbf{S}uccessor Rollout \textbf{A}ggregation \textbf{D}eep \textbf{Q}-Network (SADQ), a simple modification to Q-learning that regularizes how the TD target is formed. SADQ uses one-step rollout predictions from a learned dynamics model to guide the comparison among candidate next-state actions, introducing additional structure into the aggregation step without altering the underlying learning framework. The resulting mixed Bellman update attenuates unreliable maxima while preserving the standard fixed point under diminishing model error. We provide theoretical analysis showing that SADQ reduces bootstrap-induced overestimation in a pointwise manner. Empirically, SADQ consistently improves training stability across classical control tasks, real-world vector-based environments, and Atari benchmarks when compared to strong DQN variants.

</details>

---
