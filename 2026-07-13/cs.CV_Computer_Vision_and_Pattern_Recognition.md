# cs.CV | Computer Vision and Pattern Recognition | 2026-07-13

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/大模型/Multimodal_Scenario_Similarity_Search_for_Autonomous_Driving|Multimodal Scenario Similarity Search for Autonomous Driving]]

![[assets/2607.09428_figure.png|800]]

- **arXiv**: [2607.09428](https://arxiv.org/abs/2607.09428)
- **PDF**: https://arxiv.org/pdf/2607.09428
- **详细分析**: [[20_Research/Papers/大模型/Multimodal_Scenario_Similarity_Search_for_Autonomous_Driving|Multimodal Scenario Similarity Search for Autonomous Driving]]
- **作者**: Tamás Matuszka, András Tamásy, Balázs Szolár
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Multimodal Scenario Similarity Search for Autonomous Driving》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale autonomous-driving datasets contain vast numbers of recorded scenarios, creating a need for efficient retrieval methods that can identify situations similar to a given query. Existing approaches typically rely on either visual representations or motion-based descriptions, making it difficult to understand their relative strengths and limitations for scenario retrieval. In this work, we present a multimodal framework for autonomous-driving scenario retrieval that combines visual and trajectory-based representations within a unified retrieval pipeline. We investigate two trajectory-based approaches: Exo-Trajectory, an explicit matching method based on surrounding-agent motion, and ScenarioFormer, a transformer-based representation learned from object trajectories using contrastive learning. We compare these approaches against strong vision-based baselines and analyze their behavior across a diverse set of driving scenarios. Experimental results show that trajectory representations provide strong retrieval performance for motion-centric events such as cut-ins, turning maneuvers, and traffic queueing, while visual embeddings excel when appearance cues are informative. Most importantly, combining visual and trajectory information consistently improves retrieval quality, yielding the best overall performance. These findings demonstrate that appearance and motion capture are complementary notions of scenario similarity and motivate multimodal retrieval systems for autonomous-driving data mining, dataset curation, and scenario-based validation.

</details>

---

### [[20_Research/Papers/机器人/AnythingReality_Robust_Online_Gaussian_Splatting_SLAM_for_Open-Vocabulary_VR_Scene_Exploration|AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration]]

![[assets/2607.09260_figure.png|800]]

- **arXiv**: [2607.09260](https://arxiv.org/abs/2607.09260)
- **PDF**: https://arxiv.org/pdf/2607.09260
- **详细分析**: [[20_Research/Papers/机器人/AnythingReality_Robust_Online_Gaussian_Splatting_SLAM_for_Open-Vocabulary_VR_Scene_Exploration|AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration]]
- **作者**: Timofei Kozlov, Dmitrii Maliukov, Andrey Marchenko, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 0.7（加权：大模型 0.1，机器人 0.6）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《AnythingReality: Robust Online Gaussian Splatting SLAM for Open-Vocabulary VR Scene Exploration》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a novel integrated architecture for robust online 3D Gaussian splatting, real-time VR exploration, and speech-driven Vision-Language-Model interaction. Unlike methods assuming clean depth or external poses, our system combines ORB-SLAM3-based pose estimation with online Gaussian reconstruction for noisy real-world data. A VR pipeline enables immersive exploration of incremental reconstructions; a semantic module transcribes voice commands, generates scene descriptions, and records points of interest. Against state-of-the-art online Gaussian splatting methods, we improve image quality on our dataset (+14.5% PSNR, +8.6% SSIM, -14.3% LPIPS) and TUM-RGBD (+11.7% PSNR, +7.8% SSIM, -21.6% LPIPS), with comparable or superior frame rates via quality-speed configurations. We achieve an 88% VLM object-recognition rate.

</details>

---

### [[20_Research/Papers/具身智能/Causally_Debiased_Latent_Action_Model_for_Embodied_Action_Conditioned_World_Models|Causally Debiased Latent Action Model for Embodied Action Conditioned World Models]]

![[assets/2607.09185_figure.png|800]]

- **arXiv**: [2607.09185](https://arxiv.org/abs/2607.09185)
- **PDF**: https://arxiv.org/pdf/2607.09185
- **详细分析**: [[20_Research/Papers/具身智能/Causally_Debiased_Latent_Action_Model_for_Embodied_Action_Conditioned_World_Models|Causally Debiased Latent Action Model for Embodied Action Conditioned World Models]]
- **作者**: Yufan Wei, Kun Zhou, Lingjun Mao, Zijun Zhang, Ziming Xu, Ziqiao Xi, Shuang Liang, Ruobing Han, Yuchen Yan, Xinyue Wang, Fan Feng, Biwei Huang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，世界模型 0.8，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Causally Debiased Latent Action Model for Embodied Action Conditioned World Models》归入 具身智能、世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models (ACWMs) aim to simulate future observations conditioned on embodied actions, offering a promising foundation for robot planning, policy evaluation, and data augmentation. However, learning controllable ACWMs requires large-scale action-labeled data, which remains costly to collect in the real world. Latent action models (LAMs) mitigate this bottleneck by inferring latent actions from unlabeled videos, but existing LAMs are typically trained with reconstruction-only objectives and therefore entangle action-relevant dynamics with action-irrelevant visual factors such as backgrounds and untouched objects. In this work, we identify this action-irrelevant bias as a key obstacle to controllable ACWMs and introduce evaluation metrics to measure latent-action bias, action following, and robustness. We propose CD-LAM, a causally debiased framework for LAM-based ACWMs. CD-LAM introduces three efficient fine-tuning objectives: embodiment-centric reconstruction, action-centric contrastive learning, and latent space calibration, which together encourage embodiment-focused, action-aware, and calibrated non-collapsed latent action representations. Experiments on 2B and 14B ACWM backbones show that CD-LAM substantially improves latent-action controllability, downstream robot-action following, visual fidelity, and adaptation efficiency, requiring only 6k fine-tuning steps and more than 12$\times$ fewer robot-action adaptation updates than the baseline.

</details>

---

### [[20_Research/Papers/大模型/Beyond_Time_Shifts_Adapting_Omni-LLM_as_a_Reference-Free_Evaluator_for_Generative_Audio-Visual_Models|Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models]]

![[assets/2607.09091_figure.png|800]]

- **arXiv**: [2607.09091](https://arxiv.org/abs/2607.09091)
- **PDF**: https://arxiv.org/pdf/2607.09091
- **详细分析**: [[20_Research/Papers/大模型/Beyond_Time_Shifts_Adapting_Omni-LLM_as_a_Reference-Free_Evaluator_for_Generative_Audio-Visual_Models|Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models]]
- **作者**: Yijie Qian, Juncheng Wang, Chao Xu, Huihan Wang, Yuxiang Feng, Yang Liu, Baigui Sun, Yong Liu, Shujun Wang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 0.6（加权：大模型 0.4，强化学习 0.2）
- **关联关键词**: LLM, RL

#### 研究背景与动机

《Beyond Time Shifts: Adapting Omni-LLM as a Reference-Free Evaluator for Generative Audio-Visual Models》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AlignNet, SyncBench, SyncNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As audio-visual generative models evolve into world simulators, cross-modal synchronization stands as a critical proxy for assessing the consistency of world dynamics and causality in generated content. However, existing evaluation metrics presume structural correctness, reducing synchronization to mere temporal alignment. Consequently, they fail on generative outputs, especially when exhibiting structural hallucinations and asymmetric cross-modal relations, which currently \textbf{mandate expert human annotation to assess synchronization.} This dependency introduces a critical paradox: \emph{human evaluators rely on relative, reference-dependent comparisons, whereas automated metrics require reference-free, absolute scalars.} We resolve this paradox by proposing a framework that distills relative human perception into a continuous, globally consistent metric. First, we introduce SynthSync, a dataset of generative failures ranked via pairwise human annotations. Second, we adapt the Omni-LLM equipped with a continuous latent projection to translate relative human rankings into continuous absolute values. Third, we propose Real-Valued Group Relative Policy Optimization ($\mathbb{R}$-GRPO) to internalize the global causal structure of synchronization via listwise score distributions. Empirically, our metric achieves state-of-the-art human preference alignment. We leverage this estimator to establish a standardized benchmark, advancing AV-Gen assessment from low-level signal correlation to visually grounded causality.

</details>

---

### [[20_Research/Papers/强化学习/Toward_Active_Object_Detection_for_UAVs_in_the_Wild_A_Large-Scale_Dataset,_Benchmark_and_Method|Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method]]

![[assets/2607.09078_first_page.png|800]]

- **arXiv**: [2607.09078](https://arxiv.org/abs/2607.09078)
- **PDF**: https://arxiv.org/pdf/2607.09078
- **详细分析**: [[20_Research/Papers/强化学习/Toward_Active_Object_Detection_for_UAVs_in_the_Wild_A_Large-Scale_Dataset,_Benchmark_and_Method|Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method]]
- **作者**: Tianpeng Liu, Xinhua Jiang, Li Liu, Qinmu Shen, Siwei Tang, Zhen Liu, Yongxiang Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，强化学习 0.4，世界模型 0.2，机器人 0.5）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Toward Active Object Detection for UAVs in the Wild: A Large-Scale Dataset, Benchmark and Method》归入 机器人、强化学习、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本中出现的评测对象/数据集包括：ATRNet, DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object detection is a fundamental component in numerous Unmanned Aerial Vehicle (UAV) applications, yet it has long been plagued by hindrances like occlusion or target pixel scarcity. Active Object Detection (AOD) provides a novel paradigm to address these challenges via active vision, while UAV-based AOD research remains scarce due to the lack of high-quality datasets and benchmarks for algorithm development and evaluation. To fill this gap, this paper presents ATRNet-LUDO, the first large-scale real-world dataset for UAV-Ground Active Object Detection (UGAOD). It contains 121,000 multi-view panoramic multi-target aerial images and 1.21 million local single-target slices, covering 10 vehicle targets across 40 scenarios. It enables the construction of diverse training and testing environments for UAV agent interaction and active observation policy learning. Based on this dataset, we establish a comprehensive evaluation benchmark for AOD policy learning methods. Most existing AOD policies rely on Deep Reinforcement Learning (DRL) but suffer from poor generalization. Evaluations on our benchmark reveal a significant generalization gap between training and testing performance, highlighting an urgent need for solutions. To this end, we leverage the Joint Embedding Predictive Architecture (JEPA) to construct a world model that enhances state representation learning, and propose AOD-JEPA by incorporating AOD-specific prior knowledge. Extensive experiments validate its effectiveness and superiority. We hope ATRNet-LUDO and the benchmark will advance research in the UGAOD field. The dataset and code are soon available at https://github.com/Leo000ooo/LUDO_dataset.

</details>

---

### [[20_Research/Papers/大模型/C-GAP_Class-Aware_and_Online_Prompting_Improves_Vision-Language_Models_on_Imbalanced_Classes|C-GAP: Class-Aware and Online Prompting Improves Vision-Language Models on Imbalanced Classes]]

![[assets/2607.09008_figure.png|800]]

- **arXiv**: [2607.09008](https://arxiv.org/abs/2607.09008)
- **PDF**: https://arxiv.org/pdf/2607.09008
- **详细分析**: [[20_Research/Papers/大模型/C-GAP_Class-Aware_and_Online_Prompting_Improves_Vision-Language_Models_on_Imbalanced_Classes|C-GAP: Class-Aware and Online Prompting Improves Vision-Language Models on Imbalanced Classes]]
- **作者**: Francis Fernandez, Arash Jahangiri, Salimeh Sekeh
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《C-GAP: Class-Aware and Online Prompting Improves Vision-Language Models on Imbalanced Classes》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety-critical perception systems must reliably detect rare object classes within small label spaces, a setting that long-tailed detection methods, designed for hundreds of classes with dense annotation, fundamentally do not address. Open-vocabulary detectors offer a promising alternative, as they use natural language queries at inference time, making prompt quality a first-class lever for detection performance. We exploit this property to address class imbalance: rather than retraining models or collecting additional annotations, we ask whether iteratively refining the language prompts, fed to frozen detectors, can improve minority class detection. We introduce C-GAP Caption-Guided Augmentation and Prompting), a detector-agnostic, annotation-free framework that operates in two phases. First, we establish a composite caption baseline combining per-image scene descriptions with class-quantity context, which we show outperforms scene-description only or class-quantity-only prompts across multiple open-vocabulary architectures and benchmarks. Second, an LLM iteratively refines each image's caption individually, with trials triaged into accept, tentative, or regenerate buckets based on minority-class AP@0.5 against a dynamic threshold derived from the composite baseline. Refinement terminates early once sufficient AP@0.5 gain is achieved. No detector weights are updated at any stage. Our experiments shows that C-GAP improves minority-class average precision up to 53% over the baselines. On COCO, C-GAP improves minority-class AP@0.5 by ~81% relative over the composite baseline (17.69 -&gt; 32.09). Experiments confirm that composite captions provide the critical foundation for effective refinement: using scene-description-only or class-quantity-only prompts as the refinement starting point yields diminishing returns, supporting both stages of C-GAP as necessary contributions.

</details>

---

### [[20_Research/Papers/机器人/SplatCtrl_Perception-Action_Coupling_via_Gaussian_Scene_Representations_and_Reactive_Robot_Control|SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control]]

![[assets/2607.08948_figure.png|800]]

- **arXiv**: [2607.08948](https://arxiv.org/abs/2607.08948)
- **PDF**: https://arxiv.org/pdf/2607.08948
- **详细分析**: [[20_Research/Papers/机器人/SplatCtrl_Perception-Action_Coupling_via_Gaussian_Scene_Representations_and_Reactive_Robot_Control|SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control]]
- **作者**: Siddarth Jain, Ho Jin Choi
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《SplatCtrl: Perception-Action Coupling via Gaussian Scene Representations and Reactive Robot Control》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MERL, Real2Sim, SplatSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulators excel in structured environments but face substantial challenges in unstructured and dynamic settings. This paper presents SplatCtrl, a unified framework for real-time scene reconstruction and reactive robot motion generation to enable collision-free robotic arm control in previously unseen and continuously changing environments. Building on 3D Gaussian Splatting (3D-GS), we introduce a hybrid voxel-based filtering and dynamic Gaussian relocation strategy that supports efficient scene reconstruction from RGB-D streams while accommodating environmental changes. For safe and reactive control, we further propose a method for deriving continuous signed distance functions from isotropic Gaussians, providing stable and differentiable collision probability estimates that bridge classical distance fields with the modern implicit representation. These continuous distance metrics are incorporated into control barrier functions, resulting in a unified perception-action coupling framework that supports smooth and reliable real-time motion generation in response to scene changes. Experimental validation in simulation, on physical robot, and within shared human-robot workspace demonstrates the framework's effectiveness, achieving integrated scene reconstruction and reactive control in uncertain, and dynamic environments.

</details>

---

### [[20_Research/Papers/大模型/Mixture_of_Probes_Learning_from_Privileged_Modalities_in_Multimodal_LLMs_Through_Probing|Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing]]

![[assets/2607.08839_figure.png|800]]

- **arXiv**: [2607.08839](https://arxiv.org/abs/2607.08839)
- **PDF**: https://arxiv.org/pdf/2607.08839
- **详细分析**: [[20_Research/Papers/大模型/Mixture_of_Probes_Learning_from_Privileged_Modalities_in_Multimodal_LLMs_Through_Probing|Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing]]
- **作者**: Dominick Reilly, Qiyu Wu, Hiromi Wakaki, Srijan Das, Yuki Mistufuji
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Mixture of Probes: Learning from Privileged Modalities in Multimodal LLMs Through Probing》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal Large Language Models (MLLMs) are typically designed under the assumption that all modalities available during training will also be accessible at inference. However, many real-world settings violate this assumption, requiring models to operate under a privileged modality setting, where auxiliary modalities are available only during training. While these modalities contain valuable information, existing MLLMs largely fail to leverage them effectively, as they treat modalities as interchangeable inputs rather than sources of complementary supervision. We propose Mixture of Probes (MoP), a novel framework that disentangles modality-specific and modality-general signals within the MLLM, allowing the model to preserve modality-dependent structure while learning transferable representations across modalities. At its core, MoP achieves this through a structured probing mechanism that extracts and organizes information from intermediate representations of a shared modality encoder, rather than relying only on final-layer alignment as done in existing MLLMs. To support this disentanglement, we further introduce MoP Cross-modal Training (MoP-X), a training strategy for MoP centered around a probe disentanglement loss that prevents probe collapse and encourages cross-modal learning. We evaluate MoP across two domains spanning eight tasks and four modalities under a comprehensive evaluation protocol tailored to the privileged modality setting, where each modality is independently treated as the sole input at inference time. MoP consistently outperforms strong MLLM baselines, achieving up to 65% relative improvement, demonstrating that auxiliary modalities, even when unavailable at inference, can provide substantial gains when effectively leveraged during training. Code, model checkpoints, and evaluation protocols will be made available at https://github.com/Sony/MoP.

</details>

---

### [[20_Research/Papers/大模型/GReFEM_Multimodal_LLMs_as_Zero-Shot_Semantic_Assistants_for_Physics-Guided_3D_Mesh_Refinement|GReFEM: Multimodal LLMs as Zero-Shot Semantic Assistants for Physics-Guided 3D Mesh Refinement]]

![[assets/2607.08798_figure.png|800]]

- **arXiv**: [2607.08798](https://arxiv.org/abs/2607.08798)
- **PDF**: https://arxiv.org/pdf/2607.08798
- **详细分析**: [[20_Research/Papers/大模型/GReFEM_Multimodal_LLMs_as_Zero-Shot_Semantic_Assistants_for_Physics-Guided_3D_Mesh_Refinement|GReFEM: Multimodal LLMs as Zero-Shot Semantic Assistants for Physics-Guided 3D Mesh Refinement]]
- **作者**: Kartik Bali, Mahish K. Guru, Christian J Cyron, Roland Aydin
- **cs 子类**: cs.CV, cs.GR
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《GReFEM: Multimodal LLMs as Zero-Shot Semantic Assistants for Physics-Guided 3D Mesh Refinement》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adaptive volumetric finite element meshing is a critical step in computer-aided engineering and analysis that dictates the computational budget of a given problem. It traditionally requires iterative PDE solvers or heavily supervised, data-driven surrogates trained on large-scale simulation data. While Multimodal Large Language Models (MLLMs) excel in 2D visual tasks, their zero-shot capability to semantically ground regions based on geometric understanding and physics remains an open question. Overall, this study explores a significant question: can the high-level semantic understanding of off-the-shelf MLLMs serve as a viable, zero-shot geometric proxy for finite element mesh refinement? To investigate this, we introduce GReFEM (Geometric Reasoning Enhanced Multimodal LLMs for Finite Element Meshing), a framework that utilizes MLLMs to visually localize stress-critical regions based on physics-guided textual prompts. To bridge the gap between 2D MLLM pre-training and 3D geometries, we introduce orthoViews, a view-selection module that maximizes the observability of key geometric features. We conduct an in-depth empirical evaluation across diverse CAD geometries, loading cases, and SOTA MLLMs, comparing them against a tuned geometric heuristic under a strict, matched refinement budget. Our findings reveal that MLLMs demonstrate robust zero-shot capacity to accurately follow complex spatial-physical instructions, isolating stress-relevant features with higher precision than blind heuristics. By mapping both the successes and current limitations of MLLMs in physical grounding, this study defines the frontier of foundation models as semantic assistants in automated simulation workflows.

</details>

---
