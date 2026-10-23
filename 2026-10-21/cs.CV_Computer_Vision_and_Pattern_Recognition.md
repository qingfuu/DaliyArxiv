# cs.CV | Computer Vision and Pattern Recognition | 2026-10-21

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/Learning_Adaptable_Dexterous_Skills_via_Hybrid_Dexterous_Mimicking|Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking]]

![[assets/2610.28628_figure.png|800]]

- **arXiv**: [2610.28628](https://arxiv.org/abs/2610.28628)
- **PDF**: https://arxiv.org/pdf/2610.28628
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Adaptable_Dexterous_Skills_via_Hybrid_Dexterous_Mimicking|Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking]]
- **作者**: Yuxuan Kuang, Jiashun Wang, Yixuan Sun, Yufei Ye, Sungjae Park, Umar Iqbal, Katerina Fragkiadaki, Shubham Tulsiani
- **cs 子类**: cs.CV, cs.GR, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人, 世界模型
- **相关性评分**: 2.62（加权：具身智能 1.8，强化学习 0.36，世界模型 0.16，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《Learning Adaptable Dexterous Skills via Hybrid Dexterous Mimicking》归入 具身智能、强化学习、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-to-Sim, Real2Sim, Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous multi-finger hands hold promise to unlock diverse skills like functional grasps, in-hand reorientation, and dynamic handover that the human-designed world assumes, yet existing learning recipes force a trade-off. Goal-reaching reinforcement learning generalizes to arbitrary object poses but, lacking any human prior, converges to unnatural and unreliable finger strategies; motion tracking reproduces human-like behavior from a single clip but cannot deviate from it. We present AdaDex, a goal-conditioned RL framework that turns a single hand-object trajectory of a few seconds---from mocap data or HOI reconstruction from in-the-wild RGB(D) video---into an adaptable dexterous skill. At the core of AdaDex is Hybrid Dexterous Mimicking: a shared policy is trained on two populations of massively parallel environments: motion tracking environments trained with dense motion tracking objective, which instill the human prior from human motion; and generalization environments with noised initial states and goals and a sparse object-success reward, which force the skill to work far off the reference. From seconds of human motion per skill, the resulting policies can learn diverse adaptable dexterous skills, such as functional grasping, object reposing, in-hand reorientation with finger gaiting, and dynamic behaviors like throw-and-catch. Our method outperforms baselines in terms of generalization and functionality, and we demonstrate transfer across simulators and to the real world. Project page: https://yuxuank.com/AdaDex/.

</details>

---

### [[20_Research/Papers/世界模型/OverSeer_Multi-Agent_World_Models_Beyond_What_Agents_See|OverSeer: Multi-Agent World Models Beyond What Agents See]]

![[assets/2610.28554_figure.png|800]]

- **arXiv**: [2610.28554](https://arxiv.org/abs/2610.28554)
- **PDF**: https://arxiv.org/pdf/2610.28554
- **详细分析**: [[20_Research/Papers/世界模型/OverSeer_Multi-Agent_World_Models_Beyond_What_Agents_See|OverSeer: Multi-Agent World Models Beyond What Agents See]]
- **作者**: Runjia Li, Kam Woh Ng, Minghao Chen, Junlin Han, Jianyuan Wang, Zhaochong An, Juan-Manuel Perez-Rua, Andrea Vedaldi, Shikun Liu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.8（加权：大模型 0.8，世界模型 1）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《OverSeer: Multi-Agent World Models Beyond What Agents See》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MAC-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the success of video world models, extending them to multiple agents is difficult because it requires generating several agent-specific video streams that are consistent in time and between agents. To address this gap, we introduce OverSeer, a multi-agent world model that augments egocentric agent views with auxiliary camera views. We suggest that, by fixing the auxiliary views in space, they act as a proxy for a world-centric representation: Unlike the agents' views, which can change entirely due to a simple change in agent position, changes in the auxiliary views directly map to localized changes in the world state. We show that these fixed views substantially help the model to maintain consistency. We also show that, due to their redundant and semi-static nature, the auxiliary views can be efficiently compressed with a delta-VAE that encodes only the changes relative to a static reference image, reducing the number of tokens required to process them. Experiments in Minecraft and Doom demonstrate improved world and agent consistency, with qualitative results on real-world multi-camera captures indicating that the approach is not tied to game engines. Our compression analysis further shows that delta-VAE substantially reduces the computational overhead of auxiliary-view generation. We conclude that these fixed views provide a simple and efficient way to improve multi-agent world models.

</details>

---

### [[20_Research/Papers/大模型/CoGaussian_Open-Vocabulary_Gaussian-based_Collaborative_3D_Scene_Understanding|CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding]]

![[assets/2610.28530_figure.png|800]]

- **arXiv**: [2610.28530](https://arxiv.org/abs/2610.28530)
- **PDF**: https://arxiv.org/pdf/2610.28530
- **详细分析**: [[20_Research/Papers/大模型/CoGaussian_Open-Vocabulary_Gaussian-based_Collaborative_3D_Scene_Understanding|CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding]]
- **作者**: Om Shivam Verma, Shaya Farahmand, Lingjun Zhao, Lu Gan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《CoGaussian: Open-Vocabulary Gaussian-based Collaborative 3D Scene Understanding》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaborative perception enables agents to retrieve the scene semantics and geometry beyond the field of view of any individual agent. This broader scene understanding enhances transportation safety and improves efficiency in multi-robot systems. However, existing collaborative semantic occupancy methods rely on dense 3D voxel annotations and are limited to recognizing objects within a predefined set of semantic classes. To overcome these limitations, we present CoGaussian, an open-vocabulary Gaussian-based collaborative semantic occupancy prediction framework. CoGaussian represents a scene as a set of foundation model-aligned sparse 3D Gaussians, which serve as a compact representation for communicating and fusing geometric and semantic information across multiple agents. On the Semantic-OPV2V benchmark, our method outperforms existing open-vocabulary single-agent approaches, highlighting the effectiveness of open-vocabulary collaborative scene understanding.

</details>

---

### [[20_Research/Papers/具身智能/CLOSER_Evidence-Aware_Active_Visual_Verification_for_Embodied_Object-Goal_Navigation|CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation]]

![[assets/2610.28476_figure.png|800]]

- **arXiv**: [2610.28476](https://arxiv.org/abs/2610.28476)
- **PDF**: https://arxiv.org/pdf/2610.28476
- **详细分析**: [[20_Research/Papers/具身智能/CLOSER_Evidence-Aware_Active_Visual_Verification_for_Embodied_Object-Goal_Navigation|CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation]]
- **作者**: Pengying Wu, Mingye Jiang, Yunze Hu, Zhejia Wen, Kangjie Zhou, Zongru Yang, Zhe Peng, Chang Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《CLOSER: Evidence-Aware Active Visual Verification for Embodied Object-Goal Navigation》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：YOLO-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object-goal navigation (ObjectNav) requires an embodied agent to find an instance of a specified category in an unseen environment and stop near it. The agent typically relies on an object detector but must judge online from a limited egocentric video stream, sometimes a single frame, whether a detected candidate is the target. Detectors often confidently mistake similar objects, such as a sofa for a bed, and stopping at a false positive fails the episode. Prevailing systems also approach candidates greedily, leaving them occluded or partially observed. We present CLOSER, an evidence-aware active verification framework that treats stopping as closed-loop evidence acquisition, coupling vision-language model (VLM) verification with active perception. CLOSER fine-tunes an open-source VLM to label each view of a candidate tracked across frames as target, non-target, or uncertain, selects complementary views with an embedding-based diversity gate, and fuses their per-view probabilities with a lightweight network. If the fused judgment remains uncertain, a diffusion policy drives the agent toward the candidate using only the tracked mask and depth until the decision becomes decisive. CLOSER runs locally and plugs into existing ObjectNav systems without retraining them. On Gibson and Habitat-Matterport 3D, it raises average success rate by 3.6 points and success weighted by path length by 2.0 points, showing that verifying evidence before committing improves embodied navigation.

</details>

---

### [[20_Research/Papers/大模型/LaLa-World_Scaling_Latent_World_Models_with_Natural_Language_Actions|LaLa-World: Scaling Latent World Models with Natural Language Actions]]

![[assets/2610.27851_figure.png|800]]

- **arXiv**: [2610.27851](https://arxiv.org/abs/2610.27851)
- **PDF**: https://arxiv.org/pdf/2610.27851
- **详细分析**: [[20_Research/Papers/大模型/LaLa-World_Scaling_Latent_World_Models_with_Natural_Language_Actions|LaLa-World: Scaling Latent World Models with Natural Language Actions]]
- **作者**: Junha Song, Geonmo Gu, Jeongeun Park, Heejeong Nam, Lucas Maes, Byeongho Heo, Dongyoon Han, Sangdoo Yun
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 强化学习, 大模型
- **相关性评分**: 1.62（加权：大模型 0.1，强化学习 0.16，世界模型 1.16，机器人 0.2）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《LaLa-World: Scaling Latent World Models with Natural Language Actions》归入 世界模型、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, LaLa-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper shows that JEPA-style latent world models (LWMs) can learn across diverse domains and data sources by adopting the language-conditioned interface of video generation models. We establish this approach as an effective and efficient basis for planning with imagination and downstream policy fine-tuning. To this end, we introduce LaLa-World, a Language-conditioned Latent World model that learns from simulation and robot trajectories together with broader image and video data. Two designs make this work. First, we describe both numerical actions and visual changes in language, enabling joint training of a single future predictor across heterogeneous datasets. Second, we build the predictor on a language model, allowing it to interpret language conditions while predicting future latent states. The resulting predictor achieves higher average MPC planning performance than existing LWMs trained separately for each domain or task. Adding image and video data further improves average planning performance and robustness to action phrasing. In a matched comparison with an RAEv2-based video generation model baseline, LaLa-World reaches comparable planning performance with $6\times$ less training cost and $13.9\times$ faster planning. Beyond planning, the pretrained LaLa-World serves as an initialization for LaLa-Policy, which jointly predicts actions and future visual representations. LaLa-Policy performs competitively with Cosmos Policy on LIBERO and RoboCasa, with up to $5.5\times$ faster inference.

</details>

---

### [[20_Research/Papers/具身智能/RoboJudge_Multimodal_Language_Models_as_Judges_for_Embodied_Video_Generation|RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation]]

![[assets/2610.27782_figure.png|800]]

- **arXiv**: [2610.27782](https://arxiv.org/abs/2610.27782)
- **PDF**: https://arxiv.org/pdf/2610.27782
- **详细分析**: [[20_Research/Papers/具身智能/RoboJudge_Multimodal_Language_Models_as_Judges_for_Embodied_Video_Generation|RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation]]
- **作者**: Siyuan Ma, Yu Qi, Cheng Ye, Ruotian Peng, Xinyi Xu, Zitiantao Lin, Zedong Cai, Yijian Huang, Weiyang Liu, Siyuan Wang, Yandong Wen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 强化学习, 世界模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.5，强化学习 0.2，世界模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《RoboJudge: Multimodal Language Models as Judges for Embodied Video Generation》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AgiBot-World, Physion-Eval, RoboJudge-Bench, WBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generation models are promising foundations for embodied world models, but only if their generated rollouts are physically valid and faithful to task instructions. Multimodal large language models (MLLMs) are increasingly used to judge these properties, yet their agreement with human judgments on embodied videos has not been systematically evaluated. To address this gap, we introduce RoboJudge-Bench, a benchmark for evaluating MLLMs as judges of embodied video generation. The benchmark measures two fundamental dimensions, Physical Adherence and Instruction Alignment, across 800 human-annotated videos from 8 source corpora and 10 video generators, spanning grippers, human hands, and dexterous hands. Experiments reveal uneven alignment between existing judges and human ratings: general-purpose MLLMs show lower agreement on physical adherence, while specialized video judges designed for general-domain physical reasoning do not consistently transfer to embodied scenarios. Motivated by these findings, we construct RoboJudge-Train, comprising 12K videos annotated with 25K human-verified scores and model-assisted rationales for Physical Adherence and Instruction Alignment. We fine-tune a 9B MLLM on this dataset with supervised learning followed by reinforcement learning, yielding RoboJudge-9B. Among the model judges evaluated on RoboJudge-Bench, RoboJudge-9B achieves the highest overall agreement, reaching a Pearson correlation of 0.719 with a statistically significant 0.089 gain over Gemini-3.7-Flash, the best-performing proprietary baseline in our evaluation. Training on RoboJudge-Train also yields gains on external benchmarks, including VideoPhy2 and Physion-Eval. We further use RoboJudge-9B as a downstream evaluator to benchmark video generation models according to Physical Adherence and Instruction Alignment.

</details>

---

### [[20_Research/Papers/具身智能/VEOcc++_Learning_Persistent_Voxel_Feature_Maps_for_Embodied_Online_Semantic_Occupancy_Mapping_and_Offline_Refinement|VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement]]

![[assets/2610.27704_figure.png|800]]

- **arXiv**: [2610.27704](https://arxiv.org/abs/2610.27704)
- **PDF**: https://arxiv.org/pdf/2610.27704
- **详细分析**: [[20_Research/Papers/具身智能/VEOcc++_Learning_Persistent_Voxel_Feature_Maps_for_Embodied_Online_Semantic_Occupancy_Mapping_and_Offline_Refinement|VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement]]
- **作者**: Ruoyu Wang, Jiahan Li, Yong Liu, Kexin Zhang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 1.2，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《VEOcc++: Learning Persistent Voxel Feature Maps for Embodied Online Semantic Occupancy Mapping and Offline Refinement》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EmbodiedOcc-ScanNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Semantic occupancy mapping supports embodied perception during exploration and detailed scene understanding afterward, giving rise to two complementary requirements: online incremental mapping for maintaining an up-to-date global map under causal constraints, and offline global map refinement for improving the completed scene representation with additional computation. We present VEOcc++, a unified voxel-centric framework that connects both stages through a persistent sparse voxel feature map. During exploration, the map expands with newly observed regions and integrates aligned local features through reliability-guided updates, while context-aware decoding produces the current semantic occupancy map. After exploration, cached local features are consolidated as complementary evidence and combined with the completed online representation for multi-scale spatial refinement. On EmbodiedOcc-ScanNet, VEOcc++ achieves 67.12\% IoU and 58.40\% mIoU, establishing new state-of-the-art performance for online incremental mapping. With the local predictor fixed, our online mapping pipeline outperforms VEOcc fusion by 3.70 IoU and 3.74 mIoU points, demonstrating substantial gains from the proposed global mapping design. Offline global map refinement further improves the completed map to 67.79% IoU and 59.37% mIoU using only the observations acquired during exploration. Zero-shot deployment on a mobile robot further demonstrates transferability to unseen environments, onboard feasibility, and scalability to large-scale indoor mapping. Project page: https://wryzju.github.io/VEOccpp/.

</details>

---

### [[20_Research/Papers/具身智能/PLaCA_Learning_Patch-Level_Future_Latent_Change_for_Action_Generation|PLaCA: Learning Patch-Level Future Latent Change for Action Generation]]

![[assets/2610.27657_figure.png|800]]

- **arXiv**: [2610.27657](https://arxiv.org/abs/2610.27657)
- **PDF**: https://arxiv.org/pdf/2610.27657
- **详细分析**: [[20_Research/Papers/具身智能/PLaCA_Learning_Patch-Level_Future_Latent_Change_for_Action_Generation|PLaCA: Learning Patch-Level Future Latent Change for Action Generation]]
- **作者**: Zhan Yi, Yuchen Wang, Chao Li, Lei Hong, Boyuan Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，世界模型 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《PLaCA: Learning Patch-Level Future Latent Change for Action Generation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, CoWVLA, DreamVLA, VideoWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models generate robot actions from visual observations and language instructions, but effective manipulation also requires anticipating how the environment will change. Existing world-action models explore future image prediction and latent dynamics modeling. However, generating complete future images can be computationally expensive, while highly compressed latent representations may obscure local changes. To address these challenges, we propose PLaCA, a world-to-action framework built around future latent change. PLaCA directly predicts spatially structured patch-level future latent change from the current multimodal input, preserving local information about expected environmental changes. We introduce patch-level change-aware supervision to emphasize regions undergoing larger changes and a future-to-action interface that explicitly incorporates predicted future latent change into action generation. Experiments on LIBERO-Long show that PLaCA achieves a 79.0% success rate, improving upon the Action-only baseline by 5.0 percentage points. On CALVIN, PLaCA improves the average sequence length from 2.784 to 3.564. These improvements are achieved while updating only 2.95% of the model parameters during the second training stage, demonstrating the effectiveness of future latent change modeling for downstream robotic manipulation.

</details>

---

### [[20_Research/Papers/强化学习/CaMeWM_A_Causal_Medical_World_Model_for_Generative_Tumor_Evolution_and_Treatment_Planning|CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning]]

![[assets/2610.26923_figure.png|800]]

- **arXiv**: [2610.26923](https://arxiv.org/abs/2610.26923)
- **PDF**: https://arxiv.org/pdf/2610.26923
- **详细分析**: [[20_Research/Papers/强化学习/CaMeWM_A_Causal_Medical_World_Model_for_Generative_Tumor_Evolution_and_Treatment_Planning|CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning]]
- **作者**: Huanlong Gao, Xuelei He, Fengjun Zhao, Xiaowei He
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《CaMeWM: A Causal Medical World Model for Generative Tumor Evolution and Treatment Planning》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Treatment planning is intrinsically counterfactual: clinicians must compare how a patient's tumor and survival would evolve under competing regimens, whereas a retrospective cohort records only the regimen received and one follow-up scan. A treatment-conditioned generator trained on such data can therefore reproduce historical treatment allocation rather than simulate the interventional disease dynamics needed to rank regimens. We introduce \textbf{CaMeWM}, a causal medical world model for supported post-TACE tumor evolution and treatment planning. CaMeWM implements one intervention-to-decision loop rather than three independent prediction tasks: it first admits a queried regimen only for clinically comparable histories with empirical treatment support; it then generates a distribution of lesion-local follow-up worlds through an action-conditioned response descriptor, deterministic anchor, and residual 3D diffusion transition; and it finally maps sampled worlds to restricted mean survival time (RMST) with a response-Cox utility model. Under pre-treatment adjustment and positivity, this loop estimates a prespecified, support-restricted g-formula target; all selection and nuisance estimation are fold-local, and the induced policy is evaluated by cross-fitted, censoring-adjusted doubly robust estimation. Across 79 paired out-of-fold episodes, CaMeWM achieves 0.618 SSIM and 0.528 change-map SSIM for follow-up CT transition, while its generated-world survival pathway attains a 0.615 C-index; factual-only AIPW estimates a 9.60-week RMST gain (95\% CI 0.61--18.13) for the frozen policy. CaMeWM provides an inspectable basis for retrospective, support-restricted treatment planning.

</details>

---

### [[20_Research/Papers/具身智能/Robotic_Video_World_Models_A_Survey_of_Applications,_Research_Challenges,_Future_Directions|Robotic Video World Models: A Survey of Applications, Research Challenges, Future Directions]]

![[assets/2601.07823_figure.png|800]]

- **arXiv**: [2601.07823](https://arxiv.org/abs/2601.07823)
- **PDF**: https://arxiv.org/pdf/2601.07823
- **详细分析**: [[20_Research/Papers/具身智能/Robotic_Video_World_Models_A_Survey_of_Applications,_Research_Challenges,_Future_Directions|Robotic Video World Models: A Survey of Applications, Research Challenges, Future Directions]]
- **作者**: Zhiting Mei, Tenny Yin, Ola Shorinwa, Apurva Badithela, Zhonghe Zheng, Joseph Bruno, Madison Bland, Lihan Zha, Asher Hancock, Jaime Fernández Fisac, Philip Dames, Anirudha Majumdar
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.8（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，世界模型 0.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Robotic Video World Models: A Survey of Applications, Research Challenges, Future Directions》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video world models have emerged as promising candidates for high-fidelity world models, offering the potential to synthesize high-quality videos capturing fine-grained interactions between agents and their environments conditioned on multi-modal user inputs. Their impressive capabilities address many of the long-standing challenges faced by physics-based simulators, driving broad adoption in many problem domains, e.g., robotics. For example, video models can generate photorealistic, physically consistent deformable-body simulation without making prohibitive simplifying assumptions, which is a major bottleneck in physics-based simulation. Moreover, video models can serve as foundation world models that capture the dynamics of the world in a fine-grained and expressive way. They thus overcome the limited expressiveness of language-only abstractions in describing intricate physical interactions. However, despite their potential, video models still generate physics-violating future predictions, often manifesting as hallucinations. In this survey, we provide a review of video models and their applications as embodied world models in robotics, including efficient data generation and policy learning, dynamics and rewards modeling in reinforcement learning, policy evaluation, and visual planning. Further, we highlight important challenges hindering the trustworthy integration of video models, such as poor instruction following, hallucinations like violations of physics, unsafe content generation, in addition to significant data and compute overhead. We present potential future directions to address these open research challenges to motivate research and ultimately facilitate broader applications, especially in safety-critical settings. We provide a curated bibliography at https://github.com/irom-princeton/awesome-robotics-video-world-model-papers .

</details>

---
