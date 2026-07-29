# cs.IR | Information Retrieval | 2026-07-27

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/StARS_Socially_Appropriate_Robot_Actions_via_a_Recommender_System-Driven_Approach|StARS: Socially Appropriate Robot Actions via a Recommender System-Driven Approach]]

![[assets/2607.21802_figure.jpeg|800]]

- **arXiv**: [2607.21802](https://arxiv.org/abs/2607.21802)
- **PDF**: https://arxiv.org/pdf/2607.21802
- **详细分析**: [[20_Research/Papers/机器人/StARS_Socially_Appropriate_Robot_Actions_via_a_Recommender_System-Driven_Approach|StARS: Socially Appropriate Robot Actions via a Recommender System-Driven Approach]]
- **作者**: Erencem Ozbey, Fethiye Irmak Dogan, Jin Huang, Hatice Gunes
- **cs 子类**: cs.IR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《StARS: Socially Appropriate Robot Actions via a Recommender System-Driven Approach》归入 机器人、具身智能 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social appropriateness in human-robot interaction (HRI) is not universal: different people can judge the same robot action differently in the same situation. To capture this inter-subject variability, we reformulate socially appropriate action generation as a preference modelling problem inspired by recommender systems, treating annotators as users, contexts/scenes as items, and appropriateness scores over a set of candidate robot actions as targets. We propose StARS, a novel model-agnostic framework that integrates collaborative filtering with learnable scene representations to generate user-specific appropriateness scores over candidate robot actions. StARS is model-agnostic: it can be integrated with various scene encoders and backbones, enabling personalisation without redesigning the underlying model. We evaluate StARS on two socially aware robotics datasets, MannersDB+ and SocNav1, and analyse robustness under sparse preference feedback. Across datasets and backbones, StARS consistently improves performance and agreement with annotators, supporting personalised action selection aligned with user norms. Our code is publicly available at https://github.com/Cambridge-AFAR/StARS.git.

</details>

---
