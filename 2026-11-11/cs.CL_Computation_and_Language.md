# cs.CL | Computation and Language | 2026-11-11

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/强化学习/AutoScaffold_AI-Guided_Scaffolding_for_Reinforcement_Learning_of_Language_Models|AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models]]

![[assets/2611.14515_first_page.png|800]]

- **arXiv**: [2611.14515](https://arxiv.org/abs/2611.14515)
- **PDF**: https://arxiv.org/pdf/2611.14515
- **详细分析**: [[20_Research/Papers/强化学习/AutoScaffold_AI-Guided_Scaffolding_for_Reinforcement_Learning_of_Language_Models|AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models]]
- **作者**: Zijian Zhang, Rizhen Hu, Jiangweizhi Peng, Shiyang Li, Sujay Bhatt, Sihan Zeng, Mingyi Hong
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《AutoScaffold: AI-Guided Scaffolding for Reinforcement Learning of Language Models》归入 强化学习、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, KernelBench, PostTrainBench, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards (RLVR) produces rich training experience, yet outcome rewards reduce each attempt to a single number and leave most of this information unused. Training-time scaffolds, such as strategies or hints added to the prompt during training, offer a natural way to turn this information into guidance, but their design and adaptation are largely left to humans and tailored to specific domains. We introduce AutoScaffold, a unified AI-for-AI framework that turns a student's training experience into adaptive scaffolds, with minimal domain-specific information and no human intervention during training. A frozen teacher periodically examines this experience, diagnoses bottlenecks, and designs scaffolds in two forms: (i) strategies shared across a class of tasks and (ii) hints for individual hard tasks, adjusting the content and amount of support as the student learns. The scaffolds are removed at evaluation. We apply the same framework to ALFWorld, search-based QA, mathematical reasoning, and GPU kernel generation. When evaluated without scaffolds, students trained with AutoScaffold outperform those trained with the corresponding RL baselines in all four domains, with gains of 7.2 points in ALFWorld success and 4.0 points in average QA exact match. On GPU kernel generation, AutoScaffold increases the fraction of tasks with a correct kernel that runs faster than the PyTorch reference by up to 5.0 points. On math, our student surpasses QuestA's reported accuracy using approximately one-third as many student training steps. Analyses show that the teacher identifies a different failure in each task class and shifts its scaffolds from step-by-step workflows to targeted fixes as the student improves, and that its revised scaffolds help the student learn more than keeping the previous scaffold or using no scaffold.

</details>

---

### [[20_Research/Papers/大模型/BioMem_Agentic_Memory_for_Biomedical_LLM_Agents|BioMem: Agentic Memory for Biomedical LLM Agents]]

![[assets/2611.13426_figure.png|800]]

- **arXiv**: [2611.13426](https://arxiv.org/abs/2611.13426)
- **PDF**: https://arxiv.org/pdf/2611.13426
- **详细分析**: [[20_Research/Papers/大模型/BioMem_Agentic_Memory_for_Biomedical_LLM_Agents|BioMem: Agentic Memory for Biomedical LLM Agents]]
- **作者**: Mingchen Li, Yongkang Xiao, Rumeng Li, Rui Zhang, Hong Yu
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《BioMem: Agentic Memory for Biomedical LLM Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have demonstrated considerable potential in biomedical applications, while agentic memory systems have emerged as a promising approach to preserving and utilizing information across tasks and interactions. However, a fundamental question remains: how effectively and reliably do these systems retain, retrieve, update, and utilize biomedical information? In this study, we systematically investigate agentic memory in the biomedical domain, focusing on task effectiveness, retrieval quality, information fidelity, and long-term robustness. We evaluate five memory approaches across four LLMs in three representative settings: biomedical knowledge reasoning, clinical prediction, and long-term conversational memory. Our analyses reveal how memory construction, evidence relevance, and conversational history shape downstream biomedical performance, highlighting the distinct challenges of retrieving relevant information, preserving its fidelity, and effectively utilizing it for reasoning. Building on these findings, we introduce Hybrid Memory Retrieval and Utilization (HMRU), a training-free framework that jointly enhances evidence accessibility and task-aware utilization to improve biomedical reasoning and long-term conversational memory. HMRU achieves an average relative improvement of 8.6% across biomedical question-answering and conversational memory benchmarks, with additional gains in selected clinical prediction tasks. It further reduces conversational answer errors by 24.9% and closes 48.0% of the performance gap to full-context inference. Our findings provide a systematic characterization of biomedical agentic memory and practical insights into developing more effective and reliable memory-augmented LLM systems.

</details>

---

### [[20_Research/Papers/大模型/Using_LLM_Agents_to_Evaluate_Prosocial_Interventions_on_Social_Media_Platforms|Using LLM Agents to Evaluate Prosocial Interventions on Social Media Platforms]]

![[assets/2611.12922_figure.png|800]]

- **arXiv**: [2611.12922](https://arxiv.org/abs/2611.12922)
- **PDF**: https://arxiv.org/pdf/2611.12922
- **详细分析**: [[20_Research/Papers/大模型/Using_LLM_Agents_to_Evaluate_Prosocial_Interventions_on_Social_Media_Platforms|Using LLM Agents to Evaluate Prosocial Interventions on Social Media Platforms]]
- **作者**: Lucen Li, Erin Wertz, Muhammad Haroon, Anshuman Chhabra, Magdalena Wojcieszak
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Using LLM Agents to Evaluate Prosocial Interventions on Social Media Platforms》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social media platforms are a primary source of information for many users. Although research explores various interventions to promote prosocial content or demote harmful content on platforms, there are few systematic methods for evaluating competing intervention designs before conducting costly human-subject experiments. We develop a simulation-based evaluation pipeline built on the OASIS framework. We generate 13,835 LLM-based agents, each with a unique profile. Over 20 time steps, we expose them to real-world Twitter/X posts and let them comment, like, repost, or follow. We use those agents to systematically evaluate three interventions that increase exposure to verified news: adding content, upranking content, and celebrity source cues. All interventions significantly increase news engagement, with upranking news to prominent feed positions producing the largest effects. These effects hold across agents' gender, age, and education levels. We validate our injection treatment results against a comparable human-subject study and find strong directional alignment and similar dose-normalized efficiency. Our results suggest that LLM-based agent simulations can support early-stage evaluation of platform interventions before human-subject deployment, and upranking may be more effective than news volume or source.

</details>

---
