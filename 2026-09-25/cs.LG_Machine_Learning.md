# cs.LG | Machine Learning | 2026-09-25

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Temporal_Gradient_Inversion_for_Private_Trajectory_Reconstruction_in_Embodied_Reinforcement_Learning|Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning]]

![[assets/2609.30258_figure.png|800]]

- **arXiv**: [2609.30258](https://arxiv.org/abs/2609.30258)
- **PDF**: https://arxiv.org/pdf/2609.30258
- **详细分析**: [[20_Research/Papers/具身智能/Temporal_Gradient_Inversion_for_Private_Trajectory_Reconstruction_in_Embodied_Reinforcement_Learning|Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning]]
- **作者**: Sudip Bhujel, Shanghao Shi, Ruiquan Huang, Ning Zhang, Yang Xiao
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 世界模型, 大模型
- **相关性评分**: 2.22（加权：具身智能 1.2，大模型 0.1，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Temporal Gradient Inversion for Private Trajectory Reconstruction in Embodied Reinforcement Learning》归入 具身智能、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distributed learning in embodied reinforcement-learning agents offers a degree of privacy by retaining raw sensor data on-device and transmitting only policy gradients to the server. Yet temporal structure can amplify this leakage beyond single-frame attacks. We introduce Temporal Reconstruction Attack on Consecutive Encodings (TRACE), an amortized temporal gradient-inversion attack that autoregressively reconstructs the sequence of private observation-action trajectories from per-step policy-learning gradients. The attack exploits two structural signals ignored by prior single-frame methods: (i) cross-time correlation between successive embodied gradients, which we formalize via a conditional mutual-information bound, and (ii) closed-form action recovery from policy-head gradient structure, which we prove exact when standard entropy regularization is sufficiently small. On held-out embodied scenes, TRACE reaches $18.8$ dB PSNR with near-perfect action recovery at $3$-$4.5$ ms per reconstructed frame, dominating the learning-based baseline across all reconstruction metrics and exceeding optimization attacks while running orders of magnitude faster. Further evaluation demonstrates TRACE's broader applicability across recurrent, residual, and compact transformer victim architectures, multi-modal inputs, and larger discrete action spaces. Defense experiments suggest that protecting temporal gradient streams may require sequence-aware privacy mechanisms.

</details>

---

### [[20_Research/Papers/强化学习/Graph-Based_Inference_and_Topology-Aware_Multi-Agent_Reinforcement_Learning_for_Large-Scale_Railway_Network_Management|Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management]]

![[assets/2609.30150_figure.jpg|800]]

- **arXiv**: [2609.30150](https://arxiv.org/abs/2609.30150)
- **PDF**: https://arxiv.org/pdf/2609.30150
- **详细分析**: [[20_Research/Papers/强化学习/Graph-Based_Inference_and_Topology-Aware_Multi-Agent_Reinforcement_Learning_for_Large-Scale_Railway_Network_Management|Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management]]
- **作者**: Giacomo Arcieri, Gregory Duthé, Christophe Muller, Konstantinos G. Papakonstantinou, Daniel Straub, Eleni Chatzi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.5，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Graph-Based Inference and Topology-Aware Multi-Agent Reinforcement Learning for Large-Scale Railway Network Management》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern infrastructure asset management constitutes a complex sequential decision-making problem, characterized by long planning horizons and system-level interactions, such as spatial deterioration correlations and economies of scale. While deep reinforcement learning has shown promise in optimizing maintenance policies, scaling to real-world networks remains challenging. Centralized approaches become computationally intractable in large-scale systems, whereas decentralized approaches often fail to capture essential coordination mechanisms. To address these challenges, we propose a graph-based framework that integrates accurate environment modeling with scalable decision support. First, we employ a hierarchical Bayesian model leveraging a Gaussian Process on Graph kernel to infer a realistic, spatially correlated networked environment of railway maintenance planning from real-world data provided by the Swiss Federal Railways. Second, we introduce a topology-aware Multi-Agent Reinforcement Learning (MARL) framework by integrating graph neural networks and graph Transformers to optimize network-level policies. A central contribution of this work is the demonstration of scalability through zero-shot transfer learning: graph-based agents, trained only on small network portions, are successfully deployed in a zero-shot manner on large-scale unseen networks without any retraining. Numerical results indicate that the proposed method significantly outperforms optimized heuristics and standard MARL baselines, reducing computational training time while maintaining superior performance on large-scale networks.

</details>

---

### [[20_Research/Papers/世界模型/Aim_Short_to_Reach_Far_Your_Frozen_World_Model_Can_Plan_Better_Than_You_Think|Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think]]

![[assets/2609.30036_first_page.png|800]]

- **arXiv**: [2609.30036](https://arxiv.org/abs/2609.30036)
- **PDF**: https://arxiv.org/pdf/2609.30036
- **详细分析**: [[20_Research/Papers/世界模型/Aim_Short_to_Reach_Far_Your_Frozen_World_Model_Can_Plan_Better_Than_You_Think|Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think]]
- **作者**: Xvyuan Liu, Jianjie Fang, Chen Gao, Yong Li
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《Aim Short to Reach Far: Your Frozen World Model Can Plan Better Than You Think》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planners built on visual world models commonly score each predicted outcome by its distance to the encoded goal image. We show that this target can limit control even with exact dynamics and globally optimal short-horizon search: reaching a goal may require actions that initially move away from it. With frozen LeWM models, intermediate targets substantially improve action synthesis and recorded-action ranking on Cube, PushT, Reacher, and TwoRoom. Learned targets and targets drawn from observed experience both produce these gains. We introduce Anchored Planning, which retrieves a recorded segment whose start and end resemble the current and goal observations, then aims at an observation shortly after its start. The frozen model scores actions toward this target from the current state. Without additional training, planning toward observed targets outperforms the released LeWM planner on every task in our long-range evaluation. Additional final-goal search falls short of the same gains. Lower successor-prediction error need not translate into better control. Success also depends on how far ahead the target is placed and on shrinking the retrieval span as execution advances. Changing only the target lets the same frozen model and planner reach goals that final-goal scoring misses.

</details>

---

### [[20_Research/Papers/强化学习/Certified_Predictive_Value-of-Advice_Gating_for_Cost-Aware_Language-Model_Guidance_in_Reinforcement_Learning|Certified Predictive Value-of-Advice Gating for Cost-Aware Language-Model Guidance in Reinforcement Learning]]

![[assets/2609.29548_first_page.png|800]]

- **arXiv**: [2609.29548](https://arxiv.org/abs/2609.29548)
- **PDF**: https://arxiv.org/pdf/2609.29548
- **详细分析**: [[20_Research/Papers/强化学习/Certified_Predictive_Value-of-Advice_Gating_for_Cost-Aware_Language-Model_Guidance_in_Reinforcement_Learning|Certified Predictive Value-of-Advice Gating for Cost-Aware Language-Model Guidance in Reinforcement Learning]]
- **作者**: Ibne Farabi Shihab, Md Najmus Swaqeeb, Abu Sa-Adat Mohamed Moon-Im Al Ahsan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Certified Predictive Value-of-Advice Gating for Cost-Aware Language-Model Guidance in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GridWorld, PSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-model advice can accelerate reinforcement learning, but calls are costly and returned actions may be stale or wrong. We formulate advice acquisition as a response-contingent metareasoning problem: before querying, the controller predicts possible parsed responses, evaluates the decision and declared continuation that would follow each response, and queries only when a lower confidence bound on predictive value exceeds the priced cost. Execution is governed separately by an action-specific certificate. Under explicit assumptions, certified advice is near-optimal, a wrapped learner inherits fallback regret only under intervention stability, and conservative allocation loses at most the declared query-value estimation error relative to a myopic oracle. On BabyAI, a proxy-calibrated controller with Qwen2.5-1.5B and 7B advisors improves GoToObj return over no querying by 0.029 +/- 0.016 and 0.030 +/- 0.015 across 20 seeds while reducing calls by more than 97% relative to always-query. GoToLocal is a null result. Exactly matched-call tests show an advantage over random placement only for the 1.5B advisor and no advantage over an equal-budget early schedule. Mondrian calibration improves decision-relevant empirical coverage from 0.47 to 0.85, still below the 0.90 target, while the formally covered radius is vacuous. The demonstrated benefit is therefore robust sparse advice volume on a useful task, not a proven per-state placement advantage.

</details>

---

### [[20_Research/Papers/大模型/CataOPD_Catalytic_On-Policy_Distillation_for_Large_Language_Model_Reasoning|CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning]]

![[assets/2609.29518_figure.png|800]]

- **arXiv**: [2609.29518](https://arxiv.org/abs/2609.29518)
- **PDF**: https://arxiv.org/pdf/2609.29518
- **详细分析**: [[20_Research/Papers/大模型/CataOPD_Catalytic_On-Policy_Distillation_for_Large_Language_Model_Reasoning|CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning]]
- **作者**: Wenjin Liu, Chenxi Wang, Jiapu Wang, Zhe Cui, Anh Tuan Luu, Haoran Luo
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《CataOPD: Catalytic On-Policy Distillation for Large Language Model Reasoning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ProRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) and on-policy distillation (OPD) are two representative paradigms for improving large language model reasoning. However, when no correct trajectory is sampled, RL lacks a positive correctness signal, while OPD remains constrained by the reasoning trajectories reachable under the student's on-policy distribution. Therefore, we propose CataOPD, where the teacher acts as a catalyst rather than a target, expanding reachability while internalizing verified student-produced trajectories into a catalyst-free policy. Self-Rescue Routing uses empirically all-failed groups as routing signals rather than teacher-intervention triggers, first seeking correct trajectories through additional on-policy self-sampling. For problems unresolved after self-rescue, Catalytic-Guided Self-Resolution uses catalytic guidance to elicit a verified student-produced trajectory in the guided student distribution. Barrier-Weighted Internalization weights tokens by guided-to-unguided log-probability gaps, focusing updates on decisive tokens difficult without guidance. Experimental results show that CataOPD outperforms current baselines, extends independent student reasoning to still-unrecovered problems, and improves out-of-distribution generalization under catalyst-free inference. Our project is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Decoupled_Early_Exits_for_Task-Dependent_Compute_Allocation_in_Flow-Matching_VLAs|Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs]]

![[assets/2609.29382_figure.png|800]]

- **arXiv**: [2609.29382](https://arxiv.org/abs/2609.29382)
- **PDF**: https://arxiv.org/pdf/2609.29382
- **详细分析**: [[20_Research/Papers/具身智能/Decoupled_Early_Exits_for_Task-Dependent_Compute_Allocation_in_Flow-Matching_VLAs|Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs]]
- **作者**: Riccardo Andrea Izzo, Rimvydas Rubavicius, Gianluca Bardaro, Subramanian Ramamoorthy, Matteo Matteucci, Alessandro Suglia
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.9，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Decoupled Early Exits for Task-Dependent Compute Allocation in Flow-Matching VLAs》归入 具身智能、机器人、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BranchyNet, CEED-VLA, DeeR-VLA, EfficientVLA, Meta-World, MoLE-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching Vision-Language-Action (VLA) models have emerged as a potential solution for generalist robot control, designed by combining a pretrained Vision-Language Model (VLM) backbone with an action expert that generates continuous robot actions. While these models exhibit impressive capabilities, due to their very high number of parameters, their computational requirements are often prohibitive for robotics control. To mitigate these inefficiencies, existing methods predominantly skip VLM backbone layers with early exits or reduce denoising steps, while leaving action expert depth untouched. We propose a framework that exposes backbone depth $V$, action expert depth $A$, and denoising steps $D$ as three jointly configurable compute axes in a VLA. Starting from a pretrained VLA, we attach lightweight Exit Transformers (ET) at intermediate depths in both the backbone and the action expert, trained to distil the last layer of the policy into each exit. Furthermore, we introduce a KV Cache synthesis mechanism that manages the missing keys and values of the skipped backbone layers, allowing the action expert to exit deeper than the backbone. Finally, we show that the optimal compute budget is task-dependent, with different tasks benefiting from different axes and depths. Notably, our method does not require training the original policy from scratch, and for each exit, it increases the number of parameters by only $2.1\%$ for SmolVLA and $4.1\%$ for $\pi_{0.5}$. We validate our approach across two flow-matching VLAs (SmolVLA, $\pi_{0.5}$) and two benchmarks (LIBERO, Meta-World), revealing complementary effects: $V$ and $A$ respectively reduce FLOPs and latency, while $D$ improves both. Our joint configurations $(V,A,D)$ reduce latency by $79.2\%$ and computation (FLOPs) by $31.8\%$, while improving mean success rate by $5.6\%$.

</details>

---

### [[20_Research/Papers/大模型/Continuous_Online_Fault_Detection_for_Mobile_Robots_via_Adaptive_Edge_Models|Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models]]

![[assets/2609.29194_figure.png|800]]

- **arXiv**: [2609.29194](https://arxiv.org/abs/2609.29194)
- **PDF**: https://arxiv.org/pdf/2609.29194
- **详细分析**: [[20_Research/Papers/大模型/Continuous_Online_Fault_Detection_for_Mobile_Robots_via_Adaptive_Edge_Models|Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models]]
- **作者**: Jordan Levy, Nicolas Verstaevel, Vincent Talon, Benoit Gaudou
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《Continuous Online Fault Detection for Mobile Robots via Adaptive Edge Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robots require robust, real-time fault detection capable of continuous adaptation on constrained edge hardware. While deep time-series models excel at unsupervised anomaly detection, their computational cost prohibits high-frequency onboard execution. This paper bridges this gap via a Teacher-Student distillation framework. An offline foundation model (TSPulse) generates pseudo-labels from unlabeled time series augmented with fault injections. A lightweight MiniRocket Student, adapted with a Recursive Least Squares estimator, approximates this complex decision boundary to execute real-time inference onboard. Evaluations on the TSB-AD benchmark and a physical mobile robot demonstrate the Student achieves a 4.30 ms CPU inference latency. During real-world domain shifts, online adaptation enables the Student to recover from unseen mechanical degradation, improving VUS-PR scores from 0.26 to 0.75 without catastrophic forgetting. Crucially, an uncertainty-guided active learning strategy minimizes operator cognitive load, requesting sparse interventions only when encountering novel fault distributions. These results validate the deployment of state-of-the-art anomaly detection on resource-constrained robotics through offline-to-online distillation.

</details>

---

### [[20_Research/Papers/强化学习/A_Concentration_Bound_for_Two-Timescale_Actor-Critic_Algorithm|A Concentration Bound for Two-Timescale Actor-Critic Algorithm]]

![[assets/2609.29117_figure.png|800]]

- **arXiv**: [2609.29117](https://arxiv.org/abs/2609.29117)
- **PDF**: https://arxiv.org/pdf/2609.29117
- **详细分析**: [[20_Research/Papers/强化学习/A_Concentration_Bound_for_Two-Timescale_Actor-Critic_Algorithm|A Concentration Bound for Two-Timescale Actor-Critic Algorithm]]
- **作者**: Prashansa Panda, Shalabh Bhatnagar
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《A Concentration Bound for Two-Timescale Actor-Critic Algorithm》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Significant research effort has been directed in recent years towards establishing both asymptotic and non-asymptotic convergence guarantees for two-timescale actor--critic algorithms, where the actor recursion is run on a slower timescale than the critic recursion. This work derives a uniform all-time concentration bound for the actor--critic algorithm with function approximation in the long-run average-reward setting. This bound helps us analyze the behavior of the actor parameter with high probability. We show that, after some finite time, the actor parameter enters a safe region and remains within it thereafter with high probability. Specifically, with probability at least $1-\epsilon_1-\epsilon_2$, the actor error $\Vert \theta_k-\theta^{*}\Vert$ is $O\left(\frac{n_0^{3/4}}{k}\frac{1}{\sqrt{\epsilon_2}}+\left(\frac{1}{n_0}\right)^{1/4}\log^{1/4}\left(\frac{1}{\epsilon_1}\right)+\left(\frac{1}{n_0}\right)^{1/4}\right)$ for all $k\geq n_0$ and sufficiently large $n_0$. We also present experimental results demonstrating that the aforementioned actor error diminishes with the number of actor-parameter updates.

</details>

---

### [[20_Research/Papers/具身智能/Learning_from_Mixed-Quality_Deployment_Experience_for_Robot_Manipulation|Learning from Mixed-Quality Deployment Experience for Robot Manipulation]]

![[assets/2609.29000_figure.png|800]]

- **arXiv**: [2609.29000](https://arxiv.org/abs/2609.29000)
- **PDF**: https://arxiv.org/pdf/2609.29000
- **详细分析**: [[20_Research/Papers/具身智能/Learning_from_Mixed-Quality_Deployment_Experience_for_Robot_Manipulation|Learning from Mixed-Quality Deployment Experience for Robot Manipulation]]
- **作者**: Yangang Ren, Yujie Yan, Zirui Li, Jiaming Guo, Di Zeng, Ji Tao, Lan Yu, Xuesong Tian, Chen Lv
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 2.52（加权：具身智能 1.2，强化学习 0.36，世界模型 0.16，机器人 0.8）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning from Mixed-Quality Deployment Experience for Robot Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies deployed in real environments naturally accumulate mixed-quality experience, including successful executions, partial progress, and failures. Although these rollouts provide valuable information for further learning, directly incorporating them into imitation learning may reinforce undesirable behaviors, while offline reinforcement learning often suffers from unreliable value estimation under sparse rewards and limited data coverage. We consider a practical post-deployment setting where learning relies only on naturally accumulated autonomous rollouts, without additional human corrections or exploratory interaction. To effectively exploit such experience, we propose Predictive Action Chunk Learning (PACL). PACL first learns a predictive chunk-level critic that evaluates temporally extended action sequences and augments temporal difference learning with future latent prediction, providing richer supervision for long-horizon value estimation. The learned critic then converts chunk-level Q-values into discrete quality conditions, which guide a diffusion actor to learn jointly from these mixed-quality experiences without treating all behaviors as equivalent supervision. At inference, the actor generates multiple action chunks and the critic selects the highest valued candidate. Experiments across simulated and real-world robot manipulation tasks show that PACL consistently improves the pretrained policy and outperforms strong imitation learning and offline reinforcement learning baselines.

</details>

---

### [[20_Research/Papers/具身智能/Uncertainty-Gated_Exploration_Noise_Suppresses_Task_Collapse_in_Online_RL_Fine-Tuning_of_a_Flow-Matching_Vision-Language-Action_Policy|Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy]]

![[assets/2609.28838_first_page.png|800]]

- **arXiv**: [2609.28838](https://arxiv.org/abs/2609.28838)
- **PDF**: https://arxiv.org/pdf/2609.28838
- **详细分析**: [[20_Research/Papers/具身智能/Uncertainty-Gated_Exploration_Noise_Suppresses_Task_Collapse_in_Online_RL_Fine-Tuning_of_a_Flow-Matching_Vision-Language-Action_Policy|Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy]]
- **作者**: Mehmet Turan Yardımcı, Yunus Emre Çoğurcu
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 2.62（加权：具身智能 1.8，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Multimodal, RL, Systems

#### 研究背景与动机

《Uncertainty-Gated Exploration Noise Suppresses Task Collapse in Online RL Fine-Tuning of a Flow-Matching Vision-Language-Action Policy》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online reinforcement learning fine-tuning of pretrained flow-matching vision-language-action (VLA) policies promises robots that keep learning after deployment, but continued updates often destroy competence on individual tasks while the aggregate still looks healthy. We study this failure mode, which we call task collapse, under a matched small-compute budget on LIBERO-10 with a 450M-parameter SmolVLA policy trained by PPO with stochastic (SDE) sampling. Three exploration-noise policies differ in one live variable: a fixed noise scale, a ReinFlow-style learned noise network, and an uncertainty-gated controller that redistributes exploration across task streams from task-agnostic novelty and competence signals, without task labels or episode boundaries. Under the pooled definition, fixed noise collapses tasks in two of three seeds and learned noise in every seed measured to iteration 200, while the controller collapses none in any of its three seeds. Measured parameter displacement shows the controller's action expert keeps changing, while its mean applied noise is close to the fixed scale in the available logs. The matched comparison supports the controller's effect on task preservation; the separate contributions of its adaptation across states and over time are not disentangled. A lower fixed scale slows the decline but does not stop it. No arm improves on the behavior-cloning baseline in this budget. Two properties of that regime are measured beside this result, not offered as its cause: following the reference recipe, training runs in bfloat16 with no fp32 master copy, under which 96.02% of the action expert's elements stay bit-identical across three consecutive iterations, and an fp32 master copy at the reference learning rate collapses both arms in a single-seed observation. We release tools measuring per-task collapse under four definitions, rescoring noise and instrument tares.

</details>

---
