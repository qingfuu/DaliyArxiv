# cs.CV | Computer Vision and Pattern Recognition | 2026-05-26

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/机器人/MIND_Multi-Scale_Intent_Diffusion_for_Text-Driven_Physics-Based_Humanoid_Control|MIND: Multi-Scale Intent Diffusion for Text-Driven Physics-Based Humanoid Control]]

![[assets/2605.26006_figure.png|800]]

- **arXiv**: [2605.26006](https://arxiv.org/abs/2605.26006)
- **PDF**: https://arxiv.org/pdf/2605.26006
- **详细分析**: [[20_Research/Papers/机器人/MIND_Multi-Scale_Intent_Diffusion_for_Text-Driven_Physics-Based_Humanoid_Control|MIND: Multi-Scale Intent Diffusion for Text-Driven Physics-Based Humanoid Control]]
- **作者**: Bin Li, Ruichi Zhang, Han Liang, Jingyan Zhang, Juze Zhang, Xin Chen, Jingya Wang
- **cs 子类**: cs.CV, cs.GR, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: cs.CV

#### 研究背景与动机

《MIND: Multi-Scale Intent Diffusion for Text-Driven Physics-Based Humanoid Control》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Enabling physics-based humanoids to execute diverse behaviors from high-level textual commands remains a significant challenge. Existing methods typically follow either a two-stage paradigm that combines kinematic motion generation with physics-based tracking, or an end-to-end imitation-learning paradigm that directly generates actions from text. However, the former suffers from the inherent domain shift between kinematic generation and physics-based tracking, while the latter struggles with the substantial modality gap between textual commands and low-level actions, limiting effective semantic alignment. Notably, humanoid states encode rich motion dynamics that are more semantically aligned with textual descriptions than low-level actions, making them a natural basis for deriving behavioral intent. Building upon this insight, we propose MIND, a novel end-to-end diffusion framework for text-driven physics-based humanoid control that leverages behavioral intent as a semantic bridge between textual commands and low-level actions. At its core, MIND introduces a multi-scale intent diffusion mechanism, where a holistic intent predictor captures global behavioral dynamics to guide overall behavior synthesis, while an immediate intent predictor provides step-wise, fine-grained signals for local behavior refinement at each diffusion step. This hierarchical intent formulation imposes a structured inductive bias for humanoid control, improving semantic alignment and behavioral naturalness. Furthermore, MIND encodes humanoid states into a latent space to enable more effective semantic intent modeling. Extensive experiments demonstrate that MIND outperforms existing methods and synthesizes coherent, physically plausible, and semantically aligned humanoid behaviors from text commands. Our code will be released to facilitate future research.

</details>

---

### [[20_Research/Papers/机器人/LRDDv3_High-Resolution_Long-Range_Drone_Detection_Dataset_with_Range_Information_and_Thermal_Data|LRDDv3: High-Resolution Long-Range Drone Detection Dataset with Range Information and Thermal Data]]

![[assets/2605.25942_figure.png|800]]

- **arXiv**: [2605.25942](https://arxiv.org/abs/2605.25942)
- **PDF**: https://arxiv.org/pdf/2605.25942
- **详细分析**: [[20_Research/Papers/机器人/LRDDv3_High-Resolution_Long-Range_Drone_Detection_Dataset_with_Range_Information_and_Thermal_Data|LRDDv3: High-Resolution Long-Range Drone Detection Dataset with Range Information and Thermal Data]]
- **作者**: Knut Peterson, Zaid Mayers, Azmain Yousuf, Priontu Chowdhury, Asher Zaczepinski, Solmaz Arezoomandan, Reihaneh Maarefdoust, David Han
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《LRDDv3: High-Resolution Long-Range Drone Detection Dataset with Range Information and Thermal Data》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned Aerial Vehicles (UAVs) have quickly become common in various airspaces, representing a wide range of applications from recreation flying to commercial photography and package delivery. With the increasing prevalence of UAVs, it becomes critical that both manned and unmanned aircraft can detect UAVs and other flying objects from long range to effectively track movement and ensure safe operation in shared spaces. While several datasets have been introduced for drone detection, the need for expanded high-quality data persists, especially in the area of high-resolution long-range drone data. To address this, we introduce a high-resolution dataset of 102,532 long-range RGB images of drones, sampled at 5 FPS from 128 distinct video clips taken mid flight during 17 different data collection days spread over 8 months to ensure a wide variety of lighting scenarios, flight locations, and background elements. The dataset boasts comprehensive drone range information across the dataset, as well as 29,630 IR images, all paired with RGB counterparts from the base dataset. As one of the first drone detection datasets to leverage 4K image resolution and paired 640x512 IR images, our work represents a significant advancement to enable the detection of drones at long range. For access to the complete dataset, please visit this https URL

</details>

---

### [[20_Research/Papers/具身智能/AgentGrounder_Zero-Shot_3D_Visual_Pointcloud_Grounding_using_Multimodal_Language_Models|AgentGrounder: Zero-Shot 3D Visual Pointcloud Grounding using Multimodal Language Models]]

![[assets/2605.25901_figure.png|800]]

- **arXiv**: [2605.25901](https://arxiv.org/abs/2605.25901)
- **PDF**: https://arxiv.org/pdf/2605.25901
- **详细分析**: [[20_Research/Papers/具身智能/AgentGrounder_Zero-Shot_3D_Visual_Pointcloud_Grounding_using_Multimodal_Language_Models|AgentGrounder: Zero-Shot 3D Visual Pointcloud Grounding using Multimodal Language Models]]
- **作者**: Cuong Huynh, Maxim Popov, Denis Gridusov, Sergey Kolyubin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.9，大模型 0.5，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《AgentGrounder: Zero-Shot 3D Visual Pointcloud Grounding using Multimodal Language Models》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ScanNet, URL, VLTNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3D Visual Grounding (3DVG) is an essential capability for embodied AI, requiring agents to localize objects in 3D scenes based on natural language descriptions. Recent zero-shot methods leverage 2D vision-language models (LVLMs). However, they often rely on existing sets of multi-view images and struggle with the limited semantic and spatial details provided by standard 3D segmentation tools. We present $\textbf{AgentGrounder}$, a zero-shot 3D visual grounding framework that operates directly on colored point clouds without task-specific 3D training. Our approach follows a two-stage design: (1) an offline stage that applies 3D model to build an Object Lookup Table (OLT) with instance IDs, semantic labels, 3D bounding boxes; and (2) an online tool-driven agent that decomposes each query, retrieves only relevant candidates from the OLT, performs geometric scoring, and triggers image rendering on demand when additional visual evidence (e.g., color, material, or viewpoint-sensitive cues) is required. Compared with fixed anchor-target matching pipelines, this design reduces cascading matching errors and improves context-window efficiency by avoiding prompts overloaded with irrelevant objects. We evaluate on ScanRefer and Nr3D under a zero-shot setting and observe consistent improvements over SeeGround in our setup, including +2.5% Acc@0.5 on ScanRefer and +6.3% on Nr3D, with a notable +6.3% gain on Nr3D view-independent queries. These results show that combining selective retrieval, geometric reasoning, and adaptive visual inspection yields a practical and robust foundation for open-vocabulary 3D grounding. Our code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Rethinking_VLM_Representation_for_VLA_Initialization|Rethinking VLM Representation for VLA Initialization]]

![[assets/2605.25802_figure.png|800]]

- **arXiv**: [2605.25802](https://arxiv.org/abs/2605.25802)
- **PDF**: https://arxiv.org/pdf/2605.25802
- **详细分析**: [[20_Research/Papers/具身智能/Rethinking_VLM_Representation_for_VLA_Initialization|Rethinking VLM Representation for VLA Initialization]]
- **作者**: Weifeng Lin, Siyuan Huang, Hao Li, Tingwei Chen, Ruichuan An, Xinyu Wei, Jianbo Liu, Hongsheng Li
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.4，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Rethinking VLM Representation for VLA Initialization》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgiBot-World, OpenVLA, VLM-to-VLA, VLM4VLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models widely adopt pretrained Vision-Language Models (VLMs) as policy backbones, yet it remains unclear what kind of pretrained VLM representation is useful as a VLA initialization. In this paper, we study VLA initialization as a controlled representation-design problem along three axes: capability-level embodied VQA supervision, parameter-update strategy, and robot-data pretraining. Our experiments show that the original pretrained VLM representation is a key source of action performance. However, embodied VQA adaptation does not yield uniform gains: its benefit depends on downstream bottlenecks, and gains from different capability domains are not simply additive. For update strategy, LoRA provides a more reliable initialization than Full Finetune, indicating that overly reshaping the pretrained representation can weaken VLA initialization. Robot-data pretraining further improves VLA initialization, with the strongest variant obtained by staged LoRA-based training. Together, these findings suggest that effective VLM-to-VLA adaptation should inject action-relevant embodied and robot-trajectory signals while preserving the pretrained VLM representation that remains useful for action learning.

</details>

---

### [[20_Research/Papers/具身智能/TapSampling_Inference-Time_Sampling_with_a_Task-Progress-Understanding_Verifier_for_Robotic_Manipulation|TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation]]

![[assets/2605.25547_figure.png|800]]

- **arXiv**: [2605.25547](https://arxiv.org/abs/2605.25547)
- **PDF**: https://arxiv.org/pdf/2605.25547
- **详细分析**: [[20_Research/Papers/具身智能/TapSampling_Inference-Time_Sampling_with_a_Task-Progress-Understanding_Verifier_for_Robotic_Manipulation|TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation]]
- **作者**: Sizhe Zhao, Shengping Zhang, Shuo Yang, Weiyu Zhao, Shuigen Wang, Xiangyang Ji
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《TapSampling: Inference-Time Sampling with a Task-Progress-Understanding Verifier for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing embodied control research demonstrates remarkable performance improvements by scaling training data and model size. We instead explore inference-time strategy as an alternative axis. Non-deterministic generative models, such as diffusion and autoregressive models, have been widely adopted in the field of embodied control. However, the single-shot inference paradigm limits their performance. In this paper, we propose \textbf{TapSampling}, a plug-and-play framework for inference-time sampling. First, we introduce an Action-VAE that represents actions in a low-dimensional latent space by mapping policy-generated initial actions into a compressed posterior distribution, from which any number of latent samples can be drawn and decoded into candidate actions that approximate the true action distribution. Second, we formulate action verification as task-progress outcome prediction, using the intrinsic sequential structure of robotic datasets to train a semantically grounded verifier for interpretable action selection. Furthermore, TapSampling is a policy-agnostic framework. Extensive experiments in both simulated and real-world environments demonstrate that our method substantially improves multiple generalist policies without further policy finetuning. Code and models are available at the project page.

</details>

---

### [[20_Research/Papers/具身智能/RepSAM_Bridging_Foundation_Models_to_Robotic_Vision_via_Representation-Guided_Adaptation|RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation]]

![[assets/2605.25495_figure.png|800]]

- **arXiv**: [2605.25495](https://arxiv.org/abs/2605.25495)
- **PDF**: https://arxiv.org/pdf/2605.25495
- **详细分析**: [[20_Research/Papers/具身智能/RepSAM_Bridging_Foundation_Models_to_Robotic_Vision_via_Representation-Guided_Adaptation|RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation]]
- **作者**: Wenhui Chu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《RepSAM: Bridging Foundation Models to Robotic Vision via Representation-Guided Adaptation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GraspNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic perception in unstructured environments remains challenging despite the zero-shot capabilities of foundation models such as SAM. This work attributes performance degradation to non-uniform representation shifts across transformer layers: shallow layers exhibit substantial domain gaps (CKA &lt; 0.5), whereas deep layers transfer effectively (CKA &gt; 0.7). Based on this observation, we propose RepSAM, a representation-guided parameter-efficient fine-tuning (PEFT) framework for adapting foundation models to robotic vision. RepSAM employs a theoretically grounded CKA-guided rank allocation strategy combined with a multi-modal fusion module for robust handling of challenging robotic scenarios, including transparent objects and cluttered scenes. Experimental evaluation across six benchmarks and robotic manipulation tasks demonstrates that RepSAM achieves 97.9% of full fine-tuning performance (89.0% vs. 90.9% mIoU) while reducing trainable parameters by 158x (from 632M to 4.0M). RepSAM outperforms DoRA by 7.9% mIoU with just 4 hours of training on a single A100 GPU (a 96x reduction from full fine-tuning, which takes 384 GPU-hours). These improvements are statistically significant (p &lt; 0.01) and translate to a 12.0% absolute improvement in robotic manipulation success rates over the LoRA (RGB) baseline.

</details>

---

### [[20_Research/Papers/具身智能/VEOcc_Voxel-Centric_Online_Semantic_Occupancy_Prediction_For_Embodied_Scene_Understanding|VEOcc: Voxel-Centric Online Semantic Occupancy Prediction For Embodied Scene Understanding]]

![[assets/2605.25059_figure.png|800]]

- **arXiv**: [2605.25059](https://arxiv.org/abs/2605.25059)
- **PDF**: https://arxiv.org/pdf/2605.25059
- **详细分析**: [[20_Research/Papers/具身智能/VEOcc_Voxel-Centric_Online_Semantic_Occupancy_Prediction_For_Embodied_Scene_Understanding|VEOcc: Voxel-Centric Online Semantic Occupancy Prediction For Embodied Scene Understanding]]
- **作者**: Ruoyu Wang, Yong Liu, Sheng Tao, Yuhang Lin, Yukai Ma
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《VEOcc: Voxel-Centric Online Semantic Occupancy Prediction For Embodied Scene Understanding》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EfficientNet, EmbodiedOcc-ScanNet, Occ-ScanNet, ResNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Crucial for autonomous exploration, online 3D occupancy prediction and mapping incrementally constructs dense spatial representations on the fly. However, recent Gaussian-centric methods struggle with structural boundary fidelity and rely heavily on predefined scene-size priors, fundamentally limiting their operational efficiency. In this work, we present VEOcc, a voxel-centric framework formulated as a recursive perception-and-assimilation paradigm. By eliminating the need for initial scale estimation, VEOcc enables highly streamlined, open-ended map expansion. Furthermore, to robustly aggregate noisy temporal observations within the discrete voxel space, we propose a Spatio-Temporal-Aware Online Update Strategy. It integrates Cross-Temporal Logit Aggregation (TLA) for temporal consistency, Reliability-Aware Confidence Modulation (RCM) for spatial uncertainty calibration, and Confidence-Driven Incremental State Update (CSU) for robust global state assimilation. % Extensive experiments on Occ-ScanNet and EmbodiedOcc-ScanNet demonstrate that VEOcc establishes new state-of-the-art performance in both local and embodied settings, providing an accurate and efficient solution for real-world exploration. Extensive experiments on Occ-ScanNet and EmbodiedOcc-ScanNet demonstrate that VEOcc establishes new state-of-the-art performance in both local and embodied settings. Notably, zero-shot evaluations on self-collected video sequences further confirm its robust out-of-distribution generalization capability in completely unseen real-world environments. Ultimately, our framework provides an accurate and highly efficient solution for autonomous exploration. Code and supplementary visualizations are available on our project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/QuoVLA_Quotient_Space_for_Vision-Language-Action_Models|QuoVLA: Quotient Space for Vision-Language-Action Models]]

![[assets/2605.24890_first_page.png|800]]

- **arXiv**: [2605.24890](https://arxiv.org/abs/2605.24890)
- **PDF**: https://arxiv.org/pdf/2605.24890
- **详细分析**: [[20_Research/Papers/具身智能/QuoVLA_Quotient_Space_for_Vision-Language-Action_Models|QuoVLA: Quotient Space for Vision-Language-Action Models]]
- **作者**: Xuan Wang, Yinan Wu, Haoran Duan, Jungong Han
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.5，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《QuoVLA: Quotient Space for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, QuoVLA, TinyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models commonly adapt pretrained Vision-Language Models (VLMs) to robot control by mapping visual observations and language instructions to continuous actions. Existing approaches typically take an action-insufficiency view, assuming that pretrained VLM latents either lack directly usable action information or should be shielded from action-learning signals. Against this view, our \textit{Quotient Theory for VLA} shows that pretrained VLM latents are not action-insufficient but action-sufficient: they already contain the information needed for control, yet remain overcomplete by distinguishing prompt-level variations that induce the same optimal action behavior. To operationalize this theory, we propose QuoVLA, a quotient-space framework for VLA that compresses pretrained VLM latents into action-sufficient representations. Specifically, QuoVLA instantiates this principle with a quantization module and a dual-branch design with relative temporal-complexity regularization, preserving action-relevant information while removing prompt-level redundancy. Extensive experiments across multiple benchmarks demonstrate that QuoVLA achieves strong performance, with particularly notable improvements in generalization under visual, linguistic, and environmental distribution shifts. Our code will be made publicly available.

</details>

---

### [[20_Research/Papers/具身智能/Understanding_the_Impact_of_Geometric_Foundation_Models_on_Vision-Language-Action_Models|Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models]]

![[assets/2605.24642_figure.png|800]]

- **arXiv**: [2605.24642](https://arxiv.org/abs/2605.24642)
- **PDF**: https://arxiv.org/pdf/2605.24642
- **详细分析**: [[20_Research/Papers/具身智能/Understanding_the_Impact_of_Geometric_Foundation_Models_on_Vision-Language-Action_Models|Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models]]
- **作者**: Yurou Yang, Muyuan Lin, Roberto Martin-Martin, Martin Labrie, Shreekant Gayaka, Cheng-Hao Kuo, Luca Carlone
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Understanding the Impact of Geometric Foundation Models on Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Abouzeid25arxiv-GeoAwareVLA, Li25arxiv-pointVLA, Lin25arxiv-Evo0VLA, PointVLA, Qu25arxiv-spatialVLA, Zhen24arxiv-3DVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent work explores new opportunities at the intersection of vision-language-action models (VLAs) and geometric foundation models (GFMs) for 3D reconstruction, such as VGGT. While the resulting geometric VLAs often show improved performance, it remains unclear (i) if modern VLAs already have sufficient geometric understanding to start with, (ii) what is the best architecture to inject geometric understanding into a VLA, and (iii) what is the effect of other design choices that affect geometric VLAs. In this paper we provide a rigorous experimental analysis to shed light on these questions, for a specific choice of VLA (GR00T-N1.5) and GFM (VGGT). Our first contribution is to formalize prior work's intuition that current VLAs lack geometric understanding, by providing a rigorous analysis based on linear probing. The analysis quantifies, for the first time, the "geometric gap" between VLAs and GFMs. Our second contribution is to identify and compare different strategies to bridge GFMs with VLAs. We implement three different architectures, which differ in the way they inject geometry in the VLA, while keeping low-level implementation details as similar as possible, to ensure a fair comparison. Finally, we analyze the impact of non-architectural choices (e.g., training data, number of cameras, reconstruction quality) on the performance of the geometric VLAs.

</details>

---

### [[20_Research/Papers/具身智能/DexSIM_Real-time_Dexterous_Simulation_with_Unified_Causal_Video_Diffusion|DexSIM: Real-time Dexterous Simulation with Unified Causal Video Diffusion]]

![[assets/2605.24630_figure.png|800]]

- **arXiv**: [2605.24630](https://arxiv.org/abs/2605.24630)
- **PDF**: https://arxiv.org/pdf/2605.24630
- **详细分析**: [[20_Research/Papers/具身智能/DexSIM_Real-time_Dexterous_Simulation_with_Unified_Causal_Video_Diffusion|DexSIM: Real-time Dexterous Simulation with Unified Causal Video Diffusion]]
- **作者**: Adam Lee
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《DexSIM: Real-time Dexterous Simulation with Unified Causal Video Diffusion》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：HunyuanWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent progress of video diffusion models have enabled extensive simulation of the physical world. While simulation with hand object interaction has been less explored. We propose DexSIM, a dexterous simulation framework for simulating dexterous manipulation in real-time. While previous works utilizing video diffusion and 3D reconstruction focus on navigation, dexterous manipulation has been limited while it has extensive applications for creating interactive experiences with the simulated world and for generating synthetic data for robotics. Existing methods lack real-time interactivity and long-term spatial consistency and memory. We propose a 2-stage training framework for DexSIM. First we train a bi-directional video diffusion model by jointly embedding the hand action trajectory and video in a unified feature space. We utilize gaussian heatmap hand encoding for more accurate hand representation. Then we conduct a roll-out based autoregressive training with updated spatial cache as attention sink for spatial memory, which improves long-term consistency and 3D aware dexterous manipulation simulation. DexSIM outperforms the baseline on pixel and semantic similarity, motion fidelity, and hand projection accuracy. It also allows new applications such as hand motion transfer and runs at 15.24 FPS real-time interactivity.

</details>

---

### [[20_Research/Papers/世界模型/SparseWorld_Enhancing_End-to-End_Autonomous_Driving_via_World_Models_with_Sparse_Scene_Representation|SparseWorld: Enhancing End-to-End Autonomous Driving via World Models with Sparse Scene Representation]]

![[assets/2605.24354_figure.png|800]]

- **arXiv**: [2605.24354](https://arxiv.org/abs/2605.24354)
- **PDF**: https://arxiv.org/pdf/2605.24354
- **详细分析**: [[20_Research/Papers/世界模型/SparseWorld_Enhancing_End-to-End_Autonomous_Driving_via_World_Models_with_Sparse_Scene_Representation|SparseWorld: Enhancing End-to-End Autonomous Driving via World Models with Sparse Scene Representation]]
- **作者**: Ruoyu Wang, Jingke Wang, Yukai Ma, Yuehao Huang, Shuangming Lei, Guanglin Xu, Aixue Ye, Yong Liu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.3（加权：大模型 0.1，世界模型 1.2）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《SparseWorld: Enhancing End-to-End Autonomous Driving via World Models with Sparse Scene Representation》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Drive-OccWorld, DriveWorld, GaussianWorld, SparseWorld, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, world models have made significant progress in enhancing end-to-end driving systems through both future situation forecasting and improved scene understanding. However, existing driving world models are typically built upon dense scene representations, causing high computational costs and redundant information. In this paper, we present SparseWorld, a lightweight world model that focuses on predicting only the critical layout of the scene, enabling efficient future forecasting for end-to-end driving systems. SparseWorld first performs autoregressive rollout to forecast future map elements and surrounding agents, enabling the model to learn how driving scenarios evolve over time. It then leverages these predicted futures to refine downstream motion prediction and trajectory planning. Specifically, we propose a Sparse Dreamer that anticipates future instances in the latent space through joint temporal and spatial attention. By interacting with predicted future instances, the motion planner captures more accurate motion patterns and generates more informed and safety-aware trajectories. Extensive experiments demonstrate that SparseWorld significantly reduces collision risk and achieves state-of-the-art performance on the open-loop planning metrics of the nuScenes dataset with a collision rate of 0.05\%. Moreover, it substantially outperforms the baseline method in closed-loop planning metrics on the Bench2Drive benchmark. Supplementary material is available at the project page: this https URL .

</details>

---
