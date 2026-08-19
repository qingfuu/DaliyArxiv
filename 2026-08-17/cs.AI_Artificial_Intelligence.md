# cs.AI | Artificial Intelligence | 2026-08-17

#arxiv #ComputerScience

**论文数**: 50

### [[20_Research/Papers/世界模型/Marionette_Predicting_World_States,_Rendering_Geometry,_Painting_Appearance|Marionette: Predicting World States, Rendering Geometry, Painting Appearance]]

![[assets/2608.14530_figure.png|800]]

- **arXiv**: [2608.14530](https://arxiv.org/abs/2608.14530)
- **PDF**: https://arxiv.org/pdf/2608.14530
- **详细分析**: [[20_Research/Papers/世界模型/Marionette_Predicting_World_States,_Rendering_Geometry,_Painting_Appearance|Marionette: Predicting World States, Rendering Geometry, Painting Appearance]]
- **作者**: Zian Meng, Zhen Li, Chuanhao Li, Qiang Li, Kaipeng Zhang
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.6（加权：世界模型 0.6）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Marionette: Predicting World States, Rendering Geometry, Painting Appearance》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：WildWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive game world models typically autoregress visual observations directly in pixel or latent space, forcing structured properties such as pose, geometry, and occlusion to be implicitly maintained by the same generative sequence. Over long horizons, errors in these latent world properties accumulate, making consistency and controllability fragile. We explicitly model the evolving world state, delegate exact geometric computation to a fixed, zero-parameter renderer, and leave the neural model to synthesize appearance. We instantiate this idea as Marionette, a world model for interactive games with articulated characters. First, a two-stage autoregressive dynamics model predicts an explicit and interpretable 276-dimensional 3D world state comprising multi-entity articulated skeletons, metric root trajectories, and rotations. Second, a zero-parameter graphics bridge converts the predicted state into pose-control videos, computing world-space geometry and occlusion in closed form. Third, a control-conditioned video-diffusion observation model synthesizes photorealistic RGB observations from the resulting structured controls. Our experiments establish two properties of Marionette. First, the predicted world state is directly controllable. Forcing a mismatched action stream changes root-aligned joint error by 31% across 48 held-out segments. Second, long-horizon behaviour is determined in the state, and can be repaired there. Left free, the two generated characters drift to 21.2 m apart (recorded sessions stay near 5 m) and a third of frames show ground penetration. Two rules imposed on the explicit state, a terrain collider and a separation cap, cut penetration by 66% and keep the pair engaged, with no change to the observation model. Routing appearance through the predicted state costs no fidelity we can detect, at an FVD of 831 against 799 for recorded pose.

</details>

---

### [[20_Research/Papers/世界模型/Ensuring_Safe_Physical_AI_in_Urban_Mobility_via_Hazard-Informed_Synthesized_Envelopes|Ensuring Safe Physical AI in Urban Mobility via Hazard-Informed Synthesized Envelopes]]

![[assets/2608.14481_figure.png|800]]

- **arXiv**: [2608.14481](https://arxiv.org/abs/2608.14481)
- **PDF**: https://arxiv.org/pdf/2608.14481
- **详细分析**: [[20_Research/Papers/世界模型/Ensuring_Safe_Physical_AI_in_Urban_Mobility_via_Hazard-Informed_Synthesized_Envelopes|Ensuring Safe Physical AI in Urban Mobility via Hazard-Informed Synthesized Envelopes]]
- **作者**: Alexei Odinokov, Rostislav Yavorskiy
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.2（加权：具身智能 0.3，世界模型 0.2，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Ensuring Safe Physical AI in Urban Mobility via Hazard-Informed Synthesized Envelopes》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As heterogeneous robotic systems deploy across diverse urban zones, maintaining safety amid complex human-robot interactions remains a critical challenge. We present a unified framework that bridges systematic hazard analysis and runtime enforcement using hazard-informed safety envelopes. Rather than treating safety as a static constraint isolated within individual software modules, we introduce a cross-layer safety transformation process spanning symbolic, spatial, and dynamic world models. We show how this representation naturally interfaces with physical AI runtime harnesses to guarantee safe urban mobility.

</details>

---

### [[20_Research/Papers/大模型/Wyvern_An_Agentic_Framework_for_Generating_Grounded_Multimodal_Reports|Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports]]

![[assets/2608.14446_figure.png|800]]

- **arXiv**: [2608.14446](https://arxiv.org/abs/2608.14446)
- **PDF**: https://arxiv.org/pdf/2608.14446
- **详细分析**: [[20_Research/Papers/大模型/Wyvern_An_Agentic_Framework_for_Generating_Grounded_Multimodal_Reports|Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports]]
- **作者**: Beatrice Alessandra Motetti, Emilien Guandalino, Daniele Jahier Pagliari, Alessio Burrello, Lorenz K. Müller, Konstantin Berestizshevsky, Lukas Cavigelli
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Wyvern: An Agentic Framework for Generating Grounded Multimodal Reports》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the current artificial intelligence-driven innovation era, the pace of knowledge growth is accelerating, and is hard to keep up with. While generative models are increasingly used to synthesize content, they often lack in information grounding. To address these peculiarities of our time, we propose Wyvern, a multi-agent framework for the automated generation of grounded, multimodal technical reports. Wyvern allows for the generation of multimodal outputs, integrating images, tables, and text with supporting references in a unified report. Additionally, a particular focus is placed on the grounding of the content, with the implementation of a claims auto-revision stage. We conduct a human evaluation study to assess the quality of our proposed framework. The results show that the figures' informativeness is perceived as superior to that of a recent baseline in 87% of cases. Furthermore, Wyvern's reports are rated as more useful than those produced by three alternative methods in 63% to 100% of instances. We also carry out automatic evaluations showing that Wyvern gains up to 2.3$\times$ in citation recall and 1.6$\times$ in citation precision with respect to the baselines.

</details>

---

### [[20_Research/Papers/大模型/Whose_doctor_does_the_AI_recommend_An_algorithm_audit_of_reputation_and_demographic_signals_in_large_language_model-assisted_physician_choic|Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice]]

![[assets/2608.14399_first_page.png|800]]

- **arXiv**: [2608.14399](https://arxiv.org/abs/2608.14399)
- **PDF**: https://arxiv.org/pdf/2608.14399
- **详细分析**: [[20_Research/Papers/大模型/Whose_doctor_does_the_AI_recommend_An_algorithm_audit_of_reputation_and_demographic_signals_in_large_language_model-assisted_physician_choic|Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice]]
- **作者**: Syeda Anshrah Gillani, Mirza Samad Ahmed Baig
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.15（加权：大模型 1.15）
- **关联关键词**: LLM

#### 研究背景与动机

《Whose doctor does the AI recommend? An algorithm audit of reputation and demographic signals in large language model-assisted physician choice》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Patients increasingly ask large language model (LLM) assistants which doctor to see, making these systems AI infomediaries: algorithms that intermediate one person's choice among other people and thereby decide, silently and at scale, which physicians become visible. We report a prespecified randomized algorithm audit of what causally moves those recommendations. Seven models (six open-weight; gpt-4o-mini) each chose among five synthetic family-medicine physician cards whose attributes were independently randomized across 3,024 choice sets, three patient personas, nine prompt paraphrases and nine experimental arms, yielding 40,068 scored responses; gender and ethnicity were signaled through names following correspondence-audit methodology. Reputation signals dominate: raising a rating from 3.9 to 4.7 increases choice probability by 31.4 percentage points (pp), and raising the fee from $90 to $190 lowers it by 20.0 pp. Demographic parity is rejected, but not in the direction human audit studies predict: female-signaled names gain 2.5 pp, and Hispanic-, South-Asian- and Black-signaled names gain 1.3-2.9 pp over White-signaled names, tilts worth $7-$14 per visit in fee-equivalent terms, and a content-free first-listed position is worth $11. Yet models mentioned gender or ethnicity in at most 0.03% of their stated reasons and abstained in 0.39% of trials, so these effects are invisible in the models' own explanations, and transparency obligations relying on model self-report would not detect them. One reasoning model failed the prespecified auditability gate outright. The frozen design makes the audit repeatable: any new model can be assessed against identical stimuli, making recurring behavioural audit, rather than self-reported explanation, the monitoring technology fit for purpose.

</details>

---

### [[20_Research/Papers/大模型/AgentRewind_Recoverable_Execution_for_Long-Horizon_LLM_Agents|AgentRewind: Recoverable Execution for Long-Horizon LLM Agents]]

![[assets/2608.14380_first_page.png|800]]

- **arXiv**: [2608.14380](https://arxiv.org/abs/2608.14380)
- **PDF**: https://arxiv.org/pdf/2608.14380
- **详细分析**: [[20_Research/Papers/大模型/AgentRewind_Recoverable_Execution_for_Long-Horizon_LLM_Agents|AgentRewind: Recoverable Execution for Long-Horizon LLM Agents]]
- **作者**: Yu Zhuang, Kefei Chen, Yitong Duan, Shuxin Zheng, Jian Li, Xu-Yao Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《AgentRewind: Recoverable Execution for Long-Horizon LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MettleBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many real-world tasks require LLM agents to interact with their environments over long execution horizons. Errors that occur early in execution may propagate through both the agent context and environment state, and their effects may be difficult to reverse through subsequent actions. Existing methods mainly seek to reduce such errors through plan refinement and safety checks but provide little support after errors occur. To enable recovery during long-horizon execution, we present AgentRewind, a runtime recovery framework that records aligned checkpoints of the agent context and controlled environment, allowing agents to return to an earlier state and resume execution with information from previous attempts. We also construct MettleBench, a benchmark for evaluating task completion and partial progress on long-horizon engineering assignments containing a series of related requirements. Experiments across tasks, multiple models, execution strategies, and agent harnesses show that AgentRewind improves task success rate and average checklist progress over the compared baselines.

</details>

---

### [[20_Research/Papers/具身智能/Reflex_Enabling_Fast_and_Predictive_Vision-Language-Action_Models_for_Reaction-Critical_Manipulation|Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation]]

![[assets/2608.14379_figure.png|800]]

- **arXiv**: [2608.14379](https://arxiv.org/abs/2608.14379)
- **PDF**: https://arxiv.org/pdf/2608.14379
- **详细分析**: [[20_Research/Papers/具身智能/Reflex_Enabling_Fast_and_Predictive_Vision-Language-Action_Models_for_Reaction-Critical_Manipulation|Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation]]
- **作者**: Yuxuan Chen, Wanruo Zhang, Xiao Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Reflex: Enabling Fast and Predictive Vision-Language-Action Models for Reaction-Critical Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DynamicVLA, Real-World, ReflexBench, ReflexVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have recently achieved promising performance in robotic manipulation. However, existing benchmarks mainly evaluate generalization on static manipulation tasks and largely overlook dynamic interaction scenarios. To address this gap, we present ReflexBench, a benchmark for reaction-critical manipulation. ReflexBench contains six dynamic tasks and introduces an evaluation framework that decouples simulator stepping from robot control while supporting configurable latency under synchronous and asynchronous inference. Building upon ReflexBench, we propose ReflexVLA, an efficient VLA model designed for reaction-critical manipulation without large-scale robot-data pretraining. ReflexVLA enhances temporal reasoning through latent future prediction and multi-frame temporal fusion within the vision backbone, while reducing deployment latency through batched visual encoding and CUDA Graph replay. Experiments show that ReflexVLA consistently improves dynamic manipulation performance while maintaining competitive accuracy on standard static manipulation benchmarks, and real-world experiments further demonstrate its effectiveness under practical deployment conditions. Project website: https://reflexvla.github.io

</details>

---

### [[20_Research/Papers/大模型/Wrong_but_Useful_Trajectory_Value_Beyond_Answer_Correctness_in_Multi-Agent_Messages|Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages]]

![[assets/2608.14375_figure.png|800]]

- **arXiv**: [2608.14375](https://arxiv.org/abs/2608.14375)
- **PDF**: https://arxiv.org/pdf/2608.14375
- **详细分析**: [[20_Research/Papers/大模型/Wrong_but_Useful_Trajectory_Value_Beyond_Answer_Correctness_in_Multi-Agent_Messages|Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages]]
- **作者**: Chih-Hsuan Yang, Anjir Ahmed Chowdhury, Cheng-Hau Yang, Weijian Zheng, Fernando Llorente, Xiaolong Ma, Xinyang Li, Eliu A. Huerta, Ian T. Foster, Rajeev Thakur
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Wrong but Useful: Trajectory Value Beyond Answer Correctness in Multi-Agent Messages》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：JEEBench, LAB-Bench, MaScQA, SciBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent reasoning systems often use agreement, confidence, or automated scores to decide which messages should shape a final answer. Such filtering assumes that a message likely to be correct is also worth keeping. Yet a wrong answer can contain a useful decomposition, constraint, or scientific principle. We test this distinction with Diverse Hypothesis Deliberation (DHD), a controlled measurement protocol that caches five independently generated messages and replays the same downstream solver, called the integrator, with each message available or hidden. The replay comparison measures a message's trajectory value: whether making the message available helps or harms subsequent reasoning. Across five mathematics and science benchmarks and two openly available model families, gpt-oss-120b and gemma-4-31B-it, wrong-helpful messages appear in every benchmark-model combination. Among wrong-answer messages that change final correctness, more than four in ten changes are helpful in each model. Controlled repeats show that the number of repeatable message effects is unlikely to arise from replay variation alone (p=0.0002). A focused intervention on repeatable wrong-helpful messages finds that the complete message works best, while retaining its reasoning preserves more success than retaining only its answer; the source of the complete-message advantage remains open. Within the same problem, repeated trajectory-value evidence also identifies a better keep-or-remove choice than answer correctness alone. Answer correctness is therefore informative but does not determine trajectory value. DHD measures this missing property and produces reusable labels for learning when agents should listen.

</details>

---

### [[20_Research/Papers/大模型/A_Hybrid_LLM-Based_Framework_for_Automated_Security_Annotation_Generation_in_Business_Process_Models|A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models]]

![[assets/2608.14370_figure.png|800]]

- **arXiv**: [2608.14370](https://arxiv.org/abs/2608.14370)
- **PDF**: https://arxiv.org/pdf/2608.14370
- **详细分析**: [[20_Research/Papers/大模型/A_Hybrid_LLM-Based_Framework_for_Automated_Security_Annotation_Generation_in_Business_Process_Models|A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models]]
- **作者**: Md Kamrul Islam, Tiphaine Henry, Mattia Salnitri, Julius Köpke, Sami Souihi
- **cs 子类**: cs.AI, cs.CR, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Security, Systems

#### 研究背景与动机

《A Hybrid LLM-Based Framework for Automated Security Annotation Generation in Business Process Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The modelling and analysis of secure business processes require the incorporation of security annotations into process models. Although BPMN extensions, including SecBPMN2, exist for this purpose, the derivation of accurate and complete security annotations from natural-language specifications remains a manual, expert-intensive, and error-prone task. This paper presents a hybrid framework that takes a BPMN process model and a security requirements document as input and automatically generates security annotations adhering to the SecBPMN2 specification. The approach combines Large Language Model (LLM)--based semantic extraction with schema-constrained mapping, rule-based normalization, and deterministic validation. The framework is evaluated comprehensively on a curated dataset of 27 process models from various domains. The results indicate that it consistently produces structurally valid SecBPMN2 annotations with high schema completeness. Compared to human security analysts, the system achieves substantially higher precision (0.58 vs. 0.29) while maintaining comparable recall (0.52 vs. 0.50) and reduces erroneous or misplaced annotations by nearly 50%. In addition, annotation generation is significantly faster than manual annotation. These findings demonstrate that hybrid LLM- and rule-based automation can reduce modeling effort while improving consistency and reliability, thereby providing a scalable foundation for security-by-design BPM.

</details>

---

### [[20_Research/Papers/大模型/ScienceFlow_A_long-horizon_agent_for_ML_research,_scientific_discovery_and_beyond|ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond]]

![[assets/2608.14354_figure.png|800]]

- **arXiv**: [2608.14354](https://arxiv.org/abs/2608.14354)
- **PDF**: https://arxiv.org/pdf/2608.14354
- **详细分析**: [[20_Research/Papers/大模型/ScienceFlow_A_long-horizon_agent_for_ML_research,_scientific_discovery_and_beyond|ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond]]
- **作者**: Mingming Zhao, Jiqian Dong, Kangping Xu, Zadid Hasan, Chengrui Fan, Shan Jiang, Shuai Mao, Ting Lingya, Linyi Zou, Tailin Zhou, Yun Hin Chan, Wenkai Zhang...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《ScienceFlow: A long-horizon agent for ML research, scientific discovery and beyond》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SciModelingBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enabling LLM agents to sustain productive, stable, and goal-aligned research over extended horizons is a central challenge for autonomous machine learning and scientific discovery, as progress hinges on continuously managing evolving state, exploration decisions, and computational resources. Pioneering autoresearch agents, despite great success, still lack mechanisms for continuity, recovery from dead ends, and value-driven compute allocation, which inherently undermines overall search efficiency, wastes computational resources, and lowers the chance of ultimate success. To bridge this gap, we introduce ScienceFlow, an end-to-end autoresearch agent framework that organizes long-horizon research work into research segments grounded in executable workspaces. It represents research progress as recoverable executable states, enabling efficient exploration, revision, and execution. Transitions between research segments are governed by Executable-State Transition through Re-Anchoring (ESTRA), which selects either the live state or an archived state as the next anchor and determines whether to continue or redirect the research trajectory. An evidence-aware execution controller allocates resources to physical jobs based on resource availability, remaining budget, and validated progress. We evaluate ScienceFlow on tasks spanning machine learning, scientific modeling, and mathematical optimization. Results on diverse long-horizon benchmarks demonstrate its ability to sustain effective research processes, highlighted by a SOTA 70.22 percent Any-Medal score on the full MLE-bench within a 24-hour budget, outperforming prior reported results by 4.92 percentage points. The efficacy of ScienceFlow further demonstrates that efficient state management, adaptive exploration, and objective-aligned execution are critical for scaling autonomous research beyond short-horizon interactions.

</details>

---

### [[20_Research/Papers/大模型/Clearing_the_Fog_Towards_Installing_and_Refining_Proactive_Exploration_Capabilities_in_LLM_Agents|Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents]]

![[assets/2608.14339_figure.png|800]]

- **arXiv**: [2608.14339](https://arxiv.org/abs/2608.14339)
- **PDF**: https://arxiv.org/pdf/2608.14339
- **详细分析**: [[20_Research/Papers/大模型/Clearing_the_Fog_Towards_Installing_and_Refining_Proactive_Exploration_Capabilities_in_LLM_Agents|Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents]]
- **作者**: Zhizhao Guan, Chen Huang, Ziming Liu, Hongru Liang, Wenqiang Lei, See-Kiong Ng, Tat-Seng Chua, Anthony G Cohn
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Clearing the Fog: Towards Installing and Refining Proactive Exploration Capabilities in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SFT-RL, ScienceWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study proactive exploration in LLM agents, i.e., the ability to explore an environment to acquire information that improves future decision-making. In this regard, we first identify two fundamental bottlenecks that hinder this capability and then propose \ours, a novel method designed to instill and refine proactive exploration. Specifically, \ours\ consists of two components: (1) Exploratory Data Construction, which synthesizes exploration-rich trajectories to mitigate the hindsight bias of standard demonstrations; and (2) RL Optimization with Contrastive Signal Guidance, which leverages contrastive trajectory pairs to distinguish productive exploration from redundant wandering. Extensive experiments demonstrate the effectiveness of \ours\ and provide insights into the characteristics of proactive exploration. Our code is available at: https://github.com/GuanZhizhao/SAFARI.

</details>

---

### [[20_Research/Papers/大模型/A_Four-Axis_Trustworthiness_Benchmark_for_LLM-as-Judge_in_Principle-Based_Regulation|A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation]]

![[assets/2608.14329_first_page.png|800]]

- **arXiv**: [2608.14329](https://arxiv.org/abs/2608.14329)
- **PDF**: https://arxiv.org/pdf/2608.14329
- **详细分析**: [[20_Research/Papers/大模型/A_Four-Axis_Trustworthiness_Benchmark_for_LLM-as-Judge_in_Principle-Based_Regulation|A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation]]
- **作者**: Dipankar Sarkar
- **cs 子类**: cs.AI, cs.CL, cs.CR, cs.CY, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《A Four-Axis Trustworthiness Benchmark for LLM-as-Judge in Principle-Based Regulation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Principle-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Principle-based regulation, with evaluative standards such as "fair, clear, and not misleading" or "deliver good outcomes", cannot be reduced to binary predicates, and LLM-as-judge is increasingly used as the substitute. Our position is that any such judge must be evaluated on four axes: accuracy, paraphrase robustness, adversarial robustness, and calibration. We release Principle-Bench, 168 cryptoasset financial-promotion scenarios mapped to two UK FCA principles, with paraphrase, adversarial keyword-stuffing, and boundary perturbations authored under a pre-registered rubric; the first benchmark covering all four axes for principle-based regulation. We also introduce Ceca (Calibrated Exemplar-Cluster Assessment): a calibrated, auditable assessor that emits exact per-exemplar counterfactual attributions. Across keyword counting, three sentence-transformer embedders, an open-weight LLM-judge, and a calibrated cascade, no method dominates all four axes. A 120B LLM-judge, strongest on benign inputs, loses 47 accuracy points (0.74 to 0.27) on keyword-stuffed Consumer Duty inputs: "compliance theatre." A second judge from a different model family agrees only at Cohen's kappa = 0.16 on that split, localising the failure to the model rather than the corpus. Any deployment-grade LLM-judge for principle-based regulation must report per-principle adversarial deception and post-hoc calibration alongside aggregate accuracy.

</details>

---

### [[20_Research/Papers/强化学习/Sensor-Driven_Mission_Synthesis_for_UAV_UGV_Swarms_A_TB-CSPN_Coordination_Architecture_with_Hardware-Enforced_Safety|Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety]]

![[assets/2608.14306_figure.png|800]]

- **arXiv**: [2608.14306](https://arxiv.org/abs/2608.14306)
- **PDF**: https://arxiv.org/pdf/2608.14306
- **详细分析**: [[20_Research/Papers/强化学习/Sensor-Driven_Mission_Synthesis_for_UAV_UGV_Swarms_A_TB-CSPN_Coordination_Architecture_with_Hardware-Enforced_Safety|Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety]]
- **作者**: Uwe M. Borghoff, Paolo Bottoni, Remo Pareschi
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，机器人 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Sensor-Driven Mission Synthesis for UAV/UGV Swarms: A TB-CSPN Coordination Architecture with Hardware-Enforced Safety》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a coordination architecture for heterogeneous UAV/UGV swarms that synthesises mission actions from uncertain, multi-modal sensor evidence while preserving hardware-enforced safety at the actuation boundary. The approach combines radar, RF, acoustic, and visual observations with Topic-Based Communication Space Petri Net (TB-CSPN) orchestration to support incremental mission formation under partial and evolving information. Consultant agents transform sensor outputs into temporally bounded semantic tokens, while supervisor agents provide authorisation and policy-governed release of mission transitions. This separation between interpretation, coordination, and execution yields auditable decision paths, constrains non-determinism within the coordination layer through guards and synchronisation, and enables bounded-time integration of heterogeneous evidence. To improve resilience in contested environments, including cyber compromise, spoofing, jamming, and communication loss, the digital coordination layer is complemented by independent analogue safety envelopes that clamp or veto unsafe actuator commands issued to individual vehicles. A coastal-surveillance case study illustrates how the proposed architecture enables dependable, governed, and physically safe swarm coordination under operational uncertainty.

</details>

---

### [[20_Research/Papers/机器人/Acoustic_UAV_Detection_in_Battlefield_Scenarios_Handling_Noise,_Domain_Shift,_and_Weak_Labels|Acoustic UAV Detection in Battlefield Scenarios: Handling Noise, Domain Shift, and Weak Labels]]

![[assets/2608.14287_figure.png|800]]

- **arXiv**: [2608.14287](https://arxiv.org/abs/2608.14287)
- **PDF**: https://arxiv.org/pdf/2608.14287
- **详细分析**: [[20_Research/Papers/机器人/Acoustic_UAV_Detection_in_Battlefield_Scenarios_Handling_Noise,_Domain_Shift,_and_Weak_Labels|Acoustic UAV Detection in Battlefield Scenarios: Handling Noise, Domain Shift, and Weak Labels]]
- **作者**: Vadym Vilhurin, Volodymyr Sydorskyi, Andrii Shevtsov
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.6（加权：机器人 0.6）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Acoustic UAV Detection in Battlefield Scenarios: Handling Noise, Domain Shift, and Weak Labels》归入 机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EfficientNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Passive acoustic sensing offers a critical, cost-efficient, and, crucially, passive alternative for detecting small unmanned aerial vehicles. However, the practical deployment of acoustic systems is discouraged by extreme environmental noise and sensor-induced domain shift caused by heterogeneous hardware. This paper addresses these challenges by introducing a robust framework optimized for real-world battlefield conditions. We propose the integration of Per-Channel Energy Normalization (PCEN) and attention-based pooling to enhance feature extraction under low signal-to-noise ratio scenarios. We further propose a domain-aware training strategy that leverages auxiliary classes and multi-microphone data to mitigate cross-domain performance degradation. Evaluated on a unique dataset of combat-zone recordings from the Ukrainian frontlines, our approach significantly outperforms existing baselines, increasing the F1 score from 55.4% to 78.6%. This paper was originally presented at the International Conference on Military Communication and Information Systems (ICMCIS), organized by the Information Systems Technology (IST) Scientific and Technical Committee, IST-224-RSY - the ICMCIS, held in Bath, United Kingdom, 12-13 May 2026.

</details>

---

### [[20_Research/Papers/大模型/TimeSage-EV_A_Live_Benchmark_for_Agentic_Time_Series_Analysis_in_Evolving_Environments|TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments]]

![[assets/2608.14270_figure.png|800]]

- **arXiv**: [2608.14270](https://arxiv.org/abs/2608.14270)
- **PDF**: https://arxiv.org/pdf/2608.14270
- **详细分析**: [[20_Research/Papers/大模型/TimeSage-EV_A_Live_Benchmark_for_Agentic_Time_Series_Analysis_in_Evolving_Environments|TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments]]
- **作者**: Qingren Yao, Yaxuan Kong, Yuqi Nie, Yichen Li, Stefan Zohren, Anna Vettoruzzo, Qingsong Wen, Ming Jin, Joaquin Vanschoren
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《TimeSage-EV: A Live Benchmark for Agentic Time Series Analysis in Evolving Environments》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ChatTime-TSQA, ForecastBench, LiveBench, LiveCodeBench, TSRBench, Tau-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Time series analysis in high-stakes domains relies on recurring data releases, where new observations can alter the evidence base and the validity of later conclusions. Existing time series QA benchmarks mostly rely on fixed snapshots, leaving temporal validity and cutoff-aware evidence use unevaluated. We introduce TimeSage-EV, a live benchmark for agentic time series analysis in evolving environments. It tracks 60 real institutional scenarios across 6 domains, comprising 1,485 scenario-period QA pairs from Feb 2023 to May 2026 and spanning monthly, weekly, daily, and irregular release cadences. At each period, large language model (LLM) agents receive time series data and source reports, while the withheld target release provides ground truth. TimeSage-EV evaluates state identification, data summarization, and outlook reasoning. Experiments with frontier LLM agents and TimeSage-1.0, a novel self-evolving agent with a reusable analytical skill library, reveal significant performance gaps across model tiers and recurring failures in temporal validity, exogenous context use, and adaptation. We release TimeSage-EV as a research resource with monthly updates, code, a leaderboard, and failure-mode analyses.

</details>

---

### [[20_Research/Papers/大模型/Grounding_Without_Corrective_Control_Truth-Tracking_Profiles_for_Large_Language_Models|Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models]]

![[assets/2608.14252_first_page.png|800]]

- **arXiv**: [2608.14252](https://arxiv.org/abs/2608.14252)
- **PDF**: https://arxiv.org/pdf/2608.14252
- **详细分析**: [[20_Research/Papers/大模型/Grounding_Without_Corrective_Control_Truth-Tracking_Profiles_for_Large_Language_Models|Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models]]
- **作者**: Brett Reynolds
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.45（加权：大模型 0.45）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Grounding Without Corrective Control: Truth-Tracking Profiles for Large Language Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work suggests that some large language model representations have content or reference. Grounding can secure either without supplying live routes for correction. This paper asks what follows from that gap. An output is answerable when discrepancies can affect what a target- and task-specific arrangement produces, accepts, or withdraws. The arrangement has corrective control only when live, sufficiently independent routes can detect and repair fresh discrepancies. A route profile records which routes constrain the arrangement and how they are related. Those profiles support analysis of truth-tracking: patterned support for representational success. Language models are the pressure case; text-only arrangements provide a task-relative limiting case. Text-trained models inherit patterns of testimony, coherence, and prior correction. Where target-sensitive correction survives training, these can supply derivative answerability (inherited constraint); live answerability is the relation supplied by a current route for fresh discrepancies. Fluent failures should follow when a task requires independently informative access to the facts. Self-consistency, retrieval, tools, code execution, multimodal input, and feedback should help selectively. Route-by-task interactions test the distinctions. The decomposition's empirical burden is to predict held-out route--task combinations or improve intervention choice without conceptual refitting. Surface improvement and truth-tracking improvement can come apart.

</details>

---

### [[20_Research/Papers/大模型/How_Much_Do_Legal_RAG_Systems_Still_Hallucinate|How Much Do Legal RAG Systems Still Hallucinate?]]

![[assets/2608.14210_first_page.png|800]]

- **arXiv**: [2608.14210](https://arxiv.org/abs/2608.14210)
- **PDF**: https://arxiv.org/pdf/2608.14210
- **详细分析**: [[20_Research/Papers/大模型/How_Much_Do_Legal_RAG_Systems_Still_Hallucinate|How Much Do Legal RAG Systems Still Hallucinate?]]
- **作者**: Souvick Das, Sallam Abualhaija, Domenico Bianculli
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: cs.AI

#### 研究背景与动机

《How Much Do Legal RAG Systems Still Hallucinate?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LLeQA, LegalBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hallucination is a major challenge for retrieval-augmented generation (RAG) systems in the legal domain, where ungrounded answers can lead to serious consequences. To better understand this problem, we conduct a fine-grained analysis of hallucination behavior in eight legal RAG systems across two legal corpora, the GDPR (in English) and a national civil law (in French). Using claim-level and answer-level evaluation, we report on hallucination density and severity, analyze performance across question categories and user personas, and validate our findings on an independent set of 142 legal-expert-authored questions. Our results show that hallucinations remain pervasive, ranging from less than 10% of responses for the best-performing systems to nearly half in the worst case. We further find that false-premise questions, containing incorrect assumptions that must be rejected, produce high hallucination rates on the manually-drafted questions.

</details>

---

### [[20_Research/Papers/大模型/Removing_Temporal_Note_Redundancy_Improves_Multimodal_Reinforcement_Learning_for_Medicine|Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine]]

![[assets/2608.14157_figure.png|800]]

- **arXiv**: [2608.14157](https://arxiv.org/abs/2608.14157)
- **PDF**: https://arxiv.org/pdf/2608.14157
- **详细分析**: [[20_Research/Papers/大模型/Removing_Temporal_Note_Redundancy_Improves_Multimodal_Reinforcement_Learning_for_Medicine|Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine]]
- **作者**: Chenran Weng, Joo Seung Lee, Malini Mahendra, Anil Aswani
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.4，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Removing Temporal Note Redundancy Improves Multimodal Reinforcement Learning for Medicine》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mechanical ventilation is a critical life-support intervention, requiring dynamic adjustments to ventilator settings as a patient's condition evolves. While reinforcement learning (RL) offers a promising framework for optimizing these sequential decisions, standard approaches rely primarily on structured electronic health record (EHR) data, missing crucial clinical context recorded in free-text notes. Integrating longitudinal clinical notes into RL state spaces is challenging because notes are heavily inflated by temporal redundancy, such as copy-forward text, templating, and repetitive documentation, which dilutes time-local updates and degrades state representation quality. To address this, we propose a redundancy-aware multimodal state representation framework that explicitly removes duplicated note text over time before policy learning. We evaluate two computationally efficient temporal decomposition strategies for removing duplicated note text: (1) an embedding-space decomposition using singular value decomposition on local history subspaces, and (2) an interpretable sentence-level diff operation that filters out previously documented sentences before text encoding. Using real-world ICU data, we demonstrate that state representations constructed by stripping temporal note redundancy significantly outperform both structured-only and raw-note baselines across multiple off-policy evaluation methods (Model-Based Rollouts, Fitted Q-Evaluation, Weighted Importance Sampling, and Weighted Doubly Robust Evaluation). Our findings show that explicitly isolating new clinical information from repeated note text yields higher-quality state representations and directly improves RL performance for clinical decision support.

</details>

---

### [[20_Research/Papers/大模型/Act2Intention_A_Benchmark_For_Developing_Active_Mobile_Agents_Through_Inferring_User_Intention_from_GUI_Actions|Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions]]

![[assets/2608.14132_figure.png|800]]

- **arXiv**: [2608.14132](https://arxiv.org/abs/2608.14132)
- **PDF**: https://arxiv.org/pdf/2608.14132
- **详细分析**: [[20_Research/Papers/大模型/Act2Intention_A_Benchmark_For_Developing_Active_Mobile_Agents_Through_Inferring_User_Intention_from_GUI_Actions|Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions]]
- **作者**: Xiaokai Yan, Jingtao Ding, Yong Li, Zhiwen Yu
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Act2Intention: A Benchmark For Developing Active Mobile Agents Through Inferring User Intention from GUI Actions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ProAgentBench, ProactiveBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile GUI Agents powered by multimodal large language models (MLLMs) show promise in human-computer intelligence. However, current research primarily focuses on reactive task execution while lacking a comprehensive understanding-prediction-execution process for user intentions, which are the core requirements of active agents. In this paper, we propose the Act2Intention framework that builds an active mobile agent by integrating understanding, predicting user intentions, and executing decisions. First, we construct the Act2Intention Bench through data collection and validated generation, comprising 72,511 intentions and over 700,000 actions across 52 apps, thereby establishing the first benchmark for evaluating proactive agents via continuous intention-action trajectories. We further develop the Act2Intention Agent, achieving proactive services through Proactive-oriented Intention Understanding, Personalized Proactive Intention Prediction, and Experience-guided Intention Execution. Experimental results show that supervised fine-tuning on Act2Intention Bench yields absolute improvements of +32.0 Acc-S, +10.25 Acc-S, and +6.9 SSR points over non-fine-tuned counterparts under the same agent framework for intention understanding, prediction, and execution, respectively. This success underscores the necessity and value of the Act2Intention Bench, which establishes a standardized platform for developing and evaluating proactive agents and consequently paves the way for research on intention-driven human-computer interaction.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning-Based_Production_Scheduling_in_an_Industry-Based_Coating_Scenario_Using_the_Digital_Model_Playground|Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground]]

![[assets/2608.14122_figure.png|800]]

- **arXiv**: [2608.14122](https://arxiv.org/abs/2608.14122)
- **PDF**: https://arxiv.org/pdf/2608.14122
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning-Based_Production_Scheduling_in_an_Industry-Based_Coating_Scenario_Using_the_Digital_Model_Playground|Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground]]
- **作者**: Arne Kröger, Ralf Buschermöhle, Wilhelm Hasselbring, Henrik Wilbers
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，强化学习 1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Reinforcement Learning-Based Production Scheduling in an Industry-Based Coating Scenario Using the Digital Model Playground》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MLTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production scheduling in complex manufacturing environments is challenging when sequence-dependent setup times, stochastic disturbances, and due-date constraints must be addressed simultaneously. While reinforcement learning (RL) methods have shown promising results in research, most studies rely on simplified benchmark processes, limiting their industrial relevance. This paper demonstrates the applicability of RL-based scheduling in an industry-inspired coating process that reflects practical complexities such as sequence-dependent setup times, machine breakdowns, and variable utilization. The open-source Digital Model Playground (DMPG), a discrete event simulation framework, is used to model the scenario and to train RL agents. Two standard algorithms, Deep Q-Networks and Proximal Policy Optimization, are benchmarked against conventional dispatching rules to illustrate feasibility and to provide a transparent testbed for further research. Results indicate that RL-based scheduling achieves balanced improvements across key performance indicators, with PPO delivering the most robust performance. The main contribution of this work is to bridge the gap between academic research and industrial practice by validating RL-based scheduling in a realistic, shareable scenario and by providing a reusable open-source framework for future studies.

</details>

---

### [[20_Research/Papers/大模型/A_Graph-Based_Reinforcement_Learning_Framework_for_Structured_Drift_Diagnosis_and_Recovery_in_Autonomous_LLM_Agents|A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents]]

![[assets/2608.14109_first_page.png|800]]

- **arXiv**: [2608.14109](https://arxiv.org/abs/2608.14109)
- **PDF**: https://arxiv.org/pdf/2608.14109
- **详细分析**: [[20_Research/Papers/大模型/A_Graph-Based_Reinforcement_Learning_Framework_for_Structured_Drift_Diagnosis_and_Recovery_in_Autonomous_LLM_Agents|A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents]]
- **作者**: Ismail El Hamraoui, Sagar Jose, Nicolas Bureau, Robert Plana
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 2.12（加权：大模型 1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《A Graph-Based Reinforcement Learning Framework for Structured Drift Diagnosis and Recovery in Autonomous LLM Agents》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous LLM agents are increasingly deployed in complex real-world workflows, yet they remain vulnerable to runtime behavioral drift, a silent deviation from the original task that can lead to irreversible side effects on external systems. Existing approaches address drift at the prompt level but lack structured mechanisms for step-level detection, risk assessment, and recovery decision. Because the main task-executing agent is often a large and expensive model that cannot be re-trained on every deployment, this work targets a plug-and-play recovery module instead. It introduces a graph-based framework in which a single small language model is trained via reinforcement learning to specialize at each node of a recovery graph, external to the main agent. Each node has a precise role\,: drift classification, operation detection, risk evaluation, or final decision and the model learns to produce structured XML-formatted reasoning adapted to that role. Training combines rule-based structural rewards with an LLM-as-judge semantic-quality signal, so that the model is graded both on how it answers (schema and length) and on what it says. Experiments on the public AppWorld benchmark show that the method generally exploits information about the suspected drift onset to issue correct recovery decisions using a small language model. In addition, the trained small language model reliably respects the prescribed output schema and produces semantically appropriate content in each field according to its assigned node role.

</details>

---

### [[20_Research/Papers/大模型/P2Skill_Privacy_Preserving_Skill_Distillation_for_Cloud-Local_LLM_Inference_Systems|P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems]]

![[assets/2608.14094_figure.png|800]]

- **arXiv**: [2608.14094](https://arxiv.org/abs/2608.14094)
- **PDF**: https://arxiv.org/pdf/2608.14094
- **详细分析**: [[20_Research/Papers/大模型/P2Skill_Privacy_Preserving_Skill_Distillation_for_Cloud-Local_LLM_Inference_Systems|P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems]]
- **作者**: Myunghoon Ryu, Geunpyo Park, Sungjoon Lee, XinYu Piao, Jong-Kook Kim
- **cs 子类**: cs.AI, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Security

#### 研究背景与动机

《P2Skill: Privacy Preserving Skill Distillation for Cloud-Local LLM Inference Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cloud-local LLM inference systems have the potential to use the reasoning capability of large cloud models while protecting sensitive user data on personal devices. Cloud-bound requests must exclude personally identifiable information (PII) to prevent external data leakage. Existing privacy-preserving methods rely on prompt perturbation, entity masking, or model fine-tuning, but these approaches may distort contextual semantics or require additional training. This paper proposes P2Skill, a prompt-based skill distillation method in which a local small language model (SLM) autonomously performs decomposition, PII-aware routing, paraphrasing, and reconstruction by following the skill prompts. Skills are iteratively refined from execution failures by a cloud LLM, enabling the local SLM to generalize beyond memorized PII patterns, and therefore P2Skill requires no privacy-specific fine-tuning or learned auxiliary detectors. Evaluation on a four-domain benchmark shows that P2Skill achieves $1.69\times$ and $3.66\times$ higher privacy-preserved inference quality than previous baselines.

</details>

---

### [[20_Research/Papers/其他/Mandato_Protocol-Level_Enforcement_of_Digitally_Signed_Mandates_on_AI_Agent_Actions_with_Cryptographically_Chained_Audit_Trails|Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails]]

![[assets/2608.14074_first_page.png|800]]

- **arXiv**: [2608.14074](https://arxiv.org/abs/2608.14074)
- **PDF**: https://arxiv.org/pdf/2608.14074
- **详细分析**: [[20_Research/Papers/其他/Mandato_Protocol-Level_Enforcement_of_Digitally_Signed_Mandates_on_AI_Agent_Actions_with_Cryptographically_Chained_Audit_Trails|Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails]]
- **作者**: Giovanni Racioppi
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Mandato: Protocol-Level Enforcement of Digitally Signed Mandates on AI Agent Actions with Cryptographically Chained Audit Trails》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents increasingly act on external systems through standardized tool-calling protocols such as the Model Context Protocol (MCP), yet no infrastructure layer constrains their actions to what a principal has verifiably authorized: authorization logic lives in application code, is neither signed nor independently auditable, and the resulting logs lack evidentiary value. We present Mandato, a governance proxy that enforces digitally signed mandates on agent actions at the protocol level. A mandate is a machine-readable, cryptographically signed authorization artifact specifying which tools an agent may invoke, under which parameter constraints and contextual conditions, for how long, and on whose behalf; the proxy evaluates every tool call against the applicable mandate chain, blocks non-conforming calls in line, and records every decision -- permit, deny, and the evidence for each -- in an append-only, hash-chained audit log designed for evidentiary use and periodically anchored via qualified timestamps. The mandate is deliberately modeled on the civil-law institution of delegation of authority, making the artifact legible to lawyers and auditors, not only to engineers. We give the mandate model and its decision semantics, the reference architecture as an MCP-transparent proxy with separated decision and enforcement points, and a mapping of the mechanism onto EU AI Act Articles 12 and 14, GDPR accountability, NIS2, and eIDAS 2, including a roadmap to qualified attestation through Qualified Trust Service Providers (QTSPs). We describe the implementation status of the reference system and a quantitative evaluation plan covering enforcement overhead, audit completeness, and tamper-evidence verification cost.

</details>

---

### [[20_Research/Papers/大模型/Rethinking_Automated_Program_Repair_The_Impact_of_Bug_Complexity,_Fault_Localization,_and_LLM_Cost-efficiency|Rethinking Automated Program Repair: The Impact of Bug Complexity, Fault Localization, and LLM Cost-efficiency]]

![[assets/2608.14065_figure.png|800]]

- **arXiv**: [2608.14065](https://arxiv.org/abs/2608.14065)
- **PDF**: https://arxiv.org/pdf/2608.14065
- **详细分析**: [[20_Research/Papers/大模型/Rethinking_Automated_Program_Repair_The_Impact_of_Bug_Complexity,_Fault_Localization,_and_LLM_Cost-efficiency|Rethinking Automated Program Repair: The Impact of Bug Complexity, Fault Localization, and LLM Cost-efficiency]]
- **作者**: Junchi Liu, Ali Bigdeli, Roya Daneshi, Atu Ambala, Sudipto Ghosh, Fabio Santos
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《Rethinking Automated Program Repair: The Impact of Bug Complexity, Fault Localization, and LLM Cost-efficiency》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MuBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Background: Software bugs remain a critical challenge in development, necessitating effective Automated Program Repair (APR) techniques. While Large Language Model (LLM)-based APR systems have shown promise, prior studies primarily focus on overall repair effectiveness. The effects of bug complexity, fault localization, reasoning settings, and repair cost-effectiveness remain insufficiently explored. Aims: This study presents a comprehensive empirical analysis of LLM-based APR, focusing on how repair performance is shaped by bug complexity, fault localization, reasoning settings, and costs. Method: We evaluate two APR techniques (ChatRepair and CodeCorrector) using three LLMs (DeepSeek, GPT, and Llama), and examine their performance across diverse levels of bug complexity and localization strategies through a multi-dimensional empirical framework and statistical analysis. Results: Although structurally complex bugs and imprecise fault localization make repair more challenging, LLM-based APR techniques still achieve competitive repair effectiveness. Imprecise fault localization can substantially enlarge the performance gap between APR techniques. Furthermore, higher-cost LLMs and stronger reasoning settings do not consistently yield better cost-efficiency, revealing a nontrivial trade-off between repair effectiveness and computational cost. Conclusions: Over 50% of moderately complex bugs can be repaired by low-cost LLM-based APR techniques. The repair effectiveness gap between APR techniques becomes larger as fault localization becomes less precise. GPT-5 repairs 7 and 39 more complex bugs than DeepSeek-V4-pro and DeepSeek-V3.2, respectively; whereas the total repair cost of DeepSeek-V3.2 shows the best cost-efficiency performance.

</details>

---

### [[20_Research/Papers/具身智能/Evolve_Vision-Language-Action_Model_into_an_Agent_with_On-the-fly_Tool-use|Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use]]

![[assets/2608.14047_figure.png|800]]

- **arXiv**: [2608.14047](https://arxiv.org/abs/2608.14047)
- **PDF**: https://arxiv.org/pdf/2608.14047
- **详细分析**: [[20_Research/Papers/具身智能/Evolve_Vision-Language-Action_Model_into_an_Agent_with_On-the-fly_Tool-use|Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use]]
- **作者**: Yi Ding, Yanzhao Yu, Xili Dai, Xianbiao Qi, Peiwen Sun, Xueqian Wang, Xiangyu Yue, Jianan Wang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.5，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Evolve Vision-Language-Action Model into an Agent with On-the-fly Tool-use》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper integrates end-to-end Visual-Language-Action (VLA) models with agentic tool-use to propose Agentic Robot with Tool-use (ART). ART is a tool-injection framework that tunes any VLA model to leverage off-the-shelf tool modules for low-level vision, high-level affordance, and embodiment enhancement. Compared to vanilla VLA models with a whole continuous action solution space, ART reduces the complexity of the action solution space through tool-use, which not only improves generalizability across different tasks but also reduces data dependency. To demonstrate the advantages (high generalizability and low data dependency) of this framework, we first built a dataset of 30K tool-use trajectories and action demonstrations, which is much smaller than those used by baseline methods. We then designed a training regimen for long-trajectory tool-use reasoning in challenging environments. Experiments show that ART achieves a 20% higher success rate than mainstream baselines on simulation and real-world tasks, such as pick-and-place in the dark at novel viewpoints. Empirical results highlight the benefits of an agent-based approach: modular tool utilization enables more efficient training, lightweight deployment, and scalable integration of new tools. This design fosters robustness, adaptability, and extensibility, paving the way for the practical deployment of VLA systems in complex real-world scenarios.

</details>

---

### [[20_Research/Papers/大模型/Demystifying_Agent_Skills_Why_They_Work-Until_They_Don't|Demystifying Agent Skills: Why They Work-Until They Don't]]

![[assets/2608.14036_figure.png|800]]

- **arXiv**: [2608.14036](https://arxiv.org/abs/2608.14036)
- **PDF**: https://arxiv.org/pdf/2608.14036
- **详细分析**: [[20_Research/Papers/大模型/Demystifying_Agent_Skills_Why_They_Work-Until_They_Don't|Demystifying Agent Skills: Why They Work-Until They Don't]]
- **作者**: Zhiyuan Jiang, Fangrui Huang, Hanwen Xing, Xander Wu, Yipeng Gao, Rui Cao, Mengdi Wang, Shilong Liu, Yijiang Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Demystifying Agent Skills: Why They Work-Until They Don't》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SWE-Skills-Bench, SkillsBench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skills have emerged as a practical and effective approach for enhancing LLM agents at inference time through structured packages of knowledge. However, existing evaluations largely measure whether skills improve aggregated task success, leaving a more fundamental question underexplored: \emph{\textbf{When do skills help, why do they work, and where do they fail?}} Through controlled experiments across various benchmarks, agent harnesses and LLMs, we isolate the effects of representation, outcome annotation, retrieval difficulty, and cross-framework robustness of skills. To further answer this question, we design a contrastive study that combines controlled quantitative experiments with paired trajectory analysis. We normalize 8,135 trial records from controlled experiments and retain 238 valid unique labels from 240 open-coded records. We consolidate these observations into a taxonomy of three high-level categories and twelve skill-use modes: skills work when noisy trajectories become procedural anchors that stabilize execution. Skills improve over Workflow Memory by 6.06 points in matched comparisons. Procedural anchoring accounts for 65.7\% of skill cases, versus 4.5\% for explicit knowledge injection, showing that skills stabilize action rather than inject missing facts. Retrieval is a separate bottleneck: as pools grow from 5 to 100, actual-use precision falls from 29.6\% to 3.3\%. Confusable distractors impair offline identification, yet downstream success remains stable; exact ground-truth invocation is neither sufficient nor necessary. Skills fail under brittle assumptions, incompatible contexts, or insufficient adaptation. These findings move evaluation beyond aggregate success rates and guide reliable self-evolving agents.

</details>

---

### [[20_Research/Papers/大模型/HAM-RAG_Hierarchy-Aware_Multimodal_RAG_for_Structure-Faithful_Interleaved_Generation|HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation]]

![[assets/2608.14032_first_page.png|800]]

- **arXiv**: [2608.14032](https://arxiv.org/abs/2608.14032)
- **PDF**: https://arxiv.org/pdf/2608.14032
- **详细分析**: [[20_Research/Papers/大模型/HAM-RAG_Hierarchy-Aware_Multimodal_RAG_for_Structure-Faithful_Interleaved_Generation|HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation]]
- **作者**: Yin Li, Ziyang Hu, Zhiyu Guo, Xiangyu Liu, Wenbin Li, Boo-Ho Yang, Rav Lawana, Ziyue Li, Wei Zeng, Fugee Tsung
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《HAM-RAG: Hierarchy-Aware Multimodal RAG for Structure-Faithful Interleaved Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HAM-Bench, M3DocVQA, MMCoQA, MRAMG-Bench, WebQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing multimodal RAG methods often flatten structured documents into isolated text and image units, weakening the source organization and local text-image logic needed for faithful evidence selection and placement. We propose HAM-RAG, a Hierarchy-Aware Multimodal RAG framework for structure-faithful interleaved generation. HAM-RAG uses document hierarchy as a grounding signal across retrieval and generation, contextualizing textual and visual evidence and preserving source position and local text-image relations in the prompt. We further introduce HAM-Bench, covering Wukong, Wiki, arXiv, and Recipe across game walkthroughs, web pages, scientific papers, and step-wise recipe documents. Across multiple backbones, HAM-RAG improves the main multimodal average by 17.3% over the strongest non-hierarchical baseline. On Wukong, HAM-RAG improves Img-CBS by 24.2% over the strongest non-hierarchical baseline, demonstrating substantially better local text-image alignment. The main experiments and ablation study together demonstrate that document hierarchy is a key grounding signal for faithful image selection, placement, and local text-image alignment. These findings highlight the value of hierarchy-aware grounding for reliable multimodal assistants that generate answers faithful to the source organization, procedural structure, and local text-image evidence of structured documents, such as technical manuals, maintenance guides, and industrial SOPs. The code is available at https://github.com/MCCodeAI/HAM-RAG.git.

</details>

---

### [[20_Research/Papers/具身智能/AdvDex_Learning_Dexterous_Manipulation_from_Human_Demonstrations_via_Joint-Aligned_Actions_and_Adversarial_Learning|AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning]]

![[assets/2608.14028_figure.png|800]]

- **arXiv**: [2608.14028](https://arxiv.org/abs/2608.14028)
- **PDF**: https://arxiv.org/pdf/2608.14028
- **详细分析**: [[20_Research/Papers/具身智能/AdvDex_Learning_Dexterous_Manipulation_from_Human_Demonstrations_via_Joint-Aligned_Actions_and_Adversarial_Learning|AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning]]
- **作者**: Zhiyue Zhao, Jingyi Wu, Hairuo Liu, Mingyu Liu, Liyang Li, Hengdi Zhang, Tong He, Zhengxue Cheng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《AdvDex: Learning Dexterous Manipulation from Human Demonstrations via Joint-Aligned Actions and Adversarial Learning》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation is a fundamental capability for embodied intelligence, but scaling it remains difficult because robot demonstrations are expensive to collect and action spaces vary across embodiments. Policies trained on heterogeneous data can also entangle task-relevant visual cues with embodiment-specific appearance, limiting cross-embodiment generalization. We present AdvDex, a unified Vision-Language-Action framework for learning dexterous manipulation from human and robot demonstrations. First, we introduce OmniShare, a large-scale multimodal dataset of human manipulation demonstrations that provides high-quality kinematic supervision and tactile measurements while reducing reliance on robot teleoperation. Second, we propose the Joint-Aligned Action Space (JAAS), a canonical action representation comprising an $\mathrm{SE}(3)$ wrist pose and 15 finger joints, thereby functionally aligning human hands, dexterous robot hands, and parallel grippers. Finally, we use domain-adversarial learning to reduce embodiment-specific information in the learned visual representation. Experiments on hand-action prediction and real-world dexterous manipulation show consistent improvements over baselines, effective zero-shot human-to-robot skill transfer, generalization to unseen objects and environments, and data-efficient few-shot adaptation.

</details>

---

### [[20_Research/Papers/强化学习/ForgeWM_Progressive_Causal_Training_for_Few-Step_Action-Conditioned_Video_World_Models|ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models]]

![[assets/2608.14022_figure.png|800]]

- **arXiv**: [2608.14022](https://arxiv.org/abs/2608.14022)
- **PDF**: https://arxiv.org/pdf/2608.14022
- **详细分析**: [[20_Research/Papers/强化学习/ForgeWM_Progressive_Causal_Training_for_Few-Step_Action-Conditioned_Video_World_Models|ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models]]
- **作者**: Xinye Li, Lingshuai Lin, Lei Wang, Liuzhou Zhang, Jialin Cui, Qingshan Li, Guanchu Wang, Qingbin Liu, Xi Chen, Jiang Bian, Wai Lam
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《ForgeWM: Progressive Causal Training for Few-Step Action-Conditioned Video World Models》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DreamX-World, LingBot-World, MineWorld, VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video world models require low-latency causal generation and reliable responses to game-native controls. Although causal distillation enables one- or few-step video synthesis, extending it to interactive world models remains challenging, as discrete keyboard states and continuous mouse motion must remain aligned with temporally compressed latent chunks during causal training and autoregressive rollout. We introduce ForgeWM, a progressive framework that transforms a bidirectional action-conditioned video generator into efficient few-step world models through domain adaptation, teacher-forced causal training, causal consistency distillation, and on-policy distribution matching with a bidirectional teacher. The resulting budget-specialized students operate at steady-state denoising budgets of 1, 2, and 4 steps. ForgeWM further supports a dual-path deployment protocol combining latency-critical interaction with optional replay-time refinement, where the one-step student re-noises and refines its saved draft. On paired Minecraft trajectories, ForgeWM leads the evaluated systems in Imaging Quality, reference-aligned motion-profile agreement, action-sign accuracy, and mouse-control accuracy, while achieving the lowest reference LPIPS; the same four-stage recipe transfers to gamepad-controlled FPS gameplay. Replay-time refinement matches four-step reference quality while remaining roughly three times closer to the experienced trajectory than regeneration from noise. These results demonstrate ForgeWM's effectiveness for controllable few-step video generation.

</details>

---

### [[20_Research/Papers/大模型/MedClaw_Heuristic_Agent_Harness_for_Long-Horizon_Surgical_Video_Reasoning|MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning]]

![[assets/2608.14015_figure.png|800]]

- **arXiv**: [2608.14015](https://arxiv.org/abs/2608.14015)
- **PDF**: https://arxiv.org/pdf/2608.14015
- **详细分析**: [[20_Research/Papers/大模型/MedClaw_Heuristic_Agent_Harness_for_Long-Horizon_Surgical_Video_Reasoning|MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning]]
- **作者**: Yingying Fan, Penghui Du, Leyan Zhu, Runze He, Zimeng Wu, Yuxuan Zhang, Liang Chen, Jiahao Xie, Jiangtang Wang, Shuai Shao, Anchao Yang, Yutong Bai...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MedClawBench, SurgBench, SurgViVQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding tens-of-minutes surgical videos requires long-horizon temporal reasoning, answering what happens before, after, or across stages of a procedure by grounding the question in visual evidence spread across time. Existing approaches handle this poorly: a one-shot vision-language model (VLM) compresses the whole procedure to fit its context window and loses the detail a "before" or "after" question depends on, while video agents that train the model where to look are data-hungry and transfer poorly to out-of-domain surgery. We build an agent harness that separates reasoning from perception and improves by evolving context rather than optimizing weights. A text-only orchestrator plans which evidence to gather and issues an auditable sequence of tool calls, while frozen vision-language sub-agents execute each call over the pixels, viewing, cropping, inspecting frames, and retrieving external knowledge. We further propose a gradient-free, reward-gated Heuristic Skill Distillation loop that mines the agent's own low-scoring traces and keeps a candidate skill only when it raises a validation reward, yielding reusable retrieval skills, notably directed re-look. Growing an external skill library rather than tuning weights, the loop adapts from only about 100 labeled examples, far fewer than supervised or reinforcement fine-tuning requires. To evaluate this agent, we introduce MedClawBench, a de-leaked, doctor-grounded benchmark of 1,123 questions over self-built long neurosurgery recordings and a held-out public lecture-video test split. Across both datasets and all four evaluation dimensions, our agent consistently outperforms one-shot VLMs and general video-agent frameworks, with the largest gains on the long, out-of-domain neurosurgery videos. Project page: https://fyycs.github.io/medclaw/.

</details>

---

### [[20_Research/Papers/大模型/When_Personal_Memory_Has_No_Single_Answer_Evaluating_LLM_Agents_under_Irreducible_Conflict|When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict]]

![[assets/2608.13921_figure.png|800]]

- **arXiv**: [2608.13921](https://arxiv.org/abs/2608.13921)
- **PDF**: https://arxiv.org/pdf/2608.13921
- **详细分析**: [[20_Research/Papers/大模型/When_Personal_Memory_Has_No_Single_Answer_Evaluating_LLM_Agents_under_Irreducible_Conflict|When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict]]
- **作者**: Lu Yang, Shusheng Xu, Zhuoran Li, Tongkai Yang, Longbo Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《When Personal Memory Has No Single Answer: Evaluating LLM Agents under Irreducible Conflict》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CONFLICTINGQA, SelectiveQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly maintain personal memory across sessions, but it can conflict. Preferences depend on context, behavior evolves, and sources can conflict. When a query lacks context, time, or source authority to interpret conflict, treating one memory as definitive converts unresolved conflict into an unjustified, overconfident action. Existing benchmarks recover one answer from conflicting evidence, overlooking whether agents recognize underdetermination, preserve alternatives, seek missing information, and choose appropriate actions. We introduce \underline{T}esting \underline{A}gents' \underline{N}avigation of \underline{G}enuine, \underline{L}atent, and \underline{E}ntangled Memory Conflicts (\textsc{TANGLE}), a benchmark for genuinely unresolvable memory conflicts. It comprises 541 instances across 40 personas and three types: Context-Partitioned Conflict (CPC), Behavior-Oscillation Conflict (BOC), and Source-Contradiction Conflict (SCC). We evaluate two tracks---an oracle track with curated memory and a pipeline track that extracts memory from multi-session dialogues---on five dimensions: conflict perception, causal reasoning, confidence calibration, clarification seeking, and memory faithfulness. Experiments reveal pipeline challenges. With curated memory, models recognize conflicts more reliably than they calibrate actions or seek targeted clarification. With end-to-end pipeline memory, extraction fails to preserve conflict-bearing relations needed for downstream reasoning. Policy comparisons show fixed rules are insufficient when actions must reflect conflict. These findings motivate Conflict-Aware Action Policy (CAAP), which adapts actions to each conflict using available evidence. \textsc{TANGLE} frames conflict handling as recognizing underdetermination, retaining conflicting evidence, and acting without forcing a definitive answer.

</details>

---

### [[20_Research/Papers/大模型/Agentic_Transaction_Towards_ACID-Compliant_Agent_Systems|Agentic Transaction: Towards ACID-Compliant Agent Systems]]

![[assets/2608.13900_figure.png|800]]

- **arXiv**: [2608.13900](https://arxiv.org/abs/2608.13900)
- **PDF**: https://arxiv.org/pdf/2608.13900
- **详细分析**: [[20_Research/Papers/大模型/Agentic_Transaction_Towards_ACID-Compliant_Agent_Systems|Agentic Transaction: Towards ACID-Compliant Agent Systems]]
- **作者**: Zhaoyan Sun, Xiaoxiao Wang, Guoliang Li
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Agentic Transaction: Towards ACID-Compliant Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgenticDataBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are evolving from conversational assistants into autonomous systems that execute long-horizon tasks through reasoning, tool use, code generation, and workspace manipulation. As agents increasingly operate over persistent environments and multi-step workflows, they face challenges analogous to those addressed by transactional database systems: reliable execution, consistent outcomes, safe concurrency, and durable state management. We introduce the concept of an agentic transaction and propose an ACID-compliant agent system framework that reinterprets the classical ACID properties for agent execution through four semantic guarantees: Semantic Atomicity, Semantic Consistency, Semantic Isolation, and Semantic Durability. Together, these properties provide a principled foundation for building reliable agent systems despite model uncertainty and dynamic execution environments. To instantiate this framework, we develop an ACID-compliant data agent that realizes these guarantees through transactional exploration-execution-validation cycles, transactional skill hubs, confidence divergence-based validation, semantic dependency-aware isolation, and transaction-aware semantic state management. Experimental results on widely used benchmarks show that our system achieves a 10.6% improvement over state-of-the-art agents, including Claude Code. This work opens a broader research agenda on extending transactional principles and system architectures toward building trustworthy, scalable, and self-evolving AI agent systems.

</details>

---

### [[20_Research/Papers/大模型/MemoryLake_on_MemoryArena_A_Matched_Study_of_Agent_Memory_Backends|MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends]]

![[assets/2608.13883_first_page.png|800]]

- **arXiv**: [2608.13883](https://arxiv.org/abs/2608.13883)
- **PDF**: https://arxiv.org/pdf/2608.13883
- **详细分析**: [[20_Research/Papers/大模型/MemoryLake_on_MemoryArena_A_Matched_Study_of_Agent_Memory_Backends|MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends]]
- **作者**: Chaoqun Zhan, Qiang Zhou, Guannan Li, Zhenqiang Huang, Qianjin Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《MemoryLake on MemoryArena: A Matched Study of Agent Memory Backends》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval, MemoryAgentBench, MemoryBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most agent-memory benchmarks test post-hoc recall, whereas MemoryArena evaluates whether memory supports interdependent, multi-session task completion. We compare MemoryLake, a structured multi-track memory backend, with Mem0, text-embedding-3-small vector RAG, and a long-context control across all five MemoryArena domains. The systems share the same agent framework, requested gpt-5-mini model alias, task samples, and scoring code; the memory integration is the intentionally changed component. Because each backend bundles write, retrieval, consolidation, budgeting, and prompt-assembly choices, the study is a matched system-level comparison, not a representation-only ablation or a cost-matched experiment. On the shared evaluation sets, MemoryLake has the highest observed success rate (SR) in mathematics (9/40), physics (12/20), and progressive retrieval (4/20). Every system has zero SR in travel planning, and web shopping yields a single bundle-level success (long context, 1/150); MemoryLake ranks third on both the travel soft process score and shopping step match. Following MemoryArena's suite-level convention, a post-hoc equal-weight average over the five SRs is 20.5% for MemoryLake versus 13.6% for the best comparator. These are point estimates: sample sizes are modest, confidence intervals overlap, and we do not report paired significance tests. A separate MemoryLake-only run over all 221 progressive queries yields a failure-counted SR of 26.7% (59/221) and is not a baseline comparison. The results support a workload-dependent view of memory backends and an observed lead among the four evaluated systems on the shared sets; they do not establish benchmark-wide state of the art or a causal advantage of representation structure.

</details>

---

### [[20_Research/Papers/其他/Engineering_Reliable_Coding_Agents_Evaluating_and_Operating_the_System_Around_the_Model|Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model]]

![[assets/2608.13867_first_page.png|800]]

- **arXiv**: [2608.13867](https://arxiv.org/abs/2608.13867)
- **PDF**: https://arxiv.org/pdf/2608.13867
- **详细分析**: [[20_Research/Papers/其他/Engineering_Reliable_Coding_Agents_Evaluating_and_Operating_the_System_Around_the_Model|Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model]]
- **作者**: Stephanie Jarmak
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Engineering Reliable Coding Agents: Evaluating and Operating the System Around the Model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI coding agents are commonly evaluated as models but deployed as systems. Their reliability depends not only on model capability, but on the harness, execution state, retrieval, memory and state management, permissions, review interfaces, and resource allocation. This monograph examines those boundaries and develops a framework for evaluating and operating coding agents reliably. It synthesizes 164 scholarly works, 100 practitioner records, 29 benchmark records, and 17 author-system case records through a structured multivocal review, targeted update audits, software-engineering coverage analysis, and distributed-systems evidence synthesis. Across this evidence, many apparent model failures originate elsewhere in the system, while improvements at one layer often fail to propagate to end-to-end outcomes. Evaluation and operation are treated as a dependency chain in which weaknesses in task construction, execution environments, retrieval, state management, verification, or observability can invalidate downstream conclusions. The monograph contributes a versioned catalog of 206 reliability records: 193 gated practices, including 56 developed in depth, plus 13 research leads; an evidence ledger; a framework for dependency and repair asymmetry across the agent lifecycle; measurements and failure cases from operated agent systems; runnable evaluation and reliability protocols; and five reusable agent skills with evidence maps. Together, these provide a system-level methodology for distinguishing model capability from infrastructure effects, designing defensible evaluations, and building systems that recover safely when components fail. The review is structured rather than exhaustive, evidence strength varies by topic, and results depend on workload and configuration. The methods record which search lanes were executed, which remain unexecuted, and limits on evidence-grading claims.

</details>

---

### [[20_Research/Papers/强化学习/AdsWorldEngine_A_Self-Evolving_Conversational_Advertising_Agent_through_Orchestrator_and_Tool_Coevolution|AdsWorldEngine: A Self-Evolving Conversational Advertising Agent through Orchestrator and Tool Coevolution]]

![[assets/2608.13833_figure.png|800]]

- **arXiv**: [2608.13833](https://arxiv.org/abs/2608.13833)
- **PDF**: https://arxiv.org/pdf/2608.13833
- **详细分析**: [[20_Research/Papers/强化学习/AdsWorldEngine_A_Self-Evolving_Conversational_Advertising_Agent_through_Orchestrator_and_Tool_Coevolution|AdsWorldEngine: A Self-Evolving Conversational Advertising Agent through Orchestrator and Tool Coevolution]]
- **作者**: Simiao Zuo, Chenhui Xu, Yimeng Jia, Qiang Lou, Jian Jiao, Denis Charles
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.5（加权：大模型 0.3，强化学习 0.2）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《AdsWorldEngine: A Self-Evolving Conversational Advertising Agent through Orchestrator and Tool Coevolution》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conversational advertising aims to deliver useful ads within multi-turn assistant interactions. Unlike conventional query-based advertising, where the user's intent is often expressed in a short standalone query, conversational ads must infer latent commercial intent from the current user query, the assistant response, and dialogue history while also deciding whether an ad would be helpful rather than intrusive. We propose AdsWorldEngine, an agentic framework for conversational advertising. AdsWorldEngine uses an Opportunity Gate to determine whether ads should be shown, an Orchestrator to generate commercial intents, call advertising tools, and construct a top-3 ad slate, and an Evaluator to score delivered ads for offline optimization. The central contribution is an iterative actor-tool training procedure: we first train the Orchestrator with supervised fine-tuning and agentic reinforcement learning, then use high- and low-reward rollouts to construct preference data to train tools. This creates a self-improving loop in which the system learns not only how to use advertising tools, but also how to improve them from rewarded behavior. To support subjective production decisions, we introduce label grounded judgment modeling, which trains judgment models from human labels collected under explicit guidelines. It enriches labels with thinking traces, filters inconsistent rationales through reflection, and further optimizes binary judgments with a cost sensitive GRPO variant that preserves asymmetric reward gaps. Offline, AdsWorldEngine improves diversity by 60% and relevance by 80% over the current production ad delivery system. In an online A/B test, it increases RPM by 22% and ads coverage by 74%.

</details>

---

### [[20_Research/Papers/大模型/Simulation-Aware_In-Context_Policy_Improvement_for_LLM-Aided_Analog_Layout_Refinement|Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement]]

![[assets/2608.13767_figure.png|800]]

- **arXiv**: [2608.13767](https://arxiv.org/abs/2608.13767)
- **PDF**: https://arxiv.org/pdf/2608.13767
- **详细分析**: [[20_Research/Papers/大模型/Simulation-Aware_In-Context_Policy_Improvement_for_LLM-Aided_Analog_Layout_Refinement|Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement]]
- **作者**: Bingyang Liu, Ziming Wei, Xiaohan Gao, David Z. Pan
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Simulation-Aware In-Context Policy Improvement for LLM-Aided Analog Layout Refinement》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Analog IC layout design remains a labor-intensive iterative process dominated by simulation-driven refinement. Although end-to-end layout generators accelerate initial placement and routing, they still require experts to manually tune layout optimization parameters with repeated post-layout simulations for stringent design specifications. While Bayesian Optimization (BO) is widely adopted for parameter tuning in analog IC design, at the layout level it typically requires hundreds to thousands of evaluations, each involving costly parasitic extraction and post-layout simulation, which makes it impractical. Recently, Large Language Models (LLMs) have demonstrated potential in improving the sample efficiency of such simulation-driven tuning. However, their restricted access to geometric layout context and design-specific heuristics limits their ability to manipulate the layout optimization process. In this paper, we propose a simulation-aware LLM multi-agent framework that performs in-context policy improvement (ICPI) by iteratively updating layout optimization parameters exposed by an analog layout generator through an act-observe-reflect loop on compact structured layout representations. Experiments on real-world analog circuits show that, with only tens of post-layout simulations, our approach improves post-layout performance over the generator's built-in heuristics and BO-based tuning method.

</details>

---

### [[20_Research/Papers/机器人/Coverage_Aware_Active_Evaluation_for_Failure_Discovery_with_Paired_Systems|Coverage Aware Active Evaluation for Failure Discovery with Paired Systems]]

![[assets/2608.13719_figure.png|800]]

- **arXiv**: [2608.13719](https://arxiv.org/abs/2608.13719)
- **PDF**: https://arxiv.org/pdf/2608.13719
- **详细分析**: [[20_Research/Papers/机器人/Coverage_Aware_Active_Evaluation_for_Failure_Discovery_with_Paired_Systems|Coverage Aware Active Evaluation for Failure Discovery with Paired Systems]]
- **作者**: Anjali Parashar, Rachel Luo, Apoorva Sharma, Sushant Veer, Edward Schmerling, Carson Sobolewski, Mingxin Yu, Chuchu Fan, Marco Pavone
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Coverage Aware Active Evaluation for Failure Discovery with Paired Systems》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous systems can fail in rare and heterogeneous ways, making real-world failure discovery difficult under limited testing budgets. Although cheaper proxies such as simulators, lower-fidelity systems, or related policies can be sampled extensively to find failures, proxy failures often do not transfer to the real world due to sim-to-real and system-to-system gaps. The key challenge is therefore to effectively leverage proxy system information for accurate prediction of severe target system failures. We propose an adaptive failure discovery method that combines proxy evaluations with limited target system results to guide scenario selection for target system testing. Our method learns a local predictor of target risk by correcting proxy failure signals using control-variate-inspired residual modeling. To find failures that are both likely and diverse, we combine this predictor with a support-aware mutual-information objective that favors realistic, well-supported regions while expanding coverage across failure modes. Across autonomous driving, manipulation, and quadruped velocity-tracking tasks, our method discovers up to 2$\times$ as many failures as random sampling and active-learning baselines, including severe and diverse failures missed by competing methods.

</details>

---

### [[20_Research/Papers/大模型/TeachMateGPT_A_Multi-Agent_Knowledge-Grounded_Framework_for_Pedagogical_Assessment_Generation_from_Science_Curriculum_Materials|TeachMateGPT: A Multi-Agent Knowledge-Grounded Framework for Pedagogical Assessment Generation from Science Curriculum Materials]]

![[assets/2608.13708_figure.png|800]]

- **arXiv**: [2608.13708](https://arxiv.org/abs/2608.13708)
- **PDF**: https://arxiv.org/pdf/2608.13708
- **详细分析**: [[20_Research/Papers/大模型/TeachMateGPT_A_Multi-Agent_Knowledge-Grounded_Framework_for_Pedagogical_Assessment_Generation_from_Science_Curriculum_Materials|TeachMateGPT: A Multi-Agent Knowledge-Grounded Framework for Pedagogical Assessment Generation from Science Curriculum Materials]]
- **作者**: Fatema Tuj Johora Faria, Mukaffi Bin Moin, M. F. Mridha, Jubayer Al Mahmud
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《TeachMateGPT: A Multi-Agent Knowledge-Grounded Framework for Pedagogical Assessment Generation from Science Curriculum Materials》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NCTB-QA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatically generating textbook-grounded assessment items can reduce science teachers' workload, but existing retrieval-augmented generation (RAG) systems rely on flat retrieval, support only single-question generation, lack safeguards against weak evidence, and are ill-suited to low-resource, board-exam-structured curricula. We address these limitations with TeachMateGPT, a multi-agent system contributing four advances to curriculum-grounded science-assessment authoring. (i) COPE, a hierarchical knowledge base replacing token-window chunking with a multi-resolution index that segments documents along syllabus structure and links them at three granularities via a traversable graph-based lineage, matching evidence to each topic's instructional level. (ii) A staged, fail-closed agent pipeline replacing one-shot retrieve-then-generate: routing gates search, retrieval fuses dense and lexical evidence under a coverage gate that withholds generation on insufficient evidence, and specialist agents draft objective and constructed-response items. (iii) SAVER, a source-attributed verification protocol scoring faithfulness, relevance, and hallucination risk against retrieved evidence, applying stricter grounding checks across each creative question's four sub-parts, paired with teacher-in-the-loop evaluation rather than automatic filtering. (iv) NCTB-SciGen8, a curriculum-grounded dataset of 198 items (143 multiple-choice, 55 creative questions) spanning all 14 chapters of the NCTB Class 8 science textbook, produced by the pipeline and rated by three practicing teachers. TeachMateGPT raises faithfulness (0.68 $\rightarrow$ 0.96) and answer relevancy (0.60 $\rightarrow$ 0.89) over a vanilla RAG baseline.

</details>

---

### [[20_Research/Papers/大模型/CLAIR-Fin_An_Adversarial_Multi-Agent_Framework_for_Claim-Level_Verification_and_Adaptive_Debate_in_Cross-Modal_Financial_QA|CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA]]

![[assets/2608.13706_figure.png|800]]

- **arXiv**: [2608.13706](https://arxiv.org/abs/2608.13706)
- **PDF**: https://arxiv.org/pdf/2608.13706
- **详细分析**: [[20_Research/Papers/大模型/CLAIR-Fin_An_Adversarial_Multi-Agent_Framework_for_Claim-Level_Verification_and_Adaptive_Debate_in_Cross-Modal_Financial_QA|CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA]]
- **作者**: Fatema Tuj Johora Faria, Mukaffi Bin Moin, Jubayer Al Mahmud, M. F. Mridha, Md. Alam Hossain
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.75（加权：大模型 0.75）
- **关联关键词**: Agent, Security

#### 研究背景与动机

《CLAIR-Fin: An Adversarial Multi-Agent Framework for Claim-Level Verification and Adaptive Debate in Cross-Modal Financial QA》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BB-FinQA, FinRAGBench, FinanceBench, XFinBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing defenses against hallucination in retrieval-augmented and multi-agent pipelines remain partial: evidence is trusted despite modality disagreement, debate verifies an aggregate report rather than individual claims, and such verification occurs only after drafting, leaving inter-agent errors undetected until the final text. To close this gap, we present CLAIR-Fin, a nine-agent framework that decomposes each question into atomic claims maintained in a typed Financial Claim Ledger. Each claim is resolved through Asymmetric Evidence Authority, which conditions evidence trust on claim type rather than treating all modalities as equally reliable; Chain-of-Custody Verification, which checks grounding at the hand-off between drafting and adversarial review rather than only at the pipeline's exit; an Adaptive Rebuttal Cycle, which routes contested claims through adversarial debate whose depth scales with what that debate finds; and a terminal entailment audit paired with a continuous Hallucination Risk Index that distinguishes claims that passed scrutiny from claims never contested. We evaluate CLAIR-Fin on BB-FinQA-X, a 500-question cross-modal financial evaluation set built from Bangladesh Bank Annual Report material, stratified by query type, format, and difficulty. Relative to a single-pass retrieval-augmented generation baseline, it raises faithfulness ($0.780 \rightarrow 0.889$) while abstaining on 5.4% of questions when evidence is insufficient rather than forcing an unsupported response, and it exceeds stronger retrieval-strategy baselines such as HyDE and Graph-RAG on faithfulness ($\leq 0.874$).

</details>

---

### [[20_Research/Papers/大模型/Second_Thought_Reasoning_in_Parallel_as_LLM_Agents_Act_and_Observe|Second Thought: Reasoning in Parallel as LLM Agents Act and Observe]]

![[assets/2608.13667_figure.png|800]]

- **arXiv**: [2608.13667](https://arxiv.org/abs/2608.13667)
- **PDF**: https://arxiv.org/pdf/2608.13667
- **详细分析**: [[20_Research/Papers/大模型/Second_Thought_Reasoning_in_Parallel_as_LLM_Agents_Act_and_Observe|Second Thought: Reasoning in Parallel as LLM Agents Act and Observe]]
- **作者**: Zhensu Sun, Chengran Yang, Yunbo Lyu, Jieke Shi, David Lo
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Second Thought: Reasoning in Parallel as LLM Agents Act and Observe》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SWE-Bench, Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents in the ReAct paradigm alternate between reasoning, acting, and observing, but deliberate reasoning is confined to the Thought phase: while the agent serializes an action and waits for the environment, its reasoning is frozen. We identify this recurring interval for Action and Observation as a reasoning idle window and ask whether it can host additional reasoning in parallel that serves future turns. Therefore, we propose Second Thought, a training-free inference framework that forks four auxiliary branches the instant each Thought phase concludes, decodes them concurrently with the main loop, and merges the generated thoughts back when the environment observation arrives. In this way, Second Thought relocates the added reasoning off the main thread's sequential decoding path. Across three agentic benchmarks and three reasoning LLMs, Second Thought lowers the average turn count in all nine (model,benchmark) pairs and reduces main thread decoding in six of them by up to 43% (roughly 20% on average among those settings), while leaving it essentially unchanged in a seventh; Pass@1 shows no significant change in seven of nine pairs and the two significant differences are +12.4 and +10.2 points. Against a compute-matched control that forces an equivalent budget onto the main thread's own reasoning, it attains strictly higher Pass@1 with 1.3 to 3.2 less sequential decoding in all four settings where the control applies.

</details>

---

### [[20_Research/Papers/强化学习/Reward_Machines_for_Signal_Temporal_Logic|Reward Machines for Signal Temporal Logic]]

![[assets/2608.13625_figure.jpg|800]]

- **arXiv**: [2608.13625](https://arxiv.org/abs/2608.13625)
- **PDF**: https://arxiv.org/pdf/2608.13625
- **详细分析**: [[20_Research/Papers/强化学习/Reward_Machines_for_Signal_Temporal_Logic|Reward Machines for Signal Temporal Logic]]
- **作者**: Alper Kamil Bozkurt, Shangtong Zhang, Yuichi Motai
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Reward Machines for Signal Temporal Logic》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Signal temporal logic (STL) provides a formal language for specifying real-time properties of real-valued observations, along with a quantitative robustness score for monitoring satisfaction. Control synthesis from STL specifications is of interest since manual controller design becomes infeasible as real-world systems grow in complexity. Moreover, many modern autonomous and AI-enabled systems lack accurate and complete system models, which makes optimization-based synthesis approaches unsuitable and motivates learning-based control. Prior work uses STL robustness scores as rewards in reinforcement learning (RL) to obtain control policies satisfying given specifications; however, robustness depends on execution history, leading to intractable state space expansion for general long-horizon specifications with arbitrarily nested temporal operators. This work introduces a novel automata-based approach that provides an efficient memory mechanism and associated Markovian rewards suitable for RL frameworks. Our approach constructs a timed alternating automaton from the given STL specifications, augments the state space with automaton locations and clock valuations, and derives rewards from the automaton acceptance condition. We empirically demonstrate that our approach learns policies that achieve higher robustness scores and satisfaction rates than those learned by existing approaches using robustness-based rewards.

</details>

---

### [[20_Research/Papers/大模型/No_Universal_Signal_Predicts_Sample-Level_LLM_Regression_under_Version_Updates|No Universal Signal Predicts Sample-Level LLM Regression under Version Updates]]

![[assets/2608.13607_figure.png|800]]

- **arXiv**: [2608.13607](https://arxiv.org/abs/2608.13607)
- **PDF**: https://arxiv.org/pdf/2608.13607
- **详细分析**: [[20_Research/Papers/大模型/No_Universal_Signal_Predicts_Sample-Level_LLM_Regression_under_Version_Updates|No Universal Signal Predicts Sample-Level LLM Regression under Version Updates]]
- **作者**: Jia Sheng, Yiwei Lu
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM

#### 研究背景与动机

《No Universal Signal Predicts Sample-Level LLM Regression under Version Updates》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GPQA, HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier LLMs are updated frequently and typically outperform their predecessors in aggregate. But aggregate gains say little about individual samples: an update can still cause sample-level regression, where a response correct under the old model becomes incorrect under the new one. This paper studies how to predict such regressions from signals available at inference time. We compare single-model signals (confidence, logit margin, attention entropy) against cross-version signals (output KL divergence, likelihood drift, token-level KL, representation drift) under a unified added-value test that isolates each signal's gain over a confidence baseline. Across six benchmarks in three task families (multiple-choice question answering, or MCQ; math reasoning; code generation) and six model update pairs, we find that (1) signal effectiveness is task-dependent: confidence is strongest on MCQ and simpler math, while likelihood/KL signals give the most frequent gains on harder math and code; (2) no signal is universally best across model updates either; and (3) some cross-version signals stay informative even when confidence fails, including without labels, which supports a proof-of-concept selective fallback that routes high-risk samples back to the old model. Practitioners can use these task-level patterns to choose which regression signal to trust for a given update. Code is available at https://github.com/jiashengsally/llm-regression-signals.

</details>

---

### [[20_Research/Papers/具身智能/Active_Perception_for_Embodied_Disambiguation|Active Perception for Embodied Disambiguation]]

![[assets/2608.13605_figure.png|800]]

- **arXiv**: [2608.13605](https://arxiv.org/abs/2608.13605)
- **PDF**: https://arxiv.org/pdf/2608.13605
- **详细分析**: [[20_Research/Papers/具身智能/Active_Perception_for_Embodied_Disambiguation|Active Perception for Embodied Disambiguation]]
- **作者**: Yiwei Liu, Luwei Yang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Active Perception for Embodied Disambiguation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural language provides robots with a flexible task interface, but target ambiguity in embodied environments arises not only from user intent; it can also result from missing taskrelevant physical evidence in the current observation. Existing interactive disambiguation methods primarily obtain additional information by asking the user, whereas occlusion, restricted viewpoints, unreadable text, and unobserved targets require the robot to actively change its observation. We propose an active-perception framework for embodied target disambiguation that uses active observation as the backbone for information acquisition and uses a vision-language model to decide, on the basis of accumulated visual evidence and interaction information, whether to continue observing, request clarification, or complete target selection. Active observation can both directly recover missing discriminative evidence and reveal object names, labels, and semantic attributes, thereby improving user clarification when it remains necessary. Real-robot experiments show that the framework combines physical information acquisition and userintent clarification within a unified embodied disambiguation process.

</details>

---

### [[20_Research/Papers/大模型/Measuring_Cross-Task_Behavioral_Consistency_in_Language_Model_Agents|Measuring Cross-Task Behavioral Consistency in Language Model Agents]]

![[assets/2608.13598_figure.png|800]]

- **arXiv**: [2608.13598](https://arxiv.org/abs/2608.13598)
- **PDF**: https://arxiv.org/pdf/2608.13598
- **详细分析**: [[20_Research/Papers/大模型/Measuring_Cross-Task_Behavioral_Consistency_in_Language_Model_Agents|Measuring Cross-Task Behavioral Consistency in Language Model Agents]]
- **作者**: Amritesh Banerjee, Pranil Raichura
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Measuring Cross-Task Behavioral Consistency in Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent evaluation relies almost entirely on outcome metrics such as success rate, which capture whether an agent succeeds but not how consistently it behaves. We argue that behavioral consistency across tasks is a distinct and measurable property, and we introduce the Behavioral Consistency Metric (BCM) to quantify it. BCM trains a model to predict task success from behavioral features of agent execution traces, derives a per-trajectory feature-attribution vector, and measures the mean pairwise similarity of these vectors within an agent system. Across roughly 9,000 trajectories from six language model agents on software engineering tasks, our central finding is that cross-task and within-task consistency are distinct axes that can diverge: some systems are locally reproducible, behaving similarly on repeated attempts at one task, yet globally fragmented, with no stable strategy across different tasks, while others are consistent at both scales. Prior work measures only same-task reproducibility and so cannot observe this separation. We further find that consistency is not reducible to success rate, since systems with comparable success can differ sharply in consistency, and that the frontier-versus-open-source consistency gap persists under a within-task control that holds task difficulty constant. We position BCM as a process-level reliability signal that complements outcome metrics, and we are explicit about the conditions under which it is meaningful.

</details>

---

### [[20_Research/Papers/大模型/From_Prediction_to_Intervention_Personalized_Meal-Level_Glucose_Regulation_via_an_LLM_Agent|From Prediction to Intervention: Personalized Meal-Level Glucose Regulation via an LLM Agent]]

![[assets/2608.13581_figure.png|800]]

- **arXiv**: [2608.13581](https://arxiv.org/abs/2608.13581)
- **PDF**: https://arxiv.org/pdf/2608.13581
- **详细分析**: [[20_Research/Papers/大模型/From_Prediction_to_Intervention_Personalized_Meal-Level_Glucose_Regulation_via_an_LLM_Agent|From Prediction to Intervention: Personalized Meal-Level Glucose Regulation via an LLM Agent]]
- **作者**: Mingyu Huang, Weiqing Min, Ying Jin, Yilin Wang, Shuqiang Jiang
- **cs 子类**: cs.AI, cs.HC, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《From Prediction to Intervention: Personalized Meal-Level Glucose Regulation via an LLM Agent》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalized glucose regulation remains a central yet unresolved challenge in precision nutrition, as postprandial glucose response varies substantially across individuals. Existing approaches based on glycemic indices fail to adequately account for such heterogeneity and lack the mechanism to dynamically adjust meals based on personal physiological feedback. In this context, recent advances in LLM-based agents offer a promising direction, as they enable context-aware reasoning and iterative refinement. Inspired by this, we propose a physio-feedback agentic loop, a unified system that integrates individualized absorption modeling with dietary intervention to regulate glucose response. Specifically, we develop a Physiology-Aware Glucose Predictor to model individualized absorption dynamics through a learnable Temporal Physiological Absorption Decay Module. We then construct a Prediction-Driven Two-Stage Meal Optimization Agent that iteratively refines real-world meals using predicted outcomes as explicit feedback. Through extensive experiments on multiple public datasets, we demonstrate that our method not only improves prediction accuracy but also effectively reduces glucose excursions. To the best of our knowledge, this paper marks the first step in integrating physiological learning with an LLM-based agent for personalized glucose regulation.

</details>

---

### [[20_Research/Papers/大模型/Agentao_A_Governed_Local-First_Runtime_for_Tool-Using_LLM_Agents|Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents]]

![[assets/2608.13574_figure.png|800]]

- **arXiv**: [2608.13574](https://arxiv.org/abs/2608.13574)
- **PDF**: https://arxiv.org/pdf/2608.13574
- **详细分析**: [[20_Research/Papers/大模型/Agentao_A_Governed_Local-First_Runtime_for_Tool-Using_LLM_Agents|Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents]]
- **作者**: Bo Jin, Qiang Jiao, Xin Tong
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Agentao: A Governed Local-First Runtime for Tool-Using LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Agent-SafetyBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents increasingly operate as execution systems that invoke tools, modify local state, use persistent memory, and interact with external protocols. These capabilities make agents useful, but they also introduce risks related to over-privileged actions, weak auditability, prompt injection, tool poisoning, and uncontrolled side effects. This paper presents Agentao, a governed local-first runtime for tool-using LLM agents. Agentao separates model-generated action proposals from host-authorized execution through a layered architecture consisting of host-facing surfaces, a host contract, a runtime core, a permission-mediated tool system, and supporting subsystems for memory, replay, plugins, skills, sub-agents, and protocol integration. We describe the motivation, threat model, design goals, governance model, execution pipeline, and structured event interface of the system. Agentao does not provide formal safety guarantees; rather, it demonstrates how permissions, state, protocol boundaries, and execution traces can be made explicit runtime abstractions for building agents that are more governable, inspectable, and suitable for host-controlled local environments. The code is publicly available at https://github.com/jin-bo/agentao.

</details>

---

### [[20_Research/Papers/大模型/A_Year_in_LLM_Serving_Workload_Evolution,_Caching_and_Load-Balancing|A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing]]

![[assets/2608.13573_first_page.png|800]]

- **arXiv**: [2608.13573](https://arxiv.org/abs/2608.13573)
- **PDF**: https://arxiv.org/pdf/2608.13573
- **详细分析**: [[20_Research/Papers/大模型/A_Year_in_LLM_Serving_Workload_Evolution,_Caching_and_Load-Balancing|A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing]]
- **作者**: William Nixon, Jon Durbin, Florian Standhartinger, Haryadi S. Gunawi, Juncheng Yang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM

#### 研究背景与动机

《A Year in LLM Serving: Workload Evolution, Caching and Load-Balancing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) serving has become a critical cloud workload, and realistic traces are essential for motivating and benchmarking serving systems. However, existing LLM serving workload studies remain limited in scale and scope. They often observe short time periods and provide limited visibility into how users interact with models in production. As a result, they do not fully capture how LLM serving workloads evolve over time or how user-model interactions shape production traffic. In this work, we further the understanding of real-world LLM serving workloads through both a global characterization and a longitudinal study of a one-year production trace from Chutes. Unlike prior studies, our trace captures full production behavior across many models and users, including both popular and long-tail models. We analyze the workload from aggregate, temporal, model-level, and user-level perspectives, revealing workload evolution and user-model structure that are typically hidden behind aggregate views. To support future research, we will release the full one-year trace with the paper, enabling downstream studies of production behavior without relying on sampled or synthetically generated workloads.

</details>

---

### [[20_Research/Papers/大模型/Not_All_Tokens_Are_Equal_Inflation-Aware_Routing_for_Agentic_LLM_Systems|Not All Tokens Are Equal: Inflation-Aware Routing for Agentic LLM Systems]]

![[assets/2608.13571_figure.png|800]]

- **arXiv**: [2608.13571](https://arxiv.org/abs/2608.13571)
- **PDF**: https://arxiv.org/pdf/2608.13571
- **详细分析**: [[20_Research/Papers/大模型/Not_All_Tokens_Are_Equal_Inflation-Aware_Routing_for_Agentic_LLM_Systems|Not All Tokens Are Equal: Inflation-Aware Routing for Agentic LLM Systems]]
- **作者**: Heming Fu, Shan Lin, Qianqian Xie, Guojun Xiong
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《Not All Tokens Are Equal: Inflation-Aware Routing for Agentic LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgentBench, HotpotQA, RouterBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a language model fails to answer a query on the first attempt, an agentic system retries, consuming additional tokens each time. This retry overhead creates a gap between what a model's per-token price implies and what a full workflow actually costs. We call this gap \emph{token inflation} and define it as the ratio of true workflow cost to single-call cost. Systems like FrugalGPT route based on the latter, which can underestimate real cost by more than $2\times$ on difficult tasks. We address this with InflationAgent, a four-stage router that (1) measures token inflation systematically across model tiers and task types, finding inflation as high as $4.25\times$ for a 7B model on multi-hop question answering; (2) introduces CoT Branching Entropy (CBE), a pre-execution difficulty signal computed entirely from local inference, which predicts high inflation with AUROC 0.887; and (3) selects models by maximizing a Semantic Exchange Rate (SER) that divides expected accuracy by predicted true cost, with a fresh-escalation policy that discards failed chains before routing to a stronger model. On GSM8K under a fixed budget, InflationAgent achieves 94.7\% accuracy versus 91.0\% for FrugalGPT while using 31\% fewer tokens, and we show that forwarding a failed reasoning chain to GPT-4o reduces its accuracy by up to 34.8 percentage points, validating the fresh-escalation design.

</details>

---

### [[20_Research/Papers/大模型/Does_a_Language_Server_Save_Tokens_for_Coding_Agents_A_Measurement_Methodology_and_Preliminary_Study|Does a Language Server Save Tokens for Coding Agents? A Measurement Methodology and Preliminary Study]]

![[assets/2608.13568_figure.png|800]]

- **arXiv**: [2608.13568](https://arxiv.org/abs/2608.13568)
- **PDF**: https://arxiv.org/pdf/2608.13568
- **详细分析**: [[20_Research/Papers/大模型/Does_a_Language_Server_Save_Tokens_for_Coding_Agents_A_Measurement_Methodology_and_Preliminary_Study|Does a Language Server Save Tokens for Coding Agents? A Measurement Methodology and Preliminary Study]]
- **作者**: Pengcheng Xu
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Does a Language Server Save Tokens for Coding Agents? A Measurement Methodology and Preliminary Study》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CORE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents spend most of their context budget on retrieval. Lexical retrieval (grep) is universal, instant, and zero-setup, but noisy: it cannot tell a definition from a call from a comment. Semantic retrieval via the Language Server Protocol (LSP) is precise and typed, but needs a running, indexed server and pays a per-symbol round-trip. The claim that semantic retrieval is more token-efficient is, we find, asserted almost everywhere and measured almost nowhere: no public source isolates the LSP-vs-lexical token delta for an agent at equal task-success. This paper formalizes the question with one metric (tokens-to-success), specifies a five-arm ablation isolating semantic retrieval from confounds, maps three pre-stated failure modes onto measurable variables, and reports a preliminary study (Python and TypeScript repos; Claude Opus 4.8, Sonnet 4.6, Haiku 4.5). The answer is conditional and usually negative. On symbol-named localization the LSP costs tokens (+6% to +118%) and the agent ignores it when free. On reference-completeness it buys precision but not token savings and cannot raise the recall ceiling set by agent thoroughness; it saves tokens only for the weakest model. Tool choice is task-dependent: models default to grep on localization (0-6% semantic use) but reach for the LSP about half the time on reference tasks, unprompted. On edits scored by real test execution the gap is starkest: grep solves multi-file renames perfectly, a location-only LSP fails three-quarters of them by missing a call site, and even a complete, index-warmed, text-enriched LSP (each reference's line inline, as production LSP-MCP servers do) recovers most of the gap but cannot close it, since a rename must touch comments and strings that semantic references exclude. The implication is not LSP-always but an adaptive router keyed on task class, model capability, and lexical noise.

</details>

---

### [[20_Research/Papers/大模型/Inducing_Reward-Free_Judging_Rubrics_that_Reduce_Over-Crediting_in_Agent_Evaluation|Inducing Reward-Free Judging Rubrics that Reduce Over-Crediting in Agent Evaluation]]

![[assets/2608.13564_figure.png|800]]

- **arXiv**: [2608.13564](https://arxiv.org/abs/2608.13564)
- **PDF**: https://arxiv.org/pdf/2608.13564
- **详细分析**: [[20_Research/Papers/大模型/Inducing_Reward-Free_Judging_Rubrics_that_Reduce_Over-Crediting_in_Agent_Evaluation|Inducing Reward-Free Judging Rubrics that Reduce Over-Crediting in Agent Evaluation]]
- **作者**: Darragh Quinn, David Dylan, Roisin Healy, Fionn Carroll, Maeve Donnelly, Cormac Sheehan
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Inducing Reward-Free Judging Rubrics that Reduce Over-Crediting in Agent Evaluation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, CharacterEval, G-Eval, MT-Bench, PersonaGym, RewardBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating language-model agents at scale increasingly relies on a second language model as an automatic judge, because the gold signal, an executable environment reward, is expensive, slow, or unavailable at deployment time. Such a judge is a reward-free proxy whose value depends on whether it can be trusted, yet existing judges either hand-write the scoring rubric, as in G-Eval, or fine-tune the judge's weights, and both tend to credit fluent but unsuccessful trajectories as successes. We instead induce the text of an agent-judging rubric from a small set of ground-truth-labeled trajectories, grounding it in true outcomes. We present RubricForge, which evolves a judge rubric by reflective evolution against labeled trajectories to maximize agreement with the environment reward, freezes it, and applies it to held-out trajectories in one model call with no environment access. The optimized artifact is human-readable text, so every verdict is attributable to named criteria. Using one frozen 7B model as both agent and judge, on tau-bench (173 labeled trajectories drawn from 220 rollouts) and WebShop (160), the principal gain is faithfulness rather than raw agreement. The edge over a generic G-Eval judge is not statistically significant (McNemar p = 0.248), and absolute-score calibration marginally favors the generic judge (|err| difference -0.048, p = 2x10^-4). Yet RubricForge over-credits failed trajectories roughly half as often (0.115 vs. 0.173 false-pass rate on tau-bench, with three over-credit catches and zero reversals) and ranks graded WebShop outcomes more faithfully (Spearman 0.410 vs. 0.370). For a reward-free evaluator the false-pass rate, not aggregate agreement, is the deployment-relevant quantity, since a false pass ships a broken agent whereas a false fail merely costs a retry.

</details>

---

### [[20_Research/Papers/大模型/Proxy-Validated_LLM_UX_Micro-Simulations_An_Artifact-First_Protocol_for_Early-Stage_Decision_Support|Proxy-Validated LLM UX Micro-Simulations: An Artifact-First Protocol for Early-Stage Decision Support]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2608.13563](https://arxiv.org/abs/2608.13563)
- **PDF**: https://arxiv.org/pdf/2608.13563
- **详细分析**: [[20_Research/Papers/大模型/Proxy-Validated_LLM_UX_Micro-Simulations_An_Artifact-First_Protocol_for_Early-Stage_Decision_Support|Proxy-Validated LLM UX Micro-Simulations: An Artifact-First Protocol for Early-Stage Decision Support]]
- **作者**: Alexandre Cristovão Maiorano
- **cs 子类**: cs.AI, cs.HC, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Proxy-Validated LLM UX Micro-Simulations: An Artifact-First Protocol for Early-Stage Decision Support》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Early-stage teams often lack users, time, and budget to run repeated UX studies, yet still need decision-oriented signals to iterate safely. We study an LLM-driven UX micro-simulation pipeline that generates structured customer-experience feedback (walkthrough steps, friction points, micro-survey signals) from versioned prompts, personas, tasks, and UI snapshots. Because public usability datasets with task outcomes are scarce, we validate simulated friction themes using multiple public proxy corpora (app reviews, support tweets, and open-source software issues). We propose a lightweight proxy-validation protocol with two alignment metrics: top-k Jaccard and distributional weighted-Jaccard (W), and compare lexical, TF-IDF, and multilingual embedding baselines across six proxy datasets. Embedding-based alignment yields higher W than lexical baselines on primary app-review and support-tweet proxies (e.g., W=0.128 vs 0.000 on Gojek), while top-k Jaccard is shown to overstate alignment at large k. We ablate four agent strategies (single-pass, best-of-N, hybrid, and a proposed score-then-select judge) across Azure OpenAI deployments and report bootstrap confidence intervals over 8 method-dataset pairs; these intervals reveal that the embedding W point estimate is systematically unstable under resampling at our subsample size. We also provide a failure-mode analysis of grounding and fabrication proxies, with documented calibration caveats and worked examples of outputs flagged as fabricated by an adversarial judge. Our artifact-first pipeline produces reproducible tables and figures from versioned run artifacts, supporting iterative prompt and taxonomy refinement before final paid-model calibration.

</details>

---
