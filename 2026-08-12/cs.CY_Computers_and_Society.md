# cs.CY | Computers and Society | 2026-08-12

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/When_the_Interviewer_Is_a_Bot_Behavior,_Breakdowns,_and_Trust_in_MLLM-Led_Interviews|When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews]]

![[assets/2608.10412_figure.jpg|800]]

- **arXiv**: [2608.10412](https://arxiv.org/abs/2608.10412)
- **PDF**: https://arxiv.org/pdf/2608.10412
- **详细分析**: [[20_Research/Papers/大模型/When_the_Interviewer_Is_a_Bot_Behavior,_Breakdowns,_and_Trust_in_MLLM-Led_Interviews|When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews]]
- **作者**: He Zhang, Kambinachi Chukwuma, ChanMin Kim, John M. Carroll
- **cs 子类**: cs.CY, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, Systems

#### 研究背景与动机

《When the Interviewer Is a Bot: Behavior, Breakdowns, and Trust in MLLM-Led Interviews》归入 大模型 方向。该论文围绕 Computers and Society 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Semi-structured interviews are a cornerstone of qualitative research but remain labor-intensive. We report an empirical study of what actually happens when the interviewer is an off-the-shelf real-time multimodal LLM (MLLM). We built InterviewBot, a voice-based interviewing system that wraps a real-time MLLM with a researcher-authored outline, and deployed it not as a novel architecture but as a research instrument for observing default MLLM interviewing behavior. In a practice study (N=15), participants completed a bot-led semi-structured interview and then a human-led reflection session about that experience. We contribute (i) a turn-level behavioral analysis of an MLLM interviewer (N_turns=428) showing that it is acknowledgment-heavy but probe-light (deepening probes account for 4.9% of all turns), and that 28.7% of question-bearing turns pack multiple questions into one turn despite an explicit one-question-at-a-time instruction; (ii) an inductive catalogue of four data-collection breakdowns (information loss, premature termination, latency, and interruption) observed in a deployed rather than simulated system; and (iii) three social dynamics from participants' reflections: disclosure calibration, where reduced social pressure coincided with shallower elaboration; institutional legitimacy, where trust tracked perceived stakes and what delegation to AI signaled about the organizer rather than conversational competence; and conversational grounding, where content-grounded paraphrase, not generic social filler, was what participants read as listening. We conclude with design implications for depth control, transparent handoffs, and non-templated listening mechanisms in human-centered interview automation.

</details>

---
