# cs.CV | Computer Vision and Pattern Recognition | 2026-07-07

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Deform360_A_Massive_Multi-view_Visuotactile_Dataset_for_Deformable_World_Models|Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models]]

![[assets/2607.05390_figure.png|800]]

- **arXiv**: [2607.05390](https://arxiv.org/abs/2607.05390)
- **PDF**: https://arxiv.org/pdf/2607.05390
- **详细分析**: [[20_Research/Papers/具身智能/Deform360_A_Massive_Multi-view_Visuotactile_Dataset_for_Deformable_World_Models|Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models]]
- **作者**: Hongyu Li, Wanjia Fu, Xiaoyan Cong, Zekun Li, Binghao Huang, Hanxiao Jiang, Xintong He, Yiqing Liang, Rao Fu, Tao Lu, Srinath Sridhar, Kevin A. Smith...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，世界模型 0.8，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Deform360: A Massive Multi-view Visuotactile Dataset for Deformable World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ClothesNet, Vid2World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting object dynamics (i.e., world modeling) is a fundamental challenge for robotic manipulation, and modeling deformable objects presents a particularly difficult case due to their high-dimensional state spaces and complex material properties. While current world models approach this through two distinct paradigms: learning the dynamics over the 2D pixel space or more explicit 3D geometric space. A systematic understanding of their relative strengths and limitations remains elusive due to the lack of diverse, large-scale real-world data. To address this, we present Deform360, a large-scale visuotactile dataset featuring 198 daily-life objects, 1,980 interaction sequences, and over 215 hours of observations from 41 surround-view cameras and bimanual tactile grippers to capture both global motion and contact-induced local deformations. Leveraging a novel markerless visuotactile 3D tracking pipeline to extract dense geometry and motion, we systematically evaluate current state-of-the-art world models, comparing 2D video models against 3D particle models. Finally, we provide a preliminary demonstration indicating the real-world applicability of our dataset by performing robot planning tasks on deformable objects. Our analysis reveals key insights into the trade-offs between structural priors and scalability, providing a solid benchmark for future research in generalizable deformable object-centric world modeling. Project website: https://deform360.lhy.xyz

</details>

---

### [[20_Research/Papers/具身智能/Green_for_Go,_Red_for_No_Visual_Grounding_via_Semantic_Segmentation_for_VLA_Navigation_Policies|Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies]]

![[assets/2607.05122_figure.png|800]]

- **arXiv**: [2607.05122](https://arxiv.org/abs/2607.05122)
- **PDF**: https://arxiv.org/pdf/2607.05122
- **详细分析**: [[20_Research/Papers/具身智能/Green_for_Go,_Red_for_No_Visual_Grounding_via_Semantic_Segmentation_for_VLA_Navigation_Policies|Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies]]
- **作者**: Adrian Szvoren, Dimitrios Kanoulas, Nilufer Tuptuk
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BYOVLA, MobilityVLA, OmniVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

</details>

---

### [[20_Research/Papers/机器人/SLAM_Structured_and_Localized_Analytic_Manifold_Adaptation_for_Lifelong_VPR|SLAM: Structured and Localized Analytic Manifold Adaptation for Lifelong VPR]]

![[assets/2607.04764_first_page.png|800]]

- **arXiv**: [2607.04764](https://arxiv.org/abs/2607.04764)
- **PDF**: https://arxiv.org/pdf/2607.04764
- **详细分析**: [[20_Research/Papers/机器人/SLAM_Structured_and_Localized_Analytic_Manifold_Adaptation_for_Lifelong_VPR|SLAM: Structured and Localized Analytic Manifold Adaptation for Lifelong VPR]]
- **作者**: Kenta Tsukahara, Kanji Tanaka, Rai Hisada
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《SLAM: Structured and Localized Analytic Manifold Adaptation for Lifelong VPR》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual Place Recognition (VPR) in lifelong deployment requires continuous adaptation to new environments without catastrophic forgetting. In this paper, we propose SLAM, a Structured and Localized Analytic Manifold adaptation framework. Our framework elegantly unifies uncertainty-aware smoothing via Unscented transformation, topological space partitioning through a Gaussian Mixture Model (GMM), and $H_\infty$ robust bound optimization into a singular, unified closed-form analytical recursion. Exhaustive ablation studies demonstrate that while the synergistic combination of uncertainty smoothing and localized mapping (U+G configuration) achieves the state-of-the-art nominal accuracy of 27.5%, the full deployment of the $H_\infty$ bound does not require an architectural split; rather, it introduces a mathematically guaranteed minimax robust bound. This formulation enables the system to seamlessly modulate the intrinsic trade-off between nominal placement precision and worst-case disturbance attenuation through a single regularization parameter.

</details>

---

### [[20_Research/Papers/机器人/Trajectory-Anchor_Optimization_for_Overconfident_Thermal_Visual_Place_Recognition_Zero-Leakage_OOD_Auditing_and_Kidnapped-Robot_Recovery|Trajectory-Anchor Optimization for Overconfident Thermal Visual Place Recognition: Zero-Leakage OOD Auditing and Kidnapped-Robot Recovery]]

![[assets/2607.04745_figure.png|800]]

- **arXiv**: [2607.04745](https://arxiv.org/abs/2607.04745)
- **PDF**: https://arxiv.org/pdf/2607.04745
- **详细分析**: [[20_Research/Papers/机器人/Trajectory-Anchor_Optimization_for_Overconfident_Thermal_Visual_Place_Recognition_Zero-Leakage_OOD_Auditing_and_Kidnapped-Robot_Recovery|Trajectory-Anchor Optimization for Overconfident Thermal Visual Place Recognition: Zero-Leakage OOD Auditing and Kidnapped-Robot Recovery]]
- **作者**: Zhiyuan Lu, Kanji Tanaka
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Trajectory-Anchor Optimization for Overconfident Thermal Visual Place Recognition: Zero-Leakage OOD Auditing and Kidnapped-Robot Recovery》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Closed-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern thermal visual place recognition (TIR-VPR) frontends based on foundation models achieve remarkable closed-set retrieval but suffer from an overconfident forced-matching failure mode. Under out-of-distribution (OOD) or unmapped conditions, they generate highly plausible yet false loop candidates without a drop in similarity scores. While classical multi-hypothesis tracking (MHT) backends can mitigate these ambiguities by maintaining divergent trajectory beliefs, their exponential computational overhead violates real-time robotic constraints. To bridge this gap, we present Trajectory-Anchor Optimization (TAO). To counter the combinatorial challenge of evaluating parallel hypotheses (e.g., K=100), TAO compresses multi-view temporal verification into a batched SE(2) Procrustes alignment problem. By leveraging tensor-level vectorization and single-invocation batched SVD, this formulation bypasses the dynamic tree expansion of MHT, guaranteeing a strictly bounded per-frame execution loop of O(KN). Under a strict zero-leakage evaluation protocol, we show that while a passive geometric backend cannot mathematically separate metric localization errors from coherent hallucinations at a micro-scale (&lt;5m) due to local visual ambiguities, TAO serves as an efficient fail-safe filter at a macro-scale. Within a 5m radius, hallucinations often possess a locally consistent geometry that deceives rigid alignment. However, beyond this threshold, the K=100 disparate hypotheses disperse spatially across the global map. This dispersion breaks the rigid temporal co-visibility constraint within the sliding window (N=20), causing the joint optimization residual to escalate sharply. Consequently, TAO establishes a distinct macroscopic convergence basin (10m) where multi-view geometric consistency reliably isolates catastrophic topological breaks and suppresses critical false acceptances.

</details>

---

### [[20_Research/Papers/具身智能/PixelPilot_Scalable_Vision-Language-Action_Models_for_End-to-End_Autonomous_Driving|PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving]]

![[assets/2607.04637_figure.png|800]]

- **arXiv**: [2607.04637](https://arxiv.org/abs/2607.04637)
- **PDF**: https://arxiv.org/pdf/2607.04637
- **详细分析**: [[20_Research/Papers/具身智能/PixelPilot_Scalable_Vision-Language-Action_Models_for_End-to-End_Autonomous_Driving|PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving]]
- **作者**: Pin Tang, Guoqing Wang, Xiangxuan Ren, Zhongdao Wang, Guodongfang Zhao, Bailan, Chao Ma
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习
- **相关性评分**: 1.7（加权：具身智能 1.5，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《PixelPilot: Scalable Vision-Language-Action Models for End-to-End Autonomous Driving》归入 具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenDriveVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action Models (VLAs), which leverage the advanced reasoning capabilities of Vision-Language Models (VLMs), show promising generalization in complex autonomous driving scenarios. Existing VLAs typically predict and optimize 3D trajectories from 2D images. While intuitive, this 2D-to-3D prediction is inherently entangled with camera parameters, leading to limited data scalability across heterogeneous driving datasets. Moreover, directly optimizing in 3D space induces severe convergence to trivial solutions, where VLAs rely on ego-status rather than visual scene understanding. To address these issues, we propose PixelPilot, a novel VLA featuring a decoupled planning and lifting paradigm. In the planning phase, PixelPilot reformulates scene understanding and trajectory prediction as sensor-agnostic 2D-to-2D tasks in the image plane, thereby facilitating scalable training across diverse datasets. The planned 2D trajectories are then deterministically lifted to 3D only during inference, ensuring the full exploitation of visual cues and generalization across different vehicles. To realize this paradigm, we propose a knowledge-instilled policy learning strategy that applies dense, intermediate rewards via Group Relative Policy Optimization (GRPO) to enforce a rigorous causal chain from visual perception to spatial planning. Extensive experiments demonstrate that PixelPilot achieves state-of-the-art performance in both open-loop and closed-loop settings, validating its superior scalability and visual reasoning capabilities.

</details>

---

### [[20_Research/Papers/机器人/Real-Time_LiDAR_Gaussian_Splatting_SLAM|Real-Time LiDAR Gaussian Splatting SLAM]]

![[assets/2607.04127_figure.png|800]]

- **arXiv**: [2607.04127](https://arxiv.org/abs/2607.04127)
- **PDF**: https://arxiv.org/pdf/2607.04127
- **详细分析**: [[20_Research/Papers/机器人/Real-Time_LiDAR_Gaussian_Splatting_SLAM|Real-Time LiDAR Gaussian Splatting SLAM]]
- **作者**: Seungjun Tak, Yewon Jeon, Jaeik Hwang, SukMin Hwang, Seongbo Ha, Hyeonwoo Yu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.CV

#### 研究背景与动机

《Real-Time LiDAR Gaussian Splatting SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a real-time LiDAR-based framework for Gaussian Splatting SLAM that tightly couples fast G-ICP registration with spherical rasterization-based dense mapping for large-scale sequences. Leveraging LiDAR geometry rather than appearance, we reuse tracking-estimated local covariances to initialize Gaussians with range-aware scales and to derive surface normals for geometry-aware map optimization. We further introduce a covariance-derived geometry score that measures local complexity and drives pruning in planar regions and selective densification in structurally rich areas, while optimized Gaussians and LiDAR-specific confidence cues are fed back to improve tracking robustness. On the Newer College dataset, our method achieves an F-score of 86.78\% using purely online trajectories at real-time speed ($&gt;$20 FPS), and additional experiments on other datasets confirm its stability and scalability.

</details>

---

### [[20_Research/Papers/具身智能/WorldBagel_Uncovering_the_Power_of_Unified_Multimodal_Models_for_Vision-Language-Action-World_Modeling|WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling]]

![[assets/2607.03461_figure.png|800]]

- **arXiv**: [2607.03461](https://arxiv.org/abs/2607.03461)
- **PDF**: https://arxiv.org/pdf/2607.03461
- **详细分析**: [[20_Research/Papers/具身智能/WorldBagel_Uncovering_the_Power_of_Unified_Multimodal_Models_for_Vision-Language-Action-World_Modeling|WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling]]
- **作者**: Zelin Zhao, Min Shi, Bo Yuan, Haotian Xue, Jialuo Li, Lama Moukheiber, Humphrey Shi, Yongxin Chen
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 世界模型, 机器人, 强化学习
- **相关性评分**: 2.62（加权：具身智能 1.5，大模型 0.4，强化学习 0.16，世界模型 0.36，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《WorldBagel: Uncovering the Power of Unified Multimodal Models for Vision-Language-Action-World Modeling》归入 具身智能、大模型、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BagelVLA, CoRL, InternVLA, OpenVLA, RynnVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models aim to capture environment dynamics in ways that support perception, reasoning, and action, and have recently become a central direction in Vision-Language-Action-World (VLAW) modeling. Meanwhile, unified vision-language models have demonstrated strong multimodal generation capabilities, yet their potential as world models remains underexplored. In this work, we introduce \texttt{WorldBagel}, a unified VLAW framework built on BAGEL, a modern multimodal unified model, and use it to systematically investigate the role of unification in world modeling. Across multi-task robotic manipulation and cross-domain experiments, \texttt{WorldBagel} consistently outperforms task-specific alternatives and learns action representations that are more structured and semantically aligned with visual and linguistic context. Experiments on LIBERO, Language Table, and Franka show that unification is not only an architectural convenience, but also a key factor in learning effective VLAW models, leading to consistent empirical gains and deeper insights into multimodal world modeling. Code and model checkpoints will be released upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/CLEAR_Closed-Loop_Reinforcement_Learning_at_Scale_for_End-to-End_Autonomous_Driving|CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving]]

![[assets/2607.02841_figure.png|800]]

- **arXiv**: [2607.02841](https://arxiv.org/abs/2607.02841)
- **PDF**: https://arxiv.org/pdf/2607.02841
- **详细分析**: [[20_Research/Papers/具身智能/CLEAR_Closed-Loop_Reinforcement_Learning_at_Scale_for_End-to-End_Autonomous_Driving|CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving]]
- **作者**: Yunxiao Shi, Hong Cai, Mohammad Ghavamzadeh, Fatih Porikli
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.0（加权：具身智能 0.9，强化学习 0.8，机器人 0.3）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving》归入 具身智能、强化学习、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

</details>

---

### [[20_Research/Papers/具身智能/EVA-Client_A_Unified_Data_Collection,_Inference,_and_Deployment_Framework_for_Embodied_Policies_on_Real_Robots|EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots]]

![[assets/2607.02646_figure.png|800]]

- **arXiv**: [2607.02646](https://arxiv.org/abs/2607.02646)
- **PDF**: https://arxiv.org/pdf/2607.02646
- **详细分析**: [[20_Research/Papers/具身智能/EVA-Client_A_Unified_Data_Collection,_Inference,_and_Deployment_Framework_for_Embodied_Policies_on_Real_Robots|EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots]]
- **作者**: Heqing Yang, Yang Yi, Liyao Wang, Linqing Zhong, Donglin Yang, Ruipu Wu, Zitong Bai, Fengjiao Chen, Manyuan Zhang, Linjiang Huang, Si Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《EVA-Client: A Unified Data Collection, Inference, and Deployment Framework for Embodied Policies on Real Robots》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本中出现的评测对象/数据集包括：OpenVLA, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present EVA-Client, an open-source framework for deployment, data collection, and evaluation of trained manipulation policies on real robots. Sitting between a policy server and the physical hardware, EVA-Client unifies the real-robot stages of the policy iteration loop within a single codebase. It makes three contributions. First, a component-decoupled architecture in which robot backends, inference strategies, and transport middlewares form an orthogonal grid: adding a robot or a strategy touches only its own layer. Second, inspectable execution through Debug, Collect, and Eval workflows, with modes ranging from open-loop simulation to continuous real-time control. Third, every evaluation run doubles as a data collection, recording full rollouts in training-ready format alongside exhaustive logs and a side-by-side comparison viewer, so each evaluation feeds the next round of training rather than ending as an unrecorded impression. EVA-Client further consolidates major real-time inference strategies, synchronous and asynchronous execution, ACT-style temporal ensembling, Real-Time Chunking, and a naive-async ablation baseline, behind a single configuration surface.

</details>

---

### [[20_Research/Papers/具身智能/DynaWM_A_Base-VLA-Guided_World_Foundation_Model_for_Moving-Object_Manipulation|DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation]]

![[assets/2607.02604_figure.png|800]]

- **arXiv**: [2607.02604](https://arxiv.org/abs/2607.02604)
- **PDF**: https://arxiv.org/pdf/2607.02604
- **详细分析**: [[20_Research/Papers/具身智能/DynaWM_A_Base-VLA-Guided_World_Foundation_Model_for_Moving-Object_Manipulation|DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation]]
- **作者**: Chongkei Chang, Zhidong Deng
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 世界模型
- **相关性评分**: 2.9（加权：具身智能 1.8，大模型 0.4，世界模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《DynaWM: A Base-VLA-Guided World Foundation Model for Moving-Object Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Base-VLA, DFM-VLA, DGBench, DynamicVLA, Meta-World, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although vision-language-action (VLA) models have received widespread attention, many challenges remain in manipulating dynamic moving objects. In most existing approaches, end-to-end forward or inverse dynamics models, i.e., world models, are incorporated into high-performance base VLA architectures, which may degrade the performance of well-pretrained base VLA models due to inappropriate fine-tuning. In this paper, we propose DynaWM, a base-VLA-guided world foundation model that adapts to a wide variety of fine-tuned and coarse-tuned base-VLA checkpoints for moving-object manipulation. DynaWM uses a Mamba-3-based action encoder to encode the base action chunk produced by the base VLA into an action-conditioning representation, a V-JEPA 2.1 vision encoder to extract features from multi-view observation history, and a proprioceptive state encoder to encode robotic-arm proprioceptive states. These feature representations jointly condition a flow-matching DiT to regenerate motion-aware action trajectories for moving-object manipulation. For systematic evaluation, we construct the DynaGrasp-32 benchmark, covering six categories of moving-object manipulation tasks, including velocity variation, trajectory variation, and multi-object manipulation, as well as the DynaGrasp-1600 dataset, which consists of 32 scenarios, 1,600 demonstration trajectories, and approximately 1.53M images. For fine-tuned base-VLA checkpoints, DynaWM achieves percentage improvements of 7.19, 45.31, 1.88, and 10.94 over SmolVLA, X-VLA, π0, and π0.5, respectively. For coarse-tuned base-VLA checkpoints, performance increases by 35.13, 44.06, 35.69, and 26.13 percentage, respectively. Ablation experiments show that visual encoding enhances success by 27.50%, while reducing success by 45.44% if action conditioning is removed.

</details>

---
