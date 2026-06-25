# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-06-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/BARD-MARL_Byzantine-Agent_Detection_for_Learned_Communication_in_Multi-Agent_Reinforcement_Learning|BARD-MARL: Byzantine-Agent Detection for Learned Communication in Multi-Agent Reinforcement Learning]]

![[assets/2606.20701_figure.png|800]]

- **arXiv**: [2606.20701](https://arxiv.org/abs/2606.20701)
- **PDF**: https://arxiv.org/pdf/2606.20701
- **详细分析**: [[20_Research/Papers/强化学习/BARD-MARL_Byzantine-Agent_Detection_for_Learned_Communication_in_Multi-Agent_Reinforcement_Learning|BARD-MARL: Byzantine-Agent Detection for Learned Communication in Multi-Agent Reinforcement Learning]]
- **作者**: Almond Kiruthu Murimi
- **cs 子类**: cs.DC, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《BARD-MARL: Byzantine-Agent Detection for Learned Communication in Multi-Agent Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BARD-MARL, MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned communication improves coordination in cooperative multi-agent reinforcement learning, but it also creates a trust problem: a trained policy may route information through agents that have become faulty or adversarial. This paper studies Byzantine-agent detection for learned-communication MARL in adaptive traffic signal control. We propose BARD-MARL, a post-hoc diagnostic layer on top of BayesG, which is used as an attributed communication substrate rather than as a contribution of this paper. BARD-MARL combines two agent-level evidence streams: policy-graph features extracted from state-action trajectories and Bayesian trust statistics computed from BayesG latent mask probabilities. Across fixed-action, observation-flip, random-noise, and coordinated attacks in SUMO traffic grids, the results show that these signals are complementary rather than universally dominant. On a 25-agent grid, BARD-MARL reaches 0.843 AUC-ROC under a 10% observation-flip attack, while policy-graph-only detection reaches 0.917 AUC-ROC under a 10% coordinated attack. On a 100-agent grid, the unified BARD-MARL variant reaches 0.982 AUC-ROC for both 10% fixed-action and 10% coordinated attacks. The study shows that learned communication policies expose useful diagnostic evidence, but credible resilience claims require attack-specific ablations and explicit separation between coordination, detection, and mitigation.

</details>

---
