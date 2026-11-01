# cs.OH | cs.OH | 2026-10-30

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Dual-Agent_Reinforcement_Learning_for_Vehicle_Scheduling_and_Multi-Energy_Dispatch_in_Electric-Hydrogen-Transport_Systems|Dual-Agent Reinforcement Learning for Vehicle Scheduling and Multi-Energy Dispatch in Electric-Hydrogen-Transport Systems]]

![[assets/2610.40116_figure.png|800]]

- **arXiv**: [2610.40116](https://arxiv.org/abs/2610.40116)
- **PDF**: https://arxiv.org/pdf/2610.40116
- **详细分析**: [[20_Research/Papers/强化学习/Dual-Agent_Reinforcement_Learning_for_Vehicle_Scheduling_and_Multi-Energy_Dispatch_in_Electric-Hydrogen-Transport_Systems|Dual-Agent Reinforcement Learning for Vehicle Scheduling and Multi-Energy Dispatch in Electric-Hydrogen-Transport Systems]]
- **作者**: Fulong Yao, Yiming Xu, Maurizio Albano, Liana Cipcigan, Naeima Hamed, Bo Zou, Omar Rana
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Dual-Agent Reinforcement Learning for Vehicle Scheduling and Multi-Energy Dispatch in Electric-Hydrogen-Transport Systems》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Electric-hydrogen-transport systems (EHTSs) require coordinated scheduling of electric and hydrogen vehicles together with multi-energy dispatch. These operations form a sequential decision process: upstream vehicle scheduling (VS) determines service allocation and order, thereby endogenously shaping the electricity and hydrogen demands faced by downstream energy dispatch (ED). This paper develops a dual-agent reinforcement learning framework tailored to the heterogeneous decision structures. The vehicle-scheduling agent combines proximal policy optimisation (PPO) with a Plackett-Luce policy to learn vehicle-priority permutations, which are then mapped to feasible charger and refueller assignments through a greedy allocation. The energy-dispatch agent employs twin delayed deep deterministic policy gradient (TD3) for continuous storage and energy-flow control. The directional coupling between the two decision layers is analysed, revealing that updates to the upstream scheduling policy can shift the demand distribution experienced by the downstream dispatcher. A three-stage training mechanism is therefore introduced, combining layer-wise pretraining with concurrent fine-tuning to mitigate the effects of scheduling-induced distribution shifts on downstream ED learning. Year-long case studies show that the proposed framework achieves the lowest vehicle-service delay and energy cost among the 11 evaluated methods, demonstrating effective coordination between vehicle scheduling and multi-energy dispatch.

</details>

---
