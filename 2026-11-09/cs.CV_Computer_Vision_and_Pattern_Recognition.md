# cs.CV | Computer Vision and Pattern Recognition | 2026-11-09

#arxiv #ComputerScience

**论文数**: 8

### [[20_Research/Papers/强化学习/Seeing_What_Matters_Benchmarking_Task-Conditioned_Actionable_Spatial_Belief_for_Manipulation|Seeing What Matters: Benchmarking Task-Conditioned Actionable Spatial Belief for Manipulation]]

![[assets/2611.09794_figure.png|800]]

- **arXiv**: [2611.09794](https://arxiv.org/abs/2611.09794)
- **PDF**: https://arxiv.org/pdf/2611.09794
- **详细分析**: [[20_Research/Papers/强化学习/Seeing_What_Matters_Benchmarking_Task-Conditioned_Actionable_Spatial_Belief_for_Manipulation|Seeing What Matters: Benchmarking Task-Conditioned Actionable Spatial Belief for Manipulation]]
- **作者**: Yina Jian, Mingkun Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Seeing What Matters: Benchmarking Task-Conditioned Actionable Spatial Belief for Manipulation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ActiveVLA, ESI-Bench, EmbodiedQA, OpenVLA, RLBench, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When should a robot look at the cup, and when at the portafilter? Spatial-reasoning benchmarks evaluate whether a model can describe a scene, but manipulation needs something more specific: the ability to acquire the particular evidence that makes the current command executable. A view that is informative for one task can be useless for another, even at the same workstation. We introduce Seeing What Matters, a benchmark for task-conditioned actionable spatial belief in simulated tabletop manipulation. Across three domains--coffee workstation, drawer/cabinet, and microwave/appliance--the benchmark provides 860 frozen evaluation cases; expanding across methods, budgets, and inference repeats yields more than 115,000 evaluator episodes under two protocols: closed-loop actionability and same-object functional out-of-distribution generalization. Each case pairs a set of candidate RGB views with a manipulation command, shared scripted skills, and hidden postconditions, so the benchmark directly measures whether a view-selection policy acquires the observations its command actually needs. We also provide a diagnostic reference pipeline that maintains a spatial-functional belief state and ranks views by missing evidence. At primary budget settings, this pipeline reaches 98.8% closed-loop and 98.9% functional-OOD success; ablating the functional or command-binding components collapses performance to near zero. Seven vision-language models, evaluated on the same cases, reach only 26-43%. Replacing the reference pipeline's coverage metadata with frozen RGB-derived scores preserves 98.5%/98.9% success; shuffling the visual scores collapses it to 15%/11%, confirming that the result depends on image content. These gaps suggest that spatial belief for manipulation should be evaluated not by scene-level completeness, but by whether it acquires the evidence the current command requires.

</details>

---

### [[20_Research/Papers/大模型/Zero-Shot_Benchmarking_of_Unified_Multimodal_Models_for_Shallow-Water_UAV_Image_Distortion_Assessment_and_Restoration|Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration]]

![[assets/2611.09740_figure.png|800]]

- **arXiv**: [2611.09740](https://arxiv.org/abs/2611.09740)
- **PDF**: https://arxiv.org/pdf/2611.09740
- **详细分析**: [[20_Research/Papers/大模型/Zero-Shot_Benchmarking_of_Unified_Multimodal_Models_for_Shallow-Water_UAV_Image_Distortion_Assessment_and_Restoration|Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration]]
- **作者**: Dario Scilla, Omar A. Lopez, Mattia Rosso, Kasper Johansen, Matthew F. McCabe
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，机器人 0.8）
- **关联关键词**: Multimodal, ComputerVision

#### 研究背景与动机

《Zero-Shot Benchmarking of Unified Multimodal Models for Shallow-Water UAV Image Distortion Assessment and Restoration》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GIR-Bench, UQ-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Shallow-water UAV imagery provides centimeter-scale observations of benthic environments, but water-induced distortions complicate interpretation. To our knowledge, we present the first systematic zero-shot benchmark of unified multimodal large language models (MLLMs) for both assessing water-induced distortions and restoring shallow-water imagery within the same model framework. We evaluate five open-weight unified MLLMs with frozen pretrained weights and without access to paired reference images or descriptions of the true seabed. The benchmark contains 1,000 image pairs: 600 semi-synthetic UAV scenes created by applying synthetic water distortions to real shallow-water imagery and 400 fully synthetic through-water scenes. Three independent human annotations cover five distortion types. We evaluate four assessment prompts (P0-P3), from direct instruction to structured task decomposition, on all 1,000 images and four diagnosis-guided restoration prompts (R0-R3) on a common 100-image subset. Assessment varies substantially by model and prompt, with systematic prediction biases and a best pooled balanced accuracy of 0.654 for distortion presence. The best pooled PSNR gain is +0.255 dB, no unified MLLM improves pooled LPIPS, and some outputs alter scene structure or hallucinate content. Two restoration-only baselines also show limited transfer: InstructIR achieves a pooled PSNR gain of +0.040 dB, while PromptFix degrades all four pooled metrics under every prompt. These results show that recognizing shallow-water degradation does not imply reliable physical restoration and provide a reproducible baseline for future work.

</details>

---

### [[20_Research/Papers/大模型/Grounding-Aware_Judge_Reward_Reinforcement_Learning_for_Out-of-Domain_Face_Anti-Spoofing|Grounding-Aware Judge Reward Reinforcement Learning for Out-of-Domain Face Anti-Spoofing]]

![[assets/2611.09047_figure.png|800]]

- **arXiv**: [2611.09047](https://arxiv.org/abs/2611.09047)
- **PDF**: https://arxiv.org/pdf/2611.09047
- **详细分析**: [[20_Research/Papers/大模型/Grounding-Aware_Judge_Reward_Reinforcement_Learning_for_Out-of-Domain_Face_Anti-Spoofing|Grounding-Aware Judge Reward Reinforcement Learning for Out-of-Domain Face Anti-Spoofing]]
- **作者**: Xiaoyong Yu, Xinge Yu
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型
- **相关性评分**: 1.5（加权：大模型 0.5，强化学习 1）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《Grounding-Aware Judge Reward Reinforcement Learning for Out-of-Domain Face Anti-Spoofing》归入 强化学习、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ResNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Face Anti-Spoofing (FAS) must distinguish genuine faces from presentation attacks. A unified Multimodal Large Language Model (MLLM) is an attractive solution: it detects physical attacks (print, replay, mask) in one model and produces interpretable forensic evidence via Chain-of-Thought (CoT). A central obstacle to post-training such a model with reinforcement learning is that FAS reasoning has no rule-verifiable ground truth: only the binary verdict is checkable, while the reasoning chain cannot be verified by any hand-crafted rule. Optimizing the verdict alone is therefore a sparse, hackable signal. The model can reach the correct answer through a shortcut such as a false-rejection bias, which does not generalize. We address this with a grounding-aware judge reward. A 32B vision-language judge scores each reasoning chain against the image on evidence anchoring, logical coherence, and domain knowledge, turning the image itself into the verification signal. The reward is applied in a Group Relative Policy Optimization (GRPO) stage after CoT supervised fine-tuning. It is the judge, rather than the RL objective, that supplies the process supervision a verdict-only reward cannot. Our study starts from a model that already performs well In-Domain (ID) after CoT-based supervised fine-tuning and asks how to improve its Out-of-Domain (OOD) generalization. We find that grounding-aware rewards are an effective means to that end. We validate the method on OOD generalization, where the reward reduces ACER on two physical benchmarks (LCC-FASD 0.288 to 0.273, MSU-MFSD 0.431 to 0.409) while preserving ID accuracy (CelebA-Spoof 0.033 to 0.035). Against ResNet-50/101 and CLIP-ViT-B/16 baselines, the MLLM dominates ID and matches or surpasses the strongest baseline OOD. To our knowledge this is the first use of LLM-as-judge process supervision for FAS.

</details>

---

### [[20_Research/Papers/具身智能/DobotTrack_Target-Grounded_Vision-Language-Action_Learning_for_Embodied_Person_Tracking|DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking]]

![[assets/2611.09041_figure.png|800]]

- **arXiv**: [2611.09041](https://arxiv.org/abs/2611.09041)
- **PDF**: https://arxiv.org/pdf/2611.09041
- **详细分析**: [[20_Research/Papers/具身智能/DobotTrack_Target-Grounded_Vision-Language-Action_Learning_for_Embodied_Person_Tracking|DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking]]
- **作者**: Shengjun Deng, Yinghan Zhang, Chengrui Wei, Liu Liang, Songyuan Liu, Pengkun Zheng, Yajun Zheng, Ying Zhang, Yuan Tian, Xi Li, Teng Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.1（加权：具身智能 3.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《DobotTrack: Target-Grounded Vision-Language-Action Learning for Embodied Person Tracking》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EVT-Bench, OmTrackVLA, Real-World, TPT-Bench, TrackVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-guided embodied person tracking requires a mobile agent to identify a target from a referring description and consistently follow the target under egocentric observations. We present DobotTrack, a target-grounded vision-language-action (VLA) framework that integrates auxiliary grounding supervision with efficient temporal modeling. We systematically investigate five auxiliary tasks---person segmentation, bounding-box grounding, visual-spatial classification (VSC), future DINO feature prediction, and future-frame prediction---and adopt complementary mask and bounding-box supervision to enhance target delineation and localization. We introduce Q-identity, a target-conditioned historical visual compression module that leverages target-grounding predictions to selectively preserve identity-discriminative appearance features and spatial cues in compact historical tokens. On EVT-Bench, our 0.8B-parameter model achieves an average success rate of 77.9%, exceeding OmTrackVLA by 16.9 percentage points across the three tasks. We further construct a real-world person-tracking dataset collected using a quadruped robot, comprising 126 episodes and 596,323 mask-annotated frames. The target masks enable automatic derivation of bounding boxes and visual-spatial labels encoding horizontal position and apparent image scale, providing additional grounding supervision without separate manual annotation of these labels. Together, our framework and annotation pipeline support learning target-grounded tracking policies from simulated and real-world data. Code is available at https://github.com/Dobot-Team/dobot_track.

</details>

---

### [[20_Research/Papers/机器人/UAV-Based_Computer_Vision_for_Cattle_Detection_and_Feed_Bunk_Spatial_Analysis|UAV-Based Computer Vision for Cattle Detection and Feed Bunk Spatial Analysis]]

![[assets/2611.08928_figure.png|800]]

- **arXiv**: [2611.08928](https://arxiv.org/abs/2611.08928)
- **PDF**: https://arxiv.org/pdf/2611.08928
- **详细分析**: [[20_Research/Papers/机器人/UAV-Based_Computer_Vision_for_Cattle_Detection_and_Feed_Bunk_Spatial_Analysis|UAV-Based Computer Vision for Cattle Detection and Feed Bunk Spatial Analysis]]
- **作者**: Pedro Oliveira Torrente, Diego Giaretta de Paulo, Lucas Pascotti Valem, Jianglong Yan, Everton Castelão Tetila, Jayme Garcia Arnal Barbedo, Liang Zhao
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人
- **相关性评分**: 0.8（加权：机器人 0.8）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《UAV-Based Computer Vision for Cattle Detection and Feed Bunk Spatial Analysis》归入 机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Beef cattle production is central to Brazilian agribusiness and faces growing demands for efficiency, sustainability, and animal welfare. Precision Livestock Farming (PLF) offers tools to address these challenges, particularly through monitoring feeding-related spatial patterns in confined systems. Feeding management plays a decisive role in animal performance, yet its evaluation still relies largely on subjective, labor-intensive visual inspections that are hard to scale and prone to bias. This work proposes a computer vision framework based on Unmanned Aerial Vehicles (UAVs) to quantify cattle alignment and spatial dispersion at the feed bunk under real-world feedlot conditions. A UAV dataset was collected during flight campaigns at a commercial feedlot in Mato Grosso do Sul, Brazil. Images were manually annotated into cattle head and cattle back classes to support object detection and image-level spatial analysis of cattle distribution. You Only Look Once (YOLO) models, namely YOLOv8 and YOLOv11, were evaluated, with YOLOv8 small used for the downstream spatial analysis. The feed bunk region was segmented using the Segment Anything Model (SAM), and geometric metrics based on detected head positions were developed to characterize alignment, spacing regularity, and clustering. The selected detector achieved 84.30% mAP50 and 35.50% mAP50-95, with an inference time of approximately 2.7 ms per image on an NVIDIA RTX 5060 Ti GPU. The resulting metrics distinguished representative regular and irregular spatial distributions by Root Mean Square Deviation - RMSD (1.06 m and 4.26 m), Coefficient of Variation - CV (42.70% and 96.31%), and clustering (0 and 2 clusters), respectively. These findings indicate that the proposed approach can provide indicators for assessing feed bunk spatial patterns in PLF.

</details>

---

### [[20_Research/Papers/大模型/Measurement-Aware_Multimodal_LLM_for_No-Reference_Low-Dose_CT_Quality_Assessment|Measurement-Aware Multimodal LLM for No-Reference Low-Dose CT Quality Assessment]]

![[assets/2611.08754_figure.png|800]]

- **arXiv**: [2611.08754](https://arxiv.org/abs/2611.08754)
- **PDF**: https://arxiv.org/pdf/2611.08754
- **详细分析**: [[20_Research/Papers/大模型/Measurement-Aware_Multimodal_LLM_for_No-Reference_Low-Dose_CT_Quality_Assessment|Measurement-Aware Multimodal LLM for No-Reference Low-Dose CT Quality Assessment]]
- **作者**: Kerem Basim, Tolga Demiroglu, Mehmet Ozan Unal, Metin Ertas, Isa Yildirim
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Measurement-Aware Multimodal LLM for No-Reference Low-Dose CT Quality Assessment》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AgenticIQA, ClinReadNet, IQA, LDCT-IQA, LMM-IQA, Tool-IQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

No-reference image quality assessment (IQA) of low-dose CT predicts the score that radiologists would assign to a slice without a full-dose reference, as needed to compare dose protocols and denoisers. Trained CT IQA networks agree well with radiologists but output only a score, whereas multimodal large language models (MLLMs) can explain a score but perform poorly on CT when only prompted. We propose a measurement-aware MLLM, built on Qwen3.8-27B, that rates a slice from its image together with six image-domain measurements of noise, sharpness, high-frequency content and streaks, given to the language model as percentiles in text. On the LDCT-IQA 2023 test set, it reaches an Overall score of 2.735, on par with the retrained challenge winner (2.735) and MedSigLIP-FiLM (2.713), and substantially above its base MLLM used as a zero-shot agent. Shuffling the measurements at test time reduces the score by 0.048, mostly through noise, but the same measurements also lead the model to assign higher scores to over-smoothed denoised images.

</details>

---

### [[20_Research/Papers/具身智能/Meituan-Robotics-0_A_Vision-Language-Action_Foundation_Model_for_Desktop_Manipulation|Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation]]

![[assets/2611.08577_figure.png|800]]

- **arXiv**: [2611.08577](https://arxiv.org/abs/2611.08577)
- **PDF**: https://arxiv.org/pdf/2611.08577
- **详细分析**: [[20_Research/Papers/具身智能/Meituan-Robotics-0_A_Vision-Language-Action_Foundation_Model_for_Desktop_Manipulation|Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation]]
- **作者**: Meituan Robotics Team, Caicheng Wang, Chen Zhao, Chengpeng Jin, Duo Xu, Fengjiao Chen, Guanglu Wan, Heqing Yang, Jia Wang, Jiacong Zhou, Jie Hu, Jiyuan Ru...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 4.0（加权：具身智能 2.1，大模型 0.6，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Meituan-Robotics-0: A Vision-Language-Action Foundation Model for Desktop Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgiBot-World, Real-World, StarVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Meituan-Robotics-0 (MR0), a vision-language-action foundation model and embodied-agent system for stationary-base desktop manipulation. MR0 combines 147 million vision-language samples with 15,060 hours of curated robot trajectories spanning 12 embodiments. A three-stage training recipe aligns multimodal representations with robot behavior through discrete action-token pre-training, transfers these priors to continuous cross-embodiment control through flow-matching mid-training, and adapts the policy through real-world post-training. We introduce Rollback, which pairs replaced policy segments with human corrections to provide positive and negative supervision for CFG-DAgger without value learning or advantage labeling. A unified end-effector interface supports heterogeneous embodiments, while asynchronous action-chunk merging maintains smooth execution under variable inference latency. An event-driven agent maintains persistent task events and reassesses plans when progress or feasibility changes, enabling cross-task retrieval and conditional task resumption. MR0 achieves 93.6% success on RoboTwin 2.0 and ranks fifth in the RoboDojo VLA track. Under matched HG-DAgger post-training, MR0 achieves higher average success rate and progress score than $π_{0.5}$ across three real-robot tasks. On Ethernet insertion, CFG-DAgger trained with Rollback data reaches 70% success and a progress score of 0.90. Qualitative agent deployments demonstrate cross-task event retrieval and recovery from temporarily unsatisfied task conditions.

</details>

---

### [[20_Research/Papers/具身智能/Open-HumanWAM_An_Open_Recipe_for_Scaling_Human_and_Robot_Experience_for_Embodied_Foundation_Models|Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models]]

![[assets/2611.06817_figure.png|800]]

- **arXiv**: [2611.06817](https://arxiv.org/abs/2611.06817)
- **PDF**: https://arxiv.org/pdf/2611.06817
- **详细分析**: [[20_Research/Papers/具身智能/Open-HumanWAM_An_Open_Recipe_for_Scaling_Human_and_Robot_Experience_for_Embodied_Foundation_Models|Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models]]
- **作者**: Juncheng Ma, Jiaxin Li, Jiankai Tu, Bo Liang, Guodong Lv, Yufan Deng, Junzhe Tang, Liangzhu Yang, Chen Bian, Shukai Gong, Yintianrun Zhang, Zicong Cao...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Open-HumanWAM: An Open Recipe for Scaling Human and Robot Experience for Embodied Foundation Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HumanNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric human video offers a scalable source of manipulation priors for robot learning, yet translating raw data scale into generalizable robot policies demands rigorous data curation and training recipes. We introduce Open-HumanWAM, the first fully open recipe for scaling egocentric pretraining to 50,000 hours, anchored by Open-HumanWAM-50K---a curated egocentric video corpus densely annotated with hand motion and natural language. Leveraging this corpus, we systematically investigate pure human pretraining via closed-loop simulation evaluations and uncover an empirical log-linear scaling law linking pretraining data hours to downstream robot success rates. Grounded in these findings, we develop HumanWAM-Vanilla, a world--action model pretrained exclusively on 50k hours of egocentric human video. Upon robot post-training, HumanWAM-Vanilla reaches 92.08% success on RoboTwin 2.0 Clean2Clean and 68.88% on Clean2Random, alongside a 14.17% mean success rate and a 19.00 mean progress score on RoboDojo. To push the capability frontier further, we explore joint human--robot pretraining with HumanWAM-Goal, a visual-goal-conditioned world--action model. Hybrid data scaling unlocks broad zero-shot generalization across both simulation and physical benchmarks, propelling post-trained RoboTwin 2.0 performance to new state-of-the-art levels: 92.70% on Clean2Clean and a substantial leap to 84.60% on Clean2Random. On physical robots, HumanWAM-Goal further exhibits emergent embodied in-context learning, dynamically adapting its manipulation behavior to unseen visual goals without parameter updates. To support reproducible scaling research in embodied AI, we open-source the Open-HumanWAM-50K corpus, data curation and pretraining pipelines, alongside the pretrained and post-trained HumanWAM checkpoints, inference code, and simulation evaluation suites.

</details>

---
