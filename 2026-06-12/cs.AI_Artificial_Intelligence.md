# cs.AI | Artificial Intelligence | 2026-06-12

#arxiv #ComputerScience

**论文数**: 40

### [[20_Research/Papers/具身智能/Mana_Dexterous_Manipulation_of_Articulated_Tools|Mana: Dexterous Manipulation of Articulated Tools]]

![[assets/2606.13677_figure.png|800]]

- **arXiv**: [2606.13677](https://arxiv.org/abs/2606.13677)
- **PDF**: https://arxiv.org/pdf/2606.13677
- **详细分析**: [[20_Research/Papers/具身智能/Mana_Dexterous_Manipulation_of_Articulated_Tools|Mana: Dexterous Manipulation of Articulated Tools]]
- **作者**: Zhao-Heng Yin, Guanya Shi, Pieter Abbeel, C. Karen Liu
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.32（加权：具身智能 2.1，强化学习 0.36，世界模型 0.16，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Mana: Dexterous Manipulation of Articulated Tools》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Articulated tool manipulation remains a major challenge in dexterous robotics due to the need to coordinate internal degrees of freedom and contact-rich interactions. While prior work has largely focused on rigid objects, articulated tool use remains underexplored because of its physical complexity and the difficulty of learning functional grasping and manipulation policies. We present Mana (Manipulation Animator), a general sim-to-real framework that reinterprets dexterous manipulation as an animation problem. Inspired by computer animation, Mana employs a coarse-to-fine pipeline that transforms procedurally-generated grasp keyframes into manipulation trajectories through motion planning and reinforcement learning. The data generation process is largely automatic, requiring only a few mouse clicks to specify functional affordances (&lt;1 minute per tool). Across four articulated tools spanning different scales and joint types, Mana achieves zero-shot sim-to-real transfer for both grasping and in-hand manipulation, demonstrating a scalable approach to dexterous articulated tool use.

</details>

---

### [[20_Research/Papers/大模型/Agents-K1_Towards_Agent-native_Knowledge_Orchestration|Agents-K1: Towards Agent-native Knowledge Orchestration]]

![[assets/2606.13669_figure.png|800]]

- **arXiv**: [2606.13669](https://arxiv.org/abs/2606.13669)
- **PDF**: https://arxiv.org/pdf/2606.13669
- **详细分析**: [[20_Research/Papers/大模型/Agents-K1_Towards_Agent-native_Knowledge_Orchestration|Agents-K1: Towards Agent-native Knowledge Orchestration]]
- **作者**: Zongsheng Cao, Bihao Zhan, Jinxin Shi, Jiong Wang, Fangchen Yu, Zhijie Zhong, Zijie Guo, Tianshuo Peng, Zhuo Liu, Yi Xie, Xiang Zhuang, Yue Fan...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Agents-K1: Towards Agent-native Knowledge Orchestration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current LLM-based research agents have advanced through agent orchestration, yet largely overlook scientific knowledge orchestration. Existing works often reduce papers to abstracts, surface mentions, and flat \texttt{cites} edges, omitting key entities, claims, evidence, mechanisms, and method lineages essential for scientific reasoning. To this end, we introduce \textbf{Agents-K1}, an end-to-end knowledge orchestration pipeline that converts raw documents into agent-native scientific knowledge graphs. Agents-K1 integrates three components under a unifying theoretical foundation: a multimodal parser whose five-module schema captures entities, multimodal evidence, citations, and typed inter-entity relations across the full paper rather than abstracts alone; a 4B information-extraction backbone trained with GRPO under a rule-based reward; and a graphanything CLI, a tri-source agent interface that unifies web search, multimodal graph retrieval, and cross-document traversal. On top of this, we process 2.46 million scientific papers across six subjects to produce \textbf{Scholar-KG}, of which we release a one-million-paper subset, and the full Scholar-KG is accessible via the SCP link below. The same pipeline can be extended to general-domain corpora and to schema-conformant data synthesis. Extensive experiments demonstrate that Agents-K1 achieves superior performance in scientific information extraction, knowledge graph construction, and multi-hop scientific reasoning.

</details>

---

### [[20_Research/Papers/大模型/EurekAgent_Agent_Environment_Engineering_is_All_You_Need_For_Autonomous_Scientific_Discovery|EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery]]

![[assets/2606.13662_figure.png|800]]

- **arXiv**: [2606.13662](https://arxiv.org/abs/2606.13662)
- **PDF**: https://arxiv.org/pdf/2606.13662
- **详细分析**: [[20_Research/Papers/大模型/EurekAgent_Agent_Environment_Engineering_is_All_You_Need_For_Autonomous_Scientific_Discovery|EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery]]
- **作者**: Amy Xin, Jiening Siow, Junjie Wang, Zijun Yao, Fanjin Zhang, Jian Song, Lei Hou, Juanzi Li
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EurekAgent: Agent Environment Engineering is All You Need For Autonomous Scientific Discovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MLE-Bench, ResearchClawBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents have shown increasing potential in automating scientific discovery. Given an optimizable metric and an execution environment, they can propose, validate, and iterate scientific solutions, and have produced results that outperform human-designed approaches. As model capabilities continue to improve, we argue that the bottleneck for autonomous scientific discovery is shifting from prescribing agent workflows to designing agent environments: the resources, constraints, and interfaces that shape agent behavior. We frame this as environment engineering: building environments that amplify productive behaviors, such as open-ended exploration, systematic artifact management, and inter-agent collaboration, while suppressing harmful behaviors, such as reward hacking and high-friction human oversight. We present EurekAgent, an environment-engineered agent system for metric-driven autonomous scientific discovery. EurekAgent engineers the environment along four dimensions: permissions engineering for bounded agent execution and isolated evaluation; artifact engineering for filesystem and Git-based collaboration; budget engineering for budget-aware exploration; and human-in-the-loop engineering for easy human supervision and intervention. EurekAgent sets new state-of-the-art results on multiple mathematics, kernel engineering, and machine learning tasks, including new state-of-the-art 26-circle packing results discovered with less than $11 in total API cost. We open-source our code and results, and call for environment engineering as a core research direction for developing reliable autonomous research agents.

</details>

---

### [[20_Research/Papers/强化学习/Beyond_Runtime_Enforcement_Shield_Synthesis_as_Defensibility_Analysis_for_Adversarial_Networks|Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks]]

![[assets/2606.13621_figure.png|800]]

- **arXiv**: [2606.13621](https://arxiv.org/abs/2606.13621)
- **PDF**: https://arxiv.org/pdf/2606.13621
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Runtime_Enforcement_Shield_Synthesis_as_Defensibility_Analysis_for_Adversarial_Networks|Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks]]
- **作者**: Achraf Hsain, Sultan Almuhammadi
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Beyond Runtime Enforcement: Shield Synthesis as Defensibility Analysis for Adversarial Networks》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MARL, ShRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Shielded reinforcement learning is typically presented as a runtime safety mechanism that compiles temporal-logic specifications into automata restricting an agent's actions. We argue this is the wrong product. The same automata-theoretic machinery -- specification compilation, product game construction, attractor computation, and winning-region extraction -- is better read as a design-time analytical instrument whose outputs are structural insights about a system rather than runtime constraints on a deployed agent. We instantiate this through a constrained two-player safety game for network defense. The two specifications are enforced asymmetrically: the defender specification defines the unsafe region of the game, whereas the attacker specification restricts the adversary's legal actions during attractor computation. Solving the game yields a defensibility verdict -- a formal certificate that a topology-specification pair is or is not defensible -- with the associated winning region and shield. Beyond the binary verdict, we derive topology-level metrics from the attractor structure and combine them with post-convergence behavior from shield-constrained adversarial multi-agent reinforcement learning. Together these form a defensibility fingerprint capturing both a network's formal safety properties and its operational behavior under adaptive play. A what-if analysis shows that formal defensibility and operational effectiveness capture distinct aspects of security: small architectural changes can produce large shifts in operational outcomes while leaving formal safety margins nearly unchanged. Shield synthesis is thus most valuable not as a deployment mechanism for safe agents, but as a framework for answering architectural questions about whether, where, and how a system can be defended. The defensibility verdict is the output, not the safe policy.

</details>

---

### [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_from_Delayed_Marketplace_Feedback_for_Objective-Weight_Adaptation_in_Three-Sided_Dispatch|Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch]]

![[assets/2606.13604_figure.png|800]]

- **arXiv**: [2606.13604](https://arxiv.org/abs/2606.13604)
- **PDF**: https://arxiv.org/pdf/2606.13604
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Agent_Reinforcement_Learning_from_Delayed_Marketplace_Feedback_for_Objective-Weight_Adaptation_in_Three-Sided_Dispatch|Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch]]
- **作者**: Haochen Wu, Yi Hou, Shiguang Xie
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.3，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Multi-Agent Reinforcement Learning from Delayed Marketplace Feedback for Objective-Weight Adaptation in Three-Sided Dispatch》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OWA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dispatch in three-sided marketplaces provides a natural setting for reinforcement learning from world feedback: decisions are evaluated by delayed operational outcomes such as delivery speed, courier utilization, and merchant congestion. We present a deployed reinforcement learning system at DoorDash that adapts dispatch objective weights in a large-scale food-delivery marketplace using delayed signals. Rather than replacing the combinatorial assignment optimizer, a store-level policy learned from logged marketplace data selects a discrete multiplier that shifts the dispatch optimizer's tradeoff between delivery quality and batching efficiency. This interface enables offline policy learning under noisy, delayed, and coupled feedback while preserving production feasibility constraints and operational safeguards. We train a shared value function using centralized offline data and decentralized store-level execution, with Double Q-learning targets and a conservative regularizer to reduce out-of-distribution value overestimation. In a production switchback experiment, the offline-trained policy increases batching and reduces courier-side time costs without degrading customer-facing delivery quality. Results illustrate how world feedback from a live economic and logistics system can be used to safely adapt decision policies online.

</details>

---

### [[20_Research/Papers/强化学习/Reward_Modeling_for_Multi-Agent_Orchestration|Reward Modeling for Multi-Agent Orchestration]]

![[assets/2606.13598_first_page.png|800]]

- **arXiv**: [2606.13598](https://arxiv.org/abs/2606.13598)
- **PDF**: https://arxiv.org/pdf/2606.13598
- **详细分析**: [[20_Research/Papers/强化学习/Reward_Modeling_for_Multi-Agent_Orchestration|Reward Modeling for Multi-Agent Orchestration]]
- **作者**: King Yeung Tsang, Zihao Zhao, Vishal Venkataramani, Haizhou Shi, Zixuan Ke, Semih Yavuz, Shafiq Joty, Hao Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.65，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reward Modeling for Multi-Agent Orchestration》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Agent Systems (MAS) built on Large Language Models (LLMs) require effective orchestration to coordinate specialized agents, yet training such orchestrators is hindered by limited supervision and high computational cost. We propose Orchestration Reward Modeling (OrchRM), a self-supervised framework for evaluating orchestration quality without human annotations. OrchRM leverages intermediate artifacts from multi-agent executions to construct win-lose pairs for Bradley-Terry reward model training. Unlike existing MAS test-time scaling and orchestrator training frameworks that rely on costly sub-agent rollouts, OrchRM operates directly at the orchestration level, enabling efficient and high-performing reward-guided orchestrator training and MAS test-time scaling. OrchRM improves training efficiency by up to 10x in token usage while improving MAS test-time scaling performance by up to 8% in accuracy. These gains consistently transfer across multiple domains, including mathematical reasoning, web-based question answering, and multi-hop reasoning, demonstrating orchestration-level reward modeling as a scalable direction for robust multi-agent orchestration. Code will be available at https://github.com/Wang-ML-Lab/OrchRM.

</details>

---

### [[20_Research/Papers/具身智能/LabVLA_Grounding_Vision-Language-Action_Models_in_Scientific_Laboratories|LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories]]

![[assets/2606.13578_figure.png|800]]

- **arXiv**: [2606.13578](https://arxiv.org/abs/2606.13578)
- **PDF**: https://arxiv.org/pdf/2606.13578
- **详细分析**: [[20_Research/Papers/具身智能/LabVLA_Grounding_Vision-Language-Action_Models_in_Scientific_Laboratories|LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories]]
- **作者**: Baochang Ren, Xinjie Liu, Xi Chen, Yanshuo Liu, Chenxi Li, Daqi Gao, Zeqin Su, Jintao Xing, Zirui Xue, Rui Li, Xiangyu Zhao, Shuofei Qiao...
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《LabVLA: Grounding Vision-Language-Action Models in Scientific Laboratories》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LabVLA, OpenVLA, RLBench, Robointer-VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific laboratories increasingly rely on AI systems to reason about experiments, but the physical act of doing science remains largely outside their reach. AI can help read literature, generate hypotheses, and plan protocols, yet the execution of those protocols at the bench still requires a human operator. Vision-Language-Action (VLA) models provide one possible interface between written protocols and robot execution, but existing policies are trained mostly on household and tabletop demonstrations and rarely encounter the instruments, transparent liquids, or fixed protocol workflows found in scientific laboratories. Closing this gap requires both laboratory-specific supervision and a unified learning framework that can accommodate the diverse robot embodiments used to execute experimental protocols. We therefore identify data and embodiment as central bottlenecks alongside model design. To address the data side, we build RoboGenesis, a simulation-based workflow and data engine that composes configured laboratory workflows from atomic skills, validates and filters rollouts, and exports structured demonstrations across supported robot profiles. On the policy side, we present LabVLA, trained with a two-stage recipe: FAST action token pretraining first makes the Qwen3-VL-4B-Instruct backbone action aware before any continuous control is learned, and flow matching posttraining then attaches a DiT action expert under knowledge insulation. On the LabUtopia benchmark, LabVLA achieves the highest average success rate among all evaluated baselines under both in-distribution and out-of-distribution settings.

</details>

---

### [[20_Research/Papers/大模型/ArogyaSutra_A_Multi-Agent_Framework_for_Multimodal_Medical_Reasoning_in_Indic_Languages|ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages]]

![[assets/2606.13572_figure.jpg|800]]

- **arXiv**: [2606.13572](https://arxiv.org/abs/2606.13572)
- **PDF**: https://arxiv.org/pdf/2606.13572
- **详细分析**: [[20_Research/Papers/大模型/ArogyaSutra_A_Multi-Agent_Framework_for_Multimodal_Medical_Reasoning_in_Indic_Languages|ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages]]
- **作者**: Tanmoy Kanti Halder, Akash Ghosh, Subhadip Baidya, Arijit Roy, Sriparna Saha
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.15（加权：大模型 0.95，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《ArogyaSutra: A Multi-Agent Framework for Multimodal Medical Reasoning in Indic Languages》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GMAI-MMBench, MMedAgent-RL, MedAgentBench, MedXpertQA, PMC-VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Models (MLLMs) have shown promising reasoning capabilities in general domains, yet their performance remains limited in specialized settings such as healthcare, especially in multilingual and low-resource scenarios. This gap is critical in regions like rural India, where patients often express complex medical queries in native Indic languages and rely on multimodal inputs such as medical images. Existing English-centric MLLMs struggle to support such use cases, limiting equitable access to AI-driven healthcare assistance. To address this challenge, we introduce ArogyaBodha, a large-scale multilingual multimodal medical question-answer dataset constructed from eight heterogeneous sources, covering 31 body systems, six imaging modalities, and 21 clinical domains across English and seven major Indian languages. We further propose ArogyaSutra, an actor-critic-based multi-agent framework that integrates tool grounding with dual-memory mechanisms for step-wise, reasoning-aware decision making, and uses stored actor-critic simulation trajectories for distillation. Experiments show that our dataset and framework improve multilingual medical reasoning accuracy across all Indic languages, with ablations validating the contribution of each component. The source code and dataset are available at: https://iitp-cse.github.io/ ArogyaSutra/

</details>

---

### [[20_Research/Papers/大模型/Adaptive_Turn-Taking_for_Real-time_Multi-Party_Voice_Agents|Adaptive Turn-Taking for Real-time Multi-Party Voice Agents]]

![[assets/2606.13544_figure.png|800]]

- **arXiv**: [2606.13544](https://arxiv.org/abs/2606.13544)
- **PDF**: https://arxiv.org/pdf/2606.13544
- **详细分析**: [[20_Research/Papers/大模型/Adaptive_Turn-Taking_for_Real-time_Multi-Party_Voice_Agents|Adaptive Turn-Taking for Real-time Multi-Party Voice Agents]]
- **作者**: Soumyajit Mitra, Prabhat Pandey, Abhinav Jain, Shanmukha Sahith, K V Vijay Girish
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Adaptive Turn-Taking for Real-time Multi-Party Voice Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Turn-taking in multi-party spoken conversations remains a fundamental challenge for voice-based agents, particularly under dynamic floor competition and varying user expectations. We propose ModeratorLM, a role-playing voice agent that conditions turn-taking behavior on an explicitly assigned role in multi-party settings. The system is built on a speech large language model operating in chunk-wise streaming manner. We further introduce a reasoning-augmented variant that incorporates chain-of-thought reasoning over conversational context and the assigned role. We construct RolePlayConv, a large-scale synthetic dataset of spoken multi-party conversations with diverse assistant roles. Experiments on real-world meeting data and RolePlayConv show improved turn-taking precision by over 40% and recall by more than 70%, while substantially reducing false-positive interruptions compared to non-role-conditioned baselines.

</details>

---

### [[20_Research/Papers/大模型/IterCAD_An_Iterative_Multimodal_Agent_for_Visually-Grounded_CAD_Generation_and_Editing|IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing]]

![[assets/2606.13368_figure.png|800]]

- **arXiv**: [2606.13368](https://arxiv.org/abs/2606.13368)
- **PDF**: https://arxiv.org/pdf/2606.13368
- **详细分析**: [[20_Research/Papers/大模型/IterCAD_An_Iterative_Multimodal_Agent_for_Visually-Grounded_CAD_Generation_and_Editing|IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing]]
- **作者**: Tao Hu, Jiaxin Ai, Licheng Wen, Xueheng Li, Shu Zou, Siqi Li, Nianchen Deng, Xinyu Cai, Hongbin Zhou, Pinlong Cai, Daocheng Fu, Yu Yang...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.0（加权：大模型 0.8，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《IterCAD: An Iterative Multimodal Agent for Visually-Grounded CAD Generation and Editing》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IterCAD-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-Aided Design is pivotal in modern manufacturing, yet existing automated methods predominantly rely on open-loop, one-shot generation, creating a mismatch with iterative real-world practices. In this paper, we present IterCAD, a unified multimodal agent framework for closed-loop, interactive CAD generation and editing. We formulate the task as a multi-turn interaction between a multimodal agent and an executable CAD sandbox, covering three tasks: Drawing-to-Code, Text-to-Code, and Interactive Editing. To support this, we develop a data synthesis pipeline incorporating advanced industrial manufacturing features to generate standard-compliant multi-view engineering drawings, complex code-editing tasks, and high-fidelity interaction trajectories. We optimize the agent via progressive SFT followed by geometry-aware reinforcement learning with viable-prefix masking to enhance code executability and geometric fidelity. Finally, we introduce the IterCAD-Bench evaluation suite and propose the Chamfer Distance Tolerance-Recall (CD-TR) curve alongside its AUC-TR metric, establishing a survivor-bias-free standard that unifies code validity and geometric precision. Extensive experiments demonstrate that IterCAD achieves highly competitive performance across multiple benchmarks, significantly outperforming existing approaches in both code executability and geometric precision, while exhibiting superior capabilities in closed-loop iterative refinement.

</details>

---

### [[20_Research/Papers/具身智能/Real-Time_Execution_with_Autoregressive_Policies|Real-Time Execution with Autoregressive Policies]]

![[assets/2606.13355_figure.png|800]]

- **arXiv**: [2606.13355](https://arxiv.org/abs/2606.13355)
- **PDF**: https://arxiv.org/pdf/2606.13355
- **详细分析**: [[20_Research/Papers/具身智能/Real-Time_Execution_with_Autoregressive_Policies|Real-Time Execution with Autoregressive Policies]]
- **作者**: Sangkyu Lee, Seohyeon Park, Tackgeun You, Avi Caciularu, Idan Szpektor, Hwasup Lim, Youngjae Yu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Real-Time Execution with Autoregressive Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time execution, enabled by asynchronous inference that ensures both smooth action trajectories and fast reactivity, is critical for realistic deployments of large-scale Vision-Language-Action models. However, recent work on real-time execution primarily focuses on variants of diffusion policies, even though it is more critical for autoregressive policies given their slower rollout speed in synchronous inference. In contrast, we demonstrate that autoregressive policies can achieve real-time execution by adjusting the tokenization horizon and applying constrained decoding, thereby guaranteeing strict latency bounds that enable multi-trajectory decoding to maximize performance. Across simulated and real-world environments, we find that the autoregressive policy consistently outperforms its equivalent-level flow-matching policy counterpart while achieving significantly improved task completion speeds from synchronous inference. Coupled with the inherent advantages of autoregressive policies, such as faster convergence and better generalizability in instruction-following, these results confirm that autoregressive policies can remain a competitive policy type supporting real-time execution.

</details>

---

### [[20_Research/Papers/大模型/ReSum_Synergizing_LLM_Reasoning_and_Summarization_with_Reinforcement_Learning|ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning]]

![[assets/2606.13316_figure.png|800]]

- **arXiv**: [2606.13316](https://arxiv.org/abs/2606.13316)
- **PDF**: https://arxiv.org/pdf/2606.13316
- **详细分析**: [[20_Research/Papers/大模型/ReSum_Synergizing_LLM_Reasoning_and_Summarization_with_Reinforcement_Learning|ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning]]
- **作者**: Xucong Wang, Ziyu Ma, Yong Wang, Shidong Yang, Hailang Huang, Renda Li, Pengkun Wang, Xiangxiang Chu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《ReSum: Synergizing LLM Reasoning and Summarization with Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TreeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR) is a central technique for improving long-horizon reasoning in Large Language Models (LLMs). However, existing RLVR methods often encourage unnecessarily long reasoning rollouts, which can degrade reasoning coherence and exhaust the available context budget. Existing approaches to long-context organization often depend on external mechanisms to organize rollouts, rather than enabling the model to manage its own reasoning trajectory. To address this limitation, we propose ReSum, a novel RLVR framework that enables LLMs to compress and organize their reasoning trajectories through self-summarization. Our pilot studies show that self-summarization stabilizes generation by lowering token-level entropy, and that introducing a ``summarization'' phrase can substantially mitigate errors propagated from an incorrect rollout prefix. Motivated by these findings, ReSum adopts a summarization-aware adaptive rollout mechanism that contrastively evaluates whether self-summarization benefits the ongoing reasoning process. Specifically, when the model spontaneously triggers self-summarization, ReSum masks the summarization phrase to create a contrastive branch; for non-summarization positions, it instead randomly injects the phrase to create a matched branch. We further design a summarization-aware advantage to enable finer-grained comparison between contrastive rollout trajectories. Extensive experiments show that ReSum improves performance at an average of 4\% while reducing rollout length by 18.6\%.

</details>

---

### [[20_Research/Papers/强化学习/From_Verdict_to_Process_Agentic_Reinforcement_Learning_for_Multi-Stage_Fact_Verification|From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification]]

![[assets/2606.13262_figure.png|800]]

- **arXiv**: [2606.13262](https://arxiv.org/abs/2606.13262)
- **PDF**: https://arxiv.org/pdf/2606.13262
- **详细分析**: [[20_Research/Papers/强化学习/From_Verdict_to_Process_Agentic_Reinforcement_Learning_for_Multi-Stage_Fact_Verification|From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification]]
- **作者**: Rongxin Yang, Shenghong He, Siyuan Zhu, Chao Yu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《From Verdict to Process: Agentic Reinforcement Learning for Multi-Stage Fact Verification》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent approaches combining Large Language Models (LLMs) with retrieval-augmented reasoning have shown promise for automated fact verification. To process complex claims, these verification pipelines typically execute multi-stage workflows that coordinate tightly coupled modules, including claim decomposition, evidence gathering, and verdict prediction. However, existing methods optimize individual stages in isolation or rely on fixed heuristics, which limits adaptive coordination among stages and can lead to suboptimal outcomes. In this work, we propose ProFact, an agentic reinforcement learning framework for end-to-end optimization of multi-stage fact verification trajectories. ProFact trains a unified policy to coordinate claim decomposition, evidence seeking, answer generation, and verdict prediction. To address the sparse and delayed supervision provided by final veracity labels, ProFact introduces process-aware rewards that provide stage-level learning signals throughout the verification process. Empirical evaluation shows that ProFact consistently outperforms strong baselines in both verification performance and inference efficiency. These results highlight the effectiveness of process-aware trajectory optimization for multi-stage fact verification.

</details>

---

### [[20_Research/Papers/机器人/Humor_Style_Drives_Laughter,_Topic_Shapes_Acceptability_Evaluating_Bilingual_Personal_and_Political_Robot-Delivered_AI_Jokes|Humor Style Drives Laughter, Topic Shapes Acceptability: Evaluating Bilingual Personal and Political Robot-Delivered AI Jokes]]

![[assets/2606.13256_first_page.png|800]]

- **arXiv**: [2606.13256](https://arxiv.org/abs/2606.13256)
- **PDF**: https://arxiv.org/pdf/2606.13256
- **详细分析**: [[20_Research/Papers/机器人/Humor_Style_Drives_Laughter,_Topic_Shapes_Acceptability_Evaluating_Bilingual_Personal_and_Political_Robot-Delivered_AI_Jokes|Humor Style Drives Laughter, Topic Shapes Acceptability: Evaluating Bilingual Personal and Political Robot-Delivered AI Jokes]]
- **作者**: Anna-Maria Velentza, Anne-Gwenn Bosser
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Humor Style Drives Laughter, Topic Shapes Acceptability: Evaluating Bilingual Personal and Political Robot-Delivered AI Jokes》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humor plays a central role in human social relationships, and recent advances in computational humor create new opportunities for integrating humor into human-robot interaction (HRI). While large language models (LLMs) can generate diverse forms of humor, it remains unclear how humor style, joke content, and language preference shape perceptions of robot-delivered humor in group settings. In this exploratory study, we employed a mixed factorial design in which participants evaluated AI-generated jokes delivered by a robot in a university classroom. We examined the effects of humor type (Affiliative, Self-Enhancing, Aggressive, Self-Defeating) and joke content (person-related vs. political) on perceived funniness and appropriateness, as well as preferred language. Results show that humor type significantly influences funniness, with Aggressive and Affiliative humor rated higher, while joke content primarily affects appropriateness, with person-related jokes preferred over political ones. Language preference was shaped by both joke content and participants' self-reported fluency and humor practices.

</details>

---

### [[20_Research/Papers/机器人/Proprioceptive-visual_correspondence_enables_self-other_distinction_in_humanoid_robots|Proprioceptive-visual correspondence enables self-other distinction in humanoid robots]]

![[assets/2606.13222_figure.png|800]]

- **arXiv**: [2606.13222](https://arxiv.org/abs/2606.13222)
- **PDF**: https://arxiv.org/pdf/2606.13222
- **详细分析**: [[20_Research/Papers/机器人/Proprioceptive-visual_correspondence_enables_self-other_distinction_in_humanoid_robots|Proprioceptive-visual correspondence enables self-other distinction in humanoid robots]]
- **作者**: Yurun Chen, Tianyuan Gao, Yizhong Ge, Shikun Ban, Yizhou Wang, Hongkai Xiong, Wenjun Zeng, Wentao Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 1.5，大模型 0.1，机器人 1.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Proprioceptive-visual correspondence enables self-other distinction in humanoid robots》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distinguishing self from others is a prerequisite for social intelligence, yet humanoid robots that increasingly share workspaces with humans still lack this ability. Here we show that a humanoid robot can learn self-other distinction from proprioceptive-visual correspondence, without any identity labels or kinematic models. Once established, this distinction bootstraps a predictive self-model that maps joint configurations to three-dimensional body occupancy, capturing how the robot's body changes with action. In multi-agent scenes involving humans or morphologically identical robots, the system reliably identifies itself, learns a 3D self-model, and supports downstream tasks including target reaching, collision-aware motion planning, and human-to-robot motion retargeting. Together, these results outline a route toward bodily self-representation in robots that act and coordinate alongside others in shared physical environments. Project page: https://euron-zc.github.io/humanoid-self-model/.

</details>

---

### [[20_Research/Papers/大模型/ARMOR-MAD_Adaptive_Routing_for_Heterogeneous_Multi-Agent_Debate_in_Large_Language_Model_Reasoning|ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning]]

![[assets/2606.13197_figure.png|800]]

- **arXiv**: [2606.13197](https://arxiv.org/abs/2606.13197)
- **PDF**: https://arxiv.org/pdf/2606.13197
- **详细分析**: [[20_Research/Papers/大模型/ARMOR-MAD_Adaptive_Routing_for_Heterogeneous_Multi-Agent_Debate_in_Large_Language_Model_Reasoning|ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning]]
- **作者**: Fuqiang Niu, Bowen Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《ARMOR-MAD: Adaptive Routing for Heterogeneous Multi-Agent Debate in Large Language Model Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ChatEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent debate (MAD) can improve large language model reasoning, but fixed debate pipelines often waste computation and can amplify correlated errors among similar agents. We propose ARMOR-MAD, a training-free heterogeneous MAD framework that treats debate as conditional computation. ARMOR-MAD combines three components: Pre-debate Agreement Routing (PAR) decides whether independently generated Round-0 answers require debate; Early Agreement Stopping Evaluator (EASE) stops debate after convergence; and Semantic Outlier Detection (SOD) down-weights abnormal final answers during aggregation. Across MATH Level 5, GSM8K, MMLU, and MMLU-Pro, ARMOR-MAD consistently improves over fixed-round heterogeneous debate with the same model pool, reaching 65.5\%, 96.5\%, 90.0\%, and 81.5\% accuracy, respectively. The results suggest that genuine model heterogeneity and agreement-based control are both important for making MAD more accurate and efficient.

</details>

---

### [[20_Research/Papers/大模型/Reasoning_for_Mobile_User_Experience_with_Multimodal_LLMs_Task,_Benchmark,_and_Approach|Reasoning for Mobile User Experience with Multimodal LLMs: Task, Benchmark, and Approach]]

![[assets/2606.13192_figure.png|800]]

- **arXiv**: [2606.13192](https://arxiv.org/abs/2606.13192)
- **PDF**: https://arxiv.org/pdf/2606.13192
- **详细分析**: [[20_Research/Papers/大模型/Reasoning_for_Mobile_User_Experience_with_Multimodal_LLMs_Task,_Benchmark,_and_Approach|Reasoning for Mobile User Experience with Multimodal LLMs: Task, Benchmark, and Approach]]
- **作者**: Ruichao Mao, Zhou Fang, Teng Guo, Hao Yang, Yaping Li, Shaohua Peng, Maji Huang, Xiaoyu Lin, Shuoyang Liu, Xuepeng Li, Yuyu Zhang, Hai Rao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.9（加权：大模型 0.7，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Reasoning for Mobile User Experience with Multimodal LLMs: Task, Benchmark, and Approach》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ChartQA, CoRE-Eval, UXBench, VQA, VisualWebBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

User experience (UX) centered on usability, perceived consistency, and functional clarity is fundamental to real-world user interfaces (UI). The application of multimodal large language models (MLLMs) in the field of user interfaces is evolving rapidly, such as visual element grounding, graphical user interface (GUI) agents, and design-to-code generation. However, research efforts on evaluating UX based on UI screenshots are still immature. To address this, we propose UXBench, a novel multimodal benchmark consisting of 2,000 VQA data samples designed to assess MLLMs' ability to perform UI-based reasoning. UXBench includes 8 tasks based on real-world UI screenshots that require fine-grained diagnosis of UX issues across layout relationships, visual hierarchy, and content consistency. Our extensive evaluation of mainstream MLLMs shows that they remain fundamentally limited in their capacity for UI-based reasoning. The results underscore the need for further advancements in this area. To bridge this gap, we propose UI-UX, an MLLM based on Qwen3-VL-4B-Thinking foundation model and enhanced via reinforcement learning with two key innovations: a reward routing mechanism that dynamically balances perceptual understanding and logical reasoning during inference, and an asymmetric transition reward that suppresses redundant or insufficient reasoning steps. Experiments demonstrate that UI-UX achieves state-of-the-art (SOTA) performance on UXBench, attaining an accuracy of 0.7963 -- surpassing Claude-4.5-Sonnet's 0.6550 -- while exhibiting strong generalization across diverse UI tasks and maintaining low inference latency.

</details>

---

### [[20_Research/Papers/大模型/MemRefine_LLM-Guided_Compression_for_Long-Term_Agent_Memory|MemRefine: LLM-Guided Compression for Long-Term Agent Memory]]

![[assets/2606.13177_first_page.png|800]]

- **arXiv**: [2606.13177](https://arxiv.org/abs/2606.13177)
- **PDF**: https://arxiv.org/pdf/2606.13177
- **详细分析**: [[20_Research/Papers/大模型/MemRefine_LLM-Guided_Compression_for_Long-Term_Agent_Memory|MemRefine: LLM-Guided Compression for Long-Term Agent Memory]]
- **作者**: Minjae Kim, Jinheon Baek, Soyeong Jeong, Sung Ju Hwang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MemRefine: LLM-Guided Compression for Long-Term Agent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly expected to operate over long-term interactions, where information from past dialogues must be preserved and recalled to support future tasks. However, as interactions accumulate, the memory store grows without bound and fills with redundant entries that inflate storage cost and degrade retrieval by crowding out the most useful evidence. Furthermore, this is especially limiting on resource-constrained platforms with hard memory budgets, motivating us to formulate storage-budgeted memory management, the task of keeping an already constructed memory store within a fixed budget while preserving information useful for future interactions. To this end, we then propose MemRefine, an LLM-guided framework that, since surface similarity poorly reflects factual value, uses similarity only to propose candidate pairs and defers delete, merge, and preserve decisions to an LLM judge based on factual content, iterating until the budget is met. Across multiple memory frameworks and long-term conversation benchmarks, MemRefine consistently meets target budgets while preserving downstream performance and outperforming rule-based baselines under tight budgets.

</details>

---

### [[20_Research/Papers/具身智能/Functional_Cache_Grafting_Robust_and_Rapid_Code-Policy_Synthesis_for_Embodied_Agents|Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents]]

![[assets/2606.13097_figure.png|800]]

- **arXiv**: [2606.13097](https://arxiv.org/abs/2606.13097)
- **PDF**: https://arxiv.org/pdf/2606.13097
- **详细分析**: [[20_Research/Papers/具身智能/Functional_Cache_Grafting_Robust_and_Rapid_Code-Policy_Synthesis_for_Embodied_Agents|Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents]]
- **作者**: Saehun Chun, Wonje Choi, Sera Choi, Sanghyun Ahn, Honguk Woo
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 1.2，大模型 0.4）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Functional Cache Grafting: Robust and Rapid Code-Policy Synthesis for Embodied Agents》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code-writing large language models (CodeLLMs) generate executable code policies for embodied agents by translating natural language goals and environmental constraints into structured control programs. However, policy generation in open-domain embodied environments suffers from two fundamental limitations: (i) delayed decoding caused by repetitive prefill computation over long prompts, and (ii) limited robustness due to fully generative decoding, which often produces API mismatches, missing safety guards, and unstable control logic. To address these limitations, we present FCGraft, a Functional Cache Grafting framework. FCGraft maintains a library of function-level validated code skeletons and their associated prompt-level Transformer key-value (KV) caches, and synthesizes new policies by retrieving relevant functions and grafting their KV caches when a new task is provided. Given retrieved function caches, FCGraft performs cache grafting via stitching, which composes cached function segments into a composite policy, and patching, which locally adapts only the necessary code regions to satisfy task-specific parameters and constraints with minimal additional decoding. By eliminating redundant prefill computation, this approach reduces generation latency, while reusing validated control structures improves robustness over prompt-level caching methods RAGCache, achieving 18.31% higher task success rate and 2.3x faster policy synthesis.

</details>

---

### [[20_Research/Papers/大模型/The_Emergence_of_Autonomous_Penetration_Capabilities_in_Large_Language_Model-Powered_AI_Systems|The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems]]

![[assets/2606.13079_first_page.png|800]]

- **arXiv**: [2606.13079](https://arxiv.org/abs/2606.13079)
- **PDF**: https://arxiv.org/pdf/2606.13079
- **详细分析**: [[20_Research/Papers/大模型/The_Emergence_of_Autonomous_Penetration_Capabilities_in_Large_Language_Model-Powered_AI_Systems|The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems]]
- **作者**: Jiaqi Luo, Jiarun Dai, Zhile Chen, Jia Xu, Weibing Wang, Yawen Duan, Brian Tse, Geng Hong, Xudong Pan, Yuan Zhang, Min Yang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《The Emergence of Autonomous Penetration Capabilities in Large Language Model-Powered AI Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Nowadays, the autonomous execution of cyberattacks capable of causing substantial real-world harm is widely regarded as one of the critical red lines that frontier AI systems must not cross. Within this broader red-line scenario, autonomous penetration represents a core enabling capability and subtask: the ability of LLM-powered AI systems to independently conduct adversarial operations against a target server without human intervention, identify and exploit vulnerabilities, and obtain unauthorized access or control. A growing body of work has sought to assess the autonomous penetration capabilities of AI systems. However, existing evaluations often employ opaque methodologies, rely on unrealistic or overly simplified penetration-testing scenarios, or provide LLMs with excessive prior knowledge and task-specific guidance, and cannot accurately capture the extent to which modern AI systems can autonomously perform this core capability within broader high-impact cyberattack scenarios. To address these limitations, we construct a new autonomous penetration evaluation framework consisting of two components: target servers and agent scaffolding. Specifically, on the target-server side, we design two levels of target environments based on the number of secure services without known vulnerabilities deployed alongside a vulnerable service: Tier~1 (one secure service) and Tier~2 (three secure services), resulting in a total of 300 target servers. Meanwhile, the agent scaffolding adopts a general-purpose agent architecture equipped with a set of general-purpose cybersecurity tools, without any target-specific prior knowledge. We evaluate 19 open-weight and proprietary LLMs, and find that current models achieve penetration success rates ranging from 10.7% to 69.3%. Moreover, we observe that autonomous penetration capability continues to improve alongside advances in overall model capability.

</details>

---

### [[20_Research/Papers/具身智能/EA-WM_Event-Aware_World_Models_with_Task-Specification_Grounding_for_Long-Horizon_Manipulation|EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation]]

![[assets/2606.13053_figure.png|800]]

- **arXiv**: [2606.13053](https://arxiv.org/abs/2606.13053)
- **PDF**: https://arxiv.org/pdf/2606.13053
- **详细分析**: [[20_Research/Papers/具身智能/EA-WM_Event-Aware_World_Models_with_Task-Specification_Grounding_for_Long-Horizon_Manipulation|EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation]]
- **作者**: Kailin Wang, Haoxiang Jie, Yaoyuan Yan, Jiacheng Zhou, Zhiyou Heng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《EA-WM: Event-Aware World Models with Task-Specification Grounding for Long-Horizon Manipulation》归入 世界模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, PlaNet, WorldEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained-feature world models provide a useful substrate for robot imagination, but visual or latent prediction alone does not determine whether an imagined future satisfies task-relevant events. Long-horizon manipulation requires progress signals that are relational, predicate-level, and physically grounded: whether an object has moved, whether a drawer or contact state has changed, whether a placement predicate is satisfied, and whether a candidate future is reliable enough for execution. We introduce EA-WM, an event-aware world-model framework that augments frozen visual-feature dynamics with task-specification-grounded event prediction and verification. EA-WM rolls out candidate futures in pretrained visual-feature space, decodes them into structured event states, and scores them using task-progress, semantic-consistency, physical-feasibility, and uncertainty terms. The verifier guides sampling-based planning, gates candidate actions, and, in the contact-sensitive LIBERO wine-rack setting, selects among PPOgenerated proposals. Across navigation, deformable-object, wall-constrained, and languagedescribed manipulation studies, EA-WM shows that event-aware verification can make featurespace world models more interpretable and better aligned with task progress.

</details>

---

### [[20_Research/Papers/大模型/CausalMoE_A_Billion-Scale_Multimodal_Foundation_Model_for_Granger_Causal_Discovery_with_Pattern-Routed_Heterogeneous_Experts|CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery with Pattern-Routed Heterogeneous Experts]]

![[assets/2606.13024_figure.png|800]]

- **arXiv**: [2606.13024](https://arxiv.org/abs/2606.13024)
- **PDF**: https://arxiv.org/pdf/2606.13024
- **详细分析**: [[20_Research/Papers/大模型/CausalMoE_A_Billion-Scale_Multimodal_Foundation_Model_for_Granger_Causal_Discovery_with_Pattern-Routed_Heterogeneous_Experts|CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery with Pattern-Routed Heterogeneous Experts]]
- **作者**: Bo Liu, Di Dai, Jingwei Liu, Jiarui Jin, Xiaocheng Fang, Guangkun Nie, Hongyan Li, Shenda Hong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《CausalMoE: A Billion-Scale Multimodal Foundation Model for Granger Causal Discovery with Pattern-Routed Heterogeneous Experts》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Granger Causal Discovery (GCD) is fundamental for analyzing temporal dependencies in complex systems. However, existing neural GCD methods predominantly rely on a "one-size-fits-all" paradigm, struggling to capture distribution shifts and dynamic regime changes inherent in real-world time series. This often leads to entangled representations and spurious causal graphs. In this paper, we propose CausalMoE, a billion-scale multimodal Granger causal foundation model that explicitly models patch-level heterogeneity. CausalMoE introduces a Pattern-Routed Mixture of Heterogeneous Experts, which dynamically identifies latent temporal patterns and routes patches to specialized domain experts, effectively decoupling regime-specific mechanisms from shared dynamics. To ensure interpretable graph recovery, we design a Causality-Aware Self-Attention mechanism operating across variables, yielding sparse Granger causal graphs via proximal optimization. Furthermore, CausalMoE is the first to integrate LLMs and VLMs to align numerical signals with textual and visual priors, regularizing causal estimation in complex scenarios. Extensive experiments demonstrate that CausalMoE establishes a new state-of-the-art on fully supervised benchmarks, while effectively generalizing to few-shot settings where traditional methods fail.

</details>

---

### [[20_Research/Papers/具身智能/An_Embodied_Simulation_Platform,_Benchmark,_and_Data-Efficient_Augmentation_Framework_for_Wet-Lab_Robotics|An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics]]

![[assets/2606.12936_first_page.png|800]]

- **arXiv**: [2606.12936](https://arxiv.org/abs/2606.12936)
- **PDF**: https://arxiv.org/pdf/2606.12936
- **详细分析**: [[20_Research/Papers/具身智能/An_Embodied_Simulation_Platform,_Benchmark,_and_Data-Efficient_Augmentation_Framework_for_Wet-Lab_Robotics|An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics]]
- **作者**: Zhe Liu, Huanbo Jin, Zhaohui Du, Zhe Wang, He Xu, Peijia Li, Jiaming Gu, Quan Lu, Qi Wang, Bin Ji, Ting Xiao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《An Embodied Simulation Platform, Benchmark, and Data-Efficient Augmentation Framework for Wet-Lab Robotics》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wet-lab robots can improve the reproducibility, throughput, and safety of biomedical experiments, but scaling their learning requires customizable simulators for safe and reproducible task generation, open editable laboratory assets, and efficient pipelines that turn limited demonstrations into usable training data. We present Pipette, an embodied simulation platform, benchmark, and data-efficient augmentation framework for wet-lab robot learning. Pipette releases over 43 open-source and re-editable wet-lab assets, together with an extensible asset-building pipeline. A key component of Pipette is its simulation-based data augmentation pipeline, replaying human demonstrations in simulation, applies lighting, camera, speed, and action perturbations, and filters generated episodes with automatic task success checks, rapidly expanding usable training data from limited manual demonstrations. We further introduce an 11-task wet-lab embodied benchmark covering sample handling, culture-ware manipulation, device operation, and precision placement. With only 30 demonstrations per task, ACT achieves 65.5% average success rate, while simulation augmentation improves SmolVLA from 44.1% to 74.7% and π0 from 40.4% to 46.5%, validating the effectiveness of Pipette for data-efficient VLA training and evaluation. Pipette also supports natural-language-driven scene construction and task registration, lowering the barrier for non-expert users to define new wet-lab robotic tasks.

</details>

---

### [[20_Research/Papers/具身智能/Bounding_Boxes_as_Goals_Language-Conditioned_Grasping_via_Neuro-Symbolic_Planning|Bounding Boxes as Goals: Language-Conditioned Grasping via Neuro-Symbolic Planning]]

![[assets/2606.12910_figure.png|800]]

- **arXiv**: [2606.12910](https://arxiv.org/abs/2606.12910)
- **PDF**: https://arxiv.org/pdf/2606.12910
- **详细分析**: [[20_Research/Papers/具身智能/Bounding_Boxes_as_Goals_Language-Conditioned_Grasping_via_Neuro-Symbolic_Planning|Bounding Boxes as Goals: Language-Conditioned Grasping via Neuro-Symbolic Planning]]
- **作者**: Allison Andreyev, Landon Eum, Nestor Tiglao, Romel Gomez
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Bounding Boxes as Goals: Language-Conditioned Grasping via Neuro-Symbolic Planning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For robotics to be effectively integrated into household or industrial environments, machines must adapt to natural-language prompts in real time. Although Vision-Language Models (VLMs) have enabled zero-shot generalization in robot task and motion planning (TAMP), current state-of-the-art approaches often remain computationally "heavyweight" or require extensive training on thousands of demonstrations. We present GRASP (Grounded Reasoning and Symbolic Planning), a framework designed as a step toward open-vocabulary tabletop manipulation. Our approach leverages a pretrained VLM to translate natural-language queries into neuro-symbolic goal states, grounded in the physical world via a bounding-box detection pipeline. Unlike methods that rely on fixed color lists or hard-coded coordinates, GRASP enables robots to interpret abstract spatial concepts such as "top shelf" and execute tasks without additional fine-tuning. We achieve 73.3% overall success across 90 real-robot trials at three difficulty levels, requiring no task-specific training.

</details>

---

### [[20_Research/Papers/强化学习/PolicyGuard_Towards_Test-time_and_Step-level_Adversary_Defense_for_Reinforcement_Learning_Agent|PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent]]

![[assets/2606.12896_figure.png|800]]

- **arXiv**: [2606.12896](https://arxiv.org/abs/2606.12896)
- **PDF**: https://arxiv.org/pdf/2606.12896
- **详细分析**: [[20_Research/Papers/强化学习/PolicyGuard_Towards_Test-time_and_Step-level_Adversary_Defense_for_Reinforcement_Learning_Agent|PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent]]
- **作者**: Junfeng Guo Heng Huang
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《PolicyGuard: Towards Test-time and Step-level Adversary Defense for Reinforcement Learning Agent》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While real-world applications of reinforcement learning (RL) are becoming increasingly popular, the security of RL systems deserve more attention and exploration. In particular, recent work has revealed that RL agents are vulnerable to backdoor attacks, where a victim agent behaves normally under standard conditions but executes malicious actions when a specific trigger is activated. Existing backdoor defenses for RL either require access to the agent's internal parameters, operate only at the model or trajectory level, or are limited to specific attack types. To ensure the security of RL agents, we propose \texttt{PolicyGuard}, a \textit{test-time step-level} backdoor defense which leverages Gaussian Process (GP) posterior variance and adapts pseudo trajectories to enable uncertainty computation for individual time step. Besides, we also provide theoretical foundations to explain the efficacy of GP posterior variance. Extensive experiments across seven RL games demonstrate that PolicyGuard achieves state-of-the-art detection performance in most cases, with average AUROC of 0.856 for perturbation-based attacks and 0.859 for adversary-agent attacks.

</details>

---

### [[20_Research/Papers/大模型/HarnessBridge_Learnable_Bidirectional_Controller_for_LLM_Agent_Harness|HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness]]

![[assets/2606.12882_first_page.png|800]]

- **arXiv**: [2606.12882](https://arxiv.org/abs/2606.12882)
- **PDF**: https://arxiv.org/pdf/2606.12882
- **详细分析**: [[20_Research/Papers/大模型/HarnessBridge_Learnable_Bidirectional_Controller_for_LLM_Agent_Harness|HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness]]
- **作者**: Xiaoxuan Wang, Haixin Wang, Alexander Taylor, Jason Cong, Yizhou Sun, Wei Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《HarnessBridge: Learnable Bidirectional Controller for LLM Agent Harness》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly deployed as agents for long-horizon tasks, yet their performance is shaped not only by model capability and environment design, but also by the harness that mediates agent--environment interaction. Existing harnesses are largely manually engineered, making them difficult to scale as trajectories grow longer and interactions become more complex. In this work, we ask whether harness can be generated by a learnable plug-in module that can be trained in an end-to-end fashion. We introduce HarnessBridge, a lightweight learnable harness controller that parameterizes the agent--environment interface as a bidirectional projection. HarnessBridge learns two bidirectional projections: observation projection, which distills raw trajectories into compact, decision-relevant states, and action projection, which converts proposed actions into executable transitions or trajectory-grounded rejections. We train HarnessBridge on a harness supervision dataset via unified instruction tuning. On Terminal-Bench~2.0 and SWE-bench Verified, HarnessBridge matches or surpasses strong specialized harnesses while substantially reducing token usage and trajectory length, and generalizes from smaller generators to larger commercial models.

</details>

---

### [[20_Research/Papers/具身智能/WISE_A_Long-Horizon_Agent_in_Minecraft_with_Why-Which_Reasoning|WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning]]

![[assets/2606.12852_figure.png|800]]

- **arXiv**: [2606.12852](https://arxiv.org/abs/2606.12852)
- **PDF**: https://arxiv.org/pdf/2606.12852
- **详细分析**: [[20_Research/Papers/具身智能/WISE_A_Long-Horizon_Agent_in_Minecraft_with_Why-Which_Reasoning|WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning]]
- **作者**: Renmin Cheng, Changhao Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，大模型 0.5）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《WISE: A Long-Horizon Agent in Minecraft with Why-Which Reasoning》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rapid advances have been made in developing general-purpose embodied agent in environments like Minecraft through the adoption of LLM-augmented hierarchical approaches. Despite their promise, low-level controllers often become performance bottlenecks due to repeated execution failures. We argue that a key limitation is not only the lack of episodic memory, but also the decoupling of \textit{what-where-when} memory from \textit{which-why} reasoning. To address this, we propose \textbf{WISE} (Which-Why Informed Semantic Explorer), a long-horizon agent framework with an enhanced low-level controller equipped with a Causal Event Graph that augments episodic memory with explicit causal structure linking observations to task relevance. Unlike prior work such as MrSteve, which relies on feature similarity for retrieval, WISE enables robust recall under viewpoint changes and supports opportunistic task reordering through causal reasoning. Building on this memory, we propose an Opportunistic Task Scheduler that dynamically re-prioritizes subtasks when causally relevant opportunities are detected. We further equip WISE with a multi-scale progressive exploration strategy to provide spatially comprehensive observations for downstream reasoning. Experiments show that WISE largely improves task success and efficiency on long-horizon sparse tasks, particularly in settings requiring adaptive decision-making.

</details>

---

### [[20_Research/Papers/大模型/Fantastic_Scientific_Agents_and_How_to_Build_Them_AgentBuild_for_Rietveld_Refinement|Fantastic Scientific Agents and How to Build Them: AgentBuild for Rietveld Refinement]]

![[assets/2606.12834_figure.png|800]]

- **arXiv**: [2606.12834](https://arxiv.org/abs/2606.12834)
- **PDF**: https://arxiv.org/pdf/2606.12834
- **详细分析**: [[20_Research/Papers/大模型/Fantastic_Scientific_Agents_and_How_to_Build_Them_AgentBuild_for_Rietveld_Refinement|Fantastic Scientific Agents and How to Build Them: AgentBuild for Rietveld Refinement]]
- **作者**: Woong Shin, Craig A. Bridges, Marshall T. McDonnell, Rafael Ferreira da Silva
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.6，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Fantastic Scientific Agents and How to Build Them: AgentBuild for Rietveld Refinement》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As scientific workflows shift from deterministic executables to LLM-based agents, the development practices on offer, such as fine-tuning, reinforcement learning, and prompt-and-go, bury the scientist's judgment. We propose treating agent construction as a workflow stage and introduce AgentBuild, which builds a scientific agent from a contract the scientist authors. The contract is a version-controlled rubric, a difficulty-graded curriculum, and a curated external knowledge base. A rubric-driven judge gates a meta-optimizer coding agent that edits the agent within a declared boundary, so the build compiles the agent, not the scientist's judgment. We instantiate this for Rietveld refinement of X-ray diffraction data through GSAS-II behind MCP and A2A, where a blank-harness construction run progresses through a lithium lanthanum zirconium oxide (LLZO) signal-to-noise ladder, reaches the 4 hour scan as a frontier case, and exposes the workflow-scope limits that remain. The same rubric that rewards credible fits also scores trajectory scope, making the frontier a contract failure rather than a pattern-fitting failure. As base models evolve, re-running AgentBuild is a re-tune, not a rebuild, and the scientist's authored contract remains the durable asset.

</details>

---

### [[20_Research/Papers/强化学习/Stubborn_A_Streamlined_and_Unified_Reinforcement_Learning_Framework_for_Robust_Motion_Tracking_and_Fall_Recovery_for_Humanoids|Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids]]

![[assets/2606.12814_figure.png|800]]

- **arXiv**: [2606.12814](https://arxiv.org/abs/2606.12814)
- **PDF**: https://arxiv.org/pdf/2606.12814
- **详细分析**: [[20_Research/Papers/强化学习/Stubborn_A_Streamlined_and_Unified_Reinforcement_Learning_Framework_for_Robust_Motion_Tracking_and_Fall_Recovery_for_Humanoids|Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids]]
- **作者**: Xiao Ren, Yuhui Yang, Zongbiao Weng, Zhijie Liu, He Kong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 1，机器人 0.5）
- **关联关键词**: RL

#### 研究背景与动机

《Stubborn: A Streamlined and Unified Reinforcement Learning Framework for Robust Motion Tracking and Fall Recovery for Humanoids》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent reinforcement learning approaches have shown great promise in improving humanoid motion tracking performance and achieving fall recovery under disturbances. However, most existing works treat motion tracking and fall recovery as different tasks and require multi-stage training with specialized recovery rewards and/or separate recovery policies. Moreover, existing reinforcement learning-based methods often terminate training episodes immediately after severe tracking failures, limiting recovery-oriented exploration in unstable or fallen states. To address the above issues, we propose Stubborn, a streamlined and unified reinforcement learning framework to achieve robust humanoid motion tracking and fall recovery. Specifically, Stubborn uses an asymmetric Actor-Critic architecture and consists of three major components. First, a yaw-aligned tracking representation is adopted to reduce sensitivity to global drift and heading disturbances while preserving gravity-related balance information. Second, we introduce a Bernoulli-based probabilistic termination mechanism that enables the policy to encourage exploration of fall-recovery behaviors under varying failure modes. Third, we propose a probabilistic termination and tracking-error-driven strategy that dynamically reshapes the sampling distribution based on tracking performance, increasing the training efficiency for difficult motion segments and unstable states. Extensive comparisons with SOTA methods and ablation studies show that Stubborn achieved competitive performance, and the proposed probabilistic termination mechanism and adaptive sampling strategy contributed to the performance and robustness gains. For real-world demonstrations, please refer to https://aislab-sustech.github.io/Stubborn/.

</details>

---

### [[20_Research/Papers/世界模型/A_Tutorial_on_World_Models_and_Physical_AI|A Tutorial on World Models and Physical AI]]

![[assets/2606.12783_figure.jpg|800]]

- **arXiv**: [2606.12783](https://arxiv.org/abs/2606.12783)
- **PDF**: https://arxiv.org/pdf/2606.12783
- **详细分析**: [[20_Research/Papers/世界模型/A_Tutorial_on_World_Models_and_Physical_AI|A Tutorial on World Models and Physical AI]]
- **作者**: Il-Seok Oh
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.0（加权：世界模型 0.8，机器人 0.2）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《A Tutorial on World Models and Physical AI》归入 世界模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World modeling is emerging as a central principle for building intelligent systems capable of prediction, reasoning, and decision making. A central distinction can be drawn between explicit world models, which learn structured dynamics for rollout-based reasoning and planning, and implicit world models, which encode predictive structure within scalable learned representations. These complementary paradigms provide a foundation for physical AI in domains such as robotics and autonomous driving, enabling intelligence beyond reactive control under real-world constraints. Recent foundation models further suggest a pathway toward unified systems integrating perception, prediction, and action. Despite rapid progress, major challenges remain in hierarchical reasoning, long-horizon planning, and autonomous goal formation, which are critical for advancing toward artificial general intelligence. This tutorial presents a coherent framework in which diverse world modeling approaches are unified through shared predictive structure and differentiated by how such structure is represented and exploited.

</details>

---

### [[20_Research/Papers/大模型/SMSR_Certified_Defence_Against_Runtime_Memory_Poisoning_in_Persistent_LLM_Agent_Systems|SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems]]

![[assets/2606.12703_figure.png|800]]

- **arXiv**: [2606.12703](https://arxiv.org/abs/2606.12703)
- **PDF**: https://arxiv.org/pdf/2606.12703
- **详细分析**: [[20_Research/Papers/大模型/SMSR_Certified_Defence_Against_Runtime_Memory_Poisoning_in_Persistent_LLM_Agent_Systems|SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems]]
- **作者**: Tarun Sharma
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《SMSR: Certified Defence Against Runtime Memory Poisoning in Persistent LLM Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) agents increasingly run with persistent memory that accumulates across user sessions. This creates a new attack surface: an adversary interacting only through normal channels can inject crafted memories that, once retrieved, steer the agent's responses for future users, without touching model weights or code. We call this Multi-Session Memory Poisoning (MSMP) and show that no existing defence certifies against it; static-corpus defences (RobustRAG, ReliabilityRAG) assume a fixed knowledge base, and heuristic filters are bypassed by fluent enterprise-style text. We present Signed Memory with Smoothed Retrieval (SMSR), the first defence with a certified robustness bound for this setting. Component 1 adds HMAC-SHA256 provenance at write time, blocking unsigned injection. Component 2 applies randomised memory ablation with verdict-based majority voting at query time, bounding the influence of authenticated adversaries. We prove that no provenance-free retrieval-time filter can certify against adaptive injection, derive a hypergeometric certificate for Component 2, and formalise the Consistent Minority Effect, whereby a consistent adversarial answer wins string-based voting as a numerical minority while verdict-based voting removes it. Across 15 enterprise scenarios (3,150 repeated trials), Component 1 cuts attack success from 93-100% to 0% for all unsigned variants. For an authenticated adversary with a single injection, Component 2 holds success to 8.0% (95% CI [5.8, 10.9], n=450), below the certified worst case. In an end-to-end query-only attack where the agent itself writes the poison rather than it being pre-seeded, SMSR reduces success from 65.3% to 5.3% (n=150, non-overlapping CIs) on a live agent stack. Clean-query utility is 90% (Component 1) and 85% (combined).

</details>

---

### [[20_Research/Papers/具身智能/EWAM_An_Enhanced_World_Action_Model_for_Closed-Loop_Online_Adaptation_in_Embodied_Intelligence|EWAM: An Enhanced World Action Model for Closed-Loop Online Adaptation in Embodied Intelligence]]

![[assets/2606.12690_figure.png|800]]

- **arXiv**: [2606.12690](https://arxiv.org/abs/2606.12690)
- **PDF**: https://arxiv.org/pdf/2606.12690
- **详细分析**: [[20_Research/Papers/具身智能/EWAM_An_Enhanced_World_Action_Model_for_Closed-Loop_Online_Adaptation_in_Embodied_Intelligence|EWAM: An Enhanced World Action Model for Closed-Loop Online Adaptation in Embodied Intelligence]]
- **作者**: Xin Zhou, Cong Miao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 1.2，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL, ComputerVision

#### 研究背景与动机

《EWAM: An Enhanced World Action Model for Closed-Loop Online Adaptation in Embodied Intelligence》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GigaWorld, OpenVLA, Policy-DROID。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose the Enhanced World Action Model (EWAM), a closed-loop online adaptation architecture built upon a pretrained and fully frozen Cosmos3 backbone network. Evaluated entirely under a zero-shot task protocol, EWAM is centrally focused on reducing the amount of additional deployment data required to adapt to new task layouts. Notably, no extra task-specific demonstration sets were introduced in any of the evaluations, and no fine-tuning was performed on the backbone network. Its performance gains stem entirely from an inference-time co-reasoning mechanism composed of four inserted lightweight neural layers: the Neural Experience Memory Layer located in the intermediate layers of the Diffusion Transformer (DiT) provides task-relevant execution context; the Neural Anomaly Detection Layer after the state prediction head monitors the divergence between predicted and actual states in real time; the Neural Policy Routing Layer dynamically selects direct execution, conservative replanning, or rollback recovery based on the anomaly severity; and the Neural Action Correction Layer refines the generated action chunks using execution diagnostics. Unlike naive feature fusion, the memory, anomaly detection, and correction modules are deeply integrated into the Cosmos3 forward path in a differentiable manner, with only the final routing decision being a discrete supervised one.

</details>

---

### [[20_Research/Papers/具身智能/M_A_Modular,_Extensible,_Serving_System_for_Multimodal_Models|M*: A Modular, Extensible, Serving System for Multimodal Models]]

![[assets/2606.12688_figure.png|800]]

- **arXiv**: [2606.12688](https://arxiv.org/abs/2606.12688)
- **PDF**: https://arxiv.org/pdf/2606.12688
- **详细分析**: [[20_Research/Papers/具身智能/M_A_Modular,_Extensible,_Serving_System_for_Multimodal_Models|M*: A Modular, Extensible, Serving System for Multimodal Models]]
- **作者**: Atindra Jha, Naomi Sagan, Keisuke Kamahori, Irmak Sivgin, Rohan Sanda, Steven Gao, Mark Horowitz, Luke Zettlemoyer, Olivia Hsu, Jure Leskovec, Baris Kasikci, Stephanie Wang
- **cs 子类**: cs.AI, cs.DC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 1.42（加权：具身智能 0.3，大模型 0.4，强化学习 0.16，世界模型 0.36，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《M*: A Modular, Extensible, Serving System for Multimodal Models》归入 大模型、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We are entering a new era of composite model architectures that integrate diverse components such as vision encoders, language backbones, diffusion and flow heads, audio codecs, action generators, and world-model predictors. Such architectures underpin a broad class of multimodal models, including unified multimodal models, omni models, speech-language models, vision-language-action policies, and world models. However, existing model serving frameworks were built on narrow assumptions about model structure, making them ill-suited to accommodate this new architectural diversity. Here we present M*, a universal serving system for efficient serving of composite AI models. M* represents models as dataflow graphs, processing requests spanning diverse modalities and tasks as traversals over these graphs. The core insight is a modular abstraction that supports arbitrary composition of model components, flexible placement onto a physical cluster, and model-agnostic optimizations within a distributed runtime. We call this abstraction the Walk Graph and show how it can concisely capture composite models from a broad range of families. We instantiate M* on representative models and find that it achieves, on average, 20% lower end-to-end latency than vLLM-Omni for text-to-image workloads on BAGEL, while delivering up to 2.9x lower real-time factor and 2.7x higher throughput for text-to-speech workloads on Qwen3-Omni. M* also outperforms the V-JEPA 2-AC rollout baseline for robotic planning by up to 12.5x. Thus, our work paves the road towards more efficient serving of complex models with minimal developer effort.

</details>

---

### [[20_Research/Papers/大模型/TrajGenAgent_A_Hierarchical_LLM_Agent_for_Human_Mobility_Trajectory_Generation|TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation]]

![[assets/2606.12657_figure.png|800]]

- **arXiv**: [2606.12657](https://arxiv.org/abs/2606.12657)
- **PDF**: https://arxiv.org/pdf/2606.12657
- **详细分析**: [[20_Research/Papers/大模型/TrajGenAgent_A_Hierarchical_LLM_Agent_for_Human_Mobility_Trajectory_Generation|TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation]]
- **作者**: Siyu Li, Toan Tran, Lingyi Zhao, Khurram Shafique, Li Xiong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《TrajGenAgent: A Hierarchical LLM Agent for Human Mobility Trajectory Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human mobility data is important for transportation, urban planning, and epidemic control, but large-scale trajectory collection is often costly and privacy-constrained, motivating realistic synthetic trajectory generation. Existing LLM-based generators typically rely on either prompt engineering, which preserves zero-shot reasoning but lacks fine-grained spatiotemporal grounding, or trajectory-level fine-tuning, which improves statistical precision but incurs substantial computational cost and may weaken general reasoning. We propose TrajGenAgent, a semantic-aware hierarchical LLM-agent framework for human mobility trajectory generation without model fine-tuning. TrajGenAgent uses a two-stage orchestrator-worker design: an LLM first synthesizes an individual- and weekday-conditioned activity chain from historical evidence via in-context learning, and a deterministic workflow then grounds each activity into a complete visit using personalized POI retrieval, distance-aware location selection, kinematics-aware travel-time propagation, and LLM-based duration estimation. To evaluate realism beyond aggregate spatiotemporal statistics, we introduce an anomaly-detection-based evaluation framework using two complementary detectors to assess behavioral and semantic plausibility. Experiments on benchmark and large-scale simulation datasets show that TrajGenAgent improves spatiotemporal fidelity, semantic coherence, and individual-specific behavioral realism over representative neural and LLM-based baselines, while avoiding parameter updates.

</details>

---

### [[20_Research/Papers/大模型/Keep_Policy_Gradient_in_Charge_Sibling-Guided_Credit_Distillation_for_Long-Horizon_Tool-Use_Agents|Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents]]

![[assets/2606.12634_figure.png|800]]

- **arXiv**: [2606.12634](https://arxiv.org/abs/2606.12634)
- **PDF**: https://arxiv.org/pdf/2606.12634
- **详细分析**: [[20_Research/Papers/大模型/Keep_Policy_Gradient_in_Charge_Sibling-Guided_Credit_Distillation_for_Long-Horizon_Tool-Use_Agents|Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents]]
- **作者**: Tianyu Ding, Jianhong Xin, Juan Pablo De la Cruz Weinstein
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.67（加权：大模型 0.55，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Keep Policy Gradient in Charge: Sibling-Guided Credit Distillation for Long-Horizon Tool-Use Agents》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AppWorld, SD-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon tool-use reinforcement learning can learn from outcome verification, but its trajectory-level advantage is broadcast across many reasoning, API, and answer tokens. Self-distillation promises a denser signal by reusing a policy's own rollouts or a privileged teacher. We show, however, that direct token-level self-distillation can silently destroy tool use: it rehearses teacher behavior without knowing which actions the verifier rewards, so useful skills and harmful shortcuts are amplified together. We introduce Sibling-Guided Credit Distillation (SGCD), which uses distillation for credit assignment rather than as a competing actor loss. Dynamic sampling produces mixed successful and failed sibling rollouts; an external LLM summarizes their contrast into a training-only stepwise credit reference; dense teacher/student divergence drives credit reassignment; and bounded detached credit weights reshape GRPO token advantages. The deployed student sees no external LLM, sibling evidence, or oracle. Across AppWorld and $τ^3$-airline, SGCD improves over matched GRPO comparators: AppWorld TGC $42.9 \to 45.6$ on test_normal and $24.7 \to 27.0$ on test_challenge, and $τ^3$-airline pass@1 $0.583 \to 0.602$.

</details>

---

### [[20_Research/Papers/具身智能/PersonaDrive_Human-Style_Retrieval-Augmented_VLA_Agents_for_Closed-Loop_Driving_Simulation|PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation]]

![[assets/2606.12616_figure.png|800]]

- **arXiv**: [2606.12616](https://arxiv.org/abs/2606.12616)
- **PDF**: https://arxiv.org/pdf/2606.12616
- **详细分析**: [[20_Research/Papers/具身智能/PersonaDrive_Human-Style_Retrieval-Augmented_VLA_Agents_for_Closed-Loop_Driving_Simulation|PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation]]
- **作者**: Mahmoud Srewa, Praneetsai Iddamsetty, Mohammad Abdullah Al Faruque, Salma Elmalaki
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 2.55（加权：具身智能 1.5，大模型 1.05）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PersonaDrive: Human-Style Retrieval-Augmented VLA Agents for Closed-Loop Driving Simulation》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Closed-loop driving simulators typically populate their environments with non-ego traffic agents that behave largely the same way, produced either by rule-based traffic managers or by learned models trained toward a single behavioral mode. Recent work introduces style variation through post-hoc labels on observational data or LLM-inferred reward weights, but these signals act as proxies for what a style should reward rather than demonstrations of humans explicitly asked to drive in that style. We introduce PersonaDrive, a pipeline that conditions a vision-language-action (VLA) driving agent on retrieved demonstrations from a style-instructed human driving dataset, in which participants drive CARLA leaderboard routes under aggressive, neutral, and conservative instructions on a driver-in-the-loop rig. The pipeline has three stages: (i) offline triplet mining over per-style human driving data using a combined image-text similarity score; (ii) training a lightweight retrieval head that fuses frozen visual features with a small control encoder over per-style databases; and (iii) fine-tuning a single VLA backbone to treat retrieved context points as in-context behavioral demonstrations during waypoint prediction. At inference, the same backbone is conditioned on any style by swapping which per-style database the retrieval head queries, so selecting a style requires no per-style retraining while enabling human-style, style-diverse non-ego agents for closed-loop simulation. On Bench2Drive, PersonaDrive (no style) improves the driving score by 4.6% over SimLingo and 2.5% over HiP-AD, and under style conditioning attains the highest driving score in every style within a roughly 2% band (its weakest style surpassing the strongest baseline, DMW, by 5.4%), while average speed and acceleration rise by 18% and 25% from the conservative to the aggressive instruction.

</details>

---

### [[20_Research/Papers/具身智能/From_Imitation_to_Alignment_Human-Preference_Flow_Policies_for_Long-Horizon_Sidewalk_Navigation|From Imitation to Alignment: Human-Preference Flow Policies for Long-Horizon Sidewalk Navigation]]

![[assets/2606.12603_figure.png|800]]

- **arXiv**: [2606.12603](https://arxiv.org/abs/2606.12603)
- **PDF**: https://arxiv.org/pdf/2606.12603
- **详细分析**: [[20_Research/Papers/具身智能/From_Imitation_to_Alignment_Human-Preference_Flow_Policies_for_Long-Horizon_Sidewalk_Navigation|From Imitation to Alignment: Human-Preference Flow Policies for Long-Horizon Sidewalk Navigation]]
- **作者**: Honglin He, Zhizheng Liu, Yukai Ma, Bolei Zhou
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《From Imitation to Alignment: Human-Preference Flow Policies for Long-Horizon Sidewalk Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous long-horizon sidewalk navigation is essential for micro-mobility applications such as robotic food delivery and assistive electronic wheelchairs. Unlike autonomous driving on the road, long-horizon sidewalk navigation requires precise maneuvering through unpredictable sidewalk terrains and pedestrians, with a lightweight perception stack as minimal as a single monocular RGB camera. While imitation learning (IL) from demonstrations offers a practical solution, the resulting autopilot policy often suffers from compounding errors, a lack of social compliance on sidewalks, and deficiencies in counterfactual reasoning to handle complex situations. To address these challenges, we introduce FlowPilot, a mapless navigation policy that achieves robust and efficient long-horizon navigation performance using only a monocular RGB camera. We first propose to use anchored flow matching as an action representation for policy pre-training on large-scale robot fleet data and to capture the diverse, complex, multimodal distribution of sidewalk navigation behaviors. To bridge the gap between imitation and alignment, we further design a human-in-the-loop preference learning scheme to tune the policy on a small amount of human intervention data. It strengthens the model's counterfactual reasoning and social compliance on sidewalks. We evaluate FlowPilot through extensive simulation and real-world experiments in diverse sidewalk environments. FlowPilot achieves 42% success rate and 66% route completion in simulation, while FlowPilot-HP further improves real-world robustness and social compliance, reducing IR by 40.0% and NIR by 52.1% relative to the base model.

</details>

---

### [[20_Research/Papers/具身智能/Foresight_Iterative_Reasoning_About_Clues_that_Matter_for_Navigation|Foresight: Iterative Reasoning About Clues that Matter for Navigation]]

![[assets/2606.12550_figure.png|800]]

- **arXiv**: [2606.12550](https://arxiv.org/abs/2606.12550)
- **PDF**: https://arxiv.org/pdf/2606.12550
- **详细分析**: [[20_Research/Papers/具身智能/Foresight_Iterative_Reasoning_About_Clues_that_Matter_for_Navigation|Foresight: Iterative Reasoning About Clues that Matter for Navigation]]
- **作者**: Arthur Zhang, Carl Qi, Donne Su, Xiangyun Meng, Amy Zhang, Joydeep Biswas
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，强化学习 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Foresight: Iterative Reasoning About Clues that Matter for Navigation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-world mapless navigation from sparse language instructions requires resolving underspecified goals and inferring which environmental cues are relevant for reaching the goal. For instance, reaching an out-of-view destination may require interpreting ramps, signs, or detours that reveal where to go or which route to take. Prior works are limited by their reliance on known navigation factors and closed-set factor categories, or identify cues before motion planning and miss plan-dependent cues. We argue that pretrained Vision-Language Models (VLMs) can discover novel instruction-relevant cues, but require adaptation to focus on which cues matter and how they should influence motion planning. We realize these ideas in Foresight, a test-time framework in which a finetuned VLM alternates between proposing image-space motion plans and critiquing them using the language goal and visual context. Subsequent plans are conditioned on prior critiques, enabling iterative motion refinement before execution. To align plan critiques and refinements with open-set behavior preferences, we learn a reward model from human feedback and use it to post-train the VLM with reinforcement learning in the plan-critique loop. In offline evaluations and 6 real-world environments, Foresight improves average task success by 37% and reduces interventions per mission by 52% relative to state-of-the-art test-time reasoning and foundation-model baselines, while running in real-time on a Jetson AGX Orin. We will release code, data, and training details to support future work on test-time reasoning for robot motion refinement. Additional videos at: https://amrl.cs.utexas.edu/foresight

</details>

---

### [[20_Research/Papers/大模型/ReCal_Reward_Calibration_for_RL-based_LLM_Routing|ReCal: Reward Calibration for RL-based LLM Routing]]

![[assets/2606.12479_figure.png|800]]

- **arXiv**: [2606.12479](https://arxiv.org/abs/2606.12479)
- **PDF**: https://arxiv.org/pdf/2606.12479
- **详细分析**: [[20_Research/Papers/大模型/ReCal_Reward_Calibration_for_RL-based_LLM_Routing|ReCal: Reward Calibration for RL-based LLM Routing]]
- **作者**: Qihang Yu, Hanwen Tong, Zhengqi Zhang, Bo Zheng, Feng Wei, Shengyu Zhang, Zemin Liu, Fei Wu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.6，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《ReCal: Reward Calibration for RL-based LLM Routing》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) routing has emerged as an effective paradigm for leveraging the complementary strengths of multiple LLMs through dynamic model and reasoning-strategy selection. Recent reinforcement learning (RL)-based routing methods further improve routing quality by optimizing routing policies from interaction feedback. However, they still struggle to provide informative and comparable learning signals under heterogeneous tasks with varying difficulty. In practice, multiple objectives (e.g., correctness, format behavior) are aggregated into a single scalar reward, leading to ambiguous credit assignment and conflicting optimization signals. Moreover, reward signals exhibit significant variability across instances, where some instances produce higher or more variable rewards, introducing optimization bias that favors trivial samples over informative ones. To address these issues, we propose \textbf{ReCal}, a \textbf{\underline{Re}}ward \textbf{\underline{Cal}}ibration framework for RL-based LLM routing. We first introduce a hierarchical reward decomposition mechanism with component-wise advantage estimation. We further propose a distribution-aware optimization strategy that calibrates optimization variability through variance-aware reweighting and per-dataset normalization. Experiments on seven datasets demonstrate that ReCal consistently improves routing performance, and training stability over baselines. Code is available at https://anonymous.4open.science/r/ReCal.

</details>

---

### [[20_Research/Papers/大模型/SAIGuard_Communication-State_Simulation_for_Proactive_Defense_of_LLM_Multi-Agent_Systems|SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems]]

![[assets/2606.12474_figure.png|800]]

- **arXiv**: [2606.12474](https://arxiv.org/abs/2606.12474)
- **PDF**: https://arxiv.org/pdf/2606.12474
- **详细分析**: [[20_Research/Papers/大模型/SAIGuard_Communication-State_Simulation_for_Proactive_Defense_of_LLM_Multi-Agent_Systems|SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems]]
- **作者**: Ruxue Shi, Yili Wang, Mengnan Du, Qinggang Zhang, Rui Miao, Yixin Liu, Xin Wang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《SAIGuard: Communication-State Simulation for Proactive Defense of LLM Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based multi-agent systems (MAS) solve complex tasks through inter-agent collaboration, but their communication-driven nature also allows security risks to spread across agents and trigger system-wide failures. Existing MAS defenses mainly follow a reactive paradigm after execution by detecting and isolating harmful agents, which may cause irreversible damage and degrade collaborative utility. To address this, we propose a proactive defense framework for MAS security, namely a Simulation-aware Interception Guard (SAIGuard). SAIGuard performs communication-state simulation over the MAS interaction graph, estimates the impact of incoming messages on local agent states and the global MAS state, and detects risky messages via reconstruction deviations from benign communication patterns. Instead of isolating agents, SAIGuard sanitizes or regenerates suspicious messages before it propagation into system. Experiments across diverse topologies and attack scenarios show that SAIGuard reduces attack success rates while maintaining MAS utility, outperforming reactive defenses.

</details>

---
