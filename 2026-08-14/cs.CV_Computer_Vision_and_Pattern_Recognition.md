# cs.CV | Computer Vision and Pattern Recognition | 2026-08-14

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/世界模型/PlayWorld_Benchmarking_World_Models_with_Agent_Players_over_Long-Horizon_Objectives|PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives]]

![[assets/2608.13552_figure.png|800]]

- **arXiv**: [2608.13552](https://arxiv.org/abs/2608.13552)
- **PDF**: https://arxiv.org/pdf/2608.13552
- **详细分析**: [[20_Research/Papers/世界模型/PlayWorld_Benchmarking_World_Models_with_Agent_Players_over_Long-Horizon_Objectives|PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives]]
- **作者**: Kaixin Ding, Xi Chen, Minghong Cai, Zhiyuan Xu, Yiyang Wang, Yuxiang Lu, Junyi Li, Shuyang Chen, Yuan Gao, Xin Tao, Pengfei Wan, Hengshuang Zhao
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.4（加权：大模型 0.4，世界模型 1）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《PlayWorld: Benchmarking World Models with Agent Players over Long-Horizon Objectives》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DrivingWorld, HY-World, IRASim, LingBot-World, MemoBench, Omni-WorldBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video world models simulate future states conditioned on current observations and user actions. Recent systems have demonstrated impressive video consistency and action controllability over long sequences. However, fairly comparing these interactive models remains challenging. In practice, a human player typically evaluates a world model by pursuing long-horizon objectives through interaction. For example, a user may turn around 360 degrees to see whether the environment remains consistent, or walk into the water and inspect whether realistic water ripples are generated. The action sequence required to achieve the same objective may vary substantially between models, making fixed action-conditioned evaluation unsuitable for cross-model comparison. To address this, we employ multi-modal Agent Players to interact with world models toward specified long-horizon objectives. Building on this paradigm, we introduce PlayWorld, a benchmark providing 171 scenarios, each with a specified objective. To evaluate performance thoroughly, we assess models along four core dimensions: geometry consistency, interaction fidelity, out-of-sight evolution, and insight evolution. In addition, we incorporate basic ability metrics for video quality and controllability. Experiments across nine state-of-the-art world models reveal that current models remain unreliable on long-horizon interactive objectives, particularly in maintaining spatial consistency and persistent state evolution. Code and data are available at https://github.com/kxding/PlayWorld.

</details>

---

### [[20_Research/Papers/世界模型/Intervention-Aware_Clinical_World_Model_for_Post-Op_Outcome_Forecasting_in_Cardiology|Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology]]

![[assets/2608.13518_figure.png|800]]

- **arXiv**: [2608.13518](https://arxiv.org/abs/2608.13518)
- **PDF**: https://arxiv.org/pdf/2608.13518
- **详细分析**: [[20_Research/Papers/世界模型/Intervention-Aware_Clinical_World_Model_for_Post-Op_Outcome_Forecasting_in_Cardiology|Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology]]
- **作者**: Yunsung Chung, Yingshuo Liu, Abboud F. Hassan, Han Feng, Mary M. Maleckar, Nassir Marrouche, Jihun Hamm
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Intervention-Aware Clinical World Model for Post-Op Outcome Forecasting in Cardiology》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many clinical prediction models treat post-intervention outcomes as a one-step mapping from baseline measurements to a future endpoint. However, recovery after a procedure often unfolds as an irregular trajectory: clinical observations, medication changes, repeat interventions, and physiological measurements are recorded asynchronously and can change risk assessment over time. We propose an intervention-aware clinical world model that represents each patient with a structured latent state and evolves it through time-ordered post-intervention events. The model first encodes baseline imaging into a 3D spatial latent state. It then updates this state using procedural context, static covariates, elapsed time, and peri-event physiological embeddings. Follow-up imaging provides training-only supervision through a latent forecasting objective. We apply the framework to atrial fibrillation ablation. During the 90-day recovery window, irregular post-procedure records provide clinically meaningful evidence for long-term recurrence risk. In repeated internal cross-validation on DECAAF-II, our model achieves AUROC 0.756 and AUPRC 0.777 for recurrence prediction. It also achieves a scar-extent MAE of 2.971 percentage points without requiring follow-up MRI intensities at inference. The learned state supports recurrence-risk queries at different horizons and retrospective input editing of blanking-period records.

</details>

---

### [[20_Research/Papers/大模型/TraVEL_Trajectory-Guided_Video_Embedding_Learning_for_Driving-Video_Retrieval|TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval]]

![[assets/2608.13495_figure.png|800]]

- **arXiv**: [2608.13495](https://arxiv.org/abs/2608.13495)
- **PDF**: https://arxiv.org/pdf/2608.13495
- **详细分析**: [[20_Research/Papers/大模型/TraVEL_Trajectory-Guided_Video_Embedding_Learning_for_Driving-Video_Retrieval|TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval]]
- **作者**: Yi-Chung Chen, Philip Jacobson, Tom Lampo, Yiren Lu, Jin Yao, David I. Inouye, Jing Gao, Danhua Guo, Burhan Yaman
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《TraVEL: Trajectory-Guided Video Embedding Learning for Driving-Video Retrieval》归入 强化学习、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficiently retrieving relevant clips from large-scale driving logs is essential for data curation, model development, and safety analysis. Structured and rule-based retrieval systems can explicitly target driving events, but typically require expert-defined rules, auxiliary data, and multi-stage perception pipelines. Multimodal embedding models offer a simpler and more efficient alternative by representing each video with a single searchable vector. However, general-purpose models often rely on shortcuts from static scene context and struggle to distinguish motion-centric events, such as turning left versus right or accelerating versus decelerating. In this work, we study how to adapt a general-purpose multimodal embedding model to driving-video retrieval. We first fine-tune Qwen3-VL-Embedding on paired clips and reasoning traces from nuReasoning using an InfoNCE objective. While this stage substantially improves overall retrieval, caption supervision alone remains insufficient for fine-grained motion understanding. We therefore introduce TraVEL (Trajectory-Guided Video Embedding Learning), a motion-aware fine-tuning framework that uses ego-trajectory similarity as a reward within Group Relative Policy Optimization. Trajectories serve only as privileged training supervision; retrieval still operates on single-vector video embeddings without ego poses, expert rules, or auxiliary perception outputs. We further construct a driving-video retrieval benchmark from nuReasoning. Experiments show that TraVEL improves motion-centric retrieval across model scales: relative to SFT, it raises longitudinal and lateral mAP by 9.8 and 4.7 points at 2B, with corresponding gains of 7.2 and 1.5 points at 8B. TraVEL thus combines physically grounded supervision with efficient embedding-based search.

</details>

---

### [[20_Research/Papers/具身智能/DreamX-Phi_1.0_Action-Conditioned_Video_World_Model_for_Robotic_Manipulation|DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation]]

![[assets/2608.13489_figure.png|800]]

- **arXiv**: [2608.13489](https://arxiv.org/abs/2608.13489)
- **PDF**: https://arxiv.org/pdf/2608.13489
- **详细分析**: [[20_Research/Papers/具身智能/DreamX-Phi_1.0_Action-Conditioned_Video_World_Model_for_Robotic_Manipulation|DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation]]
- **作者**: DreamX Team, Rui Chen, Xiangxiang Chu, Geng Li, Jifan Li, Qingfeng Shi, Datao Tang, Jing Tang, Jun Wang, Pengfei Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.7（加权：具身智能 1.8，世界模型 0.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《DreamX-Phi 1.0: Action-Conditioned Video World Model for Robotic Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Cosmos3-DROID, DreamX-World, IRASim, UniSim, Vid2World, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present \textbf{DreamX-Phi 1.0}, an action-conditioned video world model for robotic manipulation that, given an observed frame, a language instruction, and a prescribed action sequence comprising end-effector poses and gripper states, predicts the resulting future observations. Yet realism alone does not guarantee faithfulness: a convincing rollout can still move the wrong arm or lose the manipulated object. To ensure the prediction respects each arm's commanded path, we inject per-arm $\mathrm{SE}(3)$ transformations into attention via \textbf{PRoPE-style geometric encoding}, preserving arm identity and rigid-motion structure. Action control alone does not fully constrain scene geometry or the evolution of small manipulated objects. We therefore add a lightweight \textbf{depth branch} for scene-level geometry and use \textbf{SAM3 masks} with a frozen \textbf{V-JEPA teacher} to maintain object consistency throughout grasping. We further distill the multi-step generator into a few-step student via distribution-matching distillation for efficient deployment. At the time of writing, \model{} achieves first place on Track~1 and second place on Track~2 of the WorldArena~2.0 Challenge. Our model and code will be publicly available.

</details>

---

### [[20_Research/Papers/具身智能/Semantic_Radiance_Fields_as_Simulators_for_Spatial_Reasoning_in_Real-World_Scenes|Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes]]

![[assets/2608.13095_figure.png|800]]

- **arXiv**: [2608.13095](https://arxiv.org/abs/2608.13095)
- **PDF**: https://arxiv.org/pdf/2608.13095
- **详细分析**: [[20_Research/Papers/具身智能/Semantic_Radiance_Fields_as_Simulators_for_Spatial_Reasoning_in_Real-World_Scenes|Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes]]
- **作者**: Nico Heider, Michał Jan Włodarczyk, Katarzyna Wasielewska-Michniewska, Przemysław Hołda, Martin Schieck, Marcin Paprzycki, Maria Ganzha, Bogdan Franczyk
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Semantic Radiance Fields as Simulators for Spatial Reasoning in Real-World Scenes》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World, STRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training and evaluating spatial reasoning in embodied agents requires diverse environments that are both geometrically faithful and semantically queryable. Synthetic simulators offer ground truth semantics but sacrifice realism; simulators based on reconstructions of real-world environments have realistic appearance but lack ground truth semantics by default. We propose using Semantic Radiance Fields (SRF) as simulators for spatial reasoning agents. SRFs are a representation that unifies these requirements by lifting 2D semantic segmentations from pretrained vision models into a 3D radiance field that jointly encodes geometry, appearance, and per-class semantic identity. The resulting fields are reconstructed from posed RGB captures of real scenes and support novel-view synthesis, semantic and free-space queries within a single grounded representation. This enables the efficient generation of diverse real-world environments to train and evaluate spatial reasoning models. As an example application, we outline an SRF-driven simulator for an orchard apple-reaching task, in which the radiance field supplies camera rendering, semantic ground truth, and occupancy queries to a physics engine.

</details>

---

### [[20_Research/Papers/具身智能/H2R-Bench_Benchmarking_Human-to-Robot_Manipulation_Video_Generation_in_World_Models|H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models]]

![[assets/2608.13049_figure.png|800]]

- **arXiv**: [2608.13049](https://arxiv.org/abs/2608.13049)
- **PDF**: https://arxiv.org/pdf/2608.13049
- **详细分析**: [[20_Research/Papers/具身智能/H2R-Bench_Benchmarking_Human-to-Robot_Manipulation_Video_Generation_in_World_Models|H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models]]
- **作者**: Dingyi Rong, Yue Shi, Chaofan Ma, Jiezhang Cao, Zongrui Wang, Zeyu Zhang, Yao Mu, Guangtao Zhai, Ning Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.6（加权：具身智能 1.5，世界模型 0.8，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《H2R-Bench: Benchmarking Human-to-Robot Manipulation Video Generation in World Models》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：H2R-Bench, RBench, RoboTrustBench, RoboWM-Bench, VBench, WorldModelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale manipulation data is essential for robot learning, yet collecting robot demonstrations remains expensive and difficult to scale. Meanwhile, abundant egocentric human manipulation videos provide rich behavioral experiences, but transferring them across embodiments remains challenging due to differences between human hands and robotic end-effectors. Recent advances in video world models offer a promising pathway to synthesize robot-centric manipulation videos from human observations, while their cross-embodiment transfer capability remains largely unexplored. Therefore, we introduce H2R-Bench, a benchmark for evaluating cross-embodiment human-to-robot manipulation video generation, where models transform egocentric human demonstrations into robot manipulation videos under specified embodiments. Each benchmark instance contains a human demonstration video, target embodiment constraints, and source-grounded annotations covering task goals, action events, functional contacts, and object responses. H2R-Bench evaluates generated videos through five dimensions, including goal-state completion, action-event completion, functional contact transfer, embodiment correctness, and general video quality. We benchmark eleven state-of-the-art video generation models across six manipulation families and two robot embodiments. Our evaluation reveals that current video world models remain limited in human-to-robot manipulation transfer: even leading models often fail in embodiment consistency, functional interaction, and task execution. H2R-Bench provides a systematic diagnostic framework for evaluating whether video world models can bridge the human-to-robot embodiment gap and convert human manipulation observations into robot-centric training resources.

</details>

---

### [[20_Research/Papers/世界模型/RGB-D_Video_Generation_for_Improving_Human-to-Robot_Object_Handover_Prediction|RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction]]

![[assets/2608.13028_figure.png|800]]

- **arXiv**: [2608.13028](https://arxiv.org/abs/2608.13028)
- **PDF**: https://arxiv.org/pdf/2608.13028
- **详细分析**: [[20_Research/Papers/世界模型/RGB-D_Video_Generation_for_Improving_Human-to-Robot_Object_Handover_Prediction|RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction]]
- **作者**: Tianyu Sun, Zhoujie Fu, Zihui Gao, Bang Zhang, Guosheng Lin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《RGB-D Video Generation for Improving Human-to-Robot Object Handover Prediction》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GraspNet, HandoverSim, PoseNet, ReferenceNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-to-robot (H2R) object handover is a fundamental capability for human-robot collaboration, yet progress is hindered by the scarcity of large-scale, human-centric datasets and the significant sim-to-real gap. To address these challenges, we introduce Hand2Bot, an RGB-D video dataset that provides rich contextual information such as body posture and facial expressions, specifically collected for handover scenarios with real-world noise patterns. We further propose PassGen, a generative pipeline that leverages stable video diffusion and an Intention-Aware Temporal Face Encoder to synthesize realistic handover sequences while ensuring hand-object consistency. To bridge the sim-to-real gap, we implement a morphology-based depth editing strategy that replicates realistic sensor noise found in physical depth maps. Experimental evaluations demonstrate that our framework achieves high intention identification accuracy and low false trigger rates in both ablation studies and real-world deployment on a physical robot platform. Our results confirm that training on PassGen allows for robust zero-shot transfer and earlier intention anticipation compared to traditional hand-centric baselines, effectively enabling socially aware robotic behavior in shared workspaces.

</details>

---

### [[20_Research/Papers/机器人/EgoPHI_Estimating_Contact_and_Force_from_Egocentric_Vision|EgoPHI: Estimating Contact and Force from Egocentric Vision]]

![[assets/2608.13014_figure.png|800]]

- **arXiv**: [2608.13014](https://arxiv.org/abs/2608.13014)
- **PDF**: https://arxiv.org/pdf/2608.13014
- **详细分析**: [[20_Research/Papers/机器人/EgoPHI_Estimating_Contact_and_Force_from_Egocentric_Vision|EgoPHI: Estimating Contact and Force from Egocentric Vision]]
- **作者**: Andela Ilic, Rachel Schuchert, Yijing Jiang, Christian Holz
- **cs 子类**: cs.CV, cs.GR, cs.HC, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《EgoPHI: Estimating Contact and Force from Egocentric Vision》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding hand-object interaction from egocentric vision is essential for modeling how people physically engage with the surrounding world. Yet reasoning about physically grounded interaction requires estimating the forces acting on hands and objects, beyond localizing contact. We present EgoPHI, the first method that jointly estimates dense contact maps and 3D force distributions on hand and object meshes from a single monocular RGB image and object geometry. To address the lack of scalable ground-truth force annotations, we introduce a physics-based simulation pipeline that augments existing hand-object datasets with dense per-vertex force supervision. EgoPHI then learns dense 3D contact and force on interacting hand and articulated object meshes, extending vision-based force estimation beyond image-space or planar settings. Our evaluation on in-distribution and out-of-distribution benchmarks shows that EgoPHI improves force estimation over existing approaches while generalizing to unseen datasets. To evaluate sim-to-real transfer, we constructed two physical objects that capture dense object contact and force magnitude and used them to record a dataset of interactions from eight participants across diverse touch and grasp types. Our results demonstrate that EgoPHI recovers meaningful 3D contact and force distributions in simulated, out-of-distribution, and real-world settings, advancing egocentric hand-object understanding from contact localization toward physically grounded interaction reasoning.

</details>

---

### [[20_Research/Papers/大模型/TennisVAR_A_Stroke-Evidence-Grounded_Multimodal_Large_Language_Model_for_Tactical_Reasoning_in_Tennis_Videos|TennisVAR: A Stroke-Evidence-Grounded Multimodal Large Language Model for Tactical Reasoning in Tennis Videos]]

![[assets/2608.12920_figure.png|800]]

- **arXiv**: [2608.12920](https://arxiv.org/abs/2608.12920)
- **PDF**: https://arxiv.org/pdf/2608.12920
- **详细分析**: [[20_Research/Papers/大模型/TennisVAR_A_Stroke-Evidence-Grounded_Multimodal_Large_Language_Model_for_Tactical_Reasoning_in_Tennis_Videos|TennisVAR: A Stroke-Evidence-Grounded Multimodal Large Language Model for Tactical Reasoning in Tennis Videos]]
- **作者**: Yifan Mei, Qingling Shi, Changli Wu, Jiayuan Rao, Jiayi Ji, Liujuan Cao
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《TennisVAR: A Stroke-Evidence-Grounded Multimodal Large Language Model for Tactical Reasoning in Tennis Videos》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CaST-Bench, FineGym, LongVideoBench, NExT-GQA, NExT-QA, SoccerNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sports-video understanding is moving beyond event recognition toward explaining how actions collectively shape match progression, however, existing tennis-video methods either perceive individual strokes without modeling their tactical dependencies or generate high-level analyses without grounding them in the underlying events. To bridge this perception-to-understanding gap, we formulate stroke-evidence-grounded tactical reasoning, a new rally-level task that requires models to jointly predict an open-ended answer, a hierarchical tactic label, an ordered sequence of supporting strokes, and decisive key actions, with each evidence stroke anchored to its racket-ball contact frame. We further introduce TRACE (Tactical Reasoning with Action-Chain Evidence in Tennis), a large-scale expert-annotated benchmark containing 11,189 rally videos, 41,485 stroke events, 25,429 tactical units, and 11,189 question-answer pairs, which unifies fine-grained stroke attributes, cross-stroke tactical relations, hierarchical tactic annotations, and evidence-grounded questions across factual perception, tactical understanding, and decision reasoning. Building on TRACE, we propose TennisVAR (Tennis Video Action-chain Reasoner), an evidence-grounded multimodal large language model that follows an "event-relation-evidence-tactic" reasoning paradigm, where an Event Parsing Module converts continuous rallies into explicit stroke-event sequences while a Tactical Graph-Guided Temporal Reasoner jointly models rally progression and same-player decision dependencies to identify question-relevant evidence and decisive actions.

</details>

---

### [[20_Research/Papers/大模型/HounsWorld_A_Multimodal_World_Model_for_Hidden_Patient-State_Readout,_Reconstruction,_and_Simulation|HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation]]

![[assets/2608.12904_figure.png|800]]

- **arXiv**: [2608.12904](https://arxiv.org/abs/2608.12904)
- **PDF**: https://arxiv.org/pdf/2608.12904
- **详细分析**: [[20_Research/Papers/大模型/HounsWorld_A_Multimodal_World_Model_for_Hidden_Patient-State_Readout,_Reconstruction,_and_Simulation|HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation]]
- **作者**: Yunhao Bai, Zhongwei Qiu, Guangyu Guo, Yiming Huang, Tony C. W. Mok, Qinji Yu, Ling Zhang, Yan Wang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.2（加权：大模型 0.4，世界模型 0.8）
- **关联关键词**: Multimodal, WorldModel

#### 研究背景与动机

《HounsWorld: A Multimodal World Model for Hidden Patient-State Readout, Reconstruction, and Simulation》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CheXWorld, HounsBench, HounsWorld, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Clinical intelligence requires estimating a patient's underlying condition from incomplete observations rather than learning isolated mappings from scans to answers. Volumetric medical images provide dense observations of anatomy, attenuation, and lesions, whereas clinical language provides sparse but complementary semantic observations. We formulate CT-centered intelligence as inference over a shared latent patient state, under which readout, reconstruction, and simulation all become state-dependent prediction problems. To operationalize this view, we introduce HounsBench, a computed tomography (CT) centric patient-state benchmark that unifies these three task families with patient-disjoint splits and per-family metrics, and HounsWorld, a 3B multimodal world model that treats volumetric scans and language as observations of the shared state through Joint Understanding-Generation Learning. A shared transformer forms an implicit patient-state estimate and supports three outputs: query-conditioned answers that read out the state, reports and captions that reconstruct it in language, and condition-specific CT volumes for low-dose denoising, virtual contrast enhancement, and anatomy-constrained text-and-mask-to-volume generation. Zero-initialized CT adapters preserve pretrained multimodal mappings, while condition-explicit Hounsfield-unit window sampling exposes clinically meaningful density observations. HounsWorld shows strong performance across all three task families while consistently improving CT understanding through clinically structured completion. Our project is available at https://github.com/byhwhite/HounsWorld.git

</details>

---

### [[20_Research/Papers/多模态技术/VOS-Agent_The_1st_Place_Solution_for_the_8th_LSVOS_Challenge_(MOSEv2_Track)|VOS-Agent: The 1st Place Solution for the 8th LSVOS Challenge (MOSEv2 Track)]]

![[assets/2608.12721_figure.png|800]]

- **arXiv**: [2608.12721](https://arxiv.org/abs/2608.12721)
- **PDF**: https://arxiv.org/pdf/2608.12721
- **详细分析**: [[20_Research/Papers/多模态技术/VOS-Agent_The_1st_Place_Solution_for_the_8th_LSVOS_Challenge_(MOSEv2_Track)|VOS-Agent: The 1st Place Solution for the 8th LSVOS Challenge (MOSEv2 Track)]]
- **作者**: Canyang Wu, Jinrong Zhang, Xusheng He, Ce Bian, Xianjing Han, Jianlong Wu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《VOS-Agent: The 1st Place Solution for the 8th LSVOS Challenge (MOSEv2 Track)》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Complex video object segmentation requires robust target propagation under severe occlusion, disappearance and reappearance. Although SAM3 provides strong promptable mask propagation, a uniform inference path remains unreliable for tiny targets with insufficient visual evidence and semantic-dominated targets whose identities depend on explicit attributes. To this end, we present VOS-Agent, a collaborative framework that retains SAM3 as the shared dense segmentation module and conditionally activates specialized agents according to target characteristics. A Target Perception and Routing Agent assigns each sequence to a regular, tiny, or semantic-dominated route. Tiny targets are supported by a Visual Tracking Agent through confidence-aware box prompts, while semantic-dominated targets are handled by an MLLM-based Semantic Agent through description-guided localization and candidate verification. On the MOSEv2 test set, VOS-Agent achieves 69.82% on the official $\mathcal{J}\&amp;\dot{\mathcal{F}}$ metric and ranks first in the MOSEv2 Track of the 8th LSVOS Challenge at ECCV 2026.

</details>

---

### [[20_Research/Papers/具身智能/FUSE_Active_Functional_Affordance_Grounding_through_Adaptive_Semantic-Geometric_Evidence_Acquisition|FUSE: Active Functional Affordance Grounding through Adaptive Semantic-Geometric Evidence Acquisition]]

![[assets/2608.12683_figure.png|800]]

- **arXiv**: [2608.12683](https://arxiv.org/abs/2608.12683)
- **PDF**: https://arxiv.org/pdf/2608.12683
- **详细分析**: [[20_Research/Papers/具身智能/FUSE_Active_Functional_Affordance_Grounding_through_Adaptive_Semantic-Geometric_Evidence_Acquisition|FUSE: Active Functional Affordance Grounding through Adaptive Semantic-Geometric Evidence Acquisition]]
- **作者**: Zhou Chen, Sathyanarayanan N. Aakur
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《FUSE: Active Functional Affordance Grounding through Adaptive Semantic-Geometric Evidence Acquisition》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied agents must often identify and interact with objects based on their function rather than their identity, requiring them to actively acquire observations that reveal discriminative functional evidence. Existing affordance grounding methods operate from fixed viewpoints and lack mechanisms for deciding where to look when functional cues are occluded or incomplete. We introduce Active Functional Affordance Grounding, a new task in which an agent sequentially explores a scene to identify and spatially ground an object satisfying a functional query. To address this problem, we propose FUSE, an adaptive semantic-geometric evidence acquisition framework that combines explicit uncertainty-driven exploration with a learned amortized planner to efficiently select informative viewpoints. We further introduce a Habitat-based benchmark for evaluating active functional grounding. Experiments show that FUSE achieves the highest observed non-oracle grounding performance while reducing computation by 1.33x relative to fully explicit exploration, and remains effective across multiple affordance knowledge sources.

</details>

---

### [[20_Research/Papers/具身智能/Can_Vision-Language_Models_Assess_Proxemic_Risk_from_Egocentric_Robot_Images|Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?]]

![[assets/2608.12515_first_page.png|800]]

- **arXiv**: [2608.12515](https://arxiv.org/abs/2608.12515)
- **PDF**: https://arxiv.org/pdf/2608.12515
- **详细分析**: [[20_Research/Papers/具身智能/Can_Vision-Language_Models_Assess_Proxemic_Risk_from_Egocentric_Robot_Images|Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?]]
- **作者**: Vladyslava Rudas, Dmytro Kuzmenko
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Can Vision-Language Models Assess Proxemic Risk from Egocentric Robot Images?》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assessing proxemic danger from a robot's egocentric perspective is critical for safe embodied navigation in human environments and requires both visual and contextual reasoning. We evaluate three opensource vision-language models (VLMs) (\textit{InternVL}, \textit{Qwen-VL}, and \textit{SmolVLM}) on the classification of egocentric robot images into four danger levels, comparing three prompting strategies and two rounds of QLoRA fine-tuning against a stratified random baseline. Without fine-tuning, all models perform near the baseline, while fine-tuning yields only modest overall improvements. However, \textit{Qwen-VL} with an advanced prompt achieves substantially higher recall for high-danger cases than the other models. An analysis of person localization further shows that correct danger classification does not correspond to better spatial grounding, indicating that a model may produce a useful safety label without attending to the relevant region of the scene. These results show that current VLMs remain limited in fine-grained proxemic reasoning and spatial grounding, although targeted prompting and fine-tuning can improve high-danger detection in selected models.

</details>

---
