# cs.AI | Artificial Intelligence | 2026-11-11

#arxiv #ComputerScience

**论文数**: 37

### [[20_Research/Papers/大模型/Comparative_Analysis_of_Agent_Evaluation_Frameworks_Stability,_Detection,_and_Discovery_in_Enterprise_Analytics_Agents|Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents]]

![[assets/2611.14493_figure.png|800]]

- **arXiv**: [2611.14493](https://arxiv.org/abs/2611.14493)
- **PDF**: https://arxiv.org/pdf/2611.14493
- **详细分析**: [[20_Research/Papers/大模型/Comparative_Analysis_of_Agent_Evaluation_Frameworks_Stability,_Detection,_and_Discovery_in_Enterprise_Analytics_Agents|Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents]]
- **作者**: Howard Zhang, Chuck Arvin, Logan Brown, Mihir Bhatia, Neelu Choudhary, Lily Miao
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Comparative Analysis of Agent Evaluation Frameworks: Stability, Detection, and Discovery in Enterprise Analytics Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FaithfulnessEval, OutputEval, ResponseRelevanceEval, TrajectoryEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying LLM-based analytics agents in enterprise settings requires evaluation frameworks that can reliably detect failures across complex, multi-tool workflows. We present a three-phase comparative study of three evaluation frameworks, each representing a distinct evaluation paradigm (trace-based LLM judging, text-only LLM judging with red-teaming, and deterministic heuristics), applied to two analytics agents in a controlled research setting using frozen execution traces. Phase 1 quantifies evaluation harness stability through repeated measurements, finding that 97% of configurations meet the stability threshold and that stability patterns are agent-independent. Phase 2 measures known risk detection on 72 ground-truth test cases, where the trace-based framework achieves the best precision-recall balance (F1=0.90) while text-only evaluation matches on recall but generates 5x more false alarms. Phase 3 evaluates unknown risk discovery, uncovering 24 novel failures with zero overlap between functional testing and security red-teaming. Our results demonstrate that (1) the information available to the evaluation harness determines evaluation quality, (2) functional and security evaluation are complementary, and (3) LLM-based evaluation harnesses surface subtle errors that human reviewers miss. We recommend a two-framework strategy: trace-based evaluation for functional assessment and adversarial red-teaming for security validation.

</details>

---

### [[20_Research/Papers/大模型/ReTrace_Distilling_Tool-Using_Agents_into_Planner-Free_Workflows|ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows]]

![[assets/2611.14492_first_page.png|800]]

- **arXiv**: [2611.14492](https://arxiv.org/abs/2611.14492)
- **PDF**: https://arxiv.org/pdf/2611.14492
- **详细分析**: [[20_Research/Papers/大模型/ReTrace_Distilling_Tool-Using_Agents_into_Planner-Free_Workflows|ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows]]
- **作者**: Kaiyuan Hou, Yang Ping Kuo, Indranil Bhattacharya, Rohith Nama, Arushi Gupta, Carlos D. Castillo, Prathap Ramachandra, Xiaofan Jiang, Francesco Carbone
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld, SOP-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Business process automation runs the same Standard Operating Procedure (SOP) again and again on new inputs. Large Language Model (LLM) agents can follow an SOP written in natural language, but they call an LLM to choose every step of every run, which adds latency and cost at scale. We present ReTrace, which turns an SOP and a few logged agent runs into a reusable workflow in which code, not an LLM, selects the next step. The agent's reasoning, the explanation it writes with each tool call, often states why it took an action; the tool calls alone do not. ReTrace extracts the condition behind each step, merges these conditions across runs into a compact rule document, and generates an executable workflow from it. Only this last stage depends on the platform, so rule documents can be compiled for different orchestration platforms. On $79$ procedures from our production platform, ReTrace workflows reach $93.8\%$ completion, against $96.8\%$ for the agent, at $24\%$ lower cost per task. On $τ^2$-Bench, they reach $75.8\%$ task success (agent: $80.6\%$) and run in $1.3$s instead of $170$s; three rounds of repair on training failures lift $k{=}2$ workflows from $66.7\%$ to $81.2\%$. On eight SOP-Bench procedures, ReTrace without repair trails few-shot generation ($80.6\%$ vs. $83.6\%$), but repair from labeled training failures lifts it to $87.8\%$ at $0.40$s per task, compared to $85.5\%$ in $46.6$s for the agent.

</details>

---

### [[20_Research/Papers/具身智能/One_Policy_for_100_Household_Tasks_Our_Solution_for_the_2026_BEHAVIOR_Challenge|One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge]]

![[assets/2611.14432_figure.png|800]]

- **arXiv**: [2611.14432](https://arxiv.org/abs/2611.14432)
- **PDF**: https://arxiv.org/pdf/2611.14432
- **详细分析**: [[20_Research/Papers/具身智能/One_Policy_for_100_Household_Tasks_Our_Solution_for_the_2026_BEHAVIOR_Challenge|One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge]]
- **作者**: Ilia Larchenko, Gleb Zarin, Atindra Nair, Keerti Manney, Vitaly Kleban, Mirko Kiefer, Anjana Yodaiken
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《One Policy for 100 Household Tasks: Our Solution for the 2026 BEHAVIOR Challenge》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BEHAVIOR2026VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We describe our solution for the 2026 BEHAVIOR Challenge: 100 long-horizon household tasks in the OmniGibson simulator. We placed 9th on the final leaderboard, the only independent team in the top 10. The core of the solution is a single vision-language-action (VLA) model, one checkpoint for all 100 tasks, built on our 1st-place 2025 solution, which is based on $π_{0.5}$. On the 50 tasks shared with 2025, its Q rises from 0.260 to 0.371; across all 100 tasks it scores 0.392. Our main conclusion from 2025 was that the model was undertrained, so most of the 2026 work went into training the model for longer, optimizing some training parameters, making each training step slightly faster and reducing the gradient noise: a migration from 50 to 100 tasks (semantic stages built from the demonstrations' skill annotations, task and stage embeddings of new tasks warm-started from similar old ones, and a 21-dimensional action space matching the teleoperation controls); variance-reduced multi-sample flow matching with a simple noise-vs-compute model that picks the number of action-expert samples per observation without ablations; and a 200k-step training run, about one pass over the 211M frames of the demonstrations. A cloud evaluation infrastructure keeps a shared record with provenance, episode diagnostics and restorable simulator states, and runs six simulators on one GPU together faster than real time. On top of the learned policy, 14 tasks are routed to a GPT-6 Astra coding agent that controls the robot through observation and motion tools, starting every episode from a frozen copy of its own practice session on training instances. Across these 14 tasks, Astra's mean Q is 0.639, against 0.108 for the learned policy. The public submission included only part of the Astra results and scored 0.446 Q with 27.3% full-task success.

</details>

---

### [[20_Research/Papers/大模型/Evaluating_LLM-Generated_World_Models_for_Neuro-Symbolic_Reasoning|Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning]]

![[assets/2611.14419_figure.png|800]]

- **arXiv**: [2611.14419](https://arxiv.org/abs/2611.14419)
- **PDF**: https://arxiv.org/pdf/2611.14419
- **详细分析**: [[20_Research/Papers/大模型/Evaluating_LLM-Generated_World_Models_for_Neuro-Symbolic_Reasoning|Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning]]
- **作者**: Souhaila Djaffal, Amna Jamal, Gagana Madhugiri Devaraja, Anidipta Pal, Jobst Heitzig
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，世界模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Evaluating LLM-Generated World Models for Neuro-Symbolic Reasoning》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Formal world models can support planning, verification, and safety reasoning, but constructing them from open-ended natural-language situations is difficult, particularly in multi-agent settings where several formalizations may be plausible. We study whether five LLMs can generate such world models as partially observable stochastic games and whether mechanical validity is sufficient to establish that the resulting model faithfully represents the intended decision problem. We introduce a benchmark of 44 scenarios spanning game, situational, and cultural settings and evaluate generated world models along three dimensions: mechanical validity, reference-relative structural agreement, and semantic criteria. Across three empirical tracks, we analyze 410 first-pass generations. In the reference-backed game track, 134/135 generated world models pass a strict mechanical audit, yet mean permutation-invariant structural F1 is only 0.366, with just 28/134 mechanically valid models exactly matching the authored reference. In the cultural track, explicitly naming the country changes the generated structural representation for most LLMs while producing only small changes in automated semantic scores. These results show that executability is a necessary but insufficient criterion for LLM-generated world models: models that are mechanically valid can still differ substantially in the structure used by downstream neuro-symbolic reasoning and planning.

</details>

---

### [[20_Research/Papers/大模型/When_Should_Agents_Remember_Falsification-Gated_Self-Evolution_for_LLM_Agents|When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents]]

![[assets/2611.14326_figure.png|800]]

- **arXiv**: [2611.14326](https://arxiv.org/abs/2611.14326)
- **PDF**: https://arxiv.org/pdf/2611.14326
- **详细分析**: [[20_Research/Papers/大模型/When_Should_Agents_Remember_Falsification-Gated_Self-Evolution_for_LLM_Agents|When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents]]
- **作者**: Runxuan Tang, Haoyu Gao, Yuyan Ding, Junyi Yao, Zihao Zheng, Zecheng Sheng, Liwei Hou
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《When Should Agents Remember? Falsification-Gated Self-Evolution for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld, LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly operate in long-horizon, verifier-rich environments, but current self-improvement mechanisms often write episode-derived lessons directly into memory, making local success an unreliable signal for reusable and safe knowledge. This paper addresses the core question of when an experience-derived behavioral update should be admitted into persistent agent state. We propose Falsification-Gated Self-Evolution (FGSE), a verifier-grounded framework that represents each candidate lesson as a structured hypothesis with an explicit precondition, behavior change, expected effect, and verifier. FGSE applies the hypothesis only in a temporary state, tests it on target-transfer, falsification, and archived-regression probes, and then commits, refines, or rejects it according to measured gain and risk. Across web, app, tool-use, and long-term memory benchmarks, FGSE achieves strong task performance, including 39.8 WebArena success rate, 78.8 AppWorld average completion, and 0.724/0.487 Pass$^1$ on $τ$-Retail/$τ$-Airline, while reducing falsification failures to 5.0%, regression damage to 1.3%, and harmful committed updates to 3.6%. These results suggest that testing memory updates as hypotheses supports more reliable long-term adaptation.

</details>

---

### [[20_Research/Papers/大模型/Don't_Just_Trust_Your_Memory_Evidence-Linked_Memory_Reduces_Memory-Induced_Degradation_in_LLM_Agents|Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents]]

![[assets/2611.14320_figure.png|800]]

- **arXiv**: [2611.14320](https://arxiv.org/abs/2611.14320)
- **PDF**: https://arxiv.org/pdf/2611.14320
- **详细分析**: [[20_Research/Papers/大模型/Don't_Just_Trust_Your_Memory_Evidence-Linked_Memory_Reduces_Memory-Induced_Degradation_in_LLM_Agents|Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents]]
- **作者**: Yukyeong Lee, Yumin Choi, Jinheon Baek, Sung Ju Hwang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Don't Just Trust Your Memory: Evidence-Linked Memory Reduces Memory-Induced Degradation in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ALFWorld, AppWorld, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

External memory enables LLM agents to improve from experience by distilling trajectories of past tasks into concise lessons for new tasks. However, memory can also lead to memory-induced degradation, where an agent fails on tasks it would solve without memory, often because it follows a lesson that is incorrect, or misapplies or misreads a valid one. This is because lessons are inferred from trajectories labeled only with task success or failure, yet are typically provided without the trajectories they came from, leaving the agent no way to check them. To address this, we introduce WikiTrace, an evidence-linked memory system designed to let agents check each lesson against its original trajectory. Specifically, motivated by the finding that a trajectory often still holds the evidence needed to catch an erroneous lesson, WikiTrace stores each lesson as a concise insight linked to a summary of why its trajectory succeeded or failed and to the raw trajectory itself. Then, on a new task, the agent starts from all insights and, whenever one lacks details needed to act, conflicts with another, or comes from a failed task, descends through its links with terminal tools to fill in missing details or correct the insight before acting. We validate WikiTrace on five agentic benchmarks, showing that it consistently outperforms existing memory approaches and a baseline given the same insights alone, while also reducing memory-induced degradation. Our code is available at https://github.com/yukyeongleee/wikitrace

</details>

---

### [[20_Research/Papers/强化学习/Recurrent_Modular_Structure_in_Spiking_Neural_Network_Reinforcement_Learning|Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning]]

![[assets/2611.14262_first_page.png|800]]

- **arXiv**: [2611.14262](https://arxiv.org/abs/2611.14262)
- **PDF**: https://arxiv.org/pdf/2611.14262
- **详细分析**: [[20_Research/Papers/强化学习/Recurrent_Modular_Structure_in_Spiking_Neural_Network_Reinforcement_Learning|Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning]]
- **作者**: Vikram Ramavarapu, Himanshu Udupi, Ashish Gautam
- **cs 子类**: cs.AI, cs.LG, cs.NE
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Recurrent Modular Structure in Spiking Neural Network Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biological neural circuits are both modular and recurrent, with dense communities sparsely linked to one another. Spiking neural networks (SNNs) for reinforcement learning are usually feed-forward, and it is unclear how to obtain functional modules in a recurrent SNN or what they buy. In this work, we introduce a class of spiking networks, called Community Recurrent SNNs (CoRe SNNs): recurrent networks partitioned into communities with fixed roles. A controller community receives the stimulus, each action has its own community, and latent communities carry internal state. Spiking activity is then a walk between communities, and the action is the community the walk reaches. All learning is local and three-factor, and the recurrent communities are closer to cortical microcircuits than a feed-forward actor. We compare three regimes for obtaining the communities: dynamic modularity, in which a new learning rule we introduce, Map-STDP, encourages modular structure during learning; partial modularity, in which a stochastic block model (SBM) initialization enforces it partly; and full modularity, in which sealing enforces it fully. On CartPole, across three spiking neuron models, Map-STDP improves learning over the same network without it matches full modularity (sealed communities) on two of the three models, and makes the observed spike walk more compressible. Replacing the feed-forward actor of a TD-STDP actor-critic with recurrent action communities improves on the feed-forward network on CartPole and LunarLander, and matches it on Acrobot. How strongly to enforce modularity depends on the task: full modularity helps most on Acrobot, while on LunarLander the dynamic, partial and full regimes perform alike. Overall, these recurrent modular networks can match or even improve upon feed-forward approaches, with improvements in bio-plausibility and energy efficiency.

</details>

---

### [[20_Research/Papers/具身智能/A_Cross-Scenario_Survey_and_Analysis_of_Self-Evolving_Multimodal_Agents|A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents]]

![[assets/2611.14256_first_page.png|800]]

- **arXiv**: [2611.14256](https://arxiv.org/abs/2611.14256)
- **PDF**: https://arxiv.org/pdf/2611.14256
- **详细分析**: [[20_Research/Papers/具身智能/A_Cross-Scenario_Survey_and_Analysis_of_Self-Evolving_Multimodal_Agents|A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents]]
- **作者**: Jingjing Jiang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《A Cross-Scenario Survey and Analysis of Self-Evolving Multimodal Agents》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work shows that multimodal agents increasingly self-improve without recurring human annotation. However, each self-improvement mechanism is designed and evaluated within a single scenario, leaving its preconditions unverified under cross-scenario transfer. This survey investigates the structural source of asymmetric mechanism transfer across four scenarios: multimodal reasoning, multimodal generation, GUI and Web navigation, and embodied manipulation. We first formalize the self-evolving multimodal agent by four criteria and a differentia of self-reference, and adopt the three-stage self-evolving loop of experience generation, feedback acquisition, and update consolidation as our analytical framework to position the scenarios along ceilings on rollout count and feedback fidelity. Comparing self-evolving with fixed loops within each scenario separates the limitations that the scenario imposes from those inherent in the self-evolving design. We then recast each mechanism as a trade-off that raises a scarce factor by presupposing a task-structural resource, such as output equivalence or checkable outcomes, and judge it portable, conditional, blocked, or redundant across scenarios. We attribute the asymmetry to divergent combinations of scarce factors and resources across opposite transfer directions, and identify the matched-budget measurements that could overturn these still untested verdicts.

</details>

---

### [[20_Research/Papers/机器人/Personalized_Affective_Perception_via_Continual_Learning_in_Human-Agent_Negotiation|Personalized Affective Perception via Continual Learning in Human-Agent Negotiation]]

![[assets/2611.14247_figure.png|800]]

- **arXiv**: [2611.14247](https://arxiv.org/abs/2611.14247)
- **PDF**: https://arxiv.org/pdf/2611.14247
- **详细分析**: [[20_Research/Papers/机器人/Personalized_Affective_Perception_via_Continual_Learning_in_Human-Agent_Negotiation|Personalized Affective Perception via Continual Learning in Human-Agent Negotiation]]
- **作者**: Mehmet Onur Keskin, Berk Buzcu, Nikhil Churamani, Reyhan Aydogan, Hatice Gunes, Catholijn Jonker
- **cs 子类**: cs.AI, cs.HC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.5，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Personalized Affective Perception via Continual Learning in Human-Agent Negotiation》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-interested intelligent agents that negotiate with humans should interpret nonverbal expressions and adapt their behavior accordingly. However, generic facial-affect models degrade across individuals and contexts, creating a generalization gap. We introduce an affect-adaptive negotiation strategy that incorporates Continual Learning with Imagination for Facial Expression Recognition (CLIFER) to personalize valence-arousal perception in real time. Differential feedback converts changes in valence-arousal direction and intensity into adjustments of the agent's target utility. An asynchronous architecture updates CLIFER in the background during live interaction. In a counterbalanced within-subject study in which 66 participants negotiated with a humanoid robot, the CL-enabled agent achieved significantly higher individual utility and elicited higher participant concession rates than the FaceChannel baseline. The CL condition yielded significantly higher mean arousal estimates, alongside a broader output range. Participant utility and Nash distance did not change significantly between conditions. These outcomes support the practical value of coupling continual affective personalization with differential feedback for real-time negotiation.

</details>

---

### [[20_Research/Papers/具身智能/Model-Free_Runtime_Measurement_of_Task-Relevant_Information|Model-Free Runtime Measurement of Task-Relevant Information]]

![[assets/2611.14111_figure.png|800]]

- **arXiv**: [2611.14111](https://arxiv.org/abs/2611.14111)
- **PDF**: https://arxiv.org/pdf/2611.14111
- **详细分析**: [[20_Research/Papers/具身智能/Model-Free_Runtime_Measurement_of_Task-Relevant_Information|Model-Free Runtime Measurement of Task-Relevant Information]]
- **作者**: Dimitris Panagopoulos, Adolfo Perrusquía, Yang Xing, Weisi Guo
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Model-Free Runtime Measurement of Task-Relevant Information》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems increasingly monitor physical kinematics, environmental states and task completion outcomes. While existing work provides methods to plan information seeking actions and interpret acquired observations, current approaches do not monitor whether the live process of information gathering is functioning properly. Consequently, such systems can remain operationally active without resolving outstanding mission requirements. To address this limitation, we introduce Acquisition-State Telemetry (AST), a model free architecture that evaluates ongoing information acquisition from observable evidence relative to declared task requirements. Specifically, a domain interface maps raw observations into task resolution coordinates and normalized comparative representations, which are processed by a fixed causal monitor. This monitor emits two continuous real time signals that quantify (i) prospective progress across unresolved requirements and (ii) informational friction generated when recurrent evidence yields negligible informational gain. We evaluated a single, unadjusted monitor configuration across eight diverse domains including search and rescue dialogue, spatial grid exploration, hierarchical capability acquisition, continuous robotic manipulation, and probabilistic intent estimation. We show that across these domains the friction channel distinguished unproductive stagnation from purposeful exploration prior to task completion, while remaining muted during post completion activity. Furthermore, in closed loop reinforcement learning experiments under early termination constraints, we demonstrate that penalizing informational friction allowed agents to sustain high mission success, whereas unpenalized policies and baselines with matched operational costs failed to complete required tasks.

</details>

---

### [[20_Research/Papers/大模型/Margin-Guided_Token_Credit_for_Reinforcement_Learning_with_Verifiable_Rewards|Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards]]

![[assets/2611.14015_first_page.png|800]]

- **arXiv**: [2611.14015](https://arxiv.org/abs/2611.14015)
- **PDF**: https://arxiv.org/pdf/2611.14015
- **详细分析**: [[20_Research/Papers/大模型/Margin-Guided_Token_Credit_for_Reinforcement_Learning_with_Verifiable_Rewards|Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards]]
- **作者**: Chi Liu, Xin Chen, Yuchuan Weng, Srinivasan Manoharan
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.42（加权：大模型 0.1，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Margin-Guided Token Credit for Reinforcement Learning with Verifiable Rewards》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：TRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In reinforcement learning with verifiable rewards, a language model is rewarded for a correct final answer, and GRPO passes that reward to every token of the solution in equal measure. We instead place the credit where the model hesitated, in a method we call MCPO (Margin-Credit Policy Optimization). We measure hesitation by the top-2 margin $M=p_1-p_2$ of the policy's next-token distribution, map it to a score with two fixed thresholds, and spread each solution's advantage over its tokens so that the mean stays unchanged. The margin is read from a forward pass the trainer already performs, so the method needs no extra model evaluation and no batch statistics. We train MiniCPM5-2B-Base with LoRA for 200 steps on 2,048 DAPO-Math problems and evaluate on six competition-math benchmarks. MCPO beats an unmodified GRPO baseline for all five data seeds, by 6.55 points of macro avg@32 on average (95\% CI $[4.1, 9.0]$), and a Qwen3-4B-Base replication improves for all three seeds ($+4.75$). The gain is largest on problems that GRPO solves only some of the time and grows with $k$ in pass@$k$, reaching 13.8 points at pass@32. MCPO models also write two to three times longer answers, and runs that write longer score higher; our experiments do not separate the two effects.

</details>

---

### [[20_Research/Papers/机器人/TransGHOST_Real-Time,_Synthesis-Free_Reconstruction_of_Instrument-Occluded_Regions_in_Ophthalmic_Microsurgery|TransGHOST: Real-Time, Synthesis-Free Reconstruction of Instrument-Occluded Regions in Ophthalmic Microsurgery]]

![[assets/2611.13971_figure.png|800]]

- **arXiv**: [2611.13971](https://arxiv.org/abs/2611.13971)
- **PDF**: https://arxiv.org/pdf/2611.13971
- **详细分析**: [[20_Research/Papers/机器人/TransGHOST_Real-Time,_Synthesis-Free_Reconstruction_of_Instrument-Occluded_Regions_in_Ophthalmic_Microsurgery|TransGHOST: Real-Time, Synthesis-Free Reconstruction of Instrument-Occluded Regions in Ophthalmic Microsurgery]]
- **作者**: Niran Nataraj, Maina Sogabe, Masamichi Yamashita, Norihiko Ito, Kenji Kawashima
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《TransGHOST: Real-Time, Synthesis-Free Reconstruction of Instrument-Occluded Regions in Ophthalmic Microsurgery》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Intraoperative scene perception in ophthalmic microsurgery is limited by instrument occlusion: when a tool enters the high-magnification field, it conceals tissue from both the surgeon and the perception components of robot-assisted systems that process the video. Generative inpainting can remove the occluder but replaces the missing image content with synthesis, which is unsuitable when visual provenance matters. Many video inpainters also depend on future frames and cannot operate online. We present TransGHOST, a causal reference-guided reconstruction pipeline whose non-generative safe mode operates in real time. Every restored value is obtained by resampling a recorded frame using geometric transforms fitted only to visible regions. The system provides per-pixel confidence and provenance and marks unsupported pixels as abstentions. We evaluate TransGHOST on a new veterinary clinical corpus of canine cataract surgery with pixel-level instrument and anatomy labels. Only the occluded region is scored, and each scoring target is verified to differ from the reference supplied to the system. Safe mode reaches 31.89 dB masked PSNR and 0.915 masked SSIM at 51.7 ms median and 85.5 ms 95th-percentile latency. On a pre-declared held-out cohort using instrument cutouts excluded from segmentation training, it reaches 29.83 dB masked PSNR, while matched-mask evaluation on validation shows a 3.45 dB advantage over LaMa. Region-aware reference selection improves masked PSNR by 3.60 dB over recency when candidate references can themselves be occluded. Reference-age analysis further defines the operating interval for the brief, repeated occlusions targeted by TransGHOST.

</details>

---

### [[20_Research/Papers/大模型/Controlled_Knowledge_Engineering_for_Taxonomy_Induction_with_Tool-Grounded_LLM_Agents_and_Runtime-Adaptive_Policies|Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies]]

![[assets/2611.13966_first_page.png|800]]

- **arXiv**: [2611.13966](https://arxiv.org/abs/2611.13966)
- **PDF**: https://arxiv.org/pdf/2611.13966
- **详细分析**: [[20_Research/Papers/大模型/Controlled_Knowledge_Engineering_for_Taxonomy_Induction_with_Tool-Grounded_LLM_Agents_and_Runtime-Adaptive_Policies|Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies]]
- **作者**: Jonas Limniatis, Bennet Schaarmann, Georg Reuber, Robert Stahlbock
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded LLM Agents and Runtime-Adaptive Policies》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TExEval, WordNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Taxonomies are structured knowledge representations that support semantic search, recommendation, product catalog organization, and retrieval-augmented generation. Their automated construction from a fixed set of candidate entities requires more than plausible text generation: the resulting hierarchy must be complete, structurally valid, and semantically coherent. Large Language Models (LLMs) are promising for this task, but iterative free-form generation remains vulnerable to omitted or hallucinated entities, invalid hierarchical relations, and inconsistent organizational principles. We introduce TIGA (Taxonomy Induction with Tool-Grounded Agents), a knowledge-engineering architecture that formulates taxonomy induction as an iterative decision process over an explicit state and constrained action space. TIGA combines executable taxonomy-editing tools, an memory that records tool calls, rationales, and outcomes, and a runtime-adaptive organizational policy that the agent revises during inference. An optional global reviewer evaluates the constructed taxonomy against the candidate set and the active policy. We evaluate TIGA on four benchmark taxonomies using two LLM backbones and compare it with single-shot and iterative prompting-based baselines. TIGA achieves the strongest structural-quality results in most evaluated configurations, but does not dominate on every precision measure. The gains are accompanied by substantially higher token consumption, API-call volume, and inference time. Ablation results show consistent benefits from the policy and interaction-memory components, whereas the effect of global review depends on the dataset and the available revision budget. These findings characterize tool grounding and runtime policy adaptation as promising but costly mechanisms for improving the controlled construction of structured knowledge representations.

</details>

---

### [[20_Research/Papers/大模型/Taxonomy-Agnostic_Neurosymbolic_Grounding_of_Robot_Kinematics|Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics]]

![[assets/2611.13850_first_page.png|800]]

- **arXiv**: [2611.13850](https://arxiv.org/abs/2611.13850)
- **PDF**: https://arxiv.org/pdf/2611.13850
- **详细分析**: [[20_Research/Papers/大模型/Taxonomy-Agnostic_Neurosymbolic_Grounding_of_Robot_Kinematics|Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics]]
- **作者**: Bastien Dussard, Aur{é}lie Clodic, Guillaume Sarthou
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Taxonomy-Agnostic Neurosymbolic Grounding of Robot Kinematics》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While symbolic reasoning for task allocation requires grounding a robot's physical capabilities, standard Unified Robot Description Format (URDF) files provide only low-level kinematics without the formal semantic context needed for reasoning. We present URDF2Ontology, an automated, taxonomy-agnostic neurosymbolic framework that transforms raw URDF files into populated, grounded OWL ontologies. It leverages a Large Language Model (LLM) for targeted semantic reasoning, coupled with an iterative sequential graph-purging mechanism to prevent context window saturation. To process complex kinematic structures, it employs a morphology-aware dual-track architecture featuring a bottom-up Tree Track for branching assemblies and a top-down Chain Track for serial limbs. Guided by neurosymbolic guardrails, the framework extracts functional sub-graphs and asserts populated ontologies aligned with arbitrary user-provided taxonomies. Empirical evaluation across a diverse fleet of heterogeneous robots demonstrates strong schema alignment, valid structural extraction, and a significant reduction in manual domain authoring overhead.

</details>

---

### [[20_Research/Papers/大模型/Integrating_Action_Prefix_Prediction_and_Alignment_Across_Modalities_for_Multimodal_Reinforcement_Learning|Integrating Action Prefix Prediction and Alignment Across Modalities for Multimodal Reinforcement Learning]]

![[assets/2611.13782_figure.png|800]]

- **arXiv**: [2611.13782](https://arxiv.org/abs/2611.13782)
- **PDF**: https://arxiv.org/pdf/2611.13782
- **详细分析**: [[20_Research/Papers/大模型/Integrating_Action_Prefix_Prediction_and_Alignment_Across_Modalities_for_Multimodal_Reinforcement_Learning|Integrating Action Prefix Prediction and Alignment Across Modalities for Multimodal Reinforcement Learning]]
- **作者**: Sijie Xu, Francisco Cruz
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Integrating Action Prefix Prediction and Alignment Across Modalities for Multimodal Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CURL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning representations from multimodal observations is difficult in reinforcement learning with limited interaction data. Multimodal Joint Predictive Representation combines multimodal latent prediction with contrastive learning across modalities, but its recursive rollout depends on earlier predictions and its pairwise alignment focuses on correspondence between modalities. We propose Improved Predictive Representation, which combines prediction from action prefixes with alignment at the observed anchor based on Contrastive Multimodal learning. At each horizon, it predicts future representations directly from the observed anchor and the corresponding sequence of actions. We evaluate two crop configurations: IPR-S with a minimum retained crop area of 10%, and IPR-H with 50%. Across five DeepMind Control Suite tasks, IPR-H achieves an average return across tasks that is 10.0% higher than the baseline with visual and depth images and 3.4% higher with visual images and position vectors. The relative performance of the two configurations varies across tasks. In Webots, both IPR configurations achieve higher mean final returns than the baseline without LiDAR, but not when LiDAR is available.

</details>

---

### [[20_Research/Papers/具身智能/Softness_is_something_you_also_need!_Why_compliance_helps_control_information_metrics_of_a_passive_walker_with_compliant_ankle|Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle]]

![[assets/2611.13779_figure.png|800]]

- **arXiv**: [2611.13779](https://arxiv.org/abs/2611.13779)
- **PDF**: https://arxiv.org/pdf/2611.13779
- **详细分析**: [[20_Research/Papers/具身智能/Softness_is_something_you_also_need!_Why_compliance_helps_control_information_metrics_of_a_passive_walker_with_compliant_ankle|Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle]]
- **作者**: Fabio Bonsignorio, Elisabetta Barletta, Sorin Dragomir, Francesco Esposito, Enrica Zereik
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Softness is something you also need! Why compliance helps control: information metrics of a passive walker with compliant ankle》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A great gap in adaptivity, flexibility, and dexterity still exists between intelligent robots, whether they are made of rigid or (partially) compliant components, and their naturally evolved animal and vegetal counterparts. One reason could be of `paradigm' nature. On the one hand, most robots (both rigid and soft) are still designed by following a `Cartesian' approach, with top-down control and a clear mind-body separation. Designing artificial agents on the basis of the principles that we observe in biology is not an easy task. The principles of organization of animals and plants rely on morphological computation and emergence of fit behaviors from loosely coupled networks of embodied agents. Modeling and control require radically new approaches. In this paper we briefly recall and explain some seminal mathematical results linking information metrics and dynamics of the agents, already published years ago; we integrate them with some recent methods developed by us and by the community, we highlight some brief remarks about their relevance and we hint to our current and near future work towards finding concrete and efficient ways for the modeling and control of completely or partially compliant artificial agents and for a better understanding of physical intelligence in nature. We present a technical note summarizing phase-space volume calculations for inverted-pendulum and passive-dynamic walking models, following our proposed framework. Starting from the McGeer compass gait, we introduce knee-ankle compliance, foot-rocker effects, and a Ruina-style compass gait with distributed leg inertia. Standard heel-strike maps are derived and used in the estimation of viable phase-space volumes $W(γ)$, based on a state-dependent Monte-Carlo and Reproducing Kernel Hilbert Spaces methods. We show how the methods based on RKHS allow deeper and more subtle analysis.

</details>

---

### [[20_Research/Papers/强化学习/Broad-Persistent_Advising_in_Interactive_Reinforcement_Learning_via_Latent_State_Encoding|Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding]]

![[assets/2611.13712_figure.png|800]]

- **arXiv**: [2611.13712](https://arxiv.org/abs/2611.13712)
- **PDF**: https://arxiv.org/pdf/2611.13712
- **详细分析**: [[20_Research/Papers/强化学习/Broad-Persistent_Advising_in_Interactive_Reinforcement_Learning_via_Latent_State_Encoding|Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding]]
- **作者**: Zhuoran Liang, Francisco Cruz
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Broad-Persistent Advising in Interactive Reinforcement Learning via Latent State Encoding》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IntRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep Interactive Reinforcement Learning (Deep IntRL) accelerates reinforcement learning training by incorporating external advice. However, conventional Deep IntRL uses each piece of advice only in the current step and discards it after a single interaction. Persistent Advising and Broad-Persistent Advising (BPA) extend this process by storing advice in persistent memory and reusing it in similar states through state generalisation based on K-means clustering. This research proposes Encoder BPA, which employs a latent encoder to retrieve and reuse advice. In this framework, a trained encoder is used to map a state sequence into a latent representation at every time step. Advice can be retrieved through latent comparison, together with a top-(k) aggregation and a consistency condition to improve reuse stability. Experimental results show that Encoder BPA improves learning efficiency and advice utilisation at an early stage of training compared with different Deep IntRL approaches, especially in complex and partially observable environments.

</details>

---

### [[20_Research/Papers/强化学习/Ego_Guidance_Enhancing_Robot_Policy_Learning_with_Action-Free_Human_Egocentric_Videos|Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos]]

![[assets/2611.13685_figure.png|800]]

- **arXiv**: [2611.13685](https://arxiv.org/abs/2611.13685)
- **PDF**: https://arxiv.org/pdf/2611.13685
- **详细分析**: [[20_Research/Papers/强化学习/Ego_Guidance_Enhancing_Robot_Policy_Learning_with_Action-Free_Human_Egocentric_Videos|Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos]]
- **作者**: Lin Long, Tianren Ma, Zhong Chu, Di Wu, Maosong Cao, Qixiang Ye, Junbo Zhao, Shanghang Zhang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Ego Guidance: Enhancing Robot Policy Learning with Action-Free Human Egocentric Videos》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we investigate how human egocentric videos can benefit robot policy learning without action supervision. Building on a pretrained VLM, we propose Shared Prediction on Action and Representation (SPAR), an MoT architecture in which future visual state prediction can provide independent and complementary learning signals alongside action prediction. We find that representations learned from egocentric videos improve downstream performance on out-of-distribution robot tasks, with further gains as video data scales. We also study the effects of objective choices and data curation, providing insights into how to leverage action-free videos for scalable robot learning.

</details>

---

### [[20_Research/Papers/具身智能/A_computational_framework_for_understanding_embodied_plans|A computational framework for understanding embodied plans]]

![[assets/2611.13669_figure.png|800]]

- **arXiv**: [2611.13669](https://arxiv.org/abs/2611.13669)
- **PDF**: https://arxiv.org/pdf/2611.13669
- **详细分析**: [[20_Research/Papers/具身智能/A_computational_framework_for_understanding_embodied_plans|A computational framework for understanding embodied plans]]
- **作者**: Aalap D. Shah, Basil Saeed, Joshua B. Tenenbaum, Tobias Gerstenberg, Hyowon Gweon, Ilker Yildirim
- **cs 子类**: cs.AI, cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《A computational framework for understanding embodied plans》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning about people's plans and goals based on their actions is fundamental to human social interaction and essential for cooperative, embodied artificial intelligence. Formalizing this capacity in naturalistic, embodied settings has been a longstanding challenge. Here, we present GenEA, a novel agent representation capable of reasoning over multi-step, long-horizon embodied plans. At the heart of GenEA lies a multilevel state-space that couples the coarse biomechanics of an articulated body and its interactions with nearby objects by extending the task-and-motion planning framework from robotics with simulation-based intuitive physics. By embedding this state-space in a generative model, GenEA yields a joint probability distribution over goals and embodied plans. Across several experiments spanning the qualitatively distinct domains of object manipulation and navigation, featuring diverse tasks and multiple behavioral measures, we show that GenEA, through simple transformations of this joint distribution, recapitulates how humans reason about embodied plans. Crucially, GenEA consistently outperforms strong alternative models, including plausible heuristics, standard task-and-motion planning, and a state-of-the-art vision-language model. GenEA thereby offers a new perspective on the architecture of human reasoning and social cognition, suggesting that embodied artificial intelligence systems seeking to seamlessly interact with humans should adopt GenEA-like generative models of action planning.

</details>

---

### [[20_Research/Papers/大模型/DrugCoding_A_Scientific_Programming_Agent_for_Drug_Discovery|DrugCoding: A Scientific Programming Agent for Drug Discovery]]

![[assets/2611.13651_figure.png|800]]

- **arXiv**: [2611.13651](https://arxiv.org/abs/2611.13651)
- **PDF**: https://arxiv.org/pdf/2611.13651
- **详细分析**: [[20_Research/Papers/大模型/DrugCoding_A_Scientific_Programming_Agent_for_Drug_Discovery|DrugCoding: A Scientific Programming Agent for Drug Discovery]]
- **作者**: Junwei Hu, Zhuohao Lin, Kun Li, Hengnan Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《DrugCoding: A Scientific Programming Agent for Drug Discovery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Drug discovery involves multiple interconnected research stages, including molecular design, property prediction, and virtual screening. These processes are characterized by complex workflows, interdependent computational tasks, and diverse specialized tools, placing substantial demands on the coordination of scientific models and computational resources. However, existing large language model (LLM)-based scientific agents still face challenges in autonomous planning of complex tasks, adaptive selection of specialized models, and reliable execution of multi-stage scientific computations, limiting their effectiveness in automating complex drug discovery workflows. To address these challenges, we propose DrugCoding, a scientific programming agent system that integrates scientific task planning, adaptive model routing, multi-agent collaboration, and programmatic tool execution. DrugCoding enables autonomous task planning and dynamic model adaptation for complex research objectives. It can flexibly invoke specialized scientific models, autonomously generate and execute code according to task requirements, and leverage multi-agent collaboration to support efficient execution and reliable validation of complex scientific tasks. To evaluate DrugCoding's performance in scientific tool invocation and multi-stage task execution, we conduct multi-turn tool-calling experiments across diverse language models and scientific tool interfaces. Experimental results demonstrate that DrugCoding achieves an average session-level Pass@1 of 97.35% on the full benchmark, outperforming the strongest baseline, Codex, by 9.24%. On the challenging subset, DrugCoding achieves 97.92%, exceeding the strongest baseline.

</details>

---

### [[20_Research/Papers/大模型/Synapse-Control_Making_Agent_Experience_Actionable_with_Lightweight_Runtime_Control|Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control]]

![[assets/2611.13615_first_page.png|800]]

- **arXiv**: [2611.13615](https://arxiv.org/abs/2611.13615)
- **PDF**: https://arxiv.org/pdf/2611.13615
- **详细分析**: [[20_Research/Papers/大模型/Synapse-Control_Making_Agent_Experience_Actionable_with_Lightweight_Runtime_Control|Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control]]
- **作者**: Zhiyuan Huang, Shengan Zheng, Chenghu Yang, Song Zhang, Lingyun Li, Chen Yu, Weiquan Huang, Linpeng Huang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Synapse-Control: Making Agent Experience Actionable with Lightweight Runtime Control》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model agents reuse execution experience to improve reliability on complex tool-based tasks. Systems such as Sentry call large models to generate failure diagnoses before retrieving advice, adding inference cost to experience reuse. We present Synapse-Control, an agent runtime whose lightweight control plane selects advice and determines when to send it to the task-executing model. Rules shortlist relevant advice, and a lightweight 1.7B classifier fine-tuned on teacher-labeled state-suggestion pairs scores those candidates instead of generating a diagnosis. Micro-contracts encode reusable interface checks, such as required arguments or valid options, without prescribing complete task programs. A Prompt Value Table records earlier guidance and feedback to limit repeated suggestions through cooldown and token-budget checks. Across 1,308 attempts per method in AppWorld and WebShop, Synapse-Control achieves 270 successes (29.8% more than Base), replaces 4,987 generative diagnosis calls, and reduces auxiliary control time relative to Sentry by 50.2% and 51.0%, respectively.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Reliable_VLM_Judges_State-Conditional_Invariance_and_Presentation-Aware_Diagnostics|Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics]]

![[assets/2611.13596_figure.png|800]]

- **arXiv**: [2611.13596](https://arxiv.org/abs/2611.13596)
- **PDF**: https://arxiv.org/pdf/2611.13596
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Reliable_VLM_Judges_State-Conditional_Invariance_and_Presentation-Aware_Diagnostics|Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics]]
- **作者**: Qinan Zhang, Xinyu Wang, Qihang Jin, Tianyuan Wang, Hongbing Luo, Pengfei Li, Wenjun Lv, Yu Kang, Jian Di
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.85（加权：具身智能 0.3，大模型 0.55）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Towards Reliable VLM Judges: State-Conditional Invariance and Presentation-Aware Diagnostics》归入 大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Habitat-Sim, MiniWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) are increasingly used as automated judges for multimodal and embodied tasks, yet aggregate accuracy or consistency alone does not reveal whether a judge changes its verdict for the right reason. We propose State-Conditional Invariance (SCI), a reliability principle requiring a judge to remain stable under semantics-preserving changes in presentation while responding to causal interventions that change the task outcome. We instantiate SCI in GridWM-Judge, a simulator-grounded diagnostic benchmark built from deterministic MiniGrid trajectories with aligned Full, evidence-removal, and counterfactual variants, plus presentation and representation probes. Across five diagnostic tasks, GridWM-Judge tests local perception, action-conditioned transitions, presentation stability, representation exchangeability, and Full-CF causal discrimination. Our diagnostic evaluations reveal heterogeneous failure modes, including sensitivity to evidence presentation and encoding, low activation on successful trajectories, and weak paired counterfactual discrimination. Perception-controlled analyses further indicate that visual grounding and objective recovery are substantial, model-dependent bottlenecks. These results motivate jointly reporting correctness, presentation stability, and causal sensitivity instead of relying on a single score.

</details>

---

### [[20_Research/Papers/强化学习/Sharp_Sample_Complexity_of_KL-Regularized_Reinforcement_Learning|Sharp Sample Complexity of KL-Regularized Reinforcement Learning]]

![[assets/2611.13480_first_page.png|800]]

- **arXiv**: [2611.13480](https://arxiv.org/abs/2611.13480)
- **PDF**: https://arxiv.org/pdf/2611.13480
- **详细分析**: [[20_Research/Papers/强化学习/Sharp_Sample_Complexity_of_KL-Regularized_Reinforcement_Learning|Sharp Sample Complexity of KL-Regularized Reinforcement Learning]]
- **作者**: Andrew Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Sharp Sample Complexity of KL-Regularized Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

KL-regularized reinforcement learning, the objective behind maximum-entropy RL and RL from human feedback, is variational inference in the graphical model of "control as inference": the regularized optimal policy is a posterior over trajectories, and the suboptimality of a policy is $β$ times a KL divergence between path measures. However, it is not known how many samples it takes to learn this posterior, even with a generative model. Earlier $1/ε$ guarantees scale with $H^5$ in the effective horizon $H$, and no lower bound for MDPs depends on the temperature $β$. In this work, we show that for a discounted MDP with $K$ state-action pairs, the plug-in estimator finds a policy that is $ε$-optimal from every initial state with $\widetilde{O}(KH^3/(ε\max\{ε,β\}) + KH)$ samples, and that no algorithm, even one that chooses where to sample, can do with fewer when $ε\lesssim \min\{H, H^2/β\}$. For $ε&lt; β$ this is a $1/ε$ rate with the same horizon dependence as unregularized RL. We also find the exact asymptotic constant of the plug-in estimator, a Fisher-weighted variance of the estimated soft Q-function. The estimator is locally asymptotically minimax among methods that sample every pair equally often, and we give the allocation of samples that is optimal among adaptive designs. Simulations on small MDPs match the rates and the constants.

</details>

---

### [[20_Research/Papers/大模型/SteerDistill_Quantizing_LLM_Agents_via_Closed-Loop_Teacher_Steering|SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering]]

![[assets/2611.13410_figure.png|800]]

- **arXiv**: [2611.13410](https://arxiv.org/abs/2611.13410)
- **PDF**: https://arxiv.org/pdf/2611.13410
- **详细分析**: [[20_Research/Papers/大模型/SteerDistill_Quantizing_LLM_Agents_via_Closed-Loop_Teacher_Steering|SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering]]
- **作者**: Genming Cui, Xiangyu Li, Zixu Hao, Xin Ding, Yunxin Liu, Ting Cao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《SteerDistill: Quantizing LLM Agents via Closed-Loop Teacher Steering》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：QeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-bit quantization reduces the inference cost of LLM agents but can compromise task success. Examining failed rollouts, we find that quantized agents overlook task requirements or environmental conditions, producing environment transitions that diverge from successful full-precision references. Correcting these behavioral divergences remains difficult: offline data may miss the student's failure contexts, while its own rollouts may provide few correct responses in those contexts. We introduce SteerDistill, a quantization-aware distillation method in which a full-precision teacher guides the student to revise failed responses and iteratively refines its guidance using feedback from student execution. This closed-loop teacher steering produces locally verified behavioral corrections. We internalize these corrections by training the student without guidance to match the steered student's predictions at corrected turns and the full-precision teacher's at other turns, enabling unassisted inference. Across five agentic benchmarks and three models, SteerDistill exceeds the strongest quantized baseline by 1.67--2.18 points in average score under W4A16 and stays within one point of BF16. On $τ^2$-Bench, it outperforms QeRL by 1.84 percentage points in success rate using 67% fewer training GPU hours and produces shorter successful trajectories than the quantized baselines.

</details>

---

### [[20_Research/Papers/机器人/Curie's_Jarvis_Autonomous_Robotic_Chemistry_Experiments_from_Printed_Protocols|Curie's Jarvis: Autonomous Robotic Chemistry Experiments from Printed Protocols]]

![[assets/2611.13251_figure.png|800]]

- **arXiv**: [2611.13251](https://arxiv.org/abs/2611.13251)
- **PDF**: https://arxiv.org/pdf/2611.13251
- **详细分析**: [[20_Research/Papers/机器人/Curie's_Jarvis_Autonomous_Robotic_Chemistry_Experiments_from_Printed_Protocols|Curie's Jarvis: Autonomous Robotic Chemistry Experiments from Printed Protocols]]
- **作者**: Rumi Loghmani, Bozhang Song, Victor Alvarado, Aliyah Redding, Amir Barati Farimani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Curie's Jarvis: Autonomous Robotic Chemistry Experiments from Printed Protocols》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：BioProVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A person running a bench experiment works from a printed instruction sheet, tells identical containers apart by the labels written on them, and looks at the bench again before each step. Lab automation usually works the other way around: the procedure is written as a script, and containers stand at fixed positions or carry fiducial markers. We present Curie's Jarvis, a system that lets a robot arm carry out a chemistry experiment on a bench set up for people. It reads the steps from a photo of the printed sheet, finds containers on an ordinary bench with no fixed positions or markers, tells identical-looking containers apart by reading their labels in four camera views, locates its target again before every step, and sets how each step is carried out, including its speed, from what is being handled. On a Franka Panda arm, Curie's Jarvis completed 5 of 5 runs of one protocol from a children's chemistry kit and 4 of 5 runs of another, with no human intervention, and in 160 locates on printed and handwritten labels it identified every container correctly. This brings robots a step closer to doing bench chemistry the way people do.

</details>

---

### [[20_Research/Papers/大模型/Cognitive_Multi-Agent_Search_and_Rescue_Language-Grounded_Hierarchical_Reinforcement_Learning_for_Collaborative_Robotics|Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics]]

![[assets/2611.13161_first_page.png|800]]

- **arXiv**: [2611.13161](https://arxiv.org/abs/2611.13161)
- **PDF**: https://arxiv.org/pdf/2611.13161
- **详细分析**: [[20_Research/Papers/大模型/Cognitive_Multi-Agent_Search_and_Rescue_Language-Grounded_Hierarchical_Reinforcement_Learning_for_Collaborative_Robotics|Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics]]
- **作者**: Sepideh Ravanbakhsh, Hamidreza Moradi
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 强化学习
- **相关性评分**: 2.6（加权：大模型 0.8，强化学习 0.8，机器人 1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Cognitive Multi-Agent Search and Rescue: Language-Grounded Hierarchical Reinforcement Learning for Collaborative Robotics》归入 机器人、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LG-HRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective search and rescue (SAR) operations require autonomous systems capable of coordinating multiple heterogeneous agents, adapting to dynamic hazards, and aligning with human mission intent. Existing language-guided reinforcement learning (RL) methods primarily focus on single-agent instruction following and lack mechanisms for team-level coordination in complex, partially observable environments. This paper presents a Cognitive Multi-Agent Framework based on Language-Grounded Hierarchical Reinforcement Learning (LG-HRL) that integrates natural-language understanding, hierarchical policy decomposition, and a shared cognitive workspace to achieve cohesive multi-agent behavior in SAR scenarios. Human instructions are interpreted by a large language model (LLM) and transformed into structured semantic cues that guide high-level strategy selection and role assignment across UAV and UGV agents. A formal Language-Grounded Multi-Agent Hierarchical Decision Process (LG-MAHDP) is introduced to model the interplay between semantic grounding, hierarchical control, and distributed coordination. Comprehensive experiments in a simulated disaster environment show that LG-HRL improves learning speed by 2.3 times, increases coordination coherence by 37%, and enhances subgoal accuracy and hazard avoidance by 46% and 31%, respectively. The system achieves 20-30% higher victim rescue rates, demonstrates emergent role specialization, and adapts immediately to human verbal updates. Ablation studies confirm that both the shared cognitive workspace and language grounding are critical to overall system performance. Overall, this work establishes a new paradigm for language-guided multi-agent SAR robotics, demonstrating that semantic grounding combined with hierarchical reasoning enables safer, more efficient, and more interpretable autonomous rescue operations.

</details>

---

### [[20_Research/Papers/具身智能/How_Much_of_Your_VLA_Is_kNN|How Much of Your VLA Is kNN]]

![[assets/2611.13160_figure.png|800]]

- **arXiv**: [2611.13160](https://arxiv.org/abs/2611.13160)
- **PDF**: https://arxiv.org/pdf/2611.13160
- **详细分析**: [[20_Research/Papers/具身智能/How_Much_of_Your_VLA_Is_kNN|How Much of Your VLA Is kNN]]
- **作者**: Denis Grachev, Damien LaRocque, Omar Moured
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《How Much of Your VLA Is kNN》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models now exceed 95% success on the LIBERO simulation benchmark, yet it remains unclear how much of this performance requires generalization beyond the training demonstrations. In this work, we show that retrieving nearby demonstrations and reusing their action chunks achieves a success rate of 91.7 % on LIBERO without policy training. Under LIBERO-Plus perturbations, retrieval shows the smallest drop of all evaluated policies. Across nine publicly available VLAs, fine-tuning mostly makes the vision-language backbone a better retrieval key, and the actions of the VLAs remain close to the demonstrations. In addition, we introduce Local Action Consistency (LAC), an offline metric that measures whether nearby observations in representation space are also associated with similar future actions. We show that LAC tracks the success rate of retrieval and can guide the training of a retrieval key. Our evaluation and source code are available at https://github.com/sereact/lerobot_knn.

</details>

---

### [[20_Research/Papers/大模型/ASPIRE_An_Agentic_System-Identification_Platform_for_Iterative_Reasoning_and_Exploration|ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration]]

![[assets/2611.13114_figure.png|800]]

- **arXiv**: [2611.13114](https://arxiv.org/abs/2611.13114)
- **PDF**: https://arxiv.org/pdf/2611.13114
- **详细分析**: [[20_Research/Papers/大模型/ASPIRE_An_Agentic_System-Identification_Platform_for_Iterative_Reasoning_and_Exploration|ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration]]
- **作者**: Erik Derner, Jiří Kubalík, Robert Babuška
- **cs 子类**: cs.AI, cs.CL, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.25（加权：具身智能 0.3，大模型 0.45，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《ASPIRE: An Agentic System-Identification Platform for Iterative Reasoning and Exploration》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

System identification requires expert decisions on the identification method, incorporation of prior physical knowledge, and model validation. We propose ASPIRE, a framework for nonlinear system identification in which a large language model agent selects and executes the identification method. ASPIRE constructs closed-form, nonlinear static or dynamic models from measured data, optionally supplemented by a system description, the intended use of the model, and physical requirements expressed formally or in natural language. Each model includes its parameters, an estimation record, an interpretation of its terms, and an error evaluated on test data inaccessible to the agent. Formal physical requirements are verified independently. ASPIRE operates autonomously or interactively, allowing the agent to ask questions and the user to request further analyses and identification rounds. We evaluate ASPIRE on three measured systems: a mobile robot, a rotational system with dry friction, and a laboratory fermenter. Each system is tested with and without a description, in five runs per task. All 30 runs delivered valid models, at a cost of 0.96 to 3.38 US dollars per run. An assessment by the authors found that, for the 30 models recommended by the agent, one per run, the interpretation of the model and the documentation of its structure selection and parameter estimation fully satisfied 132 of 150 assessed items and partly satisfied 18. The most frequent discrepancy, found in nine models, concerned inaccurate or unsupported claims about model structure selection.

</details>

---

### [[20_Research/Papers/具身智能/Building_World_Models_from_Intrinsic_Motivation|Building World Models from Intrinsic Motivation]]

![[assets/2611.13113_figure.png|800]]

- **arXiv**: [2611.13113](https://arxiv.org/abs/2611.13113)
- **PDF**: https://arxiv.org/pdf/2611.13113
- **详细分析**: [[20_Research/Papers/具身智能/Building_World_Models_from_Intrinsic_Motivation|Building World Models from Intrinsic Motivation]]
- **作者**: Reece Keller, Declan Kutscher, Xaq Pitkow, Aran Nayebi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习, 具身智能
- **相关性评分**: 2.02（加权：具身智能 0.3，强化学习 0.36，世界模型 1.36）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Building World Models from Intrinsic Motivation》归入 世界模型、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Proto-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the absence of extrinsic rewards or task supervision, human behavior is guided by intrinsic motivation---neural signals that drive curiosity, creativity, play, and other essential facets of intelligence. Intrinsic motivation plays an important developmental role in building robust world models that enable generalization and adaptation. Yet existing studies leave open how a broad range of intrinsic motivations interacts with world-model representation learning to support downstream control. This limits our understanding of which intrinsically collected experiences build reusable models. To address these gaps, we integrate 24 intrinsic objectives, including established methods and explicit variants spanning curiosity, entropy, and competency, into a common model-based reinforcement learning framework. We evaluate the world models they build through zero-shot, few-shot, and multi-task control in locomotion, manipulation, and open-ended gaming environments, using three representation-learning strategies: observation reconstruction, latent prediction, and redundancy reduction. Curiosity-driven exploration with observation reconstruction yields the strongest aggregate family profile, although the best individual pairing depends on the experiment. In compositional vision-based tasks, intrinsic motivation derived from both episodic and lifelong novelty---providing a complementary memory to the world model's generic recurrent state---achieves the best zero-shot transfer and few-shot adaptation. These findings motivate designing intrinsic motivation and representation learning jointly. Our results demonstrate world models as a powerful tool for measuring the quality of intrinsically motivated experience, and positions intrinsic motivation as a key ingredient for building world models autonomously.

</details>

---

### [[20_Research/Papers/具身智能/APS-VLA_Action-Guided_and_Future-Aware_Token_Pruning_for_Efficient_Vision-Language-Action_Models|APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models]]

![[assets/2611.13030_figure.png|800]]

- **arXiv**: [2611.13030](https://arxiv.org/abs/2611.13030)
- **PDF**: https://arxiv.org/pdf/2611.13030
- **详细分析**: [[20_Research/Papers/具身智能/APS-VLA_Action-Guided_and_Future-Aware_Token_Pruning_for_Efficient_Vision-Language-Action_Models|APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models]]
- **作者**: Xiaoyang Xing, Chun-Mei Feng, Anthony Cohn, Xiaoliang Gong, Asoke Nandi
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 2.7，机器人 0.4）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《APS-VLA: Action-Guided and Future-Aware Token Pruning for Efficient Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：APS-VLA, LightVLA, OpenVLA, Real-World, SpecPrune-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies have demonstrated strong generalization in robotic manipulation, yet processing dense visual tokens often incurs high inference latency. Visual token pruning offers a practical way to reduce this cost, but identifying a compact set of tokens that preserves reliable action generation remains challenging. Existing methods largely rely on static or immediate heuristic cues to estimate token importance. We introduce APS-VLA, a framework that learns visual token selection from robot demonstrations while keeping the pretrained VLA backbone frozen. A lightweight Decision Influence Estimator scores tokens conditioned on current visual observations, language instructions, and robot proprioception. Its training combines two complementary signals: action supervision matches both the full-input policy predictions and demonstrated actions, while an auxiliary visual transition objective uses demonstrated actions to predict subsequent visual features from the selected representation. At deployment, the estimator performs a single hard selection and packing step before the policy's native action-generation procedure; the auxiliary predictor is removed. Experiments with OpenVLA-OFT on LIBERO and with $π_{0.5}$ and XR-1 on RoboCasa365 demonstrate inference acceleration with modest changes in task success. Across five real-world tasks on two dual-arm platforms, APS-VLA reduces mean policy inference latency from 137.25 to 93.25 ms, achieving a $1.47\times$ speedup with an average success rate of 61%, compared with 60% for the unpruned baseline. Together, these results support APS-VLA as a modular, plug-in framework for efficient robotic control across VLA architectures, preserving the underlying policy parameters and native action-generation procedure.

</details>

---

### [[20_Research/Papers/具身智能/GTAGym_Real_AAA_Game_Tasks_Environment_for_Evaluation_and_Reinforcement_Learning|GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning]]

![[assets/2611.13028_figure.png|800]]

- **arXiv**: [2611.13028](https://arxiv.org/abs/2611.13028)
- **PDF**: https://arxiv.org/pdf/2611.13028
- **详细分析**: [[20_Research/Papers/具身智能/GTAGym_Real_AAA_Game_Tasks_Environment_for_Evaluation_and_Reinforcement_Learning|GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning]]
- **作者**: Jiajun Chen, Shicheng Fang, Jiahao Lu, Yuxin Wang, Xipeng Qiu
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.15（加权：大模型 0.35，强化学习 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《GTAGym: Real AAA Game Tasks Environment for Evaluation and Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GTAGym, GTAVBench, GameHorizon-Bench, GameWorld, LongPuzzleBench, VideoGameBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AAA games offer a rich testbed for evaluating agent perception, reasoning, and control. However, evaluating whether agents can complete tasks in AAA games is challenging and often human-annotated because task outcomes are often difficult to verify automatically, let alone applying it for Reinforcement Learning (RL). We introduce GTAGym, an environment and framework for evaluation and RL on GTA V tasks. Its evaluation benchmark, GTAVBench, derived from GTA V main-story missions, contains 103 online tasks reconstructed across nine task families, alongside 47 image-based shooting and sniping tasks using GTA V imagery. A web server provides access to the online environment and evaluation interface, supporting parallel testing through screenshots and keyboard-mouse actions with automatic engine-state outcome checks. We evaluate six frontier LLMs on GTAVBench with textual task instructions and on its GTAVBench-AGI branch, where instructions appear only in the first screenshot and a harness automatically compresses interaction history. The best configuration achieves 70.9% overall accuracy in GTAVBench-AGI, yet aerial navigation, evasion and interception remain difficult. GTAGym also provides a scalable generator that samples task parameters within user-specified ranges and option sets under fixed templates, creating batches of 3D and image-based shooting environments for RL with automatic reward and termination signals. LoRA RL of Qwen3.8-27B on generated on-foot navigation tasks improves the in-domain performance and transfers to out-of-domain task categories, and native GTA V tasks from 15% to 23%.

</details>

---

### [[20_Research/Papers/大模型/From_Questions_to_Decisions_Benchmarking_How_LLM_Agents_Acquire_Decision-Relevant_Information_from_Human_Beings|From Questions to Decisions: Benchmarking How LLM Agents Acquire Decision-Relevant Information from Human Beings]]

![[assets/2611.13015_first_page.png|800]]

- **arXiv**: [2611.13015](https://arxiv.org/abs/2611.13015)
- **PDF**: https://arxiv.org/pdf/2611.13015
- **详细分析**: [[20_Research/Papers/大模型/From_Questions_to_Decisions_Benchmarking_How_LLM_Agents_Acquire_Decision-Relevant_Information_from_Human_Beings|From Questions to Decisions: Benchmarking How LLM Agents Acquire Decision-Relevant Information from Human Beings]]
- **作者**: Yuhan Tang, Ke Fan, Xinkai Zou, Baichuan Mo, Kangxin Cui, Ao Qu, Ou Zheng, Jiangbo Yu, Haris N. Koutsopoulos, Jinhua Zhao, Yuan Zhou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《From Questions to Decisions: Benchmarking How LLM Agents Acquire Decision-Relevant Information from Human Beings》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：QuestBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents are increasingly asked to make plans for people, such as scheduling drivers or assigning nurses. However, people's requests are often incomplete, and the supporting information for decision-making may be outdated, requiring agents to ask for clarification. Existing benchmarks typically provide fully specified problems or rely on uncalibrated LLM-simulated users, leaving this ability insufficiently tested. We introduce Ask2Decide, a benchmark of 43 planning tasks that evaluates whether agents ask for missing information that matters for their decisions. An operator holds facts absent from the agent's request and records, and optimization solvers determine which facts change the optimal plan. We also include similarly worded facts that leave the optimal plan unchanged to test whether agents distinguish useful information from irrelevant details. We collect 79 interaction sessions from 19 participants and find that, after an incorrect plan, human replies omit the correcting fact far more often than replies from an uncalibrated simulated user (43% versus 7%). Using these interactions, we calibrate a simulated operator that more closely matches human reply patterns. Evaluating four frontier LLMs, we find that their initial plans are infeasible on 58-98% of tasks when information is missing, compared with 5-28% when all facts are provided upfront. Agents uncover facts that change the optimal plan only slightly more often than facts that leave it unchanged (39-52% versus 32-41%). These results show that obtaining decision-relevant information through interaction remains a major bottleneck for LLM planning. This is ongoing work and will be updated. The date of this version is shown on the first page.

</details>

---

### [[20_Research/Papers/具身智能/PhysMoE_Fast_Spatial_Grounding_with_Single-Token_Coordinate_Representation_in_Modality-Decoupled_VLMs|PhysMoE: Fast Spatial Grounding with Single-Token Coordinate Representation in Modality-Decoupled VLMs]]

![[assets/2611.13000_figure.png|800]]

- **arXiv**: [2611.13000](https://arxiv.org/abs/2611.13000)
- **PDF**: https://arxiv.org/pdf/2611.13000
- **详细分析**: [[20_Research/Papers/具身智能/PhysMoE_Fast_Spatial_Grounding_with_Single-Token_Coordinate_Representation_in_Modality-Decoupled_VLMs|PhysMoE: Fast Spatial Grounding with Single-Token Coordinate Representation in Modality-Decoupled VLMs]]
- **作者**: Ruimeng Liu, Denan Liang, Ruofei Bai, Fuming Zhang, Kuan Xu, Shenghai Yuan, Lihua Xie
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《PhysMoE: Fast Spatial Grounding with Single-Token Coordinate Representation in Modality-Decoupled VLMs》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Vision-Language Models (VLMs) are backbones for robotic planning and manipulation. However, for coordinate prediction in grounding tasks, existing architectures suffer from two distinct bottlenecks: discrete tokenization disrupts spatial continuity with high decoding latency, while standard point regression fails on multi-contact affordances and irregularly shaped targets. To resolve these challenges, we propose PhysMoE, introducing three core contributions: (1) sharing lower layers for multimodal context while routing upper layers to specialized spatial (pixel) and linguistic (text) experts by physical modality, eliminating gradient interference; (2) encoding each coordinate as a single token by reusing the visual encoder's learned positional embeddings, injecting 2D spatial priors to natively align coordinates with visual features and ease training; and (3) differentiable Signed Distance Field (SDF) supervision on pointing, accommodating affordances and irregular geometries without costly mask decoders. Compared to the base model, PhysMoE achieves a 15.7% average gain and an 8.31x throughput speedup across 9 coordinate-based grounding benchmarks (trajectory, affordance, and localization), while preserving multimodal understanding and reasoning across 11 text-based embodied benchmarks.

</details>

---

### [[20_Research/Papers/大模型/ICLayout-Bench_Benchmarking_LLM_Agents_for_Custom_Circuit_Layout_Design|ICLayout-Bench: Benchmarking LLM Agents for Custom Circuit Layout Design]]

![[assets/2611.12982_figure.png|800]]

- **arXiv**: [2611.12982](https://arxiv.org/abs/2611.12982)
- **PDF**: https://arxiv.org/pdf/2611.12982
- **详细分析**: [[20_Research/Papers/大模型/ICLayout-Bench_Benchmarking_LLM_Agents_for_Custom_Circuit_Layout_Design|ICLayout-Bench: Benchmarking LLM Agents for Custom Circuit Layout Design]]
- **作者**: Zhangmai Li, Tianrui Ma, Zheng Weng, Mo Zou, Zidong Du, Yifan Hao, Yongwei Zhao, Wei Li, Jing Li, Qi Guo, Yunji Chen
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ICLayout-Bench: Benchmarking LLM Agents for Custom Circuit Layout Design》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ICLayout-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are being explored for circuit design, but their ability to produce high-quality custom layouts has not been extensively evaluated. ICLayout-Bench is a benchmark in which agents use electronic design automation (EDA) tools to construct and optimize GDSII layouts from transistor-level circuit netlists. These layouts are evaluated using physical verification, parasitic extraction, and post-layout simulation. Layouts that pass the physical and functional checks are scored on electrical performance and area. The benchmark includes 165 tasks across 13 process design kits (PDKs), covering technology nodes from 3 nm to 180 nm. The tasks span analog, mixed-signal, and digital circuits in open-source and commercial EDA flows. The experiments evaluate 22 configurations spanning seven models on 21 public and 19 private tasks. Mean layout scores range from 4.22 to 80.26 on public tasks and from 1.43 to 67.01 on private tasks, on a 100-point scale. Higher reasoning effort does not consistently improve mean scores, and configurations with comparable scores can incur substantially different model costs.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Science_Agents_Making_Embodied_Experimental_Design_Learnable|Embodied Science Agents: Making Embodied Experimental Design Learnable]]

![[assets/2611.12958_figure.png|800]]

- **arXiv**: [2611.12958](https://arxiv.org/abs/2611.12958)
- **PDF**: https://arxiv.org/pdf/2611.12958
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Science_Agents_Making_Embodied_Experimental_Design_Learnable|Embodied Science Agents: Making Embodied Experimental Design Learnable]]
- **作者**: Yihang Che, Zhongwei Yu, Yang Li, Xingyu Lu, Hongxia Yu, Jun Wang
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.6，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Embodied Science Agents: Making Embodied Experimental Design Learnable》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large models have accelerated AI for Science toward agentic science, where AI agents autonomously conduct scientific discovery. Realising this vision requires closing the loop between computational reasoning and physical experimentation, positioning self-driving laboratories (SDLs) as critical enablers. However, existing SDLs exhibit a fundamental paradox: foundation model integration has increased linguistic sophistication while severing physical grounding. By treating models as disembodied planners that output symbolic workflows for separate robotic systems, current architectures inherently block the development of embodied experimental intuition. We argue that overcoming this paradox requires embedding \emph{learnability} along three interdependent axes: cognitive learnability (learning what to investigate), experimental learnability (learning where to search), and embodied learnability (learning how to act). Building on this view, we introduce the Embodied Science Agent (ESA), which unifies digital intelligence with physical embodiment through three synergistic components: a Digital Agent that provides cognitive and experimental learnability via memory-based reasoning and Bayesian optimisation, an Embodied Agent that provides embodied learnability via generalisable instrument control, and an Embodied Unified Interface for seamless coordination. We validated ESA in autonomous wastewater treatment experiments, navigating over 200 million possible conditions. Through 15 continuous rounds, ESA raised the final solution transmittance from 82\% to 99.7\%, corresponding to a 98.5\% reduction in residual dye concentration and near-complete decolourisation, while its learned visuomotor policies generalised across varying instrument placements, a promising step toward next-generation SDLs for autonomous scientific discovery.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_based_control_of_Cancer_Chemotherapy_treatments|Reinforcement Learning based control of Cancer Chemotherapy treatments]]

![[assets/2611.12940_first_page.png|800]]

- **arXiv**: [2611.12940](https://arxiv.org/abs/2611.12940)
- **PDF**: https://arxiv.org/pdf/2611.12940
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_based_control_of_Cancer_Chemotherapy_treatments|Reinforcement Learning based control of Cancer Chemotherapy treatments]]
- **作者**: Jayakody Kankanamalage Chamani Shiranthika
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning based control of Cancer Chemotherapy treatments》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning has achieved tremendous success in recent years. Extending its scope from the traditional complex games such as Atari, Go, Pokeman, and Chess, reinforcement learning has caught researchers' attention on modelling real-life scenarios. Personalized medicine and the dynamic treatment regimen are two such preliminary research fields; researchers are focusing their mindsets currently. Estimating the optimal dynamic treatment regimens from the observational real clinical data is being popularized among the researchers, widening its scope towards more advanced versions of reinforcement learning algorithms. This research is about a research study that focused on reinforcement learning techniques that have been approached in the context of cancer chemotherapy treatments. Primarily this thesis addresses the result of the study by means of the state-of-the-art on reinforcement learning techniques used in generating the optimal policy for sequential treatments, including the existing online reinforcement learning approaches. Thereby a simulation for cancer chemotherapy via traditional Q-learning would be presented. Secondly, the study will extend towards using offline reinforcement learning in the optimal policy generation. Thus, the proposed solution follows a data-driven approach, which works on the real human colon cancer clinical data. The novelty of the proposed solution resides in the implementation of an offline reinforcement learning approach by means of a model-based architecture using the conservative Q-learning and the model-based offline policy optimization algorithm. As per the experimental results and the evaluations, it was revealed that the proposed Chemo RL model caters well the problem of cancer chemotherapy treatment scheduling and serves as a supportive model for the junior oncologists in deciding their treatment decisions.

</details>

---

### [[20_Research/Papers/大模型/EarthRecord_From_Pixels_to_Land_Change_with_Multimodal_Agents_over_Four_Decades_of_Satellite_Imagery|EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery]]

![[assets/2611.12934_figure.png|800]]

- **arXiv**: [2611.12934](https://arxiv.org/abs/2611.12934)
- **PDF**: https://arxiv.org/pdf/2611.12934
- **详细分析**: [[20_Research/Papers/大模型/EarthRecord_From_Pixels_to_Land_Change_with_Multimodal_Agents_over_Four_Decades_of_Satellite_Imagery|EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery]]
- **作者**: Haoran Zhang, Huizhen Sun, Hanbin Wen, Jie Leng, Jiaxin Zhu, Zhaohua Sun
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《EarthRecord: From Pixels to Land Change with Multimodal Agents over Four Decades of Satellite Imagery》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgenticCity-Bench, DVL-Bench, Earth-Bench, GeoMMBench, NaturalBench, OSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While multimodal agents now carry out complex data analysis with tools, their ability to turn decades of satellite imagery into reliable land-change analysis, crucial for Earth observation science, remains unmeasured. Existing benchmarks fall short: they pose questions on curated images or give agents preprocessed inputs, leaving out the raw multi-sensor archives where such analysis begins. We introduce EarthRecord, a benchmark built on the raw record of 56 sites: four decades of Landsat, MODIS, VIIRS, and Sentinel-2 data, with cloud masking and cross-sensor harmonization left to the agent. It poses 238 land-change questions across ten analysis tasks, scored against withheld references from global products, agreement among methods, and visual interpretation. Two controls test what answers rest on: the closed book removes the record, and instrument pairs alter one satellite's data while nothing changes on the ground. Evaluations of twelve multimodal agents reveal that leading agents complete most analyses end to end but falter when an answer requires mapping from imagery. Further analysis shows that the record moves answers from prior knowledge to the pixels but not yet to the real change on the ground: when one satellite's data are altered, half of the right answers follow the alteration. EarthRecord thus provides a principled platform for measuring and advancing agents from pixels to land change.

</details>

---
