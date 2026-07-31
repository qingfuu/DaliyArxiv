# cs.LG | Machine Learning | 2026-07-29

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/强化学习/Reinformed_Dreamer_An_Asymmetric_World_Model_Efficiently_Trained_through_Latent_Guidance|Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance]]

![[assets/2607.26040_first_page.png|800]]

- **arXiv**: [2607.26040](https://arxiv.org/abs/2607.26040)
- **PDF**: https://arxiv.org/pdf/2607.26040
- **详细分析**: [[20_Research/Papers/强化学习/Reinformed_Dreamer_An_Asymmetric_World_Model_Efficiently_Trained_through_Latent_Guidance|Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance]]
- **作者**: Gaspard Lambrechts, Adrien Bolland, Daniel Ebi, Damien Ernst
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 2.12（加权：强化学习 0.36，世界模型 1.76）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Reinformed Dreamer: An Asymmetric World Model Efficiently Trained through Latent Guidance》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Much like humans benefit from guidance while learning, reinforcement learning algorithms may benefit from additional supervision beyond rewards. Leveraging additional information during training to learn better representations and behaviors has been the focus of asymmetric reinforcement learning. This learning paradigm has proven effective under partial observability when additional state information is available, but also under full observability when more refined state information is available. Focusing on model-based reinforcement learning, we study the effect of asymmetric learning on observation representations and on privileged information representations. First, we identify a limitation in the privileged information representations learned by an asymmetric model-based algorithm known as the Informed Dreamer. Then, we propose a novel asymmetric representation learning objective using latent guidance, resulting in a new algorithm called the Reinformed Dreamer. Experiments across several benchmarks show a more consistent improvement over Dreamer than previous asymmetric approaches.

</details>

---

### [[20_Research/Papers/强化学习/Physics-Aware_End-to-End_Deep_Reinforcement_Learning_for_Quadcopter_Control_with_Actuator_Dynamics|Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics]]

![[assets/2607.25985_first_page.png|800]]

- **arXiv**: [2607.25985](https://arxiv.org/abs/2607.25985)
- **PDF**: https://arxiv.org/pdf/2607.25985
- **详细分析**: [[20_Research/Papers/强化学习/Physics-Aware_End-to-End_Deep_Reinforcement_Learning_for_Quadcopter_Control_with_Actuator_Dynamics|Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics]]
- **作者**: Ya-Chia Shen, Woei-Leong Chan
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Physics-Aware End-to-End Deep Reinforcement Learning for Quadcopter Control with Actuator Dynamics》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicles (UAVs), particularly quadcopters, present unique challenges for autonomous control due to their underactuated dynamics: only four available control inputs must govern six degrees of freedom. This paper investigates a physics-aware, end-to-end deep reinforcement learning (DRL) approach that acts directly on low-level body inputs, total thrust and body torques $(T, τ_x, τ_y, τ_z)$, and closes the loop through a high-fidelity Simulink environment. Our simulator integrates a 12-state rigid-body model (MATLAB Level-2 S-Function) with (i) an Action2RPM allocation based on the Moore-Penrose pseudo-inverse of a coefficient matrix derived from thrust and drag terms, and (ii) first-order actuator dynamics for each motor (time constant $T_m = 0.076$ s), including rotor gyroscopic coupling. A shaped reward balances goal-reaching and stability using an exponential position well, attitude penalties, and quadratic velocity costs. Four DRL algorithms, DDPG, TD3, PPO, and SAC, are evaluated in two stages: (S1) thrust-only hover and (S2) hover with pitch torque and a translated goal. Results show that SAC and TD3 achieve superior stability and exploration efficiency, while PPO is less sample-efficient. The study highlights the significance of modeling actuator lags and aerodynamic moments for stable low-level control and provides a reproducible benchmark for quadcopter DRL.

</details>

---

### [[20_Research/Papers/强化学习/Learning_from_the_Unseen_Offline_Reinforcement_Learning_with_Hidden_Actions|Learning from the Unseen: Offline Reinforcement Learning with Hidden Actions]]

![[assets/2607.25241_figure.png|800]]

- **arXiv**: [2607.25241](https://arxiv.org/abs/2607.25241)
- **PDF**: https://arxiv.org/pdf/2607.25241
- **详细分析**: [[20_Research/Papers/强化学习/Learning_from_the_Unseen_Offline_Reinforcement_Learning_with_Hidden_Actions|Learning from the Unseen: Offline Reinforcement Learning with Hidden Actions]]
- **作者**: Zeyu Bian, Ying Zhou, Yifan Cui
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Learning from the Unseen: Offline Reinforcement Learning with Hidden Actions》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Standard offline reinforcement learning (RL) algorithms typically assume that the actions in the dataset are observed without error. However, in many real-world applications, the true actions are unobserved and only noisy proxies are available, causing existing RL methods to yield biased and potentially misleading conclusions. We study off-policy evaluation in infinite-horizon discounted Markov decision processes with hidden actions. By leveraging the next-state variable as a natural proxy for the unobserved action, we establish identification of the policy value and propose an influence-function-based estimator called LURE (Learning from the Unseen: Robust Estimator). LURE is multiply robust, remaining consistent under several combinations of correctly specified nuisance components, and is asymptotically normal, enabling valid statistical inference. To our knowledge, this is the first work to address offline RL with hidden actions. We demonstrate LURE's effectiveness through simulations and a sepsis management application using the MIMIC-III database.

</details>

---

### [[20_Research/Papers/强化学习/A_Unified_Algorithmic_Framework_for_Hybrid_Reinforcement_Learning_in_Tabular_MDPs_with_Shifted_Transition_Dynamics|A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics]]

![[assets/2607.25207_figure.png|800]]

- **arXiv**: [2607.25207](https://arxiv.org/abs/2607.25207)
- **PDF**: https://arxiv.org/pdf/2607.25207
- **详细分析**: [[20_Research/Papers/强化学习/A_Unified_Algorithmic_Framework_for_Hybrid_Reinforcement_Learning_in_Tabular_MDPs_with_Shifted_Transition_Dynamics|A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics]]
- **作者**: Zheshun Wu, Renjie Zheng, Jinhang Zuo, Zenglin Xu, Fang Kong
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《A Unified Algorithmic Framework for Hybrid Reinforcement Learning in Tabular MDPs with Shifted Transition Dynamics》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HySRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper investigates a hybrid reinforcement learning setting in tabular Markov Decision Processes (MDPs), where an agent aims to learn an optimal policy by combining online interactions with a target environment and offline data from a source environment. A central challenge is that offline data may be collected from outdated environments with shifted transition dynamics, making naive integration of historical data ineffective. To address this, we propose a unified algorithmic framework featuring two algorithms: MIN-UCB-VI for regret minimization and MAX-LCB-VI for best policy identification. Both algorithms leverage fine-grained bias information to more effectively exploit offline data under general transition shifts. We provide theoretical guarantees for our framework, including both instance-dependent and independent upper bounds on regret and sub-optimality gap. Furthermore, we establish matching lower bounds to demonstrate the optimality of our approach and validate our theoretical findings through extensive experiments.

</details>

---

### [[20_Research/Papers/强化学习/Endpoint_Replay_Compressing_the_Recency_Buffer_in_Deep_Reinforcement_Learning|Endpoint Replay: Compressing the Recency Buffer in Deep Reinforcement Learning]]

![[assets/2607.25123_figure.png|800]]

- **arXiv**: [2607.25123](https://arxiv.org/abs/2607.25123)
- **PDF**: https://arxiv.org/pdf/2607.25123
- **详细分析**: [[20_Research/Papers/强化学习/Endpoint_Replay_Compressing_the_Recency_Buffer_in_Deep_Reinforcement_Learning|Endpoint Replay: Compressing the Recency Buffer in Deep Reinforcement Learning]]
- **作者**: Parham Mohammad Panahi, Armin Ashrafi, Haoyu Du, Andrew Patterson, Martha White, Adam White
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Endpoint Replay: Compressing the Recency Buffer in Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Experience replay remains one of the most practical and useful algorithmic tools in the deep reinforcement learning (DRL) toolbox. Aside from the limited success of prioritized replay and specialized approaches for large asynchronous systems, most DRL algorithms make use of a large, uniformly sampled recency buffer---even the size, one million, remains unchanged. Could we store less data, reduce redundancy, or more effectively chain experience together to speed up value propagation and still retain the performance of large buffers? In this paper, we investigate a simple compression approach that stores representative transitions derived from the end-points of a chain of connected $n$-step sequences. By curating these end-points in a smaller recency buffer, our method maintains an effective memory horizon comparable to a standard large buffer while requiring an order of magnitude less storage. Through empirical evaluation, we demonstrate that this approach prevents the systematic bias inherent in naive compression strategies and matches the performance of traditional large buffers in the Pinball environment and the Atari 2600 benchmark.

</details>

---

### [[20_Research/Papers/大模型/Inverse_RL_Helps_Align_AI_by_Imitating_Humans|Inverse RL Helps Align AI by Imitating Humans]]

![[assets/2607.24900_first_page.png|800]]

- **arXiv**: [2607.24900](https://arxiv.org/abs/2607.24900)
- **PDF**: https://arxiv.org/pdf/2607.24900
- **详细分析**: [[20_Research/Papers/大模型/Inverse_RL_Helps_Align_AI_by_Imitating_Humans|Inverse RL Helps Align AI by Imitating Humans]]
- **作者**: Michał Wiliński, Liu Leqi, Chirag Nagpal
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.82（加权：大模型 0.1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Inverse RL Helps Align AI by Imitating Humans》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language model alignment aims to make model behavior reliably reflect desirable properties such as helpfulness, safety, and instruction following. Current approaches typically use supervised fine-tuning on demonstrations or reinforcement learning with rewards derived from verifiers or human feedback. These paradigms leave an important question underexplored: can demonstrations alone yield an implicit reward that can be inspected, reused, and optimized on-policy to align AI? Motivated by inverse reinforcement learning, we introduce Projected Alignment Reward Estimated from Demonstrations (PARED). PARED recovers the implicit reward underlying expert demonstrations as an explicit function over a small set of response-level features, learned by a lightweight discriminator that separates demonstrations from the policy's own samples in this feature space. Unlike a standard reward model, PARED requires no task-specific preference annotations: demonstrations provide the task-specific supervision, which can be augmented with AI feedback as additional dimensions of supervision. Through experiments involving inference-time reranking and adversarial on-policy RL, we show that the recovered reward improves a base policy without a supervised loss and yields further gains when optimized after standard supervised fine-tuning. Additionally, we demonstrate that PARED can be used for contextual alignment, in which a single policy can be tailored to the preferences of different audiences.

</details>

---

### [[20_Research/Papers/大模型/FinAbstain_Uncertainty-Calibrated_Multimodal_RAG_for_Selective_Financial_Forecasting|FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting]]

![[assets/2607.24875_first_page.png|800]]

- **arXiv**: [2607.24875](https://arxiv.org/abs/2607.24875)
- **PDF**: https://arxiv.org/pdf/2607.24875
- **详细分析**: [[20_Research/Papers/大模型/FinAbstain_Uncertainty-Calibrated_Multimodal_RAG_for_Selective_Financial_Forecasting|FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting]]
- **作者**: Dorothy Torres, Wei Cheng, Henan Huang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《FinAbstain: Uncertainty-Calibrated Multimodal RAG for Selective Financial Forecasting》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FinQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) can synthesize financial narratives but may express high confidence when evidence is sparse, stale, or contradictory. This failure is especially consequential in forecasting, where filings, news, prices, volume, and technical signals can disagree. We present FinAbstain, a research framework for uncertainty-calibrated multimodal retrieval-augmented generation (RAG) with selective prediction. A point-in-time retriever admits only information public at the forecast timestamp and supplies modality-specific evidence to fundamental, news, technical, risk, and verification agents. Their probabilistic assessments are aggregated with retrieval relevance, evidence contradiction, repeated-sample consistency, and historical calibration statistics. Temperature scaling, isotonic regression, conformal prediction, and a proposed hybrid uncertainty score are evaluated under a common chronological protocol. A controller predicts bullish, bearish, or neutral outcomes only when uncertainty is below a validated threshold; otherwise it abstains, requests evidence, reduces exposure, or routes the case to human review. The evaluation covers one- and five-day abnormal-return direction, twenty-day volatility intervals, and abstention decisions, using accuracy, calibration, risk--coverage, citation, trading, latency, and cost metrics. To make the design auditable before a full data collection is complete, we report explicitly labeled simulated results rather than empirical claims. These results illustrate the intended hypothesis: calibrated abstention may trade coverage for lower selective error and drawdown. The contribution is a time-safe architecture, a composite uncertainty formulation, and a reproducible evaluation blueprint for evidence-grounded selective financial forecasting.

</details>

---
