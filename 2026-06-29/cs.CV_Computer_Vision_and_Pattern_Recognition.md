# cs.CV | Computer Vision and Pattern Recognition | 2026-06-29

#arxiv #ComputerScience

**论文数**: 12

### [[20_Research/Papers/大模型/RSICCLLM_A_Multimodal_Large_Language_Model_for_Remote_Sensing_Image_Change_Captioning|RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning]]

![[assets/2606.28266_figure.png|800]]

- **arXiv**: [2606.28266](https://arxiv.org/abs/2606.28266)
- **PDF**: https://arxiv.org/pdf/2606.28266
- **详细分析**: [[20_Research/Papers/大模型/RSICCLLM_A_Multimodal_Large_Language_Model_for_Remote_Sensing_Image_Change_Captioning|RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning]]
- **作者**: Yelin Wang, Zijia Song, Shuo Ye, Chuanguang Yang, Miaoyu Wang, Yong Xu, Zhulin An, Yongjun Xu, Zitong Yu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.9（加权：大模型 0.9）
- **关联关键词**: LLM, Multimodal, ComputerVision

#### 研究背景与动机

《RSICCLLM: A Multimodal Large Language Model for Remote Sensing Image Change Captioning》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Remote Sensing Image Change Captioning (RSICC) aims to describe changes between bi-temporal remote sensing images and holds significant research and application value. However, most existing methods rely on conventional deep learning architectures, and the limited model capacity constrains performance. Although large-model post-training techniques have achieved great success in general domains, their direct transfer to RSICC remains challenging due to data scarcity and the need for fine-grained change understanding. To address this, we propose RSICCLLM, the first post-training framework for large vision-language models in RSICC. Specifically, we design a data generation paradigm, release the instruction dataset RSICI, and establish a task-specific RSICC benchmark. We further introduce Difference-aware Supervised Fine-tuning to explicitly extract change representations and guide the model in perceiving and understanding temporal differences. In addition, we propose Dual-Negative Preference Optimization (DNPO), which employs two complementary negative-sample construction strategies to construct the preference dataset RSICP and further refine model performance. Extensive experiments validate the superior capability of RSICCLLM, which achieves outstanding results with only 7B parameters, surpassing models of substantially larger scales. The code and dataset will be made publicly available at https://github.com/keaill/RSICCLLM.

</details>

---

### [[20_Research/Papers/大模型/EchoSonar-R_A_Multi-View_Reasoning-Enabled_Model_for_Disease_Classification_and_Report_Generation_in_Echocardiography|EchoSonar-R: A Multi-View Reasoning-Enabled Model for Disease Classification and Report Generation in Echocardiography]]

![[assets/2606.28164_figure.png|800]]

- **arXiv**: [2606.28164](https://arxiv.org/abs/2606.28164)
- **PDF**: https://arxiv.org/pdf/2606.28164
- **详细分析**: [[20_Research/Papers/大模型/EchoSonar-R_A_Multi-View_Reasoning-Enabled_Model_for_Disease_Classification_and_Report_Generation_in_Echocardiography|EchoSonar-R: A Multi-View Reasoning-Enabled Model for Disease Classification and Report Generation in Echocardiography]]
- **作者**: Darya Taratynova, Ahmed Aly, Numan Saeed, Mohammad Yaqub
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 大模型, 世界模型
- **相关性评分**: 0.72（加权：大模型 0.2，强化学习 0.36，世界模型 0.16）
- **关联关键词**: LLM, Multimodal, RL

#### 研究背景与动机

《EchoSonar-R: A Multi-View Reasoning-Enabled Model for Disease Classification and Report Generation in Echocardiography》归入 强化学习、大模型、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MIMICEchoQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Echocardiography is the most widely used non-invasive cardiac imaging modality, providing essential information for cardiovascular diagnosis. Interpreting an echocardiogram requires synthesizing complementary evidence across multiple heart views to identify abnormalities and produce structured clinical reports. While recent efforts focus on improving classification performance, most models lack explicit diagnostic reasoning and spatially grounded anatomical evidence, limiting clinician trust. We present EchoSonar-R, a multi-view reasoning-enabled vision-language model that jointly performs multi-label disease classification and report generation from echocardiography studies. EchoSonar-R combines a spatiotemporal video encoder with a structure-aware cardiac detector that provides spatially grounded anatomical cues to improve interpretability and clinician trust during cross-view reasoning. EchoSonar-R is trained in two stages: supervised fine-tuning (SFT) on reasoning-annotated targets, followed by Group Relative Policy Optimization (GRPO) with task-specific rewards that jointly align classification and report generation within a unified reinforcement-learning framework. Across a private multi-view dataset and two public benchmarks, EchoSonar-R improves macro balanced accuracy by 17.1% on the private set and 6.1% on MIMICEchoQA over the strongest baseline, achieves a GREEN clinical faithfulness score of 0.800, and produces interpretable reasoning traces grounded in multi-view visual evidence.

</details>

---

### [[20_Research/Papers/具身智能/Translation_as_a_Bridging_Action_Transferring_Manipulation_Skills_from_Humans_to_Robots|Translation as a Bridging Action: Transferring Manipulation Skills from Humans to Robots]]

![[assets/2606.28133_figure.png|800]]

- **arXiv**: [2606.28133](https://arxiv.org/abs/2606.28133)
- **PDF**: https://arxiv.org/pdf/2606.28133
- **详细分析**: [[20_Research/Papers/具身智能/Translation_as_a_Bridging_Action_Transferring_Manipulation_Skills_from_Humans_to_Robots|Translation as a Bridging Action: Transferring Manipulation Skills from Humans to Robots]]
- **作者**: Sijin Chen, Kaixuan Jiang, Haixin Shi, Yanhui Wang, Weiheng Zhong, Haosheng Li, Bo Jiang, Yuxiao Liu, Xihui Liu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Translation as a Bridging Action: Transferring Manipulation Skills from Humans to Robots》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study whether we can learn novel manipulation skills from human actions to a bi-manual robot with parallel grippers. Human action data is cheap, abundant, and diverse, making it one of the most promising resources for scaling up robot learning. Yet transferring skills from humans to robots remains hard: most prior work treats humans as just another bi-manual 6DoF embodiment, where hand-pose estimates are noisy and the contact patterns of human fingers differ fundamentally from those of a parallel gripper. We argue that learning rotation-inclusive action signals from human data is therefore sub-optimal, and instead propose a bridging action representation: the relative wrist translation within the initial head-camera frame, an action space shared by humans and robots. To handle the potential absence of certain action components in different embodiments, we build a $π_0$-like vision-language-action model with interleaved action tokens and attention masking. On a suite of novel bi-manual manipulation tasks, our bridging action transfers human manipulation knowledge to robots far more effectively than noisy 6DoF human actions and scales with the amount of human data.

</details>

---

### [[20_Research/Papers/具身智能/ReScene_Structured_Indoor_Scene_Reconstruction_from_Multi-View_Captures|ReScene: Structured Indoor Scene Reconstruction from Multi-View Captures]]

![[assets/2606.28060_figure.png|800]]

- **arXiv**: [2606.28060](https://arxiv.org/abs/2606.28060)
- **PDF**: https://arxiv.org/pdf/2606.28060
- **详细分析**: [[20_Research/Papers/具身智能/ReScene_Structured_Indoor_Scene_Reconstruction_from_Multi-View_Captures|ReScene: Structured Indoor Scene Reconstruction from Multi-View Captures]]
- **作者**: Haoran Xu, Lechao Zhang, Daoguo Dong, Yan Gao, Xin Tan
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型
- **相关性评分**: 0.5（加权：具身智能 0.3，大模型 0.2）
- **关联关键词**: LLM, Multimodal, EmbodiedAI

#### 研究背景与动机

《ReScene: Structured Indoor Scene Reconstruction from Multi-View Captures》归入 具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ScanNet, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Constructing simulation-ready 3D scenes from multi-view captures is a key bottleneck for Embodied Artificial Intelligence, as downstream tasks require object-level structure, explicit inter-object relations, and physical plausibility. Existing approaches either rely on specialized capture hardware, suffer from single-view bias in object reconstruction, or yield layouts that are geometrically reasonable but physically inconsistent. We identify that the problem is not single-object reconstruction but cross-view relation fusion and physically plausible scene assembly. To address this challenge, we present ReScene, a framework that threads multi-view geometry throughout the pipeline as a unifying prior. Our method consists of two main components: HierView prioritizes reconstruction views based on semantic consistency and 3D coverage completeness, replacing the largest-mask heuristic that conflates image occupancy with object coverage; and Relation-Aware Assembly fuses multi-frame relation predictions from a vision-language model with geometric and room-shell priors into a confidence-weighted scene graph, enabling physically consistent scene assembly. ReScene sets a new state of the art across geometry, rendering, and perceptual quality on a set of ScanNet scenes, achieving a 17% reduction in Chamfer Distance and 26% in LPIPS over the strongest prior baseline, while running up to 10x faster than prior multi-view methods. Based on the reconstructed scenes, we also generate an embodied visual question answering dataset, on which fine-tuned Qwen-VL approaches the performance of strong closed-source models on several spatial reasoning tasks.

</details>

---

### [[20_Research/Papers/具身智能/AirGroundBench_Probing_Spatial_Intelligence_in_Multimodal_Large_Models_under_Heterogeneous_Multi-View_Embodied_Collaboration|AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration]]

![[assets/2606.28049_figure.jpg|800]]

- **arXiv**: [2606.28049](https://arxiv.org/abs/2606.28049)
- **PDF**: https://arxiv.org/pdf/2606.28049
- **详细分析**: [[20_Research/Papers/具身智能/AirGroundBench_Probing_Spatial_Intelligence_in_Multimodal_Large_Models_under_Heterogeneous_Multi-View_Embodied_Collaboration|AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration]]
- **作者**: Haotian Li, Yida Wang, Leyuan Wang, Jinshan Lai, Keyang Wang, Zonghao Guo, Qiang Ma, Liuyu Xiang, Jianwei Hu, Zhaofeng He
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，大模型 0.5，机器人 0.2）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《AirGroundBench: Probing Spatial Intelligence in Multimodal Large Models under Heterogeneous Multi-View Embodied Collaboration》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AirCopBench, AirGroundBench, MM-UAVBench, MMSI-Bench, STI-Bench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, multimodal large language models (MLLMs) have shown strong potential for embodied intelligence, yet their ability to maintain geometrically consistent spatial understanding across heterogeneous views remains under-evaluated. Existing benchmarks largely focus on single-agent, single-view perception, leaving a gap in the systematic assessment of collaborative air-ground settings, where multi-scale observations are complementary but introduce scale mismatch, asymmetric occlusion, and reference-frame inconsistencies. We present AirGroundBench, a diagnostic benchmark for evaluating multi-view spatial intelligence in heterogeneous UAV-UGV collaboration. AirGroundBench is built from 11 high-fidelity simulated environments with 1,021 synchronized air-ground observation pairs, yielding approximately 62,000 dual-view, four-option single-choice visual question answering instances and 115 closed-loop vision-language navigation episodes. It covers 10 task types organized into four progressively demanding capability dimensions: spatial perception, cross-view alignment, spatial transformation and reasoning, and embodied decision-making. To support geometry-grounded evaluation and analysis, we provide structured spatial annotations, including cross-view object identities and metric 2D and 3D bounding boxes. Evaluations of 13 representative MLLMs under UAV-only, UGV-only, and dual-view input settings reveal consistent bottlenecks: models perform relatively well on spatial perception but struggle with cross-view alignment and transformation-intensive reasoning, and these deficits propagate to sequential decision-making in vision-language navigation. Although dual-view inputs provide measurable gains over single-view variants, a persistent gap from human performance remains, highlighting geometric consistency as a key limitation of current embodied MLLMs.

</details>

---

### [[20_Research/Papers/强化学习/NormGuard_Reward-Preserving_Norm_Constraints_in_Flow-Matching_Reinforcement_Learning|NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement Learning]]

![[assets/2606.27771_figure.png|800]]

- **arXiv**: [2606.27771](https://arxiv.org/abs/2606.27771)
- **PDF**: https://arxiv.org/pdf/2606.27771
- **详细分析**: [[20_Research/Papers/强化学习/NormGuard_Reward-Preserving_Norm_Constraints_in_Flow-Matching_Reinforcement_Learning|NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement Learning]]
- **作者**: Tianlin Pan, Lianyu Pang, Cheng Da, Huan Yang, Changqian Yu, Kun Gai, Wenhan Luo
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型, 大模型
- **相关性评分**: 1.22（加权：大模型 0.1，强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, ComputerVision

#### 研究背景与动机

《NormGuard: Reward-Preserving Norm Constraints in Flow-Matching Reinforcement Learning》归入 强化学习、世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GenEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning (RL) post-training improves the reward alignment of flow-based generators, but often degrades perceptual quality in ways that are not captured by the reward proxy. We identify a simple structural signature of this drift: across three post-training methods (NFT, AWM, DPO), RL fine-tuning inflates the per-step velocity norm $\|v_θ\|$ by $5\%$ to $15\%$ relative to the reference. A form of norm inflation has been studied in classifier-free guidance (CFG), where rescaling the velocity back to a reference norm at inference time can mitigate the resulting artifacts. However, this inference-time correction does not transfer cleanly to RL: rescaling $v_θ$ to match $\|v_{\text{ref}}\|$ at inference time neither improves reward nor fixes the quality degradation, because the inflation is co-adapted into the model weights. Furthermore, an adjoint sensitivity analysis shows that velocity magnitude rescaling carries no coherent first-order reward signal at the batch level, indicating that suppressing norm inflation is unlikely to remove a consistently reward-carrying component. Since inference-time renormalization fails while norm suppression carries no reward cost, training-time intervention is the appropriate strategy. Together, these findings motivate \methodname, a hinge penalty that activates only when $\|v_θ\|$ exceeds $\|v_{\text{ref}}\|$ and composes additively with any velocity-local base loss. Across two base models, three post-training methods, and two reward proxies, \methodname consistently improves MLLM-judged image quality and forensic realism while preserving reward, with gains that amplify under few-step inference and are not explained by early stopping.

</details>

---

### [[20_Research/Papers/机器人/DIM-WAM_World-Action_Modeling_with_Diverse_Historical_Event_Memory|DIM-WAM: World-Action Modeling with Diverse Historical Event Memory]]

![[assets/2606.27677_figure.png|800]]

- **arXiv**: [2606.27677](https://arxiv.org/abs/2606.27677)
- **PDF**: https://arxiv.org/pdf/2606.27677
- **详细分析**: [[20_Research/Papers/机器人/DIM-WAM_World-Action_Modeling_with_Diverse_Historical_Event_Memory|DIM-WAM: World-Action Modeling with Diverse Historical Event Memory]]
- **作者**: Kai Wang, Zhaopeng Gu, Yixiang Chen, Yuan Xu, Qisen Ma, Peng Su, Zhaowen Li, Yan Huang, Liang Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《DIM-WAM: World-Action Modeling with Diverse Historical Event Memory》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BridgeVLA, EventVLA, GigaWorld, MemoryBench, MemoryVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World-action models have shown promising robot-manipulation performance by jointly predicting future visual states and actions. However, existing methods mainly rely on short-term history and short-horizon future prediction, which is insufficient for long-horizon tasks whose correct execution depends on earlier observations and task progress. Such temporally dependent tasks require effective use of complementary temporal information, including recent local context, cross-stage historical events, immediate future dynamics, and global task progress. To address long-term forgetting and poor awareness of the global task state, we introduce DiM-WAM, a memory-augmented world-action model that integrates multi-scale historical context, local future dynamics, and global task progress. The memory extracts compact visual event information from real observations, updates multiple memory banks through independent similarity-based merging, and then reads the bank-identity- and time-embedded long-term context to condition video and action denoising. A progress-supervision objective further encourages memory tokens to encode not only completed historical events but also the current task stage and its implications for the remaining task. On RMBench, DiM-WAM raises average success from 28.4% with LingBot-VA to 69.8%, exceeding the explicit-memory Mem-0 baseline at 42.0%. On four real-world Franka tasks, it improves average stage success from 70.7% to 91.5% and full-task success from 52.5% to 80.0%. Project page: https://wangkai-casia.github.io/dim-wam/{\texttt{https://wangkai-casia.github.io/dim-wam/}}.

</details>

---

### [[20_Research/Papers/大模型/Temporal-Emerged_Prompting_for_Segment_Anything_in_Multiframe_Infrared_Small_Target_Detection|Temporal-Emerged Prompting for Segment Anything in Multiframe Infrared Small Target Detection]]

![[assets/2606.27655_figure.png|800]]

- **arXiv**: [2606.27655](https://arxiv.org/abs/2606.27655)
- **PDF**: https://arxiv.org/pdf/2606.27655
- **详细分析**: [[20_Research/Papers/大模型/Temporal-Emerged_Prompting_for_Segment_Anything_in_Multiframe_Infrared_Small_Target_Detection|Temporal-Emerged Prompting for Segment Anything in Multiframe Infrared Small Target Detection]]
- **作者**: Yinghui Xing, Donghao Chu, Shizhou Zhang, Di Xu
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 0.5（加权：大模型 0.5）
- **关联关键词**: LLM, ComputerVision

#### 研究背景与动机

《Temporal-Emerged Prompting for Segment Anything in Multiframe Infrared Small Target Detection》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurately localizing and segmenting small targets in low signal-to-noise ratio (SNR) infrared sequences remains a challenging task. Since targets are often indistinguishable from the background in individual frames, existing methods, even when equipped with advanced foundation model and powerful inter-frame association mechanisms, still fail to detect them. Motivated by the observation that targets tend to emerge gradually from the background over time and become distinguishable, we propose Temporal-Emerged Prompting for Segment Anything Model (TEP-SAM), a principled framework designed to explicitly exploit such temporal-emerged cues to modulate and prompt SAM. TEP-SAM operates by jointly modeling global motion patterns and local motion deviations to locate potential targets. It further enhances target region features by leveraging motion discrepancy, thereby generating temporal-emerged cues for SAM and enabling non-interactive segmentation. By bridging large-scale semantic pretraining with task-specific temporal modeling, TEP-SAM effectively adapts SAM to the challenging multiframe infrared small target detection task. Extensive experiments demonstrate the effectiveness of our approach, particularly under severely low-SNR conditions and in complex dynamic background.

</details>

---

### [[20_Research/Papers/世界模型/CascadeOcc_Rethinking_3D_Occupancy_World_Models_with_Cascaded_VQ_Representations|CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations]]

![[assets/2606.27644_figure.png|800]]

- **arXiv**: [2606.27644](https://arxiv.org/abs/2606.27644)
- **PDF**: https://arxiv.org/pdf/2606.27644
- **详细分析**: [[20_Research/Papers/世界模型/CascadeOcc_Rethinking_3D_Occupancy_World_Models_with_Cascaded_VQ_Representations|CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations]]
- **作者**: Kyumin Hwang, Wonhyeok Choi, Jaeyeul Kim, Jihun Park, Daehee Park, Sunghoon Im
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.2（加权：世界模型 1，机器人 0.2）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《CascadeOcc: Rethinking 3D Occupancy World Models with Cascaded VQ Representations》归入 世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CasMVSNet, FSF-Net, OccWorld, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This letter proposes CascadeOcc, a novel occupancy world model that prioritizes intrinsic structural hierarchy over extrinsic auxiliary modalities for autonomous driving. Occupancy world models -- forecasting the future driving environment and planning the driving trajectory -- effectively bridge perception and planning, but current approaches often heavily rely on external modalities or large language models, failing to fully exploit the inherent structural potential of occupancy representations themselves. To enhance representational capacity for complex 3D scenes, we integrate a cascaded Vector Quantized (VQ) mechanism into an autoregressive framework. Following a coarse-to-fine principle, CascadeOcc progressively refines fine-grained details from global structures through a multi-scale architecture. Additionally, we incorporate a TimeMixer to capture multi-scale temporal dependencies, establishing a dual-hierarchy mechanism in both space and time. Experimental results on 4D occupancy forecasting and motion planning benchmarks demonstrate that CascadeOcc achieves superior performance among vision-centric approaches, validating that optimizing inherent representations is a powerful alternative to relying on external foundation models.

</details>

---

### [[20_Research/Papers/强化学习/Qwen-Image-2.0-RL_Technical_Report|Qwen-Image-2.0-RL Technical Report]]

![[assets/2606.27608_first_page.png|800]]

- **arXiv**: [2606.27608](https://arxiv.org/abs/2606.27608)
- **PDF**: https://arxiv.org/pdf/2606.27608
- **详细分析**: [[20_Research/Papers/强化学习/Qwen-Image-2.0-RL_Technical_Report|Qwen-Image-2.0-RL Technical Report]]
- **作者**: Yixian Xu, Kaiyuan Gao, Yuxiang Chen, Yilei Chen, Zecheng Tang, Zihao Liu, Zikai Zhou, Deqing Li, Hao Meng, Kuan Cao, Jiahao Li, Jie Zhang...
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 0.52（加权：强化学习 0.36，世界模型 0.16）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Qwen-Image-2.0-RL Technical Report》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Qwen-Image-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present Qwen-Image-2.0-RL, a post-training pipeline that applies reinforcement learning from human feedback (RLHF) and on-policy distillation (OPD) to improve both the visual quality and instruction-following capability of the Qwen-Image-2.0 diffusion model. To provide reliable reward signals, we construct task-specific composite reward models by fine-tuning vision-language models with a pointwise scoring paradigm and chain-of-thought reasoning. For text-to-image generation, the reward models cover alignment, aesthetics, and portrait fidelity dimensions. For image editing tasks, the reward system addresses instruction-following accuracy and face identity preservation. Building on this reward system, we develop a scalable GRPO-based RL training framework, incorporating a hybrid classifier-free guidance (CFG) strategy to preserve pre-trained knowledge, prompt curation via intra-group reward range filtering, and per-category reward weight calibration. To merge the task-specialized RL policies for T2I and editing, we propose on-policy distillation as the final training stage, which consolidates multiple teachers into a single student model through trajectory-level velocity matching. Extensive evaluation shows that Qwen-Image-2.0-RL achieves 57.84 overall score on Qwen-Image-Bench (+2.61 over the base model), Elo ratings of 1193 in text-to-image arena (+78) and 1349 in image edit arena (+93), demonstrating consistent gains in aesthetic quality, prompt adherence, and editing accuracy.

</details>

---

### [[20_Research/Papers/大模型/Perceptual_3D_Simulation_With_Physical_World_Modeling|Perceptual 3D Simulation With Physical World Modeling]]

![[assets/2606.27575_figure.jpg|800]]

- **arXiv**: [2606.27575](https://arxiv.org/abs/2606.27575)
- **PDF**: https://arxiv.org/pdf/2606.27575
- **详细分析**: [[20_Research/Papers/大模型/Perceptual_3D_Simulation_With_Physical_World_Modeling|Perceptual 3D Simulation With Physical World Modeling]]
- **作者**: Wanhee Lee, Klemen Kotar, Rahul Mysore Venkatesh, Jared Watrous, Daniel L. K. Yamins
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 大模型
- **相关性评分**: 0.5（加权：大模型 0.1，世界模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《Perceptual 3D Simulation With Physical World Modeling》归入 世界模型、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：P3Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting how a scene will evolve after a desired 3D transformation from images is a central goal in vision, graphics, and robotics. Yet unlike ideal simulators with full access to 3D geometry and dynamics, real world systems must rely on perceptual inputs and local actions that are inherently partial and incomplete. In this work, we present P3Sim, a physical world modeling system that simulates future scene states under both partial observations and incomplete 3D transformation signals. P3Sim is composed of three interacting components: a learned physical world model, a geometric conditioning module, and a persistent scene memory. The world model interprets perception as probabilistic inference over multimodal scene variables, providing predictions of the distributions of any scene variable conditioned on any combination of others. The geometric conditioning module provides a partial 3D transform signal for conditioning the world model at inference time. The persistent scene memory integrates predictions over time, enabling online updates and consistency under uncertainty. By combining learned inference with explicit geometric structure, P3Sim balances data-driven flexibility with built-in inductive bias. This design yields a flexible perceptual simulator that generalizes across diverse 3D transformation tasks, such as novel view synthesis, object manipulation, and dynamic scene prediction, advancing toward general purpose 3D scene understanding and transformation.

</details>

---

### [[20_Research/Papers/大模型/Fine-tuning_a_multimodal_large_language_model_for_clinician-grade_autism_behavioral_scoring_from_short_home_videos|Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos]]

![[assets/2606.27484_figure.png|800]]

- **arXiv**: [2606.27484](https://arxiv.org/abs/2606.27484)
- **PDF**: https://arxiv.org/pdf/2606.27484
- **详细分析**: [[20_Research/Papers/大模型/Fine-tuning_a_multimodal_large_language_model_for_clinician-grade_autism_behavioral_scoring_from_short_home_videos|Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos]]
- **作者**: Mohammadmahdi Honarmand, Parnian Azizian, Aaron Kline, Kae Nurge, Zerin Nasrin Tumpa, Saimourya Surabhi, Kaitlyn Dunlap, Yang Qian, Ali Kargarandehkordi, Sameer Neupane, Peter Washington, Dennis P. Wall
- **cs 子类**: cs.CV
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.1（加权：大模型 1.1）
- **关联关键词**: LLM, Multimodal

#### 研究背景与动机

《Fine-tuning a multimodal large language model for clinician-grade autism behavioral scoring from short home videos》归入 大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autism spectrum disorder (ASD) affects 1 in 31 US children, yet median age at diagnosis exceeds four years. Artificial intelligence pipelines that provide quantified diagnosis using easy to access observational data (e.g., home videos) could help with earlier diagnosis, and timely delivery of early treatments. We fine-tuned Gemini 2.5 Pro on 400 clinician-rated home videos with low-rank adaptation, training only on 30 behavioral features previously validated to produce reliable predictions when passed to various ML models. On 99 held-out children (49 ASD, 50 neurotypical), inter-rater reliability with clinicians (per-feature weighted Cohen's kappa) improved by 40% (p&lt;0.001), with 27 of 28 evaluable features improving. As an emergent zero-shot capability, direct ASD diagnosis F1 improved by 53% (p&lt;0.001), matching or exceeding clinician outcomes. Classifier-assisted pipelines using fine-tuned LLM-derived behavioral features matched clinician-scored inputs across all tested pathways and achieved 77% accuracy (95% CI: 68-85%) and an AUC of 86% (95% CI: 78-92%). Fine-tuned multimodal LLMs can serve as scalable behavioral feature extractors for use in autism assessment and diagnosis.

</details>

---
