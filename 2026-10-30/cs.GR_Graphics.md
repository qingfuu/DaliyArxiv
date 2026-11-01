# cs.GR | Graphics | 2026-10-30

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Mastering_Multi-State_Dynamics_Continuum_Damage_and_Viscoplastic_MPM_for_RL-Based_Dexterous_Manipulation|Mastering Multi-State Dynamics: Continuum Damage and Viscoplastic MPM for RL-Based Dexterous Manipulation]]

![[assets/2610.39975_figure.png|800]]

- **arXiv**: [2610.39975](https://arxiv.org/abs/2610.39975)
- **PDF**: https://arxiv.org/pdf/2610.39975
- **详细分析**: [[20_Research/Papers/具身智能/Mastering_Multi-State_Dynamics_Continuum_Damage_and_Viscoplastic_MPM_for_RL-Based_Dexterous_Manipulation|Mastering Multi-State Dynamics: Continuum Damage and Viscoplastic MPM for RL-Based Dexterous Manipulation]]
- **作者**: Yusen Feng, Shangbo Luan
- **cs 子类**: cs.GR
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 1.6（加权：具身智能 1.2，强化学习 0.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Mastering Multi-State Dynamics: Continuum Damage and Viscoplastic MPM for RL-Based Dexterous Manipulation》归入 具身智能、强化学习、机器人 方向。该论文围绕 Graphics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CRESSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation of multi-state materials needs a simulator that handles large deformation, topology change, and two-way contact between tools and materials while staying fast enough to drive online reinforcement learning. We present MG-CD-MPM, a tool-centered localized extension of CD-MPM. The implicit Ginzburg-Landau phase-field damage system is solved on a local patch by preconditioned conjugate gradients using a geometric-multigrid V-cycle as the preconditioner. The background MPM discretization remains uniform: only the damage solve is localized. Two-way rigid-tool coupling converts MPM contact impulses into forces and torques on the tool, exposing material resistance directly to the policy. The resulting Gym-like simulator covers soft solids, brittle materials, granular media, and viscoplastic or semi-fluid media within a unified per-particle constitutive layer. We demonstrate cutting, scooping, and shoveling in six scenes, combining scripted tool motions with PPO policies trained on two cutting tasks.

</details>

---
