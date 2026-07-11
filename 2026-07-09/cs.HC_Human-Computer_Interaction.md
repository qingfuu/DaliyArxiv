# cs.HC | Human-Computer Interaction | 2026-07-09

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Initiation_Safety_A_Missing_Dimension_in_Generalist-Robot_Safety|Initiation Safety: A Missing Dimension in Generalist-Robot Safety]]

![[assets/2607.07420_figure.png|800]]

- **arXiv**: [2607.07420](https://arxiv.org/abs/2607.07420)
- **PDF**: https://arxiv.org/pdf/2607.07420
- **详细分析**: [[20_Research/Papers/具身智能/Initiation_Safety_A_Missing_Dimension_in_Generalist-Robot_Safety|Initiation Safety: A Missing Dimension in Generalist-Robot Safety]]
- **作者**: Zhijin Meng, Francisco Cruz
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Initiation Safety: A Missing Dimension in Generalist-Robot Safety》归入 机器人、具身智能 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety for generalist robots is usually discussed in terms of motion or dialogue. We argue a third question is missing: should the robot take its first hard-to-undo social action at all, such as a greeting, an uninvited grasp, or stepping into someone's space? We call this initiation authorization. Current frameworks rarely treat it as a separate safety layer. Today's stacks often skip this step: a high engagement score or a confident VLA rollout is treated as permission to act. But seeing a person is not the same as having their consent to be addressed. We frame initiation authorization within generalist-robot safety and contrast it with post-plan VLA guardrails, implementing PAS (probe-authorize-speak) on a doorway humanoid, comparing it with direct-init on logged traces, and proposing a three-condition user study, with open questions on metrics, governance, and where initiation ends and foundation-model generation begins.

</details>

---
