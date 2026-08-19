# cs.CV | Computer Vision and Pattern Recognition | 2026-08-17

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/强化学习/Designing_Reinforcement_Learning_for_Diffusion_Models_A_Unified_Path-Space_View|Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View]]

![[assets/2608.14430_figure.png|800]]

- **arXiv**: [2608.14430](https://arxiv.org/abs/2608.14430)
- **PDF**: https://arxiv.org/pdf/2608.14430
- **详细分析**: [[20_Research/Papers/强化学习/Designing_Reinforcement_Learning_for_Diffusion_Models_A_Unified_Path-Space_View|Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View]]
- **作者**: Yixian Xu, Yuanrui Zhang, Shengjie Luo, Liwei Wang, Di He
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《Designing Reinforcement Learning for Diffusion Models: A Unified Path-Space View》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GenEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training provides a direct way to align diffusion models with human preferences and task-specific rewards. However, current RL algorithms for diffusion models remain fragmented: reverse-trajectory methods rely on discretized likelihood ratios, whereas forward-matching methods train on reward-labeled noising versions of the rollout samples. This paper shows that these seemingly different losses arise from a single path-space principle. Starting from the regularized diffusion-RL objective, we use importance sampling between sampling SDEs to obtain an explicit policy-gradient estimator on trajectory space. The estimator contains the stochastic Itô integral underlying Flow-GRPO-type updates; we derive an equivalent variance-reduced value-gradient form that recovers the forward-matching structure of AWM and DiffusionNFT. This identifies the empirical gap between these method families as a variance-reduction effect rather than a difference in RL principle. The derivation yields a unified design space organized by value-gradient estimation, weight functions, and sampling choices. Within this space, we propose a multi-sample KDE value-gradient estimator that reuses rollout groups, together with scale-bounded weight families that retain stable existing recipes while excluding singular ones. Experiments on SD3.5-M and Qwen-Image models validate the variance-reduction explanation and show that the resulting recipe improves over prior diffusion-RL baselines.

</details>

---

### [[20_Research/Papers/具身智能/PRM-as-a-Judge_1.5_A_Toolkit_for_Robot_Process_Assessment|PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment]]

![[assets/2608.14284_figure.png|800]]

- **arXiv**: [2608.14284](https://arxiv.org/abs/2608.14284)
- **PDF**: https://arxiv.org/pdf/2608.14284
- **详细分析**: [[20_Research/Papers/具身智能/PRM-as-a-Judge_1.5_A_Toolkit_for_Robot_Process_Assessment|PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment]]
- **作者**: Yuyang Liu, Yanqing Shen, Ruike Chen, Jifan Zhao, Yuxuan Tian, Yichi Zhang, Tianfeng Long, Zixuan Yin, Yipu Wang, Ziheng Qin, Wenxing Tan, Yang Shi...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《PRM-as-a-Judge 1.5: A Toolkit for Robot Process Assessment》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GalaxeaVLA, GigaWorld, InternVLA, Real-World, RoboDojo-RealWorld, RoboDojo-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-grained robotic evaluation matters for understanding embodied models, going beyond binary success rates and rule-based process scores. We present PRM-as-a-Judge 1.5, a toolkit for robot process assessment that turns rollout videos into dense progress curves and derives multiple fine metrics. PRM-as-a-Judge 1.5 introduces three metrics, building on version 1.0, that characterize failure-side progress, post-drawdown recovery, and success-side execution quality, helping users understand embodied model capability. Based on the rollout videos from benchmarks, we perform a comprehensive assessment of the embodied models, providing some fine-grained metric results and key findings. We further introduce RoboPulse++ to evaluate the reliability of process reward models (PRM), providing evaluators with a more accurate testing platform. Moreover, we release a user-friendly assessment suite, including the benchmark, metric implementation, and visualization tools, to support reproducible manipulation process evaluation. We call on the community to rethink how robots are evaluated and establish transparent, procedural, and reproducible assessment as a foundation for the next generation of embodied intelligence.

</details>

---

### [[20_Research/Papers/具身智能/SSP_An_Event-Matched_Syn2Sim2Phy_Cross-Domain_Evaluation_Framework_for_Autonomous_Driving_VLA_Models|SSP: An Event-Matched Syn2Sim2Phy Cross-Domain Evaluation Framework for Autonomous Driving VLA Models]]

![[assets/2608.14024_figure.png|800]]

- **arXiv**: [2608.14024](https://arxiv.org/abs/2608.14024)
- **PDF**: https://arxiv.org/pdf/2608.14024
- **详细分析**: [[20_Research/Papers/具身智能/SSP_An_Event-Matched_Syn2Sim2Phy_Cross-Domain_Evaluation_Framework_for_Autonomous_Driving_VLA_Models|SSP: An Event-Matched Syn2Sim2Phy Cross-Domain Evaluation Framework for Autonomous Driving VLA Models]]
- **作者**: Haojie Feng, Peizhi Zhang, Xinrui Zhang, Zhuoren Li, Junpeng Huang, Xiurong Wang, Dongxiao Yin, Yuxiang Zhang, Junfan Zhu, Lu Xiong
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《SSP: An Event-Matched Syn2Sim2Phy Cross-Domain Evaluation Framework for Autonomous Driving VLA Models》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models for autonomous driving jointly produce scene interpretation, language-based reasoning, and driving trajectories. Existing evaluations often use independently selected synthetic, simulated, and physical data, so measured performance gaps can be confounded by changes in scenario content rather than genuine domain sensitivity. We propose SSP (Synthetic-Simulation-Physical), an event-matched Syn2Sim2Phy evaluation framework that anchors cross-domain comparison to the same safety-critical interaction. Starting from a synthetic long-tail video, SSP builds a validated event specification that preserves road topology, participant roles, relative motion, conflict evolution, passing order, response constraints, and event phases. Platform-specific realizations are then constructed in CARLA and on a closed proving ground and are evaluated only after transfer audits confirm preservation of mandatory event properties. SSP maps heterogeneous outputs from OpenEMMA, LLaViDA, and Alpamayo-R1 into common semantic slots and a 1 s trajectory window to assess output validity, semantic accuracy, critical-interaction recognition, trajectory quality, and risk response. Across Cut-in and vulnerable-road-user crossing cases, the macro-averaged Integrated VLA Capability Scores are 0.259, 0.291, and 0.325 in the Synthetic, Simulation, and Physical domains, respectively, while the best domain varies by scenario. Alpamayo-R1, OpenEMMA, and LLaViDA obtain scores of 0.405, 0.338, and 0.131. SSP provides a reproducible scene-transfer chain and an evidence-qualified evaluation of VLA behavior without assuming that the Physical domain is universally superior.

</details>

---

### [[20_Research/Papers/大模型/Rethinking_Auxiliary_Modalities_in_Multimodal_Zero-shot_Anomaly_Detection_From_Semantic_Fusion_to_Conditional_Modulation|Rethinking Auxiliary Modalities in Multimodal Zero-shot Anomaly Detection: From Semantic Fusion to Conditional Modulation]]

![[assets/2608.13973_figure.png|800]]

- **arXiv**: [2608.13973](https://arxiv.org/abs/2608.13973)
- **PDF**: https://arxiv.org/pdf/2608.13973
- **详细分析**: [[20_Research/Papers/大模型/Rethinking_Auxiliary_Modalities_in_Multimodal_Zero-shot_Anomaly_Detection_From_Semantic_Fusion_to_Conditional_Modulation|Rethinking Auxiliary Modalities in Multimodal Zero-shot Anomaly Detection: From Semantic Fusion to Conditional Modulation]]
- **作者**: Peng Wu, Xin Ge, Yujia Sun, Guansong Pang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《Rethinking Auxiliary Modalities in Multimodal Zero-shot Anomaly Detection: From Semantic Fusion to Conditional Modulation》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EasyNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent foundation model-based methods have endowed RGB images with strong zero-shot anomaly detection (ZSAD) through vision-language pretraining. However, RGB observations alone remain limited in perceiving anomalies dominated by geometric deformation, depth variation, or subtle surface changes. Auxiliary modalities can provide complementary structural information, but existing multimodal methods typically fuse them directly into a shared semantic space, which may disturb the text-aligned anomaly semantics established by RGB foundation models and often requires modality-specific architectures. To address this issue, we propose a plug-and-play auxiliary-conditioned enhancement framework for zero-shot anomaly detection. Instead of reconstructing a joint multimodal anomaly semantic space, our framework preserves the original RGB image-text anomaly matching pathway and uses auxiliary observations as conditional signals for RGB feature refinement, allowing auxiliary modalities to seamlessly enhance existing RGB-based zero-shot anomaly detectors. Specifically, a lightweight meta-learning module takes global RGB and auxiliary representations as input and generates sample-adaptive low-rank residual updates to determine how RGB features should be refined. We further construct uncertainty-aware spatial modulation from the initial RGB anomaly response and auxiliary reliability, which determines where local residual updates are strengthened or suppressed. This global-to-local conditional modulation enables selective multimodal enhancement while preserving the original RGB anomaly semantics. Extensive experiments on MVTec 3D-AD and Eyecandies demonstrate that our framework consistently improves multiple popular RGB-based zero-shot anomaly detectors, achieving state-of-the-art performance for multimodal zero-shot anomaly detection.

</details>

---

### [[20_Research/Papers/大模型/Label-Free_Deep-Tissue_Peripheral_Nerve_Detection_with_a_Handheld_Multimodal_OCT_Probe_and_NerveDetNet|Label-Free Deep-Tissue Peripheral Nerve Detection with a Handheld Multimodal OCT Probe and NerveDetNet]]

![[assets/2608.13807_figure.png|800]]

- **arXiv**: [2608.13807](https://arxiv.org/abs/2608.13807)
- **PDF**: https://arxiv.org/pdf/2608.13807
- **详细分析**: [[20_Research/Papers/大模型/Label-Free_Deep-Tissue_Peripheral_Nerve_Detection_with_a_Handheld_Multimodal_OCT_Probe_and_NerveDetNet|Label-Free Deep-Tissue Peripheral Nerve Detection with a Handheld Multimodal OCT Probe and NerveDetNet]]
- **作者**: Yihan Wang, Ruilin You, Shaobai Li, Jiabin Chen, Bofan Song, Anh D. Le, Rongguang Liang
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《Label-Free Deep-Tissue Peripheral Nerve Detection with a Handheld Multimodal OCT Probe and NerveDetNet》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：NerveDetNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Peripheral nerves buried beneath intact tissue are difficult to visualize during surgery and remain inaccessible to white light wide-field imaging and other surface optical imaging methods. Existing OCT nerve studies have largely relied on exposed nerves or polarization contrast with limited depth penetration, restricting their value for subsurface intraoperative guidance. Here, we introduce, to our knowledge, the first label-free framework for detecting peripheral nerves beneath unopened tissue and resolving their depth using intensity-based OCT structural signatures alone. The framework combines a handheld multimodal probe, integrating swept-source OCT with co-registered white light and autofluorescence imaging, with a ``confirm-then-capture'' workflow designed for practical surgical use. To enable efficient analysis of sparsely sampled OCT volumes, we develop NerveDetNet, a lightweight 2.5D segmentation network that recovers weak and spatially displaced nerve signals by incorporating spatial context, frame-order information, and shift-tolerant correlations across frames through a dedicated nerve feature correlation module. In ex vivo tissue experiments, NerveDetNet consistently outperformed six representative 2D baselines across all frame spacings, achieving a Dice score of 0.725 under the sparsest sampling condition while using approximately half the model parameters. End-to-end validation demonstrated localization of nerves invisible at the surface and depth-resolved detection up to 1.3--1.4~mm below the tissue surface, with OCT derived depth maps overlaid directly onto the surgical view. Together, these results establish a practical label-free approach for subsurface nerve visualization that supports intraoperative compatibility, enables efficient sparse-volume analysis, and provides depth-resolved guidance without tissue opening, contrast agents, or nerve exposure.

</details>

---

### [[20_Research/Papers/大模型/VLM-_and_LLM-Driven_Multi-Agent_System_for_PET_Image_Denoising|VLM- and LLM-Driven Multi-Agent System for PET Image Denoising]]

![[assets/2608.13791_figure.jpg|800]]

- **arXiv**: [2608.13791](https://arxiv.org/abs/2608.13791)
- **PDF**: https://arxiv.org/pdf/2608.13791
- **详细分析**: [[20_Research/Papers/大模型/VLM-_and_LLM-Driven_Multi-Agent_System_for_PET_Image_Denoising|VLM- and LLM-Driven Multi-Agent System for PET Image Denoising]]
- **作者**: Boxiao Yu, Savas Ozdemir, Yang Xing, Fumio Hashimoto, Jiong Wu, Yizhou Chen, Axel Rominger, Ruogu Fang, Kuangyu Shi, Tinsu Pan, Kuang Gong
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.2（加权：大模型 1.2）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《VLM- and LLM-Driven Multi-Agent System for PET Image Denoising》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ResNet, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Positron emission tomography (PET) imaging suffers from limited spatial resolution and low signal-to-noise ratio, which can compromise quantitative accuracy and lesion detectability. Deep learning-based denoising methods have demonstrated strong potential for improving PET image quality. However, their practical deployment in real-world settings remains challenging, often requiring multiple specialized models and expert interventions, such as identifying motion-induced misregistration artifacts, estimating noise levels to select an appropriate denoiser, and performing lesion-focused quantitative assessment after denoising. Recent advances in vision-language models (VLMs) for image quality understanding and large language models (LLMs) for contextual reasoning provide new opportunities for automated, decision-driven workflows. Inspired by expert workflows for PET image quality enhancement, we propose an VLM- and LLM-driven multi-agent PET denoising framework that dynamically assesses image quality and lesion status, autonomously selects optimal denoising models and parameters, and enables closed-loop feedback with rollback mechanisms. Experiments were conducted on Siemens Biograph Vision Quadra PET/CT data with 1/20 and 1/50 low-dose settings. Individual module evaluations demonstrated the reliability of the agentic components, while the complete framework achieved higher PSNR and SSIM than UNet, GAN, and DDPM baselines at both dose levels. These preliminary results demonstrate the feasibility of using a closed-loop multi-agent framework to adapt PET denoising strategies to different image conditions.

</details>

---
