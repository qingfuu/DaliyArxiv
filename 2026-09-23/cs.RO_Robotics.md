# cs.RO | Robotics | 2026-09-23

#arxiv #ComputerScience

**论文数**: 52

### [[20_Research/Papers/具身智能/Imperfection_for_Precision_Upcycling_Imperfect_Data_for_High-Precision_Robotic_Manipulation|Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation]]

![[assets/2609.26672_figure.png|800]]

- **arXiv**: [2609.26672](https://arxiv.org/abs/2609.26672)
- **PDF**: https://arxiv.org/pdf/2609.26672
- **详细分析**: [[20_Research/Papers/具身智能/Imperfection_for_Precision_Upcycling_Imperfect_Data_for_High-Precision_Robotic_Manipulation|Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation]]
- **作者**: Hao Wei, Yang Liu, Chao Tang, Shengbao Li, Jiangtao Chen, Jinxuan Zhu, Jiaheng Wang, Hong Yin, Zhaofeng Cao, Tingguang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Imperfection for Precision: Upcycling Imperfect Data for High-Precision Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TMRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training vision-language-action (VLA) models for high-precision manipulation typically requires task-specific, high-quality data (e.g., teleoperation), which is slow and expensive to collect. To reduce this burden without compromising manipulation precision, we propose $\varepsilon$4P (Imperfection for Precision), a simple yet effective method that "upcycles" two otherwise discarded data sources: (1) low-precision data from the target task and (2) high-precision data from mismatched tasks. Rather than naively mixing these imperfect data sources throughout co-training, $\varepsilon$4P controls where each source contributes along the flow-matching trajectory. Specifically, low-precision, target-task data is used at high noise to preserve high-level task context and high-precision, task-mismatched data is used at low noise to transfer low-level action precision. Through real-robot experiments on both sub-millimeter, high-precision tasks and coarse-grained tasks, we demonstrate that the proposed method (1) effectively leverages additional imperfect data to improve policy performance by up to 31.7 percentage points, and (2) can replace an equal amount of task-specific, high-quality data with an average performance drop of only 4.2 percentage points. Overall, $\varepsilon$4P points toward a scalable paradigm for high-precision manipulation, in which heterogeneous, imperfect data can be systematically repurposed to reduce reliance on costly task-specific, high-quality data. More details are available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Learning_Air-Ground_Motion_Control_with_Temporal_Mode_Switching_and_Cross-Terrain_Tracking|Learning Air-Ground Motion Control with Temporal Mode Switching and Cross-Terrain Tracking]]

![[assets/2609.26564_figure.png|800]]

- **arXiv**: [2609.26564](https://arxiv.org/abs/2609.26564)
- **PDF**: https://arxiv.org/pdf/2609.26564
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Air-Ground_Motion_Control_with_Temporal_Mode_Switching_and_Cross-Terrain_Tracking|Learning Air-Ground Motion Control with Temporal Mode Switching and Cross-Terrain Tracking]]
- **作者**: Ruitian Pang, Mingrui Li, Xuanting Liu, Tiancheng Lai, Juncheng Chen, Xiangyu Li, Ruibin Zhang, Qishao Wang, Jin Yu, Haiyin Piao, Fei Gao, Chao Xu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Learning Air-Ground Motion Control with Temporal Mode Switching and Cross-Terrain Tracking》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Passive-wheeled terrestrial-aerial bimodal vehicles (TABVs) combine aerial mobility with energy-efficient ground locomotion. However, reliable air-ground mode switching under limited onboard perception and robust ground trajectory tracking across diverse terrains remain challenging when targeting real-world applications. In this work, we propose a learning-based air-ground motion control framework for passive-wheeled TABVs: 1) a learned mode selector for autonomous air-ground motion mode switching. The selector uses historical single-point time-of-flight (ToF) measurements and robot states together with future reference information to determine the active locomotion mode. 2) a reinforcement learning control policy for trajectory tracking. The policy combines proprioceptive observations with future reference information to anticipate trajectory changes. For ground locomotion, multi-terrain training and dynamics randomization enable robust tracking across different terrains. Simulation and real-world experiments demonstrate reliable air-ground switching under limited perception and accurate ground tracking across diverse terrain conditions. The learned selector outperforms a rule-based mode selector in challenging transitions, while the ground controller achieves lower position RMSE than PID across all tested conditions and maintains decent tracking where NMPC fails. With these capabilities integrated, the system tracks a 101m air-ground trajectory through multiple autonomous mode transitions with a position RMSE of 0.08m.

</details>

---

### [[20_Research/Papers/具身智能/MATE_Multi-Agent_Virtual_Teleoperation_Platform_for_Humanoid_Collaboration_Data_Collection|MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection]]

![[assets/2609.26520_figure.png|800]]

- **arXiv**: [2609.26520](https://arxiv.org/abs/2609.26520)
- **PDF**: https://arxiv.org/pdf/2609.26520
- **详细分析**: [[20_Research/Papers/具身智能/MATE_Multi-Agent_Virtual_Teleoperation_Platform_for_Humanoid_Collaboration_Data_Collection|MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection]]
- **作者**: Yichuan Yu, Youzhuo Wang, Yiming Ren, Di Feng, Yexuan Yang, Bingxi Yang, Shengxiao Gong, Yujing Sun, Yuexin Ma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.9（加权：具身智能 2.1，大模型 0.5，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MATE: Multi-Agent Virtual Teleoperation Platform for Humanoid Collaboration Data Collection》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots require diverse embodied experiences to acquire complex loco-manipulation and collaborative skills. However, existing humanoid data pipelines primarily focus on individual agents, while physical multi-robot collaboration remains difficult to scale due to costly hardware, dedicated spaces, and repeated resets. In this work, we introduce MATE, a Multi-Agent virtual TEleoperation platform for humanoid collaboration data collection that enables multiple geographically distributed operators to simultaneously control whole-body humanoids in a shared physics-based environment. MATE removes the need for multiple physical robots and co-located operation while preserving physically coupled interactions among humanoids, objects, and environments. Using MATE, we construct a multi-humanoid collaboration dataset comprising 24.1 hours of coordinated behavior across 2,500 joint episodes and five long-horizon tasks, including object handover, relay delivery, environment interaction, and cooperative transport. To improve learning from these interaction-rich demonstrations, we introduce EAIS, an Execution-Aligned Interaction Sampling strategy that computes sampling signals within an execution-aligned prefix and prioritizes task-progressing and interaction-critical behaviors. We evaluate MATE with representative imitation learning and vision-language-action policies across diverse collaboration tasks. Experiments demonstrate efficient data collection, effective policy learning, and zero-shot transfer from virtual demonstrations to a physical humanoid without real-world fine-tuning. Project page: this https URL

</details>

---

### [[20_Research/Papers/大模型/Generalizing_Manipulation_Skills_with_a_Local_Coding_Agent|Generalizing Manipulation Skills with a Local Coding Agent]]

![[assets/2609.26499_figure.jpg|800]]

- **arXiv**: [2609.26499](https://arxiv.org/abs/2609.26499)
- **PDF**: https://arxiv.org/pdf/2609.26499
- **详细分析**: [[20_Research/Papers/大模型/Generalizing_Manipulation_Skills_with_a_Local_Coding_Agent|Generalizing Manipulation Skills with a Local Coding Agent]]
- **作者**: Raman Talwar, Elias Nijs, Andreas Verleysen, Francis wyffels
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.7，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Generalizing Manipulation Skills with a Local Coding Agent》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SkillsBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Today, progress in open-weight language models enables systems capable of writing, executing and debugging code while still running on a single workstation. Most language-driven robots give the model a fixed action interface or a trained policy. Generalizing to a new task therefore means more engineering effort or more data collection, both time-consuming. We investigate whether a local open-weight vision-language model can control a robot and one-shot generalize to new variations of a task without new human programming or training. We let a local open-weight VLM, Qwen3.8-27B, drive a UR3e robotic arm from a coding-agent harness. It writes and runs its own code above a service that implements kinematics, safety limits and classic computer vision techniques. We investigate if this system is capable of generalizing to unseen tasks. Specifically, we test it on nine tasks built from children's toys designed to probe generalization capability across various object characteristics: color, size, shape, and task variation of those. With five trials for each task, we observe generalization in 30 out of 45 trials with durations ranging from 3.4 to 67.5 minutes depending on task complexity. We further test if there is a speedup when an agent is asked to redo the task after successful completion. This resulted in a 50% reduction in duration, indicating that there is self-improvement over time. Finally, we expose the limitations of a local coding agent. We believe that solving those limitations combined with further investigation of self-improvement over time points at a direct path toward real-world deployment of a local coding agent.

</details>

---

### [[20_Research/Papers/具身智能/RouteRLT_Learning_When_and_Which_RL_Specialist_Should_Control_a_Vision-Language-Action_Policy|RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy]]

![[assets/2609.26467_figure.png|800]]

- **arXiv**: [2609.26467](https://arxiv.org/abs/2609.26467)
- **PDF**: https://arxiv.org/pdf/2609.26467
- **详细分析**: [[20_Research/Papers/具身智能/RouteRLT_Learning_When_and_Which_RL_Specialist_Should_Control_a_Vision-Language-Action_Policy|RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy]]
- **作者**: Chongyu Zhu, Jaden Hinds, Hyegang Kim, Juan Sebastian Rojas, Ramy Elmallah, Chi-Guhn Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RouteRLT: Learning When and Which RL Specialist Should Control a Vision-Language-Action Policy》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AtomicVLA, HIL-SERL, IARL, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models provide broad manipulation competence, but often struggle during the precision-critical stages that dominate contact-rich industrial tasks such as connector insertion and cable management. A common remedy is to refine a pretrained VLA with reinforcement learning (RL), enabling task-specific improvement beyond behavior cloning. However, how to preserve its generalist behavior while deciding when RL refinement is needed and which specialized policy should act remains an open question. In this work, we present RouteRLT, a routing framework that learns when and which RL specialist, an RL policy trained for a single precision-critical phase, should take control from a generalist VLA. A phase selector identifies the active controller, a stabilizer suppresses transient switches, and an action-boundary manager handles transitions between chunked policy outputs. We evaluate RouteRLT on multi-object pick-and-place tasks in LIBERO, as well as on a real-world cable pickup and port-insertion task with multiple precision-critical stages. In simulation, the learned routing improves over the base VLA and matches routing with privileged phase boundaries, without accessing those boundaries at deployment. The real-robot evaluation validates automatic routing to both the pickup and insertion specialists under an operator-aligned handoff protocol. Altogether, these results show that learned routing applies RL specialist control where precise adaptation is most valuable while preserving generalist VLA behavior, including recovery from failed execution attempts.

</details>

---

### [[20_Research/Papers/具身智能/SparseNav_Instruction-conditioned_Sparse_Semantic_Perception_for_Training-Free_Vision-Language_Navigation|SparseNav: Instruction-conditioned Sparse Semantic Perception for Training-Free Vision-Language Navigation]]

![[assets/2609.26408_figure.png|800]]

- **arXiv**: [2609.26408](https://arxiv.org/abs/2609.26408)
- **PDF**: https://arxiv.org/pdf/2609.26408
- **详细分析**: [[20_Research/Papers/具身智能/SparseNav_Instruction-conditioned_Sparse_Semantic_Perception_for_Training-Free_Vision-Language_Navigation|SparseNav: Instruction-conditioned Sparse Semantic Perception for Training-Free Vision-Language Navigation]]
- **作者**: Quanhua Chen, Juhan Kang, Runfeng Lin, ZiFei Zhang, Enquang Feng, Chunran Zheng, Xiwang Dong, Jiarong Lin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《SparseNav: Instruction-conditioned Sparse Semantic Perception for Training-Free Vision-Language Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Map-based vision-language navigation (VLN) relies on persistent spatial representations to connect language understanding with geometric planning. However, acquiring semantics beyond the needs of the current instruction can introduce unnecessary perception cost and irrelevant annotations. Continuously accumulating unrelated objects may not only waste computation, but also clutter the visual-spatial representation consumed by the vision-language model (VLM) planner. To address this problem, we present SparseNav, a training-free framework that follows a less-is-more principle for semantic navigation. SparseNav persistently maintains a lightweight geometric bird's-eye-view (BEV) map and sparse landmark memory, acquiring new semantics on demand using the active sub-instruction to decide what is worth grounding. An instruction manager first tracks navigation progress and identifies the active landmark query. An instruction-conditioned perception mechanism then invokes open-vocabulary segmentation when the queried landmark is visible and its metric location can inform the next decision. The resulting landmark memory supports VLM selection among hybrid frontier and local directional waypoint candidates. Without any additional training, SparseNav achieves success rates of 42.8% on R2R-CE and 40.7% on RxR-CE, both on the Val-Unseen splits. Controlled ablations examine semantic perception strategies and the contributions of individual framework components. Furthermore, we successfully deployed SparseNav on a Unitree Go2 quadruped equipped with an Intel RealSense D455 RGB-D camera for geometric mapping and landmark grounding and a Livox MID-360 LiDAR for localization, without a prebuilt map. We validated its effectiveness across multiple indoor environments using instruction-conditioned waypoint navigation.

</details>

---

### [[20_Research/Papers/具身智能/Hierarchical_Floorplan-Guided_Vision-Language_Exploration_for_Embodied_Question_Answering|Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering]]

![[assets/2609.26360_figure.png|800]]

- **arXiv**: [2609.26360](https://arxiv.org/abs/2609.26360)
- **PDF**: https://arxiv.org/pdf/2609.26360
- **详细分析**: [[20_Research/Papers/具身智能/Hierarchical_Floorplan-Guided_Vision-Language_Exploration_for_Embodied_Question_Answering|Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering]]
- **作者**: Albert Gassol Puigjaner, Kostas Alexis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.8，大模型 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Hierarchical Floorplan-Guided Vision-Language Exploration for Embodied Question Answering》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EQA, ExploreEQA, GraphEQA, HFLEX-EQA, OpenEQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Question Answering (EQA) requires an agent to explore a previously unseen environment, gather relevant information, and answer questions about the scene. Recent approaches leverage Vision-Language Models (VLMs) together with semantic maps or scene graphs to guide exploration. However, exploration is typically driven only by local observations, while structural priors about the environment remain largely unused. We propose HFLEX-EQA, a hierarchical EQA framework that combines online scene graph construction, VLM- based planning, semantic frontier exploration, and floorplan priors. The system incrementally builds a hierarchical scene graph and an open-vocabulary occupancy map from RGB-D observations, enabling a VLM to jointly reason over the scene graph, task-relevant visual observations, exploration history, and an estimated topological floorplan. Furthermore, we introduce a room-discovery strategy that leverages the floorplan and open-vocabulary frontier semantics to guide exploration toward semantically relevant yet currently unobserved room types. We evaluate HFLEX-EQA on the OpenEQA and ExploreEQA benchmarks and demonstrate deployment on a quadruped robot in real indoor environments. Our results demonstrate the benefit of combining VLM-based hierarchical planning with structural floorplan priors for the EQA task.

</details>

---

### [[20_Research/Papers/机器人/ArborSplat_Online_Semantic_Gaussian_Splatting_SLAM_for_Orchards|ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards]]

![[assets/2609.26315_figure.png|800]]

- **arXiv**: [2609.26315](https://arxiv.org/abs/2609.26315)
- **PDF**: https://arxiv.org/pdf/2609.26315
- **详细分析**: [[20_Research/Papers/机器人/ArborSplat_Online_Semantic_Gaussian_Splatting_SLAM_for_Orchards|ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards]]
- **作者**: Alessandro Masini, Matteo Frosi, Mirko Usuelli, Matteo Matteucci
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《ArborSplat: Online Semantic Gaussian Splatting SLAM for Orchards》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Orchard robots need maps that preserve small but semantically important structures such as trunks, trellises, and fruit. 3D Gaussian Splatting (3DGS) SLAM achieves high photometric fidelity. However, its optimization remains appearance-driven, and transferring image semantics to 3D points is unreliable for thin structures, whose pixels may receive depth from background surfaces. We present ArborSplat, an online semantic 3DGS SLAM system that tracks with LiDAR odometry and optimizes semantics directly on the Gaussian map, constrained by class-specific height bands above a ground plane fitted to each keyframe's stereo point cloud, and fuses multi-view evidence into a semantic point cloud online while rejecting labels inconsistent with the local ground surface or with monocular depth. Class-constrained refinement reserves Gaussian capacity for underrepresented structures and, under reduced budgets, increases training-view accuracy on tree classes. We evaluate the approach on apple and pear orchards during dormancy, flowering, and harvesting. On full routes, it keeps ATE below 0.5 m on all 12 traversals. On shared 301-frame segments, it exceeds SGS-SLAM and GS3LAM by 0.23 to 0.50 training-view and 0.15 to 0.36 held-out mIoU while running 1.7 to 7.5 times faster, whereas SemGauss-SLAM runs out of GPU memory on all six.

</details>

---

### [[20_Research/Papers/具身智能/SafeLoop_Risk-Aware_Rollback_for_Vision-Language-Action_Manipulation|SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation]]

![[assets/2609.26313_figure.png|800]]

- **arXiv**: [2609.26313](https://arxiv.org/abs/2609.26313)
- **PDF**: https://arxiv.org/pdf/2609.26313
- **详细分析**: [[20_Research/Papers/具身智能/SafeLoop_Risk-Aware_Rollback_for_Vision-Language-Action_Manipulation|SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation]]
- **作者**: Zeyu Lou, Tianran Zhang, Xinquan Yue, Ya Jing, Chenyang Si
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SafeLoop: Risk-Aware Rollback for Vision-Language-Action Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SafeVLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent vision-language-action (VLA) models are promising for general-purpose manipulation, but long-horizon execution remains fragile. Small state-estimation or control errors can lead to irreversible failures (e.g., collisions and object drops). Avoiding these risks requires a proactive safety mechanism capable of anticipating hazards. In this paper, we introduce SafeLoop, a non-invasive external wrapper that adds hazard prediction and rollback-based recovery to a VLA model without changing its parameters. SafeLoop trains a risk predictor from vision and proprioception to output four values: the probability and time-to-hazard for body collisions and for object failures. A lightweight controller then chooses one of three actions based on the predicted risk: continue execution (noop), save a safety checkpoint (record), or retreat in joint space (rollback). Rollback moves the robot back to a recent safe waypoint and queries the base policy again, which may yield an alternative continuation. Across 24 LIBERO tasks (16 random seeds each) and three real-robot tasks (25 rollouts each), SafeLoop achieves a stronger overall safety-success trade-off than alternative methods, reducing hazard cases by roughly 70% while preserving task success and the base-policy control rate. Project code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/RoboTwin-Phys_Do_WAMs_and_VLAs_Understand_the_Physical_World|RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?]]

![[assets/2609.26292_figure.jpg|800]]

- **arXiv**: [2609.26292](https://arxiv.org/abs/2609.26292)
- **PDF**: https://arxiv.org/pdf/2609.26292
- **详细分析**: [[20_Research/Papers/具身智能/RoboTwin-Phys_Do_WAMs_and_VLAs_Understand_the_Physical_World|RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?]]
- **作者**: Jiaqi Zhang, Feng Ye, Mingjia Yang, Zhihong Chen, Mingkang Xiang, Xinglin Yao, Yanbin Li, Siwei Ma, Chuanmin Jia
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《RoboTwin-Phys: Do WAMs and VLAs Understand the Physical World?》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Galaxea-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical-condition diversity is largely missing from current benchmarks for robot manipulation. While large-scale simulation benchmarks increasingly incorporate variations in object appearance, scene layout, and visual observations, they typically keep the underlying physical parameters fixed. As a result, important sources of real-world variability, such as changes in mass, friction, and joint dynamics, remain largely untested. We introduce RoboTwin-Phys, a physics-diverse benchmark that treats physical-condition diversity as an explicit dimension of robot manipulation evaluation. The benchmark continuously varies 13 physical attributes within physically plausible ranges, providing a unified setting for evaluating policies across diverse physical operating conditions. We further release more than 5,000 expert demonstrations with ground-truth physical parameters, enabling physical-attribute estimation, condition-aware modeling, and physics-conditioned policy training. Evaluations of representative WAMs and VLAs reveal a substantial robustness gap: models that remain effective under existing visual and layout randomization can degrade markedly under changes in physical conditions. RoboTwin-Phys provides the benchmark, data, and evaluation protocol needed to systematically measure and improve robustness to physical-condition diversity in robot manipulation.

</details>

---

### [[20_Research/Papers/机器人/Toward_Self-Repairing_Ubiquitous_Robots_Using_Goal-Oriented_Agentic_AI_in_Human-Robot_Interactions|Toward Self-Repairing Ubiquitous Robots Using Goal-Oriented Agentic AI in Human-Robot Interactions]]

![[assets/2609.26155_figure.png|800]]

- **arXiv**: [2609.26155](https://arxiv.org/abs/2609.26155)
- **PDF**: https://arxiv.org/pdf/2609.26155
- **详细分析**: [[20_Research/Papers/机器人/Toward_Self-Repairing_Ubiquitous_Robots_Using_Goal-Oriented_Agentic_AI_in_Human-Robot_Interactions|Toward Self-Repairing Ubiquitous Robots Using Goal-Oriented Agentic AI in Human-Robot Interactions]]
- **作者**: Morten Roed Frederiksen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Toward Self-Repairing Ubiquitous Robots Using Goal-Oriented Agentic AI in Human-Robot Interactions》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ubiquitous robotic systems often lack traditional visual interfaces, making natural language interaction important for maintenance and repair. This paper presents a goal-oriented agentic AI architecture that enables non-expert users to complete technical repair tasks through situated dialogue. The architecture separates pre-interaction goal decomposition, persistent state tracking, strategic goal management, and real-time conversational execution. We evaluated the system in a physical hardware repair task with twenty participants. Nineteen participants completed the task, corresponding to a 95% completion rate. Participants rated the system as helpful and competent, and the agent remained robust to conversational diversions such as meta-queries and code-switching. A comparison with a prior online baseline showed that physical interaction significantly reduced perceived social presence, (p=.0005), and trust and competence, (p=.037), while perceived helpfulness remained high.

</details>

---

### [[20_Research/Papers/机器人/Design_and_Implementation_of_an_Ultra-Low-Cost_Wall-Climbing_Robot_for_Infrastructure_Crack_Detection|Design and Implementation of an Ultra-Low-Cost Wall-Climbing Robot for Infrastructure Crack Detection]]

![[assets/2609.26130_figure.png|800]]

- **arXiv**: [2609.26130](https://arxiv.org/abs/2609.26130)
- **PDF**: https://arxiv.org/pdf/2609.26130
- **详细分析**: [[20_Research/Papers/机器人/Design_and_Implementation_of_an_Ultra-Low-Cost_Wall-Climbing_Robot_for_Infrastructure_Crack_Detection|Design and Implementation of an Ultra-Low-Cost Wall-Climbing Robot for Infrastructure Crack Detection]]
- **作者**: Mrinmoy Modak, Supreyo Chakravorty Pretom, Shourv Tarafder, Daniel S. Drew
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Design and Implementation of an Ultra-Low-Cost Wall-Climbing Robot for Infrastructure Crack Detection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EfficientNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Crack detection is a crucial process to ensure the safety and longevity of buildings and other infrastructure. In this paper, we developed a low-cost, automated crack detection robot that leverages CNN, EfficientNet-B0, and YOLOv8 for efficient identification of cracks in concrete surfaces with a curated crack image dataset introduced to support training and evaluation. YOLOv8's real-time object detection enhances crack localization, while CNN and EfficientNet-B0 provide binary classification, ensuring high precision and recall. The system consists of two stages. In the first stage, YOLOv8 detects and localizes wall regions from the video frame, and the bounding boxes are cropped. The second stage performs crack detection using one of three models by analyzing the cropped regions. Cost-effective approaches are also taken for robot design. The robot features a fan-based negative pressure adhesion system, a 4-wheeled skid-steering drive, and an ESP32-CAM for real-time image capture. Its lightweight 3D-printed chassis ensures stability, allowing it to navigate both walls and ceilings while capturing images for crack analysis. Unlike conventional wall-climbing robot designs, this robot incorporates a funnel-shaped body that enhances negative pressure generation and achieves a 44% reduction in duty cycle, significantly lowering power consumption. By combining low-cost hardware with a deep learning pipeline, our system provides a scalable, efficient, and accessible solution for real-time infrastructure inspection at an approximate total cost of $25, with a lightweight web application enabling smartphone-based control. This affordability makes the system more suitable for the developing world, where infrastructure inspection is often limited by budget constraints, labor intensity, and safety risks.

</details>

---

### [[20_Research/Papers/具身智能/GDLAM_Group-Disentangled_Latent_Action_Model_for_Highly_Disentangled_Embodied_Pretraining|GDLAM: Group-Disentangled Latent Action Model for Highly Disentangled Embodied Pretraining]]

![[assets/2609.26118_figure.png|800]]

- **arXiv**: [2609.26118](https://arxiv.org/abs/2609.26118)
- **PDF**: https://arxiv.org/pdf/2609.26118
- **详细分析**: [[20_Research/Papers/具身智能/GDLAM_Group-Disentangled_Latent_Action_Model_for_Highly_Disentangled_Embodied_Pretraining|GDLAM: Group-Disentangled Latent Action Model for Highly Disentangled Embodied Pretraining]]
- **作者**: Jiarui Yang, Jiawei Li, Jiale Zhang, Hang Guo, Wen Huang, Maowei Hu, Tao Dai, Shu-Tao Xia
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.0（加权：具身智能 2.1，世界模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《GDLAM: Group-Disentangled Latent Action Model for Highly Disentangled Embodied Pretraining》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent action models (LAMs) learn action-related representations from action-free videos via self-supervised future prediction, offering a scalable paradigm for embodied intelligence pretraining. However, existing LAMs collapse heterogeneous sources of visual change, including camera motion, object dynamics, and interaction events, into a single latent vector, resulting in entangled representations with limited semantic structure and consequently restricting world model controllability and VLA policy generalization. We introduce the Group-Disentangled Latent Action Model (GDLAM), a latent action model whose code is factorized by construction into N groups, each with an independent variational bottleneck and a spatially gated routing pathway, and trained with a set of information-geometric objectives: mutual exclusivity, group and gate sparsity, and static-dynamic orthogonality, that make the groups mutually causally distinct rather than merely decorrelated. Quantitatively, intervening on any single group changes only that group and leaves the others intact, and GDLAM improves label-free disentanglement metrics, including Modularity, MIG, and DCI, by wide margins over a strong unstructured LAM. Notably, this factorization is not at the expense of action information: across three mutual-information estimators and a linear probe, the grouped code is more informative than monolithic baselines both in- and out-of-distribution. As supporting evidence that the disentangled code is a reusable pretraining currency, we further transfer it to two downstream regimes: (1) World Modeling: World models pretrained with GDLAM achieve superior rollout fidelity and action-following capability compared with SOTA baselines. (2) VLA Policies: Pretraining with GDLAM substantially improves task success rates over previous methods across multiple simulation benchmarks and real-world robotic manipulation tasks

</details>

---

### [[20_Research/Papers/机器人/Acoustic_Ellipses_Bio-Inspired_Omnidirectional_Echolocation_in_Cooperative_Multi-Agent_Systems_using_Frequency_Sweeps|Acoustic Ellipses: Bio-Inspired Omnidirectional Echolocation in Cooperative Multi-Agent Systems using Frequency Sweeps]]

![[assets/2609.26085_figure.png|800]]

- **arXiv**: [2609.26085](https://arxiv.org/abs/2609.26085)
- **PDF**: https://arxiv.org/pdf/2609.26085
- **详细分析**: [[20_Research/Papers/机器人/Acoustic_Ellipses_Bio-Inspired_Omnidirectional_Echolocation_in_Cooperative_Multi-Agent_Systems_using_Frequency_Sweeps|Acoustic Ellipses: Bio-Inspired Omnidirectional Echolocation in Cooperative Multi-Agent Systems using Frequency Sweeps]]
- **作者**: Petras Swissler, Lindsay Burke, Julia Hyland Bruno
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Acoustic Ellipses: Bio-Inspired Omnidirectional Echolocation in Cooperative Multi-Agent Systems using Frequency Sweeps》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Inspired by the flight and song of birds, we propose an approach that enables cooperating agents to effectively identify obstacles in their environment by having a stationary source agent emit a frequency-modulated chirp while one or more listener agents observe the direct and reflected signals while in motion. We present a novel mapping approach that exploits the ``frequency gap'' between direct and reflected chirp signals to define candidate reflection ellipses, which are then fed into a 2D accumulation filter to identify locations with the highest density of potential reflections. We demonstrate this work first with simulation results derived from an efficient, bespoke audio simulator, examining the effect of obstacle count, sampling rate, and path curvature on the ability to accurately identify environmental obstacles for a one-listener scenario. We then examine different cooperative motion strategies for two-listener configurations. Finally, we validate the real-world viability of this approach through field experiments in an outdoor park setting to demonstrate the ability to identify frequency gaps using off-the-shelf hardware. Our results provide a foundation for a low-cost approach to environmental mapping in swarm robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Vision-Language_Models_as_copilots_for_Autonomous_UAV_Navigation_Analysis_of_Latency_and_Reliability_in_Degraded_Environments|Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments]]

![[assets/2609.26084_figure.png|800]]

- **arXiv**: [2609.26084](https://arxiv.org/abs/2609.26084)
- **PDF**: https://arxiv.org/pdf/2609.26084
- **详细分析**: [[20_Research/Papers/具身智能/Vision-Language_Models_as_copilots_for_Autonomous_UAV_Navigation_Analysis_of_Latency_and_Reliability_in_Degraded_Environments|Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments]]
- **作者**: Hiago Sodre, Sebastian Barcelona, Vincent Sandin, Pablo Moraes, Ahilen Mazondo, Igor Nunes, William Moraes, André Kelbouscas, Ricardo Grando
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, EmbodiedAI, Systems

#### 研究背景与动机

《Vision-Language Models as copilots for Autonomous UAV Navigation: Analysis of Latency and Reliability in Degraded Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The integration of Vision-Language Models (VLMs) in autonomous Unmanned Aerial Vehicles (UAVs) offers unprecedented semantic reasoning capabilities. However, real-time closed-loop navigation requires not only low inference latency but also obedience to structured flight commands. This paper proposes a hybrid FSM-VLM control architecture for UAVs in GPS-free environments. The system combines a deterministic Finite State Machine (FSM) for low-level physical control with an asynchronous VLM copilot for high-level semantic pathfinding. We evaluate three models with different parameter scales in a Software-In-The-Loop (SITL) simulation. The framework isolates and measures syntax errors at the format level versus semantic hallucinations at the logic level in a normal and degraded scenario. This study demonstrates that parameter scaling, and not pure latency, remains the primary bottleneck for the safe and compatible integration of VLM into autonomous flights.

</details>

---

### [[20_Research/Papers/具身智能/Situation_Aware_Locomotion_for_Dual_Mobile_Cobots_in_Shared_Environments|Situation Aware Locomotion for Dual Mobile Cobots in Shared Environments]]

![[assets/2609.26083_figure.png|800]]

- **arXiv**: [2609.26083](https://arxiv.org/abs/2609.26083)
- **PDF**: https://arxiv.org/pdf/2609.26083
- **详细分析**: [[20_Research/Papers/具身智能/Situation_Aware_Locomotion_for_Dual_Mobile_Cobots_in_Shared_Environments|Situation Aware Locomotion for Dual Mobile Cobots in Shared Environments]]
- **作者**: William Moraes, Igor Nunes, Ahilen Mazondo, Sebastian Barcelona, Hiago Sodre, Pablo Moraes, Ricardo B. Grando
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Situation Aware Locomotion for Dual Mobile Cobots in Shared Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a situation aware locomotion framework for two mobile collaborative robots operating in shared industrial environments. The proposed method models situation awareness through perception, comprehension, and projection to support locomotion decisions. Robot pose, load state, manipulator state, shared zone occupancy, obstacle state, and predicted inter robot conflict were used to select safe locomotion actions. The framework was implemented in simulation and evaluated in simulated industrial scenarios designed to match a feasible 4 m by 4 m physical test area. The proposed method was compared with two other baselines over multiple trials and randomized seeds. The results show that the situation aware method achieved 100% task success across all scenarios, while the independent and fixed priority baselines each achieved 33.3% overall success. The proposed method eliminated shared zone conflicts and safety stops, maintained the largest average minimum inter robot distance, and completed the tasks with the lowest average completion time. These results indicate that situational awareness can improve the locomotion of dual robots by combining load state, manipulator state, reasoning about the shared zone, and prediction of short-horizon conflicts.

</details>

---

### [[20_Research/Papers/具身智能/StrataVLA_Hierarchical_and_Efficient_3D_Geometric_Grounding_for_Vision-Language-Action_Models|StrataVLA: Hierarchical and Efficient 3D Geometric Grounding for Vision-Language-Action Models]]

![[assets/2609.26071_figure.png|800]]

- **arXiv**: [2609.26071](https://arxiv.org/abs/2609.26071)
- **PDF**: https://arxiv.org/pdf/2609.26071
- **详细分析**: [[20_Research/Papers/具身智能/StrataVLA_Hierarchical_and_Efficient_3D_Geometric_Grounding_for_Vision-Language-Action_Models|StrataVLA: Hierarchical and Efficient 3D Geometric Grounding for Vision-Language-Action Models]]
- **作者**: Jin Cui, Zhaoyu Pu, Botao Cai, Jun Ye, Xinyue Long, Boran Zhao, Pengju Ren
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《StrataVLA: Hierarchical and Efficient 3D Geometric Grounding for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, StrataVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models inherit strong semantic priors from large-scale vision-language pretraining, yet remain limited in robotic manipulation by insufficient 3D spatial awareness. Existing approaches either require explicit depth or point-cloud inputs, compress geometry into training-time supervision, or inject it only at the model input or action expert, leaving the vision-language backbone without persistent access to task-relevant spatial information. We introduce StrataVLA, a plug-and-play framework for hierarchical geometric grounding. A frozen geometry foundation model extracts shared geometric features from RGB observations, while sparse, layer-specific Geometry Adapters allow visual representations at selected backbone depths to retrieve relevant geometric evidence through cross-attention. To make inference-time geometry practical, StrataVLA further combines task-aware routing with an LRU feature cache that exploits temporal redundancy during task manipulation. Experiments on LIBERO, SimplerEnv, and real-world manipulation demonstrate consistent gains over strong VLA baselines. StrataVLA achieves 98.53% average success on LIBERO suites while reducing geometry-model invocations by up to 88%, establishing hierarchical geometry injection as an effective and efficient way to achieve spatially grounded robotic control.

</details>

---

### [[20_Research/Papers/机器人/Towards_Intent-Aware_Human-Robot_Teaming_A_Platform_for_Search-and-Rescue_Operations|Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations]]

![[assets/2609.26051_figure.png|800]]

- **arXiv**: [2609.26051](https://arxiv.org/abs/2609.26051)
- **PDF**: https://arxiv.org/pdf/2609.26051
- **详细分析**: [[20_Research/Papers/机器人/Towards_Intent-Aware_Human-Robot_Teaming_A_Platform_for_Search-and-Rescue_Operations|Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations]]
- **作者**: Rohith Prem Maben, Ayesha Jena, Björn Olofsson, Stefan Reitmann, Jacek Malec, Rogier Woltjer, Elin Anna Topp
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Towards Intent-Aware Human-Robot Teaming: A Platform for Search-and-Rescue Operations》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate the challenges of enabling effective collaboration between human operators and heterogeneous autonomous agents in complex, dynamic environments by developing an interaction platform that allows study of operator behavior and supports intent inference and decision-making using state-of-the-art frameworks. We demonstrate the extent to which the operator's perception, decisions, and actions could be supported by autonomous systems during search-and-rescue operations with our platform.

</details>

---

### [[20_Research/Papers/具身智能/Safety-Constrained_Model_Predictive_Control_for_an_Omnidirectional_Walking_Assistive_Robot_Using_Control_Barrier_Function|Safety-Constrained Model Predictive Control for an Omnidirectional Walking Assistive Robot Using Control Barrier Function]]

![[assets/2609.25994_first_page.png|800]]

- **arXiv**: [2609.25994](https://arxiv.org/abs/2609.25994)
- **PDF**: https://arxiv.org/pdf/2609.25994
- **详细分析**: [[20_Research/Papers/具身智能/Safety-Constrained_Model_Predictive_Control_for_an_Omnidirectional_Walking_Assistive_Robot_Using_Control_Barrier_Function|Safety-Constrained Model Predictive Control for an Omnidirectional Walking Assistive Robot Using Control Barrier Function]]
- **作者**: Andrea Fortuna, Marta Lorenzini, Elisa Motta, Alberto Ranavolo, Elena De Momi, Arash Ajoudani
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Safety-Constrained Model Predictive Control for an Omnidirectional Walking Assistive Robot Using Control Barrier Function》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Providing safe and effective mobility assistance plays a crucial role in restoring independence and enhancing the quality of life for individuals with motor impairments. In this context, robotic walking assistive devices have recently emerged as promising solutions to provide physically compliant interaction while ensuring user safety and support. This paper presents a novel control framework for an omnidirectional Walking Assistive Robot (I-WANDER) that integrates a Control Barrier Function (CBF) formulation into a Model Predictive Control (MPC) scheme to explicitly enforce collision-avoidance safety constraints while optimizing for energy efficiency and smooth human-robot collaboration. The method was experimentally evaluated with 12 healthy participants performing two different walking tasks using both the proposed CBF-based MPC controller (CB-MPC) and a variable admittance controller (AC). The first task involved structured navigation through a U-shaped corridor, whereas the second consisted of a single-obstacle avoidance task performed blindfolded to ensure the obstacle was unexpected. Comparative results show that the CB-MPC architecture significantly reduces energy consumption and mechanical work (p &lt; 0.01) without compromising motion smoothness, while also decreasing the number of obstacle collisions. Overall, the findings highlight the potential of the proposed control architecture to enhance both safety and efficiency in robotic walking assistance.

</details>

---

### [[20_Research/Papers/具身智能/Predict_Before_You_Step_Auditable_Occupancy_Forecasting_for_Dynamic_Obstacle_Avoidance_under_Sparse_Guidance|Predict Before You Step: Auditable Occupancy Forecasting for Dynamic Obstacle Avoidance under Sparse Guidance]]

![[assets/2609.25969_figure.png|800]]

- **arXiv**: [2609.25969](https://arxiv.org/abs/2609.25969)
- **PDF**: https://arxiv.org/pdf/2609.25969
- **详细分析**: [[20_Research/Papers/具身智能/Predict_Before_You_Step_Auditable_Occupancy_Forecasting_for_Dynamic_Obstacle_Avoidance_under_Sparse_Guidance|Predict Before You Step: Auditable Occupancy Forecasting for Dynamic Obstacle Avoidance under Sparse Guidance]]
- **作者**: Yuhui Mao, Fen Liu, Shenghai Yuan, Tianxin Hu, Ruimeng Liu, Rong Su
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Predict Before You Step: Auditable Occupancy Forecasting for Dynamic Obstacle Avoidance under Sparse Guidance》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots under sparse waypoint guidance must avoid moving obstacles using partial, rapidly changing LiDAR observations. We present LOOP (Latent-recurrent Occupancy rollOut Policy), a local avoidance policy that connects sparse waypoint guidance to a frozen locomotion controller at 50 Hz. From occupancy and ego-velocity histories, a recurrent predictor forecasts future occupancy over a 1 s horizon by warping the current map with learned flow and visibility gates. These maps guide velocity selection through map-derived features and geometric risk estimates, providing an explicit interface for inspecting and replacing predictions. In encounter-synchronised Isaac Lab evaluations, LOOP achieves 57.1% head-on success at obstacle speeds of 2.5-3.2 m/s, exceeding a retrained reactive baseline by 8.2 percentage points. Comparisons with a rollout-free BEV policy show smaller, scenario-dependent gains from the prediction branch, including improved crossing success and reduced variability across training seeds at the highest head-on speeds. The adapter runs onboard a Unitree Go2 in 14.5 ms per step and completes all 16 real-world crossing trials without collision, demonstrating deployment feasibility.

</details>

---

### [[20_Research/Papers/具身智能/Control_Barrier_Functions_for_Safe_Free-Flying_Robotic_Spacecraft_Operations_in_Tumbling_Target_Capture|Control Barrier Functions for Safe Free-Flying Robotic Spacecraft Operations in Tumbling Target Capture]]

![[assets/2609.25905_figure.png|800]]

- **arXiv**: [2609.25905](https://arxiv.org/abs/2609.25905)
- **PDF**: https://arxiv.org/pdf/2609.25905
- **详细分析**: [[20_Research/Papers/具身智能/Control_Barrier_Functions_for_Safe_Free-Flying_Robotic_Spacecraft_Operations_in_Tumbling_Target_Capture|Control Barrier Functions for Safe Free-Flying Robotic Spacecraft Operations in Tumbling Target Capture]]
- **作者**: Alexander Meinert, Peter Stadler, Niklas Baldauf, Alen Turnwald
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Control Barrier Functions for Safe Free-Flying Robotic Spacecraft Operations in Tumbling Target Capture》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a modular control barrier function (CBF) framework for safe free-flying robotic spacecraft operations during tumbling target capture. Motivated by latest ESA guidelines for safe close proximity operations, safety zones and requirements are translated into dedicated CBFs. The 13-DoF system is decomposed into translational, attitude, and robotic subsystems, each equipped with a safety filter that minimally modifies nominal control inputs in a lightweight quadratic program. The filters enforce a conical approach corridor, collision avoidance zone, attitude line-of-sight pointing, angular velocity limits, robotic joint limits, link-base collision avoidance, and actuator constraints. Dynamic coupling between subsystems is handled by treating upstream safe control commands as known interconnection inputs in the downstream safety filters, preserving modularity while supporting system-level safety. The framework is validated in an on-orbit servicing scenario, including final approach, angular rate synchronization, and tumbling target grasping, using the high-fidelity astrodynamics simulator Basilisk. Monte Carlo simulation results demonstrate runtime efficiency and operational safety for various tumbling rates.

</details>

---

### [[20_Research/Papers/具身智能/What_is_the_Better_Curriculum_Controller-Shaped_Grasping_Behavior_for_Contact_Force-Sensitive_Manipulation|What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation]]

![[assets/2609.25887_figure.png|800]]

- **arXiv**: [2609.25887](https://arxiv.org/abs/2609.25887)
- **PDF**: https://arxiv.org/pdf/2609.25887
- **详细分析**: [[20_Research/Papers/具身智能/What_is_the_Better_Curriculum_Controller-Shaped_Grasping_Behavior_for_Contact_Force-Sensitive_Manipulation|What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation]]
- **作者**: Ziyan Feng, Zizhao Yuan, Yulong Fu, Yuxin He, Zhiyuan Zhang, Zhengjie Zhang, Jinni Zhou, Renjing Xu, Qiang Nie
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《What is the Better Curriculum: Controller-Shaped Grasping Behavior for Contact Force-Sensitive Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoRL, CompliantVLA, HapticVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

How should a robot learn to manipulate objects so fragile that sub-Newton contact forces can cause irreversible damage? Existing visuo-tactile policy learning typically treats tactile sensing as an additional policy input. In direct-contact force-sensitive manipulation, however, the bottleneck can arise earlier, during data collection: manual gripper control is too delayed and coarse-grained to reliably maintain the narrow force range required for stable grasping. We therefore use a deterministic 25 Hz tactile reflex controller as a collection-time teacher, producing demonstrations with controller-shaped grasping behavior for tactile-free policy learning. On Action Chunking with Transformers (ACT), policies trained from reflex-shaped demonstrations recover the teacher's grasping profile and achieve 95% stable grasps on the nominal plastic-cup task, substantially outperforming visually screened manual demonstrations. The same intervention improves in-distribution stability on $\pi_{0.5}$ and shows a favorable exploratory trend on an unseen paper-cup variant. Under randomized external disturbance, however, the reflex-data $\pi_{0.5}$ policy still fails in 45% of policy-only trials, whereas a deployment-time reflex arbiter retains all grasps. These results reveal a new role for tactile feedback in force-sensitive manipulation: rather than integrating tactile into the policy, we use it as a collection-time teacher that shapes grasping behavior in demonstrations for policy learning, while disturbance rejection remains controller-dependent, revealing the boundary of tactile-free policy.

</details>

---

### [[20_Research/Papers/具身智能/VisForce_Visual_Grounding_of_Current_and_Desired_Forces_for_Goal-Conditioned_Dexterous_Manipulation|VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation]]

![[assets/2609.25785_figure.png|800]]

- **arXiv**: [2609.25785](https://arxiv.org/abs/2609.25785)
- **PDF**: https://arxiv.org/pdf/2609.25785
- **详细分析**: [[20_Research/Papers/具身智能/VisForce_Visual_Grounding_of_Current_and_Desired_Forces_for_Goal-Conditioned_Dexterous_Manipulation|VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation]]
- **作者**: Jung-Woo Lee, Soo-Chul Lim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《VisForce: Visual Grounding of Current and Desired Forces for Goal-Conditioned Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DexGraspVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as general-purpose robotic manipulation policies. However, in dexterous hand manipulation, contact forces are typically provided as separate states or force-specific representations, making it difficult to explicitly represent the spatial correspondence between force and their corresponding visual locations. In this work, we propose VisForce, which visually grounds the current and desired forces at their corresponding fingertip locations. VisForce renders current and desired visual force cues on the current wrist image and a task-specific goal image, and combines the two representations through goal-conditioned cross-attention to generate force-aware actions. We evaluate VisForce using a real UR10 robot equipped with an RH56F1 dexterous hand through force-conditioned grasping and three multi-stage manipulation tasks. In force-conditioned grasping experiments, VisForce exhibited a consistent grip-force response as the desired force increased, and achieved grasp-and-lift success rates of 70% and 80% for an egg and a toothpaste tube, respectively. It further achieved final success rates of 70%, 55%, and 40% on cup insertion/bottle pouring, tong-assisted bread transfer, and slip-modulated peg-in-hole, respectively. These results show that fingertip-aligned visual force representations can be effectively used for force-aware conditioning in VLA-based dexterous hand manipulation.

</details>

---

### [[20_Research/Papers/具身智能/MedVLA_A_Hierarchical_Vision-Language-Action_Framework_for_Closed-Loop_Precision_Medical_Robot_Manipulation|MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation]]

![[assets/2609.25756_figure.png|800]]

- **arXiv**: [2609.25756](https://arxiv.org/abs/2609.25756)
- **PDF**: https://arxiv.org/pdf/2609.25756
- **详细分析**: [[20_Research/Papers/具身智能/MedVLA_A_Hierarchical_Vision-Language-Action_Framework_for_Closed-Loop_Precision_Medical_Robot_Manipulation|MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation]]
- **作者**: Junjie Xie, Chuxuan He, Angen Ye, Yujia Song, Dapeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.0（加权：具身智能 2.7，大模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MedVLA: A Hierarchical Vision-Language-Action Framework for Closed-Loop Precision Medical Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MedVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Precision medical robotics demands adaptive decision-making under strict safety, interpretability, and execution constraints. Although recent Vision-Language-Action (VLA) models show strong multimodal reasoning ability, their continuous action generation paradigm is not well suited for precision medical tasks, where reliable closed-loop operation may also depend on non-action system function calls. To address this gap, we propose MedVLA, a hierarchical framework that couples high-level multimodal reasoning with low-level function-constrained execution. We further introduce a scalable multi-agent pipeline to generate skill-oriented chain-of-thought(CoT) data for structured training. Built on different multimodal large-model backbones, MedVLA consistently improves performance after fine-tuning, demonstrating the effectiveness of the proposed framework across model variants. Under identical initial conditions, we perform 100 closed-loop flexible electrode implantation trials. The results show that MedVLA achieves a 95.0\% task success rate, substantially outperforming representative VLA baselines, including OpenVLA (8\%) and $\pi_0$ (15\%), in accuracy, stability, and safety. These results indicate that structured reasoning with constrained function-level execution is a practical route toward deployable precision medical robotics.

</details>

---

### [[20_Research/Papers/强化学习/PLAT_Sparse_Timed_Keyframe_Motion_Tracking_for_Humanoid_Control_via_Privileged_Latent_Transition_Learning|PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning]]

![[assets/2609.25754_figure.png|800]]

- **arXiv**: [2609.25754](https://arxiv.org/abs/2609.25754)
- **PDF**: https://arxiv.org/pdf/2609.25754
- **详细分析**: [[20_Research/Papers/强化学习/PLAT_Sparse_Timed_Keyframe_Motion_Tracking_for_Humanoid_Control_via_Privileged_Latent_Transition_Learning|PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning]]
- **作者**: Zepeng Wang, Jiangxing Wang, Chao Ma, Xiaochuan Shi, Zongqing Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《PLAT: Sparse Timed Keyframe Motion Tracking for Humanoid Control via Privileged Latent Transition Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid motion tracking policies rely on dense frame-by-frame references, limiting their use as high-level motion controllers for planning and interactive motion generation. We study \emph{Sparse Timed Keyframe Motion Tracking}, where a policy receives only sparse future keyframes and their desired arrival times, and must execute stable whole-body motions that reach successive goals. We propose \textbf{PLAT}, a three-stage sparse timed keyframe motion tracking policy learning framework with \textbf{P}rivileged \textbf{LA}tent \textbf{T}ransition learning. PLAT bridges dense motion tracking and sparse goal-conditioned control by exploiting dense goal sequences as privileged supervision during training while requiring only sparse timed keyframe commands at deployment. A pretrained dense tracking expert first provides robust motion priors. A privileged latent prior is then learned through DAgger-style imitation, followed by latent residual reinforcement learning that refines latent transitions instead of directly optimizing actions. Extensive simulation experiments demonstrate that PLAT maintains accurate and stable sparse timed keyframe tracking across varying planning horizons, with particularly strong performance under long-horizon commands. Successful deployment on a Unitree G1 humanoid robot further demonstrates the effectiveness and practicality of PLAT for sparse humanoid motion control.

</details>

---

### [[20_Research/Papers/具身智能/Fisheye-VLA_Decoupling_Coverage_and_Acuity_for_Manipulation_with_a_Single_Fisheye_Camera|Fisheye-VLA: Decoupling Coverage and Acuity for Manipulation with a Single Fisheye Camera]]

![[assets/2609.25750_figure.png|800]]

- **arXiv**: [2609.25750](https://arxiv.org/abs/2609.25750)
- **PDF**: https://arxiv.org/pdf/2609.25750
- **详细分析**: [[20_Research/Papers/具身智能/Fisheye-VLA_Decoupling_Coverage_and_Acuity_for_Manipulation_with_a_Single_Fisheye_Camera|Fisheye-VLA: Decoupling Coverage and Acuity for Manipulation with a Single Fisheye Camera]]
- **作者**: Ziang Ren, Zike Yan, Raymond Zhang, Xuguo He, Zhongyu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Fisheye-VLA: Decoupling Coverage and Acuity for Manipulation with a Single Fisheye Camera》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EyeGym, Fisheye-VLA, OpenVLA, WristWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulation requires both broad scene awareness and detailed local feedback, yet conventional camera rigs provide them through separate front and wrist cameras. We present Fisheye-VLA, a visual interface that brings these capabilities together using a single passive fisheye. A global view preserves the workspace, while local perspective crops direct detail toward the interaction. The key design question is where this local visual budget should go. We answer it through a controlled re-rendering study, comparing alternative crop directions on the same recorded observations. The study finds that end-effector-centered views capture most of the estimated benefit of a much larger candidate pool, motivating a compact allocation around both hands. Our interface uses calibrated end-effector projection and motion lead to track the crops, while a shared ray encoding preserves their spatial meaning as they move. Integrated with a pretrained VLA, it achieves 84% and 82% success in the two expanded tabletop regions, where some target placements extend beyond the front-camera coverage, and supports shelf and conveyor manipulation. Ablations show that local crops and their viewing directions become more important in the larger workspace regions. The results demonstrate that a single fisheye can support these manipulation tasks without physical wrist cameras.

</details>

---

### [[20_Research/Papers/具身智能/The_Cartesian_Hand_In-Hand_Manipulation_with_All-Linear_Fingers|The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers]]

![[assets/2609.25696_figure.png|800]]

- **arXiv**: [2609.25696](https://arxiv.org/abs/2609.25696)
- **PDF**: https://arxiv.org/pdf/2609.25696
- **详细分析**: [[20_Research/Papers/具身智能/The_Cartesian_Hand_In-Hand_Manipulation_with_All-Linear_Fingers|The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers]]
- **作者**: Boxi Xia, Bokuan Li, Ryan Shin, Zijiang Yang, Jiaxun Liu, Boyuan Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《The Cartesian Hand: In-Hand Manipulation with All-Linear Fingers》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ARL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation has increasingly pursued human-like dexterous hands with many articulated degrees of freedom, offering rich manipulation capabilities at the cost of mechanical and control complexity. At the other extreme, parallel grippers are simple and robust, but provide little ability to manipulate an object after grasping it. Operating articulated objects such as threaded containers, manufacturing tools, and laboratory instruments often requires a second gripper, an external fixture, or coordinated arm motion. We introduce the Cartesian Hand, a 7-DoF end-effector that rethinks dexterous manipulation by combining independent grasping and relative manipulation within a single end-effector using only linear motion. Two independently actuated parallel grippers hold different parts of an object, while four translating fingertips generate relative motion between the grasped parts. Its configuration-independent fingertip kinematics allow manipulation to be composed from simple linear motion primitives. The Cartesian Hand is particularly suited to objects structured around common mechanisms such as threads, pivots, linear guides, plungers, and triggers. We demonstrate cap opening and closing, pipetting, pumping, two-handle manipulation, screwdriving, trigger actuation, and in-grasp reorientation across 35 objects spanning laboratory, manufacturing, and household settings. The same manipulation procedures transfer from a fixed-base robot arm to a humanoid, where we demonstrate bimanual laboratory manipulation using two Cartesian Hands. These results show that versatile in-hand manipulation capability can emerge from a mechanically simple architecture when independent grasping and relative motion are designed directly into the end-effector. We will open-source all software and hardware design. Our website is this https URL .

</details>

---

### [[20_Research/Papers/机器人/Induced_Riemannian_Metrics_for_Motion_Planning_with_Constraints|Induced Riemannian Metrics for Motion Planning with Constraints]]

![[assets/2609.25695_figure.png|800]]

- **arXiv**: [2609.25695](https://arxiv.org/abs/2609.25695)
- **PDF**: https://arxiv.org/pdf/2609.25695
- **详细分析**: [[20_Research/Papers/机器人/Induced_Riemannian_Metrics_for_Motion_Planning_with_Constraints|Induced Riemannian Metrics for Motion Planning with Constraints]]
- **作者**: Phone Thiha Kyaw, Thomas Cohn, Miguel Angel Rogel Garcia, Jonathan Kelly
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Induced Riemannian Metrics for Motion Planning with Constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In constrained motion planning problems, task and loop-closure constraints restrict a robot's motion to a curved, lower-dimensional submanifold of its configuration space. Planners measure path length with a metric, which sets the cost of moving in each direction. Under the Euclidean metric, this cost is the same everywhere, whereas under a general Riemannian metric, such as the kinetic-energy metric, the cost can vary with direction and configuration. Existing methods often describe the submanifold either implicitly, as a constraint level set, or explicitly, through a parameterization. The implicit representation is typically combined with the Euclidean metric of the configuration space, and the explicit representation with the parameter domain, so the path length that a planner minimizes depends on the representation. Instead, we measure path length with the induced metric, which the submanifold inherits from a Riemannian metric on the configuration space. The implicit and explicit representations yield the same induced metric, expressed in different coordinates, and hence the same geometry. This result holds for any Riemannian metric on the configuration space, not only the Euclidean one. The choice of metric is therefore independent of the choice of representation. Using this result, we extend planning under a Riemannian metric from unconstrained spaces to constraint submanifolds by applying the induced metric in both a sampling-based planner and a trajectory optimizer. For an explicit representation, the induced metric also accounts for the distortion that the parameterization introduces. In experiments on a bimanual manipulation setup with two Franka arms under end-effector task constraints, we compare the Euclidean and kinetic-energy metrics.

</details>

---

### [[20_Research/Papers/具身智能/MotionForge_A_Data_Generation_Pipeline_and_Large-Scale_Benchmark_for_Long-Horizon_Manipulation_of_Dynamic_Objects_with_Domain_Shifts|MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts]]

![[assets/2609.25689_figure.png|800]]

- **arXiv**: [2609.25689](https://arxiv.org/abs/2609.25689)
- **PDF**: https://arxiv.org/pdf/2609.25689
- **详细分析**: [[20_Research/Papers/具身智能/MotionForge_A_Data_Generation_Pipeline_and_Large-Scale_Benchmark_for_Long-Horizon_Manipulation_of_Dynamic_Objects_with_Domain_Shifts|MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts]]
- **作者**: Mohan Liu, Dengchen Mei, Haotian Xian, Ruyang Han, Jiayi Sun, Xuanyu Chen, Haitian Zhang, Luxi Li, Kaimin Mao, Lin Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《MotionForge: A Data Generation Pipeline and Large-Scale Benchmark for Long-Horizon Manipulation of Dynamic Objects with Domain Shifts》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DynamicVLA, PhysMani-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in learning-based robot policies have demonstrated promising progress, yet they are predom- inantly evaluated in static or quasi-static environments. In dynamic manipulation, objects and scenes continuously evolve while the robot perceives, reasons, and acts. However, recent dynamic simulation benchmarks largely focus on short-horizon, reactive interactions with simple motion patterns and offer limited support for both systematic evaluation under domain shifts and model-agnostic real-time execution protocols. To bridge these gaps, we introduce MotionForge, the first large- scale simulation benchmark and data-generation pipeline tailored to jointly evaluate domain shifts and long-horizon interaction in dynamic manipulation. MotionForge comprises 40 dynamic interaction tasks spanning 11 distinct motion patterns, with dedicated support for 17 long-horizon tasks. Our benchmark introduces two key novelties: (1) a systematic evaluation protocol for assessing policy robustness under both single-factor (e.g., only backgrounds shift) and joint domain shifts (e.g., simultaneous shifts of objects, backgrounds, lighting, and speed); and (2) a decoupled, latency-aware execution protocol where the environ- ment continuously evolves independently of policy inference time. Extensive evaluations of representative general-purpose robot policies on our benchmark reveal substantial limitations under joint domain shifts. These findings expose a critical gap between current policy capabilities and the requirements of robust long- horizon manipulation of dynamic objects under domain shifts, establishing MotionForge as a comprehensive testbed for future research in embodied AI.

</details>

---

### [[20_Research/Papers/机器人/MatcherCompass_A_Deployment-Aware_Benchmark_to_Guide_Image_Matcher_Selection_in_the_Wild|MatcherCompass: A Deployment-Aware Benchmark to Guide Image Matcher Selection in the Wild]]

![[assets/2609.25688_figure.png|800]]

- **arXiv**: [2609.25688](https://arxiv.org/abs/2609.25688)
- **PDF**: https://arxiv.org/pdf/2609.25688
- **详细分析**: [[20_Research/Papers/机器人/MatcherCompass_A_Deployment-Aware_Benchmark_to_Guide_Image_Matcher_Selection_in_the_Wild|MatcherCompass: A Deployment-Aware Benchmark to Guide Image Matcher Selection in the Wild]]
- **作者**: Hyunwoo Kim, Giseop Kim
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《MatcherCompass: A Deployment-Aware Benchmark to Guide Image Matcher Selection in the Wild》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：STAR-Bench, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Field robots operating across time of day and sensing modalities require accurate image correspondences within onboard time and resource budgets. However, accuracy and runtime reported for individual methods on a single device provide limited guidance for choosing a matcher and its configuration on a target platform. We present MatcherCompass, a deployment-aware benchmark for choosing local feature matchers in field robotics. Under common input and pose-evaluation procedures, we compare nine classical and learned matching pipelines across four image resolutions and supported numerical precisions. Four visual conditions cover viewpoint variation, day--night matching in visible and thermal imagery, and daytime visible--thermal matching. We evaluate pose accuracy using the area under the error--recall curve (AUC) at $5^\circ$, $10^\circ$, and $20^\circ$, and measure runtime, GPU memory, and energy per image pair on four GPU platforms spanning workstation and onboard computers. The results show that changes in hardware, input resolution, and numerical precision can move a matcher across a runtime budget boundary, altering the feasible choices. We organize the measurements into a selection guide that returns all configurations satisfying user-specified time and resource limits, together with their accuracy under the selected visual condition. MatcherCompass provides measured evidence for choosing matching pipelines that fit a robot's sensing conditions and computing hardware. Project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/SG-CPG_Severity-Gated_Central_Pattern_Generators_for_Adaptive_Quadruped_Locomotion_under_Continuous_Actuator_Degradation|SG-CPG: Severity-Gated Central Pattern Generators for Adaptive Quadruped Locomotion under Continuous Actuator Degradation]]

![[assets/2609.25687_figure.png|800]]

- **arXiv**: [2609.25687](https://arxiv.org/abs/2609.25687)
- **PDF**: https://arxiv.org/pdf/2609.25687
- **详细分析**: [[20_Research/Papers/具身智能/SG-CPG_Severity-Gated_Central_Pattern_Generators_for_Adaptive_Quadruped_Locomotion_under_Continuous_Actuator_Degradation|SG-CPG: Severity-Gated Central Pattern Generators for Adaptive Quadruped Locomotion under Continuous Actuator Degradation]]
- **作者**: Adarsh Kumar Kosta, Kaushik Roy
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SG-CPG: Severity-Gated Central Pattern Generators for Adaptive Quadruped Locomotion under Continuous Actuator Degradation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CPG-RL, FT-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An animal with a weakened limb does not necessarily switch its gait, instead it unloads the affected limb, re-coordinates the remaining limbs, and scales its response with injury severity. This graded adaptation allows locomotion to persist despite partial loss of limb strength, rather than requiring a discrete transition between healthy and failed. Inspired by this behavior, we propose SG-CPG, a central pattern generator (CPG) for quadruped locomotion under continuous actuator degradation. SG-CPG preserves a frozen healthy CPG policy and introduces two severity-driven gates: a residual gate that re-coordinates all four legs and an amplitude gate that progressively shortens the weakened leg's stride as degradation increases. We emulate progressive degradation through two mechanisms: lowering the joint torque ceiling (ceiling mechanism) and scaling its low-level controller gains (gain mechanism), representing distinct forms of actuator weakening. Our simulations on a Unitree Go2 show that SG-CPG maintains a trot gait with 100% survival across an omnidirectional command schedule under 95% joint strength loss while tracking commands within 8%. Under a lowered torque ceiling, removing either severity path, the residual's severity observation or the amplitude gate, raises clipping at the weakened joint from 4.4% to 13.6% and 26.3% of steps at an 80% loss. On a real Go2, SG-CPG survives 28 of 29 forward and turning trials with up to 93% calf torque degradation. These results show that severity-gated adaptation can extend a healthy locomotion policy to progressive actuator degradation without treating the fault as a discrete failure.

</details>

---

### [[20_Research/Papers/具身智能/Deploying_Foundation_Models_for_Embodied_Navigation|Deploying Foundation Models for Embodied Navigation]]

![[assets/2609.25666_figure.png|800]]

- **arXiv**: [2609.25666](https://arxiv.org/abs/2609.25666)
- **PDF**: https://arxiv.org/pdf/2609.25666
- **详细分析**: [[20_Research/Papers/具身智能/Deploying_Foundation_Models_for_Embodied_Navigation|Deploying Foundation Models for Embodied Navigation]]
- **作者**: Vishnu Sashank Dorbala, Dinesh Manocha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Deploying Foundation Models for Embodied Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present and tackle two problems associated with deploying Foundation Models (FMs) on Embodied Agents performing navigation: 1) Training bias in FMs leading to poor personalization in unseen environments, and 2) Limited FM context length hindering success, especially on long horizon tasks. Our solution for the former involves priming the FM with human-habit data mined from the scene and our solution for the latter involves active memory management via a novel `memory head' augmentation. We first present a taxonomy of existing literature on FM-based Embodied Navigation, and highlight these limitations. We then present our approaches, Transit-Aware Planning (TAP) and MemCtrl to address the limitations. With TAP, we present real-world results in a lab environment with a Turtlebot for personalized target finding that shows an average improvement of 18% over a non-TAP baseline. On MemCtrl, we report a 6% average improvement across various embodied tasks, with 20% on long instruction subsets, all while using nearly half the context used in the baseline model. Motivated by these result, we present our stance the deployability of FM-based embodied agents in real-world environments, and highlight open research directions.

</details>

---

### [[20_Research/Papers/具身智能/PhyVisGen_Physically_and_Visually_High-Fidelity_Robotic_Manipulation_Data_Generation|PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation]]

![[assets/2609.25653_figure.png|800]]

- **arXiv**: [2609.25653](https://arxiv.org/abs/2609.25653)
- **PDF**: https://arxiv.org/pdf/2609.25653
- **详细分析**: [[20_Research/Papers/具身智能/PhyVisGen_Physically_and_Visually_High-Fidelity_Robotic_Manipulation_Data_Generation|PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation]]
- **作者**: Yu Zheng, Qiyu Feng, Yixin Wu, Baoquan Yang, Yixuan Zhou, Bingyang Hu, Kemeng Huang, Guansheng Yang, Hesheng Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《PhyVisGen: Physically and Visually High-Fidelity Robotic Manipulation Data Generation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IPC-GraspSim, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale manipulation demonstrations are essential for learning robust visuomotor policies, yet real-world data collection is expensive and difficult to scale. Simulation offers a promising alternative, but physical and visual discrepancies can limit the transferability of synthetic data, particularly for manipulation with soft grippers. We present PhyVisGen, a physically and visually high-fidelity framework for scalable robotic manipulation data generation. On the physical side, PhyVisGen introduces an arm-gripper coupling method based on the Incremental Potential Contact (IPC), enabling high-fidelity soft contact throughout complete manipulation trajectories. On the visual side, it combines real-scene reconstruction with real-time path tracing to generate visually realistic observations while preserving captured scene appearance. Quantitative evaluations demonstrate the physical and visual fidelity of PhyVisGen. Policies trained exclusively on synthetic manipulation demonstrations achieve 65-95% success across five real-robot tasks, without real-robot demonstration data or policy fine-tuning.

</details>

---

### [[20_Research/Papers/具身智能/Skill_Sequence_Planning_for_Collaborative_Multi-Robot_Construction|Skill Sequence Planning for Collaborative Multi-Robot Construction]]

![[assets/2609.25649_figure.png|800]]

- **arXiv**: [2609.25649](https://arxiv.org/abs/2609.25649)
- **PDF**: https://arxiv.org/pdf/2609.25649
- **详细分析**: [[20_Research/Papers/具身智能/Skill_Sequence_Planning_for_Collaborative_Multi-Robot_Construction|Skill Sequence Planning for Collaborative Multi-Robot Construction]]
- **作者**: Xi Wang, Bo Fu, Carol C. Menassa, Vineet R. Kamat, Min Deng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Skill Sequence Planning for Collaborative Multi-Robot Construction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots have significant potential to automate construction processes. However, their industry adoption remains limited, partly because of the programming effort required to adapt robots to diverse tasks. This paper presents a skill sequence planning method that enables a heterogeneous team of multi-functional robots to collaboratively perform construction assembly work using reusable, preprogrammed skills such as grasping, drilling, and fastening. A central controller transforms the digital representation of the building into a construction relationship graph that represents construction entities, their states, and their parent-child relationships. Based on this representation, the system selects the next construction target, generates a symbolic sequence of skills for capable members of the robot team, and produces collision-free geometric motion plans for skill execution. The symbolic planning problem is dynamically regenerated as the construction state changes. An interactive digital twin presents the planned skill sequence and robot states to human co-workers for review and approval before execution. The method is evaluated through a construction assembly case study. By reducing the need to program robots separately for each task variation, the proposed approach supports more flexible deployment of collaborative robot teams in construction.

</details>

---

### [[20_Research/Papers/强化学习/Contact-Stable_Deformable_Tissue_Simulation_Using_Implicit_Integration_and_Live-Pose_Grasp_Constraints_for_Laparoscopic_Surgery_Robot_Policy|Contact-Stable Deformable Tissue Simulation Using Implicit Integration and Live-Pose Grasp Constraints for Laparoscopic Surgery Robot Policy Evaluation]]

![[assets/2609.25642_figure.png|800]]

- **arXiv**: [2609.25642](https://arxiv.org/abs/2609.25642)
- **PDF**: https://arxiv.org/pdf/2609.25642
- **详细分析**: [[20_Research/Papers/强化学习/Contact-Stable_Deformable_Tissue_Simulation_Using_Implicit_Integration_and_Live-Pose_Grasp_Constraints_for_Laparoscopic_Surgery_Robot_Policy|Contact-Stable Deformable Tissue Simulation Using Implicit Integration and Live-Pose Grasp Constraints for Laparoscopic Surgery Robot Policy Evaluation]]
- **作者**: Juahn Oh, Dongho Yee, Jinseok Lee, Jiyul Lee, Yechan Seo, Seong Jeong, Minsung Kim, Seonho Shim, Younghoon Noh, Hyuk Choi, Youngbin Kong, Hyoun-Joong Kon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Contact-Stable Deformable Tissue Simulation Using Implicit Integration and Live-Pose Grasp Constraints for Laparoscopic Surgery Robot Policy Evaluation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：LapGym, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Closed-loop evaluation of surgical robots requires tissue that deforms, can be grasped and lifted, and reproduces the anatomy in which the robot will operate. We present a simulator in which this tissue is reconstructed from a fixed-view RGB-D recording of the surgical field, composited to remove the instruments, closed into watertight volumes and tetrahedralised; the pipeline was applied unchanged to three specimens of two species (thirteen organs, 146,061 tetrahedra, no inverted elements). For one specimen, the organs are placed in a bimanual cell in which two Franka FR3 arms operate motorised instruments through 6 mm trocars. The core contribution is the numerical and contact design that keeps this cell stable: implicit integration, simulation meshes separate from collision meshes, numerical guards, and a grasp constraint captured at the live tissue pose. In 45 repeated grasp-lifts, a friction grasp held the tissue in 0 of 15 trials and each constraint grasp in 13 of 15; on displaced tissue, a rest-pose constraint produced one-step snaps of up to 17.8 mm, which live-pose capture eliminates. Against the recording, front-surface depth error is 1.33 to 1.41 mm, organ silhouette IoU is 0.80, and in five grasp-lifts reproduced from video the landmark displacement RMSE is 11.8 mm against 14.2 mm for a static prediction. Biofidelity is not claimed; the environment is intended for closed-loop feasibility, safety, contact and policy screening.

</details>

---

### [[20_Research/Papers/具身智能/RoboFollow_Unveiling_the_Instruction_Following_Mirage_in_Embodied_Agents|RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents]]

![[assets/2609.25636_figure.png|800]]

- **arXiv**: [2609.25636](https://arxiv.org/abs/2609.25636)
- **PDF**: https://arxiv.org/pdf/2609.25636
- **详细分析**: [[20_Research/Papers/具身智能/RoboFollow_Unveiling_the_Instruction_Following_Mirage_in_Embodied_Agents|RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents]]
- **作者**: Chang Guo, Yukun Xie, Bohan Tan, Zheng Chang, Zhaokai Yin, Qianli Ma, Yingqiao Wang, Chao Liang, Zhipeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《RoboFollow: Unveiling the Instruction Following Mirage in Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench, URL, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern embodied agents achieve impressive success rates, yet their actual instruction-following ability is far weaker than these numbers suggest. We trace this illusion to a structural property we term low scene entropy: when a visual scene admits only one valid task, language becomes redundant and a policy can score highly while barely using it. We introduce RoboFollow, a diagnostic benchmark with three principles: (1) High Scene Entropy: each training scene supports multiple kinematically distinct task branches, making vision alone insufficient and forcing reliance on language. (2) Hierarchical Diagnostic Protocol: a four-level protocol (L0--L3) progressively perturbs visual layout and semantics, probing whether equivalent instructions yield consistent behavior and distinct ones yield discriminable behavior across spatial relations, attributes, trajectory constraints, and logic. (3) Confound-Controlled Diagnosis: we simplify interaction objects, restrict actions to the trained repertoire and report stage-wise Intent and Execution scores, isolating comprehension from motor execution. Evaluation of nine VLA and WAM policies shows that strong L0 performance, where attained, does not reliably transfer to L1--L3 under our fine-tuning setup. Representative mitigations, including stronger VLM backbones, QA co-training, LangForce, and Classifier-Free Guidance, all fail to close this gap. RoboFollow exposes genuine instruction following as a critical, overlooked bottleneck. Code and dataset are available at this https URL and this https URL .

</details>

---

### [[20_Research/Papers/强化学习/DynaForge_Planning-Guided_Residual_Learning_for_Dynamic_Manipulation_Demonstration_Generation|DynaForge: Planning-Guided Residual Learning for Dynamic Manipulation Demonstration Generation]]

![[assets/2609.25631_figure.png|800]]

- **arXiv**: [2609.25631](https://arxiv.org/abs/2609.25631)
- **PDF**: https://arxiv.org/pdf/2609.25631
- **详细分析**: [[20_Research/Papers/强化学习/DynaForge_Planning-Guided_Residual_Learning_for_Dynamic_Manipulation_Demonstration_Generation|DynaForge: Planning-Guided Residual Learning for Dynamic Manipulation Demonstration Generation]]
- **作者**: Yiyang Jin, Yu Zheng, Xiao He, Hesheng Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.1（加权：具身智能 0.6，强化学习 0.2，机器人 0.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《DynaForge: Planning-Guided Residual Learning for Dynamic Manipulation Demonstration Generation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DICE-RL, DynamicVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic object manipulation is essential for robots operating in real-world environments, yet methods for generating high-quality demonstrations remain limited. Methods designed for static tasks do not readily transfer to dynamic settings. Among dynamic demonstration generators, planning-based methods can fail near contact, while DOMINO-style replay simplifies dynamic interactions and may limit the experience available for policy learning. We present DynaForge, a planning-guided framework that learns residual corrections for dynamic manipulation demonstration generation. DynaForge combines low-frequency global planning with high-frequency object-centric inverse kinematics across task phases, and applies a residual policy to correct actions during dynamic interaction. An implicit curriculum groups rollouts under matched conditions and selects mixed-success groups, focusing residual reinforcement learning on the evolving competence frontier. On Can and Bottle, it uses 0.73x as many optimizer steps as vanilla GRPO at the same nominal environment-step budget, with higher observed final success rates. Across nine simulation tasks, DynaForge increases mean demonstration-generation success from 41.30% of the planning prior to 78.37%. With 800 demonstrations per task, DP3 policies trained on DynaForge data achieve 49.11% mean success, compared with 7.07% for DOMINO data. On three real-world dynamic tasks, DynaForge-trained policies achieve 30-60% success, compared with 0-10% for DOMINO-trained policies, showing the ability of DynaForge for sim-to-real transfer.

</details>

---

### [[20_Research/Papers/强化学习/PAKT_Physically-Aligned_Kinesthetic_Teaching_for_Reinforcement_Learning|PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning]]

![[assets/2609.25630_figure.png|800]]

- **arXiv**: [2609.25630](https://arxiv.org/abs/2609.25630)
- **PDF**: https://arxiv.org/pdf/2609.25630
- **详细分析**: [[20_Research/Papers/强化学习/PAKT_Physically-Aligned_Kinesthetic_Teaching_for_Reinforcement_Learning|PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning]]
- **作者**: Lars Johannsmeier, Yashraj Narang
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《PAKT: Physically-Aligned Kinesthetic Teaching for Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HIL-SERL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world reinforcement learning (RL) systems still struggle with the demands of contact-rich industrial manipulation, including micrometer-level precision, success rates above 99%, and human-level cycle times. Although off-policy algorithms can improve performance by leveraging demonstrations and interventions, a key bottleneck is the lack of an intuitive interface for collecting such guidance while complying with constraints of the physical system and the policy. We propose PAKT, a framework for kinesthetic teaching in RL. As opposed to teleoperation approaches, PAKT relies on kinesthetic guidance, which is widely used in industry. However, a critical weakness of kinesthetic guidance is the possibility for the operator to move the robot along trajectories (e.g., velocities, accelerations, jerk) that the robot and/or policy cannot physically reproduce. Using PAKT, operators guide the robot through admittance control, which maps human-applied forces to motion. The downstream reference generator applies the same kinematic limits used during policy execution, keeping the collected trajectories within these limits. To support this teaching interface with an appropriate execution layer, PAKT adds a high-performance control stack that maps low-frequency RL actions to high-frequency torque commands. It consists of a reference generator and subsequent impedance controller, where the reference generator preserves the tracking performance of the impedance controller while improving contact handling and producing smoother policy actions. Across the reported runs on four insertion and industrial assembly benchmarks, including a data center compute tray, the end-to-end system reduces cycle time by 23%-48% and cumulative intervention count by 62%-86% relative to the HIL-SERL baseline. Project website: this https URL }{ this https URL

</details>

---

### [[20_Research/Papers/强化学习/From_Instrument-Mounted_Demonstrations_to_In-Vivo_Execution_Learning_Bimanual_Laparoscopic_Appendectomy_Without_Robot-Collected_Demonstratio|From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations]]

![[assets/2609.25625_figure.jpg|800]]

- **arXiv**: [2609.25625](https://arxiv.org/abs/2609.25625)
- **PDF**: https://arxiv.org/pdf/2609.25625
- **详细分析**: [[20_Research/Papers/强化学习/From_Instrument-Mounted_Demonstrations_to_In-Vivo_Execution_Learning_Bimanual_Laparoscopic_Appendectomy_Without_Robot-Collected_Demonstratio|From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations]]
- **作者**: Dongho Yee, Juahn Oh, Jinseok Lee, Jiyul Lee, Yechan Seo, Seong Jeong, Minsung Kim, Seonho Shim, Younghoon Noh, Hyuk Choi, Youngbin Kong, Kyu Eun Lee...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《From Instrument-Mounted Demonstrations to In-Vivo Execution: Learning Bimanual Laparoscopic Appendectomy Without Robot-Collected Demonstrations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most minimally invasive surgery is still performed with hand-held laparoscopic instruments, and the surgeon's instrument kinematics are lost when the operation ends; only the endoscope video is kept. This paper presents an end-to-end pipeline that captures this motion in the operating room and uses it to train a surgical robot policy, validated on live animals. We introduce a surgical instrument-state logger that mounts on the shaft of a standard laparoscopic instrument and recovers its pose and jaw state from an inertial sensor, a time-of-flight sensor and a Hall sensor, with no external camera or tracker. A data pipeline measures the latency of every sensor channel against a robot ground truth and aligns the channels before forming observation-action pairs. On these demonstrations we train a diffusion policy with a fine-tuned DINOv3 backbone, selecting its design by closed-loop rollouts in a physics simulator reconstructed from depth maps of an ex-vivo rabbit appendix. The policy is then retrained on 849 in-vivo demonstrations from four live rabbits and deployed on four additional live rabbits with electrosurgery armed. With the surgeon selecting the surgical phase, the policy completed the appendectomy in three of the four animals. The results show that demonstrations recorded from a surgeon's own instruments are sufficient to train, select and deploy a bimanual surgical policy in vivo. The robot serves only as the timing reference for sensor calibration and as the executor, and collects no demonstrations. Both demonstration corpora are released to support future surgical robot learning research.

</details>

---

### [[20_Research/Papers/机器人/Relative_Contact_Velocity-Controlled_Hand-Object_Mechanism_for_Dexterous_Tool_Manipulation|Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation]]

![[assets/2609.25619_figure.png|800]]

- **arXiv**: [2609.25619](https://arxiv.org/abs/2609.25619)
- **PDF**: https://arxiv.org/pdf/2609.25619
- **详细分析**: [[20_Research/Papers/机器人/Relative_Contact_Velocity-Controlled_Hand-Object_Mechanism_for_Dexterous_Tool_Manipulation|Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation]]
- **作者**: Sunyu Wang, Jean Oh, Nancy S. Pollard
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Relative Contact Velocity-Controlled Hand-Object Mechanism for Dexterous Tool Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work investigates how to enable general multi-finger robotic hands to perform the complete tool manipulation process, which entails picking up a tool, loading it into a suitable pose, and then wielding it. Inspired by human tool manipulation and mechanical design principles, we model the hand and the tool as a unified hand-object mechanism (HOM) composed of sub-assemblies. Specifically, we define a HOM as consisting of the hand, the object, and the generalized contact frames, allowing the HOM's motions to be expressed with the same set of Cartesian-space relative contact velocities, irrespective of the hand's kinematics and geometry. Then, we define a HOM's sub-assemblies as relative contact velocity and contact force constraints between fingers. Building on these definitions, we developed a lightweight and physically interpretable motion planning and contact estimation framework using least squares and a complementary filter. We evaluated our framework in simulation by teleoperating five different robotic hands. The results show that our framework enabled all five hands to execute the complete tool manipulation process, achieving dexterous behaviors even from identical, simple reference trajectories. Furthermore, the results showcase our framework's adaptability to different hands, tools, and tasks, enabled by its kinematic and geometric foundation.

</details>

---

### [[20_Research/Papers/具身智能/CableVLA_Simulation-Privileged_Global-Local_Representation_Learning_for_Cable_Routing|CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing]]

![[assets/2609.25606_figure.png|800]]

- **arXiv**: [2609.25606](https://arxiv.org/abs/2609.25606)
- **PDF**: https://arxiv.org/pdf/2609.25606
- **详细分析**: [[20_Research/Papers/具身智能/CableVLA_Simulation-Privileged_Global-Local_Representation_Learning_for_Cable_Routing|CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing]]
- **作者**: Zhifei Teng, Bo Feng, Xiang Zou, Jinpeng Xiao, Min Li, Zhouping Yin, Yiqun Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《CableVLA: Simulation-Privileged Global-Local Representation Learning for Cable Routing》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CableVLA, ForeTime-VLA, OpenVLA, Real-World, SmolVLA, TaF-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cable routing requires coordinated control of global cable topology and changing local contacts. We present CableVLA, an end-to-end multimodal vision-language-action framework that converts simulation-privileged supervision into deployable cable-topology and tactile representations. TopoHead distills node-level physics and current and future cable-topology information into causal visual context for the action expert. TacSense uses complementary frame and taxel branches to learn contact dynamics from resistive arrays, with simulator-derived kinematics and contact events providing supervision beyond the measured force map. A contact gate activates force-tactile residuals that refine the next 8 arm-and-gripper actions of a frozen topology-conditioned policy. Across 345 MuJoCo evaluations, CableVLA improves success from 62.6% for the $\pi_{0.5}$-V visual baseline to 84.9%. TacSense achieves pronounced gains in slip-transition recognition over a CNN-LSTM baseline with a similar parameter count, and this advantage persists under frozen-encoder probes. Topology prediction and 57-task tactile evaluations assess representation quality, while policy adaptation studies evaluate downstream control performance. Cross-simulator and real-robot comparisons further examine zero-shot policy transfer under changes in dynamics and sensing.

</details>

---

### [[20_Research/Papers/具身智能/RoboMP-DINOv2_Prompts,_Not_Filters_for_Robust_Robot_Manipulation|RoboMP-DINOv2: Prompts, Not Filters for Robust Robot Manipulation]]

![[assets/2609.25506_figure.png|800]]

- **arXiv**: [2609.25506](https://arxiv.org/abs/2609.25506)
- **PDF**: https://arxiv.org/pdf/2609.25506
- **详细分析**: [[20_Research/Papers/具身智能/RoboMP-DINOv2_Prompts,_Not_Filters_for_Robust_Robot_Manipulation|RoboMP-DINOv2: Prompts, Not Filters for Robust Robot Manipulation]]
- **作者**: Han Qi, Heng Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《RoboMP-DINOv2: Prompts, Not Filters for Robust Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation policies must generalize across visual shifts while preserving scene context relevant to action. General-purpose vision encoders are not tailored to visuomotor control, while object-centric approaches often use segmentation masks as hard filters that discard potentially useful context. We propose RoboMP-DINOv2 (Robotics Mask-Prompted DINOv2), a full-scene vision encoder that treats masks as spatial prompts rather than visibility filters. It extracts dense DINOv2 features from the full observation, injects learned region-specific embeddings at masked locations, and jointly contextualizes prompted and unprompted tokens for action prediction. We further introduce masked-region color randomization (MCR) to improve appearance robustness, yielding RoboMP-DINOv2-MCR. Across seven simulated manipulation settings, RoboMP-DINOv2 achieves 60.7% success under spatial shifts and 59.7% under scene clutter, compared with 50.7% and 41.0% for a DINOv2-based Diffusion Policy. Under unseen object colors, RoboMP-DINOv2-MCR achieves 72.5% success versus 35.1% for the strongest color-randomized baseline. Additional experiments and representation analyses show improved robustness while preserving behaviorally relevant scene information. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/Brace_Yourself_Task-Conditioned_Environmental_Bracing_for_Forceful_Humanoid_Manipulation|Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation]]

![[assets/2609.25486_first_page.png|800]]

- **arXiv**: [2609.25486](https://arxiv.org/abs/2609.25486)
- **PDF**: https://arxiv.org/pdf/2609.25486
- **详细分析**: [[20_Research/Papers/机器人/Brace_Yourself_Task-Conditioned_Environmental_Bracing_for_Forceful_Humanoid_Manipulation|Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation]]
- **作者**: Zongyuan Zhang, Christopher Lehnert, Will N. Browne, Jonathan M. Roberts
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forceful manipulation is challenging for humanoid robots because interaction forces can disturb whole-body balance. We introduce the Supporting Hand Strategy (SHS), which enables a humanoid to brace against the environment with one hand while performing forceful manipulation with the other. SHS optimises a task-conditioned support configuration that guides two synchronous reinforcement-learning policies, without human motion data or online whole-body trajectory planning. On a Unitree G1, SHS achieved usable contact forces up to 60 N, compared with a maximum sustained force of 13.5 N without environmental bracing, while substantially improving force tracking over a task-independent support configuration. The same policies generalised to different task regions without retraining. SHS therefore provides a simple mechanism for substantially extending humanoid forceful-manipulation capability.

</details>

---

### [[20_Research/Papers/机器人/A_bioinspired_internal_model-based_online_estimator_for_planar_pursuit|A bioinspired internal model-based online estimator for planar pursuit]]

![[assets/2609.25470_figure.png|800]]

- **arXiv**: [2609.25470](https://arxiv.org/abs/2609.25470)
- **PDF**: https://arxiv.org/pdf/2609.25470
- **详细分析**: [[20_Research/Papers/机器人/A_bioinspired_internal_model-based_online_estimator_for_planar_pursuit|A bioinspired internal model-based online estimator for planar pursuit]]
- **作者**: Tengyue Liu, Xincheng Li, Sofia Morales Ferreira, Kevin Galloway, Udit Halder
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《A bioinspired internal model-based online estimator for planar pursuit》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bioinspired feedback controls for pursuit, tracking, and collective motion are often expressed in terms of the relative configuration between interacting agents. In practice, however, onboard sensors may not directly provide all quantities required for feedback control, necessitating estimation of unobserved quantities. This paper develops a bioinspired internal model-based estimator for reconstructing those quantities from partial sensory observations and known self-motion. State reconstruction is posed as an optimization problem that treats the relative kinematics as constraints and minimizes the disagreement between the internal model outputs and measurements from onboard sensors. Pontryagin's Maximum Principle is used to derive the necessary optimality conditions. A forward-backward algorithm is used to provide a numerical solution and a moving horizon formulation is employed for online implementation. The estimator is evaluated numerically against classical state estimators. Real-time implementation of the proposed framework on robotic hardware is demonstrated through two pursuit strategies.

</details>

---

### [[20_Research/Papers/具身智能/REDACT_Robust_Perceptive_Locomotion_under_Unseen_Visual_Corruption|REDACT: Robust Perceptive Locomotion under Unseen Visual Corruption]]

![[assets/2609.25450_figure.png|800]]

- **arXiv**: [2609.25450](https://arxiv.org/abs/2609.25450)
- **PDF**: https://arxiv.org/pdf/2609.25450
- **详细分析**: [[20_Research/Papers/具身智能/REDACT_Robust_Perceptive_Locomotion_under_Unseen_Visual_Corruption|REDACT: Robust Perceptive Locomotion under Unseen Visual Corruption]]
- **作者**: Natapat Kirdwichai, Tobias Driskell-Poole, Andrei Sontea, Jadu Dash, Muhammad Burhan Hafez, Danesh Tarapore
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《REDACT: Robust Perceptive Locomotion under Unseen Visual Corruption》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ConvNet, RENet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Depth-conditioned locomotion policies have demonstrated impressive agile maneuvers, but can be steered to unpredictable actions when observations are outside their training distribution. Occlusion, invalid returns, sensor noise, and visual distractors can shift deployment observations away from nominal simulated depth. While synthetic sensor augmentation targets specified degradations, it does not by itself define behavior under corruption families omitted from training. To address gaps in training-time coverage, we present REDACT (Retaining Evidence Despite Artifacts for Continued Traversal), a teacher-student framework combining an improved visual encoder architecture, persistent feature masking, and a novel consensus-gating algorithm to retain useful depth information under unmodeled corruption. The gate uses approximate conformal calibration on clean observations alone, requiring no prior knowledge of the corruption type. Trained on clean simulated depth, REDACT retains useful visual information under unseen corruption, supporting higher traversal success than existing parkour baselines. Evaluation of depth augmentation across corruption families further shows that REDACT improves robustness where augmentation coverage is missing. Real-world trials demonstrate zero-shot transfer to structured and forested environments with unfamiliar scene content.

</details>

---

### [[20_Research/Papers/具身智能/Effects_of_Assistance_Delay_on_Joint_Mechanics_and_Energetics_in_Biological_Torque_Control_of_a_Hip_Exoskeleton|Effects of Assistance Delay on Joint Mechanics and Energetics in Biological Torque Control of a Hip Exoskeleton]]

![[assets/2609.25417_figure.png|800]]

- **arXiv**: [2609.25417](https://arxiv.org/abs/2609.25417)
- **PDF**: https://arxiv.org/pdf/2609.25417
- **详细分析**: [[20_Research/Papers/具身智能/Effects_of_Assistance_Delay_on_Joint_Mechanics_and_Energetics_in_Biological_Torque_Control_of_a_Hip_Exoskeleton|Effects of Assistance Delay on Joint Mechanics and Energetics in Biological Torque Control of a Hip Exoskeleton]]
- **作者**: Jimin An, Ryan Lee, Jingshu Peng, Eni Halilaj, Inseung Kang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Effects of Assistance Delay on Joint Mechanics and Energetics in Biological Torque Control of a Hip Exoskeleton》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biological torque control directly maps an estimated human joint moment to exoskeleton assistance, providing a task-agnostic strategy for supporting diverse locomotor activities. However, it remains unclear whether a fixed state-to-torque mapping provides effective assistance across biomechanically distinct tasks. We examined how assistance delay affected hip exoskeleton performance during level-ground (LG), ramp-ascent (RA), and ramp-descent (RD) walking. Eight participants completed a zero-torque baseline condition and five active assistance conditions with delays ranging from 40 to 320 ms. Across tasks and active delays, assistance reduced net metabolic rate by 5.24%, positive biological hip joint work by 5.86%, and total lower-limb positive joint work by 1.68% (all p &lt; 0.05). Assistance delay affected both joint-work outcomes (both p &lt; 0.001) but not net metabolic rate. Mechanical unloading generally decreased with increasing delay, whereas metabolic benefits remained comparatively stable. Relative to the zero-torque condition, net metabolic rate decreased by 9.75% during LG and 7.20% during RA but increased by 1.23% during RD. We did not detect task-dependent differences in the delay response. Our findings indicate that biological torque mappings should be evaluated based on the target outcome and mechanical role of the assisted joint, and that predominantly positive-power assistance may not generalize to negative-work-dominant locomotion without modification.

</details>

---

### [[20_Research/Papers/强化学习/Norm2Tex_Augmenting_Visuo-Tactile_Simulations_with_Texture|Norm2Tex: Augmenting Visuo-Tactile Simulations with Texture]]

![[assets/2609.25398_first_page.png|800]]

- **arXiv**: [2609.25398](https://arxiv.org/abs/2609.25398)
- **PDF**: https://arxiv.org/pdf/2609.25398
- **详细分析**: [[20_Research/Papers/强化学习/Norm2Tex_Augmenting_Visuo-Tactile_Simulations_with_Texture|Norm2Tex: Augmenting Visuo-Tactile Simulations with Texture]]
- **作者**: Seongjin Bien, Débora Oliveira Makowski, Roberto Calandra, Florian Walter, Wolfram Burgard
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Norm2Tex: Augmenting Visuo-Tactile Simulations with Texture》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale datasets are essential for training generalist robot control policies. Collecting real-world tactile data is costly and time-consuming, motivating the use of tactile simulations. However, current tactile simulators capture only overall contact geometry and miss fine details like texture. This results in a significant domain shift between simulated and real tactile data. To address this gap, we introduce Norm2Tex, a plug-in method that augments simulations of vision-based tactile sensors with high-frequency surface details from normal map textures. By modifying the target object's depth map before a tactile simulator's rendering pipeline, Norm2Tex seamlessly integrates into different tactile simulators. We also evaluate sim-to-real transfer using material classification and a reinforcement learning task. Our results show that Norm2Tex preserves material-dependent tactile information across domains, improving texture recognition and producing material-dependent control behavior in the real world.

</details>

---

### [[20_Research/Papers/具身智能/Capability-Aware_Arbitration_for_Semantic_Intent-Based_Shared_Control|Capability-Aware Arbitration for Semantic Intent-Based Shared Control]]

![[assets/2609.25369_figure.png|800]]

- **arXiv**: [2609.25369](https://arxiv.org/abs/2609.25369)
- **PDF**: https://arxiv.org/pdf/2609.25369
- **详细分析**: [[20_Research/Papers/具身智能/Capability-Aware_Arbitration_for_Semantic_Intent-Based_Shared_Control|Capability-Aware Arbitration for Semantic Intent-Based Shared Control]]
- **作者**: Zhaoda Du, Michael Bowman, Xiaoli Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Capability-Aware Arbitration for Semantic Intent-Based Shared Control》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VLM-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Shared control often allocates robot authority based on confidence in inferred human intent, assuming reliable autonomous execution. When this assumption fails, high intent confidence can cause over-helping. We present a capability-aware shared-control framework in which a vision-language model (VLM) infers human intent and provides semantic-intent confidence, while a vision-language-action (VLA) policy generates autonomous actions. VLA capability confidence is estimated online from the dispersion and local instability of stochastic action trajectories. We design a nonlinear arbitration policy that combines Bayesian-filtered semantic-intent confidence with VLA capability confidence through a sigmoid mapping to adapt robot authority. Our evaluation combined VLM/VLA confidence assessment with a study involving 12 participants performing pick-and-place and bidirectional stacking under in-distribution and out-of-distribution conditions. The proposed method achieved the highest task success rate (92%), compared with manual teleoperation (83%), intent-only arbitration (44%), and fixed equal-weight blending (10%). It also achieved higher control friendliness and lower authority-weighted disagreement than both shared-control baselines. These results demonstrate the benefit of incorporating VLA capability into authority allocation to mitigate over-helping and improve shared-control performance.

</details>

---

### [[20_Research/Papers/强化学习/HOTICE_Whole-Body_Humanoid_Object_Transportation_in_Cluttered_Environments|HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments]]

![[assets/2609.25363_figure.png|800]]

- **arXiv**: [2609.25363](https://arxiv.org/abs/2609.25363)
- **PDF**: https://arxiv.org/pdf/2609.25363
- **详细分析**: [[20_Research/Papers/强化学习/HOTICE_Whole-Body_Humanoid_Object_Transportation_in_Cluttered_Environments|HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments]]
- **作者**: Toan Nguyen, Weiduo Yuan, Siheng Zhao, Yue Wang, Daniel Seita
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.1（加权：具身智能 1.5，大模型 0.1，强化学习 0.2，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments, yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First, we introduce Humanoid-Object Decoupled Potential Fields, which jointly encode collision-avoidance guidance for the robot and the carried object, enabling coordinated, obstacle-aware motion for both. Second, to address the large action space inherent to whole-body loco-manipulation, we design a dual-agent reinforcement learning architecture that decouples upper- and lower-body control while preserving whole-body coordination via shared state observations and rewards. To train a policy that generalizes across diverse cluttered scenes, we further employ a specialist-to-generalist distillation strategy, in which privileged teacher policies are distilled into a single deployable student policy. We evaluate HOTICE in MuJoCo simulation and on a real Unitree G1 humanoid, demonstrating effective and robust object transportation across cluttered scenarios for objects of varying shapes. Our results show that HOTICE reliably coordinates whole-body motion and object-aware collision avoidance, generalizing effectively to previously unseen cluttered environments while achieving strong performance in sim2real deployment.

</details>

---

### [[20_Research/Papers/大模型/JAMB_Joint_Action-Motion_Diffusion_for_Bimanual_Manipulation|JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation]]

![[assets/2609.25322_figure.png|800]]

- **arXiv**: [2609.25322](https://arxiv.org/abs/2609.25322)
- **PDF**: https://arxiv.org/pdf/2609.25322
- **详细分析**: [[20_Research/Papers/大模型/JAMB_Joint_Action-Motion_Diffusion_for_Bimanual_Manipulation|JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation]]
- **作者**: Chuyang Xiao, Peilin Meng, David Held
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《JAMB: Joint Action-Motion Diffusion for Bimanual Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coordinated bimanual manipulation is challenging because the motion of either arm can alter the shared 3D scene and thereby affect the other arm. Yet most diffusion policies generate actions without explicitly modeling these future geometric consequences, while predictive variants typically use future state only as auxiliary supervision or fixed conditioning. We address this limitation by proposing JAMB, a diffusion policy that jointly denoises bimanual actions and future 3D point tracks. By allowing action and track hypotheses to evolve together within a shared Transformer, each can inform and refine the other throughout denoising. We further ground multimodal representations in a shared spatiotemporal coordinate system to facilitate geometry-aware interaction during joint denoising. We evaluate JAMB on diverse bimanual manipulation tasks in RoboTwin 2.0 and on a real-world robot, comparing it with action-only policies and alternative future-prediction approaches spanning different state representations and learning objectives. Across 16 simulation tasks, JAMB achieves an average success rate of 83.4%, outperforming the strongest baseline by 23.9 percentage points. On three real-world tasks, it outperforms the action-only and auxiliary geometry prediction methods by 50.0 and 21.2 percentage points, respectively. Beyond these performance gains, JAMB shows stronger generalization to cluttered scenes and out-of-distribution backgrounds than the evaluated baselines. Together, these results demonstrate the effectiveness of our joint action-motion modeling framework for coordinated bimanual manipulation. Our project website is available at this https URL

</details>

---

### [[20_Research/Papers/大模型/Learning_to_Plan_in_Human-Robot_Collaboration_Multimodal_Reinforcement_Learning_for_Adaptive_Interaction|Learning to Plan in Human-Robot Collaboration: Multimodal Reinforcement Learning for Adaptive Interaction]]

![[assets/2609.25274_figure.png|800]]

- **arXiv**: [2609.25274](https://arxiv.org/abs/2609.25274)
- **PDF**: https://arxiv.org/pdf/2609.25274
- **详细分析**: [[20_Research/Papers/大模型/Learning_to_Plan_in_Human-Robot_Collaboration_Multimodal_Reinforcement_Learning_for_Adaptive_Interaction|Learning to Plan in Human-Robot Collaboration: Multimodal Reinforcement Learning for Adaptive Interaction]]
- **作者**: Afagh Mehri Shervedani, Siyu Li, Natawut Monaikul, Bahareh Abbasi, Barbara Di Eugenio, Miloš Žefran
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 大模型, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.3，大模型 0.5，强化学习 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Learning to Plan in Human-Robot Collaboration: Multimodal Reinforcement Learning for Adaptive Interaction》归入 机器人、强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot assistants for older adults and people with disabilities need to perform collaborative tasks with users effectively. The core component of these systems is an interaction manager whose job is to observe and assess the task and infer the state of the human and their intent for the robot to choose the best course of action. Due to the sparseness of the data in this domain, the policy for such multimodal systems is often crafted by hand; as the complexity of interactions grows, this process is not scalable. This paper proposes a reinforcement learning (RL) approach to automatically generate the multimodal policy of the robot. Our system focuses on a realistic scenario where a robot assists a user in locating objects within a home environment, managing multimodal signals, including language and physical actions, to select the best action. In contrast to traditional dialog systems, our agent is trained with a simulator that uses human data and can deal with multiple modalities. We use a simple high-level reward function that needs no fine-tuning and enforce some preconditions to speed up the training process. A human study evaluating the system in a real-world setting demonstrates promising results, indicating high usability and effective task completion. This RL-based approach offers a scalable and interpretable alternative for designing interaction managers in multimodal human-robot collaborations.

</details>

---

### [[20_Research/Papers/强化学习/Towards_Adaptive_Interaction_Strategies_for_Human_Companion_Robot_via_Deep_Reinforcement_Learning|Towards Adaptive Interaction Strategies for Human Companion Robot via Deep Reinforcement Learning]]

![[assets/2609.25031_figure.png|800]]

- **arXiv**: [2609.25031](https://arxiv.org/abs/2609.25031)
- **PDF**: https://arxiv.org/pdf/2609.25031
- **详细分析**: [[20_Research/Papers/强化学习/Towards_Adaptive_Interaction_Strategies_for_Human_Companion_Robot_via_Deep_Reinforcement_Learning|Towards Adaptive Interaction Strategies for Human Companion Robot via Deep Reinforcement Learning]]
- **作者**: Cong-Thanh Vu, Yen-Chen Liu
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 2.8（加权：具身智能 0.3，强化学习 1.4，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Towards Adaptive Interaction Strategies for Human Companion Robot via Deep Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Deep-RL, LSTM-DRL, MCTS-DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the field of Human-Robot Interaction (HRI), achieving flexibility in human-accompanying within real-world environments holds great potential for various applications but also poses significant challenges. Traditional methods typically restrict robots to fixed positions relative to humans, such as tracking from behind, in front, or side-by-side, which limits robot adaptability in dynamic workspaces. This study introduces a novel human-companioning strategy that uses Reinforcement Learning (DRL) to enable mobile robots to dynamically adjust their tracking positions according to varying conditions. An interaction space is defined to capture the relationship between the human and the robot while considering the environment, which serves as the basis for state spaces in DRL to assist the robot in adapting to environmental changes. A human-robot companion controller is developed by integrating Model Predictive Path Integral (MPPI) control with Control Barrier Functions (CBF), ensuring that the robot accurately follows the target's movement in both position and orientation while avoiding obstacles and enhancing social acceptance and safety. The proposed approach is evaluated in real-world scenarios, both indoors and outdoors, and compared with other studies. The results show that the proposed method improves the success rate and tracking accuracy by at least 24% and 47%, respectively, while enhancing human comfort. Experiments demonstrate the robot's ability to flexibly accompany a person walking at speeds of up to 1.7 m/s, dynamically adjusting its strategy without being confined to a fixed position. Additionally, the robot respects the human's intimate space to ensure safety, comfort, and effective obstacle avoidance.

</details>

---
