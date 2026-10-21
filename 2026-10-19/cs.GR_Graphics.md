# cs.GR | Graphics | 2026-10-19

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Structural_Affinity_An_Algorithm_for_Coherent_Cage-Based_Shape_Design|Structural Affinity: An Algorithm for Coherent Cage-Based Shape Design]]

![[assets/2610.23173_figure.jpg|800]]

- **arXiv**: [2610.23173](https://arxiv.org/abs/2610.23173)
- **PDF**: https://arxiv.org/pdf/2610.23173
- **详细分析**: [[20_Research/Papers/机器人/Structural_Affinity_An_Algorithm_for_Coherent_Cage-Based_Shape_Design|Structural Affinity: An Algorithm for Coherent Cage-Based Shape Design]]
- **作者**: Aviraj Newatia, Shengan Yang, Hantao Zhong, Rika Antonova
- **cs 子类**: cs.GR, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Structural Affinity: An Algorithm for Coherent Cage-Based Shape Design》归入 机器人、具身智能 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ShapeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cage-based deformation (CBD) parametrises 3D geometry through a small set of control handles, effectively enabling a variety of tasks from animation and interactive modelling to tool-based co-design, neural deformation transfer, and aerodynamic shape optimization. Many optimization approaches relying on CBD employ regularisation strategies to reduce the distortion of the deformed mesh by encouraging smooth, regular cage deformations. These techniques offer soft guidance to an optimization algorithm towards desirable deformations, but compete with the task objective rather than changing the deformation parameterization itself. In this work we introduce Structural Affinity for CBD, an explicit regularisation method which enables smooth deformations through control cages by exploiting a two-cage structure to couple cage-handle motion directly. Structural Affinity precomputes an affinity matrix using mean-value coordinates, binding the inner control-cage to a coarser outer-cage. This matrix defines how much a cage handle displacement propagates to neighbouring handles which substantially decreases and often eliminates cage self-intersections, reduces mesh distortion, and adds linear overhead at deformation time. Across robotic control--morphology co-design, source-to-target neural deformation transfer, and aerodynamic wing shape optimization, Structural Affinity produces more regular deformations and substantially reduces reliance on hand-designed structural loss terms. We report consistent gains on three complementary diagnostics: the cotangent Laplacian, a proxy for surface smoothness; cage distortion, capturing whether control handles move coherently; and surface roughness, which measures undesirable oscillation in wing geometry.

</details>

---
