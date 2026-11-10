# cs.CL | Computation and Language | 2026-11-09

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/大模型/Compaction,_decay_and_reinforcement_in_a_two-tier_conversational_memory_a_paired_evaluation_against_retrieval-augmented_generation|Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation]]

![[assets/2611.09807_first_page.png|800]]

- **arXiv**: [2611.09807](https://arxiv.org/abs/2611.09807)
- **PDF**: https://arxiv.org/pdf/2611.09807
- **详细分析**: [[20_Research/Papers/大模型/Compaction,_decay_and_reinforcement_in_a_two-tier_conversational_memory_a_paired_evaluation_against_retrieval-augmented_generation|Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation]]
- **作者**: Osamudiamen Edogun, Joshua Obigwe, Irfan Mehmood
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《Compaction, decay and reinforcement in a two-tier conversational memory: a paired evaluation against retrieval-augmented generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A conversational agent that remembers has to decide what to keep. Retrieval-augmented generation keeps the transcript and searches it; the alternative is to compact each turn into atomic facts and search those. We compare the two on LoCoMo, with both arms answering all 1,985 questions in one window, against the same stores, with the same generator and judge, and both predictions on one row, which licenses McNemar's exact test on the 512 questions where they disagree. On the four categories comparable work reports, compaction scores 71.4 per cent against 64.6, a lead of 6.8 points (p = 5.5e-08) at 34 per cent fewer prompt tokens. On all five, including the adversarial set comparable work drops, the lead falls to 2.0 and stops being significant, because the baseline leads adversarial by 14.6. That loss has a structure. Our lead falls as the reference answer demands more source wording, 9.6 points ahead at one or two reference words and 3.1 behind past eight, with token overlap moving the same way, so the judge is not the cause. Compaction keeps what a fact asserts and discards how it was said, so it wins where the answer is a value and loses where it is a phrasing. We also report four negative results with their power calculations.

</details>

---

### [[20_Research/Papers/强化学习/MARS_Training_Multilingual_Search_Agents_for_Retriever-Free_Evidence_Acquisition|MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition]]

![[assets/2611.09090_figure.png|800]]

- **arXiv**: [2611.09090](https://arxiv.org/abs/2611.09090)
- **PDF**: https://arxiv.org/pdf/2611.09090
- **详细分析**: [[20_Research/Papers/强化学习/MARS_Training_Multilingual_Search_Agents_for_Retriever-Free_Evidence_Acquisition|MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition]]
- **作者**: Rui Qi, Yunlong Liang, Yufeng Chen, Jinan Xu, Fandong Meng, Kaiyu Huang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MARS: Training Multilingual Search Agents for Retriever-Free Evidence Acquisition》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LcRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing multilingual retrieval-augmented generation relies heavily on learned retrievers and similarity-based ranking from multilingual collections, which are vulnerable to cross-lingual retrieval errors and indexing overhead. In this paper, we explore retriever-free multilingual search, where the model directly interacts with raw corpora through executable shell commands. This paradigm shifts the bottleneck to multilingual search action generation, where exact search is sensitive to entity surface forms and outcome-only supervision provides limited guidance for multi-turn search. To address these challenges, we propose MARS, a multilingual search agent in direct corpus interaction (DCI) with reinforcement learning (RL). MARS introduces corpus-native entity grounding to recover reliable lexical anchors from corpus evidence, mitigating failure to retrieve evidence. Meanwhile, we present a redundancy-aware search reward to encourage concise and effective search trajectories, addressing training collapse in RL of multilingual scenarios. Experiments show that \ours~consistently outperforms strong retrieval-based and DCI baselines, while demonstrating robust cross-lingual generalization and substantially reducing redundant corpus interactions.

</details>

---

### [[20_Research/Papers/大模型/Using_an_LLM_to_Tackle_Difficult_Cases_in_NER_for_Nepali_Tweets|Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets]]

![[assets/2611.08967_figure.png|800]]

- **arXiv**: [2611.08967](https://arxiv.org/abs/2611.08967)
- **PDF**: https://arxiv.org/pdf/2611.08967
- **详细分析**: [[20_Research/Papers/大模型/Using_an_LLM_to_Tackle_Difficult_Cases_in_NER_for_Nepali_Tweets|Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets]]
- **作者**: Claire Wang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《Using an LLM to Tackle Difficult Cases in NER for Nepali Tweets》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Named entity recognition (NER) is challenging for social media data in a low-resource language. LLMs often lag behind pretrained language models (PLMs) in NER performance, but they show promise in handling cases that PLMs struggle with. Using a dataset of Nepali tweets, we split the test set into "easy" and "hard" cases using token probabilities from a fine-tuned pretrained language model (PLM). We then evaluate an LLM on the hard test cases using 16 different prompt configurations. We find that selecting examples based on semantic similarity and increasing the number of examples improves F1 score by almost 10 points from the baseline configuration. Although the LLM underperforms the PLM on the full and easy test sets, it surpasses the PLM on the hard test set, resulting in an improved score when the two models are combined.

</details>

---

### [[20_Research/Papers/大模型/From_Procedures_to_Permissions_Learning_Precise_Subagent_Authorization_from_Agent_Skills|From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills]]

![[assets/2611.08905_figure.png|800]]

- **arXiv**: [2611.08905](https://arxiv.org/abs/2611.08905)
- **PDF**: https://arxiv.org/pdf/2611.08905
- **详细分析**: [[20_Research/Papers/大模型/From_Procedures_to_Permissions_Learning_Precise_Subagent_Authorization_from_Agent_Skills|From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills]]
- **作者**: Wenkai Yu, Ning Ding, Wentao Zhang, Yehui Tang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《From Procedures to Permissions: Learning Precise Subagent Authorization from Agent Skills》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AuthBench, SkillsBench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As language agents tackle increasingly complex tasks, they increasingly rely on multiple agents to coordinate specialized work, requiring decisions not only about what each subagent should do but also which tools and workspace resources it should access. Existing agent systems provide mechanisms for controlling tools and execution environments, but do not directly specify the resources required by each delegated subtask. Moreover, task outcomes and execution trajectories alone provide limited supervision for determining whether a subagent has received appropriate permissions. We observe that Agent Skills encode procedural knowledge describing the operations, tools, and files required at each step, providing a natural source of supervision for authorization. Building on this observation, we synthesize tasks and step-by-step procedures from Skills, execute them through subagent delegation in interactive environments, and use verified trajectories to construct training data for task execution and authorization. On ClawArena-Team, our method improves tool permission precision by 13.4 percentage points and workspace permission precision by 24.1 percentage points, while increasing overall task success by 11.6 percentage points for Qwen3.5-35B-A3B. On Terminal-Bench 2.1 and SkillsBench, our method remains competitive with existing agent data synthesis approaches. These results show that the procedural knowledge embedded in Agent Skills provides a source of supervision for precise subagent orchestration that task outcomes alone cannot provide.

</details>

---

### [[20_Research/Papers/强化学习/RL-ATTACK_A_Generalized_Black-Box_Adversarial_Attack_on_Language_Models_via_Reinforcement_Learning|RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning]]

![[assets/2611.08711_figure.png|800]]

- **arXiv**: [2611.08711](https://arxiv.org/abs/2611.08711)
- **PDF**: https://arxiv.org/pdf/2611.08711
- **详细分析**: [[20_Research/Papers/强化学习/RL-ATTACK_A_Generalized_Black-Box_Adversarial_Attack_on_Language_Models_via_Reinforcement_Learning|RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning]]
- **作者**: Taikun Chen, Yue Zhang, Wei Qian, Hui Fang
- **cs 子类**: cs.CL, cs.CR
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Security

#### 研究背景与动机

《RL-ATTACK: A Generalized Black-Box Adversarial Attack on Language Models via Reinforcement Learning》归入 强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) exhibit vulnerabilities to adversarial perturbations that can induce unintended responses. These vulnerabilities can be identified via intentional attacks and subsequently used to improve model safety. In black-box settings where gradients are inaccessible, existing methods tend to guess adversarial transformations using external knowledge, ignoring the information provided by the target model. To mitigate this, we propose a trainable black-box framework based on reinforcement learning, which learns from the target model to generate tailored adversarial transformations. We demonstrate that our approach achieves lower post-attack accuracy, greater query efficiency and better semantic preservation on both natural language inference and generative Q&amp;A tasks. On natural language inference, it drives post-attack accuracy to 2% within 20 queries. Against generative language models, our trained attacker consistently achieves lower post-attack accuracy than the untrained attacker and wins in 4 out of 6 settings when compared to a strong optimization-based baseline. We further experiment with multiple reward designs and training settings, and we find that no design or setting is consistently dominant. Our code is available at https://github.com/taikunudel/RL-ATTACK.

</details>

---

### [[20_Research/Papers/大模型/Turkish_Multimodal_Video_Fact-Checking_A_New_Dataset_and_a_Comparison_of_Zero-Shot_Agentic_and_Fine-Tuned_Systems|Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of Zero-Shot Agentic and Fine-Tuned Systems]]

![[assets/2611.08651_first_page.png|800]]

- **arXiv**: [2611.08651](https://arxiv.org/abs/2611.08651)
- **PDF**: https://arxiv.org/pdf/2611.08651
- **详细分析**: [[20_Research/Papers/大模型/Turkish_Multimodal_Video_Fact-Checking_A_New_Dataset_and_a_Comparison_of_Zero-Shot_Agentic_and_Fine-Tuned_Systems|Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of Zero-Shot Agentic and Fine-Tuned Systems]]
- **作者**: Azra Açıl
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Turkish Multimodal Video Fact-Checking: A New Dataset and a Comparison of Zero-Shot Agentic and Fine-Tuned Systems》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video-based misinformation spreads rapidly on social media, but almost all existing fact-checking systems focus exclusively on English text. Tools for low-resource languages such as Turkish are severely limited. In this work, we present TeViD (Turkish Video Fact-checking Dataset), to the best of our knowledge the first multimodal video fact-checking dataset for Turkish. We compiled the dataset from articles published by Teyit.org, an IFCN-certified organisation, and enriched it with translated Snopes articles and synthetic examples to reduce class imbalance. Building on TeViD, we develop two verification pipelines that share the same open-source base model. First, in 3MFact-TR (Pipeline 1), we adapt the multi-role 3MFact framework to Turkish with the Qwen2.5-7B large language model and the Qwen2-VL-7B vision-language model, and add three modules of our own: a semantic inconsistency checker, a 5W1H question manager, and a bilingual evidence retriever that excludes fact-checking sites to prevent leakage. Second, as our Fine-Tuned Model (Pipeline 2), we fine-tune a single Qwen2.5-7B with Low-Rank Adaptation (LoRA) to produce closed-book verdicts from the claim and the video's textual description. We report accuracy, macro F1, True class F1, and True class recall for both systems, together with ablation studies.

</details>

---
