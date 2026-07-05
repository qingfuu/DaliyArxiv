# cs.NE | Neural and Evolutionary Computing | 2026-07-03

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Hybridizing_a_Grouping_Metaheuristic_with_Reinforcement_Learning_for_the_One-Dimensional_Bin_Packing_Problem|Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem]]

![[assets/2607.02315_figure.png|800]]

- **arXiv**: [2607.02315](https://arxiv.org/abs/2607.02315)
- **PDF**: https://arxiv.org/pdf/2607.02315
- **详细分析**: [[20_Research/Papers/强化学习/Hybridizing_a_Grouping_Metaheuristic_with_Reinforcement_Learning_for_the_One-Dimensional_Bin_Packing_Problem|Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem]]
- **作者**: Zitouni Rania, Mostefai Mounir Sofiane, Tati Youcef, Badaoui Ikram, Bousdjira Nadine, Hasnaoui Sarah
- **cs 子类**: cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Hybridizing a Grouping Metaheuristic with Reinforcement Learning for the One-Dimensional Bin Packing Problem》归入 强化学习、大模型 方向。该论文围绕 Neural and Evolutionary Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The one-dimensional bin packing problem (1D-BPP) is a canonical NP-hard combinatorial optimization problem with broad industrial applications. We propose RL-HGGA, a hybrid algorithm that integrates Falkenauer's Hybrid Grouping Genetic Algorithm (HGGA) with a tabular Q-learning controller. Rather than applying genetic operators at fixed probabilities, a Q-learning agent dynamically selects among eight macro-actions -- including BPCX crossover, light and heavy mutation, Martello-Toth local search, and population restart -- based on an eight-dimensional state representation encoding generation progress, stagnation level, optimality gap, average fitness, population variance, and average bin fill rate. The agent is trained with an epsilon-greedy policy over 400 episodes, with epsilon decaying to 0.05. Experiments on standard benchmark families (Falkenauer T/U, Scholl 1-3, Hard28) show that RL-HGGA achieves an average optimality gap of 0.95% -- competitive with HGGA (0.75%) and well below FFD (2.47%) -- while reducing mean computation time from 64.22 s to 1.29 s, a 50x speedup. These results demonstrate that learned adaptive operator selection can achieve near-HGGA solution quality at a fraction of the computational cost.

</details>

---
