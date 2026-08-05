# cs.IR | Information Retrieval | 2026-08-03

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Think2Go_Generative_Next_POI_Recommendation_with_LLM_Reasoning|Think2Go: Generative Next POI Recommendation with LLM Reasoning]]

![[assets/2607.28997_figure.png|800]]

- **arXiv**: [2607.28997](https://arxiv.org/abs/2607.28997)
- **PDF**: https://arxiv.org/pdf/2607.28997
- **详细分析**: [[20_Research/Papers/大模型/Think2Go_Generative_Next_POI_Recommendation_with_LLM_Reasoning|Think2Go: Generative Next POI Recommendation with LLM Reasoning]]
- **作者**: Zhuang Zhuang, Shanshan Feng, Hangwei Qian, Mingqi Yang, Heng Qi, Yanming Shen, Baocai Yin
- **cs 子类**: cs.IR
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.7（加权：大模型 0.3，强化学习 0.4）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Think2Go: Generative Next POI Recommendation with LLM Reasoning》归入 强化学习、大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Next Point-of-Interest (POI) recommendation task focuses on mining user behavioral preference patterns from historical check-ins to provide personalized suggestions for the next destination. Existing methods primarily rely on shallow contextual information and handcrafted feature interactions to predict the next POI. However, the inherent sparsity and complexity of user mobility patterns limit the computational capacity of non-reasoning models to capture deep intent, while large language models (LLMs) perform suboptimally because they lack a deep understanding of semantic IDs (SIDs) when SIDs are trained separately. To address these limitations, we propose Think2Go, a novel generative next POI recommendation framework, which enhances the model's comprehension of SID representations and explores diverse spatial-temporal patterns via test-time computational scaling. We unify supervised fine-tuning (SFT) and reinforcement learning (RL)-based reasoning within a single architecture, enabling joint optimization of memorization and adaptive reasoning to better retain user behavior patterns while exploring diverse user preferences. To further calibrate policy optimization in adaptive reasoning, we propose two advantage weighting mechanisms that integrate (1) prompt epistemic uncertainty, estimated via kernel density methods to assess the spatial-temporal periodic pattern alignment between queries and user history, promoting increased exploration under high epistemic uncertainty; and (2) reward-informed advantage scaling, captured by normalizing rewards against their maxima to adapt update magnitudes, thereby improving training stability and mitigating overfitting to noisy signals. This joint calibration forms an implicit curriculum learning strategy, delivering fine-grained, instance-aware policy updates that prevent entropy collapse and support robust exploration.

</details>

---
