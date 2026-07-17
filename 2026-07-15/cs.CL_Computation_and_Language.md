# cs.CL | Computation and Language | 2026-07-15

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/大模型/LLM_Judges_Can_Be_Too_Generous_When_There_Is_No_Reference_Answer|LLM Judges Can Be Too Generous When There Is No Reference Answer]]

![[assets/2607.12885_figure.png|800]]

- **arXiv**: [2607.12885](https://arxiv.org/abs/2607.12885)
- **PDF**: https://arxiv.org/pdf/2607.12885
- **详细分析**: [[20_Research/Papers/大模型/LLM_Judges_Can_Be_Too_Generous_When_There_Is_No_Reference_Answer|LLM Judges Can Be Too Generous When There Is No Reference Answer]]
- **作者**: Chalamalasetti Kranti, Sowmya Vajjala
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《LLM Judges Can Be Too Generous When There Is No Reference Answer》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：TyDiQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM judges are increasingly being used to evaluate open-ended model responses, often in no-reference settings where a ground-truth answer is unavailable. However, can they reliably assess in such evaluation setups? We explore this question in this paper through a two stage pipeline with a) calibration experiments that assess the judge model's knowledge of the task it is evaluating, and b) sensitivity experiments that assess how the judge model's performance is impacted by the presence and positioning of the reference answer in the prompt. Across experiments covering three languages, we show that the judge models we evaluated tend to over-credit incorrect answers in the absence of a reference answer, and adding reference answer information to the prompt flips the judge model's correct/incorrect decisions by as much as 85% in some experimental settings. Comparison with a subset of human annotations shows that these reference-driven changes generally align with human judgments. Our results emphasize the need for calibrating the LLM judges with a sample with reference-aware evaluation before using them in reference-free setups reliably, and our methodology provides a blueprint for researchers and practitioners in doing such calibration of LLM judges for other tasks.

</details>

---

### [[20_Research/Papers/大模型/Segregate,_Refine,_Integrate_Decomposing_Multimodal_Fusion_for_Sentiment_Analysis|Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis]]

![[assets/2607.12686_figure.png|800]]

- **arXiv**: [2607.12686](https://arxiv.org/abs/2607.12686)
- **PDF**: https://arxiv.org/pdf/2607.12686
- **详细分析**: [[20_Research/Papers/大模型/Segregate,_Refine,_Integrate_Decomposing_Multimodal_Fusion_for_Sentiment_Analysis|Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis]]
- **作者**: Alexios Filippakopoulos, Elias Kallioras, Nikolaos Xiros, Efthymios Georgiou, Alexandros Potamianos
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Segregate, Refine, Integrate: Decomposing Multimodal Fusion for Sentiment Analysis》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CENet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal fusion must simultaneously refine modality-specific signals and model cross-modal interactions; two competing objectives typically entangled within the same operation. We propose \textbf{SeRIn} (\textbf{Se}gregate, \textbf{R}efine, \textbf{In}tegrate), a multimodal LM fusion scheme that enforces this separation as an architectural prior. Modality-specific representations evolve along isolated pathways, each refined against its respective encoder context, while a dedicated cross-modal pathway accumulates their joint evolution without contaminating unimodal streams. Full cross-modal interaction is deferred to a final prediction step - ablations confirm that structured interactions, not added capacity, drive the gains; gate analysis under visual corruption reveals emergent modality reweighting without explicit supervision. SeRIn achieves state-of-the-art results on CH-SIMS and CMU-MOSEI, improving all metrics on both benchmarks.

</details>

---

### [[20_Research/Papers/大模型/QUBO-Optimized_Evidence_Selection_for_Retrieval-Augmented_Question_Answering_with_Unconventional_Solvers|QUBO-Optimized Evidence Selection for Retrieval-Augmented Question Answering with Unconventional Solvers]]

![[assets/2607.12334_figure.png|800]]

- **arXiv**: [2607.12334](https://arxiv.org/abs/2607.12334)
- **PDF**: https://arxiv.org/pdf/2607.12334
- **详细分析**: [[20_Research/Papers/大模型/QUBO-Optimized_Evidence_Selection_for_Retrieval-Augmented_Question_Answering_with_Unconventional_Solvers|QUBO-Optimized Evidence Selection for Retrieval-Augmented Question Answering with Unconventional Solvers]]
- **作者**: Rahul Singh, Madhav Vadlamani
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《QUBO-Optimized Evidence Selection for Retrieval-Augmented Question Answering with Unconventional Solvers》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Development-Set, HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented question answering depends on selecting evidence passages that jointly support answer generation. However, many RAG pipelines rely on top-\(k\) ranking, where passages are selected mainly by individual relevance scores, even though multi-hop questions often require complementary evidence satisfying multiple information requirements. Recent LLM-based selectors address this by treating retrieval as set selection, but using an LLM for this intermediate stage can be costly and difficult to scale. In this work, we formulate evidence selection as a Quadratic Unconstrained Binary Optimization (QUBO) problem. Given a question, candidate passages, and decomposed information requirements, our method constructs an energy function that balances relevance, requirement coverage, support strength, redundancy, complementarity, and compactness. Low-energy solutions correspond to compact evidence subsets that cover the needed requirements while avoiding unnecessary or repetitive context. The selected passages are then passed to a downstream language model for answer generation, separating combinatorial evidence selection from semantic answer generation. We evaluate the proposed QUBO selector on HotpotQA and compare it with LLM-based set selectors and non-LLM baselines including BM25, relevance top-\(k\), maximal marginal relevance, hybrid lexical--semantic ranking, greedy coverage, and random selection. The QUBO selector achieves competitive exact-match and token-F1 performance relative to LLM-based selectors while providing a solver-compatible formulation for structured evidence selection. These results suggest that multi-hop evidence selection can be cast as discrete optimization, opening a path toward RAG pipelines where LLMs are reserved for semantic processing and answer generation, while context selection is handled by Ising/QUBO-compatible solvers.

</details>

---

### [[20_Research/Papers/大模型/Speculate_with_Memory_Lossless_Acceleration_for_LLM_Agents|Speculate with Memory: Lossless Acceleration for LLM Agents]]

![[assets/2607.12236_first_page.png|800]]

- **arXiv**: [2607.12236](https://arxiv.org/abs/2607.12236)
- **PDF**: https://arxiv.org/pdf/2607.12236
- **详细分析**: [[20_Research/Papers/大模型/Speculate_with_Memory_Lossless_Acceleration_for_LLM_Agents|Speculate with Memory: Lossless Acceleration for LLM Agents]]
- **作者**: Yu Li, Qinyuan Ye, Prafulla Kumar Choubey, Jiaxin Zhang, Chien-Sheng Wu
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Speculate with Memory: Lossless Acceleration for LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Speculative execution accelerates LLM agents by using a smaller, cheaper model to predict and pre-launch the next step while the environment is idle. However, existing speculators are stateless and discard all information between tasks, preventing prediction quality from improving with experience. We equip the speculator with three online memory systems that learn from past agent trajectories: a contrastive transition table tracking action-sequence statistics, an episodic memory retrieving contextually similar segments, and a confusion tracker suppressing recurring errors. We evaluate this approach on six benchmarks spanning three speculation types: action prediction, observation prediction, and chained prediction. Memory-augmented speculation yields a 19--39\% relative accuracy improvement on action prediction and up to a $2.5\times$ increase on observation prediction tasks with repetitive action spaces. These gains grow continuously as memory accumulates and generalize across speculator models of varying cost. All speculation is lossless because it runs during idle time at zero added wall-clock cost, and the actor's trajectory is identical to non-speculative execution.

</details>

---

### [[20_Research/Papers/大模型/Fine-Tuned_Multi-Agent_Framework_for_Detecting_OCEAN_in_Life_Narratives|Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives]]

![[assets/2607.12215_figure.png|800]]

- **arXiv**: [2607.12215](https://arxiv.org/abs/2607.12215)
- **PDF**: https://arxiv.org/pdf/2607.12215
- **详细分析**: [[20_Research/Papers/大模型/Fine-Tuned_Multi-Agent_Framework_for_Detecting_OCEAN_in_Life_Narratives|Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives]]
- **作者**: Rasiq Hussain, Darshil Italiya, Joshua Oltmanns, Mehak Gupta
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Fine-Tuned Multi-Agent Framework for Detecting OCEAN in Life Narratives》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SenticNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurately assessing personality from text is challenging because traits are latent, context-dependent, and often subtly expressed across long narratives. Large language models (LLMs) offer new opportunities by processing extensive textual contexts, but pretraining of these models can induce latent "personality-like" biases, making single-model inferences inconsistent. We propose a fine-tuned multi-agent framework for detecting OCEAN personality traits, in which sub-agents are conditioned to adopt high, low, or neutral perspectives for each trait through masked language modeling (MLM) and psychometric supervision. A judge LLM aggregates and compares sub-agent outputs to generate final trait predictions, capturing multiple complementary perspectives while mitigating individual model biases. We evaluate the framework on life narrative dataset through quantitative and qualitative experiments, including baselines, ablations, and inference quality analyses. Our approach offers a scalable and interpretable method for text-based personality inference, highlighting the benefits of multi-agent reasoning grounded in psychometric supervision.

</details>

---

### [[20_Research/Papers/大模型/CityBehavEx_A_Scalable_and_Empirically_Validated_LLM-Assisted_Urban_Simulation_Platform|CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform]]

![[assets/2607.12086_figure.png|800]]

- **arXiv**: [2607.12086](https://arxiv.org/abs/2607.12086)
- **PDF**: https://arxiv.org/pdf/2607.12086
- **详细分析**: [[20_Research/Papers/大模型/CityBehavEx_A_Scalable_and_Empirically_Validated_LLM-Assisted_Urban_Simulation_Platform|CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform]]
- **作者**: Gustavo H. Santos, Aline Viana, Thiago H Silva
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《CityBehavEx: A Scalable and Empirically Validated LLM-Assisted Urban Simulation Platform》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CitySim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent LLM-based multi-agent urban simulators can generate semantically rich city routines, but they remain costly to scale and are often weakly validated against empirical mobility patterns. We present CityBehavEx, an interactive LLM-assisted urban simulation platform that scales to city-size populations, exposes agent behavior for inspection, supports empirical validation, and generates mobility patterns that better match real-world spatial, temporal, and semantic distributions. Instead of invoking large language models for every agent action, CityBehavEx combines established human mobility models with fine-tuned cross-encoders that estimate semantic alignment between agent profiles, schedules, and activity transitions. This design enables large-scale simulations, as demonstrated in a case study of 100,000 agents over 75 days in under one hour on a single consumer GPU. The platform allows users to define simulation regions, launch experiments, inspect trajectories and activity traces, debug unrealistic behaviors, and validate generated routines against real-world mobility, time-use, and semantic metrics.

</details>

---

### [[20_Research/Papers/大模型/Transforming_LLMs_into_Efficient_Cross-Encoders_via_Knowledge_Distillation_for_RAG_Reranking|Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking]]

![[assets/2607.11933_figure.png|800]]

- **arXiv**: [2607.11933](https://arxiv.org/abs/2607.11933)
- **PDF**: https://arxiv.org/pdf/2607.11933
- **详细分析**: [[20_Research/Papers/大模型/Transforming_LLMs_into_Efficient_Cross-Encoders_via_Knowledge_Distillation_for_RAG_Reranking|Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking]]
- **作者**: Shreeya Dasa Lakshminath, Shubhan S
- **cs 子类**: cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.CL

#### 研究背景与动机

《Transforming LLMs into Efficient Cross-Encoders via Knowledge Distillation for RAG Reranking》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cross-encoders achieve high reranking accuracy in Retrieval-Augmented Generation (RAG) pipelines but impose quadratic inference costs that limit real-time deployment. We address this by fine-tuning LLaMA 3 (8B) as a drop-in reranker using a two-stage pipeline: supervised fine-tuning on a custom query-document relevance dataset via the Unsloth framework with LoRA adapters, followed by 4-bit quantization for efficient inference. The resulting model replaces the cross-encoder in a dual-retriever RAG pipeline combining BM25 and dense vector search. Evaluated on a domain-specific question-answering benchmark using the RAGAS framework, our fine-tuned LLaMA 3 reranker achieves gains of 14% in answer relevancy, 16% in context precision, 19% in answer similarity, and 21% in answer correctness over the cross-encoder baseline, while reducing inference overhead through 4-bit quantization. These results demonstrate that instruction-tuned LLMs can be adapted into accurate, efficient rerankers without the quadratic complexity of traditional cross-encoders.

</details>

---

### [[20_Research/Papers/大模型/From_Words_to_Widgets_for_Controllable_LLM_Generation|From Words to Widgets for Controllable LLM Generation]]

![[assets/2604.10925_figure.jpg|800]]

- **arXiv**: [2604.10925](https://arxiv.org/abs/2604.10925)
- **PDF**: https://arxiv.org/pdf/2604.10925
- **详细分析**: [[20_Research/Papers/大模型/From_Words_to_Widgets_for_Controllable_LLM_Generation|From Words to Widgets for Controllable LLM Generation]]
- **作者**: Chao Zhang, Yiren Liu, Lunyiu Nie, Jeffrey M. Rzeszotarski, Yun Huang, Tal August
- **cs 子类**: cs.CL, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《From Words to Widgets for Controllable LLM Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural language remains the predominant way people interact with large language models (LLMs). However, users often struggle to precisely express and control subjective preferences (e.g., tone, style, and emphasis) through prompting. We propose Malleable Prompting, a new interactive prompting technique for controllable LLM generation. It reifies preference expressions in natural language prompts into GUI widgets (e.g., sliders, dropdowns, and toggles) that users can directly configure to steer generation, while visualizing each control's influence on the output to support attribution and comparison across iterations. To enable this interaction, we introduce an LLM decoding algorithm that modulates the token probability distribution during generation based on preference expressions and their widget values. Through a user study, we show that Malleable Prompting helps participants achieve target preferences more precisely and is perceived as more controllable and transparent than natural language prompting alone.

</details>

---
