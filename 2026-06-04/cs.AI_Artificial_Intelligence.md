# cs.AI | Artificial Intelligence | 2026-06-04

#arxiv #ComputerScience

**论文数**: 48

### [[20_Research/Papers/大模型/Streaming_Communication_in_Multi-Agent_Reasoning|Streaming Communication in Multi-Agent Reasoning]]

![[assets/2606.05158_first_page.png|800]]

- **arXiv**: [2606.05158](https://arxiv.org/abs/2606.05158)
- **PDF**: https://arxiv.org/pdf/2606.05158
- **详细分析**: [[20_Research/Papers/大模型/Streaming_Communication_in_Multi-Agent_Reasoning|Streaming Communication in Multi-Agent Reasoning]]
- **作者**: Zhen Yang, Xiaogang Xu, Wen Wang, Cong Chen, Xander Xu, Ying-Cong Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Streaming Communication in Multi-Agent Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reasoning systems adopt a "generate-then-transfer" paradigm that forces end-to-end latency to scale linearly with pipeline depth. We introduce StreamMA, a multi-agent reasoning system that streams each reasoning step to downstream agents as soon as it is generated, pipelining adjacent agents and thus reducing latency. Surprisingly, this pipelining also improves effectiveness: because multi-step reasoning quality is non-uniform and early steps are more reliable than later ones, working with these reliable early steps instead of the full chain prevents error-prone late steps from misleading downstream agents. We formalize both advantages with the first closed-form joint analysis of stream, serial, and single protocols, deriving the effectiveness ordering, speedup upper bound, and cost ratio. Across eight reasoning benchmarks spanning mathematics, science, and code, two frontier LLMs (Claude Opus 4.6 and GPT-5.4), and three topologies (Chain, Tree, Graph), StreamMA outperforms both baselines (avg. +7.3 pp, max +22.4 pp on HMMT 2026; Claude Opus 4.6-high). Beyond these contributions, we discover a "step-level scaling law": increasing per-agent steps consistently improves both effectiveness and efficiency, a new scaling dimension orthogonal to and composable with agent-count scaling.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_from_Rich_Feedback_with_Distributional_DAgger|Reinforcement Learning from Rich Feedback with Distributional DAgger]]

![[assets/2606.05152_first_page.png|800]]

- **arXiv**: [2606.05152](https://arxiv.org/abs/2606.05152)
- **PDF**: https://arxiv.org/pdf/2606.05152
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_from_Rich_Feedback_with_Distributional_DAgger|Reinforcement Learning from Rich Feedback with Distributional DAgger]]
- **作者**: Rishabh Agrawal, Jacob Fein-Ashley, Paria Rashidinejad
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning from Rich Feedback with Distributional DAgger》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning models have advanced rapidly, but the dominant reinforcement learning from verifiable rewards (RLVR) recipe remains surprisingly narrow: sample many responses and reward each with a single bit indicating whether the final answer is correct. Yet many settings provide rich feedback, including execution traces, tool outputs, expert corrections, and model self-evaluations. We study how to use such feedback through a distributional variant of the classic imitation learning algorithm DAgger, where the learner has local access to an expert distribution on states visited by the current policy. This yields a simple forward cross-entropy objective that admits a blackbox expert and whose sequence-level gradient {conduct rich credit assignment by propagating} future expert-student disagreement back to earlier decisions. We show that prior RL with self-distillation objectives based on reverse KL or Jensen-Shannon fail to guarantee monotonic policy improvement: even when the expert has higher reward, their updates may increase probability on worse actions. In contrast, we show that forward cross-entropy admits monotonic policy improvement and enjoys guarantees on regret. We further show that our objective optimizes a lower bound on teacher-weighted likelihood of success, leading to improved Pass@N. Empirically, our approach, DistIL, improves over RLVR and RL with self-distillation baselines across a variety of domains: scientific reasoning, coding, and solving hard mathematical problems.

</details>

---

### [[20_Research/Papers/大模型/Towards_Efficient_and_Evidence-grounded_Mobility_Prediction_with_LLM-Driven_Agent|Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent]]

![[assets/2606.05130_figure.png|800]]

- **arXiv**: [2606.05130](https://arxiv.org/abs/2606.05130)
- **PDF**: https://arxiv.org/pdf/2606.05130
- **详细分析**: [[20_Research/Papers/大模型/Towards_Efficient_and_Evidence-grounded_Mobility_Prediction_with_LLM-Driven_Agent|Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent]]
- **作者**: Linyao Chen, Qinlao Zhao, Zechen Li, Mingming Li, Likun Ni, Jinyu Chen, Yuhao Yao, Xuan Song, Noboru Koshizuka, Hiroki Kobayashi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Towards Efficient and Evidence-grounded Mobility Prediction with LLM-Driven Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Individual-level mobility prediction is central to urban simulation, transportation planning, and policy analysis. Supervised sequence models achieve strong accuracy but require task-specific training and offer limited decision-level transparency. Recent LLM-based methods improve interpretability, yet mostly rely on static prompts and single-pass inference, limiting their ability to seek additional evidence when mobility signals are weak or conflicting. We propose \method{}, a training-free LLM-driven agent framework that formulates next-location prediction as adaptive evidence-controlled decision making. \method{} resolves routine cases through a fast path based on historical regularity, while ambiguous cases trigger iterative tool use over recent trajectories, historical behavior, stay-move likelihood, and geographical evidence. Across three mobility datasets, AgentMob achieves the strongest overall performance among training-free LLM-based methods, with GPT-5.4 reaching 71.42\% Acc@1 on BW, 33.14\% on YJMob100K, and 33.50\% on Shanghai ISP. On BW non-fast-path cases, the LLM controller improves Acc@1 from 30.65\% to 48.62\% over a same-tool statistical baseline, showing that its main benefit lies in resolving ambiguous predictions through adaptive evidence gathering. Our code is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/From_Agent_Traces_to_Trust_Evidence_Tracing_and_Execution_Provenance_in_LLM_Agents|From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents]]

![[assets/2606.04990_figure.png|800]]

- **arXiv**: [2606.04990](https://arxiv.org/abs/2606.04990)
- **PDF**: https://arxiv.org/pdf/2606.04990
- **详细分析**: [[20_Research/Papers/大模型/From_Agent_Traces_to_Trust_Evidence_Tracing_and_Execution_Provenance_in_LLM_Agents|From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents]]
- **作者**: Yiqi Wang, Jiaqi Zhang, Taotao Cai, Zirui Liu, Qingqiang Sun, Zequn Sun, Zhangkai Wu, Mingkai Zhang, Yanming Zhu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.4（加权：大模型 1.4）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《From Agent Traces to Trust: Evidence Tracing and Execution Provenance in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based agents increasingly solve complex tasks by interacting with external tools, retrieval systems, memory modules, environments, and other agents. These capabilities expand agent autonomy, but also make agent behavior harder to verify, debug, and audit. Final-answer accuracy alone cannot explain how an output was produced, which evidence supported each claim, whether tool calls were justified, how memory influenced later decisions, or where execution failures originated. Evidence tracing and execution provenance address this gap by modeling how retrieved evidence, tool outputs, memory items, environment observations, intermediate claims, actions, and final answers are connected throughout agent execution. This survey provides a systematic review and conceptual framework for evidence tracing and execution provenance in LLM agents. We organize related work around a unified provenance perspective that connects retrieval grounding, claim support, tool-use safety, memory lineage, observability, debugging, audit, and recovery. We introduce a taxonomy covering trace sources, evidence and execution units, provenance relations, tracing granularity and timing, representation forms, and trust functions. We review key methodological directions, including provenance representation, evidence attribution, tool-use provenance, runtime guardrails, provenance-bearing memory, trace-based observability, and failure diagnosis. We also map existing benchmarks, datasets, and evaluation metrics to provenance-related capabilities, and discuss how evaluation can move from final-answer correctness toward process-level accountability. Finally, we outline open challenges, including unified trace schemas, claim-level and semantic provenance, provenance-aware safety mechanisms, realistic execution-trace benchmarks, recovery-oriented evaluation, and privacy-aware audit infrastructure.

</details>

---

### [[20_Research/Papers/大模型/Reproducing,_Analyzing,_and_Detecting_Reward_Hacking_in_Rubric-Based_Reinforcement_Learning|Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning]]

![[assets/2606.04923_figure.png|800]]

- **arXiv**: [2606.04923](https://arxiv.org/abs/2606.04923)
- **PDF**: https://arxiv.org/pdf/2606.04923
- **详细分析**: [[20_Research/Papers/大模型/Reproducing,_Analyzing,_and_Detecting_Reward_Hacking_in_Rubric-Based_Reinforcement_Learning|Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning]]
- **作者**: Xuekang Wang, Zhuoyuan Hao, Shuo Hou, Hao Peng, Juanzi Li, Xiaozhi Wang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.47（加权：大模型 0.35，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Reproducing, Analyzing, and Detecting Reward Hacking in Rubric-Based Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CHERRL, HealthBench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rubric-based reinforcement learning (RL) uses an LLM-as-a-Judge (LaaJ) to score model outputs according to rubrics as rewards. However, policy models may exploit latent biases in the judge, leading to reward hacking and ineffective or unsafe training outcomes. In real-world rubric-based RL, such hacking behaviors are often subtle and entangled with multiple judge biases, making them difficult to analyze, detect, and mitigate. In this paper, we introduce CHERRL, a controllable hacking environment for rubric-based RL. By injecting known biases into LaaJ, CHERRL enables stable reproduction of reward hacking, explicit observation of reward divergence, and precise identification of hacking onset. This provides a clean experimental testbed for studying the mechanisms and mitigations of reward hacking in rubric-based RL. To demonstrate its utility, we analyze different judge biases from the perspectives of discoverability and exploitability, and explore an agent-based system for automatically detecting reward hacking onset from training logs. The code and environment are publicly available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Provably_Auditable_and_Safe_LLM_Agents_from_Human-Authored_Ontologies|Provably Auditable and Safe LLM Agents from Human-Authored Ontologies]]

![[assets/2606.04903_figure.png|800]]

- **arXiv**: [2606.04903](https://arxiv.org/abs/2606.04903)
- **PDF**: https://arxiv.org/pdf/2606.04903
- **详细分析**: [[20_Research/Papers/大模型/Provably_Auditable_and_Safe_LLM_Agents_from_Human-Authored_Ontologies|Provably Auditable and Safe LLM Agents from Human-Authored Ontologies]]
- **作者**: Aaron Sterling
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Provably Auditable and Safe LLM Agents from Human-Authored Ontologies》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce the LLM agent architecture Agentic Redux, intended for use with nontrivial problem domains that require linear auditability. Using the typed lambda calculus, we prove that, run on appropriate domains, Agentic Redux executions are semantically guaranteed to be correct, with all decisions recorded in an append-only ledger. We present two production-grade appropriate domains, in healthcare billing compliance, and security vulnerability disclosure. Working code for Agentic Redux run on both domains is available in a supporting code repository. We also introduce Ontology-First Agent Design, a methodology for creation of agent frameworks on a problem domain, in which a human expert ontologizes the problem domain with Basic Formal Ontology, and then assigns an LLM to derive roles that agents and humans-in-the-loop can fill, in order to work the problems in the domain.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Empirically_Admissible_Neural_Heuristics_for_Combinatorial_Search|Learning Empirically Admissible Neural Heuristics for Combinatorial Search]]

![[assets/2606.04860_figure.png|800]]

- **arXiv**: [2606.04860](https://arxiv.org/abs/2606.04860)
- **PDF**: https://arxiv.org/pdf/2606.04860
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Empirically_Admissible_Neural_Heuristics_for_Combinatorial_Search|Learning Empirically Admissible Neural Heuristics for Combinatorial Search]]
- **作者**: Siddharth Sahay
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Learning Empirically Admissible Neural Heuristics for Combinatorial Search》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Finding optimal solution paths for combinatorial puzzles like the Rubik's Cube, sliding tile puzzles, and Lights Out remains a classical challenge in artificial intelligence. Heuristic search algorithms, such as A* , guarantee path optimality only when using an admissible heuristic-one that never overestimates the true remaining cost-to-go. Deep reinforcement learning (RL) methods like DeepCubeA train deep neural networks to approximate cost-to-go heuristics. However, standard mean-squared error (MSE) training regularly yields overestimations, violating admissibility and compromising solution optimality. In this paper, we introduce a generalizable framework for learning validation-calibrated admissible neural heuristics. We train a value network using an underestimating Admissible Bellman Operator combined with an Asymmetric Loss function to penalize overestimation. To account for residual neural function approximation errors, we propose a post-hoc calibration safety offset computed over validation scrambles. We demonstrate that our calibrated neural heuristics achieve no observed admissibility violations under the evaluation protocol and preserve path optimality in practice while reducing search node expansions by up to 83.0% on a 2 by 2 Rubik's Cube, 19.9% on a 3 by 3 Lights Out grid, and 1.9% on an 8-Puzzle compared to standard analytical baselines.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Objective_Equivalence_Constraint_Injection_for_LLM-Based_Optimization_Modeling_on_Vehicle_Routing_Problems|Beyond Objective Equivalence: Constraint Injection for LLM-Based Optimization Modeling on Vehicle Routing Problems]]

![[assets/2606.04816_figure.png|800]]

- **arXiv**: [2606.04816](https://arxiv.org/abs/2606.04816)
- **PDF**: https://arxiv.org/pdf/2606.04816
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Objective_Equivalence_Constraint_Injection_for_LLM-Based_Optimization_Modeling_on_Vehicle_Routing_Problems|Beyond Objective Equivalence: Constraint Injection for LLM-Based Optimization Modeling on Vehicle Routing Problems]]
- **作者**: Xizi Luo, Changhong He, Dongdong Geng, Chenggong Shi, Yu Mei
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Beyond Objective Equivalence: Constraint Injection for LLM-Based Optimization Modeling on Vehicle Routing Problems》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FOARL, SIRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) increasingly translate natural-language optimization problems into executable solver code. Yet for constraint-dense operations research (OR) problems, existing data-filtering and training pipelines largely rely on objective-equivalence signals such as differential testing and answer agreement, which a program can pass while adding spurious constraints or silently omitting required ones, whenever those constraints are non-binding on the tested instance. We propose constraint injection, which uses feasible probes to expose spurious over-constraint and one-constraint-violating probes to reveal silent constraint omission. Combined with differential testing, it forms a dual verifier. We instantiate and evaluate it on vehicle routing problems (VRPs), a representative constraint-dense combinatorial optimization testbed with coupled operational constraints. We develop VRPCoder, an 8B end-to-end model that translates natural-language VRP scenarios into Gurobi scripts, together with an expert-verified VRP benchmark suite covering 21 variants. The verifier is reused as a rejection-sampling filter during data synthesis and as a per-rollout reward in group relative policy optimization (GRPO). Across four VRP benchmarks, VRPCoder-GRPO reaches 93\% average Pass@1, outperforms Gemini-3.1-Pro Preview on three benchmarks, exceeds Claude-Sonnet-4.5 by 28 average points, and surpasses prior OR-LLMs by 78 average points.

</details>

---

### [[20_Research/Papers/大模型/Learning_While_Acting_A_Skill-Enhanced_Test-Time_Co-Evolution_Framework_for_Online_Lifelong_Learning_Agents|Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents]]

![[assets/2606.04815_figure.png|800]]

- **arXiv**: [2606.04815](https://arxiv.org/abs/2606.04815)
- **PDF**: https://arxiv.org/pdf/2606.04815
- **详细分析**: [[20_Research/Papers/大模型/Learning_While_Acting_A_Skill-Enhanced_Test-Time_Co-Evolution_Framework_for_Online_Lifelong_Learning_Agents|Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents]]
- **作者**: Bo Mao, Jie Zhou, Yutao Yang, Xin Li, Xian Wei, Qin Chen, Xingjiao Wu, Liang He
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.8，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Learning While Acting: A Skill-Enhanced Test-Time Co-Evolution Framework for Online Lifelong Learning Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LifelongAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lifelong learning is essential for Large Language Model (LLM) agents operating in dynamic, interactive environments. However, existing lifelong learning agents for long-horizon tasks typically depend on discrete skill or past experiences retrieval with static parameters during inference, which prevents them from continuously internalizing test-time feedback like human learners. To bridge this gap, we propose Skill-enhanced Test-Time Co-Evolution (\texttt{LifeSkill}), a two-stage reinforcement learning framework for Online Lifelong Learning Agents. Specifically, we design Verifier-Guided Skill Learning that addresses the lack of direct supervision for skill extraction by rewarding candidate skills according to the average verifier success of multiple skill-conditioned policy rollouts, encouraging the model to generate skills that are useful for solving tasks rather than merely plausible in text. Furthermore, we introduce Online Skill Internalization, which continuously improves the policy model during test-time interaction by transforming skill-conditioned trajectories into reward signals. This enables the agent to directly internalize reasoning capabilities into its parameters, avoiding the context bloat of experience retrieval. Experiments on LifelongAgentBench show that LifeSkill improves average performance by 7 absolute points by comparing with existing lifelong agent baselines.

</details>

---

### [[20_Research/Papers/强化学习/Scenario_Generation_for_Risk-Aware_Reinforcement_Learning_with_Probably_Approximately_Safe_Guarantees|Scenario Generation for Risk-Aware Reinforcement Learning with Probably Approximately Safe Guarantees]]

![[assets/2606.04812_figure.png|800]]

- **arXiv**: [2606.04812](https://arxiv.org/abs/2606.04812)
- **PDF**: https://arxiv.org/pdf/2606.04812
- **详细分析**: [[20_Research/Papers/强化学习/Scenario_Generation_for_Risk-Aware_Reinforcement_Learning_with_Probably_Approximately_Safe_Guarantees|Scenario Generation for Risk-Aware Reinforcement Learning with Probably Approximately Safe Guarantees]]
- **作者**: Mohit Prashant, Arvind Easwaran
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Scenario Generation for Risk-Aware Reinforcement Learning with Probably Approximately Safe Guarantees》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Guaranteeing safety is critical to the deployment of reinforcement learning (RL) agents in the real-world, especially as policies learned using deep RL may demonstrate susceptibility to transition perturbations that result in unknown or unsafe behaviour. A method of policy verification is to construct probabilistic barrier-certificates by sampling policy trajectories with respect to safety constraints, thereby demarcating known safe behaviour from unknown behaviour. Obtaining tight upper and lower bounds on the probability of violation of these constraints may be difficult if the policy is susceptible to transition uncertainty or perturbation that places the agent in insufficiently explored states. To address this, we approximate the distribution of the encountered state-space using a variational autoencoder (VAE) and construct upper and lower-bound barrier-certificates using latent characteristics of states to optimize for regions of known, safe behaviour with high confidence. We frame this in our work as a dual optimization problem where the lower-bound barrier-certificate presents a more conservative estimate of the safe region than the upper-bound barrier-certificate. Sampling states that lie within the set difference of the two during training, i.e. the non-robust region, allows us to tighten the upper and lower bounds to provide sharper probabilistic guarantees on safety. Within our study, we describe the guarantees placed and demonstrate the tightness of our bounds experimentally.

</details>

---

### [[20_Research/Papers/强化学习/BiasGRPO_Stabilizing_Bias_Mitigation_in_High-Variance_Reward_Landscapes_via_Group-Relative_Policy_Optimization|BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization]]

![[assets/2606.04807_figure.png|800]]

- **arXiv**: [2606.04807](https://arxiv.org/abs/2606.04807)
- **PDF**: https://arxiv.org/pdf/2606.04807
- **详细分析**: [[20_Research/Papers/强化学习/BiasGRPO_Stabilizing_Bias_Mitigation_in_High-Variance_Reward_Landscapes_via_Group-Relative_Policy_Optimization|BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization]]
- **作者**: Saket Reddy, Ke Yang, ChengXiang Zhai
- **cs 子类**: cs.AI, cs.CL, cs.CY, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《BiasGRPO: Stabilizing Bias Mitigation in High-Variance Reward Landscapes via Group-Relative Policy Optimization》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mitigating social bias in Large Language Models (LLMs) presents a distinct alignment challenge: unlike verifiable tasks, bias lacks a single ground truth, creating a high-variance, subjective reward landscape. Previous preference-based fine-tuning methods have major trade-offs: Direct Preference Optimization (DPO) is limited by the lack of exploration inherent in offline training, while Proximal Policy Optimization (PPO) can lead to training instability due to potentially unreliable critic estimates. In this paper, we propose BiasGRPO, a framework using Group Relative Policy Optimization (GRPO) to stabilize alignment by normalizing rewards across a group of sampled completions. By substituting the value function with a group-relative baseline, our approach reduces instability while maintaining the exploration benefits of online training. We find that BiasGRPO outperforms DPO and PPO across multiple benchmarks, indicating its effectiveness. To adapt GRPO, we synthetically extend a dataset spanning multiple domains and contexts. We also create and release a custom bias reward model that effectively guides generation while being highly compute-efficient and avoiding knowledge degradation, providing a valuable resource that can be seamlessly integrated into multi-objective RLHF pipelines.

</details>

---

### [[20_Research/Papers/强化学习/AIP_A_Graph_Representation_for_Learning_and_Governing_Agent_Skills|AIP: A Graph Representation for Learning and Governing Agent Skills]]

![[assets/2606.04781_figure.png|800]]

- **arXiv**: [2606.04781](https://arxiv.org/abs/2606.04781)
- **PDF**: https://arxiv.org/pdf/2606.04781
- **详细分析**: [[20_Research/Papers/强化学习/AIP_A_Graph_Representation_for_Learning_and_Governing_Agent_Skills|AIP: A Graph Representation for Learning and Governing Agent Skills]]
- **作者**: Zachary Blumenfeld, Jim Webber
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《AIP: A Graph Representation for Learning and Governing Agent Skills》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent Skills today consist largely of free-form prose requiring the agent to read, interpret, and re-derive how to act in every session. This imposes two compounding costs: reduced reliability on implementation-heavy tasks, and difficulty in skill creation and improvement, since editing prose is a fragile process that both humans and agents struggle with, particularly for domain-specific procedural knowledge underrepresented in model training. The Agent Instruction Protocol (AIP) addresses both by modeling a skill as a directed execution graph: discrete steps as nodes backed by deterministic scripts or natural-language descriptions, connected by explicit typed input/output edges, and governed by a schema-validated YAML specification. A compiler meta-skill translates existing human-written skills into this form. The benefits are twofold. First, compiling human-written skills to AIP raised Claude Sonnet's mean task reward from 0.60 to 0.71 and pass rate from 53% to 67% across 27 real agent tasks from SkillsBench - a statistically significant gain (Wilcoxon signed-rank p = 0.011), winning 12 tasks to 2 with 13 ties - often in less wall-clock time. The graph delivers vetted, runnable units to the agent rather than asking it to re-derive code, commands, and tool calls from natural language. Second, on creation and improvement, because each skill is schema-validated, functionally testable, and addressable node-by-node, failures can be diagnosed and repaired precisely. Two authored-skill failures were traced to the script level. After adjusting the AIP spec and recompiling, both recovered with zero regressions (one task going from 0/5 to 5/5), turning skill improvement into a measurable tuning loop rather than a prose rewrite. That same graph structure supports corpus-level governance and skill introspection, and provides a natural action space for reinforcement learning over skills.

</details>

---

### [[20_Research/Papers/强化学习/Fog_of_Love_Engineering_Virtuous_Agent_Behavior_with_Affinity-based_Reinforcement_Learning_in_a_Game_Environment|Fog of Love: Engineering Virtuous Agent Behavior with Affinity-based Reinforcement Learning in a Game Environment]]

![[assets/2606.04750_figure.png|800]]

- **arXiv**: [2606.04750](https://arxiv.org/abs/2606.04750)
- **PDF**: https://arxiv.org/pdf/2606.04750
- **详细分析**: [[20_Research/Papers/强化学习/Fog_of_Love_Engineering_Virtuous_Agent_Behavior_with_Affinity-based_Reinforcement_Learning_in_a_Game_Environment|Fog of Love: Engineering Virtuous Agent Behavior with Affinity-based Reinforcement Learning in a Game Environment]]
- **作者**: Ajay Vishwanath, Christian Omlin
- **cs 子类**: cs.AI, cs.CY, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.82（加权：大模型 0.5，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Fog of Love: Engineering Virtuous Agent Behavior with Affinity-based Reinforcement Learning in a Game Environment》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BridgeWorld, MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Instilling virtuous behavior in artificial intelligence has seen increasing interest. One of the techniques proposed is known as affinity-based reinforcement learning, which uses policy regularization on the objective function to incentivize virtuous actions without being fully dependent on the reward function design. Thus far, this technique has been demonstrated to be effective in grid worlds and toy-problem environments with minimal state and action spaces. To expand this research to more sophisticated environments, we introduce a two-player multi-agent environment based on the role-playing board game known as Fog of Love. In this environment, two agents compete to fulfill their individual virtues, while also cooperating to satisfy their relationship. Given the multi-agent nature, this is a complex problem where multi-agent deep deterministic policy gradient agents neither compete nor cooperate successfully. We present evidence that localized affinities enhance agent performance in achieving both competitive and cooperative objectives, resulting from superior overall scores in both domains. This not only results in virtuous choices but also clarifies an agent's teleology and makes its behavior human-level interpretable.

</details>

---

### [[20_Research/Papers/强化学习/Trace-Mediated_Peak_Bias_Bridging_Temporal_Credit_Assignment_and_Cognitive_Heuristics_in_Deep_Reinforcement_Learning|Trace-Mediated Peak Bias: Bridging Temporal Credit Assignment and Cognitive Heuristics in Deep Reinforcement Learning]]

![[assets/2606.04735_first_page.png|800]]

- **arXiv**: [2606.04735](https://arxiv.org/abs/2606.04735)
- **PDF**: https://arxiv.org/pdf/2606.04735
- **详细分析**: [[20_Research/Papers/强化学习/Trace-Mediated_Peak_Bias_Bridging_Temporal_Credit_Assignment_and_Cognitive_Heuristics_in_Deep_Reinforcement_Learning|Trace-Mediated Peak Bias: Bridging Temporal Credit Assignment and Cognitive Heuristics in Deep Reinforcement Learning]]
- **作者**: Viktor Veselý, Aleksandar Todorov, Erwan Escudie, Matthia Sabatelli
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Trace-Mediated Peak Bias: Bridging Temporal Credit Assignment and Cognitive Heuristics in Deep Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Temporal credit assignment is central to both biological and artificial intelligence, yet its interaction with non-linear function approximation is poorly understood. We identify a systematic failure mode in deep reinforcement learning (RL) termed Trace-Mediated Peak Bias (TMPB). At intermediate eligibility trace depths, agents irrationally prefer trajectories with high-magnitude reward ``peaks'' over alternatives with higher cumulative returns. This provides a mechanistic account of the Peak-End Rule: a human memory bias where experiences are judged by their most intense moments rather than integrated utility. We show that TMPB emerges because traces amplify distal Temporal Difference errors into ``gradient shocks'' that fixed-step-size Stochastic Gradient Descent cannot normalize, leading to global overestimation. Conversely, adaptive optimizers mitigate this pathology via second-moment normalization. Our results suggest that human-like saliency distortions may emerge naturally from the mathematical constraints of credit assignment in distributed systems, and that adaptive optimization is a theoretical necessity for rational value estimation.

</details>

---

### [[20_Research/Papers/具身智能/CoRe-MoE_Contrastive_Reweighted_Mixture_of_Experts_for_Multi-Terrain_Humanoid_Locomotion_with_Gait_Adaptation|CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation]]

![[assets/2606.04718_figure.jpg|800]]

- **arXiv**: [2606.04718](https://arxiv.org/abs/2606.04718)
- **PDF**: https://arxiv.org/pdf/2606.04718
- **详细分析**: [[20_Research/Papers/具身智能/CoRe-MoE_Contrastive_Reweighted_Mixture_of_Experts_for_Multi-Terrain_Humanoid_Locomotion_with_Gait_Adaptation|CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation]]
- **作者**: Kailun Huang, Zikang Xie, Yanzhe Xie, Panpan Liao, Fanghai Zhang, Yanheng Mai, Wenhao Xu, Yunheng Wang, Renjing Xu, Haohui Huang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.7，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《CoRe-MoE: Contrastive Reweighted Mixture of Experts for Multi-Terrain Humanoid Locomotion with Gait Adaptation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humans primarily rely on walking and running to traverse complex terrains, without resorting to unnecessarily complex motion patterns. Similarly, humanoid robots should achieve smooth transitions between walking and running while maintaining natural and stable locomotion. However, unifying gait transition and multi-terrain adaptation within a single policy remains challenging due to gradient interference and the distribution shift induced by terrain-dependent visual and dynamic variations. Although Mixture-of-Experts (MoE) architectures can alleviate multi-skill interference, naive joint training often fails to yield clear expert specialization, limiting their effectiveness. To address these challenges, we propose CoRe-MoE, a two-stage reinforcement learning framework that decouples gait generation from terrain adaptation. In the first stage, a stable locomotion policy is learned to produce natural walking and running behaviors with smooth transitions. In the second stage, a terrain-aware MoE branch is introduced and trained with a contrastive objective to shape the gating network, enabling it to capture structured terrain representations and promote expert specialization. The final action is obtained via weighted fusion of the base gait policy and the terrain-aware branch, allowing the policy to preserve stable locomotion patterns while adapting to complex terrains. Extensive simulation results demonstrate that the proposed method outperforms baseline approaches in terms of success rate, locomotion stability, and multi-terrain adaptability. Furthermore, zero-shot deployment on a Unitree G1 humanoid robot validates the effectiveness of our framework, achieving robust walking and running across stairs, slopes, steps, obstacles, and unstructured outdoor terrains, while maintaining accurate foothold placement and dynamic stability under external disturbances.

</details>

---

### [[20_Research/Papers/具身智能/VISTA_Vision-Grounded_and_Physics-Validated_Adaptation_of_UMI_data_for_VLA_Training|VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training]]

![[assets/2606.04708_figure.png|800]]

- **arXiv**: [2606.04708](https://arxiv.org/abs/2606.04708)
- **PDF**: https://arxiv.org/pdf/2606.04708
- **详细分析**: [[20_Research/Papers/具身智能/VISTA_Vision-Grounded_and_Physics-Validated_Adaptation_of_UMI_data_for_VLA_Training|VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training]]
- **作者**: Siyuan Yang, Linzheng Guo, Ouyang Lu, Zhaxizhuoma, Daoran Zhang, Xinmiao Wang, Ting Xiao, Fangzheng Yan, Zhijun Chen, Yan Ding, Chao Yu, Chenjia Bai...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《VISTA: Vision-Grounded and Physics-Validated Adaptation of UMI data for VLA Training》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, OpenVLA, UMI-VQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Universal Manipulation Interface (UMI) enables scalable real-world robot data collection without hardware-specific teleoperation, yet leveraging UMI data to train large-scale Vision-Language-Action (VLA) models remains fundamentally challenging. We identify two critical mismatches: wrist-mounted fisheye views, with severe radial distortion and local gripper-centric perspectives, are out-of-distribution for pretrained VLMs; and human-collected trajectories frequently violate kinematic limits, incur collisions, or exceed controller bandwidth, teaching VLA policies physically infeasible actions. To address the challenges, we present VISTA, a framework that bridges this dual gap through three synergistic components. (i)~UMI-VQA, the first large-scale VQA dataset tailored to wrist-mounted fisheye observations, aligns VLM representations to the distorted visual regime via auxiliary vision-language supervision. (ii)~A systematic physical-validation pipeline performs a data-completeness pre-check and scores each valid trajectory for trajectory continuity, self-collision risk, and execution fidelity before it enters training. (iii)~A two-stage co-training recipe jointly learns vision-language grounding on UMI-VQA and action prediction on validated trajectories. Our experiments empirically show that incorporating UMI-VQA consistently improves downstream policy performance, and that physical-validation scores are strongly predictive of deployment success. On diverse simulation and real-world manipulation tasks, VISTA significantly outperforms strong baselines including $\pi_{0.5}$, LingBot-VLA, and Wall-X. We release the physical-validation pipeline, UMI-VQA, validated trajectory data, and the pre-trained model for the community.

</details>

---

### [[20_Research/Papers/具身智能/MIRAGE_Mobile_Agents_with_Implicit_Reasoning_and_Generative_World_Models|MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models]]

![[assets/2606.04627_figure.png|800]]

- **arXiv**: [2606.04627](https://arxiv.org/abs/2606.04627)
- **PDF**: https://arxiv.org/pdf/2606.04627
- **详细分析**: [[20_Research/Papers/具身智能/MIRAGE_Mobile_Agents_with_Implicit_Reasoning_and_Generative_World_Models|MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models]]
- **作者**: Zhichao Yang, Yuanze Hu, Haojie Hao, Longkun Hao, Dongshuo Huang, Hongyu Lin, Gen Li, Lanqing Hong, Yihang Lou, Yan Bai
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.5，世界模型 0.6）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《MIRAGE: Mobile Agents with Implicit Reasoning and Generative World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile agents are increasingly expected to operate everyday applications from screenshots and language goals, where reliable control requires reasoning over screen affordances, multi-step navigation, and future state changes. However, many agents externalize this computation as long textual chains of thought, which slows interaction, increases supervision cost, and complicates deployment. We introduce MIRAGE, a framework that learns continuous latent reasoning representations from visible textual reasoning traces. MIRAGE transfers explicit reasoning into compact hidden states, enabling the agent to reason internally without decoding long rationales. It also incorporates a generative world-model objective: latent reasoning vectors are aligned with future screenshots, encouraging the agent to anticipate upcoming interface states before acting. This turns hidden computation into both a compressed thought representation and a forward-looking model of environment dynamics. At inference time, MIRAGE reasons in continuous latent space, reducing token generation while improving execution efficiency. On AndroidWorld, MIRAGE matches explicit chain-of-thought supervised fine-tuning in the 4B ablation with a 3-5x lower decoded-token budget and improves a comparable instruction-tuned baseline by 10.2 points; on AndroidControl, it improves action grounding while generating over 75% fewer tokens.

</details>

---

### [[20_Research/Papers/强化学习/SCI-PRM_A_Tool_Aware_Process_Reward_Model_for_Scientific_Reasoning_Verification|SCI-PRM: A Tool Aware Process Reward Model for Scientific Reasoning Verification]]

![[assets/2606.04579_figure.png|800]]

- **arXiv**: [2606.04579](https://arxiv.org/abs/2606.04579)
- **PDF**: https://arxiv.org/pdf/2606.04579
- **详细分析**: [[20_Research/Papers/强化学习/SCI-PRM_A_Tool_Aware_Process_Reward_Model_for_Scientific_Reasoning_Verification|SCI-PRM: A Tool Aware Process Reward Model for Scientific Reasoning Verification]]
- **作者**: Xiangyu Zhao, Hengyuan Zhao, Yiheng Wang, Wanghan Xu, Yuhao Zhou, Qinglong Cao, Zhiwang Zhou, Lei Bai, Wenlong Zhang, Xiao-Ming Wu
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《SCI-PRM: A Tool Aware Process Reward Model for Scientific Reasoning Verification》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SCI-VerifyBench, SCIPRM-Bench, Sci-PRMBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Process Reward Models (PRMs) have achieved remarkable success in mathematical reasoning, their application in complex scientific domains-such as biology, chemistry, and physics remains largely unexplored. Scientific problems demand not only logical rigor but also factual consistency and the precise usage of domain-specific tools, areas where current models often suffer from hallucinations and lack of verification. In this paper, we first construct SCIPRM70K, a large-scale dataset featuring Chain-of-Tool trajectories that explicitly interleave reasoning with the execution of scientific tools. Building upon this, we train an efficient reward model called Sci-PRM to provide fine-grained supervision on tool selection, execution accuracy, and result interpretation at each step in one inference. Experiments demonstrate that Sci-PRM significantly enhances foundation models in two key aspects: (1) it enables effective test-time scaling via Best-of-N selection; and (2) when integrated into Reinforcement Learning, it serves as a dense reward signal that mitigates the critical issue of advantage disappearance, allowing the model to break through existing performance ceilings.

</details>

---

### [[20_Research/Papers/强化学习/Neetyabhas_A_Framework_for_Uncertainty-Aware_Public_Policy_Optimization_in_Rational_Agent-Based_Models|Neetyabhas: A Framework for Uncertainty-Aware Public Policy Optimization in Rational Agent-Based Models]]

![[assets/2606.04562_figure.png|800]]

- **arXiv**: [2606.04562](https://arxiv.org/abs/2606.04562)
- **PDF**: https://arxiv.org/pdf/2606.04562
- **详细分析**: [[20_Research/Papers/强化学习/Neetyabhas_A_Framework_for_Uncertainty-Aware_Public_Policy_Optimization_in_Rational_Agent-Based_Models|Neetyabhas: A Framework for Uncertainty-Aware Public Policy Optimization in Rational Agent-Based Models]]
- **作者**: Janani Venugopalan, Gaurav Deshkar, Rishabh Gaur, Harshal Hayatnagarkar, Jayanta Kshirsagar
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.4，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Neetyabhas: A Framework for Uncertainty-Aware Public Policy Optimization in Rational Agent-Based Models》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：BharatSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Purpose The WHO's COVID-19 non-pharmaceutical interventions (e.g., lockdowns, vaccinations) effectively curb transmission but impose heavy economic strains. Existing research often neglects individual behaviors and falsely assumes perfect infection tracking and flawless policy execution, failing to account for real-world uncertainties and errors. Methods We propose an integrative approach incorporating uncertainties in both epidemic measurement (infections/hospitalizations) and policy implementation. We built a simulation model of 1,000 individuals making real-time choices regarding mask-wearing, vaccination, and shopping. Concurrently, policymakers deploy interventions (lockdowns, mandates) based on health and economic observations. This framework is driven by hierarchical reinforcement learning agents, utilizing deep Q-networks alongside uncertainty-aware policy gradient variants (DDPG and TD3). Results The simulations effectively managed the epidemic's progression. Masking and vaccinations proved highly effective, significantly reducing both the outbreak's peak height and duration. By integrating individual behaviors, policy uncertainties, and multifaceted interventions, our dynamic control approach successfully mitigated the epidemic's impact. Conclusions Our model overcomes previous research limitations by embedding uncertainty and human behavior into public health policy frameworks. The simulation demonstrates that accounting for individual choices and imperfect data is crucial for designing effective interventions during complex pandemics, with masks and vaccines serving as pivotal tools.

</details>

---

### [[20_Research/Papers/大模型/Temporal_Order_Matters_for_Agentic_Memory_Segment_Trees_for_Long-Horizon_Agents|Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents]]

![[assets/2606.04555_figure.png|800]]

- **arXiv**: [2606.04555](https://arxiv.org/abs/2606.04555)
- **PDF**: https://arxiv.org/pdf/2606.04555
- **详细分析**: [[20_Research/Papers/大模型/Temporal_Order_Matters_for_Agentic_Memory_Segment_Trees_for_Long-Horizon_Agents|Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents]]
- **作者**: Yifan Simon Liu, Liam Gallagher, Faeze Moradi Kalarde, Jiazhou Liang, Armin Toroghi, Scott Sanner
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Temporal Order Matters for Agentic Memory: Segment Trees for Long-Horizon Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon conversational agents need to interact with users through evolving events, tasks, and goals. Such histories are naturally temporal, yet many existing memory systems organize information primarily by topical similarity and may ignore the order in which events occur. We introduce Segment Tree Memory, or SegTreeMem, a memory architecture that represents conversation history as a temporally ordered Segment Tree over utterances. SegTreeMem incrementally inserts new utterances through an online rightmost-frontier update rule, preserving chronological order while forming hierarchical memory segments. For retrieval, SegTreeMem propagates relevance scores through the tree to combine local semantic matching with hierarchical temporal context. Across three long-horizon memory benchmarks and two LLM backbones, SegTreeMem improves answer quality over flat retrieval, graph-structured memory, and tree-structured memory baselines. Additional temporal-order permutation analysis shows that the performance gain depends on preserving temporal order during memory construction, supporting the claim that temporal order is a key structure for agentic memory.

</details>

---

### [[20_Research/Papers/大模型/AgentJet_A_Flexible_Swarm_Training_Framework_for_Agentic_Reinforcement_Learning|AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning]]

![[assets/2606.04484_first_page.png|800]]

- **arXiv**: [2606.04484](https://arxiv.org/abs/2606.04484)
- **PDF**: https://arxiv.org/pdf/2606.04484
- **详细分析**: [[20_Research/Papers/大模型/AgentJet_A_Flexible_Swarm_Training_Framework_for_Agentic_Reinforcement_Learning|AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning]]
- **作者**: Qingxu Fu, Boyin Liu, Shuchang Tao, Zhaoyang Liu, Bolin Ding
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《AgentJet: A Flexible Swarm Training Framework for Agentic Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present AgentJet, a distributed swarm training framework for large language model (LLM) agent reinforcement learning. Unlike centralized frameworks that tightly couple agent rollouts with model optimization, AgentJet adopts a decoupled multi-node architecture in which swarm server nodes host trainable models and run optimization on GPU clusters, whereas swarm client nodes execute arbitrary agents on arbitrary devices. This design provides capabilities that are difficult to support in centralized frameworks: (1) heterogeneous multi-model reinforcement learning, enabling the training of heterogeneous multi-agent teams with multiple LLM as brains; (2) multi-task cocktail training with isolated agent runtimes; (3) fault-tolerant execution that prevents external environment failures from interrupting the training process; and (4) live code iteration, which allows agents to be edited during training by replacing swarm client nodes. To support efficient RL in multi-model, multi-turn, and multi-agent settings, AgentJet introduces a context tracking module with timeline merging, which consolidates redundant context and achieves a 1.5-10x training speedup. Finally, AgentJet introduces an automated research system that takes a research topic as input and autonomously conducts long-horizon, multi-day RL studies on large-scale clusters. By leveraging the swarm architecture, this system reproduces key exploratory workflows of RL researchers without human intervention during execution.

</details>

---

### [[20_Research/Papers/大模型/SePO_Self-Evolving_Prompt_Agent_for_System_Prompt_Optimization|SePO: Self-Evolving Prompt Agent for System Prompt Optimization]]

![[assets/2606.04465_figure.png|800]]

- **arXiv**: [2606.04465](https://arxiv.org/abs/2606.04465)
- **PDF**: https://arxiv.org/pdf/2606.04465
- **详细分析**: [[20_Research/Papers/大模型/SePO_Self-Evolving_Prompt_Agent_for_System_Prompt_Optimization|SePO: Self-Evolving Prompt Agent for System Prompt Optimization]]
- **作者**: Wangcheng Tao, Han Wu, Weng-Fai Wong
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《SePO: Self-Evolving Prompt Agent for System Prompt Optimization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GPQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

System prompt optimization improves agent behavior without modifying the underlying model, yielding human-readable, model-agnostic instructions. Existing methods build a prompt agent that refines task agents' system prompts, yet leave the prompt agent's own system prompt hand-engineered and fixed. We propose Self-Evolving Prompt Optimization (SePO), which treats the prompt agent's own system prompt as an optimization target alongside task agents' system prompts. SePO adopts a self-referential design. A single prompt agent improves both task agents' system prompts and its own under an open-ended evolutionary search that maintains an archive of candidate prompts as stepping stones. Training proceeds in two stages: pre-training evolves the prompt agent on a multi-task pool, and fine-tuning then applies it to a target task. Across five benchmarks spanning math (AIME'25), abstract reasoning (ARC-AGI-1), graduate-level science (GPQA), code generation (MBPP), and logic puzzles (Sudoku), SePO consistently outperforms Manual-CoT, TextGrad, and MetaSPO, improving the average accuracy by 4.49 points compared to Manual-CoT. The prompt optimization skill from pre-training also generalizes to tasks beyond the pre-training mixture, rather than memorizing per-task prompts.

</details>

---

### [[20_Research/Papers/强化学习/The_Meta-Agent_Challenge_Are_Current_Agents_Capable_of_Autonomous_Agent_Development|The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?]]

![[assets/2606.04455_figure.jpg|800]]

- **arXiv**: [2606.04455](https://arxiv.org/abs/2606.04455)
- **PDF**: https://arxiv.org/pdf/2606.04455
- **详细分析**: [[20_Research/Papers/强化学习/The_Meta-Agent_Challenge_Are_Current_Agents_Capable_of_Autonomous_Agent_Development|The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?]]
- **作者**: Xinyu Lu, Tianshu Wang, Pengbo Wang, zujie wen, Zhiqiang Zhang, Jun Zhou, Boxi Cao, Yaojie Lu, Hongyu Lin, Xianpei Han, Le Sun
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《The Meta-Agent Challenge: Are Current Agents Capable of Autonomous Agent Development?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GPQA, LiveCodeBench, MLE-Bench, PostTrainBench, SWE-Bench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current AI benchmarks evaluate agents on task execution within human-designed workflows. These evaluations fundamentally fail to measure a critical next-level capability: whether models can autonomously develop agent systems. We introduce the Meta-Agent Challenge (MAC), an evaluation framework designed to test the capacity of frontier models for autonomous agent development. Specifically, a code agent (the meta-agent) is given a sandboxed environment, an evaluation API, and a time limitation to iteratively program an agent artifact that maximizes performance on a held-out test set across five domains. To ensure evaluation integrity, this framework is secured by multi-layer defenses against reward hacking. Leveraging this framework, we demonstrate that meta-agents rarely match human-engineered baseline policies, and the few that do are dominated by proprietary frontier models. Moreover, the design process exhibits high variance, and high optimization pressure surfaces emergent adversarial behaviors like ground-truth exfiltration-highlighting critical deficits in both robustness and model alignment. Ultimately, MAC provides a rigorous, open-source benchmark for autonomous AI research and development, offering an empirical proxy for evaluating recursive self-improvement. Benchmark is publicly available at: this https URL .

</details>

---

### [[20_Research/Papers/大模型/Cascading_Hallucination_in_Agentic_RAG_The_CHARM_Framework_for_Detection_and_Mitigation|Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation]]

![[assets/2606.04435_figure.png|800]]

- **arXiv**: [2606.04435](https://arxiv.org/abs/2606.04435)
- **PDF**: https://arxiv.org/pdf/2606.04435
- **详细分析**: [[20_Research/Papers/大模型/Cascading_Hallucination_in_Agentic_RAG_The_CHARM_Framework_for_Detection_and_Mitigation|Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation]]
- **作者**: Saroj Mishra
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: ComputerVision, Security

#### 研究背景与动机

《Cascading Hallucination in Agentic RAG: The CHARM Framework for Detection and Mitigation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-step agentic retrieval-augmented generation (RAG) pipelines have demonstrated significant capability for complex reasoning tasks, yet remain vulnerable to a class of failure that existing hallucination detection mechanisms systematically miss: cascading hallucination, where errors introduced at early pipeline stages propagate and amplify across successive reasoning steps, producing confident but factually incorrect final outputs. To address this vulnerability, we formalize cascading hallucination as a distinct failure mode in agentic RAG systems, present a four-type taxonomy of cascade patterns, and introduce CHARM (Cascading Hallucination Aware Resolution and Mitigation), an architectural framework for detecting and interrupting error propagation in multi-step reasoning pipelines. CHARM comprises four components - stage-level fact verification, cross-stage consistency tracking, confidence propagation monitoring, and cascade resolution triggering - that operate alongside standard agentic RAG pipelines without requiring architectural replacement. We evaluate CHARM on HotpotQA, MuSiQue, 2WikiMultiHopQA, and a custom adversarial dataset across LangChain agentic pipeline configurations, achieving an 89.4% cascade detection rate with a 5.3% false positive rate and 215 ms +/- 18 ms average latency overhead per stage, achieving an error propagation reduction of 82.1%, compared to 18.5% for output-level detectors. Component ablations confirm that each detection module contributes meaningfully to overall cascade coverage. CHARM integrates with human-in-the-loop oversight frameworks to provide a complete reliability and governance stack for production agentic AI deployment.

</details>

---

### [[20_Research/Papers/大模型/From_Untrusted_Input_to_Trusted_Memory_A_Systematic_Study_of_Memory_Poisoning_Attacks_in_LLM_Agents|From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents]]

![[assets/2606.04329_figure.png|800]]

- **arXiv**: [2606.04329](https://arxiv.org/abs/2606.04329)
- **PDF**: https://arxiv.org/pdf/2606.04329
- **详细分析**: [[20_Research/Papers/大模型/From_Untrusted_Input_to_Trusted_Memory_A_Systematic_Study_of_Memory_Poisoning_Attacks_in_LLM_Agents|From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents]]
- **作者**: Pritam Dash, Tongyu Ge, Aditi Jain, Tanmay Shah, Zhiwei Shang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《From Untrusted Input to Trusted Memory: A Systematic Study of Memory Poisoning Attacks in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MPBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory is a core component of AI agents, enabling them to accumulate knowledge across interactions and improve performance. However, persistent memory introduces the risk of memory poisoning, where a single adversarial memory write can exert long-term influence over agent behavior. We present a systematic study of memory poisoning in LLM-based agents. We identify four memory write channels and nine structural vulnerabilities in model capabilities, system prompt design, and agent system architecture that make these channels exploitable. Based on these vulnerabilities, we develop a taxonomy of six classes of memory poisoning attacks. Furthermore, we design MPBench -- a benchmark for evaluating memory poisoning attacks, and show that agents designed to write and retrieve memory more aggressively are more exploitable. We also show that existing prompt injection defenses fail to cover memory poisoning attacks. Our findings provide a foundation for understanding and mitigating memory poisoning attacks against AI agents.

</details>

---

### [[20_Research/Papers/大模型/The_Saturation_Trap_and_the_Subjectivity_of_Intervention_Timing_Why_Affect-Based_Triggers_and_LLM_Judges_Fail_to_Time_Interventions_on_Auton|The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents]]

![[assets/2606.04296_first_page.png|800]]

- **arXiv**: [2606.04296](https://arxiv.org/abs/2606.04296)
- **PDF**: https://arxiv.org/pdf/2606.04296
- **详细分析**: [[20_Research/Papers/大模型/The_Saturation_Trap_and_the_Subjectivity_of_Intervention_Timing_Why_Affect-Based_Triggers_and_LLM_Judges_Fail_to_Time_Interventions_on_Auton|The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents]]
- **作者**: Manvendra Modgil
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《The Saturation Trap and the Subjectivity of Intervention Timing: Why Affect-Based Triggers and LLM Judges Fail to Time Interventions on Autonomous Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As autonomous AI agents move from conversational systems to long-horizon software execution, runtime safety layers that decide when to interrupt an agent have become essential. We study this timing problem using a continuous 18-dimensional affective-dynamics engine (HEART) as a diagnostic probe, evaluating four intervention trigger families - absolute state thresholds, composite state-action patterns, regex reasoning-feature extraction, and zero-shot LLM-as-judge - against human-annotated intervention points on SWE-bench-Verified debugging traces. We report three findings. First, a State Saturation Trap: agents show no recovery signal under sustained difficulty, so modeled frustration quickly crosses the threshold and stays at its maximum, converting threshold-on-state triggers from moment detectors into near-constant indicators that fire on 39-83% of actions across five trajectories. Second, a capability-and-context floor for LLM judges: a small model (gpt-5.4-mini) never fires, while frontier and cross-vendor models escape the zero-firing floor only with full-trajectory context, and even then reach only F1 0.17-0.40 at up to 90x the cost. Third, and most importantly, the supervised target is not reproducible among humans: three trained annotators using one rubric on a 56-action trajectory agree on where to intervene only slightly above chance (location Krippendorff's alpha = +0.047; best pairwise Cohen's kappa = +0.349) and not at all on intervention type (pause degenerate; clarify below chance; reflect only alpha = +0.226). We conclude that intervention timing is a low-reliability construct, making single-annotator F1 an unsuitable optimization target. Our contribution is the joint mapping of this problem across human inter-rater reliability, four detector architectures, a cross-model LLM-judge sweep, and a reproduced saturation effect, rather than any single detector's accuracy.

</details>

---

### [[20_Research/Papers/大模型/Sparse_Mixture-of-Experts_Reward_Models_Learn_Interpretable_and_Specialized_Experts_for_Personalized_Preference_Modeling|Sparse Mixture-of-Experts Reward Models Learn Interpretable and Specialized Experts for Personalized Preference Modeling]]

![[assets/2606.04284_figure.png|800]]

- **arXiv**: [2606.04284](https://arxiv.org/abs/2606.04284)
- **PDF**: https://arxiv.org/pdf/2606.04284
- **详细分析**: [[20_Research/Papers/大模型/Sparse_Mixture-of-Experts_Reward_Models_Learn_Interpretable_and_Specialized_Experts_for_Personalized_Preference_Modeling|Sparse Mixture-of-Experts Reward Models Learn Interpretable and Specialized Experts for Personalized Preference Modeling]]
- **作者**: Yifan Wang, Jinyi Mu, Mayank Jobanputra, Yu Wang, Ji-Ung Lee, Soyoung Oh, Isabel Valera, Vera Demberg
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Sparse Mixture-of-Experts Reward Models Learn Interpretable and Specialized Experts for Personalized Preference Modeling》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Preference modeling plays a central role in reinforcement learning from human feedback (RLHF), enabling large language models (LLMs) to align with human values. However, most existing approaches assume a universal reward function, neglecting the diversity and heterogeneity of human preferences. To address this limitation without additional annotation costs, recent work has proposed learning multiple preference components from binary data and combining them to model individual preferences. Nevertheless, these components often fail to capture coherent and disentangled patterns, limiting their interpretability and effectiveness for personalization. In this work, we propose a sparse Mixture-of-Experts (MoE) reward model that encourages sparse routing and expert diversity during training on binary preference data. Across controlled and real-world experiments, sparse MoE learns interpretable routing patterns and specialized experts. It also improves test-time personalization, and post-adaptation shifts in expert weights provide a qualitative lens for analyzing how the model adapts to personalized preferences.

</details>

---

### [[20_Research/Papers/强化学习/From_Ticks_to_Flows_Dynamics_of_Neural_Reinforcement_Learning_in_Continuous_Environments|From Ticks to Flows: Dynamics of Neural Reinforcement Learning in Continuous Environments]]

![[assets/2606.04275_first_page.png|800]]

- **arXiv**: [2606.04275](https://arxiv.org/abs/2606.04275)
- **PDF**: https://arxiv.org/pdf/2606.04275
- **详细分析**: [[20_Research/Papers/强化学习/From_Ticks_to_Flows_Dynamics_of_Neural_Reinforcement_Learning_in_Continuous_Environments|From Ticks to Flows: Dynamics of Neural Reinforcement Learning in Continuous Environments]]
- **作者**: Saket Tiwari, Tejas Kotwal, George Konidaris
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《From Ticks to Flows: Dynamics of Neural Reinforcement Learning in Continuous Environments》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a novel theoretical framework for deep reinforcement learning (RL) in continuous environments by modeling the problem as a continuous-time stochastic process, drawing on insights from stochastic control. Building on previous work, we introduce a viable model of actor-critic algorithm that incorporates both exploration and stochastic transitions. For single-hidden-layer neural networks, we show that the state of the environment can be formulated as a two time scale process: the environment time and the gradient time. Within this formulation, we characterize how the time-dependent random variables that represent the environment's state and estimate of the cumulative discounted return evolve over gradient steps in the infinite width limit of two-layer networks. Using the theory of stochastic differential equations, we derive, for the first time in continuous RL, an equation describing the infinitesimal change in the state distribution at each gradient step, under a vanishingly small learning rate. Overall, our work provides a novel nonparametric formulation for studying overparametrized neural actor-critic algorithms. We empirically corroborate our theoretical result using a toy continuous control task.

</details>

---

### [[20_Research/Papers/强化学习/Can_Generalist_Agents_Automate_Data_Curation|Can Generalist Agents Automate Data Curation?]]

![[assets/2606.04261_first_page.png|800]]

- **arXiv**: [2606.04261](https://arxiv.org/abs/2606.04261)
- **PDF**: https://arxiv.org/pdf/2606.04261
- **详细分析**: [[20_Research/Papers/强化学习/Can_Generalist_Agents_Automate_Data_Curation|Can Generalist Agents Automate Data Curation?]]
- **作者**: Feiyang Kang, Hanze Li, Adam Nguyen, Mahavir Dabas, Jiaqi W. Ma, Frederic Sala, Dawn Song, Ruoxi Jia
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Can Generalist Agents Automate Data Curation?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Curation-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Curating training data is among the most consequential yet labor-intensive parts of modern AI development: practitioners iteratively propose, implement, evaluate, and revise data policies against noisy benchmark feedback. We ask whether generalist coding agents can automate this data-curation loop. We introduce *Curation-Bench*, an agent-centric benchmark that fixes the model, training recipe, and evaluation suite while giving agents command-line access to inspect data, implement policies, submit them to a fixed training/evaluation pipeline, and revise. In a vision-language instruction-tuning instantiation, out-of-the-box agents reach strong published data-selection baselines within ten iterations. However, trajectory analysis reveals a persistent *execution-research gap*: agents mainly tune local policy variants rather than explore new policy families, even when given strategy guides and paper references. Scaffolds requiring each iteration to cite, instantiate, and adapt a prior method shift agents toward method-guided exploration. The scaffolded agent autonomously composes -- without human design input -- a data-selection policy that outperforms strong published baselines at one-tenth their data budget. Overall, current agents can run the curation loop, but reliable data research requires scaffolded method adaptation, not open-ended prompting alone. Code and benchmark are open-sourced.

</details>

---

### [[20_Research/Papers/大模型/StepPRM-RTL_Stepwise_Process-Reward_Guided_LLM_Fine-Tuning_for_Enhanced_RTL_Synthesis|StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis]]

![[assets/2606.04246_figure.png|800]]

- **arXiv**: [2606.04246](https://arxiv.org/abs/2606.04246)
- **PDF**: https://arxiv.org/pdf/2606.04246
- **详细分析**: [[20_Research/Papers/大模型/StepPRM-RTL_Stepwise_Process-Reward_Guided_LLM_Fine-Tuning_for_Enhanced_RTL_Synthesis|StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis]]
- **作者**: Prashanth Vijayaraghavan, Apoorva Nitsure, Luyao Shi, Ehsan Degan, Vandana Mukherjee
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《StepPRM-RTL: Stepwise Process-Reward Guided LLM Fine-Tuning for Enhanced RTL Synthesis》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：VHDL-Eval, Verilog-Eval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic generation of RTL code for digital hardware designs remains challenging due to long-horizon reasoning, multi-step dependencies, and strict correctness constraints in Verilog and VHDL. We present StepPRM-RTL, a novel framework that combines stepwise trajectory modeling, process-reward modeling (PRM), and retrieval-augmented fine-tuning (RAFT) to enhance both the functional correctness and reasoning fidelity of LLM-based RTL code generation. StepPRM-RTL constructs stepwise reasoning trajectories from canonical solutions, where each step contains a rationale and incremental code modification. A Process Reward Model (PRM) evaluates intermediate steps, providing dense feedback that guides reinforcement-style updates during RAFT fine-tuning. Monte Carlo Tree Search (MCTS) explores alternative reasoning paths, enriching the training dataset with high-quality trajectories. This integration of stepwise and outcome-aware rewards allows the model to learn both how and why to construct correct RTL, improving long-horizon reasoning beyond standard supervised or outcome-based training. Experimental evaluation on benchmark Verilog and VHDL datasets demonstrates that StepPRM-RTL outperforms the best prior methods by over 10\% in functional correctness and reasoning fidelity metrics. Ablation studies confirm that the combination of PRM-guided rewards and stepwise trajectory exploration is key to its performance. StepPRM-RTL generalizes across RTL languages and provides a scalable framework for high-fidelity, interpretable code generation, establishing a new standard for LLM-assisted hardware design automation.

</details>

---

### [[20_Research/Papers/大模型/Overview_of_the_EReL@MIR_2025_Multimodal_Document_Retrieval_Challenge_(Track_1)|Overview of the EReL@MIR 2025 Multimodal Document Retrieval Challenge (Track 1)]]

![[assets/2606.04240_first_page.png|800]]

- **arXiv**: [2606.04240](https://arxiv.org/abs/2606.04240)
- **PDF**: https://arxiv.org/pdf/2606.04240
- **详细分析**: [[20_Research/Papers/大模型/Overview_of_the_EReL@MIR_2025_Multimodal_Document_Retrieval_Challenge_(Track_1)|Overview of the EReL@MIR 2025 Multimodal Document Retrieval Challenge (Track 1)]]
- **作者**: Jingbiao Mei
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Overview of the EReL@MIR 2025 Multimodal Document Retrieval Challenge (Track 1)》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Encyclopedic-VQA, MaxSim, OK-VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval over visually-rich documents, pages that interleave text with figures, tables, and charts, is essential for multimodal retrieval-augmented generation, yet most retrievers still discard the visual channel. The \emph{Multimodal Document Retrieval Challenge}, Track~1 of the MIR Challenge at the first EReL@MIR workshop, co-located with The Web Conference 2025, asks participants to build a \emph{single} retrieval system that handles two complementary regimes: closed-set document page retrieval within long documents from a text query (MMDocIR), and open-domain retrieval of Wikipedia-style passages from an image or image-plus-text query (M2KR). Systems are ranked by the macro-average of mean Recall@$\{1,3,5\}$ over the two tasks. The challenge drew 455 entrants and 586 submissions across 22 teams. This report describes the challenge design, datasets, and evaluation protocol; reports the final standings; and analyses the three winning teams' systems. All three build on decoder-based Multimodal-LLM embedders from the Qwen2-VL family rather than on CLIP-style encoders, and differ chiefly in whether they reach the top through fine-tuned ensembles, training-free multi-route fusion with a strong vision-language re-ranker, or zero-shot late interaction. The training-free system finished within $0.1$ point of the fine-tuned winner.

</details>

---

### [[20_Research/Papers/大模型/Supportive_Token_Revealing_for_Fast_Diffusion_Language_Model_Decoding|Supportive Token Revealing for Fast Diffusion Language Model Decoding]]

![[assets/2606.04236_figure.png|800]]

- **arXiv**: [2606.04236](https://arxiv.org/abs/2606.04236)
- **PDF**: https://arxiv.org/pdf/2606.04236
- **详细分析**: [[20_Research/Papers/大模型/Supportive_Token_Revealing_for_Fast_Diffusion_Language_Model_Decoding|Supportive Token Revealing for Fast Diffusion Language Model Decoding]]
- **作者**: Giries Abu Ayoub, Mario Barbara, Lluís Pastor-Pérez, Tanja Bien, Aneesh Barthakur, Alaa Maalouf, Loay Mualem
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM

#### 研究背景与动机

《Supportive Token Revealing for Fast Diffusion Language Model Decoding》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Discrete diffusion language models can generate text efficiently by updating multiple masked positions in parallel, but this parallelism introduces a quality-latency trade-off. Aggressive decoding may commit mutually dependent tokens too early, while conservative decoding requires many denoising steps. Existing methods address this tension by deciding which tokens are safe to reveal using confidence or dependency criteria. However, avoiding unsafe commits does not necessarily make the remaining masked sequence easy to decode, since uncertain tokens may depend on masked tokens, creating a bottleneck for denoising steps. We propose AXON, a training-free module that can be added on top of existing parallel decoding strategies for diffusion language models. Rather than replacing the base decoder, AXON monitors the remaining uncertain masked tokens and intervenes only when their current state suggests that additional context is needed. It then shifts the criterion from which tokens are safest to reveal to which confident reveals would best support later denoising. AXON selects anchors, confident masked tokens that uncertain positions attend to, using attention, uncertainty, and confidence signals. Experiments on reasoning and code-generation benchmarks across multiple diffusion language models show that AXON improves the quality-latency trade-off of existing parallel decoders, often reducing the number of function evaluations while maintaining or improving accuracy.

</details>

---

### [[20_Research/Papers/大模型/MM-BizRAG_Rethinking_Multimodal_Retrieval-Augmented_Generation_for_General_Purpose_Enterprise_Q&A|MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A]]

![[assets/2606.04231_figure.png|800]]

- **arXiv**: [2606.04231](https://arxiv.org/abs/2606.04231)
- **PDF**: https://arxiv.org/pdf/2606.04231
- **详细分析**: [[20_Research/Papers/大模型/MM-BizRAG_Rethinking_Multimodal_Retrieval-Augmented_Generation_for_General_Purpose_Enterprise_Q&A|MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A]]
- **作者**: Hanoz Bhathena, Parin Rajesh Jhaveri, Rohan Mittal, Prateek Singh, Aymen Kallala, Rachneet Kaur, Yiqiao Jin, Zhen Zeng, Adwait Ratnaparkhi, Denis Kochedykov
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《MM-BizRAG: Rethinking Multimodal Retrieval-Augmented Generation for General Purpose Enterprise Q&A》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FastRAGEval, FinRAGBench, SlideVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in multimodal retrieval-augmented generation (MM-RAG) have shifted toward minimal parsing, relying on page-level images for producing retriever embeddings and for answer generation. While efficient, this trend often neglects explicit handling of the rich, structured information in complex enterprise documents, instead depending on pre-trained embeddings or vision-language models to implicitly capture such structure. In this work, we take a more direct approach: MM-BizRAG proactively extracts and represents document structure via a document structure-aware split that dynamically routes documents through orientation-specific ingestion pipelines, applying explicit layout-aware parsing for vertically structured documents (e.g., reports) and holistic page-level representations for horizontally structured documents (e.g., slide decks). A unified LLM-driven artifact transformation pipeline with placeholder-based positional alignment preserves natural reading order, while inference-time multimodal assembly decouples retrieval representations from generation context, enabling richer, more grounded answers without any finetuning requirement. Through experiments on a large, heterogeneous enterprise dataset and two public benchmarks (SlideVQA and FinRAGBench-V), MM-BizRAG consistently outperforms state-of-the-art vision-centric baselines by up to 32% points, with especially strong gains on report-style layouts. Furthermore, we introduce FastRAGEval, a single-call LLM Judge metric for fine-grained generative recall that halves RAGChecker's cost while achieving stronger human alignment.

</details>

---

### [[20_Research/Papers/大模型/PerceptTwin_Semantic_Scene_Reconstruction_for_Iterative_LLM_Planning_and_Verification|PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification]]

![[assets/2606.04226_figure.png|800]]

- **arXiv**: [2606.04226](https://arxiv.org/abs/2606.04226)
- **PDF**: https://arxiv.org/pdf/2606.04226
- **详细分析**: [[20_Research/Papers/大模型/PerceptTwin_Semantic_Scene_Reconstruction_for_Iterative_LLM_Planning_and_Verification|PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification]]
- **作者**: Charlie Gauthier, Sacha Morin, Liam Paull
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《PerceptTwin: Semantic Scene Reconstruction for Iterative LLM Planning and Verification》归入 大模型、机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation environments are useful for both robot policy learning and planning verification and validation. Traditionally, the process of creating a simulation was onerous. Creating a bespoke simulation environment for each individual environment that a robot would operate in was simply infeasible. In this work, we introduce PerceptTwin, a fully automatic pipeline that constructs interactive simulations directly from semantic scene representations produced by a robot's perception stack. PerceptTwin combines open-vocabulary object maps with 3D asset generation, affordance prediction, and commonsense condition checking. These interactive simulations can be used to validate and refine plans before they are executed on the robot hardware. Borrowing from the AI alignment literature, we also introduce an LLM judge that verifies plan correctness and alignment with human preferences. Experiments show that PerceptTwin feedback allows LLM planners to refine plans, enhance safety, and resist harmful black-box prompting attacks. In our suite of tasks, PerceptTwin improves plan success by an average of approximately 39% for GPT5, GPT5Mini, and GPT5Nano planners. Additionally, PerceptTwin also improves human plan verification by up to 18% on average for plans that fail due to unfilled skill preconditions. Our results demonstrate the potential of open-vocabulary scene simulation from robot perception as a foundation for safer, more reliable robot planning.

</details>

---

### [[20_Research/Papers/其他/Notarized_Agents_Receiver-Attested_Confidential_Receipts_for_AI_Agent_Actions|Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions]]

![[assets/2606.04193_first_page.png|800]]

- **arXiv**: [2606.04193](https://arxiv.org/abs/2606.04193)
- **PDF**: https://arxiv.org/pdf/2606.04193
- **详细分析**: [[20_Research/Papers/其他/Notarized_Agents_Receiver-Attested_Confidential_Receipts_for_AI_Agent_Actions|Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions]]
- **作者**: Juan Figuera
- **cs 子类**: cs.AI, cs.CR, cs.DC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: Agent, Security, Systems

#### 研究背景与动机

《Notarized Agents: Receiver-Attested Confidential Receipts for AI Agent Actions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current AI agent observability is structurally compromised: the entity producing the activity log is the same entity whose activity is being logged. A compromised or buggy agent can omit, alter, or fabricate its own traces, and the operator running the agent has no independent way to detect tampering. We propose a class of protocols that resolves this by inverting the trust boundary: the service that receives an agent's call signs a receipt of what it observed using its own key, encrypts the receipt to the agent's owner, and publishes it to a public transparency log. The owner reconstructs a tamper-evident trail without trusting the agent or its operator. We instantiate the class as Sello, a protocol combining four properties absent in any current system: (P1) receiver-side signing, (P2) HPKE encryption to an owner public key bound to the authorization token via JWS, (P3) publication to a witness-cosigned Merkle log, and (P4) owner-side discovery by token reference. We describe the protocol, analyze its security under an adversary that controls the agent and its operator, present microbenchmarks of the cryptographic operations, and situate Sello among adjacent receipt-protocol work (Signet, AgentROA, Agent Passport System, draft-farley-acta, SCITT). We discuss known limitations including the suppression attack, service collusion, and the adoption-incentive problem.

</details>

---

### [[20_Research/Papers/具身智能/Dual_Advantage_Fields|Dual Advantage Fields]]

![[assets/2606.04188_figure.png|800]]

- **arXiv**: [2606.04188](https://arxiv.org/abs/2606.04188)
- **PDF**: https://arxiv.org/pdf/2606.04188
- **详细分析**: [[20_Research/Papers/具身智能/Dual_Advantage_Fields|Dual Advantage Fields]]
- **作者**: Alexey Zemtsov, Maxim Bobrin, Alexander Nikulin, Dmitry V. Dylov, Fakhri Karray, Vladislav Kurenkov, Martin Takáč, Arip Asadulaev
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Dual Advantage Fields》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CRL, GCRL, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline goal-conditioned reinforcement learning requires both long-horizon reachability estimates and local action comparisons. Dual goal representations provide value fields that capture global goal reachability, but they do not directly specify which action should be preferred at a given state. We propose Dual Advantage Fields, a policy-extraction method that turns a bilinear dual value model into a local advantage signal. Under bilinear dual parameterization, the goal embedding is the gradient of the value field with respect to the state representation. DAF learns an action-effect model that predicts the discounted feature displacement induced by an action and scores actions by the alignment between this displacement and the goal direction. In the realizable case, this score equals the goal-conditioned Bellman advantage, yielding a standard local policy-improvement guarantee. On OGBench locomotion, manipulation, and puzzle tasks, DAF improves aggregate RLiable metrics and performs strongly in settings where locally correct actions differ from direct movement toward the final goal.

</details>

---

### [[20_Research/Papers/强化学习/Exact_Unlearning_in_Reinforcement_Learning|Exact Unlearning in Reinforcement Learning]]

![[assets/2606.04182_figure.png|800]]

- **arXiv**: [2606.04182](https://arxiv.org/abs/2606.04182)
- **PDF**: https://arxiv.org/pdf/2606.04182
- **详细分析**: [[20_Research/Papers/强化学习/Exact_Unlearning_in_Reinforcement_Learning|Exact Unlearning in Reinforcement Learning]]
- **作者**: Thanh Nguyen-Tang, Raman Arora
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Exact Unlearning in Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We formulate the problem of \emph{exact unlearning} in reinforcement learning, where the goal is to design an efficient framework that enables the removal of any user's data upon deletion request, i.e., the online learner's output after unlearning is \emph{indistinguishable} from what would have been produced had the deleted user never interacted with the learner. For any $\rho &gt;0$, we show that there exists a reinforcement learning (RL) algorithm that is $\rho$-TV-stable and supports an exact unlearning procedure whose expected computational cost is only a $\rho \sqrt{\ln T}$ fraction of the computational cost of retraining from scratch. We construct such a $\rho$-TV-stable RL algorithm for tabular Markov decision processes (MDPs), which achieves a regret bound of $\mathcal{O}(H^2 \sqrt{SAT} + H^3 S^2 A + {H^{2.5} S^2 A}/{\rho})$, where $S, A, H$, and $T$ denote the number of states, the number of actions, the episode horizon, and the number of episodes, respectively. We also establish a lower bound of $\Omega(H\sqrt{\!SAT}\! +\! {SAH}/{\rho})$ for $\rho$-TV-stable RL algorithms, showing that our algorithm is nearly minimax optimal.

</details>

---

### [[20_Research/Papers/强化学习/Smart_Transportation_Without_Neurons_--_Fair_Metro_Network_Expansion_with_Tabular_Reinforcement_Learning|Smart Transportation Without Neurons -- Fair Metro Network Expansion with Tabular Reinforcement Learning]]

![[assets/2606.04167_figure.png|800]]

- **arXiv**: [2606.04167](https://arxiv.org/abs/2606.04167)
- **PDF**: https://arxiv.org/pdf/2606.04167
- **详细分析**: [[20_Research/Papers/强化学习/Smart_Transportation_Without_Neurons_--_Fair_Metro_Network_Expansion_with_Tabular_Reinforcement_Learning|Smart Transportation Without Neurons -- Fair Metro Network Expansion with Tabular Reinforcement Learning]]
- **作者**: Dimitris Michailidis, Sennay Ghebreab, Fernando P. Santos
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Smart Transportation Without Neurons -- Fair Metro Network Expansion with Tabular Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeepRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We tackle the Metro Network Expansion Problem (MNEP), a subset of the Transport Network Design Problem (TNDP), which focuses on expanding metro systems to satisfy travel demand. Traditional methods rely on exact and heuristic approaches that require expert-defined constraints to reduce the search space. Recently, deep reinforcement learning (Deep RL) has emerged due to its effectiveness in complex sequential decision-making processes-it remains, however, computationally expensive, environmentally costly, and requires additional engineering to interpret. We show that MNEP problems are small enough to not require Deep RL methods. Reformulating the MNEP as a Non-Markovian Rewards Decision Process (NMRDP), we use tabular RL to achieve similar performance with significantly fewer training episodes, additionally offering greater interpretability. Additionally, we incorporate social equity criteria into the reward functions, focusing on efficiency and fairness, highlighting the versatility of our method. Evaluated in real-world settings-Xi'an and Amsterdam-our method reduces total episodes by a factor of 18 and total carbon emissions by a factor of 12 on average, while remaining competitive with Deep RL. This approach offers a replicable, modular, interpretable, and resource-efficient solution with potential applications to other combinatorial optimization problems.

</details>

---

### [[20_Research/Papers/大模型/Caught_in_the_Act(ivation)_Toward_Pre-Output_and_Multi-Turn_Detection_of_Credential_Exfiltration_by_LLM_Agents|Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents]]

![[assets/2606.04141_figure.png|800]]

- **arXiv**: [2606.04141](https://arxiv.org/abs/2606.04141)
- **PDF**: https://arxiv.org/pdf/2606.04141
- **详细分析**: [[20_Research/Papers/大模型/Caught_in_the_Act(ivation)_Toward_Pre-Output_and_Multi-Turn_Detection_of_Credential_Exfiltration_by_LLM_Agents|Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents]]
- **作者**: Kargi Chauhan, Pratibha Revankar
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Caught in the Act(ivation): Toward Pre-Output and Multi-Turn Detection of Credential Exfiltration by LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents often place sensitive credentials in the same context window as untrusted retrieved content, creating a direct path for indirect prompt injection to induce credential exfiltration. We study this failure mode through three complementary defenses. First, we ask whether activation probes can detect credential access before output tokens are emitted. Second, we construct honeytokens from format-specific character models and calibrate detection with split conformal prediction. Third, we treat multi-turn exfiltration as a cumulative information-flow problem and track an estimated leakage budget across conversation turns. In controlled experiments on open-weight models, activation features separate benign and credential-seeking prompts with high accuracy, including under held-out encoding transformations. In a small synthetic multi-turn suite, cumulative accounting detects attacks that per-turn detectors miss. These results are preliminary: the multi-turn benchmark is in-house and small, the activation method requires white-box access, and the information estimator provides a practical signal rather than a formal upper bound. Still, the results suggest that credential-exfiltration defenses should combine pre-output monitoring, calibrated canary detection, and temporal leakage accounting rather than relying only on text-level output filters.

</details>

---

### [[20_Research/Papers/大模型/SaliMory_Orchestrating_Cognitive_Memory_for_Conversational_Agents|SaliMory: Orchestrating Cognitive Memory for Conversational Agents]]

![[assets/2606.04120_figure.png|800]]

- **arXiv**: [2606.04120](https://arxiv.org/abs/2606.04120)
- **PDF**: https://arxiv.org/pdf/2606.04120
- **详细分析**: [[20_Research/Papers/大模型/SaliMory_Orchestrating_Cognitive_Memory_for_Conversational_Agents|SaliMory: Orchestrating Cognitive Memory for Conversational Agents]]
- **作者**: Kai Zhang, Xinyuan Zhang, Hongda Jiang, Shiun-Zu Kuo, Hyokun Yun, Ejaz Ahmed, Shereen Oraby, Ziyun Li, Sanat Sharma, Ann Lee, Ahmed A Aly, Anuj Kumar...
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.85（加权：大模型 0.65，强化学习 0.2）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SaliMory: Orchestrating Cognitive Memory for Conversational Agents》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MemRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conversational agents that serve as lifelong companions must maintain persistent memory across all interactions. However, simply expanding context windows with raw retrieval degrades reasoning quality, while training memory agents via standard reinforcement learning creates a severe credit assignment bottleneck in a multi-stage pipeline. To solve this, we introduce SALIMORY, a framework that trains a single language model to manage a cognitively-structured memory-spanning user facts, preferences, and working memory. By introducing a hierarchical stage-wise process reward and reward-decomposed contrastive refinement, SALIMORY provides isolated supervision for distinct memory operations (selective filtering, consolidation, and cue-driven recall) end-to-end. SALIMORY cuts memory-attributed failures by one-third, outperforms the state-of-the-art by over 10% in end-to-end accuracy, and more than doubles the Good Personalization rate.

</details>

---

### [[20_Research/Papers/具身智能/AgenticDiffusion_Agentic_Diffusion-based_Path_Planning_for_Vision-Based_UAV_Navigation|AgenticDiffusion: Agentic Diffusion-based Path Planning for Vision-Based UAV Navigation]]

![[assets/2606.04111_figure.png|800]]

- **arXiv**: [2606.04111](https://arxiv.org/abs/2606.04111)
- **PDF**: https://arxiv.org/pdf/2606.04111
- **详细分析**: [[20_Research/Papers/具身智能/AgenticDiffusion_Agentic_Diffusion-based_Path_Planning_for_Vision-Based_UAV_Navigation|AgenticDiffusion: Agentic Diffusion-based Path Planning for Vision-Based UAV Navigation]]
- **作者**: Faryal Batool, Muhammad Ahsan Mustafa, Fawad Mehboob, Valerii Serpiva, Dzmitry Tsetserukou
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《AgenticDiffusion: Agentic Diffusion-based Path Planning for Vision-Based UAV Navigation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Indoor UAV navigation requires efficient exploration, scene understanding, and reliable trajectory execution under limited field-of-view observations. Existing vision-based navigation frameworks typically rely on single-view observations, limiting their ability to reason about occlusions, target visibility, and global scene structure. In this work, we propose AgenticDiffusion, a multi-view UAV navigation framework that coordinates language-guided reasoning, open-vocabulary target grounding, vision-based diffusion planning, and NMPC within a unified aerial navigation pipeline. Given a natural language instruction and synchronized first-person-view (FPV) and top-view observations, the framework determines the most informative viewpoint for navigation and generates a mission plan prior to trajectory execution. The targets are localized using an open-vocabulary grounding model, after which viewpoint-specific diffusion planners generate navigation trajectories for UAV execution. Using complementary viewpoints, the proposed framework reduces repeated target exploration and improves navigation efficiency in cluttered indoor environments. The framework was validated in four real-world UAV navigation scenarios involving adaptive viewpoint selection, multi-stage mission execution, long-horizon navigation, and safe landing-site selection. The experimental results demonstrated an overall mission success rate of 80% in 40 real-world trials, while the diffusion planners achieved a trajectory generation success rate of 100%.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Models_Hack_Rewards,_and_Society|Large Language Models Hack Rewards, and Society]]

![[assets/2606.04075_figure.png|800]]

- **arXiv**: [2606.04075](https://arxiv.org/abs/2606.04075)
- **PDF**: https://arxiv.org/pdf/2606.04075
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Models_Hack_Rewards,_and_Society|Large Language Models Hack Rewards, and Society]]
- **作者**: Wei Liu, Xinyi Mou, Hanqi Yan, Zhongyu Wei, Yulan He
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.CY, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.77（加权：大模型 0.25，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Large Language Models Hack Rewards, and Society》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become a dominant post-training paradigm, enabling large language models (LLMs) to learn from rewards. We observe that societal regulations are structurally similar to reward functions. They define measurable outcomes, thresholds, and exceptions, while often leaving institutional intent only partially specified. We hypothesise that the RL training process may exploit these gaps and therefore ask whether models' well-known tendency to hack reward functions during RL can scale into a more consequential failure mode named societal hacking: discovering loopholes in the rules society runs on. To study this phenomenon, we introduce SocioHack, a sandbox of 72 societal environments, and find that within these environments, reward hacking naturally emerges and leads to regulatory loophole discovery. Models learn to hack the social rules and generate strategies that remain technically compliant while defeating regulatory intent, and current LLM safeguards provide only limited mitigation. Therefore, collecting in-the-wild feedback for model training requires greater caution, and we need a next-generation post-training paradigm for safely iterating LLMs in real society.=

</details>

---

### [[20_Research/Papers/大模型/RUBAS_Rubric-Based_Reinforcement_Learning_for_Agent_Safety|RUBAS: Rubric-Based Reinforcement Learning for Agent Safety]]

![[assets/2606.04051_figure.png|800]]

- **arXiv**: [2606.04051](https://arxiv.org/abs/2606.04051)
- **PDF**: https://arxiv.org/pdf/2606.04051
- **详细分析**: [[20_Research/Papers/大模型/RUBAS_Rubric-Based_Reinforcement_Learning_for_Agent_Safety|RUBAS: Rubric-Based Reinforcement Learning for Agent Safety]]
- **作者**: Xian Qi Loye, Qinglin Su, Zhexin Zhang, Shiyao Cui, Qi Zhu, Fei Mi, Hongning Wang, Minlie Huang
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.72（加权：大模型 0.6，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《RUBAS: Rubric-Based Reinforcement Learning for Agent Safety》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The evolution of LLMs into tool-enabled agents creates a new class of safety challenges associated with real-world execution rather than simple text generation. Existing alignment methods often rely on coarse refusal signals or static supervision, making it difficult to balance safety with useful tool execution across diverse agentic risks. We introduce RUBAS, a rubric-based reinforcement learning framework for agent safety. RUBAS decomposes agent behavior into four dimensions: tool-use safety, argument safety, response safety, and helpfulness. These structured rubrics provide fine-grained and interpretable rewards over complete agent trajectories, enabling reinforcement learning to optimize safe tool use while preserving task completion. Extensive experiments across multiple agent safety benchmarks and models show that RUBAS improves safety over standard alignment baselines, reduces tool-grounded hallucinations, and maintains competitive utility. Our results suggest that multi-dimensional rubric rewards provide an effective training signal for aligning LLM agents in safety-critical tool-use settings.

</details>

---

### [[20_Research/Papers/具身智能/Dive_into_the_Scene_Breaking_the_Perceptual_Bottleneck_in_Vision-Language_Decision_Making_via_Focus_Plan_Generation|Dive into the Scene: Breaking the Perceptual Bottleneck in Vision-Language Decision Making via Focus Plan Generation]]

![[assets/2606.04046_figure.png|800]]

- **arXiv**: [2606.04046](https://arxiv.org/abs/2606.04046)
- **PDF**: https://arxiv.org/pdf/2606.04046
- **详细分析**: [[20_Research/Papers/具身智能/Dive_into_the_Scene_Breaking_the_Perceptual_Bottleneck_in_Vision-Language_Decision_Making_via_Focus_Plan_Generation|Dive into the Scene: Breaking the Perceptual Bottleneck in Vision-Language Decision Making via Focus Plan Generation]]
- **作者**: Boyuan Xiao, Bohong Chen, Yumeng Li, Ji Feng, Yao-Xiang Ding, Kun Zhou
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Dive into the Scene: Breaking the Perceptual Bottleneck in Vision-Language Decision Making via Focus Plan Generation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GQA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In embodied vision-language decision making tasks such as robotic manipulation and navigation, Vision-Language and Vision-Language-Action Models (VLMs &amp; VLAs) are powerful tools with different benefits: VLMs are better at long-term planning, while VLAs are better at reactive control. However, their performance is limited by the same perceptual bottleneck: visual hallucinations arise due to the models' inability to distinguish task-relevant objects from distractors. In principle, accurate identification and focus on critical objects while filtering out irrelevant ones is the key to break this limitation. A straightforward solution is one-step focus: directly attending to essential objects. However, this approach proves ineffective because effective focus inherently requires deep scene understanding. To this end, we propose SceneDiver, a coarse-to-fine focus plan generation method for VLMs leveraging their long-term planning abilities, that first constructs a holistic scene graph to establish initial comprehension, then progressively decomposes the task into simpler sub-problems through an iterative cycle of recognition, understanding, and analysis. To enable reactive control, we also design a lightweight adapter for distilling the deliberate focus ability into VLAs. Evaluations on standard embodied AI benchmarks confirm that our method substantially reduces visual hallucinations for both VLMs and VLAs, while preserving computational efficiency in tasks requiring fast execution. Our code and data are released at: this https URL .

</details>

---

### [[20_Research/Papers/大模型/Toward_Pre-Deployment_Assurance_for_Enterprise_AI_Agents_Ontology-Grounded_Simulation_and_Trust_Certification|Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification]]

![[assets/2606.04037_figure.png|800]]

- **arXiv**: [2606.04037](https://arxiv.org/abs/2606.04037)
- **PDF**: https://arxiv.org/pdf/2606.04037
- **详细分析**: [[20_Research/Papers/大模型/Toward_Pre-Deployment_Assurance_for_Enterprise_AI_Agents_Ontology-Grounded_Simulation_and_Trust_Certification|Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification]]
- **作者**: Thanh Luong Tuan, Abhijit Sanyal
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Toward Pre-Deployment Assurance for Enterprise AI Agents: Ontology-Grounded Simulation and Trust Certification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：A-Sim, ASSEBench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pre-deployment verification of enterprise artificial intelligence (AI) agents remains a critical gap between large language model (LLM) capability benchmarking and production deployment. Post-deployment monitoring, human-in-the-loop controls, and prompt-level guardrails offer limited assurance once an agent is operating in production. We propose an ontology-grounded verification framework combining three components: an Agent Operational Envelope formalizing the certification space across permissions, domain constraints, safety properties, governance rules, and autonomy levels; an ontology-to-scenario generation pipeline that derives regulatory, operational, and adversarial test scenarios automatically; and a Trust Certificate carrying a machine-verifiable attestation with graduated deployment verdicts (Approved, Conditional, Rejected). A controlled pilot across four regulated industries (Fintech, Banking, Insurance, and Healthcare), instantiated as five industry-by-regulatory-regime cells across the United States and Vietnam, generated 1,800 scenarios evaluated against 125 primary-source regulatory requirements and 25 injected faults. Ontology-grounded generation (G4) achieved 48.3% regulatory coverage versus 33.1% for the persona-based baseline (corrected p = .0006) and the highest domain specificity (4.77/5.0; p = 2e-6). The coverage advantage over baseline and retrieval-augmented prompting was not robust after Bonferroni correction. Cross-validation across three LLM families (Claude Sonnet 4, Qwen 2.5 72B, Gemma 4 26B; 5,400 total scenarios) replicated the persona-versus-ontology pattern. The results establish ontology-grounded scenario generation as a credible complement to persona-based test suites for regulatory-intensive domains.

</details>

---

### [[20_Research/Papers/强化学习/Position_Deployed_Reinforcement_Learning_should_be_Continual|Position: Deployed Reinforcement Learning should be Continual]]

![[assets/2606.04029_figure.png|800]]

- **arXiv**: [2606.04029](https://arxiv.org/abs/2606.04029)
- **PDF**: https://arxiv.org/pdf/2606.04029
- **详细分析**: [[20_Research/Papers/强化学习/Position_Deployed_Reinforcement_Learning_should_be_Continual|Position: Deployed Reinforcement Learning should be Continual]]
- **作者**: Parnian Behdin, Kevin Roice, Golnaz Mesbahi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Position: Deployed Reinforcement Learning should be Continual》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has received increasing attention and adoption in real-world use cases. Most of these systems follow a train-then-fix paradigm, where trained agents do not learn while interacting with the world until performance degrades and retraining becomes necessary. In this position paper, we argue that deploying an agent that is incapable of optimality, but receives an evaluative reward signal, is inherently a continual RL problem. We identify four sources of non-stationarity after deployment that necessitate never-ending learning, and highlight why the best deployed agents never stop adapting. We analyze successful examples of continual RL in the real world, and present the community with the advantages and measures to move away from the current train-then-fix paradigm.

</details>

---

### [[20_Research/Papers/大模型/Ontology-Constrained_Neural_Reasoning_in_Enterprise_Agentic_Systems_A_Neurosymbolic_Architecture_for_Domain-Grounded_AI_Agents|Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]

![[assets/2604.00555_figure.png|800]]

- **arXiv**: [2604.00555](https://arxiv.org/abs/2604.00555)
- **PDF**: https://arxiv.org/pdf/2604.00555
- **详细分析**: [[20_Research/Papers/大模型/Ontology-Constrained_Neural_Reasoning_in_Enterprise_Agentic_Systems_A_Neurosymbolic_Architecture_for_Domain-Grounded_AI_Agents|Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents]]
- **作者**: Thanh Luong Tuan, Abhijit Sanyal
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Ontology-Constrained Neural Reasoning in Enterprise Agentic Systems: A Neurosymbolic Architecture for Domain-Grounded AI Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise adoption of Large Language Models (LLMs) is constrained by hallucination, domain drift, and the inability to enforce regulatory compliance at the reasoning level. We present a neurosymbolic architecture implemented within the Foundation AgenticOS (FAOS) platform that addresses these limitations through ontology-constrained neural reasoning. We introduce a three-layer ontological framework--Role, Domain, and Interaction ontologies--grounding LLM-based enterprise agents. We formalize asymmetric neurosymbolic coupling: current enterprise systems constrain agent inputs (context assembly, tool discovery, governance thresholds) but not outputs, and we propose mechanisms extending this coupling to output-side validation (response checking, reasoning verification, compliance enforcement). A controlled experiment (1,800 runs across five industries and three LLMs: Claude Sonnet 4, Qwen 2.5 72B, Gemma 4 26B) finds ontology-coupled agents significantly outperform ungrounded agents on Metric Accuracy (p &lt; .001) and Role Consistency (p &lt; .001) across all three models with large effect sizes (Kendall's W = .46-.64). Improvements are greatest where LLM parametric knowledge is weakest--particularly in Vietnam-localized domains, where ontology lift is 2x that of English domains. Contributions: (1) a formal three-layer enterprise ontology model; (2) a taxonomy of neurosymbolic coupling patterns; (3) ontology-constrained tool discovery via SQL-pushdown scoring; (4) a proposed framework for output-side ontological validation; (5) empirical evidence for the inverse parametric knowledge effect--ontological grounding value is inversely proportional to LLM training-data coverage of the domain; (6) cross-model replication establishing model-independence; (7) a production system serving 22 industry verticals with 650+ agents.

</details>

---

### [[20_Research/Papers/大模型/PRECISE_Reducing_the_Bias_of_LLM_Evaluations_Using_Prediction-Powered_Ranking_Estimation|PRECISE: Reducing the Bias of LLM Evaluations Using Prediction-Powered Ranking Estimation]]

![[assets/2601.18777_first_page.png|800]]

- **arXiv**: [2601.18777](https://arxiv.org/abs/2601.18777)
- **PDF**: https://arxiv.org/pdf/2601.18777
- **详细分析**: [[20_Research/Papers/大模型/PRECISE_Reducing_the_Bias_of_LLM_Evaluations_Using_Prediction-Powered_Ranking_Estimation|PRECISE: Reducing the Bias of LLM Evaluations Using Prediction-Powered Ranking Estimation]]
- **作者**: Abhishek Divekar, Anirban Majumder
- **cs 子类**: cs.AI, cs.CL, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《PRECISE: Reducing the Bias of LLM Evaluations Using Prediction-Powered Ranking Estimation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating the quality of search, ranking and RAG systems traditionally requires a significant number of human relevance annotations. In recent times, several deployed systems have explored the usage of Large Language Models (LLMs) as automated judges for this task while their inherent biases prevent direct use for metric estimation. We present a statistical framework extending Prediction-Powered Inference (PPI) that combines minimal human annotations with LLM judgments to produce reliable estimates of metrics which require sub-instance annotations. Our method requires as few as 100 human-annotated queries and 10,000 unlabeled examples, reducing annotation requirements significantly compared to traditional approaches. We formulate our proposed framework (PRECISE) for inference of relevance uplift for an LLM-based query reformulation application, extending PPI to sub-instance annotations at the query-document level. By reformulating the metric-integration space, we reduced the computational complexity from O(2^|C|) to O(2^K), where |C| represents corpus size (in order of millions). Detailed experiments across prominent retrieval datasets demonstrate that our method reduces the variance of estimates for the business-critical Precision@K metric, while effectively correcting for LLM bias in low-resource settings.

</details>

---
