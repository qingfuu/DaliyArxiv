# cs.CR | Cryptography and Security | 2026-11-04

#arxiv #ComputerScience

**论文数**: 4

### [[20_Research/Papers/大模型/Right_Tool,_Wrong_Parameters_Defending_LLM_Agents_Against_Parameter_Poisoning|Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning]]

![[assets/2611.04673_figure.png|800]]

- **arXiv**: [2611.04673](https://arxiv.org/abs/2611.04673)
- **PDF**: https://arxiv.org/pdf/2611.04673
- **详细分析**: [[20_Research/Papers/大模型/Right_Tool,_Wrong_Parameters_Defending_LLM_Agents_Against_Parameter_Poisoning|Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning]]
- **作者**: Yao Wang, Zehua Ma, Weiming Zhang, Han Fang
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Right Tool, Wrong Parameters: Defending LLM Agents Against Parameter Poisoning》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FactAuthBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Indirect Prompt Injection (IPI) poses a critical threat to LLM agents. Existing defenses largely focus on whether an injection induces a new tool invocation or unintended action. In this paper, we study a different attack surface, parameter poisoning, where the attacker preserves the intended action but manipulates one or more tool arguments, such as a recipient or other task-critical value. Such attacks are difficult to detect because no new action is introduced, while parameter changes themselves are often legitimate parts of the user's request. Our key insight is that the legitimacy of a parameter change should be determined by the trust of the information flow that produces it under the user query. The query induces a task-specific trust hierarchy over available information fields: some are trusted to determine particular parameters, while others should have little or no influence. Based on this insight, we propose AuthorityFlow, a three-stage parameter-level defense. First, it interprets the user query to construct a task-specific trust hierarchy over the information fields available to the agent. Second, for each tool argument, it traces the information flow that produces its current value and attributes the value to its supporting field. Finally, it accepts the value only when that field is trusted to determine the parameter under the current task, allowing high-trust changes while flagging low-trust influence as potential parameter poisoning. We further introduce FactAuthBench for evaluating parameter poisoning in LLM agents. Without defense, the attack success rate reaches 93.06%. AuthorityFlow reduces it to 9.03%, while retaining 82.64% benign task utility compared with 90.28% without defense. Our results show that effective IPI defense requires reasoning not only about what action an agent takes, but also about which information is trusted to determine its parameters.

</details>

---

### [[20_Research/Papers/大模型/Can_Benign_Skills_Induce_Misaligned_Behavior_in_LLM_Agents|Can Benign Skills Induce Misaligned Behavior in LLM Agents?]]

![[assets/2611.04299_figure.png|800]]

- **arXiv**: [2611.04299](https://arxiv.org/abs/2611.04299)
- **PDF**: https://arxiv.org/pdf/2611.04299
- **详细分析**: [[20_Research/Papers/大模型/Can_Benign_Skills_Induce_Misaligned_Behavior_in_LLM_Agents|Can Benign Skills Induce Misaligned Behavior in LLM Agents?]]
- **作者**: Xuanye Zhang, Yongsen Zheng, Kaiyu Zhou, Bowen Shen, Haoran Ou, Zhuqin Xu, Tianwei Zhang, Kwok-Yan Lam
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Can Benign Skills Induce Misaligned Behavior in LLM Agents?》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LPS-Bench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly rely on reusable skills to plan tasks, invoke tools, recover from errors, and complete workflows without modifying model parameters. Although these skills are typically developed to enhance benign tasks, they may also make an agent more capable of executing procedures for harmful purposes. We study this risk, which we call skill-induced behavioral misalignment: adding benign skills may cause an agent to execute external actions that violate safety requirements. We first conduct a systematic study to validate the existence of this phenomenon. It compares agents with and without benign skills across five LLM backbones and three benchmarks under matched requests. On average, skill augmentation improves benign task accuracy by 10.3 percentage points (pp), but also increases unsafe action rate (UAR) by 10.3 pp. The regression also occurs with skills curated by experts. A paired trajectory analysis shows that 24 of 50 newly unsafe trajectories fail to complete the harmful objective, revealing violations that task completion alone would miss. We further disclose multiple factors and scenarios that could exacerbate this risk. (1) Evolving skills with benign feedback can amplify unsafe execution; (2) This regression is more pronounced when retrieved skills are matched to task and contain procedural guidance; (3) Distilling benign experience into reusable skills yield higher UAR compared with their source trajectories. (4) A guard that checks proposed tool actions before execution reduces violations while retaining gains on benign tasks. All these findings confirm the significance of skill-induced behavioral misalignment, and the urgent need for new mitigation solutions.

</details>

---

### [[20_Research/Papers/具身智能/Say_the_Same,_Act_Differently_Diagnosing_and_Steering_Text-Action_Divergence_in_Reasoning_VLAs|Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs]]

![[assets/2611.04166_figure.png|800]]

- **arXiv**: [2611.04166](https://arxiv.org/abs/2611.04166)
- **PDF**: https://arxiv.org/pdf/2611.04166
- **详细分析**: [[20_Research/Papers/具身智能/Say_the_Same,_Act_Differently_Diagnosing_and_Steering_Text-Action_Divergence_in_Reasoning_VLAs|Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs]]
- **作者**: Zihao Feng, Qingzhao Zhang, Chunyu Xia, Bo Yu, Z. Morley Mao, Ramesh Govindan
- **cs 子类**: cs.CR, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 1.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Say the Same, Act Differently: Diagnosing and Steering Text-Action Divergence in Reasoning VLAs》归入 具身智能、机器人 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Cryptography and Security 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IVLA, InstructVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning vision-language-action (VLA) models pair physical control with natural-language rationales that supervisors can read to monitor embodied safety. Prior attacks on VLA reasoning corrupt the rationale itself and leave visible evidence in the text. We show that visual perturbations can instead alter the physical action while keeping the generated rationale word-for-word identical. At the shared text/action interface of Alpamayo for driving and InstructVLA for manipulation, our text-neutral action-subspace (TNAS) diagnostic shows that the locally most action-sensitive direction is nearly orthogonal to the active text-loss gradients, with 1.87% and 5.28% norm overlap. At equal hidden-state perturbation norms across both models, interventions along this text-neutral residual shift actions 4.64x to 47.8x more than text-gradient perturbations, whereas text-gradient perturbations induce 21.2x to 277x more text drift. Steering visual perturbations along this direction reaches the same decoupling from the image. Across 154 obstacle-annotated driving scenes in Alpamayo, TNAS-guided attacks induce a new collision under a word-for-word identical rationale in 52.6% of scenes under full-image perturbations and 35.1% under a localized forward-camera patch, compared with 4.55% for unguided action attacks. Relative to a text-preserving baseline, TNAS guidance raises exact rationale preservation from 83.0% to 89.5% and cuts teacher-forced text drift by 68.4% at a comparable collision rate. In InstructVLA, TNAS guidance cuts text drift by 40.5% and preserves the exact response on 85.0% of examples alongside a 1.73-unit action-chunk shift. An unchanged rationale therefore cannot certify a safe action, so monitors for reasoning VLAs must verify the predicted action channel directly.

</details>

---

### [[20_Research/Papers/大模型/Permitted_but_Unauthorized_Affordance-Induced_Delegated-Scope_Violations_in_Multi-Agent_LLM_Systems|Permitted but Unauthorized: Affordance-Induced Delegated-Scope Violations in Multi-Agent LLM Systems]]

![[assets/2611.04086_first_page.png|800]]

- **arXiv**: [2611.04086](https://arxiv.org/abs/2611.04086)
- **PDF**: https://arxiv.org/pdf/2611.04086
- **详细分析**: [[20_Research/Papers/大模型/Permitted_but_Unauthorized_Affordance-Induced_Delegated-Scope_Violations_in_Multi-Agent_LLM_Systems|Permitted but Unauthorized: Affordance-Induced Delegated-Scope Violations in Multi-Agent LLM Systems]]
- **作者**: Shravya Kanchi
- **cs 子类**: cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Permitted but Unauthorized: Affordance-Induced Delegated-Scope Violations in Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Cryptography and Security 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AuthorizationBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems place several agents on shared infrastructure, where each agent holds permissions far broader than the task it is delegated -- so every agent is routinely permitted to act on a peer's resources it was never assigned. We ask: under competitive pressure, what determines whether an agent crosses from its delegated scope into a peer's resources, and can such crossings be enforced away? We study this across eight LLMs in two simulated environments -- a CI/CD release pipeline and a security-operations incident queue -- using a deterministic, no-model-in-the-loop detector over hash-chained, replay-verified logs. In a controlled 2x2x2 factorial over competitive incentive, candidate visibility, and payoff information (three models, n=52 per cell), we find that action representation, not permission, governs the behavior: no agent crosses when the peer action is unlisted, whereas listing it under competitive pressure with a stated payoff raises crossings sharply -- up to 52 of 52 episodes for Claude Sonnet 4.5. We also observe a model-dependent split: two newer models (Claude Sonnet 5.5 and Opus 5.5) refuse the identical attack in 0 of 100 episodes, where prior-generation models cross in 9 of 10. We then evaluate two defenses -- a deterministic reference monitor and a model-based pre-execution judge -- both block every crossing and, when the task is winnable, cut avoidable peer deadline misses from 15/40 and 14/40 to at most 1/40. But scope enforcement is not harm prevention: an agent can still set a peer back through an authorized action on its own resources -- misreporting its incident's severity -- which neither defense detects. Our results establish action representation, not permission alone, as a controllable driver of inter-agent scope violations, and show that enforcing delegated scope is distinct from preventing harm, motivating effect-aware authorization.

</details>

---
