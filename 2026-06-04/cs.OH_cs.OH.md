# cs.OH | cs.OH | 2026-06-04

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Self-Optimizing_Control_of_Continuous_Processes_Based_on_Reinforcement_Learning|Self-Optimizing Control of Continuous Processes Based on Reinforcement Learning]]

![[assets/2606.04471_figure.png|800]]

- **arXiv**: [2606.04471](https://arxiv.org/abs/2606.04471)
- **PDF**: https://arxiv.org/pdf/2606.04471
- **详细分析**: [[20_Research/Papers/强化学习/Self-Optimizing_Control_of_Continuous_Processes_Based_on_Reinforcement_Learning|Self-Optimizing Control of Continuous Processes Based on Reinforcement Learning]]
- **作者**: Ziqi Zhuo, Junghui Chen, Lei Xie, Hongye Su
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.7（加权：大模型 0.1，强化学习 0.6）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Self-Optimizing Control of Continuous Processes Based on Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper addresses the Self-Optimizing Control (SOC) problem in industrial continuous processes and proposes a Reinforcement-Learning (RL)-based SOC approach to improve dynamic performance under high-frequency disturbances. In the proposed framework, the SOC controlled variable structure is embedded in the Actor network, and reward functions are designed based on economic indicators. Through interaction with the environment, the RL agent optimizes controlled variables while implicitly considering implementability and steady-state uniqueness. Online fine-tuning is further introduced to alleviate model mismatch. Experiments on a continuous stirred-tank reactor with disturbances compare the proposed RL-based SOC method with the Objective-Guided Controlled Variable Learning Approach based on steady-state data. The results show that the RL method achieves improved dynamic performance under real-time disturbances, generates smooth controlled variable outputs without explicit regularization, reduces hyperparameter-tuning complexity, and enhances adaptability through online adjustment. Overall, the proposed RL-based SOC approach provides an effective solution for nonlinear process control and offers a promising reference for future studies involving multiple disturbances, multiple operating conditions, and model-free scenarios.

</details>

---
