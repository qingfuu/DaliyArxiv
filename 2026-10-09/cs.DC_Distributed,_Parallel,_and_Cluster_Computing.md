# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-10-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Adaptive_Multi-Discriminator_WGAN_Framework_for_Resource-Constrained_Internet_of_Vehicles_Using_Reinforcement_Learning_and_Game_Theory|Adaptive Multi-Discriminator WGAN Framework for Resource-Constrained Internet of Vehicles Using Reinforcement Learning and Game Theory]]

![[assets/2610.10926_figure.png|800]]

- **arXiv**: [2610.10926](https://arxiv.org/abs/2610.10926)
- **PDF**: https://arxiv.org/pdf/2610.10926
- **详细分析**: [[20_Research/Papers/强化学习/Adaptive_Multi-Discriminator_WGAN_Framework_for_Resource-Constrained_Internet_of_Vehicles_Using_Reinforcement_Learning_and_Game_Theory|Adaptive Multi-Discriminator WGAN Framework for Resource-Constrained Internet of Vehicles Using Reinforcement Learning and Game Theory]]
- **作者**: Farhoud Jafari Kaleibar, Amr M. Zaki, Marin Litoiu
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Adaptive Multi-Discriminator WGAN Framework for Resource-Constrained Internet of Vehicles Using Reinforcement Learning and Game Theory》归入 强化学习、世界模型、大模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Managing machine learning workloads as a network service introduces a resource-orchestration problem distinct from conventional model training; which nodes should be allocated to a task, how communication and computation budgets should be divided among them, and how service quality should be sustained as connectivity and node availability change with mobility. Deploying Generative Adversarial Networks (GANs) in Internet of Vehicles (IoV) environments is a demanding instance of this problem; resource constraints, dynamic network topologies, and competing optimization objectives mean that traditional GAN architectures cannot simultaneously achieve high accuracy, efficient resource use, low delay, and low communication overhead. This paper introduces an adaptive multi-discriminator Wasserstein GAN (MD-WGAN) framework that integrates reinforcement learning with game-theoretic coordination to address these challenges jointly. In our framework, roadside units host generators paired with Deep Q-Network (DQN) agents that select discriminator subsets and manage distributed training across mobile vehicular nodes, while a game-theoretic coordination step allocates training epochs between generators and discriminators. A unified optimization objective ties adversarial learning quality to resource efficiency, communication overhead, and latency under vehicular constraints, allowing the framework to continuously adapt its training behavior as network conditions change. Evaluation on real-world NGSIM trajectory data shows that the framework attains prediction accuracy comparable to state-of-the-art GAN baselines - the lowest RMSE (1.029) and MAE (0.894) among all evaluated methods - while markedly improving resource efficiency: average CPU utilization is reduced by roughly 28% and mean memory usage by roughly 6%, at competitive communication overhead and latency.

</details>

---
