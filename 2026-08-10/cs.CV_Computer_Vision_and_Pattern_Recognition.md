# cs.CV | Computer Vision and Pattern Recognition | 2026-08-10

#arxiv #ComputerScience

**论文数**: 11

### [[20_Research/Papers/世界模型/Addressable_Memory_for_Video_World_Models|Addressable Memory for Video World Models]]

![[assets/2608.07408_figure.png|800]]

- **arXiv**: [2608.07408](https://arxiv.org/abs/2608.07408)
- **PDF**: https://arxiv.org/pdf/2608.07408
- **详细分析**: [[20_Research/Papers/世界模型/Addressable_Memory_for_Video_World_Models|Addressable Memory for Video World Models]]
- **作者**: Xindi Wu, Sven Elflein, James Lucas, Olga Russakovsky, Laura Leal-Taixé, Despoina Paschalidou, Jonathan Lorraine, Aljoša Ošep
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Addressable Memory for Video World Models》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LoopBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study visual persistence in interactive video world models. These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames. However, we find that models can no longer reliably address stored content once rollouts extend beyond the training horizon, because temporal Rotary Positional Embeddings (RoPE) offsets then fall outside the range seen during training and the model struggles to retrieve the relevant visual information through attention. Moreover, naively compressing the cache in the RoPE-rotated space corrupts memory by averaging together incompatible positional phases. To address this, we propose WorldTrace, a training-free memory framework for long-horizon visual persistence. WorldTrace keeps compressed memory addressable by assigning each summary slot a distinct, in-distribution virtual position. Within this addressable cache, we study two memory compression approaches: WorldTrace-Field compresses history for temporal coherence, while WorldTrace-Landmark stores verbatim scene traces at detected transitions for episodic recall. We further introduce LoopBench, a benchmark evaluating whether a compressed cache can reconstruct a previously visited scene after a long detour. WorldTrace-Field improves temporal consistency by +15.5%, and WorldTrace-Landmark improves episodic recall by +19.5% on LoopBench, extending visually persistent generation without retraining.

</details>

---

### [[20_Research/Papers/具身智能/Depth-Wise_Probing_and_Pruning_of_the_Planning_Token_in_a_Driving_Vision-Language-Action_Model|Depth-Wise Probing and Pruning of the Planning Token in a Driving Vision-Language-Action Model]]

![[assets/2608.07361_figure.png|800]]

- **arXiv**: [2608.07361](https://arxiv.org/abs/2608.07361)
- **PDF**: https://arxiv.org/pdf/2608.07361
- **详细分析**: [[20_Research/Papers/具身智能/Depth-Wise_Probing_and_Pruning_of_the_Planning_Token_in_a_Driving_Vision-Language-Action_Model|Depth-Wise Probing and Pruning of the Planning Token in a Driving Vision-Language-Action Model]]
- **作者**: Harisankar Babu, Benjamin Coors, Christopher Lang, Hendrik Berkemeyer, Tamim Asfour, Simon Foell
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Depth-Wise Probing and Pruning of the Planning Token in a Driving Vision-Language-Action Model》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models route driving decisions through a deep language model, but it is unclear how much of that depth the action itself requires. We study a representative driving VLA whose entire plan is carried by a single planning token that a generative planner decodes into a trajectory. Borrowing the planner as a trajectory-space logit lens, we decode the planning token from every one of the 32 decoder layers and measure two signals: the linear decodability of the navigation command and trajectory compatibility with the frozen native planner. Our diagnostic shows that semantic intent is linearly decodable early: command-probe accuracy reaches 97.7\% after the first decoder layer, compared with 16.7\% chance. In contrast, compatibility with the frozen native planner improves gradually across depth, with open-loop Avg-L2 reaching its minimum of 2.11\,m only at the final layer. Learned readouts from the first layer recover much of this gap, indicating that planning information is already present early but is not yet represented in the format expected by the deployed planner. Ranking decoder layers by the angular deviation they induce in the planning token permits removal of 8 of 32 layers within an approximately 5\% relative open-loop error increase and yields a measured 1.33$\times$ decoder speedup. At the evaluated sample size, no family-specific degradation is statistically resolved. These findings are limited to the evaluated ORION checkpoint and Bench2Drive setup.

</details>

---

### [[20_Research/Papers/具身智能/TEMPO_Semantic-Action_Decoupled_RL_Post-Training_for_Vision-Language-Action_Models|TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models]]

![[assets/2608.07314_figure.png|800]]

- **arXiv**: [2608.07314](https://arxiv.org/abs/2608.07314)
- **PDF**: https://arxiv.org/pdf/2608.07314
- **详细分析**: [[20_Research/Papers/具身智能/TEMPO_Semantic-Action_Decoupled_RL_Post-Training_for_Vision-Language-Action_Models|TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models]]
- **作者**: Ziheng Liu, Quantao Yang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.8，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TEMPO: Semantic-Action Decoupled RL Post-Training for Vision-Language-Action Models》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DAM-VLA, OpenVLA, RIPT-VLA, RL-VLA, Real-World, SimpleVLA-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models are commonly adapted to downstream manipulation tasks via supervised fine-tuning (SFT) or online reinforcement learning (RL) post-training. SFT is prone to distribution mismatch, and existing RL approaches typically apply a single, uniform update strategy to all model components, ignoring their distinct functional roles. We propose TEMPO, a semantic-action decoupled, two-timescale RL post-training framework for VLA models. TEMPO freezes the pretrained vision-language backbone to preserve general semantic representations, and restricts adaptation to two components with dedicated RL optimization loops: the semantic projection layer and the low-level action expert. We update them at different rates--the semantic projection layer infrequently, to keep the latent action stable, and the action expert frequently, to rapidly incorporate control feedback from online interaction. This decoupling RL fine-tuning strategy prevents fast policy updates from destabilizing high-level semantic representations while still allowing the action expert to learn efficiently from online feedback. Experiments on the CALVIN benchmark and real-world manipulation tasks demonstrate that TEMPO consistently outperforms both pretrained state-of-the-art VLA models and the RL post-training baseline, while reaching and maintaining higher evaluation rewards on two real-world tasks.

</details>

---

### [[20_Research/Papers/具身智能/C2Dex_Contact-Consistent_Reconstruction_and_Retargeting_for_Dexterous_Manipulation_from_Monocular_Video|C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video]]

![[assets/2608.07045_figure.png|800]]

- **arXiv**: [2608.07045](https://arxiv.org/abs/2608.07045)
- **PDF**: https://arxiv.org/pdf/2608.07045
- **详细分析**: [[20_Research/Papers/具身智能/C2Dex_Contact-Consistent_Reconstruction_and_Retargeting_for_Dexterous_Manipulation_from_Monocular_Video|C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video]]
- **作者**: Jie Ren, Zhehao Jiang, Yinhong Yang, Haorui Jia, Han Jiang, Ben Li, Yao Yao, Cheng Lin, Qiu Shen, Zhenshan Bing, Xiao-Xiao Long, Xun Cao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.5（加权：具身智能 1.8，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《C2Dex: Contact-Consistent Reconstruction and Retargeting for Dexterous Manipulation from Monocular Video》归入 具身智能、机器人、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-quality demonstrations for dexterous robot manipulation are costly and difficult to collect, whereas monocular human videos provide a scalable source of diverse manipulation behaviors. However, transferring such demonstrations to dexterous robots remains challenging: monocular hand-object interaction (HOI) reconstruction often produces temporally unstable contacts and physically implausible interactions, while conventional retargeting methods struggle to preserve task-relevant contacts and local interaction geometry across different hand embodiments. We present C2Dex, a video-to-dexterous-manipulation framework built around a shared interaction representation: stable object-side contacts recovered by aggregating noisy frame-wise observations in the canonical object space. These stable contacts serve a dual role: as trajectory-level constraints that guide reconstruction toward temporally coherent and physically plausible human HOI trajectories, and as explicit transfer targets for the dexterous hand, where Laplacian interaction optimization preserves the local hand-object geometry across embodiments and residual reinforcement learning refines the trajectory in simulation. Experiments on DexYCB and TACO show that C2Dex achieves end-to-end trajectory success rates of 57.78% and 26.67%, respectively, substantially outperforming the strongest baselines (17.78% and 10.00%) under identical evaluation criteria. Real-robot replay experiments further demonstrate physical feasibility across diverse contact-rich manipulation tasks. Project page: this https URL

</details>

---

### [[20_Research/Papers/大模型/When_One_Modality_Is_Not_Enough_Multimodal_Sex_and_Life-Stage_Classification_of_Red_Deer_from_Aerial_RGB-Thermal_Video|When One Modality Is Not Enough: Multimodal Sex and Life-Stage Classification of Red Deer from Aerial RGB-Thermal Video]]

![[assets/2608.06973_figure.png|800]]

- **arXiv**: [2608.06973](https://arxiv.org/abs/2608.06973)
- **PDF**: https://arxiv.org/pdf/2608.06973
- **详细分析**: [[20_Research/Papers/大模型/When_One_Modality_Is_Not_Enough_Multimodal_Sex_and_Life-Stage_Classification_of_Red_Deer_from_Aerial_RGB-Thermal_Video|When One Modality Is Not Enough: Multimodal Sex and Life-Stage Classification of Red Deer from Aerial RGB-Thermal Video]]
- **作者**: Hugo Markoff, Christoph Praschl, Ivan Ludoški, Sara Beery, Michael Ørsted, David C. Schedl
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人
- **相关性评分**: 0.6（加权：大模型 0.4，机器人 0.2）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《When One Modality Is Not Enough: Multimodal Sex and Life-Stage Classification of Red Deer from Aerial RGB-Thermal Video》归入 大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial drone surveys increasingly support wildlife population estimation, yet a useful census is more than a count: population dynamics are defined by species composition, sex ratios and age structure, that is, by which species are present and how a herd splits into adult males, adult females and juveniles. We use red deer ($\textit{Cervus elaphus}$) as a test case, because managers act on these dynamics and because the visible cue defining adult males, the antlers, is seasonally variable. Surveys are flown nadir, high enough not to disturb the animals, so each deer occupies only a small, low-resolution patch. The two recording modalities fail in opposite conditions: in color a deer under canopy blends into the ground, while in thermal it becomes a bright blob that loses fine detail. Rather than trust either modality alone, we fuse them at every stage using self-supervised DINOv3 features. Our pipeline tracks animals in both modalities, treats an animal as confirmed only when the two cameras agree, keeps only the clear, non-occluded frames, and assigns species and sex by a vote across them; life stage is read separately from geo-referenced body size, since at survey resolution a juvenile often only differs from an adult female in size. Across four flights spanning the antler season the fused pipeline correctly classifies 25 of the 26 detected individuals (7 of 8 adult males, all 16 adult females and 2 juveniles), against 20 of 26 for either sensor alone. Multimodal species classification reaches 96.0%, while for sex classification fusing the two sensors matters most: the combined RGB+thermal model is the most robust across environments and seasons. Automating the demographic classification turns a drone flight from a count into a repeatable reading of herd structure, so the sex ratios and age structure that managers already act on can be gathered as often as a survey can be flown.

</details>

---

### [[20_Research/Papers/机器人/Vernata_Self-Supervised_Learning_of_LiDAR_Point_Representations|Vernata: Self-Supervised Learning of LiDAR Point Representations]]

![[assets/2608.06919_figure.png|800]]

- **arXiv**: [2608.06919](https://arxiv.org/abs/2608.06919)
- **PDF**: https://arxiv.org/pdf/2608.06919
- **详细分析**: [[20_Research/Papers/机器人/Vernata_Self-Supervised_Learning_of_LiDAR_Point_Representations|Vernata: Self-Supervised Learning of LiDAR Point Representations]]
- **作者**: Oliver Lemke, Alexander Liniger, Abel Gawel, Marco Hutter
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Vernata: Self-Supervised Learning of LiDAR Point Representations》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

LiDAR serves as a primary sensing modality for robots operating in outdoor environments. However, the performance of deep learning models in this domain is severely limited by the scarcity of labeled data, a direct result of the high cost of 3D annotation. Self-supervised learning addresses this scarcity by learning general-purpose features from unlabeled data. In this work, we present a multi-modal, multi-teacher distillation framework for self-supervised learning on outdoor LiDAR point clouds. Building upon the Sonata architecture, we introduce Vernata, consisting of three extensions: sparse view augmentation to improve robustness against varying point densities, a memory bank mechanism to stabilize resource-constrained training, and cross-modal distillation utilizing dense, high-resolution 2D image features to enable fine-grained semantic guidance. We evaluate our method on the GrandTour, TartanGround, and Waymo datasets, as well as data collected from our own robotic platforms. Our experiments demonstrate a significant performance improvement over Sonata baselines, yielding mIoU scores of 54.7 on TartanGround (+5.9 points, +12.1%) and 57.1 on Waymo (+7.3 points, +14.7%). Finally, we show that the self-supervised approach maintains strong performance even in reduced-modality settings (lacking color or normals), achieving competitive mIoU scores of 49.4 and 50.2 on the respective datasets.

</details>

---

### [[20_Research/Papers/强化学习/R2S-EGO_Dual-Proxy_Refinement_for_Sparse-Capture_Real-to-Sim|R2S-EGO: Dual-Proxy Refinement for Sparse-Capture Real-to-Sim]]

![[assets/2608.06827_figure.png|800]]

- **arXiv**: [2608.06827](https://arxiv.org/abs/2608.06827)
- **PDF**: https://arxiv.org/pdf/2608.06827
- **详细分析**: [[20_Research/Papers/强化学习/R2S-EGO_Dual-Proxy_Refinement_for_Sparse-Capture_Real-to-Sim|R2S-EGO: Dual-Proxy Refinement for Sparse-Capture Real-to-Sim]]
- **作者**: Shuai Fang, Xin Deng, Yuchen Kang, Zhenjiang Li, Jie Chen
- **cs 子类**: cs.CV, cs.GR, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《R2S-EGO: Dual-Proxy Refinement for Sparse-Capture Real-to-Sim》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GaussGym, Real-to-Sim, RoboGSim, SplatSim, Vid2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-to-sim (R2S) depends on scene representations that render observations along robot ego trajectories, yet dense multi-view capture limits per-environment real-image capture-count efficiency, and sparse human capture can leave behavior-scoped robot views under-supported. Camera-controlled synthesis can fill missing views, but its use in R2S requires behavior-admissible queries and capture-anchored structural conditioning. We present R2S-EGO, which couples a simulator-derived robot proxy that represents the behavior-scoped executable query domain with a capture-anchored geometry proxy that supplies scene-specific structural conditions. Within this domain, fixed- budget selection targets current support deficits for which geometry support is available. The generated observations are assimilated as pseudo-observations to refine the visual asset, while real captures remain anchors. The fused geometry proxy also supplies the scene collision surface, which is refreshed between rounds. Together, these updates refine the existing simulation scene while its robot dynamics and control stack stay fixed. Across 48 frozen Unitree G1 ego views in three Replica scenes, six-view R2S-EGO reaches 19.062 dB PSNR, compared with 14.226 dB for the strongest reported R2S baseline. Across five paired policy-training seeds, R2S-EGO achieves 82.5% +/- 6.8% real-G1 sitting success, compared with 10.0% +/- 10.5% for GaussGym.

</details>

---

### [[20_Research/Papers/强化学习/Is_Forward_Prediction_Enough_Physical_State_Grounding_for_JEPA_World_Models|Is Forward Prediction Enough? Physical State Grounding for JEPA World Models]]

![[assets/2608.06799_figure.png|800]]

- **arXiv**: [2608.06799](https://arxiv.org/abs/2608.06799)
- **PDF**: https://arxiv.org/pdf/2608.06799
- **详细分析**: [[20_Research/Papers/强化学习/Is_Forward_Prediction_Enough_Physical_State_Grounding_for_JEPA_World_Models|Is Forward Prediction Enough? Physical State Grounding for JEPA World Models]]
- **作者**: Haodong Yan, Jiaguan Zhu, Mingyuan Jia, Ruiqing Yin, Junjie He, Zhide Zhong, Junfeng Li, Jinxuan Lu, Hengtao Li, Tianran Zhang, Jiayi Chen, Wenxuan Song...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，世界模型 1.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Is Forward Prediction Enough? Physical State Grounding for JEPA World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OGBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning structured and control-relevant latent representations remains a key challenge for world models. Recent JEPA-based world models learn action-conditioned predictive latent dynamics from observation sequences. However, their forward-prediction objectives do not explicitly enforce reliable identifiability of robot-centric physical state from individual latents or state changes from latent pairs, which can limit downstream planning and policy performance. We propose PSG-JEPA, a physically grounded JEPA world model that shapes its latent space with two complementary grounding objectives beyond forward prediction: grounding individual latents in robot proprioceptive state, and grounding latent pairs in multi-horizon joint-angle changes. Both objectives are applied only during training, leaving the inference architecture and computational cost unchanged. To comprehensively evaluate PSG-JEPA, we conduct experiments at three levels: (1) latent identifiability via probing, (2) goal-conditioned planning on frozen latents, and (3) policy learning in simulation and on a real robot. Experiments demonstrate that our PSG-JEPA consistently outperforms state-of-the-art latent world-model baselines at all three levels.

</details>

---

### [[20_Research/Papers/具身智能/AtlasVLA_Persistent_World-Ego_State_Modeling_for_Vision-Language-Action_Models|AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models]]

![[assets/2608.06729_figure.png|800]]

- **arXiv**: [2608.06729](https://arxiv.org/abs/2608.06729)
- **PDF**: https://arxiv.org/pdf/2608.06729
- **详细分析**: [[20_Research/Papers/具身智能/AtlasVLA_Persistent_World-Ego_State_Modeling_for_Vision-Language-Action_Models|AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models]]
- **作者**: Guiyu Zhao, Longteng Guo, Yanghong Mei, Zilin Zhu, Yu Zhang, Bin Cao, Mingming Yu, Xingjian He, Jie Jiang, Jing Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 2.4，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《AtlasVLA: Persistent World-Ego State Modeling for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AtlasVLA, DexVLA, DreamVLA, MAP-VLA, MemoryVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While Vision-Language-Action (VLA) models have advanced embodied AI, their fundamentally reactive paradigm severely limits performance in partially observable and long-horizon tasks. When restricted to a single wrist-mounted camera, they inevitably suffer from perception forgetting as objects exit the field of view, and temporal task-progress forgetting} during multi-step execution. To overcome these bottlenecks, we propose AtlasVLA, a novel framework that transitions from direct reactive manipulation to proactive reasoning through a persistent world-ego state. AtlasVLA features a dual-memory architecture: a 4D Persistent World State Memory that lifts transient 2D observations into a globally updated, voxel-hashed spatial state to resolve visual blind spots, and an Ego-Working State Memory that tracks historical ego state and task progress. By conditioning a diffusion transformer (DiT) on this joint World-Ego state, AtlasVLA enables robust spatial reasoning. Extensive evaluations across LIBERO, RLBench, and real-world benchmarks demonstrate that AtlasVLA achieves state-of-the-art performance using solely a wrist camera. Remarkably, it decisively outperforms multi-view baselines, yielding absolute success rate improvements of 9.4% on LIBERO-Long and 17.5% in real-world long-horizon tasks.

</details>

---

### [[20_Research/Papers/机器人/UAV3DCrop_Benchmarking_3D_Reconstruction_in_Repeated_Multi-Angle_UAV_Crop_Surveys|UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys]]

![[assets/2608.06404_figure.png|800]]

- **arXiv**: [2608.06404](https://arxiv.org/abs/2608.06404)
- **PDF**: https://arxiv.org/pdf/2608.06404
- **详细分析**: [[20_Research/Papers/机器人/UAV3DCrop_Benchmarking_3D_Reconstruction_in_Repeated_Multi-Angle_UAV_Crop_Surveys|UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys]]
- **作者**: Junxiong Zhou, Xuechen Li, Chonghao Qiu, Lang Qiao, Xiaowei Jia, Qi Yang, Chishan Zhang, Leikun Yin, Nanshan You, Vipin Kumar, David Mulla, Ce Yang...
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《UAV3DCrop: Benchmarking 3D Reconstruction in Repeated Multi-Angle UAV Crop Surveys》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate 3D crop monitoring underpins data-driven precision agriculture by enabling field-scale analysis of plant structure, growth dynamics, and management response. Modern 3D reconstruction methods perform strongly on generic benchmarks, but rendered appearance may not translate into metrically and agronomically useful geometry in crop fields. We introduce UAV3DCrop, a public benchmark of repeated multi-angle unmanned aerial vehicle (UAV) crop surveys. It contains 88,830 RGB images at $5280 \times 3956$ pixels, with a ground sampling distance of 3.6-5.8 mm, from 91 scenes spanning corn, soybean, wheat, and oat. Track A evaluates seven scene-optimized methods -- Neural Radiance Field (NeRF) and 3D Gaussian Splatting (3DGS) variants -- on held-out views, photogrammetry-referenced depth, and canopy-height recovery. Track B tests four pretrained feed-forward models on zero-shot camera-pose and geometry estimation. The scene-optimized methods rank differently across the three targets: Splatfacto-big leads appearance, whereas Scaffold-GS leads depth and is statistically tied with Splatfacto for canopy height. Among feed-forward models, MapAnything leads on seven of the eight metrics, while the remaining models vary more across crops and fail severely on absolute scale in a way that alignment conceals. Repeated acquisitions reveal further sensitivities that differ by output type and by model, associated with position within the acquisition sequence and with tie-point multiplicity. Current 3D reconstruction methods are therefore not yet interchangeable for agronomic use: no single method wins on appearance, geometry, and canopy height at once, and only one of four feed-forward models recovers usable metric scale. The dataset is publicly available at this https URL

</details>

---

### [[20_Research/Papers/机器人/TRACE_Ergodic_Trajectory_Optimization_for_Active_Scene_Reconstruction|TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction]]

![[assets/2608.02304_figure.png|800]]

- **arXiv**: [2608.02304](https://arxiv.org/abs/2608.02304)
- **PDF**: https://arxiv.org/pdf/2608.02304
- **详细分析**: [[20_Research/Papers/机器人/TRACE_Ergodic_Trajectory_Optimization_for_Active_Scene_Reconstruction|TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction]]
- **作者**: Ziyue Zheng, Linli Shi, Bingkun He, Wen Jiang, Ziyun Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《TRACE: Ergodic Trajectory Optimization for Active Scene Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing active reconstruction systems with Gaussian-splatting maps select observations greedily, optimizing a single next-best-view (NBV) at each step and connecting the chosen views by short-horizon path planning. This greedy decoupling disregards the global structure of scene information, producing inefficient trajectories that waste sensing capacity in transit between selected views. In this work, we study active reconstruction as an ergodic coverage problem: the time-averaged spatial statistics of the sensor trajectory should match a target information distribution induced by the current map. Our approach derives this target distribution online from uncertainty and visibility, and calculates ergodic trajectories via a kernel-ergodic horizon planner with gradient flow and footprint depletion, closing the loop between mapping and trajectory optimization. We thoroughly evaluate TRACE on the Replica dataset against the Next-Best-View (NBV) baselines, improving PSNR by 1.5 dB. Code: this https URL .

</details>

---
