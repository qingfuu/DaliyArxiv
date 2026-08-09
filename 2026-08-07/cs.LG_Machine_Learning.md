# cs.LG | Machine Learning | 2026-08-07

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/强化学习/Stochastic_Dynamics_on_Persistence_Diagram_Space_via_Reinforcement_Learning|Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning]]

![[assets/2608.06276_first_page.png|800]]

- **arXiv**: [2608.06276](https://arxiv.org/abs/2608.06276)
- **PDF**: https://arxiv.org/pdf/2608.06276
- **详细分析**: [[20_Research/Papers/强化学习/Stochastic_Dynamics_on_Persistence_Diagram_Space_via_Reinforcement_Learning|Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning]]
- **作者**: Farzana Nasrin
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Stochastic Dynamics on Persistence Diagram Space via Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistence diagrams (PDs) provide stable and interpretable summaries of multiscale topological structure. While substantial progress has been made in the statistical analysis of PDs, existing literature often treats diagrams as static objects and provide limited frameworks for probabilistic modeling and stochastic evolution on PD space. We introduce a reinforcement learning framework for stochastic dynamics on PD space, where diagrams evolve through topology aware local edit operations. The dynamics define controlled Markov processes on spaces of finite PDs with variable cardinality. We establish conditions under which the induced Markov chains are irreducible, aperiodic, and geometrically ergodic, implying the existence of unique stationary probability laws on PD space. To guide the dynamics toward scientifically relevant topological targets, we formulate objectives that encompass distribution matching, task specific topological statistics, and structure-preserving compression. The resulting rewards balance task specific distributional targets, diagram fidelity, and complexity reduction, and yield a framework for adaptive topological simplification and probabilistic modeling. Experiments on synthetic and neuroimaging PDs demonstrate that the proposed framework can preserve dominant topological structure while reducing diagram complexity.

</details>

---

### [[20_Research/Papers/大模型/MetaboLLM_a_metabolomics-specialized_large_language_model_for_biochemical_knowledge_integration_and_predictive_metabolite_graph_construction|MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction]]

![[assets/2608.06253_first_page.png|800]]

- **arXiv**: [2608.06253](https://arxiv.org/abs/2608.06253)
- **PDF**: https://arxiv.org/pdf/2608.06253
- **详细分析**: [[20_Research/Papers/大模型/MetaboLLM_a_metabolomics-specialized_large_language_model_for_biochemical_knowledge_integration_and_predictive_metabolite_graph_construction|MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction]]
- **作者**: Dohyun Ku, Min Gu Kwak, Francisco J. Pasquel, Jing Li
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《MetaboLLM: a metabolomics-specialized large language model for biochemical knowledge integration and predictive metabolite graph construction》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Metabolomics knowledge is distributed across heterogeneous resources and remains difficult to translate into predictive representations. We developed MetaboLLM, a metabolomics-specialized large language model adapted through continual pretraining, supervised fine-tuning, and structured retrieval, together with MetaboLLM-GIN, which converts generated biochemical descriptions into metabolite graphs for patient-level prediction using a graph isomorphism network. Across four backbone families, MetaboLLM outperformed corresponding base and medically adapted models on metabolomics knowledge, relational, and description tasks, and transferred to an external public benchmark. MetaboLLM-GIN achieved the highest AUC for stress hyperglycemia prediction after coronary artery bypass grafting (0.8616) and postmenopausal hormone-regimen classification (0.8123), outperforming conventional models, alternative graph constructions, and graphs generated from unadapted or non-retrieval LLM configurations. Model interpretation further produced biologically meaningful findings in both applications. These results show that domain-specialized language models can organize heterogeneous biochemical knowledge into predictive and interpretable metabolite graph representations.

</details>

---

### [[20_Research/Papers/强化学习/Hybrid-Adaptive_Thread_Tuning_to_Mitigate_Simulation_Execution_Bottlenecks_in_High-Performance_Reinforcement_Learning_Inference|Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinforcement Learning Inference]]

![[assets/2608.06025_figure.png|800]]

- **arXiv**: [2608.06025](https://arxiv.org/abs/2608.06025)
- **PDF**: https://arxiv.org/pdf/2608.06025
- **详细分析**: [[20_Research/Papers/强化学习/Hybrid-Adaptive_Thread_Tuning_to_Mitigate_Simulation_Execution_Bottlenecks_in_High-Performance_Reinforcement_Learning_Inference|Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinforcement Learning Inference]]
- **作者**: Jiming Su, Hantao Hua, Lujia Yin, Yiping Yao, Feng Zhu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Hybrid-Adaptive Thread Tuning to Mitigate Simulation Execution Bottlenecks in High-Performance Reinforcement Learning Inference》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SiL-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In simulation-in-the-loop decision-making systems, reinforcement learning (RL) inference is often constrained by simulator-side execution overhead, where workloads are highly dynamic and sensitive to runtime thread configurations. Existing multithreaded strategies struggle to match thread resources before or during execution, causing resource contention, scheduling overhead, and reduced throughput. Through empirical analysis, we identify the ratio of task execution time to scheduling time as the key factor determining the optimal thread count. Building on this insight, we propose AutoThread, a hybrid adaptive thread-tuning method for mitigating simulation bottlenecks in RL inference. AutoThread employs a Physics-Informed Neural Operator (PINO) as a thread-count predictor and incorporates a finite-source M/M/1 queueing model to constrain and guide prediction, enabling fast and accurate estimation under dynamic workloads. It further performs load-aware online fine-tuning to compensate for prediction errors and refine resource allocation. Experiments show that AutoThread improves average speedup by 18.4\% over static strategies, achieves average throughput of 1.7x and 1.8x that of XGBoost and Reinforcer, respectively, and reduces execution time by up to 83.8\% compared with state-of-the-art methods. Our code and dataset are publicly available at https://github.com/suchenjm/AutoThread.

</details>

---

### [[20_Research/Papers/强化学习/Observation-Grounded_Self-Predictive_Reinforcement_Learning_for_Visual_Continuous_Control|Observation-Grounded Self-Predictive Reinforcement Learning for Visual Continuous Control]]

![[assets/2608.05989_figure.png|800]]

- **arXiv**: [2608.05989](https://arxiv.org/abs/2608.05989)
- **PDF**: https://arxiv.org/pdf/2608.05989
- **详细分析**: [[20_Research/Papers/强化学习/Observation-Grounded_Self-Predictive_Reinforcement_Learning_for_Visual_Continuous_Control|Observation-Grounded Self-Predictive Reinforcement Learning for Visual Continuous Control]]
- **作者**: Xinwei Liu, Junyuan Liang, Jianting Zhang, Wuhui Chen
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 世界模型
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.96，世界模型 0.16，机器人 0.5）
- **关联关键词**: RL

#### 研究背景与动机

《Observation-Grounded Self-Predictive Reinforcement Learning for Visual Continuous Control》归入 强化学习、具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OFENet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sample-efficient policy learning from pixels is a long-standing challenge in reinforcement learning (RL). Recent dynamics-based representation learning methods have significantly improved the sample efficiency of model-free visual RL by learning dynamics-aware representations through auxiliary prediction performed either in latent space (self-prediction) or observation space (observation prediction). However, state-of-the-art methods from both categories still struggle on challenging visual control tasks when training data is limited. We posit that relying on either predictive objective alone may be insufficient. In contrast, observation prediction grounds learned representations in observation-level dynamics, but does not directly regularize the temporal predictability of latent representations over extended horizons. In this paper, we propose Observation-Grounded Self-Predictive Representations (OG-SPR), a model-free visual RL algorithm for continuous control that learns representations that are both temporally predictive in latent space and grounded in observation-level dynamics. OG-SPR incorporates two core auxiliary objectives: multi-step latent self-prediction and next-observation prediction. We empirically show that directly imposing latent self-prediction on the shared representation may over-constrain it and does not necessarily improve performance. To address this issue, OG-SPR introduces two lightweight adapters for latent self-prediction, allowing the shared representation to benefit from temporally predictive signals without being forced to directly satisfy the self-prediction objective. Experiments on 28 visual control tasks from the DeepMind Control Suite show that OG-SPR improves aggregate performance over state-of-the-art self-predictive and observation-predictive RL methods, with particularly pronounced gains in challenging domains such as dog and humanoid.

</details>

---

### [[20_Research/Papers/世界模型/Quantum-Structured_World_Models_(QSWMs)_for_Predictive_Latent_Dynamics|Quantum-Structured World Models (QSWMs) for Predictive Latent Dynamics]]

![[assets/2608.05371_figure.png|800]]

- **arXiv**: [2608.05371](https://arxiv.org/abs/2608.05371)
- **PDF**: https://arxiv.org/pdf/2608.05371
- **详细分析**: [[20_Research/Papers/世界模型/Quantum-Structured_World_Models_(QSWMs)_for_Predictive_Latent_Dynamics|Quantum-Structured World Models (QSWMs) for Predictive Latent Dynamics]]
- **作者**: Hailong Jiang, Emran Hossain, Feng Yu, Jianfeng Zhu, Guilin Zhang, Wulan Guo
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.72（加权：强化学习 0.16，世界模型 1.56）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Quantum-Structured World Models (QSWMs) for Predictive Latent Dynamics》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：QRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models learn latent states that summarize interaction histories, evolve over time, and support prediction, simulation, or planning. Most existing world models represent these states using classical vectors, probability distributions, recurrent hidden states, or transformer activations. In this paper, we introduce Quantum-Structured World Models (QSWMs), a quantum-inspired framework for predictive world modeling with structured latent states, latent transition operators, and measurement-inspired decoding maps. We study whether mathematical structures inspired by quantum theory, such as complex-valued representations and density-matrix-like latents, provide useful inductive biases for world modeling. We establish three foundational properties: classical inclusion, predictive sufficiency, and structured compactness. We then instantiate complex-valued and density-matrix-like QSWM variants and evaluate them on elementary cellular automata against strong classical baselines. Results show promising local predictive potential for complex-valued QSWMs, while also revealing limitations in long-horizon rollout, density-matrix variants

</details>

---

### [[20_Research/Papers/大模型/When_Do_Corrective_Features_Help_An_Agent_for_Corrective_Feature_Discovery_on_Black-Box_Forecasters|When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters]]

![[assets/2608.05207_figure.png|800]]

- **arXiv**: [2608.05207](https://arxiv.org/abs/2608.05207)
- **PDF**: https://arxiv.org/pdf/2608.05207
- **详细分析**: [[20_Research/Papers/大模型/When_Do_Corrective_Features_Help_An_Agent_for_Corrective_Feature_Discovery_on_Black-Box_Forecasters|When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters]]
- **作者**: Fangxin Wang, Ziyi Zhang, Diyi Zhuang, Langzhou He, Shiyu Wang, Baichuan Mo, Philip S. Yu
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《When Do Corrective Features Help? An Agent for Corrective Feature Discovery on Black-Box Forecasters》归入 大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frozen pretrained forecasters often fail in structured, recurring ways that are costly to repair through fine-tuning. We study corrective feature discovery: mining interpretable features of a frozen forecaster's residual to drive a lightweight post-hoc corrector. Prior automated feature engineering models the data-generating process; corrective features instead model the model-failure process. We present CRAFTER (Corrective Residual Agent with Feature-based Temporal Exploration and Reasoning), which keeps the backbone frozen and mines its residual with two complementary generators: a compositional search over the raw input channels, and a large language model (LLM) that proposes named feature combinations, binary flags, and short executable code. A single validation-grounded gate accepts or rejects every candidate regardless of its origin, and a validation-selected corrector applies the accepted features or leaves the forecast unchanged. This source-agnostic pipeline also allows prior feature-engineering systems to be evaluated under identical conditions, making CRAFTER an instrument for attributing forecast improvements to the feature source alone. Across six public datasets and six frozen backbones, CRAFTER surpasses every dedicated feature-engineering system at every feature budget, roughly doubling the improvement achieved by the corrector alone and reducing the error of the weakest backbones by up to 27%. These gains are robust across different LLM backends and persist even when applied on top of fine-tuned backbones.

</details>

---
