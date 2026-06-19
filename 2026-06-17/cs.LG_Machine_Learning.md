# cs.LG | Machine Learning | 2026-06-17

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Minimum_Zero-Forcing_Sets|Deep Reinforcement Learning for Minimum Zero-Forcing Sets]]

![[assets/2606.18106_figure.png|800]]

- **arXiv**: [2606.18106](https://arxiv.org/abs/2606.18106)
- **PDF**: https://arxiv.org/pdf/2606.18106
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning_for_Minimum_Zero-Forcing_Sets|Deep Reinforcement Learning for Minimum Zero-Forcing Sets]]
- **作者**: Steve Halley, Maurício Gruppi
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Deep Reinforcement Learning for Minimum Zero-Forcing Sets》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper explores the problem of finding the minimum zero-forcing set on undirected graphs and proposes an adapted machine-learning framework to solve the problem. The minimum zero-forcing set problem is a graph coloring problem where the color of an initial set of nodes propagates throughout a network. The set of nodes is zero-forcing if it forces all uncolored nodes to change color under the constraint of the color-change rule. There are several applications to this problem across different domains such as network science, network control, and designing logical circuits. Finding the minimum zero-forcing set is shown to be NP-hard. We propose a reinforcement learning framework, SD-ZFS, that adapts the S2V-DQN architecture to the ZFS problem. We train several models on this adapted framework and analyze the performance across graph datasets that have varying structures. We evaluate how the models trained on the framework generalize, scale, and transfer to different network types. The results demonstrate the effectiveness of the framework when compared against the optimal solution and greedy heuristic. We provide further insight into how the ZFS problem can be solved through machine-learning and the influence of network structure on the problem.

</details>

---

### [[20_Research/Papers/大模型/OmniPlan_An_Adaptive_Framework_for_Timely_and_Near-Optimal_Network_Planning_Optimization|OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization]]

![[assets/2606.18105_figure.png|800]]

- **arXiv**: [2606.18105](https://arxiv.org/abs/2606.18105)
- **PDF**: https://arxiv.org/pdf/2606.18105
- **详细分析**: [[20_Research/Papers/大模型/OmniPlan_An_Adaptive_Framework_for_Timely_and_Near-Optimal_Network_Planning_Optimization|OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization]]
- **作者**: Longlong Zhu, Jiashuo Yu, Zedi Chen, Yuhan Wu, Zhifan Jiang, Yuchen Xian, Yimeng Liu, Jiajie Su, Shaopeng Zhou, Xingyuan Li, Hongyan Liu, Xuan Liu...
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.3，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《OmniPlan: An Adaptive Framework for Timely and Near-Optimal Network Planning Optimization》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Network planning optimization is a fundamental problem across diverse domains, including transportation systems, communication networks, and power grids. It requires simultaneous optimization of multiple competing objectives under complex constraints. Existing network planning optimization frameworks rely on mixed integer programming (MIP) solvers, heuristics, and deep reinforcement learning (DRL) models to compute planning decisions. However, they lack effective adaptability to diverse and dynamic user intents, thus leading to the trade-off between execution time and optimality. In this paper, we propose OmniPlan, an adaptive framework that achieves both timeliness and near-optimality in network planning optimization. To achieve the adaptability lacking in existing solutions, OmniPlan employs a large language model (LLM)-based interpreter to convert heterogeneous natural-language intents into a unified and quantifiable user-preference vector. Then it employs a mixture-of-experts architecture that integrates MIP solvers, heuristics, and DRL models as specialized experts, where OmniPlan adapts to diverse intents by dynamically selecting timely and near-optimal experts. Finally, it incorporates a DRL-based expert configuration module that fine-tunes optimization objective weights to align planning decisions with user-specific preferences. We evaluate OmniPlan with a representative real-world workload, i.e., distributed machine learning (ML), where we leverage OmniPlan to offload a wide spectrum of ML inference tasks, e.g., decision trees, SVM, naive Bayes, XGBoost, and random forests, onto a network of hardware devices. Our experiments on a real-world testbed indicate that OmniPlan achieves near-optimal and low-execution-time offloading for real-world ML inference tasks, reducing latency by up to 97.8\% and network device resource consumption by up to 11.5\%.

</details>

---

### [[20_Research/Papers/大模型/From_Reasoning_Traces_to_Reusable_Modules_Understanding_Compositional_Generalization_in_Language_Model_Reasoning|From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning]]

![[assets/2606.18089_figure.jpg|800]]

- **arXiv**: [2606.18089](https://arxiv.org/abs/2606.18089)
- **PDF**: https://arxiv.org/pdf/2606.18089
- **详细分析**: [[20_Research/Papers/大模型/From_Reasoning_Traces_to_Reusable_Modules_Understanding_Compositional_Generalization_in_Language_Model_Reasoning|From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning]]
- **作者**: Lingjing Kong, Xin Liu, Guangyi Chen, Martin Q. Ma, Xiangchen Song, Yuekai Sun, Mikhail Yurochkin, Taylor W. Killian, Ruslan Salakhutdinov, Kun Zhang, Eric P. Xing, Zhengzhong Liu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization in Language Model Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training pipelines that combine supervised fine-tuning (SFT) with reinforcement learning (RL) have emerged as the key recipe for transforming large language models (LLMs) into robust reasoners. We argue that this combined success is driven by compositional generalization, which we formalize through a hierarchical latent selection model. In this framework, reasoning traces are generated by a cascade of discrete latent selection variables corresponding to reusable atomic modules, including both skills (local operations) and routing mechanisms (how intermediate information is selected, reused, and composed). Within this model, we theoretically show that SFT and RL play asymmetric, complementary roles: SFT supplies the raw module materials in compositional traces, and RL decomposes those traces to identify the latent atomic modules and enable compositional generalization. We design controlled experiments to validate this theory. Our results demonstrate that RL can extract atomic modules from compound traces supplied by SFT and recombine them to solve new configurations. Moreover, we find that training on compound traces yields stronger generalization than training on isolated atomic modules. Finally, we investigate the relationship between SFT and RL data and identify an effective protocol in which SFT ensures coverage of all atomic modules through compositional traces, while RL focuses on novel compositions outside the SFT support to drive exploration.

</details>

---

### [[20_Research/Papers/具身智能/Uncertainty_Quantification_for_Flow-Based_Vision-Language-Action_Models|Uncertainty Quantification for Flow-Based Vision-Language-Action Models]]

![[assets/2606.18043_figure.png|800]]

- **arXiv**: [2606.18043](https://arxiv.org/abs/2606.18043)
- **PDF**: https://arxiv.org/pdf/2606.18043
- **详细分析**: [[20_Research/Papers/具身智能/Uncertainty_Quantification_for_Flow-Based_Vision-Language-Action_Models|Uncertainty Quantification for Flow-Based Vision-Language-Action Models]]
- **作者**: Ralf Römer, Maximilian Seeliger, Saida Liu, Ben Sturgis, Marco Bagatella, Daniel Marta, Andreas Krause, Angela P. Schoellig
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Uncertainty Quantification for Flow-Based Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) combine vision-language backbones with expressive generative action heads trained via flow matching on large-scale robotic datasets. Despite their strong empirical performance in robotic manipulation, VLAs lack mechanisms to quantify confidence in their predictions and to detect when their actions may be unreliable. This presents a critical limitation for real-world deployment in non-stationary environments, where models inevitably encounter scenarios outside their pretraining distribution and may fail without warning. To address this, we derive an efficient method for quantifying epistemic uncertainty in flow-matching models by leveraging velocity-field disagreement (VFD) across a small ensemble. We successfully use this uncertainty estimate for failure detection during deployment and active fine-tuning of flow-based VLAs. To this end, we propose SAVE, a framework for uncertainty-guided active multitask fine-tuning that reduces the number of costly expert demonstrations required to adapt VLAs to new tasks. Through extensive experiments on the LIBERO benchmark, we demonstrate that VFD yields better-calibrated uncertainty estimates predictive of downstream performance, that VFD achieves strong performance in detecting failures, and that uncertainty-guided data acquisition with SAVE requires at least 22% fewer samples than baselines. In summary, our work shows that quantifying epistemic uncertainty in flow-based VLAs improves both failure awareness and adaptation. Project website: this http URL .

</details>

---

### [[20_Research/Papers/强化学习/Continuous-time_Optimal_Stopping_through_Deep_Reinforcement_Learning|Continuous-time Optimal Stopping through Deep Reinforcement Learning]]

![[assets/2606.17545_figure.png|800]]

- **arXiv**: [2606.17545](https://arxiv.org/abs/2606.17545)
- **PDF**: https://arxiv.org/pdf/2606.17545
- **详细分析**: [[20_Research/Papers/强化学习/Continuous-time_Optimal_Stopping_through_Deep_Reinforcement_Learning|Continuous-time Optimal Stopping through Deep Reinforcement Learning]]
- **作者**: Cosmin Borsa, Michael Ludkovski
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Continuous-time Optimal Stopping through Deep Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation based solvers for optimal stopping problems must discretize the stopping decision. Under classical dynamic programming, a coarse exercise grid with only a few stopping opportunities can materially undervalue the optimal expected reward, whereas on a very fine grid, approximation errors accumulate through the backward recursion. To remove this limitation, we develop a new reinforcement-learning inspired algorithm that enables us to learn the exercise rule at arbitrarily fine time resolution. Our CARLOS (Continuous-time Adaptive Reinforcement Learning for Optimal Stopping) algorithm utilizes an aggregate deep neural network (ADNN) to learn a joint space-time decision boundary. Starting from a coarse time grid, we progressively increase the frequency of stopping opportunities, while in parallel training the ADNN to refine its timing-value estimates. We moreover design an adaptive sampling strategy that gradually concentrates training effort near the stopping boundary. Benchmarked results show that CARLOS delivers higher prices than existing Bermudan solvers, approaching the American upper bound, and achieves high computational efficiency relative to non-RL comparators.

</details>

---

### [[20_Research/Papers/大模型/Learning_to_Refine_Hidden_States_for_Reliable_LLM_Reasoning|Learning to Refine Hidden States for Reliable LLM Reasoning]]

![[assets/2606.17524_figure.png|800]]

- **arXiv**: [2606.17524](https://arxiv.org/abs/2606.17524)
- **PDF**: https://arxiv.org/pdf/2606.17524
- **详细分析**: [[20_Research/Papers/大模型/Learning_to_Refine_Hidden_States_for_Reliable_LLM_Reasoning|Learning to Refine Hidden States for Reliable LLM Reasoning]]
- **作者**: Chia-Hsuan Hsu, Jui-Ming Yao
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Learning to Refine Hidden States for Reliable LLM Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HotpotQA, PubMedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models show strong reasoning ability, but their internal reasoning process can remain unstable in complex multi-step settings, where early hidden-state errors may propagate to incorrect predictions. We propose ReLAR, a reinforcement-guided latent refinement framework that iteratively updates hidden representations before decoding. ReLAR maintains a compact latent reasoning state and uses learned depth and action controllers to adaptively determine both the number and direction of refinement steps. The controllers are trained with a policy gradient objective based on step-wise likelihood improvement, enabling efficient input-dependent reasoning without explicit chain-of-thought generation. Experiments on medical, mathematical, multi-hop reasoning, and open-ended generation benchmarks show that ReLAR improves accuracy, generation quality, and reasoning stability with substantially lower inference overhead than explicit reasoning baselines.

</details>

---

### [[20_Research/Papers/强化学习/Memory-Efficient_Meta-Reinforcement_Learning_for_Adaptive_Safety-Critical_Control_in_Adversarial_Spacecraft_Proximity_Operations|Memory-Efficient Meta-Reinforcement Learning for Adaptive Safety-Critical Control in Adversarial Spacecraft Proximity Operations]]

![[assets/2606.17414_figure.png|800]]

- **arXiv**: [2606.17414](https://arxiv.org/abs/2606.17414)
- **PDF**: https://arxiv.org/pdf/2606.17414
- **详细分析**: [[20_Research/Papers/强化学习/Memory-Efficient_Meta-Reinforcement_Learning_for_Adaptive_Safety-Critical_Control_in_Adversarial_Spacecraft_Proximity_Operations|Memory-Efficient Meta-Reinforcement Learning for Adaptive Safety-Critical Control in Adversarial Spacecraft Proximity Operations]]
- **作者**: Alejandro Posadas-Nava, Richard Linares, Minduli Wijayatunga
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Security, Systems

#### 研究背景与动机

《Memory-Efficient Meta-Reinforcement Learning for Adaptive Safety-Critical Control in Adversarial Spacecraft Proximity Operations》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Meta-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous spacecraft rendezvous and proximity operations (RPO) require controllers that guarantee safety under thrust constraints while minimizing fuel expenditure. Input-constrained control barrier functions (ICCBFs) provide a control method for nonlinear systems with actuation constraints that construct a forward-invariant safe set. Previous work has shown that learning class-$\mathcal{K}$ functions defining the ICCBF recursion via meta reinforcement learning (meta-RL) yields a robust, non-greedy approach to safety-critical control in RPO. This paper extends that framework further by investigating the performance of three recurrent network architectures (Long Short Term Memory (LSTM), Gated Recurrent Unit (GRU), Selective State Space Model (Mamba)) and two training algorithms (Proximal Policy Optimization (PPO) and Soft Actor Critic (SAC)) to identify the best setup for tuning ICCBF class-K functions via meta-RL. In addition to cooperative test cases, performance is evaluated in the presence of adversarial behavior where the target spacecraft behaves in a way that worsens the safety of the chaser spacecraft. Results indicate that state space models such as Mamba when used with PPO achieve superior task completion, safety, and fuel-savings compared to other architectures, across all cooperative and uncooperative scenarios tested.

</details>

---

### [[20_Research/Papers/机器人/Damage_Adaptation_in_Seconds_for_Architected_Materials|Damage Adaptation in Seconds for Architected Materials]]

![[assets/2606.17394_figure.png|800]]

- **arXiv**: [2606.17394](https://arxiv.org/abs/2606.17394)
- **PDF**: https://arxiv.org/pdf/2606.17394
- **详细分析**: [[20_Research/Papers/机器人/Damage_Adaptation_in_Seconds_for_Architected_Materials|Damage Adaptation in Seconds for Architected Materials]]
- **作者**: James Avtges, Jake Ketchum, Helena Young, Taekyoung Kim, Ryan Truby, Todd Murphey
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Damage Adaptation in Seconds for Architected Materials》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adaptation to damages and in-situ physical repairs is essential for long-term robot autonomy, yet challenging outside of narrowly defined and well-anticipated bounds. In this work we proprioceptively adapt to catastrophic damage in soft-actuated systems in under one minute. Architected materials are well equipped for adaptation: actuator failure occurs gradually rather than acutely, and damage can be described in a low-dimensional, discrete coordinate space. Surprisingly, latent damage representations plus a simple yet robust ensemble method is sufficient for adapting to unseen damage in real-time. Moreover, we identify conditions under which exponential sample complexity collapses to linear sample complexity for learned representations of architected materials, a concrete advantage over rigid components or continuum soft mechanisms. We demonstrate LEAP, our method for adaptive proprioception, via a tracing task for a 6DoF soft wrist based on Handed Shearing Auxetic (HSA) actuators. Our algorithm is able to adapt to cuts, burns, and actuator repairs, enabling simulation-free real-time adaptation that is critical for realizing the promise of soft robots outside the lab. Videos and more information are available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Performance-Driven_Environment_Abstraction_with_Multi-Timescale_Learning|Performance-Driven Environment Abstraction with Multi-Timescale Learning]]

![[assets/2606.17377_figure.png|800]]

- **arXiv**: [2606.17377](https://arxiv.org/abs/2606.17377)
- **PDF**: https://arxiv.org/pdf/2606.17377
- **详细分析**: [[20_Research/Papers/强化学习/Performance-Driven_Environment_Abstraction_with_Multi-Timescale_Learning|Performance-Driven Environment Abstraction with Multi-Timescale Learning]]
- **作者**: Yue Guan, Dipankar Maity, Panagiotis Tsiotras
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Performance-Driven Environment Abstraction with Multi-Timescale Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study performance-driven environment abstraction for decision-making in large Markov decision processes. Rather than preserving geometric or topological structure, we seek abstractions that directly optimize decision quality. We model abstraction as a controlled approximation obtained by aggregating the state space and enforcing a shared action distribution within each aggregated state. For a fixed partition, we establish a performance guarantee that separates value-function approximation error from the loss introduced by action sharing. Guided by this analysis, we develop a multi-timescale reinforcement learning framework that jointly adapts the policy and a tree-structured environment abstraction. The resulting algorithm refines and coarsens regions of the state space based on Q-value discrepancies, balancing performance against abstraction size and complexity. Empirical results demonstrate substantial state compression, improved sample efficiency, and faster replanning compared to actor-critic baselines.

</details>

---

### [[20_Research/Papers/强化学习/Decision-Driven_Geosteering_Under_Uncertainty_A_Unified_Framework_for_Sequential_Decision_Optimization|Decision-Driven Geosteering Under Uncertainty: A Unified Framework for Sequential Decision Optimization]]

![[assets/2606.17331_first_page.png|800]]

- **arXiv**: [2606.17331](https://arxiv.org/abs/2606.17331)
- **PDF**: https://arxiv.org/pdf/2606.17331
- **详细分析**: [[20_Research/Papers/强化学习/Decision-Driven_Geosteering_Under_Uncertainty_A_Unified_Framework_for_Sequential_Decision_Optimization|Decision-Driven Geosteering Under Uncertainty: A Unified Framework for Sequential Decision Optimization]]
- **作者**: Hibat Errahmen Djecta, Sergey Alyaev, Kristian Fossum, Reidar B. Bratvold, Ressi Bonti Muhammad, Apoorv Srivastava
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.92（加权：强化学习 0.76，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Decision-Driven Geosteering Under Uncertainty: A Unified Framework for Sequential Decision Optimization》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Geosteering requires navigating a well trajectory through an unknown geological configuration, while sequentially updating decisions based on indirect measurements acquired during drilling. This work presents an uncertainty-aware geosteering framework that tightly integrates particle filtering for probabilistic subsurface interpretation with value-based reinforcement learning for sequential decision-making. Geological uncertainty ahead of the drill bit is represented explicitly through a particle filter (PF), enabling belief-informed control rather than deterministic trajectory correction. The framework couples PF belief updates with belief-informed decision policies and evaluates three decision-making options that operate under identical uncertainty representations: an interpretable Approximate Dynamic Programming (ADP) scheme, a Deep Q-learning baseline, and a Dual Deep Reinforcement Learning (Dual DRL) architecture trained with a target Q-network scheme for stability, using a dueling (value/advantage) decomposition for Q-value parameterization. Beyond final placement performance, we assess policy behavior using stability-oriented metrics that quantify steering smoothness over time, providing additional operational insight into how decision policies respond as uncertainty evolves. The framework is integrated with an API for validation within an industrial geosteering simulator under realistic measurement noise and drilling constraints. Using identical geological realizations, operational limits, and reward definitions across methods, the experiments provide a controlled and high-fidelity evaluation of how alternative decision policies behave throughout the drilling process, rather than evaluating performance solely from the final well trajectory.

</details>

---

### [[20_Research/Papers/具身智能/VISTA_Scale-Aware_Visual_Navigation_via_Action_History_Conditioning|VISTA: Scale-Aware Visual Navigation via Action History Conditioning]]

![[assets/2606.17294_figure.png|800]]

- **arXiv**: [2606.17294](https://arxiv.org/abs/2606.17294)
- **PDF**: https://arxiv.org/pdf/2606.17294
- **详细分析**: [[20_Research/Papers/具身智能/VISTA_Scale-Aware_Visual_Navigation_via_Action_History_Conditioning|VISTA: Scale-Aware Visual Navigation via Action History Conditioning]]
- **作者**: Maeva Guerrier, Koki Kobayashi, Simon Roy, Jana Pavlasek, Giovanni Beltrame
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《VISTA: Scale-Aware Visual Navigation via Action History Conditioning》归入 机器人、具身智能 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EfficientNet, MetricNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision Navigation Foundation Models (VNMs) promise end-to-end learned navigation policies capable of zero-shot deployment across diverse embodiments and environments. To maintain generality, many vision-based navigation models predict normalized actions. However, this normalization introduces a critical deployment vulnerability: applying different scaling factors to the same normalized trajectory alters its physical geometry, which degrades navigation performance and increases collision risks. We address this vulnerability by conditioning the model on normalized action histories alongside image observations, providing explicit context on the relationship between the model's predictions and the robot's actual physical displacement. Furthermore, current VNMs often struggle in visually repetitive environments that lack distinct features. To resolve this issue, we integrate a DINOv3 encoder, whose richer representations enable our model to capture both spatial and geometric dimensions between observations. VISTA generalizes robustly to out-of-distribution environments, achieving 100% goal prediction accuracy in zero-shot, real-world deployment in Outdoor, Forest and Office settings, and an average of 95% checkpoints crossed, demonstrating consistent path following in unseen environments.

</details>

---
