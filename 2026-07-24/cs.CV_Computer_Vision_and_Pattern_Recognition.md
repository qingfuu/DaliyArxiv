# cs.CV | Computer Vision and Pattern Recognition | 2026-07-24

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/世界模型/Streaming_Multi-Agent_Autoregressive_Diffusion_Model_with_World_State_Registers|Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers]]

![[assets/2607.21594_figure.png|800]]

- **arXiv**: [2607.21594](https://arxiv.org/abs/2607.21594)
- **PDF**: https://arxiv.org/pdf/2607.21594
- **详细分析**: [[20_Research/Papers/世界模型/Streaming_Multi-Agent_Autoregressive_Diffusion_Model_with_World_State_Registers|Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers]]
- **作者**: Sicheng Mo, Yuheng Li, Ziyang Leng, Krishna Kumar Singh, Bolei Zhou
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 世界模型
- **相关性评分**: 0.7（加权：大模型 0.5，世界模型 0.2）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Streaming Multi-Agent Autoregressive Diffusion Model with World State Registers》归入 大模型、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent interactive world models should not only generate consistent observations, but also maintain world states that persist across agents and evolve across views. Existing autoregressive video diffusion pipelines carry forward observation history as conditioning context, which makes shared state difficult to maintain in multi-agent and multi-view settings. We present WorldWeaver (W^2), a streaming multi-agent video diffusion model that augments rollout with cross-agent world state registers: learnable tokens that store shared world information, track individual agent status, and are dynamically updated after each generated chunk. We ground these registers with supervision signals spanning individual agent status, global state views including bird's-eye views, and scene text. We further improve the architecture with a Mixture-of-Transformers design that uses separate weights for world state modeling and visual frame modeling. Extensive experiments in two-agent Minecraft video generation show that explicit world-state modeling improves logical consistency and generation quality.

</details>

---

### [[20_Research/Papers/具身智能/Scale_Up_Strategically_Learning_Compositional_Generalization_via_Bias-Aware_Evaluation_and_Data_Collection_for_Robotic_Manipulation|Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation]]

![[assets/2607.21582_figure.png|800]]

- **arXiv**: [2607.21582](https://arxiv.org/abs/2607.21582)
- **PDF**: https://arxiv.org/pdf/2607.21582
- **详细分析**: [[20_Research/Papers/具身智能/Scale_Up_Strategically_Learning_Compositional_Generalization_via_Bias-Aware_Evaluation_and_Data_Collection_for_Robotic_Manipulation|Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation]]
- **作者**: Yu Qi, Zhang Ye, Xinyi Xu, Yuxuan Lu, Amitoj Sandhu, Boce Hu, Haojie Huang, Jonathan Tremblay, Lawson L. S. Wong
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Scale Up Strategically: Learning Compositional Generalization via Bias-Aware Evaluation and Data Collection for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, XVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compositional generalization is essential for robot to follow diverse instructions. However, pretrained policies are known to take shortcuts, deferring to salient cues rather than grounding language. We introduce a diagnostic framework that localizes this failure to individual \textit{instruction factors}, \textit{e.g.,} reusable semantic components such as color, verb, object, size, and spatial attribute. Our framework formalizes instruction factor bias, the tendency of fine-tuned policies to over-rely on dominant factors as shortcuts, and quantifies it through two metrics: Factor Dominance Rate (FDR), capturing pairwise bias between factors, and Factor Dominance Hierarchy (FDH), aggregating these into a global ranking. Evaluation on six foundation policies reveals broadly consistent ordering, \textit{i.e.}, color $\geq$ object $\geq$ spatial $\geq$ verb $\geq$ size, with color dominant, and verb and size most under-grounded. We further show the diagnosis is actionable: a bias-aware data collection strategy that reallocates a fixed budget toward under-grounded factors outperforms baselines in simulation and on a real robot using half the demonstrations, thereby enabling more sample-efficient and generalizable policy learning.

</details>

---

### [[20_Research/Papers/具身智能/DAPM_UAV_Monocular_Depth_Estimation_from_Any_Height,_Pitch,_Roll_and_FOV|DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV]]

![[assets/2607.21438_figure.jpg|800]]

- **arXiv**: [2607.21438](https://arxiv.org/abs/2607.21438)
- **PDF**: https://arxiv.org/pdf/2607.21438
- **详细分析**: [[20_Research/Papers/具身智能/DAPM_UAV_Monocular_Depth_Estimation_from_Any_Height,_Pitch,_Roll_and_FOV|DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV]]
- **作者**: Tong Ling, Wenhui Diao, Yingchao Feng, Hanbo Bi, Zhongyan Hou, Xian Sun
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《DAPM: UAV Monocular Depth Estimation from Any Height, Pitch, Roll and FOV》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirSim, HSC-Net, PoseNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular depth estimation is a fundamental prerequisite for 3D reconstruction and autonomous navigation in Unmanned Aerial Vehicles (UAVs). In practical deployments, UAVs operate under highly dynamic camera poses characterized by continuous variations in height, pitch, roll, and field of view (FOV). Existing monocular depth estimation methods frequently fail to generalize across such diverse perspectives and the expansive scale of depth distributions inherent in aerial scenes. To address these challenges, we establish a quantitative representation of UAV viewing angles through rigorous theoretical analysis, deriving the geometric correspondence between viewing angles and view distances using the ground plane as a reference for observation. Building upon this, we propose Depth Estimation for Any Perspectives Model (DAPM), representing the first monocular framework specifically designed for UAV aerial imagery to jointly estimate camera pose and depth under continuously varying viewpoints. Specifically, we introduce an Ideal Ground Depth (IGD) module that leverages the derived geometric relationships between UAV perspectives and view distances to implement dense camera-pose supervision and enhance depth features. And we further develop a coarse-to-fine Progressive Quantization Bins (PQB) module. By incorporating progressive supervision and hierarchical quantization bins, the PQB module enables robust estimation in complex UAV aerial imagery. To evaluate the proposed framework, we present the UAV Any Perspectives Depth (UAPD) dataset, featuring comprehensive and continuous distributions of pose parameters. Experimental results on UAPD demonstrate that DAPM achieves state-of-the-art performance across both depth and camera-pose estimation metrics. The source code and datasets are available at: https://github.com/ThisIsLT/DAPM.

</details>

---

### [[20_Research/Papers/机器人/GLAM-SLAM_Real-time_Gaussian_Large-scale_Mapping_via_Flow_Densification_and_Spatial_Decomposition|GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition]]

![[assets/2607.21416_figure.jpg|800]]

- **arXiv**: [2607.21416](https://arxiv.org/abs/2607.21416)
- **PDF**: https://arxiv.org/pdf/2607.21416
- **详细分析**: [[20_Research/Papers/机器人/GLAM-SLAM_Real-time_Gaussian_Large-scale_Mapping_via_Flow_Densification_and_Spatial_Decomposition|GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition]]
- **作者**: Panagiotis Mermigkas, Argyris Manetas, Petros Maragos
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《GLAM-SLAM: Real-time Gaussian Large-scale Mapping via Flow Densification and Spatial Decomposition》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing Gaussian-splatting-based monocular Simultaneous Localization and Mapping (SLAM) systems are either tailored to short sequences, are not real-time, or suffer from prohibitive GPU memory requirements, limiting their applicability in realistic, long-horizon scenarios. To address this, we present GLAM-SLAM, a real-time, decoupled Gaussian-splatting SLAM system designed for large-scale outdoor scenes. We ensure lightweight tracking using a robust, feature-based SLAM frontend, while for mapping, we adopt a structured, sparse anchor grid representation that ensures scalable operation and maintains scene coherence across long-term sequences. To satisfy the dense initialization requirements of 3D Gaussian Splatting (3DGS), we introduce a geometry-based flow-densification anchoring strategy using epipolar constraints. Furthermore, by treating mapping as a multi-scene problem, we propose a scene-partitioning strategy that introduces a strong spatial inductive bias via MLP initializations to generate localized Gaussians. We evaluate our system on the challenging, long-sequence KITTI Odometry, Oxford RobotCar, and M'alaga datasets. Extensive ablations and comparisons demonstrate a 15% improvement in reconstruction quality over the second-best performer, while maintaining real-time performance and the ability to scale to longer sequences. Code is publicly available for the benefit of the community.

</details>

---

### [[20_Research/Papers/机器人/HGeo-TopoMap_Boosting_Topological_Mapping_with_Hierarchical_Geometric_Priors|HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors]]

![[assets/2607.21281_figure.png|800]]

- **arXiv**: [2607.21281](https://arxiv.org/abs/2607.21281)
- **PDF**: https://arxiv.org/pdf/2607.21281
- **详细分析**: [[20_Research/Papers/机器人/HGeo-TopoMap_Boosting_Topological_Mapping_with_Hierarchical_Geometric_Priors|HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors]]
- **作者**: Siyu Li, Kunyu Peng, Di Wen, Beiping Hou, Zhiyong Li, Kailun Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《HGeo-TopoMap: Boosting Topological Mapping with Hierarchical Geometric Priors》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AerialFusionMapNet, LaneSegNet, TopoNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Topological maps are key outputs of autonomous driving perception systems, delivering essential road information for path planning. They identify instances such as centerlines and traffic signs, along with their connectivity relationships. Due to the lack of explicit markings for centerlines in real-world environments, the detection of centerline instances remains a significant challenge. To tackle this problem, we propose HGeo-TopoMap, which leverages an explicit prior map and implicit spatial relations to hierarchically boost topological mapping. First, a geometric adaptive learning module is designed for the road structure map obtained via inverse perspective mapping. This module discretely encodes semantic and spatial features from the map, followed by a prior-mask attention mechanism that selectively focuses on informative regions. Then, a geometric consistency learning module is devised, which leverages the geometric properties and spatial relationships of centerlines. Built on the geometry-aware decoder, it enforces spatial consistency by aligning features of centerline instances with identical geometric orientations. The proposed method is evaluated on the OpenLane-V2 dataset across the centerline, lane segment, and robustness benchmarks. Beyond substantial improvements in topological mapping accuracy, the proposed method offers the benefit of enhanced robustness, consistently outperforming baselines under both standard and challenging conditions. The source code and model weights will be made publicly available at https://github.com/lynn-yu/HGeo-TopoMap.

</details>

---

### [[20_Research/Papers/具身智能/TransBiolab_A_Real-World_Multi-View_Dataset_of_Cluttered_Transparent_Biomedical_Objects|TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects]]

![[assets/2607.21071_figure.png|800]]

- **arXiv**: [2607.21071](https://arxiv.org/abs/2607.21071)
- **PDF**: https://arxiv.org/pdf/2607.21071
- **详细分析**: [[20_Research/Papers/具身智能/TransBiolab_A_Real-World_Multi-View_Dataset_of_Cluttered_Transparent_Biomedical_Objects|TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects]]
- **作者**: Ke Ma, Yifei Wang, Meng Wang, Tian Xia
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《TransBiolab: A Real-World Multi-View Dataset of Cluttered Transparent Biomedical Objects》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GraspNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous biomedical laboratories increasingly rely on visual perception to recognize, localize, and manipulate transparent plasticware, yet high-quality real-world datasets for this setting remain limited. The scarcity of domain-relevant data is particularly restrictive in cluttered multi-object scenes, where mutual occlusion and view-dependent appearance changes remain challenging even for contemporary visual foundation models. Existing transparent-object datasets have advanced segmentation, depth, and pose estimation, but they usually do not evaluate the combined setting of multi-object clutter, occlusion, and calibrated multi-view capture that characterizes real laboratory manipulation scenes. To address this gap, we present TrainsBiolab, a real-world RGB-D dataset of cluttered transparent biomedical objects captured as calibrated multi-view sequences. TrainsBiolab contains 161,315 frames from 98 scenes and 1.03M instance annotations over 15 laboratory object types, including 6D poses, full and visible masks, depth, and per-frame camera calibration. The dataset is organized along three axes that reflect operational difficulty: object category, the total number of objects in a frame, and camera viewpoint. We further define dataset-centric benchmarks for segmentation, depth estimation and completion, and 6D pose estimation, and report a system-level robot manipulation evaluation enabled by the released annotations and calibrations. By focusing on repeated transparent instances, clutter, and multi-view laboratory capture, TrainsBiolab provides a resource for segmentation, depth estimation, 6D pose estimation, and multi-view reasoning in autonomous laboratory manipulation. Project page: https://dualtransparency.github.io/TransBiolab/.

</details>

---

### [[20_Research/Papers/机器人/A_real-time_RGB-D_perception_pipeline_for_autonomous_impact_hammers_in_mining_self-filtering,_rock_segmentation_and_rock-breaking_poses_gene|A real-time RGB-D perception pipeline for autonomous impact hammers in mining: self-filtering, rock segmentation and rock-breaking poses generation]]

![[assets/2607.20748_figure.png|800]]

- **arXiv**: [2607.20748](https://arxiv.org/abs/2607.20748)
- **PDF**: https://arxiv.org/pdf/2607.20748
- **详细分析**: [[20_Research/Papers/机器人/A_real-time_RGB-D_perception_pipeline_for_autonomous_impact_hammers_in_mining_self-filtering,_rock_segmentation_and_rock-breaking_poses_gene|A real-time RGB-D perception pipeline for autonomous impact hammers in mining: self-filtering, rock segmentation and rock-breaking poses generation]]
- **作者**: Martín Gallegos, Francisco Leiva, Patricio Loncomilla, Michelle Cortés, Javier Ruiz-del-Solar
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《A real-time RGB-D perception pipeline for autonomous impact hammers in mining: self-filtering, rock segmentation and rock-breaking poses generation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RockyCenterNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Impact hammers, also known as rock-breakers, are essential machines in mining operations, where they perform secondary reduction. In underground mining, these machines are typically teleoperated, limiting operational efficiency. This paper presents a real-time RGB-D perception pipeline as a step towards automating the operation of hydraulic impact hammers used in mining. The proposed system simultaneously generates operationally feasible rock-breaking poses and a robot-free 3D representation of the workspace. The proposed approach combines image-based instance segmentation with geometric point cloud processing, and operates on embedded hardware at approximately 10 Hz with a total latency of around 675 ms, enabling responsive closed-loop behavior when integrated with a control system. Experimental results in a representative scaled scenario demonstrate that the proposed system is suitable for real-time autonomous impact hammer operation.

</details>

---

### [[20_Research/Papers/具身智能/PhysCoRe_Physics-Corrected_Residual_World_Models_for_Material-Aware_Deformable_Dynamics|PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics]]

![[assets/2607.20653_figure.png|800]]

- **arXiv**: [2607.20653](https://arxiv.org/abs/2607.20653)
- **PDF**: https://arxiv.org/pdf/2607.20653
- **详细分析**: [[20_Research/Papers/具身智能/PhysCoRe_Physics-Corrected_Residual_World_Models_for_Material-Aware_Deformable_Dynamics|PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics]]
- **作者**: Haocheng Yin, Shuohan Tao, Yongsheng Chen, Lu Gan
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.22（加权：具身智能 0.6，强化学习 0.16，世界模型 0.96，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《PhysCoRe: Physics-Corrected Residual World Models for Material-Aware Deformable Dynamics》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting how deformable objects evolve under robotic manipulation is a longstanding challenge. Existing approaches typically rely on per-object optimization to fit material parameters, which can be slow and cannot generalize, while end-to-end learned alternatives extrapolate poorly and often violate basic physical structure. We present PhysCoRe, a physics-corrected residual world model that couples a differentiable Material Point Method (MPM) simulator with two feed-forward neural networks. A material refinement module, Material from Motion (MfM), infers per-particle elasticity from visual observations, grounding the simulator in object-specific physics. A residual correction module, Residual from Dynamics (RfD), learns the discrepancy and predicts corrections to the simulator's internal dynamics, absorbing systematic biases that the analytical model cannot capture. This design also supports online material identification on novel objects. MfM adapts from limited interactions, and its predictive uncertainty steers further exploration toward the regions where its estimate is least confident. Experiments on real deformable-object manipulation sequences show that PhysCoRe outperforms state-of-the-art baselines in prediction accuracy, and that its predicted confidence forms a reliable distribution across the object's geometry, providing a natural signal for future confidence-guided exploration.

</details>

---
