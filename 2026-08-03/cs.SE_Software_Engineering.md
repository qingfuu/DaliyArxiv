# cs.SE | Software Engineering | 2026-08-03

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/Reusing_Past_Repairs_Through_Hierarchical_Trajectory_Abstraction_for_Coding_Agents|Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents]]

![[assets/2607.29658_figure.png|800]]

- **arXiv**: [2607.29658](https://arxiv.org/abs/2607.29658)
- **PDF**: https://arxiv.org/pdf/2607.29658
- **详细分析**: [[20_Research/Papers/大模型/Reusing_Past_Repairs_Through_Hierarchical_Trajectory_Abstraction_for_Coding_Agents|Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents]]
- **作者**: Yisen Xu, Jiayuan Zhou, Ruiqi Pan, Tse-Hsun Chen
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Reusing Past Repairs Through Hierarchical Trajectory Abstraction for Coding Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although LLM-driven repair agents can tackle complex, repository-level issues, they treat every issue independently and discard the procedural knowledge accumulated from previous repairs. We introduce STAIR, a framework that converts historical repair trajectories into hierarchical, reusable plans that can be adapted to steer future repairs. Each past trajectory is transformed into a multi-level tree that ranges from fine-grained diagnostic actions to high-level repair strategies, encoding experience at several granularities. When a new issue arrives, STAIR selects relevant plan nodes from multiple abstraction levels, tailors them into executable, issue-specific plans, and supplies them to the agent through its prompt. On SWE-bench Verified, STAIR integrated with Lingxi reaches 81.2% Pass@1 using MiniMax M2.5 and 79.2% using GPT-5. The generated plans also generalize across agents: without any code change, they lift the Pass@1 of a structurally different agent, mini-SWE-agent v2, from 75.8% to 81.0%. Ablation experiments further show that mixing multiple abstraction levels surpasses any single level and that raw, unabstracted trajectories transfer substantially worse.

</details>

---

### [[20_Research/Papers/大模型/Execution-First_Synthetic_Tool-Use_Trace_Generation_for_LLM_Agents|Execution-First Synthetic Tool-Use Trace Generation for LLM Agents]]

![[assets/2607.29175_figure.png|800]]

- **arXiv**: [2607.29175](https://arxiv.org/abs/2607.29175)
- **PDF**: https://arxiv.org/pdf/2607.29175
- **详细分析**: [[20_Research/Papers/大模型/Execution-First_Synthetic_Tool-Use_Trace_Generation_for_LLM_Agents|Execution-First Synthetic Tool-Use Trace Generation for LLM Agents]]
- **作者**: Hafsa Ouajdi, Francesco Giannuzzo, Alaa Boukhary, Paolo Papotti, Gerard Conangla, Adam Elwood
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Execution-First Synthetic Tool-Use Trace Generation for LLM Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SyntheticAgentTraceQA, ToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic software-engineering and industrial systems increasingly operate through executable workflows rather than code genera- tion alone: they search artifacts, invoke tools, inspect structured observations, and query databases. Training these agents requires supervision data that captures valid tool interactions and executable workflows. However, traditional query-first data synthesis can fail because plausible user requests may not correspond to valid tool sequences, compatible parameters, or available data. To address this limitation, we propose SyntheticAgentTraceQA, an execution- first framework for generating scalable supervision data for tool- augmented agents. Our framework first constructs high-level work- flow structures, maps them to available tools through dependency- aware assignment, executes and validates the resulting traces in con- trolled environments, and only then synthesizes natural-language user tasks, teacher-generated reasoning annotations, and reference answers. We evaluate the framework across four tool ecosystems and use the resulting data to fine-tune and evaluate Qwen model variants. The results show that execution-grounded supervision improves tool execution behavior, reference-trace agreement, and answer-generation performance on the evaluated tasks. Further analysis reveals a supervision trade-off: masked supervision, which excludes reasoning annotations from the training objective, im- proves final-answer metrics, whereas full supervision, computing loss over the complete assistant output including reasoning tokens, underperforms on answer quality and does not consistently im- prove reference-trace agreement, particularly at the 9B scale. These findings highlight the importance of designing synthetic supervi- sion according to the desired capabilities of tool-augmented agents.

</details>

---

### [[20_Research/Papers/大模型/Preventing_Premature_Commitment_in_Coding_Agents_with_an_Evidence-Conditioned_Execution_Layer|Preventing Premature Commitment in Coding Agents with an Evidence-Conditioned Execution Layer]]

![[assets/2607.28815_figure.png|800]]

- **arXiv**: [2607.28815](https://arxiv.org/abs/2607.28815)
- **PDF**: https://arxiv.org/pdf/2607.28815
- **详细分析**: [[20_Research/Papers/大模型/Preventing_Premature_Commitment_in_Coding_Agents_with_an_Evidence-Conditioned_Execution_Layer|Preventing Premature Commitment in Coding Agents with an Evidence-Conditioned Execution Layer]]
- **作者**: Yisen Xu, Chenglin Li, Zehao Wang, Jinqiu Yang, Tse-Hsun Chen
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Preventing Premature Commitment in Coding Agents with an Evidence-Conditioned Execution Layer》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based coding agents often edit source code or submit patches before examining enough repository evidence to justify the change, a failure pattern we call premature commitment. We present ECLoop, an execution layer that interposes between the agent and the repository to enforce evidence-conditioned execution. For each task, ECLoop uses the issue description and repository structure to compile a set of conditions specifying what the agent should observe before each type of code modification or patch submission. During execution, ECLoop tracks which conditions the agent's runtime trajectory has satisfied and postpones any proposed action whose required conditions remain unmet. Evaluated on all 500 instances of SWE-bench Verified with two language models and two agent scaffolds, ECLoop raises Pass@1 by 4.8-11.8 percentage points without model retraining or scaffold changes. Ablation experiments show that each of ECLoop's three operations contributes distinct value and that structured evidence conditions outperform an equivalent natural-language summary. These gains come at no additional inference cost: by redirecting the agent before it pursues unsupported actions, ECLoop lowers average token consumption by up to 12.1%.

</details>

---
