# cs.CV | Computer Vision and Pattern Recognition | 2026-10-26

#arxiv #ComputerScience

**论文数**: 6

### [[20_Research/Papers/世界模型/UniAction_Unified_Action_Conditioning_for_World_Models|UniAction: Unified Action Conditioning for World Models]]

![[assets/2610.32977_figure.png|800]]

- **arXiv**: [2610.32977](https://arxiv.org/abs/2610.32977)
- **PDF**: https://arxiv.org/pdf/2610.32977
- **详细分析**: [[20_Research/Papers/世界模型/UniAction_Unified_Action_Conditioning_for_World_Models|UniAction: Unified Action Conditioning for World Models]]
- **作者**: Bowen Xue, Zizhang Li, Hong-Xing Yu, Jiajun Wu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 1.2（加权：世界模型 1，机器人 0.2）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《UniAction: Unified Action Conditioning for World Models》归入 世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Actions that condition world models are highly heterogeneous, and thus existing action-conditioned world models are typically built for individual action types, fragmenting already limited action-annotated data across separate models. We introduce UniAction, a unified action-conditioning framework that represents any action as a sparse set of action elements, each with a discrete semantic identity and a continuous spatiotemporal grounding coordinate. By mapping these coordinates directly into the pretrained video model's native positional space, UniAction allows heterogeneous actions to condition a shared world model within the same spatiotemporal structure. We further introduce cardinality-calibrated attention to address the bias from differing action representation granularities. We evaluate UniAction on four representative action forms: force, camera control, hand pose, and robot pose. UniAction outperforms conditioning alternatives in action following, and a single jointly trained model surpasses the action-specific experts, showing that heterogeneous action data benefit from unified model and joint training.

</details>

---

### [[20_Research/Papers/机器人/ViT-H_Generative_Video-To-Humanoid_Control_with_Motion_Tracking_Feedback|ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback]]

![[assets/2610.32966_figure.png|800]]

- **arXiv**: [2610.32966](https://arxiv.org/abs/2610.32966)
- **PDF**: https://arxiv.org/pdf/2610.32966
- **详细分析**: [[20_Research/Papers/机器人/ViT-H_Generative_Video-To-Humanoid_Control_with_Motion_Tracking_Feedback|ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback]]
- **作者**: Zimo He, Tianyi Bian, Zizhong Yang, Hongjie Li, Nan Jiang, Jieming Cui, Baoxiong Jia, Yizhou Wang, Siyuan Huang, Yixin Zhu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《ViT-H: Generative Video-To-Humanoid Control with Motion Tracking Feedback》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning humanoid control from monocular human videos offers a scalable way to acquire diverse whole-body behaviors. Yet, existing reconstruction-retargeting-tracking pipelines are limited in system-level scalability by separately optimized intermediate stages and cannot directly optimize reference motion executability using downstream tracking feedback. We present ViT-H, a video-to-humanoid control framework following a generation-and-tracking paradigm. ViT-H directly generates humanoid reference motions from videos with a diffusion model, bypassing human motion reconstruction and retargeting, and uses motion-tracking outcomes to post-train the generator with direct preference optimization. We further introduce an autoregressive variant that enables real-time humanoid video teleoperation with sub-400 ms latency. Extensive experiments on the Unitree G1 demonstrate that ViT-H outperforms state-of-the-art reconstruction-retargeting-tracking pipelines in both motion quality and executability. We further show that ViT-H scales favorably with model size and with both pre-training and post-training data scale, while motion-tracking feedback consistently improves executability across different motion trackers.

</details>

---

### [[20_Research/Papers/强化学习/ACWM-RM_A_Reference-Free_Reward_Model_from_Complementary_Mismatch_Preferences|ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences]]

![[assets/2610.32222_figure.png|800]]

- **arXiv**: [2610.32222](https://arxiv.org/abs/2610.32222)
- **PDF**: https://arxiv.org/pdf/2610.32222
- **详细分析**: [[20_Research/Papers/强化学习/ACWM-RM_A_Reference-Free_Reward_Model_from_Complementary_Mismatch_Preferences|ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences]]
- **作者**: Shibo Hong, Siyu Ren, FengJiao Chen, Zhongyuan Peng, Wei Shi, Yixin Cao
- **cs 子类**: cs.CV
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.4（加权：强化学习 1，世界模型 0.4）
- **关联关键词**: RL, WorldModel, ComputerVision

#### 研究背景与动机

《ACWM-RM: A Reference-Free Reward Model from Complementary Mismatch Preferences》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AVM-Eval, AgiBotWorld, GE-Sim, Genie-Sim, IRASim, RLVR-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has gained attention for improving action-conditioned world models (ACWMs), as it enables reward-driven optimization of visual quality (VQ) and action-following fidelity (AF) beyond flow-matching optimization. Realizing this potential requires reward signals that reliably rank videos by both VQ and AF. However, existing rewards capture only one dimension: metric-based rewards assess VQ but require ground-truth videos and do not directly assess AF, while inverse dynamics model (IDM) rewards assess AF without references but do not guarantee VQ. Moreover, IDMs, typically trained on real videos, may provide unreliable rewards for generated videos containing visual artifacts and physical inconsistencies. In this work, we introduce the Action and Video Mismatch Benchmark (AVM-Eval), comprising 67.2k pairs that evaluate how reliably IDMs assess AF on real and generated videos. We then propose ACWM-RM, a reward model that jointly assesses VQ and AF without ground-truth videos during reward computation. To train it, we first construct the Action and Video Mismatch Preference Dataset (AVM-Pref) with 506.3k pairs providing complementary supervision: action-mismatch pairs supervise AF, while video-mismatch pairs supervise VQ and expose the model to generated videos. We then pretrain an action-conditioned predictor on real videos to learn forward dynamics before jointly training it with a patch-weighted score head on AVM-Pref to transfer these dynamics to AF assessment on generated videos. Evaluation on AVM-Eval reveals the limited reliability of IDMs on generated videos, while downstream RL experiments show that ACWM-RM outperforms reward baselines in both criteria.

</details>

---

### [[20_Research/Papers/具身智能/EgoForesight_Effectively_Scaling_Policy_Learning_with_Noisy_Egocentric_Actions|EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions]]

![[assets/2610.31845_figure.png|800]]

- **arXiv**: [2610.31845](https://arxiv.org/abs/2610.31845)
- **PDF**: https://arxiv.org/pdf/2610.31845
- **详细分析**: [[20_Research/Papers/具身智能/EgoForesight_Effectively_Scaling_Policy_Learning_with_Noisy_Egocentric_Actions|EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions]]
- **作者**: Chubin Zhang, Changyuan Wang, Yirui Wang, Ao Li, Shilin Ma, Yue Su, Cai Zhou, Xiuwei Xu, Tianle Zhang, Yansong Tang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《EgoForesight: Effectively Scaling Policy Learning with Noisy Egocentric Actions》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling policy learning requires broad experience and reliable supervision. Robot demonstrations provide high-quality trajectory supervision but are costly to collect. Egocentric videos broaden task and environment coverage, yet motion reconstruction and retargeting introduce noisy action labels. To address this challenge, we introduce EgoForesight, a vision-language-action framework that learns jointly from both sources by reducing the influence of unreliable action labels and exploiting demonstrated outcomes as complementary supervision. A joint vision-action flow couples future visual representation prediction with action generation, unifying reliability-aware action learning with outcome-informed representation transfer. Specifically, reliability-conditioned corruption allocates action supervision across noise levels according to source reliability, while reliability-weighted regression regulates each source's contribution. Complementing this treatment of noisy labels, privileged-future representation distillation draws supervision from demonstrated outcomes. An exponential-moving-average teacher observes the current scene and clean future to encode action-relevant structure from the resulting scene change. Its deeper representations supervise an earlier student layer receiving a corrupted future, providing outcome-informed structure beyond noisy action annotations. Together, these mechanisms support effective scaling with noisy egocentric actions. Over the tested range, EgoForesight exhibits steeper scaling slopes than the baseline, reducing real-world open-loop action MSE by 20.5% and improving RoboCasa few-shot success by 8.1 percentage points at 30,000 hours of pretraining data. After post-training, it also achieves strong absolute performance in both simulated and real-world dexterous manipulation.

</details>

---

### [[20_Research/Papers/机器人/WorldMirror_Agentic_Real-to-Sim_Generation_of_Interactive_Worlds_from_In-the-Wild_Robot_Demonstrations|WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations]]

![[assets/2610.31834_figure.png|800]]

- **arXiv**: [2610.31834](https://arxiv.org/abs/2610.31834)
- **PDF**: https://arxiv.org/pdf/2610.31834
- **详细分析**: [[20_Research/Papers/机器人/WorldMirror_Agentic_Real-to-Sim_Generation_of_Interactive_Worlds_from_In-the-Wild_Robot_Demonstrations|WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations]]
- **作者**: Tianling Xu, Weijie Wan, Honghao Su, Kailun Su, Junyuan Tang, Huichi Zhou, Haozheng Zhang, Qi Xiong, Ping Luo, Wenbo Ding, Tianxing Chen, Yue Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《WorldMirror: Agentic Real-to-Sim Generation of Interactive Worlds from In-the-Wild Robot Demonstrations》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World, Real-to-Sim, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing approaches for robot learning in simulation often require substantial manual effort to construct scenes and specify tasks, limiting training scalability and data diversity. Meanwhile, in-the-wild robot demonstrations naturally provide diverse and realistic observations of real-world interactions. Leveraging these demonstrations for simulation requires both high-fidelity visual reconstruction and physically consistent interactions. General-purpose agents offer flexible adaptation to diverse scenarios and strong reasoning about 3D spatial relationships, while specialized generative models provide high-fidelity reconstruction of scene appearance and geometry. We introduce WorldMirror, an agentic real-to-sim framework that constructs interactive digital twins from in-the-wild robot demonstrations. Our central idea is to formulate real-to-sim construction as the iterative refinement of an executable world program. A coding agent decomposes the observed scene, plans reconstruction steps, and orchestrates specialized image and 3D generation tools, refining the program through verification feedback. A camera-pose-anchored scene representation organizes the world into static visual context, support geometry, and editable interactive assets while preserving spatial relationships among the scene, objects, and robot. The agent uses this representation to diagnose and correct reconstruction errors, enabling physically consistent interaction and trajectory replay. Experiments on DROID demonstrate that WorldMirror can reconstruct visually faithful and geometrically consistent interactive worlds while preserving the physical validity of recorded robot trajectories.

</details>

---

### [[20_Research/Papers/具身智能/See_What_I_Need,_Dream_What_I_Want_A_Navigation_Foundation_Model_on_a_Self-Constructed_Representation_Space|See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space]]

![[assets/2610.31762_figure.png|800]]

- **arXiv**: [2610.31762](https://arxiv.org/abs/2610.31762)
- **PDF**: https://arxiv.org/pdf/2610.31762
- **详细分析**: [[20_Research/Papers/具身智能/See_What_I_Need,_Dream_What_I_Want_A_Navigation_Foundation_Model_on_a_Self-Constructed_Representation_Space|See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space]]
- **作者**: Jiawei Chen, Yinxi Wang, Zihan Yang, Meijun Gao, Yaowei Liu, Shuming Zhang, Zecheng Li, Xiangju Mi, Yuxuan Liu, Runzhong Huang, Tianlin Li, Xun Zhang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能, 世界模型
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.4，世界模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《See What I Need, Dream What I Want: A Navigation Foundation Model on a Self-Constructed Representation Space》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EVT-Bench, Real-World, TrackVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

What visual representation should a navigation policy act on? Navigation policies built on vision foundation models largely leave representation design to the encoders' pretraining objectives. We present RepresentNav, a navigation foundation model built on a self-constructed representation space: a visual representation constructed by the policy's own objectives from vision foundation models. RepresentNav builds this space with Representation Residuals, a compact three-layer transformer that attends over features spanning the full depth of multiple complementary vision foundation models, so that the policy learns to see what it needs for navigation. In the same space it dreams what it wants: before every action a latent chain-of-thought predicts the representation of the scene a moment ahead. The dream is trained end-to-end with the policy as a joint-embedding predictive architecture (JEPA), with a next-representation prediction loss and a regularizer on its targets. RepresentNav sets a new state of the art on VLNVerse, VLN-CE R2R, EVT-Bench, and two point-goal benchmarks, and its gains carry over to a physical robot amid clutter and moving people. On VLNVerse fine-grained, RepresentNav achieves 83.80% success, outperforming the previous state of the art by 20.05 percentage points, and on EVT-Bench distracted tracking it reaches 85.5% with a single camera (+10.1). With the same encoders, the self-constructed space clearly outperforms concatenating their outputs and learns to weight their layers unevenly, and a dream in it cuts collisions by a quarter. A single dreamed latent decodes into the depth, semantics, and 3D occupancy of the scene a moment ahead, more accurately than pretrained encoders applied to the real future frame, although occupancy is never supervised, and the rollout tracks the robot's own motion over the next second: the dream emerges as a compact latent world model.

</details>

---
