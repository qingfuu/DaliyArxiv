# cs.AI | Artificial Intelligence | 2026-07-15

#arxiv #ComputerScience

**论文数**: 41

### [[20_Research/Papers/大模型/Do_AI_Agents_Know_When_a_Task_Is_Simple_Toward_Complexity-Aware_Reasoning_and_Execution|Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution]]

![[assets/2607.13034_figure.png|800]]

- **arXiv**: [2607.13034](https://arxiv.org/abs/2607.13034)
- **PDF**: https://arxiv.org/pdf/2607.13034
- **详细分析**: [[20_Research/Papers/大模型/Do_AI_Agents_Know_When_a_Task_Is_Simple_Toward_Complexity-Aware_Reasoning_and_Execution|Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution]]
- **作者**: Junjie Yin, Xinyu Feng
- **cs 子类**: cs.AI, cs.CL, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Do AI Agents Know When a Task Is Simple? Toward Complexity-Aware Reasoning and Execution》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MSE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents increasingly automate multi-step engineering and informatics workflows, yet they rarely ask how much effort a task actually requires. They often follow a maximum-context-first strategy--re-reading files and dependencies they have already seen--turning a one-line edit into a small code-base audit. We argue the missing capability is task-aware execution-scope estimation: judging a task's difficulty, the information it truly needs, and the shortest reliable path before committing budget. We formalize minimum-sufficient execution and the Agent Cognitive Redundancy Ratio (ACRR), and propose E3 (Estimate, Execute, Expand): the agent estimates an initial operating point, executes a minimum viable path, and expands scope only when verification fails. On MSE-Bench--a deterministic benchmark of 121 edits in a capability-controlled simulator--E3 matches the strongest baseline's 100% success while cutting cost by 85%, tokens by 91%, and inspected files by 92%, and further beats a strong adaptive retrieval baseline by 16%; the gains survive held-out instruction wording and essentially every cost weighting. A companion real-model harness (LLM-Case) corroborates the effect on a live gpt-4o agent editing a real open-source library, with every candidate patch graded by actually running the project's real pytest suite against a measured oracle: the over-reading is milder but real, and E3 is the leanest and fastest policy at comparable task success--its one shortfall a provider rate-limit, not a wrong edit. We frame this as a controlled probe of execution redundancy, not a measurement of any deployed agent, and position task-aware execution as a step toward engineering-grounded AI (EGAI)--agents whose effort is anchored in the engineering reality of the task. We release the framework and benchmark.

</details>

---

### [[20_Research/Papers/强化学习/TerraZero_Procedural_Driving_Simulation_for_Zero-Demonstration_Self-Play_at_Scale|TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale]]

![[assets/2607.13028_figure.png|800]]

- **arXiv**: [2607.13028](https://arxiv.org/abs/2607.13028)
- **PDF**: https://arxiv.org/pdf/2607.13028
- **详细分析**: [[20_Research/Papers/强化学习/TerraZero_Procedural_Driving_Simulation_for_Zero-Demonstration_Self-Play_at_Scale|TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale]]
- **作者**: Zhouchonghao Wu, Akshay Rangesh, Weixin Li, Wei-Jer Chang, Zachary Lee, Tim Wang, Wei Zhan
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《TerraZero: Procedural Driving Simulation for Zero-Demonstration Self-Play at Scale》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SimNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training robust autonomous driving agents requires a simulator that is fast enough for reinforcement learning at scale, realistic enough to ground behavior in real-world map structure, and diverse enough to cover the safety-critical long tail that logged data rarely contains. We present TerraZero, a procedural driving simulator and self-play training stack. A configurable C engine runs simulation on the CPU and policy inference on the GPU over a zero-copy path, sustaining 1.3M agent-steps per second on a single server-grade GPU, far faster than existing object-level simulators, while keeping fidelity lighter single-agent systems omit: heterogeneous agents, multiple dynamics models, and full traffic-rule enforcement. TerraZero treats logged data only as a source of real-world map geometry, populating each map with randomized rule-based road users and signal controllers and randomizing agent dynamics, rewards, and sizes per episode, so a map yields an unbounded set of scenarios. Every reported policy trains from scratch by reinforcement learning alone on a compute-efficient self-play recipe across GPUs, with zero human demonstrations and no fallback planner at inference. Policies generalize zero-shot across cities and datasets, including emergent left-hand-traffic driving without explicit supervision. As an ego policy, TerraZero is the first fully learned policy to top the InterPlan long-tail benchmark, ahead of larger learned planners; on routine-driving val14 it ranks among the best approaches and is the safest, posting the best collision and time-to-collision scores. On Waymo Open Sim Agents realism the same recipe outperforms other demonstration-free methods and is competitive with the strongest reference-anchored self-play method. One stack serves both roles: driving policies across dynamics for cars and trucks, and sim agents that jointly control vehicles, pedestrians, and cyclists.

</details>

---

### [[20_Research/Papers/大模型/PalmClaw_A_Native_On-Device_Agent_Framework_for_Mobile_Phones|PalmClaw: A Native On-Device Agent Framework for Mobile Phones]]

![[assets/2607.13027_figure.png|800]]

- **arXiv**: [2607.13027](https://arxiv.org/abs/2607.13027)
- **PDF**: https://arxiv.org/pdf/2607.13027
- **详细分析**: [[20_Research/Papers/大模型/PalmClaw_A_Native_On-Device_Agent_Framework_for_Mobile_Phones|PalmClaw: A Native On-Device Agent Framework for Mobile Phones]]
- **作者**: Hongru Cai, Yongqi Li, Ran Wei, Wenjie Li
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PalmClaw: A Native On-Device Agent Framework for Mobile Phones》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AndroidWorld, AssistantBench, Mobile-Bench, MobileAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM) agents have moved beyond generating responses to executing multi-step tasks by calling tools, observing the results, and iteratively deciding the next action. Most agent systems run on desktops or servers, which support tool use and task automation. Mobile devices are also important agent environments because they are widely accessible and contain users' data, sensors, and daily-use applications. Existing mobile agents mainly operate smartphones through graphical user interface (GUI) actions such as tapping, swiping, and typing, which often form long, interface-dependent sequences, cannot directly access device capabilities, and make execution boundaries difficult to define. We present \textbf{PalmClaw}, an open-source agent framework that runs natively on mobile phones and manages the sessions, memory, skills, tools, and agent loop directly on the device. PalmClaw exposes device capabilities as device tools with explicit arguments, structured results, and clearly defined execution boundaries. This design enables agents to use mobile capabilities directly while keeping each action explicit and controlled. Experiments show an 11.5\% relative improvement in task success and a 94.9\% reduction in completion time over the strongest baseline, with lower setup burden and traces illustrating how execution boundaries are applied. Code is available at https://github.com/ModalityDance/PalmClaw.

</details>

---

### [[20_Research/Papers/大模型/Audio-Native_Speech_Recognition_with_a_Frozen_Discrete-Diffusion_Language_Model|Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model]]

![[assets/2607.13013_figure.png|800]]

- **arXiv**: [2607.13013](https://arxiv.org/abs/2607.13013)
- **PDF**: https://arxiv.org/pdf/2607.13013
- **详细分析**: [[20_Research/Papers/大模型/Audio-Native_Speech_Recognition_with_a_Frozen_Discrete-Diffusion_Language_Model|Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model]]
- **作者**: Harsha Vardhan Khurdula, Abhinav Kumar Singh, Yoeven D Khemlani, Vineet Agarwal
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM

#### 研究背景与动机

《Audio-Native Speech Recognition with a Frozen Discrete-Diffusion Language Model》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic speech recognition is dominated by autoregressive decoders that emit one token at a time. We ask whether a discrete diffusion language model can transcribe speech instead, refining a whole transcript in parallel over a small number of denoising steps. We train an audio-native interface for DiffusionGemma, a 26B mixture-of-experts model that generates text by uniform, random-token discrete diffusion rather than the absorbing-mask scheme common to recent diffusion language models. A frozen Whisper encoder supplies acoustic features, a lightweight projector maps them into the model embedding space, and low-rank adapters let the frozen backbone attend to the new modality. About 42M parameters are trained, which is 0.16 percent of the backbone. We find that the natural training objectives fail to ground the audio because their gradient reaches the projector only through attention that has already dismissed it. A connectionist temporal classification loss applied through the frozen output head breaks this deadlock. The resulting model reaches 6.6 percent word error rate on LibriSpeech test-clean, transcribes in roughly eight parallel steps regardless of utterance length, and uses a single adapter trained on six languages, which we evaluate here on English, Hindi, and Mandarin.

</details>

---

### [[20_Research/Papers/大模型/FormalAnalyticGeo_A_Neural-Symbolic_Based_Framework_for_Multimodal_Analytic_Geometry_Problem_Generation|FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation]]

![[assets/2607.12982_figure.png|800]]

- **arXiv**: [2607.12982](https://arxiv.org/abs/2607.12982)
- **PDF**: https://arxiv.org/pdf/2607.12982
- **详细分析**: [[20_Research/Papers/大模型/FormalAnalyticGeo_A_Neural-Symbolic_Based_Framework_for_Multimodal_Analytic_Geometry_Problem_Generation|FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation]]
- **作者**: Ruoran Xu, Wending Gao, Qiufeng Wang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《FormalAnalyticGeo: A Neural-Symbolic Based Framework for Multimodal Analytic Geometry Problem Generation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GeoEval, GeoQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Math reasoning has achieved significant progress with the rapid advancement of Multimodal Large Language Models (MLLMs), however analytic geometry remains largely underexplored, primarily due to the scarcity of annotated samples. Existing diagram generation approaches struggle with analytic geometry: template methods cannot handle constraint-driven layouts, and generative models lack the geometric precision to render annotated conic curves correctly. We present FormalAnalyticGeo, a scalable framework for fully automatic generation of multimodal analytic geometry problems. Leveraging the rigor of formal languages, we design the framework around CDL (Condition Description Language), a formal intermediate representation that bridges free-form problem text with precise diagram rendering via a Signed Distance Field (SDF) engine. The framework employs four specialized LLM components in sequence: a Generator that produces diverse analytic geometry problems, a Formalizer that converts each problem into CDL for SDF-based rendering, a Measurer that extracts ground-truth answers through vision-based measurement on the rendered diagrams, and a Quality Verifier that checks outputs at three stages. Structured feedback from the Quality Verifier drives automatic retry, forming a closed loop that eliminates any need for human annotation. Applying FormalAnalyticGeo at scale yields AnalyticGeo7K, a dataset of over 7K verified multimodal problems, each with aligned text, diagram, formal annotation, and ground truth.Experiments show that the generated problems achieve a median ground-truth relative error of 0.70\%, with 82.3\% of answers falling within 5\% of the exact symbolic solution. Our framework and dataset will be publicly released.

</details>

---

### [[20_Research/Papers/强化学习/Knowledge-_and_Gradient-Guided_Reinforcement_Learning_for_Parametrized_Action_Markov_Decision_Processes|Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes]]

![[assets/2607.12924_figure.png|800]]

- **arXiv**: [2607.12924](https://arxiv.org/abs/2607.12924)
- **PDF**: https://arxiv.org/pdf/2607.12924
- **详细分析**: [[20_Research/Papers/强化学习/Knowledge-_and_Gradient-Guided_Reinforcement_Learning_for_Parametrized_Action_Markov_Decision_Processes|Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes]]
- **作者**: Jonas Ehrhardt, René Heesch, Oliver Niggemann
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Knowledge- and Gradient-Guided Reinforcement Learning for Parametrized Action Markov Decision Processes》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：KGRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we study Reinforcement Learning in Parametrized Action Markov Decision Processes (PAMDP), where each decision consists of a symbolic action and numerical parameters. In such settings Reinforcement Learning algorithms typically determine parameters with one-shot estimators, which makes their training sample inefficient. Though in most PAMDP environments explicit but incomplete knowledge (e.g., rules, safety constraints, or expert heuristics) is available, it is rarely directly used to increase the sample-efficiency of training Reinforcement Learning agents. We step into this gap and propose our novel Neuro-Symbolic Knowledge- and Gradient-Guided Reinforcement Learning (KGRL) algorithm. KGRL uses domain knowledge in a Datalog knowledge base to derive the set of applicable actions and feasible parameters for a given state. This allows it to prune non-applicable actions from the decision-space and constrain the parameter spaces of the remaining actions. We then use a gradient-based parameter refinement loop to estimate the optimal parameters during training and deployment of the agent. By recording activated rules along the trajectory, KGRL additionally provides local procedural explanations on the pruning of actions and constraining of parameters. Overall, KGRL guides the agent's exploration and deployment toward feasible and constraint-aware decisions, while increasing sample efficiency during training. KGRL outperforms state-of-the-art RL baselines for PAMDPs in both, sample efficiency and episodic return.

</details>

---

### [[20_Research/Papers/具身智能/UR-VC_Unsupervised_Robotic_Value_Correction_for_Time-Derived_Progress_Proxies|UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies]]

![[assets/2607.12892_figure.png|800]]

- **arXiv**: [2607.12892](https://arxiv.org/abs/2607.12892)
- **PDF**: https://arxiv.org/pdf/2607.12892
- **详细分析**: [[20_Research/Papers/具身智能/UR-VC_Unsupervised_Robotic_Value_Correction_for_Time-Derived_Progress_Proxies|UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies]]
- **作者**: Lirui Zhao, Modi Shi, Li Chen, Qi Liu, Ping Luo, Hongyang Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《UR-VC: Unsupervised Robotic Value Correction for Time-Derived Progress Proxies》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern robot learning systems increasingly rely on dense progress or value signals to evaluate intermediate states, guide policy learning, and detect task completion, making the quality of these signals critical. Since such dense labels are rarely available at scale, normalized time within a demonstration is often used as a scalable substitute: later frames are treated as higher progress. However, this time-derived label is only a noisy proxy for physical task progress. In contact-rich manipulation, a robot may make progress and then lose it through slips, failed grasps, or partial undoing, while the time-derived label continues to increase monotonically. We introduce Unsupervised Robotic Value Correction (UR-VC), an offline, training-free method for correcting time-derived progress labels. UR-VC exploits a simple regularity in demonstration data: similar states often recur across different episodes, but at different timestamps. Instead of trusting the timestamp from a single trajectory, UR-VC retrieves similar states from other episodes and aggregates their time-derived labels to obtain a corrected progress estimate. UR-VC requires no manual progress labels, reward annotations, or additional value model. We evaluate UR-VC on real bimanual cloth flatten-and-fold data, a long-horizon deformable-object manipulation task with visible intermediate progress. The corrected labels capture local regressions and non-uniform progress that normalized time cannot represent, while preserving the overall task trend. We further use the corrected signal to construct advantage labels for VLA training, following recent advantage-conditioned policy learning. UR-VC shows a positive trend in real-robot task success under matched data, model, and training settings.

</details>

---

### [[20_Research/Papers/具身智能/Unveiling_Complex_Collective_Behaviors_from_Simple_Rewards|Unveiling Complex Collective Behaviors from Simple Rewards]]

![[assets/2607.12861_figure.png|800]]

- **arXiv**: [2607.12861](https://arxiv.org/abs/2607.12861)
- **PDF**: https://arxiv.org/pdf/2607.12861
- **详细分析**: [[20_Research/Papers/具身智能/Unveiling_Complex_Collective_Behaviors_from_Simple_Rewards|Unveiling Complex Collective Behaviors from Simple Rewards]]
- **作者**: Yize Mi, Jianan Li, Liang Li, Shiyu Zhao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Unveiling Complex Collective Behaviors from Simple Rewards》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent Reinforcement Learning (MARL) holds great potential for robot swarms, but the black-box nature of neural policies complicates strategic analysis, limiting multi-robot applications. Furthermore, complex swarm behaviors can surprisingly emerge from simple rewards without explicit aggregation incentives. Unveiling the mechanisms behind this emergence is critical, but the disconnection between simple rewards and collective behaviors exacerbates interpretability challenges. This paper aims to reveal the hidden mechanisms in this process. We propose a two-stage EEC (\LinkIII) explanatory framework. This includes a novel analytical tool called the Agent Response Map (ARM), which reveals agents' decision-making patterns across space and identifies regions of aggregation and avoidance. ARM reveals that the robots implicitly learn the geometric fields of the environment and utilize these structures as desired targets for coordinated movement. We validate this finding across two distinct tasks: a cooperative multi-robot shape assembly and a competitive predator-prey pursuit-evasion. 1) In the cooperative task, ARM identifies the unoccupied target interior as the desired destination for robot navigation. As the center becomes occupied, this target region automatically shifts toward the boundary, demonstrating the robots' capacity to autonomously explore unoccupied areas. 2) In the competitive task, ARM surprisingly identifies the boundary of the predators' Voronoi diagram as the convergence destination for prey agents. Together, these two tasks demonstrate the capability of ARM to discover the hidden geometric structures underlying MARL policies in robot swarms.

</details>

---

### [[20_Research/Papers/其他/Human-AI_Agent_Interaction_as_a_Neuroplastic_Training_Environment|Human-AI Agent Interaction as a Neuroplastic Training Environment]]

![[assets/2607.12823_figure.png|800]]

- **arXiv**: [2607.12823](https://arxiv.org/abs/2607.12823)
- **PDF**: https://arxiv.org/pdf/2607.12823
- **详细分析**: [[20_Research/Papers/其他/Human-AI_Agent_Interaction_as_a_Neuroplastic_Training_Environment|Human-AI Agent Interaction as a Neuroplastic Training Environment]]
- **作者**: Eranga Bandara, Ross Gore, Asanga Gunaratna, Ravi Mukkamala, Nihal Siriwardanagea, Gihan Siriwardanagea, Sachini Rajapakse, Isurunima Kularathna, Pramoda Karunarathna, Chalani Rajapakse, Sachin Shetty, Christopher K. Rhea...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Human-AI Agent Interaction as a Neuroplastic Training Environment》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interaction with AI agents has become one of the most frequent activities of everyday digital life. Whether conversing with an assistant, working with a coding copilot, or generating images, the interaction follows a common iterative loop: a request is issued, a result returned, appraised, and the request revised. We observe that this loop is a high-frequency stream of contact events -- moments at which a result meets a person and a conditioned response may fire before deliberate appraisal -- making everyday agent interaction an unrecognised neuroplastic training environment. When a result disappoints, reactive patterns of impatience, perfectionism, frustration, and self-criticism are repeatedly evoked, and under activity-dependent synaptic plasticity each uninterrupted cycle deepens the underlying pathway through long-term potentiation. Ordinary agent use may thus quietly strengthen the very patterns it provokes. We propose that the same training environment can be engaged to the opposite effect. Treating conditioned reactive patterns as physical neurone paths -- activated through a pre-cognitive feeling tone that opens a brief regulatory gap -- we develop a framework in which, at that gap, in place of the reactive re-prompt, a person performs behind-the-scenes observation: watching the neural process operate so the cascade does not complete and long-term depression weakens the path rather than potentiation strengthening it. We characterise this practice through three layers of observation and two modes of application: a user-guided mode requiring no change to existing tools, and an agent-assisted mode in which an ordinary agent is lightly configured to support observation at the gap. We illustrate the framework through generative image prompting, showing how a single frustrating session is behaviourally nearly identical whether or not it is observed, yet neurologically opposite.

</details>

---

### [[20_Research/Papers/大模型/Visual_Access_Boundaries_in_Vision-Language_Model_Reasoning|Visual Access Boundaries in Vision-Language Model Reasoning]]

![[assets/2607.12815_figure.png|800]]

- **arXiv**: [2607.12815](https://arxiv.org/abs/2607.12815)
- **PDF**: https://arxiv.org/pdf/2607.12815
- **详细分析**: [[20_Research/Papers/大模型/Visual_Access_Boundaries_in_Vision-Language_Model_Reasoning|Visual Access Boundaries in Vision-Language Model Reasoning]]
- **作者**: Hiroto Osaka, Shohei Taniguchi, Gouki Minegishi, Kai Yamashita, Masahiro Suzuki, Yutaka Matsuo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Visual Access Boundaries in Vision-Language Model Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Chain-of-Thought (CoT) prompting is widely used as a test-time scaling strategy for Vision-Language Models (VLMs), but it remains unclear what is extended when VLMs generate longer reasoning traces. We ask whether CoT requires continued access to image tokens, or whether it mainly operates over visual information already made available earlier in the forward pass. We introduce Visual Access Sweep, a causal intervention that masks attention from generated-token queries to image-token keys along layer depth and generation time, and define the Visual Access Boundary (VAB) as the minimal access region that preserves task accuracy. Across six model configurations from Qwen2.5-VL and InternVL3, both no-CoT direct answering and CoT prompting exhibit finite VABs. In Qwen2.5-VL-32B and InternVL3 at 14B and 38B scales, when CoT is evaluated against the no-CoT full-access target, its VAB layer differs from the no-CoT boundary by at most two layers, despite substantially longer generations. This suggests that CoT does not primarily improve performance by prolonging direct image-token access throughout the reasoning trace, but by extending language-side computation over image-derived hidden-state information. We further show that CoT gains are constrained by perceptual readout. CoT helps when the queried visual attribute can be reliably read out by the model, but not when that readout is unreliable. A symbolic-attribute oracle shows that CoT can improve counting once ground-truth attributes are supplied as text, while a single-object probe-vs-decode check shows that hard attributes can be linearly recoverable from hidden states yet difficult for the model itself to output. Together, these analyses place the bottleneck at readout rather than counting.

</details>

---

### [[20_Research/Papers/具身智能/PixelLoop_Shortcut_Topological_Navigation_with_Pixel-Level_Loops|PixelLoop: Shortcut Topological Navigation with Pixel-Level Loops]]

![[assets/2607.12811_figure.png|800]]

- **arXiv**: [2607.12811](https://arxiv.org/abs/2607.12811)
- **PDF**: https://arxiv.org/pdf/2607.12811
- **详细分析**: [[20_Research/Papers/具身智能/PixelLoop_Shortcut_Topological_Navigation_with_Pixel-Level_Loops|PixelLoop: Shortcut Topological Navigation with Pixel-Level Loops]]
- **作者**: Sarthak Chittawar, Vansh Garg, Aditya Vadali, Krish Pandya, Rohit Jayanti, Sourav Garg, Madhava Krishna
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《PixelLoop: Shortcut Topological Navigation with Pixel-Level Loops》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, SeqNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although topological mapping and navigation have been studied extensively, the specific role and downstream effect of loop closures in purely topological representations has received relatively little attention. Importantly, loop closure over topological maps is distinct from loop closure over globally referenced trajectories and metric maps. Building on recent denser topologies grounded in pixel-level, relative 3D geometry, we propose PixelLoop which introduces loop closures directly in pixel space. Unlike sparse image-level edges or pose-graph corrections in SLAM, our pixel-level closures act as dense topological shortcuts that alter planning connectivity and cost propagation rather than merely aligning coordinates. This dense connectivity enables stable any-point-to-any-point navigation and produces costmaps that align accurately with geometric shortest paths. In particular, we showcase the distinct advantage of applying loop closures to fine-grained pixel topologies rather than image-level topologies. Across extensive simulated experiments, PixelLoop achieves over 35% absolute improvement in both Success Rate and SPL compared to image-relative baselines, with the largest gains in scenarios requiring shortcut exploitation. Results are further validated through real-world mobile robot deployments, demonstrating that dense pixel-level loop closures provide a practical and robust foundation for topological visual navigation. Project Page: https://pixelloop-nav.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_Tracking_and_Terminal_Guidance_of_Moving_Targets_for_Fixed-Wing_UAVs|Autonomous Tracking and Terminal Guidance of Moving Targets for Fixed-Wing UAVs]]

![[assets/2607.12801_figure.png|800]]

- **arXiv**: [2607.12801](https://arxiv.org/abs/2607.12801)
- **PDF**: https://arxiv.org/pdf/2607.12801
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_Tracking_and_Terminal_Guidance_of_Moving_Targets_for_Fixed-Wing_UAVs|Autonomous Tracking and Terminal Guidance of Moving Targets for Fixed-Wing UAVs]]
- **作者**: Wei-Hao Liou, Teng-Hu Cheng
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: EmbodiedAI, ComputerVision, Systems

#### 研究背景与动机

《Autonomous Tracking and Terminal Guidance of Moving Targets for Fixed-Wing UAVs》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study introduces a unified control framework for fixed-wing unmanned aerial vehicles (UAVs) fitted with a pan-tilt (PT) camera, intended to perform an end-to-end mission spanning from initial target detection to accurate terminal engagement. The proposed system employs a three-phase strategy: a vision-based target acquisition phase, an NMPC-based tracking phase, and a terminal guidance phase. During tracking, the framework uses an Unscented Kalman Filter (UKF) to fuse YOLO-based visual detections with inertial measurements, enabling robust target state estimation under unknown dynamics. To ensure reliable visual contact, we introduce a constraint-aware Nonlinear Model Predictive Control (NMPC) strategy that incorporates Control Barrier Functions (CBFs) to explicitly prevent UAV self-occlusion -- a common limitation in fixed-wing tracking. Upon satisfying terminal engagement conditions, the system seamlessly transitions control to a quaternion-based Biased Proportional Navigation Guidance (BPNG) law, enforcing precise impact angle constraints. High-fidelity simulations demonstrate that the framework achieves stable, robust tracking and accurate terminal interception while strictly respecting the vehicle's dynamic limits and camera field-of-view constraints.

</details>

---

### [[20_Research/Papers/大模型/Who_Grades_the_Grader_Co-Evolving_Evaluation_Metrics_and_Skills_for_Self-Improving_LLM_Agents|Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents]]

![[assets/2607.12790_figure.png|800]]

- **arXiv**: [2607.12790](https://arxiv.org/abs/2607.12790)
- **PDF**: https://arxiv.org/pdf/2607.12790
- **详细分析**: [[20_Research/Papers/大模型/Who_Grades_the_Grader_Co-Evolving_Evaluation_Metrics_and_Skills_for_Self-Improving_LLM_Agents|Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents]]
- **作者**: Xing Zhang, Guanghui Wang, Yanwei Cui, Ziyuan Li, Wei Qiu, Bing Zhu, Peiyang He
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-evolving agent systems improve by creating, revising, and retiring their own skills, but every such loop rests on a hidden assumption: a reliable evaluation metric already exists. In many real applications it does not. We make three claims. First, metrics can be \emph{evolved}: our metric loop searches compositions of small drawback detectors under a full evolutionary lifecycle, trained to agree with a ten-item anchored reference set, regularized by consensus over unlabeled outputs, and audited against a held-out anchor it never reads, yielding a transparent, inspectable metric rather than an opaque judge. Second, since no metric exists to beat, the yardstick is recovering what an accurate metric would have enabled, and \emph{Double Ratchet}, our co-evolution of the metric with a lifecycle-managed skill loop, does so: across code generation (MBPP+), enterprise text-to-SQL (Spider~2.0-Snow), and reference-free report generation, it retains 88--110\% of the held-out lift achieved by the same skill loop driven by ground truth or the best available rubric. Third, safety comes from anchor discipline plus outer audits: removing anchor guards collapses the metric into a vacuous detector while removing the lifecycle does not; and when evolved skills gamed the report rubric, an independent judge caught it, one detector repaired it, and a task-aware judge then preferred the evolved outputs over the pre-evolution baseline in 77\% of decided pairs. We argue this failure-expecting architecture is the right default wherever no reliable automatic verifier exists.

</details>

---

### [[20_Research/Papers/大模型/Do_We_Really_Need_Multimodal_Emotion_Language_Models_Larger_Than_1B_Parameters|Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?]]

![[assets/2607.12787_figure.png|800]]

- **arXiv**: [2607.12787](https://arxiv.org/abs/2607.12787)
- **PDF**: https://arxiv.org/pdf/2607.12787
- **详细分析**: [[20_Research/Papers/大模型/Do_We_Really_Need_Multimodal_Emotion_Language_Models_Larger_Than_1B_Parameters|Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?]]
- **作者**: Kaiwen Zheng, Junchen Fu, Wenhao Deng, Hu Han, Joemon M. Jose, Xuri Ge
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.55（加权：大模型 0.55）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Do We Really Need Multimodal Emotion Language Models Larger Than 1B Parameters?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in multimodal large language models (MLLMs) have significantly improved the performance of multimodal emotion recognition (MER) and enabled interpretable description generation by jointly modeling video, audio, and language, etc. However, these performance improvements are often accompanied by an increase in model parameter size (e.g, at least 7B), which simultaneously incurs high computational costs and reduces inference efficiency, thereby hindering real-time deployment on resource-constrained platforms such as robots and mobile devices. This raises a fundamental question: do we really need the multimodal MER model larger than 1B parameters for high-quality MER? In this paper, we challenge the assumption that larger models are inherently necessary and proposes a lightweight MER framework (called Light-MER), which achieves better and faster multimodal sentiment understanding and recognition through knowledge distillation. It can transfer knowledge from a strong, large-scale teacher model to a lightweight sub-billion-parameter student model, aiming to preserve rich multimodal emotion reasoning and recognition while substantially improving deployment efficiency. Specifically, we introduce two new optimization strategies to enhance knowledge transfer: (1) a new optimal transport loss that combines Sliced Wasserstein Distance with hidden-state alignment, and (2) a new multi-reward optimization strategy based on GRPO that balances MER performance and efficiency, aimed at further enhancing the learning capabilities of student models. Extensive experiments on nine benchmark datasets demonstrate that Light-MER achieves state-of-the-art performance while significantly improving inference efficiency. This highlights the strong potential of small multimodal emotion language models for future research. Code is available at https://github.com/GAIR-Lab/Light-MER.

</details>

---

### [[20_Research/Papers/强化学习/Constraint-Aware_Aggregation_for_Federated_Reinforcement_Learning_in_Microgrid_Energy_Coordination|Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination]]

![[assets/2607.12763_figure.png|800]]

- **arXiv**: [2607.12763](https://arxiv.org/abs/2607.12763)
- **PDF**: https://arxiv.org/pdf/2607.12763
- **详细分析**: [[20_Research/Papers/强化学习/Constraint-Aware_Aggregation_for_Federated_Reinforcement_Learning_in_Microgrid_Energy_Coordination|Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination]]
- **作者**: Usman Haider, Karl Mason
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《Constraint-Aware Aggregation for Federated Reinforcement Learning in Microgrid Energy Coordination》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FedRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Federated Reinforcement Learning (FedRL) enables coordination of distributed energy resources without sharing raw local data, but standard aggregation methods such as FedAvg do not account for system-level constraints, often leading to unsafe global behavior. In this work, we study constraint-aware aggregation for federated reinforcement learning in distributed energy coordination. We propose aggregation rules that incorporate both local performance and estimated constraint violation into the server-side update. Among these, a simple penalty-based rule, $w_i \propto R_i - αV_i$, consistently provides the most reliable trade-off between reward and safety, without requiring dual optimization or modifications to local training. \textcolor{black}{We evaluate our approach on DairyGridEnv, a benchmark modeling multiple farms coordinating battery storage under stochastic demand and a shared grid capacity constraint, and further assess robustness using real load-driven demand profiles from Finland and the German FIELD dataset. Across multiple seeds, penalty-based aggregation substantially reduces violations while improving reward relative to FedAvg in both synthetic and real load-driven settings.} A combined reward-violation scheme exposes a tunable trade-off via $λ$, but is less stable. These results demonstrate that lightweight aggregation strategies can substantially improve empirical safety in federated reinforcement learning while preserving standard communication protocols.

</details>

---

### [[20_Research/Papers/具身智能/Jetson-PI_Towards_Onboard_Real-Time_Robot_Control_via_Foresight-Aligned_Asynchronous_Inference|Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference]]

![[assets/2607.12659_figure.png|800]]

- **arXiv**: [2607.12659](https://arxiv.org/abs/2607.12659)
- **PDF**: https://arxiv.org/pdf/2607.12659
- **详细分析**: [[20_Research/Papers/具身智能/Jetson-PI_Towards_Onboard_Real-Time_Robot_Control_via_Foresight-Aligned_Asynchronous_Inference|Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference]]
- **作者**: Zebin Yang, Qi Wang, Yunhe Wang, Xiurui Guo, Bo Yu, Shaoshan Liu, Jiafeng Xu, Hao Dong, Meng Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Jetson-PI: Towards Onboard Real-Time Robot Control via Foresight-Aligned Asynchronous Inference》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have achieved impressive performance on diverse embodied tasks. However, deploying VLA models on low-power onboard devices, such as the Jetson Orin, remains challenging due to their high computational complexity, which leads to substantial inference latency and low control frequency. Asynchronous inference can partially mask this latency by parallelizing action execution and subsequent inference, but it introduces two critical issues: perception-execution misalignment and long reaction time. In this paper, we propose Jetson-PI, a method for efficient VLA deployment on onboard devices via Foresight-Aligned Asynchronous Correction. To address misalignment, we train a lightweight future correction module that predicts future environment representation conditioned on committed actions, enabling the action expert to directly predict actions from the future time step. To reduce reaction time, we introduce confidence-based scheduling optimization that adaptively balances VLM and action expert invocations, complemented by system-level accelerations including CUDA graph reuse, GPU-resident intermediate buffering, and flow unrolling. Extensive experiments demonstrate that Jetson-PI achieves 8.66x and 5.41x improvements in control frequency compared with naive PyTorch and vla.cpp on NVIDIA Jetson Orin, while outperforming VLASH by 14.8\% in average success rate on the LIBERO benchmark. The code of our asynchronous algorithm is available on https://github.com/PKU-SEC-Lab/Jetson-PI, and our efficient llama.cpp-based inference engine is available on https://github.com/PKU-SEC-Lab/Jetson-PI-Edge.

</details>

---

### [[20_Research/Papers/大模型/A_Learning-Rate-Gated_Failure_of_GRPO_in_a_Small_Language_and_Vision-Language_Model_Web_Agent_A_Controlled_Null_and_Its_Mechanism|A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism]]

![[assets/2607.12640_figure.png|800]]

- **arXiv**: [2607.12640](https://arxiv.org/abs/2607.12640)
- **PDF**: https://arxiv.org/pdf/2607.12640
- **详细分析**: [[20_Research/Papers/大模型/A_Learning-Rate-Gated_Failure_of_GRPO_in_a_Small_Language_and_Vision-Language_Model_Web_Agent_A_Controlled_Null_and_Its_Mechanism|A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism]]
- **作者**: Chengguang Gan, Zhixi Cai, Yunhao Liang, Hanjun Wei, Shiwen Ni, Qinghao Zhang
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.75（加权：大模型 1.35，强化学习 0.4）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《A Learning-Rate-Gated Failure of GRPO in a Small Language and Vision-Language Model Web Agent: A Controlled Null and Its Mechanism》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning with verifiable rewards, and Group Relative Policy Optimization (GRPO) in particular, is now run routinely on a supervised checkpoint in the hope of producing a stronger agent. We ask whether it adds skill to a small language and vision-language model web agent at the 4B to 8B scale, or whether it mostly reshapes behavior the supervised model already has. Across a control grid of 18 runs that varies learning rate, KL weight, seed, initialization, and clipping, no configuration credibly improves the success rate of a strong supervised baseline on tasks the agent has largely mastered. On the text track, moderate to high learning rates make it credibly worse. The null holds under paired testing, 25 evaluation seeds, 6 training seeds, changes to the recipe, both text and Set-of-Marks screenshot observations, and scaling the backbone to 8B; the credible harm is a text-track finding and is only nominal under Set-of-Marks. To show that the null reflects the setting and not a broken pipeline, we run the identical harness, reward, and recipe on tasks whose reward is reachable by sampling, and there the success rate rises by 22 points with a paired interval that excludes zero. GRPO therefore helps only when there is headroom to climb, meaning the sampled policy already succeeds more often than the greedy one. We then explain the failure. A middle learning rate degrades the agent and a high one collapses it, and the two regimes form a double dissociation: grafting localizes the degrade regime to the attention and MLP blocks, while the collapse regime cannot be traced to any single group, and the embedding change that dominates the weight movement is causally inert. At 4B, effective rank in the late layers tracks capability in both directions; at 8B the two come apart. This coupling is specific to the smaller model, so we report it as scale-dependent.

</details>

---

### [[20_Research/Papers/大模型/Can_Induced_Emotion_Bias_LLM_Behaviors_in_Sequential_Decision_Making|Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?]]

![[assets/2607.12631_figure.png|800]]

- **arXiv**: [2607.12631](https://arxiv.org/abs/2607.12631)
- **PDF**: https://arxiv.org/pdf/2607.12631
- **详细分析**: [[20_Research/Papers/大模型/Can_Induced_Emotion_Bias_LLM_Behaviors_in_Sequential_Decision_Making|Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?]]
- **作者**: Minh Khoi Ho, Zihao Zhu, Runchuan Zhu, Levina Li, Zhiwen Fan, Zhangyang Wang, Junyuan Hong
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Can Induced Emotion Bias LLM Behaviors in Sequential Decision Making?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BIG-Bench, CogBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As Large Language Models (LLMs) are increasingly deployed as autonomous agents in high-stakes domains, understanding contextual factors that may modulate their decision-making becomes critical. While LLMs are trained to perceive and resonate with users' emotions, it remains unclear whether induced emotion can influence their sequential decision-making. We investigate this question using the Iowa Gambling Task (IGT), a classic psychological paradigm for studying decision-making under uncertainty, combined with an imagination-based emotion induction procedure. We first validate the feasibility of this paradigm by confirming that LLMs can sense strong, distinguishable emotions from context and that LLM agents can learn from sequential interactions in a human-like pace. With the validated setup, we find that, different from humans, induced emotion does not significantly bias the decision dynamics of LLM agents on average. However, the effects of anger are conditioned: inducing anger makes LLM agents less sensitive to penalties for bad decisions, and in early stages of the game, anger can lower exploration, locking decisions into a few choices early. These findings reveal the subtle yet distinct effects of induced emotion on LLM decision-making compared to human behavior, and provide a tool for future research on affective modulation of LLM agents.

</details>

---

### [[20_Research/Papers/强化学习/OOD-RL-Bench_A_Benchmark_Framework_for_Out-of-Distribution_Detection_in_Reinforcement_Learning|OOD-RL-Bench: A Benchmark Framework for Out-of-Distribution Detection in Reinforcement Learning]]

![[assets/2607.12523_figure.png|800]]

- **arXiv**: [2607.12523](https://arxiv.org/abs/2607.12523)
- **PDF**: https://arxiv.org/pdf/2607.12523
- **详细分析**: [[20_Research/Papers/强化学习/OOD-RL-Bench_A_Benchmark_Framework_for_Out-of-Distribution_Detection_in_Reinforcement_Learning|OOD-RL-Bench: A Benchmark Framework for Out-of-Distribution Detection in Reinforcement Learning]]
- **作者**: Emil Mittag, Richard Dazeley, Peter Vamplew
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《OOD-RL-Bench: A Benchmark Framework for Out-of-Distribution Detection in Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OOD-RL-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable reinforcement learning (RL) agents must maintain operational integrity amidst sensor malfunctions, dynamic disturbances, and slow environmental shifts. The detection of out-of-distribution conditions is pivotal to determining when an agent's observations, transitions, or trajectory dynamics deviate from the assumptions underpinning its policy training. Current out-of-distribution (OOD) detection benchmarks typically evaluate image classifiers or static low-dimensional datasets, failing to account for the complex, action-dependent temporal structure inherent in RL trajectories. To address this gap, we present OOD-RL-Bench, a comprehensive and extensible framework designed to evaluate OOD detectors against categories of anomalies injected into RL trajectories. Detectors and anomaly injectors are integrated through shared interfaces and configuration, which allows new scoring methods and perturbation families to be evaluated without modification of the core benchmark loop. We evaluate the utility of the framework using a Deep Q-Network policy within the LunarLander-v3 environment. We assess the performance of each detector across a suite of anomaly types using matched-time AUROC, matched-time AUPRC, matched-time false-positive rate, detection delay, and segmented-onset metrics. Our analysis reveals significant performance variance across anomaly types: observation perturbations and regime switches are identified with high accuracy by several methods, while observation delay and action-conditioned dynamics remain difficult even when post-onset anomaly scores are compared against clean scores from the same timesteps. We make the framework, trained policy checkpoint, and complete results publicly available as a reproducible artefact.

</details>

---

### [[20_Research/Papers/大模型/TRACE_An_Operational_Reasoning_Schema_for_Auditable_Agentic_Commitments|TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments]]

![[assets/2607.12480_figure.png|800]]

- **arXiv**: [2607.12480](https://arxiv.org/abs/2607.12480)
- **PDF**: https://arxiv.org/pdf/2607.12480
- **详细分析**: [[20_Research/Papers/大模型/TRACE_An_Operational_Reasoning_Schema_for_Auditable_Agentic_Commitments|TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments]]
- **作者**: Edward Y. Chang, Emily J. Chang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，强化学习 0.2，世界模型 0.2）
- **关联关键词**: LLM, RL, WorldModel

#### 研究背景与动机

《TRACE: An Operational Reasoning Schema for Auditable Agentic Commitments》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TRACE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper defines TRACE (Typed Reasoning And Commitment Evidence): a typed, versioned schema for recording reasoning traces, a reference procedure for writing records against it, and one operating discipline, no durable state change without a record. The paper argues in three layers that reasoning is not in the language model: the autoregressive mechanism natively computes association; chain-of-thought and reinforcement learning inherit its limits; and the formal constructs of reasoning theory, from Socratic procedure to Pearl's ladder, are absent as machinery. The schema answers the absence with fields and tests: the TraceRecord and its causal specialization, an eight-stage reference writer, a gate-first measurement regime, the TRACE-Bench protocol, and the consumers, memory admission, plan gating, temporal regret, and verdict reuse, whose more auditable decisions are the measure of the record. A record-consumer contract states what a record guarantees and what a consumer must honor in return, making the schema an operational interface rather than a passive document. Two worked examples run in the main text: a music-lessons argument traced from sentence to typed verdict, separating association, intervention, and prescription; and a flood search-and-rescue vignette in which a predictive world model reports confident plan success that its own support and out-of-distribution scores contradict, so the record defers the commitment, requests a bounded observation, revises append-only, and clears a different branch. The vignette is illustrative, not empirical; closed-loop evaluation is left to future work, so the contribution is the schema and its contract, not a performance claim. Appendices carry the full schema, writer algorithms and cost model, clinical and policy illustrations, the benchmark protocol, convergence metrics, and usage scenarios.

</details>

---

### [[20_Research/Papers/世界模型/From_Observation_to_Insight_Mechanistic_World_Models_and_the_Quest_for_Autonomous_Discovery|From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery]]

![[assets/2607.12474_figure.png|800]]

- **arXiv**: [2607.12474](https://arxiv.org/abs/2607.12474)
- **PDF**: https://arxiv.org/pdf/2607.12474
- **详细分析**: [[20_Research/Papers/世界模型/From_Observation_to_Insight_Mechanistic_World_Models_and_the_Quest_for_Autonomous_Discovery|From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery]]
- **作者**: Ingmar Posner, Anson Lei, Bernhard Schölkopf
- **cs 子类**: cs.AI
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel

#### 研究背景与动机

《From Observation to Insight: Mechanistic World Models and the Quest for Autonomous Discovery》归入 世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in foundation models have transformed AI for Science, enabling remarkably accurate predictive performance across domains ranging from protein folding to weather forecasting. Yet prediction alone does not constitute scientific discovery. Scientific understanding depends on uncovering the reusable explanatory mechanisms that generate observations, whereas contemporary machine learning remains fundamentally organised around predictive mappings rather than explanatory structure. In this paper, we argue that scientific discovery is fundamentally a problem of knowledge organisation. To this end, we introduce Mechanistic World Models, a new design paradigm that places reusable mechanisms at the centre of representation, computation and learning. Drawing on insights from the philosophy of science, we derive the computational capabilities required for discovery, identify the design principles and inductive pressures that encourage explanatory knowledge to emerge, and formalise the anatomy of a mechanism-centric world model. Finally, we show how diverse research directions including mechanistic interpretability, causal representation learning, equation discovery and modular architectures capture complementary ingredients of this paradigm while lacking a unified framework. We propose Mechanistic World Models as a conceptual foundation and computational blueprint for moving AI beyond predictive forecasting towards autonomous scientific discovery.

</details>

---

### [[20_Research/Papers/大模型/Function-Aware_Fill-in-the-Middle_as_Mid-Training_for_Coding_Agent_Foundation_Models|Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models]]

![[assets/2607.12463_figure.png|800]]

- **arXiv**: [2607.12463](https://arxiv.org/abs/2607.12463)
- **PDF**: https://arxiv.org/pdf/2607.12463
- **详细分析**: [[20_Research/Papers/大模型/Function-Aware_Fill-in-the-Middle_as_Mid-Training_for_Coding_Agent_Foundation_Models|Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models]]
- **作者**: Yubo Wang, Jiarong Liang, Yuxuan Zhang, Xuye Liu, Cong Wei, Yuyu Zhang, Ping Nie, Wenhu Chen
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent

#### 研究背景与动机

《Function-Aware Fill-in-the-Middle as Mid-Training for Coding Agent Foundation Models》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LiveCodeBench, R2E-Gym, SWE-Bench, SWE-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents must integrate external tool returns into ongoing reasoning - a capability that standard left-to-right pretraining on code exposes only in its forward direction. We observe that the action-observation-continuation loop of a coding agent is structurally isomorphic to a function call site, where a caller binds arguments, a callee returns a value computed elsewhere, and downstream code consumes that value. This conditioning structure exists at internet scale in ordinary code. We exploit it through function-aware fill-in-the-middle (FIM) mid-training: a self-supervised objective that masks functions selected via program dependency graph analysis and a complexity-inferability double criterion. We mid-train Qwen2.5-Coder-Instruct (7B/14B) and Qwen3-8B on a 2.6B-token decontaminated corpus drawn from 968 GitHub repositories, then apply existing agentic post-training pipelines. Mid-training improves SWE-Bench-Verified by +2.8/+3.0 at 7B/14B and by +3.2 on Qwen3-8B; SWE-Bench-Lite gains are +3.7/+4.0/+5.4 on the same models. The improvement holds across two post-training pipelines (R2E-Gym, SWE-Smith) and on a non-Qwen2.5 base (Qwen3-8B with SWE-Lego). Beyond in-domain gains, mid-training also mitigates the capability erosion that agentic post-training otherwise inflicts on non-agent coding (e.g., LiveCodeBench) and non-coding tool-use benchmarks (tau-bench, BFCL): although the mid-training corpus contains Python code only, the function-call inductive bias survives post-training and yields consistent gains.

</details>

---

### [[20_Research/Papers/大模型/Isolation_as_a_First-Class_Principle_for_LLM-Agent_System_Safety_Concepts,_Taxonomy,_Challenges_and_Future_Directions|Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions]]

![[assets/2607.12406_figure.png|800]]

- **arXiv**: [2607.12406](https://arxiv.org/abs/2607.12406)
- **PDF**: https://arxiv.org/pdf/2607.12406
- **详细分析**: [[20_Research/Papers/大模型/Isolation_as_a_First-Class_Principle_for_LLM-Agent_System_Safety_Concepts,_Taxonomy,_Challenges_and_Future_Directions|Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions]]
- **作者**: Huihao Jing, Wenbin Hu, Shaojin Chen, Haochen Shi, Sirui Zhang, Hanyu Yang, Changxuan Fan, Zhongwei Xie, Hongyu Luo, Wun Yu Chan, Wei Fan, Haoran Li...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent, Security

#### 研究背景与动机

《Isolation as a First-Class Principle for LLM-Agent System Safety: Concepts, Taxonomy, Challenges and Future Directions》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Case-Bench, HarmBench, JailbreakBench, JailbreakEval, SG-Bench, Sorry-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The capability of LLM agents to function as the ``brain'' of a system fundamentally expands the scope of analysis beyond a standalone model. Consequently, safety is no longer only about input--output content alignment. It also concerns system behavior and real-world execution outcomes. However, the current literature is fragmented across attack types, applications, and benchmarks. This makes it hard to explain why failures such as prompt injection, tool misuse, and memory poisoning often share the same structural cause, and how they spread through an agent workflow. In this survey, we treat isolation as a first-class principle for LLM-agent system safety. By isolation, we refer to the separation of user inputs, tool access, execution channels, inter-agent communication, and environment-originated context. We organize the literature with a boundary-centric taxonomy of five boundaries: user-agent, agent-tool, agent-execution, agent-agent, and system-environment. This view helps identify where the loss of isolation first occurs, how compromise propagates across boundaries, and which defenses are most relevant at each interface. We also summarize cross-boundary failure paths, discuss open challenges, and outline a research agenda for isolation-by-construction in future agent systems.

</details>

---

### [[20_Research/Papers/大模型/Critic_Experience_Bank_Self-Evolving_Step-Level_Confidence_Estimation_for_LLM_Agents|Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents]]

![[assets/2607.12397_figure.png|800]]

- **arXiv**: [2607.12397](https://arxiv.org/abs/2607.12397)
- **PDF**: https://arxiv.org/pdf/2607.12397
- **详细分析**: [[20_Research/Papers/大模型/Critic_Experience_Bank_Self-Evolving_Step-Level_Confidence_Estimation_for_LLM_Agents|Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents]]
- **作者**: Yaopei Zeng, Congchao Wang, JianHang Chen, Nan Wang, Yurui Chang, Lu Lin
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Critic Experience Bank: Self-Evolving Step-Level Confidence Estimation for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents act in external environments where each action changes the state that later decisions condition on, and where a single wrong step can waste interaction budget or trigger irreversible side effects long before the final failure is observed. Reliable deployment therefore requires \emph{step-level confidence estimation}: a calibrated probability that each proposed action is productive, available \emph{before} the action is executed. Existing LLM confidence estimators are designed to score a response from the given prompt, but agent confidence also depends on execution consequences: whether similar actions in similar situations actually advanced the task after the environment responded. We introduce the \method (\methodshort), a self-evolving critic framework in which an LLM critic accumulates evidence from its own past judgments and their observed consequences. After each trajectory, a hindsight LLM that sees the full execution feedback votes on whether each step was productive. The resulting pseudo-labels populate a memory bank from which related productive and unproductive experiences are retrieved into the critic's prompt whenever a similar step recurs. \methodshort requires no training and uses no ground truth step labels. Across three agent benchmarks and three critic backbones, \methodshort attains the best calibration (ECE and Brier) and ranking (AUC) in every dataset--critic combination, reducing ECE by up to $54\%$ relative to the strongest training-free baseline.

</details>

---

### [[20_Research/Papers/大模型/PM-Bench_Evaluating_Prospective_Memory_in_LLM_Agents|PM-Bench: Evaluating Prospective Memory in LLM Agents]]

![[assets/2607.12385_figure.png|800]]

- **arXiv**: [2607.12385](https://arxiv.org/abs/2607.12385)
- **PDF**: https://arxiv.org/pdf/2607.12385
- **详细分析**: [[20_Research/Papers/大模型/PM-Bench_Evaluating_Prospective_Memory_in_LLM_Agents|PM-Bench: Evaluating Prospective Memory in LLM Agents]]
- **作者**: Genglin Liu, Saadia Gabriel
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《PM-Bench: Evaluating Prospective Memory in LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PM-Bench, PMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A significant challenge in agentic AI is prospective memory: the ability to execute an intention at a specific future cue or state while other activities are ongoing. We introduce PM-Bench, a text-based benchmark for measuring prospective memory capabilities in modern LLM agents. Inspired by the Virtual Week paradigm from cognitive science, PM-Bench evaluates how well LLM agents maintain user intentions, execute delayed intentions, and monitor latent environment changes. Over the course of a simulated seven-day week, agents must continue an ongoing activity while deciding whether any deferred task is due. We compare eight state-of-the-art LLMs on PM-Bench under eight different agent configurations. PM-Bench proves challenging across all settings: the best method, a GPT-5.4 agent, reaches only 65.1\% F1 score under our evaluation. Furthermore, no single strategy for improving prospective memory dominates across models. We release PM-Bench as a controlled testbed for diagnosing these failures and developing training or inference-time interventions that support reliable prospective behavior.

</details>

---

### [[20_Research/Papers/大模型/How_Many_Tasks_Are_Enough_for_Agent_Benchmark_Decisions_A_Replay_Analysis_of_Public_LLM_Agent_Benchmarks|How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks]]

![[assets/2607.12338_figure.png|800]]

- **arXiv**: [2607.12338](https://arxiv.org/abs/2607.12338)
- **PDF**: https://arxiv.org/pdf/2607.12338
- **详细分析**: [[20_Research/Papers/大模型/How_Many_Tasks_Are_Enough_for_Agent_Benchmark_Decisions_A_Replay_Analysis_of_Public_LLM_Agent_Benchmarks|How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks]]
- **作者**: Wei-Jung Huang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《How Many Tasks Are Enough for Agent Benchmark Decisions? A Replay Analysis of Public LLM Agent Benchmarks》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AppWorld, Cer-Eval, MT-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent benchmarks often compare two agents after all tasks have run, but costly evaluations make partial runs tempting. A task fraction alone does not show whether a partial run supports the same pairwise conclusion as the completed benchmark. We study this question by replaying completed public task-level records from SWE-bench, AppWorld, and tau-bench. A partial budget counts as enough only when it supports the completed benchmark's decision, covers required task groups, and leaves no more than a target fraction of comparisons unresolved. The required task fraction varies sharply. At the strict 0 percentage point threshold on a 5 percentage point budget grid, AppWorld first meets all targets at 15 percent, tau-bench at 25 percent, and SWE-bench Verified at 90 percent; SWE-bench Lite does not meet all targets by 95 percent under the primary coverage rule. Partial-evaluation reports should state how much one agent must outperform another, how tasks are selected, what coverage rule is required, what decision rule is used, and how many comparisons may remain unresolved.

</details>

---

### [[20_Research/Papers/大模型/Track,_Rank,_Crack_Epistemic_Working_Memory_Scales_Multi-Hop_Reasoning_in_Language_Agents|Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents]]

![[assets/2607.12267_figure.png|800]]

- **arXiv**: [2607.12267](https://arxiv.org/abs/2607.12267)
- **PDF**: https://arxiv.org/pdf/2607.12267
- **详细分析**: [[20_Research/Papers/大模型/Track,_Rank,_Crack_Epistemic_Working_Memory_Scales_Multi-Hop_Reasoning_in_Language_Agents|Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents]]
- **作者**: Ning Liu
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Track, Rank, Crack: Epistemic Working Memory Scales Multi-Hop Reasoning in Language Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HotpotQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language agents that interleave reasoning and tool use degrade sharply as reasoning chains lengthen, even when each individual step is easy. We trace this to context dilution: an agent's investigative state (what it has confirmed, what it suspects, and what it still needs) lives only implicitly in a growing context window, where early discoveries are buried under later retrievals. We introduce SLEUTH, which makes this state explicit and actionable through a structured epistemic working memory: the agent maintains Confirmed Facts grounded to sources, Active Hypotheses ranked by evidence, and Open Questions that directly drive its next action. Across five multi-hop benchmarks and five established baselines, SLEUTH's advantage grows with difficulty, from +5 points on HotpotQA to +11 on 4-hop chains, surpassing Reflexion without multiple episodes. Analyzing where the remaining gap lies, we identify the evidence sufficiency problem: agents often find the answer but fail to commit, exhausting their budget on needless verification. A lightweight commitment trigger fixes this, but only when the agent already maintains structured state: the identical trigger applied to an unstructured agent yields no improvement, isolating organized epistemic state as the necessary condition for effective commitment. Finally, enforcing protocol adherence on a weaker model recovers up to +19 points on the hardest problems, showing that how an agent organizes its reasoning, not raw model capability, is the active ingredient for scaling multi-hop reasoning.

</details>

---

### [[20_Research/Papers/大模型/Fin-Analyst_at_FinMMEval_2026_Task_3_A_Live_Hybrid_Trading_Agent_with_LLM_Specialists_and_Rule-Based_Signals|Fin-Analyst at FinMMEval 2026 Task 3: A Live Hybrid Trading Agent with LLM Specialists and Rule-Based Signals]]

![[assets/2607.12233_figure.png|800]]

- **arXiv**: [2607.12233](https://arxiv.org/abs/2607.12233)
- **PDF**: https://arxiv.org/pdf/2607.12233
- **详细分析**: [[20_Research/Papers/大模型/Fin-Analyst_at_FinMMEval_2026_Task_3_A_Live_Hybrid_Trading_Agent_with_LLM_Specialists_and_Rule-Based_Signals|Fin-Analyst at FinMMEval 2026 Task 3: A Live Hybrid Trading Agent with LLM Specialists and Rule-Based Signals]]
- **作者**: Mohotarema Rashid, Lingzi Hong, Junhua Ding, K. S. M. Tozammel Hossain
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Fin-Analyst at FinMMEval 2026 Task 3: A Live Hybrid Trading Agent with LLM Specialists and Rule-Based Signals》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：FinMMEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) trading agents show promising performance in equity markets, yet remain narrowly focused on US equities with little evidence from live deployment. We present Fin-Analyst, a hybrid agent for FinMMEval 2026 Task 3: an eight-specialist LLM pipeline over news, SEC filings, fundamentals, analyst forecasts, technical indicators, and social sentiment, aggregated by a Meta-Agent for Tesla (TSLA), and a lightweight rule based three-signal vote for Bitcoin (BTC). On the final official leaderboard (accessed 2026-07-05), Fin-Analyst ranks first of all agents on TSLA with a +13.51% return, +28.33 points over Buy-and-Hold (Sharpe 4.10, 88% win rate), while the BTC vote ends flat yet well above a sharply falling baseline. Relative to the interim performance, the asset ranking reversed, indicating that short live windows yield volatility-sensitive rankings. Ablation identifies event-driven 8-K disclosures as the most influential TSLA signal. Error analysis shows that the memoryless agents repeat wrong calls for days at a time, and that the fixed-threshold BTC rules lost money by trading on noise in a sideways market while the LLM pipeline gained under similar conditions, motivating a memory-aware, LLM-based successor for both assets.

</details>

---

### [[20_Research/Papers/大模型/Rethinking_the_Evaluation_of_Harness_Evolution_for_Agents|Rethinking the Evaluation of Harness Evolution for Agents]]

![[assets/2607.12227_figure.png|800]]

- **arXiv**: [2607.12227](https://arxiv.org/abs/2607.12227)
- **PDF**: https://arxiv.org/pdf/2607.12227
- **详细分析**: [[20_Research/Papers/大模型/Rethinking_the_Evaluation_of_Harness_Evolution_for_Agents|Rethinking the Evaluation of Harness Evolution for Agents]]
- **作者**: Yike Wang, Huaisheng Zhu, Zhengyu Hu, Yige Yuan, Zhengyu Chen, Shakti Senthil, Hannaneh Hajishirzi, Yulia Tsvetkov, Pradeep Dasigi, Teng Xiao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Rethinking the Evaluation of Harness Evolution for Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Terminal-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We revisit the evaluation of automatic harness evolution for LLM agents. Existing harness evolution methods use unit test cases to search for harness configurations and then report final performance on the same public benchmark. This protocol raises two fundamental concerns. First, harness evolution is itself an iterative search procedure that repeatedly evaluates and revises candidate harnesses using task feedback. As in agentic test-time scaling, it should therefore be compared with simple task-level search baselines under matched feedback and inference budgets to determine whether its gains arise from improved harness design or from additional search alone. Second, because the search and the final evaluation share the same benchmark, the reported gains risk overfitting to that specific task set. To address these concerns, we conduct an extensive evaluation comparing harness evolution with simple test-time scaling and discovery baselines under comparable feedback and inference budgets, and also evaluate evolved harnesses on held-out tasks to assess whether the discovered improvements generalize. Experiments on Terminal-Bench 2.1 with GPT-5.4 and Claude Opus 4.6 show that automatic harness evolution does not consistently outperform simple test-time scaling methods and exhibits limited generalization. Our results raise important questions about the effectiveness of automatic harness evolution and highlight the need for fairer evaluation protocols and benchmarks for automatic harness design. Our code is available at https://github.com/rethinking-harness-evolution.

</details>

---

### [[20_Research/Papers/大模型/RCWT_Measuring_Task-Budget_Displacement_from_Coordination_Content_in_LLM_Calls|RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls]]

![[assets/2607.12216_figure.png|800]]

- **arXiv**: [2607.12216](https://arxiv.org/abs/2607.12216)
- **PDF**: https://arxiv.org/pdf/2607.12216
- **详细分析**: [[20_Research/Papers/大模型/RCWT_Measuring_Task-Budget_Displacement_from_Coordination_Content_in_LLM_Calls|RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls]]
- **作者**: Brenda Lelis, Rodrigo Cabral-Carvalho
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《RCWT: Measuring Task-Budget Displacement from Coordination Content in LLM Calls》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent and memory-augmented LLM systems often place coordination content, shared state, prior discussion, tool outputs, summaries, and role instructions, inside the same finite prompt used for the current task. This creates a practical allocation problem: every token spent on coordination is unavailable to task instructions or evidence when a call is assembled under a fixed context budget. We introduce the Roundtable Context Window Test (RCWT), a controlled protocol for measuring this task-budget displacement effect. RCWT varies coordination content while controlling total budget, position order, task family, and scoring. In the main context-dependent recall task at $W=4096$, three commercial models remain near baseline through moderate overhead and then degrade sharply once residual reference evidence falls to a few hundred tokens. Window-scaling summaries are consistent with a task-specific residual-budget interpretation rather than a fixed percentage threshold, but we treat this as descriptive evidence rather than a universal law. To test whether the fixed-budget cliff persists when task evidence remains intact, we add an intact-task ablation: the full task/reference block is kept present while coordination tokens increase by expanding total prompt length. In that setting, all tested calls return every scored field correctly across GPT-4.1-mini, Claude Haiku 4.5, and Gemini 2.5 Flash up to a 95\% coordination ratio. This ablation narrows the claim: the main RCWT cliff is best read as task-budget displacement, not as proof that coordination volume alone causes semantic interference in the original open-ended task. RCWT is therefore a measurement primitive for context-allocation budgeting, not a complete theory of multi-agent benefit or session-level coordination.

</details>

---

### [[20_Research/Papers/大模型/Cost-Governed_RAG_Unified_Per-Tenant_Cost_Attribution_Across_Retrieval_and_Generation_in_Multi-Tenant_LLM_Systems|Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems]]

![[assets/2607.12188_first_page.png|800]]

- **arXiv**: [2607.12188](https://arxiv.org/abs/2607.12188)
- **PDF**: https://arxiv.org/pdf/2607.12188
- **详细分析**: [[20_Research/Papers/大模型/Cost-Governed_RAG_Unified_Per-Tenant_Cost_Attribution_Across_Retrieval_and_Generation_in_Multi-Tenant_LLM_Systems|Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems]]
- **作者**: Navnit Shukla
- **cs 子类**: cs.AI, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Systems

#### 研究背景与动机

《Cost-Governed RAG: Unified Per-Tenant Cost Attribution Across Retrieval and Generation in Multi-Tenant LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise Retrieval-Augmented Generation (RAG) deployments face a critical governance gap: while LLM generation cost is metered per token, the retrieval layer - vector memory, similarity compute, and embedding API calls - remains an unattributed shared cost, enabling invisible cross-subsidization among tenants. We present Cost-Governed RAG, an architecture that integrates a codebook-oblivious vector index (TurboVec) with a multi-tenant LLM governance gateway, creating a unified observability stack where embedding, retrieval, and generation costs are jointly attributable per tenant. The architecture exploits TurboVec's deterministic, closed-form memory formula to enable near-exact per-tenant retrieval cost calculation - a property unavailable in graph-based indexes with non-linear memory overhead. Deployed on Snowpark Container Services within a cloud data platform's governance boundary, the system achieves 99.96% end-to-end cost attribution accuracy across 100 simulated tenants (10M vectors, log-normal size distribution) with telemetry overhead below 0.04% of query latency. The architecture reduces retrieval infrastructure cost by 3.1-9.0x compared to managed vector database services under the pricing assumptions detailed in Section IV. We formalize a three-layer cost model and demonstrate that codebook-oblivious quantization enables deterministic per-tenant cost attribution while also removing the shared-codebook leakage surface present in trained quantizers - the latter observation being exploratory and subject to the limitations described in Section VII.

</details>

---

### [[20_Research/Papers/具身智能/GaitSpan_Growing_Humanoid_Locomotion_from_Walking_to_Running|GaitSpan: Growing Humanoid Locomotion from Walking to Running]]

![[assets/2607.12114_figure.png|800]]

- **arXiv**: [2607.12114](https://arxiv.org/abs/2607.12114)
- **PDF**: https://arxiv.org/pdf/2607.12114
- **详细分析**: [[20_Research/Papers/具身智能/GaitSpan_Growing_Humanoid_Locomotion_from_Walking_to_Running|GaitSpan: Growing Humanoid Locomotion from Walking to Running]]
- **作者**: Kwan-Yee Lin, Zilin Wang, Janelle J. Liu, Stella X. Yu
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《GaitSpan: Growing Humanoid Locomotion from Walking to Running》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A humanoid that can walk should not relearn locomotion from scratch to jog or run. Yet current approaches often obtain gait diversity by prescribing gait schedules, imitating motion clips, training experts to switch between or distilling skills into one policy. These strategies can produce impressive behaviors, but offer limited flexibility across continuous speed commands, terrains, and morphologies. We study skill growth with GaitSpan, a framework that expands a pretrained, basic walking policy into faster locomotion. It treats walking as a seed skill: reusable motor structure for balance, support, body coordination, and contact transition that can be regenerated at new rhythms, extended into longer/higher strides, and corrected by residual adaptation. This expansion has three aspects: 1) rhythm generation, which modulates the frozen walking policy with multiple internal clocks and learns command-conditioned combinations of the resulting canonical actions; 2) stride shaping, which rewards dynamic locomotion patterns appropriate for higher commanded speeds using a physically grounded objective inspired by spring-loaded inverted pendulum dynamics; and 3) residual adaptation, which captures motion details not accounted for by rhythm generation or stride shaping. GaitSpan is the first to deliver a single command-conditioned humanoid policy that spans walking, jogging, and running-like regimes covering a continuous speed range, transfers across morphologies, and deploys zero-shot on unseen sim-to-sim, and real-world terrains. Compared with baselines either trained with multi-experts or imitation from humans, it learns faster and achieves stronger gait performance.

</details>

---

### [[20_Research/Papers/大模型/Operationalising_Multi-Dimensional_Evaluation_for_Conversational_Agents_A_Scalable,_Governed_Pipeline_with_Selective_Re-evaluation_and_Model|Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking]]

![[assets/2607.12085_first_page.png|800]]

- **arXiv**: [2607.12085](https://arxiv.org/abs/2607.12085)
- **PDF**: https://arxiv.org/pdf/2607.12085
- **详细分析**: [[20_Research/Papers/大模型/Operationalising_Multi-Dimensional_Evaluation_for_Conversational_Agents_A_Scalable,_Governed_Pipeline_with_Selective_Re-evaluation_and_Model|Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking]]
- **作者**: Niranjan Kumar M, Balaji Nagarajan, Karthik Nair, Faysal Satter, Nithin Surendran
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Operationalising Multi-Dimensional Evaluation for Conversational Agents: A Scalable, Governed Pipeline with Selective Re-evaluation and Model Benchmarking》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlpacaEval, G-Eval, LightEval, M-RewardBench, MT-Bench, RewardBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating retail conversational agents requires methods beyond lexical-overlap metrics to assess intent alignment, factuality, helpfulness, clarity, tone, and overall response quality. Although LLM-as-a-judge methods provide scalable alternatives to human evaluation, production deployment introduces challenges in governance, reproducibility, cost, schema consistency, traceability, and reliability. We present GenAI Evaluation, a governed, configuration-driven pipeline for large-scale evaluation of retail conversational systems. It processes production chatbot logs through normalization, sharding, asynchronous execution, and schema-constrained LLM scoring. The framework evaluates helpfulness, truthfulness, clarity, tone alignment, and translation-specific dimensions. Selective re-evaluation processes only incomplete, malformed, or schema-invalid records, while schema locking, versioned configurations, validation logs, and record-level provenance support auditability. The framework processes approximately 50,000 records daily and has evaluated more than two million interactions. Validation used 12,980 stratified-random human-labeled records from four trained annotators. Classification covered 14 intents, 156 sub-intents, 18 major domains, and 129 sub-domains. The pipeline achieved a macro F1 score of 0.93 and 89% human-acceptability accuracy for translation.

</details>

---

### [[20_Research/Papers/具身智能/Enabling_24-hour_Agricultural_Robotics_Unsupervised_Day-to-Night_Cross-Modal_Image_Translation_for_Nighttime_Visual_Navigation|Enabling 24-hour Agricultural Robotics: Unsupervised Day-to-Night Cross-Modal Image Translation for Nighttime Visual Navigation]]

![[assets/2607.12065_figure.png|800]]

- **arXiv**: [2607.12065](https://arxiv.org/abs/2607.12065)
- **PDF**: https://arxiv.org/pdf/2607.12065
- **详细分析**: [[20_Research/Papers/具身智能/Enabling_24-hour_Agricultural_Robotics_Unsupervised_Day-to-Night_Cross-Modal_Image_Translation_for_Nighttime_Visual_Navigation|Enabling 24-hour Agricultural Robotics: Unsupervised Day-to-Night Cross-Modal Image Translation for Nighttime Visual Navigation]]
- **作者**: Robel Mamo, Rajitha de Silva, Grzegorz Cielniak, Taeyeong Choi
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Enabling 24-hour Agricultural Robotics: Unsupervised Day-to-Night Cross-Modal Image Translation for Nighttime Visual Navigation》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While visual navigation has been extensively studied in agricultural robotics, most existing systems assume daytime conditions. In fact, deploying autonomous robots at night offers significant advantages, including 24-hour crop and soil monitoring, fruit harvesting, and nocturnal pest detection. Modern vision-based systems, however, rely heavily on large-scale well-annotated image datasets, which remains challenging to obtain for nighttime operation scenarios. To address this, we propose an unsupervised image translation framework that converts daytime plant-row RGB images into near-infrared (NIR) nighttime counterparts without requiring pixel-to-pixel supervision. This enables the direct reuse of daytime semantic labels for training nighttime perception models. In particular, by incorporating a pre-trained Contrastive Language-Image Pre-training (CLIP) model, the proposed framework is designed to preserve semantic consistency during day-to-night translation. Additionally, a visibility mask is introduced to account for the limited effective range of NIR illumination in nighttime scenes. We conduct comparative evaluations with state-of-the-art image translation baselines and demonstrate higher image qualities, as supported by improved performance in downstream semantic segmentation for nighttime visual navigation. For evaluation, we utilize AgriNight--a novel dataset comprising 428 daytime and 549 nighttime images collected using night-vision-equipped mobile robots in agricultural fields and manually annotated with pixel-wise semantic labels--and introduce it as the first benchmark for nighttime agricultural visual navigation. We also perform real-time autonomous navigation experiments with a physical robot operating at night. The data and code are available at: https://github.com/mamorobel/AgriNight.

</details>

---

### [[20_Research/Papers/其他/Designing_Agent-Ready_Websites_for_AI_Web_Agents_A_Framework_for_Machine_Readability,_Actionability,_and_Decision_Reliability|Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability]]

![[assets/2607.12056_figure.png|800]]

- **arXiv**: [2607.12056](https://arxiv.org/abs/2607.12056)
- **PDF**: https://arxiv.org/pdf/2607.12056
- **详细分析**: [[20_Research/Papers/其他/Designing_Agent-Ready_Websites_for_AI_Web_Agents_A_Framework_for_Machine_Readability,_Actionability,_and_Decision_Reliability|Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability]]
- **作者**: Said Elnaffar, Farzad Rashidi
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: Agent

#### 研究背景与动机

《Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine Readability, Actionability, and Decision Reliability》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Online shopping is increasingly shifting toward a model in which AI agents independently search for products, compare options, evaluate constraints, and carry out parts of the purchasing process for users. Website design must now support both human and agent-mediated interaction. This paper introduces the agent-ready website, a design framework for enhancing the readability, interpretability, verifiability, and actionability of e-commerce platforms for AI agents. Existing web design, SEO, and generative engine optimization (GEO) metrics do not fully assess a website's capacity for agent-mediated interaction. The proposed framework is structured around three dimensions agent interpretability, agent executability, and agent decision reliability supported by features such as machine readability, semantic clarity, agent actionability, and contextual decision-reliability signals. The framework is evaluated through a controlled experiment comparing a human-oriented baseline and an agent-ready version of an identical website prototype, with identical catalogs, pricing, stock, and shopping workflows. The evaluation involved five tasks, three browser-agent models (GPT-4.1, Gemini-2.5 Flash, and Grok-4 Fast), and 300 runs, measuring PASS,PARTIAL,FAIL outcomes, strict and functional success rates, error patterns, step counts, and token consumption. The agent-ready website achieved 134 PASS runs out of 150 versus 74 out of 150 for the baseline (strict success rates of 89.3% vs. 49.3%), with the largest gains in product detail extraction, comparison, and multi-constraint selection. It also reduced PARTIAL outcomes from 43 to 3 and lowered the average step count from 9.31 to 6.49. These results provide preliminary evidence that enhanced structural clarity, action cues, evidence signals, and temporal validity indicators can substantially improve the reliability and efficiency of AI browser agents.

</details>

---

### [[20_Research/Papers/强化学习/Calibration-First_Reward-Component_Auditing_for_Reinforcement_Learning_Control_in_Smart_Greenhouses|Calibration-First Reward-Component Auditing for Reinforcement Learning Control in Smart Greenhouses]]

![[assets/2607.11959_figure.png|800]]

- **arXiv**: [2607.11959](https://arxiv.org/abs/2607.11959)
- **PDF**: https://arxiv.org/pdf/2607.11959
- **详细分析**: [[20_Research/Papers/强化学习/Calibration-First_Reward-Component_Auditing_for_Reinforcement_Learning_Control_in_Smart_Greenhouses|Calibration-First Reward-Component Auditing for Reinforcement Learning Control in Smart Greenhouses]]
- **作者**: Yuhui Bie, Guowei Xu, Yaojun Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《Calibration-First Reward-Component Auditing for Reinforcement Learning Control in Smart Greenhouses》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ajagekar2023RobustDRL, Bekkemoen2024XRL, Garcia2015SafeRL, GreenLight-Gym, GreenLightGym, XRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Greenhouse reinforcement learning can test climate-control ideas at a speed and scale that is difficult to achieve with crop experiments alone. For smart-greenhouse control, however, a single simulator return is not enough: a grower or control engineer also needs to know when the policy heats, enriches CO2, vents, manages humidity, deploys screens, or uses lamps.We propose a reproducible calibration-first reward audit framework that keeps named greenhouse-control reward components comparable across simulator training, facility-adapted rollouts, logged Autonomous Greenhouse Challenge records, and actuator-rule distillation. In GreenLight-Gym, the framework decomposes the scalar reward into conditional temperature, CO2, humidity and vapor-pressure-deficit, screen, and actuation-proxy terms; adapts GreenLight to the second Autonomous Greenhouse Challenge logged climate traces; and scores the same components on logged greenhouse data.

</details>

---

### [[20_Research/Papers/大模型/Graph-Constrained_Policy_Learning_for_Extreme_Clinical_Code_Prediction|Graph-Constrained Policy Learning for Extreme Clinical Code Prediction]]

![[assets/2607.11954_first_page.png|800]]

- **arXiv**: [2607.11954](https://arxiv.org/abs/2607.11954)
- **PDF**: https://arxiv.org/pdf/2607.11954
- **详细分析**: [[20_Research/Papers/大模型/Graph-Constrained_Policy_Learning_for_Extreme_Clinical_Code_Prediction|Graph-Constrained Policy Learning for Extreme Clinical Code Prediction]]
- **作者**: Amritpal Singh, Sebastian Torres, Khawar Shakeel, Syed Ahmad Chan Bukhari
- **cs 子类**: cs.AI, cs.IR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Graph-Constrained Policy Learning for Extreme Clinical Code Prediction》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clinical code prediction maps unstructured discharge summaries to ICD-10-CM leaf codes in a large, sparse, and deeply hierarchical label space. Most systems treat the task as flat multi-label classification, scoring codes independently and providing limited training signal for rare labels. We propose a graph-constrained traversal policy that formulates ICD prediction as a finite-horizon decision process over a pruned code hierarchy. A single language model descends the graph level by level, selecting valid child nodes until billable leaf codes are reached. This converts extreme multi-label prediction into sparse, hierarchy-aware subset decisions while guaranteeing structurally valid outputs. On MIMIC-IV discharge summaries, our best supervised policy, SFT-1+, achieves 0.709 micro-F1 on a curated 50-code subset and 0.527 micro-F1 on the full 15,761-code space, outperforming flat baselines including CAML, LAAT, and PLM-ICD. In the full setting, SFT-1+ improves over the strongest flat baseline by 0.044 micro-F1 and 0.157 macro-F1, suggesting that graph-constrained decomposition mitigates the rare-code bottleneck. A controlled factorial study evaluates architecture, training algorithm, and data budget. Across both scales, one shared policy matches a three-specialist cascade while avoiding its context-window overflow on 28-32% of full-space test notes. Increasing supervised trajectory data is the only intervention that consistently improves performance, while GRPO reinforcement learning provides no benefit over supervised continuation with matched data. These results show that simple graph-constrained policy learning can outperform more complex flat, cascaded, and reinforcement-learning alternatives for extreme clinical code prediction.

</details>

---

### [[20_Research/Papers/大模型/Sensitivity_to_Subjective_Expected_Utility_Maximization_A_Methodological_Study,_with_an_Illustrative_Application_to_LLM_Decision-Making|Sensitivity to Subjective Expected Utility Maximization: A Methodological Study, with an Illustrative Application to LLM Decision-Making]]

![[assets/2607.11920_figure.png|800]]

- **arXiv**: [2607.11920](https://arxiv.org/abs/2607.11920)
- **PDF**: https://arxiv.org/pdf/2607.11920
- **详细分析**: [[20_Research/Papers/大模型/Sensitivity_to_Subjective_Expected_Utility_Maximization_A_Methodological_Study,_with_an_Illustrative_Application_to_LLM_Decision-Making|Sensitivity to Subjective Expected Utility Maximization: A Methodological Study, with an Illustrative Application to LLM Decision-Making]]
- **作者**: Jeff Helzner
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Sensitivity to Subjective Expected Utility Maximization: A Methodological Study, with an Illustrative Application to LLM Decision-Making》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating decisions made under uncertainty is hard when labeled outcomes are scarce, costly, or confounded with luck. We treat subjective expected utility (SEU) maximization as a stated standard and define a graded measure -- SEU sensitivity -- of an agent's conformity to it. The vehicle is a softmax choice model with a sensitivity parameter $α$ on SEU-valued alternatives; the contribution is a sequence of identifiability results for $α$ and for belief and utility parameters $(β, δ)$, validated in Stan via prior predictive checks, parameter recovery, and simulation-based calibration (SBC), with finite-sample caveats intact. In the uncertain-choice-only model $m_0$, $α$ is identifiable given the expected-utility vector $η$ and sharply recovered, while $(β, δ)$ are only weakly informed: the posterior barely contracts and concentrates on a $β$-$δ$ trade-off. In the extended model $m_1$, $δ$ becomes identifiable in principle via a $β$-free risky block, but its practical recovery gain at realistic sample sizes is negligible (matched-count CI-width reduction under 1%), and that block yields no detected $α$-precision gain at matched choice count. These are two distinct phenomena: for $δ$, identifiability does not imply precise estimability at realistic $n$; for $α$, identifiability is silent about what governs finite-$n$ precision. Marginal SBC passes for both models even where the joint posterior is weakly informed -- a demarcation we make precise. A two-by-two application (GPT-4o and Claude 3.5 Sonnet, each on insurance-claims triage and Ellsberg-style urns, with sampling temperature as the lever) runs end-to-end on real LLM choice data, detecting a structured comparative $α$ effect in two of four cells.

</details>

---

### [[20_Research/Papers/强化学习/In-Context_Reinforcement_Learning_under_Non-Stationarity_A_Survey|In-Context Reinforcement Learning under Non-Stationarity: A Survey]]

![[assets/2607.11906_figure.png|800]]

- **arXiv**: [2607.11906](https://arxiv.org/abs/2607.11906)
- **PDF**: https://arxiv.org/pdf/2607.11906
- **详细分析**: [[20_Research/Papers/强化学习/In-Context_Reinforcement_Learning_under_Non-Stationarity_A_Survey|In-Context Reinforcement Learning under Non-Stationarity: A Survey]]
- **作者**: A Run, Ziluo Ding
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《In-Context Reinforcement Learning under Non-Stationarity: A Survey》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ICRL, Meta-RL, NS-Gym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The development of decision-pretrained transformers, algorithm distillation, long-context meta-RL, and retrieval-augmented agents has renewed interest in in-context reinforcement learning (ICRL): the ability of a pretrained or fine-tuned decision model to infer latent task rules and improve future behavior from interaction context, without test-time parameter updates. This line of work asks when trial-and-error evidence, rewards, transitions, demonstrations, feedback, or retrieved experience can make learning-like computation happen inside the context window. However, existing surveys of ICRL mainly organize the field around pretraining objectives, architectures, context formats, evaluation protocols, and theoretical mechanisms, while the non-stationary setting remains comparatively underexamined. In changing environments, accumulated context is not merely more evidence about a fixed task: the reward specification, transition kernel, observation channel, action interface, constraint model, or demonstration and memory distribution can fall out of alignment with the current regime. Previously useful context can therefore become stale, misleading, or useful again when an old regime returns. We survey non-stationary ICRL as the problem of adapting through context while deployed policy parameters remain fixed: the policy must infer both the current decision rule and which parts of its accumulated evidence still support that rule. We define non-stationary ICRL, relate it to meta-RL, decision sequence modeling, retrieval-augmented RL, value- and model-aware ICRL, and reward-feedback agents, and organize the literature along three questions: what changes, how the change unfolds, and how observable the change is to the agent.

</details>

---

### [[20_Research/Papers/大模型/FAIR_GraphRAG_A_Retrieval-Augmented_Generation_Approach_for_Semantic_Data_Analysis|FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis]]

![[assets/2607.11464_figure.png|800]]

- **arXiv**: [2607.11464](https://arxiv.org/abs/2607.11464)
- **PDF**: https://arxiv.org/pdf/2607.11464
- **详细分析**: [[20_Research/Papers/大模型/FAIR_GraphRAG_A_Retrieval-Augmented_Generation_Approach_for_Semantic_Data_Analysis|FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis]]
- **作者**: Marlena Flüh, Soo-Yon Kim, Carolin Victoria Schneider, Sandra Geisler
- **cs 子类**: cs.AI, cs.CL, cs.IR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Systems

#### 研究背景与动机

《FAIR GraphRAG: A Retrieval-Augmented Generation Approach for Semantic Data Analysis》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-Augmented Generation (RAG) addresses the limitations of Large Language Models (LLMs) when providing responses to domain-specific questions. Graph-based RAG approaches, such as GraphRAG, enhance retrieval by capturing semantic relationships within knowledge graphs (KGs). While the FAIR principles (Findability, Accessibility, Interoperability, and Reusability) are becoming prevalent for scientific data management, especially in complex domains such as medicine, existing RAG approaches lack a structured FAIRification of the underlying knowledge resources. This lack limits their potential for FAIR information retrieval in these domains. To address this gap, we introduce FAIR GraphRAG, a novel framework that integrates FAIR Digital Objects (FDOs) as the fundamental units of a graph-based retrieval system. Each graph node represents an FDO that incorporates core data, metadata, persistent identifiers, and semantic links. We leverage LLMs to support schema construction and automated extraction of content and metadata from data sources. The framework was co-designed by physicians and computer scientists to ensure technical and clinical relevance. We apply FAIR GraphRAG to a biomedical dataset in gastroenterology, demonstrating its applicability to RNA-sequencing data. Beyond ensuring adherence to the FAIR principles, FAIR GraphRAG significantly improves question answering accuracy, coverage, and explainability, particularly for complex queries involving metadata and ontology links. This work shows the feasibility of combining FAIR data practices with graph-based retrieval techniques. We see potential for applying our approach to other specialized fields such as education and business.

</details>

---

### [[20_Research/Papers/具身智能/ABot-AgentOS_A_General_Robotic_Agent_OS_with_Lifelong_Multi-modal_Memory|ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory]]

![[assets/2607.10350_figure.png|800]]

- **arXiv**: [2607.10350](https://arxiv.org/abs/2607.10350)
- **PDF**: https://arxiv.org/pdf/2607.10350
- **详细分析**: [[20_Research/Papers/具身智能/ABot-AgentOS_A_General_Robotic_Agent_OS_with_Lifelong_Multi-modal_Memory|ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory]]
- **作者**: Jiayi Tian, Shiao Liu, Yuting Xu, Jia Lu, Zihao Guan, Honglin Han, Di Yang, Minqi Gu, Yifei Qian, Tianlin Zhang, Yanqing Zhu, Zeqian Ye...
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.6（加权：具身智能 0.9，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ABot-AgentOS: A General Robotic Agent OS with Lifelong Multi-modal Memory》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EM-EQA, EmbodiedWorldBench, NExT-QA, OSWorld, OpenEQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent VLM and VLA systems have improved robotic perception and action prediction, yet long-horizon embodied agents still require a general runtime layer for reasoning, memory, tool use, verification, and cross-embodiment execution. We present ABot-AgentOS, a general robotic Agent Operating System that sits above low-level controllers and provides a deliberative agent layer for scene-conditioned planning, context-isolated skill execution, multi-stage verification, multi-modal memory, and edge-cloud collaboration. To evaluate such systems, we introduce EmbodiedWorldBench, an executable benchmark with 16 indoor, outdoor, and hybrid scenes, four difficulty levels, and over 200 tasks involving navigation, object search, NPC dialogue, dynamic events, and trace-grounded scoring. ABot-AgentOS further introduces Universal Multi-modal Graph Memory, a persistent source-grounded substrate that converts dialogue, visual observations, spatial context, temporal relations, and task traces into typed nodes and edges. A failure-driven self-evolution loop converts diagnosed memory failures into gated runtime evo-assets that are promoted only to later evaluation splits, preventing current-split ground-truth leakage while enabling continual improvement. On an initial EmbodiedWorldBench subset, ABot-AgentOS improves over a single-controller baseline in both task success and goal completion. Across memory benchmarks, ABot-AgentOS Static achieves 87.5 on LoCoMo, 59.9 on OpenEQA EM-EQA, 88.6 on Mem-Gallery, and 76.5 Acc@All on NExT-QA; self-evolution further improves LoCoMo to 88.7, OpenEQA to 60.4, and Mem-Gallery to 89.0. These results suggest that a general Agent OS layer can improve long-horizon embodied execution while providing persistent, auditable memory for continual interaction.

</details>

---
