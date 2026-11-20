# cs.OH | cs.OH | 2026-11-18

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Safe_Reinforcement_Learning_with_Hard_Constraints_Policy_Gradient_Methods_with_Intersample_Guarantees|Safe Reinforcement Learning with Hard Constraints: Policy Gradient Methods with Intersample Guarantees]]

![[assets/2611.21987_first_page.png|800]]

- **arXiv**: [2611.21987](https://arxiv.org/abs/2611.21987)
- **PDF**: https://arxiv.org/pdf/2611.21987
- **详细分析**: [[20_Research/Papers/具身智能/Safe_Reinforcement_Learning_with_Hard_Constraints_Policy_Gradient_Methods_with_Intersample_Guarantees|Safe Reinforcement Learning with Hard Constraints: Policy Gradient Methods with Intersample Guarantees]]
- **作者**: Vipul K. Sharma, S. Sivaranjani
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.4（加权：强化学习 1.4）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《Safe Reinforcement Learning with Hard Constraints: Policy Gradient Methods with Intersample Guarantees》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We develop a policy-gradient (PG) reinforcement learning (RL) framework with hard inter-sample control barrier function (CBF)-based safety constraints for nonlinear sampled-data systems. We first design a class of stochastic policies with support truncated to sampling-period-dependent safe control sets, that guarantee safety-by-construction at sampling instants. We then propose a model-free PG algorithm that searches over the class of safe-by-design policies and establish sufficient conditions on sampling-period such that any action sampled from safe control sets remains safe throughout the sampling interval, providing inter-sample guarantees. We further establish finite-time convergence and sample complexity guarantees for the proposed PG algorithm and characterize its global optimality under gradient dominance. Finally, we illustrate inter-sample safety guarantees on a safe quadrotor navigation environment.

</details>

---
