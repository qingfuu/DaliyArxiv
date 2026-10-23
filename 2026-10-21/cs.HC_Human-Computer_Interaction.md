# cs.HC | Human-Computer Interaction | 2026-10-21

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/具身智能/Evaluating_Social_Reasoning_in_Embodied_Vision-Language_Models|Evaluating Social Reasoning in Embodied Vision-Language Models]]

![[assets/2610.27496_first_page.png|800]]

- **arXiv**: [2610.27496](https://arxiv.org/abs/2610.27496)
- **PDF**: https://arxiv.org/pdf/2610.27496
- **详细分析**: [[20_Research/Papers/具身智能/Evaluating_Social_Reasoning_in_Embodied_Vision-Language_Models|Evaluating Social Reasoning in Embodied Vision-Language Models]]
- **作者**: Daniel Weiner, Raj Korpan
- **cs 子类**: cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.2，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Evaluating Social Reasoning in Embodied Vision-Language Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HRIBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models now serve as reasoning layers for robot teams, but it remains unclear whether embodiment-specialized vision-language models (VLMs) preserve the social-reasoning capabilities of general-purpose VLMs. We evaluate Gemini Robotics-ER on SHREC, a benchmark of real human-robot social interactions, and compare it with published general-purpose VLM baselines. Robotics-ER outperforms GPT-4o-mini on error/competence detection but performs worse on detailed social-attribute judgments; adding a visual frame helps one task while hurting the other. These results suggest embodiment-specialized models may perform differently on social judgments that can be read more directly from observable interaction cues versus those requiring more inference about a person's internal state. Because the comparison spans model families, these differences cannot be attributed to embodiment specialization alone. This matters for multi-robot systems, where a shared foundation model could cause systematic social-perception errors to influence multiple coordination decisions. This work presents an initial evaluation, with broader cross-context and video-based analyses left for future work.

</details>

---
