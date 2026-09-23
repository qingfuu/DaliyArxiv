# cs.CV | Computer Vision and Pattern Recognition | 2026-09-21

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/具身智能/PRIME_Perception_Feedback_with_Situational_Memory_Embeddings_in_VLA_Models|PRIME: Perception Feedback with Situational Memory Embeddings in VLA Models]]

![[assets/2609.22040_figure.png|800]]

- **arXiv**: [2609.22040](https://arxiv.org/abs/2609.22040)
- **PDF**: https://arxiv.org/pdf/2609.22040
- **详细分析**: [[20_Research/Papers/具身智能/PRIME_Perception_Feedback_with_Situational_Memory_Embeddings_in_VLA_Models|PRIME: Perception Feedback with Situational Memory Embeddings in VLA Models]]
- **作者**: Erik Deinzer, Naya Baslan, Luca Paparusso, Narunas Vaskevicius, Peter Knott, Luigi Palmieri
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《PRIME: Perception Feedback with Situational Memory Embeddings in VLA Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current Vision-Language-Action (VLA) models for autonomous driving operate primarily through feedforward inference across the perception--reasoning--planning hierarchy. While modern architectures maintain temporal recurrence within the perceptual module, early perception remains blind to downstream reasoning and navigation goals, processing visual inputs agnostically without prioritizing cues informed by prior decisions. To bridge this gap, this paper introduces PRIME, a learned feedback mechanism that conditions the VLA perceptual queries on a novel Situational Memory. By aggregating latent representations of past perception, reasoning, navigation goals, and predicted behaviors across an L-step window via cross-attention, PRIME enables intent-driven perceptual attention at minimal computational cost, adding only a maximum of 29.7M parameters (0.41% of the 7.3B-parameter base model). Evaluated on the Bench2Drive closed-loop benchmark, PRIME achieves a state-of-the-art Driving Score of 82.47 (+4.73 over ORION) and a Success Rate of 60.00% (+5.38 percentage points), the highest reported Driving Score among published VLAs trained on Think2Drive demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/GALA_Geometry-Aware_Latent_Action_Modeling_for_Vision-Language-Action_Model_Pretraining_across_Embodiments|GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments]]

![[assets/2609.21948_figure.png|800]]

- **arXiv**: [2609.21948](https://arxiv.org/abs/2609.21948)
- **PDF**: https://arxiv.org/pdf/2609.21948
- **详细分析**: [[20_Research/Papers/具身智能/GALA_Geometry-Aware_Latent_Action_Modeling_for_Vision-Language-Action_Model_Pretraining_across_Embodiments|GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments]]
- **作者**: Yichen Liu, Puzhen Yuan, Xiang Zhu, Yanjiang Guo, Jianyu Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《GALA: Geometry-Aware Latent Action Modeling for Vision-Language-Action Model Pretraining across Embodiments》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DexVLA, HARP-VLA, OpenVLA, Real-World, URL, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning large-scale vision-language-action (VLA) models from multi-embodiment datasets remains challenging due to heterogeneous action spaces across end effectors. Although latent action models (LAMs) can learn embodiment-agnostic action representations from diverse video data, existing image-based LAMs often fail to capture fine-grained end-effector articulation, particularly finger-level geometric changes in human and dexterous robot hands. To address this limitation, we propose GALA, a Geometry-Aware Latent-Action modeling framework that augments image-based latent actions with 3D end-effector geometric motion. However, naively incorporating point clouds yields fine-grained action representations with limited shared semantics, hindering cross-embodiment pretraining. To address this issue, we introduce the Unified End-effector Motion Representation (UEMR), which preserves fine-grained motion information while improving the cross-embodiment generalizability of latent actions. Building upon UEMR, GALA combines visual latent actions that capture scene-level dynamics with geometric latent actions that capture shared fine-grained end-effector articulation, providing effective supervision for VLA pretraining from multi-embodiment data, including action-free ego-centric human videos. Experiments on fine-grained motion probing, cross-embodiment retrieval, and downstream VLA evaluation demonstrate GALA's effectiveness in modeling generalizable fine-grained motions across embodiments, achieving 68.3% RoboCasa-GR1 success rate and 75.5% real-world success rate. Code, appendix, and demos are available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/ZYT-World_A_Real-Time_Controllable_World_Model_for_Closed-Loop_Autonomous-Driving_Simulation|ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation]]

![[assets/2609.21712_figure.png|800]]

- **arXiv**: [2609.21712](https://arxiv.org/abs/2609.21712)
- **PDF**: https://arxiv.org/pdf/2609.21712
- **详细分析**: [[20_Research/Papers/具身智能/ZYT-World_A_Real-Time_Controllable_World_Model_for_Closed-Loop_Autonomous-Driving_Simulation|ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation]]
- **作者**: Boni Hu, Xiong Wei, Haoming Huang, Yong Huang, Chenbo Wang, Yi Yang, Jiancheng Wang, Ruicheng Zhu, Zhimin Yang, Guanglai Liu, Qiaowan Jin, Dongzhuo Wang...
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，世界模型 0.8）
- **关联关键词**: Multimodal, WorldModel

#### 研究背景与动机

《ZYT-World: A Real-Time Controllable World Model for Closed-Loop Autonomous-Driving Simulation》归入 世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：X-World, ZYT-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative world models offer controllable and repeatable closed-loop simulation for end-to-end and vision-language-action driving policies, but production deployment exposes three unresolved requirements: faithfully reproducing a mixed fisheye-pinhole rig at native resolutions; reconciling causal, per-timestep interaction with long-horizon stability and low latency; and preserving scene identity when a location is revisited. We present ZYT-World, a single architecture that natively generates four fisheye views with field of view &gt; 180° and three pinhole views. Projection-specific Plucker adapters encode camera geometry, ego-motion adaptive layer normalization provides global motion control, and a lightweight pixel-aligned layout conditions traffic participants and signals through instance-level boxes, headings and colors. Heterogeneous training combines full-rig geometric coverage with high-resolution detail. Teacher forcing, causal consistency distillation, self-rollout distribution matching distillation, and RigCritic transform a 40-step bidirectional teacher into a one-step, per-latent streaming generator, with RigCritic evaluating the seven-view rig jointly. A 19M-parameter variational autoencoder decoder (TinyVAE), W8A8 quantization, and our inference engine reduce decoding, backbone, and incremental-execution costs, respectively. Finally, cross-trajectory pairs derived from real captures train a plug-in implicit-memory module that preserves place-specific evidence. On the internal multi-view test set, the one-step model retains more than 90% of the teacher's PSNR and SSIM, while FID, FVD, and LPIPS stay within 11% of the teacher. Under the generator-only timing in Figure 2, it is 107.7 times faster than the 40-step bidirectional teacher. TinyVAE decodes 59.8 times faster than Wan. 30s rollouts and cross-trajectory revisits show the intended long-horizon and memory behavior.

</details>

---

### [[20_Research/Papers/大模型/Adaptive_World_Memory_3D_Foundation_Model_for_Scalable_3D_Mapping,_Localization,_and_Rendering|Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering]]

![[assets/2609.21502_figure.png|800]]

- **arXiv**: [2609.21502](https://arxiv.org/abs/2609.21502)
- **PDF**: https://arxiv.org/pdf/2609.21502
- **详细分析**: [[20_Research/Papers/大模型/Adaptive_World_Memory_3D_Foundation_Model_for_Scalable_3D_Mapping,_Localization,_and_Rendering|Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering]]
- **作者**: Tianchen Deng, Guole Shen, Yilin Shen, Wenhua Wu, Yilin Fang, Ziqi Ma, Tianjun Zhang, Shenghai Yuan, Wolfram Burgard, Hesheng Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.4，机器人 0.7）
- **关联关键词**: LLM, Robotics, ComputerVision

#### 研究背景与动机

《Adaptive World Memory 3D Foundation Model for Scalable 3D Mapping, Localization, and Rendering》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeltaNet, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent 3D foundation models enable generalizable geometric reasoning from RGB images but remain limited in persistent memory, scalability, and renderable scene modeling. We present a memory-centric 3D foundation model for scalable robotic localization, reconstruction, and Gaussian rendering. Its core is an adaptive world memory mechanism that combines transformer-based gated updates with test-time temporal-spatial regulation. Learned gates control recurrent memory propagation, while temporal state evolution and spatial observation-state consistency regulate token-wise updates and forgetting over long image sequences. To support large-scale mapping, we organize memory into local submaps and integrate progressive mapping and tracking, loop closure, and SL(4)-based global refinement to maintain local accuracy and global consistency. A Gaussian reconstruction head decodes memory-enhanced features into renderable primitives, unifying camera pose estimation, dense point-cloud reconstruction, and photorealistic rendering within a single model. Experiments on public benchmarks and self-collected datasets from diverse robotic platforms demonstrate improved trajectory accuracy, reconstruction completeness, and rendering quality over existing 3D foundation reconstruction and SLAM baselines. These results support adaptive memory as a foundation for persistent robotic world modeling. The dataset and code will be made publicly available at \href{ this https URL }{ this https URL }.

</details>

---

### [[20_Research/Papers/大模型/A_Scene_Language_Model_for_Open-Vocabulary_Scene_Mapping|A Scene Language Model for Open-Vocabulary Scene Mapping]]

![[assets/2609.21400_figure.png|800]]

- **arXiv**: [2609.21400](https://arxiv.org/abs/2609.21400)
- **PDF**: https://arxiv.org/pdf/2609.21400
- **详细分析**: [[20_Research/Papers/大模型/A_Scene_Language_Model_for_Open-Vocabulary_Scene_Mapping|A Scene Language Model for Open-Vocabulary Scene Mapping]]
- **作者**: Adam Lilja, Fabio Hübel, Siming He, Junsheng Fu, Claire Tomlin, Lars Hammarstrand, Jitendra Malik, Jonas Frey, Marco Pavone
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《A Scene Language Model for Open-Vocabulary Scene Mapping》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ScanNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-vocabulary 3D scene mapping aims to build a persistent representation of the objects in an environment. Existing systems typically rely on engineered mapping pipelines to associate observations, merge information across views, and maintain a consistent scene representation over time. Many additionally store feature-rich object representations, such as embeddings or image crops, increasing the size and complexity of the persistent memory. We introduce SceneLM, a Scene-Language Model that directly maintains a textual scene map. The full scene is represented as a structured text list of objects, which serves as the model's only persistent memory. For each input image, the model reads the current scene state and updates the map by adding, editing, and removing objects. To learn this behavior, we introduce supervision tasks for iterative scene map maintenance together with an automatic annotation pipeline that generates training data from images without human labels. We evaluate SceneLM on both a language-grounded retrieval benchmark and a localization benchmark. Across both benchmarks, the model produces a scene map that achieves competitive performance with complete mapping systems built from dedicated perception and geometric modules while producing a scene representation that is 6-12x more compact. We further show that SceneLM can be run online on an edge device through experiments on a quadruped. These results show that a persistent open-vocabulary 3D scene map can be maintained directly by a single vision-language model using only a lightweight text representation. Training and inference code is available on this https URL .

</details>

---

### [[20_Research/Papers/具身智能/ProTracer_Proprioception-Guided_Failure_Diagnosis_in_Robot_Manipulation|ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation]]

![[assets/2609.21369_figure.png|800]]

- **arXiv**: [2609.21369](https://arxiv.org/abs/2609.21369)
- **PDF**: https://arxiv.org/pdf/2609.21369
- **详细分析**: [[20_Research/Papers/具身智能/ProTracer_Proprioception-Guided_Failure_Diagnosis_in_Robot_Manipulation|ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation]]
- **作者**: Chang Dong, Mehdi Hosseinzadeh, King Hang Wong, Lingqiao Liu, Francois Fraysse, Feras Dayoub, Minh Hoai Nguyen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.5，大模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《ProTracer: Proprioception-Guided Failure Diagnosis in Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a comprehensive framework for robot manipulation failure analysis that includes binary failure detection, failure categorization, explanation generation, and the additional capability of failure onset localization, which aims to identify the earliest moment at which a robot execution deviates from a valid task-completion trajectory and is ultimately followed by task failure. To address these tasks, we propose ProTracer, a training-free framework that leverages existing Vision-Language Models (VLMs) together with proprioceptive signals for failure analysis. Our method uses proprioceptive dynamics to identify temporally informative action boundaries and converts richer robot-state signals into structured natural-language descriptions that can be jointly analyzed together with visual observations by the VLM. This design combines the temporal precision of proprioceptive signals with the multimodal reasoning capabilities of modern VLMs without requiring additional model training. We further introduce FailTime, a benchmark with synchronized visual and proprioceptive observations for evaluating conventional failure diagnosis tasks as well as failure onset localization. Experiments demonstrate that ProTracer achieves strong performance across both conventional failure diagnosis tasks and the newly introduced failure onset localization task, highlighting the importance of proprioceptive reasoning for fine-grained temporal failure analysis.

</details>

---

### [[20_Research/Papers/机器人/Multi-viewpoint_Geo-localization_with_Event_Cameras|Multi-viewpoint Geo-localization with Event Cameras]]

![[assets/2609.21219_figure.png|800]]

- **arXiv**: [2609.21219](https://arxiv.org/abs/2609.21219)
- **PDF**: https://arxiv.org/pdf/2609.21219
- **详细分析**: [[20_Research/Papers/机器人/Multi-viewpoint_Geo-localization_with_Event_Cameras|Multi-viewpoint Geo-localization with Event Cameras]]
- **作者**: Adam D. Hines, Michael Milford, Tobias Fischer
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Multi-viewpoint Geo-localization with Event Cameras》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, N-ImageNet, Real2Sim, ScanNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot localization is an ongoing challenge that demands mapping and positioning systems that are tolerant to viewpoint change. Event cameras are attracting increasing interest and adoption in robotics; however, dealing with viewpoint variance is an under-investigated problem in existing event-based localizers. In addition, event-based datasets that emphasize viewpoint variance for challenging localization situations are scarce. Here, we introduce an event-based visual place recognition (VPR) system that performs robustly under viewpoint changes. We converted five large-scale geo-tagged datasets, conventionally used to train frame-based localization systems, into synthetic event streams using Image-to-Event (I2E) conversion, and used them to fine-tune a pre-trained event-based vision transformer backbone with a multi-loss function, yielding a system we call MegaEvent that learns viewpoint-robust features for place recognition. We achieved an average Recall@1 of 82% across three existing event-based localization datasets, leading the next best event-based method by 20 recall points, and frame-based VPR models applied directly to event frames by 8 to 26 recall points. We introduce a new, challenging dataset - Springfield-Event-VPR - which features a 3.7km walking route recorded in three camera orientations for a total of 11.1km, which MegaEvent outperforms the strongest baseline by 9 recall points. The code for MegaEvent is available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/AnyviewMeter_Adapting_Robotic_Reward_Models_with_Camera_Geometry_and_Multi-View_Attention|AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention]]

![[assets/2609.20106_figure.png|800]]

- **arXiv**: [2609.20106](https://arxiv.org/abs/2609.20106)
- **PDF**: https://arxiv.org/pdf/2609.20106
- **详细分析**: [[20_Research/Papers/强化学习/AnyviewMeter_Adapting_Robotic_Reward_Models_with_Camera_Geometry_and_Multi-View_Attention|AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention]]
- **作者**: Yuang Tu, Runjia Tan, Yujie Yan, Jinghan Hu, Chen Lv
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，机器人 0.8）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《AnyviewMeter: Adapting Robotic Reward Models with Camera Geometry and Multi-View Attention》归入 机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic reward models evaluate task execution from visual observations, but their predictions can change with camera viewpoint and occlusion even when the underlying task state is unchanged. Adapting a pretrained reward model to a local task therefore requires accounting for how that task is observed. We introduce AnyviewMeter, a geometry-conditioned adaptation framework for robotic reward models that represent task progress as a scalar reward signal. It combines low-rank fine-tuning with token-aligned Plucker rays and synchronous block attention: ray conditioning incorporates camera geometry into visual features and attention queries and keys, while block attention fuses synchronized views inside the pretrained decoder. The framework supports both single-view reward prediction and joint multi-view evaluation through parameter-efficient adaptation of a pretrained Robometer model. On PickCube, single-view adaptation improves progress prediction in every camera group and reduces mean absolute error under a changed field of view by approximately 21% relative to RGB fine-tuning. Across simulated manipulation tasks, joint multi-view prediction reduces progress error by 41-69% compared with averaging single-view RGB predictions and improves temporal ordering in approximately 88% of task-camera groups. On real tasks with fixed and wrist-mounted cameras, mean absolute error decreases by approximately 21% relative to averaged RGB fine-tuning. These results support camera geometry and joint visual evidence as useful components of task-specific robotic reward adaptation.

</details>

---
