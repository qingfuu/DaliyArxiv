# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-06-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/Maestro_Workload-Aware_Cross-Cluster_Scheduling_for_LLM-Based_Multi-Agent_Systems|Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems]]

![[assets/2606.12950_figure.png|800]]

- **arXiv**: [2606.12950](https://arxiv.org/abs/2606.12950)
- **PDF**: https://arxiv.org/pdf/2606.12950
- **详细分析**: [[20_Research/Papers/大模型/Maestro_Workload-Aware_Cross-Cluster_Scheduling_for_LLM-Based_Multi-Agent_Systems|Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems]]
- **作者**: Jinghao Wang, Xiao Zhou, Xiaoyang Sun, Yihui Zhang, Yilong Li, Tianyu Wo, Xu Wang, Chunming Hu, Renyu Yang
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Maestro: Workload-Aware Cross-Cluster Scheduling for LLM-Based Multi-Agent Systems》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model based Multi-Agent Systems (LLM-MAS) have emerged as a powerful paradigm for tackling complex tasks by breaking them into collaborative workflows of specialized LLM-powered agents. However, deploying such multi-agent workloads at scale poses significant system challenges. Each user query spawns an iterative pipeline of LLM calls, greatly amplifying resource consumption compared to single-turn queries. In resource-constrained cloud settings, these workflows face non-deterministic and input-dependent costs at decode stage, heavy-tailed multi-model requirements with memory fragmentation and over-provisioning, and cross-cluster scheduling trade-offs. We present Maestro, a workload-aware scheduling system designed for LLM-MAS serving under strict GPU budgets. Maestro explicitly leverages agent semantics and roles: it predicts the output length and memory usage of each stage and uses this prediction to drive a hierarchical scheduler. At the node level, Maestro enables dynamic multi-model co-location via hierarchical weight caching and elastic memory provisioning. At the cluster level, it performs latency-aware routing to avoid cold-start delays and memory overloads. At the global level, it enforces workflow-aware prioritization to minimize head-of-line blocking for interactive tasks. Across prototype experiments and trace-driven simulations, Maestro reduces KV-reservation HBM by 67.2% and improves high-contention SLO attainment over EDF by 23.6 percentage points.

</details>

---
