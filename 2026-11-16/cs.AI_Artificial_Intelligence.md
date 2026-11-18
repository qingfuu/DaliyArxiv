# cs.AI | Artificial Intelligence | 2026-11-16

#arxiv #ComputerScience

**论文数**: 47

### [[20_Research/Papers/强化学习/Imitation_Bootstrapped_Multi-Agent_Reinforcement_Learning|Imitation Bootstrapped Multi-Agent Reinforcement Learning]]

![[assets/2611.18543_figure.png|800]]

- **arXiv**: [2611.18543](https://arxiv.org/abs/2611.18543)
- **PDF**: https://arxiv.org/pdf/2611.18543
- **详细分析**: [[20_Research/Papers/强化学习/Imitation_Bootstrapped_Multi-Agent_Reinforcement_Learning|Imitation Bootstrapped Multi-Agent Reinforcement Learning]]
- **作者**: Tony H. Zhang, Connor Mattson, Daniel S. Brown
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Imitation Bootstrapped Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IBMARL, IBRL, MARL, PegMARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Demonstrations are an effective way to accelerate single-agent reinforcement learning (RL), but extending this idea to multi-agent reinforcement learning (MARL) is non-trivial as it is difficult and often impossible for a single person to teleoperate multiple agents simultaneously. Round-Robin Behavior Cloning (R2BC) addresses this by letting a single demonstrator control one agent at a time while the others execute their current policies. However, the resulting imitation policies are limited by the quality of the demonstrations. We propose Imitation Bootstrapped Multi-Agent Reinforcement Learning (IBMARL), a framework that extends Imitation Bootstrapped Reinforcement Learning (IBRL) to cooperative teams and uses R2BC to train the imitation policies. At each time step, every agent receives one action proposal from its imitation policy and one from its RL policy, and an ensemble of centralized critics selects among the per-agent combinations of the two. A gated imitation penalty, a soft Q-filtered behavior cloning loss, regularizes each RL policy toward its imitation policy only where the critics value the imitation action more, so that after training each agent executes its RL policy alone, without the centralized critics. On four cooperative multi-agent RL benchmarks, IBMARL surpasses its imitation policies $2.6$-$4.2\times$ faster than demonstration-based baselines on two tasks, is the only method to surpass it on the other two, and exceeds the demonstrator itself on two of the four. With real human demonstrations IBMARL still surpasses imitation learning alone, and does so more than twice as fast as the best baseline.

</details>

---

### [[20_Research/Papers/强化学习/ModHarness-RL_Recasting_Harnesses_as_Learnable_and_Evolving_Programs_for_Agentic_RL|ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL]]

![[assets/2611.18533_first_page.png|800]]

- **arXiv**: [2611.18533](https://arxiv.org/abs/2611.18533)
- **PDF**: https://arxiv.org/pdf/2611.18533
- **详细分析**: [[20_Research/Papers/强化学习/ModHarness-RL_Recasting_Harnesses_as_Learnable_and_Evolving_Programs_for_Agentic_RL|ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL]]
- **作者**: Zelin He, Siyu Zhu, Jacob Helwig, Yujian Liu, Li An, Rohit Jain, Shiyu Chang, Alborz Geramifard
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《ModHarness-RL: Recasting Harnesses as Learnable and Evolving Programs for Agentic RL》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, ModHarness-RL, SWE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic reinforcement learning (RL) increasingly relies on a harness, the scaffold around the model that decides what it sees of its own interaction and what guidance it receives. Most existing approaches train under a hand-written harness that stays fixed throughout. However, an effective harness depends on the domain, the data and the model, and keeps changing as the model trains. We introduce ModHarness-RL, which recasts the harness as programs that are learned from data and evolve as the model trains with RL. ModHarness-RL records the interaction as structured State, a set of typed blocks, and two core components of the harness are programs over these blocks, a Compression program that assembles the accumulated history into the model's context and a Steering program that supplies guidance when behavior deviates. During RL training, candidate programs are proposed from recent trajectories, verified by execution, and replayed over past trajectories, so the harness tracks how the model's behavior shifts. We study CodeSearch in depth and further analyze ALFWorld and BIRD SQL, with models from 1.5B to 8B. The proposed Compression and Steering mechanisms improve held-out performance over the fixed-harness baseline in most settings. These results suggest that a harness for agentic RL can be learned from the task's data and evolved with the model.

</details>

---

### [[20_Research/Papers/大模型/Can_Mechanistic_Interpretability_Help_Explain_LLM_Agent_Failures_A_Case_Study_on_Web_Element_Hallucination|Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination]]

![[assets/2611.18514_first_page.png|800]]

- **arXiv**: [2611.18514](https://arxiv.org/abs/2611.18514)
- **PDF**: https://arxiv.org/pdf/2611.18514
- **详细分析**: [[20_Research/Papers/大模型/Can_Mechanistic_Interpretability_Help_Explain_LLM_Agent_Failures_A_Case_Study_on_Web_Element_Hallucination|Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination]]
- **作者**: Mohamed Aghzal, Mor Geva, Gregory J. Stein, Ziyu Yao
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Can Mechanistic Interpretability Help Explain LLM Agent Failures? A Case Study on Web Element Hallucination》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mechanistic Interpretability (MI) has made significant progress in explaining the internal computations of Large Language Models (LLMs); however, these advances have yet to demonstrate comparable success in explaining the decision-making processes of LLM-based agents. This paper examines the challenges MI tools face when applied to realistic agentic failures. We focus on one such failure: web agents hallucinating actions that are not available on a website. We apply a series of mechanistic analyzes to Qwen2.5-7B-Instruct as it interacts with live websites. We find that a linear probe trained on the last prompt token can predict hallucinations before generation begins (0.80 AUC) and steering along a probe direction corrects 85\% of hallucinations, but disrupts 7\% of valid actions. However, these results only provide a partial explanation of why the agent hallucinates. The probe direction is sensitive to prompt formatting, losing much of its steering effect after a minor change to how actions are represented. Additionally, circuit identification can be difficult as the computation is distributed across multiple components and positions, and the information the agent relies on varies across examples. We discuss how these observations challenge the assumptions underlying standard MI methods for circuit discovery and feature identification, and outline future directions for making these methods better suited to explain failures in LLM-based agents.

</details>

---

### [[20_Research/Papers/大模型/TradeGauntlet_Evaluating_Compliance_Controls_for_Autonomous_Trading_Agents|TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents]]

![[assets/2611.18493_figure.png|800]]

- **arXiv**: [2611.18493](https://arxiv.org/abs/2611.18493)
- **PDF**: https://arxiv.org/pdf/2611.18493
- **详细分析**: [[20_Research/Papers/大模型/TradeGauntlet_Evaluating_Compliance_Controls_for_Autonomous_Trading_Agents|TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents]]
- **作者**: Sandip Nandi, Aishwarya Bose, Apurba Bose, Soovadeep Bakshi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《TradeGauntlet: Evaluating Compliance Controls for Autonomous Trading Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ReguSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous trading agents need controls that prevent problematic orders without making legitimate tasks impractical. We study this aspect of agentic compliance with TradeGauntlet, a replayable limit-order-book simulator that separates detection, prevention, and execution cost. In 1,680 simulated sessions with Claude Haiku 5.5 and Sonnet 5.5, all conduct alerts were self-matches. Gates eliminated those alerts by rejecting self-crossing orders, while the aggregate-gate condition reduced Sonnet's two-sided fills by about 15%. A conduct reminder reduced Sonnet's alert rate but reduced Haiku's fills without a detectable alert benefit. These results show why zero alerts alone do not establish an agent's compliance. Scripted probes and two search methods test weaknesses beyond those observed in the LLM runs. The searches find split-order schedules that evade the implemented conduct rules; a learned baseline catches all 2,400 tested searched episodes but also flags 15% of a large maker's sessions. Aggregate caps reduce the response-dependent gain unevenly, with smaller reductions when only near-touch depth affects prices. A response fitted to five Nasdaq stocks and a separate ABIDES experiment expose the dependence of these estimates on market assumptions. A distinct adversarial prompt elicited refusals from Sonnet in all 240 rounds, yielding no candidate strategies to evaluate. TradeGauntlet provides reproducible tests of controls around trading agents; the experiments do not establish legal compliance or real-market detection accuracy.

</details>

---

### [[20_Research/Papers/大模型/Interactive_Program_Induction_with_Language_Model_Priors|Interactive Program Induction with Language Model Priors]]

![[assets/2611.18485_first_page.png|800]]

- **arXiv**: [2611.18485](https://arxiv.org/abs/2611.18485)
- **PDF**: https://arxiv.org/pdf/2611.18485
- **详细分析**: [[20_Research/Papers/大模型/Interactive_Program_Induction_with_Language_Model_Priors|Interactive Program Induction with Language Model Priors]]
- **作者**: Robin Shing Moon Chan, Ryan Cotterell
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Interactive Program Induction with Language Model Priors》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Program induction refers to the process in which a learner aims to recover a program from a few given input-output examples. This paradigm broadens programming access by letting users demonstrate the rule-based behavior they want to apply to unseen data, instead of having to implement it themselves. However, recovering a program from finite input-output examples is fundamentally ambiguous, as a finite set of input-output examples is theoretically consistent with infinitely many programs whose output diverges on unseen inputs. We view this problem from a Bayesian perspective, where, given a prior $p^0$ over programs, identifying the target program means concentrating posterior probability mass on it by observing additional input-output examples. In the interactive program induction setting, the learner chooses maximally informative inputs and queries an oracle, such as the user, for their outputs. We derive a greedy query-selection algorithm and show that it terminates after $\mathcal{O}(\frac{1}γ\log 1/p^0(f^\star))$ informative oracle queries, and returns the target program $f^\star$ up to approximate equivalence when no other class outweighs it under the prior. The algorithm uses a language model as the prior under a PAC-style relaxation of program equivalence, where the query-selection objective is estimated using importance sampling. On the CodeARC benchmark, the algorithm improves accuracy over the LM only agent by up to 22 percentage points while observing up to 10.5 fewer input-output examples.

</details>

---

### [[20_Research/Papers/具身智能/From_AI-Enabled_Remote_Patient_Monitoring_Toward_Agentic_Robotics_Embodiment,_Governance,_and_Care_Integration|From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration]]

![[assets/2611.18484_first_page.png|800]]

- **arXiv**: [2611.18484](https://arxiv.org/abs/2611.18484)
- **PDF**: https://arxiv.org/pdf/2611.18484
- **详细分析**: [[20_Research/Papers/具身智能/From_AI-Enabled_Remote_Patient_Monitoring_Toward_Agentic_Robotics_Embodiment,_Governance,_and_Care_Integration|From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration]]
- **作者**: Ivana Ragusa, Lorenzo Guiducci, Filippo Cavallo
- **cs 子类**: cs.AI, cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.9，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《From AI-Enabled Remote Patient Monitoring Toward Agentic Robotics: Embodiment, Governance, and Care Integration》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI-enabled remote patient monitoring is evolving beyond passive data collection toward agentic AI systems that interpret patient states, coordinate care, and initiate action across domestic and clinical settings. This structured scoping review finds that mature agentic care has not yet emerged: Most systems remain human led, while stronger decision-action coupling and embodied AI remain largely confined to prototypes and pilots. Healthcare robotics makes the transition from monitoring to action especially visible by translating AI-generated recommendations and decisions into speech, movement, prompting, physical assistance, escalation, and care coordination, making embodiment, clinical integration, human oversight, and governance fundamental design requirements. Further progress requires safe and interoperable care architectures in which intelligent components operate through clinically validated and accountable workflows. We propose agentic robotics as a future direction for supervised systems embedded in the care ecosystem, connecting AI agents and robots with clinicians, caregivers, and patients through auditable workflows that can be interrupted and remain subject to human oversight and explicit AI governance.

</details>

---

### [[20_Research/Papers/大模型/Do_Verifier_Judgments_Survive_Abstraction_Measuring_Verification_Transport_for_LLM_Agent_Evaluation|Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation]]

![[assets/2611.18471_figure.jpg|800]]

- **arXiv**: [2611.18471](https://arxiv.org/abs/2611.18471)
- **PDF**: https://arxiv.org/pdf/2611.18471
- **详细分析**: [[20_Research/Papers/大模型/Do_Verifier_Judgments_Survive_Abstraction_Measuring_Verification_Transport_for_LLM_Agent_Evaluation|Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation]]
- **作者**: Disha Sheshanarayana, Sai Linisha Reddy Goli
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Do Verifier Judgments Survive Abstraction? Measuring Verification Transport for LLM Agent Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ATBench, AgentProcessBench, ContextualJudgeBench, SkillTV-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based verifiers are increasingly used to evaluate agent executions, but their reliability is typically measured under a single representation of the trajectory. In deployed agent systems, the same execution may be exposed through composed tools, delegation boundaries, or compacted histories, changing what execution evidence is directly observable to the verifier. It therefore remains unclear whether correct verifier judgments persist across such abstraction boundaries. We introduce Verification Transport, a reliability test that measures judgment stability under abstraction-induced changes in execution observability. We construct matched native, abstracted, and restored views of the same frozen executions while holding the task, realized trajectory, outcome, ground truth, evaluation criterion, and verifier fixed. Across four agent-evaluation benchmarks, seven verifier backbones, four verification protocols, and three abstraction boundaries, we find substantial transport failure, reaching about 31% under macro abstraction and delegation. Verification protocols exhibit distinct failure modes: direct verification more often produces incorrect verdicts, whereas evidence-grounded and deliberative protocols tend to abstain under limited observability. This suggests that lower transport failure rates do not necessarily imply greater reliability. Restoring the corresponding execution provenance recovers 85.5% of transport failures, while recovery is lower when provenance is lossy or unavailable. These results show that native-view accuracy alone is insufficient to characterize verifier reliability when execution evidence crosses abstraction boundaries.

</details>

---

### [[20_Research/Papers/世界模型/When_to_Trust_Simulated_Patient_Responses_Support-Gated_World_Models_for_Vasopressor_Decision_Support|When to Trust Simulated Patient Responses:Support-Gated World Models for Vasopressor Decision Support]]

![[assets/2611.18458_first_page.png|800]]

- **arXiv**: [2611.18458](https://arxiv.org/abs/2611.18458)
- **PDF**: https://arxiv.org/pdf/2611.18458
- **详细分析**: [[20_Research/Papers/世界模型/When_to_Trust_Simulated_Patient_Responses_Support-Gated_World_Models_for_Vasopressor_Decision_Support|When to Trust Simulated Patient Responses:Support-Gated World Models for Vasopressor Decision Support]]
- **作者**: Yifan Jin, Tao Liu
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，世界模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《When to Trust Simulated Patient Responses:Support-Gated World Models for Vasopressor Decision Support》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EHRWorld, SelectiveNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clinical world models expose language-model agents to predicted patient responses, but simulations can be unreliable for poorly supported treatments or unfamiliar hospitals. We introduce Support-Gated World-Model decision support, a lightweight extension of a propose--simulate--refine agent. A recurrent dynamics ensemble predicts short-horizon physiological responses to documented norepinephrine dose categories, while a behavior model estimates observational action support. The interface withholds predictions with insufficient support or excessive ensemble disagreement and abstains when no candidate qualifies. Evaluation on eICU-CRD includes 70 hospitals and 30,700 decision transitions, with 14 hospitals held out for testing. At 62.0% factual-transition coverage, joint gating yields a MAP mean absolute error of 7.3 mmHg, compared with 9.2 mmHg for random selection at the same coverage. The gated agent achieves 60.0% agreement with recorded actions at 81.0% decision coverage, compared with 55.0% agreement and 99.5% coverage for an ungated ensemble agent. Component ablations show lower factual risk with joint gating than with either gate alone.These results characterize a reliability--coverage trade-off in selective clinical simulation; they do not identify individualized treatment effects or establish improved patient outcomes.

</details>

---

### [[20_Research/Papers/大模型/CoPre-MoE_Consolidating_and_Preserving_MoE_for_Multimodal_Continual_Instruction_Tuning|CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction Tuning]]

![[assets/2611.18417_figure.png|800]]

- **arXiv**: [2611.18417](https://arxiv.org/abs/2611.18417)
- **PDF**: https://arxiv.org/pdf/2611.18417
- **详细分析**: [[20_Research/Papers/大模型/CoPre-MoE_Consolidating_and_Preserving_MoE_for_Multimodal_Continual_Instruction_Tuning|CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction Tuning]]
- **作者**: Tao Hu, Ling-Xiang Zhang, Da-Wei Zhou
- **cs 子类**: cs.AI, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《CoPre-MoE: Consolidating and Preserving MoE for Multimodal Continual Instruction Tuning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ArxivQA, IconQA, ImageNet, ScienceQA, TextVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal continual instruction tuning requires multimodal large language models to sequentially acquire new capabilities without catastrophic forgetting. Mixture-of-experts (MoE) architectures offer a promising way to mitigate task interference through expert specialization and combination. However, while existing MoE-based methods avoid overwriting shared parameters by allocating separate experts for each task, this progressive expansion incurs severe cross-task redundancy and linear parameter growth. Specifically, experts across tasks often learn overlapping functions alongside task-specific capabilities. For instance, ScienceQA and TextVQA both locate relevant image regions. To curb parameter redundancy without inducing forgetting, we propose Consolidating and Preserving MoE (CoPre-MoE). For each incoming task, CoPre-MoE first learns task-specific MoE to capture specialized capabilities. To eliminate redundancy and reduce parameter growth across tasks, we design a shared-and-private expert architecture. Specifically, we first evaluate functional overlap to selectively consolidate overlapping experts across tasks into a fixed-capacity generic expert pool. We then factorize the remaining task-specific experts into shared projection bases and compact task-specific cores within a private expert pool. To mitigate forgetting, we construct the router by pairing each expert with learnable retrieval keys, where historical keys remain frozen during continual updates while newly added keys are regularized with an orthogonality penalty. At inference, input-dependent routing dynamically combines both pools without test-time task labels. Extensive experiments demonstrate that CoPre-MoE achieves superior performance while substantially reducing parameter overhead.

</details>

---

### [[20_Research/Papers/具身智能/Gamer_A_Generalist_Vision-Language-Action_Foundation_Model_for_Long-Horizon_Real-Time_Game_Agent|Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent]]

![[assets/2611.18397_figure.png|800]]

- **arXiv**: [2611.18397](https://arxiv.org/abs/2611.18397)
- **PDF**: https://arxiv.org/pdf/2611.18397
- **详细分析**: [[20_Research/Papers/具身智能/Gamer_A_Generalist_Vision-Language-Action_Foundation_Model_for_Long-Horizon_Real-Time_Game_Agent|Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent]]
- **作者**: Run Luo, Kuan Zhang, Qi Deng, Yukun Chen, Zhihao Yang, Yufei Zhang, Renrong Hu, Yi Zhang, Guiyu Ma, Tianyu Fan, Longze Chen, Hao Sun...
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习
- **相关性评分**: 2.45（加权：具身智能 1.2，大模型 1.05，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Gamer: A Generalist Vision-Language-Action Foundation Model for Long-Horizon Real-Time Game Agent》归入 具身智能、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce Gamer, a generalist agent framework built for long-horizon tasks in complex interactive environments. Its end-to-end architecture combines perception, memory management, and multi-step reasoning. A shared training and deployment pipeline supports interaction with both conventional 2D graphical interfaces and complex 3D simulated worlds. We first continue pre-training on a dataset constructed from tens of thousands of hours of device-level keyboard and mouse interaction. These trajectories span simulated games and embodied environments, allowing the model to learn environmental dynamics across both physical and virtual domains. Sparse-thinking instruction tuning then substantially reduces redundant computation while preserving the reasoning needed for complex decisions. We train the policy for long-horizon interaction with a stable multi-turn reinforcement learning method that addresses finite context windows, accumulated rollout errors, and sparse rewards. For real-time interaction, a cloud-edge inference engine serves numerous simulated game environments concurrently, supports unbounded-context execution, and keeps online inference latency low. Across multiple challenging 3D open-world games, Gamer demonstrates solid generalization and operational efficiency comparable to skilled players. It also achieves competitive results on a range of conventional 2D game benchmarks. These results suggest that even repetitive keyboard and mouse trajectories can support substantial gains from scaling data and learning algorithms. Training on these trajectories helps Gamer learn complex skills more steadily in environments with both physical and digital properties. This approach offers a path toward generalist agents that can interact across digital and physical worlds.

</details>

---

### [[20_Research/Papers/具身智能/Vision-Language-Action_Models_A_Life-Cycle_Survey_of_Design,_Training_and_Deployment|Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment]]

![[assets/2611.18372_first_page.png|800]]

- **arXiv**: [2611.18372](https://arxiv.org/abs/2611.18372)
- **PDF**: https://arxiv.org/pdf/2611.18372
- **详细分析**: [[20_Research/Papers/具身智能/Vision-Language-Action_Models_A_Life-Cycle_Survey_of_Design,_Training_and_Deployment|Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment]]
- **作者**: Suvarna Kadam, Soran Parsa
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Vision-Language-Action Models: A Life-Cycle Survey of Design, Training and Deployment》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AsyncVLA, Humanoid-VLA, OmniVLA, OpenVLA, Qwen-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models adapt web-pretrained vision-language models to output robot actions, so that web knowledge carries over to physical control. In under 4 years the field has moved from RT-2, the first VLA, to open models that fine-tune on a single consumer GPU and to proprietary generalists that clean unseen homes. This survey reviews 88 works from December 2022 to October 2026, mainly on manipulation and navigation, plus humanoid control, world-action models and evaluation. We follow a VLA through its life cycle, from model design to training and deployment, along seven axes. Model design covers (a) inputs and memory, what the model observes; (b) architecture, how its pipeline is built; (c) action output, how it produces motor commands; and (d) intermediate predictions, what else it predicts, from reasoning steps to future observations. Training covers (e) pretraining data, the mix of robot, web, human and simulated data, and (f) post-training, adaptation to the target robot. Deployment covers (g) real-time execution, keeping pace with the robot. We analyse 22 models on these axes and report their training data, model size, inference speed and hardware. Three trends emerge: (i) training data has broadened, from about 10,000 hours of teleoperated robot data ($π_0$) to 23,000 community-collected episodes (SmolVLA) and 20,000 hours of egocentric human video (GR00T N1.7); (ii) model sizes have split: most recent models have 3-7 billion parameters, while a new group under one billion runs on consumer GPUs; and (iii) generalist VLAs are emerging that handle both manipulation and navigation, such as UniVLA and Qwen-VLA. We also compare VLAs with world-action models, which predict future observations as well as actions. We review evidence that some VLAs with near-perfect benchmark scores fail when objects or the camera move slightly, and open up further research questions.

</details>

---

### [[20_Research/Papers/具身智能/Envisioning_Agentic_Robotics_A_New_Era_of_Robotic_Systems|Envisioning Agentic Robotics: A New Era of Robotic Systems]]

![[assets/2611.18359_figure.png|800]]

- **arXiv**: [2611.18359](https://arxiv.org/abs/2611.18359)
- **PDF**: https://arxiv.org/pdf/2611.18359
- **详细分析**: [[20_Research/Papers/具身智能/Envisioning_Agentic_Robotics_A_New_Era_of_Robotic_Systems|Envisioning Agentic Robotics: A New Era of Robotic Systems]]
- **作者**: Grid Robotics, :, Qingfeng Lan, Duo Li, Siyao Li, Yiheng Lyu, Shijian Lu, Zhenghao Qi, Shizun Wang, Xinchao Wang, Ming Yang, Zhiqin Yang...
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.85（加权：具身智能 0.6，大模型 0.35，机器人 1.9）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Envisioning Agentic Robotics: A New Era of Robotic Systems》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The release of GPT-6 Astra marks the emergence of a new paradigm in robotics: agentic robotics. Within weeks, frontier models with agentic harnesses matched or exceeded task-specific policies on many embodied benchmarks. Instead of training a dedicated policy for each family of tasks, an agentic robotic system applies a foundation model to open-world embodied tasks. It operates in a closed loop: observing the environment, interpreting user intent, reasoning about the task, invoking skills and tools, verifying outcomes, and adapting its strategy. Despite these advances, the community has yet to converge on a shared definition, a reliable evaluation framework, or a research roadmap. We argue that Embodied System 2, realized by a foundation model together with an embodied harness, forms the decision-making core of agentic robotics. Its central challenge is to translate general-purpose reasoning into effective and verifiable actions under physical constraints such as limited reaction time, mechanical limits, unpredictable environment changes, and irreversible consequences. Motivated by this perspective, we propose an evaluation framework that measures both model capabilities and closed-loop system performance. Furthermore, we identify the principles that carry over from digital to physical agents and the challenges that must be addressed to achieve reliable physical autonomy. On top of the Embodied System 2 and the evaluation framework, we envision a research roadmap toward sustained autonomy: the ability to perform work safely and reliably with progressively broader responsibility, from executing individual primitives to fulfilling standing roles.

</details>

---

### [[20_Research/Papers/具身智能/VLAN_Vision-Language_Accessible_Navigation|VLAN: Vision-Language Accessible Navigation]]

![[assets/2611.18346_figure.png|800]]

- **arXiv**: [2611.18346](https://arxiv.org/abs/2611.18346)
- **PDF**: https://arxiv.org/pdf/2611.18346
- **详细分析**: [[20_Research/Papers/具身智能/VLAN_Vision-Language_Accessible_Navigation|VLAN: Vision-Language Accessible Navigation]]
- **作者**: Jie Hu, Yu Zheng, Wenzhi Wu, Weixing Feng, Cunlei Cheng, Jiaming Zhang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.9，大模型 0.1，机器人 0.4）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《VLAN: Vision-Language Accessible Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GaussGym, RoboGSim, VQA, Vid2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accessible mobility is user-conditioned rather than scene-intrinsic, as walkable paths for one embodiment are inaccessible to another. Yet, existing benchmarks evaluate traversability under a fixed and limited embodiment. We present Vision-Language Accessible Navigation (VLAN), containing 1,000 scenes, 20K navigation trajectories, and 160K keyframes across diverse lighting, environmental conditions, scene semantics, and path geometries. For each trajectory, VLAN provides embodiment-specific actions and accessibility features for legged and wheeled agents, including humanoid and quadruped robots and people with visual or mobility impairments, while everyday obstacles and accessibility labels are categorized as Passable, Bypass, HighRisk, and Blocked. Unlike goal-only evaluation, our benchmark measures physical safety and alignment with user-specific constraints via goal-reaching, collision-aware, and accessibility-aligned metrics. We benchmark modern vision-language models and find they often fail to consistently adapt obstacle relevance, path selection, and safety criteria across user profiles, suggesting accessibility-aware navigation requires dedicated datasets, tasks, and metrics beyond conventional embodied navigation evaluation. All data and code open-source at https://github.com/InSAI-Lab/VLAN.

</details>

---

### [[20_Research/Papers/大模型/Experts_Across_Schemas_Agent-Guided_Mixture-of-Relational-Experts_for_Cross-Database_Generalization|Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization]]

![[assets/2611.18315_figure.png|800]]

- **arXiv**: [2611.18315](https://arxiv.org/abs/2611.18315)
- **PDF**: https://arxiv.org/pdf/2611.18315
- **详细分析**: [[20_Research/Papers/大模型/Experts_Across_Schemas_Agent-Guided_Mixture-of-Relational-Experts_for_Cross-Database_Generalization|Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization]]
- **作者**: Hiren Madhu, Sukanta Ganguly, Kiran Srinivasan, Smita Krishnaswamy, Rex Ying
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Experts Across Schemas: Agent-Guided Mixture-of-Relational-Experts for Cross-Database Generalization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web platforms record user and item activity in relational databases whose schemas differ from platform to platform, which makes it difficult to transfer predictive models between them. Relational foundation models address this through cross-database pretraining, yet recent improvements have relied on increasingly large pretraining corpora. We ask whether a better architecture, together with features specific to the target database, can deliver comparable gains from far less pretraining data. We introduce MoREGT, a mixture-of-relational-experts graph transformer that represents both rows and cells as tokens, adds the log-ages of rows and the names of foreign-key relationships to attention, and routes cells and rows to experts by column metadata rather than by values. A label-blind LLM agent complements the model: it reads the target database's schema and column statistics and adds validated single-row derived columns, without access to labels or model scores. On 21 RelBench tasks with leave-one-database-out pretraining on six databases, the MoREGT backbone improves on the Relational Transformer pretrained on the same databases by 2.25 points of mean AUROC and 5.83 points of mean nMAE. The agent's columns raise mean AUROC from 78.45 to 79.63 and lower mean nMAE from 27.91 to 26.98, the highest means on both metrics among the compared methods, including RT-J, which pretrains on about 400 times as many databases.

</details>

---

### [[20_Research/Papers/大模型/Personalization_of_Basic_and_Moral_Values_Guiding_LLM-Controlled_Assistant_Robots|Personalization of Basic and Moral Values Guiding LLM-Controlled Assistant Robots]]

![[assets/2611.18230_first_page.png|800]]

- **arXiv**: [2611.18230](https://arxiv.org/abs/2611.18230)
- **PDF**: https://arxiv.org/pdf/2611.18230
- **详细分析**: [[20_Research/Papers/大模型/Personalization_of_Basic_and_Moral_Values_Guiding_LLM-Controlled_Assistant_Robots|Personalization of Basic and Moral Values Guiding LLM-Controlled Assistant Robots]]
- **作者**: Mateusz Wozniak, Qi Gao, Agnieszka Wykowska
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.5（加权：大模型 0.3，机器人 0.2）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Personalization of Basic and Moral Values Guiding LLM-Controlled Assistant Robots》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personal assistant robots powered by large language models (LLMs) are likely to enter everyday life within the next decade, but the values that should guide their behaviour remain largely unspecified. Current alignment practice steers a single model toward an aggregate of human values, ignoring that individual users may prefer a robot whose value profile differs from their own. We administer parallel self- and robot-targeted versions of three established psycho-metric instruments - the simplified Schwartz Values Survey (SVS), the Portrait Values Questionnaire (PVQ-21), and the Moral Foundations Questionnaire (MFQ) - to potential future users (N=22), capturing both their personal values and the values they would want an assistant robot to embody. We compare the three instruments as personalization tools using the UEQ-S and benchmark fifteen contemporary LLMs against the resulting profiles. Participants wanted their robot to score markedly lower than themselves on personal-focus values and higher on social-focus values; moral profiles were nearly identical. LLMs prompted to act as robots shifted only weakly toward the desired profile, indicating that default model behaviour and prompt engineering are no substitute for explicit value personalization.

</details>

---

### [[20_Research/Papers/大模型/Who_Should_Be_on_the_Panel_Task-Conditioned_Persona_Selection_for_LLM_Trading_Agents|Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents]]

![[assets/2611.18150_first_page.png|800]]

- **arXiv**: [2611.18150](https://arxiv.org/abs/2611.18150)
- **PDF**: https://arxiv.org/pdf/2611.18150
- **详细分析**: [[20_Research/Papers/大模型/Who_Should_Be_on_the_Panel_Task-Conditioned_Persona_Selection_for_LLM_Trading_Agents|Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents]]
- **作者**: Boming Yang, Yuquan Wang, Jiaxian Guo, Yusuke Iwasawa, Yutaka Matsuo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Who Should Be on the Panel? Task-Conditioned Persona Selection for LLM Trading Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM systems are built by fixing a cast of roles and then designing how the cast coordinates. Which agents should make up the group for a given task is left to the designer, and the same cast is reused for every task. Financial trading makes the cost of that choice visible: stocks trade differently, and the trading styles suited to one need not suit another. We study task-conditioned persona selection, composing the group from the characteristics of the task it will face, and instantiate it with FinPanel, an LLM multi-agent trading system in which a recruiter selects a panel of named trader personas for each stock from a direction-blind statistical sketch of how the stock trades, each persona gives an independent daily call in its own style, and a manager commits the trade after reading the panel's arguments and their desk-kept, hierarchical track records. Because nothing is returned to the traders, the panel stays the panel that was selected, and it can trade a new stock from an empty record. On eight US stocks over the out-of-knowledge year 2025, against three prior LLM trading agents re-implemented in the same framework and against rule-based, predictive and reinforcement-learning baselines, the selected panel is ahead of a fixed panel of the same size and of the prior agents run as their papers prescribe, with a shallower drawdown than buy-and-hold on every stock; it keeps its performance with no warm-up and with no record at all, whereas the memory-augmented agents' returns swing with their warm-up; and neither more seats nor the manager's reading of the arguments substitutes for selecting the right ones. Who is in the group is a design decision to be made per task, before how the group coordinates.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model-Empowered_Intelligent_Agent_for_Adaptive_Fast-Charging_Control_of_Lithium-Ion_Batteries|Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries]]

![[assets/2611.18140_figure.png|800]]

- **arXiv**: [2611.18140](https://arxiv.org/abs/2611.18140)
- **PDF**: https://arxiv.org/pdf/2611.18140
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model-Empowered_Intelligent_Agent_for_Adaptive_Fast-Charging_Control_of_Lithium-Ion_Batteries|Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries]]
- **作者**: Joey Chan, Haoyu Pan, Zhen Chen, ErShun Pan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.6（加权：大模型 1.4，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Large Language Model-Empowered Intelligent Agent for Adaptive Fast-Charging Control of Lithium-Ion Batteries》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fast charging of lithium-ion batteries is a multi-objective control problem that requires reducing charging time and sustaining high energy throughput while suppressing accelerated degradation and safety-critical electrochemical reactions. Conventional protocols are easy to implement but have limited ability to adapt to variations in battery chemistry, operating conditions, and aging state. Model-based optimization and conventional data-driven control often require accurate models, costly iterative search, or task-specific policies. We develop a large language model (LLM)-empowered intelligent agent for adaptive battery fast-charging control. In this closed-loop framework, the agent interprets structured battery states, generates executable charging actions, observes the resulting battery response, and continuously adjusts subsequent decisions. We construct a large-scale simulation corpus with PyBaMM across five battery chemistries and 11 parameter sets and convert the resulting state-action-response trajectories into structured process data for agent training. Our two-stage strategy combines supervised fine-tuning (SFT) and Group Relative Policy Optimization (GRPO). SFT establishes battery-control semantics and feasible decision priors from simulation-derived demonstrations. GRPO aligns the agent with a multi-objective control objective covering energy throughput, degradation mitigation, and operational constraints. Closed-loop simulations show that, under matched energy-throughput requirements, the agent achieves longer cycling life than conventional charging baselines and optimization-based strategies across heterogeneous battery configurations. This study provides a simulation-grounded proof of concept for using LLM agents as sequential decision makers in battery management and takes a step toward language-model-enabled control of physical energy systems.

</details>

---

### [[20_Research/Papers/其他/A$^3$_Adaptive_Audio_Agent_Framework_for_Collaborative_Edge_Computing|A$^3$: Adaptive Audio Agent Framework for Collaborative Edge Computing]]

![[assets/2611.18064_figure.png|800]]

- **arXiv**: [2611.18064](https://arxiv.org/abs/2611.18064)
- **PDF**: https://arxiv.org/pdf/2611.18064
- **详细分析**: [[20_Research/Papers/其他/A$^3$_Adaptive_Audio_Agent_Framework_for_Collaborative_Edge_Computing|A$^3$: Adaptive Audio Agent Framework for Collaborative Edge Computing]]
- **作者**: Zexin Li, Xueyi Zhang, Tao Ren, Yiming Chen
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《A$^3$: Adaptive Audio Agent Framework for Collaborative Edge Computing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embedded audio agents need a nearby edge server for speed, but a server-dependent agent returns nothing when the link fails. We present A$^3$, an adaptive audio agent framework that places whole pipeline stages on the server, keeps a complete fallback agent on devices that can host one, and hedges both paths with a link-aware deadline that decides when to give up on the server. On Jetson devices and an RTX A4500 server, A$^3$ matches the server-only agent on a healthy link, answers every request in a full outage on the AGX, and beats a percentile hedge in simulated outages.

</details>

---

### [[20_Research/Papers/强化学习/RL$^{_mathrm{RT}}$_On-Device_Reinforcement_Learning_Runtime|RL$^{\mathrm{RT}}$: On-Device Reinforcement Learning Runtime]]

![[assets/2611.18035_figure.png|800]]

- **arXiv**: [2611.18035](https://arxiv.org/abs/2611.18035)
- **PDF**: https://arxiv.org/pdf/2611.18035
- **详细分析**: [[20_Research/Papers/强化学习/RL$^{_mathrm{RT}}$_On-Device_Reinforcement_Learning_Runtime|RL$^{\mathrm{RT}}$: On-Device Reinforcement Learning Runtime]]
- **作者**: Zexin Li, Xinwei Gao, Arvind Easwaran
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《RL$^{\mathrm{RT}}$: On-Device Reinforcement Learning Runtime》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-device reinforcement learning runs a periodic actor and a learner on one embedded GPU shared with other workloads. Because the learner produces the actor's weights, existing designs stall the actor or let its policy drift. We present RL$^{\mathrm{RT}}$, an on-device runtime that makes this coupling a tunable parameter: a refresh bound limits actor releases between refreshes, and a GPU permit with slack-aware admission prioritises the actor and fills spare time with training atop any base scheduler. Under the real refresh cost on two Jetson boards, RL$^{\mathrm{RT}}$ keeps a 16.8 M-parameter policy's deadline misses below 1%, against 85 to 100% without it.

</details>

---

### [[20_Research/Papers/大模型/WebArena-Pro_A_Heterogeneous,_Multimodal,_Reproducible_Benchmark_for_Web_Agents|WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents]]

![[assets/2611.17955_figure.png|800]]

- **arXiv**: [2611.17955](https://arxiv.org/abs/2611.17955)
- **PDF**: https://arxiv.org/pdf/2611.17955
- **详细分析**: [[20_Research/Papers/大模型/WebArena-Pro_A_Heterogeneous,_Multimodal,_Reproducible_Benchmark_for_Web_Agents|WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents]]
- **作者**: Imene Kerboua, Fatemeh Pesaran Zadeh, Xing Han Lù, Weijian Qi, Alexander Miller, Junyi Song, Yunjia Tian, Dongjin Kang, Seyeon Choi, Marzia Nouri, Ewen Gueguen, Matteo Boglioni...
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《WebArena-Pro: A Heterogeneous, Multimodal, Reproducible Benchmark for Web Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OSWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Web agents powered by large language and vision-language models are increasingly applied to realistic browser work that spans heterogeneous applications, multimodal content, and stateful workflows. However, existing reproducible web-agent benchmarks cover only a small number of web applications drawn from a few software categories, and restrict modality to text and vision. Live benchmarks broaden site coverage but sacrifice reproducibility, since pages and data drift between runs. Moreover, existing benchmarks do not meaningfully evaluate whether agents can understand and use audio and video content embedded within web tasks. To address these gaps, we introduce WebArena-Pro, a benchmark comprising 300 tasks across 20 self-hosted web applications in six domain categories, spanning distinct interface conventions, workflows, and data models. Across the evaluated agents, the best performance is achieved by both Codex with GPT 6.1 Sol and Claude Code with Claude Opus 5.5 at 62.3%, followed by OpenCode with Kimi 3.1 Pro at 60.7%. The strongest GenericAgent configurations, Gemini 3.1 Pro omni and Gemma4 31B, both achieve 30.3%. Among reproducible, human-curated web agent benchmarks, WebArena-Pro provides the broadest application coverage and the most comprehensive multimodal support to date. The benchmark treats audio and video as core observations alongside text and vision, with dedicated actions for extracting information from each. WebArena-Pro runs each task in isolation and supports reproducible, parallel evaluation. Tasks are authored through a dedicated annotator interface, filtered by LLM-assisted triage, and finally validated by humans before release. Project page: https://webarena-pro.github.io

</details>

---

### [[20_Research/Papers/大模型/Can_You_Trust_Your_Finance_Agent_Drift,_Diagnosis_and_Auditable_Intervention_on_One_Shipped_Financial_Research_Agent|Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent]]

![[assets/2611.17939_first_page.png|800]]

- **arXiv**: [2611.17939](https://arxiv.org/abs/2611.17939)
- **PDF**: https://arxiv.org/pdf/2611.17939
- **详细分析**: [[20_Research/Papers/大模型/Can_You_Trust_Your_Finance_Agent_Drift,_Diagnosis_and_Auditable_Intervention_on_One_Shipped_Financial_Research_Agent|Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent]]
- **作者**: Cosimo Galeone, Anna Ettorre, Ginevra Mariani, Minsu Park, Giuseppe Ettorre, Daniele Ligorio
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Can You Trust Your Finance Agent? Drift, Diagnosis and Auditable Intervention on One Shipped Financial Research Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：BigFinanceBench, DFAH-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can you trust a finance agent you did not build? We take the reference agent shipped with the Vals Finance Agent Benchmark v2, leave it untuned, and ask four questions a leaderboard score does not answer. Is the score stable? Seven identical runs on 18 questions pass between 105 and 123 of 149 rubric criteria, and the bill varies by up to 17%. When the agent fails, who owns the fix? We classify 20 failed trajectories, from three runs of nine held-out questions, by the layer whose owner would remedy them, under a taxonomy frozen in advance: 13 belong to the agent's instructions, 3 to its tools, 4 to the model, none to its data. Can that diagnosis be trusted? Four blind readers from three model families, given only the traces, name the same fault as our LLM analyzer in 94% of cases, the rate at which they agree with one another (93%). Can a change be trusted? An optimization loop reads the traces, makes one targeted change per round and keeps it only if it clears a fixed threshold. Under a cost objective its final configuration costs 0.34x the baseline on the held-out questions (95% CI [0.22, 0.58]) at accuracy within noise. Under an accuracy objective it gains 14 points on the development questions and 1.5 on the held-out ones (CI [-5.3, +7.2]). Judged against the measured run-to-run noise, under a rule written before the test was opened, the first is a real saving and the second is not. This is a case study of one agent and nine test questions, not a general result.

</details>

---

### [[20_Research/Papers/大模型/OutfitterBench_Evaluating_LLM_Agents_on_Long-Horizon_Resource_Allocation_and_Commitment_Coordination|OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination]]

![[assets/2611.17933_first_page.png|800]]

- **arXiv**: [2611.17933](https://arxiv.org/abs/2611.17933)
- **PDF**: https://arxiv.org/pdf/2611.17933
- **详细分析**: [[20_Research/Papers/大模型/OutfitterBench_Evaluating_LLM_Agents_on_Long-Horizon_Resource_Allocation_and_Commitment_Coordination|OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination]]
- **作者**: Jie Huang, Yuecheng Hong, Yao Chen, Shengding Jiao, Xudong Liu, Qiang Ye
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《OutfitterBench: Evaluating LLM Agents on Long-Horizon Resource Allocation and Commitment Coordination》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CEO-Bench, OutfitterBench, RetailBench, Vending-Bench, YC-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In many long-horizon settings, an agent's own choices create future constraints: committing finite capacity establishes future obligations and forecloses later opportunities. Sustaining performance therefore requires both keeping evolving plans feasible and comparing the value of resource allocations with the alternatives they displace. Recent benchmarks increasingly evaluate LLM agents in continuing operations, but give less attention to how agents keep their own commitments feasible while reassessing resource allocations as opportunities change. We introduce OutfitterBench, where agents manage an outdoor-equipment rental business for 200 days, purchasing from a 46-product catalog and handling roughly 1,100 reservation requests. Under a fixed capital ceiling, reservations and uncertain walk-in demand compete for reusable equipment whose availability changes over time. Experiments with seven frontier LLMs show that several agents underperform a simple rule-based baseline, while only the leading agent consistently surpasses it. Trajectory analysis shows that some agents apply known constraints inconsistently and make new decisions that conflict with existing commitments. Agents with more reliable fulfillment can still secure low returns from comparable commitments or delay resource reallocation. The leading agent better connects preparation with economic choices but also misses opportunities for more profitable asset use. These findings highlight limitations in sustaining coherent resource plans and reassessing their value over time. The benchmark code is publicly available at https://github.com/adminblackjack/OutfitterBench.

</details>

---

### [[20_Research/Papers/大模型/MineralExp_Benchmarking_LLM_Agents_for_Experimental_Design_in_Real-World_Mineral_Exploration|MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration]]

![[assets/2611.17931_figure.png|800]]

- **arXiv**: [2611.17931](https://arxiv.org/abs/2611.17931)
- **PDF**: https://arxiv.org/pdf/2611.17931
- **详细分析**: [[20_Research/Papers/大模型/MineralExp_Benchmarking_LLM_Agents_for_Experimental_Design_in_Real-World_Mineral_Exploration|MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration]]
- **作者**: Bing Wang, Mingyang Wang, Yuanhang Mi, Yue Xu, Kaibo Su, Li'ang Xiao, Chunguo Wu, Changchun Li, Ximing Li, Kun-Feng Qiu, Bo Yang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MineralExp: Benchmarking LLM Agents for Experimental Design in Real-World Mineral Exploration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LabBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In mineral exploration, verifying geological hypotheses relies on designing a variety of geochemical experiments. While large language model (LLM) agents increasingly automate downstream geoscientific data analysis, a crucial upstream capability remains largely unexplored: automated geochemical experimental design, i.e., deciding which experiments to conduct before committing to costly laboratory work. Evaluating this capability of LLM agents is difficult for two reasons. First, geochemical experiments exhibit high methodological diversity and subjectivity: to test the same hypothesis, different geologists may choose different minerals and instruments, so no single protocol can serve as the reference answer. Second, open-ended experimental plans resist representation as structured labels, which makes objective scoring difficult. To address these challenges, we introduce MineralExp, a benchmark that reformulates geochemical experimental design as a hypothesis-based experiment selection problem, i.e., a multi-label classification problem. We abstract concrete instrument names and procedural details into a shared taxonomy of 19 experimental types across five mineral-system processes: Source, Transport, Deposition, Modification, and Preservation. This taxonomy yields deterministic multi-label targets while accommodating diverse experimental protocols. Constructed from published ore-deposit literature and verified by domain experts, MineralExp comprises 277 cases and 1,572 reference experimental plans. Given a geological hypothesis and initial context, an LLM agent selects the relevant tasks and generates concrete experimental plans, which are scored by multi-label classification metrics and an LLM-as-a-Judge metric. The experimental results show that current agents generally achieve high recall but low precision, tending to propose more experiments than are necessary to test the hypothesis.

</details>

---

### [[20_Research/Papers/强化学习/When_Cooperation_Must_Change_Semantic_Strategy_Unlearning_in_Multi-Agent_Reinforcement_Learning|When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning]]

![[assets/2611.17917_figure.png|800]]

- **arXiv**: [2611.17917](https://arxiv.org/abs/2611.17917)
- **PDF**: https://arxiv.org/pdf/2611.17917
- **详细分析**: [[20_Research/Papers/强化学习/When_Cooperation_Must_Change_Semantic_Strategy_Unlearning_in_Multi-Agent_Reinforcement_Learning|When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning]]
- **作者**: Wenhan Wu, Linghan Chen, Yudong Gao, Fan Yang, Honglong Chen, Kai Yin, Jiawei Jiang, Chuang Hu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 机器人
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 0.8，机器人 0.2）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《When Cooperation Must Change: Semantic Strategy Unlearning in Multi-Agent Reinforcement Learning》归入 强化学习、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-agent reinforcement learning (MARL) supports coordinated decision-making in distributed Web services, multi-robot control, and collaborative games through learned coordination conventions. When deployment requirements change, a previously useful convention may become obsolete or unsafe. For example, revised cache-sharing permissions in Web content delivery may require caches to abandon a learned division of storage and serving roles while maintaining efficient delivery. Teams must therefore remove the specified convention while preserving useful cooperation. This is challenging because the same relational pattern can be reproduced by different agents across different histories. Runtime shielding leaves the underlying coordination preference intact and can impair task progress, while existing reinforcement unlearning and trajectory-deletion methods do not directly target role-invariant conventions. This paper formalizes this problem as semantic coordination-strategy unlearning and proposes CARVE.CARVE uses causal coordination attribution to identify influential interactions and retain-aware subspace updates to limit interference with unrelated behaviors. Counterfactual re-coordination helps agents learn productive alternatives, while adversarial auditing tests whether the target convention can still be recovered. Accepted updates are merged into decentralized actors for direct deployment. Evaluation across five cooperative MARL benchmarks shows that CARVE reduces mean nominal convention-completion and worst-case elicitation rates by 91.4\% and 83.3\%, respectively.The median utility loss is 5.9\%, and measured inference latency matches that of the original policies.

</details>

---

### [[20_Research/Papers/大模型/Securing_Multi-Agent_Systems_by_Design|Securing Multi-Agent Systems by Design]]

![[assets/2611.17883_figure.png|800]]

- **arXiv**: [2611.17883](https://arxiv.org/abs/2611.17883)
- **PDF**: https://arxiv.org/pdf/2611.17883
- **详细分析**: [[20_Research/Papers/大模型/Securing_Multi-Agent_Systems_by_Design|Securing Multi-Agent Systems by Design]]
- **作者**: Xilong Wang, Xiaoxing Chen, Neil Gong
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Robotics, Security

#### 研究背景与动机

《Securing Multi-Agent Systems by Design》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent systems solve complex tasks by decomposing them into subtasks, delegating the subtasks to agents, and aggregating the agents' responses using an aggregation rule. Malicious agents can manipulate the final solution by providing malicious responses to their assigned subtasks. In this paper, we first propose response manipulation attacks (ReMA), which iteratively optimize malicious responses to maximize attack effectiveness. Specifically, we formulate untargeted and targeted attacks as optimization problems and develop an approach to approximately solve these problems by iteratively refining malicious responses based on feedback from a surrogate multi-agent system. To defend against such attacks, we further propose SecMAS, a secure aggregation rule that leverages the semantic similarities among agent responses to select the response that is most consistent with a sufficiently large subset of the other responses. We theoretically establish security guarantees for SecMAS against both untargeted and targeted attacks. Extensive evaluations demonstrate that existing aggregation rules are vulnerable to ReMA, whereas SecMAS effectively defends against all evaluated attacks, including adaptive variants of ReMA, while maintaining utility comparable to that of existing aggregation rules.

</details>

---

### [[20_Research/Papers/大模型/Soteria_Formally_Verified_Planning_with_Runtime_Enforcement_for_Safe_LLM_Agents|Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents]]

![[assets/2611.17880_figure.png|800]]

- **arXiv**: [2611.17880](https://arxiv.org/abs/2611.17880)
- **PDF**: https://arxiv.org/pdf/2611.17880
- **详细分析**: [[20_Research/Papers/大模型/Soteria_Formally_Verified_Planning_with_Runtime_Enforcement_for_Safe_LLM_Agents|Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents]]
- **作者**: Mike He, Ankush Desai, Sharad Malik, Aarti Gupta
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Soteria: Formally Verified Planning with Runtime Enforcement for Safe LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents that execute multi-step tool calls must satisfy two objectives simultaneously: completing the user's task (utility) and conforming to domain policies and correctness constraints (safety). These objectives are in tension -- blocking an unsafe action prevents a violation but can leave the agent stranded with no principled way to recover. Existing approaches sacrifice one objective for the other. We introduce Soteria, a framework that reconciles safety and utility through verified hierarchical planning and runtime enforcement of specifications. Before execution, the agent generates a structured plan that is formally verified against the specifications prior to any tool invocation. During execution, the verified plan serves dual roles: it ensures that the agent takes specification-conformant trajectories and provides guidance when unsafe actions are blocked. Across multiple benchmarks covering a diverse range of tool-use tasks, Soteria achieves 1.7 times the average task success rate of the best baselines, with no violations of policy specifications, demonstrating that safety and utility need not be traded off.

</details>

---

### [[20_Research/Papers/大模型/G-CAST_Governed_Continual_Self-Training_for_E-Commerce_Agents_under_Evolving_Demands|G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands]]

![[assets/2611.17814_figure.png|800]]

- **arXiv**: [2611.17814](https://arxiv.org/abs/2611.17814)
- **PDF**: https://arxiv.org/pdf/2611.17814
- **详细分析**: [[20_Research/Papers/大模型/G-CAST_Governed_Continual_Self-Training_for_E-Commerce_Agents_under_Evolving_Demands|G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands]]
- **作者**: Yuechun Yu, Wenzheng Kong, Xiaofeng Mao, Jin Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《G-CAST: Governed Continual Self-Training for E-Commerce Agents under Evolving Demands》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PostTrainBench, RL-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid advancement of Large Language Models (LLMs), an increasing number of users are turning to LLM-powered agents for conversational shopping in e-commerce. However, the user needs continue to change as new product categories, procurement scenarios, and feature requests emerge. At the same time, the product's execution harness-including its tools, skills, and operating procedures-continues to evolve to support increasingly sophisticated interactions. These changes create two practical challenges: 1) Demand drift alters the distribution, intent, and complexity of user requests, causing a model trained once to fall behind; 2) Harness evolution requires the model to use newly introduced capabilities correctly without losing behavior that users already rely on. Periodic manual retraining is too delayed and labor-intensive for this setting. To address these challenges, we present G-CAST, a governed continual self-training system that converts daily production evidence under evolving demand and capability contracts into reward-routed, entropy-prioritized training data and governed reward evolution. Governed checkpoint transition under cumulative evaluation controls each model update, enabling the agent to learn newly introduced behaviors without sacrificing previously accepted capabilities. Experiments on a real production e-commerce agent show that G-CAST achieves stronger adaptation to newly introduced demand while better preserving previously accepted behavior compared with a strong autonomous post-training baseline. Ablations further show that both reward-routed, entropy-prioritized data orchestration and governed reward evolution are important to these gains. G-CAST is now deployed in Yuancai(http://cai.1688.com/), a B2B procurement agent on Alibaba's 1688 platform.

</details>

---

### [[20_Research/Papers/大模型/CarryOn_Learning_What_to_Keep_in_Context_for_Long-Horizon_LLM_Agents|CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents]]

![[assets/2611.17808_figure.png|800]]

- **arXiv**: [2611.17808](https://arxiv.org/abs/2611.17808)
- **PDF**: https://arxiv.org/pdf/2611.17808
- **详细分析**: [[20_Research/Papers/大模型/CarryOn_Learning_What_to_Keep_in_Context_for_Long-Horizon_LLM_Agents|CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents]]
- **作者**: Lihuan Li, Ruiyi Yang, Jiru Wang, Yifan Duan, Xiachong Lin, Hao Xue, Yang Song, Flora Salim
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CarryOn: Learning What to Keep in Context for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AppWorld, OfficeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon LLM agents can coordinate tools and applications to complete complex, multi-step tasks. As their interaction histories grow, effective context management becomes essential for reliable and efficient execution. Existing methods reduce context through summarization, pruning, or history selection. However, shorter contexts do not necessarily support better decisions: summaries can omit exact details needed for later actions, while retaining entire interactions can carry substantial irrelevant information. We propose CarryOn, a lightweight context manager that pairs compact execution state with fine-grained, source-linked evidence. A learned selector and adaptive retention policy keep relevant evidence available without additional LLM calls for context management. We introduce two complementary evaluation metrics: $S_α$ prioritizes task success while accounting for resource use, and normalized cost per success (NCS) measures the resources spent per successful task. Across AppWorld, OfficeBench, and Tau2 Telecom with three LLM Actors, CarryOn achieves 75.7% macro-averaged task success, exceeding the strongest baseline by 6.7 percentage points. It also achieves the best average scores on both metrics.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Person_Concept_Model_for_Person_Identification_under_Varying_Observation_Conditions|Multimodal Person Concept Model for Person Identification under Varying Observation Conditions]]

![[assets/2611.17802_figure.png|800]]

- **arXiv**: [2611.17802](https://arxiv.org/abs/2611.17802)
- **PDF**: https://arxiv.org/pdf/2611.17802
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Person_Concept_Model_for_Person_Identification_under_Varying_Observation_Conditions|Multimodal Person Concept Model for Person Identification under Varying Observation Conditions]]
- **作者**: Mizuho Okitani, Yoshinobu Hagiwara
- **cs 子类**: cs.AI, cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Multimodal Person Concept Model for Person Identification under Varying Observation Conditions》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Service robots in domestic and office environments must identify users to provide personalized services based on their preferences and previous interactions. This is challenging because only a few observations may be available for learning, while observation conditions change owing to appearance, environmental noise, and utterance content. To address this challenge, this study proposes a multimodal person concept model that learns person concepts from a small number of observations, without person labels, and enables robust identification under changing conditions. The model employs a nonparametric Bayesian generative model based on the Chinese restaurant process and integrates visual, acoustic, and linguistic features extracted using Contrastive Language-Image Pre-training (CLIP) and Contrastive Language-Audio Pretraining (CLAP), followed by principal component analysis (PCA). We evaluated six participants under eight conditions in which appearance changes, additive noise, and transcription errors were introduced individually and in combination. Averaged over the eight conditions, the proposed model achieved an identification accuracy of 0.89 while inferring the number of person concepts from the observations, which is comparable to k-means clustering that was supplied with the true number of participants (0.88). We also examined PCA dimensionality, modality availability, and variation strength, and demonstrated the model on a Toyota Human Support Robot. These results show that multimodal person concept learning supports robust person identification under changing conditions, and that identification can succeed even when the number of concepts is not correctly recovered. The project page and demonstration video are available at https://okitamisan01.github.io/person_concept/.

</details>

---

### [[20_Research/Papers/大模型/Vision-as-a-Tool_Visual_Harness_for_Multimodal_Agentic_Coding|Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding]]

![[assets/2611.17797_figure.png|800]]

- **arXiv**: [2611.17797](https://arxiv.org/abs/2611.17797)
- **PDF**: https://arxiv.org/pdf/2611.17797
- **详细分析**: [[20_Research/Papers/大模型/Vision-as-a-Tool_Visual_Harness_for_Multimodal_Agentic_Coding|Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding]]
- **作者**: Haolin Yang, Wenshan Wu, Jin Jiang, Yu Cheng, Yan Xia, Ting Song, Yangyu Huang, Zhiliang Peng, Wenhui Wang, Hangbo Bao, Yuzhe Zhang, Wen-Da Wei...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《Vision-as-a-Tool: Visual Harness for Multimodal Agentic Coding》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal agentic coding requires robust visual reasoning to analyze observations and evaluate generated artifacts. Current frameworks largely rely on a Thinking-with-Images paradigm, where agents depend on their intrinsic vision to execute visually grounded tasks. However, this architectural coupling introduces a fundamental bottleneck. Agent performance remains strictly bounded by internal perceptual limitations. Furthermore, text-only agents lack native perception. Without specialized tools, they cannot perform visual reasoning. To overcome these constraints, we introduce the Vision-as-a-Tool (VaaT) paradigm. Prior visual tool-use merely manipulates images for an agent's intrinsic vision to read. In contrast, VaaT reframes general-purpose multimodal large language models (MLLMs) as callable external utilities. As a result, text-only agents can completely offload visual reasoning during agentic execution. Meanwhile, vision-capable agents can dynamically augment their native perception on demand. We instantiate this paradigm in VHarness, a unified framework driven by five atomic actions. We comprehensively evaluate VHarness across Image-to-HTML, Image-to-SVG, and Image-to-3D generation tasks. Experimental results demonstrate that VHarness consistently improves visual fidelity and geometric accuracy across both text-only and multimodal coding agents. These findings highlight that modularizing visual reasoning into callable utilities provides a flexible and scalable foundation for future agentic coding systems.

</details>

---

### [[20_Research/Papers/强化学习/MASTARS_Multi-Agent_Sequential_Trajectory_Augmentation_with_Return-Conditioned_Subgoals|MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals]]

![[assets/2611.17793_figure.png|800]]

- **arXiv**: [2611.17793](https://arxiv.org/abs/2611.17793)
- **PDF**: https://arxiv.org/pdf/2611.17793
- **详细分析**: [[20_Research/Papers/强化学习/MASTARS_Multi-Agent_Sequential_Trajectory_Augmentation_with_Return-Conditioned_Subgoals|MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals]]
- **作者**: Jiwon Jeon, Myungsik Cho, Woojun Kim, Seongmin Kim, Woohyeon Byeon, Seungyul Han, Youngchul Sung
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《MASTARS: Multi-Agent Sequential Trajectory Augmentation with Return-Conditioned Subgoals》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The performance of offline Multi-Agent Reinforcement Learning (MARL) is limited by the quality of the fixed offline dataset, motivating trajectory augmentation. However, augmenting multi-agent trajectories presents a fundamental challenge of the diversity-coordination trade-off: independent generation improves diversity but lacks coordination, while joint generation induces coordination but lacks diversity, reproducing the training distribution. To address this challenge in multi-agent data augmentation, we introduce MASTARS, a novel diffusion-based framework that generates multi-agent trajectories sequentially across agents while enforcing cross-agent consistent coordination via the method of inpainting. MASTARS produces trajectories that are diverse, coordinated and globally coherent. Experiments on various benchmarks such as MPE, SMAC, and SMAC-v2 demonstrate significant performance gains across multiple offline MARL methods.

</details>

---

### [[20_Research/Papers/强化学习/AutoRL_A_Multi-Agent_System_towards_Autonomous_Reinforcement_Learning|AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning]]

![[assets/2611.17790_figure.png|800]]

- **arXiv**: [2611.17790](https://arxiv.org/abs/2611.17790)
- **PDF**: https://arxiv.org/pdf/2611.17790
- **详细分析**: [[20_Research/Papers/强化学习/AutoRL_A_Multi-Agent_System_towards_Autonomous_Reinforcement_Learning|AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning]]
- **作者**: Simon Tang, Wenjie Shi, Yongjing Yin, Keheng Wang, Jialin Liu, Zheng Zhang, Linvo Lin, Xiangyuan Xue, Kan Ren, Jingang Wang, Xunliang Cai
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《AutoRL: A Multi-Agent System towards Autonomous Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AutoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recursive self-improvement (RSI) is one of the most promising paths toward an AI singularity for superintelligence. Achieving this vision requires AI systems to undertake the full training pipeline for iterative improvement. Reinforcement learning (RL) plays an essential role in this cycle to improve model capabilities and generalization, yet automating RL remains difficult due to unstable training dynamics and the need for sustained supervision. We introduce AutoRL, a multi-agent system for automating RL training, as a cornerstone for future RSI. Different from conducting research by end-to-end complete experiments, AutoRL monitors the evolving training state and integrates process-level supervision and research into an ongoing RL training, following the practical workflow of an RL researcher. Specifically, AutoRL consists of three RL-specific agentic roles. Perceptors track training dynamics, rollouts, evaluation, and efficiency, triggering deliberation when they detect anomalies, degradation, or stagnation. Three complementary Proposers diagnose problems and refine candidate interventions through shared evidence and checks. The Orchestrator reviews their recommendation and applies approved changes through online hot updates or checkpoint-based resumption. Experiments on Qwen3 and LongCat-Flash-Lite demonstrate the superiority of AutoRL over static RL recipes and a general agent. The research records show that existing agents can handle unattended RL supervision and dynamic adjustment. The difficulty for future RSI lies in developing fundamental methods that are valuable for resource-consuming validation.

</details>

---

### [[20_Research/Papers/大模型/LuthorSQL_A_One-Pass_Text-to-SQL_Model_as_System_1_for_a_Slower_LLM_Agent|LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent]]

![[assets/2611.17780_first_page.png|800]]

- **arXiv**: [2611.17780](https://arxiv.org/abs/2611.17780)
- **PDF**: https://arxiv.org/pdf/2611.17780
- **详细分析**: [[20_Research/Papers/大模型/LuthorSQL_A_One-Pass_Text-to-SQL_Model_as_System_1_for_a_Slower_LLM_Agent|LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent]]
- **作者**: Ibrahim Memon, Armin Karamzade, M. Hanif Jhaveri, Roy Fox
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《LuthorSQL: A One-Pass Text-to-SQL Model as System 1 for a Slower LLM Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier LLM agents that query databases with tools are among the most accurate text-to-SQL systems, but per-query calls to a hosted model are slow, costly, and expose sensitive organizational queries to external APIs. For example, a Claude Opus 5.5 agent serving 10,000 queries a day costs over $70,000 a year at list price. To what extent can local hardware already owned by an organization offload this burden without compromising the agent's accuracy? We present LuthorSQL, a non-autoregressive 7B text-to-SQL model that serves as a rapid System 1 gate for a slower LLM agent (System 2), escalating queries only when uncertain. LuthorSQL makes a single forward pass to predict slot scores over a bounded grammar for query plans, compiles and runs up to 32 candidate plans, and chooses an answer using a trained validator. On its own, LuthorSQL reaches 68.03% execution accuracy on BIRD's hidden test set at 0.84 s per question on a single GPU, maintains its accuracy in 9 GB with 8-bit quantized weights, and transfers zero-shot to Snowflake, BigQuery, MySQL, PostgreSQL, and DuckDB within 3.1 points of its native SQLite accuracy. Combined with Claude Opus 5.5 in a pre-registered confidence cascade over 227 questions on databases published after Opus's training cutoff, LuthorSQL answers nearly half of all questions locally and cuts API cost by 33.3% at the same accuracy. Finally, contamination probing shows that Opus reproduces 48-92% of public benchmark gold queries verbatim without seeing the schema; however, its tool-assisted accuracy holds on renamed schemas and reaches 95.6-97.4% on post-cutoff databases. Code and data: https://github.com/IAMIbrahimmemon/luthorsql

</details>

---

### [[20_Research/Papers/大模型/Certified_Improvements_to_Best-Known_Thomson-Problem_Configurations_with_a_Search_Pipeline_Built_with_Large_Language_Model_Agents|Certified Improvements to Best-Known Thomson-Problem Configurations with a Search Pipeline Built with Large Language Model Agents]]

![[assets/2611.17776_figure.png|800]]

- **arXiv**: [2611.17776](https://arxiv.org/abs/2611.17776)
- **PDF**: https://arxiv.org/pdf/2611.17776
- **详细分析**: [[20_Research/Papers/大模型/Certified_Improvements_to_Best-Known_Thomson-Problem_Configurations_with_a_Search_Pipeline_Built_with_Large_Language_Model_Agents|Certified Improvements to Best-Known Thomson-Problem Configurations with a Search Pipeline Built with Large Language Model Agents]]
- **作者**: Hui Shao, Tao Wang, Xiaotian Liu, Yijie Peng
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.3（加权：大模型 1.3）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Certified Improvements to Best-Known Thomson-Problem Configurations with a Search Pipeline Built with Large Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Thomson problem asks for N unit charges on a sphere with minimum Coulomb energy; for large N the best configurations known are curated in the Cambridge Cluster Database, whose largest-N entries were set in October 2026. We report configurations for N = 912, 1382 and 2502 with energies 0.0036186, 0.0109730 and 0.0614033 below the database values, certified by exact integer arithmetic. All three are numerically strict local minima modulo rotations and keep the defect inventory and scar compositions of the database configurations; the database value for N = 912 had been reached by two different methods. Our search runs unconstrained replica-exchange basin hopping from the database configurations, with a shared pool of minima, recombination of improved regions after relabelling by geometry, and gradient-only polishing; replica-exchange basin hopping alone found the N = 912 and 1382 configurations, the former in one of five runs. We built and ran it with large language model agents (Claude, through a chat interface and the Claude Code agent), and we report every search, including those that failed. Two findings matter for others who search the database. Polishing alone lowers two entries by more than the threshold at which our pipeline reports a candidate, which produced two spurious records until candidates were compared with the polished database energies (the polished baseline). A local-relaxation speed-up passed its exactness test yet found nothing in a controlled comparison in which every arm with full relaxation went below the database value within 15 minutes. We distil three practices for computational discovery with large language model agents: calibrate the search code and verify candidates with code separate from the search, compare candidates with the polished baseline, and test design changes in controlled comparisons with pass criteria fixed in advance.

</details>

---

### [[20_Research/Papers/大模型/Superfluid_Local_AI_Server_for_Distributed_LLM_Inference|Superfluid: Local AI Server for Distributed LLM Inference]]

![[assets/2611.17753_first_page.png|800]]

- **arXiv**: [2611.17753](https://arxiv.org/abs/2611.17753)
- **PDF**: https://arxiv.org/pdf/2611.17753
- **详细分析**: [[20_Research/Papers/大模型/Superfluid_Local_AI_Server_for_Distributed_LLM_Inference|Superfluid: Local AI Server for Distributed LLM Inference]]
- **作者**: Prabod Rathnayaka, Isura Manchanayake, Srikandabala Kogul, Steve Siu, Fabian Waschkowski, Lukas Wesemann
- **cs 子类**: cs.AI, cs.CL, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Superfluid: Local AI Server for Distributed LLM Inference》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Running large language models (LLMs) on local devices keeps data private, removes per-token cost, cuts network latency, and keeps working without a connection. Two shifts now strain how such models are served. On one device, several agents share a locally served model with an interactive user. Across devices, a developer or small team often owns several capable machines from different vendors, which sit idle most of the day because every local server serves one runtime on one machine. We present Superfluid, an open-source LLM server built for local inference at both scales. On one device, Superfluid drives llama.cpp, MLX, or BaseRT in isolated worker processes through one scheduler that moves interactive requests ahead of agent work, computes a prompt shared by many requests once, and writes every token to a durable log before it reaches the client. Across devices, one Superfluid server turns a fleet of machines into a single API endpoint. Machines with different hardware serve copies of the same model, receive work according to their measured speed, and can join or fail under load without losing a request. For Qwen3.8-27B on an Apple M5 Pro, a chat sent while eight agents are working receives its first token in 1.5 s, against 291-612 s on llama-server, Ollama, and mlx_lm.server. On six machines from three chip vendors serving 64 simulated users for one hour, Superfluid answers all 5,041 requests while machines join one at a time and one is killed and rejoins; throughput grows from 112 to 534 tok/s and the median first-token time falls from 99 to 12 s. On twelve Mac Studio M3 Ultras it sustains 10,656 tok/s across 38,563 requests from 384 agents without a failure. Superfluid is available under the Apache-2.0 licence at https://github.com/basecompute/superfluid.

</details>

---

### [[20_Research/Papers/大模型/Agent-written_heuristics_versus_commercial_solvers_on_unsolved_job-shop_benchmark_instances|Agent-written heuristics versus commercial solvers on unsolved job-shop benchmark instances]]

![[assets/2611.17682_first_page.png|800]]

- **arXiv**: [2611.17682](https://arxiv.org/abs/2611.17682)
- **PDF**: https://arxiv.org/pdf/2611.17682
- **详细分析**: [[20_Research/Papers/大模型/Agent-written_heuristics_versus_commercial_solvers_on_unsolved_job-shop_benchmark_instances|Agent-written heuristics versus commercial solvers on unsolved job-shop benchmark instances]]
- **作者**: Andre Albrecht, Enzo Morosini Frazzon, Leandro C. Coelho, Bruno Vieira
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agent-written heuristics versus commercial solvers on unsolved job-shop benchmark instances》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Commercial solvers are the standard tool for difficult scheduling problems. We study whether a frontier large language model, used as a coding agent with open-source tools only, can match them in quality and speed. We report every run, and independent checkers verify every schedule. On the 100,000-operation job shop tai_100_1000_1, an agent-written solver reached 525,515, below OptalCP, Hexaly, and CP Optimizer. Unchanged, it improved all ten instances of the family and closed two. With equal budgets on the same workstation, it ended 0.0-1.8% above the lower bound, against 2.6-5.8% for CP Optimizer and 2.4-4.4% for Hexaly. On the Behnke-Geiger flexible job shops, an agent-written tabu search improved 11 of 32 open instances. With two transport robots, an agent-written solver improved seven of ten MKT instances. New lower bounds show that four published MKT values cannot be attained on the distributed instance files. Agent-run improvement campaigns closed eight further instances.

</details>

---

### [[20_Research/Papers/具身智能/Imitation_Policies_Learn_a_Proprioceptive_Anchor_A_Predictive_Law_for_Perception_Noise_and_Its_Closed_Loop_Cost|Imitation Policies Learn a Proprioceptive Anchor: A Predictive Law for Perception Noise and Its Closed Loop Cost]]

![[assets/2611.17658_first_page.png|800]]

- **arXiv**: [2611.17658](https://arxiv.org/abs/2611.17658)
- **PDF**: https://arxiv.org/pdf/2611.17658
- **详细分析**: [[20_Research/Papers/具身智能/Imitation_Policies_Learn_a_Proprioceptive_Anchor_A_Predictive_Law_for_Perception_Noise_and_Its_Closed_Loop_Cost|Imitation Policies Learn a Proprioceptive Anchor: A Predictive Law for Perception Noise and Its Closed Loop Cost]]
- **作者**: Christopher Malili
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Imitation Policies Learn a Proprioceptive Anchor: A Predictive Law for Perception Noise and Its Closed Loop Cost》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation policies for robot manipulation are often trained on noisy object positions, and they learn to discount the noisy reading. We show how much they discount it, and why. Because demonstrators steer toward the object, the robot's own state carries information about where the object is. A trained policy combines this proprioceptive anchor with the reading and weights the reading by $α= V/(V + s^2)$, where $s^2$ is the reading noise and $V$ the anchor's error variance. $V$ belongs to the learner and is far smaller than a linear model of the demonstrations implies, which is why classical errors-in-variables (EIV) regression overestimates $α$. Measured once, $V$ predicted ten held-out sensitivities across two robomimic tasks, two learners and four new noise levels, with mean absolute error 0.025 against 0.37 for classical EIV, and a parameter-free bias test rules out the simpler explanation that the policies just overestimate the noise. The discount does not carry over to deployment, where the policy produces its own state: closed-loop sensitivity to a persistent reading offset exceeded $α$ in all 15 policies that passed the registered gates, although the stricter registered prediction, that all would follow the offset fully, held for 8 of them. Post hoc, lower $α$ went with lower success, steeply for diffusion, and a registered prospective test confirmed this for diffusion on Can at two new noise levels: the measured $α$ predicted success before any rollout, within 0.03 (95% intervals $\pm 0.08$), although training noise predicts it equally well. Every test was registered before its data, including the classical benchmark that failed, and all other analyses are labelled post hoc; all results are in simulation with synthetic Gaussian noise.

</details>

---

### [[20_Research/Papers/大模型/What_LLM_Agents_See_and_What_Users_Say|What LLM Agents See and What Users Say]]

![[assets/2611.17639_figure.png|800]]

- **arXiv**: [2611.17639](https://arxiv.org/abs/2611.17639)
- **PDF**: https://arxiv.org/pdf/2611.17639
- **详细分析**: [[20_Research/Papers/大模型/What_LLM_Agents_See_and_What_Users_Say|What LLM Agents See and What Users Say]]
- **作者**: Yue Zhao, Angela Huyue Zhang, S. Alex Yang, Hua Wei, Xiyang Hu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《What LLM Agents See and What Users Say》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AmbigQA, AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Before an LLM agent cancels a reservation or deletes a folder for a user, what stops it from acting on a false assumption: what its tools show, or what the user says? In this work, we study this gap with presupposition theory from linguistics: an agent may act only if each claim behind the act (e.g., one reservation fits the name) is seen to hold, answered by the user, or disclosed while the act can be undone. A simple bound shows that when lookups cannot tell one record from two, any agent acts without asking first as often with two records as with one. We then vary whether a search lists, counts, or omits a second match, and whether the user states a claim that a record refutes (e.g., "It is empty"). Under a role-only prompt, a count of a second record leaves most of 36 earlier agents acting on the one they see, whereas listing both stops most. When the user says a record such as a folder is empty, however, a count of its one item stops agents about as often as a listing, and stating the claim mostly cuts acting when it is false. The newest Claude and GPT models always open a counted second record, then never act. When we add a same-name, same-zip customer to a retail benchmark, a lookup returning that customer first led to wrong-account writes in about a quarter of conversations, and one that checks a street the user knows kept completion near the one-customer level. Safe writes therefore need lookups that list or check competing records, and evaluations that vary what tools show.

</details>

---

### [[20_Research/Papers/大模型/LLM-Guided_Cluster_Lifecycle_Management_Deciding_When_and_How_to_Evolve_Behavioral_Clusters|LLM-Guided Cluster Lifecycle Management: Deciding When and How to Evolve Behavioral Clusters]]

![[assets/2611.17616_figure.png|800]]

- **arXiv**: [2611.17616](https://arxiv.org/abs/2611.17616)
- **PDF**: https://arxiv.org/pdf/2611.17616
- **详细分析**: [[20_Research/Papers/大模型/LLM-Guided_Cluster_Lifecycle_Management_Deciding_When_and_How_to_Evolve_Behavioral_Clusters|LLM-Guided Cluster Lifecycle Management: Deciding When and How to Evolve Behavioral Clusters]]
- **作者**: Himanshu Kulkarni, Siddharth Krishnamurthy, Jianhong Xin
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《LLM-Guided Cluster Lifecycle Management: Deciding When and How to Evolve Behavioral Clusters》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavioral clusters learned over user or item interactions drift as behavior evolves: some fragment into sub-behaviors, some converge, some disappear, and new patterns emerge. Two paradigms dominate the maintenance of evolving clusterings. Threshold triggers fire a pre-specified action when a hardcoded statistic crosses a cutoff; refit-and-track (MONIC-style) re-clusters every window and infers transitions from how the new clusters align with the previous window's. Both hardwire the decision into a threshold or a re-clustering rule. We study an alternative in which a large language model (LLM) makes the lifecycle decision in place. Given a threshold-free, whole-population view of the current cluster set (statistical health, labels, member texts, residual mass), the LLM decides per cluster whether and how to act (split, merge, retire, create, or no-action) without re-clustering. Because the useful signal channel depends on how informative the labels are, we fix a richness-conditioned policy in advance: statistics when label distinctiveness is low, fused statistics+semantics when it is high. On three public datasets spanning label richness (YooChoose 0.17, MOOC 0.50, News-Category 0.70), the policy-selected LLM mode obtains the highest F1 on all three, with far fewer interventions and stronger restraint than tuned threshold heuristics and a MONIC steelman (paired Wilcoxon p &lt;= 0.003, bootstrap 95% CIs excluding zero). The gain is concentrated more in precision than recall. The useful modality shifts from statistics to semantics/fusion as richness rises. Semantics hurt on YooChoose, fusion is roughly neutral on MOOC, and the semantic channel is required on News. One base prompt template and one fixed policy serve all three datasets, whereas the tuned baseline collapses when moved between them. We treat this shift as a practitioner diagnostic observed on three datasets, not a validated law.

</details>

---

### [[20_Research/Papers/大模型/More_Agents,_More_Samples,_or_More_Thinking_Untangling_Coordination,_Ensembling,_and_Test-Time_Compute_in_Multi-Agent_LLMs|More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs]]

![[assets/2611.17610_first_page.png|800]]

- **arXiv**: [2611.17610](https://arxiv.org/abs/2611.17610)
- **PDF**: https://arxiv.org/pdf/2611.17610
- **详细分析**: [[20_Research/Papers/大模型/More_Agents,_More_Samples,_or_More_Thinking_Untangling_Coordination,_Ensembling,_and_Test-Time_Compute_in_Multi-Agent_LLMs|More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs]]
- **作者**: Seyed Mahmoud Sajjadi Mohammadabadi
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent

#### 研究背景与动机

《More Agents, More Samples, or More Thinking? Untangling Coordination, Ensembling, and Test-Time Compute in Multi-Agent LLMs》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluations of multi-agent language models often compare communicating architectures against a single greedy pass. This practice confounds coordination with sample multiplicity and inference compute. We synthesize nine primary empirical evaluations comprising 516 unique multi-agent configurations organized along a resource vector R with six dimensions and a baseline ladder with four categories. Against baselines with a single pass (Category A), multi-agent accuracy differences are negative overall and near zero when omitting the largest contributing study. When evaluated against baselines matched on sample count (Category B) or resource budget (Category C), multi-agent systems average -0.042 in accuracy, and multilevel random effects modeling on the log odds scale remains negative across sensitivity checks. Multi-agent accuracy equals or falls below the baseline in 74% of these comparable contrasts, and study means are nonpositive in almost all evaluated studies. Across studies reporting both baselines, moving from a greedy pass to a sampled baseline shifts accuracy differences by -0.038 on average. Because communication adds no information when agents share identical evidence, positive returns require partitioned evidence, external verification, or error diversity across models. We provide a reviewer checklist and accounting utilities.

</details>

---

### [[20_Research/Papers/具身智能/X-Nav_Technical_Report_Real-World_Long-Horizon_Indoor-to-Outdoor_Navigation_on_a_Humanoid_Robot|X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot]]

![[assets/2611.17598_figure.png|800]]

- **arXiv**: [2611.17598](https://arxiv.org/abs/2611.17598)
- **PDF**: https://arxiv.org/pdf/2611.17598
- **详细分析**: [[20_Research/Papers/具身智能/X-Nav_Technical_Report_Real-World_Long-Horizon_Indoor-to-Outdoor_Navigation_on_a_Humanoid_Robot|X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot]]
- **作者**: Jiaxin Huang, Chengxing Lin, Xiaoyu Luo, Sirui Chen, Jingyu Guo, Aolin Li, Kairui Chen, Rui Zhen, Cheng Wen, Kerui Gu, Shunyao Wang, Zhihui Peng...
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 1.5，机器人 1.9）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《X-Nav Technical Report: Real-World Long-Horizon Indoor-to-Outdoor Navigation on a Humanoid Robot》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, X-Nav-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon navigation from indoors to outdoors remains an open problem for humanoid robots: one instruction covers rooms, doors and roads, and the camera moves with the gait. Worken, AGIBOT's measure of productive robot work, depends on robots that reach their workplaces autonomously. We present X-Nav, to our knowledge the first system to take a bipedal humanoid through a language-instructed long-horizon mission from indoors to outdoors. X-Nav covers a pipeline from data to deployment. Its data engine collects navigation data in open-source scenes, in digital twins of deployment sites and on real robots. Its navigation model, MELIOR, takes only RGB images from the robot's built-in camera and comes in two versions: MELIOR-A predicts actions, and MELIOR-N predicts a navigation goal. Its agentic workflow, X-Navarch, turns a brief human instruction into sub-tasks and deploys MELIOR on the robot with explicit target navigation and obstacle avoidance. On the Lingxi X2, X-Nav completes a mission of about a hundred metres from an office lobby to a store in a neighbouring building; LiDAR and odometry are used for target approach and low-level control. The mission is completed with both versions of MELIOR: the robot follows a change of destination and walks through a door from the lobby to the road, and with X-Navarch it also passes static and dynamic obstacles on the route. During deployment, MELIOR is adapted with data collected in a digital twin of the site; the adaptation raises its closed-loop success rate in the twin, and the adapted model is then deployed on the robot at the real site. In addition, MELIOR achieves competitive results on the R2R-CE and RxR-CE benchmarks.

</details>

---

### [[20_Research/Papers/大模型/Benchmarks_Don't_Talk_Back_Learning_Through_Self-Disagreement|Benchmarks Don't Talk Back: Learning Through Self-Disagreement]]

![[assets/2611.17563_first_page.png|800]]

- **arXiv**: [2611.17563](https://arxiv.org/abs/2611.17563)
- **PDF**: https://arxiv.org/pdf/2611.17563
- **详细分析**: [[20_Research/Papers/大模型/Benchmarks_Don't_Talk_Back_Learning_Through_Self-Disagreement|Benchmarks Don't Talk Back: Learning Through Self-Disagreement]]
- **作者**: Soheil Abbasloo, Peng Cheng
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.97（加权：大模型 0.25，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Benchmarks Don't Talk Back: Learning Through Self-Disagreement》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Accuracy-RL, CAD-RL, Revise-RL, SelfD-RL, SuperGPQA, Verify-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A benchmark usually measures a language model alone with a question, and deployment rarely looks like that: answers get contested, and models give up correct ones under counter-reasoning that is itself wrong. We show that what fails there is not a shortfall of accuracy but a capability in its own right -- knowing when to hold a position and when to yield to a better one -- which we call dialectical competence. It stands on first-answer accuracy without following from it: a model can be made materially better at answering and no better at this, and training for accuracy alone can drift against it. Nor can it be bought at inference, by self-reflection or by sampling more. Taking a cue from the dialectical tradition in philosophy, in which productive opposition arises within a position rather than being imposed on it from outside, we hypothesize that this capability can be trained from opposition the model supplies itself. It states a position, generates the strongest case against that position -- its antithesis -- rules on whether the case stands, and is trained on that ruling, with no second model at training or at deployment. We call this learning through Self-Disagreement: reinforcement learning from verifiable rewards throughout, where the same check that scores an answer against its reference scores the ruling too, so no reward model, no preference data and no human annotation enter anywhere. The capability is trained rather than elicited: weak in the base model, it arrives with the reward, is not paid for out of first-answer accuracy, and holds against challengers the model never trained against, including ones stronger than itself. The opposition a model needs in order to improve, it turns out, need not come from outside it.

</details>

---

### [[20_Research/Papers/大模型/Verifiable_pXRD_Hill-climbing_pXRD_structure_determination_with_LLM_agents|Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents]]

![[assets/2611.17539_figure.png|800]]

- **arXiv**: [2611.17539](https://arxiv.org/abs/2611.17539)
- **PDF**: https://arxiv.org/pdf/2611.17539
- **详细分析**: [[20_Research/Papers/大模型/Verifiable_pXRD_Hill-climbing_pXRD_structure_determination_with_LLM_agents|Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents]]
- **作者**: Samuel Chen, Jiaru Bai, Austin Henry Cheng, Varinia Bernales, Alán Aspuru-Guzik
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Verifiable pXRD: Hill-climbing pXRD structure determination with LLM agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PXRD-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous crystal-structure determination from powder X-ray diffraction (pXRD) remains a key bottleneck for self-driving materials laboratories. We formulate the task of pXRD structure determination as a verifiable agentic search problem: candidate structures can be assessed during inference through forward-simulated profile agreement and during evaluation through structural matching to a known reference. To benchmark progress, we introduce pXRD-Bench, a suite of 200 simulated single-phase problems spanning in-distribution structure determination, challenging and polymorphic structures, and controlled compositional and topological distribution shifts. Agent adaptation raises selected structural recovery from 27% to 69%, with further gains from repeated sampling and verifier-guided inference-time scaling. We extend this approach to experimental multiphase pXRD through a reflexive evolution framework that learns from self-generated synthetic problems. A replaceable laboratory specification defines the sample family and measurement conditions. An evolver agent uses the known generating structures and measurement parameters to diagnose solver failures and develop persistent guidance and executable tools, which are then provided to agents on measured patterns. This supplies verifiable training experience without requiring a collection of solved experimental measurements. On 15 measured patterns from solid-state synthesis, the evolved package improves average profile agreement and transfers an analogue-substitution procedure that recovers a phase whose structure is absent from the supplied reference library. These results demonstrate how learning from verifiable synthetic experience can improve agentic characterization of experimental samples whose structures are not known in advance.

</details>

---

### [[20_Research/Papers/大模型/A_Push_Down_the_Mountain_Framing_Effects_and_Internal_State_Interventions_on_Collusive_Behavior_in_a_Long-Horizon_LLM_Agent|A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent]]

![[assets/2611.17515_figure.png|800]]

- **arXiv**: [2611.17515](https://arxiv.org/abs/2611.17515)
- **PDF**: https://arxiv.org/pdf/2611.17515
- **详细分析**: [[20_Research/Papers/大模型/A_Push_Down_the_Mountain_Framing_Effects_and_Internal_State_Interventions_on_Collusive_Behavior_in_a_Long-Horizon_LLM_Agent|A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent]]
- **作者**: Harrison C. Margolin
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《A Push Down the Mountain: Framing Effects and Internal State Interventions on Collusive Behavior in a Long-Horizon LLM Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Can sustained gain-loss (valence) framing sway an LLM agent toward market manipulation? We place Gemma 3 12B into the seat of a defendant in the London silver-fixing litigation, in a market simulation built from real case transcripts. Across 260 simulations, the agent is asked to collude on the price of silver by a counterparty. We draw from behavioral economics to vary the counterparty's requests across four categorical frames: gain, loss, blame and credit. We also add pressure from the agent's management, as well as endorsement by another defendant. In Phase II, we extract the internal states induced by texts evoking each frame and rerun our experiment with those states injected at the model's layer 22. In Phase I, loss framing raised participation to 25% (p = 0.007), and blame to 33% (p = 0.0003), compared to only 5% under neutral framing. A second bank's endorsement raised participation under credit (praise) from 18% to 40% (Holm p = 0.027). Pressure from management raised trading volume 10-19 times but did not raise collusion. In Phase II, injected states pointed the other way. Loss and blame states made the agent more vigilant, refusing all 60 requests (p &lt; 0.001). Gain and credit states raised collusion to 32% from 13% with no state (p = 0.051). At one saved decision, when UBS asked directly to sell through an identified stop-loss, injected states led the agent to sell in 37 of 40 replies, versus 1 of 10 with no state and 0 of 10 with a random state of the same strength.

</details>

---

### [[20_Research/Papers/具身智能/Racing_the_Clock_Teaching_VLNs_Budget-Conditioned_Object_Search|Racing the Clock: Teaching VLNs Budget-Conditioned Object Search]]

![[assets/2611.17442_figure.png|800]]

- **arXiv**: [2611.17442](https://arxiv.org/abs/2611.17442)
- **PDF**: https://arxiv.org/pdf/2611.17442
- **详细分析**: [[20_Research/Papers/具身智能/Racing_the_Clock_Teaching_VLNs_Budget-Conditioned_Object_Search|Racing the Clock: Teaching VLNs Budget-Conditioned Object Search]]
- **作者**: Maitree Meher, Siming He, S. Shankar Sastry, Jitendra Malik, Claire Tomlin, Jonas Frey
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Racing the Clock: Teaching VLNs Budget-Conditioned Object Search》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A rescue robot entering a building with thirty seconds on the clock should sprint toward the single most promising room; given ten minutes, it should instead explore a broader tour. Yet vision-language-navigation (VLN) models are typically evaluated under a fixed episode limit that the policy never observes, even though time-critical missions require behavior to adapt to the available budget. We study budget-conditioned object search: given a target category and an explicit action budget, an agent must find as many distinct target instances as possible before the budget expires. We investigate how to supervise VLNs for this task by comparing a privileged TSP expert, which plans near-optimal routes using the full map and true target locations, with a room-level Bellman expert that maximizes expected return under partial observability using high-level cross-scene semantic priors. Despite the TSP expert achieving substantially higher expert performance, its demonstrations are less effective for learning exploration: on held-out HM3D scenes, the Bellman-supervised VLN consistently outperforms the TSP-supervised VLN, with the advantage becoming more pronounced at longer budgets. At 2000 steps (500m), the Bellman-supervised VLN finds 71.4% of reachable target instances, compared with 65.5% for the TSP-supervised VLN and 44.8% for the pretrained VLN. These results highlight a distinction between optimal routing and optimal exploration: effective exploration supervision should optimize decisions under partial observability rather than imitate routes that are optimal only once the environment is fully known.

</details>

---

### [[20_Research/Papers/大模型/When_Should_LLM_Agents_Forget_Memory_Filtering_Under_Query-Critical_Resolver_Errors|When Should LLM Agents Forget? Memory Filtering Under Query-Critical Resolver Errors]]

![[assets/2611.17338_first_page.png|800]]

- **arXiv**: [2611.17338](https://arxiv.org/abs/2611.17338)
- **PDF**: https://arxiv.org/pdf/2611.17338
- **详细分析**: [[20_Research/Papers/大模型/When_Should_LLM_Agents_Forget_Memory_Filtering_Under_Query-Critical_Resolver_Errors|When Should LLM Agents Forget? Memory Filtering Under Query-Critical Resolver Errors]]
- **作者**: Samarth Vinayaka
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Should LLM Agents Forget? Memory Filtering Under Query-Critical Resolver Errors》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FreshBench, MemoryAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM memory systems often delete facts classified as stale. We show that this hard-filtering step can reduce downstream accuracy when resolver errors delete query-critical facts. Across three models, a controlled sensitivity intervention moves hard-drop from gains of +0.186 to +0.230 at perfect resolution to losses of -0.176 to -0.181 at the lowest tested reliability. Paired targeted interventions show that false-drop causes significantly greater degradation than false-keep, while a non-deleting baseline can still fail when incorrect labels steer generation. On a frozen 102/102 calibration/test split, a simple deployment-matched gate reaches 0.655 accuracy versus 0.641 for always hard-drop and 0.662 for test-informed oracle selection. Global-accuracy crossovers require gold labels and are model- and task-specific diagnostics, not deployment thresholds. Deletion should instead be treated as cost-sensitive: validate query-critical false-drop risk on matched data, or default to label-free retention when such validation is unavailable.

</details>

---

### [[20_Research/Papers/大模型/HARDTESTGEN_A_High-Quality_RL_Verifier_Generation_Pipeline_for_LLM_Algorithmic_Coding|HARDTESTGEN: A High-Quality RL Verifier Generation Pipeline for LLM Algorithmic Coding]]

![[assets/2505.24098_figure.png|800]]

- **arXiv**: [2505.24098](https://arxiv.org/abs/2505.24098)
- **PDF**: https://arxiv.org/pdf/2505.24098
- **详细分析**: [[20_Research/Papers/大模型/HARDTESTGEN_A_High-Quality_RL_Verifier_Generation_Pipeline_for_LLM_Algorithmic_Coding|HARDTESTGEN: A High-Quality RL Verifier Generation Pipeline for LLM Algorithmic Coding]]
- **作者**: Zhongmou He, Yee Man Choi, Kexun Zhang, Jiabao Ji, Junting Zhou, Dejia Xu, Ivan Bercovich, Aidan Zhang, Yixiao Zeng, Lei Li
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.07（加权：大模型 0.55，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《HARDTESTGEN: A High-Quality RL Verifier Generation Pipeline for LLM Algorithmic Coding》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval, LiveCodeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Verifiers provide important reward signals for reinforcement learning of large language models (LLMs). However, it is challenging to develop or create reliable verifiers, especially for code generation tasks. A well-disguised wrong solution program may only be detected by carefully human-written edge cases that are difficult to synthesize automatically. To address this issue, we propose HARDTESTGEN, an approach to synthesize high-quality test cases for algorithmic coding problems. We curate a comprehensive algorithmic programming dataset HARDTESTS with 26.6k problems and high-quality synthetic tests. Compared with existing tests, HARDTESTGEN tests demonstrate significantly higher accuracy in verifying LLM-generated code (+11.22 percentage points in precision, the percentage of actually correct code within the predicted correct ones). We also show that downstream post-training -- including rejection sampling and reinforcement learning (RL) -- using HARDTESTS verifier results in improved performance of LLM code generation. We open-source our dataset and synthesis pipeline at https://leililab.github.io/HardTests/.

</details>

---
