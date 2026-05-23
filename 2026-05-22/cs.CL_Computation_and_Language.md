# cs.CL | Computation and Language | 2026-05-22

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/强化学习/LANG_Reinforcement_Learning_for_Multilingual_Reasoning_with_Language-Adaptive_Hint_Guidance|LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance]]

![[assets/2605.22567_first_page.png|800]]

- **arXiv**: [2605.22567](https://arxiv.org/abs/2605.22567)
- **PDF**: https://arxiv.org/pdf/2605.22567
- **详细分析**: [[20_Research/Papers/强化学习/LANG_Reinforcement_Learning_for_Multilingual_Reasoning_with_Language-Adaptive_Hint_Guidance|LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance]]
- **作者**: Yuchun Fan, Bei Li, Peiguang Li, Yilin Wang, Yongyu Mu, Jian Yang, Xin Chen, Rongxiang Weng, Jingang Wang, Xunliang Cai, Jingbo Zhu, Tong Xiao
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive Hint Guidance》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has proven effective for enhancing multi-step reasoning in large language models (LLMs), yet its benefits have not fully translated to multilingual contexts. Existing methods struggle with a fundamental trade-off: prioritizing input-language consistency severely hampers reasoning quality, while prioritizing reasoning often leads to unintended language drift toward English. We address this challenge with LANG, a novel framework that leverages language-conditioned hints to guide exploration in non-English reasoning tasks. Our method incorporates two key mechanisms to prevent dependency on these hints: a progressive decay schedule that gradually withdraws scaffolding, and a language-adaptive switch that tailors learning horizons to specific language difficulties. Empirical results on challenging multilingual mathematical benchmarks reveal that LANG substantially enhances reasoning performance without compromising language consistency. Moreover, we show that our framework generalizes beyond mathematics, fostering more consistent language alignment across model layers

</details>

---

### [[20_Research/Papers/大模型/Maestro_Reinforcement_Learning_to_Orchestrate_Hierarchical_Model-Skill_Ensembles|Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles]]

![[assets/2605.22177_figure.png|800]]

- **arXiv**: [2605.22177](https://arxiv.org/abs/2605.22177)
- **PDF**: https://arxiv.org/pdf/2605.22177
- **详细分析**: [[20_Research/Papers/大模型/Maestro_Reinforcement_Learning_to_Orchestrate_Hierarchical_Model-Skill_Ensembles|Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles]]
- **作者**: Jinyang Wu, Guocheng Zhai, Ruihan Jin, Yuhao Shen, Zhengxi Lu, Fan Zhang, Haoran Luo, Zheng Lian, Zhengqi Wen, Jianhua Tao
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.45，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Maestro: Reinforcement Learning to Orchestrate Hierarchical Model-Skill Ensembles》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The proliferation of large language models (LLMs) and modular skills has endowed autonomous agents with increasingly powerful capabilities. Existing frameworks typically rely on monolithic LLMs and fixed logic to interface with these skills. This gives rise to a critical bottleneck: different LLMs offer distinct advantages across diverse domains, yet current frameworks fail to exploit the complementary strengths of models and skills, thereby limiting their performance on downstream tasks. In this paper, we present Maestro (Multimodal Agent for Expert-Skill Targeted Reinforced Orchestration), a Reinforcement Learning (RL)-driven orchestration framework that reframes heterogeneous multimodal tasks as a sequential decision-making process over a hierarchical model-skill registry. Rather than consolidating all knowledge into a single model, Maestro trains a lightweight policy to dynamically compose ensembles of frozen expert models and a two-tier skill library, deciding at each step whether to invoke an external expert, which model-skill pair to select, and when to terminate. The policy is optimized via outcome-based RL, requiring no step-level supervision. We evaluate Maestro across ten representative multimodal benchmarks spanning mathematical reasoning, chart understanding, high-resolution perception, and domain-specific analysis. With only a 4B orchestrator, Maestro achieves an average accuracy of 70.1%, surpassing both GPT-5 (69.3%) and Gemini-2.5-Pro (68.7%). Crucially, the learned coordination policy generalizes to unseen models and skills without retraining: augmenting the registry with out-of-domain experts yields a 59.5% average on four challenging benchmarks, outperforming all closed-source baselines. Maestro further maintains high computational efficiency with low latency. The source code is available at https://github.com/jinyangwu/Maestro.

</details>

---

### [[20_Research/Papers/大模型/A_Comparative_Study_of_Language_Models_for_Khmer_Retrieval-Augmented_Question_Answering|A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering]]

![[assets/2605.22099_figure.png|800]]

- **arXiv**: [2605.22099](https://arxiv.org/abs/2605.22099)
- **PDF**: https://arxiv.org/pdf/2605.22099
- **详细分析**: [[20_Research/Papers/大模型/A_Comparative_Study_of_Language_Models_for_Khmer_Retrieval-Augmented_Question_Answering|A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering]]
- **作者**: Sereiwathna Ros, Phannet Pov, Ratanaktepi Chhor, Kimleang Ly, Wan-Sup Cho, Saksonita Khoeurn
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《A Comparative Study of Language Models for Khmer Retrieval-Augmented Question Answering》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AnsSim, GEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) has emerged as a promising paradigm for grounding large language model (LLM) outputs in retrieved evidence, thereby reducing hallucination and improving factual accuracy. Its efficacy, however, remains largely unexamined for low-resource, non-Latin-script languages such as Khmer. In this paper, we present a RAG-based question answering system for Khmer-language telecom-domain documents. We conduct a two-phase comparative evaluation. First, we benchmark three embedding models: BGE-M3 (567M), Jina-Embeddings-v3 (570M), and Qwen3-Embedding (597M), for dense retrieval over Khmer documents. BGE-M3 consistently performs best, achieving a Hit Rate@3 of 0.285, File Hit Rate@3 of 0.700, MRR@3 of 0.221, and Precision@3 of 0.112, substantially outperforming the other retrievers. Second, using BGE-M3 as the selected retriever, we evaluate five generator backends: Qwen3 (8B), Qwen3.5 (9B), Sailor2-8B-Chat, SeaLLMs-v3-7B-Chat, and Llama-SEA-LION-v2-8B-IT, on a curated golden dataset of 200 Khmer question-answer pairs. To quantify system performance, we apply six RAGAS-inspired metrics: faithfulness, answer relevance, context relevance, factual correctness, answer similarity, and answer correctness. The results show no single model dominates across all metrics: Qwen3.5-9B achieves the highest faithfulness (0.859) and context relevance (0.726), Qwen3-8B attains the highest factual correctness (0.380), and SeaLLMs-v3-7B-Chat performs best on answer relevance (0.867), answer similarity (0.836), and answer correctness (0.599). These findings highlight that retriever choice remains a major bottleneck for Khmer RAG, while generator strengths vary depending on whether the priority is grounding, factual precision, or semantic similarity.

</details>

---

### [[20_Research/Papers/大模型/Faithful-MR1_Faithful_Multimodal_Reasoning_via_Anchoring_and_Reinforcing_Visual_Attention|Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention]]

![[assets/2605.22072_first_page.png|800]]

- **arXiv**: [2605.22072](https://arxiv.org/abs/2605.22072)
- **PDF**: https://arxiv.org/pdf/2605.22072
- **详细分析**: [[20_Research/Papers/大模型/Faithful-MR1_Faithful_Multimodal_Reasoning_via_Anchoring_and_Reinforcing_Visual_Attention|Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention]]
- **作者**: Changyuan Tian, Zhicong Lu, Huaxing Liu, Xiang Wang, Shuai Li, Yu Chen, Wenqian Lv, Zichuan Lin, Juncheng Diao, Deheng Ye
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.75（加权：大模型 0.55，强化学习 0.2）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Faithful-MR1: Faithful Multimodal Reasoning via Anchoring and Reinforcing Visual Attention》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) has emerged as a promising paradigm for advancing complex reasoning in large language models, and recent work extends RLVR to multimodal large language models (MLLMs). This transfer, however, surfaces a faithfulness challenge: faithful perception of task-relevant visual evidence and faithful use of that evidence during reasoning, leading to unsatisfactory gains on multimodal benchmarks. Specifically, existing perception supervision often operates on textual descriptions rather than natively on image regions, and faithful use is largely overlooked, exposing the perception-reasoning disconnect where correctly perceived evidence is dropped or contradicted during reasoning. To close these gaps, we propose Faithful-MR1, a training framework that anchors and reinforces visual attention to address both halves of faithful multimodal reasoning. The Anchoring stage turns perception into an explicit pre-reasoning subtask, supervising a dedicated &lt;Focus&gt; token's attention directly against image regions rather than through textual descriptions. The Reinforcing stage exposes faithful use through counterfactual image intervention, rewarding answer-correct trajectories that concentrate visual attention where vision causally matters. Extensive experiments demonstrate that Faithful-MR1 outperforms recent multimodal reasoning baselines on both Qwen2.5-VL-Instruct 3B and 7B backbones while using substantially less training data.

</details>

---

### [[20_Research/Papers/大模型/FlyRoute_Self-Evolving_Agent_Profiling_via_Data_Flywheel_for_Adaptive_Task_Routing|FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing]]

![[assets/2605.22057_figure.png|800]]

- **arXiv**: [2605.22057](https://arxiv.org/abs/2605.22057)
- **PDF**: https://arxiv.org/pdf/2605.22057
- **详细分析**: [[20_Research/Papers/大模型/FlyRoute_Self-Evolving_Agent_Profiling_via_Data_Flywheel_for_Adaptive_Task_Routing|FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing]]
- **作者**: Rongjun Li, Ziyu Zhou, Yihang Wu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《FlyRoute: Self-Evolving Agent Profiling via Data Flywheel for Adaptive Task Routing》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise routers assign queries to expert agents, yet deployed profiles stay static while agents evolve (prompts, tools, models), and developers rarely keep descriptions or exemplars current. We present FlyRoute, a self-evolving profiling framework that grows capability evidence from real traffic: dispatch candidates, quality-gate successful pairs into each agent's success store, periodically distill evidence into learned capability descriptions, and inject those descriptions together with BM25-retrieved successes into an LLM router. To make this flywheel data-efficient, FlyRoute introduces a targeted exploration policy that combines profile uncertainty, BM25 relevance, and lexical novelty, prioritizing under-profiled agents only for plausible queries and avoiding redundant evidence collection. In experiments on our proprietary enterprise developer-support dataset of real routed queries, FlyRoute improves a same-backbone zero-shot LLM router from 72.57% to 78.04% with only five seed queries per agent, showing that profile retrieval already strengthens cold-start routing. After streaming 7,211 labeled training queries through the flywheel, accuracy rises to 89.83% (+17.26pp over zero-shot; +11.79pp over cold start), with consistent gains across four expert domains under standard routing accuracy on single-gold test queries.

</details>

---

### [[20_Research/Papers/大模型/Check_Your_LLM's_Secret_Dictionary!_Five_Lines_of_Code_Reveal_What_Your_LLM_Learned_(Including_What_It_Shouldn't_Have)|Check Your LLM's Secret Dictionary! Five Lines of Code Reveal What Your LLM Learned (Including What It Shouldn't Have)]]

![[assets/2605.22005_figure.png|800]]

- **arXiv**: [2605.22005](https://arxiv.org/abs/2605.22005)
- **PDF**: https://arxiv.org/pdf/2605.22005
- **详细分析**: [[20_Research/Papers/大模型/Check_Your_LLM's_Secret_Dictionary!_Five_Lines_of_Code_Reveal_What_Your_LLM_Learned_(Including_What_It_Shouldn't_Have)|Check Your LLM's Secret Dictionary! Five Lines of Code Reveal What Your LLM Learned (Including What It Shouldn't Have)]]
- **作者**: Hisashi Miyashita
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Check Your LLM's Secret Dictionary! Five Lines of Code Reveal What Your LLM Learned (Including What It Shouldn't Have)》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We show that singular value decomposition of the lm_head} weight matrix of a transformer-based large language model -- requiring only five lines of PyTorch and no model inference -- reveals interpretable semantic subspaces directly from the model weights. Each left singular vector identifies the vocabulary tokens most readily selected when the hidden state aligns with the corresponding singular direction; inspecting these clusters exposes the model's training data composition and curation philosophy. Analysing GPT-OSS-120B, Gemma-2-2B, and Qwen2.5-1.5B, we find that singular value spectra and vocabulary cluster structures differ systematically across models: GPT exhibits a graduated hierarchy of functionally differentiated subspaces; Gemma is dominated by pre-nineteenth-century English orthography, forming a stepwise clustering structure that may contribute to high output controllability; and Qwen exhibits broad multilingual coverage alongside subspaces whose vocabulary the authors have determined to be ethically inappropriate for direct publication. Base-instruct comparison reveals that ethically concerning subspaces originate in pretraining and are not removed by post-training alignment. We introduce the Vocabulary Cluster Score (VCS) to quantify subspace coherence, and the Weighted Projection Score (WPS) as a static glitch token detector; applying WPS to GPT-OSS-120B recovers shokubutsu-hyakka-tsu (ID 137606), a well-known glitch token widely reported in the CJK language community, without any model inference. We propose a taxonomy of root causes for problematic vocabulary content and call for lm_head} SVD analysis to be adopted as a standard pre-release safety auditing step. Our findings further suggest directions toward SVD-guided tokenizer optimisation and more controllable LLM design.

</details>

---

### [[20_Research/Papers/强化学习/Why_Semantic_Entropy_Fails_Geometry-Aware_and_Calibrated_Uncertainty_for_Policy_Optimization|Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization]]

![[assets/2605.21801_figure.png|800]]

- **arXiv**: [2605.21801](https://arxiv.org/abs/2605.21801)
- **PDF**: https://arxiv.org/pdf/2605.21801
- **详细分析**: [[20_Research/Papers/强化学习/Why_Semantic_Entropy_Fails_Geometry-Aware_and_Calibrated_Uncertainty_for_Policy_Optimization|Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization]]
- **作者**: Zheyuan Zhang, Kaiwen Shi, Han Bao, Zehong Wang, Tianyi Ma, Yanfang Ye
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Why Semantic Entropy Fails: Geometry-Aware and Calibrated Uncertainty for Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：NarrativeQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training has become central to improving reasoning and alignment in large language models, where critic-free models enable scalable learning from model-generated outputs but lack principled mechanisms to distinguish informative from noisy signals. Recent approaches leverage response-level measures as uncertainty signals to regulate group-based optimization methods such as GRPO. Yet their empirical success remains unstable and unclear in how they influence optimization dynamics. In this paper, we provide, to our knowledge, the first principled formulation that interprets uncertainty signals as mechanisms for characterizing and regulating gradient variance and learning signal quality. Based on both empirical and theoretical analysis, we identify two critical gaps of current entropy-based estimators: The anisotropic gap and The calibration gap. Motivated by this analysis, we propose Geometric-aware Calibrated Policy Optimization (GCPO), a novel framework integrating geometry-aware measures to capture semantic disagreement with reward-based calibration to align uncertainty with learning signal strength. Experiments on multiple benchmarks show that our approach more faithfully tracks gradient variability and consistently improves post-training performance. Our results highlight the importance of designing uncertainty signals that are aligned with optimization dynamics, offering a principled perspective for robust post-training.

</details>

---
