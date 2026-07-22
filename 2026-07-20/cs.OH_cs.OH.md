# cs.OH | cs.OH | 2026-07-20

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/强化学习/Co-Design_of_Aeroelastic_Systems_with_Deep_Reinforcement_Learning|Co-Design of Aeroelastic Systems with Deep Reinforcement Learning]]

![[assets/2607.15329_figure.png|800]]

- **arXiv**: [2607.15329](https://arxiv.org/abs/2607.15329)
- **PDF**: https://arxiv.org/pdf/2607.15329
- **详细分析**: [[20_Research/Papers/强化学习/Co-Design_of_Aeroelastic_Systems_with_Deep_Reinforcement_Learning|Co-Design of Aeroelastic Systems with Deep Reinforcement Learning]]
- **作者**: Yao Cheng Li, Urban Fasel
- **cs 子类**: 
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.6（加权：强化学习 1.6）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Co-Design of Aeroelastic Systems with Deep Reinforcement Learning》归入 强化学习 方向。该论文围绕 cs.OH 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Control co-design considers the physical system and its controller together, enabling the strong coupling between system design and control to be uncovered and exploited. This is especially relevant in aeroelastic flight systems, where structural, aerodynamic, and control design choices jointly determine manoeuvrability and efficiency. This paper presents a model-free nested co-design framework for aeroelastic systems using deep reinforcement learning, in which a design-conditioned control policy is trained with proximal policy optimisation while an outer loop updates a distribution over candidate design parameters. The approach is evaluated on three case studies of increasing complexity: a spring-mass-damper system, a pitch-plunge-flap aerofoil, and a highly flexible high-aspect-ratio glider performing a thermal-soaring mission in a stochastic environment. Across these case studies, the framework is shown to progressively concentrate the design search towards high-performing regions and to outperform policies trained on randomly sampled designs. The results also show that reward shaping plays an important role in enabling stable learning in partially observed and stochastic environments. In the final glider case, the method jointly addresses wing design, flight control, and mission-level behaviour in the presence of aeroelastic coupling and atmospheric uncertainty. These results highlight the potential of model-free co-design for complex aeroelastic systems in which design, control, and mission objectives are tightly coupled.

</details>

---
