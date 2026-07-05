# cs.CV | Computer Vision and Pattern Recognition | 2026-07-03

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/具身智能/Embodied.cpp_A_Portable_Inference_Runtime_of_Embodied_AI_Models_on_Heterogeneous_Robots|Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots]]

![[assets/2607.02501_figure.png|800]]

- **arXiv**: [2607.02501](https://arxiv.org/abs/2607.02501)
- **PDF**: https://arxiv.org/pdf/2607.02501
- **详细分析**: [[20_Research/Papers/具身智能/Embodied.cpp_A_Portable_Inference_Runtime_of_Embodied_AI_Models_on_Heterogeneous_Robots|Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots]]
- **作者**: Ling Xu, Chuyu Han, Borui Li, Hao Wu, Shiqi Jiang, Ting Cao, Chuanyou Li, Sheng Zhong, Shuai Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 3.3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Embodied.cpp: A Portable Inference Runtime of Embodied AI Models on Heterogeneous Robots》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DAM-VLA, GeneralVLA, HY-VLA, MuseVLA, OpenVLA, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied AI models now span vision-language-action (VLA) models and world-action models (WAMs), but practical deployment remains fragmented across model-specific Python stacks, backend assumptions, and robot-side glue code, especially on heterogeneous edge devices. Existing inference runtimes are designed mainly for request-response serving and therefore do not satisfy the runtime contract of embodied deployment: multi-rate execution inside closed-loop control, latency-first batch-1 inference on heterogeneous hardware, and extensible embodied interfaces beyond fixed token I/O. We present Embodied.cpp, a portable C++ inference runtime for embodied models. Based on an architectural analysis of representative VLA models and WAMs, Embodied.cpp captures a shared execution path and organizes it into five layers: input adapters, sequence builders, backbone execution, head plugins, and deployment adapters. The runtime provides modular multi-rate execution, latency-first fused inference, and extensible operator and I/O support, enabling deployment across heterogeneous devices, robots, and simulators through one backend abstraction. We evaluate Embodied.cpp on two VLA models, HY-VLA and pi0.5, and on a preliminary WAM benchmark using a LingBot-VA Transformer block. The VLA deployments achieve successful closed-loop execution with 100.0% and 91.0% task success rates, respectively. The WAM benchmark reduces block memory from 312.2 MiB to 88.1 MiB. These results show that Embodied.cpp improves deployment efficiency while preserving high accuracy across diverse embodied model architectures.

</details>

---

### [[20_Research/Papers/具身智能/Seek_to_Segment_Active_Perception_for_Panoramic_Referring_Segmentation|Seek to Segment: Active Perception for Panoramic Referring Segmentation]]

![[assets/2607.02497_figure.png|800]]

- **arXiv**: [2607.02497](https://arxiv.org/abs/2607.02497)
- **PDF**: https://arxiv.org/pdf/2607.02497
- **详细分析**: [[20_Research/Papers/具身智能/Seek_to_Segment_Active_Perception_for_Panoramic_Referring_Segmentation|Seek to Segment: Active Perception for Panoramic Referring Segmentation]]
- **作者**: Song Tang, Shuming Hu, Xincheng Shuai, Henghui Ding, Yu-Gang Jiang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.5，强化学习 0.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Seek to Segment: Active Perception for Panoramic Referring Segmentation》归入 具身智能、大模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing referring segmentation models passively process static images captured from fixed perspectives, limiting their applicability in Embodied AI, where agents must perform active perception in the continuous 360$^\circ$ environments. To bridge this gap, we introduce a novel task: Active Panoramic Referring Segmentation (APRS). In this setting, an agent is required to adjust its viewing direction ($Δθ, Δφ$) to explore the 360$^\circ$ environment, seeking the object specified by a user instruction for segmentation. To tackle this challenging task, we propose PanoSeeker, a memory-augmented agent for efficient APRS. Rather than relying on heuristic scanning, PanoSeeker integrates a Vision-Language Model (VLM) with EgoSphere, an explicit spatial visual memory. By progressively integrating sequential local observations into a unified 360$^\circ$ representation, EgoSphere enables the agent to plan efficient and non-redundant search trajectories. Once the target is found, the agent performs active viewpoint alignment and outputs the segmentation mask. Furthermore, we curate an expert-annotated search trajectory dataset with memory timelines for Supervised Fine-Tuning, followed by Reinforcement Learning post-training to explicitly optimize PanoSeeker's exploration efficiency. Extensive experiments on our newly established APRS benchmark demonstrate that PanoSeeker achieves superior search efficiency and segmentation accuracy, significantly outperforming adapted state-of-the-art baselines.

</details>

---

### [[20_Research/Papers/具身智能/EAGLE-360_Embodied_Active_Global-to-Local_Exploration_in_360$^_circ$|EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$]]

![[assets/2607.02479_figure.png|800]]

- **arXiv**: [2607.02479](https://arxiv.org/abs/2607.02479)
- **PDF**: https://arxiv.org/pdf/2607.02479
- **详细分析**: [[20_Research/Papers/具身智能/EAGLE-360_Embodied_Active_Global-to-Local_Exploration_in_360$^_circ$|EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$]]
- **作者**: Jingtao Xu, Zizhuo Lin, Jianwen Sun, Yi Yang, Yawei Luo
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 大模型
- **相关性评分**: 1.5（加权：具身智能 1.2，大模型 0.1，强化学习 0.2）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《EAGLE-360: Embodied Active Global-to-Local Exploration in 360$^\circ$》归入 具身智能、强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OSR-Bench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Multimodal Large Language Models (MLLMs) have demonstrated exceptional capabilities in standard visual understanding, adapting them for active visual search in 360$^\circ$ panoramic environments exposes fundamental limitations. Specifically, standard MLLMs struggle to effectively model inherent panoramic properties, such as severe polar distortion and continuous cylindrical topologies, which significantly degrades target detection accuracy. Consequently, existing panoramic search methods attempt to compensate by relying heavily on fragmented local viewpoints. Burdened by rigid initialization and a lack of global panoramic priors, these approaches suffer from myopic, inefficient exploration and struggle with robust error recovery when targets are out of view. To overcome these challenges, we propose EAGLE-360, a novel Embodied Active Global-to-Local Exploration framework. Rather than performing exhaustive local searches, EAGLE-360 leverages global priors to establish an initial holistic perspective, iteratively reasoning and progressively narrowing the search space. Architecturally, we adapt RoPE Rolling, a coordinate-shifting positional encoding mechanism, to seamlessly model the continuous topologies of panoramas. To facilitate this paradigm, we construct the large-scale EAGLE-360 dataset, comprising 14,000+ 4K panoramas and 70,000+ rounds of high-quality VQA dialogues. By employing a training pipeline that integrates Supervised Fine-Tuning (SFT) with Group Relative Policy Optimization (GRPO), we effectively elicit complex spatial reasoning and tool-calling capabilities. Extensive experiments demonstrate that EAGLE-360 establishes a new state-of-the-art for 360$^\circ$ visual search, achieving nearly an 8-fold increase in accuracy over the base model while significantly enhancing exploration efficiency.

</details>

---

### [[20_Research/Papers/具身智能/Learning_to_Evolve_Scenes_Reasoning_about_Human_Activities_with_Scene_Graphs|Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs]]

![[assets/2607.02425_figure.png|800]]

- **arXiv**: [2607.02425](https://arxiv.org/abs/2607.02425)
- **PDF**: https://arxiv.org/pdf/2607.02425
- **详细分析**: [[20_Research/Papers/具身智能/Learning_to_Evolve_Scenes_Reasoning_about_Human_Activities_with_Scene_Graphs|Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs]]
- **作者**: Francesca Pistilli, Simone Alberto Peirone, Giuseppe Averta
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 0.6（加权：具身智能 0.6）
- **关联关键词**: EmbodiedAI, ComputerVision

#### 研究背景与动机

《Learning to Evolve Scenes: Reasoning about Human Activities with Scene Graphs》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EXPLORE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding human behavior while interacting with the surrounding world is crucial for many applications of embodied AI. First-person videos are particularly informative for this problem, as they well capture how activities reshape the scene over time. However, existing approaches often rely on implicit visual or language-aligned representations, disregarding structured reasoning over the scene dynamic. We argue that explicit, compositional and editable representations of human-environment interactions can play a crucial role for rich grounded activity understanding. To this end, we introduce SG-Ego, a large scale annotation set extending Ego4D with spatio-temporal scene graphs, where relations triplets are consolidated over time into explicit time-evolving descriptions of the scene state. To reason over this representation, we propose GLEN, a graph-based model that operates over scene graph sequences to both align them with textual actions and model their temporal evolution. In addition, we formulate the activity-driven graph-edit forecasting (A-GEF) problem, a novel task that casts scene dynamics as a sequence of structured transformations conditioned on ongoing actions, enabling explicit reasoning about how scenes change over time. We validate our approach across multiple downstream tasks, spanning retrieval benchmarks as EgoMCQ and EgoCVR, as well as long-horizon reasoning benchmarks as EXPLORE-Bench and the newly introduced A-GEF. GLEN achieves strong results compared to raw video baselines and it excels in reasoning settings, typically addressed only with MLLMs, while enabling controllable and structured predictions of scene dynamics driven by human activities. We believe our results establish spatio-temporal scene graphs, together with models that reason over them, as strong compositional and interpretable representations for video understanding and potentially beyond.

</details>

---

### [[20_Research/Papers/具身智能/LIME_Learning_Intent-aware_Camera_Motion_from_Egocentric_Video|LIME: Learning Intent-aware Camera Motion from Egocentric Video]]

![[assets/2607.02417_figure.jpg|800]]

- **arXiv**: [2607.02417](https://arxiv.org/abs/2607.02417)
- **PDF**: https://arxiv.org/pdf/2607.02417
- **详细分析**: [[20_Research/Papers/具身智能/LIME_Learning_Intent-aware_Camera_Motion_from_Egocentric_Video|LIME: Learning Intent-aware Camera Motion from Egocentric Video]]
- **作者**: Boyang Sun, Jiajie Li, Yung-Hsu Yang, Chenyangguang Zhang, Tim Engelbracht, Sunghwan Hong, Cesar Cadena, Marc Pollefeys, Hermann Blum
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《LIME: Learning Intent-aware Camera Motion from Egocentric Video》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：E3VS-Bench, EQA, EXPRESS-Bench, EmbodiedQA, GOAT-Bench, HM-EQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots often need to move their camera before they can act: to inspect an object, reveal an occluded region, or obtain a view that responds to a user's intent. While vision-language navigation translates instructions to base motion and vision-language-action policies map instructions to manipulation actions, language-conditioned camera motion remains comparatively underexplored as a first-class action. We formulate language-conditioned camera motion generation: given a current RGB observation and a free-form natural-language intent, predict a relative target camera pose for the next observation. This task is inherently non-trivial: viewpoint changes are driven by latent perceptual intentions, and a valid motion may operate at different semantic granularity, from entering a room to looking around a corner, inspecting a visible object, or revealing an occluded detail. To model this structure, we mine multi-intention camera-motion supervision from egocentric video, pairing plausible intents and observation-gain descriptions with relative SE(3) target poses. We propose LIME, a vision-language camera-motion generator that combines an auto-regressive observation-gain output with a continuous flow-matching pose head. This design lets the model jointly predict what the next view should reveal while representing multi-hypothesis target views. Across experiments and downstream robotic tasks, we show that LIME can learn to actively choose camera poses from passive human video, turning ordinary egocentric recordings into supervision for intent-aware active perception.

</details>

---

### [[20_Research/Papers/具身智能/The_Moving_Eye_Enhancing_VLA_Spatial_Generalization_via_Hybrid_Dynamic_Data_Collection|The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection]]

![[assets/2607.02322_figure.jpg|800]]

- **arXiv**: [2607.02322](https://arxiv.org/abs/2607.02322)
- **PDF**: https://arxiv.org/pdf/2607.02322
- **详细分析**: [[20_Research/Papers/具身智能/The_Moving_Eye_Enhancing_VLA_Spatial_Generalization_via_Hybrid_Dynamic_Data_Collection|The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection]]
- **作者**: Jincheng Tang, Yilong Zhu, Zhengyuan Xie, Jiang-Jiang Liu, Jiaxing Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《The Moving Eye: Enhancing VLA Spatial Generalization via Hybrid Dynamic Data Collection》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GeoAware-VLA, OG-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown remarkable promise in generalized robotic manipulation. However, their spatial generalization remains fragile. We argue that simply increasing the number of viewpoints is insufficient. Models often fall into the trap of Shortcut Learning, latching onto spurious correlations (e.g., fixed relative poses between objects or between the camera and robot base) rather than learning true spatial relationships. In this work, we propose a data-centric solution to enhance VLA spatial generalization. We utilize a dual-arm setup where one arm performs manipulation while the other serves as a mobile environmental camera. We systematically evaluate three data distribution patterns: Fixed, Multi-Fixed, and Moving Views. Our findings reveal that a hybrid strategy, combining continuous camera motion with diverse static viewpoints, yields the best performance by substantially reducing spurious correlations while maintaining training stability. Our experiments demonstrate that this strategy mitigates spurious correlations, enabling VLAs to generalize to unseen camera poses and object configurations where simply adding more static viewpoints fails. Crucially, we reveal that the susceptibility to shortcut learning and the struggle with spatial generalization are universal characteristics shared across diverse architectures. Consequently, all evaluated models (ACT, Diffusion, and VLA models including Pi0 and Gr00t) benefit significantly from our mixed data strategy.

</details>

---

### [[20_Research/Papers/具身智能/Real-Time_Visual_Intelligence_on_Low-Cost_UAVs_A_Modular_Approach_for_Tracking,_Scanning,_and_Navigation|Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation]]

![[assets/2607.02298_first_page.png|800]]

- **arXiv**: [2607.02298](https://arxiv.org/abs/2607.02298)
- **PDF**: https://arxiv.org/pdf/2607.02298
- **详细分析**: [[20_Research/Papers/具身智能/Real-Time_Visual_Intelligence_on_Low-Cost_UAVs_A_Modular_Approach_for_Tracking,_Scanning,_and_Navigation|Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation]]
- **作者**: Andrei-Marian Ungureanu, Stelian Spînu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Real-Time Visual Intelligence on Low-Cost UAVs: A Modular Approach for Tracking, Scanning, and Navigation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous drones are rapidly transforming modern warfare and civil applications alike. This paper presents the development of an integrated intelligent drone system designed to serve as a personal assistant. Leveraging the DJI Tello drone platform, we implemented a modular architecture that integrates three core artificial intelligence functionalities: facial detection, facial recognition, and depth estimation from monocular vision. A web-based interface enables seamless drone control and real-time video monitoring, while a Python-based server processes visual data and executes inference pipelines using lightweight neural models optimized for embedded systems. Unlike existing commercial solutions, this system emphasizes accessibility, low-cost hardware, and open-source technologies. The system demonstrates robust performance in real-world conditions, including person tracking, indoor scanning, and autonomous line following using virtual sensors. This project validates the applicability of advanced AI techniques in real-time robotic systems and illustrates the feasibility of deploying them on constrained hardware, providing a foundation for future research in autonomous UAVs for military, rescue, and surveillance missions.

</details>

---

### [[20_Research/Papers/世界模型/PWM-ArtGen_Part_World_Model_for_Articulated_Object_Generation|PWM-ArtGen: Part World Model for Articulated Object Generation]]

![[assets/2607.02045_figure.png|800]]

- **arXiv**: [2607.02045](https://arxiv.org/abs/2607.02045)
- **PDF**: https://arxiv.org/pdf/2607.02045
- **详细分析**: [[20_Research/Papers/世界模型/PWM-ArtGen_Part_World_Model_for_Articulated_Object_Generation|PWM-ArtGen: Part World Model for Articulated Object Generation]]
- **作者**: Wentao Zheng, Ancong Wu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《PWM-ArtGen: Part World Model for Articulated Object Generation》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PartNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The key challenge in articulated 3D object generation from a single image is accurately predicting the underlying kinematic structure. Existing methods either infer kinematic parameters directly from a static image that lacks dynamic part-level kinematic relationships, or estimate parameters from visual dynamics generated from a single image, which is prone to accumulated errors of two steps. Moreover, the limited scale and diversity of existing annotated datasets further hinder generalization to complex, real-world objects. To overcome these limitations, we propose to learn the joint distribution of visual dynamics and kinematic parameters. Recognizing that articulated objects can be formulated as dynamic systems, we propose a unified Part World Model called PWM-ArtGen. To leverage unannotated data, this model couples action diffusion and image diffusion with independent diffusion timesteps, which enables visual branch co-training. We further curate a photorealistic dataset of 19.7k part-level image pairs without kinematic annotations, to support co-training. Experiments demonstrate that PWM-ArtGen substantially outperforms existing baselines in the resting state and exhibits strong zero-shot generalization to out-of-distribution objects.

</details>

---

### [[20_Research/Papers/机器人/A_Stereo_Visual_SLAM_System_Using_Object-Level_Motion_Estimation_and_Geometric_Filtering_Based_on_Cross_Disparity|A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity]]

![[assets/2607.02005_figure.png|800]]

- **arXiv**: [2607.02005](https://arxiv.org/abs/2607.02005)
- **PDF**: https://arxiv.org/pdf/2607.02005
- **详细分析**: [[20_Research/Papers/机器人/A_Stereo_Visual_SLAM_System_Using_Object-Level_Motion_Estimation_and_Geometric_Filtering_Based_on_Cross_Disparity|A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity]]
- **作者**: Sujan Kumar Dhali, Bhaskar Dasgupta
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《A Stereo Visual SLAM System Using Object-Level Motion Estimation and Geometric Filtering Based on Cross Disparity》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CenterNet, S2R-DepthNet, SegNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents OCD SLAM, a dynamic stereo visual SLAM framework that extends ORB-SLAM2 by jointly addressing dynamic objects and dynamic features in the scene. Usual visual SLAM systems operating in dynamic environments often fail in the presence of moving objects, due to the static-world assumption used in pose estimation and mapping. To address this predicament, we introduce a novel geometric approach based on the discrepancy between disparity and a newly proposed notion called ``cross disparity'', which exploits both temporal and stereo inconsistency to identify dynamic feature points. Complementary to this feature-level motion analysis, OCD SLAM integrates a 3D object detection module (SMOKE) with Kalman filter-based object tracking to perform object-level motion classification, enabling robust separation of static and dynamic scene elements for accurate pose estimation. The proposed approach has been evaluated on various sequences from the KITTI Odometry and KITTI Raw datasets. Results demonstrate that OCD SLAM achieves significant improvement in trajectory accuracy compared to ORB-SLAM2 and several state-of-the-art dynamic SLAM methods. Ablation studies further demonstrate the effectiveness of the cross disparity module in the KITTI Raw dataset and show that this method is able to detect dynamic features that are missed by the 3D object detection scheme alone.

</details>

---

### [[20_Research/Papers/世界模型/Liquid_Latent_State_Dynamics_for_Interpretable_Turbofan_Degradation_Modeling|Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling]]

![[assets/2607.01986_figure.png|800]]

- **arXiv**: [2607.01986](https://arxiv.org/abs/2607.01986)
- **PDF**: https://arxiv.org/pdf/2607.01986
- **详细分析**: [[20_Research/Papers/世界模型/Liquid_Latent_State_Dynamics_for_Interpretable_Turbofan_Degradation_Modeling|Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling]]
- **作者**: Weizhi Nie, Weijie Wang, Yuting Su
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 0.92（加权：强化学习 0.16，世界模型 0.76）
- **关联关键词**: WorldModel, Systems

#### 研究背景与动机

《Liquid Latent State Dynamics for Interpretable Turbofan Degradation Modeling》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multivariate time-series models for prognostics are often evaluated by point prediction accuracy, yet their internal states rarely expose a coherent degradation process. We study liquid neural networks as latent dynamics models for aircraft engine health monitoring on the C-MAPSS benchmark. The proposed model encodes a history window into a latent state, evolves that state with a liquid transition model, and decodes future sensor observations. To separate health evolution from operating-condition variation, the latent state is factorized into degradation and condition components. Remaining useful life, monotonic risk, and latent-consistency losses supervise the degradation component, while condition prediction and decorrelation losses discourage operating-condition leakage. Across FD001--FD004, the full disentangled model improves overall sensor forecasting RMSE from 0.2438 for a GRU baseline to 0.2266, with the largest gains on the multi-condition subsets FD002 and FD004. The learned degradation state also forms a clearer temporal degradation axis, reaching an average state-speed Spearman correlation of 0.5960. Direct remaining-useful-life regression remains stronger for the GRU baseline, indicating that the proposed representation is currently more effective as an interpretable world model for degradation dynamics than as a calibrated lifetime regressor. These results suggest that liquid latent dynamics can bridge predictive maintenance forecasting and inspectable health-state modeling.

</details>

---

### [[20_Research/Papers/机器人/Robust_Image_Processing_Techniques_for_Construction_Environment_Monitoring_Using_Underwater_Robots|Robust Image Processing Techniques for Construction Environment Monitoring Using Underwater Robots]]

![[assets/2607.01915_first_page.png|800]]

- **arXiv**: [2607.01915](https://arxiv.org/abs/2607.01915)
- **PDF**: https://arxiv.org/pdf/2607.01915
- **详细分析**: [[20_Research/Papers/机器人/Robust_Image_Processing_Techniques_for_Construction_Environment_Monitoring_Using_Underwater_Robots|Robust Image Processing Techniques for Construction Environment Monitoring Using Underwater Robots]]
- **作者**: Seunghee Yun, Geonmo Yang, Juhui Lee, Changbeom Park, Jeahyung Choi, Younggun Cho
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Robust Image Processing Techniques for Construction Environment Monitoring Using Underwater Robots》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper proposes a robust image processing framework for underwater robot-based construction environment monitoring, targeting complex degradations observed in real marine environments. Unlike conventional approaches that mainly consider absorption and backscattering, real underwater imagery is strongly affected by depth-dependent forward scattering blur and particle-induced degradations such as marine snow. To address this, we introduce a staged processing pipeline that sequentially models background degradation via depth-aware forward scattering and foreground degradation using realistic marine snow patterns extracted from real images. The resulting synthetic data are used to retrain an existing Joint-ID network without modifying its architecture, enabling an isolated evaluation of dataset realism. In addition, a lightweight post-processing scheme is applied to enhance contrast and structural clarity. Experiments on real underwater datasets collected in Korean coastal environments demonstrate consistent improvements in visual quality and UIQM scores. The results indicate that explicitly modeling forward scattering and realistic particle effects effectively reduces the synthetic-to-real gap and improves practical applicability in real-world underwater robotic operations.

</details>

---

### [[20_Research/Papers/机器人/DL-SLAM_Enabling_High-Fidelity_Gaussian_Splatting_SLAM_in_Dynamic_Environments_based_on_Dual-Level_Probability|DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability]]

![[assets/2607.01860_figure.png|800]]

- **arXiv**: [2607.01860](https://arxiv.org/abs/2607.01860)
- **PDF**: https://arxiv.org/pdf/2607.01860
- **详细分析**: [[20_Research/Papers/机器人/DL-SLAM_Enabling_High-Fidelity_Gaussian_Splatting_SLAM_in_Dynamic_Environments_based_on_Dual-Level_Probability|DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability]]
- **作者**: Ziheng Xu, Qingfeng Li, Xuefeng Liu, Chen Chen, Jianwei Niu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《DL-SLAM: Enabling High-Fidelity Gaussian Splatting SLAM in Dynamic Environments based on Dual-Level Probability》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in 3D Gaussian Splatting (3DGS) have enabled significant progress in dense dynamic Simultaneous Localization And Mapping (SLAM). Prevailing methods typically discard predefined dynamic objects, ignoring that transiently static objects offer valuable geometric constraints for pose estimation. A recent work attempts to leverage this potential by employing per-pixel uncertainty maps to quantify the magnitude of motion. While this approach enables transiently static objects to enhance pose estimation, it erroneously integrates these objects into the static map, resulting in persistent artifacts. Moreover, its reliance on purely geometric information leads to ambiguous object boundaries in the uncertainty maps. To overcome these limitations, we present DL-SLAM, a monocular Gaussian Splatting SLAM system built upon a novel dual-level probabilistic framework. Our method computes dynamic probability maps by combining semantic and geometric information. These pixel-level probabilities are lifted to 3D and aggregated to derive an object-level dynamic probability for each instance. Object-level probability enables the categorical pruning of dynamic Gaussians, resulting in an artifact-free static map. The static map, in turn, provides a geometrically consistent guidance to refine the pixel-wise probabilities, enhancing their reliability. Experimental results demonstrate that DL-SLAM outperforms existing approaches, improving tracking accuracy by up to 13\% while generating high-fidelity semantic maps.

</details>

---

### [[20_Research/Papers/大模型/LLM-Empowered_Multimodal_Fusion_Framework_for_Autonomous_Driving_Semantic_Enhancement_and_Channel-Adaptive_Design|LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design]]

![[assets/2607.01772_figure.png|800]]

- **arXiv**: [2607.01772](https://arxiv.org/abs/2607.01772)
- **PDF**: https://arxiv.org/pdf/2607.01772
- **详细分析**: [[20_Research/Papers/大模型/LLM-Empowered_Multimodal_Fusion_Framework_for_Autonomous_Driving_Semantic_Enhancement_and_Channel-Adaptive_Design|LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design]]
- **作者**: Wen Wang, Yaping Sun, Yejun He, Hao Chen, Zhiyong Chen, Xiaodong Xu, Nan Ma, Shuguang Cui
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《LLM-Empowered Multimodal Fusion Framework for Autonomous Driving: Semantic Enhancement and Channel-Adaptive Design》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-radar fusion is central to robust autonomous driving, combining dense visual semantics with precise range and velocity measurements from radar. However, real-world fusion quality is fundamentally challenged by dynamically varying input quality, stemming from occlusion, adverse weather, and channel noise. To address this, we re-frame the problem from static data fusion to channel-aware semantic reasoning and propose a Large Language Model-centric Semantic-layer Channel-aware Integrated Perception (LM-SCIP) framework. It places a Large Language Model (LLM) as a central reasoning core to fuse a local visual stream with a quality-varying external radar stream used to cover perception-blind spots. Concretely, LM-SCIP couples a hierarchical radar-vision encoder with a Channel-Adaptive Semantic Module (CASM) that maps link indicators into a "Channel Prompt" to dynamically gate external radar features. A parameter-efficient, LoRA-tuned LLM, in conjunction with a heterogeneous Mixture-of-Experts (H-MoE), then arbitrates between local visual cues and the channel-conditioned radar context. Finally, a decoupled multi-task decoder outputs localization, trajectory forecasting, and image reconstruction. Experiments on nuScenes and VIRAT validate our approach. On nuScenes, under a controlled toggle of radar input, LM-SCIP reduces localization RMSE by 40.0% versus a vision-only baseline. On VIRAT, the model attains a 0.214m localization RMSE and 0.179m minFDE (k=1). These results reveal that the proposed LM-SCIP enables a robust vision-dominant fallback at low SNR and synergistic fusion at high SNR.

</details>

---

### [[20_Research/Papers/机器人/DL-VINS-Factory_A_Modular_Framework_for_Learned_Visual_Front-Ends_in_Visual-Inertial_SLAM|DL-VINS-Factory: A Modular Framework for Learned Visual Front-Ends in Visual-Inertial SLAM]]

![[assets/2607.01757_figure.png|800]]

- **arXiv**: [2607.01757](https://arxiv.org/abs/2607.01757)
- **PDF**: https://arxiv.org/pdf/2607.01757
- **详细分析**: [[20_Research/Papers/机器人/DL-VINS-Factory_A_Modular_Framework_for_Learned_Visual_Front-Ends_in_Visual-Inertial_SLAM|DL-VINS-Factory: A Modular Framework for Learned Visual Front-Ends in Visual-Inertial SLAM]]
- **作者**: Shoon Kit Lim, Melissa Jia Ying Chong, Ting Yang Ling
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Systems

#### 研究背景与动机

《DL-VINS-Factory: A Modular Framework for Learned Visual Front-Ends in Visual-Inertial SLAM》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HF-Net, HFNet, PLNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deep-learning features excel in visual matching, yet their practical value in tightly coupled visual-inertial SLAM (VI-SLAM) remains insufficiently characterized. We present DL-VINS-Factory, a unified framework that integrates learned feature extractors (ALIKED, RaCo, SuperPoint, XFeat) with either Lucas--Kanade (LK) optical-flow tracking or LightGlue (LG) descriptor matching. All front-ends share a sliding-window Ceres back-end, with optional AnyLoc DINOv2-VLAD loop closure, and 4-DoF pose-graph optimization. We benchmark the system across the four datasets covering indoor, unstructured outdoor, aggressive-motion, and visually degraded conditions. Results show that learned front-ends are viable for real-time embedded VI-SLAM, but are not universally superior to classical tracking. Relative to the corresponding GFTT+LK baseline, ALIKED+LG reduces EuRoC ATE by $5\%$ in monocular odometry and by $7\%$ in stereo with loop-closure. On NTU-VIRAL, where aggressive aerial motion increases inter-frame viewpoint change, ALIKED+LG stereo reduces loop-closed ATE by $12\%$. In Botanic Garden dataset, optical-flow tracking remains preferable, but learned keypoints still improve over the baseline GFTT, in which SuperPoint+LK reduces grayscale camera ATE by $29\%$, while RaCo+LK reduces RGB camera ATE by $38\%$. On SubT-MRS, learned front-ends display varying degree of improvement based on individual cases. With TensorRT acceleration on a Jetson AGX Orin, all valid configurations run in real time between $29$--$47$ FPS in monocular mode and $18$--$33$ FPS in stereo mode for the EuRoC and NTU-VIRAL datasets. AnyLoc further confirms roughly $2$--$7\times$ more valid loops than BRIEF+DBoW2. The implementation is open-sourced at https://github.com/limshoonkit/DL-VINS-Factory-ROS2/.

</details>

---

### [[20_Research/Papers/具身智能/Teaching_Vision-Language-Action_Models_What_to_See_and_Where_to_Look|Teaching Vision-Language-Action Models What to See and Where to Look]]

![[assets/2607.01658_first_page.png|800]]

- **arXiv**: [2607.01658](https://arxiv.org/abs/2607.01658)
- **PDF**: https://arxiv.org/pdf/2607.01658
- **详细分析**: [[20_Research/Papers/具身智能/Teaching_Vision-Language-Action_Models_What_to_See_and_Where_to_Look|Teaching Vision-Language-Action Models What to See and Where to Look]]
- **作者**: Yuguang Yang, Canyu Chen, Zhewen Tan, Yizhi Wang, Zichao Feng, Chunyang Liu, Kehua Sheng, Juan Zhang, Linlin Yang, Baochang Zhang, Yan Wang, Bo Zhang...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, Agent

#### 研究背景与动机

《Teaching Vision-Language-Action Models What to See and Where to Look》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DriveTeach-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a promising paradigm for end-to-end autonomous driving. However, existing VLAs' training relies heavily on text-centric visual question answering and chain-of-thought reasoning data, which emphasizes linguistic reasoning rather than action-grounded planning. As a result, the learned representations capture semantic knowledge but lack spatial dependencies crucial for reliable trajectory prediction. We propose DriveTeach-VLA, a framework that explicitly teaches VLAs what to see and where to look. Driving-aware Vision Distillation (DVD) injects driving-specific perceptual priors into the vision encoder, while 2D Trajectory-Guided Prompts (2D-TGP) provide spatial conditioning aligned with feasible driving trajectories. Together, they form a vision-guided learning pipeline: what to see (DVD pretraining) - where to look (TGP-guided SFT) - how to act (TGP-guided GRPO). DriveTeach-VLA achieves the state-of-the-art performance on NAVSIM and nuScenes. Our code is available at: https://github.com/ShivaTeam/DriveTeach-VLA.

</details>

---
