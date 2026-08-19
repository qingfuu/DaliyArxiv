# cs.IR | Information Retrieval | 2026-08-17

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/How_retriever_redundancy_and_diversity_impact_RAG_effectiveness|How retriever redundancy and diversity impact RAG effectiveness]]

![[assets/2608.13956_figure.png|800]]

- **arXiv**: [2608.13956](https://arxiv.org/abs/2608.13956)
- **PDF**: https://arxiv.org/pdf/2608.13956
- **详细分析**: [[20_Research/Papers/大模型/How_retriever_redundancy_and_diversity_impact_RAG_effectiveness|How retriever redundancy and diversity impact RAG effectiveness]]
- **作者**: Jonathan J Ross, Bevan Koopman, Anton van der Vegt, Guido Zuccon
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM

#### 研究背景与动机

《How retriever redundancy and diversity impact RAG effectiveness》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Information Retrieval 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FictionalQA, GroupQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In RAG, while the retriever typically ranks documents by their individual relevance to the query, the generator instead produces an answer based on the retrieved documents as a whole. This paper investigates how redundancy and diversity from the retrieved document set impact the generator in terms of answer correctness. Previous work has provided a mix of findings: some showing that redundancy improves generation by reinforcing relevant information, others that LLM-based paraphrasing of the same content may be beneficial. Many of these studies did not control for confounding factors like whether the documents contained the exact answer or not, and if parametric knowledge plays a role. We conduct a carefully controlled experiment investigating three key scenarios of retrieved document sets: 1) Duplicate (exact copies of the same document), 2) Paraphrased (LLM rephrased versions of one document) and 3) Diverse (documents from different genres each containing relevant information in different forms). We control for which documents contain the answer in exact match or rephrased form. Evaluation is done with FictionalQA, a synthetic, fictional question-answer dataset that ensures the LLM generator prior knowledge cannot answer the question; the answer must come from retrieved documents. We show that duplicate redundancy and LLM paraphrasing does not significantly improve answer correctness. However, providing diverse documents is highly beneficial, improving answer correctness by 17%-47%. We further show this improvement is driven by diverse forms of document genre (news, blogs, etc.) alone and not a consequence of more relevant answer being available to generator. Our findings help to direct more attention to how new retrieval methods might improve RAG by catering to the generator preference for diversity in retrieval results.

</details>

---
