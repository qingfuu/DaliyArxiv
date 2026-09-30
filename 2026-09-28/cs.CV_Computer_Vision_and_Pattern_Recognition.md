# cs.CV | Computer Vision and Pattern Recognition | 2026-09-28

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/SatNav_A_Scalable_Benchmark_for_Long-Horizon_UAV_Vision-Language_Navigation_from_Satellite_Imagery|SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery]]

![[assets/2609.31507_figure.png|800]]

- **arXiv**: [2609.31507](https://arxiv.org/abs/2609.31507)
- **PDF**: https://arxiv.org/pdf/2609.31507
- **详细分析**: [[20_Research/Papers/具身智能/SatNav_A_Scalable_Benchmark_for_Long-Horizon_UAV_Vision-Language_Navigation_from_Satellite_Imagery|SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery]]
- **作者**: Jiajun Jiang, Chunliang Hua, Zichun Chen, Yanxing Wu, Zeyuan Yang, Jie Song, Xiao Hu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《SatNav: A Scalable Benchmark for Long-Horizon UAV Vision-Language Navigation from Satellite Imagery》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Urban uncrewed aerial vehicle (UAV) vision-language navigation (VLN) requires agents to follow instructions across extended urban spaces, inherently demanding long-term memory and geospatial grounding. However, scaling existing benchmarks remains difficult because of their reliance on costly reconstructed 3D assets, limiting geographic diversity and episode scale. To address this, we introduce SatNav, a scalable, long-horizon UAV VLN benchmark built from high-resolution satellite imagery. SatNav targets city-level navigation missions and uses satellite crops as approximations of UAV nadir views for visual observations. Through an automated cue-to-episode pipeline, SatNav constructs 118K episodes from 59 scenes across 18 cities, with an average trajectory length of 379 m. To stress-test long-horizon memory and geospatial reasoning, SatNav defines three task families: Boundary, Landmark, and Route, targeting loop progress tracking, landmark-based spatial grounding, and route following with counting cues. Benchmarking classical VLN agents and recent agents based on large vision-language models (LVLMs) on SatNav shows that city-scale navigation remains challenging. We further introduce SwiftVLN, a modular framework with switchable memory components, and conduct systematic memory-design ablations. Finally, satellite-to-UAV transfer experiments show that satellite-trained navigation models can operate on real-flight UAV observations, showing the practical relevance of SatNav. Our project page: https://eku127.github.io/SatNav/

</details>

---

### [[20_Research/Papers/机器人/Vision-Based_6-DoF_Grasp_Pose_Estimation_for_Robot_Cloth_Unfolding|Vision-Based 6-DoF Grasp Pose Estimation for Robot Cloth Unfolding]]

![[assets/2609.31452_figure.png|800]]

- **arXiv**: [2609.31452](https://arxiv.org/abs/2609.31452)
- **PDF**: https://arxiv.org/pdf/2609.31452
- **详细分析**: [[20_Research/Papers/机器人/Vision-Based_6-DoF_Grasp_Pose_Estimation_for_Robot_Cloth_Unfolding|Vision-Based 6-DoF Grasp Pose Estimation for Robot Cloth Unfolding]]
- **作者**: Domen Tabernik, Peter Nimac, Jan Jerićević, Danijel Skočaj, Andrej Gams
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Vision-Based 6-DoF Grasp Pose Estimation for Robot Cloth Unfolding》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CeDiRNet, DenseRegNet, LocNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cloth manipulation is a challenging task due to the deformable and high-dimensional nature of cloth, which leads to complex interaction dynamics and perceptual ambiguity arising from frequent occlusions of critical visual cues such as folds, edges, and grasp points. In this work, we tackle cloth unfolding using a regrasping-in-the-air strategy, where one manipulator holds the cloth while the other grasps it at an optimally selected point to unfold it. To this end, we propose CeDiRNet-6DoF, a deep learning framework that jointly predicts effective grasp points and the complete 6-DoF grasp pose from the observed cloth configuration. By integrating dense 3D grasp regression with segmentation and sine-cosine-encoded Euler angles, the proposed method reliably estimates the grasp configuration that maximizes the unfolded cloth area. We extensively evaluated CeDiRNet-6DoF on a bimanual robotic setup within the ICRA 2024 Cloth Competition framework, achieving state-of-the-art performance. An ablation study further validates the benefits of key design components, including joint segmentation, background randomization, and image cropping. These results establish CeDiRNet-6DoF as a robust and versatile foundation for reliable robotic cloth manipulation in unstructured environments.

</details>

---

### [[20_Research/Papers/具身智能/InternW0-$Δ$_A_World_Action_Model_Bridging_Predictive_Dynamics_and_Actions_with_20K+_Hours_of_Open_Data|InternW0-$Δ$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data]]

![[assets/2609.31394_figure.png|800]]

- **arXiv**: [2609.31394](https://arxiv.org/abs/2609.31394)
- **PDF**: https://arxiv.org/pdf/2609.31394
- **详细分析**: [[20_Research/Papers/具身智能/InternW0-$Δ$_A_World_Action_Model_Bridging_Predictive_Dynamics_and_Actions_with_20K+_Hours_of_Open_Data|InternW0-$Δ$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data]]
- **作者**: Xingyu Miao, Zizun Li, Baole Fang, Kaiwen Song, Tenghui Wang, Hanxue Zhang, Yating Wang, Xudong Li, Yuping He, Xueyuan Wei, Chao Gao, Xijie Yang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《InternW0-$Δ$: A World Action Model Bridging Predictive Dynamics and Actions with 20K+ Hours of Open Data》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ActionNet, AgiBotWorld, EBench, InternVLA, LingBot-VLA, Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) jointly model visual dynamics and action generation for generalist robot manipulation. A central challenge is to integrate priors from large-scale pretrained models---including visual dynamics, scene semantics, geometry, and motion---into a unified framework for robot action generation. We introduce InternW0-$Δ$, a unified WAM pretrained on a heterogeneous corpus that outperforms prior methods across simulation benchmarks and real-robot platforms. InternW0-$Δ$ combines pretrained visual dynamics, scene-level semantics, 4D geometric and motion priors, and action generation within a Mixture-of-Transformers (MoT) framework. A pretrained video expert and an action expert interact under semantic guidance from a frozen VLM, while a pretrained 4D foundation model injects geometric and motion priors through training-only distillation. We further introduce Causal Imprint, which learns future-relevant scene changes from training-only future supervision and provides predictive representations directly to the action expert without future-video rollout at inference. For large-scale joint training, we construct a heterogeneous corpus of robot demonstrations, UMI data, egocentric human demonstrations, and Ego2Robot data, curated and aligned under a common state-action representation. The resulting corpus contains over 20K hours of processed training data, to our knowledge the largest open-source corpus of its kind. We pretrain InternW0-$Δ$ on this corpus and demonstrate strong performance across simulation benchmarks and real-robot platforms. We will open source the training code, model weights, infrastructure, data-processing pipeline, and processed data where licenses permit. Project page: https://internrobotics.github.io/InternW0-Delta/

</details>

---

### [[20_Research/Papers/机器人/Enabling_a_Unified_Cross-Domain_Representation_for_Two-Finger_Gripper_Manipulation_via_Interaction-Centric_Modeling|Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling]]

![[assets/2609.31207_figure.png|800]]

- **arXiv**: [2609.31207](https://arxiv.org/abs/2609.31207)
- **PDF**: https://arxiv.org/pdf/2609.31207
- **详细分析**: [[20_Research/Papers/机器人/Enabling_a_Unified_Cross-Domain_Representation_for_Two-Finger_Gripper_Manipulation_via_Interaction-Centric_Modeling|Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling]]
- **作者**: Guanlin Li, Shifeng Bao, Yihan Zhao, Haitao Shen, Haoyang Li, Chen Zhao, Tong Yang, Jie Tang, Jing Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Enabling a Unified Cross-Domain Representation for Two-Finger Gripper Manipulation via Interaction-Centric Modeling》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Achieving robust cross-embodiment generalization in imitation learning demands overcoming a critical representation flaw that inextricably entangles task semantics with hardware-specific visual geometry. We propose an interaction-centric framework that leverages the shared structure of two-finger grippers via a parameterized universal gripper abstraction, yielding a canonical gripper-frame representation. Given language and RGB-D observations, a VLM infers the subtask and grounds an interaction triplet (gripper, held, target), while SAM~2.1 tracks masks to reduce VLM queries. We design concise hybrid features that combine target/collision artificial potential fields for global guidance with segmented gripper-frame point clouds for local geometry, and use a Flow-Matching Transformer to predict smooth 7-DoF action chunks. Experiments in simulation and real-world tasks demonstrate that ours is the first imitation learning approach to simultaneously achieve competitive benchmark scores and extreme cross-embodiment/cross-viewpoint zero-shot sim-to-real transfer to completely distinct, heterogeneous robot platforms.

</details>

---

### [[20_Research/Papers/机器人/TRACKGRAPH_Online_Open-Vocabulary_3D_Scene_Graphs_via_Image-Space_Tracking|TRACKGRAPH: Online Open-Vocabulary 3D Scene Graphs via Image-Space Tracking]]

![[assets/2609.31005_figure.png|800]]

- **arXiv**: [2609.31005](https://arxiv.org/abs/2609.31005)
- **PDF**: https://arxiv.org/pdf/2609.31005
- **详细分析**: [[20_Research/Papers/机器人/TRACKGRAPH_Online_Open-Vocabulary_3D_Scene_Graphs_via_Image-Space_Tracking|TRACKGRAPH: Online Open-Vocabulary 3D Scene Graphs via Image-Space Tracking]]
- **作者**: Peder Borge Hellesylt, Albert Gassol Puigjaner, Kostas Alexis, Annette Stahl
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Multimodal, ComputerVision, Systems

#### 研究背景与动机

《TRACKGRAPH: Online Open-Vocabulary 3D Scene Graphs via Image-Space Tracking》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-vocabulary 3D maps enable robots to reason about previously unknown environments using natural language. However, existing systems typically segment every incoming image, associate detections with persistent 3D segments, and frequently perform costly Vision-Language (VL) inference. We present TRACKGRAPH, an online open-vocabulary system that maintains short-term 2D mask identity directly in the image stream before fusing segments into 3D. FastSAM masks and CLIP features are computed at sparse keyframes, while dense DINOv3 features are used to propagate masks at a high rate in between. The resulting tracked masks are fused into a class-agnostic 3D segment layer within a hierarchical scene graph, with 3D association handling tracking interruptions and long-term revisits. Compact multi-view CLIP embeddings enable open-vocabulary retrieval. Across Replica, ScanNet++, and HM3D, TRACKGRAPH achieves competitive open-vocabulary segmentation and retrieval against state-of-the-art mapping methods, including the highest synonym frequency on Replica (0.50). On the same NVIDIA A100, it is 1.7x faster and uses 3.3x less GPU memory than ViT-H OVI-MAP. Real-world quadruped deployments demonstrate onboard scene graph construction and object search at 7.5Hz, while recorded drone data is used to test the method under aerial viewpoints.

</details>

---

### [[20_Research/Papers/大模型/MM-VeriAgent_Learning_to_Use_Extensive_Tools_to_Verify_Multimodal_Misinformation_with_Reinforcement_Learning|MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning]]

![[assets/2609.30698_figure.png|800]]

- **arXiv**: [2609.30698](https://arxiv.org/abs/2609.30698)
- **PDF**: https://arxiv.org/pdf/2609.30698
- **详细分析**: [[20_Research/Papers/大模型/MM-VeriAgent_Learning_to_Use_Extensive_Tools_to_Verify_Multimodal_Misinformation_with_Reinforcement_Learning|MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning]]
- **作者**: Peipei Li, Shuhan Xia, Shengyang Liu, Zekun Li, Ran He
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.4（加权：大模型 0.6，强化学习 0.8）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《MM-VeriAgent: Learning to Use Extensive Tools to Verify Multimodal Misinformation with Reinforcement Learning》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CapRL, MMFakeBench, MVSS-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-world multimodal misinformation often involves mixed forgery sources, requiring sample-specific detection strategies. Existing tool-augmented methods rely on predefined workflows or inference-time planning, limiting adaptability or increasing inference cost. To address this issue, we introduce \textbf{MM-VeriAgent}, which learns to verify mixed-source multimodal misinformation with tools. We first build \textbf{MM-VeriTools}, a specialized toolkit for misinformation detection agents. By benchmarking various candidate models and methods on the sub-tasks required by mixed-source detection, we select the strongest for textual, visual, and cross-modal forgery analysis and encapsulate them as callable tools with a unified interface. On top of this toolkit, we train the LVLM agent with reinforcement learning to teach it how to use these tools to better solve mixed-source detection. Since many of the tools are specialized models whose online execution at every rollout severely limits RL efficiency, we further introduce \textbf{Tool-Execution Cache}, which pre-executes candidate tool calls and reuses their cached outputs during training. This preserves multi-step rollouts while reducing online tool execution, largely improving the training efficiency.Experiments on MMFakeBench demonstrate substantial accuracy gains over the base model without explicit tool search at inference time. Ablation and efficiency analyses further validate the learned tool-use policy and show that Tool-Execution Cache reduces online tool executions during training.

</details>

---

### [[20_Research/Papers/强化学习/StarWM_Self-Supervised_Trained_Attention_Routing_for_Robust_World_Models|StarWM: Self-Supervised Trained Attention Routing for Robust World Models]]

![[assets/2609.30667_figure.png|800]]

- **arXiv**: [2609.30667](https://arxiv.org/abs/2609.30667)
- **PDF**: https://arxiv.org/pdf/2609.30667
- **详细分析**: [[20_Research/Papers/强化学习/StarWM_Self-Supervised_Trained_Attention_Routing_for_Robust_World_Models|StarWM: Self-Supervised Trained Attention Routing for Robust World Models]]
- **作者**: Zeqiang Zhang, Fabian Wurzberger, Maximilian Otte, Daniel Schmid, Sebastian Gottwald, Arne Peter Raulf, Daniel Alexander Braun
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《StarWM: Self-Supervised Trained Attention Routing for Robust World Models》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robust world model must strike the balance between faithfully capturing environmental dynamics and abstracting away from irrelevant content. While reconstruction-based world models ensure faithful supervision, they misallocate representational capacity by pixel area rather than dynamics relevance for visual tasks, which can cause task-irrelevant content to dominate the learned representation. Alternatively, reconstruction-free methods avoid this bias but risk discarding possibly relevant information. We propose StarWM, which uses a cross-attention module trained on self-supervised dynamics to decide where reconstruction applies. A dual-stream decoder then restricts reconstruction to the attended regions, with stop-gradient barriers preventing interference between the two objectives. These components allows reconstruction to supervise the visual content of attended regions without contaminating the latent with non-predictive information. On DeepMind Control with dynamic video backgrounds, default (reward-free) StarWM achieves the strongest performance under random-frame distractors and substantially outperforms reconstruction-based baselines under sequential video. In addition, its reward-augmented variant matches or exceeds reconstruction-free methods on sequential video, achieving the highest overall return across all distractor regimes. Mechanistic probing confirms StarWM preserves state attributes with near-perfect fidelity through long-horizon imagination while systematically discarding distractors.

</details>

---

### [[20_Research/Papers/具身智能/FRESHLATENT_Channel-Aware_Latent_Adaptation_for_Resource-Constrained_Embodied_VLM_Perception|FRESHLATENT: Channel-Aware Latent Adaptation for Resource-Constrained Embodied VLM Perception]]

![[assets/2609.30629_figure.png|800]]

- **arXiv**: [2609.30629](https://arxiv.org/abs/2609.30629)
- **PDF**: https://arxiv.org/pdf/2609.30629
- **详细分析**: [[20_Research/Papers/具身智能/FRESHLATENT_Channel-Aware_Latent_Adaptation_for_Resource-Constrained_Embodied_VLM_Perception|FRESHLATENT: Channel-Aware Latent Adaptation for Resource-Constrained Embodied VLM Perception]]
- **作者**: Rajat Bhattacharjya, Minwoo Kim, Arnab Sarkar, Tamoghno Das, Sing-Yao Wu, Eli Bozorgzadeh, Marco Levorato, Nikil Dutt
- **cs 子类**: cs.CV, cs.DC, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.2，大模型 0.6，机器人 0.3）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《FRESHLATENT: Channel-Aware Latent Adaptation for Resource-Constrained Embodied VLM Perception》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FFMNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mission-critical UAVs increasingly rely on split vision-language model (VLM) perception under tight onboard-resource and wireless-communication constraints. However, corruption of transmitted intermediate features creates a deployment mismatch for clean-trained split interfaces, while stronger channel-aware codecs can impose substantial onboard cost. We present FreshLatent, a lightweight channel-aware latent adapter that trains a power-normalized encoder-decoder through wireless corruption while keeping the surrounding VLM frozen. We formulate deployment around a mission-conditioned perception requirement and embedded interface cost, linking channel quality and communication budget to the operating conditions under which perception remains usable. At 0 dB and the tightest communication budget, FreshLatent improves gIoU and cIoU over clean split compression by 20.79 and 20.87 points, respectively. At the most adverse evaluated SNR (0 dB), across all three communication budgets, FreshLatent recovers 63.5-69.1% of the gIoU improvement achieved by a much heavier, range-trained feature-JSCC codec. On an NVIDIA Jetson AGX Xavier in 10-W mode, FreshLatent uses 37-40x fewer encoder parameters, 7.7-9.9x lower edge-interface latency, and 8.8-10.0x lower edge-interface energy than the heavier codec. Together, these results show that lightweight channel-aware adaptation can recover a substantial fraction of the robustness of a much larger communication interface while broadening quality-valid operation under constrained wireless conditions.

</details>

---

### [[20_Research/Papers/强化学习/MVAgent_Multi-Agent_Video_Generation_via_Consistent_Condition_Construction_and_Shot-Level_Policy_Optimization|MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization]]

![[assets/2609.30609_figure.png|800]]

- **arXiv**: [2609.30609](https://arxiv.org/abs/2609.30609)
- **PDF**: https://arxiv.org/pdf/2609.30609
- **详细分析**: [[20_Research/Papers/强化学习/MVAgent_Multi-Agent_Video_Generation_via_Consistent_Condition_Construction_and_Shot-Level_Policy_Optimization|MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization]]
- **作者**: Xiangyu Kong, Wenjie Zhou, Fengping Tian, Lihua Fang, Haoqin Sun, Chenyang Lyu, Longyue Wang, Weihua Luo
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，强化学习 0.8）
- **关联关键词**: Agent, RL, ComputerVision

#### 研究背景与动机

《MVAgent: Multi-Agent Video Generation via Consistent Condition Construction and Shot-Level Policy Optimization》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ViMax-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-shot agentic video generation requires consistent character appearance, stable spatial layout across camera angles, and continuous character state between shots. When every shot is a separate request to a frozen generator, repeated text does not determine appearance, layout or state. We therefore recast the problem as condition construction and present MVAgent, a multi-agent pipeline whose agents collaborate through typed conditioning inputs. Because an environment image shows one viewpoint, a Spatial Grounding agent samples views from generated camera-traversal clips and anchors each shot to the view matching its framing. As generated shots drift from the plan, an Observer records how each shot ends in a continuity memory, from which a Transition agent builds character action and spatial references for the next shot. An Orchestrator composes these inputs into each request. Since a request reveals its effect only after rendering, we train it by agentic reinforcement learning with Trunk-GDPO, which compares rendered candidates at every shot rather than once per video and continues the best as the trunk. With generator and judges frozen, MVAgent attains the highest cross-shot consistency and narrative-planning quality among the compared methods on ViMax-Bench and is preferred over the strongest agentic baseline in human evaluation.

</details>

---

### [[20_Research/Papers/机器人/VkVIO_Cross-platform_GPU_Acceleration_for_Visual-Inertial_Odometry_with_Vulkan|VkVIO: Cross-platform GPU Acceleration for Visual-Inertial Odometry with Vulkan]]

![[assets/2609.30459_figure.png|800]]

- **arXiv**: [2609.30459](https://arxiv.org/abs/2609.30459)
- **PDF**: https://arxiv.org/pdf/2609.30459
- **详细分析**: [[20_Research/Papers/机器人/VkVIO_Cross-platform_GPU_Acceleration_for_Visual-Inertial_Odometry_with_Vulkan|VkVIO: Cross-platform GPU Acceleration for Visual-Inertial Odometry with Vulkan]]
- **作者**: Ole Hoffmann, Mateo de Mayo, Daniel Cremers
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《VkVIO: Cross-platform GPU Acceleration for Visual-Inertial Odometry with Vulkan》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perception in robotics and XR fundamentally relies on good state estimation. Visual-inertial odometry (VIO) and Simultaneous Localization and Mapping (VI-SLAM) are proven ways of achieving this goal in a cost-effective and accurate manner. Efficiency in these systems allows for smaller, cooler, and lighter devices. GPU acceleration is a natural approach for reducing latency, thanks to their wide availability in platforms like embedded computers, mobile phones, and XR headsets. However, previous works in the literature have limited themselves to the use of CUDA for this task, significantly reducing deployment options to a single vendor. We instead leverage the vendor-agnostic Vulkan API, originally designed for the strict performance requirements of 3D graphics applications. In this work, we present VkVIO, the first, to the best of our knowledge, cross-platform GPU-accelerated VIO method. We provide state-of-the-art accuracy with causal estimates required for real-time operation. We deploy VkVIO on a diverse range of devices spanning a workstation, a laptop, and an extremely inexpensive single-board computer, while outperforming CUDA-based systems on the same hardware. VkVIO enables possibilities for low-latency, low-power, and low-cost VIO in robotics and XR.

</details>

---
