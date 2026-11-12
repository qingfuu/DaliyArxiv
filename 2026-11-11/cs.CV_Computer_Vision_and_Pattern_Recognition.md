# cs.CV | Computer Vision and Pattern Recognition | 2026-11-11

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/机器人/TanCRAFT_Context-Reasoned_Anticipatory_Feedback_for_Assembly_Tasks|TanCRAFT: Context-Reasoned Anticipatory Feedback for Assembly Tasks]]

![[assets/2611.14470_figure.png|800]]

- **arXiv**: [2611.14470](https://arxiv.org/abs/2611.14470)
- **PDF**: https://arxiv.org/pdf/2611.14470
- **详细分析**: [[20_Research/Papers/机器人/TanCRAFT_Context-Reasoned_Anticipatory_Feedback_for_Assembly_Tasks|TanCRAFT: Context-Reasoned Anticipatory Feedback for Assembly Tasks]]
- **作者**: Sassan Mokhtar, Lars Doorenbos, Marius Bock, Sina Mokhtar, Katharina Beckh, Dominik Bach, Juergen Gall
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《TanCRAFT: Context-Reasoned Anticipatory Feedback for Assembly Tasks》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Preventing human error in physical assembly tasks requires assistance systems that can intervene before mistakes are made. This is especially challenging in settings where users are free to choose the construction order and correctness depends on the evolving assembly rather than a fixed next step. We present TanCRAFT, a four-stage real-time predictive assistance system that tracks the scene state, reasons about the current partial assembly, forecasts the near-future motion of manipulated pieces, and intervenes when the predicted placement is incompatible with the target. We instantiate our framework and confirm its effectiveness in a controlled tangram assembly task through offline benchmarks and a within-subject user study. Our findings show that the predictive feedback significantly reduces mistakes relative to unguided and reactive sessions, while yielding the lowest mean perceived workload and shortest mean completion time. Overall, these results demonstrate the value of predictive feedback for error prevention and provide a step toward cost-aware assistance for automation and human-robot workcells.

</details>

---

### [[20_Research/Papers/强化学习/Metric-Aligned_Group_Relative_Policy_Optimization_for_Explainable_Deepfake_Detection|Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection]]

![[assets/2611.14436_figure.png|800]]

- **arXiv**: [2611.14436](https://arxiv.org/abs/2611.14436)
- **PDF**: https://arxiv.org/pdf/2611.14436
- **详细分析**: [[20_Research/Papers/强化学习/Metric-Aligned_Group_Relative_Policy_Optimization_for_Explainable_Deepfake_Detection|Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection]]
- **作者**: Luka Dragar, Peter Peer, Vitomir Štruc, Borut Batagelj
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Metric-Aligned Group Relative Policy Optimization for Explainable Deepfake Detection》归入 强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DFBench, SID-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deepfake detectors are commonly evaluated on real/fake classification alone, but real-world applications require explanations of the visual evidence behind each prediction. Joint vision-language models struggle with authenticity assessment, producing "real" narratives for manipulated images. To address this, we propose a decoupled predict-then-explain pipeline as our submission to the ACM Multimedia 2026 Explainable Deepfake Detection Challenge, with methods trained and evaluated on the XPlainVerse benchmark. A vision-foundation-model ensemble first classifies the image, then a Qwen3-VL-8B model generates a decision-conditioned explanation of the visual evidence. For fake images, a second Qwen3-VL-8B compresses that text into a short non-expert summary without using the image. We further apply metric-aligned Group Relative Policy Optimization (GRPO) to optimize both explainers against the challenge criteria. Under matched conditions, GRPO raises complex BERTScore-F1 from 0.686 to 0.712 and also improves grounding (entity and evidence F1); our submission ranked first on complex BERTScore-F1 and seventh overall.

</details>

---

### [[20_Research/Papers/具身智能/OnlyAct_Extracting_Action_Representations_from_Foundation_Models_for_World_Models|OnlyAct: Extracting Action Representations from Foundation Models for World Models]]

![[assets/2611.14420_figure.png|800]]

- **arXiv**: [2611.14420](https://arxiv.org/abs/2611.14420)
- **PDF**: https://arxiv.org/pdf/2611.14420
- **详细分析**: [[20_Research/Papers/具身智能/OnlyAct_Extracting_Action_Representations_from_Foundation_Models_for_World_Models|OnlyAct: Extracting Action Representations from Foundation Models for World Models]]
- **作者**: Runjia Li, Minghao Chen, Junyu Xie, Philip Torr, Andrea Vedaldi, Tomas Jakab
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.1，世界模型 0.8，机器人 0.2）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《OnlyAct: Extracting Action Representations from Foundation Models for World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video world models promise general-purpose interactive simulators, but their training is limited by action supervision: action labels are scarce, fragmented across incompatible specifications, and do not scale with the unlabeled video pretraining corpus. A common workaround jointly trains an action encoder to compress consecutive frames into a latent action and a decoder to reconstruct the next frame from the previous frame and that latent, forcing the latent to capture only new information. This has two limitations: learning the action space from scratch can limit generalization to unseen domains, and the bottleneck trades expressiveness for separation, with tighter settings losing nuance and looser ones risking scene leakage under domain shifts. We argue for a different starting point: rather than learning actions from scratch, we start from a pretrained foundation model (V-JEPA 2), whose embeddings of a frame pair already carry substantial action information after large-scale, diverse video pretraining. The remaining challenge is to extract the action while discarding the scene. We propose a label-free contrastive adaptation framework that pulls together frame pairs sharing the same motion under a different scene and pushes apart pairs from the same scene with different motion, reshaping the geometry of the pretrained space without imposing a reconstruction bottleneck. We introduce a unified evaluation protocol along three axes (action expressiveness, scene invariance, and action-conditioned video generation quality) across robot manipulation, camera navigation, game, and driving benchmarks, most of which are unseen during adaptation. Compared with annotation-free latent-action methods, our representations are substantially more expressive while matching their scene invariance, and they yield world models that transfer demonstrated actions to new scenes more faithfully.

</details>

---

### [[20_Research/Papers/强化学习/From_Video_Frames_to_Robot_Meta-Frames_A_Unified_Latent_Interface_for_World_Action_Models|From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models]]

![[assets/2611.14365_figure.png|800]]

- **arXiv**: [2611.14365](https://arxiv.org/abs/2611.14365)
- **PDF**: https://arxiv.org/pdf/2611.14365
- **详细分析**: [[20_Research/Papers/强化学习/From_Video_Frames_to_Robot_Meta-Frames_A_Unified_Latent_Interface_for_World_Action_Models|From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models]]
- **作者**: Guoqiang Liang, Yiqi Lin, Yanzhe Chen, Kevin Yuchen Ma, Mike Zheng Shou
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《From Video Frames to Robot Meta-Frames: A Unified Latent Interface for World Action Models》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgiBot-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained video diffusion models (VDMs) offer a powerful foundation for World Action Models (WAMs), which jointly predict robot actions and future observations. Building such models requires injecting low-dimensional robot signals (e.g. proprioception, actions, and values) into a latent space shaped by natural videos, and a key design choice is the interface through which these signals enter: existing schemes treat it as a formatting detail, spending a separate latent frame on each signal or bolting on dedicated encoders and decoders. We argue that signal injection is instead a distribution-alignment problem: how well a representation matches the prior of the pretrained VDMs during denoising. Using the relative reconstruction error of a frozen VDM denoiser as a probe, we find that conventional spatial encodings sit far off this prior, whereas frequency-domain packing yields latents that the denoiser corrects far less. Motivated by this diagnostic result, we propose MetaWAM, which folds all robot signals into a single unified meta-frame: each signal is assigned to a disjoint frequency-domain channel band and lifted to the spatial latent by an inverse DCT, yielding a decodable interface aligned with the pretrained VDM prior without any added module or architectural change. A fixed band layout together with slot-aware routing lets the same meta-frame support policy, world-model, and value prediction over a shared set of robot variables. On RoboCasa, MetaWAM reaches 68.9% success while collapsing the per-signal frames into one and cutting inference latency by 39%, and attains 85.0% success on three real-world Franka tasks. Code and models are available at https://github.com/showlab/MetaWAM

</details>

---

### [[20_Research/Papers/机器人/Elastic-WAM_Adaptive_Spatiotemporal_Imagination_for_Efficient_Robot_Control|Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control]]

![[assets/2611.14257_figure.png|800]]

- **arXiv**: [2611.14257](https://arxiv.org/abs/2611.14257)
- **PDF**: https://arxiv.org/pdf/2611.14257
- **详细分析**: [[20_Research/Papers/机器人/Elastic-WAM_Adaptive_Spatiotemporal_Imagination_for_Efficient_Robot_Control|Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control]]
- **作者**: Haitian Li, Tianfu Li, Xuxi Zhao, Zizheng Liu, Yangcheng Yu, Yiwen Hou, Zeyu Xiao, Mutian Xu, Ziqian Yang, Haonan Chen, Lin Shao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Elastic-WAM: Adaptive Spatiotemporal Imagination for Efficient Robot Control》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-Action Models improve robot control by predicting future visual dynamics, but iterative video denoising incurs substantial inference overhead. Recent approaches reduce this cost through partial future denoising, yet typically rely on fixed refinement budgets. Our empirical observations reveal that preferred refinement depths vary across tasks and states, while different future regions exhibit varying relevance to action generation. Motivated by these findings, we propose Elastic-WAM, which adaptively allocates world refinement computation across temporal denoising time and spatial future space. A unified spatiotemporal refinement demand field governs when to stop world refinement, how far to advance each denoising step, and which regions to refresh. We parameterize this field with a shared temporal basis and spatial amplitudes, and learn it through a three-stage action-grounded supervised procedure. At inference, the learned field guides recurrent sparse world refinement to improve task success while reducing inference overhead. Evaluations across diverse simulation benchmarks and real-world long-horizon manipulation demonstrate state-of-the-art control performance with reduced inference latency.

</details>

---

### [[20_Research/Papers/机器人/HiPFuse_Real-Time_LiDAR_Semantic_Segmentation_for_Robotic_Perception_on_Edge_Devices|HiPFuse: Real-Time LiDAR Semantic Segmentation for Robotic Perception on Edge Devices]]

![[assets/2611.14025_figure.png|800]]

- **arXiv**: [2611.14025](https://arxiv.org/abs/2611.14025)
- **PDF**: https://arxiv.org/pdf/2611.14025
- **详细分析**: [[20_Research/Papers/机器人/HiPFuse_Real-Time_LiDAR_Semantic_Segmentation_for_Robotic_Perception_on_Edge_Devices|HiPFuse: Real-Time LiDAR Semantic Segmentation for Robotic Perception on Edge Devices]]
- **作者**: Haiyang Wu, George Vosselman, Ville Lehtola
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《HiPFuse: Real-Time LiDAR Semantic Segmentation for Robotic Perception on Edge Devices》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LidarMultiNet, MINet, PolarNet, RPVNet, RandLA-Net, RangeNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time robotic perception requires accurate LiDAR semantics under limited resources. Bird's-eye-view (BEV) aggregation is efficient but can mix differently labeled surfaces in columns. We present HiPFuse, a point-BEV fusion framework that exchanges point and height-partitioned BEV features across horizontal scales, combining point-wise detail with 2D spatial context from one LiDAR scan. Fixed height assignments preserve separate vertical aggregation groups, with auxiliary supervision of initial BEV features using targets from the same 3D cells. A dual-scale BEV context module adds broader context from a coarser grid. On SemanticKITTI and MCD, HiPFuse achieves 63.7% and 62.5% mIoU at 14.2 and 22.4 FPS on Jetson AGX Orin, respectively, exceeding the 10 Hz scan rate. Separate training and evaluation show indoor applicability. Replacing only the baseline semantic front end with HiPFuse in fixed robotic systems reduces odometry absolute trajectory error RMSE by 10.6% on average across two outdoor sequences and increases accepted-loop recall by 8.7 percentage points on SemanticKITTI. Qualitative semantic maps show more continuous road labeling. Our code is available at https://github.com/haiyang2022/HiPFuse.

</details>

---

### [[20_Research/Papers/多模态技术/A_10K_drone_image_dataset_with_component-level_annotations_for_rooftop_photovoltaic_inspection|A 10K drone image dataset with component-level annotations for rooftop photovoltaic inspection]]

![[assets/2611.13892_figure.png|800]]

- **arXiv**: [2611.13892](https://arxiv.org/abs/2611.13892)
- **PDF**: https://arxiv.org/pdf/2611.13892
- **详细分析**: [[20_Research/Papers/多模态技术/A_10K_drone_image_dataset_with_component-level_annotations_for_rooftop_photovoltaic_inspection|A 10K drone image dataset with component-level annotations for rooftop photovoltaic inspection]]
- **作者**: Penglei Zhang, Wan Zhang, Ruizhe Deng, Bo Chen, Wenhao Duan, Jinhe Zhang, Yanzhen Zhang, Qi Chen, Zhiling Guo, Haoran Zhang, Yuntian Chen
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《A 10K drone image dataset with component-level annotations for rooftop photovoltaic inspection》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Component-level information supports rooftop photovoltaic (PV) inspection, but recognizing individual components across complex scenes remains challenging. We present PVIS-10K, a dataset of 10,065 drone images with component-level annotations covering 63,632 physical PV modules across 22 rooftop installations. The high-resolution red-green-blue (RGB) images were acquired by unmanned aerial vehicles (UAVs, also known as drones) in Ningbo, Shaoxing and Shenzhen, China. Multi-angle oblique observations capture installation-height and scale variation, dense arrangements, occlusion, shadows and reflections. Three-dimensional delineation, reprojection and image-by-image review produced 3,516,675 image-level polygon annotations, stored in Common Objects in Context (COCO) format. Station-disjoint partitions support evaluation on unseen stations within and across cities. Four supervised models and text-prompted zero-shot Segment Anything Model 3 (SAM 3) provide full-resolution benchmarks of instance matching and foreground coverage. PVIS-10K supports component localization, delineation and image-based counting for drone-based rooftop PV inspection research.

</details>

---

### [[20_Research/Papers/大模型/DroneSegEdit_Adapting_Pretrained_Generative_Editors_for_UAV_Segmentation_with_Language-Grounded_Verification|DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification]]

![[assets/2611.13890_figure.png|800]]

- **arXiv**: [2611.13890](https://arxiv.org/abs/2611.13890)
- **PDF**: https://arxiv.org/pdf/2611.13890
- **详细分析**: [[20_Research/Papers/大模型/DroneSegEdit_Adapting_Pretrained_Generative_Editors_for_UAV_Segmentation_with_Language-Grounded_Verification|DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification]]
- **作者**: Dehua Chen, Long Xin, Jiangtao Wei
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，机器人 0.8）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《DroneSegEdit: Adapting Pretrained Generative Editors for UAV Segmentation with Language-Grounded Verification》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work has shown that pretrained image generators can support diverse visual tasks. Yet directly applying them to language-guided unmanned aerial vehicle (UAV) segmentation exposes a key limitation: a plausible mask may correspond to the wrong instance among small and repeated objects. We call this mismatch between mask rendering and expression-level target selection the Grounding-Rendering Gap. We present DroneSegEdit, which combines RGB proposal rendering with language-grounded, proposal-constrained verification to select supported foreground while retaining rendered geometry. DroneSegEdit adapts the open-weight LongCat-Image-Edit model using task-specific LoRA and fixed color-to-label decoding. For referring segmentation, a Language-Grounded Spatial Verifier (LGSV) reads hierarchical states from the frozen multimodal large language model backbone to derive expression-conditioned spatial evidence, which is mapped back to the rendered proposal without introducing foreground outside it. On RIS-LAD, DroneSegEdit reaches a new state of the art at 52.78 mIoU, 7.16 points above the previous best. It remains competitive overall on UAVid-RIS and VDD-RIS, with its clearest class-wise gains on compact, application-relevant categories, notably vehicles and humans. A separate verifier-free experiment extends the RGB interface to full-scene parsing: a task-specific adapter jointly renders all classes from one task-level instruction without enumerating class names or palette colors.

</details>

---

### [[20_Research/Papers/具身智能/From_Depth_to_Safe_Depth_Uncertainty-Aware_Monocular_Perception_for_Mobile_Robot_Navigation|From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation]]

![[assets/2611.13769_first_page.png|800]]

- **arXiv**: [2611.13769](https://arxiv.org/abs/2611.13769)
- **PDF**: https://arxiv.org/pdf/2611.13769
- **详细分析**: [[20_Research/Papers/具身智能/From_Depth_to_Safe_Depth_Uncertainty-Aware_Monocular_Perception_for_Mobile_Robot_Navigation|From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation]]
- **作者**: Saeid Firouzi Daghigh, Saeed Ayat
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《From Depth to Safe Depth: Uncertainty-Aware Monocular Perception for Mobile Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular depth foundation models make it tempting to replace depth sensors on mobile robots with a single RGB camera. We show that, used off the shelf, this is unsafe: in a simulated indoor navigation benchmark, a standard Nav2 stack driven by Depth Anything V2 (metric) collides in 63\% of 120 episodes, because the model systematically over-estimates the distance to nearby obstacles. We propose a lightweight plug-in module that turns predicted depth into \emph{safe depth}. A 0.58\,M-parameter head on top of the \emph{frozen} depth model predicts, per pixel, a log-depth correction $μ$ and an uncertainty $σ$, trained with a $β$-weighted Gaussian negative log-likelihood. The navigation stack consumes the one-sided bound $\hat d_{\text{safe}}=d\,e^{μ-kσ}$, where $k$ is set by conformal calibration on a held-out world, and uncertainty also decides which pixels may be treated as floor. The correction halves the depth error (AbsRel $0.262\rightarrow0.134$) and reduces near-range over-estimation from 59.8\% to 12.0\%. In navigation, safe depth raises the success rate from 37\% to 70\% and lowers collisions from 63\% to 3\%, close to the 2\% of ground-truth depth. A constant safety margin calibrated to the same pixel coverage reaches only 30\% success because it freezes the robot; uncertainty-aware safety wins 52 of 56 discordant paired episodes against it. Gains hold on glass, texture-less walls and dark regions.

</details>

---

### [[20_Research/Papers/世界模型/GEMOR-GS_Global_Extrinsic-calibration-refined_Mapping_and_Online_Relocalization_for_3D_Gaussian-Splatting_SLAM|GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM]]

![[assets/2611.13528_figure.png|800]]

- **arXiv**: [2611.13528](https://arxiv.org/abs/2611.13528)
- **PDF**: https://arxiv.org/pdf/2611.13528
- **详细分析**: [[20_Research/Papers/世界模型/GEMOR-GS_Global_Extrinsic-calibration-refined_Mapping_and_Online_Relocalization_for_3D_Gaussian-Splatting_SLAM|GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM]]
- **作者**: Yuchen Yang, Ming Ding, Xinyu Wu, Hesheng Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《GEMOR-GS: Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Photorealistic and metrically consistent world representations are a primary requirement for LiDAR--inertial--visual SLAM systems that serve robots over continuous operation. 3D Gaussian splatting makes such representations attainable by supplying an explicit, renderable, and queryable scene model. We present GEMOR-GS (Global Extrinsic-calibration-refined Mapping and Online Relocalization for 3D Gaussian-Splatting SLAM) to make the Gaussian map geometrically accurate, globally refined, and re-enterable, providing a better appearance for robot perception and decision-making. To improve the 3DGS map, the LiDAR--camera extrinsic is first estimated offline by direct-method alignment over dedicated calibration segments and reused by all following online and offline processes. Under the calibrated geometry, keyframe poses and Gaussian parameters are refined alternately under a gated differentiable-rendering and LiDAR--projection objective. The final global reconstruction is then rebuilt from the refined keyframe schema with all online constraints lifted. For the robot SLAM lifecycle, the method recovers the pose from the 3DGS map after tracking loss through an XFeat bypass map, RANSAC-PnP coarse localization, and Gaussian RGB-D warp refinement. Experiments on one self-collected and five public sequences quantify each element: the offline reconstruction wins all paired keyframes against the online map by 14.3--19.9 dB, improves PSNR by approximately 9 dB over Gaussian-LIC2, and achieves 86--100% held-out relocalization success tied to extrinsic quality. The results show that GEMOR-GS improves the geometric accuracy, appearance fidelity, and re-enterability of the 3DGS map, serving as a dependable robot world model for SLAM and downstream tasks.

</details>

---

### [[20_Research/Papers/强化学习/Topology-Aware_Reinforcement_Learning_for_CAD_Decomposition_toward_All-Hexahedral_Meshing|Topology-Aware Reinforcement Learning for CAD Decomposition toward All-Hexahedral Meshing]]

![[assets/2611.12930_figure.png|800]]

- **arXiv**: [2611.12930](https://arxiv.org/abs/2611.12930)
- **PDF**: https://arxiv.org/pdf/2611.12930
- **详细分析**: [[20_Research/Papers/强化学习/Topology-Aware_Reinforcement_Learning_for_CAD_Decomposition_toward_All-Hexahedral_Meshing|Topology-Aware Reinforcement Learning for CAD Decomposition toward All-Hexahedral Meshing]]
- **作者**: Jiaming Peng, Zhihao Zheng, Rui Wang, Qinglin Wang, Jing Xiao, Jie Liu, Na Lei, Xinhai Chen
- **cs 子类**: cs.CV, cs.GR, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.32（加权：强化学习 1.16，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《Topology-Aware Reinforcement Learning for CAD Decomposition toward All-Hexahedral Meshing》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BRepNet, DRL, DecompRL, LMFF-to-DecompRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic hexahedral meshing for complex CAD models has long been regarded as the "holy grail" of mesh generation. The fundamental challenge arises from feature misalignment, where orthogonal or interacting features coexist, making direct hexahedral meshing infeasible and requiring decomposition into simpler, meshable blocks. While existing decomposition methods, including frame-field pipelines and learning-based techniques, have reduced manual intervention, they can remain sensitive to geometric and topological complexity and may fail to produce valid decompositions for challenging feature configurations. Specifically, their action spaces are typically restricted to surface-based splitting, which often yields invalid or unmeshable decompositions. To address these limitations, we propose DecompRL, a deep reinforcement learning framework for CAD decomposition toward hexahedral meshing. We design a set of topology-aware internal-splitting actions that leverage both global topological structure and local geometric property to effectively separate misaligned features. Furthermore, we introduce geometric rewards together with meshability feedback to guide the learning process toward valid decompositions and high-quality meshes. Extensive experiments on ABC, Fusion360, NIST, and DeepCAD show that DecompRL achieves the highest success rate among the evaluated learning-based methods on three of the four benchmarks, while maintaining competitive mesh quality. The measured LMFF-to-DecompRL runtime ratio reaches up to two orders of magnitude; this compares the full LMFF procedure with DecompRL decomposition alone, excluding subsequent mesh generation. The largest SR improvement is observed on Fusion360, where DecompRL reaches a success rate of 59.6%.

</details>

---
