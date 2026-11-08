# cs.SE | Software Engineering | 2026-11-06

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/A_Multi-Modal_Robotic_Framework_for_Physical_GUI_Interaction_Testing|A Multi-Modal Robotic Framework for Physical GUI Interaction Testing]]

![[assets/2611.06939_figure.png|800]]

- **arXiv**: [2611.06939](https://arxiv.org/abs/2611.06939)
- **PDF**: https://arxiv.org/pdf/2611.06939
- **详细分析**: [[20_Research/Papers/大模型/A_Multi-Modal_Robotic_Framework_for_Physical_GUI_Interaction_Testing|A Multi-Modal Robotic Framework for Physical GUI Interaction Testing]]
- **作者**: Davi Freitas
- **cs 子类**: cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，机器人 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《A Multi-Modal Robotic Framework for Physical GUI Interaction Testing》归入 机器人、大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated testing of mobile applications remains challenging when realistic user interactions must be reproduced and GUI behavior verified without relying on invasive mechanisms such as instrumentation or ADB-level control. Existing approaches, including DLD and R-DLD, detect data loss triggered by activity restarts but still depend on system-level access, which limits their applicability on real devices. This doctoral research proposes RFNIT, a multi-modal, fully non-invasive robotic framework for physical GUI interaction testing on smartphones. RFNIT supports end-to-end automation by perceiving the device state through external sensing and executing physical interactions, enabling human-like actions while preserving reproducibility and execution accuracy. The framework integrates a vision-based perception module, an LLM-driven reasoning agent, and a robotic actuator capable of performing touch, swipe, and typing gestures. Multimodal data, including external camera images and OCR-extracted text, are combined to identify GUI elements and guide subsequent testing decisions. Preliminary results indicate that RFNIT accurately recognizes buttons, text fields, and virtual keyboards from external camera input, achieving over 85\% visual detection accuracy. Ongoing and future work will focus on improving robustness, repeatability, and coverage of GUI states during long-running testing sessions.

</details>

---
