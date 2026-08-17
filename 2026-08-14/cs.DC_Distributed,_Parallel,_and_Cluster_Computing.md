# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-08-14

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/RoutePack_Expert_Placement_and_Attention-Aware_Data_Packing_for_MoE_Reinforcement_Learning|RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning]]

![[assets/2608.12146_first_page.png|800]]

- **arXiv**: [2608.12146](https://arxiv.org/abs/2608.12146)
- **PDF**: https://arxiv.org/pdf/2608.12146
- **详细分析**: [[20_Research/Papers/大模型/RoutePack_Expert_Placement_and_Attention-Aware_Data_Packing_for_MoE_Reinforcement_Learning|RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning]]
- **作者**: Yibo Shen, Xudong Han, Xiaowei Zhu, Gen Li, Zhenxuan Pan
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《RoutePack: Expert Placement and Attention-Aware Data Packing for MoE Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DeltaNet, GQA, MQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training Mixture-of-Experts (MoE) models for reinforcement learning (RL) couples two load-balancing problems: sequence composition determines dense attention work in each data-parallel microbatch, while token routing determines sparse expert work on expert-parallel ranks. Optimizing either alone can shift the bottleneck to the other. In MoE RL, rollout-time routing replay exposes every sample's sequence length and layer-wise expert demand before its training step. We present RoutePack, a hierarchical planner that coordinates state-consistent, layer-wise expert rerouting with joint attention- and expert-aware data packing over an optimizer-step window. RoutePack first places experts independently at each MoE layer using aggregate routing demand. It then packs samples into the smallest certified, or best-known feasible, number of token-capped execution rows and optimizes their DP layout with a projected EDP-shard-aware objective. The objective combines a window-normalized linear-quadratic attention proxy with per-layer physical EP-rank peaks and minimizes the accumulated cost of the slowest EDP shard. Parallel population annealing searches fixed-row feasible layouts while preserving sample coverage, capacity, nonempty cells, equal microbatch counts, and communicator topology. State-consistent materialization preserves logical top-k routing and existing MoE kernels without microbatch-level expert replication. Across Ling-3.0-Tiny and Ling-3.0-Flash, expert rerouting improves mean trainer-measured token throughput by 3.80% and 10.50%, while routing-aware packing adds another 4.86% and 3.98%, respectively. Overall, RoutePack improves throughput by 8.85% and 14.89% over the baseline.

</details>

---
