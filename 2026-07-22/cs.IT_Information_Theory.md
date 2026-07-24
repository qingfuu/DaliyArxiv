# cs.IT | Information Theory | 2026-07-22

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Accelerating_Heterogeneous_Agent_Collaboration_in_Dynamic_Edge_Networks|Accelerating Heterogeneous Agent Collaboration in Dynamic Edge Networks]]

![[assets/2607.18244_figure.png|800]]

- **arXiv**: [2607.18244](https://arxiv.org/abs/2607.18244)
- **PDF**: https://arxiv.org/pdf/2607.18244
- **详细分析**: [[20_Research/Papers/大模型/Accelerating_Heterogeneous_Agent_Collaboration_in_Dynamic_Edge_Networks|Accelerating Heterogeneous Agent Collaboration in Dynamic Edge Networks]]
- **作者**: Tianji He, Yulin Shao, Fen Hou
- **cs 子类**: cs.IT, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Accelerating Heterogeneous Agent Collaboration in Dynamic Edge Networks》归入 大模型、强化学习 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying large language models (LLMs) at the network edge is hindered by their enormous cost, yet the reasoning quality they provide remains indispensable. Heterogeneous collaboration between edge small models and a server LLM has emerged as a promising direction, but existing methods fail under the dynamic conditions of multi-user contention, autoregressive generation, and time-varying resources. This paper puts forward a process reward model (PRM)-aided two-stage decoupled acceleration (PRADA) framework, which is built on a fundamental change of perspective: instead of querying a PRM online, which cripples multi-user systems with prohibitive latency, we use the PRM solely as an offline teacher. Its reasoning-quality intuition is fully distilled into a lightweight policy that screen each step locally, without any context upload, while a Lagrangian scheduler at the server resolves resource contention through a threshold-structured policy. Across diverse reasoning benchmarks, PRADA retains the vast majority of the LLM's accuracy while substantially reducing end-to-end latency. The results further reveal threshold effects for both server parallel capacity and total bandwidth: performance saturates beyond critical resource levels, after which the system bottleneck shifts from queuing to computation or from communication to contention. These structural findings provide actionable guidance for joint provisioning of computation and communication resources without requiring per-benchmark tuning.

</details>

---
