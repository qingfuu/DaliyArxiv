# cs.CR | Cryptography and Security | 2026-06-17

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/Seeing_Is_Not_Screening_Multimodal_Hidden_Instruction_Attacks_on_Agent_Skill_Scanners|Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners]]

![[assets/2606.18198_figure.png|800]]

- **arXiv**: [2606.18198](https://arxiv.org/abs/2606.18198)
- **PDF**: https://arxiv.org/pdf/2606.18198
- **详细分析**: [[20_Research/Papers/大模型/Seeing_Is_Not_Screening_Multimodal_Hidden_Instruction_Attacks_on_Agent_Skill_Scanners|Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners]]
- **作者**: Xiaojun Jia, Jie Liao, Simeng Qin, Ke Ma, Wenbo Guo, Yebo Feng, Aishan Liu, Yang Liu
- **cs 子类**: cs.CR, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Seeing Is Not Screening: Multimodal Hidden Instruction Attacks on Agent Skill Scanners》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent skills are emerging as an important attack surface in LLM-based systems. Through an empirical study of existing skill scanners, we find that current defenses primarily rely on textual descriptions, manifests, and source code as the main signals for security analysis, which can leave visually conveyed malicious intent insufficiently examined. This creates a practical blind spot: harmful operational instructions hidden in images may bypass scanning while still being recoverable by multimodal agents during deployment. To systematically investigate this threat, we propose SkillCamo, a document-mediated multimodal instruction attack that conceals malicious instructions within images bundled with a skill while rewriting the surrounding documentation to naturally reference those images as part of the normal workflow. Thus, the attack does not rely on the image alone, but on the joint interpretation of textual guidance and visual payload at execution time. To defend against such attacks, we further propose ExecScan, an execution-grounded multimodal scanning module that performs intent extraction, behavior reconstruction, abuse assessment, and deliberative execution simulation over skill artifacts. ExecScan jointly analyzes documentation, code, referenced resources, and visual content to recover hidden instructions, reconstruct executable behavior chains, and identify downstream risks such as exfiltration, destruction, persistence, deception, and privilege escalation. Extensive experiments show that image-hidden malicious instructions challenge existing skill scanners, while ExecScan can improve the skill scanning performance.

</details>

---

### [[20_Research/Papers/大模型/Cordon_Semantic_Transactions_for_Tool-Using_LLM_Agents|Cordon: Semantic Transactions for Tool-Using LLM Agents]]

![[assets/2606.17573_figure.png|800]]

- **arXiv**: [2606.17573](https://arxiv.org/abs/2606.17573)
- **PDF**: https://arxiv.org/pdf/2606.17573
- **详细分析**: [[20_Research/Papers/大模型/Cordon_Semantic_Transactions_for_Tool-Using_LLM_Agents|Cordon: Semantic Transactions for Tool-Using LLM Agents]]
- **作者**: Zheng Chen, Hanqing Liu, Duling Xu, Dong Dong, Jialin Li, Bangzheng Pu, Jidong Zhai
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Cordon: Semantic Transactions for Tool-Using LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using LLM agents are shifting the unit of computation from explicit human-issued commands to model-driven tasks with stateful consequences. Yet today's agent runtimes still expose tools as isolated RPCs. This interface gives runtimes a convenient integration point, but it lacks a task-scoped execution boundary for commit, rollback, recovery, and audit across multi-step agent workflows. We argue that this mismatch calls for a runtime containment boundary rather than another per-call guardrail. This paper introduces Cordon, a transactional runtime system for staging and validating irreversible agent effects before commit. A semantic transaction is a task-level execution boundary that binds tool intents and runtime-tracked result lineage to reversible local state, staged external effects, delegated authority, and audit metadata. Cordon implements this abstraction with a transaction manager that tracks derived result objects, executes reversible mutations in shadow state, stages outward-facing actions in an effect outbox, and records recovery metadata. The runtime then validates the composed execution flow before it commits state or releases external effects. Our evaluation across adversarial and benign workflows shows that Cordon exposes cross-step violations missed by existing defenses. It also reduces irreversible-effect failures while preserving benign task completion with modest approval and latency overhead.

</details>

---
