# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-08-03

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/SLIM_Saturation-Aware_Lightweight_Performance_Modeling_for_LLM_Serving|SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving]]

![[assets/2607.29575_figure.png|800]]

- **arXiv**: [2607.29575](https://arxiv.org/abs/2607.29575)
- **PDF**: https://arxiv.org/pdf/2607.29575
- **详细分析**: [[20_Research/Papers/大模型/SLIM_Saturation-Aware_Lightweight_Performance_Modeling_for_LLM_Serving|SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving]]
- **作者**: Pol G. Recasens, Ferran Agullo, Yue Zhu, Chen Wang, Jordi Torres, Josep Ll. Berral
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《SLIM: Saturation-Aware Lightweight Performance Modeling for LLM Serving》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) serving commonly increases batch size to improve throughput, but performance eventually reaches a deployment-dependent plateau beyond which larger batches provide marginal gains while increasing latency and GPU memory consumption. Previous studies have attributed this behavior to HBM/DRAM bandwidth limitations, but the underlying causes have primarily been supported by conceptual arguments or high-level performance observations. As our first contribution, we present a detailed GPU characterization using hardware profiling techniques, demonstrating that throughput saturation originates in the attention kernels during the decode phase. Specifically, we show that their nearly constant arithmetic intensity as active-context lengths increases -not merely larger batch sizes- drives DRAM-bandwidth saturation, while the achieved compute throughput remains far below the hardware limit. Building on this analysis, we present the Batching Configuration Advisor (BCA), which selects the highest-throughput batching configuration satisfying a target latency constraint and identifies up to 55 GB of GPU memory allocation that can be avoided for the evaluated OPT models with minimal throughput loss. To enable these recommendations, we introduce SLIM (Saturation-Aware Lightweight Performance Model), a semi-analytical model that predicts LLM inference throughput and latency from analytical formulations of Transformer computation and memory traffic. Across the evaluated scenarios, SLIM outperforms representative performance-modeling baselines while successfully generalizing to previously unseen operating conditions.

</details>

---

### [[20_Research/Papers/大模型/Characterizing_LLM_Kernel_Access_and_Memory_Interaction_in_Multi-Partition_NUMA_GPUs|Characterizing LLM Kernel Access and Memory Interaction in Multi-Partition NUMA GPUs]]

![[assets/2607.28824_figure.png|800]]

- **arXiv**: [2607.28824](https://arxiv.org/abs/2607.28824)
- **PDF**: https://arxiv.org/pdf/2607.28824
- **详细分析**: [[20_Research/Papers/大模型/Characterizing_LLM_Kernel_Access_and_Memory_Interaction_in_Multi-Partition_NUMA_GPUs|Characterizing LLM Kernel Access and Memory Interaction in Multi-Partition NUMA GPUs]]
- **作者**: Donghyeon Joo, Sooraj Puthoor, Nuwan Jayasena, Bahar Asgari
- **cs 子类**: cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《Characterizing LLM Kernel Access and Memory Interaction in Multi-Partition NUMA GPUs》归入 大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) workloads motivate multi-partition GPUs as a path to scaling compute and memory capacity, but their non-uniform memory access characteristics and inter-partition communication can amplify contention and degrade locality, leading to suboptimal kernel latency. To address this, we analyze performance-critical LLM kernel implementations spanning weight projection, mixture-of-experts, and attention variants of state-of-the-art serving engines to present a characterization of data access patterns in multi-partition GPUs. First, we introduce memory trace analysis methodology to derive workgroup-level data access and sharing behavior, then evaluate the locality implications on latency using a cycle-level simulator. Using these tools, we categorize LLM kernel operands into three inter-workgroup sharing patterns (global, partial, or private) and show that the required optimization strategies differ across categories, from simple per-workgroup pinning to subgroup-aware co-scheduling. Our findings highlight the need for placement-aware kernel programming and smarter architectural support for work and data locality in multi-partition GPUs.

</details>

---
