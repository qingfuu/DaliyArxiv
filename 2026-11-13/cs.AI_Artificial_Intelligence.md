# cs.AI | Artificial Intelligence | 2026-11-13

#arxiv #ComputerScience

**论文数**: 20

### [[20_Research/Papers/大模型/CapLite_Prompt-Injection_Defense_for_Small_Language_Model_Agents_without_Model-Written_Security_Artifacts|CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts]]

![[assets/2611.17115_figure.png|800]]

- **arXiv**: [2611.17115](https://arxiv.org/abs/2611.17115)
- **PDF**: https://arxiv.org/pdf/2611.17115
- **详细分析**: [[20_Research/Papers/大模型/CapLite_Prompt-Injection_Defense_for_Small_Language_Model_Agents_without_Model-Written_Security_Artifacts|CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts]]
- **作者**: Zimo Xu, Wenzhuo Liu, Hideki Nakayama
- **cs 子类**: cs.AI, cs.CL, cs.CR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.05（加权：大模型 1.05）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《CapLite: Prompt-Injection Defense for Small Language Model Agents without Model-Written Security Artifacts》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enforcement defenses against prompt injection, such as CaMeL, Progent, IPIGuard and DRIFT, ask the agent's own model to write a security artifact (a program, a privilege policy, a dependency graph or a constraint list) that code then enforces. We ask whether small language model (SLM) agents can be trusted to write these artifacts. Across 15 open-weight models, 13 of them between 1.7B and 12B parameters, they cannot: the policies, graphs and constraints that the agent's model writes admit attacks on 14 (Progent), 13 (IPIGuard) and 11 (DRIFT) of the models, and CaMeL's programs fail to run in up to 68% of episodes. We present CapLite, which derives its policy from the tool schemas, commits the write calls before any tool result is read, and admits a write only if every argument that decides whom or what it affects is stated in the user's request. This guarantees write integrity: injected text cannot add a write, and no write reaches a recipient, amount, object or destination that the user did not state. No attack succeeds in 13,935 attacked AgentDojo episodes. CapLite reaches utility under attack comparable to CaMeL's (29.0% vs. 27.2%) with fewer tokens than every other enforcement defense and than the undefended agent: 17.1k per episode, 18% of CaMeL's, and the highest utility per token of all enforcement defenses.

</details>

---

### [[20_Research/Papers/具身智能/SALA_Semantically_Aligned_Latent_Actions_Enable_Dual-Axis_Scaling_of_Embodied_Foundation_Models|SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models]]

![[assets/2611.17110_figure.png|800]]

- **arXiv**: [2611.17110](https://arxiv.org/abs/2611.17110)
- **PDF**: https://arxiv.org/pdf/2611.17110
- **详细分析**: [[20_Research/Papers/具身智能/SALA_Semantically_Aligned_Latent_Actions_Enable_Dual-Axis_Scaling_of_Embodied_Foundation_Models|SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models]]
- **作者**: Jiachun Jin, Zetong Zhou, Haonan Wang, Xiao Yang, Jun Zhu, Zhijie Deng
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《SALA: Semantically Aligned Latent Actions Enable Dual-Axis Scaling of Embodied Foundation Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied foundation models hinge on diverse robot interaction data, which are costly to collect. Egocentric human videos offer a complementary source of experience, and latent action models (LAMs) provide a popular means of leveraging these videos for policy supervision. Compared with world-action models (WAMs), LAMs can offer greater training efficiency and potentially lower inference costs by avoiding explicit pixel prediction during policy learning and execution. However, most existing LAMs learn latent actions solely through video reconstruction, which can cause their representations to cluster by visual appearance rather than by the underlying actions. As a result, they struggle to align human actions with their robot counterparts. To bridge the gap, we introduce SALA, which emphasizes establishing the semantic correspondence for latent actions. Without requiring paired data, we use the language descriptions of unpaired human and robot clips to estimate semantic similarities and supervise cross-embodiment correspondence. Specifically, we translate these similarities into soft neighborhood structures that guide human latent actions toward semantically related robot latents, while robot action reconstruction grounds the latent space in control. The resulting shared latent action space provides a unified supervision signal for training an embodied foundation model on both human and robot videos. Notably, latent action supervision enables scaling along two axes: (1) pre-training on increasing amounts of general human video consistently reduces robot action prediction error on downstream tasks, and (2) post-training on increasing amounts of task-specific human video substantially improves real-world robot task success rates.

</details>

---

### [[20_Research/Papers/具身智能/AgriSense_Vision-Language_Decision_Support_and_Robotic_Intervention_in_a_Virtual_Greenhouse_Copy_title|AgriSense: Vision-Language Decision Support and Robotic Intervention in a Virtual Greenhouse Copy title]]

![[assets/2611.16752_figure.png|800]]

- **arXiv**: [2611.16752](https://arxiv.org/abs/2611.16752)
- **PDF**: https://arxiv.org/pdf/2611.16752
- **详细分析**: [[20_Research/Papers/具身智能/AgriSense_Vision-Language_Decision_Support_and_Robotic_Intervention_in_a_Virtual_Greenhouse_Copy_title|AgriSense: Vision-Language Decision Support and Robotic Intervention in a Virtual Greenhouse Copy title]]
- **作者**: Lyes Saad Saoud, Oualid Doukhi, Reza Ghorbani, Moussa Ayyash
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《AgriSense: Vision-Language Decision Support and Robotic Intervention in a Virtual Greenhouse Copy title》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous greenhouse management increasingly requires robotic systems that integrate perception, navigation, environmental regulation, and plant-level intervention. This paper presents AgriSense, a framework combining an Isaac Sim virtual greenhouse, a quadruped mobile manipulator, RGB and LiDAR-inertial sensing, environmental control, and supervised vision-language decision support. Frozen DINOv2 and BERT encoders, together with structured environmental inputs, support joint prediction of twelve environmental references, a target zone, and an intervention flag. Checkpoint replay reproduces 41/43 zone decisions. Across five seeds on a source-grouped test set, the full, image-removed, and language-removed configurations each achieve 43/44 correct zone decisions, providing no evidence of incremental multimodal zone-accuracy improvement. The full model achieves mean absolute errors of 0.249 degrees C for temperature, 2.030 percentage points for humidity, and 0.997 percentage points for soil moisture. Sensor-only inputs match full-model zone accuracy, while language-only inputs achieve 68.64%. External real-image benchmarks reveal distribution-shift limitations. Five offline Point-LIO routes yield rigidly aligned trajectory errors of 5.22-17.32 mm. Of 40 virtual-arm targets, 32 satisfy geometric acceptance criteria and eight are rejected at boundaries. Six long-horizon climate cases and fault protocols characterize integration limits. Navigation and integrated treatment rely on simulator-state inputs; physical greenhouse performance and agronomic treatment efficacy remain unvalidated. The contribution is an evaluated decision-support and robotic-intervention framework for a virtual greenhouse.

</details>

---

### [[20_Research/Papers/机器人/EgoX_Egocentric_Cross-Embodiment_Manipulation_with_Embodiment_Dreaming|EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming]]

![[assets/2611.16728_figure.png|800]]

- **arXiv**: [2611.16728](https://arxiv.org/abs/2611.16728)
- **PDF**: https://arxiv.org/pdf/2611.16728
- **详细分析**: [[20_Research/Papers/机器人/EgoX_Egocentric_Cross-Embodiment_Manipulation_with_Embodiment_Dreaming|EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming]]
- **作者**: Yaru Niu, Binghong Chen, Changwei Yao, Shangtao Li, Zhenlong Fang, Revanth Krishna Senthilkumaran, Shuai Zhou, Yuemin Mao, Kalie Ching, Po-Ju Chao, Yudong Luo, Peiqi Yu...
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《EgoX: Egocentric Cross-Embodiment Manipulation with Embodiment Dreaming》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：G1-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist manipulation policies can benefit from the complementary experience of humans, real robots, and simulated agents. However, differences in morphology, sensing, and control interfaces make it difficult to learn effectively from their combined demonstrations. We introduce EgoX, an egocentric cross-embodiment learning framework that organizes heterogeneous demonstrations through semantically corresponding observation and action modalities. EgoX pretrains a Modularized Cross-Embodiment Transformer with Embodiment Dreaming (MXT+) on this mixture and fine-tunes it on target-embodiment demonstrations. Within each embodiment, MXT+ assigns a dedicated tokenizer to each observation modality and a dedicated expert to each action modality, with a Transformer trunk shared across embodiments. A training-only embodiment-dreaming objective predicts latent representations of future visual and proprioceptive states, encouraging the shared trunk to model each embodiment's dynamics. Across 13 task-embodiment pairs spanning five tasks and six robot embodiments, including five physical robots and one simulated humanoid, cross-embodiment pretraining raises MXT+'s average normalized task progress from 0.63 to 0.80 over training from scratch. The gains are particularly pronounced under out-of-distribution conditions, where average task progress increases from 0.53 to 0.77. Ablations demonstrate the benefits of broader pretraining mixtures, modular interfaces, and embodiment dreaming, with dreaming producing more similar latent geometry across embodiments. Project page: egox-dream.github.io.

</details>

---

### [[20_Research/Papers/具身智能/AstroMemBench_A_Benchmark_for_Memory_Systems_in_Embodied_Spacecraft_Agents|AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents]]

![[assets/2611.16590_first_page.png|800]]

- **arXiv**: [2611.16590](https://arxiv.org/abs/2611.16590)
- **PDF**: https://arxiv.org/pdf/2611.16590
- **详细分析**: [[20_Research/Papers/具身智能/AstroMemBench_A_Benchmark_for_Memory_Systems_in_Embodied_Spacecraft_Agents|AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents]]
- **作者**: You Wu, Guhong Zhang, Hongwei Li, Xinyue Hong, Yuan Jia
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.7，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《AstroMemBench: A Benchmark for Memory Systems in Embodied Spacecraft Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AMA-Bench, AstroAgentBench, AstroMemBench, LMEE-Bench, LongMemEval, Mem2ActBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term spacecraft autonomy requires embodied agents to use operational history under communication delays, time-critical operations, environmental uncertainty, complex physical interactions, power and computational constraints, and safety and reliability requirements. We introduce AstroMemBench and a Scenario-Challenge-Capability design method that maps these requirements to executable memory tests. The benchmark covers 16 memory subchallenges through 140 templates and 2240 instances across nine tasks in planetary surface operations, on-orbit servicing, and deep-space exploration. A deterministic environment scores actions for task completion, state changes, safety, and resource use. Ablations under nine conditions show that the benchmark is sensitive to how accurately agents recover and use historical information and to differences in memory-system design. Main experiments compare six configurations. Mem0, Chain-of-Memory, LightMem, and retrieval-augmented generation (RAG) improve same-session mean scores over native Pi Agent, with no clear advantage of the three memory systems over RAG. After a session restart, Mem0 outperforms RAG by 12.25 points. Benefits favor instruction retention and result reuse over ongoing state tracking and energy reservation. AstroMemBench supports the design, development, and selection of memory systems for embodied spacecraft agents. AstroMemBench 1.0 and its evaluation code are publicly available: https://github.com/flyingView/AstroMemBench-v1.

</details>

---

### [[20_Research/Papers/大模型/A_Joint_LLM_and_Optimization_Agent_Solution_for_Drone_Scheduling_in_Victim_Search_Missions|A Joint LLM and Optimization Agent Solution for Drone Scheduling in Victim Search Missions]]

![[assets/2611.16524_figure.png|800]]

- **arXiv**: [2611.16524](https://arxiv.org/abs/2611.16524)
- **PDF**: https://arxiv.org/pdf/2611.16524
- **详细分析**: [[20_Research/Papers/大模型/A_Joint_LLM_and_Optimization_Agent_Solution_for_Drone_Scheduling_in_Victim_Search_Missions|A Joint LLM and Optimization Agent Solution for Drone Scheduling in Victim Search Missions]]
- **作者**: Yinghao Zhang, Yalin Liu, Hong-Ning Dai, Yan Zhang, Qubeijian Wang, Bishenghui Tao, Yaohan Li
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 2.0（加权：大模型 1，机器人 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《A Joint LLM and Optimization Agent Solution for Drone Scheduling in Victim Search Missions》归入 大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Victim search in wilderness areas is time-critical. Drones enable rapid area search, but scheduling them is challenging because victims may continue moving, detection results are uncertain, and effective decisions must combine structured mission information with unstructured contextual clues and domain knowledge. To address this, we propose an agent-aided drone scheduling system. The system employs an agent at the ground control station (GCS) to coordinate multiple drones over successive search cycles. In each cycle, the agent applies a scheduling policy that combines a large language model (LLM) for reasoning about where to search with an optimizer for determining how to dispatch the drones under energy constraints. Simulation results show that the proposed system consistently completes the victim-search mission, whereas none of the six non-LLM baselines does so and direct LLM scheduling is considerably less reliable. The source code is publicly available at https://github.com/1643204431/llm-uav-victim-search.

</details>

---

### [[20_Research/Papers/具身智能/HeMeR_Heterogeneous_Memory_Reconciliation_for_Embodied_Agents_via_Structured_KV_Reuse|HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse]]

![[assets/2611.16487_figure.png|800]]

- **arXiv**: [2611.16487](https://arxiv.org/abs/2611.16487)
- **PDF**: https://arxiv.org/pdf/2611.16487
- **详细分析**: [[20_Research/Papers/具身智能/HeMeR_Heterogeneous_Memory_Reconciliation_for_Embodied_Agents_via_Structured_KV_Reuse|HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse]]
- **作者**: Saehun Chun, Wonje Choi, Jinwoo Jang, Taeyoon Kwack, Honguk Woo
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.6，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《HeMeR: Heterogeneous Memory Reconciliation for Embodied Agents via Structured KV Reuse》归入 具身智能、大模型、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, EmbodiedBench, MemRL, RealWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents make decisions by combining information from heterogeneous memory modules, including declarative memory for explicit knowledge, procedural memory for learned routines, and working memory for current observations. During interaction, the memory contents required for decision making change with the agent's state, goal, and task progress, while many contents remain shared across consecutive decisions. However, existing memory modules are typically accessed through separate interfaces, so each updated memory context is often processed as a new input to the foundation model. This prevents selective key-value (KV) cache reuse for unchanged memory contents and forces full KV cache recomputation even when much of the memory context remains valid. We introduce HeMeR, an inference framework that performs KV reconciliation between dynamically updated memory contexts and reusable KV states. HeMeR tracks declarative, procedural, and working memory contents across action decisions, preserves KV states for unchanged contents, and reconciles only the KV states affected by memory-content updates. This enables efficient and stable inference as memory contents evolve during interaction. We evaluate HeMeR on ALFWorld, Habitat, and real-world robotic deployments requiring coordinated use of heterogeneous memory contents. In the real-world setting, HeMeR achieves 83.20% task success and reduces per-step inference time from 2.94 to 1.87 seconds compared with MemRL, while preserving compatible KV states as task progress updates the memory context.

</details>

---

### [[20_Research/Papers/强化学习/JustRUA_A_Controlled_Study_of_GPT-6_Robot-Use_Agents|JustRUA: A Controlled Study of GPT-6 Robot-Use Agents]]

![[assets/2611.16009_figure.png|800]]

- **arXiv**: [2611.16009](https://arxiv.org/abs/2611.16009)
- **PDF**: https://arxiv.org/pdf/2611.16009
- **详细分析**: [[20_Research/Papers/强化学习/JustRUA_A_Controlled_Study_of_GPT-6_Robot-Use_Agents|JustRUA: A Controlled Study of GPT-6 Robot-Use Agents]]
- **作者**: Zefan Wang, Yufan Dang, Xuanwei Shi, Mingqi Gao, Cheng Yin, SikYuen Tam, Hanyu Liu, Yasheng Wang, Yaxi Lu, Songyang Zhang, Xin Cong, Yuan Yao
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《JustRUA: A Controlled Study of GPT-6 Robot-Use Agents》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

GPT-6 Astra can drive a robot arm directly through a fixed harness, and scores of such robot-use agents on RoboDojo have risen quickly since. Reported systems differ in harness and test subset and often change several designs at once, so it is hard to tell which choices produce the gains. We take these designs apart and test them in one framework, along the harness around the model, the action interface, the reuse of experience and the scene geometry given to the model. A lean harness that keeps the full episode history and stops each motion early goes a long way. Reusing experience changes how the model acts but is not a free lunch, and scene geometry helps most, even when depth is predicted from RGB alone. JustRUA starts from the official L3 harness and keeps only what matters most. Even with no learned policy, self-improvement loop or task-specific tuning, this simple harness raises the score on the RoboDojo simulation benchmark substantially, from 29.7 to 50.3.

</details>

---

### [[20_Research/Papers/大模型/Reward-Driven_Collider_Physics_Challenges_for_Self-Improving_Agentic_AI_via_Reinforcement_Learning|Reward-Driven Collider Physics Challenges for Self-Improving Agentic AI via Reinforcement Learning]]

![[assets/2611.15885_figure.png|800]]

- **arXiv**: [2611.15885](https://arxiv.org/abs/2611.15885)
- **PDF**: https://arxiv.org/pdf/2611.15885
- **详细分析**: [[20_Research/Papers/大模型/Reward-Driven_Collider_Physics_Challenges_for_Self-Improving_Agentic_AI_via_Reinforcement_Learning|Reward-Driven Collider Physics Challenges for Self-Improving Agentic AI via Reinforcement Learning]]
- **作者**: Alexander Yue, Qibin Liu, Julia Gonski
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.32（加权：大模型 0.2，强化学习 0.96，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Reward-Driven Collider Physics Challenges for Self-Improving Agentic AI via Reinforcement Learning》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in agentic AI have demonstrated the potential to automate complex high-energy physics (HEP) workflows. We focus on the regime of HEP tasks where frontier models still struggle to provide correct and complete solutions, and introduce an open-ended optimization task format with continuous, automatically evaluated rewards. Unlike conventional benchmarks focused on task completion, these tasks target reinforcement learning (RL) environments to generate agentic improvement on state- of-the-art HEP challenges. We benchmark frontier reasoning models on several HEP tasks and demonstrate an initial proof of concept in which a small language model improves through RL using automated feedback without human intervention. By connecting challenging HEP problems with verifiable scientific rewards and RL, we aim to advance agentic AI from reproducing established workflows to autonomously discovering better scientific solutions, paving the way toward self-improving scientific agents.

</details>

---

### [[20_Research/Papers/机器人/RUMI_A_Robotiq-Matched_Universal_Manipulation_Interface_for_Robot_Learning_with_Augmented_Reality_and_Haptic_Feedback|RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback]]

![[assets/2611.15802_figure.png|800]]

- **arXiv**: [2611.15802](https://arxiv.org/abs/2611.15802)
- **PDF**: https://arxiv.org/pdf/2611.15802
- **详细分析**: [[20_Research/Papers/机器人/RUMI_A_Robotiq-Matched_Universal_Manipulation_Interface_for_Robot_Learning_with_Augmented_Reality_and_Haptic_Feedback|RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback]]
- **作者**: Kevin Avdiu, Seongjin Bien, Yannik Blei, Philine Meister, Johannes Hechtl, Philipp Schmitt, Kai Wurm, Georg von Wichert, Wolfram Burgard
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《RUMI: A Robotiq-Matched Universal Manipulation Interface for Robot Learning with Augmented Reality and Haptic Feedback》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many manipulation tasks require carefully controlled contact forces for successful execution, yet large-scale, force-aware datasets remain scarce. Handheld interfaces can help by transmitting interaction forces directly through the operator's arm, but most existing designs are tailored to simple linear grippers and do not match the nonlinear mechanics of widely used robotic grippers. We present RUMI, a handheld universal manipulation interface matched to the Robotiq 2F-85 with exchangeable fingertip sensors that preserves the target gripper geometry while enabling natural input before contact and force measurement after contact. By integrating the tracking system into a virtual reality headset, our method provides real-time augmented reality feedback about the kinematic feasibility of motion on the target robot platform. We further introduce a haptic feedback mechanism that supports force-aware teleoperation for simulated and real robots. A user study shows fewer episodes containing joint-limit violations with live robot visualization and pose initialization (3/50) than without augmented reality (16/50). We additionally train imitation policies from demonstrations, collected using two different fingertip modalities enabled by the gripper-matched hardware, and assess the haptic interface's capability for collecting force-aware teleoperation datasets in simulation.

</details>

---

### [[20_Research/Papers/具身智能/DISCERN_Preserve_at_Write,_Resolve_at_Read_for_Persistent_LLM-Agent_Memory|DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory]]

![[assets/2611.15729_figure.png|800]]

- **arXiv**: [2611.15729](https://arxiv.org/abs/2611.15729)
- **PDF**: https://arxiv.org/pdf/2611.15729
- **详细分析**: [[20_Research/Papers/具身智能/DISCERN_Preserve_at_Write,_Resolve_at_Read_for_Persistent_LLM-Agent_Memory|DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory]]
- **作者**: Chirag Ahuja, Vladislav Tanov, Ramcharan Kakarla, Jonathan Taws
- **cs 子类**: cs.AI
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《DISCERN: Preserve at Write, Resolve at Read for Persistent LLM-Agent Memory》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LongMemEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enterprise agents accumulate memory across dozens of sessions in which facts contradict, get superseded, and blur as similarly named entities collide in embedding space. The field treats this as a retrieval problem; we show it is not. On ENT-310, a synthetic enterprise sales-agent memory benchmark of 310 queries (210 answerable, 100 unanswerable), a vanilla Retrieval-Augmented Generation (RAG) reader over a memory store already matches strong memory systems on the recall pillars. Retention and currency are near-saturated, roughly 0.93 to 0.98 for every competent system, so recall is essentially solved. What remains unsolved is resolution: which entity a query refers to, which time-state is current, and whether to commit an answer at all or decline when evidence is insufficient. We propose DISCERN (DISambiguation and Cross-session Episodic memoRy Navigation), an agent-memory framework built on a single rule: preserve at write, resolve at read. At write time DISCERN builds a strictly additive bi-temporal provenance graph that never merges confusable entities and never drops superseded values. At read time a zero-LLM tool surface drives an agentic loop that navigates this graph and commits exactly one of four gated terminal actions. A four-judge LLM-as-a-Judge council scores two axes: answer correctness on answerable questions, and the answer-versus-abstain decision as a classification problem. On ENT-310, DISCERN is the best-calibrated system on abstention (F1 0.924 versus at most 0.802 across eight baselines) and leads macro answer correctness under equal pillar weighting (0.861 versus 0.806 for the strongest baseline), a lead driven by entity resolution (0.800, where no baseline exceeds 0.40). Applied with zero tuning to the full LoCoMo corpus, the same pipeline again leads macro answer correctness (0.663 versus 0.638) and stays among the best-calibrated on false-premise abstention.

</details>

---

### [[20_Research/Papers/具身智能/EMS-Nav_Embodied_Multi-Scale_Navigation|EMS-Nav: Embodied Multi-Scale Navigation]]

![[assets/2611.15589_figure.png|800]]

- **arXiv**: [2611.15589](https://arxiv.org/abs/2611.15589)
- **PDF**: https://arxiv.org/pdf/2611.15589
- **详细分析**: [[20_Research/Papers/具身智能/EMS-Nav_Embodied_Multi-Scale_Navigation|EMS-Nav: Embodied Multi-Scale Navigation]]
- **作者**: Zenghui Yang, Xinan Wang, Danyang Li, Zhe Xu, Zheng Yang, Jingao Xu, Qiang Ma
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《EMS-Nav: Embodied Multi-Scale Navigation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial inspection robots must reach work areas and specific equipment. These destinations span spatial scales from regions to objects, so robots must relate each target to its surroundings to interpret the task and determine where to go. Existing methods support multi-scale navigation through rich environment representations, but at substantial computational and storage cost. These costs limit deployment where wireless coverage is incomplete and robots must rely on onboard computation to keep navigating. We introduce EMS-Nav, a biologically inspired multi-scale navigation framework for online, on-device operation. Its core innovation is to organize perception, spatial understanding, and navigation around regions, making local spaces the basic units of both environmental understanding and computation. EMS-Nav groups objects and their relationships into functionally meaningful spaces and builds a hierarchy from local areas to the broader environment. This organization supports efficient map construction alongside the interpretation and execution of language goals at different scales. In multi-scale navigation experiments, EMS-Nav achieves the highest success rates across all four target categories: objects, rooms, regions, and specific instances. It outperforms state-of-the-art open-vocabulary mapping and navigation methods, improving overall first-attempt success by 9.39 percentage points over the strongest baseline while reducing mapping overhead and language-model input size. Local deployment in real indoor environments further demonstrates its applicability to on-device embodied navigation. By establishing regions as the organizing basis for perception, spatial understanding, and language-guided action, EMS-Nav provides a system that combines multi-scale understanding with computational efficiency to support diverse language goals on resource-constrained robots.

</details>

---

### [[20_Research/Papers/强化学习/ReShap_Interpretable_Reinforcement_Learning_for_High-Dimensional_Multi-Action_Settings|ReShap: Interpretable Reinforcement Learning for High-Dimensional Multi-Action Settings]]

![[assets/2611.15507_figure.png|800]]

- **arXiv**: [2611.15507](https://arxiv.org/abs/2611.15507)
- **PDF**: https://arxiv.org/pdf/2611.15507
- **详细分析**: [[20_Research/Papers/强化学习/ReShap_Interpretable_Reinforcement_Learning_for_High-Dimensional_Multi-Action_Settings|ReShap: Interpretable Reinforcement Learning for High-Dimensional Multi-Action Settings]]
- **作者**: Yiyu Qian, Pengfei Guo, Liyuan Zhao
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《ReShap: Interpretable Reinforcement Learning for High-Dimensional Multi-Action Settings》归入 强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PIRL, SVERL, XRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep Reinforcement Learning (RL) plays a crucial role in tackling complex tasks, yet its reliance on deep neural networks makes the learned policies opaque. To enhance the trustworthiness of RL policies, existing work (e.g., the SILVER framework [Li et al., 2025]) has focused on Shapley-based interpretability, but is typically restricted to low-dimensional state spaces, binary-action settings, and a single class of linear surrogate. We propose ReShap, a policy-distillation framework that extends Shapley-based interpretability to high-dimensional, multi-action environments. ReShap extracts compact feature representations from raw image observations, performs SHAP-based feature attribution to characterize how each feature contributes to the policy's decisions, and distills the deep RL policy into an interpretable surrogate trained on the full set of (state, policy-action) pairs along the policy's visited distribution. We instantiate the surrogate with three interpretable model families (decision trees, linear regression, and logistic regression) and compare their fidelity and task return. We evaluate ReShap on Atari and Box2D environments using three deep RL algorithms and conduct a human-subject study to assess the clarity and trustworthiness of the resulting policies. Results show that ReShap preserves competitive task performance, that decision trees generally outperform linear and logistic regression, and that linear regression is weakest in most settings.

</details>

---

### [[20_Research/Papers/大模型/Is_the_Importance_Ratio_Necessary_for_Stable_Reinforcement_Learning_in_LLMs|Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?]]

![[assets/2611.15404_figure.png|800]]

- **arXiv**: [2611.15404](https://arxiv.org/abs/2611.15404)
- **PDF**: https://arxiv.org/pdf/2611.15404
- **详细分析**: [[20_Research/Papers/大模型/Is_the_Importance_Ratio_Necessary_for_Stable_Reinforcement_Learning_in_LLMs|Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?]]
- **作者**: Shuibai Zhang, Junhyuck Kim, Gyeongman Kim, Jaewoong Cho
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 1.57（加权：大模型 0.25，强化学习 1.16，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Is the Importance Ratio Necessary for Stable Reinforcement Learning in LLMs?》归入 强化学习、大模型、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) has become central to post-training large language models (LLMs). However, popular RL methods like GRPO incur non-negligible overhead by computing both old-policy and current-policy likelihoods to form importance sampling ratios. In this work, we propose Likelihood-Gated Policy Optimization (LGPO), which enforces a soft trust region constraint via likelihood-based gating, eliminating the need to compute old-policy likelihoods. Empirically, we show that removing the importance sampling correction term does not harm training stability, whereas removing the trust region mechanism can lead to collapse. Moreover, ratio-based clipping can fail in fully on-policy training: the importance ratio stays at 1, so the ratio-based trust region constraint never activates. Under standard training settings where GRPO is stable, LGPO achieves comparable training stability and peak performance while reducing training time by ~18% on average relative to a standard implementation that recomputes old-policy likelihoods. In fully on-policy training, where GRPO fails, LGPO remains stable, enabling more efficient and robust LLM RL post-training across training regimes.

</details>

---

### [[20_Research/Papers/强化学习/A_physics-constrained_deep_reinforcement_learning_method_for_autonomous_mission_planning_of_Titan_deep_space_probes|A physics-constrained deep reinforcement learning method for autonomous mission planning of Titan deep space probes]]

![[assets/2611.15389_figure.png|800]]

- **arXiv**: [2611.15389](https://arxiv.org/abs/2611.15389)
- **PDF**: https://arxiv.org/pdf/2611.15389
- **详细分析**: [[20_Research/Papers/强化学习/A_physics-constrained_deep_reinforcement_learning_method_for_autonomous_mission_planning_of_Titan_deep_space_probes|A physics-constrained deep reinforcement learning method for autonomous mission planning of Titan deep space probes]]
- **作者**: Hanmin Li, Tao Wang, Shuangliang Liu, Zhe Zhang, Maodeng Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.4（加权：强化学习 1.4）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《A physics-constrained deep reinforcement learning method for autonomous mission planning of Titan deep space probes》归入 强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Titan is a compelling target for future deep space exploration, while its extreme Earth-Titan distance and complex environment make continuous ground-in-the-loop planning impractical. Existing planning methods, primarily developed for Earth-observation scenarios, have limited generalizability to uncertain deep space conditions and adaptability to time-varying mission states. To address these challenges, this paper proposes a physics-constrained maskable proximal policy optimization (PCM-PPO) method for Titan autonomous mission planning. A Titan-specific discrete-time Markov decision process is established to characterize mission feasibility and resource constraints. A system dynamics and geometric model is incorporated to enhance physical representation, including central gravity, J2 perturbation, third-body attraction, and downlink occultation. To accommodate opportunity targets under a bounded action dimension, PCM-PPO organizes predefined and opportunity targets through a fixed-capacity target pool and represents the mission state with a target-wise state matrix and a global state vector. A physics-constrained action mask constructs an admissible decision domain from current mission states, guiding policy learning toward physically executable decisions and avoiding infeasible exploration. An integrated training strategy facilitates policy optimization under coupled constraints. Comparative, ablation, and uncertainty experiments validate the effectiveness of PCM-PPO. PCM-PPO provides a feasible and interpretable scheme for autonomous mission planning of Titan deep space probes.

</details>

---

### [[20_Research/Papers/大模型/Knowledge_in_the_Harness,_Reliability_in_the_Weights_Teacher-Free_Co-Evolution_of_an_LLM_Agent|Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent]]

![[assets/2611.15268_first_page.png|800]]

- **arXiv**: [2611.15268](https://arxiv.org/abs/2611.15268)
- **PDF**: https://arxiv.org/pdf/2611.15268
- **详细分析**: [[20_Research/Papers/大模型/Knowledge_in_the_Harness,_Reliability_in_the_Weights_Teacher-Free_Co-Evolution_of_an_LLM_Agent|Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent]]
- **作者**: Yujia Zhang, Xinqi Ren, Shixiong Zhou, Jia Meng
- **cs 子类**: cs.AI, cs.CL, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.37（加权：大模型 0.85，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Knowledge in the Harness, Reliability in the Weights: Teacher-Free Co-Evolution of an LLM Agent》归入 大模型、强化学习、世界模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MUA-RL, SkillRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small open models suit private customer-service deployments but trail frontier models in two ways: they miss what the written policy requires in a given situation, and they act inconsistently on what they know. We study whether such a model can close both gaps from its own deployment logs and their reference outcomes, without a stronger teacher model. Our starting point is a Gemma 4 12B agent that reads its domain policy from on-demand skills rather than from its system prompt. In each round, the deployed system serves a fresh batch of tasks; the base model diagnoses failed conversations and writes rules into the skills, and a rule survives only if it passes code checks, counterexample self-review, a paired retest, and a noise-calibrated validation gate. Reinforcement learning (GRPO) then trains a LoRA adapter on complete multi-turn, tool-using conversations. On the retail and airline domains of $τ^2$-bench, without training or selecting on official tasks, the agent after two rounds improves on this starting point by 12.5 pass$^1$ points in retail and 19.5 in airline, and by 18.4 and 22.0 pass$^4$ points. It also exceeds the benchmark's reference agent, which runs the same model with the whole policy in its system prompt, by 11.8 and 8.0 pass$^1$ points and by 22.8 and 16.0 pass$^4$ points, closing most of the gap to three frontier models under the same protocol. A $2\times2$ ablation shows that the rules rescue tasks the agent never solved and carry policy knowledge that RL with the rules in context does not internalize, whereas the trained weights make solved tasks reliable.

</details>

---

### [[20_Research/Papers/具身智能/AFTER_A_World_Model_with_Adaptive_Fast--Slow_Timescales_for_Error-Driven_Retention|AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention]]

![[assets/2611.15215_figure.png|800]]

- **arXiv**: [2611.15215](https://arxiv.org/abs/2611.15215)
- **PDF**: https://arxiv.org/pdf/2611.15215
- **详细分析**: [[20_Research/Papers/具身智能/AFTER_A_World_Model_with_Adaptive_Fast--Slow_Timescales_for_Error-Driven_Retention|AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention]]
- **作者**: Haoyi Zhang, Qi Zhang, Yunfan Ren, Yi Bin, Lei Zhu, Heng Tao Shen
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 3.0（加权：具身智能 0.9，世界模型 1，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《AFTER: A World Model with Adaptive Fast--Slow Timescales for Error-Driven Retention》归入 机器人、世界模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotics and embodied AI, a core challenge for world models is adapting to sudden, persistent, yet initially unknown changes in robot dynamics during interaction. For instance, when a robotic arm grasps an object with an unknown payload, the robot dynamics change suddenly. If the world model fails to adapt, its prediction errors accumulate over the open-loop rollout and ultimately mislead the robot's actions. Existing world models, however, struggle to simultaneously satisfy three critical requirements for dynamics adaptation: responsiveness, reacting promptly to sudden changes to curb prediction error accumulation; stability, distinguishing persistent changes from transient disturbances to prevent incorrect updates; and persistence, retaining the adapted dynamics without new observations so that later predictions do not revert to the old dynamics. Inspired by predictive coding in the human brain with multi-timescale adaptation, we propose AFTER-WM, a world model with Adaptive Fast-slow Timescales for Error-driven Retention, whose prediction errors drive a fast correction that fades and a slow correction that persists, while dynamically adjusting the combination weights of pre-trained experts without altering them, to overcome the trade-offs among responsiveness, stability and persistence. On five simulated robot datasets and real UAV data, AFTER-WM has a lower multi-step mean error than all ten compared models and the highest mean return in a joint-failure control task. In simulation, its multistep mean error is 16%-34% below the strongest compared model's and is also the lowest 1-4 steps after a change and under transient disturbances alone, and its step-40 error is the lowest as well, reflecting responsiveness, stability and persistence. All code (method, baselines, experiments) and datasets will be released online.

</details>

---

### [[20_Research/Papers/具身智能/CFGComposer_Compositional_Audio-Text-to-Motion_Generation_via_Copula_Score_Correction|CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction]]

![[assets/2611.15101_figure.png|800]]

- **arXiv**: [2611.15101](https://arxiv.org/abs/2611.15101)
- **PDF**: https://arxiv.org/pdf/2611.15101
- **详细分析**: [[20_Research/Papers/具身智能/CFGComposer_Compositional_Audio-Text-to-Motion_Generation_via_Copula_Score_Correction|CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction]]
- **作者**: Pengyang Shi, Jinlu Zhang, Chunze Lin, Yizhou Wang, Li Yi
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 1.2，机器人 0.4）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《CFGComposer: Compositional Audio-Text-to-Motion Generation via Copula Score Correction》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating whole-body gestures that are simultaneously rhythmically synchronized with speech audio and semantically aligned with text descriptions is a fundamental challenge in embodied AI and social robotics. We tackle this Audio-Text-to-Motion (AT2M) problem by composing two independently-trained diffusion models at inference time and refine bias in joint inference by modeling the copula score $s_I$. A rigorous theoretical analysis reveals that naive epsilon blending corresponds to a Product-of-Experts formulation that omits the copula score $s_I$: the cross-modal interaction between audio and text that neither marginal model can capture. We propose CFGComposer: a jointly-trained AT2M diffusion model that estimates $s_I$ via a CFG analogy and injects it as an $ε$-space correction. Experiments on BEAT demonstrate best-in-class semantic fidelity (SRGR $0.9916$, FID $27.18$) with GT-level beat alignment (BA $0.1826$ vs. GT $0.1743$), and 76-83% win rate in blind pairwise human evaluation against all prior methods. Physical deployment on a Unitree G1 humanoid confirms direct sim-to-real transfer.

</details>

---

### [[20_Research/Papers/大模型/LLM-Enhanced_Deep_Reinforcement_Learning_with_Human-in-the-Loop_Calibration_for_Real-Time_Optimal_Power_Flow|LLM-Enhanced Deep Reinforcement Learning with Human-in-the-Loop Calibration for Real-Time Optimal Power Flow]]

![[assets/2611.15003_figure.png|800]]

- **arXiv**: [2611.15003](https://arxiv.org/abs/2611.15003)
- **PDF**: https://arxiv.org/pdf/2611.15003
- **详细分析**: [[20_Research/Papers/大模型/LLM-Enhanced_Deep_Reinforcement_Learning_with_Human-in-the-Loop_Calibration_for_Real-Time_Optimal_Power_Flow|LLM-Enhanced Deep Reinforcement Learning with Human-in-the-Loop Calibration for Real-Time Optimal Power Flow]]
- **作者**: Jiayang Tu, Bozhen Jiang, Bojun Du, Yunxiao Ling, Ershun Du, Qin Wang
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 2.0（加权：大模型 0.4，强化学习 1.6）
- **关联关键词**: LLM, RL, Systems

#### 研究背景与动机

《LLM-Enhanced Deep Reinforcement Learning with Human-in-the-Loop Calibration for Real-Time Optimal Power Flow》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time optimal power flow (RT-OPF) requires fast and reliable decision-making under time-varying operating conditions. However, many practical operating preferences and safety related requirements are difficult to encode using conventional numerical rewards alone, which limits the effectiveness and controllability of deep reinforcement learning (DRL) for RT-OPF. To address this issue, this paper proposes an LLM-enhanced DRL framework with human-in-the-loop (HITL) for RT-OPF. The proposed method augments the physics-based reward with sparse language evaluative feedback during offline training, so that semantic operational requirements can be incorporated into policy learning. To improve reliability in RT-OPF, a selective HITL calibration mechanism is further introduced to inspect and correct questionable LLM judgments before they continuously shape the learning process. Case studies on the IEEE 30-bus and IEEE 118-bus systems show that LLM feedback improves policy safety over vanilla TD3, while further HITL calibration achieves the best overall performance and more stable training behavior. These results demonstrate the effectiveness of combining language guidance and expert calibration for RT-OPF.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Low-Latency_Action_Verification_for_Frozen_Vision-Language-Action_Models|Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models]]

![[assets/2611.14834_figure.png|800]]

- **arXiv**: [2611.14834](https://arxiv.org/abs/2611.14834)
- **PDF**: https://arxiv.org/pdf/2611.14834
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Low-Latency_Action_Verification_for_Frozen_Vision-Language-Action_Models|Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models]]
- **作者**: Wen-Han Hsieh, Ken Jiankun Zheng, Chia-Chien Chen, David M. Chan, Trevor Darrell
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Learning Low-Latency Action Verification for Frozen Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoVer-VLA, DSRL, Real-World, SafeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have made significant progress in general-purpose robotic manipulation. However, sampled action sequences can be ineffective, while evaluating alternatives with computationally expensive verifiers adds latency at each policy query. In this work, we propose HDH, a lightweight framework that uses hindsight from a frozen VLA's own deployments to improve action verification. The framework has three stages. First, we deploy the policy and collect its autonomous rollouts. We then train a compact action verifier to assign each action chunk a predicted task-success score. Finally, the frozen VLA generates action candidates, and the verifier selects the candidate with the highest score for execution. Across four LIBERO-10 tasks, HDH achieves an average success rate of 82.3\% and on three real-world manipulation tasks, HDH improves average success over the baseline policy by 22.6\%.

</details>

---
