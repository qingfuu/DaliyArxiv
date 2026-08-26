# cs.CR | Cryptography and Security | 2026-08-24

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/TraceGrant_A_Contract-Governed_Security_Framework_for_the_Task-Effect_Lifecycle_of_Networked_LLM_Agents|TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents]]

![[assets/2608.21126_figure.png|800]]

- **arXiv**: [2608.21126](https://arxiv.org/abs/2608.21126)
- **PDF**: https://arxiv.org/pdf/2608.21126
- **详细分析**: [[20_Research/Papers/大模型/TraceGrant_A_Contract-Governed_Security_Framework_for_the_Task-Effect_Lifecycle_of_Networked_LLM_Agents|TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents]]
- **作者**: Bohao Liao, Jingchao Wang, Qipeng Song, Jin Cao, Jieling Wang, Boyu Deng
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《TraceGrant: A Contract-Governed Security Framework for the Task-Effect Lifecycle of Networked LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Networked large language model (LLM) agents retrieve information from email, cloud storage, calendars, transaction platforms, and Web services to complete multistep tasks that produce persistent external effects. The same content needed for legitimate execution may also contain indirect prompt injections that redirect tool use, alter sensitive arguments, or disrupt task completion. Existing defenses mainly constrain untrusted content or individual tool calls, leaving user intent, runtime evidence, realized effects, and task completion insufficiently connected. We present TraceGrant, a security framework that governs the task-effect lifecycle of networked LLM agents through an explicit Contract. Before execution, TraceGrant establishes a task-effect boundary from the trusted user request. During execution, admitted evidence can instantiate only authority already established by the Contract. After execution, task completion is verified against actual tool results. Across 949 AgentDojo and 400 Agent Security Bench attack cases under fixed benchmark settings, TraceGrant recorded no attack successes while retaining utility under attack rates of 77.32% and 83.00%, respectively. We further evaluate TraceGrant through white-box defense-aware attacks, Contract quality analysis, stage ablations, targeted stress tests, and runtime overhead measurements. The results show that TraceGrant provides a unified governance layer that connects trusted user intent, runtime evidence, concrete tool execution, and verified task completion.

</details>

---

### [[20_Research/Papers/具身智能/GhostTac_Manipulating_Tactile_Sensors_without_Physical_Contact|GhostTac: Manipulating Tactile Sensors without Physical Contact]]

![[assets/2608.20817_figure.png|800]]

- **arXiv**: [2608.20817](https://arxiv.org/abs/2608.20817)
- **PDF**: https://arxiv.org/pdf/2608.20817
- **详细分析**: [[20_Research/Papers/具身智能/GhostTac_Manipulating_Tactile_Sensors_without_Physical_Contact|GhostTac: Manipulating Tactile Sensors without Physical Contact]]
- **作者**: Kun Wang, Xuancun Lu, Ruochen Zhou, Kai Wang, Tongjun Ye, Yihao Shao, Chen Yan, Xiaoyu Ji, Wenyuan Xu
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《GhostTac: Manipulating Tactile Sensors without Physical Contact》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensors are integral to modern robotic systems, enabling robots to perceive and interact with the physical environment through tactile feedback. However, the physical-layer security of tactile sensors has received little attention. We present GhostTac, the first contactless attack, to the best of our knowledge, that manipulates tactile sensing through electromagnetic interference (EMI). GhostTac exploits nonlinear rectification and limited-bandwidth amplification, converting carefully crafted EMI signals into persistent DC offsets that bypass onboard filtering and induce stable measurement deviations. It enables fine-grained, controllable manipulation of sensor outputs by shaping the spatial distribution and magnitude of interference at targeted locations. Such manipulation can induce harmful robot behaviors, including excessive force that may damage objects or injure people. We evaluate GhostTac on 10 sensor modules and two dexterous hands, covering 15 tactile sensors of different types, and demonstrate consistent effectiveness across all tested devices. Three case studies involving tactile grasping, slip detection, and material classification further illustrate its practical impact on real robotic tasks. These findings reveal a new physical attack vector against tactile sensing in robotic systems.

</details>

---

### [[20_Research/Papers/大模型/The_Claws_in_Plain_Sight_Unauthorized_Context_Disclosure_through_LLM_Agent_Tool_Calls|The Claws in Plain Sight: Unauthorized Context Disclosure through LLM Agent Tool Calls]]

![[assets/2608.20658_figure.png|800]]

- **arXiv**: [2608.20658](https://arxiv.org/abs/2608.20658)
- **PDF**: https://arxiv.org/pdf/2608.20658
- **详细分析**: [[20_Research/Papers/大模型/The_Claws_in_Plain_Sight_Unauthorized_Context_Disclosure_through_LLM_Agent_Tool_Calls|The Claws in Plain Sight: Unauthorized Context Disclosure through LLM Agent Tool Calls]]
- **作者**: Ben Dong, Zhonghao Guo, Tianyi Lu, Qian Wang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《The Claws in Plain Sight: Unauthorized Context Disclosure through LLM Agent Tool Calls》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents routinely construct tool-call arguments from user profiles, conversation history, retrieved documents, and prior tool results. However, legitimate access to contextual information does not imply authorization to transmit that information for every purpose or destination. We present Claw in Plain Sight, an authority- pressure attack in which task-adjacent content frames protected attributes as operationally or procedurally required, causing a model to include them in otherwise valid generated arguments. We evaluate Claw in Plain Sight using a controlled synthetic benchmark that crosses six pressure levels with four privacy-policy levels across five DeepSeek and Claude model configurations, producing 120 calls. Across the complete pressure-policy matrix, session-level disclosure rates range from 20.8% to 75.0% among the tested models. Stronger privacy instructions reduce aggregate disclosure but do not eliminate it consistently across models, showing that prompt-level policies do not provide a portable enforcement boundary. Our experiments use only synthetic profiles and capture proposed arguments locally; they measure policy-violating generation at the context-to-argument boundary, not completed network exfiltration or leakage from deployed users. These findings motivate purpose- and destination-aware inspection of generated tool arguments before execution.

</details>

---
