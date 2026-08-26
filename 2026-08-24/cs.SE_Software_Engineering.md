# cs.SE | Software Engineering | 2026-08-24

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Natural-Language_Workflows_Are_Not_Software_Yet_Artifact-Driven_Compilation_for_Reliable_Agent_Execution|Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution]]

![[assets/2608.21341_figure.png|800]]

- **arXiv**: [2608.21341](https://arxiv.org/abs/2608.21341)
- **PDF**: https://arxiv.org/pdf/2608.21341
- **详细分析**: [[20_Research/Papers/大模型/Natural-Language_Workflows_Are_Not_Software_Yet_Artifact-Driven_Compilation_for_Reliable_Agent_Execution|Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution]]
- **作者**: Xiangzhe Xu, Hanxi Guo, Guangyu Shen, Siyuan Cheng, Xiangyu Zhang
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Natural-Language Workflows Are Not Software Yet: Artifact-Driven Compilation for Reliable Agent Execution》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural-language workflows offer a software-like interface for agents: domain experts can write reusable procedures, and agents can execute them as instructions. This promise is not yet reliable. Workflow descriptions often leave data dependencies implicit, so the executor must infer which prior results a step should use; agents can also fail to follow long or branching instructions under context pressure. We propose Artic, an artifact-driven workflow compiler that transforms a natural-language workflow into an artifact-driven workflow in which each step declares the artifacts it reads and writes, constraints gate produced artifacts, and explicit control transfers route execution. This representation exposes the enforcement burden placed on agent execution, allowing the compiler to identify steps that depend on too much state or contain difficult control logic and refine them through constrained optimization. To validate the LLM-assisted transformation, Artic decomposes faithfulness checking into local obligations and uses scenario-based dry runs to test whether compiled workflow regions conform to the source workflow. We evaluate Artic on 488 problem instances from 11 real-world domain workflows; it improves task resolve rate by 28 percentage points over the original text workflow. We also show that workflows compiled by Artic are 32 and 56 percentage points more consistent in cross-model and repeated-execution setups, respectively.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Fault_Localization_A_Trajectory-Level_Study_of_LLM_Agents_for_Microservice_Root_Cause_Analysis|Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis]]

![[assets/2608.21310_figure.png|800]]

- **arXiv**: [2608.21310](https://arxiv.org/abs/2608.21310)
- **PDF**: https://arxiv.org/pdf/2608.21310
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Fault_Localization_A_Trajectory-Level_Study_of_LLM_Agents_for_Microservice_Root_Cause_Analysis|Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis]]
- **作者**: Qisheng Lu, Aoyang Fang, Junjielong Xu, Jin'ao Shang, Songhan Zhang, Yifan Yang, Xiaochuan Yan, Pinjia He
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Beyond Fault Localization: A Trajectory-Level Study of LLM Agents for Microservice Root Cause Analysis》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RCABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing evaluations of automated root cause analysis (RCA) for microservices assess diagnostic performance mainly by endpoint correctness: whether a method localizes the responsible service. This criterion enables comparison but does not reveal the evidentiary basis of a diagnosis or the fault-propagation route connecting the source to observed symptoms, both of which an on-call site reliability engineer needs to judge whether action is warranted. We therefore treat RCA as an observable diagnostic process. Our trajectory-level framework evaluates agent executions against manually curated service-level fault-propagation paths. Applied to a public microservice RCA benchmark, it analyzes 3,500 diagnostic trajectories, characterizing where agents investigate and how they use retrieved telemetry. We find a disconnect between answer correctness and diagnostic quality: an agent may localize the fault source yet fail to reconstruct its propagation. Successful investigations stay on the fault-impact surface, act on retrieved evidence, and broaden their query repertoire as the search deepens. Failures arise when decisive evidence is omitted, retrieved evidence is misinterpreted, or unsupported inference substitutes for missing evidence. We operationalize this taxonomy as DiagGuard, a two-stage defense-in-depth architecture in which grounding surveys available observations before localization and verification audits the diagnosis against them. In an independent setting with a different model, benchmark, and service topology, DiagGuard raises Acc@1 from 43.5% to 52.5%. These results show that trajectory-level evaluation exposes limitations hidden by final-answer metrics and provides actionable guidance for improving automated RCA.

</details>

---

### [[20_Research/Papers/大模型/Spike-Killer_Evidence-Gated_LLM_Assistance_for_Safe_Performance_Diagnosis_on_a_Real_Windows_Workstation|Spike-Killer: Evidence-Gated LLM Assistance for Safe Performance Diagnosis on a Real Windows Workstation]]

![[assets/2608.21069_first_page.png|800]]

- **arXiv**: [2608.21069](https://arxiv.org/abs/2608.21069)
- **PDF**: https://arxiv.org/pdf/2608.21069
- **详细分析**: [[20_Research/Papers/大模型/Spike-Killer_Evidence-Gated_LLM_Assistance_for_Safe_Performance_Diagnosis_on_a_Real_Windows_Workstation|Spike-Killer: Evidence-Gated LLM Assistance for Safe Performance Diagnosis on a Real Windows Workstation]]
- **作者**: Baocheng Zeng, Jinhao Yang
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Spike-Killer: Evidence-Gated LLM Assistance for Safe Performance Diagnosis on a Real Windows Workstation》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OSWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-assisted agents can synthesize system evidence, propose configuration changes, and automate diagnostic tasks, but their flexibility makes an imprecise action or an intrusive collector an operational risk. We present Spike-Killer, a human-approved workflow for diagnosing frame-time complaints on one real Windows workstation. The workflow treats each action as an evidence-gated transaction: it records the exact target state, classifies risk, preserves a snapshot, verifies a postcondition, and retains failed measurements as first-class evidence. This experience paper reports a completed same-day study with Counter-Strike 2 as a demanding target application. The evidence bundle contains preserved state snapshots, exploratory microbenchmarks, a ten-run same-state repeatability probe, live telemetry, a repaired over-broad registry action, incompatible presentation-capture attempts, an invalid local replay, and a system-level tracing replacement. Windows Performance Recorder produced two CS2 local-Bot GPU traces of 90.69 and 85.85 seconds; both were attributed to cs2.exe, exposed DxgKrnl Present metadata, and had zero lost ETW buffers or events. These results qualify trace integrity, not performance: the study reports no frame intervals, P99 estimate, or intervention effect. The contribution is an auditable, human-in-the-loop pattern for trustworthy agent assistance on a real workstation, including explicit stop conditions when evidence is insufficient.

</details>

---
