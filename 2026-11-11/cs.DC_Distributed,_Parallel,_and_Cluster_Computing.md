# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-11-11

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Multi-Objective_Scheduling_of_LLM-Based_Multi-Agent_Workflows_in_Cloud_Computing|Multi-Objective Scheduling of LLM-Based Multi-Agent Workflows in Cloud Computing]]

![[assets/2611.13740_figure.png|800]]

- **arXiv**: [2611.13740](https://arxiv.org/abs/2611.13740)
- **PDF**: https://arxiv.org/pdf/2611.13740
- **详细分析**: [[20_Research/Papers/大模型/Multi-Objective_Scheduling_of_LLM-Based_Multi-Agent_Workflows_in_Cloud_Computing|Multi-Objective Scheduling of LLM-Based Multi-Agent Workflows in Cloud Computing]]
- **作者**: Goshgar Can Ismayilov
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Multi-Objective Scheduling of LLM-Based Multi-Agent Workflows in Cloud Computing》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) have been increasingly composed into multi-agent workflows to accomplish complex and multi-step tasks. As the open-weight models continue to close the performance gap with the proprietary ones, model parameters are becoming a less significant source of competitive advantage in the artificial intelligence market. Yet how these models are efficiently scheduled onto distributed infrastructure such as the cloud, with respect to overall latency, monetary cost and resource utilization, remains largely unaddressed in the literature despite being an increasingly critical problem. Existing agentic workflow frameworks mostly focus on output quality and task success rates over popular benchmarks, rarely accounting for execution dynamics of LLM-based agents such as inference latency, computation power of heterogeneous resources, cloud-specific billing period and resource provisioning overheads. Therefore, this paper formulates multi-agent scheduling in cloud computing as a multi-objective optimization problem that jointly minimizes makespan and cost while maximizing resource utilization. Building on this formulation, we propose MO-SAIC (Multi-Objective Scheduling of Multi-Agent Workflows in Cloud Computing), a scheduling framework comprising four multi-objective schedulers with Non-Dominated Sorting Genetic Algorithm II (NSGA-II), Weighted-Sum Genetic Algorithm (W-GA), a multi-objective adaptation of Heterogeneous Earliest Finish Time (MO-HEFT) and a random baseline (RAND). We evaluate the schedulers from the workflow scheduling, multi-objective optimization and system perspectives to measure their overall performance, quality of their Pareto-optimal fronts and impacts of workflow topology, cloud resource composition and scalability parameters. We report the experimental results with their statistical significance via the Wilcoxon test.

</details>

---
