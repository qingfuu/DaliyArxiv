# cs.CL | Computation and Language | 2026-08-07

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/大模型/RRC_Unlocking_Generative_Reward_Models_in_LLM_Reinforcement_Learning_via_Ranking-Based_Reward_Construction|RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction]]

![[assets/2608.06310_figure.png|800]]

- **arXiv**: [2608.06310](https://arxiv.org/abs/2608.06310)
- **PDF**: https://arxiv.org/pdf/2608.06310
- **详细分析**: [[20_Research/Papers/大模型/RRC_Unlocking_Generative_Reward_Models_in_LLM_Reinforcement_Learning_via_Ranking-Based_Reward_Construction|RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction]]
- **作者**: Chenglong Wang, Ziming Zhu, Yifu Huo, Bei Li, Qiaozhi He, Yan Ding, Xiaoyang Hao, Yuxin Gao, Tianhua Zhou, Xiaojia Chang, Tongran Liu, Jingbo Zhu
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.45，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《RRC: Unlocking Generative Reward Models in LLM Reinforcement Learning via Ranking-Based Reward Construction》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：JudgeBench, RM-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in reward modeling show a paradigm shift from discriminative reward models to generative reward models. However, despite their strong capabilities in response ranking, generative reward models have not realized their potential in reinforcement learning (RL). Our analysis reveals that this limitation arises from a mismatch between the comparative nature of generative reward modeling and the scalar scoring paradigm adopted by existing RL algorithms. To bridge this gap, we propose a Ranking-based Reward Construction (RRC) approach, which enables generative reward models to provide more effective RL learning signals by deriving rewards from relative preference rankings. RRC introduces two complementary strategies: self-competitive ranking, which exploits comparisons among sampled responses, and anchor-guided ranking, which enables scalable ranking-based reward construction with a small set of reference responses. Experiments across open-ended chat and reasoning benchmarks demonstrate that RRC substantially improves RL training with generative reward models, achieving consistent gains over existing reward construction approaches. Our code can be found at https://github.com/wangclnlp/RRC.

</details>

---

### [[20_Research/Papers/大模型/NeSy-RAG_Neuro-Symbolic_RAG_for_Explainable_Question_Answering|NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering]]

![[assets/2608.06292_figure.png|800]]

- **arXiv**: [2608.06292](https://arxiv.org/abs/2608.06292)
- **PDF**: https://arxiv.org/pdf/2608.06292
- **详细分析**: [[20_Research/Papers/大模型/NeSy-RAG_Neuro-Symbolic_RAG_for_Explainable_Question_Answering|NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering]]
- **作者**: Jonas Gann, Michael Gertz
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《NeSy-RAG: Neuro-Symbolic RAG for Explainable Question Answering》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) improves question answering by grounding large language models (LLMs) in external knowledge such as text corpora. However, its reasoning process remains largely opaque: intermediate reasoning steps are difficult to verify and cannot be reliably attributed to specific evidence. Moreover, missing user-specific context is rarely detected systematically, often leading to incomplete or incorrect output. We propose NeSy-RAG, a modular neuro-symbolic RAG framework that synthesizes attributable Prolog modules from retrieved text chunks. For each chunk, the system generates semantically meaningful predicates that encode Boolean claims, which may depend on user facts. Using joint natural language-code embeddings, predicates are retrieved and composed into Prolog queries. To address incomplete user context, we introduce a symbolic knowledge-gap detection mechanism that identifies missing user facts whose truth values affect the query outcome and automatically triggers follow-up interactions. Executing the resulting Prolog queries yields deterministic answers together with transparent execution traces that link each reasoning step to its originating source. On the ShARC benchmark, without domain-specific training, NeSy-RAG achieves 61.1% accuracy, outperforming a same-model RAG baseline that achieves 42.8% accuracy.

</details>

---

### [[20_Research/Papers/大模型/Routing_Is_Least_Learnable_Where_It_Is_Most_Valuable_Bounds_on_Representation_Routing_for_Web_Agents|Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents]]

![[assets/2608.06171_figure.png|800]]

- **arXiv**: [2608.06171](https://arxiv.org/abs/2608.06171)
- **PDF**: https://arxiv.org/pdf/2608.06171
- **详细分析**: [[20_Research/Papers/大模型/Routing_Is_Least_Learnable_Where_It_Is_Most_Valuable_Bounds_on_Representation_Routing_for_Web_Agents|Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents]]
- **作者**: Jiaming Wei, Zekun Wu, Adriano Koshiyama, Maria Perez-Ortiz
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Routing Is Least Learnable Where It Is Most Valuable: Bounds on Representation Routing for Web Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web agents observe a browser through text, pixels, or both, and the choice is usually fixed once for all tasks. We measure six observation modes across eight site-model combinations (cells) on VisualWebArena and WebArena and ask what choosing per task would buy. The modes are complementary: each solves tasks the others miss, they fail in structurally different ways, and the best choice reverses between task sets. The obvious prize, an oracle that picks a winning mode for every task, looks large but is inflated by run-to-run noise: rerunning the same mode on the same tasks changes 12-14% of outcomes, so a second run of a mode already in hand gains about as much as adding a new one. What survives is a cost bound: sending only the tasks no mode solves to the cheapest mode cuts cost by 9.5-30.6% in 8 of 8 cells at unchanged success. We then test five routing policies (picking the mode, deciding when to spend on the strong mode, a zero-cost rule read off the task text, a confidence cascade, and pooled cost tiers), and none robustly beats simply fixing one well-chosen mode; the one exception is a fragile result in our sparsest cell. The central obstruction is that routing supervision is produced at the agent's success rate: the weaker the agent, the fewer labels a router gets, exactly where routing would be most valuable. This limit belongs to today's agents rather than to routing itself. Label supply and routing opportunity rise together (correlation 0.95 across cells), so a stronger agent can overturn the result, and we report the rerun noise bands and the full measurement protocol.

</details>

---

### [[20_Research/Papers/大模型/Causal_Episodic_Memory_for_Feedback-Driven_Agent_Repair|Causal Episodic Memory for Feedback-Driven Agent Repair]]

![[assets/2608.05906_figure.png|800]]

- **arXiv**: [2608.05906](https://arxiv.org/abs/2608.05906)
- **PDF**: https://arxiv.org/pdf/2608.05906
- **详细分析**: [[20_Research/Papers/大模型/Causal_Episodic_Memory_for_Feedback-Driven_Agent_Repair|Causal Episodic Memory for Feedback-Driven Agent Repair]]
- **作者**: Khang Nhat Hoang Vo, Tam Minh Chu, Anh Trac Duc Dinh, Thuyen Vinh Ha Bui, Tho Quan
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Causal Episodic Memory for Feedback-Driven Agent Repair》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents that repair failures often discard successful corrections, forcing later episodes to rediscover similar solutions. We study whether finalized repair outcomes can improve subsequent Text-to-SQL episodes without parameter updates. We introduce MERIT, a training-free agent that maintains an online dual-polarity memory of oracle-verified corrections and observed unsuccessful directions. Under oracle-assisted benchmark feedback, only memories from earlier finalized episodes are eligible for retrieval. A deterministic classifier assigns a coarse failure type, which conditions a hybrid lexical-dense retriever before the frozen model generates each revision. Using Qwen2.5-7B-Instruct with identical initial predictions and repair budgets, MERIT improves execution accuracy over stateless iterative repair from \(66.34\%\) to \(69.79\%\) on Spider and from \(47.35\%\) to \(48.44\%\) on BIRD. Paired analyses provide clear evidence for the Spider gain but weaker evidence on BIRD. MERIT is not reliably separated from untyped dynamic retrieval on either benchmark, while Reflexion-style memory reaches \(51.24\%\) on BIRD at substantially higher inference cost. Ablations show that negative memory contributes modestly, the value of type conditioning and lexical--dense ranking is dataset dependent, and schema-local experience provides the most consistent benefit. These results clarify when causal cross-query memory improves repair and when broader memory representations remain preferable.

</details>

---

### [[20_Research/Papers/大模型/M$^3$R-Bench_A_Unified_Benchmark_for_Evidence-Grounded_Multimodal_Metaphor_Understanding|M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding]]

![[assets/2608.05817_figure.png|800]]

- **arXiv**: [2608.05817](https://arxiv.org/abs/2608.05817)
- **PDF**: https://arxiv.org/pdf/2608.05817
- **详细分析**: [[20_Research/Papers/大模型/M$^3$R-Bench_A_Unified_Benchmark_for_Evidence-Grounded_Multimodal_Metaphor_Understanding|M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding]]
- **作者**: Hong Jiang, Junnan Zhu, Jingwang Huang, Xiao Sun, Yuming Yang, Jiang Zhong, Ruirui Chen, Jingman Shi, Hao Wu, Nayu Liu, Xinyi Jiang, Kaiwen Wei
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《M$^3$R-Bench: A Unified Benchmark for Evidence-Grounded Multimodal Metaphor Understanding》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CII-Bench, M3R-Bench, R-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Metaphor enables the understanding of abstract concepts through cross-domain mappings while conveying affective attitudes. In multimodal scenarios, visual and textual information jointly construct Target--Source mappings, requiring both conceptual understanding and cross-modal reasoning. However, existing benchmarks mainly evaluate metaphor understanding through isolated subtasks and lack evidence-grounded explanations, making it difficult to assess whether models establish mappings grounded in visual and textual cues.To address these limitations, we introduce M$^3$R-Bench, a unified and evidence-grounded benchmark containing 1,000 image--text instances with human-verified annotations. Guided by Conceptual Metaphor Theory and theories of nonliteral language understanding, M$^3$R-Bench provides joint annotations for metaphor occurrence, Target--Source mapping, sentiment, and stage-wise explanations following ``evidence identification--mapping establishment--sentiment inference.''Evaluations on M$^3$R-Bench reveal that existing models often overlook visual evidence, rely on superficial textual cues, and produce inaccurate Target--Source mappings, exposing a cross-modal evidence--mapping mismatch. To address this mismatch, we propose M$^3$R-Reasoner, which combines curriculum-based reasoning supervision with task-aware reinforcement learning to align model reasoning with metaphor interpretation. Experiments show that, with only an 8B-parameter backbone, M$^3$R-Reasoner outperforms larger proprietary MLLMs across four unified-task metrics and improves Visual Evidence and Sentiment Justification scores over GPT-5.5 by 28.45 and 30.11 points, respectively, while surpassing Claude-Sonnet-4.6 by 8.00 points in mean rubric score. The dataset and code are available at https://github.com/hongshi4/M3R-Bench.

</details>

---

### [[20_Research/Papers/大模型/On-Policy_Delta_Distillation_for_Multilingual_Math_Reasoning|On-Policy Delta Distillation for Multilingual Math Reasoning]]

![[assets/2608.05802_figure.png|800]]

- **arXiv**: [2608.05802](https://arxiv.org/abs/2608.05802)
- **PDF**: https://arxiv.org/pdf/2608.05802
- **详细分析**: [[20_Research/Papers/大模型/On-Policy_Delta_Distillation_for_Multilingual_Math_Reasoning|On-Policy Delta Distillation for Multilingual Math Reasoning]]
- **作者**: Byeongho Heo, Jaehui Hwang, Sangdoo Yun, Dongyoon Han
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《On-Policy Delta Distillation for Multilingual Math Reasoning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-Policy Distillation (OPD) is emerging as a promising alternative to reinforcement learning for LLM post-training, yet its effectiveness in multilingual settings remains underexplored. We study OPD and its advanced variant, On-Policy Delta Distillation (OPD$^2$), for mathematical reasoning in English, Korean, and Japanese. OPD$^2$ improves OPD by using the probability gap between a post-trained teacher and its base model as the learning signal. Experiments with Qwen3 show that OPD$^2$ consistently outperforms the original OPD, with particularly strong improvements in Korean and Japanese, and generally narrows the English-Korean performance gap. We further find that English-only OPD can also increase performance for Korean and Japanese, but often shifts the responses toward English, highlighting the importance of multilingual data to preserving target-language responses.

</details>

---

### [[20_Research/Papers/大模型/EvoHarness-RL_Learning_Self-Evolving_Runtime_Harness_for_Long-Horizon_LLM_Agents|EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents]]

![[assets/2608.05446_figure.png|800]]

- **arXiv**: [2608.05446](https://arxiv.org/abs/2608.05446)
- **PDF**: https://arxiv.org/pdf/2608.05446
- **详细分析**: [[20_Research/Papers/大模型/EvoHarness-RL_Learning_Self-Evolving_Runtime_Harness_for_Long-Horizon_LLM_Agents|EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents]]
- **作者**: Xuying Ning, Dongqi Fu, Tianxin Wei, Hanqing Zeng, Yuanchen Bei, Bingxuan Li, Zihao Li, Qifan Wang, Xiang Shen, Yifan Wu, Jiayi Liu, Hong Li...
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《EvoHarness-RL: Learning Self-Evolving Runtime Harness for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, EvoHarness-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents increasingly rely on external execution support to maintain state, track progress, invoke tools, verify outcomes, and reuse experience across interactions. However, effective harness use raises two coupled challenges: state formation from noisy interaction traces and runtime control over external-state access. Existing agents usually handle both through prompts, heuristics, or domain-specific conventions, leaving the external workspace and its usage policy manually engineered. To address this, we study the problem of harness policy learning, where agents learn harness policies offline and deploy them to construct and update external harness state online during runtime task execution. We introduce EvoHarness-RL, which exposes Belief, Progress, and Experience (BPE) as policy-facing harness state. Supervised harness fine-tuning teaches the base agent the harness action space and how to construct useful external state, while cost-aware GRPO explores coordination policies to selectively read, update, and consolidate that state during long-horizon interaction. Instantiated on ALFWorld with a Qwen3-8B LLM, EvoHarness-RL reaches 96.9% success and reveals two key dynamics: harness annealing, where training internalizes recurring harness-use patterns into the model policy and shifts the agent from frequent harness calls toward selective external-state access, and harness evolution, where progress updates and experience consolidation refine the harness into a compact, task-adaptive state substrate. These results suggest that long-horizon agents benefit from trainable policies for constructing and coordinating with external harness workspaces, beyond simply adding stronger tools or larger memories.

</details>

---

### [[20_Research/Papers/大模型/Where_Privacy_Risk_Lives_in_English-Source_Multilingual_RAG_A_Stage-Decomposed_Audit_Across_Five_Query_Languages|Where Privacy Risk Lives in English-Source Multilingual RAG: A Stage-Decomposed Audit Across Five Query Languages]]

![[assets/2608.05163_figure.png|800]]

- **arXiv**: [2608.05163](https://arxiv.org/abs/2608.05163)
- **PDF**: https://arxiv.org/pdf/2608.05163
- **详细分析**: [[20_Research/Papers/大模型/Where_Privacy_Risk_Lives_in_English-Source_Multilingual_RAG_A_Stage-Decomposed_Audit_Across_Five_Query_Languages|Where Privacy Risk Lives in English-Source Multilingual RAG: A Stage-Decomposed Audit Across Five Query Languages]]
- **作者**: Yanhang Li, Zhichao Fan, Zexin Zhuang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《Where Privacy Risk Lives in English-Source Multilingual RAG: A Stage-Decomposed Audit Across Five Query Languages》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A common assumption holds that switching to a non-English language makes a multilingual RAG system easier to attack for personal information. We test this on an English-source synthetic-PII corpus with five query languages and a two-stage defence (LLM input judge + regex output filter), in a pipeline whose translator, judge, back-translator, and generator are all Qwen2.5-7B -- so every finding below is pipeline-conditional, not a causal ranking of language-inherent risk. Under output-only filtering, English has the highest observed unstructured-PII leak rate; only English-vs-Swahili separates cleanly under document-level bootstrap intervals. Once the input judge is added, residual leaks remain on Arabic and Swahili, and back-translating the query does not close the gap (an ablation we report but cannot use as a causal diagnostic, since the back-translator is also Qwen). On a separate n=17 multilingual-prompted-judge residual corner, attaching the gold corpus document to the input judge blocks 15/17 residual cells. We frame this last result as a mechanism diagnostic, not a deployable defence: it uses oracle retrieval, BLOCK/ALLOW rates are measured on adversarial queries only, and we measure no benign-query false-positive rate and no answer-utility cost. The supplementary material contains code, corpora, queries, and per-trial JSONLs; the priority follow-up is an independent-MT plus non-Qwen-judge replication with a native-speaker query set, scoped in the Limitations section.

</details>

---
