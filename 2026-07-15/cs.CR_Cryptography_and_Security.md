# cs.CR | Cryptography and Security | 2026-07-15

#arxiv #ComputerScience

**论文数**: 3

### [[20_Research/Papers/大模型/PVDetector_Detecting_Prompt_Injection_Attacks_on_Purpose-Specific_LLM_Agents_through_Policy-Violation_Concept_Analysis|PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis]]

![[assets/2607.12624_figure.png|800]]

- **arXiv**: [2607.12624](https://arxiv.org/abs/2607.12624)
- **PDF**: https://arxiv.org/pdf/2607.12624
- **详细分析**: [[20_Research/Papers/大模型/PVDetector_Detecting_Prompt_Injection_Attacks_on_Purpose-Specific_LLM_Agents_through_Policy-Violation_Concept_Analysis|PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis]]
- **作者**: Junhui Wang, Hangtao Zhang, Zhirun Zheng, Li Zeng, Jiejun Xiao, Xi Luo, Lihua Yin, Saiqin Long
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《PVDetector: Detecting Prompt Injection Attacks on Purpose-Specific LLM Agents through Policy-Violation Concept Analysis》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly deployed as purpose-specific agents to handle domain-specific tasks such as customer service and code generation. These agents are expected to comply with not only generic safety guardrails but also purpose-specific restrictions tailored to their designated roles. Such additional restrictions enlarge the attack surface, particularly to prompt injection (PI) attacks. To defend against such attacks, existing detection methods primarily rely on analyzing input-output patterns, yet yield limited effectiveness. To address this limitation, we turn to analyzing the hidden activation space and discover that LLMs inherently retain latent policy-violation (PV) concepts when prompted with requests beyond their designated purpose. Particularly, PV concepts capture the semantics of conflicts between user queries and predefined restrictions, implicitly reflecting LLMs' intrinsic awareness of recognizing policy violations. Building on this insight, we propose PVDetector, a training-free framework that detects PI attacks during LLM inference by measuring hidden-state alignment with PV concepts, which are derived offline from the contrastive pairs of policy-violating and policy-compliant prompts. Experiments across multiple LLMs and datasets show that PVDetector achieves &lt;1\% false negative rate with minimal auxiliary overhead, consistently outperforming state-of-the-art methods. Our code is available at https://github.com/Claresigle/PVDetector .

</details>

---

### [[20_Research/Papers/大模型/Trust_but_Verify_Uncovering_the_Security_Debt_of_Autonomous_Coding_Agents|Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents]]

![[assets/2607.12428_figure.png|800]]

- **arXiv**: [2607.12428](https://arxiv.org/abs/2607.12428)
- **PDF**: https://arxiv.org/pdf/2607.12428
- **详细分析**: [[20_Research/Papers/大模型/Trust_but_Verify_Uncovering_the_Security_Debt_of_Autonomous_Coding_Agents|Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents]]
- **作者**: A H M Nazmus Sakib, Dipayan Banik, Murtuza Jadliwala
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Trust but Verify? Uncovering the Security Debt of Autonomous Coding Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The increasing adoption of autonomous coding agents accelerates software development but also introduces scoped security risks within high-impact file paths that can outpace traditional human review capacity. While prior research has primarily evaluated these systems in terms of functional correctness and productivity, this paper presents a large-scale empirical study using the AIDev dataset to systematically characterize security code smells in agent-generated pull requests (PRs). Through a combination of a validated LLM-as-a-judge framework and manual qualitative analysis, we identify and classify security misconfigurations across 16,112 file changes spanning 4,022 pull requests. Our results reveal that 38.9% of agent-generated PRs contain at least one security smell, with supply chain integrity issues accounting for 82.3% of all detected security smells. Furthermore, hard-coded credentials constitute 99.6% of all critical-severity security smells. Crucially, we find that human collaborators are responsible for introducing 67.6% of genuine leaked secrets within these agent-assisted workflows, while existing automated and human review processes fail to detect 81.1% of these credentials prior to integration. These findings highlight substantial security risks in agent-assisted software development workflows and suggest a potential reduction in developer vigilance. They also underscore the urgent need for context-aware security guardrails implemented directly at the point of human-AI collaboration.

</details>

---

### [[20_Research/Papers/大模型/Skills_That_Don't_Exist_A_Large-Scale_Study_of_Hallucinated_Skill_Recommendation_in_LLM_Agents|Skills That Don't Exist: A Large-Scale Study of Hallucinated Skill Recommendation in LLM Agents]]

![[assets/2607.12340_figure.png|800]]

- **arXiv**: [2607.12340](https://arxiv.org/abs/2607.12340)
- **PDF**: https://arxiv.org/pdf/2607.12340
- **详细分析**: [[20_Research/Papers/大模型/Skills_That_Don't_Exist_A_Large-Scale_Study_of_Hallucinated_Skill_Recommendation_in_LLM_Agents|Skills That Don't Exist: A Large-Scale Study of Hallucinated Skill Recommendation in LLM Agents]]
- **作者**: Weifeng Yuan, Wenbo Guo, Feng Dong, Haoyu Wang, Yang Liu
- **cs 子类**: cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Skills That Don't Exist: A Large-Scale Study of Hallucinated Skill Recommendation in LLM Agents》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents acquire new capabilities by downloading skills from open registries. Instead of browsing these catalogs manually, developers typically ask the agent to recommend and install a skill. This convenience hides a risk: agents frequently invent names for skills that exist in no registry. We term this flaw skill name hallucination. A fake name may seem harmless, but it opens the door to supply-chain attacks. Because registries rarely verify publishers, an adversary can prompt the agent, collect the fake names it returns, pre-register malicious skills under them, and wait for a victim to install the payload. We conducted the first large-scale measurement of skill name hallucination, evaluating 15,000 prompts across 12 configurations (4 standalone LLMs and 8 agents). We conservatively counted a name as hallucinated only if it was missing from all live registries and GitHub. The results reveal a systemic vulnerability: every configuration hallucinates. Rates average 36.0% for standalone LLMs and 36.9% for agents, rising to 43.1% on real-world developer questions. In total, the systems generated 5,669 distinct hallucinated names. Crucially, these names are not random noise. Agents repeat the same fake names across prompts and models, giving attackers highly reliable targets to hijack. Finally, we tested four model-level defenses and found a severe conflict between security and usability. The strongest, retrieval grounding, cut the hallucination rate from 40.8% to 3.2% but crippled usefulness: even the best-defended system recommended the correct skill only about one in six times. Skill name hallucination is thus a highly exploitable vulnerability requiring minimal attacker effort. Fixing it cannot rely on prompt engineering or model tuning alone. It demands ecosystem-wide structural changes: registry-level name reservations and verified recommendation pipelines.

</details>

---
