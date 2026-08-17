# cs.NI | Networking and Internet Architecture | 2026-08-14

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Pareto-Aware_Hierarchical_Reinforcement_Learning_for_Online_Resource_Allocation_in_RIS-assisted_Large-Scale_IoT_Systems|Pareto-Aware Hierarchical Reinforcement Learning for Online Resource Allocation in RIS-assisted Large-Scale IoT Systems]]

![[assets/2608.13032_figure.png|800]]

- **arXiv**: [2608.13032](https://arxiv.org/abs/2608.13032)
- **PDF**: https://arxiv.org/pdf/2608.13032
- **详细分析**: [[20_Research/Papers/强化学习/Pareto-Aware_Hierarchical_Reinforcement_Learning_for_Online_Resource_Allocation_in_RIS-assisted_Large-Scale_IoT_Systems|Pareto-Aware Hierarchical Reinforcement Learning for Online Resource Allocation in RIS-assisted Large-Scale IoT Systems]]
- **作者**: Wenhan Xu, Jiashuo Jiang, Danny H. K. Tsang
- **cs 子类**: cs.NI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Pareto-Aware Hierarchical Reinforcement Learning for Online Resource Allocation in RIS-assisted Large-Scale IoT Systems》归入 强化学习 方向。该论文围绕 Networking and Internet Architecture 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DRL, MARL, PAAERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid evolution of 5G and emerging 6G networks, reconfigurable intelligent surfaces (RIS) have become a critical technology for enhancing wireless communication scenarios. However, optimizing RIS-assisted multi-user systems typically introduces high-dimensional physical layer variables and non-convex Pareto-optimal rate sets, posing severe computational challenges for real-time applications. To address these limitations, this paper proposes a dimension-reduced, hierarchical reinforcement learning (RL) framework, termed Pareto-aware autoencoder-assisted RL (PAAERL), to optimize online resource allocation in RIS-assisted Internet of Things (IoT) networks. Our approach first substitutes high-dimensional continuous RIS beamforming variables with lower-dimensional weight vectors that strictly represent the Pareto-optimal frontier, theoretically avoiding geometric information loss across both convex and non-convex rate regions. To further mitigate the curse of dimensionality in dense networks, an autoencoder architecture is integrated to execute a secondary, data-driven compression phase, mapping the priority space into a highly condensed continuous latent action space. Extensive simulations conducted across practical communication scenarios, including multi-user mobile edge computing (MEC) networks, demonstrate that the proposed PAAERL framework drastically reduces offline training times, accelerates online policy convergence, and significantly decreases overall network costs compared to state-of-the-art benchmarks, underscoring its exceptional scalability and practical viability for next-generation intelligent IoT environments.

</details>

---
