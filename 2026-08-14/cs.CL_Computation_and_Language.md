# cs.CL | Computation and Language | 2026-08-14

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/大模型/Measuring_Task-Agnostic_Training_Data_Influence_Across_Language_Model_Pretraining|Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining]]

![[assets/2608.13515_figure.png|800]]

- **arXiv**: [2608.13515](https://arxiv.org/abs/2608.13515)
- **PDF**: https://arxiv.org/pdf/2608.13515
- **详细分析**: [[20_Research/Papers/大模型/Measuring_Task-Agnostic_Training_Data_Influence_Across_Language_Model_Pretraining|Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining]]
- **作者**: Yuto Nishida, Hirokazu Kiyomaru, Yusuke Oda, Takashi Kodama, Chaoran Liu, Daisuke Kawahara, Yusuke Miyao, Max Müller-Eberstein, Masaru Isonuma
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Measuring Task-Agnostic Training Data Influence Across Language Model Pretraining》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Measuring training data influence consistently across language model pretraining is challenging. It is difficult to select downstream tasks or validation sets representative of a model's general capabilities, and reliance on task performance at intermediate checkpoints complicates comparisons across training. We propose a measure of training data influence that does not require selecting a downstream task or validation set as the attribution target. Specifically, we define an example's influence by how much its gradient update reduces the squared distance to the final parameters of a given pretraining run, and estimate this quantity from intermediate checkpoints without retraining. Applying the method to 18 configurations from the Pythia and PolyPythia suites, we find systematic temporal changes in influential data. Early in training, literature-related data are more strongly aligned with the trajectory toward the final parameters, whereas STEM data become more strongly aligned in later stages. This qualitative crossover is broadly consistent across model configurations. Our results provide a tractable trajectory-level view of how influential data change throughout pretraining, complementing influence analyses defined with respect to specific downstream tasks or validation sets.

</details>

---

### [[20_Research/Papers/大模型/Intern-S2-Preview_Scientific_Agentic_Foundation_Model|Intern-S2-Preview: Scientific Agentic Foundation Model]]

![[assets/2608.13505_figure.png|800]]

- **arXiv**: [2608.13505](https://arxiv.org/abs/2608.13505)
- **PDF**: https://arxiv.org/pdf/2608.13505
- **详细分析**: [[20_Research/Papers/大模型/Intern-S2-Preview_Scientific_Agentic_Foundation_Model|Intern-S2-Preview: Scientific Agentic Foundation Model]]
- **作者**: Lei Bai, Jiaqi Cao, Chiyu Chen, Guanzhou Chen, Kai Chen, Guangran Cheng, Erfei Cui, Xuanlang Dai, Shengyuan Ding, Shangheng Du, Yanhui Duan, Yue Fan...
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Intern-S2-Preview: Scientific Agentic Foundation Model》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scientific discovery increasingly requires AI systems that can reason over scientific evidence of heterogeneous modalities, interact with scientific tools and environments, and sustain progress across long task horizons. We present Intern-S2-Preview, a series of scientific agentic foundation models designed to support multimodal scientific understanding, reasoning, generation, and long-horizon tasks. The training pipeline begins with scientific multimodal pre-training over rendered scientific documents, interleaved image-text data, and diverse scientific corpora. Starting from the pretrained checkpoint, we apply a unified post-training pipeline consisting of supervised fine-tuning, scalable multi-task reinforcement learning (RL), black- and white-box agentic RL, and on-policy distillation. This pipeline is supported by practical techniques that improve rollout and training stability and efficiency, including partial rollout with off-policy correction, adaptive length regularization, online speculative decoding, robust multi-task optimization, and trace-aware experience assembly for agentic tasks. At the architecture level, Intern-S2-Preview-397B extends time series modelling from efficient long-sequence understanding to numerical forecasting, while Memory Decoder is studied as a separate memory-augmented path for rapid scientific specialization without modifying the frozen 397B backbone. Evaluations across scientific, multimodal, agentic, and general-purpose benchmarks show that Intern-S2-Preview-397B achieves competitive or leading results in multiple settings. The time series modules improve scientific signal understanding and forecasting on SciTS, while the separate Intern-MemDec-4B extension improves the Biology-Instructions average score from 56.92 to 60.32 without modifying the frozen 397B backbone.

</details>

---

### [[20_Research/Papers/大模型/RippleMem_From_Isolated_Retrieval_to_Associative_Recollection_for_Long-Term_Agent_Memory|RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory]]

![[assets/2608.13334_figure.png|800]]

- **arXiv**: [2608.13334](https://arxiv.org/abs/2608.13334)
- **PDF**: https://arxiv.org/pdf/2608.13334
- **详细分析**: [[20_Research/Papers/大模型/RippleMem_From_Isolated_Retrieval_to_Associative_Recollection_for_Long-Term_Agent_Memory|RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory]]
- **作者**: Jingbo Ji, Lingyi Li, Xilong Cheng, Yuhao Zhou, Wenji Zhang, Yuting Tan, Yunxiao Qin
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《RippleMem: From Isolated Retrieval to Associative Recollection for Long-Term Agent Memory》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EverMemBench, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based agents increasingly rely on external memory to support long-horizon reasoning and interaction. However, the main bottleneck is not simply storing past experience, but recovering the right set of evidence when relevant information is distributed across many interactions. Existing approaches struggle with this access problem. Full-context methods require noisy long-context search, flat retrieval often returns isolated and incomplete records, and graph-based memory systems can be expensive to construct while compressing rich event context. We introduce RippleMem, a long-term memory system that replaces one-shot retrieval with adaptive associative recollection. Inspired by cue-dependent episodic retrieval and associative completion, RippleMem stores interaction history as cue-rich episodic memory units and organizes them in an event-centric memory graph. Given a query, it first recalls relevant memory anchors through hybrid cues, then expands from these anchors along semantic and structural associations to recover missing supporting evidence. In this way, initially recalled memories serve not only as answer context, but also as cues for completing the evidence needed to answer. Experiments on LoCoMo and LongMemEval-S show that RippleMem achieves the best overall performance across evaluated settings, improving LLM-as-a-Judge accuracy by 3.95% on LoCoMo and up to 11.87% on LongMemEval-S, while reducing graph construction cost by about 30x.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Local_Accuracy_A_Protocol-Level_Identifiability_Audit_for_Controlled_LLM_Reasoning_Evaluation|Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled LLM Reasoning Evaluation]]

![[assets/2608.13326_figure.png|800]]

- **arXiv**: [2608.13326](https://arxiv.org/abs/2608.13326)
- **PDF**: https://arxiv.org/pdf/2608.13326
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Local_Accuracy_A_Protocol-Level_Identifiability_Audit_for_Controlled_LLM_Reasoning_Evaluation|Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled LLM Reasoning Evaluation]]
- **作者**: Junhao Luo, Ning Huang, Ziqi Sha, Wenxuan Tang, Wei Deng
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Beyond Local Accuracy: A Protocol-Level Identifiability Audit for Controlled LLM Reasoning Evaluation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM benchmark scores can be precise even when the observation protocol does not identify the behavioral property they are intended to measure. In a controlled, solver-grounded setting, we formalize a protocol-level identifiability audit over a finite behavioral policy class: given policies H, observation support O, and estimand $τ$, we test whether O separates every pair with different $τ$. The audit requires zero model calls and resolves our diagnostic case: base-only observation collapses seven frozen deterministic policies into one equivalence class; full support yields seven classes and no cross-estimand collisions; every leave-one-out support retains a constructive collision witness. Empirically, both constrained-generation variants have pair-validity 1.0, yet base accuracy and selective-response fidelity diverge - 0.620 versus 0.324 across six balanced oracle-transition directions (cluster-bootstrap 95% CI [0.600, 0.642] vs. [0.304, 0.345]) - and the gap recurs on a second deterministic source (0.646 vs. 0.331). The audit also synthesizes a minimum identifying support $O^*$ for the frozen policy class: two cells instead of the full 36-cell tensor. This case shows how evaluation-design validity can be checked structurally before model inference and why base correctness does not determine intervention-response fidelity.

</details>

---

### [[20_Research/Papers/大模型/When_Should_Multi-Round_RAG_Stop_Structured_Stopping_Judgments_and_Retrieval_Reduction_in_Search-R1|When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1]]

![[assets/2608.13237_first_page.png|800]]

- **arXiv**: [2608.13237](https://arxiv.org/abs/2608.13237)
- **PDF**: https://arxiv.org/pdf/2608.13237
- **详细分析**: [[20_Research/Papers/大模型/When_Should_Multi-Round_RAG_Stop_Structured_Stopping_Judgments_and_Retrieval_Reduction_in_Search-R1|When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1]]
- **作者**: Weimeng Luo
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: RL

#### 研究背景与动机

《When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Full-Set, HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-round retrieval-augmented generation (RAG) must decide when to stop searching as evidence accumulates. Because the deployed policy is determined by the first STOP on each trajectory, this is a sequential selection problem rather than an independent state-classification task. We adapt S2G-RAG's structured sufficiency-and-gap judgment to a frozen Search-R1 pipeline and train a Qwen3.5-2B judge on 3,009 states from 900 disjoint HotpotQA questions. Search-R1's reasoner, retriever, corpus, prompt, and search budget remain unchanged, while the judge checkpoint and stopping threshold are selected on grouped validation and frozen before confirmatory evaluation. On the confirmatory test set, the resulting policy reduces retrieval calls by 77 (3.70\%) relative to Native Search-R1, while Official Exact Match decreases by 0.625 percentage points. Thus, the trained S2G-style structured judge reduces retrieval while broadly preserving answer accuracy. The result does not imply unchanged or improved accuracy, safe stopping, or lower total inference cost.

</details>

---

### [[20_Research/Papers/大模型/Which_LLM_Is_Your_Ideal_Companion_Evaluating_Emotional_Companion_Capabilities_of_LLMs_Based_on_Adult_Attachment_Theory|Which LLM Is Your Ideal Companion? Evaluating Emotional Companion Capabilities of LLMs Based on Adult Attachment Theory]]

![[assets/2608.13168_figure.png|800]]

- **arXiv**: [2608.13168](https://arxiv.org/abs/2608.13168)
- **PDF**: https://arxiv.org/pdf/2608.13168
- **详细分析**: [[20_Research/Papers/大模型/Which_LLM_Is_Your_Ideal_Companion_Evaluating_Emotional_Companion_Capabilities_of_LLMs_Based_on_Adult_Attachment_Theory|Which LLM Is Your Ideal Companion? Evaluating Emotional Companion Capabilities of LLMs Based on Adult Attachment Theory]]
- **作者**: Junkai Zhou, Shiting Guan, Zhaoyi Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《Which LLM Is Your Ideal Companion? Evaluating Emotional Companion Capabilities of LLMs Based on Adult Attachment Theory》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ECBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language models (LLMs) are increasingly applied for emotional companionship, evaluating their behavior and capabilities in intimate relationships has become a pressing issue. However, existing assessments primarily characterize general personality traits, providing limited insight into model behavior within intimate and emotionally sensitive contexts. Therefore, we introduce adult attachment theory into LLM evaluation and use the Experiences in Close Relationships-Revised (ECR-R) scale to characterize attachment anxiety and avoidance. To evaluate emotional companionship capabilities of LLMs in realistic interaction scenarios, we present an emotional companionship benchmark, ECBench, spanning four scenarios including emotional support, collaborative tasks, conflict resolution, and social guidance, across friendship and romantic relationships. ECBench is utilized to assess model behavior using 11 dialogue-quality metrics and three evaluation methods. We evaluate the attachment tendencies of 32 LLMs and select representative models to investigate how these tendencies manifest in contextualized multi-turn interactions and whether they can be shaped through prompting. Our study provides a theoretical lens from psychology, along with practical tools to understand and select LLMs for emotional companionship.

</details>

---

### [[20_Research/Papers/大模型/CASA_Content-Acoustic_Speaking_Assessment_with_Speech_Encoder_and_Large_Language_Model|CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model]]

![[assets/2608.13101_figure.png|800]]

- **arXiv**: [2608.13101](https://arxiv.org/abs/2608.13101)
- **PDF**: https://arxiv.org/pdf/2608.13101
- **详细分析**: [[20_Research/Papers/大模型/CASA_Content-Acoustic_Speaking_Assessment_with_Speech_Encoder_and_Large_Language_Model|CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model]]
- **作者**: Nhan Phan, Ilona Lähteenmäki, Anna von Zansen, Olli-Pekka Pauna, Yaroslav Getman, Tamás Grósz, Mikko Kurimo
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《CASA: Content-Acoustic Speaking Assessment with Speech Encoder and Large Language Model》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Research on automatic speaking assessment (ASA) has increasingly adopted multimodal speech large language models to assess learners' speaking performance. However, existing studies provide limited analysis of how acoustic and content information contribute to predictions and how stable the resulting performance is. We propose CASA, a simpler architecture combining Whisper-medium and Qwen3.5-2B that achieves state-of-the-art performance while providing a more interpretable separation between speech delivery and content. On the Speak &amp; Improve Corpus 2025, CASA achieves a root mean square error (RMSE) of 0.358, improving on the previous best RMSE while using approximately half the estimated inference parameters. The general-purpose architecture is designed for adaptation to other ASA corpora without structural changes and relies on three handcrafted fluency features. Through ablations and repeated runs, we analyze the individual and complementary contributions of acoustic and content information, examine performance variability, and demonstrate the potential of large language model reasoning for training-free content validation.

</details>

---

### [[20_Research/Papers/大模型/RAGSieve_Self-Referenced_Local_Contrast_for_Knowledge-Poison_Detection_in_Retrieval-Augmented_Generation|RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation]]

![[assets/2608.13010_figure.png|800]]

- **arXiv**: [2608.13010](https://arxiv.org/abs/2608.13010)
- **PDF**: https://arxiv.org/pdf/2608.13010
- **详细分析**: [[20_Research/Papers/大模型/RAGSieve_Self-Referenced_Local_Contrast_for_Knowledge-Poison_Detection_in_Retrieval-Augmented_Generation|RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation]]
- **作者**: Xinlong Xu, Yoshua Y. Li
- **cs 子类**: cs.CL, cs.CR, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: ComputerVision, Security, Systems

#### 研究背景与动机

《RAGSieve: Self-Referenced Local Contrast for Knowledge-Poison Detection in Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation treats an external corpus as inference evidence, allowing injected documents to promote attacker-chosen claims. Existing detectors depend on trusted references, specific attack artifacts, or global thresholds sensitive to corpus topology. We present RAGSieve, a self-referenced detection framework that constructs its reference from the inspected system. RAGSieve-Query (RSQ) performs query-local contrast, scoring top-five candidates against ranks 6-20 of the same retrieval to detect answer-anchor concentration and carrier transitions. RAGSieve-Graph (RSG) performs corpus-local contrast, comparing each document's semantically similar but lexically distinct neighbors with its local baseline to detect coordinated density before queries arrive. Across three QA datasets and six poisoning constructions, RSQ achieves 95.2% AUROC and detects 82.2% of poison at 5% clean-document removal, versus 81.1%/52.5% for GMTP. RSG achieves 93.3%/79.8%, versus 79.4%/37.6% for CleanBase. Joint deployment reduces attack success from 67.4% to 14.0% while retaining 41.3% F1 on unpoisoned retrieval, demonstrating practical protection at both corpus ingestion and query time without poison labels or trusted corpora. Source code is available at https://github.com/XrazyMee/RAGSieve.

</details>

---

### [[20_Research/Papers/大模型/HybridRAG-BN_A_Retrieval-Augmented_Framework_with_Fine-Tuned_Verification_for_Bangla_KBQA|HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA]]

![[assets/2608.13004_first_page.png|800]]

- **arXiv**: [2608.13004](https://arxiv.org/abs/2608.13004)
- **PDF**: https://arxiv.org/pdf/2608.13004
- **详细分析**: [[20_Research/Papers/大模型/HybridRAG-BN_A_Retrieval-Augmented_Framework_with_Fine-Tuned_Verification_for_Bangla_KBQA|HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA]]
- **作者**: Rathijit Aich, Nirjhar Das, Mahfuzulhoq Chowdhury
- **cs 子类**: cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: cs.CL

#### 研究背景与动机

《HybridRAG-BN: A Retrieval-Augmented Framework with Fine-Tuned Verification for Bangla KBQA》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：KBQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Knowledge-base question answering (KBQA) systems rely on effective retrieval and reasoning mechanisms to generate accurate answers from external knowledge sources. However, developing reliable KBQA systems for low-resource languages such as Bangla remains challenging due to limited retrieval-focused research, scarce language resources, and difficulties in grounding generated responses in external knowledge. In this work, we propose HybridRAG-BN, a retrieval-augmented framework for Bangla KBQA that integrates hybrid retrieval using BM25 and BGE-M3, answer generation using the GGUF version of Gemma-4-31B-Instruct, and a LoRA-fine-tuned Gemma-4-31B-Instruct model for answer verification and refinement. To further improve robustness, the framework incorporates a post-processing stage that addresses unresolved cases through fallback answer replacement and DuckDuckGo-assisted retrieval. Experimental results demonstrate the effectiveness of the proposed framework, achieving token-level F1 scores of 0.71654 and 0.72912 on the public and private leaderboards, respectively, securing first place in the competition.

</details>

---

### [[20_Research/Papers/大模型/LycheeMemory_V2_Efficient_Long-Term_Memory_for_LLM_Agents_via_Semantic_Segment-Level_Consolidation|LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation]]

![[assets/2608.12990_figure.png|800]]

- **arXiv**: [2608.12990](https://arxiv.org/abs/2608.12990)
- **PDF**: https://arxiv.org/pdf/2608.12990
- **详细分析**: [[20_Research/Papers/大模型/LycheeMemory_V2_Efficient_Long-Term_Memory_for_LLM_Agents_via_Semantic_Segment-Level_Consolidation|LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation]]
- **作者**: Dongfang Li, Zixuan Liu, Junmai Wang, Jiahe Huang, Fuhao Li, Bonian Jia, Baotian Hu, Min Zhang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《LycheeMemory V2: Efficient Long-Term Memory for LLM Agents via Semantic Segment-Level Consolidation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents must preserve information from past interactions to support future tasks. Existing memory systems typically rely on eager consolidation, invoking LLMs after each interaction to extract, summarize, or update memories. This design makes memory construction increasingly costly as conversations grow. Coarse summarization can reduce construction cost but risks discarding fine-grained contextual evidence, whereas larger retrieval contexts or multi-hop LLM reasoning shift the overhead to query time. We present LycheeMemory V2, an efficient long-term memory framework that replaces turn-level consolidation with semantic segment-level consolidation. Instead of consolidating every interaction, LycheeMemory batches multiple exchanges into segments and encodes each finalized segment into context-independent typed memory records. Segment-level batching lowers LLM encoding frequency, while semantic boundary detection helps preserve coherent event-level and temporal evidence compared with fixed-window batching. The resulting records are organized with lightweight structured indexes for query-planned evidence retrieval. Experiments using GPT-4.1-Mini show that LycheeMemory achieves state-of-the-art performance, reaching 89.22% on LoCoMo and 92.20% on LongMemEval-S. Compared with A-Mem, it reduces construction tokens by 86.0% on LoCoMo and 75.9% on LongMemEval-S without increasing query-time token usage. More broadly, our results suggest that the accuracy--cost trade-off of long-term agent memory depends not only on what information is retained, but also on the granularity at which it is consolidated.

</details>

---

### [[20_Research/Papers/大模型/Reconcile_Once,_Write_Anytime_A_Trust-Tiered_Librarian_and_a_Multi-Agent_Writer_for_Drift-Free,_Point-in-Time_Research|Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research]]

![[assets/2608.12984_first_page.png|800]]

- **arXiv**: [2608.12984](https://arxiv.org/abs/2608.12984)
- **PDF**: https://arxiv.org/pdf/2608.12984
- **详细分析**: [[20_Research/Papers/大模型/Reconcile_Once,_Write_Anytime_A_Trust-Tiered_Librarian_and_a_Multi-Agent_Writer_for_Drift-Free,_Point-in-Time_Research|Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research]]
- **作者**: Xing Zhang, Yanwei Cui, Guanghui Wang, Peiyang He
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Reconcile Once, Write Anytime: A Trust-Tiered Librarian and a Multi-Agent Writer for Drift-Free, Point-in-Time Research》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-form research reports generated by large language models drift, contradict themselves, and lose provenance: the same metric appears with different values, and rumor is quoted as confidently as an audited filing. We present a two-tier agentic system that separates a maintained, point-in-time knowledge library from report writing. A deterministic "librarian" ingests timestamped sources into a trust-tiered ontology, layering evidence cards, an authoritative metric ledger, and a claim graph into an always-current source of truth, not per-query RAG over raw chunks. A portable multi-agent "writer" runtime then composes a contradiction-free, evidence-grounded report at any knowledge cutoff T, reading only evidence with as_of &lt;= T (no look-ahead); red-team verdicts flow back into the librarian. We evaluate on a self-collected, public corpus of 6,130 sources yielding 555,926 evidence cards (SEC EDGAR filings across 295 issuers and 11 sectors, U.S. Bureau of Labor Statistics releases, and Wikipedia). From the one library we compose four point-in-time reports on distinct theses and run eight reproducible experiments, whose headline metrics come from a deterministic quality-control gate, itself validated by defect-injection meta-evaluation at recall 1.0 and precision 1.0. A shared metric ledger removes 6,845 cross-section contradictions to zero. Tier-first selection is correct on 22/22 gold cases where a popularity-first baseline scores only 9/22; trust tiering leaks zero media-sourced numbers, and no government statistic displaces a company's own filing. A red-team refutation propagates back and self-corrects a later run with zero manual edits. Replay exhibits zero look-ahead violations across seven cutoffs while the library grows from 235,373 to 555,312 cards. Difficulty-tiered model routing exceeds the all-Opus quality ceiling while running 3.7x faster than serial.

</details>

---

### [[20_Research/Papers/强化学习/I-SDPO_Instance-Level_Adaptive_Self-Distillation_Policy_Optimization|I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization]]

![[assets/2608.12957_figure.png|800]]

- **arXiv**: [2608.12957](https://arxiv.org/abs/2608.12957)
- **PDF**: https://arxiv.org/pdf/2608.12957
- **详细分析**: [[20_Research/Papers/强化学习/I-SDPO_Instance-Level_Adaptive_Self-Distillation_Policy_Optimization|I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization]]
- **作者**: Yubo Zhang, Xinhong Ma, Zezhong Tan, Ziqiang Dong
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《I-SDPO: Instance-Level Adaptive Self-Distillation Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SciKnowEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group Relative Policy Optimization (GRPO) learns from reward differences within a rollout group, but receives no useful relative signal when every sampled response is incorrect. Privileged self-distillation can fill this gap with dense token supervision, yet applying it throughout training creates a different failure mode: the teacher is a biased, low-variance surrogate for the reward objective, so persistent imitation can oppose reward-improving updates after the policy becomes capable of producing successful trajectories. We introduce I-SDPO (Instance-Level Adaptive Self-Distillation Policy Optimization), which treats teacher reliance as capability-dependent. I-SDPO makes one routing decision per input instance and shares it across that instance's rollout group: all-incorrect groups use a privileged self-distillation objective, whereas any-success groups remain intact for GRPO. This design uses imitation only where group-relative rewards are uninformative. A local analysis characterizes when teacher and reward directions align and shows that a non-vanishing biased distillation weight induces an optimization bias floor. The routing rule automatically reduces the expected distillation rate as success probability rises, withdrawing teacher influence without a hand-designed schedule. On SciKnowEval, I-SDPO obtains the best result in all four scientific domains and improves average mean@16 accuracy from 56.67% with GRPO to 70.31%, with a maximum domain gain of 18.24 points.

</details>

---

### [[20_Research/Papers/大模型/When_Your_Agent_Opens_the_Chat_App_Agent-Controlled_Search_over_Raw_Chat_Logs_Rivals_Structured_Memory|When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory]]

![[assets/2608.12888_figure.png|800]]

- **arXiv**: [2608.12888](https://arxiv.org/abs/2608.12888)
- **PDF**: https://arxiv.org/pdf/2608.12888
- **详细分析**: [[20_Research/Papers/大模型/When_Your_Agent_Opens_the_Chat_App_Agent-Controlled_Search_over_Raw_Chat_Logs_Rivals_Structured_Memory|When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory]]
- **作者**: Ruizhe Li, Licheng Zhang, Benfeng Xu, Mingxuan Du, Zheren Fu, Weidong Chen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《When Your Agent Opens the Chat App: Agent-Controlled Search over Raw Chat Logs Rivals Structured Memory》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, MABench, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent-memory systems increasingly buy retrieval quality with structure, transforming raw conversation histories into summaries, embeddings, trees, or knowledge graphs before any question is asked. We ask how much of that benefit comes from the structure itself, rather than from competent retrieval over the raw history. We present ReFind, an agent-controlled search interface that builds no semantic structure at all: it leaves the conversation archive unmodified, indexes it lexically at turn granularity, and combines a generic iterative keyword-search loop with four chat-native controls grounded in empirical refinding work: session-aware rank fusion, local context expansion, temporal narrowing, and skipping already-inspected sessions. A separate reasoning stage answers from the collected evidence. Across a broad suite of conversational-memory tasks (single- and multi-hop QA, event ordering, and fact consolidation), roughly 2,800 questions on precise-retrieval and fact-tracking capabilities evaluated under the incremental multi-turn setting of MemoryAgentBench, ReFind attains the highest mean accuracy (58.2) of any system compared, above the strongest graph- and tree-based memory systems (HippoRAG 2, 53.2), all under a GPT-4o-mini backbone matched to every reused baseline. Controlled comparisons to single-shot BM25, a matched generic-agentic BM25 control, component removals, and agentic dense/hybrid variants separately support the roles of agent control, chat-native controls, and lexical retrieval. On LongMemEval-S/M, the same interface reaches 93.2 +/- 3.3 and 89.3 +/- 6.0 with GPT-5-mini. The results indicate that for precise, evidence-grounded questions over chat archives, much of the benefit credited to elaborate memory structures is recoverable by giving an agent controllable search over the unmodified record, with no LLM-based index construction at all.

</details>

---

### [[20_Research/Papers/大模型/When_Explanations_Betray_Backdoors_Black-Box_Auditing_for_Language_Model_Classifiers|When Explanations Betray Backdoors: Black-Box Auditing for Language Model Classifiers]]

![[assets/2608.12623_first_page.png|800]]

- **arXiv**: [2608.12623](https://arxiv.org/abs/2608.12623)
- **PDF**: https://arxiv.org/pdf/2608.12623
- **详细分析**: [[20_Research/Papers/大模型/When_Explanations_Betray_Backdoors_Black-Box_Auditing_for_Language_Model_Classifiers|When Explanations Betray Backdoors: Black-Box Auditing for Language Model Classifiers]]
- **作者**: Yang Liu, Ran Zou
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《When Explanations Betray Backdoors: Black-Box Auditing for Language Model Classifiers》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language model classifiers with explanations are used for moderation, routing, topic triage, and low-resource annotation. We study black-box auditing when the defender has only clean calibration data without trigger information but can ask the classifier for a label plus a short rationale or quoted evidence. We introduce Groundedness Drift, a lightweight score measuring whether the answer summary remains grounded in the input. Across two 7B backbones, five datasets, and four common non-adaptive OpenBackdoor-style attack families, Groundedness Drift achieves higher AUROC and lower residual target ASR than every compared detector in all cases at a nominal 5\% clean-FPR budget. We then evaluate Unsupported Groundedness, a multi-probe escalation for explanation-camouflage stress cases. Unsupported Groundedness improves signals but does not close the adaptive gap.

</details>

---

### [[20_Research/Papers/强化学习/From_Refuse_to_Richness_Rubric_Rewards_for_Long-Form_Hallucination_Reinforcement_Learning|From Refuse to Richness: Rubric Rewards for Long-Form Hallucination Reinforcement Learning]]

![[assets/2608.12337_figure.png|800]]

- **arXiv**: [2608.12337](https://arxiv.org/abs/2608.12337)
- **PDF**: https://arxiv.org/pdf/2608.12337
- **详细分析**: [[20_Research/Papers/强化学习/From_Refuse_to_Richness_Rubric_Rewards_for_Long-Form_Hallucination_Reinforcement_Learning|From Refuse to Richness: Rubric Rewards for Long-Form Hallucination Reinforcement Learning]]
- **作者**: Yudong Wang, Zhe Yang, Wenhan Ma, Rang Li, Qibin Yang, Weimin Xiong, Jiangshan Duo, Liang Zhao, Zhifang Sui
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.6（加权：强化学习 0.6）
- **关联关键词**: RL

#### 研究背景与动机

《From Refuse to Richness: Rubric Rewards for Long-Form Hallucination Reinforcement Learning》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rewards that penalize unsupported claims can improve grounding in long-form generation, but they can also teach models to answer less. We study this refusal-to-richness trade-off in long-form hallucination RL. Instead of using global richness proxies such as length, claim count, detail, or pairwise relevance, we represent each question with a key-point rubric that specifies the required and optional information a useful answer should cover. These rubrics define coverage directly and are used both for evaluation and as reward signals. Across grounding-only, proxy-based, rubric-only, and combined rewards, we find a stable trade-off: strict grounding rewards improve support but suppress coverage, while unconstrained rubric rewards improve coverage but weaken grounding. A soft combination of grounding, rubric coverage, and relevance gives the best balance in our experiments, improving in-distribution support while transferring better to out-of-distribution checklist tasks than either grounding-only or rubric-only rewards.

</details>

---

### [[20_Research/Papers/大模型/HC-RAG_Evidence-Centric_Retrieval-Augmented_Generation_over_Heterogeneous_Financial_Filings|HC-RAG: Evidence-Centric Retrieval-Augmented Generation over Heterogeneous Financial Filings]]

![[assets/2608.12335_figure.png|800]]

- **arXiv**: [2608.12335](https://arxiv.org/abs/2608.12335)
- **PDF**: https://arxiv.org/pdf/2608.12335
- **详细分析**: [[20_Research/Papers/大模型/HC-RAG_Evidence-Centric_Retrieval-Augmented_Generation_over_Heterogeneous_Financial_Filings|HC-RAG: Evidence-Centric Retrieval-Augmented Generation over Heterogeneous Financial Filings]]
- **作者**: Siyuan Chen, Huaye Tan, You Li, Jiajun Liang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: cs.CL

#### 研究背景与动机

《HC-RAG: Evidence-Centric Retrieval-Augmented Generation over Heterogeneous Financial Filings》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ConvFinQA, DocFinQA, FinQA, FinanceBench, TAT-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Financial question answering over annual reports requires more than retrieving semantically similar passages. It often involves identifying relevant companies and fiscal years, locating standardized filing sections, collecting textual and tabular evidence, and checking answers against the original documents. Existing RAG systems, however, usually flatten long filings into unordered chunks, pay limited attention to the typed structure of financial reports, and use fixed text-table fusion strategies without considering query intent. To address these limitations, we propose \textbf{HC-RAG}, a hierarchical cross-modal retrieval-augmented generation framework for evidence-centric financial QA. HC-RAG organizes filings into a typed financial evidence graph with documents, sections, text units, table units, and metadata nodes. It retrieves evidence through document-section-unit paths, aligns textual and tabular evidence in a shared retrieval space, and routes evidence according to four semantic intents: calculation, trend, fact, and comparison. We further introduce \textbf{Multi-Doc-2025}, a benchmark containing 2,327 expert-verified QA pairs from 179 SEC 10-K filings of 87 S\&amp;P 500 companies across fiscal years 2022--2024, with labels for intent, difficulty, and structural evidence attributes. Experiments on public financial QA benchmarks and Multi-Doc-2025 show that HC-RAG improves both answer quality and evidence localization, especially in long-document, table-related, and cross-document settings. HC-RAG outperforms RAPTOR by 6.6 F1 points on DocFinQA and GraphRAG by 10.9 F1 points on Multi-Doc-2025. Evidence-level analysis and ablation studies show that the improvements mainly come from more accurate section localization, table grounding, cross-document evidence aggregation, and intent-aware text-table routing.

</details>

---
