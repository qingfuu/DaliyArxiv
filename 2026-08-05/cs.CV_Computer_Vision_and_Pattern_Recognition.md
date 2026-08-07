# cs.CV | Computer Vision and Pattern Recognition | 2026-08-05

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/Beyond_Simply_Environment_Scaling_Designing_Effective_Environment_Distributions_for_Multimodal_Agent_Learning|Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning]]

![[assets/2608.03571_figure.png|800]]

- **arXiv**: [2608.03571](https://arxiv.org/abs/2608.03571)
- **PDF**: https://arxiv.org/pdf/2608.03571
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Simply_Environment_Scaling_Designing_Effective_Environment_Distributions_for_Multimodal_Agent_Learning|Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning]]
- **作者**: Kejian Zhu, Zhuoran Jin, Dongqi Huang, Hongbang Yuan, Yupu Hao, Kang Liu, Jun Zhao
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Beyond Simply Environment Scaling: Designing Effective Environment Distributions for Multimodal Agent Learning》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent works train agents by constructing large-scale multimodal environment pools. However, we find that simply increasing the number of multimodal environments does not always benefit. We further analyze the limitations in current multimodal environment distributions through a series of experiments. Based on these findings, we study how to build more effective training environment distributions from two dimensions: **diversity** and **difficulty structure**. For diversity, we propose **Ability-aware Environment Selection (AES)** to obtain diverse environment sets. For difficulty structure, we propose **Hierarchical Difficulty Curriculum (HDC)**, which organizes curriculum learning through two difficulty levels: harness weakening and state-scale progression. Experiments show that AES and HDC effectively improve multimodal agent training.

</details>

---

### [[20_Research/Papers/具身智能/Lightweight_3D_Object_Detection_via_Mamba-Based_Knowledge_Distillation|Lightweight 3D Object Detection via Mamba-Based Knowledge Distillation]]

![[assets/2608.03490_figure.png|800]]

- **arXiv**: [2608.03490](https://arxiv.org/abs/2608.03490)
- **PDF**: https://arxiv.org/pdf/2608.03490
- **详细分析**: [[20_Research/Papers/具身智能/Lightweight_3D_Object_Detection_via_Mamba-Based_Knowledge_Distillation|Lightweight 3D Object Detection via Mamba-Based Knowledge Distillation]]
- **作者**: Quoc Cuong Ninh, Huy Xuan Pham, Anh Tung Nguyen, Dinh Hoan Trinh
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Lightweight 3D Object Detection via Mamba-Based Knowledge Distillation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3D object detection using light detection and ranging (LiDAR) sensors requires a balance between accuracy and computational efficiency for onboard perception in autonomous driving and robotic navigation. Many existing LiDAR-based detection methods employ complex architectures to extract features, integrating large amounts of contextual information to enhance accuracy. This often results in significant computational costs, leading to suboptimal performance on resource-constrained embedded devices. In this study, we propose a knowledge distillation framework that transfers object-level voxel representations from a strong teacher model to lightweight student models through selective voxel-space feature alignment. Taking advantage of the linear-time sequence model with selective state spaces (Mamba), we design a multi-branch Mamba teacher backbone and a box-aware feature transfer mechanism that aligns spatially corresponding voxel features between teacher and student networks through a Mamba-based projection module. Experimental results on both a public dataset and real-world data show that our approach significantly reduces computational load while maintaining competitive accuracy compared with state-of-the-art methods.

</details>

---

### [[20_Research/Papers/机器人/SLAMFormer-$_infty$_Infinite_SLAM_Transformer_for_Unbounded_Frontend_and_Backend_Processing|SLAMFormer-$\infty$: Infinite SLAM Transformer for Unbounded Frontend and Backend Processing]]

![[assets/2608.03429_figure.png|800]]

- **arXiv**: [2608.03429](https://arxiv.org/abs/2608.03429)
- **PDF**: https://arxiv.org/pdf/2608.03429
- **详细分析**: [[20_Research/Papers/机器人/SLAMFormer-$_infty$_Infinite_SLAM_Transformer_for_Unbounded_Frontend_and_Backend_Processing|SLAMFormer-$\infty$: Infinite SLAM Transformer for Unbounded Frontend and Backend Processing]]
- **作者**: Zhijian Fang, Weicheng Zheng, Yijun Yuan, Weibang Wang, Zhuoguang Chen, Chang Sun, Junhao Huang, Kenan Li, Minghui Qin, Hang Zhao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《SLAMFormer-$\infty$: Infinite SLAM Transformer for Unbounded Frontend and Backend Processing》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce the Infinite SLAM Transformer (SLAMFormer-$\infty$), the first geometric transformer capable of supporting both long-range frontend and backend processing without an explicit distance bound. Instead of relying on a first-frame-anchored formulation, SLAMFormer-$\infty$ employs memory conditions to define flexible coordinate systems and scales for input frames, enabling more expressive structural conditioning. Built upon this formulation, the frontend preserves efficient local computation, while the backend jointly optimizes long-range trajectories and scene geometry in a globally consistent manner. Experimental results demonstrate that SLAMFormer-$\infty$ achieves superior or highly competitive performance in both trajectory estimation and scene reconstruction across large-scale datasets. Notably, SLAMFormer-$\infty$ generalizes to extremely long trajectories, successfully operating on sequences exceeding $17\mathrm{km}$.

</details>

---

### [[20_Research/Papers/机器人/PLS-Calib_A_Partial_Least_Squares_Framework_for_Event_Camera_and_Odometry_Calibration_under_Ground_Motion_Constraints|PLS-Calib: A Partial Least Squares Framework for Event Camera and Odometry Calibration under Ground Motion Constraints]]

![[assets/2608.03296_figure.png|800]]

- **arXiv**: [2608.03296](https://arxiv.org/abs/2608.03296)
- **PDF**: https://arxiv.org/pdf/2608.03296
- **详细分析**: [[20_Research/Papers/机器人/PLS-Calib_A_Partial_Least_Squares_Framework_for_Event_Camera_and_Odometry_Calibration_under_Ground_Motion_Constraints|PLS-Calib: A Partial Least Squares Framework for Event Camera and Odometry Calibration under Ground Motion Constraints]]
- **作者**: Guangyu Li, Xiao Li, Yujie Wu, Changshuo Wang, Prayag Tiwari, Jiang Cai, Fangwen Yu, Mingkun Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《PLS-Calib: A Partial Least Squares Framework for Event Camera and Odometry Calibration under Ground Motion Constraints》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate extrinsic rotation calibration between sensors is fundamental to the performance of robotic perception systems. However, most existing calibration techniques rely on full 6-DoF motion to excite all degrees of freedom, which is often infeasible for ground-constrained robots with limited motion capabilities. Recent approaches designed for such restricted settings, such as Canonical Correlation Analysis (CCA)-based methods, suffer from ill-conditioned covariance matrices that lead to numerical instability and suboptimal calibration accuracy. To overcome these limitations, we present a novel rotation calibration framework named PLS-Calib that, for the first time, leverages Partial Least Squares (PLS) regression to model the latent kinematic correlations between asynchronous, heterogeneous sensor streams. Specifically, we apply our method to the calibration of an event camera and an odometry onboard a ground robot. To improve event-based pattern detection, we introduce a polarity-aware event representation, which enhances spatiotemporal contrast in circular calibration targets. Our PLS-based formulation yields a closed-form, stable solution that avoids matrix singularities inherent in CCA-based approaches. Extensive experiments on both synthetic and real-world datasets validate the effectiveness of our approach, demonstrating significant improvements in calibration robustness and accuracy over state-of-the-art methods. This work offers a practical and theoretically grounded solution for rotation calibration in constrained robotic systems and opens up new directions for applying statistical learning techniques in neuromorphic vision.

</details>

---

### [[20_Research/Papers/世界模型/CrossScope_A_Role-Asymmetric_World_Model_for_Joint_Dual-Scope_Surgical_Video_Prediction|CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction]]

![[assets/2608.03211_figure.png|800]]

- **arXiv**: [2608.03211](https://arxiv.org/abs/2608.03211)
- **PDF**: https://arxiv.org/pdf/2608.03211
- **详细分析**: [[20_Research/Papers/世界模型/CrossScope_A_Role-Asymmetric_World_Model_for_Joint_Dual-Scope_Surgical_Video_Prediction|CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction]]
- **作者**: Wanhao Liu, Jinsong Lin, Rulin Zhou, Chi Kit Ng, Wenbin Pan, Zhiqing Tang, Dongyue Li, Liwei Luo, Yanshen Wu, Panshuo Li, Zhiyong Xiong, Huxin Gao...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《CrossScope: A Role-Asymmetric World Model for Joint Dual-Scope Surgical Video Prediction》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual world models typically learn future dynamics from a single observation stream, limiting their ability to model cooperative systems with multiple independently moving observers. We investigate this challenge in Mother--Child endoscopic retrograde cholangiopancreatography (ERCP), where two flexible scopes provide complementary yet role-dependent views without a calibrated stereo relationship. Unlike conventional multi-view fusion that assumes symmetric information exchange, we formulate \textbf{role-asymmetric dual-scope future prediction}, where cross-view evidence is selectively transferred according to the prediction target and its underlying spatial requirements. We propose \textbf{CrossScope}, a dual-stream surgical world model that preserves view-specific experts while enabling target-specific evidence routing through geometry-guided residual interactions. CrossScope learns two complementary communication directions: geometric motion cues from the Mother view guide Child-view future dynamics, while pose-aligned Child appearance supports Mother-view prediction only when valid spatial correspondence is established. This design allows each scope to contribute task-relevant evidence without compromising its view-specific representation. To evaluate this problem, we establish a paired dual-scope benchmark comprising synchronized phantom and real-world ERCP episodes, with evaluations assessing visual fidelity, structural preservation, target localization, and motion consistency. Experiments demonstrate that CrossScope consistently outperforms strong surgical video generation baselines, validating the importance of role-aware evidence routing for multi-observer visual world modeling.

</details>

---

### [[20_Research/Papers/具身智能/DRIFT_Derailing_Denoising_Trajectories_of_Flow-Matching_VLAs_with_Adversarial_Patch_Attack|DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack]]

![[assets/2608.03207_figure.png|800]]

- **arXiv**: [2608.03207](https://arxiv.org/abs/2608.03207)
- **PDF**: https://arxiv.org/pdf/2608.03207
- **详细分析**: [[20_Research/Papers/具身智能/DRIFT_Derailing_Denoising_Trajectories_of_Flow-Matching_VLAs_with_Adversarial_Patch_Attack|DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack]]
- **作者**: Hoseong Tae, Jong-Seok Lee
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.8（加权：具身智能 0.6，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DRIFT: Derailing Denoising Trajectories of Flow-Matching VLAs with Adversarial Patch Attack》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching vision-language-action (VLA) models such as pi0 generate robot actions by integrating a learned denoising velocity field, and have been reported to resist adversarial perturbations that readily fool autoregressive VLAs. We show that this robustness is largely illusory: it stems from prior attacks ignoring the multi-step denoising ODE. We introduce DRIFT (Denoising Redirection via Input perturbation of the Flow-matching Trajectory), a test-time universal adversarial patch placed on the robot's gripper that attacks the denoising velocity field of an off-the-shelf policy. Our central finding is counterintuitive: attacking only the first denoising step is both stronger and cheaper than attacking a wider window of steps, which we explain through a gradient conflict unique to input-space optimization and which is exactly opposite to the training-time backdoor regime. On pi0 and pi0.5 across four LIBERO suites, DRIFT breaks essentially all originally-solvable tasks with a small single patch, far exceeding action- and embedding-space attack baselines.

</details>

---

### [[20_Research/Papers/机器人/Bridging_Online_and_Offline_Handwriting_via_Differentiable_Physical_Rendering|Bridging Online and Offline Handwriting via Differentiable Physical Rendering]]

![[assets/2608.03198_figure.png|800]]

- **arXiv**: [2608.03198](https://arxiv.org/abs/2608.03198)
- **PDF**: https://arxiv.org/pdf/2608.03198
- **详细分析**: [[20_Research/Papers/机器人/Bridging_Online_and_Offline_Handwriting_via_Differentiable_Physical_Rendering|Bridging Online and Offline Handwriting via Differentiable Physical Rendering]]
- **作者**: Seonmi Park, Seunghyun Shin, Vihaan Misra, Dongmin Shin, Ukcheol Shin, Jean Oh, Hae-Gon Jeon
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Bridging Online and Offline Handwriting via Differentiable Physical Rendering》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Realistic handwritten text generation plays an important role in numerous applications, such as font design, biometric authentication, and robotic calligraphy. Existing methods are typically divided into two independent paradigms: online approaches that estimate handwriting trajectories and offline approaches that synthesize realistic handwriting images. While online models capture structural and temporal dynamics, they often lack fine-grained textures, whereas offline models reproduce realistic appearance but discard stroke order. However, unifying online and offline models remains challenging due to (1) the lack of an explicit physical model linking stroke kinematics to pixel-level appearance and (2) the absence of paired trajectory-image datasets. Moreover, enabling end-to-end learning requires a differentiable rendering process across motion and appearance domains. To address these challenges, we propose a compact physical brush model that bridges stroke dynamics and visual appearance, together with a differentiable rendering module that converts stroke trajectories into stylized images. By integrating these components, we propose a unified online-offline handwriting generation framework via differentiable brush rendering. The proposed framework consists of four core modules: 1) a text-to-stroke generator that predicts the target stroke conditioned on the given text and style image, 2) a brush parameter observer that extracts brush model parameters from style references, 3) a differentiable brush renderer that maps a stroke sequence and physical brush parameters into a handwritten image, and 4) a zero-shot image refiner that refines rendered images via diffusion models. Extensive experiments and real-world robotic calligraphy demonstrations validate our approach, achieving both structural and visual fidelity.

</details>

---

### [[20_Research/Papers/大模型/Multimodal_Plant_Root_Phenotyping_with_Integration_of_3D_Skeleton_Extraction_and_Language_Analysis|Multimodal Plant Root Phenotyping with Integration of 3D Skeleton Extraction and Language Analysis]]

![[assets/2608.03109_figure.png|800]]

- **arXiv**: [2608.03109](https://arxiv.org/abs/2608.03109)
- **PDF**: https://arxiv.org/pdf/2608.03109
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Plant_Root_Phenotyping_with_Integration_of_3D_Skeleton_Extraction_and_Language_Analysis|Multimodal Plant Root Phenotyping with Integration of 3D Skeleton Extraction and Language Analysis]]
- **作者**: Jiakai Lin, Zijun Li, Guoyu Lu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Multimodal Plant Root Phenotyping with Integration of 3D Skeleton Extraction and Language Analysis》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Plant root phenotyping is fundamental to understanding below-ground structures, optimizing crop management, and improving agricultural sustainability. This paper presents a multimodal robotic AI framework that integrates 3D skeleton extraction with language-guided reasoning for interpretable and data-efficient root analysis. We develop an unsupervised skeleton extraction network based on Weighted Laplacian Contraction (W-LBC) to generate high-fidelity structural representations from dense point clouds captured by robotic 3D sensing platforms. Quantitative morphological descriptors, including root count, length, branching angle, and density, are computed from the reconstructed skeleton graph to capture geometric and topological characteristics. Building on these features, we introduce an Evidence-First language modeling framework that fine-tunes GPT as an interactive analytical chatbot using automatically generated instruction--response pairs. Each training sample provides measurable evidence before natural-language reasoning, enabling the model to ground interpretation in quantitative morphology. Through supervised fine-tuning, GPT associates numerical structure with semantic meaning, producing biologically consistent explanations of growth patterns and adaptive traits. Experiments show that the structure-guided framework achieves robust, interpretable reasoning across 12 plant species with diverse root architectures. By integrating unsupervised 3D geometric perception with large-scale language understanding, our approach bridges quantitative analysis and semantic interpretation, establishing a unified paradigm for explainable robotic plant root phenotyping.

</details>

---

### [[20_Research/Papers/强化学习/RealWeather_Realistic_and_Scene-Faithful_Weather_Translation_with_Driving_World_Models|RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models]]

![[assets/2608.02953_figure.png|800]]

- **arXiv**: [2608.02953](https://arxiv.org/abs/2608.02953)
- **PDF**: https://arxiv.org/pdf/2608.02953
- **详细分析**: [[20_Research/Papers/强化学习/RealWeather_Realistic_and_Scene-Faithful_Weather_Translation_with_Driving_World_Models|RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models]]
- **作者**: Yuwei Ning, Liangzhi Wang, Yi Xiao, Zhenhua Wu, Yun Pang, Mingkun Chan, Jichang Li, Guanbin Li
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，世界模型 0.8）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《RealWeather: Realistic and Scene-Faithful Weather Translation with Driving World Models》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Realistic weather translation is valuable for developing and evaluating autonomous driving systems, yet collecting paired videos of the same scenes under different weather conditions at scale is impractical. Existing methods therefore rely on synthetic data, 3D weather editing, or geometry-conditioned generation, often compromising weather realism or scene fidelity. We propose RealWeather, a driving world model for both realistic and scene-faithful weather translation. Our key idea is to learn authentic weather dynamics directly from real-world videos. Specifically, RealWeather employs Progressive Realism Bootstrapping, an iterative data-refinement strategy. Assisted by an auxiliary Pseudo-Clear Generation pipeline, training initially starts with pseudo-style conditioning videos. As training proceeds, these inputs are progressively replaced with increasingly realistic videos generated by the model itself. This strategy bridges the pseudo-to-real domain gap, allowing the model to adapt seamlessly to real-world input distributions and naturally support bidirectional clear adverse translation. Furthermore, to strictly enforce structural integrity and suppress hallucinations, we introduce Scene-Fidelity RL Optimization, a reward-driven policy optimization strategy that explicitly penalizes alterations to safety-critical driving elements. Extensive experiments demonstrate that RealWeather significantly outperforms existing methods in visual realism and structural preservation, while enabling robust long-tail weather scenario generation and strong zero-shot out-of-distribution generalization.

</details>

---

### [[20_Research/Papers/具身智能/Enfold_Folding_World_Model_Imagination_into_Predictive_Representations_for_Ultra-Efficient_Embodied_Control|Enfold: Folding World Model Imagination into Predictive Representations for Ultra-Efficient Embodied Control]]

![[assets/2607.26657_figure.png|800]]

- **arXiv**: [2607.26657](https://arxiv.org/abs/2607.26657)
- **PDF**: https://arxiv.org/pdf/2607.26657
- **详细分析**: [[20_Research/Papers/具身智能/Enfold_Folding_World_Model_Imagination_into_Predictive_Representations_for_Ultra-Efficient_Embodied_Control|Enfold: Folding World Model Imagination into Predictive Representations for Ultra-Efficient Embodied Control]]
- **作者**: Weili Zeng, Yitong Xing, Fulong Liu, Chengqun Yang, Antao Xiang, Feng Tian, Jingnan Gao, Jisong Cai, Xin Wang, Xiaomin Wu, Yao Mu, Xiaokang Yang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，世界模型 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Enfold: Folding World Model Imagination into Predictive Representations for Ultra-Efficient Embodied Control》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World generative models are typically used through what they produce: a rendered future, a video-conditioned action, or latent context computed by a costly generative branch. We argue that their more reusable asset is the computation that constructs a future. As a generator transforms a corrupted future into a coherent trajectory, its intermediate states organize appearance, spatial layout, and interaction across levels of abstraction. Can this future-generative computation be internalized in a representation inferred from the present alone? We present Enfold, which transfers this computation into a representation predicted from the current visual context and language instruction. During training, multi-level states exposed as the generator processes the observed future supervise a current-only encoder. The learned representation is fed back to condition future generation and is read by task heads without allowing task gradients to reshape the encoder. At deployment, action prediction no longer executes the generator. Across LIBERO, RoboTwin2.0, and real-robot tasks, Enfold supports strong control while reducing action latency by $3.7\times$ relative to Fast--WAM, Enfold-Flash reaches $10.1\times$. Representation analyses show that it suppresses nuisance variation and preferentially captures changes that emerge over longer horizons. When the current scene is altered by human intervention, both the generated continuation and the executed actions adapt, which is inconsistent with fixed trajectory replay. These results recast a world generator as a source of predictive control representations: its future need not be materialized at every step if its internal structure can be enfolded into the present.

</details>

---
