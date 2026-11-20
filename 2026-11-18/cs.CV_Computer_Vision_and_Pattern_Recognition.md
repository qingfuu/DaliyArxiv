# cs.CV | Computer Vision and Pattern Recognition | 2026-11-18

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/具身智能/TCP4D_A_Unified_Tool-Center-Point_Tracking_and_Generation_Model_for_Robot_Manipulation|TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation]]

![[assets/2611.23143_figure.png|800]]

- **arXiv**: [2611.23143](https://arxiv.org/abs/2611.23143)
- **PDF**: https://arxiv.org/pdf/2611.23143
- **详细分析**: [[20_Research/Papers/具身智能/TCP4D_A_Unified_Tool-Center-Point_Tracking_and_Generation_Model_for_Robot_Manipulation|TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation]]
- **作者**: Haosong Peng, Xiangyang Liu, Zhengshen Zhang, Yunfeng Fan, Tianyu Qi, Xin Xia, Yufeng Zhan, Wenchao Xu
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《TCP4D: A Unified Tool-Center-Point Tracking and Generation Model for Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation videos provide a rich visual experience, yet recovering robot action and gripper-state annotations from RGB observations still remains challenging. Using the embodiment-agnostic tool-center-point (TCP) pose as the action space, we present TCP4D, a unified model in which a shared 4D scene representation both tracks observed TCP motion and generates future TCP trajectories. Given a monocular video and initial 2D TCP queries, the tracker directly recovers metric TCP poses in SE(3) and gripper states alongside scene geometry and camera parameters. The generator samples local features from the same 4D representation along the recovered TCP tracks, then combines them with robot observations and language instructions to predict future TCP states. Our new cross-embodiment augmentation pipeline converts existing RGB videos into demonstrations for alternative embodiments by retargeting the recovered motion and synthesizing the corresponding observations, without recorded source-robot states. Experiments show that the tracker achieves absolute trajectory errors of 7.60 and 16.07 mm on DROID and RoboLab and adapts to a new embodiment with only ten demonstrations. The generator achieves 69.19% mean success on RoboTwin and outperforms well-established policy models on two real-world tasks, while joint training on source and augmented demonstrations improves target-robot success by 41.5% over augmented-only training.

</details>

---

### [[20_Research/Papers/具身智能/RFW-S_Everyday_Deformable_Objects_with_Independent_Simulation_Verification|RFW-S: Everyday Deformable Objects with Independent Simulation Verification]]

![[assets/2611.23056_figure.png|800]]

- **arXiv**: [2611.23056](https://arxiv.org/abs/2611.23056)
- **PDF**: https://arxiv.org/pdf/2611.23056
- **详细分析**: [[20_Research/Papers/具身智能/RFW-S_Everyday_Deformable_Objects_with_Independent_Simulation_Verification|RFW-S: Everyday Deformable Objects with Independent Simulation Verification]]
- **作者**: Jiarui Guo, Saining Zhang, Jiaying Wan, Jiawei Weng, Junhao Chen, Rui Zhang, Yuanbo Lyu, Zhiheng Lee, Peishuo Li, Jingrun Du, Weiqing Xiao, Weiyi Lin...
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《RFW-S: Everyday Deformable Objects with Independent Simulation Verification》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ClothesNet, DaXBench, DefGraspSim, Real2Sim, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large-scale robotic simulation requires diverse deformable objects with executable physical properties and realistic interaction behaviors. However, existing 3D asset collections primarily emphasize visual diversity, while scalable physical construction and verification remain challenging. We introduce RFW-S, a large-scale dataset of 83,365 simulation-verified assets spanning 485 everyday categories across five structural families: soft solids, cloth sheets, shells, garments, and bags. We develop an automated pipeline integrating reference-guided 3D generation, structure-aware physical modeling, and LLM-assisted parameter estimation and calibration. To ensure physical reliability, we introduce an independent simulation verification framework that evaluates object behaviors under interactions distinct from those used for parameter calibration. Extensive experiments demonstrate the effectiveness of independent verification and characterize deformable responses under different physical configurations. We further evaluate robotic grasping in terms of both task success and object integrity, and demonstrate the physical realism of our simulated objects through sim-to-real replay of fragile-object manipulation. RFW-S provides a scalable foundation for physically grounded simulation and embodied robotic learning.

</details>

---

### [[20_Research/Papers/强化学习/When_Anchors_Shift_the_Target_Advantage-Gated_Adaptation_for_Diffusion_Reinforcement_Learning|When Anchors Shift the Target: Advantage-Gated Adaptation for Diffusion Reinforcement Learning]]

![[assets/2611.23038_first_page.png|800]]

- **arXiv**: [2611.23038](https://arxiv.org/abs/2611.23038)
- **PDF**: https://arxiv.org/pdf/2611.23038
- **详细分析**: [[20_Research/Papers/强化学习/When_Anchors_Shift_the_Target_Advantage-Gated_Adaptation_for_Diffusion_Reinforcement_Learning|When Anchors Shift the Target: Advantage-Gated Adaptation for Diffusion Reinforcement Learning]]
- **作者**: Pu Cao, Min Zhou, Ying Shu, Tiezheng Ge, Qing Song, Lu Yang
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《When Anchors Shift the Target: Advantage-Gated Adaptation for Diffusion Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Forward-process reinforcement learning adapts diffusion and flow-matching models by re-noising rewarded generations into regression targets. Because negative advantages induce concave updates with unbounded repulsive gradients, existing methods stabilize training using cached predictions from a moving policy copy, yet these anchors also alter what positive feedback teaches the model to fit. We formalize this conflict as anchor coupling: after separating frozen-reference regularizers, affine moving-anchor rules cannot eliminate negative curvature while preserving every positive regression target. We propose Advantage-Gated Adaptation (AGA) to decouple these roles. Positive samples retain standard target fitting, whose self-limiting update vanishes at the observed target independently of the moving anchor. Negative samples instead use the first-order tangent of the concave objective at the moving-policy prediction, preserving the local repulsion direction with a prediction-independent gradient. Within the quadratic-anchor family, these requirements uniquely determine the parameter-free gate $ω(a)=\max(-a,0)$. Because the moving copy provides local linearization rather than retention, AGA assigns long-horizon behavior preservation to a frozen pretrained reference regularized at its operating classifier-free guidance scale, interpreted through an implicit-reward lens. Across compositional generation, text rendering, and preference alignment, our experiments show that displacing positive targets degrades visual quality and heightens sensitivity to policy-copy schedules, whereas AGA consistently improves the reward--quality trade-off.

</details>

---

### [[20_Research/Papers/具身智能/Technical_Report_of_Mobile_Manipulator_Robot_for_Industrial_Environments|Technical Report of Mobile Manipulator Robot for Industrial Environments]]

![[assets/2611.22852_figure.png|800]]

- **arXiv**: [2611.22852](https://arxiv.org/abs/2611.22852)
- **PDF**: https://arxiv.org/pdf/2611.22852
- **详细分析**: [[20_Research/Papers/具身智能/Technical_Report_of_Mobile_Manipulator_Robot_for_Industrial_Environments|Technical Report of Mobile Manipulator Robot for Industrial Environments]]
- **作者**: Aria Dadnavi, Matin Jamshidi, Kian Khatibi, Shahriar Karimi Makhsous, Saina Najafi Shabestari, Seyed Sobhan Hosseini Hajibekandeh, Zahra Mahaam, Reyhane Mohasseli, Ghazal Ghoreishi, Amirhossein Gholizadeh Behbahani, Mohammad Hossein Moaiyeri
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Technical Report of Mobile Manipulator Robot for Industrial Environments》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents the design and implementation of Auriga Robotics' mobile manipulator robot, developed at the Robotics and Intelligent Automation Laboratory, Department of Electrical Engineering, Shahid Beheshti University. Hereafter, this platform is referred to as the @Work Robot. The robot targets industrial tasks, with an emphasis on improving efficiency in repetitive or hazardous work environments. It uses a 4-wheel Mecanum drive for omnidirectional movement and a 5-degree-of-freedom manipulator arm with a 3D-printed gripper for object handling and navigation. The electronics consist of custom PCB boards built around ESP32 microcontrollers, together with an NVIDIA Jetson Orin NX that handles high-level processing and real-time system control. On the software side, Hector SLAM provides mapping and localization, A* handles path planning, and YOLO performs real-time object detection. These modules draw on fused sensor data to deliver robust navigation and reliable collision avoidance. Overall, the system shows effective hardware-software integration, with consistent performance in autonomous navigation, object handling, and task execution in industrial-like settings.

</details>

---

### [[20_Research/Papers/具身智能/RefCloth_Transferable_Adversarial_Tablecloths_for_Vision-Language-Action_Models|RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models]]

![[assets/2611.22736_figure.png|800]]

- **arXiv**: [2611.22736](https://arxiv.org/abs/2611.22736)
- **PDF**: https://arxiv.org/pdf/2611.22736
- **详细分析**: [[20_Research/Papers/具身智能/RefCloth_Transferable_Adversarial_Tablecloths_for_Vision-Language-Action_Models|RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models]]
- **作者**: Shaozhen Liu, Zhiwei Li, Jiayang Sun, Shuangjun Du, Yi Zhong, Shenrui Ma, Yaozu Liu, Qi Li, Zhenan Sun
- **cs 子类**: cs.CV
- **归属领域**: 具身智能
- **相关领域**: 具身智能
- **相关性评分**: 1.5（加权：具身智能 1.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《RefCloth: Transferable Adversarial Tablecloths for Vision-Language-Action Models》归入 具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA, SpatialVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Closed-loop vision-language-action (VLA) policies rely continuously on multi-view cameras, yet existing visual attacks typically hijack sensor streams with 2D patches or alter target object meshes that require retraining when manipulation objects change. We introduce RefCloth, a framework that optimizes one persistent adversarial tablecloth on a frozen source policy and deploys it zero-shot across unseen tasks and target models without modifying task objects or cameras. Throughout manipulation, static third-person and moving wrist views observe this shared world-bound texture under evolving occlusions. To generalize across shifting surface views while bridging the gap between differentiable and native renderers, RefCloth combines bounded texture parameterization with shared surface UV transformations and a same-path clean reference that removes static rendering offsets at initialization. Across four LIBERO suites in native simulation, one frozen texture transfers from OpenVLA-OFT to $π_0$ and $π_{0.5}$, reducing success relative to an unoptimized cloth by 62.50 and 43.75 percentage points on average and far exceeding amplitude- and variation-matched random controls. Dual-view audits and target closed-loop camera interventions show that moving wrist exposure drives over twice the standalone drop of the main view with strong synergy, while ablations confirm the roles of UV diversification and path calibration.

</details>

---

### [[20_Research/Papers/世界模型/Beyond_the_Camera_A_Tri-Modal_Driving_World_Model_for_Future_RGB,_Thermal,_and_LiDAR_Forecasting_in_Adverse_Weather|Beyond the Camera: A Tri-Modal Driving World Model for Future RGB, Thermal, and LiDAR Forecasting in Adverse Weather]]

![[assets/2611.22669_figure.png|800]]

- **arXiv**: [2611.22669](https://arxiv.org/abs/2611.22669)
- **PDF**: https://arxiv.org/pdf/2611.22669
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_the_Camera_A_Tri-Modal_Driving_World_Model_for_Future_RGB,_Thermal,_and_LiDAR_Forecasting_in_Adverse_Weather|Beyond the Camera: A Tri-Modal Driving World Model for Future RGB, Thermal, and LiDAR Forecasting in Adverse Weather]]
- **作者**: Faysal Mehrab Chowdhury, Md. Mahfuzur Rahman, Ahmed Rafi Hasan, Kishor Datta Gupta, Mohd Ariful Haque, Savannah Shannon
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Beyond the Camera: A Tri-Modal Driving World Model for Future RGB, Thermal, and LiDAR Forecasting in Adverse Weather》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：DrivingWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Driving world models forecast what a vehicle's sensors will record next. Most forecast camera video and some add LiDAR, but thermal cameras, which still see in darkness and some adverse weather, are rarely a forecast target, and to our knowledge no world model forecasts all three sensors. We study joint forecasting of RGB, thermal, and LiDAR on real adverse-weather sequences of the DSERT-RoLL dataset. We post-train a pretrained video world model for each sensor and represent LiDAR as a depth video aligned with the RGB camera, with densification and encoding chosen by what the model's video tokenizer can reconstruct. A tri-sensor model sees all three sensors as one video. We score LiDAR in meters against measured returns and compare against persistence baselines passed through the same tokenizer as the model. With this matching, an apparent loss of the thermal model to persistence in fog disappears. On all 58 validation sequences in six weather conditions, post-trained RGB and thermal forecasts beat compression-matched persistence. Joint training lowers the LiDAR error at 2s by 2.1m at a small cost in camera fidelity, and only the tri-sensor model's LiDAR forecasts beat persistence in mean error. Blanking one sensor degrades the forecasts of the others more in snow than in fog.

</details>

---

### [[20_Research/Papers/具身智能/VSpark_Speculative_Decoding_for_Autoregressive_Vision-Language-Action_Models|VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models]]

![[assets/2611.22666_figure.png|800]]

- **arXiv**: [2611.22666](https://arxiv.org/abs/2611.22666)
- **PDF**: https://arxiv.org/pdf/2611.22666
- **详细分析**: [[20_Research/Papers/具身智能/VSpark_Speculative_Decoding_for_Autoregressive_Vision-Language-Action_Models|VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models]]
- **作者**: Suho Yoo, Youngjoon Jang, Hyebin Cho, Taeyeop Lee, Jaewook Jeong, Joon Son Chung
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《VSpark: Speculative Decoding for Autoregressive Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Spec-VLA, StarVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Our aim is to accelerate autoregressive vision-language-action models (VLAs), which generate robot actions one token at a time. Speculative decoding makes this possible: a lightweight draft model proposes several tokens at once, and the VLA verifies them in a single pass, accepting only those that match its own predictions, so decoding remains lossless. The speedup, however, is limited in robot control, where many different tokens encode nearly the same motion and a draft close to the correct action is still rejected. To address this, our approach, VSpark, is built upon three design choices: (i) rollouts collected with calibrated action noise, which expose the draft to a wider range of robot states; (ii) feature alignment, which trains the draft to match the VLA's hidden features rather than its output tokens alone; and (iii) continuation reuse, which keeps the predictions the VLA has already computed along rejected drafts as candidates for the next verification step, instead of discarding them. On four VLAs with different action tokenizers and four manipulation benchmarks, VSpark achieves 1.28x to 2.10x speedup while keeping the VLA's decoding lossless.

</details>

---

### [[20_Research/Papers/强化学习/Plausible_Videos_Can_Lead_to_Poor_Decisions_Diagnosing_and_CURE-ing_World_Models_for_Planning|Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning]]

![[assets/2611.22561_figure.png|800]]

- **arXiv**: [2611.22561](https://arxiv.org/abs/2611.22561)
- **PDF**: https://arxiv.org/pdf/2611.22561
- **详细分析**: [[20_Research/Papers/强化学习/Plausible_Videos_Can_Lead_to_Poor_Decisions_Diagnosing_and_CURE-ing_World_Models_for_Planning|Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning]]
- **作者**: Raphael C. Kim, Michele Santacatterina, Jingsen Zhu, Ramin Zabih
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: Agent, RL, WorldModel

#### 研究背景与动机

《Plausible Videos Can Lead to Poor Decisions: Diagnosing and CURE-ing World Models for Planning》归入 世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PhyWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Action-conditioned world models are increasingly used as world models for planning, yet a world model that makes plausible, realistic-looking videos that are consistent with the training data can produce poor decisions. We address two key questions: (1) when can we trust a world model for planning, and (2) what should we do when we cannot? We introduce CURE (Certify, Upweight, Rollout, Explore), a certificate-guided technique that assesses whether a world model can be trusted for planning and determines what to do next: whether to upweight the training data to debias the model; roll out more samples at test time; or explore by collecting new data where support (how well the training data cover the planner's decisions) is missing. We deploy CURE across multiple domains, spanning simulated physics based on PhyWorld, MuJoCo arm control, and Language-Table pushing in simulation and on real videos. The decisions our certificate trusts have lower regret than those it does not (e.g., 0.06 vs. 0.38 on Language-Table sim and 0.07 vs. 0.38 on MuJoCo contact), whereas video perceptual quality does not identify good decisions. By focusing on decision quality rather than perceptual quality, CURE lowers regret over the best pessimistic decision rule by 10-25% across support levels, and over world-action models, search and policy learning by 41-64%, given the same data.

</details>

---

### [[20_Research/Papers/具身智能/CoBoVLA_Decoupling_Language_from_Action_with_Discrete_Codes_for_Robust_and_Interpretable_Robot_Manipulation|CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation]]

![[assets/2611.22395_figure.png|800]]

- **arXiv**: [2611.22395](https://arxiv.org/abs/2611.22395)
- **PDF**: https://arxiv.org/pdf/2611.22395
- **详细分析**: [[20_Research/Papers/具身智能/CoBoVLA_Decoupling_Language_from_Action_with_Discrete_Codes_for_Robust_and_Interpretable_Robot_Manipulation|CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation]]
- **作者**: Mehul Arora, Dhruv Agarwal, Ambuj Agrawal
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《CoBoVLA: Decoupling Language from Action with Discrete Codes for Robust and Interpretable Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoBoVLA, CodeBookVLA, NanoVLA, OpenVLA, ParaVLA, RoVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models achieve high success rates on the LIBERO benchmark but remain sensitive to paraphrasing. Existing VLAs ranging from 0.6B to 7.5B parameters experience a 22-52 point performance drop on LIBERO-Para while SmolVLA exhibits an even larger decline, from 83\% to 8\%. Because most VLAs jointly learn language understanding and action generation, it is difficult to determine whether a failure originates from misunderstanding an instruction or executing it incorrectly. To address these challenges, we introduce CoBoVLA, or CodeBookVLA, a 250M-parameter VLA that decouples language understanding, planning, and control through learned discrete interpretable codes. A text encoder maps the instructions to shared step codes, which a visual planner then converts into action code sequences executed by a language-independent actor. This design improves robustness to instruction paraphrasing while allowing failures to be traced to individual stages. It also enables efficient real-time control on resource-constrained hardware by encoding instructions only once and using compact discrete representations to keep each component lightweight. CoBoVLA achieves 91.4\% success on LIBERO-Goal, compared with 82.8\% for SmolVLA, under a matched protocol, with 17 ms per control step latency. On LIBERO-Para, it achieves 81.1\% across 4,092 unseen paraphrases and 78.5\% on matched episodes, compared with 36.5\% for SmolVLA LoRA fine-tuned on paraphrases. Without two-step demonstrations, CoBoVLA completes 48.8\% of 160 free-form two-step tasks. Finally, success reaches 91\% when instructions are correctly encoded but falls to 27.2\% otherwise, identifying language understanding as the main source of remaining failures. Together, these results demonstrate that decoupling language understanding and control can improve instruction robustness while making VLA failures easier to diagnose.

</details>

---

### [[20_Research/Papers/具身智能/Inertial_Video_World_Models|Inertial Video World Models]]

![[assets/2611.22314_figure.png|800]]

- **arXiv**: [2611.22314](https://arxiv.org/abs/2611.22314)
- **PDF**: https://arxiv.org/pdf/2611.22314
- **详细分析**: [[20_Research/Papers/具身智能/Inertial_Video_World_Models|Inertial Video World Models]]
- **作者**: Yuan Gao, Fan Xu, Yu Guo, Yuxu Lu, Zhengru Fang, Hao Wu, Xiaomeng Huang
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.3，世界模型 1，机器人 0.2）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《Inertial Video World Models》归入 世界模型、具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：InertialWorld, Real2Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The physical world has inertia: it evolves from what already exists rather than being recreated at every instant. However, many existing video world models lack an explicit mechanism for inertial state evolution, leaving the continuity of motion and structure implicit in video prediction. During autoregressive rollouts, repeated reconstruction can accumulate errors and destabilize the predicted dynamics. To address this limitation, we introduce InertialWorld, an Inertial Video World Model that makes inertia a structural prior for autoregressive prediction: existing scene evidence is carried across time rather than reconstructed at every step. Central to this formulation is Inertial Memory, which turns memory from passive predictive context into an evolving video state with two complementary views: a dense Eulerian grid preserves scene-aligned evidence, while persistent Lagrangian carriers bind local content to learned canonical coordinates. At each step, the model transports the carrier content according to action-conditioned motion, predicts the complete next video state from the transported carriers and dense grid, and uses a learned gate to combine transported and newly predicted content into the memory for the next step. Extensive experiments across multiple domains, including robot manipulation, 3D game simulation, and open-world navigation, demonstrate that InertialWorld achieves competitive autoregressive prediction performance against strong video world model baselines. Codes link: https://github.com/YuanGao-YG/InertialWorld

</details>

---

### [[20_Research/Papers/机器人/Heave-Ho_Decentralized_Long-Horizon_Multi-Humanoid_Collaboration|Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration]]

![[assets/2611.22275_figure.png|800]]

- **arXiv**: [2611.22275](https://arxiv.org/abs/2611.22275)
- **PDF**: https://arxiv.org/pdf/2611.22275
- **详细分析**: [[20_Research/Papers/机器人/Heave-Ho_Decentralized_Long-Horizon_Multi-Humanoid_Collaboration|Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration]]
- **作者**: Ting-Hsuan Chen, Siheng Zhao, Han Jiang, Qi Pan, Louison Lu, Jiaheng Luo, Henghui Bao, Yiyu Chen, Quan Nguyen, Yue Wang
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration》归入 具身智能、机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HH-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.

</details>

---

### [[20_Research/Papers/机器人/CoSphere-SLAM_Multi-Agent_Panoramic_Gaussian_Splatting_SLAM_with_Spherical_Loop_Closure|CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure]]

![[assets/2611.22235_figure.png|800]]

- **arXiv**: [2611.22235](https://arxiv.org/abs/2611.22235)
- **PDF**: https://arxiv.org/pdf/2611.22235
- **详细分析**: [[20_Research/Papers/机器人/CoSphere-SLAM_Multi-Agent_Panoramic_Gaussian_Splatting_SLAM_with_Spherical_Loop_Closure|CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure]]
- **作者**: Qi Shao, Zhihao Cao, Shuhao Zhai, Taoyu Wu, Zhuoxiao Li, Anh Nguyen, Long Hu, Xianzhi Li, Hong Liang, Baoru Huang, Liang Li
- **cs 子类**: cs.CV
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型
- **相关性评分**: 1.3（加权：大模型 0.5，机器人 0.8）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《CoSphere-SLAM: Multi-Agent Panoramic Gaussian Splatting SLAM with Spherical Loop Closure》归入 机器人、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dense collaborative mapping is essential for search and rescue, building inspection, and warehouse automation, where panoramic cameras capture the entire surroundings in a single frame. Unlike pinhole agents that share views only at similar headings, panoramic agents observe overlapping scenes at any 3D orientation, yet searching full rotations also produces mutually consistent false loop closures across distinct symmetric rooms. Moreover, continuous monocular scale drift splits rigidly merged maps at revisited surfaces, while depth noise at short baselines distorts loop translation directions. To address these challenges, we propose CoSphere-SLAM, the first multi-agent Gaussian splatting SLAM framework for panoramic cameras, whose spherical loop closure aligns spherical features over $\mathrm{SO}(3)$ via fast Fourier correlation across arbitrary orientations and rejects symmetric false closures through global $\mathrm{Sim}(3)$ consensus. Building on these closures, directional global optimization solves a per-keyframe $\mathrm{Sim}(3)$ pose graph with log-scale regularization to correct scale drift while separating optical-flow translation directions from depth-based magnitudes. Finally, omnidirectional Gaussian fusion transforms each Gaussian with its keyframe similarity and renders Gaussians at their maximum ray response to jointly refine poses and maps. Experiments on indoor and cross-session multi-agent panoramic benchmarks demonstrate that CoSphere-SLAM achieves state-of-the-art trajectory accuracy and rendering quality among single-agent and multi-agent methods. Project website: https://cosphere-slam.github.io.

</details>

---

### [[20_Research/Papers/机器人/TRIDENT_Efficient_Triple-Task_Learning_of_Dehazing,_Depth,_and_Uncertainty_Estimation_for_Underwater_3-D_Robot_Visual_Perception|TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception]]

![[assets/2611.22224_figure.png|800]]

- **arXiv**: [2611.22224](https://arxiv.org/abs/2611.22224)
- **PDF**: https://arxiv.org/pdf/2611.22224
- **详细分析**: [[20_Research/Papers/机器人/TRIDENT_Efficient_Triple-Task_Learning_of_Dehazing,_Depth,_and_Uncertainty_Estimation_for_Underwater_3-D_Robot_Visual_Perception|TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception]]
- **作者**: Geonmo Yang, Younggun Cho
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《TRIDENT: Efficient Triple-Task Learning of Dehazing, Depth, and Uncertainty Estimation for Underwater 3-D Robot Visual Perception》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Underwater visual systems often suffer from blurry textures and low color contrast due to the inevitable light propagation. These issues can significantly degrade the perception of stable robotic operations. In this paper, we introduce a novel learning-based sensing system that tackles the multidimensional vision tasks in underwater; concretely, we deal with image enhancement, depth estimation, and uncertainty for 3-D visual systems. Also, we propose a TRIDENT model in a fast and lightweight manner; TRIDENT consists of three parallelized decoders and one backbone structure for efficient feature sharing. In addition, it is designed to be trained to express complex parameterization. In experimental evaluation on several standard datasets, we demonstrate that TRIDENT significantly outperforms other existing methods on image enhancement and depth estimation. Despite performing three tasks, our model has better efficiency than the others for both memory size and inference time. Finally, our joint learning approach demonstrates robustness in feature matching and seamlessly extends from 2-D to 3-D vision tasks. Supplements are available at https://sites.google.com/view/underwater-trident/home

</details>

---

### [[20_Research/Papers/大模型/DailyBrick_Language-Guided_Synthesis_of_Brick_Assembly_Instructions|DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions]]

![[assets/2611.22132_figure.png|800]]

- **arXiv**: [2611.22132](https://arxiv.org/abs/2611.22132)
- **PDF**: https://arxiv.org/pdf/2611.22132
- **详细分析**: [[20_Research/Papers/大模型/DailyBrick_Language-Guided_Synthesis_of_Brick_Assembly_Instructions|DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions]]
- **作者**: Hang Zhang, Qijian Tian, Yuan Xie, Xuhong Wang, Xin Tan
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《DailyBrick: Language-Guided Synthesis of Brick Assembly Instructions》归入 机器人、大模型、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BrickNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating a LEGO model from a user request is more than a plausible 3D shape generation. LEGO models require physical support per brick, and each brick should be placed unblocked. Current methods address this issue by training an expert large language model. We reduce the problem of generating extremely long context on all brick connections to that of writing a program that builds LEGO models like a human, considering each intermediate step could be executed. We introduce DailyBrick , a multi-stage agentic system that produces a LEGO model together with a brick-by-brick assembly instruction for human building and robot assembly. We design a multi-stage harness with roles to help LLMs generate more effectively. A versioned construction SDK compiles multi-level decisions, from semantic subparts to individual bricks, into canonical operations. An external Meta-Reviewer agent replays and inspects the generated package, verifies the model and its construction process, identifies failures, traces them to the responsible stage, and routes them to bounded repairs or to editable candidates for later skill or tool updates. Extensive experiments demonstrate that DailyBrick generates LEGO models based on simple user requests better than recent agentic systems, and show its utility in downstream applications such as robot manipulations on model assembly from instructions and brick sets (https://SpatialAgent.github.io/DailyBrick/).

</details>

---

### [[20_Research/Papers/具身智能/CRA_Continuous_Risk_Assessment_for_Safety-critical_Visual_Navigation|CRA: Continuous Risk Assessment for Safety-critical Visual Navigation]]

![[assets/2611.22080_figure.png|800]]

- **arXiv**: [2611.22080](https://arxiv.org/abs/2611.22080)
- **PDF**: https://arxiv.org/pdf/2611.22080
- **详细分析**: [[20_Research/Papers/具身智能/CRA_Continuous_Risk_Assessment_for_Safety-critical_Visual_Navigation|CRA: Continuous Risk Assessment for Safety-critical Visual Navigation]]
- **作者**: Lihao Zheng, Ying Wu, Chen Jiang, Randy Freeman
- **cs 子类**: cs.CV, cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《CRA: Continuous Risk Assessment for Safety-critical Visual Navigation》归入 具身智能、机器人 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Traditional safety-critical control methods often rely on predefined constraints that separate states into safe and unsafe regions. While recent studies have extended geometric safety toward semantic safety, real-world safety is rarely purely binary. The risk associated with an object or human can vary continuously with its physical properties, like motion, and interaction context; for example, a person carrying a heavy object or a hot object moving at high speed may require a different safety response from an ordinary static obstacle. In this paper, we propose a vision-based continuous risk assessment framework for safety-critical visual navigation. Our method uses RGB and LiDAR observations to estimate four risk factors (kinetic, potential, contact-severity, and thermal) and combines them into a continuous risk score for each assessed object or person. These estimates are integrated into a Poisson safety function with a Laplace guidance field as a safety filter, enabling online monitoring and intervention in open-world robot navigation. We demonstrate the proposed method in a simulated restaurant scene.

</details>

---

### [[20_Research/Papers/强化学习/RiDEx_Reward-Informed_Directional_Exploration_for_Diffusion_Reinforcement_Learning|RiDEx: Reward-Informed Directional Exploration for Diffusion Reinforcement Learning]]

![[assets/2611.22052_figure.png|800]]

- **arXiv**: [2611.22052](https://arxiv.org/abs/2611.22052)
- **PDF**: https://arxiv.org/pdf/2611.22052
- **详细分析**: [[20_Research/Papers/强化学习/RiDEx_Reward-Informed_Directional_Exploration_for_Diffusion_Reinforcement_Learning|RiDEx: Reward-Informed Directional Exploration for Diffusion Reinforcement Learning]]
- **作者**: Song Yan, Chenfeng Wang, Wei Zhai, Xingchen Wang, Tao Zhang, Yawen Shao, Shi Pan, Min Li, Zheng-Jun Zha
- **cs 子类**: cs.CV, cs.LG
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.12（加权：强化学习 0.96，世界模型 0.16）
- **关联关键词**: RL

#### 研究背景与动机

《RiDEx: Reward-Informed Directional Exploration for Diffusion Reinforcement Learning》归入 强化学习、世界模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Computer Vision and Pattern Recognition 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：ExploreNet, GenEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reward-based diffusion post-training updates model parameters from task rewards. While existing approaches improve sampling and policy optimization, they still rely largely on isotropic random perturbations in a high-dimensional latent space for exploration. Such variation often spends the perturbation budget on changes with little influence on the target reward, making exploration inefficient. We study where diffusion models should explore and how to learn from that exploration. We introduce Reward-Informed Directional Exploration (RiDEx), which concentrates local exploration in reward-relevant subspaces of the denoising velocity field. Conditional residuals or differentiable reward gradients propose the subspace, and equal-and-opposite perturbations at the same generation state measure its terminal reward response. The reward difference supplies signed local supervision in the explored coordinates, while all generated images contribute to global DiffusionNFT learning. RiDEx thereby couples exploration-space selection with feedback about the changes it produces. On Stable Diffusion 3.5 Medium, RiDEx attains the highest peak rewards among the evaluated methods on four alignment and preference tasks. Its gradient-direction instantiation achieves 15x and 29x target-attainment speedups over DiffusionNFT on HPSv2 and PickScore, measured in H200 GPU hours. Controlled experiments confirm that reward-aligned directions elicit stronger responses at equal perturbation magnitude, and that applying their measured credit improves curve-average reward across all four tasks.

</details>

---

### [[20_Research/Papers/强化学习/HubEgo-100K_In-the-Wild_Egocentric_Video_of_Skilled_Work_for_Robot_Learning|HubEgo-100K: In-the-Wild Egocentric Video of Skilled Work for Robot Learning]]

![[assets/2611.21938_figure.png|800]]

- **arXiv**: [2611.21938](https://arxiv.org/abs/2611.21938)
- **PDF**: https://arxiv.org/pdf/2611.21938
- **详细分析**: [[20_Research/Papers/强化学习/HubEgo-100K_In-the-Wild_Egocentric_Video_of_Skilled_Work_for_Robot_Learning|HubEgo-100K: In-the-Wild Egocentric Video of Skilled Work for Robot Learning]]
- **作者**: Javad Amirian, Armin Kiani, Loïc Schaeffer, Tim Sprecher, Mohamed Taha, Karthik Yadati
- **cs 子类**: cs.CV, cs.LG, cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《HubEgo-100K: In-the-Wild Egocentric Video of Skilled Work for Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot policies trained by imitation generalize poorly outside the environments and objects seen in training. Published data-scaling studies find that generalization grows with the diversity of training environments and objects rather than with more demonstrations per environment. Robot data is costly to collect across many environments, whereas egocentric human video can be recorded in the wild at scale; existing egocentric video, however, mostly shows daily-life activity and contains little skilled work in real workplaces. We present HubEgo-100K, a dataset built for diversity. This version of the paper covers the first release, v1.0: 10,124 hours of 1080p egocentric video with synchronized 100 Hz inertial (IMU) data from one head-mounted phone camera. In v1.0, 12,227 contributors record their own unscripted work in 15,548 environments (each one contributor's own setting of one type, such as their kitchen or workshop) across 11 setting types, 30 work categories, 56 task types and 35 action families, with 83% of hours in workplace settings. The release comprises 72,754 episodes with machine-generated action and language annotations, in LeRobot and MCAP formats under CC BY 4.0. We measure diversity along each axis, show that inside v1.0, with episodes in random order, new contributors and words keep appearing, and relate the measurements to published evidence on six data properties tied to policy performance, including hand visibility and inertial sensing. We also document collection, curation, privacy measures and data format, and provide a datasheet. Later versions of this paper will add benchmarks and cover further releases toward 100,000 hours.

</details>

---

### [[20_Research/Papers/具身智能/Every_Camera_Grows_Up_Camera-Height_Regression_in_Interactive_Video_World_Models|Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models]]

![[assets/2611.21782_figure.png|800]]

- **arXiv**: [2611.21782](https://arxiv.org/abs/2611.21782)
- **PDF**: https://arxiv.org/pdf/2611.21782
- **详细分析**: [[20_Research/Papers/具身智能/Every_Camera_Grows_Up_Camera-Height_Regression_in_Interactive_Video_World_Models|Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models]]
- **作者**: Sheng Lu, Guangpin Tao, Tong Lu, Ying Tai
- **cs 子类**: cs.CV
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 大模型, 机器人
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.2，世界模型 0.8，机器人 0.2）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Every Camera Grows Up: Camera-Height Regression in Interactive Video World Models》归入 世界模型、具身智能、大模型 方向。该论文围绕 Computer Vision and Pattern Recognition 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Habitat-Sim, LingBot-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Interactive video world models serve as simulators for embodied agents: from a starting image and an action trajectory, they generate the views the agent would see. The starting image fixes how high the camera is, for example 0.15 m for a floor robot or 2.2 m for an overhead camera, and a faithful simulator must keep this height as the camera moves. We show that six recent open-weight models fail to do so: as motion replaces the starting view with generated content, they move the camera toward human eye level, a failure we call camera-height regression. Our benchmark, EyeHeight, pairs six rendered elevations (0.15 m to 2.2 m) and four calibrated real-world rig heights with scale-free multi-view height estimation. All six models lose their initial height during a $180^\circ$ turn-and-walk rollout: initialized at 0.15 m, only 0-20% of clips end within $1.3\times$ of the starting height as inferred viewpoints converge to human heights of 1.1 m to 1.5 m, whereas ground-truth renders remain within a few percent. In Matrix-Game models, homography-tracked floor motion stays consistent with constant elevation during rotation even as newly outpainted room geometry yields a higher reconstructed viewpoint. Regression grows with rotation angle, begins while the start frame remains in context, and largely reverses in SANA-WM when a $360^\circ$ turn restores the initial view. We trace this pull to human-centric video priors in which floor-level views are nearly absent: in SANA-WM, textual height cues and dense floor-disparity maps do not prevent it, whereas classifier-free text guidance during the first half of denoising strengthens it. Combining unguided sampling with height-balanced fine-tuning recovers more retention but costs 5 MUSIQ points, a loss fixed during those same early steps. Viewpoint drift alone shifts the paths predicted by visual navigation policies.

</details>

---
