# cs.IR | Information Retrieval | 2026-11-02

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Pix2Evidence_A_Multimodal_RAG_System_for_Text_and_Visual_Evidence|Pix2Evidence: A Multimodal RAG System for Text and Visual Evidence]]

![[assets/2610.41335_figure.png|800]]

- **arXiv**: [2610.41335](https://arxiv.org/abs/2610.41335)
- **PDF**: https://arxiv.org/pdf/2610.41335
- **详细分析**: [[20_Research/Papers/大模型/Pix2Evidence_A_Multimodal_RAG_System_for_Text_and_Visual_Evidence|Pix2Evidence: A Multimodal RAG System for Text and Visual Evidence]]
- **作者**: Ziniu Liu, Xiaoyang Chen, Dezhi Ye, Jie Liu, Jin Ma, Hao Deng
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, ComputerVision, Security

#### 研究背景与动机

《Pix2Evidence: A Multimodal RAG System for Text and Visual Evidence》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EVQA, MultiModalQA, RocketQA, SimpleQA, WebQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) over visually rich documents must find both relevant content and the evidence that supports an answer. Screenshot retrieval preserves images and page structure, but written facts within screenshots also need to be searchable. Moreover, topical relevance alone does not identify which retrieved tile contains evidence for the answer. We introduce Pix2Evidence, a multimodal RAG system that encodes each screenshot tile together with its available transcription into a single fused image--text representation, so that layout and readable text are considered jointly during retrieval. To guide evidence selection, a vision-language teacher describes the visible content that supports each training question. We use these descriptions to adapt the retriever, then rerank the retrieved candidates before answer generation. Extensive experiments demonstrate that Pix2Evidence outperforms state-of-the-art methods. Across five widely-used Wikipedia QA benchmarks, the non-reranked Pix2Evidence leads the main comparison in answer accuracy on four. On MMSearch, it reaches 26.0\%, 4.4 percentage points above PixelRAG. We will release the code and share derived data where licensing and privacy reviews permit.

</details>

---
