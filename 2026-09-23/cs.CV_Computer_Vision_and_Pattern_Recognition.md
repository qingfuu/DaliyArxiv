# cs.CV | Computer Vision and Pattern Recognition | 2026-09-23

#arxiv #ComputerScience

**论文数**: 9

### [[20_Research/Papers/强化学习/DreamStream_Towards_Policy-Oriented_Generative_Simulation_for_End-to-End_Driving|DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving]]

![[assets/2609.26792_figure.png|800]]

- **arXiv**: [2609.26792](https://arxiv.org/abs/2609.26792)
- **PDF**: https://arxiv.org/pdf/2609.26792
- **详细分析**: [[20_Research/Papers/强化学习/DreamStream_Towards_Policy-Oriented_Generative_Simulation_for_End-to-End_Driving|DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving]]
- **作者**: Ziyang Leng, Sicheng Mo, Seth Z. Zhao, Haoyuan Cai, Yu Zeng, Rowan McAllister, Bolei Zhou
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: RL, ComputerVision, Security

#### 研究背景与动机

《DreamStream: Towards Policy-Oriented Generative Simulation for End-to-End Driving》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Faithfully evaluating end-to-end driving policies in simulation requires observations that are not merely photo-realistic, but preserve the scene features a policy relies on to make decisions. Existing platforms, however, exhibit a sim-to-real visual gap that corrupts policy perception, undermining their ability to assess a policy's closed-loop decision-making. To this end, we propose DreamStream, a generative, closed-loop simulator that achieves policy-oriented fidelity using a simulator-grounded autoregressive video model. Our video model is distilled from a large pretrained video model via traffic layout guidance, varying visual appearance while preserving policy-relevant features such as scenario layout and the temporal consistency of dynamic objects. We further observe that perceptual metrics like FID misrank how well these features are preserved. To tackle this, we introduce FD$\pi$, a new multi-representation metric that measures the sim-to-real gap as the Fréchet distance over scene-context features from public E2E policies. Under FD$\pi$, DreamStream improves over the strongest prior closed-loop simulator by $1.6\times$ on nuScenes and $4.7\times$ on NAVSIM, and induces the least perturbation to policy's perceptual observability. Based on DreamStream, we construct Navhard-CL benchmark, which turns non-reactive real-world benchmark NAVSIM into interactive testing environments with adversarial driving behaviors and weather variations. This benchmark exposes many failure modes of driving policies, such as scorer bias and lack of recovery behaviors, that prior closed-loop benchmarks overlook. Code and data are available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Beyond_End-Task_Success_How_to_Audit_Visual_Experience_Retrieval_in_Robotics|Beyond End-Task Success: How to Audit Visual Experience Retrieval in Robotics]]

![[assets/2609.26567_first_page.png|800]]

- **arXiv**: [2609.26567](https://arxiv.org/abs/2609.26567)
- **PDF**: https://arxiv.org/pdf/2609.26567
- **详细分析**: [[20_Research/Papers/强化学习/Beyond_End-Task_Success_How_to_Audit_Visual_Experience_Retrieval_in_Robotics|Beyond End-Task Success: How to Audit Visual Experience Retrieval in Robotics]]
- **作者**: Eshika Pathak, Leela Krishna
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Beyond End-Task Success: How to Audit Visual Experience Retrieval in Robotics》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots that store past experiences must select which one to reuse in a new scene. Most systems select by visual similarity, and most evaluations report only the success of the selected experience. That number does not show whether the selection was good: a rule can score well by repeatedly using one broadly transferable experience, or poorly because its preferred experience is weak. Since robots increasingly adapt by reuse rather than retraining, a score that describes the library rather than the rule misleads what the field builds next. We contribute an audit methodology: execute every stored experience in every query scene, over two manipulation tasks, three reuse mechanisms, and libraries of $K=3$, $10$, and $50$. Because every alternative's outcome is known, a score can be traced to per-scene selection or to library quality. The audited rules select by nearest-neighbor distance in five visual embeddings, from raw pixels to CLIP. (1) One fixed experience, chosen with hindsight, captures 30-58% of the gap between random selection and an oracle; per-scene selection competes for the remaining 0.07-0.15 in success rate. (2) At $K\ge10$, visual rules concentrate on one experience 1.5-3 times more than the oracle does, and their scores then follow that experience's quality. (3) Wherever a rule differs significantly from a shuffle that keeps its selection rates but pairs them with scenes at random, the rule is worse, for every learned image policy. (4) Visual distance predicts well whether a given pair will succeed (AUROC up to 0.96), yet ranks the candidates within one scene no better than chance for four of five embeddings at $K=50$ (AUROC 0.45-0.52). Exhaustive execution is usually infeasible, so the audit reduces to two cheap reports any study can give: the distribution of selected experiences, and the success of the best single experience in hindsight.

</details>

---

### [[20_Research/Papers/强化学习/Sample,_Simulate,_Select_Physics-in-the-Loop_Text-to-Motion_for_Humanoids_Without_Training|Sample, Simulate, Select: Physics-in-the-Loop Text-to-Motion for Humanoids Without Training]]

![[assets/2609.26420_figure.jpg|800]]

- **arXiv**: [2609.26420](https://arxiv.org/abs/2609.26420)
- **PDF**: https://arxiv.org/pdf/2609.26420
- **详细分析**: [[20_Research/Papers/强化学习/Sample,_Simulate,_Select_Physics-in-the-Loop_Text-to-Motion_for_Humanoids_Without_Training|Sample, Simulate, Select: Physics-in-the-Loop Text-to-Motion for Humanoids Without Training]]
- **作者**: Raphael Memmesheimer, Sven Behnke
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Sample, Simulate, Select: Physics-in-the-Loop Text-to-Motion for Humanoids Without Training》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Text-to-motion models generate plausible human motion but do not model a robot's dynamics; whole-body tracking controllers execute robot references reliably but cannot replan an infeasible one. Recent language-to-humanoid systems bridge this gap by training. We measure how much of the gap closes with no training at all, by putting the deployment controller itself in the loop. Sample-simulate-select (S$^3$) draws $N$ motions per prompt from a frozen text-to-motion model, retargets each to a Unitree G1 by direction-matching inverse kinematics, rolls all of them out under full rigid-body dynamics with the pretrained SONIC tracking policy, and keeps the candidate the policy executed best. Because the verifier is the deterministic simulator itself, S$^3$ attains the any-of-$N$ ceiling by construction; what we measure is where that ceiling lies and what falls short of it. On 200 stratified HumanML3D test prompts with $N=8$, upright execution rises from 83.5% to 89.5% and hardware-gate passes from 33 to 85; on the complete test split (4,184 prompts) it rises from 80.5% to 89.5%. A kinematic verifier that predicts falls well (AUROC 0.90) recovers only a quarter of this gain: ranking a prompt's own candidates is harder than classifying the population. What selection cannot fix is one class, prompts that lower the pelvis, which a generator trained on retargeted robot data does execute. We further score the semantic fidelity of the executed motion with the standard text-motion evaluator, with a real-mocap control that attributes the loss to the robot projection, ablate the retargeter against GMR (complementary failures: the any-of-8 ceiling rises to 95.0% over both), and execute all 177 gate-selected clips on the real G1: every one completes standing, with hardware tracking error matching simulation ($r=0.94$).

</details>

---

### [[20_Research/Papers/强化学习/ForeDrive_Foresight-Guided_End-to-End_Autonomous_Driving_with_a_Planning-Relevant_Latent_World_Model|ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model]]

![[assets/2609.26299_figure.png|800]]

- **arXiv**: [2609.26299](https://arxiv.org/abs/2609.26299)
- **PDF**: https://arxiv.org/pdf/2609.26299
- **详细分析**: [[20_Research/Papers/强化学习/ForeDrive_Foresight-Guided_End-to-End_Autonomous_Driving_with_a_Planning-Relevant_Latent_World_Model|ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model]]
- **作者**: Sinuo Wang, Zichong Gu, Yuhan Huang, Wenxin Wen, Xun Yang, Yiqing Zhang, Xingyu Zhang, Ningyu Che, Jie Ling, Qiankun Yu, Wei Liu, Jing Xu...
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.2（加权：强化学习 0.2，世界模型 1）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《ForeDrive: Foresight-Guided End-to-End Autonomous Driving with a Planning-Relevant Latent World Model》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DriveVLA, ReCogDrive-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Existing latent world models are typically optimized for future predictability, yet the resulting representations are not necessarily useful for planning in autonomous driving. Predictions are commonly used for pretraining or auxiliary supervision rather than as direct conditioning signals for trajectory generation. We propose ForeDrive, which learns a planning-relevant latent representation and couples it asymmetrically to a Diffusion Transformer (DiT) planner. The planner consumes multi-horizon latent future representations learned with a JEPA-style world model; planning gradients update the shared online encoder, while stop-gradient routing trains the latent predictor with forecasting losses only. Because predicted futures have varying reliability across horizons and BEV trajectories are misaligned with image tokens, we use gated visual fusion, future-status injection, and Trajectory-Adaptive Bias (TAB) to inject future latents as guidance without overriding the current observation. Trained with pure imitation learning and using only the current front-view image as visual input at inference, ForeDrive attains 89.9 PDMS on NAVSIM v1 and 90.0 one-stage EPDMS on NAVSIM v2, without reinforcement learning or an external trajectory scorer.

</details>

---

### [[20_Research/Papers/具身智能/Metric-Bench_Exploring_In-context_Spatial_Metric_Reasoning_in_VLMs_for_Indoor_Scenes|Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes]]

![[assets/2609.25841_figure.png|800]]

- **arXiv**: [2609.25841](https://arxiv.org/abs/2609.25841)
- **PDF**: https://arxiv.org/pdf/2609.25841
- **详细分析**: [[20_Research/Papers/具身智能/Metric-Bench_Exploring_In-context_Spatial_Metric_Reasoning_in_VLMs_for_Indoor_Scenes|Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes]]
- **作者**: Yuling Xi, Haokai Zhang, Muzhi Zhu, Hao Zhong, Zongze Du, Hengyu Zhao, Chenchen Jing, Yufei Yin, Bin Qin, Yongjie Yang, Zhenbo Luo, Hao Chen...
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.2，机器人 0.2）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Metric-Bench: Exploring In-context Spatial Metric Reasoning in VLMs for Indoor Scenes》归入 具身智能、大模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ERQA, Metric-Bench, ScanNet, VSI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Metric reasoning is a critical and challenging task for Vision Language Models (VLMs), playing a pivotal role in embodied AI tasks such as robotic manipulation and autonomous navigation. However, current spatial reasoning remains bottlenecked by rigid pixel-level supervision; such localized optimization often compromises general multimodal intelligence, triggering performance degradation or catastrophic forgetting of broad reasoning capabilities. To address these limitations, we introduce Metric-Bench, a focused benchmark designed to guide metric-spatial reasoning using contextual information. By incorporating in-image reference objects with known physical dimensions, Metric-Bench guides models to implicitly learn the 2D-to-3D mapping without camera intrinsics. We further present MetricReasoner, a task-adapted reinforcement fine-tuning recipe for reference-grounded metric reasoning, using structured prompts and verifiable numerical rewards. Extensive experiments on Metric-Bench demonstrate that our approach significantly enhances spatial metric understanding, outperforming existing and even larger proprietary models by 43.1\%, while improving downstream embodied performance over a spatial-specialized counterpart by 30.4\% on RoboSpatial overall accuracy and 9.3\% on ERQA, and additionally delivering consistent gains on general benchmarks (15.9\% on V$\star$Bench, 88.9\% on BLINK), indicating that the proposed adaptation does not necessarily compromise general VLM capabilities.

</details>

---

### [[20_Research/Papers/机器人/Dual_Covariance_Gaussian_Splatting_SLAM_Decoupling_Rendering_and_Registration_for_Robust_Real-Time_Tracking|Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking]]

![[assets/2609.25746_figure.png|800]]

- **arXiv**: [2609.25746](https://arxiv.org/abs/2609.25746)
- **PDF**: https://arxiv.org/pdf/2609.25746
- **详细分析**: [[20_Research/Papers/机器人/Dual_Covariance_Gaussian_Splatting_SLAM_Decoupling_Rendering_and_Registration_for_Robust_Real-Time_Tracking|Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking]]
- **作者**: Edward Beng Wai Tan, Siew-Kei Lam
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Dual Covariance Gaussian Splatting SLAM: Decoupling Rendering and Registration for Robust Real-Time Tracking》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

ICP-based 3D Gaussian Splatting (3DGS) SLAM tracks in real time by registering incoming frames against map Gaussians, using each primitive's covariance for both rendering and registration. These two uses place conflicting demands on one covariance. The mapper shapes it to minimize photometric error, often flattening it against surfaces, while robust registration typically benefits from measurement uncertainty. We propose a dual-covariance parameterization. Each Gaussian keeps a single mean but holds two covariances: a rendering covariance optimized by the mapper, and a tracking covariance derived from an RGB-D sensor noise model. We further use the tracking covariances as Gaussian anchors for image corners, providing constraints in directions where depth geometry is weak. We evaluate on TUM RGB-D, ScanNet, Replica, and two outdoor sequences recorded with a RealSense D435i on wheeled and handheld platforms. We achieve robust tracking performance across multiple scenes and reduced odometry drift, while tracking at $\sim$ 60 FPS.

</details>

---

### [[20_Research/Papers/世界模型/GameDirector_Decoupling_Gameplay_Logic_from_Rendering_for_Player-Configurable_Game_World_Models|GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models]]

![[assets/2609.25652_figure.png|800]]

- **arXiv**: [2609.25652](https://arxiv.org/abs/2609.25652)
- **PDF**: https://arxiv.org/pdf/2609.25652
- **详细分析**: [[20_Research/Papers/世界模型/GameDirector_Decoupling_Gameplay_Logic_from_Rendering_for_Player-Configurable_Game_World_Models|GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models]]
- **作者**: Zijun Lin, Zhiyang Deng, Yuzhe Wu, Bihan Wen, Yeying Jin
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 大模型
- **相关性评分**: 1.1（加权：大模型 0.1，世界模型 1）
- **关联关键词**: Agent, WorldModel, ComputerVision

#### 研究背景与动机

《GameDirector: Decoupling Gameplay Logic from Rendering for Player-Configurable Game World Models》归入 世界模型、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AttackNet, LingBot-World, ResNet, SituationNet, WildWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent game world models support realistic visual simulation and interactive gameplay based on player inputs. However, they typically learn environment dynamics from pixel-level supervision, jointly modeling perception, memory, state transitions, and rendering within a single end-to-end framework. While this design enables open-ended, action-controllable generation, it still falls short of delivering a complete gameplay experience. Games are governed by explicit mechanics, such as health deduction, skill activation, combat rules, and termination conditions. These mechanics depend on precise and consistent state transitions that generative models alone cannot reliably enforce. In contrast, game engines can guarantee such mechanics through hard-coded rules, but provide limited flexibility for player-driven creation. To bridge these paradigms, we introduce GameDirector, the first agentic framework that decouples rule-based gameplay logic from visual rendering. Given player-defined configurations, the framework acts as an intelligent director that interprets visual observations, updates game states, tactically controls NPCs, and enforces gameplay rules. It then translates these decisions into text prompts that guide the video world model to render the resulting gameplay. This separation allows players to configure characters, states, and rules much like a game developer while preserving coherent game mechanics. Experiments on three games, using data collected by our automated gameplay agent, show that GameDirector achieves accurate state tracking, reliable rule following, and improves boss action quality by more than 39.9% over various end-to-end game world model settings. Overall, by externalizing player-controllable game logic, GameDirector establishes a middle ground between hard-coded simulation and generative modeling, enabling more flexible and closed-loop gameplay experiences.

</details>

---

### [[20_Research/Papers/具身智能/MachEmbodied-U0_Unified_Understanding_and_Generation_Model_for_Embodied_Intelligence|MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence]]

![[assets/2609.25627_figure.png|800]]

- **arXiv**: [2609.25627](https://arxiv.org/abs/2609.25627)
- **PDF**: https://arxiv.org/pdf/2609.25627
- **详细分析**: [[20_Research/Papers/具身智能/MachEmbodied-U0_Unified_Understanding_and_Generation_Model_for_Embodied_Intelligence|MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence]]
- **作者**: Haoran Wen, Wenfu Wang, Kunsong Shi, Jingke Wang, Wancheng Feng, Yiren Zhang, Yueran Zhao, Xuancheng Zhang, Nanfei Ye, Xingru Chen, Zhaohong Sun, Chengmin Yang...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.9（加权：具身智能 2.1，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《MachEmbodied-U0: Unified Understanding and Generation Model for Embodied Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BagelVLA, Open-World, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

General-purpose robot control requires models to understand task intent, identify where to interact, capture how the scene evolves, and generate precise actions. Vision-language-action models provide strong semantic priors but typically do not explicitly model scene dynamics, while world-action models couple visual prediction with control without necessarily exposing the task-relevant semantic and spatial structure needed for fine-grained manipulation. We present MachEmbodied-U0 (ME-U0), a unified embodied foundation model connecting understanding and generation experts through a Mixture-of-Transformers architecture. Subtask prediction and affordance grounding guide joint visual-dynamics and action generation via flow matching. Visual dynamics encompass future RGB, depth, surface normals, and optical flow, providing complementary supervision for appearance, geometry, and motion. Multi-rate Rotary Position Encoding (MRPE) aligns visual dynamics with fine-grained control. We pretrain ME-U0 on approximately 4,200 hours of curated demonstrations from robotic datasets and egocentric datasets. Using only the supervision natively available in each downstream benchmark, ME-U0 achieves an average score of 17.66 on the RoboDojo simulation benchmark and average success rates of 99.0\% and 82.5\% on LIBERO and LIBERO-Plus, respectively. We additionally validate ME-U0 on real-world robotic manipulation tasks, demonstrating its effectiveness beyond simulation. Without corresponding downstream supervision, ME-U0 further demonstrates zero-shot subtask prediction, affordance grounding, and visual dynamics on simulated and real-world observations. Overall, ME-U0 combines competitive downstream control performance with transferable task-grounding and visual-dynamics capabilities across simulation and the real world.

</details>

---

### [[20_Research/Papers/机器人/A_Deployment_Study_of_Identity-Gated_Drone_Gesture_Control|A Deployment Study of Identity-Gated Drone Gesture Control]]

![[assets/2609.25511_figure.png|800]]

- **arXiv**: [2609.25511](https://arxiv.org/abs/2609.25511)
- **PDF**: https://arxiv.org/pdf/2609.25511
- **详细分析**: [[20_Research/Papers/机器人/A_Deployment_Study_of_Identity-Gated_Drone_Gesture_Control|A Deployment Study of Identity-Gated Drone Gesture Control]]
- **作者**: Diyari Mohammed Salih, Ilyes Chaabeni, Naima Ait Oufroukh
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Systems

#### 研究背景与动机

《A Deployment Study of Identity-Gated Drone Gesture Control》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MobileFaceNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based gesture control accepts commands from any hand in the camera field of view, which is unsafe in shared indoor spaces. This paper presents IGate, an identity-gated control stack that includes gesture control and face tracking, in which commands are admitted only when an enrolled operator is verified. The system performs few-shot user enrolment from 20 initial face frames, without prior user-specific training: verification compares an embedding of the current face crop against the enrolled template by cosine similarity, while face tracking uses proportional correction. Gesture control is achieved by classifying extracted hand landmarks using an RBF-SVM trained on a custom dataset. Additionally, a hierarchical finite-state machine handles mode selection, default, and fallback behaviours. The approach is tested on a DJI Tello EDU, each component evaluated offline and in-flight across 270 trials (149 flown). Face verification yields a 0.32% offline equal error rate versus 19.3% in-flight. Under hover-locked conditions, the RBF-SVM gesture classifier outperforms the geometric rule (0.850 vs. 0.651 accuracy), with 82% of this gap stemming from the depth channel. All logs and reproduction scripts will be released.

</details>

---
