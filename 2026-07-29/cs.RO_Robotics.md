# cs.RO | Robotics | 2026-07-29

#arxiv #ComputerScience

**论文数**: 20

### [[20_Research/Papers/强化学习/INTACT_Isomorphic_Intent-to-Action_Learning_for_Search-Free_World_Models|INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models]]

![[assets/2607.26056_figure.png|800]]

- **arXiv**: [2607.26056](https://arxiv.org/abs/2607.26056)
- **PDF**: https://arxiv.org/pdf/2607.26056
- **详细分析**: [[20_Research/Papers/强化学习/INTACT_Isomorphic_Intent-to-Action_Learning_for_Search-Free_World_Models|INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models]]
- **作者**: Junhan Sun, Hao Zhao, Guofeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: RL

#### 研究背景与动机

《INTACT: Isomorphic Intent-to-Action Learning for Search-Free World Models》归入 世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forward latent world models predict how actions change a scene, but recover actions for a desired change only through expensive test-time search. We introduce INTACT (INtent-To-ACTion), an end-to-end JEPA that turns action-labeled, reward-free trajectories into a deployable intent-to-action interface. Each transition supplies physical intent $z_{t+1}-z_t$, while a future goal supplies deployment intent $\operatorname{sg}(z_g)-z_t$. The architecture is isomorphic between the local and goal motion-intent backbone-input graphs through an identical four-slot grammar and shared parameters, and between supported local and goal motion-intent families through action-law semantics induced by the same predictor rather than pointwise latent equality. INTACT also provides intact transfer from RGB evidence to action-effective latent intent coordinates and from intent families to their corresponding action-law families. Asymmetric endpoint gradients ground physical successors and fix future goals as anchors, joining representation learning and control without pointwise latent matching or globally linear dynamics. The resulting coordinates support a robust distributional action law: its conditional mean serves directly as a search-free policy, while sampling remains available for diversity or optional verification. On the four official LeWM tasks, one-epoch, zero-search models reach 85.78\%, 100.00\%, 97.67\%, and 97.89\% success. Optional local CEM centered on the Direct plan reaches 96.86\% macro success using 384 instead of 9,000 candidate sequences, reducing sampling by $23.44\times$ while improving pure CEM by 16.00 points. One shared four-task encoder reaches 89.39\% E5 Direct macro and improves every task over jointly trained LeWM, while predicted--expert action-family kNN tracks Direct success at $r=0.954$. Direct inference takes 2.9--5.5 ms.

</details>

---

### [[20_Research/Papers/具身智能/S2A2_Audio-Visual_Imitation_Learning_for_Manipulation_Tasks_Using_Acoustic_Spatial_Information|S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information]]

![[assets/2607.26047_figure.png|800]]

- **arXiv**: [2607.26047](https://arxiv.org/abs/2607.26047)
- **PDF**: https://arxiv.org/pdf/2607.26047
- **详细分析**: [[20_Research/Papers/具身智能/S2A2_Audio-Visual_Imitation_Learning_for_Manipulation_Tasks_Using_Acoustic_Spatial_Information|S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information]]
- **作者**: Kaneyoshi Hiratsuka, Benjamin Yen, Ryosuke Kojima
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《S2A2: Audio-Visual Imitation Learning for Manipulation Tasks Using Acoustic Spatial Information》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Acoustic information provides rich cues about object location, material properties, and changes caused by contact or motion. This paper introduces a new set of acoustic-aware manipulation tasks for imitation learning, in which robots must use auditory cues to determine manipulation targets. These tasks require sound source localization and identification for active exploration in robotic manipulation. Also, we propose a multimodal imitation learning framework, Spatial-Spectral Audio Action (S2A2), that integrates visual features with acoustic spatial and acoustic signal information for the acoustic-aware manipulation tasks. We implemented S2A2 models that integrates policies such as ACT, Diffusion Policy, VQ-BeT, and $π_0$, into our framework. Simulation experiments showed that the proposed method is the most effective for tasks requiring both position and timbre. Furthermore, real-robot experiments confirm the applicability of the proposed tasks and framework to real-world manipulation.

</details>

---

### [[20_Research/Papers/强化学习/DC-WAM_Dynamic-Centric_Visual_Supervision_and_Reasoning_for_World-Action_Models|DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models]]

![[assets/2607.25918_figure.png|800]]

- **arXiv**: [2607.25918](https://arxiv.org/abs/2607.25918)
- **PDF**: https://arxiv.org/pdf/2607.25918
- **详细分析**: [[20_Research/Papers/强化学习/DC-WAM_Dynamic-Centric_Visual_Supervision_and_Reasoning_for_World-Action_Models|DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models]]
- **作者**: Haoyuan Ji, Lingxiang Fan, Shang Su, Yinqiao Lu, Mengkai Shi, Jun Gao, Shuo Feng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《DC-WAM: Dynamic-Centric Visual Supervision and Reasoning for World-Action Models》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-Action Models (WAMs) augment robot policies with future visual prediction, but it remains unclear what the visual modality should learn for control. While photorealistic future prediction provides dense supervision, it also incurs substantial computation and can allocate capacity to texture, illumination, and background variations that are only weakly related to action selection. Recent efficient WAM variants suggest that the main benefit of the video branch may not lie in the rendered future itself, but in the control-relevant visual representations induced during training. In this work, we revisit future video prediction from a dynamic-centric perspective and ask whether an existing RGB-based WAM can be redirected from appearance-dominated reconstruction toward interaction-induced visual dynamics without introducing additional modality-specific predictions or online inputs at deployment. We propose DC-WAM, a dynamic-centric WAM framework that redistributes supervision and computation in the RGB video branch. At the supervision level, DC-WAM combines temporal-difference flow matching with trajectory-guided weighting, emphasizing dense temporal changes and localized regions where the gripper, manipulated objects, and contact areas move. At the reasoning level, DynaRoute predicts token-wise dynamic relevance and converts it into an attention bias, guiding the model toward control-relevant future tokens. Experiments in simulation and on real-world manipulation tasks show that DC-WAM consistently improves policy performance, especially under out-of-distribution perturbations in lighting, object appearance, and background texture.

</details>

---

### [[20_Research/Papers/机器人/Modular_Robotic_Catheters_for_Endovascular_Aneurysm_Repair|Modular Robotic Catheters for Endovascular Aneurysm Repair]]

![[assets/2607.25807_figure.png|800]]

- **arXiv**: [2607.25807](https://arxiv.org/abs/2607.25807)
- **PDF**: https://arxiv.org/pdf/2607.25807
- **详细分析**: [[20_Research/Papers/机器人/Modular_Robotic_Catheters_for_Endovascular_Aneurysm_Repair|Modular Robotic Catheters for Endovascular Aneurysm Repair]]
- **作者**: Alex Ranne, Jinshi Zhao, Ali Anil Demircali, Songli Moey, Ayhan Aktas, Burak Temelkuran, Nassir Navab, Ferdinando Rodriguez y Baena
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Modular Robotic Catheters for Endovascular Aneurysm Repair》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fenestrated/Branched endovascular aneurysm repair (FEVAR/BEVAR) require surgeons to navigate catheters and guidewires into various branches of the abdominal aorta, before deploying stent grafts to alleviate pressure on the aneurysm. Previous clinical studies suggests that surgeons continue to struggle with vessel access using standard commercial instruments, prolonging the procedural time and inducing further complications. In this work, we present two contributions to solving this problem: 1) A bespoke 2-segment steerable catheter, consisting of 4 degrees of freedom to enhance dexterity. 2) An expandable, modular tendon-driven actuation platform that can accommodate for the redundancies introduced in our system. To fabricate the catheter, we capitalized on thermal fiber drawing, a technique that creates high-aspect ratio devices at scale, and processed the catheter with laser micro-machining to soften its tip. We evaluated the system using simulations, where we investigated the catheter's bending stiffness, then its steerability with in-vitro experiments in vascular phantoms. This handheld, robotic steerable catheter system has the potential to shorten the length of future endovascular surgeries, and give clinicians the tools to resolve challenging clinical cases.

</details>

---

### [[20_Research/Papers/具身智能/Transformer_Transformer_A_Unified_Model_for_Motion-Conditioned_Robot_Co-design|Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design]]

![[assets/2607.25798_figure.jpg|800]]

- **arXiv**: [2607.25798](https://arxiv.org/abs/2607.25798)
- **PDF**: https://arxiv.org/pdf/2607.25798
- **详细分析**: [[20_Research/Papers/具身智能/Transformer_Transformer_A_Unified_Model_for_Motion-Conditioned_Robot_Co-design|Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design]]
- **作者**: Huy Ha, C. Karen Liu, Shuran Song
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.9（加权：具身智能 0.6，世界模型 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Transformer Transformer: A Unified Model for Motion-Conditioned Robot Co-design》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

An often overlooked factor of robot manipulation performance is the embodiment of the robot itself. Motivated by this problem, we study motion-conditioned robot co-design, where the goal is to generate complete robot designs that track target end-effector trajectories (from human demonstrations) while optimizing user-defined rewards. We introduce Transformer Transformer, a diffusion transformer trained on RoboTokens, a unified tokenization of robot embodiments, states, and actions. The same architecture can be used across embodiment spaces (e.g., wheeled bimanual, quadrupeds, humanoids) and use cases (embodiment generation, cross embodiment controller). Rather than overfitting to one reward function, Transformer Transformer is a dynamics model, whose reward-agnostic state and action predictions can be converted into reward-specific value predictions. These value predictions are used to steer embodiment diffusion towards high value robot designs, through a procedure we call Dynamics Self-Guidance. Experiments across multiple design spaces show zero-shot optimization of unseen rewards and trajectories, improving performance and runtime over the evolutionary baseline. Finally, we fabricated an optimized ALOHA design, which reduced tracking error by over 70% compared to the original design.

</details>

---

### [[20_Research/Papers/机器人/Tripody_An_Overconstrained_3-SPR-like_Parallel_Robot_for_High-Reach_Construction_Tasks|Tripody: An Overconstrained 3-SPR-like Parallel Robot for High-Reach Construction Tasks]]

![[assets/2607.25781_figure.jpg|800]]

- **arXiv**: [2607.25781](https://arxiv.org/abs/2607.25781)
- **PDF**: https://arxiv.org/pdf/2607.25781
- **详细分析**: [[20_Research/Papers/机器人/Tripody_An_Overconstrained_3-SPR-like_Parallel_Robot_for_High-Reach_Construction_Tasks|Tripody: An Overconstrained 3-SPR-like Parallel Robot for High-Reach Construction Tasks]]
- **作者**: Julien Kindle, Jakub Raczy, Riccardo Balbi, Andrea Alessandretti, Cesar Cadena, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Tripody: An Overconstrained 3-SPR-like Parallel Robot for High-Reach Construction Tasks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many ceiling construction tasks still rely on heavy serial manipulators that are difficult to deploy in cluttered interiors, motivating lightweight, field-ready alternatives that reach ceiling height while maintaining millimeter-level accuracy and the stiffness demanded by overhead tool loads. We introduce Tripody, a wheeled 3-DoF parallel robot for high-reach tasks that replaces the base spherical joints of a classical 3-SPR (3 legs; S: base spherical joint; P: actuated prismatic joint; R: end-effector revolute joint) morphology with universal joints, intentionally overconstraining the mechanism; small, distributed elastic deflections absorb the resulting incompatibilities, preserving predominantly translational motion. The 33kg system extends from 1.7m to 3.4m in height, supports a continuous 32kg payload, and offers a modular end-effector interface for ceiling operations. We detail the mechanical design - including custom linear actuators and a kinematic-compatibility analysis - and a control stack for accurate positioning that combines SE(3) state estimation, forward kinematics, and task-space control. In experiments, Tripody exhibits similar in-plane stiffness to a spherical-base variant but substantially higher torsional stiffness - an increase of 67% at 1.7m, 196% at 2.6m, and 454% at 3.4m - while maintaining negligible cross-axis coupling. Closed-loop positioning with a total station converges below 0.6mm across the entire workspace; pure model extrapolation achieves a 95th-percentile error of 2.7mm (max 3.6mm). Finally, we demonstrate task-level ceiling-drilling feasibility in an open-loop study by drilling a 15-hole pattern with 4.5mm maximum relative hole-position error after rigid alignment. These results support overconstrained, compliance-absorbing 3-SPR-like architectures as a practical path to lightweight, high- reach, millimeter-accurate construction robots.

</details>

---

### [[20_Research/Papers/具身智能/Cooperative_Multi-UAV_Navigation_in_Complex_Environments_via_Systematic_Multi-Agent_Deep_Reinforcement_Learning|Cooperative Multi-UAV Navigation in Complex Environments via Systematic Multi-Agent Deep Reinforcement Learning]]

![[assets/2607.25754_figure.png|800]]

- **arXiv**: [2607.25754](https://arxiv.org/abs/2607.25754)
- **PDF**: https://arxiv.org/pdf/2607.25754
- **详细分析**: [[20_Research/Papers/具身智能/Cooperative_Multi-UAV_Navigation_in_Complex_Environments_via_Systematic_Multi-Agent_Deep_Reinforcement_Learning|Cooperative Multi-UAV Navigation in Complex Environments via Systematic Multi-Agent Deep Reinforcement Learning]]
- **作者**: Yu Su, Nabil Aouf
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 大模型, 具身智能
- **相关性评分**: 3.3（加权：具身智能 0.3，大模型 0.5，强化学习 1.6，机器人 0.9）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Cooperative Multi-UAV Navigation in Complex Environments via Systematic Multi-Agent Deep Reinforcement Learning》归入 强化学习、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative navigation of multi-agent UAVs in complex environments faces key challenges including local optima traps, sparse rewards, learning imbalance among agents, and insufficient cross-scenario generalisation. This paper proposes a multi-agent deep reinforcement learning framework that addresses these issues through coordinated exploration, demonstration exploitation, safe curriculum scheduling, and structure-aware generalisation. First, a perception mechanism combining memory of visited states, directional novelty estimates, and penalty backpropagation enables agents to proactively detect and escape local optima. Second, a hierarchical collaborative demonstration buffer with tiered behaviour cloning manages trajectories by degree of team collaboration and applies differential supervision to the actor network, improving demonstration utilisation under sparse collaborative signals. Third, a safety-aware dual-condition curriculum scheduling mechanism reviews mastered scenarios through back-testing and experience pre-filling during training, suppressing catastrophic forgetting while ensuring both task performance and flight safety. For generalisation, local geometric features computed from sensor readings are abstracted into a domain parameter, through which a structure-aware gating network and mixture-of-experts mechanism condition the policy on local structural patterns rather than scenario-specific coordinates, enabling cross-scenario transfer without exposure to the target environment. The framework is further validated under mixed static-dynamic obstacle settings, showing robust adaptability to dynamic disturbances. Simulation results confirm strong performance in collaboration success rate, navigation robustness, zero-shot cross-scenario generalisation, and dynamic environment adaptability.

</details>

---

### [[20_Research/Papers/强化学习/Tri-Manual_Visuomotor_Imitation_Learning_of_Robot_Policies|Tri-Manual Visuomotor Imitation Learning of Robot Policies]]

![[assets/2607.25731_figure.png|800]]

- **arXiv**: [2607.25731](https://arxiv.org/abs/2607.25731)
- **PDF**: https://arxiv.org/pdf/2607.25731
- **详细分析**: [[20_Research/Papers/强化学习/Tri-Manual_Visuomotor_Imitation_Learning_of_Robot_Policies|Tri-Manual Visuomotor Imitation Learning of Robot Policies]]
- **作者**: James Zhao, Mingyuan Ba, Weiming Zhi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Tri-Manual Visuomotor Imitation Learning of Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual teleoperation provides an effective way to collect robot demonstrations, but it assumes that the operator and robot have matching numbers of simultaneous control channels. This assumption breaks for tri-manual systems: the robot can coordinate three arms concurrently, whereas a single operator can continuously control only two. Pairwise mode switching may therefore record otherwise independent motions sequentially, causing behaviour cloning to reproduce delays imposed by the interface rather than required by the task. We present TriManPolicy, a tri-manual imitation learning system that allows one operator to demonstrate behaviours for three arms. Its central component is Dependency-Aware Tri-Arm Scheduling (DATS). The key idea is to preserve the demonstrated arm motions while reconsidering when they occur. DATS retimes demonstrations offline by preserving local sensorimotor segments of fixed duration and repositioning them according to constraints on task order and arm usage that are reviewed by a human. The resulting data train a single synchronous policy for all three arms, while deployment requires neither the dependency graph nor the scheduler. Across six challenging tasks performed in the real world, policies trained on demonstrations retimed by DATS exhibit more efficient coordination while maintaining comparable observed task success. Offline analysis further shows that DATS changes the supervision across arms rather than merely removing idle periods.

</details>

---

### [[20_Research/Papers/具身智能/When_Does_Legacy_Data_Start_to_Help_Emergent_Transfer_in_Cross-Configuration_Robot_Learning|When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning]]

![[assets/2607.25593_figure.png|800]]

- **arXiv**: [2607.25593](https://arxiv.org/abs/2607.25593)
- **PDF**: https://arxiv.org/pdf/2607.25593
- **详细分析**: [[20_Research/Papers/具身智能/When_Does_Legacy_Data_Start_to_Help_Emergent_Transfer_in_Cross-Configuration_Robot_Learning|When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning]]
- **作者**: Tao Wang, Hudson Hou, Yingdong Hu, Yufeng Liu, Qinghai Li, Yingjie Jiang, Yingzhi Wang, Cheng Ma, Richard Wang, Yang Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.9，机器人 1.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《When Does Legacy Data Start to Help? Emergent Transfer in Cross-Configuration Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, RoboNet, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic hardware evolves over time, but demonstration data is often tied to a specific sensor and actuator configuration. This raises a practical and underexplored question: when does legacy data begin to benefit an upgraded robot? We study this question on a wheeled humanoid platform across two hardware generations, where both the camera and gripper are changed while the overall morphology remains fixed. Contrary to the common assumption that more cross-configuration data is always helpful, we observe a grokking-like transition: legacy data remains ineffective until the upgraded configuration acquires a minimum level of task competence, after which co-training gains rise sharply before diminishing near saturation. We hypothesize that this task-dependent transition is governed by a transfer threshold and characterize the resulting three-phase pattern. Across real-robot manipulation tasks, we observe all three phases: no measurable benefit at low competence ($10.0\% \rightarrow 10.0\%$), a sharp gain after crossing the threshold ($23.3\% \rightarrow 86.7\%$ on flower insertion), and diminishing returns at high competence ($85.0\% \rightarrow 93.3\%$ on pen insertion). We provide a theoretical account based on gradient alignment and residual policy uncertainty, and derive a phase-aware rule for deciding when to collect more new-hardware data and when to reuse legacy demonstrations. We further validate this three-phase pattern on a mobile dual-arm watering task, with results consistent with our predictions.

</details>

---

### [[20_Research/Papers/强化学习/P3_Probabilistic_Policy_Propagation_for_Stable_VAE-Based_Robot_Learning|P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning]]

![[assets/2607.25541_figure.png|800]]

- **arXiv**: [2607.25541](https://arxiv.org/abs/2607.25541)
- **PDF**: https://arxiv.org/pdf/2607.25541
- **详细分析**: [[20_Research/Papers/强化学习/P3_Probabilistic_Policy_Propagation_for_Stable_VAE-Based_Robot_Learning|P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning]]
- **作者**: Liyun Yan, Jianming Ma, Yang Zhang, Shengcheng Fu, Zhanxiang Cao, Keqi Zhu, Yizhi Chen, Yue Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Variational Autoencoders are widely used to encode high-dimensional and noisy observations in robotics. However, their stochastic latent creates a mismatch with Proximal Policy Optimization (PPO): an effective policy marginalizes over the latent distribution, whereas former implementations estimate its probability ratio and KL divergence using only one latent sample. We identify a fundamental but overlooked theoretical cause: naive single-sample approximations in stochastic latent space induce significant variance and bias in the surrogate loss. To address this, we introduce P^3 (Probabilistic Policy Propagation), a distribution-aware optimization framework for VAE-based policies. $P^3$ couples moment-based probabilistic method for stable and efficient learning with sampling-based calibration for robust policy behavior under latent uncertainty. In our experiments, P^3 boosts data efficiency from 64.6% to &gt;96%, reduces convergence steps by &gt;20%. Furthermore, P^3 is evaluated on challenging humanoid parkour tasks and shows an effective foundation for VAE-based PPO. Code is available at https://github.com/ylyem9x/P3_Open.

</details>

---

### [[20_Research/Papers/具身智能/A_Causality-aware_Infer-diagnose-refine_Framework_for_Test-time_Modality_Adaptation_in_VLA_Models|A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models]]

![[assets/2607.25516_figure.png|800]]

- **arXiv**: [2607.25516](https://arxiv.org/abs/2607.25516)
- **PDF**: https://arxiv.org/pdf/2607.25516
- **详细分析**: [[20_Research/Papers/具身智能/A_Causality-aware_Infer-diagnose-refine_Framework_for_Test-time_Modality_Adaptation_in_VLA_Models|A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models]]
- **作者**: Haoyu Zhang, Yuwei Wu, Jin Chen, Gao Zhi, Zhenxin Diao, Mingyang Gao, Kun Wu, Yongchun Liu, Fan Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《A Causality-aware Infer-diagnose-refine Framework for Test-time Modality Adaptation in VLA Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models predict sequential actions to execute tasks specified by language instructions, conditioned on visual observations and proprioceptive states. However, how to fuse modalities in VLA models remains an open problem, since robot manipulation involves dynamic phases, such as long-distance movements and close-range interactions, in which the importance of visual observations may vary over time. In this paper, we propose an infer-diagnose-refine (IDR) framework, a model-agnostic framework that can be integrated with diverse VLA architectures for refining action predictions at test time. IDR first infers actions under factual and counterfactual scenarios of visual observations, and then diagnoses the causal effects of visual observations as the estimated dynamic importance, which is finally used to refine the action predictions in a training-free manner. We further design a causality-aware action refiner to realize the IDR framework, including zero-padding interventions for inferring counterfactual actions, norm-based quantification for diagnosing causal effects, and gated residual fusion for refining actions. Extensive experiments on both simulation benchmarks and real-world tasks show improvements in overall performance across multiple VLA backbones, demonstrating the efficacy of dynamically adjusting visual importance at test time.

</details>

---

### [[20_Research/Papers/具身智能/Decompose_and_Reorganize_Planning_with_Primitives_and_Visuomotor_Policies_Learned_from_Demonstrations|Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations]]

![[assets/2607.25397_figure.png|800]]

- **arXiv**: [2607.25397](https://arxiv.org/abs/2607.25397)
- **PDF**: https://arxiv.org/pdf/2607.25397
- **详细分析**: [[20_Research/Papers/具身智能/Decompose_and_Reorganize_Planning_with_Primitives_and_Visuomotor_Policies_Learned_from_Demonstrations|Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations]]
- **作者**: Yizhou Chen, Hang Xu, Dongjie Yu, Yupu Lu, Tengye Xu, Zeqing Zhang, Wei Zhang, Yi Ren, Ben M. Chen, Jia Pan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Decompose and Reorganize: Planning with Primitives and Visuomotor Policies Learned from Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Successfully automating dexterous, long-horizon robotic manipulation requires frameworks capable of both high-level reasoning and fine-grained execution. Traditional task and motion planning (TAMP), while excellent at symbolic planning, is often brittle in contact-rich operations. Simultaneously, imitation learning (IL), while effective in manipulation tasks with visual feedback, is limited by its low capability in spatial generalization and multi-stage operation. To reconcile their complementary strengths and limitations, we propose DR-LfD (Decomposed and Reorganized Skills Learned from Demonstrations), a framework that seamlessly integrates visuomotor policies into a TAMP-gated decision-making system. Based on contact relationships, DR-LfD decomposes human demonstrations into atomic skills, which are reproduced as visuomotor policies or object-centric primitives. The initiation, termination, and constraints of the visuomotor policies are carefully modeled and implemented in a TAMP-compatible form, enabling reorganization of skills learned from different sources. DR-LfD transforms the learning problem from one requiring exponential demonstration data over possible skill sequences to one whose demonstration burden scales with the number of distinct skill types, with limited data for each skill. Through comprehensive real-world and simulation benchmarking across diverse scenarios, we demonstrate the strong performance of DR-LfD on tasks involving multiple steps, unseen setups, and physical constraints. Project website: https://dr-lfd.github.io/DR-LfD-website.

</details>

---

### [[20_Research/Papers/机器人/Belief-Aware_Influence_and_Trust_(BAIT)_Shaping_Human_Belief_During_Repeated_Human-Robot_Interaction|Belief-Aware Influence and Trust (BAIT): Shaping Human Belief During Repeated Human-Robot Interaction]]

![[assets/2607.25327_figure.png|800]]

- **arXiv**: [2607.25327](https://arxiv.org/abs/2607.25327)
- **PDF**: https://arxiv.org/pdf/2607.25327
- **详细分析**: [[20_Research/Papers/机器人/Belief-Aware_Influence_and_Trust_(BAIT)_Shaping_Human_Belief_During_Repeated_Human-Robot_Interaction|Belief-Aware Influence and Trust (BAIT): Shaping Human Belief During Repeated Human-Robot Interaction]]
- **作者**: Ye-Ji Mun, Mahsa Golchoubian, Shahabedin Sagheb, Yan Bai, Tianhao Ji, Dylan P. Losey, Katherine Driggs-Campbell
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Belief-Aware Influence and Trust (BAIT): Shaping Human Belief During Repeated Human-Robot Interaction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Repeated human-robot interaction (HRI) requires proactively accounting for humans who continually adapt to evolving beliefs about the robot. Prior frameworks often treat encounters as isolated events, suffering cumulative task performance decay as human perception drifts, or maintain long-term influence through erratic, unpredictable behavior that erodes perceived human trust and relies on computationally unscalable formulations. To address these gaps, we introduce the Belief- Aware Influence and Trust (BAIT) controller. BAIT integrates a hierarchical particle filter, which infers both fast human strategic shifts and slow perceptual belief updates, with a belief-aware Model Predictive Path Integral planner. BAIT explicitly optimizes the trade-off between long-horizon influence and human trust, while enforcing immediate task performance as a strict constraint. Across simulations, a human-subject study, and a real-world GEM vehicle deployments in repeated lane-merging scenarios, BAIT achieves task performance comparable to baselines that optimize long-term influence through unpredictability while yielding significantly higher user trust. The video demonstrating our experiments is available at https://youtu.be/GsPfHRujzVs.

</details>

---

### [[20_Research/Papers/具身智能/SONG_A_Photorealistic_3D_Gaussian_Simulation_Platform_for_Benchmarking_Social_Navigation|SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation]]

![[assets/2607.25219_figure.png|800]]

- **arXiv**: [2607.25219](https://arxiv.org/abs/2607.25219)
- **PDF**: https://arxiv.org/pdf/2607.25219
- **详细分析**: [[20_Research/Papers/具身智能/SONG_A_Photorealistic_3D_Gaussian_Simulation_Platform_for_Benchmarking_Social_Navigation|SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation]]
- **作者**: Weiqi Huang, Dianyi Yang, Jiaxin Li, Shuangyi Dong, Hao Xu, Zan Wang, Wei Liang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《SONG: A Photorealistic 3D Gaussian Simulation Platform for Benchmarking Social Navigation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SONG-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social navigation has progressed from simplified 2D environments toward a more general vision-based setting, in which a robot needs to achieve socially compliant behavior purely from onboard visual observations. Yet supporting simulation platforms have not kept pace: existing options either lack visual observations, lack moving human avatars, or fall short of real-world fidelity in appearance and pedestrian behavior, offering limited support for advancing vision-based social navigation. We introduce SONG, a SOcial Navigation platform powered by 3D Gaussian splatting (3DGS). It leverages 3DGS for both scene and avatar representations, drives pedestrians using semantically grounded trajectories generated by a large language model, and synthesizes their full-body motion with a trajectory-conditioned generator to produce continuous, natural movement. On top of the platform, we curate SONG-Bench, a set of evaluation episodes stratified by difficulty, and propose a multi-dimensional metric suite covering effectiveness, safety, and social compliance. A systematic evaluation of representative navigation baselines reveals three findings: (a) vision-based social navigation is far from solved; (b) a critical safety deficit precedes social etiquette; (c) real-world data matters more than model scale. Crucially, we demonstrate that fine-tuning on our curated data effectively improves the success rate in real-world environments. We hope our platform provides a faithful and rigorous testbed for the next generation of vision-based social navigation research.

</details>

---

### [[20_Research/Papers/强化学习/Decentralized_Scalable_Exploration_via_Emergent_Adaptive_Lévy_Walks_on_Minimal-Sensing_Platforms|Decentralized Scalable Exploration via Emergent Adaptive Lévy Walks on Minimal-Sensing Platforms]]

![[assets/2607.25195_figure.png|800]]

- **arXiv**: [2607.25195](https://arxiv.org/abs/2607.25195)
- **PDF**: https://arxiv.org/pdf/2607.25195
- **详细分析**: [[20_Research/Papers/强化学习/Decentralized_Scalable_Exploration_via_Emergent_Adaptive_Lévy_Walks_on_Minimal-Sensing_Platforms|Decentralized Scalable Exploration via Emergent Adaptive Lévy Walks on Minimal-Sensing Platforms]]
- **作者**: Wai Lun Leong, Teo Swee Huat Rodney
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Decentralized Scalable Exploration via Emergent Adaptive Lévy Walks on Minimal-Sensing Platforms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient autonomous exploration with palm-sized nano-UAVs remains challenging due to severe limitations in sensing, computation, and flight endurance. We present a lightweight sensor-driven Lévy walk (SDLW) controller for aerial robots weighing under 50 grams and equipped with sparse local sensing. The method combines discrete Lévy step-length sampling with a sensor-reactive heading policy using directional range measurements. Each robot independently samples its Lévy exponent from a uniform prior to diversify exploration without inter-robot communication for exploration control. Each robot then selects headings using a von Mises distribution that biases motion toward open directions while preserving superdiffusive exploration properties. The controller operates at constant computational cost, enabling scalable multi-UAV exploration. Simulation results show coverage improvements of 79.6% in open arenas, 43.1% in rooms-and-corridors layouts, and 13.6% in cluttered environments, with collision reductions of 13.0%, 7.1%, and 1.4%, respectively, relative to a uniform-heading Lévy walk baseline. This work provides a practical framework for scalable multi-robot exploration on minimal-sensing, resource-constrained nano-UAVs.

</details>

---

### [[20_Research/Papers/机器人/Reactive_3D_Motion_Planning_for_a_Franka_Arm_via_Star-World_Workspace_Reshaping|Reactive 3D Motion Planning for a Franka Arm via Star-World Workspace Reshaping]]

![[assets/2607.25138_figure.png|800]]

- **arXiv**: [2607.25138](https://arxiv.org/abs/2607.25138)
- **PDF**: https://arxiv.org/pdf/2607.25138
- **详细分析**: [[20_Research/Papers/机器人/Reactive_3D_Motion_Planning_for_a_Franka_Arm_via_Star-World_Workspace_Reshaping|Reactive 3D Motion Planning for a Franka Arm via Star-World Workspace Reshaping]]
- **作者**: Gia Dcosta, Saayuj Deshpande, Samhitha Vedire
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, ComputerVision, Systems

#### 研究背景与动机

《Reactive 3D Motion Planning for a Franka Arm via Star-World Workspace Reshaping》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Star-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety inflation can cause nearby obstacles to overlap, violating the disjoint-obstacle assumptions used by many modulation-based reactive planners. We investigate Star-World workspace reshaping for three-dimensional reactive control of a Franka Emika Panda manipulator. At each update, intersecting inflated obstacles are clustered and replaced by star-shaped proxies before a dynamical-system-based end-effector controller is evaluated. A null-space artificial-potential-field term provides complementary arm-body avoidance. We compare reshaped and unreshaped obstacle representations in six PyBullet scenarios using goal attainment, path-length ratio, and computation time. In this preliminary 12-trial evaluation, reshaping reaches the goal in five of six scenarios, compared with four of six for the unreshaped baseline. It resolves the canonical overlapping-wall case and requires 0.68--8.70\,ms per workspace update for scenes containing one to seven obstacles. However, it also increases path length, produces near-equilibria in two cases, and closes a navigable corridor through over-aggressive merging. These results show both the promise and the practical limitations of transferring Star-World guarantees from workspace geometry to a redundant manipulator controlled through inverse kinematics.

</details>

---

### [[20_Research/Papers/机器人/Input_Shaping_for_Point-to-Point_Motion_with_a_Continuum_Robot_Arm|Input Shaping for Point-to-Point Motion with a Continuum Robot Arm]]

![[assets/2607.25071_figure.png|800]]

- **arXiv**: [2607.25071](https://arxiv.org/abs/2607.25071)
- **PDF**: https://arxiv.org/pdf/2607.25071
- **详细分析**: [[20_Research/Papers/机器人/Input_Shaping_for_Point-to-Point_Motion_with_a_Continuum_Robot_Arm|Input Shaping for Point-to-Point Motion with a Continuum Robot Arm]]
- **作者**: Rodolfo Hdz. Ibarra, Karan Baker, Parsa Molaei, Adrian Stein, Hunter B. Gilbert
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Input Shaping for Point-to-Point Motion with a Continuum Robot Arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A cable-driven continuum robot arm is an underactuated mechanism and may suffer residual vibration at the end of a rest-to-rest maneuver. In this work, a time-delay filter is applied as an input shaper to the system to eliminate the excitation of vibratory modes. A non-robust and a robust time-delay filter are designed based on a linear system model and demonstrate improved response compared to a velocity-driven pulse input. Experimental results using the continuum robot validate the application of the input shaper, with reduced overshoot and settling time exemplifying the reduction in oscillation at the end of the maneuver. It is also shown that utilizing the robust shaper further improves the response of the arm in comparison to applying the non-robust shaper. These results are significant towards the precise and robust implementation of continuum robots in applications involving arbitrary end-effector trajectories.

</details>

---

### [[20_Research/Papers/具身智能/Hybrid_Artificial_Potential_Fields_and_Spatio-Temporal_Transformers_for_Real-Time_AUV_Path_Planning|Hybrid Artificial Potential Fields and Spatio-Temporal Transformers for Real-Time AUV Path Planning]]

![[assets/2607.25056_figure.png|800]]

- **arXiv**: [2607.25056](https://arxiv.org/abs/2607.25056)
- **PDF**: https://arxiv.org/pdf/2607.25056
- **详细分析**: [[20_Research/Papers/具身智能/Hybrid_Artificial_Potential_Fields_and_Spatio-Temporal_Transformers_for_Real-Time_AUV_Path_Planning|Hybrid Artificial Potential Fields and Spatio-Temporal Transformers for Real-Time AUV Path Planning]]
- **作者**: Khadija Rais, Abdelmadjid Benmachiche, Imene Soualmia
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Hybrid Artificial Potential Fields and Spatio-Temporal Transformers for Real-Time AUV Path Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL, MARL, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous Underwater Vehicles (AUVs) operate in complex, unstructured environments where efficient and safe path planning is critical for mission success and energy conservation. This paper presents a comprehensive comparative evaluation of thirteen path planning algorithms, ranging from classical graph-search methods (A*, Dijkstra) and sampling-based approaches (RRT*) to metaheuristics (PSO, GA, ACO, BCO) and learning-based architectures. Special emphasis is placed on a proposed hybrid approach combining Artificial Potential Fields (APF) with a Spatio-Temporal (ST) Transformer. Evaluated across five navigation scenarios on high-resolution underwater terrain maps, all algorithms achieved 100\% task completion; however, significant trade-offs emerged in path optimality, collision avoidance, and computational load. The Hybrid APF + ST-Transformer demonstrated superior balanced performance, achieving the shortest average path length (943.15 units), a low collision rate (0.031), and efficient computation time (0.96 s), outperforming standalone learning models, which required fallback mechanisms and classical methods that incurred higher latency. While classical algorithms guaranteed collision-free paths, their excessive path lengths and processing times render them less suitable for dynamic underwater operations. Conversely, metaheuristic approaches introduced trajectory complexity unsuitable for strict energy constraints. Based on these findings, the Hybrid APF + ST framework is recommended as a principal approach for real-time AUV navigation, offering a robust solution that harmonizes reactive obstacle avoidance with global path optimality in resource-constrained underwater systems.

</details>

---

### [[20_Research/Papers/机器人/Motion_Generation_With_Environmental_Constraints|Motion Generation With Environmental Constraints]]

![[assets/2607.25053_figure.png|800]]

- **arXiv**: [2607.25053](https://arxiv.org/abs/2607.25053)
- **PDF**: https://arxiv.org/pdf/2607.25053
- **详细分析**: [[20_Research/Papers/机器人/Motion_Generation_With_Environmental_Constraints|Motion Generation With Environmental Constraints]]
- **作者**: Előd Páll, Oliver Brock
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Motion Generation With Environmental Constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot motion planning faces challenges in high-dimensional spaces and uncertain environments, often constrained by the need for collision-free motions. We advocate an alternative approach, Environmental Constraint Exploitation (ECE), where deliberate contact with the environment simplifies planning by reducing dimensionality and computational complexity. By integrating ECE into motion planning algorithms, we bias exploration to task-relevant regions and leverage contact for uncertainty reduction to improve robustness during execution. We evaluate ECE benefits with RRT-based planners and demonstrate their practical benefits in a real-world application. This work consolidates and extends prior research, showcasing how ECE simplifies motion planning while enhancing adaptability and performance in complex environments.

</details>

---

### [[20_Research/Papers/强化学习/Egocentric_Station_Holding_of_Robotic_Fish_in_Unknown_Turbulent_Background_Flow|Egocentric Station Holding of Robotic Fish in Unknown Turbulent Background Flow]]

![[assets/2607.24860_figure.png|800]]

- **arXiv**: [2607.24860](https://arxiv.org/abs/2607.24860)
- **PDF**: https://arxiv.org/pdf/2607.24860
- **详细分析**: [[20_Research/Papers/强化学习/Egocentric_Station_Holding_of_Robotic_Fish_in_Unknown_Turbulent_Background_Flow|Egocentric Station Holding of Robotic Fish in Unknown Turbulent Background Flow]]
- **作者**: Xiaozhu Lin, Xu Huang, Hongru Dai, Xiaopei Liu, Junzhi Yu, Yang Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.9（加权：具身智能 0.6，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Egocentric Station Holding of Robotic Fish in Unknown Turbulent Background Flow》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Approaching a target position and holding station in flowing water is a fundamental and critical capability for robotic fish operating in natural aquatic environments. Despite decades of advances in enhancing swimming efficiency and maneuverability, this capability remains underdeveloped, largely owing to the insufficiently characterized, highly nonlinear fluid-structure interactions inherent to freely swimming robotic fish in flows. To bridge this gap, we propose the SWiFT framework, a Swimming With Flow Toolbox that enables the efficient exploration of an egocentric station-holding policy for a body and/or caudal fin (BCF) robotic fish in unknown and turbulent background flows via reinforcement learning (RL). Our SWiFT integrates a free-swimming flow-tank experimental setup with a highly efficient, physically consistent computational fluid dynamics (CFD)-based simulator and a systematic sim-to-real transfer pipeline. The resulting policy achieves substantial improvements over state-of-the-art methods across all metrics, most notably root-mean-square error (RMSE) of distance. Furthermore, we validated that egocentric feedback alone, without any explicit flow sensing, enables station-holding in unknown turbulent flows, closely mirroring the biological phenomenon of rheotaxis. Accordingly, the success of this egocentric station-holding policy not only advances robotic fish control toward real-world deployment, but also highlights SWiFT's promise as a foundation for tackling complex swimming tasks for underwater robots.

</details>

---
