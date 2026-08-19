# cs.CR | Cryptography and Security | 2026-08-17

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/MazeRunner_Nonlinear_Task_and_Clue_Orchestration_for_LLM-driven_Black-Box_Automated_Penetration_Testing|MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing]]

![[assets/2608.14216_first_page.png|800]]

- **arXiv**: [2608.14216](https://arxiv.org/abs/2608.14216)
- **PDF**: https://arxiv.org/pdf/2608.14216
- **详细分析**: [[20_Research/Papers/大模型/MazeRunner_Nonlinear_Task_and_Clue_Orchestration_for_LLM-driven_Black-Box_Automated_Penetration_Testing|MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing]]
- **作者**: Zhenyuan Li, Yi Jiang, Junjie Cheng, Yaokun Li, Jing Qiu, Shouling Ji
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《MazeRunner: Nonlinear Task and Clue Orchestration for LLM-driven Black-Box Automated Penetration Testing》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Penetration testing is essential yet resource-intensive. Although large language models (LLMs) show promise for automating security auditing, existing agents mainly execute end-to-end workflows in simplified linear scenarios. Real-world black-box testing is fundamentally nonlinear: the attack graph is initially unknown and must be incrementally inferred from environmental feedback. Observations may reveal multiple attack branches, failures are often ambiguous, and critical clues may span long action horizons. Existing agents therefore tend to become trapped in depth-first exploration, misdiagnose failures, and forget prior evidence. We present MazeRunner, an autonomous penetration testing system built on a three-agent task-and-clue orchestration framework. It separates global orchestration, context-intensive execution, and failure-oriented review while persistently maintaining task states and environmental evidence. This design supports action revision, prerequisite recovery, branch switching, and long-range clue correlation. We evaluate MazeRunner on 10 recently released HTB targets, limiting each system-target run to 20 million LLM tokens and preventing target-specific solution leakage. With Claude Sonnet 4.5, MazeRunner completes 47.7% of annotated subtasks, compared with 36.2% for PentestGPT-V2 and 34.2% for Claude Code. It achieves user-level or higher access on six targets, including root access on two; each same-model baseline reaches user-level access on only two targets and never obtains root access. Execution-trace analysis further shows that MazeRunner explores more attack branches and acquires shells more efficiently.

</details>

---
