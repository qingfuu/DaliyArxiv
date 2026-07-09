# cs.CR | Cryptography and Security | 2026-07-07

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Occluding_the_Solution_Space_Planner-Agnostic_Adversarial_Attacks_on_Tolerance-Aware_Manipulation|Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation]]

![[assets/2607.03758_figure.png|800]]

- **arXiv**: [2607.03758](https://arxiv.org/abs/2607.03758)
- **PDF**: https://arxiv.org/pdf/2607.03758
- **详细分析**: [[20_Research/Papers/具身智能/Occluding_the_Solution_Space_Planner-Agnostic_Adversarial_Attacks_on_Tolerance-Aware_Manipulation|Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation]]
- **作者**: Keke Tang, Tianyu Hao, Weilong Peng, Hao Jiang, Feng Wu, Peican Zhu, Jianmin Ji, Zhihong Tian
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Agent, Robotics, Security

#### 研究背景与动机

《Occluding the Solution Space: Planner-Agnostic Adversarial Attacks on Tolerance-Aware Manipulation》归入 机器人、具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adversarial attacks on motion planning are crucial for evaluating and quantifying the intrinsic robustness of robotic manipulation. However, existing approaches are typically limited by restrictive exact-pose objectives and their reliance on planner-in-the-loop queries. To address these limitations, we propose a planner-agnostic attack framework for tolerance-aware manipulation. Our approach shifts the evaluation paradigm to task-level feasibility over goal regions, efficiently inserting adversarial obstacles without requiring oracle access to the victim system. Offline, we characterize the robot's intrinsic workspace capabilities via a kinematic occupancy heatmap, which encodes the density of feasible trajectories and robustness priors without invoking a specific planner. Online, we formulate the attack as a budgeted maximum-coverage optimization, strategically deploying obstacles subject to explicit geometric constraints to occlude the solution space. Extensive experiments across simulation and real-world scenarios demonstrate that our method reliably induces planning failures, significantly outperforming planner-in-the-loop baselines in both computational efficiency and attack efficacy.

</details>

---
