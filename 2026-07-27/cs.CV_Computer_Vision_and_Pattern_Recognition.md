# cs.CV | Computer Vision and Pattern Recognition | 2026-07-27

#arxiv #ComputerScience

**论文数**: 7

### [[20_Research/Papers/具身智能/Robot-Factored_World_Models_via_Robot_Rendering|Robot-Factored World Models via Robot Rendering]]

![[assets/2607.22535_figure.png|800]]

- **arXiv**: [2607.22535](https://arxiv.org/abs/2607.22535)
- **PDF**: https://arxiv.org/pdf/2607.22535
- **详细分析**: [[20_Research/Papers/具身智能/Robot-Factored_World_Models_via_Robot_Rendering|Robot-Factored World Models via Robot Rendering]]
- **作者**: Byungjun Kim, Taeksoo Kim, Hyunsoo Cha, Hanbyul Joo
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.9（加权：具身智能 0.6，世界模型 1，机器人 1.3）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Robot-Factored World Models via Robot Rendering》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video world models predict future observations from an initial observation and an action signal. In robotics, actions influence future observations through two distinct processes: they are first realized into robot motion by the robot body and controller, and the scene then responds through contact and object motion. Conditioning directly on action commands asks the world model to learn the realization process itself, while conditioning on logged future states leaks the interaction outcomes it is meant to predict. We propose robot-factored world models, which move two robot-specific factors outside the world model. First, action realization: each command is rolled through the robot's own controller and kinematics into a deployment-available nominal trajectory, a middle signal that avoids both action-realization learning and future-state leakage. Second, robot rendering: this nominal trajectory is rendered through the robot URDF, factoring the robot's geometry, kinematics, and appearance out of the model and into explicit rendered robot geometry. To resolve depth ambiguity, we pair end-effector depth with scene depth, giving geometric cues for contact and occlusion beyond image-plane overlap. Together, camera-aware static RGB/depth context and rendered robot geometry form a shared visual world-model interface that stays consistent across viewpoints and robot embodiments, so the model sees the action only as visible robot geometry and learns how objects respond to it. Our experiments show that the rendered interface outperforms vector-conditioned baselines and generalizes to unseen robot embodiments at inference. We further demonstrate that our model generates robot manipulation videos from human demonstrations by retargeting and rendering the hand motion as robot geometry.

</details>

---

### [[20_Research/Papers/机器人/Geometric_2D_Scene_Graph_Generation|Geometric 2D Scene Graph Generation]]

![[assets/2607.22325_figure.png|800]]

- **arXiv**: [2607.22325](https://arxiv.org/abs/2607.22325)
- **PDF**: https://arxiv.org/pdf/2607.22325
- **详细分析**: [[20_Research/Papers/机器人/Geometric_2D_Scene_Graph_Generation|Geometric 2D Scene Graph Generation]]
- **作者**: Christoph Jahn, Urs Waldmann, Bastian Goldluecke
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Geometric 2D Scene Graph Generation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In production processes for consumer products, assembly instructions are essential not only for planning but also for executing the production process. Likewise in robotics, it is crucial for an assembly robot to understand how components fit together and can be assembled. To facilitate these tasks, we contribute a method for constructing scene graphs to represent and characterize assembly relationships between components. Our approach does not rely on semantic data and is capable of handling a very small dataset. To realize this, the output of a Faster R-CNN model is used to create geometric representations, which are then processed by a transformer architecture to generate an adjacency matrix. This matrix serves as input to a Siamese network that uses message passing based on an attentional graph convolutional network (aGCN) architecture to characterize the connections between the components. We validate our method on a study dataset of toy model components which can be assembled into transportation vehicles.

</details>

---

### [[20_Research/Papers/大模型/RadSight_Towards_Perceptually_Reliable_Multimodal_Radiology_Image_Understanding|RadSight: Towards Perceptually Reliable Multimodal Radiology Image Understanding]]

![[assets/2607.22293_figure.png|800]]

- **arXiv**: [2607.22293](https://arxiv.org/abs/2607.22293)
- **PDF**: https://arxiv.org/pdf/2607.22293
- **详细分析**: [[20_Research/Papers/大模型/RadSight_Towards_Perceptually_Reliable_Multimodal_Radiology_Image_Understanding|RadSight: Towards Perceptually Reliable Multimodal Radiology Image Understanding]]
- **作者**: Jianqin Liu, Weiwei Cao, Wanxing Chang, Ruifeng Yuan, Bowen Shi, Zhilin Zheng, Xianjie Zhang, Ling Zhang, Peng Wang, Jianpeng Zhang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《RadSight: Towards Perceptually Reliable Multimodal Radiology Image Understanding》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CT-FineBench, CT-SpatialVQA, DeepTumorVQA, M3D-Bench, OmniMedVQA, PMC-VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medical multimodal large language models (MLLMs) are increasingly expected to perform complex image understanding tasks, yet their reliability is often compromised by frequent errors in visual interpretation. To systematically trace these failures, we traverse the hierarchy from high-level clinical tasks down to fundamental visual perception. We therefore introduce Perception-Bench, a large-scale benchmark comprising 1.13 million samples that assesses medical MLLMs across six dimensions: attribute judgment, spatial grounding, spatial understanding, disease prediction, anomaly detection, and report generation, spanning both 2D and 3D radiology images. Our analysis on Perception-Bench reveals that existing MLLMs lack the ability to capture even the most basic lesion attributes, such as location, size, and density. This inability to ground clinical outputs in primary visual evidence reveals that the models' diagnostic unreliability is rooted in a critical but overlooked bottleneck in low-level visual perception. Motivated by this, we propose RadSight, a perception-driven MLLM built upon a dual 2D/3D encoder architecture that preserves native imaging spatial structures. RadSight formulates medical image understanding as a four-stage progressive process: visual-language alignment, fine-grained visual perception, clinical diagnosis, and diagnostic interpretation. The model is trained on an 8.37 million perception-oriented corpus using progressive curriculum learning. On Perception-Bench, RadSight consistently outperforms existing MLLMs across all six evaluation dimensions, with particularly strong gains in spatial grounding and clinical diagnosis. It also achieves consistent improvements on public 2D and 3D medical benchmarks, further demonstrating that robust low-level visual perception is a critical foundation for reliable clinical understanding. Code and model will be publicly available.

</details>

---

### [[20_Research/Papers/世界模型/AgentHOI_Multi-Agent_Reasoning_for_Human-Object-Interaction_Video_Generation_via_Implicit_Representation_Alignment|AgentHOI: Multi-Agent Reasoning for Human-Object-Interaction Video Generation via Implicit Representation Alignment]]

![[assets/2607.22241_figure.png|800]]

- **arXiv**: [2607.22241](https://arxiv.org/abs/2607.22241)
- **PDF**: https://arxiv.org/pdf/2607.22241
- **详细分析**: [[20_Research/Papers/世界模型/AgentHOI_Multi-Agent_Reasoning_for_Human-Object-Interaction_Video_Generation_via_Implicit_Representation_Alignment|AgentHOI: Multi-Agent Reasoning for Human-Object-Interaction Video Generation via Implicit Representation Alignment]]
- **作者**: Ziyao Huang, Shunkai Li, Juan Cao, Chenyu Li, Youliang Zhang, Zixiang Zhou, Cong Wang, Yuan Zhou, Qinglin Lu, Fan Tang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.6（加权：大模型 0.4，机器人 0.2）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《AgentHOI: Multi-Agent Reasoning for Human-Object-Interaction Video Generation via Implicit Representation Alignment》归入 大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in video diffusion models have spurred interest in human-object interaction (HOI) video generation, which demands fine-grained control over interaction logic beyond single-subject animation. However, existing HOI methods rely heavily on explicit motion control, limiting scalability and generalization across diverse objects and interactions. In this study, we propose AgentHOI, a text-driven HOI video generation following a thinking-before-generation framework that bridges the gap between high-level textual intent and physical execution through multi-agent reasoning over perception, interaction, and motion planning. Building upon the generated interaction plans, we further strengthen text-driven motion understanding. We introduce an implicit text-motion alignment strategy that distills text-to-motion priors into the video diffusion model, enabling robust HOI synthesis without explicit motion inputs at inference. Experiments show that AgentHOI significantly improves interaction naturalness, object appearance preservation, and adherence to complex textual instructions across challenging object-centric scenarios such as wearing and riding. The code is available at https://github.com/bone-11/agenthoi.

</details>

---

### [[20_Research/Papers/强化学习/LayoutLite_Token-Level_Implicit_Layout_Analysis_for_Efficient_Document_OCR|LayoutLite: Token-Level Implicit Layout Analysis for Efficient Document OCR]]

![[assets/2607.22200_figure.png|800]]

- **arXiv**: [2607.22200](https://arxiv.org/abs/2607.22200)
- **PDF**: https://arxiv.org/pdf/2607.22200
- **详细分析**: [[20_Research/Papers/强化学习/LayoutLite_Token-Level_Implicit_Layout_Analysis_for_Efficient_Document_OCR|LayoutLite: Token-Level Implicit Layout Analysis for Efficient Document OCR]]
- **作者**: Xudong Liu, Bicheng Wan, Yulin Jin
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，强化学习 0.4）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《LayoutLite: Token-Level Implicit Layout Analysis for Efficient Document OCR》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OmniDocBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end OCR systems based on vision-language models have achieved strong performance in complex document OCR, but their efficiency is limited by the large number of visual tokens produced from document images. Many of these tokens correspond to blank margins or visually redundant regions, yet directly applying generic visual token compression methods may remove OCR-critical fine-grained details. In this paper, we propose LayoutLite, a lightweight plug-and-play module for efficient document OCR. Instead of relying on explicit document layout detection, LayoutLite performs implicit layout analysis at the token level between the vision encoder and the language decoder. It aggregates multi-layer visual representations from the vision encoder, and predicts an importance score for each visual token with a lightweight scoring network. Low-information tokens are then removed before entering the language decoder while preserving the original spatial positional information of retained tokens. To train LayoutLite without human annotations, we cast token selection as a reinforcement learning problem and optimize it with a group-relative policy optimization objective driven by OCR output consistency, together with an auxiliary layout supervision signal to stabilize training. Experiments on OmniDocBench demonstrate that LayoutLite can substantially reduce visual token length and inference cost with negligible degradation in recognition quality. We further evaluate LayoutLite on two OCR-specialized VLMs, FireRed-OCR and Logics-Parsing-V2. Under up to 50% token compression, LayoutLite preserves almost the same score on both models while reducing prefill latency, FLOPs, and KV cache memory by over 40%, with only a small additional inference overhead. These results show that token-level implicit layout analysis is an effective and practical approach for accelerating VLM-based OCR systems.

</details>

---

### [[20_Research/Papers/大模型/Low-Altitude_Channel_Multipath_Prediction_via_Panoramic_Perception_and_Vision-Language_Model|Low-Altitude Channel Multipath Prediction via Panoramic Perception and Vision-Language Model]]

![[assets/2607.21953_figure.png|800]]

- **arXiv**: [2607.21953](https://arxiv.org/abs/2607.21953)
- **PDF**: https://arxiv.org/pdf/2607.21953
- **详细分析**: [[20_Research/Papers/大模型/Low-Altitude_Channel_Multipath_Prediction_via_Panoramic_Perception_and_Vision-Language_Model|Low-Altitude Channel Multipath Prediction via Panoramic Perception and Vision-Language Model]]
- **作者**: Zihang Zeng, Shu Sun, Meixia Tao, Zhiyong Chen, Jianhua Mo, Xiangwen Gu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 1.1（加权：大模型 0.9，机器人 0.2）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Low-Altitude Channel Multipath Prediction via Panoramic Perception and Vision-Language Model》归入 大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) communication is expected to support a wide range of low-altitude applications in 6G mobile networks. However, traditional statistical channel models provide limited accuracy in specific environments, while deterministic methods such as ray tracing usually rely on accurate three-dimensional environment models and involve high computational complexity. Existing multimodal channel prediction approaches mainly focus on large-scale metrics such as path loss, and remain insufficient for modeling small-scale parameters. To address these limitations, this paper proposes PanoLAMP, a Panoramic perception and vision-language model-based Low-Altitude Multipath Prediction framework. It adopts a pretrained vision-language model as the backbone and captures the propagation environment features through panoramic RGB-D observations collected at both the transmitter and receiver to predict the delay, power, azimuth angle, and zenith angle offset relative to the line-of-sight path. Experiments are conducted on a synthetic dataset containing 18,949 UAV-vehicle links across seven UAV altitudes. Experimental results show that the proposed method consistently outperforms representative baselines in both multipath parameters and statistical metrics, and demonstrates stronger generalization across different flight heights.

</details>

---

### [[20_Research/Papers/大模型/Oxygen-TryOn_Fashion-Native_Foundation_Model_for_Any-item_Virtual_Try-On|Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On]]

![[assets/2607.21694_figure.png|800]]

- **arXiv**: [2607.21694](https://arxiv.org/abs/2607.21694)
- **PDF**: https://arxiv.org/pdf/2607.21694
- **详细分析**: [[20_Research/Papers/大模型/Oxygen-TryOn_Fashion-Native_Foundation_Model_for_Any-item_Virtual_Try-On|Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On]]
- **作者**: Yong Liu, Xiaolong Fu, Zihang Xu, Wen Xue, Xueheng Li, Lin Song, Yuan Zhang, Chuyang Zhao, Haoyang Huang, Nan Duan, Yipeng Sun, Yan Li...
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.8（加权：大模型 0.4，强化学习 0.4）
- **关联关键词**: LLM, RL, ComputerVision

#### 研究背景与动机

《Oxygen-TryOn: Fashion-Native Foundation Model for Any-item Virtual Try-On》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Oxygen-TryOn, a unified foundation model for any-item virtual try-on. Rather than repurposing a general-purpose image editor, Oxygen-TryOn is fashion-native, built for try-on through a dedicated data engine and try-on-specific training. Given one or more reference items (clean product shots or in-the-wild worn-on photos) and a single target subject image, it synthesizes a photorealistic image of the subject wearing the items across virtually any fashion category. Prior systems handle a single garment category in a studio setting, and recent multi-reference methods remain garment-centric; in contrast, Oxygen-TryOn supports diverse items and scenarios, including full- and half-body views, a variable number of references, and free multi-item composition, while faithfully preserving both subject identity and item appearance. Instead of mask-based inpainting, we reformulate try-on as a multi-reference, understanding-driven generation task. We build a data engine that collects, manufactures, annotates, and filters high-quality try-on data at scale, and design a three-stage recipe of continued pre-training (CPT), supervised fine-tuning (SFT), and reinforcement learning (RL). The RL stage uses a hybrid reward combining an in-house try-on reward model with a proprietary, rubric-guided general-purpose model, jointly supervising fine-grained consistency and instruction-level quality. It also follows general editing instructions (e.g., pose changes) in the same pass. Across public benchmarks and our in-house Oxygen-TryOn Bench, it achieves state-of-the-art consistency and realism on single-item try-on and leads on multi-item try-on, matching or surpassing both leading proprietary systems (Nano Banana Pro, GPT-Image-2, Seedream5 Lite) and open-source models (FLUX.2).

</details>

---
