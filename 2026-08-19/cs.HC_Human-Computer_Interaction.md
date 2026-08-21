# cs.HC | Human-Computer Interaction | 2026-08-19

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/LadderTeam_Dual-Agent_Laddering_Elicitation_Framework|LadderTeam: Dual-Agent Laddering Elicitation Framework]]

![[assets/2608.17029_figure.png|800]]

- **arXiv**: [2608.17029](https://arxiv.org/abs/2608.17029)
- **PDF**: https://arxiv.org/pdf/2608.17029
- **详细分析**: [[20_Research/Papers/大模型/LadderTeam_Dual-Agent_Laddering_Elicitation_Framework|LadderTeam: Dual-Agent Laddering Elicitation Framework]]
- **作者**: Manjushree Aithal, Alexander Kotz, James Mitchell
- **cs 子类**: cs.HC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LadderTeam: Dual-Agent Laddering Elicitation Framework》归入 大模型 方向。该论文围绕 Human-Computer Interaction 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Eliciting detailed and actionable software requirements from end-users is a critical phase in the iterative development of a software product or application. To ensure the feedback collected is detailed and actionable, software teams can leverage the laddering interview technique. While effective for ensuring granular and actionable items from the software feedback, these interviews are subject to several limitations. They are traditionally a manual process associated with a time and financial burden, limiting scalability; interviewers must balance probing for depth while managing interviewee behavioral and cultural constraints. To address these limitations, we present \textbf{LadderTeam}, an open, reproducible framework that automates UX wireframe interviews using a dual-agent Large Language Model (LLM) architecture. An active interviewer agent executes one of three probing strategies (ACV, 5-Whys, and JTBD) to elicit actionable software requirements from usability feedback comments, while a concurrent background Judge agent evaluates probe-response pairs and triggers real-time guardrails to prevent topic drift. To rigorously evaluate LLM laddering without participant variance confounds, we introduce a controlled simulation methodology utilizing scripted ground-truth transcripts to isolate probe quality as the sole experimental variable. Across 216 interviews, \textbf{LadderTeam} achieved 99.1\% chain convergence and an 81.0\% ground-truth actionable response match (86.1\% reluctant personality, 75.9\% terse personality) with zero drift across all runs. All evaluation code, all transcripts, inputs, and a live demonstration platform will be open-sourced upon acceptance.

</details>

---
