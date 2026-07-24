# cs.IR | Information Retrieval | 2026-07-22

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Exposure-Based_Reinforcement_Learning_to_Rank|Exposure-Based Reinforcement Learning to Rank]]

![[assets/2607.18689_figure.png|800]]

- **arXiv**: [2607.18689](https://arxiv.org/abs/2607.18689)
- **PDF**: https://arxiv.org/pdf/2607.18689
- **详细分析**: [[20_Research/Papers/强化学习/Exposure-Based_Reinforcement_Learning_to_Rank|Exposure-Based Reinforcement Learning to Rank]]
- **作者**: Harrie Oosterhuis, Rolf Jagerman, Zhen Qin, Xuanhui Wang
- **cs 子类**: cs.IR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Exposure-Based Reinforcement Learning to Rank》归入 强化学习、世界模型 方向。该论文围绕 Information Retrieval 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) methods for learning-to-rank (LTR) can optimize (almost) any ranking goal, e.g., from precision or discounted cumulative gain to fairness-of-exposure or ranking distillation. However, standard RL is ineffective and computationally costly due to the enormous action space in LTR settings. Existing methods reach computational efficiency through custom gradient computation algorithms, but they are very complex to implement and often clash with auto-differentiation. Consequently, existing RL for LTR is not attractive to many practitioners. We reconsider RL for LTR while actively avoiding reliance on custom gradients. Contrary to the existing approaches, we focus on variance reduction and GPU computation. In doing so, we discover that high sample-efficiency can be reached through baseline corrections and partial marginalization. Furthermore, we propose an abstraction that places gradient estimation behind a document-exposure distribution, this enables seamless plug-and-play integration with auto-differentiation. Thereby, one only has to implement a loss as a differentiable function of exposure and RL for LTR can optimize it using auto-differentiation. Our experimental results reveal that our new exposure-based RL for LTR approach converges considerably faster and at significantly higher ranking performance than existing custom gradients, with no additional costs in computation time when using GPUs. In contrast, existing custom gradients result in severe stability issues when converging over many epochs, which never occur for our methods. Thus, we considerably improve RL for LTR methodology by increasing its effectiveness, efficiency, and ease of application.

</details>

---
