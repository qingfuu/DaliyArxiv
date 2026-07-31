# cs.IR | Information Retrieval | 2026-07-29

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/RecoReward_Recommender-Guided_Multimodal_Description_Generation_for_Recommendation|RecoReward: Recommender-Guided Multimodal Description Generation for Recommendation]]

![[assets/2607.25901_figure.png|800]]

- **arXiv**: [2607.25901](https://arxiv.org/abs/2607.25901)
- **PDF**: https://arxiv.org/pdf/2607.25901
- **详细分析**: [[20_Research/Papers/大模型/RecoReward_Recommender-Guided_Multimodal_Description_Generation_for_Recommendation|RecoReward: Recommender-Guided Multimodal Description Generation for Recommendation]]
- **作者**: Guohong Mu, Yueyang Liu, Jiangxia Cao, Changxin Lao, Zijie Zhuang, Yuhui Zhang, Jiaqi Feng, Ruochen Yang, Shuang Yang, Zhaojie Liu, Qibin Hou
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《RecoReward: Recommender-Guided Multimodal Description Generation for Recommendation》归入 大模型、强化学习 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) can convert multimodal item content into structured descriptions used as semantic features for recommendation. Conventional content-only generation, however, cannot use downstream user signals to determine which semantics should be emphasized. Recent user-conditioned methods incorporate these signals through user histories or profiles, but they require user information at inference and make generation user-dependent. In this paper, we introduce RecoReward, which instead uses behavior-derived rewards during training and preserves content-only inference. To instantiate this idea in live-stream recommendation, we treat historically engaged users as a proxy for future target users and use observational non-target users to estimate affinity shared broadly across users. The Recommender Affinity Score (RAS) contrasts these signals to provide user-selective feedback for reinforcement learning, allowing the learned policy to generate a single shared description without user inputs. In our offline benchmark, RecoReward-9B outperforms its Qwen3.5-9B baseline and all other evaluated models across seven recall metrics. Online A/B testing also shows performance gains. These results show that RecoReward trains the MLLM to produce item features that benefit downstream recommendation while retaining content-only serving.

</details>

---

### [[20_Research/Papers/强化学习/SearchArt_Training_Long-Horizon_Search_Agent_with_Scalable_Synthetic_and_Verified_Task|SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task]]

![[assets/2607.24850_first_page.png|800]]

- **arXiv**: [2607.24850](https://arxiv.org/abs/2607.24850)
- **PDF**: https://arxiv.org/pdf/2607.24850
- **详细分析**: [[20_Research/Papers/强化学习/SearchArt_Training_Long-Horizon_Search_Agent_with_Scalable_Synthetic_and_Verified_Task|SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task]]
- **作者**: Lang Mei, Xiaohan Yu, Chong Chen, Liyan Liu, Xiangnan Chen, Jinchao Ma, Chao Feng, Li Huang, Siyu Mo, Sichen Kang, Yunkun Xu, Zhihan Yang...
- **cs 子类**: cs.IR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.4，强化学习 0.56，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SearchArt: Training Long-Horizon Search Agent with Scalable Synthetic and Verified Task》归入 强化学习、大模型、世界模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large language models (LLMs) have enabled search agents to autonomously tackle complex tasks across extended search and reasoning horizons. However, training effective search agents remains challenging due to the lack of scalable and long-horizon tasks, and the difficulty of evaluating and correcting intermediate reasoning and tool-use behaviors. We introduce SearchArt, a scalable framework for training long-horizon search agents through verification-driven task synthesis and a multi-stage post-training pipeline. SearchArt constructs large-scale datasets for complex search-, research- and user-oriented tasks by synthesizing diverse information-seeking QA pairs and corresponding search trajectories from web documents and automatically generated evidence graphs. To ensure the reliability of the synthesized data, we design a verification pipeline that jointly evaluates QA consistency, trajectory quality, and the relevance of retrieved evidence. The verified trajectories are subsequently used in a multi-stage training process comprising supervised fine-tuning and reinforcement learning-based policy optimization. Search agents trained with SearchArt exhibit adaptive search planning, iterative evidence aggregation, and complex reasoning over extended interaction horizons. Experimental results demonstrate that, with only (Qwen3.5-) 27B parameters, SearchArt scores 74.39 on BrowseComp-ZH, 70.06 on BrowseComp, and 52.55 on Deepresearch-bench, matching or surpassing frontier closed-source agents on both deepsearch and deepresearch benchmarks.

</details>

---

### [[20_Research/Papers/大模型/Retrieval-based_and_Fine-tuned_LLM_Approaches_for_Industrial_Asset_Health_Monitoring_and_Decision_Support|Retrieval-based and Fine-tuned LLM Approaches for Industrial Asset Health Monitoring and Decision Support]]

![[assets/2607.24824_first_page.png|800]]

- **arXiv**: [2607.24824](https://arxiv.org/abs/2607.24824)
- **PDF**: https://arxiv.org/pdf/2607.24824
- **详细分析**: [[20_Research/Papers/大模型/Retrieval-based_and_Fine-tuned_LLM_Approaches_for_Industrial_Asset_Health_Monitoring_and_Decision_Support|Retrieval-based and Fine-tuned LLM Approaches for Industrial Asset Health Monitoring and Decision Support]]
- **作者**: Seshu Kumar Damarla, Xiuli Zhu
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《Retrieval-based and Fine-tuned LLM Approaches for Industrial Asset Health Monitoring and Decision Support》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial plants run many important machines such as pumps, turbines, and compressors. Although engineers can use their experience to identify and diagnose machine problems, transferring this reasoning ability to computer systems remains difficult. This work studies how well a retrieval-only method and an open-source large language model (LLM) perform failure-sensor diagnostic reasoning using the FailureSensorIQ benchmark, a multiple-choice question-answering task introduced by IBM Research. In the retrieval-only approach, each answer option is converted into an option-level query and scored using similar correct and incorrect records from the training data. TF-IDF, BM25, semantic search, and hybrid search are tested and compared. In the LLM-based approach, the Qwen2.5-7B-Instruct model is evaluated using zero-shot prompting, few-shot prompting, and QLoRA fine-tuning. The results show that semantic search and hybrid search perform better than pure keyword-matching techniques, indicating that meaning-based similarity is more important for industrial failure-sensor reasoning. Among the LLM-based methods, the fine-tuned model achieves the best performance and substantially improves over zero-shot and few-shot prompting. Error analysis shows that performance decreases as the number of answer options increases. Robustness analysis also shows that all methods are sensitive to option shuffling, changed labels, paraphrasing, and additional distractors.

</details>

---
