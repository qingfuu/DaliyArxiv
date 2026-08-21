# cs.CR | Cryptography and Security | 2026-08-19

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/KeyPooling_Measuring_Where_LLM_API_Relay_Paths_Collapse_Prompt_Cache_Isolation|KeyPooling: Measuring Where LLM API Relay Paths Collapse Prompt Cache Isolation]]

![[assets/2608.17485_first_page.png|800]]

- **arXiv**: [2608.17485](https://arxiv.org/abs/2608.17485)
- **PDF**: https://arxiv.org/pdf/2608.17485
- **详细分析**: [[20_Research/Papers/大模型/KeyPooling_Measuring_Where_LLM_API_Relay_Paths_Collapse_Prompt_Cache_Isolation|KeyPooling: Measuring Where LLM API Relay Paths Collapse Prompt Cache Isolation]]
- **作者**: Bowen Sun, Yixi Cai, Xiaogeng Liu, Zhengyue Zhao, Yinzhi Cao, Chaowei Xiao
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《KeyPooling: Measuring Where LLM API Relay Paths Collapse Prompt Cache Isolation》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) API relays authenticate customers separately but often forward requests through shared provider credentials. Providers scope prompt caches to upstream principals and namespaces, so relay customers mapped to one cache identity can observe each other's cache state. Prior work showed cache sharing at selected endpoints but did not identify which credential, pool, adapter, or nested hop controls the finalidentity. We present KeyPooling, a measurement method that traces customer identity through cache lookup and write, verifies runtime transformations, and tests one predicted identity component at a time. Across five open-source gateways connected to OpenAI and Anthropic, none bound customers to upstream credentials by default; under a shared credential, all five exposed cross-customer cache reads for both providers. Principal and namespace splits, pool associations, and adapter and nested-relay contrasts localized the controlling transformations. In an outcome-independent weekly OpenRouter frame, tests covered 80.5% of eligible token volume and found cross-account reads for 12 of 28 labels carrying 33.7% of volume. On one production route, a controlled procedure recovered eight consecutive target positions without target access. Broader tests identify cache granularity, routing, rate limits, attribution, and budget as conditions for token-by-token recovery, not security controls. We derive a defense contract: every customer must enter a provider-enforced domain, or a namespace derived from authenticated identity must survive every final cache lookup and write. Placing this split after reusable public prefixes preserved most modeled reuse at a 1.7-2.5% cost increase.

</details>

---

### [[20_Research/Papers/大模型/MITRE-SAGE_A_Multi-Agent_Cybersecurity_Question-Answering_model|MITRE-SAGE: A Multi-Agent Cybersecurity Question-Answering model]]

![[assets/2608.16921_figure.png|800]]

- **arXiv**: [2608.16921](https://arxiv.org/abs/2608.16921)
- **PDF**: https://arxiv.org/pdf/2608.16921
- **详细分析**: [[20_Research/Papers/大模型/MITRE-SAGE_A_Multi-Agent_Cybersecurity_Question-Answering_model|MITRE-SAGE: A Multi-Agent Cybersecurity Question-Answering model]]
- **作者**: Ali Habibzadeh, Farid Feyzi, Reza Ebrahimi Atani
- **cs 子类**: cs.CR, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《MITRE-SAGE: A Multi-Agent Cybersecurity Question-Answering model》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MITRE-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective cybersecurity operations require timely and accurate analysis of large-scale heterogeneous security information; however, analysts increasingly struggle with information overload, alert fatigue, and time-constrained decision-making. Although large language models (LLMs) have demonstrated promising capabilities for question answering (QA), their effectiveness in cybersecurity remains limited by insufficient domain knowledge, a tendency to hallucinate, and difficulties in capturing both semantic and structural relationships. This work proposes MITRE-SAGE, a multi-agent retrieval-augmented generation framework that integrates semantic and structural cybersecurity knowledge to improve the reliability and interpretability of LLM-based QA systems. By decomposing complex tasks into query interpretation, evidence retrieval, and answer synthesis, MITRE-SAGE effectively supports cybersecurity tasks such as vulnerability assessment, threat profiling, and relationship extraction. Furthermore, we propose MITRE-QA, a comprehensive benchmark comprising 3,000 question-answer pairs for evaluating LLMs across diverse cybersecurity knowledge tasks, and use it to systematically evaluate MITRE-SAGE against representative baseline methods. Extensive experiments demonstrate that MITRE-SAGE consistently outperforms standalone LLMs and conventional RAG approaches. Notably, a lightweight configuration comprising Qwen2.5-7B sub-agents and a Qwen2.5-14B orchestrator achieves superior performance on five of the eight benchmark tasks, indicating the effectiveness of the proposed multi-agent framework. The results highlight the potential of MITRE-SAGE as a scalable and interpretable approach for reliable cybersecurity QA, while MITRE-QA provides a standardized benchmark for future research.

</details>

---
