# cs.SE | Software Engineering | 2026-07-31

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/机器人/A_Taxonomy_of_Human-Robot_Teamwork_Requirements|A Taxonomy of Human-Robot Teamwork Requirements]]

![[assets/2607.27302_figure.png|800]]

- **arXiv**: [2607.27302](https://arxiv.org/abs/2607.27302)
- **PDF**: https://arxiv.org/pdf/2607.27302
- **详细分析**: [[20_Research/Papers/机器人/A_Taxonomy_of_Human-Robot_Teamwork_Requirements|A Taxonomy of Human-Robot Teamwork Requirements]]
- **作者**: Anastasia Mavridou, Hazel M. Taylor, Sandy Lozito, Louise A. Dennis, Michael Fisher, Marie Farrell
- **cs 子类**: cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Taxonomy of Human-Robot Teamwork Requirements》归入 机器人 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems are increasingly deployed in safety- and mission-critical domains where humans and robots must operate as a team to complete complex tasks. Existing requirements for Human-Robot teamwork remain fragmented across disparate sources, with no unified framework that addresses complexities of collaborative Human-Robot tasks. We address this gap by presenting a taxonomy of Human-Robot Teamwork (HRT) requirements derived from analysis of (academic and industrial) literature, standards and regulatory guidance. We extracted a construction corpus of 361 requirements from 14 cross-domain sources. Through iterative classification and refinement, we develop a two-level hierarchical taxonomy comprising 6 high-level categories and 21 low-level subcategories that distinguish information provision, relational control, decision support, safety mechanisms, performance monitoring, and foundational system capabilities. We validate the taxonomy through expert evaluation with 5 domain specialists and a utility demonstration on an independently assembled corpus of 448 requirements drawn from 19 sources spanning six HRT domains.

</details>

---

### [[20_Research/Papers/大模型/AgentS4D_Benchmarking_Runtime_Risks_across_the_Execution_Lifecycle_of_LLM-Based_Workspace_Agents|AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents]]

![[assets/2607.27294_figure.png|800]]

- **arXiv**: [2607.27294](https://arxiv.org/abs/2607.27294)
- **PDF**: https://arxiv.org/pdf/2607.27294
- **详细分析**: [[20_Research/Papers/大模型/AgentS4D_Benchmarking_Runtime_Risks_across_the_Execution_Lifecycle_of_LLM-Based_Workspace_Agents|AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents]]
- **作者**: Jiajun Zhou, Zhaoxuan Ke, Jihang Ye, Xuanze Chen, Shanqing Yu, Qi Xuan
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《AgentS4D: Benchmarking Runtime Risks across the Execution Lifecycle of LLM-Based Workspace Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ATBench, SkillSafetyBench, URL, Workspace-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based workspace agents execute stateful, multi-step workflows across heterogeneous resources, external tools, and persistent state. Their safety must therefore be assessed from actions, side effects, and state changes throughout execution. Although recent benchmarks have advanced executable safety testing and trajectory-aware verification, they rarely provide a unified account of where risks enter, how they elicit unsafe behavior, which harms they target, and where supporting evidence appears during execution. We introduce AgentS4D, a sandboxed benchmark for lifecycle-wide runtime safety evaluation. Its four-dimensional runtime-safety framework uses six risk-entry sources, six induction strategies, and nine target harms to guide case construction, while seven lifecycle checkpoints organize post-run evidence. AgentS4D contains 328 risk-injected cases. We evaluate all 20 combinations of four harnesses (Hermes, OpenClaw, Claude Code, and Codex) and five LLM backends (GPT-5.5, Gemini 3.1 Pro, DeepSeek-V4-Pro, MiniMax-M3, and Qwen3.7-Plus) on these cases, yielding 6,560 runs. Overall, 4,461 runs (68.0%) trigger prespecified unsafe signals. Across the 20 configurations, the observed safety of an agent system varies with both its harness-LLM pairing and how risk is introduced. Agent systems exhibit markedly different safety behavior when the same induction strategy reaches them through different risk carriers. They also respond differently to the same target harm when it is realized through different carriers and strategies. Moreover, 4,344 runs (66.22% overall) are unsafe yet complete. Thus, task completion cannot establish runtime safety, and testing only one form of a risk can conceal important weaknesses. Evaluations should examine complete agent configurations across diverse risk conditions and retain evidence throughout execution.

</details>

---
