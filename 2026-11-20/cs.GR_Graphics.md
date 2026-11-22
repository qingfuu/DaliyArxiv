# cs.GR | Graphics | 2026-11-20

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/A_Tutorial_on_Complementarity-Based_Contact_Models_for_Robotics|A Tutorial on Complementarity-Based Contact Models for Robotics]]

![[assets/2611.26600_first_page.png|800]]

- **arXiv**: [2611.26600](https://arxiv.org/abs/2611.26600)
- **PDF**: https://arxiv.org/pdf/2611.26600
- **详细分析**: [[20_Research/Papers/机器人/A_Tutorial_on_Complementarity-Based_Contact_Models_for_Robotics|A Tutorial on Complementarity-Based Contact Models for Robotics]]
- **作者**: Onur Beker, A. René Geist, Michael Posa, Marc Toussaint, Justin Carpentier, Georg Martius
- **cs 子类**: cs.GR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Tutorial on Complementarity-Based Contact Models for Robotics》归入 机器人、具身智能 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulating rigid-body dynamics with contact is fundamental to robotics, from motion synthesis and control to mechanism design. Many widely used simulators rely on cone complementarity formulations, whose physical assumptions and numerical solution require substantial background. While excellent surveys, monographs, and course notes exist, they mostly address computational mechanics or computer graphics or document a single simulator. To the best of our knowledge, a self-contained pedagogical treatment for robotics, bringing these formulations and their solvers together with complete derivations and a unified notation, does not yet exist. This tutorial addresses this gap by connecting rigid-body dynamics, conic optimization, and frictional contact. In particular, we explain how complementarity conditions encode non-penetration and frictional dissipation, determining separation, sticking, and sliding without prescribed contact modes. We distinguish equivalent transcriptions from convex relaxations, showing how the latter can introduce artifacts such as lift-off and creep. We examine the existence and uniqueness of motion and contact forces, including the solver's role in selecting among multiple solutions. We then compare first-order and Newton-based methods, explain regularization and proximal strategies, and discuss trade-offs between computational cost, robustness, and physical fidelity. Connections to widely used simulators, optimal control, and differentiable simulation help readers interpret simulation results, choose suitable formulations and solvers, and develop their own contact dynamics routines.

</details>

---
