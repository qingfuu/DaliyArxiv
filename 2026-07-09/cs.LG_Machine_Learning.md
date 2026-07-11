# cs.LG | Machine Learning | 2026-07-09

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Safe_Reinforcement_Learning_using_Ideas_from_Model_Predictive_Control|Safe Reinforcement Learning using Ideas from Model Predictive Control]]

![[assets/2607.07252_figure.png|800]]

- **arXiv**: [2607.07252](https://arxiv.org/abs/2607.07252)
- **PDF**: https://arxiv.org/pdf/2607.07252
- **详细分析**: [[20_Research/Papers/强化学习/Safe_Reinforcement_Learning_using_Ideas_from_Model_Predictive_Control|Safe Reinforcement Learning using Ideas from Model Predictive Control]]
- **作者**: Georg Schäfer, Jakob Rehrl, Stefan Huber, Simon Hirlaender
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.22（加权：具身智能 0.3，大模型 0.1，强化学习 1.16，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Safe Reinforcement Learning using Ideas from Model Predictive Control》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) enables the synthesis of control policies directly from data, making it highly appealing for complex cyber-physical systems (CPSs) and robotics. A persistent challenge, however, is ensuring strict, hard safety constraints during the active learning phase. In real-world physical systems, violating mechanical limits can cause irreversible damage, necessitating that exploration remains strictly within safe operational regions. We propose a generalized framework that combines the adaptive, high-performance nature of deep reinforcement learning (DRL) with the formal safety guarantees of model predictive control (MPC). Using a mathematical model of the system dynamics, offline MPC computations define a feasible state-action space, representing all safe combinations of system states and control inputs that guarantee constraint satisfaction. During training and deployment, the RL agent's instantaneous actions are projected onto this globally verified feasible set via a safety filter. We systematically evaluate our generalized approach on a non-linear 1-DoF laboratory testbed, demonstrating successful exploration and stable policy convergence on physical hardware.

</details>

---

### [[20_Research/Papers/大模型/A_knowledge-augmented_dataset_of_high-risk_driving_scenarios_with_LLM_annotations_for_autonomous_driving|A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving]]

![[assets/2607.07103_figure.png|800]]

- **arXiv**: [2607.07103](https://arxiv.org/abs/2607.07103)
- **PDF**: https://arxiv.org/pdf/2607.07103
- **详细分析**: [[20_Research/Papers/大模型/A_knowledge-augmented_dataset_of_high-risk_driving_scenarios_with_LLM_annotations_for_autonomous_driving|A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving]]
- **作者**: Heye Huang, Jingguang Li, Zhiyuan Zhou, Paul Liang, Mingyu Wu, Kitae Jang, Jianqiang Wang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《A knowledge-augmented dataset of high-risk driving scenarios with LLM annotations for autonomous driving》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CitySim, CoVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe autonomous driving requires both rapid responses to common high-risk events and deeper reasoning over rare, extreme long-tail scenarios in traffic safety. These scenarios are severely under-represented in naturalistic driving data, and existing trajectory and language-augmented datasets seldom provide high-risk event labels, semantic annotations, and verifiable safety signals. Here we present K-Risk, a knowledge-augmented dataset that combines structured driving trajectories with large language model generated semantic annotations for safety-critical driving scenarios. K-Risk integrates 20 human-driven and autonomous-vehicle trajectory datasets from Europe, China, and the United States, covering highways, urban freeways, intersections, and roundabouts. Using a unified risk-centric extraction pipeline, K-Risk curates 31,398 high-risk events, together with a 1,036-event extreme subset of near-collision cases. Each event is released as a synchronized trajectory, metadata, and language triplet containing structured scenario descriptions, abnormal-behavior notifications, and, for a representative subset, causal risk analyses and action recommendations validated through a closed-loop simulator with iterative reflection. By combining multi-dimensional risk annotations, interpretable language supervision, and verifiable decisions, K-Risk bridges structured traffic trajectories, semantic reasoning, and decision supervision, providing a standardized foundation for developing and evaluating next-generation risk-aware autonomous driving agents.

</details>

---

### [[20_Research/Papers/强化学习/Online_Data_Selection_Is_Implicit_Alignment|Online Data Selection Is Implicit Alignment]]

![[assets/2607.07023_figure.png|800]]

- **arXiv**: [2607.07023](https://arxiv.org/abs/2607.07023)
- **PDF**: https://arxiv.org/pdf/2607.07023
- **详细分析**: [[20_Research/Papers/强化学习/Online_Data_Selection_Is_Implicit_Alignment|Online Data Selection Is Implicit Alignment]]
- **作者**: Aoxiong Zeng, Yuxin Yang, Xiangquan Yang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Online Data Selection Is Implicit Alignment》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Supervised fine-tuning (SFT) is often treated as a capability-adaptation step, while alignment is attributed to later preference optimization or reinforcement learning. This separation is incomplete: when examples are scored and kept online during fine-tuning, the choice of which data to train on already changes the model's behavioral preferences. We study online data selection as an implicit alignment mechanism. Given the same base model, optimizer, and selected-token budget, we compare random, loss-based, quality-based, and diversity-based online selectors and measure the behavioral drift they induce without any preference optimization. The proposed evaluation tracks helpfulness, refusal rate, verbosity, truthfulness, sycophancy, calibration, and jailbreak robustness, together with diagnostics for which behavioral modes are over-represented in the selected data. We formalize online selection as a reweighted SFT objective whose weights define an implicit preference over response styles and safety postures, so that an online scorer plays the role usually assigned to a reward model. This view predicts that high-scoring data can systematically favor longer, more assertive, more compliant, or more refusal-prone behaviors depending on how the online score is defined. Empirically, selectors that are statistically indistinguishable in task accuracy diverge sharply in refusal rate, verbosity, and sycophancy, and we show that the direction of the shift is predictable from the attribute mixture of the selected data. We introduce Alignment Drift Auditing (ADA), a controlled protocol for quantifying selection-induced behavioral movement, and Alignment-Aware Selection (AAS), a diagnostic online selector that retains data efficiency while constraining drift along safety and style axes.

</details>

---

### [[20_Research/Papers/大模型/UP_Unbounded_Positive_Asymmetric_Optimization_for_Breaking_the_Exploration-Stability_Dilemma|UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma]]

![[assets/2607.06987_first_page.png|800]]

- **arXiv**: [2607.06987](https://arxiv.org/abs/2607.06987)
- **PDF**: https://arxiv.org/pdf/2607.06987
- **详细分析**: [[20_Research/Papers/大模型/UP_Unbounded_Positive_Asymmetric_Optimization_for_Breaking_the_Exploration-Stability_Dilemma|UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma]]
- **作者**: Chongyu Fan, Pengfei Liu, Jingjia Huang, Sijia Liu, Yi Lin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《UP: Unbounded Positive Asymmetric Optimization for Breaking the Exploration-Stability Dilemma》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become the standard paradigm for enhancing the complex reasoning capabilities of large language models (LLMs). To achieve sample efficiency, modern RL frameworks rely on importance sampling (IS). However, these algorithms suffer from an exploration-stability dilemma. Pure IS often leads to catastrophic training instability, while standard clipping mechanisms used to mitigate this instability strictly constrain the policy update budget. By formalizing the concept of Probability Capacity (Cap), we reveal that conservative clipping structurally stifles exploration by prematurely truncating the update budget for correct but low-confidence reasoning paths. To break free from these constraints, we propose Unbounded Positive Asymmetric Optimization (UP), a universal and plug-and-play objective. UP theoretically restructures the optimization process by anchoring the policy to its current state via the stop-gradient operator. This asymmetric design unleashes unclipped, stable gradients for positive advantages to maximize exploration, while maintaining standard clipping safeguards for negative advantages to prevent training instability. Furthermore, our formulation readily extends across different optimization granularities, including token-level (GRPO, DAPO) and sequence-level (GSPO) frameworks. Extensive experiments demonstrate that UP enhances exploration capacity and achieves superior reasoning accuracy across diverse RL algorithms (DAPO, GSPO, and GRPO), model architectures (Dense, MoE, and vision-language), and training modalities (language and multimodal), validating UP as a truly universal plug-and-play enhancement for RL-based training.

</details>

---

### [[20_Research/Papers/强化学习/Mathematical_methods_of_reinforcement_learning|Mathematical methods of reinforcement learning]]

![[assets/2607.06935_first_page.png|800]]

- **arXiv**: [2607.06935](https://arxiv.org/abs/2607.06935)
- **PDF**: https://arxiv.org/pdf/2607.06935
- **详细分析**: [[20_Research/Papers/强化学习/Mathematical_methods_of_reinforcement_learning|Mathematical methods of reinforcement learning]]
- **作者**: Denis Belomestny, Alexander Gasnikov, Egor Gladin, Alexey Naumov, Artemy Rubtsov, Yuri Sapronov, Daniil Tiapkin, Nikita Yudin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Mathematical methods of reinforcement learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is increasingly grounded in tools from probability, optimization, and operator theory. This survey organizes the mathematical structures that underpin the design and analysis of modern algorithms in RL. We begin from Markov decision processes (MDPs) and the Bellman operators, emphasizing contraction mappings, monotonicity, and fixed-point theory that yield convergence guarantees and rates for value and policy iteration, and temporal-difference schemes. We then develop the optimization perspective: stochastic approximation and martingale methods, convex duality and the role of regularization linking mirror/proximal methods. Function approximation is treated through linear and non-linear settings, covering stabilization, error decomposition, and sample-complexity via concentration inequalities for dependent data and mixing processes. We further cover off-policy evaluation/learning, constrained RL and constrained MDPs (CMDPs). Throughout we unify algorithmic templates under common operator and variational lenses, highlighting both finite-sample bounds and asymptotic results. Our presentation is intended to provide a unified mathematical entry point for researchers in probability, optimization, and statistics interested in reinforcement learning.

</details>

---

### [[20_Research/Papers/机器人/CaLiSym_Learning_Symplectic_Dynamics_of_Real-World_Systems_through_Structured_Canonical_Lifts|CaLiSym: Learning Symplectic Dynamics of Real-World Systems through Structured Canonical Lifts]]

![[assets/2607.06824_figure.png|800]]

- **arXiv**: [2607.06824](https://arxiv.org/abs/2607.06824)
- **PDF**: https://arxiv.org/pdf/2607.06824
- **详细分析**: [[20_Research/Papers/机器人/CaLiSym_Learning_Symplectic_Dynamics_of_Real-World_Systems_through_Structured_Canonical_Lifts|CaLiSym: Learning Symplectic Dynamics of Real-World Systems through Structured Canonical Lifts]]
- **作者**: Aristotelis Papatheodorou, Pranav Vaidhyanathan, Natalia Ares, Ioannis Havoutis, Gerard J. Milburn
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《CaLiSym: Learning Symplectic Dynamics of Real-World Systems through Structured Canonical Lifts》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GR-SympNet, GRB-SympNet, Real-World, SympNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physics-informed learning promises data-efficient and stable dynamics prediction, yet its strongest geometric guarantees have largely remained confined to closed conservative systems. This excludes many robotic systems of practical interest, where actuation, dissipation, and constraints continuously exchange energy and momentum with the environment. We introduce CaLiSym, a lightweight framework that extends exact symplectic learning to such systems by changing where the geometric prior is imposed. Rather than enforcing symplecticity on the measured physical state, CaLiSym embeds the state and its physical ports into a structured lifted canonical phase space, where the learned dynamics evolve through an exactly symplectic map. The lift is explicit and algebraic, requiring neither recurrent latent states, transformer decoders, implicit optimization, nor inference-time ODE integration. We instantiate the framework with generalized-ridge SympNet predictors and introduce GRB-SympNet, a B-spline variant that combines local approximation with exact symplectic structure. Experiments on a controlled dissipative double pendulum, a real-world quadrotor, and a contact-rich quadruped demonstrate consistent improvements in out-of-distribution autoregressive prediction while using parameter-efficient models. At the same time, the learned lifted dynamics preserve the symplectic form to numerical precision. These results show that symplectic learning can be extended beyond conservative mechanics through structured canonical lifts, enabling geometry-preserving dynamics models for real-world robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Pelican-VLA_0.5_Attending_Before_Acting_Benefits_Generalization|Pelican-VLA 0.5: Attending Before Acting Benefits Generalization]]

![[assets/2607.06655_figure.png|800]]

- **arXiv**: [2607.06655](https://arxiv.org/abs/2607.06655)
- **PDF**: https://arxiv.org/pdf/2607.06655
- **详细分析**: [[20_Research/Papers/具身智能/Pelican-VLA_0.5_Attending_Before_Acting_Benefits_Generalization|Pelican-VLA 0.5: Attending Before Acting Benefits Generalization]]
- **作者**: Zeyuan Ding, Wenhai Liu, Yang Xu, Jiayu Hu, Yinda Chen, Yi Zhang, Yong Dai, Jian Tang, Xiaozhu Ju
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Pelican-VLA 0.5: Attending Before Acting Benefits Generalization》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Pelican-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this report, we present Pelican-VLA 0.5, a unified VLA model that integrates vision-language understanding, future-frame generation, and action prediction within a single architecture. Pelican-VLA 0.5 achieves attention-level generalization: without object annotations, segmentation masks, attention supervision, or task-specific fine-tuning, its action pathway already focuses on the instruction-relevant object and contact region. This behavior persists across unseen scenes and unseen robot embodiments, and is substantially stronger than in other open-source VLA baselines. We verify that this ability originates from the learnable Reasoning Slots inserted between perception and action: by routing task-relevant visual information through a compact bottleneck, the slot interface induces manipulation-centric attention during pre-training and remains effective across different policy structures, including a MoT-style architecture.

</details>

---

### [[20_Research/Papers/强化学习/HiFuzz_Hierarchical_Reinforcement_Learning_for_Semantic-Aware_and_Adaptive_CPU_Fuzzing|HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing]]

![[assets/2607.06619_figure.png|800]]

- **arXiv**: [2607.06619](https://arxiv.org/abs/2607.06619)
- **PDF**: https://arxiv.org/pdf/2607.06619
- **详细分析**: [[20_Research/Papers/强化学习/HiFuzz_Hierarchical_Reinforcement_Learning_for_Semantic-Aware_and_Adaptive_CPU_Fuzzing|HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing]]
- **作者**: Ya Wang, Hanwei Fan, Zhenguo Liu, Xiaofeng Zhou, Yangdi Lyu, Jiang Xu, Wei Zhang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《HiFuzz: Hierarchical Reinforcement Learning for Semantic-Aware and Adaptive CPU Fuzzing》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern processor verification struggles to reach deep architectural states due to the inefficiencies of traditional mutation-based fuzzing. We propose HiFuzz, a novel hierarchical reinforcement learning framework that replaces mutation with a structured, two-layer generation process: a Program Agent for global layout and a Basic Block Agent for precise instruction filling. To overcome reward sparsity, HiFuzz integrates an adaptive coverage reward mechanism and a semantic-aware basic block encoder providing intrinsic feedback. Extensive evaluations on three real-world RISC-V cores demonstrate that HiFuzz significantly outperforms state-of-the-art fuzzers in coverage and bug detection.

</details>

---
