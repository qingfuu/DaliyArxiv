# cs.CV | Computer Vision and Pattern Recognition | 2026-06-15

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/大模型/RepFusion_Leveraging_Multimodal_Priors_for_Denoising_in_Representation_Space|RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space]]

![[assets/2606.14700_figure.png|800]]

- **arXiv**: [2606.14700](https://arxiv.org/abs/2606.14700)
- **PDF**: https://arxiv.org/pdf/2606.14700
- **详细分析**: [[20_Research/Papers/大模型/RepFusion_Leveraging_Multimodal_Priors_for_Denoising_in_Representation_Space|RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space]]
- **作者**: Xichen Pan, Aashu Singh, Satya Narayan Shukla, Xiangjun Fan, Shlok Kumar Mishra, Saining Xie
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《RepFusion: Leveraging Multimodal Priors for Denoising in Representation Space》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GenEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are widely used in text-to-image (T2I) systems, but they are typically limited to text encoding, while denoising is handled by newly trained generative backbones. The emergence of representation autoencoders (RAEs) shifts the generation target toward semantically structured visual representations, creating a latent space that is more compatible with pretrained LLM priors. Inspired by multimodal LLMs (MLLMs), where an MLP projector is sufficient to align clean visual representations with a pretrained LLM, we repurpose the MLLM itself as a noisy representation encoder, extending this mechanism from clean to noisy inputs. We present RepFusion, which uses the resulting MLLM outputs as the conditioning signal for a diffusion transformer. In controlled comparisons at similar inference budgets, RepFusion outperforms baselines that devote comparable capacity to newly initialized denoisers. These results demonstrate that MLLMs provide strong priors for denoising visual representations and that, by conditioning on evolving noisy representations, test-time compute can be productively spent on repeated MLLM conditioning in modern T2I systems.

</details>

---

### [[20_Research/Papers/机器人/Instruct-Particulate_Scaling_Feed-Forward_3D_Object_Articulation_with_Kinematic_Control|Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control]]

![[assets/2606.14699_figure.png|800]]

- **arXiv**: [2606.14699](https://arxiv.org/abs/2606.14699)
- **PDF**: https://arxiv.org/pdf/2606.14699
- **详细分析**: [[20_Research/Papers/机器人/Instruct-Particulate_Scaling_Feed-Forward_3D_Object_Articulation_with_Kinematic_Control|Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control]]
- **作者**: Ruining Li, Yuxin Yao, Matt Zhou, Chuanxia Zheng, Christian Rupprecht, Joan Lasenby, Shangzhe Wu, Andrea Vedaldi
- **cs 子类**: cs.CV, cs.GR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Instruct-Particulate: Scaling Feed-Forward 3D Object Articulation with Kinematic Control》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HY3D-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reconstructing articulated 3D objects is important for animation, gaming, and robotic simulations. Recent neural networks can estimate the articulated structure of 3D objects, but their generalization remains limited by the scarcity of annotated data for this task. To address this gap, we introduce Instruct-Particulate, a model that takes a 3D mesh together with a target kinematic specification, including part descriptions, connectivity, joint types, and optional point prompts, and predicts the corresponding kinematic part segmentation and joint motion parameters. The kinematic specification disambiguates the task and allows the model to target annotations of different granularity, thereby making it possible to use more abundant heterogeneous training data. At test time, the kinematic specification can be obtained automatically from large-scale vision-language models, so the model can be applied to any input mesh. To train our model at scale, we construct a heterogeneous dataset of more than 150,000 articulated 3D objects, extending existing publicly available collections with data obtained by partially labelling other 3D models (monolithic or already decomposed into parts) with kinematic labels by means of vision-language models. Experiments show that our model generalizes better across categories and to AI-generated meshes, enabling articulated asset reconstruction from real-world images via image-to-3D models.

</details>

---

### [[20_Research/Papers/大模型/NEST3D_A_High-Resolution_Multimodal_Dataset_of_Sociable_Weaver_Tree_Nests|NEST3D: A High-Resolution Multimodal Dataset of Sociable Weaver Tree Nests]]

![[assets/2606.14562_figure.png|800]]

- **arXiv**: [2606.14562](https://arxiv.org/abs/2606.14562)
- **PDF**: https://arxiv.org/pdf/2606.14562
- **详细分析**: [[20_Research/Papers/大模型/NEST3D_A_High-Resolution_Multimodal_Dataset_of_Sociable_Weaver_Tree_Nests|NEST3D: A High-Resolution Multimodal Dataset of Sociable Weaver Tree Nests]]
- **作者**: Constanza A. Molina Catricheo, Simon Boeder, Ting-Jia Guo, Giacomo May, Clément Berthelot, Devis Tuia, Friedrich Fedor Reinhard, Fabio Remondino, Benjamin Risse
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.6（加权：大模型 0.4，机器人 0.2）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《NEST3D: A High-Resolution Multimodal Dataset of Sociable Weaver Tree Nests》归入 大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RandLA-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sociable weaver nests function as complex ecological structures offering thermoregulatory microhabitats and sustaining diverse species; however, datasets used in prior studies lack fine-grained 3D structural detail. Producing usable and accurate 3D weaver nest data is challenging due to their irregular geometry and integration with complex host vegetation. We bridge this gap with an open-access, 1.4 TB multimodal drone dataset of 104 nest-bearing trees, comprising 27,945 RGB images, 111,780 multispectral images, approximately 781 million 3D points, and expert-annotated semantic segmentation labels. We benchmark semantic segmentation using KPConv, RandLA-Net, and Point Transformer V3, with PT-v3 achieving an mIoU of 86.35% on the test set. While the results demonstrate strong performance for transformer-based and point-wise methods, they also highlight architecture-dependent challenges, particularly for convolution-based approaches such as KPConv. By uniquely combining spectral, spatial, and structural information, the presented dataset advances 3D reconstruction, segmentation, and classification algorithms, enabling ecological applications from nest volume estimation to species conservation, and serves as a demanding benchmark that exposes architecture-dependent performance under extreme class imbalance.

</details>

---

### [[20_Research/Papers/具身智能/MUSE_Agentic_3D_Scene_Authoring_via_Memory-Grounded_Incremental_Requirement_Satisfaction|MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction]]

![[assets/2606.14168_figure.png|800]]

- **arXiv**: [2606.14168](https://arxiv.org/abs/2606.14168)
- **PDF**: https://arxiv.org/pdf/2606.14168
- **详细分析**: [[20_Research/Papers/具身智能/MUSE_Agentic_3D_Scene_Authoring_via_Memory-Grounded_Incremental_Requirement_Satisfaction|MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction]]
- **作者**: Ruijie Xu, Xinnan Zhu, Jiayu Ying, Daoguo Dong, Yuzhou Ji, Xin Tan
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.7（加权：具身智能 0.6，大模型 0.1）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MUSE: Agentic 3D Scene Authoring via Memory-Grounded Incremental Requirement Satisfaction》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AuthorBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-driven 3D scene generation is a promising technique for digital content creation, embodied AI simulation, and interactive design, yet practical workflows often require refining, extending, or correcting existing scenes while preserving non-target content. Existing methods can produce realistic and structurally plausible scenes, but they generally lack editability with requirement-level state tracking, so part-level failures often lead to full-scene regeneration or manual intervention. To tackle this challenge, we formulate controllable 3D scene authoring as incremental requirement satisfaction, unifying construction and editing. In this paper, we present MUSE, a memory-grounded multi-agent framework in which an Architect compiles instructions into structured requirements, a Sculptor executes local scene operations, and an Inspector verifies each step while updating Working, Scene, and Skill Memory. To evaluate requirement-level controllability and preservation-aware editing, we introduce AuthorBench, offering 145 constrained construction cases and a 1,584-case preservation-aware editing pool paired with external structured checks. On full construction cases, MUSE improves All-Goal success from 37.9 to 80.7 and surface-constraint fulfillment from 35.0 to 92.6 over the strongest baseline. On a stratified 240-case editing test split, MUSE achieves 49.6 All-Goal success, 99.9 preservation rate, and only 0.6 unintended change rate. Beyond automated metrics, human evaluations on compared local-editing baselines support stronger alignment with user intent, and downstream navigation-proxy tests indicate stronger spatial stability. Combined with ablations validating our memory designs, these results establish MUSE as an effective framework for controllable 3D scene authoring.

</details>

---

### [[20_Research/Papers/具身智能/Encoder_Winners_Do_Not_Reliably_Transfer_Across_VLA_Backbone_Scale_A_Frozen-Backbone_Grafting_Diagnostic|Encoder Winners Do Not Reliably Transfer Across VLA Backbone Scale: A Frozen-Backbone Grafting Diagnostic]]

![[assets/2606.14153_figure.png|800]]

- **arXiv**: [2606.14153](https://arxiv.org/abs/2606.14153)
- **PDF**: https://arxiv.org/pdf/2606.14153
- **详细分析**: [[20_Research/Papers/具身智能/Encoder_Winners_Do_Not_Reliably_Transfer_Across_VLA_Backbone_Scale_A_Frozen-Backbone_Grafting_Diagnostic|Encoder Winners Do Not Reliably Transfer Across VLA Backbone Scale: A Frozen-Backbone Grafting Diagnostic]]
- **作者**: Qingping Zeng, Fei She
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.2，机器人 0.3）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Encoder Winners Do Not Reliably Transfer Across VLA Backbone Scale: A Frozen-Backbone Grafting Diagnostic》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA, SmolVLA-EdgeBench, VLM4VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies typically inherit their vision encoder from upstream VLM releases, but it is unclear whether an encoder choice validated on a small VLA transfers to a larger backbone. We introduce a frozen-backbone grafting diagnostic: the vision tower of a released VLA is replaced by a candidate encoder under a fixed protocol (adaptive average pooling, LayerNorm, and a single trainable linear projector), with the language model and action expert frozen. Across four encoders, two LIBERO suites, two backbones (SmolVLA-450M and $π_{0.5}$-3.3B), and two-to-three seeds per cell (40 main grafting runs plus native, LoRA, pooling, and zero-/shuffled-image controls, all scored by offline action MSE), the small-backbone winner does not reliably select the large-backbone top tier: SigLIP is best on SmolVLA across both suites, while on $π_{0.5}$ DINOv2-small leads the spatial suite and the object suite is a seed-sensitive near-tie band; three of the four backbone-suite comparisons (and 11 of 12 seed-level cells) support backbone-dependent rankings. The grafting wrapper is itself non-neutral with opposite sign across backbones (+45-56% MSE on the SmolVLA native tower, -50-52% on $π_{0.5}$), so all conclusions are conditional on the fixed grafting protocol. We position frozen grafting as a cheap target-backbone diagnostic to run before committing to an encoder at scale, not as a closed-loop deployment claim.

</details>

---

### [[20_Research/Papers/机器人/WAM4D_Fast_4D_World_Action_Model_via_Spatial_Register_Tokens|WAM4D: Fast 4D World Action Model via Spatial Register Tokens]]

![[assets/2606.14048_figure.png|800]]

- **arXiv**: [2606.14048](https://arxiv.org/abs/2606.14048)
- **PDF**: https://arxiv.org/pdf/2606.14048
- **详细分析**: [[20_Research/Papers/机器人/WAM4D_Fast_4D_World_Action_Model_via_Spatial_Register_Tokens|WAM4D: Fast 4D World Action Model via Spatial Register Tokens]]
- **作者**: Ying Li, Xiaobao Wei, Jiajun Cao, Hao Wang, Xiaowei Chi, Chengyu Bai, Qianpu Sun, Jiajun Li, Xiaojie Zhang, Jian Tang, Sirui Han, Shanghang Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《WAM4D: Fast 4D World Action Model via Spatial Register Tokens》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World action models (WAMs) have recently shown promise in jointly modeling future observations and executable robot actions. However, most existing WAMs still operate in 2D video or latent spaces, where visually plausible rollouts miss the 3D spatial constraints and occluded contact geometry required for precise manipulation. While geometric foundation models offer strong priors for recovering dense 3D structure and motion from visual observations, forcing WAMs to predict the dense 4D representation introduces costly geometric decoding and slows down causal action generation. To address the trade-off, we present WAM4D, a fast 4D world action model that uses lightweight spatial register tokens as training-time future-depth readouts to transfer pretrained geometric priors into a causal video-action transformer, then removes the register branch for lightweight action inference. To prevent non-causal shortcuts, we further design causal mixture attention for the Mixture-of-Transformers (MoT) WAM backbone, defining modality-specific visibility among video, action, and geometry tokens. Comprehensive experiments on RoboTwin 2.0 and challenging real-world manipulation tasks show that WAM4D improves spatial consistency and achieves competitive action prediction while maintaining efficient inference.

</details>

---

### [[20_Research/Papers/具身智能/RT-VLA_Real-Time_Vision-Language-Action_Models_via_Knowledge_Distillation|RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation]]

![[assets/2606.14010_figure.png|800]]

- **arXiv**: [2606.14010](https://arxiv.org/abs/2606.14010)
- **PDF**: https://arxiv.org/pdf/2606.14010
- **详细分析**: [[20_Research/Papers/具身智能/RT-VLA_Real-Time_Vision-Language-Action_Models_via_Knowledge_Distillation|RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation]]
- **作者**: Xiangyu Huang, Zhenlin Hua, Han Zhou, Shounak Sural, Ragunathan Rajkumar
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.0（加权：具身智能 2.7，机器人 0.3）
- **关联关键词**: Multimodal

#### 研究背景与动机

《RT-VLA: Real-Time Vision-Language-Action Models via Knowledge Distillation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AutoVLA, OpenDriveVLA, RT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong potential for end-to-end autonomous driving by jointly modeling visual perception, language reasoning, explainability and action prediction. However, their large vision-language backbones and reasoning modules introduce substantial inference latency and thereby prevent their deployment in the unforgiving reality of the road networks. We propose RT-VLA, a lightweight, distilled VLA model that transfers the driving and reasoning capabilities of the state-of-the-art SimLingo model into a compact student through multi-level supervised distillation. RT-VLA preserves language-based reasoning and supports post-hoc explanation through offline language analysis of safety-critical driving moments without adding latency to real-time control. Compared to the SimLingo teacher, RT-VLA maintains competitive closed-loop driving and language reasoning performance while reducing inference time by 44.8X in vision-only mode and 7.9X in vision+language mode. These results suggest that supervised distillation is a practical approach for building real-time, explainable VLA-style autonomous driving models.

</details>

---

### [[20_Research/Papers/具身智能/PhysVLA_Towards_Physically-Grounded_VLA_for_Embodied_Robotic_Manipulation|PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation]]

![[assets/2606.13886_figure.png|800]]

- **arXiv**: [2606.13886](https://arxiv.org/abs/2606.13886)
- **PDF**: https://arxiv.org/pdf/2606.13886
- **详细分析**: [[20_Research/Papers/具身智能/PhysVLA_Towards_Physically-Grounded_VLA_for_Embodied_Robotic_Manipulation|PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation]]
- **作者**: Namai Chandra, Shriram Damodaran, Lin Wang
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.7（加权：具身智能 3.6，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《PhysVLA: Towards Physically-Grounded VLA for Embodied Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Diffusion-VLA, FD-VLA, Force-VLA, ForceVLA, Generalist-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models excel at mapping visual inputs and natural language instructions directly to robotic control policies. However, because they are trained primarily to fit behavioural demonstration data, they do not explicitly enforce fundamental physical principles such as rigid-body dynamics or contact constraints. This exposes a critical physics gap: standard temporal smoothing applied on top of single-step or chunked VLAs trades trajectory quality for added failures that short-term memory cannot resolve. To bridge this gap, we introduce PhysVLA (Physics-VLA), a plug-and-play, inference-time framework designed to wrap any frozen VLA backbone without retraining, fine-tuning, or weight access, with less than 1 ms of overhead per control step. PhysVLA intercepts the predicted control action, captures only the simulator or system state, and applies a dual-layered correction: (i) a phase-aware finite-state machine that structures discrete task segments (approach, grasp, transport, and place), and (ii) a selective Euler-Lagrange gate that activates only when a dynamics oracle detects kinodynamic inconsistency. Evaluated across OpenVLA, OpenVLA-OFT, Force-VLA, and Generalist-VLA on LIBERO-Spatial with a 7-DoF Franka Panda, the framework delivers absolute success rate increases of up to 17% and stability increases of up to 19% with no per-task regressions, improves trajectory efficiency by up to 15% across all four backbones, and shows up to a 10x improvement in trajectory jerk robustness on a Robosuite Lift cross-simulator sweep. We further validate the framework on a real Agilex Piper arm with a pick-and-place task, confirming that PhysVLA transfers to physical hardware without retraining, with success-rate improvements of up to 50%, establishing physical awareness as a composable, backbone-agnostic runtime module.

</details>

---

### [[20_Research/Papers/具身智能/Multi-Agent_Embodied_Autonomous_Driving_From_V2X_Information_Exchange_to_Shared_World_Models|Multi-Agent Embodied Autonomous Driving: From V2X Information Exchange to Shared World Models]]

![[assets/2606.13840_first_page.png|800]]

- **arXiv**: [2606.13840](https://arxiv.org/abs/2606.13840)
- **PDF**: https://arxiv.org/pdf/2606.13840
- **详细分析**: [[20_Research/Papers/具身智能/Multi-Agent_Embodied_Autonomous_Driving_From_V2X_Information_Exchange_to_Shared_World_Models|Multi-Agent Embodied Autonomous Driving: From V2X Information Exchange to Shared World Models]]
- **作者**: Senkang Hu, Zhengru Fang, Yihang Tao, Zihan Fang, Sam Tak Wu Kwong, Yuguang Fang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 大模型, 机器人
- **相关性评分**: 3.0（加权：具身智能 1.5，大模型 0.4，世界模型 0.8，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Multi-Agent Embodied Autonomous Driving: From V2X Information Exchange to Shared World Models》归入 具身智能、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous driving is shifting from isolated vehicle intelligence toward multi-agent embodied systems that share perception, infer intent, and coordinate action under uncertainty. This survey examines this transition through the lens of Shared World Models (SWMs): predictive cross-agent representations maintained across vehicles, infrastructure, and other traffic participants. We review more than 380 publications spanning vehicle-to-everything (V2X) communication, collaborative perception, inter-agent cognition, cooperative planning, end-to-end cooperative driving, and simulation and data engines for closed-loop validation. The organizing question is how exchanged observations become aligned state, intent-aware interaction, and coordinated downstream action. Across the surveyed literature, evaluation remains concentrated in simulation, curated benchmarks, and offline protocols. Foundation-model-based coordination also lacks verified real-time safety guarantees in open traffic. These gaps motivate key research priorities for multi-agent embodied autonomous driving (MAEAD): verifiable shared-state maintenance, robust intent and plan alignment, and safe coordinated action under communication, latency, and deployment constraints.

</details>

---

### [[20_Research/Papers/具身智能/$μ_0$_A_Scalable_3D_Interaction-Trace_World_Model|$μ_0$: A Scalable 3D Interaction-Trace World Model]]

![[assets/2606.13769_figure.png|800]]

- **arXiv**: [2606.13769](https://arxiv.org/abs/2606.13769)
- **PDF**: https://arxiv.org/pdf/2606.13769
- **详细分析**: [[20_Research/Papers/具身智能/$μ_0$_A_Scalable_3D_Interaction-Trace_World_Model|$μ_0$: A Scalable 3D Interaction-Trace World Model]]
- **作者**: Seungjae Lee, Yoonkyo Jung, Jusuk Lee, Jonghun Shin, Amir Hossein Shahidzadeh, Yao-Chih Lee, H. Jin Kim, Jia-Bin Huang, Furong Huang
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 2.52（加权：具身智能 0.6，大模型 0.1，强化学习 0.16，世界模型 1.16，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《$μ_0$: A Scalable 3D Interaction-Trace World Model》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models that capture how actions induce physical change enable scalable robot learning without reliance on embodiment-specific action labels. Pixel-space video models provide broad visual priors but expend model capacity on dense appearance reconstruction, while direct action models require embodiment-specific labels that hinder scalability. We present $μ_0$, a scalable world model based on 3D traces. Rather than predicting dense pixels or directly modeling actions, $μ_0$ forecasts smooth 3D trajectories for salient interaction points such as objects, tools, hands, and contact regions, yielding a compact, embodiment-agnostic motion interface. To enable training from diverse video sources, our TraceExtract system automatically extracts 3D supervision by selecting keypoints, constructing globally aligned traces, and associating motion segments with hierarchical language captions. This TraceExtract supervision pretrains $μ_0$ by combining a pretrained vision-language backbone with a modular trace expert, which represents each query via B-spline control points and predicts future traces. Experiments show that $μ_0$ outperforms baselines in both 2D and 3D trace prediction, including trace prediction models and tokenized VLM methods. Because $μ_0$ is frozen and reusable, it can be paired with action experts for downstream robot embodiments. Despite action-free pretraining, the resulting trace-conditioned policies achieve performance competitive with VLA models pretrained with action supervision, such as $π_0$. These results establish 3D traces as a scalable and transferable representation for cross-embodiment manipulation.

</details>

---
