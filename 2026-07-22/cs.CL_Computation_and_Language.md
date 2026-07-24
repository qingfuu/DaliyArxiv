# cs.CL | Computation and Language | 2026-07-22

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/大模型/Selective_State-Space_Adaptation_and_Retrieval_for_Language_Model_Reasoning|Selective State-Space Adaptation and Retrieval for Language Model Reasoning]]

![[assets/2607.19326_figure.png|800]]

- **arXiv**: [2607.19326](https://arxiv.org/abs/2607.19326)
- **PDF**: https://arxiv.org/pdf/2607.19326
- **详细分析**: [[20_Research/Papers/大模型/Selective_State-Space_Adaptation_and_Retrieval_for_Language_Model_Reasoning|Selective State-Space Adaptation and Retrieval for Language Model Reasoning]]
- **作者**: Atahan Dokme, Larry Heck
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Selective State-Space Adaptation and Retrieval for Language Model Reasoning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-rank adaptation introduces a static learned update applied identically to every input. The update provides task-level adaptation but does not explicitly represent token-level or instance-level state variation. A family of adapters is proposed that introduces selective state-space recurrence at two complementary granularities. At the token level, \textbf{MaLoRA} (Mamba-modulated low-rank adaptation) makes the adapter's scaling factor a dynamic input-dependent function with recurrent state across tokens, in contrast to the stateless modulators of prior work. At the context level, \textbf{MaRA} (Mamba Retrieval Adapter) tracks cross-segment state and selects the segments most relevant to the query, before the modulated language model generates its answer. Across three frozen backbones (Qwen-2.5-7B, Llama-3.1-8B, Gemma-2-9B) and two reasoning benchmarks (MuSiQue, 2WikiMultihopQA), the family improves reasoning accuracy on every cell of the $3{\times}2$ grid, by $+6.8$ F1 ($+10.5\%$ relative) on average and up to $+9.3$ F1 ($+18.2\%$ relative) on the hardest cell over the LoRA baseline, and the token-level gains carry to RULER QA-2 under length stress.

</details>

---

### [[20_Research/Papers/大模型/MeetingToM_Evaluating_Multimodal_LLMs_on_Theory-of-Mind_Reasoning_in_Multi-Party_Meetings|MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party Meetings]]

![[assets/2607.19235_figure.png|800]]

- **arXiv**: [2607.19235](https://arxiv.org/abs/2607.19235)
- **PDF**: https://arxiv.org/pdf/2607.19235
- **详细分析**: [[20_Research/Papers/大模型/MeetingToM_Evaluating_Multimodal_LLMs_on_Theory-of-Mind_Reasoning_in_Multi-Party_Meetings|MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party Meetings]]
- **作者**: Ziyi Wang, Yuhang Wu, Dongxu Piao, Xingyu Liu, Tianhui Zhou, Miao Liu
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《MeetingToM: Evaluating Multimodal LLMs on Theory-of-Mind Reasoning in Multi-Party Meetings》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：SIV-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Theory of Mind (ToM), the ability to infer other's beliefs, intentions, and states of knowledge, is central to social interaction, yet remains challenging for current Multimodal Large Language Models (MLLMs), especially in multi-party meetings where cues are distributed across speech and behavior. Existing multimodal ToM benchmarks mainly focus on video-grounded question answering over overt, externally verifiable signals, and provide limited coverage of latent social states and group dynamics. We introduce MeetingToM, a benchmark for complex social behavior reasoning in naturalistic multi-party meetings. MeetingToM targets meeting-specific phenomena such as \textbf{pseudo-consensus}, where apparent agreement masks private dissent under social pressure. The benchmark is hierarchically organized to evaluate ToM at increasing levels of social granularity, including (i) subject-level mental state prediction, (ii) dyadic-level addressee understanding, and (iii) group-level consensus reasoning. We provide a unified evaluation protocol and conduct systematic analyses of representative MLLMs, revealing persistent limitations in integrating non-verbal cues, inferring hidden attitudes, and distinguishing genuine consensus from pseudo-consensus. Our results highlight key challenges and establish MeetingToM as a testbed for advancing meeting-grounded ToM in multimodal models.

</details>

---

### [[20_Research/Papers/大模型/Reasoning_Error_from_Known_Fact_Step-Level_Self-Consistency_Group_Relative_Policy_Optimization_for_LLM|Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM]]

![[assets/2607.18915_figure.png|800]]

- **arXiv**: [2607.18915](https://arxiv.org/abs/2607.18915)
- **PDF**: https://arxiv.org/pdf/2607.18915
- **详细分析**: [[20_Research/Papers/大模型/Reasoning_Error_from_Known_Fact_Step-Level_Self-Consistency_Group_Relative_Policy_Optimization_for_LLM|Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM]]
- **作者**: Xiaomeng Hu, Jiaqi Hu, Hao Chen, Qi Zhang, Zhanming Shen, Wentao Ye, Junbo Zhao
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.55，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Reasoning Error from Known Fact: Step-Level Self-Consistency Group Relative Policy Optimization for LLM》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TruthRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid advancement of large language models (LLMs), modern systems not only possess strong foundational capabilities and extensive knowledge, but can also solve complex problems via long, multi-step reasoning. However, as reasoning traces become longer, LLMs may produce a substantial amount of hallucinated content during the reasoning process, which is often difficult to detect. In this work, we conduct a fine-grained analysis of hallucinations arising in LLM reasoning and find that the reasoning traces are particularly prone to Context-Sensitive Factual Hallucinations: cases where the model actually has the relevant knowledge, yet makes factual errors due to contextual interference during reasoning. To address this issue, we propose Step-level Self-Consistency Group Relative Policy Optimization (SSC-GRPO), which assigns step-level rewards to reasoning traces by computing self-consistency scores of individual steps across multiple rollouts. Compared with prior methods, SSC-GRPO achieves state-of-the-art performance on both mathematical reasoning benchmarks and hallucination leaderboards. Our results offer a new perspective for detecting and mitigating hallucinations in the reasoning process of large language models.

</details>

---

### [[20_Research/Papers/大模型/HindsightBench_A_Black-Box_Behavioral_Audit_Protocol_for_Parametric_Hindsight_in_Time-Indexed_LLM_Decision_Tasks|HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks]]

![[assets/2607.18867_figure.png|800]]

- **arXiv**: [2607.18867](https://arxiv.org/abs/2607.18867)
- **PDF**: https://arxiv.org/pdf/2607.18867
- **详细分析**: [[20_Research/Papers/大模型/HindsightBench_A_Black-Box_Behavioral_Audit_Protocol_for_Parametric_Hindsight_in_Time-Indexed_LLM_Decision_Tasks|HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks]]
- **作者**: Haozhe Jia
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《HindsightBench: A Black-Box Behavioral Audit Protocol for Parametric Hindsight in Time-Indexed LLM Decision Tasks》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CutoffBench, HindsightBench, LLMLagBench, Look-Ahead-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models leak parametric knowledge of realized outcomes into historical financial decision tasks. Existence is settled; what users lack is a cheap way to audit a given model for it. We present HindsightBench, a black-box behavioral audit protocol that profiles parametric hindsight in any time-indexed LLM decision task at probe-level cost (no backtests, no logprobs, no corpus access). The protocol chains a four-arm date-manipulation matrix (revealed/date-only/masked/transplanted), dual memory probes (date recovery; outcome recall), and six per-model metrics -- trigger strength, transplant effect, post-cutoff placebo, recoverability, behaviorally effective knowledge cutoff, and a recall-accuracy dissociation coefficient -- with explicit gates where identifiability is data-dependent. Applying it to 15 models from seven vendors on a 258-node vintage-correct macro panel yields three headline patterns: (i) the date-trigger reflex tracks training generation, not scale -- absent across the 2024 open-weight generation from 1B to 70B, present in every tested 2026-generation model, and switching on within one vendor lineage (Qwen3 -&gt; Qwen3.6) at fixed MoE architecture and 3B active parameters; (ii) effective cutoffs span 22 months across vendors and precede vendor-reported dates by up to eight months, invalidating calendar-window placebo designs; (iii) audit results are not invariant to serving -- BF16 serving of an FP8-referenced model breaks the trigger estimate's stability while AWQ-INT4 preserves it, and a provider-locked reasoning regime makes one probe non-convergent -- so the protocol ships with operational requirements (pin quantization and thinking regime; disclose parser and sampling policy). We release the panel, frozen preregistrations, per-model audit rows with measured dollar costs, transcripts, and one-command regeneration.

</details>

---

### [[20_Research/Papers/大模型/RF-Agent_A_Practical_Framework_for_Building_Language_Agents_for_RFIC_Design|RF-Agent: A Practical Framework for Building Language Agents for RFIC Design]]

![[assets/2607.18772_figure.png|800]]

- **arXiv**: [2607.18772](https://arxiv.org/abs/2607.18772)
- **PDF**: https://arxiv.org/pdf/2607.18772
- **详细分析**: [[20_Research/Papers/大模型/RF-Agent_A_Practical_Framework_for_Building_Language_Agents_for_RFIC_Design|RF-Agent: A Practical Framework for Building Language Agents for RFIC Design]]
- **作者**: Yueqi Xing, Houbo He, Jolie Wang, Erin Ni, Shikai Wang, Qiufeng Li, Weidong Cao, Taiyun Chi
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《RF-Agent: A Practical Framework for Building Language Agents for RFIC Design》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have driven rapid progress in electronic design automation (EDA), yet their application to radio-frequency (RF) circuit design remains limited by the scarcity of domain-specific datasets and standardized benchmarks. We present RF-Agent, which addresses this gap through textbook-driven knowledge distillation. A multi-agent Question-Thinking-Solution-Answer (QTSA) pipeline converts a subsection-level corpus from seven canonical RF textbooks into the first-of-its-kind RF-domain reasoning dataset (over 11,000 samples) with a dedicated multiple-choice benchmark. On this benchmark we study two adaptation strategies: supervised fine-tuning (SFT) and three retrieval-augmented generation (RAG) configurations (semantic, keyword, hybrid). Across multiple LLM families, domain-specific SFT significantly improves RF reasoning, especially for small and medium-sized models; among RAG configurations, semantic retrieval performs best, indicating embedding-based context alignment suits RF reasoning better than naive fusion. The dataset and benchmark provide a reusable foundation for future work on LLM-aided RF circuit design.

</details>

---

### [[20_Research/Papers/强化学习/Stale_but_Stable_Staleness-Adaptive_Trust_Regions_for_Stabilizing_Asynchronous_Reinforcement_Learning|Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning]]

![[assets/2607.18722_first_page.png|800]]

- **arXiv**: [2607.18722](https://arxiv.org/abs/2607.18722)
- **PDF**: https://arxiv.org/pdf/2607.18722
- **详细分析**: [[20_Research/Papers/强化学习/Stale_but_Stable_Staleness-Adaptive_Trust_Regions_for_Stabilizing_Asynchronous_Reinforcement_Learning|Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning]]
- **作者**: Junyao Yang, Yucheng Shi, Zongxia Li, Zhongzhi Li, Ruhan Wang, Xiangxin Zhou, Kishan Panaganti, Haitao Mi, Leowei Liang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Stale but Stable: Staleness-Adaptive Trust Regions for Stabilizing Asynchronous Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Asynchronous reinforcement learning improves throughput by decoupling rollout generation from optimization, but staleness is an inevitable byproduct compounded by policy lag, engine delays, and mixture-of-experts routing. From a trust-region perspective, this mismatch is critical: training-inference divergence governs approximation error in finite-horizon bounds, whereas PPO clipping only gates sampled outward updates, acting as a sampled surrogate rather than a full-policy constraint. As a result, high-staleness updates remain weakly controlled in the asynchronous regime where stale rollouts matter most. We introduce the Staleness-Adaptive Trust Region (SAT), which uses the detached sampled log-ratio as a practical staleness proxy, identifies high-mismatch tails within each batch via staleness-based kernel scaling, and contracts only the sign-selected endpoint of the nominal PPO interval. This preserves baseline behavior on ordinary tokens while enforcing more conservative updates on newly intercepted outward bands. We prove local interval containment and pointwise pessimism relative to PPO, showing how the adaptive rule reshapes update geometry under heterogeneous staleness. We evaluate SAT in a decoupled asynchronous RL setup built on Qwen3-30B-A3B-Base, using SGLang as the inference engine and Megatron for training. In this setting, SAT-GSPO w/ R3 achieves the best observed AIME24 avg@8, reaching 35.83 at lag 1 and 34.79 at lag 8, while SAT-GSPO reaches 34.17 at lag 1. Adaptive clipping and routing replay act as complementary stabilizers targeting mismatch tails and routing inconsistency, respectively. Overall, aligning clip intervals with staleness heterogeneity effectively stabilizes asynchronous RL.

</details>

---

### [[20_Research/Papers/大模型/Stochastic_Meta-Unlearning_Bridging_Language_Backbone_and_Multimodal_Unlearning|Stochastic Meta-Unlearning: Bridging Language Backbone and Multimodal Unlearning]]

![[assets/2607.18615_figure.png|800]]

- **arXiv**: [2607.18615](https://arxiv.org/abs/2607.18615)
- **PDF**: https://arxiv.org/pdf/2607.18615
- **详细分析**: [[20_Research/Papers/大模型/Stochastic_Meta-Unlearning_Bridging_Language_Backbone_and_Multimodal_Unlearning|Stochastic Meta-Unlearning: Bridging Language Backbone and Multimodal Unlearning]]
- **作者**: Zijie Liu, Jinhao Duan, Gaowen Liu, Sijia Liu, Tianlong Chen
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Stochastic Meta-Unlearning: Bridging Language Backbone and Multimodal Unlearning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FIUBench, MLLMU-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Machine unlearning for vision-language models (VLMs) remains underexplored. Unlike language models, VLMs combine a language backbone with visual components, which makes unlearning more complex. There is a surprising phenomenon when moving from single-modality unlearning to VLM unlearning: a target forgotten by the standalone language backbone can still be recovered when image information is given to the full VLM. This shows that text-only feedback is not enough for reliable VLM unlearning. Motivated by this observation, we propose Stochastic Meta-Unlearning (SMU), a bilevel framework that uses VLM-level feedback to learn an unlearning-ready initialization. In the inner loop, SMU applies a few unlearning steps to the language backbone using text data. In the outer loop, SMU recomposes the updated backbone with the frozen VLM and evaluates forgetting and utility at the VLM level. This design makes the unlearning update aware of the final multimodal behavior, while still keeping the update local to the language backbone. Experiments on two VLMs, two multimodal meme datasets, and three baselines show that SMU achieves the best overall forget-retain trade-off. Compared with the strongest baseline for each metric, SMU reduces average Forget accuracy by 10.52 points and improves average Retain and Test accuracy by 20.10 and 17.01 points, respectively. More importantly, SMU also transfers to new forgetting targets and to different meta-test unlearning methods. These results suggest that VLM-level feedback can make language-backbone unlearning more reliable and more transferable for VLMs.

</details>

---

### [[20_Research/Papers/具身智能/Search-on-Graph-R1_Training_Large_Language_Models_to_Search_Knowledge_Graphs_with_Reinforcement_Learning|Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning]]

![[assets/2607.18481_figure.png|800]]

- **arXiv**: [2607.18481](https://arxiv.org/abs/2607.18481)
- **PDF**: https://arxiv.org/pdf/2607.18481
- **详细分析**: [[20_Research/Papers/具身智能/Search-on-Graph-R1_Training_Large_Language_Models_to_Search_Knowledge_Graphs_with_Reinforcement_Learning|Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning]]
- **作者**: Jia Ao Sun, Hao Yu, Fengran Mo, Zhan Su, Yuchen Hui, Bang Liu, Jian-Yun Nie
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.05（加权：大模型 0.25，强化学习 0.8）
- **关联关键词**: LLM, EmbodiedAI, RL

#### 研究背景与动机

《Search-on-Graph-R1: Training Large Language Models to Search Knowledge Graphs with Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GrailQA, KGQA, Rule-KBQA, SFT-then-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge graph question answering (KGQA) requires navigating from topic entities to an answer several relations away. Recent methods prompt a frontier LLM to explore the graph through a retrieval tool, but their reliance on frontier-scale inference makes them costly to deploy. We present Search-on-Graph-R1 (\sogrone{}), which internalizes this navigation into a compact 8B model through supervised fine-tuning (SFT) followed by reinforcement learning (RL). Our central idea is to scaffold a frontier teacher with each question's gold SPARQL query, so the teacher traverses a known answer-bearing path with a live \texttt{Search} tool rather than having to discover the path itself. Since every call executes against a live Freebase server, the resulting trajectories are grounded in the knowledge graph by construction. On WebQSP, CWQ, and GrailQA, \sogrone{} at 8B surpasses every frozen frontier-LLM system in our comparison and posts the strongest results on CWQ of any system we compare against. It does so using no auxiliary module at inference and no LLM judge during training. Isolating each training stage shows that SFT and RL contribute complementary gains, our approach transfers across model families, and RL learns to reach answers in fewer \texttt{Search} calls than its SFT initialization.

</details>

---
