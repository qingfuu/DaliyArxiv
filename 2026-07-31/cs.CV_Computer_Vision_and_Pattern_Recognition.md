# cs.CV | Computer Vision and Pattern Recognition | 2026-07-31

#arxiv #ComputerScience

**论文数**: 10

### [[20_Research/Papers/具身智能/ACE-Data-0_Human-Centric_Ambient_Capture_as_Embodied_Data_Engine|ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine]]

![[assets/2607.28625_figure.png|800]]

- **arXiv**: [2607.28625](https://arxiv.org/abs/2607.28625)
- **PDF**: https://arxiv.org/pdf/2607.28625
- **详细分析**: [[20_Research/Papers/具身智能/ACE-Data-0_Human-Centric_Ambient_Capture_as_Embodied_Data_Engine|ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine]]
- **作者**: Yukang Cao, Haozhe Xie, Beichen Wen, Runmao Yao, Yinghao Liu, Yue Huang, Zhichao Liao, Yunxiang Wang, Haiheng Liu, Xingshun Tian, Dawei Su, Long Zhuo...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型
- **相关性评分**: 2.6（加权：具身智能 2.4，世界模型 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《ACE-Data-0: Human-Centric Ambient Capture as Embodied Data Engine》归入 具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied intelligence faces a fundamental data bottleneck. Models must capture how first-person perception, whole-body motion, dexterous manipulation, object state, sound, and touch evolve together as humans pursue goals over time. Existing datasets fragment this experience across viewpoints, modalities, or spatial scales, leaving the full perception-action loop only partially observed. We introduce the Ambient Capture Engine (ACE), a human-centric data engine that transforms real home environments into spatially calibrated, temporally synchronized recording studios. ACE operates at two complementary scales: a table-scale configuration resolves hand-object manipulation, while a room-scale configuration captures whole-body motion, locomotion, and interactions across a furnished home. ACE records egocentric and multi-view exocentric video, full-body and articulated hand motion, object geometry and 6-DoF trajectories, audio, and tactile signals as a unified multisensory stream. Using ACE, we build ACE-Data-0, comprising 150 hours and 17M video frames across 200 task categories, performed by 50 participants in 2 environments, for a total of 75,000 interaction episodes. The dataset spans atomic manipulation, long-horizon chains of household activities, and human-scene interaction, while preserving natural behavioral variation through goal-level rather than step-by-step instructions. We further introduce a hierarchical benchmark that progresses from signals to scene components and then to interactions. Evaluations of state-of-the-art methods expose substantial gaps under contact, occlusion, egomotion, and long temporal horizons. ACE-Data-0 provides synchronized human demonstrations with aligned perceptual, kinematic, and contact supervision, offering a scalable foundation for imitation learning, world models, vision-language-action systems, and embodied AI.

</details>

---

### [[20_Research/Papers/世界模型/PhiZero_A_World_Model_Built_Around_Physical_Language|PhiZero: A World Model Built Around Physical Language]]

![[assets/2607.28624_figure.png|800]]

- **arXiv**: [2607.28624](https://arxiv.org/abs/2607.28624)
- **PDF**: https://arxiv.org/pdf/2607.28624
- **详细分析**: [[20_Research/Papers/世界模型/PhiZero_A_World_Model_Built_Around_Physical_Language|PhiZero: A World Model Built Around Physical Language]]
- **作者**: Shuyao Shang, Yuqi Wang, Ruopeng Gao, Xu Chen, Tieniu Tan, Lue Fan, Zhaoxiang Zhang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel

#### 研究背景与动机

《PhiZero: A World Model Built Around Physical Language》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：WorldModelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce PhiZero, a physical world model built around physical language, a compact discrete representation of world-state transitions. Existing physical world models typically predict future videos directly in pixel space, leaving the underlying world dynamics implicit within high-dimensional visual predictors. Motivated by humans' ability to abstract predictive structure from visual experience and organize it in natural language for explicit reasoning, we learn physical language from in-the-wild videos through self-supervision and use it to explicitly reason about how the physical world evolves. Accordingly, PhiZero adopts a reason-then-render paradigm: it first infers future world evolution as a physical-language sequence and then renders the inferred transitions into videos. Extensive experiments across generation and understanding benchmarks validate the ability of PhiZero to model physically coherent world evolution. We further show its potential for realistic and interactive world modeling, fine-grained action-conditioned simulation, and zero-shot motion transfer.

</details>

---

### [[20_Research/Papers/大模型/ScaFE_Data-Efficient_Scar_Classification_with_LLM-Generated_Clinical_Feature_Programs|ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature Programs]]

![[assets/2607.28538_figure.png|800]]

- **arXiv**: [2607.28538](https://arxiv.org/abs/2607.28538)
- **PDF**: https://arxiv.org/pdf/2607.28538
- **详细分析**: [[20_Research/Papers/大模型/ScaFE_Data-Efficient_Scar_Classification_with_LLM-Generated_Clinical_Feature_Programs|ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature Programs]]
- **作者**: Ruman Wang, Hangting Ye
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.8（加权：大模型 0.8）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《ScaFE: Data-Efficient Scar Classification with LLM-Generated Clinical Feature Programs》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Classifying pathological scars from clinical photographs requires distinguishing keloids from hypertrophic scars despite limited expert-labeled data and substantial acquisition variation across hospitals. End-to-end image models remain data-dependent, whereas sending photographs to a hosted vision-language model (VLM) may conflict with local data-governance requirements and yields decisions that are difficult to reproduce and audit. We introduce ScaFE (Scar Feature Engineering), which transfers clinical knowledge from a large language model (LLM) into deterministic, executable feature programs instead of asking the model to diagnose images. A web-enabled LLM retrieves clinical evidence and synthesizes programs that measure visually assessable scar attributes. Candidate programs execute in a restricted local environment, and only aggregate validation statistics and feature-level SHAP summaries are returned for iterative repair and refinement; raw images and patient-level outputs remain local. A lightweight Random Forest then operates on the resulting structured representation. On 600 photographs from three hospitals under leave-one-site-out evaluation, ScaFE achieves 81.0% site-macro balanced accuracy, exceeding the strongest baseline, BiomedCLIP, by 10.0 percentage points. With only 10% of the development data, ScaFE retains 72.0% balanced accuracy and an 11.8-point lead. Iterative refinement also raises the executable-program rate from 66.7% to 95.0%, with verified evidence for 91.7% of the final features. These results show that LLM knowledge can support data-efficient, cross-site medical image classification through local and auditable feature programs rather than direct VLM decisions.

</details>

---

### [[20_Research/Papers/具身智能/ViewMind3D_Modular_View-Aware_Inference_for_Training-Free_3D-QA|ViewMind3D: Modular View-Aware Inference for Training-Free 3D-QA]]

![[assets/2607.28442_figure.png|800]]

- **arXiv**: [2607.28442](https://arxiv.org/abs/2607.28442)
- **PDF**: https://arxiv.org/pdf/2607.28442
- **详细分析**: [[20_Research/Papers/具身智能/ViewMind3D_Modular_View-Aware_Inference_for_Training-Free_3D-QA|ViewMind3D: Modular View-Aware Inference for Training-Free 3D-QA]]
- **作者**: Ping-Kun Chiang, Kun-Ru Wu, Po-han Li, Sandeep Chinchali, Ufuk Topcu, Yu-Chee Tseng
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.8（加权：具身智能 0.6，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《ViewMind3D: Modular View-Aware Inference for Training-Free 3D-QA》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSPNet, MV-ScanQA, ScanNet, ScanQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large language models (LLMs) and vision-language models (VLMs) have enabled new possibilities for 3D question answering (3D-QA), a key capability for embodied AI and robotic perception. However, most existing methods rely on 3D-specific training or fine-tuning with costly annotations, limiting their scalability and real-world applicability. We present \textbf{ViewMind3D}, a fully training-free and modular framework for 3D spatial reasoning over multi-view observations of a scene without requiring complete 3D reconstruction. The framework decomposes the 3D-QA task into four interpretable components: (1) question-driven multi-view selection, (2) guided visual grounding with language-conditioned object cues, (3) spatial context encoding via a bird's-eye-view (BEV) viewpoint indicator, and (4) structured answer generation through role-based reasoning. This design enables structured, robust, and interpretable reasoning without requiring model tuning. Experimental results on ScanQA and SQA3D show that ViewMind3D achieves competitive performance compared to prior training-free and fine-tuned 3D-LLMs. In particular, our method improves performance on spatially grounded question types, such as ``What'' questions in SQA3D, while maintaining strong overall accuracy (50.8\%) and achieving 73.4 CIDEr on ScanQA. These results demonstrate that effective 3D reasoning can be achieved through modular orchestration of general-purpose LLMs and VLMs for robotic perception in real-world environments.

</details>

---

### [[20_Research/Papers/具身智能/Hand-Object_Interaction_in_the_Age_of_Large_Foundation_Models_Reconstruction,_Generation,_and_Embodied_Transfer|Hand-Object Interaction in the Age of Large Foundation Models:Reconstruction, Generation, and Embodied Transfer]]

![[assets/2607.28394_figure.png|800]]

- **arXiv**: [2607.28394](https://arxiv.org/abs/2607.28394)
- **PDF**: https://arxiv.org/pdf/2607.28394
- **详细分析**: [[20_Research/Papers/具身智能/Hand-Object_Interaction_in_the_Age_of_Large_Foundation_Models_Reconstruction,_Generation,_and_Embodied_Transfer|Hand-Object Interaction in the Age of Large Foundation Models:Reconstruction, Generation, and Embodied Transfer]]
- **作者**: Weiquan Lin, Yu Deng, Shiyang Liu, Luping Xiao, Xu Tang, Junzhi Yu, Jiaolong Yang, Lei Zhang, Xingyu Chen
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.9，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Hand-Object Interaction in the Age of Large Foundation Models:Reconstruction, Generation, and Embodied Transfer》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ControlNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hand-object interaction (HOI) modeling remains challenging because it requires joint reasoning about hand articulation, object geometry, contact, semantics, and dynamics under severe visual uncertainty. Foundation models introduce transferable prior knowledge learned from large-scale cross-domain data, offering new ways to address these challenges beyond task-specific data and models. However, the rapidly growing literature remains fragmented, and existing studies typically describe these methods simply as ``using large models'' without systematically characterizing what knowledge is introduced, where it enters the HOI pipeline, or which HOI uncertainty it helps reduce. This survey presents the first systematic review of foundation-model priors for HOI. We organize the literature into six HOI tasks spanning reconstruction and generation. More importantly, we establish a taxonomy of eight foundation-model sub-priors grouped into geometric, semantic, and visual families. Geometric priors encompass shape retrieval, shape reconstruction, and spatial reconstruction; semantic priors include semantic grounding and language reasoning; and visual priors cover visual representation, image generation, and video generation. Based on this taxonomy, we systematically analyze how different priors are represented, injected, and adapted across HOI pipelines and tasks. Beyond how foundation models empower HOI, we further examine how HOI-derived knowledge is used in robot learning, including human-data pretraining, human-to-robot skill transfer, and HOI-to-robot data generation. Finally, we summarize datasets and evaluation protocols, and discuss limitations and future directions toward more generalizable HOI systems. To support long-term progress, we curate a live repository that continuously aggregates emerging methods and benchmarks.

</details>

---

### [[20_Research/Papers/机器人/AdaAnchor4D_Anchor-Conditioned_Spatiotemporal_Feature_Aggregation_for_Monocular_UAV_4D_Reconstruction|AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction]]

![[assets/2607.28320_figure.png|800]]

- **arXiv**: [2607.28320](https://arxiv.org/abs/2607.28320)
- **PDF**: https://arxiv.org/pdf/2607.28320
- **详细分析**: [[20_Research/Papers/机器人/AdaAnchor4D_Anchor-Conditioned_Spatiotemporal_Feature_Aggregation_for_Monocular_UAV_4D_Reconstruction|AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction]]
- **作者**: Peiyi Xu, Junpeng Zhang, Guanbin Li, Ronghua Shang, Mingtao Feng, Le Dong, Weisheng Dong, Guangming Shi, Jie Feng
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: cs.CV

#### 研究背景与动机

《AdaAnchor4D: Anchor-Conditioned Spatiotemporal Feature Aggregation for Monocular UAV 4D Reconstruction》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Monocular UAV videos provide valuable observations for dynamic reconstruction of complex urban scenes. However, such scenes exhibit pronounced spatiotemporal heterogeneity: different regions follow distinct temporal activity patterns, while the motion states of some dynamic regions may further evolve over time. Although dynamic Gaussian methods based on decomposed shared spatiotemporal feature fields have achieved efficient and accurate reconstruction in object-centric or relatively compact scenes, their commonly adopted fixed plane-wise feature combination mechanisms are less suited to the heterogeneous local dynamics of UAV scenes, often leading to ghosting artifacts and blurred dynamic details. To address this challenge, we propose AdaAnchor4D, an adaptive anchor deformation framework for monocular UAV dynamic scene reconstruction. At its core, Anchor-Conditioned Feature Aggregation (ACFA) adaptively aggregates shared spatiotemporal features using anchor-specific aggregation embeddings and temporal information, allowing different local units to obtain dynamic representations tailored to their local and temporal states. Decoupled Local Geometry Deformation (DLGD) separates anchor-state deformation from local Gaussian geometry deformation, while Density-Adaptive Coordinate Warping (DACW) reparameterizes feature-query coordinates according to the axis-wise anchor distributions, alleviating the mismatch between non-uniform geometric sampling and uniform grid parameterization. Experiments on UAV-Arc4D, VisDrone, and UAVDT show that AdaAnchor4D achieves higher rendering quality than representative dynamic Gaussian methods while maintaining real-time rendering performance. The code will be made publicly available.

</details>

---

### [[20_Research/Papers/大模型/FaithEyes_Towards_Faithful_Tool_Use_via_Multi-Agent_Process-Image_Verification|FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification]]

![[assets/2607.28225_figure.png|800]]

- **arXiv**: [2607.28225](https://arxiv.org/abs/2607.28225)
- **PDF**: https://arxiv.org/pdf/2607.28225
- **详细分析**: [[20_Research/Papers/大模型/FaithEyes_Towards_Faithful_Tool_Use_via_Multi-Agent_Process-Image_Verification|FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification]]
- **作者**: Haoqing Wang, Xingrun Xing, Wei Xia, Ziheng Li, Yehui Tang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.6（加权：大模型 0.6）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《FaithEyes: Towards Faithful Tool Use via Multi-Agent Process-Image Verification》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HR-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic vision-language models (VLMs), which interleave textual reasoning with explicit tool calls such as cropping and code-based image manipulation, have emerged as a compelling paradigm for reliable and interpretable multimodal reasoning. However, recent studies have revealed that such models often use tools unfaithfully. Many process images are irrelevant to the question (e.g., the tool crops the wrong region or misses the queried target), yet the call still receives full credit and the model still answers correctly. Such decorative or misaligned tool calls waste computation and reveal that the model leans on prior knowledge or the original image rather than the evidence it retrieves. This may stem from two limitations of prevailing methods: the tool reward fails to distinguish useful from useless calls, and tool feedback carries no signal of usefulness. To this end, we introduce FaithEyes, a multi-agent self-judging framework. Concretely, we use a VLM to judge whether each process image helps answer the question. The judgement is injected into the reasoning context as part of the tool observation to help subsequent reasoning, and meanwhile is used to scale the tool reward by the helpful-tool ratio to suppress reward hacking. To keep judgement available at evaluation and thus ensure train-test consistency, we further design a multi-agent framework where the model itself serves as a subagent to judge the tool calls from main agent, eliminating any dependence on an external model at inference. Training via a two-stage SFT + RL pipeline on adapted open-source data, FaithEyes attains competitive or superior accuracy across visual perception and reasoning benchmarks, while markedly improving tool faithfulness. The homepage is at https://github.com/Mosi-AI/FaithEyes.

</details>

---

### [[20_Research/Papers/具身智能/UniCross_Unified_Cross-Skill_Dexterous_Manipulation_Synthesis|UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis]]

![[assets/2607.28198_figure.png|800]]

- **arXiv**: [2607.28198](https://arxiv.org/abs/2607.28198)
- **PDF**: https://arxiv.org/pdf/2607.28198
- **详细分析**: [[20_Research/Papers/具身智能/UniCross_Unified_Cross-Skill_Dexterous_Manipulation_Synthesis|UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis]]
- **作者**: Hui Zhang, Julian Ferchow, Jie Song, Mirko Meboldt
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《UniCross: Unified Cross-Skill Dexterous Manipulation Synthesis》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：IsaacGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many dexterous manipulation tasks require the object to remain securely held throughout the interaction. From the perspective of hand-object relational motion, such manipulation comprises four canonical skills: grasping, relocation, in-hand rotation, and in-hand translation. Human hands flexibly compose these skills to accomplish complex tasks. Existing approaches, however, model these skills separately with skill-specific action constraints, objectives, or even dedicated hand morphologies, which breaks the compatibility and continuity required for long-horizon composition. In this work, we present a unified framework that models all four skills in a single formulation that shares the same state and action spaces and a common objective structure. This formulation enables straightforward distillation of a single cross-skill policy that performs strongly on every skill, generalizes to unseen objects, stays robust to disturbances, and chains skills seamlessly into long-horizon manipulation. The framework also transfers effectively across different hand morphologies. Overall, our results suggest that different dexterous manipulation skills can be viewed as instantiations of a shared task formulation, revealing the intrinsic consistency across different behaviors.

</details>

---

### [[20_Research/Papers/强化学习/GVR-Coder_A_Visual-Feedback_Framework_for_Structured_SVG_Generation_in_Complex_Document_and_Meeting_Scenarios|GVR-Coder: A Visual-Feedback Framework for Structured SVG Generation in Complex Document and Meeting Scenarios]]

![[assets/2607.28073_figure.png|800]]

- **arXiv**: [2607.28073](https://arxiv.org/abs/2607.28073)
- **PDF**: https://arxiv.org/pdf/2607.28073
- **详细分析**: [[20_Research/Papers/强化学习/GVR-Coder_A_Visual-Feedback_Framework_for_Structured_SVG_Generation_in_Complex_Document_and_Meeting_Scenarios|GVR-Coder: A Visual-Feedback Framework for Structured SVG Generation in Complex Document and Meeting Scenarios]]
- **作者**: Yiming Xu, Jihua Kang, Chunsai Du, Qifan Zhang, Wangqiu Zhou, Yiting Wu, Tianqi Li, Qi Song
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 0.62（加权：大模型 0.1，强化学习 0.36，世界模型 0.16）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《GVR-Coder: A Visual-Feedback Framework for Structured SVG Generation in Complex Document and Meeting Scenarios》归入 强化学习、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In demanding professional environments and meeting review scenarios, lengthy text often imposes a high cognitive load. To facilitate efficient information communication, transforming verbose text into logically clear diagrams is essential. Scalable Vector Graphics (SVG) provide an effective representation for this purpose due to their editability and resolution independence. However, current research on Text-to-SVG generation remains hindered by three major challenges: (1) the scarcity of datasets for complex, logic-rich diagrams; (2) the absence of explicit layout priors, which leads to chaotic spatial arrangements; and (3) the lack of fine-grained visual feedback to validate rendered outputs and correct aesthetic defects. To address these challenges, at the data level, we introduce DocMeetSVG-100K, a large-scale SVG dataset tailored for document authoring and meeting review scenarios. At the model level, we propose GVR-Coder, a novel framework designed to generate high-quality logical diagrams from lengthy professional texts. Specifically, we adopt a curriculum-driven rejection sampling fine-tuning to progressively enhance the model's capability in modeling complex structures, while explicitly incorporating layout constraint knowledge during training. In addition, we introduce reinforcement learning from dual rendering feedback, a mechanism that provides implicit feedback through reward signals to jointly optimize structural complexity and visual aesthetics. Furthermore, we design a generate-verify-repair agent loop, which improves generation quality through explicit, fine-grained feedback and targeted refinement. Extensive experiments demonstrate that GVR-Coder outperforms competitive baselines and reliably produces logically coherent and visually appealing diagrams. Code and data are available at https://github.com/CurryaNa/GVR-Coder.

</details>

---

### [[20_Research/Papers/强化学习/ODEWorld_A_Continuous_Predictive_Architecture_via_Physical-Time_Flow|ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow]]

![[assets/2607.27924_figure.png|800]]

- **arXiv**: [2607.27924](https://arxiv.org/abs/2607.27924)
- **PDF**: https://arxiv.org/pdf/2607.27924
- **详细分析**: [[20_Research/Papers/强化学习/ODEWorld_A_Continuous_Predictive_Architecture_via_Physical-Time_Flow|ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow]]
- **作者**: Dongxiu Liu, Haoyi Niu, Peng Cheng, Yuan Gao, Xirui Kang, Sangli Teng, Koushil Sreenath, Xianyuan Zhan
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 强化学习
- **相关性评分**: 1.32（加权：具身智能 0.3，强化学习 0.16，世界模型 0.36，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《ODEWorld: A Continuous Predictive Architecture via Physical-Time Flow》归入 机器人、世界模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgiBot-World, Agibot-World, ODEWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the physical world we inhabit, space and time are fundamentally continuous. However, existing machine learning paradigms for world modeling are largely confined to discrete-time prediction, thereby exhibiting significant inefficiency in capturing the dynamics of physical world. We introduce Physical-Time Flow (\textbf{PT-Flow}), a novel approach that learns a continuous latent velocity field operating in physical time. Crucially, the underlying dynamics of sequential data are parameterized by an ordinary differential equation (ODE) embedded in a well-structured representation space. Under this paradigm, the prediction of future can be recast as temporal integration via an ODE solver in the compressed latent space. Building upon PT-Flow, we construct \textbf{ODEWorld}, a continuous-time latent world model that is both efficient and versatile. By extracting time-variant features and enforcing ODE properties on both the dynamical representation space and the latent velocity field, ODEWorld effectively addresses the long-standing representation collapse issue in latent world model literature. This also enables high-quality image reconstruction even after long-horizon prediction. Moreover, its continuous nature allows for arbitrary temporal resolution and even backward prediction, which is impossible for most discrete-time models. Lastly, ODEWorld can provide rich planning-oriented information to facilitate downstream policy learning. Comprehensive experiments demonstrate that ODEWorld successfully reconciles planning-conducive dynamics abstraction with visual realism, excelling in both video generation and robotic control. \href{https://dstate.github.io/odeworld_website/}{Project Website}.

</details>

---
