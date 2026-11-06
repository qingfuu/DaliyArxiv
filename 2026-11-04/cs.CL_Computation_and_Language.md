# cs.CL | Computation and Language | 2026-11-04

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/强化学习/MDSKILL_Learning_to_Internalize_Skill_Memory_through_Multi-View_Distillation_for_Efficient_Dynamic_Agent_Self-Evolution|MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution]]

![[assets/2611.05313_figure.png|800]]

- **arXiv**: [2611.05313](https://arxiv.org/abs/2611.05313)
- **PDF**: https://arxiv.org/pdf/2611.05313
- **详细分析**: [[20_Research/Papers/强化学习/MDSKILL_Learning_to_Internalize_Skill_Memory_through_Multi-View_Distillation_for_Efficient_Dynamic_Agent_Self-Evolution|MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution]]
- **作者**: Dian Jin, Jinluan Yang, Kairong Han, Baohong Li, Zijing Hu, Yi He, Wenlin Zhong, Yunze Tong, Minqin Zhu, Linchuan Li, Yanan Niu, Kun Kuang
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MDSKILL: Learning to Internalize Skill Memory through Multi-View Distillation for Efficient Dynamic Agent Self-Evolution》归入 大模型、强化学习 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skill memories encode past experiences as textual prompts to improve reinforcement learning (RL) for self-evolving agents. Complementing RL, On-Policy Self-Distillation (OPSD) provides dense, fine-grained supervision to internalize knowledge from skill-guided trajectories and accelerate policy learning. However, self-generated memories often contain noisy supervision and functionally entangled, redundant, or conflicting knowledge, making direct distillation difficult. Under limited training budgets, these issues can hinder knowledge internalization and even degrade performance. To address this problem, we propose MDSKILL, a multi-view distillation approach for skill memory internalization. MDSKILL organizes skill memories into three complementary functional views (state grounding, action planning, and execution control) and selects high-quality skills using dynamic metrics to construct view-specific and integrated reasoning branches. OPSD then transfers and consolidates complementary experiential knowledge across these branches into a shared policy, enabling efficient skill internalization and continuous agent self-evolution. We evaluate MDSKILL on three agent benchmarks against RL, skill-augmented, and self-distillation baselines that do not rely on stronger external teacher models. Without additional computational overhead, MDSKILL improves upon SOTA performance by up to 7.1% and 8.1% on ALFWorld and WebShop. Extensive ablations and evolution analyses further validate its effectiveness in knowledge internalization and policy improvement. The code is available at https://anonymous.4open.science/r/MDSKILL-CF53.

</details>

---

### [[20_Research/Papers/大模型/What_Does_the_Model_See_Representation_Validity_in_Multimodal_LLM-Based_Video_Analysis|What Does the Model See? Representation Validity in Multimodal LLM-Based Video Analysis]]

![[assets/2611.05181_figure.png|800]]

- **arXiv**: [2611.05181](https://arxiv.org/abs/2611.05181)
- **PDF**: https://arxiv.org/pdf/2611.05181
- **详细分析**: [[20_Research/Papers/大模型/What_Does_the_Model_See_Representation_Validity_in_Multimodal_LLM-Based_Video_Analysis|What Does the Model See? Representation Validity in Multimodal LLM-Based Video Analysis]]
- **作者**: Christian Pipal, Eva-Maria Vogel, Morgan Wack
- **cs 子类**: cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《What Does the Model See? Representation Validity in Multimodal LLM-Based Video Analysis》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) allow social scientists to analyze video at scale, but researchers must decide which parts of a video to provide as input. We use the term representation validity to examine how text, audio, video, and combined inputs affect measurement and subsequent analysis. We compare input representations across six open-weight MLLMs and three human-annotated video datasets. No representation consistently performs best. On seven news-related constructs, native-video performance varies little across models (macro-F1 = .70-.77), while extracted-text performance ranges from .52 to .80. Three models perform better with text and three with video. Combining inputs rarely improves performance. Higher classification accuracy also does not reliably produce estimates closer to those based on human codes. The highest-F1 representation best reproduces human-coded regression coefficients in 17 of 42 comparisons. Even when each model uses its highest-F1 deployable representation, 45% of sample-prevalence estimates differ from the human-coded benchmark by more than ten percentage points. Input representation therefore requires validation for both the construct being measured and the quantity estimated from the resulting labels.

</details>

---

### [[20_Research/Papers/大模型/AdSteer_Native_Advertising_in_Large_Language_Model_Generation|AdSteer: Native Advertising in Large Language Model Generation]]

![[assets/2611.04147_figure.png|800]]

- **arXiv**: [2611.04147](https://arxiv.org/abs/2611.04147)
- **PDF**: https://arxiv.org/pdf/2611.04147
- **详细分析**: [[20_Research/Papers/大模型/AdSteer_Native_Advertising_in_Large_Language_Model_Generation|AdSteer: Native Advertising in Large Language Model Generation]]
- **作者**: Shuhang Lin, Chuhao Zhou, Zhenyu Wang, Xiao Lin, Changsheng Wang, Saibo Geng, Dimitris N. Metaxas
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM

#### 研究背景与动机

《AdSteer: Native Advertising in Large Language Model Generation》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GEM-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) services face rapidly rising serving costs. To sustain free or affordable access for a broad user base, alternative monetization mechanisms are needed. Native advertising offers a promising approach, as it creates economic value by aligning user intent with merchant offerings. Yet how to integrate sponsored content naturally into LLM responses remains largely underexplored. Existing approaches primarily rely on prompt-level injection, multi-pass rewriting, or fine-tuning, which can compromise response quality or introduce additional computational costs. We propose AdSteer, a lightweight decoding-time advertising framework that adaptively adjusts token probabilities to integrate contextually appropriate advertisement into responses. AdSteer calibrates the strength and duration of advertising influence, making sponsored content a natural part of the response. Experiments on GEM-Bench across three application scenarios show that AdSteer achieves an average improvement of 14.1% in overall score over the strongest baselines and 22.5% fewer total tokens on average than rewrite-based methods. These results demonstrate that AdSteer provides an effective and practical solution for native advertising in LLMs.

</details>

---

### [[20_Research/Papers/大模型/Language_Model_Augmented_Decision_Transformer_for_Multi-Task_Offline_Reinforcement_Learning|Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning]]

![[assets/2611.04031_figure.png|800]]

- **arXiv**: [2611.04031](https://arxiv.org/abs/2611.04031)
- **PDF**: https://arxiv.org/pdf/2611.04031
- **详细分析**: [[20_Research/Papers/大模型/Language_Model_Augmented_Decision_Transformer_for_Multi-Task_Offline_Reinforcement_Learning|Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning]]
- **作者**: Xinbo Zhao, Yuhang Liu, Xin Zhang, Lei Le, Zhaohan Xi, Yu Yang, Yingxue Zhang
- **cs 子类**: cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.87（加权：大模型 0.75，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Language Model Augmented Decision Transformer for Multi-Task Offline Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MTRL, Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline multi-task reinforcement learning (MTRL) aims to learn a unified policy from heterogeneous offline datasets that generalizes across tasks. However, existing offline MTRL methods often struggle with two fundamental issues: severe per-task data scarcity and limited cross-task generalization. In this paper, we propose Language-Model Augmented Decision Transformer (LaMA-DT), a unified sequence-modeling framework that leverages a single large language model (LLM) for both trajectory augmentation and multi-task policy learning. LaMA-DT uses natural-language task descriptions to guide task-aligned trajectory augmentation through a set of supervised generation and alignment objectives, and incorporates a scoring-and-filtering mechanism to retain high-quality augmented trajectories. The same LLM is then repurposed as a language-conditioned Decision Transformer and fine-tuned on a mixture of real and augmented data. Experiments on Meta-World and MuJoCo multi-task benchmarks demonstrate that LaMA-DT consistently outperforms competitive baselines, particularly in low-data regimes, showing that language-guided data augmentation substantially improves cross-task generalization.

</details>

---
