# cs.CR | Cryptography and Security | 2026-08-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/TrustRAG_Blockchain-Enhanced_RAG_via_Committee-Based_Credibility_Scoring|TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring]]

![[assets/2608.20097_figure.png|800]]

- **arXiv**: [2608.20097](https://arxiv.org/abs/2608.20097)
- **PDF**: https://arxiv.org/pdf/2608.20097
- **详细分析**: [[20_Research/Papers/大模型/TrustRAG_Blockchain-Enhanced_RAG_via_Committee-Based_Credibility_Scoring|TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring]]
- **作者**: Baixiang Liu, Haotian Che, Yuan Li
- **cs 子类**: cs.CR, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Systems

#### 研究背景与动机

《TrustRAG: Blockchain-Enhanced RAG via Committee-Based Credibility Scoring》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) lets Large Language Models (LLMs) pull in up-to-date, domain-specific information instead of relying only on what they were trained on. Yet most RAG systems still draw from centralized databases with limited oversight, making it difficult to verify where a document came from, whether it has been tampered with, or whether it should be trusted at all. This is a serious problem in domains where both the timeliness and accuracy of retrieved content are critical, such as healthcare, finance, logistics, and legal case law, where a wrong or manipulated document can directly lead to bad decisions. We present TrustRAG, a committee-based, blockchain-backed RAG system: before a document is used, it is certified by a committee of domain experts through a zero-knowledge protocol, and the committee's hidden scores are combined via secure multi-party computation into a trust score that any client can verify. These scores, along with the underlying document data, are maintained jointly across chains through hash commitments, so no document or score can be silently altered or dropped, and every ranking can be independently replayed and checked.

</details>

---
