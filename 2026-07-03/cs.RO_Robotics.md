# cs.RO | Robotics | 2026-07-03

#arxiv #ComputerScience

**论文数**: 20

### [[20_Research/Papers/机器人/QuadRocket_An_Aerial_Robotic_Testbed_for_Adaptive_Thrust-Vector_Control_of_Rocket-Like_Vehicles|QuadRocket: An Aerial Robotic Testbed for Adaptive Thrust-Vector Control of Rocket-Like Vehicles]]

![[assets/2607.02474_figure.png|800]]

- **arXiv**: [2607.02474](https://arxiv.org/abs/2607.02474)
- **PDF**: https://arxiv.org/pdf/2607.02474
- **详细分析**: [[20_Research/Papers/机器人/QuadRocket_An_Aerial_Robotic_Testbed_for_Adaptive_Thrust-Vector_Control_of_Rocket-Like_Vehicles|QuadRocket: An Aerial Robotic Testbed for Adaptive Thrust-Vector Control of Rocket-Like Vehicles]]
- **作者**: Pedro Santos, Joel Reis, Paulo Oliveira, Carlos Silvestre
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《QuadRocket: An Aerial Robotic Testbed for Adaptive Thrust-Vector Control of Rocket-Like Vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents QuadRocket, a quadrotor-based rocket prototype that provides a low-cost, low-risk platform for validating advanced thrust-vector control strategies for launch vehicle-type systems. The prototype consists of a cylindrical main body mounted on top of a quadrotor through a universal joint, forming a flying inverted pendulum with non-negligible inertia. For control design, the coupled system is modeled as a single axisymmetric rigid body actuated by a vectored force applied along its longitudinal axis. A reduced-attitude representation on the two sphere is adopted to explicitly exploit the vehicle's axial symmetry and to decouple yaw from the thrust-vector direction. On this model, we derive an adaptive backstepping controller that achieves almost global trajectory tracking in the presence of unknown constant disturbances, while a control-point transformation mitigates non minimum-phase behavior. The quadrotor is then treated as a thrust vector actuator, and a dynamic-surface-based attitude controller is designed to track the desired thrust-vector, accounting for actuation dynamics and avoiding explicit differentiation of virtual control signals. The complete architecture is evaluated in simulation and validated experimentally in an indoor motion-capture arena. Results demonstrate accurate trajectory tracking, effective disturbance compensation, and confirm the suitability of the QuadRocket as a versatile testbed for thrust-vector-controlled robotic vehicles.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Agile_Intruder_Interception_using_Differentiable_Quadrotor_Dynamics|Learning Agile Intruder Interception using Differentiable Quadrotor Dynamics]]

![[assets/2607.02472_figure.png|800]]

- **arXiv**: [2607.02472](https://arxiv.org/abs/2607.02472)
- **PDF**: https://arxiv.org/pdf/2607.02472
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Agile_Intruder_Interception_using_Differentiable_Quadrotor_Dynamics|Learning Agile Intruder Interception using Differentiable Quadrotor Dynamics]]
- **作者**: Michael Anoruo, Xiaoyu Tian, Abhishek Rathod, Timothy Naudet, Thomas Canchola, Eric Sturzinger, Kshitij Goel, Wennie Tabib
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.6（加权：强化学习 0.6）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Learning Agile Intruder Interception using Differentiable Quadrotor Dynamics》归入 强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a methodology for learning a control policy to intercept an intruder using the 3D direction unit vector to the intruder and the interceptor state. Prior deep reinforcement learning approaches assume either relative position or distance to the intruder is available, but this information is not readily accessible in real-world applications that employ passive, monocular camera sensors. Instead, we propose a solution that leverages an analytical policy gradient method using differentiable quadrotor dynamics to learn agile interception at speeds up to 10 m/s. The proposed approach outperforms baseline methods that utilize simplified point mass dynamics by an average of 30%.

</details>

---

### [[20_Research/Papers/具身智能/HEFT_Heavy-Payload_Full-size_Humanoid_Teleoperation_with_Privileged_Motion_Guidance_and_Windowed_Payload_Curriculum|HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum]]

![[assets/2607.02332_figure.png|800]]

- **arXiv**: [2607.02332](https://arxiv.org/abs/2607.02332)
- **PDF**: https://arxiv.org/pdf/2607.02332
- **详细分析**: [[20_Research/Papers/具身智能/HEFT_Heavy-Payload_Full-size_Humanoid_Teleoperation_with_Privileged_Motion_Guidance_and_Windowed_Payload_Curriculum|HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum]]
- **作者**: Chenxin Liu, Qingzhou Lu, Guangxiao Yang, Xuanyang Shi, Chenghan Yang, Yanjiang Guo, Jianyu Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《HEFT: Heavy-Payload Full-size Humanoid Teleoperation with Privileged Motion Guidance and Windowed Payload Curriculum》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General motion tracking and teleoperation offer a promising path to scalable humanoid skill acquisition, yet most existing frameworks are validated on compact platforms or without real payload interaction, leaving full-size humanoids with real payloads largely unexplored. Scaling to full-size humanoids introduces two compounding challenges: their larger inertia and tighter balance margins make tracking highly sensitive to noise, drift, and retargeting errors from commodity VR trackers, while their payload potential remains largely underutilized. We present HEFT, a heavy-payload full-size humanoid teleoperation framework that addresses both challenges. HEFT learns from deployable noisy VR references with physically plausible reconstructed references through Privileged Motion Guidance (PMG), and uses a Windowed Payload Curriculum (WPC) with expert-guided payload caps to acquire robust heavy-payload tracking. We deploy HEFT on L7, a 175cm, 65kg humanoid. The robot tracks motions including turns, forward/backward locomotion, and squats under payloads up to 24kg.

</details>

---

### [[20_Research/Papers/机器人/NEUROSYMLAND_Neuro-Symbolic_Landing-Site_Assessment_for_Robust_and_Edge-Deployable_UAV_Autonomy|NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy]]

![[assets/2607.02277_figure.jpg|800]]

- **arXiv**: [2607.02277](https://arxiv.org/abs/2607.02277)
- **PDF**: https://arxiv.org/pdf/2607.02277
- **详细分析**: [[20_Research/Papers/机器人/NEUROSYMLAND_Neuro-Symbolic_Landing-Site_Assessment_for_Robust_and_Edge-Deployable_UAV_Autonomy|NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy]]
- **作者**: Weixian Qian, Tianyi Yang, Sebastian Schroder, Yao Deng, Jiaohong Yao, Xiao Cheng, Richard Han, Xi Zheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《NEUROSYMLAND: Neuro-Symbolic Landing-Site Assessment for Robust and Edge-Deployable UAV Autonomy》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe landing-site assessment in unstructured environments remains a key challenge for autonomous UAV deployment, as vision-only learning approaches often degrade under terrain variability and provide limited transparency in safety decisions. We present NEUROSYMLAND, a neuro-symbolic landing-site assessment system that integrates lightweight perception with explicit safety reasoning. The framework constructs a probabilistic semantic scene graph from onboard visual input and evaluates candidate landing regions using symbolic constraints capturing terrain flatness, obstacle clearance, and spatial consistency, enabling structured reasoning under perceptual uncertainty while maintaining edge-feasible execution. Across 72 simulated landing scenarios spanning diverse terrains, NEUROSYMLAND achieves 61 successful assessments, outperforming four competitive baselines (37-57 successes). To evaluate deployability, we further conduct 100 hardware-in-the-loop trials with randomized initial poses, profiling end-to-end latency, stage-wise execution time, and system-level metrics including CPU/GPU utilization, memory footprint, and power consumption. Results demonstrate improved robustness and interpretability with bounded edge-resource usage. Profiling shows that symbolic reasoning contributes only a small fraction of end-to-end latency, while the main computational cost arises from perception and PSSG construction. These results demonstrate the feasibility of deploying the landing-site assessment stack on edge-constrained UAV hardware, and all source code, datasets, prompts, and symbolic rule refinement examples are released in an open-source repository

</details>

---

### [[20_Research/Papers/强化学习/Actuator_Reality_Shaping_for_Zero-Shot_Sim-to-Real_Robot_Learning|Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning]]

![[assets/2607.02205_figure.png|800]]

- **arXiv**: [2607.02205](https://arxiv.org/abs/2607.02205)
- **PDF**: https://arxiv.org/pdf/2607.02205
- **详细分析**: [[20_Research/Papers/强化学习/Actuator_Reality_Shaping_for_Zero-Shot_Sim-to-Real_Robot_Learning|Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning]]
- **作者**: Satoshi Yamamori, Koji Ishihara, Kentaro Minamikawa, Kiyoharu Ohomori, Taiyo Yazaki, Norikazu Sugimoto, Jun Morimoto
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.5（加权：具身智能 1.8，强化学习 0.2，机器人 1.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Actuator Reality Shaping for Zero-Shot Sim-to-Real Robot Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sim-to-real transfer in robot learning is often limited by discrepancies between the ideal actuator dynamics assumed during policy training and the nonlinear, hardware-dependent behavior of physical motors. While conventional approaches attempt to bridge this gap by increasing simulator fidelity through system identification, domain randomization, or learned actuator models, we introduce an alternative paradigm: actuator reality shaping. Instead of modifying the simulator to match the real world, our method shapes the closed-loop behavior of physical actuators to match the idealized second-order reference dynamics used in simulation. By equipping each joint with a two-degree-of-freedom feedforward--feedback controller, we decouple reference-response shaping from robust stabilization, thereby providing a standardized actuator interface for reinforcement learning policies. As a result, policies trained only with the prescribed reference model can be deployed zero-shot on real hardware without task-level fine-tuning or learned actuator models. We validate the approach on a single-joint high-gear-ratio servo under external loads and a 7-DOF robotic arm reaching task, where actuator reality shaping substantially reduces sim-to-real tracking error and improves zero-shot task performance compared with standard servo-control and representative real-to-sim-to-real baselines. We further demonstrate zero-shot transfer on a wheeled-legged robot driving over a slope and a humanoid robot walking, suggesting that actuator reality shaping can serve as a reusable interface for robot learning across diverse hardware platforms.

</details>

---

### [[20_Research/Papers/具身智能/Bridge-WA_Predicting_Where_and_How_the_World_Changes_for_Robotic_Action|Bridge-WA: Predicting Where and How the World Changes for Robotic Action]]

![[assets/2607.02195_figure.png|800]]

- **arXiv**: [2607.02195](https://arxiv.org/abs/2607.02195)
- **PDF**: https://arxiv.org/pdf/2607.02195
- **详细分析**: [[20_Research/Papers/具身智能/Bridge-WA_Predicting_Where_and_How_the_World_Changes_for_Robotic_Action|Bridge-WA: Predicting Where and How the World Changes for Robotic Action]]
- **作者**: Yongjie Bai, Hanting Wang, Mingtong Dai, Qijun Zhong, Yang Liu, Liang Lin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.9（加权：具身智能 0.6，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Bridge-WA: Predicting Where and How the World Changes for Robotic Action》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, VLABench, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose vision-language-action models benefit from large vision-language priors, but effective manipulation also requires anticipating action-relevant scene changes. Existing world-action models often rely on large generative world models or dense future rollouts, which are expensive and spend capacity on visual details weakly coupled to control. We present Bridge-WA, a lightweight world-action framework that distills a frozen future-change teacher into three compact priors: future tokens for intended outcomes, change maps for intervention support, and motion-flow maps for local transition direction. A WorldBridge conditions the action transformer on these priors through multi-source attention memories and spatial-temporal biases, while the teacher model is removed at inference. Across VLABench, RoboTwin2.0, LIBERO-Plus and real-robot evaluations, Bridge-WA improves task success, progress, and robustness, with particularly clear gains under out-of-distribution visual shifts. By focusing action generation on where and how the scene will change, Bridge-WA suppresses nuisance appearance factors such as background, lighting, and distractors, leading to better generalization without deployment-time dense future-image generation. Code and visualizations are available at: https://hcplab-sysu.github.io/BRIDGE-WA .

</details>

---

### [[20_Research/Papers/机器人/Influence_of_Radial_Basis_Activation_Functions_on_Intelligent_Controller_for_Robotic_Manipulators|Influence of Radial Basis Activation Functions on Intelligent Controller for Robotic Manipulators]]

![[assets/2607.02167_figure.png|800]]

- **arXiv**: [2607.02167](https://arxiv.org/abs/2607.02167)
- **PDF**: https://arxiv.org/pdf/2607.02167
- **详细分析**: [[20_Research/Papers/机器人/Influence_of_Radial_Basis_Activation_Functions_on_Intelligent_Controller_for_Robotic_Manipulators|Influence of Radial Basis Activation Functions on Intelligent Controller for Robotic Manipulators]]
- **作者**: Kimmo Paldanius, Gabriel Da Silva Lima, Wallace Moreira Bessa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Influence of Radial Basis Activation Functions on Intelligent Controller for Robotic Manipulators》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents an intelligent control framework for trajectory tracking of robotic manipulators using radial basis function (RBF) neural networks for online disturbance estimation. The proposed control structure combines model-based nonlinear control with an adaptive neural approximator that compensates for parametric uncertainties, friction, and unmodeled dynamics. A Lyapunov-based adaptation law with projection guarantees boundedness of the closed-loop signals and convergence of the tracking error to a compact region. The primary objective of this work is to investigate how the choice of activation function within the RBF network influences transient behavior, steady-state accuracy, and control smoothness. The controller is implemented on a robotic manipulator. Experimental results demonstrate that although stability is preserved for all kernels, activation function selection significantly affects adaptation dynamics and practical tracking performance. These findings demonstrate that activation function selection acts as a structural design parameter in intelligent control, directly shaping adaptation dynamics and practical closed-loop performance.

</details>

---

### [[20_Research/Papers/具身智能/SPLC_Social_Preference_Learning_for_Crowd_Robot_Navigation|SPLC: Social Preference Learning for Crowd Robot Navigation]]

![[assets/2607.01925_figure.png|800]]

- **arXiv**: [2607.01925](https://arxiv.org/abs/2607.01925)
- **PDF**: https://arxiv.org/pdf/2607.01925
- **详细分析**: [[20_Research/Papers/具身智能/SPLC_Social_Preference_Learning_for_Crowd_Robot_Navigation|SPLC: Social Preference Learning for Crowd Robot Navigation]]
- **作者**: Zixuan Chen, Hao Fu, Haiwen Hu, Shiquan Zheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.4，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《SPLC: Social Preference Learning for Crowd Robot Navigation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offline reinforcement learning (RL) holds significant potential for crowd robot navigation in human-robot coexistence applications. However, the inherent complexity of pedestrian motion renders the design of effective reward functions for promoting socially compliant robot behaviors a persistent challenge. This paper proposes a Social Preference Learning for Crowd Robot Navigation (SPLC) algorithm to eliminate the need for detailed reward design. Its core innovation lies in the introduction of a social preference feedback mechanism to automatically generate preference data through principled preference evaluation criteria. By explicitly accounting for the intricacies of pedestrian dynamics, the pipeline mitigates the reward bias and facilitates the systematic quantification of broad social norms, thereby fostering socially compliant behaviors. Extensive experiments integrating SPLC with offline RL methods demonstrate consistent improvements over state-of-the-art baselines across standard performance metrics. Furthermore, real-world experiments on the TurtleBot4 further validate the effectiveness of SPLC in practical human-robot coexistence settings. Our code and video demos are available at https://github.com/sklus949/SPLC.

</details>

---

### [[20_Research/Papers/具身智能/VLA-Corrector_Lightweight_Detect-and-Correct_Inference_for_Adaptive_Action_Horizon|VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon]]

![[assets/2607.01804_figure.png|800]]

- **arXiv**: [2607.01804](https://arxiv.org/abs/2607.01804)
- **PDF**: https://arxiv.org/pdf/2607.01804
- **详细分析**: [[20_Research/Papers/具身智能/VLA-Corrector_Lightweight_Detect-and-Correct_Inference_for_Adaptive_Action_Horizon|VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon]]
- **作者**: Yi Pan, Miao Pan, Qi Lu, Jiaming Huang, Man Zhang, Siteng Huang, Xin Li, Jie Zhang, Yongliang Shen, Xuhong Zhang, Wenqi Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 2.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《VLA-Corrector: Lightweight Detect-and-Correct Inference for Adaptive Action Horizon》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CosSim, Real-World, SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) foundation models have recently achieved strong progress in embodied intelligence. To reduce policy-call frequency while preserving temporal coherence, most generative policies adopt an action chunk mechanism, executing multiple future actions in an open-loop manner under a fixed action horizon. However, this "predict-then-blindly-execute" paradigm sacrifices closed-loop reactivity: in contact-rich physical interactions, even small local perturbations can rapidly amplify within the open-loop blind spot, leading to compounding errors and ultimately task failure. To address this limitation, we propose VLA-Corrector, a lightweight corrective inference framework for action-chunked VLA policies. Without modifying the backbone policy weights, VLA-Corrector introduces a lightweight Latent-space Vision Monitor (LVM) that continuously compares predicted and actual visual feature evolution, enabling online detection of visual dynamics deviations. Once persistent deviation is detected, the system triggers a truncation event, discards the remaining stale actions, and invokes corrective replanning via Online Gradient Guidance (OGG). The detect-and-correct mechanism of VLA-Corrector naturally induces an event-triggered adaptive action horizon: it preserves long-horizon execution when the current chunk remains reliable, and invokes short-horizon corrective replanning when execution begins to drift. In doing so, VLA-Corrector mitigates the trade-off imposed by static horizons between execution robustness and policy-call frequency. It can be integrated into different VLA models without further retraining the VLA backbone, interrupting compounding errors while preserving much of the efficiency benefit of action chunking and substantially improving robustness in long-horizon, contact-rich robotic manipulation tasks.

</details>

---

### [[20_Research/Papers/具身智能/CoRe_Combined_Rewards_with_Vision-Language_Model_Feedback_for_Preference-Aligned_Reinforcement_Learning|CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning]]

![[assets/2607.01721_figure.png|800]]

- **arXiv**: [2607.01721](https://arxiv.org/abs/2607.01721)
- **PDF**: https://arxiv.org/pdf/2607.01721
- **详细分析**: [[20_Research/Papers/具身智能/CoRe_Combined_Rewards_with_Vision-Language_Model_Feedback_for_Preference-Aligned_Reinforcement_Learning|CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning]]
- **作者**: Hexian Ni, Tao Lu, Yinghao Cai
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 0.6，大模型 0.6，强化学习 0.8，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《CoRe: Combined Rewards with Vision-Language Model Feedback for Preference-Aligned Reinforcement Learning》归入 强化学习、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-Reward-Net, MetaWorld, PbRL, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward design remains a central challenge in reinforcement learning (RL). Hand-crafted rewards are often difficult to specify and may lead to suboptimal policies, while learned rewards from preferences can suffer from inefficiency and unstable training. Inspired by the dual nature of human learning explored in cognitive science, we decompose rewards into two complementary components: Formal Rewards (FR), explicitly designed based on task knowledge, and Residual Rewards (RR), learned from observations to capture implicit and nuanced preferences. Based on this decomposition, we propose CoRe, a hybrid framework that integrates FR and RR with vision-language models (VLMs) feedback to achieve preference-aligned policies without human involvement. Our contributions are twofold: (1) We propose a Formal Reward Module (FRM) that leverages VLMs to iteratively design and optimize FR based on task knowledge and preference feedback, enabling the continual improvement of policy during training; (2) We introduce a Residual Reward Module (RRM) that learns RR from video-level preference by employing VLMs to generate preference labels and capturing nuanced rewards that complement FR, ensuring alignment with human intent. Through the synergy of FRM and RRM, CoRe enables the automatic construction of reliable rewards that are efficient and preference-aligned. Extensive experiments demonstrate that CoRe outperforms existing approaches in terms of policy learning effectiveness and efficiency on ten robotic manipulation tasks in simulation and five real-worlds. Videos can be found on our project website: https://core-2026.github.io/

</details>

---

### [[20_Research/Papers/具身智能/Imagining_the_Sense_of_Touch_Touch-Informed_Manipulation_via_Imagined_Tactile_Representations|Imagining the Sense of Touch: Touch-Informed Manipulation via Imagined Tactile Representations]]

![[assets/2607.01684_figure.png|800]]

- **arXiv**: [2607.01684](https://arxiv.org/abs/2607.01684)
- **PDF**: https://arxiv.org/pdf/2607.01684
- **详细分析**: [[20_Research/Papers/具身智能/Imagining_the_Sense_of_Touch_Touch-Informed_Manipulation_via_Imagined_Tactile_Representations|Imagining the Sense of Touch: Touch-Informed Manipulation via Imagined Tactile Representations]]
- **作者**: Zhiyuan Zhang, Adeesh Desai, Jyun-Chi Hu, Yosuke Saka, Quan Khanh Luu, Jiuzhou Lei, Davood Soleymanzadeh, Bihao Zhang, Minghui Zheng, Yu She
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Imagining the Sense of Touch: Touch-Informed Manipulation via Imagined Tactile Representations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ContactWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing can substantially improve contact-rich robotic manipulation, yet its practical deployment remains limited by the fragility, calibration requirements, and maintenance burden of tactile hardware. This raises a fundamental question: can robots benefit from tactile knowledge without requiring tactile sensors at deployment? We present TacImag, a tactile imagination framework that predicts tactile observations from vision and proprioception and uses the generated signals to guide manipulation policies. Trained from paired visuotactile demonstrations, TacImag enables touch-informed manipulation using only visual observations at test time. We evaluate TacImag on six simulated and four real-world manipulation tasks. Across simulation and real-world experiments, imagined tactile observations consistently improve manipulation performance without requiring tactile hardware. In real-world experiments, imagined force fields improve contact-sensitive tasks by 44.4% on average, whereas imagined tactile images improve texture-sensitive tasks by 23.3%, revealing that the effectiveness of tactile imagination depends strongly on the relationship between tactile representation and task requirements. Our results further suggest that tactile imagination does not simply recover missing tactile measurements. Instead, it acts as a form of contact-aware supervision that transforms subtle visual interaction cues into representations that are easier for manipulation policies to exploit.

</details>

---

### [[20_Research/Papers/强化学习/One_Demonstration_Is_Enough_for_Real-World_Robotic_Reinforcement_Learning|One Demonstration Is Enough for Real-World Robotic Reinforcement Learning]]

![[assets/2607.01651_figure.png|800]]

- **arXiv**: [2607.01651](https://arxiv.org/abs/2607.01651)
- **PDF**: https://arxiv.org/pdf/2607.01651
- **详细分析**: [[20_Research/Papers/强化学习/One_Demonstration_Is_Enough_for_Real-World_Robotic_Reinforcement_Learning|One Demonstration Is Enough for Real-World Robotic Reinforcement Learning]]
- **作者**: Yuwan Liu, Hongze Yu, Song Liu, Yuhan Wang, Junge Zhang, Yaodong Yang, Yuanpei Chen, Ceyao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《One Demonstration Is Enough for Real-World Robotic Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AutoSERL, HIL-SERL, Real-World, SERL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning effective robot control policies on physical hardware is challenging due to costly data collection and the difficulty of reward specification. Prior work has incorporated demonstrations into reinforcement learning (RL), yet existing approaches either require large numbers of demonstrations or depend on continuous human intervention during training. To address these limitations, we present AutoSERL, a framework that leverages a single demonstration to fully automate the intervention process in real-world robot RL. The framework includes three complementary mechanisms to accomplish certain tasks: a sliding window intervention mechanism that continuously guides exploration to prevent local optima and unsafe deviations, a safety recovery mechanism that detects and corrects failure states via predefined trajectory recovery points, and an intervention termination criterion that automatically disables guidance once the policy can independently complete the task, preserving its exploration advantage. We evaluate AutoSERL on six contact-intensive manipulation tasks across two robot platforms, spanning insertion, hanging, and hinge-based tasks. AutoSERL consistently outperforms SERL initialized with 20 demonstrations, behavior cloning, and MILES -- a dedicated one-shot imitation learning baseline -- across all tasks while matching HIL-SERL, achieves 100% success rate on insertion tasks, and demonstrates improved robustness to positional variations, all from a single demonstration. Code and videos are available on our project website: https://autoserl.github.io/.

</details>

---

### [[20_Research/Papers/机器人/Path_planning_for_unmanned_naval_surface_vehicles|Path planning for unmanned naval surface vehicles]]

![[assets/2607.01631_first_page.png|800]]

- **arXiv**: [2607.01631](https://arxiv.org/abs/2607.01631)
- **PDF**: https://arxiv.org/pdf/2607.01631
- **详细分析**: [[20_Research/Papers/机器人/Path_planning_for_unmanned_naval_surface_vehicles|Path planning for unmanned naval surface vehicles]]
- **作者**: Daniel G. Schwartz
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Path planning for unmanned naval surface vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

There nowadays is a myriad of approaches to real-time avoidance of fixed obstacles for unmanned surface vehicles (USVs) and, to a lesser extent, also the task of avoiding moving obstacles such as boats, ships, swimmers, and other USVs, but both topics still present challenges. This paper offers novel approaches to both of these problems. It uses a combination of a global path planner, which finds a path from a start point to a goal point that avoids fixed obstacles (given that their locations are known in advance), and a local path planner, which can circumnavigate a moving obstacle (as well as any previously unknown fixed obstacles). The global planner is novel in that it employs a combination of three path planners, one known in the literature as Grassfire, one that is a new modification of Grassfire, and one that is a new, and arguably more intuitive, version of the well-known Probabilistic Roadmap. The local planner is novel in that it employs a higher-level decision logic based on its observations regarding the direction of movement of the obstacle relative to the USVs global path. This logic enables the USV to determine the best strategy for avoiding the obstacle by systematically routing the vehicle behind the obstacle rather than running parallel to it until the opportunity to pass appears. Simulations are provided that validate these claims. For comparison with other systems, the simulations include an implementation of the well-known D* algorithm, and the discussion covers additional dynamic path planning systems, which, like D*, do not necessarily route the vehicle behind the moving obstacle.

</details>

---

### [[20_Research/Papers/具身智能/Multi-Rate_Nonlinear_Model_Predictive_Control_for_Wall-Supported_Bipedal_Locomotion_of_Quadrupedal_Robots|Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots]]

![[assets/2607.01574_figure.png|800]]

- **arXiv**: [2607.01574](https://arxiv.org/abs/2607.01574)
- **PDF**: https://arxiv.org/pdf/2607.01574
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Rate_Nonlinear_Model_Predictive_Control_for_Wall-Supported_Bipedal_Locomotion_of_Quadrupedal_Robots|Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots]]
- **作者**: Taizoon Chunawala, Jeeseop Kim, Kaveh Akbari Hamed
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.2（加权：具身智能 1.5，世界模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Multi-Rate Nonlinear Model Predictive Control for Wall-Supported Bipedal Locomotion of Quadrupedal Robots》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a novel layered planning and control framework based on multi-rate nonlinear model predictive control (MR-NMPC) that enables quadrupedal robots to perform hybrid bipedal locomotion with wall-assisted support in constrained environments. Real-time trajectory optimization for this locomotion presents significant challenges, as the controller must simultaneously plan for both the contact points and the continuous trajectories of the robot's center of mass (CoM) and orientation within the robot's nonlinear dynamics while accounting for unilateral contact constraints, underactuation, and the switching nature of the robot's dynamics. At the high level of the control framework, an MR-NMPC is proposed, which dynamically plans both the discrete-time trajectories of the contact points and the continuous-time trajectories of the CoM and orientation, using a single rigid body (SRB) dynamics model. By incorporating contact-point planning within the multi-rate optimal control framework, this approach enhances dynamic stability compared to heuristic foot placement strategies. At the low level of the control framework, a nonlinear whole-body controller (WBC) based on virtual constraints and a quadratic program enforces full-order dynamics and tracks the MR-NMPC references. The proposed approach is validated through extensive numerical simulations demonstrating the robust wall-assisted bipedal locomotion of a Unitree A1 quadrupedal robot on rough terrains and under external disturbances in a constrained environment. Comparative analysis shows that the proposed MR-NMPC achieves a 2.9 times higher success rate compared to conventional MPC with heuristic-based foot placement strategies in negotiating irregular terrain at high speeds.

</details>

---

### [[20_Research/Papers/机器人/A_Reconfigurable_Rocker-Bogie_Robot_for_High_Step_Climbing_and_Turning|A Reconfigurable Rocker-Bogie Robot for High Step Climbing and Turning]]

![[assets/2607.01554_figure.png|800]]

- **arXiv**: [2607.01554](https://arxiv.org/abs/2607.01554)
- **PDF**: https://arxiv.org/pdf/2607.01554
- **详细分析**: [[20_Research/Papers/机器人/A_Reconfigurable_Rocker-Bogie_Robot_for_High_Step_Climbing_and_Turning|A Reconfigurable Rocker-Bogie Robot for High Step Climbing and Turning]]
- **作者**: Kento Koizumi, Tomoaki Ohba, Yuta Saito, Takeya Morito, Kenji Suzuki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Reconfigurable Rocker-Bogie Robot for High Step Climbing and Turning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study proposes a reconfigurable rocker-bogie mechanism that achieves efficient turning motion with a small number of actuators while maintaining high step-climbing capability. By installing motors at the bogie joints and actively swinging up and down bogies, the system enables switching between four-wheel and six-wheel configurations. Omnidirectional wheels are mounted on the rear ends of the rockers, allowing smooth turning in the four-wheel configuration based on a differential-drive model. Experimental evaluation using a prototype robot demonstrated that the proposed mechanism achieves zero-radius turning at a speed more than five times that of a conventional rocker-bogie mechanism equipped with six non-steerable grip wheels, while requiring only approximately 17% of the total average wheel torque. In addition, the robot successfully climbed a 40 cm step with an average climbing time of 6.4 s, confirming its high turning and step-climbing performance.

</details>

---

### [[20_Research/Papers/具身智能/SE(2)_Navigation_Mesh|SE(2) Navigation Mesh]]

![[assets/2607.01454_figure.png|800]]

- **arXiv**: [2607.01454](https://arxiv.org/abs/2607.01454)
- **PDF**: https://arxiv.org/pdf/2607.01454
- **详细分析**: [[20_Research/Papers/具身智能/SE(2)_Navigation_Mesh|SE(2) Navigation Mesh]]
- **作者**: Shuyang Shi, Kaixian Qu, Changan Chen, Ines Kast, Yuntao Ma, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SE(2) Navigation Mesh》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Global navigation for ground robots in complex multi-level environments requires representations that accurately capture traversable regions while enabling efficient path planning. Current approaches present key limitations: Point clouds and volumetric occupancy maps lack explicit surface structure for traversability estimation, whereas direct pathfinding on dense triangle meshes is computationally prohibitive. Navigation meshes mitigate these challenges through polygonal abstraction of the underlying mesh, but assume yaw-invariant traversability, rendering them unsuitable for non-circular robots in constrained spaces. We propose SE(2) Navigation Mesh (SE(2) NavMesh), a polygonal representation of traversable regions that encodes yaw-dependent traversability. Our method evaluates traversability using footprint masks and constructs a graph over yaw-specific layers with explicit translational and rotational connectivity. Grounded in this representation, we develop an A*-String Pulling-A* (ASA) pathfinding strategy that hierarchically optimizes robot position and heading. We also present an online method that incrementally updates the SE(2) NavMesh from streaming point clouds during concurrent geometry reconstruction. In simulation, the SE(2) NavMesh captures over 50% more traversable area than classical NavMeshes, and the SE(2) NavMesh + ASA pipeline consistently outperforms sampling-based baselines in constrained environments. Extensive real-world experiments on a physical robot validate real-time online generation and successful navigation across multiple environments.

</details>

---

### [[20_Research/Papers/机器人/CommonRoad-Game_A_Human-in-the-Loop_Simulation_Framework_for_Autonomous_Driving|CommonRoad-Game: A Human-in-the-Loop Simulation Framework for Autonomous Driving]]

![[assets/2607.01382_figure.png|800]]

- **arXiv**: [2607.01382](https://arxiv.org/abs/2607.01382)
- **PDF**: https://arxiv.org/pdf/2607.01382
- **详细分析**: [[20_Research/Papers/机器人/CommonRoad-Game_A_Human-in-the-Loop_Simulation_Framework_for_Autonomous_Driving|CommonRoad-Game: A Human-in-the-Loop Simulation Framework for Autonomous Driving]]
- **作者**: Yunfei Bi, Youran Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《CommonRoad-Game: A Human-in-the-Loop Simulation Framework for Autonomous Driving》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion planning algorithms should be evaluated in human-in-the-loop environments to ensure they produce safe and efficient behaviors during interactions. However, existing simulation platforms often rely on recorded datasets, lack dedicated interfaces for real-time human interaction, or remain weakly integrated with an autonomous driving ecosystem. Moreover, many human-in-the-loop simulators are computationally intensive by design, making them less suitable for rapid prototyping and flexible experimentation in early-stage autonomous driving research. To address these limitations, we present CommonRoad-Game, a lightweight human-in-the-loop simulation framework tightly integrated with the CommonRoad platform, focusing on the systematic testing of motion planners with human participation and the analysis of human driving behaviors in interactive scenarios. We introduce a multi-threaded architecture with a robust synchronization mechanism that aligns simulation time with wall-clock time, enabling deterministic and temporally consistent interaction between autonomous and human-driven vehicles. In addition, the framework provides a scenario generation module that records driving logs, allowing diverse and reproducible test cases to be constructed from human-in-the-loop experiments. Experimental results demonstrate that CommonRoad-Game achieves stable temporal synchronization, supports scalable multi-agent simulation, and seamlessly integrates CommonRoad-compatible motion planners to generate interactive driving scenarios. The source code is publicly available at https://github.com/Yunfei-Bi8/CommonRoad-Game.

</details>

---

### [[20_Research/Papers/具身智能/Neuro-Symbolic_Safety_Guidance_for_Vision-Language-Action_Models_via_Constrained_Flow_Matching|Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching]]

![[assets/2607.01378_figure.png|800]]

- **arXiv**: [2607.01378](https://arxiv.org/abs/2607.01378)
- **PDF**: https://arxiv.org/pdf/2607.01378
- **详细分析**: [[20_Research/Papers/具身智能/Neuro-Symbolic_Safety_Guidance_for_Vision-Language-Action_Models_via_Constrained_Flow_Matching|Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching]]
- **作者**: William English, Hao Zheng, Rickard Ewetz
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Neuro-Symbolic Safety Guidance for Vision-Language-Action Models via Constrained Flow Matching》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SafeLIBERO, SafeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have demonstrated promising generalization capabilities across robotic manipulation tasks, yet their real-world deployment remains limited by the lack of effective safety measures. Specifically, existing safety measures only prevent collisions caused by the robot's next action. In this paper, we propose a neuro-symbolic safety guidance mechanism for flow matching based VLAs that enables predictive collision avoidance. Flow matching based VLAs determine the next actions by predicting a trajectory (a sequence of actions) through an iterative neural flow matching process. Our method formulates safety enforcement as a minimum-norm constrained optimization problem that corrects safety violations during the denoising process of noisy intermediate trajectory predictions. By analyzing predicted trajectories and applying corrections during iterative denoising, our approach anticipates collisions before they become unavoidable. This interleaving of symbolic constraint satisfaction with neural trajectory generation enables predictive collision avoidance rather than reactive intervention. On the SafeLIBERO benchmark, our method achieves 82.8% collision avoidance and 81.6% task success, a 6.3% and 19.8% improvement respectively over single-step methods, with the largest gains on long-horizon tasks where compounding distribution shift is most pronounced. Video demonstrations of our approach are included on our project page at https://willenglish.tech/SafetyGuidedFlowMatching/.

</details>

---

### [[20_Research/Papers/强化学习/Simulation_Based_Reward_Function_Validation_for_Multi-Agent_On_Orbit_Inspection|Simulation Based Reward Function Validation for Multi-Agent On Orbit Inspection]]

![[assets/2607.01367_figure.jpg|800]]

- **arXiv**: [2607.01367](https://arxiv.org/abs/2607.01367)
- **PDF**: https://arxiv.org/pdf/2607.01367
- **详细分析**: [[20_Research/Papers/强化学习/Simulation_Based_Reward_Function_Validation_for_Multi-Agent_On_Orbit_Inspection|Simulation Based Reward Function Validation for Multi-Agent On Orbit Inspection]]
- **作者**: Patrick Quinn, Bala Prenith Reddy Gopu, George M. Nehma, Madhur Tiwari
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《Simulation Based Reward Function Validation for Multi-Agent On Orbit Inspection》归入 大模型、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A proposed method for the control of groups of inspection spacecraft is Multi-Agent Reinforcement Learning (MARL). While MARL has already been employed for this purpose in previous work, the reward functions used focus on reaching a finite set of predetermined inspection points around the target. In this work, we study and develop a generalized reward function for the MARL inspection task informed by the analysis of 3D reconstructions of inspected objects in orbit. Because the reward function is generalized such that any number of images at arbitrary locations may evaluated, we also allow trained agents to have complete control over when images are collected. With this approach, we gather insights into best practices for not only the specific MARL inspection task, but also gain key takeaways informative to the broader inspection task outside of a MARL context.

</details>

---

### [[20_Research/Papers/强化学习/WaveLander_A_Generalizable_Hierarchical_Control_Framework_for_UAV_Landing_on_Wave-Disturbed_Platforms_via_Reinforcement_Learning|WaveLander: A Generalizable Hierarchical Control Framework for UAV Landing on Wave-Disturbed Platforms via Reinforcement Learning]]

![[assets/2607.01281_first_page.png|800]]

- **arXiv**: [2607.01281](https://arxiv.org/abs/2607.01281)
- **PDF**: https://arxiv.org/pdf/2607.01281
- **详细分析**: [[20_Research/Papers/强化学习/WaveLander_A_Generalizable_Hierarchical_Control_Framework_for_UAV_Landing_on_Wave-Disturbed_Platforms_via_Reinforcement_Learning|WaveLander: A Generalizable Hierarchical Control Framework for UAV Landing on Wave-Disturbed Platforms via Reinforcement Learning]]
- **作者**: Chun-Kit Li, Iok Long Sit, Ming Fung Siu, Ka Yu Kui, Hin Wang Lin, Pengyu Wang, Ling Shi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，强化学习 0.8，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《WaveLander: A Generalizable Hierarchical Control Framework for UAV Landing on Wave-Disturbed Platforms via Reinforcement Learning》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous landing of unmanned aerial vehicles (UAVs) on wave-disturbed marine platforms remains challenging due to stochastic platform motion, time-varying platform attitude, and uncertain touchdown conditions. Existing model-based methods often require accurate motion prediction and online optimization, while end-to-end learning approaches may suffer from high training complexity and limited interpretability. This paper presents WaveLander, a hierarchical control framework via reinforcement learning (RL) that decouples vertical landing decision-making from low-level flight stabilization. The RL policy maps a compact platform-relative observation to a scalar vertical velocity reference, while a conventional low-level flight controller maintains attitude stability and lateral tracking. This formulation reduces dynamic platform landing to a low-dimensional, timing-aware control problem and enables smooth landing behavior without explicit switching rules. Simulation results under randomized wave-induced platform motions show that WaveLander achieves robust landing performance and generalizes to unseen disturbance conditions, demonstrating the potential of hierarchical learning-based control for marine UAV recovery.

</details>

---
