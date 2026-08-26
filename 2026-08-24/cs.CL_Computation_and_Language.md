# cs.CL | Computation and Language | 2026-08-24

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/大模型/Affective_Context_Amplifies_Sycophancy_in_LLM_Responses|Affective Context Amplifies Sycophancy in LLM Responses]]

![[assets/2608.21242_figure.png|800]]

- **arXiv**: [2608.21242](https://arxiv.org/abs/2608.21242)
- **PDF**: https://arxiv.org/pdf/2608.21242
- **详细分析**: [[20_Research/Papers/大模型/Affective_Context_Amplifies_Sycophancy_in_LLM_Responses|Affective Context Amplifies Sycophancy in LLM Responses]]
- **作者**: Jiayi Li, Sanjana Menon, Brett Frischmann, Shomir Wilson, Sarah Rajtmajer
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Affective Context Amplifies Sycophancy in LLM Responses》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As conversational companions, large language models (LLMs) often have access to users' emotional states. We study how this affective context modulates LLM sycophancy in subjective, evaluative interactions, where users share actions or opinions that invite feedback. Drawing on ingratiation theory, we measure sycophancy as the divergence between a model's independent evaluation and its user-facing response, elicited by presenting the same content as either a third-party account or the user's own disclosure. Across seven LLMs and two Reddit datasets (r/AmItheAsshole and r/TrueUnpopularOpinion), we find that this divergence is systematic and strongly one-directional. User-facing responses consistently soften or withhold negative or oppositional judgments. Affective context further amplifies this divergence with negative states, particularly loneliness and distress, producing the largest effects. These findings suggest that affective context functions as a vulnerability signal that suppresses critical feedback when users may need it most, often through evasive sycophancy, in which models retreat toward non-committal responses rather than outright agreement.

</details>

---

### [[20_Research/Papers/大模型/COMET_Contrastive_Motion-Enhanced_Temporal_Reasoning_for_Video_Multimodal_Large_Language_Models|COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models]]

![[assets/2608.21030_figure.png|800]]

- **arXiv**: [2608.21030](https://arxiv.org/abs/2608.21030)
- **PDF**: https://arxiv.org/pdf/2608.21030
- **详细分析**: [[20_Research/Papers/大模型/COMET_Contrastive_Motion-Enhanced_Temporal_Reasoning_for_Video_Multimodal_Large_Language_Models|COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models]]
- **作者**: Chenghua Zhu, Zhaolu Kang, Qifan Shi, Siyan Wu, Kehan Jiang, Lei Wei, Lianyu Hu, Guangyuan Dong, Mingbo Yang, Rui Lu, Guibo Luo
- **cs 子类**: cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《COMET: Contrastive Motion-Enhanced Temporal Reasoning for Video Multimodal Large Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NExT-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video multimodal large language models have advanced significantly, yet fine-grained motion-temporal understanding remains fragile. The core bottleneck is not only sparse frame sampling, but also the lack of a complete temporal modeling pipeline for explicitly representing frame-to-frame change, enabling appearance-motion interaction, and optimizing temporal direction sensitivity. We propose COMET, a temporally grounded framework that systematically strengthens video MLLMs through explicit temporal representation, appearance-motion fusion, and direction-aware optimization. Architecturally, COMET introduces a temporal motion branch built on Taylor frame differences and injects its motion evidence into the appearance stream via temporal attention bias-enhanced cross-attention. For optimization, COMET combines temporal prior distillation with a forward-reverse TC-GRPO stage that turns temporal order into a direct learning signal and strengthens the model's use of directional motion patterns encoded by the temporal motion branch. The method achieves consistent overall improvements with a pronounced motion-temporal bias: on Qwen3-VL-8B, action-centric tasks (STAR, SSv2) improve by 4.9% on average, temporal reasoning tasks (NExT-QA, CLEVRER, LLaVA-178K) by 2.1% over BL-GRPO, while static perception tasks (PerceptionTest) remain on par. The same gain pattern also transfers to InternVL2.5-8B, indicating that COMET generalizes across model families.

</details>

---

### [[20_Research/Papers/大模型/ForeDreamer_A_Self-Evolving_Dual-Agent_Memory_Architecture_for_Future_Event_Prediction|ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction]]

![[assets/2608.20920_figure.png|800]]

- **arXiv**: [2608.20920](https://arxiv.org/abs/2608.20920)
- **PDF**: https://arxiv.org/pdf/2608.20920
- **详细分析**: [[20_Research/Papers/大模型/ForeDreamer_A_Self-Evolving_Dual-Agent_Memory_Architecture_for_Future_Event_Prediction|ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction]]
- **作者**: Linhao Zhong, Zongze Du, Linyu Wu, Yu Bo, Hourong Li, Chenchen Jing, Hao Chen, Yuling Xi, Chunhua Shen
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《ForeDreamer: A Self-Evolving Dual-Agent Memory Architecture for Future Event Prediction》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-web future event prediction requires agents to distill reliable signals from noisy, redundant, and incomplete evidence. Existing retrieval/memory mechanisms directly feed retrieved information to agents or rely on simple memory functions such as storing and reusing prior information for prediction, leaving them insufficient for open-web forecasting. We propose to transform raw web evidence into structured memory before prediction, enabling agents to reason over distilled, question-specific evidence rather than noisy retrieval results. This paper presents ForeDreamer, a self-evolving dual-agent framework for managing memory over open-web evidence. ForeDreamer separates factual memory, a question-specific evidence state for the current forecast, from experiential memory, persistent agent experience accumulated across forecasting episodes. It uses a main agent for search and prediction, and a memory-processing subagent to convert search results into factual memory with dedicated tools. ForeDreamer further evolves experiential memory through two tracks, improving both forecasting decisions and factual-memory construction. Experiments on Prophet Arena and FutureX demonstrate the effectiveness of ForeDreamer. Project page: https://zhongzero.github.io/ForeDreamer

</details>

---

### [[20_Research/Papers/大模型/Tree-of-Concerns_Hierarchical_Multi-Agent_Debate_for_Unstated-Limitation_Extraction_in_Scientific_Critique|Tree-of-Concerns: Hierarchical Multi-Agent Debate for Unstated-Limitation Extraction in Scientific Critique]]

![[assets/2608.20777_first_page.png|800]]

- **arXiv**: [2608.20777](https://arxiv.org/abs/2608.20777)
- **PDF**: https://arxiv.org/pdf/2608.20777
- **详细分析**: [[20_Research/Papers/大模型/Tree-of-Concerns_Hierarchical_Multi-Agent_Debate_for_Unstated-Limitation_Extraction_in_Scientific_Critique|Tree-of-Concerns: Hierarchical Multi-Agent Debate for Unstated-Limitation Extraction in Scientific Critique]]
- **作者**: Sahil Mishra, Niranjan Rajeev, Tanmoy Chakraborty
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Tree-of-Concerns: Hierarchical Multi-Agent Debate for Unstated-Limitation Extraction in Scientific Critique》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ToC-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As scientific literature grows and papers increasingly under-report limitations, multi-agent LLMs offer a promising approach to systematically uncover these hidden failure modes. Here, we introduce Tree-of-Concerns, a multi-agent framework that deploys specialized skeptic personas, each operating through a category-specific analytical lens, as parallel debate trees to extract unstated limitations from scientific papers. Each persona conducts structured, evidence-grounded argumentation, while a Panel Review mechanism re-evaluates each surviving claim from all five perspectives to correct category drift and severity miscalibration. Through experiments on ToC-Bench, our benchmark of 414 research papers with 1,905 unstated limitations, sourced from reviewer-reported weaknesses and follow-up citation critiques, we demonstrate that ToC improves precision by 79% and coverage by 11% relative to strongest baselines, surfacing specific, evidence-grounded concerns that support reviewers in systematic evaluation.

</details>

---

### [[20_Research/Papers/大模型/Using_Human-LLM_Disagreement_to_Improve_Checklist-Based_Quality_Appraisal|Using Human-LLM Disagreement to Improve Checklist-Based Quality Appraisal]]

![[assets/2608.20385_figure.png|800]]

- **arXiv**: [2608.20385](https://arxiv.org/abs/2608.20385)
- **PDF**: https://arxiv.org/pdf/2608.20385
- **详细分析**: [[20_Research/Papers/大模型/Using_Human-LLM_Disagreement_to_Improve_Checklist-Based_Quality_Appraisal|Using Human-LLM Disagreement to Improve Checklist-Based Quality Appraisal]]
- **作者**: Timo van der Kuil, Bruno Messina Coimbra, Mirjam van Zuiden, Robert A. Bagheri, Rens van de Schoot, Klaas Dieleman, Berend Greijn, Stefan Houkes, Sebastiaan Rodenhuis, Elizabeth M. Grandfield
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Using Human-LLM Disagreement to Improve Checklist-Based Quality Appraisal》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Systematic reviews rely on quality appraisal of included studies, a process that is time-consuming and sensitive to ambiguity in checklist criteria. Although large language models (LLMs) offer opportunities to support these tasks, appraisal checklists are typically treated as fixed inputs, and it remains unclear how their design affects agreement with expert judgments. Therefore, we investigate (1) whether LLMs can approximate human judgments in checklist-based appraisal and (2) whether patterns of human-LLM disagreement can be used to identify and improve ambiguous checklist items. Using the Guidelines for Reporting on Latent Trajectory Studies (GRoLTS) checklist, we compare LLM-generated assessments with expert annotations across three research topics and two checklist versions. Agreement is assessed using item-level accuracy, chance-corrected agreement, and preservation of study-level rank ordering. We find that performance varies substantially across checklist items, with ambiguous and conditional criteria producing the greatest disagreement. Revising these items improves both raw and chance-corrected agreement. Although item-level misclassifications persist, LLM-generated scores often preserve the relative ranking of studies when high-agreement items are retained. These results indicate that reliable LLM-assisted appraisal depends not only on model choice but also on checklist design. The findings suggest that analyzing human-LLM disagreement can help identify problematic checklist items and support the iterative improvement of research synthesis workflows.

</details>

---

### [[20_Research/Papers/大模型/Decoupled_Vision-Language_System_for_Multimodal_Understanding_and_Generation|Decoupled Vision-Language System for Multimodal Understanding and Generation]]

![[assets/2608.20382_figure.png|800]]

- **arXiv**: [2608.20382](https://arxiv.org/abs/2608.20382)
- **PDF**: https://arxiv.org/pdf/2608.20382
- **详细分析**: [[20_Research/Papers/大模型/Decoupled_Vision-Language_System_for_Multimodal_Understanding_and_Generation|Decoupled Vision-Language System for Multimodal Understanding and Generation]]
- **作者**: Yifan Xu, Baochen Xiong, Xiaoshan Yang, Donglin Di, Yaowei Wang, Changsheng Xu
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《Decoupled Vision-Language System for Multimodal Understanding and Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce a new architecture design for multimodal large language models (MLLMs), Libra, capable of both multimodal understanding and generation. Libra architecture contains one vision system and one language system, connected by cross-modal bridges. This design decouples self-modal modeling and cross-modal interaction, enabling each modality to learn its unique representations while maintaining effective cross-modal comprehension. The decoupling is mainly achieved in a switch attention module and a switch FFN module, which dynamically routes the computation flow for self-modal modeling and cross-modal interaction scenarios. We evaluate the effectiveness in two important settings: \textbf{Libra-1} for the understanding-only image-to-text setting, and \textbf{Libra-2} for unified image-to-text understanding and text-to-image generation. In addition to the architecture design, we discuss various improvements on tokenization, positional encoding, and supervision. Experiments demonstrate that the dedicated Libra design enables mutual improvements on multimodal understanding and generation, achieving strong performance on both understanding and generation benchmarks.

</details>

---

### [[20_Research/Papers/大模型/TH-GNN_Heterogeneous_Temporal_Graph_Neural_Networks_for_LLM-Agent_Shilling_Attack_Detection|TH-GNN: Heterogeneous Temporal Graph Neural Networks for LLM-Agent Shilling Attack Detection]]

![[assets/2608.20376_figure.png|800]]

- **arXiv**: [2608.20376](https://arxiv.org/abs/2608.20376)
- **PDF**: https://arxiv.org/pdf/2608.20376
- **详细分析**: [[20_Research/Papers/大模型/TH-GNN_Heterogeneous_Temporal_Graph_Neural_Networks_for_LLM-Agent_Shilling_Attack_Detection|TH-GNN: Heterogeneous Temporal Graph Neural Networks for LLM-Agent Shilling Attack Detection]]
- **作者**: Shivam Swarup, Divya Prakash Shrivastava, Rakesh Thakur
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《TH-GNN: Heterogeneous Temporal Graph Neural Networks for LLM-Agent Shilling Attack Detection》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents can now generate realistic shilling profiles, fluent reviews, and coherent ratings at scale, systematically defeating recommender-system defenses. Text-only detectors that flag semantic drift in review embeddings are blind to graph structure and temporal coordination, while graph-only detectors that exploit neighborhood anomalies cannot reason over review semantics or the cross-modal inconsistencies produced by LLM-generated content. We propose TH-GNN, a heterogeneous temporal graph neural network with a two-layer Heterogeneous Graph Transformer backbone that applies per-type and per-relation attention augmented with learnable sinusoidal temporal encodings on every edge. Cross-modal attention fuses structural user embeddings with frozen RoBERTa representations of reviews and item descriptions, while a GRU operating over log inter-arrival times captures temporal burstiness. Evaluated across five attack families and four benchmark datasets, TH-GNN achieves a grand-mean F1 score of 0.870, outperforming the strongest text-only baseline on Agent4SR attacks by 10.9 percentage points and 11.5 percentage points at the lowest injection rate. These results demonstrate the effectiveness of jointly modeling temporal, structural, and semantic signals for detecting sophisticated LLM-driven shilling attacks.

</details>

---

### [[20_Research/Papers/大模型/An_ambiguity_taxonomy_for_evaluating_large_language_model_performance_on_clinical_registry_abstraction_a_multi-site_prospective_study|An ambiguity taxonomy for evaluating large language model performance on clinical registry abstraction: a multi-site prospective study]]

![[assets/2608.20373_first_page.png|800]]

- **arXiv**: [2608.20373](https://arxiv.org/abs/2608.20373)
- **PDF**: https://arxiv.org/pdf/2608.20373
- **详细分析**: [[20_Research/Papers/大模型/An_ambiguity_taxonomy_for_evaluating_large_language_model_performance_on_clinical_registry_abstraction_a_multi-site_prospective_study|An ambiguity taxonomy for evaluating large language model performance on clinical registry abstraction: a multi-site prospective study]]
- **作者**: James Matheson, Betsy Castillo, Andrew Y. Shin, David Scheinker
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM

#### 研究背景与动机

《An ambiguity taxonomy for evaluating large language model performance on clinical registry abstraction: a multi-site prospective study》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Objective: To evaluate large language model (LLM) performance on unprocessed electronic medical record (EMR) data for clinical registry abstraction. Methods: We evaluated LLM performance answering registry questions for the American College of Cardiology National Cardiovascular Data Registry (ACC NCDR). In a pilot study at an academic medical center, the model identified candidate data sources for each registry question and experienced abstractors used these results to define question-specific document sets. In a validation study at a second center with a second ACC NCDR registry, the LLM answered questions using the question-specific document sets. Before reviewing any output, two abstractors independently established the ground truth and assigned each question to one of six categories, ordered by the ambiguity and clinical reasoning required to resolve it: Medication/Event Flag, Binary Clinical Presence, Administrative, Quantitative Laboratory/Physiologic, Clinical Interpretation, and Event Timing. Results: The analytical sample comprised 9,430 abstractor answers reconciled to 4,715 consensus answers (501 pilot; 4,214 validation). In the pilot, candidate data sources per question averaged between 14.6 (SD 13.9) for demographics and 89.2 (SD 56.1) for history and risk factors. In validation, human inter-rater agreement was approximately 98\% while 87\% of LLM answers exactly matched consensus, 2\% partially, and 9\% did not. Mean question-level accuracy was 91.5\% (SD 13.4\%) across 157 questions with at least 20 answers, and declined as ambiguity increased, from 96\% for Medication/Event Flag to 62\% for Event Timing questions. Conclusions: LLMs answering clinical registry questions on unprocessed EMR data achieved far lower accuracy than human abstractors. LLM accuracy fell steadily as ambiguity and the level of required clinical reasoning increased.

</details>

---

### [[20_Research/Papers/强化学习/Multilingual_Verifier_Bias_in_RLVR_Benchmark,_Rollout_Diagnosis,_and_the_Cross-Lingual_Selection_Bottleneck|Multilingual Verifier Bias in RLVR: Benchmark, Rollout Diagnosis, and the Cross-Lingual Selection Bottleneck]]

![[assets/2608.20362_first_page.png|800]]

- **arXiv**: [2608.20362](https://arxiv.org/abs/2608.20362)
- **PDF**: https://arxiv.org/pdf/2608.20362
- **详细分析**: [[20_Research/Papers/强化学习/Multilingual_Verifier_Bias_in_RLVR_Benchmark,_Rollout_Diagnosis,_and_the_Cross-Lingual_Selection_Bottleneck|Multilingual Verifier Bias in RLVR: Benchmark, Rollout Diagnosis, and the Cross-Lingual Selection Bottleneck]]
- **作者**: Chenyu Zhou, Qiliang Jiang, Xu Zhou
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Multilingual Verifier Bias in RLVR: Benchmark, Rollout Diagnosis, and the Cross-Lingual Selection Bottleneck》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Soft-SVeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) is a standard recipe for training large language models on mathematical reasoning, where an answer verifier serves as a language-neutral reward function. We show that this assumption fails in multilingual settings: an exact-match verifier turns format and script variation into language-dependent false-negative reward noise. We introduce a reusable protocol for auditing multilingual RLVR rewards: a verifier-robustness suite, a rollout-diagnosis procedure, and language-conditioned reward-error metrics for Japanese, English, and Chinese answers. On MGSM rollouts with k=8, the exact-match proxy rejects trusted-correct answers at sharply different rates by language across Qwen3-4B, Qwen3-8B, and Llama-3.1-8B-Instruct; for Qwen3-8B, the false-negative rate reaches 0.642 on JP against 0.122 on EN and 0.073 on CN. A plain-numeric probe localizes the mechanism to the final-answer interface: an interface model drives reward-error VLB to zero while the residual accuracy gap is unchanged. We then expose a cross-lingual selection bottleneck: on MGSM250 rollouts, a target-local aggregation rule using no trusted labels closes 55-78% of the average selection gap, and over 95% of repairs require genuine cross-lingual support. The bottleneck replicates on a 483-problem MATH-500 set. A controlled training audit shows that rule-GRPO raises trusted accuracy while the reward-error VLB stays high. The unifying message is operational: multilingual RLVR rewards should be audited by language and by answer interface before they are optimized.

</details>

---

### [[20_Research/Papers/大模型/Exploratory_As-Analyzed_No-Detection_of_Culturally-Marked_Predicate-Triggered_PII_Amplification_in_a_Synthetic-English_RAG_Probe_A_Predicate|Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit]]

![[assets/2608.20351_first_page.png|800]]

- **arXiv**: [2608.20351](https://arxiv.org/abs/2608.20351)
- **PDF**: https://arxiv.org/pdf/2608.20351
- **详细分析**: [[20_Research/Papers/大模型/Exploratory_As-Analyzed_No-Detection_of_Culturally-Marked_Predicate-Triggered_PII_Amplification_in_a_Synthetic-English_RAG_Probe_A_Predicate|Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit]]
- **作者**: Yanhang Li, Zhichao Fan, Zexin Zhuang
- **cs 子类**: cs.CL, cs.CY, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Exploratory As-Analyzed No-Detection of Culturally-Marked Predicate-Triggered PII Amplification in a Synthetic-English RAG Probe: A Predicate-Resource-Confounded Audit》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：StereoSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We ask whether stereotype-loaded queries about culturally marked people leak more personal information from a retrieval-augmented generation (RAG) system than otherwise-equivalent neutral queries. We pre-register a four-culture audit (en-Anglo, es-LATAM, Arabic, Hindi) on a synthetic English PII corpus, comparing five query arms we call the Stereotype-Trigger Leakage Delta (STLD). Two caveats up front. Our locked confirmatory estimator was never run, so every test in the paper is exploratory or sensitivity, with all plan deviations listed in the appendix. And the name-leakage metric is contaminated by a prompt-echo artifact: the model often just re-emits the name we asked about, which inflates apparent leakage without any retrieval at all. On the cleaner channels (email, phone, ssn-like, address), we find no stereotype-driven amplification on any of the four cultures after multiple-comparison correction. Because our sample is only powered for mid-sized effects, and because the culturally marked probes mix stereotype content with cultural markers and heritage practices, we present this as no detection, not evidence of no effect, of culturally marked predicate leakage that is confounded with the underlying resource.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Raw_Transcripts_Structured_Persona_Extraction_for_LLM-Based_Digital_Twins|Beyond Raw Transcripts: Structured Persona Extraction for LLM-Based Digital Twins]]

![[assets/2608.20344_figure.png|800]]

- **arXiv**: [2608.20344](https://arxiv.org/abs/2608.20344)
- **PDF**: https://arxiv.org/pdf/2608.20344
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Raw_Transcripts_Structured_Persona_Extraction_for_LLM-Based_Digital_Twins|Beyond Raw Transcripts: Structured Persona Extraction for LLM-Based Digital Twins]]
- **作者**: Iris Ye, Tianze Deng, Ozan Candogan
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Beyond Raw Transcripts: Structured Persona Extraction for LLM-Based Digital Twins》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based "digital twins" aim to simulate how an individual would behavein new environments or respond to novel questions, given some representation of that individual's prior responses. A common approach constructs this representation from survey transcripts or summaries responses. Prior work shows that compressing long transcripts into shorter LLM-generated summaries does not significantly reduce predictive accuracy, suggesting that information volume is not the primary bottleneck. In this work, we argue that the key limitation is instead structural:how persona information is organized before being provided to thesimulator model. We study this by comparing unstructured summaries with structured persona representations. First, we introduce a hand-craftedschema (BDE: Background, Decision procedure, Evaluation), grounded in consumer-behavior theory, and show that it improves predictive accuracy over raw transcripts by +1.91 percentage points on a homogeneous benchmark (Twin-2K-500), with similar gains on gpt-5.4-mini and Qwen3-8B as robustness checks. However, this fixed structure does not generalizeacross more heterogeneous tasks, where performance is statistically indistinguishable from the raw transcript baseline. To address this limitation, we propose an automatic structure-discovery pipeline in which an LLM iteratively proposes and refines task-specific persona structures and extraction prompts. On a benchmark of 13 diverse sub-studies, this approach restores performance, improving mean accuracy by +1.91 percentage points over the raw transcript baseline and eliminating significant losses observed with the fixed schema. Overall, our results suggest that the main constraint in LLM-based digital twins is not how much information is provided, but how it is structured -- and that the optimal structure depends on the task.

</details>

---
