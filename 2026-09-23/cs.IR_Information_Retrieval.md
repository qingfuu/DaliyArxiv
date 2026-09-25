# cs.IR | Information Retrieval | 2026-09-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Knowledge-as-Skill_A_Structural_Design_for_Autonomous_Knowledge-Base_Use_by_LLM_Agents|Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2609.25991](https://arxiv.org/abs/2609.25991)
- **PDF**: https://arxiv.org/pdf/2609.25991
- **详细分析**: [[20_Research/Papers/具身智能/Knowledge-as-Skill_A_Structural_Design_for_Autonomous_Knowledge-Base_Use_by_LLM_Agents|Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents]]
- **作者**: Jiangxu Wu
- **cs 子类**: cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《Knowledge-as-Skill: A Structural Design for Autonomous Knowledge-Base Use by LLM Agents》归入 大模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：URL, WixQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented generation (RAG) gives large language models (LLMs) access to external knowledge, but its conventional retrieve-concatenate-generate pipeline makes retrieval decisions on behalf of the model. As tool use and agent loops become more reliable, an agent can decide whether to retrieve, what to inspect, and when to stop. This shift exposes a new bottleneck: the agent may not know what a knowledge base contains. Traditional knowledge bases expose documents as anonymous text chunks with limited information about scope, purpose, provenance, or relations. We propose Knowledge-as-Skill, an organization scheme that makes a knowledge base discoverable, navigable, and self-descriptive. It has three layers: a discovery layer centered on this http URL ; a navigation layer with one this http URL per directory; and a knowledge layer containing documents with YAML frontmatter for topic, type, provenance, and lifecycle. The design follows the Open Knowledge Format (OKF) and the Skill protocol without modifying the agent framework. We also provide knowledge-as-skill, a pipeline for converting heterogeneous collections of PDFs, Word files, web exports, and notes into this structure. In a preliminary evaluation on the WixQA enterprise customer-support benchmark, our setup obtains 0.889 Factuality and 0.816 Context Recall, compared with reported Corpus2Skill values of 0.767 and 0.708. It obtains slightly lower Faithfulness, lower Context Precision, and more interaction turns. Because the models, prompts, and knowledge-package construction differ, these results are directional cross-work evidence rather than a controlled comparison.

</details>

---
