# cs.IT | Information Theory | 2026-07-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Communicative_Efficiency_of_Single_vs._Multi-Axis_Robot_Neck_Motion|Communicative Efficiency of Single vs. Multi-Axis Robot Neck Motion]]

![[assets/2607.07390_figure.jpg|800]]

- **arXiv**: [2607.07390](https://arxiv.org/abs/2607.07390)
- **PDF**: https://arxiv.org/pdf/2607.07390
- **详细分析**: [[20_Research/Papers/机器人/Communicative_Efficiency_of_Single_vs._Multi-Axis_Robot_Neck_Motion|Communicative Efficiency of Single vs. Multi-Axis Robot Neck Motion]]
- **作者**: Chapa Sirithunge, Haewon Jeong, Qinghua Guan, Fumiya Iida, Josie Hughes
- **cs 子类**: cs.IT, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Communicative Efficiency of Single vs. Multi-Axis Robot Neck Motion》归入 机器人、具身智能 方向。该论文围绕 Information Theory 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Nonverbal communication through head and neck movement is fundamental to human social signalling, yet how robotic neck morphology translates motion into communicative information remains poorly understood. We present an information-theoretic framework characterising robot neck movement as a communication channel, quantifying information transmitted and energy expended across varied configurations. Using a robotic neck platform, we recorded 84 video stimuli spanning three rotational degrees of freedom (DoF), varying amplitude, acceleration, and frequency, measuring Shannon entropy of pixel-change signals alongside energy consumption. A perceptual study validated communicative interpretations of each motion. While humans typically engage one axis per gesture, robots are unconstrained by biological architecture, motivating tests up to 3 DoF. Yet communicative information peaks at two DoF and decreases at three despite rising energy cost, a phenomenon we term the morphological information bottleneck. Motion parameter effects were parameter-dependent, some additive, others non-linear. We introduce the Motor Information Space, a framework mapping entropy against energy to expose communicative efficiency across morphologies, in which the optimal configuration achieves 5.26 bits at competitive energy cost. Perception data further confirm multi-axis movements reduce clarity. These findings challenge the assumption that anatomical completeness improves robotic expressiveness, establishing a quantitative basis for morphological design in robots, especially humanoids.

</details>

---
