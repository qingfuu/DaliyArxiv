# cs.CL | Computation and Language | 2026-10-21

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/大模型/GPT-6-Astra_Understands_Touch_and_Outperform_Vision--Tactile--Language--Action_Models|GPT-6-Astra Understands Touch and Outperform Vision--Tactile--Language--Action Models]]

![[assets/2610.28457_figure.png|800]]

- **arXiv**: [2610.28457](https://arxiv.org/abs/2610.28457)
- **PDF**: https://arxiv.org/pdf/2610.28457
- **详细分析**: [[20_Research/Papers/大模型/GPT-6-Astra_Understands_Touch_and_Outperform_Vision--Tactile--Language--Action_Models|GPT-6-Astra Understands Touch and Outperform Vision--Tactile--Language--Action Models]]
- **作者**: Ziyong Wang, Yupei Lin, Runxuan Huang, Liang Lin, Dongyu Zhang, Guangrun Wang
- **cs 子类**: cs.CL, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.25（加权：具身智能 0.3，大模型 0.25，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GPT-6-Astra Understands Touch and Outperform Vision--Tactile--Language--Action Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Tactile-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose multimodal models have shown promise as direct robot action policies, yet whether they grasp the physics underlying real-world interactions and can apply that understanding to guide action remains underexplored. We investigate this question using contact-rich manipulation as a representative testbed, examining tactile understanding as a concrete instance of this broader capability. Contact-rich manipulation requires interpreting tactile feedback and adjusting actions after obstruction. Existing learned tactile policies acquire these capabilities through specialized pretraining and per-task optimization, with substantial data and training costs. We present GPT-as-Tactile-Policy, which summarizes expert demonstrations into task guidance and tactile references for contact assessment and corrective action. GPT-6-Astra combines this context with multimodal observations and interaction history to generate control commands and adjust actions through contact feedback. Without additional robotics-specific pretraining or per-task policy fine-tuning, our method achieves 93.8\% mean success across five UniVTAC tasks. Overall performance is comparable to state-of-the-art policies, with higher success on selected tasks. On Insert Hole, tactile feedback improves success from 31\% to 99\%. Execution analysis further demonstrates contact-guided probing and correction, supporting manipulation progress through explicit expert experience and online feedback.

</details>

---

### [[20_Research/Papers/具身智能/CAPSafe_A_Benchmark_for_Contextual_Action_and_Plan_Safety_Reasoning_in_Embodied_Agents|CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents]]

![[assets/2610.28381_first_page.png|800]]

- **arXiv**: [2610.28381](https://arxiv.org/abs/2610.28381)
- **PDF**: https://arxiv.org/pdf/2610.28381
- **详细分析**: [[20_Research/Papers/具身智能/CAPSafe_A_Benchmark_for_Contextual_Action_and_Plan_Safety_Reasoning_in_Embodied_Agents|CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents]]
- **作者**: Youmna Farag, Svetlana Stoyanchev, Simon Keizer, Mohan Li, Rama Doddipatla
- **cs 子类**: cs.CL, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.35（加权：具身智能 1.5，大模型 0.55，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《CAPSafe: A Benchmark for Contextual Action and Plan Safety Reasoning in Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EARBench, IS-Bench, Is-Bench, MSSBench, SafeAgent-Bench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning about safety is essential for embodied agents powered by large language models (LLMs). We introduce the Contextual Action and Plan Safety benchmark (CAPSafe), designed to evaluate safety reasoning at two levels: (1) an action-level dataset that tests whether a single action is safe given its environmental context, and (2) a plan-level dataset that evaluates whether agents can generate safe long-horizon plans for complex hazardous household tasks. CAPSafe models safety conditions where hazards are situational (inferred from object properties), multiple hazards can co-occur within the same environment, and each is annotated with a relative severity level for fine-grained analysis. Evaluating nine closed and open-source LLMs reveals a substantial gap between hazard recognition and safe long-horizon planning. Several models achieve high accuracy in recognizing unsafe actions (exceeding 90% in the best cases), yet safe long-horizon planning remains substantially harder. Gemini-3-pro achieves the highest safe success rate (78.19%), while other models remain below 65%. These results highlight that robust safety reasoning over long action sequences remains an open challenge.

</details>

---

### [[20_Research/Papers/大模型/Disclosure_Begets_Disclosure_A_Self-Reinforcing_Privacy_Loop_in_LLM_Agents_with_Persistent_Memory|Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory]]

![[assets/2610.28315_figure.png|800]]

- **arXiv**: [2610.28315](https://arxiv.org/abs/2610.28315)
- **PDF**: https://arxiv.org/pdf/2610.28315
- **详细分析**: [[20_Research/Papers/大模型/Disclosure_Begets_Disclosure_A_Self-Reinforcing_Privacy_Loop_in_LLM_Agents_with_Persistent_Memory|Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory]]
- **作者**: Masahiro Kaneko, Hiromi Arai, Timothy Baldwin
- **cs 子类**: cs.CL, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Disclosure Begets Disclosure: A Self-Reinforcing Privacy Loop in LLM Agents with Persistent Memory》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly use persistent memory to personalize responses, and personal attributes in this memory pose a privacy risk if exposed. We ask how consulting memory during dialogue changes what users go on to say, and thus what the memory comes to reveal. In multi-session simulations, a simulated user with 24 personal attributes talks with a support agent that does or does not consult memory, and in both settings attributes are inferred from the full accumulated record. Across four support models, memory raises response quality but also empirical leakage, the share of attribute values correctly inferred from the record, by a margin that widens over sessions. The cause is a loop in ordinary, non-adversarial assistance. Memory-conditioned responses carry earlier values forward, often as presuppositions, and users affirm them or leave them uncorrected, so that cues and the agent's own guesses become recorded values. The loop reinforces itself, and removing the agent's mentions of an attribute lowers its later disclosure about twice as much as single-turn effects predict. Users cannot leave it on their own, since correcting a value discloses the attribute, declining to discuss it shifts later predictions toward sensitive values, and incorrect values left in place become entrenched. The loop is best weakened at the agent's response. Instructing the agent not to state or presuppose attributes brings leakage to about the no-memory level while keeping most of the quality gains, whereas filtering or anonymizing what users say or what is stored gives up much of them.

</details>

---

### [[20_Research/Papers/大模型/Adaptive_Stopping_of_Streamed_Reasoning_for_Language_Model_Agents|Adaptive Stopping of Streamed Reasoning for Language Model Agents]]

![[assets/2610.27981_figure.png|800]]

- **arXiv**: [2610.27981](https://arxiv.org/abs/2610.27981)
- **PDF**: https://arxiv.org/pdf/2610.27981
- **详细分析**: [[20_Research/Papers/大模型/Adaptive_Stopping_of_Streamed_Reasoning_for_Language_Model_Agents|Adaptive Stopping of Streamed Reasoning for Language Model Agents]]
- **作者**: JunHyeok Oh, Byung-Jun Lee
- **cs 子类**: cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Adaptive Stopping of Streamed Reasoning for Language Model Agents》归入 大模型 方向。该论文围绕 Computation and Language 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning-enabled language model agents can incur substantial computation before acting, although the reasoning needed varies across decisions. Existing stopping signals, such as confidence and intermediate-answer stability, can vary in effectiveness across reasoning models; signals obtained from hidden states or token probabilities also require internal access that may be unavailable or impractical. We introduce StreamStop, which learns model-specific stopping policies offline from prefix-level action agreement. A frozen prefix reader encodes available reasoning text for a lightweight stop head, allowing stopping without access to the reasoning model's internal signals. We construct and publicly release a dataset of agent reasoning trajectories with prefix-level action annotations. These annotations compare each prefix action with the full-reasoning reference action, enabling offline comparison of stopping rules and exact expected-return optimization of a discounted action-agreement objective. Conditioning the head on the discount factor allows the agreement-token trade-off to be adjusted at inference without retraining. In closed-loop evaluations on WebShop and ScienceWorld, StreamStop achieves higher observed success than most validation-selected fixed-budget settings while using fewer reasoning tokens than Full thinking. On WebShop with Qwen3.8-27B, it uses 42% fewer reasoning tokens per episode with similar observed task success.

</details>

---
