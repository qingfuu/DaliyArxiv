# cs.CL | Computation and Language | 2026-08-10

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/大模型/An_Exploratory_Evaluation_of_LLM-Assisted_Rewriting_of_Moderate-Complexity_Financial_Sentences_for_DisCoCat-Based_Sentiment_Analysis|An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis]]

![[assets/2608.07439_figure.png|800]]

- **arXiv**: [2608.07439](https://arxiv.org/abs/2608.07439)
- **PDF**: https://arxiv.org/pdf/2608.07439
- **详细分析**: [[20_Research/Papers/大模型/An_Exploratory_Evaluation_of_LLM-Assisted_Rewriting_of_Moderate-Complexity_Financial_Sentences_for_DisCoCat-Based_Sentiment_Analysis|An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis]]
- **作者**: Brian Llinas, Nikos Chrisochoides
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《An Exploratory Evaluation of LLM-Assisted Rewriting of Moderate-Complexity Financial Sentences for DisCoCat-Based Sentiment Analysis》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantum natural language processing (QNLP) provides a grammar-aware framework for text modeling, and Distributional Compositional Categorical (DisCoCat) is one of its theoretically grounded formulations. Prior work on financial sentiment analysis has identified practical limitations of DisCoCat, including parser sensitivity, high simulation cost, and difficulty handling longer sentences. We study an LLM-assisted preprocessing workflow that uses controlled rewriting to compress, simplify, or decompose moderate-complexity financial sentiment sentences into parser-compatible, circuit-efficient variants while preserving sentiment-bearing meaning. We compare prompting strategies, language models, and filtering configurations with the low-complexity-only DisCoCat baseline of Stein et al. At the circuit level, the strongest compression variants reduce average qubit and gate counts by more than 70 percent relative to the raw moderate-complexity subset. Across repeated training runs, GPT-4.1-mini with Prompt B achieves the highest observed mean accuracy, $0.550 \pm 0.035$, compared with $0.521 \pm 0.050$ for the baseline. Larger training splits do not necessarily improve downstream performance; across evaluated configurations, training-split size has a moderately negative association with accuracy (Pearson $r=-0.446$). These results provide exploratory evidence that LLM-assisted rewriting can make some moderate-complexity inputs usable within the evaluated DisCoCat configuration, while highlighting prompt design, filtering, and circuit-aware preprocessing as considerations for more scalable QNLP-based financial sentiment analysis.

</details>

---

### [[20_Research/Papers/强化学习/Trajectory-Relative_Hindsight_Distillation_for_Agentic_Reinforcement_Learning|Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning]]

![[assets/2608.07371_figure.png|800]]

- **arXiv**: [2608.07371](https://arxiv.org/abs/2608.07371)
- **PDF**: https://arxiv.org/pdf/2608.07371
- **详细分析**: [[20_Research/Papers/强化学习/Trajectory-Relative_Hindsight_Distillation_for_Agentic_Reinforcement_Learning|Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning]]
- **作者**: Haoyu Zheng, Yun Zhu, Qing Wang, Wenqiao Zhang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Trajectory-Relative Hindsight Distillation for Agentic Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent agentic reinforcement learning methods use hindsight to complement sparse outcome rewards. However, a completed rollout can yield many such signals, leaving their appropriate allocation across turns unclear. We introduce TRIAL, a trajectory-relative hindsight distillation framework with a unified turn-aligned scoring protocol. For each decision turn, TRIAL extracts an outcome view of that decision's realized consequence and evaluates the same response under ordinary and hindsight-conditioned contexts. The signed log-probability gap determines the direction and local strength of token-level supervision, while turn-level magnitudes are normalized jointly over the realized trajectory. The resulting allocation multipliers have an eligible-token-weighted mean of one, redistributing dense supervision across turns while fixing its average multiplier. Experiments on WebShop and ALFWorld with different backbones show that TRIAL outperforms GRPO across all eight combinations of backbone, environment, and evaluation metric, while achieving the best or tied-best performance among six methods on six of them. On WebShop with Qwen3-1.7B, TRIAL improves the success rate from 56.4% to 75.2% and the task score from 78.7% to 85.7%. Controlled ablations further show that trajectory-relative turn allocation provides substantial gains beyond those of dense hindsight distillation alone.

</details>

---

### [[20_Research/Papers/大模型/Does_More_Retrieved_Evidence_Help_Visual_Retrieval-Augmented_Generation_with_Diffusion_Language_Models|Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?]]

![[assets/2608.07006_figure.png|800]]

- **arXiv**: [2608.07006](https://arxiv.org/abs/2608.07006)
- **PDF**: https://arxiv.org/pdf/2608.07006
- **详细分析**: [[20_Research/Papers/大模型/Does_More_Retrieved_Evidence_Help_Visual_Retrieval-Augmented_Generation_with_Diffusion_Language_Models|Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?]]
- **作者**: Jiankun Wang, Yisen Gao, Ziwei Zhang, Xingcheng Fu, Jiaxin Bai, Chen Gao
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Does More Retrieved Evidence Help Visual Retrieval-Augmented Generation with Diffusion Language Models?》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ChartQA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual retrieval-augmented generation (RAG) commonly expands the retrieved evidence set to improve answer-page coverage, implicitly assuming that all available evidence should be passed to the generator. We show that this assumption does not hold for diffusion language models (DLMs): retrieving more pages increases answer-page recall, whereas unconditionally passing all retrieved pages to the generator often reduces answer accuracy, primarily because of semantic conflict. A latent-source analysis explains this mismatch through source-coherence loss in parallel denoising, where position-wise proposals can combine incompatible visual sources into unsupported answers. We further find that such interference is already visible in the first-step answer-block distribution, making it possible to assess evidence before decoding. To preserve retrieval coverage while limiting harmful visual exposure, we propose the Entropy-Based Candidate Filter (ECF), a training-free evidence-admission framework. To reduce irrelevant content within individual candidates, ECF constructs multi-granularity evidence units; to identify beneficial additional evidence, it uses blank-controlled block confidence and retrieval rank to determine whether and which candidate should enter the final context. Across three multimodal DLMs and five visual QA benchmarks, ECF improves answer accuracy by 2.62 percentage points on average over the strongest fixed top-$k$ input and, with LLaDA2.0-Uni, by 2.37 percentage points on average over the best competing training-free result for each dataset. These results show that broader retrieval benefits visual DLM-RAG through selective evidence admission rather than unconditional evidence expansion. Code is publicly available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/How_Should_I_Pick_a_Foundation_Model_for_My_Robot_In_Favor_of_a_Community_Evaluation_Framework_for_Social_Robots|How Should I Pick a Foundation Model for My Robot? In Favor of a Community Evaluation Framework for Social Robots]]

![[assets/2608.06898_figure.png|800]]

- **arXiv**: [2608.06898](https://arxiv.org/abs/2608.06898)
- **PDF**: https://arxiv.org/pdf/2608.06898
- **详细分析**: [[20_Research/Papers/具身智能/How_Should_I_Pick_a_Foundation_Model_for_My_Robot_In_Favor_of_a_Community_Evaluation_Framework_for_Social_Robots|How Should I Pick a Foundation Model for My Robot? In Favor of a Community Evaluation Framework for Social Robots]]
- **作者**: Eric Nichols, Alva Markelius, Hatice Gunes
- **cs 子类**: cs.CL, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.15（加权：具身智能 0.6，大模型 0.45，机器人 1.1）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《How Should I Pick a Foundation Model for My Robot? In Favor of a Community Evaluation Framework for Social Robots》归入 机器人、具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CommonsenseQA, HumanEval, IFEval, LiveBench, MinorBench, OR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Researchers who seek to build social robot applications on foundation models are faced with a difficult question: how should we pick a model? Public leaderboards offer little guidance: the demands of real-time, embodied social interaction lie largely outside their focus. And direct evaluation is impractical at scale: each embodied study requires scarce participant, robot, and experimenter time. In this paper, we identify five evaluation dimensions for foundation models in social robots: (i) conversational competence, (ii) user safety, (iii) embodied character, (iv) target scene effectiveness, and (v) audience appropriateness. To make model selection cheaper and better informed, we propose a three-tiered evaluation funnel paradigm that first filters with general metrics, then extends to simulated interactions, and terminates in more expensive, robot-specific evaluation. We map all five dimensions across all three tiers, chart where applicable evaluation methods exist and are missing, and close with a call to action: let's build the evaluation framework together as a community.

</details>

---

### [[20_Research/Papers/大模型/LLMRouter_Unified_Infrastructure_for_Developing,_Evaluating,_and_Deploying_LLM_Routers|LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers]]

![[assets/2608.06867_figure.png|800]]

- **arXiv**: [2608.06867](https://arxiv.org/abs/2608.06867)
- **PDF**: https://arxiv.org/pdf/2608.06867
- **详细分析**: [[20_Research/Papers/大模型/LLMRouter_Unified_Infrastructure_for_Developing,_Evaluating,_and_Deploying_LLM_Routers|LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers]]
- **作者**: Tao Feng, Fangxu Yu, Haozhen Zhang, Zhongjie Dai, Liangqi Yuan, Zijie Lei, Weizhi Zhang, Kunlun Zhu, Haodong Yue, Keyang Xuan, Ge Liu, Jiaxuan You
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《LLMRouter: Unified Infrastructure for Developing, Evaluating, and Deploying LLM Routers》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

No single large language model (LLM) is optimal across all queries and budget constraints, making model routing essential for cost-effective deployment. Existing routers adopt diverse formulations and implementations, making fair comparison and extension difficult. We present a unified formulation of LLM routing as a sequential decision process characterized by five components: context encoders, model encoders, scoring functions, decision rules, and learning signals, covering single-turn, multi-turn, and personalized routing. Based on this formulation, we develop an automated pipeline for constructing routing supervision and evaluating routers jointly on response quality and inference cost. The resulting benchmark, xRouteBench, spans generic LLM, memory-augmented, vision, time-series, and personalized routing tasks. We further introduce LLMRouter, an open-source modular infrastructure with more than 16 representative routers. Our empirical study shows that learned routers outperform the strongest fixed-model baseline by 14.6% relatively, lightweight routers become more competitive under tight cost constraints, and user-conditioned routing consistently improves personalization.

</details>

---

### [[20_Research/Papers/大模型/Retrieval-Constrained_Policy_Optimization_for_Attack_Technique_Extraction_from_Cyber_Threat_Intelligence|Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence]]

![[assets/2608.06778_figure.png|800]]

- **arXiv**: [2608.06778](https://arxiv.org/abs/2608.06778)
- **PDF**: https://arxiv.org/pdf/2608.06778
- **详细分析**: [[20_Research/Papers/大模型/Retrieval-Constrained_Policy_Optimization_for_Attack_Technique_Extraction_from_Cyber_Threat_Intelligence|Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence]]
- **作者**: Jiayun Zhang, Junshen Xu, Zejun Xie, Yi Fan
- **cs 子类**: cs.CL, cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.35（加权：大模型 0.35，强化学习 1）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《Retrieval-Constrained Policy Optimization for Attack Technique Extraction from Cyber Threat Intelligence》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mapping cyber threat intelligence (CTI) text to MITRE ATT&amp;CK techniques is essential for structured threat analysis, yet manual annotation is costly and does not scale. The ATT&amp;CK taxonomy comprises several hundred attack techniques, and a single CTI passage may describe multiple techniques, making accurate and complete extraction challenging. Existing automated approaches fall short in different ways: multi-label classifiers struggle with severe class imbalance and the large label space, while LLM-based methods--retrieval pipelines and fine-tuned generators--optimize token-level objectives that treat technique annotation as sequence generation rather than set prediction, lacking direct supervision on whether the predicted technique set is correct and complete. We propose TTP-R1, a two-stage framework that combines retrieval-augmented supervised fine-tuning (SFT) with reinforcement learning using verifiable rewards (RLVR). A hybrid retriever first narrows the large label space to a candidate set, and a fine-tuned LLM learns to select the correct techniques. We then apply Group Relative Policy Optimization with a decomposed reward that directly supervises the precision, recall, and output format of the predicted technique set. Across four CTI benchmarks, TTP-R1 achieves the best average F1, improving sub-technique-level F1 by 7.4 percentage points over Claude Sonnet 4.5 with retrieval augmentation, while running 28x faster when served as an 8B-parameter model on a single GPU.

</details>

---

### [[20_Research/Papers/大模型/TA-RAG_Tone_Awareness_as_a_Design_Imperative_for_Retrieval-Augmented_Generation|TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation]]

![[assets/2608.06672_figure.png|800]]

- **arXiv**: [2608.06672](https://arxiv.org/abs/2608.06672)
- **PDF**: https://arxiv.org/pdf/2608.06672
- **详细分析**: [[20_Research/Papers/大模型/TA-RAG_Tone_Awareness_as_a_Design_Imperative_for_Retrieval-Augmented_Generation|TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation]]
- **作者**: Yong-Bin Kang, Anthony McCosker
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Systems

#### 研究背景与动机

《TA-RAG: Tone Awareness as a Design Imperative for Retrieval-Augmented Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) has become a robust architecture for grounding large language models (LLMs) in trusted knowledge. However, standard RAG systems exhibit a structural limitation: retrieved documents carry their own communication styles-professional jargon, formal tone, or academic writings-that shape the behavior of a RAG system before any tone instructions are processed, often causing the system to ignore user requests for a specific tone. We term this phenomenon contextual decoupling, in which a system optimises for factual accuracy while remaining decoupled from the social or operational context of the recipient. Building on prior research in public health peer-support communities, we identify three communicative misalignment-linguistic, cognitive, and relational-that can persist even when retrieval is relevant and the generated response is factually accurate. We conceptualise these as failures of communicative transformation, which remain largely invisible to accuracy-centred RAG evaluation metrics. To address this gap, we propose Tone-Aware RAG (TA-RAG), a conceptual architectural framework that positions communicative alignment alongside factual accuracy as a core design objective. TA-RAG operationalises four constraints-stigma-free language, readability alignment, recipient-sensitive adaptation, and empathetic framing-across the retrieval, context construction, generation, and constraint validation phases in the proposed RAG pipeline. We further highlight an evaluation agenda for jointly assessing factual fidelity and communicative alignment, and identify open challenges. We argue that tone awareness should be treated not as an optional refinement, but as a present design imperative for RAG systems operating in socially sensitive and high-stakes contexts.

</details>

---

### [[20_Research/Papers/大模型/The_Horizon_Gap_Planning,_Memory,_Execution,_Training,_and_Evaluation_for_Long-Horizon_LLM_Agents|The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents]]

![[assets/2608.06663_figure.png|800]]

- **arXiv**: [2608.06663](https://arxiv.org/abs/2608.06663)
- **PDF**: https://arxiv.org/pdf/2608.06663
- **详细分析**: [[20_Research/Papers/大模型/The_Horizon_Gap_Planning,_Memory,_Execution,_Training,_and_Evaluation_for_Long-Horizon_LLM_Agents|The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents]]
- **作者**: Mingguang Chen, Licheng Wang, Bo Qu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《The Horizon Gap: Planning, Memory, Execution, Training, and Evaluation for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier language models solve reasoning problems in a single forward pass that would have been research contributions years ago, yet fail at multi-hour tasks: losing track of earlier decisions, declaring half-finished work done, or drifting from goals. We call this the horizon gap and survey 1,547 arXiv papers (2024-2026) collected via systematic seed harvest with a disclosed 26.8% bleed filter, extended by targeted supplementation. We disambiguate three routinely conflated properties: long-horizon (task property: required steps), long-context (model property: token capacity), and long-term memory (system property: persistence across steps/sessions). We organize the corpus into six categories tracking a long-horizon task's lifecycle -- planning, memory, execution, training, evaluation, and foundations/safety -- crossed with an axis capturing where horizons are carried (within-context, within-task-beyond-context, or cross-task-persistent). Across all categories, we find the same pattern: outcome-only signals grow uninformative as horizons lengthen, and the field's response -- whether process reward models, credit assignment, or trajectory-level diagnostics -- manufactures denser step-level signals. We treat critical and diagnostic literature as first-class threads throughout, arguing that segregating critique from method would routinely split single papers across chapters. We close by naming open measurement problems: decomposing model versus harness capability, managing correlated bias in process-level signals used for both training and evaluation, and whether long-horizon reliability admits general predictive theory.

</details>

---

### [[20_Research/Papers/大模型/GRASP_Reinforcing_Language_Model_Anonymizers_with_Group_Relative_Policy_Optimization|GRASP: Reinforcing Language Model Anonymizers with Group Relative Policy Optimization]]

![[assets/2608.06526_figure.png|800]]

- **arXiv**: [2608.06526](https://arxiv.org/abs/2608.06526)
- **PDF**: https://arxiv.org/pdf/2608.06526
- **详细分析**: [[20_Research/Papers/大模型/GRASP_Reinforcing_Language_Model_Anonymizers_with_Group_Relative_Policy_Optimization|GRASP: Reinforcing Language Model Anonymizers with Group Relative Policy Optimization]]
- **作者**: Sajjad Ghiasvand, Nader Sehatbakhsh
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.45（加权：大模型 0.65，强化学习 0.8）
- **关联关键词**: LLM, RL, Security

#### 研究背景与动机

《GRASP: Reinforcing Language Model Anonymizers with Group Relative Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models can infer sensitive personal attributes, such as age, location, and occupation, from ordinary text, turning everyday writing into a privacy risk. Adversarial anonymization defends against this by rewriting a text with a capable language model that also plays the attacker, but it needs a powerful model at inference time and thus sends private text to a third party, the very exposure anonymization should prevent. Recent work distills this behavior into a small on-device model using supervised fine-tuning and direct preference optimization (DPO), but DPO only imitates the teacher's offline choices and never directly optimizes the privacy--utility objective we care about. We introduce \textbf{GRASP} (\textbf{G}roup-\textbf{R}elative \textbf{A}nonymization via \textbf{S}elf-refinement \textbf{P}olicy-optimization), which reinforces the local anonymizer online with Group Relative Policy Optimization. A single small model acts as anonymizer, adversary, and utility judge, trained against a self-generated reward that hides attributes while preserving meaning, with a design that guards against reward hacking. Trained on Llama-3.1-8B, \ours{} improves the privacy--utility trade-off over the DPO-distilled baseline, consistently across three independent LLM judges. Against adversarial anonymization driven by frontier models such as Gemini~2.5~Flash and Claude, it achieves a comparable or better overall trade-off while removing substantially more private information, and it runs entirely on-device at roughly $1\%$ of the GPT-4o teacher's cost.

</details>

---
