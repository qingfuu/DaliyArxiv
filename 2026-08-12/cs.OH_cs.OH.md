# cs.OH | cs.OH | 2026-08-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Control_of_hybrid_wind-wave_energy_systems_using_reinforcement_learning|Control of hybrid wind-wave energy systems using reinforcement learning]]

![[assets/2608.10754_figure.png|800]]

- **arXiv**: [2608.10754](https://arxiv.org/abs/2608.10754)
- **PDF**: https://arxiv.org/pdf/2608.10754
- **详细分析**: [[20_Research/Papers/强化学习/Control_of_hybrid_wind-wave_energy_systems_using_reinforcement_learning|Control of hybrid wind-wave energy systems using reinforcement learning]]
- **作者**: Zechuan Lin, Kemeng Chen, Maosen Fan, Xiaofan Li, Xi Xiao, John V. Ringwood
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Control of hybrid wind-wave energy systems using reinforcement learning》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenFAST-WEC-Sim, WEC-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Integrating wave energy converters (WECs) with floating offshore wind turbines (FOWTs), to form hybrid wind-wave energy (HWWE) systems, is a promising approach to achieve further cost reduction for offshore renewable energy. In such systems, the control of the integrated WECs plays an important role, with the potential to generate additional wave energy while simultaneously suppressing floating platform motion. However, HWWE systems are characterized by complex dynamics, making accurate modelling only viable through numerical simulation, and posing significant challenges for control design. This paper proposes a reinforcement learning (RL) control framework for HWWE systems, in which the real-time control policy is learned directly through interactions with high-fidelity simulation. A numerical model is established for a HWWE system consisting of an IEA 15 MW wind turbine, a VolturnUS semi-submersible platform, and three torus-type WECs, which is then employed as the RL training environment. Control performance is evaluated in terms of both wave energy generation and platform motion reduction, two competing objectives, from a Pareto perspective. It is shown that the proposed RL controller achieves substantial Pareto improvements over conventional control strategies, e.g., over 75\% higher wave energy capture at the same platform motion level, or nearly 50\% lower motion at the same energy capture level, thereby significantly extending the attainable performance boundary of HWWE systems.

</details>

---
