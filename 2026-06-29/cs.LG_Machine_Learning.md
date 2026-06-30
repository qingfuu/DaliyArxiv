# cs.LG | Machine Learning | 2026-06-29

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/世界模型/Disentangling_Continuous-Time_Latent_Dynamics_Identifiability_of_Latent_SDEs_via_Diffusion_Shifts|Disentangling Continuous-Time Latent Dynamics: Identifiability of Latent SDEs via Diffusion Shifts]]

![[assets/2606.28228_figure.png|800]]

- **arXiv**: [2606.28228](https://arxiv.org/abs/2606.28228)
- **PDF**: https://arxiv.org/pdf/2606.28228
- **详细分析**: [[20_Research/Papers/世界模型/Disentangling_Continuous-Time_Latent_Dynamics_Identifiability_of_Latent_SDEs_via_Diffusion_Shifts|Disentangling Continuous-Time Latent Dynamics: Identifiability of Latent SDEs via Diffusion Shifts]]
- **作者**: Yuanyuan Wang, Wenjie Wang, Haoxuan Li, Mingming Gong, Kun Zhang
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Disentangling Continuous-Time Latent Dynamics: Identifiability of Latent SDEs via Diffusion Shifts》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Causal representation learning for time series has developed strong identifiability results in discrete-time latent causal models, but identifiability in continuous-time latent stochastic differential equation (SDE) models remains largely open. We address this gap using environment-induced shifts in diffusion covariance. We study additive-noise latent SDEs observed through an unknown nonlinear diffeomorphism, with shared drift but environment-specific diffusion covariance. We show that two diagonal diffusion regimes with pairwise distinct coordinate-wise variance ratios identify the latent coordinates up to permutation and scaling, without any sparsity assumption on the drift. We first prove this result for linear Ornstein--Uhlenbeck systems and then extend it to general additive-noise latent SDEs. Under mild smoothness, the instantaneous drift-Jacobian causal graph is identifiable up to the same permutation. We propose a two-stage estimator for latent disentanglement and optional graph recovery; experiments on synthetic systems confirm the predicted identifiability boundary, and an application to Hardanger Bridge monitoring data illustrates the approach on real sensor trajectories.

</details>

---

### [[20_Research/Papers/具身智能/Regularized_Reward-Punishment_Reinforcement_Learning|Regularized Reward-Punishment Reinforcement Learning]]

![[assets/2606.28152_figure.jpg|800]]

- **arXiv**: [2606.28152](https://arxiv.org/abs/2606.28152)
- **PDF**: https://arxiv.org/pdf/2606.28152
- **详细分析**: [[20_Research/Papers/具身智能/Regularized_Reward-Punishment_Reinforcement_Learning|Regularized Reward-Punishment Reinforcement Learning]]
- **作者**: Jiexin Wang, Eiji Uchibe
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Regularized Reward-Punishment Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RPRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose KL-Coupled Policy Regularization (KCPR), a policy coordination framework for Reward-Punishment Reinforcement Learning (RPRL). Based on KCPR, we derive KL-Coupled Soft Optimality (KCSO) and develop its deep realization, klDMP. Unlike existing RPRL approaches that optimize reward-seeking and punishment-related policies largely independently, KCPR enables direct interactions between companion policies by treating each as a dynamically learned prior for the other. KCSO yields coupled soft-optimal policies and KL-regularized Bellman operators, allowing reward and punishment information to jointly influence value propagation. To improve learning stability, we introduce a companion-prior softening mechanism and evaluate separate replay-buffer designs for balancing reward- and punishment-related experience. Experiments in grid-world and Gazebo robotic navigation tasks demonstrate that klDMP improves safety and learning stability while maintaining competitive task performance compared with DQN, SQL and softDMP. These results suggest that policy-level coordination provides an effective mechanism for integrating multiple behavioral objectives and may serve as a useful design principle for reinforcement learning systems with interacting motivational processes.

</details>

---

### [[20_Research/Papers/大模型/From_Detection_to_Action_Using_LLM_Agents_for_Fault-Tolerant_Control|From Detection to Action: Using LLM Agents for Fault-Tolerant Control]]

![[assets/2606.28011_figure.png|800]]

- **arXiv**: [2606.28011](https://arxiv.org/abs/2606.28011)
- **PDF**: https://arxiv.org/pdf/2606.28011
- **详细分析**: [[20_Research/Papers/大模型/From_Detection_to_Action_Using_LLM_Agents_for_Fault-Tolerant_Control|From Detection to Action: Using LLM Agents for Fault-Tolerant Control]]
- **作者**: Javal Vyas, Milapji Singh Gill, Artan Markaj, Felix Gehlhoff, Mehmet Mercangöz
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《From Detection to Action: Using LLM Agents for Fault-Tolerant Control》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose an agentic Large Language Model (LLM) framework for active Fault-Tolerant Control (FTC) that transforms fault detection outputs into constraint-aware recovery actions grounded in plant-specific knowledge. The approach couples (i) a multi-agent workflow that decomposes operator duties into monitoring, planning, action synthesis, simulation, validation, and reprompting; (ii) a Digital Process Plant Twin (DPPT) that exposes plant data, models, and a simulation service for pre-execution testing; and (iii) a Graph Retrieval-Augmented Generation (Graph RAG) layer built on the CPSMod ontology, which organizes plant knowledge (structure, function, hybrid dynamics, control context, and fault semantics) into a graph that supports relation-aware, multi-hop retrieval for the agents. Corrective actions are generated as minimal-risk state-machine recovery paths and corresponding discrete commands or continuous setpoint adaptations, then validated deterministically against interlocks, envelopes, and dynamic feasibility before any actuation. If no acceptable plan is found within a bounded time window, control is handed to a safety fallback. The framework is evaluated in simulation on two representative benchmarks: a discrete batch Mixing Module and a Continuous Stirred-Tank Reactor (CSTR) under closed-loop PID regulation. Results with lightweight LLMs (GPT-4o-mini and GPT-4.1-mini) show that semantically grounded agents can derive valid recovery decisions within latency budgets compatible with the respective process dynamics, demonstrating a practical pathway from detection to validated corrective action across both discrete and continuous FTC tasks.

</details>

---

### [[20_Research/Papers/强化学习/PerturbCellRL_Verifier-Guided_Reinforcement_Learning_for_Single-Cell_Perturbation_Prediction|PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction]]

![[assets/2606.27752_figure.png|800]]

- **arXiv**: [2606.27752](https://arxiv.org/abs/2606.27752)
- **PDF**: https://arxiv.org/pdf/2606.27752
- **详细分析**: [[20_Research/Papers/强化学习/PerturbCellRL_Verifier-Guided_Reinforcement_Learning_for_Single-Cell_Perturbation_Prediction|PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction]]
- **作者**: Dongxia Wu, Mingyu Li, Yuhui Zhang, Anurendra Kumar, Emma Lundberg, Serena Yeung-Levy, Emily B. Fox
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《PerturbCellRL: Verifier-Guided Reinforcement Learning for Single-Cell Perturbation Prediction》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PerturbCellRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Single-cell perturbation models can reduce costly wet-lab screening by predicting how cells respond transcriptionally to interventions. While recent generative models improve population-level prediction, individual generated cells are not explicitly checked for biological consistency. We introduce PerturbCellRL, a reinforcement learning (RL) framework that post-trains a pretrained single-cell transcriptomic generator using a suite of cell-level verifiers as rewards. These verifiers define four rewards: Pearson top-k similarity, RMSE top-k proximity, DE Spearman, and Pathway activity. The Pathway activity verifier rewards cells whose pathway responses match known perturbation biology. We evaluate PerturbCellRL on multiple genetic and chemical perturbation benchmarks. Across these benchmarks, PerturbCellRL improves over the pretrained flow-matching generator on reward-aligned evaluation metrics and a held-out evaluation metric. Moreover, PerturbCellRL remains competitive with state-of-the-art methods on population-level metrics. Together, these results frame trustworthy single-cell prediction as verifier-guided generative alignment, moving beyond matching expression distributions toward predictions whose single-cell perturbation effects are explicitly checked for biological consistency.

</details>

---

### [[20_Research/Papers/强化学习/Learning_to_Reason_with_Curriculum_II_Compositional_Generalization|Learning to Reason with Curriculum II: Compositional Generalization]]

![[assets/2606.27721_first_page.png|800]]

- **arXiv**: [2606.27721](https://arxiv.org/abs/2606.27721)
- **PDF**: https://arxiv.org/pdf/2606.27721
- **详细分析**: [[20_Research/Papers/强化学习/Learning_to_Reason_with_Curriculum_II_Compositional_Generalization|Learning to Reason with Curriculum II: Compositional Generalization]]
- **作者**: Nived Rajaraman, Audrey Huang, Miroslav Dudik, Robert Schapire, Dylan Foster, Akshay Krishnamurthy
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Learning to Reason with Curriculum II: Compositional Generalization》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compositional generalization, the ability to solve complex problems by combining solutions to simpler sub-problems, is a fundamental capability of both natural and artificial intelligence, and a key mechanism underlying chain-of-thought reasoning. However, the theoretical underpinnings of compositional generalization remain poorly understood: when and why does decomposing a problem into parts yield more efficient learning than solving it directly? We study this question through the canonical problem of learning to simulate semiautomata (predicting the outcome of $T$ steps of sequential computation), a model that captures state tracking, regular language recognition, and modular arithmetic. We show that an autocurriculum-based approach building on Part I of this series, recursively decomposing longer sequences into shorter sub-problems, learning to solve them, and composing the solutions, achieves dramatically better statistical complexity than direct methods. (i) For a setting inspired by supervised fine-tuning (SFT) where the learner receives interactive feedback on intermediate states of the computation, curriculum facilitates learning from only $2^{\mathcal{O}(\sqrt{\log T})}$ tokens of supervision; i.e., subpolynomial in the sequence length $T$, overcoming the $Ω(T)$ token barrier required by direct simulation. (ii) For a setting inspired by reinforcement learning with verifiable rewards (RLVR), where the learner improves a pre-trained reference model using an outcome verifier, we show that curriculum reduces the requirement on the reference model from coverage at the full sequence length $T$ to coverage at a shorter block length $B \ll T$, an exponentially weaker condition.

</details>

---

### [[20_Research/Papers/机器人/Physics-Guided_Robotic_Radiation_Source_Localization_along_Arbitrary_Measurement_Paths_in_Unstructured_Environments|Physics-Guided Robotic Radiation Source Localization along Arbitrary Measurement Paths in Unstructured Environments]]

![[assets/2606.27624_figure.png|800]]

- **arXiv**: [2606.27624](https://arxiv.org/abs/2606.27624)
- **PDF**: https://arxiv.org/pdf/2606.27624
- **详细分析**: [[20_Research/Papers/机器人/Physics-Guided_Robotic_Radiation_Source_Localization_along_Arbitrary_Measurement_Paths_in_Unstructured_Environments|Physics-Guided Robotic Radiation Source Localization along Arbitrary Measurement Paths in Unstructured Environments]]
- **作者**: Hojoon Son, Kai Tan, Fan Zhang
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Physics-Guided Robotic Radiation Source Localization along Arbitrary Measurement Paths in Unstructured Environments》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Using robots to estimate the location of the radiation source is an effective way to improve efficiency and safety. Existing methods focus on planning the robot's path to achieve precise estimation, typically approaching the source. However, approaching the source increases the risk of radiation damage to a robot. In addition, a path-planning algorithm designed solely for radiation source localization (RSL) limits the flexibility of missions that deploy robots into radioactive environments. This study presents an automation framework for robotic RSL that leverages a physics-informed machine learning (PIML) model to precisely estimate the source location, regardless of measurement paths, in unknown environments. Physics-inspired model tensors have been designed for PIML to handle attenuated gamma-ray flux signals from unknown obstacles, and multiple models are computed in parallel to improve the robustness and precision of the RSL. The proposed method is evaluated in high-fidelity simulation environments using Monte Carlo particle transport across diverse randomized domains, including spatial scales, radiation source types, obstacle materials and geometries, and robot trajectories. The method is also validated through physical experiments on configurations that are not included in the simulation-based evaluation. The continuous learning technique is applied in real-robot deployment to enhance the practical applicability of the online robotic RSL system. The proposed method advances robot radiation perception from pointwise flux detection to spatial intelligence.

</details>

---

### [[20_Research/Papers/大模型/COOPA_A_Modular_LLM_Agent_Architecture_for_Operations_Research_Problems|COOPA: A Modular LLM Agent Architecture for Operations Research Problems]]

![[assets/2606.27611_figure.png|800]]

- **arXiv**: [2606.27611](https://arxiv.org/abs/2606.27611)
- **PDF**: https://arxiv.org/pdf/2606.27611
- **详细分析**: [[20_Research/Papers/大模型/COOPA_A_Modular_LLM_Agent_Architecture_for_Operations_Research_Problems|COOPA: A Modular LLM Agent Architecture for Operations Research Problems]]
- **作者**: Chuanhao Li, Xiaoan Xu, Dirk Bergemann, Ethan X. Fang, Yehua Wei, Zhuoran Yang
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《COOPA: A Modular LLM Agent Architecture for Operations Research Problems》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Operations Research (OR) provides a rigorous framework for high-stakes decision-making, but effective OR modeling requires substantial domain knowledge, mathematical abstraction, and solver expertise. Recent LLM-based systems automate parts of this pipeline, yet remain limited by low accuracy on complex problems, opaque outputs, and narrow solver support. We propose COOPA (COoperative OPerations Agent), a modular LLM-agent architecture for interpretable and scalable OR decision support. It combines three components: iterative confidence-based modeling, which generates multiple candidate formulations, self-evaluates them across modeling dimensions, and selects one using a max-min confidence criterion; element-level provenance and confidence explanations, which link variables, parameters, constraints, and objectives to quoted source text and provide an audit trail for human verification; and multi-solver routing to specialized optimizer agents for different OR problem classes. Across three OR benchmarks, eight LLM backbones, and four baselines under identical conditions, COOPA achieves the best macro-average accuracy on six of eight backbones and improves over the strongest baseline by up to 6.7 percentage points. A within-system ablation isolates the contribution of iterative confidence-based modeling, while additional analyses and case studies illustrate the value of source traceability and multi-solver dispatch.

</details>

---

### [[20_Research/Papers/强化学习/Training_Observable_Control_Policies_to_Expose_Agent_State_Through_Actions|Training Observable Control Policies to Expose Agent State Through Actions]]

![[assets/2606.27609_figure.png|800]]

- **arXiv**: [2606.27609](https://arxiv.org/abs/2606.27609)
- **PDF**: https://arxiv.org/pdf/2606.27609
- **详细分析**: [[20_Research/Papers/强化学习/Training_Observable_Control_Policies_to_Expose_Agent_State_Through_Actions|Training Observable Control Policies to Expose Agent State Through Actions]]
- **作者**: Andres Enriquez Fernandez, John J. Bird
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Training Observable Control Policies to Expose Agent State Through Actions》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical or operational constraints often impose communications limitations on autonomous agents. Such limitations complicate monitoring or multiagent coordination. Even when strong communications are absent, some information may still be available. The remainder of the relevant agent state may be reconstructed via estimation. The actions taken by an agent are a potential source of information -- as the agent interacts with the environment, these actions may be observed even in the absence of explicit communication. We investigate using actions to estimate the state of an agent, using reinforcement learning to develop policies which make the estimation problem more tractable. Policy observability is encouraged through the training reward and is analyzed using simulation of the trained agent. In an aircraft tracking problem a policy with enhanced observability is found that has minimal impact on nominal task performance.

</details>

---

### [[20_Research/Papers/具身智能/Support-Constrained_RL_Enables_Real-World_Policy_Improvement_without_Real-World_Experience|Support-Constrained RL Enables Real-World Policy Improvement without Real-World Experience]]

![[assets/2606.27475_first_page.png|800]]

- **arXiv**: [2606.27475](https://arxiv.org/abs/2606.27475)
- **PDF**: https://arxiv.org/pdf/2606.27475
- **详细分析**: [[20_Research/Papers/具身智能/Support-Constrained_RL_Enables_Real-World_Policy_Improvement_without_Real-World_Experience|Support-Constrained RL Enables Real-World Policy Improvement without Real-World Experience]]
- **作者**: Raymond Yu, William Huey, Mustafa Mukadam, Anusha Nagabandi, Abhishek Gupta
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 2.42（加权：具身智能 1.2，强化学习 0.56，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Support-Constrained RL Enables Real-World Policy Improvement without Real-World Experience》归入 具身智能、强化学习、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots trained on real world data tend to be imprecise, slow, and brittle to perturbations. Improving these policies with reinforcement learning (RL) is an appealing alternative, but this process often requires expensive training in the real world. Performing policy improvement in simulation instead provides a far cheaper alternative, but unconstrained RL in simulation can exploit contact and dynamics mismatches, resulting in unsafe behaviors that do not transfer to hardware. Common forms of regularization can furthermore limit improvement by overconstraining to an imperfect behavior prior. In this work, we propose Support-Constrained Off-Domain REinforcement (SCORE), a real-to-sim-to-real framework that constrains RL in simulation to the support of a generative policy pretrained on real data. We instantiate this constraint through flow steering, restricting SCORE to actions the base policy can already produce, which ensures transferable behaviors while maximizing policy improvement. Improving a policy with SCORE requires minimal effort: it learns from sparse rewards, avoids distillation, and leaves the base policy untouched. Across eight real-world dexterous multi-fingered robotic manipulation tasks, SCORE improves average success rate from 37.8% to 89.9%, compared to 59.5% for the best baseline, and reaches success in 36.8% fewer steps than the base policy. Ultimately, through extensive experiments and ablations, we show that simulation can substantially improve real-world manipulation policies when policy optimization is appropriately constrained, introducing a new paradigm for real-to-sim-to-real policy improvement. Videos and code are available at https://weirdlabuw.github.io/score/.

</details>

---
