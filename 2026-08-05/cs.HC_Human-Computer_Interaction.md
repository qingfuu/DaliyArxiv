# cs.HC | Human-Computer Interaction | 2026-08-05

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Semantic_Haptic_Feedback_Enhances_Dexterous_Robotic_Teleoperation|Semantic Haptic Feedback Enhances Dexterous Robotic Teleoperation]]

![[assets/2608.02780_figure.png|800]]

- **arXiv**: [2608.02780](https://arxiv.org/abs/2608.02780)
- **PDF**: https://arxiv.org/pdf/2608.02780
- **详细分析**: [[20_Research/Papers/机器人/Semantic_Haptic_Feedback_Enhances_Dexterous_Robotic_Teleoperation|Semantic Haptic Feedback Enhances Dexterous Robotic Teleoperation]]
- **作者**: Bingjian Huang, Sahar Aseeri, Jonas Schmidtler, Joseph Zhang, Sonny Chan, Andrew Doxon, Jom Preechayasomboon, Evan Pezent, Alberto Rigo, Amir Memar, Nicholas Colonnese, Chase Tymms
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Semantic Haptic Feedback Enhances Dexterous Robotic Teleoperation》归入 具身智能、机器人 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robot teleoperation, haptic feedback can be used to help human operators accomplish dexterous manipulation tasks. However, existing haptic feedback methods try to replicate high-fidelity sensory haptics that are felt in real world interactions, which are constrained by the sensing and feedback hardware capability and may lead to higher workload. To addresses these limitations, this work introduces semantic haptics for teleoperation, which uses abstract haptic patterns to convey critical information about robot states. We categorize robot states into "Confirmations" and "Exceptions", implement a modular haptic rendering pipeline in robot simulation, and deliver semantic haptic feedback to operators through pneumatic and vibrotactile wristbands. This simplifies hardware requirements and enables one-to-many mappings between haptic patterns and robot states. Through three evaluation studies, we identify the most effective semantic haptic design for a common pick and place teleoperation task and compare semantic haptics to other teleoperation feedback approaches including sensory haptics and visual feedback. Results suggest that while semantic haptics performs similarly as other feedback in unimanual tasks, it achieves superior performance in bimanual tasks, with reduced task workload, increased situational awareness, and overall preference.

</details>

---
