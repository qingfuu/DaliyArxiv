# cs.CV | Computer Vision and Pattern Recognition | 2026-06-08

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/AnchorWorld_Embodied_Egocentric_World_Simulation_with_View-based_Evolution_Customization|AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization]]

![[assets/2606.07326_figure.png|800]]

- **arXiv**: [2606.07326](https://arxiv.org/abs/2606.07326)
- **PDF**: https://arxiv.org/pdf/2606.07326
- **详细分析**: [[20_Research/Papers/具身智能/AnchorWorld_Embodied_Egocentric_World_Simulation_with_View-based_Evolution_Customization|AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization]]
- **作者**: Yu Li, Menghan Xia, Gongye Liu, Xintao Wang, Conglang Zhang, Lei Ke, Yuxuan Lin, Ruihang Chu, Pengfei Wan, Kun Gai, Yujiu Yang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.9，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《AnchorWorld: Embodied Egocentric World Simulation with View-based Evolution Customization》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AnchorWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite being a pivotal frontier, interactive world modeling remains underexplored in terms of the versatile controllability required by practical scenarios. To bridge this gap, we present AnchorWorld, a framework that advances egocentric simulation through enhanced interaction integrity and a flexible mechanism for world customization. First, we utilize 3D human motion as the primary interaction modality. To complement the out-of-view or truncated body parts in egocentric views, we introduce an auxiliary training supervision that incorporates exogenous viewpoints decoupled from the agent's first-person sensorium. It allows the model to observe the agent's full-body positioning relative to the environment, facilitating a more robust spatial grounding of human-world interactions. Furthermore, we propose a simple yet effective mechanism for customizing self-evolving worlds. This is achieved by defining anchor views within a unified world coordinate system, coupled with textual descriptions dictating the dynamic evolution of local scenes. Experimental results show that AnchorWorld significantly outperforms state-of-the-art baselines, while ablation studies validate the effectiveness of our key designs. Notably, our customization scheme exhibits promising spatio-temporal geometric consistency and adheres strictly to the prescribed evolutionary dynamics.

</details>

---

### [[20_Research/Papers/具身智能/Does_Appearance_Help_A_Systematic_Study_of_Image-Based_Re-Identification_in_Online_3D_Multi-Pedestrian_Tracking|Does Appearance Help? A Systematic Study of Image-Based Re-Identification in Online 3D Multi-Pedestrian Tracking]]

![[assets/2606.07233_figure.png|800]]

- **arXiv**: [2606.07233](https://arxiv.org/abs/2606.07233)
- **PDF**: https://arxiv.org/pdf/2606.07233
- **详细分析**: [[20_Research/Papers/具身智能/Does_Appearance_Help_A_Systematic_Study_of_Image-Based_Re-Identification_in_Online_3D_Multi-Pedestrian_Tracking|Does Appearance Help? A Systematic Study of Image-Based Re-Identification in Online 3D Multi-Pedestrian Tracking]]
- **作者**: Eduardo Borges, Luís Garrote, Urbano J. Nunes
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Does Appearance Help? A Systematic Study of Image-Based Re-Identification in Online 3D Multi-Pedestrian Tracking》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MobileNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LiDAR-based 3D Multi-Object Tracking (MOT) typically relies solely on geometric information, which is often insufficient to distinguish between targets during prolonged occlusions or in crowded human-populated environments. While integrating RGB-based Re-Identification (ReID) offers a theoretical solution for preserving identity context, existing approaches often rely on computationally expensive parallel detectors that hinder real-time robot responsiveness. This work presents a systematic study of image-based ReID in online 3D MOT, utilizing a lightweight projection-based framework to decouple geometric and appearance modeling for mobile robots. A comprehensive analysis of feature extraction architectures is conducted, employing lightweight CNNs and Vision Transformers, and evaluating various multi-modal data association strategies to balance computational latency with robust tracking. Experiments on the Pedestrian class of the KITTI dataset reveal that naive linear fusion, of appearance and motion costs, degrades performance due to visual noise. Conversely, a cascaded matching strategy successfully recovers occluded tracks without compromising overall precision, effectively preventing identity switches to maintain human-robot interaction continuity. We show that lightweight architectures can offer an optimal trade-off between the low latency required for safe navigation and the discriminative power needed for social awareness.

</details>

---

### [[20_Research/Papers/具身智能/Robotic_Policy_Adaptation_via_Weight-Space_Meta-Learning|Robotic Policy Adaptation via Weight-Space Meta-Learning]]

![[assets/2606.07217_figure.png|800]]

- **arXiv**: [2606.07217](https://arxiv.org/abs/2606.07217)
- **PDF**: https://arxiv.org/pdf/2606.07217
- **详细分析**: [[20_Research/Papers/具身智能/Robotic_Policy_Adaptation_via_Weight-Space_Meta-Learning|Robotic Policy Adaptation via Weight-Space Meta-Learning]]
- **作者**: Christian Bianchi, Siamak Yousefi, Alessio Sampieri, Andrea Roberti, Luca Rigazio, Fabio Galasso, Luca Franco
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Robotic Policy Adaptation via Weight-Space Meta-Learning》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Hyper-GoalNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are emerging as a promising paradigm for robotic manipulation, enabling general-purpose policies trained from large corpora of demonstrations and action labels. However, adapting these models to new tasks still typically requires task-specific demonstrations, action annotations, and additional fine-tuning, making deployment costly and difficult to scale. We propose WIZARD, a weight-space meta-learning framework that sidesteps task-specific fine-tuning by generating task-specific LoRA parameters for a frozen VLA policy. Given only a language instruction and a short demonstration video, WIZARD predicts the corresponding adaptation weights in a single forward pass, without target-task action labels or test-time optimization. During meta-training, WIZARD learns to map task evidence directly to expert LoRA updates, capturing relationships between tasks in weight space. Experiments on LIBERO show that WIZARD improves performance by up to ~2x on unseen dataset collections and up to ~14x on unseen tasks. On a Franka Emika Panda, WIZARD consistently improves over a real-domain adapted baseline, showing that generated adapters provide task-level specialization beyond simulation.

</details>

---

### [[20_Research/Papers/具身智能/LARA_Latent_Action_Representation_Alignment_for_Vision-Language-Action_Models|LARA: Latent Action Representation Alignment for Vision-Language-Action Models]]

![[assets/2606.07100_figure.png|800]]

- **arXiv**: [2606.07100](https://arxiv.org/abs/2606.07100)
- **PDF**: https://arxiv.org/pdf/2606.07100
- **详细分析**: [[20_Research/Papers/具身智能/LARA_Latent_Action_Representation_Alignment_for_Vision-Language-Action_Models|LARA: Latent Action Representation Alignment for Vision-Language-Action Models]]
- **作者**: Mengya Liu, Baoxiong Jia, Jiangyong Huang, Jingze Zhang, Siyuan Huang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《LARA: Latent Action Representation Alignment for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual-language action (VLA) models enable robots to predict actions directly from observations and language instructions, but their performance depends on large-scale, high-quality data and is limited by the scarcity of real-world robot action datasets. To facilitate VLA model learning with abundant unlabeled human videos, Latent Action Models (LAM) learn latent action representations from visual dynamics to provide additional supervision for VLA learning. However, LAM and VLA are typically trained separately, leaving LAM ungrounded during VLA training and VLA models constrained by frozen LAM representations. To address these issues, we propose Latent Action Representation Alignment (LARA), a plug-and-play framework that jointly optimizes LAM and VLA via representation alignment. This enables reciprocal benefits where LAMs learn with action trajectories to avoid spurious visual changes, while VLAs are regularized by forward dynamics learned within LAMs to reduce hallucinations of functionally ineffective trajectories. We demonstrate LARA versatility and effectiveness for pre-training, post-training enhancement of pre-trained VLA models, and LAM refinement, achieving an average of ~10%, ~5%, and ~15% improvement over 3 simulation and 1 meticulously designed real-world robotic manipulation benchmarks.

</details>

---

### [[20_Research/Papers/具身智能/ActionMap_Robot_Policy_Learning_via_Voxel_Action_Heatmap|ActionMap: Robot Policy Learning via Voxel Action Heatmap]]

![[assets/2606.06904_figure.png|800]]

- **arXiv**: [2606.06904](https://arxiv.org/abs/2606.06904)
- **PDF**: https://arxiv.org/pdf/2606.06904
- **详细分析**: [[20_Research/Papers/具身智能/ActionMap_Robot_Policy_Learning_via_Voxel_Action_Heatmap|ActionMap: Robot Policy Learning via Voxel Action Heatmap]]
- **作者**: Pei Yang, Hai Ci, Yanzhe Chen, Qi Lv, Han Cai, Mike Zheng Shou
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.9，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ActionMap: Robot Policy Learning via Voxel Action Heatmap》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have advanced rapidly across backbones, training recipes, and data scale, yet the action decoder, which converts the backbone's hidden state into a continuous control signal, has barely changed and remains a single-point predictor across the majority of current VLAs. Whether implemented via autoregressive token bins, L1 regression, or flow-matching denoising, the resulting decoder treats the action space as unstructured, leaving the geometric proximity of neighboring actions unexploited during training. To advance this, we introduce ActionMap, a voxel heatmap action head that drops into an existing VLA in place of its native action decoder. For each new action, the head predicts a voxel heatmap over the action space, where each voxel directly stores the probability of the corresponding action. Across LIBERO simulation and real-world Franka manipulation, our heatmap head surpasses two architecturally distinct backbones at matched training steps (e.g., +8.2% over OpenVLA-OFT's L1 regression head on the LIBERO four-suite average), converges at comparable or faster rates on both backbones, and remains markedly more data-efficient at low training data. The cross-backbone consistency indicates that action representation is a real lever for VLA performance, distinct from further backbone or recipe scaling. Project Page: https://github.com/showlab/ActionMap.

</details>

---

### [[20_Research/Papers/大模型/Stream3D-VLM_Online_3D_Spatial_Understanding_with_Incremental_Geometry_Priors|Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors]]

![[assets/2606.06891_figure.png|800]]

- **arXiv**: [2606.06891](https://arxiv.org/abs/2606.06891)
- **PDF**: https://arxiv.org/pdf/2606.06891
- **详细分析**: [[20_Research/Papers/大模型/Stream3D-VLM_Online_3D_Spatial_Understanding_with_Incremental_Geometry_Priors|Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors]]
- **作者**: Hanxun Yu, Xuan Qu, Lei Ke, Boqiang Zhang, Yuxin Wang, Jianke Zhu, Dong Yu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Stream3D-VLM: Online 3D Spatial Understanding with Incremental Geometry Priors》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OST-Bench, ScanNet, Stream3D-Bench, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite advances in 3D scene understanding, existing 3D Large Multimodal Models operate in offline settings, requiring complete scene observations or predefined video clips. In this paper, we present an online 3D vision-language model that enables real-time spatial understanding from streaming video. Our approach adopts an autoregressive streaming control modeling based on the LLM's next-token prediction objective to learn when to respond, and employs a lightweight Visual-Spatial Feature Integration (VSFI) module to incrementally inject temporally aligned geometry priors into the visual stream. To alleviate long-context decoding overhead, we propose a plug-and-play Geometry-Adaptive Voxel Compression (GAVC) module for efficient visual token compression. To address the scarcity of streaming 3D-language data, we further develop a scalable data generation pipeline that curates over 1M online spatio-temporal 3D QA pairs and establishes a comprehensive benchmark spanning 29 tasks. Extensive experiments show that our approach significantly outperforms both proprietary and open-source models across online and offline 3D spatial understanding, reasoning, and grounding tasks. The project page is available at https://stream3d-vlm.github.io/

</details>

---

### [[20_Research/Papers/具身智能/A_Cross-view_Fusion_Framework_for_Robust_6-DoF_Grasp_Pose_Estimation|A Cross-view Fusion Framework for Robust 6-DoF Grasp Pose Estimation]]

![[assets/2606.06878_figure.png|800]]

- **arXiv**: [2606.06878](https://arxiv.org/abs/2606.06878)
- **PDF**: https://arxiv.org/pdf/2606.06878
- **详细分析**: [[20_Research/Papers/具身智能/A_Cross-view_Fusion_Framework_for_Robust_6-DoF_Grasp_Pose_Estimation|A Cross-view Fusion Framework for Robust 6-DoF Grasp Pose Estimation]]
- **作者**: Kangjian Zhu, Haobo Jiang, Jianjun Qian, Jin Xie
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《A Cross-view Fusion Framework for Robust 6-DoF Grasp Pose Estimation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GSNet, GraspNet, PointNet, ResUNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose a cross-view fusion framework that enhances the robustness of 6-DoF grasp pose estimation in corner views. Our framework alleviates occlusion by incorporating an auxiliary view and avoids the time-consuming, task-agnostic multi-view reconstruction through a post-fusion strategy. To enhance cross-view fusion, we propose a self-supervised contrastive learning strategy that leverages cross-view associations to regularize point cloud features. In brief, a cross-view point pair is considered a match if the two points correspond to the same 3D location, and a non-match if they represent distinct grasp directions. The learning strategy significantly enhances the spatial consistency and direction distinctiveness of point features, thereby facilitating cross-view fusion and improving estimation robustness. Furthermore, we propose a cross-view-aligned cylinder integration module to fuse grasp-relevant geometry into a comprehensive representation. Specifically, the module first aligns the cross-view points and features according to their similarity to enhance the robustness against noise. Subsequently, these points are registered into the cylindrical coordinate frame, emphasizing the rotation-symmetric geometry which is important for grasping. Finally, local self-attention and seed cross-attention layers are alternately employed, respectively enabling interactions within single views and across views, which supports fine-grained representation of grasp-relevant geometry. Our framework achieves strong performance on the GraspNet-1Billion benchmark and in real-world applications. Code is available at https://github.com/KJZhuAutomatic/Cross-view-Grasp.

</details>

---

### [[20_Research/Papers/强化学习/AdaGRPO_A_Capability-Aware_Adaptive_Enhancement_for_Flow-based_GRPO|AdaGRPO: A Capability-Aware Adaptive Enhancement for Flow-based GRPO]]

![[assets/2606.06828_figure.png|800]]

- **arXiv**: [2606.06828](https://arxiv.org/abs/2606.06828)
- **PDF**: https://arxiv.org/pdf/2606.06828
- **详细分析**: [[20_Research/Papers/强化学习/AdaGRPO_A_Capability-Aware_Adaptive_Enhancement_for_Flow-based_GRPO|AdaGRPO: A Capability-Aware Adaptive Enhancement for Flow-based GRPO]]
- **作者**: Jiazi Bu, Pengyang Ling, Yujie Zhou, Yibin Wang, Yuhang Zang, Tianyi Wei, Xiaohang Zhan, Jiaqi Wang, Tong Wu, Xingang Pan, Dahua Lin
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.72（加权：强化学习 0.56，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《AdaGRPO: A Capability-Aware Adaptive Enhancement for Flow-based GRPO》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ProCuRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Group Relative Policy Optimization (GRPO) has demonstrated remarkable success in aligning text-to-image (T2I) flow models with human preferences. However, we have identified that the learning loop of current flow-based GRPO is fundamentally decoupled from the learner's current capability, suffering from critical blind spots at both prompt selection and advantage estimation: (i) Existing methods sample prompts randomly, overlooking the substantial impact of data selection on reinforcement learning (RL) efficacy--a factor proven crucial in GRPO for large language models; (ii) They evaluate sample quality solely relying on intra-group statistics, lacking a global perspective to accurately measure true policy improvement. To address these issues, we propose Adaptive GRPO (AdaGRPO), a novel capability-aware RL algorithm tailored for flow models. Specifically, AdaGRPO consists of two principal components: (i) Online Curriculum Filtering Strategy: Dynamically tracks the model's proficiency and adaptively selects prompts that best match its current learning boundary; (ii) Cross-Level Advantage Fusion: Synergistically integrates fine-grained intra-group advantages with macro-level global advantages, providing a comprehensive and unbiased policy evaluation. As a lightweight, plug-and-play module, AdaGRPO can be seamlessly integrated with existing frameworks such as Flow-GRPO, DanceGRPO, and Flow-CPS. Extensive experiments demonstrate that AdaGRPO consistently drives performance gains while significantly stabilizes GRPO training for flow models.

</details>

---

### [[20_Research/Papers/强化学习/VideoSEG-O3_A_Multi-turn_Reinforcement_Learning_Framework_for_Reasoning_Video_Object_Segmentation|VideoSEG-O3: A Multi-turn Reinforcement Learning Framework for Reasoning Video Object Segmentation]]

![[assets/2606.06819_figure.png|800]]

- **arXiv**: [2606.06819](https://arxiv.org/abs/2606.06819)
- **PDF**: https://arxiv.org/pdf/2606.06819
- **详细分析**: [[20_Research/Papers/强化学习/VideoSEG-O3_A_Multi-turn_Reinforcement_Learning_Framework_for_Reasoning_Video_Object_Segmentation|VideoSEG-O3: A Multi-turn Reinforcement Learning Framework for Reasoning Video Object Segmentation]]
- **作者**: Ming Dai, Sen Yang, Boqiang Duan, Boyuan Tong, Jiedong Zhuang, Wankou Yang, Jingdong Wang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《VideoSEG-O3: A Multi-turn Reinforcement Learning Framework for Reasoning Video Object Segmentation》归入 强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Post-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning Video Object Segmentation (RVOS) demands a sophisticated integration of temporal dynamics, spatial details, and linguistic reasoning to achieve precise pixel-level localization. Existing methods are limited to reasoning over fixed initial inputs and lack the capacity to actively acquire further visual evidence, which is often essential for resolving complex references in long or intricate videos. To address this, we propose \textbf{VideoSEG-O3}, the first multi-turn reinforcement learning framework for RVOS that emulates the human \textit{``coarse-to-fine''} cognitive process. It employs a \textit{multi-turn temporal-spatial chain-of-thought} to capture fine-grained details by iteratively pinpointing critical intervals and keyframes. Additionally, to enable the policy to perceive segmentation quality beyond mere text probability of \texttt{[SEG]} during the RL stage, we introduce \textit{SEG-aware logit calibration}, which integrates pixel-wise segmentation feedback directly into the token-level logits. Furthermore, we design a \textit{decoupled thinking trace} to hierarchically decompose the reasoning process into temporal, spatial, and linguistic dimensions, and construct \textbf{VTS-CoT}, a specialized cold-start dataset featuring comprehensive reasoning trajectories. The code and models will be released at https://github.com/Dmmm1997/VideoSEG-O3.

</details>

---

### [[20_Research/Papers/机器人/USU-Corn-WeedDB_A_UAV_RGB_Image_Dataset_for_Multi-Species_Weed_Detection_in_Forage_Corn|USU-Corn-WeedDB: A UAV RGB Image Dataset for Multi-Species Weed Detection in Forage Corn]]

![[assets/2606.06709_first_page.png|800]]

- **arXiv**: [2606.06709](https://arxiv.org/abs/2606.06709)
- **PDF**: https://arxiv.org/pdf/2606.06709
- **详细分析**: [[20_Research/Papers/机器人/USU-Corn-WeedDB_A_UAV_RGB_Image_Dataset_for_Multi-Species_Weed_Detection_in_Forage_Corn|USU-Corn-WeedDB: A UAV RGB Image Dataset for Multi-Species Weed Detection in Forage Corn]]
- **作者**: Utsav Bhandari, Saroj Burlakoti, Rhonda Miller, Sierra Young, Eric Westra, Aaron Etienne
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 1.0（加权：机器人 1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《USU-Corn-WeedDB: A UAV RGB Image Dataset for Multi-Species Weed Detection in Forage Corn》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Weed pressure in forage corn production causes yield losses of up to 31.5%, yet site-specific weed management (SSWM) systems built on UAV imagery and deep learning remain constrained by the scarcity of field-representative training datasets. We present USU-Corn-WeedDB, a publicly available UAV RGB image dataset collected from a commercial forage corn field in Cache Valley, Utah, designed to support multi-class weed detection under both supervised and semi-supervised learning frameworks. RGB imagery was acquired on 27 June 2025 using an Autel EVO II Dual 640T V2 drone at ~10m above ground level, yielding a ground sampling distance of approximately 0.48 cm/pixel. A total of 366 full-resolution images were tiled into 8,800 patches at 640 x 640-pixel resolution. Of these, 800 images were manually annotated for three weed species; common lambsquarters (Chenopodium album), redroot pigweed (Amaranthus retroflexus), and green foxtail (Setaria viridis) comprising 10,539 bounding-box instances, with the remaining 8,000 tiles retained as an unlabeled pool for semi-supervised experiments. This dataset reflects a natural class imbalance where redroot pigweed constitutes 53.86% of annotated instances, which was preserved intentionally to mirror real field conditions. To validate dataset utility, we trained 28 object detection models spanning five architecture families including YOLOv8, YOLOv9, YOLOv10, YOLO11, YOLO26, and RT-DETR under identical conditions without hyperparameter tuning. Test set mAP@0.5 ranged from 0.773 to 0.840, with lightweight models achieving competitive performance relevant to edge-deployed UAV systems. USU-Corn-WeedDB is publicly available at https://doi.org/10.5281/zenodo.20044178.

</details>

---
