# cs.CV | Computer Vision and Pattern Recognition | 2026-10-28

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/具身智能/PDRVLA_A_Vision-Language-Action_Model_with_Physical_Dynamics_Representations|PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations]]

![[assets/2610.37381_figure.png|800]]

- **arXiv**: [2610.37381](https://arxiv.org/abs/2610.37381)
- **PDF**: https://arxiv.org/pdf/2610.37381
- **详细分析**: [[20_Research/Papers/具身智能/PDRVLA_A_Vision-Language-Action_Model_with_Physical_Dynamics_Representations|PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations]]
- **作者**: Hanqing Wang, Zhaotian Cai, Ruichuan An, Bohan Zeng, Tao Zhang, Yilin Chen, Xu Jiang, Kaiquan Chen, Chongyang Wu, Haoran Li, Fan Yang, Mingan Lin...
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 强化学习
- **相关性评分**: 3.02（加权：具身智能 1.8，强化学习 0.16，世界模型 0.56，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《PDRVLA: A Vision-Language-Action Model with Physical Dynamics Representations》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GR00T-X-Embodiment-Sim, HuggingFaceVLA, InternVLA, Meta-World, PDRVLA, RoboSet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision--Language--Action (VLA) models generate robot actions from visual observations and language instructions, but their understanding of physical dynamics remains limited. Video world models can capture scene dynamics, yet generating future videos introduces high latency into the control loop. We introduce PDRVLA, whose lightweight Physical Dynamics Module extracts physical tokens from vision--language features to condition action generation without online video generation. The module learns through direct prediction of future RGB, depth, and optical-flow features, with auxiliary supervision through a frozen pretrained video world model. Training relies entirely on publicly available data, expanded through human-to-robot synthesis, subtask annotation, and embodied chain-of-thought (ECoT) annotation. Across four simulation benchmarks, PDRVLA achieves success rates of 99.3% on LIBERO, 89.9% on LIBERO-Plus, 93.6% on RoboTwin~2.0, and 81.5% on SimplerEnv. Ablations show improved future prediction with world-model supervision and evaluate how subtask conditioning, future object-pose supervision, and ECoT training affect action success.

</details>

---

### [[20_Research/Papers/具身智能/Vision-Language-Action_or_World-Action_Just_Action_Models|Vision-Language-Action or World-Action? Just Action Models]]

![[assets/2610.37219_figure.png|800]]

- **arXiv**: [2610.37219](https://arxiv.org/abs/2610.37219)
- **PDF**: https://arxiv.org/pdf/2610.37219
- **详细分析**: [[20_Research/Papers/具身智能/Vision-Language-Action_or_World-Action_Just_Action_Models|Vision-Language-Action or World-Action? Just Action Models]]
- **作者**: Yonghao Yu, Lang Huang, Runyi Li, Toshihiko Yamasaki
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Vision-Language-Action or World-Action? Just Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The vision-language-action (VLA) and world-action model (WAM) communities debate whether control policies should inherit pretrained knowledge from vision-language models or from visual generators. The debate, however, bundles three separable choices: backbone initialization, the objective applied to future observations, and whether the machinery for that future loss is kept at inference. A gap between a VLA and a WAM therefore cannot simply be attributed to any one of them. We show that decoupling these choices yields a common framework for both families, which we term Just Action Model (JAM): a pretrained visual backbone with an action expert, trained with an action loss and a foresight loss. The foresight loss trains current-observation features to predict frozen encodings of the recorded future through a prediction head discarded after training, so no visual generation is involved in either training or inference, and the backbone can be chosen freely. We first compare objectives within fixed policy architectures, then evaluate the foresight recipe across backbone families. The resulting JAM policies outperform their matched FastWAM and ImageWAM counterparts on LIBERO and LIBERO-Plus, and achieve similar or slightly higher success rates on RoboTwin. Compared with FastWAM, JAM improves the success rates from 97.0%/55.3%/91.2% to 98.2%/64.5%/91.4%, respectively. With cached foresight targets, JAM reduces estimated online training FLOPs per sample per update by 73% relative to FastWAM. Our results show that future supervision improves control without visual generation or additional inference machinery, and strong foresight performance is attainable with either generator-initialized or vision-language backbones. Project Page: https://y0uroy.github.io/JAM

</details>

---

### [[20_Research/Papers/具身智能/MCP-Net_Real-Time_Coronary_Perception_Network_and_Topological_Analysis_for_Robotic_Guidewire_Navigation|MCP-Net: Real-Time Coronary Perception Network and Topological Analysis for Robotic Guidewire Navigation]]

![[assets/2610.37127_figure.png|800]]

- **arXiv**: [2610.37127](https://arxiv.org/abs/2610.37127)
- **PDF**: https://arxiv.org/pdf/2610.37127
- **详细分析**: [[20_Research/Papers/具身智能/MCP-Net_Real-Time_Coronary_Perception_Network_and_Topological_Analysis_for_Robotic_Guidewire_Navigation|MCP-Net: Real-Time Coronary Perception Network and Topological Analysis for Robotic Guidewire Navigation]]
- **作者**: Sahar Nasirihaghighi, Tianyuan Wang, Kenan Niu, Stefano Stramigioli
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MCP-Net: Real-Time Coronary Perception Network and Topological Analysis for Robotic Guidewire Navigation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MCP-Net, TVS-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coronary guidewire navigation during percutaneous coronary intervention requires continuous interpretation of vessel anatomy, guidewire position, and target stenosis under two-dimensional X-ray fluoroscopy. While existing approaches commonly address vessel segmentation or device localization as separate tasks, a robotic system requires a more structured perception of the coronary scene to support downstream navigation. In this work, we present a simulation-driven framework centered on a Multi-Task Coronary Perception Network (MCP-Net) for robotic guidewire navigation, integrating coronary vessel segmentation, vascular topology extraction, and roadmap generation. Starting from three-dimensional coronary CT angiography, we generate simulated fluoroscopy images containing vascular structures, simulated guidewires, stenotic lesions with varying severity, and diverse vascular geometries, together with simulation-derived ground truth. MCP-Net jointly performs coronary vessel segmentation, guidewire-tip localization, and stenosis localization from a single fluoroscopic frame. These predictions are subsequently converted into a structured vascular graph containing centerlines, bifurcations, endpoints, branch directions, and branch angles. By associating the predicted stenosis with this graph, the framework generates a roadmap from the automatically selected graph root toward the target lesion. The results demonstrate that the proposed framework can jointly recover coronary perception targets and transform them into an interpretable vascular representation suitable for downstream robotic navigation.

</details>

---

### [[20_Research/Papers/大模型/LingGS_Decoupling_Feed-Forward_Geometry_Prediction_from_Camera_Tracking_for_High-Fidelity_Gaussian_SLAM|LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM]]

![[assets/2610.36853_figure.png|800]]

- **arXiv**: [2610.36853](https://arxiv.org/abs/2610.36853)
- **PDF**: https://arxiv.org/pdf/2610.36853
- **详细分析**: [[20_Research/Papers/大模型/LingGS_Decoupling_Feed-Forward_Geometry_Prediction_from_Camera_Tracking_for_High-Fidelity_Gaussian_SLAM|LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM]]
- **作者**: Da Li, Yihan Zang, Ivan Viola, Zeyu Wang, Dominik Engel
- **cs 子类**: cs.CV, cs.GR
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.9（加权：大模型 0.1，机器人 0.8）
- **关联关键词**: LLM, ComputerVision, Systems

#### 研究背景与动机

《LingGS: Decoupling Feed-Forward Geometry Prediction from Camera Tracking for High-Fidelity Gaussian SLAM》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving high-quality reconstruction and responsive camera tracking remains challenging for monocular RGB Gaussian splatting SLAM under a limited optimization budget. We present an online system that addresses this challenge by combining learned geometric priors with explicit geometric camera tracking, which can substantially outperform learned camera prediction in terms of tracking accuracy. A frozen streaming 3D foundation model serves as a virtual RGB-D sensor, providing depth estimation from monocular video. An explicit geometric solver then estimates camera motion through feature reprojection, and a streaming Gaussian mapper integrates the resulting observations into a dense scene representation. We further show that geometric tracking improves camera pose accuracy across representative streaming geometry backbones, demonstrating the broader applicability of our approach. Extensive experiments on indoor and outdoor datasets show that our method significantly improves reconstruction quality over existing approaches, achieving about 7 FPS on a single RTX 4090 and delivering 2-3 times the throughput of the evaluated prior SLAM systems.

</details>

---

### [[20_Research/Papers/具身智能/Evaluation-Guided_Demonstration_Refinement_for_Vision-Language-Action_Policies_The_Winning_Entry_in_the_MetaFine_Open_Competition|Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition]]

![[assets/2610.36765_first_page.png|800]]

- **arXiv**: [2610.36765](https://arxiv.org/abs/2610.36765)
- **PDF**: https://arxiv.org/pdf/2610.36765
- **详细分析**: [[20_Research/Papers/具身智能/Evaluation-Guided_Demonstration_Refinement_for_Vision-Language-Action_Policies_The_Winning_Entry_in_the_MetaFine_Open_Competition|Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition]]
- **作者**: Lifan Zheng, Guotao Chen, Zhenyang Li, Shujie Cui, Qiang Huang, Fan Liu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《Evaluation-Guided Demonstration Refinement for Vision-Language-Action Policies: The Winning Entry in the MetaFine Open Competition》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoRL, MetaFine-Challenge_CoRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We fine-tuned a separate $π_{0.5}$ policy for each of the five tasks in the MetaFine Open Competition, with a task-specific training mixture and number of actions executed per prediction. Training started from the official demonstrations and expert procedures. Local evaluation exposed recurring grasping, pushing, and insertion failures. We addressed them by revising the demonstrated motions and by adding expert continuations from states the policy reached, while keeping nominal demonstrations in training. Checkpoints were compared on every instruction, so that a gain on one instruction could not hide a loss on another. Our submission, MAI, ranked first overall with a score of 96.66.

</details>

---

### [[20_Research/Papers/具身智能/SWIM_Learning_What_Matters_from_Behaviors_for_JEPA_World_Models|SWIM: Learning What Matters from Behaviors for JEPA World Models]]

![[assets/2610.36662_figure.png|800]]

- **arXiv**: [2610.36662](https://arxiv.org/abs/2610.36662)
- **PDF**: https://arxiv.org/pdf/2610.36662
- **详细分析**: [[20_Research/Papers/具身智能/SWIM_Learning_What_Matters_from_Behaviors_for_JEPA_World_Models|SWIM: Learning What Matters from Behaviors for JEPA World Models]]
- **作者**: Jiaming Hu, Shi Bo, Yan Zheng, Tian Wang, Florian Dubost, Alejandro Mottini, Junze Liu, Arvind Srinivasan, Kai Zhong, Kun Qian, Sharon Gao, Vianne Gao...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 0.6，世界模型 1.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《SWIM: Learning What Matters from Behaviors for JEPA World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Joint-embedding predictive architectures (JEPAs) enable world models to plan from images by predicting future embeddings. However, their visual prediction objectives do not explicitly incorporate task-relevant state information, so the physical state that determines task progress may not be reliably captured in the latent space. Supervising world models with simulator state can make planning more informative, but it requires deciding which state features matter. Features are typically selected by hand or weighted uniformly, and a uniform weighting gives every standardized state feature equal influence, so redundant coordinates can overcount the same variation, while irrelevant ones can obscure task-relevant differences. To address this limitation, we propose SWIM (State Weighting with Inverse-Dynamics Model), which learns state weights from offline trajectories by predicting recorded actions from current states and observed future displacements. The learned weights quantify each feature's contribution to action prediction and define a weighted state metric for state-supervised training, which we demonstrate by aligning latent and state distances. The inverse-dynamics model is used only during training, so the resulting world model plans from images with no additional planning-time computation. Across five simulated robotic manipulation tasks, SWIM consistently improves planning success over uniform state weighting.

</details>

---

### [[20_Research/Papers/机器人/Camera-to-Quadruped_Robot_Pose_Estimation_from_Sequential_Images|Camera-to-Quadruped Robot Pose Estimation from Sequential Images]]

![[assets/2610.36599_figure.png|800]]

- **arXiv**: [2610.36599](https://arxiv.org/abs/2610.36599)
- **PDF**: https://arxiv.org/pdf/2610.36599
- **详细分析**: [[20_Research/Papers/机器人/Camera-to-Quadruped_Robot_Pose_Estimation_from_Sequential_Images|Camera-to-Quadruped Robot Pose Estimation from Sequential Images]]
- **作者**: Seobin Hwang, Ji-Seong Beom, Yeong-Jun Cho
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 3.4（加权：具身智能 1.5，机器人 1.9）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Camera-to-Quadruped Robot Pose Estimation from Sequential Images》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadruped robots are increasingly deployed in hazardous environments such as disaster response and facility inspection, where external-camera monitoring is essential for safe operation. This setting is challenging because quadrupeds are articulated systems with time-varying leg joints, leg symmetry, and frequent self-occlusions, which make keypoint correspondence ambiguous. Moreover, no public benchmark exists, making quantitative comparison difficult. To address these challenges, we propose QuadPose, which estimates the full-body 18-DoF pose (6-DoF base pose + 12-DoF joint angles) from monocular video sequences, and introduce QuadSyn, the first camera-to-quadruped robot pose benchmark. On QuadSyn, QuadPose achieves 92.18% PCK@2.5px, 95.54% PCK-AUC, 85.94% ADD@20cm, 66.98% ADD-AUC, and 3.65 degree mean joint-angle error at approximately 33 FPS.

</details>

---
