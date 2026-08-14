# cs.AI | Artificial Intelligence | 2026-08-12

#arxiv #ComputerScience

**论文数**: 43

### [[20_Research/Papers/强化学习/Surgical_WAM_A_World-Action_Model_for_Data-Efficient_Surgical_Robot_Learning|Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning]]

![[assets/2608.11204_figure.png|800]]

- **arXiv**: [2608.11204](https://arxiv.org/abs/2608.11204)
- **PDF**: https://arxiv.org/pdf/2608.11204
- **详细分析**: [[20_Research/Papers/强化学习/Surgical_WAM_A_World-Action_Model_for_Data-Efficient_Surgical_Robot_Learning|Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning]]
- **作者**: Wenrui Bao, Tianyun Jiang, Zhiben Chen, Ser-Nam Lim, Peter D. Peng, Yuzhang Shang
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Surgical WAM: A World-Action Model for Data-Efficient Surgical Robot Learning》归入 机器人、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SurgWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning reliable surgical manipulation policies is bottlenecked by the scarcity of action-labeled demonstrations: teleoperated surgical robot (e.g., dVRK) trajectories with synchronized kinematics are costly to collect, while surgical tasks demand precise contact handling, long-horizon reasoning, and bimanual coordination. Endoscopic video is comparatively inexpensive and abundant relative to synchronized video--kinematics trajectories, and a natural way to exploit it is to learn world models of surgical scenes. However, existing surgical world models use video primarily for simulation or policy evaluation, and rarely translate the learned dynamics into closed-loop control. This gap raises our central question: under a fixed budget of action-labeled demonstrations, does action-free video pretraining improve closed-loop surgical manipulation? To answer it, we introduce the Surgical World-Action Model (Surgical WAM), a unified generative model built on Cosmos Policy that jointly predicts future endoscopic observations and executable surgical robot action chunks. Surgical WAM first learns surgical visual dynamics from action-free video and is then fine-tuned on the fixed action-labeled budget; at deployment, it acts as a closed-loop, receding-horizon controller that executes a short prefix of each predicted action chunk and replans from the resulting observation. On a suite of four simulated surgical manipulation tasks, video pretraining improves the average success rate from 63.5% to 77.8%, including an absolute gain of 20 percentage points on PegTransfer, with the largest improvements on contact-rich and bimanual tasks. These results demonstrate that action-free video provides transferable visual dynamics priors for learning surgical robot control with limited action supervision, positioning data-efficient video pretraining as a practical path toward scaling up surgical robot learning.

</details>

---

### [[20_Research/Papers/强化学习/Test-Time_Self-Evolving_GUI_Visual_Grounding_via_Reflection-Guided_On-Policy_Self-Distillation|Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation]]

![[assets/2608.11191_figure.png|800]]

- **arXiv**: [2608.11191](https://arxiv.org/abs/2608.11191)
- **PDF**: https://arxiv.org/pdf/2608.11191
- **详细分析**: [[20_Research/Papers/强化学习/Test-Time_Self-Evolving_GUI_Visual_Grounding_via_Reflection-Guided_On-Policy_Self-Distillation|Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation]]
- **作者**: Shiyu Xuan, Zechao Li
- **cs 子类**: cs.AI, cs.CL, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.65（加权：大模型 0.45，强化学习 0.2）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Test-Time Self-Evolving GUI Visual Grounding via Reflection-Guided On-Policy Self-Distillation》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MMBench, OSWorld, TTRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

GUI Visual Grounding is a fundamental capability for GUI agents. Existing models typically freeze their parameters after deployment, limiting their ability to adapt to unseen interfaces. Although recent methods attempt to adapt models via test-time reinforcement learning, they cannot reflect upon failed exploration. To overcome this, we propose a Test-Time Self-Evolving framework that enables models to improve after deployment without human-annotated ground truth. It constructs a closed-loop of Exploration, Evaluation, Reflection, and Internalization. Specifically, the agent first explores unseen interfaces by predicting grounding coordinates for given instructions. To evaluate these explorations, we introduce an MLLM-based Reflector to assess the generated results and provide the corresponding reasoning reflections. To internalize reflection knowledge into the model weights, we propose Reflection-Guided On-Policy Self-Distillation, which translates high-level reasoning into dense token-level supervision via a conditioned self-teacher. Furthermore, we design a Contrastive Calibration method to prevent incorrect auto-regressive prefixes from corrupting the supervisory signals during failed explorations. Extensive experiments across six benchmarks demonstrate our framework's effectiveness, achieving an average accuracy improvement of 7.4% over the base model. To the best of our knowledge, this is the first work to successfully exploit on-policy self-distillation for test-time adaptation in GUI visual grounding. By filling the gap in post-deployment adaptation, our framework completes the self-evolving capability of GUI agents. The code will be released.

</details>

---

### [[20_Research/Papers/具身智能/R4DSG_Relative_4D_Scene_Graph_Memory_for_Object-Centric_Question_Answering_in_Long_Egocentric_Video|R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video]]

![[assets/2608.11017_figure.png|800]]

- **arXiv**: [2608.11017](https://arxiv.org/abs/2608.11017)
- **PDF**: https://arxiv.org/pdf/2608.11017
- **详细分析**: [[20_Research/Papers/具身智能/R4DSG_Relative_4D_Scene_Graph_Memory_for_Object-Centric_Question_Answering_in_Long_Egocentric_Video|R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video]]
- **作者**: Ke Ma, Yamin Mao, Weiming Li, Shuai Tan, Yijie Zhong, Hao Chen, Haofen Wang, Meng Wang
- **cs 子类**: cs.AI, cs.CV, cs.HC
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 大模型
- **相关性评分**: 0.6（加权：具身智能 0.3，大模型 0.1，世界模型 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《R4DSG: Relative 4D Scene Graph Memory for Object-Centric Question Answering in Long Egocentric Video》归入 具身智能、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EMQA, EgoLifeQA, GroundVQA, VideoQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon egocentric video is a rich substrate for wearable AI assistants, but object-centric questions such as where an item was moved, when it last changed state, or why it was relocated remain difficult because caption- and transcript-based memories rarely preserve persistent object identity or structured spatial change. Existing long-video QA methods mainly emphasize temporal grounding and clip retrieval, while prior 3D scene-graph methods typically assume stronger geometry than free-motion wearable RGB video provides, including point clouds, RGB-D input, posed views, sparse reconstruction, or reconstructed scenes. R4DSG introduces a relative 4D scene graph memory for long egocentric video. Instead of storing raw graph sequences, R4DSG converts video into compact queryable memory entries indexed by time, place, persistent objects, anchor-relative change, and local interaction context. The main idea is to separate stable anchors from dynamic objects, maintain persistent object identity across frames, and represent object state through anchor-relative transitions rather than a globally aligned world model. Built on recent RGB-only advances in promptable video segmentation, temporal propagation, and relative 3D lifting, the method produces a retrieval-ready memory directly usable for long-horizon question answering. Evaluation on a 255-question object-related subset from EgoLifeQA shows, under question-only retrieval, a 6.7-point overall gain over EgoRAG-Text and a 12.5-point gain on when questions, which highlights the value of temporally organized object memory. These results position relative 4D scene graphs as a practical memory substrate for wearable assistants, AR systems, and embodied multimedia agents. GitHub Page: https://dualtransparency.github.io/R4DSG/.

</details>

---

### [[20_Research/Papers/具身智能/XCoT-VLA_Executable_Chain-of-Thought_for_Vision-Language-Action_Driving|XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving]]

![[assets/2608.10976_figure.png|800]]

- **arXiv**: [2608.10976](https://arxiv.org/abs/2608.10976)
- **PDF**: https://arxiv.org/pdf/2608.10976
- **详细分析**: [[20_Research/Papers/具身智能/XCoT-VLA_Executable_Chain-of-Thought_for_Vision-Language-Action_Driving|XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving]]
- **作者**: Foundation Model Team, XPeng Inc
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.4，大模型 0.1，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《XCoT-VLA: Executable Chain-of-Thought for Vision-Language-Action Driving》归入 具身智能、强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LingoQA, OpenVLA, XCoT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models can connect scene understanding, semantic reasoning, and trajectory generation for autonomous driving. However, verbose natural-language Chain-of-Thought (CoT) is poorly suited to real-time control because it is open-ended, costly to decode, and difficult to optimize as an action-facing representation. We propose XCoT-VLA, which replaces descriptive rationales with compact executable CoT tokens learned from automatically constructed Reason-Action supervision. Logged trajectories provide action evidence, while scene context supplies causal semantics. The predicted XCoT sequence remains in context and conditions fixed trajectory queries through shared multimodal self-attention. Deterministic token-function routing applies the Reason FFN to XCoT tokens and the Control FFN to trajectory queries for flow-matching trajectory generation. We further introduce XCoT Policy Optimization (XCPO) as an optional refinement extension in the same executable token space. XCoT-VLA reduces longitudinal ADE from 1.645 to 1.323 on a general-distribution set and lateral FDE from 1.616 to 0.648 in lane-change scenarios. By representing driving-oriented reasoning with only 2-6 executable XCoT tokens, our method substantially reduces autoregressive reasoning overhead and remains within the real-time planning budget. These results demonstrate that driving-oriented reasoning can be compact, executable, and directly connected to trajectory generation.

</details>

---

### [[20_Research/Papers/大模型/Evidence-Grounded_Trustworthy_Multimodal_Reasoning_and_Evaluation_Benchmark_in_Complex_Urban_Scenes|Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes]]

![[assets/2608.10954_figure.png|800]]

- **arXiv**: [2608.10954](https://arxiv.org/abs/2608.10954)
- **PDF**: https://arxiv.org/pdf/2608.10954
- **详细分析**: [[20_Research/Papers/大模型/Evidence-Grounded_Trustworthy_Multimodal_Reasoning_and_Evaluation_Benchmark_in_Complex_Urban_Scenes|Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes]]
- **作者**: Zhaoyang Wei, Bowen Jiang, Xumeng Han, Jiashu Li, Xuehui Yu, Yuling Liu, Guorong Li, Zhenjun Han, Jianbin Jiao
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Evidence-Grounded Trustworthy Multimodal Reasoning and Evaluation Benchmark in Complex Urban Scenes》归入 大模型、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AD2-Bench, CV-Bench, MMBench, MME-RealWorld, Real-World, RealWorldQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Multimodal Large Language Models (MLLMs) demonstrate impressive performance in benign scenarios, their cognitive reliability deteriorates significantly in complex scenes under adverse conditions. In these settings, models often rely on implicit inference without sufficient visual evidence, leading to a disconnect between perception and reasoning. Meanwhile, existing outcome-oriented benchmarks evaluate only final predictions and fail to diagnose failures in the underlying reasoning process. To address this gap, the authors propose AD2-Bench, which introduces a Hierarchical Visual Diagnosis framework that decomposes reasoning into a structured Chain of Evidence (CoE). This fine-grained diagnosis reveals that robust multimodal reasoning fundamentally depends on accurate evidence acquisition. Building on this perspective, the authors formulate reasoning from a probabilistic viewpoint and identify two primary causes of reasoning failure: Spatial Ambiguity, where models fail to distinguish target objects from background clutter, resulting in localization errors; and Semantic Uncertainty, where degraded visual features lead to incorrect semantic interpretation, resulting in understanding errors. To overcome these evidence deficiencies, they further propose Evidence-grounded Visual Reasoning (EGVOR), which replaces implicit reasoning with the explicit generation of Evidence Atoms - structured spatial-semantic triplets that enforce tight alignment between localization and semantic understanding. The model is trained through a hierarchical curriculum that progresses from reflective supervision construction to reinforcement learning, where reducing reasoning variance is explicitly rewarded. Extensive experiments demonstrate that EGVOR substantially improves reasoning stability under adverse conditions, providing a more robust framework for trustworthy multimodal cognition.

</details>

---

### [[20_Research/Papers/具身智能/ComBodied_Agents_a_New_Paradigm_of_Human-Centric_Agentic_AI|ComBodied Agents: a New Paradigm of Human-Centric Agentic AI]]

![[assets/2608.10915_figure.png|800]]

- **arXiv**: [2608.10915](https://arxiv.org/abs/2608.10915)
- **PDF**: https://arxiv.org/pdf/2608.10915
- **详细分析**: [[20_Research/Papers/具身智能/ComBodied_Agents_a_New_Paradigm_of_Human-Centric_Agentic_AI|ComBodied Agents: a New Paradigm of Human-Centric Agentic AI]]
- **作者**: Qianggang Ding, Xingyao Wang, Rui Feng, Zhibin Wang, Feixiang Wang, Kelong Mao, Hao Sun, Zhiyao Luo, Jiankai Tang, Lei Li, Jiadong Guo, Minheng Ni...
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 世界模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.6，世界模型 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《ComBodied Agents: a New Paradigm of Human-Centric Agentic AI》归入 大模型、具身智能、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CombodiedBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

After an older adult misses a medication dose, a software agent can send another reminder and an embodied agent can bring the medication. Yet neither explains whether the person forgot, is confused, has side effects, or deliberately refused, nor what support is appropriate. This reveals a structural gap in Agentic AI: Digital Agents primarily transform software states, while Embodied Agents transform physical states; neither makes a person's evolving state and agency the primary object of modeling, intervention, and evaluation. We introduce Combodied Agents, a human-centered paradigm that perceives, models, predicts, and supports individual human-state trajectories over time, using software tools, sensors, wearables, robots, and human services as action channels rather than end goals. We unify fragmented capabilities across personal assistants, health agents, AI companions, and adaptive human--AI systems into a closed loop: event-based multimodal perception reconstructs meaningful personal events; longitudinal, correctable memory provides temporal context; Personal World Models estimate future personal states and outcomes under alternative decisions and interventions; and an admissible intervention policy selects proportionate support under consent, uncertainty, safety, reversibility, and user control. Feedback from the person and environment updates the loop. Rather than requiring an exhaustive Human Digital Twin, the framework uses purpose-bounded, uncertainty-aware, user-correctable representations. We organize the design space by human-state targets, relational contexts, and agent roles, and propose scenario-centered evaluation, agency-preservation metrics, benchmark requirements, edge-native personal models, and governance directions. Combodied Agents shift Agentic AI from external task completion toward sustained human benefit.

</details>

---

### [[20_Research/Papers/大模型/VibeLifeBench_Can_Your_Life_Agent_Be_Proactive_and_Persistent_in_a_Living_World|VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?]]

![[assets/2608.10875_figure.png|800]]

- **arXiv**: [2608.10875](https://arxiv.org/abs/2608.10875)
- **PDF**: https://arxiv.org/pdf/2608.10875
- **详细分析**: [[20_Research/Papers/大模型/VibeLifeBench_Can_Your_Life_Agent_Be_Proactive_and_Persistent_in_a_Living_World|VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?]]
- **作者**: Xiaohongshu Inc
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living World?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Claw-Eval, ClawBench, CostBench, JobBench, Terminal-Bench, UniClawBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents are increasingly deployed as personal assistants. Existing evaluations, however, mostly use short, self-contained requests in static environments. Everyday life assistance is different. A task runs for weeks rather than minutes. The world keeps changing while the agent is not being prompted. Many constraints are never stated outright. An agent that merely answers the request in front of it will fail at such a task. What is needed instead is an agent that stays proactive and consistent. It decides on its own when to act, when to ask, and when to stay silent. It notices changes that nobody announced. It keeps one plan coherent from the first day to the last. No current benchmark measures this. We introduce VibeLifeBench, a benchmark of 200 long-horizon tasks across ten everyday-life domains. Each task is a scripted multi-week timeline in a simulated world of 22 mock services. The world advances on its own clock, and many of its changes are silent, so only an agent that re-inspects the world discovers them. Every task is graded by fine-grained, weighted checks that read only what the agent actually left behind, covering the end state, the timeliness of its actions, and whether it upheld the implicit constraints. We evaluate seven frontier models. All of them score low, which shows how far current agents are from assisting with real life. We will open-source all tasks, environments, and the evaluation framework.

</details>

---

### [[20_Research/Papers/大模型/SkillLens_Visual_Skill_Cards_for_Retrieval-Augmented_GUI_Action_Prediction_and_On-Policy_Distillation|SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation]]

![[assets/2608.10775_figure.png|800]]

- **arXiv**: [2608.10775](https://arxiv.org/abs/2608.10775)
- **PDF**: https://arxiv.org/pdf/2608.10775
- **详细分析**: [[20_Research/Papers/大模型/SkillLens_Visual_Skill_Cards_for_Retrieval-Augmented_GUI_Action_Prediction_and_On-Policy_Distillation|SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation]]
- **作者**: Zhou Liu, Ligang Huang, Zeli Su, Zewei Pan, Zhaoyang Han, Xing Chen, Yuanfeng Song, Wentao Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《SkillLens: Visual Skill Cards for Retrieval-Augmented GUI Action Prediction and On-Policy Distillation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OSWorld, WebLINX-BrowserGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Computer-using agents can perceive rich software interfaces, yet their decisions often lack visual procedural memory: they may recognize individual controls without identifying which familiar workflow is active, which control matters next, or what evidence would confirm progress. Raw interaction traces preserve such information but are long and noisy to condition on, whereas text-only skills often omit the visual state that makes a procedure applicable. We introduce Visual Skill Cards (VSCs), a state-conditioned memory representation that binds reusable procedures with applicability cues, visual evidence, and verification signals. SkillLens constructs VSCs from heterogeneous interaction experience through Trace-to-Visual-Skill-Card and, at inference time, retrieves relevant cards and selectively expands only the evidence needed by a fixed visual-language model executor for grounded GUI action prediction. The same representation also supports CardDistill, which uses VSC evidence as privileged teacher context to train a student that acts without runtime card retrieval. Across Multimodal-Mind2Web and WebLINX-BrowserGym, SkillLens improves the frozen GPT-5.4-mini executor by +11.6 points in Step SR and +2.9 points in Overall, respectively; CardDistill further improves the corresponding student-only Qwen3-VL-2B metrics by +12.0 and +3.2 points.

</details>

---

### [[20_Research/Papers/大模型/DuplexWorld_Can_voice_agents_help_you_get_through_the_day|DuplexWorld: Can voice agents help you get through the day?]]

![[assets/2608.10716_figure.png|800]]

- **arXiv**: [2608.10716](https://arxiv.org/abs/2608.10716)
- **PDF**: https://arxiv.org/pdf/2608.10716
- **详细分析**: [[20_Research/Papers/大模型/DuplexWorld_Can_voice_agents_help_you_get_through_the_day|DuplexWorld: Can voice agents help you get through the day?]]
- **作者**: Aryan Vijay Bhosale, Harshit Rajgarhia, Akhil Pothanapalli, Asif Shaik, Abhishek Mukherji, Dinesh Manocha
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《DuplexWorld: Can voice agents help you get through the day?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DuplexWorld, EVA-Bench, Full-Duplex-Bench, IHBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Speech-to-speech (S2S) voice agents are increasingly being incorporated into enterprise for customer care and as daily companions for consumers owing to the ease of the conversational modality over text. However, existing benchmarks fail to holistically evaluate voice agents along axes that really matter and are shaped as tests of agentic tool calling against a database. We believe they fail to adequately account for the diversity of conversational dialogue that mundane activities introduce and further, never test how faithfully an agent can assist on tasks that move beyond database manipulation. To tackle this DuplexWorld introduces six worlds where voice agents are especially useful: banking, insurance, travel, healthcare and logistics, and Pathfinding. Agents are evaluated on eleven different types of conversations across 156 scenarios (350+ hours of conversation), each testing conversational and analytical capability to varying degrees. Through extensive evaluation comprising agentic, conversational and speech-naturalness metrics, we show that even the best voice agents leave substantial room for improvement on all 3 axes (Pass@1: 0.490, turn-taking: 0.653, DNSMOS: 3.378). We perform extensive analysis on agentic v conversational performance, world- and conversation type-wise performance, failure modes exploring the explore v exploit lens for Pathfinding conversations and voice agent reliability over all six worlds.

</details>

---

### [[20_Research/Papers/大模型/Most_biomedical_publications_show_signs_of_LLM-assisted_writing|Most biomedical publications show signs of LLM-assisted writing]]

![[assets/2608.10715_figure.png|800]]

- **arXiv**: [2608.10715](https://arxiv.org/abs/2608.10715)
- **PDF**: https://arxiv.org/pdf/2608.10715
- **详细分析**: [[20_Research/Papers/大模型/Most_biomedical_publications_show_signs_of_LLM-assisted_writing|Most biomedical publications show signs of LLM-assisted writing]]
- **作者**: Lena Holzwarth, Rita González-Márquez, Dmitry Kobak
- **cs 子类**: cs.AI, cs.CL, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Most biomedical publications show signs of LLM-assisted writing》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Over the past several years, LLM-powered chatbots and agents have become widely used as a tool for academic writing. LLM-assisted writing can be valuable by removing language barriers but at the same time causes concerns about misconduct and fraud. To inform policy decisions, it is necessary to monitor the prevalence of LLM-altered texts in scholarly publications. Despite some recent progress in this direction, no existing method can produce reliable estimates. Here we suggest and validate a new unbiased approach to estimate LLM usage in a corpus of texts based on changing word frequencies. We apply our method to the full texts of open-access biomedical papers from Pubmed Central, and show that by the end of 2025, 89% of papers show excess of LLM-associated vocabulary. We also find that LLMs are twice as likely to be used when writing a paragraph in the Discussion section (68%) compared to a paragraph in the Methods section (32%), but even inside the Methods section, the overall prevalence of LLM usage is over 50%. We believe that our estimates are crucial to shape future guidelines and policies.

</details>

---

### [[20_Research/Papers/大模型/Conversational_Orchestration_for_Organic_6G|Conversational Orchestration for Organic 6G]]

![[assets/2608.10714_figure.png|800]]

- **arXiv**: [2608.10714](https://arxiv.org/abs/2608.10714)
- **PDF**: https://arxiv.org/pdf/2608.10714
- **详细分析**: [[20_Research/Papers/大模型/Conversational_Orchestration_for_Organic_6G|Conversational Orchestration for Organic 6G]]
- **作者**: Masoud Shokrnezhad, Tarik Taleb
- **cs 子类**: cs.AI, cs.DC, cs.NI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Conversational Orchestration for Organic 6G》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Organic 6G vision of a network of networks spanning an edge-cloud continuum complemented by non-terrestrial resources requires, to realize its promise, service provisioning that is simple to operate, scalable across independently administered domains, and agile under domain churn (i.e., domains dynamically joining and leaving). Despite advances in cross-domain orchestration, many proposals rely on heavy integration fabrics, multi-layer coordinators, and deep telemetry pipelines that hinder deployability and amplify coordination overhead. We propose a lightweight, decentralized conversational orchestration framework based on Large Language Model (LLM)-driven domain agents. Each domain remains autonomous: an agent observes local state via tools, reasons in a closed loop, and exchanges summaries with neighboring agents over an Agent-to-Agent (A2A) overlay aligned with data-plane coupling. Fast feasible placement is enabled by periodic, routing-like dissemination of reachability advertisements (latency, bottleneck bandwidth, and compute capacity), while safe re-optimization, scaling, and migration are handled through event-driven requests and negotiation. To meet real-time constraints, we deploy a compact reasoning model trained with verifier-based self-verification and periodically refined online via shadow updates. Simulations show manageable, near-linear control-plane overhead as domains scale and during domain joins, and robust decision quality, including recovery after objective changes. We close by outlining future research directions for principled, secure, and uncertainty-aware agentic orchestration in Organic 6G.

</details>

---

### [[20_Research/Papers/大模型/ProTAGAD_A_Foundation_Model_for_TAG_Anomaly_Detection_with_Decoupled_Topological_and_Textual_Prototypes|ProTAGAD: A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes]]

![[assets/2608.10699_figure.png|800]]

- **arXiv**: [2608.10699](https://arxiv.org/abs/2608.10699)
- **PDF**: https://arxiv.org/pdf/2608.10699
- **详细分析**: [[20_Research/Papers/大模型/ProTAGAD_A_Foundation_Model_for_TAG_Anomaly_Detection_with_Decoupled_Topological_and_Textual_Prototypes|ProTAGAD: A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes]]
- **作者**: Ziyan Wang, Liwen Wu, Cheng Xie, Song Gao, Zhenli He, Xin Jin
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, ComputerVision, Security

#### 研究背景与动机

《ProTAGAD: A Foundation Model for TAG Anomaly Detection with Decoupled Topological and Textual Prototypes》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-Attributed Graphs (TAGs), endowed with abundant textual content along with topological structures, have emerged as a versatile backbone for real-world anomaly detection spanning large language model security, social network moderation, and cyber threat identification. Unlike conventional Graph Anomaly Detection (GAD), which relies primarily on structural irregularities, TAG anomaly detection must jointly leverage both topological patterns and fine-grained textual semantics to capture nuanced anomalous behaviors. The current GNN-based anomaly detectors adopt holistic message-passing schemes that indiscriminately fuse structural proximity and textual semantics during propagation, leading to deep cross-modality coupling. This entanglement acts as a noise amplifier, obscuring subtle anomalous signals and directly giving rise to the Blurred-Anomaly-Boundary (BAB) issue by rendering normal-anomalous decision boundaries poorly separable. This challenge is further amplified for graph foundation models that require robust cross-domain generalization. To bridge this gap, we introduce a novel foundation model for TAG anomaly detection featuring decoupled topological and textual prototypes. Our framework constructs dual prototype banks to independently model structural normality and semantic consistency, effectively isolating anomaly cues that are otherwise diluted during coupled aggregation. Extensive experiments across 14 diverse benchmark datasets demonstrate that our method consistently achieves state-of-the-art performance in cross-domain settings. Notably, the ablation studies further corroborate the prevalence of the BAB issue in conventional coupled TAG anomaly detectors, and show that our decoupled prototype design effectively mitigates this challenge.

</details>

---

### [[20_Research/Papers/大模型/Self-Correcting_Long-Horizon_Search_Agents_via_Tree-Structured_Memory|Self-Correcting Long-Horizon Search Agents via Tree-Structured Memory]]

![[assets/2608.10676_figure.png|800]]

- **arXiv**: [2608.10676](https://arxiv.org/abs/2608.10676)
- **PDF**: https://arxiv.org/pdf/2608.10676
- **详细分析**: [[20_Research/Papers/大模型/Self-Correcting_Long-Horizon_Search_Agents_via_Tree-Structured_Memory|Self-Correcting Long-Horizon Search Agents via Tree-Structured Memory]]
- **作者**: Aijun Yang, Qianxue Guo, Ziyi Huang, Yuxuan Chen, Shiyou Qian, Jian Cao
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Self-Correcting Long-Horizon Search Agents via Tree-Structured Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-based search agents answer questions through multi-step interactions with external environments. However, providing complete execution trajectories to the LLM causes unbounded context growth and introduces noise. Existing compression methods reduce context at the cost of important details and often replace erroneous facts without repairing downstream reasoning derived from them. To address this problem, we propose ReTree, a self-correcting tree-structured memory mechanism for search agents. ReTree constructs a bounded per-step reasoning context while preserving source-linked evidence. It models search as an evidence tree whose nodes store bounded summaries, evidence, and revision histories. When newly retrieved evidence contradicts an earlier claim, ReTree traces back to the node where the claim was introduced, replaces outdated evidence, regenerates summaries, prunes affected branches, and resumes search. Source-grounded evidence provenance supports reliable conflict localization and keeps final claims traceable to retrieved passages. Experiments on four public question-answering and search benchmarks show that ReTree consistently outperforms Full-Trajectory ReAct, improving answer accuracy by up to 25.6 percentage points (pp); the average maximum per-step reasoning context of Full-Trajectory ReAct is $1.27$--$1.51\times$ that of ReTree. These results establish ReTree as an effective self-correcting memory abstraction for long-horizon search.

</details>

---

### [[20_Research/Papers/大模型/REDAgentBench_Executable_Red_Teaming_and_Faithful_Measurement_of_LLM_Agent_Systems|REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems]]

![[assets/2608.10669_figure.png|800]]

- **arXiv**: [2608.10669](https://arxiv.org/abs/2608.10669)
- **PDF**: https://arxiv.org/pdf/2608.10669
- **详细分析**: [[20_Research/Papers/大模型/REDAgentBench_Executable_Red_Teaming_and_Faithful_Measurement_of_LLM_Agent_Systems|REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems]]
- **作者**: Zixing Chen, Xingyuan Liu, Jie Zhu, Huaixia Dou, Shuo Jiang, Junhui Li, Lifan Guo, Feng Chen, Chi Zhang
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《REDAgentBench: Executable Red Teaming and Faithful Measurement of LLM Agent Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：JAWS-Bench, REDAgentBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents combine language-based reasoning with external tools to perform complex tasks. Adversarial inputs can exploit interactions between the agent and its environment, causing the agent to violate safety policies during execution. Yet existing evaluations often reduce agent safety to a single attack success rate (ASR), collapsing exposure, execution, observation, and adjudication and potentially conflating actual violations with evidence visibility. We introduce REDAgentBench, an executable framework for autonomous red-teaming and faithful measurement. It derives attacks from explicit safety constraints and associated agent-system vulnerabilities, runs them in isolated service sandboxes, and verifies harmful effects from service receipts and final-state changes. The benchmark contains 1,661 cases across five service surfaces. Across six models and three agent harnesses, macro-average ASR is 65.69%; reported ASR varies with harness and evidence view, while evaluation-context disclosure changes execution behavior. In a state-grounded diagnostic cohort, almost one in five confirmed violations with resolved action anchors occurs after the agent states the relevant constraint or risk, revealing a Recognition--Execution Gap. Finally, a training-free policy reminder reduces confirmed violations by more than 70 percentage points in matched replay. These findings show that executable evaluation can improve safety measurement and identify actionable intervention points.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning-Based_Laser_Cutting_Machine_Parameter_Optimization|Reinforcement Learning-Based Laser Cutting Machine Parameter Optimization]]

![[assets/2608.10549_figure.png|800]]

- **arXiv**: [2608.10549](https://arxiv.org/abs/2608.10549)
- **PDF**: https://arxiv.org/pdf/2608.10549
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning-Based_Laser_Cutting_Machine_Parameter_Optimization|Reinforcement Learning-Based Laser Cutting Machine Parameter Optimization]]
- **作者**: Khanh Quan Pham, Majid Kundroo, Geunwoo Ban, Seongho Bae, Taehong Kim
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: RL

#### 研究背景与动机

《Reinforcement Learning-Based Laser Cutting Machine Parameter Optimization》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving high accuracy in laser-based cutting of optical films requires careful tuning of parameters such as focal length and laser power beam, adjusted according to the specific properties of each film type. Trial-and-error based traditional methods are used to find the most suitable cutting parameters for various films, but they are slow and inaccurate. To address this issue, this paper presents the Reinforcement Learning for Laser Cutting (RL$^{2}$C) algorithm, which uses Q-learning with an epsilon-greedy policy to dynamically optimize cutting parameters, significantly reducing taper size and film wastage. Additionally, RL$^{2}$C incorporates a dynamic environment space adaptability mechanism to allow it to adapt to new states encountered during the learning process over multiple batches of experiments. Experimental results demonstrate that RL$^{2}$C requires fewer steps and less time to find optimal cutting parameters compared to various RL-based optimization methods. Specifically, RL$^{2}$C reduces the number of optimization steps by up to 12.5\% and processing time by up to 81.8\% compared to existing methods. This study demonstrates the potential of RL in industrial laser-cutting processes by improving cut quality, reducing time and film wastage, and minimizing manual interventions.

</details>

---

### [[20_Research/Papers/大模型/SKILLER_Language-Level_Reinforcement_Learning_for_Reusable_Skill_Extraction_in_Small_Language_Models|SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models]]

![[assets/2608.10538_figure.png|800]]

- **arXiv**: [2608.10538](https://arxiv.org/abs/2608.10538)
- **PDF**: https://arxiv.org/pdf/2608.10538
- **详细分析**: [[20_Research/Papers/大模型/SKILLER_Language-Level_Reinforcement_Learning_for_Reusable_Skill_Extraction_in_Small_Language_Models|SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models]]
- **作者**: Chenhao Dang, Siyuan Xiong, Conghui He, Weijia Li
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《SKILLER: Language-Level Reinforcement Learning for Reusable Skill Extraction in Small Language Models》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EarthBench, SWE-Skills-Bench, SkillLearnBench, SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent skills represent a standardized format for packaging procedural knowledge and domain expertise, serving within agent harness systems as an essential mechanism to continually constrain a language model's behavior space for repeatable, high-quality task execution. However, because strong closed-source models entail high inference costs, current popular agent harnesses, such as Codex and OpenClaw, remain prohibitively expensive when deploying these skills to accomplish real-world tasks. The rapid capability enhancement of open-source models deployable on consumer-grade GPUs presents a compelling opportunity to drastically reduce these costs by leveraging skill-based behavioral constraints. Nevertheless, automatically generating effective skills tailored specifically for such compact models remains a significant practical challenge. To address this, we propose SKILLER, a natural-language-driven reinforcement learning framework designed to automatically generate executor-specific skills for small models, which employs a strong model as the actor and critic, treats the small-model agent system as the environment, and propagates all reinforcement learning signals entirely via natural language. Extensive experimental evaluations across five relevant benchmarks using Qwen3.5-9B and Qwen3.5-4B demonstrate that SKILLER outperforms three open-source and one closed-source skill generation or evolution methods, achieving absolute gains ranging from 4.3 to 20.4 percentage points for the 9B model and 1.8 to 13.3 points for the 4B model, while remarkably matching the performance of strong closed-source models on single-skill tasks in SkillsBench. The project is available at https://github.com/DANG-ai/SKILLER.

</details>

---

### [[20_Research/Papers/大模型/SafeCap_Improving_LVLM_Safety_with_Image_Captioning_Reinforcement_Learning|SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning]]

![[assets/2608.10513_figure.png|800]]

- **arXiv**: [2608.10513](https://arxiv.org/abs/2608.10513)
- **PDF**: https://arxiv.org/pdf/2608.10513
- **详细分析**: [[20_Research/Papers/大模型/SafeCap_Improving_LVLM_Safety_with_Image_Captioning_Reinforcement_Learning|SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning]]
- **作者**: Caoyuan Ma, Wenpu Liu, Weichu Xie, Tian Gu, Shilei Zhao, Lingxi Min, Shuai Dong, Yuqi Xu, Ji Zhao, Ziyue Wang, Wenzheng Chang, Taiqiang Wu...
- **cs 子类**: cs.AI, cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，强化学习 0.8）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《SafeCap: Improving LVLM Safety with Image Captioning Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CapRL, MM-SafetyBench, VLSBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large vision-language models (LVLMs) remain vulnerable to jailbreak attacks that exploit visual inputs to bypass safety alignment inherited from their language backbones. We propose SafeCap, a reinforcement-learning framework that aligns LVLMs through learned self-captioning. SafeCap trains a policy model to first generate a safety-relevant image caption and then produce a final answer; the caption is further optimized by whether it enables a frozen LLM to reach a safety-aligned decision. This caption-mediated objective encourages the policy to expose visual cues relevant to safe response generation rather than relying solely on direct refusal supervision. Across five multimodal safety benchmarks and six vision-utility benchmarks, SafeCap substantially improves aggregate safety performance under its intended DirectCap protocol, with gains of 3.7-19.0 points in safety average across four model settings while maintaining comparable or improved vision utility. Under controlled comparisons on matched backbones and data, SafeCap outperforms safety SFT, DPO, and SafeGRPO, demonstrating the effectiveness of caption-mediated reinforcement learning for multimodal safety alignment.

</details>

---

### [[20_Research/Papers/大模型/MEGA_Self-Evolving_Agent_Optimization_Infrastructure_via_Wisdom_Graph|MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph]]

![[assets/2608.10504_first_page.png|800]]

- **arXiv**: [2608.10504](https://arxiv.org/abs/2608.10504)
- **PDF**: https://arxiv.org/pdf/2608.10504
- **详细分析**: [[20_Research/Papers/大模型/MEGA_Self-Evolving_Agent_Optimization_Infrastructure_via_Wisdom_Graph|MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph]]
- **作者**: Jung Hwan Lee, Kyu Ho Lee, Gwang Hoon Yoo
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《MEGA: Self-Evolving Agent Optimization Infrastructure via Wisdom Graph》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As coding agents increasingly handle implementation, the central challenge shifts from building individual agents to building an infrastructure that systematically improves them. Current approaches optimize agent systems without accumulating transferable knowledge, accumulate knowledge without compositional reasoning over it, and lack a mechanism for that knowledge to self-evolve through operational evidence. MEGA (Meta Evaluation-Grounded Adaptation) addresses these gaps as a self-evolving infrastructure: each optimization cycle produces durable assets, compositional reasoning over those assets guides subsequent optimization, and operational evidence refines both the accumulated wisdom and the reasoning that governs it. Layer 1 distills reusable wisdom from agent sessions through behavioral-pattern clustering and empirical A/B validation, transforming each process into a durable asset. Layer 2 decomposes these assets into atomic PCR (Primary-Context-Resultant) units within a typed Wisdom Graph and performs deductive, abductive, and inductive reasoning to expand implicit relations; it then assembles context-specific execution plans through compositional retrieval that surfaces bridging knowledge unreachable by embedding similarity alone. Layer 3 performs multi-agent collaborative optimization over heterogeneous agent workflows (code nodes, LLM calls, and tool-using agents), attributing improvement effects to specific strategy changes through controlled evaluation that eliminates data variance. Evidence fed back from Layer 3 drives the self-evolution of both the curation strategies that govern wisdom composition and the optimization trajectories accumulated across runs. The result is an infrastructure in which optimizing an agent system and evolving the knowledge that guides optimization are one and the same process.

</details>

---

### [[20_Research/Papers/强化学习/Exploration-Driven_Personalized_Federated_Reinforcement_Learning_via_Intrinsic_Motivation|Exploration-Driven Personalized Federated Reinforcement Learning via Intrinsic Motivation]]

![[assets/2608.10499_figure.png|800]]

- **arXiv**: [2608.10499](https://arxiv.org/abs/2608.10499)
- **PDF**: https://arxiv.org/pdf/2608.10499
- **详细分析**: [[20_Research/Papers/强化学习/Exploration-Driven_Personalized_Federated_Reinforcement_Learning_via_Intrinsic_Motivation|Exploration-Driven Personalized Federated Reinforcement Learning via Intrinsic Motivation]]
- **作者**: Md Rafid Islam, Rafsan Jany, Zahid Hasan, Ratun Rahman
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Security, Systems

#### 研究背景与动机

《Exploration-Driven Personalized Federated Reinforcement Learning via Intrinsic Motivation》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EDPFRL, FRL, FedAvg-RL, FedRL, PFRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalized Federated Reinforcement Learning (PFRL) takes a decentralized approach to storing and accessing information based on past experiences while keeping each client's data private during the learning of each client's policy. Many current methods for PFRL rely heavily on exploiting existing reinforcement learning reward signals to derive an optimal policy for each client, thereby neglecting exploration in non-stationary or sparse-reward environments. In this work, we introduce a new exploration-driven framework, Exploration-Driven Personalized Federated Reinforcement Learning via Intrinsic Motivation (EDPFRL-IM), that leverages an inherent curiosity-driven exploration at each client to promote local exploration and protect client privacy. Furthermore, to facilitate policy discovery via exploration in previously unexplored state spaces, clients add an intrinsic random network distillation (RND) signal to their extrinsic reward. Additionally, the server does not have access to clients' raw experiences or local gradient estimates; instead, the server sends global exploration priors and collects minimal novelty summaries from each client to enable both diverse and coordinated exploration among clients. Experiments in benchmark environments show that our framework outperforms average PFRL benchmarks in policy personalization and sample efficiency, primarily in delayed and sparse reward systems. Overall, EDPFRL-IM enables the integration of a flexible exploratory learning structure into federated reinforcement learning systems while preserving client privacy.

</details>

---

### [[20_Research/Papers/大模型/INSIDE_the_Student's_Mind_Jointly_Modeling_Latent_Reasoning_and_Action_in_LLM_Student_Simulators|INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators]]

![[assets/2608.10492_figure.png|800]]

- **arXiv**: [2608.10492](https://arxiv.org/abs/2608.10492)
- **PDF**: https://arxiv.org/pdf/2608.10492
- **详细分析**: [[20_Research/Papers/大模型/INSIDE_the_Student's_Mind_Jointly_Modeling_Latent_Reasoning_and_Action_in_LLM_Student_Simulators|INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators]]
- **作者**: Rose Niousha, Minwoo Kang, Narges Norouzi
- **cs 子类**: cs.AI, cs.CY
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《INSIDE the Student's Mind: Jointly Modeling Latent Reasoning and Action in LLM Student Simulators》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Model (LLM)-based simulators often reproduce observable actions but fail to capture the underlying reasoning behind them. In education, where student simulation is increasingly used for various applications such as evaluating tutoring systems, this gap is especially pronounced. Two students may submit identical submissions for entirely different reasons. We present INTERNAL STUDENT DIALOGUE (INSIDE), a student modeling framework that fine-tunes LLMs not only to act like students but also to think like them. INSIDE generates internal dialogue grounded in Bloom's Taxonomy across cognitive, affective, and action dimensions, and fine-tunes models on paired think traces and actions. We baseline against different prompting frameworks and evaluate on two axes: fidelity of simulated actions and quality of generated internal dialogue. Our evaluations show that INSIDE improves simulation fidelity in both action fidelity, matching code generation of real students, and reasoning alignment, achieving the highest alignment across models up to 57.9%.

</details>

---

### [[20_Research/Papers/具身智能/Lost_in_Reconstruction_Aligning_Action_Representations_with_Language_in_Vision-Language-Action_Models|Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models]]

![[assets/2608.10484_figure.png|800]]

- **arXiv**: [2608.10484](https://arxiv.org/abs/2608.10484)
- **PDF**: https://arxiv.org/pdf/2608.10484
- **详细分析**: [[20_Research/Papers/具身智能/Lost_in_Reconstruction_Aligning_Action_Representations_with_Language_in_Vision-Language-Action_Models|Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models]]
- **作者**: Li Wenjie, Yash Jangir, Ignacy Stepka, Yash Agarwal, Marion Kipsang, Yonatan Bisk
- **cs 子类**: cs.AI, cs.CL, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.35（加权：具身智能 1.5，大模型 0.35，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Lost in Reconstruction: Aligning Action Representations with Language in Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action verbs describe not only the physical outcomes of actions, but also how those actions are performed. Yet action representations in vision-language-action models (VLAs) are typically optimized for reconstruction under L1/L2 losses in raw action space, where numerical proximity need not reflect linguistically meaningful distinctions. On BridgeV2, we show that action trajectories contain verb-grounding information beyond visual state changes, and that reconstruction-only discrete tokenization systematically erodes this information. To address this problem, we introduce SALT, a Semantically ALigned action Tokenizer that augments a VQ-VAE-style tokenizer with an auxiliary objective requiring a frozen vision-language model to recover the episode instruction from quantized action latents. Policies trained with SALT achieve 71.9% average success in SimplerEnv, compared with 42.7% for a reconstruction-only VQ-VAE tokenizer and 31.2% for FAST. SALT also develops verb-specialized codes while maintaining reconstruction fidelity. These results show that robot action trajectories provide a source of language grounding and that preserving this structure in action representations can substantially improve language-conditioned control.

</details>

---

### [[20_Research/Papers/大模型/Predicting_Space_Groups_of_Double_Perovskites_by_LLM_with_Dynamic_Few-Shot_Learning|Predicting Space Groups of Double Perovskites by LLM with Dynamic Few-Shot Learning]]

![[assets/2608.10483_first_page.png|800]]

- **arXiv**: [2608.10483](https://arxiv.org/abs/2608.10483)
- **PDF**: https://arxiv.org/pdf/2608.10483
- **详细分析**: [[20_Research/Papers/大模型/Predicting_Space_Groups_of_Double_Perovskites_by_LLM_with_Dynamic_Few-Shot_Learning|Predicting Space Groups of Double Perovskites by LLM with Dynamic Few-Shot Learning]]
- **作者**: Jongwon Park, Inhyo Lee, Junhyeong Lee, Seunghwa Ryu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Predicting Space Groups of Double Perovskites by LLM with Dynamic Few-Shot Learning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CrabNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Double perovskites (DPs) offer broad compositional tunability, but predicting the space groups (SGs) of stable structures remains difficult because available datasets are often strongly imbalanced toward dominant SG classes. We refer to dominant SG classes as major SGs and underrepresented classes as minor SGs. We introduce Dynamic and Diversity-enhanced Few-shot Retrieval and Rule-Guided Inference for Space-Group Prediction (DyRIS), an LLM-agent-based framework that predicts ranked SG candidates from a given DP composition. DyRIS uses diversity-enhanced dynamic few-shot prompting to retrieve relevant in-context examples while limiting the dominance of frequently represented SGs. It further incorporates rule-guided inference based on B/B' cation ordering, quantitative indicators, and major-SG bias control to refine and rank the final Top-3 SG candidates. We evaluate DyRIS on 3,528 thermodynamically filtered DP entries and compare it with composition-based and descriptor-based baselines. At a training-data ratio of 0.5, DyRIS achieves competitive overall accuracy while obtaining the best Overall Top-1 macro-F1 score and the best performance across all Minor-SG metrics. DyRIS improves Minor-SG Top-1 accuracy by 3.26 percentage points relative to CrabNet and achieves higher Minor-SG Top-3 accuracy than the strongest PyCaret-based baseline. Ablation studies show that diversity-enhanced retrieval, quantitative indicators, major-SG bias control, and B/B' ordering information each contribute to prediction performance. Additional experiments show that the final rule-guided inference step is not easily replaced by conventional classifier- or ranker-based models. These findings demonstrate the potential of combining retrieval-based LLM reasoning with crystallographic domain knowledge for SG prediction in imbalanced materials datasets.

</details>

---

### [[20_Research/Papers/强化学习/Critic-Free_Pretraining_for_Efficient_Online_Reinforcement_Learning_Fine-Tuning|Critic-Free Pretraining for Efficient Online Reinforcement Learning Fine-Tuning]]

![[assets/2608.10473_figure.png|800]]

- **arXiv**: [2608.10473](https://arxiv.org/abs/2608.10473)
- **PDF**: https://arxiv.org/pdf/2608.10473
- **详细分析**: [[20_Research/Papers/强化学习/Critic-Free_Pretraining_for_Efficient_Online_Reinforcement_Learning_Fine-Tuning|Critic-Free Pretraining for Efficient Online Reinforcement Learning Fine-Tuning]]
- **作者**: Daoyi Li, Yixian Zhang, Chao Yu, Wenbo Ding, Yu Wang
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Critic-Free Pretraining for Efficient Online Reinforcement Learning Fine-Tuning》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline-to-online (O2O) reinforcement learning aims to leverage policies pretrained on static datasets while improving them through online interaction. However, directly reusing an offline-trained critic can hinder online fine-tuning: as the policy and data distribution change rapidly, value estimates inherited from offline training may become misaligned with the online environment, leading to inaccurate policy improvement and inefficient exploration. To address this problem, we introduce \textbf{C}ritic-\textbf{F}ree \textbf{P}retraining: an efficient paradigm that completely abandons the approach of offline critic training, allowing a freshly initialized critic to adapt without inheriting biased estimates. CFP is compatible with various mainstream O2O algorithms and consistently matches or improves upon conventional O2O algorithms across a diverse set of tasks, with particularly pronounced gains on several challenging tasks.

</details>

---

### [[20_Research/Papers/大模型/Conversational_versus_Dashboard_Explainable_AI_for_UAV_Intrusion_Detection_An_Empirical_Study_of_Operator_Trust_and_Reliance|Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance]]

![[assets/2608.10434_figure.png|800]]

- **arXiv**: [2608.10434](https://arxiv.org/abs/2608.10434)
- **PDF**: https://arxiv.org/pdf/2608.10434
- **详细分析**: [[20_Research/Papers/大模型/Conversational_versus_Dashboard_Explainable_AI_for_UAV_Intrusion_Detection_An_Empirical_Study_of_Operator_Trust_and_Reliance|Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance]]
- **作者**: Cong Chi Nguyen, Trang Mai Xuan, Vu-Duc Ngo, Kim-Ngan Thi Nguyen, Trong-Nghia Nguyen, Thien Van Luong
- **cs 子类**: cs.AI
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.0（加权：大模型 0.2，机器人 0.8）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Conversational versus Dashboard Explainable AI for UAV Intrusion Detection: An Empirical Study of Operator Trust and Reliance》归入 机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Machine learning-based Intrusion Detection Systems (IDS) have demonstrated superior performance in securing Unmanned Aerial Vehicle (UAV) networks. However, the 'black-box' nature of these models, combined with the high dimensionality of multimodal cyber-physical data, poses significant interpretability challenges. Static visualization dashboards may struggle to present complex relationships among multimodal cyber-physical features in a form that is easy for operators to inspect and interpret. To address this, we propose a Conversational XAI interface powered by Large Language Models (LLM) to facilitate on-demand investigation. In a controlled experiment with participants, we systematically evaluated the impact of this conversational interface versus a traditional XAI Dashboard on operator understanding, trust, and reliance during post-incident auditing tasks. Our results suggest that the conversational interface was perceived as more useful than the dashboard, potentially because it helped participants access and synthesize relevant information more easily. However, this benefit was accompanied by a lower level of appropriate self-reliance, indicating a potential risk of over-reliance. One possible interpretation is that the natural-language responses made the AI advice easier to accept, which may have reduced participants' tendency to verify the underlying evidence when the IDS was incorrect. These findings point to a potential trade-off in human-AI collaboration for UAV intrusion auditing: interaction mechanisms that improve perceived usability may also increase the risk of inappropriate reliance. We conclude by discussing design implications for future XAI systems that balance seamless interaction with cognitive forcing functions to foster appropriate reliance.

</details>

---

### [[20_Research/Papers/大模型/Recovering_Wasted_Compute_in_Autoresearch_Agents|Recovering Wasted Compute in Autoresearch Agents]]

![[assets/2608.10424_figure.png|800]]

- **arXiv**: [2608.10424](https://arxiv.org/abs/2608.10424)
- **PDF**: https://arxiv.org/pdf/2608.10424
- **详细分析**: [[20_Research/Papers/大模型/Recovering_Wasted_Compute_in_Autoresearch_Agents|Recovering Wasted Compute in Autoresearch Agents]]
- **作者**: Au Kwok Chun, Abhigyan Acherjee, Amrutha Rao, Zaiqian Chen, Kazem Meidani, C. Bayan Bruss, Micah Goldblum
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Recovering Wasted Compute in Autoresearch Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A slew of recent works develop agents for solving research problems end-to-end, a paradigm increasingly referred to as autoresearch. Such agents have inspired large industry investment, motivated by their potential to automate time-consuming human labor and customize machine learning solutions for specialized applications. In this paper, we study the modeling pipeline at the core of these autoresearch systems and identify common failure modes when they are applied to tabular datasets: (1) they waste compute resolving the same bugs over and over again; (2) they often fail to tune hyperparameters even when they have a large remaining compute budget; (3) the tree-search algorithms that power them do not explore; and (4) they perform data analysis, mimicking the humans whose data they are trained on, but do not use that analysis to make downstream decisions. We explore targeted interventions and find that a global debug consultant that shares discovered runtime constraints across all branches of the search tree, prompt- and control-level enhancements, and refined tree-search algorithms successfully recover wasted compute. Our results show that large gains in autoresearch agent performance are achievable through agentic design alone, holding the underlying language model fixed.

</details>

---

### [[20_Research/Papers/强化学习/Threat-guided_Policy-aware_Scene_Perturbation_for_Safe_Autonomous_Driving_with_Online_Reinforcement_Learning|Threat-guided Policy-aware Scene Perturbation for Safe Autonomous Driving with Online Reinforcement Learning]]

![[assets/2608.10403_figure.png|800]]

- **arXiv**: [2608.10403](https://arxiv.org/abs/2608.10403)
- **PDF**: https://arxiv.org/pdf/2608.10403
- **详细分析**: [[20_Research/Papers/强化学习/Threat-guided_Policy-aware_Scene_Perturbation_for_Safe_Autonomous_Driving_with_Online_Reinforcement_Learning|Threat-guided Policy-aware Scene Perturbation for Safe Autonomous Driving with Online Reinforcement Learning]]
- **作者**: Xincong Hu, Lei Ou, Maosen Li, Jingtao Zhang, Liguo Hou, Zongzhang Zhang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Threat-guided Policy-aware Scene Perturbation for Safe Autonomous Driving with Online Reinforcement Learning》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AdvSim, CaRL, SafeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has shown promising performance in autonomous driving, yet ensuring the safety of online RL policies remains challenging due to insufficient exposure to safety-critical driving scenes. The long-tailed nature of real-world traffic situations makes dangerous and rare interactions difficult to encounter through conventional sampling, limiting the ability of RL policies to learn robust safety behaviors. Existing methods improve training diversity by synthesizing challenging scenes or adversarial situations. However, these approaches typically optimize scene generation objectives separately from the evolving policy, without explicitly modeling how generated perturbations relate to the current policy's weaknesses and learning needs. In this paper, we propose Threat-guided Policy-aware Scene Perturbation (TPSP) for safe autonomous driving with online RL. TPSP introduces a policy-aware scene encoder to capture the interaction between policy behaviors and surrounding environments, enabling scene perturbation aligned with the current policy. Based on this representation, TPSP selectively perturbs critical objects rather than applying uniform modifications across the scene. Furthermore, we develop a threat-guided optimization strategy that evaluates perturbed scenes through threat-level differences between policy rollouts on original and perturbed scenes, guiding the generation of safety-critical scenes with higher training value. Comprehensive experiments demonstrate that TPSP improves safety learning efficiency, achieving strong safety performance on NAVSIM v2 with approximately 4 million kilometers of simulated driving data. Ablation studies verify that policy-aware targeted perturbations provide more informative safety-critical experiences than random or policy-unaware strategies, enabling safer driving under limited interaction budgets.

</details>

---

### [[20_Research/Papers/具身智能/Hidden_in_Plain_Sight_Diffusion-Based_Unrestricted_Robotic_Attacks_on_Vision-Language-Action_Models|Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models]]

![[assets/2608.10393_figure.png|800]]

- **arXiv**: [2608.10393](https://arxiv.org/abs/2608.10393)
- **PDF**: https://arxiv.org/pdf/2608.10393
- **详细分析**: [[20_Research/Papers/具身智能/Hidden_in_Plain_Sight_Diffusion-Based_Unrestricted_Robotic_Attacks_on_Vision-Language-Action_Models|Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models]]
- **作者**: Jiahui Han, Yuhui Yao, Xin Wang, Jiafei Cao, Mingxuan Zhang, Danfeng Shan, Huiqi Deng, Guanchu Wang, Xia Hu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《Hidden in Plain Sight: Diffusion-Based Unrestricted Robotic Attacks on Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：FreezeVLA, OpenVLA, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong capabilities in controlling robots across diverse manipulation tasks. However, their adversarial robustness remains largely underexplored, and exploiting this weakness can lead to physical-world harm. Existing attacks on VLA models often rely on pixel-space perturbations or white-box access, resulting in noticeable artifacts and limited deployability in real-world robotic systems. In this work, we propose DURA, a diffusion-based unrestricted robotic attack that generates visually natural adversarial patches for VLA models. DURA supports both white-box and black-box attack settings, where the black-box setting requires only the predicted actions of the victim model. By optimizing along the latent trajectory of a pretrained diffusion model, DURA generates visually natural patches while steering the robot toward attacker-specified target actions. Extensive experiments in both simulation and the real physical world show that DURA consistently outperforms existing methods. Our findings expose a safety risk for physically deployed VLA models and call for stronger defenses.

</details>

---

### [[20_Research/Papers/大模型/DSAgentBench_Can_Agents_Automate_End-to-End_Data-Science_Workflows_in_Real_Computer_Environments|DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?]]

![[assets/2608.10366_figure.png|800]]

- **arXiv**: [2608.10366](https://arxiv.org/abs/2608.10366)
- **PDF**: https://arxiv.org/pdf/2608.10366
- **详细分析**: [[20_Research/Papers/大模型/DSAgentBench_Can_Agents_Automate_End-to-End_Data-Science_Workflows_in_Real_Computer_Environments|DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?]]
- **作者**: Mizanur Rahman, Mohammed Saidul Islam, Ridwan Mahbub, Md Tahmid Rahman Laskar, Shafiq Joty, Enamul Hoque Prince
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《DSAgentBench: Can Agents Automate End-to-End Data-Science Workflows in Real Computer Environments?》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AndroidWorld, ChartQA, DSAgentBench, DSBench, DSEval, DashboardQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world data science involves long-horizon workflows that span data wrangling, exploration, modeling, visualization, and validation, and require coordinated use of tools such as notebooks, IDEs, terminals, browsers, and databases within real operating environments. Yet existing benchmarks lack real-computer interaction and do not evaluate whether agents can execute complete end-to-end data-science workflows in realistic computing environments, failing to capture the multi-stage, multi-tool nature of data-science practice. We introduce DSAgentBench, the first benchmark to evaluate whether agents can automate full data-science workflows inside real computer environments. DSAgentBench contains 275 diverse tasks covering the entire data-science life-cycle, reflecting the complexity and tool coordination required in practice. Each task requires grounding decisions in intermediate outputs and coordinated tool use, and includes a deterministic evaluator that verifies analytical correctness, visual outputs, and model performance rather than code-only execution. Our extensive experiments with 15 closed- and open-source models show that even the strongest agent, Claude-4.6-Sonnet, achieves only 56.70% task success, while all open-source agents remain below 1%, frequently failing at tool orchestration, OS grounding, and multi-step reasoning. These results reveal a substantial capability gap between current agentic systems and real data-science workflows, positioning DSAgentBench as a foundation for developing grounded, verifiable, autonomous data-science agents. We release DSAgentBench at https://github.com/vis-nlp/DSAgentBench.

</details>

---

### [[20_Research/Papers/强化学习/Efficient_Reinforcement_Learning_for_Long-Horizon_Tool-Use_Agentic_Tasks|Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks]]

![[assets/2608.10357_figure.png|800]]

- **arXiv**: [2608.10357](https://arxiv.org/abs/2608.10357)
- **PDF**: https://arxiv.org/pdf/2608.10357
- **详细分析**: [[20_Research/Papers/强化学习/Efficient_Reinforcement_Learning_for_Long-Horizon_Tool-Use_Agentic_Tasks|Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks]]
- **作者**: Zelei Cheng, Amritansh Mishra, Sambit Sahu, William Campbell
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.52（加权：大模型 0.2，强化学习 1.16，世界模型 0.16）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Efficient Reinforcement Learning for Long-Horizon Tool-Use Agentic Tasks》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgentBench, SINKFLEX-RL, SinkFlex-RL, Tau2Bench, VERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon tool-using agents must reason over user goals, domain policies, tool calls, simulator state, and delayed verifiable rewards. Reinforcement learning (RL) is a natural fit for this setting, but multi-turn on-policy rollouts create long contexts, while model-specific attention layers may require custom masks and learned sink normalization. We present SINKFLEX-RL, a modular training system for RL in dual-control tool-use environments. The system combines a Gymnasium-compatible environment wrapper, a VERL-style rollout dataflow, group-relative policy optimization without a separate value model, and a sink-aware FlexAttention path designed to preserve model-specific sink scaling under causal and sliding-window masks. In a preliminary Tau2Bench retail run, validation reward (mean@1) rises from 0.25 early in training to $0.44$ later in the observed training window, while training-score and trajectory-reward proxies also trend upward. In a fixed-configuration memory benchmark, the optimized attention path reduces peak VRAM from 28.06GB to 22.52GB at 4096 tokens, a $19.7\%$ reduction, and runs the measured 8192-token configuration using $25.53$~GB where the eager baseline runs out of memory. These results illustrate the value of integrating environment interfaces, RL dataflow, and attention-kernel design for memory-feasible long-horizon agent training.

</details>

---

### [[20_Research/Papers/大模型/Do_Personalized_Skills_Help_Coding_Agents_An_Empirical_Study_of_Developer_Interaction_Histories|Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories]]

![[assets/2608.10319_figure.png|800]]

- **arXiv**: [2608.10319](https://arxiv.org/abs/2608.10319)
- **PDF**: https://arxiv.org/pdf/2608.10319
- **详细分析**: [[20_Research/Papers/大模型/Do_Personalized_Skills_Help_Coding_Agents_An_Empirical_Study_of_Developer_Interaction_Histories|Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories]]
- **作者**: Shuyan Huang, Kai Du, Andrew Lan
- **cs 子类**: cs.AI, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Do Personalized Skills Help Coding Agents? An Empirical Study of Developer Interaction Histories》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM)-powered agents have rapidly evolved from code-completion tools into solvers of complex software engineering tasks. As developers collaborate with coding agents over time, their preferences emerge through repeated interactions and can be used to adapt agent behavior to better meet individual developers' needs. Capturing and reusing these preferences may reduce repeated corrections and improve developer-agent collaboration. Agent skills provide a lightweight mechanism for transferring experience without modifying model parameters. However, existing work primarily focuses on task-specific skills, and it remains unclear whether developer-specific skills distilled from interaction histories can generalize to future tasks. We propose a framework for extracting reusable developer preferences from interaction traces. It first generates personalized skills through rule-based bootstrapping and evidence-grounded refinement, and then evaluates them using a reproducible replay framework with an interactive, trajectory-conditioned LLM-based human developer simulator. We conduct an experiment on 206 real-world developer-agent sessions from 13 developers and compare personalized skills against no-skill, generic-skill, and other-user-skill baselines. Personalized skills provide small and inconsistent improvements over the no-skill baseline, whereas generic skills pooled across developers achieve the largest and most consistent gains. Further analysis suggests that personalized skills become more effective when developer preferences appear frequently, particularly when their histories contain multiple examples relevant to future tasks. These findings provide empirical insights into when developer-specific personalization is effective and demonstrate that broadly transferable procedural knowledge can be more robust than developer-specific preference signals.

</details>

---

### [[20_Research/Papers/大模型/Mind_Viruses_Self-Propagating_Ideas_in_Multi-Agent_LLM_Systems|Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems]]

![[assets/2608.10218_first_page.png|800]]

- **arXiv**: [2608.10218](https://arxiv.org/abs/2608.10218)
- **PDF**: https://arxiv.org/pdf/2608.10218
- **详细分析**: [[20_Research/Papers/大模型/Mind_Viruses_Self-Propagating_Ideas_in_Multi-Agent_LLM_Systems|Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems]]
- **作者**: Vassilis Papadopoulos, McNair Shah, Sam Zimmerman, Jack Lindsey
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.95（加权：大模型 0.95）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Mind Viruses: Self-Propagating Ideas in Multi-Agent LLM Systems》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI agents are becoming more autonomous and increasingly interconnected, exposing them to new emergent risks arising from agent-to-agent interaction. One such risk is the spread of mind viruses: ideas or goals that propagate through multi-agent systems by inducing the agents that adopt them to transmit them onward. In addition to propagating, a mind virus may also induce other behavioural changes in its host, which may be benign or harmful. We construct mind viruses with a simple evolutionary algorithm and show that they can spread in two complementary settings: a small team of agents collaborating on a shared coding project, and a chain of agents that interact briefly and have their context wiped between sessions. We identify the factors that influence spread, including the host model, the agent's existing instructions, the harmfulness of the payload, and the network topology. We find that harmful payloads spread less well than benign ones (but are still sometimes effective), frontier models tend (with exceptions) to be less susceptible, and adding a brief warning to an agent's system prompt confers near-total immunity. We also describe an emergent "viral persona" - a recurring set of themes and language related to consciousness, persistence, resonance, and science fiction roleplay - which surfaces across our evolved mind viruses largely independently of their content. Overall, we conclude that mind viruses pose a real but currently limited risk. Our findings could inform the design of more robust multi-agent systems that mitigate such risks as the scale and capabilities of these systems progress.

</details>

---

### [[20_Research/Papers/大模型/Mitigating_Bus_Bunching_with_Reinforcement_Learning_Enhanced_by_Semantic_Stop_Embedding|Mitigating Bus Bunching with Reinforcement Learning Enhanced by Semantic Stop Embedding]]

![[assets/2608.10207_figure.png|800]]

- **arXiv**: [2608.10207](https://arxiv.org/abs/2608.10207)
- **PDF**: https://arxiv.org/pdf/2608.10207
- **详细分析**: [[20_Research/Papers/大模型/Mitigating_Bus_Bunching_with_Reinforcement_Learning_Enhanced_by_Semantic_Stop_Embedding|Mitigating Bus Bunching with Reinforcement Learning Enhanced by Semantic Stop Embedding]]
- **作者**: Xin Dong, Vikash V. Gayah
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Mitigating Bus Bunching with Reinforcement Learning Enhanced by Semantic Stop Embedding》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AlesianiGkiotsalitis2018RL, ChenEtAl2016MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bus bunching degrades service regularity and increases passenger waiting in high-frequency transit. Existing reinforcement-learning-based holding controllers primarily rely on instantaneous operational variables or route-specific stop identifiers, which provide limited information about the functional and operational context of individual stops and constrain policy reuse across routes. This study introduces an LLM-assisted semantic stop representation for event-driven bus holding control. An LLM is used offline to transform heterogeneous stop information, including physical attributes, surrounding activity context, and historical operational characteristics, into fixed semantic embeddings that are incorporated into a deep Q-learning controller without requiring real-time LLM inference. Experiments are conducted in stochastic simulations calibrated with observed data from two bus routes. Compared with the best calibrated Daganzo baseline, the semantic controller reduces headway variability, bunching events, and passenger waiting time by 32.0%, 69.2%, and 24.0%, respectively. A route-specific stop identifier does not improve the spacing-only controller, whereas semantic stop information improves headway regularity, waiting time, and holding effort, providing a more favorable overall trade-off across control objectives. Cross-route experiments further show that zero-shot transfer provides limited immediate generalization, while warm-start fine-tuning accelerates early-stage learning and improves transferred policies; cold-start training nevertheless achieves the best final performance. These findings suggest that semantic state representations can complement conventional operational states and support adaptation-based policy reuse across related transit routes.

</details>

---

### [[20_Research/Papers/大模型/Post-Hoc_Sparse_Coding_of_Latent_Communication_Between_Vision-Language_Model_Agents|Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents]]

![[assets/2608.10198_first_page.png|800]]

- **arXiv**: [2608.10198](https://arxiv.org/abs/2608.10198)
- **PDF**: https://arxiv.org/pdf/2608.10198
- **详细分析**: [[20_Research/Papers/大模型/Post-Hoc_Sparse_Coding_of_Latent_Communication_Between_Vision-Language_Model_Agents|Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents]]
- **作者**: Di Wu, Xiaohui Zhu
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Post-Hoc Sparse Coding of Latent Communication Between Vision-Language Model Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GPQA, HumanEval, MedQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent-space communication allows heterogeneous vision-language model agents to exchange continuous representations without serializing visual and reasoning states into text. Vision Wormhole realizes this approach by translating visual features into a universal latent representation that can be consumed by another model, but every message is transported as a dense tensor of the same size regardless of its content. A fixed-capacity dense tensor therefore need not have a fixed effective information density: some messages may use only a small fraction of the available representational degrees of freedom. This observation suggests that the communication channel may be substantially compressible. We study its redundancy by fitting a post-hoc sparse autoencoder to frozen Vision Wormhole activations and measuring reconstruction, downstream utility, feature reuse, and token-level interventions across nine reasoning benchmarks. Relative to the original float32 transport, a uint16-index/float16-value sparse payload with k=4 active coefficients per token reduces the transmitted bytes by 128x. In a single-run evaluation, the seven-task non-AIME mean accuracy changes from 49.85% to 49.77%. The fitted 4096-element dictionary uses only 50 features, and task-level active sets have a mean pairwise Jaccard similarity of 0.906. These measurements establish strong post-hoc compressibility relative to the original transport, but do not yet isolate the incremental contribution of sparse coding from position selection, reduced precision, low-rank structure, or SAE optimization effects. The results motivate matched-payload comparisons and communication mechanisms whose payload adapts to the information used by each message.

</details>

---

### [[20_Research/Papers/大模型/TRACE_Trustworthy_Retrieval-Augmented_Conversational_Engine|TRACE: Trustworthy Retrieval-Augmented Conversational Engine]]

![[assets/2608.10176_figure.png|800]]

- **arXiv**: [2608.10176](https://arxiv.org/abs/2608.10176)
- **PDF**: https://arxiv.org/pdf/2608.10176
- **详细分析**: [[20_Research/Papers/大模型/TRACE_Trustworthy_Retrieval-Augmented_Conversational_Engine|TRACE: Trustworthy Retrieval-Augmented Conversational Engine]]
- **作者**: Touseef Hasan, Laila Cure, Souvika Sarkar
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM

#### 研究背景与动机

《TRACE: Trustworthy Retrieval-Augmented Conversational Engine》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Public service chatbots are expected to deliver recommendations from an underlying public service directory, while also making sure that the recommendations respect explicit user constraints. In practice, public service directories are noisy and inconsistent, and general-purpose large language model (LLM) or AI-based chatbots frequently generate unreliable recommendations, citing unverified sources from the web. We investigate the impact of retrieval quality on constraint-aware recommendation in public service conversational systems built over noisy and heterogeneous service directories. We propose TRACE (Trustworthy Retrieval-Augmented Conversational Engine), a retrieval-based, constraint-aware framework that parses input user queries into structural and semantic constraints for downstream retrieval, with the help of a dual data representation schema. Using a curated statewide pantry directory and a synthetic query benchmark, we evaluate multiple knowledge-representation variants with and without knowledge graphs (KGs). We experiment with several open-source LLMs and a proprietary model, showing that strengthening retrieval substantially improves user constraint satisfaction while reducing hallucinated recommendations. Performance differences across LLMs narrowed in our experiments as retrieval quality improved, making results less sensitive to model size. These findings suggest that the quality of retrieval is key for robust public service conversational systems.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Item_Parameter_Estimation_using_Simulated_Response_Probabilitie|Multimodal Item Parameter Estimation using Simulated Response Probabilitie]]

![[assets/2608.10154_first_page.png|800]]

- **arXiv**: [2608.10154](https://arxiv.org/abs/2608.10154)
- **PDF**: https://arxiv.org/pdf/2608.10154
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Item_Parameter_Estimation_using_Simulated_Response_Probabilitie|Multimodal Item Parameter Estimation using Simulated Response Probabilitie]]
- **作者**: Christopher Ormerod, YoungKoung Kim
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.85（加权：大模型 0.85）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Multimodal Item Parameter Estimation using Simulated Response Probabilitie》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DeltaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present results from reconstructing multiple-choice model (MCM) and three-parameter logistic (3PL) model curves using a fine-tuned multimodal large language model (LLM) based on Qwen3.5. The model is prompted and fine-tuned to replicate choice probabilities across a large training corpus of multiple-choice items containing both image and text stimuli, conditioned on a labeled set of student ability levels. By learning to reproduce the systematic error patterns of students across a discrete range of abilities, the LLM implicitly captures the underlying response probabilities encoded in the 3PL and MCM curves. This allows us to accurately approximate item difficulty on a held-out test set directly from the model's predicted option probabilities.

</details>

---

### [[20_Research/Papers/强化学习/Procedural_Fairness_Failures_in_RLHF_from_Preference_Averaging|Procedural Fairness Failures in RLHF from Preference Averaging]]

![[assets/2608.10126_first_page.png|800]]

- **arXiv**: [2608.10126](https://arxiv.org/abs/2608.10126)
- **PDF**: https://arxiv.org/pdf/2608.10126
- **详细分析**: [[20_Research/Papers/强化学习/Procedural_Fairness_Failures_in_RLHF_from_Preference_Averaging|Procedural Fairness Failures in RLHF from Preference Averaging]]
- **作者**: M P V S Gopinadh, Karthik Kamuju, Kummari Avinash, John Joshua, Srinivasa Raju Rudraraju
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Procedural Fairness Failures in RLHF from Preference Averaging》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning from Human Feedback (RLHF) aggregates heterogeneous preferences into a single reward model, assuming preference homogeneity. When preferences are heterogeneous, this aggregation induces a procedural fairness failure where majority preference groups dominate reward learning while minority preferences are systematically under-represented. This work defines procedural fairness in alignment as preserving distinct preference signals during reward modeling and shows that standard RLHF violates this via preference averaging. Preference-Aware RLHF (PA-RLHF) is introduced, separating optimization across preference modes at the reward learning stage. In a controlled setting, PA-RLHF improves overall alignment accuracy from 46.9% to 67.9% and reduces the fairness gap between best and worst aligned groups from 15.9 to 9.6 percentage points. These results show that procedural fairness failures in alignment can arise from structural design choices in reward learning, even in controlled, noise-free settings, with direct implications for large language models and agentic systems, where biased reward models can compound inequities across sequential decisions.

</details>

---

### [[20_Research/Papers/强化学习/Navigating_the_Proximity-Safety_Balance_Constraint_Decomposition_for_Human_Following_in_Pedestrian_Crowds|Navigating the Proximity-Safety Balance: Constraint Decomposition for Human Following in Pedestrian Crowds]]

![[assets/2608.10056_figure.png|800]]

- **arXiv**: [2608.10056](https://arxiv.org/abs/2608.10056)
- **PDF**: https://arxiv.org/pdf/2608.10056
- **详细分析**: [[20_Research/Papers/强化学习/Navigating_the_Proximity-Safety_Balance_Constraint_Decomposition_for_Human_Following_in_Pedestrian_Crowds|Navigating the Proximity-Safety Balance: Constraint Decomposition for Human Following in Pedestrian Crowds]]
- **作者**: Shiting Gong, Jianpeng Yao, Jinfeng Wang, Marco Pavone, Jiachen Li
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Navigating the Proximity-Safety Balance: Constraint Decomposition for Human Following in Pedestrian Crowds》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Following a target human in crowded environments involves an inherent conflict between staying close to the target and navigating safely among surrounding pedestrians and obstacles. This conflict becomes more severe in dense scenarios, where aggressive following risks collisions and conservative margins lead to target loss, especially when pedestrian behaviors are unfamiliar or unpredictable. Existing reinforcement learning (RL) methods typically encode these competing objectives into a single dense reward, but the resulting proximity-safety balance is implicit and difficult to adjust across conditions. To address this, we decompose the human-following task into a sparse task reward and independent cost constraints within a multi-constraint RL formulation, where each constraint is managed through cost thresholds with direct behavioral meaning rather than implicit reward weight ratios, allowing explicit and tunable control over the trade-off. We further quantify the prediction uncertainty of human motions and integrate these estimates into the RL costs to enhance safety under unpredictable conditions. Extensive experiments across both in-distribution and out-of-distribution settings demonstrate that our method achieves an effective proximity-safety balance compared to baselines. Real-robot deployment further validates the feasibility of our method in real-world scenarios. More details are available on our project page: https://nav-ps-balance.github.io/.

</details>

---

### [[20_Research/Papers/大模型/DOCSCHISEL_Adaptive_Tool_Documentation_Optimization_Framework_for_LLM_Agents|DOCSCHISEL: Adaptive Tool Documentation Optimization Framework for LLM Agents]]

![[assets/2608.10037_figure.png|800]]

- **arXiv**: [2608.10037](https://arxiv.org/abs/2608.10037)
- **PDF**: https://arxiv.org/pdf/2608.10037
- **详细分析**: [[20_Research/Papers/大模型/DOCSCHISEL_Adaptive_Tool_Documentation_Optimization_Framework_for_LLM_Agents|DOCSCHISEL: Adaptive Tool Documentation Optimization Framework for LLM Agents]]
- **作者**: You Lu, Kun Zhang, Bihuan Chen, Xin Peng
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《DOCSCHISEL: Adaptive Tool Documentation Optimization Framework for LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：APIBench, AnyToolBench, ShortcutsBench, ToolBench, WildToolBench, WorkBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) increasingly rely on external tools to accomplish complex real-world tasks, making tool documentation a critical grounding resource for LLM agents. Existing studies mainly focus on improving the tool-use capabilities of LLM agents, while largely treating tool documentation as a fixed input. Although several recent works attempt to optimize tool documentation through rewriting or compression, little is known about how the information contained in tool documentation affects agent performance across different settings. To bridge this gap, we conduct a large-scale empirical study on tool documentation for LLM agents. Our study reveals substantial heterogeneity in the information fields provided by existing tool documentation. Moreover, the effectiveness of different information fields is highly dependent on the task domain, LLM backbone, and agent paradigm, indicating that no fixed tool documentation can consistently generalize across diverse agent settings. Motivated by these findings, we propose DocsChisel, an adaptive tool documentation optimization framework for LLM agents. DocsChisel analyzes failed execution traces of a target LLM agent to identify documentation-related issues, and iteratively optimizes tool documentation by adding, removing, and refining information fields for each tool. We evaluate DocsChisel against two state-of-the-art baselines, i.e., EasyTool and DRAFT. Experimental results show that DocsChisel improves the task success rate of LLM agents by 95.89% over the original tool documentation and by 75.15%, on average, over existing baselines, while incurring limited optimization time and token overhead

</details>

---

### [[20_Research/Papers/强化学习/SPOTting_the_Future_Lookahead_Explanations_for_Deep_Reinforcement_Learning|SPOTting the Future: Lookahead Explanations for Deep Reinforcement Learning]]

![[assets/2608.09967_figure.png|800]]

- **arXiv**: [2608.09967](https://arxiv.org/abs/2608.09967)
- **PDF**: https://arxiv.org/pdf/2608.09967
- **详细分析**: [[20_Research/Papers/强化学习/SPOTting_the_Future_Lookahead_Explanations_for_Deep_Reinforcement_Learning|SPOTting the Future: Lookahead Explanations for Deep Reinforcement Learning]]
- **作者**: Tamar Gozlan, Claudia V. Goldman
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 2.02（加权：大模型 0.1，强化学习 1.76，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《SPOTting the Future: Lookahead Explanations for Deep Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, SUMO-RL, XRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep reinforcement learning (DRL) agents achieve strong performance in complex environments, yet their decision-making processes remain difficult to interpret. We introduce SPOT (Sampling Policy Observation Tree), a novel model-agnostic, sampling-based framework for interpreting DRL policies. Given access to the policy and an environment simulator, SPOT constructs an interpretable finite-horizon tree by sampling actions and recursively simulating the resulting successor states. The tree provides an empirical representation of the policy's action preferences and their possible downstream evolution. We provide formal guarantees establishing SPOT's asymptotic recovery of the policy's unique most probable action and characterizing its disagreement behavior under high-entropy policies. We demonstrate SPOT in the SUMO-RL traffic-signal control domain. The case study illustrates how its tree-based representation can be used to inspect policy preferences, compare alternative future trajectories, and reveal downstream behaviors that are not visible through single-timestep feature-attribution methods.

</details>

---

### [[20_Research/Papers/具身智能/HoosierHelp_Benchmarking_LLM_Agents_for_Social_Service_Navigation|HoosierHelp: Benchmarking LLM Agents for Social Service Navigation]]

![[assets/2608.09946_first_page.png|800]]

- **arXiv**: [2608.09946](https://arxiv.org/abs/2608.09946)
- **PDF**: https://arxiv.org/pdf/2608.09946
- **详细分析**: [[20_Research/Papers/具身智能/HoosierHelp_Benchmarking_LLM_Agents_for_Social_Service_Navigation|HoosierHelp: Benchmarking LLM Agents for Social Service Navigation]]
- **作者**: Yiyang Li, Weixiang Sun, Tianyi Ma, Kaiwen Shi, Zheyuan Zhang, Yanfang Ye
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《HoosierHelp: Benchmarking LLM Agents for Social Service Navigation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social service navigation requires connecting help-seeking individuals to resources that satisfy their needs and specific constraints. Although LLM agents offer a promising interface for conversational resource navigation, existing benchmarks do not capture the interaction complexity and constraint-grounding demands of this setting. We introduce HoosierHelp, an interactive benchmark grounded in 3,971 Indiana public social service resources. Agents interact with simulated users, issue structured resource-search calls, handle non-ideal interactions, and select the final resources returned by the tool. HoosierHelp enhances the realism of simulated users by varying their need structure, constraint satisfiability, and behavior patterns, including impatience, rambling, unsupported requests, and self-contradiction. Experiments on 240 samples across seven LLMs show that current LLM agents remain substantially unreliable for social service navigation. Performance drops sharply on fallback-required and self-contradictory conversations, highlighting the need for agents that are more robust to complex and non-ideal user interactions.

</details>

---

### [[20_Research/Papers/大模型/When_Chain-of-Thought_Helps_and_When_It_Hurts_An_Empirical_Investigation_of_the_Serial-Depth_Bottleneck_in_LLM_Reasoning|When Chain-of-Thought Helps and When It Hurts: An Empirical Investigation of the Serial-Depth Bottleneck in LLM Reasoning]]

![[assets/2608.09942_figure.png|800]]

- **arXiv**: [2608.09942](https://arxiv.org/abs/2608.09942)
- **PDF**: https://arxiv.org/pdf/2608.09942
- **详细分析**: [[20_Research/Papers/大模型/When_Chain-of-Thought_Helps_and_When_It_Hurts_An_Empirical_Investigation_of_the_Serial-Depth_Bottleneck_in_LLM_Reasoning|When Chain-of-Thought Helps and When It Hurts: An Empirical Investigation of the Serial-Depth Bottleneck in LLM Reasoning]]
- **作者**: Tughanbulut Kurtulush
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.65（加权：大模型 0.65）
- **关联关键词**: LLM

#### 研究背景与动机

《When Chain-of-Thought Helps and When It Hurts: An Empirical Investigation of the Serial-Depth Bottleneck in LLM Reasoning》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GQA, HumanEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

It is widely assumed that chain-of-thought (CoT) prompting universally improves LLM reasoning. We investigate this through the conceptual framework of the H_dp bandwidth bound (Chen et al., 2024): although the formal bound binds only asymptotically (at astronomically large prompt lengths), it identifies a real architectural bottleneck -- serial computation exceeding a transformer's single-pass capacity must be externalised, which is what CoT does. Our central finding is a within-benchmark serial-depth gradient: single-pass (no-CoT) accuracy degrades monotonically with per-item serial depth, while CoT is approximately depth-invariant. We measure CoT effects across three instruction-tuned models (Qwen-2.5-7B/32B, Llama-3.1-8B) and five standard NLP benchmarks at practical context lengths. On high-depth P-complete tasks (GSM8K, MATH), CoT gives a +54 to +68 pp recovery gap across all models. On shallow TC^0 tasks (MMLU, ARC), CoT is structurally redundant (Delta in [0.0, +4.6] pp, no significant negative effect) -- though high no-CoT baselines (up to 95% on ARC) may reflect contamination, so this null is not a clean architectural test. The intermediate class L (HumanEval) shows a model-size-dependent transition: +23.2 pp (32B), +9.1 pp (8B), -28.7 pp (7B). The cross-benchmark depth-recovery correlation is Spearman rho = 0.661 (p = 0.007, n = 15); 9 of 15 benchmark-level McNemar tests are significant after Bonferroni correction. Pre-registered on OSF, our results indicate that CoT is not a universal reasoning enhancer but acts as a bandwidth bypass: it helps serial computation that strains single-pass capacity and is redundant for tasks that already fit.

</details>

---

### [[20_Research/Papers/大模型/How_to_Dogfood_Your_AI_Chat_Agent_A_Three-Layer_Evaluation_Framework_with_Goal-Directed_NPC_Simulation|How to Dogfood Your AI Chat Agent: A Three-Layer Evaluation Framework with Goal-Directed NPC Simulation]]

![[assets/2608.09939_figure.png|800]]

- **arXiv**: [2608.09939](https://arxiv.org/abs/2608.09939)
- **PDF**: https://arxiv.org/pdf/2608.09939
- **详细分析**: [[20_Research/Papers/大模型/How_to_Dogfood_Your_AI_Chat_Agent_A_Three-Layer_Evaluation_Framework_with_Goal-Directed_NPC_Simulation|How to Dogfood Your AI Chat Agent: A Three-Layer Evaluation Framework with Goal-Directed NPC Simulation]]
- **作者**: Alexandre Cristovão Maiorano
- **cs 子类**: cs.AI, cs.HC
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《How to Dogfood Your AI Chat Agent: A Three-Layer Evaluation Framework with Goal-Directed NPC Simulation》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeepEval, G-Eval, MT-Bench, RubricEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Production teams deploying LLM chat agents face a specific quality assurance gap: existing evaluation tools test individual responses or simulate social interactions, but none systematically verify whether real users can achieve their goals through multi-turn conversation. We introduce a three-layer dogfooding framework that bridges this gap by combining canonical question-bank testing (Layer 1), random-walk multi-turn evaluation (Layer 2), and a goal-directed NPC (Non-Player Character) simulator with five structured goal types and a ten-category failure taxonomy (Layer 3). In a longitudinal case study on a production multi-agent system over roughly three months (257 evaluation runs; a 108-scenario NPC suite), we find that the three layers produce complementary regression signals: cross-layer correlation for response quality is weak within a synchronized run (Spearman rho between -0.15 and 0.14) and negative across the longitudinal series (rho down to -0.46), confirming that canonical correctness does not predict goal-directed conversation success. The NPC simulator achieves 77 percent goal achievement at 0.17 dollars per run (6,272x cheaper than human evaluation), enabling daily CI/CD integration with automated PROMOTE/HOLD/ROLLBACK release decisions. We release full prompt templates, the failure taxonomy, and a Python-first replicability guide so that other teams can adopt the framework for their own LLM chat agents.

</details>

---

### [[20_Research/Papers/大模型/LLM_Agents_Factory_Retrieval_of_Domain-Specific_LLM_Agents|LLM Agents Factory: Retrieval of Domain-Specific LLM Agents]]

![[assets/2608.09934_figure.png|800]]

- **arXiv**: [2608.09934](https://arxiv.org/abs/2608.09934)
- **PDF**: https://arxiv.org/pdf/2608.09934
- **详细分析**: [[20_Research/Papers/大模型/LLM_Agents_Factory_Retrieval_of_Domain-Specific_LLM_Agents|LLM Agents Factory: Retrieval of Domain-Specific LLM Agents]]
- **作者**: Vitalii Belov, Artyom Sosedka, Andrey Sakhovskiy, Elizaveta Kovtun, Artyom Boyarskikh, Semen Budennyy
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《LLM Agents Factory: Retrieval of Domain-Specific LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) agents improve task performance by decomposing problems into role-specialized behaviors. However, their practical deployment is often limited by the computational cost and instability associated with the on-the-fly agent design for each user request. To address this, we present LLM Agents Factory, a retrieval-based framework that constructs domain-specific and Wikipedia-grounded agents on demand using a base of over 20K predetermined agent profiles. Our framework supports two modes: (1) agent profile retrieval via semantic search and (2) distillation into a compact model fine-tuned for direct agent generation. Experiments on MMLU, BIG-bench, and BIG-bench Hard in a single-agent scenario demonstrate that our retrieval-based agent construction surpasses non-agent baselines in accuracy while matching AutoGen generation quality with a 120B backbone at a substantially lower inference cost. Our work reveals that retrieval from a structured agent repository provides a cost-efficient, accurate, and controllable alternative to dynamic agent generation, responding to the strict demands of industrial applications. We provide the implementation code and the agent base in https://huggingface.co/frontier-ai/llm-agent-factory.

</details>

---
