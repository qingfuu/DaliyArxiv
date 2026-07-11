# cs.SE | Software Engineering | 2026-07-09

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/What_Makes_a_Good_Bug_Report_for_an_AI_Agent|What Makes a Good Bug Report for an AI Agent?]]

![[assets/2607.07593_first_page.png|800]]

- **arXiv**: [2607.07593](https://arxiv.org/abs/2607.07593)
- **PDF**: https://arxiv.org/pdf/2607.07593
- **详细分析**: [[20_Research/Papers/大模型/What_Makes_a_Good_Bug_Report_for_an_AI_Agent|What Makes a Good Bug Report for an AI Agent?]]
- **作者**: Lara Khatib, Noble Saji Mathews, Meiyappan Nagappan, Pengyu Nie, Thomas Zimmermann
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《What Makes a Good Bug Report for an AI Agent?》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated program repair (APR) agents are transitioning from research benchmarks to developer workflows, yet they still begin with bug reports written for human developers. While decades of research have established what makes a good bug report for humans (e.g., steps to reproduce, stack traces), it remains unclear whether these features transfer to LLM-based agents. We study this question in two analyses. First, we use statistical modeling to examine associations between 27 bug-report features and repair success across 433 SWE-bench Verified issues attempted by 87 repair agents. We find that fix suggestions, reproduction scripts, repository source code, and localization info are associated with higher resolution likelihood, while longer reports are associated with lower odds. Second, we conduct controlled ablations across 2 models and 17 problem-statement mutations on SWE-bench Pro, varying the information available to an agent while holding the underlying task fixed. We remove or isolate selected bug-report content, delete fault-localization cues, and test structural changes that flatten lists or remove section headers. We find that both models depend on localization cues and expected behavior, and that structural changes alone can reduce solve rates, even without removing any content. The two models diverge in how they handle missing information: Qwen searches more widely and can exhaust its turn budget, while Gemma commits to a plausible interpretation early and patches on it. Our findings indicate that a good bug report for an agent overlaps with, but is not identical to, a good report for a human: agents benefit most from concrete, executable, and well-localized information, whereas some qualities long emphasized for human readers, such as natural language steps to reproduce and readable descriptions, contribute little or even correlate with lower success.

</details>

---

### [[20_Research/Papers/大模型/Mining_Workflow_Graphs_for_Black-Box_Boundary_Testing_of_Conversational_LLM_Agents|Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents]]

![[assets/2607.06873_figure.png|800]]

- **arXiv**: [2607.06873](https://arxiv.org/abs/2607.06873)
- **PDF**: https://arxiv.org/pdf/2607.06873
- **详细分析**: [[20_Research/Papers/大模型/Mining_Workflow_Graphs_for_Black-Box_Boundary_Testing_of_Conversational_LLM_Agents|Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents]]
- **作者**: Liting Lin, Boxi Yu, Yuzhong Zhang, Lionel Briand, David-Paul Niland, Emir Muñoz
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Mining Workflow Graphs for Black-Box Boundary Testing of Conversational LLM Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentEval, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conversational LLM agents can cause real-world harm when their internal workflows fail, such as completing a transaction without confirmation. Testing these state-dependent failures is difficult because critical boundaries, such as identity checks and confirmation gates, are hidden behind multi-turn conversational prerequisites, rendering them inaccessible to standard tests. We present AgentEval, a black-box testing framework that discovers and stresses these stateful boundaries. AgentEval interacts with an agent to mine a \emph{conversational workflow graph}, a model of its behavior. Instead of prompting blindly, AgentEval uses this graph's structure to enumerate specific guards and prerequisites as test targets, replaying the conversational path to a boundary before applying a perturbation. AgentEval then executes each test, determining whether it passes or fails using only the conversation turns. We benchmark AgentEval against a privileged, white-box auditor with access to the agent's underlying source code, which AgentEval never sees. On four $τ^3$-bench agents, AgentEval successfully generates tests covering $23$--$38$ distinct boundaries per agent; ablation studies attribute the gain to the graph's structure: $23$ distinct boundaries versus $12$ with a prompt-only baseline, at lower duplicate and false-alarm rates.

</details>

---
