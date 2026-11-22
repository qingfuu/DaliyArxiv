# cs.CV | Computer Vision and Pattern Recognition | 2026-11-20

#arxiv #ComputerScience

**论文数**: 20

### [[20_Research/Papers/具身智能/Risk-Controlled_Test-Time_Adaptation_for_Vision-Language-Action_Models|Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models]]

![[assets/2611.26438_figure.png|800]]

- **arXiv**: [2611.26438](https://arxiv.org/abs/2611.26438)
- **PDF**: https://arxiv.org/pdf/2611.26438
- **详细分析**: [[20_Research/Papers/具身智能/Risk-Controlled_Test-Time_Adaptation_for_Vision-Language-Action_Models|Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models]]
- **作者**: Zixuan Liu, Hashem Haghbayan, Zizhan Zheng, Siavash Khajavi
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.8，大模型 0.1，机器人 0.2）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Risk-Controlled Test-Time Adaptation for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MiniVLA, OpenVLA, R2-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Retrieval-augmented vision-language-action (VLA) models enable efficient test-time adaptation by leveraging expert demonstrations as additional context without updating model parameters. However, even when retrieved demonstrations are relevant to the current task, the VLA may fail to effectively utilize the retrieved information, ultimately leading to task failure. To address this challenge, we propose R2-VLA, a risk-controlled retrieval-augmented VLA framework that enables reliable test-time adaptation by satisfying a user-specified task success rate requirement with minimal expert assistance. Specifically, R2-VLA learns an uncertainty predictor that estimates the uncertainty of the VLA's predicted actions given the retrieved demonstrations, guiding when to act autonomously or request expert assistance. We further introduce a task-level risk-control procedure that calibrates the uncertainty threshold to satisfy a user-specified task-failure risk requirement. Moreover, R2-VLA continually incorporates expert corrections into its retrieval memory to improve future adaptation while preserving the prescribed task-level risk guarantee. Experiments across three VLA backbones and four LIBERO benchmark suites demonstrate that R2-VLA improves average task success by 9.2--11.2 percentage points, achieving the desired target with fewer expert requests. These results highlight the effectiveness of connecting the usefulness of retrieved demonstrations with task-level risk control to enable successful robotic manipulation.

</details>

---

### [[20_Research/Papers/具身智能/TacInno_Teaching_Vision-Language-Action_Models_the_Contact_Dynamics_Beyond_Vision_and_Action|TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action]]

![[assets/2611.26405_figure.png|800]]

- **arXiv**: [2611.26405](https://arxiv.org/abs/2611.26405)
- **PDF**: https://arxiv.org/pdf/2611.26405
- **详细分析**: [[20_Research/Papers/具身智能/TacInno_Teaching_Vision-Language-Action_Models_the_Contact_Dynamics_Beyond_Vision_and_Action|TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action]]
- **作者**: Weile Li, Yunfan Lou, Muqing Shi, Zihao Zhang, Zhenbiao Huang, Boxian Yao, Xiyu Zhu, Zhibo Pang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.8，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TacInno: Teaching Vision-Language-Action Models the Contact Dynamics Beyond Vision and Action》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, ResTacVLA, TacInno-VLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have recently been equipped with tactile sensing to perceive visually subtle contact events in contact-rich manipulation. However, adding tactile input yields inconsistent gains, and some visuo-tactile VLA models rely little on tactile input, because much of the tactile change, such as the gel deformation during gripper closure, is predictable from visual observations and executed actions. To address this problem, we introduce TacInno, which isolates the contact dynamics that vision and executed actions cannot explain, termed tactile innovation, and uses tactile innovation only as a training target. Specifically, the TacInno tokenizer, conditioned on visual observations and executed actions, compresses the future tactile change into a discrete code, and the policy, TacInno-VLA, learns to predict the code, adding no module for the code at deployment. TacInno-VLA achieves average success rates of 87.5% across six simulation tasks and 70.5% across four real-world tasks, outperforming the strongest visuo-tactile baseline by 10.7 and 9.0 percentage points, respectively. Ablation studies validate the contributions of visual and action conditioning, multi-frame encoding, and auxiliary code prediction. Together, these results demonstrate the effectiveness of tactile innovation as a supervision signal for contact-rich manipulation.

</details>

---

### [[20_Research/Papers/大模型/MixReact_Physics-Based_Reactive_Humanoid_Control_from_Multimodal_Cues_via_a_Discrete-Continuous_Mixture_of_Transformers|MixReact: Physics-Based Reactive Humanoid Control from Multimodal Cues via a Discrete-Continuous Mixture of Transformers]]

![[assets/2611.26218_figure.png|800]]

- **arXiv**: [2611.26218](https://arxiv.org/abs/2611.26218)
- **PDF**: https://arxiv.org/pdf/2611.26218
- **详细分析**: [[20_Research/Papers/大模型/MixReact_Physics-Based_Reactive_Humanoid_Control_from_Multimodal_Cues_via_a_Discrete-Continuous_Mixture_of_Transformers|MixReact: Physics-Based Reactive Humanoid Control from Multimodal Cues via a Discrete-Continuous Mixture of Transformers]]
- **作者**: Bin Li, Xing Zhu, Jingya Wang
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.4，机器人 0.8）
- **关联关键词**: Multimodal, Agent, ComputerVision

#### 研究背景与动机

《MixReact: Physics-Based Reactive Humanoid Control from Multimodal Cues via a Discrete-Continuous Mixture of Transformers》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ReactMotionNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid agents in everyday environments are expected to react to diverse cues as humans do, with semantically appropriate and physically executable behaviors. Existing cue-driven reaction generation methods support only a narrow range of cue modalities and are limited to purely kinematic generation, leaving the resulting reactions susceptible to physical artifacts. To this end, we present MixReact, the first unified framework for physics-based reactive humanoid control from text, audio, and video cues, integrating a Discrete--Continuous Mixture of Transformers (DisCo-MoT) for state prediction with a History-aware Action Transformer (HAT) for physical execution. DisCo-MoT couples a discrete masked-modeling branch with a continuous autoregressive diffusion branch via one-way mixture attention within a MoT architecture. Guidance from discrete context mitigates collapse into averaged behaviors in one-to-many reaction generation, while direct prediction in continuous state space bypasses the decoding bottleneck of discrete representations. HAT then maps the predicted next state and observed execution history to executable actions, enabling robust closed-loop control in physics-based simulation. Experiments across all three modalities demonstrate consistent improvements over the baselines in fidelity, diversity, and physical consistency, while ablations validate the complementary contributions of the components. Our code will be released to facilitate future research. Project page: https://binlee26.github.io/MixReact_Page/

</details>

---

### [[20_Research/Papers/具身智能/SpecWM_Turning_Verification_into_Refinement_for_Streaming_World_Models|SpecWM: Turning Verification into Refinement for Streaming World Models]]

![[assets/2611.26211_figure.png|800]]

- **arXiv**: [2611.26211](https://arxiv.org/abs/2611.26211)
- **PDF**: https://arxiv.org/pdf/2611.26211
- **详细分析**: [[20_Research/Papers/具身智能/SpecWM_Turning_Verification_into_Refinement_for_Streaming_World_Models|SpecWM: Turning Verification into Refinement for Streaming World Models]]
- **作者**: Jiaming Li, Lingzhen Li, Xiaze Yang, Chenyu Zhu, Kaiqi Liu, Xiaotong Zhao, Songlian Li, Toyota Li, Alan Zhao, Haobin Zhong, Yue Ma, Zhiyuan Ma
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: EmbodiedAI, WorldModel, ComputerVision

#### 研究背景与动机

《SpecWM: Turning Verification into Refinement for Streaming World Models》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LongSpecBench, VBench, WBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently, video world models have advanced interactive generation, with large models offering higher quality and smaller models enabling faster inference. Existing speculative methods combine their strengths through fast draft generation and selective target regeneration guided by rewards on decoded frames. However, verification covers only the external scorer's evaluation dimensions and adds decoding and scoring costs. Moreover, these scores provide no correction, requiring costly target regeneration for rejected drafts. To address these limitations, we propose Speculative World Model (SpecWM), a unified, training-free inference framework for streaming world models. It verifies draft chunks using the target's latent velocity field. Verification also yields a reusable correction; two thresholds select Accept, Refine, or Reject. Specifically, one-step refinement reuses it to improve perceptual quality, while three-step refinement strengthens camera following and trajectory consistency. These findings motivate transition-aware refinement. On WBench Navigation, SpecWM improves visual quality at 1.63$\times$ speedup over the target and raises NavScore from the draft's 75.99 to 85.63, achieving the best quality-speed-control trade-off. Additionally, our LongSpecBench shows sustained quality and control over long, multi-turn rollouts, while experiments on Hy-Nomas validate SpecWM across backbones and denoising budgets.

</details>

---

### [[20_Research/Papers/机器人/A_Practical_Proprioceptive_Data_Collection_Utility_for_the_Unitree_GO1|A Practical Proprioceptive Data Collection Utility for the Unitree GO1]]

![[assets/2611.26146_figure.png|800]]

- **arXiv**: [2611.26146](https://arxiv.org/abs/2611.26146)
- **PDF**: https://arxiv.org/pdf/2611.26146
- **详细分析**: [[20_Research/Papers/机器人/A_Practical_Proprioceptive_Data_Collection_Utility_for_the_Unitree_GO1|A Practical Proprioceptive Data Collection Utility for the Unitree GO1]]
- **作者**: Jack Anders Smitterberg, Tan Chen
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Practical Proprioceptive Data Collection Utility for the Unitree GO1》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The Unitree Go1 is a widely used platform for legged robotics research, yet collecting proprioceptive data from it is unnecessarily difficult: the Unitree SDK is sparsely documented, and ROS1 (Robot Operating System), the Go1's native middleware, is fully deprecated. We present an open-source graphical utility that enables researchers to reliably record proprioceptive data from the Go1, including joint states, IMU (Inertial Measurement Unit) readings, foot force sensor data, and gyroscope measurements, without requiring ROS expertise. The tool provides a simple GUI (Graphical User Interface) for starting, stopping, and labeling recordings in real time. The contribution of this paper is the collection utility. We characterize the acquisition quality of 51 recordings collected with it, including the achieved sampling rate and repeated samples. As a secondary, deliberately modest check that the data is useful, we train a terrain classifier on it. The results are weak: a Temporal Convolutional Network reaches about 38% accuracy on held-out recordings across ten terrain classes (10% would be chance), and a window-level split that ignores recording boundaries inflates the same measurement to about 99%. We report this as a demonstration that the logged signals carry terrain information, not as a competitive classifier. The utility is designed to lower the barrier to collecting Go1 proprioceptive data without ROS.

</details>

---

### [[20_Research/Papers/具身智能/UniVEP_Unifying_Velocity_and_Endpoint_Prediction_for_Robot_Manipulation|UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation]]

![[assets/2611.26103_figure.png|800]]

- **arXiv**: [2611.26103](https://arxiv.org/abs/2611.26103)
- **PDF**: https://arxiv.org/pdf/2611.26103
- **详细分析**: [[20_Research/Papers/具身智能/UniVEP_Unifying_Velocity_and_Endpoint_Prediction_for_Robot_Manipulation|UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation]]
- **作者**: Zhengtu Liang, Qiwei Liang, Tao Lin, Shihang Weng, Boyang Cai, Xiangyu Chen, Yikeng Chen, Jiaming Liang, Bohan Tan, Yu Yan, Renjing Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《UniVEP: Unifying Velocity and Endpoint Prediction for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow-matching robot policies usually use one prediction target throughout action generation, even though recovering actions from noise and polishing nearly clean actions bring different challenges. We systematically compare velocity prediction (V), endpoint prediction (X), and velocity-weighted endpoint prediction (X--V) across multiple robot policies, benchmarks, and inference budgets. On StarVLA and LiLa-WAM, X--V works best for few-step generation, while V gains more from iterative refinement. We further uncover their complementary strengths across noise levels: clean actions have concentrated covariance spectra, endpoint predictions stay more stable under high noise, and velocity predictions offer more accurate corrections near clean actions. Inspired by these findings, we introduce UniVEP, which learns both prediction targets together with consistency supervision and switches from endpoint recovery to velocity refinement as noise drops. Each step only needs one network run, and joint training also boosts single-step endpoint generation. Tests on simulated and real-world manipulation show better success rates and efficiency. On RoboTwin, UniVEP hits 61.36% success with one StarVLA run, beating the best single-target baseline at sixteen runs (59.96%). With LiLa-WAM, two runs outperform the best sixteen-step single-target baseline and cut inference latency by 77.1%.

</details>

---

### [[20_Research/Papers/多模态技术/Fixing_the_Twin,_Not_the_Detector_Sim-to-Real_Roadside_LiDAR_Detection_from_Digital-Twin_Data|Fixing the Twin, Not the Detector: Sim-to-Real Roadside LiDAR Detection from Digital-Twin Data]]

![[assets/2611.26035_first_page.png|800]]

- **arXiv**: [2611.26035](https://arxiv.org/abs/2611.26035)
- **PDF**: https://arxiv.org/pdf/2611.26035
- **详细分析**: [[20_Research/Papers/多模态技术/Fixing_the_Twin,_Not_the_Detector_Sim-to-Real_Roadside_LiDAR_Detection_from_Digital-Twin_Data|Fixing the Twin, Not the Detector: Sim-to-Real Roadside LiDAR Detection from Digital-Twin Data]]
- **作者**: KuanLin Chen, Feng-jui Kuo
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.2（加权：具身智能 1.2）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Fixing the Twin, Not the Detector: Sim-to-Real Roadside LiDAR Detection from Digital-Twin Data》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Roadside LiDAR detectors are expensive to train on real labels, and digital twins promise to replace these labels, but a detector trained on a twin meets a different sensor, different objects and different annotation conventions on the real site. We describe the pipeline that placed first in the LUMPI track of the UrbanTwin Sim2Real LiDAR Challenge (IEEE BigData 2026 Cup, 0.5541 combined score) and fifth on its V2X-Real track (0.8102). Every detector is a CenterPoint model trained only on synthetic data, on a single 8 GB laptop GPU. Most of the gain came from correcting differences between the twin and the real site rather than from the detector. We align the twin's coordinates, point density and box convention with the test sensor, generate the pedestrians and riders that the twins lack, plus street clutter as unlabeled negatives, and rebuild twin objects at real size and real point density. A non-learned resampling to the per-cell point density of unlabeled real frames lifts LUMPI realism from 0.589 to 0.947, against 0.949 between real frames. Label-free post-processing then exploits what a fixed roadside sensor guarantees: static structures recur in every frame, and real objects have characteristic point statistics. Reporting the validation and test gain of each component side by side, we find that corrections of systematic sim-to-real differences transfer to the test set, typically keeping a quarter to three quarters of their validation gain, while choices that fit the few objects of a validation set do not.

</details>

---

### [[20_Research/Papers/强化学习/Learning_What_Actions_Change_Action_Effect_Matching_for_Dynamics-Faithful_World_Models|Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models]]

![[assets/2611.25980_figure.png|800]]

- **arXiv**: [2611.25980](https://arxiv.org/abs/2611.25980)
- **PDF**: https://arxiv.org/pdf/2611.25980
- **详细分析**: [[20_Research/Papers/强化学习/Learning_What_Actions_Change_Action_Effect_Matching_for_Dynamics-Faithful_World_Models|Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models]]
- **作者**: John Won, Yonghoon Dong, Jinwoo Shin
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，世界模型 1，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Learning What Actions Change: Action Effect Matching for Dynamics-Faithful World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World models aim to predict environment dynamics under actions, enabling the prediction of action consequences without executing them in the real world. Yet despite producing increasingly realistic videos, current world models often fail to capture how small action changes affect future observations. This limits their use in tasks such as robotic policy evaluation and model-based planning, where nearly identical actions can lead to qualitatively different outcomes. To address this, we propose AFFECT, an auxiliary training objective for learning the distribution of visual changes induced by action perturbations. Specifically, we inject temporally correlated noise into the actions of a policy trained on task-agnostic human teleoperation. We then train the world model so that its generated videos respond to this noise as the recorded videos do, without requiring repeated executions from the same initial state. Across OGBench simulation and real-world DROID and ALOHA-2 setups, AFFECT makes world-model rollouts more faithful to real outcomes. On DROID, the Pearson correlation between policy success rates in the world model and on the real robot rises from 0.47 to 0.79, alongside up to 23% lower FVD. These gains carry over to planning, where selecting actions with AFFECT-trained world models improves task success by up to 8.3%.

</details>

---

### [[20_Research/Papers/世界模型/Point_Dynamics_as_Proxy_for_Robotic_World_Models|Point Dynamics as Proxy for Robotic World Models]]

![[assets/2611.25946_figure.png|800]]

- **arXiv**: [2611.25946](https://arxiv.org/abs/2611.25946)
- **PDF**: https://arxiv.org/pdf/2611.25946
- **详细分析**: [[20_Research/Papers/世界模型/Point_Dynamics_as_Proxy_for_Robotic_World_Models|Point Dynamics as Proxy for Robotic World Models]]
- **作者**: Dong An, Tianyu Liu, Haoran Ding, Wen Yang, Anqing Duan, Zhengzhong Liu, Eric P. Xing, Guangyi Liu
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人
- **相关性评分**: 2.0（加权：世界模型 1，机器人 1）
- **关联关键词**: Robotics, WorldModel, ComputerVision

#### 研究背景与动机

《Point Dynamics as Proxy for Robotic World Models》归入 世界模型、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Ctrl-World, PointWorld, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic world models predict future video frames from the current observation and a sequence of robot actions. While recent models follow the given actions closely, manipulated objects often collapse or move inconsistently with the action. We attribute this to the conditioning: an action, or a rendering of the robot, specifies where the robot goes but not how the scene responds, leaving a single video model to infer the interaction dynamics implicitly while also rendering appearance. We therefore separate dynamics prediction from visual rendering, with 3D point dynamics as the proxy between them. Specifically, we lift the first frame into 3D points, simulate how they respond to the robot's motion with a learned point dynamics model, and render the simulated points back into pixel-aligned videos that any video model can read. In controlled experiments on the DROID dataset with two video renderers of different architectures, this point dynamics proxy reduces object motion error by 8.6% and 6.2% without degrading image quality, and by 8.1% on a real bimanual robot. Moreover, the video follows the simulation: more accurate dynamics yield more accurate object motion, and editing the points steers the video. This suggests that advances in dynamics modeling can translate into more faithful robotic world models.

</details>

---

### [[20_Research/Papers/机器人/Fast_and_Accurate_Body_Estimation_in_Pixels,_World_Space_and_Scenes|Fast and Accurate Body Estimation in Pixels, World Space and Scenes]]

![[assets/2611.25801_figure.png|800]]

- **arXiv**: [2611.25801](https://arxiv.org/abs/2611.25801)
- **PDF**: https://arxiv.org/pdf/2611.25801
- **详细分析**: [[20_Research/Papers/机器人/Fast_and_Accurate_Body_Estimation_in_Pixels,_World_Space_and_Scenes|Fast and Accurate Body Estimation in Pixels, World Space and Scenes]]
- **作者**: Jinkun Cao
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Fast and Accurate Body Estimation in Pixels, World Space and Scenes》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：GaussGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present FAB (Fast and Accurate Body estimation), a human body estimator that jointly improves inference efficiency and body-recovery fidelity. Rather than predicting only parametric mesh-model parameters, FAB directly predicts human skeleton joints and dense surface points. In images, it predicts dense 2D and 3D body points alongside a parametric Momentum Human Rig (MHR) head, then fits SMPL in one learned pass followed by two Gauss-Newton steps. Its ViT-L student, FAB-L, distilled from a fine-tuned SAM 3D Body, runs in real time for one person on an RTX 4070 Ti SUPER, from detection to a fitted body, at 4.6x the speed of SAM 3D Body's eager-PyTorch body-only path, while improving accuracy on most camera-space benchmarks. The same network predicts heel, toe, hand, and knee contacts, which connect the body to the scene. FAB also estimates world-space motion, fuses static-scene depth around the visible person, and aligns body and scene using predicted contacts. For human-to-humanoid real-to-sim transfer, an in-model G1 head and FAB-Retarget, a motion-level retargeter that reads dense points or the fitted mesh, map motion to a Unitree G1. FAB-Retarget produces references that follow the person more closely than specialized retargeters including SOMA, GMR, UMR, and OmniRetarget, and substantially more closely than Fast SAM 3D Body retargeted with our sequence IK. Project page: https://www.jinkuncao.com/FAB.

</details>

---

### [[20_Research/Papers/具身智能/CauSyncVLA_Causal_Latent_World_Modeling_for_Asynchronous_Robot_Control|CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control]]

![[assets/2611.25667_figure.png|800]]

- **arXiv**: [2611.25667](https://arxiv.org/abs/2611.25667)
- **PDF**: https://arxiv.org/pdf/2611.25667
- **详细分析**: [[20_Research/Papers/具身智能/CauSyncVLA_Causal_Latent_World_Modeling_for_Asynchronous_Robot_Control|CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control]]
- **作者**: Xu Pan, Chubin Zhang, Xingrui Yu, Runmin Lan, Zihao Wang, Wenkai Guo, Bofang Jia, Bo An, Ziwei Wang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 2.2（加权：具身智能 0.9，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, WorldModel

#### 研究背景与动机

《CauSyncVLA: Causal Latent World Modeling for Asynchronous Robot Control》归入 机器人、具身智能、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：CauSyncVLA, EagleVLA, EfficientVLA, HBVLA, MAP-VLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) policies must react while visual inference is still running. Overlapping computation and execution reduces waiting, yet leaves perceptual memory stale and successive action chunks disconnected. We present CauSyncVLA, an asynchronous dual-system controller that aligns perceptual-memory prediction and trajectory correction with actual robot execution. Rather than forecasting pixels or physical states, a Causal Latent World Model predicts current perceptual memory from delayed visual anchors and executed state-action history, supervised through action-sensitive distillation to retain the frozen expert's control response. Conditioned on this updated memory, Predictive Flow Warm-Starting (PFWS) aligns the unexecuted action horizon for single-step flow correction without extra training. On LIBERO-10, CauSyncVLA reaches 93.8% success at 5.04$\times$ inference throughput, improving closed-loop robustness and robot motion smoothness.

</details>

---

### [[20_Research/Papers/世界模型/Physical_Laws_without_Physics_Loss_Probing_Learned_Dynamics_in_Video_World_Models_through_Forced_Response|Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response]]

![[assets/2611.25626_figure.png|800]]

- **arXiv**: [2611.25626](https://arxiv.org/abs/2611.25626)
- **PDF**: https://arxiv.org/pdf/2611.25626
- **详细分析**: [[20_Research/Papers/世界模型/Physical_Laws_without_Physics_Loss_Probing_Learned_Dynamics_in_Video_World_Models_through_Forced_Response|Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response]]
- **作者**: Yutao Li, Chen Wang, Wangmeng Zuo, Hui Li
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 强化学习
- **相关性评分**: 1.12（加权：强化学习 0.16，世界模型 0.96）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《Physical Laws without Physics Loss? Probing Learned Dynamics in Video World Models through Forced Response》归入 世界模型、强化学习 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Do video world models learn physical laws without a physics loss, or merely imitate motion? Overall motion and appearance scores cannot settle it. We investigate this through nonlinear forced response: an excitation shakes the support of a suspended object. We introduce dual visual-numeric conditioning and adapt six image-to-video backbones to predict this motion using only the flow-matching loss. Wan predicts motion accurately and generalizes to unseen excitations, objects, poses, and scenes. Counterfactual tests suggest capabilities beyond replaying training videos. But what laws have they learned? We design three tiers of tests using Taylor expansions of the dynamics and geometry. All six reproduce the linear response, including resonance; five capture higher-order dynamics, including nonlinear softening. Remarkably, softening is barely present in training: only 0.74% of the swing's squared displacement. Extensions to a double pendulum and a rocking block show sustained dynamics are learned more faithfully than brief impacts. Yet learned dynamics may fail to appear when state estimation or propagation goes wrong. We turn these tests and findings into strategies to improve video training and generation.

</details>

---

### [[20_Research/Papers/强化学习/LoopedWAM_Looped_World_Action_Models_for_Elastic_Inference|LoopedWAM: Looped World Action Models for Elastic Inference]]

![[assets/2611.25595_figure.png|800]]

- **arXiv**: [2611.25595](https://arxiv.org/abs/2611.25595)
- **PDF**: https://arxiv.org/pdf/2611.25595
- **详细分析**: [[20_Research/Papers/强化学习/LoopedWAM_Looped_World_Action_Models_for_Elastic_Inference|LoopedWAM: Looped World Action Models for Elastic Inference]]
- **作者**: Anh Dao, Xinxin Liu, Hang Yu, Jeffrey A Chan Santiago, Yuzhang Shang
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《LoopedWAM: Looped World Action Models for Elastic Inference》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GigaWorld, RD-VLA, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World action models (WAMs) couple generative video modeling with robotic action prediction but typically require large video and action transformers, limiting deployment efficiency. We present LoopedWAM, a compact WAM that recurrently applies a shared six-block core in each expert, executing 30 transformer layers while storing only 12 blocks per expert. To account for their asymmetric inference costs, the video and action experts can operate at different depths: visual features are computed once per query, whereas action computation repeats at every sampling step. We further propose elastic self-distillation, which trains a single elastic checkpoint, LoopedWAM-E, across action-depth and sampling-step budgets. With only 0.58B policy parameters and no robot pretraining, LoopedWAM achieves 96.1% success on LIBERO, 91.9% on RoboTwin 2.0, and 52.2% on RoboCasaGR1, while using $7.4\times$ less peak GPU memory than Fast-WAM under matched inference measurements. On LIBERO, LoopedWAM-E achieves 96.0% success in 27.6 ms or 95.2% in 24.7 ms on an H100, providing multiple accuracy-latency operating points from a single checkpoint; with two sampling steps and four action loops, it stays within 0.5 points of LoopedWAM on all three benchmarks. Ablations demonstrate that weight-shared depth preserves competitive performance, while aggressive action-depth reduction requires explicit budget-aware training. On a real AgileX PiPER arm, LoopedWAM succeeds in 71.3% of 80 trials across four tasks.

</details>

---

### [[20_Research/Papers/具身智能/Trajectory-Calibrated_Merging_of_Embodied_Policies|Trajectory-Calibrated Merging of Embodied Policies]]

![[assets/2611.25575_figure.png|800]]

- **arXiv**: [2611.25575](https://arxiv.org/abs/2611.25575)
- **PDF**: https://arxiv.org/pdf/2611.25575
- **详细分析**: [[20_Research/Papers/具身智能/Trajectory-Calibrated_Merging_of_Embodied_Policies|Trajectory-Calibrated Merging of Embodied Policies]]
- **作者**: Wenshuo Chen, Honglei Jin, Le Yang, Jianfei Song, Shaofeng Liang, Lei Wang, Junze Zhu, Kailong Wang, Zhengxi Jin, Haozhe Jia, Honglin Chu, Songning Lai...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Trajectory-Calibrated Merging of Embodied Policies》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MergeVLA, OpenVLA, ReVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot foundation models are increasingly adapted into task specialists to expand their embodied capabilities. Yet these capabilities remain fragmented across separate policies, and existing model-merging methods do not reliably preserve them during closed-loop execution: parameter-space alignment provides only an indirect proxy for behavior, while regression may fail to preserve behavior at states not covered by its calibration inputs. We present Trajectory-Calibrated Regression (TCR), an execution-aware, gradient-free framework that consolidates robot specialists into a single policy. Across two complementary timescales, TCR collects calibration inputs from expert rollouts spanning different stages of task execution and from intermediate states within iterative action generation. To account for representation shifts introduced by merging, TCR recomputes each block's input through the already merged blocks. It then uses each expert's computation within the block to form module inputs and fits merged weights to match the experts' linear outputs. A two-pass calibration procedure further refines the merged policy using separate rollout caches while retaining the frozen specialists as teachers. The resulting model preserves the original inference graph and requires neither expert routing nor additional gradient training. On LIBERO, TCR merges four $π_{0.5}$ specialists and achieves 77.83% success across 1,200 evaluation episodes, outperforming FeatCal, RegMean, and direct weight averaging by 9.50, 24.17, and 33.00 percentage points, respectively.

</details>

---

### [[20_Research/Papers/具身智能/TwoPass_Draft-Guided_Few-Step_Video_Prediction_for_Robotic_Manipulation|TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation]]

![[assets/2611.25553_figure.png|800]]

- **arXiv**: [2611.25553](https://arxiv.org/abs/2611.25553)
- **PDF**: https://arxiv.org/pdf/2611.25553
- **详细分析**: [[20_Research/Papers/具身智能/TwoPass_Draft-Guided_Few-Step_Video_Prediction_for_Robotic_Manipulation|TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation]]
- **作者**: Yijun Liu, Shijia Ge, Tongtong Feng, Xin Wang, Yuan Meng, Yuwei Liu, Zhi Wang, Wenwu Zhu
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.9，机器人 0.6）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《TwoPass: Draft-Guided Few-Step Video Prediction for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Ctrl-World, IRASim, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned video prediction lets robots anticipate the visual consequences of their actions for planning and policy evaluation. Existing predictors denoise each future from noise without using their own estimate of it, which limits the quality of the predicted future, in particular of the manipulated objects, and requires many network calls. We present TwoPass, a self-conditioned training-and-inference framework that keeps the standard flow-matching objective. Self-Generated Draft Training supplies a detached clean-video estimate from the shared network as conditioning at the same noisy state. A Refinement-Only Late Adapter applies a dedicated residual transformation when a draft is present. At inference, Draft-Reuse Iterative Refinement obtains both a solver update and the next draft from each velocity prediction, requiring as few as 4 function evaluations (NFE) per video chunk. Training samples discrete solver-query noise levels and updates the pretrained backbone. Extensive experiments on Bridge and Language Table show that TwoPass achieves state-of-the-art results with 4 NFE, far fewer than the 50-59 calls of existing predictors. Code: https://github.com/PlantPotatoOnMoon/TwoPass.

</details>

---

### [[20_Research/Papers/具身智能/TuringPAI_A_Foundation_for_On-Device_Physical_AI|TuringPAI: A Foundation for On-Device Physical AI]]

![[assets/2611.25474_figure.png|800]]

- **arXiv**: [2611.25474](https://arxiv.org/abs/2611.25474)
- **PDF**: https://arxiv.org/pdf/2611.25474
- **详细分析**: [[20_Research/Papers/具身智能/TuringPAI_A_Foundation_for_On-Device_Physical_AI|TuringPAI: A Foundation for On-Device Physical AI]]
- **作者**: Qiman Wu, Hanlin Chen, Yuhua Wei, Mingyuan Wang, Shaman Tang, Minghao Li, Rui Xin, Xingye Liu, Zhichao Yang, Yiqi Yu, Hongyan Pei, Xiaowen Tian...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.2，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《TuringPAI: A Foundation for On-Device Physical AI》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical AI requires models that understand spatial relationships and dynamic environments and translate observations into actions under limited onboard compute. We present TuringPAI, a family of models for on-device Physical AI comprising TuringPAI-VL for shared vision-language understanding, TuringPAI-Drive for autonomous driving, and TuringPAI-Embodied for robotic manipulation. TuringPAI-VL is a 0.65B model built on HybridViT-MLQ, which combines convolutional local aggregation with Transformer-based global modeling. Multi-scale Latent Queries integrate spatial features and observation history within the same visual Transformer, providing a compact, structured interface to the language model. Training combines general vision-language data with geometric, cross-view, and temporal supervision. TuringPAI-VL supports general multimodal understanding and improves quantitative geometric perception over Qwen2-VL-2B, while providing a shared initialization for the two downstream VLA models. For autonomous driving, TuringPAI-Drive maintains all evaluated ADE/FDE metrics within 1.2\% of a full-token HybridViT baseline using the MLQ interface and achieves comparable aggregate scores in an in-house simulation evaluation. Using XPeng Native Runtime (XNRT) on a single NVIDIA Orin-X SoC, TuringPAI-Drive generates trajectories at 12\,Hz in on-vehicle operation. For robotic manipulation, TuringPAI-Embodied achieves a 96.8\% average success rate across the four LIBERO suites. These results demonstrate a shared vision-language foundation for driving and robotic manipulation under practical on-device constraints.

</details>

---

### [[20_Research/Papers/具身智能/ActMem_From_Latent_Memory_Reasoning_to_Grounded_Robotic_Action|ActMem: From Latent Memory Reasoning to Grounded Robotic Action]]

![[assets/2611.25461_figure.png|800]]

- **arXiv**: [2611.25461](https://arxiv.org/abs/2611.25461)
- **PDF**: https://arxiv.org/pdf/2611.25461
- **详细分析**: [[20_Research/Papers/具身智能/ActMem_From_Latent_Memory_Reasoning_to_Grounded_Robotic_Action|ActMem: From Latent Memory Reasoning to Grounded Robotic Action]]
- **作者**: Linfeng Dong, Jianwei Niu, Jiuyi Zhao, Ruibing Feng, Xinghao Wu, Wu Yang, Shuai Tao, Wulong Liu, Mu Li
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.2，机器人 0.6）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《ActMem: From Latent Memory Reasoning to Grounded Robotic Action》归入 机器人、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MemoryVLA, Real-World, SimpleMemVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown promising results in real-world long-horizon manipulation, where memory plays a crucial role. However, existing memory-augmented VLAs either retrieve past observations without reasoning about what they imply, or reason over the full history in a shared context where it crowds out current perception. Cognitive science treats them as distinct systems: memory reconstructs past experience to decide what to do, while perception guides how to act. We therefore propose ActMem, an in-context memory framework that decouples memory reasoning from perceptual grounding within a single vision-language backbone. Built on a vision-language model with native video understanding, ActMem infers the current subtask from a timestamped interaction history and keeps the hidden states formed during this inference as a Latent Memory Chain-of-Thought (Memory CoT), which conditions a flow-matching action expert. Perception Attention further lets the expert attend directly to the current view. To keep inference fast under long histories, Efficient Memory CoT Inference reuses computation across consecutive decisions without changing the output. ActMem achieves 71.1% task success and 80.8% completion success on RoboMemArena, surpassing the strongest baseline by 7.5 and 8.7 percentage points, and 73.8% average success on MIKASA-Robo, the best among all compared methods. In the real world, it reaches 68.8% average success on exogenous, endogenous, and traceless memory tasks, 10.0 percentage points above the strongest memory-augmented VLA. Code and checkpoints will be released at https://github.com/LigphiDonk/ActMem and https://huggingface.co/donk111/ActMem.

</details>

---

### [[20_Research/Papers/具身智能/MIR-Depth_Multi-Range_Refinement_for_Single-View_RGB-D_Depth_Completion_of_Transparent_Objects|MIR-Depth: Multi-Range Refinement for Single-View RGB-D Depth Completion of Transparent Objects]]

![[assets/2611.25417_figure.png|800]]

- **arXiv**: [2611.25417](https://arxiv.org/abs/2611.25417)
- **PDF**: https://arxiv.org/pdf/2611.25417
- **详细分析**: [[20_Research/Papers/具身智能/MIR-Depth_Multi-Range_Refinement_for_Single-View_RGB-D_Depth_Completion_of_Transparent_Objects|MIR-Depth: Multi-Range Refinement for Single-View RGB-D Depth Completion of Transparent Objects]]
- **作者**: Xinzhe Fu, Qi Shao, Yuanfei Xie, Taoyu Wu, Zhihao Cao, Long Hu, Hong Liang, Xianzhi Li, Anh Nguyen, Baoru Huang, Rongsheng Li
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MIR-Depth: Multi-Range Refinement for Single-View RGB-D Depth Completion of Transparent Objects》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BP-Net, CasMVSNet, DCIRNet, DFNet, PSMNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recovering accurate visible-surface depth from a single RGB-D image and an object mask is essential for robotic grasping and manipulation of transparent objects. Specular reflections cause missing depth, while refraction corrupts nonzero returns with background depth, making raw measurements unreliable as surface anchors. Under a fixed sampling budget, refining an initial single-view prediction within a single search interval either misses large refraction offsets or sacrifices fine local resolution. To resolve this single-view trade-off, MIR-Depth constructs Coordinate-Aware Multi-Range Hypotheses: a 3D-aggregated global inverse-depth volume and depth-axis-filtered pixel-wise local volumes around a prior-guided initial depth. Selective Recurrent Refinement then introduces out-of-bounds lookup masking and validity-masked softmax fusion to iteratively update inverse depth from these volumes using a multi-scale ConvGRU. Finally, Spatially Gated Correction applies a learned per-pixel spatial gate to the full-resolution residual, preserving accurate initial geometry without imposing raw sensor readings as hard constraints. Experiments on TransCG, TODD, TRansPose, ClearPose, and HouseCat6D show that MIR-Depth achieves lower error than ReMake, DFNet, BP-Net, and PSD. Real-robot evaluations confirm accurate surface geometry for 6-DoF grasp pose prediction. Code and pretrained models will be publicly available.

</details>

---

### [[20_Research/Papers/世界模型/Identity_World_Model_Recognizing_People_in_an_Imagined_Latent_World|Identity World Model: Recognizing People in an Imagined Latent World]]

![[assets/2611.25204_figure.png|800]]

- **arXiv**: [2611.25204](https://arxiv.org/abs/2611.25204)
- **PDF**: https://arxiv.org/pdf/2611.25204
- **详细分析**: [[20_Research/Papers/世界模型/Identity_World_Model_Recognizing_People_in_an_Imagined_Latent_World|Identity World Model: Recognizing People in an Imagined Latent World]]
- **作者**: Dingqiang Ye, Kartik Narayan, Vishal M. Patel
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel

#### 研究背景与动机

《Identity World Model: Recognizing People in an Imagined Latent World》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IDWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body human recognition has advanced rapidly with large vision models. However, existing methods remain fragile under real-world variations, as they tie identity to transient cues such as clothing, texture, pose, or viewpoint. We argue that a robust recognizer should not merely learn to ignore these cues, but imagine how a person would be represented if they changed. To this end, we propose IDWorld, an identity world model: just as a latent world model predicts the features of a scene after an action, IDWorld predicts how a person would be represented under a changed condition. In a single forward pass, IDWorld imagines these counterfactual features under shared canonical conditions, such as the same outfit, a fixed view, or a bare silhouette, without rendering any pixels. Compared with explicit imagination in pixels, this latent imagination keeps nearly the same accuracy while being over 11x faster, at 5.9 ms per frame. Since each imagined condition has its own strengths, IDWorld then fuses them adaptively, weighting each condition for every probe-gallery pair. Extensive experiments show that IDWorld achieves state-of-the-art results on CCPG and CCGR-MINI, outperforms the compared methods on MEVID, and generalizes best to CASIA-B* and SUSTech1K, with the best mAP on CCVID. These results suggest identity world models offer a simple yet effective path to robust recognition. Code will be released.

</details>

---

### [[20_Research/Papers/具身智能/GEMS_Generation_and_Experience_Memory_for_Subgoal-Guided_Long-Horizon_World_Model_Planning|GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning]]

![[assets/2611.25134_figure.png|800]]

- **arXiv**: [2611.25134](https://arxiv.org/abs/2611.25134)
- **PDF**: https://arxiv.org/pdf/2611.25134
- **详细分析**: [[20_Research/Papers/具身智能/GEMS_Generation_and_Experience_Memory_for_Subgoal-Guided_Long-Horizon_World_Model_Planning|GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning]]
- **作者**: Yangchen Zhao, Ali Payani, Caiwen Ding
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《GEMS: Generation and Experience Memory for Subgoal-Guided Long-Horizon World Model Planning》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Meta-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual world models enable effective short-horizon goal-conditioned planning, such as reaching nearby targets and pushing objects over short distances, by predicting candidate action outcomes and comparing their representations with a goal representation. However, extending this approach to long-horizon tasks is challenging: prediction errors accumulate over extended rollouts, while latent-space similarity to distant goals provides limited guidance for ranking candidate outcomes. Existing methods address these limitations by introducing intermediate subgoals, either generated by learned models or selected from experience memory. Generated subgoals can contain hallucinations or be inaccurate in aspects such as object positions and timing. Memory-based approaches are constrained by experience coverage and may lack precise guidance for selecting appropriate intermediate states from stored observations. We introduce GEMS, which generates temporally structured subgoals to guide action search and state selection from Latent Experience Memory (LEM). A distance gate determines whether predicted outcomes are evaluated against the generated subgoal or the selected memory state. Experiments across six tasks and task suites spanning manipulation, navigation, and reaching demonstrate the effectiveness of GEMS for long-horizon planning. GEMS outperforms state-of-the-art world-model planning baselines across different manipulation settings, achieving success rates of 92.8% on Cube, 68.4% on Push-T, and 54.1% on Meta-World. It improves over the strongest evaluated baseline on these tasks by 24.0, 7.3, and 22.2 percentage points, respectively. These results demonstrate that generated subgoals and experience memory can jointly strengthen long-horizon planning with a frozen world model.

</details>

---
