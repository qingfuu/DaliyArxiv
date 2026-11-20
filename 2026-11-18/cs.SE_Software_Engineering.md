# cs.SE | Software Engineering | 2026-11-18

#arxiv #ComputerScience

**论文数**: 2

### [[20_Research/Papers/大模型/The_Defense_Rests_A_Courtroom-Inspired_Multi-Agent_LLM_Framework_for_Automated_Safety_Case_Generation|The Defense Rests: A Courtroom-Inspired Multi-Agent LLM Framework for Automated Safety Case Generation]]

![[assets/2611.21618_figure.png|800]]

- **arXiv**: [2611.21618](https://arxiv.org/abs/2611.21618)
- **PDF**: https://arxiv.org/pdf/2611.21618
- **详细分析**: [[20_Research/Papers/大模型/The_Defense_Rests_A_Courtroom-Inspired_Multi-Agent_LLM_Framework_for_Automated_Safety_Case_Generation|The Defense Rests: A Courtroom-Inspired Multi-Agent LLM Framework for Automated Safety Case Generation]]
- **作者**: Gerhard Yu, Amanuel Aknaw, Amir Ali Mohaghegh, Yong Song, Cao, Alvine B. Belle
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Defense Rests: A Courtroom-Inspired Multi-Agent LLM Framework for Automated Safety Case Generation》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety cases are widely used to demonstrate that mission-critical systems, such as autonomous vehicles and unmanned aerial systems, can operate safely after deployment. However, manually constructing safety cases is complex, time-consuming, and labor-intensive, which calls for the proposal of automated approaches to support their creation. Inspired by the legal nature of safety case construction, we formalize the safety case creation problem through a courtroom analogy, where stakeholders collaboratively propose, examine, criticize, review, improve and validate safety claims and their supporting evidence. In this analogy, the safety analyst acts as a prosecutor by identifying hazards and safety concerns, while the assurance case developer serves as a defense attorney by constructing and substantiating safety arguments. An orchestrator acts as a judge by coordinating stakeholder interactions, and a review board serves as a jury by assessing argument completeness and persuasiveness. Based on this formalization, we propose eTrustWare, a Large Language Model (LLM)-based multi-agent framework for automated safety case generation and review. Our experiments on several safety cases of ML-enabled autonomous driving systems demonstrate the feasibility of coordinated LLM-based agents for generating safety cases.

</details>

---

### [[20_Research/Papers/大模型/Does_Your_Agent_Need_to_Know_Its_Budget_A_Placebo-Controlled_Experiment_on_LLM_Coding_Agents|Does Your Agent Need to Know Its Budget? A Placebo-Controlled Experiment on LLM Coding Agents]]

![[assets/2611.21614_figure.png|800]]

- **arXiv**: [2611.21614](https://arxiv.org/abs/2611.21614)
- **PDF**: https://arxiv.org/pdf/2611.21614
- **详细分析**: [[20_Research/Papers/大模型/Does_Your_Agent_Need_to_Know_Its_Budget_A_Placebo-Controlled_Experiment_on_LLM_Coding_Agents|Does Your Agent Need to Know Its Budget? A Placebo-Controlled Experiment on LLM Coding Agents]]
- **作者**: Iftesam Nabi, Jarif Ul Alam, Sunzid Hassan, Sabbir Alom Shuvo, Md Faiaz Al Islam, Yead Rahman, Mehrab Hosain
- **cs 子类**: cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Does Your Agent Need to Know Its Budget? A Placebo-Controlled Experiment on LLM Coding Agents》归入 大模型 方向。该论文围绕 Software Engineering 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Organizations deploying autonomous coding agents impose token budgets, yet the causal effects of a budget, and of telling the agent about it, are unmeasured. We conduct a placebo-controlled factorial experiment under a frozen, timestamped protocol, crossing budget enforcement with budget disclosure on two executable program-repair benchmarks (5,835 runs, two open models, three cap levels). Enforcing a calibrated cap reduced task resolution by 20.0 percentage points while reducing tokens per resolved task roughly twelvefold. Disclosing the enforced budget never helped: the placebo-controlled risk difference was -2.8 pp (95% CI [-6.2, +0.7]) at the medium cap and -4.2 pp ([-8.1, -0.2], nominally significant, unadjusted) at the tight cap, with every prompt wording and per-turn feedback variant far below the 10-point effect size of interest. Observed run-to-run outcome variance was roughly 1.5x the uncapped level under caps, though part of this reflects resolution rates moving nearer one half. These results make budget governance for coding agents an enforcement-design problem: no communication variant produced an effect beyond that of an unrelated sentence, which itself raised resolution by 7.2 pp (95% CI [+4.0, +10.5]) over silent enforcement, a sentence effect that only a placebo control removes.

</details>

---
