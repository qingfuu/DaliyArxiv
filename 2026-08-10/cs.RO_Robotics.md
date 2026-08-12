# cs.RO | Robotics | 2026-08-10

#arxiv #ComputerScience

**论文数**: 13

### [[20_Research/Papers/具身智能/Identifying_the_Key_Biomechanical_Features_of_Movement_Adaptation_during_Exoskeleton-Assisted_Locomotion|Identifying the Key Biomechanical Features of Movement Adaptation during Exoskeleton-Assisted Locomotion]]

![[assets/2608.07140_figure.png|800]]

- **arXiv**: [2608.07140](https://arxiv.org/abs/2608.07140)
- **PDF**: https://arxiv.org/pdf/2608.07140
- **详细分析**: [[20_Research/Papers/具身智能/Identifying_the_Key_Biomechanical_Features_of_Movement_Adaptation_during_Exoskeleton-Assisted_Locomotion|Identifying the Key Biomechanical Features of Movement Adaptation during Exoskeleton-Assisted Locomotion]]
- **作者**: Peter Seungjune Lee, Katja Mombaur
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Identifying the Key Biomechanical Features of Movement Adaptation during Exoskeleton-Assisted Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The understanding of natural human adaptation during exoskeleton-assisted locomotion - particularly individual differences in adaptation behaviors and temporal progression - remains limited. In this work, we investigate temporal evolution of biomechanical variables to uncover participant-specific adaptation strategies across different exoskeleton-assisted locomotion scenarios. Nine healthy participants performed treadmill walking under three conditions: without an exoskeleton, with exoskeleton active ankle assistance, and with exoskeleton zero-torque. Lower limb kinematics, inter-joint coordination, and metabolic cost of transport (MCoT) were analyzed at both the group and individual levels. Results indicate that adaptation is gradual and highly individualized, with substantial variability in convergence timing and movement patterns across participants. Kinematic adaptation occurred asynchronously across lower limb, with larger fluctuations during the swing phase. Metabolic responses were heterogeneous and often non-convergent, highlighting the limitations of steady-state assumptions commonly adopted in the literature. These findings emphasize the importance of individual-level, temporal evolution analyses for understanding adaptation dynamics in exoskeleton use.

</details>

---

### [[20_Research/Papers/机器人/Detection_and_Ranging_of_Transient_Extrinsic_Contacts_Based_on_6D_Dynamic_Tactile_Sensing|Detection and Ranging of Transient Extrinsic Contacts Based on 6D Dynamic Tactile Sensing]]

![[assets/2608.07075_figure.png|800]]

- **arXiv**: [2608.07075](https://arxiv.org/abs/2608.07075)
- **PDF**: https://arxiv.org/pdf/2608.07075
- **详细分析**: [[20_Research/Papers/机器人/Detection_and_Ranging_of_Transient_Extrinsic_Contacts_Based_on_6D_Dynamic_Tactile_Sensing|Detection and Ranging of Transient Extrinsic Contacts Based on 6D Dynamic Tactile Sensing]]
- **作者**: Haowen Zheng, Yinghao Wu, Fuyuan Liu, Yichen Li, Yitian Shao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Detection and Ranging of Transient Extrinsic Contacts Based on 6D Dynamic Tactile Sensing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Delicate manipulation often involves transient and subtle collisions between a grasped object and the environment. While the human hand localizes these contacts effortlessly thanks to superior tactile sensitivity, robotic systems often lack the requisite resolution to acquire the information necessary for motion planning, resulting in clumsy manipulation or even task failure. Here, we propose transient extrinsic contact detection and ranging (TECDAR), a simple yet fast and efficient method for detecting and ranging extrinsic contact of grasped objects. Our design of gripper tips employs dynamic tactile sensing leveraging a single 2.5$\times$3 mm 6D inertial measurement unit. The sensor captures sub-millisecond tip deformations at a 7 kHz sampling rate, but operating on a data stream of only 84 KB/s. High bandwidth and compact data size enable the system to rapidly detect and localize contact between grasped objects and their surroundings. Specifically, fusing tactile data with robot pose via an extended Kalman filter enables fast and precise localization of extrinsic contact, reaching millimeter-level accuracy within 180 ms. Experimental results demonstrate that the system achieves an average localization accuracy of approximately 7\,mm in both line-contact and point-contact localization tasks. Furthermore, this near-instantaneous localization enables the robot to rectify its trajectory on a millisecond scale, facilitating precise tool manipulation and enhanced perception of complex environments purely through tactile exploration and mapping. We envision such techniques advancing the future of robotics across domains requiring delicate manipulation, including precision assembly, surgical assistance, and autonomous exploration in touch-dominant environments. Project page: this http URL

</details>

---

### [[20_Research/Papers/机器人/Real-time_Whole-Body_Motion_Planning_for_Mobile_Manipulators_Carrying_Arbitrarily_Shaped_Payloads_via_Kinematically-Coupled_SVSDF|Real-time Whole-Body Motion Planning for Mobile Manipulators Carrying Arbitrarily Shaped Payloads via Kinematically-Coupled SVSDF]]

![[assets/2608.07005_figure.png|800]]

- **arXiv**: [2608.07005](https://arxiv.org/abs/2608.07005)
- **PDF**: https://arxiv.org/pdf/2608.07005
- **详细分析**: [[20_Research/Papers/机器人/Real-time_Whole-Body_Motion_Planning_for_Mobile_Manipulators_Carrying_Arbitrarily_Shaped_Payloads_via_Kinematically-Coupled_SVSDF|Real-time Whole-Body Motion Planning for Mobile Manipulators Carrying Arbitrarily Shaped Payloads via Kinematically-Coupled SVSDF]]
- **作者**: Yisheng Li, Longji Yin, Tingrui Zhang, Ruize Xue, Haoda Zhu, Nan Chen, Siqi Liang, Yuxi Liu, Fu Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Real-time Whole-Body Motion Planning for Mobile Manipulators Carrying Arbitrarily Shaped Payloads via Kinematically-Coupled SVSDF》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile manipulators are increasingly tasked with transporting large, non-convex payloads through cluttered environments, yet existing planners either oversimplify the payload geometry or fail to handle the kinematic coupling between manipulator links, leading to lost feasible space or stalled optimization. This letter presents a real-time whole-body motion planning framework for mobile manipulators carrying arbitrarily shaped payloads. The front-end employs a chain-decomposed kernel-based collision check that preserves the true geometry of the robot and payload, with compact storage and fast bit-level queries. A mid-end preprocessing stage converts the front-end path into a continuous trajectory enforcing smoothness and feasibility, and executes it directly when collision-free to bypass the costly back-end. When refinement is required, the back-end performs trajectory optimization built on a Kinematically-Coupled SVSDF (KC-SVSDF), which propagates collision-avoidance gradients along the kinematic chain to produce coherent whole-body escape directions. Ablation studies, comparative benchmarks against state-of-the-art baselines, and real-world experiments on a differential-drive mobile manipulator demonstrate that the proposed framework reliably transports large, non-convex payloads through tight passages and cluttered environments.

</details>

---

### [[20_Research/Papers/机器人/Benchmarking_and_Reasoning_Distillation_of_Large_Language_Models_for_Feedback_Controller_Design_in_Complex_Dynamical_Systems|Benchmarking and Reasoning Distillation of Large Language Models for Feedback Controller Design in Complex Dynamical Systems]]

![[assets/2608.07004_figure.png|800]]

- **arXiv**: [2608.07004](https://arxiv.org/abs/2608.07004)
- **PDF**: https://arxiv.org/pdf/2608.07004
- **详细分析**: [[20_Research/Papers/机器人/Benchmarking_and_Reasoning_Distillation_of_Large_Language_Models_for_Feedback_Controller_Design_in_Complex_Dynamical_Systems|Benchmarking and Reasoning Distillation of Large Language Models for Feedback Controller Design in Complex Dynamical Systems]]
- **作者**: Zhongchao Zhou, Yixuan Xie, Wenwei Yu, Yuxi Lu, Yaonan Zhu, Qian Niu, Yutaka Matsuo, Yusuke Iwasawa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Benchmarking and Reasoning Distillation of Large Language Models for Feedback Controller Design in Complex Dynamical Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoDyControlBench, ControlBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although remarkable capabilities have been demonstrated by Large Language Models (LLMs) across scientific domains, feedback controller design remains underexplored. Existing benchmarks focus mainly on linear single-Degree-of-Freedom (DoF) systems and large API-hosted models, leaving performance on complex controller-design tasks and feasibility for edge deployment unclear. To address these limitations, we introduce the Complex Dynamics-to-Control Benchmark for Large Language Models (CoDyControlBench), comprising 132 system configurations across five evaluation dimensions: number of DoF, system type, coupling level, damping regime, and controller type. Six state-of-the-art LLMs were evaluated over three independent runs, including three commercial models (GPT, Gemini, and Claude) and three open-source models (GLM, DeepSeek, and Qwen). GPT achieved the highest design success rate at 94.8\%, whereas Qwen showed the lowest rate at 50.0\%. Across the benchmark dimensions, DoF and controller type exhibited the largest model-averaged variations in design success, with success-rate ranges of 36.3\% and 17.6\%, respectively, exceeding those associated with system type, coupling level, and damping regime. Comparison of GPT and Qwen showed that their performance gap arose mainly from the control-design knowledge, particularly gain selection and the use of transient-limiting mechanisms. For edge deployment, a specialized 1.5B-parameter model was developed through reasoning distillation. The reasoning-distilled model outperformed the answer-distilled and base model on CoDyControlBench, maintained stable performance across 1-6 DoFs, and achieved successful traget tracking in all three physical trials on a pneumatic-artificial-muscle-driven robotic arm. These results establish a benchmark baseline and highlight the potential of lightweight, edge-deployable controller-design models.

</details>

---

### [[20_Research/Papers/具身智能/A_Haptic_Robot_Finger_Designed_for_Guqin_Instrument_Playing|A Haptic Robot Finger Designed for Guqin Instrument Playing]]

![[assets/2608.07002_figure.jpg|800]]

- **arXiv**: [2608.07002](https://arxiv.org/abs/2608.07002)
- **PDF**: https://arxiv.org/pdf/2608.07002
- **详细分析**: [[20_Research/Papers/具身智能/A_Haptic_Robot_Finger_Designed_for_Guqin_Instrument_Playing|A Haptic Robot Finger Designed for Guqin Instrument Playing]]
- **作者**: Tianwei Zhang, Hanming Yan, Yang Yang. Ziya Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.8（加权：具身智能 1.2，大模型 0.1，机器人 1.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《A Haptic Robot Finger Designed for Guqin Instrument Playing》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the rapid advancement of humanoid robotics and embodied intelligence technologies, numerous musical instrument-playing robots have emerged in recent years, such as pianos, chime bells, and taiko drums. These robots primarily employ open-loop positional control, rendering them incapable of operating instruments requiring dexterous hands and precise tactile perception, such as a violin, guitar, and guqin. This paper describes the design and validation of a high-precision tactile-sensing finger. By mimicking the shape of the fingertip and fingernail found on a human finger, we develop a biomimetic multimodal haptic fingertip and validate it on selected guqin string-contact tasks, including open-string and stopped-note comparisons, harmonic-tuning, and tactile-triggered bimanual coordination, using the guqin, a traditional Chinese musical instrument, as a challenging validation scenario rather than as a fully demonstrated robotic performance system. This research integrates tactile sensing with robotics technology, thereby contributing to applications in world heritage conservation and cultural dissemination.

</details>

---

### [[20_Research/Papers/具身智能/Cross-View_Action_Consistency_for_Camera-Robust_Vision-Language-Action_Policies|Cross-View Action Consistency for Camera-Robust Vision-Language-Action Policies]]

![[assets/2608.06965_figure.png|800]]

- **arXiv**: [2608.06965](https://arxiv.org/abs/2608.06965)
- **PDF**: https://arxiv.org/pdf/2608.06965
- **详细分析**: [[20_Research/Papers/具身智能/Cross-View_Action_Consistency_for_Camera-Robust_Vision-Language-Action_Policies|Cross-View Action Consistency for Camera-Robust Vision-Language-Action Policies]]
- **作者**: Bingqi Huang, Bingchuan Wei, Xuan Wang, Yingkai Cai, Zhaokui Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Cross-View Action Consistency for Camera-Robust Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Cross-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies fine-tuned from a fixed scene camera can fail when the camera is moved, even when the task, objects, language, and robot state are unchanged. We study scene-camera viewpoint robustness using only a scene RGB image, language, and proprioception, without camera labels, extrinsics, depth, or point-cloud inputs. The wrist stream is masked throughout to prevent an unperturbed visual shortcut from confounding attribution to scene-camera variation. For flow-based VLAs, we propose to regularize the action-flow velocity field, the quantity directly integrated to generate continuous action chunks. We construct action-equivalent view pairs by resetting original LIBERO demonstrations to the same MuJoCo state and rendering nominal and perturbed scene-camera views. Both views are supervised by flow matching, while a cross-view loss encourages their predicted action-flow velocities to agree at the same sampled flow coordinates. On the LIBERO-Plus camera-perturbation track, our method reaches 87.2$\pm$0.4% (4,797 rollouts per seed across 3 training seeds), +7.4pp over flow-matching-only training on the same paired data (79.8$\pm$0.8%, also 3 seeds) and +12.5pp over naive mixed-camera SFT, while maintaining nominal-camera ID performance (95.0$\pm$0.8%; same-data FM-only: 95.0$\pm$4.3%). A shuffled-pair control collapses to 25.8%, showing that the gain depends on action-equivalent pairing. On a real robot, we evaluate three tabletop tasks with 10 rollouts per task and camera placement; held-out-camera success improves from 53.3% to 74.4% under the same single-scene-RGB inference interface.

</details>

---

### [[20_Research/Papers/具身智能/Spatiotemporal_Agility_Time-Constrained_Reinforcement_Learning_for_Vision-Guided_Dynamic_Quadrupedal_Interception|Spatiotemporal Agility: Time-Constrained Reinforcement Learning for Vision-Guided Dynamic Quadrupedal Interception]]

![[assets/2608.06907_first_page.png|800]]

- **arXiv**: [2608.06907](https://arxiv.org/abs/2608.06907)
- **PDF**: https://arxiv.org/pdf/2608.06907
- **详细分析**: [[20_Research/Papers/具身智能/Spatiotemporal_Agility_Time-Constrained_Reinforcement_Learning_for_Vision-Guided_Dynamic_Quadrupedal_Interception|Spatiotemporal Agility: Time-Constrained Reinforcement Learning for Vision-Guided Dynamic Quadrupedal Interception]]
- **作者**: Yidong Zhu, Zibo Dai, Tongning Zhang, Leixin Chang, Hua Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.7（加权：具身智能 1.2，强化学习 0.6，机器人 0.9）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Spatiotemporal Agility: Time-Constrained Reinforcement Learning for Vision-Guided Dynamic Quadrupedal Interception》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots require robust agility to perceive and interact with complex and dynamic environments within a constrained time. However, most existing quadruped locomotion works rely on velocity-tracking policy, which struggle to reach precise targets within strict temporal constraints. Moreover, integrating real-time perception with agile locomotion for highly dynamic targets remains challenging due to sensor latency and processing delays. To concretely study and benchmark such agility in dynamic settings, we introduce a challenging ball-catching task for legged robots. This paper proposes an integrated framework that combines a vision module for landing point and time prediction with a direct position and time conditioned RL locomotion policy, instead of intermediate velocity commands. Beyond the method design, this work presents a system-level contribution that completes real-time robotic interception system that integrates multi-camera perception, online trajectory prediction, low-latency target communication, and sim-to-real locomotion control into a closed-loop deployment pipeline. By explicitly predicting the future spatial-temporal target, our approach mitigates perception latency during dynamic interception. We conducted extensive ball-catching experiments for the legged robot. Through comparative experiments against a velocity-tracking baseline, our direct target-conditioned approach achieves a higher success rate in catching balls with predicted landing spots within 2 meters and flight times between 0.8 and 1.2 seconds. This shows that the robot has successfully completed the dynamic ball-catching task under our tested setup. Furthermore, our policy exhibits a smaller performance gap after deployment, suggesting improved sim-to-real behavior in these trials.

</details>

---

### [[20_Research/Papers/具身智能/Unordered_Landmark_Visual_Navigation|Unordered Landmark Visual Navigation]]

![[assets/2608.06833_first_page.png|800]]

- **arXiv**: [2608.06833](https://arxiv.org/abs/2608.06833)
- **PDF**: https://arxiv.org/pdf/2608.06833
- **详细分析**: [[20_Research/Papers/具身智能/Unordered_Landmark_Visual_Navigation|Unordered Landmark Visual Navigation]]
- **作者**: Hao Ren, Junzhe Zhu, Yihan Li, Zetong Bi, Le Zheng, Zhi Li, Yiqing Yuan, Zhaoliang Wan, Dizhe Zhang, Lu Qi, Hui Cheng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Unordered Landmark Visual Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Image-goal navigation is a fundamental capability for embodied AI, yet its practical deployment is strained by strong prior assumptions. Existing methods predominantly rely on temporally ordered video streams or auxiliary sensors (e.g., depth, LiDAR) to maintain spatial consistency. These sequential and multimodal dependencies severely restrict scalability, especially when deploying robots using crowd-sourced or pre-recorded unordered image collections. When temporal priors are removed, current methods struggle with severe perceptual aliasing, noisy associations, and catastrophic mapping failures. To address this underexplored challenge, we propose Unordered Landmark Visual Navigation (ULVN), a unified RGB-only framework free from temporal and odometric priors. ULVN systematically mitigates error accumulation by integrating mapping, localization, and planning. Specifically, it constructs a robust 2D topological map directly from unstructured images via calibrated geometric verification and maximum spanning forest refinement. For closed-loop execution, ULVN abandons sequential heuristics, utilizing a graph-based belief propagation filter with entropy-adaptive fusion for global localization and dynamic subgoal planning. Extensive experiments in simulation and real-world deployments demonstrate that ULVN significantly outperforms state-of-the-art methods.

</details>

---

### [[20_Research/Papers/机器人/Ising_Acceleration_for_Multi-Robot_Multi-Target_Planning|Ising Acceleration for Multi-Robot Multi-Target Planning]]

![[assets/2608.06803_figure.png|800]]

- **arXiv**: [2608.06803](https://arxiv.org/abs/2608.06803)
- **PDF**: https://arxiv.org/pdf/2608.06803
- **详细分析**: [[20_Research/Papers/机器人/Ising_Acceleration_for_Multi-Robot_Multi-Target_Planning|Ising Acceleration for Multi-Robot Multi-Target Planning]]
- **作者**: Ahmet Efe, Recep B. Uludag, Chris H. Kim, Ulya R. Karpuzcu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Ising Acceleration for Multi-Robot Multi-Target Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ising machines are emerging as promising hardware for combinatorial optimization. With recent advances in CMOS Ising technology, they are becoming attractive as low-power accelerator systems for robotics, where energy is limited and combinatorial optimization arises in multiple forms. However, a hardware-aware analysis of where such chips fit within a robotics planning stack is still missing. This paper studies the capabilities and limitations of CMOS Ising machines for low-power acceleration in multi-robot multi-target planning. We analyze three planning layers---target sharing, tour construction, and pathfinding---using real 45-spin all-to-all connected CMOS Ising chips as representative devices. We propose new Ising-based planning methods and a multi-mapping pipeline that uses spin merging, coefficient quantization, and spin-budget branching to adapt subproblems to spin- and coefficient-limited hardware. Our results show that the proposed recursive target-sharing method naturally matches the Ising hardware, achieving up to 8,000x lower energy than a classical baseline. End to end, the Ising pipeline produces routes within 9% of a strong classical baseline at 130x lower energy, showing that compact CMOS Ising machines can be effective in selected parts of the planning stack.

</details>

---

### [[20_Research/Papers/机器人/Hoverflie_An_empirical_investigation_of_rotor_shrouds_to_transform_micro_air_vehicles_into_multi-modal_hovercraft|Hoverflie: An empirical investigation of rotor shrouds to transform micro air vehicles into multi-modal hovercraft]]

![[assets/2608.06707_figure.png|800]]

- **arXiv**: [2608.06707](https://arxiv.org/abs/2608.06707)
- **PDF**: https://arxiv.org/pdf/2608.06707
- **详细分析**: [[20_Research/Papers/机器人/Hoverflie_An_empirical_investigation_of_rotor_shrouds_to_transform_micro_air_vehicles_into_multi-modal_hovercraft|Hoverflie: An empirical investigation of rotor shrouds to transform micro air vehicles into multi-modal hovercraft]]
- **作者**: Mrinmoy Modak, Daniel S. Drew
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Hoverflie: An empirical investigation of rotor shrouds to transform micro air vehicles into multi-modal hovercraft》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Small rotorcraft intended for use indoors or around the built environment have extremely limited flight duration. This paper presents the design and experimental characterization of a custom shroud system that transforms a Crazyflie 2.1 micro air vehicle into a multi-modal robot capable of operating as a high-efficiency hovercraft or a free-flying drone. A custom experimental platform was developed for precise control of hover height and rotor duty cycle, and automated data logging of lift forces. Parametric testing of duct, intake, and nozzle geometries was performed to investigate the impact of shroud configuration on in-ground-effect and free-flight performance. An empirical model is developed which, unlike typical models for ground effect in rotorcraft, captures the suckdown effect that reduces force at intermediate height. It is shown that, through proper design of the shroud, beneficial ground effects can be increased while diminishing negative effects both close to the ground and in free flight. An optimized configuration exhibited nearly three times higher in-ground-effect force while maintaining comparable out-of-ground-effect aerodynamic thrust, although the added shroud mass reduces free-flight control authority. Lightweight shrouds are manufactured using thin-film thermoformed components, and total single-charge flight time is shown to increase by 60% in-ground-effect while decreasing by only 30% in free-flight as compared to the stock drone. Finally, controlled flight in the air, hovering close to the ground, and hover-to-flight transitions are demonstrated using a simple mode-switching controller, with tracking errors reported to quantify performance. This work provides an experimentally-validated and easily adoptable foundation for future research into lightweight ground-effect vehicles and hybrid drone-hovercraft systems.

</details>

---

### [[20_Research/Papers/具身智能/CrossTracer_Cross-Embodiment_Navigation_via_VLA_Model_Reasoning_and_Trace_Residuals_Adapting|CrossTracer: Cross-Embodiment Navigation via VLA Model Reasoning and Trace Residuals Adapting]]

![[assets/2608.06688_first_page.png|800]]

- **arXiv**: [2608.06688](https://arxiv.org/abs/2608.06688)
- **PDF**: https://arxiv.org/pdf/2608.06688
- **详细分析**: [[20_Research/Papers/具身智能/CrossTracer_Cross-Embodiment_Navigation_via_VLA_Model_Reasoning_and_Trace_Residuals_Adapting|CrossTracer: Cross-Embodiment Navigation via VLA Model Reasoning and Trace Residuals Adapting]]
- **作者**: Yao Wang, Siyuan Wang, Zhirui Sun, Wenzheng Chi, Liang Lin, Jiankun Wang, Wenjun Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《CrossTracer: Cross-Embodiment Navigation via VLA Model Reasoning and Trace Residuals Adapting》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OmniVLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models provide strong semantic priors for robot navigation, but they often ignore embodiment-specific mobility constraints. A path that is semantically plausible for one robot may be physically infeasible for another. We propose CrossTracer, a hierarchical framework for cross-embodiment navigation through adaptive trace residuals. CrossTracer represents navigation plans as normalized image-plane waypoints, forming a unified pixel-space interface between semantic reasoning and physical grounding. First, Vision-Language Trace Proposer (VL-Tracer) adapts a pretrained VLA model to predict an initial navigation trace from egocentric observations and flexible goal specifications. Second, CE-Adapter refines this trace by predicting embodiment-conditioned residual corrections from visual traversability cues, robot identity, and the initial trace. To train the refinement module without costly manual annotation, Cross-Embodiment RRT* (CE-RRT*) converts panoptic segmentation into robot-conditioned traversability cost maps and generates cost-minimizing pixel-space traces. We evaluate CrossTracer on the NaviTrace benchmark, which tests whether a model can generate embodiment-consistent navigation traces from egocentric observations, language instructions, and robot embodiment types. CrossTracer achieves a total score of 45.68, outperforming the strongest evaluated general-purpose baseline, Gemini-2.5-Pro, by 10.01 points, corresponding to a 28.1% relative improvement. Real-world deployment on wheeled and legged robots further shows improved navigation success and execution efficiency.

</details>

---

### [[20_Research/Papers/机器人/A_Disturbance_in_the_Force_Force_Actuation_on_the_RAVEN_II_Surgical_Robot_with_Parallel_Motor-Cable_Units|A Disturbance in the Force: Force Actuation on the RAVEN II Surgical Robot with Parallel Motor-Cable Units]]

![[assets/2608.06488_figure.png|800]]

- **arXiv**: [2608.06488](https://arxiv.org/abs/2608.06488)
- **PDF**: https://arxiv.org/pdf/2608.06488
- **详细分析**: [[20_Research/Papers/机器人/A_Disturbance_in_the_Force_Force_Actuation_on_the_RAVEN_II_Surgical_Robot_with_Parallel_Motor-Cable_Units|A Disturbance in the Force: Force Actuation on the RAVEN II Surgical Robot with Parallel Motor-Cable Units]]
- **作者**: Haonan Peng, Dun-Tin Chiang, Jordan Hendricks, Andrew Lewis, Jared Shing, Haokun Feng, Yun-Hsuan Su, Blake Hannaford
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Disturbance in the Force: Force Actuation on the RAVEN II Surgical Robot with Parallel Motor-Cable Units》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Difficulty in haptic feedback for surgical robots has been a long-term problem for decades. In recent years, learning-based force estimation from robot states suggests desirable accuracy without the necessity of extra sensors. However, challenges remain in obtaining representative training data in which the robot moves in the workspace under various external forces. In this work, a parallel motor-cable system is developed. With six motor-cable units installed around the robot workspace, cables with controllable tension connected to the robot end-effector can provide the desired external force without interfering with the movement of the surgical robot. The development of the system includes motor-unit hardware, control software, sensor drivers, simulations, and more. Preliminary experiments suggest an accuracy of force actuation with errors less than 1 N.

</details>

---

### [[20_Research/Papers/机器人/Beyond_Visibility_Real-Time_Surface_Accessibility_Fields_from_Sparse_LiDAR|Beyond Visibility: Real-Time Surface Accessibility Fields from Sparse LiDAR]]

![[assets/2608.06412_figure.png|800]]

- **arXiv**: [2608.06412](https://arxiv.org/abs/2608.06412)
- **PDF**: https://arxiv.org/pdf/2608.06412
- **详细分析**: [[20_Research/Papers/机器人/Beyond_Visibility_Real-Time_Surface_Accessibility_Fields_from_Sparse_LiDAR|Beyond Visibility: Real-Time Surface Accessibility Fields from Sparse LiDAR]]
- **作者**: Bradley Scott, Sam Schofield, Richard Green
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Beyond Visibility: Real-Time Surface Accessibility Fields from Sparse LiDAR》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Understanding which surfaces in a scene are physically accessible to a given tool is fundamental for robotic interaction, yet 3D perception systems typically stop at geometric reconstruction or visibility estimation. Existing geometric accessibility methods require complete, noise-free meshes and fixed kinematic bases, assumptions that fail for mobile platforms mapping incrementally from live data; visibility estimation cannot account for tool geometry or approach-corridor clearance. We propose the Accessibility Field: a per-point labelling of surface accessibility for a given tool, produced in real time from streaming sparse LiDAR and updated at sensor rate as the platform moves. Running entirely on GPU, our method evaluates each surface point against precomputed geometry kernels representing the tool at a set of rotated approach orientations, checking tool collisions and approach-corridor clearance. A scan-centric Truncated Signed Distance Field integration scheme underpins our system, updating only voxels near each observed return rather than projecting every frustum voxel each frame -- critical for nonrepetitive sensors like the Livox Mid-360, where some bins contain no returns. Our system is tool-agnostic, needs no prior scene model, and runs on workstation and Jetson Orin edge hardware. We evaluate quantitatively on synthetic objects and mature-scale Pinus radiata models, showing visibility alone is insufficient as an accessibility proxy: our method achieves F1=90.8 vs. 69.8 for a Hidden Point Removal baseline on mixed-accessibility geometry, and correctly identifies 56.8% of pine branch surfaces as inaccessible despite being visible from the sensor. To our knowledge, this is the first method to estimate per-point surface accessibility in real time from streaming sparse LiDAR without a prior scene model or fixed base frame -- a capability visibility estimation cannot provide.

</details>

---
