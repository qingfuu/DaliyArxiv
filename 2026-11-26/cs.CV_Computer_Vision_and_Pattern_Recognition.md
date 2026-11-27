# cs.CV | Computer Vision and Pattern Recognition | 2026-11-26

#arxiv #ComputerScience

**论文数**: 21

### [[20_Research/Papers/具身智能/Cairn_Object-Centric_3D_Trajectory_Priors_for_Steering_Frozen_VLAs|Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs]]

![[assets/2611.34914_figure.png|800]]

- **arXiv**: [2611.34914](https://arxiv.org/abs/2611.34914)
- **PDF**: https://arxiv.org/pdf/2611.34914
- **详细分析**: [[20_Research/Papers/具身智能/Cairn_Object-Centric_3D_Trajectory_Priors_for_Steering_Frozen_VLAs|Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs]]
- **作者**: Agelos Kratimenos, Kostas Daniilidis, Evangelos Chatzipantazis
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Cairn: Object-Centric 3D Trajectory Priors for Steering Frozen VLAs》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) are capable low-level controllers, but they tie where objects go to the layouts they were trained on: when objects are moved or obstacles block the way, they carry them to the wrong place or into collisions. Fine-tuning on new layouts needs robot data for each one and erodes skills the model already has. We introduce Cairn, which keeps the VLA frozen and steers it at test time along learned 3D trajectories of the object in its gripper. A small prior reads point clouds of the scene and the held object, along with its pose when grasped and the instruction, and samples SE(3) trajectories up to its release that lead it around obstacles and turn it to fit through gaps. The prior and the VLA form the two levels of a hierarchical planner in which feedback runs both ways: the VLA's intended motion chooses and reshapes the trajectories, and the chosen one guides the VLA's denoising. Its predicted actions, mapped to the held object's poses through the grasp, are pulled toward the next waypoint, while the VLA's weights stay untouched. Across 1,941 held-out LIBERO scenes with displaced objects and obstacles, Cairn raises the success rate of a frozen π0.5 from 24.5% to 95.1%, above that of a π0.5 fine-tuned on our training layouts, without hurting standard LIBERO. On the third-party LIBERO-PRO benchmark, it raises success from 27.3% to 38.0%, and from 54.4% to 81.1% on the episodes it steers. On a real Franka, with a prior trained purely in simulation, it guides the frozen DROID π0.5 around an obstacle and to a placement at the limit of the arm's reach, where it otherwise fails. All code, models and data will be made public.

</details>

---

### [[20_Research/Papers/机器人/FineDex_Bridging_Fine-Grained_Human-Object_Interaction_Generation_to_Dexterous_Humanoid_Manipulation|FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation]]

![[assets/2611.34884_figure.png|800]]

- **arXiv**: [2611.34884](https://arxiv.org/abs/2611.34884)
- **PDF**: https://arxiv.org/pdf/2611.34884
- **详细分析**: [[20_Research/Papers/机器人/FineDex_Bridging_Fine-Grained_Human-Object_Interaction_Generation_to_Dexterous_Humanoid_Manipulation|FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation]]
- **作者**: Yujia Zeng, Yuxin Chen, Yuzhen Song, Runhan Huang, Chensheng Peng, Yiyang Shao, Koushil Sreenath, Masayoshi Tomizuka, Yilun Du
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.1（加权：具身智能 2.7，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《FineDex: Bridging Fine-Grained Human-Object Interaction Generation to Dexterous Humanoid Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FingerBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterity is, at its core, finger-level control, yet existing dexterous manipulation and human-object interaction (HOI) generation methods rarely let one specify how an interaction is performed: five-fingered hands are often reduced to grippers, or finger usage is copied from individual human demonstrations. We present FineDex, a framework that makes finger-level intent both expressible and executable. FineDex learns coordinated human body, hand, and object motions that follow fine-grained instructions on hand selection, individual fingers, and contacts with articulated objects. To bridge generation and execution, FineDex leverages generated interactions as actionable priors for an agent that discovers physically feasible contact strategies through practice in a physics-based digital twin. By adapting at test time without per-instance retraining, FineDex generalizes across fine-grained instructions and object configurations. Experiments demonstrate state-of-the-art HOI generation quality and fine-grained controllability, substantial improvements in dexterous manipulation success, and successful deployment on a real dexterous humanoid robot.

</details>

---

### [[20_Research/Papers/具身智能/SOLVE_Sparse,_Ordered_Keyposes_Make_LLM_Agents_Versatile_and_Efficient_Robot_Manipulator|SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator]]

![[assets/2611.34750_figure.png|800]]

- **arXiv**: [2611.34750](https://arxiv.org/abs/2611.34750)
- **PDF**: https://arxiv.org/pdf/2611.34750
- **详细分析**: [[20_Research/Papers/具身智能/SOLVE_Sparse,_Ordered_Keyposes_Make_LLM_Agents_Versatile_and_Efficient_Robot_Manipulator|SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator]]
- **作者**: Xiang Li, Hongyu Zhou, Ya-Li Li, Tao Li, Rui Zhang, Junjie Lai, Weihua Zhang, Shengjin Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.6，大模型 1，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《SOLVE: Sparse, Ordered Keyposes Make LLM Agents Versatile and Efficient Robot Manipulator》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RoboDojo-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LLM agents have made remarkable progress in robot manipulation, yet they suffer from expensive inference, dense step-by-step control, and tool bottlenecks. We introduce SOLVE, a training-free, versatile and efficient agent policy: a multimodal LLM agent writes a sparse, ordered sequence of 6-DoF end-effector keyposes per call, observes the result, and writes the next, while a motion planner interpolates between them. The agent decides the number and spacing of keyposes for both fast long-range motion and fine-grained manipulation. This granularity matches the sparsity of teleoperated manipulation: most demonstrations in DROID can be compressed into a few keyposes instead of dense actions. SOLVE grounds keyposes with sparse depth queries answered by noisy sources, such as multi-view triangulation, stereo, or monocular depth, and copes with that noise itself. It also improves from execution feedback, reflecting on its own rollouts and distilling a few rules per task. SOLVE reaches state-of-the-art performance of 74.5% on RoboDojo and 84.5% on RoboLab, with only $1.7 per episode on average, 12x less than previous dense-control agent policies. On a real robot, the same agent achieves an 88% success rate (75 of 85 episodes) over 16 challenging zero-shot tasks. Our project page is at https://serenos.github.io/solve-website.

</details>

---

### [[20_Research/Papers/具身智能/Was_the_Model_Given_the_Right_Action_Auditing_and_Repairing_Action_Interfaces_in_Navigation_World_Models|Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models]]

![[assets/2611.34739_figure.png|800]]

- **arXiv**: [2611.34739](https://arxiv.org/abs/2611.34739)
- **PDF**: https://arxiv.org/pdf/2611.34739
- **详细分析**: [[20_Research/Papers/具身智能/Was_the_Model_Given_the_Right_Action_Auditing_and_Repairing_Action_Interfaces_in_Navigation_World_Models|Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models]]
- **作者**: Ajmain Istiak Apon, Md Mehedi Hasan, Sejuti Rahman
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: EmbodiedAI, WorldModel

#### 研究背景与动机

《Was the Model Given the Right Action? Auditing and Repairing Action Interfaces in Navigation World Models》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ActionFaultBench, DreamSim, DrivingWorld, MiraBench, Vid2World, World-in-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are evaluated by predicting future observations from actions. These evaluations assume that actions are prepared the same way as during training, but an unchecked mismatch can make a model appear less accurate than it is. We audit this assumption in Navigation World Models (NWM) and find three interacting differences between its training and rollout code. Correcting the inputs, without retraining, reduces mean visual prediction error by 42%, measured with DreamSim on the RECON navigation dataset. The correction also changes the ranking of NWM checkpoints in an exploratory analysis and removes or reduces two alternative models' measured advantages. Correcting only the normalization offset instead increases error, showing why interacting mismatches must be checked together. To test whether sensitivity to input preparation extends beyond NWM, we deliberately introduce encoding errors into two alternative models; both become less accurate. We introduce ActRosetta, a tool that checks whether action encoding matches training, identifies supported causes of disagreement, and repairs inputs when sufficient information is available. Repair helps little where predictions barely respond to actions, the tool's diagnosis has limited coverage, and improved control remains unproven. For any action-conditioned world model, the lesson is the same: before reporting rollout error, verify that evaluation encodes actions exactly as training did.

</details>

---

### [[20_Research/Papers/具身智能/Commit2Drive_Perception-Grounded_Language_Decisions_as_Commitments_for_Trajectory_Planning_in_Vision-Language-Action_Driving_Models|Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models]]

![[assets/2611.34614_figure.png|800]]

- **arXiv**: [2611.34614](https://arxiv.org/abs/2611.34614)
- **PDF**: https://arxiv.org/pdf/2611.34614
- **详细分析**: [[20_Research/Papers/具身智能/Commit2Drive_Perception-Grounded_Language_Decisions_as_Commitments_for_Trajectory_Planning_in_Vision-Language-Action_Driving_Models|Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models]]
- **作者**: Zikai Zhang, Hubert P. Shum, Toby Breckon
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.5，大模型 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Commit2Drive: Perception-Grounded Language Decisions as Commitments for Trajectory Planning in Vision-Language-Action Driving Models》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AutoVLA, CF-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models introduce language reasoning into end-to-end autonomous driving. They output a language decision together with a trajectory, which makes the planner more interpretable. However, in existing methods the language decision is either an independent output or an index that selects among similar candidate trajectories, and its annotations are not verified against the trajectory. As a result, the language decision and the trajectory are often inconsistent in closed-loop driving. To address this, we propose Commit2Drive, a framework that imposes the language decision as a consistency constraint on trajectory planning. The decision is a commitment, a maneuver class with a continuous parameter that one deterministic rule reads from any trajectory, and it is grounded in facts reported by the perception of the model itself. A Maneuver Bank maps the commitment to a code with a kinematic meaning, and consistency losses train the planner to execute every admissible decision of a scene, so that the trajectory follows the decision. An automatic data pipeline supplies the supervision. Decisions are labeled from the future motion of the expert, counterfactual executions train the decision and the trajectory together, and rule-based functions with a Vision-Language Model (VLM) generate, review and refine the language annotations. The code is a lookup that involves no hidden state of the language model, so Commit2Drive is extensible to rule-based decisions, which the same planner executes without retraining. Commit2Drive uses a 0.5B language model and runs closed-loop inference online on a single consumer graphics card. On Bench2Drive, Commit2Drive reaches a Driving Score (DS) of 78.50 and a Success Rate (SR) of 55.91% with a lightweight model, which is competitive with the state of the art, and greatly reduces the language-action inconsistency. Code will be released soon.

</details>

---

### [[20_Research/Papers/世界模型/$μ$MPC_Microsecond-Scale_Nonlinear_and_World_Model_Control_from_Edge_to_GPU_via_Koopman-Linearized_Precompilation|$μ$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation]]

![[assets/2611.34597_figure.png|800]]

- **arXiv**: [2611.34597](https://arxiv.org/abs/2611.34597)
- **PDF**: https://arxiv.org/pdf/2611.34597
- **详细分析**: [[20_Research/Papers/世界模型/$μ$MPC_Microsecond-Scale_Nonlinear_and_World_Model_Control_from_Edge_to_GPU_via_Koopman-Linearized_Precompilation|$μ$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation]]
- **作者**: Devesh Nath, Glen Chou
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《$μ$MPC: Microsecond-Scale Nonlinear and World Model Control from Edge to GPU via Koopman-Linearized Precompilation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present $μ$MPC, a fast model predictive control (MPC) framework that reduces online computation using learned Koopman-linearized dynamics. By precomputing finite-horizon control-to-output maps, $μ$MPC eliminates lifted-state trajectories, yielding an action-only Koopman-Compiled QP (KC-QP) with $Hn_u$ decision variables, independent of lifted dimension. A fixed, precomputed primal operator enables efficient primal-dual iterations using only matrix-vector products and projections, accommodating changing goals and constraints without refactorization. This efficiency also enables control-aware dynamics learning through differentiable KC-QPs in the training loop and batched DAgger-style data aggregation. $μ$MPC achieves solve times as low as $23μ$s on a desktop CPU and 24 ms onboard a 168 MHz Crazyflie microcontroller. It scales to 4096D quadruped control in under 5 ms, visual planning with 2048D world models in 0.4 ms, and collision-aware planning for 200 quadrotors at over 30 Hz on the GPU. Across these benchmarks, $μ$MPC achieves up to $108\times$ faster constrained MPC and $1907\times$ faster visuomotor planning than competing methods.

</details>

---

### [[20_Research/Papers/具身智能/M$^{2}$AdaptVLA_Multimodal_Memory-Augmented_Vision-Language-Action_Model_with_Predictive_Test-Time_Adaptation|M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation]]

![[assets/2611.34560_figure.png|800]]

- **arXiv**: [2611.34560](https://arxiv.org/abs/2611.34560)
- **PDF**: https://arxiv.org/pdf/2611.34560
- **详细分析**: [[20_Research/Papers/具身智能/M$^{2}$AdaptVLA_Multimodal_Memory-Augmented_Vision-Language-Action_Model_with_Predictive_Test-Time_Adaptation|M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation]]
- **作者**: Liufan Tan, Tong Wang, Yuehao Yin, Jian Chen, Yihang Yin, Ying Qu, Wenyu Li, Ruyi Gan, Hao Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.8，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《M$^{2}$AdaptVLA: Multimodal Memory-Augmented Vision-Language-Action Model with Predictive Test-Time Adaptation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AdaptVLA, DAM-VLA, DeltaNet, EventVLA, FM-VLA, M2AdaptVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective robotic manipulation calls for multimodal memory and rapid adaptation to shifts in contact dynamics. However, many existing policies, which retain either visual or wrench history, may miss key cues from the other modality. Moreover, even with wrench memory, fixed policies can struggle when contact conditions shift at deployment. To this end, we introduce M$^{2}$AdaptVLA, a vision-language-action model that integrates visual and wrench memories with predictive test-time adaptation. For visual memory, the model uses test-time training (TTT) to encode observation history in fast weights. Each entry in the bounded TTT bank combines the corresponding frame's features with a readout from these weights, preserving cues that predate the oldest retained frame. For wrench memory, a context gate controls how much the action expert draws on wrench history as it jointly denoises future actions and wrenches. For predictive test-time adaptation, the auxiliary wrench prediction loss also provides online self-supervision. Using measured wrenches as targets, we update low-rank policy adapters by backpropagating only through the final denoising step. Real-world experiments show that the TTT bank outperforms visual memory baselines on progress tracking, scene recall, and demonstration following. On contact-sensitive tasks, the context gate yields higher success rates than direct injection or gated cross-attention. Predictive test-time adaptation improves robustness to shifts in contact dynamics. On eight tasks requiring visual and wrench memory, M$^{2}$AdaptVLA achieves a mean success rate of 82.71%, a 31.46% absolute gain over the strongest baseline. The project page is available at https://tlf-tlf.github.io/M2AdaptVLAPage/.

</details>

---

### [[20_Research/Papers/具身智能/Can_Visual_World_Models_See_Force|Can Visual World Models See Force?]]

![[assets/2611.34422_figure.png|800]]

- **arXiv**: [2611.34422](https://arxiv.org/abs/2611.34422)
- **PDF**: https://arxiv.org/pdf/2611.34422
- **详细分析**: [[20_Research/Papers/具身智能/Can_Visual_World_Models_See_Force|Can Visual World Models See Force?]]
- **作者**: Felix Tristram, Benjamin D. Killeen, Nassir Navab
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 0.9，世界模型 0.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Can Visual World Models See Force?》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：FD-VLA, OpenVLA, TA-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models and vision-language-action policy models are increasingly proposed as foundations for robot manipulation. They predict how scenes evolve and which actions to take, yet successful manipulation depends not solely on following observable trajectories but also on the hidden variable of interaction force. Neurophysiology has shown that humans possess a visual prior for this hidden variable, motivating us to ask the question: Do the representations of visual foundation models also capture the forces involved in an interaction? We define force awareness as the ability of representations to (1) indicate when contact force is applied, (2) track how it changes during an interaction, and (3) reflect how large it is. We probe frozen image, video, world- and policy model representations with a lightweight readout trained on synchronized video and force measurements from two manipulation datasets. Our experiments show that most models capture when contact occurs but not how much force is being applied. Surprisingly, robot post-training does not improve this either, highlighting an important gap in current models capabilities.

</details>

---

### [[20_Research/Papers/具身智能/One_Patch,_Many_Policies_Object-Associated_Physical_Patch_Attacks_on_Robotic_Manipulation|One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation]]

![[assets/2611.34360_figure.png|800]]

- **arXiv**: [2611.34360](https://arxiv.org/abs/2611.34360)
- **PDF**: https://arxiv.org/pdf/2611.34360
- **详细分析**: [[20_Research/Papers/具身智能/One_Patch,_Many_Policies_Object-Associated_Physical_Patch_Attacks_on_Robotic_Manipulation|One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation]]
- **作者**: Yiqian Liu, Yuqi Lin, Hui Lu, Jiaming He, Qi Zhu, Deyi Ji, Bing Li, Kaizheng Wang, Zhiyuan Zha, Yi Yu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.5，机器人 0.6）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《One Patch, Many Policies: Object-Associated Physical Patch Attacks on Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) and World Action Models (WAMs) are vulnerable to adversarial visual interference, motivating the study of universal and transferable physical patch attacks. We propose Object-Associated Patch Attack (OAPA), a universal and transferable physical patch framework that enables an attacker to select which task object's manipulation to disrupt through patch placement, without re-optimizing the patch. Our framework combines object-associated placement, differentiable physical compositing, and final action-expert representation divergence. Physical compositing accounts for perspective and occlusion across camera views, while representation divergence guides patch optimization using either relative RMS or cosine distance. Experimental results demonstrate strong attack transferability across task suites and policies, together with the ability to selectively disrupt manipulation of an attacker-chosen task object through patch placement.

</details>

---

### [[20_Research/Papers/具身智能/AIRIS_Benchmarking_Social_Embodied_Intelligence_in_Egocentric_Streaming_Videos|AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos]]

![[assets/2611.34347_figure.png|800]]

- **arXiv**: [2611.34347](https://arxiv.org/abs/2611.34347)
- **PDF**: https://arxiv.org/pdf/2611.34347
- **详细分析**: [[20_Research/Papers/具身智能/AIRIS_Benchmarking_Social_Embodied_Intelligence_in_Egocentric_Streaming_Videos|AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos]]
- **作者**: Yuchen Zhou, Hongsheng Wu, Jiayu Tang, Yunxuan Mao, Hanjing Ye, Shenghao Zhang, Jing Tang, Chun-Kai Fan, Yufei Huang, Yonggen Ling, He Zhang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《AIRIS: Benchmarking Social Embodied Intelligence in Egocentric Streaming Videos》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ESTP-Bench, GRASP-Bench, IPIBench, OVO-Bench, ProactiveVideoQA, RTV-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents operating around people must not only recognize social cues, but also decide when the available evidence is sufficient, whether to intervene, and how to respond without violating social norms. Existing benchmarks typically evaluate these abilities in isolation or with access to completed videos, obscuring where an online social decision fails. We introduce AIRIS, a causal streaming benchmark that formulates social embodied intelligence as a time-anchored chain of Attention, Intention, Reaction, and Interaction (A-I-R-I). AIRIS contains 8,000 expert-curated questions grounded in 357 egocentric clips across 11 context categories and 36 capability dimensions. At each query, models receive only the observation prefix available at that time; decision-aware metrics reward calibrated waiting and complete reactions while penalizing premature commitment. Evaluating 45 proprietary and open-source general-purpose, embodied, streaming-video, and omni-modal models reveals fragmented and temporally miscalibrated competence. General-purpose VLMs excel at passive cue grounding and intent recognition, whereas embodied specialists lead on isolated reaction sub-decisions; yet across all families, models frequently guess intents before sufficient evidence emerges and fail to jointly align intervention timing, action domain, and concrete execution within the same episode. AIRIS thus provides a diagnostic foundation for bridging the gap between passive social perception and reliable embodied interaction.

</details>

---

### [[20_Research/Papers/具身智能/Rehearse_in_3D,_Render_in_2D_Physically_Consistent_and_Editable_Robot_World_Models|Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models]]

![[assets/2611.34288_figure.png|800]]

- **arXiv**: [2611.34288](https://arxiv.org/abs/2611.34288)
- **PDF**: https://arxiv.org/pdf/2611.34288
- **详细分析**: [[20_Research/Papers/具身智能/Rehearse_in_3D,_Render_in_2D_Physically_Consistent_and_Editable_Robot_World_Models|Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models]]
- **作者**: Guangyu Liu, Hanzhang Wang, Huijia Zhang, Hanbei Zhan, Linjie Hu, Bin Xiao, Xuan Zhou, Dong Zhang, Hanwei Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 3.0（加权：具身智能 0.9，世界模型 1，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Rehearse in 3D, Render in 2D: Physically Consistent and Editable Robot World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, PointWorld, RehearsalWorld, UniSim, WorldGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied world models aim to predict future interactions that are both visually realistic and physically consistent. Yet explicit 3D motion prediction alone does not guarantee that object structure and contact relationships are preserved. Beyond motion prediction, 3D representations provide an explicit state space for imposing structural and physical constraints. Building on this insight, we introduce RehearsalWorld, an editable robot world model driven by 3D Interaction Rehearsal (3DIR). Given an initial RGB-D observation and robot actions, Interaction-Consistent Rehearsal (ICR) uses a pretrained 3D point-flow model as a motion prior. It refines the predicted trajectories through response-aware object grouping, persistent grasp memory, and contact structure refiner, preserving scene stability, object structure, and grasp attachments. Rehearsal-Aligned Video Generation (RAVG) then uses geometric projections of the rehearsal as temporal conditioning. We fine-tune a video generator on projection-video pairs to synthesize realistic interaction videos. Thanks to the decoupling of physical response from visual synthesis, RehearsalWorld also supports independent editing of material properties and camera viewpoints. Compared with PointWorld on real DROID grasping sequences, RehearsalWorld reduces gripper-relative offset by approximately 79% to 84% across deformable, articulated, and rigid objects and lowers reference motion error. For video prediction, it achieves a PSNR of 23.92 dB and an FVD of 149.

</details>

---

### [[20_Research/Papers/具身智能/Loop4D_Embodied_World_Modeling_with_4D_VAEs_and_Looped_Diffusion_Transformers|Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers]]

![[assets/2611.34199_figure.png|800]]

- **arXiv**: [2611.34199](https://arxiv.org/abs/2611.34199)
- **PDF**: https://arxiv.org/pdf/2611.34199
- **详细分析**: [[20_Research/Papers/具身智能/Loop4D_Embodied_World_Modeling_with_4D_VAEs_and_Looped_Diffusion_Transformers|Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers]]
- **作者**: Gen Li, Fan Luo, Mengjun Lin, Shu Han, Bohan Li, Hao Zhao
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 1.2，机器人 0.4）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Loop4D: Embodied World Modeling with 4D VAEs and Looped Diffusion Transformers》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting the outcomes of robotic manipulation requires modeling both visual appearance and evolving 3D geometry. This poses two challenges: video compression can obscure fine-grained robot motion, while jointly predicting RGB and geometry demands sufficient generative capacity. We introduce Loop4D, a framework that addresses these challenges through motion-preserving 4D representations and recurrent generative refinement. Our 4D VAE encodes RGB and pointmap sequences into compact spatiotemporal latents while preserving motion details and geometric structure. Our RGB VAE combines geometry-guided supervision with predictive reconstruction to reduce compression-induced motion artifacts. Our geometry VAE uses lightweight adapters to adapt pretrained RGB representations while preserving their priors. Building on these representations, our Dual-Stream Looped Diffusion Transformer maintains separate appearance and geometry streams with shared Transformer weights and cross-modal connections. By reusing Transformer blocks across loops, we increase effective depth without replicating backbone parameters, enabling models with fewer parameters to improve joint RGB-geometry prediction through additional computation. Experiments demonstrate high-quality 4D generation and validate Loop4D in simulated robotic manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/A_Simple_Yet_Effective_Agent_for_Open-World_Aerial_Object_Search|A Simple Yet Effective Agent for Open-World Aerial Object Search]]

![[assets/2611.34115_figure.png|800]]

- **arXiv**: [2611.34115](https://arxiv.org/abs/2611.34115)
- **PDF**: https://arxiv.org/pdf/2611.34115
- **详细分析**: [[20_Research/Papers/具身智能/A_Simple_Yet_Effective_Agent_for_Open-World_Aerial_Object_Search|A Simple Yet Effective Agent for Open-World Aerial Object Search]]
- **作者**: Jitai Hao, Liangxing Yang, Zhenyang Li, Fan Liu, Qiang Huang, Jun Yu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能, 世界模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.7，世界模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《A Simple Yet Effective Agent for Open-World Aerial Object Search》归入 大模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Open-World, SearchWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-world aerial object search methods often rely on persistent spatial maps, learned world models, or task-specific policy training. To examine how far a minimal, training-free design can go, we introduce SimpleUAV, an agent built around a frozen, off-the-shelf vision-language model (VLM). SimpleUAV separates current-view target assessment from history-conditioned action selection, combining fresh candidate evidence with lightweight search context. Local geometry converts visual selections into bounded straight-line movements, depth-based checks halt blocked segments, and measured execution feedback guides subsequent decisions. This closed loop sustains search without persistent spatial maps or task-specific training. SimpleUAV achieves 41.61% Success Rate (SR) on UAV-ON and 11.98% on AerialDojo-200K, compared with 23.80% and 3.20% for the strongest prior baselines, respectively. With limited benchmark-specific adaptation, the same core agent transfers to aerial Vision-and-Language Navigation (VLN) on TravelUAV, improving Full SR by at least 19.66% across all three splits under L1 assistance. These results establish a strong baseline for evaluating when additional architectural complexity benefits aerial search.

</details>

---

### [[20_Research/Papers/具身智能/iMFPO_Improving_Mean_Flow_Policy_Optimization_with_Drift-Aware_Velocity_Alignment_for_Embodied_Control|iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control]]

![[assets/2611.33922_figure.png|800]]

- **arXiv**: [2611.33922](https://arxiv.org/abs/2611.33922)
- **PDF**: https://arxiv.org/pdf/2611.33922
- **详细分析**: [[20_Research/Papers/具身智能/iMFPO_Improving_Mean_Flow_Policy_Optimization_with_Drift-Aware_Velocity_Alignment_for_Embodied_Control|iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control]]
- **作者**: Lisiyu Pan, Ting Huang, Zeyu Zhang, Hao Tang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 1，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《iMFPO: Improving Mean Flow Policy Optimization with Drift-Aware Velocity Alignment for Embodied Control》归入 具身智能、强化学习、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-based generative policies offer expressive action modeling for embodied control, yet achieving efficient one-step generation under reward-driven policy optimization remains challenging. In particular, evolving action distributions during online reinforcement learning may introduce inconsistencies between instantaneous-velocity learning and interval-averaged action generation. To address this challenge, we propose iMFPO, a one-step generative policy optimization framework with decoupled velocity learning and drift-aware velocity alignment. A shared interval-conditioned actor supports instantaneous-velocity supervision and interval-averaged action generation. JVP-corrected velocity regression is jointly optimized with reward-driven policy objectives, with action-level guidance from a frozen PPO teacher during training. At inference, iMFPO directly generates actions through interval-averaged velocity prediction, achieving one-step control without iterative flow integration. Across Go2, G1, H1, and Spot, zero-latent evaluation yields mean returns of 35.69, 34.44, 416.23, and 29.86. On Go2, action-generation latency drops from 15.57 ms to 0.41 ms relative to 64-step RFPO. Code: https://github.com/AIGeeksGroup/iMFPO. Website: https://aigeeksgroup.github.io/iMFPO.

</details>

---

### [[20_Research/Papers/具身智能/SEEK_Self-Evolution_through_Execution_Knowledge_for_Agentic_Robot_Manipulation|SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation]]

![[assets/2611.33915_figure.png|800]]

- **arXiv**: [2611.33915](https://arxiv.org/abs/2611.33915)
- **PDF**: https://arxiv.org/pdf/2611.33915
- **详细分析**: [[20_Research/Papers/具身智能/SEEK_Self-Evolution_through_Execution_Knowledge_for_Agentic_Robot_Manipulation|SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation]]
- **作者**: Zeyang Guan, Qihao Zhao, Rui Gong, Zhang Haitian, Yalun Dai, Yangyu Huang, Lingao Xiao, Haozhe Du, Xuehui Yu, Ye Lu, Jianjun Gao, Ruoyu Wang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SEEK: Self-Evolution through Execution Knowledge for Agentic Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose multimodal foundation models enable robots to adapt during deployment from observations and execution feedback, without task-specific demonstrations or training. However, the robot retains what it learns only in the model's working context. Once the task ends, it loses this execution knowledge, such as how to carry a bowl between two grippers. On the next attempt at the task, the robot may take just as long and repeat the same mistakes. To avoid this repetition, robots must retain execution knowledge across attempts. Yet replaying past actions is insufficient, because their effects depend on the current conditions. Procedures that determine actions from the current scene address this, but when they meet conditions that earlier attempts did not cover, revising them requires the measured effects of earlier actions. We therefore propose SEEK, an agentic framework that retains both, enabling robots to improve across attempts while keeping the underlying model fixed. To adapt retained knowledge to the current scene, SEEK adopts a Self-Evolving Programmatic Policy (SEPP) that encodes manipulation as executable procedures and determines each action from current observations. As the robot executes these procedures, SEEK records the measured effects of its actions, including those from failed attempts, in a Persistent Action-Effect Bank (PAEB). Where a retained procedure applies, it acts without a model request; where it meets a condition it does not cover, this evidence guides its revision. On RoboDojo, knowledge retained over ten attempts raises SEEK's average task score from 27.0 to 54.4 and its success rate from 19.7% to 48.0% across all 42 tasks. On 34 of these tasks with GPT-6.2 Astra, SEEK reaches 80.1 after five attempts, against 49.6 for the same model acting directly, and uses 77.6% fewer model requests. https://zeyangguan.github.io/SEEK-Agentic-Robot-Manipulation/

</details>

---

### [[20_Research/Papers/具身智能/Measuring_the_Value_of_One_Shared_Image_at_Robot_Handoffs_in_Vision-and-Language_Navigation|Measuring the Value of One Shared Image at Robot Handoffs in Vision-and-Language Navigation]]

![[assets/2611.33865_figure.png|800]]

- **arXiv**: [2611.33865](https://arxiv.org/abs/2611.33865)
- **PDF**: https://arxiv.org/pdf/2611.33865
- **详细分析**: [[20_Research/Papers/具身智能/Measuring_the_Value_of_One_Shared_Image_at_Robot_Handoffs_in_Vision-and-Language_Navigation|Measuring the Value of One Shared Image at Robot Handoffs in Vision-and-Language Navigation]]
- **作者**: Yuze Lu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Measuring the Value of One Shared Image at Robot Handoffs in Vision-and-Language Navigation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoNavBench, CommNet, IC3Net, SAGE-Bench, V2VNet, YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When the lead robot cannot continue, what should it send the teammate that must finish the route? We replay a frozen receiver at each contact under alternative messages. Across 3,920 autonomous departures in 106 environments, adding the view before the lead's last action block to its executed actions raised success by 7.51 percentage points (pp) per RxR handoff and 8.54 pp per SAGE handoff. Per departure the gains were 2.23 and 1.44 pp, respectively. The lead continuing in simulation defines the empirical full-history ceiling (Solo). At contact, the lead had accumulated a median of 41 frames. Sending one frame when available recovered 24% of the full-history advantage over actions alone in SAGE and 30% in RxR. Over an estimated progress cue in SAGE, the image rescued 100 routes and reversed 54 successes. Near-goal receivers finished outside less often (63.1% to 51.7%, post hoc). In secondary comparisons the earlier view outperformed the contact view by 6-7 pp per handoff. Exact-route specificity and image gains at controlled starts with mostly unknown progress or outside the goal region remained unresolved. Gains were detectable from about 7 kB per handoff. Random transmission matched within size bins nearly equaled the learned sender's team success. At a required handoff, a view of the approach to the last maneuver helps the receiver finish.

</details>

---

### [[20_Research/Papers/世界模型/DuoWM_Integrating_Dual_6-DoF_Visual_Flows_into_Action-Conditioned_Drone_World_Model|DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model]]

![[assets/2611.33779_figure.png|800]]

- **arXiv**: [2611.33779](https://arxiv.org/abs/2611.33779)
- **PDF**: https://arxiv.org/pdf/2611.33779
- **详细分析**: [[20_Research/Papers/世界模型/DuoWM_Integrating_Dual_6-DoF_Visual_Flows_into_Action-Conditioned_Drone_World_Model|DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model]]
- **作者**: Zixuan Li, Kangyao Huang, Meng Xu, Wan Tian, Xiaoyu Tang, Jinge Sun, Yingliang Yao, He Chen, Lingzhong Meng, Yunzhi Xue, Jingyu Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，世界模型 1，机器人 1.1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《DuoWM:Integrating Dual 6-DoF Visual Flows into Action-Conditioned Drone World Model》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video world models generate future observations from an initial frame and a camera trajectory, but often fail to align camera commands with visual dynamics or represent full 6-DoF scene transformations. We present DuoWM, a first-person drone video world model with two complementary visual conditions. Action flow projects future camera positions and orientations into each target frame, while Object flow forward-warps the initial observation and overlays local 6-DoF transformations to ground the induced scene motion. We further introduce transform-aware pretraining, which pairs object appearance with explicit transformation axes before standard RGB video training. On Sekai-drone dataset, DuoWM achieves the best results across video quality, 3D consistency, and trajectory following. Compared with Captain Safari, the state-of-the-art method, our approach reduces real-domain FVD and LPIPS by 17.2\% and 21.6\%, respectively, while improving game-domain AUC@30 from 0.5003 to 0.5719 and AUC@15 from 0.3088 to 0.3747.

</details>

---

### [[20_Research/Papers/大模型/WorldUAV_Scaling_UAV_Data_Synthesis_via_World_Models|WorldUAV: Scaling UAV Data Synthesis via World Models]]

![[assets/2611.33682_figure.png|800]]

- **arXiv**: [2611.33682](https://arxiv.org/abs/2611.33682)
- **PDF**: https://arxiv.org/pdf/2611.33682
- **详细分析**: [[20_Research/Papers/大模型/WorldUAV_Scaling_UAV_Data_Synthesis_via_World_Models|WorldUAV: Scaling UAV Data Synthesis via World Models]]
- **作者**: Xuewen Liu, Mengjuan Chen, Jing Zhang, Mengzhe Shen, Zekun Xu, Zibo Chen, Zuoxiu Zhang, Yue Dong, Zhikai Li, Qingyi Gu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 大模型
- **相关性评分**: 1.9（加权：大模型 0.3，世界模型 0.8，机器人 0.8）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《WorldUAV: Scaling UAV Data Synthesis via World Models》归入 世界模型、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

UAV detection and tracking remain constrained by the scarcity of high-quality training data. Existing game-engine-based synthetic UAV data suffer from a substantial synthetic-to-real gap, while the high cost of manually collected real-world UAV data limits dataset scale. Therefore, we introduce WorldUAV, a high-quality UAV dataset constructed through an efficient framework powered by world models. Specifically, WorldUAV directly integrates UAVs into readily available real-world videos, naturally preserving realistic backgrounds, illumination, and scene dynamics. Leveraging the spatiotemporal priors of world models, it generates UAV videos with plausible motion, pose variations, and cross-frame consistency, effectively narrowing the gap between synthetic and real data. We further develop an agentic pipeline orchestrated by a multimodal large language model that acquires sources, plans UAV trajectories, invokes synthesis, and verifies generated videos, enabling fully automated dataset construction. WorldUAV comprises 6,878 UAV videos and 205,778 UAV images. Experiments show that WorldUAV significantly improves the performance of UAV detectors. Moreover, it substantially reduces dataset construction costs, requiring only 15 seconds and USD 0.0005 API cost per high-quality UAV image. Our work offers both a high-quality dataset and a scalable data generation paradigm for UAV detection and tracking.

</details>

---

### [[20_Research/Papers/强化学习/SplatWAM_Splatting_World_Action_Models_for_Real-Time_3D_Imagination|SplatWAM: Splatting World Action Models for Real-Time 3D Imagination]]

![[assets/2611.33467_figure.png|800]]

- **arXiv**: [2611.33467](https://arxiv.org/abs/2611.33467)
- **PDF**: https://arxiv.org/pdf/2611.33467
- **详细分析**: [[20_Research/Papers/强化学习/SplatWAM_Splatting_World_Action_Models_for_Real-Time_3D_Imagination|SplatWAM: Splatting World Action Models for Real-Time 3D Imagination]]
- **作者**: Frank Tsu-Fang Lu, Karthik Sundar Senthilkumar, Christopher Thirgood, Oscar Mendez, Simon Hadfield
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.72（加权：具身智能 0.3，强化学习 0.16，世界模型 0.76，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《SplatWAM: Splatting World Action Models for Real-Time 3D Imagination》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OGBench, OpenVLA, PointWorld, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models typically predict future observations in pixel or latent space, limiting their ability to directly represent true 3D scene evolution. We present SplatWAM (Splatting World Action Model), a generative world model that learns action-conditioned dynamics directly over compact 3D Gaussian primitives. A tokenizer SplatWAM-T first encodes a variable number of unposed views into a fixed budget of Gaussian tokens. A dynamics model SplatWAM-D then predicts future Gaussian states in a single forward pass per action, using log-Euclidean covariance coordinates and differentiable rendering supervision to facilitate learning in an explicit 3D space. Each predicted state can be rasterized from arbitrary viewpoints, enforcing a shared 3D representation across views by construction. On OGBench Scene, SplatWAM renders novel views 12x faster than video world models (~80 FPS on an RTX 5090) with up to 2.0 dB higher PSNR. We further introduce SplatWAM-P, a lightweight flow-matching policy head jointly trained with the dynamics model. Across 8 task suites, model-free Gaussian-token policies outperform pixel-based counterparts by up to 24.8 percentage points. SplatWAM-P improves over Latent Particle World Model (LPWM) by 12 percentage points and matches HIQL without a learned value function. On LIBERO, our ~1B model outperforms WorldVLA (~7B) and the robot-pretrained OpenVLA (~7B), while matching OpenVLA-OFT when both are trained without large-scale robot pretraining. Code and checkpoints will be released.

</details>

---

### [[20_Research/Papers/具身智能/Innata-0_A_Native_Embodied_World_System_with_Model-Agent_Co-Design|Innata-0: A Native Embodied World System with Model-Agent Co-Design]]

![[assets/2611.30254_figure.png|800]]

- **arXiv**: [2611.30254](https://arxiv.org/abs/2611.30254)
- **PDF**: https://arxiv.org/pdf/2611.30254
- **详细分析**: [[20_Research/Papers/具身智能/Innata-0_A_Native_Embodied_World_System_with_Model-Agent_Co-Design|Innata-0: A Native Embodied World System with Model-Agent Co-Design]]
- **作者**: Innata Team, Yu Bai, Ziyi Bai, Yuxuan Cai, Chenrui He, Wenhao Li, Zhe Lin, Heng Wang, Hai Yuan, Zhiwei Yu, Yuanhang Zhang, Luyou Chen...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.8，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Innata-0: A Native Embodied World System with Model-Agent Co-Design》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RoboDojo-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The physical world is open-ended, dynamic, and partially observable. While foundation models have advanced embodied intelligence, standalone models struggle with long-horizon execution, and simply integrating models with agents may lead to inconsistencies between planning and physical control. To support reliable and adaptive behaviors in the physical world, we introduce Innata-0, a native embodied world system. Innata-0 jointly designs an embodied world-action model and an agent to combine their complementary strengths. The model, Innata-0-WAM, adopts a tri-tower Mixture-of-Transformers architecture that integrates understanding, prediction, and action generation. The agent, Innata-0-Agent, coordinates long-horizon execution through memory, verification, and recovery. A co-design protocol is further proposed to align model training with agent execution and leverage validated experiences to support subsequent adaptation and model improvement. Extensive evaluations demonstrate strong embodied capabilities across understanding, world prediction, and robotic manipulation. Innata-0 represents our first step toward physical intelligence, and we see it as the beginning of a much longer journey.

</details>

---

### [[20_Research/Papers/机器人/Confidently_Lost_Silent_Failure_and_Edge_Deployment_of_Dense_Visual_SLAM_under_Photon_Starvation|Confidently Lost: Silent Failure and Edge Deployment of Dense Visual SLAM under Photon Starvation]]

![[assets/2611.30173_figure.png|800]]

- **arXiv**: [2611.30173](https://arxiv.org/abs/2611.30173)
- **PDF**: https://arxiv.org/pdf/2611.30173
- **详细分析**: [[20_Research/Papers/机器人/Confidently_Lost_Silent_Failure_and_Edge_Deployment_of_Dense_Visual_SLAM_under_Photon_Starvation|Confidently Lost: Silent Failure and Edge Deployment of Dense Visual SLAM under Photon Starvation]]
- **作者**: Shrikrishna Bhagirath Rajule, Srinath Neelamagam, Aniket Bera
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Confidently Lost: Silent Failure and Edge Deployment of Dense Visual SLAM under Photon Starvation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dense visual SLAM built on learned two-view geometry is evaluated in good light; in low light it fails silently. Two frames of 9-level quantized noise, no scene at all, give MASt3R-SLAM's network a cross-view geometric self-consistency of 0.936; a real dark frame pair gives 0.935. Starved of structure, the network invents the same geometry for both views and the system trusts the agreement: on a dark sequence it consumes 1,605 frames, emits 7 keyframes, rejects no factor-graph edges and reports full frame rate, while over 95% of the correspondences it accepts violate the ground-truth epipolar geometry. One inflated statistic is read by two subsystems against thresholds in opposite directions, so keyframing starves while relocalization accepts almost every candidate. The same statistic, read at keyframe-pair baselines, separates the confident collapse from working runs on the ETH3D dark sequences without ground truth or extra computation (in-sample). Low-light-adapted weights take tracked trajectories from 1/6 to 5/6, as does retuning two thresholds; neither yields accurate ones, because the adaptation withdraws confidence from wrong geometry rather than finding right geometry. Replayed on a Jetson AGX Orin carried by a legged robot, the mechanism's signature reproduces on the two darkest of four routes, and which of its faces appears varies with route geometry and sensor encoding. The network does not lose confidence in the dark; it manufactures it.

</details>

---
