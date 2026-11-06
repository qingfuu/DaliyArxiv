# cs.CV | Computer Vision and Pattern Recognition | 2026-11-04

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Route_Anything_A_Study_of_Model_and_Policy_Routing_for_General-Purpose_AI_Systems|Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems]]

![[assets/2611.05275_first_page.png|800]]

- **arXiv**: [2611.05275](https://arxiv.org/abs/2611.05275)
- **PDF**: https://arxiv.org/pdf/2611.05275
- **详细分析**: [[20_Research/Papers/具身智能/Route_Anything_A_Study_of_Model_and_Policy_Routing_for_General-Purpose_AI_Systems|Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems]]
- **作者**: Pengfei Zhou, Yixing Ma, Hexin Wang, Weidong Tang, Zhenglin Wan, Wangbo Zhao, Yang You
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.1，机器人 0.4）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Route Anything: A Study of Model and Policy Routing for General-Purpose AI Systems》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CodeRouterBench, Qwen-Image-Bench, RouterBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial general intelligence (AGI) requires a method that can understand, generate, reason, and act across diverse domains and modalities. Rather than relying on a single model to master every capability, a promising path toward AGI now is to orchestrate a heterogeneous ecosystem of specialized models, tools, and policies (candidates) into a unified AI system. At the heart of this vision lies a fundamental question: how can an AI system dynamically select and coordinate the most capable candidate for each task while balancing performance and computational cost? In this work, we present Route Anything, a unified framework for studying model and policy routing across general-purpose AI systems. We develop a unified theoretical foundation that characterizes optimal routing under quality--cost trade-offs and establishes how the information available to a router determines its attainable performance. To systematically investigate routing across diverse capabilities, we first construct an omni-modal trajectory matrix spanning 25 benchmarks across language understanding, image, video, and speech generation, coding and workplace agents, and robotic manipulation, comprising 374,401 scored runs from 452 candidate configurations. Building on this framework, we train and test different routers to investigate the potential of omni-modal model routing, the capabilities of learned routers, and the conditions under which routing improves efficiency. Our results reveal substantial opportunities for capability orchestration: per-input oracle routing outperforms the best fixed candidate by 5.4 points, and learned routers outperform it by 0.3 points across 16 benchmarks, by 2.1 points on video generation, and by 1.1 points on robot manipulation while using 24% less policy time. More importantly, routing raises efficiency by 8.82x on average compared with the reference model.

</details>

---

### [[20_Research/Papers/机器人/High-fidelity_training-free_photovoltaic_module_mapping_from_multi-view_UAV_imagery|High-fidelity training-free photovoltaic module mapping from multi-view UAV imagery]]

![[assets/2611.05131_figure.png|800]]

- **arXiv**: [2611.05131](https://arxiv.org/abs/2611.05131)
- **PDF**: https://arxiv.org/pdf/2611.05131
- **详细分析**: [[20_Research/Papers/机器人/High-fidelity_training-free_photovoltaic_module_mapping_from_multi-view_UAV_imagery|High-fidelity training-free photovoltaic module mapping from multi-view UAV imagery]]
- **作者**: WenHao Duana, Qi Chena, Penglei Zhang, Ruizhe Deng, Zhiling Guo, Haoran Zhang, Yuntian Chen
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《High-fidelity training-free photovoltaic module mapping from multi-view UAV imagery》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-fidelity photovoltaic (PV) module mapping requires complete instance recovery and accurate delineation. Vision foundation models offer zero-shot segmentation, but converting incomplete and inconsistent predictions across views into a complete, geometrically accurate map of individual modules remains challenging. We propose the Multi-View PV Module Mapper (MV-PVMapper), a training-free framework coupling vision foundation models with unmanned aerial vehicle (UAV) photogrammetry. First, Segment Anything Model 3 (SAM 3) generates candidates from original images using text prompts. Their contours are then transferred into object space through per-module slope correction to limit distortion from surface-model noise, and verified against representative module dimensions to guide cross-view instance selection. Finally, accepted instances return to all covering images as box prompts for SAM~3, supplementing text prompts with spatial cues for iterative segmentation, verification and fusion. On five-direction surveys of three operational rooftop PV plants at approximately 1 cm nadir ground sampling distance, two feedback iterations recover 7,710 of 7,711 reference modules with no false positives at an intersection-over-union (IoU) matching threshold of 0.5. Macro-averaged area precision and recall reach 99.00 % and 98.52 %, respectively. Averaged across sites, the aggregated Jaccard index reaches 97.55 %, compared with 60.73 % and 41.24 % for orthomosaic segmentation and multi-view pixel-voting baselines, respectively; average precision at the stricter IoU threshold of 0.95 reaches 95.67 %. Ablation studies show that module-size constraints are critical for instance separation, while slope correction and feedback to all covering views improve boundary accuracy. These results are achieved without task-specific image annotation or segmentation-model weight updates.

</details>

---

### [[20_Research/Papers/机器人/Sparse_Anchors_for_Visual_Multi-Session_Registration_in_Changing_Environments|Sparse Anchors for Visual Multi-Session Registration in Changing Environments]]

![[assets/2611.05084_figure.png|800]]

- **arXiv**: [2611.05084](https://arxiv.org/abs/2611.05084)
- **PDF**: https://arxiv.org/pdf/2611.05084
- **详细分析**: [[20_Research/Papers/机器人/Sparse_Anchors_for_Visual_Multi-Session_Registration_in_Changing_Environments|Sparse Anchors for Visual Multi-Session Registration in Changing Environments]]
- **作者**: Yunus Talha Erzurumlu, Niklas Trekel, Saurabh Gupta, Nico Koltermann, Olga Vysotska, Jens Behley, Louis Wiesmann, Cyrill Stachniss
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Sparse Anchors for Visual Multi-Session Registration in Changing Environments》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Repeated robotic monitoring requires localization across visits to the same environment, even if the environment changes. Such changes can substantially reduce persistent visual content, and repetitive structures can lead to incorrect cross-session correspondences. In this paper, we address visual multi-session registration of a new data recording (the query session) to a previously reconstructed reference map. Under substantial visual and structural changes, cross-session localization may be possible only for parts of the trajectory. In our approach, we therefore rely on a sparse set of reliable absolute pose constraints and combine them with within-session relative-pose information to register the complete trajectory to the reference map. We first estimate absolute alignment hypotheses through visual place recognition, local feature matching, and geometric verification. We then use sequence consensus to reject hypotheses that are inconsistent with a common query-to-reference alignment and retain the remaining poses as absolute anchors. These anchors are refined through featuremetric alignment against a Gaussian feature field and combined with within-session relative-pose constraints in a robust pose-graph optimization. We evaluate our approach on 15 cross-session experiments from the challenging HILTI26 construction-site dataset, covering substantial scene changes and difficult-to-match environments. Our method achieves 94.4% recall within 1m and 100.0% within 5m, outperforming independent image localization, which peaks at 65.3% and 70.7%, respectively, as well as direct registration of independently reconstructed Structure-from-Motion geometry. Our results show that sparse, reliable absolute anchors can provide accurate and complete trajectory registration even when reliable cross-session correspondences are available only for part of the query session.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Where_to_Look_Observation_Policy_Optimization_for_Thinking_with_Images|Learning Where to Look: Observation Policy Optimization for Thinking with Images]]

![[assets/2611.04943_figure.png|800]]

- **arXiv**: [2611.04943](https://arxiv.org/abs/2611.04943)
- **PDF**: https://arxiv.org/pdf/2611.04943
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Where_to_Look_Observation_Policy_Optimization_for_Thinking_with_Images|Learning Where to Look: Observation Policy Optimization for Thinking with Images]]
- **作者**: Junfeng Wang, Jiawei Liu, Yongchao Xu, Tao Jiang, Jiangbo Ai, Jin Zhang, Chong Wang, Qixing Zhang
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 1.0（加权：强化学习 1）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Learning Where to Look: Observation Policy Optimization for Thinking with Images》归入 强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Complex visual question answering often requires vision-language models to think with images, i.e., actively acquire local visual evidence by zooming into informative regions of high-resolution images. Our error analysis shows that many failures in this setting originate from incorrect observation actions, where the model fails to localize key regions or obtain crops that contain sufficient evidence for answering. We further observe that bounding-box tokens exhibit substantially higher generation entropy than ordinary language tokens, indicating high uncertainty when the model decides where to look. However, existing reinforcement learning methods based on final-answer rewards provide only trajectory-level feedback, making it difficult to assign precise credit to the observation actions. We propose Observation Policy Optimization (OPO), an RL algorithm for optimizing observation actions in tool-augmented thinking with images. OPO consists of two core modules. First, Uncertainty-Guided Observation Branching (UOB) treats each image zoom-in tool call as an observation event and selectively branches at high-uncertainty, low-redundancy events during rollout, enabling efficient exploration of alternative cropping decisions and their resulting visual evidence. Second, Evidence-Localized Advantage Attribution (ELAA) compares sibling branches using local evidence-sufficiency rewards and assigns credit only to the corresponding observation-action tokens. By decoupling observation-action optimization from trajectory-level outcome supervision, OPO improves visual evidence acquisition and further enhances visual reasoning performance. Experiments show that OPO consistently improves Qwen3-VL models across scales and achieves competitive performance against larger models and tool-augmented baselines. Code is publicly available.

</details>

---

### [[20_Research/Papers/大模型/Behind_Video_Generation_Observations_and_Insights_on_Multimodal_Understanding_from_Kling|Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling]]

![[assets/2611.04916_figure.png|800]]

- **arXiv**: [2611.04916](https://arxiv.org/abs/2611.04916)
- **PDF**: https://arxiv.org/pdf/2611.04916
- **详细分析**: [[20_Research/Papers/大模型/Behind_Video_Generation_Observations_and_Insights_on_Multimodal_Understanding_from_Kling|Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling]]
- **作者**: Kling Team, Dong Chen, Jialu Chen, Xinlong Chen, Yifan Dai, Haotian Dong, Binzong Geng, Yushuo Guan, Minghui Guo, Guanlin He, Guanxiao He, Jingyun Hua...
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 强化学习
- **相关性评分**: 1.1（加权：大模型 0.7，强化学习 0.4）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Behind Video Generation: Observations and Insights on Multimodal Understanding from Kling》归入 大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generation has progressed from isolated clips to coherent short-form audiovisual sequences, and the bottleneck is shifting from rendering to semantic control. This report summarizes the observations and insights on multimodal understanding gained from successive generations of Kling. We argue that generation quality is the projection of multimodal understanding through the entire data--conditioning--alignment--evaluation chain, and we examine this chain module by module. Kling-MLLM, a shared multimodal foundation model that unifies image, video, audio, synchronized audio--video, and interleaved inputs, is specialized for each downstream module. Because a DiT is trained on far fewer training samples than a language model, we treat captioning as a semantic contract that maximizes description density, and extend it to reference-grounded captioning that makes reference bindings explicit. Prompt enhancement translates user intent into this caption distribution: basic PE is derived from captions of compelling videos and refined with text-level and generator-in-the-loop reinforcement learning, while agentic PE refines the story and retrieves compelling examples. We show that a reliable text encoder comes from perceptual training rather than from stronger language ability, and that candidates can be screened from text alone before end-to-end training. Reward modeling pairs a general reward model for explainable, localized critiques with a decision reward model for fast multidimensional scoring, treating perceptual bandwidth as a first-class design parameter. Finally, we review task-specific automatic evaluation, focusing on protocols that expose scoring shortcuts and help trace failures to their upstream source. We hope these lessons offer practical guidance for building the understanding stack behind controllable video generation.

</details>

---

### [[20_Research/Papers/具身智能/Trusting_Imagined_Futures_Auditing_Imagined_Rewards_for_VLA_Post-Training|Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training]]

![[assets/2611.04873_figure.png|800]]

- **arXiv**: [2611.04873](https://arxiv.org/abs/2611.04873)
- **PDF**: https://arxiv.org/pdf/2611.04873
- **详细分析**: [[20_Research/Papers/具身智能/Trusting_Imagined_Futures_Auditing_Imagined_Rewards_for_VLA_Post-Training|Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training]]
- **作者**: Zicheng Kong, Zhenbo Xu, Haoyan Zhang, Jinghan Yang, Zhenzhen Li, Yiwei Ru, Liuyu Xiang, WanTing Xu, Min Ren, Zhaofeng He
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 2.7（加权：具身智能 1.8，强化学习 0.2，世界模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Trusting Imagined Futures: Auditing Imagined Rewards for VLA Post-Training》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MeRL, OpenVLA, RIPT-VLA, VLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video world models enable candidate actions to be evaluated through imagined outcomes, but high predicted rewards can favor trajectories with poor execution quality. We introduce Trusting Imagined Futures (TIF), an offline supervision selection method for vision-language-action (VLA) post-training that audits predicted rewards using execution feedback. A multidimensional reward model predicts a utility score for candidate ranking and five dimensions of execution quality. An auditor uses reward predictions and uncertainty to identify overestimation patterns learned from paired imagined videos and real executions. TIF accepts the candidate with the highest predicted utility when its advantage over the existing trajectory exceeds a margin and its audit risk passes a threshold; otherwise, it retains the existing supervision. The retained real trajectories then supervise behavior cloning. Across four LIBERO suites and three training seeds, TIF achieves a mean success rate of 76.25%, improving over training on the existing trajectories by 3.00 percentage points with the same trajectory count and training budget. Adding audit gating yields 1.47 percentage points with the reward model and advantage margin held fixed. The gains persist against advantage ranking and logistic regression risk selection at matched replacement counts. On recorded videos from three real robot tasks, TIF increases clean completion among selected trajectories from 58.33% to 70.00% across 60 candidate pools.

</details>

---

### [[20_Research/Papers/大模型/Hybrid_Particle-Voxel_Dynamics_for_Multimodal_3D_World_Simulation|Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation]]

![[assets/2611.04492_first_page.png|800]]

- **arXiv**: [2611.04492](https://arxiv.org/abs/2611.04492)
- **PDF**: https://arxiv.org/pdf/2611.04492
- **详细分析**: [[20_Research/Papers/大模型/Hybrid_Particle-Voxel_Dynamics_for_Multimodal_3D_World_Simulation|Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation]]
- **作者**: Jimmy Wang, Yifan Chou, Kaifeng Zhang, Yixuan Wang, Binghao Huang, Tao Yu, Saleh Nabi, Yunzhu Li
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 大模型, 具身智能, 强化学习
- **相关性评分**: 2.12（加权：具身智能 0.3，大模型 0.4，强化学习 0.16，世界模型 0.76，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Hybrid Particle-Voxel Dynamics for Multimodal 3D World Simulation》归入 世界模型、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting how the world evolves in response to robot actions is central to policy learning, evaluation, and planning. However, many action-conditioned world models predict future observations in 2D image or video space without explicitly modeling the underlying 3D scene, making spatial consistency across viewpoints and over long-horizon interactions challenging. We introduce 3D World Simulator, an action-conditioned multimodal world modeling framework that jointly predicts appearance, geometry, and tactile observations from a unified 3D representation. Our approach combines a hybrid particle-voxel autoencoder that compresses point clouds into compact 3D voxel latents with an action-conditioned latent dynamics model that predicts their evolution. The shared 3D representation supports geometrically consistent rendering from arbitrary viewpoints and flexible integration of spatially aligned tactile signals. Our experiments demonstrate interactive, long-horizon, multimodal prediction at 50 Hz. We then show how our model enables scalable data generation for policy training and evaluation using tactile and multi-view visual observations, including wrist-mounted and novel camera views. Furthermore, we scale our method to large datasets containing diverse objects and demonstrate model-based planning with unseen objects and robot configurations. Together, these results highlight the potential of hybrid particle-voxel dynamics as a foundation for multimodal 3D world simulation.

</details>

---

### [[20_Research/Papers/具身智能/GVT3D_Gesture-Vision-Text_Token_Enrichment_for_3D_Embodied_Reference_Understanding|GVT3D: Gesture-Vision-Text Token Enrichment for 3D Embodied Reference Understanding]]

![[assets/2611.04422_figure.png|800]]

- **arXiv**: [2611.04422](https://arxiv.org/abs/2611.04422)
- **PDF**: https://arxiv.org/pdf/2611.04422
- **详细分析**: [[20_Research/Papers/具身智能/GVT3D_Gesture-Vision-Text_Token_Enrichment_for_3D_Embodied_Reference_Understanding|GVT3D: Gesture-Vision-Text Token Enrichment for 3D Embodied Reference Understanding]]
- **作者**: Vimarsh Shah, Dulanga Weerakoon, Ajinkya Deshpande, Saksham Agarwal, Nilesh Bhatia, Neel Kiran Naik, Parth Shah, Sravan Danda, Sanjay E. Sarma, Archan Misra, Vigneshwaran Subbaraju, Sougata Sen
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《GVT3D: Gesture-Vision-Text Token Enrichment for 3D Embodied Reference Understanding》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Natural human-robot interaction requires robots to interpret language and gestures within a 3D environment to support tasks such as pick-and-place and object retrieval. 3D Embodied Reference Understanding (3D-ERU) supports this by identifying the 3D location of a target object from a scene (point-cloud) containing a human pointing gesture and an accompanying language description. However, current 3D-ERU models lack alignment of cross-modal representations and incur high processing costs that increase with the point-cloud's size. To address this, we propose GVT3D, which employs an Embodied Fusion module that jointly models language, gesture, and vision inputs within a shared embedding space, promoting cross-modal alignment. We additionally introduce a foveation approach that selectively processes the point cloud within a coarse region around the estimated pointing direction to reduce computations. GVT3D achieves ~8% higher accuracy and foveation enables 2.95x faster execution while maintaining comparable accuracy, relative to prior 3D-ERU models.

</details>

---

### [[20_Research/Papers/具身智能/RAFT_Reasoning-Aligned_Fine-Tuning_Improves_Robustness_of_VLA_Post-Training|RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training]]

![[assets/2611.04368_figure.png|800]]

- **arXiv**: [2611.04368](https://arxiv.org/abs/2611.04368)
- **PDF**: https://arxiv.org/pdf/2611.04368
- **详细分析**: [[20_Research/Papers/具身智能/RAFT_Reasoning-Aligned_Fine-Tuning_Improves_Robustness_of_VLA_Post-Training|RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training]]
- **作者**: Shresth Grover, Andrey Kolobov, Dhruv Shah
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RAFT: Reasoning-Aligned Fine-Tuning Improves Robustness of VLA Post-Training》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adapting a generalist vision-language-action (VLA) policy to a target task with limited demonstrations can improve nominal task success while reducing robustness to variations in appearance, objects, and instructions. We introduce reasoning-aligned fine-tuning (RAFT), a two-stage post-training procedure: RAFT first trains low-rank adapters on task-relevant reasoning annotations, then freezes them while fine-tuning the policy on action demonstrations. On a physical DROID robot, RAFT achieves $75.0\%$ out-of-distribution success, compared with $27.9\%$ for plain fine-tuning; on a multi-stage bimanual YAM task, it reaches $70.0\%$ mean success, compared with $36.0\%$ for the strongest baseline. RAFT also improves success under visual, object, and instruction shifts in simulated pick-and-place and open-drawer tasks. Compared with plain fine-tuning, RAFT policies place more attention on annotated task regions and yield higher linear-probe accuracy for object identity in later layers. A broader reasoning-data mixture further improves downstream success across demonstration budgets.

</details>

---

### [[20_Research/Papers/具身智能/CoReMatch_Recurrent_Continuous_Coordinate_Refinement_for_Real-Time_Robotic_Feature_Matching|CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching]]

![[assets/2611.03932_figure.png|800]]

- **arXiv**: [2611.03932](https://arxiv.org/abs/2611.03932)
- **PDF**: https://arxiv.org/pdf/2611.03932
- **详细分析**: [[20_Research/Papers/具身智能/CoReMatch_Recurrent_Continuous_Coordinate_Refinement_for_Real-Time_Robotic_Feature_Matching|CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching]]
- **作者**: Robert J. Wang, Charles Ling, Boyu Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《CoReMatch: Recurrent Continuous Coordinate Refinement for Real-Time Robotic Feature Matching》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Feature matching underpins many robotic perception tasks, including visual localization, mapping, SLAM, and autonomous navigation. Existing semi-dense matchers predict confidence on fixed grids, limiting correspondences to predefined locations and requiring costly high-resolution grids for precise localization. We present CoReMatch (Coordinate Refinement Match), a recurrent framework that refines correspondences directly in continuous coordinate space rather than predicting discrete confidence maps. CoReMatch progressively improves correspondence estimates by propagating information across iterations. At the coarse stage, a Deep Aggregated Transformer captures global context and iteratively updates correspondence coordinates, while a lightweight regression head further sharpens their localization. Experiments on indoor and outdoor benchmarks show that CoReMatch strikes a strong balance between accuracy and efficiency, outperforming Efficient LoFTR in accuracy while running more than 10x faster on embedded edge hardware. These results demonstrate that recurrent coordinate refinement offers an efficient and scalable approach to real-time feature matching for robotic perception.

</details>

---
