# cs.HC | Human-Computer Interaction | 2026-06-23

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/机器人/Toward_Machine_Risk_Perception_Integrating_Trust_Calibration_and_Precursor-Based_Risk_Estimation_for_Humanoid|Toward Machine Risk Perception: Integrating Trust Calibration and Precursor-Based Risk Estimation for Humanoid]]

![[assets/2606.20748_first_page.png|800]]

- **arXiv**: [2606.20748](https://arxiv.org/abs/2606.20748)
- **PDF**: https://arxiv.org/pdf/2606.20748
- **详细分析**: [[20_Research/Papers/机器人/Toward_Machine_Risk_Perception_Integrating_Trust_Calibration_and_Precursor-Based_Risk_Estimation_for_Humanoid|Toward Machine Risk Perception: Integrating Trust Calibration and Precursor-Based Risk Estimation for Humanoid]]
- **作者**: He Wen
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Toward Machine Risk Perception: Integrating Trust Calibration and Precursor-Based Risk Estimation for Humanoid》归入 具身智能、机器人 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Human-Computer Interaction 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots are emerging as co-workers in smart manufacturing, yet their dynamic, human-like movements introduce safety risks that differ fundamentally from those of fixed or wheeled robots. Conventional safety paradigms based on reactive force or distance limits fail to capture the sequential, uncertain nature of humanoid failures. This study proposes a precursor-driven, trust-calibrated framework to enable proactive humanoid risk perception. Accident evolution is modeled through sequential precursor cues using a Logistic-Exponential (LE) formulation that couples logistic escalation from diverse precursors with exponential decay for temporal dissipation. Trust is defined as the inverse of the estimated accident probability, allowing humanoids to adapt behavior in real time, reducing aggressiveness when risk intensifies, and restoring confidence as stability returns. A multi-source dataset of 126 documented events and 241 precursors revealed twelve dominant accident modes, most evolving through overlapping cues within one second. A simulated case study ("fall-onto-human") demonstrated how the LE-Trust coupling can trigger early intervention and prevent collapse. The results advance humanoid safety from static thresholds toward dynamic, evidence-based inference, establishing a foundation for risk-aware and trustworthy human-robot collaboration in Industry 5.0 environments.

</details>

---
