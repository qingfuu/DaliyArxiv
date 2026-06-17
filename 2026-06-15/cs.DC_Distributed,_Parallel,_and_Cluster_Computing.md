# cs.DC | Distributed, Parallel, and Cluster Computing | 2026-06-15

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Selective_Field_Transmission_Bandwidth_Efficient_Communication_under_Standardized_Message_Schemas|Selective Field Transmission: Bandwidth Efficient Communication under Standardized Message Schemas]]

![[assets/2606.14228_figure.png|800]]

- **arXiv**: [2606.14228](https://arxiv.org/abs/2606.14228)
- **PDF**: https://arxiv.org/pdf/2606.14228
- **详细分析**: [[20_Research/Papers/机器人/Selective_Field_Transmission_Bandwidth_Efficient_Communication_under_Standardized_Message_Schemas|Selective Field Transmission: Bandwidth Efficient Communication under Standardized Message Schemas]]
- **作者**: David Philipp Klüner, David Murach, Stefan Kowalewski, Alexandru Kampmann
- **cs 子类**: cs.DC, cs.NI
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.6（加权：机器人 0.6）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Selective Field Transmission: Bandwidth Efficient Communication under Standardized Message Schemas》归入 机器人 方向。该论文围绕 Distributed, Parallel, and Cluster Computing 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we introduce and evaluate Selective Field Transmission (SFT), a middleware mechanism that decouples transmission content from statically defined message types in publish-subscribe systems. Industrial and robotics developers often face a dilemma: They can follow established best practices and use standard message types, such as in the Robot Operating System 2 (ROS 2) and COVESA projects, to benefit from reusable and interoperable interfaces, or they can introduce proprietary, project-specific message types tailored to receiver requirements to reduce bandwidth. SFT resolves this trade-off by dynamically adapting the transmitted message components to each receivers actual needs while preserving unmodified standard interfaces. Receivers declare or automatically derive the required message components, which are communicated to the publisher. The publisher then serializes and transmits only the required component subset per receiver with minimal developer intervention. Our evaluation shows that SFT achieves significant bandwidth reductions without measurable per-message latency overhead, with savings proportional to the number and size of unused fields.

</details>

---
