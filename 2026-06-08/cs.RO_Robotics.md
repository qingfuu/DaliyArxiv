# cs.RO | Robotics | 2026-06-08

#arxiv #ComputerScience

**论文数**: 22

### [[20_Research/Papers/具身智能/Affordance-Based_Hierarchical_Reinforcement_Learning_for_Quadruped_Pedipulation|Affordance-Based Hierarchical Reinforcement Learning for Quadruped Pedipulation]]

![[assets/2606.07506_figure.png|800]]

- **arXiv**: [2606.07506](https://arxiv.org/abs/2606.07506)
- **PDF**: https://arxiv.org/pdf/2606.07506
- **详细分析**: [[20_Research/Papers/具身智能/Affordance-Based_Hierarchical_Reinforcement_Learning_for_Quadruped_Pedipulation|Affordance-Based Hierarchical Reinforcement Learning for Quadruped Pedipulation]]
- **作者**: Tuba Girgin, Jose Castelblanco, Gabriel Rodriguez, Emre Girgin, Cagri Kilic
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.9（加权：具身智能 1.8，强化学习 0.8，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Affordance-Based Hierarchical Reinforcement Learning for Quadruped Pedipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IsaacSim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The object manipulation capabilities of quadruped robots is an open research challenge. While previous studies have focused on low-level policy learning, task execution still relies on expert-designed high-level trajectories. Autonomous selection of both an affordable interaction point on the target object and an affordable robot base pose removes the need for pre-designed trajectories. This study proposes a three-level hierarchical reinforcement learning (RL) framework that utilizes pose affordances to guide the navigation policy, while the navigation policy drives the locomotion policy. In addition, the pedipulation policy is guided by interaction-point affordances, enabling object-centric pose alignment of the quadruped robot and effective end-effector manipulation planning. We train the proposed framework in the IsaacSim ecosystem and evaluate it in both simulation and real-world settings. We investigate the effectiveness of pose affordance across multiple scenarios in simulation while various object interaction tasks are validated on real-world setting forming an object-interaction dataset. The results show that the proposed framework can autonomously identify candidate poses based on their affordance and successfully execute object manipulation tasks in the real world without human guidance.

</details>

---

### [[20_Research/Papers/具身智能/Rapid_co-design_of_Buoyancy-assisted_robots_for_Challenging_Locomotion_using_Gaussian_Evolutionary_Specialists|Rapid co-design of Buoyancy-assisted robots for Challenging Locomotion using Gaussian Evolutionary Specialists]]

![[assets/2606.07424_figure.png|800]]

- **arXiv**: [2606.07424](https://arxiv.org/abs/2606.07424)
- **PDF**: https://arxiv.org/pdf/2606.07424
- **详细分析**: [[20_Research/Papers/具身智能/Rapid_co-design_of_Buoyancy-assisted_robots_for_Challenging_Locomotion_using_Gaussian_Evolutionary_Specialists|Rapid co-design of Buoyancy-assisted robots for Challenging Locomotion using Gaussian Evolutionary Specialists]]
- **作者**: Ankit Sinha, Nitish Sontakke, Dennis Hong, Yusuke Tanaka, Sehoon Ha
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.9（加权：具身智能 1.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Rapid co-design of Buoyancy-assisted robots for Challenging Locomotion using Gaussian Evolutionary Specialists》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing high-performance legged robots requires jointly optimizing morphology and control. Model-free Reinforcement Learning (RL) offers an alternative to model-predictive control for developing robust controllers without explicitly specifying robot dynamics. Thus, we have seen theuse of RL to train controllers and evaluate designs for robot morphology optimization. While RL has shown success inlocomotion, using it in the co-design inner loop is expensive due to repeated policy training. Universal policies conditioned on morphology offer a promising alternative, but suffer from behavioral diversity collapse, converging to a single strategy that performs sub-optimally across designs. On the other hand, end-to-end Mixture-of-Experts (MoE) architectures fail due to a collapse in its representation. We propose Gaussian Evolutionary Specialists (GES), a framework that decouples design-space partitioning from policy learning to capture diverse behaviors explicitly. GES assigns specialist policies to evolving Gaussian regions and iteratively refines them via training, probing, and territory expansion. The resulting specialists are integrated into a design sampling loop, replacing costly re-training with direct evaluation. When tested on the Buoyancy-Assisted Light Legged Unit (BALLU), GES discovers designs with 5 - 25% higher performance than naive universal policies. On hardware, a GES optimized design overcomes a 24 cm tall obstacle - 3x improvement over the baseline BALLU design. Moreover, GES curtails design optimization time by 37%.

</details>

---

### [[20_Research/Papers/具身智能/Simulation-Driven_Imitation_Learning_for_Biosignals-Free_Shared-Autonomy_Prosthetic_Grasping|Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping]]

![[assets/2606.07389_figure.png|800]]

- **arXiv**: [2606.07389](https://arxiv.org/abs/2606.07389)
- **PDF**: https://arxiv.org/pdf/2606.07389
- **详细分析**: [[20_Research/Papers/具身智能/Simulation-Driven_Imitation_Learning_for_Biosignals-Free_Shared-Autonomy_Prosthetic_Grasping|Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping]]
- **作者**: Kaijie Shi, Wanglong Lu, Huiling Chen, Vinicius Prado da Fonseca, Ting Zou, Hanli Zhao, Xianta Jiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Simulation-Driven Imitation Learning for Biosignals-Free Shared-Autonomy Prosthetic Grasping》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biosignals-free shared-autonomy control of upper-limb prosthetic hands aims to enable natural and low-effort manipulation without relying on EMG or other physiological signals. Recent imitation-learning-based approaches have shown promising results, but their scalability is limited by the cost and variability of collecting large amounts of real-world human demonstration data. In this work, we present a scalable simulation framework that automatically generates diverse reach-to-grasp demonstrations from a wrist-mounted virtual camera. The framework combines physically feasible grasp synthesis, natural reaching trajectories retargeting, and reach--grasp--lift execution in procedurally generated indoor environments. It records wrist-view observations, proprioception, and actions to build a large-scale demonstration dataset for imitation learning. Through extensive simulation benchmarks, we evaluate object and scene generalization and compare several representative state-of-the-art imitation learning methods. Results show that the simulated demonstrations are sufficiently rich and consistent for effective policy learning. In three realistic settings, the learned sim-to-real policy achieves over 90\% grasp success, surpasses baseline methods, and exhibits stronger generalization, highlighting the promise of simulation-driven training for biosignals-free shared-autonomy prosthetic grasping. The demonstrations are available at \href{https://sites.google.com/view/sim-prosthetic-grasp/home}{https://sites.google.com/view/sim-prosthetic-grasp/home}.

</details>

---

### [[20_Research/Papers/具身智能/Spline_Policy_A_Structured_Representation_for_Robot_Policies|Spline Policy: A Structured Representation for Robot Policies]]

![[assets/2606.07386_figure.jpg|800]]

- **arXiv**: [2606.07386](https://arxiv.org/abs/2606.07386)
- **PDF**: https://arxiv.org/pdf/2606.07386
- **详细分析**: [[20_Research/Papers/具身智能/Spline_Policy_A_Structured_Representation_for_Robot_Policies|Spline Policy: A Structured Representation for Robot Policies]]
- **作者**: Mengze Tian, Yiming Li, Sichao Liu, Auke Ijspeert, Sylvain Calinon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Spline Policy: A Structured Representation for Robot Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern imitation-learning policies for robot manipulation often represent actions as fixed-resolution action chunks, which are simple and effective but expose limited geometric and temporal structure before execution. This paper studies Spline Policy (SP), a structured representation that replaces action chunks with spline parameters while keeping the policy backbone unchanged. The predicted spline can be decoded as a compact continuous trajectory, queried at different temporal resolutions, constrained or edited in parameter space, and passed to downstream controllers. For quadratic spline outputs, the same representation can also be converted into a state-dependent vector field through an analytical distance-field construction. Under the regularity and projection assumptions of this construction, the induced dynamics do not increase the distance to the generated spline, yielding a principled local corrective mechanism around the predicted motion. The spline output further supports uncertainty propagation from observations to spline parameters, trajectories, and flow fields, and can be combined with classical control mechanisms such as null-space collision avoidance without retraining the policy backbone. We instantiate SP with diffusion, flow-matching, transformer-based, and vision-language-action backbones. Experiments in low-dimensional motion learning, simulated manipulation under matched backbones, dexterous manipulation, and real-robot case studies show that SP remains compatible with modern policy learners while exposing useful motion-structure properties, including compact decoding, temporal resampling, local correction around predicted motions, uncertainty evaluation, and controller compatibility.

</details>

---

### [[20_Research/Papers/具身智能/CAPE_Contrastive_Action-conditioned_Parallel_Encoding_for_Embodied_Planning|CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning]]

![[assets/2606.07304_figure.png|800]]

- **arXiv**: [2606.07304](https://arxiv.org/abs/2606.07304)
- **PDF**: https://arxiv.org/pdf/2606.07304
- **详细分析**: [[20_Research/Papers/具身智能/CAPE_Contrastive_Action-conditioned_Parallel_Encoding_for_Embodied_Planning|CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning]]
- **作者**: Cong Chen, Haowen Wang, Zhixiang Zhang, Pei Ren, Zhengping Che
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《CAPE: Contrastive Action-conditioned Parallel Encoding for Embodied Planning》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PlaNet, RoboNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents need to predict the future consequences of candidate actions in order to plan effectively before execution. Existing visual dynamics models learn by reconstructing future visual states or rolling out dense latent representations, which spreads learning capacity across visually salient but planning-irrelevant content rather than the action-conditioned changes that drive manipulation outcomes. We propose CAPE, a Contrastive Action-conditioned Parallel Encoding framework that learns visual dynamics by distinguishing the future outcomes induced by different action sequences. Given an initial observation and a candidate action sequence, CAPE decodes the full future latent trajectory in a single forward pass and is trained with a Goal-Convergent Contrastive Objective that aligns predictions corresponding to the same future outcome while separating those corresponding to different outcomes. On real-world DROID and zero-shot transfer to RoboCasa, CAPE substantially outperforms prior baselines on future-state retrieval, offline action matching, and closed-loop planning, while notably reducing planning-time inference cost at long prediction horizons.

</details>

---

### [[20_Research/Papers/具身智能/Shield-Loco_Shielding_Locomotion_Policies_with_Predictive_Safety_Filtering|Shield-Loco: Shielding Locomotion Policies with Predictive Safety Filtering]]

![[assets/2606.07193_figure.png|800]]

- **arXiv**: [2606.07193](https://arxiv.org/abs/2606.07193)
- **PDF**: https://arxiv.org/pdf/2606.07193
- **详细分析**: [[20_Research/Papers/具身智能/Shield-Loco_Shielding_Locomotion_Policies_with_Predictive_Safety_Filtering|Shield-Loco: Shielding Locomotion Policies with Predictive Safety Filtering]]
- **作者**: Aditya Shirwatkar, Sebastian Sanokowski, Shishir Kolathaya, Aaron Johnson, Majid Khadiv
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.7（加权：具身智能 1.8，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Shield-Loco: Shielding Locomotion Policies with Predictive Safety Filtering》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) policies enable dynamic legged locomotion but lack mechanisms to avoid violations of safety constraints that are absent during training. Large-scale offline safe learning is impractical for covering all edge cases. Existing safety frameworks either rely on reduced-order models that cannot reason about whole-body behaviors or require conservative recovery controllers that degrade task performance. We propose a predictive safety filter that post-hoc filters the nominal contact locations fed to the RL policy. When a collision is predicted, a sampling-based optimizer asynchronously searches for safer contact sequences using a full-physics model, while a learned value function bootstraps long-horizon returns. Our three algorithmic components (geometric projection of sampled contacts, momentum-augmented updates, and replica-exchange) make the optimization tractable in a discontinuous contact landscape. We validate the filter on a quadruped robot in dense, cluttered environments, both in simulation and in the real world, showing substantial reductions in safety violations with minimal deviation from the nominal input.

</details>

---

### [[20_Research/Papers/具身智能/QuadVerse_An_Integrated_Framework_Aligning_Visual-Physical_Reality_for_Quadruped_Simulation|QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation]]

![[assets/2606.07118_figure.png|800]]

- **arXiv**: [2606.07118](https://arxiv.org/abs/2606.07118)
- **PDF**: https://arxiv.org/pdf/2606.07118
- **详细分析**: [[20_Research/Papers/具身智能/QuadVerse_An_Integrated_Framework_Aligning_Visual-Physical_Reality_for_Quadruped_Simulation|QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation]]
- **作者**: Yuxiang Chen, Yuanhao Wang, Ziheng Zhang, Meng Zhang, Yu Liu, Yufei Jia, Tiancai Wang, Erjin Zhou, Jin Xie
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《QuadVerse: An Integrated Framework Aligning Visual-Physical Reality for Quadruped Simulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Real-to-Sim, Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation is central to robot learning, yet the sim-to-real gap remains a major bottleneck.Existing approaches often tackle visual or dynamic gaps separately, overlooking how these individual mismatches accumulate and propagate throughout the robot's state evolution.In this paper, we introduce QuadVerse, an integrated framework that uses reconstructed scenes as a calibration substrate for aligning visual perception, physical interaction, and actuator dynamics.From captured RGB videos, we reconstruct geometry-constrained 3D Gaussian Splatting (3DGS) scenes that support batched photorealistic ego-view rendering and collision-ready semantic mesh extraction. The meshes further enable contact calibration by initializing spatially varying friction priors and refining them through trajectory-based posterior search.To address remaining actuator discrepancies, QuadVerse trains a residual dynamics compensator by replaying real-world trajectories on the contact-calibrated terrain, reducing the entanglement between terrain-induced contact errors and actuator non-idealities.Experiments show that QuadVerse improves reconstruction quality and locomotion tracking over relevant baselines.Leveraging this foundation, we demonstrate robust zero-shot visual-navigation policy deployment without task-specific real-world rollouts.

</details>

---

### [[20_Research/Papers/具身智能/Coarse-to-Control_Action-Token_Planning_for_Vision-Language-Action_Models|Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models]]

![[assets/2606.07107_figure.png|800]]

- **arXiv**: [2606.07107](https://arxiv.org/abs/2606.07107)
- **PDF**: https://arxiv.org/pdf/2606.07107
- **详细分析**: [[20_Research/Papers/具身智能/Coarse-to-Control_Action-Token_Planning_for_Vision-Language-Action_Models|Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models]]
- **作者**: Jinhao Wu, Shiduo Zhang, Yicheng Liu, Xiaopeng Yu, Sixian Li, Siyin Wang, Hang Zhao, Jing Huo, Yang Gao, Jingjing Gong, Xipeng Qiu, Yu-Gang Jiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Coarse-to-Control: Action-Token Planning for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DreamVLA, OpenVLA, Real-World, SmolVLA, UD-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most vision-language-action (VLA) models map observations directly to actions without explicit intermediate planning, which limits performance on long-horizon tasks where early mistakes compound. We propose Coarse-to-Control, a plan-execute VLA that introduces planning natively in the action-token space. The key idea is to let the policy first predict a compact sequence of coarse action tokens that summarize the intended future trajectory, and then generate executable action tokens conditioned on this plan. Because both planning and execution share a unified discrete action vocabulary, the plan stays close to the control manifold and provides directly actionable guidance rather than an abstract hint that must be translated back to motor commands. Experiments on LIBERO, SimplerEnv-WidowX, and real-world manipulation tasks show that action-token planning consistently improves over direct action generation, with the largest gains on long-horizon multi-stage tasks.

</details>

---

### [[20_Research/Papers/具身智能/Dreaming_when_Necessary_Advancing_World_Action_Models_with_Adaptive_Multi-Modal_Reasoning|Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning]]

![[assets/2606.07089_figure.png|800]]

- **arXiv**: [2606.07089](https://arxiv.org/abs/2606.07089)
- **PDF**: https://arxiv.org/pdf/2606.07089
- **详细分析**: [[20_Research/Papers/具身智能/Dreaming_when_Necessary_Advancing_World_Action_Models_with_Adaptive_Multi-Modal_Reasoning|Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning]]
- **作者**: Yinzhou Tang, Jingbo Xu, Yu Shang, Zihao Song, Chen Gao, Wei Wu, Yong Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Dreaming when Necessary: Advancing World Action Models with Adaptive Multi-Modal Reasoning》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) offer a promising approach to embodied intelligence, yet existing methods rely heavily on video prediction as action priors and lack adaptive multimodal reasoning, limiting their effectiveness on long-horizon, complex tasks. We observe that WAMs require different multimodal reasoning modes under different execution contexts: textual reasoning is essential during task transitions to guide high-level action prediction, while visual reasoning is critical during fine-grained manipulation for precise control. Motivated by this observation, we propose \textbf{AdaWAM}, a world action model with adaptive multimodal reasoning abilities. AdaWAM integrates a lightweight dynamic router that autonomously triggers textual or visual reasoning as needed during task execution. Experiments on both simulated and real-world embodied tasks show that AdaWAM substantially improves inference efficiency while outperforming state-of-the-art embodied policies. Codes and demos are available at: https://adawam.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Predictive_Style_Matching_Natural_and_Robust_Humanoid_Locomotion|Predictive Style Matching: Natural and Robust Humanoid Locomotion]]

![[assets/2606.07083_figure.png|800]]

- **arXiv**: [2606.07083](https://arxiv.org/abs/2606.07083)
- **PDF**: https://arxiv.org/pdf/2606.07083
- **详细分析**: [[20_Research/Papers/具身智能/Predictive_Style_Matching_Natural_and_Robust_Humanoid_Locomotion|Predictive Style Matching: Natural and Robust Humanoid Locomotion]]
- **作者**: Simeon Nedelchev, Ekaterina Chaikovskaia, Egor Davydenko, Eduard Zaliaev, Roman Gorbachev
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.2（加权：具身智能 2.7，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Predictive Style Matching: Natural and Robust Humanoid Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has become the prevailing approach to humanoid locomotion control: policies transfer reliably from simulation to hardware and recover gracefully from disturbances. Motion quality, however, still lags behind: task-only rewards often converge to stiff, asymmetric gaits, while motion imitation methods improve appearance but become more sensitive to external disturbances because reference signals can oppose the transient poses needed to regain balance. We propose Predictive Style Matching, in which an offline predictor maps the robot's lower-body state history and velocity commands to interpretable upper-body joint and gait targets that shape the rewards during training. Because the targets are state-conditioned rather than time-indexed and the predictor is used only at training time, the deployed controller inherits the proprioceptive interface and inference cost of a task-only RL baseline. On the Unitree G1, in both simulation and hardware, PSM reduces upper-body style error by roughly an order of magnitude over task-only RL while preserving its fall-recovery rate, whereas the motion-imitation baseline attains the lowest style error but fails to recover from disturbances about five times as often.

</details>

---

### [[20_Research/Papers/具身智能/Task_Editing_for_Generalizable_3D_Visuomotor_Policy_Learning|Task Editing for Generalizable 3D Visuomotor Policy Learning]]

![[assets/2606.07012_figure.png|800]]

- **arXiv**: [2606.07012](https://arxiv.org/abs/2606.07012)
- **PDF**: https://arxiv.org/pdf/2606.07012
- **详细分析**: [[20_Research/Papers/具身智能/Task_Editing_for_Generalizable_3D_Visuomotor_Policy_Learning|Task Editing for Generalizable 3D Visuomotor Policy Learning]]
- **作者**: Jian-Jian Jiang, YiHan Yang, Lan Wei, Yuming Luo, Xiao-Ming Wu, Xuhang Chen, Bin Fan, Dandan Zhang, Wei-Shi Zheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Task Editing for Generalizable 3D Visuomotor Policy Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PointNet, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3D visuomotor policies offer a promising direction for complex robotic manipulation, as depth maps and point clouds provide rich geometric information for spatial reasoning. However, their success often depends on large-scale real-world demonstrations, which are costly and time-consuming to collect. To this end, existing methods commonly use demonstration generation strategies to improve data efficiency by applying object-centric transformations to human-collected demonstrations, such as varying object poses or scales. While effective for local variation, these transformations largely preserve the original scene structure and skill sequence, limiting their ability to synthesize diverse scene-skill-object combinations for complex tasks. In this paper, we propose Task-Edit, a novel demonstration generation framework that generates diverse trajectories from a task-centric editing perspective. The key insight of Task-Edit is to decompose a task into scene, skill and object components, and flexibly recombine them. In this way, Task-Edit enables scalable demonstration generation and significantly improves generalization for long-horizon manipulation tasks. We evaluate Task-Edit through extensive real-world experiments and demonstrate three advantages: (1) Effectiveness: Task-Edit significantly improves 3D visuomotor policies across various real-world tasks and robot embodiments. (2) Generalizability: Task-Edit improves model generalization across different scenario setups. (3) Applicability: Task-Edit enables models to handle scenarios that are difficult to collect in the real world, including disturbance resistance, obstacle avoidance and unseen cluttered scenes.

</details>

---

### [[20_Research/Papers/机器人/Compliance-Based_Sensor_Placement_for_Force_Sensing_on_a_Sensorized_Prostate_Phantom|Compliance-Based Sensor Placement for Force Sensing on a Sensorized Prostate Phantom]]

![[assets/2606.06977_figure.png|800]]

- **arXiv**: [2606.06977](https://arxiv.org/abs/2606.06977)
- **PDF**: https://arxiv.org/pdf/2606.06977
- **详细分析**: [[20_Research/Papers/机器人/Compliance-Based_Sensor_Placement_for_Force_Sensing_on_a_Sensorized_Prostate_Phantom|Compliance-Based Sensor Placement for Force Sensing on a Sensorized Prostate Phantom]]
- **作者**: Sizhe Tian, Yinoussa Adagolodjo, Jeremie Dequidt
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Compliance-Based Sensor Placement for Force Sensing on a Sensorized Prostate Phantom》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work presents a compliance-based sensor placement method for force sensing on a sensorized prostate phantom designed for Digital Rectal Examination training. The phantom combines three internal pneumatic chambers, used as intrinsic pressure sensors, with ten surface displacement markers. A finite-element simulation dataset is generated by applying external forces at sampled surface locations, from which a compliance matrix relating force inputs to pressure and displacement responses is constructed. Based on this matrix, we propose a weighted greedy selection strategy that maximizes local force reconstructability while prioritizing the clinically relevant posterior contact region and avoiding marker placement directly within the Region of Interest. Compared with a global QR-based placement strategy, the proposed method increases the mean reconstructability score in the target region by 22.5%. These results suggest that region-aware sparse sensor placement can improve force observability in soft robotic medical phantoms while maintaining a limited and practical sensing configuration.

</details>

---

### [[20_Research/Papers/机器人/LIMMT_Less_is_More_for_Motion_Tracking|LIMMT: Less is More for Motion Tracking]]

![[assets/2606.06953_figure.png|800]]

- **arXiv**: [2606.06953](https://arxiv.org/abs/2606.06953)
- **PDF**: https://arxiv.org/pdf/2606.06953
- **详细分析**: [[20_Research/Papers/机器人/LIMMT_Less_is_More_for_Motion_Tracking|LIMMT: Less is More for Motion Tracking]]
- **作者**: Yu Guan, Zekun Qi, Chenghuai Lin, Xuchuan Chen, Dairu Liu, Wenyao Zhang, Jilong Wang, Xinqiang Yu, He Wang, Li Yi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: cs.RO

#### 研究背景与动机

《LIMMT: Less is More for Motion Tracking》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We argue that high-quality motion data can steer tracking policies toward better optimization trajectories early in training. In this work, we introduce LIMMT (Less Is More for Motion Tracking). To our knowledge, this is the first data-centric study for physics-based humanoid motion tracking. We go beyond simply removing low-quality and erroneous clips, but define motion data quality through three dimensions: physics feasibility, diversity, and complexity. We show that even training with under 3% of AMASS yields better tracking performance than training with the full dataset. We further conduct data cleaning on the estimated web-sourced mocap data. Extensive experiments and analyses validate the effectiveness of our framework.

</details>

---

### [[20_Research/Papers/具身智能/T-GMP_Terrain-conditioned_Generative_Motion_Priors_for_Versatile_and_Natural_Humanoid_Locomotion|T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion]]

![[assets/2606.06944_figure.png|800]]

- **arXiv**: [2606.06944](https://arxiv.org/abs/2606.06944)
- **PDF**: https://arxiv.org/pdf/2606.06944
- **详细分析**: [[20_Research/Papers/具身智能/T-GMP_Terrain-conditioned_Generative_Motion_Priors_for_Versatile_and_Natural_Humanoid_Locomotion|T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion]]
- **作者**: Junhong Guo, Hao Hu, Chen Chen, Haoxuan Han, Linao Gong, Xin Yang, Zhicheng He, Yao Su, Fenghua He
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.0（加权：具身智能 2.7，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Security

#### 研究背景与动机

《T-GMP: Terrain-conditioned Generative Motion Priors for Versatile and Natural Humanoid Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving both anthropomorphic naturalness and robust terrain traversal remains a fundamental challenge in humanoid locomotion. Existing Reinforcement Learning (RL) approaches typically rely on fixed motion priors, limiting their adaptability to varying environments. We propose Terrain-conditioned Generative Motion Priors (T-GMP), a module that captures a terrain-conditioned latent motion manifold from a few expert state-terrain demonstrations using a Conditional Variational Autoencoder (CVAE). The learned priors enable smooth style transitions, facilitating a unified policy that adapts to terrain variations. We integrate T-GMP into an adversarial learning pipeline with our proposed Foothold Penalty, where a discriminator dynamically modulates naturalness constraints conditioned on local terrain features, guiding the generation of versatile and human-like motions. Experimental results demonstrate that our method outperforms existing baselines in traversal success rate and motion smoothness, while preserving biomimetically natural and physically coordinated motions.

</details>

---

### [[20_Research/Papers/机器人/What_Is_My_Robot_Thinking_Design_Considerations_for_Transparent_and_Trustworthy_Shared_Autonomy|What Is My Robot Thinking? Design Considerations for Transparent and Trustworthy Shared Autonomy]]

![[assets/2606.06870_figure.png|800]]

- **arXiv**: [2606.06870](https://arxiv.org/abs/2606.06870)
- **PDF**: https://arxiv.org/pdf/2606.06870
- **详细分析**: [[20_Research/Papers/机器人/What_Is_My_Robot_Thinking_Design_Considerations_for_Transparent_and_Trustworthy_Shared_Autonomy|What Is My Robot Thinking? Design Considerations for Transparent and Trustworthy Shared Autonomy]]
- **作者**: Atharv Belsare, Zohre Karimi, Connor Mattson, Rushiil Nakka, Daniel S. Brown
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《What Is My Robot Thinking? Design Considerations for Transparent and Trustworthy Shared Autonomy》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assistive robots operating under shared autonomy must balance user control with autonomous assistance. Because robot actions depend on internal intent inference that is not directly observable, mismatches between inferred and intended goals can undermine coordination and trust. We investigate how interface-level transparency, including feedback modality (visual vs. auditory) and information richness (sparse vs. rich), shapes interaction in a vision-based shared autonomy system. In a user study with N=25 participants across two assistive manipulation tasks, we evaluate how these designs influence coordination and trust. Providing feedback significantly improves intent alignment and reduces corrective intervention, indicating that making the inferred goal legible accelerates convergence in shared control. Participants preferred visual over auditory feedback, while preferences for sparse versus rich information depended on task complexity. We also found that revealing the full belief distribution did not consistently improve alignment or trust. Together, these findings indicate that effective transparency enhances coordination primarily through goal legibility, while trust depends on task-appropriate information exposure rather than maximal disclosure. Based on these results, we outline guidelines for designing transparent shared autonomy systems.

</details>

---

### [[20_Research/Papers/世界模型/STRIPS-WM_Learning_Grounded_Propositional_STRIPS-style_World_Models_from_Images|STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images]]

![[assets/2606.06832_figure.png|800]]

- **arXiv**: [2606.06832](https://arxiv.org/abs/2606.06832)
- **PDF**: https://arxiv.org/pdf/2606.06832
- **详细分析**: [[20_Research/Papers/世界模型/STRIPS-WM_Learning_Grounded_Propositional_STRIPS-style_World_Models_from_Images|STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images]]
- **作者**: Abhiroop Ajith, Constantinos Chamzas
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，世界模型 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《STRIPS-WM: Learning Grounded Propositional STRIPS-style World Models from Images》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots performing long-horizon visual manipulation observe high-dimensional images, but successful plans depend on action-relevant facts: what can be done now and what changes afterward. A useful planning representation should discard irrelevant visual details while preserving action applicability and effects. Classical task planners exploit this structure through symbolic operators with preconditions and effects, but obtaining such representations from raw visual experience remains challenging. We study a visual task-planning setting in which a robot receives only image transitions: the current image, executed high-level action, and the resulting image. At test time, given a start image and a goal image, the robot must produce a sequence of high-level actions that reaches the goal. To address this problem, we introduce STRIPS-WM, a framework for learning image-grounded STRIPS-style world models directly from visual transitions. STRIPS-WM first induces a finite abstract transition graph from images, then learns latent binary predicates and one grounded propositional operator per action label. The learned operators form a symbolic action model with sparse preconditions and add/delete effects. Finally, the learned predicates are distilled into a visual encoder, enabling classical planning directly from novel start and goal images. Experiments on visual rearrangement tasks show that STRIPS-WM improves image-to-plan success over the tested visual rollout, latent graph-search and latent-symbolic baselines.

</details>

---

### [[20_Research/Papers/具身智能/Three-dimensional_hydro-cluttered_locomotion_by_an_undulatory_robot|Three-dimensional hydro-cluttered locomotion by an undulatory robot]]

![[assets/2606.06829_figure.png|800]]

- **arXiv**: [2606.06829](https://arxiv.org/abs/2606.06829)
- **PDF**: https://arxiv.org/pdf/2606.06829
- **详细分析**: [[20_Research/Papers/具身智能/Three-dimensional_hydro-cluttered_locomotion_by_an_undulatory_robot|Three-dimensional hydro-cluttered locomotion by an undulatory robot]]
- **作者**: Tianyu Wang, Matthew Fernandez, Galen Tunnicliffe, Nikolas Cornell, Justin Duong, Donoven Dortilus, Zhaochen J. Xu, Patricia Meza, Sean Lublinsky, Darsh Parikh, Jianfeng Lin, Emily Grace...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Three-dimensional hydro-cluttered locomotion by an undulatory robot》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aquatic robots have expanded human access to underwater environments, yet many underwater spaces contain obstacles that can disrupt open-water locomotion. In "hydro-cluttered" environments, water is interspersed with rigid and flexible clutter, making body-obstacle contact unavoidable. Operating in these spaces requires robots that can regulate and exploit contact, but this regime remains difficult to model or simulate. Building on recent advances in mechanical intelligence in terradynamically capable limbless robotics, we develop principles for 3D aquatic locomotion using AquaMILR, an elongate limbless robot that combines bilateral cable-driven actuation, programmable body compliance, distributed depth regulation, corrosion-resistant enclosures, and onboard power and electronics for untethered field operation. Systematic robophysical experiments reveal that programmable body compliance regulates body deformation and converts body-environment interactions into fast, robust, forward progression across increasing hydro-clutter constraint strength. Depth regulation provides three-dimensional access, allowing the robot to bypass clutter, recover from obstruction, and continue through otherwise inaccessible routes. In potential jamming scenarios, emergent inertia-induced rolling acts as a spontaneous recovery mechanism, freeing the robot from clutter that would otherwise lead to failure and allowing locomotion to continue without additional control. Tests of the robot in an aquatic mangrove field demonstrate that these principles transfer to practical operation, enabling navigation and onboard visual inspection of inaccessible root zones. These results establish principles for hydro-cluttered locomotion and a design paradigm in which aquatic robots exploit environmental complexity as a locomotor resource.

</details>

---

### [[20_Research/Papers/具身智能/Multi-Robot_Planning_and_Control_from_CCTV_Camera_Networks_in_a_Real_Warehouse|Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse]]

![[assets/2606.06762_figure.png|800]]

- **arXiv**: [2606.06762](https://arxiv.org/abs/2606.06762)
- **PDF**: https://arxiv.org/pdf/2606.06762
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Robot_Planning_and_Control_from_CCTV_Camera_Networks_in_a_Real_Warehouse|Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse]]
- **作者**: Luke Robinson, Benjamin Ramtoula, Anas Izaaryene, Paul Newman, Daniele De Martini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Multi-Robot Planning and Control from CCTV Camera Networks in a Real Warehouse》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Off-board control of mobile robots from cameras embedded in the environment offers a practical path to scalable autonomy, moving sensing and compute off the robots. We extend this idea from the single-robot case to coordinated fleets in a real warehouse, driving multiple robots with only a distributed CCTV network and edge compute. The system operates entirely in image space over an uncalibrated, pixel-wise topological camera graph, enabling wide-area operation with flexible camera placement. A hierarchical planner selects a camera sequence per robot and plans its image-space motion through each view, coordinating robots with a prioritised-then-joint strategy and treating overlapping camera regions as shared resources held by one robot at a time to prevent collisions and deadlocks. We validate the approach in a real warehouse with four robots and 30 cameras across six 27 m aisles, reporting mission times and coordination statistics. To our knowledge, this is the first field demonstration of multi-robot planning and coordination using only an external camera network and off-board compute, with robots carrying no task-specific navigation hardware.

</details>

---

### [[20_Research/Papers/机器人/IDDMBSE_Integrating_Data-Driven_and_Model-Based_Systems_Engineering_for_Trusted_Autonomous_Cyber-Physical_Systems|IDDMBSE: Integrating Data-Driven and Model-Based Systems Engineering for Trusted Autonomous Cyber-Physical Systems]]

![[assets/2606.06727_figure.png|800]]

- **arXiv**: [2606.06727](https://arxiv.org/abs/2606.06727)
- **PDF**: https://arxiv.org/pdf/2606.06727
- **详细分析**: [[20_Research/Papers/机器人/IDDMBSE_Integrating_Data-Driven_and_Model-Based_Systems_Engineering_for_Trusted_Autonomous_Cyber-Physical_Systems|IDDMBSE: Integrating Data-Driven and Model-Based Systems Engineering for Trusted Autonomous Cyber-Physical Systems]]
- **作者**: John S. Baras, Sai Sandeep Damera, Ryan Matheu, Clinton Enwerem, Praveen M. S. Kumar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《IDDMBSE: Integrating Data-Driven and Model-Based Systems Engineering for Trusted Autonomous Cyber-Physical Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous cyber-physical systems (CPS) sit at the intersection of Model-Based Systems Engineering (MBSE) and data-driven Machine Learning and Artificial Intelligence (ML/AI), yet no integrated Systems Engineering (SE) methodology natively spans both. We address this gap with IDDMBSE, an Integrated Data-Driven and Model-Based Systems Engineering methodology that extends the rigorous MBSE V-process with a data-driven loop at every step, anchored in SysML, the autonomy stack, and a hybrid model-based plus data-driven trade-off architecture. We instantiate IDDMBSE as an interoperable, open-source tool chain: PERFECT, which maps SysML system architectures to executable ROS autonomy stacks for scalable performance evaluation; TRADES-X, which decomposes design-space exploration into a model-based optimization stage followed by a data-driven evaluation stage; and VERITAS, which combines formal, data-driven, and runtime verification into a single assurance workflow. We demonstrate IDDMBSE on a Trusted Autonomous Ground Robot across its development lifecycle, spanning sensor-suite selection, risk-sensitive path planning, behavior-tree task verification, conformal-prediction-based robust perception, and assured multi-robot coordination, all exercised in a contested-terrain Isaac Sim test range that we release with the tool chain. We close by sketching how IDDMBSE is being re-formulated on SysML v2 / KerML foundations to enable language-native composability and tighter ML/AI integration.

</details>

---

### [[20_Research/Papers/机器人/Optimal_Control_Approach_for_Non-prehensile_Ball_Juggling_Using_a_7-DoF_Manipulator|Optimal Control Approach for Non-prehensile Ball Juggling Using a 7-DoF Manipulator]]

![[assets/2606.06704_figure.png|800]]

- **arXiv**: [2606.06704](https://arxiv.org/abs/2606.06704)
- **PDF**: https://arxiv.org/pdf/2606.06704
- **详细分析**: [[20_Research/Papers/机器人/Optimal_Control_Approach_for_Non-prehensile_Ball_Juggling_Using_a_7-DoF_Manipulator|Optimal Control Approach for Non-prehensile Ball Juggling Using a 7-DoF Manipulator]]
- **作者**: Joel Ramadani, Vasilije Rakčević, Riddhiman Laha, Arne Sachtler, Valentin Le Mesle, Achim J. Lilienthal, Sami Haddadin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Optimal Control Approach for Non-prehensile Ball Juggling Using a 7-DoF Manipulator》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Non-prehensile object manipulation skills are important for real-world robot interactions, enabling highly dynamic tasks such as balancing a glass on a tray or the controlled sliding of items on a table. Among such tasks, those characterised by high-speed manipulation requirements and general sensitivity of the resulting hybrid dynamics are particularly hard to accomplish. Within these, juggling can be seen as a highly challenging maneuver to be solved. The key to robotic juggling is achieving dynamic stabilisation of an underactuated object. Since the object does not possess the ability of self-correction, its stability is entirely dependent on the forces applied to it. This creates a system that is sensitive to control inputs, where timing is critical to continuously counteract deviations and maintain the desired behavior. We develop a systematic method to control a 7-degree-of-freedom manipulator performing non-prehensile ball juggling with a tool. Our primary contribution is a model-based framework for generating juggling trajectories and stabilizing a periodic juggling motion for this hybrid system. The framework incorporates a two-stage optimal control approach to compute the underlying feasible motion patterns required for stable juggling. Offline-computed trajectories are then organised to enable real-time error correction without solving optimal control problems online. We demonstrate the effectiveness of the resulting controller by first evaluating its performance in a simulation environment and performing an experiment using a Franka Emika Panda robot.

</details>

---

### [[20_Research/Papers/具身智能/PhyRoGen_Synthetic_Generation_of_Physical_Robot_Manipulation_Puzzles_Using_Procedural_Content_Generation|PhyRoGen: Synthetic Generation of Physical Robot Manipulation Puzzles Using Procedural Content Generation]]

![[assets/2606.06569_figure.png|800]]

- **arXiv**: [2606.06569](https://arxiv.org/abs/2606.06569)
- **PDF**: https://arxiv.org/pdf/2606.06569
- **详细分析**: [[20_Research/Papers/具身智能/PhyRoGen_Synthetic_Generation_of_Physical_Robot_Manipulation_Puzzles_Using_Procedural_Content_Generation|PhyRoGen: Synthetic Generation of Physical Robot Manipulation Puzzles Using Procedural Content Generation]]
- **作者**: Lennart Julian Droß, Andreas Orthey, Marc Toussaint
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《PhyRoGen: Synthetic Generation of Physical Robot Manipulation Puzzles Using Procedural Content Generation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Meta-World, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation of physical puzzles is important for automatic assembly and disassembly tasks. However, to enable robots to solve physical puzzles, manipulation skills need to be learned, which requires large training datasets, the generation of which is often time consuming and tedious. To overcome this problem, we propose the Physical Robot Manipulation Puzzle Generation framework (PhyRoGen), which leverages procedural content generation (PCG) for automated generation of synthetic datasets of manipulation puzzles. PhyRoGen is a general-purpose puzzle generator, which can generate physical puzzles with interlocking object dependencies, where one articulated object must be manipulated before another can be moved. Based upon PhyRoGen, we define six concrete generators which we use to generate 24 physical puzzles. By using a benchmarking framework, we are able to solve all puzzles in 1 to 300 seconds using sampling-based planning algorithms. Finally, we demonstrate that every generated puzzle is manipulatable by using a KUKA LBR iiwa robot in a physical simulation. This shows that our framework is able to procedurally generate unique, solvable robot manipulation puzzles, which is a crucial ingredient to benchmark manipulation algorithms and to develop robust foundation models.

</details>

---

### [[20_Research/Papers/具身智能/Robots_Need_More_than_VLA_and_World_Models|Robots Need More than VLA and World Models]]

![[assets/2606.06556_figure.png|800]]

- **arXiv**: [2606.06556](https://arxiv.org/abs/2606.06556)
- **PDF**: https://arxiv.org/pdf/2606.06556
- **详细分析**: [[20_Research/Papers/具身智能/Robots_Need_More_than_VLA_and_World_Models|Robots Need More than VLA and World Models]]
- **作者**: Elis Karcini, Faisal Mehrban, Quang Nguyen, Mac Schwager, Arash Ajoudani, Cesar Cadena, Jan Peters, Marco Hutter, Haitham Bou-Ammar
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 3.3（加权：具身智能 1.8，世界模型 0.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Robots Need More than VLA and World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, RoboNet, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot intelligence is often framed as a policy-scaling problem: collect more robot demonstrations, train larger Vision-Language-Action (VLA) models, and expect broader generalisation. In this position paper, we argue that this framing is incomplete. The central bottleneck is not only policy learning, but the absence of mechanisms that convert the world's abundant unstructured behavioural data into grounded robot supervision. Human motion, internet video, simulation rollouts, and interactive demonstrations contain rich information about tasks, goals, contacts, failures, and physical constraints, yet most of this information is not directly usable by robot policies because it lacks embodiment-specific action labels, task semantics, and reward structure. We identify four missing components for the next generation of robotics: data interfaces for autolabelling unstructured behaviour, embodiment interfaces for retargeting human motion to robot actions, world-model interfaces for physics-grounded 3D reasoning, and reward interfaces for inferring task progress and success from video and language. We survey recent progress in robot foundation models, cross-embodiment datasets, learning from video, world models, and reward modelling, and propose a research agenda for building robotics systems that can learn not only from robot demonstrations, but from the broader physical world.

</details>

---
