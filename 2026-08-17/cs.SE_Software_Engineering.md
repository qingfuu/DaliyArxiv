# cs.SE | Software Engineering | 2026-08-17

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/LegacyWorld_Atomicity-Aware_Evaluation_of_GUI_Agents_for_Legacy_Workflows|LegacyWorld: Atomicity-Aware Evaluation of GUI Agents for Legacy Workflows]]

![[assets/2608.14131_figure.png|800]]

- **arXiv**: [2608.14131](https://arxiv.org/abs/2608.14131)
- **PDF**: https://arxiv.org/pdf/2608.14131
- **详细分析**: [[20_Research/Papers/大模型/LegacyWorld_Atomicity-Aware_Evaluation_of_GUI_Agents_for_Legacy_Workflows|LegacyWorld: Atomicity-Aware Evaluation of GUI Agents for Legacy Workflows]]
- **作者**: Thilo Reintjes, Sivajeet Chand, Derui Zhu, Sushant Kumar Pandey, Alexander Pretschner
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《LegacyWorld: Atomicity-Aware Evaluation of GUI Agents for Legacy Workflows》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LegacyWorld, OSWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legacy and legacy-like enterprise systems often remain difficult to modernize because critical workflows expose limited programmable interfaces and still require manual GUI interaction. This paper reports a pre-deployment evaluation study motivated by the development of legacy-use, an industry-oriented framework for automating such workflows with multimodal LLM agents. During framework development, domain experts helped identify stateful workflows where successful demos are not sufficient: a failed agent run may still leave persistent invalid changes in business or healthcare records. We therefore evaluate computer-use agents using atomicity: a run should either complete the intended workflow correctly or fail without unintended persistent side effects. We construct a domain-expert-informed benchmark of 28 Windows GUI workflows, each specified with an initial state, goal state, and task-specific validator. We compare expert-crafted prompts with prompts generated from screen recordings of expert golden-path executions. Across six hosted computer-use agents, our results show that useful completion, safe failure, and non-atomic side effects are distinct operational profiles. We conclude that workflow capture, state validators, and atomicity-aware acceptance tests should be first-class requirements for AI-based legacy workflow automation.

</details>

---
