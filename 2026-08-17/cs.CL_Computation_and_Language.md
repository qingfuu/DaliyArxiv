# cs.CL | Computation and Language | 2026-08-17

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/大模型/You_Only_Pass_Once_Answering_and_Abstaining_Together_in_a_Single_Forward_Pass_of_a_Frozen_Language_Model|You Only Pass Once: Answering and Abstaining Together in a Single Forward Pass of a Frozen Language Model]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2608.14465](https://arxiv.org/abs/2608.14465)
- **PDF**: https://arxiv.org/pdf/2608.14465
- **详细分析**: [[20_Research/Papers/大模型/You_Only_Pass_Once_Answering_and_Abstaining_Together_in_a_Single_Forward_Pass_of_a_Frozen_Language_Model|You Only Pass Once: Answering and Abstaining Together in a Single Forward Pass of a Frozen Language Model]]
- **作者**: Ziyang Luo, Zhongyao Chu, Xinjie He, Youting Wang, Xukui Qin, Runxiong Wu, Yan-Syuan Chen
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《You Only Pass Once: Answering and Abstaining Together in a Single Forward Pass of a Frozen Language Model》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：RepLiQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A frozen language model on reasoning tasks has two coupled weaknesses: it under-uses evidence its own residual stream already encodes, and it fails to detect when the input is insufficient to answer, so it confabulates. This paper consolidates two research lines that address these on the same residual stream: a conditional steering probe writes the stream at mid-stack layers and recovers reasoning accuracy from a frozen backbone, and a zero-shot sufficiency direction reads the stream and abstains when information is insufficient. Deployed in one forward pass they interfere: the steering write shifts the state the direction reads, costing up to 8 AUROC points of cross-domain transfer on small models; a separate clean pass doubles inference cost. We keep the direction fixed and train a small network to reconstruct the pre-steering residual from the steered one -- mean-squared error on (steered, clean) pairs, no sufficiency labels -- and read the direction on the reconstruction. The resulting system, YOPO (You Only Pass Once), answers, steers, and abstains in one forward pass of a frozen Qwen2.5 backbone (1.5B/3B/7B). End to end, three-way accuracy more than doubles the frozen baseline (0.375-&gt;0.798 on 1.5B alphaNLI) and one pass beats the two-pass reference at every scale (0.798/0.830/0.893 vs 0.753/0.790/0.863) and on ten backbones across six model families. We chart the capacity-transfer frontier quantifying the principle that abstention should not be trained in; a source-side audit catches our own alphaNLI construction leaking a surface artifact, so architectural claims are anchored on native-label replications (SQuAD2, RepLiQA, MuSiQue); and on the standard four-domain suite we contribute, to our knowledge, the first answer-or-abstain benchmark, where our gate tops every in-domain dataset and the label-free direction is the only gate family to survive domain transfer.

</details>

---

### [[20_Research/Papers/大模型/Local_and_Global_Regimes_of_Geometric_Complexity_in_Language_Model_Representations|Local and Global Regimes of Geometric Complexity in Language Model Representations]]

![[assets/2608.14361_first_page.png|800]]

- **arXiv**: [2608.14361](https://arxiv.org/abs/2608.14361)
- **PDF**: https://arxiv.org/pdf/2608.14361
- **详细分析**: [[20_Research/Papers/大模型/Local_and_Global_Regimes_of_Geometric_Complexity_in_Language_Model_Representations|Local and Global Regimes of Geometric Complexity in Language Model Representations]]
- **作者**: Arwa Osman, Marco Baroni, Iuri Macocco
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM

#### 研究背景与动机

《Local and Global Regimes of Geometric Complexity in Language Model Representations》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Intrinsic dimensionality (ID) is widely used to probe the representational complexity of language models, but it remains unclear whether ID differences reflect properties of language itself or artefacts of how the underlying dataset was constructed. In this paper, we focus specifically on how lexical diversity, the number of unique last-token items present in a dataset, affects ID estimates of that dataset. We find a scale-dependent transition between two regimes: at low lexical diversity, conditions with fewer unique final words produce higher ID, while at high lexical diversity, this ordering reverses, and conditions with more unique words produce higher ID. We derive an exact, parameter-free formula for the point at which this reversal occurs, which matches the observed transition point at every scale tested. On the one hand, our results highlight how care must be taken when interpreting the intrinsic dimensionality of a set of representations as a straightforward cue of their complexity. On the other hand, our discovery of the two ID regimes reveals a general principle of organisation of linguistic data in LLMs that sheds new light on their inner manifold structures.

</details>

---

### [[20_Research/Papers/强化学习/Envs-FORGE_Frontier-Optimized_Reward-Grounded_Environment_Synthesis_for_Agent_RL|Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent RL]]

![[assets/2608.14312_figure.png|800]]

- **arXiv**: [2608.14312](https://arxiv.org/abs/2608.14312)
- **PDF**: https://arxiv.org/pdf/2608.14312
- **详细分析**: [[20_Research/Papers/强化学习/Envs-FORGE_Frontier-Optimized_Reward-Grounded_Environment_Synthesis_for_Agent_RL|Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent RL]]
- **作者**: Xiaojun Wu, Cehao Yang, Honghao Liu, Xueyuan Lin, Zhichao Shi, Hao Zhou, Xuhui Jiang, Chengjin Xu, Jia Li, Jian Guo
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Envs-FORGE: Frontier-Optimized Reward-Grounded Environment Synthesis for Agent RL》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Agent-World, CLI-Gym, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) for terminal agents needs executable training environments with reliable rewards and useful difficulty. Fixed recipes such as few-shot, Self-Instruct, and Evol-Instruct apply the same prompting policy to every seed, even when the current policy would benefit from a harder, easier, or simply different task. We present Envs-FORGE, a prompting policy that converts verifier rewards into per-seed environment-synthesis actions. Envs-FORGE estimates seed pass rates, scores six projection--direction actions around a target learning frontier, and solves a per-seed mixed-integer linear program (MILP) to choose the action that conditions generation. The selected action drives synchronized rewriting of the instruction, fixtures, oracle solution, tests, and Docker environment; only gold-verified bundles enter RL training. The indexed MILP form also supports optional soft skill coverage for portfolio planning. On Qwen 3.5 35B, Envs-FORGE improves Pass@1 over Base by 9.2 percentage points on tb-core (40.0% to 49.2%) and 6.4 points on tb-2.0 (23.0% to 29.4%), exceeding the strongest fixed-recipe baseline by 2.4 and 2.1 points. It reaches 77.1% on SWE-bench Verified versus 73.4% for Base, and improves tb-core by 6.8--9.2 points across the evaluated 4B--35B models. All synthesis methods export 100 verified environments and use 2.27M--2.88M synthesis tokens, placing the comparison at the same downstream training-set size and the same operational scale. The source code is available at https://github.com/DataArcTech/DataArc-SynData-Toolkit/.

</details>

---

### [[20_Research/Papers/大模型/The_More_Popular,_The_Harder_to_Forget_Adaptive_Popularity_for_LLM_Unlearning|The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning]]

![[assets/2608.14229_figure.png|800]]

- **arXiv**: [2608.14229](https://arxiv.org/abs/2608.14229)
- **PDF**: https://arxiv.org/pdf/2608.14229
- **详细分析**: [[20_Research/Papers/大模型/The_More_Popular,_The_Harder_to_Forget_Adaptive_Popularity_for_LLM_Unlearning|The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning]]
- **作者**: Anna Borisiuk, Andrey Savchenko, Alexander Panchenko, Elena Tutubalina
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《The More Popular, The Harder to Forget: Adaptive Popularity for LLM Unlearning》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Popular facts are memorised more deeply during pretraining and resist removal longer than rare ones, yet existing LLM unlearning methods apply uniform gradient pressure regardless of training-data frequency. We propose the AdaPop (Adaptive Popularity) method, which combines local token confidence with a per-fact popularity-dependent exponent derived from an external proxy (e.g., Wikidata sitelinks, LLM-as-Judge), and automates the forget-retain balance via a dual-ascent controller that adjusts the retain penalty each epoch. Across three model families and two benchmarks, AdaPop leaks ~5x less forgotten content than competing methods under paraphrased queries and ~1.6x less under adversarial reformulations. We support our analysis with internal metrics: under our method, forget-set hidden states move further from the pre-unlearning model's states than under other methods, while retain-set representations remain close.

</details>

---

### [[20_Research/Papers/大模型/MINT_A_Universal_Zero-Shot_Predictor_for_Transaction_Data|MINT: A Universal Zero-Shot Predictor for Transaction Data]]

![[assets/2608.14198_figure.png|800]]

- **arXiv**: [2608.14198](https://arxiv.org/abs/2608.14198)
- **PDF**: https://arxiv.org/pdf/2608.14198
- **详细分析**: [[20_Research/Papers/大模型/MINT_A_Universal_Zero-Shot_Predictor_for_Transaction_Data|MINT: A Universal Zero-Shot Predictor for Transaction Data]]
- **作者**: Parameswaran Kamalaruban, Viktor Drobnyi, Maeve Madigan, Julia Rozanova, David Sutton, Stuart Burrell
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《MINT: A Universal Zero-Shot Predictor for Transaction Data》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Banks analyse sequential financial transaction data to perform many tasks, including fraud prevention, credit risk assessment and offer personalization. To improve the predictive accuracy of these tasks, Payments Foundation Models encode transaction sequence data as rich contextual embeddings, which can then be provided to task-specific models as features. However, these Foundation Models are not designed for flexible zero-shot reasoning across novel downstream prediction tasks, limiting their adaptability and utility. Existing LLM-based approaches to zero-shot prediction often fail to fully exploit the predictive signal within transaction data, while relying on costly text serialization or task-specific architectures that scale poorly. To address these limitations, we present the Multimodal Instruction Network for Transactions (MINT), a framework that connects a pretrained transaction sequence encoder to a decoder-only LLM through lightweight embedding injection, transaction-language alignment, and instruction tuning. We find that MINT achieves state-of-the-art predictive question-answering performance in both in-distribution and out-of-distribution questions, while substantially reducing input tokens, latency, and memory consumption compared to text-serialization baselines. Through comprehensive analyses of representations, alignment strategies, training data, and history length, we establish that compact transaction embeddings are a superior approach to transaction representation than text serialization for multimodal reasoning and zero-shot prediction tasks.

</details>

---

### [[20_Research/Papers/大模型/HERMES_a_multi-agent_framework_for_structured_knowledge_extraction_from_ultra-long_documents_in_geoscience|HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience]]

![[assets/2608.14055_first_page.png|800]]

- **arXiv**: [2608.14055](https://arxiv.org/abs/2608.14055)
- **PDF**: https://arxiv.org/pdf/2608.14055
- **详细分析**: [[20_Research/Papers/大模型/HERMES_a_multi-agent_framework_for_structured_knowledge_extraction_from_ultra-long_documents_in_geoscience|HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience]]
- **作者**: Ziqi Song, Zongyuan Xiang, James G. Ogg, Bruce S. Lieberman, Gabi Ogg, Natalia López Carranza, Wen Du, Yufei Ye, Shuan Li, Zhong Peng, Shaoqi Yu, Juye Wei...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《HERMES: a multi-agent framework for structured knowledge extraction from ultra-long documents in geoscience》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Authoritative scientific knowledge in geoscience remains largely trapped in legacy monographs and historical literature, where unstructured text and complex layouts hinder computational access. We introduce HERMES, a scalable multi-agent framework that extracts structured data from ultra-long scientific documents. Using a coordinating large language model, HERMES integrates domain constraints, validation rules and evidence tracing within a unified document-level extraction process that incorporates parsed text, tables, figures and captions. Applied to the 55-volume Treatise on Invertebrate Paleontology, the system produced a structured database of 32,277 fossil taxonomic entities and 451,878 attributes, released online at https://treatise.geolex.org. Extraction performance remained stable across fossil groups (average F1 scores of approximately 0.90 for entities and 0.91 for attributes), improving per-volume efficiency approximately sixfold relative to the tested fully manual baseline. Evaluation in palaeomagnetism and geochemistry, conducted without additional model training, demonstrated transfer across distinct geoscience domains. This work provides a practical pathway to transform historical scientific literature into FAIR-oriented structured data, offering a sustainable infrastructure for data-intensive disciplines and large-scale knowledge integration.

</details>

---

### [[20_Research/Papers/大模型/S2Dialog_Multimodal_Dialogue_Retrieval_with_Semantic_and_Acoustic-Style_Modeling|S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling]]

![[assets/2608.14029_figure.png|800]]

- **arXiv**: [2608.14029](https://arxiv.org/abs/2608.14029)
- **PDF**: https://arxiv.org/pdf/2608.14029
- **详细分析**: [[20_Research/Papers/大模型/S2Dialog_Multimodal_Dialogue_Retrieval_with_Semantic_and_Acoustic-Style_Modeling|S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling]]
- **作者**: Xueqi Wang, Zhigang Wang, Runqing Zhang, Zhenqi Jia, Junfeng Zhao
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal

#### 研究背景与动机

《S2Dialog: Multimodal Dialogue Retrieval with Semantic and Acoustic-Style Modeling》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal dialogue retrieval aims to retrieve dialogues from multimodal dialogue banks that are similar to a target dialogue in terms of both textual semantics and acoustic conversational styles. Such dialogue-level retrieval is crucial for many dialogue-related tasks, including Emotion Recognition in Conversation, Spoken Dialogue Systems, and Conversational Speech Synthesis, where external dialogue examples can provide valuable semantic and stylistic references. However, existing retrieval methods are still largely limited to utterance-level or unimodal matching, and often fail to capture the global semantic coherence and stylistic consistency of an entire dialogue. To address this gap, we propose S2Dialog, a unified framework for dialogue-level semantic-style retrieval from multimodal dialogue banks. Specifically, S2Dialog consists of a Dialogue-level Textual Retriever and a Dialogue-level Acoustic Retriever, which encode the textual and acoustic modalities of a dialogue into dialogue-level representations, respectively. To further enhance multimodal retrieval, we introduce Dialogue-level Textual-Acoustic Contrastive Learning, which aligns semantically and stylistically similar dialogues while distinguishing unrelated ones. Extensive experiments on the multimodal dialogue dataset DailyTalk demonstrate that S2Dialog achieves outstanding retrieval performance.

</details>

---

### [[20_Research/Papers/大模型/Geometric_Filtering_of_LLM-Generated_Samples_for_Few-Shot_Text_Classification|Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification]]

![[assets/2608.13866_figure.png|800]]

- **arXiv**: [2608.13866](https://arxiv.org/abs/2608.13866)
- **PDF**: https://arxiv.org/pdf/2608.13866
- **详细分析**: [[20_Research/Papers/大模型/Geometric_Filtering_of_LLM-Generated_Samples_for_Few-Shot_Text_Classification|Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification]]
- **作者**: Benjamín Schindler, Gonzalo A. Ruz
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《Geometric Filtering of LLM-Generated Samples for Few-Shot Text Classification》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：XLNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) can generate synthetic training data for text classification, but the quality of generated samples is heterogeneous: some fall in correct class regions of the embedding space while others land in peripheral or cross-class zones. We propose a geometric filtering framework that evaluates each LLM-generated sample by its Euclidean distance to real class examples in a sentence embedding space, selecting only geometrically consistent candidates. A soft weighting mechanism transforms filter scores into sample weights for classifier training. Evaluated across 13 datasets, 5 classifiers, 10 augmentation methods, and over 6,700 configurations, our method achieves +2.61 percentage points (pp) over SMOTE ($p&lt;0.0001$, Cohen's $d=0.95$, 88.9% win rate). The approach generalizes to named entity recognition (+9.26pp, 100% win rate) without filter modification, and is robust across 5 LLMs from 4 providers. A key finding is that the simplest distance-based filter consistently outperforms complex multi-criteria alternatives.

</details>

---

### [[20_Research/Papers/大模型/Bootstrapping_Niche_Multilingual_Code_Translation_via_Reinforcement_Learning_with_Execution-Based_Verifiable_Supervision|Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision]]

![[assets/2608.13854_figure.png|800]]

- **arXiv**: [2608.13854](https://arxiv.org/abs/2608.13854)
- **PDF**: https://arxiv.org/pdf/2608.13854
- **详细分析**: [[20_Research/Papers/大模型/Bootstrapping_Niche_Multilingual_Code_Translation_via_Reinforcement_Learning_with_Execution-Based_Verifiable_Supervision|Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision]]
- **作者**: Kouki Yuki, Jie Zeng, Kyoko Ogawa, Ryunosuke Ikeda, Yohei Kobashi, Takeshi Kojima, Ikuya Yamada, Yusuke Iwasawa, Yutaka Matsuo
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.25（加权：大模型 0.25，强化学习 1）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Bootstrapping Niche Multilingual Code Translation via Reinforcement Learning with Execution-Based Verifiable Supervision》归入 强化学习、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HumanEval, OORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code translation must preserve executable behavior across many programming languages, yet neural code translation has largely focused on a few popular languages such as C++, Java, and Python. This leaves a niche, many-to-many setting where parallel supervision is sparse, producing plausible but non-executable translations. We address this setting with preference-based reinforcement learning driven by execution-based supervision. Our pipeline firstly expands verifiable seed Python programs into a multilingual pool of execution-validated codes. Using the pool, a base LLM generates translation candidates across language pairs, which we label by their execution outcomes. The resulting preferences are used to train a reward model that scores cross-language translation quality. Finally, we optimize our base LLMs with GRPO over 600 directed language pairs (25 x 24) using the reward model as a signal. To evaluate the niche translation capability, we introduce HumanEval-X++, an execution-based benchmark that extends HumanEval-X to a broad many-to-many language space. We evaluate our approach using Qwen-3.5 4B and 9B models. On HumanEval-X++ and existing benchmarks, it yields consistent gains over the untrained baselines. In particular, the 4B model achieves an average improvement of 13% across all languages on HumanEval-X++, with a gain of 21% on mid-tier languages. Our study establishes a reliable approach of data generation, training, and benchmarking, paving the way toward further bootstrapping the quality of many-to-many translation for programming languages.

</details>

---

### [[20_Research/Papers/大模型/When_Lexical_Change_Misleads_Rethinking_Dynamic_Topic_Model_Evaluation_with_Traditional_and_LLM-Based_Metrics|When Lexical Change Misleads: Rethinking Dynamic Topic Model Evaluation with Traditional and LLM-Based Metrics]]

![[assets/2608.13835_figure.png|800]]

- **arXiv**: [2608.13835](https://arxiv.org/abs/2608.13835)
- **PDF**: https://arxiv.org/pdf/2608.13835
- **详细分析**: [[20_Research/Papers/大模型/When_Lexical_Change_Misleads_Rethinking_Dynamic_Topic_Model_Evaluation_with_Traditional_and_LLM-Based_Metrics|When Lexical Change Misleads: Rethinking Dynamic Topic Model Evaluation with Traditional and LLM-Based Metrics]]
- **作者**: Charu Karakkaparambil James
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《When Lexical Change Misleads: Rethinking Dynamic Topic Model Evaluation with Traditional and LLM-Based Metrics》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic topic models capture evolving word distributions, but traditional coherence metrics may fail when vocabulary changes while semantic meaning persists. We evaluate 120 topics from CoNTM and DLDA across NYT, DBLP, and arXiv, using three human annotators and Low, Medium, and High lexical-change categories. Traditional temporal coherence shows highly variable agreement with human judgments ($ρ$=-0.256 to 0.614). In contrast, LLM-based semantic similarity agrees strongly with human semantic judgments for CoNTM on NYT ($ρ$=0.609), DBLP ($ρ$=0.721), and arXiv ($ρ$=0.502), but is less consistent for DLDA. Lexical-change stratification reveals variation hidden by aggregate evaluation. We therefore advocate lexical-change-aware evaluation, jointly reporting traditional coherence and LLM-based semantic measures as complementary rather than interchangeable signals.

</details>

---

### [[20_Research/Papers/大模型/VoiceChat-TTS_A_Low-Latency_Continuous_Speech_Synthesis_Model_for_Interactive_Agents|VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents]]

![[assets/2608.13831_figure.png|800]]

- **arXiv**: [2608.13831](https://arxiv.org/abs/2608.13831)
- **PDF**: https://arxiv.org/pdf/2608.13831
- **详细分析**: [[20_Research/Papers/大模型/VoiceChat-TTS_A_Low-Latency_Continuous_Speech_Synthesis_Model_for_Interactive_Agents|VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents]]
- **作者**: Edresson Casanova, Jaehyeon Kim, Mariana Graterol Fuenmayor, Shehzeen Hussain, Viacheslav Klimkov, Valentin Mendelev, Mikyas Desta, Paarth Neekhara, Piotr Zelasko, Chen Chen, Elena Rastorgueva, Ke Hu...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《VoiceChat-TTS: A Low-Latency Continuous Speech Synthesis Model for Interactive Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spoken dialogue is a natural form of human--computer interaction, yet most speech language models remain limited to turn-based operation and lack real-time adaptability, such as user barge-in. Recent duplex speech-to-speech and speech-to-text models reduce latency by replacing multi-stage pipelines, but often compromise speech quality because accurate ASR, interruption handling, and high-fidelity synthesis must be optimized jointly. We propose VoiceChat-TTS, a low-latency, continuous, and streamable text-to-speech model for interactive agents. VoiceChat-TTS is driven directly by LLM text-token streams, supports explicit interruption via control tokens, and produces silence when no textual input is available. The model enables always-on, responsive speech generation while preserving modularity and high speech quality, and it supports mid-utterance interruptions without resetting the KV cache.

</details>

---

### [[20_Research/Papers/强化学习/GRPO_Beyond_English_A_Large-Scale_Study_of_GRPO_in_Non-English_and_Multilingual_Settings|GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings]]

![[assets/2608.13698_first_page.png|800]]

- **arXiv**: [2608.13698](https://arxiv.org/abs/2608.13698)
- **PDF**: https://arxiv.org/pdf/2608.13698
- **详细分析**: [[20_Research/Papers/强化学习/GRPO_Beyond_English_A_Large-Scale_Study_of_GRPO_in_Non-English_and_Multilingual_Settings|GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings]]
- **作者**: Konstantin Dobler, Federico Scozzafava, Jonathan Janke, Mohamed Ali, Simon Lehnerer
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《GRPO Beyond English: A Large-Scale Study of GRPO in Non-English and Multilingual Settings》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning with Verifiable Rewards (RLVR), often optimized with Group Relative Policy Optimization (GRPO), has become a central recipe for improving the reasoning capabilities of pretrained language models but current studies remain heavily English-centric. We conduct a large-scale empirical study of multilingual and non-English GRPO across a wide range of base models, training languages, and different reasoning language rewards. We find that training to reason in the native language often leaves only a small gap to training for English reasoning. We further observe strong crosslingual transfer: training in one language often improves performance in many others. However, specific trends are highly model- and language-dependent. In some cases, training in a particular language induces severe regressions on out-of-domain capabilities in other languages. Our analysis shows that RLVR beyond English can provide broad crosslingual gains, but also requires broad evaluation to detect language-specific regressions.

</details>

---
