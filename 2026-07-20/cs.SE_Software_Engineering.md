# cs.SE | Software Engineering | 2026-07-20

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/大模型/DiffTestGen_Change-Directed_LLM-Based_Testing_for_Exposing_Behavioral_Differences|DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences]]

![[assets/2607.16024_figure.png|800]]

- **arXiv**: [2607.16024](https://arxiv.org/abs/2607.16024)
- **PDF**: https://arxiv.org/pdf/2607.16024
- **详细分析**: [[20_Research/Papers/大模型/DiffTestGen_Change-Directed_LLM-Based_Testing_for_Exposing_Behavioral_Differences|DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences]]
- **作者**: Huimin Hu, Cristian Cadar, Michael Pradel
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.4（加权：大模型 0.4）
- **关联关键词**: LLM

#### 研究背景与动机

《DiffTestGen: Change-Directed LLM-Based Testing for Exposing Behavioral Differences》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：StrSequenceOrSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As software evolves over time, it is important to ensure that any behavioral changes occur as intended by developers. A promising approach for this goal is to generate tests that expose behavioral differences between the old and new versions of a program. However, current approaches fail to trigger behavioral differences for many code changes. This paper presents~DiffTestGen, a novel change-directed, LLM-based differential testing approach specifically designed to expose behavioral differences introduced by a code change. The approach is enabled by two key contributions: First, DiffTestGen leverages static call graph analysis and project documentation to identify valid entry points for test generation and to guide the LLM toward reaching the changed code. Second, DiffTestGen iteratively improves our newly introduced union coverage metric, which combines coverage of modified code in the old and the new version, by providing targeted coverage feedback to the LLM. We evaluate DiffTestGen on two datasets comprising a total of 463 PRs. DiffTestGen exposes behavioral differences in 78.2% of the PRs while achieving an average union coverage of 90.7%. Compared with the baselines, DiffTestGen exposes 99 more PRs overall and increases code coverage by 12.5% and 15.6% percentage points, respectively. By integrating DiffTestGen with the Testora regression detector, we show that the identified behavioral differences can be used to detect regression bugs missed by the best existing approaches.

</details>

---

### [[20_Research/Papers/大模型/TARS_A_Theory-of-Mind_Agent_for_Personalized_In-IDE_Code_Comprehension|TARS: A Theory-of-Mind Agent for Personalized In-IDE Code Comprehension]]

![[assets/2607.15948_figure.png|800]]

- **arXiv**: [2607.15948](https://arxiv.org/abs/2607.15948)
- **PDF**: https://arxiv.org/pdf/2607.15948
- **详细分析**: [[20_Research/Papers/大模型/TARS_A_Theory-of-Mind_Agent_for_Personalized_In-IDE_Code_Comprehension|TARS: A Theory-of-Mind Agent for Personalized In-IDE Code Comprehension]]
- **作者**: Leopoldo Todisco, Antonio Della Porta, Stefano Lambiase, Fabio Palomba
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TARS: A Theory-of-Mind Agent for Personalized In-IDE Code Comprehension》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CodeSearchNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Code comprehension is one of the most time-consuming tasks in software engineering, yet most LLM-based assistants produce explanations that ignore who is asking and force developers into a disruptive copy-paste workflow. We present TARS, an LLM-powered agent integrated into Visual Studio Code that supports program comprehension through autonomous explanations anchored directly to the code under analysis. Built around a lightweight Theory of Mind paradigm, TARS profiles a developer's expertise, role, and stylistic preferences, then adapts the depth and tone of its explanations accordingly, grounding them in project documentation via Retrieval-Augmented Generation. To evaluate TARS, we conducted a controlled experiment with 18 participants on non-trivial Java snippets. Participants using TARS completed tasks 26\% faster, reported lower cognitive load, and found the explanations meaningfully adapted to their profiles.

</details>

---

### [[20_Research/Papers/大模型/Verified_LLM-Driven_Synthesis_for_Concept_Design|Verified LLM-Driven Synthesis for Concept Design]]

![[assets/2607.15718_first_page.png|800]]

- **arXiv**: [2607.15718](https://arxiv.org/abs/2607.15718)
- **PDF**: https://arxiv.org/pdf/2607.15718
- **详细分析**: [[20_Research/Papers/大模型/Verified_LLM-Driven_Synthesis_for_Concept_Design|Verified LLM-Driven Synthesis for Concept Design]]
- **作者**: Alcino Cunha
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM

#### 研究背景与动机

《Verified LLM-Driven Synthesis for Concept Design》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Concept Design structures software systems around concepts: user-facing, self-contained units of functionality with a focused purpose. Concepts are composed into applications using synchronization rules called reactions, which specify how actions in one concept trigger actions in others. This paper first gives a formal semantics for concepts and reactions, enabling automatic verification of safety invariants in applications developed with this methodology. It then presents a CEGIS-style, LLM-driven synthesis procedure for generating reaction designs that satisfy such invariants. Because many different designs can satisfy the same invariant, we study two ways of steering synthesis toward the user's intended design: natural-language prompts and positive/negative scenarios. We also propose an LLM-driven scenario elicitation technique to support early design exploration. In an evaluation on three applications and twelve design variants using one LLM configuration, invariant-only synthesis reached verified designs quickly but often produced inconsistent designs across runs, some of which were implausible, showing that invariants alone underconstrain the design task. Scenario-guided synthesis recovered intended designs more consistently than natural-language prompting, although minimal scenarios can lead to overfitting. LLM-driven scenario elicitation, where the user classifies proposed scenarios rather than authoring them from scratch, recovered the intended designs in most variants when enough scenarios were elicited, but missed behaviors and non-determinism prevented reliable coverage in all cases.

</details>

---

### [[20_Research/Papers/大模型/Understanding_Agent-Reactive_Bugs_at_the_Model-Harness_Boundary_An_Empirical_Study_of_LLM_Agent_Issue_Reports|Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports]]

![[assets/2607.15684_figure.png|800]]

- **arXiv**: [2607.15684](https://arxiv.org/abs/2607.15684)
- **PDF**: https://arxiv.org/pdf/2607.15684
- **详细分析**: [[20_Research/Papers/大模型/Understanding_Agent-Reactive_Bugs_at_the_Model-Harness_Boundary_An_Empirical_Study_of_LLM_Agent_Issue_Reports|Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports]]
- **作者**: Jingyi Chen, Songqiang Chen, Hengcheng Zhu, Jialun Cao, Jiasi Shen, Shing-Chi Cheung
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Understanding Agent-Reactive Bugs at the Model-Harness Boundary: An Empirical Study of LLM Agent Issue Reports》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents span command-line interfaces (e.g., Codex) and agent frameworks (e.g., LangChain), integrating backend LLMs with harness code that parses model outputs, controls agent loops, and manages context. Both the harness and LLM-generated responses jointly shape an agent's execution. This architecture gives rise to bugs that cannot be readily understood by inspecting either component alone, because some bugs occur only when a particular LLM response elicits an abnormal reaction from the agent. Prior empirical studies of agent bugs have largely attributed failures either to limited model capabilities or to harness-side defects, such as outdated APIs and configuration misalignment, without characterizing these AR bugs. We conduct the first empirical study focused on agent-reactive (AR) bugs. Through manual analysis of 255 bug reports from Codex, Gemini-CLI, LangChain, and CrewAI, we construct a two-axis taxonomy covering observable symptoms and the LLM behaviors that trigger them. Our findings show that many AR bugs manifest as silent errors without well-defined test oracles, which makes detection difficult. The stochasticity of LLM responses further complicates bug reproduction. We additionally examine fixes proposed by users and implemented by developers. This analysis exposes a mismatch: users frequently advocate harness-side guardrails, whereas developers may attribute the issue to the LLM or respond slowly to user-proposed fixes. These findings point to the need for mechanisms that help users and developers understand the root causes and resolutions of AR bugs. Overall, the study highlights challenges specific to LLM agents and motivates the design of test oracles, reproduction support, and fault-localization techniques for AR bugs.

</details>

---
