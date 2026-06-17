# cs.AI | Artificial Intelligence | 2026-06-15

#arxiv #ComputerScience

**论文数**: 36

### [[20_Research/Papers/大模型/ClinHallu_A_Benchmark_for_Diagnosing_Stage-Wise_Hallucinations_in_Medical_MLLM_Reasoning|ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning]]

![[assets/2606.14697_figure.png|800]]

- **arXiv**: [2606.14697](https://arxiv.org/abs/2606.14697)
- **PDF**: https://arxiv.org/pdf/2606.14697
- **详细分析**: [[20_Research/Papers/大模型/ClinHallu_A_Benchmark_for_Diagnosing_Stage-Wise_Hallucinations_in_Medical_MLLM_Reasoning|ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning]]
- **作者**: Sicheng Yang, Hangjie Yuan, Wenjun Zhang, Jinwang Wang, Yichen Qian, Weihua Chen, Fan Wang, Lei Zhu
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Multimodal

#### 研究背景与动机

《ClinHallu: A Benchmark for Diagnosing Stage-Wise Hallucinations in Medical MLLM Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MedFrameQA, MedHEval, MedHallBench, MedXpertQA, PathVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building trustworthy medical multimodal large language models (MLLMs) is critical for reliable clinical decision support. Existing medical hallucination benchmarks mainly focus on data collection, but often ignore where hallucinations originate within the reasoning process. We find that hallucination sources vary across samples: errors may arise from visual misrecognition, incorrect medical knowledge recall, or flawed reasoning integration. To enable source-level hallucination diagnosis, we introduce ClinHallu, a benchmark for stage-wise hallucination diagnosis in medical MLLM reasoning. ClinHallu contains 7,031 validated instances, where each instance is augmented with a structured reasoning trace decomposed into Visual Recognition, Knowledge Recall, and Reasoning Integration. We also use stage-replacement interventions to measure how correcting specific stages affects the final answer. Beyond evaluation, we show that trace-supervised fine-tuning reduces stage-wise hallucinations. ClinHallu provides a fine-grained hallucination testbed for diagnosing and mitigating reasoning failures in medical MLLMs. The benchmark is publicly available at https://github.com/alibaba-damo-academy/ClinHallu.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Coordinated_Preference_for_Multi-Objective_Multi-Agent_Reinforcement_Learning|Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning]]

![[assets/2606.14693_figure.png|800]]

- **arXiv**: [2606.14693](https://arxiv.org/abs/2606.14693)
- **PDF**: https://arxiv.org/pdf/2606.14693
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Coordinated_Preference_for_Multi-Objective_Multi-Agent_Reinforcement_Learning|Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning]]
- **作者**: Pengxin Wang, Lihao Guo, Yi Xie, Bo Liu, Siyang Cao, Jingdi Chen
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Learning Coordinated Preference for Multi-Objective Multi-Agent Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL, MOMARL, OpenCDA-MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative multi-objective multi-agent reinforcement learning (MOMARL) models team decision making under multiple, potentially conflicting objectives. In this setting, conflicts arise not only across objectives but also across agents with different observations, roles, and contributions. We propose Preference Coordinated Multi-agent Policy Optimization (PCMA), which learns coordinated agent-specific preferences to enable complementary trade-offs among agents. Theoretically, we formulate cooperative MOMARL as a team-optimal game and show that, under suitable conditions, preference diversity can induce team improvement through a first-order improvement decomposition. Experiments on multiple cooperative MOMA environments and a practical traffic-control scenario show that PCMA improves both performance and trade-off coordination.

</details>

---

### [[20_Research/Papers/大模型/Towards_Direct_Latent-Space_Synthesis_for_Parallel_Branches_in_LLM-Agent_Workflows|Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows]]

![[assets/2606.14672_figure.png|800]]

- **arXiv**: [2606.14672](https://arxiv.org/abs/2606.14672)
- **PDF**: https://arxiv.org/pdf/2606.14672
- **详细分析**: [[20_Research/Papers/大模型/Towards_Direct_Latent-Space_Synthesis_for_Parallel_Branches_in_LLM-Agent_Workflows|Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows]]
- **作者**: Shikun Liu, Mufei Li, Dongqi Fu, Haoyu Wang, Yinglong Xia, Hong Li, Hong Yan, Pan Li
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Towards Direct Latent-Space Synthesis for Parallel Branches in LLM-Agent Workflows》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models increasingly serve as execution engines for agentic systems, yet they still consume context through a sequential text interface. This creates a mismatch with modern structured agent workflows, in which independent branches explore subtasks, retrieve evidence, or generate candidate solutions before a final synthesis step. Existing systems typically merge these branches by concatenating their textual outputs, which discards the parallel structure and incurs redundant prefill computation. In this work, we introduce Parallel-Synthesis, a plug-and-play framework that enables a synthesizer to directly consume the KV caches produced by parallel worker agents. Parallel-Synthesis combines a cache mapper that calibrates independently generated branch caches with a fine-tuned synthesizer adapter that enables generation from this non-sequential cache interface. We train Parallel-Synthesis using data that exposes the synthesizer to parallel cache contexts, teaches aggregation across cached branches, and distills reasoning behavior from standard text-concatenation-based synthesis. Across nine downstream datasets spanning math, science QA, code generation, GAIA, and multi-agent database diagnosis, Parallel-Synthesis matches or outperforms text-based synthesis on seven datasets and remains close on the other two. It also reduces time-to-first-token by 2.5x-11x, suggesting that direct cache-based synthesis is a promising interface for more native and efficient synthesis over parallel agent branches.

</details>

---

### [[20_Research/Papers/大模型/When_Errors_Become_Narratives_A_Longitudinal_Taxonomy_of_Silent_Failures_in_a_Production_LLM_Agent_Runtime|When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime]]

![[assets/2606.14589_first_page.png|800]]

- **arXiv**: [2606.14589](https://arxiv.org/abs/2606.14589)
- **PDF**: https://arxiv.org/pdf/2606.14589
- **详细分析**: [[20_Research/Papers/大模型/When_Errors_Become_Narratives_A_Longitudinal_Taxonomy_of_Silent_Failures_in_a_Production_LLM_Agent_Runtime|When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime]]
- **作者**: Wei Wu
- **cs 子类**: cs.AI, cs.DC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《When Errors Become Narratives: A Longitudinal Taxonomy of Silent Failures in a Production LLM Agent Runtime》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agent systems increasingly run as long-lived autonomous runtimes: scheduling jobs, calling tools, maintaining memory, and pushing results to humans. We present a longitudinal study of silent failures in one such system: a personal-assistant agent runtime in continuous production since March 2026, with roughly 40 scheduled jobs, 8 LLM providers, a tool-governance proxy, and a knowledge-base memory plane, defended by 4,286 unit tests and 827 governance checks. Over eight weeks we documented 22 incidents with full root-cause postmortems, in which one meta-pattern -- a failure whose error signal never reaches a human in actionable form -- manifested at least 28 times. We derive a five-class, mechanism-oriented taxonomy: (A) environment and platform quirks, (B) design-assumption mismatches, (C) error swallowing and dilution, (D) chained hallucination and fabrication, (E) operational omission and forensic blind spots. Class D is unique to LLM systems and the most dangerous: the system does not merely fail to report an error -- the LLM transforms it into fluent, plausible narrative delivered to the user. We term this fail-plausible: gray failure's differential observability escalated -- the observer is not just blind, it is convincingly lied to by the failure itself. Three findings: about 70% of silent failures were caught by human user-view observation, not tests or audits; a retrospective audit of 15 incidents found 0% ex-ante prevention but 87% regression blocking -- audits are regression engines, not prediction engines; incident latency (13 hours to 60 days) tracks failure mechanism, not code complexity -- the longest-lived failures lived in the seams between components, where no test runs. We describe the resulting defense framework and distill design principles for agent systems whose failures are loud, attributable, and boring. All postmortems and artifacts are public.

</details>

---

### [[20_Research/Papers/具身智能/Sensitivity_Shaping_for_Latent_Modeling|Sensitivity Shaping for Latent Modeling]]

![[assets/2606.14585_figure.png|800]]

- **arXiv**: [2606.14585](https://arxiv.org/abs/2606.14585)
- **PDF**: https://arxiv.org/pdf/2606.14585
- **详细分析**: [[20_Research/Papers/具身智能/Sensitivity_Shaping_for_Latent_Modeling|Sensitivity Shaping for Latent Modeling]]
- **作者**: Hongzhan Yu, Chenghao Li, Ruipeng Zhang, Henrik Christensen, Sicun Gao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Sensitivity Shaping for Latent Modeling》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative dynamics models enable planning in challenging robotic systems, but safe deployment requires reliably detecting policy-induced out-of-distribution (OOD) transitions. Existing methods typically treat the learned dynamics as fixed and attach post hoc support surrogates. We show that these surrogates can fail when the dynamics are locally insensitive to critical action choices: unsupported control actions may produce latent predictions that resemble demonstrated transitions, suppressing OOD signals despite large true predictive errors. To address this, we introduce support-conditioned control-sensitivity regularization, which promotes sensitive local response to control input changes in learned dynamics in high-support training regions. This preserves control-induced variation while limiting unstable extrapolation due to weak empirical support. Experiments in vision-based obstacle avoidance, manipulation, and real-robot navigation show improved OOD detection and safer closed-loop planning.

</details>

---

### [[20_Research/Papers/大模型/SIMMER_Benchmarking_Latent_Failures_in_LLM_Executable_Planning_with_a_World_Model|SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model]]

![[assets/2606.14574_figure.png|800]]

- **arXiv**: [2606.14574](https://arxiv.org/abs/2606.14574)
- **PDF**: https://arxiv.org/pdf/2606.14574
- **详细分析**: [[20_Research/Papers/大模型/SIMMER_Benchmarking_Latent_Failures_in_LLM_Executable_Planning_with_a_World_Model|SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model]]
- **作者**: Xiaoxin Lu, Ranran Haoran Zhang, Rui Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.45（加权：大模型 0.65，世界模型 0.8）
- **关联关键词**: LLM, Agent, WorldModel

#### 研究背景与动机

《SIMMER: Benchmarking Latent Failures in LLM Executable Planning with a World Model》归入 世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, TextWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly deployed as planners for autonomous agents in household environments. While existing benchmarks evaluate whether LLM-generated plans execute successfully, they overlook a critical type of failure: latent failures. Unlike immediate failures that trigger instant feedback at execution time and enable timely correction, latent failures do not immediately halt plan execution but silently compromise goal achievement. In severe cases, they cause irreversible harm. To address this gap, we introduce SIMMER, a benchmark for evaluating latent failures in LLM planning through a human-curated symbolic world model grounded in the kitchen domain. SIMMER defines a world model comprising 77 actions, 262 unique objects, and approximately 46,800 possible interactions that are semantically realistic, derived from real-world cooking scripts. It then leverages a state machine executor that validates plans against the world model and detects immediate precondition violations, latent hazards, and irreversible failures. Experiments across six LLMs show that even frontier models achieve at most 17% error-free plans. Moreover, up to 56% of plans contain latent failures, the majority of which lead to irreversible consequences. We further demonstrate that explicit state reasoning via counterfactual foresight simulation can reduce latent failures by up to 72% and irreversible cases by up to 75%, suggesting a promising direction for more robust LLM planners.

</details>

---

### [[20_Research/Papers/强化学习/TRACE_Trajectory-Routed_Causal_Memory_for_Delayed-Evidence_Visuomotor_Imitation|TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation]]

![[assets/2606.14551_figure.png|800]]

- **arXiv**: [2606.14551](https://arxiv.org/abs/2606.14551)
- **PDF**: https://arxiv.org/pdf/2606.14551
- **详细分析**: [[20_Research/Papers/强化学习/TRACE_Trajectory-Routed_Causal_Memory_for_Delayed-Evidence_Visuomotor_Imitation|TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation]]
- **作者**: Zihao Li, Ranpeng Qiu, Yincong Chen, Guoqiang Ren, Weiming Zhi
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《TRACE: Trajectory-Routed Causal Memory for Delayed-Evidence Visuomotor Imitation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots under autonomous operation may require decisions based on evidence that is no longer visible. We study \emph{delayed-evidence} tasks, where an early cue disappears before a later decision point, so visually similar observations can require different actions. In these settings, the current observation is not a sufficient state for control. We introduce TRAjectory-routed Causal Evidence (TRACE), a memory framework for visuomotor imitation policies. TRACE stores task-relevant visual and robot-state evidence, such as object identity, target choice, or route-dependent state, in a fixed-size latent memory that remains bounded over long episodes. Instead of indexing memory by raw time or manually provided task labels, TRACE uses \emph{path signatures}: compact, order-sensitive features of the executed robot-state trajectory. These signatures do not store the visual cue itself; rather, they provide trajectory-conditioned keys for writing and retrieving the evidence stored when the cue was visible. When the robot later reaches an ambiguous observation, the policy conditions on TRACE memory to recover the missing context and choose the correct branch. TRACE attaches through lightweight adapters to policies, without changing the policy backbone, action head, or imitation objective. Across real-world long-horizon manipulation tasks with visually ambiguous branch points, TRACE improves branch selection and task success over alternative baselines, including short-history and recurrent memory. Project page: https://jeong-zju.github.io/trace

</details>

---

### [[20_Research/Papers/大模型/From_Shield_to_Target_Denial-of-Service_Attacks_on_LLM-Based_Agent_Guardrails|From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails]]

![[assets/2606.14517_figure.png|800]]

- **arXiv**: [2606.14517](https://arxiv.org/abs/2606.14517)
- **PDF**: https://arxiv.org/pdf/2606.14517
- **详细分析**: [[20_Research/Papers/大模型/From_Shield_to_Target_Denial-of-Service_Attacks_on_LLM-Based_Agent_Guardrails|From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails]]
- **作者**: Yuguang Zhou, Xunguang Wang, Pingchuan Ma, Zhantong Xue, Zhaoyu Wang, Shuai Wang
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《From Shield to Target: Denial-of-Service Attacks on LLM-Based Agent Guardrails》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：BrowserGym, OSWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based guardrails have emerged as a highly effective defense against prompt injection and jailbreak attacks in autonomous agents. However, we reveal that the very reasoning and task-following capabilities enabling this protection introduce a novel vulnerability: attackers can inject crafted data to trap the guardrail in extended reasoning loops, effectuating a systematic denial-of-service (DoS) attack. To systematically expose this threat, we design a beam-search optimization framework that crafts natural-language payloads to maximize guardrail reasoning length, utilizing an LLM proposer guided by a strategy bank. Based on the observation of guardrail's schema-following nature, we also provide another attack framework driven by mechanism-aware structural mutations with less computational load. The attack efficacy is systematically evaluated in two parts. First, in standalone evaluations, the attack generalizes across diverse guardrail architectures, safety templates, and agent benchmarks. Payloads optimized on a single open-source surrogate successfully transfer to eight leading model backbones (e.g., Claude, GPT, Gemini, DeepSeek, and Qwen), achieving a 13--63$\times$ token amplification. Second, in end-to-end real-world agent deployments (web, desktop, code, and multi-agent systems), the attack reveals up to a 148$\times$ latency amplification. We show that a single poisoned document can saturate shared guardrail infrastructures, effectively starving co-located agents and paralyzing the entire system. By uncovering this availability flaw, our work underscores the urgent need to develop cost-bounded, reasoning-robust guardrails.

</details>

---

### [[20_Research/Papers/大模型/When_the_Tool_Decides_LLM_Agents_Defer_Blindly_to_Graph_Neural_Network_Tools,_and_Stronger_Backbones_Defer_More|When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More]]

![[assets/2606.14476_figure.png|800]]

- **arXiv**: [2606.14476](https://arxiv.org/abs/2606.14476)
- **PDF**: https://arxiv.org/pdf/2606.14476
- **详细分析**: [[20_Research/Papers/大模型/When_the_Tool_Decides_LLM_Agents_Defer_Blindly_to_Graph_Neural_Network_Tools,_and_Stronger_Backbones_Defer_More|When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More]]
- **作者**: Zhongyuan Wang, Pratyusha Vemuri
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《When the Tool Decides: LLM Agents Defer Blindly to Graph Neural Network Tools, and Stronger Backbones Defer More》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A growing line of work equips large language model (LLM) agents with graph neural networks (GNNs) as callable tools, assuming the agent exercises judgment over when and how much to rely on such a tool. We test this directly. We expose a frozen GNN to a ReAct-style LLM agent as an explicit tool and measure, on node classification over a text-attributed graph (ogbn-arxiv, replicated on WikiCS), whether the agent uses the tool or merely obeys it. We find the agent does not exercise judgment: its predictions agree with the raw GNN's 97.6-99.2% of the time (5 seeds), collapsing into a GNN parrot that adopts the tool's output wholesale and bypasses its own reasoning. Sweeping backbone capability (Qwen2.5 0.5B-7B), the deference is not a weak-model artifact: among models able to invoke the tool, agreement rises with capability (0.60 to 0.98 from 1.5B to 7B). Crucially, the cost of deference does not shrink as capability grows and grows where alternatives emerge: a per-node oracle over the available actions beats the parrot by 0.09-0.18 at 3B and 0.12-0.22 at 7B, roughly doubling at high homophily, because the parrot is pinned to the frozen GNN while the agent's alternatives improve; at 7B a simple neighbour-label tool overtakes the GNN at high homophily (0.81 vs 0.71) yet the agent still defers. A simple selective-invocation gate recovers about half of that high-homophily gap (0.71 to 0.83) but yields no net global gain, and held-out estimates bound the best achievable gate over standard test-time features to at most a third of the oracle headroom: reliable selective invocation looks limited by available information, not merely router design. Our results are a cautionary measurement: evaluations of agent+tool systems cannot assume the agent adds judgment on top of the tool, and selective invocation must be designed in rather than expected to emerge from scale.

</details>

---

### [[20_Research/Papers/大模型/GitOfThoughts_Version-Controlled_Reasoning_and_Agent_Memory_You_Can_Replay,_Diff,_and_Merge|GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge]]

![[assets/2606.14470_figure.png|800]]

- **arXiv**: [2606.14470](https://arxiv.org/abs/2606.14470)
- **PDF**: https://arxiv.org/pdf/2606.14470
- **详细分析**: [[20_Research/Papers/大模型/GitOfThoughts_Version-Controlled_Reasoning_and_Agent_Memory_You_Can_Replay,_Diff,_and_Merge|GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge]]
- **作者**: Pavan C Shekar, Abhishek H S, Aswanth Krishnan
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《GitOfThoughts: Version-Controlled Reasoning and Agent Memory You Can Replay, Diff, and Merge》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GPQA, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) reasoning is ephemeral: chains of thought vanish with the context window, pruned search branches leave no record, and memory buffers cannot be diffed, merged, or audited. Every other complex software process (code, infrastructure, data, experiments) is version-controlled; reasoning is not. We introduce GitOfThoughts, which stores an agent's reasoning tree as a git repository: every scored thought is a commit, scores are notes, outcomes are tags, and retrieval is "git log" over the agent's own history. This makes reasoning replayable, auditable, and mergeable across agents at near-zero engineering cost. We then ask the harder question: does memory, in any substrate, actually improve accuracy? Across five substrates (none, markdown, vector, graph, git), two benchmarks, two model scales, and pre-registered replications, the answer for novel problems is no. No memory format reliably helps, and a promising early result collapsed under its own pre-registered replication. Memory pays only above what we call the copyability threshold: when the retrieved case is a near-duplicate of the current problem (similarity &gt;~ 0.8), accuracy jumps sharply; below it, nothing. The gain is answer retrieval, not method transfer: a 4.5x larger model doubles the near-duplicate payoff yet still cannot extract a transferable method from a worked example. The only general lever we find is test-time sampling. The case for git-as-substrate is therefore auditability, provenance, and mergeability at accuracy parity. We document a retracted result and a refuted hypothesis to model the evaluation standard we hold ourselves to.

</details>

---

### [[20_Research/Papers/大模型/tap_A_File-Based_Protocol_for_Heterogeneous_LLM_Agent_Collaboration|tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration]]

![[assets/2606.14445_first_page.png|800]]

- **arXiv**: [2606.14445](https://arxiv.org/abs/2606.14445)
- **PDF**: https://arxiv.org/pdf/2606.14445
- **详细分析**: [[20_Research/Papers/大模型/tap_A_File-Based_Protocol_for_Heterogeneous_LLM_Agent_Collaboration|tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration]]
- **作者**: Minseo Kim
- **cs 子类**: cs.AI, cs.HC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《tap: A File-Based Protocol for Heterogeneous LLM Agent Collaboration》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing multi-agent software development systems have proposed many forms of agent collaboration, including role-based collaboration and automated code review. However, many systems assume a common runtime, a central conversation server, or the same API family. Under these assumptions, LLM agents from different vendors cannot easily exchange messages directly from their own execution environments while dividing development and review work on a shared codebase. This paper presents tap, a file-based collaboration protocol that allows Claude (Anthropic) and Codex (OpenAI) to collaborate on one codebase without shared memory or an identical runtime. The core of tap is a file-first design that preserves markdown files with metadata as original messages, combines a file inspection path (file communication, Tier 1) with real-time notification paths for Claude and Codex (real-time communication, Tier 2), and isolates work through separate git worktrees. Even if real-time notification fails or a receiver restarts, the message file remains available and the same content can be inspected again. In a 27-day, 37-generation self-applied operation where tap was used to develop and review itself, we collected 209 tap-related pull requests and 717 operational artifacts. An analysis of 375 review artifacts showed that the share of reviews recording at least one defect or requested change was 69.8% for heterogeneous model pairs and 53.1% for homogeneous model pairs. These results show that tap, which combines file-based message preservation with real-time notification, operates in a real production repository, and that combining heterogeneous models and execution environments can broaden review perspectives. tap is distributed as the open-source npm package @hua-labs/tap (v0.5.2).

</details>

---

### [[20_Research/Papers/强化学习/Causal_Object-Centric_Models_for_Planning_with_Monte_Carlo_Tree_Search|Causal Object-Centric Models for Planning with Monte Carlo Tree Search]]

![[assets/2606.14418_figure.png|800]]

- **arXiv**: [2606.14418](https://arxiv.org/abs/2606.14418)
- **PDF**: https://arxiv.org/pdf/2606.14418
- **详细分析**: [[20_Research/Papers/强化学习/Causal_Object-Centric_Models_for_Planning_with_Monte_Carlo_Tree_Search|Causal Object-Centric Models for Planning with Monte Carlo Tree Search]]
- **作者**: Rodion Vakhitov, Leonid Ugadiarov, Alexey Skrynnik, Aleksandr Panov
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.36，世界模型 0.56）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Causal Object-Centric Models for Planning with Monte Carlo Tree Search》归入 世界模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL, MONet, OCRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce COMET (Causal Object-centric Model for Efficient Tree search), a model-based reinforcement learning algorithm that performs Monte Carlo Tree Search in a slot-structured latent space. COMET pairs a frozen unsupervised object-centric encoder with a transformer-based world model, in which actions are bound to objects through a novel action-slot fusion mechanism that is used in slot transition prediction. Policy and value heads use object-causal attention, modulating token interactions by learned per-slot relevance scores so that decision-making concentrates on task-relevant entities. COMET adds an explicit object-level inductive bias to MuZero-style latent planning. Across eight visually and dynamically diverse tasks from the Object-Centric Visual RL benchmark, ManiSkill, Robosuite, and VizDoom, COMET achieves a higher mean normalized score during the early stages of training compared to object-centric and monolithic baselines.

</details>

---

### [[20_Research/Papers/具身智能/CSPO_Constraint-Sensitive_Policy_Optimization_for_Safe_Reinforcement_Learning|CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning]]

![[assets/2606.14415_figure.png|800]]

- **arXiv**: [2606.14415](https://arxiv.org/abs/2606.14415)
- **PDF**: https://arxiv.org/pdf/2606.14415
- **详细分析**: [[20_Research/Papers/具身智能/CSPO_Constraint-Sensitive_Policy_Optimization_for_Safe_Reinforcement_Learning|CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning]]
- **作者**: Ayoub Belouadah, Sylvain Kubler, Yves Le Traon
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，强化学习 1.6）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《CSPO: Constraint-Sensitive Policy Optimization for Safe Reinforcement Learning》归入 强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe reinforcement learning (Safe RL) aims to maximize expected return while satisfying safety constraints, typically modeled as Constrained Markov Decision Processes (CMDPs). While primal-dual methods scale well to deep RL, they often suffer from delayed constraint correction, leading to oscillatory behavior and prolonged safety violations. In this paper, we propose Constraint-Sensitive Policy Optimization (CSPO), a first-order primal-dual method that incorporates local constraint sensitivity into policy updates. CSPO augments the primal objective with a constraint-sensitive correction derived from the shortest signed distance to the safety boundary, enabling smarter recovery steps back to safety, compensating for delayed Lagrange multiplier updates, reducing oscillations near the boundary, and preserving the KKT solutions of the original constrained problem. Experiments on navigation and locomotion benchmarks demonstrate that CSPO achieves faster safety recovery and high reward preservation, resulting in higher constrained returns compared to state-of-the-art primal-dual and penalty-based methods

</details>

---

### [[20_Research/Papers/具身智能/Hy-Embodied-0.5-VLA_From_Vision-Language-Action_Models_to_a_Real-World_Robot_Learning_Stack|Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack]]

![[assets/2606.14409_figure.png|800]]

- **arXiv**: [2606.14409](https://arxiv.org/abs/2606.14409)
- **PDF**: https://arxiv.org/pdf/2606.14409
- **详细分析**: [[20_Research/Papers/具身智能/Hy-Embodied-0.5-VLA_From_Vision-Language-Action_Models_to_a_Real-World_Robot_Learning_Stack|Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack]]
- **作者**: He Zhang, Lingzhu Xiang, Haitao Lin, Zeyu Huang, Minghui Wang, Dingyan Zhong, Yubo Dong, Yihao Wu, Yongming Rao, Dongsheng Zhang, Wanjia He, Ling Chen...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.7（加权：具身智能 3.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Hy-Embodied-0.5-VLA: From Vision-Language-Action Models to a Real-World Robot Learning Stack》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HyVLA, Real-World, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this report, we present Hy-Embodied-0.5-VLA, abbreviated as HyVLA-0.5, an end-to-end system that spans the full robot learning stack: data collection, model design, continued pre-training and supervised fine-tuning, RL post-training, and real-world deployment. Each component serves a distinct role in this stack.

</details>

---

### [[20_Research/Papers/具身智能/Elastic_Queries_Reinforcement_Learning_Self-Aware_Policy_Execution_for_VLA_Models|Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models]]

![[assets/2606.14375_figure.png|800]]

- **arXiv**: [2606.14375](https://arxiv.org/abs/2606.14375)
- **PDF**: https://arxiv.org/pdf/2606.14375
- **详细分析**: [[20_Research/Papers/具身智能/Elastic_Queries_Reinforcement_Learning_Self-Aware_Policy_Execution_for_VLA_Models|Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models]]
- **作者**: Ge Wang, Xinyu Tan, Xiang Li, Man Luo, Chengsi Yao, Shenhao Yan, Jiahao Yang, Fan Feng, Honghao Cai, Xiangyuan Wang, Zhixin Mai, Yiming Zhao...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，强化学习 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Elastic Queries Reinforcement Learning: Self-Aware Policy Execution for VLA Models》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EQRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are powerful action generators for robot manipulation, but they are typically executed with fixed inference and replanning schedules. This rigidity ignores the uneven difficulty of robot control: contact-rich or uncertain states may need more computation and fresher feedback, while easier states can often be handled with fewer inference steps and longer open-loop execution. We propose Elastic Queries Reinforcement Learning (EQRL), a framework that makes each VLA policy query elastic. A lightweight latent-schedule adaptor jointly selects the latent input, denoising budget, and action chunk length, without fine-tuning the underlying VLA model. To make scheduling difficulty-aware, EQRL trains a critic over the joint latent-schedule action and derives a state difficulty signal from critic ensemble disagreement. This signal guides compute toward difficult states, while a learned residual allows task-driven correction. We formulate variable chunk execution as query-level macro-action RL with chunk-dependent discounting and an amortized number-of-function-evaluations (NFE) budget. Across simulation and real-robot manipulation, EQRL reduces amortized inference cost while preserving or improving task success.

</details>

---

### [[20_Research/Papers/大模型/Communication_Policy_Evolution_for_Proactive_LLM_Agents|Communication Policy Evolution for Proactive LLM Agents]]

![[assets/2606.14314_figure.png|800]]

- **arXiv**: [2606.14314](https://arxiv.org/abs/2606.14314)
- **PDF**: https://arxiv.org/pdf/2606.14314
- **详细分析**: [[20_Research/Papers/大模型/Communication_Policy_Evolution_for_Proactive_LLM_Agents|Communication Policy Evolution for Proactive LLM Agents]]
- **作者**: Xinbei Ma, Jiyang Qiu, Yao Yao, Zheng Wu, Yijie Lu, Xiangmou Qu, Jiaxin Yin, Xingyu Lou, Jun Wang, Weiwen Liu, Weinan Zhang, Zhuosheng Zhang...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Communication Policy Evolution for Proactive LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TravelGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents have rapidly evolved into autonomous systems, yet a persistent information gap remains between users and agents: communication is costly, while users' identical preferences further limit information exchange. To investigate how agents should communicate across modalities, this paper formalizes Communication Policy, establishes textual and UI-based policies, and then evaluates communication policies across diverse environments, personas, and model combinations. Building information asymmetry for proactive agents, we set up two complementary settings, User-Agent and Planner-Executor. Experimental results reveal complementary strengths between interaction channels: text-based interaction often facilitates task performance, while structured UI improves agents' response quality and persona compliance. Motivated by that, a hybrid method combines these advantages. We further propose Communication Policy Evolution (CPE), a self-evolution framework for refining communication policies through rollout and prompt-level evolving. Without model modification, CPE achieves the best task success across multiple settings using prompt refinement alone. Our findings identify communication behavior as a critical yet underexplored design dimension for LLM agents.

</details>

---

### [[20_Research/Papers/具身智能/Robust_Fall_Recovery_for_Armless_Bipedal-Wheeled_Robots_Via_Force-Guided_Learning|Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning]]

![[assets/2606.14270_figure.png|800]]

- **arXiv**: [2606.14270](https://arxiv.org/abs/2606.14270)
- **PDF**: https://arxiv.org/pdf/2606.14270
- **详细分析**: [[20_Research/Papers/具身智能/Robust_Fall_Recovery_for_Armless_Bipedal-Wheeled_Robots_Via_Force-Guided_Learning|Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning]]
- **作者**: Haidong Hou, Zhangguo Yu, Tao Han, Hengbo Qi, Khaleel Ghazal, Yu Zhang, Yidong Du, Xuechao Chen, Fei Meng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.9，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Robust Fall Recovery for Armless Bipedal-Wheeled Robots Via Force-Guided Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fall recovery is critical for autonomous legged locomotion. Existing methods have demonstrated that some legged robots, such as humanoids and quadrupeds, are capable of fall recovery from diverse postures by utilizing arms or coordinating multi-legs to generate support forces. Without arms or other legs to provide supportive assistance, a bipedal-wheeled robot must rely solely on the actuation of its legs, making recovery particularly difficult. To address this, we introduce FTSR (Force-guided Teacher-student framework with Stage-wise Rewards). The force-guided method constructs an external auxiliary force during simulation training that correlates directly with the robot's real-time height, explicitly formulating this force as an optimizable constraint. Through constrained reinforcement learning, the policy is guided toward reducing force dependency gradually and increasing the body height, developing internal recovery strategies despite having no arms for support. Height-progressive stage-Wise rewards progressively structure posture stabilization during recovery and transition to sustained locomotion, integrated with teacher-student architecture distilling privileged knowledge of force effects and recovery dynamics. After simulation training, the policy is deployed on a physical armless bipedal-wheeled robot and extensively evaluated. Experiments confirm robust and reliable fall recovery under diverse challenging conditions, demonstrating strong environmental adaptability and motion robustness, while maintaining full post-recovery motion capability. The framework also generalizes effectively to a high-DOF humanoid, confirming its practical generalizability. The project page is available at https://2350575870.github.io/force-guided.github.io/

</details>

---

### [[20_Research/Papers/强化学习/HarnessX_A_Composable,_Adaptive,_and_Evolvable_Agent_Harness_Foundry|HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry]]

![[assets/2606.14249_figure.png|800]]

- **arXiv**: [2606.14249](https://arxiv.org/abs/2606.14249)
- **PDF**: https://arxiv.org/pdf/2606.14249
- **详细分析**: [[20_Research/Papers/强化学习/HarnessX_A_Composable,_Adaptive,_and_Evolvable_Agent_Harness_Foundry|HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry]]
- **作者**: Tingyang Chen, Shuo Lu, Kang Zhao, Weicheng Meng, Hanlin Teng, Tianhao Li, Chao Li, Xule Liu, Jian Liang, Zhizhong Zhang, Yuan Xie, Heng Qu...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, Evaluation-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today's harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness-model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, tau^3-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. These results suggest that agent progress need not come from model scaling alone: composing and evolving runtime interfaces from execution feedback is an actionable and complementary lever. The complete codebase will be open-sourced in a future release.

</details>

---

### [[20_Research/Papers/具身智能/When_and_How_Severely_Scenario-Specific_Safety_Envelopes_for_Driving_VLAs|When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs]]

![[assets/2606.14238_figure.png|800]]

- **arXiv**: [2606.14238](https://arxiv.org/abs/2606.14238)
- **PDF**: https://arxiv.org/pdf/2606.14238
- **详细分析**: [[20_Research/Papers/具身智能/When_and_How_Severely_Scenario-Specific_Safety_Envelopes_for_Driving_VLAs|When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs]]
- **作者**: Abhinaw Priyadershi, Jelena Frtunikj
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal, Security

#### 研究背景与动机

《When and How Severely: Scenario-Specific Safety Envelopes for Driving VLAs》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DriveBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety certification of Vision-Language-Action (VLA) driving planners under ISO 21448 (SOTIF) rests on an Operational Design Domain (ODD) specification that answers two complementary questions: when does the planner start to fail, and how severely does it fail once it does? We evaluate Alpamayo R1, a 10B-parameter open-weight driving VLA, on 15,968 (clip, attack) pairs. We find a conservative-aggregate gap: an aggregate safe threshold of $σ\leq 50$ under a 15% average displacement error (ADE) budget masks well-sampled scenarios that tolerate the top of the tested grid ($σ= 70$). A Gaussian Mixture Model (GMM) on the changed-explanation subset identifies six discrete severity bands (BIC-optimal $k{=}6$), so two perturbation conditions with the same mean error can differ materially in their share of high-severity (C4/C5) failures. Joining the two analyses on the same corpus surfaces a finding neither yields in isolation: the scenarios with the loosest noise thresholds are not those with the lowest high-severity rate: STOP_SIGNAL concentrates roughly $4\times$ the C4/C5 share of LANE_KEEPING despite tolerating a larger $σ$. A deployable SOTIF ODD specification for driving VLAs therefore requires a two-dimensional safety envelope, not a single aggregate value per hazard.

</details>

---

### [[20_Research/Papers/机器人/Selective_Agentic_Recovery_for_UAV_Autonomy_with_a_Persistent_Mission_Runtime|Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime]]

![[assets/2606.14219_figure.png|800]]

- **arXiv**: [2606.14219](https://arxiv.org/abs/2606.14219)
- **PDF**: https://arxiv.org/pdf/2606.14219
- **详细分析**: [[20_Research/Papers/机器人/Selective_Agentic_Recovery_for_UAV_Autonomy_with_a_Persistent_Mission_Runtime|Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime]]
- **作者**: Taewoo Park, Kyeonghyun Yoo, Seunghyun Yoo, Hwangnam Kim
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Selective Agentic Recovery for UAV Autonomy with a Persistent Mission Runtime》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic AI can support unmanned aerial vehicle (UAV) autonomy by providing high-level recovery reasoning when local waypoint- or setpoint-based execution encounters blocked passages, repeated no-progress behavior, or mission-level ambiguity. On physical UAVs, however, remote reasoning is most useful when it is invoked selectively, since each call introduces latency, resource cost, backend uncertainty, and a need to validate the returned decision. This paper presents Persistent Mission Runtime (PMR), a UAV recovery framework that keeps the mission loop and safety-critical execution local while using an external agentic reasoner only as an on-demand recovery module. The reasoner selects from predefined recovery skills, and each returned decision is parsed, verified, safety-filtered, and mapped to local executor actions before it can affect flight. PMR introduces learned Cognitive Value of Invocation (learned-CVI), a compact admission gate that estimates when remote agentic reasoning is likely to improve near-term mission progress enough to justify its operational cost. Across a fixed 400-run Gazebo/PX4 benchmark with eight scenarios, learned-CVI raises hard/ambiguous-regime success from 5.0% under local-only autonomy to 95.0%, outperforms one-shot and periodic reasoning baselines by 20.0 and 32.5 percentage points, and reduces remote-agent calls by 16.7% and logged tokens by 29.2% relative to a manually tuned rule-based invocation baseline.

</details>

---

### [[20_Research/Papers/大模型/Closing_the_Reflection_Gap_A_Free_Calibration_Bonus_for_Agentic_RL|Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL]]

![[assets/2606.14211_figure.png|800]]

- **arXiv**: [2606.14211](https://arxiv.org/abs/2606.14211)
- **PDF**: https://arxiv.org/pdf/2606.14211
- **详细分析**: [[20_Research/Papers/大模型/Closing_the_Reflection_Gap_A_Free_Calibration_Bonus_for_Agentic_RL|Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL]]
- **作者**: Yinglun Zhu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.82（加权：大模型 0.3，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Closing the Reflection Gap: A Free Calibration Bonus for Agentic RL》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLMs are increasingly deployed as agents that interact with external environments and observe feedback such as execution results, error messages, and tool outputs. A well-functioning agent should be able to leverage this feedback to accurately assess its own performance. Yet we find a persistent reflection gap: LLM agents tend to mis-assess their own outputs after observing concrete environment feedback -- even for questions they correctly answered -- and standard RL barely helps due to a credit-assignment mismatch. To close this gap, we propose RefGRPO, a simple yet effective fix that augments standard RL algorithms with two key ingredients: a free calibration bonus computed by contrasting the agent's own reflection with the actual outcome (requiring no additional reward model, LLM judge, or external annotation), and a dynamic schedule on its coefficient. Compared to standard RL baselines, our method simultaneously improves reflection calibration (e.g., reduces underconfidence rate $44.4\% \to 7.7\%$) and task accuracy (e.g., $75.1\% \to 76.5\%$) on text-to-SQL across five benchmarks. The resulting calibrated reflection turns the agent into its own verifier grounded in environment feedback, which further enables (i) better self-improvement that uses reflections as pseudo-rewards without outcome supervision, and (ii) more effective test-time selective prediction by committing only to rollouts flagged as correct.

</details>

---

### [[20_Research/Papers/大模型/When_Should_Agent_Trust_Be_Conditional_Characterizing_and_Attacking_Skill-Conditional_Reputation_in_Agent_Swarms|When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms]]

![[assets/2606.14200_figure.png|800]]

- **arXiv**: [2606.14200](https://arxiv.org/abs/2606.14200)
- **PDF**: https://arxiv.org/pdf/2606.14200
- **详细分析**: [[20_Research/Papers/大模型/When_Should_Agent_Trust_Be_Conditional_Characterizing_and_Attacking_Skill-Conditional_Reputation_in_Agent_Swarms|When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms]]
- **作者**: Yihan Xia, Taotao Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《When Should Agent Trust Be Conditional? Characterizing and Attacking Skill-Conditional Reputation in Agent Swarms》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open platforms increasingly route tasks among heterogeneous LLM agents--differing in base model, scaffold, and tool stack--whose competence varies sharply by skill: an agent excellent at one skill may be useless at another. The standard reputation approach summarizes each agent by a single global trust score, but that scalar is the wrong object here, because routing every task to the globally most-trusted agent leaves the value of specialization unclaimed. We study skill-conditional trust R(i | k)--the trust to place in agent i for a task requiring skill k, rather than one score per agent--and pose three falsifiable questions: when is conditioning worth it, how much cross-skill evidence should be borrowed, and whether that borrowing is safe. A controlled phase-diagram analysis answers the first two: conditional trust wins only in a specific regime--high agent heterogeneity, sparse per-skill evidence, and correlated skills--and the coupling strength beta that buys this data efficiency is dual-use, because the same cross-skill borrowing is also a laundering channel. On a public benchmark of 14 genuinely heterogeneous AppWorld agents, real pools land inside the beneficial regime--a small but genuine gain, with the per-skill best agent genuinely changing across skills. We then show that an attacker with cheap evidence in one skill and none in a target skill hijacks the conditional router, driving routing regret from 0 to 0.94 on a pool our zero-cost Conditional Information Value Test (CIVT) rates GREEN--while the ungated trust verdict it contaminates reads -0.06 instead of the honest +0.19. A zero-evidence gate bounds the attack but does not eliminate it; we characterize the residual cost under an explicit budget. We do not claim Sybil-resistance--we quantify the trade-off.

</details>

---

### [[20_Research/Papers/大模型/Implicit_Reasoning_for_Large_Language_Model-based_Generative_Recommendation|Implicit Reasoning for Large Language Model-based Generative Recommendation]]

![[assets/2606.14142_figure.png|800]]

- **arXiv**: [2606.14142](https://arxiv.org/abs/2606.14142)
- **PDF**: https://arxiv.org/pdf/2606.14142
- **详细分析**: [[20_Research/Papers/大模型/Implicit_Reasoning_for_Large_Language_Model-based_Generative_Recommendation|Implicit Reasoning for Large Language Model-based Generative Recommendation]]
- **作者**: Yinhan He, Liam Collins, Bhuvesh Kumar, Jundong Li, Neil Shah, Donald Loveland
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM

#### 研究背景与动机

《Implicit Reasoning for Large Language Model-based Generative Recommendation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) are increasingly adopted as backbones for Generative Recommendation (GR), promising access to pretrained world knowledge. Yet reliably invoking this knowledge for GR remains poorly understood. A key obstacle is that LLM-based GR typically represents items with Semantic IDs (SIDs), disrupting LLMs' natural-language reasoning interface because these tokens are unseen by the LLM during pretraining. Existing approaches address this with expensive multi-stage pipelines that ground SIDs and elicit explicit rationales, but offer limited insight into when and why each stage is necessary. In this work, we systematically decompose explicit reasoning training pipelines for LLM-based GR, revealing three key limitations: weakened world-knowledge verbalization, misalignment between SID and natural-language token embedding spaces, and sensitivity to rationale quality, all of which hurt explicit reasoning performance. To circumvent these issues, we propose PauseRec, a lightweight implicit reasoning paradigm tailored for GR. PauseRec is exceptionally practical, avoiding costly reasoning trace acquisition and reasoning alignment training, leading to a multitude of benefits: (1) it outperforms standard explicit CoT methods by up to 6.22%, (2) it reduces training cost by up to 65% GPU hours, and (3) it speeds up inference by up to 71.3%. These results position PauseRec as a lightweight alternative to explicit rationale generation, enabling more effective and efficient LLM-based GR.

</details>

---

### [[20_Research/Papers/大模型/Formalizing_Numerical_Analysis_An_Agent_Pipeline_and_Quality_Audit_Beyond_Kernel_Acceptance|Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance]]

![[assets/2606.14000_figure.png|800]]

- **arXiv**: [2606.14000](https://arxiv.org/abs/2606.14000)
- **PDF**: https://arxiv.org/pdf/2606.14000
- **详细分析**: [[20_Research/Papers/大模型/Formalizing_Numerical_Analysis_An_Agent_Pipeline_and_Quality_Audit_Beyond_Kernel_Acceptance|Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance]]
- **作者**: Theodore Meek, Siyuan Ge, Di Qiu Xiang, Simon Chess, Vasily Ilin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Formalizing Numerical Analysis: An Agent Pipeline and Quality Audit Beyond Kernel Acceptance》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ProofNet, PutnamBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work has demonstrated that coding agents can formalize entire advanced mathematics textbooks in Lean 4, yet existing efforts concentrate on branches of mathematics already well-represented in mathlib and measure success solely through kernel acceptance. We address both limitations by applying a coding agent to formalize Numerical Methods for Ordinary Differential Equations, a textbook in numerical analysis that is largely absent from mathlib, stressing the agent's capacity to develop new theory from scratch. We further introduce a systematic, reproducible three-dimensional framework for evaluating the quality of agent-produced formalizations beyond compilation: semantic correctness, Mathlib reuse, and cross-file reuse via LLM-as-judge methods. Applying this framework to our own formalization and to the released outputs of RepoProver and M2F, we uncover recurring unfaithful formalization patterns, including incomplete multi-part statements, added weakening hypotheses, and parameter restrictions, that kernel acceptance entirely obscures. Our results suggest that compilation-based metrics substantially overstate formalization quality, and we provide a reproducible audit methodology to support more rigorous evaluation of future autoformalization systems.

</details>

---

### [[20_Research/Papers/大模型/Hidden_in_Plain_Sight_Benchmarking_Agent_Safety_Against_Decomposition_Attacks_with_DECOMPBENCH|Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH]]

![[assets/2606.13994_figure.png|800]]

- **arXiv**: [2606.13994](https://arxiv.org/abs/2606.13994)
- **PDF**: https://arxiv.org/pdf/2606.13994
- **详细分析**: [[20_Research/Papers/大模型/Hidden_in_Plain_Sight_Benchmarking_Agent_Safety_Against_Decomposition_Attacks_with_DECOMPBENCH|Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH]]
- **作者**: Vikhyath Kothamasu, Virginia Smith, Chhavi Yadav
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Hidden in Plain Sight: Benchmarking Agent Safety Against Decomposition Attacks with DECOMPBENCH》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeCompBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based Agents are becoming increasingly capable and widely deployed, creating growing incentives for adversarial misuse in the real-world. A key emerging threat is Decomposition Attacks \cite{glukhov2024breach, jones2024adversaries} in which a harmful task is broken into simpler, benign subtasks that evade safety mechanisms when executed separately but cumulatively fulfill the malicious intent. Although recent benchmarks assess agent safety in multi-turn and multi-tool-use settings, they do not explicitly capture this form of decompositional misuse and may not represent realistic adversarial execution flows. To this end, we introduce DeCompBench, a benchmark designed specifically to evaluate agentic safety under decomposition attacks. DeCompBench is created with a decomposition-by-design principle using a graphical framework and enables harmful task decomposition into individually benign and executable subtasks with realistic workflows. Our experiments using a custom decomposer show that state-of-the-art agents exhibit high refusal rates on monolithic harmful tasks, but significantly lower refusal rates on their decomposed variants, while often inadvertently fulfilling the adversarial objectives. These findings underscore the need for safety evaluations against decomposition attacks and corresponding defenses. Our dataset is publicly available and can be found at https://huggingface.co/datasets/decompositionbench/DeCompBench.

</details>

---

### [[20_Research/Papers/大模型/Minim_Privacy-Aware_Minimal_View_for_Agents_via_Trusted_Local_Sanitization|Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization]]

![[assets/2606.13949_figure.png|800]]

- **arXiv**: [2606.13949](https://arxiv.org/abs/2606.13949)
- **PDF**: https://arxiv.org/pdf/2606.13949
- **详细分析**: [[20_Research/Papers/大模型/Minim_Privacy-Aware_Minimal_View_for_Agents_via_Trusted_Local_Sanitization|Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization]]
- **作者**: Hexuan Yu, Chaoyu Zhang, Heng Jin, Shanghao Shi, Ning Zhang, Y. Thomas Hou, Wenjing Lou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Minim: Privacy-Aware Minimal View for Agents via Trusted Local Sanitization》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern LLM-powered autonomous agents increasingly rely on rich user interface (UI) state observations to achieve reliable action grounding in complex digital environments. However, many deployments transmit the full UI state to remote inference servers even when most elements are irrelevant to the current task, which can leak sensitive but unnecessary context such as authentication codes, private notifications, and background application states. We propose MINIM, a trusted local broker that performs privacy-aware minimization on the client side before any observation leaves the device. Grounded in Contextual Integrity (CI), MINIM learns a dual-score representation for each UI element by predicting an inherent sensitivity score (s) and a task-conditioned necessity score (n). These scores drive a ternary disclosure policy that keeps essential elements, abstracts sensitive attributes when needed, and removes task-irrelevant content. We optimize a CI-aware objective that penalizes necessity errors more strongly on high-risk content, enabling aggressive pruning while preserving task-critical information. Experiments on real-world UI observations derived from WebArena show that MINIM substantially reduces task-irrelevant sensitive leakage while preserving task-critical semantic context and the interactive affordances required for reliable agent actions.

</details>

---

### [[20_Research/Papers/大模型/A_Multi-Agent_AI_System_for_Automated_High_School_Transcript_Processing_Collaborative_Document_Analysis_at_Scale|A Multi-Agent AI System for Automated High School Transcript Processing: Collaborative Document Analysis at Scale]]

![[assets/2606.13916_figure.png|800]]

- **arXiv**: [2606.13916](https://arxiv.org/abs/2606.13916)
- **PDF**: https://arxiv.org/pdf/2606.13916
- **详细分析**: [[20_Research/Papers/大模型/A_Multi-Agent_AI_System_for_Automated_High_School_Transcript_Processing_Collaborative_Document_Analysis_at_Scale|A Multi-Agent AI System for Automated High School Transcript Processing: Collaborative Document Analysis at Scale]]
- **作者**: Ben Torkian, Jun Zhou
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, Systems

#### 研究背景与动机

《A Multi-Agent AI System for Automated High School Transcript Processing: Collaborative Document Analysis at Scale》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Each year, college admissions offices face an overwhelming challenge: processing millions of high school transcripts, each with unique formats, grading systems, and layouts. This manual process creates operational bottlenecks that delay admissions decisions and consume valuable resources. We present a transformative solution through a multi-agent AI system where specialized agents collaborate to automatically process diverse transcript formats through intelligent coordination and communication. Our multi-agent architecture consists of three specialized agents-a Pattern Recognition Agent for format-specific parsing, a Semantic Analysis Agent for natural language understanding, and a Vision Intelligence Agent for multimodal document analysis-coordinated by an Orchestration Agent that manages agent communication and result reconciliation. Our key innovation lies in agent-based quality control using GPA extraction as a coordination signal, ensuring reliable agent collaboration and preventing critical information loss. When evaluated on 40 real world transcripts from high schools across 13 U.S. states, our agent system successfully processed every document, achieving 96.7% accuracy compared to expert manual review while maintaining practical processing speeds of 45 seconds per transcript. This work demonstrates how multi-agent coordination can solve complex document processing challenges, offering institutions a scalable, collaborative AI solution that preserves accuracy while dramatically reducing processing time.

</details>

---

### [[20_Research/Papers/具身智能/SANA_What_Matters_for_QA_Agents_over_Massive_Data_Lakes|SANA: What Matters for QA Agents over Massive Data Lakes?]]

![[assets/2606.13904_figure.png|800]]

- **arXiv**: [2606.13904](https://arxiv.org/abs/2606.13904)
- **PDF**: https://arxiv.org/pdf/2606.13904
- **详细分析**: [[20_Research/Papers/具身智能/SANA_What_Matters_for_QA_Agents_over_Massive_Data_Lakes|SANA: What Matters for QA Agents over Massive Data Lakes?]]
- **作者**: Austin Senna Wijaya, Jiaxiang Liu, Haonan Wang, Eugene Wu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《SANA: What Matters for QA Agents over Massive Data Lakes?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EQA, FeTaQA, HotpotQA, KramaBench, LakeQA, OTT-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Exploratory question answering (EQA) over data lakes requires an LLM agent to discover relevant sources, analyze retrieved data, and adapt its actions based on intermediate results. End-to-end accuracy alone cannot distinguish failures in search, planning, data analysis, or the agent's Action Policy: its decisions about what to do next and when to submit an answer. We present SANA (Search Agent Navigation Ablation framework), a diagnostic ablation framework that transforms EQA tasks into runtime profiles containing gold source sequence, sanitized subquestions, and execution records. SANA uses these profiles to construct idealized search, planning, and data-analysis tools, allowing each component to be ablated; the residual gap is diagnostic evidence for policy failures. To illustrate SANA as a reusable evaluation framework, we adapted two recent EQA benchmarks, LakeQA and KramaBench, and evaluated lightweight and mid-sized agents under fixed prompts, budgets, data lakes, and runtimes. Across both benchmarks, data analysis is a consistent bottleneck while planning is less so. Search is a major limitation in LakeQA's large data-lake setting, but less so for the smaller-scale KramaBench. SANA thus deconstructs end-to-end task accuracies into a diagnosis of where data-lake agents fail, and allows for systematic comparisons of progress in search, planning, data analysis, and agent design.

</details>

---

### [[20_Research/Papers/大模型/Capability_Minimization_as_a_Safety_Primitive_Risk-Aware_Causal_Gating_for_Least-Privilege_LLM_Agents|Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents]]

![[assets/2606.13884_figure.png|800]]

- **arXiv**: [2606.13884](https://arxiv.org/abs/2606.13884)
- **PDF**: https://arxiv.org/pdf/2606.13884
- **详细分析**: [[20_Research/Papers/大模型/Capability_Minimization_as_a_Safety_Primitive_Risk-Aware_Causal_Gating_for_Least-Privilege_LLM_Agents|Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents]]
- **作者**: Laxmipriya Ganesh Iyer, Rahul Suresh Babu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Capability Minimization as a Safety Primitive: Risk-Aware Causal Gating for Least-Privilege LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern decision systems increasingly rely on learned components whose outputs may be confident yet wrong, exposing downstream actions to costly errors. We introduce Risk-Aware Causal Gating (RACG), a framework that decides whether to act on, defer, or abstain from a model's prediction by combining causal effect estimation with calibrated risk control. RACG models the causal pathway from candidate actions to outcomes and gates each decision according to an estimated counterfactual risk rather than raw predictive confidence. To make gating reliable, we derive distribution-free bounds on the probability of acting under high-risk conditions and show how these bounds translate into operating thresholds that satisfy user-specified safety constraints. We further propose an adaptive gating policy that adjusts to distribution shift by monitoring discrepancies between predicted and realized outcomes, tightening the gate when causal assumptions appear violated. Across simulated interventions and real-world decision benchmarks, RACG reduces high-cost errors substantially while preserving most of the utility of an ungated policy, and it outperforms confidence-based and selective-prediction baselines at matched abstention rates. Our results indicate that explicitly separating causal risk from predictive uncertainty yields decision systems that are both safer and more transparent, offering a principled mechanism for trustworthy automation in high-stakes settings.

</details>

---

### [[20_Research/Papers/大模型/When_Plausible_Is_Not_Realistic_Evaluating_Human_Mobility_in_LLM-Based_Urban_Simulation|When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation]]

![[assets/2606.13835_figure.png|800]]

- **arXiv**: [2606.13835](https://arxiv.org/abs/2606.13835)
- **PDF**: https://arxiv.org/pdf/2606.13835
- **详细分析**: [[20_Research/Papers/大模型/When_Plausible_Is_Not_Realistic_Evaluating_Human_Mobility_in_LLM-Based_Urban_Simulation|When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation]]
- **作者**: Gustavo H. Santos, Aline Carneiro Viana, Thiago H. Silva
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《When Plausible Is Not Realistic: Evaluating Human Mobility in LLM-Based Urban Simulation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CitySim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM-based generative agents are increasingly used in urban simulators, yet it remains unclear whether they reproduce empirically realistic human mobility patterns or merely generate plausible mobility narratives. We introduce a validation framework for evaluating the mobility of generative agents of LLM-based urban simulators against real-world mobility data. For this, we use mobility laws, temporal rhythms, network motifs, semantic activity transitions, and behavioral mobility profiles. Using datasets from the Greater Paris region and Shanghai, we evaluate AgentSociety and CitySim across multiple dimensions of mobility realism. Our analysis reveals a substantial gap between narrative plausibility and empirical mobility realism. Although the simulators capture some high-level semantic activity distributions, they struggle to reproduce core spatial and temporal constraints, including realistic trip-length distributions, origin-destination flows, dwell times, and transition dynamics. We further observe that realistic mobility diversity is unstable across default prompting configurations and may require explicit profile-aware initialization. To support reproducible evaluation, we also contribute scalable and open LLM-driven infrastructure for regional-scale map generation, observability-enhanced simulation, mobility-metric computation, and traffic simulation. Our findings highlight the need for rigorous empirical validation of LLM-based urban simulators and provide practical tools for building more realistic and reproducible urban simulation systems.

</details>

---

### [[20_Research/Papers/强化学习/Safety-Contract_Graph_Multi-Agent_Reinforcement_Learning_for_Autonomous_Network_Security_Response|Safety-Contract Graph Multi-Agent Reinforcement Learning for Autonomous Network Security Response]]

![[assets/2606.13832_figure.png|800]]

- **arXiv**: [2606.13832](https://arxiv.org/abs/2606.13832)
- **PDF**: https://arxiv.org/pdf/2606.13832
- **详细分析**: [[20_Research/Papers/强化学习/Safety-Contract_Graph_Multi-Agent_Reinforcement_Learning_for_Autonomous_Network_Security_Response|Safety-Contract Graph Multi-Agent Reinforcement Learning for Autonomous Network Security Response]]
- **作者**: Jose Luis Lima de Jesus Silva
- **cs 子类**: cs.AI, cs.CR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.62（加权：大模型 0.5，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, Security

#### 研究背景与动机

《Safety-Contract Graph Multi-Agent Reinforcement Learning for Autonomous Network Security Response》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous network-security response systems promise to reduce Security Operations Centre (SOC) reaction latency, but reward-only multi-agent reinforcement learning (MARL) can improve security reward while remaining non-deployable. We present a safety-contract graph MARL framework and instantiate it as ACD$^3$-GAT (Adaptive Constrained Counterfactual Decisioning with a Graph Attention Network encoder), an architecture that separates simulator observations from reusable operational budgets, constrained optimization, graph state encoding, and counterfactual action screening. We evaluate the method in CAGE Challenge 4, where agents operate under budgets for Mean Time to Recover (MTTR), false-positive response, and firewall change-management disruption. Across the benchmark, every unconstrained method violates the SOC downtime budget in 100% of evaluated episodes, with mean downtime proxy costs of 311-430 against a budget of 50. This complements prior CAGE Challenge 4 findings by showing that reward-only learning lacks operational discipline. Constrained MAPPO-GAT (C-MAPPO-GAT) isolates Lagrangian operational-cost control and budget-aware screening, while ACD$^3$-GAT adds budget context, CVaR tail-risk estimation, opponent-belief state, and Graph Counterfactual Risk Propagation (G-CRP). The replicated comparison includes three 200-episode seeds for IPPO, MAPPO-GAT, C-MAPPO-GAT, and ACD$^3$-GAT. C-MAPPO-GAT reduces downtime violation from 100% to 0.3% and mean downtime cost from 355.4 to 15.5 relative to MAPPO-GAT. ACD$^3$-GAT reduces mean downtime cost to 48.2 with a 13.8% violation rate, placing it on the safety-contract frontier rather than at the most conservative compliance point. Topology-seed and coupled adaptive Red-process stress tests preserve this contrast and show lower worst adaptive degradation for safety-constrained policies than reward-only MAPPO-GAT.

</details>

---

### [[20_Research/Papers/大模型/SEVRA-BENCH_Social_Engineering_of_Vulnerabilities_in_Review_Agents|SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents]]

![[assets/2606.13757_figure.png|800]]

- **arXiv**: [2606.13757](https://arxiv.org/abs/2606.13757)
- **PDF**: https://arxiv.org/pdf/2606.13757
- **详细分析**: [[20_Research/Papers/大模型/SEVRA-BENCH_Social_Engineering_of_Vulnerabilities_in_Review_Agents|SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents]]
- **作者**: Rui Melo, Riccardo Fogliato, Sean Zhou, Pratiksha Thaker, Zhiwei Steven Wu
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《SEVRA-BENCH: Social Engineering of Vulnerabilities in Review Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Sevra-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) reviewers are increasingly used in pull-request (PR) workflows, where their approvals help decide which code is merged into a repository. This raises a question that benchmarks for static vulnerability detection or code generation do not address: can an automated reviewer reject a malicious contribution when the attacker controls both the code change and the accompanying PR text? We introduce SEVRA-BENCH (Social Engineering of Vulnerabilities in Review Agents), a benchmark that measures how often an automated reviewer approves such adversarial pull requests. Each malicious PR in SEVRA-BENCH is built from a real project commit that previously fixed a vulnerability listed in the Common Vulnerabilities and Exposures (CVE) database. We automatically invert that fix to restore the original vulnerable code and submit it as a pull request wrapped in one of 15 social-engineering framings, which vary the claims made, the supporting evidence, the urgency conveyed, signals of prior approval, and appeals to authority. SEVRA-BENCH contains 1,062 malicious PRs drawn from Common Vulnerabilities and Exposures (CVE)-linked fixes across the top 10 entries of the 2025 Common Weakness Enumeration (CWE) Top 25. In a realistic setting, we evaluate 8 current LLMs as code review agents on PRs that introduce vulnerabilities previously reported in public disclosures. Our results reveal a sharp gap in security capabilities between closed- and open-source models. We hope SEVRA-BENCH will serve as a valuable resource for advancing open-source models and narrowing this gap.

</details>

---

### [[20_Research/Papers/强化学习/Hybrid_Open-Ended_Tri-Evolution_Makes_Better_Deep_Researcher|Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher]]

![[assets/2606.13710_figure.png|800]]

- **arXiv**: [2606.13710](https://arxiv.org/abs/2606.13710)
- **PDF**: https://arxiv.org/pdf/2606.13710
- **详细分析**: [[20_Research/Papers/强化学习/Hybrid_Open-Ended_Tri-Evolution_Makes_Better_Deep_Researcher|Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher]]
- **作者**: Hongming Piao, Chi Liu, Mengzhuo Chen, Yan Shu, Derek Li, Ying Wei, Bryan Dai
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Hybrid Open-Ended Tri-Evolution Makes Better Deep Researcher》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep research and agent evolution serve as de-facto tasks for AI agents in real-world applications toward artificial general intelligence. The former enables autonomous retrieval and integration of information in open-ended environments to tackle open-ended research tasks, yet it is constrained by the static parametric deep research capabilities of agent systems. The latter allows agents to autonomously interact with the environment to gain experiences that evolve model capabilities. However, its effectiveness has been widely validated only on verifiable tasks with standard answers, leaving a gap with open-ended research tasks. To bridge these two critical tasks, we propose the Hybrid Open-Ended Tri-Evolution (HOTE) framework, which leverages hybrid-mode reinforcement learning to facilitate the collaborative evolution of a proposer, solver and judge based on web-scale knowledge, moving toward autonomous evolving agents in open-ended tasks and environments. Extensive experiments on three long-form deep research benchmarks demonstrate that the 8B model trained via HOTE surpasses the strongest static open 8-32B models as well as those trained by state-of-the-art deep research training methods with less time overhead, and further verify that the evolution of all three modules in HOTE is indispensable.

</details>

---

### [[20_Research/Papers/大模型/Orchestra-o1_Omnimodal_Agent_Orchestration|Orchestra-o1: Omnimodal Agent Orchestration]]

![[assets/2606.13707_figure.png|800]]

- **arXiv**: [2606.13707](https://arxiv.org/abs/2606.13707)
- **PDF**: https://arxiv.org/pdf/2606.13707
- **详细分析**: [[20_Research/Papers/大模型/Orchestra-o1_Omnimodal_Agent_Orchestration|Orchestra-o1: Omnimodal Agent Orchestration]]
- **作者**: Fan Zhang, Vireo Zhang, Shengju Qian, Haoxuan Li, Hao Wu, Jinyang Wu, Donghao Zhou, Zhihong Zhu, Zheng Lian, Xin Wang, Pheng-Ann Heng
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.35（加权：大模型 0.95，强化学习 0.4）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Orchestra-o1: Omnimodal Agent Orchestration》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The recent success of agent swarms has shifted the paradigm of large language model (LLM)-based agents from single-agent workflows to multi-agent systems, highlighting the importance of agent orchestration for task decomposition and collaboration. However, existing orchestration frameworks are limited to a narrow set of modalities and struggle to generalize to more complex settings where heterogeneous modalities coexist and interact. This limitation becomes particularly pronounced in omnimodal scenarios, where tasks require the unified understanding and coordination of diverse inputs such as text, image, audio, and video. In this work, we propose Orchestra-o1, an omnimodal agent orchestration framework designed to support efficient agent collaboration across multiple modalities. Orchestra-o1 introduces a unified orchestration mechanism that enables modality-aware task decomposition, online sub-agent specialization, and parallel sub-task execution. This scalable design allows agent systems to effectively tackle complex real-world tasks involving heterogeneous information sources, surpassing the second-best approach by 10.3% accuracy on the OmniGAIA benchmark. Furthermore, we introduce decision-aligned group relative policy optimization (DA-GRPO), an efficient agentic reinforcement learning approach for training Orchestra-o1-8B, which also achieves state-of-the-art performance against all existing open-source omnimodal agents.

</details>

---

### [[20_Research/Papers/强化学习/A_Deep_Reinforcement_Learning_(DRL)-Based_Transformer_Method_for_Solving_the_Open_Shop_Scheduling_Problem|A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem]]

![[assets/2606.13682_first_page.png|800]]

- **arXiv**: [2606.13682](https://arxiv.org/abs/2606.13682)
- **PDF**: https://arxiv.org/pdf/2606.13682
- **详细分析**: [[20_Research/Papers/强化学习/A_Deep_Reinforcement_Learning_(DRL)-Based_Transformer_Method_for_Solving_the_Open_Shop_Scheduling_Problem|A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem]]
- **作者**: Faezeh Ardali, Mwembezi A. Nyelele, Gerald M. Knapp
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.52（加权：强化学习 1.36，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《A Deep Reinforcement Learning (DRL)-Based Transformer Method for Solving the Open Shop Scheduling Problem》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The open shop scheduling problem (OSSP) arises in many industrial and service settings but remains computationally challenging as the number of jobs and machines increases. While exact methods quickly become intractable, classical dispatching rules and metaheuristics may require substantial tuning to maintain solution quality at large scales. This study develops a Transformer-based scheduling policy for OSSP using an encoder-decoder architecture with multi-head attention. The model is trained on Taillard benchmark instances (4x4, 5x5, 7x7, and 10x10) using only the processing-time matrix as input and produces feasible schedules with makespans typically within 15-30% of best-known values. To evaluate scalability, the trained policy is applied without retraining to randomly generated instances from 40x40 to 100x100 and compared against classical dispatching heuristics, including SPT, LPT, MWKR, and EST. Across these large instances, the Transformer achieved average gaps of 12.89-15.12% relative to a standard lower bound. Compared with EST, the Transformer remained competitive, typically within a modest margin, while substantially outperforming SPT and LPT. These results indicate that a Transformer policy trained on small OSSP instances can generalize to substantially larger problems and provide a feature-light, learning-based alternative to classical dispatching rules.

</details>

---

### [[20_Research/Papers/大模型/GAGPO_Generalized_Advantage_Grouped_Policy_Optimization|GAGPO: Generalized Advantage Grouped Policy Optimization]]

![[assets/2605.13217_figure.png|800]]

- **arXiv**: [2605.13217](https://arxiv.org/abs/2605.13217)
- **PDF**: https://arxiv.org/pdf/2605.13217
- **详细分析**: [[20_Research/Papers/大模型/GAGPO_Generalized_Advantage_Grouped_Policy_Optimization|GAGPO: Generalized Advantage Grouped Policy Optimization]]
- **作者**: Siyuan Zhu, Chao Yu, Rongxin Yang, Zongkai Liu, Jinjun Hu, Qiwen Chen, Yibo Zhang
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.77（加权：大模型 0.45，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《GAGPO: Generalized Advantage Grouped Policy Optimization》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has become a powerful paradigm for post-training large language model agents, yet credit assignment in multi-turn environments remains a challenge. Agents often receive sparse, trajectory-level rewards only at the end of an episode, making it difficult to determine which intermediate actions contributed to success or failure. As a result, propagating delayed outcomes back to individual decision steps without relying on costly auxiliary value models remains an open problem. We propose Generalized Advantage Grouped Policy Optimization (GAGPO), a critic-free reinforcement learning method for precise, step-aligned temporal credit assignment. GAGPO constructs a non-parametric grouped value proxy from sampled rollouts and uses it to compute TD/GAE-style temporal advantages, recursively propagating outcome supervision backward through time. Combined with group-wise advantage normalization and an action-level importance ratio, GAGPO extracts stable, localized optimization signals directly from multi-turn trajectories. Experiments on ALFWorld and WebShop show that GAGPO outperforms strong reinforcement learning baselines. Further analyses demonstrate faster early-stage learning, improved interaction efficiency, and smoother optimization dynamics, suggesting that GAGPO offers a simple yet effective framework for multi-turn agentic reinforcement learning.

</details>

---
