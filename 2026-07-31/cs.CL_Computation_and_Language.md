# cs.CL | Computation and Language | 2026-07-31

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/大模型/Change2Task_From_Repository_Changes_to_Executable_Coding_Agent_Tasks_and_Environments|Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments]]

![[assets/2607.28591_figure.png|800]]

- **arXiv**: [2607.28591](https://arxiv.org/abs/2607.28591)
- **PDF**: https://arxiv.org/pdf/2607.28591
- **详细分析**: [[20_Research/Papers/大模型/Change2Task_From_Repository_Changes_to_Executable_Coding_Agent_Tasks_and_Environments|Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments]]
- **作者**: Haomin Qi, Xingliang Wang, Xuanqi Gao, Baihui Sang, Xin Zhang, Minghua Ma, Pengfei Gao, Yu Kang, Qingwei Lin, Saravan Rajmohan, Dongmei Zhang, Qi Zhang
- **cs 子类**: cs.CL, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Security, Systems

#### 研究背景与动机

《Change2Task: From Repository Changes to Executable Coding Agent Tasks and Environments》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EnvBench, FeatureBench, R2E-Gym, SWE-Bench, SWE-Gym, SWT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling coding agents requires a continuing supply of executable data for training, benchmarking, and continuous evaluation. Each task must couple a realistic software state with a specification, development tools, and reliable verification. To expand this supply, we present Change2Task, a system grounded in repository history that converts merged pull requests into verified tasks on healthy modern revisions of the same repository. It aligns historical evidence with evolved code, reconstructs task states through Patch Reversal, Code Mapping, or Agent Reconstruction, and validates the lifecycle from a healthy base to a task state and a restored state. By deriving multiple tasks grounded in developer evidence from maintained environments, Change2Task provides executable data for coding agent training and evaluation while reducing repeated environment setup, storage, and task construction effort. We evaluate the system through five common and widely adopted coding agent task families: Bug Fix, Feature Addition, Test Generation, Application Programming Interface Migration, and Security Repair. Starting from 1,130 source changes eligible for construction, Change2Task achieves 79.6% verified task construction success across these task families. On a matched candidate set, it recovers 29.2% more verified tasks than a construction baseline based on pull requests. Historical and reconstructed cases achieve up to 98.0% matched outcome agreement under agent evaluation, while reuse of modern bases reduces measured expenditure across the complete pipeline by 10.8%.

</details>

---

### [[20_Research/Papers/大模型/RRM_Experience-Driven_Reflective_Retrieval_Memory_for_Long-Horizon_Multimodal_Reasoning|RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning]]

![[assets/2607.28156_figure.jpg|800]]

- **arXiv**: [2607.28156](https://arxiv.org/abs/2607.28156)
- **PDF**: https://arxiv.org/pdf/2607.28156
- **详细分析**: [[20_Research/Papers/大模型/RRM_Experience-Driven_Reflective_Retrieval_Memory_for_Long-Horizon_Multimodal_Reasoning|RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning]]
- **作者**: Jingxiang Fan, Junbao Zhuo, Bochao Zou
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.85（加权：大模型 0.65，机器人 0.2）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RRM: Experience-Driven Reflective Retrieval Memory for Long-Horizon Multimodal Reasoning》归入 大模型、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：M3-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing multimodal long-term memory agents use external memory to overcome the limited context available for long videos. However, most methods emphasize what to store rather than how stored memory should be retrieved. When retrieval becomes inaccurate or repeatedly fails to obtain useful evidence, existing agents lack mechanisms to diagnose failures from previous task trajectories and adapt future search strategies.We introduce Reflective Retrieval Memory (RRM), a reflective memory framework for long-horizon multimodal reasoning. RRM augments an entity-centric multimodal memory graph with reflective experience memory, which distills transferable procedural retrieval knowledge from historical task trajectories. Unlike episodic and semantic memories that preserve factual evidence from the current video, reflective experience memory captures reusable search strategies across tasks. RRM converts retrieved experiences into query-level guidance, while answer generation remains conditioned only on factual evidence newly retrieved from the current video. A lifecycle management mechanism further regulates experience memory through usage frequency, reuse feedback, and temporal decay, thereby reducing redundancy and noise. RRM consistently outperforms previous state-of-the-art approaches on M3-Bench-Robot, M3-Bench-Web, and Video-MME-Long, demonstrating the effectiveness of reflective retrieval memory for long-horizon multimodal reasoning.

</details>

---

### [[20_Research/Papers/强化学习/FinSMART_Financial_Sentiment_Analysis_for_Algorithmic_Trading_through_Market-Aligned_Reinforcement_Learning|FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning]]

![[assets/2607.28127_figure.png|800]]

- **arXiv**: [2607.28127](https://arxiv.org/abs/2607.28127)
- **PDF**: https://arxiv.org/pdf/2607.28127
- **详细分析**: [[20_Research/Papers/强化学习/FinSMART_Financial_Sentiment_Analysis_for_Algorithmic_Trading_through_Market-Aligned_Reinforcement_Learning|FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning]]
- **作者**: Giorgos Iacovides, Wuyang Zhou, Danilo Mandic
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《FinSMART: Financial Sentiment Analysis for Algorithmic Trading through Market-Aligned Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in Generative AI have substantially improved financial sentiment analysis through post-trained financial large language models (LLMs). However, existing approaches remain confined to a market-agnostic, supervised learning paradigm that relies on limited, static and human-annotated datasets, and thus are incapable of adapting to evolving market conditions. To address this limitation, we introduce FinSMART, the first market-aligned reinforcement learning framework for financial sentiment analysis, which directly optimizes sentiment signals using realized market outcomes. To deal with the noisy, non-stationary, and multifactorial nature of financial markets, FinSMART incorporates a signal extraction pipeline that combines market-aware data filtering with a discrete asymmetric trading reward, enabling stable reinforcement learning from economically meaningful market feedback. Experimental results demonstrate that FinSMART significantly outperforms existing state-of-the-art methods in profitability, risk-adjusted performance, and sentiment signal quality, improving cumulative trading returns by 220% over the strongest baseline. Uniquely, the FinSMART framework naturally supports market-aware retraining, at any point in time, by replacing costly manual annotation with newly observed financial articles and their realized market outcomes. Such a retraining strategy enables the model to continuously adapt to changing market dynamics, resulting in consistent performance gains over its static counterpart. These findings demonstrate the practical applicability of market-aligned reinforcement learning and highlight its potential as a next-generation paradigm for developing adaptive financial LLMs.

</details>

---

### [[20_Research/Papers/大模型/ChronoMem_Version_Control_and_Semantic_Rollback_for_Large_Language_Model_Agent_Memory|ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory]]

![[assets/2607.27773_figure.png|800]]

- **arXiv**: [2607.27773](https://arxiv.org/abs/2607.27773)
- **PDF**: https://arxiv.org/pdf/2607.27773
- **详细分析**: [[20_Research/Papers/大模型/ChronoMem_Version_Control_and_Semantic_Rollback_for_Large_Language_Model_Agent_Memory|ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory]]
- **作者**: Yongye Su, Wujiang Xu, Chaoji Zuo, Elisa Bertino
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《ChronoMem: Version Control and Semantic Rollback for Large Language Model Agent Memory》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on long-term memory to support multi-session interaction and personalization. However, existing agent memory systems are designed around forward-only evolution, continuously accumulating, consolidating, and overwriting knowledge, with no principled mechanism to inspect, version, or revert prior states. This makes agents brittle under corrections, concept drift, and memory corruption, particularly after they have already been exposed to subsequent information. We present ChronoMem, a semantic version-control layer for agentic memory integrated into the production-ready, open-source Agent Development Kit by Google. ChronoMem commits whole-memory snapshots at each memory write, maintains structured version histories, and supports natural-language rollback requests by mapping undo intents to concrete historical versions through hybrid lexical and semantic retrieval, rank fusion, and reranking. We further introduce a post-exposure evaluation protocol that tests whether an agent can behave counterfactually after rollback by answering queries and summarizing history as if future updates had never occurred. On long-horizon conversational benchmarks augmented with evolving memory states and rollback tasks, ChronoMem substantially improves rollback-consistent question answering and history summarization relative to prompt-only and retrieval-only baselines, while achieving strong performance in semantic version selection. To our knowledge, ChronoMem is the first open-source system and benchmark for systematic semantic global memory rollback in LLM agents.

</details>

---

### [[20_Research/Papers/强化学习/Harness-G_A_Graph-Structured_Harness_for_Search_Agents|Harness-G: A Graph-Structured Harness for Search Agents]]

![[assets/2607.27652_figure.png|800]]

- **arXiv**: [2607.27652](https://arxiv.org/abs/2607.27652)
- **PDF**: https://arxiv.org/pdf/2607.27652
- **详细分析**: [[20_Research/Papers/强化学习/Harness-G_A_Graph-Structured_Harness_for_Search_Agents|Harness-G: A Graph-Structured Harness for Search Agents]]
- **作者**: Yanning Hou, Haoyuan Chen, Sihang Zhou, Xiaoshu Chen, Xirui Liu, Duanyang Yuan, Lingyuan Meng, Quan Liu, Jian Huang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Harness-G: A Graph-Structured Harness for Search Agents》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：KGQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) search agents commonly model retrieval as free-form natural-language query generation and optimize multi-turn interactions using final-answer rewards. Current studies mainly improve training with denser or more structured credit signals, but rarely examine whether retrieval is properly formulated at the policy-environment interface. We observe pronounced retrieval aliasing during Search-R1 training: rollouts for the same question continue to generate distinct query strings, yet their accumulated evidence sets increasingly overlap. We call this phenomenon retrieval-equivalence collapse; in this regime, trajectories approach utility equivalence with respect to retrieval decisions, leaving within-group returns with little effective retrieval contrast. To address this problem, we propose Harness-G, a graph-structured retrieval framework that redesigns this interface. It reformulates free-form query generation as finite action selection: the policy selects an evidence sentence or entity, or chooses to answer, while the environment constructs the menu, tracks retrieval state, and validates and executes each choice. This interface reduces linguistic aliasing and makes same-state alternatives directly comparable. Building on this interface, we introduce Structured Non-myopic Credit (SNC), which uses a frozen answer scorer to compare the selected action with its alternatives and assigns downstream gains to the earlier actions that enabled them. Across six QA benchmarks, Harness-G achieves the highest average F1 at both evaluated model scales, outperforming the strongest baseline, Graph-R1, by 10.74 points at 1.5B and 3.98 points at 3B.

</details>

---

### [[20_Research/Papers/大模型/Training_Skills_Like_Parameters_via_Self-Supervised_Semantic_Diffusion|Training Skills Like Parameters via Self-Supervised Semantic Diffusion]]

![[assets/2607.27557_figure.png|800]]

- **arXiv**: [2607.27557](https://arxiv.org/abs/2607.27557)
- **PDF**: https://arxiv.org/pdf/2607.27557
- **详细分析**: [[20_Research/Papers/大模型/Training_Skills_Like_Parameters_via_Self-Supervised_Semantic_Diffusion|Training Skills Like Parameters via Self-Supervised Semantic Diffusion]]
- **作者**: Mo Li, Zixin Yin, Ting Cao, Yunxin Liu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.65（加权：大模型 0.45，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Training Skills Like Parameters via Self-Supervised Semantic Diffusion》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Large Language Models (LLMs) demonstrate remarkable general instruction-following capabilities, they often fall short of human experts in highly specialized, open-ended domains such as creative screenwriting. Prior approaches typically adopt post-training, yet both supervised fine-tuning and reinforcement learning require weight access that closed-source frontier models do not offer, and demand heavy compute. Moreover, what is learned is tied to a single checkpoint and cannot be inspected by humans. Recent advancements in agentic continual learning instead attempt to bridge this gap by accumulating external textual skills. However, these methods heavily rely on costly human expert annotations or unreliable LLM-as-a-judge feedback for reflection. To overcome this bottleneck, we propose a novel, unsupervised self-evolving agent framework inspired by the corruption-and-reconstruction paradigm of diffusion models. Instead of relying on explicit external scoring, we leverage existing high-quality human artifacts to construct self-supervised signals. Training then follows the familiar loop of neural network training, forward, loss, and backward, with the loss coming from contrasting the agent's reconstruction against the human original. What is updated is not model weights but an external library of textual skills. We evaluate our framework on the challenging task of short drama screenwriting. Experimental results demonstrate that our method enables the agent to autonomously extract and internalize highly generalizable skills, significantly enhancing its domain-specific generation capabilities. Furthermore, this self-contrastive reflection paradigm offers a scalable pathway for agents to teach themselves the production of complex, high-quality human artifacts, without requiring external supervision.

</details>

---
