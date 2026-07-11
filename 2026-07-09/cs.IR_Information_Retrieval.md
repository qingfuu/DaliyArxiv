# cs.IR | Information Retrieval | 2026-07-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Seeing_and_Reflecting_Multimodal_Memory-Enhanced_Agent_Collaboration_for_Recommendation|Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation]]

![[assets/2607.07108_figure.png|800]]

- **arXiv**: [2607.07108](https://arxiv.org/abs/2607.07108)
- **PDF**: https://arxiv.org/pdf/2607.07108
- **详细分析**: [[20_Research/Papers/大模型/Seeing_and_Reflecting_Multimodal_Memory-Enhanced_Agent_Collaboration_for_Recommendation|Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation]]
- **作者**: Hao Cong, Huizu Lin, Zihan Wang, Chengkai Huang, Quan Z. Sheng, Lina Yao
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Seeing and Reflecting: Multimodal Memory-Enhanced Agent Collaboration for Recommendation》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based agentic recommender systems show promise in modeling user preferences through natural-language reasoning, yet they remain limited by text-centric inputs and coarse-grained memory updates, making agents prone to missing visual evidence, semantic noise, and preference drift. To address these limitations, we propose MMEACR, a Multimodal Memory-Enhanced Agent Collaboration framework for recommendation. MMEACR introduces a dual-track memory architecture that separates interpretable agent reasoning from fine-grained multimodal matching. In the reasoning track, collaborative User and Item Memory Agents maintain persistent multimodal memories and update them through an attribute-guided reinforcement-and-reflection mechanism. In the matching track, a decoupled multi-modal embedding memory is built from raw interaction narratives and item images to preserve detailed cross-modal signals beyond structured memory updates. The two tracks are integrated through weighted Reciprocal Rank Fusion to produce robust and interpretable rankings. Experiments on three real-world domains show that MMEACR achieves strong overall performance against competitive LLM-based and agent-based baselines, with notable gains in visually grounded recommendation scenarios.

</details>

---
