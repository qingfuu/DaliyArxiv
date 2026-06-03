# cs.RO | Robotics | 2026-06-01

#arxiv #ComputerScience

**论文数**: 26

### [[20_Research/Papers/具身智能/Learning_Controlled_Separation_of_Small_Objects_Between_Two_Fingers_with_a_Tactile_Skin|Learning Controlled Separation of Small Objects Between Two Fingers with a Tactile Skin]]

![[assets/2605.31486_figure.jpg|800]]

- **arXiv**: [2605.31486](https://arxiv.org/abs/2605.31486)
- **PDF**: https://arxiv.org/pdf/2605.31486
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Controlled_Separation_of_Small_Objects_Between_Two_Fingers_with_a_Tactile_Skin|Learning Controlled Separation of Small Objects Between Two Fingers with a Tactile Skin]]
- **作者**: Ulf Kasolowsky, Berthold Bäuml
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.9，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Controlled Separation of Small Objects Between Two Fingers with a Tactile Skin》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce and solve the novel task of controlled separation of small objects with two fingers of a multi-purpose robotic hand: after grasping into a box of small objects, the task is to drop as many of them until a desired number remains between the fingers. The objects are small compared to the width of the fingers but also in absolute terms. In our case little pellets with a diameter of only 6mm are handled. We show that the task can be performed purely tactile (no vision) using a spatially-resolved tactile skin on a fingertip. The separation policy is trained in simulation via reinforcement learning using a straightforward sparse reward, which basically checks if the desired number of objects is reached. In simulation experiments, we provide an exhaustive analysis of the benefits of using spatially-resolved tactile feedback: while an ideal (high-resolution) tactile sensor allows solving the task almost perfectly, a sensor with lower spatial resolution (here 4x4 taxels) still leads to an improvement of up to 20% compared to using only the fingers' joint sensors. For this analysis, we further train an estimator alongside the policy that predicts the ground truth contact positions. Finally, we demonstrate the successful sim-to-real transfer for the DLR-Hand II equipped with a tactile skin.

</details>

---

### [[20_Research/Papers/强化学习/Batched_Differentiable_Rigid_Body_Dynamics_in_PyTorch_for_GPU-Accelerated_Robot_Learning|Batched Differentiable Rigid Body Dynamics in PyTorch for GPU-Accelerated Robot Learning]]

![[assets/2605.31481_figure.png|800]]

- **arXiv**: [2605.31481](https://arxiv.org/abs/2605.31481)
- **PDF**: https://arxiv.org/pdf/2605.31481
- **详细分析**: [[20_Research/Papers/强化学习/Batched_Differentiable_Rigid_Body_Dynamics_in_PyTorch_for_GPU-Accelerated_Robot_Learning|Batched Differentiable Rigid Body Dynamics in PyTorch for GPU-Accelerated Robot Learning]]
- **作者**: Yue Wang, Yanran Xu, Wenbo Wu, Chuanhang Qiu, Zhaoxing Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Batched Differentiable Rigid Body Dynamics in PyTorch for GPU-Accelerated Robot Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As robot control shifts toward large-scale reinforcement learning with in-loop dynamics computation, the community's reliance on CPU-bound libraries such as Pinocchio creates a throughput bottleneck in GPU-based training pipelines. We present BARD (Batched Articulated Rigid-body Dynamics), a self-contained PyTorch implementation of Featherstone's rigid-body dynamics algorithms, optimized for batched GPU evaluation and automatic differentiation. Three design choices make this efficient: a tiered lazy-evaluation cache that avoids redundant tree traversals, matmul-free joint transforms via pre-computed Rodrigues constants, and level-parallel propagation that reduces sequential operations to tree-depth batched steps. On five robot models (7-23 DOFs), BARD matches Pinocchio numerically while reaching up to 64x higher throughput for Forward Kinematics and 63x for Jacobians at batch size 4096 on an NVIDIA H200. We validate differentiability through gradient-based system identification on a 7-DOF manipulator, recovering link masses to 1.24% mean error under 5% torque noise, and integrate BARD into an Isaac Lab AMP training pipeline for an 11-DOF spined quadruped with 4096 parallel environments, where it is 8.5x faster than Pinocchio and 2.0x faster than ADAM for in-loop dynamics. BARD is open-sourced at: https://github.com/YueWang996/bard-pytorch-dynamics.

</details>

---

### [[20_Research/Papers/具身智能/On-Device_Robotic_Planning_Eliminating_Inference_Redundancy_for_Efficient_Decision-Making|On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making]]

![[assets/2605.31460_figure.png|800]]

- **arXiv**: [2605.31460](https://arxiv.org/abs/2605.31460)
- **PDF**: https://arxiv.org/pdf/2605.31460
- **详细分析**: [[20_Research/Papers/具身智能/On-Device_Robotic_Planning_Eliminating_Inference_Redundancy_for_Efficient_Decision-Making|On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making]]
- **作者**: Joonhee Lee, Hyunseung Shin, Hyunmi Kim, Pei Zhang, Jeonggil Ko
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《On-Device Robotic Planning: Eliminating Inference Redundancy for Efficient Decision-Making》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DP-VLA, DiffusionVLA, OpenVLA, RealWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning-based robotic policies using large language and vision-language models achieve strong semantic planning capabilities but mostly suffer from a high inference latency that limits practical real-time deployment. In this work, we observe that robotic reasoning workloads contain substantial temporal redundancy, where consecutive observations frequently produce identical actions and subgoals. Based on this insight, we present REIS, a human cognition inspired robotic decision-making framework that minimizes unnecessary reasoning while preserving semantic adaptability. REIS combines lightweight scene gating, KV-steered affordance routing, and deliberative reasoning to accelerate robotic control under embodied constraints. Experiments on ALFRED, and real-world robotic tasks demonstrate that REIS significantly suppresses reasoning overhead while maintaining competitive task performance.

</details>

---

### [[20_Research/Papers/机器人/Adaptive_Artificial_Time-Delay_Control_with_Barrier_Lyapunov_Constraints_for_Euler-Lagrange_Robots|Adaptive Artificial Time-Delay Control with Barrier Lyapunov Constraints for Euler-Lagrange Robots]]

![[assets/2605.31405_figure.png|800]]

- **arXiv**: [2605.31405](https://arxiv.org/abs/2605.31405)
- **PDF**: https://arxiv.org/pdf/2605.31405
- **详细分析**: [[20_Research/Papers/机器人/Adaptive_Artificial_Time-Delay_Control_with_Barrier_Lyapunov_Constraints_for_Euler-Lagrange_Robots|Adaptive Artificial Time-Delay Control with Barrier Lyapunov Constraints for Euler-Lagrange Robots]]
- **作者**: Saksham Gupta, Rishabh Dev Yadav, Sarthak Mishra, Amitabh Sharma, Sourish Ganguly, Wei Pan, Spandan Roy, Simone Baldi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Adaptive Artificial Time-Delay Control with Barrier Lyapunov Constraints for Euler-Lagrange Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper addresses the challenge of simultaneously compensating for state-dependent uncertainties and enforcing time-varying state constraints in Euler-Lagrange systems, a common requirement in robotics that remains underserved by existing control designs. A novel adaptive control framework is developed that combines an artificial time-delay-based uncertainty estimation strategy, also known as time-delay estimation, with a barrier Lyapunov function to enforce constraint-aware control design. Specifically, a state-dependent upper bound on the time-delay estimation approximation error is analytically formulated, and an adaptive law is constructed to estimate its parameters online, enabling real-time state-dependent uncertainty compensation without relying on prior model knowledge. To ensure constraint compliance, the barrier Lyapunov function-based controller enforces time-varying bounds on both position and velocity. The resulting architecture is provably stable via Lyapunov analysis. Experimental results on a five-degree-of-freedom robotic manipulator validate the framework's capability, compared with the state of the art, in maintaining strict adherence to safety-critical constraints under dynamic uncertainties.

</details>

---

### [[20_Research/Papers/机器人/Haptic_Sorter_A_Unified_Planning_Framework_for_Online_Shape_Estimation_and_Real-Time_Pose_Inference|Haptic Sorter: A Unified Planning Framework for Online Shape Estimation and Real-Time Pose Inference]]

![[assets/2605.31352_figure.jpg|800]]

- **arXiv**: [2605.31352](https://arxiv.org/abs/2605.31352)
- **PDF**: https://arxiv.org/pdf/2605.31352
- **详细分析**: [[20_Research/Papers/机器人/Haptic_Sorter_A_Unified_Planning_Framework_for_Online_Shape_Estimation_and_Real-Time_Pose_Inference|Haptic Sorter: A Unified Planning Framework for Online Shape Estimation and Real-Time Pose Inference]]
- **作者**: Zhuoyi Lu, Lin Yang, Sri Harsha Turlapati, Domenico Campolo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Haptic Sorter: A Unified Planning Framework for Online Shape Estimation and Real-Time Pose Inference》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotics manipulation usually assumes that the shape and pose of the object are known to the robot prior to motion planning. However, precise geometric information is not always available in practice, and pose inference suffers from sensor uncertainties and view occlusion. In this work, we propose a unified model-based geometric framework integrating robotic haptic perception, modeling, and manipulation planning. Our novelties involve: \textit{i)} Introducing Bayesian Optimization (BO) to guide the haptic exploration for object shape inference, where superellipses are used to approximate geometric boundary; \textit{ii)} Adaptive formulation of manipulation potential encoding object geometry for quasi-static robot-object interaction; \textit{iii)} Proposing an online Ordinary Differential Equation (ODE) for real-time pose inference based on model prediction and tactile feedback. We deploy our system on a 2D robotic sorting task, and vary object geometries to validate the robustness and generalizability of our framework in both simulation and a real-world multi-arm setup.

</details>

---

### [[20_Research/Papers/大模型/Surface_Constraint_Policy_for_Learning_Surface-Constrained_and_Dynamically_Feasible_Robot_Skills|Surface Constraint Policy for Learning Surface-Constrained and Dynamically Feasible Robot Skills]]

![[assets/2605.31321_figure.jpg|800]]

- **arXiv**: [2605.31321](https://arxiv.org/abs/2605.31321)
- **PDF**: https://arxiv.org/pdf/2605.31321
- **详细分析**: [[20_Research/Papers/大模型/Surface_Constraint_Policy_for_Learning_Surface-Constrained_and_Dynamically_Feasible_Robot_Skills|Surface Constraint Policy for Learning Surface-Constrained and Dynamically Feasible Robot Skills]]
- **作者**: Shuai Ke, Jiexin Zhang, Huan Zhao, Zhiao Wei, Yikun Guo, Jie Pan, Han Ding
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Surface Constraint Policy for Learning Surface-Constrained and Dynamically Feasible Robot Skills》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based imitation learning methods have driven rapid progress in robot dexterous manipulation tasks. However, they have limitations when applied to tasks that involve complex free-form surface constraints because of their lack of explicit surface geometry constraint modeling and the dynamic feasibility issue, resulting in stochastic action generation that fails to achieve reliable surface alignment and maintain stable contact. To address these limitations, we propose a novel surface constraint policy (SCP) for generating robot actions that satisfy free-form surface constraints on the basis of human demonstrations and real-time visual observations. First, the surface geometry constraint is encoded using a two-dimensional weighted Gaussian kernel function that is derived from demonstrations. Building on the encoded surface geometry constraints, the diffusion-based policy is used to infer task-level action intentions from multimodal sensory inputs, including visual observations and robot state feedback. These intentions are further transformed into surface-constrained dynamic movement primitives (DMPs) through a similarity-based action mapping method, thereby enabling smooth and compliant motion execution. The SCP achieves generation of structured surface geometric intent and dynamically admissible actions. The proposed method is validated on multiple surface manipulation tasks and compared with existing techniques. The experimental results demonstrate superior task success rates and contact stability under surface constraints.

</details>

---

### [[20_Research/Papers/具身智能/AR_Forcing_Towards_Long-Horizon_Robot_Navigation_World_Model|AR Forcing: Towards Long-Horizon Robot Navigation World Model]]

![[assets/2605.31314_figure.png|800]]

- **arXiv**: [2605.31314](https://arxiv.org/abs/2605.31314)
- **PDF**: https://arxiv.org/pdf/2605.31314
- **详细分析**: [[20_Research/Papers/具身智能/AR_Forcing_Towards_Long-Horizon_Robot_Navigation_World_Model|AR Forcing: Towards Long-Horizon Robot Navigation World Model]]
- **作者**: Yifei Yang, Zehua Fan, Huan Li, Aoqi Wang, Lida Huang, Haibao Yu, Haiyan Liu, Xuanyao Mao, Jason Bao, Liang Xu, Bingchuan Sun, Yan Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.6（加权：具身智能 1.5，世界模型 0.8，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《AR Forcing: Towards Long-Horizon Robot Navigation World Model》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The diffusion based robot navigation world models are typically trained using parallel supervision, while autoregressive inference is employed during path planning. This results in a distribution shift between training and inference, which destabilizes the performance over long-horizon prediction. We propose AR Forcing, an autoregressive training strategy, which integrates the standard diffusion loss into the autoregressive training loop. At each step, the model uses its own predictions to update the context and optimize the single step noise prediction objective, thereby explicitly exposing the model to the inference state distribution during training. Our method does not require additional discriminators or distribution-matching losses, retains the original diffusion framework and sampler, and is easy to integrate. Experiments on multi-domain navigation datasets (RECON, SCAND, HuRoN, TartanDrive) show that compared with strong baselines, AR Forcing improved the consistency of generated images during long-horizon navigation and the accuracy of predicted trajectories, enhancing robustness of the model in complex known and unknown environments. We will release the code soon.

</details>

---

### [[20_Research/Papers/具身智能/Before_Parc_Fermé_RL-Time_Pruning_for_Efficient_Embodied_LLMs_in_Autonomous_Driving|Before Parc Fermé: RL-Time Pruning for Efficient Embodied LLMs in Autonomous Driving]]

![[assets/2605.31256_figure.png|800]]

- **arXiv**: [2605.31256](https://arxiv.org/abs/2605.31256)
- **PDF**: https://arxiv.org/pdf/2605.31256
- **详细分析**: [[20_Research/Papers/具身智能/Before_Parc_Fermé_RL-Time_Pruning_for_Efficient_Embodied_LLMs_in_Autonomous_Driving|Before Parc Fermé: RL-Time Pruning for Efficient Embodied LLMs in Autonomous Driving]]
- **作者**: Luca Benfenati, Ali Azimi, Matteo Risso, Fabio Carapellese, Daniele Jahier Pagliari, Alessio Burrello
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《Before Parc Fermé: RL-Time Pruning for Efficient Embodied LLMs in Autonomous Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BPF-RL, SFT-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Large Language Models (LLMs) are increasingly used as reasoning modules in robotic control pipelines to improve human-robot interaction, but their memory and generation latency make real-time deployment difficult. Pruning can reduce these costs, but for controllers that undergo multiple pre- and post-training phases, the crucial question is not only how much to prune, but when pruning should occur. In this work, we propose Before Parc Fermé (BPF), a pruning strategy performed during RL that compresses embodied LLM controllers while they are still being optimized for closed-loop behavior. This allows pruning decisions to account for the task-specific supervision and closed-loop feedback that shape the final controller. We propose two variants: BPF-RL, which performs iterative pruning during RL by removing part of the model at predefined training intervals, and BPF-SFT/RL, which first prunes part of the model structure during SFT and then further compresses it during RL using the same iterative strategy as BPF-RL until the target pruning ratio is reached. We evaluate BPF on RobotxR1, an LLM-based autonomous-driving control pipeline, using an established LLM pruning framework (LLM-Pruner), and compare it against post-training pruning, post-training pruning with RL recovery, SFT-stage pruning, and smaller dense models from the same family. Our results show that BPF provides the best task-performance vs. memory and throughput trade-off among the considered pruning strategies. When compressing the larger RobotxR1 models, BPF-SFT/RL achieves a $1.69\times$ better size-end-to-end performance trade-off than directly selecting a smaller dense model from the same family, measured as removed parameters per lost percentage point of control adaptability. On the Jetson AGX Orin mounted on the target robotic platform, the compact models improve decode throughput by up to $27\%$.

</details>

---

### [[20_Research/Papers/具身智能/HARP-VLA_Human-Robot_Aligned_Representation_Learning_for_Vision-Language-Action_Model|HARP-VLA: Human-Robot Aligned Representation Learning for Vision-Language-Action Model]]

![[assets/2605.31234_figure.png|800]]

- **arXiv**: [2605.31234](https://arxiv.org/abs/2605.31234)
- **PDF**: https://arxiv.org/pdf/2605.31234
- **详细分析**: [[20_Research/Papers/具身智能/HARP-VLA_Human-Robot_Aligned_Representation_Learning_for_Vision-Language-Action_Model|HARP-VLA: Human-Robot Aligned Representation Learning for Vision-Language-Action Model]]
- **作者**: Xiang Zhu, Puzhen Yuan, Yichen Liu, Jianyu Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《HARP-VLA: Human-Robot Aligned Representation Learning for Vision-Language-Action Model》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HARP-VLA, OpenVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning generalizable vision-language-action (VLA) models from large-scale human videos is promising but challenging due to cross-embodiment discrepancies in both visual observations and executable actions. While latent action models reduce the action execution gap by learning action abstractions, they still rely on visual features. Thus, misaligned human and robot visual representations can lead to inconsistencies in policy inputs and induce domain-dependent latent actions, hindering effective co-training with human videos. To address this, we propose HARP, a human-robot aligned representation learning framework for more effective VLA pretraining from human videos. Specifically, HARP uses limited paired human-robot demonstrations as cross-embodiment bridges and abundant unpaired human and robot videos as a scalable dynamics supervision data source. It trains a robot-adapted visual encoder and a latent action model with manipulation-centric auxiliary cues and a source-relative pair-discriminative alignment loss, which adapts robot representations toward human semantics while preserving pair-level discrimination. The learned aligned vision encoder and latent action model provide a unified vision and action representation for VLA-style policy learning, where human and robot videos provide vision-language-to-latent-action supervision and a lightweight robot action head grounds latent actions into executable commands. Experiments on feature visualization, simulation, and realworld manipulation show improved human-robot alignment and downstream policy performance, achieving 4.481 average length on CALVIN ABC$\rightarrow$D and a 7.1\% realworld success rate gain over the strongest baseline.

</details>

---

### [[20_Research/Papers/机器人/Building_Generalization_Into_Behavior_Generation_Via_Adaptive_Compositions_of_Regularities|Building Generalization Into Behavior Generation Via Adaptive Compositions of Regularities]]

![[assets/2605.31110_figure.png|800]]

- **arXiv**: [2605.31110](https://arxiv.org/abs/2605.31110)
- **PDF**: https://arxiv.org/pdf/2605.31110
- **详细分析**: [[20_Research/Papers/机器人/Building_Generalization_Into_Behavior_Generation_Via_Adaptive_Compositions_of_Regularities|Building Generalization Into Behavior Generation Via Adaptive Compositions of Regularities]]
- **作者**: Aravind Battaje, Malte Bernhard, Vito Mengers, Oliver Brock
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Building Generalization Into Behavior Generation Via Adaptive Compositions of Regularities》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalization in robotics requires prior knowledge about how the world is structured, yet this structure changes from one situation to the next. This paper investigates the proposition that generalization arises from adaptively composing regularities -- predictable relationships within the robot-environment system -- into situation-appropriate structures for behavior generation. We examine this proposition by analyzing the mechanism in AICON (Active InterCONnect), a framework representing regularities as interacting processes in a differentiable network, where sensory feedback realizes composition and gradient descent generates behavior. To isolate adaptive composition as the key mechanism, we study a simple simulated problem in which all relevant regularities can be identified. We expose the resulting model to a wide range of novel conditions not considered during design, and we find that it generates context-appropriate behavior in all but one case, where encoded regularities are provably insufficient. Ablations reveal that the network automatically modulates which regularities influence behavior based on their informativeness. These results suggest that adaptive composition of regularities constitutes a powerful inductive bias for building generalization into behavior generation.

</details>

---

### [[20_Research/Papers/具身智能/Can_Aerial_VLA_Models_Cooperate_Evaluating_Closed-Loop_Air-Ground_Coordination_with_CARLA-Air|Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air]]

![[assets/2605.31066_figure.png|800]]

- **arXiv**: [2605.31066](https://arxiv.org/abs/2605.31066)
- **PDF**: https://arxiv.org/pdf/2605.31066
- **详细分析**: [[20_Research/Papers/具身智能/Can_Aerial_VLA_Models_Cooperate_Evaluating_Closed-Loop_Air-Ground_Coordination_with_CARLA-Air|Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air]]
- **作者**: Tianle Zeng, Yanci Wen, Xueang Yu, Hong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.8，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Can Aerial VLA Models Cooperate? Evaluating Closed-Loop Air-Ground Coordination with CARLA-Air》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AerialVLA, AirSim, SimWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent aerial vision-language-action (VLA) models show promising single-UAV capabilities, such as tracking moving objects and navigating to language-specified landmarks. However, it remains unclear whether these capabilities can transfer to air-ground cooperation, where a UAV and a UGV must act jointly in a shared, closed-loop physical world. We study this question with CARLA-Air, a single-process air-ground evaluation environment that unifies CARLA and AirSim inside one Unreal Engine runtime. By sharing the same world state, physics tick, and sensing pipeline, CARLA-Air enables physically consistent UAV--UGV interaction and precise measurement of simulation-timestamp alignment and effective coordination latency. Using CARLA-Air, we evaluate representative aerial VLA and planning baselines on two complementary diagnostic tasks: moving-platform landing and occlusion-recovery escort. The results show that current aerial VLA models can often track or follow a ground partner, but struggle to convert this single-agent competence into stable cooperative behavior. State prompting provides limited benefit, and naive bidirectional interaction fails to consistently improve performance and can amplify errors for most baselines. These findings suggest that, under the tested text-based cue interfaces, zero-shot cooperative air-ground VLA requires three components beyond the current paradigm: explicit partner-state grounding, low-latency action coordination, and team-level objective alignment. Our code is available at https://github.com/louiszengCN/CarlaAir.

</details>

---

### [[20_Research/Papers/具身智能/RDGen_Demonstration_Generation_for_High-Quality_Robot_Learning_via_Reinforcement_Learning|RDGen: Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning]]

![[assets/2605.30957_figure.png|800]]

- **arXiv**: [2605.30957](https://arxiv.org/abs/2605.30957)
- **PDF**: https://arxiv.org/pdf/2605.30957
- **详细分析**: [[20_Research/Papers/具身智能/RDGen_Demonstration_Generation_for_High-Quality_Robot_Learning_via_Reinforcement_Learning|RDGen: Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning]]
- **作者**: Zijian Zhu, Menglin Zou, Zhuang Li, Yaojie Tu, Xinhai Sun
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.2，大模型 0.1，强化学习 0.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RDGen: Demonstration Generation for High-Quality Robot Learning via Reinforcement Learning》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for general-purpose robot control. However, their performance remains fundamentally constrained by the availability of high-quality robot trajectory data. In current robot learning practice, such data are primarily collected through human teleoperation, which is labor-intensive, costly, and difficult to scale. In this paper, we propose RDGen, a sim-to-real reinforcement learning framework for generating high-quality robot demonstrations. Rather than employing reinforcement learning solely as the final control policy, RDGen leverages trained RL policies as a structured trajectory generator. The system consists of a VLM-based task parser that identifies task-relevant objects, a Grounding DINO-based object localizer, and an RL policy transferred from simulation to the real robot. Successful rollouts are then harvested as clean, high-quality demonstrations for downstream VLA training, while the simulation stage further provides a scalable source of additional trajectories at little marginal cost. Experiments on a pick-and-place task demonstrate that the transferred RL policy achieves a high task success rate. Compared with human teleoperation, RDGen produces significantly smoother trajectories and yields superior downstream VLA performance. These results indicate that RL-generated demonstrations can serve as more reliable and consistent supervisory signals for robot policy learning.

</details>

---

### [[20_Research/Papers/强化学习/Enhancing_Human-Likeness_in_Reinforcement_Learning_Agents_via_Hierarchical_Macro_Action_Quantization|Enhancing Human-Likeness in Reinforcement Learning Agents via Hierarchical Macro Action Quantization]]

![[assets/2605.30928_figure.png|800]]

- **arXiv**: [2605.30928](https://arxiv.org/abs/2605.30928)
- **PDF**: https://arxiv.org/pdf/2605.30928
- **详细分析**: [[20_Research/Papers/强化学习/Enhancing_Human-Likeness_in_Reinforcement_Learning_Agents_via_Hierarchical_Macro_Action_Quantization|Enhancing Human-Likeness in Reinforcement Learning Agents via Hierarchical Macro Action Quantization]]
- **作者**: Usman Nizamani, M. Shaheer Luqman, Fawad Javed Fateh, Ali Shah Ali, Murad Popattia, M. Zeeshan Zia, Quoc-Huy Tran
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Enhancing Human-Likeness in Reinforcement Learning Agents via Hierarchical Macro Action Quantization》归入 强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-like agents are a long-standing goal of artificial intelligence. Despite strong performance, most reinforcement learning (RL) agents remain reward-driven and often exhibit behaviors that differ from humans, limiting interpretability and reliability. In this work, we introduce a novel human-like RL framework that predicts action sequences closely aligned with human behaviors while maximizing rewards. Specifically, we encode human demonstrations into macro actions using a hierarchical macro action quantization approach (termed HiMAQ) consisting of two successive levels of vector quantization. The lower quantization level maps input actions to fine-grained subaction clusters, while the higher quantization level aggregates these subaction clusters into action clusters. Extensive evaluations on the D4RL benchmarks show that our hierarchical approach outperforms the non-hierarchical baseline (MAQ), achieving better human-likeness scores while maintaining comparable or better success rates than previous RL agents. The improvements generalize across integrations with various RL algorithms, namely IQL, SAC, and RLPD.

</details>

---

### [[20_Research/Papers/具身智能/Wall-OSS-0.5_Technical_Report|Wall-OSS-0.5 Technical Report]]

![[assets/2605.30877_figure.png|800]]

- **arXiv**: [2605.30877](https://arxiv.org/abs/2605.30877)
- **PDF**: https://arxiv.org/pdf/2605.30877
- **详细分析**: [[20_Research/Papers/具身智能/Wall-OSS-0.5_Technical_Report|Wall-OSS-0.5 Technical Report]]
- **作者**: Ryan Yu, Pushi Zhang, Starrick Liu, Brae Liu, Miracle Kang, Shalfun Li, Lights Shi, Ellie Ma, Ping Yang, Chris Pan, Jerry Chen, Dongxiu Liu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Wall-OSS-0.5 Technical Report》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale Vision-Language-Action (VLA) pretraining is increasingly adopted as the foundation for robot policies, yet the evidence for pretrained VLAs is almost invariably reported after task-specific fine-tuning.This leaves a foundational question unanswered: does VLA pretraining itself yield executable robot behavior, or does it merely furnish a better initialization for downstream policy learning? We present Wall-OSS-0.5, an open-source 4B VLA built upon a 3B VLM backbone augmented with action-generation components, designed so that pretrained robotic capability is directly measurable on physical hardware.The model is pretrained across more than 20 embodiments, processing over one million robot trajectories per epoch alongside a grounded multimodal corpus. We adopt a gradient-bridged co-training recipe in which three objectives play distinct and complementary roles: discrete action prediction routes strong VLM-native gradients into the backbone, multimodal prediction preserves grounded vision-language understanding, and continuous flow matching serves as the deployment-time action interface. Before task-specific fine-tuning, the pretrained checkpoint achieves non-trivial zero-shot real-robot behavior, completing several tasks, including a held-out deformable manipulation task, at high task progress on a 17-task suite. After fine-tuning, the same checkpoint serves as a stronger adaptation prior, reaching 60.5% average task progress on 15 real-robot tasks and outperforming π_0.5 by 17.5%. Multimodal evaluations further confirm that action training does not erode grounded vision-language competence: the model preserves broad vision-language ability while strengthening embodied grounding. Together, these results reposition VLA pretraining from an initialization strategy to a directly testable, already useful source of robot capability.

</details>

---

### [[20_Research/Papers/具身智能/High-Load-Density_Electro-Permanent_Magnetic_Foot_with_Controllable_Adhesion_for_Quadruped_Wall-Climbing_Robots|High-Load-Density Electro-Permanent Magnetic Foot with Controllable Adhesion for Quadruped Wall-Climbing Robots]]

![[assets/2605.30849_first_page.png|800]]

- **arXiv**: [2605.30849](https://arxiv.org/abs/2605.30849)
- **PDF**: https://arxiv.org/pdf/2605.30849
- **详细分析**: [[20_Research/Papers/具身智能/High-Load-Density_Electro-Permanent_Magnetic_Foot_with_Controllable_Adhesion_for_Quadruped_Wall-Climbing_Robots|High-Load-Density Electro-Permanent Magnetic Foot with Controllable Adhesion for Quadruped Wall-Climbing Robots]]
- **作者**: An Li, Bo Tao, I-Ming Chen, Han Ding
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《High-Load-Density Electro-Permanent Magnetic Foot with Controllable Adhesion for Quadruped Wall-Climbing Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

To enable reliable climbing locomotion of quadruped robots on ferromagnetic surfaces, this paper presents a high-load-density electro-permanent magnetic foot with controllable adhesion, featuring force-feedback circular Halbach-net electro-permanent magnet (CHN-EPM) adhesion units and a magnetization control system. Due to its three-dimensional magnetic circuit structure and flux-concentration effect, the CHN-EPM enables a distributed parallel magnetic flux path with enhanced flux utilization, resulting in reduced sensitivity to air-gap variations and allowing effective adhesion to be maintained even under partial contact conditions. The proposed CHN-EPM generates a maximum adhesion force exceeding 1000 N with a load-to-weight ratio over 200:1. A magnetization driver and a two-stage pulse current control strategy are developed to regulate the excitation current amplitude and duration, enabling accurate and reliable magnetization. By incorporating a flexible pressure sensor for contact force feedback, the system can effectively monitor attachment and detachment states, ensuring robust adhesion switching under uncertain contact conditions. The proposed system is integrated into a commercial quadruped robot (Unitree GO2), demonstrating high-load adhesion on ceiling and vertical-wall surfaces and stable locomotion on painted, perforated, and curved ferromagnetic surfaces.

</details>

---

### [[20_Research/Papers/具身智能/Feat2Go_Visual_Feature-Grounded_Value_Estimation_for_Embodied_Reinforcement_Learning|Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning]]

![[assets/2605.30795_figure.png|800]]

- **arXiv**: [2605.30795](https://arxiv.org/abs/2605.30795)
- **PDF**: https://arxiv.org/pdf/2605.30795
- **详细分析**: [[20_Research/Papers/具身智能/Feat2Go_Visual_Feature-Grounded_Value_Estimation_for_Embodied_Reinforcement_Learning|Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning]]
- **作者**: Junyang Shu, Zhiwei Lin, Bingqing Wei, Yongtao Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 3.6（加权：具身智能 2.1，强化学习 1，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Feat2Go: Visual Feature-Grounded Value Estimation for Embodied Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, RL-for-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning is a promising approach for improving the capabilities of vision-language-action (VLA) models while avoiding the heavy data requirements of imitation learning. However, its effectiveness for VLA models is often constrained by sparse supervision and the difficulty of designing informative reward signals for long-horizon manipulation. In this work, we present Feat2Go, a fine-grained value estimation framework for embodied reinforcement learning. Specifically, Feat2Go first derives a continuous progress target from a pretrained visual world model by measuring patch-level similarity to subgoal states and partitioning episodes into semantic stages with trend-based clustering. We then train an embodied value model to predict this structural progress from the current observation and task instruction, and use the predicted value to reshape terminal rewards during policy optimization. The proposed framework is compatible with existing VLA policy reinforcement learning pipelines, including PPO and GRPO, and does not rely on manual reward engineering. Extensive experiments on ManiSkill3 and RoboTwin 2.0 demonstrate that Feat2Go consistently improves the performance of existing VLA models under both single-arm and bimanual manipulation settings. More specifically, on ManiSkill3, Feat2Go improves OpenVLAOFT from 17.5% to 82.9% average out-of-distribution success while retaining 96.9% in-distribution performance. On RoboTwin 2.0, Feat2Go achieves an average success rate of 88.8% in domain-randomized task settings, outperforming prior reinforcement learning methods.

</details>

---

### [[20_Research/Papers/具身智能/Object-Informed_Model_Predictive_Path_Integral_Control_for_Non-Prehensile_Robot_Manipulation|Object-Informed Model Predictive Path Integral Control for Non-Prehensile Robot Manipulation]]

![[assets/2605.30778_figure.png|800]]

- **arXiv**: [2605.30778](https://arxiv.org/abs/2605.30778)
- **PDF**: https://arxiv.org/pdf/2605.30778
- **详细分析**: [[20_Research/Papers/具身智能/Object-Informed_Model_Predictive_Path_Integral_Control_for_Non-Prehensile_Robot_Manipulation|Object-Informed Model Predictive Path Integral Control for Non-Prehensile Robot Manipulation]]
- **作者**: Nikola Raicevic, Bharath Raam Radhakrishnan, Chenbin Yu, Ki Myung Brian Lee, Nikolay Atanasov
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Object-Informed Model Predictive Path Integral Control for Non-Prehensile Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon planning for non-prehensile robot manipulation is challenging due to underactuated and discontinuous interactions. We propose a hierarchical formulation of model predictive path integral (MPPI) control that guides robot-level planning with a separately computed object-level plan to achieve efficient long-horizon prediction. We first solve a simplified object-only problem, assuming the object can be actuated directly, and use the planned object trajectory as a reference in solving the joint robot-object planning problem. We evaluate our method in both simulation and hardware using a 6-DoF xArm6 manipulator to perform object pushing tasks in which the target object must reach a goal while avoiding static obstacles, necessitating non-myopic reasoning. Our object-informed MPPI increases task success by 40\% with a 26\% faster control frequency in simulation, and by 20\% in real experiments with similar computation as regular MPPI.

</details>

---

### [[20_Research/Papers/具身智能/SSR_Scaling_Surefooted_and_Symmetric_Humanoid_Traversal_to_the_Open_World|SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World]]

![[assets/2605.30770_figure.png|800]]

- **arXiv**: [2605.30770](https://arxiv.org/abs/2605.30770)
- **PDF**: https://arxiv.org/pdf/2605.30770
- **详细分析**: [[20_Research/Papers/具身智能/SSR_Scaling_Surefooted_and_Symmetric_Humanoid_Traversal_to_the_Open_World|SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World]]
- **作者**: Ruiqi Yu, Yiwen Wang, Yuan Hao, Jun WU, Qiuguo Zhu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《SSR: Scaling Surefooted and Symmetric Humanoid Traversal to the Open World》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Extending humanoid traversal to the open world is key to practical deployment in human environments, but remains challenging. The robot must use vision to ensure safe and reliable foot placement on heterogeneous terrain under highly dynamic motion, while producing coordinated, natural whole-body behaviors. We propose SSR, an efficient end-to-end framework for egocentric vision-based humanoid traversal that jointly learns these capabilities. SSR introduces imagined foothold guidance, which learns to model forthcoming swing-foot contacts and evaluates their support to guide pre-touchdown swings toward stable regions, reducing edge slips. It further employs equivariant latent-space symmetry augmentation to efficiently induce bilateral coordination under high-dimensional visual observations, and uses terrain-specific multi-discriminator motion priors to encourage human-like behavior across scenes. Extensive experiments show that SSR achieves safe, stable, and high-quality locomotion on diverse real-world terrains, including stairs with varied structures and extreme challenges such as wide gaps and high platforms, while enabling reliable long-horizon traversal in open outdoor environments.

</details>

---

### [[20_Research/Papers/具身智能/Geometry-Aware_Control_Barrier_Functions_for_Collision_Avoidance_via_Bernstein_Polynomial_Approximations|Geometry-Aware Control Barrier Functions for Collision Avoidance via Bernstein Polynomial Approximations]]

![[assets/2605.30696_figure.png|800]]

- **arXiv**: [2605.30696](https://arxiv.org/abs/2605.30696)
- **PDF**: https://arxiv.org/pdf/2605.30696
- **详细分析**: [[20_Research/Papers/具身智能/Geometry-Aware_Control_Barrier_Functions_for_Collision_Avoidance_via_Bernstein_Polynomial_Approximations|Geometry-Aware Control Barrier Functions for Collision Avoidance via Bernstein Polynomial Approximations]]
- **作者**: Siwon Jo, Yanze Zhang, Yupeng Yang, Wenhao Luo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Geometry-Aware Control Barrier Functions for Collision Avoidance via Bernstein Polynomial Approximations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe navigation often relies on well-defined conditions based on the shape of robots and obstacles, and can be challenging when they have irregular geometries. While Control Barrier Functions (CBFs) offer an efficient mechanism to enforce safe set forward invariance, common shape surrogates (e.g., spheres or super-ellipsoids) either are overly conservative in unstructured scenes or require many local primitives, which inflates constraint counts and degrades real-time performance. In this paper, we introduce a novel geometry-aware Control Barrier Function (CBF) based on Bernstein-Polynomial Signed Distance Fields (BP-SDFs). It provides a unified way to represent the obstacles and robots, so as to represent the barrier function with a unified minimum distance. Benefiting from the differentiability of the Bernstein polynomials, one can easily enforce the control constraints in a closed loop. We validate the method's efficiency and performance to guarantee safety in single-robot navigation and heterogeneous multi-robot collision avoidance via simulations under different environments.

</details>

---

### [[20_Research/Papers/具身智能/Primitive_Subspaces_Mediate_Few-Shot_Transfer_in_VLAs|Primitive Subspaces Mediate Few-Shot Transfer in VLAs]]

![[assets/2605.30695_first_page.png|800]]

- **arXiv**: [2605.30695](https://arxiv.org/abs/2605.30695)
- **PDF**: https://arxiv.org/pdf/2605.30695
- **详细分析**: [[20_Research/Papers/具身智能/Primitive_Subspaces_Mediate_Few-Shot_Transfer_in_VLAs|Primitive Subspaces Mediate Few-Shot Transfer in VLAs]]
- **作者**: Anya Singh, Cabrel Happi, Jai Relan, Varun Nair, Vidyut Baradwaj
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Primitive Subspaces Mediate Few-Shot Transfer in VLAs》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deploying vision-language-action (VLA) policies in industrial environments requires the ability to teach new tasks at low cost, a property current VLAs lack, since each new task requires fine-tuning. We investigate whether primitive-aware training produces a transferable artifact: a learned library of sub-skills that can be composed at inference time, conditioned on a small number of demonstrations, to perform tasks the policy was never trained on. We train two VLA architectures with different inductive biases, OpenVLA and $π_{0.5}$, on the REASSEMBLE contact-rich assembly dataset under matched LoRA fine-tuning recipes and locked hyperparameters, varying training between flat trajectories and primitive-segmented episodes with primitive-specific language prompts. We hold out 6 object-task combinations from training and evaluate few-shot transfer: models receive $m \in \{0, 1, 3, 5, 10\}$ demonstrations of a held-out task and attempt execution without weight updates. We replicate across three training seeds and validate on a second dataset (LIBERO-Long). Primitive-trained models reach 78% of fine-tuned upper-bound performance with only m=3 demonstrations, while flat-trained models require m=10 demonstrations to reach the same level -- a $3\times$ sample efficiency gap that replicates across seeds, architectures, and datasets. To establish causation, we ablate the primitive-decodable subspace of hidden states and show few-shot transfer degrades by 32 percentage points while ablating a random subspace of equal dimensionality has no effect, indicating primitive representations are causally necessary rather than incidentally correlated with transfer. We identify and correct a methodological pitfall in evaluating chunked policies: family-wise inflation of single-step action-range gates produces order-of-magnitude higher false-failure rates against ground-truth human demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/Exploiting_Chordal_Sparsity_for_Globally_Optimal_Estimation_with_Factor_Graphs|Exploiting Chordal Sparsity for Globally Optimal Estimation with Factor Graphs]]

![[assets/2605.30617_figure.png|800]]

- **arXiv**: [2605.30617](https://arxiv.org/abs/2605.30617)
- **PDF**: https://arxiv.org/pdf/2605.30617
- **详细分析**: [[20_Research/Papers/具身智能/Exploiting_Chordal_Sparsity_for_Globally_Optimal_Estimation_with_Factor_Graphs|Exploiting Chordal Sparsity for Globally Optimal Estimation with Factor Graphs]]
- **作者**: Avinash Subramanian, Connor Holmes, Timothy D. Barfoot, Frank Dellaert, Frederike Dümbgen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Exploiting Chordal Sparsity for Globally Optimal Estimation with Factor Graphs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust and efficient state estimation is crucial for perception, navigation, and control in robotics. State estimation problems are conveniently modeled using the factor-graph framework as enabled by modern software packages such as GTSAM or g2o. However, the standard solvers included in such frameworks are local and may converge to poor local minima, posing significant safety concerns. Conversely, techniques based on convex relaxations have been shown to provide a means of globally solving or certifying many state estimation problems. However, these relaxations 1) often require substantial effort to formulate, and 2) may incur significantly higher cost compared to efficient local solvers, as they require solving a large semidefinite program (SDP). In this work, we address both shortcomings by 1) creating a new procedure within the GTSAM framework for automatically constructing convex SDP relaxations for any factor graphs with common factor and variable types, and by 2) exploiting the Bayes tree constructions native to GTSAM to decompose the SDP problem, leading to significant speedup in solver time for chordally sparse problems. We demonstrate the favorable scaling of this structure-exploiting global estimator compared to standard local solvers for two case studies: A 3D pose-graph SLAM problem with a ring factor graph and a 2D localization problem with a chain factor graph. The software framework is available at https://github.com/borglab/gtsam.

</details>

---

### [[20_Research/Papers/具身智能/Any-ttach_Quick_End-effector_Swapping_Enables_Manipulation_Dexterity_with_Simplicity|Any-ttach: Quick End-effector Swapping Enables Manipulation Dexterity with Simplicity]]

![[assets/2605.30569_figure.png|800]]

- **arXiv**: [2605.30569](https://arxiv.org/abs/2605.30569)
- **PDF**: https://arxiv.org/pdf/2605.30569
- **详细分析**: [[20_Research/Papers/具身智能/Any-ttach_Quick_End-effector_Swapping_Enables_Manipulation_Dexterity_with_Simplicity|Any-ttach: Quick End-effector Swapping Enables Manipulation Dexterity with Simplicity]]
- **作者**: Weizhe Ni, Jinzhou Li, Haoyu Li, Cody Andres Alessio-Bunnell, Wenjing Pan, Xianyi Cheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Any-ttach: Quick End-effector Swapping Enables Manipulation Dexterity with Simplicity》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation dexterity is often pursued by building increasingly complex high-DoF multifingered hands. While many robotic hands are designed to replicate human morphology, the functional role of human hands suggests a different perspective: much of their complexity may exist to enable tool use and tool making. This observation motivates Any-ttach, a tool-centric manipulation framework that treats quick end-effector swapping as a mechanism for dexterity with simplicity. Any-ttach combines a low-cost automatic swapping mechanism for an open-close robot interface, a handheld device for collecting human demonstrations, and a task planning framework that composes learned, parameterized, and planned tool-use skills. The system supports diverse tools and end-effector modules, including daily tools, articulated tools such as scissors, Fin Ray fingers, and a low-cost anthropomorphic hand, through the same shared interface. Our experiments show that Any-ttach improves tool-swapping reliability, increases demonstration efficiency, reduces tool-pose variability, and supports diverse tool-use skills. In two long-horizon tasks, making a sandwich and preparing a cucumber, Any-ttach executes six tool-use subskills through end-effector switching and execution monitoring. These results suggest that robots can expand manipulation capability not only through more complex end-effectors, but also through rapidly exchangeable tools and end-effector modules. More details and videos are available at https://any-ttach.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Physics-informed_Goal-Conditioned_Reinforcement_Learning_under_Hybrid_Contact_Dynamics|Physics-informed Goal-Conditioned Reinforcement Learning under Hybrid Contact Dynamics]]

![[assets/2605.30503_figure.png|800]]

- **arXiv**: [2605.30503](https://arxiv.org/abs/2605.30503)
- **PDF**: https://arxiv.org/pdf/2605.30503
- **详细分析**: [[20_Research/Papers/具身智能/Physics-informed_Goal-Conditioned_Reinforcement_Learning_under_Hybrid_Contact_Dynamics|Physics-informed Goal-Conditioned Reinforcement Learning under Hybrid Contact Dynamics]]
- **作者**: Vittorio Giammarino, Anastasios Manganaris, Ahmed H. Qureshi
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Physics-informed Goal-Conditioned Reinforcement Learning under Hybrid Contact Dynamics》归入 强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GCRL, Pi-GCRL, QRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning to reach arbitrary goals from sparse feedback requires agents to infer a rich notion of reachability across state--goal pairs. Goal-conditioned reinforcement learning (GCRL) tackles this challenge by learning policies that generalize across goals, but this generalization becomes increasingly difficult as the underlying dynamics become high-dimensional, hybrid, or contact-dependent. To address this issue, physics-informed GCRL (Pi-GCRL) introduces optimal-control-inspired inductive biases into goal-conditioned value learning. While Pi-GCRL methods have proven effective in navigation and object-free goal-reaching domains, their reliability in contact-rich tasks remains unclear, where contact interactions induce hybrid dynamics, mode-dependent controllability, and nonsmooth value landscapes. In this work, we show that these structural properties can cause existing Pi-GCRL methods to degrade when applied naively to contact-rich manipulation. Motivated by this analysis, we introduce contact-aware and hierarchical formulations that apply physics-informed inductive biases selectively across the manipulation problem. Our results provide a principled step toward extending Pi-GCRL to contact-rich manipulation.

</details>

---

### [[20_Research/Papers/机器人/CoMo3R-SLAM_Collaborative_Monocular_Dense_SLAM_with_Learned_3D_Reconstruction_Priors_for_Outdoor_Multi-Agent_Systems|CoMo3R-SLAM: Collaborative Monocular Dense SLAM with Learned 3D Reconstruction Priors for Outdoor Multi-Agent Systems]]

![[assets/2605.30488_figure.png|800]]

- **arXiv**: [2605.30488](https://arxiv.org/abs/2605.30488)
- **PDF**: https://arxiv.org/pdf/2605.30488
- **详细分析**: [[20_Research/Papers/机器人/CoMo3R-SLAM_Collaborative_Monocular_Dense_SLAM_with_Learned_3D_Reconstruction_Priors_for_Outdoor_Multi-Agent_Systems|CoMo3R-SLAM: Collaborative Monocular Dense SLAM with Learned 3D Reconstruction Priors for Outdoor Multi-Agent Systems]]
- **作者**: Zhihao Cao, Qi Shao, Shuhao Zhai, Feng Tian, Anh Nguyen, Hesheng Wang, Baoru Huang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.4，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《CoMo3R-SLAM: Collaborative Monocular Dense SLAM with Learned 3D Reconstruction Priors for Outdoor Multi-Agent Systems》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaborative dense SLAM is essential for multi-robot teams to achieve scalable and consistent 3D perception across large-scale outdoor environments. Existing systems typically depend on depth sensors, incurring significant payload, power, and calibration costs. Monocular RGB cameras are a lightweight alternative, but collaborative monocular dense SLAM remains difficult due to scale ambiguity, unreliable inter-agent data association, especially in outdoor scenes where low overlap and repetitive structures make traditional feature matching unreliable, motivating robust geometric information. We propose CoMo3R-SLAM, the first collaborative monocular dense RGB SLAM system that leverages robust learned feed-forward 3D reconstruction priors for outdoor multi-agent mapping. Each agent runs a prior-guided front-end for real-time tracking and local dense fusion, while a coordinator performs dense pointmap matching for cross-agent verification, closed-form Sim(3) gauge synchronization, and GPU-accelerated global bundle adjustment with segment-level depth optimization. Requiring neither depth sensors nor parametric intrinsics, our system produces robust cross-agent constraints and globally consistent metric maps from monocular RGB alone. On Tanks and Temples and Waymo sequences, CoMo3R-SLAM achieves the best ATE on three of four Tanks and Temples scenes and competitive Waymo accuracy, matching or exceeding state-of-the-art RGB-D methods while running online at 8 FPS.

</details>

---

### [[20_Research/Papers/具身智能/ELAN4D_Embodiment-Centric_4D_Supervision_for_Vision-Language-Action_Models_via_Plug-and-Play_Adaptation|ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models via Plug-and-Play Adaptation]]

![[assets/2605.30484_figure.png|800]]

- **arXiv**: [2605.30484](https://arxiv.org/abs/2605.30484)
- **PDF**: https://arxiv.org/pdf/2605.30484
- **详细分析**: [[20_Research/Papers/具身智能/ELAN4D_Embodiment-Centric_4D_Supervision_for_Vision-Language-Action_Models_via_Plug-and-Play_Adaptation|ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models via Plug-and-Play Adaptation]]
- **作者**: Zeyuan He, Bowen Yang, Zhirui Fang, Keru Zhou, Lei Jiang, Jingjing Qian, Fan Mo, Junchi Yan, Philip Torr, Xiu Li, Li Jiang, Jialin Yu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ELAN4D: Embodiment-Centric 4D Supervision for Vision-Language-Action Models via Plug-and-Play Adaptation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ControlNet, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown promise for robotic manipulation, yet most existing policies operate reactively by directly regressing actions from current observations, without explicitly modeling future dynamics. This limits their ability to generalize under out-of-distribution perturbations. To address this issue, we propose ELAN4D, an embodiment-centric, 4D-aware training framework that enhances VLA policies with future robot keypoint tracks as predictive spatio-temporal supervision. Using only forward kinematics from proprioceptive states, we derive 3D displacement tracks of robot keypoints, such as joints and the end-effector, with negligible preprocess cost. These tracks provide metric and compact supervision without requiring external trackers or reconstruction. A plug-and-play auxiliary branch with a lightweight track decoder injects this 4D signal into the action expert while preserving the pretrained vision-language backbone through gradient isolation. The track decoder is discarded during inference, leaving the base policy interface unchanged. Extensive experiments on LIBERO, LIBERO-Plus, RoboTwin2.0 and real-world manipulation tasks demonstrate that ELAN4D consistently improves over strong VLA baselines, achieving the best overall performance and substantial gains under out-of-distribution perturbations, including camera, background, and layout shifts. These results highlight the effectiveness of embodiment-centric 4D supervision for building more robust and generalizable manipulation policies.

</details>

---

### [[20_Research/Papers/具身智能/Learning-Based_Navigation_for_Indoor_Mobile_Robots|Learning-Based Navigation for Indoor Mobile Robots]]

![[assets/2605.30468_figure.png|800]]

- **arXiv**: [2605.30468](https://arxiv.org/abs/2605.30468)
- **PDF**: https://arxiv.org/pdf/2605.30468
- **详细分析**: [[20_Research/Papers/具身智能/Learning-Based_Navigation_for_Indoor_Mobile_Robots|Learning-Based Navigation for Indoor Mobile Robots]]
- **作者**: Tri-Tin Nguyen, Tien-Dat Nguyen, Gia-Uy Le, Vinh Nguyen, Vinh-Hao Nguyen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Learning-Based Navigation for Indoor Mobile Robots》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, DWA-RL, MPNet, PRM-RL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a learning-based navigation framework for indoor mobile robots. The proposed method combines a supervised neural global planner, trained from cost-aware A* expert trajectories, with the proposed Learning-Based DWA local planner, which is formulated as discrete candidate selection over the Dynamic Window Approach (DWA) action lattice. For local planning, the policy is first trained by behavior cloning and then refined by Proximal Policy Optimization (PPO) under feasibility-aware masking. The framework is implemented and evaluated in both simulated and real-world indoor environments. Experimental results show that the proposed method generates feasible global routes and reliable local motion commands for safe goal-directed navigation in the presence of obstacles. These results demonstrate the effectiveness of integrating learning-based global planning with reinforcement-learning-refined local control for indoor mobile robot navigation. The source code will be released at https://ntdathp.github.io/rl_robot_web/.

</details>

---
