# cs.CV | Computer Vision and Pattern Recognition | 2026-06-19

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/强化学习/Current_World_Models_Lack_a_Persistent_State_Core|Current World Models Lack a Persistent State Core]]

![[assets/2606.20545_figure.png|800]]

- **arXiv**: [2606.20545](https://arxiv.org/abs/2606.20545)
- **PDF**: https://arxiv.org/pdf/2606.20545
- **详细分析**: [[20_Research/Papers/强化学习/Current_World_Models_Lack_a_Persistent_State_Core|Current World Models Lack a Persistent State Core]]
- **作者**: Jinpeng Lu, Dexu Zhu, Haoyuan Shi, Linghan Cai, Guo Tang, Yinda Chen, Jie Cao, Duyu Tang, Yi Zhang, Yong Dai, Xiaozhu Ju
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: RL, WorldModel

#### 研究背景与动机

《Current World Models Lack a Persistent State Core》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ChronoMagic-Bench, Lingbot-World, LiveBench, LiveWorld, MBench, PhyGenBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models are increasingly regarded as a decisive step toward artificial general intelligence, yet modeling the physical world demands more than rendering convincing frames on demand: it requires an internal world state that keeps evolving over time, decoupled from observation, so that objects endure and events run to their conclusions whether or not a camera is watching, much as the moon holds to its orbit when no one is looking. This requirement is a blind spot of existing benchmarks, which reward surface properties such as fidelity, motion, and camera controllability while never asking whether a generated world keeps evolving once it is unobserved. We introduce \textbf{WRBench}, the first systematic diagnostic benchmark that treats camera motion as an intervention on observability and resolves evaluation into a human-calibrated chain that asks whether the camera executes the requested interaction, whether the scene stays continuous and identifiable while in view, and whether a returning target remains consistent with the event that was set in motion. Across 9{,}600 videos from 23 models spanning four control paradigms, one finding proves stubborn: current systems maintain the observed world as a tracking shot, resuming a returning target in the state at which it was abandoned rather than advancing the event while it went unseen. Because this failure recurs across control paradigms, model families, and increments of scale, robust world-state evolution does not follow from cleaner imagery, tighter control, richer geometric priors, or sheer parameter count We therefore argue that the stability of the physical state kernel and the consistency of worldlines under viewpoint intervention should become first-class objectives of world-model design, so that a world model captures how the world will unfold rather than how the next frame appears.

</details>

---

### [[20_Research/Papers/具身智能/HumanScale_Egocentric_Human_Video_Can_Outperform_Real-Robot_Data_for_Embodied_Pretraining|HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining]]

![[assets/2606.20521_first_page.png|800]]

- **arXiv**: [2606.20521](https://arxiv.org/abs/2606.20521)
- **PDF**: https://arxiv.org/pdf/2606.20521
- **详细分析**: [[20_Research/Papers/具身智能/HumanScale_Egocentric_Human_Video_Can_Outperform_Real-Robot_Data_for_Embodied_Pretraining|HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining]]
- **作者**: Juncheng Ma, Jianxin Bi, Yufan Deng, Xuanran Zhai, Kewei Zhang, Ye Huang, Bo Liang, Shukai Gong, Jiankai Tu, Xiaotian Tang, Jiaxin Li, Kaiqi Chen...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.2，机器人 0.8）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《HumanScale: Egocentric Human Video Can Outperform Real-Robot Data for Embodied Pretraining》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied foundation models are expected to benefit from data scaling like large language models, but face a much tighter data bottleneck. Teleoperated real-robot trajectories remain the dominant pretraining source due to their precise action supervision and embodiment alignment, yet their scalability is limited by high collection cost, acquisition difficulty, and low behavioral and environmental diversity. These limitations have sparked interest in egocentric human video as a scalable, substantially lower-cost, and more diverse alternative for embodied model pretraining. However, its effectiveness compared to teleoperated real-robot data remains underexplored. To address this question, we conduct a systematic study comparing egocentric human video and teleoperated real-robot trajectories as pretraining data sources for embodied foundation models, under fixed post-training and validation protocols. Surprisingly, we find that egocentric data, when processed through a carefully designed filtering and labeling pipeline, is not merely a viable substitute for model pretraining but can lead to superior performance. With the same amount of pretraining data, models pretrained on egocentric data achieve a 24% lower validation loss on real-robot action prediction, as well as 52.5% and 90% higher success rates on in-distribution and out-of-distribution real-robot task execution, respectively. This finding verifies a scalable paradigm for embodied foundation models: pretrain on egocentric human video to learn diverse world representations, then adapt with a small amount of labeled real-robot data for action-space alignment. We hope this study encourages broader exploration of egocentric data and offers guidance for data quality assessment before costly robot data collection.

</details>

---

### [[20_Research/Papers/具身智能/Fast_Human_Attention_Prediction_for_Fixation-guided_Active_Perception_in_Autonomous_Navigation|Fast Human Attention Prediction for Fixation-guided Active Perception in Autonomous Navigation]]

![[assets/2606.20491_figure.png|800]]

- **arXiv**: [2606.20491](https://arxiv.org/abs/2606.20491)
- **PDF**: https://arxiv.org/pdf/2606.20491
- **详细分析**: [[20_Research/Papers/具身智能/Fast_Human_Attention_Prediction_for_Fixation-guided_Active_Perception_in_Autonomous_Navigation|Fast Human Attention Prediction for Fixation-guided Active Perception in Autonomous Navigation]]
- **作者**: Fatma Youssef Mohammed, Grzegorz Malczyk, Kostas Alexis
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.0（加权：具身智能 0.3，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Fast Human Attention Prediction for Fixation-guided Active Perception in Autonomous Navigation》归入 机器人、具身智能、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human visual attention relies on structured scanpaths to efficiently process scenes, yet instilling this behavior into robot autonomy is in its infancy and hindered by the high,computational costs of existing predictive models. To address this, we introduce GazeLNN, a computationally lightweight,scanpath prediction model that leverages Liquid Neural Networks as its recurrent engine and employs MobileNetV3 for feature extraction. Operating auto-regressively, the architecture predicts sequential fixation heatmaps conditioned on the current visual stimulus and fixation history. Despite requiring only 0.61 GFLOPs, GazeLNN achieves state-of-the-art performance on the MIT Low Resolution dataset achieving 0.47 ScanMatch score. It outperforms existing recurrent baselines across diverse evaluation metrics, while reducing computational costs by 99.40% and accelerating inference by up to six times. To investigate the role of human attention modeling in robot autonomy and demonstrate the practical utility of this highly efficient architecture, we integrate GazeLNN into an active camera-robot control policy trained via Reinforcement Learning. This integration enables human-fixation-guided perception during autonomous navigation, validated through successful real-world deployments on an aerial robot.

</details>

---

### [[20_Research/Papers/具身智能/Efficiently_Linking_Real_Scenes_with_Synthetic_Data_Generation_for_AI-based_Cognitive_Robotics_and_Computer_Vision_Applications|Efficiently Linking Real Scenes with Synthetic Data Generation for AI-based Cognitive Robotics and Computer Vision Applications]]

![[assets/2606.20272_figure.png|800]]

- **arXiv**: [2606.20272](https://arxiv.org/abs/2606.20272)
- **PDF**: https://arxiv.org/pdf/2606.20272
- **详细分析**: [[20_Research/Papers/具身智能/Efficiently_Linking_Real_Scenes_with_Synthetic_Data_Generation_for_AI-based_Cognitive_Robotics_and_Computer_Vision_Applications|Efficiently Linking Real Scenes with Synthetic Data Generation for AI-based Cognitive Robotics and Computer Vision Applications]]
- **作者**: Paul Koch, Vivek Chavan, André Sers, Adem Karakurt, Paul Hofmann, Mohamad Zaher Ziadeh, Jörg Krüger
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Efficiently Linking Real Scenes with Synthetic Data Generation for AI-based Cognitive Robotics and Computer Vision Applications》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GraspNet, SuchtionNet, SuctionNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

AI vision models are a driving factor for the potential use case scenarios of cognitive robotics within in the industry and household applications. A large array of methods from semantic environment analysis towards 6D and grasping pose estimation have been proposed based on the latest AI achievements. However, such advancements require further strong and efficient methods w.r.t. training data and AI-architectures, which are capable in synergy to tackle current challenges, precision limits, and scalability beyond domain gaps. In this paper, we discuss these current limits and trends in the related state-of-the-art which are challenging those. Further we discuss our current work in progress on bridging the domain gap between simulations and real world applications by linking those in the training data generation.

</details>

---

### [[20_Research/Papers/具身智能/EventVLA_Event-Driven_Visual_Evidence_Memory_for_Long-Horizon_Vision-Language-Action_Policies|EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies]]

![[assets/2606.20092_figure.png|800]]

- **arXiv**: [2606.20092](https://arxiv.org/abs/2606.20092)
- **PDF**: https://arxiv.org/pdf/2606.20092
- **详细分析**: [[20_Research/Papers/具身智能/EventVLA_Event-Driven_Visual_Evidence_Memory_for_Long-Horizon_Vision-Language-Action_Policies|EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies]]
- **作者**: Ganlin Yang, Zhangzheng Tu, Yuqiang Yang, Sitong Mao, Junyi Dong, Tianxing Chen, Jiaqi Peng, Jing Xiong, Jiafei Cao, Jifeng Dai, Wengang Zhou, Yao Mu...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.8，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《EventVLA: Event-Driven Visual Evidence Memory for Long-Horizon Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EventVLA, RMBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory remains a critical bottleneck for long-horizon robotic manipulation, as standard Vision-Language-Action (VLA) policies often fail when task-relevant cues become occluded or unobservable over time. While existing memory-augmented methods utilize historical context, they either suffer from severe information bottlenecks, incur high latency via decoupled dual systems, or rely on unselective buffers that accumulate massive visual redundancies. To address these limitations, we introduce EventVLA, an end-to-end framework founded on the concept of sparse visual evidence memory that comprises two core components: foundational visual anchors to retain initial and short-term contexts, and a dynamic Keyframe Evidence Memory (KEM) module. Specifically, KEM directly predicts future keyframe probabilities from the VLA's latent embeddings to autonomously capture and store sparse, task-critical visual events. This foresight-driven mechanism empowers the policy to dynamically evaluate the future causal utility of current observations, preserving transient visual evidence before it becomes unobservable. Furthermore, we propose RoboTwin-MeM, a diagnostic benchmark specifically designed to evaluate non-Markovian manipulation tasks with interactive visual evidence. Extensive evaluations show that across 17 memory-requiring simulation tasks and 4 real-world bimanual tasks, EventVLA achieves an average success rate improvement of +40% over state-of-the-art memory-augmented VLAs.

</details>

---

### [[20_Research/Papers/世界模型/Holo-World_Unified_Camera,_Object_and_Weather_Control_for_Video_World_Model|Holo-World: Unified Camera, Object and Weather Control for Video World Model]]

![[assets/2606.20083_first_page.png|800]]

- **arXiv**: [2606.20083](https://arxiv.org/abs/2606.20083)
- **PDF**: https://arxiv.org/pdf/2606.20083
- **详细分析**: [[20_Research/Papers/世界模型/Holo-World_Unified_Camera,_Object_and_Weather_Control_for_Video_World_Model|Holo-World: Unified Camera, Object and Weather Control for Video World Model]]
- **作者**: Xiangchen Yin, Wenzhang Sun, Jiahui Yuan, Zijie Liu, Yinda Chen, Wei Li, Dachun Kai, Chunfeng Wang, Xiaoyan Sun
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Holo-World: Unified Camera, Object and Weather Control for Video World Model》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Holo-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video world models are moving toward preserving an observed world under controllable camera and object motion while allowing its environmental state to change. Yet these controls remain isolated, and weather generation typically relies on a source video or reconstructed scene that already specifies future structure. We study a first-frame-anchored source-to-state setting, where the model starts from a single image and follows explicit camera and object controls and an optional weather instruction, then generates a video that either preserves the source world or transfers it to a target weather state. To address these challenges, we first build HoloStateData, a state video dataset that turns diverse videos into unified control samples for camera, object, and weather supervision. Second, we introduce Holo-World, a unified controllable video world model that jointly controls scene from a single image. Its Unified Scene Adapter factorizes world preservation and weather transfer into distinct parameter subspaces, using rendered background, geometry buffers, and object controls to maintain controlled scene structure while modeling weather-dependent appearance and particle effects. Additionally, Scene-Weather Decomposed CFG guides scene and weather residuals separately, strengthening target weather effects without over-amplifying the full condition. Quantitative and qualitative experiments demonstrate that Holo-World maintains precise camera and object control with consistent scene structure while transferring scenes into diverse target weather state, outperforming video-to-video weather editing baselines on weather-state generation. Our project page is available at \url{https://xiangchenyin.github.io/Holo-World/}.

</details>

---

### [[20_Research/Papers/机器人/MMD-SLAM_Structure-Enhanced_Multi-Meta_Gaussian_Distribution-Guided_Visual_SLAM|MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM]]

![[assets/2606.19874_figure.png|800]]

- **arXiv**: [2606.19874](https://arxiv.org/abs/2606.19874)
- **PDF**: https://arxiv.org/pdf/2606.19874
- **详细分析**: [[20_Research/Papers/机器人/MMD-SLAM_Structure-Enhanced_Multi-Meta_Gaussian_Distribution-Guided_Visual_SLAM|MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM]]
- **作者**: Fan Zhu, Ziyu Chen, Peichen Liu, Yifan Zhao, Zhisong Xu, Hui Zhu, Hongxing Zhou, Sixun Liu, Chunmao Jiang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《MMD-SLAM: Structure-Enhanced Multi-Meta Gaussian Distribution-Guided Visual SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

3D Gaussian Splatting (3DGS) has significantly boosted novel view synthesis and high-fidelity scene reconstruction, expanding the potential of 3DGS-based Visual Simultaneous Localization and Mapping (SLAM) methods. However, most existing systems fail to fully exploit the underlying structural information, which limits rendering quality and often leads to inconsistent maps. To address these limitations, we propose MMD-SLAM, a structure-enhanced Visual SLAM framework that leverages the Atlanta World (AW) assumption to guide a Multi-Meta Gaussian representation for photorealistic mapping. First, we introduce a point-line fusion strategy for pose optimization, where 3D line segments are incorporated to improve tracking robustness and provide additional constraints for mapping. Second, we design a Multi-Meta Gaussian representation with dominant directions, explicitly encoding structural priors from the AW hypothesis. Finally, we propose a Gaussian evolution strategy that adapts to scene geometry and incorporates structural cues into global optimization. Extensive experiments demonstrate that these innovations enable MMD-SLAM to achieve state-of-the-art performance in both tracking accuracy and mapping quality. e.g., our method achieves a 48.56% reduction in ATE RMSE on ScanNet and a 5.71% improvement in PSNR on Replica, compared with MonoGS.

</details>

---

### [[20_Research/Papers/具身智能/Occ-VLM_Occupancy_Grounded_Vision_Language_Model_for_Indoor_Scene_Understanding|Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding]]

![[assets/2606.19776_figure.png|800]]

- **arXiv**: [2606.19776](https://arxiv.org/abs/2606.19776)
- **PDF**: https://arxiv.org/pdf/2606.19776
- **详细分析**: [[20_Research/Papers/具身智能/Occ-VLM_Occupancy_Grounded_Vision_Language_Model_for_Indoor_Scene_Understanding|Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding]]
- **作者**: Jianing Li, Zhou Fang, Yijiang Liu, Li Du
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 1，机器人 0.2）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Occ-VLM: Occupancy Grounded Vision Language Model for Indoor Scene Understanding》归入 大模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, vision-language models (VLMs) have made significant progress in 3D scene understanding, driving advances in applications such as embodied intelligence and robotic vision. However, existing approaches typically either rely directly on explicit 3D inputs (e.g., point clouds or RGB-D sequences), or introduce an additional 3D geometry encoder to derive 3D-aware visual tokens from 2D images. Such designs structurally decouple 3D geometric perception from the rich 2D semantics learned via vision-language pre-training, hindering the development of a unified 3D vision-language representation. In this work, we propose Occ-VLM, a novel framework for 3D scene understanding that operates purely on posed RGB images and employs a single 2D vision encoder. Specifically, Occ-VLM reconstructs 3D scene occupancy as an auxiliary geometric prior, which is utilized to spatially associate foreground 2D tokens with 3D space. These tokens are then decoded by a Large Language Model (LLM) for unified scene understanding. Extensive experiments demonstrate that Occ-VLM achieves both accurate geometric perception and robust vision-language reasoning: it attains state-of-the-art performance on multi-view occupancy prediction, while performing on par with 3D-input VLMs on 3D Visual Question Answering (VQA) and 3D dense captioning benchmarks.

</details>

---

### [[20_Research/Papers/强化学习/Scaling_Self-Play_for_End-to-End_Driving|Scaling Self-Play for End-to-End Driving]]

![[assets/2606.19641_figure.png|800]]

- **arXiv**: [2606.19641](https://arxiv.org/abs/2606.19641)
- **PDF**: https://arxiv.org/pdf/2606.19641
- **详细分析**: [[20_Research/Papers/强化学习/Scaling_Self-Play_for_End-to-End_Driving|Scaling Self-Play for End-to-End Driving]]
- **作者**: Luke Rowe, Roger Girgis, Rodrigue de Schaetzen, Daphne Cornelisse, Alaap Grandhi, Felix Heide, Eugene Vinitsky, Christopher Pal, Liam Paull
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, RL, Systems

#### 研究背景与动机

《Scaling Self-Play for End-to-End Driving》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end autonomous driving models are typically trained on offline human-demonstration datasets that provide limited state coverage and often no closed-loop feedback, making them prone to compounding errors when deployed in closed-loop and brittle to long-tail agent interactions. To overcome these limitations, we propose an alternative strategy for training end-to-end driving models: large-scale self-play directly from pixels in simulation. While prior self-play approaches have shown promising transfer to real-world driving, they typically assume vectorized Bird's-Eye-View (BEV) observations that are incompatible with end-to-end policies operating directly on sensor observations. To this end, we introduce Gigapixel, a high-throughput batched driving simulator with perspective rendering, enabling scalable self-play directly from pixel observations. Rather than targeting compute-costly photorealistic sensor simulation, Gigapixel renders a simplified bounding-box world that preserves essential scene structure while achieving throughput at 50k agent steps per second. Since direct pixel-space self-play RL is prohibitively sample-inefficient at end-to-end model scale, we propose self-play DAgger training: we train pixel-based policies in self-play via on-policy distillation from a privileged RL teacher. To bridge the sim-to-real gap, we subsequently transfer the self-play trained policies to real-world sensor data through lightweight perception adaptation. Policies trained in Gigapixel and adapted to real-world sensor data achieve competitive performance on the HUGSIM and NAVSIM-v2 benchmarks without human trajectory supervision. Moreover, scaling self-play training yields proportional gains in policy performance, establishing self-play as a practical and scalable strategy for training end-to-end models.

</details>

---

### [[20_Research/Papers/具身智能/Mix-QVLA_Task-Evidence-Aware_Mixed-Precision_Quantization_of_Vision-Language-Action_Models|Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models]]

![[assets/2606.19565_figure.png|800]]

- **arXiv**: [2606.19565](https://arxiv.org/abs/2606.19565)
- **PDF**: https://arxiv.org/pdf/2606.19565
- **详细分析**: [[20_Research/Papers/具身智能/Mix-QVLA_Task-Evidence-Aware_Mixed-Precision_Quantization_of_Vision-Language-Action_Models|Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models]]
- **作者**: Navin Ranjan, Andreas Savakis
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: Multimodal

#### 研究背景与动机

《Mix-QVLA: Task-Evidence-Aware Mixed-Precision Quantization of Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CEED-VLA, DyQ-VLA, EaqVLA, EfficientVLA, Mix-QVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose Mix-QVLA, a task-evidence-aware mixed-precision PTQ framework for VLA models. Mix-QVLA anchors each quantized variant to the full-precision action-token reference decision and evaluates whether quantization preserves task-relevant evidence across key VLA functional boundaries. It computes normalized gradient-weighted task-evidence maps from boundary activations and compares full-precision and quantized maps using evidence-mass and attribution-distribution distortion, capturing changes in both the strength and allocation of decision-supporting evidence. A soft-bottleneck objective aggregates boundary-level degradation into layer-wise sensitivity scores. Mix-QVLA further models sensitivity throughout task execution, capturing phase-dependent shifts in layer importance rather than assuming a fixed sensitivity profile. The resulting evidence- and time-aware scores guide mixed-precision bit allocation under model-size and BitOps budgets. Extensive evaluations on OpenVLA-style policies show that Mix-QVLA improves the accuracy-efficiency trade-off of low-bit VLA deployment. On LIBERO, Mix-QVLA reduces OpenVLA-OFT memory from 15.4 GB to 4.1 GB, retains 96.3 average success compared with 97.1 for the BF16 model, and achieves a 1.52x inference speedup.

</details>

---

### [[20_Research/Papers/具身智能/ImageWAM_Do_World_Action_Models_Really_Need_Video_Generation,_or_Just_Image_Editing|ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?]]

![[assets/2606.19531_figure.png|800]]

- **arXiv**: [2606.19531](https://arxiv.org/abs/2606.19531)
- **PDF**: https://arxiv.org/pdf/2606.19531
- **详细分析**: [[20_Research/Papers/具身智能/ImageWAM_Do_World_Action_Models_Really_Need_Video_Generation,_or_Just_Image_Editing|ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?]]
- **作者**: Yuyang Zhang, Wenyao Zhang, Zekun Qi, He Zhang, Haitao Lin, Jingbo Zhang, Yao Mu, Xiaokang Yang, Wenjun Zeng, Xin Jin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ImageWAM: Do World Action Models Really Need Video Generation, or Just Image Editing?》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) commonly rely on video generation to bridge visual world modeling and robot control. However, video-based WAMs face three coupled limitations: dense multi-frame future tokens make inference costly, full video prediction spends capacity on action-irrelevant temporal and appearance details, and long-horizon future imagination may introduce errors that mislead action prediction. These issues raise a simple question: Does world action model really need video generation? We propose ImageWAM, a simple WAM framework that repurposes pretrained image editing models for robot action prediction. In contrast to video generation, image editing provides a better-matched prior: it only needs to model a target-frame transformation, focuses on action-relevant current-to-target visual differences, and grounds task instructions to localized visual changes through edit pretraining. In practice, ImageWAM does not decode the target frame at inference time; instead, it conditions a flow-matching action expert on the KV caches produced by image-editing denoising, using them as a compact world-action context. ImageWAM outperforms standard VLA baselines and matching competitive WAMs without additional policy pretraining across different simulator and real-world experiments. It also reduces FLOPs to 1/6 and latency to 1/4 of video-based WAMs. Attention analysis further shows that editing caches focus on task-relevant change regions, supporting image editing as an effective alternative to video-based world-action modeling.

</details>

---

### [[20_Research/Papers/具身智能/3D-DLP_Self-Supervised_3D_Object-Centric_Scene_Representation_Learning|3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning]]

![[assets/2606.19451_figure.png|800]]

- **arXiv**: [2606.19451](https://arxiv.org/abs/2606.19451)
- **PDF**: https://arxiv.org/pdf/2606.19451
- **详细分析**: [[20_Research/Papers/具身智能/3D-DLP_Self-Supervised_3D_Object-Centric_Scene_Representation_Learning|3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning]]
- **作者**: Ellina Zhang, Madhaven Iyengar, Amir Zadeh, Chuan Li, Deepak Pathak, David Held, Tal Daniel
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《3D-DLP: Self-Supervised 3D Object-Centric Scene Representation Learning》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce 3D-DLP, a self-supervised object-centric representation learning model that decomposes scene-level RGB-D or voxel observations into a set of 3D latent particles. Building on the Deep Latent Particles (DLP) framework, each particle encodes disentangled attributes, including 3D keypoint position, bounding box dimensions, and appearance features, and represents a distinct entity in the scene. The model learns interpretable per-particle segmentation maps through an end-to-end self-supervised reconstruction objective. We demonstrate on both simulated and real-world datasets that the learned latent space is interpretable and controllable: by manipulating particle positions and decoding, we can generate novel scene configurations. Furthermore, we show that leveraging these compact 3D latent particles for downstream robotic manipulation improves performance over baselines that either lack explicit 3D information or rely on memory-intensive dense 3D inputs without object-centric structure. Code and videos are available at https://eubooks3003.github.io/3d-dlp.

</details>

---
