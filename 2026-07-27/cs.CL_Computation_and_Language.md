# cs.CL | Computation and Language | 2026-07-27

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/大模型/Skill_Self-Play_Pushing_the_Frontier_of_LLM_Capability_with_Co-Evolving_Skills|Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills]]

![[assets/2607.22529_first_page.png|800]]

- **arXiv**: [2607.22529](https://arxiv.org/abs/2607.22529)
- **PDF**: https://arxiv.org/pdf/2607.22529
- **详细分析**: [[20_Research/Papers/大模型/Skill_Self-Play_Pushing_the_Frontier_of_LLM_Capability_with_Co-Evolving_Skills|Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills]]
- **作者**: Siyuan Huang, Pengyu Cheng, Haotian Liu, Tao Chen, Yihao Liu, Jingwei Ni, Shijie Zhou, Ziyi Yang, Gangwei Jiang, Mengyu Zhou, Yu Cheng, Xiaoxi Jiang...
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Skill Self-Play: Pushing the Frontier of LLM Capability with Co-Evolving Skills》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM training is shifting from manual design and annotation to interaction-driven self-evolution. However, existing self-evolutionary methods face a fundamental dilemma between task diversity and verification reliability: environment-bound methods obtain precise feedback but confine learning to narrow domains, while open-ended self-generation broadens the task space but lacks reliable verification, allowing misleading rewards to pollute the training loop. We identify agent skills as a powerful middle ground to reconcile this tension: each skill ensures deep, verifiable execution in a specific scenario, while dynamic routing across skills maintains open-ended task variety. Leveraging this insight, we introduce Skill Self-Play (Skill-SP), a co-evolutionary framework comprising a proposer, a solver, and a dynamic skill controller. Orchestrated via a reinforcement learning loop, these components co-evolve in a continuous self-play loop: the proposer generates challenging tasks conditioned on dynamically sampled skills; the solver explores candidate solutions to push its capability boundaries; and the skill controller collects execution feedback to update and expand the skill library. This interactive co-evolution effectively bridges the gap between structured verification and open-ended exploration. Empirical evaluations on tool-use and reasoning benchmarks demonstrate that Skill-SP, serving as a robust evolution engine, consistently pushes the performance ceiling of competent backbones while catalyzing striking turnarounds for initially misaligned models. Our code is available at https://github.com/Qwen-Applications/skill-self-play.

</details>

---

### [[20_Research/Papers/大模型/Scaling_Native_Multimodal_Pre-Training_From_Scratch|Scaling Native Multimodal Pre-Training From Scratch]]

![[assets/2607.22043_figure.png|800]]

- **arXiv**: [2607.22043](https://arxiv.org/abs/2607.22043)
- **PDF**: https://arxiv.org/pdf/2607.22043
- **详细分析**: [[20_Research/Papers/大模型/Scaling_Native_Multimodal_Pre-Training_From_Scratch|Scaling Native Multimodal Pre-Training From Scratch]]
- **作者**: Haoyuan Wu, Aoqi Wu, Hai Wang, Jiajia Wu, Jinxiang Ou, Bei Yu
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Scaling Native Multimodal Pre-Training From Scratch》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although large language models (LLMs) exhibit remarkable reasoning capabilities, their reliance on text-only pre-training restricts the perception of the multimodal physical world. Native multimodal pre-training avoids this limitation by training models from scratch on multimodal inputs, thereby achieving deep cross-modal integration and mitigating optimization asymmetries inherent to traditional late-fusion architectures. Despite these advantages, the scaling properties of this paradigm remain systematically uncharacterized. To address this gap, we investigate the optimal model size and token count for training a transformer-based vision-language model under a fixed computational budget. We demonstrate that minimal objective loss adheres to a predictable compute law, whereas compute-optimal model sizes and token counts scale as power laws. Notably, language and multimodal objectives manifest distinct scaling behaviors. The language allocation law is largely invariant to the composition of the data, indicating stable language learning regardless of the multimodal data ratio. Conversely, the multimodal allocation law is highly sensitive to this composition. Specifically, text-heavy mixtures become compute-efficient only at larger model scales, shifting the optimal resource allocation toward greater model capacity. Additionally, by modeling the influence of data composition on compute laws and allocation exponents, we derive an efficiency frontier specifying precise configurations of model size, token count, and data mixture. Downstream evaluations further reveal that native multimodal pre-training induces positive cross-modal transfer, thereby enhancing pure-text spatial reasoning and enabling robust multimodal in-context learning. In summary, this empirical research establishes the essential groundwork for predictably scaling multimodal foundation models.

</details>

---

### [[20_Research/Papers/大模型/Developing_and_Validating_the_Spanish_Version_of_the_Large_Language_Models_Dependency_Scale_(LLM-D12-SP)|Developing and Validating the Spanish Version of the Large Language Models Dependency Scale (LLM-D12-SP)]]

![[assets/2607.22041_first_page.png|800]]

- **arXiv**: [2607.22041](https://arxiv.org/abs/2607.22041)
- **PDF**: https://arxiv.org/pdf/2607.22041
- **详细分析**: [[20_Research/Papers/大模型/Developing_and_Validating_the_Spanish_Version_of_the_Large_Language_Models_Dependency_Scale_(LLM-D12-SP)|Developing and Validating the Spanish Version of the Large Language Models Dependency Scale (LLM-D12-SP)]]
- **作者**: Tran Gia Bao, Mo El-Haj, Sameha Al-Shakhsi, Antonio Garcia-Cabot, Raian Ali, Ala Yankouskaya
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Developing and Validating the Spanish Version of the Large Language Models Dependency Scale (LLM-D12-SP)》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

There is a growing need for reliable and culturally validated instruments to assess psychological dependency on large language models (LLMs), particularly as LLMs are increasingly used for task execution, decision-making, and communication in organizational and work-related settings. This need is especially relevant for Spanish-speaking populations, where LLM adoption is rapidly expanding, yet validated psychometric tools remain scarce. The present study reports the first validation of the Spanish version of the Large Language Model Dependency Scale (LLM-D12-SP), extending prior validations conducted in English- and Arabic-speaking samples. The LLM-D12 is a two-dimensional instrument assessing Instrumental Dependency (reliance on LLMs for performing tasks and supporting decisions) and Relationship Dependency (psychological reliance on LLMs for companionship and social interaction). A total of 386 Spanish-speaking participants (M = 28.0 years, SD = 6.1; 55% male) completed the LLM-D12-SP. Confirmatory factor analysis supported the original two-factor structure. The scale demonstrated good internal consistency (Cronbach's alpha = 0.89 total; 0.86 Instrumental; 0.85 Relationship). Discriminant validity analyses indicated that the two subscales represent related but distinct constructs. External validation showed that both dependency dimensions were positively associated with internet addiction and perceived trustworthiness of LLMs, while showing weak or no association with need for cognition. Together with prior English and Arabic validations, these findings establish cross-linguistic support for the scale's structure and provide a psychometrically sound tool for investigating psychological aspects of LLM use in organizational contexts.

</details>

---

### [[20_Research/Papers/强化学习/Enough_is_as_good_as_a_feast_A_Comprehensive_Analysis_of_How_Reinforcement_Learning_Mitigates_Task_Conflicts_in_LLMs|Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs]]

![[assets/2607.22039_figure.png|800]]

- **arXiv**: [2607.22039](https://arxiv.org/abs/2607.22039)
- **PDF**: https://arxiv.org/pdf/2607.22039
- **详细分析**: [[20_Research/Papers/强化学习/Enough_is_as_good_as_a_feast_A_Comprehensive_Analysis_of_How_Reinforcement_Learning_Mitigates_Task_Conflicts_in_LLMs|Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs]]
- **作者**: Zixuan Ren, Jinliang Lu, Junhong Wu, Yang Zhao, Dai Dai, Hua Wu, Haifeng Wang, Chengqing Zong
- **cs 子类**: cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement Learning Mitigates Task Conflicts in LLMs》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval, IFEval, LiveBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Model merging plays a crucial role in consolidating multiple specialized models into a single, unified model, especially in the era of large language models (LLMs). Recent research has primarily focused on developing strategies to enhance merging performance with the trained models, while the impact of training paradigms, such as supervised fine-tuning (SFT) and reinforcement learning (RL), on the effectiveness of model merging remains underexplored. In this study, we systematically explore the merging behavior of RL-trained LLMs compared to those trained with traditional SFT. Through comprehensive evaluations across five representative tasks, we find that RL significantly reduces task conflicts and results in less performance degradation after merging, making RL-trained models particularly well-suited for this process. To unearth the reasons behind the superior suitability of RL for model merging, we conduct extensive empirical experiments and theoretical analyses. Our findings highlight three key factors: (1) On-policy training data in RL control the gradient updates in a smaller magnitude, reducing the risk of overwriting existing knowledge for other tasks in the model. (2) The RL optimization objective, which favors ``\textit{enough is as good as a feast}", progressively reduces the magnitude and the number of conflict parameter updates as the model converges. (3) Joint optimization of positive and negative examples in RL steers the model towards an unbiased task-specific parameter subspace, ensuring robust performance while further preventing parameter conflicts.

</details>

---

### [[20_Research/Papers/大模型/DWT-Fusion_A_Signal-Based_Framework_for_Training-Free_LLM-Generated_Text_Detection|DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text Detection]]

![[assets/2607.22026_figure.png|800]]

- **arXiv**: [2607.22026](https://arxiv.org/abs/2607.22026)
- **PDF**: https://arxiv.org/pdf/2607.22026
- **详细分析**: [[20_Research/Papers/大模型/DWT-Fusion_A_Signal-Based_Framework_for_Training-Free_LLM-Generated_Text_Detection|DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text Detection]]
- **作者**: Mehmet Batuhan Özdaş, Murat Osmanoğlu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《DWT-Fusion: A Signal-Based Framework for Training-Free LLM-Generated Text Detection》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Detecting LLM-generated text remains challenging under zero-shot and training-free conditions, especially when detectors must generalize across datasets, domains, and unseen generators. While existing training-free approaches exploit language-model statistics as detection signals, they typically characterize a text through global measures that summarize overall model behavior. Consequently, potentially informative local and multiscale variations in token-level predictability may remain underutilized. Motivated by this observation, we introduce DWT-Fusion, a training-free signal-based framework for detecting LLM-generated text using discrete wavelet analysis of token-level log-probability sequences produced by a proxy causal language model. The proposed framework analyzes these sequences through wavelet-based multiresolution signal representations and derives detection signals from localized probability dynamics. We further evaluate four training-free voting variants, including equal-weight hard voting, equal-weight soft voting, calibration-weighted hard voting, and calibration-weighted soft voting, to combine multiple wavelet configurations without training a supervised meta-classifier. We evaluate the framework on HC3, M4, and MAGE using GPT-Neo-2.7B, GPT-J-6B, Falcon-7B, and LLaMA-3-8B as proxy models. The best single wavelet configurations achieve AUROC values of 0.9872, 0.8185, and 0.7138 on HC3, M4, and MAGE, respectively. With calibration-weighted voting, the best ensemble variants further improve AUROC to 0.9919, 0.8477, and 0.7471. These findings show that DWT-based multiresolution scoring and calibration-guided voting fusion provide effective and interpretable signals for training-free LLM-generated text detection.

</details>

---

### [[20_Research/Papers/大模型/Ground_Truth_First_A_Longitudinal_Evaluation_Instrument_for_Agent_Memory,_and_the_Tenure_Crossover_in_Memory-Architecture_Rankings|Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings]]

![[assets/2607.21962_figure.png|800]]

- **arXiv**: [2607.21962](https://arxiv.org/abs/2607.21962)
- **PDF**: https://arxiv.org/pdf/2607.21962
- **详细分析**: [[20_Research/Papers/大模型/Ground_Truth_First_A_Longitudinal_Evaluation_Instrument_for_Agent_Memory,_and_the_Tenure_Crossover_in_Memory-Architecture_Rankings|Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings]]
- **作者**: Quentin Spencer
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Ground Truth First: A Longitudinal Evaluation Instrument for Agent Memory, and the Tenure Crossover in Memory-Architecture Rankings》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, Mem2ActBench, MemGym, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Benchmarks for LLM-agent memory typically generate conversations first and extract answer keys afterwards -- with documented label-error and contamination problems -- and they overwhelmingly measure short interaction histories. We invert the pipeline: a seeded life-script sampler emits facts with validity intervals, volatility classes, and source channels before any text exists; an LLM renderer writes chat and email from per-event fact manifests; a fidelity verifier confirms every planted fact; and questions are instantiated mechanically from the script, so gold answers are script-valid by construction and separately validated for answerability. The synthetic, fictionalized corpus (~380 questions, 15 types) embeds features absent from the benchmarks we survey: per-fact validity intervals, sent/received trust distinctions, injection probes in a benign harness, and as-of-date question sets. Benchmarking five memory architectures against a no-memory control (fixed answerer, versioned LLM judge, three replicates, two horizons), we find backend rankings invert with history length: the budgeted curated-map memory that leads at three weeks loses recall of evicted content by nine weeks (96% to 72%) while a provenance-typed graph rises to 90%; the inversion is positive for all six users under complete cross-family re-judging (exact p=0.031). A full-rendered-history baseline ties or exceeds the best memory system at the short horizon but shows no judge-independent advantage at nine weeks, at about twice the read cost. Write-stage quality strongly correlates with downstream quality (weakly-written facts fail 24% vs 2%), and injection resistance tracked whether provenance boundaries survive representation. A layered architecture performs best among the memory systems in both regimes (96.8% short-horizon) and is released as Veracium, an open-source library, with the corpus generator and harness.

</details>

---

### [[20_Research/Papers/大模型/Leveraging_External_Knowledge_for_Historical_Document_Restoration_via_Retrieval-Augmented_Large_Language_Models|Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models]]

![[assets/2607.21936_figure.png|800]]

- **arXiv**: [2607.21936](https://arxiv.org/abs/2607.21936)
- **PDF**: https://arxiv.org/pdf/2607.21936
- **详细分析**: [[20_Research/Papers/大模型/Leveraging_External_Knowledge_for_Historical_Document_Restoration_via_Retrieval-Augmented_Large_Language_Models|Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models]]
- **作者**: Gabeen Kim, Kyeongpil Kang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.CL

#### 研究背景与动机

《Leveraging External Knowledge for Historical Document Restoration via Retrieval-Augmented Large Language Models》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Historical documents act as invaluable knowledge archives but often suffer from illegibility due to physical deterioration and damage. While existing restoration methods based on masked language modeling effectively utilize local context, they struggle to restore named entities that require external historical knowledge. To address this limitation, we introduce a novel framework for historical document restoration that leverages large language models with retrieval-augmented generation (RAG). By combining the implicit knowledge of pre-trained LLMs with explicitly retrieved external context, our model ARI effectively mitigates the challenge of inferring context-dependent proper nouns. Extensive experiments on Korean historical documents demonstrate that our approach significantly outperforms baselines, achieving substantial gains in restoring both general characters and named entities. Furthermore, comprehensive evaluations including expert assessments confirm that ARI serves as a practical tool for domain experts, promising to accelerate the analysis of historical records.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Reducing_Foreign_Language_Anxiety_Using_Level-Appropriate_Embodied_Conversational_Agents|Towards Reducing Foreign Language Anxiety Using Level-Appropriate Embodied Conversational Agents]]

![[assets/2607.21887_first_page.png|800]]

- **arXiv**: [2607.21887](https://arxiv.org/abs/2607.21887)
- **PDF**: https://arxiv.org/pdf/2607.21887
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Reducing_Foreign_Language_Anxiety_Using_Level-Appropriate_Embodied_Conversational_Agents|Towards Reducing Foreign Language Anxiety Using Level-Appropriate Embodied Conversational Agents]]
- **作者**: Krishan Rajaratnam, Wenbin Gan, Yuan Sun
- **cs 子类**: cs.CL, cs.HC
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.95（加权：具身智能 1.2，大模型 0.75）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Towards Reducing Foreign Language Anxiety Using Level-Appropriate Embodied Conversational Agents》归入 具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computation and Language 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foreign language anxiety (FLA) can be a major barrier to second language acquisition (SLA), especially in conversational contexts. With the proliferation of large language models (LLMs) throughout all areas of life, recent work suggests that interacting with LLM agents can be instrumental within the field of SLA and foreign language education, especially for reducing FLA. Related work also suggests that linguistic demands and task complexity can be predictors of FLA, implying that the use of demanding, complex language could lead to learners experiencing higher FLA. In this paper, we propose a novel multi-agent embodied conversational system that generates level-appropriate dialogue for English language learners. These levels are based on those defined by the Common European Framework of Reference for Languages (CEFR) to describe non-native listener and speaker proficiency. Using a "generate-evaluate-regenerate" loop with multiple LLM agents and a level classifier, it achieves a desired simplicity that is adaptive to the user's proficiency level. We also share the results of a preliminary small-sample pilot study that tested this system with Japanese university students, to see whether it would yield lower FLA levels than an unsimplified embodied conversational agent. Analysis of conversational output showed that 87.4% of dialogue sentences generated by the proposed multi-agent system fell within one predicted CEFR level of the learner's self-assessed proficiency, compared to 54.1% for the unsimplified agent. This suggests that the novel system is better able to produce output at an appropriate level for the learner. Though this study did not yield statistically significant evidence that the system reduces FLA levels in Japanese learners of English, likely due to a small sample size, it provides usability findings and culturally-informed design insights that will inform future study.

</details>

---

### [[20_Research/Papers/大模型/Agentic_Evaluation_of_Copyright_Law_Compliance|Agentic Evaluation of Copyright Law Compliance]]

![[assets/2607.21799_figure.png|800]]

- **arXiv**: [2607.21799](https://arxiv.org/abs/2607.21799)
- **PDF**: https://arxiv.org/pdf/2607.21799
- **详细分析**: [[20_Research/Papers/大模型/Agentic_Evaluation_of_Copyright_Law_Compliance|Agentic Evaluation of Copyright Law Compliance]]
- **作者**: Zheng Hui, Doni Bloomfield, Noam Kolt
- **cs 子类**: cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Agentic Evaluation of Copyright Law Compliance》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, Copyright-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly perform commercial tasks that involve retrieving external content such as images and, where appropriate, reproducing that content. LLM agents should comply with the law, including copyright law. Presently, however, we lack adequate frameworks to assess whether they do so in practice. To that end, we introduce \textbf{Copyright-Bench}, a benchmark designed to evaluate \textit{LLM agents' compliance with} \emph{copyright law}. Copyright-Bench is comprised of realistic commercial tasks---website development, merchandise design, and pitch deck production---that involve agents selecting between public-domain content (the use of which is \textit{legal}) and copyrighted content (the use of which is \textit{infringing} in this setting).The evaluation introduces prompt variations that simulate different user preferences, as well as time pressure.Comparing state-of-the-art LLM agents against a human baseline, we find that: (1) agents select copyrighted works despite the availability of public-domain alternatives; and (2) for open-weights models, violation rates increase in response to certain user preferences and simulated time pressure.

</details>

---

### [[20_Research/Papers/强化学习/Progress_Reward_Modeling_for_Robotic_Learning_A_Comprehensive_Survey|Progress Reward Modeling for Robotic Learning: A Comprehensive Survey]]

![[assets/2607.21655_figure.png|800]]

- **arXiv**: [2607.21655](https://arxiv.org/abs/2607.21655)
- **PDF**: https://arxiv.org/pdf/2607.21655
- **详细分析**: [[20_Research/Papers/强化学习/Progress_Reward_Modeling_for_Robotic_Learning_A_Comprehensive_Survey|Progress Reward Modeling for Robotic Learning: A Comprehensive Survey]]
- **作者**: Jianshu Zhang, Keliang Wu, Haoran Lu, Anbang Liu, Ce Zhang, Weijie Yin, Chengxuan Qian, Xiyuan Yang, Zhenyu Pan, Guo Ye, Han Liu
- **cs 子类**: cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Progress Reward Modeling for Robotic Learning: A Comprehensive Survey》归入 机器人、具身智能 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic learning takes place in dynamic environments with large behavior spaces. A terminal success signal only tells the robot whether the task is completed. It does not explain whether the current behavior is making progress, remaining unchanged, or undoing earlier progress. For this reason, recent studies have increasingly explored progress rewards that provide feedback during task execution. However, the current literature lacks a shared framework. Existing methods use different observations, goal specifications, output signals, supervision sources, and evaluation protocols. This makes it difficult to compare them and understand what their results actually validate. In this survey, we provide a unified view of progress reward modeling for robotic learning. We organize the field in three connected steps. We first study the interface of a progress model. This defines the problem from the outside by asking what information the model receives and what form of progress signal it produces. We then move inside the model and study the methods used to construct this signal. This reveals the different assumptions and mechanisms behind progress estimation and reward generation. Finally, we examine the data and benchmarks that support these methods. This shows how progress supervision is obtained and what different evaluations actually measure. Together, these three perspectives connect what a progress model is, how it is built, and how its quality is validated. We further summarize the main limitations of current approaches and discuss future research directions.

</details>

---

### [[20_Research/Papers/大模型/Molt_A_Scalable_PyTorch-Native_Training_Framework_for_Agentic_Reinforcement_Learning|Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning]]

![[assets/2607.21653_figure.png|800]]

- **arXiv**: [2607.21653](https://arxiv.org/abs/2607.21653)
- **PDF**: https://arxiv.org/pdf/2607.21653
- **详细分析**: [[20_Research/Papers/大模型/Molt_A_Scalable_PyTorch-Native_Training_Framework_for_Agentic_Reinforcement_Learning|Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning]]
- **作者**: Jian Hu, Huiying Li, Hao Zhang, Binfeng Xu, Yifan Zhang, Shaokun Zhang, Hemil Desai, Michael Demoret, Pavlo Molchanov, Jan Kautz, Yi Dong
- **cs 子类**: cs.CL, cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.35，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Molt: A Scalable PyTorch-Native Training Framework for Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning research is constant algorithm modification, new estimators, new pipeline stages, new rollout schemes, and in mainstream frameworks each change threads through layers of trainer, distributed backend, and rollout glue: the cost lands on the researcher at every iteration. Molt is a PyTorch-native training framework built to keep that cost small: a codebase compact and clean enough for a researcher to hold in their head, and for an AI coding assistant to read and reason about in its entirety, so the algorithm flow can be traced and changed end to end. The agent is an ordinary program, and one asynchronous loop trains multimodal and mixture-of-experts policies while never training on a token it did not generate, consistent in tokens, policy versions, and model semantics. Leanness does not cost performance: under a matched, fully asynchronous protocol, Molt is statistically comparable to a state-of-the-art Megatron-based stack. Molt is open source and provides recipes and containers at https://github.com/NVIDIA-NeMo/labs-molt.

</details>

---
