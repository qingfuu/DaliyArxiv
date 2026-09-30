# cs.LG | Machine Learning | 2026-09-28

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/强化学习/HySTAR_Anchored_Hypergraphs_for_Stable_Credit_Assignment_in_Cooperative_Multi-Agent_Reinforcement_Learning|HySTAR: Anchored Hypergraphs for Stable Credit Assignment in Cooperative Multi-Agent Reinforcement Learning]]

![[assets/2609.31531_figure.png|800]]

- **arXiv**: [2609.31531](https://arxiv.org/abs/2609.31531)
- **PDF**: https://arxiv.org/pdf/2609.31531
- **详细分析**: [[20_Research/Papers/强化学习/HySTAR_Anchored_Hypergraphs_for_Stable_Credit_Assignment_in_Cooperative_Multi-Agent_Reinforcement_Learning|HySTAR: Anchored Hypergraphs for Stable Credit Assignment in Cooperative Multi-Agent Reinforcement Learning]]
- **作者**: Xinglong Luo, Yuding Zhang, Yuheng Kuang, Shuxuan Yuan, Zhenni Zeng, Weiqiang Zhu, Zhenhai Ji, Zhengning Wang
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《HySTAR: Anchored Hypergraphs for Stable Credit Assignment in Cooperative Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-agent reinforcement learning under partial observability and shared rewards requires assigning team outcomes to individual agents and high-order coalitions. A MAPPO-style critic compresses joint behavior into one global value, while critics that dynamically reconstruct the grouping topology change the mapping from agents and coalitions to value components as interactions or active agents evolve. We refer to this inconsistency as structural target drift. We introduce HySTAR, a MAPPO-based framework that separates adaptive representation learning from a temporally consistent high-order value-decomposition basis. HySTAR anchors an overlapping sparse hypergraph as a uniformly covered decomposition scaffold, uses a spatiotemporal encoder to represent physical and task-dependent interactions, and combines temporal and structural relevance to construct agent-specific advantages. Experiments on SMAC, GRF, Traffic Junction, and MPE demonstrate consistent improvements over MAPPO-style, value-factorization, and dynamic-grouping baselines. On the hardest SMAC settings, HySTAR achieves relative gains of 16.7\% over MAPPO and 15.6\% over HYGMA, ranks first on all six GRF scenarios, reduces Traffic Junction convergence epochs by up to 40.2\% relative to MAGIC, and obtains the highest MPE episode rewards. Controlled topology, agent-death, neighborhood, and parameter analyses support the benefit of anchoring the decomposition scaffold while adapting the propagated representations.

</details>

---

### [[20_Research/Papers/大模型/WorldTS_World_Modeling_for_Multimodal_Covariate-aware_Time_Series_Forecasting|WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting]]

![[assets/2609.31162_figure.png|800]]

- **arXiv**: [2609.31162](https://arxiv.org/abs/2609.31162)
- **PDF**: https://arxiv.org/pdf/2609.31162
- **详细分析**: [[20_Research/Papers/大模型/WorldTS_World_Modeling_for_Multimodal_Covariate-aware_Time_Series_Forecasting|WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting]]
- **作者**: Yuhan Zhu, Xiangfei Qiu, Hanyin Cheng, Wangmeng Shen, Chenjuan Guo, Bin Yang, Jilin Hu, Christian S. Jensen
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 强化学习
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.16，世界模型 0.36）
- **关联关键词**: Multimodal, WorldModel, Systems

#### 研究背景与动机

《WorldTS: World Modeling for Multimodal Covariate-aware Time Series Forecasting》归入 大模型、世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GCGNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Time series forecasting is typically framed as learning a direct mapping from historical to future observations in the observation space. However, sequences of observations generally provide only a partial view of the dynamics of the underlying system, with future observations being shaped by latent dynamics. Recent latent-space forecasting methods thus achieve improved performance by predicting future observations from latent-space representations of historical observations rather than directly forecasting future observations in the observation space. Next, while future observations are also shaped by external factors, how to incorporate external, often multimodal, information into forecasting, so that it can shape latent-state formation and evolution directly, remains underexplored. We propose WorldTS, a world-modeling based forecasting framework that integrates multimodal covariates directly into the forecasting to further improve forecasting performance. Specifically, WorldTS employs a two-stage training strategy. First, it learns forecasting-relevant latent state dynamics conditioned on multimodal covariates, yielding encoded future states. Next, the learned state dynamics are frozen, and an observation decoder is trained to map the predicted future states back to future observations. Extensive experiments on 21 real-world datasets offer insight into WorldTS and its effectiveness.

</details>

---

### [[20_Research/Papers/强化学习/Precision_at_Speed_Sample-Efficient_Online_Model-Based_Reinforcement_Learning_for_Hydraulic_Excavator_Control|Precision at Speed: Sample-Efficient Online Model-Based Reinforcement Learning for Hydraulic Excavator Control]]

![[assets/2609.31025_figure.png|800]]

- **arXiv**: [2609.31025](https://arxiv.org/abs/2609.31025)
- **PDF**: https://arxiv.org/pdf/2609.31025
- **详细分析**: [[20_Research/Papers/强化学习/Precision_at_Speed_Sample-Efficient_Online_Model-Based_Reinforcement_Learning_for_Hydraulic_Excavator_Control|Precision at Speed: Sample-Efficient Online Model-Based Reinforcement Learning for Hydraulic Excavator Control]]
- **作者**: Claudio Canales, Fang Nan, Marco Hutter, Javier Ruiz-del-Solar
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 0.96，世界模型 0.96）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Precision at Speed: Sample-Efficient Online Model-Based Reinforcement Learning for Hydraulic Excavator Control》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precise, high-speed control remains challenging for robots with complex actuation dynamics. Learning directly on hardware is further constrained by the cost of real-world interaction. We present an online model-based reinforcement learning framework that learns a probabilistic dynamics ensemble model from scratch for sampling-based model predictive control. A precision-gated contouring objective conditions the progress reward on path accuracy, prioritizing precision over speed. In a data-driven excavator simulator, the framework achieves higher sample efficiency than the evaluated model-based reinforcement learning baselines. We validate the framework by learning directly on an 11.5-ton Menzi Muck M445 hydraulic excavator, without demonstrations or simulation pretraining. After 20 minutes of interaction, the controller reaches tracking accuracy comparable to prior learned controllers trained on 100-150 minutes of data. After 40 minutes, it sustains sub-centimeter mean path error at high operating speeds.

</details>

---

### [[20_Research/Papers/强化学习/Probabilistic_Robustness-driven_Universal_Adversarial_Perturbations_with_Explainability_against_Deep_Reinforcement_Learning-based_Intrusion_|Probabilistic Robustness-driven Universal Adversarial Perturbations with Explainability against Deep Reinforcement Learning-based Intrusion Detection System]]

![[assets/2609.30605_figure.png|800]]

- **arXiv**: [2609.30605](https://arxiv.org/abs/2609.30605)
- **PDF**: https://arxiv.org/pdf/2609.30605
- **详细分析**: [[20_Research/Papers/强化学习/Probabilistic_Robustness-driven_Universal_Adversarial_Perturbations_with_Explainability_against_Deep_Reinforcement_Learning-based_Intrusion_|Probabilistic Robustness-driven Universal Adversarial Perturbations with Explainability against Deep Reinforcement Learning-based Intrusion Detection System]]
- **作者**: Hongsen Zhang, Lu Zhang, Mingjing Xu, Yi Zhang, Gregory Epiphaniou, Carsten Maple
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.92（加权：强化学习 1.76，世界模型 0.16）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《Probabilistic Robustness-driven Universal Adversarial Perturbations with Explainability against Deep Reinforcement Learning-based Intrusion Detection System》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) enables adaptive intrusion detection in dynamic network environments but also exposes intrusion detection systems (IDS) to adversarial threats such as universal adversarial perturbations (UAPs), which apply a single input-agnostic perturbation to degrade detection performance across traffic. Probabilistic Robustness (PR), as a post-hoc evaluation metric, provides a principled, population-level measure of adversarial impact that conceptually aligns with the universality objective of UAPs, i.e., PR quantifies the prevalence of misclassification in the input space, making it a natural signal for guiding UAP generation. Hence, we propose PR-based UAP, which represents the first integration of an explicit PR-driven objective into generating UAPs against DRL-based IDS. Building on this formulation, we introduce PX-UAP, which leverages explainable artificial intelligence (XAI) to guide perturbation shaping under realistic domain constraints, and provides a rigorous theoretical analysis of its design. Extensive experiments demonstrate that PX-UAP consistently outperforms state-of-the-art UAP methods in attack effectiveness.

</details>

---

### [[20_Research/Papers/具身智能/Reinforcement_Learning_of_Communication_in_a_Mesh_of_Small_Language_Models|Reinforcement Learning of Communication in a Mesh of Small Language Models]]

![[assets/2609.30578_first_page.png|800]]

- **arXiv**: [2609.30578](https://arxiv.org/abs/2609.30578)
- **PDF**: https://arxiv.org/pdf/2609.30578
- **详细分析**: [[20_Research/Papers/具身智能/Reinforcement_Learning_of_Communication_in_a_Mesh_of_Small_Language_Models|Reinforcement Learning of Communication in a Mesh of Small Language Models]]
- **作者**: Mehmet Kerem Turkcan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 具身智能, 世界模型
- **相关性评分**: 1.72（加权：具身智能 0.3，大模型 0.3，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Reinforcement Learning of Communication in a Mesh of Small Language Models》归入 强化学习、大模型、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SwarmBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language models gain accuracy from more compute at test time, but majority voting over independent samples saturates: as samples grow, the vote converges to the model's most frequent answer. Communication can add what sampling cannot: an agent that solves a problem can pass the key step to the others. We present TalkMesh, a decentralized mesh of small language model agents that learns when and what to communicate. Each agent samples a proposal and scores it with a trained confidence head. The most confident agent broadcasts a hint; agents below a confidence threshold revise, keeping each revision that outscores its proposal. Gossip consensus approximates the vote weighted by confidence without a coordinator. A talk policy, trained with group relative policy optimization on the change in correctness after revision, writes hints and revisions. With three agents, which together generate at most six outputs, the mesh reaches the accuracy of majority voting over 32 samples with each of three models. Trained with at most 8 agents and evaluated with 32, it raises accuracy from 0.568 under self-consistency to 0.705 (Qwen3.5-0.8B, GSM8K) and from 0.492 to 0.722 (SmolLM3-3B, MATH-500). When 4 of 8 agents collude on a wrong answer with fabricated confidence and poisoned hints, majority vote accuracy falls to 0.000 (Qwen3.5-0.8B, GSM8K). A defended mesh, whose agents rescore solutions with their own confidence heads, retains 0.507. Across reasoning, embodied coordination, and traffic signal control, messages improve a decision when the acting agent cannot observe the information it requires and another agent can send it.

</details>

---

### [[20_Research/Papers/强化学习/From_Weak_Data_to_Strong_Policy_Q-Targets_Enable_Provable_In-Context_Reinforcement_Learning|From Weak Data to Strong Policy: Q-Targets Enable Provable In-Context Reinforcement Learning]]

![[assets/2609.30391_figure.jpg|800]]

- **arXiv**: [2609.30391](https://arxiv.org/abs/2609.30391)
- **PDF**: https://arxiv.org/pdf/2609.30391
- **详细分析**: [[20_Research/Papers/强化学习/From_Weak_Data_to_Strong_Policy_Q-Targets_Enable_Provable_In-Context_Reinforcement_Learning|From Weak Data to Strong Policy: Q-Targets Enable Provable In-Context Reinforcement Learning]]
- **作者**: Yichen Lin, Xuyuan Xiong, Xue Wang, Xiangfu Meng, Mike Mingcheng Wei, Tao Yao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《From Weak Data to Strong Policy: Q-Targets Enable Provable In-Context Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D4RL, ICRL, Meta-RL, PEARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing in-context reinforcement learning methods mainly pretrain Transformers with supervised behavior-prediction objectives. This enables task inference from context, but makes the learned policy strongly depend on the quality of offline actions: when trajectories are weak or suboptimal, imitation itself becomes a biased learning signal. We propose Q-Target Pretrained Transformers (QTPT), which keeps the context-conditioned Transformer architecture but replaces behavior cloning with a Bellman-style Q-target objective. QTPT therefore learns to use rewards and transitions in the context to estimate action values, rather than simply imitating the behavior policy. We theoretically analyze QTPT in stochastic linear bandits and finite-horizon MDPs, showing stronger robustness to data quality than supervised pretraining. Empirically, QTPT improves over supervised behavior prediction on controlled RL benchmarks with random or suboptimal data, and we examine extensions to D4RL Kitchen and AntMaze. Supplementary experiments evaluate backbone robustness, meta-RL comparisons, task-coherent context, and unsupported-action value overestimation. These comparisons distinguish the benefits of Q-target pretraining from the remaining limitations of offline coverage.

</details>

---

### [[20_Research/Papers/大模型/HybridInfer_Thermal-Aware_Reinforcement-Learning_Tier_Routing_for_On-Device,_Edge,_and_Cloud_LLM_Inference|HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing for On-Device, Edge, and Cloud LLM Inference]]

![[assets/2609.30270_figure.png|800]]

- **arXiv**: [2609.30270](https://arxiv.org/abs/2609.30270)
- **PDF**: https://arxiv.org/pdf/2609.30270
- **详细分析**: [[20_Research/Papers/大模型/HybridInfer_Thermal-Aware_Reinforcement-Learning_Tier_Routing_for_On-Device,_Edge,_and_Cloud_LLM_Inference|HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing for On-Device, Edge, and Cloud LLM Inference]]
- **作者**: Simran Koul
- **cs 子类**: cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 0.92（加权：大模型 0.4，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《HybridInfer: Thermal-Aware Reinforcement-Learning Tier Routing for On-Device, Edge, and Cloud LLM Inference》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-device inference with small language models keeps user data local, works offline, and incurs no per-query cost, so the on-device tier is preferred when it is adequate. It is thermally constrained, however, and I find the constraint is sharper than a slowdown: on a flagship Snapdragon device, sustained on-device generation destabilizes the GPU inference runtime, which crashes or silently wedges after a few consecutive queries. The failure lies in the current toolchain (OpenCL kernel compilation and long-prompt prefill on the mobile GPU), recurs even when the device is cool, and is worst for long generations. Multi-tier routers across on-device, edge, and cloud models can relieve this pressure, but existing routers are thermal-blind and typically evaluated in simulation or on non-mobile hardware. I present HybridInfer, a thermal-aware reinforcement-learning router for a three-tier hierarchy (on-device Llama 3.2 3B, edge Llama 3.1 8B with retrieval, cloud GPT-4o) that uses the phone's thermal headroom and a query-complexity estimate as state and selects a tier by an offline-trained Q-learning policy. Its reward trades quality against latency, cost, and a thermal penalty, plus a locality bonus crediting on-device execution. I show this bonus is a precondition for thermal-aware routing: without it the optimal policy offloads every query. On a real Android benchmark of 210 prompts, the learned router attains significantly higher quality than two hand-tuned heuristics (paired Wilcoxon, p &lt; 0.02) at the lowest cost of any adaptive condition. Always-on-device conditions match per-query quality on servable queries but are three to six times slower and fail on long queries, so routing wins on latency, reliability, and coverage rather than quality. To my knowledge this is the first use of on-device thermal headroom to select among LLM inference tiers of differing capability on real hardware.

</details>

---
