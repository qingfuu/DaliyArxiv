# cs.OH | cs.OH | 2026-07-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Centralized_PPO-Based_DRL_for_Multi-UAV-BS_Positioning_and_Trajectory_Optimization_in_Disaster_Response_Networks|Centralized PPO-Based DRL for Multi-UAV-BS Positioning and Trajectory Optimization in Disaster Response Networks]]

![[assets/2607.02533_figure.png|800]]

- **arXiv**: [2607.02533](https://arxiv.org/abs/2607.02533)
- **PDF**: https://arxiv.org/pdf/2607.02533
- **详细分析**: [[20_Research/Papers/具身智能/Centralized_PPO-Based_DRL_for_Multi-UAV-BS_Positioning_and_Trajectory_Optimization_in_Disaster_Response_Networks|Centralized PPO-Based DRL for Multi-UAV-BS Positioning and Trajectory Optimization in Disaster Response Networks]]
- **作者**: Azim Akhtarshenas, Mario Rico Ibanez, Matteo Bernabe, David Lopez-Perez, Merouane Debbah
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型
- **相关性评分**: 1.9（加权：大模型 0.1，强化学习 1，机器人 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Centralized PPO-Based DRL for Multi-UAV-BS Positioning and Trajectory Optimization in Disaster Response Networks》归入 强化学习、机器人、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle-mounted base stations (UAV-BSs) constitute a flexible and effective solution for global positioning system (GPS)-free emergency and disaster scenarios, where the rapid deployment of communication infrastructure is critical for maximizing life-saving operations. In this work, we extend a centralized learning framework to a multi-UAV-BS network architecture, in which a single centralized UAV-BS -- as an intelligent agent -- coordinates the three-dimensional positioning and navigation of multiple UAV-BSs, while the remaining UAV-BSs actively serve ground user equipments (UEs) with uncertain positions. We formulate a fairness-aware sum-throughput maximization problem for UAV-BS coordination, which is inherently nonconvex due to the non-linear and interference-coupled throughput expressions. To address this challenge, we cast the problem as a Markov Decision Process (MDP) and solve it using a deep reinforcement learning (DRL) framework based on Proximal Policy Optimization (PPO). The central agent interacts with the environment and learns optimal joint positioning policies that guide the serving UAV-BSs to provide efficient, adaptive, and resilient wireless coverage. The proposed approach exploits spatial configuration and radio signal sensing capabilities to dynamically adapt to heterogeneous UE mobility patterns. Extensive simulations are conducted to evaluate the performance of the proposed method. Numerical results demonstrate that PPO shows competitive performance during both training and evaluation phases. Furthermore, comparative analysis with state-of-the-art RL algorithms, namely Deep Deterministic Policy Gradient (DDPG) and Deep QNetwork (DQN), shows that PPO consistently outperforms these methods in terms of convergence stability, mean reward, and network throughput.

</details>

---
