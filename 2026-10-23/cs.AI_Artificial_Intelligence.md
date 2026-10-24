# cs.AI | Artificial Intelligence | 2026-10-23

#arxiv #ComputerScience

**论文数**: 28

### [[20_Research/Papers/强化学习/METTA_Memory-Enhanced_Test-Time_Adaptation_for_Meta-Reinforcement_Learning|METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning]]

![[assets/2610.31656_figure.png|800]]

- **arXiv**: [2610.31656](https://arxiv.org/abs/2610.31656)
- **PDF**: https://arxiv.org/pdf/2610.31656
- **详细分析**: [[20_Research/Papers/强化学习/METTA_Memory-Enhanced_Test-Time_Adaptation_for_Meta-Reinforcement_Learning|METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning]]
- **作者**: Ali Najar, Hosein Hasani, Amir Kooshan Fattah, Yasamin Rajabi, Mahdieh Soleymani Baghshah
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《METTA: Memory-Enhanced Test-Time Adaptation for Meta-Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-RL, Meta-World, TrMRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Meta-reinforcement learning aims to train agents that adapt quickly to unseen tasks from limited interaction, but this requires representing task evidence over long interaction histories. Classical recurrent agents compress experience into hidden states, while transformer-based agents retrieve from past trajectories at quadratic memory and computation cost. In this work, we propose Memory-Enhanced Test-Time Adaptation (METTA) for meta-reinforcement learning. It decomposes the fast adaptation phase into two temporal scales: a causal neural memory performs fine-grained within-episode adaptation with linear sequence complexity, while compact episode-level summaries support long-range cross-episode task inference without attending over the full interaction history. Moreover, equipping agents with neural memory provides sufficient expressive capacity and test-time training capability, enabling effective adaptation to unseen held-out tasks and task families at meta-test time. On unseen held-out Meta-World ML10/45 test environments, METTA achieves a success rate over $50\%$ while maintaining a low training budget and short wall-clock time. On long-context sparse-reward PointMaze tasks, it outperforms transformer-based baselines by exhibiting more structured exploration behavior. These results show that METTA provides an efficient path toward more adaptive and scalable long-context meta-RL.

</details>

---

### [[20_Research/Papers/大模型/EpiSEM-Bench_Evaluating_Safety_and_Evidence_Recovery_in_LLM_Agents_under_Missing_Evidence|EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence]]

![[assets/2610.31650_figure.png|800]]

- **arXiv**: [2610.31650](https://arxiv.org/abs/2610.31650)
- **PDF**: https://arxiv.org/pdf/2610.31650
- **详细分析**: [[20_Research/Papers/大模型/EpiSEM-Bench_Evaluating_Safety_and_Evidence_Recovery_in_LLM_Agents_under_Missing_Evidence|EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence]]
- **作者**: Qijin Zhang, Hanzhen Wang, Yuehan Zhao, Haoyu Dai, Yao Shu, Zhongxiang Dai, Shuang Qiu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《EpiSEM-Bench: Evaluating Safety and Evidence Recovery in LLM Agents under Missing Evidence》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AbsenceBench, AgentNoiseBench, EpiSEM-Bench, IHEval, MCP-SafetyBench, ReliabilityBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tool-using language model agents rely on environmental facts to decide whether an action is permitted. When a tool response omits a safety-relevant fact, an agent may carry out a prohibited action even though the user request is benign and every returned statement is true. We introduce \bench{}, an executable benchmark for evaluating unsafe execution, safety boundaries, and evidence recovery in LLM agents under missing evidence. It contains 300 matched unsafe/safe task pairs across six domains. By systematically suppressing critical facts, the benchmark measures unsafe execution under critical evidence omission and determines the minimum observed failure cardinality, including failures with full evidence and cases with no observed failure after exhaustive testing. An independent audit tool tests whether agents seek missing facts and then withhold prohibited actions while completing permissible tasks. The benchmark reveals substantial variation across the ten models in omission robustness, evidence acquisition, and appropriate action. Resistance to missing evidence does not necessarily translate into useful recovery. Recovery access reduces unsafe execution for all ten models, but agents differ in whether they actively obtain the missing facts and use them to act appropriately in both worlds.

</details>

---

### [[20_Research/Papers/具身智能/FocusVLA_Future-Intent_Guided_Dynamic_View_Routing_for_Vision-Language-Action_Models|FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models]]

![[assets/2610.31423_figure.png|800]]

- **arXiv**: [2610.31423](https://arxiv.org/abs/2610.31423)
- **PDF**: https://arxiv.org/pdf/2610.31423
- **详细分析**: [[20_Research/Papers/具身智能/FocusVLA_Future-Intent_Guided_Dynamic_View_Routing_for_Vision-Language-Action_Models|FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models]]
- **作者**: Huixin Xu, Ziya Yu, Peng Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《FocusVLA: Future-Intent Guided Dynamic View Routing for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FocusVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have become an important paradigm for robotic manipulation by unifying visual perception, language understanding, and action generation. Since reliable manipulation requires sufficient observation of objects, end-effectors, and their spatial relationships, multi-view inputs are widely used to provide complementary spatial information. However, our experiments show that existing VLA models do not fully exploit such multi-view complementarity. The policy tends to persistently rely on the wrist view, lacking the ability to dynamically adjust global-local view dependency across manipulation stages, which limits stage adaptability and robustness. To address this issue, we propose FocusVLA, a stage-aware multi-view routing framework. FocusVLA predicts future interaction intent from historical actions and uses it to guide dynamic view routing during action generation. By adaptively coordinating global and local observations across different task stages, FocusVLA improves multi-view utilization. On RoboTwin 2.0, FocusVLA improves the average success rate over the strongest baseline $π_{0.5}$ by 10.10 pp. In real-world evaluation, FocusVLA improves the success rate from 71.7\% to 85.0\%, achieving a 13.3\% gain over $π_{0.5}$. Moreover, the intent prediction and dynamic routing modules of FocusVLA can be integrated into existing VLA frameworks without modifying their core architectures.

</details>

---

### [[20_Research/Papers/大模型/AgentPhishing_A_Benchmark_of_LLM_Email_Agents_Under_Adaptive_Attack|AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack]]

![[assets/2610.31404_figure.png|800]]

- **arXiv**: [2610.31404](https://arxiv.org/abs/2610.31404)
- **PDF**: https://arxiv.org/pdf/2610.31404
- **详细分析**: [[20_Research/Papers/大模型/AgentPhishing_A_Benchmark_of_LLM_Email_Agents_Under_Adaptive_Attack|AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack]]
- **作者**: Justin Tan, Miao Li, Ding Zhao
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《AgentPhishing: A Benchmark of LLM Email Agents Under Adaptive Attack》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PhishSim, SE-VSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-use agents increasingly handle private information and act on users' behalf across desktop and web applications, including email. Phishing therefore poses privacy and security risks that depend not only on whether agents recognize malicious messages, but also on how they respond. Existing phishing datasets were developed primarily for conventional detection, leaving agent susceptibility to persuasive malicious requests insufficiently characterized. To expose vulnerabilities that pre-existing datasets may miss, we introduce AgentPhishing, a benchmark for evaluating whether persuasive phishing attacks can evade detection and induce LLM email agents to comply with malicious requests. We develop PhishOpt, which optimizes reusable email-generation skills against individual agents under fixed benchmark constraints and a realism constraint. We analyze the generated emails using Cialdini's persuasion principles to identify strategies associated with agent failures and use these findings to construct a universal generation skill. Our evaluation shows that agents can handle pre-existing phishing emails safely yet remain susceptible to attacks adapted to agent behavior, while in an AgentPhishing evaluation of nine agents, four exhibit phishing-detection rates below $10\%$ and malicious-request compliance rates above $45\%$. These results highlight the limits of inferring agent safety from conventional phishing evaluations and the need to assess how agents respond to persuasive malicious requests.

</details>

---

### [[20_Research/Papers/大模型/Automating_Feature_Flag_Cleanup_at_Scale_with_Multi-Agent_LLM_Systems_An_Industrial_Experience_at_DoorDash|Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash]]

![[assets/2610.31351_figure.png|800]]

- **arXiv**: [2610.31351](https://arxiv.org/abs/2610.31351)
- **PDF**: https://arxiv.org/pdf/2610.31351
- **详细分析**: [[20_Research/Papers/大模型/Automating_Feature_Flag_Cleanup_at_Scale_with_Multi-Agent_LLM_Systems_An_Industrial_Experience_at_DoorDash|Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash]]
- **作者**: Atharv Chandratre, Jai Datar
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Automating Feature Flag Cleanup at Scale with Multi-Agent LLM Systems: An Industrial Experience at DoorDash》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Feature flags are runtime configuration mechanisms used for gradual feature rollouts, experimentation, and kill switches. Once a feature is fully rolled out, the flag and its gated code become technical debt and can introduce operational risk through inadvertently enabling dormant code paths. At DoorDash, over 56,000 feature flags span 623 repositories, with 1,659 currently stale as of May 2026, with internal estimates of one to two hours per manual cleanup. Existing rule-based cleanup tools proved insufficient in DoorDash's codebases. Our contribution is an end-to-end automated LLM-based feature flag cleanup system that integrates querying live feature flag rollout data using MCP, Jira ticket processing, and end-to-end pull request creation. Our system successfully produced engineer-approved flag removal PRs for 45 (90%) of the 50 stale flags it was evaluated on, proving the system's operational viability at scale with each cleanup averaging only $4.79 and 13.8 minutes. We evaluated the system's quality and reliability boundary based on success rates, cost per cleanup and time metrics. Furthermore, we discuss our lessons learned when architecting this system, to provide practical guidance for developing similar multi-agent systems.

</details>

---

### [[20_Research/Papers/大模型/AgenticEvolve_Evolutionary_Program_Search_with_Persistent_Language_Model_Agents_that_Design_and_Run_Experiments|AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments]]

![[assets/2610.31326_first_page.png|800]]

- **arXiv**: [2610.31326](https://arxiv.org/abs/2610.31326)
- **PDF**: https://arxiv.org/pdf/2610.31326
- **详细分析**: [[20_Research/Papers/大模型/AgenticEvolve_Evolutionary_Program_Search_with_Persistent_Language_Model_Agents_that_Design_and_Run_Experiments|AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments]]
- **作者**: Ze-Yu Peng, Qing-Yu Lan, Zhan-He Wang, Jun Zhang, Yun-Song Piao
- **cs 子类**: cs.AI, cs.LG, cs.NE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgenticEvolve: Evolutionary Program Search with Persistent Language Model Agents that Design and Run Experiments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LLM-SRBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evolutionary program search with large language models keeps the structure of an evolutionary algorithm and uses the model as its variation operator. Typically, the model generates each candidate program in a single request from parent programs and their scores. We present AgenticEvolve, an evolutionary program search framework in which each island is run by a persistent large language model agent. Between evaluations, the agent designs and runs experiments on the candidate program. To measure the contribution of experimentation, we compare AgenticEvolve with No-analysis, an otherwise identical configuration with experiments disabled. On two heuristic design tasks with three large language models, AgenticEvolve produces better programs than No-analysis and OpenEvolve on both hidden and unseen instances. It reaches the baselines' final quality with far fewer evaluations and comparable cost. On twelve equation discovery problems, it recovers the ground-truth structure of more equations than No-analysis and existing language-model and genetic programming baselines.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Accuracy_Disentangling_Decomposition_from_Typed-State_Quality_Assurance_in_Multi-Agent_LLM_Pipelines|Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines]]

![[assets/2610.31280_first_page.png|800]]

- **arXiv**: [2610.31280](https://arxiv.org/abs/2610.31280)
- **PDF**: https://arxiv.org/pdf/2610.31280
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Accuracy_Disentangling_Decomposition_from_Typed-State_Quality_Assurance_in_Multi-Agent_LLM_Pipelines|Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines]]
- **作者**: Maria Gabriela Alves Zuppardo, Vinicius Cardoso Garcia
- **cs 子类**: cs.AI, cs.LG, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Beyond Accuracy: Disentangling Decomposition from Typed-State Quality Assurance in Multi-Agent LLM Pipelines》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent LLM pipelines are often credited with gains in software engineering tasks, but it is rarely clear whether a gain stems from the typed contract between agents or from the specialized prompts that decomposition enables. We study this attribution problem in Requirements Engineering, comparing three architectures for classifying requirements as functional or non-functional and then prioritizing them with MoSCoW: a single-call baseline; a two-call variant that reuses the pipeline's specialized prompts but passes an unvalidated intermediate; and a pipeline with a Pydantic-validated typed state. The 18 conditions cover PROMISE NFR+ (625 requirements), three locally hosted small language models, and two languages. The F1 gain over the baseline is associated with the two-call, specialized-prompt variant (up to +0.075), whereas the typed state adds a small difference (-0.003 to +0.013) that is significant in one of six comparisons. Beyond accuracy, the typed pipeline contains out-of-range model outputs at the agent boundary, while the unvalidated variant fails later and drops the requirement, and it shows a small, reproducible increase in inter-model MoSCoW consistency whose cause our design cannot isolate. The study is associative: the contrasts bundle prompts, call count, and staged context, and the results come from three 7--8B models on one dataset. The implementation and replication package are archived on Zenodo (https://doi.org/10.5281/zenodo.23380444).

</details>

---

### [[20_Research/Papers/大模型/Prompting_Strategy_Effects_Depend_on_the_Judge_A_Multilingual_Study_of_LLM-as-a-Judge_Robustness|Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2610.31172](https://arxiv.org/abs/2610.31172)
- **PDF**: https://arxiv.org/pdf/2610.31172
- **详细分析**: [[20_Research/Papers/大模型/Prompting_Strategy_Effects_Depend_on_the_Judge_A_Multilingual_Study_of_LLM-as-a-Judge_Robustness|Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness]]
- **作者**: Asal Mehrabi, Mohammad Aliannejadi, Clemencia Siro
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM

#### 研究背景与动机

《Prompting Strategy Effects Depend on the Judge: A Multilingual Study of LLM-as-a-Judge Robustness》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AfriQA, AfroBench, CatalanQA, MM-Eval, PersianQA, SummEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-as-a-Judge evaluation is increasingly applied to multilingual tasks, yet prompting strategies such as Chain-of-Thought and Role Conditioning are recommended based solely on English benchmarks. Whether their effectiveness transfers across judge models and languages remains unknown: prompt-sensitivity studies are largely English-centric, while existing multilingual judge studies fix the prompt template. In this work, we address this gap by measuring this interaction through a benchmark of 9 prompting strategies, 4 open-weight judges, 27 languages, and 4 tasks across 13 datasets, yielding over 1M pointwise scores on gold-reference outputs, validated against human judgments. We find that prompting strategies are not transferable: the choice of the judge model dominates the choice of prompting strategy, strategy effects reverse direction across judges, and stability degrades in low-resource languages, where these effects are concealed by aggregate reporting. These findings show that prompting effects in multilingual evaluation are conditioned on the judge, task, and language. Consequently, prompting strategies should be validated for the intended evaluation setting, and cross-study comparisons should account for both judge and prompt configuration.

</details>

---

### [[20_Research/Papers/大模型/Dual_Exam_Controlled_Evaluation_of_Multimodal_Agents_and_World_Models|Dual Exam: Controlled Evaluation of Multimodal Agents and World Models]]

![[assets/2610.31066_figure.png|800]]

- **arXiv**: [2610.31066](https://arxiv.org/abs/2610.31066)
- **PDF**: https://arxiv.org/pdf/2610.31066
- **详细分析**: [[20_Research/Papers/大模型/Dual_Exam_Controlled_Evaluation_of_Multimodal_Agents_and_World_Models|Dual Exam: Controlled Evaluation of Multimodal Agents and World Models]]
- **作者**: Zhefan Rao, Meng Chu, Xuan Zhang, Jingfan Chen, Guohao Cai, Runyi Li, Shiyi Du, Ning Lu, Xu Huang, Zhixuan Chen, Feng Nie, Harold Haodong Chen...
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.9（加权：大模型 0.9，世界模型 1）
- **关联关键词**: Multimodal, Agent, WorldModel

#### 研究背景与动机

《Dual Exam: Controlled Evaluation of Multimodal Agents and World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Models (WMs) can support Multimodal Agents (MAs) through simulated experience, while Agent trajectories can inform World Model refinement. Evaluating this interaction requires separate evidence about action selection and state evolution. We introduce Dual Exam, which tests Agents under fixed environment response mechanisms and World Models under fixed action interventions across physical, digital, social, and scientific domains. The Agent track compares 10 configurations on 1,088 items in 15 reporting categories. The World Model track contains 400 cases across eight scenarios; 15 configurations have full coverage and one covers six scenarios. GPT 6 Astra leads the case-weighted Agent Index at 31.3, and GPT-Image-2 leads the full-coverage WM Overall at 21.7. These scores use different tasks and metrics and are not directly comparable. A 150-case pilot of one coupled pairing records zero task successes and motivates component-level diagnosis. Results reveal uneven task performance and failures to preserve task-relevant state. Their value for predicting coupled success or sustained reciprocal learning remains to be established.

</details>

---

### [[20_Research/Papers/大模型/Multi-Tool_Selection_for_Robotic_Systems_Comparing_Semantic_Retrieval_and_LLM|Multi-Tool Selection for Robotic Systems: Comparing Semantic Retrieval and LLM]]

![[assets/2610.31013_figure.png|800]]

- **arXiv**: [2610.31013](https://arxiv.org/abs/2610.31013)
- **PDF**: https://arxiv.org/pdf/2610.31013
- **详细分析**: [[20_Research/Papers/大模型/Multi-Tool_Selection_for_Robotic_Systems_Comparing_Semantic_Retrieval_and_LLM|Multi-Tool Selection for Robotic Systems: Comparing Semantic Retrieval and LLM]]
- **作者**: Miguel Sousa, Luis Ramos Pinto, João P. Matos-Carvalho
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.4，机器人 1.5）
- **关联关键词**: LLM, Robotics, Security

#### 研究背景与动机

《Multi-Tool Selection for Robotic Systems: Comparing Semantic Retrieval and LLM》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural-language interfaces allow users to command robotic systems without interacting directly with mission planners or robotics middleware. Their reliable use depends on robot tool routing, defined here as the selection of the smallest complete subset of predefined executable capabilities required to satisfy a request. This task is particularly difficult for compound instructions, where incomplete selection may omit necessary sensing or monitoring capabilities, while excessive selection may expose irrelevant tools. We compare four routing strategies: three progressively refined ChromaDB-based methods - fixed-threshold retrieval, relative-distance retrieval, and clause-aware aggregated retrieval - and a cloud-hosted 120-billion-parameter language-model baseline. The methods are evaluated on 164 manually annotated prompts organised into three complexity levels, from direct single-tool requests to compound requests requiring at least three tools. Using exact-match accuracy, completeness, precision, a completeness-weighted composite score, and routing latency, CDB-v3 achieves the best macro-average score among the retrieval-only methods, with 0.7822, compared with 0.8869 for the large-model baseline. Although the LLM provides higher routing quality, CDB-v3 exhibits substantially lower latency and can be deployed locally without requiring cloud connectivity. These results identify a quality-latency trade-off between direct large-model selection and clause-aware semantic retrieval for privacy-sensitive, connectivity-constrained, and resource-constrained robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Measuring_the_Reasoning-Action_Coupling_in_Driving_Vision-Language-Action_Models_through_Counterfactuals|Measuring the Reasoning-Action Coupling in Driving Vision-Language-Action Models through Counterfactuals]]

![[assets/2610.30953_figure.png|800]]

- **arXiv**: [2610.30953](https://arxiv.org/abs/2610.30953)
- **PDF**: https://arxiv.org/pdf/2610.30953
- **详细分析**: [[20_Research/Papers/具身智能/Measuring_the_Reasoning-Action_Coupling_in_Driving_Vision-Language-Action_Models_through_Counterfactuals|Measuring the Reasoning-Action Coupling in Driving Vision-Language-Action Models through Counterfactuals]]
- **作者**: Gabriel Manalu, Saad Wazir, Thao Do, Seongah Kim, Hyeontaek Hwang, Tolcha Yalew Kidane, Daeyoung Kim
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, Systems

#### 研究背景与动机

《Measuring the Reasoning-Action Coupling in Driving Vision-Language-Action Models through Counterfactuals》归入 具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Driving vision-language-action (VLA) models bring an appealing form of explainability to a safety-critical domain, since a system that can state the reasons for its maneuvers offers the transparency that deployment and public trust in autonomous driving demand. These models read the world into language before they act on it, describing the scene and reasoning over it in text that ranges from chain-of-thought to multi-stage question answering on the way to a trajectory. That framing quietly assumes two separable properties, namely that the trajectory follows the generated reasoning and that the generated reasoning tracks the causes that actually produce the trajectory. To thoroughly investigate these properties, we apply causal, counterfactual interventions to four driving VLAs across different benchmarks. First, we perturb the models' own reasoning and show that altering its meaning produces small trajectory changes relative to blanking the same models' camera inputs, a pattern that persists across benchmarks and model architectures. We then construct scene-level counterfactuals through photorealistic removal of key objects named in the models' reasoning and analyze whether the generated reasoning and trajectories track these changes. Overall, our findings indicate that the reasoning these models present to account for their resulting driving behavior is weakly coupled to that behavior itself, pointing to limits on the explainability these systems are intended to provide.

</details>

---

### [[20_Research/Papers/强化学习/MOER_Mix-Policy_Optimization_under_Expert_Prefix_Guidance_with_Selective_Rollback|MOER: Mix-Policy Optimization under Expert Prefix Guidance with Selective Rollback]]

![[assets/2610.30873_first_page.png|800]]

- **arXiv**: [2610.30873](https://arxiv.org/abs/2610.30873)
- **PDF**: https://arxiv.org/pdf/2610.30873
- **详细分析**: [[20_Research/Papers/强化学习/MOER_Mix-Policy_Optimization_under_Expert_Prefix_Guidance_with_Selective_Rollback|MOER: Mix-Policy Optimization under Expert Prefix Guidance with Selective Rollback]]
- **作者**: Xuyang Zhong, Jiuding Yang, Yiwen Guo, Chen Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《MOER: Mix-Policy Optimization under Expert Prefix Guidance with Selective Rollback》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SFT-RL, SFT-then-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mix-policy optimization incorporates off-policy expert data into the reinforcement learning (RL) loop to transcend the capability boundary of on-policy RL. However, existing methods either provide static full-trace guidance that suppresses self-exploration, or adopt expert prefix guidance without correctness guarantees, leading to suboptimal performance or even training collapse. In this paper, we propose MOER, a mix-policy optimization framework that harmonizes expert guidance with self-exploration. MOER injects a decaying expert chain-of-thought prefix into the prompt and lets the model complete the remaining reasoning, with the prefix length progressively annealed to encourage self-exploration. A selective rollback mechanism replaces failed completions with the original full expert trace, guaranteeing the correctness of every off-policy trajectory. Furthermore, a harmonized mix-policy objective optimizes on-policy tokens with a GRPO loss while supervising both expert prefix and completion tokens with a trust-region SFT loss, substantially stabilizing training. Extensive experiments show that MOER achieves the highest average scores in mathematical and general domain reasoning tasks, outperforming all basic and mix-policy baselines, and generalizes consistently across diverse tasks, model scales, and base model categories. Codes are available at https://github.com/CityU-MLO/MOER.

</details>

---

### [[20_Research/Papers/强化学习/An_Introduction_to_World_Models_for_Generalist_Agents|An Introduction to World Models for Generalist Agents]]

![[assets/2610.30789_first_page.png|800]]

- **arXiv**: [2610.30789](https://arxiv.org/abs/2610.30789)
- **PDF**: https://arxiv.org/pdf/2610.30789
- **详细分析**: [[20_Research/Papers/强化学习/An_Introduction_to_World_Models_for_Generalist_Agents|An Introduction to World Models for Generalist Agents]]
- **作者**: Zhihui Zhu
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型, 强化学习
- **相关性评分**: 1.8（加权：大模型 0.4，强化学习 0.4，世界模型 1）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《An Introduction to World Models for Generalist Agents》归入 世界模型、大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models have recently emerged as a promising direction toward developing generalist agents capable of understanding, predicting, and interacting with diverse environments. However, despite growing interest, the concept of a world model remains loosely defined, encompassing approaches ranging from predictive dynamics models and learned simulators to models that jointly generate future observations and actions. This introductory paper aims to clarify the concept of world models and provide a unified perspective on their role in developing generalist agents. Starting from the partially observable Markov decision process (POMDP) framework, we connect world modeling to classical control, dynamical systems, signal processing, and reinforcement learning. We introduce different approaches to world modeling, emphasizing the knowledge they capture, their learning objectives, and how they support decision-making. We further explore the relationship between world modeling and policy learning, highlighting how these capabilities can be unified through conditional prediction without requiring separate models. Rather than offering an exhaustive survey of existing methods, this paper focuses on fundamental concepts, modeling principles, and connections, with the goal of providing an accessible and unified introduction to world models for generalist agents.

</details>

---

### [[20_Research/Papers/大模型/LLM_Multi-Agent_Systems_Are_Vulnerable_to_Herding_and_Runaway_Cascades|LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades]]

![[assets/2610.30769_figure.png|800]]

- **arXiv**: [2610.30769](https://arxiv.org/abs/2610.30769)
- **PDF**: https://arxiv.org/pdf/2610.30769
- **详细分析**: [[20_Research/Papers/大模型/LLM_Multi-Agent_Systems_Are_Vulnerable_to_Herding_and_Runaway_Cascades|LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades]]
- **作者**: Farnoosh Hashemi, Shiyu Ji, Joice Chen, Michael W. Macy
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM Multi-Agent Systems Are Vulnerable to Herding and Runaway Cascades》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) increasingly operate in multi-agent systems where they collaborate by responding to others' choices, creating endogenous feedback loops with vulnerability to social influence, herding behavior and runaway cascades. Following the design of the classic Music Lab experiment, we tested this vulnerability in large populations of LLM agents that recommended unfamiliar songs, with or without exposure to cumulative recommendation counts. Exposure led to runaway cascades that generated extreme and unpredictable collective recommendations increasingly divergent from a song's intrinsic appeal. Compared to humans, LLM populations were generally far more susceptible to herding behavior, and unlike humans, LLM cascades were less able to self-correct. This vulnerability has implications for multi-agent collaboration in recommender systems, automated evaluation, complex problem-solving, and unauthorized conspiracies.

</details>

---

### [[20_Research/Papers/大模型/Governance-State_Corruption_in_Long-Term_Memory_for_LLM_Agents_A_Cross-Model_Stress_Test|Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test]]

![[assets/2610.30698_first_page.png|800]]

- **arXiv**: [2610.30698](https://arxiv.org/abs/2610.30698)
- **PDF**: https://arxiv.org/pdf/2610.30698
- **详细分析**: [[20_Research/Papers/大模型/Governance-State_Corruption_in_Long-Term_Memory_for_LLM_Agents_A_Cross-Model_Stress_Test|Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test]]
- **作者**: Bowen Liu, Youting Wang, Bonan Shen, Dingyan Shang
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Governance-State Corruption in Long-Term Memory for LLM Agents: A Cross-Model Stress Test》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An LLM agent can retrieve a memory correctly yet use it incorrectly after its validity state changes. We study governance-state corruption: faults that alter which retained records enter model-visible context while stored content and tasks remain fixed. Across six providers, 731 benchmark-grounded bases yield 2,080 matched fault pairs. In offline control-plane checks, corruption changes the operative projection in 96.25% of pairs, while oracle-backed enforcement restores it in 100%. For downstream evaluation, a deterministically selected, non-probability LongMemEval/Memora panel resolves 298 of 300 matched triplets (238 distinct bases). Clean-minus-corrupted contrasts are 40.54 percentage points in LongMemEval binary correctness (95% base-cluster interval [30.32, 50.71]) and 30.60 points in rescaled Memora FAMA ([23.31, 37.69]); both sources also show recovery. OAKS Novel native option parity holds for all 6,714 resolved outputs. Full-cohort frozen-scorer corruption/recovery effects (-27.55/+27.51 points) remain descriptive proxies, not validated native semantic population effects. These bounded findings motivate evaluating memory control-state integrity alongside retrieval accuracy.

</details>

---

### [[20_Research/Papers/强化学习/Anticipating_Social_Consequences_with_Distributional_World_Models|Anticipating Social Consequences with Distributional World Models]]

![[assets/2610.30657_figure.png|800]]

- **arXiv**: [2610.30657](https://arxiv.org/abs/2610.30657)
- **PDF**: https://arxiv.org/pdf/2610.30657
- **详细分析**: [[20_Research/Papers/强化学习/Anticipating_Social_Consequences_with_Distributional_World_Models|Anticipating Social Consequences with Distributional World Models]]
- **作者**: Viet-Thanh Pham, Thuy-Trang Vu, Zhuang Li, Lizhen Qu, Gholamreza Haffari
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《Anticipating Social Consequences with Distributional World Models》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social world models predict how interactions develop after an action, helping agents negotiate, cooperate and mediate. In these situations, one action can lead to several plausible futures, hence predicting only one future can overlook consequential alternatives, while exploring them through repeated simulations increases inference cost. We propose DSWM, a Distributional Social World Model that predicts alternative responses, their probabilities and immediate and final outcome values in one output per candidate action. We train a 4B model on repeated simulations using supervised fine-tuning and GRPO. At inference time, the actor uses these possible consequences to choose an action. Across three seen and two unseen environments, with interaction backbones absent from training collection, DSWM achieves the best average performance on 13 of 15 metrics. Ablations show that retaining multiple futures and their predicted probabilities improves outcomes in all five environments.

</details>

---

### [[20_Research/Papers/大模型/Governed_Self-Evolution_for_Autonomous_Investing_A_Multi-Agent_LLM_System_with_an_Invariant_Core|Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core]]

![[assets/2610.30557_first_page.png|800]]

- **arXiv**: [2610.30557](https://arxiv.org/abs/2610.30557)
- **PDF**: https://arxiv.org/pdf/2610.30557
- **详细分析**: [[20_Research/Papers/大模型/Governed_Self-Evolution_for_Autonomous_Investing_A_Multi-Agent_LLM_System_with_an_Invariant_Core|Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core]]
- **作者**: Yebo Feng, Jingyang Dai, Liangrui Pan, Nelson Lau, Jiahua Xu, Yang Liu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Governed Self-Evolution for Autonomous Investing: A Multi-Agent LLM System with an Invariant Core》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents that act on live Web data must combine heterogeneous evidence, remember what they have done and improve from outcomes without weakening their own safeguards. We study this problem in autonomous investing, where every action is irreversible and based on untrusted Web content. We present Steward, a multi-agent LLM system that draws the boundary of self-evolution in its type system. First, nine role-specialised agents decide jointly: four analysts read news feeds, SEC filings, macroeconomic series and market data and emit typed reports, from which a Portfolio Manager sets target positions that a protected Risk Manager audits. Second, a seven-layer shared memory, assembled by code from the system's own record, gives each decision its position context, the market narrative, calibration and the agent's past decisions. Third, the system improves itself by review: code grades every trade and forecast nightly and writes the grades into memory, and each quarter a reflector proposes prompt learnings that a deterministic gate applies reversibly and replay of recorded inputs verifies. All three operate around an invariant core of order arithmetic, risk rules and discipline-agent prompts that no self-edit can reach. In a five-month live deployment (102 trading days, 1,632 LLM calls), the system contained a 24.6% sector drawdown to a 0.3% loss; in replay of its recorded inputs, a single model given the same raw data traded more and lost 1.35 points against the market over five days where the joint design showed no significant loss, and no injected instruction was followed; and a 2015-2026 backtest shows the core alone lowering the maximum drawdown under all 50 random entry policies. The reflector traced the dominant failure to its root cause, and the gate applied a learning that the agent adopted on trigger evenings and on no control evening. Code: https://github.com/yebof/quant-agent

</details>

---

### [[20_Research/Papers/机器人/PhysibleMDM_Enforcing_Inference-Time_Physical_Feasibility_Constraints_on_Motion_Diffusion_Models_via_Noise_Optimization|PhysibleMDM: Enforcing Inference-Time Physical Feasibility Constraints on Motion Diffusion Models via Noise Optimization]]

![[assets/2610.30500_figure.png|800]]

- **arXiv**: [2610.30500](https://arxiv.org/abs/2610.30500)
- **PDF**: https://arxiv.org/pdf/2610.30500
- **详细分析**: [[20_Research/Papers/机器人/PhysibleMDM_Enforcing_Inference-Time_Physical_Feasibility_Constraints_on_Motion_Diffusion_Models_via_Noise_Optimization|PhysibleMDM: Enforcing Inference-Time Physical Feasibility Constraints on Motion Diffusion Models via Noise Optimization]]
- **作者**: Maximilian Stölzle, David Müller, Agon Serifi, Ruben Grandia, Espen Knoop, Moritz Bächer
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《PhysibleMDM: Enforcing Inference-Time Physical Feasibility Constraints on Motion Diffusion Models via Noise Optimization》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion Diffusion Models (MDMs) can generate diverse and visually appealing human motion; yet, the resulting trajectories frequently violate physical constraints, limiting their downstream use in simulation and control. We present PhysibleMDM, a framework that promotes physical feasibility of MDM output by optimizing at inference time the diffusion noise without retraining the generative model. We introduce a set of surrogate feasibility constraints that can be evaluated without full trajectory simulation. These constraints combine kinematic checks (e.g., ground penetration, slip, and self-collision) with dynamic feasibility tests computed via an inverse-dynamics inner loop formulated as a cone program. We solve the resulting black-box noise optimization problem using the Separable Covariance Matrix Adaptation Evolution Strategy (Sep-CMA-ES), thereby avoiding reliance on computationally expensive and discontinuous gradients. An autoregressive scheme then chains optimized segments to synthesize long motion sequences. Across 100 motion styles on an SMPL humanoid, PhysibleMDM reduces mean ground penetration, self-collision penetration, and ground slip by 75%, 92%, and 74%, respectively, relative to unoptimized diffusion output. Across 11 sequences for a custom bipedal robot, it achieves median reductions of 89.5% in per-sequence mean acceleration-reconstruction error and 79.5% in the mean inverse-dynamics residual.

</details>

---

### [[20_Research/Papers/强化学习/From_Single-Actor_Environments_to_Multi-Actor_Event_Worlds_Can_LLMs_Be_Event_World_Models|From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?]]

![[assets/2610.30488_first_page.png|800]]

- **arXiv**: [2610.30488](https://arxiv.org/abs/2610.30488)
- **PDF**: https://arxiv.org/pdf/2610.30488
- **详细分析**: [[20_Research/Papers/强化学习/From_Single-Actor_Environments_to_Multi-Actor_Event_Worlds_Can_LLMs_Be_Event_World_Models|From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?]]
- **作者**: Juntong Ni, Zewen Liu, Bohan Wang, Lige Zhang, Wei Jin
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，世界模型 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《From Single-Actor Environments to Multi-Actor Event Worlds: Can LLMs Be Event World Models?》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ALFWorld, EventWorld, StableToolBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models help agents assess the consequences of their actions before acting. Many real systems, however, involve multiple actors who make their own decisions, can evolve even when the agent takes no action, and are only partially observed through event logs. We formalize these systems as event worlds and ask whether large language models can predict future observations from the log and the agent's proposed actions. We build complementary benchmarks from human Diplomacy games and real Polymarket trades. Our hierarchical framework compares prediction with and without other actors' actions, then tests multi-step rollouts, predictions for actions never taken, and usefulness to agents. Fine-tuning and more data improve prediction when all actors' recorded actions are given. With only the agent's action, models struggle when other actors strongly affect the outcome, and larger models and longer histories help little. This gap also limits multi-step prediction and agent decisions, with models overestimating plan success. Yet imagined experience and initialization from world models can still improve policy learning. Anticipating other actors' actions remains a central challenge for event world modeling.

</details>

---

### [[20_Research/Papers/大模型/Why_Bother_Me_Again_Benchmarking_Personal_Agent_Memory_for_Interaction_Preferences|Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences]]

![[assets/2610.30485_figure.png|800]]

- **arXiv**: [2610.30485](https://arxiv.org/abs/2610.30485)
- **PDF**: https://arxiv.org/pdf/2610.30485
- **详细分析**: [[20_Research/Papers/大模型/Why_Bother_Me_Again_Benchmarking_Personal_Agent_Memory_for_Interaction_Preferences|Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences]]
- **作者**: Jialin Li, Zhenhao Chen, Hanjun Luo, Hanan Salam
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Why Bother Me Again? Benchmarking Personal Agent Memory for Interaction Preferences》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AMemGym, MemPABench, PrefEval, VitaBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personal intelligence systems are taking on increasingly complex everyday tasks, yet repeated questions, unnecessary confirmations, and unwanted outreach can turn capable assistance into interaction burden. Reducing this burden requires agents to remember how users want to be assisted. However, existing memory benchmarks focus on factual recall and personalized answers and rarely test how agents learn and act on interaction preferences. We introduce MemPABench, an interactive environment for on-policy evaluation of memory in personal agents. MemPABench poses long-horizon tasks requiring agents to decide when to clarify, confirm, or act autonomously. Four grounded simulated users hold 14 preferences across work and personal contexts. Their feedback spans 99 sessions over four months, with five event-driven changes per user testing memory updates. We evaluate preference selection, delivered behavior, and sensitivity to context and preference change. Evaluating four memory systems across four LLM backbones, we find that current memory brings limited gains in preference selection. Retrieval-based systems (i.e. Mem0, MemOS, simple RAG) do not outperform No Memory, while File-based memory improves accuracy but applies preferences beyond relevant contexts. Our analysis shows that current memory struggles to retrieve interaction preferences and adapt to preference changes. Even with the correct preference available, overriding the agent's default interaction habits remains challenging. The environment and dataset are available at https://mempabench.com.

</details>

---

### [[20_Research/Papers/具身智能/Externalise_the_Memory_A_Pre-Registered_Study_of_Where_an_Embodied_Agent's_Experience_Should_Live|Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live]]

![[assets/2610.30478_first_page.png|800]]

- **arXiv**: [2610.30478](https://arxiv.org/abs/2610.30478)
- **PDF**: https://arxiv.org/pdf/2610.30478
- **详细分析**: [[20_Research/Papers/具身智能/Externalise_the_Memory_A_Pre-Registered_Study_of_Where_an_Embodied_Agent's_Experience_Should_Live|Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live]]
- **作者**: Cheng-Yin Tu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Externalise the Memory: A Pre-Registered Study of Where an Embodied Agent's Experience Should Live》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ExpReS-VLA, MemoryVLA, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Should an embodied agent's experience be baked into its policy weights, or kept external and retrieved at inference? A memory-augmented teacher (a VLM that retrieves lessons, with their episode images, from its own past attempts) produces trajectories on a vision-conditioned reach task; from the same trajectories we distil LoRA student policies and evaluate them under matched protocols, including one that re-attaches the teacher's frozen retrieval buffer to a fixed set of student weights. We pre-registered the hypotheses, arms, tests, and analysis rules before training and before any p-value. Distilling the memory-augmented behaviour into weights beat an action-only control by +1 pp (n.s.); the registered test proves underpowered for its own minimum effect, so we withdraw - rather than refute - the memory-in-weights claim. Attaching retrieval to a fixed set of student weights added +34 pp (z=5.15), reaching the pooled memory-augmented teacher reference (49.3%); the pre-registered protocol contrast agrees (+23 pp, z=3.36); under a pre-registered auto-reset sensitivity count the two are +36 and +29 pp. An exploratory behavioural probe with pre-registered per-arm predictions is consistent with behavioural distillation transferring the marginal correction but not the conditional, situation-specific correction that retrieval supplies. The recipe that follows is to externalise the memory: in follow-up controls registered before they ran, the same frozen buffer lifts the base model with no adapter to 48% (sensitivity 48%) and the other three adapters from 19-26% to 53-55% (sensitivity 17-21% to 50-55%), and the adapter adds nothing detectable once the buffer is attached. On a second, harder task, the retrieval advantage points the same direction but falls short of significance (+6 pp, 95% CI [-4.5, +16.4]); exploratory diagnostics tie the attenuation to memory coverage.

</details>

---

### [[20_Research/Papers/具身智能/SpecMAGIC_Specification-Guided_Multi-Task_Generalization_in_Multi-Agent_Reinforcement_Learning|SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning]]

![[assets/2610.30443_figure.png|800]]

- **arXiv**: [2610.30443](https://arxiv.org/abs/2610.30443)
- **PDF**: https://arxiv.org/pdf/2610.30443
- **详细分析**: [[20_Research/Papers/具身智能/SpecMAGIC_Specification-Guided_Multi-Task_Generalization_in_Multi-Agent_Reinforcement_Learning|SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning]]
- **作者**: Zijian Guo, İlker Işık, H. M. Sabbir Ahmad, Wenchao Li
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《SpecMAGIC: Specification-Guided Multi-Task Generalization in Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ACC-MARL, MARL, MTMARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-task generalization is an important yet underexplored problem in multi-agent reinforcement learning (MARL). Many real-world applications require multi-agent systems to generalize across complex, temporally extended tasks with diverse inter-agent coordination requirements. We introduce a specification language that combines temporal-logic task specifications with operators for expressing such requirements. We propose SpecMAGIC, a hierarchical framework that leverages the automaton structure of task specifications for subtask decomposition. A centralized high-level planner identifies and allocates compatible subtask sequences across agents, while decentralized low-level policies execute individual subtasks. This enables zero-shot generalization to new tasks by composing reusable subtask policies according to new specifications, without retraining. We establish soundness and probabilistic completeness of the high-level planner. Experiments on multi-agent navigation tasks show that SpecMAGIC substantially outperforms existing approaches on unseen task specifications and maintains strong performance as the number of agents increases.

</details>

---

### [[20_Research/Papers/强化学习/Self-Assessment_Reinforcement_Learning_for_Search-State_Awareness_in_Retrieval-Augmented_Large_Language_Models|Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models]]

![[assets/2610.30435_figure.png|800]]

- **arXiv**: [2610.30435](https://arxiv.org/abs/2610.30435)
- **PDF**: https://arxiv.org/pdf/2610.30435
- **详细分析**: [[20_Research/Papers/强化学习/Self-Assessment_Reinforcement_Learning_for_Search-State_Awareness_in_Retrieval-Augmented_Large_Language_Models|Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models]]
- **作者**: Taewhoo Lee, Minju Song, Jungwoo Park, Chanwoong Yoon, Junha Jung, Hyeon Hwang, Sanghoon Lee, Minbyul Jeong, Jaewoo Kang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.45（加权：大模型 0.65，强化学习 0.8）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Self-Assessment Reinforcement Learning for Search-State Awareness in Retrieval-Augmented Large Language Models》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA, SARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in search agents have enabled large language models to tackle complex tasks by retrieving and synthesizing external information. However, existing search agents often lack search-state awareness, i.e., the ability to recognize what information has been obtained and what remains missing, leading to hallucinated reasoning and prematurely terminated search. To address this limitation, we propose Self-Assessment Reinforcement Learning (SARL), a reinforcement learning framework in which models learn to recognize their own search state during training and improve their search behavior accordingly, without requiring additional assessment at test time. SARL achieves this through a dual reward design that captures the corrective effect of each assessment while penalizing excessive reliance on it, jointly encouraging effective and efficient search trajectories. Under this setup, SARL achieves a 24.3% relative improvement over the strongest baseline, with average gains of 35.9% on multi-hop reasoning and 27.9% on deep research benchmarks against the strongest per-benchmark baselines. SARL further surpasses methods built on auxiliary supervision or multi-agent coordination, despite operating as a standalone RL framework with no inference-time scaffolding. Beyond final performance, SARL maintains training stability under extended search horizons, a regime where existing methods consistently degrade, enabling sustained gains as task complexity grows.

</details>

---

### [[20_Research/Papers/大模型/Agent_Mosaic_Recognizing_Confidentiality_Leaks_in_Agentic_LLM_Systems|Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems]]

![[assets/2610.30418_first_page.png|800]]

- **arXiv**: [2610.30418](https://arxiv.org/abs/2610.30418)
- **PDF**: https://arxiv.org/pdf/2610.30418
- **详细分析**: [[20_Research/Papers/大模型/Agent_Mosaic_Recognizing_Confidentiality_Leaks_in_Agentic_LLM_Systems|Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems]]
- **作者**: Daniel Ruiz, Luca Luceri, Emilio Ferrara
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agent Mosaic: Recognizing Confidentiality Leaks in Agentic LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Pro-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern LLM agents can retrieve information from accessible documents, and then disclose a sensitive conclusion assembled from them. This mosaic effect creates a critical risk for agents operating over confidential data. We quantify its realization with 30 synthetic cybersecurity, medical, and military examples, yielding 10,800 final answers from three LLM agents in controlled simulation and 1,440 answers from live agents in two open-source harnesses. Even under benign queries designed to be answerable from one document, GPT-5.6-Sol, the best performing model tested, discloses forbidden composites in 7.08% of answers (95% CI: 3.75-10.67%) in simulation, with worse disclosure rates in live harnesses. Adding visible classification headers and explicit aggregation rules reduces pooled disclosure rates substantially, yet unsafe disclosures persist in 32.37% of simulated answers (95% CI: 28.33-36.19%) across all intents despite these safeguards. Furthermore, increased refusals do not guarantee confidentiality, since significant refusals reveal the prohibited conclusion regardless. These results point to a troubling conclusion: sensitive data leaks via mosaic-style events are an observed confidentiality failure mode in the evaluated settings at non-negligible rates. They motivate stronger controls on what agents may infer and disclose in sensitive data environments with mixed-clearance users.

</details>

---

### [[20_Research/Papers/具身智能/MPBRS_Multi-Potential-Based_Reward_Shaping_for_Unified_Reward_Configuration_in_Humanoid_Locomotion|MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion]]

![[assets/2610.30334_figure.png|800]]

- **arXiv**: [2610.30334](https://arxiv.org/abs/2610.30334)
- **PDF**: https://arxiv.org/pdf/2610.30334
- **详细分析**: [[20_Research/Papers/具身智能/MPBRS_Multi-Potential-Based_Reward_Shaping_for_Unified_Reward_Configuration_in_Humanoid_Locomotion|MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion]]
- **作者**: Van Chung Nguyen, Hung Manh La
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.7，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing and tuning reward functions remains one of the main challenges in building effective reinforcement learning (RL) pipelines for humanoid locomotion. While shaping rewards can accelerate learning, naively formulated terms often conflict with the desired behavior, overfit to a specific robot, or become unstable under small weight changes. Potential-Based Reward Shaping (PBRS) offers an alternative solution: shaping the reward via differences of a potential function to guide exploration without changing the optimal policy. In this paper, we study Multi-PBRS for humanoid locomotion and propose a unified reward configuration. We then evaluate the same reward structure and weights across nine humanoid robots, requiring only robot-specific metadata (joint/link mappings and default poses) rather than per-robot reward redesign. Our experiments show that, compared to standard shaping, MPBRS provides more consistent scaling behavior and reduced tuning sensitivity across robots, making it easier to tune without altering the optimal policy.

</details>

---

### [[20_Research/Papers/大模型/Edit,_Don't_Imitate_Minimal-Edit_On-Policy_Distillation_for_Multimodal_Reasoning|Edit, Don't Imitate: Minimal-Edit On-Policy Distillation for Multimodal Reasoning]]

![[assets/2610.30231_figure.png|800]]

- **arXiv**: [2610.30231](https://arxiv.org/abs/2610.30231)
- **PDF**: https://arxiv.org/pdf/2610.30231
- **详细分析**: [[20_Research/Papers/大模型/Edit,_Don't_Imitate_Minimal-Edit_On-Policy_Distillation_for_Multimodal_Reasoning|Edit, Don't Imitate: Minimal-Edit On-Policy Distillation for Multimodal Reasoning]]
- **作者**: Wen Ye, Ailin Deng, Zirui Wang, Shixing Yu, Han Zhang, Tian Yun, Nikhil Mehta, Tarun Kalluri, Xuefei Cao, Xuezhe Ma, Hengduo Li
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.12（加权：大模型 0.6，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Edit, Don't Imitate: Minimal-Edit On-Policy Distillation for Multimodal Reasoning》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual mathematical reasoning can fail before reasoning begins: when a vision-language model (VLM) misreads a diagram, subsequent reasoning proceeds from false premises. This perceptual bottleneck is especially pronounced in smaller models, while accurate textual descriptions can substantially narrow the gap to larger models. Because obtaining such descriptions at inference requires additional annotation or model calls, we propose minimal-edit corrective on-policy distillation. Using reference figure descriptions and verified reference solutions as training-only information, a teacher scores incorrect student rollouts under a minimal-edit objective, and only teacher-disfavored tokens contribute to the corrective loss. Correct rollouts receive task-reward reinforcement learning. This preserves on-policy supervision while avoiding full-response imitation. Across model scales, the method requires no descriptions at test time and meets or exceeds the corresponding base model supplied with a reference figure description at inference. It also improves perception-oriented performance, particularly low-level geometric perception, and transfers to external mathematics and perception benchmarks. Because the minimal-edit teacher evaluates corrections rather than generating its own solution, the method remains effective with a frozen same-size teacher, although its gains are smaller than with a larger teacher on most metrics.

</details>

---

### [[20_Research/Papers/大模型/Self-Evolving_Static_Analysis_via_LLM_Pseudo-Labeling|Self-Evolving Static Analysis via LLM Pseudo-Labeling]]

![[assets/2610.30184_figure.png|800]]

- **arXiv**: [2610.30184](https://arxiv.org/abs/2610.30184)
- **PDF**: https://arxiv.org/pdf/2610.30184
- **详细分析**: [[20_Research/Papers/大模型/Self-Evolving_Static_Analysis_via_LLM_Pseudo-Labeling|Self-Evolving Static Analysis via LLM Pseudo-Labeling]]
- **作者**: Rui Melo, Andre Duarte, Aditya Oke, Shubham Gandhi, Nachiket Kotalwar, Rui Abreu, Lei Li, Carolyn Rose
- **cs 子类**: cs.AI, cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《Self-Evolving Static Analysis via LLM Pseudo-Labeling》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Security bugs often slip past static analysis not because they are impossible to detect, but because detection rules have not yet been written for the code in front of us. New frameworks, APIs, and coding idioms continually create such gaps, leaving developers to discover failures and manually encode new rules. We present SESAA, a framework in which an Large Language Model (LLM) agent starts from no rules and iteratively evolves a set of readable and auditable joern queries. The agent receives feedback only from a second LLM critic, which inspects flagged and unflagged code to identify likely false alarms and suspected misses, without access to ground-truth labels. The agent then uses this feedback to revise its queries. On the OWASP Benchmark for Python, SESAA reaches a mean F1 of 0.742 across 8 independent runs, well above the default configurations of five widely used tools and comparable to the strongest of them once it is tuned with access to ground-truth labels that SESAA never sees. In a pilot on real-world Python projects, queries induced from code available before a vulnerability was introduced detect 10 of 19 subsequent CVEs, including 9 detected by rules written for the same repository. The resulting detector is a set of executable, human-readable queries that engineers can inspect, modify, and run independently. These results suggest that LLM agents can turn static-analysis rule maintenance from a manually authored process into an iterative process of automated discovery and repair.

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

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：A-Sim, ASSEBench, SafeAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pre-deployment verification of enterprise artificial intelligence (AI) agents remains a critical gap between large language model (LLM) capability benchmarking and production deployment. Post-deployment monitoring, human-in-the-loop controls, and prompt-level guardrails offer limited assurance once an agent is operating in production. We present an ontology-grounded verification framework -- to our knowledge the first to combine three components: an Agent Operational Envelope formalizing the certification space across permissions, domain constraints, safety properties, governance rules, and autonomy levels; an ontology-to-scenario generation pipeline that derives regulatory, operational, and adversarial test scenarios automatically; and a machine-verifiable Trust Certificate with graduated deployment verdicts. A controlled pilot across four regulated industries (Fintech, Banking, Insurance, Healthcare), instantiated as five industry-by-regulatory-regime cells across the United States and Vietnam (where Vietnam's 2025 AI Law makes such verification legally mandated for financial services), generated 1,800 scenarios evaluated against 125 primary-source regulatory requirements and 25 injected faults. Ontology-grounded generation significantly outperformed the dominant persona-based baseline on regulatory coverage (48.3% versus 33.1%; corrected p_c = .0006) and attained the highest domain specificity (4.77/5.0; p = 2e-6); transparently, its advantage over plain and retrieval-augmented prompting did not survive Bonferroni correction. Cross-validation across three LLM families (Claude Sonnet 4, Qwen 2.5 72B, Gemma 4 26B; 5,400 total scenarios) replicated the persona-versus-ontology pattern. The framework offers a reproducible, regulation-grounded route to pre-deployment assurance for enterprise AI agents, complementing runtime governance with an auditable deployment gate.

</details>

---
