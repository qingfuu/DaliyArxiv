# cs.CV | Computer Vision and Pattern Recognition | 2026-07-01

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/世界模型/MemLearner_Learning_to_Query_Context_memory_for_Video_World_Models|MemLearner: Learning to Query Context memory for Video World Models]]

![[assets/2606.31734_figure.png|800]]

- **arXiv**: [2606.31734](https://arxiv.org/abs/2606.31734)
- **PDF**: https://arxiv.org/pdf/2606.31734
- **详细分析**: [[20_Research/Papers/世界模型/MemLearner_Learning_to_Query_Context_memory_for_Video_World_Models|MemLearner: Learning to Query Context memory for Video World Models]]
- **作者**: Jiwen Yu, Jianxiong Gao, Jianhong Bai, Yiran Qin, Kaiyi Huang, Quande Liu, Xintao Wang, Pengfei Wan, Kun Gai, Xihui Liu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《MemLearner: Learning to Query Context memory for Video World Models》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video World Models are interactive video generation models that predict future world states based on user actions and history video frames. A critical challenge in video world models is the lack of memory, causing inconsistent generated scenes over extended durations. Previous methods explored rule-based context frame retrieval as memory, but they fail to generalize in scenarios with scene occlusions and dynamic objects. We propose MemLearner, a learning-based adaptive context query method using query tokens to bridge context and predicted tokens. By leveraging the video generation model itself for context querying, MemLearner exploits pre-trained visual priors without training additional modules from scratch, and incorporates efficient strategies for training and inference. We collect a dataset of long videos with scene occlusions and dynamic objects, paired with camera pose annotations, and propose a multi-dataset training strategy leveraging both annotated rendered and unannotated real-world videos. Extensive experiments demonstrate that MemLearner significantly outperforms prior video world models in terms of scene consistency and memory, particularly under challenging occlusion and dynamic scenarios.

</details>

---

### [[20_Research/Papers/具身智能/DynFly_Dynamic-Aware_Continuous_Trajectory_Generation_for_UAV_Vision-Language_Navigation_in_Urban_Environments|DynFly: Dynamic-Aware Continuous Trajectory Generation for UAV Vision-Language Navigation in Urban Environments]]

![[assets/2606.31654_figure.png|800]]

- **arXiv**: [2606.31654](https://arxiv.org/abs/2606.31654)
- **PDF**: https://arxiv.org/pdf/2606.31654
- **详细分析**: [[20_Research/Papers/具身智能/DynFly_Dynamic-Aware_Continuous_Trajectory_Generation_for_UAV_Vision-Language_Navigation_in_Urban_Environments|DynFly: Dynamic-Aware Continuous Trajectory Generation for UAV Vision-Language Navigation in Urban Environments]]
- **作者**: Wen Jiang, Hanfang Liang, Li Wang, Kangyao Huang, Wang Xu, Wei Fan, Jinyuan Liu, Shaoyu Liu, Hongwei Duan, Bin Xu, Xiangyang Ji, Huaping Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《DynFly: Dynamic-Aware Continuous Trajectory Generation for UAV Vision-Language Navigation in Urban Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in multimodal large models have significantly improved UAV vision-language navigation (UAV-VLN) by enhancing high-level perception and reasoning. However, existing methods mainly focus on predicting discrete actions, local targets, or sparse waypoints, while the continuous transition from navigation intent to executable UAV motion remains weakly modeled. This motion-interface gap limits the continuity, stability, and executability of generated UAV trajectories. To address this gap, we propose DynFly, a dynamic-aware continuous trajectory generation framework that bridges high-level navigation reasoning and executable UAV motion. DynFly bridges high-level navigation intent and continuous UAV motion through a lightweight trajectory generation layer. Specifically, it represents expert trajectories in B-spline control-point space and employs a Spline-DiT generator to learn conditional trajectory generation via flow matching. Furthermore, we introduce UAV-oriented dynamic-aware supervision over position, finite-difference velocity, finite-difference acceleration, heading consistency, and local target alignment, enabling the generated trajectories to better satisfy UAV motion characteristics. And our trajectory generation framework can also be integrated with an existing UAV-VLN framework while preserving its original visual-language reasoning pipeline. Extensive experiments on the OpenUAV UAV-VLN benchmark show that DynFly improves both navigation performance and trajectory quality. On the Test Unseen Full split, DynFly improves the strongest baseline by 4.69 NDTW, 2.40 SDTW, 2.14 SR points and 4.87 OSR points, while reducing NE by 4.51 m.

</details>

---

### [[20_Research/Papers/具身智能/Technical_Report_of_RoboSpatial_Challenge_at_CVPR_2026_Selective_Reasoning_Activation_and_Reference-Frame_Disambiguation_for_Embodied_Spatia|Technical Report of RoboSpatial Challenge at CVPR 2026: Selective Reasoning Activation and Reference-Frame Disambiguation for Embodied Spatial Reasoning]]

![[assets/2606.31645_figure.png|800]]

- **arXiv**: [2606.31645](https://arxiv.org/abs/2606.31645)
- **PDF**: https://arxiv.org/pdf/2606.31645
- **详细分析**: [[20_Research/Papers/具身智能/Technical_Report_of_RoboSpatial_Challenge_at_CVPR_2026_Selective_Reasoning_Activation_and_Reference-Frame_Disambiguation_for_Embodied_Spatia|Technical Report of RoboSpatial Challenge at CVPR 2026: Selective Reasoning Activation and Reference-Frame Disambiguation for Embodied Spatial Reasoning]]
- **作者**: Yuxiang Xie, Qi Lv, Jianming Xing, Zijian Hong, Xiang Deng, Weili Guan, Liqiang Nie
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 1.2，大模型 0.1）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Technical Report of RoboSpatial Challenge at CVPR 2026: Selective Reasoning Activation and Reference-Frame Disambiguation for Embodied Spatial Reasoning》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models achieve strong general perception but often struggle with the spatial reasoning required for embodied tasks. We present RoboSpatialBrain, our submission to the RoboSpatial Challenge at the Embodied Reasoning in Action Workshop, CVPR 2026, built on RoboBrain2.5-8B-NV. RoboSpatialBrain combines two training-free, inference-time mechanisms: a forced &lt;think&gt; prefix activation strategy paired with a task-specific post-prompt that elicits deliberate reasoning on context and compatibility tasks, and an explicit reference-frame redirection pipeline that resolves camera-centric and object-centric ambiguity for context tasks. We additionally explore fine-tuning RoboBrain2.5 on compatibility data and present a detailed analysis of its interaction with prompting. RoboSpatialBrain achieved first place in the RoboSpatial Challenge, with an overall success rate of 80.9\% on RoboSpatial-Home. Code is available at https://github.com/YuxiangXie2003/RoboSpatialBrain.

</details>

---

### [[20_Research/Papers/大模型/Robust_Autonomous_UAV_Landing_on_Maritime_Platforms_via_Multimodal_Agentic_AI_and_Active_Wave_Compensation|Robust Autonomous UAV Landing on Maritime Platforms via Multimodal Agentic AI and Active Wave Compensation]]

![[assets/2606.31613_figure.png|800]]

- **arXiv**: [2606.31613](https://arxiv.org/abs/2606.31613)
- **PDF**: https://arxiv.org/pdf/2606.31613
- **详细分析**: [[20_Research/Papers/大模型/Robust_Autonomous_UAV_Landing_on_Maritime_Platforms_via_Multimodal_Agentic_AI_and_Active_Wave_Compensation|Robust Autonomous UAV Landing on Maritime Platforms via Multimodal Agentic AI and Active Wave Compensation]]
- **作者**: Francisco S. Neves, Pedro N. Pereira, Raul D. S. G. Campilho, Andry M. Pinto
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 强化学习, 具身智能
- **相关性评分**: 2.6（加权：具身智能 0.3，大模型 0.6，强化学习 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Robust Autonomous UAV Landing on Maritime Platforms via Multimodal Agentic AI and Active Wave Compensation》归入 机器人、大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous aerial inspection of marine infrastructure is frequently compromised by stochastic sea states, introducing risks of high-kinetic impacts, post-landing toppling, and sensory occlusion. This paper proposes a decoupled, multi-vehicle landing framework synchronizing an Unmanned Surface Vehicle (USV) equipped with a 3-RPU stabilized platform with a robust Unmanned Aerial Vehicle (UAV). The architecture utilizes two independent Deep Reinforcement Learning (DRL) agents: a Soft Actor-Critic (SAC) agent providing high-frequency wave-motion compensation for the landing deck, and a multimodal RL agent for the UAVs final approach. Evaluated in high-fidelity maritime simulations, the system achieved a 100% landing success rate across 15 trials in wave states varying from calm to rough. Results show a mean stabilization efficacy of 87.8%, maintaining the landing surface within 1 degree of the horizontal plane for 96% of the mission duration in rough conditions, effectively contributing to safer landings.

</details>

---

### [[20_Research/Papers/具身智能/AeroVerse-SatAgent_UAV-Satellite_Collaborative_Spatial_Reasoning_Inspired_by_the_Dual_Visual_Pathway_Theory_of_Cognitive_Neuroscience|AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience]]

![[assets/2606.31467_figure.png|800]]

- **arXiv**: [2606.31467](https://arxiv.org/abs/2606.31467)
- **PDF**: https://arxiv.org/pdf/2606.31467
- **详细分析**: [[20_Research/Papers/具身智能/AeroVerse-SatAgent_UAV-Satellite_Collaborative_Spatial_Reasoning_Inspired_by_the_Dual_Visual_Pathway_Theory_of_Cognitive_Neuroscience|AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience]]
- **作者**: Wenyi Zhang, Fanglong Yao, Youzhi Liu, Peng Hu, Zhengqiu Zhu, Chen Gao, Xian Sun, Kun Fu
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.1，机器人 0.8）
- **关联关键词**: EmbodiedAI, ComputerVision, Systems

#### 研究背景与动机

《AeroVerse-SatAgent: UAV-Satellite Collaborative Spatial Reasoning Inspired by the Dual Visual Pathway Theory of Cognitive Neuroscience》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirCopBench, MMSI-Bench, Open3D-VQA, UrBench, VQA, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid advancement of aerospace embodied intelligence, enabling Unmanned Aerial Vehicles (UAVs) to autonomously understand and reason about complex environments has become increasingly important. However, existing UAV-based spatial reasoning approaches face critical limitations: single-view perception renders them vulnerable to occlusions and perspective distortions, while most VLMs lack explicit geometric modeling, relying on semantic cues and yielding inconsistent reasoning under viewpoint and scale variations. To address these challenges, we propose SatAgent, a UAV-Satellite collaborative spatial reasoning model inspired by the dual-pathway mechanism of the human visual system. By jointly leveraging satellite and UAV perspectives, SatAgent enables robust, accurate reasoning in complex urban environments. We first introduce a Geometric-Aware 3D Reconstruction Encoder that elevates 2D UAV features into explicit 3D spatial representations. Next, we design a multi-view topology-semantic alignment module integrating cross-view features within a unified BEV coordinate system. We further introduce a multi-view consistency loss encouraging viewpoint-invariant representations. Finally, we construct SatAgent-SR130K, the first large-scale UAV-Satellite collaborative multi-view spatial reasoning dataset. Experiments show SatAgent outperforms state-of-the-art general-purpose foundation models and specialized spatial reasoning models by 25.91\% and 11.69\%, respectively, across diverse tasks, achieving particularly high accuracy in complex geometric relationship reasoning.

</details>

---

### [[20_Research/Papers/具身智能/One_Video,_One_World_Turning_Monocular_Video_into_Physical_4D_Scenes|One Video, One World: Turning Monocular Video into Physical 4D Scenes]]

![[assets/2606.31388_figure.png|800]]

- **arXiv**: [2606.31388](https://arxiv.org/abs/2606.31388)
- **PDF**: https://arxiv.org/pdf/2606.31388
- **详细分析**: [[20_Research/Papers/具身智能/One_Video,_One_World_Turning_Monocular_Video_into_Physical_4D_Scenes|One Video, One World: Turning Monocular Video into Physical 4D Scenes]]
- **作者**: Junhao Chen, Boran Zhang, Mingjin Chen, Henghaofan Zhang, Saining Zhang, Congcong Zhu, Hao Zhao, Ruqi Huang, Zhihao Li, Yufei Wang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 世界模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.2，世界模型 0.2）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《One Video, One World: Turning Monocular Video into Physical 4D Scenes》归入 具身智能、大模型、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OneVideoOneWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce \textbf{OVOW}, the first training-free system that reconstructs \emph{instance-level, simulation-ready} 4D mesh scenes from a single monocular video. Recent 4D reconstruction achieves impressive rendering quality, but its outputs (\eg, implicit fields, Gaussian primitives, or point clouds) lack the watertight topology, instance separation, and standardized physical interfaces required by physics simulators and embodied AI. OVOW closes this gap with a four-stage pipeline: a vision-language model discovers, labels, and motion-classifies all instances; category-aware reconstruction yields per-instance meshes for rigid objects and topology-consistent mesh sequences for deformable ones; an iterative render-match-optimize procedure recovers metric scale and 6-DoF pose trajectories; and physics-grounded assembly enforces ground contact and inter-object support. Crucially, we model all motion, rigid and non-rigid, through direct vertex deformation without category-specific priors or skeleton rigging, producing watertight mesh scenes ready for downstream physics simulation and editing. We further establish the first benchmark for \emph{structured Video-to-4D} evaluation, with metrics for geometric correctness, instance separation, and physical plausibility beyond visual fidelity; the same pipeline doubles as a scalable engine for \emph{synthesizing} paired video-to-4D simulation data for future 4D world models and embodied AI. Across two synthetic benchmarks (static and 4D), OVOW attains the best overall layout and geometry accuracy and the lowest photometric and semantic error among all baselines, and on monocular video runs one to two orders of magnitude faster than the baselines, while downstream physics simulation confirms its physical stability.

</details>

---

### [[20_Research/Papers/具身智能/Reasoning-aware_Speculative_Decoding_for_Efficient_Vision-Language-Action_Models_in_Autonomous_Driving|Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving]]

![[assets/2606.31160_figure.png|800]]

- **arXiv**: [2606.31160](https://arxiv.org/abs/2606.31160)
- **PDF**: https://arxiv.org/pdf/2606.31160
- **详细分析**: [[20_Research/Papers/具身智能/Reasoning-aware_Speculative_Decoding_for_Efficient_Vision-Language-Action_Models_in_Autonomous_Driving|Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving]]
- **作者**: Anh Dung Dinh, Simon Khan, Flora Salim
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Reasoning-aware Speculative Decoding for Efficient Vision-Language-Action Models in Autonomous Driving》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AARL, AutoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern Vision-Language-Action (VLA) planners for autonomous driving emit a chain-of-causation (CoC) reasoning step \emph{before} producing a trajectory. The reasoning is autoregressive and dominates inference latency, while the trajectory head is parallel and cheap. Latency is an operational constraint in autonomous driving, so accelerating the reasoning step is the central problem we address. We observe that CoC reasoning has two qualitatively different needs: most tokens continue routine setup that follows naturally from the ego-trajectory history, and a small fraction encode commitments that require fresh visual evidence about an unexpected situation. We split this reasoning into two specialized paths: a \emph{routine reasoner} that handles the predictable continuation by attending to trajectory history, and a \emph{deliberative reasoner} (the unmodified VLA target) that handles novel cases by attending to current visual evidence, using the speculative decoding framework as the architectural template for how the two paths cooperate. Unlike standard speculative decoding, our routine reasoner is not a smaller replica of the target; the two reasoners are deliberately specialized to read different parts of the prompt. We propose two techniques to realize this. First, we introduce \textbf{FlatRoPE}, a 1D rotary positional embedding in the draft that breaks the rotational symmetry of the target's 3D M-RoPE, redirecting attention away from visual tokens and onto trajectory-history tokens. Second, we introduce \textbf{Action-aware RL (AARL)}, a post-training stage that uses an action-quality reward together with a static-reference KL anchor. Together, our two-reasoner system reduces the reasoning-step running time by approximately $4\times$ relative to the original Alpamayo planner.

</details>

---

### [[20_Research/Papers/具身智能/Rethinking_Foundation_Model_Collaboration_Enhancing_Specialized_Models_through_Proxy_Task_Reasoning|Rethinking Foundation Model Collaboration: Enhancing Specialized Models through Proxy Task Reasoning]]

![[assets/2606.31157_figure.png|800]]

- **arXiv**: [2606.31157](https://arxiv.org/abs/2606.31157)
- **PDF**: https://arxiv.org/pdf/2606.31157
- **详细分析**: [[20_Research/Papers/具身智能/Rethinking_Foundation_Model_Collaboration_Enhancing_Specialized_Models_through_Proxy_Task_Reasoning|Rethinking Foundation Model Collaboration: Enhancing Specialized Models through Proxy Task Reasoning]]
- **作者**: Hongyi Lin, Yang Liu, Jinhua Zhao, Xiaobo Qu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.6）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《Rethinking Foundation Model Collaboration: Enhancing Specialized Models through Proxy Task Reasoning》归入 大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoverNet, HPNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models are increasingly integrated into embodied intelligence systems, but directly assigning them structured prediction tasks requires precise geometric and numerical estimation, where specialized models often remain stronger. This capability mismatch raises a key question: should foundation models replace task-specific predictors, or should they collaborate through tasks better aligned with their strengths? We propose FAT, a foundation-model-augmented task-specific reasoning framework that treats collaboration as task decomposition rather than model replacement. FAT decomposes structured prediction into specialist prediction, information-space reconstruction, and foundation-model proxy reasoning. The specialist generates geometrically and physically valid hypotheses in the native output space, while the foundation model performs a bounded proxy task, such as selection or verification, over reconstructed multimodal candidates. We instantiate this principle as ProxySelect with a vision--language model. Across 2D object detection, 3D object detection, trajectory prediction, and semantic segmentation, ProxySelect consistently improves specialized baselines and substantially outperforms direct foundation-model regression at lower computational cost. These results suggest a general collaboration principle: specialized models preserve task-specific structure, while foundation models refine their hypotheses through contextual proxy reasoning.

</details>

---

### [[20_Research/Papers/机器人/PiLoT_v2_Pixel-to-Orthogonal_Map_Alignment_for_Free-view_UAV_Geo-localization|PiLoT v2: Pixel-to-Orthogonal Map Alignment for Free-view UAV Geo-localization]]

![[assets/2606.31098_figure.png|800]]

- **arXiv**: [2606.31098](https://arxiv.org/abs/2606.31098)
- **PDF**: https://arxiv.org/pdf/2606.31098
- **详细分析**: [[20_Research/Papers/机器人/PiLoT_v2_Pixel-to-Orthogonal_Map_Alignment_for_Free-view_UAV_Geo-localization|PiLoT v2: Pixel-to-Orthogonal Map Alignment for Free-view UAV Geo-localization]]
- **作者**: Xinyi Liu, Xiaoya Cheng, Rouwan Wu, Zhaochen Wang, Shen Yan, Maojun Zhang, Yu Liu
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《PiLoT v2: Pixel-to-Orthogonal Map Alignment for Free-view UAV Geo-localization》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AirSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-time, drift-free UAV geo-localization is essential for autonomous missions in GNSS-denied environments. The pioneering system, PiLoT, achieves high precision via Neural Pixel-to-3D Registration, aligning UAV video streams with a single rendered reference view from 3D meshes. However, its reliance on heavy 3D meshes incurs massive storage overheads, complex map acquisition, and significant computational rendering costs, severely hindering deployment on embedded platforms. To address these bottlenecks, we propose PiLoT v2, a lightweight yet robust evolution that shifts the paradigm to direct pixel-to-orthogonal map registration for free-view UAV geo-localization. By leveraging True Digital Orthophoto Maps (TDOMs) and Digital Surface Models (DSMs) as the reference substrate, PiLoT v2 replaces GPU-intensive 3D rendering with a highly efficient, CPU-friendly map cropping operation. To bridge the severe geometric discrepancy between these 2.5D orthogonal crops and free-view oblique UAV imagery, we train a cross-view feature registration network using a novel, large-scale geometrically annotated dataset. Furthermore, we integrate onboard sensor prior--specifically gravity direction and single-point laser rang--directly into the pose optimization manifold to enhance robustness against cross-view visual degradation. Experimental results demonstrate that PiLoT v2 achieves performance comparable to, or even exceeding, its Pixel-to-3D predecessor, while offering drastically lower storage and computational costs.

</details>

---

### [[20_Research/Papers/具身智能/Hierarchical_3D_Scene_Graph_Construction_and_Belief-based_Planning_for_Semantic_Navigation|Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation]]

![[assets/2606.31071_figure.png|800]]

- **arXiv**: [2606.31071](https://arxiv.org/abs/2606.31071)
- **PDF**: https://arxiv.org/pdf/2606.31071
- **详细分析**: [[20_Research/Papers/具身智能/Hierarchical_3D_Scene_Graph_Construction_and_Belief-based_Planning_for_Semantic_Navigation|Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation]]
- **作者**: Bing Wu, Zuyao Chen, Changwen Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Hierarchical 3D Scene Graph Construction and Belief-based Planning for Semantic Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Semantic navigation is a fundamental task for embodied agents operating in unseen environments, requiring both semantic understanding and long-term decision-making. Recent foundation models have empowered agents with rich semantic priors for this task. However, without structured global representations, decision-making often falls back on local observations and greedy strategies, resulting in inefficient exploration and myopic behaviors, especially in long-distance navigation. To address these challenges, we propose a zero-shot semantic navigation framework. Our method incrementally maintains an online Hierarchical 3D Scene Graph (HSG) to form a multi-granular semantic topology over objects, zones, and regions, serving as a compact state abstraction for global planning. Building on this memory, we introduce a hierarchical belief-based planning framework that fuses semantic priors with exploration evidence on the HSG, and performs finite-horizon rollouts on an HSG-based simulator to explicitly estimate the long-term expected returns of candidate macro-actions. This enables globally consistent decisions and reduces redundant backtracking. Extensive experiments in high-fidelity simulation environments across multiple tasks and datasets demonstrate that our method outperforms existing state-of-the-art methods, particularly in long-distance scenarios, where our approach improves SR and SPL by an average of 9.4\% and 5.0\%, respectively.

</details>

---

### [[20_Research/Papers/大模型/GaussLite_Online_Task-Conditioned_3D_Gaussian_Splatting_for_Real-Time_Robotic_Mapping|GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping]]

![[assets/2606.30809_figure.png|800]]

- **arXiv**: [2606.30809](https://arxiv.org/abs/2606.30809)
- **PDF**: https://arxiv.org/pdf/2606.30809
- **详细分析**: [[20_Research/Papers/大模型/GaussLite_Online_Task-Conditioned_3D_Gaussian_Splatting_for_Real-Time_Robotic_Mapping|GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping]]
- **作者**: Annika Thomas, Mason Peterson, Jonathan P. How
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《GaussLite: Online Task-Conditioned 3D Gaussian Splatting for Real-Time Robotic Mapping》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing 3D Gaussian Splatting (3DGS) systems distribute representation capacity uniformly across a scene, ignoring the fact that many downstream robotic tasks engage only a fraction of the reconstructed geometry. This causes valuable onboard compute to be allocated towards optimizing irrelevant parts of the scene, either limiting online capacity or under-optimizing the most relevant parts of the scene. We introduce GaussLite, a task-driven 3DGS mapping system that conditions its representation density on a natural-language task specification. Given a posed RGB-D stream and a task such as "prepare to pick up the object on the desk," GaussLite uses a one-shot LLM parser to extract target and anchor objects, which are grounded per-frame by an open-vocabulary detector and segmented to produce per-pixel relevance masks in real time. The mapper allocates seeding density, gradient flow and scaling by task relevance. At matched Gaussian budget and real-time mapping at 4 Hz on resource-constrained hardware, GaussLite outperforms baselines on ROI PSNR on the Replica Dataset by an average +2.72 dB and on a real-hardware demonstration in indoor and outdoor settings by +2.23 dB. We further show that two task-specialized agents' maps can be fused into a single shared map via per-voxel voting on active-optimization counts in real time, outperforming concatenation by +3.42 dB while only sharing an average 7.08% of the map.

</details>

---
