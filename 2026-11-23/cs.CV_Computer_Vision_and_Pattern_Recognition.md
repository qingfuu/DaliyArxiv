# cs.CV | Computer Vision and Pattern Recognition | 2026-11-23

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/具身智能/SOAR_Training-Free_Rank-Consistent_Rollout_Compression_for_Latent_World_Model_Planning|SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning]]

![[assets/2611.27639_figure.png|800]]

- **arXiv**: [2611.27639](https://arxiv.org/abs/2611.27639)
- **PDF**: https://arxiv.org/pdf/2611.27639
- **详细分析**: [[20_Research/Papers/具身智能/SOAR_Training-Free_Rank-Consistent_Rollout_Compression_for_Latent_World_Model_Planning|SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning]]
- **作者**: Anqi Li, Kai Liu, Linghe Kong, Yulun Zhang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SOAR: Training-Free Rank-Consistent Rollout Compression for Latent World Model Planning》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models plan by rolling out hundreds of candidate action sequences through a transformer predictor, so a single decision can take tens of seconds. Existing accelerations prune spatial tokens as in vision-language models, yet a sampling-based planner uses predicted costs only to rank candidates, so a rollout can be compressed freely as long as the ranking survives. We propose SOAR, a training-free method that adapts rollout compression to each planning decision. At every decision, SOAR probes a few candidates under several token budgets and keeps the smallest budget that preserves their ranking, so it compresses as far as the current decision allows, without task labels. A closed-loop study of more than 80,000 episodes fixes the rest of the rollout: the first step, which alone reads a real observation, stays exact, and the context frame is cached rather than recomputed. On seven navigation and manipulation tasks with frozen checkpoints, SOAR matches dense-level planning success at 2.3x speedup and retains 98% at 2.5x. Our code is available at https://github.com/starrywiki/SOAR.

</details>

---

### [[20_Research/Papers/强化学习/Sketch2TikZ_Multi-Reward_Reinforcement_Learning_for_Converting_Hand-Drawn_Sketches_to_Executable_TikZ|Sketch2TikZ: Multi-Reward Reinforcement Learning for Converting Hand-Drawn Sketches to Executable TikZ]]

![[assets/2611.27620_first_page.png|800]]

- **arXiv**: [2611.27620](https://arxiv.org/abs/2611.27620)
- **PDF**: https://arxiv.org/pdf/2611.27620
- **详细分析**: [[20_Research/Papers/强化学习/Sketch2TikZ_Multi-Reward_Reinforcement_Learning_for_Converting_Hand-Drawn_Sketches_to_Executable_TikZ|Sketch2TikZ: Multi-Reward Reinforcement Learning for Converting Hand-Drawn Sketches to Executable TikZ]]
- **作者**: Shubham Paliwal, Arushi Jain, Monika Sharma, Manasi Patwardhan
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习
- **相关性评分**: 0.8（加权：强化学习 0.8）
- **关联关键词**: Multimodal, RL, ComputerVision

#### 研究背景与动机

《Sketch2TikZ: Multi-Reward Reinforcement Learning for Converting Hand-Drawn Sketches to Executable TikZ》归入 强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CodeRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic digitization of hand-drawn sketches into editable formats is crucial for modern document workflows and LaTeX integration. Converting sketches into executable TikZ code provides a structured representation of diagrams, but remains challenging due to noisy and ambiguous inputs, which hinder reliable interpretation and limit the effectiveness of token-level supervision for ensuring global diagram validity. To address these challenges, we propose Sketch2TikZ, a reinforcement learning framework that optimizes sketch-to-code generation via a sequential multi-reward strategy, combining Code-Structure ($\mathcal{R}_{cs}$), OCR ($\mathcal{R}_{ocr}$), CleanDIFT ($\mathcal{R}_{cd}$), and Self-Similarity ($\mathcal{R}_{ss}$) rewards to enforce textual, visual and structural correctness. We evaluate Sketch2TikZ on the SkeTikZ and FlowChart-3B benchmarks using metrics including compilation success rate (CSR), image similarity, code similarity, and character similarity. Our method achieves near-perfect compilation success and improves visual and textual alignment over strong open-source baselines, while remaining competitive with proprietary GPT-based vision-language models. Extensive ablations demonstrate that curriculum-based reward scheduling is critical for reducing reward interference, stabilizing training and mitigating proxy over-optimization. Overall, our results highlight the effectiveness of reference-aware, multi-objective reinforcement learning for structured diagram generation from noisy sketches.

</details>

---

### [[20_Research/Papers/世界模型/Ego2Ego_Generative_Visual_Perspective_Taking_Across_Collaborators|Ego2Ego: Generative Visual Perspective Taking Across Collaborators]]

![[assets/2611.27459_figure.png|800]]

- **arXiv**: [2611.27459](https://arxiv.org/abs/2611.27459)
- **PDF**: https://arxiv.org/pdf/2611.27459
- **详细分析**: [[20_Research/Papers/世界模型/Ego2Ego_Generative_Visual_Perspective_Taking_Across_Collaborators|Ego2Ego: Generative Visual Perspective Taking Across Collaborators]]
- **作者**: Chuhan Jiao, John Gideon, Anshul Gupta, Guy Rosman, Andreas Bulling
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Ego2Ego: Generative Visual Perspective Taking Across Collaborators》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ME-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual perspective taking, the ability to infer what another person sees from their position, is fundamental to human collaboration. However, prior works reduced perspective taking to state estimation, geometric reconstruction, or discrete question answering, whereas existing cross-view video generation methods either inferred the target view from the input video alone or required an external camera that observes the target person. We introduce generative visual perspective taking: Given an ego person's egocentric video, a scene point cloud, and a collaborator's camera trajectory, the task is to generate the continuous egocentric video from the collaborator's perspective. This task is challenging given extreme viewpoint shifts, dynamic occlusions, and sparse visual overlap. We address these challenges with Ego2Ego -- a set of backbone-agnostic geometric modules that provide a pretrained video diffusion model with the 3D scene geometry shared by both interactants. Ego2Ego renders dense, temporally consistent scene coordinate maps into every view as a shared spatial reference, aligns cross-view tokens in 3D ray space through relative geometric attention, and recovers regions outside the ego person's current view from the ego person's visual memory. Experiments on the CoMind dataset across three video diffusion backbones show that Ego2Ego consistently improves visual quality, Level-2 scene layout accuracy, and collaborator motion, outperforming state-of-the-art cross-view video generation baselines on every backbone. By generating the collaborator's egocentric video more accurately, Ego2Ego brings visual perspective taking to human-robot collaboration, where it can help infer what a human collaborator sees and does, and can turn single-person recordings into synchronised multi-perspective videos for robot learning.

</details>

---

### [[20_Research/Papers/机器人/BladeR_Scalable,_Shape-Guided_3D_Reconstruction_of_Wind_Turbine_Blades_from_UAV_Imagery|BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery]]

![[assets/2611.27407_figure.jpg|800]]

- **arXiv**: [2611.27407](https://arxiv.org/abs/2611.27407)
- **PDF**: https://arxiv.org/pdf/2611.27407
- **详细分析**: [[20_Research/Papers/机器人/BladeR_Scalable,_Shape-Guided_3D_Reconstruction_of_Wind_Turbine_Blades_from_UAV_Imagery|BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery]]
- **作者**: Jonathan Sterckx, Michiel Vlaminck, Hiep Luong
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《BladeR: Scalable, Shape-Guided 3D Reconstruction of Wind Turbine Blades from UAV Imagery》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The structural integrity of wind turbine blades is critical for safe, efficient energy production. Accurate 3D reconstruction allows precise localization and quantification of wear and early damage detection. While drone-based inspections are standard, their high-resolution imagery poses challenges such as weak texture, lighting variability, and high computational cost. We present BladeR, a scalable pipeline for high-quality 3D reconstruction from inspection imagery. A hierarchical sparse reconstruction strategy leverages GPS/IMU data and blade shape priors to guide advanced keypoint matchers on full-resolution images. For dense reconstruction, a tiled Gaussian Splatting framework processes 45 MP images at native resolution, isolates the blade from background, and adaptively enhances detail recovery along the leading edge. Validation against commercial and open-source baselines shows significant improvements in model completeness and detail.

</details>

---

### [[20_Research/Papers/具身智能/SCAP_Stochastic_Context_for_Action_Expert_Pretraining|SCAP: Stochastic Context for Action Expert Pretraining]]

![[assets/2611.27187_figure.png|800]]

- **arXiv**: [2611.27187](https://arxiv.org/abs/2611.27187)
- **PDF**: https://arxiv.org/pdf/2611.27187
- **详细分析**: [[20_Research/Papers/具身智能/SCAP_Stochastic_Context_for_Action_Expert_Pretraining|SCAP: Stochastic Context for Action Expert Pretraining]]
- **作者**: Xiao Lin, Yaoxu Lyu, Ronghao Dang, Zhili Liu, Kaijing Ma, Yang Zhou, Dingning Liu, Runzhe Teng, Jun Cen, Shanghang Zhang, Chengju Liu, Qijun Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《SCAP: Stochastic Context for Action Expert Pretraining》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：BayesVLA, LA4VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Single-modality action-expert pretraining controls competition from visual shortcuts before vision--language--action (VLA) adaptation. Yet single-modality pretraining can impair the vision--language interactions needed for subsequent joint prediction. We construct a diagnostic model in which VA or LA pretraining can disable an initially active pathway for joint vision--language modeling. In this model, subsequent training with complete visual and language inputs cannot restore the pathway, even with unlimited adaptation. We therefore introduce Stochastic Context for Action Expert Pretraining (SCAP), a new action-expert pretraining stage that precedes full-input training. During this stage, visual and text tokens are randomly masked before entering the VLM. In this unified diagnostic model, SCAP can preserve the joint vision--language modeling pathway during pretraining and subsequent full-input training. Compared with direct full-input training, it can also reduce reliance on visual shortcuts and increase reliance on language instructions. SCAP consistently improves performance across four different VLA architectures. In real-robot experiments, it achieves 76.67% average success across three instruction-conditioned manipulation tasks, outperforming full-input pretraining by 25 percentage points.

</details>

---

### [[20_Research/Papers/具身智能/Tripwire_Robot_Agents_that_Program_Their_Own_Interrupts_under_Human_Disturbance|Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance]]

![[assets/2611.27182_figure.png|800]]

- **arXiv**: [2611.27182](https://arxiv.org/abs/2611.27182)
- **PDF**: https://arxiv.org/pdf/2611.27182
- **详细分析**: [[20_Research/Papers/具身智能/Tripwire_Robot_Agents_that_Program_Their_Own_Interrupts_under_Human_Disturbance|Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance]]
- **作者**: Sunli Chen, Yun Zong, Qinhong Zhou, Xiaowen Qiu, Jiaben Chen, Zeyuan Yang, Chuang Gan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.6（加权：具身智能 0.9，大模型 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Tripwire: Robot Agents that Program Their Own Interrupts under Human Disturbance》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agent harnesses are turn-based: the agent acts, waits for the result, then reasons. When the action invokes a pretrained robot policy, such as a vision-language-action (VLA) or world action model (WAM), the policy may react continuously to observations, but the agent cannot revisit its decision until the call returns. Meanwhile, a person may step into the robot's path or move the object it is about to grasp. Invoking the agent more often narrows this blind interval, but a reasoning model takes seconds per decision and most control steps need no new one. We propose TRIP, a training-free, event-driven harness in which the agent programs its own interrupts. With each call, the agent writes a tripwire: a lightweight, stateful Python program that runs alongside the policy, can query a compact VLM (for example, to locate a person and measure their distance), and decides whether the call continues or control returns to the agent. When it fires, the harness halts the policy and returns control with the reason; the agent then reassesses, adapts, and continues under a rewritten tripwire. We evaluate TRIP with three VLAs and one WAM on RoboHD, a benchmark of 168 RoboCasa365 scenes in which a simulated person disturbs the robot and any human-robot contact counts as failure. Compared with a turn-based harness using the same agent and tools, TRIP halves the rate of human contact with the strongest policy, raising safety from 61.3% to 81.3%, without sacrificing task success (38.7% vs. 31.0%). Real-robot experiments show that TRIP completes two manipulation tasks under human interference where the turn-based harness and the policy alone largely fail.

</details>

---

### [[20_Research/Papers/机器人/HumanoidPose_Monocular_3D_Pose_Estimation_for_Humanoid_Robots|HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots]]

![[assets/2611.27181_figure.png|800]]

- **arXiv**: [2611.27181](https://arxiv.org/abs/2611.27181)
- **PDF**: https://arxiv.org/pdf/2611.27181
- **详细分析**: [[20_Research/Papers/机器人/HumanoidPose_Monocular_3D_Pose_Estimation_for_Humanoid_Robots|HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots]]
- **作者**: Jinlin Gan, Mingzhe Li, Junsheng Zhang, Zhibo Zhou, Jiahan Geng, Yuhua Luo, Changwang Zhang, Chenglu Wen, Lan Xu, Siqi Shen, Cheng Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《HumanoidPose: Monocular 3D Pose Estimation for Humanoid Robots》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, RoboNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As humanoid robots increasingly enter real-world environments, recovering their 3D whole-body pose from monocular imagery is becoming increasingly important for external state perception, motion analysis, and robot learning. However, Humanoid Robot Pose Estimation (HRPE) lies at the intersection of conventional Robot Pose Estimation (RPE) and Human Pose Estimation (HPE), while not being fully addressed by either paradigm: RPE primarily focuses on non-humanoid robots, particularly fixed-base manipulators, whereas HPE is built upon human-specific skeletal topologies, body models, and motion priors. Despite recent progress in humanoid 2D keypoint detection and HPE adaptation, humanoid-native 3D pose recovery remains insufficiently studied, and a dedicated benchmark with suitable training data and evaluation protocols is still lacking. To address this gap, we introduce Humanoids, a benchmark for monocular 3D humanoid robot pose estimation, and propose HumanoidPose, a framework for this task. Humanoids provides synthetic 3D supervision across diverse humanoid embodiments, manually annotated real-world 2D data, and real-world RGB sequences paired with robot states for 3D evaluation on a physical Roban humanoid. HumanoidPose combines human-inspired visual perception with robot articulation modeling and explicit kinematic grounding. Experiments on Humanoids and the DHRP-H1 benchmark demonstrate strong performance in articulation recovery and 3D pose estimation, including zero-shot transfer to real-world 2D and 3D evaluation. Ablation studies further show the contribution of robot-native articulation modeling and explicit kinematic grounding. The dataset and code will be publicly released to support future research in the community.

</details>

---

### [[20_Research/Papers/具身智能/Inject,_Encode,_Navigate_Feature-Wise_Time_Injection_for_Rectified_Flow_with_Bidirectional_Feature_Encoding|Inject, Encode, Navigate: Feature-Wise Time Injection for Rectified Flow with Bidirectional Feature Encoding]]

![[assets/2611.27179_figure.png|800]]

- **arXiv**: [2611.27179](https://arxiv.org/abs/2611.27179)
- **PDF**: https://arxiv.org/pdf/2611.27179
- **详细分析**: [[20_Research/Papers/具身智能/Inject,_Encode,_Navigate_Feature-Wise_Time_Injection_for_Rectified_Flow_with_Bidirectional_Feature_Encoding|Inject, Encode, Navigate: Feature-Wise Time Injection for Rectified Flow with Bidirectional Feature Encoding]]
- **作者**: Xiaogang Wang, Debasish Mishra, Jia Hao Toh, Wangsheng Liu, Yash Shah
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Inject, Encode, Navigate: Feature-Wise Time Injection for Rectified Flow with Bidirectional Feature Encoding》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-model-based robotic navigation has gained increasing popularity, yet existing approaches still struggle to deliver effective and efficient navigation performance, \textit{e.g.}, diffusion-based policies that require costly iterative denoising. In this work, we propose three improvements to bridge these gaps. First, we adopt a rectified flow framework to reduce the required inference steps to one while achieving comparable or even superior performance. Second, we leverage a bidirectional Mamba-based visual encoder that employs selective state-space modeling to more effectively capture bidirectional temporal dependencies across observation frames, even with longer input sequences. Most importantly, we find that naïvely combining these two components to balance accuracy with inference speed yields no further performance gains or even produces inferior results. Upon extensive analysis, we realized that the root cause lies in the fact that the Hydra-derived temporal context is shared unchanged across all flow timesteps, and timestep information is introduced only within the velocity network. This weak coupling limits the model's ability to adaptively exploit temporal visual features at different flow states. To address this, we propose a feature-wise timestep conditioning design that explicitly conditions the visual embedding on the flow timestep, enabling noise-level-aware trajectory generation, thereby restoring a meaningful gradient pathway and enabling coherent interaction between the rectified flow and the temporal encoder. Extensive quantitative and qualitative experiments across multiple datasets demonstrate that our approach consistently outperforms both baseline and competitive methods.

</details>

---

### [[20_Research/Papers/具身智能/Mem-X_A_Memory-Dependent_Cross-Episode_Benchmark_for_Vision-and-Language_Navigation|Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation]]

![[assets/2611.27166_figure.png|800]]

- **arXiv**: [2611.27166](https://arxiv.org/abs/2611.27166)
- **PDF**: https://arxiv.org/pdf/2611.27166
- **详细分析**: [[20_Research/Papers/具身智能/Mem-X_A_Memory-Dependent_Cross-Episode_Benchmark_for_Vision-and-Language_Navigation|Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation]]
- **作者**: Zhikang Shi, Yuk Tung Samuel Fang, Hongyu Ding, Zixuan Chen, Yujin Wang, Junhui Guo, You Wu, Jieqi Shi, Jing Huo, Yang Gao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.6，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《Mem-X: A Memory-Dependent Cross-Episode Benchmark for Vision-and-Language Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, LMEE-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-term memory enables embodied agents to reuse past observations across tasks. However, existing cross-episode vision-and-language navigation (VLN) benchmarks often leave it unclear whether successful navigation relies on historical memory or current exploration. We introduce Mem-X, a benchmark designed to evaluate memory-dependent cross-episode VLN. Mem-X organizes episodes into sessions in which subsequent instructions refer to objects or routes encountered in earlier episodes. Its three levels evaluate historical-object recall, in-memory localization and episodic indexing, and off-memory relocalization and historical-route reproduction. For the latter two levels, agents receive episode-local poses but no transformations between episode frames, requiring them to establish spatial correspondence with historical memory. Mem-X comprises 2,071 episodes across 710 sessions in 34 scenes, including 1,204 memory-dependent episodes. We also provide MemBridge, a modular baseline that combines semantic scene memory, cross-episode localization, and coarse-to-fine retrieval to support existing VLN agents. Experiments with state-of-the-art VLN methods demonstrate the benefits of MemBridge while revealing substantial room for improvement on memory-dependent navigation. The benchmark and baseline code are available at https://github.com/NJU-R-L-Group-Embodied-Lab/Mem-X.

</details>

---

### [[20_Research/Papers/强化学习/PhysForce_Physics-aware_Force_Control_for_Interactive_Video_World_Model|PhysForce: Physics-aware Force Control for Interactive Video World Model]]

![[assets/2611.27164_figure.png|800]]

- **arXiv**: [2611.27164](https://arxiv.org/abs/2611.27164)
- **PDF**: https://arxiv.org/pdf/2611.27164
- **详细分析**: [[20_Research/Papers/强化学习/PhysForce_Physics-aware_Force_Control_for_Interactive_Video_World_Model|PhysForce: Physics-aware Force Control for Interactive Video World Model]]
- **作者**: Xuancheng Xu, Xiaofeng Wang, Yue Ma, Zheng Zhu, Bing-Kun Bao
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.0（加权：强化学习 0.2，世界模型 0.8）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《PhysForce: Physics-aware Force Control for Interactive Video World Model》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive video world models aim to predict how visual environments evolve in response to user interventions, including physically consistent state changes induced by applied forces. Existing methods often represent forces as motion trajectories, which may introduce inappropriate motion priors, causing the model to over-rely on encoded displacement patterns. More fundamentally, the model's internal representations do not reliably localize force-induced state changes, making it difficult to associate applied forces with their resulting physical responses. Also, limited force-annotated data make it difficult to produce physically consistent and temporally stable predictions in unseen scenarios. To address these limitations, we propose PhysForce, a two-stage framework that integrates supervised fine-tuning and reinforcement learning through three complementary components. During supervised fine-tuning, (1) the Latent Force Intervention Encoder maps force location, direction, and magnitude into the video latent space without exposing future motion; and (2) the Physics Attribution Network associates force interventions with localized changes in the latent state, strengthening the learning of physical responses to applied forces. During reinforcement learning, (3) Physics-Aware Reinforcement Learning uses self-supervised rewards on out-of-distribution videos to improve physical consistency and generalization. Extensive experiments show that PhysForce improves force responsiveness, physical consistency, and generalization, demonstrating its effectiveness for interactive video world models.

</details>

---

### [[20_Research/Papers/具身智能/TrajRealm_A_Large-Scale_Point_Tracking_Dataset_with_Diverse_Dynamics|TrajRealm: A Large-Scale Point Tracking Dataset with Diverse Dynamics]]

![[assets/2611.27136_figure.png|800]]

- **arXiv**: [2611.27136](https://arxiv.org/abs/2611.27136)
- **PDF**: https://arxiv.org/pdf/2611.27136
- **详细分析**: [[20_Research/Papers/具身智能/TrajRealm_A_Large-Scale_Point_Tracking_Dataset_with_Diverse_Dynamics|TrajRealm: A Large-Scale Point Tracking Dataset with Diverse Dynamics]]
- **作者**: Ni Yang, Weiguang Zhao, Jiafei Cao, Yankai Jiang, Haoyu Guo, Tao Yang, Chunhua Shen, Junting Dong
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.9，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《TrajRealm: A Large-Scale Point Tracking Dataset with Diverse Dynamics》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：EBench, OmniNavBench, TrajRealm-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose point tracking requires large-scale training data with diverse dynamics, yet existing datasets struggle to combine rich dynamic content, accurate scene geometry, and sufficient scale. We introduce TrajRealm, the first public synthetic point-tracking dataset to reach the ten-million-frame scale, constructed from games and embodied simulations. TrajRealm uses the rich environments and motion systems of modern games to capture diverse targets, activities, and interactions across diverse worlds, while embodied simulations add robot manipulation and indoor navigation data. The dataset provides RGB observations, depth, camera parameters, and persistent 2D and 3D point trajectories. These annotations provide precise, geometrically consistent supervision across foreground objects and static environmental surfaces. We also build TrajRealm-Bench with eight subcategories under Interaction and Locomotion to evaluate tracking across diverse scenes. Benchmark evaluations reveal the strengths and limitations of existing trackers in handling complex motion and maintaining long-term point correspondences. Training on TrajRealm improves the performance of existing tracking methods on synthetic and real-world benchmarks.

</details>

---

### [[20_Research/Papers/世界模型/A_Plan_or_an_Adversarial_Example_A_Round-Trip_Check_for_Latent_World_Models|A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models]]

![[assets/2611.27124_figure.png|800]]

- **arXiv**: [2611.27124](https://arxiv.org/abs/2611.27124)
- **PDF**: https://arxiv.org/pdf/2611.27124
- **详细分析**: [[20_Research/Papers/世界模型/A_Plan_or_an_Adversarial_Example_A_Round-Trip_Check_for_Latent_World_Models|A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models]]
- **作者**: Huiyuan Tian, Chih-Yung Wen, Shijian Li
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.32（加权：强化学习 0.16，世界模型 1.16）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《A Plan or an Adversarial Example? A Round-Trip Check for Latent World Models》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

If we optimize an image until a classifier is confident it shows a cat, we may get an adversarial example, not a cat. Planning with a latent world model is a similar search for actions whose predicted future is closest to the goal. Is the result a plan, or an adversarial example of the world model? We show that it can be either. On the released DINO-WM and LeWM, more iterations of the cross-entropy method (CEM) lower the predicted cost but lose up to half of the problems CEM had already solved. The model's own predictions do not reveal these failures. We propose a simple test that executes the plan after every iteration and counts the problems a planner solves and then loses. Unlike an image, a plan comes with its actions, which our round-trip check reads back from the predicted states with a small network, penalizing mismatches. The check reads back the sum of each block of five actions, the part that two consecutive predicted states determine. Without retraining the world model and at only 0.2% to 3.1% more planning time, it improves the widely used planners CEM and MPPI on three released world models, and gains more where planners lose more problems. Without replanning, success rises from 0.39 to 0.76 on Wall with DINO-WM and from 0.56 to 0.94 for MPPI on JEPA-WM. With replanning (MPC), it rises from 0.70 to 0.81 on Cube with LeWM.

</details>

---

### [[20_Research/Papers/机器人/EgoSurgHands_An_Egocentric_3D_Hand_Pose_Dataset_&_Benchmark_for_Open_Surgery_Training|EgoSurgHands: An Egocentric 3D Hand Pose Dataset & Benchmark for Open Surgery Training]]

![[assets/2611.27101_figure.png|800]]

- **arXiv**: [2611.27101](https://arxiv.org/abs/2611.27101)
- **PDF**: https://arxiv.org/pdf/2611.27101
- **详细分析**: [[20_Research/Papers/机器人/EgoSurgHands_An_Egocentric_3D_Hand_Pose_Dataset_&_Benchmark_for_Open_Surgery_Training|EgoSurgHands: An Egocentric 3D Hand Pose Dataset & Benchmark for Open Surgery Training]]
- **作者**: Ankit Pal, Guillaume Kugener, Sofia Volpi, Joshua Schwartz, Alex Idarraga, Pranav Rajpurkar, Gabriel A. Brat
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《EgoSurgHands: An Egocentric 3D Hand Pose Dataset & Benchmark for Open Surgery Training》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Surgical skill assessment, AR guidance, and robot learning from demonstration all benefit from 3D tracking of the surgeon's hands, yet no surgical dataset offers real egocentric articulated 3D hand pose. We introduce EgoSurgHands, a benchmark for real-captured egocentric hand pose estimation in open surgery training on synthetic pads. Captured with multi-sensor glasses, it contains 41,909 training hand-instance rows across 55 procedure recordings and 9,476 human-validated evaluation rows across 13 held-out recordings, spanning 13 tasks, 3 glove colors, and 4 trainees from first-year medical student to third-year resident. Each frame carries a multi-sensor stack: intrinsics, hand landmarks with per-hand confidence, timestamps, and eye gaze, plus SLAM extrinsics where SLAM succeeded. Evaluation labels combine sensor-fused pseudo-ground truth, human cross-review of every frame, surgeon adjudication of flagged cases, and an independent multi-view triangulated reference. Alongside the within-corpus, procedure-disjoint split, a leave-one-wearer-out protocol tested unseen trainees. Across eight methods evaluated zero-shot, from MANO-based reconstructors to the two-hand IntagHand and the keypoint-only MediaPipe Hands, egocentric pretraining was associated with stronger transfer on every held-out wearer. WildHands and JointTransformer had 18\% and 40\% lower PA-MPJPE, respectively, than the non-egocentric HaMeR. JointTransformer was the best performing model with an error of 14.95 mm. A substantial surgical domain gap remains, and the widely deployed MediaPipe Hands detected a hand in only 24.1\% of evaluation rows. As a baseline, a 58K-parameter residual corrector (JRN) on frozen backbones reached 10.96-14.85 mm PA-MPJPE on held-out wearers for the two ego-pretrained backbones. We release the dataset and benchmark code at https://egosurghands.github.io

</details>

---

### [[20_Research/Papers/强化学习/ReactDrive_Self-Reactive_Driving_World_Model|ReactDrive: Self-Reactive Driving World Model]]

![[assets/2611.27024_figure.png|800]]

- **arXiv**: [2611.27024](https://arxiv.org/abs/2611.27024)
- **PDF**: https://arxiv.org/pdf/2611.27024
- **详细分析**: [[20_Research/Papers/强化学习/ReactDrive_Self-Reactive_Driving_World_Model|ReactDrive: Self-Reactive Driving World Model]]
- **作者**: Yifan Wang, Xiaoqi Wang, Cho-Ying Wu, Wenbin He, Chenyu You, Liu Ren
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《ReactDrive: Self-Reactive Driving World Model》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The world evolves through the dynamics of its constituent entities and their interactions, with changes in one entity influencing the behavior of others. To simulate this evolution under different actions, interactive world models need to capture the resulting agent responses as part of the world's own dynamics. In autonomous driving, errors in modeling these responses can misrepresent maneuver safety and undermine the reliability of generated videos used for policy evaluation and learning. To formalize this intrinsic requirement for driving world model, we define self-reactivity as the capability to model agent responses from observed history and a specified ego action, and generate visual futures that reflect those responses without prescribed future agent trajectories. To realize this capability, we introduce ReactDrive, a driving world model that jointly learns agent dynamics and visual generation through a shared agent state representation. Within this framework, dynamics supervision grounds a reactive dynamics prior in observed agent states, while the video objective jointly optimizes the self-reactivity and visual realism. Experiments show improved agent responses, ego controllability, and video quality, a 96.0% preference for agent reactivity in human comparisons across five baselines, and better downstream planning through augmentation with generated videos. We hope this work encourages the community to recognize self-reactivityas a foundational capability for developing and evaluating interactive world models. Project page: https://reactdrive.github.io/ .

</details>

---

### [[20_Research/Papers/世界模型/ViewDreamer_A_Robot_World_Model_beyond_Fixed_Camera_Setups|ViewDreamer: A Robot World Model beyond Fixed Camera Setups]]

![[assets/2611.26981_figure.png|800]]

- **arXiv**: [2611.26981](https://arxiv.org/abs/2611.26981)
- **PDF**: https://arxiv.org/pdf/2611.26981
- **详细分析**: [[20_Research/Papers/世界模型/ViewDreamer_A_Robot_World_Model_beyond_Fixed_Camera_Setups|ViewDreamer: A Robot World Model beyond Fixed Camera Setups]]
- **作者**: Ye Mao, Jinhui Xiong, Egor Larionov, Shiyang Lu, Krystian Mikolajczyk, Wei Ye
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.6（加权：世界模型 0.8，机器人 0.8）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《ViewDreamer: A Robot World Model beyond Fixed Camera Setups》归入 世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AgiBot-World, Ctrl-World, GE-Sim, MultiWorld, PAIWorld, RoboView-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video generation models are increasingly important for robot learning, yet most generate each camera view separately or tile all views in a fixed layout. Robot demonstrations, however, are captured by synchronized cameras whose number, placement, and order vary across embodiments. We present ViewDreamer, a single world model that handles variable sets of cameras by disentangling per-view generation from cross-view interaction. Each view follows the generation path of a pretrained single-view model, and views interact only through shared slot tokens. We stabilize multi-view training with a curriculum that gradually increases the number of views. Cross-View Slot Agreement uses visual foundation models to group geometrically and semantically similar regions across views into shared slots. On RoboView-Bench, which covers one to four cameras, ViewDreamer achieves the best generation quality among the models evaluated and improves cross-view consistency over independent per-view generation. These gains carry over to our world-action model (WAM) and action-conditioned world model (AC-WM). Our WAM outperforms the FastWAM-Joint baseline on LIBERO-Plus, RoboTwin 2.0, and RoboDojo, and on a real Franka robot. Both variants improve out-of-domain generalization to various camera settings and scenes.

</details>

---

### [[20_Research/Papers/具身智能/RoboPRO_A_Perturbation-Resilient_and_Obstacle-Aware_Benchmark_for_Robotic_Manipulation|RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation]]

![[assets/2611.26971_figure.png|800]]

- **arXiv**: [2611.26971](https://arxiv.org/abs/2611.26971)
- **PDF**: https://arxiv.org/pdf/2611.26971
- **详细分析**: [[20_Research/Papers/具身智能/RoboPRO_A_Perturbation-Resilient_and_Obstacle-Aware_Benchmark_for_Robotic_Manipulation|RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation]]
- **作者**: Zhiyuan Li, Charles Eret, Dingsheng Liu, Xuan Zhao, Joshua Choi, Yangzheng Wu, Tongtong Cao, Yingxue Zhang, Amir Rasouli
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.7（加权：具身智能 1.2，机器人 1.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《RoboPRO: A Perturbation-Resilient and Obstacle-Aware Benchmark for Robotic Manipulation》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GenieSim, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Object manipulation in the real world requires robotic policies to be robust to contextual perturbations and capable of safe planning in cluttered scenes. However, the majority of existing robotics benchmarks contain clean tabletop environments with success rate as the sole metric, leaving two critical deployment questions unanswered: does the policy manipulate safely under real conditions and what does lead to its failure? To this end, we present RoboPRO, a Robotics benchmark for Perturbation-Resilient and Obstacle-aware planning, which unifies various axes of robustness in manipulation. RoboPRO comprises 80 diverse bimanual atomic and compositional tasks across four furnished indoor environments, with a total of 16,000 demonstrations and 5.6K diverse language instructions. The scenes are populated with different numbers of distractors (non-targets), ranging from clean, involving only target objects, to densely populated to impose both visual and operational clutter. Moreover, we propose two safety-aware event metrics to determine unsafe contact between the robot and the environment or distractors. Our evaluation protocol consists of a per-factor analysis of three key perturbations, namely visual, linguistic, and object-level, with different levels of distractor densities. We conduct extensive experiments on RoboPRO using state-of-the-art manipulation policies to analyze the impact of visual and operational clutter, perturbations, and instructional diversity. Our findings indicate clutter can drastically reduce success and increase non-target collision, different perturbations have different effects on the performance, and that training data composition affects overall performance. Our findings highlight the key challenges for manipulation in real-world conditions and motivate future research in this domain. Project page: https://robopro-bench.github.io/RoboPRO/

</details>

---

### [[20_Research/Papers/强化学习/SonoAtlasWorld_Anatomy-Grounded_Ultrasound_World_Models_for_Wide-Range_Scanning|SonoAtlasWorld: Anatomy-Grounded Ultrasound World Models for Wide-Range Scanning]]

![[assets/2611.26867_figure.png|800]]

- **arXiv**: [2611.26867](https://arxiv.org/abs/2611.26867)
- **PDF**: https://arxiv.org/pdf/2611.26867
- **详细分析**: [[20_Research/Papers/强化学习/SonoAtlasWorld_Anatomy-Grounded_Ultrasound_World_Models_for_Wide-Range_Scanning|SonoAtlasWorld: Anatomy-Grounded Ultrasound World Models for Wide-Range Scanning]]
- **作者**: Zheyuan Zhang, Boris Mailhe, Hang Yu, Yikang Liu, Xiao Chen, Ankush Mukherjee, Terrence Chen, Shanhui Sun
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.2（加权：世界模型 1，机器人 0.2）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《SonoAtlasWorld: Anatomy-Grounded Ultrasound World Models for Wide-Range Scanning》归入 世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AdaWorld, CheXWorld, EchoWorld, LiveWorld, SonoAtlasWorld, SonoGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning robotic ultrasound policies requires interactive environments for scalable data generation and repeatable evaluation, while exploration on real patients is limited by acquisition costs and safety constraints. Generative world models offer an alternative, but image history and probe actions alone do not ensure anatomical consistency across wide-range scans and changing acoustic windows. We introduce SonoAtlasWorld, an ultrasound world model built on anatomy as state. A persistent 3D anatomical asset extracted from computed tomography (CT) anchors each scan to a specific anatomy. Probe actions determine anatomical and acoustic visibility conditions for a causal ultrasound generator trained on clinical videos. Our three-stage pipeline combines anatomy-conditioned pretraining, causal conversion and long-rollout alignment. Inference optimizations achieve pose-to-ultrasound throughput of 81.2 FPS. To evaluate anatomical control beyond image similarity, we introduce the Action-Following Index (AFI), which measures normalized reconstruction gain over a static-prefix baseline. On 40 held-out 3D volumes, SonoAtlasWorld achieves liver and macro-organ AFI of 0.428 and 0.262, compared with at most 0.117 and 0.038 for the tested action- and geometry-conditioned methods. Long-rollout alignment reduces brightness drift by 3.46x at the end of 40 repeated scan cycles. SonoAtlasWorld also generates offline policy-training demonstrations and supports anatomically grounded closed-loop evaluation. Scaling the generated training data improves key-plane acquisition success from 48.2% to 81.2% on unseen anatomies in simulation, demonstrating its utility for robotic ultrasound policy learning.

</details>

---

### [[20_Research/Papers/强化学习/FlowScope_3D_Scene_Flow_Pretraining_Improves_Surgical_Robot_Policies|FlowScope: 3D Scene Flow Pretraining Improves Surgical Robot Policies]]

![[assets/2611.26865_figure.png|800]]

- **arXiv**: [2611.26865](https://arxiv.org/abs/2611.26865)
- **PDF**: https://arxiv.org/pdf/2611.26865
- **详细分析**: [[20_Research/Papers/强化学习/FlowScope_3D_Scene_Flow_Pretraining_Improves_Surgical_Robot_Policies|FlowScope: 3D Scene Flow Pretraining Improves Surgical Robot Policies]]
- **作者**: John J. Han, Adam Schmidt, Jingpei Lu, Zooey He, Muhammad Abdullah Jamal, Jie Ying Wu, Omid Mohareri
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《FlowScope: 3D Scene Flow Pretraining Improves Surgical Robot Policies》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Imitation learning for surgical robots is limited by the cost of collecting demonstrations. Meanwhile, many robot-assisted procedures are recorded as stereo video, yet policies cannot learn from them directly; clinical video carries no action labels. We present FlowScope, which pretrains a surgical policy network on unlabeled clinical video by forecasting scene flow, the metric 3D motion of scene points, with labels computed by off-the-shelf stereo depth and optical flow models. We pretrain the trunk of an Action Chunking Transformer (ACT) on a dataset of 1,149 clinical procedures (1.35M clips) and discard the flow head afterward, so the deployed policy is a standard ACT with no added inference cost. On a real surgical robotic system, FlowScope raises needle pickup success from 54% to 90% and first-handover success on needle regrasp from 4% to 52% (full task: 2% to 14%) over training from scratch (n=50 trials each), and retains its gains with a generative flow-matching action head. Ablations indicate that metric 3D motion is the strongest pretraining signal among those tested; kinematics, 2D tracks, depth alone, and scale-free 3D flow, each paired with kinematics, yield smaller or no gains. Representation analyses suggest that scene-flow pretraining encodes metric needle depth more accurately, that kinematics pretraining increases reliance on the robot state, and that needle-depth probes follow the ordering of real-robot success where offline validation error does not.

</details>

---
