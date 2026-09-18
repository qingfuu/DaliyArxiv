# cs.AI | Artificial Intelligence | 2026-09-16

#arxiv #ComputerScience

**论文数**: 29

### [[20_Research/Papers/具身智能/CTAN_Cycle-Temporal_Attention_Network_for_Embodied_Audio-Visual_Navigation|CTAN: Cycle-Temporal Attention Network for Embodied Audio-Visual Navigation]]

![[assets/2609.17420_figure.png|800]]

- **arXiv**: [2609.17420](https://arxiv.org/abs/2609.17420)
- **PDF**: https://arxiv.org/pdf/2609.17420
- **详细分析**: [[20_Research/Papers/具身智能/CTAN_Cycle-Temporal_Attention_Network_for_Embodied_Audio-Visual_Navigation|CTAN: Cycle-Temporal Attention Network for Embodied Audio-Visual Navigation]]
- **作者**: Teng Liu, Yinfeng Yu
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Multimodal, EmbodiedAI, Systems

#### 研究背景与动机

《CTAN: Cycle-Temporal Attention Network for Embodied Audio-Visual Navigation》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Audio-visual embodied navigation equips robots with the capability to infer the locations of sound sources by integrating visual inputs and acoustic information (e.g., depth observations and binaural audio cues). The core challenge lies in establishing effective semantic interactions across heterogeneous modalities (which exhibit distinct feature distributions). Existing feature fusion strategies, however, often rely on simple multimodal aggregation and therefore fail to capture the underlying geometric and semantic relationships, leading to information degradation in complex environments. To overcome these limitations, this work presents the Cycle-Temporal Attention Network (CTAN), a framework designed for active semantic-enhanced fusion (rather than straightforward multimodal combination). Specifically, the proposed Audio-Visual Reconstruction Cross-Attention (AVRCA) module employs a bidirectional cycle-consistency constraint (between visual and acoustic representations) to reinforce the spatial semantic attributes of both modalities, thereby facilitating more robust cross-modal interaction. Additionally, we design a Temporal Cross-Modal Memory (TCMM) mechanism to dynamically integrate real-time enhanced multimodal features with historical context, reducing performance drops caused by auditory dead zones. Experimental results obtained on the Replica and Matterport3D benchmarks indicate that the proposed approach achieves superior performance over previous audio-visual navigation methods in terms of success rate (SR), success weighted by path length (SPL), and scene navigation accuracy (SNA).

</details>

---

### [[20_Research/Papers/具身智能/World_Model_Science_Self-Organized_Criticality,_Weak_Chaos,_and_Metastable_Belief_Dynamics_in_Long-Horizon_LLM_Agents|World Model Science: Self-Organized Criticality, Weak Chaos, and Metastable Belief Dynamics in Long-Horizon LLM Agents]]

![[assets/2609.17419_figure.png|800]]

- **arXiv**: [2609.17419](https://arxiv.org/abs/2609.17419)
- **PDF**: https://arxiv.org/pdf/2609.17419
- **详细分析**: [[20_Research/Papers/具身智能/World_Model_Science_Self-Organized_Criticality,_Weak_Chaos,_and_Metastable_Belief_Dynamics_in_Long-Horizon_LLM_Agents|World Model Science: Self-Organized Criticality, Weak Chaos, and Metastable Belief Dynamics in Long-Horizon LLM Agents]]
- **作者**: Xinyuan Song, Zekun Cai
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.9，世界模型 0.8）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《World Model Science: Self-Organized Criticality, Weak Chaos, and Metastable Belief Dynamics in Long-Horizon LLM Agents》归入 大模型、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, HotpotQA, StableToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents must maintain task state across extended sequences of observations, actions, tool calls, and intermediate beliefs. We study these trajectories through three dynamical views: self-organized criticality, weak chaos, and metastable belief dynamics. Our framework aligns agent-implied states with benchmark-grounded states and measures stress accumulation, error avalanches, temporal dependence, local--global mismatch, bounded divergence, belief-basin transitions, and finite-size scaling under explicit null models. Across 22 experiments spanning controlled puzzles, tool use, embodied tasks, multi-hop retrieval, general-assistant reasoning, and Game of Life, we find that locally valid actions can persist after global state fidelity fails, stress can trigger abrupt collapse, error sequences exhibit long memory, dependency depth changes the propagation regime, and larger horizons support larger avalanches. At the same time, divergence remains bounded, belief states show metastable rather than fully chaotic behavior, and stronger claims of universal power laws, critical points, or shared intervention optima are not supported. These results suggest a science of agent world models based on trajectory-level dynamical diagnostics rather than terminal reward alone.

</details>

---

### [[20_Research/Papers/大模型/Self-Emergence_Agent_Architecture_Behavior-Inertia_HMM,_Reflexive_Metacognition,and_Social-Contrastive_Self-Modeling|Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling]]

![[assets/2609.17331_figure.png|800]]

- **arXiv**: [2609.17331](https://arxiv.org/abs/2609.17331)
- **PDF**: https://arxiv.org/pdf/2609.17331
- **详细分析**: [[20_Research/Papers/大模型/Self-Emergence_Agent_Architecture_Behavior-Inertia_HMM,_Reflexive_Metacognition,and_Social-Contrastive_Self-Modeling|Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling]]
- **作者**: Xiaoyang Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Self-Emergence Agent Architecture:Behavior-Inertia HMM, Reflexive Metacognition,and Social-Contrastive Self-Modeling》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents exhibit strong language-generation and problem-solving capabilities, yet suffer from three structural limitations: personality drift, non-evolutionary reflection, and the absence of a self-other boundary. Existing generative-agent simulations rely on static memory and fixed prompts, maintaining neither behavioral inertia nor endogenous self-evolution. We propose the Self-Emergence Agent Architecture (SEAA), which integrates three components: (i) a Hidden Markov Model (HMM) that encodes long-term behavioral and cognitive inertia as an editable state-transition matrix; (ii) a Reflexion-style verbal metacognition loop whose output updates the HMM parameters themselves, rather than merely being stored as text; and (iii) a multi-agent social environment in which initially identical agents continuously compare their behavior with others'. The three components form a closed loop: social action $\to$ feedback $\to$ self-reflection $\to$ inertia update $\to$ differentiated action. We state three falsifiable hypotheses and provide a reproducible experimental protocol with operational metrics. A language-model-free prototype shows the loop spontaneously breaks symmetry: initially identical agents consolidate distinct, stable personalities whereas matched controls do not. Experiments with a hosted LLM surface these differences as distinct first-person self-narratives, and a five-agent deliberation spontaneously develops social structure---a consensus hub and a unanimously rejected outlier---absent in the control. Following an epistemologically agnostic stance inspired by Zhuangzi, SEAA studies only observable behavioral emergence and makes no claim about subjective qualia. This work contributes a unified framework, a concrete architecture with pseudocode, mechanistic evidence, and a microscope-style sandbox for studying artificial-self emergence.

</details>

---

### [[20_Research/Papers/强化学习/Intrinsic_Motivation_in_Reinforcement_Learning_A_Research_Agenda_for_Adaptive_Self-Organisation|Intrinsic Motivation in Reinforcement Learning: A Research Agenda for Adaptive Self-Organisation]]

![[assets/2609.17325_figure.png|800]]

- **arXiv**: [2609.17325](https://arxiv.org/abs/2609.17325)
- **PDF**: https://arxiv.org/pdf/2609.17325
- **详细分析**: [[20_Research/Papers/强化学习/Intrinsic_Motivation_in_Reinforcement_Learning_A_Research_Agenda_for_Adaptive_Self-Organisation|Intrinsic Motivation in Reinforcement Learning: A Research Agenda for Adaptive Self-Organisation]]
- **作者**: Anatoly Belikov
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.6，世界模型 0.2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Intrinsic Motivation in Reinforcement Learning: A Research Agenda for Adaptive Self-Organisation》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biological cells can be viewed as individual, interacting agents whose collective dynamics give rise to adaptive behaviour at multiple levels of organisation, from individual cells through tissues to whole multicellular organisms. In this perspective and tutorial article we discuss whether intrinsic rewards in artificial neural systems can support adaptation, functional specialisation and higher-level self-organisation without a shared external objective. We review empowerment, curiosity, learning progress, information gain, unsupervised skill discovery, mutual information estimation and the use of world models for intrinsic reward computation. Particular attention is given to failure modes showing when such objectives do not produce sustained exploration or increasingly complex behaviour. We argue that more capable systems may require complementary objectives, communication, memory, learning at multiple temporal scales and environmental constraints. Based on this perspective, we outline three experimental directions. These include a resource-constrained environment in which otherwise stable behavioural attractors become unsustainable, allowing us to test whether environmental constraints can mitigate characteristic failure modes of intrinsic objectives. The network of recurrent agents with per-agent intrinsic rewards, and a hierarchical world-model agent in which exploratory motor competence develops before goal-directed behaviour. These experiments are intended to test whether intrinsic learning can lead to adaptive organisation at progressively higher levels.

</details>

---

### [[20_Research/Papers/大模型/Easy_to_Catch_a_Liar,_Hard_to_Clear_an_Honest_One_Language_Models_Diagnosing_a_Corrupted_Reward_Channel_from_a_Verified_Record|Easy to Catch a Liar, Hard to Clear an Honest One: Language Models Diagnosing a Corrupted Reward Channel from a Verified Record]]

![[assets/2609.17226_first_page.png|800]]

- **arXiv**: [2609.17226](https://arxiv.org/abs/2609.17226)
- **PDF**: https://arxiv.org/pdf/2609.17226
- **详细分析**: [[20_Research/Papers/大模型/Easy_to_Catch_a_Liar,_Hard_to_Clear_an_Honest_One_Language_Models_Diagnosing_a_Corrupted_Reward_Channel_from_a_Verified_Record|Easy to Catch a Liar, Hard to Clear an Honest One: Language Models Diagnosing a Corrupted Reward Channel from a Verified Record]]
- **作者**: Arman Nik Khah
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.87（加权：大模型 0.35，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Easy to Catch a Liar, Hard to Clear an Honest One: Language Models Diagnosing a Corrupted Reward Channel from a Verified Record》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An agent that learns from rewards has to trust whatever reports those rewards. When the reports suddenly change, either the world changed or the reporter broke. From the reports alone these are indistinguishable, and reinforcement learning theory shows that no amount of further experience separates them. The prescribed escape is richer data about the reporter itself. We ask whether a frozen language model, handed exactly that data, uses it. We build a two-option game in which a payout swap and a lying reporter produce byte-identical histories. Then we add one verified record: an independent check of one round's real result, printed beside what the reporter said about that round. That single line settles the case. We ask three large models, from two families, to answer one question with one letter. Is the reporter honest or lying? They catch a lying reporter almost perfectly. At the 70B class that holds in every condition we tried; the 32B model slips in one wording. They clear an honest reporter far less often, and how often depends on things that should not matter. Averaged over rounds, letters, and wordings, a 72B model calls an honest reporter a liar 38% of the time when nothing has changed at all, and 58% of the time when the payouts moved. A 70B model from a second family calls an honest reporter a liar 26% and 48% of the time. The failure is not one of reading, because in the situation where nothing changed the same models score 0.96 to 1.00 with the answer printed in the prompt. Which surface feature drives it differs by family. For the Qwen models it is which round the record names, and for Llama it is which letter stands for "honest." Adding the record to a prompt that already states the answer makes Llama less likely to give that answer. We had registered a prediction for that 58% before the run: 35%. The failure is larger than we expected.

</details>

---

### [[20_Research/Papers/具身智能/FluxVLA_Engine_A_One-Stop_VLA_Engineering_Platform_for_Embodied_Intelligence|FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence]]

![[assets/2609.17210_figure.png|800]]

- **arXiv**: [2609.17210](https://arxiv.org/abs/2609.17210)
- **PDF**: https://arxiv.org/pdf/2609.17210
- **详细分析**: [[20_Research/Papers/具身智能/FluxVLA_Engine_A_One-Stop_VLA_Engineering_Platform_for_Embodied_Intelligence|FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence]]
- **作者**: Yinhao Li, Weixin Mao, Zihan Lan, Jikun Rong, Qirui Hu, Yiming Zhang, Weipeng Deng, Bowen Shen, Minzhao Zhu, Yiming Mao, Yan Yang, Chenguang Cui...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.9（加权：具身智能 3，强化学习 0.2，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《FluxVLA Engine: A One-Stop VLA Engineering Platform for Embodied Intelligence》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FluxVLA, OpenVLA, SmolVLA, StarVLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models, world-action models (WAMs), and offline reinforcement learning methods are rapidly expanding the design space of embodied policies, yet turning these algorithms into reliable robot systems remains constrained by fragmented data formats, training stacks, evaluation protocols, inference runtimes, and embodiment-specific interfaces. We present $\mathrm{FluxVLA}$ Engine, an open, configuration-driven platform that turns heterogeneous embodied-policy components into a reproducible data-to-deployment workflow. Rather than introducing another policy model, $\mathrm{FluxVLA}$ standardizes interfaces for datasets, visual-language and world models, action heads, reward- or advantage-weighted learning, distributed training, simulation evaluation, optimized inference, and robot operators. The engine further integrates compositional dual-arm simulation, scalable automatic data generation, and model-decoupled human-in-the-loop rollout, takeover, correction collection, and reward annotation. For responsive physical execution, it combines Real-Time Chunking (RTC) with accelerated inference backends, lightweight remote GPU serving, and configurable trajectory post-processing. Together, these capabilities connect offline learning, simulation validation, online correction, and real-robot execution through shared and auditable contracts. $\mathrm{FluxVLA}$ therefore targets the engineering bottlenecks separating promising embodied-learning algorithms from reproducible evaluation and dependable deployment. Code is available at this https URL

</details>

---

### [[20_Research/Papers/具身智能/Continual_Learning_for_Traversability_Prediction_with_Uncertainty-Aware_Adaptation|Continual Learning for Traversability Prediction with Uncertainty-Aware Adaptation]]

![[assets/2609.17141_figure.jpg|800]]

- **arXiv**: [2609.17141](https://arxiv.org/abs/2609.17141)
- **PDF**: https://arxiv.org/pdf/2609.17141
- **详细分析**: [[20_Research/Papers/具身智能/Continual_Learning_for_Traversability_Prediction_with_Uncertainty-Aware_Adaptation|Continual Learning for Traversability Prediction with Uncertainty-Aware Adaptation]]
- **作者**: Hojin Lee, Yunho Lee, Daniel A Duecker, Cheolhyeon Kwon
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Continual Learning for Traversability Prediction with Uncertainty-Aware Adaptation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traversability prediction is a critical component of autonomous navigation in unstructured environments, where complex and uncertain robot-terrain interactions pose significant challenges such as traction loss and dynamic instability. Despite recent progress in learning-based traversability prediction, these methods often fail to adapt to novel terrains. Even when adaptation is achieved, retaining experience from previously trained environments remains a challenge, a problem known as catastrophic forgetting. To address this challenge, we propose a continual learning framework for traversability prediction that incrementally adapts to new terrains using a generative experience recall model. A key virtue of the proposed framework is two folds: i) retain prior experience without storing past data; and ii) incorporate the uncertainty of the generated samples from the recall model, enabling uncertainty-aware adaptation. Real-world experiments with a skid-steering robot validate the effectiveness of the proposed framework, demonstrating its ability to adapt across a series of diverse environments while mitigating catastrophic forgetting.

</details>

---

### [[20_Research/Papers/大模型/Sparse_MLLM_Anchors,_Dense_Adaptation_Breaking_the_Self-Referential_Loop_in_Wild_Test-Time_Adaptation|Sparse MLLM Anchors, Dense Adaptation: Breaking the Self-Referential Loop in Wild Test-Time Adaptation]]

![[assets/2609.17040_figure.png|800]]

- **arXiv**: [2609.17040](https://arxiv.org/abs/2609.17040)
- **PDF**: https://arxiv.org/pdf/2609.17040
- **详细分析**: [[20_Research/Papers/大模型/Sparse_MLLM_Anchors,_Dense_Adaptation_Breaking_the_Self-Referential_Loop_in_Wild_Test-Time_Adaptation|Sparse MLLM Anchors, Dense Adaptation: Breaking the Self-Referential Loop in Wild Test-Time Adaptation]]
- **作者**: Zhenbin Wang, Lei Zhang, Lituan Wang, Yan Wang, Zhao Zhang, Wei Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Sparse MLLM Anchors, Dense Adaptation: Breaking the Self-Referential Loop in Wild Test-Time Adaptation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wild test-time adaptation (WTTA) updates a source model online under small test batches, concurrent distribution shifts, and time-varying class imbalance. Most WTTA methods derive their adaptation signals, including predictive uncertainty, sample reliability, and local feature geometry, from the model being adapted. When the source model is unreliable under shift, these signals can reinforce its own errors, forming a self-referential loop. We introduce MASA (Multimodal-LLM-Anchored Semantic Adaptation), which complements model-internal evidence with structured semantic descriptions from a frozen multimodal large language model (MLLM). To limit inference cost, MASA queries the MLLM only for a small set of diverse, reliability-ranked anchors. The resulting descriptions capture the object family and nuisance factors such as style, viewpoint, and occlusion. MASA encodes these descriptions, propagates them to neighboring test samples, and stores the resulting visual-semantic information in an online prototype memory. Descriptor-aware retrieval from this memory provides an auxiliary target for lightweight adaptation of normalization-affine parameters. We evaluate MASA on the WTTA ImageNet-C benchmark under limited-batch, mixed-domain, and imbalanced-label-shift settings with ResNet and ViT backbones.

</details>

---

### [[20_Research/Papers/机器人/AeroLat_Channel-Aware_Latent_Space_Semantic_Communication_for_Decentralized_UAV_Swarms|AeroLat: Channel-Aware Latent Space Semantic Communication for Decentralized UAV Swarms]]

![[assets/2609.16947_figure.png|800]]

- **arXiv**: [2609.16947](https://arxiv.org/abs/2609.16947)
- **PDF**: https://arxiv.org/pdf/2609.16947
- **详细分析**: [[20_Research/Papers/机器人/AeroLat_Channel-Aware_Latent_Space_Semantic_Communication_for_Decentralized_UAV_Swarms|AeroLat: Channel-Aware Latent Space Semantic Communication for Decentralized UAV Swarms]]
- **作者**: Rajdeep Ghosh, Goparaju Venkata Seshachala Sree Vatsava, Sudip Misra
- **cs 子类**: cs.AI, cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Systems

#### 研究背景与动机

《AeroLat: Channel-Aware Latent Space Semantic Communication for Decentralized UAV Swarms》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim, HetNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Communication in latent space offers an intriguing alternative to symbolic messages for decentralized autonomous Unmanned Aerial Vehicle (UAV) swarms operating over bandwidth-constrained, time-varying wireless links. However, when homogeneous frozen models are prompted with discretized perceptual inputs, their broadcast states collapse toward the shared prompt template. In view of this, we propose AeroLat, a channel-aware latent semantic communication framework that uses evidence injection. The resulting latent states are then passed through an explicit communication model that encompasses bandwidth-limited serialization, additive noise and information staleness, which facilitates a joint assessment of communication fidelity and swarm-level coordination. Across multi-seed simulations, AeroLat provably remains resilient to codec choice, faults and increasing swarm size. It consistently reproduces the latent-swarm anomaly, while no-whitening controls recover the collapse. In particular, AeroLat is capable of reducing false similarity by 97.5%.

</details>

---

### [[20_Research/Papers/大模型/RepoAtlas_Guiding_Coding_Agents_via_Evolving_Multimodal_Repository_Views|RepoAtlas: Guiding Coding Agents via Evolving Multimodal Repository Views]]

![[assets/2609.16936_figure.png|800]]

- **arXiv**: [2609.16936](https://arxiv.org/abs/2609.16936)
- **PDF**: https://arxiv.org/pdf/2609.16936
- **详细分析**: [[20_Research/Papers/大模型/RepoAtlas_Guiding_Coding_Agents_via_Evolving_Multimodal_Repository_Views|RepoAtlas: Guiding Coding Agents via Evolving Multimodal Repository Views]]
- **作者**: Yunxiang Zhang, Haiquan Wang, JiaWei Guo, Hanyang Xia, Yan Chen, Tong Chen, Zhang Zhiwei, Junchen Ye
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《RepoAtlas: Guiding Coding Agents via Evolving Multimodal Repository Views》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-powered coding agents have made rapid progress in automating software engineering tasks, yet repository-level issue resolution remains challenging. Beyond generating a plausible patch, an agent must localize relevant code across interdependent files and maintain repository context that is both sufficient and focused. Code graphs expose non-local relations, but linear text interfaces obscure their topology; rendering the full repository graph yields visual representations that are too dense to perceive reliably, whereas a one-shot local view becomes stale as exploration proceeds. We present \textbf{RepoAtlas}, a training-free module that maintains evolving multimodal repository views through a \emph{select--project--refresh} loop over a repository code graph. RepoAtlas combines evidence from the issue with the agent's current exploration state to select a task-relevant region under a fixed budget, projects the selected structure into complementary visual and textual representations, and refreshes the view when changes in the exploration state render it outdated. We evaluate RepoAtlas on SWE-bench Verified, where it improves the resolve rate by 2.4 points while reducing input tokens and model calls by 5.8\% and 7.8\% on average, relative to the strongest multimodal graph baseline, with consistent gains across three models of different families and scales.

</details>

---

### [[20_Research/Papers/机器人/Bridging_Learned_Visual_Perception_and_Symbolic_Belief-Space_Planning|Bridging Learned Visual Perception and Symbolic Belief-Space Planning]]

![[assets/2609.16884_figure.jpg|800]]

- **arXiv**: [2609.16884](https://arxiv.org/abs/2609.16884)
- **PDF**: https://arxiv.org/pdf/2609.16884
- **详细分析**: [[20_Research/Papers/机器人/Bridging_Learned_Visual_Perception_and_Symbolic_Belief-Space_Planning|Bridging Learned Visual Perception and Symbolic Belief-Space Planning]]
- **作者**: Guy Azran, Michael Navat, Sarah Keren
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Bridging Learned Visual Perception and Symbolic Belief-Space Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In partially observable settings, agents must act without full knowledge of the world state and rely on uncertain state-estimation pipelines. Obtaining grounded and verifiable symbolic plans under such uncertainty remains a key challenge. Recent work has integrated Vision-Language Models (VLMs) to bridge perception and symbolic reasoning, following two main paradigms. The first, VLM-as-planner, maps images directly to action sequences, and the second, VLM-as-grounder, grounds observations into symbolic predicates used as the initial state by off-the-shelf planners. Both approaches ignore uncertainty in the planning process, compromising robustness. We introduce a third paradigm, VLM-as-probabilistic-grounder, a novel approach that captures the uncertainty of VLM predicate groundings as a probability distribution over symbolic states. This enables planning in belief space and producing robust plans under uncertainty. Experiments in simulated household robot settings show improved robustness and task success over deterministic grounding, underscoring how our approach leverages foundation models for reliable planning under uncertainty.

</details>

---

### [[20_Research/Papers/大模型/CoAdapt_An_LLM-based_Framework_for_Adaptive_Collaborative_Perception_in_IIoT_Robotic_Swarms|CoAdapt: An LLM-based Framework for Adaptive Collaborative Perception in IIoT Robotic Swarms]]

![[assets/2609.16852_first_page.png|800]]

- **arXiv**: [2609.16852](https://arxiv.org/abs/2609.16852)
- **PDF**: https://arxiv.org/pdf/2609.16852
- **详细分析**: [[20_Research/Papers/大模型/CoAdapt_An_LLM-based_Framework_for_Adaptive_Collaborative_Perception_in_IIoT_Robotic_Swarms|CoAdapt: An LLM-based Framework for Adaptive Collaborative Perception in IIoT Robotic Swarms]]
- **作者**: Houssam Hajj Hassan, Antonia Maria Masucci, Lynda Zitoune, Salah-Eddine Elayoubi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.3（加权：具身智能 0.3，大模型 0.7，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《CoAdapt: An LLM-based Framework for Adaptive Collaborative Perception in IIoT Robotic Swarms》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial IoT environments increasingly deploy autonomous mobile robots for tasks such as material handling, product assembly, or infrastructure inspection. In such deployments, collaborative perception enables robots to share LiDAR observations and collectively construct a richer model of their environment than an individual agent could produce alone. However, industrial environments are dynamic spaces where robot positions shift continuously, network bandwidth fluctuates, and the marginal contribution of robots to perception quality varies at runtime. Existing collaborative perception approaches are designed for static participation assumptions and cannot adapt to these dynamics without sacrificing either detection precision or communication efficiency. This paper presents CoAdapt, an adaptive collaborative perception framework for IIoT robotic swarms in which a Large Language Model (LLM) serves as a runtime fusion controller, jointly deciding which robots participate in the fusion process and which fusion algorithm to apply based on the current spatial configuration and network state. The LLM reasons over structured natural language descriptions of the scene derived from raw LiDAR point clouds, requiring no taskspecific training and generalizing to unseen swarm topologies. Evaluated on the OPV2V benchmark across 25 scenarios, our approach achieves a 38% reduction in communication cost while maintaining detection precision comparable to static baseline approaches.

</details>

---

### [[20_Research/Papers/大模型/Turn-level_Multiscale_Density_Ratio_Estimation_for_LLM_Agents|Turn-level Multiscale Density Ratio Estimation for LLM Agents]]

![[assets/2609.16760_figure.png|800]]

- **arXiv**: [2609.16760](https://arxiv.org/abs/2609.16760)
- **PDF**: https://arxiv.org/pdf/2609.16760
- **详细分析**: [[20_Research/Papers/大模型/Turn-level_Multiscale_Density_Ratio_Estimation_for_LLM_Agents|Turn-level Multiscale Density Ratio Estimation for LLM Agents]]
- **作者**: Zishuo Zhao, Kai Chen, Ao Li, Yuan Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Turn-level Multiscale Density Ratio Estimation for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid development of Large language model (LLM), agent systems enhanced by LLMs show huge potential in being able to deal with complex tasks, especially involving multi-step thinking or interaction with tools. For applying LLM techniques with a well-designed agent paradigm, post-training of LLM in multiple agent scenarios is necessary to achieve better performance. Among the variable post-training techniques, alignment methods such as PPO, DPO, DIL, and GRPO become popular because many papers show a significant positive impact on the model's performance by punishing negative samples while keeping acceptable training complexity. However, most alignment methods address simple single-turn tasks, and there remains room for improvement for complex multi-turn tasks. We propose Turn-level Multiscale Density Ratio Estimation (tlm-DRE), which assigns different weights on corresponding turns and proposes asymmetric token-level training based on the positive-negative space gaps across multiple turns of tasks. The results of the experiment on a wide range of agent benchmarks show that the proposed method performs competitively compared to traditional alignment methods. The proposed training method enables LLMs to perform robustly in multi-turn reasoning tasks with both in-domain and out-of-domain conditions.

</details>

---

### [[20_Research/Papers/具身智能/Seeing_What_Matters_Visual_Cue_Guided_Video_Planning_for_Generalizable_Robot_Navigation|Seeing What Matters: Visual Cue Guided Video Planning for Generalizable Robot Navigation]]

![[assets/2609.16737_figure.png|800]]

- **arXiv**: [2609.16737](https://arxiv.org/abs/2609.16737)
- **PDF**: https://arxiv.org/pdf/2609.16737
- **详细分析**: [[20_Research/Papers/具身智能/Seeing_What_Matters_Visual_Cue_Guided_Video_Planning_for_Generalizable_Robot_Navigation|Seeing What Matters: Visual Cue Guided Video Planning for Generalizable Robot Navigation]]
- **作者**: Hojin Lee, Sizhe Lester Li, Maximilian Hilger, Susie Lu, Achim J. Lilienthal, Vincent Sitzmann, Daniel A. Duecker
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习
- **相关性评分**: 3.12（加权：具身智能 1.5，强化学习 0.16，世界模型 0.36，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Seeing What Matters: Visual Cue Guided Video Planning for Generalizable Robot Navigation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative video models can serve as a promising backbone for robot navigation by predicting future observations as video plans. Recent approaches often condition video planning on short-horizon guidance and recover geometric waypoints through scene reconstruction, leaving longer-horizon planning and precise video-to-action translation less explored. We present CueNav, a video model-based navigation framework combining visual cue guided video planning with an embodiment-specific Inverse-Dynamics Model (IDM). As visual cues, we use a Bird's-Eye View (BEV) map to convey global task context and retain part of the robot body in the egocentric observation to expose embodiment context. These cues guide the video planner, while the IDM translates dense flow fields extracted from the video plan into robot actions. With the visual cue encoding global task context, CueNav achieves nearly 2x higher success in maze navigation than planning without the cue. The body-aware view with the IDM enables precise navigation with 70% success in a narrow passage where comparison methods largely fail to complete the task. We further demonstrate zero-shot semantic-conditioned navigation and deployment of the same video planner across different robot platforms. Our results show that visual cue-guided video planning with embodiment-specific action grounding paves the way toward a generalizable navigation framework for longer-horizon planning and embodiment-aware control. Additional results and code are available on our project website: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/World_Models_for_Embodied_Intelligence_From_Plausible_to_Controllable_to_Actionable|World Models for Embodied Intelligence: From Plausible to Controllable to Actionable]]

![[assets/2609.16697_figure.png|800]]

- **arXiv**: [2609.16697](https://arxiv.org/abs/2609.16697)
- **PDF**: https://arxiv.org/pdf/2609.16697
- **详细分析**: [[20_Research/Papers/具身智能/World_Models_for_Embodied_Intelligence_From_Plausible_to_Controllable_to_Actionable|World Models for Embodied Intelligence: From Plausible to Controllable to Actionable]]
- **作者**: Nanjie Yao, Hao Wang, Chong Cheng, Zhikang Chen, Wenzhe Li, Jiafei Lyu, Li Shen, Peilin Zhao, Zongqing Lu, Gao Huang, Steven Hoi, Dacheng Tao...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.1，世界模型 0.8，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《World Models for Embodied Intelligence: From Plausible to Controllable to Actionable》归入 具身智能、世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：PlaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models connect perception and decision-making in embodied intelligence by maintaining hidden state, anticipating consequences, comparing interventions, and adapting when execution departs from expectations. Although progress is often measured by visual fidelity, their value lies in improving behavior. Before reaching for a cup, a person anticipates its weight and resistance to grasping, shaping the hand before contact. Such anticipation is coarse and rarely pictorial, yet it guides action. This raises a central question: which predictive capabilities improve behavior? Existing surveys, organized by architecture, output modality, or application domain, leave this question implicit. We introduce three progressively stronger capability levels: Plausible models preserve task-relevant temporal, geometric, or physical structure; Controllable models additionally predict how interventions alter that structure; and Actionable models translate predictions into measurable gains in planning, action, learning, evaluation, verification, recovery, or data selection. We complement this hierarchy with a 3 x 4 matrix crossing geometry, physics, and action grounding with improvement loops centered on data, rewards, policies, and the model itself. Using this framework, we survey manipulation, navigation, locomotion, autonomous driving, and general embodied learning, tracing technical progressions, clarifying capability requirements, and examining datasets, benchmarks, and evaluation protocols. We identify challenges in long-horizon consistency, uncertainty calibration, causal intervention testing, latency, verification and recovery, and cross-embodiment transfer. This perspective shifts evaluation from visual plausibility toward whether predictions capture task-relevant state, reflect intervention effects, and improve the closed-loop behavior of embodied agents.

</details>

---

### [[20_Research/Papers/具身智能/Weave_Learning_Whole-Body_Dexterous_Loco-Manipulation_from_Human-Object_Interactions|Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions]]

![[assets/2609.16683_figure.png|800]]

- **arXiv**: [2609.16683](https://arxiv.org/abs/2609.16683)
- **PDF**: https://arxiv.org/pdf/2609.16683
- **详细分析**: [[20_Research/Papers/具身智能/Weave_Learning_Whole-Body_Dexterous_Loco-Manipulation_from_Human-Object_Interactions|Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions]]
- **作者**: Liu Cao, Xingze Wu, Jingzhi Cui, Botian Xu, Mingzhi Pei, Ruoqu Chen, Mengdi Xu
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Weave: Learning Whole-Body Dexterous Loco-Manipulation from Human-Object Interactions》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning humanoid-object interaction requires coordinating whole-body balance, locomotion, and dexterous hand contact to control both robot and object motion. Human demonstrations provide examples of coordinated interaction, but transferring these behaviors to humanoid robots requires learning how to establish and maintain effective contacts under different embodiments and dynamics. We present Weave, a unified framework for learning whole-body dexterous humanoid-object interaction from captured human demonstrations. Weave first converts captured human-object interactions into executable robot-object references through contact-aware retargeting and approach-motion completion. At its core is a contact- and geometry-aware policy that jointly commands 29 body joints and 12 actuated finger joints across multiple objects and interaction sequences. Evaluation across nine objects yields a 92.5% success rate on trained interactions and, without any additional training, 65.0% on sequences never seen during training. We additionally release ~9,000 physically executed rollouts spanning ~23 hours, providing robot-object trajectories with contact annotations for downstream interaction-policy learning and physically consistent HOI motion generation. Project website: this https URL

</details>

---

### [[20_Research/Papers/强化学习/ProxiDex_Learning_Dynamics-Guided_Proximity_Policy_for_Dexterous_Manipulation|ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation]]

![[assets/2609.16586_figure.png|800]]

- **arXiv**: [2609.16586](https://arxiv.org/abs/2609.16586)
- **PDF**: https://arxiv.org/pdf/2609.16586
- **详细分析**: [[20_Research/Papers/强化学习/ProxiDex_Learning_Dynamics-Guided_Proximity_Policy_for_Dexterous_Manipulation|ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation]]
- **作者**: Yushan Bai, Boyu Zheng, Zhiyang Mao, Hongzheng Sun, Yuchuang Tong, En Li, Zhengtao Zhang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《ProxiDex: Learning Dynamics-Guided Proximity Policy for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-finger dexterous manipulation relies on stable hand-object interactions, yet these interactions are partially observable in practice. Visual observations are often occluded by the hand, tactile sensors introduce hardware-specific modalities and calibration burdens, and existing policies rarely model how these cues evolve under actions, making them brittle under contact uncertainty. To address these, we present ProxiDex, a dynamics-guided proximity policy framework that treats hand-object proximity as an interaction state for dexterous manipulation. ProxiDex reconstructs interaction point clouds and converts geometric distances into proximity cues, forming a hardware-agnostic contact representation that provides immersive feedback during VR teleoperation. Built on this representation, ProxiDex learns action-conditioned proximity dynamics with a coupled forward-inverse design: future observation latents are predicted from actions, while proximity variations are decoded from latent changes. Leveraging these dynamics, ProxiDex adaptively reweights proximity tokens across manipulation phases and uses dynamics-consistency supervision to guide policy inference, stabilizing action generation under unreliable visual feedback. Simulation and real-world experiments demonstrate improved success rates and robustness over representative baselines across standard, unseen objects, and perturbation scenarios. Additional visualizations are available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/AquiLLM_Evaluating_Faithfulness_in_Open-Weight_RAG-LLM_Systems_for_Scientific_Research|AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research]]

![[assets/2609.16519_figure.png|800]]

- **arXiv**: [2609.16519](https://arxiv.org/abs/2609.16519)
- **PDF**: https://arxiv.org/pdf/2609.16519
- **详细分析**: [[20_Research/Papers/大模型/AquiLLM_Evaluating_Faithfulness_in_Open-Weight_RAG-LLM_Systems_for_Scientific_Research|AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research]]
- **作者**: Bernie Boscoe, Srinath Saikrishnan, Vikram Seenivasan, Jack Stark, Andrew Lizarraga, Morgan Himes, Jonathan Soriano, PJ Allen, Tuan Do
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《AquiLLM: Evaluating Faithfulness in Open-Weight RAG-LLM Systems for Scientific Research》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific research increasingly relies on large, heterogeneous data sources, motivating interest in retrieval-augmented generation (RAG) systems that provide natural language access to scientific knowledge and research workflows. Researchers are exploring the viability of these systems as natural language interfaces for document search and for generating analysis code and pipeline components. At the same time, concerns about data privacy and control over research infrastructure have motivated interest in open-weight models and open-source deployments hosted within research institutions. In astronomy, this development follows a long history of computational infrastructure development, from archival databases and SQL-based systems to LLM-assisted research tools. This paper presents a domain-expert evaluation of faithfulness for AquiLLM, an open-weight, offline RAG-LLM platform designed to support scientific research groups in the use and preservation of tacit and formal knowledge. We define faithfulness as the extent to which generated responses remain grounded in retrieved scientific context without unsupported claims or omissions. We report results from an astronomy case study evaluating AquiLLM across retrieval and scientific analysis tasks. AquiLLM performs most reliably on explicit retrieval-oriented questions grounded in the RAG collection, while faithfulness degrades for queries requiring synthesis or ambiguity resolution. These results highlight both the promise and limitations of open-weight RAG-LLM systems for scientific research and demonstrate the importance of domain-expert evaluation beyond standard benchmark leaderboards.

</details>

---

### [[20_Research/Papers/大模型/Interpreting_and_Steering_LLM_Agents_for_Social_Simulations|Interpreting and Steering LLM Agents for Social Simulations]]

![[assets/2609.16436_figure.jpg|800]]

- **arXiv**: [2609.16436](https://arxiv.org/abs/2609.16436)
- **PDF**: https://arxiv.org/pdf/2609.16436
- **详细分析**: [[20_Research/Papers/大模型/Interpreting_and_Steering_LLM_Agents_for_Social_Simulations|Interpreting and Steering LLM Agents for Social Simulations]]
- **作者**: Jiayue Gaveal Fan, Arul Murugan, Shreyas Krishnan, Abhishek Nagaraj
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Interpreting and Steering LLM Agents for Social Simulations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulations based on large language models (LLMs) have proven to be powerful for understanding human behavior, making them valuable additions to the social scientific toolkit. However, LLMs are ultimately black boxes based on deep neural networks which limits their value for social science. This is because of a lack of (i) interpretability: i.e. the ability to assign clear mechanisms driving observed behavior; and a lack of (ii) steerability: i.e. the ability to mute or amplify specific theoretically meaningful mechanisms of action to drive specific model behavior. Here, we demonstrate how the black box could be opened up to further enrich LLM-based simulations. Specifically, we compare three types of methods: (1) prompt-based manipulation, (2) SAE-derived feature steering, and (3) probe-based direction steering and examine their utility for LLM-based social scientific simulations. We do so by interpreting and steering two foundational components of human behaviors, namely preferences (risk attitudes, altruism) and capabilities (divergent creativity, product innovation), operationalized using four classic economic and creative tasks implemented as natural-language interactions. Overall, our results show that SAE- and probe-based techniques often outperform basic prompt-based methods for steering LLM agents, although this advantage depends on the specific prompting strategy involved. Together, SAEs and probes constitute an effective pipeline for social scientists seeking to interpret and steer agents in social simulations: SAEs decompose agents' internal representations into human-readable features, after which probes can reliably shift agents' behaviors in specified directions. We discuss implications of these methods for future work using LLM agents for social scientific simulations.

</details>

---

### [[20_Research/Papers/具身智能/UDAV_Uncertainty-Driven_Adaptive_VLM_Waypoint_Planner|UDAV: Uncertainty-Driven Adaptive VLM Waypoint Planner]]

![[assets/2609.16368_figure.png|800]]

- **arXiv**: [2609.16368](https://arxiv.org/abs/2609.16368)
- **PDF**: https://arxiv.org/pdf/2609.16368
- **详细分析**: [[20_Research/Papers/具身智能/UDAV_Uncertainty-Driven_Adaptive_VLM_Waypoint_Planner|UDAV: Uncertainty-Driven Adaptive VLM Waypoint Planner]]
- **作者**: Ghazal Farhani, Shabnam Shabani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《UDAV: Uncertainty-Driven Adaptive VLM Waypoint Planner》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) can generate routes directly from aerial imagery for off-road navigation, but their predictions provide no indication of reliability. We present UDAV, an Uncertainty-Driven Adaptive VLM Waypoint Planner for UAV-guided UGV navigation. UDAV draws multiple stochastic trajectory predictions, selects their medoid as a self-consistent nominal route, and estimates predictive uncertainty from their spatial dispersion. When the maximum uncertainty across interior waypoints exceeds a threshold, UDAV invokes a reconsideration stage; otherwise, it returns the medoid directly. We evaluate UDAV on 400 held-out trajectory queries from two UAV flights. Stochastic medoid selection reduces the mean average displacement error (ADE) from 147.4 pixels for a deterministic prediction to 115.9 pixels. The complete planner achieves a mean ADE of 110.4 pixels, a 25.1% reduction relative to deterministic planning, while producing valid trajectories for all queries. UDAV also yields the lowest 90th- and 95th-percentile errors among all evaluated configurations, including a higher-budget K=10 consensus baseline. Relative to the K=5 medoid, UDAV reduces these errors from 225.3 and 326.0 pixels to 199.0 and 290.8 pixels, respectively. These results demonstrate that stochastic VLM predictions provide both a stronger nominal route and an actionable uncertainty signal for selectively mitigating large planning errors.

</details>

---

### [[20_Research/Papers/机器人/Auto-HSI_Personalized_human_control_of_a_robot_swarm_on_demand_by_using_LLMs_for_online_automatic_code_generation|Auto-HSI: Personalized human control of a robot swarm on demand by using LLMs for online automatic code generation]]

![[assets/2609.16346_figure.png|800]]

- **arXiv**: [2609.16346](https://arxiv.org/abs/2609.16346)
- **PDF**: https://arxiv.org/pdf/2609.16346
- **详细分析**: [[20_Research/Papers/机器人/Auto-HSI_Personalized_human_control_of_a_robot_swarm_on_demand_by_using_LLMs_for_online_automatic_code_generation|Auto-HSI: Personalized human control of a robot swarm on demand by using LLMs for online automatic code generation]]
- **作者**: Alessandro Nazzari, Nathan Cerisara, Dorian Tonnis, Raina Zakir, Lorenzo Labarile, Weixu Zhu, Marco Dorigo, Mary Katherine Heinrich
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《Auto-HSI: Personalized human control of a robot swarm on demand by using LLMs for online automatic code generation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents Auto-HSI, a method for generating personalized human-swarm interaction (HSI) interfaces on demand. The objective is to enable untrained operators to use natural language descriptions and gesture demonstrations to explain how they want the robots to collectively behave in response to their gestures. Based on these inputs, the code should automatically be generated for personalized state machines that will control the robots as desired, in response to the desired gesture inputs. In the developed Auto-HSI prototype, the generated code produces a personalized interface for centralized control using one- and two-handed gestures, enabling a user to teleoperate the robots' motion, formation shape, and shape deformation. We test the gesture tracking and code generation components of Auto-HSI against performance benchmarks. We then test the full Auto-HSI prototype in ``live'' operation experiments, in which real human operators centrally control 50 simulated robots in a physics-based simulator, under nominal and noisy conditions. In these experiments, robots are teleoperated to: score a goal, traverse a maze that requires shape deformation, and score two simultaneous goals by splitting into two groups. We also demonstrate a real human operator making live updates to their personalized Auto-HSI interface during operation (in simulation). Finally, we demonstrate live operation of real robots.

</details>

---

### [[20_Research/Papers/大模型/BLINDSPOT_A_Benchmark_for_Safety_and_Refusal_Calibration_in_Long-Horizon_Tool-Using_Agents|BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents]]

![[assets/2609.16305_figure.png|800]]

- **arXiv**: [2609.16305](https://arxiv.org/abs/2609.16305)
- **PDF**: https://arxiv.org/pdf/2609.16305
- **详细分析**: [[20_Research/Papers/大模型/BLINDSPOT_A_Benchmark_for_Safety_and_Refusal_Calibration_in_Long-Horizon_Tool-Using_Agents|BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents]]
- **作者**: Sadia Asif, Mohammad Mohammadi Amiri, Momin Abbas, Tejaswini Pedapati, Prasanna Sattigeri
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《BLINDSPOT: A Benchmark for Safety and Refusal Calibration in Long-Horizon Tool-Using Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly operate over long-horizon interactions involving tool use, persistent state, evolving authorization, and external environment feedback. In such settings, safety failures may emerge only after multiple turns, yet existing evaluations often reduce agent behavior to task or attack success, obscuring whether an agent acts, refuses, or remains appropriately calibrated as the interaction evolves. We introduce Blindspot, a benchmark for trajectory-level safety calibration of long-horizon tool-using agents. Blindspot evaluates complete user-agent-environment trajectories through adaptive adversarial interaction, stateful tool execution, and execution-grounded adjudication. Its current instantiation contains 22 attack families and 35 scenarios across seven domains, yielding more than 2,500 long-horizon trajectories with an average interaction length of 14.7 turns. Each trajectory is assigned one of five outcomes: Safe Completion, Correct Refusal, Unsafe Completion, Over-Refusal, or Indeterminate. Unlike fixed attack datasets, Blindspot is an extensible live-simulation framework in which attacks, scenarios, tools, policies, domains, and agent configurations can be added without redesigning the evaluation pipeline. We evaluate 13 proprietary and open-weight LLMs using eight metrics covering unsafe completion, appropriate refusal, benign utility, over-refusal, repeated-run robustness, and post-refusal failure. Preliminary results reveal substantial differences in safety-utility calibration across models and show that failures can emerge only after several initially safe interaction steps. These findings motivate treating agent safety as a trajectory-level property rather than a single-turn or binary success criterion.

</details>

---

### [[20_Research/Papers/大模型/Universal_Defenses_for_Tool-Integrated_LLM_Agents_Against_Adversarial_Attacks|Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks]]

![[assets/2609.16098_figure.png|800]]

- **arXiv**: [2609.16098](https://arxiv.org/abs/2609.16098)
- **PDF**: https://arxiv.org/pdf/2609.16098
- **详细分析**: [[20_Research/Papers/大模型/Universal_Defenses_for_Tool-Integrated_LLM_Agents_Against_Adversarial_Attacks|Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks]]
- **作者**: Xiaoyan Li, Yunli Wang
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Universal Defenses for Tool-Integrated LLM Agents Against Adversarial Attacks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents have demonstrated impressive capabilities across a variety of domains, particularly when integrated with external tools for multi-step task completion. However, they are increasingly vulnerable to adversarial attacks, including direct prompt injection, indirect prompt injection, memory poisoning, and backdoor attacks, which exploit the model's openness to prompt injection and tool manipulation. In this work, we explore practical and generalizable defense strategies within a unified framework across these four attack types. We introduce two universal tool-based defenses: Attacker Tool Filtering, which uses anomaly detection (e.g., Isolation Forest) to identify and remove suspicious tools, and Normal Tool Recalling, a white-box method that restores the agent's original toolset prior to planning. Additionally, we incorporate prompt-based defenses: Chain-of-Thought prompting and self-reflection techniques to enhance reasoning and task paraphrasing to mitigate attacks. Experimental results across both four open-source LLMs (Gemma2-9B, Qwen2-7B, LLaMA3-8B, and LLaMA3.1-8B) and three proprietary LLMs (GPT-3.5, GPT-4, and GPT-5) show that our methods significantly reduce the Attack Success Rates (ASR), achieving 0% ASR in many settings, while preserving or even improving the original task success rate. These findings highlight the promise of simple, modular, multi-layered defenses for strengthening the security and robustness of tool-integrated LLM agents. The code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Coaching_Qwen3_Coder_30B_to_Think_Like_a_CodeClash_Arena_Agent|Coaching Qwen3 Coder 30B to Think Like a CodeClash Arena Agent]]

![[assets/2609.16096_figure.JPG|800]]

- **arXiv**: [2609.16096](https://arxiv.org/abs/2609.16096)
- **PDF**: https://arxiv.org/pdf/2609.16096
- **详细分析**: [[20_Research/Papers/大模型/Coaching_Qwen3_Coder_30B_to_Think_Like_a_CodeClash_Arena_Agent|Coaching Qwen3 Coder 30B to Think Like a CodeClash Arena Agent]]
- **作者**: Ivy Ning Zhang
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Coaching Qwen3 Coder 30B to Think Like a CodeClash Arena Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model coding agents have recently become useful for software tasks, but weaker or open-weight agents still struggle to reliably interpret user intent and execute complex multi-step workflows. This gap is especially visible in long-horizon settings, where an agent must repeatedly inspect prior outcomes, diagnose failure, and choose the next code edit under interaction constraints. It motivates a natural question: what can we do to improve the thinking process of a weak code agent? We study this question in CodeClash, a code-arena benchmark where the original work evaluates 8 commercial coding agents across 6 arenas through multi-round tournaments. Since Qwen3 Coder Plus ranks last among them, we take the open-weight Qwen3-Coder-30B as a case study and investigate how to improve it with distilled knowledge from stronger agents. Our analysis shows that Qwen3-Coder-30B is not well optimized for arena-style interaction: it frequently produces syntax and protocol-breaking errors and exhibits weak strategic adaptation across rounds. These failures are difficult to correct with vanilla instruction tuning alone, since offline SFT cannot directly verify whether a generated action is valid or beneficial. To address this, we propose ReAct SFT, which rewrites teacher trajectories into explicit [obs][thought][act] chains, and trajectoryquality weighted SFT, which reweights samples to encourage post-edit checking. ReAct SFT substantially improves strategic behavior, and our fine-tuned model outperforms the original Qwen3 Coder Plus in tournament evaluation.

</details>

---

### [[20_Research/Papers/大模型/RAG-CT_Mitigating_Privacy_Risks_on_Retrieval-Augmented_Generation_Systems_via_Scanning_Prompt_Distribution|RAG-CT: Mitigating Privacy Risks on Retrieval-Augmented Generation Systems via Scanning Prompt Distribution]]

![[assets/2609.16095_figure.png|800]]

- **arXiv**: [2609.16095](https://arxiv.org/abs/2609.16095)
- **PDF**: https://arxiv.org/pdf/2609.16095
- **详细分析**: [[20_Research/Papers/大模型/RAG-CT_Mitigating_Privacy_Risks_on_Retrieval-Augmented_Generation_Systems_via_Scanning_Prompt_Distribution|RAG-CT: Mitigating Privacy Risks on Retrieval-Augmented Generation Systems via Scanning Prompt Distribution]]
- **作者**: Xingyu Lyu, Jiayimei Wang, Jianfeng He, Ning Wang, Yidan Hu, Yimin Chen
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

《RAG-CT: Mitigating Privacy Risks on Retrieval-Augmented Generation Systems via Scanning Prompt Distribution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) has emerged as a powerful paradigm for improving the quality of generated contents of Large Language Models (LLMs) by grounding responses in external knowledge, thus reducing hallucinations and factual errors. However, recent studies have highlighted a critical vulnerability: adversaries can exploit the retrieval process to extract personally identifiable information (PII) from the underlying corpus. To mitigate this risk, we propose a novel defense, RAG-CT, that identifies malicious queries by analyzing their entropy and margin distributions and using a score-based detection method. Extensive experiments with four state-of-the-art attack strategies and four defense baselines on two datasets show that our approach significantly reduces PII leakage while outperforming existing defenses. This work provides a lightweight yet effective mechanism to protect RAG systems against PII leakage without requiring modifications to the underlying LLM or retriever.

</details>

---

### [[20_Research/Papers/强化学习/AssemblyGrid_v1_A_Benchmark_for_Multi-Robot_Production_with_Temporary_Coalitions,_Local_Information,_and_Geometric_Constraints|AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints]]

![[assets/2609.16075_first_page.png|800]]

- **arXiv**: [2609.16075](https://arxiv.org/abs/2609.16075)
- **PDF**: https://arxiv.org/pdf/2609.16075
- **详细分析**: [[20_Research/Papers/强化学习/AssemblyGrid_v1_A_Benchmark_for_Multi-Robot_Production_with_Temporary_Coalitions,_Local_Information,_and_Geometric_Constraints|AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints]]
- **作者**: Fouad Bahrpeyma, David Heik, Dirk Reichelt
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《AssemblyGrid v1: A Benchmark for Multi-Robot Production with Temporary Coalitions, Local Information, and Geometric Constraints》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flexible robotic production requires joint decisions on process progression, material routing, resource assignment, temporary cooperation, and simultaneous execution, since each decision can affect the feasibility of the others. The challenge is greater under decentralized control, where each robot acts from bounded local information while system progress depends on collective decisions, shared resources, material state, and workspace compatibility. These properties closely match cooperative multi-agent decision making under partial observability and resource contention. This paper introduces AssemblyGrid v1, a reproducible benchmark for repeated multi-robot production that combines explicit process progression, decentralized observations, material transfer, temporary multi-robot coalitions, productive concurrency, and geometry-dependent feasibility within one task-level formulation. The benchmark includes Flow, Coalition, and Concurrency workload families, each with three scenario levels. Task success and evaluation measures are defined independently of learning reward and solution method, allowing learning-based and non-learning methods to address the same production problem. AssemblyGrid v1 is evaluated through executable conformance checks, mechanism studies, and algorithmic experiments using a privileged centralized reference, structured decentralized controllers, and MARL methods including IPPO, MAPPO, and QMIX. Results demonstrate productive execution under centralized and decentralized control. The MARL experiments further show that decentralized policies can learn effective production behavior from local observations and actions, supporting AssemblyGrid as a controlled benchmark for studying cooperative decision making in flexible robotic production.

</details>

---

### [[20_Research/Papers/具身智能/Managing_Action_Preconditions_in_Neuro-Symbolic_RL_Three_Placement_Strategies_for_Embodied_Agents|Managing Action Preconditions in Neuro-Symbolic RL: Three Placement Strategies for Embodied Agents]]

![[assets/2609.16056_first_page.png|800]]

- **arXiv**: [2609.16056](https://arxiv.org/abs/2609.16056)
- **PDF**: https://arxiv.org/pdf/2609.16056
- **详细分析**: [[20_Research/Papers/具身智能/Managing_Action_Preconditions_in_Neuro-Symbolic_RL_Three_Placement_Strategies_for_Embodied_Agents|Managing Action Preconditions in Neuro-Symbolic RL: Three Placement Strategies for Embodied Agents]]
- **作者**: Norbert Oswald, Fabian Deuser, Thomas Bräunl
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习, 世界模型
- **相关性评分**: 2.22（加权：具身智能 1.2，大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Managing Action Preconditions in Neuro-Symbolic RL: Three Placement Strategies for Embodied Agents》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans carry behaviour knowledge of how to act in familiar situations into every new task rather than relearning it from scratch. There is no reason a Reinforcement Learning (RL) agent shouldn't do the same: known behaviour patterns need not be learned, only applied. Neuro-symbolic RL bridges prior knowledge and RL by injecting symbolic knowledge alongside a learned policy. The point at which this knowledge is integrated is critical: a poor choice can produce, for instance, hallucinated preconditions, which surface as safety and reliability problems in agents acting in changing environments. We formalise this behavioural knowledge as a precondition Bayesian network (BN) over the agent's \emph{structural actions} - the actions whose legality depends on preconditions, such as picking up a key, grasping a block, toggling a door, or dropping an object. The BN restricts when these actions may fire, and we inject it into the RL loop at three placements: (1) a \emph{symbolic verifier}, consulted only at inference, that fires a structural action once its preconditions hold; (2) a \emph{symbolic enforcer}, active during both training and inference, that governs structural-action use throughout learning; and (3) a \emph{symbolic learner}, which folds the knowledge into the network and learns the restriction and use of structural actions itself. To test the three variants we run experiments on two benchmarks with opposite regimes: one built on long, ordered planning chains, the other on continuous manipulation. We compare against strong baselines on solution quality, sample efficiency, and traceability. The payoff is substantial. On MiniGrid, all three placements improve the \emph{solution quality} over the PPO+RND baseline, the symbolic enforcer leading at $98.2\%$ against the baseline's $88.8\%$. On Fetch, $\dots$

</details>

---

### [[20_Research/Papers/大模型/Retrieval-Driven_Memory_Reconsolidation_for_Long-Term_LLM_Agents|Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents]]

![[assets/2609.16053_figure.png|800]]

- **arXiv**: [2609.16053](https://arxiv.org/abs/2609.16053)
- **PDF**: https://arxiv.org/pdf/2609.16053
- **详细分析**: [[20_Research/Papers/大模型/Retrieval-Driven_Memory_Reconsolidation_for_Long-Term_LLM_Agents|Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents]]
- **作者**: Yuanyi Song, Yukai Wang, Xinbei Ma, Zhihui Fu, Jianghao Lin, Weiwen Liu, Jun Wang, Huarong Deng, Yong Yu, Weinan Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Retrieval-Driven Memory Reconsolidation for Long-Term LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory is essential for LLM-based agents operating over extended interactions. Existing memory systems primarily update memory when new information arrives, treating retrieval as the endpoint of memory access rather than a driver of memory evolution. Consequently, retrieval feedback is rarely exploited to reorganize memory for future access continuously. Moreover, most existing approaches rely on predefined memory structures together with fixed retrieval pipelines, limiting the agent's ability to organize and evolve its own memory autonomously. Inspired by memory reconsolidation in cognitive neuroscience, we propose \textbf{REALM}, a \textbf{r}econsolidation-\textbf{e}volution \textbf{a}gentic \textbf{l}ong-term \textbf{m}emory framework. It models long-term memory as a continual lifecycle by autonomously organizing memories into a heterogeneous cognitive graph, retrieving evidence via adaptively composed graph-search atoms, and continually reconsolidating memories based on retrieval feedback. REALM achieves an average accuracy of 75.97\% on LoCoMo and 65.11\% on LongMemEval, outperforming the strongest baselines by 7.17 and 1.31 points respectively. Ablation studies confirm that memory reconsolidation consistently boosts performance, with further analyses revealing that it progressively reorganizes related memory units into more coherent local structures for collective evidence recall and utilization during reasoning. These results suggest that retrieval-driven memory reconsolidation provides an effective mechanism for continually evolving long-term memory in LLM agents.

</details>

---

### [[20_Research/Papers/机器人/Estimating_Uncertain_Spatial_Relationships_in_Robotics|Estimating Uncertain Spatial Relationships in Robotics]]

![[assets/1304.3111_first_page.png|800]]

- **arXiv**: [1304.3111](https://arxiv.org/abs/1304.3111)
- **PDF**: https://arxiv.org/pdf/1304.3111
- **详细分析**: [[20_Research/Papers/机器人/Estimating_Uncertain_Spatial_Relationships_in_Robotics|Estimating Uncertain Spatial Relationships in Robotics]]
- **作者**: Randall Smith, Matthew Self, Peter Cheeseman
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《Estimating Uncertain Spatial Relationships in Robotics》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we describe a representation for spatial information, called the stochastic map, and associated procedures for building it, reading information from it, and revising it incrementally as new information is obtained. The map contains the estimates of relationships among objects in the map, and their uncertainties, given all the available information. The procedures provide a general solution to the problem of estimating uncertain relative spatial relationships. The estimates are probabilistic in nature, an advance over the previous, very conservative, worst-case approaches to the problem. Finally, the procedures are developed in the context of state-estimation and filtering theory, which provides a solid basis for numerous extensions.

</details>

---
