# cs.IR | Information Retrieval | 2026-06-12

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/CQC-RAG_Robust_Retrieval-Augmented_Generation_via_Cross-Query_Consistency|CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency]]

![[assets/2606.13438_figure.png|800]]

- **arXiv**: [2606.13438](https://arxiv.org/abs/2606.13438)
- **PDF**: https://arxiv.org/pdf/2606.13438
- **详细分析**: [[20_Research/Papers/大模型/CQC-RAG_Robust_Retrieval-Augmented_Generation_via_Cross-Query_Consistency|CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency]]
- **作者**: Yanjia Sun, Sifan Liu, Jie Shao
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: cs.IR

#### 研究背景与动机

《CQC-RAG: Robust Retrieval-Augmented Generation via Cross-Query Consistency》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TriviaQA, TrivialQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) has become a common approach for improving the factuality of Large Language Models (LLMs), yet its reliability remains highly sensitive to how external evidence is retrieved and used. Semantically equivalent queries with different syntactic forms may lead to different retrieval results, while irrelevant or misleading documents can further induce hallucinated answers. Existing multi-path reasoning methods improve robustness by sampling multiple candidate answers and applying voting- or confidence-based selection, but they still face two limitations: diversity is often injected through uncontrollable decoding randomness, and answer evaluation is usually confined to a single query-induced evidence view. To address these limitations, we propose a Cross-Query Consistency Hypothesis: correct answers tend to maintain high confidence across semantically equivalent but syntactically diverse queries, whereas noise-induced hallucinations exhibit unstable confidence under such query variations. Based on this hypothesis, we introduce CQC-RAG, a framework that co-designs query-level diversity injection with cross-query consistency evaluation. CQC-RAG rewrites the original question into diverse but meaning-preserving queries, reranks a shared document pool to construct query-conditioned reasoning contexts, applies an evidence-grounded protocol to extract answer-evidence pairs and selects answers according to their confidence stability across these contexts. This design enables self-evaluation without external supervision and does not rely on expanded retrieval coverage. Experiments on four open-domain question answering benchmarks show that CQC-RAG outperforms the strongest previous multi-query baseline by +4.76 pp EM on TriviaQA and +9.12 pp EM on MuSiQue, validating the effectiveness of cross-query consistency for filtering noise-induced hallucinations.

</details>

---

### [[20_Research/Papers/大模型/CFALR_Collaborative_Filtering-Augmented_Large_Language_Model_for_Personalized_Fashion_Outfit_Recommendation|CFALR: Collaborative Filtering-Augmented Large Language Model for Personalized Fashion Outfit Recommendation]]

![[assets/2606.13001_figure.png|800]]

- **arXiv**: [2606.13001](https://arxiv.org/abs/2606.13001)
- **PDF**: https://arxiv.org/pdf/2606.13001
- **详细分析**: [[20_Research/Papers/大模型/CFALR_Collaborative_Filtering-Augmented_Large_Language_Model_for_Personalized_Fashion_Outfit_Recommendation|CFALR: Collaborative Filtering-Augmented Large Language Model for Personalized Fashion Outfit Recommendation]]
- **作者**: Yujuan Ding, Junrong Liao, Yunshan Ma, Yi Bin, Wenqi Fan, Tat-Seng Chua, Qing Li
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM

#### 研究背景与动机

《CFALR: Collaborative Filtering-Augmented Large Language Model for Personalized Fashion Outfit Recommendation》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalized outfit recommendation poses a significant challenge in e-commerce and social media platforms, requiring systems that balance user preferences with aesthetic compatibility. Collaborative filtering (CF) provides a traditional solution for this, but it struggles with data-sparse scenarios and complex user-item-outfit relationships. Meanwhile, existing template-based approaches are constrained by rigid pre-designed structures. To bridge these research gaps, we introduce CFALR (Collaborative Filtering-Augmented Large Language Model for Recommendation), a novel framework that synergizes collaborative filtering with large language models for personalized outfit recommendation. Specifically, CFALR describes user-outfit interactions in natural language and leverages LLMs to capture fashion semantics while employing CF-enhanced embeddings to bridge the semantic space and the collaborative interaction spaces. Our technical contributions include: (1) the first LLM-based architecture specifically designed for personalized outfit recommendation, (2) a CF-augmented generative mechanism that efficiently navigates the extensive combination space of outfit items, and (3) trainable projection layers that optimally integrate relational and content features. Experiments on Polyvore and IQON benchmarks demonstrate CFALR's superior performance over both traditional CF-based and LLM-based methods in personalized fill-in-the-blank and personalized outfit generation tasks.

</details>

---
