# cs.SE | Software Engineering | 2026-08-10

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/AgentChaos_Chaos_Engineering_for_Agent_Systems_via_Programmatic_Fault_Injection|AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection]]

![[assets/2608.06790_figure.png|800]]

- **arXiv**: [2608.06790](https://arxiv.org/abs/2608.06790)
- **PDF**: https://arxiv.org/pdf/2608.06790
- **详细分析**: [[20_Research/Papers/大模型/AgentChaos_Chaos_Engineering_for_Agent_Systems_via_Programmatic_Fault_Injection|AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection]]
- **作者**: Gou Tan, Zhensu Sun, Jieke Shi, Ting Zhang, Zilong He, Qingfu Wu, Shuai Liang, Weifeng Sun, Junda He, Pengfei Chen, Chuanfu Zhang, Lwin Khin Shar...
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AgentChaos: Chaos Engineering for Agent Systems via Programmatic Fault Injection》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent systems rely on LLM APIs for every response, but these APIs can return server errors, truncated responses, or corrupted content that propagates through downstream agents and causes task failure. Evaluating robustness under these faults is crucial for reliable deployment. Existing fault injection methods are offline, require source code modification, or cannot modify specific response fields. A comprehensive evaluation also requires a systematic fault taxonomy because different fault types affect downstream agents differently. We propose AgentChaos, a chaos engineering framework for controlled, runtime, non-intrusive LLM API fault injection. Since all agent systems access LLMs through the same HTTP interface, we inject faults at this shared layer without modifying source code. We define crash, omission, and value faults on content and tool call fields, intercept and modify LLM API responses at runtime, and verify whether each fault is triggered to filter untriggered tasks and avoid underestimating fault impact. Evaluations across agent systems, benchmarks, and backbone LLMs under 65 fault configurations show that all systems degrade under fault injection, with pass@1 dropping by up to 50 percentage points. The ranking is consistent across models, suggesting that robustness depends on system implementation rather than model capability. Existing fault diagnosis methods achieve below 53% accuracy on fault type and below 56% on fault step, leaving room for improvement. We further reveal practical findings for agent system developers.

</details>

---
