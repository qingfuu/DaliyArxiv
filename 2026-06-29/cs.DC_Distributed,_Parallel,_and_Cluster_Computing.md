# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-06-29

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/P-ARC_Exploiting_Subproblem_Independence_for_Parallel_Multi-Robot_Motion_Planning|P-ARC: Exploiting Subproblem Independence for Parallel Multi-Robot Motion Planning]]

![[assets/2606.27625_figure.png|800]]

- **arXiv**: [2606.27625](https://arxiv.org/abs/2606.27625)
- **PDF**: https://arxiv.org/pdf/2606.27625
- **详细分析**: [[20_Research/Papers/机器人/P-ARC_Exploiting_Subproblem_Independence_for_Parallel_Multi-Robot_Motion_Planning|P-ARC: Exploiting Subproblem Independence for Parallel Multi-Robot Motion Planning]]
- **作者**: James D. Motes, Marco Morales, Nancy M. Amato
- **cs 子类**: cs.DC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《P-ARC: Exploiting Subproblem Independence for Parallel Multi-Robot Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents Parallel ARC (P-ARC), a parallel variant of the Adaptive Robot Coordination (ARC) approach to multi-robot motion planning (MRMP). P-ARC proposes a parallel variant for each of the three main stages in ARC: initial individual solutions, conflict detection, and conflict resolution, exploiting the independence created by ARC's decomposition of the MRMP problem. Additionally, we employ an OR-parallel multi-start strategy to both ARC and P-ARC, creating a hybrid parallel strategy OR-P-ARC. We evaluate the impact of the different parallel strategies for ARC using a set of scaling 2D mobile and planar manipulator scenarios with up to 128 robots to control for conflicts and work distribution across the stages of ARC. Additionally, we demonstrate planning time speedups approaching 4X over the sequential version for large Panda multi-manipulator teams in real-world inspired scenarios when deploying 16 CPU cores.

</details>

---
