# cs.CV | Computer Vision and Pattern Recognition | 2026-07-20

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/Knowing_the_Self,_Understanding_the_World_A_Dual-Cognition_Benchmark_for_UAV_Spatio-temporal_Reasoning_with_MLLMs|Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs]]

![[assets/2607.16193_figure.png|800]]

- **arXiv**: [2607.16193](https://arxiv.org/abs/2607.16193)
- **PDF**: https://arxiv.org/pdf/2607.16193
- **详细分析**: [[20_Research/Papers/具身智能/Knowing_the_Self,_Understanding_the_World_A_Dual-Cognition_Benchmark_for_UAV_Spatio-temporal_Reasoning_with_MLLMs|Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs]]
- **作者**: Like Liu, Zhengzheng Xu, Haitao He, Hongzhe Li, Shuchang Zhang, Dian Shao
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.1（加权：大模型 0.3，机器人 0.8）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Knowing the Self, Understanding the World: A Dual-Cognition Benchmark for UAV Spatio-temporal Reasoning with MLLMs》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CityEQA, HUGE-Bench, Open3D-VQA, SIS-Bench, UrbanVideo-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models have achieved strong performance across diverse vision-language tasks, yet their capabilities in UAV scenarios remain insufficiently explored. Recent UAV-oriented benchmarks have begun to evaluate MLLMs in aerial scenarios, but they typically focus on scene understanding, event recognition, or navigation completion, rather than jointly assessing the dual-cognition capability required for UAV agents: reasoning about both the UAV's own state and the external environment in multiview spatio-temporal contexts. To address this gap, we present UAV-DualCog, a benchmark for aerial multiview spatio-temporal reasoning built on this dual-cognition perspective. UAV-DualCog includes both image and video tasks to jointly evaluate self-state and environment-state reasoning, while requiring spatial or temporal grounding beyond discrete answer prediction. We also develop an automated pipeline that constructs data from scene-level semantic point clouds, yielding a scalable benchmark with diverse scenes, hundreds of landmarks, and thousands of QA samples. Extensive evaluations show that current MLLMs remain far from reliable in UAV dual cognition. Self-state reasoning, viewpoint transformation, precise spatial grounding, and temporal interval localization are persistent bottlenecks, and additional validation with thinking/frontier models and a human baseline confirms that the benchmark is understandable to humans but challenging for existing models. We further construct UAV-DualCog-Train from disjoint scenes and show through a lightweight optimization probe that it provides useful structured supervision, suggesting its value not only as an evaluation benchmark but also as a data resource for advancing MLLM-based UAV agents. Project website and supplementary materials: https://uav-dualcog.lozumi.com

</details>

---

### [[20_Research/Papers/具身智能/Searching_Videos_as_Trees_Self-Correcting_Agents_for_Grounded_Long_Video_QA|Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA]]

![[assets/2607.16189_figure.png|800]]

- **arXiv**: [2607.16189](https://arxiv.org/abs/2607.16189)
- **PDF**: https://arxiv.org/pdf/2607.16189
- **详细分析**: [[20_Research/Papers/具身智能/Searching_Videos_as_Trees_Self-Correcting_Agents_for_Grounded_Long_Video_QA|Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA]]
- **作者**: Ce Zhang, Ziyang Wang, Yulu Pan, Oluwatumininu Oguntola, Pranav Wagh, Qiyu Wu, Hiromi Wakaki, Mohit Bansal, Gedas Bertasius
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Searching Videos as Trees: Self-Correcting Agents for Grounded Long Video QA》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CG-Bench, Haystack-LVBench, LVBench, LVQA, LongClueQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Grounded long-video question answering (Grounded LVQA) requires answering a question about a long video while localizing the short evidence interval that supports the answer. Recent agentic methods frame this task as multi-turn exploration with a single crop_video(start, end) action, which supports coarse-to-fine narrowing but provides no primitive for fine-to-coarse backtracking. As a result, these agents typically converge prematurely and cannot recover from an early mistake. We propose VideoTreeSearch (VTS), a framework that casts grounded LVQA as iterative self-correcting search over an adaptive temporal tree. VTS constructs a non-uniform tree from visual scene boundaries so that each node corresponds to a semantically coherent segment, and trains an agent to navigate the tree through four discrete operations: zoom_in, zoom_out, shift, and answer. These operations expose backtracking and recovery as explicit, learnable primitives rather than implicit behaviors. To train this navigation, we introduce a trajectory synthesis pipeline that produces multi-step paths through the tree, including deliberate detours into incorrect branches followed by recovery. We use these trajectories for supervised fine-tuning, followed by reinforcement learning with grounding and answer-accuracy rewards. On three Grounded LVQA benchmarks (CG-Bench, Haystack-LVBench, Haystack-Ego4D), VTS outperforms the strongest prior agentic methods by +12.5 mIoU on CG-Bench and +7.4 T-F1 on Haystack-Ego4D. The learned policy also transfers to general long-video QA, surpassing all prior agentic baselines on Video-MME, MLVU, and LVBench by up to +7.1 accuracy points. Ablations confirm that self-correcting hierarchical search is the central mechanism behind these gains: removing either adaptive descent or explicit backtracking substantially degrades performance. Code is available at https://github.com/CeeZh/VTS.

</details>

---

### [[20_Research/Papers/机器人/VTLoc_Learning-based_Tactile_Contact_Localization_in_Visual_Point_Clouds|VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds]]

![[assets/2607.16146_first_page.png|800]]

- **arXiv**: [2607.16146](https://arxiv.org/abs/2607.16146)
- **PDF**: https://arxiv.org/pdf/2607.16146
- **详细分析**: [[20_Research/Papers/机器人/VTLoc_Learning-based_Tactile_Contact_Localization_in_Visual_Point_Clouds|VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds]]
- **作者**: Zhiyuan Wu, Zhuo Chen, Shan Luo
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《VTLoc: Learning-based Tactile Contact Localization in Visual Point Clouds》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision and touch are complementary modalities essential for robotic perception and manipulation. While vision provides global object context, touch offers precise local information at contact points. Integrating these modalities for contact localization, i.e., predicting the location of touch on an object's surface, poses significant challenges due to the need for accurate spatial alignment between tactile data and visual geometry. To address this challenge, we propose VTLoc, a novel visual-tactile framework that localizes contact points from tactile readings using a 3D point cloud as visual input. VTLoc introduces two key components: a geometric multi-modal alignment module, which reconstructs a pseudo-point cloud from fused visual-tactile features and aligns it with the visual point cloud to enforce spatial consistencies across modalities; and an iterative localizing updater, which iteratively refines the predicted contact location using fused visual-tactile features. Evaluated on a new benchmark of 100 real-world objects, VTLoc improves single-touch contact localization by reducing local-to-global correspondence ambiguity.

</details>

---

### [[20_Research/Papers/机器人/PIXIE_A_Zero-Shot_texture-invariant_6D_pose_estimation_framework_for_unseen_objects_with_assembly_defects|PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects]]

![[assets/2607.16015_figure.jpg|800]]

- **arXiv**: [2607.16015](https://arxiv.org/abs/2607.16015)
- **PDF**: https://arxiv.org/pdf/2607.16015
- **详细分析**: [[20_Research/Papers/机器人/PIXIE_A_Zero-Shot_texture-invariant_6D_pose_estimation_framework_for_unseen_objects_with_assembly_defects|PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects]]
- **作者**: Leon Jungemeyer, Alejandro Magaña, Gautham Mohan, Matthias Karl, Daniel Werdehausen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《PIXIE: A Zero-Shot texture-invariant 6D pose estimation framework for unseen objects with assembly defects》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

6D pose estimation remains a key challenge in robotics and computer vision, particularly in industrial environments. The deployment of currently available data-driven methods is often limited by resource-intensive data pipelines, reliance on textured 3D models, and sensitivity to geometric deviations caused by damages or assembly defects. We present PIXIE, a zero-shot framework that estimates the 6D pose of an object from an RGB image using only an untextured 3D model. Synthetic depth and normal maps are rendered from sampled reference viewpoints and matched to the query image via a pretrained cross-modality feature matcher. Matched keypoints are back-projected to obtain 2D--3D correspondences for PnP-based pose estimation. Relying exclusively on geometry makes the method inherently robust to lighting and texture variation, while correspondence filtering handles geometric deviations between the model and physical object. We evaluate on widely-used public benchmarks, reporting state-of-the-art results on texture-less objects without object-specific training, and introduce a novel dataset with assembly defects, texture variations, and occlusion to demonstrate real-world applicability.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Active_Learning_under_Limited_Annotation_and_Navigation_Budget_for_Object_Detection|Embodied Active Learning under Limited Annotation and Navigation Budget for Object Detection]]

![[assets/2607.15974_figure.png|800]]

- **arXiv**: [2607.15974](https://arxiv.org/abs/2607.15974)
- **PDF**: https://arxiv.org/pdf/2607.15974
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Active_Learning_under_Limited_Annotation_and_Navigation_Budget_for_Object_Detection|Embodied Active Learning under Limited Annotation and Navigation Budget for Object Detection]]
- **作者**: Hadrien Crassous, Mohamed Yassine Kabouri, Minahil Raza, Joni Pajarinen, Riad Akrour
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied Active Learning under Limited Annotation and Navigation Budget for Object Detection》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies how to adapt a computer vision object detector to an unknown environment under both a robot navigation time and annotation budget constraint. Our approach selects informative robot trajectories and image samples to retrain the detector, explicitly targeting its failure cases. Formally, the approach is an embodied variant of batch active learning, where at each round an agent has a limited navigation budget to collect candidate samples and a limited annotation budget for the most relevant images. We leverage spatial consistency to identify images with inconsistent labels, which are likely to provide the greatest improvement to the vision model. We evaluate the approach using different active learning objectives on large scenes from the AI2-THOR simulator and on a real-world setup using a Boston Dynamics Spot robot with the real-time object detector YOLOv5. Through comparison against several baselines, our experimental results show that spatial inconsistency helps guide the agent and select relevant images without external supervision, achieving the highest detection accuracy at the end of the adaptation process under the same budget. The open-source project can be found at https://mkabouri.github.io/embodied-active-learning-od

</details>

---

### [[20_Research/Papers/大模型/More_with_Less_a_Large_Scale_Remote_Sensing_VLM_with_a_Simple_Recipe|More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe]]

![[assets/2607.15942_figure.png|800]]

- **arXiv**: [2607.15942](https://arxiv.org/abs/2607.15942)
- **PDF**: https://arxiv.org/pdf/2607.15942
- **详细分析**: [[20_Research/Papers/大模型/More_with_Less_a_Large_Scale_Remote_Sensing_VLM_with_a_Simple_Recipe|More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe]]
- **作者**: Stefan Maria Ailuro, Mario Markov, Mohammad Mahdi, Luc Van Gool, Danda Pani Paudel
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习, 世界模型
- **相关性评分**: 1.02（加权：大模型 0.5，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《More with Less: a Large Scale Remote Sensing VLM with a Simple Recipe》归入 大模型、强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LRS-VQA, MC-VQA, VQA, XLRS-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Remote sensing vision-language models are increasingly expected to support open-ended reasoning over Earth Observation data and a variety of tasks. Most recent progress in this area has been driven by remote-sensing-specific architectural designs, often introducing new encoders, alignment modules, or task-specific fusion mechanisms. In this work, we challenge the necessity of such architectural specialization. We show that a generally capable vision-language model can achieve competitive or state-of-the-art performance at challenging remote sensing benchmarks, provided that it is trained at sufficient scale across diverse data and tasks. Our model uses a single language policy that can either answer directly in text or invoke a localization tool for segmentation and grounding. To train this heterogeneous behaviour, we employ a multi-task reinforcement learning framework with adaptive task rewards covering multiple-choice VQA, free-form VQA, captioning, detection, and segmentation across a large variety of input types. Our approach achieves competitive results across a broad set of benchmarks, including high-resolution, multi-temporal, multi-modal and multi-view tasks. Further, as training data scales, our experiments show consistent improvements across most tasks both in and out of distribution, which correlate with per-task data diversity. These findings suggest that, for remote sensing VLMs, data scale is more important than architectural novelty.

</details>

---

### [[20_Research/Papers/具身智能/Exo2EgoPose_Leveraging_Exocentric_Demonstrations_for_Vision-Language_guided_Egocentric_3D_Hand_Pose_Forecasting|Exo2EgoPose: Leveraging Exocentric Demonstrations for Vision-Language guided Egocentric 3D Hand Pose Forecasting]]

![[assets/2607.15890_figure.png|800]]

- **arXiv**: [2607.15890](https://arxiv.org/abs/2607.15890)
- **PDF**: https://arxiv.org/pdf/2607.15890
- **详细分析**: [[20_Research/Papers/具身智能/Exo2EgoPose_Leveraging_Exocentric_Demonstrations_for_Vision-Language_guided_Egocentric_3D_Hand_Pose_Forecasting|Exo2EgoPose: Leveraging Exocentric Demonstrations for Vision-Language guided Egocentric 3D Hand Pose Forecasting]]
- **作者**: Zhaofeng Shi, Heqian Qiu, Lanxiao Wang, Xiang Li, Hongliang Li
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.6，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Exo2EgoPose: Leveraging Exocentric Demonstrations for Vision-Language guided Egocentric 3D Hand Pose Forecasting》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perceiving multimodal cues and forecasting fine-grained actions from an egocentric (Ego) perspective is vital for applications like robot manipulation. However, previous studies either rely mainly on under-informed visual inputs to predict coarse human motions or follow the VRM/VLA paradigm, which suffers from insufficient robot data and the gap between human and robot embodiments. We observe that 3D hand pose naturally serves as a unified representation to bridge human-robot actions. Hence, we investigate an under-explored Vision-Language guided Egocentric 3D Hand Pose Forecasting (VL-EHPF) task, which aims to predict future Ego 3D hand poses from visual observations, a language instruction, and pose states. To overcome the limited field-of-view and highly dynamic motions in the Ego view, we propose a framework dubbed Exo2EgoPose, which innovatively leverages holistic and stable exocentric (Exo) demonstrations as guidance to compensate for partial and dynamic Ego-view cues. Specifically, we introduce a Dual-level Exocentric Reconstruction Module (DERM), which incorporates the paired Exo videos as supervision to reconstruct their video-level and chunked frame-level representations, thereby modeling spatial contexts and temporal dynamics. Then, the Global-to-Local Modulation Module (GLMM) utilizes the reconstructed hierarchical Exo representations for progressive feature refinement via attention mechanisms and adaptive modulation, enabling comprehensive Exo guidance for accurate Ego hand pose forecasting. Extensive experiments on \textit{AssemblyHands}, \textit{Ego-Exo4D}, and our newly constructed \textit{EgoMe-pose} benchmarks show the superiority of our method, which outperforms state-of-the-art methods by a large margin. Moreover, it demonstrates an effective human-to-robot transfer capability and yields improvements on the \textit{CALVIN} dataset. Code will be released.

</details>

---

### [[20_Research/Papers/机器人/Beyond_Frontiers_Scene-Anomaly_Guided_Autonomous_Exploration|Beyond Frontiers: Scene-Anomaly Guided Autonomous Exploration]]

![[assets/2607.15828_figure.png|800]]

- **arXiv**: [2607.15828](https://arxiv.org/abs/2607.15828)
- **PDF**: https://arxiv.org/pdf/2607.15828
- **详细分析**: [[20_Research/Papers/机器人/Beyond_Frontiers_Scene-Anomaly_Guided_Autonomous_Exploration|Beyond Frontiers: Scene-Anomaly Guided Autonomous Exploration]]
- **作者**: Akash Kumbar, Abhinav Raundhal, Madhava Krishna
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Beyond Frontiers: Scene-Anomaly Guided Autonomous Exploration》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous exploration of unknown 3D environments is traditionally driven by coverage-maximizing geometric heuristics. However, these methods typically determine exploration targets without considering the underlying structural context. This leads to inefficient trajectories often limiting the fidelity of the final 3D reconstruction. To bridge the gap between spatial coverage and reconstruction quality, we introduce a novel paradigm: reframing exploration as a geometric anomaly minimization problem. We present SCAGE: SCene Anomaly Guided Exploration, a novel autonomous exploration framework that operates directly on unstructured 3D point clouds. Instead of blindly chasing volumetric boundaries, we equip the robot with a foundational understanding of standard indoor architecture. As the robot navigates, it continuously evaluates its live 3D observations against these learned expectations. When the incoming geometry contradicts the learned priors of a typical indoor environment, such as a fragmented wall or a partial table, the system flags these regions as scene anomalies. These geometric inconsistencies act as a guiding signal, naturally drawing the robot to investigate and resolve these structural anomalies from optimal vantage points. By actively targeting poorly reconstructed regions rather than just empty space, our approach seamlessly couples spatial discovery with high-fidelity mapping. Extensive evaluations demonstrate that SCAGE achieves superior volumetric coverage (~90% in all scenes) and higher 3D reconstruction quality compared to state-of-the-art baselines.

</details>

---

### [[20_Research/Papers/具身智能/Event3R_Asynchronous-to-Global_3D_Reconstruction_from_Event_Camera_via_Spatial-Temporal_Feature_Aggregation|Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation]]

![[assets/2607.15727_figure.png|800]]

- **arXiv**: [2607.15727](https://arxiv.org/abs/2607.15727)
- **PDF**: https://arxiv.org/pdf/2607.15727
- **详细分析**: [[20_Research/Papers/具身智能/Event3R_Asynchronous-to-Global_3D_Reconstruction_from_Event_Camera_via_Spatial-Temporal_Feature_Aggregation|Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation]]
- **作者**: Jian Huang, Haotian Shen, Xinhao Lou, Chengrui Dong, Wenpu Li, Peidong Liu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.5（加权：具身智能 0.3，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Event3R: Asynchronous-to-Global 3D Reconstruction from Event Camera via Spatial-Temporal Feature Aggregation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust 3D reconstruction is essential for robotics and embodied perception. Recent feed-forward approaches such as DUSt3R have demonstrated impressive progress in dense 3D reconstruction from RGB images, achieving global geometric consistency and strong generalization. However, extending such dense 3D reconstruction to event cameras remains challenging due to their asynchronous, sparse, and highly dynamic nature, as well as the lack of large-scale, well-labeled datasets. In this work, we introduce Event3R, a feed-forward framework that directly maps asynchronous event streams to globally consistent 3D point clouds. Event3R represents incoming events as spatial-temporal voxels, enabling time-aware feature integration through a temporal attention module that enhances the module's temporal feature learning. To further strengthen temporal representation learning and reduce reliance on labeled data, we propose a Masked Bin Modeling (MBM) strategy for self-supervised pre-training, enabling robust temporal representation learning with minimal labeled data, and retain it as an auxiliary fine-tuning objective. In addition, contrastive alignment and consistency regularization losses are incorporated during fine-tuning to reinforce structural correspondence and temporal coherence across views. Extensive experiments on both synthetic and real-world benchmarks demonstrate that Event3R achieves robust, temporally consistent, and globally aligned 3D reconstructions, significantly outperforming existing event-based methods.

</details>

---

### [[20_Research/Papers/强化学习/GoStop_Reinforcement_Learning_for_Adaptive_Temporal_Aggregation_in_Event-Based_Feature_Tracking|GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking]]

![[assets/2607.15699_figure.png|800]]

- **arXiv**: [2607.15699](https://arxiv.org/abs/2607.15699)
- **PDF**: https://arxiv.org/pdf/2607.15699
- **详细分析**: [[20_Research/Papers/强化学习/GoStop_Reinforcement_Learning_for_Adaptive_Temporal_Aggregation_in_Event-Based_Feature_Tracking|GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking]]
- **作者**: Youngho Kim, Hoonhee Cho, Jae-Young Kang, Kuk-Jin Yoon
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，强化学习 0.8）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《GoStop: Reinforcement Learning for Adaptive Temporal Aggregation in Event-Based Feature Tracking》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Feature tracking plays a fundamental role in understanding scene motion and supports various downstream tasks. Event cameras, with their high temporal resolution and asynchronous sensing, enable low-latency and motion-robust perception, making them well-suited for feature tracking under fast and non-linear motion. However, existing event-based feature tracking methods rely on fixed heuristic rules based on hand-tuning for event accumulation. Such strategies fail to adapt to diverse motion dynamics, leading to degraded performance under abrupt motion changes or low-motion scenarios. In this paper, we model event accumulation as a sequential decision-making problem and introduce reinforcement learning (RL) framework to adaptively control the accumulation process for online event-based feature tracking. Our approach trains a RL agent that decides whether to continue accumulating events or to perform tracking inference based on motion cues. The proposed adaptive temporal agent enables dynamic adaptation to varying motion patterns without relying on hand-crafted rules. Furthermore, we introduce a Dynamic Event-based Tracking (DEFT) dataset with dynamic motion distributions to evaluate the robustness of the feature tracking. Extensive experiments demonstrate that integrating our plug-and-play framework to existing feature tracking methods consistently outperforms heuristic-based approaches, improving robustness under dynamic motion while offering a better balance between tracking accuracy and efficiency. Our project codes and datasets are available at https://github.com/kmax2001/GoSTOP

</details>

---

### [[20_Research/Papers/大模型/Efficient_Frame_Selection_for_Long_Videos_at_Test_Time_with_Attention-Based_MLLM_Selectors|Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors]]

![[assets/2607.15689_figure.png|800]]

- **arXiv**: [2607.15689](https://arxiv.org/abs/2607.15689)
- **PDF**: https://arxiv.org/pdf/2607.15689
- **详细分析**: [[20_Research/Papers/大模型/Efficient_Frame_Selection_for_Long_Videos_at_Test_Time_with_Attention-Based_MLLM_Selectors|Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors]]
- **作者**: Yilin Wang, Xiangxi Zheng, Dongxing Mao, Linjie Li, Zhengyuan Yang, Ping Yu, Rui Yan, Yuan Yao, Alex Jinpeng Wang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Efficient Frame Selection for Long Videos at Test Time with Attention-Based MLLM Selectors》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：NExT-GQA, ViaRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding long videos with multimodal large language models (MLLMs) requires selecting a compact set of frames from thousands of candidates, yet identifying the right frames seemingly requires understanding the video first. We resolve this circular dependency with a simple observation: cross-modal attention at validation-selected extraction layers in MLLMs already provides query-relevant frame evidence without requiring autoregressive generation. We exploit this property to build DAFS (Dynamic Attention-based Budget-aware Frame Selection), a training-free frame selector. A lightweight MLLM selector, even with only 2B parameters, can extract frame-level evidence by converting selected-layer attention into relevance scores through query-conditioned aggregation. This enables cross-frame comparison without autoregressive decoding. To handle the selector's own context constraint, we formulate the joint allocation of candidate pool size and per-frame token budget as a discrete optimization problem solved by dynamic programming. Under a 32-frame budget, our selector improves over uniform sampling by up to 6.4 points on Video-MME and outperforms prior training-based selectors under matched frame budgets, while generalizing across selector and answerer backbones, and across tasks, without retraining.

</details>

---

### [[20_Research/Papers/具身智能/ImprovedVBGS_Real-time_Continual_Variational_Bayes_Gaussian_Splatting|ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting]]

![[assets/2607.15542_figure.png|800]]

- **arXiv**: [2607.15542](https://arxiv.org/abs/2607.15542)
- **PDF**: https://arxiv.org/pdf/2607.15542
- **详细分析**: [[20_Research/Papers/具身智能/ImprovedVBGS_Real-time_Continual_Variational_Bayes_Gaussian_Splatting|ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting]]
- **作者**: Damani Mguni-Coker
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《ImprovedVBGS: Real-time Continual Variational Bayes Gaussian Splatting》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

On-the-fly reconstruction is a key requirement for many applications in robotics and autonomous navigation. Variational Bayes Gaussian Splatting (VBGS) enables continual learning without replay buffers using Coordinate Ascent Variational Inference (CAVI), but its per-frame iterations over all observed points make it too slow for real-time use with strict memory and latency requirements. We present ImprovedVBGS, an accelerated framework for on-the-fly continual reconstruction. This is achieved primarily through (i) spatially truncated variational inference, and (ii) improved reassignment that uses forwarding, truncation and eliminates wasteful dynamic recompilation. On the NeRF synthetic dataset, we reduce mean per-frame latency from ~84.0 s to ~0.050 s on an RTX 3070 Ti, a 1680x speed-up while maintaining reconstruction quality.

</details>

---

### [[20_Research/Papers/大模型/Reasoning-Guided_Part-Level_Visual_Grounding_via_Reinforcement_Learning|Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning]]

![[assets/2607.15374_first_page.png|800]]

- **arXiv**: [2607.15374](https://arxiv.org/abs/2607.15374)
- **PDF**: https://arxiv.org/pdf/2607.15374
- **详细分析**: [[20_Research/Papers/大模型/Reasoning-Guided_Part-Level_Visual_Grounding_via_Reinforcement_Learning|Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning]]
- **作者**: Kazi Sajeed Mehrab, Hani Alomari, Najibul Haque Sarker, Chia-Wei Tang, Zaber Ibn Abdul Hakim, Anuj Karpatne, Chris Thomas
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.7（加权：大模型 0.1，强化学习 0.6）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Reasoning-Guided Part-Level Visual Grounding via Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现。 可见文本中出现的评测对象/数据集包括：PartImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models (MLLMs) ground whole objects well from free-form language queries, but they struggle when the query names a part rather than the object. We trace this to a missing object-part hierarchy, since parts are localized in the same single step used for objects. We propose Object-Part Hierarchical Reflective Grounding (OP-HRG), a coarse-to-fine reasoning-guided grounding strategy that first localizes the parent object and then the part within it. A self-check then reflects on the result, with an extension to re-encode the predicted crop to inspect the region it is correcting. We introduce a part-aware GRPO framework to train our pipeline with stage-wise rewards. A 4B model trained this way outperforms 7B grounding LLMs and SAM3 across PascalPart, PartImageNet, and InstructPart, and transfers to reasoning segmentation.

</details>

---

### [[20_Research/Papers/具身智能/Xiaomi-Robotics-1_Scaling_Vision-Language-Action_Models_with_over_100K_Hours_of_Real-World_Trajectories|Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories]]

![[assets/2607.15330_figure.png|800]]

- **arXiv**: [2607.15330](https://arxiv.org/abs/2607.15330)
- **PDF**: https://arxiv.org/pdf/2607.15330
- **详细分析**: [[20_Research/Papers/具身智能/Xiaomi-Robotics-1_Scaling_Vision-Language-Action_Models_with_over_100K_Hours_of_Real-World_Trajectories|Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories]]
- **作者**: Xiaomi Robotics Team, Jun Guo, Piaopiao Jin, Jason Li, Peiyan Li, Yingyan Li, Futeng Liu, Wanli Peng, Optimus Qin, Yifei Su, Nan Sun, Qiao Sun...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Xiaomi-Robotics-1: Scaling Vision-Language-Action Models with over 100K Hours of Real-World Trajectories》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Xiaomi-Robotics-1, a foundational vision-language-action (VLA) model capable of (1) following diverse language instructions to perform a wide range of mobile manipulation tasks in unseen environments out-of-the-box, and (2) efficiently adapting to novel downstream tasks with minimal fine-tuning data. We propose a two-stage training recipe consisting of pre-training and post-training. During pre-training, we imbue the model with broad and generalizable action-generation capabilities by training on over 100k hours of real-world manipulation trajectories collected via UMI devices. Crucially, we develop a scalable auto-labeling pipeline that annotates trajectory clips with natural languages describing scene state transitions, providing rich and precise conditioning for action learning. During post-training, we aim to align these capabilities with robot embodiments and imperative instructions that humans naturally use to prompt robots. Extensive experiments demonstrate strong scaling behavior. Xiaomi-Robotics-1 consistently improves with increased data scales and model sizes during pre-training. This scaling behavior directly transfers to post-training, where a stronger pre-training model yields better out-of-the-box real-robot performance in unseen environments. Furthermore, Xiaomi-Robotics-1 serves as a strong robot foundation policy that can be efficiently fine-tuned on complex, dexterous tasks with high data efficiency. Across multiple simulation benchmarks, Xiaomi-Robotics-1 outperforms state-of-the-art methods. Notably, it establishes a new state-of-the-art with a 57.6% success rate on RoboCasa365, surpassing the previous best of 46.6%. Furthermore, it achieves an average score of 20.07 on RoboDojo, significantly outperforming the prior state-of-the-art (13.07). Code and model checkpoints will be released. Project page: https://robotics.xiaomi.com/xiaomi-robotics-1.html

</details>

---

### [[20_Research/Papers/大模型/MLLM-DataEngine_Closing_the_Loop_of_Multimodal_Instruction_Tuning_Data_Generation|MLLM-DataEngine: Closing the Loop of Multimodal Instruction Tuning Data Generation]]

![[assets/2607.15299_figure.png|800]]

- **arXiv**: [2607.15299](https://arxiv.org/abs/2607.15299)
- **PDF**: https://arxiv.org/pdf/2607.15299
- **详细分析**: [[20_Research/Papers/大模型/MLLM-DataEngine_Closing_the_Loop_of_Multimodal_Instruction_Tuning_Data_Generation|MLLM-DataEngine: Closing the Loop of Multimodal Instruction Tuning Data Generation]]
- **作者**: Zhiyuan Zhao, Bin Wang, Linke Ouyang, Yiqi Lin, Pan Zhang, Xiaoyi Dong, Jiaqi Wang, Conghui He
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: Multimodal, Systems

#### 研究背景与动机

《MLLM-DataEngine: Closing the Loop of Multimodal Instruction Tuning Data Generation》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GQA, MMBench, OK-VQA, SEED-Bench, ScienceQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we propose MLLM-DataEngine, a novel closed-loop system that bridges data generation, model training, and evaluation. Within each loop iteration, the MLLM-DataEngine first analyzes the weakness of the model based on the evaluation results, then generates a proper incremental dataset for the next training iteration, and enhances the model capability iteratively. Compared with previous instruction fine-tuning dataset collection methods which are separate from the benchmarking, MLLM-DataEngine shows better targeting and can improve MLLMs's capabilities more effectively. Firstly, we propose an Adaptive Bad-case Sampling module, which can effectively analyze model weakness based on the benchmarking results and adjust the generation of incremental datasets flexibly. Secondly, in order to ensure high-quality data for specific capability types, the most representative in-context examples and abundant information are provided to GPT-4, which helps GPT-4 fully comprehend the model's weakness and further guarantees high-quality generated data. Through extensive experiments, we find MLLM-DataEngine could boost the MLLMs capability in a targeted and automatic manner without human participants. We hope MLLM-DataEngine could be a general solution for the following MLLMs data curation. Code, data, and model are available at https://github.com/opendatalab/MLLM-DataEngine.

</details>

---
