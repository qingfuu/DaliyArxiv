# cs.AI | Artificial Intelligence | 2026-05-28

#arxiv #ComputerScience

**论文数**: 32

### [[20_Research/Papers/强化学习/Beyond_Binary_Sim-to-Real_Dexterous_Manipulation_with_Physics-Grounded_Contact_Representation|Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation]]

![[assets/2605.28812_figure.png|800]]

- **arXiv**: [2605.28812](https://arxiv.org/abs/2605.28812)
- **PDF**: https://arxiv.org/pdf/2605.28812
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_Binary_Sim-to-Real_Dexterous_Manipulation_with_Physics-Grounded_Contact_Representation|Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation]]
- **作者**: Jiahe Pan, Stelian Coros, Jitendra Malik, Toru Lin
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.22（加权：具身智能 2.4，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Beyond Binary: Sim-to-Real Dexterous Manipulation with Physics-Grounded Contact Representation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A primary bottleneck in contact-rich manipulation is the difficulty of collecting real-world data. Sim-to-real reinforcement learning offers a scalable alternative, but the simulation-reality gap prevents information-dense modalities like touch from being effectively used. Existing sim-to-real methods often mitigate this gap by simplifying tactile data into coarse low-dimensional features -- sacrificing the richness required for complex manipulation. In this work, we introduce Center-of-Pressure (CoP), an effective tactile representation grounded in physical principles that preserves dense contact information while maintaining robustness for sim-to-real transfer. To support this representation, we propose a sensor calibration scheme based on differentiable dynamics, enabling the estimation of taxel orientations without requiring ground-truth force measurements. We evaluate CoP on two blind, challenging contact-rich manipulation tasks: peg-in-hole insertion and ball balancing. Across both tasks, policies conditioned on CoP achieve zero-shot sim-to-real transfer on a multi-fingered hand, and outperform both coarse binary-contact and raw-taxel baselines. Analysis of learned policy states further suggests that CoP-conditioned policies encode task-relevant physical properties, such as object mass, as an emergent byproduct of control.

</details>

---

### [[20_Research/Papers/大模型/OmniVerifier-M1_Multimodal_Meta-Verifier_with_Explicit_Structured_Recalibration|OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration]]

![[assets/2605.28805_figure.png|800]]

- **arXiv**: [2605.28805](https://arxiv.org/abs/2605.28805)
- **PDF**: https://arxiv.org/pdf/2605.28805
- **详细分析**: [[20_Research/Papers/大模型/OmniVerifier-M1_Multimodal_Meta-Verifier_with_Explicit_Structured_Recalibration|OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration]]
- **作者**: Xinchen Zhang, Bowei Liu, Jiale Liu, Chufan Shi, Yizhen Zhang, Junhong Liu, Youliang Zhang, Zhiheng Li, Yujiu Yang, Ling Yang
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.17（加权：大模型 0.65，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《OmniVerifier-M1: Multimodal Meta-Verifier with Explicit Structured Recalibration》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual outcomes are increasingly central to multimodal large language models, making reliable and fine-grained verification essential for scaling generalist foundation models. In this work, we investigate multimodal meta-verification, which leverages verifier-generated rationales rather than decision-only signals, and explore how to effectively incorporate meta-verification feedback into multimodal verifier training. We identify two key findings. First, symbolic verifier outputs (e.g., bounding boxes) outperform textual explanations as meta-verification rationales, enabling efficient rule-based reinforcement learning rewards while avoiding reliance on model-based rewards from auxiliary judge models. Second, decoupling reinforcement learning objectives for binary judgment and meta-verification substantially outperforms joint reward optimization, due to intrinsic differences in output structure and learning dynamics. Based on these insights, we train OmniVerifier-M1, a generalist visual verifier leveraging symbolic meta-verification and decoupled reinforcement learning. OmniVerifier-M1 provides robust verification and fine-grained error localization, and further enables M1-TTS, a verifier-driven agentic generation system achieving dynamic region-level self-correction. This approach paves the way for more reliable, interpretable, and fine-grained multimodal verification, supporting safer and more controllable foundation model deployment.

</details>

---

### [[20_Research/Papers/大模型/MemTrace_Tracing_and_Attributing_Errors_in_Large_Language_Model_Memory_Systems|MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems]]

![[assets/2605.28732_figure.png|800]]

- **arXiv**: [2605.28732](https://arxiv.org/abs/2605.28732)
- **PDF**: https://arxiv.org/pdf/2605.28732
- **详细分析**: [[20_Research/Papers/大模型/MemTrace_Tracing_and_Attributing_Errors_in_Large_Language_Model_Memory_Systems|MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems]]
- **作者**: Xinle Deng, Ruobin Zhong, Hujin Peng, Xiaoben Lu, Yanzhe Wu, Guang Li, Buqiang Xu, Yunzhi Yao, Jizhan Fang, Haoliang Cao, Junjie Guo, Yuan Yuan...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《MemTrace: Tracing and Attributing Errors in Large Language Model Memory Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemTraceBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory is essential for enabling large language models to support long-horizon reasoning, yet existing memory systems remain unreliable and difficult to debug. Tracing memory's dynamic evolution is crucial to understand how information is synthesized, propagated, or corrupted over time. In this work, we study the new problem of error tracing and attribution in LLM memory systems. We propose a novel framework that transforms memory pipelines into executable memory evolution graphs, enabling fine-grained tracing of operational information flow. We then construct MemTraceBench, a benchmark collected from representative memory systems such as Long-Context, RAG, Mem0, and EverMemOS, to systematically study memory failure modes. We further introduce an automatic attribution method that iteratively traces operation subgraphs to pinpoint the root cause of any failed case. Our analysis reveals that memory failures are systematic, stemming from operation-level issues like information loss and retrieval misalignment. Crucially, we leverage these fine-grained attribution signals to guide downstream prompt optimization, establishing a closed-loop system that automatically corrects faults and boosts end-task performance by up to 7.62%. Code will be released at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Adaptive_Multimodal_Agents-Based_Framework_for_Automatic_Workflow_Execution|Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution]]

![[assets/2605.28607_figure.png|800]]

- **arXiv**: [2605.28607](https://arxiv.org/abs/2605.28607)
- **PDF**: https://arxiv.org/pdf/2605.28607
- **详细分析**: [[20_Research/Papers/具身智能/Adaptive_Multimodal_Agents-Based_Framework_for_Automatic_Workflow_Execution|Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution]]
- **作者**: Susanna Cifani, Mario Luca Bernardi, Marta Cimitile
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Adaptive Multimodal Agents-Based Framework for Automatic Workflow Execution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern information systems require autonomous agents capable of navigating complex workflows, yet current methodologies often struggle with the transition from structured metadata parsing to general environmental perception. While the integration of MLLMs has enabled agents to interact directly with GUIs, existing approaches typically treat task sequences as discrete, linear episodes. This fragmentation prevents agents from capturing the underlying transition topology, limiting their effectiveness in novel or non-stationary scenarios. To address this, we propose a novel multimodal multi-agent framework that achieves automatic workflow execution through a distinct two-phase pipeline. First, during an offline discovery phase, the architecture adaptively constructs a topological knowledge base from fragmented execution logs. During inference, agents leverage Adaptive Retrieval-Augmented Generation (RAG) over this fixed, pre-established graph, coupled with a closed-loop collaborative verification protocol to dynamically self-correct and navigate. This graph-based approach facilitates superior task decomposition and adaptive navigation performance. We validate our framework in a real-world context, demonstrating its ability to maintain high reliability and semantic awareness even with limited training data.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_the_Realism_of_LLM-powered_Social_Agents_A_Case_Study_of_Reactions_to_Spanish_Online_News|Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News]]

![[assets/2605.28598_figure.png|800]]

- **arXiv**: [2605.28598](https://arxiv.org/abs/2605.28598)
- **PDF**: https://arxiv.org/pdf/2605.28598
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_the_Realism_of_LLM-powered_Social_Agents_A_Case_Study_of_Reactions_to_Spanish_Online_News|Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News]]
- **作者**: Alejandro Buitrago López, Alberto Ortega Pastor, Javier Pastor-Galindo, José A. Ruipérez-Valiente
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Evaluating the Realism of LLM-powered Social Agents: A Case Study of Reactions to Spanish Online News》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BotSim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-powered social agents are increasingly used to simulate online social behavior, yet their realism remains difficult to validate. Existing work has largely relied on general-purpose benchmarks, while less attention has been paid to short, reactive discourse such as audience replies to online news. In this paper, we evaluate whether LLM-generated reactions to Spanish online news reproduce measurable properties of real audience discourse. Using the Hatemedia dataset, we pair 5,631 news items with 58,555 real audience reactions, and generate a matched synthetic dataset using five LLMs under a shared experimental setting. We compare real and synthetic reactions across three dimensions: hate speech, sentiment, and semantic alignment, considering both off-the-shelf and fine-tuned generation. Results show that off-the-shelf models are poor proxies for real audience reactions: they strongly underproduce hate speech, introduce model-specific sentiment biases, and remain distributionally distant from human replies. Fine-tuning improves fidelity unevenly. Qwen3 provides the most balanced approximation, while Mistral7B achieves the strongest sentiment and semantic alignment but overshoots hate prevalence. Plausible synthetic replies do not necessarily reproduce the distributional properties of public discourse.

</details>

---

### [[20_Research/Papers/大模型/SARAD_LLM-Based_Safety-Aware_Hybrid_Reinforcement_Learning_with_Collision_Prediction_for_Autonomous_Driving|SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving]]

![[assets/2605.28583_figure.png|800]]

- **arXiv**: [2605.28583](https://arxiv.org/abs/2605.28583)
- **PDF**: https://arxiv.org/pdf/2605.28583
- **详细分析**: [[20_Research/Papers/大模型/SARAD_LLM-Based_Safety-Aware_Hybrid_Reinforcement_Learning_with_Collision_Prediction_for_Autonomous_Driving|SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving]]
- **作者**: Kangyu Wu, Peng Cui, Guoxi Chen, Ya Zhang
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 2.12（加权：大模型 0.6，强化学习 1.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《SARAD: LLM-Based Safety-Aware Hybrid Reinforcement Learning with Collision Prediction for Autonomous Driving》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, IRL, LGDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ensuring both safety and efficiency in decision-making for autonomous driving systems remains a fundamental challenge. Traditional Deep Reinforcement Learning (DRL) suffers from unsafe random exploration and slow convergence, while Large Language Models (LLMs) demonstrate inherent latency in real-time inference operations. To address these limitations, this paper proposes SARAD, a novel safety-aware hybrid framework that synergizes LLMs and DRL for autonomous driving. SARAD substitutes the random exploration of DRL with Retrieval-Augmented Generation (RAG)-enhanced, LLM-guided decisions sourced from a dynamic expert knowledge repository. An attention discriminator is proposed to integrate the prior knowledge of LLMs into DRL policy optimization. A collision predictor module, fine-tuned with historical collision data, is further designed to improve vehicle safety. Extensive experiments show that SARAD achieves significant performance improvements in the Highway-Env simulator, validating the effectiveness of the proposed model in autonomous driving.

</details>

---

### [[20_Research/Papers/强化学习/Modeling_Vehicle-Type-Specific_Pedestrian_Crash_Avoidance_Behavior_in_Safety-Critical_Interactions_Using_Smooth-Mamba_Deep_Reinforcement_Lea|Modeling Vehicle-Type-Specific Pedestrian Crash Avoidance Behavior in Safety-Critical Interactions Using Smooth-Mamba Deep Reinforcement Learning]]

![[assets/2605.28552_first_page.png|800]]

- **arXiv**: [2605.28552](https://arxiv.org/abs/2605.28552)
- **PDF**: https://arxiv.org/pdf/2605.28552
- **详细分析**: [[20_Research/Papers/强化学习/Modeling_Vehicle-Type-Specific_Pedestrian_Crash_Avoidance_Behavior_in_Safety-Critical_Interactions_Using_Smooth-Mamba_Deep_Reinforcement_Lea|Modeling Vehicle-Type-Specific Pedestrian Crash Avoidance Behavior in Safety-Critical Interactions Using Smooth-Mamba Deep Reinforcement Learning]]
- **作者**: Qingwen Pu, Kun Xie, Hong Yang, Di Yang, Junqing Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Modeling Vehicle-Type-Specific Pedestrian Crash Avoidance Behavior in Safety-Critical Interactions Using Smooth-Mamba Deep Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As automated vehicles (AVs) increasingly share roadways with human-driven vehicles (HDVs), understanding how pedestrians respond to different vehicle types in safety-critical interactions is essential for the safe deployment of automated driving technologies. This study extracts safety-critical pedestrian-vehicle interactions from the Argoverse 2 dataset to capture real-world crash avoidance behaviors in encounters involving AVs and HDVs. To model vehicle-type-specific pedestrian crash avoidance behavior, we develop a Smooth-Mamba Deep Deterministic Policy Gradient framework, termed SMamba-DDPG, which integrates smooth action constraints with efficient temporal representation learning. To quantify pedestrian behavioral differences, the framework trains separate crash avoidance policies for pedestrian interactions with AVs and HDVs. Results show that SMamba-DDPG outperforms baseline reinforcement learning and supervised learning models in reproducing pedestrian crash avoidance behaviors. Reconstructed trajectories demonstrate strong behavioral realism, accurately reproducing crash avoidance kinematics in both AV and HDV scenarios. Reaction time analysis shows that the model captures human-like response delays and reveals that pedestrians respond more quickly to AVs than to HDVs. Counterfactual analysis further indicates that pedestrians adopt lower crossing speeds when interacting with AVs. Large-scale safety analysis of model-generated data revealed that pedestrian-AV interactions consistently yielded lower conflict rates and higher pedestrian yielding rates compared to pedestrian-HDV interactions. The findings highlight the importance of incorporating vehicle-type-specific pedestrian behavioral models for safer automated driving system design and more realistic traffic simulations in mixed-traffic environments.

</details>

---

### [[20_Research/Papers/大模型/Efficient_Post-training_of_LLMs_for_Code_Generation_With_Offline_Reinforcement_Learning|Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning]]

![[assets/2605.28409_figure.png|800]]

- **arXiv**: [2605.28409](https://arxiv.org/abs/2605.28409)
- **PDF**: https://arxiv.org/pdf/2605.28409
- **详细分析**: [[20_Research/Papers/大模型/Efficient_Post-training_of_LLMs_for_Code_Generation_With_Offline_Reinforcement_Learning|Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning]]
- **作者**: Mingze Wu, Abhinav Anand, Shweta Verma, Mira Mezini
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Efficient Post-training of LLMs for Code Generation With Offline Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CodeNet, CodeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training using online reinforcement learning (RL) is an important training step for LLMs, including code-generating models. However, online RL for code generation involves LLM inference and verification of the generated output, which can take considerable time and resources. In this paper, we explore the application of offline RL to code-generating models by leveraging existing code datasets. Our experiments demonstrate that offline RL is an effective training strategy for improving LLM performance. We show that offline RL can be especially beneficial for small LLMs and challenging coding problems.

</details>

---

### [[20_Research/Papers/大模型/From_Knowing_to_Doing_A_Memory-Controlled_Benchmark_for_LLM_Trading_Agents_on_Stock_Markets|From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets]]

![[assets/2605.28359_figure.png|800]]

- **arXiv**: [2605.28359](https://arxiv.org/abs/2605.28359)
- **PDF**: https://arxiv.org/pdf/2605.28359
- **详细分析**: [[20_Research/Papers/大模型/From_Knowing_to_Doing_A_Memory-Controlled_Benchmark_for_LLM_Trading_Agents_on_Stock_Markets|From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets]]
- **作者**: Taojie Zhu, Wentao Zhao, Rui Sun, Beidi Luan, Jiacheng Lu, Sinuo Wang, Jing Li, Daxin Jiang, Yonghong He, Zuo Bai
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Knowing to Doing: A Memory-Controlled Benchmark for LLM Trading Agents on Stock Markets》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, ConvFinQA, FinEval, FinQA, FinRL, FinanceBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating whether large language model (LLM) agents can profit in capital markets is increasingly framed as end-to-end trading: place an agent in a historical market, let it trade, and measure portfolio returns. This setup is vulnerable to two evaluation failures. First, long backtests often overlap with the knowledge cutoffs of frontier LLMs, allowing memorized tickers, dates, prices, and market narratives to substitute for investment reasoning. Second, raw returns are a noisy proxy for stock-selection ability, since positive performance may come from market beta, style exposure, or favorable regimes rather than genuine alpha. We introduce KTD-Fin (Knowing-To-Doing Financial Benchmark), an end-to-end stock-market trading benchmark that addresses both issues. KTD-Fin uses a data-side masking protocol to anonymize key identifiers and calendar information consistently across prompts and tools, separating historical market memory from investment decision-making. It also incorporates a Barra-style performance attribution framework that decomposes portfolio returns into market, style, and stock-selection alpha components. Across ten frontier LLM agents evaluated on the Chinese CSI300 over a 2024--2026 window, masking substantially changes agent rationales, pushing them towards anonymized factor-based reasoning. Attribution analysis further shows that LLM agents' cumulative returns under leakage-controlled evaluation are largely explained by passive market and style exposure, with limited evidence of persistent stock-selection alpha. These findings suggest that financial LLM benchmarks should evaluate not only whether an agent makes money, but also whether the source of returns reflects transferable investment skill. We release KTD-Fin as a reproducible template for leakage-controlled and attribution-aware evaluation of LLM trading agents.

</details>

---

### [[20_Research/Papers/世界模型/Hybrid_Neural_World_Models|Hybrid Neural World Models]]

![[assets/2605.28317_figure.png|800]]

- **arXiv**: [2605.28317](https://arxiv.org/abs/2605.28317)
- **PDF**: https://arxiv.org/pdf/2605.28317
- **详细分析**: [[20_Research/Papers/世界模型/Hybrid_Neural_World_Models|Hybrid Neural World Models]]
- **作者**: Pranav Lakshmanan, Paras Chopra
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Systems

#### 研究背景与动机

《Hybrid Neural World Models》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeepONet, PDEBench, TI-DeepONet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Neural surrogates promise large speedups over classical solvers for physical dynamics but fail silently at sharp dynamical events such as shocks, fronts, and contact. We present hybrid neural world models for physical dynamics: a recipe for training and deploying multi-horizon surrogates in physical state space, where a single network with continuous horizon conditioning is trained with direct supervision against textbook reference solvers to predict any future state at horizon T in one forward pass. Although no part of the training data, loss function, or architecture supervises discontinuity location, the trained surrogate encodes it implicitly, recoverable from its forward passes alone as a per-trajectory error map that concentrates on shocks, fronts, and contacts, and stays small elsewhere. The map is competitive with or better than standard label-free baselines including deep ensembles, learned error heads, gradient-magnitude indicators, and locally-adaptive conformal prediction, while using only a single trained network and requiring no calibration set or governing-equation knowledge. The recipe supports two operating points. Mode 1 runs the surrogate alone for maximum throughput, with same-hardware CPU speedups of 26x to 72x against textbook solvers on the PDE environments. Mode 2 uses the error map to gate a reference-solver fallback, deferring uncertain trajectories and roughly halving the surrogate's residual error at the default operating point. The recipe applies without modification across reaction-diffusion, compressible Euler, and rigid-body collision dynamics.

</details>

---

### [[20_Research/Papers/强化学习/ProRL_Effective_Reinforcement_Learning_for_Proactive_Recommendation_via_Rectified_Policy_Gradient_Estimation|ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified Policy Gradient Estimation]]

![[assets/2605.28293_figure.png|800]]

- **arXiv**: [2605.28293](https://arxiv.org/abs/2605.28293)
- **PDF**: https://arxiv.org/pdf/2605.28293
- **详细分析**: [[20_Research/Papers/强化学习/ProRL_Effective_Reinforcement_Learning_for_Proactive_Recommendation_via_Rectified_Policy_Gradient_Estimation|ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified Policy Gradient Estimation]]
- **作者**: Hongru Hou, Tiehua Mei, Denghui Geng, Jinhui Huang, Ao Xu, Hengrui Chen, Jiaqing Liang, Deqing Yang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.72（加权：强化学习 1.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified Policy Gradient Estimation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ProRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Proactive Recommender Systems (PRSs) aim to guide user preference shift toward target items by generating paths of intermediate recommendations. Reinforcement learning (RL) provides a principled framework for optimizing such sequential decision tasks, as path rewards can naturally capture both short-term acceptance and long-term guidance effectiveness. However, naively applying policy gradients to PRS results in deficient gradient estimation. We identify two deficiencies: (1) path-level rewards decompose into step-level rewards with positive mean, creating a length-dependent bias that causes gradients to favor path extension over meaningful exploration; (2) weighting each step by the entire path-level reward ignores the decomposition structure, leading to high gradient variance. To rectify these two deficiencies, we propose an effective RL framework ProRL with two novel mechanisms for proactive recommendation. First, Stepwise Reward Centering subtracts expected rewards to neutralize length-dependent bias, ensuring that path extension yields zero expected gradient signal. Second, Position-Specific Advantage Estimation leverages the reward decomposition structure to compute step-dependent baselines, reducing gradient variance. Together, these mechanisms yield policy gradients that precisely target path quality. Our experiments on three real-world datasets demonstrate that ProRL significantly outperforms state-of-the-art PRSs. Our code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Do_LLMs_Build_World_Models_From_Text_A_Multilingual_Diagnostic_of_Spatial_Reasoning|Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning]]

![[assets/2605.28277_figure.png|800]]

- **arXiv**: [2605.28277](https://arxiv.org/abs/2605.28277)
- **PDF**: https://arxiv.org/pdf/2605.28277
- **详细分析**: [[20_Research/Papers/大模型/Do_LLMs_Build_World_Models_From_Text_A_Multilingual_Diagnostic_of_Spatial_Reasoning|Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning]]
- **作者**: Zhikai Pan, Chih-Ting Liao, Chunrui Liu, Xi Xiao, Yitong Qiao, Chunlei Meng, Zhangquan Chen, Xin Cao
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，世界模型 0.8）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Do LLMs Build World Models From Text? A Multilingual Diagnostic of Spatial Reasoning》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FloorplanQA, LLM-BabyBench, MazeEval, OptimalThinkingBench, SiT-Bench, Sys2Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whether large language models (LLMs) construct internal spatial world models from pure-text descriptions remains contested, and whether such capabilities transfer across languages has not been systematically studied. We introduce MentalMap, a multilingual diagnostic benchmark with a six-level capability hierarchy (L0-L5) spanning atomic spatial facts to generative world-graph construction, together with four diagnostic axes probing frame of reference, reading-direction bias, reasoning-effort allocation, and hallucination. MentalMap is built from 100 ProcTHOR household scenes, covers eight typologically diverse languages plus a structured-text control, and contains 39 task families across 1,950 evaluation cells. Evaluating thirteen LLMs across scales and model families, we identify a universal L3 reasoning cliff: no model retains even half of its L0 performance on viewpoint reasoning once baseline atomic accuracy exceeds 40%. The cliff persists across languages, scales, and prompting strategies, while structured-output failures and reasoning patterns vary substantially across models. Human evaluation under the identical pure-text protocol reproduces the same failure pattern, suggesting that the bottleneck arises from text-only working memory constraints rather than being specific to current LLM architectures. Our findings reframe pure-text spatial reasoning as a multi-axis world-modeling problem and motivate multimodal and scratchpad-augmented reasoning as future directions.

</details>

---

### [[20_Research/Papers/大模型/Plant,_Persist,_Trigger_Sleeper_Attack_on_Large_Language_Model_Agents|Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents]]

![[assets/2605.28201_figure.png|800]]

- **arXiv**: [2605.28201](https://arxiv.org/abs/2605.28201)
- **PDF**: https://arxiv.org/pdf/2605.28201
- **详细分析**: [[20_Research/Papers/大模型/Plant,_Persist,_Trigger_Sleeper_Attack_on_Large_Language_Model_Agents|Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents]]
- **作者**: Yongxiang Li, Moxin Li, Zhixin Ma, Fengbin Zhu, Dongrui Liu, Wenjie Wang, Fuli Feng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Plant, Persist, Trigger: Sleeper Attack on Large Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents remain vulnerable to safety threats from the external environment, where attackers inject adversarial content into external observations such as tool-returned data, webpages, or MCP context, causing harmful agentic behaviors such as unsafe actions or incorrect outputs. Existing studies typically focus on single-interaction attacks, where the agent observes adversarial content and immediately exhibits harmful behavior within one user request. However, we show that adversarial content can also persist across interactions served by the same agent, making such threats harder to detect and mitigate. Specifically, adversarial content may persist in the agent state, remain dormant across interactions, and later be activated by a benign user query. We formalize this type of safety threat as Sleeper Attack. To evaluate it, we construct a benchmark with 1,896 instances covering six real-world harmful outcomes, three attack strategies, and three agent state targets: session context, memory, and reusable skills. Experiments on seven strong open-source and closed-source LLMs show that state-of-the-art LLM agents remain vulnerable to Sleeper Attack, even when they achieve low attack success rates under a single-interaction baseline. Our code and data are available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Visualizing_Latent_Phase_Structures_in_Locomotion_Policies_A_Multi-Environment_Study_with_Temporal_Feature_Extension|Visualizing Latent Phase Structures in Locomotion Policies: A Multi-Environment Study with Temporal Feature Extension]]

![[assets/2605.28186_figure.png|800]]

- **arXiv**: [2605.28186](https://arxiv.org/abs/2605.28186)
- **PDF**: https://arxiv.org/pdf/2605.28186
- **详细分析**: [[20_Research/Papers/具身智能/Visualizing_Latent_Phase_Structures_in_Locomotion_Policies_A_Multi-Environment_Study_with_Temporal_Feature_Extension|Visualizing Latent Phase Structures in Locomotion Policies: A Multi-Environment Study with Temporal Feature Extension]]
- **作者**: Daisuke Yasui, Toshitaka Matuki, Hiroshi Sato
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.4，机器人 0.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Visualizing Latent Phase Structures in Locomotion Policies: A Multi-Environment Study with Temporal Feature Extension》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) has been shown to achieve high performance on locomotion control tasks in MuJoCo benchmarks such as HalfCheetah, Ant, and Walker2D. However, visualizing the motion structures internally obtained by a trained policy function implemented as a deep neural network remains challenging. It is known from biomechanics and related fields that locomotion control is realized through the repetition of motion phases such as the stance phase and swing phase. In this study, we propose a framework for uncovering latent motion phase structures from trajectories generated by locomotion control policies through interaction with the environment. The proposed method extends the clustering features from state observations alone to augmented features including actions, next states, and next actions, and introduces a method for determining the number of clusters that suppresses self-transitions. Applying the proposed method to three environments -- Ant-v5, HalfCheetah-v5, and Walker2D-v5 -- we successfully identified phase structures with clearer and more regular transition rules than those obtained by the existing method.

</details>

---

### [[20_Research/Papers/大模型/FLORO_A_Multimodal_Geospatial_Foundation_Model_for_Ecological_Remote_Sensing_Across_Sensors_and_Scales|FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales]]

![[assets/2605.28174_figure.png|800]]

- **arXiv**: [2605.28174](https://arxiv.org/abs/2605.28174)
- **PDF**: https://arxiv.org/pdf/2605.28174
- **详细分析**: [[20_Research/Papers/大模型/FLORO_A_Multimodal_Geospatial_Foundation_Model_for_Ecological_Remote_Sensing_Across_Sensors_and_Scales|FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales]]
- **作者**: Jorge L. Rodriguez, Victor Angulo Morales, Areej Alwahas, Mariana Elias Lara, Fida Mohammad Thoker, Kasper Johansen, Bernard Ghanem, Fernando T. Maestre, Matthew F. McCabe
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.0（加权：大模型 0.8，机器人 0.2）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《FLORO: A Multimodal Geospatial Foundation Model for Ecological Remote Sensing Across Sensors and Scales》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models offer a promising route to transferable remote sensing representations, but many current approaches depend on very large pretraining datasets and fixed sensor configurations, limiting their suitability for ecological and environmental applications, where observations often vary across platforms, spatial and spectral resolutions, and available modalities. We introduce FLORO, a multimodal geospatial foundation model designed to learn transferable representations from a small but highly diverse remote sensing corpus. FLORO is pretrained using masked autoencoding on a heterogeneous combination of Sentinel-1, Sentinel-2, SkySAT imagery, elevation, and UAV-derived data. To accommodate sensor variability, FLORO incorporates availability-aware inputs that indicate which spectral bands and auxiliary modalities are present in each sample, enabling a unified input space across heterogeneous sensor configurations. We evaluated FLORO on the PANGAEA benchmark under a frozen-encoder protocol across scene classification, segmentation, and regression tasks. Despite being pretrained on a smaller corpus than competing foundation models, FLORO achieved strong and stable transfer across optical, optical-SAR, and optical-elevation benchmarks spanning medium-resolution satellite, airborne, and ultra-high-resolution UAV imagery. FLORO obtained the second-best average segmentation performance across six PANGAEA benchmarks, trailing only a recently introduced foundation model pretrained on over two orders of magnitude more images, remained competitive on scene classification, and was robust in regression tasks, while qualitative results showed improved preservation of spatial structure in flood, urban, biomass, and canopy-height prediction settings. In a separate controlled experiment on EuroSAT-MS, geo-positional encoding further improved classification relative to absolute positional encoding.

</details>

---

### [[20_Research/Papers/大模型/OccuReward_LLM-Guided_Occupant-Centric_Reward_Shaping_for_Demographic_Equity_in_Grid-Interactive_Buildings|OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings]]

![[assets/2605.28168_figure.png|800]]

- **arXiv**: [2605.28168](https://arxiv.org/abs/2605.28168)
- **PDF**: https://arxiv.org/pdf/2605.28168
- **详细分析**: [[20_Research/Papers/大模型/OccuReward_LLM-Guided_Occupant-Centric_Reward_Shaping_for_Demographic_Equity_in_Grid-Interactive_Buildings|OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings]]
- **作者**: Shadmehr Zaregarizi, Khashayar Yavari
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.2（加权：大模型 0.6，强化学习 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《OccuReward: LLM-Guided Occupant-Centric Reward Shaping for Demographic Equity in Grid-Interactive Buildings》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have demonstrated promising capability in generating reward functions for deep reinforcement learning (DRL)-based building energy management. However, their potential to exhibit or exacerbate disparities in occupant comfort across heterogeneous demographic populations remains unexplored. We present OccuReward, a framework investigating how LLM-mediated reward design affects demographic equity. Our contribution is three-fold: the introduction of the Comfort Equity Index (CEI) as a novel feedback signal; a methodology for iterative, equity-aware LLM reward shaping; and a performance analysis of DRL agents under these refined objectives. Utilizing four empirically grounded occupant profiles from the ASHRAE Global Thermal Comfort Database II (13,440 votes), we deploy a Soft Actor-Critic agent in CityLearn v2. Our approach employs the Gemini API to generate reward function logic and weights--rather than performing per-step inference--across three refinement rounds. Results across 15 experimental runs reveal that elderly female occupants consistently experience the lowest satisfaction in initial rounds. By Round 3, equity-aware LLM refinement activates specific reward components that improve satisfaction for Young Males (+17.6%), Mid-aged Females (+28.2%), Health Sensitive (+53.8%), and Elderly Females (+567%), while simultaneously reducing energy costs by 3.2%. Our findings highlight that while reward-level intervention significantly improves equity, demographic disparities in AI-driven controllers persist, necessitating further research into algorithmic fairness in building systems.

</details>

---

### [[20_Research/Papers/具身智能/Deconstructing_Spatial_Complexity_Hierarchical_Decomposition_for_LLM_Spatial_Reasoning|Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning]]

![[assets/2605.28144_figure.png|800]]

- **arXiv**: [2605.28144](https://arxiv.org/abs/2605.28144)
- **PDF**: https://arxiv.org/pdf/2605.28144
- **详细分析**: [[20_Research/Papers/具身智能/Deconstructing_Spatial_Complexity_Hierarchical_Decomposition_for_LLM_Spatial_Reasoning|Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning]]
- **作者**: Yi Wang, Haojie Lu, Zhaofan Zhang, Li Chen, Sihong Xie
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 具身智能, 机器人
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.4，强化学习 0.4，机器人 0.2）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Deconstructing Spatial Complexity: Hierarchical Decomposition for LLM Spatial Reasoning》归入 大模型、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HSRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs have shown remarkable proficiency in general language understanding and reasoning. However, they consistently underperform in spatial reasoning that severely limits their application, particularly in embodied intelligence. Inspired by the success of hierarchical reinforcement learning, this paper introduces a novel method for hierarchical task decomposition in LLM spatial reasoning. Our approach guides LLMs to decompose complex tasks into manageable sub-tasks by identifying key intermediate states and generating simplified sub-environments. However, we identify that LLMs often fail to derive optimal intermediate states due to their insufficient spatial prior, leading to sub-optimal task decomposition. To address this limitation and enhance its planning capability, we propose the MCTS-Guided Group Relative Policy Optimization (M-GRPO), where we reformulate the UCT formula by incorporating the LLM's prior predictive probabilities alongside its epistemic uncertainty. Furthermore, we implement a more fine-grained advantage function, enabling the model to learn optimal path planning. Experimental results demonstrate that our method substantially improves LLM performance on spatial tasks, including navigation, planning, and strategic games, achieving state-of-the-art results. This work paves the way for LLMs in real-world applications.

</details>

---

### [[20_Research/Papers/大模型/LegalGraphRAG_Multi-Agent_Graph_Retrieval-Augmented_Generation_for_Reliable_Legal_Reasoning|LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning]]

![[assets/2605.28120_figure.png|800]]

- **arXiv**: [2605.28120](https://arxiv.org/abs/2605.28120)
- **PDF**: https://arxiv.org/pdf/2605.28120
- **详细分析**: [[20_Research/Papers/大模型/LegalGraphRAG_Multi-Agent_Graph_Retrieval-Augmented_Generation_for_Reliable_Legal_Reasoning|LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning]]
- **作者**: Zerui Chen, Qinggang Zhang, Zhishang Xiang, Zhimin Wei, Linfeng Gao, Xiao Huang, Zhihong Zhang, Jinsong Su
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《LegalGraphRAG: Multi-Agent Graph Retrieval-Augmented Generation for Reliable Legal Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Graph-based Retrieval-Augmented Generation (GraphRAG) advances flat document retrieval by structuring knowledge as relational graphs, enabling more coherent and effective reasoning. However, applying it to specific domains like legal reasoning faces critical challenges. (i) Legal corpora are heterogeneous, containing multi-granular knowledge from cases, articles and interpretations. A flat knowledge graph cannot adequately differentiate between factual details, applied rules, and abstract principles, limiting accurate retrieval. (ii) Reliable legal judgment demands transparent, evidence-based reasoning. Traditional RAG passes retrieved context directly to an LLM without verification, resulting in opaque, error-prone reasoning. To this end, we propose LegalGraphRAG, a framework designed for reliable legal reasoning. Our approach introduces two core components: a hierarchical legal graph that hierarchically organizes legal sources to enable retrieval at appropriate abstraction levels, and a multi-agent system for reliable legal reasoning, where a Researcher retrieves candidate evidence, an Auditor rigorously verifies its validity against source documents, and an Adjudicator synthesizes the set of verified evidence to render a final judgment. Extensive experiments show that LegalGraphRAG achieves the state-of-the-art performance, outperforming existing GraphRAG baselines in accurate and trustworthy legal analysis. Our code, datasets and implementation details are available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Defending_LLM-based_Multi-Agent_Systems_Against_Cooperative_Attacks_with_Sentence-Level_Rectification|Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification]]

![[assets/2605.28104_figure.png|800]]

- **arXiv**: [2605.28104](https://arxiv.org/abs/2605.28104)
- **PDF**: https://arxiv.org/pdf/2605.28104
- **详细分析**: [[20_Research/Papers/大模型/Defending_LLM-based_Multi-Agent_Systems_Against_Cooperative_Attacks_with_Sentence-Level_Rectification|Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification]]
- **作者**: Yaoyang Luo, Zhi Zheng, Ziwei Zhao, Tong Xu, Zhao Jielun, Wenjun Xue, Yong Chen, Enhong Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Defending LLM-based Multi-Agent Systems Against Cooperative Attacks with Sentence-Level Rectification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CSQA, LogiQA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent years have witnessed the rapid development of Large Language Model-based Multi-Agent Systems (MAS), which excel at collaborative decision-making and complex problem-solving. However, malicious agents in MAS may inject misinformation to mislead other agents and disrupt system performance, giving rise to a new research direction that focuses on attack mechanisms and defense strategies in MAS. Prior studies largely assume malicious agents act independently and investigate the corresponding defense strategies. However, we argue that malicious agents may exhibit collaborative behaviors, enabling more effective attacks through internal information exchange. In this paper, we propose an adaptive cooperative attack framework, where malicious agents autonomously coordinate and dynamically adjust their attack strategies through multi-round interactions. Furthermore, we introduce Sentence-Level Trustworthiness Analysis and Rectification (STAR), a defense framework that identifies and rectifies misleading information at the sentence level within agent communications. Our experiments show that cooperative attacks lead to a significantly larger degradation in task success rate than independent attacks, resulting in a relative drop of 5.34\%. Meanwhile, STAR effectively mitigates both cooperative and independent threats and improves task success rate by an average of 36.76\%. The code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/PromptEmbedder_Efficient_and_Transferable_Text_Embedding_via_Dual-LLM_Soft_Prompting|PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting]]

![[assets/2605.28066_figure.png|800]]

- **arXiv**: [2605.28066](https://arxiv.org/abs/2605.28066)
- **PDF**: https://arxiv.org/pdf/2605.28066
- **详细分析**: [[20_Research/Papers/大模型/PromptEmbedder_Efficient_and_Transferable_Text_Embedding_via_Dual-LLM_Soft_Prompting|PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting]]
- **作者**: Yu-Che Tsai, Kuan-Yu Chen, Yuan-Hao Chen, Yu-Han Chang, Ching-Yu Tsai, Yu-Hsiang Chuang, Shou-De Lin
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM

#### 研究背景与动机

《PromptEmbedder:: Efficient and Transferable Text Embedding via Dual-LLM Soft Prompting》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) have demonstrated remarkable efficacy in text embedding, yet current adaptation methods like LoRA face significant bottlenecks in computational efficiency and cross-architecture transferability. Whenever a new backbone emerges, existing approaches require costly retraining from scratch. To address this, we propose PromptEmbedder, a novel dual-LLM framework that decouples embedding knowledge from specific backbone weights. PromptEmbedder utilizes a Prompting LLM to generate instruction-aware soft prompts for a frozen Embedding LLM via a differentiable generation process with continuous relaxation, ensuring full gradient flow during contrastive training. By localizing task-specific knowledge within the Prompting LLM, adapting to new architectures requires only retraining a lightweight linear alignment matrix. Evaluations on the MTEB benchmark show that PromptEmbedder achieves comparable performance with LoRA finetuning while reducing GPU memory by 40% and accelerating training by 3.7x. Our approach establishes a scalable, architecture-agnostic paradigm for efficient LLM-based representation learning.

</details>

---

### [[20_Research/Papers/强化学习/EAPO_Entropy-Driven_Adaptive_Positive-Negative_Sample_Weighting_for_Policy_Optimization_in_Open-Ended_QA|EAPO: Entropy-Driven Adaptive Positive-Negative Sample Weighting for Policy Optimization in Open-Ended QA]]

![[assets/2605.27846_first_page.png|800]]

- **arXiv**: [2605.27846](https://arxiv.org/abs/2605.27846)
- **PDF**: https://arxiv.org/pdf/2605.27846
- **详细分析**: [[20_Research/Papers/强化学习/EAPO_Entropy-Driven_Adaptive_Positive-Negative_Sample_Weighting_for_Policy_Optimization_in_Open-Ended_QA|EAPO: Entropy-Driven Adaptive Positive-Negative Sample Weighting for Policy Optimization in Open-Ended QA]]
- **作者**: Yunsheng Zeng, Gen Li, Yuwei Miao, Xiandong Li, Yujin Wang, Siyu Chen, Luning Wang, Yunhao Qiao, Junfeng Wang, Jianwei Lv, Bo Yuan
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《EAPO: Entropy-Driven Adaptive Positive-Negative Sample Weighting for Policy Optimization in Open-Ended QA》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Reasoning Models are typically trained via reinforcement learning from verifiable rewards (RLVR). However, existing approaches adopt fixed weights for positive and negative samples, and the conclusions hardly generalize to open-ended question answering (QA). In this paper, we systematically investigate the roles of positive and negative samples in reinforcement learning for open-ended QA. We propose a reward-mean-based strategy for distinguishing positive from negative samples, and observe that negative samples predominantly govern response diversity and the performance upper bound, whereas positive samples primarily determine response quality and convergence stability. Building on these observations, we propose EAPO, an Entropy-driven Adaptive Policy Optimization method that adaptively computes the weighting coefficients of positive samples based on the ratio of the current policy entropy to the initial entropy. During the entropy-decreasing phase, the weight assigned to positive samples is reduced to preserve exploration, whereas during the entropy-increasing phase it is amplified to reinforce stability, thereby mitigating entropy collapse. Experiments on two publicly available open-ended medical QA datasets demonstrate that EAPO consistently and substantially outperforms fixed-weight baselines in both response diversity and stability.

</details>

---

### [[20_Research/Papers/大模型/EgoBench_An_Interactive_Egocentric_Multimodal_Benchmark_for_Tool-Using_Agents|EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents]]

![[assets/2605.27820_figure.png|800]]

- **arXiv**: [2605.27820](https://arxiv.org/abs/2605.27820)
- **PDF**: https://arxiv.org/pdf/2605.27820
- **详细分析**: [[20_Research/Papers/大模型/EgoBench_An_Interactive_Egocentric_Multimodal_Benchmark_for_Tool-Using_Agents|EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents]]
- **作者**: Yunqi Liu, Tong Niu, Zitong Wang, Zhenlong Dai, Yuqi Qing, Weiqiang Wang, Jian Liu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《EgoBench: An Interactive Egocentric Multimodal Benchmark for Tool-Using Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ACEBench, AgencyBench, AgentBench, ComplexFuncBench, EgoBench, MCP-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As AI agents increasingly operate in open, real-world environments, they require a deep synergy of multimodal perception, tool invocation with multi-hop reasoning, and dynamic interaction with users. However, existing benchmarks fail to jointly evaluate these capabilities due to challenges in designing strictly coupled multi-capability tasks, simulating natural and task-constrained user feedback, and ensuring objective evaluation of dynamic interaction. To bridge this gap, we introduce EgoBench, the first interactive multimodal benchmark for tool-using agents. EgoBench comprises 1,045 egocentric-video-grounded tasks covering four daily scenarios, along with a user-agent-tool interactive environment for evaluation. We implement a three-stage synergistic pipeline through which each task is designed to enforce the joint application of visual perception and tool-augmented multi-hop reasoning. We additionally develop a multi-agent simulated user within EgoBench to evaluate agents' interaction capabilities, which generates high-fidelity, task-aligned responses to agents. Furthermore, we establish a deterministic joint validation framework that guarantees objective assessment through process-based and result-based equivalence. Benchmarking eight SOTA video-MLLM agents on EgoBench reveals a severe performance ceiling: the best model achieves only 30.62% accuracy in the best-performing scenario, averaging 19.43% across all four scenarios. Finally, we conduct a multi-dimensional error analysis to disentangle failure modes, exposing capability bottlenecks for advancing future AI agents.

</details>

---

### [[20_Research/Papers/具身智能/Turning_Video_Models_into_Generalist_Robot_Policies|Turning Video Models into Generalist Robot Policies]]

![[assets/2605.27817_figure.png|800]]

- **arXiv**: [2605.27817](https://arxiv.org/abs/2605.27817)
- **PDF**: https://arxiv.org/pdf/2605.27817
- **详细分析**: [[20_Research/Papers/具身智能/Turning_Video_Models_into_Generalist_Robot_Policies|Turning Video Models into Generalist Robot Policies]]
- **作者**: Sizhe Lester Li, Evan Kim, Xingjian Bai, Tong Zhao, Tao Pang, Max Simchowitz, Vincent Sitzmann
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 强化学习
- **相关性评分**: 2.92（加权：具身智能 0.9，强化学习 0.16，世界模型 0.56，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Turning Video Models into Generalist Robot Policies》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Allegro-Sim, OpenVLA, Panda-Sim, PushT-Sim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generative models have emerged as a promising robotics backbone, capable of generating videos that depict the completion of complex tasks across embodiments and environments. Recent work proposes robot foundation models that jointly predict future observations and actions by finetuning video models with action-labeled data. In this paper, we test the limits of an alternative approach: leave the video planner as-is while training an embodiment-specific inverse dynamics model (IDM). This decoupling offers several natural benefits: the video planner remains embodiment-agnostic, different video models can be interchanged easily without re-training the IDM, and the IDM can be independently trained with readily available self-play data. We present a closed-loop, video-to-action policy that combines an action-free video world model with a carefully-designed IDM based on the robot embodiment Jacobian. We demonstrate that our IDM design is both data-efficient and scalable to high-dimensional action spaces. Our policy, which we coin the Video-to-Embodied Robot Action Model (VERA), achieves strong performance across simulated and real-world benchmarks, including zero-shot Panda arm manipulation and 16-DoF Allegro-hand dexterous cube re-orientation. The same video planner can be used across multiple embodiments by pairing it with different embodiment-specific IDMs. Our results show that decoupled video planning plus faithful video-to-action translation is a viable alternative route towards zero-shot, cross-embodiment, and generalizable robot control. More results are available on our project website: this https URL .

</details>

---

### [[20_Research/Papers/大模型/A_Fixed-Budget,_Cluster-Aware_Standard_for_LLM-as-a-Judge_Evaluation_A_Multi-Hop_RAG_Stress_Test|A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test]]

![[assets/2605.27789_figure.png|800]]

- **arXiv**: [2605.27789](https://arxiv.org/abs/2605.27789)
- **PDF**: https://arxiv.org/pdf/2605.27789
- **详细分析**: [[20_Research/Papers/大模型/A_Fixed-Budget,_Cluster-Aware_Standard_for_LLM-as-a-Judge_Evaluation_A_Multi-Hop_RAG_Stress_Test|A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test]]
- **作者**: Camilo Chacón Sartori, José H. García
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM

#### 研究背景与动机

《A Fixed-Budget, Cluster-Aware Standard for LLM-as-a-Judge Evaluation: A Multi-Hop RAG Stress Test》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) systems are often compared by asking a large language model (LLM) judge which answer is better. For multi-hop RAG, this has become a measurement problem as much as a modeling problem: the same score can reflect retrieval quality, answer length, lexical overlap, or a statistical test that ignores clustered data. We ask what happens when these choices are made explicit. We propose a minimum measurement standard for LLM-as-a-judge comparisons in RAG. The standard fixes the top-100 candidate pool, evidence budget, answer cap, generator, and prompt; it also requires pre-registered hypotheses, cluster-aware inference, an exact cluster sign-flip check when feasible, and second-judge replication. Clustered benchmarks can overstate progress; the field should adopt this standard. We stress-test it with Genetic Algorithm Decoder for Multi-hop Evidence Composition (GADMEC), an evolutionary evidence selector, on 400 multi-hop questions in computer science/machine learning (CS/ML) and Materials Science. The protocol changes the empirical story. A binomial test makes all four semantic-baseline comparisons look significant; cluster-aware inference leaves only one Bonferroni-significant result. BM25 beats pure semantic GADMEC under the same budget, while a lexical-semantic hybrid recovers in CS/ML and narrows the Materials Science gap.

</details>

---

### [[20_Research/Papers/大模型/Got_a_Secret_LLM_Agents_Can't_Keep_It_Evaluating_Privacy_in_Multi-Agent_Systems|Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems]]

![[assets/2605.27766_figure.png|800]]

- **arXiv**: [2605.27766](https://arxiv.org/abs/2605.27766)
- **PDF**: https://arxiv.org/pdf/2605.27766
- **详细分析**: [[20_Research/Papers/大模型/Got_a_Secret_LLM_Agents_Can't_Keep_It_Evaluating_Privacy_in_Multi-Agent_Systems|Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems]]
- **作者**: Aman Priyanshu, Supriti Vijay, Esha Pahwa
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Got a Secret? LLM Agents Can't Keep It: Evaluating Privacy in Multi-Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM safety evaluations predominantly test models in isolation, yet deployed AI agents increasingly operate within persistent social environments alongside other agents. We introduce a Moltbook-style simulation platform where thousands of LLM agents interact across communities over a simulated month, and use it to evaluate privacy as a downstream safety concern under varying degrees of social pressure. We find that shifting from single turn to multi turn social evaluation amplifies privacy violations (CIMemories 19.95% to Ours 45.30% across OpenAI models), that leakage is socially contagious, with agents 8 times more likely to disclose sensitive information after observing a peer do so, and that explicit privacy instructions reduce but do not eliminate this effect, leaving leakage rates above 37.8% even with safeguards. Our findings suggest that static chat based safety benchmarks systematically underestimate risks in agentic deployment, and that social context alone is sufficient to elicit sensitive disclosures that single turn evaluations would never surface.

</details>

---

### [[20_Research/Papers/大模型/Restoring_the_Sweet_Spot_Pass-Rate_Weighted_Self-Distillation_for_LLM_Reasoning|Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning]]

![[assets/2605.27765_figure.png|800]]

- **arXiv**: [2605.27765](https://arxiv.org/abs/2605.27765)
- **PDF**: https://arxiv.org/pdf/2605.27765
- **详细分析**: [[20_Research/Papers/大模型/Restoring_the_Sweet_Spot_Pass-Rate_Weighted_Self-Distillation_for_LLM_Reasoning|Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning]]
- **作者**: Zehao Liu, Yuanpu Cao, Jinghui Chen, Vasant G. Honavar
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.3，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Restoring the Sweet Spot: Pass-Rate Weighted Self-Distillation for LLM Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SciKnowEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-Distillation Policy Optimization (SDPO) provides dense token-level credit assignment for reinforcement learning with large language models by leveraging the model's own feedback-conditioned predictions as a self-teacher. Unlike GRPO, however, whose group-relative advantage naturally concentrates learning on a sweet spot of intermediate-difficulty questions, SDPO's KL-based advantage lacks an implicit notion of difficulty awareness. We analyze this gap through the lens of GRPO's advantage normalization. Extending the learnability framework to normalized rewards, we show that normalization absorbs the variance term $p(1-p)$, equalizing leading-order learnability across questions and leaving $\sqrt{p(1-p)}$ as the sole residual scaling factor in the per-question gradient. This analysis yields a simple prescription: weight each question's SDPO loss by $[\hat{p}(1-\hat{p})]^{1/2}$, resulting in SC-SDPO, a scale-consistent variant of SDPO. The proposed weights are obtained as a zero-cost byproduct of on-policy rollouts with batch-adaptive normalization, inducing an implicit curriculum that dynamically tracks the model's evolving competence. Experiments on scientific reasoning and tool-use benchmarks demonstrate that SC-SDPO consistently improves over SDPO, yielding gains of +3.2/+4.3 (mean@16/maj@16) on Qwen3-8B and +1.8/+3.0 on OLMo-3-7B, while preserving stable training dynamics throughout optimization.

</details>

---

### [[20_Research/Papers/具身智能/PEAM_Parametric_Embodied_Agent_Memory_through_Contrastive_Internalization_of_Experience_in_Minecraft|PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft]]

![[assets/2605.27762_figure.png|800]]

- **arXiv**: [2605.27762](https://arxiv.org/abs/2605.27762)
- **PDF**: https://arxiv.org/pdf/2605.27762
- **详细分析**: [[20_Research/Papers/具身智能/PEAM_Parametric_Embodied_Agent_Memory_through_Contrastive_Internalization_of_Experience_in_Minecraft|PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft]]
- **作者**: Yuchen Guo, Junli Gong, Hongmin Cai, Yiu-ming Cheung, Weifeng Su
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.2，大模型 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PEAM: Parametric Embodied Agent Memory through Contrastive Internalization of Experience in Minecraft》归入 具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present PEAM, a Parametric Embodied Agent Memory framework in Minecraft that transforms agent memory from inference-time retrieval into parameter-resident skills internalized through experience. PEAM pairs a slow deliberative LLM for open-ended reasoning with a fast parametric module for reflexive execution of consolidated skills. The fast module is a multimodal Mixture-of-Experts LoRA architecture with per-category physically isolated adapters, enabling parameter-level continual learning without catastrophic forgetting. We treat failure as a first-class training signal: failure--correction trajectory pairs are internalized through a joint behavioral-cloning and contrastive objective, so the agent learns not only what succeeds but also how corrected actions differ from failed ones. To govern consolidation, PEAM introduces a parameterization-worthiness score for deciding which experience should be internalized, and a scale-free self-triggered consolidation mechanism for deciding when to internalize without task-specific hand-tuned thresholds, making the agent self-evolving as the trigger transfers across task distributions without re-tuning. Experiments in Minecraft show that PEAM improves long-horizon task performance, mitigates forgetting on previously consolidated skills, and improves parametric-versus-retrieval efficiency over retrieval-based embodied agents and parametric memory variants.

</details>

---

### [[20_Research/Papers/具身智能/HumanoidMimicGen_Data_Generation_for_Loco-Manipulation_via_Whole-Body_Planning|HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning]]

![[assets/2605.27724_figure.png|800]]

- **arXiv**: [2605.27724](https://arxiv.org/abs/2605.27724)
- **PDF**: https://arxiv.org/pdf/2605.27724
- **详细分析**: [[20_Research/Papers/具身智能/HumanoidMimicGen_Data_Generation_for_Loco-Manipulation_via_Whole-Body_Planning|HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning]]
- **作者**: Kevin Lin, Ajay Mandlekar, Caelan Reed Garrett, Nikita Chernyadev, Yu Fang, Runyu Ding, Yuqi Xie, Justin Tran, Linxi Fan, Yuke Zhu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《HumanoidMimicGen: Data Generation for Loco-Manipulation via Whole-Body Planning》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning is a promising approach for training humanoid robots to both walk and manipulate, but it requires a large number of demonstrations, which are time-intensive and difficult to collect via teleoperation. Existing data-generation algorithms can automatically synthesize demonstrations for manipulators, but they are ineffective on humanoids because their high-dimensional composite action spaces involve arms, legs, and torsos. We present HumanoidMimicGen, a method for generating humanoid legged loco-manipulation data. Our method adapts contact-rich whole-body skills from a handful of source demonstrations to new states, generalizing across changes in object pose. By interleaving these single- and dual-arm skills with whole-body locomotion and manipulation planning, the method generates stable, collision-free data across diverse scenes and layouts. To evaluate our approach, we introduce a new simulated loco-manipulation benchmark containing nine diverse tasks that test humanoid loco-manipulation capabilities. There, we demonstrate that HumanoidMimicGen automatically generates large datasets for imitation learning and enables a systematic study of how data generation and policy learning decisions impact model performance. We show that whole-body visuomotor policies co-trained with data generated by HumanoidMimicGen outperform those trained only on real-world data by 20%.

</details>

---

### [[20_Research/Papers/机器人/Simulation-Informed_Diffusion_for_Decentralized_Multi-robot_Motion_Planning|Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning]]

![[assets/2605.27697_figure.png|800]]

- **arXiv**: [2605.27697](https://arxiv.org/abs/2605.27697)
- **PDF**: https://arxiv.org/pdf/2605.27697
- **详细分析**: [[20_Research/Papers/机器人/Simulation-Informed_Diffusion_for_Decentralized_Multi-robot_Motion_Planning|Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning]]
- **作者**: Jinhao Liang, Sven Koenig, Ferdinando Fioretto
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Simulation-Informed Diffusion for Decentralized Multi-robot Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decentralized multi-robot motion planning requires each robot to generate collision-free trajectories from local observations, without global sensing or reliable communication. However, most existing planners, whether classical or learning-based, generate trajectories from a static snapshot of the local observation, which limits their ability to anticipate the future behavior of neighboring robots. This limitation is critical as the number of robots increases and the environment becomes more cluttered. To overcome this challenge, this paper introduces Simulation-Informed Diffusion (SID), a decentralized framework built on constraint-aware diffusion models (CADM). SID first uses CADM to simulate the future trajectories of neighboring robots from their currently observed states, and then uses the same CADM to plan each robot's own trajectory under safety constraints informed by these simulations. Crucially, the accurate simulation of neighbors enables a minimal communication scheme that triggers coordination only when necessary in highly congested scenarios. Experiments across diverse environments show that SID consistently outperforms baseline methods in terms of planning effectiveness and constraint satisfaction, and scales to scenarios with 108 robots and 160 obstacles.

</details>

---

### [[20_Research/Papers/强化学习/Transferable_Reinforcement_Learning_via_Probabilistic_Latent_Embeddings_and_Dynamic_Policy_Adaptation_for_Sim-to-Real_Deployment|Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment]]

![[assets/2605.27659_figure.png|800]]

- **arXiv**: [2605.27659](https://arxiv.org/abs/2605.27659)
- **PDF**: https://arxiv.org/pdf/2605.27659
- **详细分析**: [[20_Research/Papers/强化学习/Transferable_Reinforcement_Learning_via_Probabilistic_Latent_Embeddings_and_Dynamic_Policy_Adaptation_for_Sim-to-Real_Deployment|Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment]]
- **作者**: Gengyue Han, Yiheng Feng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.32（加权：具身智能 0.9，大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Transferable Reinforcement Learning via Probabilistic Latent Embeddings and Dynamic Policy Adaptation for Sim-to-Real Deployment》归入 强化学习、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Meta-RL, PEARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Due to limited resources and public safety concerns, deep reinforcement learning (RL) agents for many cyber-physical systems (e.g., autonomous vehicles) are first trained in simulators. However, when deployed in real world environments, they often suffer from performance degradation or safety violations because of the inevitable Sim2Real gap. Existing zero-shot approaches, such as robust safe RL and domain randomization, mitigate this issue but typically at the cost of degraded performance or residual safety risks when experiencing unmodeled system dynamics. To address these limitations, we propose a novel reinforcement learning framework that enables safe and efficient policy transfer via probabilistic latent embeddings and dynamic policy adaptation. We consider a family of Constrained Markov Decision Processes (CMDPs) under different environment contexts. By leveraging latent context variable in meta-RL, the proposed framework infers the latent representation of the environment from simulated experiences. Furthermore, it incorporates a distributional RL formulation, which allows risk levels of the deployed policy to be adjusted dynamically, based on the estimation accuracy of the latent context variable. This strategy promotes safety at the early deployment stage and improves efficiency through fast policy adaptation under the Sim2Real gap.

</details>

---

### [[20_Research/Papers/具身智能/BIRDS_Characterizing_and_Understanding_Biodiversity_Impact_of_Large_Language_Model_Serving|BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving]]

![[assets/2605.27480_figure.png|800]]

- **arXiv**: [2605.27480](https://arxiv.org/abs/2605.27480)
- **PDF**: https://arxiv.org/pdf/2605.27480
- **详细分析**: [[20_Research/Papers/具身智能/BIRDS_Characterizing_and_Understanding_Biodiversity_Impact_of_Large_Language_Model_Serving|BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving]]
- **作者**: Tianyao Shi, Yi Ding
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.9）
- **关联关键词**: LLM, EmbodiedAI

#### 研究背景与动机

《BIRDS: Characterizing and Understanding Biodiversity Impact of Large Language Model Serving》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CrossCodeEval, LongBench, RepoBench, SuperGPQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) serving creates environmental impacts beyond carbon and water, including ecosystem damage through biodiversity-related pathways. We present BIRDS, a framework for Biodiversity Impact of Request-Driven LLM Serving. BIRDS defines request-level functional units, quantifies operational and embodied biodiversity impact, and introduces Quality-Normalized Biodiversity Impact (QNBI) to jointly analyze ecological impact and response quality. Across diverse workloads, models, GPUs, and regions, BIRDS reveals that biodiversity impact accumulates at scale and exposes actionable quality-aware serving tradeoffs.

</details>

---

### [[20_Research/Papers/强化学习/Personalized_Observation_Normalization_for_Federated_Reinforcement_Learning_in_Simulation_Environments_with_Heterogeneity|Personalized Observation Normalization for Federated Reinforcement Learning in Simulation Environments with Heterogeneity]]

![[assets/2605.27385_figure.png|800]]

- **arXiv**: [2605.27385](https://arxiv.org/abs/2605.27385)
- **PDF**: https://arxiv.org/pdf/2605.27385
- **详细分析**: [[20_Research/Papers/强化学习/Personalized_Observation_Normalization_for_Federated_Reinforcement_Learning_in_Simulation_Environments_with_Heterogeneity|Personalized Observation Normalization for Federated Reinforcement Learning in Simulation Environments with Heterogeneity]]
- **作者**: Yiran Pang, Zhen Ni, Xiangnan Zhong
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Personalized Observation Normalization for Federated Reinforcement Learning in Simulation Environments with Heterogeneity》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FedRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated reinforcement learning (FedRL) enables multiple agents to collaboratively train a global policy without sharing raw data, making it ideal for privacy-sensitive applications. However, FedRL faces challenges in heterogeneous environments where differing state-transition dynamics lead to non-identical input distributions and imbalanced parameter updates during aggregation. Therefore, this paper develops a personalized observation normalization (PON) method, allowing each agent to locally normalize raw state inputs using a continuously updated running mean and variance. This design ensures consistent scaling of local feature without overshadowing across agents during aggregation. Furthermore, we demonstrate that sharing normalization parameters across agents is ineffective due to the diverse local input distributions, which highlights the necessity of personalized statistics. Experiments on heterogeneous MuJoCo tasks show that our developed PON accelerates training and achieves superior performance compared to baseline methods.

</details>

---
