# cs.CR | Cryptography and Security | 2026-09-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/ASGARD_Action-Space_Guard_for_UAV_Resilience_via_Reinforcement_Learning|ASGARD: Action-Space Guard for UAV Resilience via Reinforcement Learning]]

![[assets/2609.20982_figure.png|800]]

- **arXiv**: [2609.20982](https://arxiv.org/abs/2609.20982)
- **PDF**: https://arxiv.org/pdf/2609.20982
- **详细分析**: [[20_Research/Papers/具身智能/ASGARD_Action-Space_Guard_for_UAV_Resilience_via_Reinforcement_Learning|ASGARD: Action-Space Guard for UAV Resilience via Reinforcement Learning]]
- **作者**: Mohsen Salehi, Karthik Pattabiraman
- **cs 子类**: cs.CR, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 2.52（加权：具身智能 0.3，强化学习 0.96，世界模型 0.16，机器人 1.1）
- **关联关键词**: EmbodiedAI, RL, Security

#### 研究背景与动机

《ASGARD: Action-Space Guard for UAV Resilience via Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Baseline-RL, DRL, RARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) controllers have been recently adopted for Unmanned Aerial Vehicles (UAV) navigation and control. However, they are susceptible to action-space attacks that overwrite the action commands after the policy generates them and before the actuators execute them. While most existing defenses target attacks on the policy's inputs, those addressing action-space attacks retrain the policy at training time and are not resilient to corrupted actions at runtime. We propose ASGARD, a two-phase teacher-student pipeline for making RL-based UAV control resilient to action-space attacks. In the teacher phase, an encoder combines the UAV's physical state with action-attack-related privileged information to produce an action-attack-aware latent that trains the RL control policy and a monitor that outputs corrected action commands to the actuators. In the student phase, both the encoder and the monitor are trained via supervised learning from their teacher counterparts to run on-board using only the UAV's physical state history. We evaluate ASGARD across attack scenarios targeting different action commands on UAV. We find that ASGARD is resilient to action-space attacks and completes the missions despite the attack. We further find that ASGARD generalizes to unseen attacks and remains resilient against stealthy attacks.

</details>

---
