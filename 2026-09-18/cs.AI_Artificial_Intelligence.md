# cs.AI | Artificial Intelligence | 2026-09-18

#arxiv #ComputerScience

**论文数**: 20

### [[20_Research/Papers/具身智能/Coding_Agents_with_an_Obstacle-Aware_Harness_for_Safe_Robot_Manipulation|Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation]]

![[assets/2609.20822_figure.png|800]]

- **arXiv**: [2609.20822](https://arxiv.org/abs/2609.20822)
- **PDF**: https://arxiv.org/pdf/2609.20822
- **详细分析**: [[20_Research/Papers/具身智能/Coding_Agents_with_an_Obstacle-Aware_Harness_for_Safe_Robot_Manipulation|Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation]]
- **作者**: Bingxin Xu, Yuzhang Shang, Zhen Dong, Emilio Ferrara
- **cs 子类**: cs.AI, cs.CL, cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.35（加权：具身智能 1.5，大模型 0.75，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SafeLIBERO, URL, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents have emerged as a promising paradigm for robot manipulation: a language model writes the robot controller as a program, and agents built in this way now operate robots without robot-specific this http URL this paradigm is also safe, however, has not been asked. We evaluate coding agent under a safety constraint, where each task pairs a manipulation goal with an obstacle the robot must not touch. The agent pursues the goal but collides with the obstacle in most cases, treating task completion as its sole objective while neglecting safety. The agent reasons about the obstacle in its traces, and the prompt already forbids touching it, so neither perception nor instruction is at fault; the fault lies in the planning, where the stated constraint never becomes a priority. By decomposing manipulation into a route phase and a contact-rich moment, we locate the source of the failure. Along the route, the model cannot prioritize the safety constraint, having no notion of a clearing route and none of replanning once a chosen route becomes infeasible. At the contact, it is unaware that contact execution is bounded by the same constraint. To close this gap, we present SafeHarness, which equips the model with two obstacle-aware harnesses that enable it to prioritize the safety constraint. Obstacle-aware route planning grounds the objects as bounding boxes and draws candidate routes over them as sequences of waypoints. The agent then plans a route in advance, verifies it, replans when necessary, and only then executes it. Obstacle-aware contact execution instead selects the contact position so that the contact itself avoids the obstacle. SafeHarness attains 71.9% task success and 87.5% collision avoidance, surpassing the previous SOTA by 6.5% and 27.0%, respectively. These results are $2.3\times$ and $1.5\times$ those of the same agent without harnesses.

</details>

---

### [[20_Research/Papers/具身智能/Workspace_Models_Lightweight_Robotic_Memory_via_Saliency-Driven_Supervision|Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision]]

![[assets/2609.20820_figure.png|800]]

- **arXiv**: [2609.20820](https://arxiv.org/abs/2609.20820)
- **PDF**: https://arxiv.org/pdf/2609.20820
- **详细分析**: [[20_Research/Papers/具身智能/Workspace_Models_Lightweight_Robotic_Memory_via_Saliency-Driven_Supervision|Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision]]
- **作者**: Nitish Dashora, Douglas Chen, Idan Shenfeld, John Marangola, Pulkit Agrawal, Max Simchowitz
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Workspace Models: Lightweight Robotic Memory via Saliency-Driven Supervision》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Complex robotic manipulation tasks frequently require a long-term memory of past events and actions. As conditioning on full histories renders policies prone to spurious correlations and degrades performance, many approaches to policy memory involve compressing historical information through expensive VLM queries in-the-loop to process only task-salient information. In this paper, we propose an alternative approach in which computationally intensive VLM queries are made during train-time to learn a lightweight latent memory that can be efficiently queried at deployment time. Our representation, which we call the \textbf{workspace token}, is trained by (1) using a VLM to identify current and historical information necessary for completing a task, then (2) distilling these into the workspace token using a set-reconstruction decoder loss. In both simulation and hardware, we show that the workspace token can be used as a drop-in replacement for observations during deployment, enabling policies to solve memory-intensive tasks without the need for VLM reasoning in-the-loop. Interestingly, we found that workspace tokens are not only more lightweight but also lead to better policy performance.

</details>

---

### [[20_Research/Papers/具身智能/GeoAAC_Geometry-Based_Adaptive_Action_Chunking_from_Denoising_Trajectories_in_VLA_Policies|GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies]]

![[assets/2609.20776_figure.png|800]]

- **arXiv**: [2609.20776](https://arxiv.org/abs/2609.20776)
- **PDF**: https://arxiv.org/pdf/2609.20776
- **详细分析**: [[20_Research/Papers/具身智能/GeoAAC_Geometry-Based_Adaptive_Action_Chunking_from_Denoising_Trajectories_in_VLA_Policies|GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies]]
- **作者**: Xin Chen, Sen Chen, Yujuan Ding, Jian Liu, Guoqing Wang, Wei Ye, Heng Tao Shen, Yi Bin
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《GeoAAC: Geometry-Based Adaptive Action Chunking from Denoising Trajectories in VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action chunking is widely used for action generation and execution in Vision-Language-Action (VLA) policies, yet existing approaches commonly use a fixed action horizon. During a rollout, different task stages may require different levels of action continuity, control precision, and closed-loop feedback, making a fixed horizon unable to accommodate changing control requirements. We propose \textbf{GeoAAC}, a geometry-based adaptive action chunking method for flow-based VLA policies that adjusts the action horizon according to the reliability of the current action prediction. We show that the geometry of Flow Matching denoising trajectories provides process-level information for characterizing prediction reliability, with geometric variation across action prefixes remaining positively correlated with predictive uncertainty. GeoAAC uses this prefix-wise geometry to construct a horizon-wise geometric profile and adaptively determine the action horizon from a single generation without additional training. Experiments with GR00T N1.5 and {\pi}0.5 on LIBERO, LIBERO-Pro, RoboCasa365, and real-world manipulation tasks show consistent improvements over fixed-action-horizon baselines and existing adaptive methods, including up to 8.7 percentage points in simulation and an increase in average real-world success rate from 53.3\% to 74.4\%.

</details>

---

### [[20_Research/Papers/具身智能/HIL-UMI_Bringing_Human-in-the-Loop_Post-Training_of_Vision-Language-Action_Models_to_Universal_Manipulation_Interface|HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface]]

![[assets/2609.20659_figure.png|800]]

- **arXiv**: [2609.20659](https://arxiv.org/abs/2609.20659)
- **PDF**: https://arxiv.org/pdf/2609.20659
- **详细分析**: [[20_Research/Papers/具身智能/HIL-UMI_Bringing_Human-in-the-Loop_Post-Training_of_Vision-Language-Action_Models_to_Universal_Manipulation_Interface|HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface]]
- **作者**: Zimu Han, Yiming Zeng, Jiyao Zhang, Zihao Zhao, Yuanfei Wang, Yixiang Jin, Shiqi Li, Shuangben Chen, Wei Huang, Ruodai Li, Hui Shen, Hao Dong
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《HIL-UMI: Bringing Human-in-the-Loop Post-Training of Vision-Language-Action Models to Universal Manipulation Interface》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GR-RL, HIL-SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale vision-language-action (VLA) models provide powerful priors for robot manipulation, yet adapting them to a specific deployment remains challenging. Supervised fine-tuning (SFT) on task-specific demonstrations provides a step toward deployment, but faces two persistent limitations: static data provide limited coverage of out-of-distribution states, and standard imitation objectives do not distinguish progressing behavior from less useful data. Interactive post-training can address these limitations, but typically requires repeated policy execution and human intervention on a physical robot. We introduce HIL-UMI, a policy-guided Universal Manipulation Interface (UMI) framework for robot-free human-in-the-loop VLA post-training. During handheld UMI demonstrations, HIL-UMI queries the current policy on the same observation stream without executing its predictions. The Energy Score compares the human action trajectory with policy inference and triggers collection when their discrepancy indicates an out-of-distribution region. In a separate feedback loop, low online advantage predictions identify essential segments for refining a progress-based advantage estimator. The updated estimator then guides advantage-conditioned behavioral cloning using a balanced mixture of base demonstrations and new policy data. This design preserves the iterative and policy-aware nature of human-in-the-loop learning while decoupling data collection from robot deployment. Experiments on four real-world tasks spanning long-horizon and precise manipulation show that HIL-UMI achieves consistent improvement over SFT and benefits from both targeted collection and advantage refinement. Moreover, HIL-UMI outperforms HG-DAgger on Clean Up Table with lower per-frame collection time, suggesting a scalable path for VLA post-training across operators and locations.

</details>

---

### [[20_Research/Papers/大模型/Chronicle_Cut-Point_Replay_for_Regression_Testing_of_LLM_Agents|Chronicle: Cut-Point Replay for Regression Testing of LLM Agents]]

![[assets/2609.20625_first_page.png|800]]

- **arXiv**: [2609.20625](https://arxiv.org/abs/2609.20625)
- **PDF**: https://arxiv.org/pdf/2609.20625
- **详细分析**: [[20_Research/Papers/大模型/Chronicle_Cut-Point_Replay_for_Regression_Testing_of_LLM_Agents|Chronicle: Cut-Point Replay for Regression Testing of LLM Agents]]
- **作者**: Tisha Chawla, Susheem Koul
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.25（加权：大模型 1.25）
- **关联关键词**: LLM, Agent

#### 研究背景与动机

《Chronicle: Cut-Point Replay for Regression Testing of LLM Agents》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model responses are non-deterministic, so failures in LLM agents are hard to reproduce: a failure depends on inference that is not bitwise reproducible, on tools that read changing state, and on a multi-step trajectory that a re-run rarely repeats. Record-and-replay makes a run reproducible, but existing agent tooling records runs only to trace or score them, not to test a code change against them. We present Chronicle, which records an agent run at its non-deterministic boundaries as immutable envelopes and replays it from the record. Its central operation, cut-point replay, serves a chosen subset of boundaries from the record and executes the complementary subset live with new code, turning a recorded incident into a regression test that runs in continuous integration. On a benchmark of 6 recorded failures with simulated model boundaries, recording adds 23 {\mu}s per crossing (0.008% of an assumed 300 ms model call), full replay issues zero model calls and is bit-stable across 20 repetitions, and cut-point tests fail on faulty code and pass on guarded and benign changes for all 6 incidents. In a mutation study of the guarded tools, cut-point tests catch every mutant that lets the recorded unsafe action through, while a baseline that stubs every boundary, using the same assertion, catches none. Chronicle and the benchmark are publicly available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Accelerating_Visual_Policy_Learning_with_Sampling-Based_Model_Predictive_Control|Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control]]

![[assets/2609.20575_figure.png|800]]

- **arXiv**: [2609.20575](https://arxiv.org/abs/2609.20575)
- **PDF**: https://arxiv.org/pdf/2609.20575
- **详细分析**: [[20_Research/Papers/具身智能/Accelerating_Visual_Policy_Learning_with_Sampling-Based_Model_Predictive_Control|Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control]]
- **作者**: Yilang Liu, Haoxiang You, Qian Wang, Daniel Rakita, Ian Abraham
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 1.42（加权：具身智能 0.6，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Accelerating Visual Policy Learning with Sampling-Based Model Predictive Control》归入 具身智能、强化学习、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning visual policies for locomotion and manipulation requires coordinating contact with the environment and can incur substantial computation and GPU memory costs. First-order policy gradients (FoPG) reduce training cost through differentiable simulation, but local optimization can converge to unintended contact patterns. To address this shortfall, we propose Sampling-Guided Policy Search (SGPS), which couples recurring action-target refinement by sampling-based model-predictive control with first-order policy optimization. Behavior cloning initializes the policy from sampled actions; training then alternates sampling-based refinement with short-horizon FoPG updates under perturbed initial states and randomized dynamics. For visual policy training, we use a decoupled FoPG formulation that excludes rendering from the computation graph, enabling direct learning from depth observations without a state-policy teacher. On a single GPU, SGPS learns policies for locomotion, obstacle traversal, crate pushing, and bimanual carrying on simulated Unitree Go2 and G1 robots. Our experiments further show that refinement improves policy learning beyond initialization and tracking alone. For hardware deployment, the distilled policy transfers zero-shot to a real Go2 and uses onboard depth to autonomously trot, crawl, clear hurdles, and switch between these behaviors.

</details>

---

### [[20_Research/Papers/具身智能/A_Mathematical_Model_of_Motivated_Emotional_Mind_-_Cognitive_Embodied_System|A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System]]

![[assets/2609.20437_first_page.png|800]]

- **arXiv**: [2609.20437](https://arxiv.org/abs/2609.20437)
- **PDF**: https://arxiv.org/pdf/2609.20437
- **详细分析**: [[20_Research/Papers/具身智能/A_Mathematical_Model_of_Motivated_Emotional_Mind_-_Cognitive_Embodied_System|A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System]]
- **作者**: Wiesław L. Galus, Janusz A. Starzyk
- **cs 子类**: cs.AI
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习
- **相关性评分**: 1.4（加权：具身智能 1.2，强化学习 0.2）
- **关联关键词**: EmbodiedAI, RL, Systems

#### 研究背景与动机

《A Mathematical Model of Motivated Emotional Mind - Cognitive Embodied System》归入 具身智能、强化学习 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This article presents a mathematical model of the Motivated Emotional Mind cognitive architecture developed for embodied intelligent systems. Such a system learns to maintain its homeostasis through a generalized form of reinforcement learning based on its internal motivations, termed motivated learning (ML). The principal contribution of this article is a rigorous formalization of the re-entrant loop integrating feedforward processing, lateral interactions, and feedback pathways, together with the representational selection mechanisms that govern adaptive system responses. The model specifies how ongoing exteroceptive and interoceptive signals, bodily-motivational context, and memory traces are bound into associative memory structures termed semblions, which compete for access to further processing and top-down reconstruction. The formalization encompasses secondary perception, representational competition, curiosity, procedural gaps, and action selection directed toward limiting allostatic violations. Within this framework, motivated learning is tailored to embodied systems whose dynamics are shaped by needs, affect, and the current regulatory state. Unlike standard reinforcement-learning models, the proposed approach incorporates need thresholds, goal generation and shifting goals, bodily state, resource constraints, and action uncertainty, thereby providing a more adequate account of response selection under regulatory pressure. Global affect functions as a central control signal, modulating the learning rate, representational valence, and the balance between exploration and exploitation. The model presented here is a step toward a more rigorous formalization of cognitive phenomena and may provide a basis for further theoretical analysis, computer simulation, and implementation in artificial-intelligence systems inspired by biological processes.

</details>

---

### [[20_Research/Papers/具身智能/JEPA-WAM_Connecting_Generated_Visual_Instructions_to_World_Action_Models_through_JEPA_Latent_Representations|JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations]]

![[assets/2609.20277_figure.png|800]]

- **arXiv**: [2609.20277](https://arxiv.org/abs/2609.20277)
- **PDF**: https://arxiv.org/pdf/2609.20277
- **详细分析**: [[20_Research/Papers/具身智能/JEPA-WAM_Connecting_Generated_Visual_Instructions_to_World_Action_Models_through_JEPA_Latent_Representations|JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations]]
- **作者**: Tianbin Liu, Jian Zhu, Taiyi Su, Jianjun Zhang, Chong Ma, Zitai Huang, Yi Xu
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《JEPA-WAM: Connecting Generated Visual Instructions to World Action Models through JEPA Latent Representations》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Interleave-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) have demonstrated strong robotic manipulation capabilities by augmenting pretrained video generative models with action experts. However, current WAMs still show limited instruction-following ability when conditioned solely on text instructions. We argue that this limitation stems in part from a structural imbalance in robot-learning data: rich visual-action trajectories are often paired with sparse and repetitive language annotations, allowing policies to identify tasks from visual context and motion regularities rather than grounding the instruction itself. To address this limitation, we introduce JEPA-WAM, which augments each text instruction with a bank of stochastically generated visual instructions, providing diverse visual cues for instruction following. Specifically, JEPA-WAM uses an off-the-shelf text-to-image generator to sample multiple task-completion images conditioned on the text instruction, without training the generator. Although these generated images may differ from the current visual scene in appearance and layout, they remain semantically aligned with the instruction and serve as visual goal references. To focus on task-level semantics beyond appearance, we encode these references with a frozen V-JEPA 2.1 encoder. The resulting dense goal representations are compressed into compact goal tokens that condition both the video and action experts through cross-attention. We further construct a real-robot instruction-following benchmark covering in-distribution, out-of-distribution scene, and out-of-distribution instruction settings. On this benchmark, JEPA-WAM achieves success rates of 87.3%, 74.5%, and 80.9% in these three settings, outperforming {\pi}0 and Fast-WAM by at least 10.0, 27.3, and 14.5 percentage points, respectively.

</details>

---

### [[20_Research/Papers/具身智能/VLN_on_the_Fly_An_Onboard_Vision-Language_Navigation_Stack_for_Aerial_Robots|VLN on the Fly: An Onboard Vision-Language Navigation Stack for Aerial Robots]]

![[assets/2609.20191_figure.png|800]]

- **arXiv**: [2609.20191](https://arxiv.org/abs/2609.20191)
- **PDF**: https://arxiv.org/pdf/2609.20191
- **详细分析**: [[20_Research/Papers/具身智能/VLN_on_the_Fly_An_Onboard_Vision-Language_Navigation_Stack_for_Aerial_Robots|VLN on the Fly: An Onboard Vision-Language Navigation Stack for Aerial Robots]]
- **作者**: Marco S. Tayar, Felipe Tommaselli, Gianluca Capezutto, Pedro Antonio Rabelo Saraiva, Pedro H. V. de Freitas, Lucas Kido, Guilherme Sonego, Ricardo V. Godoy, Marcelo Becker
- **cs 子类**: cs.AI, cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.42（加权：具身智能 0.3，大模型 0.1，强化学习 0.36，世界模型 0.16，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VLN on the Fly: An Onboard Vision-Language Navigation Stack for Aerial Robots》归入 机器人、强化学习、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AerialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Running vision-language navigation fully onboard an aerial robot is hard, since grounding, planning, and control must share limited compute and a single-stage error is difficult to isolate in flight. End-to-end aerial policies fuse these stages into one network, giving up the observability and safety checks a modular stack keeps available. We propose VLN on the Fly, an onboard stack that keeps grounding, planning, and control as separate, inspectable stages. A quantized VLM grounds an instruction to a coarse image cell, depth lifts it to a 3D goal, a fast B-spline planner returns a feasible trajectory, and a pretrained reinforcement learning policy tracks it to motor commands across quadrotors. Across 15 onboard flights over three everyday referents in a controlled indoor volume, the stack reaches the target in 13 of 15 trials with 5.72 cm mean goal error and 39.3% average GPU utilization. In 6 additional cluttered-environment trials, the stack tracks collision-free trajectories under onboard perception gating.

</details>

---

### [[20_Research/Papers/具身智能/Astronex-World_1.0_Real-Time_Interactive_World_Model_Foundation|Astronex-World 1.0: Real-Time Interactive World Model Foundation]]

![[assets/2609.20034_figure.png|800]]

- **arXiv**: [2609.20034](https://arxiv.org/abs/2609.20034)
- **PDF**: https://arxiv.org/pdf/2609.20034
- **详细分析**: [[20_Research/Papers/具身智能/Astronex-World_1.0_Real-Time_Interactive_World_Model_Foundation|Astronex-World 1.0: Real-Time Interactive World Model Foundation]]
- **作者**: Xin Zhou, Cong Miao
- **cs 子类**: cs.AI, cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.6，世界模型 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI, WorldModel, ComputerVision

#### 研究背景与动机

《Astronex-World 1.0: Real-Time Interactive World Model Foundation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Astronex-World, InteractiveWorld, LingBot-World, UniSim, VBench, WBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Astronex-World 1.0, an open controllable video world-model foundation. Given a text prompt (text-to-video) or an initial observation (image-to-video), the model predicts future visual states under frame-aligned camera trajectories, continuous actions, and an embodiment identifier, and accepts text events inserted at a specified position of a rollout. The family provides a bidirectional model for full-context generation and a causal model with block-causal attention and cross-block KV caching for persistent generation, both built on the Wan2.2-TI2V-5B prior. PRoPE injects camera intrinsics and extrinsics, while a 64-dimensional action stream modulates every Transformer layer. A five-stage training path develops bidirectional camera and action control, converts the backbone to block-causal generation, distills a few-step student, restores mixed-domain dynamics, and applies asymmetric DMD/DMD2 distribution matching. The causal model generates 832x480 video at 24 fps. All five training stages run on two NVIDIA L20 48 GB GPUs, and the causal model streams in real time on one. It scores 73.5 on WBench Navi and 70.0 on WBench Full. On Full, this 5B model is above the 13.6B LongCat-Video and the 14B Helios, within one point of the 22B LTX-2.3, and above YUME 1.5, which is post-trained from the same 5B prior on NVIDIA A100 GPUs. The reserved action input and output interfaces allow post-training for embodied intelligence and autonomous driving.

</details>

---

### [[20_Research/Papers/大模型/EPIG-Tree_Compute-Optimal_Branching_for_Gradient-Efficient_Reinforcement_Learning|EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning]]

![[assets/2609.20004_figure.png|800]]

- **arXiv**: [2609.20004](https://arxiv.org/abs/2609.20004)
- **PDF**: https://arxiv.org/pdf/2609.20004
- **详细分析**: [[20_Research/Papers/大模型/EPIG-Tree_Compute-Optimal_Branching_for_Gradient-Efficient_Reinforcement_Learning|EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning]]
- **作者**: Nikita Khomich, Leopold Hermansson, Ido Hakimi
- **cs 子类**: cs.AI, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 1.36，世界模型 0.16）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《EPIG-Tree: Compute-Optimal Branching for Gradient-Efficient Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TreeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward-based reinforcement learning for language models, exemplified by Group Relative Policy Optimization (GRPO), collapses an entire stochastic trajectory into a single scalar reward. This is clean and scalable, but it explores and allocates reward inefficiently: a trajectory may contain many causal decisions, recovery attempts, and environment-randomness events, yet every token or action inherits one trajectory-level advantage. We study tree-based rollout construction as a compute-allocation problem for policy-gradient estimation. Our central claim is that branches should be placed not where the policy is merely uncertain, but where an additional branch most reduces uncertainty about the policy gradient per unit of compute. From a law-of-total-variance decomposition of the local policy-gradient random variable, we derive two allocation laws: new branches reduce decision uncertainty, while repeated suffix rollouts reduce continuation uncertainty. The resulting EPIG-Tree score allocates branches using the already computed rollouts. It estimates occupancy- and score-weighted value uncertainty, along with a suffix law $n_e \propto w_e \|\nabla_\theta \log \pi(a_e|h_e)\| \sigma_e / \sqrt{c_e}$. Empirically, EPIG reduces gradient MSE in cloned-state control, winning in all nine dense continuous-control environments of a 13-environment sweep and recovering the reference gradient direction near-perfectly, and it improves frozen-LLM gradient calibration relative to entropy branching. In online single-turn math, tree-local credit beats flat GRPO, while branch placement is secondary to token-level credit assignment. In online multi-turn Wordle, EPIG attains the highest final win rate (0.850), overtaking flat GRPO, which saturates early at 0.790, and entropy branching as training proceeds, confirming that the gradient-estimation advantage transfers to a stateful, large-action setting.

</details>

---

### [[20_Research/Papers/具身智能/MaskHarness-WAM_Instance-Grounded_Harnessing_for_Long-Horizon_Robot_Manipulation|MaskHarness-WAM: Instance-Grounded Harnessing for Long-Horizon Robot Manipulation]]

![[assets/2609.19974_figure.png|800]]

- **arXiv**: [2609.19974](https://arxiv.org/abs/2609.19974)
- **PDF**: https://arxiv.org/pdf/2609.19974
- **详细分析**: [[20_Research/Papers/具身智能/MaskHarness-WAM_Instance-Grounded_Harnessing_for_Long-Horizon_Robot_Manipulation|MaskHarness-WAM: Instance-Grounded Harnessing for Long-Horizon Robot Manipulation]]
- **作者**: Zitai Huang, Taiyi Su, Jian Zhu, Jianjun Zhang, Chong Ma, Tianbin Liu, Weiyi Lu, Yi Xu, Hanli Wang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《MaskHarness-WAM: Instance-Grounded Harnessing for Long-Horizon Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robot manipulation requires not only stable local visuomotor control, but also continuous target tracking and reliable task progress assessment throughout execution. This challenge becomes particularly critical when multiple objects share identical appearances and must be manipulated in a prescribed order. In such scenarios, relying solely on a limited-horizon manipulation policy is often insufficient to determine which instance should be operated on and when the task should transition to the next stage. To address this challenge, we propose MaskHarness-WAM, an instance-grounded harness for long-horizon manipulation. The proposed system connects high-level task planning with low-level manipulation policies through target masks, while leveraging visual feedback for subtask scheduling and continuous execution. Since each subtask corresponds to a different target instance, the low-level policy requires a newly established initial target mask under the updated scene at each subtask transition. The harness continuously re-observes the environment, generates, and verifies the target mask at subtask boundaries, thereby updating the instance-level spatial condition provided to the low-level policy. Furthermore, the system advances the manipulation process by switching target instances according to the verified completion status of each subtask. Experiments on a real robot platform demonstrate that MaskHarness-WAM substantially outperforms limited-horizon policies on sequential multi-object manipulation, showing its effectiveness in extending local manipulation skills to reliable long-horizon execution.

</details>

---

### [[20_Research/Papers/强化学习/Learning_and_Transferring_Closed-Loop_Robot_Software|Learning and Transferring Closed-Loop Robot Software]]

![[assets/2609.19906_figure.png|800]]

- **arXiv**: [2609.19906](https://arxiv.org/abs/2609.19906)
- **PDF**: https://arxiv.org/pdf/2609.19906
- **详细分析**: [[20_Research/Papers/强化学习/Learning_and_Transferring_Closed-Loop_Robot_Software|Learning and Transferring Closed-Loop Robot Software]]
- **作者**: So Kuroki, Yujin Tang
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Learning and Transferring Closed-Loop Robot Software》归入 机器人、具身智能、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Closed-loop robot policies require observation processing, state management, and situation-dependent branching, making them costly to design and tune manually. Although coding agents increasingly support control-code generation and optimization, it remains unclear whether implementations improved on source tasks also support policy acquisition for new tasks. We study this question by treating complete closed-loop implementations as reusable execution experience. For each source task, a coding agent generates policy code from a few successful demonstrations and iteratively improves it using simulation feedback. The validation-selected implementations are retained in a software archive. For new tasks, the agent generates and improves policies using archived implementations, target demonstrations, and execution feedback. The resulting policy is then frozen and executes without further model calls. Across four source tasks in RoboCasa, iterative optimization increases mean success from 28.3% to 64.2%. Across nine target tasks and three independent runs, mean success is 45.2% without references, 41.5% with initial source code, and 57.0% with optimized source code. Optimized references outperform initial references in all three runs on the nine-task average, with a mean gain of 15.6 percentage points. These results demonstrate the value of execution-improved software as a resource for acquiring new policies in this setting, although initial references remain better on two target tasks when averaged across runs.

</details>

---

### [[20_Research/Papers/大模型/Dual-Axis_Policy_Optimization_for_LLM_Agents_Bayesian_Feedback_Attribution_and_Trajectory_Mass_Normalization|Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization]]

![[assets/2609.19830_figure.png|800]]

- **arXiv**: [2609.19830](https://arxiv.org/abs/2609.19830)
- **PDF**: https://arxiv.org/pdf/2609.19830
- **详细分析**: [[20_Research/Papers/大模型/Dual-Axis_Policy_Optimization_for_LLM_Agents_Bayesian_Feedback_Attribution_and_Trajectory_Mass_Normalization|Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization]]
- **作者**: Yingxuan Zhuang, Binhe Yu, Jingxiao Yang, Ruopei Sun, Ziting Li, Cheng Tan, Xuhong Zhang, Jianwei Yin, Jintao Chen
- **cs 子类**: cs.AI
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.8（加权：大模型 0.8，强化学习 1）
- **关联关键词**: LLM, Agent, RL

#### 研究背景与动机

《Dual-Axis Policy Optimization for LLM Agents: Bayesian Feedback Attribution and Trajectory Mass Normalization》归入 强化学习、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ALFWorld, SearchQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning for LLM agents involves two distinct optimization di- mensions: how environment feedback is exploited within a trajectory, and how complete trajectories are aggregated across a batch. We formulate these dimen- sions as Intra-Trajectory Feedback Attribution and Inter-Trajectory Objec- tive Aggregation, and introduce BATON (Bayesian Attribution and Trajectory Objective Normalization), a dual-axis policy optimization framework. BATON instantiates the first axis with Bayesian Feedback Attribution, which constructs a feedback-conditioned posterior over sampled actions, and the second with Trajec- tory Mass Normalization (TMN), which assigns equal optimization mass to com- plete trajectories. Experiments with GRPO and GiGPO on ALFWorld, WebShop, and SearchQA show that both axes provide independent gains and that their combi- nation consistently achieves the strongest overall performance across model scales.

</details>

---

### [[20_Research/Papers/强化学习/TacSushi_Tactile-Grounded_World-Action_Modeling_for_Dexterous_Sushi_Manipulation|TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation]]

![[assets/2609.19613_figure.png|800]]

- **arXiv**: [2609.19613](https://arxiv.org/abs/2609.19613)
- **PDF**: https://arxiv.org/pdf/2609.19613
- **详细分析**: [[20_Research/Papers/强化学习/TacSushi_Tactile-Grounded_World-Action_Modeling_for_Dexterous_Sushi_Manipulation|TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation]]
- **作者**: Haodi Hu, Kaen Kogashi, Toshiaki Koike-Akino
- **cs 子类**: cs.AI, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《TacSushi: Tactile-Grounded World-Action Modeling for Dexterous Sushi Manipulation》归入 具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous food manipulation requires control under deformation, occlusion, and uncertain contact. We present TacSushi, a tactile-grounded, Cosmos3-based world-action policy that learns from recorded future consequences while acting on current observations. The backbone encodes current RGB, language, and hand state, and feature-wise gated fusion incorporates fingertip tactile features into the action representation. During training, a decoder conditioned on demonstrated action chunks predicts logged future visual observations, task progress, relative contact risk, and tactile summaries; this decoder is removed at deployment. Failed trials provide consequence supervision, but their actions are excluded from imitation. We train TacSushi on 340 successful and 50 failed real-robot trials and compare six methods in 600 separate rollouts across three in-distribution tasks and two out-of-distribution ingredient variants. To assess food quality beyond a single geometric threshold, we score terminal outcomes using an anchored visual-quality protocol that equally weights five human ratings and three vision-language-model ratings per rollout. Full TacSushi achieves 68.3% average in-distribution success and 37.5% out-of-distribution success, compared with 36.7%/10.0% without future-consequence supervision and 25.0%/17.5% with direct tactile concatenation in place of gated fusion. These comparisons support complementary benefits of feature-wise gated tactile fusion and training-only predictive supervision.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model_Agents_for_Evidence_Based_Genetic_Disease_Severity_Classification|Large Language Model Agents for Evidence Based Genetic Disease Severity Classification]]

![[assets/2609.19569_first_page.png|800]]

- **arXiv**: [2609.19569](https://arxiv.org/abs/2609.19569)
- **PDF**: https://arxiv.org/pdf/2609.19569
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model_Agents_for_Evidence_Based_Genetic_Disease_Severity_Classification|Large Language Model Agents for Evidence Based Genetic Disease Severity Classification]]
- **作者**: Tohid Ghasemnejad, Ahmadreza Argha, Mark Grosser, John Wang, Min Yang, Thantrira Porntaveetus, Tony Roscioli, Nigel H. Lovell, Mahmoud Aarabi, Hamid Alinejad-Rokny
- **cs 子类**: cs.AI, cs.CL
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.35（加权：大模型 1.35）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Large Language Model Agents for Evidence Based Genetic Disease Severity Classification》归入 大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Disease severity classification for genetic conditions is subjective and labor-intensive, creating bottlenecks in genomic screening, where commercial panels vary widely in size and overlap. We developed an autonomous AI agent integrating Reasoning and Acting (ReAct) with Retrieval-Augmented Generation (RAG) to classify 10,211 Human Phenotype Ontology terms. It uses American College of Medical Genetics (ACMG)-endorsed severity guidelines and American College of Obstetricians and Gynecologists (ACOG) quality-of-life criteria to retrieve PubMed literature, generate interpretable reasoning chains, and independently verify claims. At the phenotype level, using expert-curated cohorts, the agent achieved 93.55% accuracy (MCC 0.9237) with 82.6% to 91.4% of claims supported by direct evidence or valid inferences. Gene-level severity was aggregated across 8,738 pairs, identifying 3,283 autosomal recessive pairs with severe or profound presentations. External validation showed 95.2% concordance with Mackenzie's Mission gene list. This system enables standardized panel design by providing reliable, automated classification supported by direct evidence.

</details>

---

### [[20_Research/Papers/强化学习/CoreSense_Traceable_Failure_Recall_and_Conflict-Aware_Belief_Gating_for_Auditable_Robot_Decisions|CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions]]

![[assets/2609.19512_first_page.png|800]]

- **arXiv**: [2609.19512](https://arxiv.org/abs/2609.19512)
- **PDF**: https://arxiv.org/pdf/2609.19512
- **详细分析**: [[20_Research/Papers/强化学习/CoreSense_Traceable_Failure_Recall_and_Conflict-Aware_Belief_Gating_for_Auditable_Robot_Decisions|CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions]]
- **作者**: Zoe Li
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《CoreSense: Traceable Failure Recall and Conflict-Aware Belief Gating for Auditable Robot Decisions》归入 机器人、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Artificial Intelligence 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ARMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots can recall prior failures without knowing whether recalled evidence remains valid, conflicts with current observations, or is sufficient to guide a decision. We present CoreSense, a robot-system integration architecture that combines traceable episodic evidence with a conflict-aware belief gate and bounded, auditable recommendations. The gate checks scope, provenance, time, contradiction, and support before it permits PROCEED, requests re-observation, abstains, or escalates. Evaluation follows three complementary layers without commanding a physical robot: offline public real-robot data, a frozen signal-level simulation, and a live cloud deployment path. On CableTrace-120 and BotFails-200, belief gating reduces protocol-defined unsafe proceeds from 20% and 40% to 0%. A disjointly calibrated raw-video policy also reaches 0% unsafe proceed, but overblocks every nominal episode. On public data, a ViFailback-BotFails visual detector reaches 0.778 AUROC yet remains all-blocking, whereas cycle-disjoint UR3 telemetry for protective stops yields 0% unsafe proceed, 36.1% overblocking, and 61.9% coverage; grip-loss transfer remains a negative result. Controlled physical corroboration yields 3.3%, 0%, and 42.0%, while conflict-aware fusion yields 4.7%, 0%, and 42.8%. Finally, 20/20 cloud recalls validate a CockroachDB Cloud-Amazon Bedrock deployment path. The evidence supports an auditable integration pattern, not autonomous recovery or certified safety.

</details>

---

### [[20_Research/Papers/具身智能/From_Rollout_to_Reset_A_Graph-Based_Harness_for_Autonomous_Long-Horizon_Manipulation_Evaluation|From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation]]

![[assets/2609.19413_figure.png|800]]

- **arXiv**: [2609.19413](https://arxiv.org/abs/2609.19413)
- **PDF**: https://arxiv.org/pdf/2609.19413
- **详细分析**: [[20_Research/Papers/具身智能/From_Rollout_to_Reset_A_Graph-Based_Harness_for_Autonomous_Long-Horizon_Manipulation_Evaluation|From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation]]
- **作者**: Jing Jiang, Yue Yang, Xinkai Jiang, Gedas Bertasius, Daniel J. Szafir, Rudolf Lioutikov
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《From Rollout to Reset: A Graph-Based Harness for Autonomous Long-Horizon Manipulation Evaluation》归入 具身智能、机器人、大模型 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AutoEval, FurnitureBench, LiLo-VLA, Long-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation policies are improving quickly, and real-robot evaluation remains the standard evidence for that progress. It still relies on a human to reset the scene between rollouts, which consumes operator time and leaves the initial state distribution unspecified, so results reproduce poorly. A recent system, AutoEval, automates both reset and scoring, but only for single-step tasks, because a long-horizon rollout can terminate in combinatorially many configurations that no single learned reset policy covers. We present HALTER, a Harness for Autonomous Long-horizon Task Evaluation and Reset, which restores the scene by planning over a library of learned atomic reset skills, so demonstration cost scales with the size of that library rather than with the number of terminal states. HALTER builds a spatial scene graph online from point clouds and vision foundation models, and an LLM reasons over this graph to score the rollout, plan the reset, and verify that the reset succeeded, without collecting labeled success images for any task. On four long-horizon tasks on a Franka arm, HALTER restores the scene in 76% of episodes, against 52% for AutoEval and 65% for a motion-planning reset, and it estimates the completed-skill fraction correctly in 90% of episodes, against 76%. Its reset-verification verdict is correct in 91% of episodes, compared with 78% for AutoEval. It also cuts the operator time of an evaluation campaign by 72% relative to manual reset. We further measure compositional generalization on three held-out tasks, where HALTER resets 74.7% of episodes against 1.3% for a per-task reset policy, and we ablate the scene representation and the graph update rate.

</details>

---

### [[20_Research/Papers/大模型/Kinematics-Grounded_Agentic_AI_for_Robotic_Additive_Manufacturing_Process_Planning|Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning]]

![[assets/2609.19347_figure.png|800]]

- **arXiv**: [2609.19347](https://arxiv.org/abs/2609.19347)
- **PDF**: https://arxiv.org/pdf/2609.19347
- **详细分析**: [[20_Research/Papers/大模型/Kinematics-Grounded_Agentic_AI_for_Robotic_Additive_Manufacturing_Process_Planning|Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning]]
- **作者**: Jingzhan Ge, Ruimin Chen, Azadeh Haghighi, Jiong Tang, Farhad Imani
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Kinematics-Grounded Agentic AI for Robotic Additive Manufacturing Process Planning》归入 机器人、大模型、具身智能 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FDM-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic additive manufacturing (AM) extends material-extrusion printing beyond gantry kinematics but makes process planning robot-dependent. A slicer-generated plan that appears favorable in part coordinates can become infeasible or robotically unfavorable on a manipulator because slicer-process decisions and part orientation determine the generated path, while part orientation and workspace placement affect its kinematic realization. Existing AM tools, large language model (LLM)-based decision-support methods, and digital-shadow systems do not provide integrated pre-execution evaluation of these coupled decisions. This paper presents agentic robotic additive manufacturing (A-RAM), an agent-specialist-tool framework that converts user intent and a part file into traceable, execution-ready plans. The LLM interprets manufacturing objectives and constraints, identifies prescribed and searchable planning variables, and encodes this reasoning in a schema-constrained request; a deterministic Planning Agent instantiates the corresponding search workflow, while domain tools compute quantitative evidence for slicing, placement, inverse kinematics, trajectory timing, Joint-6 jerk, and extrusion. The framework is evaluated on a six-axis robotic-arm AM cell through three case studies covering expert-specified planning, goal-only planning, objective-dependent infill screening, and geometry-dependent orientation-placement selection. Across the evaluated candidate sets, selected plans achieve up to 53.5% lower maximum Joint-6 jerk and 48.3% lower mean absolute Joint-6 jerk than the least favorable valid candidates, while objective-specific infill screening yields motion-plan completion times up to 40.1% shorter and extrusion paths up to 12.7% shorter than the corresponding least favorable screened patterns.

</details>

---

### [[20_Research/Papers/具身智能/GAVEL_Graph_World_Models_for_Verified_and_Efficient_Long-Horizon_LLM_Task_Planning|GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning]]

![[assets/2609.19315_figure.png|800]]

- **arXiv**: [2609.19315](https://arxiv.org/abs/2609.19315)
- **PDF**: https://arxiv.org/pdf/2609.19315
- **详细分析**: [[20_Research/Papers/具身智能/GAVEL_Graph_World_Models_for_Verified_and_Efficient_Long-Horizon_LLM_Task_Planning|GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning]]
- **作者**: Ruiyang Wang, Hao-Lun Hsu, Swarajh Mehta, Jiwoo Kim, Zhihao Dou, Miroslav Pajic
- **cs 子类**: cs.AI, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.6，大模型 0.4，世界模型 0.8，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《GAVEL: Graph World Models for Verified and Efficient Long-Horizon LLM Task Planning》归入 世界模型、具身智能、机器人 方向。该论文围绕 Artificial Intelligence 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) provide a flexible interface for long-horizon robot planning, but generated plans often fail to respect embodiment constraints, recover from planning errors, or reason effectively under partial observability. We present GAVEL, a framework for verifying and repairing long-horizon LLM planning built around an explicit graph world model. The graph represents relevant object-relations, action pre-conditions and effects, and probabilistic beliefs over unobserved object locations. This model can predict the consequences of LLM-generated actions before execution, detect violations, and repair those whose corrections follow directly from the world model. This method also reserves LLM replanning solely for errors requiring semantic reasoning. For multi-task instructions, GAVEL reasons over distributions of possible object locations to reorder remaining subtasks and minimize expected search cost. We evaluate GAVEL on BEHAVIOR-1K across 100 single long-horizon tasks and 500 multi-task instructions. With Qwen3-8B, GAVEL improves single-task success from 41.2% to 91.8% and multi-task success from 19.9% to 92.6%. Distributional belief reasoning also reduces travel distance by approximately 5.4% compared with a static variant. These improvements show that an explicit graph world model harness can substantially improve the reliability and efficiency of long-horizon embodied planning across compact and frontier hosted LLM capabilities.

</details>

---
