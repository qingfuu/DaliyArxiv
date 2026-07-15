# cs.AI | Artificial Intelligence | 2026-07-13

#arxiv #ComputerScience

**论文数**: 47

### [[20_Research/Papers/大模型/VEXAIoT_Autonomous_IoT_Vulnerability_EXploitation_using_AI_Agents|VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents]]

![[assets/2607.09653_figure.png|800]]

- **arXiv**: [2607.09653](https://arxiv.org/abs/2607.09653)
- **PDF**: https://arxiv.org/pdf/2607.09653
- **详细分析**: [[20_Research/Papers/大模型/VEXAIoT_Autonomous_IoT_Vulnerability_EXploitation_using_AI_Agents|VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents]]
- **作者**: Katherine Swinea, Kshitiz Aryal, Lopamudra Praharaj, Maanak Gupta
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《VEXAIoT: Autonomous IoT Vulnerability EXploitation using AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Internet of Things (IoT) systems are inherently vulnerable due to constrained hardware, outdated firmware, and insecure default configurations, creating a need for scalable and adaptive security testing approaches. While recent adoptions of Large Language Model (LLM) agents have demonstrated promise in penetration testing and Capture-the-Flag (CTF) environments, their application to IoT specific vulnerabilities remains unexplored. This paper presents an autonomous multi-agent framework, referred to as Vulnerability EXploitation using AI Agents (VEXAIoT), for vulnerability discovery and exploitation in IoT environments using LLM-based reasoning and offensive security tools. The framework combines a vulnerability detection agent and an attack execution agent to perform reconnaissance, plan attack sequences, and execute exploits against vulnerable IoT services. The system is evaluated in IoTGoat and Metasploitable environments across ten attack scenarios mapped to OWASP IoT vulnerabilities. Experimental results show attack success rate of up to 100% with low token overhead and average execution times under two minutes for most attacks. Across 260 attack executions, VEXAIoT achieves a 95.0% overall success rate, including 94.5% success in IoTGoat and 96.7% success in Metasploitable2. These results demonstrate the potential for LLM-driven agents to automate IoT vulnerability assessment and offensive security workflows in controlled environments

</details>

---

### [[20_Research/Papers/强化学习/Semantic_Pareto-DQN_A_Multi-Objective_Reinforcement_Learning_Framework_for_Financial_Anomaly_Detection|Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for Financial Anomaly Detection]]

![[assets/2607.09641_first_page.png|800]]

- **arXiv**: [2607.09641](https://arxiv.org/abs/2607.09641)
- **PDF**: https://arxiv.org/pdf/2607.09641
- **详细分析**: [[20_Research/Papers/强化学习/Semantic_Pareto-DQN_A_Multi-Objective_Reinforcement_Learning_Framework_for_Financial_Anomaly_Detection|Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for Financial Anomaly Detection]]
- **作者**: Cláudio Lúcio do Val Lopes, Lucca Machado da Silva
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Semantic Pareto-DQN: A Multi-Objective Reinforcement Learning Framework for Financial Anomaly Detection》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Financial anomaly detection suffers from extreme class imbalance, causing traditional single-objective algorithms to exhibit ``fraud collapse'', defaulting to the majority class and failing to balance anomaly interdiction with customer friction. To overcome this without distortive data resampling, we propose the Semantic Pareto-DQN, a multi-objective reinforcement learning framework. Our approach synthesizes heterogeneous transaction features into cohesive natural-language narratives, encoded by large language models, thereby producing a robust, scale-invariant state representation. The agent optimizes a vectorial reward that explicitly decouples financial efficacy, operational friction, and semantic discovery. By mapping the continuous Pareto frontier, the system dynamically navigates the asymmetric costs of missed anomalies versus false positives. Empirical evaluations across E-Commerce fraud and UCI Credit datasets show that semantic Pareto-DQN successfully shatters the zero-recall trap. It achieves superior minority-class recall compared to scalarized baselines, providing an alternative to trade bounded operational friction for financial anomaly discovery.

</details>

---

### [[20_Research/Papers/大模型/Task-Specific_Multimodal_Question_Answering_Agents_via_Confidence_Calibration_and_Incremental_Reasoning_for_QANTA_2026|Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026]]

![[assets/2607.09623_figure.png|800]]

- **arXiv**: [2607.09623](https://arxiv.org/abs/2607.09623)
- **PDF**: https://arxiv.org/pdf/2607.09623
- **详细分析**: [[20_Research/Papers/大模型/Task-Specific_Multimodal_Question_Answering_Agents_via_Confidence_Calibration_and_Incremental_Reasoning_for_QANTA_2026|Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026]]
- **作者**: Nirjhar Das, Md. Al-Mamun Provath
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Task-Specific Multimodal Question Answering Agents via Confidence Calibration and Incremental Reasoning for QANTA 2026》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EMM-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present our submission to the QANTA 2026 shared challenge at the ICML 2026 Workshop on Efficient Multimodal Question Answering (EMM-QA). Quanta evaluates multimodal quizbowl systems that answer pyramid-style questions from incrementally revealed text and accompanying images while operating under realistic efficiency constraints. The challenge consists of two distinct tasks: Tossup questions, which require deciding when to answer under uncertainty, and Bonus questions, which emphasize accurate answer selection and human adoption. To address these differing objectives, we develop a task-specific two-agent architecture. Our Tossup agent utilizes a GPT-4o-mini-class model (referred to as GPT-4.1-mini in the competition logs) with confidence-calibrated answering and a domain-specific numeric reasoning policy that reduces overconfident predictions from isolated quantitative clues. Our Bonus agent uses GPT-4o-class model (referred to as GPT-4.1) with leadin-aware reasoning, structured relational reasoning, and multimodal evidence integration to improve exact answer selection. Rather than relying on a retrieval pipeline or model ensembles, our approach emphasizes efficient reasoning policies and confidence calibration within a hosted-only environment. Our system achieved the highest overall leaderboard score of 0.402, including a Tossup score of 0.238 and a Bonus Effect score of 0.164. The results demonstrate that lightweight, task-specific reasoning strategies can provide strong performance on resource-constrained multimodal question answering benchmarks.

</details>

---

### [[20_Research/Papers/大模型/Agora_Enhancing_LLM_Agent_Reasoning_Via_Auction-Based_Task_Allocation|Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation]]

![[assets/2607.09600_figure.png|800]]

- **arXiv**: [2607.09600](https://arxiv.org/abs/2607.09600)
- **PDF**: https://arxiv.org/pdf/2607.09600
- **详细分析**: [[20_Research/Papers/大模型/Agora_Enhancing_LLM_Agent_Reasoning_Via_Auction-Based_Task_Allocation|Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation]]
- **作者**: Kaiji Zhou, Ales Leonardis, Yue Feng
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agora: Enhancing LLM Agent Reasoning Via Auction-Based Task Allocation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enhancing the reasoning capabilities of large language model (LLM) agents requires effective orchestration of diverse expert models and tools. However, existing frameworks typically call APIs based on coarse-grained matching between tasks and the functions of expert models or tools, while overlooking critical factors such as performance variability and cost efficiency among functionally similar alternatives. To address this, we propose Agora, a framework that introduces an incentive-compatible auction mechanism for dynamically allocating tasks to expert models and tools. By treating reasoning steps as tradeable items, Agora enables agents to bid based on their rectified competence-ensuring that critical logic is routed to the most capable solver rather than the most overconfident one. Evaluations across five benchmarks show that Agora improves over matched single-model, routing, and cascade baselines under comparable candidate pools, while exposing a controllable cost-quality trade-off through a single auction parameter.

</details>

---

### [[20_Research/Papers/具身智能/PAC-ACT_Post-training_Actor-Critic_for_Action_Chunking_Transformers|PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers]]

![[assets/2607.09590_figure.png|800]]

- **arXiv**: [2607.09590](https://arxiv.org/abs/2607.09590)
- **PDF**: https://arxiv.org/pdf/2607.09590
- **详细分析**: [[20_Research/Papers/具身智能/PAC-ACT_Post-training_Actor-Critic_for_Action_Chunking_Transformers|PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers]]
- **作者**: Yujie Pang, Zudong Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PAC-ACT: Post-training Actor-Critic for Action Chunking Transformers》归入 强化学习、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precision industrial contact manipulation requires reliable robot policies under pose perturbations and contact-force constraints. Vision-language-action models offer broad generalization but often introduce high inference latency and GPU-memory cost, while vision-action chunking policies are more suitable for real-time industrial control. However, these policies are usually trained by behavior cloning and suffer from distribution shift in contact-rich tasks. This paper proposes PAC-ACT, a reinforcement-learning post-training framework for pretrained Action Chunking Transformer policies. PAC-ACT reformulates policy optimization at the chunk level, constructs an ACT-transferred actor-critic architecture, and introduces a hybrid behavior-prior constraint to preserve the pretrained action distribution during online fine-tuning. Experiments on industrial precision-contact benchmarks show that PAC-ACT improves task success, contact stability, and force safety while retaining low latency and low GPU-memory usage. On the Contour task, PAC-ACT significantly reduces peak contact force and decreases the proportion of force readings above 60 N by 46 times. Sparse-reward ablations further show that the proposed behavior-prior constraint enables effective exploration under randomized initial poses.

</details>

---

### [[20_Research/Papers/其他/TrustX_Agent_Risk_Classification_Framework_(ARC)_Risk-Tiering_Internally_Created_Agentic_AI_Systems|TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems]]

![[assets/2607.09586_first_page.png|800]]

- **arXiv**: [2607.09586](https://arxiv.org/abs/2607.09586)
- **PDF**: https://arxiv.org/pdf/2607.09586
- **详细分析**: [[20_Research/Papers/其他/TrustX_Agent_Risk_Classification_Framework_(ARC)_Risk-Tiering_Internally_Created_Agentic_AI_Systems|TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems]]
- **作者**: Hannah M. Liu, Rhea Saxena, Shiv Asthana
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《TrustX Agent Risk Classification Framework (ARC): Risk-Tiering Internally Created Agentic AI Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The proliferation of agentic AI systems across enterprise and public-sector contexts has outpaced the capacity of general-purpose AI risk frameworks to classify and govern them. In this paper, we introduce the TrustX Agent Risk Classification Framework, a structured, repeatable instrument that can be applied to seven types of agentic AI systems and is grounded in foundational pre-existing AI governance frameworks. At the core of the framework is a twelve-dimension scoring rubric that robustly quantifies the risk. This rubric is combined with other components, such as the GPA + IAT classification model and the five-level autonomy framework derived from existing literature. These inputs produce a three-tier governance output with mapped control recommendations. A specialised Coding Assistant extension is also included to account for nuances specific to this type of agentic AI system. We then use an illustrative example to show our framework in practice. ARC is intended for AI governance practitioners, risk officers, developers, and regulators, and it will regularly undergo iteration as we continue to expand it and make it more robust. The community can access the interactive framework here: https://arc.responsible.ai/

</details>

---

### [[20_Research/Papers/大模型/ALICE_Learning_a_General-Purpose_Pathology_Foundation_Model_from_Vision,_Vision-Language,_and_Slide-Level_Experts|ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts]]

![[assets/2607.09526_figure.png|800]]

- **arXiv**: [2607.09526](https://arxiv.org/abs/2607.09526)
- **PDF**: https://arxiv.org/pdf/2607.09526
- **详细分析**: [[20_Research/Papers/大模型/ALICE_Learning_a_General-Purpose_Pathology_Foundation_Model_from_Vision,_Vision-Language,_and_Slide-Level_Experts|ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts]]
- **作者**: Jiawen Li, Tian Guan, Huijuan Shi, Xitong Ling, Mingxi Fu, Anjia Han, Chao He, Yonghong He
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ProtoNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models are reshaping computational pathology, yet their capabilities remain shaped by pretraining objectives, data sources, and spatial scales, fragmenting complementary expertise across separate backbones. Here we present ALICE, a unified foundation model trained through multi-stage agglomerative distillation that sequentially distills eight vision-only, vision-language, and slide-level teacher models into dedicated modules of a single backbone. ALICE is pretrained on 24,985,184 tile-level pathology images and 155,604 high-resolution images, and evaluated across 21 task scenarios, 96 downstream tasks, and 48 data sources, spanning region-of-interest tissue analysis, vision-language multimodal evaluation, and whole-slide clinical assessment. In all three evaluation settings, ALICE achieved the best average rank among task-matched pathology foundation models. These results demonstrate that agglomerative distillation can consolidate complementary capabilities from specialized models into a unified backbone for broad computational pathology applications. The model is available at https://github.com/WonderLandxD/ALICE.

</details>

---

### [[20_Research/Papers/大模型/SAGEAgent_A_Self-Evolving_Agent_for_Cost-Aware_Modality_Acquisition_in_Multimodal_Survival_Prediction|SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction]]

![[assets/2607.09521_figure.png|800]]

- **arXiv**: [2607.09521](https://arxiv.org/abs/2607.09521)
- **PDF**: https://arxiv.org/pdf/2607.09521
- **详细分析**: [[20_Research/Papers/大模型/SAGEAgent_A_Self-Evolving_Agent_for_Cost-Aware_Modality_Acquisition_in_Multimodal_Survival_Prediction|SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction]]
- **作者**: Chongyu Qu, Can Cui, Zhengyi Lu, Junchao Zhu, Tianyuan Yao, Junlin Guo, Juming Xiong, Yanfan Zhu, Yuechen Yang, Bennett A. Landman, Yuankai Huo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《SAGEAgent: A Self-Evolving Agent for Cost-Aware Modality Acquisition in Multimodal Survival Prediction》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Does every cancer patient truly need a complete diagnostic workup for accurate survival prediction? In multimodal clinical oncology, diagnostic modalities follow a clinically mandated order of escalating burden -- from demographics collected at intake to genomic profiling requiring specialized tissue analysis. Current multimodal survival methods either assume all modalities are available or passively handle missing data, but none actively reason about whether acquiring the next modality is justified for a given patient along this ordered workflow. We formulate this as a sequential decision problem and propose SAGEAgent (Sequential Acquisition Guided by Experience), a self-evolving LLM-based clinical agent that decides which diagnostic modalities to acquire for each patient, balancing predictive accuracy against clinical invasiveness. SAGEAgent reasons about each patient's evolving diagnostic state through clinical tools that translate numerical predictions into text, an episodic memory that retrieves similar past cases, and a semantic memory that accumulates reusable decision patterns from experience. Experiments on a glioma cohort combining TCGA-LGG, TCGA-GBM, and BraTS with four diagnostic modalities demonstrate that SAGEAgent achieves competitive survival prediction accuracy while reducing average acquisition burden by 55%.

</details>

---

### [[20_Research/Papers/具身智能/Seeing_is_Free,_Speaking_is_Not_Uncovering_the_True_Energy_Bottleneck_in_Edge_VLM_Inference|Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference]]

![[assets/2607.09520_figure.png|800]]

- **arXiv**: [2607.09520](https://arxiv.org/abs/2607.09520)
- **PDF**: https://arxiv.org/pdf/2607.09520
- **详细分析**: [[20_Research/Papers/具身智能/Seeing_is_Free,_Speaking_is_Not_Uncovering_the_True_Energy_Bottleneck_in_Edge_VLM_Inference|Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference]]
- **作者**: Junfei Zhan, Haoxun Shen, Mingang Guo, Zixuan Huang, Tengjiao He
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.4）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Seeing is Free, Speaking is Not: Uncovering the True Energy Bottleneck in Edge VLM Inference》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language Models (VLMs) are the perceptual backbone of embodied AI, but their energy footprint on edge hardware remains poorly understood. Existing efficiency efforts focus predominantly on reducing visual tokens, implicitly treating visual processing as the dominant energy cost. We overturn this implicit assumption through the first systematic energy profiling of on-device VLM inference, spanning five models across three architecture families, four input resolutions, and two hardware platforms (NVIDIA RTX 3070 and Jetson Orin NX). Our analysis yields three findings. First, average inference power is a model-intrinsic constant, invariant to input resolution, image complexity, and prompt type, with less than 5% variation across all conditions. This means that all energy variation across inputs must arise from variation in inference time, not from variation in power draw. Second, each output token costs 11 to 39x more wall-clock time than each input token due to the compute-bound and memory-bound asymmetry between prefill and decode, making output token count the dominant driver of both latency and energy. Third, image complexity, measured by the number of objects in an image, induces up to 4.1x energy differences at identical resolution. This variation arises not from increased visual processing cost, but from differences in output length. These findings expose a fundamental limitation of visual token pruning: even removing all visual tokens saves at most 10% of total energy for fixed-token models. Across models spanning 1 billion to 8 billion parameters, controlling output length saves up to 97% of total energy, with the energy dominance of decoding growing stronger at larger model scale. In short, the true energy bottleneck in edge VLM inference is not what the model sees, but how much it says.

</details>

---

### [[20_Research/Papers/大模型/Failure_as_a_Process_An_Anatomy_of_CLI_Coding_Agent_Trajectories|Failure as a Process: An Anatomy of CLI Coding Agent Trajectories]]

![[assets/2607.09510_figure.png|800]]

- **arXiv**: [2607.09510](https://arxiv.org/abs/2607.09510)
- **PDF**: https://arxiv.org/pdf/2607.09510
- **详细分析**: [[20_Research/Papers/大模型/Failure_as_a_Process_An_Anatomy_of_CLI_Coding_Agent_Trajectories|Failure as a Process: An Anatomy of CLI Coding Agent Trajectories]]
- **作者**: Xiangxin Zhao, Han Li, Shuaiting Li, Tianyi Zhao, Earl T. Barr, Federica Sarro, He Ye
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Failure as a Process: An Anatomy of CLI Coding Agent Trajectories》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) coding agents are increasingly deployed to autonomously perform software engineering tasks in terminal-based environments, making their reliability a growing concern. Existing empirical studies investigate why coding agents fail, yet they largely treat failure as a final outcome rather than a temporal process, providing limited insight into how failures emerge, evolve, and become unrecoverable. We present the first large-scale empirical study of CLI coding-agent failure trajectories, introducing a process-oriented framework that analyzes failure through its onset, evolution, and recovery across execution trajectories. We first collect 3,843 execution trajectories generated by seven frontier models across three coding-agent scaffolds (OpenHands, MiniSWE, and Terminus2) on Terminal-Bench, then carefully filter them to obtain 1,794 complete and valid trajectories for manual annotation (over 63,000 execution steps), from which we derive 14 findings spanning failure occurrence, root causes, recovery, and cross-system consistency. Our findings show that coding-agent failures are predominantly driven by epistemic errors, typically begin within the first few execution steps, and often remain hidden until recovery is no longer possible, suggesting that improving coding-agent reliability requires earlier validation and intervention rather than relying solely on final-outcome evaluation.

</details>

---

### [[20_Research/Papers/大模型/What_VGGT_Knows_About_Overlap_Probing_Geometric_Foundation_Models_for_Co-Visibility|What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility]]

![[assets/2607.09503_figure.png|800]]

- **arXiv**: [2607.09503](https://arxiv.org/abs/2607.09503)
- **PDF**: https://arxiv.org/pdf/2607.09503
- **详细分析**: [[20_Research/Papers/大模型/What_VGGT_Knows_About_Overlap_Probing_Geometric_Foundation_Models_for_Co-Visibility|What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility]]
- **作者**: Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，机器人 0.4）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《What VGGT Knows About Overlap: Probing Geometric Foundation Models for Co-Visibility》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A fundamental challenge in 3D reconstruction and robotic localization is co-visibility: determining which image pairs share overlapping visible surfaces, particularly in scenarios with minimal overlap. We demonstrate that VGGT implicitly encodes co-visibility as an emergent behavior: without any supervision for this task, its internal representations exhibit a clear hierarchical structure mirroring that of large language models, i.e. early layers build a 3D-aware scene representation, while late layers act as dedicated co-visibility reasoners. In particular, we identify layer L17 as a negative anchor that consistently routes non-co-visible pairs for this backbone, regardless of the evaluation setting, providing task-grounded evidence of layer specialization in a geometry-grounded foundation model. Building on this, we introduce Co-VGGT, which freezes VGGT and trains only a lightweight layer-wise mixture-of-experts head (less than 7.5M parameters) to classify co-visibility from RGB alone, treating each layer as a specialized expert whose geometric abstraction is adaptively weighted per input pair. On the Co-VisiON benchmark, Co-VGGT surpasses the human annotation baseline and improves over prior work by more than 25% pairwise and 10% multiview. Pairwise predictions are well-calibrated (ECE=0.030), enabling direct use as edge weights in visibility graphs for downstream SfM and SLAM pipelines without post-hoc correction. Code and data are available.

</details>

---

### [[20_Research/Papers/大模型/Shared_Selective_Persistent_Memory_for_Agentic_LLM_Systems|Shared Selective Persistent Memory for Agentic LLM Systems]]

![[assets/2607.09493_first_page.png|800]]

- **arXiv**: [2607.09493](https://arxiv.org/abs/2607.09493)
- **PDF**: https://arxiv.org/pdf/2607.09493
- **详细分析**: [[20_Research/Papers/大模型/Shared_Selective_Persistent_Memory_for_Agentic_LLM_Systems|Shared Selective Persistent Memory for Agentic LLM Systems]]
- **作者**: Sanjana Pedada, Aditya Dhavala, Neelraj Patil
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Shared Selective Persistent Memory for Agentic LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic LLM systems that generate code through multi-turn tool use face a fundamental context problem: each session starts from zero, discarding the configuration choices, domain constraints, data schemas, and tool-use patterns that made previous sessions productive. Naively persisting entire conversation histories is token-inefficient and counterproductive: irrelevant context degrades generation quality. We introduce shared selective persistent memory, an architecture that identifies and retains four categories of reusable context (task specifications, data schemas, tool configurations, and output constraints) while discarding session-specific reasoning traces. Crucially, this memory is shared: workspaces encapsulating selective memory can be transferred across users with role-based access control, enabling collaborative reuse without redundant specification. We implement it in a deployed collaborative workspace platform where LLM agents produce, edit, and maintain git-versioned artifacts (dashboards, reports, and data-driven documents) from heterogeneous sources (CSV, SQL, REST APIs, and MCP servers). A complementary zero-token data refresh mechanism decouples generated programs from runtime data, enabling artifact reuse without re-invocation. Across three enterprise scenarios, shared selective persistent memory achieves 96% task completion (vs. 79% without memory and 71% with full history). Zero-token refresh eliminates LLM re-invocation for recurring updates (14x task-time reduction), while summary-driven generation cuts per-invocation token cost by 97x versus raw data injection. A replication on four public datasets confirms generalizability, with zero-token refresh succeeding in 12/12 trials. Notably, naive full-history persistence actively degrades completion by biasing the agent with stale traces, while selective memory outperforms both extremes.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Reward_Hacking_in_Reinforcement_Learning|Multimodal Reward Hacking in Reinforcement Learning]]

![[assets/2607.09492_figure.png|800]]

- **arXiv**: [2607.09492](https://arxiv.org/abs/2607.09492)
- **PDF**: https://arxiv.org/pdf/2607.09492
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Reward_Hacking_in_Reinforcement_Learning|Multimodal Reward Hacking in Reinforcement Learning]]
- **作者**: Jiayu Yao, Yiwei Wang, Anmeng Zhang, Zhe Sun, Songsong Wang, Lingrui Mei, Yuyao Ge, Shenghua Liu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Multimodal Reward Hacking in Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MM-SafetyBench, VLSBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) is increasingly used to align multimodal large language models (MLLMs), but higher rewards do not always imply better task performance. This risk is amplified when visual evidence is evaluated by text-only or weakly grounded rewards. We study reward hacking in MLLM RL across safety VQA, chart VQA, and stress-test settings, varying reward design, data ambiguity, model scale (2B-32B), and RL algorithm (GRPO, RLOO, DAPO). We introduce Newly Rewarded Failure Rate (NRFR), which measures failures among samples whose proxy reward improves over the SFT baseline. Outcome-only rewards cause severe hacking, reaching 48.1% Reward Hacking Rate (RHR), while NRFR exceeding RHR shows that RL creates new failures rather than merely inheriting them. Scaling reduces but does not eliminate hacking: even the 32B model retains a 54.9% worse rate under outcome-only rewards, whereas answer-aware rewards improve the oracle trend at every scale. Robustness is also algorithm- and scale-dependent: GRPO is consistently most resistant, RLOO remains vulnerable, and DAPO improves substantially from 2B to 8B. Visual-evidence rewards help only with reliable verification: keyword-based checks increase hacking, while VLM-as-judge semantic verification reduces it. Overall, multimodal reward hacking is a systematic result of optimizing imperfect rewards, and robust alignment requires rewards and verifiers that remain reliable under optimization pressure.

</details>

---

### [[20_Research/Papers/大模型/ProofCouncil_An_LLM_Agent_for_Solving_Open_Mathematical_Problems|ProofCouncil: An LLM Agent for Solving Open Mathematical Problems]]

![[assets/2607.09474_figure.png|800]]

- **arXiv**: [2607.09474](https://arxiv.org/abs/2607.09474)
- **PDF**: https://arxiv.org/pdf/2607.09474
- **详细分析**: [[20_Research/Papers/大模型/ProofCouncil_An_LLM_Agent_for_Solving_Open_Mathematical_Problems|ProofCouncil: An LLM Agent for Solving Open Mathematical Problems]]
- **作者**: Johannes Schmitt, Tim Gehrunger, Jasper Dekoninck, Gergely Bérczi, Uri Kreitner, Liam Price, David Holmes
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ProofCouncil: An LLM Agent for Solving Open Mathematical Problems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have shown increasing promise in solving open problems in mathematics. However, their performance can be further improved through agentic workflows tailored to real-world mathematical practice. To this end, we introduce ProofCouncil, a mathematical agent that is designed to tackle open problems using an author-critic architecture. ProofCouncil served as a submission to the second batch of FirstProof, a challenge consisting of 10 real-world mathematical problems that agents must solve autonomously. Its submissions for 6 of the 10 problems were judged by the referees to be correct up to at most minor revisions, showing the best performance among participating teams. We also evaluate ProofCouncil on 30 open problems collected from mathematical researchers. Among the 21 solutions that received human feedback, 5 were judged completely correct, 2 more were judged promising pending final verification, and a further 8 contained useful partial progress. In this short paper, we describe the development of ProofCouncil and the agent-building library used to create it, which we release as open source to the community.

</details>

---

### [[20_Research/Papers/大模型/Practical_Source_Code_Recovery_from_Binary_Functions_Using_Anchor-Based_Retrieval_and_LLM_Reasoning|Practical Source Code Recovery from Binary Functions Using Anchor-Based Retrieval and LLM Reasoning]]

![[assets/2607.09452_figure.png|800]]

- **arXiv**: [2607.09452](https://arxiv.org/abs/2607.09452)
- **PDF**: https://arxiv.org/pdf/2607.09452
- **详细分析**: [[20_Research/Papers/大模型/Practical_Source_Code_Recovery_from_Binary_Functions_Using_Anchor-Based_Retrieval_and_LLM_Reasoning|Practical Source Code Recovery from Binary Functions Using Anchor-Based Retrieval and LLM Reasoning]]
- **作者**: Charles Edward Gagnon, Steven H. H. Ding, Philippe Charland, Benjamin C. M. Fung
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Practical Source Code Recovery from Binary Functions Using Anchor-Based Retrieval and LLM Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a practical pipeline for recovering source code from stripped binary functions by combining reverse engineering, anchor-based source code retrieval, and large language model reasoning. Our binary-to-source-code retrieval method attempts to identify the source function from a source code database, rather than generating approximate decompiled pseudocode. It extracts anchors such as strings, constants, external calls, and available function names using Ghidra, retrieves candidate files via an inverted-index search database, narrows candidates to likely function snippets, and re-ranks them with a large language model (LLM) based on disassembly, decompiled code, and source metadata. Confident matches can also serve as anchors in later passes. In an evaluation backed by our high-fidelity source code database on a stripped, optimized tcpdump binary, our proposed binary-to-source matching method achieves 95.2% assembly instruction coverage. Experiments on a GitHub-based retrieval database showed lower performance with 35.5% instruction coverage on average, mainly due to retrieval misses. These results show that source-level binary recovery excels with high-quality databases and remains a useful tool in noisy environments.

</details>

---

### [[20_Research/Papers/大模型/A_Sovereign,_Open-Source_Foundation_Model_for_German_and_English|A Sovereign, Open-Source Foundation Model for German and English]]

![[assets/2607.09424_figure.png|800]]

- **arXiv**: [2607.09424](https://arxiv.org/abs/2607.09424)
- **PDF**: https://arxiv.org/pdf/2607.09424
- **详细分析**: [[20_Research/Papers/大模型/A_Sovereign,_Open-Source_Foundation_Model_for_German_and_English|A Sovereign, Open-Source Foundation Model for German and English]]
- **作者**: The Soofi-Team, :, Benedikt Droste, David Fitzek, Ruben Härle, Lukas Helff, Maximilian Idahl, Alex Jude, Abbas Goher Khan, Maurice Kraus, Timm Ruland, Richard Rutmann...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《A Sovereign, Open-Source Foundation Model for German and English》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GPQA, GQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Soofi S 30B-A3B, a sovereign, open-source Mixture-of-Experts (MoE) hybrid Mamba Transformer foundation model for German and English. Its hybrid design activates only 3B of 30B parameters per token and keeps the inference cache near-constant as context grows, giving it a decisive throughput advantage over dense models for long-context, high-concurrency deployment. Pretrained on roughly 27 trillion tokens with deliberately up-weighted German, Soofi S matches dense 14 to 27B models on aggregate English and German benchmarks while achieving the best code aggregates in both languages among 17 open base models, and outperforms every European sovereign baseline in our comparison, including ones far larger in active parameters. Among fully open models, Soofi S obtains the highest English and German evaluation scores, ahead of Olmo 3 32B and Apertus 70B. Soofi S was built end-to-end on the German Industrial AI Cloud, a sovereign HPC scale AI infrastructure operated by Deutsche Telekom in Munich. Soofi S will be released under highly permissive, open-access terms: weights, selected intermediate checkpoints, full per-source data accounting, hyperparameters, and training and evaluation code. Where source licenses permit, data-construction artifacts are released under permissive licenses; commercially licensed sources are documented with aggregate statistics and exact mixture accounting.

</details>

---

### [[20_Research/Papers/大模型/SVF-CR_Synchronized_Visual-Facial_Cross-Refinement_for_Multimodal_Ambivalence_and_Hesitancy_Recognition|SVF-CR: Synchronized Visual-Facial Cross-Refinement for Multimodal Ambivalence and Hesitancy Recognition]]

![[assets/2607.09417_figure.png|800]]

- **arXiv**: [2607.09417](https://arxiv.org/abs/2607.09417)
- **PDF**: https://arxiv.org/pdf/2607.09417
- **详细分析**: [[20_Research/Papers/大模型/SVF-CR_Synchronized_Visual-Facial_Cross-Refinement_for_Multimodal_Ambivalence_and_Hesitancy_Recognition|SVF-CR: Synchronized Visual-Facial Cross-Refinement for Multimodal Ambivalence and Hesitancy Recognition]]
- **作者**: Hyein Park, Namho Kim, Junhwa Kim
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《SVF-CR: Synchronized Visual-Facial Cross-Refinement for Multimodal Ambivalence and Hesitancy Recognition》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ambivalence and hesitancy are subtle behavioral states that are expressed through a combination of verbal content, facial behavior, visual context, and acoustic cues. Effective recognition therefore requires not only extracting informative unimodal representations, but also modeling how temporally aligned behavioral evidence interacts across modalities. In this paper, we propose a synchronized visual-facial cross-refinement framework (SVF-CR) with pairwise multimodal evidence fusion for ambivalence and hesitancy recognition. The proposed method first extracts whole-video segment tokens and cropped-face segment tokens using the same temporal partition. The synchronized visual and facial tokens are refined through intra-modal self-attention and bidirectional visual-facial cross-attention, allowing whole-video context and local facial behavior to mutually refine each other before evidence construction. We then construct segment-level visual-facial evidence using consistency and discrepancy modeling, followed by temporal self-attention and attention pooling. Textual and acoustic features are lightly refined through context self-attention and are fused with the enhanced visual-facial evidence at the final decision stage using pairwise evidence fusion. Experiments on the BAH (Behavioral Ambivalence/Hesitancy) public evaluation split show that the proposed synchronized visual-facial cross-refinement improves public macro-F1 over both global visual-face token fusion and synchronized evidence baselines, achieving a public macro-F1 of 0.7156. Code is available at : https://github.com/hiinnnii/BAH-Challenge-ECCV2026\_SVF-CR.

</details>

---

### [[20_Research/Papers/大模型/Fictional_Worldbuilding_Multi-Agent_LLM_Collaboration_with_Hierarchical_Context_Compression_and_Iterative_Review|Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review]]

![[assets/2607.09403_figure.jpg|800]]

- **arXiv**: [2607.09403](https://arxiv.org/abs/2607.09403)
- **PDF**: https://arxiv.org/pdf/2607.09403
- **详细分析**: [[20_Research/Papers/大模型/Fictional_Worldbuilding_Multi-Agent_LLM_Collaboration_with_Hierarchical_Context_Compression_and_Iterative_Review|Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review]]
- **作者**: Jingbo Chen, He Wang, Wei Yuan, Yuqiao Lai, Zhenyan Lu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Fictional Worldbuilding: Multi-Agent LLM Collaboration with Hierarchical Context Compression and Iterative Review》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ConceptNet, SenticNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Worldbuilding, the construction of coherent fictional worlds, is a foundational task in game design and literary creation. Large Language Models (LLMs) offer new possibilities for automated content generation, but their application to worldbuilding faces three challenges: context explosion that grows linearly with the building process, the tension between creative diversity and content consistency, and the absence of automated quality assurance. This paper presents AutoWorldBuilder, a multi-agent collaborative system that addresses these challenges through five integrated components: a structured concept network with conflict detection; a DAG-based hybrid batch scheduler that groups tasks by semantic locality; a four-layer context compression mechanism achieving approximately 90% token reduction; an iterative review system with specialized Auditor agents that improves proposal pass rates from 42% to over 85%; and a skill-driven agent architecture supporting zero-code extension with differentiated temperature configuration. Two experiments across 20 diverse worldbuilding tasks, using GPT-OSS 120B and DeepSeek v3.2 as LLM backends, demonstrate a 95.0% success rate. The system generated 56-103 self-consistent concepts per world in 18-31 minutes with zero-conflict delivery. The architectural patterns validated here, including layer-as-budget compression, semantic-locality scheduling, and separation of generation and review, transfer to the broader class of knowledge-intensive, multi-agent LLM applications.

</details>

---

### [[20_Research/Papers/大模型/Deceptive_Grounding_Entity_Attribution_Failure_in_Clinical_Retrieval-Augmented_Generation|Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation]]

![[assets/2607.09349_figure.png|800]]

- **arXiv**: [2607.09349](https://arxiv.org/abs/2607.09349)
- **PDF**: https://arxiv.org/pdf/2607.09349
- **详细分析**: [[20_Research/Papers/大模型/Deceptive_Grounding_Entity_Attribution_Failure_in_Clinical_Retrieval-Augmented_Generation|Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation]]
- **作者**: Cedric Caruzzo, Donggeun Yoo, Tae Soo Kim
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Security, Systems

#### 研究背景与动机

《Deceptive Grounding: Entity Attribution Failure in Clinical Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation evaluation checks whether model claims are factually grounded in retrieved documents. It does not check whether retrieved evidence is attributed to the correct entity. A clinical RAG response can pass every automated check (zero hallucinations, near-perfect faithfulness, real citations) while presenting drug Y's clinical evidence as evidence about queried drug X. We term this deceptive grounding (DG): a failure invisible to faithfulness, hallucination, and citation checks because every claim is sourced from a real document, about the wrong entity. Using a controlled factorial benchmark across 13 models, we find DG rates spanning 8-87% at peak adversarial conditions. Medical and biomedical fine-tuned models reach up to 86.7%; domain specialization amplifies the failure rather than mitigating it. A controlled ablation identifies the mechanism: removing entity-specific clinical evidence from retrieved documents eliminates entity-attribution failure entirely, shifting all failures to confabulation. The two failure modes respond to the same trigger, taking different paths. Production measurement across 740 drug-disease pairs finds 7.8% overall DG in a deployed RAG system, rising to 13.6% for recently approved drugs. Entity-attribution verification (checking that cited evidence applies to the queried entity) detects DG at 97.0% precision and 98.7% DG recall (IPW-adjusted human gold standard); no existing framework implements it.

</details>

---

### [[20_Research/Papers/具身智能/Shortcut_Trajectory_Planning_for_Efficient_Offline_Reinforcement_Learning|Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning]]

![[assets/2607.09336_figure.png|800]]

- **arXiv**: [2607.09336](https://arxiv.org/abs/2607.09336)
- **PDF**: https://arxiv.org/pdf/2607.09336
- **详细分析**: [[20_Research/Papers/具身智能/Shortcut_Trajectory_Planning_for_Efficient_Offline_Reinforcement_Learning|Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning]]
- **作者**: Guanquan Wang, Yoshimasa Tsuruoka
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型, 机器人
- **相关性评分**: 2.52（加权：具身智能 0.9，强化学习 0.96，世界模型 0.36，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Shortcut Trajectory Planning for Efficient Offline Reinforcement Learning》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：D4RL, SORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based trajectory planners have shown strong performance in offline reinforcement learning, but their iterative denoising process often incurs high inference cost. Consistency-based planners reduce the number of sampling steps, yet they typically rely on a two-stage teacher--student distillation pipeline that increases training cost and may introduce instability. We propose Shortcut Trajectory Planning (STP), an offline model-based reinforcement learning framework that incorporates shortcut models as efficient trajectory generators. STP trains a conditional shortcut trajectory model in a single stage, supports adjustable one-step and few-step inference through step-size conditioning, and selects candidate plans using a critic augmented with feasibility-aware correction. Across standard D4RL benchmarks, including locomotion, navigation, manipulation, and dexterous control tasks, STP achieves strong performance while simplifying the training pipeline for fast generative planning.

</details>

---

### [[20_Research/Papers/具身智能/Communication-Efficient_Digital-Twin_Coordination_for_Heterogeneous_LLM_Embodied_Agents_over_Computing_Power_Networks|Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks]]

![[assets/2607.09330_figure.jpg|800]]

- **arXiv**: [2607.09330](https://arxiv.org/abs/2607.09330)
- **PDF**: https://arxiv.org/pdf/2607.09330
- **详细分析**: [[20_Research/Papers/具身智能/Communication-Efficient_Digital-Twin_Coordination_for_Heterogeneous_LLM_Embodied_Agents_over_Computing_Power_Networks|Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks]]
- **作者**: Nuocheng Yang, Sihua Wang, Zihan Chen, Tony Q. S. Quek, Changchuan Yin
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.2，大模型 0.9，强化学习 0.2，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Communication-Efficient Digital-Twin Coordination for Heterogeneous LLM Embodied Agents over Computing Power Networks》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agent teams powered by heterogeneous large language models (LLMs) are being widely deployed in physical artificial intelligence such as smart factories, warehouses, and service robotics. To enable collaboration among such an agent team, efficient coordination mechanisms that operate reliably under limited network resources are required. However, existing heterogeneous LLM-agent coordination frameworks that rely on multi-round natural-language-based conversations introduce three coupled challenges. First, inter-agent dialogue incurs communication overhead that grows rapidly with team size. Second, the quality of coordination is constrained by the heterogeneous capabilities of the agent team's LLMs. Third, agents may suffer from action delays due to iterative negotiation. To address these challenges, we propose LDT-Coord, a networked coordination framework built upon a lightweight digital twin (DT). Specifically, each agent independently selects its intended action and reports both the action decision and a structured temporal constraint over shared resources to the DT server, thereby decoupling coordination performance from natural-language reasoning ability. Then, DT executes a training-free, rule-based orchestrator algorithm to resolve cross-agent conflicts and returns coordination instructions to prevent such conflicts. To further reduce communication overhead, we formulate agent reporting control as a constrained partially observable Markov decision process (C-POMDP) and solve it with the PPO-Lagrangian algorithm. Simulation results show that LDT-Coord achieves a task success rate comparable to conventional coordination methods while reducing communication overhead by more than 70x and maintaining robustness under LLM heterogeneity.

</details>

---

### [[20_Research/Papers/大模型/LongMedBench_Benchmarking_Medical_Agents_for_Long-Horizon_Clinical_Decision-Making|LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making]]

![[assets/2607.09322_figure.png|800]]

- **arXiv**: [2607.09322](https://arxiv.org/abs/2607.09322)
- **PDF**: https://arxiv.org/pdf/2607.09322
- **详细分析**: [[20_Research/Papers/大模型/LongMedBench_Benchmarking_Medical_Agents_for_Long-Horizon_Clinical_Decision-Making|LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making]]
- **作者**: Yanzhen Chen, Zihan Xu, Xiaocheng Zhang, Zhiting Fan, Weiqi Zhai, Hongxia Xu, Zuozhu Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《LongMedBench: Benchmarking Medical Agents for Long-Horizon Clinical Decision-Making》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DiagBench, LongMedBench, MedAgentBench, MedBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we introduce LongMedBench, a real-world EHR-based benchmark for long-horizon clinical decision-making. Prior evaluations of LLM-based medical agents have largely emphasized short-context knowledge QA and tool use. However, real-world medical care is inherently longitudinal, and clinicians must aggregate evidence across repeated visits, tests, and evolving treatments. Therefore, long-horizon interaction is essential for realistic assessment. LongMedBench is constructed via a reproducible pipeline that integrates MIMIC-IV admission records and clinical notes into time-series event streams and long-context memory datasets, enabling long-horizon, multi-session interactions between agents and a clinical environment. It comprises 335 patients, with 19.72 inpatient visits per patient on average and 44.91 medical events per visit. Guided by the long-horizon decision process, we propose an evaluation taxonomy with three suites: fact-based QA, temporal reasoning, and long-horizon decision-making. This taxonomy measures how agents understand and leverage historical patient information over extended horizons. Our experiments show that while recent LLMs can make good use of explicit timestamps, they have challenges in implicit time inference; The RAG and agent memory system can improve the performance of information retrieval tasks, but the performance of decision-making tasks is highly dependent on the model's immediate context.

</details>

---

### [[20_Research/Papers/世界模型/Tactile_and_Vision_Conditioned_Contact-Centric_Control_for_Whole-Arm_Manipulation|Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation]]

![[assets/2607.09218_figure.png|800]]

- **arXiv**: [2607.09218](https://arxiv.org/abs/2607.09218)
- **PDF**: https://arxiv.org/pdf/2607.09218
- **详细分析**: [[20_Research/Papers/世界模型/Tactile_and_Vision_Conditioned_Contact-Centric_Control_for_Whole-Arm_Manipulation|Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation]]
- **作者**: Rishabh Madan, Angchen Xie, Samantha Saak, Andres Blanco, Dohyeok Lee, Sarah Grace Brown, Yunting Yan, Mark Zolotas, Jose Barreiros, Tapomayukh Bhattacharjee
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，世界模型 0.4，机器人 0.5）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Tactile and Vision Conditioned Contact-Centric Control for Whole-Arm Manipulation》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-arm manipulation involves direct contact with the environment while the robot completes a task by distributing contact across multiple links as contacts form, slide, and break. This setting breaks common implicit assumptions in many learning-based manipulation pipelines: arm configuration tightly couples motion and contact forces, contact state is partially observed under occlusion, and purely learned rollouts can become physically inconsistent under distribution shift because many multi-link contact configurations are sparsely represented in the data. To address this, we propose TACTIC (Tactile and Vision Conditioned Contact-Centric Control), a receding-horizon controller for whole-arm manipulation. TACTIC uses a contact-centric hybrid predictive model that combines RGB-D, distributed tactile sensing, and a compact 2D proximity representation. The model couples a learned, action-conditioned latent dynamics model with analytical kinematics through contact Jacobians, enabling rollouts of future contact configurations and interaction forces. TACTIC integrates these rollouts into a sampling-based MPC planner with contact-aware action sampling: contact Jacobian-based projections steer sampled action sequences toward force-modulating directions, and objectives defined over predicted proximity and interaction forces trade task progress against whole-arm force regulation. We evaluate TACTIC in simulation against state-of-the-art model-based and model-free methods, and perform ablations that isolate the contribution of each design choice. TACTIC consistently outperforms other methods. We further demonstrate real-world performance on a robot with distributed tactile sensing across three whole-arm manipulation tasks that require multi-contact trajectories: turning over and repositioning a manikin, and goal-reaching in a 3D dynamic maze. Website: https://emprise.cs.cornell.edu/tactic

</details>

---

### [[20_Research/Papers/大模型/Toward_Auditable_AI_Scientists_A_Hypothesis_Evolution_Protocol_for_LLM_Agents|Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents]]

![[assets/2607.09195_figure.png|800]]

- **arXiv**: [2607.09195](https://arxiv.org/abs/2607.09195)
- **PDF**: https://arxiv.org/pdf/2607.09195
- **详细分析**: [[20_Research/Papers/大模型/Toward_Auditable_AI_Scientists_A_Hypothesis_Evolution_Protocol_for_LLM_Agents|Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents]]
- **作者**: Izumi Takahara, Teruyasu Mizoguchi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Toward Auditable AI Scientists: A Hypothesis Evolution Protocol for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly expected to play a central role in AI-driven scientific discovery. Equipped with broad knowledge, flexible reasoning, and tool use, they have the potential to autonomously explore and solve scientific problems by repeatedly proposing hypotheses, testing them, and revising their beliefs in the light of the evidence. In current agents, however, these hypotheses, tests, and belief updates are buried in unstructured logs, and no mechanism lets the agent or the human researcher audit that process. Here we propose the Hypothesis Evolution Protocol (HEP), an agent harness that provides hypothesis generation, evaluation, and evolution as explicit, auditable operations. On materials-science research tasks, a HEP-equipped agent operates the hypothesis--test--evidence--belief cycle that planning-style agents lack, generalizes across research questions, and exploits the protocol more fully as the base LLM becomes more capable. These results mark a step toward auditable AI scientists, whose scientific reasoning can be inspected, verified, and built upon.

</details>

---

### [[20_Research/Papers/大模型/Scoped_Verification_for_Reliable_Long-Horizon_Agentic_Context_Evolution_under_Distribution_Shift|Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift]]

![[assets/2607.09175_figure.jpg|800]]

- **arXiv**: [2607.09175](https://arxiv.org/abs/2607.09175)
- **PDF**: https://arxiv.org/pdf/2607.09175
- **详细分析**: [[20_Research/Papers/大模型/Scoped_Verification_for_Reliable_Long-Horizon_Agentic_Context_Evolution_under_Distribution_Shift|Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift]]
- **作者**: Dan C. Hsu, Luke Lu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Scoped Verification for Reliable Long-Horizon Agentic Context Evolution under Distribution Shift》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deployed LLM agents rely on agentic context, the model-external textual control content assembled by an operational harness. In this work, the mutable component of that context is a persistent system-level instruction that is updated from operational experience while the model, tools, and harness remain fixed. Over long evolution horizons, flat-text maintenance makes verification increasingly difficult as accumulated instructions grow and interact. We propose Graph-Regularized Agentic Context Evolution (GRACE), which maintains the persistent instruction component as a typed semantic graph and validates proposed updates within the local typed neighborhoods of modified nodes. Accepted graph updates are reconstructed as incremental edits to the textual instruction checkpoint used at deployment. We evaluate GRACE within a fixed telecom agent harness derived from $τ^2$-bench under a controlled distribution-shift protocol. Across five independent replications, GRACE improves strict reliability, measured by pass^3, from the Gemini 2.5 Flash zero-shot value of 0.091 to 0.673$\pm$0.136 at the final checkpoint. This exceeds a Gemini 3.1 Pro zero-shot reference of 0.242 on the same held-out set, while the flat-text HCE baseline finishes at 0.191$\pm$0.051. These results identify two requirements for reliable long-horizon context evolution, a structural substrate that makes verification local and a consolidation mechanism that keeps accumulated instruction content usable.

</details>

---

### [[20_Research/Papers/大模型/KV-PRM_Efficient_Process_Reward_Modeling_via_KV-Cache_Transfer_for_Multi-Agent_Test-Time_Scaling|KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling]]

![[assets/2607.09153_figure.png|800]]

- **arXiv**: [2607.09153](https://arxiv.org/abs/2607.09153)
- **PDF**: https://arxiv.org/pdf/2607.09153
- **详细分析**: [[20_Research/Papers/大模型/KV-PRM_Efficient_Process_Reward_Modeling_via_KV-Cache_Transfer_for_Multi-Agent_Test-Time_Scaling|KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling]]
- **作者**: Peng Kuang, Haibo Jin, Xiaoyu Han, Yanli Wang, Xiaopeng Yuan, Ye Yu, Kaidi Xu, Haohan Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《KV-PRM: Efficient Process Reward Modeling via KV-Cache Transfer for Multi-Agent Test-Time Scaling》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Process Reward Models (PRMs) have been proven to be highly effective in guiding test-time scaling (TTS) methods, which significantly boost the capabilities of LLM-based multi-agent systems. However, existing PRMs are text-based: they re-encode the entire trajectory text from scratch. In long multi-agent rollouts, the scoring cost, growing quadratically with respect to sequence length L, creates a severe computational bottleneck, severely limiting PRMs' application in long-context scenarios. To resolve this, we introduce KV-PRM, a highly efficient process reward model that eliminates the heavy text re-encoding by directly reading the KV cache produced naturally during the LLM's generation phase. By processing a single "verify token" against the pre-existing KV cache, KV-PRM reduces the scoring cost from O(L^2) to O(L). We formally prove that the KV cache contains strictly greater information capacity than text, and is more efficient for downstream reward modeling. Empirically, across the MATH, GSM8K, and AIME benchmarks, KV-PRM matches or strictly outperforms text-PRMs under various TTS methods such as Beam Search, MCTS, and Weighted Voting, with up to a 5,000x reduction in scoring FLOPs, a 37x reduction in latency, and a 34x reduction in per-sequence memory footprint compared to text-based PRMs.

</details>

---

### [[20_Research/Papers/大模型/MedRealMM_A_Real-World_Multimodal_Benchmark_for_Chinese_Online_Medical_Consultation|MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation]]

![[assets/2607.09142_first_page.png|800]]

- **arXiv**: [2607.09142](https://arxiv.org/abs/2607.09142)
- **PDF**: https://arxiv.org/pdf/2607.09142
- **详细分析**: [[20_Research/Papers/大模型/MedRealMM_A_Real-World_Multimodal_Benchmark_for_Chinese_Online_Medical_Consultation|MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation]]
- **作者**: Runhan Shi, Quan Zhou, Yuqian Xu, Shuai Yang, Xin Wu, Zitong Zhou, Hui Liu, Bin Cha, Zheming Wang, Liya Li, Wei Wei, Haoyuan Hu...
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《MedRealMM: A Real-World Multimodal Benchmark for Chinese Online Medical Consultation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly deployed in online medical consultation, yet existing benchmarks remain poorly aligned with real clinical practice. Many rely on synthetic conversations or patient simulators, omit patient-uploaded medical images, or evaluate open-ended clinical responses using multiple-choice or lexical-overlap metrics that poorly reflect clinical quality. We introduce \textbf{MedRealMM}, a large-scale benchmark for multimodal online medical consultation built from de-identified patient-doctor interactions collected from a nationwide Chinese internet hospital. MedRealMM uses a Multimodal Clinical Challenge Point (MCCP) extraction framework to identify clinically demanding moments in authentic consultation trajectories and converts each into a standardized next-response generation task while preserving the preceding text-image context. Each instance is paired with a case-specific rubric refined by physicians that rewards clinically desirable behaviors and penalizes unsafe, unsupported, or contradictory responses. The current release contains 5,620 real-world multimodal cases spanning 64 clinical departments. We evaluate 19 general-purpose and medical-specialized LLMs, including text-only and multimodal systems. Our results show that image information is critical for reliable clinical performance and that current frontier models remain below the online physician response. Although some frontier models satisfy as many or more positive clinical criteria than physicians, they trigger more negative criteria, indicating that safety-sensitive error avoidance remains a central bottleneck. MedRealMM offers a realistic and reproducible benchmark for evaluating multimodal medical reasoning in real-world online consultation. The dataset will be publicly available on Hugging Face at https://huggingface.co/datasets/jdh-algo/MedRealMM.

</details>

---

### [[20_Research/Papers/大模型/Augmenting_Fundamental_Analysis_with_Large_Language_Models_A_RAG-Based_System_for_Generating_Investor_Briefs|Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs]]

![[assets/2607.09121_figure.png|800]]

- **arXiv**: [2607.09121](https://arxiv.org/abs/2607.09121)
- **PDF**: https://arxiv.org/pdf/2607.09121
- **详细分析**: [[20_Research/Papers/大模型/Augmenting_Fundamental_Analysis_with_Large_Language_Models_A_RAG-Based_System_for_Generating_Investor_Briefs|Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs]]
- **作者**: Bartosz Ziółko, Kacper Dobrzeniewski
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Augmenting Fundamental Analysis with Large Language Models: A RAG-Based System for Generating Investor Briefs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this study, we examine the opportunities brought by Large Language Models (LLMs) to various aspects of fundamental analysis of companies based on their reports as well as data and documents describing macroeconomic situation like GDP and inflation changes as well as documents filled to the U.S. Securities and Exchange Commission (SEC) which can be found in EDGAR. We were preprocessing those data and than sending via API to gpt-4o model in a Retrieval-Augmented Generation (RAG) like regime. We prepared as well a document describing an exemplar investor knowledge based on Kitchin cycles. We were scanning data important for analysis of 9 companies for 4 weeks. Using LLM we were producing automatic briefs about them. They were sent to nine participants who are individual investors to evaluate usefulness of such approach to data analysis.

</details>

---

### [[20_Research/Papers/其他/L-MAD_A_Systematic_Evaluation_of_Multi-Agent_Debate_Structures_in_Legal_Reasoning|L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning]]

![[assets/2607.09099_figure.png|800]]

- **arXiv**: [2607.09099](https://arxiv.org/abs/2607.09099)
- **PDF**: https://arxiv.org/pdf/2607.09099
- **详细分析**: [[20_Research/Papers/其他/L-MAD_A_Systematic_Evaluation_of_Multi-Agent_Debate_Structures_in_Legal_Reasoning|L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning]]
- **作者**: Tan-Minh Nguyen, Hoang-Trung Nguyen, Huu-Dong Nguyen, Dinh-Truong Do, Thi-Hai-Yen Vuong, Le-Minh Nguyen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《L-MAD: A Systematic Evaluation of Multi-Agent Debate Structures in Legal Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While multi-agent debate (MAD) frameworks have shown significant potential in general reasoning, their effectiveness in highly structured, knowledge-heavy legal domains remains under-explored. In this work, we introduce the Legal Multi-Agent Debate (L-MAD) framework to systematically evaluate different debate structures and aggregation methods within Legal Textual Entailment. By assigning distinct expert personas to multiple agents, L-MAD improves upon strong single-agent baselines by up to 8\%. Furthermore, analyzing how debate scales reveals a clear trade-off: increasing the agent population reduces inconsistency and improves accuracy, whereas extending discussion rounds induces a detrimental \textit{over-deliberation drift} where agents reinforce each other's mistakes. Ultimately, our findings outline the practical boundaries and safety margins of deploying collaborative multi-agent systems in high-stakes legal reasoning environments.

</details>

---

### [[20_Research/Papers/大模型/Neuro-Agentic_Control_A_Deep_Learning-based_LLM-Powered_Agentic_AI_Framework_for_Controlling_Security_Controls|Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls]]

![[assets/2607.09076_figure.png|800]]

- **arXiv**: [2607.09076](https://arxiv.org/abs/2607.09076)
- **PDF**: https://arxiv.org/pdf/2607.09076
- **详细分析**: [[20_Research/Papers/大模型/Neuro-Agentic_Control_A_Deep_Learning-based_LLM-Powered_Agentic_AI_Framework_for_Controlling_Security_Controls|Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls]]
- **作者**: Saroj Gopali, Bipin Chhetri, Deepika Giri, Sima Siami-Namini, Akbar Siami Namin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《Neuro-Agentic Control: A Deep Learning-based LLM-Powered Agentic AI Framework for Controlling Security Controls》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cyberattacks on operational technology are increasingly causing costly downtime and physical damage, exposing the limitations of traditional rule-based monitoring in industrial IoT environments. While Large Language Models (LLMs) have strong semantic reasoning abilities to assist in decision support, their hallucinatory nature presents unacceptable safety liabilities for closed-loop control. This paper introduces a neuro-agentic control framework, a novel architecture that couples an LLM-based planner (i.e., such as Gemini 2.5 Flash-Lite) with a pre-trained Time-Series Foundation Model (TimesFM), to achieve physics-grounded autonomous defense. The paper introduces a ``Counterfactual Physics Injection'' mechanism that simulates the impact of LLM-proposed interventions within the numerical latent space of the foundation model before actuation, while allowing the system to reject hallucinatory or unsafe actions. Evaluated on an industrial dataset (e.g., the Secure Water Treatment (SWaT)) in the context of stochastic attack scenarios, the framework exhibited better performance compared to LSTM and TCN baselines. The Neuro-Agentic Loop prevented five breaches (33.3%) below the threshold versus LSTM (26.7%) and TCN (13.3%), with zero physically invalid (hallucinated) actions executed. These results demonstrate the efficacy of using foundation models as deterministic ``Sentinels'' to safeguard agentic AI in critical infrastructure.

</details>

---

### [[20_Research/Papers/其他/Inside_the_Skill_Market_From_Software_Engineering_Activities_to_Reusable_Agent_Skills|Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills]]

![[assets/2607.09065_figure.png|800]]

- **arXiv**: [2607.09065](https://arxiv.org/abs/2607.09065)
- **PDF**: https://arxiv.org/pdf/2607.09065
- **详细分析**: [[20_Research/Papers/其他/Inside_the_Skill_Market_From_Software_Engineering_Activities_to_Reusable_Agent_Skills|Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills]]
- **作者**: Jialun Cao, Xinru Yan, Songqiang Chen, Yaojie Lu, Zhongxin Liu, Shing-Chi Cheung
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Inside the Skill Market: From Software Engineering Activities to Reusable Agent Skills》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SkillNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Software engineering (abbrev. SE) has continuously evolved through increasingly powerful forms of reuse, from source code and libraries to components and services. Recent advances in AI agents have introduced a potentially new reusable artifact: skills. Emerging agent skill repositories and marketplaces enable developers to package, share, and reuse SE expertise as reusable skills. This trend raises a fundamental question: what SE activities are being encapsulated into reusable skills? Existing studies primarily focus on a broad range of skills acquisition, safety, or benchmarking, while lacking a systematic understanding of SE-specific skills and their coverage across the software development lifecycle. To address this gap, we conduct the first large-scale empirical study of SE skills in public repositories and marketplaces. We collect and analyze a large corpus of SE skills, examining the activities they encapsulate, lifecycle coverage, evolution characteristics, and evaluation mechanisms. Our findings reveal that SE activities are increasingly becoming reusable artifacts via skills and suggest promising research opportunities for skill recommendation and engineering-oriented structuring, as well as the need for mechanisms to encapsulate high-context SE activities into reusable skills. Overall, our study provides the first activity-centric characterization of SE skills and reveals how SE activities are increasingly being transformed into reusable skills. These findings offer new insights into skill reuse, ecosystem development, and the future of agent-centric SE.

</details>

---

### [[20_Research/Papers/强化学习/ARCANA_A_Reflective_Multi-Agent_Program_Synthesis_Framework_for_ARC-AGI-2_Reasoning|ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning]]

![[assets/2607.09059_figure.jpg|800]]

- **arXiv**: [2607.09059](https://arxiv.org/abs/2607.09059)
- **PDF**: https://arxiv.org/pdf/2607.09059
- **详细分析**: [[20_Research/Papers/强化学习/ARCANA_A_Reflective_Multi-Agent_Program_Synthesis_Framework_for_ARC-AGI-2_Reasoning|ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning]]
- **作者**: Kunbo Zhang, Lei Fu, Zeyu Wang, Zijing Liu, Kejian Tong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《ARCANA: A Reflective Multi-Agent Program Synthesis Framework for ARC-AGI-2 Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MERIT-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present ARCANA, a collaborative multi agent framework for solving ARC AGI 2 tasks under strict test time and hardware constraints. ARCANA decomposes each task into iterative perception, hypothesis generation, symbolic execution, and reflective refinement. A perceptual grounding agent builds object centric scene graphs from raw grids, a latent program policy proposes diverse DSL programs, a symbolic executor verifies candidates on demonstrations, and a reflective agent synthesizes failure driven feedback for the next turn. These agents communicate through a shared differentiable blackboard and are scheduled by a learned meta controller. The design combines structured program search with adaptive multi turn correction, improving reasoning efficiency and solution quality on challenging abstract transformation tasks.

</details>

---

### [[20_Research/Papers/大模型/Correlation-Aware_Contextual_Bandits_with_Surrogate_Rewards_for_LLM_Routing|Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing]]

![[assets/2607.09015_figure.png|800]]

- **arXiv**: [2607.09015](https://arxiv.org/abs/2607.09015)
- **PDF**: https://arxiv.org/pdf/2607.09015
- **详细分析**: [[20_Research/Papers/大模型/Correlation-Aware_Contextual_Bandits_with_Surrogate_Rewards_for_LLM_Routing|Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing]]
- **作者**: Ajay Narayanan Sridhar, Ronak Singh, Mehrdad Mahdavi, Vijaykrishnan Narayanan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Correlation-Aware Contextual Bandits with Surrogate Rewards for LLM Routing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study contextual bandit problems with correlated arms and access to surrogate reward signals produced by a machine learning model, motivated by applications such as large language model (LLM) routing. Unlike classical contextual bandits that rely solely on bandit feedback and assume conditional independence across arms, our setting allows context-dependent inter-arm correlations and auxiliary reward information that may be noisy or misspecified. We propose algorithms that leverage such surrogate rewards through two complementary designs. A coupled reward-mixing approach pools true and surrogate rewards to accelerate learning when surrogate signals are reliable, while a decoupled prediction-mixing approach maintains separate estimators for bandit feedback and surrogate rewards and adaptively combines their predictions. This decoupling yields robustness to surrogate misspecification, recovering regret guarantees comparable to reward-only bandit methods in the worst case, while achieving improved regret when surrogate predictions are sufficiently informative. We provide theoretical regret analyses for both approaches and evaluate them on LLM routing benchmarks under varying accuracy versus cost trade-offs. The results demonstrate improved sample efficiency and consistently better accuracy-cost trade-offs compared to standard contextual bandit baselines and strong static routing methods.

</details>

---

### [[20_Research/Papers/强化学习/SCATE_Learning_to_Supervise_Coding_Agents_for_Cost-Effective_Test_Generation|SCATE: Learning to Supervise Coding Agents for Cost-Effective Test Generation]]

![[assets/2607.08983_figure.png|800]]

- **arXiv**: [2607.08983](https://arxiv.org/abs/2607.08983)
- **PDF**: https://arxiv.org/pdf/2607.08983
- **详细分析**: [[20_Research/Papers/强化学习/SCATE_Learning_to_Supervise_Coding_Agents_for_Cost-Effective_Test_Generation|SCATE: Learning to Supervise Coding Agents for Cost-Effective Test Generation]]
- **作者**: Sijia Gu, Noor Nashid, Ali Mesbah
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SCATE: Learning to Supervise Coding Agents for Cost-Effective Test Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While autonomous coding agents have significantly advanced automated test generation, they remain fundamentally limited by lazy generation, a phenomenon where agents prematurely terminate tasks and systematically avoid complex programmatic logic, resulting in inadequate code coverage. Currently, mitigating this premature termination requires continuous human-in-the-loop supervision. This heavy reliance on human intuition creates a bottleneck that negates the efficiency gains of automated generation. We propose SCATE, a framework for adaptive, automated supervision of coding agents that replaces human intervention during test generation. By formulating supervision as a contextual bandit problem, SCATE learns to select the most promising testing actions based on the current coverage and class testability metrics, maximizing coverage gains while minimizing wasted generation effort. Our empirical evaluation demonstrates that SCATE integrates seamlessly with different coding agents. When applied to GEMINI-CLI, it achieves 32.3% higher line coverage and 30.9% higher branch coverage than the agent-only baseline. A comparison with CLAUDE CODE confirms the framework dynamically adapts its policy to optimize each agent's unique strengths. SCATE also consistently outperforms state-of-the-art non-agentic approaches across all metrics.

</details>

---

### [[20_Research/Papers/大模型/The_Patchwork_Problem_in_LLM-Generated_Code|The Patchwork Problem in LLM-Generated Code]]

![[assets/2607.08981_figure.png|800]]

- **arXiv**: [2607.08981](https://arxiv.org/abs/2607.08981)
- **PDF**: https://arxiv.org/pdf/2607.08981
- **详细分析**: [[20_Research/Papers/大模型/The_Patchwork_Problem_in_LLM-Generated_Code|The Patchwork Problem in LLM-Generated Code]]
- **作者**: Viraaji Mothukuri, Reza M. Parizi
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM

#### 研究背景与动机

《The Patchwork Problem in LLM-Generated Code》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BaxBench, EvoCodeBench, RepoBench, SafeGenBench, SecRepoBench, SecureVibeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-generated code often compiles, passes tests, and appears correct, yet breaks once deployed. The root cause is frequently structural rather than logical. A generated endpoint references configuration keys never declared in the project, an import targets a package that does not exist in any registry, or a new route omits the authentication guard applied to every sibling endpoint. Each patch is locally valid but globally incoherent, and standard CI toolchains rarely surface these failures. As LLM-powered coding tools see widespread adoption, this blind spot poses a growing risk to software quality. We call this the \textbf{patchwork problem}. This paper formalizes structural coherence as consistency invariants over graph representations of repository artifacts, including import, call, dependency, configuration, schema, resource, control-flow, and routing graphs, and introduces an eight-category failure taxonomy distinguishing defects specific to LLM generation from those merely amplified by it. We present a hybrid verification framework that delegates to mature static analysis tools where they already excel and deploys purpose-built detectors for cross-cutting invariants underserved by existing toolchains, targeting provable constraint violations rather than heuristic pattern matching. Empirical evaluation across two frontier models under four prompting strategies reveals that the vast majority of structural failures evade type checking, testing, and SAST entirely, and that failure patterns diverge qualitatively between models in ways that challenge model-agnostic mitigation strategies. External validation on real-world AI-generated repositories confirms that these failures are not artifacts of controlled experimentation but are prevalent wherever LLMs write code with minimal human oversight.

</details>

---

### [[20_Research/Papers/具身智能/CLAP_Direct_VLM-to-VLA_Adaptation_via_Language-Action_Grounding|CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding]]

![[assets/2607.08974_figure.png|800]]

- **arXiv**: [2607.08974](https://arxiv.org/abs/2607.08974)
- **PDF**: https://arxiv.org/pdf/2607.08974
- **详细分析**: [[20_Research/Papers/具身智能/CLAP_Direct_VLM-to-VLA_Adaptation_via_Language-Action_Grounding|CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding]]
- **作者**: Yuri Ishitoya, Jeremy Siburian, Masashi Hamaya, Kuniaki Saito, Cristian C. Beltran-Hernandez, Mai Nishimura
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.8，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《CLAP: Direct VLM-to-VLA Adaptation via Language-Action Grounding》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GenVLA, SmolVLA, TinyVLA, TraceVLA, VLABench, VLM-to-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) inherit semantic capabilities from pretrained VLMs, yet large-scale post-training on robot data and architectural modifications can reshape the backbone so extensively that it becomes difficult to isolate what the VLM contributes to control. Directly converting pretrained VLMs into VLAs with minimal architectural change offers a more transparent path to understanding how VLM capabilities transfer across model scales. The core obstacle is output-distribution mismatch: predicting actions as bare numeric token sequences moves generation away from the VLM's pretrained language distribution, degrading the capabilities we seek to preserve. To address this, we propose CLAP (Causal Language-Action Prediction), which prepends each numeric action sequence with a natural-language action description, causally conditioning precise action-token prediction on a language-action plan without modifying the backbone architecture. With single-epoch fine-tuning alone, 2B CLAP achieves 90.8% on LIBERO (+14.9 pt over VLA-0) and improves robustness on LIBERO-PRO under language, object, and spatial perturbations. We will release CLAP at 0.8B, 2B, and 4B as an open-weight, multi-scale compact VLA family from a single VLM lineage, enabling controlled analysis of VLM-to-VLA capability transfer.

</details>

---

### [[20_Research/Papers/大模型/Long-Horizon-Terminal-Bench_Testing_the_Limits_of_Agents_on_Long-Horizon_Terminal_Tasks_with_Dense_Reward-Based_Grading|Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading]]

![[assets/2607.08964_figure.png|800]]

- **arXiv**: [2607.08964](https://arxiv.org/abs/2607.08964)
- **PDF**: https://arxiv.org/pdf/2607.08964
- **详细分析**: [[20_Research/Papers/大模型/Long-Horizon-Terminal-Bench_Testing_the_Limits_of_Agents_on_Long-Horizon_Terminal_Tasks_with_Dense_Reward-Based_Grading|Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading]]
- **作者**: Zongxia Li, Zhongzhi Li, Yucheng Shi, Ruhan Wang, Junyao Yang, Zhichao Liu, Xiyang Wu, Anhao Li, Yue Yu, Ninghao Liu, Lichao Sun, Haotao Mi...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Long-Horizon-Terminal-Bench: Testing the Limits of Agents on Long-Horizon Terminal Tasks with Dense Reward-Based Grading》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Long-Horizon-Terminal-Bench, SWE-Bench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents have become capable of autonomously completing short, well-specified tasks. However, existing terminal benchmarks largely focus on simple problems that finish within minutes and are evaluated only by their final outcome. This setup overlooks intermediate progress and partial solutions, yielding sparse reward signals and an incomplete picture of agent capability. We introduce Long-Horizon-Terminal-Bench, a terminal benchmark of 46 long-horizon tasks spanning nine categories, including experiment reproduction, software engineering, multimodal analysis, interactive games, and scientific computing. Each task follows a Terminal-Bench-style setup with a reference solution or simulation engine, but is further decomposed into fine-grained graded subtasks. This design enables dense intermediate rewards and partial credit, allowing evaluation to capture not only whether an agent reaches the final goal, but also how far it progresses on open-ended workflows. Tasks in Long-Horizon-Terminal-Bench typically require hundreds of episodes and minutes to hours of execution, stressing long-horizon planning, long-context management, and iterative debugging rather than one-shot problem solving. We evaluate 15 frontier models and find that agents consume on average 9.9M tokens per task, with roughly 231 episodes and 85.3 minutes of execution time per run, making Long-Horizon-Terminal-Bench more demanding than prior terminal-based benchmarks. Even the strongest tested model achieves 15.2% pass@1 at a partial-reward threshold of 0.95 and 10.9% at a perfect-reward threshold of 1.0, while the mean pass rate across models is 4.3% and 1.7% under the two thresholds, respectively. These results reveal headroom for improvement. We further analyze failure modes and error patterns, and release Long-Horizon-Terminal-Bench to support future progress on long-horizon terminal agents.

</details>

---

### [[20_Research/Papers/大模型/Eluna_An_Agentic_LLM_System_for_Automating_Warehouse_Operations_with_Reasoning_and_Task_Execution|Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution]]

![[assets/2607.08960_figure.png|800]]

- **arXiv**: [2607.08960](https://arxiv.org/abs/2607.08960)
- **PDF**: https://arxiv.org/pdf/2607.08960
- **详细分析**: [[20_Research/Papers/大模型/Eluna_An_Agentic_LLM_System_for_Automating_Warehouse_Operations_with_Reasoning_and_Task_Execution|Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution]]
- **作者**: Ning Liu, Kalle Kujanpää, Zhaoxuan Zhu, P Aditya Sreekar, Kaiwen Liu, Chuanneng Sun, Jorge Marchena Menendez, Matthew Bales, Tianyu Yang, Shahnawaz Alam, Rose Yu, Baoyuan Liu...
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Eluna: An Agentic LLM System for Automating Warehouse Operations with Reasoning and Task Execution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Warehouse operations are governed by Standard Operating Procedures (SOPs) that encode complex, multi-system decision logic, which must be executed reliably under strict time constraints, yet LLM agents lack mechanisms to enforce procedural compliance and degrade under the context overload full SOP specifications introduce. We present Eluna, a production-deployed agentic system for reliable SOP execution. Eluna is a graph-guided, multi-agent framework that encodes SOPs as directed acyclic graphs with progressive disclosure and delegates independent tasks to parallel sub-agents, each with persistent code execution and live data access. To meet production latency and accuracy needs, we use asymmetric episodic distillation where a strong teacher is improved through episodic error memories, then a smaller student is fine-tuned on the corrected trajectories with memory stripped, internalizing corrections without inference-time overhead. On a 13-task benchmark and two production applications, our fine-tuned models match or exceed their teacher, beat all larger off-the-shelf baselines, and reach 94% expert agreement on the ticket processing application.

</details>

---

### [[20_Research/Papers/具身智能/GATS_Graph-Augmented_Tree_Search_with_Layered_World_Models_for_Efficient_Agent_Planning|GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning]]

![[assets/2607.08894_first_page.png|800]]

- **arXiv**: [2607.08894](https://arxiv.org/abs/2607.08894)
- **PDF**: https://arxiv.org/pdf/2607.08894
- **详细分析**: [[20_Research/Papers/具身智能/GATS_Graph-Augmented_Tree_Search_with_Layered_World_Models_for_Efficient_Agent_Planning|GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning]]
- **作者**: Maureese Williams, Dymitr Nowicki
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 2.12（加权：大模型 0.8，强化学习 0.16，世界模型 1.16）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《GATS: Graph-Augmented Tree Search with Layered World Models for Efficient Agent Planning》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents have shown promise in multi-step planning tasks, but existing approaches like LATS (Language Agent Tree Search) and ReAct rely heavily on LLM inference during planning, leading to high computational costs and stochastic behavior. We present \textbf{GATS} (Graph-Augmented Tree Search), a planning framework that combines systematic UCB1-based tree search with a layered world model to eliminate LLM calls during inference while achieving superior planning performance. Our three-layer world model integrates: (L1) exact symbolic action matching, (L2) statistics learned from execution logs, and (L3) LLM-based prediction for unknown actions. On synthetic planning tasks with branching paths and dead-ends, GATS achieves \textbf{100\% success rate} compared to 92 % for LATS and 64\% for ReAct. On a comprehensive stress test spanning 12 challenging scenarios -- including coding workflows, web navigation, and long-horizon tasks -- GATS maintains \textbf{100\% success} while LATS drops to 88.9 % and ReAct to 23.9%. GATS requires \textbf{zero LLM calls per task} during planning (vs. 37 per task for LATS) and produces deterministic plans with zero variance across runs. Our results demonstrate that systematic search with learned world models can substantially outperform LLM-guided exploration for agent planning.

</details>

---

### [[20_Research/Papers/具身智能/Prompt-Driven_Exploration|Prompt-Driven Exploration]]

![[assets/2607.08837_figure.png|800]]

- **arXiv**: [2607.08837](https://arxiv.org/abs/2607.08837)
- **PDF**: https://arxiv.org/pdf/2607.08837
- **详细分析**: [[20_Research/Papers/具身智能/Prompt-Driven_Exploration|Prompt-Driven Exploration]]
- **作者**: Sunshine Jiang, John Marangola, David Zhang, Raghuram Kowdeed, Ruiyang Luo, Nitish Dashora, Richard Li, Pulkit Agrawal, Zhang-Wei Hong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Prompt-Driven Exploration》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoVer-VLA, LiveCodeBench, PSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exploration is essential to RL since a policy cannot improve by repeatedly sampling the behaviors it already prefers. Standard methods inject stochasticity in the action space, but such jitter only yields rollouts close to the original. Escaping a weak policy often requires global perturbations that action noise cannot produce. Large language models (LLMs) and vision-language-action (VLA) models offer a pathway: they condition the policy on a natural language prompt, and since the rollout follows from it, modifying the prompt induces global changes. The challenge is finding prompts that induce useful global changes. With a weak policy that rarely succeeds, reward is too sparse to select on. Our idea is to refine prompts from the rollouts themselves: a vision-language model (VLM) reasons over the rollout video, diagnoses how the policy responded, and rewrites the prompt to elicit better behavior next time. This procedure realizes posterior sampling, a classical RL exploration framework, at the level of prompts: the VLM maintains an implicit distribution over useful prompts and updates it from observed rollouts. We call this strategy Prompt-Driven Exploration (PDE). Across manipulation and reasoning tasks, PDE enables RL to learn successful policies even from zero-reward starts, and improves sample efficiency more broadly. Our website is available at https://xinyunsunshine.github.io/prompt-rl.

</details>

---

### [[20_Research/Papers/大模型/TheBioCollection_Unified_Pre-Training_Scale_LLM_Corpus_for_Biology|TheBioCollection: Unified Pre-Training Scale LLM Corpus for Biology]]

![[assets/2607.08803_figure.png|800]]

- **arXiv**: [2607.08803](https://arxiv.org/abs/2607.08803)
- **PDF**: https://arxiv.org/pdf/2607.08803
- **详细分析**: [[20_Research/Papers/大模型/TheBioCollection_Unified_Pre-Training_Scale_LLM_Corpus_for_Biology|TheBioCollection: Unified Pre-Training Scale LLM Corpus for Biology]]
- **作者**: Hyunjin Seo, Hyeon Hwang, Gyubok Lee, Jay Shin, Jimin Park, Taesoo Kim, Sanghoon Lee, Hongjoon Ahn, Sungjun Han, Sangwon Jung
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《TheBioCollection: Unified Pre-Training Scale LLM Corpus for Biology》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MolLangBench, ProteinLMBench, TheBioCollection-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The push toward large language models for biology (BioLM) has created a need for training corpora that can endow models with a genuine understanding of biology. However, existing biological resources, such as molecular databases, protein repositories, genomic annotations, single-cell atlases, and pathway databases, are scattered across heterogeneous formats and remain unorganized into a cohesive corpus for language model training. We present TheBioCollection, a 52.6B-token pre-training-scale corpus that converts these disparate resources into a unified, training-ready form spanning small molecules, proteins, genomic sequences, cells, and pathways. Beyond consolidating existing data, TheBioCollection enriches each record with tool-computed biological properties and introduces new instruction tasks for capabilities that current corpora barely cover. We pair the corpus with TheBioCollection-Eval, a matched suite probing recognition, generation, and prediction across molecular, protein, genomic, cellular, and cross-domain settings. Holding the base Gravity-16B-A3B architecture fixed, training on TheBioCollection more than doubles its overall score on TheBioCollection-Eval with gains in every domain, while leaving general linguistic ability nearly intact.

</details>

---

### [[20_Research/Papers/强化学习/EHR-MPC_Inference-Time_Control_for_Sepsis_Treatment_with_Generative_Patient_Digital_Twins|EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins]]

![[assets/2607.08793_figure.png|800]]

- **arXiv**: [2607.08793](https://arxiv.org/abs/2607.08793)
- **PDF**: https://arxiv.org/pdf/2607.08793
- **详细分析**: [[20_Research/Papers/强化学习/EHR-MPC_Inference-Time_Control_for_Sepsis_Treatment_with_Generative_Patient_Digital_Twins|EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins]]
- **作者**: Joshua Pickard, Wei Qi, Na Li, Ann Woolley, Lisa Cosimi, Roy Kishony, Deborah Hung
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《EHR-MPC: Inference-Time Control for Sepsis Treatment with Generative Patient Digital Twins》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sepsis is a leading cause of mortality, yet optimal treatment policies remain contested. Existing reinforcement learning (RL) approaches learn fixed strategies for sepsis treatment, limiting adaptability to changing clinical objectives during inference. We propose EHRMPC, a framework that decouples learning patient dynamics from optimizing treatment by training a patient digital twin in the form of a generative electronic health record (EHR) model. The digital twin predicts clinical trajectories under interventions and enables model predictive control (MPC) to optimize treatments via inference-time planning over simulations. We evaluate EHR-MPC on a multicenter ICU sepsis cohort spanning 8 hospitals in the Mass General Brigham health system using both off-policy importance sampling and on-policy simulation-based evaluation. Relative to RL baselines, EHR-MPC achieves comparable off-policy performance and improved simulation performance. Unlike RL, this work frames sepsis treatment optimization as inference-time control over learned patient dynamics, establishing a general framework for decision making with generative clinical models.

</details>

---

### [[20_Research/Papers/大模型/LLM-Driven_Evolutionary_Generation_of_Multi-Objective_Bayesian_Optimization_Algorithms|LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms]]

![[assets/2607.08791_figure.png|800]]

- **arXiv**: [2607.08791](https://arxiv.org/abs/2607.08791)
- **PDF**: https://arxiv.org/pdf/2607.08791
- **详细分析**: [[20_Research/Papers/大模型/LLM-Driven_Evolutionary_Generation_of_Multi-Objective_Bayesian_Optimization_Algorithms|LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms]]
- **作者**: Georgios Laskaris, Reuben Brasher, Niki van Stein, Elena Raponi, Thomas Bäck, Florian Neukart
- **cs 子类**: cs.AI, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《LLM-Driven Evolutionary Generation of Multi-Objective Bayesian Optimization Algorithms》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing effective multi-objective Bayesian optimization (MOBO) algorithms requires balancing many interdependent design choices whose optimal configuration is problem-dependent and typically demands deep expertise. We extend the LLaMEA framework to MOBO, using large language models as mutation and crossover operators within evolutionary strategies to generate complete algorithm implementations, with SMAC hyperparameter optimization integrated into the evolutionary loop. Across nine evolutionary runs we generated approximately 900 algorithms and benchmarked them on twelve synthetic problems (ZDT, DTLZ, WFG) and three real-world engineering problems (RE), using a BoFire qParEGO implementation as a state-of-the-art Bayesian-optimization baseline. On the synthetic suite the strongest generated algorithm attains the highest mean normalized hypervolume (0.971, vs. 0.869 for qParEGO) while requiring roughly 60x less wall-clock time; a Friedman test with post-hoc analysis places the two in a single top-performing group, and per-problem tests find the generated algorithm significantly better than qParEGO on 7 of the 12 problems and never worse, matching state-of-the-art accuracy at an order-of-magnitude lower cost. On the three unseen real-world engineering problems a generated algorithm attains the best mean normalized hypervolume (0.985, vs. 0.971 for qParEGO)--significantly better than qParEGO on two of the three problems--at roughly 3.4x lower wall-clock cost, confirming that the gains transfer beyond the synthetic regime. LLM-driven evolutionary search can thus discover algorithm designs that achieve Pareto-efficient trade-offs difficult to reach through manual design.

</details>

---

### [[20_Research/Papers/强化学习/Reward_Transport_Property_Control_in_Flow_Matching_via_Noise-Space_Alignment|Reward Transport: Property Control in Flow Matching via Noise-Space Alignment]]

![[assets/2607.08781_figure.png|800]]

- **arXiv**: [2607.08781](https://arxiv.org/abs/2607.08781)
- **PDF**: https://arxiv.org/pdf/2607.08781
- **详细分析**: [[20_Research/Papers/强化学习/Reward_Transport_Property_Control_in_Flow_Matching_via_Noise-Space_Alignment|Reward Transport: Property Control in Flow Matching via Noise-Space Alignment]]
- **作者**: Kehan Guo, Yili Shen, Yujun Zhou, Yue Huang, Chujie Gao, Shiyi Du, Xiangliang Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Reward Transport: Property Control in Flow Matching via Noise-Space Alignment》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The coupling in flow matching -- the rule pairing noise vectors with data points -- is typically treated as a computational choice. We show that this coupling can instead serve as an alignment interface: by matching noise and data according to a target molecular property, it embeds controllable structure directly into the learned flow field. Building on this view, we introduce Reward Transport, which uses optimal transport coupling at training time to align a scalar noise-space coordinate with molecular rewards; at inference, varying this coordinate steers the generated distribution without requiring an oracle, reward model, gradient guidance, or additional computation. In the coupling-preserving limit, thresholding this coordinate recovers the Cross-Entropy Method's truncated reward distribution, providing a principled, continuously adjustable distribution-level control knob. Empirically, on ZINC-250K and GuacaMol, sweeping the scalar induces monotone control of logP and consistent QED control over its operating range; most tellingly, the same knob produces opposite structural responses for different targets, growing molecules for logP but shrinking them for QED, which rules out a generic size bias. The interface is complementary to classifier-free guidance and conditional flow matching, while a negative result under epsilon-prediction diffusion clarifies where coupling-level alignment is structurally absent. Code: https://github.com/KehanGuo2/reward-transport

</details>

---

### [[20_Research/Papers/大模型/iLENS_Interpretable_LLM-Guided_Mixture-of-Experts_for_Neuroimaging_Survival_Analysis|iLENS: Interpretable LLM-Guided Mixture-of-Experts for Neuroimaging Survival Analysis]]

![[assets/2607.08778_figure.png|800]]

- **arXiv**: [2607.08778](https://arxiv.org/abs/2607.08778)
- **PDF**: https://arxiv.org/pdf/2607.08778
- **详细分析**: [[20_Research/Papers/大模型/iLENS_Interpretable_LLM-Guided_Mixture-of-Experts_for_Neuroimaging_Survival_Analysis|iLENS: Interpretable LLM-Guided Mixture-of-Experts for Neuroimaging Survival Analysis]]
- **作者**: Farica Zhuang, Seong Woo Han, Zixuan Wen, Shu Yang, Yize Zhao, Li Shen
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《iLENS: Interpretable LLM-Guided Mixture-of-Experts for Neuroimaging Survival Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Alzheimer's Disease (AD) is a complex neurodegenerative disorder that continues to impact millions of people worldwide. Predicting AD conversion during the prodromal stage remains critical for disease understanding and patient care. As such, survival models are widely used for AD risk prediction, yet they are typically static predictors with limited interpretability and no capacity for natural language reasoning. In this work, we propose iLENS, an interpretable large language model (LLM) guided framework based on mixture-of-experts (MoE) for survival prediction in AD conversion. Our approach uses LLM to synthesize structured neuroimaging measurements and unstructured information to guide expert routing. Our framework demonstrates competitive predictive performance and capability in patient subtyping. Furthermore, our framework provides transparent, biologically grounded rationales for its routing decisions, bridging the gap between high-performance survival analysis and interpretable clinical decision support.

</details>

---

### [[20_Research/Papers/大模型/CogniConsole_Externalizing_Inference-Time_Control_as_a_Formal_Abstraction_for_Reliable_LLM_Interactions|CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions]]

![[assets/2607.08774_figure.png|800]]

- **arXiv**: [2607.08774](https://arxiv.org/abs/2607.08774)
- **PDF**: https://arxiv.org/pdf/2607.08774
- **详细分析**: [[20_Research/Papers/大模型/CogniConsole_Externalizing_Inference-Time_Control_as_a_Formal_Abstraction_for_Reliable_LLM_Interactions|CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions]]
- **作者**: Vanessa Figueiredo, Wilter Franceschi
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《CogniConsole: Externalizing Inference-Time Control as a Formal Abstraction for Reliable LLM Interactions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliability in large language model (LLM) systems is typically framed as a function of model capability. We challenge this by demonstrating that reliability is significantly influenced by \emph{inference-time control} -- the computational layer governing task framing and context selection. We introduce \emph{CogniConsole}, an architectural instantiation that externalizes this control into a structured interface combining programmatic coordination with bounded prompt-based reasoning. Through \emph{controllability-oriented probes} ($N=489$) in a multi-step interactive environment, we show that increasing structural scaffolding -- from unstructured to fully scaffolded -- \textbf{systematically reduces output variance and failure rates under a fixed model architecture}. Our results indicate that many observed failure modes, such as context drift and inconsistent constraint adherence, arise from under-specified control rather than insufficient capability. This work provides an empirical basis for treating inference-time control as a first-class abstraction, opening new directions for designing and evaluating LLM systems beyond scaling alone.

</details>

---

### [[20_Research/Papers/大模型/SolarChain-Eval_A_Physics-Constrained_Benchmark_for_Trustworthy_Economic_Agents_in_Decentralized_Energy_Markets|SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets]]

![[assets/2607.08681_figure.png|800]]

- **arXiv**: [2607.08681](https://arxiv.org/abs/2607.08681)
- **PDF**: https://arxiv.org/pdf/2607.08681
- **详细分析**: [[20_Research/Papers/大模型/SolarChain-Eval_A_Physics-Constrained_Benchmark_for_Trustworthy_Economic_Agents_in_Decentralized_Energy_Markets|SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets]]
- **作者**: Shilin Ou, Yifan Xu, Luyao Zhang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SolarChain-Eval: A Physics-Constrained Benchmark for Trustworthy Economic Agents in Decentralized Energy Markets》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, SolarChain-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As agentic AI systems are increasingly applied to cyber-physical environments, their evaluation requires assessment of both task performance and trustworthiness. In decentralized energy markets, autonomous agents may improve market utility, but may also exploit invalid physical data, create artificial liquidity, and produce unstable governance decisions. Therefore, we propose SolarChain-Eval, a physics-constrained benchmark for evaluating trustworthy economic agents. It formulates market governance as a Gymnasium-compatible Markov Decision Process, where agents make hourly decisions. SolarChain-Eval evaluates each policy across multiple dimensions, including market utility, physical safety, slippage, action smoothness, spatial fairness, and auditability. To support agentic evaluation, SolarChain-Eval incorporates an LLM-based Planner/Auditor layer. The Planner defines episode-level action bounds and audit rules, while the Auditor reviews and revises high-risk actions. All interventions are recorded through structured logs, including trigger signals, proposed actions, revised actions, and audit rationales. Experiments with static, random, myopic, RL, and RL+LLM policies reveal a clear utility-safety trade-off. RL agents improve market utility but can still produce unsafe behavior. When the physics penalty is removed, reward-maximizing agents exploit invalid generation and increase artificial liquidity. The LLM Planner/Auditor improves auditability and mitigates selected risks, but it cannot fully compensate for a misspecified reward function. These results indicate that trustworthy agentic AI evaluation requires both physical constraints and transparent intervention traces. We release data and code as open access on GitHub for replicability.

</details>

---
