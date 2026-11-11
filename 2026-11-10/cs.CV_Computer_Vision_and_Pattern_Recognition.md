# cs.CV | Computer Vision and Pattern Recognition | 2026-11-10

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/World_In-Context_Learning_for_Agentic_Robot_Manipulation|World In-Context Learning for Agentic Robot Manipulation]]

![[assets/2611.12885_first_page.png|800]]

- **arXiv**: [2611.12885](https://arxiv.org/abs/2611.12885)
- **PDF**: https://arxiv.org/pdf/2611.12885
- **详细分析**: [[20_Research/Papers/具身智能/World_In-Context_Learning_for_Agentic_Robot_Manipulation|World In-Context Learning for Agentic Robot Manipulation]]
- **作者**: Heng Fang, Zehui Guo, Yuehan Zhang, Mingyang Du, Dingkang Liang, Xiang Bai
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.2，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《World In-Context Learning for Agentic Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Trained action policies write manipulation skill into network weights, tying what is learned to the distribution it is learned from. In-context learning (ICL) avoids this coupling but has not matched trained policies, because a demonstration recorded in another scene carries no feedback from the world the robot currently faces. We observe that what an agent learns in context is semantic, recording task steps and object roles rather than visual appearance, so experience gathered in one world transfers to another. Based on this insight, we propose World In-Context Learning (WICL), a paradigm in which a frozen model starts from a demonstration, rehearses the task in a world such as a simulator, and writes the feedback into its context rather than its weights. We build RoboScript, a modular infrastructure that implements WICL for agentic manipulation. From a single demonstration, RoboScript learns each task through rehearsal in simulation, freezes the learned knowledge as a Task Memory, and deploys the frozen memory on new scenes with data isolation that ensures every deployment input is available on a real robot. On all 50 tasks of RoboTwin 2.0, RoboScript reaches 83.4% mean success across clean and randomized settings with one demonstration per task and no gradient updates, exceeding the strongest trained action policy by over 20 points. The method generalizes across visual distributions, improves through reflection, scales with the foundation model, and transfers to a physical dual-arm robot through cross-embodiment memory adaptation. With a world in the loop, a robot can learn a manipulation task in its context as well as it learns one in its weights. All code is available at https://github.com/ArcheOne-AI/RoboScript

</details>

---

### [[20_Research/Papers/具身智能/Grasping_the_Future_Joint_3D_Hand-Object_Forecasting_From_Internet_Videos|Grasping the Future: Joint 3D Hand-Object Forecasting From Internet Videos]]

![[assets/2611.12879_figure.png|800]]

- **arXiv**: [2611.12879](https://arxiv.org/abs/2611.12879)
- **PDF**: https://arxiv.org/pdf/2611.12879
- **详细分析**: [[20_Research/Papers/具身智能/Grasping_the_Future_Joint_3D_Hand-Object_Forecasting_From_Internet_Videos|Grasping the Future: Joint 3D Hand-Object Forecasting From Internet Videos]]
- **作者**: Rustin Soraki, Matthew Wallingford, Ryan Aby, Brandon Chee, Jason Ren, Ali Farhadi, Homanga Bharadhwaj, Roozbeh Mottaghi
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Grasping the Future: Joint 3D Hand-Object Forecasting From Internet Videos》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To interact with an object, we need to anticipate both how it will move and how our hands should move with it. Human videos capture these relationships across everyday activities, offering a natural source for learning to predict future interactions. Learning from them requires recovering motion from completed interactions and using it to anticipate what could happen next. We present $\textit{Grasping-the-Future}$, a unified generative model of joint 3D hand-object motion, including wrist motion, finger articulation, and object position and orientation. Through masked spatiotemporal completion and flow matching, we train a single model for several prediction tasks: forecasting future interactions, predicting hand motion given object motion or vice versa, generating both trajectories toward a desired final object pose, and completing partially observed interactions. We explicitly model hand-object relations and incorporate contact constraints to help preserve grasp relationships during motion. To obtain 3D supervision from internet videos, we develop a scalable pipeline that combines pretrained perception models with joint geometric optimization to reconstruct completed interactions. We combine these recovered trajectories with annotated interaction datasets as training data for all tasks. We demonstrate strong performance across all tasks, outperforming released forecasters on datasets with 3D annotations. Moreover, we show geometric and physical plausibility of the predicted trajectories by retargeting them to a robotic embodiment. Videos are available at https://grasping-the-future.github.io.

</details>

---

### [[20_Research/Papers/机器人/V3DSAM_Semantic-Geometric_Loop_Verification_and_Geometry-Anchored_Persistent_Instance_Mapping_for_Feed-Forward_Dense_SLAM|V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM]]

![[assets/2611.12452_figure.png|800]]

- **arXiv**: [2611.12452](https://arxiv.org/abs/2611.12452)
- **PDF**: https://arxiv.org/pdf/2611.12452
- **详细分析**: [[20_Research/Papers/机器人/V3DSAM_Semantic-Geometric_Loop_Verification_and_Geometry-Anchored_Persistent_Instance_Mapping_for_Feed-Forward_Dense_SLAM|V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM]]
- **作者**: Maolin Ye, Dongqing Zhao, Linyang Li, Shuai Xue, Yuan Liu, Yiyuan Wang, Wen Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《V3DSAM: Semantic-Geometric Loop Verification and Geometry-Anchored Persistent Instance Mapping for Feed-Forward Dense SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To address unreliable cross-view association in long-sequence feed-forward dense SLAM, this letter presents V3DSAM, an open-vocabulary semantic dense SLAM system that establishes physical correspondences at both the scene and object levels. The system combines feed-forward geometric estimates from VGGT-SLAM 2.0 with open-vocabulary semantic observations from SAM3. We introduce semantic-geometric dual-scale loop verification, which identifies false loop closures using pixel-level bidirectional reprojection and object-level 3D spatial correspondences, without accessing backbone-internal features. We further propose geometry-anchored persistent instance mapping, which defines physical instances through class-constrained 3D connectivity in an optimized global coordinate system and assigns global IDs without inter-frame identity propagation. The proposed verifier rejects all four false loop candidates in our TUM RGB-D evaluation, while long-sequence ScanNet experiments show improved instance identity consistency. Thus, V3DSAM reduces dependence on internal backbone features and temporal ID propagation for robust long-term cross-view association.

</details>

---

### [[20_Research/Papers/具身智能/AutoVLA-D_Learn_a_Trajectory-Geometric_Condition_from_Reasoning_for_Autonomous_Driving_VLA|AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA]]

![[assets/2611.12382_figure.png|800]]

- **arXiv**: [2611.12382](https://arxiv.org/abs/2611.12382)
- **PDF**: https://arxiv.org/pdf/2611.12382
- **详细分析**: [[20_Research/Papers/具身智能/AutoVLA-D_Learn_a_Trajectory-Geometric_Condition_from_Reasoning_for_Autonomous_Driving_VLA|AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA]]
- **作者**: Yuguang Yang, Zhewen Tan, Canyu Chen, Linlin Yang, Cheng Chi, Chunyang Liu, Kehua Sheng, Jinyu Yang, Baochang Zhan, Bo Zhang, Yan Wang, Xianbin Cao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《AutoVLA-D: Learn a Trajectory-Geometric Condition from Reasoning for Autonomous Driving VLA》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA, Curious-VLA, DriveVLA, ELF-VLA, OpenDriveVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autoregressive VLA planning usually predicts continuous trajectories as the final output, but driving instructions often describe actions rather than ego states, which weakens direct conditioning on the final continuous trajectory. We address this gap with TrajCond, which introduces a discrete trajectory-geometric condition for VLA planning. Specifically, we represent TrajCond as a 1D-Brohan differential action trajectory and learn it with a two-stage training framework before final continuous trajectory prediction. With the simultaneous autoregressive generation of discrete and numeric trajectories, we name our method AutoVLA-D (Double). Experiments on NAVSIM navtest, nuScenes, and NeuroNCAP show that discrete trajectories are weaker as direct outputs but more effective as TrajCond, consistently improving final continuous trajectory prediction across closed-loop and open-loop driving benchmarks. Code is available at https://github.com/ShivaTeam/AutoVLA-D.

</details>

---

### [[20_Research/Papers/具身智能/VLA-MOPD_On-Policy_Distillation_for_Multi-Task_VLA_Policy_Consolidation|VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation]]

![[assets/2611.12286_figure.png|800]]

- **arXiv**: [2611.12286](https://arxiv.org/abs/2611.12286)
- **PDF**: https://arxiv.org/pdf/2611.12286
- **详细分析**: [[20_Research/Papers/具身智能/VLA-MOPD_On-Policy_Distillation_for_Multi-Task_VLA_Policy_Consolidation|VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation]]
- **作者**: Yongxuan Lv, Zhen Fang, Lichen Man, Hao Li, Pu Li, Hengyi Wang, Langfeng Cao, Lin Chen, Jie Huang, Xiu Su, Shan You, Fei Wang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《VLA-MOPD: On-Policy Distillation for Multi-Task VLA Policy Consolidation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MergeVLA, MixRL, OpenVLA, Real-World, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical intelligence requires embodied agents to ground language in observations and execute actions while retaining useful skills. Vision-language-action (VLA) policies offer a shared interface, but task-specific post-training often produces separate specialists. Consolidation is difficult: mixed-task reinforcement learning provides sparse trajectory-level credit, while offline distillation may miss student-visited observations and endpoint distillation does not supervise intermediate action-generation states. We introduce VLA Multi-teacher On-Policy Distillation (VLA-MOPD), a protocol for consolidating flow-matching VLA specialists. After acquiring task or suite experts, a shared student collects robot rollouts and queries the instruction-routed frozen teacher at each visited observation and intermediate ordinary differential equation (ODE) state. Detached per-flow-step transition targets supervise valid action chunks through a masked local matching loss; an optional reference-policy term supports retention on other tasks. Starting from one trajectory per LIBERO task, VLA-MOPD raises mean success-once from 75.4% to 98.9%, compared with 98.15% for endpoint action distillation. It improves mean RoboTwin 2.0 success from 73.0% to 89.3%; on a Piper robot, two consolidation rounds improve average success from 70.0% to 90.0%. In a near-matched Spatial-adaptation study, reference matching limits the Object suite decrease to 3.0 points, versus 13.2 without the reference term.

</details>

---

### [[20_Research/Papers/具身智能/LHNav_Long-Horizon_Humanoid_Navigation_via_Multirate_Coordination_and_Physics-Grounded_Action_Data|LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data]]

![[assets/2611.12136_figure.png|800]]

- **arXiv**: [2611.12136](https://arxiv.org/abs/2611.12136)
- **PDF**: https://arxiv.org/pdf/2611.12136
- **详细分析**: [[20_Research/Papers/具身智能/LHNav_Long-Horizon_Humanoid_Navigation_via_Multirate_Coordination_and_Physics-Grounded_Action_Data|LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data]]
- **作者**: Xueyang Wang, Zehong Shen, Dingkun Wei, Huaijin Pi, Changpeng Wang, Xing Zhu, Hujun Bao, Yujun Shen, Xiaowei Zhou
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《LHNav: Long-Horizon Humanoid Navigation via Multirate Coordination and Physics-Grounded Action Data》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TIC-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study humanoid navigation across multiple destinations under long-horizon language instructions. This task is challenging because robots must maintain progress across successive goals while continuously producing natural, stable whole-body motion through confined spaces. However, task decomposition in existing methods does not by itself ensure progress throughout execution, while waypoint-based navigation does not guarantee natural, route-faithful whole-body motion. Our key idea is to organize navigation into three complementary roles operating at different time scales: a Brain for task reasoning, a Cerebellum for local motion generation, and a Brainstem for whole-body execution. We realize this idea in LHNav, an asynchronous system that uses progress and arrival feedback to coordinate navigation goals, VLA motion-token prediction, and whole-body control. To train the Cerebellum for natural, route-faithful motion, we develop a physics-grounded data engine that improves physical tracking of motion references along collision-aware routes and pairs the resulting demonstrations with rendered visual observations. Together, these designs allow task planning to proceed alongside continuous movement and extend single-goal navigation to successive destinations with natural, route-faithful whole-body motion. In simulation, our navigation VLA outperforms OmniNav and DualVLN in single-goal success and motion smoothness, with fewer collisions and falls. Using a VLA trained only on single-goal demonstrations, LHNav achieves a 75.56% success rate on long-horizon navigation tasks. Deployment on the Unitree G1 further demonstrates single-goal navigation and zero-shot long-horizon task execution in real-world environments, including layouts with repositioned objects. Project website: https://robbyant-research.github.io/LHNav/.

</details>

---

### [[20_Research/Papers/具身智能/SPARK_Simple_Post-training_for_Adapting_pRetrained_Knowledge_to_Robot_Control|SPARK: Simple Post-training for Adapting pRetrained Knowledge to Robot Control]]

![[assets/2611.12102_figure.png|800]]

- **arXiv**: [2611.12102](https://arxiv.org/abs/2611.12102)
- **PDF**: https://arxiv.org/pdf/2611.12102
- **详细分析**: [[20_Research/Papers/具身智能/SPARK_Simple_Post-training_for_Adapting_pRetrained_Knowledge_to_Robot_Control|SPARK: Simple Post-training for Adapting pRetrained Knowledge to Robot Control]]
- **作者**: Taekyung Kim, Jeongeun Park, Byeongho Heo, Sungjoon Choi, Sangdoo Yun, Dongyoon Han
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《SPARK: Simple Post-training for Adapting pRetrained Knowledge to Robot Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale representation learning has produced public foundation models that provide strong general-purpose visual features. However, their pretraining objectives are not designed for robot representation learning, so the resulting embeddings tend to emphasize global semantics rather than the temporally sensitive representations required for robot control. Training robot models from scratch is also undesirable due to the limited scale and high collection cost of robotics data, as well as the substantial computational burden of pre-training. In this paper, we propose SPARK (Simple Post-training for Adapting pRetrained Knowledge), a post-training method that adapts foundation models to robot control. SPARK is built on two principles: temporal abstraction, which encourages the encoder to derive compact features that preserve information essential for understanding temporal changes and action-relevant scene structure, and knowledge preservation, which aligns patch-level representations with those of the original foundation model to retain useful pretrained semantics. These objectives yield compact visual state representations that remain semantically meaningful while preserving useful prior knowledge. Experiments across multiple robotics benchmarks show that SPARK consistently improves success rates and generalization over vanilla foundation models, and further demonstrate that these gains transfer to real-world robot manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Compass_1_Towards_Open-World_and_Persistent_Embodied_Navigation_from_Monocular_RGB_Videos|Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos]]

![[assets/2611.12087_first_page.png|800]]

- **arXiv**: [2611.12087](https://arxiv.org/abs/2611.12087)
- **PDF**: https://arxiv.org/pdf/2611.12087
- **详细分析**: [[20_Research/Papers/具身智能/Compass_1_Towards_Open-World_and_Persistent_Embodied_Navigation_from_Monocular_RGB_Videos|Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos]]
- **作者**: Hai Zhang, Siqi Liang, Yanjun Guo, Shoufeng Zhang, Yunhao Wang, Hangyu Du, Haoguang Mai, Hongchen Li, Jiazhi Yang, Jialong Zeng, Yu Hu, Chen Chen...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.4（加权：具身智能 2.1，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Compass 1: Towards Open-World and Persistent Embodied Navigation from Monocular RGB Videos》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied navigation requires agents to achieve persistent spatial awareness and long-horizon execution stability in open-world environments. However, existing navigation architectures struggle to sustain both capabilities, remaining effective only over a handful of recent frames. We present Compass 1, the first embodied navigation foundation model to unify language understanding and video generation while enabling memory backtracking through nearly 2mins of visual history. Without altering the underlying architecture, we introduce History Representation, which integrates sparse visual keyframes with an explicit History Representation Map to preserve long-term spatiotemporal context. To effectively leverage this history, we further introduce History Utilization, a structured VQA supervision protocol comprising three categories: task-stage grounding, exploration consistency, and spatiotemporal target retrieval, enabling map-grounded reasoning and stable persistent long-horizon navigation. To fuel this system, we establish a complete annotation pipeline for monocular RGB videos and open-source a massive dataset featuring over 500 hours of high-quality real-world interactions and over 2,000 hours of annotated web videos. Trained mainly on the distribution of 1m height camera, Compass 1 generalizes seamlessly across diverse embodiments and scenarios, ranging from indoor environments to pedestrian-dense streets, spanning wheeled robot at 0.35m, quadruped dog at 0.5m, humanoid at 0.85m, and aerial drone at 1.5m. Compass 1achieves a dominant overall success rate of 79.4% across open-world evaluations, compared to 17.8% for the strongest baseline. It demonstrates exceptional zero-shot execution exceeding 90% on foundational tasks, a 250% boost in exploration, and an unparalleled leap from 0% to 58% in challenging persistent history backtracking.

</details>

---

### [[20_Research/Papers/机器人/DPGS-SLAM_Diffusion-Prior_and_Provenance-Aware_Monocular_Gaussian_Splatting_SLAM_for_Dynamic_Visual_Sensing|DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing]]

![[assets/2611.12038_figure.png|800]]

- **arXiv**: [2611.12038](https://arxiv.org/abs/2611.12038)
- **PDF**: https://arxiv.org/pdf/2611.12038
- **详细分析**: [[20_Research/Papers/机器人/DPGS-SLAM_Diffusion-Prior_and_Provenance-Aware_Monocular_Gaussian_Splatting_SLAM_for_Dynamic_Visual_Sensing|DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing]]
- **作者**: Yifan Luo, Takafumi Matsumaru, Vibekananda Dutta, Xin He
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《DPGS-SLAM: Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM for Dynamic Visual Sensing》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents DPGS-SLAM (Diffusion-Prior and Provenance-Aware Monocular Gaussian Splatting SLAM) for dense mapping in environments containing dynamic objects. Dynamic observations can contaminate camera tracking and scene reconstruction in visual SLAM (simultaneous localization and mapping). Although 3DGS (3D Gaussian splatting) enables efficient dense mapping, existing 3DGS-SLAM systems may exhibit instability when dynamic objects violate their underlying static-scene assumption. Excluding dynamic observations can reduce their influence on tracking and mapping, but may leave occluded static backgrounds missing or weakly constrained. Our proposed DPGS-SLAM is a monocular RGB SLAM framework that supports provisional representations of insufficiently observed static backgrounds through asynchronous diffusion-based background completion and provenance-aware Gaussian mapping. Dynamic regions are identified through optical-flow-based motion discovery and temporally consistent mask propagation by SAM2 (segment anything model 2). For selected keyframes, a fine-tuned diffusion inpainting model generates plausible background appearance in occluded regions, while Metric3D v2 predicts metric depth from the completed images to initialize provisional Gaussian primitives. Provenance labels distinguish generated primitives from observation-supported primitives, excluding generated content from camera-pose estimation and observed-map optimization. When previously occluded backgrounds become visible, eligible generated primitives are removed, and observation-supported primitives are independently initialized from real RGB observations and predicted depth. Experimental results demonstrated competitive camera tracking, with average ATE RMSE values of 1.2 cm on TUM RGB-D and 2.7 cm on BONN RGB-D. On StaDy4D, DPGS-SLAM improved average PSNR by 4.60 dB over WildGS-SLAM using only monocular RGB input.

</details>

---

### [[20_Research/Papers/世界模型/How_Many_Candidates_Does_a_One-Step_World_Model_Need_A_Random-Codebook_Account_of_Nearest-of-m_Training_on_Frozen_DINO_Tokens|How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens]]

![[assets/2611.11887_figure.png|800]]

- **arXiv**: [2611.11887](https://arxiv.org/abs/2611.11887)
- **PDF**: https://arxiv.org/pdf/2611.11887
- **详细分析**: [[20_Research/Papers/世界模型/How_Many_Candidates_Does_a_One-Step_World_Model_Need_A_Random-Codebook_Account_of_Nearest-of-m_Training_on_Frozen_DINO_Tokens|How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens]]
- **作者**: Yong Hwi Song, Keon Myung Lee
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《How Many Candidates Does a One-Step World Model Need? A Random-Codebook Account of Nearest-of-m Training on Frozen DINO Tokens》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

One-step stochastic world models avoid the mode averaging of deterministic feature predictors without the tens of network evaluations per step that diffusion and flow matching require. The simplest such objective is nearest-of-m matching (conditional implicit maximum likelihood estimation, IMLE): draw m candidate futures and pull only the one closest to the observed outcome. Recent work conjectures that a small m suffices for feature-space world models and that a strictly proper energy score should replace the hard minimum. We test both claims with one-step world models on frozen DINOv2/v3 patch tokens, using benchmarks whose futures can be enumerated. Under mode-like uncertainty, nearest-of-m with m=16 covers the enumerated futures better than 50-step flow matching (at about 1/30 of its latency), one-step flow generators and an energy-score generator at matched parameter counts, and its rollouts stay on the token manifold where flow rollouts drift. One quantity governs the choice of m: the nearest-of-m objective is the expected distortion of a random codebook of m draws from the generator. This view yields three predictions, recorded before the corresponding runs: (i) memorization of the realized outcome in contexts that never repeat, whose strength is governed by the codebook's miss distortion I(m) rather than its miss probability, and which an energy-score generator does not escape by raising m; (ii) a flattening of mode probabilities with m, matching a known optimum within 0.01; and (iii) under-dispersion on continuous high-dimensional outcomes, which bounds the method on real robot video. Per-step matching on self-rollouts cuts long-horizon error by a third on a stochastic Push-T variant; an ablation separates its manifold and coverage benefits. Planning success does not improve despite accurate risk estimates, a negative result we report with its diagnosis.

</details>

---

### [[20_Research/Papers/具身智能/SurgTAP-3D_A_Large-Scale_Cross-Surgery_Video_Dataset_with_Contact-Aware_3D_Motion_Tracking|SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking]]

![[assets/2611.11697_figure.png|800]]

- **arXiv**: [2611.11697](https://arxiv.org/abs/2611.11697)
- **PDF**: https://arxiv.org/pdf/2611.11697
- **详细分析**: [[20_Research/Papers/具身智能/SurgTAP-3D_A_Large-Scale_Cross-Surgery_Video_Dataset_with_Contact-Aware_3D_Motion_Tracking|SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking]]
- **作者**: Jiaxin Guo, Wenzhen Dong, Taoyu Wu, Haomin Kuang, Mengya Xu, Kejian Shi, Ziyi Wang, Tongfan Guan, Mingkai Jia, Yue Wang, Qi Dou, Yun-Hui Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.1，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《SurgTAP-3D: A Large-Scale Cross-Surgery Video Dataset with Contact-Aware 3D Motion Tracking》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding 3D scene dynamics in minimally invasive surgery (MIS) is a fundamental step toward physically intelligent and autonomous surgical systems. However, existing public datasets offer limited scalability and diversity in real-world clinical scenarios. Moreover, annotations typically focus on either tissue or instruments alone, overlooking tool-tissue interactions. This gap limits applications such as augmented reality guidance and autonomous surgery driven by vision-language-action (VLA) models or world models, which demand large-scale, high-quality 3D supervision. In this work, we construct SurgTAP-3D, a large-scale in-vivo pseudo-3D surgical motion tracking dataset and benchmark, comprising 520K frames, 4,549 action clips, and 1.4M 2D/3D point trajectories from diverse robotic and manual procedures under unified action categories. To make annotation scalable, we design a unified framework for surgical 3D point tracking that converts uncalibrated monocular surgical videos into structured 4D annotations through contact-region prompting, active-tool segmentation, dynamic bundle adjustment, and global 4D refinement. This pipeline adapts foundation priors to surgical videos and produces temporally consistent trajectories, pseudo-scale geometry, camera poses, and instrument masks. The dataset captures realistic challenges inherent to surgical environments, including occlusions, smoke, bleeding, and rapid instrument motion. We establish a comprehensive benchmark on SurgPose, SurgT, and STIR, covering both instrument and tissue tracking. We demonstrate instrument displacement estimation, deformable surface reconstruction, and foundation-model fine-tuning. Extensive experiments and analysis demonstrate the effectiveness of our dataset and annotation framework for 3D surgical point tracking, reconstruction, and surgical action understanding. Homepage: https://wrld.github.io/surgtap-3d/

</details>

---

### [[20_Research/Papers/具身智能/From_Game_Generation_to_Game_Playing_Fully_Automated_Ability_Training_for_Vision-Language-Action_Models|From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models]]

![[assets/2611.11136_figure.png|800]]

- **arXiv**: [2611.11136](https://arxiv.org/abs/2611.11136)
- **PDF**: https://arxiv.org/pdf/2611.11136
- **详细分析**: [[20_Research/Papers/具身智能/From_Game_Generation_to_Game_Playing_Fully_Automated_Ability_Training_for_Vision-Language-Action_Models|From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models]]
- **作者**: Changran Liu, Qi Wu, Wenchao Ma, Sharon X. Huang, Haomiao Jiang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《From Game Generation to Game Playing: Fully Automated Ability Training for Vision-Language-Action Models》归入 具身智能、大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GameWorld, VideoGameBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training vision-language-action (VLA) models to follow gameplay instructions across diverse games is limited by the cost of collecting demonstrations. We introduce a framework that automatically generates game environments and expert demonstrations. An LLM-powered agent uses game-building tools to construct executable environments and tasks targeting specified skills. Programmatic experts then use privileged simulator state to generate aligned instructions, rendered observations, and keyboard and mouse actions. We train our game policy, Script2Play, by post-training a 4B vision-language model with behavior cloning on 150.3 hours of synthetic Minecraft and Roblox gameplay, without human gameplay demonstrations or reinforcement learning. Evaluation on multiple public game benchmarks demonstrates that Script2Play follows gameplay instructions effectively and generalizes across game engines, highlighting the effectiveness of targeted synthetic supervision.

</details>

---

### [[20_Research/Papers/具身智能/HARP-Bench_Benchmarking_Robot_Manipulation_Around_Active_Humans|HARP-Bench: Benchmarking Robot Manipulation Around Active Humans]]

![[assets/2611.11123_figure.png|800]]

- **arXiv**: [2611.11123](https://arxiv.org/abs/2611.11123)
- **PDF**: https://arxiv.org/pdf/2611.11123
- **详细分析**: [[20_Research/Papers/具身智能/HARP-Bench_Benchmarking_Robot_Manipulation_Around_Active_Humans|HARP-Bench: Benchmarking Robot Manipulation Around Active Humans]]
- **作者**: Qinhong Zhou, Riley Zong, Chunru Lin, Diyi Hu, Shivraj Singh Bhatti, Hongxin Zhang, Lin Qiu, Hanqing Zeng, Chuang Gan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HARP-Bench: Benchmarking Robot Manipulation Around Active Humans》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HARP-Bench, HR-Gym, Real-World, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent robot manipulation benchmarks have enabled systematic evaluation of general-purpose robot policies across diverse objects, scenes, instructions, and embodiments. However, most existing benchmarks still assume that the robot is the only active agent and that task semantics are determined primarily by the instruction and object state. This assumption overlooks a common source of real-world variation: humans actively sharing the workspace. In such settings, humans may reveal an implicit goal, complete part of the task, temporarily change object availability, or constrain safe robot motion while working nearby. We introduce HARP-Bench, a benchmark for evaluating robot manipulation policies in workspaces shared with active humans. HARP-Bench treats human activity as part of the manipulation problem, rather than as background scene variation. It organizes human-present manipulation into four conditions: Cueing, Contribution, Interruption, and Co-presence. These conditions are instantiated through everyday manipulation tasks, including paired human-present variants for controlled comparison with standard manipulation. HARP-Bench also provides a demonstration-generation pipeline for dynamic human-present settings. We evaluate VLA models, imitation-learning methods, and heuristic policies on HARP-Bench. Human-present variations challenge current policies, and higher task success does not consistently improve safety. Quantitative failure analysis identifies manipulation and recovery as the dominant remaining challenges. Training with HARP-Bench demonstrations improves human-present performance in simulation. A real-world study on one task family shows improved performance under human contribution, but not interruption, providing initial evidence of the data's utility and identifying limits of transfer. Code is available at https://github.com/UMass-Embodied-AGI/harp.

</details>

---

### [[20_Research/Papers/机器人/EmbodiedIntentBench_Benchmarking_Intent-Driven_Runtime_Adaptation_for_Mobile_Robotic_Missions|EmbodiedIntentBench: Benchmarking Intent-Driven Runtime Adaptation for Mobile Robotic Missions]]

![[assets/2611.10498_figure.png|800]]

- **arXiv**: [2611.10498](https://arxiv.org/abs/2611.10498)
- **PDF**: https://arxiv.org/pdf/2611.10498
- **详细分析**: [[20_Research/Papers/机器人/EmbodiedIntentBench_Benchmarking_Intent-Driven_Runtime_Adaptation_for_Mobile_Robotic_Missions|EmbodiedIntentBench: Benchmarking Intent-Driven Runtime Adaptation for Mobile Robotic Missions]]
- **作者**: Rajat Bhattacharjya, Changwoon Lee, Hyeonjong Ju, Sing-Yao Wu, Hamidreza Alikhani, Zhuoyi Yang, Ian Harris, Nalini Venkatasubramanian, Nikil Dutt
- **cs 子类**: cs.CV, cs.DC, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《EmbodiedIntentBench: Benchmarking Intent-Driven Runtime Adaptation for Mobile Robotic Missions》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EmbodiedIntentBench, MAVBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robotic sensing systems must adapt to operator requirements, limited resources, changing connectivity, and observation opportunities shaped by physical motion. Evaluating runtime strategies therefore requires assessing whether their decisions fulfill mission objectives, beyond isolated perception accuracy or execution efficiency. We present EmbodiedIntentBench, a benchmark for intent-driven runtime adaptation in mobile robotic missions. It represents mission intent through structured contracts for coverage, temporal evidence, reporting, urgency, and resources, and couples simulated unmanned aerial vehicle (UAV) workloads with causal, resource-accounted execution. Computation decisions affect mission time, resource use, and which observations can contribute evidence. We evaluate fixed and adaptive perception strategies in multi-phase missions and under changing urgency, connectivity, and battery conditions. In the multi-phase Depot study, a configuration with 87.5% full-bank target recall across visible target observations completes only 1 of 16 missions, whereas a lower-recall configuration completes 14. In an ablation, ignoring execution-induced observation loss increases aggregate mission success and reverses the ordering of two runtime strategies. Replays using Jetson AGX Orin CPU and GPU profiles change the relative success of local and remote strategies. In selected Jetson GPU-profile replays, intent-driven adaptation reduces modeled task energy by up to 28% with unchanged mission success. EmbodiedIntentBench provides an extensible framework for evaluating runtime decisions against mission fulfillment under physical and resource constraints.

</details>

---

### [[20_Research/Papers/具身智能/How_Many_Demonstrations_Does_a_VLA_Need_On_the_Sample_Efficiency_of_VLA_Finetuning|How Many Demonstrations Does a VLA Need? On the Sample Efficiency of VLA Finetuning]]

![[assets/2611.09964_first_page.png|800]]

- **arXiv**: [2611.09964](https://arxiv.org/abs/2611.09964)
- **PDF**: https://arxiv.org/pdf/2611.09964
- **详细分析**: [[20_Research/Papers/具身智能/How_Many_Demonstrations_Does_a_VLA_Need_On_the_Sample_Efficiency_of_VLA_Finetuning|How Many Demonstrations Does a VLA Need? On the Sample Efficiency of VLA Finetuning]]
- **作者**: Rahul Chand, Miguel Villa Floran
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《How Many Demonstrations Does a VLA Need? On the Sample Efficiency of VLA Finetuning》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision language action (VLA) models show strong zero-shot performance, but are rarely deployed directly and are often first post-trained on demonstrations from the target setting. Yet VLAs are typically compared by zero-shot or full-data fine-tuned success, revealing little about the data and compute required for adaptation. We study adaptation efficiency for six VLAs ($π_{0}$, $π_{0.5}$, and GR00T N1-N1.7) on four LIBERO suites, varying both demonstrations and training steps. This reveals differences hidden by full-data fine-tuning: models within two points on the full LIBERO-Spatial dataset differ by up to $3\times$ in success with 50 demonstrations. $π_{0.5}$ needs $2$--$5\times$ fewer demonstrations than $π_{0}$ and is the most sample-efficient model at every budget, with the largest gap on the long-horizon suite. Within GR00T, N1.5 adapts more efficiently than N1.6 and N1.7 on three of four suites, despite their stronger zero-shot performance. We study one pretraining factor behind these differences by freezing the VLM during finetuning: this severely degrades the $π$ models, whose VLM is jointly trained with the action expert during pretraining, but barely affects GR00T models. Finally, validation loss on held-out demonstrations tracks closed-loop success within a suite, but understates how much more sample-efficient $π_{0.5}$ is than $π_{0}$.

</details>

---
