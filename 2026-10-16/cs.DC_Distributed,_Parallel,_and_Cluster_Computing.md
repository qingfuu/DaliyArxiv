# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-10-16

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/ReFlow_Replay-Driven_Decoupling_for_Efficient_RL_Post-Training|ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training]]

![[assets/2610.21640_figure.jpg|800]]

- **arXiv**: [2610.21640](https://arxiv.org/abs/2610.21640)
- **PDF**: https://arxiv.org/pdf/2610.21640
- **详细分析**: [[20_Research/Papers/大模型/ReFlow_Replay-Driven_Decoupling_for_Efficient_RL_Post-Training|ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training]]
- **作者**: Yukun Tian, Junwei Su, Haofeng Xu, Lansong Diao, Zhengping Qian, Weibo Zhao, Wenchao Zhou, Ruiting Zhou, Chuan Wu
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.3，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《ReFlow: Replay-Driven Decoupling for Efficient RL Post-Training》归入 强化学习、大模型、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：StreamRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has been a critical paradigm for improving large language model (LLM) reasoning and agentic capabilities, but its efficiency remains a major bottleneck. Existing RL systems commonly rely on asynchronous execution to overlap rollout generation with policy optimization for enhanced efficiency. However, this approach faces inherent limitations: mild policy staleness offers only limited training efficiency gains, whereas aggressive asynchrony can degrade model quality and yields diminishing efficiency gains. The dynamic nature of LLM RL and multi-turn agentic workloads further challenges RL system design, as resource demands shift over time, making static resource allocation and generation strategy inefficient. This paper presents ReFlow, a system-algorithm co-designed RL framework for efficient LLM post-training. Its key insight is that, unlike existing RL frameworks which consume each trajectory only once, experience replay of recent trajectories enables effective sample reuse, thereby amortizing the high cost of rollout generation without incurring excessive policy staleness. To fully exploit this opportunity, ReFlow adopts a decoupled and adaptive architecture with three key designs: a dual replay data cycle supports efficient experience reuse while balancing training throughput and optimization stability; an elastic resource pool enables dynamic resource placement to accommodate evolving RL workloads; an adaptive scheduler coordinates generation strategies and resource allocation to improve resource utilization and boost generation throughput. Experiments across representative single-turn reasoning and multi-turn agentic RL tasks show that ReFlow improves training throughput by up to $2.06\times$ over state-of-the-art synchronous and asynchronous RL systems, while maintaining comparable or better model performance.

</details>

---
