# cs.RO | Robotics | 2026-05-28

#arxiv #ComputerScience

**论文数**: 25

### [[20_Research/Papers/强化学习/Imitation_Learning_for_Robot_Assistance_in_Open_Surgery_A_Multi-Policy_Evaluation_on_Suture_Following|Imitation Learning for Robot Assistance in Open Surgery: A Multi-Policy Evaluation on Suture Following]]

![[assets/2605.28736_figure.png|800]]

- **arXiv**: [2605.28736](https://arxiv.org/abs/2605.28736)
- **PDF**: https://arxiv.org/pdf/2605.28736
- **详细分析**: [[20_Research/Papers/强化学习/Imitation_Learning_for_Robot_Assistance_in_Open_Surgery_A_Multi-Policy_Evaluation_on_Suture_Following|Imitation Learning for Robot Assistance in Open Surgery: A Multi-Policy Evaluation on Suture Following]]
- **作者**: Xucheng Wang, Zhizhou Yang, Xiaoman Zhang, Sung Eun Kim, Romain Hardy, Pranav Rajpurkar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Imitation Learning for Robot Assistance in Open Surgery: A Multi-Policy Evaluation on Suture Following》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ResNet, RoboNurse-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study presents the first evaluation of general-purpose imitation learning for surgeon-robot collaborative assistance in open surgery, targeting suture following: the grab-pull-release motion an assistant performs at every stitch. We collect 160 teleoperated demonstrations (32,374 frames) on an open-source robot arm, benchmark four architecturally diverse imitation learning policies (ACT, Diffusion Policy, SmolVLA, $\pi_0$) across 28 trained models evaluated in 32 configurations along three clinically motivated dimensions: dataset size, camera viewpoint, and background variation. Our results demonstrate that under ideal conditions, the four policies achieve $50$-$75\%$ task success, with depth error as the dominant failure mode across all architectures. Among all policies, $\pi_0$ achieves the strongest results with a pretrained vision-language backbone, demonstrating superior data efficiency, greater robustness to background variation, and smoother trajectories compatible with surgical workflow. When deployed in a surgeon-robot suturing trial, $\pi_0$ yields a $92\%$ stitch completion rate. These findings establish collaborative robotic assistance in open surgery as a feasible target for imitation learning and highlight depth perception and end-effector design as key priorities for clinical translation.

</details>

---

### [[20_Research/Papers/机器人/Integrated_Exploration-Aware_UAV_Route_Optimization_and_Path_Planning|Integrated Exploration-Aware UAV Route Optimization and Path Planning]]

![[assets/2605.28654_figure.png|800]]

- **arXiv**: [2605.28654](https://arxiv.org/abs/2605.28654)
- **PDF**: https://arxiv.org/pdf/2605.28654
- **详细分析**: [[20_Research/Papers/机器人/Integrated_Exploration-Aware_UAV_Route_Optimization_and_Path_Planning|Integrated Exploration-Aware UAV Route Optimization and Path Planning]]
- **作者**: Jimin Choi, Grant Stagg, Cameron K. Peterson, Max Z. Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent

#### 研究背景与动机

《Integrated Exploration-Aware UAV Route Optimization and Path Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Uncrewed aerial vehicles (UAVs) are increasingly used for exploration-driven monitoring in hazardous environments such as disaster zones, contaminated sites, wildfire areas, and damaged infrastructure, where limited flight endurance must be allocated between visiting reported locations and gathering new information. In these settings, prior information regarding hazards is often incomplete, spatially imprecise, and subject to change during execution. For example, initial reports may identify a region where a hazard is likely to exist, but the actual hazard may be displaced, partially observed, or entirely unreported. We present an integrated exploration-aware UAV route optimization and path planning framework for hazard monitoring under uncertain and evolving prior information. The environment is represented as a spatial risk map, where each location has an associated belief of hazardous conditions. Reported hazards are modeled as uncertain regions of interest (ROIs) rather than confirmed target locations, requiring the UAV to inspect reported areas while also using its limited flight endurance to explore informative regions. The proposed method solves a vehicle routing problem over reported ROIs, augments the route with auxiliary pseudo-nodes to improve spatial coverage, allocates the remaining flight distance budget across route segments, and optimizes dynamically feasible B-spline trajectories for local exploration. During execution, UAV measurements update a grid-based belief map, and the remaining trajectory is replanned when new information and the remaining budget justify adaptation. Across 48 scenario configurations, online replanning improves average KL reduction by 15.9% over the offline optimized planner and 48.6% over straight-line traversal.

</details>

---

### [[20_Research/Papers/具身智能/PrimitiveVLA_Learning_Reusable_Motion_Primitives_for_Efficient_and_Generalizable_Robotic_Manipulation|PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation]]

![[assets/2605.28634_figure.png|800]]

- **arXiv**: [2605.28634](https://arxiv.org/abs/2605.28634)
- **PDF**: https://arxiv.org/pdf/2605.28634
- **详细分析**: [[20_Research/Papers/具身智能/PrimitiveVLA_Learning_Reusable_Motion_Primitives_for_Efficient_and_Generalizable_Robotic_Manipulation|PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation]]
- **作者**: Yutai Li, Shaohui Peng, Jiaming Guo, Di Huang, Zihao Zhang, Yuxuan Guo, Yunkai Gao, Siming Lan, Ling Li, Xing Hu, Yunji Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《PrimitiveVLA: Learning Reusable Motion Primitives for Efficient and Generalizable Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoT-VLA, OpenVLA, PrimitiveVLA, Real-World, SPiRL, VideoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models offer a promising paradigm for generalist robotic policies, yet their adaptation is hindered by data inefficiency and poor generalization. We argue that these bottlenecks stem from the prevailing Direct Instruction-to-Control Mapping, which forces models to memorize monolithic trajectories rather than reusable motion patterns, i.e., primitives. We propose PrimitiveVLA, a framework that shifts this paradigm toward a Primitive-Centric Disassemble &amp; Assemble paradigm. Supported by a shared Multimodal Canonical Representation (MCR), PrimitiveVLA unifies two phases: (1) Fine-tuning-phase Disassembly, which uses an automated pipeline to disassemble demonstrations into reusable primitives; and (2) Inference-phase Assembly, which employs a VLM-based planner and an LLM-generated switch module for robust closed-loop execution. By disassembling tasks into reusable primitives, PrimitiveVLA enables VLA models to learn invariant motion patterns instead of task-specific trajectories. Extensive experiments show that our framework improves data efficiency and achieves superior zero-shot generalization across unseen and long-horizon tasks.

</details>

---

### [[20_Research/Papers/具身智能/What_Frozen_VLAs_Already_Know_About_Success_A_Probing_Study_of_Value-Like_Structure_in_Foundation_Robot_Policies|What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies]]

![[assets/2605.28527_figure.png|800]]

- **arXiv**: [2605.28527](https://arxiv.org/abs/2605.28527)
- **PDF**: https://arxiv.org/pdf/2605.28527
- **详细分析**: [[20_Research/Papers/具身智能/What_Frozen_VLAs_Already_Know_About_Success_A_Probing_Study_of_Value-Like_Structure_in_Foundation_Robot_Policies|What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies]]
- **作者**: Jiachen Zhang, Junnan Nie, Junyi Lao, Wei Cheng, Chenghao Liu, Jiaxin Jiang, Songfang Huang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《What Frozen VLAs Already Know About Success: A Probing Study of Value-Like Structure in Foundation Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision--language--action (VLA) policies are trained to imitate actions; their loss never asks them to estimate reward, progress, or future success. Their frozen representations nevertheless carry such information, and it can be read out and used to guide action choice without retraining the policy. From mixed successful and failed manipulation trajectories on LIBERO-Goal, we recover Monte-Carlo outcome targets using lightweight linear probes on frozen features. The targets are consistently predictable from OpenVLA, Pi0.5, DINOv2, and CLIP features, and substantially less so from baselines built on progress, time-to-go, task identity, or proprioception. To rule out task and temporal shortcuts, we evaluate the probes under same-task, same-timestep matched comparisons: Pi0.5 probes still reach roughly 92% pairwise ordering accuracy, while label-shuffled controls stay at chance. Used as a test-time selector over sampled Pi0.5 action prefixes, the same probe turns this offline finding into behavior: on push-plate, success rises from 26.7% under greedy decoding to 44.3%, with a second positive case on wine-rack. The gains are not universal and require additional inference compute, but the underlying finding is clean: frozen VLAs already encode information about success that their imitation objective never explicitly demands.

</details>

---

### [[20_Research/Papers/具身智能/Mag-VLA_Vision-Language-Action_Model_for_Bimanual_Magnetically_Actuated_Microrobot_Manipulation|Mag-VLA: Vision-Language-Action Model for Bimanual Magnetically Actuated Microrobot Manipulation]]

![[assets/2605.28486_figure.jpg|800]]

- **arXiv**: [2605.28486](https://arxiv.org/abs/2605.28486)
- **PDF**: https://arxiv.org/pdf/2605.28486
- **详细分析**: [[20_Research/Papers/具身智能/Mag-VLA_Vision-Language-Action_Model_for_Bimanual_Magnetically_Actuated_Microrobot_Manipulation|Mag-VLA: Vision-Language-Action Model for Bimanual Magnetically Actuated Microrobot Manipulation]]
- **作者**: Yongchen Wang, Kangyi Lu, Lan Wei, Dandan Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Mag-VLA: Vision-Language-Action Model for Bimanual Magnetically Actuated Microrobot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Mag-VLA, OpenVLA, TMR-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Magnetically actuated microrobots have been used as wireless, non-contact manipulation tools at microscales, making them promising for minimally invasive applications. However, their control remains challenging due to indirect actuation, limited sensing, and nonlinear magnetic interactions. In this work, we propose Mag-VLA, a vision-language-action (VLA) model for dexterous magnetic microrobot manipulation using two robotic arms with mounted magnets for dynamic magnetic-field construction. Bimanual coordination enables capabilities such as microrobot reorientation that are difficult or infeasible with a single arm, but it also introduces coupled control challenges, as the policy must generate coordinated trajectories for both actuators within a shared workspace. Our framework adapts a Qwen2.5-VL-7B backbone using Low-Rank Adaptation (LoRA) to process visual observations and language instructions for action prediction. To capture task progression, we introduce a motion-aware phase classifier and a phase-conditioned Action Chunking Transformer (ACT) decoder for temporally coherent multi-step control. We further construct a teleoperated magnetic microrobot manipulation dataset covering three task configurations. Ablation studies show that the ACT-based decoder substantially outperforms alternative generative action heads. In real-robot experiments, Mag-VLA achieves a 90% approach success rate across all tasks and transport success rates of 80%, 70%, and 50% as task difficulty increases. These results demonstrate that hierarchical VLA modeling provides a promising framework for magnetic microrobot manipulation.

</details>

---

### [[20_Research/Papers/机器人/EIT-Pneumatic_Hybrid_Robotic_Skin_for_Practical_and_Accurate_Force_Map_Reconstruction|EIT-Pneumatic Hybrid Robotic Skin for Practical and Accurate Force Map Reconstruction]]

![[assets/2605.28468_figure.png|800]]

- **arXiv**: [2605.28468](https://arxiv.org/abs/2605.28468)
- **PDF**: https://arxiv.org/pdf/2605.28468
- **详细分析**: [[20_Research/Papers/机器人/EIT-Pneumatic_Hybrid_Robotic_Skin_for_Practical_and_Accurate_Force_Map_Reconstruction|EIT-Pneumatic Hybrid Robotic Skin for Practical and Accurate Force Map Reconstruction]]
- **作者**: Junhwi Cho, Sunggyu Bae, Junghyeon Ma, Hyosang Lee, Jung Kim, Kyungseo Park
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《EIT-Pneumatic Hybrid Robotic Skin for Practical and Accurate Force Map Reconstruction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a hybrid robotic skin that combines electrical impedance tomography (EIT) with pneumatic tactile sensing to improve force reconstruction capability. The developed robotic skin is fabricated entirely by 3D printing and spray coating, making it affordable and easy to build. A Tikhonov-regularized inverse reconstruction, paired with per-pad pneumatic calibration, enables accurate large-area tactile sensing with a simple measurement scheme. For validation, we conducted load-cell indentation experiments; the results showed consistent force reconstruction across locations within a pad. Compared with an EIT-only baseline, sensitivity non-uniformity was also reduced, with the coefficient of variation decreasing from 0.31 to 0.14, indicating that the proposed approach addresses a longstanding limitation of EIT. We further demonstrated chest-mounted integration on a humanoid robot and found that the pneumatic signals remained reliable across diverse contact scenarios, including multiple simultaneous contacts on the same sensing pad. These results indicate a practical path toward accurate, scalable whole-body tactile sensing in real robotic systems.

</details>

---

### [[20_Research/Papers/机器人/A_Digital_Twin_Framework_for_Virtual_Visuo-Haptic_Teleoperation_of_Complex-Shaped_Optical_Microrobots|A Digital Twin Framework for Virtual Visuo-Haptic Teleoperation of Complex-Shaped Optical Microrobots]]

![[assets/2605.28448_figure.png|800]]

- **arXiv**: [2605.28448](https://arxiv.org/abs/2605.28448)
- **PDF**: https://arxiv.org/pdf/2605.28448
- **详细分析**: [[20_Research/Papers/机器人/A_Digital_Twin_Framework_for_Virtual_Visuo-Haptic_Teleoperation_of_Complex-Shaped_Optical_Microrobots|A Digital Twin Framework for Virtual Visuo-Haptic Teleoperation of Complex-Shaped Optical Microrobots]]
- **作者**: Zongcai Tan, Lan Wei, Dandan Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《A Digital Twin Framework for Virtual Visuo-Haptic Teleoperation of Complex-Shaped Optical Microrobots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Optical tweezers (OT) provide piconewton-scale manipulation for delicate biomedical tasks, where visuo-haptic feedback can improve operator awareness by conveying interaction-force cues and trap-stability information. However, visuo-haptic teleoperation frameworks for complex-shaped optical microrobots remain underdeveloped, particularly in multi-trap manipulation scenarios. This paper presents a digital twin framework for virtual visuo-haptic teleoperation of complex-shaped OT-driven microrobots. The framework integrates a digital twin environment, image-based pose and depth estimation, microrobot motion simulation, and model-based haptic rendering within a Robot Operating System (ROS)-connected bimanual teleoperation system. For force modeling, we combine a Multi-Sphere Distributed Manipulation (MSDM) model with optical-force estimation from the Optical Tweezers Toolbox, enabling simulator-driven visuo-haptic feedback. The framework reproduces representative microrobot motion trends and provides haptic force rendering that is numerically consistent with the fitted optical-force model. In simulated cell-delivery tasks, haptic feedback reduced the standard deviations of the contact-force metric and the microrobot-to-trap-center distance metric by 53.2% and 55.2%, respectively, and improved task success from 30% to 80%. These results demonstrate the framework's effectiveness for evaluating visuo-haptic teleoperation strategies for complex-shaped optical microrobots.

</details>

---

### [[20_Research/Papers/机器人/Safety-Critical_Adaptive_Impedance_Control_via_Nonsmooth_Control_Barrier_Functions_under_State_and_Input_Constraints|Safety-Critical Adaptive Impedance Control via Nonsmooth Control Barrier Functions under State and Input Constraints]]

![[assets/2605.28367_figure.jpg|800]]

- **arXiv**: [2605.28367](https://arxiv.org/abs/2605.28367)
- **PDF**: https://arxiv.org/pdf/2605.28367
- **详细分析**: [[20_Research/Papers/机器人/Safety-Critical_Adaptive_Impedance_Control_via_Nonsmooth_Control_Barrier_Functions_under_State_and_Input_Constraints|Safety-Critical Adaptive Impedance Control via Nonsmooth Control Barrier Functions under State and Input Constraints]]
- **作者**: Faisal Lawan, Xiaoran Han, Joaquin Carrasco, Barry Lennox, Xiaoxiao Cheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Safety-Critical Adaptive Impedance Control via Nonsmooth Control Barrier Functions under State and Input Constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe physical interaction is critical for deploying robotic manipulators in human-robot interaction and contact-rich tasks, where uncertainty, external forces, and actuator limitations can compromise both performance and safety. We propose an online adaptive impedance control framework that enforces joint-state safety while achieving compliant interaction under uncertain dynamics. The approach combines a quadratic-program-based safety filter with a novel composed position-velocity non-smooth control barrier function (NCBF), enabling joint position and velocity constraints to be enforced through a unified relative-degree-one barrier. Unknown dynamics are compensated online using an interval type-2 fuzzy logic system, while actuator torque limits are handled through soft constraints with exact penalty recovery of feasible solutions. A disturbance-observer-enhanced safety mechanism improves robustness against modelling errors and external interaction forces. Using composite Lyapunov analysis, we prove forward invariance of the safe set and the uniform ultimately boundedness of the impedance-tracking error. Simulations on a 7-DOF manipulator with severe parametric uncertainty and external interaction wrenches demonstrate safe constraint satisfaction and robust impedance tracking.

</details>

---

### [[20_Research/Papers/机器人/Accelerating_Robot_Path_Planning_via_Connectivity-Preserving_Region_Proposal_Network|Accelerating Robot Path Planning via Connectivity-Preserving Region Proposal Network]]

![[assets/2605.28362_figure.png|800]]

- **arXiv**: [2605.28362](https://arxiv.org/abs/2605.28362)
- **PDF**: https://arxiv.org/pdf/2605.28362
- **详细分析**: [[20_Research/Papers/机器人/Accelerating_Robot_Path_Planning_via_Connectivity-Preserving_Region_Proposal_Network|Accelerating Robot Path Planning via Connectivity-Preserving Region Proposal Network]]
- **作者**: Zhanzheng Ma, Cancan Zhao, Shuai Zhang, Bo Ouyang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，机器人 1.9）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Accelerating Robot Path Planning via Connectivity-Preserving Region Proposal Network》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MPNet, Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robot path planning methods are often constrained by vast search spaces, resulting in latency in samplingbased algorithms. Learning-based approaches frequently suffer from local region fragmentation and global topological inconsistency. To tackle the problem, we present the Connectivity- Preserving Region Proposal Network (CP-RPN), a segmentationguided model designed to predict compact and topologically connected candidate regions, significantly compressing the search space. Specifically, we design a segmentation model that leverages a Deformable Attention Transformer (DAT) to capture long-range dependencies for global connectivity, with a Deconvolutional decoder to preserve fine-grained spatial details. To guarantee the connectivity of the predicted mask, we design a composite loss function that combines Cross-Entropy loss for pixelwise supervision, a Connectivity-Aware loss to enhance local coherence, and a Topological Continuity loss based on persistent homology to enforce global connectivity. Building on these highconnectivity corridor-like regions, the Voronoi diagram is used to plan the path, backed by a local A* fallback mechanism to ensure robustness. Experimental results demonstrate that CPRPN reduces the candidate region size by over 60.13% compared to the MPT baseline and achieves deterministic low-latency planning (avg. 0.11s) with a 99.60% success rate, outperforming traditional sampling-based algorithms in stability.

</details>

---

### [[20_Research/Papers/机器人/Magnet-Based_Soft_Robotic_Skin_Using_a_3D-Printed_Multi-Lattice_Structure_and_CNN-Based_Tactile_Super-Resolution|Magnet-Based Soft Robotic Skin Using a 3D-Printed Multi-Lattice Structure and CNN-Based Tactile Super-Resolution]]

![[assets/2605.28352_first_page.png|800]]

- **arXiv**: [2605.28352](https://arxiv.org/abs/2605.28352)
- **PDF**: https://arxiv.org/pdf/2605.28352
- **详细分析**: [[20_Research/Papers/机器人/Magnet-Based_Soft_Robotic_Skin_Using_a_3D-Printed_Multi-Lattice_Structure_and_CNN-Based_Tactile_Super-Resolution|Magnet-Based Soft Robotic Skin Using a 3D-Printed Multi-Lattice Structure and CNN-Based Tactile Super-Resolution]]
- **作者**: Yunseong Bang, Joowon Park, Suan Sim, Youngjun Ryu, Sukho Park, Kyungseo Park
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Magnet-Based Soft Robotic Skin Using a 3D-Printed Multi-Lattice Structure and CNN-Based Tactile Super-Resolution》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a magnet-based robotic skin that integrates a multilayer soft lattice with distributed Hall-effect sensor arrays and a tactile super-resolution model. External contact forces are converted to magnetic field changes by embedded permanent magnets, and the lattice spreads these changes across the sensing domain. This gives each sensor a large, overlapping receptive field and enables a large sensing area with minimal blind spots. Lattice parameters are tunable, enabling joint adjustment of mechanical compliance and transduction characteristics. An implicit modeling workflow and selective laser sintering (SLS) 3D printing support rapid fabrication of conformal, high-complexity structures. A convolutional neural network trained on experimental measurements estimates contact location and normal force in real time. Experiments validate localization accuracy and indicate scalability to larger surfaces, suggesting applicability to whole-body robotic skin and safe human-robot interaction.

</details>

---

### [[20_Research/Papers/具身智能/Natural_Locomotion_Principle_and_Method|Natural Locomotion: Principle and Method]]

![[assets/2605.28254_figure.png|800]]

- **arXiv**: [2605.28254](https://arxiv.org/abs/2605.28254)
- **PDF**: https://arxiv.org/pdf/2605.28254
- **详细分析**: [[20_Research/Papers/具身智能/Natural_Locomotion_Principle_and_Method|Natural Locomotion: Principle and Method]]
- **作者**: Mirado Mortel, Luc Jaulin, Lionel Lapierre, Simon Rohou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Natural Locomotion: Principle and Method》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic locomotion can become efficient when mechanisms exploit passive dynamics, compliance, and resonance rather than track prescribed trajectories. This paper formulates natural locomotion as an exchange principle for systems whose motion is mediated by environmental constraints or interactions. A motion is natural when an internal oscillator returns periodically, the body pose drifts, and the mean Propulsion--Oscillator Exchange power (POE power) vanishes over one cycle. The selected family is a Natural Locomotion Manifold (NLM). We develop the conservative realization of this principle for continuous ideal environmental constraints: the constraints do no external work, total mechanical energy is conserved, and zero mean POE power is an internal exchange with the environment-mediated propulsive channel, not external energy input. The method is a closed/open construction. The propulsive channel is first closed to reveal an effective internal oscillator, organized by scalar action-angle structure in one effective degree of freedom or by nonlinear modal sectors in several degrees of freedom. The channel is then reopened, pose is reconstructed, and accepted cycles must preserve internal recurrence and zero mean POE power. We demonstrate the principle on two ideal nonholonomic no-slip systems: a Chaplygin-sleigh / pendulum-driven car and a three-body extension. In the scalar case, POE closure is equivalent to the missing internal return condition, giving a theorem-backed computation of the NLM family. In the multi-degree case, POE closure remains necessary but must be completed by modal identity, internal return, dynamics consistency, same fixed passive architecture, and nonzero displacement. Natural locomotion becomes a design question: which passive architectures support no, one, or several certified NLM families?

</details>

---

### [[20_Research/Papers/具身智能/Natural_Functional_Gradients_for_Smooth_Trajectory_Optimization|Natural Functional Gradients for Smooth Trajectory Optimization]]

![[assets/2605.28202_figure.png|800]]

- **arXiv**: [2605.28202](https://arxiv.org/abs/2605.28202)
- **PDF**: https://arxiv.org/pdf/2605.28202
- **详细分析**: [[20_Research/Papers/具身智能/Natural_Functional_Gradients_for_Smooth_Trajectory_Optimization|Natural Functional Gradients for Smooth Trajectory Optimization]]
- **作者**: Kisang Park, Chanwoo Kim, Kyungjae Lee, Sungjoon Choi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Natural Functional Gradients for Smooth Trajectory Optimization》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating collision-free and smooth motions remains a central challenge in robotic manipulation, particularly in cluttered environments and narrow passages where feasible regions are highly constrained and fragmented. We propose a trajectory optimization framework that performs geometry-aware updates directly in function space using natural functional gradients. The method optimizes a Gaussian-smoothed surrogate objective that regularizes the optimization landscape through smooth trajectory perturbations while preserving trajectory-level structure. Because the updates are defined intrinsically in function space, trajectory regularity can be controlled independently of a particular time discretization. We derive a practical Monte-Carlo estimator of the natural functional gradient that requires only black-box trajectory evaluations, making the method applicable when analytic gradients are unavailable or unreliable due to collision checking and contact-rich simulation. Experiments on constrained robotic manipulation tasks demonstrate that the proposed method improves trajectory feasibility and produces smoother motions than representative planning and trajectory optimization baselines in environments with narrow geometric clearances. Additional results, videos, and implementation details are available at the project page: this https URL

</details>

---

### [[20_Research/Papers/机器人/Provably_Guaranteed_Polytopic_Uncertainty_Quantification_for_SLAM|Provably Guaranteed Polytopic Uncertainty Quantification for SLAM]]

![[assets/2605.28172_figure.png|800]]

- **arXiv**: [2605.28172](https://arxiv.org/abs/2605.28172)
- **PDF**: https://arxiv.org/pdf/2605.28172
- **详细分析**: [[20_Research/Papers/机器人/Provably_Guaranteed_Polytopic_Uncertainty_Quantification_for_SLAM|Provably Guaranteed Polytopic Uncertainty Quantification for SLAM]]
- **作者**: Guangyang Zeng, Yulong Gao, Yuan Shen, Lingpeng Chen, Haoying Li, Guodong Shi, Junfeng Wu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Provably Guaranteed Polytopic Uncertainty Quantification for SLAM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In safety-critical robotics applications, guaranteed and practical uncertainty quantification (UQ) in perception is vital. Many existing works either offer no formal containment guarantee, rely on restrictive modeling assumptions, or focus only on pose estimation rather than a complete SLAM pipeline. This paper presents provably guaranteed UQ algorithms for 3D-3D landmark-based SLAM. The algorithms consist of three basic UQ modules: forward UQ for mapping, backward UQ for pose tracking, and pose compound. Each module produces a certified uncertainty set; when the input uncertainty bounds are deterministic, the output sets inherit deterministic guarantees, i.e., they provably contain the true poses and landmarks. Specifically, we use polytopes to represent uncertainty sets, enabling tractable computations and a unified treatment of pose uncertainty. To enhance algorithms' practical usability, we incorporate conformal prediction to calibrate measurement uncertainty from data with prescribed probability. Simulations and experiments demonstrate that the proposed algorithms provide both strong theoretical guarantees and practical usability. The code is open-sourced at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/STR_Robot_Design_of_an_Autonomous_Mobile_Robot_from_Simulation_to_Reality|STR Robot: Design of an Autonomous Mobile Robot from Simulation to Reality]]

![[assets/2605.28110_figure.png|800]]

- **arXiv**: [2605.28110](https://arxiv.org/abs/2605.28110)
- **PDF**: https://arxiv.org/pdf/2605.28110
- **详细分析**: [[20_Research/Papers/具身智能/STR_Robot_Design_of_an_Autonomous_Mobile_Robot_from_Simulation_to_Reality|STR Robot: Design of an Autonomous Mobile Robot from Simulation to Reality]]
- **作者**: Vinh Nguyen, Gia-Uy Le, Tien-Dat Nguyen, Tri-Tin Nguyen, Vinh-Hao Nguyen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《STR Robot: Design of an Autonomous Mobile Robot from Simulation to Reality》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid development of simulation tools, the development and validation of autonomous robotic systems have become more efficient before real-world deployment. This paper presents a simulation-to-real implementation of an autonomous mobile robot based on an existing mechanical platform. Instead of focusing on mechanical design, our work concentrates on the development of the onboard control, self-localization, and autonomous navigation system. The proposed robot is equipped with onboard sensing and computation to estimate its pose and navigate autonomously in the environment. The overall framework is first developed and tested in simulation, and then deployed on the real robot for experimental evaluation. The results demonstrate the feasibility of the proposed approach and show that simulation provides an effective foundation for developing reliable autonomous mobile robot systems. The source code will be released at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/ICAN-Deploy_Identity-Stable_Canary_Deployment_for_Safety-Critical_Embodied_Agents|ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents]]

![[assets/2605.28097_figure.png|800]]

- **arXiv**: [2605.28097](https://arxiv.org/abs/2605.28097)
- **PDF**: https://arxiv.org/pdf/2605.28097
- **详细分析**: [[20_Research/Papers/具身智能/ICAN-Deploy_Identity-Stable_Canary_Deployment_for_Safety-Critical_Embodied_Agents|ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents]]
- **作者**: Xue Qin, Simin Luan, John See, Zeyd Boukhers, Cong Yang, Zhijun Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，大模型 0.6，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《ICAN-Deploy: Identity-Stable Canary Deployment for Safety-Critical Embodied Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Name-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Canary deployment routes a fraction of traffic to a new software version, monitors metrics, and rolls back on regression. Mainstream controllers (Argo Rollouts, Spinnaker, Flagger) change the deployed system's cryptographic identity during the canary window. The drift is harmless for stateless microservices but breaks the claim that "the agent you certified is still the agent you have" for safety-critical embodied agents, forcing re-certification per canary. We present ICAN-Deploy (Identity-stable CANary Deployment), a middleware construction whose state machine holds the identity hash invariant across the canary window by separating capability names (frozen, hashed) from capability versions (mutable runtime state). We implement ICAN-Deploy inside a runtime governance layer for LLM-driven robots and verify invariance by closed-form proof, AST lint, and TLA+ model-checking, then corroborate over N=100 real canary cycles on a Franka Panda arm in MuJoCo (zero drift; entry latency 95% BCa CI [1.52, 2.01] ms). A feature-flagged strawman that folds versions into the manifest falsifies on the same workload. A system certified once at identity-creation time can then ship arbitrary capability evolution under that same certification, within the version-and-name envelope.

</details>

---

### [[20_Research/Papers/机器人/SAFEVPR_Patch-Based_Conformal_Verification_for_Safe_Cross-Condition_Sequence_Visual_Place_Recognition|SAFEVPR: Patch-Based Conformal Verification for Safe Cross-Condition Sequence Visual Place Recognition]]

![[assets/2605.28048_figure.png|800]]

- **arXiv**: [2605.28048](https://arxiv.org/abs/2605.28048)
- **PDF**: https://arxiv.org/pdf/2605.28048
- **详细分析**: [[20_Research/Papers/机器人/SAFEVPR_Patch-Based_Conformal_Verification_for_Safe_Cross-Condition_Sequence_Visual_Place_Recognition|SAFEVPR: Patch-Based Conformal Verification for Safe Cross-Condition Sequence Visual Place Recognition]]
- **作者**: Ha Sier, Jiaqiang Zhang, Zhuo Zou, Xianjia Yu, Tomi Westerlund
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《SAFEVPR: Patch-Based Conformal Verification for Safe Cross-Condition Sequence Visual Place Recognition》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Sequence-based visual place recognition (VPR) for SLAM and robot relocalization must decide whether the retrieved top-1 candidate is safe to accept. Conformal prediction is a natural framework for this accept/reject decision, but its finite-sample guarantees rely on exchangeability between calibration and deployment (test) data, which is violated under cross-condition deployment. We introduce SAFEVPR, a non-trainable verification-and-calibration pipeline for safe cross-condition sequence VPR. SAFEVPR replaces the standard backbone cosine similarity with a mutual-nearest-neighbour (MNN) patch-matching score computed from frozen DINOv2 ViT features, and replaces flat Learn-Then-Test calibration with Mondrian conformal LTT, fitting separate Bonferroni-corrected thresholds across score bins. Under exchangeability, these thresholds would provide finite-sample false-discovery-rate (FDR) control; under condition shift, we evaluate empirical validity per deployment. Across 23 cross-condition setups from Oxford RobotCar, NCLT, and St Lucia datasets, using three frozen VPR backbones, SAFEVPR is empirically valid on 23/23 setups at target FDR alpha = 0.10, achieving mean accepted FDR 0.014 and mean true-positive rate (TPR) 0.75. The results show that raw discrimination alone is not sufficient for conformal validity: AnyLoc-VLAD and Super-Point+LightGlue reach comparable area under the receiver operating characteristic curve (AUROC) but fail more setups under the same calibration. On textureless repetitive scenery, SAFEVPR safely abstains rather than accepting unreliable matches. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/SANTS_A_State-Adaptive_Scheduler_for_World_Action_Models|SANTS: A State-Adaptive Scheduler for World Action Models]]

![[assets/2605.27947_figure.png|800]]

- **arXiv**: [2605.27947](https://arxiv.org/abs/2605.27947)
- **PDF**: https://arxiv.org/pdf/2605.27947
- **详细分析**: [[20_Research/Papers/具身智能/SANTS_A_State-Adaptive_Scheduler_for_World_Action_Models|SANTS: A State-Adaptive Scheduler for World Action Models]]
- **作者**: Yirui Sun, Guangyu Zhuge, Keliang Liu, Jie Gu, Xinyu Bing, Zhongxue Gan, Chunxu Tian
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《SANTS: A State-Adaptive Scheduler for World Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) improve robot manipulation by using video-based future representations to condition action generation. In pixel-space WAMs, however, the best action condition is not necessarily the fully denoised video. Controlled denoising-depth scans show that video refinement can reduce action error up to a state-dependent point, after which the gain may saturate or even reverse when late predictions become less action-relevant or physically unreliable. This suggests that action generation should use a state-dependent point along the video noise trajectory rather than a fixed terminal denoising depth. We introduce State-Adaptive Noise Trajectory Scheduler (SANTS), a lightweight scheduler for video-to-action diffusion policies. At each video decision point, SANTS reads the current video-state representation and noise level, then jointly predicts a cumulative stopping hazard and a relative noise-progression ratio. SANTS is post-trained with a path-level reward computed after the frozen action branch generates the final action chunk, so the scheduler is optimized for downstream action quality rather than intermediate video fidelity, while redundant video-state updates are explicitly penalized. Experiments show that SANTS reaches \(94.4\%\) overall success on RoboTwin 2.0 and \(73.1\%\) average success across seven real-robot tasks, while reducing latency by \(81.7\%\) and \(79.0\%\) relative to full video denoising, respectively. These results indicate that adaptive selection along the video noise trajectory can preserve the control benefits of WAM-style future reasoning while removing much of its redundant inference cost.

</details>

---

### [[20_Research/Papers/具身智能/S-Cheetah_A_Novel_Quadrupedal_Robot_with_a_3-DOF_Active_Spine_Learning_Agile_Locomotion|S-Cheetah: A Novel Quadrupedal Robot with a 3-DOF Active Spine Learning Agile Locomotion]]

![[assets/2605.27909_figure.png|800]]

- **arXiv**: [2605.27909](https://arxiv.org/abs/2605.27909)
- **PDF**: https://arxiv.org/pdf/2605.27909
- **详细分析**: [[20_Research/Papers/具身智能/S-Cheetah_A_Novel_Quadrupedal_Robot_with_a_3-DOF_Active_Spine_Learning_Agile_Locomotion|S-Cheetah: A Novel Quadrupedal Robot with a 3-DOF Active Spine Learning Agile Locomotion]]
- **作者**: Zimu Li, Weibang Bai
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《S-Cheetah: A Novel Quadrupedal Robot with a 3-DOF Active Spine Learning Agile Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RSL-RL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The biological spine of quadrupeds enables sagittal flexion/extension, lateral bending, and axial rotation, playing a crucial role in highly agile and dexterous locomotion. While numerous studies have integrated active spinal joints into quadrupedal robots to enhance agility, most designs simplify control complexity by reducing spinal degrees of freedom (DOF), failing to achieve the spatial tri-axial rotation characteristic of biological spines. Consequently, replicating a multi-DOF biomimetic spine and effectively leveraging it to empower the agile locomotion of quadrupedal robots remains a significant research challenge. In this study, we present S-Cheetah, a quadrupedal robot featuring a 3-DOF bio-inspired serial active spine capable of biomimetic spatial tri-axial rotation. To empower the robot to fully utilize this active spine, we developed a specialized reinforcement learning framework to actively promote the engagement of the introduced spine and maximize the robot's locomotive capabilities by integrating an acceleration curriculum learning strategy with tailored reward functions, such as a gallop gait reward, a spine undulation reward, and a spine steering reward. Experimental results demonstrate that S-Cheetah can achieve a peak speed of 6.9 m/s using the rotary G2 gallop gait and an in-place turning rate of 7.2 rad/s. Besides, the system exhibits an emergent, feline-inspired aerial self-righting capability, allowing it to land stably on four feet from arbitrary orientations during free fall. Finally, through extensive evaluations across diverse locomotion tasks, we prove that the introduction of the proposed 3-DOF spine comprehensively enhances the locomotive agility of quadrupedal robots. Project website: this http URL

</details>

---

### [[20_Research/Papers/具身智能/Tabero_Learning_Gentle_Manipulation_with_Closed-Loop_Force_Feedback_from_Vision,_Touch,_and_Language|Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language]]

![[assets/2605.27886_figure.png|800]]

- **arXiv**: [2605.27886](https://arxiv.org/abs/2605.27886)
- **PDF**: https://arxiv.org/pdf/2605.27886
- **详细分析**: [[20_Research/Papers/具身智能/Tabero_Learning_Gentle_Manipulation_with_Closed-Loop_Force_Feedback_from_Vision,_Touch,_and_Language|Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language]]
- **作者**: Qiwei Wu, Rui Zhang, Xin Xiang, Tao Li, Weihua Zhang, Junjie Lai, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Tabero: Learning Gentle Manipulation with Closed-Loop Force Feedback from Vision, Touch, and Language》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：TA-VLA, Tactile-VLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing is essential for robots to achieve human-like gentle manipulation. However, existing Vision-Language-Action (VLA) models struggle to exploit tactile feedback for gentle manipulation due to scarce aligned vision-tactile-language data and the lack of effective closed-loop force feedback mechanisms. To address these challenges, we introduce Tabero, a benchmark and model suite for gentle, language-conditioned robotic manipulation that demands fine-grained contact force perception. First, the Tabero benchmark addresses the scarcity of tactile data by presenting a data-efficient pipeline that repurposes open-source robot manipulation trajectories to generate diverse vision-tactile-language tasks, and establishes a multidimensional evaluation protocol that measures task success alongside physical interaction quality. Second, we propose Tabero-VTLA, an architecture with a decoupled force-position command interface; the resulting force-position commands are executed by a fixed hybrid controller to enable real-time, force-aware manipulation. Evaluated on Tabero, our model maintains high task success while reducing average grip force by over 70\% under gentle instructions, demonstrating its ability to modulate interaction forces based on multimodal experience. Our code is publicly available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Colosseum_V2_Benchmarking_Generalization_for_Vision_Language_Action_Models|Colosseum V2: Benchmarking Generalization for Vision Language Action Models]]

![[assets/2605.27759_figure.png|800]]

- **arXiv**: [2605.27759](https://arxiv.org/abs/2605.27759)
- **PDF**: https://arxiv.org/pdf/2605.27759
- **详细分析**: [[20_Research/Papers/具身智能/Colosseum_V2_Benchmarking_Generalization_for_Vision_Language_Action_Models|Colosseum V2: Benchmarking Generalization for Vision Language Action Models]]
- **作者**: Jeremy Morgan, Prajwal Vijay, Hyeonho Oh, Jincen Song, Ashvin Arora, Alina Du, Gaurav Sukhatme, Jesse Thomason, Ishika Singh
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Colosseum V2: Benchmarking Generalization for Vision Language Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoppeliaSim, ManipBench, Meta-World, OpenVLA, RLBench, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models demonstrate promising generalization in robotic manipulation, driven by advances in large-scale vision and language pre-training. This progress can be misleading. Despite the zero-shot perception and language capabilities of VLAs, their overall task performance often degrades under distribution shifts, revealing gaps in how these systems translate high-level understanding into robust behavior. To systematically study this gap, we introduce Colosseum V2, a large-scale simulation benchmark for evaluating VLA generalization in robot learning across diverse conditions. The benchmark comprises 28 tasks spanning 13 task categories and two robot morphologies, covering a wide range of manipulation primitives and long-horizon behaviors. Built on the ManiSkill simulator, Colosseum V2 enables fast, GPU-parallelized evaluation and supports both in-domain and out-of-domain testing at scale. We evaluate state-of-the-art methods, including Action Chunking Transformers (ACT) and Pi0.5, and reveal limitations in both base performance and generalization. We demonstrate strong correlations between simulation and real-world metrics that support the ecological validity of the benchmark. By standardizing tasks, metrics, and evaluation protocols within a unified benchmark, Colosseum V2 enables reproducible and fair comparisons, reduced evaluation overhead, and accelerated progress toward general-purpose robot policies.

</details>

---

### [[20_Research/Papers/大模型/Agentic_Language-to-Objective_Synthesis_for_Optofluidic_Assembly|Agentic Language-to-Objective Synthesis for Optofluidic Assembly]]

![[assets/2605.27643_first_page.png|800]]

- **arXiv**: [2605.27643](https://arxiv.org/abs/2605.27643)
- **PDF**: https://arxiv.org/pdf/2605.27643
- **详细分析**: [[20_Research/Papers/大模型/Agentic_Language-to-Objective_Synthesis_for_Optofluidic_Assembly|Agentic Language-to-Objective Synthesis for Optofluidic Assembly]]
- **作者**: Ivan Saraev, Elena Erben, Weida Liao, Fan Nan, Gerhard Neumann, Eric Lauga, Moritz Kreysing
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Agentic Language-to-Objective Synthesis for Optofluidic Assembly》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Light-based advanced manufacturing increasingly requires programmable, closed-loop tools that translate human design intent into executable operations at small length scales. Yet a key bottleneck persists across robotic and manufacturing modalities: turning user intent into machine-readable objectives that are reliably executable. While micro-robotics offers versatile manipulation via optical actuation of fluids, mathematically tractable goal specification remains manual and hard to reuse. Here, we introduce Speak-to-Objective, a modular agentic pipeline that uses a conditioned Large Language Model (LLM) to translate spoken or written commands into fully differentiable objective functions for assembling microparticles in a constraint-aware inverse solver (SLSQP) and on an experimental optofluidic platform. The approach employs a compact loop - perceive -&gt; compose -&gt; propose -&gt; act -&gt; report &amp; learn - that treats the objective as the interface between intent and actuation, separating what to assemble or pattern from how to actuate, while learning from user feedback. The pipeline composes geometry, spacing, and assignment/topology terms to generate robust descriptive objectives that assemble from partial traces and recover after perturbations, as well as explicit objectives for precise placement, all in an actuator-agnostic fashion. Using laser-induced thermoviscous flows as the physical actuation modality, we demonstrate natural-language-programmable, light-based microscale assembly of particle patterns in a microfluidic environment. Beyond its immediate impact on programmable microassembly, and using laser-induced optofluidic actuation as a reduced-complexity experimental platform, our work points toward self-driving, AI-assisted optical manufacturing platforms in which natural language, differentiable objectives, and laser-based actuation are coupled into a reusable digital workflow.

</details>

---

### [[20_Research/Papers/具身智能/Inducing_Calmness_With_Pocket-Sized_Robotics_Reducing_Movement_and_Heart_Rate_in_Children_through_Hand-Held_Tactile_Interactions|Inducing Calmness With Pocket-Sized Robotics: Reducing Movement and Heart Rate in Children through Hand-Held Tactile Interactions]]

![[assets/2605.27533_first_page.png|800]]

- **arXiv**: [2605.27533](https://arxiv.org/abs/2605.27533)
- **PDF**: https://arxiv.org/pdf/2605.27533
- **详细分析**: [[20_Research/Papers/具身智能/Inducing_Calmness_With_Pocket-Sized_Robotics_Reducing_Movement_and_Heart_Rate_in_Children_through_Hand-Held_Tactile_Interactions|Inducing Calmness With Pocket-Sized Robotics: Reducing Movement and Heart Rate in Children through Hand-Held Tactile Interactions]]
- **作者**: Morten Roed Frederiksen, Kasper Støy, Maja Matarić
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.6，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Inducing Calmness With Pocket-Sized Robotics: Reducing Movement and Heart Rate in Children through Hand-Held Tactile Interactions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Periods of heightened arousal or restlessness can interfere with children's ability to focus, self-regulation, and physically calm. Technologies that encourage embodied self-regulation through tactile interaction may provide a simple and accessible means of promoting calmness. This paper investigates how interaction with a pocket-sized tactile device influences physiological and behavioral markers of calmness in typically developing children. Building on prior work examining heart rate modulation, we present new findings on how tactile interaction affects full-body movement and postural stability. We employ a device that engages children through a hand-held rhythmic vibration-matching game, designed to focus attention and encourage stillness. Eighteen children participated in a within-subjects study that involved two conditions: with and without tactile interaction with a hand-held device, while having their heart rate and body movement recorded. Results show that the tactile game interaction reduced physiological arousal (heart rate decreased by 3.56 bpm, p &lt; 0.01) and physical restlessness (overall movement decreased by 38%, p &lt; 0.05), with attention-related body regions showing the greatest change toward stillness (45% reduction in movement). These findings demonstrate that brief tactile game-like engagement with a hand-held device can down-regulate physiological activation, promoting the calm and focused states toward sustained attention and behavior regulation.

</details>

---

### [[20_Research/Papers/具身智能/GE-Sim_2.0_A_Roadmap_Towards_Comprehensive_Closed-loop_Video_World_Simulators_for_Robotic_Manipulation|GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation]]

![[assets/2605.27491_figure.png|800]]

- **arXiv**: [2605.27491](https://arxiv.org/abs/2605.27491)
- **PDF**: https://arxiv.org/pdf/2605.27491
- **详细分析**: [[20_Research/Papers/具身智能/GE-Sim_2.0_A_Roadmap_Towards_Comprehensive_Closed-loop_Video_World_Simulators_for_Robotic_Manipulation|GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation]]
- **作者**: Boxiang Qiu, Liliang Chen, Yue Liao, Nan Wang, Lintao Wang, Jiayi Luo, Wenzhi Zhao, Shengcong Chen, Di Chen, Ye Li, Chen Gao, Shuicheng Yan...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 3.3（加权：具身智能 1.8，世界模型 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《GE-Sim 2.0: A Roadmap Towards Comprehensive Closed-loop Video World Simulators for Robotic Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Cosmos-Predict2-2B-Video2World, Ctrl-World, GE-Sim, GigaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce GE-Sim 2.0 (Genie Envisioner World Simulator 2.0), a closed-loop video world simulator for robotic manipulation. Building on the action-conditioned video generation framework of Genie Envisioner, GE-Sim 2.0 is re-trained on thousands of hours of real-world robot data spanning teleoperation, contact-rich interaction, and on-robot policy deployment, substantially improving action-following fidelity and trajectory coverage. On top of this foundation, three new modules close the loop from video simulation to policy learning: a state expert that decodes proprioceptive state from video latents to support next-chunk prediction by downstream VLA policies; a world judge that scores generated rollouts against task instructions, yielding machine-verifiable success signals and rewards in place of manual inspection; and an acceleration framework that delivers a 25-frame rollout in 2.3 seconds on a single H100, with up to 4* frame skipping at inference for long-horizon evaluation. GE-Sim 2.0 tops the public WorldArena leaderboard at only 2B parameters, outperforming both dedicated robotic world models and closed-source general video generators, and policies trained against its rollouts and rewards translate into measurable real-world gains, establishing GE-Sim 2.0 as a practical platform for scalable evaluation and closed-loop learning of manipulation policies.

</details>

---

### [[20_Research/Papers/具身智能/A_Factory-Floor_Deployment_Case_Study_of_VLA_Pipelines_for_Industrial_Packaging_Task_Workflow,_Failures,_and_Lessons|A Factory-Floor Deployment Case Study of VLA Pipelines for Industrial Packaging Task: Workflow, Failures, and Lessons]]

![[assets/2605.27461_figure.png|800]]

- **arXiv**: [2605.27461](https://arxiv.org/abs/2605.27461)
- **PDF**: https://arxiv.org/pdf/2605.27461
- **详细分析**: [[20_Research/Papers/具身智能/A_Factory-Floor_Deployment_Case_Study_of_VLA_Pipelines_for_Industrial_Packaging_Task_Workflow,_Failures,_and_Lessons|A Factory-Floor Deployment Case Study of VLA Pipelines for Industrial Packaging Task: Workflow, Failures, and Lessons]]
- **作者**: Brian Zhu, Philipp Schmitt, Philine Meister, Lukas Gensler, Momen Khalil, Emmanuele Poggi, Johannes Hechtl, Carsten Braunroth, Kai Wurm, Gokul Narayanan, Eugen Solowjow, Georg von Wichert...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《A Factory-Floor Deployment Case Study of VLA Pipelines for Industrial Packaging Task: Workflow, Failures, and Lessons》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies have shown promising manipulation capabilities, yet their practical impact is often limited by the reliability demands of real-world deployment. We present a deployment study of an industrial packaging task at Siemens Factory (GWE, Erlangen, Germany), where a robot must pick a transparent accessory bag from a cluttered pile, insert it into the remaining cavity of a cardboard package, and ensure that the bag and its contents remain below the closing plane. Our goal is to understand the practical effort required to adapt a pretrained Pi0.5 policy to a single factory-floor task through iterative fine-tuning and deployment-driven refinement. The pipeline consists of repeated loops of data collection, curation, fine-tuning, evaluation, and targeted recovery data collection. We have accumulated 2535 episodes (10 hours) from the on-site factory settings. In this paper, we contribute an empirical account of a factory-floor VLA deployment, highlighting recurring failure modes and lessons that inform how to improve the deployment workflow.

</details>

---

### [[20_Research/Papers/强化学习/Differentiable_Model_Predictive_Safety_for_Heterogeneous_Mobility_at_Urban_Intersections|Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections]]

![[assets/2605.27418_first_page.png|800]]

- **arXiv**: [2605.27418](https://arxiv.org/abs/2605.27418)
- **PDF**: https://arxiv.org/pdf/2605.27418
- **详细分析**: [[20_Research/Papers/强化学习/Differentiable_Model_Predictive_Safety_for_Heterogeneous_Mobility_at_Urban_Intersections|Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections]]
- **作者**: Wenzhe Song, Hao Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能, 大模型, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，强化学习 0.2，世界模型 0.4，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Differentiable Model Predictive Safety for Heterogeneous Mobility at Urban Intersections》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The imminent integration of autonomous vehicles and mobile robots in urban settings presents a critical safety challenge for future intelligent transportation systems. This paper addresses the complex problem of coordinating heterogeneous agents with disparate dynamics at unregulated intersections. We introduce a novel framework, differentiable model predictive safety (DMPS), which embeds the foresight of model-predictive control into a data-driven, end-to-end reinforcement learning architecture. DMPS agents learn a latent dynamics model to predict future trajectories contingent on their actions. A learned, differentiable safety critic then evaluates the risk of these trajectories. Crucially, by leveraging backpropagation through the entire unrolled predictive model, agents can efficiently compute the gradient of future safety with respect to their current action, enabling a minimal and precise online safety correction. Integrated into a multi-agent training scheme, DMPS virtually eliminates collisions to less than 5.6% in high-density, mixed vehicle-robot traffic simulations, demonstrating state-of-the-art safety without compromising energy and traffic efficiency.

</details>

---
