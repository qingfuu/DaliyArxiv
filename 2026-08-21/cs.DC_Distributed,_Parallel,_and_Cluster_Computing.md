# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-08-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/When_Do_LLM_Agents_Help_Deadline-Aware_Mixed-Criticality_Task_Scheduling_at_the_Autonomous-Vehicle_Edge|When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge]]

![[assets/2608.19557_first_page.png|800]]

- **arXiv**: [2608.19557](https://arxiv.org/abs/2608.19557)
- **PDF**: https://arxiv.org/pdf/2608.19557
- **详细分析**: [[20_Research/Papers/大模型/When_Do_LLM_Agents_Help_Deadline-Aware_Mixed-Criticality_Task_Scheduling_at_the_Autonomous-Vehicle_Edge|When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge]]
- **作者**: Reza Zakerian
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Do LLM Agents Help? Deadline-Aware Mixed-Criticality Task Scheduling at the Autonomous-Vehicle Edge》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Contract-Net, DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous vehicles offload latency-sensitive perception tasks to nearby mobile edge computing (MEC) servers, where a missed safety-critical task is unsafe rather than merely degraded. Large language models (LLMs) are increasingly proposed as adaptive, explainable schedulers, yet evidence of when they help is scarce. We study deadline-aware, mixed-criticality scheduling on heterogeneous MEC servers, where time-critical (TC) tasks must be protected at a controlled cost to best-effort traffic, and ask whether a multi-agent LLM control layer improves on a strong heuristic. We answer in two steps. First we build the heuristic: a windowed contract-net auction that orders each admission window time-critical-first by earliest deadline and places tasks by earliest-finish-time. Across 60 instances on three topologies and 15 baselines under an identical online constraint, it attains a TC completion rate of 0.902, above every baseline (Holm-corrected p &lt; 0.001; best baseline 0.838) and at 0.87 of a CP-SAT upper bound. Second, we add the LLM control plane. A controlled decomposition traces the scheduler's advantage to two ordinary factors, the batching horizon and time-critical-first ordering; the auction, the per-window LLM policy, and online adaptation add nothing while the load is stationary, where the heuristic is already near-optimal. Under a mid-run surge of safety-critical tasks the picture changes, and the LLM control plane gains significantly over both the static heuristic and the bandit. LLM orchestration therefore earns its cost only when non-stationarity opens headroom a fixed policy cannot use. We report control-plane latency and rationale, and release all code and seeded instances.

</details>

---
