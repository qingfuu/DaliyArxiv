# cs.LG | Machine Learning | 2026-07-20

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/PagedWeight_Efficient_MoE_LLM_Serving_with_Dynamic_Quality-Aware_Weight_Quantization|PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization]]

![[assets/2607.16184_figure.png|800]]

- **arXiv**: [2607.16184](https://arxiv.org/abs/2607.16184)
- **PDF**: https://arxiv.org/pdf/2607.16184
- **详细分析**: [[20_Research/Papers/大模型/PagedWeight_Efficient_MoE_LLM_Serving_with_Dynamic_Quality-Aware_Weight_Quantization|PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization]]
- **作者**: Yuchen Yang, Yifan Zhao, Anisha Dasgupta, Sasa Misailovic
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《PagedWeight: Efficient MoE LLM Serving with Dynamic Quality-Aware Weight Quantization》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mixture-of-Experts (MoE) is a popular class of large language models (LLMs), offering high efficiency and accuracy. However, in KV-cache-intensive serving scenarios, MoEs often exhibit a tension between the GPU memory requirements of the model weights and the growing KV cache. We propose PagedWeight, a novel management method for MoE LLM serving that dynamically quantizes MoE model's weights at runtime and balances expert-weight precision with the KV cache sizes. PagedWeight exposes and effectively navigates the complex tradeoff between the model's task accuracy, memory consumption, and throughput/latency. Across several memory-sensitive MoE serving scenarios, PagedWeight improves the quality-memory tradeoff over several existing quantization baselines. PagedWeight achieves FP16-equivalent accuracy with up to 72.0% GPU memory savings and 1.94$\times$ throughput improvement, and improves quality over quantization methods by up to 39.3% at a similar memory budget with at most 4.1% throughput loss.

</details>

---

### [[20_Research/Papers/具身智能/Physics-enhanced_reinforcement_learning_for_real-time_optimal_control_of_dynamical_systems|Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems]]

![[assets/2607.16177_figure.png|800]]

- **arXiv**: [2607.16177](https://arxiv.org/abs/2607.16177)
- **PDF**: https://arxiv.org/pdf/2607.16177
- **详细分析**: [[20_Research/Papers/具身智能/Physics-enhanced_reinforcement_learning_for_real-time_optimal_control_of_dynamical_systems|Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems]]
- **作者**: Matteo Tomasetto, Nicolò Botteghi, Gabriele Bruni, Andrea Manzoni
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Physics-enhanced reinforcement learning for real-time optimal control of dynamical systems》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MARL, MBRL, PEARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has recently emerged as a promising feedback control strategy for nonlinear and complex dynamical systems. However, RL algorithms are sample inefficient and require a large number of interaction with the environment to synthesize optimal control strategies. Consequently, applications of RL are typically limited to sparse sensors and actuators due to the curse of dimensionality entailed by the exploration-exploitation dilemma in high-dimensional spaces. In this work, we bridge RL and traditional optimal control for dynamical system with a novel Physics-EnhAnced Reinforcement Learning (PEARL) paradigm tailored to the control of high-dimensional and parametric dynamical systems, exploiting the differentibility of their dynamics. Specifically, PEARL employs an actor-adjoint algorithm that leverages automatic differentiation to compute policy gradients over short horizons and adjoint-based sensitivities of future returns approximated via neural networks, significantly reducing the number of environment interactions, while mitigating long-term gradient instabilities. Through two challenging parametric navigation problems in unsteady flows, we show that PEARL (i) effectively exploits differentiable environments to outperform state-of-the-art RL algorithms, (ii) is sample efficient, thanks to the physics-guided policy learning, (iii) generalizes across multiple scenarios, which is crucial when dealing with parametric systems, and (iv) enables scaling RL to high-dimensional state and action spaces, without requiring low-dimensional state representations or multi-agent strategies.

</details>

---

### [[20_Research/Papers/大模型/DELUGE_Towards_Continental-Scale_Daily_Pluvial_Flood_Damage_Prediction_via_Interpretable_Conditioning_on_Foundation_Model_Embeddings|DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings]]

![[assets/2607.16050_figure.png|800]]

- **arXiv**: [2607.16050](https://arxiv.org/abs/2607.16050)
- **PDF**: https://arxiv.org/pdf/2607.16050
- **详细分析**: [[20_Research/Papers/大模型/DELUGE_Towards_Continental-Scale_Daily_Pluvial_Flood_Damage_Prediction_via_Interpretable_Conditioning_on_Foundation_Model_Embeddings|DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings]]
- **作者**: Yuya Kawakami, Daniel Cayan, Dongyu Liu, Kwan-Liu Ma, Tom Corringham
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《DELUGE: Towards Continental-Scale Daily Pluvial Flood Damage Prediction via Interpretable Conditioning on Foundation Model Embeddings》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pluvial (rainfall-driven) flooding accounts for 45% of National Flood Insurance Program (NFIP) claims in the United States and is harder to predict than its riverine and coastal counterparts, with existing approaches limited to coarse resolution, regional domains, or computationally intensive process-based models unsuitable for daily continental-scale use. We present DELUGE, a multimodal deep learning framework for daily pluvial flood damage prediction at ~1 km resolution and national scale, trained on spatially and temporally corrected NFIP claims (2017-2022) and structured around the hazard, exposure, and vulnerability components of disaster risk. Rather than blanket coverage of the Conterminous United States (CONUS), we model the top 100 highest-claim 75 km cells, distributed nationwide and accounting for ~81% of total pluvial flood claims. Our architectural novelty is a pair of parametric modules in the hydrometeorology branch, a Value Modulator and a Temporal Modulator, conditioned on terrain descriptors and AlphaEarth foundation-model embeddings, that expose directly inspectable hydrological response parameters and provide architecture-level interpretability-by-design. Under a spatial block holdout, DELUGE outperforms tuned Random Forest, XGBoost, and LightGBM baselines by 9% to 30% on a dollar-weighted area under the precision-recall curve (PR-AUC), a metric that emphasizes the rare, high-cost claims of greatest operational interest. Beyond DELUGE, we argue this interpretable conditioning scheme is a transferable pattern for integrating foundation-model embeddings into other geospatial prediction tasks.

</details>

---

### [[20_Research/Papers/强化学习/CLaC@FinMMEval_2026_Task_3_Sentiment-Augmented_Deep_Reinforcement_Learning_for_Active_Trading_--_An_Alpha-Reward_Approach|CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach]]

![[assets/2607.16028_figure.png|800]]

- **arXiv**: [2607.16028](https://arxiv.org/abs/2607.16028)
- **PDF**: https://arxiv.org/pdf/2607.16028
- **详细分析**: [[20_Research/Papers/强化学习/CLaC@FinMMEval_2026_Task_3_Sentiment-Augmented_Deep_Reinforcement_Learning_for_Active_Trading_--_An_Alpha-Reward_Approach|CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach]]
- **作者**: Andrei Neagu, Eeham Khan, Leila Kosseim
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.62（加权：大模型 0.1，强化学习 2.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《CLaC@FinMMEval 2026 Task 3: Sentiment-Augmented Deep Reinforcement Learning for Active Trading -- An Alpha-Reward Approach》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, FinMMEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents our system for Task 3 of the CLEF 2026 FinMMEval Lab, which requires daily long, flat, or short trading decisions for Bitcoin (BTC) and Tesla (TSLA) using news and historical market data. We formulate the problem as a discrete-action Markov Decision Process and compare four deep reinforcement learning algorithms: Policy Gradient (PG), Proximal Policy Optimization (PPO), Deep Q-Learning (DQL), and Deep Deterministic Policy Gradient (DDPG). The agents use technical indicators, cyclical calendar encodings, and daily news sentiment scores produced by LLaMA 3.2 1B. To reduce overfitting and align training with the objective of outperforming buy-and-hold, we introduce an alpha reward based on excess market return and randomize episode start dates. Hyperparameters are optimized with Ray Tune over 180 trials per algorithm-asset pair, with early stopping and model selection based on validation Sharpe ratio. On the CLEF Task 3 test set, DDPG achieves the strongest overall performance. DQL was selected a priori for the live endpoint because it obtained the highest validation Sharpe ratio, with selection performed without access to the test period. For TSLA, DDPG and DQL achieve cumulative returns of 54.96% and 52.62%, respectively, compared with 16.45% for buy-and-hold. For BTC, DDPG achieves a positive return of 1.58% while buy-and-hold declines by -34.27%. The results also reveal a substantial validation-to-test generalization gap, highlighting the difficulty of transferring policies selected in bull-market conditions to a bear-market regime.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Reach-Avoid_Task_with_Reinforcement_Learning_Vectorized_Simulation_and_Benchmark|Learning Reach-Avoid Task with Reinforcement Learning: Vectorized Simulation and Benchmark]]

![[assets/2607.15935_figure.png|800]]

- **arXiv**: [2607.15935](https://arxiv.org/abs/2607.15935)
- **PDF**: https://arxiv.org/pdf/2607.15935
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Reach-Avoid_Task_with_Reinforcement_Learning_Vectorized_Simulation_and_Benchmark|Learning Reach-Avoid Task with Reinforcement Learning: Vectorized Simulation and Benchmark]]
- **作者**: Jonas Weihing, Shahram Eivazi
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.42（加权：具身智能 0.3，大模型 0.1，强化学习 1.16，世界模型 0.16，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Learning Reach-Avoid Task with Reinforcement Learning: Vectorized Simulation and Benchmark》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, Panda-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) has a longstanding tradition in addressing the reach-avoid task problem, especially for controlling robotic arms. While this task serves as a baseline environment within the research community, the ability of DRL to effectively learn the each-avoid task in complex and realistic scenarios beyond simplified and restricted tabletop settings remains uncertain. In this paper, we present, for the first time, a comprehensive benchmark for the reachavoid task that accurately captures real-world complexities without simplifications. We demonstrate a diverse range of settings for robotic arm reach-avoid task, which can be used for evaluating DRL research. We achieved this by utilizing the MuJoCo MJX physics engine and parallelizing both the simulation environment and DRL algorithms using the Brax library. We achieved state-of-the-art results with success rates of 96.1% (UR5e) and 98.8% (Franka Emika Robot) for the reach task and 86.8% (UR5e) and 95.2% (Franka) for the static reachavoid task. Our results indicate that while in previous works DRL agents could solve, for example, a reach task in a simplified setting perfectly, their agents performance collapses when evaluated in realistic scenarios. Overall, this work identifies that additional research is still required to claim the successful resolution of the robotic arm reach-avoid task using DRL. The environment and benchmarking code is available as open source at the following link

</details>

---

### [[20_Research/Papers/大模型/ContinuityBench_A_Benchmark_and_Systems_Study_of_Stateful_Failover_in_Multi-Provider_LLM_Routing|ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing]]

![[assets/2607.15899_figure.png|800]]

- **arXiv**: [2607.15899](https://arxiv.org/abs/2607.15899)
- **PDF**: https://arxiv.org/pdf/2607.15899
- **详细分析**: [[20_Research/Papers/大模型/ContinuityBench_A_Benchmark_and_Systems_Study_of_Stateful_Failover_in_Multi-Provider_LLM_Routing|ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing]]
- **作者**: Vishal Pandey, Gopal Singh
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《ContinuityBench: A Benchmark and Systems Study of Stateful Failover in Multi-Provider LLM Routing》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AlpacaEval, ContinuityBench, HaluEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In production large language model (LLM) deployments, high API availability guarantees do not equate to conversational continuity. When a primary provider experiences an outage or strict rate-limiting, naive stateless failover mechanisms successfully maintain uptime but silently discard conversation history, severely disrupting the user experience. To rigorously quantify and resolve this failure mode, we introduce two novel metrics: Continuity Preservation Rate (CPR) and Continuity Latency Overhead (CLO). We propose a stateful, multi-provider proxy architecture utilizing a History-Forwarding strategy to seamlessly reconstruct conversational state across heterogeneous LLM endpoints during failover events. Furthermore, we release continuity-bench, https://github.com/Vishal-sys-code/continuity-bench, an open evaluation harness designed to stress-test context preservation under high-concurrency provider failure conditions. Our empirical evaluation ($N=750$ failover events) demonstrates that our stateful proxy achieves a 99.20\% CPR [95\% CI: 98.27\%, 99.63\%], cleanly transferring deep conversational context to fallback providers, compared to a near-0\% preservation rate for standard stateless architectures. Finally, we characterize failover latency distributions, identifying the critical necessity of asynchronous exponential backoff with jitter to prevent cascading retry storms against strict-limit fallback APIs. Our results provide a principled foundation for building robust, state-preserving multi-model inference systems.

</details>

---

### [[20_Research/Papers/具身智能/Dynamics-Aware_Meta-Imitation_for_Generalization_to_Unseen_Robotic_Manipulation|Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation]]

![[assets/2607.15880_figure.png|800]]

- **arXiv**: [2607.15880](https://arxiv.org/abs/2607.15880)
- **PDF**: https://arxiv.org/pdf/2607.15880
- **详细分析**: [[20_Research/Papers/具身智能/Dynamics-Aware_Meta-Imitation_for_Generalization_to_Unseen_Robotic_Manipulation|Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation]]
- **作者**: Zhenduo Shang, Xiyao Liu, Bohan Li, Xudong Wang, Teng Ren, Lianqing Liu, Zhi Han
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.2，大模型 0.2，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Dynamics-Aware Meta-Imitation for Generalization to Unseen Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-World, RLBench, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation Learning aims to learn skills from extensive observations and demonstrations for robots, so it suffers from data scarcity and environment generalization. The existing methods predominantly focus on imitation from in-domain tasks and consequently struggle with generalization to unseen tasks. To bridge this generalization gap, we propose the \textbf{D}ynamics-\textbf{A}ware \textbf{M}eta-\textbf{I}mitation (DAMI) framework. By integrating meta-learning to construct a shared skill space, DAMI equips agents for rapid adaptation to novel tasks. We introduce the Visual-Motor Trajectory (VMT) module to capture complex spatio-temporal dynamics within the task latent space. Furthermore, we propose the Unpaired Unified Task (U2T) block to fuse unstructured multimodal observations. To coordinate these representations, we integrate a Task-Conditioned Feature Modulation (TCFM) mechanism customized for modulating low-level 3D features. By capturing intrinsic dynamics from a random complete reference demonstration, our framework learns the underlying task logic rather than memorizing static cues, ensuring effective generalization. Extensive experiments in both simulation and real-world settings demonstrate that our approach outperforms state-of-the-art baselines regarding direct inference on seen tasks and adaptation to unseen tasks via few-shot fine-tuning.

</details>

---

### [[20_Research/Papers/大模型/QUADS_Stabilizing_NVFP4_Reinforcement_Learning_for_MoE_via_QUantization-error_Alignment_across_Dual_Sides|QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides]]

![[assets/2607.15810_figure.png|800]]

- **arXiv**: [2607.15810](https://arxiv.org/abs/2607.15810)
- **PDF**: https://arxiv.org/pdf/2607.15810
- **详细分析**: [[20_Research/Papers/大模型/QUADS_Stabilizing_NVFP4_Reinforcement_Learning_for_MoE_via_QUantization-error_Alignment_across_Dual_Sides|QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides]]
- **作者**: Zhengyang Zhuge, Hao Yu, Xin Wang, Zheng Li, Yizhong Cao, Dayiheng Liu, Jianwei Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《QUADS: Stabilizing NVFP4 Reinforcement Learning for MoE via QUantization-error Alignment across Dual Sides》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：QeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rollout generation is a major bottleneck in Reinforcement Learning (RL) for Mixture-of-Experts (MoE) Large Language Models, motivating low-precision rollout acceleration such as FP8. As an emerging low-precision format, NVFP4 combines fine-grained scaling for accuracy preservation with native W4A4 FP4 GEMMs for higher throughput than FP8. However, we find that directly applying NVFP4 to MoE RL rollout is impractical. NVFP4 rollout with BF16 training collapses after roughly 150 steps, accompanied by rapidly growing rollout-trainer log-probability gaps. Through training-inference error analysis and controlled ablations, we identify activation error, rather than weight error, as the dominant source of FP4 RL instability: weights can be synchronized and aligned by a shared quantization-dequantization path, whereas activations are recomputed online and error is amplified by the coarse E2M1 grid. Therefore, to stabilize NVFP4 RL for MoE, we propose QUantization-error Alignment across Dual Sides (QUADS). On the trainer side, we introduce Asymmetric Quantization-Aware Training fake-quantizing weights while keeping activations unquantized for better alignment. On the rollout side, Residual Activation Compensation corrects high-error activation channels while preserving native W4A4 GEMMs. In our MoE RL experiments on several benchmarks, QUADS achieves BF16-level accuracy, improves average pass@1 by 21.49 points over naive NVFP4 RL, and delivers ~16% higher rollout throughput than FP8.

</details>

---

### [[20_Research/Papers/强化学习/Robust_Peak-cost_Constrained_Reinforcement_Learning|Robust Peak-cost Constrained Reinforcement Learning]]

![[assets/2607.15457_figure.png|800]]

- **arXiv**: [2607.15457](https://arxiv.org/abs/2607.15457)
- **PDF**: https://arxiv.org/pdf/2607.15457
- **详细分析**: [[20_Research/Papers/强化学习/Robust_Peak-cost_Constrained_Reinforcement_Learning|Robust Peak-cost Constrained Reinforcement Learning]]
- **作者**: Shilpa Mukhopadhyay, Sourav Ganguly, Santosh Mohan Rajkumar, Honghao Wei, Debdipta Goswami, Arnob Ghosh
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Robust Peak-cost Constrained Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CRL, RCRL, RP-CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study robust peak-cost constrained reinforcement learning (RP-CRL), where the objective is to maximize expected reward while controlling the maximum cost encountered along a trajectory. This setting is motivated by safety-critical applications in which a single large violation can be catastrophic and therefore cannot be adequately captured by the standard CMDP framework based on expected cumulative cost. Existing reachability-constrained RL methods adopt Lagrangian-based approaches, yet the underlying duality properties of peak-cost constrained MDPs remain unclear. We show that, unlike standard CMDPs, peak-cost constrained MDPs may not admit zero duality gap. We further consider a robust formulation to address simulator-to-real-world mismatch in the transition dynamics. To solve this problem, we develop a surrogate optimization framework and a robust value estimation method based on integral probability metrics. We prove that, with appropriate hyperparameter choices, the surrogate solution attains the same robust reward value as the original problem while violating the constraint by at most epsilon. Experiments show that the proposed method effectively enforces safety under dynamics perturbations while retaining strong reward performance.

</details>

---

### [[20_Research/Papers/强化学习/Proactive_Inpatient_Bed_Requests_for_Emergency_Department_Admissions|Proactive Inpatient Bed Requests for Emergency Department Admissions]]

![[assets/2607.15432_figure.png|800]]

- **arXiv**: [2607.15432](https://arxiv.org/abs/2607.15432)
- **PDF**: https://arxiv.org/pdf/2607.15432
- **详细分析**: [[20_Research/Papers/强化学习/Proactive_Inpatient_Bed_Requests_for_Emergency_Department_Admissions|Proactive Inpatient Bed Requests for Emergency Department Admissions]]
- **作者**: QIan Cheng, Nilay Tanik Argon, Aniruddhan Ganesaraman, Serhan Ziya
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Proactive Inpatient Bed Requests for Emergency Department Admissions》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Emergency department (ED) boarding occurs when admitted patients remain in the ED while awaiting inpatient beds. Boarding is a major driver of ED crowding and has been associated with poor patient outcomes. We propose a framework to help EDs reduce boarding time and length of stay by using information about current patients and bed availability to proactively request inpatient beds before admission decisions are finalized. We formulate the problem as a Markov decision process in which predictions of each patient's admission probability and time to disposition are aggregated to guide early inpatient bed requests. This formulation leads to three data-driven policies based on approximate dynamic programming, reinforcement learning, and a newsvendor-type approach. Using a simulation model based on data from a large ED, we evaluate these policies across a wide range of settings. The simulation study shows that proactive aggregate bed requests can reduce average boarding times for admitted patients by 30-70\% and average length of stay for all ED patients by 6-15\%, while creating only modest idle time for prepared inpatient beds. The newsvendor heuristic provides the most attractive tradeoff between ED performance and inpatient bed idle time, whereas the reinforcement learning heuristic produces smoother bed-request patterns when stability in downstream hospital processes is especially important. Our work shows how EDs can use prediction tools to make proactive bed-request decisions that improve ED operations while helping managers balance reductions in ED delays against inpatient bed idle time. Our findings also illustrate the value of evaluating both simple myopic heuristics and more sophisticated reinforcement learning-based approaches, since each can offer distinct advantages depending on the performance measures and implementation constraints most important to managers.

</details>

---
