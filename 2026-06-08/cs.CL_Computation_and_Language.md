# cs.CL | Computation and Language | 2026-06-08

#arxiv #ComputerScience

**论文数**: 19

### [[20_Research/Papers/大模型/Agentopia_Long-Term_Life_Simulation_and_Learning_in_Agent_Societies|Agentopia: Long-Term Life Simulation and Learning in Agent Societies]]

![[assets/2606.07513_figure.png|800]]

- **arXiv**: [2606.07513](https://arxiv.org/abs/2606.07513)
- **PDF**: https://arxiv.org/pdf/2606.07513
- **详细分析**: [[20_Research/Papers/大模型/Agentopia_Long-Term_Life_Simulation_and_Learning_in_Agent_Societies|Agentopia: Long-Term Life Simulation and Learning in Agent Societies]]
- **作者**: Xintao Wang, Sirui Zheng, Hongqiu Wu, Weiyuan Li, Jen-tse Huang, Minghao Zhu, Can Zu, Qi Deng, Jiawei Wang, Qianyu He, Heng Wang, Xiaojian Wu...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Agentopia: Long-Term Life Simulation and Learning in Agent Societies》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BookWorld, Cross-World, Per-World, RoleEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans learn from social life. Simulating this process with LLM-powered agents represents a promising research direction, raising a natural question: whether LLMs can learn from such simulated social experience to better understand and replicate human behavior. However, prior agent society simulations typically operate at the scale of days, limiting the depth of social interactions and long-term growth. In this paper, we study long-term life simulation and LLM learning in agent societies, with two goals: (1) investigating social behaviors that emerge from life-long simulation, and (2) developing anthropomorphic capabilities in LLMs, particularly intelligence in social life, through years of simulated social experience. Specifically, we present Agentopia, a comprehensive framework for long-term life simulation in multi-agent societies, where 100 agents autonomously pursue personal growth, develop social relationships, and fulfill their needs and goals over 10 simulated years. We define life reward to mirror human well-being, and leverage this reward to train LLMs via rejection sampling. Extensive experiments show that agents exhibit rich emergent social behaviors. Furthermore, life reward training effectively enhances the underlying LLM, which leads to improved agent well-being in simulation, and generalizes to downstream role-playing benchmarks with +15.6% improvement.

</details>

---

### [[20_Research/Papers/大模型/M$^3$Exam_Benchmarking_Multimodal_Memory_for_Realistic_User-Agent_Interactions|M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions]]

![[assets/2606.07402_figure.png|800]]

- **arXiv**: [2606.07402](https://arxiv.org/abs/2606.07402)
- **PDF**: https://arxiv.org/pdf/2606.07402
- **详细分析**: [[20_Research/Papers/大模型/M$^3$Exam_Benchmarking_Multimodal_Memory_for_Realistic_User-Agent_Interactions|M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions]]
- **作者**: Zhengjun Huang, Wenxuan Liu, Zhoujin Tian, Wei Chen, Junle Chen, Yuqian Wu, Fangyuan Zhang, Qintian Guo, Xiaofang Zhou
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《M$^3$Exam: Benchmarking Multimodal Memory for Realistic User-Agent Interactions》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language agents are increasingly deployed over accumulating multimodal information, yet existing benchmarks assume a human-human form with sparse visuals and straightforward content, evaluating neither reasoning over authentic multimodal file interaction nor the interpretation of concealed user information. We therefore introduce M$^3$Exam, a query-centric multimodal conversational memory benchmark built on realistic user-agent interaction, with multi-dimensional evaluation spanning cross-modal grounding and implicit information inference. Benchmarking MLLMs and memory systems reveals persistent gaps in cross-modal grounding, cross session reasoning, and the efficiency cost of accumulating multimodal context. We further propose M$^3$Proctor, a multimodal memory method that detects query modality bias and consumes raw visual sources only on demand, improving accuracy by 13% while cutting index-construction time and retrieved tokens by over 70%.

</details>

---

### [[20_Research/Papers/大模型/LLM-Guided_Evolution_for_Medical_Decision_Pipelines|LLM-Guided Evolution for Medical Decision Pipelines]]

![[assets/2606.07342_figure.png|800]]

- **arXiv**: [2606.07342](https://arxiv.org/abs/2606.07342)
- **PDF**: https://arxiv.org/pdf/2606.07342
- **详细分析**: [[20_Research/Papers/大模型/LLM-Guided_Evolution_for_Medical_Decision_Pipelines|LLM-Guided Evolution for Medical Decision Pipelines]]
- **作者**: Ivan Sviridov, Artem Oskin, Ivan Panin, Iaroslav Bespalov, Dmitry Dylov, Ivan Oseledets, Aleksandr Nesterov
- **cs 子类**: cs.CL, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《LLM-Guided Evolution for Medical Decision Pipelines》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adapting large language models (LLMs) to clinical workflows often requires costly fine-tuning or manual prompt and pipeline engineering. We study LLM-guided MAP-Elites evolution as an inference-time alternative for discovering medical decision strategies and provide an implementation repository at https://github.com/univanxx/llm_guided_evo_medical. We formulate urgency triage, interactive consultation, and medical image classification as evolutionary searches over executable artifacts optimized by task-specific fitness functions. Across all three settings, evolution improves over manually designed baselines under practical constraints. In triage, evolved programs increase Semigran accuracy from $77.3\%$ to $87.1\%$ and emergency recall from $0.60$ to $0.97$, while improving safety-weighted held-out MIMIC-ESI performance. In interactive consultation, evolved policies improve the accuracy--cost frontier across Llama-3, Qwen-3.5, and Gemma-4 and transfer to held-out iCRAFTMD. In PneumoniaMNIST, prompt-only evolution improves frozen MedGemma VLMs while preserving strict JSON outputs. Qualitative analysis shows that the gains come from interpretable program-level mechanisms, calibrated triage boundaries, targeted evidence acquisition, selective commitment, and finding-oriented visual decision rules, rather than superficial prompt rewording alone.

</details>

---

### [[20_Research/Papers/大模型/SWE-Explore_Benchmarking_How_Coding_Agents_Explore_Repositories|SWE-Explore: Benchmarking How Coding Agents Explore Repositories]]

![[assets/2606.07297_figure.png|800]]

- **arXiv**: [2606.07297](https://arxiv.org/abs/2606.07297)
- **PDF**: https://arxiv.org/pdf/2606.07297
- **详细分析**: [[20_Research/Papers/大模型/SWE-Explore_Benchmarking_How_Coding_Agents_Explore_Repositories|SWE-Explore: Benchmarking How Coding Agents Explore Repositories]]
- **作者**: Shaoqiu Zhang, Yuhang Wang, Jialiang Liang, Yuling Shi, Wenhao Zeng, Maoquan Wang, Shilin He, Ningyuan Xu, Siyu Ye, Kai Cai, Xiaodong Gu
- **cs 子类**: cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《SWE-Explore: Benchmarking How Coding Agents Explore Repositories》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ContextBench, Loc-Bench, SWE-Bench, SWE-ContextBench, SWE-Explore-Bench, SWE-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Repository-level coding benchmarks such as SWE-bench have driven a rapid surge in the capabilities of coding agents. Yet they usually treat coding tasks as a holistic, binary prediction problem (e.g., resolved or unresolved), neglecting fine-grained agent capabilities such as repository understanding, context retrieval, code localization, and bug diagnosis. In this paper, we introduce SWE-Explore, a benchmark that isolates the evaluation of repository exploration, a critical capability of coding agents. Given a repository and an issue, SWE-Explore asks an explorer to return a ranked list of relevant code regions under a fixed line budget. SWE-Explore covers 848 issues across 10 programming languages and 203 open-source repositories. For each instance, we derive line-level ground truth from independent agent trajectories that successfully solved the same issue, distilling the specific code regions their solution paths actually consulted. We evaluate exploration along coverage, ranking, and context-efficiency dimensions, showing that these metrics strongly track downstream repair behavior. Across a broad set of retrieval methods, general coding agents, and specialized localizers, we find that agentic explorers form a clear tier above classical retrieval. While file-level localization is already strong for modern methods, line-level coverage and efficient ranking remain the key axes differentiating state-of-the-art explorers.

</details>

---

### [[20_Research/Papers/大模型/HKVM-RAG_Key-Value-Separated_Hypergraph_Evidence_Organization_for_Multi-Hop_RAG|HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop RAG]]

![[assets/2606.07218_figure.png|800]]

- **arXiv**: [2606.07218](https://arxiv.org/abs/2606.07218)
- **PDF**: https://arxiv.org/pdf/2606.07218
- **详细分析**: [[20_Research/Papers/大模型/HKVM-RAG_Key-Value-Separated_Hypergraph_Evidence_Organization_for_Multi-Hop_RAG|HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop RAG]]
- **作者**: Mingyu Zhang, Ying Ma
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《HKVM-RAG: Key-Value-Separated Hypergraph Evidence Organization for Multi-Hop RAG》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-hop RAG poses a data-engineering problem beyond passage matching: under fixed retrieval budgets, a system must organize retrieved text into evidence units that expose answer chains. Dense retrievers score passages independently, while graph-based memories make associations explicit but often rely on pairwise or entity-centered keys that fragment multi-hop evidence. We present HKVM-RAG, a key-value-separated evidence-organization layer. It assembles answer-path hyperedges from cached passage-level LLM evidence tuples and uses them as retrieval keys, while retaining passage text as answer values. To isolate key-space design, our fixed-substrate protocol holds the tuple cache, candidate passages, reader, and evaluation budget constant across pairwise graph and hypergraph variants. Weighted hypergraph key-value retrieval improves over KG-PPR by +3.426 F1 on 2WikiMultiHopQA and +3.592 F1 on MuSiQue; HotpotQA shows that higher structured support coverage need not yield standalone answer-F1 gains. We therefore study WHG-KV as an evidence-control signal rather than a dense-retrieval replacement. Oracle and train-to-dev analyses identify support selection as repairable, and a dense-aware controller combines frozen ColBERTv2 and HKVM rank/score features using out-of-fold HKVM predictions. It reaches 88.846, 65.073, and 85.810 F1 on the three benchmarks, improving over ColBERTv2 by +11.084, +6.763, and +5.966 F1. Source-level ablations show that matched non-WHG structured signals do not match the WHG-KV gains. These results provide bounded evidence that key-value-separated hypergraph organization can serve as a reusable evidence-control mechanism for multi-hop RAG.

</details>

---

### [[20_Research/Papers/大模型/From_Correctness_to_Utility_Gain-Based_Prefix_Evaluation_for_LLM_Reasoning|From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning]]

![[assets/2606.07190_first_page.png|800]]

- **arXiv**: [2606.07190](https://arxiv.org/abs/2606.07190)
- **PDF**: https://arxiv.org/pdf/2606.07190
- **详细分析**: [[20_Research/Papers/大模型/From_Correctness_to_Utility_Gain-Based_Prefix_Evaluation_for_LLM_Reasoning|From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning]]
- **作者**: Yuhang Zhou, Yixin Cao, Guangnan Ye
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《From Correctness to Utility: Gain-Based Prefix Evaluation for LLM Reasoning》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning prefixes shape the future trajectory of LLM problem solving, yet existing process reward models usually evaluate them through local step correctness. We argue that correctness is a useful but indirect proxy for the effect we ultimately care about: whether a prefix increases the probability of successful completion. We define this effect as prefix gain, the solve-rate improvement induced by conditioning lightweight student model group on a prefix, and use it to train a Prefix Utility Model (PUM) with a simple pairwise ranking objective. PUM learns outcome-grounded prefix utility and can score both complete trajectories and partial reasoning prefixes. Across Best-of-$N$ selection, beam search, and reinforcement learning on mathematical reasoning, PUM provides a strong prefix-level supervision signal, especially when candidate pools are large, search budgets increase, or rule-based rewards are sparse. We release all data, models, and code at https://zhiqix.github.io/pum-project-page.

</details>

---

### [[20_Research/Papers/大模型/SigmaScale_LLM_Compression_with_SVD-based_Low-Rank_Decomposition_and_Learned_Scaling_Matrices|SigmaScale: LLM Compression with SVD-based Low-Rank Decomposition and Learned Scaling Matrices]]

![[assets/2606.07098_figure.png|800]]

- **arXiv**: [2606.07098](https://arxiv.org/abs/2606.07098)
- **PDF**: https://arxiv.org/pdf/2606.07098
- **详细分析**: [[20_Research/Papers/大模型/SigmaScale_LLM_Compression_with_SVD-based_Low-Rank_Decomposition_and_Learned_Scaling_Matrices|SigmaScale: LLM Compression with SVD-based Low-Rank Decomposition and Learned Scaling Matrices]]
- **作者**: Ernests Lavrinovics, Marco Letizia, Roy Janco, Shai Segal, Johannes Bjerva, Maurizio Pierini
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《SigmaScale: LLM Compression with SVD-based Low-Rank Decomposition and Learned Scaling Matrices》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenBookQA, PIQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present SigmaScale, a method for learning auxiliary scaling matrices $S$ to aid truncated Singular Value Decomposition (SVD) based Large Language Model (LLM) compression. Instead of deriving scaling matrices analytically, SigmaScale optimizes two sets of vectors that define diagonal row and column scaling transformations under an activation-aware compression loss. We show that learned scaling lowers the effective intrinsic rank of weight matrices, as reflected by reductions in effective-rank entropy, and that this reduction is strongly correlated with compression loss. Experiments on Llama 3.1 8B Instruct and Qwen3-8B show that SigmaScale is competitive with closely related state-of-the-art SVD-based compression methods across perplexity and zero-shot benchmarks. By using learned activation-aware transformations, SigmaScale explores a more flexible route to low-rank LLM compression by adapting to the structure of individual model weights. The advantage observed in specific tasks makes our approach a valid option for applications requiring a reduced LLM-inference computing cost.

</details>

---

### [[20_Research/Papers/大模型/Modeling_semantic_association_in_self-paced_reading_with_language_model_embeddings|Modeling semantic association in self-paced reading with language model embeddings]]

![[assets/2606.07066_figure.png|800]]

- **arXiv**: [2606.07066](https://arxiv.org/abs/2606.07066)
- **PDF**: https://arxiv.org/pdf/2606.07066
- **详细分析**: [[20_Research/Papers/大模型/Modeling_semantic_association_in_self-paced_reading_with_language_model_embeddings|Modeling semantic association in self-paced reading with language model embeddings]]
- **作者**: Sara Møller Østergaard, Kenneth Enevoldsen, Afra Alishahi, Bruno Nicenboim
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Modeling semantic association in self-paced reading with language model embeddings》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Semantic association between a word and its context has been identified as an important component of reading comprehension, even when word predictability is accounted for. Recent research has highlighted the potential of language model ( LM) embeddings to quantify semantic association. Yet, embedding-based semantic association have been operationalized in a myriad of ways. In this study, we use embeddings from LMs to estimate semantic association on a corpus of joint electroencephalography (EEG) and self-paced reading of natural, Dutch texts. Semantic association is calculated in ten different implementations that vary the embedding model and context lengths. The effects of semantic association across the different implementations on the N400 and self-paced reading times are examined using Bayesian hierarchical models and Bayes factor. The results show that the choice of embedding model can alter the estimated effect of semantic association on both the N400 and self-paced reading times. Furthermore, the results demonstrate a promising potential of sentence embeddings for capturing semantic association, as only implementations relying on sentence embeddings indicate reliable results of semantic association beyond word predictability on both neural and behavioral measures. Together, these findings highlight the importance of methodological choices in quantifying semantic association.

</details>

---

### [[20_Research/Papers/大模型/Contrastive_Training_with_LLM-generated_Near-Misses_for_Robust_Code-Switching_Speech_Recognition|Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition]]

![[assets/2606.06985_figure.png|800]]

- **arXiv**: [2606.06985](https://arxiv.org/abs/2606.06985)
- **PDF**: https://arxiv.org/pdf/2606.06985
- **详细分析**: [[20_Research/Papers/大模型/Contrastive_Training_with_LLM-generated_Near-Misses_for_Robust_Code-Switching_Speech_Recognition|Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition]]
- **作者**: Tung X. Nguyen, Hieu Minh Truong, Giang-Son Nguyen, Nhu Vo, Wray Buntine, Dung D. Le
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Contrastive Training with LLM-generated Near-Misses for Robust Code-Switching Speech Recognition》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code-switching (CS), the alternation between multiple languages within a single utterance, remains challenging for Automatic Speech Recognition (ASR). To address this issue, we propose a Point-of-Interest (POI)-aware contrastive training framework that improves recognition at CS-critical regions. We first identify CS spans by adopting POI detection method from literature, then construct acoustically plausible near-miss hypotheses by perturbing POIs in ASR N-best outputs and expanding candidates with a large language model. Hard but plausible negatives are retained through filtering with acoustic, phonemic, and textual constraints. Finally, we fine-tune Whisper-small with LoRA using a POI-weighted cross-entropy anchor objective together with a multi-negative contrastive ranking loss. Experiments on CS-FLEURS (cmn-eng) and ViMedCSS (vie-eng) show consistent reductions of over 2% in both general and CS-aware error rates compared to standard LoRA fine-tuning.

</details>

---

### [[20_Research/Papers/大模型/Tree-of-Experience_A_Structured_Experience-Management_Solution_for_Self-Evolving_Agents_under_Low-Repetition_and_Implicit-Reward_Environment|Tree-of-Experience: A Structured Experience-Management Solution for Self-Evolving Agents under Low-Repetition and Implicit-Reward Environments]]

![[assets/2606.06960_figure.png|800]]

- **arXiv**: [2606.06960](https://arxiv.org/abs/2606.06960)
- **PDF**: https://arxiv.org/pdf/2606.06960
- **详细分析**: [[20_Research/Papers/大模型/Tree-of-Experience_A_Structured_Experience-Management_Solution_for_Self-Evolving_Agents_under_Low-Repetition_and_Implicit-Reward_Environment|Tree-of-Experience: A Structured Experience-Management Solution for Self-Evolving Agents under Low-Repetition and Implicit-Reward Environments]]
- **作者**: Zihao Deng, Yining Zhu, Leiming Wang, Jingfei Lu, Junbo Wang, Chuncheng Ran, Yu Yang, Dixuan Yang, Jikun Shen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Tree-of-Experience: A Structured Experience-Management Solution for Self-Evolving Agents under Low-Repetition and Implicit-Reward Environments》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, BigCodeBench, FinEvolveBench, FinQA, LifelongAgentBench, MemRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Experience-based self-evolution is crucial for LLM agents, but existing benchmarks often assume explicit goals, stable task patterns, and clear feedback. We study a more challenging setting: low-repetition tasks with implicit rewards, where past experience is difficult to reuse and feedback is delayed, noisy, and outcome-level. We introduce \textsc{FinEvolveBench}, a temporally controlled benchmark for financial sentiment prediction that links daily news-driven predictions to future excess returns. We further propose Tree-of-Experience (ToE), a structured experience-management method that organizes, retrieves, validates, and updates agent experience. Experiments show that general-purpose experience mechanisms do not consistently outperform no-experience baselines, while ToE achieves stronger overall performance. These results highlight the importance of structured experience management for self-evolving agents in implicit-reward environments.

</details>

---

### [[20_Research/Papers/强化学习/Translate-R1_Cost-Aware_Translation_Tool_Use_via_Reinforcement_Learning|Translate-R1: Cost-Aware Translation Tool Use via Reinforcement Learning]]

![[assets/2606.06835_figure.png|800]]

- **arXiv**: [2606.06835](https://arxiv.org/abs/2606.06835)
- **PDF**: https://arxiv.org/pdf/2606.06835
- **详细分析**: [[20_Research/Papers/强化学习/Translate-R1_Cost-Aware_Translation_Tool_Use_via_Reinforcement_Learning|Translate-R1: Cost-Aware Translation Tool Use via Reinforcement Learning]]
- **作者**: Pratik Jayarao, Chaitanya Dwivedi, Himanshu Gupta, Neeraj Varshney, Adithya M Devraj, Meet Vadera, Priyanka Nigam, Bing Yin
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.6（加权：强化学习 0.6）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Translate-R1: Cost-Aware Translation Tool Use via Reinforcement Learning》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ToRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The performance gap across languages in LLMs is well documented, and closing it natively requires pretraining or fine-tuning on corpora that, for most languages, do not exist. Translation offers an alternative: converting an input into the model's dominant language unlocks its full capabilities at once. Applying translation to every input, however, is wasteful for languages the model already handles, while leaving the choice to the model fails in the opposite way, as LLMs are overconfident and skip the tool even when they cannot understand the input. Prior work resolves this with language-specific rules, domain heuristics, language identifiers, or external routers, each requiring manual engineering. We instead learn a single policy that decides when to translate from reward alone, developing language- and domain-adaptive introspection that assesses its own comprehension and invokes translation only when it cannot solve a task natively. Using data built by our answer-preserving translation pipeline, we continue RL on the post-trained Qwen3-4B across 22 languages in 3 resource tiers (High, Low, XLow) and 5 domains, and introduce confidence-gated GSPO for cost-sensitive tool use. The gated policy lifts reward over the baseline by +4.6 on High, +23.5 on Low, and +17.5 on XLow. Against an unconstrained policy that almost always translates, it preserves full reward at 63% of the cost and is Pareto-optimal across 87% of the cost-sensitivity range. Additionally, to simulate behavior on a completely unseen language, we create 2 synthetic languages, where our gated policy improves +18.7 over the overconfident baseline that underutilizes the tool even on these incomprehensible inputs. The policy transfers zero-shot to 9 held-out languages, and we analyze how tool use emerges over training, per language and per domain.

</details>

---

### [[20_Research/Papers/大模型/Korean_Culture_into_LLM_Alignment_Toward_Cultural_Coherence|Korean Culture into LLM Alignment: Toward Cultural Coherence]]

![[assets/2606.06797_figure.png|800]]

- **arXiv**: [2606.06797](https://arxiv.org/abs/2606.06797)
- **PDF**: https://arxiv.org/pdf/2606.06797
- **详细分析**: [[20_Research/Papers/大模型/Korean_Culture_into_LLM_Alignment_Toward_Cultural_Coherence|Korean Culture into LLM Alignment: Toward Cultural Coherence]]
- **作者**: MinJae Jung, Minwoo Kim
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Korean Culture into LLM Alignment: Toward Cultural Coherence》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Training-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cultural-aspect work on large language models is dominated by a negative target: which outputs to suppress. We argue that a constructive counterpart is also needed, a working definition of what a culturally coherent response is rather than only what it must avoid, and instantiate it for Korean. We design an alignment-data pipeline around a prompt-based LLM seed generator that expands a Korean harm taxonomy, with a Korean-culturally-adapted safe-response policy at its centre: a per-category guideline grounded in Korean legal frameworks, social norms, and interpretive conventions, against which three frontier models each produce a candidate response. DPO fine-tuning on the resulting triplets improves the Korean cultural safe rate across six open-weight LLMs while causing no large degradation on Korean general-capability benchmarks, and qualitative outputs show fine-tuned models naming Korean statutes and institutional procedures and, where appropriate, supplying constructive Korean-context information alongside refusal.

</details>

---

### [[20_Research/Papers/大模型/TA-RAG_Tone-Aware_Retrieval-Augmented_Generation_for_Peer-Support_Health_Communication|TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication]]

![[assets/2606.06794_figure.png|800]]

- **arXiv**: [2606.06794](https://arxiv.org/abs/2606.06794)
- **PDF**: https://arxiv.org/pdf/2606.06794
- **详细分析**: [[20_Research/Papers/大模型/TA-RAG_Tone-Aware_Retrieval-Augmented_Generation_for_Peer-Support_Health_Communication|TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication]]
- **作者**: Yong-Bin Kang, Anthony McCosker
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM

#### 研究背景与动机

《TA-RAG: Tone-Aware Retrieval-Augmented Generation for Peer-Support Health Communication》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SemSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) successfully grounds large language model (LLM) outputs in trusted documents, but factual grounding alone is insufficient for sensitive peer-support health communication. In domains such as HIV peer support, responses must also be accessible, stigma-free, empathetic, and tailored to the recipient. This paper presents TA-RAG, a lightweight, prompt-based tone-aware RAG framework that embeds explicit tone control into a RAG pipeline without requiring model fine-tuning. We operationalise tone across four core components: stigma-free rewriting, readability adjustment, recipient adaptation, and empathy rephrasing. We evaluate TA-RAG through component-level tests using questions derived from HIV Online Learning Australia (HOLA), UNAIDS terminology guidance, readability metrics, peer-support standards from National Association of People with HIV Australia (NAPWHA), and a public empathy dataset. Results show that the TA-RAG's components improve their targeted communication quality while preserving key content. These findings emphasise that prompt-based tone control is a potential direction for making RAG outputs suitable for sensitive peer-support health communication.

</details>

---

### [[20_Research/Papers/大模型/When_Better_Codebooks_Are_Not_Enough_Predictive_Performance_and_Behavioral_Reliability_in_LLM_Political_Event_Coding|When Better Codebooks Are Not Enough: Predictive Performance and Behavioral Reliability in LLM Political Event Coding]]

![[assets/2606.06781_figure.png|800]]

- **arXiv**: [2606.06781](https://arxiv.org/abs/2606.06781)
- **PDF**: https://arxiv.org/pdf/2606.06781
- **详细分析**: [[20_Research/Papers/大模型/When_Better_Codebooks_Are_Not_Enough_Predictive_Performance_and_Behavioral_Reliability_in_LLM_Political_Event_Coding|When Better Codebooks Are Not Enough: Predictive Performance and Behavioral Reliability in LLM Political Event Coding]]
- **作者**: Zixian He, Bharath Raahul Murugesan, Patrick Brandt, Yibo Hu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《When Better Codebooks Are Not Enough: Predictive Performance and Behavioral Reliability in LLM Political Event Coding》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High accuracy does not necessarily make an LLM a faithful coder. This issue matters because many social-science studies rely on expert-written codebooks to turn text into structured data. We study this problem in political event coding, a challenging source-target relation classification task beyond ordinary sentence-level classification, where models must determine what one actor did to another using detailed coding rules. We test whether expert codebooks become more effective when operationalized into LLM-friendly forms with clearer definitions, examples, retrieved context, and rules for difficult cases. We then evaluate behavioral reliability under controlled changes to label names, codebook order, and label-definition mappings. Clearer codebooks substantially improve classification performance, especially for fine-grained event classification. However, these predictive gains do not fully translate into behavioral reliability. Models may produce valid labels and recover definitions while still failing behavioral reliability tests under controlled codebook changes. These findings suggest that codebook-guided LLM systems should be evaluated not only by accuracy, but also by whether they preserve the coding logic that makes coded outputs meaningful for social-science research.

</details>

---

### [[20_Research/Papers/大模型/A_Four-Condition_Diagnostic_Protocol_for_Evidence_Utilization_in_Long-Context_and_Retrieval-Augmented_Language_Models|A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models]]

![[assets/2606.06758_first_page.png|800]]

- **arXiv**: [2606.06758](https://arxiv.org/abs/2606.06758)
- **PDF**: https://arxiv.org/pdf/2606.06758
- **详细分析**: [[20_Research/Papers/大模型/A_Four-Condition_Diagnostic_Protocol_for_Evidence_Utilization_in_Long-Context_and_Retrieval-Augmented_Language_Models|A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models]]
- **作者**: Haizhou Xia
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《A Four-Condition Diagnostic Protocol for Evidence Utilization in Long-Context and Retrieval-Augmented Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HotpotQA, LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Final-answer accuracy, retrieval recall, and citation overlap do not by themselves identify whether a long-context or retrieval-augmented language model used the evidence it was given. A model can answer from parametric memory, fail despite receiving the right passages, or cite evidence without converting it into the requested answer. This paper proposes a matched four-condition evidence-availability protocol--no evidence, full context, retrieved evidence, and oracle-evidence reference--for diagnosing evidence utilization under fixed examples, prompts, score fields, retrieval settings, and validity checks. ONCU is used as a protocol-bound estimator of recovered oracle-reference evidence advantage and is computed only for denominator-valid groups; denominator-free answer, evidence, retrieval, and failure-audit metrics are reported separately. The empirical study evaluates five local open-weight models from the Qwen, Gemma, Llama, and Mistral families across Controlled-ONCU-safe16K, HotpotQA-ONCU, and 2WikiMultiHopQA-ONCU, with 18,000 ONCU-compatible predictions. The main finding is a task-dependent bottleneck split: controlled synthetic settings primarily expose full-context utilization failures, whereas the tested realistic multi-hop settings primarily expose retrieval-chain coverage failures in denominator-free answer and evidence metrics, with ONCU supporting the same direction on oracle-improving groups. The contribution is a diagnostic protocol for separating no-evidence answerability, oracle-evidence recoverability, full-context utilization, and retrieval-conditioned utilization, rather than a single-score leaderboard for long-context or retrieval-augmented systems.

</details>

---

### [[20_Research/Papers/大模型/PromptPrint_Behavioral_Biometrics_Through_Natural_Language_Prompting_in_LLMs|PromptPrint: Behavioral Biometrics Through Natural Language Prompting in LLMs]]

![[assets/2606.06755_figure.png|800]]

- **arXiv**: [2606.06755](https://arxiv.org/abs/2606.06755)
- **PDF**: https://arxiv.org/pdf/2606.06755
- **详细分析**: [[20_Research/Papers/大模型/PromptPrint_Behavioral_Biometrics_Through_Natural_Language_Prompting_in_LLMs|PromptPrint: Behavioral Biometrics Through Natural Language Prompting in LLMs]]
- **作者**: Shaiv Patel, Kartik Narayan, Vishal Patel
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《PromptPrint: Behavioral Biometrics Through Natural Language Prompting in LLMs》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL, WordNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Authorship attribution research has traditionally focused on long-form, expressive texts; however, interactions with large language models (LLMs) are typically brief and task-driven prompts. This raises a fundamental question: do such prompts contain a stable, author-identifiable, and distinctive signal? We introduce PromptPrint, a systematic study of prompt-based identity, the hypothesis that a user's habitual vocabulary, syntax, and discourse patterns form a learnable behavioral biometric. Using 20,680 real prompts from 1,034 users, we establish three key findings. First, lexical representations significantly outperform semantic encoders, supporting the "lexical stability hypothesis": identity is primarily encoded in surface-level word choice rather than abstract intent. Second, stylometric features exhibit a "uniqueness-consistency paradox": users are highly distinctive across the population, yet behaviorally inconsistent across contexts. Third, adversarial analysis reveals a clear vulnerability spectrum: identity signals are robust to minor lexical perturbations but degrade substantially under semantic paraphrasing. Overall, our results demonstrate strong identification performance at scale, establishing prompt-based identity as a viable behavioral biometric. This work introduces a new perspective on user modeling in LLM interactions, with important implications for security and privacy. Data and code will be released upon the acceptance of our work.

</details>

---

### [[20_Research/Papers/大模型/MADRAG_Multi-Agent_Debate_with_Retrieval-Augmented_Generation_for_Training-Free_Analytic_Essay_Scoring|MADRAG: Multi-Agent Debate with Retrieval-Augmented Generation for Training-Free Analytic Essay Scoring]]

![[assets/2606.06754_first_page.png|800]]

- **arXiv**: [2606.06754](https://arxiv.org/abs/2606.06754)
- **PDF**: https://arxiv.org/pdf/2606.06754
- **详细分析**: [[20_Research/Papers/大模型/MADRAG_Multi-Agent_Debate_with_Retrieval-Augmented_Generation_for_Training-Free_Analytic_Essay_Scoring|MADRAG: Multi-Agent Debate with Retrieval-Augmented Generation for Training-Free Analytic Essay Scoring]]
- **作者**: Ali Keramati, Shiyuan Zhou, Sharad Mehrotra, Mark Warschauer
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《MADRAG: Multi-Agent Debate with Retrieval-Augmented Generation for Training-Free Analytic Essay Scoring》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present MADRAG, a training-free framework for analytic essay scoring that combines multi-agent reasoning with retrieval-augmented grounding. Unlike standard LLM-as-judge approaches, which are prone to bias and unstable scoring, MADRAG decomposes evaluation into an interactive process: an Advocate identifies strengths, a Skeptic critiques weaknesses, and a Judge aggregates their arguments into a final score. Crucially, the Judge is augmented with rubric-aligned exemplar retrieval, enabling calibration through comparison with scored examples. Our results show that MADRAG significantly outperforms prompt-based baselines while approaching the performance of supervised systems without requiring task-specific training. Ablation studies demonstrate that retrieval drives calibration gains, while debate improves reasoning on higher-level traits. Our findings highlight the complementary roles of structured interaction and external memory in reliable LLM-based evaluation.

</details>

---

### [[20_Research/Papers/大模型/Signal-Driven_Observation_for_Long-Horizon_Web_Agents|Signal-Driven Observation for Long-Horizon Web Agents]]

![[assets/2606.06708_figure.png|800]]

- **arXiv**: [2606.06708](https://arxiv.org/abs/2606.06708)
- **PDF**: https://arxiv.org/pdf/2606.06708
- **详细分析**: [[20_Research/Papers/大模型/Signal-Driven_Observation_for_Long-Horizon_Web_Agents|Signal-Driven Observation for Long-Horizon Web Agents]]
- **作者**: Shubham Gaur, Ian Lane
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Signal-Driven Observation for Long-Horizon Web Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld, BrowserGym, OSWorld, OfficeBench, ST-WebAgentBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web agents operating over long horizons ingest raw DOM and accessibility trees -- routinely tens of thousands of tokens -- at every action step, causing progressive context degradation that erodes reasoning well before tasks complete. We argue that this coupling of observation frequency to action frequency is an architectural mistake. Drawing on the insight from Recursive Language Models that querying a document outperforms reading it wholesale, we propose Signal-Driven Observation (SDO): a dedicated sub-call reads the full DOM but returns only task-relevant elements and their selectors, and is re-invoked only when a lightweight signal detector fires -- triggered by URL transitions, newly visible interactive elements, action failures, or exogenous browser events. We outline the open problems SDO introduces and call on the community to treat observation compression as a core architectural decision in web agent design.

</details>

---

### [[20_Research/Papers/强化学习/Improving_Cross-Lingual_Factual_Recall_via_Consistency-Driven_Reinforcement_Learning|Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning]]

![[assets/2606.06586_figure.png|800]]

- **arXiv**: [2606.06586](https://arxiv.org/abs/2606.06586)
- **PDF**: https://arxiv.org/pdf/2606.06586
- **详细分析**: [[20_Research/Papers/强化学习/Improving_Cross-Lingual_Factual_Recall_via_Consistency-Driven_Reinforcement_Learning|Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning]]
- **作者**: Jonathan von Rad, Louis Arts, George Burgess, Eleftheria Kolokytha, Harry O'Donnell, Ektor Oikonomidis Doumpas, Eduardo Sanchez, Yao Lu, Pontus Stenetorp
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Improving Cross-Lingual Factual Recall via Consistency-Driven Reinforcement Learning》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) trained predominantly on English data encode substantial world knowledge, yet often fail to express it reliably in other languages, a phenomenon known as cross-lingual factual inconsistency. To study and address this, we introduce PolyFact, a large-scale parallel multilingual factual QA dataset containing 100K Wikidata-grounded facts across 12 typologically diverse languages. Using PolyFact, we compare light continual pretraining (CPT), supervised fine-tuning (SFT), and reinforcement learning via Group Relative Policy Optimization (GRPO) for improving cross-lingual factual recall in Qwen-2.5-7B and OLMo-2-1124-7B. We find that GRPO consistently outperforms SFT, improving both cross-lingual consistency and generalization to unseen languages, while CPT on parallel data yields limited additional gains. Mechanistic analyses further show that GRPO reorganizes multilingual routing by reducing language specialization in MLP layers and attention heads, thereby promoting more shared cross-lingual representations. We release our code, models, and dataset.

</details>

---
