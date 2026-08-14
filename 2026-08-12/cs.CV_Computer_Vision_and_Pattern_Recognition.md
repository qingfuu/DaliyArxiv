# cs.CV | Computer Vision and Pattern Recognition | 2026-08-12

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/强化学习/VidForensics-M1_Meta-Detection_Reinforcement_Learning_with_Verifiable_Temporal_Grounding_for_AI-Generated_Video_Forensics|VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics]]

![[assets/2608.11201_figure.png|800]]

- **arXiv**: [2608.11201](https://arxiv.org/abs/2608.11201)
- **PDF**: https://arxiv.org/pdf/2608.11201
- **详细分析**: [[20_Research/Papers/强化学习/VidForensics-M1_Meta-Detection_Reinforcement_Learning_with_Verifiable_Temporal_Grounding_for_AI-Generated_Video_Forensics|VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics]]
- **作者**: Bowei Liu, Zheng Lu, Yuhan Bian, Xinchen Zhang, Xingming Shui, Yuesheng Huang, Xuhuan Li, Zihao Liu, Yifan Yang, Jun Zhou, Xiu Li
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《VidForensics-M1: Meta-Detection Reinforcement Learning with Verifiable Temporal Grounding for AI-Generated Video Forensics》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ActivityNet, GenVidBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in video generation models have significantly improved the realism of synthetic videos, blurring the boundary between generated and authentic content and raising concerns about misinformation. Existing MLLM-based detectors mainly rely on supervised fine-tuning or label-level reinforcement learning, where coarse supervision limits generalization to unseen scenarios and emerging video generators. To overcome these limitations, we are the first to introduce \textbf{meta-detection} into AI-generated video detection, enabling reliable forgery detection by jointly optimizing predicted labels and supporting evidence within reinforcement learning. This paradigm requires reliable evidence signals and effective mechanisms to integrate them into label-level optimization. Textual rationales provide semantic descriptions of forgery artifacts, but their generation and verification depend on external models, making supervision vulnerable to hallucinations and semantic biases. In contrast, temporal grounding provides more objective and verifiable evidence, as manipulated intervals can be precisely controlled during forgery construction. Based on this insight, we propose an automated data construction pipeline that generates paired real-fake videos by replacing temporal segments with boundary-frame-conditioned video generation models. Furthermore, we introduce \textbf{Evidence-Guided Reward Redistribution}, which performs evidence-aware credit assignment by redistributing rewards among label-correct responses according to evidence quality. This preserves reliable label supervision while encouraging detectors to acquire fine-grained and verifiable forgery localization capabilities. Extensive experiments demonstrate that \textbf{VidForensics-M1} effectively leverages verifiable temporal evidence to achieve robust and generalizable AI-generated video detection.

</details>

---

### [[20_Research/Papers/具身智能/HUI360_A_360°_Egocentric_Dataset_and_Baselines_for_Human-Robot_Interaction_Anticipation|HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation]]

![[assets/2608.11051_figure.jpg|800]]

- **arXiv**: [2608.11051](https://arxiv.org/abs/2608.11051)
- **PDF**: https://arxiv.org/pdf/2608.11051
- **详细分析**: [[20_Research/Papers/具身智能/HUI360_A_360°_Egocentric_Dataset_and_Baselines_for_Human-Robot_Interaction_Anticipation|HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation]]
- **作者**: Raphael Lorenzo-Louis, Fabio Amadio, Bertrand Luvison, Serena Ivaldi
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.1，机器人 0.8）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《HUI360: A 360° Egocentric Dataset and Baselines for Human-Robot Interaction Anticipation》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As robots increasingly operate in human-populated environments, anticipating human intentions is essential for enabling proactive and socially aware behavior. Automatic anticipation of human-robot interactions is thus emerging as a crucial perception challenge for embodied agents. To this end, we introduce HUI360, the largest dataset for human-robot interaction anticipation in the wild and its set of baselines. The dataset was collected from a mobile robot, in the wild, over multiple days within a 3-month period, and in several environments, capturing natural, spontaneous behaviors from both passersby and users, and encompassing a diverse range of individuals. This variety enables evaluating and improving the generalization capabilities of interaction anticipation models. We designed a pipeline and share code for automatic interaction annotation in arbitrary 360-degree equirectangular videos, along with interfaces for manual refinement. Using this pipeline, we release the HUI360 open set of 1M pre-processed annotations, including detailed 2D poses, facial keypoints, and segmentation masks, obtained using state-of-the-art computer vision methods and manually curated to ensure high-quality tracking and interaction annotation. Additionally, we release the raw panoptic 360-degree images captured from the robot's egocentric viewpoint (on demand, for research purpose only in compliance with GDPR). Finally, we establish benchmark baselines for interaction anticipation, including the first cross-dataset evaluations for this task: to this end, we also release 6M annotations for another existing in-the-wild outdoor dataset collected from a mobile robot (SSUP-HRI). Dataset and code can be found at https://hucebot.github.io/hui360.

</details>

---

### [[20_Research/Papers/大模型/ConfTriage_A_Calibration-Aware_LLM_Triage_Framework_for_Pulmonary_Nodule_Malignancy_with_Selective_Specialist_Deferral|ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral]]

![[assets/2608.10885_figure.png|800]]

- **arXiv**: [2608.10885](https://arxiv.org/abs/2608.10885)
- **PDF**: https://arxiv.org/pdf/2608.10885
- **详细分析**: [[20_Research/Papers/大模型/ConfTriage_A_Calibration-Aware_LLM_Triage_Framework_for_Pulmonary_Nodule_Malignancy_with_Selective_Specialist_Deferral|ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral]]
- **作者**: Md Rabiul Islam, Samir Abdaljalil, Erchin Serpedin, Hasan Kurban
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《ConfTriage: A Calibration-Aware LLM Triage Framework for Pulmonary Nodule Malignancy with Selective Specialist Deferral》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Certain-Net, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pulmonary nodule malignancy prediction typically depends on image-trained specialist deep learning (DL) models that require substantial annotated imaging data and task-specific training. We investigate whether a generalist large language model (LLM), reading only a faithful natural-language rendering of standard nodule attributes, can serve as a calibrated triage layer. We propose ConfTriage, a confidence-calibrated method built on three pillars: language as the modality, calibration as the safety mechanism, and a selective specialist DL backstop for low-confidence cases. We prove two guarantees: a finite-sample combined-error bound yielding an explicit per-threshold operational certificate, and an oracle inequality showing that excess risk over the Bayes-optimal deferral classifier is controlled by the L1 calibration error of the LLM probability. A controlled seven-way input ablation across five frontier LLMs on LIDC-IDRI shows that natural-language descriptions dominate the diagnostic signal, while low-level image statistics are essentially diagnostically vacuous. ConfTriage achieved an F1 score of 88.22% and an AUC of 0.92, resolving 76.5% of cases using zero-shot LLM inference alone and referring only uncertain cases to the specialist DL backstop. These results demonstrate that clinically meaningful diagnostic information can be captured through structured radiological descriptions and leveraged by calibrated LLMs for selective referral. The framework suggests a practical pathway for combining generalist LLM prediction with specialist AI models in medical decision-support systems. Source code is publicly available at https://github.com/rabiul-ai/ConfTriage.

</details>

---

### [[20_Research/Papers/具身智能/Multi-View_Relational_Distillation_for_Spatial_Reasoning_with_Vision-Language_Models|Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models]]

![[assets/2608.10864_figure.png|800]]

- **arXiv**: [2608.10864](https://arxiv.org/abs/2608.10864)
- **PDF**: https://arxiv.org/pdf/2608.10864
- **详细分析**: [[20_Research/Papers/具身智能/Multi-View_Relational_Distillation_for_Spatial_Reasoning_with_Vision-Language_Models|Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models]]
- **作者**: Kiet T. Nguyen, Hanbo Shim, Jinwoo Kim, Seunghoon Hong
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.8（加权：具身智能 0.6，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Multi-View Relational Distillation for Spatial Reasoning with Vision-Language Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) have achieved strong image and video understanding, yet their visual-spatial representations remain geometrically fragile, leading to failures in spatial reasoning needed for embodied AI, robotics, and autonomous driving. Prior approaches to geometry grounding either fine-tune VLMs on spatial question answering, which can perpetuate spurious visual representations, or fuse features from large geometry-grounded vision models, which substantially increases model size at inference. Knowledge distillation from geometry-grounded vision models offers an alternative, but directly matching multi-view teacher features can disrupt the pretrained alignment between visual and textual representations, degrading object- and language-semantic capabilities. We propose multi-view relational distillation (MVRD), which distills patch-wise cosine similarities across views instead of the teacher features themselves. These relations encode geometric correspondences adequate for spatial understanding, while leaving the student representation underdetermined, allowing it to remain close to its pretrained vision- language space. Across representative VLMs, MVRD improves visual-spatial reasoning, outperforming supervised fine-tuning and feature distillation while approaching feature fusion methods with considerably fewer added parameters and lower latency. We show that MVRD makes visual representations more geometric while retaining language alignment, and generalizes to 3D scene understanding tasks such as object grounding, dense captioning, and question answering.

</details>

---

### [[20_Research/Papers/强化学习/Flex-$π$_A_Multi-Stream_World-Action_Model_with_Compute_Flexibility|Flex-$π$: A Multi-Stream World-Action Model with Compute Flexibility]]

![[assets/2608.10860_figure.png|800]]

- **arXiv**: [2608.10860](https://arxiv.org/abs/2608.10860)
- **PDF**: https://arxiv.org/pdf/2608.10860
- **详细分析**: [[20_Research/Papers/强化学习/Flex-$π$_A_Multi-Stream_World-Action_Model_with_Compute_Flexibility|Flex-$π$: A Multi-Stream World-Action Model with Compute Flexibility]]
- **作者**: Ge Yan, Jinghao Liu, Yuzhi Fan, Lei Cai, Minwen Liao, Jesse Zhang, Dieter Fox
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Flex-$π$: A Multi-Stream World-Action Model with Compute Flexibility》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgiBot-World, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models (WAMs) predict the future to act better, but nearly all of them predict only RGB latents, trained purely for pixel reconstruction, with no explicit signal for the 3D geometry or object semantics manipulation needs. We find a surprising free lunch: the same frozen video-generation VAE that encodes RGB also encodes 3D pointmaps almost losslessly, with no pointmap-specific training at all. This lets us supervise Flex-$π$, a 6B-parameter WAM, on 3D geometry and object-centric DINO semantics alongside RGB, at no cost in new sensors, new pre-training, or inference latency. Every visual signal is projected into this shared latent space and denoised jointly with actions inside a Mixture-of-Transformers backbone; per-stream dropout with cross-modality forcing then lets a single trained checkpoint run on any subset of these streams, from a fast action-only mode to full joint generation. The result is a policy that is exceptionally demonstration-efficient and generalizes well, beating the strongest baselines by up to 2-7$\times$ on dexterous, precise, real-world bimanual manipulation tasks both in and out of distribution, all while running faster than $π_{0.5}$. Our project website: https://flex-pi.github.io/

</details>

---

### [[20_Research/Papers/大模型/PolyLayout_Hierarchical_VLM-Guided_Layout_Generation_Beyond_Rectangular_Rooms|PolyLayout: Hierarchical VLM-Guided Layout Generation Beyond Rectangular Rooms]]

![[assets/2608.10838_figure.png|800]]

- **arXiv**: [2608.10838](https://arxiv.org/abs/2608.10838)
- **PDF**: https://arxiv.org/pdf/2608.10838
- **详细分析**: [[20_Research/Papers/大模型/PolyLayout_Hierarchical_VLM-Guided_Layout_Generation_Beyond_Rectangular_Rooms|PolyLayout: Hierarchical VLM-Guided Layout Generation Beyond Rectangular Rooms]]
- **作者**: Yutong Jiang, Zahra Atashgahi, Carlos Soto Garcia Delgado, Ruben Brokkelkamp, Davide Zanutto, Efşan Sökmen, Shahin Shahkarami
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《PolyLayout: Hierarchical VLM-Guided Layout Generation Beyond Rectangular Rooms》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating physically plausible 3D room layouts is essential for home furnishing retail, enabling customers to visualize products in their own homes and confidently make purchasing decisions. However, a gap exists between academic research and real-world application: existing solutions primarily focus on algorithmic strategies for furniture placement, largely neglecting the non-rectangular geometries and strict door/window constraints prevalent in real homes. To bridge the gap, we introduce a hybrid, hierarchical framework tailored for retail, specifically designed to support scalable spatial planning applications. Our system decouples generation into three stages: (1) functional furniture clustering and fine-grained intra-zone placement; (2) macro-routing guided by a vision-language model (VLM) to anchor both these clustered zones and any remaining standalone furniture within diverse polygonal boundaries; and (3) rule-based optimization for collision-free micro-arrangements that respect architectural constraints. We evaluate our system on production-scale catalogs and a representative set of irregular real-world topologies. Our results show that our approach attains the highest perceptual plausibility while maintaining good geometric compliance at relatively low latency, and extends to irregular boundaries that existing methods do not natively support.

</details>

---

### [[20_Research/Papers/具身智能/Neural_Introspection_Gating_for_Adaptive_KV-Cache_Reuse_in_Vision-Language-Action_Models|Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models]]

![[assets/2608.10824_figure.png|800]]

- **arXiv**: [2608.10824](https://arxiv.org/abs/2608.10824)
- **PDF**: https://arxiv.org/pdf/2608.10824
- **详细分析**: [[20_Research/Papers/具身智能/Neural_Introspection_Gating_for_Adaptive_KV-Cache_Reuse_in_Vision-Language-Action_Models|Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models]]
- **作者**: Zhijie Wu, Kento Kawaharazuka, Kei Okada
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Neural Introspection Gating for Adaptive KV-Cache Reuse in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA, TinyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action(VLA) models map camera images and language instructions directly to motor commands through a single autoregressive transformer. In real-time control, they still spend substantial compute recomputing key-value(KV) representations for visual tokens that barely change across neighboring frames. Recent work such as VLA-Cache reduces that cost by reusing KV states for visually static patches, but its policy relies only on observation-space heuristics and does not account for the model's own uncertainty. We propose Gated VLA-Cache, a lightweight, training-free extension that augments visual-similarity caching with neural introspection. The method monitors the logit margin between the top two predicted action tokens, a zero-cost confidence signal available during decoding. When the margin drops below a threshold, the cache is invalidated and a full recompute is triggered. Evaluated on four LIBERO benchmark suites with both OpenVLA and OpenVLA-OFT, Gated VLA-Cache improves reliability when blind caching hurts. On LIBERO-Goal and LIBERO-Long, it recovers over 100% of the lost accuracy while retaining 80% of the compute savings.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Multimodal_Grounding_for_Open-Vocabulary_Mobile_Manipulation_via_Semantic_3D_Gaussian_Splatting|Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting]]

![[assets/2608.10756_figure.png|800]]

- **arXiv**: [2608.10756](https://arxiv.org/abs/2608.10756)
- **PDF**: https://arxiv.org/pdf/2608.10756
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Multimodal_Grounding_for_Open-Vocabulary_Mobile_Manipulation_via_Semantic_3D_Gaussian_Splatting|Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting]]
- **作者**: Huosen Ou, Dongni Song, Yuncong Wang, Tao Zhou, Yiding Ji
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 2.1，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Multimodal Grounding for Open-Vocabulary Mobile Manipulation via Semantic 3D Gaussian Splatting》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DexVLA, PointVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied mobile manipulation requires language, visual observations, three-dimensional scene structure, and action feasibility to be aligned before execution. We study open-vocabulary target grounding with few-shot manipulation in local household workspaces and present an embodied multimodal grounding framework that integrates active multi-view Semantic 3D Gaussian Splatting (Semantic-3DGS), reachability-aware base positioning, and a diffusion-based vision-language-action policy. A task-driven local Semantic-3DGS serves as a shared interface across active sensing, language-conditioned 3D localization, obstacle-aware scene reasoning, base preparation, and semantic conditioning of the action model. To preserve pretrained action priors, the 3D semantic cues are injected only into the late action-expert blocks. In expanded 50-trial real-robot evaluations against representative vision-language-action (VLA) approaches, the full system achieves 60% long-horizon success compared with 40% for PointVLA and 28% for DexVLA, and reaches 74% success in heavily cluttered manipulation compared with 52% for the single-view variant and 46% for PointVLA. It also maintains 75% success under a 75 cm height shift and eliminates photo-induced false grasps. These results indicate that explicit, refreshable 3D semantic grounding can improve robustness under clutter, occlusion, viewpoint variation, and embodiment constraints.

</details>

---

### [[20_Research/Papers/具身智能/Precise_Top-Layer_Fabric_Segmentation_for_Fabric_Destacking_with_Edge-_and_Shape-Aware_Deep_Networks|Precise Top-Layer Fabric Segmentation for Fabric Destacking with Edge- and Shape-Aware Deep Networks]]

![[assets/2608.10648_figure.png|800]]

- **arXiv**: [2608.10648](https://arxiv.org/abs/2608.10648)
- **PDF**: https://arxiv.org/pdf/2608.10648
- **详细分析**: [[20_Research/Papers/具身智能/Precise_Top-Layer_Fabric_Segmentation_for_Fabric_Destacking_with_Edge-_and_Shape-Aware_Deep_Networks|Precise Top-Layer Fabric Segmentation for Fabric Destacking with Edge- and Shape-Aware Deep Networks]]
- **作者**: Wenbo Dong, Dipankar Bhattacharya, Akinari Kobayashi, Akira Seino, Fuyuki Tokuda, Xuzhao Huang, Kai Tang, Norman C. Tien, Kazuhiro Kosuge
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Precise Top-Layer Fabric Segmentation for Fabric Destacking with Edge- and Shape-Aware Deep Networks》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BASNet, BiseNet, CASENet, EGNet, SegNet, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fabric destacking requires precise segmentation of the topmost fabric layer, a task complicated by subtle fabric boundaries and high visual similarity between fabric layers. Existing semantic and edge-based segmentation approaches often struggle with these complexities, limiting the performance of robotic manipulation for different tasks. In this work, a novel segmentation training architecture tailored for top-layer fabric segmentation in stacked fabrics is proposed. The method extends the classical encoder-decoder framework by introducing two specialized branches - an edge-aware branch and a shape-aware branch - that are used to supervise the backbone network for better tuning. The edge-aware branch enhances boundary delineation, while the shape-aware branch guides the network to capture and align the overall fabric shape with reference masks derived from Computer Aided Design (CAD) models. Experiments on a real-world fabric dataset demonstrate that the training approach outperforms established baselines, verifying the effectiveness of the multi-branch design through both quantitative results and ablation studies.

</details>

---

### [[20_Research/Papers/强化学习/BooST_Bridging_Semantics_and_Motions_for_Efficient_Skill_Transfer|BooST: Bridging Semantics and Motions for Efficient Skill Transfer]]

![[assets/2608.10600_figure.png|800]]

- **arXiv**: [2608.10600](https://arxiv.org/abs/2608.10600)
- **PDF**: https://arxiv.org/pdf/2608.10600
- **详细分析**: [[20_Research/Papers/强化学习/BooST_Bridging_Semantics_and_Motions_for_Efficient_Skill_Transfer|BooST: Bridging Semantics and Motions for Efficient Skill Transfer]]
- **作者**: Jusuk Lee, Daesol Cho, Jonghun Shin, Seungyeon Yoo, Jonghae Park, Taekbeom Lee, H. Jin Kim
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《BooST: Bridging Semantics and Motions for Efficient Skill Transfer》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Skill abstraction---the process of learning reusable and temporally extended behaviors---has emerged as a key paradigm for improving sample efficiency and generalization in robot learning. For efficient skill transfer to real robots, learned skills must generalize across tasks and domains, remain robust to visual and dynamic perturbations, and be efficient enough for practical deployment. However, existing methods typically satisfy only a subset of these properties, as they capture either high-level semantic intent (what) or low-level motion dynamics (how). This incomplete skill transfer yields weak priors for policy learning, thereby demanding substantial in-domain data for downstream adaptation. To address these challenges, we introduce BooST, a two-stage framework that explicitly bridges semantics and motions to satisfy all three desiderata. BooST first leverages a cross-modal VQ-VAE to capture both semantic intent and motion dynamics, yielding a unified skill representation. It then distills this representation into a lightweight policy for efficient downstream adaptation to new tasks. Extensive experiments across simulation and real-robot settings demonstrate that BooST achieves superior few-shot adaptation, cross-domain skill transfer, and robustness to dynamic visual distractors, while maintaining a lightweight yet expressive design suitable for real-world deployment.

</details>

---

### [[20_Research/Papers/具身智能/DriveVLA-M0_Failure-Aware_Memory_Augmentation_for_Autonomous_Driving|DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving]]

![[assets/2608.10413_figure.png|800]]

- **arXiv**: [2608.10413](https://arxiv.org/abs/2608.10413)
- **PDF**: https://arxiv.org/pdf/2608.10413
- **详细分析**: [[20_Research/Papers/具身智能/DriveVLA-M0_Failure-Aware_Memory_Augmentation_for_Autonomous_Driving|DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving]]
- **作者**: Zebin Xing, Yupeng Zheng, Qiang Chen, Linbo Wang, Yichen Zhang, Pengxuan Yang, Junli Wang, Deheng Qian, Xiaoqing Ye, Junyu Han, Yifeng Pan, Qichao Zhang...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.8（加权：具身智能 0.6，大模型 0.2）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《DriveVLA-M0: Failure-Aware Memory Augmentation for Autonomous Driving》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AutoVLA, DriveVLA, ELF-VLA, EchoVLA, EvoVLA, MemoNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have recently emerged as a promising paradigm for end-to-end autonomous driving by enabling unified reasoning across perception, language, and planning. However, existing approaches lack mechanisms to exploit past failures or adapt to distribution shifts, causing the model to persistently underperform on similar scenarios where it has previously failed. In this paper, we propose DriveVLA-M0, a retrieval-augmented VLA with failure-aware latent memory. We construct a latent memory pool that stores failure cases along with their structure scene representations and expert trajectory labels, and design a dedicated Retrieve Model that decouples static road structure and dynamic agent interactions to enable structurally grounded retrieval. At inference time, retrieved cases are injected into the model via a lightweight decoupled LoRA-based test-time training (TTT) mechanism, allowing targeted and scenario-specific correction without modifying the backbone. Extensive experiments on NAVSIMv1 and NAVSIMv2 benchmark demonstrate that our approach consistently outperforms prior methods, achieving 94.1 PDMS on Navtest and 47.0 EPDMS on Navhard with only 26.44 ms TTT backward latency overhead. Furthermore, we show that DriveVLA-M0 scales effectively with additional memory, enabling training-free performance gains through memory expansion. The code is available at https://github.com/ZebinX/DriveVLA-M0.

</details>

---

### [[20_Research/Papers/具身智能/Chain_of_Spatial_Thoughts_Modality-Agnostic_Spatial_Grounding_for_Vision_Language_Models|Chain of Spatial Thoughts: Modality-Agnostic Spatial Grounding for Vision Language Models]]

![[assets/2608.10278_figure.png|800]]

- **arXiv**: [2608.10278](https://arxiv.org/abs/2608.10278)
- **PDF**: https://arxiv.org/pdf/2608.10278
- **详细分析**: [[20_Research/Papers/具身智能/Chain_of_Spatial_Thoughts_Modality-Agnostic_Spatial_Grounding_for_Vision_Language_Models|Chain of Spatial Thoughts: Modality-Agnostic Spatial Grounding for Vision Language Models]]
- **作者**: Hunter Schofield, Mohammed Elmahgiubi, Mohammad Mahdavian, Richard Shi, Jinjun Shan, Amir Rasouli, Dongfeng Bai
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Chain of Spatial Thoughts: Modality-Agnostic Spatial Grounding for Vision Language Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VQA, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Spatial understanding is fundamental to embodied intelligence, underpinning applications such as robotic manipulation, embodied navigation, and autonomous driving. Although recent vision-language models (VLMs) have achieved impressive performance on spatial reasoning benchmarks, state-of-the-art approaches typically rely on additional spatial encoders or architectural modifications during inference, increasing computational cost. We introduce Space Tokens, a lightweight, architecture-agnostic framework that equips VLMs with explicit continuous spatial representations without requiring additional inference-time modules. By distilling scene-level 3D geometry and object-centric spatial attributes into continuous latent tokens, our method enables these modalities to be directly incorporated into a chain-of-thought reasoning process, thereby improving the VLM's spatial reasoning capabilities. At the same time, the learned representations can be explicitly decoded to verify that they encode meaningful geometric information, while the unified token interface remains extensible to additional modalities. Experiments on VSI-Bench improve Qwen3-VL-8B by 4.3% and SenseNova-SI-1.3 by 1.3%, while achieving state-of-the-art performance on object size (79.2%) and room size estimation (75.7%). These results demonstrate that continuous spatial tokens provide an effective, interpretable, and computationally efficient mechanism for integrating geometric reasoning into large vision-language models.

</details>

---
