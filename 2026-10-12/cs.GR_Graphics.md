# cs.GR | Graphics | 2026-10-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/PriMoRetarget_Humanoid_Motion_Transfer_Through_Prioritized_Motion_Retargeting|PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting]]

![[assets/2610.12642_figure.png|800]]

- **arXiv**: [2610.12642](https://arxiv.org/abs/2610.12642)
- **PDF**: https://arxiv.org/pdf/2610.12642
- **详细分析**: [[20_Research/Papers/机器人/PriMoRetarget_Humanoid_Motion_Transfer_Through_Prioritized_Motion_Retargeting|PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting]]
- **作者**: Nicholas Ioannidis, Dun Yang, Max Smith, Tue Vu, Ziyu Zhang, Shayegan Omidshafiei, Xue Bin Peng
- **cs 子类**: cs.GR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《PriMoRetarget: Humanoid Motion Transfer Through Prioritized Motion Retargeting》归入 具身智能、机器人 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion retargeting is a critical preprocessing step for transferring human motion data to humanoid robots. While existing methods are effective for single-character motions, interactions involving multiple characters and objects introduce additional contacts and spatial relationships that must be preserved. Retargeting is commonly formulated as a weighted multi-objective optimization problem, where conflicting objectives can require careful tuning of relative weights and can still compromise important motion characteristics. We introduce PriMoRetarget, a prioritized motion-retargeting framework that replaces relative objective weighting with an explicit priority hierarchy. Lower-priority updates are constrained to preserve higher-priority objectives, allowing critical characteristics such as foot placement and interaction contacts to take precedence over lower-priority pose objectives. The method is evaluated on four datasets spanning single-character motion, character-object manipulation, and character-character interactions. The resulting motions better preserve task-relevant interactions and provide reference trajectories that can be tracked more reliably than those produced by widely used retargeting methods.

</details>

---
