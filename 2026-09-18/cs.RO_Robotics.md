# cs.RO | Robotics | 2026-09-18

#arxiv #ComputerScience

**论文数**: 52

### [[20_Research/Papers/强化学习/StageGuard_Learning_Stage_Transitions_for_Long-Horizon_Robot_Tasks_via_Agentic_Distillation|StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation]]

![[assets/2609.20791_figure.png|800]]

- **arXiv**: [2609.20791](https://arxiv.org/abs/2609.20791)
- **PDF**: https://arxiv.org/pdf/2609.20791
- **详细分析**: [[20_Research/Papers/强化学习/StageGuard_Learning_Stage_Transitions_for_Long-Horizon_Robot_Tasks_via_Agentic_Distillation|StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation]]
- **作者**: Jinbang Huang, Yuanzhao Hu, Zhiyuan Li, Ran Qi, Yixin Xiao, Yangzheng Wu, Tengyue Ba, Zhanguang Zhang, Yingxue Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《StageGuard: Learning Stage Transitions for Long-Horizon Robot Tasks via Agentic Distillation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hierarchical planning frameworks combine skills from multiple robot control policies for long-horizon task execution, where determining when to terminate the current skill and advance to the next subtask is essential. Existing approaches often rely on pre-designed completion signal checkers that are hard to obtain in real-world execution. Large-scale vision-language models (VLMs) offer strong reasoning capabilities, but their decision boundaries are not inherently aligned with task completion criteria, while cloud deployment and lengthy reasoning introduce substantial latency, limiting real-time monitoring. We propose StageGuard, an agentic distillation framework for accurate and efficient stage-transition decisions. StageGuard combines teacher-model reasoning with demonstration trajectories to generate structured explanations of subtask completion and policy switching. A lightweight student VLM uses these explanations to generate compact self-explanations, which are used for supervised fine-tuning. We evaluate stage-transition prediction on trajectories from two benchmarks and assess closed-loop task success through integration into hierarchical robot control on BEHAVIOR-1K, with further validation on real robots. Results show substantial improvements in stage-transition prediction while supporting efficient online monitoring.

</details>

---

### [[20_Research/Papers/具身智能/SkipVLA_Skipping_VLA_Steps_with_Classical_Planning_for_Fast_Robot_Manipulation|SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation]]

![[assets/2609.20648_figure.png|800]]

- **arXiv**: [2609.20648](https://arxiv.org/abs/2609.20648)
- **PDF**: https://arxiv.org/pdf/2609.20648
- **详细分析**: [[20_Research/Papers/具身智能/SkipVLA_Skipping_VLA_Steps_with_Classical_Planning_for_Fast_Robot_Manipulation|SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation]]
- **作者**: Kaivalya Agrawal, Md Ashiqur Rahman, Raymond A. Yeh, Zachary Kingston
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.1（加权：具身智能 3，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SkipVLA: Skipping VLA Steps with Classical Planning for Fast Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LiLo-VLA, Real-World, SkipVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are a class of generalist robot policies that map camera images and language instructions directly to robot actions. While promising, these models remain slow at test time, particularly for long-horizon tasks that require many queries to the policy. Recent efforts reduce VLA latency by distilling smaller models, overlapping asynchronous action chunks, or pairing the VLA with a fast low-level policy, but still run a learned policy for the entire task. In contrast to VLA, classical motion planners quickly find collision-free motions, but require an explicit goal and have no semantic understanding of the task. In this work, we present SkipVLA, a hybrid policy that combines a pretrained VLA with a classical motion planner, using the planner for free-space motion and querying the VLA only for contact-rich skills such as grasping and placing. SkipVLA reuses the frozen vision-language backbone of the VLA to predict a target pose for each planned motion, and learns this predictor without additional demonstrations introduced into the system by using what was already learnt by the large VLA. We evaluate SkipVLA with three VLAs on 13 LIBERO tasks in simulation and three pick-and-place tasks on a physical 6-DoF YAM arm, demonstrating up to 2.5x faster task completion and significantly lower energy consumption while achieving the same task success rate.

</details>

---

### [[20_Research/Papers/具身智能/TraceFlow_Guiding_Frozen_Flow-Matching_Robot_Policies_with_Success_and_Failure_Traces|TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces]]

![[assets/2609.20646_figure.png|800]]

- **arXiv**: [2609.20646](https://arxiv.org/abs/2609.20646)
- **PDF**: https://arxiv.org/pdf/2609.20646
- **详细分析**: [[20_Research/Papers/具身智能/TraceFlow_Guiding_Frozen_Flow-Matching_Robot_Policies_with_Success_and_Failure_Traces|TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces]]
- **作者**: Jiaxuan Zhang, Ruizhe Liu, Yu Zhang, Yanchao Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 2.2（加权：具身智能 0.9，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TraceFlow: Guiding Frozen Flow-Matching Robot Policies with Success and Failure Traces》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MAP-VLA, OptimusVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A vision-language-action (VLA) policy with a flow-matching action expert generates each action chunk (a short command sequence) by integrating a learned velocity field; once its weights are fixed, the success or failure of an earlier rollout cannot change the chunk generated now. Concurrent test-time methods give a frozen policy such an input from retrieved successes, a learned critic, a verifier, or a dynamics model, but none uses the robot's own failed rollouts as negative evidence with nothing but a terminal outcome bit. We introduce TraceFlow, a progress-aligned guidance field that turns the action densities of retrieved successful and failed rollouts into a bounded correction to a frozen flow-matching action expert, using one terminal outcome bit per rollout and no other label. Its TraceBank stores traces, time-ordered state-action records with a terminal label, starts from the target-task training traces, and later admits the deployed robot's own rollouts. On an ordered real-robot packing task the base completes 21 of 50 trials in order, TraceFlow 39, and one stacking round without any weight update 47, with wrong-sequence episodes falling from 20 to 0. In simulation the gain is selective: with per-suite selected settings, TraceFlow raises RoboMemArena Sequence from 78.92\% to 91.50\% task success and Transferring from 54.41\% to 62.00\% at stacking round 2, leaves the 26-task aggregate unchanged, lowers Counting and Occlusion by 1.12 and 1.42 points, and changes LIBERO-Plus (Long) by +1.27 points (p = 0.0733). Stacking gains are finite, every branch peaking before round ten, and the bank's success-to-failure ratio predicts no retrieval allocation.

</details>

---

### [[20_Research/Papers/具身智能/RTK-Vision_PPO_for_Autonomous_Micro_UAV_Recovery_on_an_Airborne_Carrier|RTK-Vision PPO for Autonomous Micro UAV Recovery on an Airborne Carrier]]

![[assets/2609.20629_figure.png|800]]

- **arXiv**: [2609.20629](https://arxiv.org/abs/2609.20629)
- **PDF**: https://arxiv.org/pdf/2609.20629
- **详细分析**: [[20_Research/Papers/具身智能/RTK-Vision_PPO_for_Autonomous_Micro_UAV_Recovery_on_an_Airborne_Carrier|RTK-Vision PPO for Autonomous Micro UAV Recovery on an Airborne Carrier]]
- **作者**: Aashish Sahu, R Prasanth Kumar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《RTK-Vision PPO for Autonomous Micro UAV Recovery on an Airborne Carrier》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous recovery of a micro unmanned aerial vehicle (UAV) onto a moving airborne carrier enables reusable deploy-mission-recover operation, but couples long-range rendezvous, close-range perception, carrier motion, aerodynamic interaction, and a discontinuous contact event. This paper presents an RTK-vision-guided reinforcement-learning framework in which a child UAV is physically transported by a larger carrier, takes off from the carrier while airborne, executes an independent sortie, returns to the carrier's current position, redocks, and subsequently descends with the carrier. Both vehicles carry RTK-GNSS, and the carrier continuously shares its navigation state with the child. Near the recovery deck, RTK remains active while a downward-facing camera with a fiducial marker detector provides marker-relative alignment cues. A proximal policy optimization (PPO) policy governing the terminal recovery phase is trained in a physics-based MuJoCo simulation environment with explicit sensor noise models, an aerodynamic disturbance surrogate, and marker-latency randomization, then transferred to hardware. PX4 retains low-level stabilization, and a deterministic safety gate authorizes descent independently of the learned policy. The PPO checkpoint achieves 99.55% success over 2,000 held-out randomized terminal episodes, compared with 78.4% for a tuned PD baseline under identical conditions, with a median planar terminal error of 6.62 cm. Across 14 outdoor trials, the full mission succeeds in 13 trials (92.9%), spanning both near-region recovery and recovery after the carrier translates away from the release point. The results demonstrate a complete autonomous aerial deployment-and-recovery cycle rather than an isolated landing maneuver, establishing a practical basis for reusable carrier-child operation in inspection, surveillance, and mobile-logistics applications.

</details>

---

### [[20_Research/Papers/具身智能/SmellDiffusion_Diffusion-Based_Quadruped_Navigation_with_Olfactory_Scene_Graphs|SmellDiffusion: Diffusion-Based Quadruped Navigation with Olfactory Scene Graphs]]

![[assets/2609.20624_figure.png|800]]

- **arXiv**: [2609.20624](https://arxiv.org/abs/2609.20624)
- **PDF**: https://arxiv.org/pdf/2609.20624
- **详细分析**: [[20_Research/Papers/具身智能/SmellDiffusion_Diffusion-Based_Quadruped_Navigation_with_Olfactory_Scene_Graphs|SmellDiffusion: Diffusion-Based Quadruped Navigation with Olfactory Scene Graphs]]
- **作者**: Faith Ogunwoye, Iana Zhura, Hajira Amjad, Timofei Kozlov, Didar Seyidov, Dmitrii Plotnikov, Fedor Fedorov, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《SmellDiffusion: Diffusion-Based Quadruped Navigation with Olfactory Scene Graphs》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot sent to a named gas leak must preserve gas identity, estimate the source, and navigate to the resulting goal. We present SmellDiffusion, a simulation pipeline that represents species-specific gas zones in an open-vocabulary olfactory scene graph and shares the selected goal between classical and diffusion planners. Its key components are a peak-local geometric gate for selective source correction and diffusion-based, gas-guided trajectory generation. Among 424 unique source-wind configurations in solved flow, 28 have a concentration peak displaced more than 0.5m from the source. A source-independent geometric gate, calibrated only on the training split and evaluated at the observed peak, detects 9 of 10 held-out displacements at 0.64 precision. Gating a precomputed forward-matching correction reduces mean error on the displaced cases from 1.468m to 0.592m (60%), using matching for only 14/204 cases. All-case mean error falls from 0.205m to 0.180m. All planners receive the same scene-graph source estimate as their goal. In a controlled comparison, best-of-ten diffusion achieves mean gas exposure comparable to gas-guided A* (0.0476 versus 0.0455). A single diffusion proposal takes 41.7ms, compared with 72.3ms for gas-guided A*, although best-of-ten sequential sampling increases total runtime. Plain A* also reaches the same goal and remains the fastest and shortest-path method. Six matched Gazebo runs give mean robot-to-source errors of 0.39m for A* and 0.31m for diffusion.

</details>

---

### [[20_Research/Papers/机器人/Bayesian_Continuum_Robot_Dynamics_and_State_Estimation|Bayesian Continuum Robot Dynamics and State Estimation]]

![[assets/2609.20605_figure.png|800]]

- **arXiv**: [2609.20605](https://arxiv.org/abs/2609.20605)
- **PDF**: https://arxiv.org/pdf/2609.20605
- **详细分析**: [[20_Research/Papers/机器人/Bayesian_Continuum_Robot_Dynamics_and_State_Estimation|Bayesian Continuum Robot Dynamics and State Estimation]]
- **作者**: James M. Ferguson, Tucker Hermans, Alan Kuntz
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Bayesian Continuum Robot Dynamics and State Estimation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent factor graph approaches to continuum robot state estimation have been successful for quasi-static applications and spatiotemporal estimation using white-noise kinematic motion priors. However, when inertial effects are significant, these approximations may fail to capture the underlying physics, limiting accuracy during dynamic motions. In contrast, our approach approximates the Cosserat rod dynamics of continuum robots. We write inertia and damping as equivalent applied loads, so that the dynamic balance retains the algebraic form of the static one from prior work with quasi-static robots. Without backbone observations, the framework reduces to a stochastic forward simulation of the robot's motion. Given observations, it jointly refines kinematic and dynamic states and infers external loads, among other states. We validate the approach through simulation and experiments, demonstrating stochastic forward simulation as well as state estimation on tendon-driven continuum robots.

</details>

---

### [[20_Research/Papers/机器人/Semantic_SLAM_in_Precision_Agriculture_using_Bayesian_Inference|Semantic SLAM in Precision Agriculture using Bayesian Inference]]

![[assets/2609.20604_figure.jpg|800]]

- **arXiv**: [2609.20604](https://arxiv.org/abs/2609.20604)
- **PDF**: https://arxiv.org/pdf/2609.20604
- **详细分析**: [[20_Research/Papers/机器人/Semantic_SLAM_in_Precision_Agriculture_using_Bayesian_Inference|Semantic SLAM in Precision Agriculture using Bayesian Inference]]
- **作者**: Ruben Beumer, Sander Doodeman, René van de Molengraft, Duarte Antunes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Semantic SLAM in Precision Agriculture using Bayesian Inference》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a real-time semantic world modeling framework specialized for precision agriculture using autonomous robots. The framework combines probabilistic mapping of objects and their semantic attributes, updated through Bayesian inference, with a graph-based Simultaneous Localization and Mapping (SLAM) approach implemented using $g^2o$, a general framework for graph optimization. This integration enables accurate mapping and localization without relying solely on GPS. By leveraging semantic information such as plant type, size, and health, the robot can perform tasks while mapping and localizing itself within a field of crops. The proposed framework was validated through Gazebo simulations and physical experiments on an indoor field with artificial plants using Boston Dynamics' robot dog Spot. A YOLOv8n object detection model was trained to extract object and semantic data from depth camera observations. These simulations and experiments demonstrate that the system can successfully perform real-time mapping of up to at least 400 plants.

</details>

---

### [[20_Research/Papers/世界模型/V2-STRep_VLM-Grounded_Structured_Task_Representations_for_Reusable_Robot_Skills_Acquired_from_Generated_Videos|V2-STRep: VLM-Grounded Structured Task Representations for Reusable Robot Skills Acquired from Generated Videos]]

![[assets/2609.20582_figure.png|800]]

- **arXiv**: [2609.20582](https://arxiv.org/abs/2609.20582)
- **PDF**: https://arxiv.org/pdf/2609.20582
- **详细分析**: [[20_Research/Papers/世界模型/V2-STRep_VLM-Grounded_Structured_Task_Representations_for_Reusable_Robot_Skills_Acquired_from_Generated_Videos|V2-STRep: VLM-Grounded Structured Task Representations for Reusable Robot Skills Acquired from Generated Videos]]
- **作者**: Yexin Hu, Dongheui Lee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《V2-STRep: VLM-Grounded Structured Task Representations for Reusable Robot Skills Acquired from Generated Videos》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human manipulation videos provide rich motion and interaction cues for acquiring robot skills without robot demonstrations. Video generation models synthesize such demonstrations from an initial scene image and task instruction, avoiding the need to record demonstrations for each task. However, the recovered motion captures only one scene-specific realization, leaving task structure, geometric relations, and constraints implicit. We present V2-STRep, a zero-shot framework that converts generated video motion into reusable robot skills through VLM-grounded structured task representations. The representation specifies motion phases, references, and task-relevant constraints, with targets described by minimal geometric structures: points, point-normals, axes, planes, and full 6D poses. VLM-provided 2D image-space cues are lifted into 3D using RGB-D observations to reconstruct task geometry and candidate grasp poses. Geometry-specific rules transfer motion to new scenes, while task-constrained trajectory optimization couples grasp selection with complete robot motion planning. It preserves task requirements while using remaining rotational freedom to accommodate joint limits. Updating deployment grounding and constraints enables reuse under new compatible instructions without generating another video. Experiments on six real-world manipulation tasks demonstrate improved execution success over baselines, reliable cross-scene transfer of successfully acquired skills, and adaptation to changed deployment instructions.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Slope-Adaptive_Whole-Body_Locomotion_for_Humanoid_Robots_in_Roofing_Construction|Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction]]

![[assets/2609.20558_figure.jpg|800]]

- **arXiv**: [2609.20558](https://arxiv.org/abs/2609.20558)
- **PDF**: https://arxiv.org/pdf/2609.20558
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Slope-Adaptive_Whole-Body_Locomotion_for_Humanoid_Robots_in_Roofing_Construction|Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction]]
- **作者**: Songyang Liu, Shuai Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.7，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Learning Slope-Adaptive Whole-Body Locomotion for Humanoid Robots in Roofing Construction》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Roofing requires workers to coordinate locomotion, balance, and work-related body motions on pitched surfaces, creating a challenging application for humanoid robots. Directly retargeted human demonstrations, however, may preserve motion appearance while placing the robot's feet or hands incorrectly relative to the roof. This study presents a task-semantic scene-grounded framework for learning roofer-style whole-body motions on a Unitree G1. Human demonstrations are captured using a tracking system and retargeted to the robot, while a metric roof model supplies the spatial reference unavailable from the tracking system. A trajectory-level optimization grounds inferred support contacts and annotated work relations to the roof, and execution-aware reinforcement learning encourages the resulting policy to preserve these relations under dynamic tracking errors. The framework is evaluated through a multi-motion tracking study, a roof-pitch coverage matrix, a five-way nailgun ablation, cross-task experiments on hammering and lateral pushing, and comparisons with pure reinforcement learning and zero-shot teleoperation. Our method enables the robot to satisfy support, work-clearance, and nonpenetration criteria across all evaluated seeds. Across nailgun, hammering, and pushing, it achieves work-clearance errors between 0.256 and 0.531 cm and 3/3 successful evaluations per task. Physical experiments reproduce uphill walking, nailgun, hammering, and bending motions with mean base-frame motion errors below 80 mm. These findings establish scene-grounded human motion learning as a promising basis for construction-oriented humanoid motion primitives.

</details>

---

### [[20_Research/Papers/机器人/Integrated_Guidance_and_Control_of_a_Mother-Child_UAV-UGV_System_for_Cooperative_Missions|Integrated Guidance and Control of a Mother-Child UAV-UGV System for Cooperative Missions]]

![[assets/2609.20540_first_page.png|800]]

- **arXiv**: [2609.20540](https://arxiv.org/abs/2609.20540)
- **PDF**: https://arxiv.org/pdf/2609.20540
- **详细分析**: [[20_Research/Papers/机器人/Integrated_Guidance_and_Control_of_a_Mother-Child_UAV-UGV_System_for_Cooperative_Missions|Integrated Guidance and Control of a Mother-Child UAV-UGV System for Cooperative Missions]]
- **作者**: Aashish Sahu, R. Prasanth Kumar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《Integrated Guidance and Control of a Mother-Child UAV-UGV System for Cooperative Missions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous recovery of a small multirotor onto a hovering multirotor carrier differs from recovery onto ground or shipborne platforms because the recovery surface is itself an actively controlled, thrust-limited aerial vehicle. This paper presents a field-validated autonomy framework for a heterogeneous rover-mothership-child system executing rover supervision, mothership transit, child deployment and sortie, autonomous return, aerial recovery, and synchronized descent. The recovery stack combines jerk-bounded reference generation, disturbance-observer-augmented planar tracking, feasibility-aware vertical control, a discrete-time barrier-based safety filter for relative vertical geometry, and communication-aware carrier-state prediction. The contribution is the coordinated system-level integration of these methods for recovery onto a hovering multirotor and its full-scale outdoor validation. The framework is implemented on a PX4-ROS 2 architecture using RTK-enabled GNSS, IMU, and barometric fusion, with mothership-side 1D lidar used only as an auxiliary near-contact cue. RTK-fixed positioning was maintained throughout testing. Across 20 outdoor cooperative missions, 17 successfully completed deployment, sortie, and recovery, giving an observed mission success rate of 85%. For successful recoveries, mean terminal-alignment time was 6.3 s, mean planar alignment error at acceptance was 0.18 m, maximum terminal planar deviation was 0.32 m within a 0.40 m capture radius, and minimum logged relative vertical separation during coupled descent was 0.41 m. Mothership planar station-keeping RMS error was 0.25 m. The three unsuccessful trials occurred at different mission stages and are analyzed separately. Results demonstrate practical autonomous aerial recovery within the tested outdoor operating envelope.

</details>

---

### [[20_Research/Papers/机器人/Towards_AI-enhanced_control_a_numerical_technique_for_trajectory_smoothing_of_a_parallel_robot_for_pancreatic_surgery|Towards AI-enhanced control: a numerical technique for trajectory smoothing of a parallel robot for pancreatic surgery]]

![[assets/2609.20499_first_page.png|800]]

- **arXiv**: [2609.20499](https://arxiv.org/abs/2609.20499)
- **PDF**: https://arxiv.org/pdf/2609.20499
- **详细分析**: [[20_Research/Papers/机器人/Towards_AI-enhanced_control_a_numerical_technique_for_trajectory_smoothing_of_a_parallel_robot_for_pancreatic_surgery|Towards AI-enhanced control: a numerical technique for trajectory smoothing of a parallel robot for pancreatic surgery]]
- **作者**: Iosif Birlescu, Alexandru Pusca, Bogdan Gherman, Calin Vaida, Ionut Zima, Damien Chablat, Doina Pisla
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Towards AI-enhanced control: a numerical technique for trajectory smoothing of a parallel robot for pancreatic surgery》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The paper presents a numerical approach for the end-effector trajectory smoothing of a parallel robot designed for minimally invasive pancreatic surgery. The approach is tailored for real-time master-slave control architecture and uses a 3D space mouse for command input for velocity control. The trajectory smoothing is achieved by generating S-curves in the end-effector velocity fields, thus controlling the accelerations, which in turn reduces tissue trauma in the minimally invasive procedures. Real-time control is enabled by segmenting the S-curves based on the command inputs from the 3D space mouse. A special case is considered where the acceleration time is constant for all command inputs. Numeric results demonstrate stable transitions (without abrupt changes) in both the end-effector parameter space and in the active joints parameters, thereby validating the proposed approach. Further work aims to test the approach on an experimental model and integrate it into AI-based training modules.

</details>

---

### [[20_Research/Papers/强化学习/Visual_Sim-to-Real_Learning_for_Robotic_Insertion_under_Geometric_Variations_Application_to_Rebar_Installation|Visual Sim-to-Real Learning for Robotic Insertion under Geometric Variations: Application to Rebar Installation]]

![[assets/2609.20477_figure.jpg|800]]

- **arXiv**: [2609.20477](https://arxiv.org/abs/2609.20477)
- **PDF**: https://arxiv.org/pdf/2609.20477
- **详细分析**: [[20_Research/Papers/强化学习/Visual_Sim-to-Real_Learning_for_Robotic_Insertion_under_Geometric_Variations_Application_to_Rebar_Installation|Visual Sim-to-Real Learning for Robotic Insertion under Geometric Variations: Application to Rebar Installation]]
- **作者**: Tao Sun, Beining Han, Patrick Yin, Rui Xu, Harry He, Abhishek Gupta, Szymon Rusinkiewicz, Yi Shao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Visual Sim-to-Real Learning for Robotic Insertion under Geometric Variations: Application to Rebar Installation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, RebarSim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rebar insertion is among the most repetitive and physically demanding tasks on construction sites, and a contact-rich problem at 1.4 mm clearance. The parts, however, vary at two levels: a nominal design per structural member, and fabrication tolerance around each nominal design. Real-world data therefore has to be re-collected as designs and batches change. We present RebarSim, a visual sim-to-real system trained entirely in simulation. A privileged state-based teacher is trained with reinforcement learning over procedurally generated rebar geometries, then distilled into a multi-view student that maps raw RGB and proprioception directly to actions under extensive domain randomization. The student transfers to the real world zero-shot, seating rebars taken from a real factory production run in 91.3% of real-robot rollouts. Underlying that result, geometry diversity and pretraining both bring benefits. Training across a diverse set of nominal designs rather than one lifts the zero-shot success of both the teacher and the student on unseen designs, and the student policy outperforms a single-design specialist on that specialist's own design. A pretrained student then adapts to a new design with 4--6x fewer distillation samples than one trained from scratch. Visual sim-to-real transfer depends on appearance randomization and the DAgger mixture: removing either one sharply lowers success. Videos, code, and task assets are available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Spatial-Semantic_Uncertainty_in_VLM-Based_Target_Search_Balancing_Exploration_and_Identification|Spatial-Semantic Uncertainty in VLM-Based Target Search: Balancing Exploration and Identification]]

![[assets/2609.20443_figure.png|800]]

- **arXiv**: [2609.20443](https://arxiv.org/abs/2609.20443)
- **PDF**: https://arxiv.org/pdf/2609.20443
- **详细分析**: [[20_Research/Papers/具身智能/Spatial-Semantic_Uncertainty_in_VLM-Based_Target_Search_Balancing_Exploration_and_Identification|Spatial-Semantic Uncertainty in VLM-Based Target Search: Balancing Exploration and Identification]]
- **作者**: Alkesh K. Srivastava, Jonathan Diller, Vijay Kumar, Philip Dames
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.4，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Spatial-Semantic Uncertainty in VLM-Based Target Search: Balancing Exploration and Identification》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots searching for a target from a natural-language description must determine not only where to search, but also which observed candidate is the desired target. These decisions reflect two distinct sources of uncertainty - spatial uncertainty over candidate locations and semantic uncertainty over target identity - that are often conflated in VLM-based search systems. We introduce a spatial-semantic uncertainty formulation that maintains separate beliefs over each component and integrates probabilistic VLM evidence into a global target-identity posterior, including probability mass for undiscovered targets. This decomposition allows an information-theoretic planner to independently value candidate discovery and target disambiguation through spatial and semantic expected information gain (EIG), providing an explicit mechanism for trading broader exploration against earlier identification. We evaluate six VLM uncertainty-elicitation interfaces on 500 synthetic targets and show that similar recognition accuracy can conceal substantial differences in calibration and false confidence. In degraded-observation search-and-identify experiments, EIG-based planners reach confident decisions in 75.0%-92.5% of trials, compared with 20.0% for Random search, while different spatial-semantic weightings achieve comparable identification accuracy once confidence is attained. Increasing semantic emphasis reduces unnecessary exploration and VLM queries, demonstrating that explicitly planning over semantic uncertainty can accelerate target resolution without sacrificing decision quality. These results highlight the distinct roles of uncertainty representation and uncertainty-driven planning in embodied VLM systems.

</details>

---

### [[20_Research/Papers/机器人/Resilient_Motion_Planning_for_Free-Flying_Space_Robots_under_Actuator_Failures|Resilient Motion Planning for Free-Flying Space Robots under Actuator Failures]]

![[assets/2609.20407_figure.png|800]]

- **arXiv**: [2609.20407](https://arxiv.org/abs/2609.20407)
- **PDF**: https://arxiv.org/pdf/2609.20407
- **详细分析**: [[20_Research/Papers/机器人/Resilient_Motion_Planning_for_Free-Flying_Space_Robots_under_Actuator_Failures|Resilient Motion Planning for Free-Flying Space Robots under Actuator Failures]]
- **作者**: Nicolas de Maddalena, Joris Verhagen, Jana Tumova
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Resilient Motion Planning for Free-Flying Space Robots under Actuator Failures》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Free-flying robots rely on multiple thrusters to maneuver in space. If one or more of these thrusters fail, the robot may lose control authority and risk mission failure. At the same time, their free-flying nature implies that, even in the absence of actuation, they continue along (locally) straight-line trajectories. In this work we present a probabilistic, proactive, motion planning framework that explicitly accounts for actuator failures in space. We model actuator failure modes as a Markov chain and propagate the probability of successfully reaching the goal along the planning horizon. Precomputed reachable sets evaluate the robot's capabilities of reaching waypoints under potential failures and an RRT$^*$-based planner concatenates these waypoints. The resulting algorithm maximizes the overall target-reaching probability, providing maximally resilient motion plans utilizing free-flying properties. We validate our approach experimentally on a physical free-flyer platform with injected actuator failures.

</details>

---

### [[20_Research/Papers/大模型/Imagine-TAMP_Imagination-Guided_Task_and_Motion_Planning_in_Partial_Observability|Imagine-TAMP: Imagination-Guided Task and Motion Planning in Partial Observability]]

![[assets/2609.20396_figure.png|800]]

- **arXiv**: [2609.20396](https://arxiv.org/abs/2609.20396)
- **PDF**: https://arxiv.org/pdf/2609.20396
- **详细分析**: [[20_Research/Papers/大模型/Imagine-TAMP_Imagination-Guided_Task_and_Motion_Planning_in_Partial_Observability|Imagine-TAMP: Imagination-Guided Task and Motion Planning in Partial Observability]]
- **作者**: Antareep Singha, Shivaram Kumar, Yoonwoo Kim, Yoonchang Sung
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Imagine-TAMP: Imagination-Guided Task and Motion Planning in Partial Observability》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in cluttered environments must often manipulate objects whose locations are only partially observable. A central challenge is deciding whether to acquire another observation or to first manipulate objects that may occlude the target. Conventional task and motion planning (TAMP) approaches typically make this decision using symbolic action costs or expensive geometric planning, neither of which adequately captures how likely an observation is to reveal an occluded target. We introduce Imagine-TAMP, an interleaved planning and execution framework that uses semantic and geometric imagination to compare alternative task-level strategies under partial observability before committing to expensive motion planning. A vision-language model shapes a particle belief over target locations using commonsense relationships between the target and visible objects, while a generative scene model estimates plausible geometry in unobserved regions. Given a target hypothesis and imagined scene, Imagine-TAMP generates multiple symbolic plan skeletons and assigns non-unit costs that approximate both manipulation effort and target visibility from sensing actions, distinguishing a short but poorly informative observation strategy from a longer strategy that first manipulates an occluder to better expose the target. The selected skeleton is then refined into a feasible continuous plan and executed, with new observations updating the belief and triggering replanning when necessary. Experiments show that imagination-guided evaluation improves observation-versus-manipulation decisions: in viewpoint-constrained shelf scenes, non-unit geometric evaluation increases success from 46.0% to 84.0%, while semantic belief shaping further reduces manipulation and replanning. On a real robot, the complete system reduces planning time by 32% relative to a geometry-only ablation.

</details>

---

### [[20_Research/Papers/具身智能/RoboFind_Multi-Agent_Personalized_Object_Search_for_People_Who_Are_Blind_or_Have_Low_Vision|RoboFind: Multi-Agent Personalized Object Search for People Who Are Blind or Have Low Vision]]

![[assets/2609.20330_figure.png|800]]

- **arXiv**: [2609.20330](https://arxiv.org/abs/2609.20330)
- **PDF**: https://arxiv.org/pdf/2609.20330
- **详细分析**: [[20_Research/Papers/具身智能/RoboFind_Multi-Agent_Personalized_Object_Search_for_People_Who_Are_Blind_or_Have_Low_Vision|RoboFind: Multi-Agent Personalized Object Search for People Who Are Blind or Have Low Vision]]
- **作者**: Ruiping Liu, Shaofang Quan, Qian Yin, Jingqi Zhang, Junwei Zheng, Yufan Chen, Di Wen, Weijia Fan, Kailun Yang, M. Saquib Sarfraz, Tamim Asfour, Kunyu Peng...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.6，大模型 0.4，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《RoboFind: Multi-Agent Personalized Object Search for People Who Are Blind or Have Low Vision》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Blind and low-vision users often need to locate a specific personal object rather than an arbitrary instance of the same category. The task calls for a robot that can move through the space and reach viewpoints the user cannot, and for an accessible interface where the user says which object is meant and learns whether the right one was found. We present RoboFind, a multi-agent framework in which a smartphone teaches the target and a quadruped robot carries out the search. A Target Teaching Agent converts guided smartphone recordings into a semantic target profile and a reusable multi-view reference bank through an accessible capture flow with AR guidance, speech and haptic feedback, and screen-reader support, so later missions refer to a stored object without repeating the teaching process. At runtime, a Navigation Agent explores the environment and proposes candidate targets, a Verification Agent checks each candidate against the stored references, and a Coordination and Recovery Agent completes the mission or triggers recovery and continued search. Across 32 real-robot missions, RoboFind reaches 85.0% success against 25.0% for a reconstructed sequential first-stop baseline over 20 trials with ten targets, and reduces false success from 75.0% to 5.0%. On six shared targets it succeeds in 10/12 trials, against 5/12 for 12 independently executed GPT-6 Astra-only trials. These results show that the multi-agent design fits the demands of personalized object search, where verifying object identity before declaring completion is what makes the outcome something a user can rely on.

</details>

---

### [[20_Research/Papers/机器人/Implementation_of_Tightly-Coupled_SLAM_Fusion_of_GPS,_IMU,_and_LiDAR_for_Autonomous_Vehicles|Implementation of Tightly-Coupled SLAM Fusion of GPS, IMU, and LiDAR for Autonomous Vehicles]]

![[assets/2609.20321_figure.png|800]]

- **arXiv**: [2609.20321](https://arxiv.org/abs/2609.20321)
- **PDF**: https://arxiv.org/pdf/2609.20321
- **详细分析**: [[20_Research/Papers/机器人/Implementation_of_Tightly-Coupled_SLAM_Fusion_of_GPS,_IMU,_and_LiDAR_for_Autonomous_Vehicles|Implementation of Tightly-Coupled SLAM Fusion of GPS, IMU, and LiDAR for Autonomous Vehicles]]
- **作者**: Amr O. Elmehrath, Farah Khaled, Rana Nahas, Catherine M. Elias
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Implementation of Tightly-Coupled SLAM Fusion of GPS, IMU, and LiDAR for Autonomous Vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous vehicles depend entirely on Simultaneous Localization and Mapping (SLAM) to navigate safely in unknown environments. However, relying on a single sensory modality introduces critical failure points: LiDAR systems degrade in featureless corridors, Inertial Measurement Units (IMUs) accumulate mathematical drift, and GPS drops frequently in urban canyons. This paper presents the implementation of a tightly-coupled SLAM fusion architecture that integrates a Velodyne 3D LiDAR, a high-frequency IMU, and GPS to achieve continuous spatial awareness. Utilizing a phased development methodology, we establish a 2D baseline to validate hardware synchronization and transform geometries before upgrading to a full 3D architecture driven by FAST-LIO2. This advanced approach uses an Iterated Error-State Kalman Filter (IESKF) to process dense 3D laser points alongside continuous inertial data, eliminating motion blur at high speeds. To eradicate long-term drift, a GTSAM pose-graph optimization back-end executes multi-modal loop closures. Evaluated across simulated environments and physical deployments, the results demonstrate that tightly-coupled 3D fusion effectively overcomes individual sensor blind spots to generate highly detailed point clouds, providing the foundational High-Definition (HD) maps required for advanced downstream autonomous planners.

</details>

---

### [[20_Research/Papers/具身智能/Strategic_Transformer_for_Resource-Constrained_Multi-Object_Navigation_in_Ultra-Large-Scale_Environments|Strategic Transformer for Resource-Constrained Multi-Object Navigation in Ultra-Large-Scale Environments]]

![[assets/2609.20227_figure.png|800]]

- **arXiv**: [2609.20227](https://arxiv.org/abs/2609.20227)
- **PDF**: https://arxiv.org/pdf/2609.20227
- **详细分析**: [[20_Research/Papers/具身智能/Strategic_Transformer_for_Resource-Constrained_Multi-Object_Navigation_in_Ultra-Large-Scale_Environments|Strategic Transformer for Resource-Constrained Multi-Object Navigation in Ultra-Large-Scale Environments]]
- **作者**: Daiki Iwata, Kanji Tanaka, Senta Hishida
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, Systems

#### 研究背景与动机

《Strategic Transformer for Resource-Constrained Multi-Object Navigation in Ultra-Large-Scale Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Resource-constrained multi-object navigation in vast indoor environments ($&gt;2,000\text{ m}^2$) poses significant challenges for efficiency and strategic planning. To tackle this, we reformulate the task as a Set Orienteering Problem (SOP), providing an optimization framework under resource constraints where exploitation is governed by the SOP model and exploration is managed by a separate heuristic switcher. Conventional baselines suffer from either rigid planning or myopic behaviors. To overcome these limitations and resolve the NP-hard computational challenges of SOP for real-time navigation, we develop the Strategic Transformer. This lightweight architecture functions as a priority planner that internalizes expert combinatorial logic into a predictable $41.03\text{ ms}$ forward pass while reducing teacher-student information asymmetry. Incorporating geometric attention biases allows the network to effectively model long-range structural dependencies. By coupling the Transformer's macro-plan with a bounded iterative 2-opt local refinement on a capped candidate graph, our framework achieves a $94\times$ speedup compared to heavy meta-heuristics, ensuring bounded-latency inference suitable for onboard deployment. Experiments on ProcTHOR validate that our method successfully bridges the gap between exploration and exploitation, outperforming carefully re-implemented baselines under Progress weighted by Path Length (PPL) and establishing a new benchmark for scalable, resource-constrained navigation.

</details>

---

### [[20_Research/Papers/具身智能/Universal_Navigation_Interface_Robot-Free_Data_for_Wheeled_Robot_Navigation|Universal Navigation Interface: Robot-Free Data for Wheeled Robot Navigation]]

![[assets/2609.20114_figure.png|800]]

- **arXiv**: [2609.20114](https://arxiv.org/abs/2609.20114)
- **PDF**: https://arxiv.org/pdf/2609.20114
- **详细分析**: [[20_Research/Papers/具身智能/Universal_Navigation_Interface_Robot-Free_Data_for_Wheeled_Robot_Navigation|Universal Navigation Interface: Robot-Free Data for Wheeled Robot Navigation]]
- **作者**: Sarvesh Prajapati, Ananya Trivedi, Lorena Maria Genua, Drake Moore, Bruce Maxwell, Taskin Padir
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Universal Navigation Interface: Robot-Free Data for Wheeled Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting real-world navigation data for mobile robots typically requires platform-specific teleoperation, making large-scale collection expensive and difficult to scale. We introduce Universal Navigation Interface (UNI), a robot-free data collection paradigm that uses a four-wheeled rollator walker (rollator) and smartphone to collect physically constrained human demonstrations. Because the rollator cannot climb stairs, negotiate uncut curbs, or pass through narrow gaps, demonstrations are naturally biased toward wheeled-feasible routes. Using UNI, we collect 37.2 km of real-world navigation data and recover metric trajectories that directly supervise goal-conditioned navigation models. Fine-tuning visual-navigation models on UNI reduces trajectory prediction error by 17.4-24.8% on held-out UNI demonstrations. Evaluation on other navigation datasets shows benefits that vary by dataset and metric. We further demonstrate closed-loop transfer to a powered wheelchair in curb, staircase, and curb-cut scenarios. These results support low-cost physical proxies as a practical source of navigation supervision collected without the target robot.

</details>

---

### [[20_Research/Papers/具身智能/AnyViewDex_View-Invariant_Dexterous_Manipulation_from_RGB_Observations|AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations]]

![[assets/2609.20107_figure.png|800]]

- **arXiv**: [2609.20107](https://arxiv.org/abs/2609.20107)
- **PDF**: https://arxiv.org/pdf/2609.20107
- **详细分析**: [[20_Research/Papers/具身智能/AnyViewDex_View-Invariant_Dexterous_Manipulation_from_RGB_Observations|AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations]]
- **作者**: Soham Patil, Om Sanjay Gunjal, Sourabh Bhosale, Arhan Chavare, Ramandeep Singh Hora, Spandan Roy
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.8，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《AnyViewDex: View-Invariant Dexterous Manipulation from RGB Observations》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ResNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor policies for multi-fingered dexterous manipulation are highly sensitive to camera viewpoint shifts. To achieve view invariance, recent methods increasingly rely on explicit 3D modalities like RGB-D or point clouds, which can introduce hardware dependencies, calibration requirements, and vulnerability to sensor noise during real-world deployment. In this work, we show that view-invariant control can be achieved without explicit test-time 3D sensing by encoding geometric knowledge into the visual representation during simulation. We present AnyViewDex, an asymmetric training pipeline that combines multi-view contrastive alignment with privileged 3D geometric supervision. By regressing absolute 3D object coordinates during simulated training, this auxiliary objective provides a geometric grounding signal that mitigates the spatial collapse of the globally pooled contrastive embedding. At deployment, the policy operates zero-shot using only uncalibrated monocular RGB and proprioception. We validate this approach across both reinforcement learning and student-teacher distillation. In hardware evaluation on an xArm7 with a 16-DoF LEAP Hand, AnyViewDex reaches 76.7% grasping success across eight unseen objects and six uncalibrated viewpoints (480 trials; 2,400 across all ablation conditions), indicating that geometrically grounded monocular policies transfer zero-shot without test-time depth. Project Page: this https URL

</details>

---

### [[20_Research/Papers/机器人/Mechanical_Precision_Weeding_with_a_Quadruped_Robot|Mechanical Precision Weeding with a Quadruped Robot]]

![[assets/2609.20048_figure.jpg|800]]

- **arXiv**: [2609.20048](https://arxiv.org/abs/2609.20048)
- **PDF**: https://arxiv.org/pdf/2609.20048
- **详细分析**: [[20_Research/Papers/机器人/Mechanical_Precision_Weeding_with_a_Quadruped_Robot|Mechanical Precision Weeding with a Quadruped Robot]]
- **作者**: Ruben Beumer, Tom Janssen, René van de Molengraft, Duarte Antunes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 1.5，机器人 1.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Mechanical Precision Weeding with a Quadruped Robot》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Herbicide-based weed control is increasingly unsustainable due to rising weed resistance and the adverse environmental impacts of chemical use. While mechanical weed control avoids these drawbacks, it is typically implemented using large machines that cause soil compaction. We propose a novel alternative based on small mobile robots for mechanical weeding. Compared with existing automated mechanical weeding approaches, the proposed method offers reduced soil compaction, simpler automation, and improved scalability. Our solution involves a Boston Dynamics Spot quadruped robot equipped with a custom weed removal tool featuring a milling bit at its end. The tool is rigidly attached to the robot and uses the degrees of freedom of the robot base by actuating the legs, while keeping the feet stationary. We develop a software architecture that enables autonomous weed removal and integrate this system with all other required components. We analyze the accuracy and efficiency of the current proof of concept both in an indoor and outdoor environment and provide recommendations for future work to make the system more accurate and efficient.

</details>

---

### [[20_Research/Papers/具身智能/DR-MPC_Fast_and_Feasible_Dynamics-Relaxed_Model-Predictive_Control_for_Legged_Locomotion|DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion]]

![[assets/2609.20035_figure.png|800]]

- **arXiv**: [2609.20035](https://arxiv.org/abs/2609.20035)
- **PDF**: https://arxiv.org/pdf/2609.20035
- **详细分析**: [[20_Research/Papers/具身智能/DR-MPC_Fast_and_Feasible_Dynamics-Relaxed_Model-Predictive_Control_for_Legged_Locomotion|DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion]]
- **作者**: Run Wang, Alapati Tuerxun, Shuo Liu, Wei Xiao, Ján Drgoňa, Yilin Mo, Liang Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《DR-MPC: Fast and Feasible Dynamics-Relaxed Model-Predictive Control for Legged Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents dynamics-relaxed model predictive control (DR-MPC), a novel MPC formulation for legged locomotion, and a tailored interior-point method (IPM) solver. The formulation combines online optimization feasibility by construction with a contact-aware input parameterization. DR-MPC moves the dynamics equality and affine input constraints into quadratic penalties and retains only nonempty box constraints. The resulting box-constrained quadratic program (QP) has a block-arrow Hessian that enables the state and affine-output directions to be eliminated through a Schur complement. The solver factors only the reduced control system after swing-force elimination and contact-aligned move blocking. For the evaluated implementations using the same DR-MPC formulation, our method achieves median end-to-end MPC speedups of $16.0\times$ over HPIPM and $4.4\times$ over OSQP, with comparable locomotion performance in simulation. DR-MPC achieves a median onboard MPC end-to-end time of $4.4$ ms and is validated on a Unitree Go1 quadruped. Open-source code will be made available after publication.

</details>

---

### [[20_Research/Papers/具身智能/Compliance_for_Free_Learning_Identifiable_Impedance_via_Bilateral_Teleoperation|Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation]]

![[assets/2609.19976_figure.png|800]]

- **arXiv**: [2609.19976](https://arxiv.org/abs/2609.19976)
- **PDF**: https://arxiv.org/pdf/2609.19976
- **详细分析**: [[20_Research/Papers/具身智能/Compliance_for_Free_Learning_Identifiable_Impedance_via_Bilateral_Teleoperation|Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation]]
- **作者**: Harsha Guda, Adrià Colomé, Carme Torras
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Compliance for Free: Learning Identifiable Impedance via Bilateral Teleoperation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FD-VLA, ForceVLA, HapticVLA, PaCo-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models tell a robot where to move, but not how hard to push. Contact-rich tasks depend on that second quantity, compliance, yet no widely used demonstration interface records it. The obstacle is identifiability as realized pose and measured force cannot separate the operator's intended equilibrium from their stiffness, so VR controllers, SpaceMouse and handheld grippers cannot supply compliance supervision even in principle. Prior compliance-output policies work around this with hand-specified task structure, privileged simulation contact state, or dedicated force and tactile hardware. Four-channel bilateral teleoperation removes the ambiguity directly by using the leader arm as a separate measurement of the intended equilibrium, making per-axis stiffness identifiable by regression using only the joint-torque sensing already on the manipulator. This yields per-timestep, direction-dependent compliance labels at zero annotation cost, which we use to fine-tune a VLA to emit stiffness alongside pose. On a Franka Research 3 wiping task, ours is the only policy of five whose contact force changes when the instruction asks for a firm wipe rather than a normal one (6.4N (normal) to 9.1N (firm) RMS, Cohen's d = 0.89, p = 0.023

</details>

---

### [[20_Research/Papers/强化学习/Hybrid_Residual_Reinforcement_Learning_for_Contact-Rich_Robotic_Book_Insertion|Hybrid Residual Reinforcement Learning for Contact-Rich Robotic Book Insertion]]

![[assets/2609.19962_figure.png|800]]

- **arXiv**: [2609.19962](https://arxiv.org/abs/2609.19962)
- **PDF**: https://arxiv.org/pdf/2609.19962
- **详细分析**: [[20_Research/Papers/强化学习/Hybrid_Residual_Reinforcement_Learning_for_Contact-Rich_Robotic_Book_Insertion|Hybrid Residual Reinforcement Learning for Contact-Rich Robotic Book Insertion]]
- **作者**: Tianyuan Liu, Rutherford Agbeshi Patamia, Benjamin Champion, Akansel Cosgun, Richard Dazeley
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.6，机器人 0.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Hybrid Residual Reinforcement Learning for Contact-Rich Robotic Book Insertion》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Placing a grasped book into a tight shelf is a compact but difficult contact-rich control problem: millimetre-scale pose error can turn a geometrically valid approach into jamming, failed release, or incomplete seating. We study this final phase after grasp acquisition and global approach, and ask how control authority should be divided between known geometry and learned behaviour. Our method retains a nominal task-space controller for structured insertion and seating, while residual PPO supplies bounded local corrections and decides when to release. Only the brief open-retreat-reclose transition is scripted. For the final policy used on hardware, a deployment-matched simulation evaluation over 512 fixed conditions yields 98.50 percent mean success (0.23 percentage-point sample SD) across three independent training runs, compared with 37.89 percent for nominal control. On the physical xArm7, 60 trials over 30 matched conditions show the same qualitative advantage: residual control raises success from 26.7 percent to 63.3 percent, reduces failures from 22 to 11, and wins 13 of the 15 matched conditions in which the two controllers differ. Robustness tests show that performance remains above 87 percent under initialization perturbations up to 1.5x, while very tight clearances expose the geometric limit of local correction. These results support a hybrid design in which geometry preserves reliable task structure and learning is concentrated on the contact-sensitive behaviour that fixed rules handle poorly.

</details>

---

### [[20_Research/Papers/机器人/Execution-Aware_Pre-Execution_Ranking_for_Grasp-Conditioned_Robotic_Placement|Execution-Aware Pre-Execution Ranking for Grasp-Conditioned Robotic Placement]]

![[assets/2609.19946_figure.png|800]]

- **arXiv**: [2609.19946](https://arxiv.org/abs/2609.19946)
- **PDF**: https://arxiv.org/pdf/2609.19946
- **详细分析**: [[20_Research/Papers/机器人/Execution-Aware_Pre-Execution_Ranking_for_Grasp-Conditioned_Robotic_Placement|Execution-Aware Pre-Execution Ranking for Grasp-Conditioned Robotic Placement]]
- **作者**: Tianyuan Liu, Rutherford Agbeshi Patamia, Benjamin Champion, Richard Dazeley, Akansel Cosgun
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Execution-Aware Pre-Execution Ranking for Grasp-Conditioned Robotic Placement》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Dex-Net, PointNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A geometrically valid placement can still be difficult to execute because the selected grasp changes the required end-effector pose, collision geometry, and transport motion. Placement is formulated as a pre-execution ranking problem in which supplied grasp-placement candidates are scored before planning. The model combines a typed target-conditioned point cloud with three pose descriptors and hierarchical heads for planning success and execution success conditioned on planning. On a 30-object, 1,235-scene dataset with scene-group-held-out splits, three-seed top-1 success on covered test groups reaches 85.63 +/- 1.08% for joint selection and 79.84 +/- 0.16% for fixed-target ranking. For the designated frozen seed-42 checkpoint, top-1 success improves from 72.84% to 85.78% over full-pool cuMotion for joint ranking and from 59.65% to 79.67% for fixed-target ranking. Frozen transfer to xArm7/MoveIt requires no xArm-specific retraining. Across 27 locked cases, 13 complete end to end (48.15%). Of the 16 cases that pass Top-5 preflight and begin execution, 13 succeed (81.25%). Candidate-level deployment-feasibility prediction reaches 81.25% recall, 85.20% specificity, and 83.23% balanced accuracy.

</details>

---

### [[20_Research/Papers/具身智能/Co-VLA_Consensus-based_Federated_Training_for_Vision-Language-Action_Models|Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models]]

![[assets/2609.19923_figure.png|800]]

- **arXiv**: [2609.19923](https://arxiv.org/abs/2609.19923)
- **PDF**: https://arxiv.org/pdf/2609.19923
- **详细分析**: [[20_Research/Papers/具身智能/Co-VLA_Consensus-based_Federated_Training_for_Vision-Language-Action_Models|Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models]]
- **作者**: Haolong Li, Guner Dilsad Er, Michael Muehlebach, Joerg Stueckler
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.7，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《Co-VLA: Consensus-based Federated Training for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Co-VLA, FedVLA, OpenVLA, Real-World, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs) have emerged as a promising paradigm for general-purpose robot learning, with performance improving as models and datasets scale. Scaling robot data collection, however, remains challenging because data are naturally distributed across robots, tasks, and locations, making centralization costly or impractical. Federated learning offers a way to train on decentralized robot data, but applying it to VLAs requires accounting for heterogeneous robot client data distributions. We present Co-VLA, which applies consensus optimization using the Alternating Direction Method of Multipliers~(ADMM) to federated VLA training. We show that the same algorithm supports both full-model training and parameter-efficient fine-tuning with both fixed-rank and rank-adaptive adapters. The name Co-VLA reflects both consensus and collaboration: clients with different local robot datasets collaboratively train a shared model without sharing their data. Our experiments demonstrate that Co-VLA achieves performance comparable to centralized training in both full-model training and parameter-efficient fine-tuning settings.

</details>

---

### [[20_Research/Papers/强化学习/GR2PO_Group_Relative_Return_Policy_Optimization_for_Continuous_Robot_Control|GR2PO: Group Relative Return Policy Optimization for Continuous Robot Control]]

![[assets/2609.19850_figure.png|800]]

- **arXiv**: [2609.19850](https://arxiv.org/abs/2609.19850)
- **PDF**: https://arxiv.org/pdf/2609.19850
- **详细分析**: [[20_Research/Papers/强化学习/GR2PO_Group_Relative_Return_Policy_Optimization_for_Continuous_Robot_Control|GR2PO: Group Relative Return Policy Optimization for Continuous Robot Control]]
- **作者**: Pengqin Wang, Qiming Zhang, Shaojie Shen, Jun Ma
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 2.6（加权：具身智能 0.3，强化学习 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《GR2PO: Group Relative Return Policy Optimization for Continuous Robot Control》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actor-critic architecture has been widely used in continuous robot control. However, they rely on learning a value network, introducing additional computational overhead during training. Moreover, policy learning may also be affected by the approximation error of value estimation. Critic-free group relative policy optimization methods provide a simpler training approach by removing the need for a critic. However, they fail to learn long-term action outcomes when directly applying immediate rewards to policy optimization in dense-reward environments. To address these problems, we propose Group Relative Return Policy Optimization (GR2PO), a critic-free reinforcement learning framework for continuous robot control. GR2PO estimates the discounted returns from the parallelly collected trajectories, performs group normalization at each rollout time index, and uses relative advantages and clipped targets to update the policy. To evaluate the effectiveness of the proposed framework, we instantiate it on robot control simulation environments and deploy the model to a real-world edge device. The results show that GR2PO significantly outperforms critic-free baselines that use immediate rewards and performs competitively against state-of-the-art actor-critic methods. Furthermore, GR2PO demonstrates competitive training efficiency. Inference tests on NVIDIA Jetson TX2 demonstrate the feasibility of deploying the learned policies on edge platforms. Further ablation experiments analyze the effects of parallel group size, return estimation methods, and target clipping ratio on learning performance. To support follow-up research, we will make the complete code publicly available after the paper is accepted, including the framework implementation, experimental configuration, and training and evaluation scripts.

</details>

---

### [[20_Research/Papers/具身智能/TADreamer_Zero-Shot_Language-Guided_3D_Navigation_for_Terrestrial-Aerial_Bimodal_Robots_via_Video_Imagination|TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination]]

![[assets/2609.19824_figure.png|800]]

- **arXiv**: [2609.19824](https://arxiv.org/abs/2609.19824)
- **PDF**: https://arxiv.org/pdf/2609.19824
- **详细分析**: [[20_Research/Papers/具身智能/TADreamer_Zero-Shot_Language-Guided_3D_Navigation_for_Terrestrial-Aerial_Bimodal_Robots_via_Video_Imagination|TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination]]
- **作者**: Xiangyu Li, Tiancheng Lai, Xijie Huang, Ruitian Pang, Siqi Shen, Juncheng Chen, Zaisheng Pan, Chao Xu, Fei Gao, Yanjun Cao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《TADreamer: Zero-Shot Language-Guided 3D Navigation for Terrestrial-Aerial Bimodal Robots via Video Imagination》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-guided navigation for terrestrial-aerial bimodal robots requires selecting routes and locomotion modes that match scene context and task intent. Generated videos can represent such motion sequences, but recovering metrically consistent navigation references from them is challenging because of scale ambiguity and axis-dependent geometric distortions. We present TADreamer, a zero-shot framework that grounds video-imagined navigation in measured geometry without task-specific training or fine-tuning. A vision-language model translates onboard observations and instructions into navigation prompts, selects valid generated videos, and provides corrective feedback when regeneration is needed. The selected video is reconstructed into 3D waypoints annotated with terrestrial or aerial modes. A two-stage calibration procedure uses field-of-view constraints to initialize scale estimation, then refines axis-dependent scales, rotation, and translation by registering the reconstructed point cloud to measured geometry. The calibrated waypoints and mode labels guide a planner that incorporates measured geometry for robot execution. Real-world experiments demonstrate navigation across seven indoor and outdoor scenarios. With five candidates per round, usable videos are obtained within two rounds in all seven scenarios. On the calibration observations, our method reduces mean absolute depth error by 87.7% and mean absolute relative depth error by 86.3% compared with NavDreamer.

</details>

---

### [[20_Research/Papers/大模型/HEROIC_Heterogeneous_Evidential_Reasoning_for_Open-Vocabulary_Identification_and_Cross-Robot_Collaboration|HEROIC: Heterogeneous Evidential Reasoning for Open-Vocabulary Identification and Cross-Robot Collaboration]]

![[assets/2609.19803_figure.png|800]]

- **arXiv**: [2609.19803](https://arxiv.org/abs/2609.19803)
- **PDF**: https://arxiv.org/pdf/2609.19803
- **详细分析**: [[20_Research/Papers/大模型/HEROIC_Heterogeneous_Evidential_Reasoning_for_Open-Vocabulary_Identification_and_Cross-Robot_Collaboration|HEROIC: Heterogeneous Evidential Reasoning for Open-Vocabulary Identification and Cross-Robot Collaboration]]
- **作者**: Mihir Chauhan, Aarav Jain, Addison Zucek, Manmeet Dang, Damon Conover, Aniket Bera
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《HEROIC: Heterogeneous Evidential Reasoning for Open-Vocabulary Identification and Cross-Robot Collaboration》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent heterogeneous air-ground robot teams are attractive for open world search, with applications for reconnaissance, urban search and rescue missions (USAR), disaster response and recovery, and hazardous environments. These two platforms have different failure modes: aerial robots cover ground quickly but cannot resolve small or occluded targets from altitude, while ground robots can identify objects-of-interest, such as people or hazardous objects, at close range but cover less area. Existing language-tasked teams either have roles fixed prior, or have a language model assign them from hand-written capability tags, so the team is unable to know when within a mission an asset is no longer useful. We present HEROIC, a decentralized heterogeneous multi-agent open-vocabulary search coordination framework that requires agents to communicate in natural language only. HEROIC's initial agent role assignment is derived from sensor properties and a scale law to determine whether targets can be detected with a high confidence. From the mission's natural language prompt alone, this law assigns aerial flight altitudes and sweep spacing. When this calculated height falls below the altitude for safe flight, aerial agents re-task themselves from searcher to aerial triage, escort, and route guide for ground agents. Both robots maintain an evidential belief over the search area (bearing rays for positive evidence, a log-odds posterior for negative evidence) and gate any arrival on close-range verification. In full-stack experiments, HEROIC reaches the target 84% of the time across all 6 scenes, compares to 35-54% for vision-language frontier baselines, frontier-based search, lawnmower, and random-walk running the same perception, all while being 2-4x sooner to arrive at the target.

</details>

---

### [[20_Research/Papers/具身智能/LIFD_Anchored_Diffusion_for_3D-Aware_Scene_Memory_in_Robotic_Manipulation|LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation]]

![[assets/2609.19796_figure.png|800]]

- **arXiv**: [2609.19796](https://arxiv.org/abs/2609.19796)
- **PDF**: https://arxiv.org/pdf/2609.19796
- **详细分析**: [[20_Research/Papers/具身智能/LIFD_Anchored_Diffusion_for_3D-Aware_Scene_Memory_in_Robotic_Manipulation|LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation]]
- **作者**: Wenbo Li, Yiteng Chen, Wenhao Li, Qingyao Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《LIFD: Anchored Diffusion for 3D-Aware Scene Memory in Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：BridgeVLA, FabriVLA, LA4VLA, MemoryVLA, MetaWorld, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation under partial observability requires spatial information that extends beyond the current view. Geometry-aware RGB features describe visible structure, but previously observed regions may disappear as the robot or scene moves. Maintaining a useful scene representation therefore requires retaining observation history while inferring missing content without losing its connection to visible evidence. We introduce LIFD (Look, Imagine, Focus, and Do), a framework for persistent, 3D-aware scene memory. LIFD learns a scene-token representation from multi-view agreement and completes it from a single RGB view and recurrent memory. A rectified-flow model generates the tokens while Anchor-Guided Cross-Attention conditions completion on current geometric features. Compact slot features connect this representation to a manipulation policy. Multi-view and geometric supervision are used during representation learning; deployment requires one RGB camera, proprioception, and a task instruction. LIFD (Staged) reaches 91.6% average success on LIBERO and 79.8% on MetaWorld, improving LIBERO average success by 3.1 percentage points over Joint training. On four UR5e task families with ten demonstrations per family, it achieves 56.0% mean success, compared with 40.5% for OpenVLA-7B.

</details>

---

### [[20_Research/Papers/具身智能/Towards_High-DoF_Dexterous_Manipulation_through_VLA_Post-Training|Towards High-DoF Dexterous Manipulation through VLA Post-Training]]

![[assets/2609.19666_figure.png|800]]

- **arXiv**: [2609.19666](https://arxiv.org/abs/2609.19666)
- **PDF**: https://arxiv.org/pdf/2609.19666
- **详细分析**: [[20_Research/Papers/具身智能/Towards_High-DoF_Dexterous_Manipulation_through_VLA_Post-Training|Towards High-DoF Dexterous Manipulation through VLA Post-Training]]
- **作者**: Junlei Zhu, Shenzhe Yao, Chaogui Huang, Wenkai Zhu, Jingwei Peng, Guanqi He, Soren Schwertfeger, Jiahao Chen, Yide Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.4（加权：具身智能 2.7，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Towards High-DoF Dexterous Manipulation through VLA Post-Training》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation-learned vision--language--action (VLA) foundation models acquire broad manipulation capabilities by scaling robot data across tasks and embodiments, but reliable deployment on a specific downstream task and hardware platform still requires post-training. Dexterous hands make this adaptation particularly difficult: their broad behavioural repertoire and high degree of freedom create a large and structured action space. Three obstacles are central: open-source VLAs do not natively provide an action interface for high-DoF hands; gesture mismatch during human-gated DAgger takeover creates command discontinuities and contaminates corrective trajectories; and reinforcement learning in the raw joint space is sample-inefficient. We present a unified four-step post-training pipeline comprising a learned temporal hand-action codec, supervised fine-tuning, DAgger, and real-world residual reinforcement learning. The codec adapts a pretrained VLA to absolute dexterous-hand commands. Buffered rollback, pose alignment, and smooth command blending enable continuous, task-relevant DAgger corrections, while latent residual RL confines exploration to coordinated hand motions captured by the codec. We evaluate the pipeline on five diverse real-world tasks spanning bimanual transfer, in-hand reorientation, and tool use. Within the reported post-training budgets, the resulting policies achieve 100\% success on every evaluated task over 20 trials per task. These results provide a practical path for adapting VLA foundation models to reliable real-world dexterous manipulation.

</details>

---

### [[20_Research/Papers/强化学习/Runtime_Safety_Filtering_for_Two-Terminal_Hazards_in_Robotic_Battery_Recycling|Runtime Safety Filtering for Two-Terminal Hazards in Robotic Battery Recycling]]

![[assets/2609.19665_figure.png|800]]

- **arXiv**: [2609.19665](https://arxiv.org/abs/2609.19665)
- **PDF**: https://arxiv.org/pdf/2609.19665
- **详细分析**: [[20_Research/Papers/强化学习/Runtime_Safety_Filtering_for_Two-Terminal_Hazards_in_Robotic_Battery_Recycling|Runtime Safety Filtering for Two-Terminal Hazards in Robotic Battery Recycling]]
- **作者**: Yuxin Cao, Wei Song, Xianglin Yang, Fusen Guo, Lin Li, Xiao Cheng, Jin Song Dong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Runtime Safety Filtering for Two-Terminal Hazards in Robotic Battery Recycling》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Runtime safety filters for learned manipulation policies typically define unsafe states as unions of object-wise keep-out regions. This representation can be unnecessarily restrictive for hazards that depend on a joint spatial relation, such as battery recycling, where a conductive payload can short a charged cell only when it approaches both terminals simultaneously. We study runtime filtering for this two-terminal hazard in LIBERO using frozen OpenVLA policies. We factor a runtime filter into three design choices: the predicate structure, its geometric margin, and the fallback action applied when a commanded action is rejected. We compare a conjunctive predicate, a conventional two-site keep-out, and a composite of the two. For each predicate, we vary its margin to obtain a frontier between task success and residual hazard. We then compare four fallback strategies at matched operating points: holding, retreat, sampled search, and a continuous-action barrier projection. Across three workcells, the three predicate families trace nearly identical safety--utility frontiers once each is evaluated over its own margin. In contrast, the fallback strategy has a substantially larger effect: holding reduces task success by up to 0.302 relative to retreat without reducing hazard, while both minimally invasive fallbacks leave substantially more residual hazard. This ordering transfers to a second policy and task suite, while retreat-based filtering remains effective under standing errors in the clearances available to the filter, although correlated error in the estimated payload size is more damaging than larger independent errors in terminal position. These results show that, for proximity-defined manipulation hazards, margin selection and fallback strategy can matter more than predicate structure in determining the safety--utility trade-off of a runtime filter.

</details>

---

### [[20_Research/Papers/大模型/ReShoot_Generative_Visual_Domain_Randomization_of_Recorded_Robot_Demonstrations_for_Visuomotor_Policy_Learning|ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning]]

![[assets/2609.19661_figure.png|800]]

- **arXiv**: [2609.19661](https://arxiv.org/abs/2609.19661)
- **PDF**: https://arxiv.org/pdf/2609.19661
- **详细分析**: [[20_Research/Papers/大模型/ReShoot_Generative_Visual_Domain_Randomization_of_Recorded_Robot_Demonstrations_for_Visuomotor_Policy_Learning|ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning]]
- **作者**: Chiyoung Kim, Min Sung Choi, Jinho Ju, Chanhoe Gu, Donghwan Hwang, Wonseok Choi, Woongsun Jeon, Minhyeok Lee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《ReShoot: Generative Visual Domain Randomization of Recorded Robot Demonstrations for Visuomotor Policy Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ControlNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation-learned robot policies are frequently overfit to the visual conditions present in their training demonstrations. Consequently, variations in object color or background appearance often induce substantial performance degradation. A common mitigation strategy is to acquire additional demonstrations in each novel visual context; however, this approach is resource-intensive, requiring repeated access to a robot, a controlled environment, and human operation for every appearance condition to be covered. We introduce ReShoot, a framework that synthesizes visual diversity by re-rendering previously recorded demonstrations under altered appearances, thereby shifting the burden from data collection to generation. A vision-language model captions the scene, edits a targeted attribute (e.g., background, object color, or material), and an edge-conditioned video generator re-renders both camera views to match. The instruction is updated accordingly. The action sequence and proprioceptive trajectory are copied verbatim without relabeling, so each generated episode retains the recorded action and proprioceptive labels. On LIBERO, a policy trained on an equal mixture of recorded and re-rendered demonstrations matches the performance of recorded-only training (96.5% vs. 96.9%). Moreover, the mixed training set improves robustness to scene perturbations on LIBERO-Plus (85.5% vs. 82.3%). Across two physical robotic platforms, deploying ReShoot with 43 and 100 pre-collected demonstrations increased the success rate on recolored objects from 0.0% to 42.9% and 47.5%, respectively, while maintaining performance under the original recorded appearance.

</details>

---

### [[20_Research/Papers/具身智能/WorldContact_A_Contact-Centric_World_Model_for_Scalable_Robot_Learning|WorldContact: A Contact-Centric World Model for Scalable Robot Learning]]

![[assets/2609.19600_figure.png|800]]

- **arXiv**: [2609.19600](https://arxiv.org/abs/2609.19600)
- **PDF**: https://arxiv.org/pdf/2609.19600
- **详细分析**: [[20_Research/Papers/具身智能/WorldContact_A_Contact-Centric_World_Model_for_Scalable_Robot_Learning|WorldContact: A Contact-Centric World Model for Scalable Robot Learning]]
- **作者**: Caoliwen Wang, Mengdi Wang, Heng Zhang, Shixun Huang, Siyuan Chen, Chao Liu, Anpei Chen, Zhendong Wang, Peter Yichen Chen, Huamin Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.5（加权：具身智能 0.6，世界模型 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《WorldContact: A Contact-Centric World Model for Scalable Robot Learning》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DPI-Net, IRASim, PointWorld, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adapting robots to new objects and tasks requires interaction experience that can be costly to obtain. We present WorldContact, a contact-centric world model for deformable-object manipulation, constructed from a limited set of high-quality trajectories to generate additional training data efficiently. It predicts object dynamics using larger time steps than the source numerical simulator, which requires small integration steps to resolve rapid motion and prevent interpenetration. We evaluate WorldContact across 16 shopping-bag manipulation tasks. State-rollout measurements on a single H100 GPU show a $10\times$ speedup over the source simulator, excluding rendering and disk I/O. We use the generated data to fine-tune an existing vision-language-action policy and deploy it directly on a real robot. In bag lifting, the same policy achieves 65% single-attempt success when fine-tuned on source simulation data alone, compared with 95% when fine-tuned on the dataset expanded with WorldContact. These results support efficient data generation with WorldContact for robot policy adaptation.

</details>

---

### [[20_Research/Papers/具身智能/Quantifying_Mechanical_Intelligence_in_Legged_Robots_with_Information_Theory|Quantifying Mechanical Intelligence in Legged Robots with Information Theory]]

![[assets/2609.19588_figure.png|800]]

- **arXiv**: [2609.19588](https://arxiv.org/abs/2609.19588)
- **PDF**: https://arxiv.org/pdf/2609.19588
- **详细分析**: [[20_Research/Papers/具身智能/Quantifying_Mechanical_Intelligence_in_Legged_Robots_with_Information_Theory|Quantifying Mechanical Intelligence in Legged Robots with Information Theory]]
- **作者**: Zach J. Patterson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Quantifying Mechanical Intelligence in Legged Robots with Information Theory》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mechanical intelligence, loosely defined as the reduction in control burden afforded by a robot's physical form, has become a prominent concept in robotics, with instantiations in bioinspired robotics, soft robotics, robotic swarms, and many other areas. However, rigorous theoretical understanding and quantitative measures of mechanical intelligence have lagged behind the engineering systems that the community has developed. In this work, using modern legged robots as a benchmark and exemplar, we propose several information-theoretic metrics for quantifying mechanical intelligence. By viewing body dynamics as both a computational process and a communication channel, we show that several prior insights in legged-robot engineering can be described using information theory, and we quantify how bits are processed by mechanical modes and across robot coordinates. Specifically, we examine the trade-off between explicitly incorporating compliance through series-elastic actuation and using so-called proprioceptive, low-gear-ratio transmissions, and we explore how these mechanisms interact with control policies during locomotion. We develop these results on systems of increasing complexity: a simplified linear model of a robot-leg transmission, a nonlinear single-leg simulation, and simulated quadruped robots controlled by a learned policy while navigating challenging terrain. These results lay the groundwork for broader study of robot mechanisms and their role in embodied computation.

</details>

---

### [[20_Research/Papers/机器人/OmniCalib_Target-Free,_Task-Structured_Self-Calibration_for_Humanoid_Robots|OmniCalib: Target-Free, Task-Structured Self-Calibration for Humanoid Robots]]

![[assets/2609.19582_figure.png|800]]

- **arXiv**: [2609.19582](https://arxiv.org/abs/2609.19582)
- **PDF**: https://arxiv.org/pdf/2609.19582
- **详细分析**: [[20_Research/Papers/机器人/OmniCalib_Target-Free,_Task-Structured_Self-Calibration_for_Humanoid_Robots|OmniCalib: Target-Free, Task-Structured Self-Calibration for Humanoid Robots]]
- **作者**: Kaixiang Lu, Haiyu Lan, Chunxiao Qiao, You Li, Enyu Li, Yehao Lu, Jiarui Yang, Peiwen Lin, Chuang Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 1.5，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《OmniCalib: Target-Free, Task-Structured Self-Calibration for Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assembly, wear, and component replacement perturb the sensor extrinsics and joint zeros encoded by a humanoid CAD model. Existing procedures calibrate one sensor pair or require external fiducials. Using only robot-native motion and onboard sensing, we present OmniCalib, a target-free workflow that calibrates the full upper limbs---all 14 arm joint zeros and the extrinsics of both wrist and chest cameras---as well as lower limbs and the multi-camera head rig. Each module matches a robot-native task to a parameter block, checks observability, and writes only supported corrections to the CAD model. Our depth ICP method recovers all 14 arm joint zeros and calibrates all RGB-D camera extrinsics without any calibration target. Relative to CAD, the estimated extrinsic corrections are 10.56 mm and 1.74 degrees for the left wrist, 6.33 mm and 1.25 degrees for the right wrist, and 9.81 mm and 0.929 degrees for the chest RGB-D camera. ICP point-to-plane residual is 2.09 mm. On the same injected offsets, ICP and ArUco recover all 14 joint zeros below the 0.1-degree encoder-resolution reference. On an AGIBOT A3 Ultra humanoid, four static double-support stances recover all 12 lower-limb joint-zero offsets injected with an RMS error of 0.063 degrees. The head module combines multi-camera visual odometry with legged odometry and dynamic compensation through the live ROS transform tree. Using only planar walking, it attains a mean SO(3) error of 1.061 degrees across three sequences. The best sequence reaches 0.775 degrees, competitive with iKalibr at 0.902 degrees from rich 6-DOF excitation. Rig-relative angles repeat within 0.140 degrees. Injection recovery and held-out tests validate each observable block.

</details>

---

### [[20_Research/Papers/具身智能/Recovering_Aggressively_Pruned_Vision-Language-Action_Models_with_Offline_Hidden-State_Distillation|Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation]]

![[assets/2609.19579_figure.png|800]]

- **arXiv**: [2609.19579](https://arxiv.org/abs/2609.19579)
- **PDF**: https://arxiv.org/pdf/2609.19579
- **详细分析**: [[20_Research/Papers/具身智能/Recovering_Aggressively_Pruned_Vision-Language-Action_Models_with_Offline_Hidden-State_Distillation|Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation]]
- **作者**: Chiyoung Kim, Sanghyuk Roy Choi, Minhyeok Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models let robots follow language instructions, but their language backbones of several billion parameters are the main obstacle to running them on robot hardware. Structured pruning reduces that backbone, and removing 63% of it from OpenVLA-OFT drops LIBERO-Long success from 93.2% to 0.8%. A recent approach restores such a model with supervised fine-tuning followed by reinforcement learning, which needs online rollouts and hundreds of GPU-hours. We recover most of the lost success entirely offline. Width pruning narrows the blocks but keeps the residual stream at its original size, so teacher and student hidden states have the same shape and are matched directly, without a projector. Training against a cache built in one teacher pass lifts the 63%-reduced student to within 3.5 points of the teacher in about 8 GPU-hours. A sweep over nine ratios locates where the recovery objective starts to matter. Up to 45% reduction the two do not differ significantly on OpenVLA-OFT. Hidden-state distillation then adds +2.1 to +4.5 points there between 63% and 87%, and +9.4 to +22.1 points on CogACT from 63% onward. At 81% on CogACT, a tripled recovery budget narrows the distilled student's gap to the teacher to 3.9 points on average, while supervised recovery stays more than 20 points below. At matched compression, width pruning yields higher success and depth pruning lower latency. On a 6-DoF manipulator, the distilled student at 72% reduction reaches 77.5% success against 59.5% for supervised recovery, runs 2.23x faster on-board than the teacher, and uses 62% less memory.

</details>

---

### [[20_Research/Papers/机器人/SLAMSqueezeBench_Comparing_SLAM_Systems_under_Resource_Constraints|SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints]]

![[assets/2609.19533_first_page.png|800]]

- **arXiv**: [2609.19533](https://arxiv.org/abs/2609.19533)
- **PDF**: https://arxiv.org/pdf/2609.19533
- **详细分析**: [[20_Research/Papers/机器人/SLAMSqueezeBench_Comparing_SLAM_Systems_under_Resource_Constraints|SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints]]
- **作者**: Mohamed Hefny, Karthik Dantu, Steven Y. Ko
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《SLAMSqueezeBench: Comparing SLAM Systems under Resource Constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：SLAMSqueezeBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simultaneous localization and mapping (SLAM) is one of the services running on an autonomous robot. It is typically run to assist other tasks such as planning, manipulation, etc. All these tasks are run on edge hardware and are subject to severe resource constraints. However, most SLAM systems are built and tested in isolation, and their performance is reported as if they are the only task running on a system. We observe that existing benchmarks lack a common mechanism for comparing SLAM systems under realistic resource constraints. To address this limitation, we have developed SLAMSqueezeBench, a framework that allows testing of SLAM systems under realistic workloads on edge hardware. It does so by imposing constraints on compute and memory resources available for the SLAM system during execution. It also simulates realistic camera frame acquisition with frame drops when a finite buffer is full. Using SLAMSqueezeBench, we compare nine SLAM systems spanning classical systems, learning-based systems, and approaches for Gaussian splatting. Our testing framework will be available for use by the community upon publication.

</details>

---

### [[20_Research/Papers/机器人/PIVOT_Perception-aware_Independent_Viewpoint_Online_Optimization|PIVOT: Perception-aware Independent Viewpoint Online Optimization]]

![[assets/2609.19510_first_page.png|800]]

- **arXiv**: [2609.19510](https://arxiv.org/abs/2609.19510)
- **PDF**: https://arxiv.org/pdf/2609.19510
- **详细分析**: [[20_Research/Papers/机器人/PIVOT_Perception-aware_Independent_Viewpoint_Online_Optimization|PIVOT: Perception-aware Independent Viewpoint Online Optimization]]
- **作者**: Yuyang Chen, Shekoufeh Sadeghi, Charuvahan Adhivarahan, Elton Lemos, Chen Wang, Sanjeev J. Koppal, Karthik Dantu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《PIVOT: Perception-aware Independent Viewpoint Online Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A fundamental assumption in robotic perception is that the sensor's field of view (FoV) is fixed relative to the robot body. Motion-decoupled sensors, such as gimbal-mounted cameras and MEMS-based LiDARs, instead allow sensing direction to be controlled independently at runtime. This freedom creates a computational challenge: efficiently selecting useful viewing directions online in feature-dense environments. We propose PIVOT, a lightweight iterative method that optimizes sensor viewing direction along a fixed translation trajectory to maximize feature visibility. Under a conical FoV model, visibility depends only on the optical axis, yielding a two-degree-of-freedom optimization on the viewing sphere $S^2$. Coordinate-free $SO(3)$ exponential-map updates enable efficient continuous optimization without explicit angular parameterizations or exhaustive viewing-sphere search. Monte Carlo evaluations retain 98.1--99.6% of brute-force visibility with a 76--85x speedup. Photorealistic simulation and real-world experiments further demonstrate improved visual localization robustness and practical viewpoint control on a quadruped robot.

</details>

---

### [[20_Research/Papers/具身智能/FASA_Feedback-Aware_Sampling_Adaptation_for_Efficient_Diffusion-Based_VLA_Models|FASA: Feedback-Aware Sampling Adaptation for Efficient Diffusion-Based VLA Models]]

![[assets/2609.19475_figure.png|800]]

- **arXiv**: [2609.19475](https://arxiv.org/abs/2609.19475)
- **PDF**: https://arxiv.org/pdf/2609.19475
- **详细分析**: [[20_Research/Papers/具身智能/FASA_Feedback-Aware_Sampling_Adaptation_for_Efficient_Diffusion-Based_VLA_Models|FASA: Feedback-Aware Sampling Adaptation for Efficient Diffusion-Based VLA Models]]
- **作者**: Yuchen Han, Jianhan Wu, Xiaoyang Qu, Lingwei Kong, Shiyi Li, Jianzong Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 2.4，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《FASA: Feedback-Aware Sampling Adaptation for Efficient Diffusion-Based VLA Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based Vision-Language-Action (VLA) models achieve strong performance in embodied tasks, but their iterative sampling imposes heavy computational and memory-access cost, blocking real-time deployment on edge platforms. Existing acceleration methods either require expensive training (e.g., distillation, flow matching) or degrade perception via statically scheduled pruning and caching, ignoring the dynamic workload variance of robotic interactions. This paper presents FASA (Feedback-Aware Sampling Adaptation), a training-free runtime framework that treats real-time multimodal feedback as a control signal for the denoising pipeline: an interaction-driven range adaptor modulates the global sampling-step budget based on visual and gripper-force feedback, and a proprioception-aware step adaptor pinpoints the optimized step within the adapted range. This co-designed framework allows the underlying hardware architecture to adaptively match the workload demands of different execution phases. Comparative evaluations across several benchmarks show that the inference speed can be increased by up to 1.45$\times$ while maintaining competitive success rates, providing a novel dynamic runtime architecture paradigm for deploying heavy generative embodied AI workloads onto resource-constrained computing platforms.

</details>

---

### [[20_Research/Papers/大模型/Pose-aware_Legged_Robot_Semantic_Exploration_with_Omnidirectional_Perception_in_Confined_Unknown_Environments|Pose-aware Legged Robot Semantic Exploration with Omnidirectional Perception in Confined Unknown Environments]]

![[assets/2609.19460_figure.png|800]]

- **arXiv**: [2609.19460](https://arxiv.org/abs/2609.19460)
- **PDF**: https://arxiv.org/pdf/2609.19460
- **详细分析**: [[20_Research/Papers/大模型/Pose-aware_Legged_Robot_Semantic_Exploration_with_Omnidirectional_Perception_in_Confined_Unknown_Environments|Pose-aware Legged Robot Semantic Exploration with Omnidirectional Perception in Confined Unknown Environments]]
- **作者**: Xiaoyang Zhan, Shiyu Chen, Kenji Shimada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Pose-aware Legged Robot Semantic Exploration with Omnidirectional Perception in Confined Unknown Environments》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Semantic exploration in confined environments requires both environment mapping and detailed observation of target objects. For ground robots, limited sensor vertical fields of view and restricted standoff distances can leave upper object surfaces unobserved from planar viewpoints. Body tilting can improve coverage, but additional observations and posture transitions increase mission time. To address this trade-off, we present POSE, a pose-aware semantic exploration system that exploits a legged robot's intrinsic body pitch and roll with omnidirectional camera-LiDAR perception. The proposed pose-aware viewpoint sampling module selects body postures from partial object maps according to expected coverage gain, while aim-aligned execution reduces unnecessary body reorientation. Further, we introduce an object-centric viewpoint pruning strategy assisted by a vision-language model (VLM), which uses persistent observation history and bird's-eye-view (BEV) maps to reduce redundant inspection visits. The resulting semantic viewpoints are combined with geometric exploration viewpoints in a global exploration planner. Simulations show that POSE improves final target-surface coverage by 8-10 percentage points over the planar planning baseline while reducing exploration time by 17-32%, and achieves the highest mean object coverage AUC among the evaluated baselines. Real-world experiments with a legged robot carrying an omnidirectional camera-LiDAR suite in a machine shop further demonstrate the system's applicability. These results support adaptive body-posture planning for improving the coverage-efficiency trade-off in legged robot semantic exploration. We plan to release the code for community benefit in the future.

</details>

---

### [[20_Research/Papers/强化学习/Winning_a_Won_Game_Strict_Reach-Avoid-Stay_Control_Barrier_Functions_for_High-Dimensional_Black-Box_Systems|Winning a Won Game: Strict Reach-Avoid-Stay Control Barrier Functions for High-Dimensional Black-Box Systems]]

![[assets/2609.19449_figure.png|800]]

- **arXiv**: [2609.19449](https://arxiv.org/abs/2609.19449)
- **PDF**: https://arxiv.org/pdf/2609.19449
- **详细分析**: [[20_Research/Papers/强化学习/Winning_a_Won_Game_Strict_Reach-Avoid-Stay_Control_Barrier_Functions_for_High-Dimensional_Black-Box_Systems|Winning a Won Game: Strict Reach-Avoid-Stay Control Barrier Functions for High-Dimensional Black-Box Systems]]
- **作者**: Donggeon David Oh, Duy P. Nguyen, Gongkai Yuan, Qingchen Li, Jaime Fernández Fisac, Haimin Hu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《Winning a Won Game: Strict Reach-Avoid-Stay Control Barrier Functions for High-Dimensional Black-Box Systems》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots must complete their tasks and maintain the achieved outcomes while avoiding safety failures at all times. Strict reach-avoid-stay (sRAS) formalizes this requirement: safely reaching a target and remaining there indefinitely after first entry. We propose an sRAS Q-control barrier function (CBF) safety filter for high-dimensional black-box systems under bounded uncertainty. Our construction combines a stay value encoding safe permanent residence in a target subset with a reach-avoid value encoding safe reachability of this subset while avoiding target states from which safe permanent residence cannot be guaranteed. We prove that these values jointly yield a valid robust discrete-time CBF and lift them to state-action Q-functions for runtime intervention. For exact values and under a measure-zero condition, our filter preserves sRAS feasibility from almost every winnable initial state and keeps the system safely within the target after first entry, against all admissible uncertainty realizations. We adopt reachability-based adversarial reinforcement learning for scalable value approximation using only black-box interactions. Notably, neither synthesis nor deployment of our filter requires known dynamics, affine structure, value derivatives, or hand-designed barriers. We validate our framework in quadruped gap jumping in simulation and hardware, where the robot crosses the gap, lands safely, and remains safe afterward. Simulated F1TENTH races further demonstrate safe overtaking and lead retention.

</details>

---

### [[20_Research/Papers/强化学习/From_Wizard-of-Oz_Human-Robot_Dialogue_Collection_to_a_Taxonomy_of_Robot_Response_Decisions_A_Retrospective_Analysis_of_Assistive_Pilot_Inte|From Wizard-of-Oz Human-Robot Dialogue Collection to a Taxonomy of Robot Response Decisions: A Retrospective Analysis of Assistive Pilot Interactions]]

![[assets/2609.19447_figure.png|800]]

- **arXiv**: [2609.19447](https://arxiv.org/abs/2609.19447)
- **PDF**: https://arxiv.org/pdf/2609.19447
- **详细分析**: [[20_Research/Papers/强化学习/From_Wizard-of-Oz_Human-Robot_Dialogue_Collection_to_a_Taxonomy_of_Robot_Response_Decisions_A_Retrospective_Analysis_of_Assistive_Pilot_Inte|From Wizard-of-Oz Human-Robot Dialogue Collection to a Taxonomy of Robot Response Decisions: A Retrospective Analysis of Assistive Pilot Interactions]]
- **作者**: Guangping Liu, Nicholas Hawkins, Tipu Sultan, Flavio Esposito, Madi Dian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《From Wizard-of-Oz Human-Robot Dialogue Collection to a Taxonomy of Robot Response Decisions: A Retrospective Analysis of Assistive Pilot Interactions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots that follow natural-language instructions in everyday indoor environments must act on incomplete human utterances. Instructions often omit essential information, such as the identity of an out-of-view object, an intended destination, or the user's goal. Existing datasets contain little real-world situated dialogue and provide few practice-grounded criteria for deciding when a robot should act, confirm, clarify, or refuse. We retrospectively analyze a pilot Wizard-of-Oz study in which five participants performed everyday indoor tasks, including door opening, drawer opening, feeding, drinking, and cleaning, with a wheelchair-mounted mobile manipulator while the wizard responded without a formal communication policy. This preserved authentic user behavior but produced inconsistent robot-side decisions, motivating an explicit decision scheme. From 40 episodes, we derived a hierarchical taxonomy of six response modes (ANSWER, REPORT_DONE, REFUSE, CONFIRM, CLARIFY, ACT) and four ambiguity types (intent, referential, spatial, intelligibility). Two human annotators and an AI annotator applied the scheme to the pilot data. Clean-label rates were 91% and 89%, and Cohen's ranged from 0.72 to 0.95 across decision-point, mode, and ambiguity levels for both human-human and human-AI comparisons. Fine-tuning LLaVA-1.6-7B on taxonomy-derived labels for ACT and CLARIFY indicates the feasibility of training vision-language models using annotations from our taxonomy. Remaining boundary cases in decision-point identification and REPORT_DONE motivate a constrained protocol for more consistent dialogue collection.

</details>

---

### [[20_Research/Papers/机器人/Enhancing_the_Perception_of_Safety_and_Comfort_during_Physical_Human-Robot_Handshake_Interactions_by_Integrating_Flexible_Elements_into_a_Ro|Enhancing the Perception of Safety and Comfort during Physical Human-Robot Handshake Interactions by Integrating Flexible Elements into a Robotic Arm]]

![[assets/2609.19375_first_page.png|800]]

- **arXiv**: [2609.19375](https://arxiv.org/abs/2609.19375)
- **PDF**: https://arxiv.org/pdf/2609.19375
- **详细分析**: [[20_Research/Papers/机器人/Enhancing_the_Perception_of_Safety_and_Comfort_during_Physical_Human-Robot_Handshake_Interactions_by_Integrating_Flexible_Elements_into_a_Ro|Enhancing the Perception of Safety and Comfort during Physical Human-Robot Handshake Interactions by Integrating Flexible Elements into a Robotic Arm]]
- **作者**: Joel Hidalgo, Dennys Paillacho, Melissa Cobos, Luigi Miranda
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《Enhancing the Perception of Safety and Comfort during Physical Human-Robot Handshake Interactions by Integrating Flexible Elements into a Robotic Arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety and comfort in human-robot physical in-teractions are essential aspects in the development of social technologies, where natural gestures, such as handshakes, represent a challenge due to their direct physical contact. The implementation of series elastic actuators (SEA) to absorb impacts is proposed as a design strategy that favors safer interactions. This paper presents an experimental study aimed at evaluating how the incorporation of SEAs in robotic arms influences perceived safety and the interaction experience dur-ing handshaking. The design allows a direct comparison of the effect of rigidity versus the incorporation of elastic elements, in order to identify the advantages of SEAs in improving the physical safety and social acceptance of robotic systems in everyday contexts. The experiment was carried out with 10 volunteers (6 men and 4 women), who performed two interactions with each robotic arm: one with rigid joints and the other with flexible joints using SEA. During testing, objective data on end-effector trajectories were collected, as well as subjective information through a perception survey focused on safety, naturalness, and confidence during the handshake. The survey results show increased perceptions of safety and comfort with the SEA-equipped arm, supporting its potential to facilitate safer and more socially accepted human-robot interactions.

</details>

---

### [[20_Research/Papers/机器人/Design_and_Experimental_Validation_of_a_3D_Printed_Torsional_Series_Elastic_Actuator_for_Safe_Human_Robot_Interaction|Design and Experimental Validation of a 3D Printed Torsional Series Elastic Actuator for Safe Human Robot Interaction]]

![[assets/2609.19367_first_page.png|800]]

- **arXiv**: [2609.19367](https://arxiv.org/abs/2609.19367)
- **PDF**: https://arxiv.org/pdf/2609.19367
- **详细分析**: [[20_Research/Papers/机器人/Design_and_Experimental_Validation_of_a_3D_Printed_Torsional_Series_Elastic_Actuator_for_Safe_Human_Robot_Interaction|Design and Experimental Validation of a 3D Printed Torsional Series Elastic Actuator for Safe Human Robot Interaction]]
- **作者**: Joel Hidalgo Pisco, Melissa Cobos Condo, Luigi Miranda, Dennys Paillacho
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Design and Experimental Validation of a 3D Printed Torsional Series Elastic Actuator for Safe Human Robot Interaction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ensuring intrinsic safety in physical human robot interaction (pHRI) is a critical requirement for social and service robots. While Series Elastic Actuators (SEAs) offer hardware based compliance, traditional metallic designs often require complex, multi part assemblies. This paper presents the design, finite element analysis (FEA), and experimental validation of a low stiffness, torsional spring for SEAs, manufactured via 3D printed thermoplastic polyurethane (TPU). The compliant element exhibits a highly linear torque deformation response (Ks = 0.066 Nm/degree), matching numerical predictions with under 3% deviation, a variance attributed to FDM structural anisotropy. To accommodate external interactions using standard position limited servomotors, a hybrid position controller with torque threshold switching was implemented. Experimental evaluations demonstrate the system ability to accurately track non stationary trajectories and safely yield to external disturbances. Furthermore, the inherent material damping of the TPU acts as a passive low pass filter, preventing high frequency oscillations during control mode transitions. The proposed architecture offers a cost effective, reliable, and easily manufacturable solution for safe pHRI.

</details>

---

### [[20_Research/Papers/具身智能/ViLoMan_Learning_Visual-Proprioceptive_Whole-Body_Loco-Manipulation_Skills_for_Humanoid_Robots|ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots]]

![[assets/2609.19340_figure.png|800]]

- **arXiv**: [2609.19340](https://arxiv.org/abs/2609.19340)
- **PDF**: https://arxiv.org/pdf/2609.19340
- **详细分析**: [[20_Research/Papers/具身智能/ViLoMan_Learning_Visual-Proprioceptive_Whole-Body_Loco-Manipulation_Skills_for_Humanoid_Robots|ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots]]
- **作者**: Zejie Tian, Ruibing Hou, Bingpeng Ma, Börje F. Karlsson, Shiguang Shan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ViLoMan: Learning Visual-Proprioceptive Whole-Body Loco-Manipulation Skills for Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DoorGym, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation requires adaptive whole-body coordination to seamlessly integrate locomotion and physical interaction. Despite recent advances, learning autonomous loco-manipulation remains challenging due to the scarcity of diverse, physically executable robot-object interaction data and the difficulty of learning unified whole-body control directly from onboard observations. We present ViLoMan, a scalable framework for autonomous humanoid loco-manipulation. ViLoMan first transforms partial kinematic demonstrations of human-object interactions into complete, physically executable robot trajectories. It then leverages these trajectories within a teacher-student distillation framework to learn a unified policy that maps egocentric depth observations and proprioceptive measurements directly to joint-level whole-body actions. During deployment, the policy requires neither reference motions nor intermediate commands. We evaluate ViLoMan on door-closing tasks across diverse door configurations and robot initial conditions in both simulation and the real world. Experimental results demonstrate that a single policy enables a Unitree G1 humanoid to complete the full task using only onboard depth sensing and proprioception, while generalizing robustly across task variations and transferring effectively from simulation to reality. Project page: this http URL .

</details>

---

### [[20_Research/Papers/机器人/A_Morphing_Aerial_Robot_With_Thruster-Integrated_Flexible_Continuum_Links_for_Shape_Adaptive_Aerial_Manipulation|A Morphing Aerial Robot With Thruster-Integrated Flexible Continuum Links for Shape Adaptive Aerial Manipulation]]

![[assets/2609.19328_figure.png|800]]

- **arXiv**: [2609.19328](https://arxiv.org/abs/2609.19328)
- **PDF**: https://arxiv.org/pdf/2609.19328
- **详细分析**: [[20_Research/Papers/机器人/A_Morphing_Aerial_Robot_With_Thruster-Integrated_Flexible_Continuum_Links_for_Shape_Adaptive_Aerial_Manipulation|A Morphing Aerial Robot With Thruster-Integrated Flexible Continuum Links for Shape Adaptive Aerial Manipulation]]
- **作者**: Eri Sawada, Kazuki Sugihara, Ayano Miyamichi, Kunio Kojima, Kei Okada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Morphing Aerial Robot With Thruster-Integrated Flexible Continuum Links for Shape Adaptive Aerial Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, aerial manipulation has attracted increasing attention as a key to expand the application of aerial robots. In this work, we focus on two major research directions for achieving versatile aerial manipulation: (i) acquiring high environmental adaptability using soft manipulators, and (ii) expanding the feasible wrench space by distributing thrusters along the manipulator. However, no aerial robot has simultaneously satisfied these two requirements. Therefore, in this paper, we propose a morphing rotor-distributed aerial robot with flexible continuum links that achieves both high shape adaptability and an expanded wrench space. The flexible continuum links function as soft manipulators, passively conforming to the shape of the environment, while the thrusters distributed along the continuum links expand the feasible thrust wrench space and enable the end-effector to exert large interaction forces. To realize the proposed robot, it is essential to suppress vibrations of the lightweight continuum links. Thus, we develop a composite leaf-spring structure that provides both high torsional and vertical stiffness, and vibration-suppressing control methods. Using these implementations, we demonstrate stable flight and a variety of aerial manipulation tasks. To the best of our knowledge, this is the first work to realize aerial manipulations using flexible links with an integrated thruster.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Safe_Humanoid_Navigation_from_Reduced_Order_Models|Learning Safe Humanoid Navigation from Reduced Order Models]]

![[assets/2609.19272_figure.png|800]]

- **arXiv**: [2609.19272](https://arxiv.org/abs/2609.19272)
- **PDF**: https://arxiv.org/pdf/2609.19272
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Safe_Humanoid_Navigation_from_Reduced_Order_Models|Learning Safe Humanoid Navigation from Reduced Order Models]]
- **作者**: William D. Compton, Zachary Olkin, Ryan Bena, Aaron D. Ames
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Safe Humanoid Navigation from Reduced Order Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NavRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Research in humanoid robotics has achieved rapid progress in locomotion, and recent results have pushed the boundary on autonomous navigation. We demonstrate that a standard single-stage RL navigation pipeline struggles to scale to multi-level and multi-story terrain, limited by the difficulty of complex humanoid terrain interactions such as stairs. To overcome this challenge, we decompose the navigation problem into two pieces. First, we train a policy operating on the reduced order dynamics but with full 3D LiDAR observations to navigate complex, multi-story terrain. We then utilize this navigation knowledge to kickstart a policy operating on the full-order humanoid dynamics, with a frozen locomotion policy in the loop. Additionally, we demonstrate that applying a Poisson safety filter to the navigation policy output recovers safety in the presence of out-of-distribution obstacles, without dropping navigation success rate. We demonstrate the resulting RoM-Nav policy on a Unitree G1, accomplishing mapless multi-floor navigation covering trials with over 10m of vertical displacement and over 100m of path length. Project page with videos this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Grasping_by_interconnection_robust_closing_motions_from_coarse_object_templates|Grasping by interconnection: robust closing motions from coarse object templates]]

![[assets/2609.19228_figure.png|800]]

- **arXiv**: [2609.19228](https://arxiv.org/abs/2609.19228)
- **PDF**: https://arxiv.org/pdf/2609.19228
- **详细分析**: [[20_Research/Papers/具身智能/Grasping_by_interconnection_robust_closing_motions_from_coarse_object_templates|Grasping by interconnection: robust closing motions from coarse object templates]]
- **作者**: Julien Vanderheyden, Guillaume Drion, Fulvio Forni, Pierre Sacré
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Grasping by interconnection: robust closing motions from coarse object templates》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous robot hands must often grasp objects whose shape, size, and pose are known only approximately. Grasp planners typically require accurate object models or correct errors with feedback, but how much inaccuracy a closing motion can tolerate on its own remains unclear. To address this question, we designed a motion planner based on four principles: a coarse template of the object, human grasp types, an object-centric interaction, and compliant, sliding contacts instead of prescribed contact points. This paper presents the planner, implemented through virtual model control, and its evaluation on a Shadow Dexterous Hand. Without feedback, the planned closing motions tolerated size errors of about 1cm and pose errors of several centimeters and tens of degrees, a wider range than a state-of-the-art data-driven planner in 25 of 27 tested conditions. They also grasped 82.5% of 80 everyday objects and succeeded within an autonomous pipeline. Robustness can thus be designed into the closing motion itself, rather than left only to feedback. This planner opens a path toward reliable manipulation in uncertain settings, which we will pursue by combining it with adaptive feedback control on the physical hand.

</details>

---

### [[20_Research/Papers/强化学习/ULOHA_An_Underwater_Bimanual_Robot_System_for_Robot_Learning|ULOHA: An Underwater Bimanual Robot System for Robot Learning]]

![[assets/2609.19200_figure.png|800]]

- **arXiv**: [2609.19200](https://arxiv.org/abs/2609.19200)
- **PDF**: https://arxiv.org/pdf/2609.19200
- **详细分析**: [[20_Research/Papers/强化学习/ULOHA_An_Underwater_Bimanual_Robot_System_for_Robot_Learning|ULOHA: An Underwater Bimanual Robot System for Robot Learning]]
- **作者**: Masato Kobayashi, Takeru Tsunoori
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《ULOHA: An Underwater Bimanual Robot System for Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SmolVLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underwater visuomotor policy learning has focused primarily on single manipulators, while bimanual imitation learning has been studied largely in air. We present ULOHA, an underwater bimanual robot learning platform that combines custom-designed leader--follower hardware with software extensions to LeRobot, integrating teleoperation, multi-view sensing, demonstration collection, policy training, and autonomous deployment. Real-robot experiments demonstrate a range of coordinated underwater bimanual behaviors, including inter-arm transfer, shared-object manipulation, and buoyancy-driven interception. We evaluate ACT, Diffusion Policy, and the vision--language--action model SmolVLA on the platform. We investigate how learning methods and execution strategies developed for manipulation in air perform underwater, examining bubble disturbances, buoyancy-driven object motion, action-execution horizons, and real-time chunking. A separate single-arm study examines policy transfer between air and water and shows that demonstrations spanning both media support execution in both under the tested conditions. ULOHA provides a unified experimental platform for studying underwater bimanual robot learning under the coupled perceptual and physical effects of underwater environments. Additional material: this https URL

</details>

---

### [[20_Research/Papers/机器人/DITTO_Dexterous_Interface_for_Transparent_TeleOperation|DITTO: Dexterous Interface for Transparent TeleOperation]]

![[assets/2609.19196_figure.png|800]]

- **arXiv**: [2609.19196](https://arxiv.org/abs/2609.19196)
- **PDF**: https://arxiv.org/pdf/2609.19196
- **详细分析**: [[20_Research/Papers/机器人/DITTO_Dexterous_Interface_for_Transparent_TeleOperation|DITTO: Dexterous Interface for Transparent TeleOperation]]
- **作者**: Joaquin Palacios, Katelyn Lee, Cheng Zhang, Zhanpeng He, Matei Ciocarlie
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《DITTO: Dexterous Interface for Transparent TeleOperation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting data for manipulation with high-DOF hands is challenging, as interfaces must capture rich hand motion while rendering the contact interactions essential for precise manipulation. Existing data collection approaches face a trade-off: teleoperation ensures deployment consistency but lacks force feedback, while handheld (in-the-wild) systems provide natural force transparency but introduce a visual embodiment gap at deployment. We present DITTO, a Dexterous Interface for Transparent TeleOperation, which resolves this through the anatomically informed co-design of a dexterous 7-DOF robotic hand and a kinematically equivalent motorized exoskeleton. A 1-to-1 actuator mapping between the exoskeleton and robotic hand enables handheld (in-the-wild) data collection and bilateral teleoperation with joint-level force feedback unified in a single platform. We demonstrate that the DITTO exoskeleton spans the operator's natural index-to-thumb workspace, and showcase DITTO's dexterous capabilities via learned policies on contact-rich tasks.

</details>

---

### [[20_Research/Papers/机器人/AthenaZero_A_low-inertia,_bimanual_robot_for_dynamic_manipulation|AthenaZero: A low-inertia, bimanual robot for dynamic manipulation]]

![[assets/2609.19194_figure.png|800]]

- **arXiv**: [2609.19194](https://arxiv.org/abs/2609.19194)
- **PDF**: https://arxiv.org/pdf/2609.19194
- **详细分析**: [[20_Research/Papers/机器人/AthenaZero_A_low-inertia,_bimanual_robot_for_dynamic_manipulation|AthenaZero: A low-inertia, bimanual robot for dynamic manipulation]]
- **作者**: Andrew S. Morgan, Gregory Xie, Capprin Bass, Rachel Thomasson, Chunpeng Wang, Erfan Shahriari, Harrison Busa, Oluwaseun Araromi, Joseph Aronov, Michael Burgess, Velin D. Dimitrov, Matthew A. Estrada...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《AthenaZero: A low-inertia, bimanual robot for dynamic manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AthenaZero is a bimanual manipulator designed to minimize inertia without compromising control authority. By utilizing quasi-direct drive actuation and transmission remotization techniques, the system achieves an effective endpoint mass comparable to that of a human---about an order of magnitude less than conventional robot manipulators. This characteristic, combined with its inherent torque transparency, makes AthenaZero exceptionally well-suited for dynamic manipulation. We describe the methodology} that led to this design and demonstrate the robot's capabilities on three baseball-inspired tasks: throwing, catching, and batting, which showcase complex interactions on human-comparable timescales where milliseconds matter. AthenaZero was capable of throwing at speeds in excess of 30 m/s, with catching and batting at speeds in excess of 14 m/s over a short 7.3 m distance. Batting practice and a game of catch were subsequently performed in robot-to-robot and human-to-robot variations, showcasing the efficacy and adaptability of our system in tasks that require high acceleration.

</details>

---
