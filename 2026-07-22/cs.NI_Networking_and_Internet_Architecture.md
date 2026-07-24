# cs.NI | Networking and Internet Architecture | 2026-07-22

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/HACO_Hedged_Agent_Computing_for_Reliable_LLM_Systems|HACO: Hedged Agent Computing for Reliable LLM Systems]]

![[assets/2607.19215_figure.png|800]]

- **arXiv**: [2607.19215](https://arxiv.org/abs/2607.19215)
- **PDF**: https://arxiv.org/pdf/2607.19215
- **详细分析**: [[20_Research/Papers/大模型/HACO_Hedged_Agent_Computing_for_Reliable_LLM_Systems|HACO: Hedged Agent Computing for Reliable LLM Systems]]
- **作者**: Enhan Li, Hongyang Du
- **cs 子类**: cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《HACO: Hedged Agent Computing for Reliable LLM Systems》归入 大模型 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：InfiAgent-Bench, MatplotBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As large language model (LLM) agents move from isolated prompting to longhorizon workflows, failures increasingly arise at the role-to-instance binding boundary, where task-specific role requests must be assigned to concrete agent instances under current service, network, and query conditions. Existing agent system research has improved role specialization, workflow topology, memory, and tool use, but often assumes a fixed stable execution environment. This assumption limits deployed reliability, because the same role request can exhibit different latency, failure probability, and output quality across agent instances operating under different service regions and network conditions. We propose Hedged Agent Computing (HACO), a runtime control scheme that treats each role request as a reliability-constrained selection problem over candidate agent instances, each coupling a role type, an LLM, and a concrete execution environment. Different from routing, HACO adaptively selects a hedge set of candidates for each invocation. Its allocation rule combines optimistic ranking, which prioritizes candidates with high estimated quality, reliability, and informative uncertainty, with conservative reliability accumulation, which stops selection only after the hedge set reaches a target success probability. Through experience harvesting, HACO updates candidate and link profiles from all executed candidate traces, including quality, success, latency, and network statistics. Experiments on various benchmarks, together with runtime degradation studies, show that HACO improves robustness and output quality under changing deployment conditions, while using lower token and latency cost than exhaustive parallel execution.

</details>

---
