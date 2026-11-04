# cs.LG | Machine Learning | 2026-11-02

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/Hyperbolic_Inverse_Reinforcement_Learning|Hyperbolic Inverse Reinforcement Learning]]

![[assets/2610.42104_figure.png|800]]

- **arXiv**: [2610.42104](https://arxiv.org/abs/2610.42104)
- **PDF**: https://arxiv.org/pdf/2610.42104
- **详细分析**: [[20_Research/Papers/具身智能/Hyperbolic_Inverse_Reinforcement_Learning|Hyperbolic Inverse Reinforcement Learning]]
- **作者**: Iulia Rusu, Anoop Praturu, Sergei Gepshtein, Tatyana Sharpee
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Hyperbolic Inverse Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inverse reinforcement learning (IRL) seeks to infer the reward function underlying observed behavior, but its predictive accuracy and interpretability depend on how that reward is computed from the underlying features. While prior IRL reward functions have been implemented through a variety of techniques including linear weights, neural networks, or other function approximators, none make assumptions about the geometry of the underlying feature space. Inspired by geometric organization observed in neural circuits, we introduce Hyperbolic inverse reinforcement learning (Hyperbolic IRL), which parameterizes reward as a function of Hyperbolic distance between the feature vector and a learned parameter vector, as well as its Euclidean distance variant. We tested our methods against a range of linear and nonlinear IRL baselines under both deterministic and stochastic policies. Our Hyperbolic approach achieved comparable performance to state-of-the-art models on established benchmarks and excelled in the low data limit and across dense environments. Applied to human navigation among multiple exhibits in a museum room, Hyperbolic IRL reveals reward structure that depends not only on individual exhibit-distance features, but also on non-separable conjunctions between them. Together, these results demonstrate that a Hyperbolic reward parameterization can improve both the predictive accuracy and interpretability of IRL, providing a framework for studying how non-separable, conjunctive structure can begin to explain behavior.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Understanding_the_Impact_of_Plasticity_Loss_on_Reinforcement_Learning_in_Stochastic_Environments|Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments]]

![[assets/2610.42100_figure.png|800]]

- **arXiv**: [2610.42100](https://arxiv.org/abs/2610.42100)
- **PDF**: https://arxiv.org/pdf/2610.42100
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Understanding_the_Impact_of_Plasticity_Loss_on_Reinforcement_Learning_in_Stochastic_Environments|Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments]]
- **作者**: Philipp Bordne, André Biedenkapp
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Towards Understanding the Impact of Plasticity Loss on Reinforcement Learning in Stochastic Environments》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AutoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (RL) is a powerful framework for sequential decision-making. Despite many high-profile successes in recent years, deep RL is known to be brittle. An emerging line of research attributes this brittleness to a loss of plasticity in neural networks. However, plasticity loss has so far been understudied in stochastic environments. We study this interplay systematically, training SAC agents on three DeepMind Control tasks augmented with controlled levels of observation and action noise. We find that plasticity-preserving methods increase learning robustness on the two harder tasks, with their advantage growing as observation noise increases, while combining resets with layer normalization underperforms resets alone at every observation noise level tested. Further, stochasticity can accelerate the loss of plasticity in harder environments, whereas in easier settings noise can act as a regularizer that sustains plasticity. Lastly, plasticity loss is most pronounced in the early stages of training. In the most challenging stochastic settings, TD instability rather than gradual plasticity loss becomes the dominant failure mode.

</details>

---

### [[20_Research/Papers/强化学习/RAMA_Retrieval-Augmented_Multi-Agent_Routing_with_Episodic_Memory_for_LEO_Satellite_Networks|RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks]]

![[assets/2610.42068_first_page.png|800]]

- **arXiv**: [2610.42068](https://arxiv.org/abs/2610.42068)
- **PDF**: https://arxiv.org/pdf/2610.42068
- **详细分析**: [[20_Research/Papers/强化学习/RAMA_Retrieval-Augmented_Multi-Agent_Routing_with_Episodic_Memory_for_LEO_Satellite_Networks|RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks]]
- **作者**: Xin Ming Li, Peng Hu
- **cs 子类**: cs.LG, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.8，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《RAMA: Retrieval-Augmented Multi-Agent Routing with Episodic Memory for LEO Satellite Networks》归入 大模型、强化学习、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, MADRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-Earth orbit (LEO) satellite networks present a challenging routing environment due to rapidly changing topology, traffic, and link conditions. Existing deep reinforcement learning (DRL) routing methods typically rely on current observations and information encoded in network weights, limiting their ability to exploit successful past experiences. We propose RAMA, a retrieval-augmented multi-agent DRL framework with Approximate Information State (AIS), in which each satellite combines its local observation, recent routing history, neighboring state information, and retrieved entries from a per-satellite episodic memory. Retrieved experiences are integrated through a Transformer-based decision network trained with AIS-based auxiliary objectives. With weights frozen in a 140-satellite Kepler constellation, RAMA reduces mean end-to-end latency by 13.4% and 99th-percentile latency by 66.7% relative to the state-of-theart double deep Q-network (DDQN) routing method, mainly by avoiding long detours. Updated online, RAMA remains stable while DDQN degrades. On the 1,584-satellite Starlink shell 1, the reduction in mean latency grows to 93.2%, and updating RAMA online lowers its mean latency by a further 25.5%. These results demonstrate the effectiveness of retrieval-augmented memory for scalable decentralized routing in LEO satellite networks.

</details>

---

### [[20_Research/Papers/强化学习/CausalXRL_Explainable_Reinforcement_Learning_through_Causal_Graph_Reasoning|CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning]]

![[assets/2610.42028_figure.png|800]]

- **arXiv**: [2610.42028](https://arxiv.org/abs/2610.42028)
- **PDF**: https://arxiv.org/pdf/2610.42028
- **详细分析**: [[20_Research/Papers/强化学习/CausalXRL_Explainable_Reinforcement_Learning_through_Causal_Graph_Reasoning|CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning]]
- **作者**: Yanming Zhang, Eric Papenhausen, Klaus Mueller
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《CausalXRL: Explainable Reinforcement Learning through Causal Graph Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CausalXRL, DRL, XRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning is a powerful paradigm for training autonomous agents and has achieved impressive performance in complex environments. However, this success often comes at the cost of interpretability, diminishing trust and complicating efforts to debug and improve agent behavior. To address these challenges, we introduce CausalXRL, a novel framework for explainable reinforcement learning (XRL). A key feature of CausalXRL is its use of causal graph reasoning, which provides transparent, structured, multi-level explanations of agent decision-making. We validate CausalXRL through comprehensive case studies and a two-part evaluation: (1) a quantitative analysis of explanation fidelity and causal-structure learning efficiency in benchmark RL environments, and (2) a qualitative expert study assessing explainability in the real-time strategy (RTS) benchmark MicroRTS. The quantitative results show that CausalXRL can provide faithful explanations while efficiently learning causal structures, and the qualitative expert study suggests that participants found CausalXRL useful for inspecting high-level RTS strategies.

</details>

---

### [[20_Research/Papers/强化学习/When_Is_a_Game_a_Markov_Decision_Process_Correspondences_Between_Game_Theory_and_Reinforcement_Learning|When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning]]

![[assets/2610.41962_first_page.png|800]]

- **arXiv**: [2610.41962](https://arxiv.org/abs/2610.41962)
- **PDF**: https://arxiv.org/pdf/2610.41962
- **详细分析**: [[20_Research/Papers/强化学习/When_Is_a_Game_a_Markov_Decision_Process_Correspondences_Between_Game_Theory_and_Reinforcement_Learning|When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning]]
- **作者**: Eduardo C. Garrido-Merchán
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《When Is a Game a Markov Decision Process? Correspondences Between Game Theory and Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning and game theory describe the same object from two sides. Game theory says what a rational outcome of a strategic interaction is; reinforcement learning says how an agent could reach one through experience. The two literatures nevertheless keep separate vocabularies for identical structures, and the treatments that bridge them present the correspondence as analogy rather than theorem. This monograph supplies the theorems. A game is a Markov decision process in three distinct senses, and every table entry is labelled with the one that applies: a definitional identity, an exact reduction carried by a value- and solution-preserving map, or a structural analogy that fails under identifiable conditions. We take every standard class of game, from normal-form through repeated, stochastic, partially observable, extensive-form with imperfect information, Bayesian, graphical, Stackelberg, potential, coalitional, mean-field and evolutionary games, and identify for each the decision-theoretic model that reinforcement learning already studies under another name. The same treatment is applied to solution concepts: Nash equilibrium and the fixed point of the Bellman optimality operator, quantal response equilibrium and the soft Bellman operator, the Shapley value and credit assignment, Blackwell approachability and no-regret learning. We map each model class onto the training procedures sound for it and record the complexity of the associated solution problems. A final part collects the correspondences that do not hold: the non-stationarity that invalidates the independent-learner reduction, the impossibility results that forbid uncoupled convergence to Nash equilibrium, and the gap between the coarse correlated equilibria that no-regret self-play reaches and the correlated equilibria it is credited with.

</details>

---

### [[20_Research/Papers/强化学习/Continual_Reinforcement_Learning_Is_an_Integration_Problem|Continual Reinforcement Learning Is an Integration Problem]]

![[assets/2610.41809_figure.png|800]]

- **arXiv**: [2610.41809](https://arxiv.org/abs/2610.41809)
- **PDF**: https://arxiv.org/pdf/2610.41809
- **详细分析**: [[20_Research/Papers/强化学习/Continual_Reinforcement_Learning_Is_an_Integration_Problem|Continual Reinforcement Learning Is an Integration Problem]]
- **作者**: Nis Meinert, Jakob Gawlikowski, Edward Grant, Max Cyprys, Nathan Schurr, Neil Boston, Alfredo Ibias, Milind Tambe, Janusz Marecki
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.2，强化学习 0.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Continual Reinforcement Learning Is an Integration Problem》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an opinionated set of ten desiderata intended to inform the design and evaluation of reinforcement-learning agents that learn continually throughout a continuing lifetime. We use these desiderata to examine a representative selection of existing approaches. Progress on individual desiderata is valuable, but the longer-term aim should be to integrate all ten within a single agent. To our knowledge, no published evaluation has yet provided evidence for such an integration. Likewise, the representative benchmarks we review probe different parts of this target, but separate evaluations do not establish that the corresponding properties coexist within one agent throughout a continuing lifetime. As a secondary contribution, we therefore present a compact persistent-world scenario as a playable companion to the desiderata and outline a proposed benchmark that examines a broad range of associated behavioral capabilities together within one such lifetime.

</details>

---

### [[20_Research/Papers/强化学习/$_nabla$Mimic_Ultra-Efficient_Humanoid_Control_with_Differentiable_Simulation|$\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation]]

![[assets/2610.41654_first_page.png|800]]

- **arXiv**: [2610.41654](https://arxiv.org/abs/2610.41654)
- **PDF**: https://arxiv.org/pdf/2610.41654
- **详细分析**: [[20_Research/Papers/强化学习/$_nabla$Mimic_Ultra-Efficient_Humanoid_Control_with_Differentiable_Simulation|$\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation]]
- **作者**: Weyl Lu, Yubei Chen
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《$\nabla$Mimic: Ultra-Efficient Humanoid Control with Differentiable Simulation》归入 具身智能、机器人 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policy learning is dominated by zeroth-order methods such as PPO, which treat the simulator as a black box and pay for it with enormous sample counts. First-order policy learning differentiates through the dynamics, but on contact-rich whole-body control it has rarely worked: its gradients explode. A recent world-model method showed that derivative information can make humanoid motion tracking far more efficient, using surrogate gradients of a learned model. We show that exact gradients of the simulator itself do better, once two obstacles are removed. Exact gradients contain rare unbounded samples, because contact dynamics is not differentiable everywhere and its derivative diverges near some events; and they are expensive, because the simulator's adjoint has to replay the contact solve. $\nabla$Mimic bounds these samples with median-relative per-sample gradient clipping at every step of the backward pass, and reuses each costly simulated window by multistep regression onto gradient-derived action targets, which bounds every action target independently of the gradient scale. NablaEngine, a differentiable GPU simulation engine for the Unitree G1, removes the cost: it computes MuJoCo's full contact dynamics with fused per-world kernels and the adjoint of a whole control step as a single megakernel, with analytic gradients that match float64 finite differences, $11.5\times$ faster than the available MuJoCo Warp adjoint. On whole-body tracking of all 40 LAFAN1 clips with one policy on one GPU, $\nabla$Mimic reaches the score reported by the state-of-the-art world-model method, 0.82, in 20 minutes instead of 1.2 h, and 0.874 in 1.8 h. SHAC, the standard first-order baseline, stops on exploding gradients within minutes. We release NablaEngine and $\nabla$Mimic as open-source infrastructure for first-order humanoid policy learning.

</details>

---

### [[20_Research/Papers/具身智能/FOCUS_First-Order_Control_Using_Optimal_Transport_Supervision_for_Imitation_from_Observations|FOCUS: First-Order Control Using Optimal Transport Supervision for Imitation from Observations]]

![[assets/2610.41540_figure.png|800]]

- **arXiv**: [2610.41540](https://arxiv.org/abs/2610.41540)
- **PDF**: https://arxiv.org/pdf/2610.41540
- **详细分析**: [[20_Research/Papers/具身智能/FOCUS_First-Order_Control_Using_Optimal_Transport_Supervision_for_Imitation_from_Observations|FOCUS: First-Order Control Using Optimal Transport Supervision for Imitation from Observations]]
- **作者**: João A. Cândido Ramos, Lionel Blondé, Hugues Vinzant, Jacopo Castellini, Alexandros Kalousis
- **cs 子类**: cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：具身智能 0.9，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《FOCUS: First-Order Control Using Optimal Transport Supervision for Imitation from Observations》归入 具身智能、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FO-MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning from observations must recover behavior from state-only demonstrations without known temporal correspondence. Differentiable simulators provide pathwise policy gradients, but differentiating through long, contact-rich trajectories can make optimization unstable. We introduce FOCUS, which combines local optimal-transport alignment with short-horizon differentiable actor-critic learning. FOCUS matches agent rollout windows to multiple sampled expert segments using a soft best-of-$K$ objective that emphasizes locally compatible matches. The resulting transport-based costs provide differentiable imitation rewards, while a learned critic bootstraps value beyond the rollout horizon. FOCUS requires neither temporally aligned trajectories nor expert-aligned initialization or teacher forcing. Across contact-rich locomotion tasks in DFlex, including a musculoskeletal humanoid controlled by 152 muscle activations, FOCUS improves sample efficiency and training stability over adversarial imitation-from-observation methods and prior differentiable imitation baselines.

</details>

---

### [[20_Research/Papers/强化学习/rl_rob_A_transparent,_from-scratch_Python_library_for_teaching_reinforcement_learning_from_tabular_methods_to_deep_policy_gradients|rl_rob: A transparent, from-scratch Python library for teaching reinforcement learning from tabular methods to deep policy gradients]]

![[assets/2610.41303_first_page.png|800]]

- **arXiv**: [2610.41303](https://arxiv.org/abs/2610.41303)
- **PDF**: https://arxiv.org/pdf/2610.41303
- **详细分析**: [[20_Research/Papers/强化学习/rl_rob_A_transparent,_from-scratch_Python_library_for_teaching_reinforcement_learning_from_tabular_methods_to_deep_policy_gradients|rl_rob: A transparent, from-scratch Python library for teaching reinforcement learning from tabular methods to deep policy gradients]]
- **作者**: Abdulrahman Altahhan
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《rl_rob: A transparent, from-scratch Python library for teaching reinforcement learning from tabular methods to deep policy gradients》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Machine Learning 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

rl_rob is an open-source Python library for teaching reinforcement learning. It implements the arc of a modern course, from tabular temporal-difference learning through linear function approximation to deep value-based and policy-gradient methods, with every algorithm written from first principles so that its update rule is visible in a few lines of code. All agents share one interface, so learners can compare methods directly across stages and trace a deep reinforcement learning update from the temporal-difference error to the weight change. The library supports teaching and assessment in which students implement, modify and explain update rules, rather than only produce working code.

</details>

---

### [[20_Research/Papers/世界模型/SPT-Flow_One_Integration,_Many_Futures_in_Continuous-Time_World_Models|SPT-Flow: One Integration, Many Futures in Continuous-Time World Models]]

![[assets/2610.41273_figure.png|800]]

- **arXiv**: [2610.41273](https://arxiv.org/abs/2610.41273)
- **PDF**: https://arxiv.org/pdf/2610.41273
- **详细分析**: [[20_Research/Papers/世界模型/SPT-Flow_One_Integration,_Many_Futures_in_Continuous-Time_World_Models|SPT-Flow: One Integration, Many Futures in Continuous-Time World Models]]
- **作者**: Mingyang Lyu, Yinqian Sun, Gongce Cao, Yuhao Zhang, Lu Jia, Qian Zhang, Bo Wang, Pin Lyu
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 0.96，机器人 0.2）
- **关联关键词**: Robotics

#### 研究背景与动机

《SPT-Flow: One Integration, Many Futures in Continuous-Time World Models》归入 世界模型、机器人、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ODEWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuous-time world models generate a latent trajectory through a single ODE integration, but adding stochastic conditioning does not ensure that the model uses it. In our teacher-forced baseline, posterior means vary by only about 1% of the prior scale, and matched and swapped latents yield indistinguishable reconstruction PSNR at the reported precision. We study a supervision-shortcut hypothesis: ground-truth intermediate states can reduce the need for trajectory-associated latent information. We introduce SPT-Flow, which samples one latent per trajectory and matches a free-running ODE rollout to demonstration states at multiple readout times. Re-anchoring experiments support the proposed mechanism. On LIBERO, with both models trained for 30k optimizer steps, SPT-Flow improves best-of-10 PSNR over our retrained ODEWorld baseline by 2.0 and 2.4 dB at the mid-trajectory and final frames and reduces mean LPIPS by 23%, with comparable per-sample inference cost. The rollout control recovers most of the accuracy gain; learned latent conditioning adds diversity and best-of-K gains while reducing mean sample accuracy relative to this control. The diagnostics support trajectory-associated latent utilization; semantic mode coverage under matched conditions in the robotic setting remains unverified.

</details>

---

### [[20_Research/Papers/大模型/TalentRL_Strategy-Guided_Reinforcement_Learning_for_Hierarchical_Skill_Routing|TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing]]

![[assets/2610.41143_figure.png|800]]

- **arXiv**: [2610.41143](https://arxiv.org/abs/2610.41143)
- **PDF**: https://arxiv.org/pdf/2610.41143
- **详细分析**: [[20_Research/Papers/大模型/TalentRL_Strategy-Guided_Reinforcement_Learning_for_Hierarchical_Skill_Routing|TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing]]
- **作者**: Huancheng Chen, Xiaodi Sun, Zhaoqiong Huang, Michelle Chang, Jingwen Lu
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《TalentRL: Strategy-Guided Reinforcement Learning for Hierarchical Skill Routing》归入 强化学习、大模型、世界模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SkillRL, TalentRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural-language skills enable large language model (LLM) agents to reuse procedures across tasks, yet most systems retrieve individual skills from a flat SkillBank without explicitly modeling the high-level strategy that governs their selection and use. We introduce TalentRL, a strategy-guided reinforcement learning framework for hierarchical routing over procedural memory. Coarse-grained talents represent recurring strategies for skill use, while fine-grained skills provide executable procedures. For each task, the policy model selects a talent that guides execution and softly prioritizes its associated skills during similarity-based retrieval. However, since task outcomes depend jointly on talent selection, retrieved skill context, and downstream execution, terminal rewards alone cannot isolate the contribution of the routing decision. TalentRL therefore trains talent routing with reward contrasts between rollouts of the same task under matched interventions on the talent-conditioned context, and optimizes downstream execution with group-relative advantages. Across seven open-domain and multi-hop question-answering benchmarks, talent-aware supervised fine-tuning improves average success rate by 7.53%, 6.71%, and 9.21% over the corresponding zero-shot baselines for Qwen2.5-7B, Qwen3-8B, and Llama-3.1-8B, respectively. Reinforcement learning further improves these SFT checkpoints by 7.58% to 9.32%, and TalentRL achieves the highest average success rate among all compared methods on all three backbones. On the agentic benchmarks ALFWorld and WebShop, TalentRL achieves the highest ALFWorld success rate (99.3%) and the highest WebShop score (90.7) among all compared methods.

</details>

---

### [[20_Research/Papers/世界模型/Meshless_Latent_Dynamics_Models_for_Model_Order_Reduction_of_time-dependent_Partial_Differential_Equations|Meshless Latent Dynamics Models for Model Order Reduction of time-dependent Partial Differential Equations]]

![[assets/2610.41043_figure.png|800]]

- **arXiv**: [2610.41043](https://arxiv.org/abs/2610.41043)
- **PDF**: https://arxiv.org/pdf/2610.41043
- **详细分析**: [[20_Research/Papers/世界模型/Meshless_Latent_Dynamics_Models_for_Model_Order_Reduction_of_time-dependent_Partial_Differential_Equations|Meshless Latent Dynamics Models for Model Order Reduction of time-dependent Partial Differential Equations]]
- **作者**: Lorenzo Tomada, Federico Pichi, Gianluigi Rozza
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Meshless Latent Dynamics Models for Model Order Reduction of time-dependent Partial Differential Equations》归入 世界模型、强化学习 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent dynamics learning has emerged as a prominent approach for Model Order Reduction (MOR) of time-dependent, parameterized Partial Differential Equations (PDEs). Traditional autoencoder-based approaches are intrinsically tied to fixed spatial discretizations during both training and inference, motivating the development of meshless methodologies. In this context, conditioning provides a natural mechanism for representing temporal evolution through spatially continuous functions, enabling mesh-agnostic Latent Dynamics Models (LDMs). In this work, we introduce a unified mathematical framework for mesh-agnostic LDMs based on conditioning in Neural Fields (NeFs). Leveraging a taxonomy of conditioning mechanisms (weak, strong, and pure), we formulate meshless LDMs as NeFs conditioned on a latent state. We establish a Universal Approximation Theorem (UAT) for this class of models and analyze their stability by deriving Lipschitz bounds for different conditioning mechanisms. Our analysis reveals an expressivity--stability trade-off, providing insight into why more expressive conditioning, despite its higher representational capacity, can potentially degrade performance during temporal extrapolation. Finally, we provide a comprehensive comparison of meshless and mesh-based architectures in the continuous limit of the spatial discretization, showing that meshless models guarantee grid-independent Lipschitz bounds, unlike mesh-based counterparts. Our experiments across Burgers' equation, Navier--Stokes flow past a cylinder, and linear advection show that meshless LDMs can achieve predictive accuracy comparable to or better than their mesh-based counterparts while using only 2% of the trainable parameters and exhibiting nearly constant error across spatial discretizations.

</details>

---

### [[20_Research/Papers/强化学习/Before_We_Adapt_The_Zero-Shot_Generalization_Bottleneck_in_Continual_World_Models|Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models]]

![[assets/2610.41041_figure.png|800]]

- **arXiv**: [2610.41041](https://arxiv.org/abs/2610.41041)
- **PDF**: https://arxiv.org/pdf/2610.41041
- **详细分析**: [[20_Research/Papers/强化学习/Before_We_Adapt_The_Zero-Shot_Generalization_Bottleneck_in_Continual_World_Models|Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models]]
- **作者**: Amir Mesbah, Di Wu
- **cs 子类**: cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 0.36，世界模型 1.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Before We Adapt: The Zero-Shot Generalization Bottleneck in Continual World Models》归入 世界模型、强化学习、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CRL, MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual reinforcement learning (CRL) requires agents to operate under environmental changes while reusing prior knowledge whenever possible. We argue that model-based reinforcement learning provides a promising framework for this setting because learned world models (WMs) can, in principle, support change detection, knowledge reuse, adaptation, and acquisition of new knowledge. However, such benefits depend heavily on whether the learned model can generalize beyond the contexts in which it was trained. In this work, we propose to formulate this problem with a contextual Markov decision process in which context is decomposed into behavioral and physical components. This view organizes continual WM learning into reuse, adaptation, and acquisition of new knowledge. As a first step, we study direct reuse when behavioral rules remain unchanged. Using Dyna-Q and TD-MPC in controlled FourRooms tasks, we find that zero-shot reuse can degrade substantially under physical-context changes and that this behavior depends strongly on the observation representation used by the WM. Additional ablation studies and latent-space diagnostics suggest that learned representations do not automatically provide the invariances needed for reuse. These results identify representation generalization as an important bottleneck for reliable world-model reuse in CRL.

</details>

---

### [[20_Research/Papers/强化学习/Density-Guided_Bootstrap_Boundaries_for_Latent_World-Model_Reinforcement_Learning|Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning]]

![[assets/2610.41022_figure.png|800]]

- **arXiv**: [2610.41022](https://arxiv.org/abs/2610.41022)
- **PDF**: https://arxiv.org/pdf/2610.41022
- **详细分析**: [[20_Research/Papers/强化学习/Density-Guided_Bootstrap_Boundaries_for_Latent_World-Model_Reinforcement_Learning|Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning]]
- **作者**: Shashank Gupta, Pilhwa Lee
- **cs 子类**: cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 0.96，世界模型 0.56）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Density-Guided Bootstrap Boundaries for Latent World-Model Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models allow reinforcement learning agents to learn policies from imagined trajectories, yet determining the optimal depth of model reliance remains a fundamental challenge. Fixed imagination horizons apply uniform prediction depths regardless of trajectory reliability, exposing target values to compounding model error or over-relying on critic approximations. We introduce density-guided bootstrap boundaries, a trajectory-dependent mechanism that adapts the depth of imagined returns using a score-informed relative density proxy. The proxy accumulates the estimated divergence of a score-corrected auxiliary field formed by a feature displacement network and a noise-conditioned score estimator along imagined paths. We propose two gating mechanisms: a hard boundary that halts return expansion at a discrete state, and a soft boundary that continuously shifts the return recursion toward critic bootstrapping. Both variants preserve boundary value estimates and apply corresponding survival weights to actor and critic losses. Formulated independently of specific dynamics models and instantiated within Dreamer V3, we prove that the resulting gated Bellman operator is a strict contraction mapping and that early bootstrapping monotonically reduces conditional target variance. We clarify the theoretical assumptions distinguishing our expansion proxy from exact path likelihoods. Across continuous-control tasks and Atari Pong, empirical evaluations show that dynamic boundary selection enhances sample efficiency and late-training performance over fixed-horizon and auxiliary-enabled baselines.

</details>

---

### [[20_Research/Papers/大模型/Frozen_in_Time_How_a_Physics_Foundation_Model_Forgets_Under_Sim-to-Real_Adaptation|Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation]]

![[assets/2610.40857_figure.png|800]]

- **arXiv**: [2610.40857](https://arxiv.org/abs/2610.40857)
- **PDF**: https://arxiv.org/pdf/2610.40857
- **详细分析**: [[20_Research/Papers/大模型/Frozen_in_Time_How_a_Physics_Foundation_Model_Forgets_Under_Sim-to-Real_Adaptation|Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation]]
- **作者**: Haaris Mian, Miles Cranmer, Alessandro Favero, Payel Mukhopadhyay
- **cs 子类**: cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 1.2，大模型 0.3）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Frozen in Time: How a Physics Foundation Model Forgets Under Sim-to-Real Adaptation》归入 具身智能、大模型 方向。该论文围绕 Machine Learning 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RealPDEBench, TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific foundation models (SciFMs) have achieved remarkable performance on a wide range of PDEs, including the ability to efficiently adapt to unseen data distributions with additional finetuning. As with all neural architectures, finetuning such models comes with the risk of catastrophic forgetting, whereby adapting to new tasks degrades prior knowledge of the model. We study catastrophic forgetting in Walrus-1.3B, a SciFM for continuum dynamics, over the course of a two-stage sim-to-real adaptation: first finetuning on simulated flow around a cylinder and then adapting to experimental data of the same system. We find that finetuning on the simulations rapidly degrades rollout performance on the original pretraining datasets, with one-step errors increasing up to 35x after just 20 epochs. Subsequent adaptation to real data further erodes performance on the simulated task. We characterize the potential drivers of forgetting, such as dataset dependence and task representation similarity. We then show that replaying as little as 1% simulated data during real-data finetuning recovers most of the lost simulation performance while retaining effective adaptation to the experimental dynamics. Our results identify catastrophic forgetting as a practical obstacle to sim-to-real adaptation of SciFMs and show that lightweight replay strategies significantly improve retention.

</details>

---
