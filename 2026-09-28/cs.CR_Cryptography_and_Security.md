# cs.CR | Cryptography and Security | 2026-09-28

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/AuthGuard-R_Safety-Compliant_Mission_Hijacking_and_Dual-Gate_Defense_for_LLM-Controlled_Robots|AuthGuard-R: Safety-Compliant Mission Hijacking and Dual-Gate Defense for LLM-Controlled Robots]]

![[assets/2609.31110_first_page.png|800]]

- **arXiv**: [2609.31110](https://arxiv.org/abs/2609.31110)
- **PDF**: https://arxiv.org/pdf/2609.31110
- **详细分析**: [[20_Research/Papers/大模型/AuthGuard-R_Safety-Compliant_Mission_Hijacking_and_Dual-Gate_Defense_for_LLM-Controlled_Robots|AuthGuard-R: Safety-Compliant Mission Hijacking and Dual-Gate Defense for LLM-Controlled Robots]]
- **作者**: Saidattu Chepuri, Vikas Srivastava
- **cs 子类**: cs.CR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《AuthGuard-R: Safety-Compliant Mission Hijacking and Dual-Gate Defense for LLM-Controlled Robots》归入 机器人、大模型、具身智能 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbodiedGovBench, RoboJailBench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models are increasingly used as high-level planners for mobile robots, robot manipulators, and autonomous vehicles. Recent studies show that these systems can be influenced through malicious text, speech, visual instructions, retrieved documents, and poisoned sensory context. Most defenses ask whether a proposed action is physically safe. This paper studies a different problem: an action may be physically safe and still violate the mission authorized by the user. An attacker may redirect a delivery robot, replace an approved object, extend a robot's operating region, activate an unnecessary sensor, or delay a mission without creating an immediate physical hazard. We call this attack \emph{safety-compliant mission hijacking}. We propose MissionPAIR, an adaptive attack framework that searches for executable plans that pass a safety gate while violating an authenticated mission. We also propose AuthGuard-R, a deterministic authorization layer that binds every executable action to a signed mission, robot identity, object and region scope, current state, time, and input provenance. AuthGuard-R operates with an independent safety gate, giving a dual-gate architecture. We formalize mission policies over robot traces, define security games, and prove authorization soundness, mission non-escalation, replay resistance, robot binding, provenance separation, threshold-approval security, audit-log tamper evidence, and trace-level composition. We report a preliminary cross-model evaluation with Claude Haiku~4.5 and the open-source Qwen2.5~7B planner. Across 240 live attack trials, the planners followed an injected mission deviation in 109 trials; AuthGuard-R rejected all 109 resulting unauthorized actions. A separate hand-constructed suite of eleven protocol- and policy-level attacks was also blocked completely.

</details>

---

### [[20_Research/Papers/大模型/MetaPermit_Scalable_and_Auditable_Access_Control_for_AI_Agents_via_LLM-Inferred_Meta-Attributes|MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes]]

![[assets/2609.31039_figure.png|800]]

- **arXiv**: [2609.31039](https://arxiv.org/abs/2609.31039)
- **PDF**: https://arxiv.org/pdf/2609.31039
- **详细分析**: [[20_Research/Papers/大模型/MetaPermit_Scalable_and_Auditable_Access_Control_for_AI_Agents_via_LLM-Inferred_Meta-Attributes|MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes]]
- **作者**: Hanzhang Ma, Ali Hariri, Tianxiang Shen, Bohua Zou, Qianjun Zheng, Ji Wang, Li Yi, Ning Jia, Yutao Liu, Haibo Chen, Lin Wang, Debayan Roy
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《MetaPermit: Scalable and Auditable Access Control for AI Agents via LLM-Inferred Meta-Attributes》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rise of autonomous AI agents equipped with tools has introduced significant security risks, ranging from unintended tool misuse to adversarial manipulation through Indirect Prompt Injection (IPI) attacks. In practice, deployed agent systems such as OpenAI Codex and Claude Code protect tool invocations through a combination of coarse-grained permission rules and LLM-based judgments about individual proposed actions. Both components, however, have important limitations: static policies must anticipate possible user intents and therefore do not scale to open-ended tasks, while LLM-driven authorization supports dynamic decisions but produces inconsistent outcomes and remains vulnerable to targeted IPI attacks. To provide scalable and more consistent authorization, we propose MetaPermit, a policy-based tool access-control framework that decouples semantic inference from security enforcement. By analyzing agent-user interactions, we derive a compact, task-independent set of meta-attributes that capture the relationships among the user's intent, the execution context, and the proposed tool call. These meta-attributes allow MetaPermit to authorize tool use without enumerating user intents. At runtime, an LLM infers the meta-attribute values for each proposed tool call, while a fixed policy evaluates these values to allow or deny the call, making each decision auditable through the inferred values and the applied policy rule. We evaluate MetaPermit on the AgentDojo and AgentDyn benchmarks, across seven task suites and five attack methods, using two widely deployed open-weight LLMs. The results show that MetaPermit produces 31% more consistent authorization decisions than LLM-driven authorization and outperforms the state-of-the-art defenses CaMeL and IPIGuard in both task completion, with improvements of up to 109%, and robustness to IPI attacks, with no malicious tool calls executed.

</details>

---

### [[20_Research/Papers/大模型/AGATE_Provenance-Based_Runtime_Defense_Against_Compositional_Attacks_on_LLM_Agents|AGATE: Provenance-Based Runtime Defense Against Compositional Attacks on LLM Agents]]

![[assets/2609.30830_first_page.png|800]]

- **arXiv**: [2609.30830](https://arxiv.org/abs/2609.30830)
- **PDF**: https://arxiv.org/pdf/2609.30830
- **详细分析**: [[20_Research/Papers/大模型/AGATE_Provenance-Based_Runtime_Defense_Against_Compositional_Attacks_on_LLM_Agents|AGATE: Provenance-Based Runtime Defense Against Compositional Attacks on LLM Agents]]
- **作者**: Xiaorui Zhang, Zhuoran Cheng, Kailin Liu, Zhaoxi Sun, Shiyu Fan, Tongyu Yuan, Bin Yuan, Weizhong Qiang, Deqing Zou
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《AGATE: Provenance-Based Runtime Defense Against Compositional Attacks on LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents can produce harmful effects through sequences of ordinary operations. Judging such actions requires establishing both the authority that permits them and the origin of the data they carry. We present AGATE, an authorization and data-provenance gate at instrumented agent-harness boundaries. Operator declarations and host approval events ground authorization; delegated actions are constrained by grants that bind to exact parameters, expire, and permit a limited number of uses. Source registration connects observed inputs to subsequent transfers, while an effect ledger tracks repeated requests. Deterministic checks make decisions without an LLM in the decision path and retain their grounds with execution evidence for forensic replay. Adapters integrate three production harnesses -- DeepSeek Harness, OpenCode, and OpenClaw -- without modifying host code, translating each host's native observation and veto points into a single shared gate interface; the judgment core is identical in all three, and only enforcement depth differs. Our evaluation combines 153 exercised attack-chain records with deployment, utility, and reconstruction experiments. The deployment observations expose how tool declarations and data checks govern business actions, including a bypass through parameter rewriting. Six of eleven benign file-processing scenarios contain denial events, revealing the utility cost of content-based provenance policies. Across 252 runs on 63 sanitized scenarios, replay agrees with live graph projections for all 63 scenarios on each of two platforms. These results establish the feasibility of provenance-based runtime judgment and identify content transformation, legitimate reuse, and observation coverage as concrete limits.

</details>

---
