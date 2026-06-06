# cs.RO | Robotics | 2026-06-04

#arxiv #ComputerScience

**论文数**: 23

### [[20_Research/Papers/世界模型/GRAIL_Generating_Humanoid_Loco-Manipulation_from_3D_Assets_and_Video_Priors|GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors]]

![[assets/2606.05160_figure.jpeg|800]]

- **arXiv**: [2606.05160](https://arxiv.org/abs/2606.05160)
- **PDF**: https://arxiv.org/pdf/2606.05160
- **详细分析**: [[20_Research/Papers/世界模型/GRAIL_Generating_Humanoid_Loco-Manipulation_from_3D_Assets_and_Video_Priors|GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors]]
- **作者**: Tianyi Xie, Haotian Zhang, Jinhyung Park, Zi Wang, Bowen Wen, Jiefeng Li, Xueting Li, Qingwei Ben, Haoyang Weng, Yufei Ye, David Minor, Tingwu Wang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《GRAIL: Generating Humanoid Loco-Manipulation from 3D Assets and Video Priors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling humanoid loco-manipulation requires robot-compatible demonstrations across diverse objects, whole-body motions, and scene geometries, but teleoperation and motion capture are difficult to scale because each collection depends on physical setups, instrumented actors, and robot operation. We present GRAIL, a digital generation pipeline that remains fully virtual until deployment: it composes 3D assets, simulator-ready scenes, and priors from video foundation models (VFMs) to synthesize interactions without rebuilding physical environments or teleoperating the robot. Rather than reconstructing unconstrained in-the-wild videos, GRAIL starts from fully specified 3D configurations in which object geometry, camera parameters, metric scale, environment depth, and a robot-proportioned character are known before video generation and reused during reconstruction. This privileged setup better conditions 4D recovery, allowing model-based object tracking, human motion estimation, and interaction-aware optimization to reconstruct metric 4D human-object interaction (HOI) trajectories with reduced depth ambiguity and morphology mismatch. We retarget the recovered motions to a humanoid robot and train complementary task-general trackers: an object-aware latent adaptor for manipulation and a scene-aware tracker for terrain traversal. GRAIL produces over 20,000 sequences spanning pick-up, object manipulation, sitting, and terrain traversal. Using only GRAIL-generated data, we train egocentric visual policies through a sim-to-real pipeline and deploy them on a Unitree G1 humanoid, achieving 84\% real-world success on diverse object pick-up and 90\% success on stair-climbing.

</details>

---

### [[20_Research/Papers/具身智能/X4Val_Learning_Neural_Surrogates_for_Variance-Reduced_Policy_Evaluation|X4Val: Learning Neural Surrogates for Variance-Reduced Policy Evaluation]]

![[assets/2606.05159_figure.png|800]]

- **arXiv**: [2606.05159](https://arxiv.org/abs/2606.05159)
- **PDF**: https://arxiv.org/pdf/2606.05159
- **详细分析**: [[20_Research/Papers/具身智能/X4Val_Learning_Neural_Surrogates_for_Variance-Reduced_Policy_Evaluation|X4Val: Learning Neural Surrogates for Variance-Reduced Policy Evaluation]]
- **作者**: Rachel Luo, Michael Watson, Apoorva Sharma, Heng Yang, Han Qi, Edward Schmerling, Sushant Veer, Boris Ivanovic, Marco Pavone
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《X4Val: Learning Neural Surrogates for Variance-Reduced Policy Evaluation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SureSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rigorous evaluation of learning-based robotic systems is an essential prerequisite for deployment. However, real-world test data is expensive to gather; moreover, in a typical iterative development context, data gathered from the latest policy is necessarily limited in scale. This motivates evaluation methodologies that make use of heterogeneous data sources, including simulation, historical policy logs, and data collected from related platforms or environments. While such auxiliary data are abundant and inexpensive, they are generally not directly representative of real-world outcomes -- for example, performance in simulation may differ substantially from performance in the real world -- making their principled use for high-confidence performance estimation challenging. In this paper, we introduce X4Val, a general framework for variance-reduced real-world metric estimation in the presence of non-paired, multi-domain data. X4Val embeds samples from real and auxiliary domains into a shared representation space and learns a transferable predictor of real-world metrics; this learned predictor is then incorporated into a control-variates estimator, enabling variance reduction even when paired samples are unavailable. We provide theoretical analysis and empirical evaluations on autonomous driving and real-world robot manipulation tasks, domains across which X4Val achieves up to 38.4% variance reduction and demonstrates consistent improvements over strong baselines. These results show that non-paired, heterogeneous data can be leveraged to substantially improve the sample efficiency of rigorous robotic system validation.

</details>

---

### [[20_Research/Papers/具身智能/HORIZON_Recoverability-Governed_Curriculum_for_Physical-Domain_Scaling|HORIZON: Recoverability-Governed Curriculum for Physical-Domain Scaling]]

![[assets/2606.05143_figure.jpg|800]]

- **arXiv**: [2606.05143](https://arxiv.org/abs/2606.05143)
- **PDF**: https://arxiv.org/pdf/2606.05143
- **详细分析**: [[20_Research/Papers/具身智能/HORIZON_Recoverability-Governed_Curriculum_for_Physical-Domain_Scaling|HORIZON: Recoverability-Governed Curriculum for Physical-Domain Scaling]]
- **作者**: Chenhao Bai, Liqin Lu, Kaijun Wang, Hui Chen, Jin-Chuan Shi, Yuyang Liu, Hao Chen, Chunhua Shen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《HORIZON: Recoverability-Governed Curriculum for Physical-Domain Scaling》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scaling robust robot policies requires more than broader randomization, because physical-domain experience must remain organized and learnable throughout training. We study when a policy can benefit from harder physics and identify recoverability as a central constraint in on-policy physical-domain scaling. In on-policy training, new dynamics are useful only insofar as they remain close enough to the current policy to generate corrective on-policy data, rather than collapsing rollouts into unrecoverable failures. Using quadruped locomotion as a physically demanding benchmark for embodied generalization, we introduce HORIZON, a checkpointed frontier curriculum that expands physical domains only within the current policy's recoverable boundary. HORIZON uses rollback and boundary refinement to govern each expansion step, turning fixed randomization into a continual process of physical-domain growth. Experiments reveal three regularities of physical-domain expansion. First, direct domain widening is uneven across physical axes and often unlearnable without staged ordering. Second, domain composition is non-monotonic, and adding more domains beyond a compact core can dilute recoverable joint samples and reduce overall robustness. Third, offline distillation of isolated experts cannot substitute for the joint interaction generated by on-policy curriculum. Together, these results frame physical-domain generalization as a continual growth problem for embodied control, with recoverability as the organizing principle for on-policy expansion.

</details>

---

### [[20_Research/Papers/具身智能/Generalization_of_World_Models_under_Environmental_Variability_for_Vision-based_Quadrotor_Navigation|Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation]]

![[assets/2606.05015_figure.png|800]]

- **arXiv**: [2606.05015](https://arxiv.org/abs/2606.05015)
- **PDF**: https://arxiv.org/pdf/2606.05015
- **详细分析**: [[20_Research/Papers/具身智能/Generalization_of_World_Models_under_Environmental_Variability_for_Vision-based_Quadrotor_Navigation|Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation]]
- **作者**: Luca Zanatta, Grzegorz Malczyk, Kostas Alexis
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 0.6，强化学习 0.2，世界模型 1，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Generalization of World Models under Environmental Variability for Vision-based Quadrotor Navigation》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AerialGym, MBRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models, learned generative models that predict how an environment evolves, have become a promising tool for sample-efficient robot learning. Yet how robust they are to environmental variability remains poorly understood. To address this, we conduct a systematic study using vision-based quadrotor navigation as a testbed problem, training DreamerV3-based world models under varying levels of environmental randomness and evaluating them across all levels through cross-environment validation, spanning both Self-Supervised Learning (SSL) pretraining and Reinforcement Learning (RL) fine-tuning. We then deploy all world models and associated navigation policies on a real quadrotor in unseen environments, including an open-loop run where the model receives just 2.5s of real sensory input before all sensors are cut off, leaving the system to navigate entirely in imagination over a 12m traverse. Our results show that world model robustness during SSL pretraining is a strong predictor of sim-to-real transfer: every model that generalized well in cross-environment SSL validation deployed successfully in the real world, passing through gaps as narrow as 0.67m, whereas the model that dominated simulation policy evaluation failed on the real platform. We further identify (a) the discrete latent size and (b) the training-sequence length as the dominant factors governing world model quality.

</details>

---

### [[20_Research/Papers/具身智能/Potential-Guided_Flow_Matching_for_Vision-Language-Action_Policy_Improvement|Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement]]

![[assets/2606.04968_figure.png|800]]

- **arXiv**: [2606.04968](https://arxiv.org/abs/2606.04968)
- **PDF**: https://arxiv.org/pdf/2606.04968
- **详细分析**: [[20_Research/Papers/具身智能/Potential-Guided_Flow_Matching_for_Vision-Language-Action_Policy_Improvement|Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement]]
- **作者**: Yunpeng Mei, Jiakai He, Hongjie Cao, Chenyu Wang, Xiaowen Zhu, Yihan Zhou, Jiamin Wang, Chenbo Xin, Peng Cheng, Yuxuan Yang, Yijie Wang, Xinhu Zheng...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.3（加权：具身智能 1.8，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, RL

#### 研究背景与动机

《Potential-Guided Flow Matching for Vision-Language-Action Policy Improvement》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large vision-language-action (VLA) policies are increasingly trained as conditional generative models over action chunks. Yet deployment produces mixed-quality experience-successful demonstrations, partial completions, recoverable mistakes, and failures-that is difficult to use with standard imitation. Full behavior cloning (BC) imitates failures, filtered BC discards useful sub-trajectories, and offline reinforcement learning adds a large critic. We introduce ForesightFlow, a self-guided flow-matching policy that augments each generated action chunk with a learned success-potential trajectory. The same flow proposes and scores candidate actions, enabling best-of-$K$ inference without an external critic. The key issue is that policy improvement and value calibration require different supervision: advantage weighting should emphasize high-quality actions, but applying the same weights to potential coordinates suppresses failure gradients and creates overconfident scores. We address this with decoupled advantage-weighted flow matching, applying exponentiated advantage weights only to action velocities while training potential velocities uniformly. We further derive a one-step boundary estimator for conditional flow matching, allowing advantage computation with a single stop-gradient forward pass. Across five BEHAVIOR-1K simulation tasks and five real-world bimanual tasks, ForesightFlow improves over imitation baselines, matches the strongest separate-critic baseline in simulation success, improves real-world success, and reduces training compute by $38\%$. Ablations show that decoupling prevents value hallucination, the one-step estimator preserves candidate-ranking fidelity, and self-guided sampling improves long-horizon execution.

</details>

---

### [[20_Research/Papers/具身智能/WAM-Nav_Asymmetric_Latent_World-Action_Modeling_for_Unified_Visual_Navigation|WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation]]

![[assets/2606.04907_figure.png|800]]

- **arXiv**: [2606.04907](https://arxiv.org/abs/2606.04907)
- **PDF**: https://arxiv.org/pdf/2606.04907
- **详细分析**: [[20_Research/Papers/具身智能/WAM-Nav_Asymmetric_Latent_World-Action_Modeling_for_Unified_Visual_Navigation|WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation]]
- **作者**: Ning Yang, Yan Huang, Kaiwen Peng, Ziheng He, Kai Wang, Cui Miao, Kailin Lyu, Guo Li, Xiaofeng Wang, Zheng Zhu, Jing Liu, Nianfeng Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL, ComputerVision

#### 研究背景与动机

《WAM-Nav: Asymmetric Latent World-Action Modeling for Unified Visual Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual navigation requires generating smooth and collision-free trajectories under complex geometric and physical constraints. Existing reactive policies that directly map observations to actions lack anticipatory reasoning, limiting their ability to proactively avoid obstacles. While visual imagination offers predictive foresight, conventional modular approaches separate scene prediction from policy learning, often leading to error accumulation and inefficient inference. To address these limitations, we propose WAM-Nav, a Latent World-Action Model for embodied visual navigation that jointly learns action generation and latent visual foresight, enabling more robust and foresighted navigation decisions without compromising inference efficiency. Specifically, WAM-Nav utilizes a shared Diffusion Transformer for asymmetric joint diffusion to concurrently generate long-horizon actions and short-horizon visual foresight, reducing the inference latency and visual error accumulation inherent in multi-step autoregressive rollouts. To further encourage smooth and consistent trajectory generation, we introduce a dual-stream contextual conditioning mechanism that integrates episode-level ego-motion history with sequential visual observations. Combined with a unified goal alignment module that preserves balanced representations across goal types, WAM-Nav naturally supports Image-Goal, Point-Goal, and No-Goal exploration within a single policy. Extensive experiments on the challenging ClutterScenes and InternScenes benchmarks demonstrate strong generalization of WAM-Nav, particularly on Image-Goal and Point-Goal navigation, where it improves success rates by 15.7% and 3.3%, respectively. Real-world deployment further validates effective zero-shot sim-to-real transfer, achieving an average 85% task success rate across diverse indoor and outdoor environments.

</details>

---

### [[20_Research/Papers/机器人/Teaching_Robots_to_Say_'I_Don't_Know'_SENTINEL_for_Uncertainty-Aware_SLAM|Teaching Robots to Say 'I Don't Know' : SENTINEL for Uncertainty-Aware SLAM]]

![[assets/2606.04853_figure.jpg|800]]

- **arXiv**: [2606.04853](https://arxiv.org/abs/2606.04853)
- **PDF**: https://arxiv.org/pdf/2606.04853
- **详细分析**: [[20_Research/Papers/机器人/Teaching_Robots_to_Say_'I_Don't_Know'_SENTINEL_for_Uncertainty-Aware_SLAM|Teaching Robots to Say 'I Don't Know' : SENTINEL for Uncertainty-Aware SLAM]]
- **作者**: Abhishek S, Badrikanath Praharaj, Sreeram MV
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Teaching Robots to Say 'I Don't Know' : SENTINEL for Uncertainty-Aware SLAM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-cost 2D LiDARs lack the intensity channel that higher-end sensors use to diagnose measurement failures, yet they are widely used on educational and budget robotics platforms. We present SENTINEL, a training - free, label - free reliability estimation framework that gives range - only LiDAR an effective diagnostic signal. SENTINEL combines geometry-based scan statistics with cross - modal depth consistency between LiDAR and an RGB - D camera to compute a per - scan reliability score between 0 and 1. When the score falls below a threshold, corrupted scans are rejected and the robot falls back to calibrated wheel odometry, preventing silent SLAM corruption. We evaluate SENTINEL on a GEFIER R1 four - wheel skid-steer robot equipped with an RPLidar A2M12 and an Intel RealSense D435i in a 185 cm by 245 cm arena containing controlled transparent and reflective failure elements on a central obstacle. Spatial reliability maps across five surface conditions, including glass, mirror, shiny paper, and a mixed mirror and shiny-paper condition, show clear separation between clean and failure cases, allowing affected regions to be identified as reject or noise. Because these failure modes are absent in simulation, validation is performed entirely on real hardware.

</details>

---

### [[20_Research/Papers/具身智能/M3imic_Learning_a_Versatile_Whole-Body_Controller_for_Multimodal_Motion_Mimicking|M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking]]

![[assets/2606.04829_figure.png|800]]

- **arXiv**: [2606.04829](https://arxiv.org/abs/2606.04829)
- **PDF**: https://arxiv.org/pdf/2606.04829
- **详细分析**: [[20_Research/Papers/具身智能/M3imic_Learning_a_Versatile_Whole-Body_Controller_for_Multimodal_Motion_Mimicking|M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking]]
- **作者**: Zuxing Lu, Ziang Zheng, Yao Lyu, Jingyu Liu, Feihong Zhang, Song Lu, Xin Yuan, Changyin Sun, Xingxing Zuo, Shengbo Eben Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.3，强化学习 0.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《M3imic: Learning a Versatile Whole-Body Controller for Multimodal Motion Mimicking》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Building a general-purpose whole-body controller is essential for enabling diverse motion capabilities in humanoid robots across a wide range of downstream tasks, including locomotion and loco-manipulation. Different tasks rely on distinct motion reference modalities: locomotion primarily depends on coordinated robot joint trajectories, whereas manipulation requires precise end-effector trajectory tracking. Existing methods often overlook the representational mismatch between dense robot joint angles and sparse end-effector poses. To address this, we propose Multi-Modal Mimic (M3imic), a versatile multi-modal whole-body control framework that unifies heterogeneous motion reference modalities, including robot joint angles, human pose trajectories, and end-effector poses, using modality-specific encoders to map them into a shared latent space. Leveraging large-scale reinforcement learning in the simulator, we train a single policy that achieves sim-to-real transfer across multiple motion reference modalities without modality-specific retraining. Extensive simulation and real-world experiments on the Unitree G1 robot are conducted to evaluate the proposed framework. In simulation, the policy achieves a peak success rate of 98.42\% on an unseen test dataset, demonstrating its exceptional generalization capability. The code is available at this https URL

</details>

---

### [[20_Research/Papers/具身智能/HapTile_A_Haptic-Informed_Vision-Tactile-Language-Action_Dataset_for_Contact-Rich_Imitation_Learning|HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning]]

![[assets/2606.04825_figure.jpg|800]]

- **arXiv**: [2606.04825](https://arxiv.org/abs/2606.04825)
- **PDF**: https://arxiv.org/pdf/2606.04825
- **详细分析**: [[20_Research/Papers/具身智能/HapTile_A_Haptic-Informed_Vision-Tactile-Language-Action_Dataset_for_Contact-Rich_Imitation_Learning|HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning]]
- **作者**: Amirhosein Alian, Yongqiang Zhao, Shiyi Gu, Xuyang Zhang, Zhuo Chen, Christopher E. Mower, Haitham Bou-Ammar, Shan Luo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《HapTile: A Haptic-Informed Vision-Tactile-Language-Action Dataset for Contact-Rich Imitation Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FD-VLA, ForceVLA, OpenVLA, RoboSet, TaF-VLA, Tactile-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the importance of tactile sensing for reliable manipulation, most existing Vision-Language-Action (VLA) datasets remain vision-only, and those that do incorporate tactile information typically lack the joint combination of task diversity, language conditioning, and action trajectories. Furthermore, existing teleoperation pipelines rarely provide haptic feedback to the operator, despite its established role in demonstration quality and manipulation stability. In this work, we present HapTile, a contact-grounded visuotactile manipulation dataset that advances beyond vision-only trajectory datasets by embedding physical interaction sensing at two levels: fingertip tactile feedback at the robot end-effector, and haptic-informed demonstrations at the teleoperator side. The data collection platform integrates haptic feedback directly into the teleoperation controller, enabling the operator to perceive contact interactions in real time. It is built around a standard and reproducible robotic system equipped with custom-designed fingertip tactile sensors. The dataset comprises everyday manipulation tasks spanning a broad range of contact-rich skills, including pick-and-place, folding, pressing, stacking, and other routine activities. Each task is paired with language instructions that condition the policy on the manipulation objective, together with synchronized visuotactile observations and action trajectories. In addition, we provide a benchmarking study on contact-rich policy learning using two baseline models to evaluate the effectiveness of the proposed contact-grounded dataset. The dataset and additional details are available on our website: this http URL .

</details>

---

### [[20_Research/Papers/机器人/Real-World_Deployment_of_a_5G-Connected_Edge-Controlled_Aerial_Robot_in_Industrial_Subterranean_Mines|Real-World Deployment of a 5G-Connected Edge-Controlled Aerial Robot in Industrial Subterranean Mines]]

![[assets/2606.04818_figure.png|800]]

- **arXiv**: [2606.04818](https://arxiv.org/abs/2606.04818)
- **PDF**: https://arxiv.org/pdf/2606.04818
- **详细分析**: [[20_Research/Papers/机器人/Real-World_Deployment_of_a_5G-Connected_Edge-Controlled_Aerial_Robot_in_Industrial_Subterranean_Mines|Real-World Deployment of a 5G-Connected Edge-Controlled Aerial Robot in Industrial Subterranean Mines]]
- **作者**: Achilleas Santi Seisa, Emanuele Pagliari, Gerasimos Damigos, Elias Small, George Nikolakopoulos
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Real-World Deployment of a 5G-Connected Edge-Controlled Aerial Robot in Industrial Subterranean Mines》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This article presents the first real-world autonomous flight of a 5G-connected aerial robot controlled by an edge-offloaded controller, and aims to bridge the gap between controlled and factual setups. The robot operates within an active industrial subterranean mine, while the high-level controller is deployed in a nearby Kubernetes-based edge cluster. Communication between the robot and the edge is enabled via a 5G New Radio (NR) Standalone (SA) network. The chosen controller is a Model Predictive Controller (MPC), which generates control actions to allow the robot to navigate seamlessly through the mining environment. A human operator selects waypoints for the aerial robot, and the MPC generates smooth, collision-free paths for autonomous executions. The proposed 5G edge-based closed-loop system is evaluated in a real industrial setting and demonstrates the potential of edge-controlled robotic systems toward time-critical, safe and efficient future deployments.

</details>

---

### [[20_Research/Papers/具身智能/SoftPINCH_EMG-Driven_Soft_Exoskeleton_Assistance_for_Finger_Flexion_and_Grasping|SoftPINCH: EMG-Driven Soft Exoskeleton Assistance for Finger Flexion and Grasping]]

![[assets/2606.04776_figure.png|800]]

- **arXiv**: [2606.04776](https://arxiv.org/abs/2606.04776)
- **PDF**: https://arxiv.org/pdf/2606.04776
- **详细分析**: [[20_Research/Papers/具身智能/SoftPINCH_EMG-Driven_Soft_Exoskeleton_Assistance_for_Finger_Flexion_and_Grasping|SoftPINCH: EMG-Driven Soft Exoskeleton Assistance for Finger Flexion and Grasping]]
- **作者**: Nicklas Nikolaj Grønvall, Magnus Malthe Sigsgaard Nielsen, Xiaofeng Xiong, Saravana Prashanth Murali Babu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《SoftPINCH: EMG-Driven Soft Exoskeleton Assistance for Finger Flexion and Grasping》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：WaveNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Surface electromyography (sEMG) provides a non-invasive interface for detecting hand-movement intention and controlling wearable assistive devices. However, reliable EMG-driven hand assistance remains challenging because EMG signals are affected by noise, motion artifacts, electrode placement, muscle fatigue, and inter-subject variability. At the same time, many hand exoskeletons remain mechanically restrictive or bulky, limiting comfort and natural hand motion. This work presents SoftPINCH, an EMG-driven soft wearable exoskeleton for thumb-index finger flexion and pinch grasp assistance. The system combines a tendon-driven soft exoskeleton, fingertip magnetic contact sensing, and neural EMG decoding for intention-based assistance. Surface EMG was recorded from forearm muscles during index and thumb movements, and three subject-independent decoding architectures were evaluated: LSTM, CNN+LSTM, and CNN+LSTM with attention. The CNN+LSTM and CNN+LSTM-attention models both achieved 99.4% LOSO test accuracy, outperforming the standalone LSTM, which reached 97.8%. However, the attention mechanism did not provide a significant improvement over CNN+LSTM, indicating that CNN-based feature extraction was sufficient for robust EMG representation. The CNN+LSTM model was therefore selected for real-time deployment due to its high accuracy and lower architectural complexity. Functional evaluation showed that active exoskeleton assistance reduced muscular effort during isolated finger flexion and object grasping. During weighted grasping, assistance reduced muscular effort across all tested loads, with a 92.6% reduction at the highest load. These results demonstrate the potential of SoftPINCH for intuitive, low-effort pinch assistance using real-time EMG-driven soft robotic control.

</details>

---

### [[20_Research/Papers/机器人/CADENCE_Predicting_Realized_MAPF_Execution_Time_Beyond_Sum_of_Costs|CADENCE: Predicting Realized MAPF Execution Time Beyond Sum of Costs]]

![[assets/2606.04746_figure.png|800]]

- **arXiv**: [2606.04746](https://arxiv.org/abs/2606.04746)
- **PDF**: https://arxiv.org/pdf/2606.04746
- **详细分析**: [[20_Research/Papers/机器人/CADENCE_Predicting_Realized_MAPF_Execution_Time_Beyond_Sum_of_Costs|CADENCE: Predicting Realized MAPF Execution Time Beyond Sum of Costs]]
- **作者**: Abhishek S, Badrikanath Praharaj, Sreeram MV
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《CADENCE: Predicting Realized MAPF Execution Time Beyond Sum of Costs》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-Agent Path Finding (MAPF) algorithms are increasingly used to plan motion for robot teams in industrial warehouses and robotic shared workspaces, but standard MAPF algorithm evaluation metrics, such as Sum of Costs (SoC), makespan, and planner runtime, can obscure how planner choices translate into realistic execution performance. We present CADENCE (Coordination and Action-Driven Estimation for Networked Continuous Execution), a hardware study of this evaluation gap on a fixed 7 by 7 workcell with seven differential drive robots, asking which features available before execution can best predict final wall-clock completion time. We compare SoC, total planned travel cost, primitive motion burden (how much basic motion the plan requires, such as makespan, turns, consecutive moves, and start-stop transitions), and interaction aware coordination structure (how much inter-robot coordination the plan induces, such as dependency links, interacting robot pairs, dependency depth, and crowding exposure). To test this, we generate 120 plans across 15 scenarios -- 5 Empty, 5 Medium Random, and 5 Bottleneck and execute each plan four times, yielding a 480 trial hardware corpus. Using both a scenario-held -- out ridge model and a trial-level mixed-effects model, we find that SoC alone is informative but incomplete, while primitive motion burden gives the strongest improvement, reducing held out error by about 48.6%-59.8% in MAE and 44.2%-61.4% in RMSE relative to SoC-only models. Interaction-aware coordination features add smaller, less uniform gains, most clearly in the mixed-effects analysis. Across both models and uncertainty checks, primitive motion burden is the most reliable additional signal beyond SoC, suggesting that much of the execution time gap is already visible in the offline plan before any robot starts moving.

</details>

---

### [[20_Research/Papers/机器人/BPDA-GMM_Bayesian_Probabilistic_Data_Association_via_Gaussian_Mixture_Models_for_Semantic_SLAM|BPDA-GMM: Bayesian Probabilistic Data Association via Gaussian Mixture Models for Semantic SLAM]]

![[assets/2606.04618_figure.png|800]]

- **arXiv**: [2606.04618](https://arxiv.org/abs/2606.04618)
- **PDF**: https://arxiv.org/pdf/2606.04618
- **详细分析**: [[20_Research/Papers/机器人/BPDA-GMM_Bayesian_Probabilistic_Data_Association_via_Gaussian_Mixture_Models_for_Semantic_SLAM|BPDA-GMM: Bayesian Probabilistic Data Association via Gaussian Mixture Models for Semantic SLAM]]
- **作者**: Thanh Nguyen Canh, Haolan Zhang, Xiem HoangVan, Antonio Sgorbissa, Nak Young Chong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《BPDA-GMM: Bayesian Probabilistic Data Association via Gaussian Mixture Models for Semantic SLAM》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Probabilistic data association (PDA) improves semantic SLAM in perceptually aliased scenes, but existing methods often assume a fixed landmark set, recompute association weights as the map grows, or rely on hand-tuned null-hypothesis weights. To address these limitations, we propose \textbf{BPDA-GMM}, an online Bayesian PDA framework for semantic SLAM with a growing object-level map. BPDA-GMM uses a Dirichlet-process prior to induce a Chinese Restaurant Process (CRP) association model, where accumulated evidence favors existing landmarks, and the concentration parameter assigns probability mass to new landmarks. For each semantic detection, plausible candidates are selected by a joint semantic-geometric gate, CRP-weighted association probabilities are computed, and object landmarks are updated as semantic Gaussians in closed form. The resulting landmark set forms a Gaussian mixture model, and its dominant component is passed to the back-end as a max-mixture semantic factor. When association weights are inconclusive, an ambiguity-triggered $\alpha$-divergence tempering step improves discrimination. Finally, a decoupled back-end zeroes the pose Jacobian of semantic factors, allowing noisy detections to refine landmarks without directly perturbing the trajectory. Experiments in simulation and on a real indoor dataset demonstrate improved trajectory accuracy, semantic mapping quality, and robustness to perceptual aliasing and classifier errors over state-of-the-art baselines. Code and video are publicly available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/MineXplore_An_Open-Source_Reinforcement_Learning_Exploration_Benchmark_for_GNSS-Denied_Underground_Environment|MineXplore: An Open-Source Reinforcement Learning Exploration Benchmark for GNSS-Denied Underground Environment]]

![[assets/2606.04569_figure.png|800]]

- **arXiv**: [2606.04569](https://arxiv.org/abs/2606.04569)
- **PDF**: https://arxiv.org/pdf/2606.04569
- **详细分析**: [[20_Research/Papers/具身智能/MineXplore_An_Open-Source_Reinforcement_Learning_Exploration_Benchmark_for_GNSS-Denied_Underground_Environment|MineXplore: An Open-Source Reinforcement Learning Exploration Benchmark for GNSS-Denied Underground Environment]]
- **作者**: Abhishek S, Badrikanath Praharaj, Sreeram MV
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，强化学习 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《MineXplore: An Open-Source Reinforcement Learning Exploration Benchmark for GNSS-Denied Underground Environment》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underground mines present extreme conditions for autonomous robot navigation: GPS is denied, lighting is degraded, and tunnel topology is loop-rich and non-convex. Simulation benchmarks grounded in real production-mine geometry and compatible with GPU-accelerated learning pipelines do not yet exist in the open-source ecosystem. We present MineXplore, an open-source MuJoCo-based navigation benchmark derived from the Leung et al. 2017 Chilean underground copper mine dataset. The environment reconstructs a 104,423 sq.m tunnel network through an six-stage contour-to-MJCF pipeline incorporating octagonal wall cross-sections, LiDAR-sourced jagged wall geometry, three terrain friction zones, a global 5 degree incline, and periodic spot lighting. Geometric fidelity is validated at an Intersection over Union (IoU) of 0.9538 against the source survey map, and surface texture similarity scores 79.4% across six structural dimensions. A single-agent PPO baseline trained via RLlib across five independent random seeds achieves a best rolling coverage of 88.89% (3 of 5 seeds reaching the 90% coverage target), confirming that MineXplore supports stable and reproducible policy learning under realistic underground sensing and topology.

</details>

---

### [[20_Research/Papers/具身智能/MAD_Mapping-Aware_World_Models_for_Agile_Quadrotor_Flight|MAD: Mapping-Aware World Models for Agile Quadrotor Flight]]

![[assets/2606.04534_figure.png|800]]

- **arXiv**: [2606.04534](https://arxiv.org/abs/2606.04534)
- **PDF**: https://arxiv.org/pdf/2606.04534
- **详细分析**: [[20_Research/Papers/具身智能/MAD_Mapping-Aware_World_Models_for_Agile_Quadrotor_Flight|MAD: Mapping-Aware World Models for Agile Quadrotor Flight]]
- **作者**: Xinhong Zhang, Runqing Wang, Yunfan Ren, Ding Yu, Boyu Zhou, Jian Sun, Fang Deng, Jie Chen, Gang Wang
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.5（加权：大模型 0.1，世界模型 1.4）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《MAD: Mapping-Aware World Models for Agile Quadrotor Flight》归入 世界模型、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MBRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agile quadrotor flight in cluttered scenes requires more than a reactive mapping from a depth image to a control command: the vehicle must remember which regions have been observed, infer nearby occupied space, and act under partial visibility and tight latency. In this paper, we present Mapping-Aware Dreamer (MAD), a geometry-aware world model for vision-based quadrotor flight. Instead of using raw-image reconstruction as the main self-supervised objective, MAD learns recurrent latent dynamics that reconstruct robocentric occupancy and visibility grid maps together with proprioceptive states. This design forces the latent state to encode local geometry, visibility history, and ego-motion in a form that is directly relevant to collision avoidance. MAD is trained in DiffAero using a GPU-parallel map-construction module that provides high-throughput supervision for occupancy and visibility. The learned representation is used in three policy-learning modes: imagination-based MAD-Dreamer and feature-extractor variants based on PPO and SHAC. Across visual navigation and racing tasks, MAD-based agents achieve higher success rates, faster flight, and better cross-task transfer than corresponding vision-only baselines. The model also produces interpretable map predictions and accurate ego-motion estimates from depth observations. We further deploy the learned policy on a physical quadrotor with an Intel RealSense D435i and demonstrate safe indoor and outdoor flight under limited sensing, reaching 9.66 m/s in simulation and 5.05 m/s in real-world forest experiments. These results show that mapping-aware world models provide a practical middle ground between modular aerial navigation and end-to-end learning.

</details>

---

### [[20_Research/Papers/强化学习/OSCAR_Omni-Embodiment_Skeleton-Conditioned_World_Action_Model_for_Robotics|OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics]]

![[assets/2606.04463_figure.png|800]]

- **arXiv**: [2606.04463](https://arxiv.org/abs/2606.04463)
- **PDF**: https://arxiv.org/pdf/2606.04463
- **详细分析**: [[20_Research/Papers/强化学习/OSCAR_Omni-Embodiment_Skeleton-Conditioned_World_Action_Model_for_Robotics|OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics]]
- **作者**: Zhuoyuan Wu, Jun Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，世界模型 0.4，机器人 1.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《OSCAR: Omni-Embodiment Skeleton-Conditioned World Action Model for Robotics》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AdaWorld, Ctrl-World, EWMBench, GE-Sim, IRASim, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present OSCAR, a precise action-conditioned video world model that generalizes across different robot embodiments and enables robot policy evaluation. Existing video world models face three main challenges for real-world robot evaluation: limited scenario diversity in current robot training datasets, imprecise action following, and poor generalization across embodiments for broad adoption. We tackle these challenges from two perspectives. At its core is a large-scale standardized data pipeline that curates, filters, and deduplicates broad robotics and egocentric human datasets, yielding a clean joint-training dataset that spans diverse tasks, scenarios, actions, and robot embodiments. To condition the video model, we adopt 2D kinematic skeleton rendering as a unified conditioning representation that generalizes across different robot arms or even human hands. We finetune the Cosmos-Predict2.5-2B model on a single GH200 GPU. Our model achieves significant improvement on action following, appearance quality, and motion consistency, compared to existing baselines, which either have a much larger model size or require more GPUs. We further deploy OSCAR to evaluate robot policies from RoboArena. Extensive experiments demonstrate the significant correlation between our virtual policy evaluation in OSCAR and real-world evaluation, paving the way for the future where robot policies can be purely evaluated in virtual generated worlds.

</details>

---

### [[20_Research/Papers/机器人/Think_Fast_and_Far_Long-Horizon_Online_POMDP_Planning_via_Rapid_State_Sampling|Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling]]

![[assets/2606.04355_figure.jpg|800]]

- **arXiv**: [2606.04355](https://arxiv.org/abs/2606.04355)
- **PDF**: https://arxiv.org/pdf/2606.04355
- **详细分析**: [[20_Research/Papers/机器人/Think_Fast_and_Far_Long-Horizon_Online_POMDP_Planning_via_Rapid_State_Sampling|Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling]]
- **作者**: Yuanchu Liang, Edward Kim, J. Arden Knoll, Wil Thomason, Zachary Kingston, Lydia E. Kavraki, Hanna Kurniawati
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，强化学习 0.8，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Think Fast and Far: Long-Horizon Online POMDP Planning via Rapid State Sampling》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Partially Observable Markov Decision Processes (POMDPs) are a general and principled framework for motion planning under uncertainty. Despite tremendous improvement in the scalability of POMDP solvers, long-horizon POMDPs remain difficult to solve. To alleviate the difficulty, this paper proposes a new approximate online POMDP solver, called Reference-Based Online POMDP Planning via Rapid State Space Sampling (ROP-RAS3). ROP-RAS3 uses novel extremely fast sampling-based motion planning techniques to sample the state space and generate a diverse set of macro actions online, which are then used to bias belief-space sampling and infer high-quality policies without requiring exhaustive enumeration of the action space -- a fundamental constraint for modern online POMDP solvers. ROP-RAS3 converges to a near-optimal reference-based solution at a rate that depends on the number of sampled actions, rather than the size of the action space. ROP-RAS3 is evaluated on various long-horizon POMDPs with up to 3000 lookahead steps and 35-dimensional state spaces, where the state, action and observation spaces can be continuous, discrete, or a hybrid of discrete and continuous. Although the reference-based optimal solution may not be the same as the optimal POMDP solution, empirical results indicate that in all of these problems, in terms of success rate, ROP-RAS3 outperforms other state-of-the-art methods by up to multiple folds. We also demonstrate the capability of our approach on a physical robot demonstration. This work extends the theory and empirical results of our ISRR24 paper. Code can be found at \texttt{ this https URL }.

</details>

---

### [[20_Research/Papers/具身智能/What_Are_We_Actually_Benchmarking_in_Robot_Manipulation|What Are We Actually Benchmarking in Robot Manipulation?]]

![[assets/2606.04233_figure.png|800]]

- **arXiv**: [2606.04233](https://arxiv.org/abs/2606.04233)
- **PDF**: https://arxiv.org/pdf/2606.04233
- **详细分析**: [[20_Research/Papers/具身智能/What_Are_We_Actually_Benchmarking_in_Robot_Manipulation|What Are We Actually Benchmarking in Robot Manipulation?]]
- **作者**: Tianchong Jiang, Xiangshan Tan, Samuel Wheeler, Luzhe Sun, Tewodros W. Ayalew, Matthew Walter
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《What Are We Actually Benchmarking in Robot Manipulation?》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DeeR-VLA, Foundation-VLA, ImageNet, MMaDA-VLA, OpenVLA, SimVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robotics benchmark score measures success under one fixed evaluation setup, yet is routinely treated as evidence of general manipulation capability. We identify four failure modes, each of which weakens or invalidates a benchmark's role as a valid proxy for that capability: shortcut solvability, lack of statistical significance, creeping overfitting, and data-source dependence. We propose one diagnostic per failure mode. We audit LIBERO, CALVIN, SimplerEnv, RoboCasa, and RoboTwin 2.0 under these diagnostics. LIBERO and CALVIN fail multiple diagnostics. RoboCasa and RoboTwin 2.0 fail fewer, despite appearing far less often in recent progress claims. On LIBERO, a 0.09B probe with no language encoder scores at or near reported SOTA, and most reported gains are not provably statistically significant. On CALVIN, randomizing block poses within the training range drops performance for every tested policy. We release the four diagnostics with reference implementations for authors and reviewers to apply before treating a benchmark score as evidence of progress. Code and artifacts are available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/DLO-Lab_Benchmarking_Deformable_Linear_Object_Manipulations_with_Differentiable_Physics|DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics]]

![[assets/2606.04206_figure.png|800]]

- **arXiv**: [2606.04206](https://arxiv.org/abs/2606.04206)
- **PDF**: https://arxiv.org/pdf/2606.04206
- **详细分析**: [[20_Research/Papers/具身智能/DLO-Lab_Benchmarking_Deformable_Linear_Object_Manipulations_with_Differentiable_Physics|DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics]]
- **作者**: Junyi Cao, Yian Wang, Ziyan Xiong, Chunru Lin, Zhehuan Chen, Chuang Gan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《DLO-Lab: Benchmarking Deformable Linear Object Manipulations with Differentiable Physics》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DaXBench, DiffSim, FO-MBRL, MFRL, Real-World, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We address the challenge of enabling robots to manipulate deformable linear objects (DLOs), such as ropes, cables, and rubber bands. Prior work has primarily focused on narrow, task-specific problems, often relying on real-world demonstrations or handcrafted heuristics. Such approaches, however, struggle to scale to the wide variety of materials and tasks encountered in practice, and collecting sufficiently diverse real-world data is often impractical. Additionally, existing simulation environments offer limited support for the broad spectrum of material behaviors necessary for generalizable DLO manipulation. To overcome these limitations, we introduce a differentiable simulator explicitly designed for versatile DLO manipulation. Our simulator models a wide range of material properties-including (in)extensibility, elasticity, bending plasticity, and complex interactions with other objects-providing a robust foundation for learning and evaluating manipulation skills. Building on this simulator, we propose a benchmark suite of representative tasks that highlight the unique challenges of DLO manipulation. The successful execution of these tasks is often hindered by the topological complexity and grasp sensitivity inherent to DLOs. Therefore, we introduce a specialized DLO agent that explicitly manages these challenges by proposing strategic grasping points and decomposing long-horizon tasks to maximize control authority. Finally, we evaluate various policy-learning algorithms using our framework, alongside sim-to-real transfer experiments, demonstrating our platform's potential to advance DLO manipulation.

</details>

---

### [[20_Research/Papers/具身智能/Affordance2Action_Task-Conditioned_Scene-level_Affordance_Grounding_for_Real-Time_Manipulation|Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation]]

![[assets/2606.04172_figure.png|800]]

- **arXiv**: [2606.04172](https://arxiv.org/abs/2606.04172)
- **PDF**: https://arxiv.org/pdf/2606.04172
- **详细分析**: [[20_Research/Papers/具身智能/Affordance2Action_Task-Conditioned_Scene-level_Affordance_Grounding_for_Real-Time_Manipulation|Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation]]
- **作者**: Litao Liu, Yifan Han, Pengfei Yi, Wenbo Yu, Hanqing Wang, Haoran Du, Enze Yuan, Zilin Yuan, Ruiding Feng, Michael Liu, Qi Zhang, Jingjin Yu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.6，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Affordance2Action: Task-Conditioned Scene-level Affordance Grounding for Real-Time Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：A2A-Bench, CoA-VLA, RAGNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task-conditioned manipulation requires grounding instructions to task-relevant functional parts rather than object categories. This setting is scene-dependent and often one-to-many in cluttered scenes: the same object may afford different interactions across tasks, while a single task may correspond to either one functional region or multiple valid functional regions, depending on the scene layout. Existing affordance datasets and benchmarks remain misaligned with this setting, as they typically focus on grasping or object-level affordances, rely on synthetic scenes, or assume a single instruction-region correspondence. We present Affordance2Action (A2A), a benchmark-centered learning framework for scene-level, task-conditioned part affordance grounding. At its core is A2A-Bench, a manipulation-oriented benchmark that covers both single-region and multi-region instruction correspondences in everyday scenes, with the latter highlighting the ambiguity and diversity of affordance grounding in realistic multi-object environments. To construct it at scale, we build A2A-AffordGen, an agent-assisted annotation pipeline that combines language-model filtering, interactive part segmentation, instance-level mask-out refinement, task-reasoning instruction generation, and human verification. A2A-Bench's supervision further supports diverse downstream applications, with real-time affordance grounding and affordance-conditioned manipulation policies as two representative examples. Experiments show that A2A exposes substantial gaps in generic segmentation, VLM-based grounding, and affordance distillation baselines, while improving task-level localization and providing useful spatial priors for downstream manipulation. All datasets and code will be publicly released to promote open research.

</details>

---

### [[20_Research/Papers/机器人/Multi-Agent_Next-Best-View_Optimization_for_Risk-Averse_Planning|Multi-Agent Next-Best-View Optimization for Risk-Averse Planning]]

![[assets/2606.04158_figure.png|800]]

- **arXiv**: [2606.04158](https://arxiv.org/abs/2606.04158)
- **PDF**: https://arxiv.org/pdf/2606.04158
- **详细分析**: [[20_Research/Papers/机器人/Multi-Agent_Next-Best-View_Optimization_for_Risk-Averse_Planning|Multi-Agent Next-Best-View Optimization for Risk-Averse Planning]]
- **作者**: Amirhossein Mollaei Khass, Vivek Pandey, Guangyi Liu, Athanasios Cosse, Emrah Bayrak, Nader Motee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.4，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Multi-Agent Next-Best-View Optimization for Risk-Averse Planning》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-agent Next-Best-View (NBV) selection for safe path planning in uncertain and unknown environments requires informative, safety-aware, and efficient coordination. Centralized approaches rely on sharing raw sensor data or significant communication overhead, resulting in limited scalability. We propose a distributed, risk-aware multi-agent NBV framework in which each robot maintains a private local 3D Gaussian Splatting map and the team jointly maximizes expected information gain (EIG) restricted to masked zones along planned trajectories. The resulting distributed objective is solved by Consensus ADMM (C-ADMM) over a communication graph, with each robot exchanging only candidate viewpoints, planned trajectory descriptors, and scalar EIG contributions. Collision risk along each trajectory is modeled via Average Value-at-Risk (AV@R) over the local 3DGS map and used both to shape the masking radius and to score planned paths. Experiments in Gibson environments at multiple team sizes show that the distributed formulation approaches the centralized baseline in mapping quality and trajectory safety while reducing communication by orders of magnitude.

</details>

---

### [[20_Research/Papers/世界模型/CLAW_Learning_Continuous_Latent_Action_World_Models_via_Adversarial_Latent_Regularization|CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization]]

![[assets/2606.04130_figure.png|800]]

- **arXiv**: [2606.04130](https://arxiv.org/abs/2606.04130)
- **PDF**: https://arxiv.org/pdf/2606.04130
- **详细分析**: [[20_Research/Papers/世界模型/CLAW_Learning_Continuous_Latent_Action_World_Models_via_Adversarial_Latent_Regularization|CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization]]
- **作者**: Tewodros Ayalew, Matthew Jeung, Samuel Wheeler, Xiao Zhang, Andre de la Cruz Arce, Kaylene Stocking, Michael Maire, Matthew R. Walter
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《CLAW: Learning Continuous Latent Action World Models via Adversarial Latent Regularization》归入 世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We introduce CLAW, a fully end-to-end self-supervised framework for learning a world model jointly with continuous latent action representations directly from action-free videos. Our approach leverages adversarial latent regularization and diffusion-based video generation to capture structured and semantically meaningful action representations while modeling rich, predictive environment dynamics, without relying on any action labels or annotations. By simultaneously training the Latent Action Model and world model, CLAW learns to reason about how inferred actions induce environment transitions from visual observations alone. We show that the resulting latent action world model supports both imitation learning from observation and goal-directed planning. In imitation learning, latent actions extracted from raw videos enable behavior cloning. For planning, CLAW generates sequences of latent actions and maps them to executable actions to reach desired goals. Extensive experiments across diverse tasks and embodiments demonstrate that CLAW produces semantically meaningful latent action representations, supports effective action transfer, and enables planning and imitation from observation, outperforming existing methods.

</details>

---

### [[20_Research/Papers/具身智能/PointAction_3D_Points_as_Universal_Action_Representations_for_Robot_Control|PointAction: 3D Points as Universal Action Representations for Robot Control]]

![[assets/2606.03943_figure.png|800]]

- **arXiv**: [2606.03943](https://arxiv.org/abs/2606.03943)
- **PDF**: https://arxiv.org/pdf/2606.03943
- **详细分析**: [[20_Research/Papers/具身智能/PointAction_3D_Points_as_Universal_Action_Representations_for_Robot_Control|PointAction: 3D Points as Universal Action Representations for Robot Control]]
- **作者**: Mutian Tong, Han Jiang, Qiao Feng, Lingjie Liu, Jiatao Gu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《PointAction: 3D Points as Universal Action Representations for Robot Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DreamVLA, Real-World, RynnVLA, UniVLA, WorldVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Video-Action Models (VAMs) leverage the broad visual dynamics captured by pre-trained video diffusion models, offering a promising path toward generalizable robot manipulation. However, RGB-only video rollouts are not directly actionable: they leave metric 3D motion, contact geometry, and fine-grained spatial constraints under-specified, making action grounding ambiguous. Meanwhile, scaling action supervision across diverse tasks and embodiments remains costly. We present PointAction, a framework that bridges video predictions to robot actions through explicit point-based 4D modeling. PointAction fine-tunes a foundation video generation model to jointly predict future RGB frames and dynamic 3D pointmaps, producing temporally consistent 3D motion of task-relevant scene geometry. These point dynamics serve as a structured, embodiment-agnostic action interface, which a diffusion-based action decoder maps to executable robot actions. By using metric 3D point dynamics as the interface between video prediction and control, PointAction reduces the ambiguity of RGB-only action grounding and supports transfer across tasks and embodiments with limited action supervision. Experiments show that PointAction achieves state-of-the-art 4D generation quality on robot scenes, outperforms existing baselines in simulation, and generalizes to two real robot arms unseen during pretraining.

</details>

---
