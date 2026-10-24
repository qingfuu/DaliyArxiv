# cs.CV | Computer Vision and Pattern Recognition | 2026-10-23

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/具身智能/Sensorimotor_Alignment_A_Platonic_Proxy_for_Embodied_Policy_Success|Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success]]

![[assets/2610.31670_figure.png|800]]

- **arXiv**: [2610.31670](https://arxiv.org/abs/2610.31670)
- **PDF**: https://arxiv.org/pdf/2610.31670
- **详细分析**: [[20_Research/Papers/具身智能/Sensorimotor_Alignment_A_Platonic_Proxy_for_Embodied_Policy_Success|Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success]]
- **作者**: Yunfei Xie, Howard H. Qian, Shiyi Lan, Kaiyu Hang, Chen Wei
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.8，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Sensorimotor Alignment: A Platonic Proxy for Embodied Policy Success》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VLM4VLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic foundation models are typically evaluated through costly closed-loop rollouts, which motivates cheap offline proxies for model capability. The Platonic Representation Hypothesis (PRH) suggests that as representations improve, different modalities such as vision and language converge toward a shared statistical model of reality. We ask whether motion trajectories form another such modality: as embodied models become more capable, should their sensory representations converge toward the structure of physical motion? To examine this, we propose Sensorimotor Alignment ($S^2$), a training-free offline metric that measures how well a model's sensory representation aligns with the geometry of physical motion. We find that $S^2$ correlates positively with downstream robot task success across embodied model families, making it a low-cost offline proxy for prioritizing models before closed-loop evaluation. $S^2$ can also identify promising vision-language model (VLM) backbones even before costly fine-tuning into vision-language-action models (VLAs). Beyond this correlation, $S^2$ offers representation-level explanations for phenomena observed in VLAs and world action models (WAMs). With $S^2$, we extend PRH to embodied models and make sensorimotor alignment empirically measurable, offering insight into why an embodied model succeeds beyond its closed-loop success rate.

</details>

---

### [[20_Research/Papers/具身智能/A_Sparse_Topometric_Graph_for_Scalable_Cross-Session_Indoor_Navigation|A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation]]

![[assets/2610.31432_figure.png|800]]

- **arXiv**: [2610.31432](https://arxiv.org/abs/2610.31432)
- **PDF**: https://arxiv.org/pdf/2610.31432
- **详细分析**: [[20_Research/Papers/具身智能/A_Sparse_Topometric_Graph_for_Scalable_Cross-Session_Indoor_Navigation|A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation]]
- **作者**: Eun Sun Lee, Minkyun Seo, Gwangtak Bae, Junho Kim, Seunggu Kang, Jaesik Park, Young Min Kim
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《A Sparse Topometric Graph for Scalable Cross-Session Indoor Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A conventional embodied agent in an indoor environment builds a map by accumulating noisy real-world measurements and results from heavy inference to guide navigation. While the detailed measurements may differ due to scene changes or sensor settings, the unique topological structure of navigable passages or the connectivity between rooms may provide training-free guidance that complements local observations. We propose a sparse topometric graph as an efficient structural representation for robust indoor navigation, alleviating the need for fine-grained matching, which is computationally expensive, memory-intensive, and prone to real-world variations. The map consists of nodes that encode local 3D geometry and distance-weighted edges that capture traversable connectivity. A learned graph-matching network finds consistent subgraph structures across sessions by considering both node-level geometric descriptors and neighborhood connectivity. The holistic contextual matching is robust to local ambiguities caused by weak distinctiveness or repetitive structure, and establishes stable correspondences despite local scene changes, different sensor modalities, or limited spatial overlap. We analyze the practicality of the graph through cross-session point-goal navigation, where a goal specified in a prior reference map must be reached from an unknown initial pose in a later session. Experiments show that our method achieves the highest success rates (77.1% on Gibson and 40.0% under 3D-FRONT scene changes), while reducing memory by more than two orders of magnitude compared to point-level representations. The proposed approach further supports cross-session alignment and goal-directed navigation with strong scalability and robust real-world transfer.

</details>

---

### [[20_Research/Papers/世界模型/Inside-JEPA_From_Prediction_to_Relational_Grounding_in_Latent_World_Models|Inside-JEPA: From Prediction to Relational Grounding in Latent World Models]]

![[assets/2610.31194_figure.png|800]]

- **arXiv**: [2610.31194](https://arxiv.org/abs/2610.31194)
- **PDF**: https://arxiv.org/pdf/2610.31194
- **详细分析**: [[20_Research/Papers/世界模型/Inside-JEPA_From_Prediction_to_Relational_Grounding_in_Latent_World_Models|Inside-JEPA: From Prediction to Relational Grounding in Latent World Models]]
- **作者**: Hossein Resani, Javen Qinfeng Shi
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Inside-JEPA: From Prediction to Relational Grounding in Latent World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-embedding predictive architectures (JEPAs) learn world models in latent space, enabling efficient planning but leaving their states opaque. We introduce Inside-JEPA, which places relational channels for ordered entity pairs inside the JEPA latent state and shows that an inverse-dynamics loss can ground these channels without relation labels when its head reads them, either alone or as part of the full state. On Something-Something V2, latent prediction alone performs no better than a random relation head, while inverse-dynamics supervision that recovers actions from channel changes improves relational AUROC by .065-.103 across ten settings with annotated boxes, by .081 on RH20T robot episodes with held-out tasks, and by .050-.061 across five relations using off-the-shelf detection and tracking. An inverse head on entity latents decodes actions more accurately but barely improves relational grounding; shuffled labels, two label-free objectives, and action labels on only 5% of the pairs also fail to ground the channels. Given an action, predicted relational changes approach the quality of observed future relations (AUROC .599 vs .621). For one-step relational goals, a supervised readout of the 16 channels ranks the correct action among the top five of 65 in 43% of cases, compared with 24% for prediction-only latents and 17% for a frequency prior.

</details>

---

### [[20_Research/Papers/具身智能/Memory_before_Goal_Role_of_Pre-History_Memory_for_Humanoid_Loco-Manipulation|Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation]]

![[assets/2610.31166_figure.png|800]]

- **arXiv**: [2610.31166](https://arxiv.org/abs/2610.31166)
- **PDF**: https://arxiv.org/pdf/2610.31166
- **详细分析**: [[20_Research/Papers/具身智能/Memory_before_Goal_Role_of_Pre-History_Memory_for_Humanoid_Loco-Manipulation|Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation]]
- **作者**: Chenyuan Chen, Ran Ding, Lechen Zhang, Zewen He, Yoshihiko Nakamura
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EgoVLA, InternVLA, MemoryBench, POT-VLA, Real-World, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

</details>

---

### [[20_Research/Papers/具身智能/HiSTEVE_1.0_Harnessing_Human-Interface_VLA_Agents_for_Open-World_Games|HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games]]

![[assets/2610.31162_figure.png|800]]

- **arXiv**: [2610.31162](https://arxiv.org/abs/2610.31162)
- **PDF**: https://arxiv.org/pdf/2610.31162
- **详细分析**: [[20_Research/Papers/具身智能/HiSTEVE_1.0_Harnessing_Human-Interface_VLA_Agents_for_Open-World_Games|HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games]]
- **作者**: Zecong Tang, Zian Guan, Yuncheng Guo, Zhanqiu Zhang, Yiwen Guo, Bo Dai
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.6，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《HiSTEVE 1.0: Harnessing Human-Interface VLA Agents for Open-World Games》归入 具身智能、大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongBench, Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building virtual embodied agents that operate in open-ended games like human players is a long-standing goal requiring both long-horizon autonomy and reliable native-interface control. As a procedurally generated open world, Minecraft provides a natural testbed for studying the integration of these capabilities. Existing agents typically provide either native visuomotor control without long-horizon autonomy or high-level planning executed through environment APIs or predefined skills. To bridge this gap, we propose HiSTEVE, a hierarchical VLA agent with a capability-aware agent harness. At the orchestration level, we equip the harness with structured memory for tracking progress and a VLM planner for selecting subtasks within the VLA's capabilities. To reliably determine subtask completion, we further introduce a policy-coupled task completion state detector that conditions on VLA policy context to signal candidate completion. At the control level, a single VLA executes all subtasks with vision-only perception and native keyboard-and-mouse actions. To mitigate interference between heterogeneous GUI and non-GUI interactions, we introduce regime-specific RMSNorm branches and separate mouse-movement token embeddings. We also train the VLA through world knowledge injection, imitation learning, and reinforcement learning with environment feedback to improve reliability and recovery. HiSTEVE achieves state-of-the-art atomic-task performance, scoring 85.0% on MineStudio Bench and a 37.4% average success rate on OpenHA, while also completing long-horizon tasks such as crafting an iron pickaxe from scratch like human players.

</details>

---

### [[20_Research/Papers/具身智能/Navigating_human-robot_interaction_challenges_in_private_and_residential_aged_care_homes|Navigating human-robot interaction challenges in private and residential aged care homes]]

![[assets/2610.31149_figure.png|800]]

- **arXiv**: [2610.31149](https://arxiv.org/abs/2610.31149)
- **PDF**: https://arxiv.org/pdf/2610.31149
- **详细分析**: [[20_Research/Papers/具身智能/Navigating_human-robot_interaction_challenges_in_private_and_residential_aged_care_homes|Navigating human-robot interaction challenges in private and residential aged care homes]]
- **作者**: David Ahmedt-Aristizabal, Mohammad Ali Armin, Akila Pemasiri, Harshala Gammulle, Tharindu Fernando, David Silvera-Tawil, Simon Denman
- **cs 子类**: cs.CV, cs.HC, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Security

#### 研究背景与动机

《Navigating human-robot interaction challenges in private and residential aged care homes》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This chapter explores how robotic systems and ambient intelligence can enhance care for older adults in residential aged care (RAC) homes and private homes. Although these settings differ, we frame both as extreme and challenging environments for human-robot interaction (HRI), characterised by cluttered and dynamic layouts, diverse resident needs, and limited on-site technical support. We review embodied and non-embodied systems that assist with daily living, safety monitoring, and social engagement, highlighting hybrid deployments where robots complement fixed and wearable sensors. To ensure these technologies are usable and effective, design considerations consider the cognitive, physical, and social needs of older adults. Interaction design prioritises accessibility for older adults with low digital literacy, using robust but simple voice interfaces, small sets of non-verbal cues, accessible screen-based companions, and safe object handovers. Privacy, trust, and acceptability are addressed via practical strategies such as on-device inference, data minimisation, visible consent controls, and transparent data handling aligned with emerging artificial intelligence (AI) and privacy regulation. Evaluation emphasises real-world metrics including false alarms per day, time to recover from faults, staff workload, and long-term system reliability. We close by outlining open research challenges and future directions for scalable, regulation-ready deployments that support aging with dignity, safety, and independence.

</details>

---

### [[20_Research/Papers/具身智能/Revisiting_Distribution_Matching_for_State-to-Vision_Policy_Distillation_in_Laparoscopic_Robotic_Manipulation|Revisiting Distribution Matching for State-to-Vision Policy Distillation in Laparoscopic Robotic Manipulation]]

![[assets/2610.31010_figure.png|800]]

- **arXiv**: [2610.31010](https://arxiv.org/abs/2610.31010)
- **PDF**: https://arxiv.org/pdf/2610.31010
- **详细分析**: [[20_Research/Papers/具身智能/Revisiting_Distribution_Matching_for_State-to-Vision_Policy_Distillation_in_Laparoscopic_Robotic_Manipulation|Revisiting Distribution Matching for State-to-Vision Policy Distillation in Laparoscopic Robotic Manipulation]]
- **作者**: Mingyu Sheng, Jianan Fan, Dongnan Liu, Guoyan Zheng, Ron Kikinis, Weidong Cai
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Revisiting Distribution Matching for State-to-Vision Policy Distillation in Laparoscopic Robotic Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end control policies trained via Reinforcement Learning (RL) have emerged as an alternative to conventional surgical robotic control approaches, with recent studies exploring state-based policies trained on privileged state observations. However, such approaches rely on precise physical states that are difficult to obtain reliably in surgical environments. Vision-based RL provides an alternative by learning manipulation policies directly from RGB observations, avoiding explicit state estimation and manually engineered perception pipelines while enabling policies to acquire task-relevant visual representations. Nevertheless, obtaining vision-based policies via pure RL methods for surgical manipulation remains challenging. Thus, imitation learning (IL) becomes another solution, yet it requires a large number of expert demonstrations, which are difficult to obtain in minimally invasive surgery. In this work, we propose a framework for state-to-vision policy distillation in laparoscopic robotic manipulation. Specifically, a state-based policy with privileged observations is employed as the teacher, and a vision-based policy learns from RGB observations and robot proprioceptive information, which requires less expert demonstrations than IL and introduces superior performance than RL methods. We conduct extensive experiments on various surgical manipulation tasks in the simulated environment. Experimental results show that, in the context of laparoscopic robotic manipulation, training vision-based policies with general-purpose RL methods is challenging, whereas our proposed state-to-vision policy distillation leads to more consistent and stable performance across tasks.

</details>

---

### [[20_Research/Papers/具身智能/DRILL_Training_World_Models_to_Improve_Policies,_Not_Predict_Pixels|DRILL: Training World Models to Improve Policies, Not Predict Pixels]]

![[assets/2610.30814_figure.png|800]]

- **arXiv**: [2610.30814](https://arxiv.org/abs/2610.30814)
- **PDF**: https://arxiv.org/pdf/2610.30814
- **详细分析**: [[20_Research/Papers/具身智能/DRILL_Training_World_Models_to_Improve_Policies,_Not_Predict_Pixels|DRILL: Training World Models to Improve Policies, Not Predict Pixels]]
- **作者**: Zhaolu Kang, Tailong Luo, Lei Wei, Guangyuan Dong, Sihan Liu, Yingjie He, Siheng Wang, Shuaibo Li, Rongchao Zhang, Zhen Tian, Richeng Xuan, Zhichao Hu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.6，强化学习 0.2，世界模型 1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DRILL: Training World Models to Improve Policies, Not Predict Pixels》归入 世界模型、具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, OpenVLA, RLVR-World, SC-VLA, World4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are increasingly used to reduce environment interaction when post-training vision-language-action (VLA) policies with reinforcement learning. Yet they are typically trained to predict pixels one step ahead, even though their role here is not merely to render visually faithful videos but to produce learning signals from imagined rollouts that improve the policy. We show that this mismatch is substantial: lower pixel MSE can produce worse policy gradients, and a world model trained for policy utility can yield better downstream policies despite 17% higher pixel MSE on the next frame. We propose the Downstream-Return Imagination Learning Loop (DRILL), a bilevel framework that updates the world model to maximize the policy's return after an inner GRPO update on imagined rollouts. DRILL has two instantiations. DRILL-VWI is a closed-form surrogate, requiring no additional simulator rollouts, that reweights prediction errors by policy visitation, the group-relative GRPO advantage, and model confidence. DRILL-IMG is a full meta-gradient method that differentiates through the inner update using truncated Hessian-vector products. We show that DRILL-VWI recovers the local one-step component of the DRILL-IMG meta-gradient under score-compatibility and small-residual assumptions. Across five manipulation simulators and two VLA backbones, DRILL-IMG raises mean success rate by 13.1 points over WMPO and 7.9 points over RLVR-World, and complements RLVR pretraining rather than competing with it. More broadly, we believe video world models for VLA reinforcement learning can be productively trained by the policy gradients they produce, not only by pixel-level prediction.

</details>

---

### [[20_Research/Papers/世界模型/DeXplicit_Making_Physical_State_Explicit_in_Dexterous_Manipulation_World_Models|DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models]]

![[assets/2610.30781_figure.png|800]]

- **arXiv**: [2610.30781](https://arxiv.org/abs/2610.30781)
- **PDF**: https://arxiv.org/pdf/2610.30781
- **详细分析**: [[20_Research/Papers/世界模型/DeXplicit_Making_Physical_State_Explicit_in_Dexterous_Manipulation_World_Models|DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models]]
- **作者**: Adam Lee, Mutian Xu, Yukang Cao, Shulin Tian, Ziwei Liu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.2，世界模型 0.8，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《DeXplicit: Making Physical State Explicit in Dexterous Manipulation World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ControlNet, Ctrl-World, EgoSim, Hand2World, HandsOnWorld, IRASim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Before acting on an object, a robot needs to anticipate how its hand motion will change the physical world and what the resulting scene will look like. Existing approaches typically entangle action-conditioned dynamics, camera motion, and visual synthesis within a video generation model, or represent dynamics as point trajectories without explicit object structure. We introduce DeXplicit, a dexterous manipulation world model that instead predicts how the world evolves explicitly in metric 3D before rendering its visual consequences. Given an initial scene and a future hand trajectory, a lightweight 3D dynamics network predicts object-centric motion and deformation, providing structured and geometrically grounded future world states. These predictions then serve as a strong scaffold for video generation: appearance is transported through the predicted 3D motion and projected into future views, allowing the renderer to focus on completing uncertain and newly visible content rather than implicitly learning world dynamics from pixels. This explicit-3D-first decomposition also enables efficient causal generation, requiring only two denoising steps per block while conditioning on generated history. Across HOT3D, OakInk2, and PhysTwin, DeXplicit reduces moved-point error by 27-40% relative to PointWorld and improves object fidelity IoU+ by 47% on HOT3D under a shared renderer. Our design with two-step causal generation achieves a 57x speedup from our 14B bi-directional configuration in video synthesis.

</details>

---

### [[20_Research/Papers/具身智能/Evaluation_of_Front-End_Feature_Matching_for_Lunar_Visual_SLAM|Evaluation of Front-End Feature Matching for Lunar Visual SLAM]]

![[assets/2610.30774_figure.png|800]]

- **arXiv**: [2610.30774](https://arxiv.org/abs/2610.30774)
- **PDF**: https://arxiv.org/pdf/2610.30774
- **详细分析**: [[20_Research/Papers/具身智能/Evaluation_of_Front-End_Feature_Matching_for_Lunar_Visual_SLAM|Evaluation of Front-End Feature Matching for Lunar Visual SLAM]]
- **作者**: Guillem Casadesus Vila, Grace Gao
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《Evaluation of Front-End Feature Matching for Lunar Visual SLAM》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：D2-Net, LunaNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lunar rovers will primarily rely on cameras for localization until navigation satellite services are deployed, and will continue to need them afterwards for relative navigation, hazard detection, and surface operations. Visual odometry (VO) and Simultaneous Localization and Mapping (SLAM) mostly estimate motion by matching features between frames. However, feature matchers are developed on urban, indoor and driving scenes, planetary studies compare them on orbital registration or within complete SLAM systems, and real lunar imagery with reference poses is scarce, so matching between rover frames on low-texture, harshly lit terrain, and its effect on VO, has not been compared. We benchmark eleven classical and learned detector-matcher combinations on nine synthetic, lunar-testbed, and terrestrial-analogue datasets, and a feature tracker, scoring pairwise pose accuracy against baseline and the trajectory error of the resulting VO. Under a common rotation-only metric, the SuperPoint pairings outperform SIFT with ratio-tested FLANN matching on both lunar testbeds and one analogue site, with smaller or unresolved differences on synthetic data. When rotation and translation direction are scored jointly, this SIFT pairing exceeds both SuperPoint pairings on four synthetic datasets, so synthetic results alone do not establish relative performance on real rover imagery. In stereo VO, the SuperPoint pairings are not consistently more accurate than SIFT, but only they keep tracking on all eight sequential datasets. Pairings with classical detectors depend on lighting while SuperPoint changes little: a low spotlight makes them more accurate than diffuse light on the same testbed views, consistent with more contrast and detected keypoints. SuperPoint with LightGlue is the fastest learned combination (16 ms per frame), and DINOv2 retrieval proposals still need geometric verification.

</details>

---

### [[20_Research/Papers/具身智能/SmolVLA-MoE_Sparse_Mixture-of-Experts_for_Efficient_Multi-Task_Robotic_Manipulation|SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation]]

![[assets/2610.30732_figure.png|800]]

- **arXiv**: [2610.30732](https://arxiv.org/abs/2610.30732)
- **PDF**: https://arxiv.org/pdf/2610.30732
- **详细分析**: [[20_Research/Papers/具身智能/SmolVLA-MoE_Sparse_Mixture-of-Experts_for_Efficient_Multi-Task_Robotic_Manipulation|SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation]]
- **作者**: Shiyang Zhang, Miao Yang, Zhengda Li, Yang Shao, Ruifang Zhai, Hui Peng, Peng Song
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.8，大模型 0.1，机器人 0.8）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《SmolVLA-MoE: Sparse Mixture-of-Experts for Efficient Multi-Task Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown promising results in multi-task robotic manipulation by leveraging visual and language understanding for action generation. However, existing lightweight VLA models employ a single dense action expert to handle all tasks, which limits their multi-task capability under constrained computational budgets. To address this issue, we propose SmolVLA-MoE, a novel framework that introduces sparse Mixture-of-Experts (MoE) into the FFN layers of the action expert in VLA models. SmolVLA-MoE replaces dense FFN layers with multiple parallel expert FFNs and a token-level router, enabling each token to adaptively select the most suitable expert for action generation. We further introduce a shared expert with a tunable weight parameter to balance the inheritance of pre-trained capabilities and task-specific expert specialization. Through sparse activation, SmolVLA-MoE activates only a single expert FFN during inference, with a total activated parameter count of approximately 500M including the frozen VLM backbone, while benefiting from approximately 800M total stored parameters. We evaluate our method on four task suites of the LIBERO benchmark. SmolVLA-MoE achieves an average success rate of 84.25%, outperforming SmolVLA (82.75%) and OpenVLA-7B (76.5%), while maintaining comparable inference efficiency. Our code is publicly available at https://github.com/dudu435/smolvla-moe.

</details>

---

### [[20_Research/Papers/具身智能/KinoUAV_A_Benchmark_for_Safe_and_Stable_UAV_Vision-Language_Navigation_with_Kinodynamic_Modeling|KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling]]

![[assets/2610.30609_figure.png|800]]

- **arXiv**: [2610.30609](https://arxiv.org/abs/2610.30609)
- **PDF**: https://arxiv.org/pdf/2610.30609
- **详细分析**: [[20_Research/Papers/具身智能/KinoUAV_A_Benchmark_for_Safe_and_Stable_UAV_Vision-Language_Navigation_with_Kinodynamic_Modeling|KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling]]
- **作者**: Chenyao Yang, Peijin Wang, Yingchao Feng, Wenhui Diao
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，机器人 0.8）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《KinoUAV: A Benchmark for Safe and Stable UAV Vision-Language Navigation with Kinodynamic Modeling》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicles (UAVs) have recently emerged as important remote sensing platforms, and UAV navigation has shown great potential in remote sensing applications. However, existing methods do not explicitly incorporate kinodynamic modeling or safety distances into trajectory generation, resulting in high absolute yaw rates, frequent collisions, and low navigation success rates, which limit safety and motion stability. To address this challenge, we introduce KinoUAV, a kinodynamic benchmark comprising a dataset and KinoUAV-Agent. First, we develop a hierarchical kinodynamic trajectory generation pipeline that drives UAV through acceleration actions. It uses waypoint chains from global planning and generates trajectories segment by segment under velocity, acceleration, and jerk constraints, reducing oscillations and improving trajectory stability. Furthermore, we introduce directional free-space distance (DFD) labels into the constructed dataset to describe the available clearance for safe motion decisions. The proposed KinoUAV-Agent predicts DFDs and uses them to generate safe actions, decoupling perception from action decision-making. This design enables autonomous obstacle avoidance and improves navigation safety. The benchmark incorporates the proposed Cruise-Seek task, in which the UAV first enters the target region and then searches for the target, reducing the difficulty of target search and improving navigation success. Experiments on KinoUAV show that KinoUAV-Agent outperforms existing methods, achieving the highest success rate while maintaining lower absolute yaw rates and collision rates. These results demonstrate the effectiveness of kinodynamic modeling for safe and stable UAV navigation.

</details>

---

### [[20_Research/Papers/世界模型/Self-Distilling_Future_Video_Representations_for_World_Action_Models|Self-Distilling Future Video Representations for World Action Models]]

![[assets/2610.30320_figure.png|800]]

- **arXiv**: [2610.30320](https://arxiv.org/abs/2610.30320)
- **PDF**: https://arxiv.org/pdf/2610.30320
- **详细分析**: [[20_Research/Papers/世界模型/Self-Distilling_Future_Video_Representations_for_World_Action_Models|Self-Distilling Future Video Representations for World Action Models]]
- **作者**: Huiwon Jang, Suhyeok Jang, Hyeonmo Kang, Seungku Kim, Jinwoo Shin, Sihyun Yu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Self-Distilling Future Video Representations for World Action Models》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) have emerged as a promising approach to learning generalist robot policies using rich spatiotemporal priors from pre-trained video diffusion models. A recent line of WAMs improves inference efficiency by conditioning a separate action decoder on intermediate future video representations extracted from a single denoising step, avoiding costly iterative denoising required for video generation. This design makes action prediction depend directly on the quality of these future representations. In this paper, we introduce Future REpresentation learning via self-Distillation with temporal context (FRED), a framework that trains WAMs to improve the quality of future video representations from noise in a single denoising step. Specifically, FRED uses self-distillation to predict future representations from noise, using representations extracted from ground-truth future observations as targets. We further condition the video model on historical observations, providing temporal context for predicting future representations better. Across diverse real-world manipulation scenarios, FRED consistently outperforms competing WAMs. It achieves particularly large gains on long-horizon and out-of-domain tasks under zero-shot environment generalization, and substantially improves human-to-robot skill transfer, reaching 50.0% task success on tasks absent from robot training data and demonstrated only in human videos, compared with 19.4% for the best competing WAM.

</details>

---
