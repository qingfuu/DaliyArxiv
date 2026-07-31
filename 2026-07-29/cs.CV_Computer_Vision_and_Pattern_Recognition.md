# cs.CV | Computer Vision and Pattern Recognition | 2026-07-29

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/大模型/VetClaw_An_Edge-Cloud_Multimodal_Agentic_System_for_Veterinary_Disease_Screening|VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening]]

![[assets/2607.26042_figure.png|800]]

- **arXiv**: [2607.26042](https://arxiv.org/abs/2607.26042)
- **PDF**: https://arxiv.org/pdf/2607.26042
- **详细分析**: [[20_Research/Papers/大模型/VetClaw_An_Edge-Cloud_Multimodal_Agentic_System_for_Veterinary_Disease_Screening|VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening]]
- **作者**: Syed Mhamudul Hasan, Anas AlSobeh, Hussein Zangoti, Abdur R. Shahid
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《VetClaw: An Edge-Cloud Multimodal Agentic System for Veterinary Disease Screening》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present VetClaw, an edge-cloud multimodal agentic system for early veterinary disease screening. VetClaw uses a camera module as an edge sensing device and sends captured images, together with optional symptom descriptions, to a server-hosted vision-language model for zero-shot disease classification. The system separates agent interaction from workflow orchestration: OpenClaw provides scheduling, tool access, user interaction, and notification services on the edge device, while LangGraph manages the stateful screening workflow, including input validation, image transmission, model invocation, safety checks, conditional routing, failure handling, and structured logging. This design moves beyond static image classification by enabling the system to collect visual evidence, invoke external models, apply deterministic safety rules, and generate diagnostic-support alerts. Results show that image-only VLM prediction remains limited, whereas symptom-guided and multimodal inputs improve zero-shot classification performance. Thus, VetClaw transforms a static prediction model into a coordinated, safety-aware system that can use tools, manage workflows, handle failures, and escalate uncertain cases.

</details>

---

### [[20_Research/Papers/世界模型/Wonder_Video_World_Model_Done_Better|Wonder: Video World Model Done Better]]

![[assets/2607.26037_figure.png|800]]

- **arXiv**: [2607.26037](https://arxiv.org/abs/2607.26037)
- **PDF**: https://arxiv.org/pdf/2607.26037
- **详细分析**: [[20_Research/Papers/世界模型/Wonder_Video_World_Model_Done_Better|Wonder: Video World Model Done Better]]
- **作者**: Jiacong Xu, Hanwen Jiang, Zhixin Shu, Kalyan Sunkavalli, Vishal M. Patel, Yiqun Mei
- **cs 子类**: cs.CV, cs.GR
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: WorldModel, ComputerVision, Systems

#### 研究背景与动机

《Wonder: Video World Model Done Better》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DreamX-World, Inspatio-World, LingBot-World, MineWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Wonder, a general-purpose video world model for real-time, camera-controllable world exploration. Given an image or a conditional video, Wonder constructs a playable world where users can navigate interactively by moving the camera, discovering unseen regions, and revisiting previously observed areas in real time and over a long-term horizon. Achieving this capability requires a system-level co-design of control method, memory mechanism, and training strategy. We introduce a novel camera conditioning with a dense coordinate field whose renderings provide spatially aligned motion and orientation cues, allowing the model to interpret camera motion directly as visual evidence. To support fast and precise memory retrieval over a growing generation context, we propose an efficient sparse attention-based memory mechanism, enabling the model to selectively attend to a small set of relevant context tokens at inference time, regardless of actual context length. We further develop several techniques to rectify the self-forcing-style distillation pipeline, improving the student model's ability to respect control signals, as well as maintaining diverse generation modes and long-term memory from the teacher. Together, these components enable Wonder to synthesize diverse, minute-scale videos at 16 FPS while preserving coherent geometry, appearance, and dynamics across long rollouts. Beyond image-to-video generation, Wonder naturally supports video-conditioned generation, allowing existing dynamic scenes to be re-shot in real time.

</details>

---

### [[20_Research/Papers/具身智能/HiFi-UMI_Learning_Deployable_Manipulation_Policies_from_High-Fidelity_UMI_Data_Alone|HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone]]

![[assets/2607.25895_figure.png|800]]

- **arXiv**: [2607.25895](https://arxiv.org/abs/2607.25895)
- **PDF**: https://arxiv.org/pdf/2607.25895
- **详细分析**: [[20_Research/Papers/具身智能/HiFi-UMI_Learning_Deployable_Manipulation_Policies_from_High-Fidelity_UMI_Data_Alone|HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone]]
- **作者**: Simple AI, :, Yuteng Wei, Jinming Ma, Jiawei Wang, Weitao Zhou, Yushen Zuo, Ke Rui, Minglei Li, Jinhao Zhang, Zhikang Pan, Xiang Wang...
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《HiFi-UMI: Learning Deployable Manipulation Policies from High-Fidelity UMI Data Alone》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning deployable manipulation policies is bottlenecked by the scarcity of data that is both high-fidelity and scalable. Real-robot teleoperation is accurate but costly to scale; robot-free UMI capture scales readily, and current practice uses the resulting data mainly for pre-training, adding a small real-robot "anchor" at post-training. We ask whether raising the fidelity of robot-free UMI data, rather than shrinking the real-robot fraction, can remove that anchor. We present HiFi-UMI, a portable UMI data-production system co-designed for trajectory accuracy, inter-gripper relative pose, synchronization, and field of view: head-mounted offline stereo-inertial SLAM, native rather than reconstructed relative pose, a shared microsecond GPIO trigger, and two wide-angle cameras per hand covering ~200 degrees. It reaches 3 mm workspace-local end-effector accuracy without external tracking infrastructure. Using this corpus, we demonstrate zero-robot post-training: a policy post-trained solely on HiFi-UMI demonstrations deploys directly on a real robot and matches in-domain teleoperation across three backbones spanning the vision-language-action and world-action-model families, with success-rate differences of -2.5, +3.1, and -0.6 percentage points on StarVLA-QwenPI, OpenPI-pi_0.5, and LingBot-VA; the strongest policy reaches 85% on a precision insertion task, even though the teleoperation baseline is collected in the evaluation scene and no HiFi-UMI trajectory is. Pre-training on 4,000 hours from the same corpus lowers action error on ten unseen tasks by 41% and, on StarVLA-QwenPI, raises real-robot success by a further 18.1 percentage points. We open-source HiFi-UMI-2K, 2,000 hours of microsecond-synchronized, ultra-wide-FoV demonstrations, each automatically reconstructed and validated through simulation replay, as a large-scale, high-fidelity resource for the robot-learning community.

</details>

---

### [[20_Research/Papers/大模型/Food_Image_Segmentation_with_LLM-Derived_Ingredient_Labels_and_Multimodal_Fusion|Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion]]

![[assets/2607.25820_figure.png|800]]

- **arXiv**: [2607.25820](https://arxiv.org/abs/2607.25820)
- **PDF**: https://arxiv.org/pdf/2607.25820
- **详细分析**: [[20_Research/Papers/大模型/Food_Image_Segmentation_with_LLM-Derived_Ingredient_Labels_and_Multimodal_Fusion|Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion]]
- **作者**: Jui-Feng Chi, Wei-Ta Chu, Sheng-Long Lin
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Food Image Segmentation with LLM-Derived Ingredient Labels and Multimodal Fusion》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, K-Net, PSPNet, UPerNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Food image segmentation plays a vital role in health-related applications such as nutrition tracking and personalized health monitoring. However, existing models often underperform on visually similar ingredients and rare food categories. To address this issue, we propose two plug-and-play multimodal modules that enhance the segmentation performance by leveraging ingredient labels inferred from food images using large language models (LLMs). The first module, called LIM-F (Language Injection Module for Features), is designed to pair with any image encoder that produces multi-layer outputs (e.g., Swin Transformer), while the second module, LIM-Q (Language Injection Module for Queries), targets Mask2Former-style Transformer-based decoders. Both modules enable training without the need for pre-aligning images with text by directly injecting semantic ingredient information into the visual analysis pipeline. On the FoodSeg103 benchmark, the proposed method achieves state-of-the-art performance. Specifically, integrating LIM-Q into the Mask2Former decoder with a Swin-L image encoder yields a mean Intersection over Union (mIoU) of 55.0. LIM-F also demonstrates strong generalization and competitive performance, reaching an mIoU of 54.4 under the same model (Swin-L+Mask2Former). Furthermore, its applicability extends beyond Transformer-based decoders, as evidenced by an improvement from 47.7 to 49.8 mIoU when integrated into a CNN-based architecture. Notably, the improved segmentation accuracy is achieved with only a moderate (at most 3.8 GB) increase in the GPU memory consumption during training. Thus, the proposed approach offers a practical and scalable solution for fine-grained food understanding.

</details>

---

### [[20_Research/Papers/多模态技术/GeoMFD_Continual_Drone-View_Geo-Localization_with_Geometry-Aware_Adapter_and_Margin-Field_Distillation|GeoMFD: Continual Drone-View Geo-Localization with Geometry-Aware Adapter and Margin-Field Distillation]]

![[assets/2607.25788_figure.png|800]]

- **arXiv**: [2607.25788](https://arxiv.org/abs/2607.25788)
- **PDF**: https://arxiv.org/pdf/2607.25788
- **详细分析**: [[20_Research/Papers/多模态技术/GeoMFD_Continual_Drone-View_Geo-Localization_with_Geometry-Aware_Adapter_and_Margin-Field_Distillation|GeoMFD: Continual Drone-View Geo-Localization with Geometry-Aware Adapter and Margin-Field Distillation]]
- **作者**: Zhongwei Chen, Hai-jun Rong, Tao Zhang, Xianfeng Nie, Xiangbao Zhang, Guoqi Li, Zhao-Xu Yang
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: cs.CV

#### 研究背景与动机

《GeoMFD: Continual Drone-View Geo-Localization with Geometry-Aware Adapter and Margin-Field Distillation》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing drone-view geo-localization (DVGL) methods are mainly developed under a static training paradigm, where models are optimized for fixed environments with all training data available in advance. However, this paradigm is difficult to extend to real-world deployment, where drones may encounter diverse environments and require multiple environment-specific models, resulting in additional storage and model-selection costs. Directly adapting a single model to new environments also risks distorting previously learned cross-view embedding geometry and causing forgetting. To address these challenges, we formalize the continual drone-view geo-localization (C-DVGL) setting and propose GeoMFD, a geometry-aware continual adaptation method for DVGL. GeoMFD combines a cold-start bootstrapping strategy (CBS), a geometry-aware adapter (Geo-Adapter), and margin-field distillation (MFD) to balance adaptation and cross-view geometry preservation. CBS initializes a stable embedding space, Geo-Adapter enables environment adaptation through controlled residual corrections, and MFD preserves similarity margins between positive pairs and hard negatives to alleviate cross-view geometry forgetting. Extensive experiments demonstrate that GeoMFD effectively mitigates forgetting and achieves competitive performance with environment-specific DVGL methods using a single continuously updated model.

</details>

---

### [[20_Research/Papers/多模态技术/A_Unified_Benchmark_and_Modality-Adaptive_Network_for_Day-and-Night_Drone-View_Geo-Localization|A Unified Benchmark and Modality-Adaptive Network for Day-and-Night Drone-View Geo-Localization]]

![[assets/2607.25778_figure.png|800]]

- **arXiv**: [2607.25778](https://arxiv.org/abs/2607.25778)
- **PDF**: https://arxiv.org/pdf/2607.25778
- **详细分析**: [[20_Research/Papers/多模态技术/A_Unified_Benchmark_and_Modality-Adaptive_Network_for_Day-and-Night_Drone-View_Geo-Localization|A Unified Benchmark and Modality-Adaptive Network for Day-and-Night Drone-View Geo-Localization]]
- **作者**: Songtianhao Xu, Zhongwei Chen, Zhao-Xu Yang, Weifeng Wang
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《A Unified Benchmark and Modality-Adaptive Network for Day-and-Night Drone-View Geo-Localization》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CDIKTNet, MASTR-Net, Real-World, SURFNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most existing drone-view geo-localization (DVGL) benchmarks contain drone imagery captured under a single illumination condition and lack geographically aligned visible drone images, infrared drone images, and satellite images from the same locations. To evaluate the generalization capability of DVGL methods under challenging illumination conditions, some methods train models on a visible benchmark and test them on an independent infrared benchmark. This protocol essentially constitutes transfer between datasets, which makes it difficult to systematically evaluate DVGL across daytime and nighttime conditions within a unified benchmark. To address this limitation, we construct IRCHN,a real-world DVGL benchmark designed for localization across different illumination conditions. IRCHN contains 26,460 images collected from 8,820 geographic locations across four representative scene categories, including farmland, coastline, forest, and urban areas. Each location provides one visible drone image, one infrared drone image, and one corresponding satellite image, which enables unified evaluation of DVGL methods across different illumination conditions and sensing modalities. We further propose the Modality-Adaptive State-Space Transport Relation Network (MASTR-Net), a DVGL framework tailored to localization under varying illumination conditions. MASTR-Net integrates modality-adaptive feature enhancement, bidirectional selective state-space relation modeling, and soft optimal transport relation alignment to jointly reduce modality gaps and view-induced structural discrepancies. Extensive experiments demonstrate that MASTR-Net outperforms existing state-of-the-art methods on IRCHN for localization under varying illumination conditions and achieves competitive performance on two infrared benchmarks, IR-VL328 and CVGL-RGBT. Code: https://github.com/SongtianhaoXu/MASTR-Net

</details>

---

### [[20_Research/Papers/大模型/Towards_Reliable_Stain_Transfer_An_Iterative_Data-Model_Co-Optimization_Framework_Based_on_Multimodal_Expert-Guided_Assessment|Towards Reliable Stain Transfer: An Iterative Data-Model Co-Optimization Framework Based on Multimodal Expert-Guided Assessment]]

![[assets/2607.25393_figure.png|800]]

- **arXiv**: [2607.25393](https://arxiv.org/abs/2607.25393)
- **PDF**: https://arxiv.org/pdf/2607.25393
- **详细分析**: [[20_Research/Papers/大模型/Towards_Reliable_Stain_Transfer_An_Iterative_Data-Model_Co-Optimization_Framework_Based_on_Multimodal_Expert-Guided_Assessment|Towards Reliable Stain Transfer: An Iterative Data-Model Co-Optimization Framework Based on Multimodal Expert-Guided Assessment]]
- **作者**: Siyuan Xu, Yan Wang, Haofei Song, Lili Gao, Jiansheng Wang, Qing Zhang, Dan Huang, Boxiang Yun, Hongkai Xiong, Qingli Li
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Towards Reliable Stain Transfer: An Iterative Data-Model Co-Optimization Framework Based on Multimodal Expert-Guided Assessment》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ATST-Net, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Histopathological examination primarily relies on hematoxylin and eosin (H&amp;E) and immunohistochemistry (IHC) staining. Although IHC provides critical molecular information, it is costly and requires specialized expertise. Stain transfer provides an efficient alternative by computationally generating IHC from H&amp;E images, but remains challenged by unified and interpretable modeling for heterogeneous biomarkers under pixel-unaligned supervision. We propose DMCoStain, a novel Data-Model Co-optimization framework for Stain transfer. It iteratively co-refines training data and model capability, improving staining accuracy and interpretability in both pathological and structural consistency. To refine training data in a clinically meaningful manner, it incorporates the Multimodal Expert-Guided Finer Selection (MEGFS) strategy, built upon a pioneering IHC-positive-expression (IPE) vision-language model (VLM) that emulates pathologist reasoning. To support MEGFS, we construct ImmunoInstruction, the first large-scale IPE instruction-following dataset with 150K VQA samples. Extensive experiments on multiple tissues and biomarkers demonstrate that DMCoStain achieves state-of-the-art (SOTA) accuracy. This paradigm offers strong practical value, and MEGFS also functions as a specialized evaluation tool for future model development. Dataset, code, and more details are in https://github.com/SikangSHU/DMCoStain.

</details>

---

### [[20_Research/Papers/机器人/HOME_Robust_Hough-space_Matching_Method_for_Structured_and_Textureless_Videos|HOME: Robust Hough-space Matching Method for Structured and Textureless Videos]]

![[assets/2607.25389_figure.png|800]]

- **arXiv**: [2607.25389](https://arxiv.org/abs/2607.25389)
- **PDF**: https://arxiv.org/pdf/2607.25389
- **详细分析**: [[20_Research/Papers/机器人/HOME_Robust_Hough-space_Matching_Method_for_Structured_and_Textureless_Videos|HOME: Robust Hough-space Matching Method for Structured and Textureless Videos]]
- **作者**: Masaki Satoh
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《HOME: Robust Hough-space Matching Method for Structured and Textureless Videos》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual front-ends for robotic localization typically rely on point-based features such as Oriented FAST and Rotated BRIEF (ORB), which frequently fail in structured environments dominated by strong linear structures or textureless surfaces. While line-based Simultaneous Localization and Mapping (SLAM) systems mitigate this by utilizing line segments, conventional line extraction and description algorithms are computationally prohibitive for real-time edge robotics. To address this fundamental bottleneck, we propose HOME (Hough-space One-dimensional Matching of Extrema), an ultra-lightweight, training-free feature matching framework. HOME transforms images into Hough space, mapping global linear structures to stable local extrema, which serve as keypoints, thereby reformulating complex line matching into highly efficient one-dimensional point matching. The proposed 1D radial descriptor mathematically guarantees rotational and translational invariance without the overhead of explicit orientation estimation. As a proof of concept to validate the matching accuracy and efficiency of HOME, this paper focuses on homography estimation. Extensive evaluations demonstrate that HOME achieves robust registration in challenging scenarios where point-based methods fail, operating at a much faster speed than existing line-based methods. Extending this robust matching engine to full 3D pose estimation remains a highly promising future direction.

</details>

---

### [[20_Research/Papers/机器人/Human-in-the-Loop_Signature_Bootstrapping_for_UAV_Hyperspectral_PFM-1_Mine_Detection|Human-in-the-Loop Signature Bootstrapping for UAV Hyperspectral PFM-1 Mine Detection]]

![[assets/2607.25310_figure.png|800]]

- **arXiv**: [2607.25310](https://arxiv.org/abs/2607.25310)
- **PDF**: https://arxiv.org/pdf/2607.25310
- **详细分析**: [[20_Research/Papers/机器人/Human-in-the-Loop_Signature_Bootstrapping_for_UAV_Hyperspectral_PFM-1_Mine_Detection|Human-in-the-Loop Signature Bootstrapping for UAV Hyperspectral PFM-1 Mine Detection]]
- **作者**: Sagar Lekhak, Prasanna Reddy Pulakurthi, Emmett J. Ientilucci
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Human-in-the-Loop Signature Bootstrapping for UAV Hyperspectral PFM-1 Mine Detection》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hyperspectral imaging (HSI) is useful for material discrimination, but operational mine screening also depends on how many false alarms must be inspected before targets are found. This paper studies PFM-1 landmine detection in unmanned aerial vehicle (UAV) visible and near-infrared (VNIR) HSI using spectral angle mapper (SAM), matched filter (MF), adaptive coherence estimator (ACE), and constrained energy minimization (CEM). We compare a ground-measured SVC signature, a fully informed in-scene core-pixel signature, and a simulated human-in-the-loop signature bootstrap. Besides receiver operating characteristic area under the curve and average precision, we report target-discovery curves and spatial candidate-review counts. Full-review bootstrapping reaches the fully informed in-scene signature case after all seven target regions are verified, but the required inspection effort varies strongly: ACE confirms all regions in two rounds and nine candidate inspections, whereas the SAM variants need thousands of candidate reviews for their final target locations. Code is available at https://github.com/SagarLekhak/IEEE_WHISPERS_2026_UAV_HSI_PFM1.

</details>

---

### [[20_Research/Papers/大模型/Medical_world_models_in_healthcare_foundations,_applications,_and_challenges_for_trustworthy_clinical_translation|Medical world models in healthcare: foundations, applications, and challenges for trustworthy clinical translation]]

![[assets/2607.25242_figure.png|800]]

- **arXiv**: [2607.25242](https://arxiv.org/abs/2607.25242)
- **PDF**: https://arxiv.org/pdf/2607.25242
- **详细分析**: [[20_Research/Papers/大模型/Medical_world_models_in_healthcare_foundations,_applications,_and_challenges_for_trustworthy_clinical_translation|Medical world models in healthcare: foundations, applications, and challenges for trustworthy clinical translation]]
- **作者**: Zhaoyan Chen, Zhongxiu Cong, Zhuanfeng Jin, Wanshu Fan, Dongsheng Zhou, Qi Ai, Haifan Gong, Congyu Liao, Xiaofeng Liu, Cong Wang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Multimodal, Agent, WorldModel

#### 研究背景与动机

《Medical world models in healthcare: foundations, applications, and challenges for trustworthy clinical translation》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：EHRWorld, EchoWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical world models offer a framework for extending medical artificial intelligence beyond static prediction by representing evolving patient states and modelling how they change over time and in response to clinical interventions. This Review defines the conceptual boundaries, technical foundations, application domains, and evidence requirements of the field through a structured narrative synthesis with reproducible evidence mapping.We screened 1,455 unique records and assembled a corpus of 98 sources, including 14 studies that met a strict empirical definition of a medical world model. The field is organised around four capabilities: patient state representation, temporal dynamics modelling, intervention-conditioned simulation, and clinician-supervised planning. Evidence spans medical imaging, longitudinal electronic health records, treatment response modelling, physiological and multimodal state modelling, ultrasound and surgical interaction, and population and health-system simulation; clinical digital twins are treated as a cross-cutting integration framework.Current studies provide early evidence of technical feasibility for trajectory forecasting and comparison of candidate interventions, but most remain retrospective, task-specific, or preclinical. The evidence base is further limited by incomplete longitudinal intervention data, inconsistent action semantics, limited causal identifiability, long-horizon error accumulation, inadequate uncertainty estimation, and limited external validation. Clinical translation will therefore depend on precise intervention representations, robust causal and mechanistic grounding, calibrated trajectory-level uncertainty, safety-constrained planning, and prospective multicentre validation against clinically meaningful endpoints.

</details>

---

### [[20_Research/Papers/机器人/Leveraging_Semantic_Maps_for_City-Scale_Cross-View_Localization|Leveraging Semantic Maps for City-Scale Cross-View Localization]]

![[assets/2607.25215_figure.jpg|800]]

- **arXiv**: [2607.25215](https://arxiv.org/abs/2607.25215)
- **PDF**: https://arxiv.org/pdf/2607.25215
- **详细分析**: [[20_Research/Papers/机器人/Leveraging_Semantic_Maps_for_City-Scale_Cross-View_Localization|Leveraging Semantic Maps for City-Scale Cross-View Localization]]
- **作者**: Ethan Fahnestock, Erick Fuentes, Philip R Osteen, Nicholas Roy
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Leveraging Semantic Maps for City-Scale Cross-View Localization》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We want robots to localize in previously untraversed environments against commonly available prior data. Rich semantic data available from OpenStreetMap can be useful in this task. However, existing methods either ignore this semantic information, directly matching panoramas and overhead imagery, or dramatically compress the semantic information, working with a small set of fixed classes. To leverage this rich semantic information, two challenges need to be overcome. First, useful semantic information needs to be extracted from the robot's egocentric observations. Second, the observed information must be quickly associated with the large prior semantic map (e.g., up to 628 km^2). We show that VLMs are effective at both extracting relevant landmarks from panoramas, and identifying feasible correspondences between these landmarks and prior overhead landmarks. However, using VLMs to propose all correspondences scales poorly as the number of mapped landmarks increases. Instead, we propose distilling a lightweight matcher from a VLM which computes correspondences for all entities in a map. We use this output to form an observation likelihood which is fused over time with a Bayes filter to create a time series of pose estimates. To support further investigation into generalizable cross-view methods that leverage semantic information, we release a dataset of extracted semantics and evaluation trajectories spanning eleven environments, including panoramas we collected in a snowstorm and at night in Boston. We demonstrate our method, trained on a single city's fair-weather data, generalizes across location, lighting, weather, and other challenges. Code and datasets are available at https://efahnestock.github.io/loci/.

</details>

---

### [[20_Research/Papers/具身智能/IMPRINT_Image-Conditioned_Query_Enrichment_for_Long-Tail_Object_Goal_Navigation|IMPRINT: Image-Conditioned Query Enrichment for Long-Tail Object Goal Navigation]]

![[assets/2607.25106_figure.png|800]]

- **arXiv**: [2607.25106](https://arxiv.org/abs/2607.25106)
- **PDF**: https://arxiv.org/pdf/2607.25106
- **详细分析**: [[20_Research/Papers/具身智能/IMPRINT_Image-Conditioned_Query_Enrichment_for_Long-Tail_Object_Goal_Navigation|IMPRINT: Image-Conditioned Query Enrichment for Long-Tail Object Goal Navigation]]
- **作者**: Jelin Raphael Akkara, Filippo Ziliotto, Luciano Serafini, Lamberto Ballan, Tommaso Campari
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.8（加权：具身智能 0.6，大模型 0.2）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《IMPRINT: Image-Conditioned Query Enrichment for Long-Tail Object Goal Navigation》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL, YOLOWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied AI increasingly relies on queryable semantic maps built from pre-trained vision-language models to enable zero-shot Object Goal Navigation (ObjectNav). However, existing approaches typically depend on text-only queries, which become less reliable as semantic specificity increases toward fine-grained object categories. We introduce IMPRINT, a zero-shot plug-and-play framework that enriches textual object queries with web-sourced images to improve grounding in queryable maps. Retrieved images are encoded using a vision-language model, matched against the semantic map to produce similarity maps, and aggregated to yield context-aware localization. Notably, this requires no training or modification of the underlying navigation policy. To explicitly evaluate long-tail behavior, we present HSSD-rare, a new ObjectNav benchmark built on Habitat Synthetic Scenes and featuring semantically specific subcategories. Across both OVON and HSSD-rare, image-conditioned queries consistently improve object grounding and yield end-to-end navigation gains. Further analysis reveals that translating localization gains to navigation performance depends critically on downstream detection quality, highlighting a key systems bottleneck in long-tail embodied navigation.

</details>

---

### [[20_Research/Papers/大模型/NEXT_Reasoning-Driven_Video_Recommendation_via_a_Vision-Language_Model|NEXT: Reasoning-Driven Video Recommendation via a Vision-Language Model]]

![[assets/2607.24789_figure.png|800]]

- **arXiv**: [2607.24789](https://arxiv.org/abs/2607.24789)
- **PDF**: https://arxiv.org/pdf/2607.24789
- **详细分析**: [[20_Research/Papers/大模型/NEXT_Reasoning-Driven_Video_Recommendation_via_a_Vision-Language_Model|NEXT: Reasoning-Driven Video Recommendation via a Vision-Language Model]]
- **作者**: Yuming Liu, Hongye Yang, Harrison Zhao, Ellie Zhu, Bokai Cao, Lei Huang, Lizhu Zhang, Xiangjun Fan
- **cs 子类**: cs.CV, cs.IR, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.72（加权：大模型 1，强化学习 0.56，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《NEXT: Reasoning-Driven Video Recommendation via a Vision-Language Model》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DocVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present NEXT (Next-interest EXploration Transformer), a reasoning-driven video recommendation framework that reasons over the video a user has just watched, infers the viewer's next intent, and retrieves concrete follow-up videos. Explicit continuations such as episodes are linked directly; implicit cases are handled by generating intent queries and searching for matching candidates. This Item-to-Intent-to-Item formulation produces directed recommendations beyond co-engagement correlation or semantic similarity. To make this framework reliable at scale, we train NEXT-8B, a purpose-trained 8B vision-language model with a three-stage recipe: Perception-Enhanced Reinforcement Learning for query-agnostic evidence extraction, Distribution-Aligned Supervised Fine-Tuning over real and synthetic visual QA mixtures, and Group Relative Policy Optimization for last-mile alignment. NEXT-8B achieves the best single-model DocVQA performance, ranking second overall only behind a multi-agent system while surpassing a substantially larger 200B+ scale model, and improves next-intent logic-wise quality by 3.3% over the base model in a task-specific LLM-as-a-judge evaluation. We deploy NEXT as an additional retrieval path in a large-scale social media recommendation system and observe statistically significant production gains, including +0.53% watch time and +0.51% distinct video exposure. Overall, NEXT shows that a carefully trained compact vision-language model can serve as a practical reasoning engine for next-interest exploration at production scale.

</details>

---
