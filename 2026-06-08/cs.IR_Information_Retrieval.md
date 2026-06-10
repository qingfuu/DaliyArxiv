# cs.IR | Information Retrieval | 2026-06-08

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Constrained_Dominant_Sets_for_Multimodal_Document_Question_Answering|Constrained Dominant Sets for Multimodal Document Question Answering]]

![[assets/2606.07252_first_page.png|800]]

- **arXiv**: [2606.07252](https://arxiv.org/abs/2606.07252)
- **PDF**: https://arxiv.org/pdf/2606.07252
- **详细分析**: [[20_Research/Papers/大模型/Constrained_Dominant_Sets_for_Multimodal_Document_Question_Answering|Constrained Dominant Sets for Multimodal Document Question Answering]]
- **作者**: Ambuj Mehrish, Sebatiano Vascon
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Constrained Dominant Sets for Multimodal Document Question Answering》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MMLongBench, VisDoMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long multimodal document question answering is limited by which evidence reaches the reader, rather than by the quantity retrieved. In lengthy documents, findings often recur across figures, captions, and introductory sentences, causing similarity based retrievers in modern multimodal retrieval-augmented generation (RAG) systems to allocate resources to near-duplicates while overlooking complementary evidence. This work introduces a retriever that selects evidence as a Constrained Dominant Set (CDS) on a query-augmented affinity graph, offering three advantages that similarity ranking does not. First, the query is encoded as a hard structural constraint, ensuring that every selected element is directly connected to the question through the cluster anchor. Second, the relevance-redundancy balance is determined automatically by a spectral bound, eliminating the need for manually tuned trade offs required by diversity-aware selectors. Third, the selection process achieves a global equilibrium via replicator dynamics, thereby avoiding the distortions introduced by greedy heuristics. The method is inherently graph-based and does not require training. Using a Qwen3-VL-32B reader, CDS establishes a new state of the art on VisDoMBench ($66.99$ average) and improves over the no-retrieval baseline by $37.1$ points on VisDoMBench and $4.8$ on MMLongBench-Doc.

</details>

---
