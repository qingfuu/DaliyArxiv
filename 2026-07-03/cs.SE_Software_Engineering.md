# cs.SE | Software Engineering | 2026-07-03

#arxiv #ComputerScience

**论文数**: 1

### [[20_Research/Papers/大模型/When_Agents_Do_Not_Stop_Uncovering_Infinite_Agentic_Loops_in_LLM_Agents|When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents]]

![[assets/2607.01641_figure.png|800]]

- **arXiv**: [2607.01641](https://arxiv.org/abs/2607.01641)
- **PDF**: https://arxiv.org/pdf/2607.01641
- **详细分析**: [[20_Research/Papers/大模型/When_Agents_Do_Not_Stop_Uncovering_Infinite_Agentic_Loops_in_LLM_Agents|When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents]]
- **作者**: Xinyi Hou, Shenao Wang, Yanjie Zhao, Haoyu Wang
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Agents Do Not Stop: Uncovering Infinite Agentic Loops in LLM Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on iterative execution to solve tasks through planning, tool use, state updates, and agent collaboration. While this design enables flexible automation, it also creates a new class of failures: an agent may repeatedly execute model calls, tools, workflow transitions, or agent handoffs when the feedback path is not effectively bounded. We call this problem Infinite Agentic Loops (IALs). IALs are not ordinary programming loops; they arise from the interaction between agent logic, framework semantics, runtime observations, and termination mechanisms. Such failures can amplify a single request into long running model and tool execution, causing cost exhaustion, model denial of service, context growth, and repeated external side effects. We propose IAL-Scan, a static analysis tool for detecting IAL failures in real-world LLM agent projects. IAL-Scan abstracts heterogeneous agent code into a framework independent Agent IR, builds an Agentic Loop Dependence Graph (ALDG) to recover explicit and framework induced feedback paths, and checks whether these paths can repeatedly reach costly or state growing operations without an effective bound. We evaluate IAL-Scan on 6,549 LLM agent repositories. It reports 74 potential findings, among which manual review confirms 68 IAL failures across 47 projects, achieving 91.9% precision.

</details>

---
