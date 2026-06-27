# cs.RO | Robotics | 2026-06-25

#arxiv #ComputerScience

**论文数**: 37

### [[20_Research/Papers/具身智能/ForceBand_Learning_Forceful_Manipulation_with_sEMG|ForceBand: Learning Forceful Manipulation with sEMG]]

![[assets/2606.26093_figure.png|800]]

- **arXiv**: [2606.26093](https://arxiv.org/abs/2606.26093)
- **PDF**: https://arxiv.org/pdf/2606.26093
- **详细分析**: [[20_Research/Papers/具身智能/ForceBand_Learning_Forceful_Manipulation_with_sEMG|ForceBand: Learning Forceful Manipulation with sEMG]]
- **作者**: Botao He, Zhi Wang, Linna Kuang, Ishaan Ghosh, Jitendra Malik, Cornelia Fermuller, Tingfan Wu, Jiayuan Mao, Ruoshi Liu, Haozhi Qi, Yiannis Aloimonos
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《ForceBand: Learning Forceful Manipulation with sEMG》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human demonstrations are a scalable data source for learning robot manipulation policies. However, common sources of human demonstration data, such as motion-capture trajectories and internet videos, capture mostly motion and appearance while missing the contact forces that are critical for force-sensitive manipulation. In this paper, we introduce ForceBand, a low-cost wrist-worn sEMG system that turns human muscle activity into force-enriched demonstrations. We first collect a 10-hour multimodal dataset containing egocentric video, sEMG, IMU, and fingertip force measurements across diverse actions and objects. Using this dataset, we pre-train an EMG2Force model that predicts per-finger forces from sEMG and IMU signals. After a short user-specific calibration, users can collect target-task demonstrations using only ForceBand and video; EMG2Force then labels these demonstrations with per-finger force traces, producing force-augmented demonstrations for robot policy learning. Experiments show that ForceBand recovers fine-grained fingertip interactions with over 50% lower force prediction error than vision-based baselines and achieves an 87% success rate on pick, squeeze, and place tasks that require object-specific force control across objects with diverse shapes, sizes, and weights. Project website: https://forceband-emg.github.io

</details>

---

### [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning-Enhanced_Event-Triggered_Data-Driven_Predictive_Control_for_a_3D_Cable-Driven_Soft_Robotic_Arm|Deep Reinforcement Learning-Enhanced Event-Triggered Data-Driven Predictive Control for a 3D Cable-Driven Soft Robotic Arm]]

![[assets/2606.26048_figure.png|800]]

- **arXiv**: [2606.26048](https://arxiv.org/abs/2606.26048)
- **PDF**: https://arxiv.org/pdf/2606.26048
- **详细分析**: [[20_Research/Papers/强化学习/Deep_Reinforcement_Learning-Enhanced_Event-Triggered_Data-Driven_Predictive_Control_for_a_3D_Cable-Driven_Soft_Robotic_Arm|Deep Reinforcement Learning-Enhanced Event-Triggered Data-Driven Predictive Control for a 3D Cable-Driven Soft Robotic Arm]]
- **作者**: Cheng Ouyang, Moeen Ul Islam, Kaixiang Zhang, Zhaojian Li, Xiaobo Tan, Dong Chen
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 2.6（加权：具身智能 0.3，强化学习 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Deep Reinforcement Learning-Enhanced Event-Triggered Data-Driven Predictive Control for a 3D Cable-Driven Soft Robotic Arm》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft robots are challenging to control due to their nonlinear and time-varying dynamics. Data-enabled predictive control (DeePC) offers a model-free alternative by directly leveraging measured input-output trajectories to construct a predictive controller. However, its receding-horizon formulation requires solving a constrained optimization problem at every sampling instant, which can be computationally demanding for real-time deployment on resource-limited robotic platforms.To address this limitation, we propose an adaptive reinforcement-learning-based event-triggered DeePC (RL-ET-DeePC) framework for soft robotic control. A model-free RL policy is trained to determine when to invoke the DeePC optimizer based on the current system state representation, thereby reducing unnecessary optimization calls while preserving closed-loop performance.Simulation results show that RL-ET-DeePC reduces optimization frequency by up to 66% compared to periodic DeePC, while maintaining comparable tracking accuracy. Hardware experiments on a three-dimensional cable-driven soft robotic arm demonstrate zero-shot transfer, achieving a 34% reduction in optimization frequency with tracking accuracy comparable to periodic DeePC and more consistent performance than a static threshold-based event-triggered baseline.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Robot_Visual_Navigation_in_Crowds_via_Intention-Aware_Scene_Representations|Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations]]

![[assets/2606.26047_figure.png|800]]

- **arXiv**: [2606.26047](https://arxiv.org/abs/2606.26047)
- **PDF**: https://arxiv.org/pdf/2606.26047
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Robot_Visual_Navigation_in_Crowds_via_Intention-Aware_Scene_Representations|Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations]]
- **作者**: Han Bao, Bingyi Xia, Hanjing Ye, Yu Zhan, Hao Cheng, Baozhi Jia, Wenjun Xu, Jiankun Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.4，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Robot Visual Navigation in Crowds via Intention-Aware Scene Representations》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, Real-World, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot crowd navigation requires the ability to infer human intentions while accounting for the structural constraints of the environment. Currently, deep reinforcement learning (DRL) provides a promising method for learning navigation policies that understand human intentions. However, most of them rely on limited scene representations, treating pedestrians as simple 2D points and ignoring rich visual cues from both humans and the environment. To address this issue, we introduce iCrowdNav, a novel visual crowd navigation method with intention-aware scene representations, to encode behavioral and structural context from egocentric visual observations. Our method employs two key components: a spatio-temporal encoder for extracting occupancy features of the scene, and Intent-Interact Former (I$^2$ Former), an attention-based module that encodes human poses to infer pedestrians' motion intentions. These features are integrated into a compact state embedding that supports effective DRL policy training. Extensive experiments show that our method achieves superior performance over baselines, and real-world deployment demonstrates vision-based crowd navigation.

</details>

---

### [[20_Research/Papers/机器人/G2DP_Diffusion_Planning_with_Spatio-Temporal_Grid_Guidance|G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance]]

![[assets/2606.26017_figure.png|800]]

- **arXiv**: [2606.26017](https://arxiv.org/abs/2606.26017)
- **PDF**: https://arxiv.org/pdf/2606.26017
- **详细分析**: [[20_Research/Papers/机器人/G2DP_Diffusion_Planning_with_Spatio-Temporal_Grid_Guidance|G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance]]
- **作者**: Hang Yu, Ye Jin, Alessandro Canevaro, Julian Schmidt, Julian Jordan, Peizheng Li, Marc Kaufeld, Silvan Lindner, Johannes Betz, Wilhelm Stork
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《G2DP: Diffusion Planning with Spatio-Temporal Grid Guidance》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Dauner2023CORL, PredictionNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In autonomous driving, diffusion-based planners have emerged as a promising paradigm for robust motion planning in dense and interactive traffic, as they can effectively model diverse driving behaviors. However, their inherent stochasticity often requires explicit guidance during denoising to ensure safety and route adherence for robust closed-loop execution. Existing guidance typically relies on sparse, entity-centric geometric queries or post-hoc refinement, yielding limited situational awareness and fragile performance in interactive scenes. To address this issue, we propose G2DP (Grid-Guided Diffusion Planning), a diffusion-based planner that directly enforces dense environmental constraints through inference-time guidance. Specifically, G2DP constructs a differentiable spatio-temporal cost volume by fusing probabilistic future occupancy distributions with a route-progress map. By formulating this volume as a continuous safety energy functional, it injects dense gradients directly into the denoising loop, actively steering trajectory generation toward collision-free and progress-optimal regions. Extensive closed-loop evaluations show that G2DP achieves state-of-the-art performance on nuPlan, outperforming the strongest imitation-learning baseline by +7.2 points in reactive score. It further maintains top scores in zero-shot transfers to interPlan and DeepScenario benchmarks, with collision avoidance improving by +10.15 over the unguided approach on interPlan. These results demonstrate that spatio-temporal cost grids serve as an effective representation for robust guidance in diffusion-based planning.

</details>

---

### [[20_Research/Papers/机器人/FAR-LIO_Enabling_High-Speed_Autonomy_through_Fast,_Accurate,_and_Robust_LiDAR-Inertial_Odometry|FAR-LIO: Enabling High-Speed Autonomy through Fast, Accurate, and Robust LiDAR-Inertial Odometry]]

![[assets/2606.26010_first_page.png|800]]

- **arXiv**: [2606.26010](https://arxiv.org/abs/2606.26010)
- **PDF**: https://arxiv.org/pdf/2606.26010
- **详细分析**: [[20_Research/Papers/机器人/FAR-LIO_Enabling_High-Speed_Autonomy_through_Fast,_Accurate,_and_Robust_LiDAR-Inertial_Odometry|FAR-LIO: Enabling High-Speed Autonomy through Fast, Accurate, and Robust LiDAR-Inertial Odometry]]
- **作者**: Maximilian Leitenstern, Marcel Weinmann, Patrick Haft, Tobias Lasser, Dominik Kulmer, Markus Lienkamp
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《FAR-LIO: Enabling High-Speed Autonomy through Fast, Accurate, and Robust LiDAR-Inertial Odometry》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust and accurate odometry estimation is essential in modern robotics. In environments characterized by highly dynamic motion and sensor noise, odometry estimation becomes increasingly challenging. Autonomous racing combines both factors in an unstructured setting, where minimizing odometry latency is essential for stable closed-loop control. This paper introduces FAR-LIO, a highly optimized CUDA-accelerated LiDAR-inertial odometry framework developed for Fast, Accurate, and Robust performance. Our system leverages a novel CUDA-based voxel hashmap to enable parallelized nearest-neighbor search and efficient map updates. We employ a sparsity-aware Generalized Iterative Closest Point algorithm with adaptive thresholding on top of the CUDA-based voxel hashmap with adaptive density to achieve low-latency without compromising accuracy. An Extended Kalman Filter serves as a robust backend. It utilizes an upsampling and delay compensation strategy to fuse the LiDAR odometry with high-frequency IMU data, thereby ensuring a robust and smooth odometry output. We evaluate FAR-LIO across four different sensor setups, using both public datasets and data from two autonomous racecars driving at speeds of up to 250 km/h. FAR-LIO achieves an average 6.9% reduction in the positional error and 38.4% lower runtime compared to state-of-the-art baselines on target hardware using a single parameter set. This demonstrates its computational efficiency and broad applicability. To build upon our work, our code is available open-source on https://github.com/TUMFTM/FAR-LIO.

</details>

---

### [[20_Research/Papers/具身智能/Emcar_Embodied_Controller_for_Animating_Robots|Emcar: Embodied Controller for Animating Robots]]

![[assets/2606.26008_figure.jpg|800]]

- **arXiv**: [2606.26008](https://arxiv.org/abs/2606.26008)
- **PDF**: https://arxiv.org/pdf/2606.26008
- **详细分析**: [[20_Research/Papers/具身智能/Emcar_Embodied_Controller_for_Animating_Robots|Emcar: Embodied Controller for Animating Robots]]
- **作者**: Carlos Gomez Cubero, Elizabeth Jochum
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Emcar: Embodied Controller for Animating Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This chapter describes EMCAR, a novel software tool for programming robot motion that leverages the unique affordances of artistic practices such as puppetry and drawing to conceive, design, and program novel interactions and realize new use cases for HRI. The advantage of this no-code platform is that it expands creative applications for collaborative robots - putting robots directly in the hands of artists - and provides an inclusive environment that enables individuals with little or no technical backgrounds to engage meaningfully in collaborations and robotics research.

</details>

---

### [[20_Research/Papers/具身智能/Action_ControlNet_A_Lightweight_Delay-Aware_Adapter_for_Smooth_Asynchronous_Control_in_Vision-Language-Action_Models|Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models]]

![[assets/2606.25985_figure.png|800]]

- **arXiv**: [2606.25985](https://arxiv.org/abs/2606.25985)
- **PDF**: https://arxiv.org/pdf/2606.25985
- **详细分析**: [[20_Research/Papers/具身智能/Action_ControlNet_A_Lightweight_Delay-Aware_Adapter_for_Smooth_Asynchronous_Control_in_Vision-Language-Action_Models|Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models]]
- **作者**: Tiecheng Guo, Meng Guo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Action ControlNet: A Lightweight Delay-Aware Adapter for Smooth Asynchronous Control in Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ACNet, ControlNet, Meta-World, OpenVLA, Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have shown strong potential for general-purpose robot manipulation, but their inference latency remains a major obstacle to stable high-frequency control. Asynchronous execution mitigates this bottleneck by overlapping policy inference with action execution, yet the next action chunk is still predicted from stale observations while the robot continues to move. Direct chunk stitching therefore introduces handoff discontinuities, action jitter, and failures in contact-rich manipulation. Existing remedies typically require either full-policy retraining or architecture-specific runtime logic. This work proposes Action ControlNet (ACNet), a lightweight delay-aware adapter that uses the executed motion suffix as a residual condition for a mostly frozen action head. ACNet leaves the pretrained backbone unchanged, introduces few trainable parameters, and remains compatible with generative action heads such as diffusion and flow matching. On Kinetix, Meta-World MT50, and a real-world SO-ARM101 platform, ACNet improves robustness under inference delay and yields smoother asynchronous trajectories than direct chunk stitching, while remaining more lightweight than full delay-conditioned retraining.

</details>

---

### [[20_Research/Papers/具身智能/Mixture-of-Experts_RL_for_Fault-Tolerant_Legged_Locomotion|Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion]]

![[assets/2606.25965_figure.png|800]]

- **arXiv**: [2606.25965](https://arxiv.org/abs/2606.25965)
- **PDF**: https://arxiv.org/pdf/2606.25965
- **详细分析**: [[20_Research/Papers/具身智能/Mixture-of-Experts_RL_for_Fault-Tolerant_Legged_Locomotion|Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion]]
- **作者**: Giulio Turrisi, Ozan Pali, Luca Oneto, Claudio Semini
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Mixture-of-Experts RL for Fault-Tolerant Legged Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots deployed in planetary exploration and other remote environments must maintain reliable locomotion despite actuator failures and challenging terrain conditions. Although reinforcement learning has achieved strong results in legged locomotion, monolithic policies can struggle to efficiently represent the diverse control strategies required to compensate for different fault conditions. In this work, we propose a fault-aware modular control architecture that explicitly leverages fault-diagnosis information to activate specialized control experts associated with distinct actuator failure modes. Experimental results show that explicit fault-conditioned modular policies consistently outperform monolithic policies of comparable size, achieving higher locomotion performance across failure scenarios. Moreover, the proposed modular architecture retains competitive performance even under significantly reduced network capacity, highlighting its suitability for compute-constrained robotic platforms, such as those typically employed in space applications. The code associated with this work is available at: https://github.com/iit-DLSLab/fault-locomotion-isaaclab.

</details>

---

### [[20_Research/Papers/机器人/From_Rubble_Simulation_to_Active_Magnetic_Mapping_Quantum_Sensing_for_Disaster_Response|From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response]]

![[assets/2606.25957_figure.png|800]]

- **arXiv**: [2606.25957](https://arxiv.org/abs/2606.25957)
- **PDF**: https://arxiv.org/pdf/2606.25957
- **详细分析**: [[20_Research/Papers/机器人/From_Rubble_Simulation_to_Active_Magnetic_Mapping_Quantum_Sensing_for_Disaster_Response|From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response]]
- **作者**: Samuel Tovey, Stefan Prestel, Hiroshi Yamauchi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《From Rubble Simulation to Active Magnetic Mapping: Quantum Sensing for Disaster Response》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Locating survivors of building collapses within the first 72 hours is a critical challenge in disaster response, and existing sensing modalities provide only partial information about the structure beneath the rubble. This paper proposes drone-based quantum magnetometry as a complementary modality and develops a simulation pipeline spanning rubble physics, sensor-array deployment, and active spatial reconstruction. We use Unreal Engine to generate a steel-reinforced concrete parking-garage collapse and compute the induced magnetic field via a per-triangle dipole approximation, establishing that meaningful magnetic structure is recoverable in the sub-pT to sub-nT range from roughly 1 m above the roofline. Then, we feed sparse multi-sensor samples into a Gaussian Process Regression back-end driven by Bayesian active sampling and validate the pipeline across multiple independent collapse realizations; a three-sensor array optimizes the trade-off between gradient resolution and UAV payload constraints, and active sampling reaches peak structural correlation in roughly $100$ samples. Together, these results indicate that quantum-grade sensing could become a useful tool for drone-based structural analysis and potentially void detection in collapsed buildings.

</details>

---

### [[20_Research/Papers/大模型/MIL-LC_A_Robust_Magnetometer-Inertial-LiDAR_Fusion_Multimodal_Localization_Framework|MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework]]

![[assets/2606.25796_figure.jpg|800]]

- **arXiv**: [2606.25796](https://arxiv.org/abs/2606.25796)
- **PDF**: https://arxiv.org/pdf/2606.25796
- **详细分析**: [[20_Research/Papers/大模型/MIL-LC_A_Robust_Magnetometer-Inertial-LiDAR_Fusion_Multimodal_Localization_Framework|MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework]]
- **作者**: Qiyang Lyu, Zhenyu Wu, Wei Wang, Hongming Shen, Danwei Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《MIL-LC: A Robust Magnetometer-Inertial-LiDAR Fusion Multimodal Localization Framework》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Localization in challenging environments, such as GNSS-denied, geometrically repetitive, or textureless scenes commonly found in offices, hotels, and underground parking facilities, remains an open problem for reliable autonomous mobile robot (AMR) deployment. Single-modality localization methods are inherently limited by the constraints of individual sensors. Although multimodal fusion frameworks have shown improved robustness, most existing approaches still rely heavily on geometric or texture features, or on infrastructure-based beacons, which increase installation and maintenance costs while reducing deployment flexibility. Recently, ambient magnetic field (AMF)-based localization has attracted growing attention because it does not depend on geometric or texture features, nor does it require additional infrastructure, making it a promising complementary modality for AMR localization. However, existing studies have only explored such fusion in pedestrian scenarios using smartphone-mounted sensor suites, and practical solutions for AMR systems remain largely unexplored. To address this gap, this article proposes a magnetometer-inertial-LiDAR fused multimodal localization framework with a custom-designed sensor suite, termed MIL-LC, which provides reliable localization even when LiDAR suffers from geometric degeneration or when the magnetic map changes during long-term deployment. Extensive experiments in both simulation and real-world environments demonstrate that the proposed MIL-LC framework achieves robust and accurate localization performance.

</details>

---

### [[20_Research/Papers/具身智能/StairMaster_Learning_to_Conquer_Risky_Hollow_Stairs_for_Agile_Quadrupedal_Robots|StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots]]

![[assets/2606.25765_figure.png|800]]

- **arXiv**: [2606.25765](https://arxiv.org/abs/2606.25765)
- **PDF**: https://arxiv.org/pdf/2606.25765
- **详细分析**: [[20_Research/Papers/具身智能/StairMaster_Learning_to_Conquer_Risky_Hollow_Stairs_for_Agile_Quadrupedal_Robots|StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots]]
- **作者**: Xincheng Tang, Youhan Xie, Zhengjie Shu, Wanyu Li, Lai Jiang, Wenkang Hu, Yitong Li, Ruigang Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.1（加权：具身智能 1.2，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《StairMaster: Learning to Conquer Risky Hollow Stairs for Agile Quadrupedal Robots》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Climbing hollow stairs remains a challenging problem for quadruped robots due to the high risk of leg trapping, severe depth sparsity, and high-frequency depth-sensing noise. In this paper, we propose StairMaster, a novel three-stage reinforcement learning framework for stable locomotion on such extreme discontinuous terrains. Our architecture integrates a Cross-Attention mechanism to extract structural features from noisy depth data, alongside a Spatial-aware Recurrent Unit (SRU) that maintains robust spatio-temporal memory to mitigate perception blind spots. To bridge the sim-to-real gap in depth perception, we propose a high-fidelity sim-to-real depth sensor modeling pipeline that faithfully replicates real-world sensor artifacts. Additionally, we employ a 3D waypoint-guided active perception reward for proactive sensing, alongside hollow gap kinematic and stair edge penalties to ensure precise foothold placement. We successfully deployed StairMaster on a Unitree Go2 robot, demonstrating its ability to conquer hollow stairs with an unprecedented incline of up to 55$^\circ$ through zero-shot transfer. To the best of our knowledge, this is the first RL-based policy to achieve such steep hollow stair climbing in real-world environments. Project Website: https://sivan666666.github.io/StairMaster/.

</details>

---

### [[20_Research/Papers/大模型/Stage-Aware_and_Roughness-Constrained_Diffusion_Policy_for_Multi-Stage_Robotic_Polishing|Stage-Aware and Roughness-Constrained Diffusion Policy for Multi-Stage Robotic Polishing]]

![[assets/2606.25754_figure.png|800]]

- **arXiv**: [2606.25754](https://arxiv.org/abs/2606.25754)
- **PDF**: https://arxiv.org/pdf/2606.25754
- **详细分析**: [[20_Research/Papers/大模型/Stage-Aware_and_Roughness-Constrained_Diffusion_Policy_for_Multi-Stage_Robotic_Polishing|Stage-Aware and Roughness-Constrained Diffusion Policy for Multi-Stage Robotic Polishing]]
- **作者**: Shuai Ke, Jiexin Zhang, Huan Zhao, Zhiao Wei, Yikun Guo, Tiange Wu, Guoqiang Guo, Haoyuan Zhou, Jie Pan, Han Ding
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Stage-Aware and Roughness-Constrained Diffusion Policy for Multi-Stage Robotic Polishing》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Polishing is a critical finishing process in high-end manufacturing fields such as aerospace, where surface quality directly affects the service performance and reliability of components. Robotic imitation learning provides a flexible solution for such tasks, but current methods remain limited in industrial polishing because of long-horizon dependencies, uncertain stage transitions, and the difficulty of modeling and regulating coupled process parameters. To address these issues, this paper proposes a Stage-Aware and Roughness-Constrained Diffusion Policy (SRDP) for robotic polishing. SRDP infers the process-stage posterior from multimodal observation histories and uses it to condition the shared reverse denoising process, enabling stage-consistent action generation without external stage labels during execution. Furthermore, a roughness-oriented process-constrained diffusion sampling method is incorporated to generate constrained feed speed and normal contact force under stage-wise preset spindle speeds, thereby improving process consistency and physical feasibility. Systematic experiments are conducted on two representative scenarios, namely spacecraft cabin coating-surface polishing and inner-cavity structural surface finishing. Comparisons with advanced baselines, ablation studies, and real-robot validations comprehensively evaluate the proposed method. The results show that SRD improves stage-transition stability, process-parameter consistency, and final surface quality across different polishing scenarios.

</details>

---

### [[20_Research/Papers/强化学习/Learning_Asynchronous_Upper-body_Task-space_Trajectory_Tracking_Policy_for_Humanoid_Robots|Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots]]

![[assets/2606.25706_figure.png|800]]

- **arXiv**: [2606.25706](https://arxiv.org/abs/2606.25706)
- **PDF**: https://arxiv.org/pdf/2606.25706
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Asynchronous_Upper-body_Task-space_Trajectory_Tracking_Policy_for_Humanoid_Robots|Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots]]
- **作者**: Yumeng Liu, Dongqi Wang, Jiyu Yu, Yijun Fan, Rong Xiong, Yue Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Learning Asynchronous Upper-body Task-space Trajectory Tracking Policy for Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

High-level humanoid planners often output sparse task-space, low-rate trajectories, whereas whole-body controllers run at high frequency. This creates temporal asynchrony between the planning and execution, and structural incompleteness for full-body control. We propose an asynchronous upper body task-space tracking framework for humanoids. A student policy is initialized by teacher-student distillation, conditioned on the full cached future trajectory and an execution-time index, and trained with a sliding-window global reward to reduce frame drift without explicit frame estimation. For task-specific post-training, an MPC module completes sparse references into floating-base and upper-body guidance, while action- and FK level self-guidance constrain policy drift. Simulation and Unitree G1 hardware experiments show improved tracking under low update rates, stronger performance than synchronous and decoupled baselines, and safer adaptation to out-of-distribution motions.

</details>

---

### [[20_Research/Papers/具身智能/Event-Adaptive_Motion_Planning_with_Distilled_Vision-Language_Model_in_Safety-Critical_Situations|Event-Adaptive Motion Planning with Distilled Vision-Language Model in Safety-Critical Situations]]

![[assets/2606.25629_figure.png|800]]

- **arXiv**: [2606.25629](https://arxiv.org/abs/2606.25629)
- **PDF**: https://arxiv.org/pdf/2606.25629
- **详细分析**: [[20_Research/Papers/具身智能/Event-Adaptive_Motion_Planning_with_Distilled_Vision-Language_Model_in_Safety-Critical_Situations|Event-Adaptive Motion Planning with Distilled Vision-Language Model in Safety-Critical Situations]]
- **作者**: Zhenwei Huang, Changsheng You, Shuai Wang, Chao Zhou, Wei Xu, Yi Gong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.6，大模型 0.8，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Event-Adaptive Motion Planning with Distilled Vision-Language Model in Safety-Critical Situations》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot navigation in safety-critical scenarios faces significant challenges from unforeseen semantic events, where collisions arise primarily from the unpredictable behaviors of dynamic agents rather than unseen objects. While large vision-language models (VLMs) offer remarkable capabilities in commonsense reasoning, frequently invoking them within the continuous control loop introduces severe computational latency, fundamentally destabilizing physical execution. To address these challenges, we propose event-adaptive motion planning (EAMP), an efficient framework for VLM-based robot navigation. Specifically, a prompt-configurable semantic event trigger (PC-SET) selectively activates semantic intervention by continuously monitoring short temporal clips for behavioral anomalies. Upon triggering, an event-triggered distilled SemNav-VLM, fine-tuned via physically verified semantic distillation, maps detected anomalies into discrete strategy-level decisions. Subsequently, a semantic model predictive control (SMPC) module translates these strategies into dynamic reconfigurations of optimization objectives and geometric references. Extensive experiments in safety-critical logistics scenarios demonstrate that EAMP effectively aligns high-level reasoning with low-level control, significantly improving dynamic safety margins over existing baselines while preserving real-time efficiency.

</details>

---

### [[20_Research/Papers/具身智能/WOLF-VLA_Whole-Body_Humanoid_Optimal_Locomotion_Framework_for_Vision-Language-Action_Learning|WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning]]

![[assets/2606.25591_figure.png|800]]

- **arXiv**: [2606.25591](https://arxiv.org/abs/2606.25591)
- **PDF**: https://arxiv.org/pdf/2606.25591
- **详细分析**: [[20_Research/Papers/具身智能/WOLF-VLA_Whole-Body_Humanoid_Optimal_Locomotion_Framework_for_Vision-Language-Action_Learning|WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning]]
- **作者**: Melya Boukheddimi, Omar Adjali, Daniel Sontag, Frank Kirchner
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 6.7（加权：具身智能 5.4，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《WOLF-VLA: Whole-Body Humanoid Optimal Locomotion Framework for Vision-Language-Action Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HumanoidBench, Mimicking-Bench, OpenVLA, SmolVLA, WOLF-VLA, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have recently demonstrated strong generalization in robotic manipulation, yet their applicability to whole-body, contact-rich humanoid locomotion remains severely underexplored due to data scarcity, the absence of dynamically consistent demonstrations, and the difficulty of encoding optimality and safety in learning-based pipelines. This work introduces a unified framework WOLF-VLA that integrates whole-body optimal-control (OC) motion synthesis with large-scale multi-modal dataset to train VLAs capable of generating humanoid locomotion policies directly from natural-language instructions. We construct a comprehensive dataset of dynamically feasible humanoid trajectories across six locomotion-related task families, each parameterized by environmental variations, object colors, placements, and visual distractors. We train a VLA model using the collected joint trajectories, ego-centric visual observations and natural language instruction, yielding a policy that exhibits strong reasoning and robustness to initial-condition variability, and competitive performance across several tasks and environment settings. A systematic ablation study demonstrates the impact of each modality on the model performance. The full dataset, model checkpoints, and benchmarking simulation suite will be openly released, establishing a reproducible dynamically consistent benchmark for whole-body humanoid locomotion rich VLA control and enabling future research in scalable transfer of instruction-driven locomotion policies.

</details>

---

### [[20_Research/Papers/具身智能/One_Body,_Two_Minds_Variable_Autonomy_Approach_for_a_Co-embodied_Robotic_Hand|One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand]]

![[assets/2606.25575_figure.png|800]]

- **arXiv**: [2606.25575](https://arxiv.org/abs/2606.25575)
- **PDF**: https://arxiv.org/pdf/2606.25575
- **详细分析**: [[20_Research/Papers/具身智能/One_Body,_Two_Minds_Variable_Autonomy_Approach_for_a_Co-embodied_Robotic_Hand|One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand]]
- **作者**: Piotr Koczy, Yuchong Zhang, Danica Kragic, Michael C. Welle
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.3（加权：具身智能 1.8，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《One Body, Two Minds: Variable Autonomy Approach for a Co-embodied Robotic Hand》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assistive robotic systems face a fundamental trade-off: fully autonomous systems lack user agency, while fully user-controlled systems demand continuous cognitive effort. Existing shared autonomy approaches blend human and robot commands but are mostly deployed in separate physical bodies. We introduce co-embodiment with variable autonomy, where human and robot share a single physical body and operate at different autonomy levels across task phases, from mutual autonomy during object search and grasping to human-dominant control during actuation. We present a co-embodied, wearable robotic hand that has its own ``mind'' and operates with variable autonomy levels. A learning-from-demonstration visuomotor diffusion policy enables autonomous grasping when the user positions the hand near known objects. Once grasped, the system signals completion and the human can actuate the grasped tool (drill, spray bottle, infrared thermometer, lighter, and ice-cream scoop) via hands-free head gestures. The human retains veto authority at all times through a release gesture that returns the system to the initial phase. Unlike blended autonomy, where control is continuously negotiated, our co-embodied approach consists of variable autonomy from full human control to full independent actions while maintaining physical coupling, realizing a one body, two minds paradigm. In a user study with 44 participants performing five bimanual tasks, users rapidly adapted to this ``two minds'' paradigm: completion times improved by 23.3% across trials ($p &lt; 0.001$, Cohen's $d = 0.94$), the best-performing policy variant reached a 93.6% task success rate, and acceptance ratings were high (5.70/7 overall impression, 5.52/7 daily use willingness). This work establishes co-embodiment with variable autonomy as a viable approach for assistive robotics, enabling human-robot collaboration through co-embodiment.

</details>

---

### [[20_Research/Papers/具身智能/GROVE_Grounded_Pedestrian_Simulation_via_Natural_Language_for_Interactive_Social_Robot_Navigation|GROVE: Grounded Pedestrian Simulation via Natural Language for Interactive Social Robot Navigation]]

![[assets/2606.25504_figure.png|800]]

- **arXiv**: [2606.25504](https://arxiv.org/abs/2606.25504)
- **PDF**: https://arxiv.org/pdf/2606.25504
- **详细分析**: [[20_Research/Papers/具身智能/GROVE_Grounded_Pedestrian_Simulation_via_Natural_Language_for_Interactive_Social_Robot_Navigation|GROVE: Grounded Pedestrian Simulation via Natural Language for Interactive Social Robot Navigation]]
- **作者**: Duc Tai Nguyen, Volodymyr Shcherbyna, Anh Do Duc, Zhengcheng Shen, Teham Buiyan, Linh Kästner
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《GROVE: Grounded Pedestrian Simulation via Natural Language for Interactive Social Robot Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HuNavSim, SocNavBench, SocialGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pedestrian simulation is a critical component for training and deploying social robot navigation approaches, yet it remains a largely rigid system that repeatedly requires manual data generation to define even simple scenarios. We propose GROVE, a text-to-scenario pedestrian simulation framework that combines state-of-the-art approaches to produce realistic, socially challenging scenarios for social robot navigation. Our framework allows users to customize one of several common presets (emergency, queuing, normal) or even enter a fully independent prompt to generate a highly customizable pedestrian simulation. Multiple modules separately ensure the realism and soundness of long-horizon human behavior, medium-horizon pedestrian navigation, and short-horizon robot/social interactions. Each module is tuned by the prompt in a way that reflects the user intent across all aspects of pedestrian simulation. By dynamically selecting one of several state-of-the-art (SotA) approaches in our modules based on the scenario, we capture many situational nuances of pedestrian behavior in order to narrow the simulation-to-real (sim2real) gap. The human simulation is directly integrated into Isaac Sim, Gazebo, and RViz simulators for robot deployment in highly social environments. We validate our approach through qualitative comparison against existing pedestrian simulation baselines across scenarios of varying complexity in residential, hospital, and office environments. The result is a high-fidelity pedestrian simulation that challenges social robot navigation with complex, diverse, realistic human behaviors.

</details>

---

### [[20_Research/Papers/具身智能/SAGE-Nav_Leveraging_LLM_Planning_and_Alignment_Fusion_for_Hierarchical_Scene_Graph-Guided_Navigation|SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation]]

![[assets/2606.25497_first_page.png|800]]

- **arXiv**: [2606.25497](https://arxiv.org/abs/2606.25497)
- **PDF**: https://arxiv.org/pdf/2606.25497
- **详细分析**: [[20_Research/Papers/具身智能/SAGE-Nav_Leveraging_LLM_Planning_and_Alignment_Fusion_for_Hierarchical_Scene_Graph-Guided_Navigation|SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation]]
- **作者**: Hao Su, Yuehao Huang, Yukai Ma, Yong Liu, Jiajun Lv
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《SAGE-Nav: Leveraging LLM Planning and Alignment Fusion for Hierarchical Scene Graph-Guided Navigation》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object-Goal Navigation (ObjNav) requires embodied agents to autonomously locate specified targets using only egocentric visual observations. Existing monolithic methods struggle with long-horizon reasoning and generalize poorly to novel environments. To address these limitations, we propose SAGE-Nav, a novel hierarchical framework that integrates the reasoning capabilities of Large Language Models (LLMs) with dynamic scene graphs. Crucially, it decouples asynchronous global semantic planning from the high-frequency reactive control loop. The LLM serves as a global planner, decomposing abstract instructions into a sequence of semantically grounded waypoints. To translate these plans into dense multi-modal guidance, we design a Hierarchical Scene Graph Encoder (HSGE) that leverages relational graph convolutions to produce structure-aware embeddings preserving both semantic and spatial topology. Furthermore, we develop the Goal-aware Alignment-Fusion Network (GAFN) to dynamically fuse real-time perception with these structural priors. Using an adaptive gating mechanism with an explicit inductive bias, GAFN ensures robust visual-topological alignment for the low-level policy. Extensive evaluations in the i-THOR and RoboTHOR environments demonstrate that SAGE-Nav achieves state-of-the-art performance, delivering substantial gains in navigation efficiency and zero-shot generalization while maintaining the low control latency required for physical robotic deployment.

</details>

---

### [[20_Research/Papers/机器人/Generative_AI_for_Safe_and_Photorealistic_Drone_Light_Shows|Generative AI for Safe and Photorealistic Drone Light Shows]]

![[assets/2606.25458_first_page.png|800]]

- **arXiv**: [2606.25458](https://arxiv.org/abs/2606.25458)
- **PDF**: https://arxiv.org/pdf/2606.25458
- **详细分析**: [[20_Research/Papers/机器人/Generative_AI_for_Safe_and_Photorealistic_Drone_Light_Shows|Generative AI for Safe and Photorealistic Drone Light Shows]]
- **作者**: Pascal Reinhold, Alexander Gräfe, Sebastian Trimpe
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Generative AI for Safe and Photorealistic Drone Light Shows》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Drone light shows are redefining aerial entertainment, yet their widespread adoption is bottlenecked by labor-intensive, manual animation. While generative AI promises an automated alternative, current frameworks fail to provide photorealism with fluid, dynamic motion. To address this limitation, we introduce SWAN, an end-to-end pipeline that synthesizes photorealistic, large-scale, and collision-free drone choreographies directly from text prompts. SWAN converts text into realistic reference videos and translates these pixel-space dynamics into physical swarm kinematics using a novel, adaptive point-tracking algorithm. Unlike existing trackers, this method maintains spatial coherence through severe occlusions and rapid topological shifts. A dedicated planner then allocates these trajectories to individual drones, while a subsequent safety filter ensures collision-free execution. We demonstrate scalability by safely orchestrating simulated 2,000-drone formations and validate physical feasibility on a dense real-world swarm of 49 quadcopters, operating everything entirely on standard consumer hardware. Combined, this work demonstrates how generative AI can be leveraged to automate multi-robot choreography design, providing an accessible new framework for drone light shows.

</details>

---

### [[20_Research/Papers/大模型/HEART_Coordination_of_Heterogeneous_Expert_Agents_for_Physically_Grounded_Robotic_Task_Planning|HEART: Coordination of Heterogeneous Expert Agents for Physically Grounded Robotic Task Planning]]

![[assets/2606.25404_figure.png|800]]

- **arXiv**: [2606.25404](https://arxiv.org/abs/2606.25404)
- **PDF**: https://arxiv.org/pdf/2606.25404
- **详细分析**: [[20_Research/Papers/大模型/HEART_Coordination_of_Heterogeneous_Expert_Agents_for_Physically_Grounded_Robotic_Task_Planning|HEART: Coordination of Heterogeneous Expert Agents for Physically Grounded Robotic Task Planning]]
- **作者**: Junho Lee, Seabin Lee, Wonjong Lee, Nayoung Kim, Moonjeong Kang, Changjoo Nam
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.3，大模型 0.5，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《HEART: Coordination of Heterogeneous Expert Agents for Physically Grounded Robotic Task Planning》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large Language Models (LLMs) can reason over complex instructions but often fail to satisfy the physical and spatial constraints required for robotic task planning. Recent LLM-based planners directly translate text into action sequences, yet they lack structured reasoning about feasibility, reachability, and logical order, resulting in invalid or incomplete plans. We present a heterogeneous multi-LLM framework that decomposes instructions into atomic reasoning tasks and allocates them to role-specialized expert agents under a token budget for real-world computational and communicational constraints. By combining role-oriented reasoning from heterogeneous agents followed by constraint-driven plan synthesis, HEART validates capability, reachability, and constraint conditions before planning and helps produce physically executable plans while maintaining efficiency. Experiments across different household benchmarks show that HEART consistently improves plan success compared to single-LLM and rule-based planners, demonstrating that heterogeneous LLM collaboration enables robust and scalable robotic task planning under resource constraints.

</details>

---

### [[20_Research/Papers/具身智能/MAPL_Multi-Objective_Preference_Learning_for_Robot_Locomotion|MAPL: Multi-Objective Preference Learning for Robot Locomotion]]

![[assets/2606.25398_figure.png|800]]

- **arXiv**: [2606.25398](https://arxiv.org/abs/2606.25398)
- **PDF**: https://arxiv.org/pdf/2606.25398
- **详细分析**: [[20_Research/Papers/具身智能/MAPL_Multi-Objective_Preference_Learning_for_Robot_Locomotion|MAPL: Multi-Objective Preference Learning for Robot Locomotion]]
- **作者**: Xiyue Chen, Muhan Lin, Shuyang Shi, Joseph Campbell
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 3.8（加权：具身智能 1.8，大模型 0.3，强化学习 0.4，机器人 1.3）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《MAPL: Multi-Objective Preference Learning for Robot Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PbRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward design remains a major bottleneck in reinforcement learning for robot locomotion, where successful policies often depend on carefully tuned, task-specific reward functions. Preference-based reinforcement learning offers an alternative, but existing LLM-based methods typically ask for a single overall judgment between behaviors, making it difficult to capture the multiple competing objectives that underlie high-quality locomotion. We present Multi-Objective AI-Informed Preference Learning (MAPL), a framework that learns locomotion rewards from high-level natural language objectives rather than manually engineered reward equations. MAPL prompts a large language model to compare trajectories independently along semantically meaningful criteria, using generic language descriptions that are terrain-invariant and require little domain expertise. These objective-wise preferences are used to train a multi-head preference scoring model, whose outputs are aggregated to form a scalar reward for policy optimization. Across four quadruped locomotion environments, MAPL trains policies using only LLM-generated preferences and achieves performance comparable to or better than expert-designed rewards, while eliminating task-specific reward engineering.

</details>

---

### [[20_Research/Papers/机器人/Large-Scale_Tunnel_Air--Ground_Collaboration_With_FLISP_Fast_LiDAR-IMU_Synchronized_Path_Planne|Large-Scale Tunnel Air--Ground Collaboration With FLISP: Fast LiDAR-IMU Synchronized Path Planne]]

![[assets/2606.25393_figure.png|800]]

- **arXiv**: [2606.25393](https://arxiv.org/abs/2606.25393)
- **PDF**: https://arxiv.org/pdf/2606.25393
- **详细分析**: [[20_Research/Papers/机器人/Large-Scale_Tunnel_Air--Ground_Collaboration_With_FLISP_Fast_LiDAR-IMU_Synchronized_Path_Planne|Large-Scale Tunnel Air--Ground Collaboration With FLISP: Fast LiDAR-IMU Synchronized Path Planne]]
- **作者**: Fenghe Guo, Runjie Shen, Chenyang Sun, Junrui Zhang, Quanxi Zhan, Yongchun Wang, Junjie Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Large-Scale Tunnel Air--Ground Collaboration With FLISP: Fast LiDAR-IMU Synchronized Path Planne》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hydropower tunnel inspection is critical for infrastructure integrity yet remains inefficient and hazardous using manual methods. We propose FLISP (Fast LiDAR-IMU Synchronized Path Planner), a mapless planning framework for cooperative UGV-UAV inspection. Unlike traditional map-based paradigms, FLISP features three core contributions: (1) a unified architecture where a single UGV-mounted LiDAR-IMU suite drives synchronized path generation for both platforms; (2) platform-specific solvers utilizing an enhanced Firefly Algorithm for UGV obstacle avoidance and a dynamic iterative optimizer for UAV flight; and (3) a hierarchical refinement strategy ensuring kinematic feasibility without state estimation drift. Benchmarks in a 1.2 km operational tunnel demonstrate that FLISP circumvents structural bottlenecks of map-based methods, eliminating map rasterization overhead (Fast-LIO2 + A*) and sampling instability (LIO-SAM + RRT*). FLISP achieves a 100% success rate with ~7 ms latency, representing a 7-fold speedup over grid-based and three-order-of-magnitude improvement over sampling-based baselines. Validated in operational hydropower tunnels, this approach offers a scalable solution for robotic inspection in feature-degraded linear infrastructure. A demonstration video is available at https://youtu.be/Y_ezs1PfLJ4, and the code at https://github.com/ArchibaldGuo/FLISP.git.

</details>

---

### [[20_Research/Papers/机器人/Commerge_Communication-Efficient,_Robust,_and_Fast_LiDAR_Map_Merging_Framework_for_Multi-Robot_Coordination_in_Resource-Constrained_Scenario|Commerge: Communication-Efficient, Robust, and Fast LiDAR Map Merging Framework for Multi-Robot Coordination in Resource-Constrained Scenarios]]

![[assets/2606.25386_first_page.png|800]]

- **arXiv**: [2606.25386](https://arxiv.org/abs/2606.25386)
- **PDF**: https://arxiv.org/pdf/2606.25386
- **详细分析**: [[20_Research/Papers/机器人/Commerge_Communication-Efficient,_Robust,_and_Fast_LiDAR_Map_Merging_Framework_for_Multi-Robot_Coordination_in_Resource-Constrained_Scenario|Commerge: Communication-Efficient, Robust, and Fast LiDAR Map Merging Framework for Multi-Robot Coordination in Resource-Constrained Scenarios]]
- **作者**: Hogyun Kim, Jiwon Choi, Juwon Kim, Geonmo Yang, Seokhwan Jeong, Hyungtae Lim, Younggun Cho
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Commerge: Communication-Efficient, Robust, and Fast LiDAR Map Merging Framework for Multi-Robot Coordination in Resource-Constrained Scenarios》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

By maintaining global consistency across robot teams, multi-robot LiDAR map merging enables faster exploration and efficient area coverage. However, map merging requires exchanging massive sensor data between the server and robots, making communication the bottleneck, especially in communication-constrained environments. Therefore, we present Commerge, a communication-efficient map merging framework that achieves bandwidth reduction through graph-theoretic selective data exchange. By doing so, our Commerge reduces inter-robot communication by up to 5,000x while maintaining alignment accuracy. Our key insight is that only a small subset of carefully selected scans is sufficient for robust map merging. We formulate this as a three-stage cascaded optimization problem on an exchange graph, where vertices represent robot keyframes and edges denote candidate inter-robot loops. Through three cascade stages, we select a sequentially overlapped, balanced-transmission-cost, and geometrically-perceptually optimal scan subset that preserves alignment quality while reducing communication. Unlike existing approaches that either transmit whole scans, which require GB-scale data exchange, or employ naive downsampling, our approach exchanges only MB-scale data while achieving comparable alignment accuracy. Extensive evaluation on five public datasets and four in-house datasets covering cave, planetary-analog, indoor, and outdoor campus environments shows up to 99.98% reduction in data exchange (e.g., from 7,000MB to 1.3MB on the HeLiPR dataset), while maintaining alignment performance across embedded to desktop platforms. The supplementary materials are available at https://sparolab.github.io/research/commerge.

</details>

---

### [[20_Research/Papers/具身智能/Decoupling_Semantics_and_Geometric_Grounding_Spatial_Visual_Prompts_for_Language-Conditioned_Imitation_Learning|Decoupling Semantics and Geometric Grounding: Spatial Visual Prompts for Language-Conditioned Imitation Learning]]

![[assets/2606.25360_figure.png|800]]

- **arXiv**: [2606.25360](https://arxiv.org/abs/2606.25360)
- **PDF**: https://arxiv.org/pdf/2606.25360
- **详细分析**: [[20_Research/Papers/具身智能/Decoupling_Semantics_and_Geometric_Grounding_Spatial_Visual_Prompts_for_Language-Conditioned_Imitation_Learning|Decoupling Semantics and Geometric Grounding: Spatial Visual Prompts for Language-Conditioned Imitation Learning]]
- **作者**: Yanzhe Tang, Xinyu Shao, Yuxuan Hu, Siyu Chen, Bowen Yang, Yajun Gao, Tongtong Cao, Xiu Li, Long Zeng
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Decoupling Semantics and Geometric Grounding: Spatial Visual Prompts for Language-Conditioned Imitation Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While end-to-end Vision-Language-Action (VLA) models show promise in robotic manipulation, their monolithic paradigm inherently couples semantic reasoning and spatial control. This creates a severe alignment bottleneck, limiting precise target disambiguation in data-constrained imitation learning. To overcome this, we propose SVP-IL, a decoupled architecture that explicitly extracts spatial visual grounding from the action generation loop. By leveraging vision-language foundation models, we parse instructions into zero-shot geometric masks, translating language into explicit Spatial Visual Prompts (SVP). These priors are injected into a continuous action generator via a lightweight direct feature-level fusion mechanism. This integration provides explicit and uncorrupted spatial gradient guidance while ensuring highly stable optimization under low-data regimes. Extensive experiments demonstrate that SVP-IL significantly outperforms state-of-the-art VLAs and pure visuomotor baselines. Trained on as few as 50 to 100 demonstrations, SVP-IL improves average success rates on highly ambiguous language-conditioned tasks from 24.0% to 39.5%, achieving 67.8% on standard benchmarks. Real-world robotic experiments further validate its robustness and data efficiency in unstructured physical environments.

</details>

---

### [[20_Research/Papers/机器人/Self_Capacitive_Tactile_Sensor_System_designed_for_Companion_Robots|Self Capacitive Tactile Sensor System designed for Companion Robots]]

![[assets/2606.25348_figure.png|800]]

- **arXiv**: [2606.25348](https://arxiv.org/abs/2606.25348)
- **PDF**: https://arxiv.org/pdf/2606.25348
- **详细分析**: [[20_Research/Papers/机器人/Self_Capacitive_Tactile_Sensor_System_designed_for_Companion_Robots|Self Capacitive Tactile Sensor System designed for Companion Robots]]
- **作者**: Mohsin Ali, Hidenobu Sumioka, Shuhei Ikemoto
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Self Capacitive Tactile Sensor System designed for Companion Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing is essential for humanoid robots to achieve safe physical interaction, dexterous manipulation, and truly human-like responsiveness. However, the design of such systems remains challenging. Conventional approaches often suffer from complex multilayer structures, intricate wiring, high cost, and poor scalability, making it difficult to realize full-body tactile sensing with real-time, low-latency detection while maintaining minimal computational load on the robot's main processor. In this work, we present a simple, scalable and hardware friendly tactile sensing system for a companion humanoid robot based on the self-capacitance principle. The proposed sensor system employs a single conductive fabric layer with a conductive fabric wire architecture and does not require intricate electrode patterning. Scalability was demonstrated by fabricating a 100-point sensor array on a flexible printed circuit (FPC). Evaluation across sampling frequencies showed that 10 Hz is insufficient and misses transient events, whereas 100 Hz and 1000 Hz reliably capture and clearly distinguish all interaction types: gentle touch, slow tapping, fast tapping, and hitting. A decision-tree classifier was implemented directly on the FPGA, offloading real-time inference from the Raspberry Pi 4 with minimal latency and negligible power overhead. This design fully meets the tactile sensing requirements of the HIRO-chan robot and is well-suited for full-body tactile sensing in HIRO-chan and other companion robots.

</details>

---

### [[20_Research/Papers/强化学习/WaveForward_An_Omnidirectional_Passive_Wheeled_Quadruped_Robot_with_Casters|WaveForward: An Omnidirectional Passive Wheeled Quadruped Robot with Casters]]

![[assets/2606.25299_first_page.png|800]]

- **arXiv**: [2606.25299](https://arxiv.org/abs/2606.25299)
- **PDF**: https://arxiv.org/pdf/2606.25299
- **详细分析**: [[20_Research/Papers/强化学习/WaveForward_An_Omnidirectional_Passive_Wheeled_Quadruped_Robot_with_Casters|WaveForward: An Omnidirectional Passive Wheeled Quadruped Robot with Casters]]
- **作者**: Chuanlin Zhao, Qifeng Zheng, Shuhan Wang, Tiancheng Ma, Weixian Lin, Xin Luo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 3.6（加权：具身智能 1.5，强化学习 0.2，机器人 1.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《WaveForward: An Omnidirectional Passive Wheeled Quadruped Robot with Casters》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wheeled-legged robots possess both agile mobility for traversing complex terrains and high efficiency, making them suitable for long-distance transportation applications. Conventional actuated wheeled robots require specialized hardware and electrical design due to the incorporation of wheel components. We propose a novel and low-cost passive wheeled legged robot equipped with standard casters on each leg to obtain omnidirectional mobility. The control method employs an asymmetric actor-critic structure, enabling the utilization of the privileged information of the passive caster's angles and velocities. We develop a caster base posture adjustment strategy based on velocity commands, utilizing actuated joints to modify the caster base joint axis posture and thereby adjust the propulsion direction of the casters. Moreover, we implemented multiple propulsion modes to achieve varying degrees of caster twisting oscillation, converting these into propulsive force. We conducted a slalom test and mode switch experience, which shows the passive wheeled quadruped could achieve omnidirectional movement versatility, and reduce the cost of transport (COT) by up to 89.1% with respect to legged motion.

</details>

---

### [[20_Research/Papers/具身智能/DynaMOMA_Instantaneous_Prediction_of_Grasp_Poses_for_Mobile_Manipulation_of_Dynamic_Objects|DynaMOMA: Instantaneous Prediction of Grasp Poses for Mobile Manipulation of Dynamic Objects]]

![[assets/2606.25295_figure.png|800]]

- **arXiv**: [2606.25295](https://arxiv.org/abs/2606.25295)
- **PDF**: https://arxiv.org/pdf/2606.25295
- **详细分析**: [[20_Research/Papers/具身智能/DynaMOMA_Instantaneous_Prediction_of_Grasp_Poses_for_Mobile_Manipulation_of_Dynamic_Objects|DynaMOMA: Instantaneous Prediction of Grasp Poses for Mobile Manipulation of Dynamic Objects]]
- **作者**: Zhinan Yu, Junyan Xu, Jiazhao Zhang, Zheng Qin, Yijie Tang, Yuhang Huang, Yihan Cao, Zhiyuan Yu, Yongjun Wang, Renjiao Yi, Chenyang Zhu, Kai Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《DynaMOMA: Instantaneous Prediction of Grasp Poses for Mobile Manipulation of Dynamic Objects》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GraspNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile manipulation is a fundamental robotics task and has advanced rapidly in recent years, enabling robots to navigate, reach, and interact with objects in complex environments. However, mobile manipulation of dynamic objects remains highly challenging, as robots must coordinate the mobile base and arm while adapting to continuously evolving target poses. A key challenge lies in predicting temporally consistent short-horizon grasp trajectories from dynamic observations. In this work, we propose \ours{}, a dynamic mobile manipulation framework that couples instantaneous grasp trajectory prediction with whole-body control policy. Our predictor uses an anchor-based diffusion model to generate temporally consistent short-horizon grasp trajectories conditioned on historical observations. The predicted trajectories are then encoded as compact features and fed to a whole-body reinforcement learning policy, which controls the mobile manipulator for dynamic grasping. We further introduce a anticipation-guided reward that equips the policy with an anticipatory grasping horizon by adaptively shifting the target from the current grasp observation to the instantaneously predicted grasp trajectory. Through extensive experiments in Isaac Gym simulation, we show that our method achieves strong performance in mobile manipulation of dynamic objects across diverse settings and grasping metrics. Furthermore, our predictor and policy demonstrate strong generalizability in real-world experiments.

</details>

---

### [[20_Research/Papers/具身智能/GRAFT_Graph-Based_Affordance_Transfer_via_Part_Correspondence|GRAFT: Graph-Based Affordance Transfer via Part Correspondence]]

![[assets/2606.25241_figure.png|800]]

- **arXiv**: [2606.25241](https://arxiv.org/abs/2606.25241)
- **PDF**: https://arxiv.org/pdf/2606.25241
- **详细分析**: [[20_Research/Papers/具身智能/GRAFT_Graph-Based_Affordance_Transfer_via_Part_Correspondence|GRAFT: Graph-Based Affordance Transfer via Part Correspondence]]
- **作者**: Mengying Lin, Utkarsh Mishra, Ajay Mandlekar, Danfei Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《GRAFT: Graph-Based Affordance Transfer via Part Correspondence》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalizing robotic manipulation to unseen objects remains challenging, as learning-based approaches require many demonstrations and fail in few-shot settings. Prior work transfers affordances through semantic retrieval, but semantics alone neglect geometric similarity, which is critical for manipulation. We propose GRAFT, a geometry-aware correspondence framework for zero-shot manipulation transfer using only one demonstration per object. Objects are represented as part-based graphs, where part-level descriptors support global instance retrieval and part correspondence, and vertex-level descriptors enable fine-grained contact point matching. For an unseen object, our method first retrieves the most functionally and geometrically similar instance from the demonstration buffer with aligned functional parts, and finally propagates the contact points through point-wise correspondence.

</details>

---

### [[20_Research/Papers/具身智能/RigPI_Dynamic_Parameter_Identification_of_Rigid_Body_via_VLM-Seeded_Differentiable_Simulation|RigPI: Dynamic Parameter Identification of Rigid Body via VLM-Seeded Differentiable Simulation]]

![[assets/2606.25212_figure.png|800]]

- **arXiv**: [2606.25212](https://arxiv.org/abs/2606.25212)
- **PDF**: https://arxiv.org/pdf/2606.25212
- **详细分析**: [[20_Research/Papers/具身智能/RigPI_Dynamic_Parameter_Identification_of_Rigid_Body_via_VLM-Seeded_Differentiable_Simulation|RigPI: Dynamic Parameter Identification of Rigid Body via VLM-Seeded Differentiable Simulation]]
- **作者**: Xincheng He, Rongrong Zhang, Wei Jiang, Wenqiang Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，大模型 0.6，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《RigPI: Dynamic Parameter Identification of Rigid Body via VLM-Seeded Differentiable Simulation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PhysBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate physical parameter identification of manipulated objects is fundamental to advanced robotic manipulation and the construction of faithful digital twins. However, acquiring physically consistent inertial and frictional properties from real-world interactions remains challenging due to sensing noise, modeling errors, and limited prior knowledge. This paper presents \textbf{RigPI}, a systematic framework for identifying dynamic parameters of both unconstrained rigid bodies and multi-link rigid bodies during robot-object interaction. RigPI integrates vision-based semantic priors, force-torque measurements, and motion observations within a differentiable simulation pipeline. A vision-language model (VLM) provides informed initialization and a constrained search space, while gradient information from a differentiable physics simulator enables efficient and stable parameter refinement. The proposed two-stage optimization strategy alleviates sensitivity to noise and avoids physically implausible solutions. Extensive real-world experiments on objects with revolute and prismatic joints demonstrate that RigPI achieves accurate and stable parameter estimates, and successfully reproduces manipulation trajectories on a real robot with parameter-aware predictive validity. These results highlight the effectiveness and robustness of RigPI for real-world robotic system identification tasks.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Perceptive_Platform_Adaptive_Locomotion_Controllers_for_Quadrupedal_Robots|Learning Perceptive Platform Adaptive Locomotion Controllers for Quadrupedal Robots]]

![[assets/2606.25179_figure.png|800]]

- **arXiv**: [2606.25179](https://arxiv.org/abs/2606.25179)
- **PDF**: https://arxiv.org/pdf/2606.25179
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Perceptive_Platform_Adaptive_Locomotion_Controllers_for_Quadrupedal_Robots|Learning Perceptive Platform Adaptive Locomotion Controllers for Quadrupedal Robots]]
- **作者**: David Rytz, Kim Tien Ly, Ioannis Havoutis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.9（加权：具身智能 1.8，强化学习 0.4，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Learning Perceptive Platform Adaptive Locomotion Controllers for Quadrupedal Robots》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：RaiSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Universal quadrupedal locomotion remains limited by the difficulty of integrating perception across diverse robot morphologies. State-of-the-art controllers rely on single-robot training or blind policies that omit real-time perception, leading to poor cross-embodiment generalization. Designing locomotion policies that remain robust across related quadruped morphologies while incorporating perception is challenging. Moreover, fully perceptive policies are often sensitive to noise, whereas blind controllers lack terrain awareness. In this work, we study how perception should be integrated into morphology-aware reinforcement learning architectures for deployable quadrupedal control. Building on MorAL, we train morphology-specialized universal controllers on multiple reference quadrupeds using adaptive terrain curricula. We compare a blind baseline, a critic-perceptive variant (MorAL+), and a fully perceptive actor-critic (PPAL). Policies are evaluated in simulation on flat and rough terrains, and deployed on ANYmal hardware. Results show that critic-only perception improves robustness and tracking consistency over blind baselines while remaining more stable than fully perceptive policies under perception noise. These findings highlight that perception placement and curriculum design are key factors for scalable, morphology-aware locomotion.

</details>

---

### [[20_Research/Papers/机器人/SwarmFly_A_simulation_platform_for_UAV_swarm_experiment_design_and_validation|SwarmFly: A simulation platform for UAV swarm experiment design and validation]]

![[assets/2606.25146_figure.png|800]]

- **arXiv**: [2606.25146](https://arxiv.org/abs/2606.25146)
- **PDF**: https://arxiv.org/pdf/2606.25146
- **详细分析**: [[20_Research/Papers/机器人/SwarmFly_A_simulation_platform_for_UAV_swarm_experiment_design_and_validation|SwarmFly: A simulation platform for UAV swarm experiment design and validation]]
- **作者**: Abhishek Phadke, Karthik Kumar Vasudeva, Abhishek Joshi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《SwarmFly: A simulation platform for UAV swarm experiment design and validation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CoppeliaSim, UavNetSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The initial development phase of UAV swarms largely depends on simulation for experimental design and validation, yet existing open-source tools are often unmaintained, have steep learning curves, or are built around a single fixed scenario. The need for a comprehensive, modular simulation platform is a recognized research gap. This paper presents SwarmFly, a MATLAB-based simulation and test platform for multi- UAV swarms that addresses these gaps. SwarmFly combines a real-time operational map, four swarm coordination modes (leader-follower, decentralized, heterogeneous relay, and heterogeneous speed), simulated IMU telemetry, and IP-based geolocation with a plugin architecture that lets researchers add behaviors, fault models, and analysis tools without touching the core code. Eight bundled plugins extend the base simulator into a full test harness. The SwarmFly platform exposes multi-agent aerial swarms to a wide range of internal and external disruptions, enabling observation and quantification of underlying swarm control and behavioral mechanisms. This study verifies and characterizes each subsystem through eight experiments that measure formation accuracy, wind tolerance, fault recovery, energy endurance, and airspace compliance. The platform runs entirely in MATLAB. Its modular design supports straightforward extension toward hardware-in-the-loop testing, larger swarms, and higher-fidelity dynamics. An open-source release is available at [https://github.com/abhishekphadke/SwarmFly.git]

</details>

---

### [[20_Research/Papers/大模型/Memory_Retrieval_in_Visuomotor_Policies_for_Long-Horizon_Robot_Control|Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control]]

![[assets/2606.25136_figure.png|800]]

- **arXiv**: [2606.25136](https://arxiv.org/abs/2606.25136)
- **PDF**: https://arxiv.org/pdf/2606.25136
- **详细分析**: [[20_Research/Papers/大模型/Memory_Retrieval_in_Visuomotor_Policies_for_Long-Horizon_Robot_Control|Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control]]
- **作者**: Rutav Shah, Yisu Li, Femi Bello, Yuke Zhu, Roberto Martín-Martín
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.3，机器人 0.9）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Memory Retrieval in Visuomotor Policies for Long-Horizon Robot Control》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ReMemBench, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robots operating in partially observable environments, such as homes, require memory to support autonomy. They must recall diverse information from the past, such as where objects were placed, which tasks a human partner has completed, and when an appliance was turned on. Achieving this versatility requires a general memory retrieval mechanism. Transformer architectures that use attention over long contexts for memory retrieval provide a promising approach, as they learn retrieval from data rather than relying on task-specific or hand-designed rules. However, directly incorporating them into imitation learning from offline data introduces two key challenges: (1) the policy may learn spurious correlations between past information and predicted actions, and (2) errors accumulate in memory due to prediction inaccuracies and their compounding interactions with the environment, causing model drift and cascading failures. To address both challenges, we introduce HALO, a visuomotor policy with an attention-based memory retrieval mechanism for long-horizon control. First, to suppress spurious correlations, HALO distills vision-language model (VLM) priors into the policy. It generates memory-dependent question--answer pairs from demonstration trajectories and trains jointly with a video question--answering objective, steering retrieval toward task-relevant information. Second, to reduce the impact of accumulated errors in memory during closed-loop control, HALO uses sparse attention that restricts retrieval to only the most relevant parts of the history. Together, these components enable more reliable long-horizon control by guiding the policy to retrieve task-relevant information from up to eight minutes of past experience. Project website: https://robin-lab.cs.utexas.edu/HALO

</details>

---

### [[20_Research/Papers/强化学习/RGB_RL_Guided_Whole-Body_MPPI_for_Humanoid_Control|RGB: RL Guided Whole-Body MPPI for Humanoid Control]]

![[assets/2606.25123_figure.png|800]]

- **arXiv**: [2606.25123](https://arxiv.org/abs/2606.25123)
- **PDF**: https://arxiv.org/pdf/2606.25123
- **详细分析**: [[20_Research/Papers/强化学习/RGB_RL_Guided_Whole-Body_MPPI_for_Humanoid_Control|RGB: RL Guided Whole-Body MPPI for Humanoid Control]]
- **作者**: Yunsoo Seo, Sol Choi, Euncheol Im, Myo Taeg Lim, Yisoo Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，强化学习 0.4，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《RGB: RL Guided Whole-Body MPPI for Humanoid Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots require whole-body controllers that are both robust and precise in contact-rich environments. While deep reinforcement learning (RL) achieves robust stability, its behavior is tightly coupled to the training objective and command interface, making it difficult to add new feedback objectives without retraining. In this study, we propose an RL guided whole-body model predictive path integral (MPPI) framework that acts as an add-on feedback controller on top of a pretrained RL policy. Instead of using RL policy as the final controller, we use it as a sampling prior that biases MPPI rollouts toward dynamically feasible behaviors. Task objectives are specified through modular MPPI cost terms, and MPPI closes the loop by continuously correcting the RL prior online to satisfy these objectives without retraining the policy. Simulations on a 29-DoF Unitree G1 humanoid in MuJoCo demonstrate stable high-rate control (average 280~Hz). The proposed method improves task-level precision over a pure RL baseline under the same command interface. This is achieved by correcting systematic drift during straight walking and tracking additional whole-body reference signals imposed through the cost.

</details>

---

### [[20_Research/Papers/具身智能/SurveilNav_Collaborative_Object_Goal_Navigation_with_Robot_and_Surveillance_System|SurveilNav: Collaborative Object Goal Navigation with Robot and Surveillance System]]

![[assets/2606.25119_figure.png|800]]

- **arXiv**: [2606.25119](https://arxiv.org/abs/2606.25119)
- **PDF**: https://arxiv.org/pdf/2606.25119
- **详细分析**: [[20_Research/Papers/具身智能/SurveilNav_Collaborative_Object_Goal_Navigation_with_Robot_and_Surveillance_System|SurveilNav: Collaborative Object Goal Navigation with Robot and Surveillance System]]
- **作者**: Ming-Ming Yu, Qunbo Wang, Rongtao Xu, Yanghong Mei, Yirong Yang, Longteng Guo, Wenjun Wu, Jing Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.6，大模型 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SurveilNav: Collaborative Object Goal Navigation with Robot and Surveillance System》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Habitat-Sim, V2VNet, V2X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

With the growing deployment of surveillance systems in factories, offices, and homes, integrating them with robots offers a promising direction for collaborative and efficient task execution. However, existing approaches largely focus on single-robot scenarios and struggle with multi-view collaboration in large-scale environments. In this paper, we present a novel indoor collaborative object navigation dataset built on Habitat-Sim, featuring 206 cameras across 74 floors. The dataset enables systematic evaluation of an agent's ability to exploit multi-view surveillance information. To address the limitations of single-robot perception, we propose SurveilNav, a collaborative navigation framework that integrates active camera scheduling, joint 2D/3D mapping, VLM-based value estimation, and collaborative target verification. By synergizing the robot's dynamic local perception with the static global view of surveillance, this architecture effectively overcomes both the limited perception range of single agents and the inherent blind spots of fixed cameras, resolving inefficient exploration. Experimental results on the HM3D dataset demonstrate that SurveilNav substantially outperforms existing methods, achieving state-of-the-art performance in both exploration efficiency and navigation success rate. Moreover, the system shows strong potential for applications in large-scale search, home environments, and rescue missions.

</details>

---

### [[20_Research/Papers/机器人/Invariant_Kalman_filtering_for_extended_pose_estimation_in_multi-IMU_articulated_rigid-body_systems|Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems]]

![[assets/2606.25083_figure.png|800]]

- **arXiv**: [2606.25083](https://arxiv.org/abs/2606.25083)
- **PDF**: https://arxiv.org/pdf/2606.25083
- **详细分析**: [[20_Research/Papers/机器人/Invariant_Kalman_filtering_for_extended_pose_estimation_in_multi-IMU_articulated_rigid-body_systems|Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems]]
- **作者**: Sven Goffin, Cédric Schwartz, Silvère Bonnabel, Olivier Brüls, Pierre Sacré
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Invariant Kalman filtering for extended pose estimation in multi-IMU articulated rigid-body systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate extended pose estimation (orientation, velocity, and position) for IMU-instrumented articulated rigid-body systems is a key challenge in robotics and human motion analysis. The invariant extended Kalman filter (IEKF) addresses this problem for a single rigid body with convergence guarantees and consistency under unobservability, but extending these properties to articulated systems is nontrivial: inter-body pose coupling prevents a direct application, and incorporating joint kinematic constraints within the invariant framework remains an open problem. To address this gap, we introduce the relative L-extended pose, a Lie group representation for kinematic-tree systems. With one IMU per body, it yields group-affine dynamics and allows joint constraints to be expressed in invariant form. We incorporate these constraints as noise-free pseudo-measurements within an iterated IEKF (IterIEKF), thereby preserving the convergence and consistency guarantees of invariant filtering. Validated on both a UR5e robot and a human leg, the proposed IterIEKF outperforms all EKF, IterEKF, and absolute-pose IterIEKF baselines. It converges faster, exhibits lower run-to-run variability, and consistently achieves the lowest RMSE, with reductions of at least 50% compared to the second-best filter across all scenarios considered in this work.

</details>

---

### [[20_Research/Papers/强化学习/BFMTrack_Latent_Sequence_Optimization_for_Physics-Based_Motion_Tracking_with_Behavioral_Foundation_Models|BFMTrack: Latent Sequence Optimization for Physics-Based Motion Tracking with Behavioral Foundation Models]]

![[assets/2606.25056_figure.png|800]]

- **arXiv**: [2606.25056](https://arxiv.org/abs/2606.25056)
- **PDF**: https://arxiv.org/pdf/2606.25056
- **详细分析**: [[20_Research/Papers/强化学习/BFMTrack_Latent_Sequence_Optimization_for_Physics-Based_Motion_Tracking_with_Behavioral_Foundation_Models|BFMTrack: Latent Sequence Optimization for Physics-Based Motion Tracking with Behavioral Foundation Models]]
- **作者**: Thomas Rupf, Agon Serifi, David Müller, Sammy Christen, Ruben Grandia, Espen Knoop, Moritz Bächer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《BFMTrack: Latent Sequence Optimization for Physics-Based Motion Tracking with Behavioral Foundation Models》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavioral Foundation Models (BFMs) offer a promising path toward universal physics-based character control by organizing a rich repertoire of physically plausible behaviors into a latent space, guided by a large-scale motion dataset. While these models excel at time-invariant tasks, such as goal-reaching and state-based reward optimization, their latent space does not directly support time-varying objectives, such as tracking a motion sequence. For tracking, existing heuristics rely on moving-window-averaging that fails to capture the nuances of highly dynamic motions. In this work, we propose a novel Latent Sequence Optimization (LSO) to address these shortcomings. Our approach combines simulation rollouts with a policy gradient update to optimize over a sequence of latents, extending the capabilities of BFMs toward precise motion tracking without requiring reward engineering and tuning. To guide the optimization toward smooth, coherent latent trajectories, we model the latent sequence using temporally correlated noise. We validate our approach across dense tracking, sparse keyframing, and direct deployment onto a real humanoid robot.

</details>

---

### [[20_Research/Papers/具身智能/MANGO_Automated_Multi-Agent_Test_Oracle_Generation_for_Vision-Language-Action_Models|MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models]]

![[assets/2606.24815_figure.png|800]]

- **arXiv**: [2606.24815](https://arxiv.org/abs/2606.24815)
- **PDF**: https://arxiv.org/pdf/2606.24815
- **详细分析**: [[20_Research/Papers/具身智能/MANGO_Automated_Multi-Agent_Test_Oracle_Generation_for_Vision-Language-Action_Models|MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models]]
- **作者**: Pablo Valle, Shaukat Ali, Aitor Arrieta, Lionel Briand
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.3（加权：具身智能 2.1，大模型 0.5，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《MANGO: Automated Multi-Agent Test Oracle Generation for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models are emerging robotic control systems that integrate perception, language understanding, and action generation in a unified architecture. Existing testing approaches for VLA-enabled robots rely on manually constructed symbolic test oracles that determine task success from final environment states. These oracles are costly to construct, require domain expertise, and are often tightly coupled to specific tasks and environments, limiting scalability and reuse. Furthermore, they provide only end-state assessments of task outcomes, offering limited insight into intermediate behavior and fault localization. To address these limitations, we introduce MANGO, a multi-agent framework that automatically generates fine-grained oracles from natural-language descriptions of robotic tasks. MANGO first generates a reusable library of atomic tasks, then generates simulator-grounded oracle definitions for each atomic task, and finally produces executable fine-grained oracles by decomposing complex instructions into ordered sequences of atomic actions and corresponding oracles. The framework uses collaborative Generator, Assessor, and Judge agents that iteratively refine generated artifacts through structured feedback. We evaluate MANGO on the LIBERO_10 and RoboCasa Humanoid Tabletop benchmarks. Results show that MANGO generates executable, fine-grained oracles that detect a similar number of failures as symbolic oracles while accurately localizing them and providing richer diagnostic information. Through ablation studies, we further analyzed component contributions and the effect of initial task set, while preserving oracle quality. Overall, the results show the feasibility and effectiveness of test oracle generation for VLA-enabled robots testing.

</details>

---
