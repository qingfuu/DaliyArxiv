# cs.IR | Information Retrieval | 2026-06-19

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/PACMS_Submodular_Context_Selection_as_a_Pluggable_Engine_for_LLM_Agents|PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents]]

![[assets/2606.20047_figure.png|800]]

- **arXiv**: [2606.20047](https://arxiv.org/abs/2606.20047)
- **PDF**: https://arxiv.org/pdf/2606.20047
- **详细分析**: [[20_Research/Papers/大模型/PACMS_Submodular_Context_Selection_as_a_Pluggable_Engine_for_LLM_Agents|PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents]]
- **作者**: Manu Ghulyani, Arunabh Singh, Karan Bharadwaj, Ankit Nath, Suranjan Goswami
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PACMS: Submodular Context Selection as a Pluggable Engine for LLM Agents》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conversational and tool-using LLM agents operate over a context window that fills from several directions simultaneously. As a session proceeds, the agent accumulates user and assistant turns, entries drawn from a persistent memory store, and often largest of all, the verbatim outputs of tool calls such as file reads, search results, and API responses. Once the cumulative context exceeds the model's token budget, the framework must decide what to keep. The prevailing mechanism is recency truncation, sometimes paired with periodic summarization. This is topic-blind: a fact established early in a session is discarded simply because it is old, even when the current user query is about exactly that fact; conversely, verbose but irrelevant recent material is retained. Agents that must recall information across many turns, the defining case for memory, are precisely where recency truncation fails. Existing alternatives sit outside the agent's assembly step. Retrieval augmented generation fetches external documents into the prompt but does not arbitrate the agent's \emph{already-present} pooled context. Context-compression methods reduce token count by rewriting or pruning text, but operate query-blind and lossily. Neither treats memory entries, conversation turns, and tool outputs as a single candidate pool to be selected from by relevance at the moment the prompt is assembled.

</details>

---

### [[20_Research/Papers/大模型/Stellar_Scalable_Multimodal_Document_Retrieval_for_Natural_Language_Queries|Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries]]

![[assets/2606.19960_figure.png|800]]

- **arXiv**: [2606.19960](https://arxiv.org/abs/2606.19960)
- **PDF**: https://arxiv.org/pdf/2606.19960
- **详细分析**: [[20_Research/Papers/大模型/Stellar_Scalable_Multimodal_Document_Retrieval_for_Natural_Language_Queries|Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries]]
- **作者**: Yuxiang Guo, Zhonghao Hu, Yuren Mao, Yuhang Liu, Congcong Ge, Xiaolu Zhang, Jun Zhou, Yunjun Gao
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Stellar: Scalable Multimodal Document Retrieval for Natural Language Queries》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal document retrieval--selecting the most relevant multimodal document from a large corpus to answer a natural language query--plays an essential role in Retrieval-Augmented Generation (RAG) systems. State-of-the-art methods represent each document and query with multiple token-level embeddings and use late interaction to achieve high effectiveness. However, such multi-vector representations incur substantial memory overhead during retrieval, leading to poor scalability and hindering real-world deployment. In this paper, we present Stellar, a scalable multimodal document retrieval framework that stores token-level document embeddings on disk and loads only a small set of candidate embeddings into memory for late interaction. Stellar comprises two key components: (i) Lexical Representation-based Filtering (LRF), which fine-tunes a Multimodal Large Language Model (MLLM) as a sparse encoder to produce high-quality lexical representations, enabling efficient and effective document filtering to significantly reduce the candidate set; (ii) Efficient Disk-backed Late Interaction (DLI), which designs an on-disk token embedding storage layout guided by a balanced clustering algorithm, and dynamically loads only the necessary token embeddings into memory using a simple yet effective cost model. Extensive experiments on four real-world benchmarks and a newly presented large-scale dataset demonstrate that Stellar reduces memory overhead and query latency by 1-2 orders of magnitude compared to existing methods without compromising retrieval effectiveness.

</details>

---
