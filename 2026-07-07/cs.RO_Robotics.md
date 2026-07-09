# cs.RO | Robotics | 2026-07-07

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/具身智能/InternVLA-A1.5_Unifying_Understanding,_Latent_Foresight,_and_Action_for_Compositional_Generalization|InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization]]

![[assets/2607.04988_figure.png|800]]

- **arXiv**: [2607.04988](https://arxiv.org/abs/2607.04988)
- **PDF**: https://arxiv.org/pdf/2607.04988
- **详细分析**: [[20_Research/Papers/具身智能/InternVLA-A1.5_Unifying_Understanding,_Latent_Foresight,_and_Action_for_Compositional_Generalization|InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization]]
- **作者**: Haoxiang Ma, Junhao Cai, Xiaoxu Xu, Hao Li, Yuyin Yang, Yang Tian, Jiafei Cao, Hongrui Zhu, Zherui Qiu, Zhaxizhuoma, Yuqiang Yang, Jiaqi Peng...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《InternVLA-A1.5: Unifying Understanding, Latent Foresight, and Action for Compositional Generalization》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DeltaNet, EBench, InternVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unified models for robot manipulation aim to equip one policy with both the semantic priors of pretrained VLMs and the physical dynamics learned through future prediction. In practice, existing designs tend to erode the semantics of the pretrained backbone, suffer interference among heterogeneous objectives, and learn future prediction from scratch in pixel space, leaving the dynamics priors of pretrained video generators unexploited. We present InternVLA-A1.5, which builds the policy on a native VLM backbone that keeps training on VQA and subtask prediction, and attaches a lightweight unified expert for continuous action generation. Future prediction is recast as a latent-querying problem, where a small set of learnable foresight tokens condenses the task-relevant future into a compact latent code under the supervision of a frozen pretrained video generation model, so the policy inherits world-model dynamics priors without ever learning pixel-level generation. The video branch is discarded at inference, keeping real-time control. Pretrained on 1.2M robot episodes and 3M multimodal samples, InternVLA-A1.5 achieves the best overall results on all six simulation benchmarks. In the real world, the preserved semantics deliver the strongest compositional generalization on held-out instruction bindings, and the two designs together sustain long-horizon execution.

</details>

---

### [[20_Research/Papers/具身智能/Closing_the_Reality_Gap_Zero-Shot_Sim-to-Real_Deployment_for_Dexterous_Force-Based_Grasping_and_Manipulation|Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]

![[assets/2607.04940_figure.png|800]]

- **arXiv**: [2607.04940](https://arxiv.org/abs/2607.04940)
- **PDF**: https://arxiv.org/pdf/2607.04940
- **详细分析**: [[20_Research/Papers/具身智能/Closing_the_Reality_Gap_Zero-Shot_Sim-to-Real_Deployment_for_Dexterous_Force-Based_Grasping_and_Manipulation|Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation]]
- **作者**: Zhe Zhao, Zhibin Li, Yilin Ou, Mengshi Qi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.8（加权：具身智能 3.9，强化学习 0.4，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Closing the Reality Gap: Zero-Shot Sim-to-Real Deployment for Dexterous Force-Based Grasping and Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-like dexterous hands with multiple fingers offer human-level manipulation capabilities but remain difficult to train the control policies that can deploy on real hardware due to contact-rich physics and imperfect actuation. We present a sim-to-real reinforcement learning method that leverages dense tactile feedback combined with joint torque sensing to explicitly regulate physical interactions. To enable effective sim-to-real transfer, we introduce (i) a computationally fast tactile simulation that computes distances between dense virtual tactile units and the object via parallel forward kinematics, providing high-rate, high-resolution touch signals needed by RL; (ii) a current-to-torque calibration that eliminates the need for torque sensors on dexterous hands by mapping motor current to joint torque; and (iii) actuator dynamics modeling with randomization to account for non-ideal torque-speed effects and bridge the actuation gaps. Using an asymmetric actor-critic PPO pipeline, we train policies entirely in simulation and deploy them directly to a five-finger hand. The resulting policies demonstrate two essential human-hand skills: (1) command-based controllable grasp force tracking and (2) reorientation of objects in the hand, both of which are robustly executed without fine-tuning on the robot. By combining tactile and torque in the observation space with scalable sensing and actuation modeling, our system provides a practical solution to achieve reliable dexterous manipulation. To our knowledge, this is the first demonstration of controllable grasping on a multi-finger dexterous hand trained entirely in simulation and transferred zero-shot on real hardware.

</details>

---

### [[20_Research/Papers/具身智能/PRISM_Personalized_Robotic_Dataset_Generation_via_Image-based_Scene_and_Motion_Synthesis|PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis]]

![[assets/2607.04880_figure.png|800]]

- **arXiv**: [2607.04880](https://arxiv.org/abs/2607.04880)
- **PDF**: https://arxiv.org/pdf/2607.04880
- **详细分析**: [[20_Research/Papers/具身智能/PRISM_Personalized_Robotic_Dataset_Generation_via_Image-based_Scene_and_Motion_Synthesis|PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis]]
- **作者**: Dogyu Ko, Haneul Kim, Chanyoung Yeo, Dowoon Lee, Taeho Park, Hyoseok Hwang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PRISM: Personalized Robotic Dataset Generation via Image-based Scene and Motion Synthesis》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Gen2Sim, Real-World, Real-to-Sim, Sim-to-LIBERO, Sim-to-Sim, X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in large-scale pretrained vision-language-action models have improved robot policy learning, but directly deploying such policies in user-specific environments remains challenging due to limited generalization, which inevitably requires collecting a dataset tailored to the target environment. Teleoperation yields well-aligned data but is costly and difficult to scale, whereas simulation scales easily but struggles to resemble the target environment and generate task-specific trajectories. To meet both simultaneously, we propose PRISM, an end-to-end pipeline that generates personalized robotic datasets from a single image and a natural-language instruction. PRISM constructs digital cousin scenes that are semantically and geometrically aligned with the user environment yet diverse at the instance level, and synthesizes executable demonstrations without human teleoperation. Extensive experiments show that policies trained on PRISM-generated datasets outperform those trained on baseline-generated datasets on LIBERO and LIBERO-Plus, achieve up to 100\% success rate on three real-world manipulation tasks, and maintain stronger performance when evaluated in environments that differ from those seen during training.

</details>

---

### [[20_Research/Papers/强化学习/Athena-WBC_Capability-Aligned_Policy_Experts_for_Long-Tail_Humanoid_Whole-Body_Control|Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control]]

![[assets/2607.04837_figure.png|800]]

- **arXiv**: [2607.04837](https://arxiv.org/abs/2607.04837)
- **PDF**: https://arxiv.org/pdf/2607.04837
- **详细分析**: [[20_Research/Papers/强化学习/Athena-WBC_Capability-Aligned_Policy_Experts_for_Long-Tail_Humanoid_Whole-Body_Control|Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control]]
- **作者**: Yuan Jiang, Ningyuan Zhang, Xicun Yang, Shidi Li, Yuzhi Jiang, Zhiyi Rong, Shuaikang Ma, Chuanzheng Li, Jie Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《Athena-WBC: Capability-Aligned Policy Experts for Long-Tail Humanoid Whole-Body Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Training-Set。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale humanoid motion-tracking controllers are commonly improved by reallocating training effort: difficult motions are sampled more often, isolated into smaller subsets, or assigned to specialized experts. We show that this view is incomplete. In strong whole-body-control baselines, a residual set of feasible training clips remains unsolved even under targeted training, especially for high-dynamic transitions and balance-critical motions. These failures arise not only from insufficient exposure, but from a mismatch between the motion demands and the effective capability induced by the default training recipe. We propose Athena-WBC, a compact teacher-student pipeline with capability-aligned policy experts for long-tail humanoid whole-body control. Dynamic experts use a tracking-focused, constraint-aware objective that removes conservative effort and temporal-control penalties while preserving physical feasibility constraints; balance experts use a gravity curriculum to improve early-training survivability. The resulting privileged teachers are motion-routed for DAgger distillation and then compressed into a single controller with deployable observations followed by RL fine-tuning. Experiments on a full-size humanoid show improved recovery of training-set long-tail motions and better held-out tracking than a strong SONIC-recipe baseline, using only a small number of experts.

</details>

---

### [[20_Research/Papers/具身智能/CAC-VLA_Context-Gated_Action_Conditioning_for_Vision-Language-Action_Models|CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models]]

![[assets/2607.04816_figure.png|800]]

- **arXiv**: [2607.04816](https://arxiv.org/abs/2607.04816)
- **PDF**: https://arxiv.org/pdf/2607.04816
- **详细分析**: [[20_Research/Papers/具身智能/CAC-VLA_Context-Gated_Action_Conditioning_for_Vision-Language-Action_Models|CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models]]
- **作者**: Yifu Xiong, Wenhao Yu, Jiaxuan Lin, Bojun Zou, Jiahao Li, Lu Zhang, Yanyong Zhang, Jianmin Ji
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.7（加权：具身智能 3，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《CAC-VLA: Context-Gated Action Conditioning for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ACoT-VLA, CAC-VLA, Real-World, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have become a promising paradigm for generalist robot manipulation, where visual-language representations are used to condition continuous action generation. However, these representations are not explicitly optimized for action conditioning, leaving the action expert to bridge the gap between multimodal understanding and precise motor control. Recent action-reasoning methods introduce additional modules to generate explicit action plans or action-space reasoning signals, demonstrating the benefit of action-level guidance but often requiring separate action-generation frameworks. We propose CAC-VLA, a Context-Gated Action Conditioning framework that learns a lightweight latent-action interface directly within the VLM. Instead of generating executable trajectories, CAC-VLA trains the VLM to predict coarse-to-fine latent actions, which are structured representations encoded from future action segments, and adaptively leverages them to condition the action expert via a context gate. This enables VLM-native action conditioning while calibrating the influence of latent-action guidance on expert action generation. Experiments on LIBERO and LIBERO-Plus demonstrate the effectiveness of CAC-VLA, achieving 98.3% average success rate on LIBERO and 89.5% LIBERO-Plus, suggesting that context-gated latent-action conditioning is an effective interface for continuous expert control.

</details>

---

### [[20_Research/Papers/具身智能/KAM-WM_Kinematic_Affordance_Maps_from_Latent_World_Models_for_Robot_Manipulation|KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation]]

![[assets/2607.04652_figure.png|800]]

- **arXiv**: [2607.04652](https://arxiv.org/abs/2607.04652)
- **PDF**: https://arxiv.org/pdf/2607.04652
- **详细分析**: [[20_Research/Papers/具身智能/KAM-WM_Kinematic_Affordance_Maps_from_Latent_World_Models_for_Robot_Manipulation|KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation]]
- **作者**: Xinyu Shao, Keru Zhou, Guowei Huang, Yajun Gao, Tongtong Cao, Xiu Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 2.9（加权：具身智能 1.2，世界模型 0.8，机器人 0.9）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《KAM-WM: Kinematic Affordance Maps from Latent World Models for Robot Manipulation》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning manipulation from few demonstrations requires visual priors that capture not only where to interact, but also how the interaction should begin; static priors such as segmentation masks encode only the former. We present KAM-WM, a framework that extracts a coarse directional interaction cue from a frozen latent video world model without rollout or world-model fine-tuning. KAM-WM queries a Flow Matching image-to-video backbone once and interprets its single-step latent velocity as a Kinematic Affordance Map (KAM), which provides task-conditioned interaction regions and coarse motion structure. A lightweight Perceiver compresses KAM into tokens that condition a diffusion policy together with RGB observations and proprioception. Across LIBERO and RoboTwin2.0, KAM-WM reaches 90.6% average success on LIBERO and achieves 65.7% and 22.4% success rates in the Easy and Hard settings on RoboTwin2.0, respectively. Controlled comparisons against a zero-order mask prior suggest that part of the gains comes from directional information beyond spatial localization alone. These results indicate that, in the evaluated settings, a frozen video model can provide a useful first-order visual prior for control without the test-time cost of future rollout.

</details>

---

### [[20_Research/Papers/机器人/RoboVista_Evaluating_Vision_Language_Models_for_Diverse_Robot_Applications|RoboVista: Evaluating Vision Language Models for Diverse Robot Applications]]

![[assets/2607.04610_figure.png|800]]

- **arXiv**: [2607.04610](https://arxiv.org/abs/2607.04610)
- **PDF**: https://arxiv.org/pdf/2607.04610
- **详细分析**: [[20_Research/Papers/机器人/RoboVista_Evaluating_Vision_Language_Models_for_Diverse_Robot_Applications|RoboVista: Evaluating Vision Language Models for Diverse Robot Applications]]
- **作者**: Shuangyu Xie, Kaiyuan Chen, Ziyang Chen, Simeon Adebola, Yixuan Huang, Zehan Ma, Tianshuang Qiu, Wentao Yuan, Dhruv Shah, Pannag R. Sanketi, Ken Goldberg
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboVista: Evaluating Vision Language Models for Diverse Robot Applications》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ChartQA, ERQA, OpenVLA, RQA, Robot-VQA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diverse applications for robotics, such as industry and agriculture, require robots to operate across various embodiments, changing visual conditions, and complex planning. Vision-Language Models (VLMs) offer a promising foundation for general-purpose and interpretable robotic reasoning. Aligning VLMs with diverse robot applications requires a modular understanding of the individual decision components that underlie robotic behavior. Capturing such structure is challenging for conventional robot benchmarks that are primarily based on teleoperated, end-to-end datasets. We propose Robot Question Answering (RQA), a modular evaluation framework and RoboVista, a benchmark curated from real robotic systems, research papers, and expert annotations. RoboVista contains 474 Visual Question Answering (VQA) instances with human annotated reasoning and covers 39 unique task types in agricultural, industrial, domestic, surgical robotics, autonomous driving, and open robot datasets. Experiments on RoboVista show that state-of-the-art VLMs exhibit substantial gaps. Physical robot experiments suggest strong correlation between RoboVista performance and real-world task execution.

</details>

---

### [[20_Research/Papers/具身智能/SEAM_Smooth_Execution_of_Action-Chunked_Motion_for_Vision-Language-Action_Policies|SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies]]

![[assets/2607.04609_figure.png|800]]

- **arXiv**: [2607.04609](https://arxiv.org/abs/2607.04609)
- **PDF**: https://arxiv.org/pdf/2607.04609
- **详细分析**: [[20_Research/Papers/具身智能/SEAM_Smooth_Execution_of_Action-Chunked_Motion_for_Vision-Language-Action_Policies|SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies]]
- **作者**: Dijia Zhan, Xuemiao Xu, Jinyi Li, Jie Tang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SEAM: Smooth Execution of Action-Chunked Motion for Vision-Language-Action Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies that execute fixed-length action chunks can exhibit multimodal bifurcation: a cross-chunk inconsistency in which adjacent chunks generated from independent Gaussian latents can converge to incompatible trajectory modes, producing abrupt discontinuities at chunk boundaries. Existing remedies either require backpropagation through the policy at each denoising step, rely on rejection sampling, or require retraining, each trading computational cost or task reliability for smoother transitions. We propose SEAM (Smooth Execution of Action-Chunked Motion), a training-free inference-time method for flow matching VLAs. SEAM exploits a simple synchronous-execution insight: after the robot consumes the executed prefix, the previous chunk's unexecuted tail is already available as an analytic consistency reference. Its core mechanism, Velocity-guided Loss Steering (VLS), derives a time-dependent target from this tail and applies a closed-form correction after each Euler step without backpropagating through the policy network. On LIBERO-10 with pi_0.5, SEAM reduces boundary jerk by 28%, reduces chunk transition discontinuity by 27%, preserves baseline-level task success, and keeps denoising-loop cost near the unguided baseline.

</details>

---

### [[20_Research/Papers/具身智能/HUGS_Guiding_Unified_Dexterous_Grasp_Synthesis_Across_Modes_and_Scales_via_Learned_Human_Priors|HUGS: Guiding Unified Dexterous Grasp Synthesis Across Modes and Scales via Learned Human Priors]]

![[assets/2607.04554_figure.png|800]]

- **arXiv**: [2607.04554](https://arxiv.org/abs/2607.04554)
- **PDF**: https://arxiv.org/pdf/2607.04554
- **详细分析**: [[20_Research/Papers/具身智能/HUGS_Guiding_Unified_Dexterous_Grasp_Synthesis_Across_Modes_and_Scales_via_Learned_Human_Priors|HUGS: Guiding Unified Dexterous Grasp Synthesis Across Modes and Scales via Learned Human Priors]]
- **作者**: Mingrui Yu, Yongpeng Jiang, Yongyi Jia, Kangchen Lv, Li Huang, Yi Ren, Xiang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《HUGS: Guiding Unified Dexterous Grasp Synthesis Across Modes and Scales via Learned Human Priors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HOGraspNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous grasping across diverse object scales requires contact modes ranging from two-finger pinches to bimanual grasps. Existing dexterous grasp synthesis methods reduce the high-dimensional optimization space with manually designed expected contacts and initialization heuristics, which struggle to balance synthesis success rate and diversity. We present HUGS (Human-prior-guided Unified Dexterous Grasp Synthesis), a human-prior-guided framework for unified dexterous grasp synthesis across modes and scales. Instead of directly retargeting human demonstrations, HUGS learns an object-conditioned human prior that captures human grasp preferences and guides downstream force-closure-aware optimization. The prior is trained on a compact self-collected human grasp dataset with 1.8K grasps over 304 objects, providing broad coverage of object scales and contact modes. During synthesis, HUGS adaptively proposes contact modes and wrist initializations, substantially improving the balance between contact-mode coverage and synthesis success rate over heuristic-based methods. With HUGS, we synthesize 3.2M robotic grasps over 157K scenes, spanning object half-diagonal lengths from 2 cm to 30 cm and modes from two-finger to bimanual grasps. Models trained on the synthesized dataset autonomously select appropriate contact modes in the real world, enabling grasping from screws to large boxes.

</details>

---

### [[20_Research/Papers/具身智能/ACE-Brain-0.5_A_Unified_Embodied_Foundational_Model_for_Physical_Agentic_AI|ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI]]

![[assets/2607.04426_first_page.png|800]]

- **arXiv**: [2607.04426](https://arxiv.org/abs/2607.04426)
- **PDF**: https://arxiv.org/pdf/2607.04426
- **详细分析**: [[20_Research/Papers/具身智能/ACE-Brain-0.5_A_Unified_Embodied_Foundational_Model_for_Physical_Agentic_AI|ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI]]
- **作者**: ACE-Brain Team, :, Ziyang Gong, Haoming Gu, Zehang Luo, Tianyi Zhang, Tao Tao, Yixiao Chi, Zhe Liu, Lingsi Zhu, Jingyuan Liu, Anke Tang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.8，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《ACE-Brain-0.5: A Unified Embodied Foundational Model for Physical Agentic AI》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied AI is moving from isolated perception or action modules toward physical agents that understand, plan under goals, act through robot bodies, monitor progress, and improve from experience. Existing systems address this loop only in parts: end-to-end policies generate actions but often lack spatial reasoning, planning, and execution assessment, while robot-agent systems orchestrate tools or specialists but do not learn a shared representation. This fragmentation limits general Physical Agentic AI. We present ACE-Brain-0.5, a unified embodied foundation model that organizes robot intelligence into five coupled functions: spatial perception, decision making, embodied interaction, self-monitoring, and self-improvement. Built on ACE-Brain-0, which established spatial intelligence as a shared scaffold across robot platforms, ACE-Brain-0.5 extends an understanding-centric model into a closed-loop foundation model. A single 8B backbone instantiates the first four functions: grounding objects and affordances, reasoning over 3D and egocentric spatial relations, decomposing instructions into subgoals, generating navigation and manipulation actions, and estimating progress for verification and recovery. To unify these capabilities without cross-task interference, we introduce SSR+, which extends Scaffold-Specialize-Reconcile with a Reactivate stage after task-vector merging. The fifth function, self-improvement, is realized by a companion framework that updates external execution state, including task schemas, spatial memory, and failure-recovery cases, from rollouts. Across fifteen benchmarks, ACE-Brain-0.5 improves over ACE-Brain-0 on 14 of 18 spatial perception and grounding benchmarks, achieves competitive navigation and manipulation performance, and provides strong progress estimation in ID and OOD settings. Together, these results mark an early step toward general Physical Agentic AI.

</details>

---

### [[20_Research/Papers/大模型/SurgAM_Surgical_Affordance_Map_Prediction_with_Multimodal_Feature_Fusion_for_Robot_Autonomy|SurgAM: Surgical Affordance Map Prediction with Multimodal Feature Fusion for Robot Autonomy]]

![[assets/2607.04378_figure.png|800]]

- **arXiv**: [2607.04378](https://arxiv.org/abs/2607.04378)
- **PDF**: https://arxiv.org/pdf/2607.04378
- **详细分析**: [[20_Research/Papers/大模型/SurgAM_Surgical_Affordance_Map_Prediction_with_Multimodal_Feature_Fusion_for_Robot_Autonomy|SurgAM: Surgical Affordance Map Prediction with Multimodal Feature Fusion for Robot Autonomy]]
- **作者**: Lei Song, Yonghao Long, Mengya Xu, Jiayi Geng, Xiuyuan Chen, Qi Dou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SurgAM: Surgical Affordance Map Prediction with Multimodal Feature Fusion for Robot Autonomy》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Surgical automation is being increasingly studied, yet bridging visual scene understanding with autonomous action planning remains a fundamental challenge. While much research effort has been made on scene perception (e.g., tool recognition and scene segmentation), understanding and predicting actionable possibilities for surgical automation is still underexplored. In this paper, we introduce surgical affordance prediction, which identifies actionable regions for fundamental surgical actions from visual data. Specifically, a novel adaptive feature fusion framework is proposed that leverages the complementary strengths of a self-supervised vision transformer encoder for its superior semantic understanding and a large-scale generative model encoder for its spatially-aware capability. Furthermore, we introduce a hierarchical prompt learning mechanism to adapt to varying procedural contexts. Finally, a scene-guided attention decoder is proposed to focus on critical surgical areas while suppressing background distractions. To validate the effectiveness, we established a new dataset, derived from publicly available surgical datasets with affordance annotations for three basic surgical actions: aspiration, clipping, and retraction. Extensive experiments demonstrate that our approach achieves state-of-the-art performance. Moreover, we validate our framework's applicability for downstream automation on a realistic lung and prostate phantom, and results show that the predicted affordance maps successfully enable autonomous surgical actions.

</details>

---

### [[20_Research/Papers/强化学习/A_Perception-Manipulation_Robotics_System_for_Food_Cutting|A Perception-Manipulation Robotics System for Food Cutting]]

![[assets/2607.04367_figure.png|800]]

- **arXiv**: [2607.04367](https://arxiv.org/abs/2607.04367)
- **PDF**: https://arxiv.org/pdf/2607.04367
- **详细分析**: [[20_Research/Papers/强化学习/A_Perception-Manipulation_Robotics_System_for_Food_Cutting|A Perception-Manipulation Robotics System for Food Cutting]]
- **作者**: Xinyuan Luo, Wenzhen Yuan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.4（加权：具身智能 0.3，强化学习 0.2，机器人 0.9）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《A Perception-Manipulation Robotics System for Food Cutting》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the development of cooking robots, mastering the task of cutting is crucial. A significant challenge lies in the diverse properties of food, which necessitate distinct cutting policies and even different knives for optimal processing. This paper presents a perception-manipulation framework for food-cutting tasks. Our system features a knife selection module that utilizes force data from a preliminary fixed trial cut to select the appropriate knife for the given food. This is followed by an adaptive cutting phase using reinforcement learning (RL) to balance cutting speed and energy efficiency. In our experiments, the knife selection module achieved 100% successful rate on unseen food, and we compared the performances of fixed policy, RL policy, with human operators. Our method not only achieves high performance but also demonstrates comparable results to those of human participants.

</details>

---

### [[20_Research/Papers/机器人/FLOAT_Drone_for_Physical_Interaction_Lateral_Airflow_Reduction,_Wrench_Modeling,_and_Adaptive_Control|FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control]]

![[assets/2607.04260_figure.png|800]]

- **arXiv**: [2607.04260](https://arxiv.org/abs/2607.04260)
- **PDF**: https://arxiv.org/pdf/2607.04260
- **详细分析**: [[20_Research/Papers/机器人/FLOAT_Drone_for_Physical_Interaction_Lateral_Airflow_Reduction,_Wrench_Modeling,_and_Adaptive_Control|FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control]]
- **作者**: Junxiao Lin, Kehan Zhou, Shuhang Ji, Yimin Peng, Shen Wang, Jialiang Hou, Fei Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《FLOAT Drone for Physical Interaction: Lateral Airflow Reduction, Wrench Modeling, and Adaptive Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial physical interaction represents a promising direction for next-generation unmanned aerial vehicles (UAVs), but it requires an aerial platform that can exert contact forces while maintaining stable flight. For close-proximity tasks, this translates into three coupled design requirements: multidimensional wrench generation for stable contact, compactness for maneuverability and safety in confined spaces, and reduced lateral airflow toward the target when generating horizontal force. This article presents FLOAT Drone, a fully actuated coaxial UAV with servo-driven control surfaces for close-proximity physical interaction. The coaxial dual-rotor layout provides a compact propulsion layout, while the control surfaces, immersed in the rotor downwash, generate lateral forces and moments for 6-DoF wrench generation. A force-matched computational fluid dynamics (CFD) comparison with a tilted-rotor alternative quantifies the reduction in target-facing lateral airflow. To account for nonlinear rotor--control-surface coupling in the rotor wake, a high-fidelity polynomial aerodynamic wrench model is identified from precision force measurements and embedded in a constrained nonlinear allocator for real-time wrench tracking. Comparative flight and interaction experiments show that the proposed framework improves control accuracy over linear allocation baselines, rejects ground-effect and payload disturbances, and enables close-proximity drawer push--pull manipulation through a $2~\mathrm{cm}$ handle clearance.

</details>

---

### [[20_Research/Papers/机器人/Integrated_Graph_Search_and_Model_Predictive_Control_for_Smooth_and_Efficient_Path_Planning_in_Autonomous_Vehicles|Integrated Graph Search and Model Predictive Control for Smooth and Efficient Path Planning in Autonomous Vehicles]]

![[assets/2607.04259_figure.jpg|800]]

- **arXiv**: [2607.04259](https://arxiv.org/abs/2607.04259)
- **PDF**: https://arxiv.org/pdf/2607.04259
- **详细分析**: [[20_Research/Papers/机器人/Integrated_Graph_Search_and_Model_Predictive_Control_for_Smooth_and_Efficient_Path_Planning_in_Autonomous_Vehicles|Integrated Graph Search and Model Predictive Control for Smooth and Efficient Path Planning in Autonomous Vehicles]]
- **作者**: Duc-Tien Bui, Ngoc Thinh Nguyen, Hung Duy Nguyen, Dong Bi, Tomislav Mihalj, Arno Eichberger
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Integrated Graph Search and Model Predictive Control for Smooth and Efficient Path Planning in Autonomous Vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Path planning is a fundamental component of autonomous vehicles, where achieving safe, comfortable, and dynamically feasible paths while ensuring computational efficiency remains a significant challenge. This paper presents a sequential path planning framework in which a rough path obtained from graph search is explicitly exploited to guide a Model Predictive Control (MPC)-based path refinement. A rough path is first obtained via Dijkstra search on a discretized grid and is then used to construct a spatially varying convex lateral safety corridor that explicitly captures obstacle avoidance constraints, transforming discrete obstacle avoidance decisions into continuous feasibility constraints for optimization. Within this corridor, an MPC problem is formulated to refine the path, enabling efficient optimization while maintaining path smoothness by penalizing the third-order spatial derivative of the lateral offset over a prediction horizon. The proposed algorithm is evaluated in multiple overtaking scenarios on both straight and curved roads, including cases with single and multiple target vehicles, using high-fidelity environment simulations (i.e., CarMaker). Compared with the previous study, which used polynomial fitting and a quadratic programming method, the proposed approach consistently achieves lower lateral acceleration, curvature, and jerk while reducing computational cost by 28.08% on straight roads and 29.52% on curved roads. These results demonstrate that exploiting graph-search structure within an MPC formulation provides an effective balance between path smoothness and computational efficiency for autonomous vehicles in structured driving environments.

</details>

---

### [[20_Research/Papers/具身智能/WSA$_1$_a_3D-Centric_World-Spatial-Action_Model_for_Generalizable_Robot_Control|WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control]]

![[assets/2607.03941_figure.png|800]]

- **arXiv**: [2607.03941](https://arxiv.org/abs/2607.03941)
- **PDF**: https://arxiv.org/pdf/2607.03941
- **详细分析**: [[20_Research/Papers/具身智能/WSA$_1$_a_3D-Centric_World-Spatial-Action_Model_for_Generalizable_Robot_Control|WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control]]
- **作者**: Jiahao Jiang, Jianing Zhang, Zhenhan Yin, Ruidong Chen, Sen Wang, Zhaoshu Yu, Pengpeng Zeng, Xiaofeng Cao, Xuanhan Wang, Jingkuan Song, Heng Tao Shen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《WSA$_1$: a 3D-Centric World-Spatial-Action Model for Generalizable Robot Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, PointWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in embodied AI have established robot foundation models (RFMs) as the dominant approach for generalist robotic systems to date. By leveraging imitation learning on extensive robot demonstrations, RFMs have achieved impressive capabilities in mapping visual observations and language instructions to continuous robotic actions. However, current RFMs lack an inherent ability to reason about physical dynamics and the causal effects of robot behaviors on the 3D physical world. This creates a fundamental mismatch between 2D-centric visual perception and 3D-centric embodied interaction, severely limiting the generalization ability of RFMs in real-world tasks.To address this gap, we present WSA$_1$, a novel RFM built upon proposed 3D-Centric World-Spatial-Action modeling paradigm. It not only learns 3D world-aware visual thought for future robot behaviors, but also models mutual constraints between 3D world state transitions and robotic actions to enhance behavior generalization. Notably, WSA$_1$ achieves highly data-efficient pre-training with 6k hours of expert demonstration data (only 1k hours from real robot), while delivering competitive manipulation performance (93% success rate) on RoboTwin2.0 simulation benchmark and achieving +20% average boosted performance over state-of-the-art RFMs on real-world robot control tasks. These results reveal that generalizable RFM can be attained without large-scale real robot data when paired with 3D-centric world-action joint modeling, which offers a practical and affordable pathway to generalist robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/ObjRetarget_An_Object-Aware_Motion_Retargeting_Framework_with_Anthropomorphic_Arm_Constraints_and_Polyhedral_Hand_Modeling|ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand Modeling]]

![[assets/2607.03828_first_page.png|800]]

- **arXiv**: [2607.03828](https://arxiv.org/abs/2607.03828)
- **PDF**: https://arxiv.org/pdf/2607.03828
- **详细分析**: [[20_Research/Papers/具身智能/ObjRetarget_An_Object-Aware_Motion_Retargeting_Framework_with_Anthropomorphic_Arm_Constraints_and_Polyhedral_Hand_Modeling|ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand Modeling]]
- **作者**: Yuanchuan Lai, Qing Gao, Ziyan Liang, Junjie Hu, Zhaojie Ju
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.9，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《ObjRetarget: An Object-Aware Motion Retargeting Framework with Anthropomorphic Arm Constraints and Polyhedral Hand Modeling》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning robot dexterous manipulation from human manipulation videos requires reliably retargeting human intent to executable robot actions while maintaining stable hand-object contact, which remains a key challenge in embodied intelligence. Existing retargeting methods often ignore explicit contact modeling or rely on reinforcement learning, resulting in limited accuracy and generalization. To address this, we propose ObjRetarget, a human-to-robot motion retargeting framework for learning robot dexterous manipulation from human videos, which integrates anthropomorphic arm trajectory constraints with structured hand-object geometric modeling. For arm motion, reference trajectories extracted from human videos are used for initialization, followed by anthropomorphic constraints and redundancy-aware optimization to generate natural and accurate movements. For hand manipulation, ObjRetarget represents multi-finger contacts using polytope clusters and preserves contact structure through geometric invariants to improve stability. Experiments on real robots show that ObjRetarget improves manipulation success rates and contact stability across multiple dexterous tasks, and generalizes well to different demonstrations, object poses, and task settings.

</details>

---

### [[20_Research/Papers/具身智能/Look_Before_You_Leap_Distilling_Tree_Search_into_Action_Evaluation_for_Frozen_VLA_Models|Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models]]

![[assets/2607.03751_figure.png|800]]

- **arXiv**: [2607.03751](https://arxiv.org/abs/2607.03751)
- **PDF**: https://arxiv.org/pdf/2607.03751
- **详细分析**: [[20_Research/Papers/具身智能/Look_Before_You_Leap_Distilling_Tree_Search_into_Action_Evaluation_for_Frozen_VLA_Models|Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models]]
- **作者**: Xinyi Xie, Zican Hu, Zhanyu Liu, Yicheng Dong, Wenhao Wu, Zhenhong Sun, Haoran Li, Chunlin Chen, Zhi Wang, Pichao Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.6（加权：具身智能 2.1，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Look Before You Leap: Distilling Tree Search into Action Evaluation for Frozen VLA Models》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoVer-VLA, EmbodiedBench, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models acquire broad embodied capabilities through large-scale pretraining, yet their generalization remains far more fragile than that of LLMs and VLMs. The prevailing remedy, post-training via supervised fine-tuning or reinforcement learning, improves task-specific performance but narrows the generalist capability that makes pretraining valuable. We identify a key bottleneck: VLA failures stem not only from action generation but also from action evaluation. A diagnostic pass@k study confirms that frozen VLAs already contain competent behaviors in their output distribution, with overall success rates rising from 33% at pass@1 to 92% at pass@32. Inspired by this, we propose SVA (Search, Value, and Act), a simple framework that equips frozen VLA policies with long-term consequence awareness. SVA first uses Monte-Carlo tree search in simulation to fully explore the VLA's output distribution and collect diverse trajectories annotated with empirical returns; this knowledge is then distilled into a lightweight Q-value model that predicts the expected consequence of candidate actions; at deployment, the frozen VLA proposes multiple candidates and the evaluator selects the one with the highest uncertainty-regularized Q-value, requiring no simulator access. By decoupling action proposal from consequence evaluation, SVA preserves the generalization capacity of the VLA backbone while substantially improving task success rates. Experiments across embodied benchmarks show that SVA consistently improves generalization on unseen tasks and exhibits strong test-time scaling behavior. Strikingly, SVA enables a 9B VLA to outperform a 27B VLA by 7 points at 27% lower inference latency, suggesting that scaling test-time evaluation is more cost-effective than scaling model size.

</details>

---

### [[20_Research/Papers/具身智能/CoRE-VLA_Towards_Scalable_and_Robust_Vision-Language-Action_Modeling_via_Conditional_Routing_of_Experts|CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts]]

![[assets/2607.03693_figure.png|800]]

- **arXiv**: [2607.03693](https://arxiv.org/abs/2607.03693)
- **PDF**: https://arxiv.org/pdf/2607.03693
- **详细分析**: [[20_Research/Papers/具身智能/CoRE-VLA_Towards_Scalable_and_Robust_Vision-Language-Action_Modeling_via_Conditional_Routing_of_Experts|CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts]]
- **作者**: Haozhe Zhang, Sixian Li, Yifei Zhang, Zezheng Huai, Hao Chen, Chunhua Shen, Jingjing Gong, Xipeng Qiu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.7（加权：具身智能 3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《CoRE-VLA: Towards Scalable and Robust Vision-Language-Action Modeling via Conditional Routing of Experts》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoRE-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have advanced generalist robotic manipulation, yet real-world deployment reveals a fundamental challenge: robots are equipped with diverse and heterogeneous sensor configurations, auxiliary sensors can fail unexpectedly during operation, and different robot embodiments often lack certain sensors by design. A unified policy that can exploit auxiliary perceptual inputs when available while remaining reliable under sensor absence, whether incidental or by design, is therefore essential for practical deployment. However, existing VLA policies couple action generation to a fixed sensor set through shared dense computation, making them brittle when sensors are missing and limiting their ability to specialize across diverse tasks and long-horizon behaviors. We propose CoRE-VLA, a scalable and robust VLA framework that formulates action generation as context-conditioned sparse computation. Sensor availability gates modality-specialized experts, enabling graceful degradation under missing sensors without retraining. Task intent further routes action-side representations to task-relevant experts, improving specialization across diverse tasks and long-horizon subgoals. While the framework is designed to accommodate different auxiliary sensors, we focus on depth as a representative and practically important auxiliary modality in our experiments. Experiments on LIBERO, RoboCasa GR1 Tabletop, and real-world dual-arm manipulation show that CoRE-VLA achieves strong results on long-horizon and multi-task benchmarks, and outperforms both a dense-action-generator ablation and a strong pretrained VLA baseline, including in zero-shot generalization to unseen scenarios. Modality analysis shows that CoRE-VLA can exploit auxiliary depth when available while remaining robust when depth is unavailable during deployment.

</details>

---

### [[20_Research/Papers/具身智能/ROBOCYCLE_Autonomous_Dual-Arm_Robotic_Manipulation_and_Coordination_for_Recycling_Applications|ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications]]

![[assets/2607.03616_figure.png|800]]

- **arXiv**: [2607.03616](https://arxiv.org/abs/2607.03616)
- **PDF**: https://arxiv.org/pdf/2607.03616
- **详细分析**: [[20_Research/Papers/具身智能/ROBOCYCLE_Autonomous_Dual-Arm_Robotic_Manipulation_and_Coordination_for_Recycling_Applications|ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications]]
- **作者**: Rubén de J. Hilario-Cruz, Jesus A. García-González, Enrique Coronado, Arturo E. Cerón-López
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《ROBOCYCLE: Autonomous Dual-Arm Robotic Manipulation and Coordination for Recycling Applications》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RTDRNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As urban waste volumes escalate and labor shortages intensify, automated waste sorting systems are becoming a necessity. However, current robotic solutions often struggle with the 3D perception and manipulation of transparent, deformable, or cluttered objects. This work introduces ROBOCYCLE, an autonomous dual-arm robotic recycling platform designed to meet the recycling standards of the Tokyo metropolitan area. Our approach integrates multi-view RGB-D perception, transformer-based instance segmentation using RF-DETR, and 6-DoF grasp planning via the Anygrasp SDK. By processing segmentated point clouds, the system generates robust candidate poses for irregular and deformable waste. The system achieved a 90.3% grasp success rate and 84.3% overall task success rate, effectively performing complex coordinated tasks such as unscrewing PET bottle caps. The proposed platform offers a scalable solution for autonomous waste management in real-world human environments.

</details>

---

### [[20_Research/Papers/具身智能/Cross-Embodiment_Robot_Manipulation_via_a_Unified_Hand_Action_Space|Cross-Embodiment Robot Manipulation via a Unified Hand Action Space]]

![[assets/2607.03570_figure.png|800]]

- **arXiv**: [2607.03570](https://arxiv.org/abs/2607.03570)
- **PDF**: https://arxiv.org/pdf/2607.03570
- **详细分析**: [[20_Research/Papers/具身智能/Cross-Embodiment_Robot_Manipulation_via_a_Unified_Hand_Action_Space|Cross-Embodiment Robot Manipulation via a Unified Hand Action Space]]
- **作者**: Luis Felipe Casas, Robert Teal, Keval Shah, Abhijit Tadepalli, Wanxin Jin, Yu Xiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Cross-Embodiment Robot Manipulation via a Unified Hand Action Space》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, XL-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation policies are typically tied to specific robotic hand embodiments, limiting the transfer of learned behaviors across platforms with different kinematic structures. In this work, we propose the Unified Hand Action Space (UHAS), a sphere-based unified action representation for cross-embodiment dexterous manipulation. UHAS represents robotic hand actions as geometric deformations of a canonical sphere and uses a Cascade Inverse Kinematics (CIK) algorithm to map the shared representation to embodiment-specific joint configurations. Using reinforcement learning, we train dexterous manipulation policies directly in the proposed action space for in-hand cube reorientation tasks. We evaluate our method in both simulation and real-world experiments across multiple robotic hands, including the Allegro Hand, LEAP Hand, Shadow Hand, and MANO Human Hand. Experimental results demonstrate effective dexterous manipulation, zero-shot transfer to unseen hands, rapid finetuning across embodiments, and successful real-world deployment. Our experiments show that the proposed UHAS representation enables stable dexterous control and cross-embodiment policy transfer across robotic hands.

</details>

---

### [[20_Research/Papers/具身智能/CoorGrasp_Coordinated_Contact_Control_for_Adaptive_Dexterous_Grasping_Under_Uncertainty|CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]

![[assets/2607.03557_figure.png|800]]

- **arXiv**: [2607.03557](https://arxiv.org/abs/2607.03557)
- **PDF**: https://arxiv.org/pdf/2607.03557
- **详细分析**: [[20_Research/Papers/具身智能/CoorGrasp_Coordinated_Contact_Control_for_Adaptive_Dexterous_Grasping_Under_Uncertainty|CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty]]
- **作者**: Mingrui Yu, Yongpeng Jiang, Yongyi Jia, Ren Yi, Xiang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.7，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《CoorGrasp: Coordinated Contact Control for Adaptive Dexterous Grasping Under Uncertainty》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While recent research has focused heavily on dexterous grasp pose generation, less attention has been devoted to the execution of planned grasps. Under shape and position uncertainty, open-loop execution often yields uncoordinated contacts, causing undesired in-hand object motion and even grasp failures. To address this, this paper proposes a tactile-driven model predictive controller for adaptive and delicate execution of diverse dexterous grasps. Our approach emphasizes multi-contact coordination across both approaching and grasping phases, with three key novelties: (i) coordination-aware phase separation, (ii) arm-hand coordination to compensate for position errors, and (iii) adaptive force coordination to increase contact forces in a balanced manner. An analytical model is employed to relate contact forces to robot joint motions for predictive control. Our formulation imposes no restrictions on grasp types or contact configurations and integrates seamlessly with state-of-the-art grasp pose generation methods. We validate the approach through large-scale simulations involving 15k grasps across 478 objects on three robotic hands, and real-world experiments on 8 objects. Results demonstrate that our method achieves higher grasp success rates and reduced undesired object movements.

</details>

---

### [[20_Research/Papers/具身智能/Current_as_Touch_Proprioceptive_Contact_Feedback_for_Compliant_Dexterous_Manipulation|Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation]]

![[assets/2607.03529_figure.png|800]]

- **arXiv**: [2607.03529](https://arxiv.org/abs/2607.03529)
- **PDF**: https://arxiv.org/pdf/2607.03529
- **详细分析**: [[20_Research/Papers/具身智能/Current_as_Touch_Proprioceptive_Contact_Feedback_for_Compliant_Dexterous_Manipulation|Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation]]
- **作者**: Chenyang Ma, Yunchao Yao, Zhenyu Wei, Ruogu Li, Daniel Szafir, Mingyu Ding
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Current as Touch: Proprioceptive Contact Feedback for Compliant Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Compliance is essential for dexterous manipulation, yet existing solutions often rely on external tactile or force sensors that are costly, fragile, and difficult to deploy on low-cost robot hands. We propose a proprioception-driven framework that learns contact-aware compliance cues from motor current and joint states. Since motor current is closely related to actuator torque, it provides an intrinsic signal for perceiving contact force, object resistance, and grasp stability without additional sensing hardware. Rather than estimating external wrenches or commanding torque, our method predicts a compliance reference position: an ideal joint-position target for a standard PD controller whose induced position error generates appropriate grasping force. This position-based formulation is compatible with mainstream teleoperation and policy-learning pipelines, while enabling the robot to adapt interaction forces from real-time proprioceptive feedback. Thus, motor current serves not only as a force proxy but also as a learnable proprioceptive contact signal for compliance reference prediction. Experiments on multiple dexterous hands and contact-rich tasks, including fragile object handling, sustained surface contact, thin-object retrieval, and dynamic load adaptation, show stable compliant grasping, safer and more efficient teleoperation, and improved downstream policy learning without external tactile or force sensors.

</details>

---

### [[20_Research/Papers/具身智能/High-Precision_Formation_Control_for_Heterogeneous_Multi-Robot_Systems_via_Hierarchical_Hybrid_Physics-Informed_Deep_Reinforcement_Learning|High-Precision Formation Control for Heterogeneous Multi-Robot Systems via Hierarchical Hybrid Physics-Informed Deep Reinforcement Learning]]

![[assets/2607.03512_figure.png|800]]

- **arXiv**: [2607.03512](https://arxiv.org/abs/2607.03512)
- **PDF**: https://arxiv.org/pdf/2607.03512
- **详细分析**: [[20_Research/Papers/具身智能/High-Precision_Formation_Control_for_Heterogeneous_Multi-Robot_Systems_via_Hierarchical_Hybrid_Physics-Informed_Deep_Reinforcement_Learning|High-Precision Formation Control for Heterogeneous Multi-Robot Systems via Hierarchical Hybrid Physics-Informed Deep Reinforcement Learning]]
- **作者**: Yanzhou Li, Guangli Chen, Xiao-Meng Li, Wenjian Zhong, Yongkang Lu, Shenghuang He
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 大模型
- **相关性评分**: 3.3（加权：具身智能 0.3，大模型 0.1，强化学习 1.8，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《High-Precision Formation Control for Heterogeneous Multi-Robot Systems via Hierarchical Hybrid Physics-Informed Deep Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, HHy-PIDRL, HM-DRL, PIDRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing classical control methods commonly require precise models and struggle to cope with model uncertainties and external disturbances, while end-to-end reinforcement learning (RL) approaches suffer from low sample efficiency and poor convergence. To overcome these challenges, this paper proposes a hierarchical hybrid physics-informed deep reinforcement learning (HHy-PIDRL) framework, aiming to realize high-precision, highly responsive formation control for heterogeneous multi-robot systems (HMRSs). The proposed framework contains two layers. Specifically, first, the upper layer designs an autonomous navigation policy network for Ackermann-steering leader based on the Soft Actor-Critic (SAC) deep reinforcement learning (DRL) algorithm. Second, the lower module integrates a high-fidelity physical feed-forward controller, a classical proportional-derivative (PD) controller, and an adaptive DRL residual controller to propose an effective hybrid model and DRL (HM-DRL)-based formation control policy network. Third, a unique hierarchical reward function is designed for training Omnidirectional followers, which effectively guides agents toward a refined, stable control policy. Experimental results demonstrate that, the success rate of both the upper-layer autonomous navigation policy network and the HM-DRL based formation control policy networks reach 100%. Meanwhile, ablation experiments are conducted to verify the validity and credibility of the proposed method.

</details>

---

### [[20_Research/Papers/具身智能/GDPR-Aware_Trajectory_Sharing_for_ISAC-Assisted_Robot_Navigation_A_Case_Study_on_FID-Constrained_Collision_Prediction|GDPR-Aware Trajectory Sharing for ISAC-Assisted Robot Navigation: A Case Study on FID-Constrained Collision Prediction]]

![[assets/2607.03254_figure.png|800]]

- **arXiv**: [2607.03254](https://arxiv.org/abs/2607.03254)
- **PDF**: https://arxiv.org/pdf/2607.03254
- **详细分析**: [[20_Research/Papers/具身智能/GDPR-Aware_Trajectory_Sharing_for_ISAC-Assisted_Robot_Navigation_A_Case_Study_on_FID-Constrained_Collision_Prediction|GDPR-Aware Trajectory Sharing for ISAC-Assisted Robot Navigation: A Case Study on FID-Constrained Collision Prediction]]
- **作者**: Zexin Fang, Bin Han, Donglin Wang, Fengchen Pei, Hans D. Schotten
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Security

#### 研究背景与动机

《GDPR-Aware Trajectory Sharing for ISAC-Assisted Robot Navigation: A Case Study on FID-Constrained Collision Prediction》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Integrated sensing and communication (ISAC) enables intelligent wireless infrastructure but raises growing regulatory concern as fine-grained personal trajectory histories become a byproduct of sensing. General Data Protection Regulation (GDPR) Articles 5(1)(c) and 5(1)(f) require that personal data be limited to what is necessary and protected through appropriate technical measures against unauthorised reconstruction. This paper addresses both requirements through a Fisher information density (FID)-constrained trajectory sharing scheme for robot collision avoidance, where sensing estimates are perturbed according to local information content before sharing. Experiments on real pedestrian traces show that FID-controlled sharing achieves a strictly better privacy-utility tradeoff than fixed-error perturbation: at matched missed-conflict rates, reconstruction leakage and sustained exposure lengths are consistently lower, establishing information-aware perturbation as a principled technical measure aligned with GDPR data minimisation and integrity requirements.

</details>

---

### [[20_Research/Papers/具身智能/Strouhal-Aware_Model_Predictive_Control_for_Efficient_Multi-Fin_Flapping_Locomotion|Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion]]

![[assets/2607.03216_figure.png|800]]

- **arXiv**: [2607.03216](https://arxiv.org/abs/2607.03216)
- **PDF**: https://arxiv.org/pdf/2607.03216
- **详细分析**: [[20_Research/Papers/具身智能/Strouhal-Aware_Model_Predictive_Control_for_Efficient_Multi-Fin_Flapping_Locomotion|Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion]]
- **作者**: Yuya Hamamatsu, Zixi Chen, Maarja Kruusmaa, Asko Ristolainen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 1.5，机器人 0.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Strouhal-Aware Model Predictive Control for Efficient Multi-Fin Flapping Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient flapping propulsion hinges on operating within a narrow Strouhal number window, a principle nature has converged upon for maximum thrust-to-power ratio. We translate this bioinspired empirical rule into real-time control, demonstrating it on an autonomous underwater vehicle driven by four soft fins. The proposed Strouhal-aware Model Predictive Control (MPC) enhances a quasi-steady hydrodynamic model with an explicit penalty for Strouhal deviation, solving the resulting nonconvex problem via a two-stage sampling and gradient optimization that runs onboard at 25 Hz. Pool and field trials show that the controller keeps each fin within the optimal Strouhal corridor (0.25-0.35) while precisely tracking commanded forces. This results in a mean reduction in mechanical power of 8.8\% to 32\% throughout the cruising range of 0.1 to 0.3 m/s. The proposed method also allows for a velocity of 0.4 m/s, which is unattainable for a baseline of the conventional inverse model. The results confirm that embedding first-principle flow physics into an MPC objective yields tangible endurance gains without sacrificing agility, offering a generic pathway to energy-aware locomotion in next-generation multifin robots.

</details>

---

### [[20_Research/Papers/具身智能/Exp2VLA_Enabling_Vision-Language-Action_for_Drone_Navigation_from_Expert_Demonstrations|Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations]]

![[assets/2607.03146_figure.png|800]]

- **arXiv**: [2607.03146](https://arxiv.org/abs/2607.03146)
- **PDF**: https://arxiv.org/pdf/2607.03146
- **详细分析**: [[20_Research/Papers/具身智能/Exp2VLA_Enabling_Vision-Language-Action_for_Drone_Navigation_from_Expert_Demonstrations|Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations]]
- **作者**: Van Huyen Dang, Kabilesh Rajendran, Erdi Sayar, Erdal Kayacan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Exp2VLA: Enabling Vision-Language-Action for Drone Navigation from Expert Demonstrations》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Exp2VLA, MobileVLA, OpenVLA, RaceVLA, SmolVLA, UPB-RAT-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models open a new path toward intuitive robot control by directly linking perception, language, and action in a single end-to-end framework. Yet for UAVs, practical adoption remains difficult because existing solutions are either computationally heavy or insufficiently capable in complex environments. In this work, we propose a practical expert-distillation pipeline (Exp2VLA) for language-conditioned drone navigation. The core idea is to distill expert behavior, obtained from reinforcement learning, teleoperation, or other controllers, into training data that can be used to fine-tune compact VLA models. This allows existing control strategies to be transferred into a unified language-guided navigation model, reducing manual system integration and lowering the barrier for deploying new robot behaviors. Experiments in both sim-to-sim and simulation-in-the-loop settings across multi-object scenes show that the fine-tuned models can handle varied semantic commands and generalize to unseen target compositions. The proposed framework demonstrates how expert-policy distillation can help mechatronic systems move from specialized control modules toward more flexible and reusable robot intelligence.

</details>

---

### [[20_Research/Papers/机器人/LOTUSim_Multi-Domain_Simulator_for_Marine_Robotics|LOTUSim: Multi-Domain Simulator for Marine Robotics]]

![[assets/2607.03072_figure.png|800]]

- **arXiv**: [2607.03072](https://arxiv.org/abs/2607.03072)
- **PDF**: https://arxiv.org/pdf/2607.03072
- **详细分析**: [[20_Research/Papers/机器人/LOTUSim_Multi-Domain_Simulator_for_Marine_Robotics|LOTUSim: Multi-Domain Simulator for Marine Robotics]]
- **作者**: Cédric Buche, Juliette Grosset, Hélène Lechêne, Marie Dubromel, Pierig Havez-Bodivit, Malcom Neo, Julien Prodhon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《LOTUSim: Multi-Domain Simulator for Marine Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim, IRL, LOTUSim, LRAUVSim, MarineGym, OceanSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simulation is essential for maritime robotics, supporting operator training, mission rehearsal, and human-vehicle interaction in environments where real-world testing is costly or hazardous. Existing simulators focus primarily on autonomy systems and often lack human-in-the-loop interaction and realistic environmental physics. This paper introduces LOTUSim, an open-source, real-time maritime simulator supporting multi-user interaction across aerial, surface, and underwater robotic systems for coordinated naval-style operations. The first contribution of this work is enabling real-time interactive performance for users while ensuring scalability to large fleets operating within a shared interactive simulation environment. Validation demonstrates robust human-in-the-loop performance, maintaining strict real-time execution and high visual fidelity while scaling to large heterogeneous maritime drone swarms. The second contribution is a computationally efficient, Ekman-inspired layered, underwater current model that captures wind-driven, depth-dependent flow dynamics with sufficient physical fidelity for large-scale simulations. Validation against ocean reanalysis data demonstrates substantially improved accuracy compared to commonly used stochastic Gauss-Markov current models. These results confirm LOTUSim's suitability as a simulation platform for operatorin-the-loop maritime robotics research.

</details>

---

### [[20_Research/Papers/机器人/DRBA_Dynamic_Robotic_Balance_Assistant_--_An_assist-as-needed_gait_and_balance_rehabilitation_robot_for_versatile_training|DRBA: Dynamic Robotic Balance Assistant -- An assist-as-needed gait and balance rehabilitation robot for versatile training]]

![[assets/2607.03027_figure.png|800]]

- **arXiv**: [2607.03027](https://arxiv.org/abs/2607.03027)
- **PDF**: https://arxiv.org/pdf/2607.03027
- **详细分析**: [[20_Research/Papers/机器人/DRBA_Dynamic_Robotic_Balance_Assistant_--_An_assist-as-needed_gait_and_balance_rehabilitation_robot_for_versatile_training|DRBA: Dynamic Robotic Balance Assistant -- An assist-as-needed gait and balance rehabilitation robot for versatile training]]
- **作者**: Yifan Wang, Li Li, Youlong Wang, Chengyuan Yang, Sherwin Stephen Chan, Jiaye Chen, Xiaoyue Yan, Hao Wang, Xuesheng Gong, Jun Lin, Hongping Hu, Wei Tech Ang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《DRBA: Dynamic Robotic Balance Assistant -- An assist-as-needed gait and balance rehabilitation robot for versatile training》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The decline of human balance control due to aging and pathological conditions increases fall risk, a major concern in geriatric care and rehabilitation. Gait training is essential for balance recovery, enhancing walking ability and postural control. However, existing overground robotic gait trainers have limitations: body weight support systems are bulky and impractical for daily use, while end-effector-based systems often compromise transparency, altering natural gait dynamics. This paper presents the Dynamic Robotic Balance Assistant (DRBA), a novel gait trainer providing assist-as-needed body weight and balance support for various training scenarios. DRBA integrates a 3-degree-of-freedom (3-DoF) robotic arm for pelvic support with flexible motion, a compact sit-to-stand assistance module, and user-following and fall detection algorithms to ensure minimal interference and responsive support. Experimental results demonstrated high transparency, with minimal impact on natural gait dynamics. A patient trial with nine elderly patients with varying medical conditions and balance impairments (ranging from severe to mild) further validated DRBA's effectiveness. The results showed that DRBA-assisted training increased step length and walking speed compared to therapist-assisted gait training. Additionally, DRBA enabled users to perform tasks beyond their unaided ability, expanding rehabilitation possibilities. These findings highlight DRBA's potential to enhance rehabilitation outcomes by facilitating higher training intensity and enabling task-oriented exercises.

</details>

---

### [[20_Research/Papers/机器人/Beyond_Heuristics_A_Standardized_Real2Sim_Pipeline_for_Physical_Human_Robot_Interaction_in_Human-in-the-Loop_Simulation|Beyond Heuristics: A Standardized Real2Sim Pipeline for Physical Human Robot Interaction in Human-in-the-Loop Simulation]]

![[assets/2607.03017_figure.png|800]]

- **arXiv**: [2607.03017](https://arxiv.org/abs/2607.03017)
- **PDF**: https://arxiv.org/pdf/2607.03017
- **详细分析**: [[20_Research/Papers/机器人/Beyond_Heuristics_A_Standardized_Real2Sim_Pipeline_for_Physical_Human_Robot_Interaction_in_Human-in-the-Loop_Simulation|Beyond Heuristics: A Standardized Real2Sim Pipeline for Physical Human Robot Interaction in Human-in-the-Loop Simulation]]
- **作者**: Chengyuan Yang, Yifan Wang, Chun Kwang Tan, Sherwin Stephen Chan, Youlong Wang, Xiaoyue Yan, Lei Li, Wei Tech Ang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Beyond Heuristics: A Standardized Real2Sim Pipeline for Physical Human Robot Interaction in Human-in-the-Loop Simulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The aging global population drives demand for assistive robots, yet the safety risks and costs of physical testing make Human-in-the-Loop (HITL) simulation an attractive alternative. Its fidelity for coupled systems, however, is limited by interaction models whose impedance parameters are tuned heuristically rather than identified from data. We present a Real2Sim pipeline that identifies the coupled Physical Human-Robot Interaction (pHRI) dynamics of a pelvis--strap interface on an overground mobile balance assistant. The interface is modeled as a 6-DoF viscoelastic mechanism whose 12 directional stiffness and damping parameters are identified per subject via Covariance Matrix Adaptation Evolution Strategy (CMA-ES), using the user's ``Safe \&amp; Comfortable'' feedback as a reproducible operating point that resolves harness-tightness ambiguity across anthropometrics. An intraclass-correlation analysis over a five-subject cohort separates shareable from subject-specific parameters, yielding a set of prior parameters derived from the existing data. Deploying this prior configures a previously unseen subject by refining only 5 of the 12 parameters. The calibrated model then reproduces the real interaction envelope and induces biomechanically accurate gait adaptations in the Human Digital Twin (HDT). Overly compliant and overly stiff settings, by contrast, fail as extreme settings, confirming a correct operating point that no heuristic tuning procedure can reliably select. The pipeline thus improves HITL simulation fidelity and supports the Human Digital Twin as a predictive tool for pre-clinical verification of personalized controllers.

</details>

---

### [[20_Research/Papers/机器人/Function-Space_Diffusion_for_Motion_Planning|Function-Space Diffusion for Motion Planning]]

![[assets/2607.02977_figure.png|800]]

- **arXiv**: [2607.02977](https://arxiv.org/abs/2607.02977)
- **PDF**: https://arxiv.org/pdf/2607.02977
- **详细分析**: [[20_Research/Papers/机器人/Function-Space_Diffusion_for_Motion_Planning|Function-Space Diffusion for Motion Planning]]
- **作者**: Zinuo Chang, Yipu Chen, Byoungwoo Park, Hongzhe Yu, Yongxin Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Function-Space Diffusion for Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion-based motion planners have demonstrated strong performance in generating diverse and high-quality robot trajectories in cluttered environments with multiple feasible solutions. However, existing approaches typically operate on fixed-length waypoint sequences, making the learned model resolution-dependent, thereby preventing zero-shot generalization across resolutions. In this work, we propose Function-Space Diffusion for Motion Planning (FSD-MP), a diffusion-based motion planner that models trajectories as continuous functions and performs diffusion directly in function space, achieving discretization-invariant trajectory generation. We define a mode-wise forward process in the spectral domain, driven by Gaussian noise with a Matérn-type covariance, and parameterize the reverse process with a boundary-compatible Discrete Sine Transform-based Fourier Neural Operator (DST-FNO) that preserves start-goal constraints across resolutions. We evaluate FSD-MP on 2D point robot and 7-DoF Franka manipulator planning benchmarks. Our method achieves competitive planning performance at the training resolution and generalizes zero-shot across resolutions up to 16$\times$ higher, preserving consistent planning behavior without retraining. These results demonstrate that function-space diffusion provides an effective framework for discretization-invariant motion planning.

</details>

---

### [[20_Research/Papers/机器人/Continuous-Time_Gaussian_Belief_Trees_for_Motion_Planning|Continuous-Time Gaussian Belief Trees for Motion Planning]]

![[assets/2607.02884_figure.png|800]]

- **arXiv**: [2607.02884](https://arxiv.org/abs/2607.02884)
- **PDF**: https://arxiv.org/pdf/2607.02884
- **详细分析**: [[20_Research/Papers/机器人/Continuous-Time_Gaussian_Belief_Trees_for_Motion_Planning|Continuous-Time Gaussian Belief Trees for Motion Planning]]
- **作者**: Rayan Mazouz, Qi Heng Ho, Zachary N. Sunberg, Morteza Lahijanian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Continuous-Time Gaussian Belief Trees for Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We address sampling-based motion planning for continuous-time stochastic systems under process and measurement uncertainty, with probabilistic guarantees on safety and performance. The robot dynamics are modeled as a continuous-time linear stochastic differential equation, while sensor measurements arrive at discrete time instants. We derive an offline hybrid belief propagation model in which the belief evolves according to continuous-time ODEs between measurements and undergoes discrete Kalman filter update jumps at measurement times. To ensure safety, we introduce a belief-barrier-function-based safety checker for segment-level probabilistic verification. This enables the planner to certify safety over entire continuous trajectory segments and detect inter-sample chance-constraint violations that are missed by conventional node-based checks. Together, these components provide a principled framework for sampling-based belief planning that accounts for both continuous-time uncertainty propagation and continuous-time safety requirements. We integrate the method with RRT and SST planners and evaluate it across multiple benchmark environments. The results show that the proposed method achieves high success rates and robust enforcement of chance constraints, including in narrow-passage scenarios where discrete-time counterparts fail due to missed inter-sample unsafe behavior.

</details>

---

### [[20_Research/Papers/具身智能/DREAMSTEER_Latent_World_Models_Can_Steer_VLA_Policies_During_Deployment_Without_Any_Finetuning|DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning]]

![[assets/2607.02865_figure.png|800]]

- **arXiv**: [2607.02865](https://arxiv.org/abs/2607.02865)
- **PDF**: https://arxiv.org/pdf/2607.02865
- **详细分析**: [[20_Research/Papers/具身智能/DREAMSTEER_Latent_World_Models_Can_Steer_VLA_Policies_During_Deployment_Without_Any_Finetuning|DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning]]
- **作者**: Hanchen Cui, Sergio Arnaud, Arjun Majumdar, Daniel Dugas, Elie Aljalbout, Karthik Desingh, Krishna Murthy Jatavallabhula, Franziska Meier
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，世界模型 0.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《DREAMSTEER: Latent World Models Can Steer VLA Policies During Deployment Without Any Finetuning》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained vision-language-action (VLA) policies show promising zero-shot generalization, but often fail under deployment-time distribution shift, leading to decreased robustness and inconsistent instruction following. While prior work commonly tackles this by finetuning on in-distribution data, it assumes demonstrations collected on tasks in the target environment. In this work, we propose DREAMSTEER, a deployment-time steering framework for pretrained VLAs without any finetuning or parameter modifications. The key insight in DREAMSTEER is to leverage a latent world model and a value model to steer pretrained VLA policies. During deployment, DREAMSTEER samples candidate action chunks from a VLA policy and predefined motion primitives, imagines their outcomes using an action-conditioned latent world model, and ranks the imagined trajectories with a language-conditioned value model. Across four real-world manipulation benchmarks with unseen objects, DREAMSTEER improves task success rate from 23.75% to 66.25% and instruction-following accuracy from 38.75% to 56.25% over the base VLA policy.

</details>

---

### [[20_Research/Papers/具身智能/TACO_TActile_World_Model_as_a_Self-COrrector_forScalable_VLA_Post-Training|TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training]]

![[assets/2607.02840_figure.png|800]]

- **arXiv**: [2607.02840](https://arxiv.org/abs/2607.02840)
- **PDF**: https://arxiv.org/pdf/2607.02840
- **详细分析**: [[20_Research/Papers/具身智能/TACO_TActile_World_Model_as_a_Self-COrrector_forScalable_VLA_Post-Training|TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training]]
- **作者**: Shengbang Liu, Yueru Jia, Yuyang Yan, Jiaming Liu, Xinran Zhang, Qiuxuan Feng, Yandong Guo, Shiji Zhou, Boxin Shi, Shanghang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.1，世界模型 1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TACO: TActile World Model as a Self-COrrector forScalable VLA Post-Training》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown promising generalization in robotic manipulation, but they still struggle with contact-rich tasks, where minor contact perturbations can cause unrecoverable failures that are hard to detect from vision alone. Since these failures are localized rather than task-level semantic errors, tactile-aware corrective post-training offers an efficient way to improve recovery. However, scaling such supervision through human intervention is costly. Recent works have explored world models to synthesize imagined rollouts for policy improvement, but vision-only world models may produce visually plausible yet contact-inconsistent trajectories. We therefore introduce TACO, a tactile-aware world-model-driven framework for scalable VLA post-training in contact-rich manipulation. Given real robot rollouts, TACO follows a Recognize-Imagine-Label loop with a tactile-aware world model: a unified progress-action model recognizes failure-adjacent states using progress estimates, a visuo-tactile generation model imagines local correction segments, and the progress-action model labels them with executable corrective actions. To incorporate tactile corrective supervision into VLA post-training, TACO combines knowledge-insulated tactile adaptation with advantage-conditioned training, enabling the policy to learn from imagined corrections without degrading pretrained visual-language priors. These components enable TACO to convert real-world failures into imagined visuo-tactile corrections for iterative VLA post-training. Experiments on real-world contact-rich manipulation tasks show that TACO achieves 44% absolute success rate improvement over the base policy and 32% over the policy without knowledge-insulated tactile adaptation.

</details>

---

### [[20_Research/Papers/具身智能/GigaWorld-1_A_Roadmap_to_Build_World_Models_for_Robot_Policy_Evaluation|GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation]]

![[assets/2607.02642_figure.png|800]]

- **arXiv**: [2607.02642](https://arxiv.org/abs/2607.02642)
- **PDF**: https://arxiv.org/pdf/2607.02642
- **详细分析**: [[20_Research/Papers/具身智能/GigaWorld-1_A_Roadmap_to_Build_World_Models_for_Robot_Policy_Evaluation|GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation]]
- **作者**: GigaWorld Team, Angyuan Ma, Boyuan Wang, Bohan Li, Chaojun Ni, Guo Li, Guan Huang, Guosheng Zhao, Hao Li, Hengtao Li, Jingyu Liu, Jiwen Lu...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.9（加权：具身智能 0.6，世界模型 1，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《GigaWorld-1: A Roadmap to Build World Models for Robot Policy Evaluation》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GigaWorld, OpenVLA, WMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Evaluating embodied robot foundation models remains a critical bottleneck; unlike large language models efficiently assessed via digital benchmarks, robotic policies require slow, costly real-world rollouts limited by hardware and human supervision, which has driven interest in world models as surrogate policy evaluators, yet the key properties that make a world model reliable for policy assessment remain poorly understood. This work presents a systematic study of world models for robotic policy evaluation and introduces WMBench, a benchmark constructed from real-robot teleoperation data and matched policy rollouts covering diverse manipulation tasks to enable controlled comparisons across model families, action encodings, rollout horizons, and evaluation metrics. Using WMBench, we analyze 7 video world models, 4 action representation schemes, and over 324,000 simulated policy rollouts paired with real robot executions, further enriching our analysis with large-scale community submissions from the CVPR 2026 GigaBrain Challenge, curated synthetic trajectories, and a training videos spanning more than 12,000 hours. Our experiments deliver three core insights: evaluator quality is dominated by long-horizon, action-faithful rollout consistency rather than short-term visual realism; pretraining gains stem not only from data scale but from balancing general world knowledge with robot-specific controllability; and architectural choices including action encoding, memory design, and evaluator-focused post-training strongly determine alignment with real-world robot behavior. Drawing on these results, we derive a practical design roadmap and realize it in \textit{GigaWorld-1}, a world model specially optimized for policy evaluation, and we fully release our code, models, datasets, and toolkits to advance scalable evaluation research for embodied foundation models.

</details>

---
