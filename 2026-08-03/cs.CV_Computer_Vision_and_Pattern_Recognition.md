# cs.CV | Computer Vision and Pattern Recognition | 2026-08-03

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/CodeShrink_Adaptive_Visual_Compression_for_Efficient_Multimodal_Code_Understanding|CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding]]

![[assets/2607.29637_figure.png|800]]

- **arXiv**: [2607.29637](https://arxiv.org/abs/2607.29637)
- **PDF**: https://arxiv.org/pdf/2607.29637
- **详细分析**: [[20_Research/Papers/大模型/CodeShrink_Adaptive_Visual_Compression_for_Efficient_Multimodal_Code_Understanding|CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding]]
- **作者**: Wenxin Tang, Jingyu Xiao, Zhenyu Liu, Zipeng Xie, Junliang Liu, Wang Luo, Yuan Jiang, Yintong Huo, Michael Lyu
- **cs 子类**: cs.CV, cs.SE
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.7（加权：大模型 0.5，强化学习 0.2）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《CodeShrink: Adaptive Visual Compression for Efficient Multimodal Code Understanding》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rendering source code as images offers a promising way to reduce the input costs of Multimodal Large Language Models (MLLMs). Adjusting image resolution can trade visual token cost against content fidelity. However, resolution scaling alone overlooks two sources of inefficiency: blank regions created by line breaks and indentation, and code regions irrelevant to the current instruction. Moreover, the best compression setting varies across inputs, tasks, and models, limiting fixed-ratio strategies. We propose CodeShrink, an adaptive visual compression framework with three components. Blank-Free Rendering replaces whitespace-dependent layouts with compact layouts and explicit structural markers, removing layout-induced tokens. Adaptive Compression Configuration uses a lightweight agent trained with reinforcement learning to predict a per-input setting that balances token efficiency and readability. Dominant Token Selection jointly analyzes the instruction and code image to prune task-irrelevant visual tokens during inference. We evaluate CodeShrink on code question answering, clone detection, and code completion. CodeShrink reduces visual token use by up to 71.2\% while matching or exceeding uncompressed text-only inputs, and consistently outperforms text-based and visual compression baselines across all three tasks. These results show that combining layout compaction, adaptive configuration, and instruction-aware pruning can make multimodal code understanding more efficient. Our code is available at https://github.com/vinsontang1/CodeShrink.

</details>

---

### [[20_Research/Papers/机器人/RayViT_Ray-Conditioned_Visual_Representations_for_Viewpoint-Robust_Imitation_Learning|RayViT: Ray-Conditioned Visual Representations for Viewpoint-Robust Imitation Learning]]

![[assets/2607.29622_figure.png|800]]

- **arXiv**: [2607.29622](https://arxiv.org/abs/2607.29622)
- **PDF**: https://arxiv.org/pdf/2607.29622
- **详细分析**: [[20_Research/Papers/机器人/RayViT_Ray-Conditioned_Visual_Representations_for_Viewpoint-Robust_Imitation_Learning|RayViT: Ray-Conditioned Visual Representations for Viewpoint-Robust Imitation Learning]]
- **作者**: Qian Wang, Longrui Chen, Peiran Sun, Aleksandar Taranovic, Niklas Freymuth, Ge Li, Weiran Liao, C. F. Maximilian Nagy, Yucheng Tan, Tao Chen, Gerhard Neumann
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《RayViT: Ray-Conditioned Visual Representations for Viewpoint-Robust Imitation Learning》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual imitation learning enables robots to acquire visuomotor skills directly from images, yet RGB observations lack explicit geometric cues, making learned policies brittle to camera perturbations. To address this, we propose \textbf{Ray-conditioned Vision Transformer Encoder (RayViT)}, a lightweight architecture that injects camera geometry into pretrained ViT backbones. RayViT represents camera geometry as a Plücker ray map, patchifies it into ray features, and uses gated cross-attention to produce a ray-conditioned class token. These ray features are added as dense positional embeddings, while the ray class token replaces the original ViT class token to provide a geometry-aware summary representation. We combine this approach with an auxiliary cosine similarity loss to consistently improve the performance and robustness for geometry-aware tokens. Experiments on sim- and real-robot tasks demonstrate that RayViT improves robustness by approximately 13 percentage points under camera perturbations in multi-task RoboCasa benchmark and by 1.78 average completed stages in real-world multi-task success rate compared to baselines.

</details>

---

### [[20_Research/Papers/具身智能/FibVLA_An_Efficient_Temporal_Vision-Language-Action_Model_with_Fibonacci_Sampling|FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling]]

![[assets/2607.29596_figure.png|800]]

- **arXiv**: [2607.29596](https://arxiv.org/abs/2607.29596)
- **PDF**: https://arxiv.org/pdf/2607.29596
- **详细分析**: [[20_Research/Papers/具身智能/FibVLA_An_Efficient_Temporal_Vision-Language-Action_Model_with_Fibonacci_Sampling|FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling]]
- **作者**: Li Lin, Wujun Xu, Weiwei Meng, Kaiwen Xia, Kang Hao Cheong, Shuai Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 2.1，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《FibVLA: An Efficient Temporal Vision-Language-Action Model with Fibonacci Sampling》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FibVLA, HybridVLA, OpenVLA, TraceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action models (VLAs), which leverage the cognition of multimodal information to infer physical-world actions, provide a generalized solution for embodied AI applications. Conventional VLAs usually concentrate on current digital cognition. While some efforts are made to enhance VLAs' reasoning capabilities by capturing temporal information, encoding the long-context history causes an efficiency-decreasing issue. To reconcile the conflict between capturing temporal information and maintaining inference efficiency in VLAs, this paper introduces FibVLA, an efficient framework featuring temporal perception of long-context history. Specifically, we leverage logarithmic hindsight sampling to both proprioceptive states and visual frames to capture long-term temporal dependencies with minimal redundancy. For the action expert, we introduce the flow matching to produce action distributions, and the Fibonacci recurrent inference strategy to generate long-range planning steps based on real-time closed-loop feedback. Experiments demonstrate that FibVLA significantly improves action smoothness and success rates without retraining large-scale visual encoders. Efficiency analysis demonstrates superior real-time responsiveness compared to video-based baselines in real-world evaluations.

</details>

---

### [[20_Research/Papers/大模型/MoRoute_Dynamic_Routing_for_In-Context_Multimodal_Video_Generation|MoRoute: Dynamic Routing for In-Context Multimodal Video Generation]]

![[assets/2607.29545_figure.png|800]]

- **arXiv**: [2607.29545](https://arxiv.org/abs/2607.29545)
- **PDF**: https://arxiv.org/pdf/2607.29545
- **详细分析**: [[20_Research/Papers/大模型/MoRoute_Dynamic_Routing_for_In-Context_Multimodal_Video_Generation|MoRoute: Dynamic Routing for In-Context Multimodal Video Generation]]
- **作者**: Chong Gao, Jie Ma, Zhan Peng, Chongxiao Wang, Haoxue Wu, Jun Liang, Guanbin Li, Jing Li
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《MoRoute: Dynamic Routing for In-Context Multimodal Video Generation》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IntelligentVBench, OpenVE-Bench, RefVIE-Bench, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal video generation aims to generate and edit videos conditioned on arbitrary combinations of text, images, and videos within a single model, allowing diverse tasks to share complementary data and generative priors. Unifying these tasks requires multimodal understanding of diverse conditions, which is typically provided by a pretrained vision-language model (VLM). A key challenge is how to connect the VLM's hierarchical multimodal representations with a pretrained video diffusion transformer (DiT). Existing methods either inject features from only the final or a few manually selected VLM layers, or jointly train architecture-matched understanding and generation streams, making it difficult to reuse heterogeneous pretrained backbones. We introduce MoRoute, a unified multimodal video generation framework that formulates a frozen VLM and a pretrained video DiT with different architectures as heterogeneous experts connected through dynamic layer routing. For each input, a lightweight block-wise router enables every DiT block to select the VLM layer most relevant to its generation stage, thereby learning an adaptive correspondence between multimodal understanding and video synthesis. MoRoute further incorporates reference images and source videos directly into the DiT token sequence through unified in-context conditioning, preserving fine-grained visual details across diverse generation and editing tasks. Experiments on IntelligentVBench, OpenVE-Bench, and RefVIE-Bench show that MoRoute consistently surpasses the best competing method on each benchmark, improving the average score by 0.15, 0.18, and 0.34 on a 1-5 scale, respectively.

</details>

---

### [[20_Research/Papers/大模型/SatEdit_Mask-Conditioned_Image_Editing_via_VLM-Guided_Segment_Annotation|SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation]]

![[assets/2607.29367_figure.png|800]]

- **arXiv**: [2607.29367](https://arxiv.org/abs/2607.29367)
- **PDF**: https://arxiv.org/pdf/2607.29367
- **详细分析**: [[20_Research/Papers/大模型/SatEdit_Mask-Conditioned_Image_Editing_via_VLM-Guided_Segment_Annotation|SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation]]
- **作者**: Muhammad Talha, Muhammad Ahmed Amer
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.7（加权：大模型 0.7）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《SatEdit: Mask-Conditioned Image Editing via VLM-Guided Segment Annotation》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Satellite image editing requires spatially precise object-level control, but supervised editing datasets for overhead imagery are costly to build because object masks, semantic labels, and paired edits are rarely available at scale. We introduce SatEdit, a mask-conditioned satellite image editing framework that constructs training supervision from unlabeled imagery. SatEdit proposes object masks with a seg- mentation foundation model, assigns semantic la- bels to sampled segments with a Vision-Language Model, and applies lightweight human verification before generating paired addition and removal exam- ples through mask-guided inpainting. We fine-tune a high-resolution image editing backbone with LoRA on a SODA-A-derived dataset containing 1,014 im- ages and 852 verified object annotations across 91 classes. In controlled comparisons with open- source and proprietary image editing models, SatE- dit achieves the highest aggregate masked-region se- mantic alignment, with a CLIP score of 0.6322 and CLIP delta of 0.0726, while preserving the surround- ing scene qualitatively. These results suggest that VLM-assisted segment annotation is a practical route to data-efficient, spatially controllable satellite image editing.

</details>

---

### [[20_Research/Papers/具身智能/BWM_A_Low-Cost_High-Fidelity_World_Simulator_for_Robot_Learning|BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning]]

![[assets/2607.29302_first_page.png|800]]

- **arXiv**: [2607.29302](https://arxiv.org/abs/2607.29302)
- **PDF**: https://arxiv.org/pdf/2607.29302
- **详细分析**: [[20_Research/Papers/具身智能/BWM_A_Low-Cost_High-Fidelity_World_Simulator_for_Robot_Learning|BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning]]
- **作者**: BWM Team
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 2.2（加权：具身智能 0.9，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《BWM: A Low-Cost High-Fidelity World Simulator for Robot Learning》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robot learning requires a world simulator that can predict action consequences before execution on physical hardware, including risky and failure-prone outcomes. Existing physics simulators require substantial asset construction and calibration and still face a sim-to-real gap, while video generators often lack precise control over their responses to fine-grained robot actions. In this paper, we present the Boundless World Model (BWM), an open-source, low-cost, high-fidelity world simulator for robot manipulation. BWM is an action-conditioned world model that combines initial-environment guidance, dynamic visual history, and temporally aligned robot-action conditioning for stateful autoregressive prediction of future observations. We construct action-aligned training clips through trajectory replay, overlapping clip sampling, and initial-observation enhancement. BWM serves as a data engine that augments imitation-learning data with action-aligned rollouts, and as a policy evaluator for closed-loop assessment, risk anticipation, and policy ranking. Experiments on the WorldArena benchmark and physical robots demonstrate improved simulator fidelity and functional utility across the data-engine and policy-evaluator settings. BWM ranks first overall in the WorldArena Challenge across Track 1 and its two Track 2 applications. We release the BWM open-source ecosystem, including model checkpoints, training and inference code, and interfaces for data generation and policy evaluation.

</details>

---

### [[20_Research/Papers/大模型/UltraSAM3_A_Concept-Driven_Foundation_Model_for_Universal_Ultrasound_Image_Segmentation|UltraSAM3: A Concept-Driven Foundation Model for Universal Ultrasound Image Segmentation]]

![[assets/2607.29200_figure.png|800]]

- **arXiv**: [2607.29200](https://arxiv.org/abs/2607.29200)
- **PDF**: https://arxiv.org/pdf/2607.29200
- **详细分析**: [[20_Research/Papers/大模型/UltraSAM3_A_Concept-Driven_Foundation_Model_for_Universal_Ultrasound_Image_Segmentation|UltraSAM3: A Concept-Driven Foundation Model for Universal Ultrasound Image Segmentation]]
- **作者**: Bo Xu, Quanhao Zhu, Rui Lin, Boling Zhu, Chenyuan Wang, Hongfei Lin, Feng Xia, Chenhua Ji
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Agent, ComputerVision

#### 研究背景与动机

《UltraSAM3: A Concept-Driven Foundation Model for Universal Ultrasound Image Segmentation》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：TransUNet, U-Net, VM-UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ultrasound imaging has become increasingly widespread in clinical practice due to its portability, low cost and real-time capability, making ultrasound image segmentation important. However, ultrasound images differ substantially from CT, MRI, and other medical imaging modalities, as they are often affected by speckle noise, low contrast, acoustic shadows and ambiguous boundaries. Existing ultrasound segmentation methods are still mainly limited to task-specific models or visual-prompt-based foundation models, which are either tailored to particular tasks or require expert-provided visual prompts, making them inconvenient for flexible clinical use. To address these challenges, we propose UltraSAM3, a concept-driven foundation model for universal ultrasound image segmentation. Unlike conventional models, UltraSAM3 enables text-based target specification by adapting SAM3 to ultrasound-specific image--mask--concept triplets. The model is trained on a large-scale ultrasound segmentation corpus covering 37 public datasets and 13 anatomical categories, allowing it to align ultrasound visual patterns with clinically meaningful concepts across diverse organs and lesions. To further improve usability under realistic clinical interaction, we propose an instruction-guided agent that parses complex natural language queries into concise ultrasound concept prompts for UltraSAM3. Extensive experiments demonstrate that UltraSAM3 consistently outperforms representative concept- and text-driven biomedical segmentation models on multi-organ ultrasound benchmarks, external datasets, and visual-prompt-enhanced settings. Moreover, the agent improves segmentation robustness for complex user instructions. These results indicate that ultrasound-specific concept adaptation is effective for building generalizable and interactive ultrasound segmentation foundation models.

</details>

---

### [[20_Research/Papers/机器人/SULAND_v2_A_Refined_RGB_Dataset_and_Deep_Learning_Object_Detection_Benchmark_for_UAV_UGV-Based_SUrface_LANDmine_Detection_Under_Domain_Shift|SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift]]

![[assets/2607.28996_figure.png|800]]

- **arXiv**: [2607.28996](https://arxiv.org/abs/2607.28996)
- **PDF**: https://arxiv.org/pdf/2607.28996
- **详细分析**: [[20_Research/Papers/机器人/SULAND_v2_A_Refined_RGB_Dataset_and_Deep_Learning_Object_Detection_Benchmark_for_UAV_UGV-Based_SUrface_LANDmine_Detection_Under_Domain_Shift|SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift]]
- **作者**: Sagar Lekhak, Prasanna Reddy Pulakurthi, Lalit Joshi, Ramesh Bhatta, Emmett J. Ientilucci
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《SULAND v2: A Refined RGB Dataset and Deep Learning Object Detection Benchmark for UAV/UGV-Based SUrface LANDmine Detection Under Domain Shift》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

RGB imagery offers a practical, low-cost option for Unmanned Aerial/Ground Vehicle (UAV/UGV) survey support in surface-landmine detection, but object detectors remain underexplored in this safety-critical domain. Limited cross-architecture benchmarking and insufficient out-of-distribution (OOD) analysis obscure whether detectors generalize across deployment conditions. This challenge is amplified by the scarcity of public RGB landmine datasets, making SULAND a key benchmark for PFM-1 and PMA-2 detection. However, inspection reveals missing/false annotations, localization errors, inconsistent visibility criteria, visual artifacts, temporal labeling inconsistencies, and an inverted OOD class-ID convention in SULAND. We present SULAND_v2, a refined RGB surface-landmine dataset and benchmark. Preserving original images and splits, we manually revise annotations to ensure completeness, precise localization, label validity, and class consistency. SULAND_v2 contains 33,771 images and 12,433 bounding boxes. We benchmark 35 detector configurations across nine families. Annotation refinement improves YOLOv8 in-distribution (IID) test mAP@50 by 14.6-19.6 percentage points, while fixing the OOD class-ID convention increases mean YOLOv8 OOD mAP@50 by ~25 percentage points. On SULAND_v2, YOLOv12-Small achieves the highest IID mAP@50 (0.908), while RF-DETR-Large yields the strongest OOD performance (0.799 mAP@50, 0.675 recall). Our results demonstrate that high IID accuracy does not guarantee operational readiness. SULAND_v2 provides a reliable benchmark for evaluating domain-shift robustness in RGB-based mine-action survey support.

</details>

---

### [[20_Research/Papers/具身智能/ST-WAM_Semantic-Temporal_World_Action_Model_for_Robust_Manipulation_under_Visual_Distribution_Shifts|ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts]]

![[assets/2607.28993_figure.png|800]]

- **arXiv**: [2607.28993](https://arxiv.org/abs/2607.28993)
- **PDF**: https://arxiv.org/pdf/2607.28993
- **详细分析**: [[20_Research/Papers/具身智能/ST-WAM_Semantic-Temporal_World_Action_Model_for_Robust_Manipulation_under_Visual_Distribution_Shifts|ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts]]
- **作者**: Mingxin Wang, Bin Hu, Bin Qian, Kaitao Jiang, Haoning Wu, Feng Yan, Bowen Jing, Ruiyang Hao, Enyi Wang, Kangning Niu, Yandan Yang, Mu Xu...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《ST-WAM: Semantic-Temporal World Action Model for Robust Manipulation under Visual Distribution Shifts》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DreamVLA, GigaWorld, IntentVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) have emerged as a promising paradigm by jointly modeling robot actions and future visual dynamics. However, their reliance on pixel-generative future supervision can entangle action-relevant state transitions with task-irrelevant visual content, limiting robustness under visual distribution shifts. We identify Training-Distribution Hallucination, a recurring phenomenon in which futures conditioned on visually shifted observations hallucinate training-domain content rather than remain faithful to the current scene. A controlled frame-triplet diagnosis further shows that DINOv3 features remain more stable across visual shifts while better preserving task-state distinctions than Wan-VAE latents. Rather than correcting the predicted futures, we propose Semantic-Temporal WAM (ST-WAM) to improve action robustness by using DINOv3 as a shared semantic representation for future prediction and history retrieval while retaining fine-grained VAE dynamics. Its Dual-Space Future Experts (DSFE) jointly predict future VAE latents and DINO features, while Current-Anchored Intent Retrieval (CAIR) retrieves task-relevant evidence from recent DINO history under the current visual-language context. ST-WAM is trained end-to-end without additional embodied pretraining or task-specific annotations, and requires no explicit future generation at inference. It achieves 98.7% on LIBERO and 92.8% on RoboTwin 2.0; more importantly, compared with Fast-WAM, it improves zero-shot LIBERO-Plus performance by 21.3 percentage points and more than doubles real-world success under visual shifts from 25.8% to 61.5%. These results demonstrate that semantic-temporal modeling effectively complements pixel-generative dynamics for robust manipulation.

</details>

---

### [[20_Research/Papers/强化学习/Mirror_Learning|Mirror Learning]]

![[assets/2607.28737_figure.png|800]]

- **arXiv**: [2607.28737](https://arxiv.org/abs/2607.28737)
- **PDF**: https://arxiv.org/pdf/2607.28737
- **详细分析**: [[20_Research/Papers/强化学习/Mirror_Learning|Mirror Learning]]
- **作者**: Yunpeng Liu, Matthew Niedoba, Oluwanifemi A. Adekanye, Jason Yoo, Yingchen He, Berend Zwartsenberg, Frank Wood
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.72（加权：强化学习 0.16，世界模型 0.56）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《Mirror Learning》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Training-Set, Validation-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We investigate imitation learning through the lens of third-person observation and propose a framework for mirror learning: acquiring actionable policies from passive observation. While behavior cloning (BC) excels under dense, well-aligned first-person data, it fundamentally fails to leverage the rich observational signals arising from third-person demonstrations that humans and animals routinely exploit. We introduce a method that composes (i) a learned perspective transformation that places learners in demonstrators' shoes using a fine-tuned video diffusion model and (ii) an inverse dynamics model that infers action trajectories in the learners' control space. This enables the synthesis of mirror data, pseudo first-person expert data generated from third-person observations of demonstrator behavior. Empirically, we show that mirror data alone can train effective policies, and that augmenting first-person BC training with mirror data further improves downstream policy performance. Our results suggest that modern generative world models implicitly encode sufficient structure to enable a scalable and safe alternative to teleoperation-heavy data collection.

</details>

---
