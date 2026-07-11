# cs.CV | Computer Vision and Pattern Recognition | 2026-07-09

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/具身智能/Scaling_Mixture-of-Experts_Video_Pretraining_for_Embodied_Intelligence|Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence]]

![[assets/2607.07675_first_page.png|800]]

- **arXiv**: [2607.07675](https://arxiv.org/abs/2607.07675)
- **PDF**: https://arxiv.org/pdf/2607.07675
- **详细分析**: [[20_Research/Papers/具身智能/Scaling_Mixture-of-Experts_Video_Pretraining_for_Embodied_Intelligence|Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence]]
- **作者**: Shuailei Ma, Jiaqi Liao, Xinyang Wang, Jingjing Wang, Chaoran Feng, Zijing Hu, Chong Bao, Zichen Xi, Yuqi Gan, Weisen Wang, Yanhong Zeng, Qin Zhao...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 1.2，大模型 0.1，机器人 0.2）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《Scaling Mixture-of-Experts Video Pretraining for Embodied Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the recent promise in robot control, video generative models suffer from a domain mismatch due to their primary focus on content creation. For example, their design inherently prioritizes visual fidelity and creativity over computational efficiency and physical realism. In this work, we present LingBot-Video, a DiT-based video pretraining paradigm specifically tailored for embodied intelligence. From the architecture perspective, we adopt the Mixture-of-Experts (MoE), instead of dense, framework to achieve a better trade-off between modeling capacity and inference efficiency, and manage to scale it up from scratch. From the data perspective, we construct a data profiling engine that augments standard internet videos with extensive robot-oriented footage, encompassing manipulation, navigation, and egocentric perspectives, to equip the base model with an intrinsic understanding of actions and world dynamics. From the training perspective, we develop a multi-dimensional reward system to enforce the alignment regarding physical rationality and task completion, going beyond standard criteria such as aesthetics, prompt-following, and motion consistency. Comprehensive evaluations validate its performance and efficiency as a video foundation model. We contribute LingBot-Video as the inaugural large-scale, open-source MoE video foundation model to the community, in a pioneering effort to bridge digital creativity and physical actuation.

</details>

---

### [[20_Research/Papers/大模型/MedPMC_A_Systematic_Framework_for_Scaling_High-Fidelity_Medical_Multimodal_Data_for_Foundation_Models|MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models]]

![[assets/2607.07673_figure.png|800]]

- **arXiv**: [2607.07673](https://arxiv.org/abs/2607.07673)
- **PDF**: https://arxiv.org/pdf/2607.07673
- **详细分析**: [[20_Research/Papers/大模型/MedPMC_A_Systematic_Framework_for_Scaling_High-Fidelity_Medical_Multimodal_Data_for_Foundation_Models|MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models]]
- **作者**: Hyunjae Kim, Dain Kim, Pan Xiao, Serina S. Applebaum, Younjoon Chung, Xuguang Ai, Yu Yin, Roy Jiang, Yuexi Du, Yawen Wei, Yiming Kong, Tuo Guo...
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《MedPMC: A Systematic Framework for Scaling High-Fidelity Medical Multimodal Data for Foundation Models》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Medicine is inherently multimodal, requiring clinicians to synthesize information across diverse data streams. Yet the development of multimodal foundation models is constrained by limited access to large-scale, high-quality clinical data. Although PubMed Central (PMC) offers a complementary source of expert-authored image-text data, existing PMC-derived resources remain limited in fidelity, reproducibility, and clinical validation. We introduce MedPMC, an automated, continuously updatable framework that transforms permissively licensed literature into high-fidelity infrastructure for medical multimodal models. Applied to 6.1 million PMC articles, MedPMC curated 11 million medical image-text pairs. Component evaluations showed strong performance for initial screening (F1 = 93.2), multi-panel figure detection (F1 = 96.5), figure separation (mAP = 89.8), caption separation and alignment (F1 = 81.4; ROUGE-L = 85.3), and medical figure classification (F1 = 96.5). Manual review by five annotators, three with medical training, found 95.3% of MedPMC images medically relevant, versus 19.7% in a prior PMC-derived dataset. Across 26 benchmarks spanning 11 specialties, a MedPMC-trained CLIP-style model improved average zero-shot AUC by 7.1 percentage points over the strongest architecture-matched biomedical CLIP baseline despite using fewer than half as many image-text pairs. As the vision encoder in a multimodal large language model, it improved medical visual question-answering by 1.9 and 16.9 percentage points across two benchmarks. In 10,524 Yale New Haven Health System dermatology photographs, it improved morphology-to-image retrieval Recall@5 by 11.7 percentage points. These findings show that high-fidelity literature curation strengthens medical multimodal foundation models across benchmark and clinical settings. We publicly release the framework, corpus, benchmarks, and pretrained models.

</details>

---

### [[20_Research/Papers/具身智能/Dual_Latent_Memory_in_Vision-Language-Action_Models_for_Robotic_Manipulation|Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation]]

![[assets/2607.07608_figure.png|800]]

- **arXiv**: [2607.07608](https://arxiv.org/abs/2607.07608)
- **PDF**: https://arxiv.org/pdf/2607.07608
- **详细分析**: [[20_Research/Papers/具身智能/Dual_Latent_Memory_in_Vision-Language-Action_Models_for_Robotic_Manipulation|Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation]]
- **作者**: Hongyu Qu, Jianzhe Gao, Xiaobin Hu, Shaohuan Yang, Xinlei Yu, Rui Yan, Wenguan Wang, Xiangbo Shu, Shuicheng Yan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.7（加权：具身智能 2.7，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Dual Latent Memory in Vision-Language-Action Models for Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LaMem-VLA, MemoryVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mainstream Vision-Language-Action (VLA) models predict actions primarily from the current observation under a Markovian assumption, thus struggling with long-horizon, temporally dependent tasks. Existing memory-augmented VLAs either expand the observation window or retrieve history from the memory bank as auxiliary policy-side context. However, they leave memory outside the native latent embedding space of VLA reasoning, preventing historical experience from being fluidly interleaved with multimodal reasoning and action formation. To this end, we introduce LaMem-VLA, a latent-memory-native framework that reconstructs historical experience into latent memory tokens and directly interweaves them with VLA reasoning. At its core, LaMem-VLA introduces four coordinated components: (i) a curator that organizes historical experience into two complementary short-term and long-term memory vaults; (ii) a seeker that queries both vaults using the multimodal cognition to retrieve context-relevant evidence; (iii) a condenser that reconstructs the retrieved evidence into compact short-term and long-term latent memory tokens; and (iv) a weaver that injects these memory tokens with the current observation and instruction into one continuous embedding sequence. By representing, retrieving, and consuming historical experience entirely in the same continuous latent space, LaMem-VLA enables memory to directly participate in VLA reasoning and guide action generation under a bounded context. Extensive experiments on SimplerEnv and LIBERO demonstrate the superiority of our LaMem-VLA.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedGen_V2_An_Agentic,_Simulation-Ready_3D_World_Engine_for_Embodied_AI|EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI]]

![[assets/2607.07459_figure.png|800]]

- **arXiv**: [2607.07459](https://arxiv.org/abs/2607.07459)
- **PDF**: https://arxiv.org/pdf/2607.07459
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedGen_V2_An_Agentic,_Simulation-Ready_3D_World_Engine_for_Embodied_AI|EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI]]
- **作者**: Xinjie Wang, Liu Liu, Taojun Ding, Andrew Choi, Chaodong Huang, Mengao Zhao, Ziang Li, Jackson Jiang, Chunlei Yu, Shengxiang Liu, Wei Xu, Zhizhong Su
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.9（加权：具身智能 2.4，强化学习 0.2，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《EmbodiedGen V2: An Agentic, Simulation-Ready 3D World Engine for Embodied AI》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present EmbodiedGen V2, a generative 3D world engine for building executable sim-ready environments for embodied intelligence. Sim-ready 3D asset generation has advanced rapidly, yet assembling such assets into policy-ready task environments remains largely manual, limiting scalable closed-loop learning. EmbodiedGen V2 addresses this gap through a unified sim-ready representation that connects cross-simulator assets, interaction affordances, task-driven worlds, large-scale multi-room scenes, and stateful Vibe Coding into a generative, editable, and reusable simulation pipeline. The generated environments support manipulation, navigation, mobile manipulation, cross-simulator deployment, and embodied policy training. In evaluation, the asset pipeline achieves 96.5% human acceptance and 98.6% collision success, and 83.3% of task-driven worlds are directly usable for downstream simulation without manual modification. Online reinforcement learning with generated environments further improves simulation success from 9.7% to 79.8%, and transfers to real robots with task success increasing from 21.7% to 75.0%. These results establish EmbodiedGen V2 as scalable simulation infrastructure for training, evaluating, and deploying embodied policies.

</details>

---

### [[20_Research/Papers/大模型/BUS_Brain-Inspired_Unsupervised_Self-Reflection_for_Advanced_Multimodal_Reasoning|BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning]]

![[assets/2607.07361_figure.png|800]]

- **arXiv**: [2607.07361](https://arxiv.org/abs/2607.07361)
- **PDF**: https://arxiv.org/pdf/2607.07361
- **详细分析**: [[20_Research/Papers/大模型/BUS_Brain-Inspired_Unsupervised_Self-Reflection_for_Advanced_Multimodal_Reasoning|BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning]]
- **作者**: Jiacheng Yang, Tongying Xiao, Yunkai Dang, Cong Wang, Yuekun Yang, Qi Fan, Wenbin Li, Feng Miao, Yang Gao
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《BUS: Brain-Inspired Unsupervised Self-Reflection for Advanced Multimodal Reasoning》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HR-Bench, MME-RealWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current Vision-Language Models (VLMs) often struggle to handle complex visual tasks that require consistent and fine-grained reasoning. Recent methods aim to train models to facilitate self-reflective reasoning, i.e., reviewing and improving the generated reasoning. However, they require large volumes of annotated data and lack explicit reflective behavior during test time. This work aims to bridge this gap through inspiration from neuroscience. The human brain exhibits efficient backward prediction, i.e., predicting which current states are likely to precede a given future state. In this work, we first verify that mainstream VLMs can perform backward prediction, similar to the human brain. Then, we propose Brain-inspired Unsupervised Self-reflection (BUS), a label-free training framework to enhance reflective reasoning capability in challenging image analysis. BUS enables VLMs to perform backward prediction and provide explicit learning signals on data without ground-truth labels. In this way, BUS eliminates reliance on annotated data while improving reasoning performance. Notably, BUS is compatible with popular fine-tuning methods, such as Supervised Fine-Tuning (SFT) and Reinforcement Learning (RL). Finally, extensive experiments on 8 benchmarks demonstrate the effectiveness of BUS across a wide range of complex visual tasks. It achieves notable improvements over the base model while using only unlabeled training data. Our experimental findings validate that backward prediction capability is critical for VLM reasoning.

</details>

---

### [[20_Research/Papers/具身智能/Ego-Human_Motion_Prediction_with_3D-Aware_LLM|Ego-Human Motion Prediction with 3D-Aware LLM]]

![[assets/2607.07001_figure.png|800]]

- **arXiv**: [2607.07001](https://arxiv.org/abs/2607.07001)
- **PDF**: https://arxiv.org/pdf/2607.07001
- **详细分析**: [[20_Research/Papers/具身智能/Ego-Human_Motion_Prediction_with_3D-Aware_LLM|Ego-Human Motion Prediction with 3D-Aware LLM]]
- **作者**: Yujin Bae, Jaewoo Jeong, Hyeonseong Kim, Kuk-Jin Yoon
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.4，机器人 0.2）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《Ego-Human Motion Prediction with 3D-Aware LLM》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Anticipating human motion from an egocentric perspective is fundamental for proactive assistance in AR/VR, human-robot collaboration, and embodied AI. While recent works incorporate language as a semantic prior to reduce the ill-posed nature of egocentric forecasting, they largely neglect the 3D spatial and semantic context that governs how motion unfolds, and treat pose and language prediction as separate inference streams. We introduce Ego3DLM, built on two core principles: accurate motion forecasting requires explicit spatial and semantic understanding of the 3D environment, and pose and language must be predicted holistically in a single pass, since motion is inherently tied to the semantic interpretation of actions being performed. Given three-point tracking, 3D scene features, and egocentric video, Ego3DLM simultaneously decodes past pose, future pose, past narration, and future narration in a single autoregressive pass, grounding predicted poses and descriptions in one another to enforce cross-modal and temporal consistency. We adopt a three-stage training scheme: (1) spatial-semantic scene awareness pretraining; (2) holistic instruction tuning over all four outputs in a single pass; and (3) GRPO-based reinforcement finetuning with intra- and inter-modal rewards that directly optimize pose-language fidelity. Experiments on the Nymeria benchmark demonstrate that Ego3DLM achieves state-of-the-art performance across future motion prediction, past motion tracking, and motion description, showing that 3D scene grounding and holistic cross-modal prediction yield physically plausible and semantically coherent motion forecasts. The project page is available at https://jaewoo97.github.io/Ego3DLM/.

</details>

---

### [[20_Research/Papers/机器人/Dynamic_Object_Detection_and_Tracking_in_Construction_A_Fisheye_Camera_and_LiDAR_Sensor_Fusion_Model|Dynamic Object Detection and Tracking in Construction: A Fisheye Camera and LiDAR Sensor Fusion Model]]

![[assets/2607.06896_first_page.png|800]]

- **arXiv**: [2607.06896](https://arxiv.org/abs/2607.06896)
- **PDF**: https://arxiv.org/pdf/2607.06896
- **详细分析**: [[20_Research/Papers/机器人/Dynamic_Object_Detection_and_Tracking_in_Construction_A_Fisheye_Camera_and_LiDAR_Sensor_Fusion_Model|Dynamic Object Detection and Tracking in Construction: A Fisheye Camera and LiDAR Sensor Fusion Model]]
- **作者**: Yilong Chen, Huili Huang, Yong K. Cho
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Dynamic Object Detection and Tracking in Construction: A Fisheye Camera and LiDAR Sensor Fusion Model》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust dynamic object detection and tracking are essential for enabling robots to operate safely and effectively alongside humans in complex environments such as construction sites. While LiDAR-based SLAM and occupancy grid methods offer viable solutions for detecting and tracking motion, many state-of-the-art 3D vision approaches rely heavily on pre-trained neural networks and require additional post-processing to identify moving objects. Sensor fusion techniques, combining the precision of LiDAR with the semantic richness of RGB imagery, offer a promising alternative. In this work, we present a novel framework that enhances a quadruped robot equipped with a LiDAR sensor and an upward-facing fisheye camera for real-time dynamic object detection and tracking. After identifying moving objects within a registered point cloud, our method assigns semantic labels by projecting 3D coordinates onto a 2D cylindrical panorama, aligning with real-time image-based detections for observation update of the Kalman filter. The proposed system demonstrates high precision, simplicity, and robustness, particularly in handling objects transitioning between dynamic and static states, thus it is well-suited for deployment in real-world construction environments.

</details>

---

### [[20_Research/Papers/大模型/LEMUR_2_Unlocking_Neural_Network_Diversity_for_AI|LEMUR 2: Unlocking Neural Network Diversity for AI]]

![[assets/2607.06839_figure.png|800]]

- **arXiv**: [2607.06839](https://arxiv.org/abs/2607.06839)
- **PDF**: https://arxiv.org/pdf/2607.06839
- **详细分析**: [[20_Research/Papers/大模型/LEMUR_2_Unlocking_Neural_Network_Diversity_for_AI|LEMUR 2: Unlocking Neural Network Diversity for AI]]
- **作者**: Tolgay Atinc Uzun, Waleed Khalid, Saif U Din, Sai Revanth Mulukuledu, Akashdeep Singh, Chandini Vysyaraju, Raghuvir Duvvuri, Avi Goyal, Yashkumar Rajeshbhai Lukhi, Muhammad A. Hussain, Krunal Jesani, Usha Shrestha...
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《LEMUR 2: Unlocking Neural Network Diversity for AI》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AirNet, AlexNet, BagNet, DenseNet, FBNet, HW-NAS-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing NAS benchmarks (e.g., NAS-Bench, NATS-Bench) cover only narrow, task-specific regions of the architectural design space and lack cross-domain or deployment-aware evaluation. LEMUR 2 introduces a large-scale, extensible framework unifying generative, evaluative, and deployment pipelines to unlock neural-network diversity. It comprises over 14,000 distinct architectures and more than 750,000 structured training records documenting model performance, hyperparameters, and task outcomes. These models were produced through AST-based code mutation, genetic and reinforcement-learning evolution, generation of fractal architectures, and synthesis guided by a Large Language Model (LLM). This includes deep models generated with the retrieval-augmented system NN-RAG, which derived and used architectural motifs from over 900 PyTorch modules extracted from public repositories. LEMUR 2 further employs NN-VR and NN-Lite pipelines for automated deployment and latency benchmarking on heterogeneous mobile and Unity-based VR platforms, providing real-device performance metadata. It spans multimodal tasks, image captioning, text-to-image synthesis, and language modeling, supporting cross-domain analysis of architectural transferability. By linking diverse architectures, tasks, and deployment data, LEMUR 2 provides the data foundation for LLM fine-tuning and coupling diverse architectural origins with large-scale, cross-platform empirical validation. This dataset defines a new basis for reproducible and data-driven AI design, advancing the emerging paradigm of LLM-driven AutoML and architectural generalization across modalities and hardware.

</details>

---
