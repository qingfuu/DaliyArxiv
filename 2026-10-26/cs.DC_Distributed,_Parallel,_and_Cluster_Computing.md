# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-10-26

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/KnitTrans_Coordinated_Trajectory_Transfer_for_Effective_and_Efficient_LLM_Reinforcement_Learning|KnitTrans: Coordinated Trajectory Transfer for Effective and Efficient LLM Reinforcement Learning]]

![[assets/2610.32389_figure.png|800]]

- **arXiv**: [2610.32389](https://arxiv.org/abs/2610.32389)
- **PDF**: https://arxiv.org/pdf/2610.32389
- **详细分析**: [[20_Research/Papers/大模型/KnitTrans_Coordinated_Trajectory_Transfer_for_Effective_and_Efficient_LLM_Reinforcement_Learning|KnitTrans: Coordinated Trajectory Transfer for Effective and Efficient LLM Reinforcement Learning]]
- **作者**: Bangjun Xiao, Chiheng Lou, Xiaodong Ji, Xiangwei Deng, Yikai Zhao, Gang Huang, Hailin Zhang
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.6，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《KnitTrans: Coordinated Trajectory Transfer for Effective and Efficient LLM Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Trajectory transfer from rollout to training affects both learning quality and system efficiency in large language model reinforcement learning (RL). Enforcing batch-wide training requirements can delay the admission of completed trajectories, resulting in higher architectural staleness: the additional parameter-version gap from disaggregated pipelining relative to colocated execution. Beyond admission, misalignment between data access and training consumption causes redundant movement and unnecessary waiting when transferring large trajectory payloads. We present KnitTrans, a system that coordinates the rollout-to-training path through three designs. First, constraint-preserving mini-batch admission allows flexibility in early mini-batch composition, while checking that enough capacity remains to satisfy the remaining quotas. Second, on-demand trajectory data access matches storage units to consumer assignments and overlaps micro-batch data preparation with computation. Third, multimodal encoding deduplication supports reuse across a mini-batch while preserving gradient contributions from all backbone micro-batches. Experiments show up to 93% lower architectural staleness than with train-batch admission, narrowing the learning-quality gap between disaggregated execution and colocated execution. On multimodal workloads, KnitTrans reduces transfer latency by two orders of magnitude and achieves a speedup of up to 5.8 times in transfer plus training over the baseline.

</details>

---
