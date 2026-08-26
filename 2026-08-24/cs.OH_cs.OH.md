# cs.OH | cs.OH | 2026-08-24

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Multi-Objective_Deep_Reinforcement_Learning_for_Secure_and_Stable_Power_System_Operation|Multi-Objective Deep Reinforcement Learning for Secure and Stable Power System Operation]]

![[assets/2608.20914_first_page.png|800]]

- **arXiv**: [2608.20914](https://arxiv.org/abs/2608.20914)
- **PDF**: https://arxiv.org/pdf/2608.20914
- **详细分析**: [[20_Research/Papers/强化学习/Multi-Objective_Deep_Reinforcement_Learning_for_Secure_and_Stable_Power_System_Operation|Multi-Objective Deep Reinforcement Learning for Secure and Stable Power System Operation]]
- **作者**: Ioannis Papadopoulos, Georgios Tsaousoglou, Johanna Vorwerk
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.7（加权：大模型 0.1，强化学习 1.6）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Multi-Objective Deep Reinforcement Learning for Secure and Stable Power System Operation》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The ongoing energy transition challenges the stable operation of power systems and increases the need for rapid decision-making under uncertainty. While reinforcement learning has emerged as a promising framework for power system control and operation, existing applications typically focus on a single operational criterion, such as thermal security or small-signal stability. However, power system operation is inherently multi-objective and may involve trade-offs between objectives. This paper develops a unified-control deep reinforcement learning agent that maintains thermal security under stochastic load variations while steering the system toward operating points with improved damping of the most critical mode. Compared to a thermal-security-only agent and a business-as-usual policy, the proposed agent achieves a better balance among the operational objectives considered, with notably improved damping and negligible thermal-security violations. Finally, the operational value of increased critical damping is demonstrated under small- and large-signal disturbances, where operating points with higher damping lead to faster oscillation decay and improved critical clearing times.

</details>

---
