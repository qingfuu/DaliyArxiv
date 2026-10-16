# cs.CV | Computer Vision and Pattern Recognition | 2026-10-14

#arxiv #ComputerScience

**论文数**: 16

### [[20_Research/Papers/世界模型/Grid_or_Nodes_Probing_Object_Memory_in_World_Models_Under_Partial_Observability|Grid or Nodes? Probing Object Memory in World Models Under Partial Observability]]

![[assets/2610.18637_first_page.png|800]]

- **arXiv**: [2610.18637](https://arxiv.org/abs/2610.18637)
- **PDF**: https://arxiv.org/pdf/2610.18637
- **详细分析**: [[20_Research/Papers/世界模型/Grid_or_Nodes_Probing_Object_Memory_in_World_Models_Under_Partial_Observability|Grid or Nodes? Probing Object Memory in World Models Under Partial Observability]]
- **作者**: Justin McMillen, Yasin Yilmaz
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能, 强化学习
- **相关性评分**: 1.92（加权：具身智能 0.3，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《Grid or Nodes? Probing Object Memory in World Models Under Partial Observability》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MemoBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot's world model must remember objects that leave the camera's view. FloWM, a learned world model, keeps them in a spatial grid of features that it moves with five built-in velocities. A node memory instead keeps each object's position and velocity as numbers. We compare them in FloWM's own block world, with an oracle-fed Kalman tracker as the node memory. How the grid is read changes its score: a single-cell probe finds 66% of out-of-view blocks, while FloWM's own probe 89%. FloWM also scores 8 points higher in view although no frame is shown, which we attribute to its write-back of its own predictions. Out of view, the tracker reaches FloWM's range in 14KB against 5.6MB, with no probe. On diagonal motion, outside its five velocities, FloWM finds 11% of blocks even after fine-tuning, while the unchanged tracker keeps 93%. Faster blocks defeat both until one more allowed speed takes the tracker to 94%, where FloWM's built-in shifts would need 25 copies of its grid. A learned node memory must still replace the oracles and handle velocity under noise, long gaps, and the bounce.

</details>

---

### [[20_Research/Papers/强化学习/DexStitch_Learning_and_Composing_Dexterous_Skills_from_Human_Videos_via_Contact-Aware_Robotic_Inpainting|DexStitch: Learning and Composing Dexterous Skills from Human Videos via Contact-Aware Robotic Inpainting]]

![[assets/2610.17789_figure.png|800]]

- **arXiv**: [2610.17789](https://arxiv.org/abs/2610.17789)
- **PDF**: https://arxiv.org/pdf/2610.17789
- **详细分析**: [[20_Research/Papers/强化学习/DexStitch_Learning_and_Composing_Dexterous_Skills_from_Human_Videos_via_Contact-Aware_Robotic_Inpainting|DexStitch: Learning and Composing Dexterous Skills from Human Videos via Contact-Aware Robotic Inpainting]]
- **作者**: Byeonggyeol Choi, Seongmin Jung, Unghui Nam, Youngbo Song, Sunhong Min, MinHyung Lee, Byonghyo Shim, Yongseok Lee
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexStitch: Learning and Composing Dexterous Skills from Human Videos via Contact-Aware Robotic Inpainting》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A long-horizon manipulation task consists of primitive skills and the transitions connecting them. Learning skills that can be executed in sequence requires supervision for both, which is costly to collect on a robot. Human videos offer a scalable source of demonstrations, but transferring them to robots requires extracting robot-compatible observations and actions together with their skill structure. We present DexStitch, a framework that cuts long-horizon human videos into skills and transitions, converts them into aligned robot observation-action-skill data, and stitches the learned skills into a requested sequence. A skill classifier first segments the videos into manipulation skills and transitions. DexStitch then converts the human demonstrations into robot observations and actions while retaining their corresponding skill labels. During conversion, per-finger human-object contacts guide dexterous hand retargeting and robotic inpainting, preserving contact geometry and finger-object occlusion ordering. To stitch the learned skills into a sequence, a shared skill-conditioned policy is pretrained on the resulting synthetic data and finetuned on a mixture of synthetic data and a small set of single-skill teleoperation episodes. Conditioning on the current and next skills guides each transition toward the following skill, while predicted skill progression enables closed-loop switching. On a held-out session, the classifier agrees with manual annotations on 92.4% of frames. Across four household skills, DexStitch achieves 80.0% single-skill success and 77.5% sequence success.

</details>

---

### [[20_Research/Papers/具身智能/Code2Worlds-2_Physically_Plausible_Agent_Harness_for_Embodied_World_Simulation|Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation]]

![[assets/2610.17651_figure.png|800]]

- **arXiv**: [2610.17651](https://arxiv.org/abs/2610.17651)
- **PDF**: https://arxiv.org/pdf/2610.17651
- **详细分析**: [[20_Research/Papers/具身智能/Code2Worlds-2_Physically_Plausible_Agent_Harness_for_Embodied_World_Simulation|Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation]]
- **作者**: Haoyu Zhang, Siming Li, Zeyu Zhang, Yi Zhang, Tat-Seng Chua, Hao Tang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Code2Worlds-2: Physically Plausible Agent Harness for Embodied World Simulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, Generated-World, Meta-World, RLBench, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent coding large language models (LLMs) can synthesize dynamic 4D worlds from natural language, but the resulting content remains a visual artifact. It lacks physical semantics such as the collision geometry, mass, friction, inertia, and joint structure, required to enable it to simulate the physical world, and its dynamics are scripted to look plausible rather than designed to execute. What is needed is an executable world: one that a physics engine can load and step, resolving contact physically. We present Code2Worlds-2, an extension of Code2Worlds that turns 4D world generation into an embodied world simulation. We keep the original dual-stream generation pipeline intact and append two modules. First, a SimReady Scene Compiler that turns a generated visual scene into a simulator-compatible representation: it assigns collision meshes via convex decomposition, estimates physical attributes with a vision-language model, infers a lightweight support graph, instantiates the engine's contact, friction, and dynamics constraints, and applies a gravity settling pass, before exporting the scene as MuJoCo MJCF. Second, a Simulator-in-the-Loop 4D Refiner that implements an automated agent harness-a compile, simulate, critique and refine loop-that converts visual dynamics into executable rigid and articulated dynamics and evolves the physical settings rather than only the code, replacing the purely visual motion critic with a simulator critic that inspects penetration depth, collision pairs, stability, contact forces, joint limits, and robot reachability. We further propose SimCode4D, a state-based benchmark with five task templates for evaluating embodied simulation. Experiments on SimCode4D and across natural, indoor, industrial, urban, and service scenes show that Code2Worlds-2 produces physically plausible, simulator-compatible, and robot-interactable scenes.

</details>

---

### [[20_Research/Papers/具身智能/From_Pixels_to_Executable_Physics_Behavior-Grounded_World_Models_for_Embodied_Action_Consequence_Prediction|From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction]]

![[assets/2610.17630_figure.png|800]]

- **arXiv**: [2610.17630](https://arxiv.org/abs/2610.17630)
- **PDF**: https://arxiv.org/pdf/2610.17630
- **详细分析**: [[20_Research/Papers/具身智能/From_Pixels_to_Executable_Physics_Behavior-Grounded_World_Models_for_Embodied_Action_Consequence_Prediction|From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction]]
- **作者**: Ruo Chen, Jiahua Pang, Yingjie Niu, Hongyi Lin, Jun Tian, Yang Zhu, Chao Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 3.4（加权：具身智能 1.5，大模型 0.2，世界模型 1，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《From Pixels to Executable Physics: Behavior-Grounded World Models for Embodied Action Consequence Prediction》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In outdoor environments, varying terrain and contact conditions can cause identical action commands to produce different motion outcomes for quadruped robots. Predicting these outcomes is essential for reliable navigation and informed path selection. Existing video world models can generate visually plausible futures, yet often struggle to capture robot dynamics and terrain interactions, leading to overly optimistic predictions of action outcomes. We present DR-WM, a physically consistent world model that incorporates robot-terrain contact dynamics to predict the consequences of quadruped actions. Starting from an initial RGB image, our method reconstructs scene geometry and integrates dense, dimensionless priors over terrain contact properties, calibrated using real-world action-response data. The resulting terrain model supports the simulation of physics with spatially varying contact properties such as friction. Given the initial state of the robot and candidate action sequences, we simulate its future motion and use the resulting camera trajectories and rendered geometry to guide the training of a video world model. The generated future observations are then used to update the terrain reconstruction, enabling iterative model rollouts without additional real-world images. Extensive experiments demonstrate that DR-WM substantially outperforms geometry-only baselines and baselines with uniform physical parameters on key physical metrics characterizing action outcomes, while achieving the best performance among the evaluated baselines. These physically grounded predictions support more informed action selection: across 90 challenging scenarios, an 8B vision-language model augmented with DR-WM outperforms an unassisted 32B vision-language model on five of six evaluation metrics.

</details>

---

### [[20_Research/Papers/强化学习/DexNinja_Learning_Robust_Dexterous_Cutting_Policy_with_a_Real-to-Sim-to-Real_Data_Engine|DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine]]

![[assets/2610.17208_figure.png|800]]

- **arXiv**: [2610.17208](https://arxiv.org/abs/2610.17208)
- **PDF**: https://arxiv.org/pdf/2610.17208
- **详细分析**: [[20_Research/Papers/强化学习/DexNinja_Learning_Robust_Dexterous_Cutting_Policy_with_a_Real-to-Sim-to-Real_Data_Engine|DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine]]
- **作者**: Haozhe Lou, Runyi Yang, Wanqi Zhong, Caiyun Liu, Yicheng Liu, Wenhao Liu, Wenlong Ma, Jiawei Xia, Kanzhi Wu, Danda Pani Paudel, Luc Van Gool, Hang Zhao...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.7，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DexNinja: Learning Robust Dexterous Cutting Policy with a Real-to-Sim-to-Real Data Engine》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GSWorld, PointWorld, Real-to-Sim, Real2Sim, SplatSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cutting a piece of food looks effortless in human hands. For a robot, however, every cut is a high-contact interaction with a deformable, elasto-plastic object whose behavior changes with pose, contact mode, and cutting stage. Collecting real-world data is expensive and wasteful: each trial typically contaminates or damages the food, so obtaining scalable real world data for dexterous cutting is expensive and difficult. Simulation is an appealing alternative, but a large sim-to-real gap exists in both physics and perception. This gap is especially severe for topology-changing interactions like cutting, where small errors in contact, friction, or material and elasticity responses quickly compound. We propose \textsc{DexNinja}, a real2sim2real framework that turns a handful of real demonstrations into a dense and realistic training distribution. \textsc{DexNinja} (i) reconstructs object instances from real captures, (ii) randomizes physically meaningful parameters under category-level constraints, and (iii) produces augmented dexterous manipulation episodes using a custom differentiable simulator that couples robot dynamics, tactile contact, and deformable cutting. We evaluate \textsc{DexNinja} on a dexterous food-slicing task and show that (1) with tens of real demonstrations and hundreds of augmented simulator data, the success rate could reach more than 60\%. (2) the augmented data consistently improves success rates when only using real data with more than 20\% via sim-to-real, and (3) the resulting policies generalize to out-of-distribution objects with varying shapes and sizes.

</details>

---

### [[20_Research/Papers/具身智能/UniLAP_A_Unified_Latent_Action_Policy_for_Cross-Embodiment_Manipulation|UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation]]

![[assets/2610.16969_figure.png|800]]

- **arXiv**: [2610.16969](https://arxiv.org/abs/2610.16969)
- **PDF**: https://arxiv.org/pdf/2610.16969
- **详细分析**: [[20_Research/Papers/具身智能/UniLAP_A_Unified_Latent_Action_Policy_for_Cross-Embodiment_Manipulation|UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation]]
- **作者**: Lei Yao, Qiao Feng, Mutian Tong, Qihao Yun, Lap-Pui Chau, Lingjie Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《UniLAP: A Unified Latent Action Policy for Cross-Embodiment Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AdaWorld, DreamVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent Action Models (LAMs) can capture manipulation priors from action-free videos, but discrete latents usually impose a granularity bottleneck, limiting their ability to represent fine-grained action. Recent continuous alternatives mitigate this, but they are typically used as proxies for world modeling and require a further planning step to produce executable actions. We thus introduce UniLAP, a unified continuous latent-action policy that models the latent space via flow matching and bypasses reliance on future frames during inference. By distilling a LAM teacher with a flow-adaptive objective, UniLAP inherits the teacher's action representation while retaining the multimodal distribution of feasible behaviors. To decouple latent representations from task-irrelevant appearance, we extract a label-free motion target to isolate relevant kinematic cues from spurious visual dynamics. With the established embodiment-agnostic latent manifold, UniLAP can be easily adapted to novel platforms. Pretrained on multi-source videos at a compact 1.1B parameter scale, UniLAP outperforms state-of-the-art latent-action and Vision-Language-Action (VLA) baselines across hand pose forecasting, single-arm and humanoid manipulation, and real-world deployment.

</details>

---

### [[20_Research/Papers/具身智能/Language2Drive_Do_Vision-Language-Action_Models_Really_Follow_the_Instructions_in_Autonomous_Driving|Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?]]

![[assets/2610.16634_figure.png|800]]

- **arXiv**: [2610.16634](https://arxiv.org/abs/2610.16634)
- **PDF**: https://arxiv.org/pdf/2610.16634
- **详细分析**: [[20_Research/Papers/具身智能/Language2Drive_Do_Vision-Language-Action_Models_Really_Follow_the_Instructions_in_Autonomous_Driving|Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?]]
- **作者**: Zihan You, Zehua Fan, Wenqi Lyu, Aoqi Wang, Ni Wang, Yifei Yang, Linge Zhao, Huan Li, Sining Ang, Yuguang Yang, Jueyu Chen, Xiangyu Li...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Language2Drive: Do Vision-Language-Action Models Really Follow the Instructions in Autonomous Driving?》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlpSim, AlpaSim, RealSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent Vision-Language-Action (VLA) models increasingly use natural-language instructions to condition autonomous driving behavior. Yet existing closed-loop benchmarks primarily measure route completion, safety, and rule compliance, leaving a fundamental question unresolved: does language actually determine which feasible behavior the vehicle executes? A trajectory may be safe and successful while still violating or even ignoring the passenger's instruction. To address this, we introduce \ltd, a benchmark designed to directly test this capability. Its key evaluation unit, the paired counterfactual unit (PCU), holds the initial driving scene fixed while changing only the instruction. This design enables us to distinguish isolated instruction success from counterfactual paired success across four instruction-following scopes. To test whether this distinction persists across evaluation regimes, we instantiate Language2Drive in complementary closed-loop CARLA simulation, reconstructed real-world scenes, and open-loop driving benchmarks, including our released CARLA-Language2Drive simulator with purpose-built maps. Evaluating representative driving VLAs across these settings reveals a striking mismatch between strong driving competence and weak language control: 93.2% of successful rollouts do not have a successful counterpart under the alternative feasible instruction. This failure is dominated by one-sided completion, where a model repeatedly executes one preferred behavior but fails when the same scene requires the counterfactual alternative. These results expose two fundamental limitations of current evaluation: isolated success and driving scores, which are widely used by conventional driving benchmarks, can substantially overstate language-following capability, while current driving VLAs themselves lack reliable instruction following under matched counterfactual tests.

</details>

---

### [[20_Research/Papers/具身智能/Recovering_Low-Bit_Failures_in_Vision-Language-Action_Policies_via_Quantization-Conditioned_Reinforcement_Learning|Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning]]

![[assets/2610.15675_figure.png|800]]

- **arXiv**: [2610.15675](https://arxiv.org/abs/2610.15675)
- **PDF**: https://arxiv.org/pdf/2610.15675
- **详细分析**: [[20_Research/Papers/具身智能/Recovering_Low-Bit_Failures_in_Vision-Language-Action_Policies_via_Quantization-Conditioned_Reinforcement_Learning|Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning]]
- **作者**: Seongmin Park, Jaewon Lee, Yujun Heo, Yoonsik Kim, Seheon Choi, Hyoung-rock Kim, Jungwook Choi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 1，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Recovering Low-Bit Failures in Vision-Language-Action Policies via Quantization-Conditioned Reinforcement Learning》归入 具身智能、强化学习、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, QCRL, QVLA, QuantVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quantization lowers deployment costs of vision-language-action (VLA) policies but can compromise task completion. Across five VLA models and 4,050 real-world trials, we systematically reveal that quantization-aware training (QAT) generally improves on post-training quantization (PTQ) but leaves substantial gaps to full precision (FP) on long-horizon tasks and under visual and semantic shifts, while its imitation-based objective does not explicitly use rollout success or partial completion. To exploit these outcome signals, we introduce Quantization-Conditioned Reinforcement Learning (QCRL), an offline RL method coupling progress-based advantage estimation with quantization-aware source conditioning. FP rollouts supply reference experience beyond action-level distillation, progress-scaled terminal penalty distinguishes partial completion, and quantization-aware conditioning selects advantageous reference behavior within the quantized policy. We evaluate weight-only INT4 W4A16 on $π_{0.5}$ and GR00T N1.5 and joint weight-activation NVFP4 W4A4 on $π_{0.5}$. Using only in-distribution data, QCRL reaches 99.3% of FP's mean score across three visual-shift conditions for $π_{0.5}$ with INT4 W4A16, alongside 42.9% model-memory savings. With NVFP4 W4A4, it reaches 100.7% of the same FP baseline, alongside a $1.73\times$ speedup using NVFP4/FP8 deployment. Hardware gains are relative to FP16 on Jetson Thor.

</details>

---

### [[20_Research/Papers/机器人/RootSLAM_Square_Root_Bundle_Adjustment_for_Visual-Inertial_SLAM|RootSLAM: Square Root Bundle Adjustment for Visual-Inertial SLAM]]

![[assets/2610.15157_figure.png|800]]

- **arXiv**: [2610.15157](https://arxiv.org/abs/2610.15157)
- **PDF**: https://arxiv.org/pdf/2610.15157
- **详细分析**: [[20_Research/Papers/机器人/RootSLAM_Square_Root_Bundle_Adjustment_for_Visual-Inertial_SLAM|RootSLAM: Square Root Bundle Adjustment for Visual-Inertial SLAM]]
- **作者**: Tomás Santucci, Mateo de Mayo, Daniel Cremers, Taihú Pire
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《RootSLAM: Square Root Bundle Adjustment for Visual-Inertial SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient perception is a prerequisite for the small, low-power devices targeted by robotics, mixed reality, autonomous driving, and drone applications, all of which rely on Simultaneous Localization and Mapping (SLAM) to estimate their motion within their surroundings. Learning-based SLAM systems achieve state-of-the-art accuracy but are demanding in compute, whereas classical geometry-based methods retain a strong efficiency advantage with little to no loss in accuracy. In this work we present RootSLAM, a fully-featured visual-inertial SLAM system for multi-camera setups built on Basalt. RootSLAM achieves accuracy competitive with the state of the art while running up to 20 times faster, facilitating the deployment of perception systems in resource constrained environments. We adapt the square-root bundle adjustment formulation from structure from motion into the multi-camera visual-inertial SLAM setting through a novel reformulation that leverages the system's pose-graph, letting the global optimizer run in single-precision floating point, thus doubling its performance. We provide a thorough benchmark against the state of the art together with an ablation study of our contributions. Our new implementation, including its map management and loop detection module, pose-graph optimizer, and global mapping components, will be open-sourced.

</details>

---

### [[20_Research/Papers/具身智能/Flow-Support-Weighted_Proposals_for_Test-Time_Verified_VLA_Policies|Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies]]

![[assets/2610.14588_figure.png|800]]

- **arXiv**: [2610.14588](https://arxiv.org/abs/2610.14588)
- **PDF**: https://arxiv.org/pdf/2610.14588
- **详细分析**: [[20_Research/Papers/具身智能/Flow-Support-Weighted_Proposals_for_Test-Time_Verified_VLA_Policies|Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies]]
- **作者**: Chen Zhao, Zipeng Ye, Haitao Shen, Guanlin Li, Yuchen Xie, Jing Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Flow-Support-Weighted Proposals for Test-Time Verified VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Finite-Set, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Test-time sampling promises to turn one action prediction into a set of distinct executable candidates that a verifier can choose among. Downstream fine-tuning works against that promise. A vision-language-action model trained to solve one task distribution concentrates its flow-matching decoder around the dominant demonstrated action, so repeated samples differ only marginally and the verifier receives many copies of one decision. We call this proposal contraction and identify it as a key constraint on test-time scaling: repeated samples can remain highly redundant as the candidate budget grows. Action Dynamic Sampling (ADS) alleviates the constraint on the proposal side, during training. At each training step, ADS integrates $K$ additional trajectories from the current policy under fresh base noise, scores each by the flow support along its path with a Hutchinson trace estimator, and corrects the policy's local action distribution toward this weighted set through a detached finite-set KL term. Training cost rises; deployment cost is unchanged. Across simulation and four physical-robot tasks, ADS raises proposal spread without the success penalty that Gaussian perturbation incurs, lifts oracle best-of-8 success on RoboCasa from 57.6% to 63.0%, improves fixed verifiers by 2.4 to 4.9 points in simulation, and raises TokenPB by up to 13.0 points on real-world manipulation.

</details>

---

### [[20_Research/Papers/世界模型/Remembering_What_Matters_for_Long-Horizon_Robotic_World_Models|Remembering What Matters for Long-Horizon Robotic World Models]]

![[assets/2610.14583_figure.png|800]]

- **arXiv**: [2610.14583](https://arxiv.org/abs/2610.14583)
- **PDF**: https://arxiv.org/pdf/2610.14583
- **详细分析**: [[20_Research/Papers/世界模型/Remembering_What_Matters_for_Long-Horizon_Robotic_World_Models|Remembering What Matters for Long-Horizon Robotic World Models]]
- **作者**: Hao Wu, Tianyu Shao, Shengju Qian, Yizhou Zhao, Fan Zhang, Penghao Zhao, Weiyan Wang, Yufei Huang, Fan Xu, Kun Wang, Xin Wang, Ming-Hsuan Yang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，世界模型 1，机器人 1.1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Remembering What Matters for Long-Horizon Robotic World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autoregressive robot video world models based on discrete visual tokens remain unreliable over long rollout horizons. Retaining the entire generated history does not necessarily improve prediction quality. We investigate a possible memory-role conflict in Full Context decoding: persistent scene information, recent visual-action states, and stale generated history compete for attention despite their different predictive roles. This perspective motivates ReCAP (Receding Context with Anchor Preservation), a training-free context-scheduling method for long-horizon robot video world models. ReCAP keeps the pretrained tokenizer, world model, and visual decoder frozen. It preserves the initial scene anchor and a contiguous window of recent complete visual-action blocks while evicting older generated history. The schedule preserves within-block structure and temporal order, requires no additional modules or parameter updates, and bounds active-context growth independently of rollout length. We evaluate ReCAP on RT-1, BridgeV2, LIBERO-90, and CALVIN using frozen autoregressive world models. Across evaluated environments and horizons, ReCAP improves visual fidelity, action-conditioned consistency, and robot structure preservation relative to Full Context. On BridgeV2, it reduces LPIPS by 63.3%. In the system benchmark at H=64, it reduces the logical KV footprint by 73.3% and p50 latency by 6.51%. Attention analyses show increased attention to retained recent states, while history interventions associate larger amounts of stale context with higher prediction error. These observations are consistent with the memory-role-conflict hypothesis, although they do not isolate it from context-length and position-handling effects. Our results support inference-time context scheduling as a practical approach to improving long-horizon robot video prediction and computational efficiency without retraining.

</details>

---

### [[20_Research/Papers/具身智能/Disentangling_Task-Relevant_Latent_Dynamics_for_Reward_Modeling|Disentangling Task-Relevant Latent Dynamics for Reward Modeling]]

![[assets/2610.14159_figure.png|800]]

- **arXiv**: [2610.14159](https://arxiv.org/abs/2610.14159)
- **PDF**: https://arxiv.org/pdf/2610.14159
- **详细分析**: [[20_Research/Papers/具身智能/Disentangling_Task-Relevant_Latent_Dynamics_for_Reward_Modeling|Disentangling Task-Relevant Latent Dynamics for Reward Modeling]]
- **作者**: Dayou Li, Jionghao Wang, Peihao Wang, Jiuzhou Lei, Hao Wang, Jichen Chai, Hezhen Hu, Minghui Zheng, Zhangyang Wang, Xin Li, Wenping Wang, Zhiwen Fan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 0.6，强化学习 0.4，世界模型 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Disentangling Task-Relevant Latent Dynamics for Reward Modeling》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MetaWorld, Real-World, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward design remains a major bottleneck for reinforcement learning in robotic manipulation. Handcrafted dense rewards can compensate for the limited guidance provided by sparse rewards, but require substantial task-specific reward engineering. Learning rewards from videos provides a scalable, data-driven alternative to manual reward design. However, existing video-based rewards are often computed in entangled visual spaces where task-relevant state changes are confounded with extraneous visual variation. As a result, the learned reward may respond to visual distractors instead of actual task execution. To address this limitation, we propose DiTaR (Disentangling Task-Relevant Latent Dynamics for Reward Modeling), a framework for learning dense rewards from heterogeneous videos. DiTaR learns a continuous task-relevant representation from multi-frame video latents through an asymmetric two-stage procedure that suppresses task-irrelevant visual variation. In the task-relevant latent space, we train a history- and language-conditioned rectified-flow model to capture task dynamics and derive a directional dense reward from temporal changes in dynamics compatibility. Together, these components enable reward modeling directly over task-relevant dynamics rather than generic visual variation. DiTaR substantially improves policy learning on MetaWorld-v3 and ManiSkill over video-based reward baselines, and transfers to real-world offline RL through reward relabeling. Reward analyses further show that DiTaR provides more reliable rewards.

</details>

---

### [[20_Research/Papers/具身智能/Axiom-0_Hierarchical_Self-Refinement_for_Vision-Language-Action_Policies|Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies]]

![[assets/2610.14155_first_page.png|800]]

- **arXiv**: [2610.14155](https://arxiv.org/abs/2610.14155)
- **PDF**: https://arxiv.org/pdf/2610.14155
- **详细分析**: [[20_Research/Papers/具身智能/Axiom-0_Hierarchical_Self-Refinement_for_Vision-Language-Action_Policies|Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies]]
- **作者**: Renbin Shu, Jing Yang, Xiangyuan You, Guolin Qiu, Yufei Xia, Yiming Zhu, Nanjun Dai, Fei Zhang, Feng Wu, Keke Tang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.8，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Axiom-0: Hierarchical Self-Refinement for Vision-Language-Action Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable manipulation requires policies that generalize across tasks, layouts, and object interactions. Vision-language-action (VLA) models combine pretrained multimodal understanding with learned control, but their performance remains limited on unfamiliar task compositions. We present Axiom-0, a VLA policy that addresses both the quality of its representations and their use in action generation through hierarchical self-refinement. Intra-VLM Representation Refinement (IVRR) strengthens selected intermediate features through consistency supervision with learned feature projections during training. VLM-Action Interface Refinement (VAIR) recursively updates the resulting conditioning before action generation. Joint optimization of the supervised VLM layers, VAIR, and the action generator connects the two components. On RoboCasa365, Axiom-0 achieves 62.32% overall success in our evaluation, exceeding the highest published leaderboard score (Paimon-0, 58.1%) by 4.22 percentage points and the Xiaomi-Robotics-1 reference by 4.92 points. Under the evaluated profiling setup, mean action-chunk generation latency increases by 1.7% over Xiaomi-Robotics-1. These results demonstrate improved task completion with modest inference overhead.

</details>

---

### [[20_Research/Papers/大模型/SenseWeather_Multimodal_Sensing_for_Robust_Robotic_Perception_under_Extreme_Conditions|SenseWeather: Multimodal Sensing for Robust Robotic Perception under Extreme Conditions]]

![[assets/2610.14082_figure.png|800]]

- **arXiv**: [2610.14082](https://arxiv.org/abs/2610.14082)
- **PDF**: https://arxiv.org/pdf/2610.14082
- **详细分析**: [[20_Research/Papers/大模型/SenseWeather_Multimodal_Sensing_for_Robust_Robotic_Perception_under_Extreme_Conditions|SenseWeather: Multimodal Sensing for Robust Robotic Perception under Extreme Conditions]]
- **作者**: Fucai Ke, Sukai Huang, Junyi Hao, Kal Backman, Naim Rastgoo, Gholamreza Haffari, Hamid Rezatofighi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《SenseWeather: Multimodal Sensing for Robust Robotic Perception under Extreme Conditions》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AirSim, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic perception must remain reliable when extreme environmental conditions severely degrade the primary RGB observation. Although robotic platforms commonly carry complementary sensors such as depth and infrared, much of the modern perception stack remains RGB-centric, creating a mismatch between multimodal onboard sensing and pretrained downstream models. We study whether complementary sensing can be used upstream to recover a task-compatible RGB observation that preserves existing perception capabilities without modifying or retraining the downstream stack. To this end, we introduce SenseWeather, a controlled multimodal benchmark for robotic perception under severe rain, snow, dust, fog, and darkness, with registered RGB, depth, and infrared observations, clean references, and grounded high-level perception tasks. We further develop Fusion-to-RGB, with two parameter-efficient sensor-fusion realizations based on token-space fusion for a diffusion transformer and residual latent conditioning for an inpainting UNet. Across frozen open-vocabulary grounding and vision-language models, RGB+D+IR fusion improves all paired downstream comparisons over the corresponding RGB-only restorers, including AP50 gains across all ten detector comparisons. Importantly, these perception gains do not consistently follow conventional image-fidelity metrics, and increasing weather severity does not induce monotonic downstream degradation. These results show that complementary sensing can preserve reusable robotic perception under extreme conditions, while highlighting task-level perception robustness as an objective distinct from visual restoration quality.

</details>

---

### [[20_Research/Papers/具身智能/RAIN_Robotic_Task_Generalization_with_Region-Aware_Interaction_Networks|RAIN: Robotic Task Generalization with Region-Aware Interaction Networks]]

![[assets/2610.14039_figure.png|800]]

- **arXiv**: [2610.14039](https://arxiv.org/abs/2610.14039)
- **PDF**: https://arxiv.org/pdf/2610.14039
- **详细分析**: [[20_Research/Papers/具身智能/RAIN_Robotic_Task_Generalization_with_Region-Aware_Interaction_Networks|RAIN: Robotic Task Generalization with Region-Aware Interaction Networks]]
- **作者**: Seunghun Lee, Kyuhwan Shim, Yeogyeong Song, Seung Hwan Kim, Sihaeng Lee, Byoung-Tak Zhang, Sunghoon Im, Gunhee Lee
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.9，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《RAIN: Robotic Task Generalization with Region-Aware Interaction Networks》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing vision-language-action (VLA) models benefit from large-scale vision-language pretraining, but tend to memorize training trajectories, limiting their ability to adapt learned interactions to new task and scene configurations. To address this problem, we propose \textbf{Region-Aware Interaction Networks (RAIN)}, which formulates a task as a sequence of goal-conditioned subtasks, each specified by an action type and a target-region mask. This formulation allows learned skills to be reused across different objects and scene layouts and composed into task sequences not seen during training. Its Target-adaptive Cross-View Encoder (TCE) conditions multi-view features on target masks and exchanges information across views, while PlanDiT predicts target-directed trajectories and actions. A Transition Head estimates subtask completion to enable automatic transitions. We also introduce a \textbf{Reference-based Retargeting Strategy (RRS)}, which uses recorded trajectories to synthesize smooth approaches to reference interactions with alternative target regions, without collecting additional data. Experiments on \textbf{LIBERO-Analogy}, our new benchmark for robotic task generalization, and real-world tabletop tasks demonstrate that RAIN generalizes more robustly than existing VLA baselines.

</details>

---

### [[20_Research/Papers/具身智能/AERR-Nav_Adaptive_Exploration-Recovery-Reminiscing_Strategy_for_Zero-Shot_Object_Navigation|AERR-Nav: Adaptive Exploration-Recovery-Reminiscing Strategy for Zero-Shot Object Navigation]]

![[assets/2603.17712_figure.png|800]]

- **arXiv**: [2603.17712](https://arxiv.org/abs/2603.17712)
- **PDF**: https://arxiv.org/pdf/2603.17712
- **详细分析**: [[20_Research/Papers/具身智能/AERR-Nav_Adaptive_Exploration-Recovery-Reminiscing_Strategy_for_Zero-Shot_Object_Navigation|AERR-Nav: Adaptive Exploration-Recovery-Reminiscing Strategy for Zero-Shot Object Navigation]]
- **作者**: Jingzhi Huang, Junkai Huang, Haoyang Yang, Haoang Li, Yi Wang
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.5，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《AERR-Nav: Adaptive Exploration-Recovery-Reminiscing Strategy for Zero-Shot Object Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-Shot Object Navigation (ZSON) in unknown multi-floor environments presents a significant challenge. Recent methods, mostly based on semantic value greedy waypoint selection, spatial topology-enhanced memory, and Multimodal Large Language Model (MLLM) as a decision-making framework, have led to improvements. However, these architectures struggle to balance exploration and exploitation for ZSON when encountering unseen environments, especially in multi-floor settings, such as robots getting stuck at narrow intersections, endlessly wandering, or failing to find stair entrances. To overcome these challenges, we propose AERR-Nav, a Zero-Shot Object Navigation framework that dynamically adjusts its state based on the robot's environment. Specifically, AERR-Nav has the following two key advantages: (1) An Adaptive Exploration-Recovery-Reminiscing Strategy, enables robots to dynamically transition between three states, facilitating specialized responses to diverse navigation scenarios. (2) An Adaptive Exploration State featuring Fast and Slow-Thinking modes helps robots better balance exploration, exploitation, and higher-level reasoning based on evolving environmental information. Extensive experiments on the HM3D and MP3D benchmarks demonstrate that our AERR-Nav achieves state-of-the-art performance among zero-shot methods. Comprehensive ablation studies further validate the efficacy of our proposed strategy and modules.

</details>

---
