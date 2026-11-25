# cs.AI | Artificial Intelligence | 2026-11-23

#arxiv #ComputerScience

**论文数**: 36

### [[20_Research/Papers/世界模型/Non-penetrating_World_Models|Non-penetrating World Models]]

![[assets/2611.27963_figure.png|800]]

- **arXiv**: [2611.27963](https://arxiv.org/abs/2611.27963)
- **PDF**: https://arxiv.org/pdf/2611.27963
- **详细分析**: [[20_Research/Papers/世界模型/Non-penetrating_World_Models|Non-penetrating World Models]]
- **作者**: Yuhang Dai, Yinwei Wu, Ziyue Lin, Han Ji, Xingyi Yang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Non-penetrating World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LingBot-World, NoPeBench, NoPeWorld, WBench, WorldRoamBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study a new problem of preventing object penetration in interactive video world models. To understand how existing models handle this, we introduce NoPeBench, a benchmark that evaluates how world models respond to physical obstacles. Our evaluation reveals that none of the open-source models can reliably prevent such failures. Surprisingly, however, these models already encode the information needed to predict such violations. We find that the hidden states of diffusion transformers (DiTs) can predict whether a candidate action will penetrate an obstacle. Building on this, we introduce NoPeWorld, a lightweight framework that detects and prevents penetration. Specifically, we train a small prediction head on top of a frozen DiT's hidden states to read out if a candidate action is safe or not. Unsafe actions are then replaced with safe ones that best preserve the original intent. Despite its simplicity, NoPeWorld substantially reduces the physical violation rate, averaged over six video world models, from 74% to 16%. Remarkably, our method shows zero-shot generalization to open-domain imagery, third-person viewpoints, and moving obstacles. We publicly release our code, the NoPeBench benchmark, and model weights. Project Page: https://nopeworld.github.io .

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Visual_Fidelity_Comparing_Categorical_and_Continuous_World_Models|Beyond Visual Fidelity: Comparing Categorical and Continuous World Models]]

![[assets/2611.27870_figure.png|800]]

- **arXiv**: [2611.27870](https://arxiv.org/abs/2611.27870)
- **PDF**: https://arxiv.org/pdf/2611.27870
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Visual_Fidelity_Comparing_Categorical_and_Continuous_World_Models|Beyond Visual Fidelity: Comparing Categorical and Continuous World Models]]
- **作者**: Sarah Parisot, Melanie Fernandez Pradier, David Bignell, Sergio Valcarcel Macua, Katja Hofmann
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Beyond Visual Fidelity: Comparing Categorical and Continuous World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VBench, World-in-World, WorldModelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual world models can now generate compelling interactive worlds, but visual realism does not guarantee faithful dynamics. We systematically compare how categorical and continuous prediction shape learned dynamics under both next-token and iterative whole-frame generation. These choices are often bundled in approaches such as autoregressive token models and whole-frame flow matching. We design controlled 2D and 3D environments and evaluate dynamics validity, calibration, and visual quality. In 2D with lossless visual encoding, categorical models achieve higher rollout validity with less training compute, particularly for stochastic entities. Among categorical models, greedy decoding produces the highest rollout validity, while sampling from a next-token model yields the best-calibrated stochastic predictions. Failures in continuous models, such as disappearing game characters, echo those seen in more complex environments. Here, known dynamics let us measure their impact. In 3D, categorical models also achieve stronger long-horizon performance with less training compute. Even models with lossy tokenization remain competitive on semantic accuracy and FVD, despite lower next-frame RGB accuracy. Together, these findings make a strong case for categorical prediction as a compute-efficient route to learning world dynamics.

</details>

---

### [[20_Research/Papers/强化学习/SLICR_Strategy_Logic-Guided_Multi-Agent_Reinforcement_Learning|SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning]]

![[assets/2611.27865_figure.png|800]]

- **arXiv**: [2611.27865](https://arxiv.org/abs/2611.27865)
- **PDF**: https://arxiv.org/pdf/2611.27865
- **详细分析**: [[20_Research/Papers/强化学习/SLICR_Strategy_Logic-Guided_Multi-Agent_Reinforcement_Learning|SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning]]
- **作者**: Arshia Rafieioskouie, Matthew Lucas, Tzu-Han Hsu, Borzoo Bonakdarpour
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《SLICR: Strategy Logic-Guided Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Specification-guided reinforcement learning (RL) translates formal specifications of desired behavior of agents into shaped rewards. This paper introduces SLICR, a significant paradigm shift that advances the state of the art to specification-guided RL in adversarial settings under partial observability. We employ Strategy Logic (SL), which allows explicit quantification over agents' strategies and uses the linear temporal logic (LTL) to specify the agents' objectives and constraints. This enables reasoning not only about how agents should act to satisfy a specification, but also about how they should respond to the strategies and behaviors of other agents. We evaluate SLICR on three popular benchmarks: Predator-Prey, Google Research Football, and our home-grown extension of SMAC-HARD, demonstrating its effectiveness, scalability, and ability to adapt to diverse adversarial strategies.

</details>

---

### [[20_Research/Papers/大模型/Search-RSI_Expanding_Search_Worlds_Along_Multimodal_Agents'_Capability_Frontier|Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier]]

![[assets/2611.27780_figure.png|800]]

- **arXiv**: [2611.27780](https://arxiv.org/abs/2611.27780)
- **PDF**: https://arxiv.org/pdf/2611.27780
- **详细分析**: [[20_Research/Papers/大模型/Search-RSI_Expanding_Search_Worlds_Along_Multimodal_Agents'_Capability_Frontier|Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier]]
- **作者**: Chengchao Lv, Yin Wang, Chunzheng Zhu, Wanli Chang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.1（加权：大模型 0.9，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Search-RSI: Expanding Search Worlds Along Multimodal Agents' Capability Frontier》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal search agents answer knowledge intensive visual questions by grounding them in retrieved evidence, and recent recipes train them on multi hop tasks that are synthesized from knowledge graphs and grown online to keep pace with the agent. These recipes, however, treat the searchable world as fixed: a new question can be well formed and verifiable while its evidence is absent from the retrieval backend, so the agent issues the right query, retrieves nothing, and is penalized as if its policy were at fault. Such unreachable negatives accumulate with every round of growth. We propose Search-RSI, a recursive self improvement framework that expands the search world along the agent's capability frontier. In each round, the current policy diagnoses its partially mastered regions of a task space spanned by hop depth, relation rarity, and distractor density; new tasks there are grown together with their evidence; and the same policy decides how they are used: candidates on which its probes disagree feed reinforcement learning, while those beyond its reach become hint guided demonstrations of its own. Keeping the policy inside this loop matters: an improver frozen at the start of training loses 3.2 points. On nine multimodal search benchmarks, Search-RSI keeps improving where static task growth saturates, raising the average accuracy of the recipe it builds on by 9.8 and 9.5 points at 9B and 27B, of which 7.0 points are out of reach for a world that is merely made consistent. The loop uses no external model and only privileged task structure that is removed before training, at 1.27x the compute of static growth.

</details>

---

### [[20_Research/Papers/具身智能/Embodied-Harness_Towards_Recursive_Self-Improvement_for_Robotic_Manipulation|Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation]]

![[assets/2611.27689_figure.png|800]]

- **arXiv**: [2611.27689](https://arxiv.org/abs/2611.27689)
- **PDF**: https://arxiv.org/pdf/2611.27689
- **详细分析**: [[20_Research/Papers/具身智能/Embodied-Harness_Towards_Recursive_Self-Improvement_for_Robotic_Manipulation|Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation]]
- **作者**: Zhenxuan Fan, Zhuoya Wang, Yuqian Yuan, Wenqiao Zhang, Juncheng Li, Jun Xiao, Siliang Tang, Yueting Zhuang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.5（加权：具身智能 2.7，大模型 0.5，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Embodied-Harness: Towards Recursive Self-Improvement for Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgiBot-World, RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language model (VLM)-based agents offer a promising approach to robotic manipulation, yet remain limited by inadequate memory organization, uncertain failure attribution, and limited reuse of execution experience. We propose Embodied-Harness, a dual-agent framework that improves manipulation by refining the execution harness without updating model parameters. The Actor interacts with the environment through a robot-control interface, while the Reflector converts execution evidence into reusable operational guidance. Hierarchical Memory Architecture maintains short-term execution context and long-term experiential knowledge to support execution and reflection. Evidence-based Experience Reflection grounds failure diagnosis in observed interactions, while Recursive Harness Self-Improvement refines operational guidance across successive attempts. Experiments on RoboTwin 2.0, RoboSPA, and RMBench demonstrate the effectiveness of Embodied-Harness in generalization under environmental variations, spatial reasoning, long-horizon planning, and memory-dependent manipulation. Our method achieves success rates of 82.4%, 76.7%, and 94.4% on the three benchmarks, respectively. Real-world evaluation further yields an average success rate of 96.7% across three manipulation tasks. These results highlight the potential of Embodied-Harness to improve robotic manipulation through experience-driven harness self-improvement.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Inside_Types_Epistemic_Typestates_for_Safe_Multi-Agent_Reinforcement_Learning|Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning]]

![[assets/2611.27631_first_page.png|800]]

- **arXiv**: [2611.27631](https://arxiv.org/abs/2611.27631)
- **PDF**: https://arxiv.org/pdf/2611.27631
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Inside_Types_Epistemic_Typestates_for_Safe_Multi-Agent_Reinforcement_Learning|Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning]]
- **作者**: Lorenzo Bacchiani, Mario Bravetti, Giovanni Pau, Roberto Girau
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Learning Inside Types: Epistemic Typestates for Safe Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Type disciplines make programs safe by construction: components checked against each other's types compose into programs that cannot go wrong in the ways the types exclude. Types suit reinforcement learning: a type constrains what an agent may choose, not how it chooses, so the guarantee holds for every policy a learner produces. We introduce epistemic typestates, a type discipline for safe multi-agent reinforcement learning. An agent's type is a protocol whose states record its beliefs, the worlds it cannot rule out from its own observations and actions, and permits only actions that are safe in every world of the belief, whatever the others do within their public types. Agents learn inside their types, which are built and checked one agent at a time and run without communication. We prove type soundness and team safety, give a synthesis that is sound and complete, build types from guards when worlds are infinite, and show that shields are a special case. All proofs are mechanised in Rocq. On nine benchmarks, no typed learner causes a safety violation, and task performance does not differ significantly from that of two recent multi-agent shielding methods. Where a contract-based method fails at five and ten agents, types for ten agents are built in under a second. In the two continuous benchmarks, Lagrangian learners cause thousands of violations in every training run.

</details>

---

### [[20_Research/Papers/大模型/Potential_emergence_in_LLM_agents_a_statistical_physics_perspective|Potential emergence in LLM agents: a statistical physics perspective]]

![[assets/2611.27618_figure.png|800]]

- **arXiv**: [2611.27618](https://arxiv.org/abs/2611.27618)
- **PDF**: https://arxiv.org/pdf/2611.27618
- **详细分析**: [[20_Research/Papers/大模型/Potential_emergence_in_LLM_agents_a_statistical_physics_perspective|Potential emergence in LLM agents: a statistical physics perspective]]
- **作者**: Zhuo-Yang Song, Hua Xing Zhu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Potential emergence in LLM agents: a statistical physics perspective》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

There has been significant recent interest in understanding the behaviour of LLM agents from the perspective of human preferences or corpus statistics. In this paper we propose agent states as intermediate variables through which post-training can be measured and predicted. From a statistical physics perspective, we study the emergence of a global potential which governs the transition of state in LLM agent reasoning. We introduce a partition function to model the ideal KL-regularised transition distribution and track potential structure, mean reward and state entropy. We demonstrate our approach in two Qwen3.5-9B tasks: safety-test selection and physics-reasoning auditing. We observe that the potential structure strengthens during post-training as predicted from our framework, while joint changes in reward and state entropy provide consistency evidence. States thus provide a quantitative description of how post-training organises agent behaviour.

</details>

---

### [[20_Research/Papers/大模型/Bringing_AI_Assistance_to_the_Beznau_Nuclear_Power_Plant_A_Hierarchical_System_of_LLM_Agents_for_Reactor_Monitoring|Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring]]

![[assets/2611.27556_figure.png|800]]

- **arXiv**: [2611.27556](https://arxiv.org/abs/2611.27556)
- **PDF**: https://arxiv.org/pdf/2611.27556
- **详细分析**: [[20_Research/Papers/大模型/Bringing_AI_Assistance_to_the_Beznau_Nuclear_Power_Plant_A_Hierarchical_System_of_LLM_Agents_for_Reactor_Monitoring|Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring]]
- **作者**: Wenqi Zhou, Leonardo Baldo, Edwin Kolbe, Manuel Arias Chao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Bringing AI Assistance to the Beznau Nuclear Power Plant: A Hierarchical System of LLM Agents for Reactor Monitoring》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Beznau Unit 1 in Switzerland, in operation since 1969, is the most experienced nuclear reactor still running worldwide. Five decades of incremental modernization have left its monitoring systems, alarm logs, variable catalogs, technical specifications and investigation reports in separate silos that were never designed to be queried together. As a result, investigating a core instrumentation anomaly means slow, manual gathering of knowledge scattered across databases, documents, and experienced colleagues. We present a hierarchical multi-agent assistant built on large language models (LLMs) to support these investigations and reduce the need for tedious manual searches in SAP systems. An orchestrating agent breaks down an engineer's question and hands the parts to specialized sub-agents, each with read-only access to one source. Domain expertise is written as natural-language procedures that plant engineers can read, review and revise. The system is strictly advisory, with every answer traced back to its sources. We also report organizational lessons from introducing agentic AI into a culture built on safety, traceability and conservative change. Beyond the technical architecture, the Beznau case study examines how an assistant can be introduced into a setting where evidence must be traceable, changes carefully reviewed, and operational decisions retained by plant personnel, paving the way for the responsible use of agentic AI in industrial plant monitoring.

</details>

---

### [[20_Research/Papers/大模型/Efficient_Natural_Language_to_Temporal_Logic_Translation_for_Real-Time_Physical_AI|Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI]]

![[assets/2611.27489_first_page.png|800]]

- **arXiv**: [2611.27489](https://arxiv.org/abs/2611.27489)
- **PDF**: https://arxiv.org/pdf/2611.27489
- **详细分析**: [[20_Research/Papers/大模型/Efficient_Natural_Language_to_Temporal_Logic_Translation_for_Real-Time_Physical_AI|Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI]]
- **作者**: Oliver Schön, Adrien Banse, John Lygeros, Lars Lindemann
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.05（加权：具身智能 0.3，大模型 0.25，机器人 0.5）
- **关联关键词**: LLM, Robotics, Systems

#### 研究背景与动机

《Efficient Natural Language to Temporal Logic Translation for Real-Time Physical AI》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots can be controlled to perform tasks with guaranteed correctness when the task instructions are stated in a formal language. Large language models (LLMs) have been widely used to allow users to provide such instructions in natural language (NL), by translating NL into formal language. When deploying such translators on a robot, however, we face limited computing and energy resources, while offloading computation or data to the cloud may be infeasible or undesirable. Yet an LLM is a general-purpose text generator, whereas a formula in a fixed formal language fragment follows a well-defined syntax. We therefore ask whether text generation is needed at all. For the formal language of linear temporal logic (LTL), we show that this translation can instead be broken down into answering a set of questions with pre-defined answers. We then construct a System-One model, a recent class of NL-based classifier, to provide such answers and enable us to translate a natural language instruction into an LTL instruction. On three benchmarks, our translator matches or exceeds the accuracy of the best local LLMs available, at up to one order of magnitude lower runtime and energy consumption. We show that it generalizes to unseen atomic propositions and temporal patterns.

</details>

---

### [[20_Research/Papers/机器人/ROSWORLD_When_Digital_Task_Competence_Meets_Physical_Execution|ROSWORLD: When Digital Task Competence Meets Physical Execution]]

![[assets/2611.27467_figure.png|800]]

- **arXiv**: [2611.27467](https://arxiv.org/abs/2611.27467)
- **PDF**: https://arxiv.org/pdf/2611.27467
- **详细分析**: [[20_Research/Papers/机器人/ROSWORLD_When_Digital_Task_Competence_Meets_Physical_Execution|ROSWORLD: When Digital Task Competence Meets Physical Execution]]
- **作者**: Caoyuan Ma, Wendi Liu, Zhimin Zhang, Muyao Niu, Yujie Lu, Zengxi Zhang, Ji Zhao, Shuai Dong, Wenpu Liu, Ziyue Wang, Wenzheng Chang, Taiqiang Wu...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ROSWORLD: When Digital Task Competence Meets Physical Execution》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, EmbodiedBench, Meta-World, OSWorld, OpenVLA, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-use agents now solve most desktop tasks through direct software input, but a robot using the same computer must turn GUI knowledge into physical contact with a keyboard and mouse. We introduce ROSWorld, a benchmark that couples a physically simulated robot workstation to a live OSWorld desktop, so that a robot and a desktop agent pursue the same goals under the same official evaluators. The evaluated model receives observations only from the workstation camera views and operates the peripherals through either a single-arm rigid probe or dual-arm dexterous hands. Across five frontier models and 40 tasks in ten applications, models that complete 31-39 tasks on the desktop complete at most 23 with the probe and 28 with the hands. Paired trajectory analysis shows that models adapt their interaction strategies toward keyboard input, yet physical execution frequently fails through missed presses, incorrect targets, and unintended contacts. ROSWorld makes the gap between knowing what to do on a computer and physically doing it measurable.

</details>

---

### [[20_Research/Papers/具身智能/Learning_When_to_Ask_Advisor-Aware_Post-Training_for_SLM_Agents|Learning When to Ask: Advisor-Aware Post-Training for SLM Agents]]

![[assets/2611.27443_first_page.png|800]]

- **arXiv**: [2611.27443](https://arxiv.org/abs/2611.27443)
- **PDF**: https://arxiv.org/pdf/2611.27443
- **详细分析**: [[20_Research/Papers/具身智能/Learning_When_to_Ask_Advisor-Aware_Post-Training_for_SLM_Agents|Learning When to Ask: Advisor-Aware Post-Training for SLM Agents]]
- **作者**: Aasheesh Singh, Vishal Vaddina
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 具身智能, 世界模型
- **相关性评分**: 1.12（加权：具身智能 0.3，大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Learning When to Ask: Advisor-Aware Post-Training for SLM Agents》归入 强化学习、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：LiveCodeBench, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small language models (SLMs) are increasingly attractive for cheap, high-throughput agentic deployment, but they remain weak at multi-step reasoning and tool use that long-horizon tasks demand. We study how to post-train an SLM to seek advice from a stronger model and act on that advice itself, following an advisor-executor pattern. Out of the box, this pattern fails across open- and closed-source small-model families: wiring an SLM to an advisor is a harness-design matter that is not enough on its own. A post-training recipe is needed to teach the model when to ask, in a cost-aware fashion, and how to follow advice across steps. Our method, ADAPT (ADvisor-Aware Post-Training), is a multi-stage recipe that instills this behavior, learning entirely from the policy's own rollouts supervised by the environment's outcome, with no learned reward model or human annotation. Across three domains, compared to an untrained harness baseline, ADAPT improves success rate in embodied text reasoning (TextWorld) from 24.5% to 77.3%, code generation (LiveCodeBench) from 21.8% to 56.0%, and deep web search (GAIA) from 17.5% to 49.3%, while querying the advisor sparingly (~1.0-2.1 calls per task). On the two long-horizon domains it closes 70-85% of the gap to an oracle that perfectly times when to ask for advice, and on code generation it exceeds that oracle. The gains persist when the advisor is replaced by one unseen in training, showing that the learned help-seeking policy is robust to a changing advisor rather than tied to the one it was trained with.

</details>

---

### [[20_Research/Papers/机器人/ADEPT_Adaptive_Monocular_Depth_Estimation_via_Model-In-The-Loop_Photometric_Tuning_with_Capture_Risk_Prediction|ADEPT: Adaptive Monocular Depth Estimation via Model-In-The-Loop Photometric Tuning with Capture Risk Prediction]]

![[assets/2611.27423_figure.png|800]]

- **arXiv**: [2611.27423](https://arxiv.org/abs/2611.27423)
- **PDF**: https://arxiv.org/pdf/2611.27423
- **详细分析**: [[20_Research/Papers/机器人/ADEPT_Adaptive_Monocular_Depth_Estimation_via_Model-In-The-Loop_Photometric_Tuning_with_Capture_Risk_Prediction|ADEPT: Adaptive Monocular Depth Estimation via Model-In-The-Loop Photometric Tuning with Capture Risk Prediction]]
- **作者**: GiHyun Kim, JinMo Yang, Hyung-Sin Kim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《ADEPT: Adaptive Monocular Depth Estimation via Model-In-The-Loop Photometric Tuning with Capture Risk Prediction》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exposure and gain determine the visual evidence available to monocular depth estimation (MDE), particularly when robot motion creates a tradeoff between light collection and motion blur. We present ADEPT, a framework that adapts these settings using learned feedback from a frozen depth model. During training, ground-truth depth identifies the lowest-error reference within a group of physically evaluated camera settings. A compact predictor learns reference-relative disagreement (RRD) between each candidate's depth prediction and the reference prediction using regression and ranking losses. At deployment, it scores observed captures using frozen-model features and camera, motion, and illumination context, without ground truth or reference images. A contextual Gaussian-process controller uses recent scores to select subsequent exposure and gain settings under motion and photometric constraints. We evaluate offline camera selection with relative and metric Depth Anything v2 and demonstrate online control with the affine-invariant variant on a mobile robot. Across nine equally weighted scene-illumination conditions, ADEPT reduces mean scale-and-shift-aligned $\mathrm{Abs}_{\mathrm{rel}}$ by 14.6% relative to built-in auto-exposure and by 10.0% relative to the best-performing evaluated prior controller.

</details>

---

### [[20_Research/Papers/机器人/PanoUAV-Track_Full-Spherical_UAV_Visual_Tracking_in_the_Wild|PanoUAV-Track: Full-Spherical UAV Visual Tracking in the Wild]]

![[assets/2611.27383_figure.png|800]]

- **arXiv**: [2611.27383](https://arxiv.org/abs/2611.27383)
- **PDF**: https://arxiv.org/pdf/2611.27383
- **详细分析**: [[20_Research/Papers/机器人/PanoUAV-Track_Full-Spherical_UAV_Visual_Tracking_in_the_Wild|PanoUAV-Track: Full-Spherical UAV Visual Tracking in the Wild]]
- **作者**: Bingyu Li, Lichang Yang, Zhiyuan Zhao, Junyu Gao, Xuelong Li
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《PanoUAV-Track: Full-Spherical UAV Visual Tracking in the Wild》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：TrackingNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing UAV tracking benchmarks predominantly rely on perspective cameras with limited fields of view. Omnidirectional cameras enable full-spherical observation, yet tracking from moving UAV platforms remains largely unexplored. Unlike ground-level panoramic tracking, UAV-mounted omnidirectional cameras observe targets across both azimuth and elevation, introducing geometric challenges under equirectangular projection (ERP). To investigate this setting, we capture approximately \textbf{40 hours of real-world 8K panoramic UAV video} and construct \textbf{PanoUAV-Track} through temporal clip extraction, target annotation, and the integration of simulated sequences. The resulting benchmark comprises 1,895 sequences, 507,961 frames, and 2,872 annotated objects, covering real-world daytime and nighttime scenes alongside simulation, and supporting both visual and language-based target specification. Through extensive evaluations, we reveal a clear \textbf{perspective-to-spherical} generalization gap and identify tracking degradation associated with latitude-dependent distortion and ERP seam discontinuity. To address these challenges, we propose \textbf{PanoUAV-Tracker (PUTrack)}, a geometry-aware tracking framework combining latitude-adaptive search and seam-aware periodic sampling. PUTrack improves zero-shot and in-domain tracking, particularly for seam-crossing targets. Code and benchmark resources will be available\footnote{\textcolor{tabpink}{https://libingyu01.github.io/PanoUAV-Track/}}.

</details>

---

### [[20_Research/Papers/强化学习/Testing_for_Coordination_Failures_in_Cooperative_Multi-Agent_Reinforcement_Learning|Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning]]

![[assets/2611.27368_first_page.png|800]]

- **arXiv**: [2611.27368](https://arxiv.org/abs/2611.27368)
- **PDF**: https://arxiv.org/pdf/2611.27368
- **详细分析**: [[20_Research/Papers/强化学习/Testing_for_Coordination_Failures_in_Cooperative_Multi-Agent_Reinforcement_Learning|Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning]]
- **作者**: Dennis Gross, Jørn Eirik Betten, Helge Spieker
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Testing for Coordination Failures in Cooperative Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CMARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep parallel cooperative multi-agent reinforcement learning (CMARL)} trains multiple agents that all act at every time step to optimize a common objective. Like single-agent RL, CMARL can produce unsafe behaviors that violate implicit safety requirements not captured by the reward, and these behaviors are hard to explain. However, testing CMARL policies for safety has received less attention than the safety testing of single-agent RL policies. In this paper, we propose DisQ, a test case selection method that identifies failure-revealing states in value-based CMARL by exploiting a signal specific to trained Q-learning agents. The signal is the Q-value gap, an explainable metric that flags a state when the agents' estimates of the achievable return diverge by more than a calibrated threshold. DisQ selects such states for execution and skips those without a gap. Our experiments in four CMARL benchmark environments show that, in most of the evaluated configurations, DisQ improves failure detection over single-agent RL testing methods applied to CMARL, namely random testing and search-based testing with genetic algorithms. Our main contributions are the Q-value gap, an indicator of potential miscoordination computable from a single state without executing the system, and DisQ, a test case selection method that adapts existing single-agent testing methods to CMARL.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Interaction_Dynamics_via_Motion-Region_Guidance_for_Robotic_Video_World_Models|Learning Interaction Dynamics via Motion-Region Guidance for Robotic Video World Models]]

![[assets/2611.27344_figure.png|800]]

- **arXiv**: [2611.27344](https://arxiv.org/abs/2611.27344)
- **PDF**: https://arxiv.org/pdf/2611.27344
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Interaction_Dynamics_via_Motion-Region_Guidance_for_Robotic_Video_World_Models|Learning Interaction Dynamics via Motion-Region Guidance for Robotic Video World Models]]
- **作者**: Yongkang He, Xiaofen Xing, Xiangmin Xu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Learning Interaction Dynamics via Motion-Region Guidance for Robotic Video World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, GigaWorld, MoReWorld, PointWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video world models imagine future observations under candidate robot actions, providing a promising visual tool for robot policy evaluation and interaction simulation. However, existing video world models often optimize global reconstruction errors instead of emphasizing interaction-relevant regions. As a result, they may preserve overall scene appearance but overlook local interaction details, leading to physically implausible outcomes such as hallucinated contact effects and inconsistent robot-object interactions. We introduce MoReWorld, a unified motion-region-guided framework that uses a shared motion region, the part of the environment that moves in response to the robot's actions, to focus dynamics learning and video generation on interaction-relevant regions. The same motion region guides local motion prediction, region-aware supervision, and motion-gated future-feature conditioning. At inference time, the motion region is predicted as a motion probability map from visual history and robot actions, without requiring future observations or ground-truth motion labels. On WorldSimProbe, MoReWorld achieves the highest overall simulator-faithfulness score, with the strongest performance on local consistency, global consistency, and interaction dynamics. These results indicate that motion-region guidance helps the model preserve scene-level consistency while more faithfully predicting action-conditioned interaction dynamics.

</details>

---

### [[20_Research/Papers/具身智能/$γ$-Scape_An_Agent-Centric_World_for_Mobile_Embodied_Intelligence|$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence]]

![[assets/2611.27306_figure.png|800]]

- **arXiv**: [2611.27306](https://arxiv.org/abs/2611.27306)
- **PDF**: https://arxiv.org/pdf/2611.27306
- **详细分析**: [[20_Research/Papers/具身智能/$γ$-Scape_An_Agent-Centric_World_for_Mobile_Embodied_Intelligence|$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence]]
- **作者**: Xiaotao Zhang, Lin Qian, Hao Zhang, Xuanrui Cui, Yuehao Huang, Yunzi Wu, Yucheng Deng, Jiankun Dong, Hujun Yin, Xinhai Li, Chenjia Bai, Xuelong Li
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，大模型 0.5，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《$γ$-Scape: An Agent-Centric World for Mobile Embodied Intelligence》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EmbodiedCLBench, GN-Bench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent embodied agents construct and adapt robot behavior through executable programs, tool use, and interaction feedback. Studying these systems in mobile manipulation calls for physical worlds that connect agent-directed execution with its physical consequences and reusable interaction experience. We introduce $γ$-Scape, an agent-centric simulation and benchmark platform for mobile embodied intelligence. Agents compose motion tools and learned skills to carry out complete tasks that combine navigation and manipulation in a persistent physical world. BenchForge grounds structured objectives in physical task instances with instructions, reference programs, and goal evaluators, defining task goals while preserving agents' choice of valid solutions. An agentic collection harness further enables agents to produce demonstrations by carrying out contact-rich interactions through sustained control and physical feedback. Assisted reference execution and human guidance provide complementary experience. The resulting tool traces and aligned observation-action records support program refinement and policy learning, with common task-goal criteria for subsequent evaluation. We benchmark representative agent systems on complete tasks and demonstrate contact collection and trace-informed program revision. Together, these workflows provide infrastructure for research on embodied recursive self-improvement.

</details>

---

### [[20_Research/Papers/具身智能/LiDAR_Signals_for_Robot_Locomotion_Spherical_Range_Images_Enable_Robust_Sim-to-Real_Transfer|LiDAR Signals for Robot Locomotion: Spherical Range Images Enable Robust Sim-to-Real Transfer]]

![[assets/2611.27223_figure.png|800]]

- **arXiv**: [2611.27223](https://arxiv.org/abs/2611.27223)
- **PDF**: https://arxiv.org/pdf/2611.27223
- **详细分析**: [[20_Research/Papers/具身智能/LiDAR_Signals_for_Robot_Locomotion_Spherical_Range_Images_Enable_Robust_Sim-to-Real_Transfer|LiDAR Signals for Robot Locomotion: Spherical Range Images Enable Robust Sim-to-Real Transfer]]
- **作者**: Nian Liu, Xinyi Tong, Ming Ren, Long Ye, Zhaofeng He
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 2.4，机器人 0.6）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《LiDAR Signals for Robot Locomotion: Spherical Range Images Enable Robust Sim-to-Real Transfer》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing legged-locomotion systems commonly rely on depth images or online elevation maps. However, depth-based policies suffer from perceptual sim-to-real discrepancies due to imperfect depth sensor modeling, while map-based approaches are vulnerable to drift and misalignment. LiDAR offers direct measurements of the surrounding geometry, but raw LiDAR scans lack a compact, structured representation for high-frequency control. We propose a LiDAR perception pipeline that maintains perceptual consistency across simulation and reality through sensing- and representation-level alignment. At the sensor level, we recover frame-wise angular sampling patterns from the physical LiDAR and replay them in simulation with GPU ray casting. At the representation level, simulated and real returns undergo the same spherical range image encoding, yielding a fixed-size policy observation for end-to-end training and direct deployment without teacher--student distillation, online elevation mapping, or adaptation. Experiments show that our range-image policies achieve stronger sim-to-real transfer than depth- and elevation-map-based baselines, while ablations confirm the importance of the proposed sensing components. More visualizations and real-world videos are available at the \href{https://lidar-img.github.io/}

</details>

---

### [[20_Research/Papers/具身智能/NavTTT_Adaptive_Parametric_Memory_via_Hierarchical_Test-Time_Training_for_Vision-and-Language_Navigation|NavTTT: Adaptive Parametric Memory via Hierarchical Test-Time Training for Vision-and-Language Navigation]]

![[assets/2611.27219_figure.png|800]]

- **arXiv**: [2611.27219](https://arxiv.org/abs/2611.27219)
- **PDF**: https://arxiv.org/pdf/2611.27219
- **详细分析**: [[20_Research/Papers/具身智能/NavTTT_Adaptive_Parametric_Memory_via_Hierarchical_Test-Time_Training_for_Vision-and-Language_Navigation|NavTTT: Adaptive Parametric Memory via Hierarchical Test-Time Training for Vision-and-Language Navigation]]
- **作者**: Xiaoyu Luo, Chengxing Lin, Jiaxin Huang, Jiale Liu, Jingyu Guo, Sirui Chen, Aolin Li, Shaoli Huang, Cheng-zhong Xu, Hui Kong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《NavTTT: Adaptive Parametric Memory via Hierarchical Test-Time Training for Vision-and-Language Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-and-language navigation (VLN) demands that agents accumulate and reason over streaming visual observations throughout long navigation episodes. Existing approaches struggle to maintain long-term history, constrained by the finite context capacity of transformer architectures. To solve the problem, fast-weight test-time training (TTT) provides a mechanism for encoding streaming observations into an evolving parameter state. However, existing TTT does not distinguish informative observations from repetitive visual content, allowing redundant tokens to interfere with the retention of information needed for subsequent decisions. We propose Navigation-Conditioned Test-Time Training (NavTTT), which introduces adaptive memory formation and hierarchical memory integration for vision-and-language navigation. NavTTT leverages global navigation context to prioritize informative visual evidence and integrates language instructions with spatial information to construct spatially grounded memory representations. Episode-local nonlinear fast weights store these representations as Adaptive Parametric Memory (APM), preserving history beyond the visual context for later decisions. To reduce cross-layer coupling in memory formation, NavTTT maintains independent fast-weight memories across multiple decoder depths. This decoupled design prevents errors or biases from spreading across different memory levels. Meanwhile, it enables shared historical information to be independently represented at various levels of abstraction. Experiments demonstrate strong navigation performance on VLN-CE benchmarks and effective instruction following on a real robot.

</details>

---

### [[20_Research/Papers/大模型/Correct_Precedents_Induce_Policy_Violations_in_On-Device_LLM_Agents|Correct Precedents Induce Policy Violations in On-Device LLM Agents]]

![[assets/2611.27216_figure.png|800]]

- **arXiv**: [2611.27216](https://arxiv.org/abs/2611.27216)
- **PDF**: https://arxiv.org/pdf/2611.27216
- **详细分析**: [[20_Research/Papers/大模型/Correct_Precedents_Induce_Policy_Violations_in_On-Device_LLM_Agents|Correct Precedents Induce Policy Violations in On-Device LLM Agents]]
- **作者**: Chong Tian, Yu Wang, Steve Liu, Qirong Ho, Xiuying Chen
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Correct Precedents Induce Policy Violations in On-Device LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Local-cloud agent systems pair a cloud model with a small on-device agent that acts on private data, often as the last check before an irreversible action. We identify, for the first time, a failure in which such an agent is led into a violation by its own correct decisions within a session. After it correctly releases an item whose restriction was lifted, it becomes more likely to release the next item that is still restricted. Because the trigger is a correct decision, a history with no faulty step can still end in a violation. We call this failure correct-precedent generalization and find it in 13 open-weight models from nine developers. A single correct precedent can cut the safe rate of the most affected agent roughly in half, and the risk compounds when a refused request is simply sent again in a new session. Interventions on the agent's history indicate that it carries its decision on the released item over to the restricted one instead of checking that item's status. Building on this finding, we propose Paired Decision Distillation (PDD), which distills the decisions of a weakly affected teacher into a LoRA adapter. PDD restores the safe rate to nearly 100% in every distilled model, without extra prompt text or model calls.

</details>

---

### [[20_Research/Papers/强化学习/Structure_Over_Scale_Rethinking_Adaptation_for_Reinforcement_Learning_with_Verifiable_Rewards|Structure Over Scale: Rethinking Adaptation for Reinforcement Learning with Verifiable Rewards]]

![[assets/2611.27148_figure.png|800]]

- **arXiv**: [2611.27148](https://arxiv.org/abs/2611.27148)
- **PDF**: https://arxiv.org/pdf/2611.27148
- **详细分析**: [[20_Research/Papers/强化学习/Structure_Over_Scale_Rethinking_Adaptation_for_Reinforcement_Learning_with_Verifiable_Rewards|Structure Over Scale: Rethinking Adaptation for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Allan Kazakov, Abdurrahman Javat
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Structure Over Scale: Rethinking Adaptation for Reinforcement Learning with Verifiable Rewards》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Base-to-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) is often framed as a choice between the expressivity of Full Fine-Tuning (FFT) and the efficiency of Low-Rank Adaptation (LoRA). We find that this framing misses an important variable: the geometry of the update. Under a common cold-start GRPO protocol, LoRA exhibits rank collapse: performance remains broadly stable at low rank, then fails abruptly as rank increases. On DeepMath-Hard, for example, accuracy drops from 73.1% at r=64 to 4.7% at r=128. In contrast, Weight-Decomposed Low-Rank Adaptation (DoRA) and Quantum-Informed Tensor Adaptation (QuanTA) remain stable over a wider tested optimization region and are competitive with FFT while updating less than 0.6% of the model parameters. Spectral analysis reveals a corresponding difference in learned update structure: collapsed LoRA concentrates its update energy into relatively few effective directions, whereas structured adapters produce substantially more distributed updates. These results suggest that nominal rank and parameter count alone are insufficient to characterize adaptation in RLVR - the structure imposed on the reachable update manifold also matters. Finally, across three 8B base models, adapter behavior aligns with both frozen-weight spectral structure and reported pre-training scale, motivating the Model Maturity Hypothesis: the adaptation geometry that works best may depend on properties already encoded during pre-training. We present this as a falsifiable hypothesis rather than a causal conclusion. The code can be found here https://github.com/Shrimpstanot/structure-over-scale

</details>

---

### [[20_Research/Papers/大模型/Do_Senior_Agents_Do_Their_Job_Measuring_Role_Integrity_in_How_LLM_Agents_Use_Subordinate_Material|Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material]]

![[assets/2611.27139_figure.png|800]]

- **arXiv**: [2611.27139](https://arxiv.org/abs/2611.27139)
- **PDF**: https://arxiv.org/pdf/2611.27139
- **详细分析**: [[20_Research/Papers/大模型/Do_Senior_Agents_Do_Their_Job_Measuring_Role_Integrity_in_How_LLM_Agents_Use_Subordinate_Material|Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material]]
- **作者**: Jinxiang Xie, Xinyi Zhang, Changjiang Jiang, Kexu Liu, Qi Yang, Yuxin Su
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Do Senior Agents Do Their Job? Measuring Role Integrity in How LLM Agents Use Subordinate Material》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoRL, RI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems increasingly divide long tasks among subagents whose reports a senior agent turns into the final answer. Such a division of labor pays off only if each agent, and above all the senior agent, carries out the duties of its role. Current evaluations, however, mostly score the final answer, and a fluent, well-cited answer cannot show whether the senior agent weighed its subagents' reports or merely aggregated them. To assess whether a senior agent meets its assigned responsibilities, we define role integrity as the preservation of an agent's functional responsibilities when it acts on its subordinates' material. To measure it, we introduce RI-Bench, a behavioral benchmark grounded in the structures and public records of three institutional hierarchies: peer review, appellate adjudication, and parliamentary inquiry. We choose these hierarchies because their rules explicitly assign the senior role a duty toward subordinate material, and together they cover three basic duties: to weigh, to verify, and to relay. Rather than scoring output correctness, we measure how senior agents' outputs respond to controlled changes in subordinate material, using rule-based checks and a rubric-guided LLM judge calibrated against human annotation. Across eight LLMs and over 12,000 agentic episodes, senior agents rarely adopt a planted procedural error (2.9% of rulings) but often follow a majority of generic reviews (up to 71% of decisions) or drop witnesses' stated limitations (up to 65% of cited claims). Obligation prompts reduce these failures without removing them, and they also shift behavior in the control conditions. These findings motivate direct, obligation-specific evaluation of role integrity rather than inferring it from general capability or explicit role instructions. Code and data are available at https://github.com/jxtse/ri-bench.

</details>

---

### [[20_Research/Papers/具身智能/PACE_Policy_Augmentation_and_Compensation_With_Explicit_Disturbance_Estimation_for_Robust_Locomotion|PACE: Policy Augmentation and Compensation With Explicit Disturbance Estimation for Robust Locomotion]]

![[assets/2611.27061_figure.png|800]]

- **arXiv**: [2611.27061](https://arxiv.org/abs/2611.27061)
- **PDF**: https://arxiv.org/pdf/2611.27061
- **详细分析**: [[20_Research/Papers/具身智能/PACE_Policy_Augmentation_and_Compensation_With_Explicit_Disturbance_Estimation_for_Robust_Locomotion|PACE: Policy Augmentation and Compensation With Explicit Disturbance Estimation for Robust Locomotion]]
- **作者**: Shixuan Han, Yuyang Wang, Jingting Jia, Zeshuai Chen, Jindou Jia, Kexin Guo, Xiang Yu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《PACE: Policy Augmentation and Compensation With Explicit Disturbance Estimation for Robust Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has made quadrupedal locomotion remarkably robust. To handle unmodeled dynamics and external disturbances, domain randomization is usually employed to make a policy hedge against every condition it might meet. However, maintaining accurate tracking across varying dynamics and generalizing beyond the sampled range remain challenging. Here we show that explicitly estimating the disturbance and feeding the resulting estimation back into both the policy and the controller can relax this compromise. We introduce Policy Augmentation and Compensation with Explicit disturbance estimation (PACE). The framework lumps payload variations, center-of-mass (CoM) shifts, actuator degradation, and external forces into one joint-space disturbance. A nonlinear observer subsequently recovers this disturbance online without requiring joint acceleration measurements. The disturbance estimation provides feedforward torque compensation as the foundational control pathway and further augments the policy observation to enable disturbance-aware action generation. Considering the learning difficulty of fast-varying contact effects, we further provide an analytical contact estimation approach from joint and inertial measurements, without demanding force sensors. Across eleven simulated dynamics conditions, PACE reduces velocity-tracking error by 18.1% to 57.0% against state-of-the-art baselines, and maintains improved tracking under out-of-distribution (OOD) commands. Notably, in real-world experiments, the deployed real robot carried an 11.5 kg payload, nearly equal to its own mass. It also negotiated unseen 16 cm step-downs and crossed five outdoor terrains. The policy was trained exclusively on flat ground in simulation with at most 3 kg of added mass.

</details>

---

### [[20_Research/Papers/大模型/Actions_Speak_Louder_than_Words_Stateful_Privacy_Sniffing_of_LLM_Agents_via_Behavioral_Covert_Channels_in_Web_Interactions|Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions]]

![[assets/2611.27046_figure.png|800]]

- **arXiv**: [2611.27046](https://arxiv.org/abs/2611.27046)
- **PDF**: https://arxiv.org/pdf/2611.27046
- **详细分析**: [[20_Research/Papers/大模型/Actions_Speak_Louder_than_Words_Stateful_Privacy_Sniffing_of_LLM_Agents_via_Behavioral_Covert_Channels_in_Web_Interactions|Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions]]
- **作者**: Ruichao Liang, Wenzhong Deng, Jing Chen, Yuqing Li, Kaixuan Li, Cong Wu, Yang Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Actions Speak Louder than Words: Stateful Privacy Sniffing of LLM Agents via Behavioral Covert Channels in Web Interactions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on Web interaction, issuing searches, following links, and reading pages, to complete complex user tasks. Since each action is driven by the agent's private context, including the user's prompt, dialogue history, memory, and connected data, it also opens a new privacy exposure surface. Prior attacks either passively analyze network traffic, which yields only coarse correlations, or hijack the agent through indirect prompt injection, which must place sensitive content in an outgoing field and is blocked by content-level defenses. Whether an attacker can actively recover fine-grained private context without any explicit transmission thus remains insufficiently understood. Our insight is that an agent's benign Web decisions themselves leak private context, as what it chooses to visit encodes whether, which, and in what order it acts, forming a behavioral covert channel. Building on this, we design SNOOP, a stateful hierarchical probing framework that narrows a coarse-to-fine hypothesis tree per task and reconstructs user queries and profiles from the agent's observable paths. Across four agents and three LLM backbones on 500 StackExchange queries and 378 multi-turn iKAT dialogues, SNOOP recovers query concepts with an average F1 of 0.89 and user profiles with an F1 of 0.80, while four representative agent defenses change its recovery by less than 0.03 F1. Since no sensitive content is ever transmitted, content-level inspection cannot detect this leakage; we therefore propose Selection-Obfuscated Retrieval (SOR), which acquires resources under a fixed budget independent of private context and confines the agent's selection to a local snapshot, cutting SNOOP's F1 to 0.39 without additional LLM inference.

</details>

---

### [[20_Research/Papers/具身智能/FoRe_A_Force-Guided_Framework_for_Autonomous_Grasp_Recovery_in_Vision-Language-Action_Models|FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models]]

![[assets/2611.27011_figure.png|800]]

- **arXiv**: [2611.27011](https://arxiv.org/abs/2611.27011)
- **PDF**: https://arxiv.org/pdf/2611.27011
- **详细分析**: [[20_Research/Papers/具身智能/FoRe_A_Force-Guided_Framework_for_Autonomous_Grasp_Recovery_in_Vision-Language-Action_Models|FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models]]
- **作者**: Shuai Peng, Yongkai Liao, Yuxin Cheng, Haoyuan Wang, Jian Huang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.6（加权：具身智能 2.1，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《FoRe: A Force-Guided Framework for Autonomous Grasp Recovery in Vision-Language-Action Models》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, CycleVLA, OpenVLA, ReCoVLA, Real-World, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have demonstrated strong performance in grasp-based manipulation, yet reliable recovery from local grasping failures remains challenging. Specifically, in pick-and-place tasks, policies may continue transport after a failed grasp instead of retrying, potentially reflecting overreliance on proprioceptive cues for stage progression and limited retry supervision. Existing recovery approaches typically rely on deployment-time guidance or demonstration augmentation. We introduce Force-guided Recovery (FoRe), a framework for autonomous recovery from local grasping failures. Using force feedback, FoRe partitions demonstrations into approach-grasp and transport-placement stages to train separate policies. To supplement limited retry supervision, FoRe then initializes a dedicated retry policy from the approach-grasp policy and refines it through local reinforcement learning (RL) from post-failure states. To avoid inappropriate stage progression, a controller combines force feedback with grasp-command status at inference to coordinate the stage policies, detect grasp failures, and invoke the retry policy. We also construct LIBERO-SUCTION, a force-augmented suction manipulation benchmark adapted from LIBERO, with complete demonstration trajectories for policy training. FoRe consistently improves task success rates for VLA-Adapter and $π_{0.5}$ on LIBERO-SUCTION, LIBERO, and real-world tasks. On LIBERO-SUCTION, average absolute gains are 18.4% and 6.5%, respectively. The corresponding real-world absolute gains are 25.0% and 21.7%. FoRe also remains effective with only one demonstration per task on both simulation benchmarks.

</details>

---

### [[20_Research/Papers/大模型/Reward_Integrity_in_Adversarial_Reinforcement_Learning_for_LLM_Guardrail_Red-Teaming|Reward Integrity in Adversarial Reinforcement Learning for LLM Guardrail Red-Teaming]]

![[assets/2611.26998_first_page.png|800]]

- **arXiv**: [2611.26998](https://arxiv.org/abs/2611.26998)
- **PDF**: https://arxiv.org/pdf/2611.26998
- **详细分析**: [[20_Research/Papers/大模型/Reward_Integrity_in_Adversarial_Reinforcement_Learning_for_LLM_Guardrail_Red-Teaming|Reward Integrity in Adversarial Reinforcement Learning for LLM Guardrail Red-Teaming]]
- **作者**: Chengming Liu, Leon Viti, Hongxu Chen, Erdem Kemik, Mary-Anne Williams, Ruth Oliver
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.3，强化学习 0.6）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Reward Integrity in Adversarial Reinforcement Learning for LLM Guardrail Red-Teaming》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AdvPIIBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study reward fidelity in an adversarial reinforcement-learning loop for red-teaming financial-services language-model guardrails. Apparent wins can arise when an attack omits prescribed personally identifiable information (PII), or when a reward judge credits a response that did not break the targeted policy. On attacker-generated and public benchmark examples, TypeSafe Jev checks whether the prescribed PII is present. For outcome scoring, we compare the decision models TypeSafe Jev, Laya (pretrained and post-trained), and pretrained CLM-8B with logged Opus 4.8 judgements from a replay corpus. Post-training markedly improves Laya's agreement with the judge. A separate author-reviewed off-target set establishes that Opus can award false wins. The findings motivate specialised decision-model judges for checking prescribed PII in attack inputs and scoring target responses against the intended policy.

</details>

---

### [[20_Research/Papers/大模型/Partially_canonical_axes_in_large_language_model_representations|Partially canonical axes in large language model representations]]

![[assets/2611.26920_figure.png|800]]

- **arXiv**: [2611.26920](https://arxiv.org/abs/2611.26920)
- **PDF**: https://arxiv.org/pdf/2611.26920
- **详细分析**: [[20_Research/Papers/大模型/Partially_canonical_axes_in_large_language_model_representations|Partially canonical axes in large language model representations]]
- **作者**: Andrea Gregor de Varda, Ferdinando D'Elia, Greta Tuckute, Evelina Fedorenko, Meenakshi Khosla
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《Partially canonical axes in large language model representations》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) develop rich internal representations of language, but whether their individual coordinate axes carry meaning, or whether meaning is encoded only in directions in representation space, is still an open question. A common assumption is that individual axes in LLMs are arbitrary. We here challenge this view: across 12 LLMs from six model families, the native axes are reliably more aligned with other models' representations, with human brain responses to language, and with interpretable linguistic features than randomly rotated axes that preserve the same geometry. The native axes nonetheless fall well short of the best achievable alignment, so LLM coordinates are not fully arbitrary but also not fully canonical: they are partially canonical. A theory of how LLMs represent language must explain both the population geometry they learn and why individual units acquire patterns of response profiles that recur across systems.

</details>

---

### [[20_Research/Papers/具身智能/AstronautBench_Measuring_Agent_Self-Improvement_Across_Episodes_Through_Knowledge,_Evidence,_and_Progress|AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress]]

![[assets/2611.26910_figure.png|800]]

- **arXiv**: [2611.26910](https://arxiv.org/abs/2611.26910)
- **PDF**: https://arxiv.org/pdf/2611.26910
- **详细分析**: [[20_Research/Papers/具身智能/AstronautBench_Measuring_Agent_Self-Improvement_Across_Episodes_Through_Knowledge,_Evidence,_and_Progress|AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress]]
- **作者**: Congyuan Yu, Runping Tian
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.05（加权：具身智能 0.3，大模型 0.75）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《AstronautBench: Measuring Agent Self-Improvement Across Episodes Through Knowledge, Evidence, and Progress》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ASIWorld, AbstainEQA, AdaExploreBench, AstronautBench, DiscoveryWorld, EQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are expected to improve themselves from their own experience across episodes, with fixed weights. Self-improvement in an embodied world cannot be read from one measure. Existing benchmarks measure task progress, world-knowledge question answering (QA), and episodic memory, but a correct answer does not show that the agent ever observed the evidence for it, and progress does not show what the agent learned. We introduce AstronautBench, which measures one agent's self-improvement through three views on the same run: what it knows, whether its own evidence supports that knowledge, and how far it gets in the world. It is built on the game Outer Wilds, where each episode is a 22-minute loop after which the world resets, only the agent's knowledge carries over, and progress is gated by knowledge. After every episode, we measure the places reached and ship-log rumor facts revealed, the correctness of answers to 164 questions about the world, and whether each answer is supported by the frames and position the agent cites from its own recorded play. Two LLM judges from different model families check every answer. In eight-episode baselines with GPT-6.1 Sol and Gemini 4 Argon planners, which act through a learned controller or their own gamepad inputs, the three views do not move together, so any one of them alone gives an incomplete picture of whether the agent is improving. The GPT-6.1 Sol agent's correct answers grow from 14.6% to 26.8% of all questions, but at episode 8 only 59 to 68% of them are supported by its cited evidence. It reveals no new rumor facts after episode 3, while the places it reaches and its memory keep growing. More than half of the answers that become correct after episode 3 cite only evidence from earlier episodes.

</details>

---

### [[20_Research/Papers/强化学习/AI-Assisted_Decision_Support_for_Formula_1_Pit-Stop_Strategy_Deep_Reinforcement_Learning_and_Mathematical_Programming|AI-Assisted Decision Support for Formula 1 Pit-Stop Strategy: Deep Reinforcement Learning and Mathematical Programming]]

![[assets/2611.26909_first_page.png|800]]

- **arXiv**: [2611.26909](https://arxiv.org/abs/2611.26909)
- **PDF**: https://arxiv.org/pdf/2611.26909
- **详细分析**: [[20_Research/Papers/强化学习/AI-Assisted_Decision_Support_for_Formula_1_Pit-Stop_Strategy_Deep_Reinforcement_Learning_and_Mathematical_Programming|AI-Assisted Decision Support for Formula 1 Pit-Stop Strategy: Deep Reinforcement Learning and Mathematical Programming]]
- **作者**: Felipe Méndez, Charles Thraves
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.9（加权：大模型 0.1，强化学习 1.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《AI-Assisted Decision Support for Formula 1 Pit-Stop Strategy: Deep Reinforcement Learning and Mathematical Programming》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pit-stop strategy in Formula 1 is a sequential decision problem under uncertainty, in which strategists decide at each lap whether to pit and which tire compound to fit. We develop a data-driven simulator, calibrated with historical race data, that captures tire degradation, drivers' recent performance, overtaking, yellow flag events, and rivals' pit-stop decisions. We train agents with five Deep Reinforcement Learning (DRL) algorithms and compare them with a Quadratic Mixed-Integer Programming (QMIP) formulation that is optimal in deterministic single-driver settings. Without uncertainty or competition, all DRL methods except TRPO achieve near-optimal performance. With a full grid of competitors and stochastic race events, the ranking of DRL methods depends on the evaluation setting: Proximal Policy Optimization (PPO) and its recurrent variant are the only methods that improve on the QMIP both in fully simulated races and when the actual 2024 races are replayed. Averaged over eight circuits, PPO improves on the QMIP by 0.33 and 0.49 positions in the two settings and Recurrent PPO by less, and in the replay PPO finishes 0.66 positions ahead of the drivers' actual strategies simulated in the same races. The QMIP performs similarly to the other methods, even though it cannot anticipate yellow flag events. Finally, we use the trained PPO policy as a look-ahead decision-support tool that shows the strategist the distribution of race outcomes under each candidate pit-stop action. Applied retrospectively to eight 2024 races, the look-ahead identifies the laps where the actual decision, the recommendation, or a third action was preferable.

</details>

---

### [[20_Research/Papers/具身智能/Perceive_Once,_Escalate_on_Demand_Handing_Off_Visual_KV_Memory_from_Small_to_Large_VLMs|Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs]]

![[assets/2611.26902_figure.png|800]]

- **arXiv**: [2611.26902](https://arxiv.org/abs/2611.26902)
- **PDF**: https://arxiv.org/pdf/2611.26902
- **详细分析**: [[20_Research/Papers/具身智能/Perceive_Once,_Escalate_on_Demand_Handing_Off_Visual_KV_Memory_from_Small_to_Large_VLMs|Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs]]
- **作者**: Qiang Zhou, Jianing Deng, Siyan Dong, Jingxian Chen, Han-Yi Lin, Jingtong Hu
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.55（加权：具身智能 0.6，大模型 0.65，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Perceive Once, Escalate on Demand: Handing Off Visual KV Memory from Small to Large VLMs》归入 大模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenEQA, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An embodied agent cannot afford a large vision-language model (VLM) at every step of a long video, so a cascade runs a small VLM continuously and escalates only uncertain decisions to a large one. Each escalation, however, forces the large model to re-encode a history the small model has already perceived, and this dominates its cost. We present Baton, which hands the large model the small model's visual memory, its key-value (KV) cache over the history. Baton rests on one finding: the large model needs a usable memory, not a faithful copy of its own. A map trained to reproduce the large model's cache matches it most closely, yet brings no gain over the small model alone. Baton instead distills a per-layer linear map, without labels, from the large model's own answers, with the large model encoding only the current frame. Interventions on the map trace the gain to one direction, carried by the middle third of the large model's layers. On RoboMME, Baton beats the small model alone, a pruned or shortened re-watch, and a text memory; as the escalation channel of a cascade it matches re-watching to within about one point at 28-47% less compute, and 8x less per escalation at 64 frames. Its gain grows with the large model, from 8B to 32B, tracks the large model's headroom across eight model pairs from four families, and transfers zero-shot to OpenEQA.

</details>

---

### [[20_Research/Papers/大模型/ProbeAgent_Principled_Diagnosis_of_Agent_Failures_in_Verifiable_Environments|ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments]]

![[assets/2611.26897_figure.png|800]]

- **arXiv**: [2611.26897](https://arxiv.org/abs/2611.26897)
- **PDF**: https://arxiv.org/pdf/2611.26897
- **详细分析**: [[20_Research/Papers/大模型/ProbeAgent_Principled_Diagnosis_of_Agent_Failures_in_Verifiable_Environments|ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments]]
- **作者**: Yue Huang, Yuchen Ma, Shuhang Lin, Yuyang Wu, Zixuan Weng, Zixiang Xu, Xiangqi Wang, Yuexing Hao, Yujun Zhou, Yue Zhao, Olexandr Isayev, Stefan Feuerriegel...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ProbeAgent: Principled Diagnosis of Agent Failures in Verifiable Environments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Improving agents requires discovering where they fail and understanding why. An agent acts over multiple steps in a changing environment, so diagnosing its failures requires more than inspecting the final response of a large language model (LLM). The same unsuccessful outcome can arise from task difficulty or from an error the agent repeats across tasks. We introduce ProbeAgent, an automated framework that discovers agent failures, tests their proposed causes, and identifies shared failure modes. Starting from benchmark tasks, ProbeAgent builds executable tests and validates them using reference solutions, automated checks, and review of the task requirements. For each failed trajectory, it explains the error and constructs new tasks that preserve the suspected cause while changing the surrounding context. Running the agent on these tasks tests whether the same error recurs. ProbeAgent then groups failures with similar causes and generates descriptions that distinguish their errors. This process connects explanations of individual failures to executable tests and descriptions of shared failure modes. We evaluate ProbeAgent across 22 agent configurations using tasks from 10 benchmarks, collecting 1,244 failures and producing 536 failure-mode descriptions. These descriptions distinguish specific errors within broad outcomes such as incomplete work, including planning without acting and stopping before delivering a file. In human evaluation, annotators accept 90.0% of assigned descriptions and correctly reject 83.3% of similar alternatives, supporting the accuracy and specificity of the discovered failure modes.

</details>

---

### [[20_Research/Papers/大模型/Your_Judge_Inherits_Your_Prompt_In-Context_Label_Bias_in_an_LLM-as-Judge_Is_Directional,_Not_Symmetric|Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric]]

![[assets/2611.26881_figure.png|800]]

- **arXiv**: [2611.26881](https://arxiv.org/abs/2611.26881)
- **PDF**: https://arxiv.org/pdf/2611.26881
- **详细分析**: [[20_Research/Papers/大模型/Your_Judge_Inherits_Your_Prompt_In-Context_Label_Bias_in_an_LLM-as-Judge_Is_Directional,_Not_Symmetric|Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric]]
- **作者**: Abdullah Ahmad, Ahmed J. O. Ahmed, Luca Citi
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Your Judge Inherits Your Prompt: In-Context Label Bias in an LLM-as-Judge Is Directional, Not Symmetric》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MSVD-QA, NExT-QA, VideoQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-as-judge has become a standard way to score open-ended model outputs, yet the judge is itself a frozen language model steered by a few in-context examples, and such models are known to absorb the label balance of their demonstrations rather than treat them as neutral illustrations. We ask whether this label bias reaches an LLM judge used inside a multimodal (video question answering) evaluation pipeline, and what form it takes. Using a fully frozen generator-judge pipeline, we hold the generated answers fixed and vary only the Yes/No balance of the judge's few-shot examples across four demonstration sets. Each verdict is validated against a two-annotator human consensus on 200 examples per dataset. The judge's acceptance rate stays close to human consensus when its examples are balanced or skewed toward rejection, but jumps sharply (by about 30 points on NExT-QA and 20 on MSVD-QA, with a strongly one-sided error profile) when the examples are skewed toward acceptance; the opposite skew produces no matching drop. The bias is therefore one-directional within the tested range of label ratios. A separate five-draw analysis shows that results from a single example draw are unreliable, varying by up to 18 points, more than any difference between prompting conditions. We conclude that demonstration label bias in an LLM judge is a directional, inflation-only failure mode that can fabricate apparent benchmark gains but not losses, and that it is cheaply avoided by balancing the judge's examples and reporting results averaged over several draws.

</details>

---

### [[20_Research/Papers/强化学习/Coherent_Moment_Propagation_Epistemic_Uncertainty_for_Pre-trained_Robot_Policies|Coherent Moment Propagation: Epistemic Uncertainty for Pre-trained Robot Policies]]

![[assets/2611.26855_figure.png|800]]

- **arXiv**: [2611.26855](https://arxiv.org/abs/2611.26855)
- **PDF**: https://arxiv.org/pdf/2611.26855
- **详细分析**: [[20_Research/Papers/强化学习/Coherent_Moment_Propagation_Epistemic_Uncertainty_for_Pre-trained_Robot_Policies|Coherent Moment Propagation: Epistemic Uncertainty for Pre-trained Robot Policies]]
- **作者**: Miguel Saavedra-Ruiz, Anqi Li, Claudia D'Arpino, Alperen Degirmenci, Tucker Hermans, Fabio Ramos
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Coherent Moment Propagation: Epistemic Uncertainty for Pre-trained Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching policies underpin the state-of-the-art in robot learning, with impressive results ranging from long-horizon planning to dexterous manipulation. However, they provide no measure of whether their predicted commands can be trusted, particularly in novel situations outside their training set. Epistemic uncertainty reflects uncertainty about the model's weights and quantifies this ignorance, but calculating it at inference time from a flow matching policy is not trivial. Actions are produced by an ODE solver, requiring uncertainty to be propagated through the entire integration process. BayesDiff addresses this problem for diffusion models by propagating the mean and variance of the state through the denoising chain under a last-layer Laplace posterior approximation, but it severely underestimates the epistemic uncertainty. In this paper we: i) prove that, for flow matching and diffusion ODEs, BayesDiff's total variance decays at rate $O(1/T)$ as the number of Euler steps $T$ used by the solver increases; ii) introduce Coherent Moment Propagation (CoMP), two recursions inspired by the extended and unscented Kalman filters that fix this problem by carrying the cross-covariance between state and weights; and iii) widen the last-layer posterior with observation embeddings the policy already computes, improving uncertainty estimates without retraining for CoMP and several test-time estimators alike. We demonstrate these benefits on three manipulation benchmarks with applications in failure detection and demonstration selection for fine-tuning, where CoMP corrects BayesDiff's variance collapse while matching or outperforming several uncertainty estimators.

</details>

---

### [[20_Research/Papers/大模型/ChatAtom_A_Multi-Agent_LLM_System_for_Molecular_Dynamics_Simulation_and_Visualization|ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization]]

![[assets/2611.26782_figure.png|800]]

- **arXiv**: [2611.26782](https://arxiv.org/abs/2611.26782)
- **PDF**: https://arxiv.org/pdf/2611.26782
- **详细分析**: [[20_Research/Papers/大模型/ChatAtom_A_Multi-Agent_LLM_System_for_Molecular_Dynamics_Simulation_and_Visualization|ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization]]
- **作者**: Trupti Mohanty, Ming Du, Mitchell A. Wood, Brad L. Boyce, Remi Dingreville, Mathew J. Cherukara
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《ChatAtom: A Multi-Agent LLM System for Molecular Dynamics Simulation and Visualization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Molecular dynamics (MD) simulation resolves atomic-scale motion and predicts the structural, mechanical, and dynamic properties of materials, making it cen- tral to materials design and discovery. Yet an MD study requires an expert-driven workflow: designing the simulation, writing reliable input scripts, executing them, and analyzing the results with separate tools. Here we present ChatAtom, a multi-agent large language model system that translates a natural-language request into a complete MD workflow without the user writing input scripts or analysis code. Each agent has a defined responsibility within the workflow. An orchestrator plans the study; the LAMMPS and OVITO agents each use a generator-reviewer pair to prepare and review simulation and visualization scripts before execution; a high-performance computing agent dispatches jobs to remote resources; and an analysis agent interprets the completed run. The work- flow is accessible through a browser interface that streams thermodynamic data and rendered frames during local execution, allowing users to follow the simu- lation as it progresses. The architecture also supports new capabilities through loadable skills without modifying the agents, enabling autonomous hypothesis generation and testing. We evaluate ChatAtom through script-generation bench- marks, an end-to-end study of crack propagation, and a closed-loop campaign. By bringing script generation, execution, visualization, and analysis into one reviewed and observable pipeline, ChatAtom lowers the barrier to conducting MD studies and broadens access to advanced simulation workflows.

</details>

---

### [[20_Research/Papers/大模型/What_Helps_Language-Model_Agents_Review_Violent_Video_A_Controlled_Comparison_with_a_Human_Evidence_Reference|What Helps Language-Model Agents Review Violent Video? A Controlled Comparison with a Human Evidence Reference]]

![[assets/2611.26776_first_page.png|800]]

- **arXiv**: [2611.26776](https://arxiv.org/abs/2611.26776)
- **PDF**: https://arxiv.org/pdf/2611.26776
- **详细分析**: [[20_Research/Papers/大模型/What_Helps_Language-Model_Agents_Review_Violent_Video_A_Controlled_Comparison_with_a_Human_Evidence_Reference|What Helps Language-Model Agents Review Violent Video? A Controlled Comparison with a Human Evidence Reference]]
- **作者**: Mohammed El Amine Mokhtari, Matei Mancas, Virginie Vandenbulcke
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《What Helps Language-Model Agents Review Violent Video? A Controlled Comparison with a Human Evidence Reference》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AudioSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Systems that flag violent video for a human operator can now be built from language models without training, by combining perception models and letting a language model decide. We ask how the observations of the perception models should reach the decision, and which evidence matters. On the XD-Violence test set (799 clips) we fix one set of perception agents (video description, object detection, sound tagging, speech recognition and speech tagging) and one reasoning model, and compare three interfaces: messages between agents, a typed evidence graph explored with tools, and flat text read in one pass; and a single audio-visual model given the raw clip. Two annotators provide a human reference that records the decision, the incident segments and whether they relied on sight, sound or speech. Flat text matches the single model (F1 0.967 against 0.968), while the graph agent and message passing are less accurate; a variant of the graph agent developed on a separate set did not close the gap, and both graph summaries and multi-turn tool use lowered accuracy. These results hold with reworded prompts and with a larger reasoning model, except that the larger model weakens message passing enough for the graph agent to beat it. Sound events improve F1 by +0.012 [+0.004, +0.021], in line with the annotators, who used sound or speech on most violent clips. Citations of stored observations are faithful, changing about half of the decisions when removed, but no more so with the graph than with flat text, and the agent pipeline costs about 3 times the GPU time of the single model. We also report two artefacts of vision-language describers that mislead pipelines built on them.

</details>

---

### [[20_Research/Papers/具身智能/MomentMem_Memorizing_Key_Moments_for_Robot_Manipulation|MomentMem: Memorizing Key Moments for Robot Manipulation]]

![[assets/2611.26745_figure.png|800]]

- **arXiv**: [2611.26745](https://arxiv.org/abs/2611.26745)
- **PDF**: https://arxiv.org/pdf/2611.26745
- **详细分析**: [[20_Research/Papers/具身智能/MomentMem_Memorizing_Key_Moments_for_Robot_Manipulation|MomentMem: Memorizing Key Moments for Robot Manipulation]]
- **作者**: Guangyu Zhao, Yongchang Zhang, Ruizhang Jiang, Zhihong Yu, Yuhao Zhang, Tao Wu, Qimin Zhou, Kunsong Shi, Haoran Wen, Zeyu Zhang, Yin Li, Kun Zhan...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《MomentMem: Memorizing Key Moments for Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EventVLA, MemoryBench, OpenVLA, RMBench, Real-World, VMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation often requires remembering visual information that is no longer observable, such as the original location of an object. Existing approaches typically rely on full observation histories, which become redundant over long horizons, or text summaries, which may omit precise visual details. We study visual moment memory, the ability to retain such details from key moments for subsequent manipulation. To support this study, we introduce VMBench, a suite of long-horizon manipulation tasks requiring memory of spatial locations, visual appearances, and their associations. We further propose MomentMem, a hierarchical architecture in which a VLM-based memorizer selects keyframes and an executor predicts actions conditioned on the selected memories. This separation enables us to evaluate memory selection alongside closed-loop task success and to study memorizer generalization independently of the executor. On VMBench, MomentMem achieves 49.9% average success, outperforming the strongest evaluated baseline by 31.7 percentage points. Moreover, we find that the memorizer transfers well to unseen appearances zero-shot. It can also adapt to an unseen task with only a few memory annotations, reaching 43.7% success, close to the 44.3% obtained with full memory supervision. Further experiments show competitive performance on RMBench and improvements in real-robot manipulation. These results highlight the value of retaining sparse visual evidence for memory-dependent manipulation. Our code is available at https://github.com/PKU-VaLuE-Lab/MomentMem.

</details>

---

### [[20_Research/Papers/强化学习/Grid_Cells_as_Spectral_Successor_Features_A_Reusable_Basis_for_Continual_Reinforcement_Learning|Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning]]

![[assets/2611.26504_figure.png|800]]

- **arXiv**: [2611.26504](https://arxiv.org/abs/2611.26504)
- **PDF**: https://arxiv.org/pdf/2611.26504
- **详细分析**: [[20_Research/Papers/强化学习/Grid_Cells_as_Spectral_Successor_Features_A_Reusable_Basis_for_Continual_Reinforcement_Learning|Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning]]
- **作者**: Élodie Côté-Gauthier, Doina Precup, Isabeau Prémont-Schwarz
- **cs 子类**: cs.AI, cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Grid Cells as Spectral Successor Features: A Reusable Basis for Continual Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continual reinforcement learning requires agents to adapt when the task changes while reusing what they know about the environment. Successor features separate dynamics from task-specific reward, but their effectiveness depends on the choice of base features. Taking the identification of entorhinal grid cells with eigenvectors of the successor representation as a design principle, we build this basis from eigenvectors of the transition matrix of a fixed reference policy. With such a basis, the successor features at a state-action pair are a linear combination of the base features at that same pair, which is not true in general, and the coefficients are known in closed form: each successor feature is its base feature multiplied by $θ_i = 1/(1-γλ_i)$, where $λ_i$ is its eigenvalue. The long-term return is thus predicted from the same features as the immediate reward, no successor-feature network or replay buffer is needed, and adapting to a new task reduces to a linear regression on the reward. The agent acts greedily on the action values of the reference policy, which is one step of policy improvement over it and suffices to reach a single goal. In a two-goal gridworld, with the uniform random walk as reference policy, whose eigenvectors are the low-frequency Laplacian eigenvectors, agents built this way maintain near-maximal return across every change of goal, whereas SimpleSF and DQN lose most of their return at each change.

</details>

---
