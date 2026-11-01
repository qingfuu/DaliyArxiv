# cs.RO | Robotics | 2026-10-30

#arxiv #ComputerScience

**论文数**: 44

### [[20_Research/Papers/具身智能/SwapBot_Tool-Centric_Robot_Manipulation_via_Interchangeable_End-Effectors_and_Tactile_Sensing|SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing]]

![[assets/2610.40646_figure.jpg|800]]

- **arXiv**: [2610.40646](https://arxiv.org/abs/2610.40646)
- **PDF**: https://arxiv.org/pdf/2610.40646
- **详细分析**: [[20_Research/Papers/具身智能/SwapBot_Tool-Centric_Robot_Manipulation_via_Interchangeable_End-Effectors_and_Tactile_Sensing|SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing]]
- **作者**: Yunchu Zhang, Ray Song, Junhan Jiao, Liyiming Ke, Yuchen Yang, Ruihan Gao, Emma Romig, Siddhartha Srinivasa, Yiyue Luo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《SwapBot: Tool-Centric Robot Manipulation via Interchangeable End-Effectors and Tactile Sensing》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot manipulation in everyday environments inherently involves substantial tool usage. Seemingly simple household tasks, such as cooking pan-fried tofu, require forceful cutting, delicate brushing, and precise placement using different tools under contact-rich interaction. Thus, the ability to autonomously swap and use task-appropriate tools is important for tool-centric manipulation. We introduce SwapBot, a modular, tool-centric end effector system featuring low-cost adapters that quickly convert common household tools into robot end effectors. Rather than pursuing a single universal gripper, SwapBot adopts a unified design principle that combines a fixed robot-side coupling interface with low-cost, tool-side adapters, enabling compatibility with diverse tools, including articulated ones, and multiple robot platforms. Each adapter integrates compact tactile sensors, supports fast autonomous swapping, and interfaces with an intuitive teleoperation system for efficient demonstration collection. User studies show that, during teleoperation, SwapBot reduces task completion time and operator workload. Using collected demonstrations on the robot, we train imitation learning policies to successfully perform tool-centric tasks like cooking tofu, stirring salad, flipping meat. Our ablation study shows that using tactile-augmented demonstrations improves policy performance across contact-rich skills, increasing success rates by 15 to 25 percentage points over RGB-only policies. These results highlight modular, tactile-equipped tools as a practical and extensible pathway toward robust and capable robot manipulation. Project website https://personalrobotics.github.io/SwapBot.

</details>

---

### [[20_Research/Papers/机器人/PhysVLMM_Interaction-Conditioned_Physical_Belief_Maps_for_Articulated_Objects_in_Robot_Scene_Maps|PhysVLMM: Interaction-Conditioned Physical Belief Maps for Articulated Objects in Robot Scene Maps]]

![[assets/2610.40539_figure.png|800]]

- **arXiv**: [2610.40539](https://arxiv.org/abs/2610.40539)
- **PDF**: https://arxiv.org/pdf/2610.40539
- **详细分析**: [[20_Research/Papers/机器人/PhysVLMM_Interaction-Conditioned_Physical_Belief_Maps_for_Articulated_Objects_in_Robot_Scene_Maps|PhysVLMM: Interaction-Conditioned Physical Belief Maps for Articulated Objects in Robot Scene Maps]]
- **作者**: Dibyendu Ghosh
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《PhysVLMM: Interaction-Conditioned Physical Belief Maps for Articulated Objects in Robot Scene Maps》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GAPartNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Mobile robots must open doors and drawers, yet their scene maps record what each object is and whether it has moved, not how it will respond to a pull. This paper proposes PhysVLMM, a method that maintains a physical belief for every articulated part of a Vision-Language-Motion Map and answers a planner's queries about it, with two algorithms: a map update and a query. Watching a part move provably cannot identify its dynamics, and a measured pull identifies only the pulled part, up to one direction. PhysVLMM therefore (i) keeps that direction as a posterior instead of a point estimate, (ii) passes the evidence of each pull in closed form to the untouched look-alike parts of the map, and (iii) answers whether an action will succeed at a stated risk, or abstains. On real doors and drawers in 18 homes, it identifies the joint type in 86% of held-out pulls (48% for a learned single-view method) and predicts the response to a pull with 41% lower error than differentiable simulation (CRPS 0.323 vs. 0.544), four orders of magnitude faster (13 ms vs. 230 s per case). The posterior lowers the final-position error from 0.460 to 0.270, sharing lowers the force error of untouched parts from 56% to 42%, and at every stated risk from 0.02 to 0.30 the false-safe answers stay within it. Pooling all measured parts of a home does as well as the look-alike groups, and simpler variants predict where a pulled part stops at least as well.

</details>

---

### [[20_Research/Papers/机器人/Optimal_Path_Planning_with_Localization_constraints|Optimal Path Planning with Localization constraints]]

![[assets/2610.40429_figure.png|800]]

- **arXiv**: [2610.40429](https://arxiv.org/abs/2610.40429)
- **PDF**: https://arxiv.org/pdf/2610.40429
- **详细分析**: [[20_Research/Papers/机器人/Optimal_Path_Planning_with_Localization_constraints|Optimal Path Planning with Localization constraints]]
- **作者**: Chinmay Mundane, Manav Mishra, PB Sujit
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Optimal Path Planning with Localization constraints》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper studies UAV path planning in areas where GPS signals are not present. Because these drones can easily get lost when they don't have GPS, they must rely on dead reckoning and occasionally pass near cellular towers, which act as landmarks to reset and fix their position. The goal is to find the shortest path from a start to a goal location while keeping the estimation uncertainty within a given bound. To solve this problem, we propose a localization-constrained A* planner that treats uncertainty as a hard constraint during search. The robot state and covariance are propagated using an Extended Kalman Filter (EKF), and only paths that satisfy the covariance limit are considered. We also show that the proposed method does not affect heuristic used in A* and remains admissible and consistent, ensuring optimality among all feasible paths. Extensive Monte Carlo simulations and PyBullet quadrotor test show that the proposed method finds shorter and more reliable paths compared to RRT* and PRM, while always satisfying the uncertainty constraint.

</details>

---

### [[20_Research/Papers/机器人/Securing_the_Robotics_Supply_Chain|Securing the Robotics Supply Chain]]

![[assets/2610.40385_first_page.png|800]]

- **arXiv**: [2610.40385](https://arxiv.org/abs/2610.40385)
- **PDF**: https://arxiv.org/pdf/2610.40385
- **详细分析**: [[20_Research/Papers/机器人/Securing_the_Robotics_Supply_Chain|Securing the Robotics Supply Chain]]
- **作者**: Cindy L. Bethel, Henrik I. Christensen, Odest Chadwicke Jenkins, George Pappas, Holly Yanco, Haley Griffin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Securing the Robotics Supply Chain》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper sets out what a sustained federal research and investment agenda would need to include to close that gap--not within a single budget cycle, but over the decade such an undertaking will realistically require. It identifies where the gap is most pronounced today: in the methods needed to verify and certify components of uncertain origin, in the foundational hardware research that has long been underfunded relative to software, in the physical infrastructure researchers need to test systems at scale, and in the workforce required to build and sustain all of it. Robotics should not be treated merely as a downstream beneficiary of a broader artificial intelligence investment strategy. It constitutes its own supply chain, with its own points of failure, and merits its own sustained federal commitment.

</details>

---

### [[20_Research/Papers/具身智能/TouchBridge_Tactile-Conditioned_Human-to-Robot_Transfer_for_Dexterous_Manipulation|TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation]]

![[assets/2610.40349_figure.png|800]]

- **arXiv**: [2610.40349](https://arxiv.org/abs/2610.40349)
- **PDF**: https://arxiv.org/pdf/2610.40349
- **详细分析**: [[20_Research/Papers/具身智能/TouchBridge_Tactile-Conditioned_Human-to-Robot_Transfer_for_Dexterous_Manipulation|TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation]]
- **作者**: Haozhe Zhang, Gu Zhang, Zirui Zou, Yuzheng Chen, Jinlong Wu, Zixuan Hu, Jianke Zhang, Yucheng Hu, Zhecheng Yuan, Huazhe Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 2.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《TouchBridge: Tactile-Conditioned Human-to-Robot Transfer for Dexterous Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human demonstrations offer an efficient and scalable source of data for dexterous robot manipulation, but differences in sensing and hand morphology complicate the transfer of contact-rich interactions. We present TouchBridge, a hardware--software co-designed framework for human-to-robot data transformation. A wearable human demonstration interface and a corresponding robot interface establish cross-embodiment correspondence in visual and fingertip tactile sensing. We introduce Tac-Retarget, a tactile-conditioned retargeting method that uses measured contact to align fingertip contact patches and preserve their spatial relations within and across hands. Unlike object-aware or simulation-based transfer pipelines, Tac-Retarget requires no object mesh, object-pose estimate, or physics simulation for retargeting, enabling direct and scalable conversion of human demonstrations into robot-domain training data. Combined with visual synthesis and camera-anchored action conversion, TouchBridge produces robot-domain demonstrations for fine-tuning a pretrained vision-language-action (VLA) model. Across four real-world contact-rich tasks, policies fine-tuned solely on TouchBridge-converted human demonstrations achieve a 72.5% average success rate, compared with 77.5% using an equal number of teleoperated robot demonstrations, while human demonstration collection is 7.0x faster. Under the same policy and training setup, Tac-Retarget outperforms DexPilot and UniDex by 25.0 and 42.5 percentage points, respectively.

</details>

---

### [[20_Research/Papers/具身智能/MUSBRIC_LEGO-Compatible_Pneumatic_Muscle_Bricks_for_Reconfigurable_Musculoskeletal_Robots|MUSBRIC: LEGO-Compatible Pneumatic Muscle Bricks for Reconfigurable Musculoskeletal Robots]]

![[assets/2610.40285_figure.png|800]]

- **arXiv**: [2610.40285](https://arxiv.org/abs/2610.40285)
- **PDF**: https://arxiv.org/pdf/2610.40285
- **详细分析**: [[20_Research/Papers/具身智能/MUSBRIC_LEGO-Compatible_Pneumatic_Muscle_Bricks_for_Reconfigurable_Musculoskeletal_Robots|MUSBRIC: LEGO-Compatible Pneumatic Muscle Bricks for Reconfigurable Musculoskeletal Robots]]
- **作者**: Qiyao Wang, Yinglei Zhu, Liang Zhou, Wenzhe Gong, Xin-Jun Liu, Huichan Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.9，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《MUSBRIC: LEGO-Compatible Pneumatic Muscle Bricks for Reconfigurable Musculoskeletal Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Musculoskeletal robots combine compliant actuators with articulated skeletons, but exploring alternative configurations often requires repeated fabrication. We present MUSBRIC, a modular hardware platform and accompanying MuJoCo-based simulator for reconfigurable musculoskeletal robots. LEGO-compatible endcaps turn fiber-reinforced extensile pneumatic artificial muscles into reusable, plug-and-play muscle bricks that connect directly to standard LEGO components. Experimentally identified actuator behavior supports corresponding musculoskeletal simulations. An elbow-joint prototype validates load-dependent flexion and extension, showing that pulley-guided routing enables reversible motion and a mechanical stop stabilizes the straight posture. A robotic hand demonstrates compliant grasping and multi-joint construction. Matched hardware and simulation sweeps across 15 leg configurations demonstrate systematic exploration of attachment geometry, while a quadruped assembled from four legs demonstrates walking. Together, these demonstrations span mechanism analysis, configuration exploration, and functional robot construction within a single reconfigurable system. The hardware designs and simulation code will be released as open source soon to facilitate reproduction and further development.

</details>

---

### [[20_Research/Papers/强化学习/AcrossDEX_1.0_From_Human_Motion_Pretraining_to_Bimanual_Dexterous_Manipulation_across_Hand_Embodiments|AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments]]

![[assets/2610.40210_figure.png|800]]

- **arXiv**: [2610.40210](https://arxiv.org/abs/2610.40210)
- **PDF**: https://arxiv.org/pdf/2610.40210
- **详细分析**: [[20_Research/Papers/强化学习/AcrossDEX_1.0_From_Human_Motion_Pretraining_to_Bimanual_Dexterous_Manipulation_across_Hand_Embodiments|AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments]]
- **作者**: Xiaoyu Yang, Nan Wu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《AcrossDEX 1.0: From Human Motion Pretraining to Bimanual Dexterous Manipulation across Hand Embodiments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual dexterous manipulation requires continuous coordination of wrist motion, finger contact, and object motion. Human videos provide rich manipulation experience. Using this experience for robot control requires aligning human poses with robot commands and accounting for embodiment-specific kinematics and contact dynamics. We present AcrossDEX 1.0, a learning system that connects human motion pretraining, simulation-based expert learning, robot demonstration collection, and visual closed-loop execution. Pretraining on HOT3D Aria predicts one second of bimanual motion from five images and thirty annotated hand states over the preceding second. Robot adaptation preserves the visual encoder, temporal backbone, and wrist parameters. Shared wrist representations, separate finger fields, and validity masks support both six-channel Inspire hands and sixteen-joint Allegro hands. The robot policy predicts sixty control targets from frontal images, command history, and task conditions. It executes a prefix and replans from updated observations. We compare direct regression, diffusion, and flow matching on lid opening and return and closed-lid object reorientation. Direct regression achieves success rates of 40.6\% for opening and return, 100.0\% for Inspire reorientation, and 93.3\% for Allegro reorientation. Flow matching achieves 90.0\% on Allegro reorientation. Paired comparisons further show that constraining replanning with the previous plan improves the continuous execution of generative policies. These results demonstrate a common adaptation pipeline for two hand embodiments and highlight the roles of contact coordination and action-chunk continuity.

</details>

---

### [[20_Research/Papers/机器人/RoboAtom_Large-scale_Atomic-Action_Supervision_for_Robot_Learning|RoboAtom: Large-scale Atomic-Action Supervision for Robot Learning]]

![[assets/2610.40207_figure.png|800]]

- **arXiv**: [2610.40207](https://arxiv.org/abs/2610.40207)
- **PDF**: https://arxiv.org/pdf/2610.40207
- **详细分析**: [[20_Research/Papers/机器人/RoboAtom_Large-scale_Atomic-Action_Supervision_for_Robot_Learning|RoboAtom: Large-scale Atomic-Action Supervision for Robot Learning]]
- **作者**: Xueyuan Wei, Xuanxu Wang, Xudong Li, Yuping He, Wanshui Gan, Jiaqi Peng, Wenqi Guo, Jianjun Zhou, Junting Dong, Chunhua Shen, Haoyu Guo, Mulin Yu...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《RoboAtom: Large-scale Atomic-Action Supervision for Robot Learning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Open-World, RoboAtom-Bench, Test-Set, WGO-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fine-grained action annotations can support skill reuse and compositional generalization in robot policies. However, robot datasets typically provide task-level instructions without subtask annotations. Although some include subtask labels, inconsistent formats and conventions hinder cross-source joint training. We propose RoboAtom-Data, which adds unified, time-aligned atomic-action annotations to existing data from multiple sources, covering 1.45 million trajectories, 6.88 million skill-labeled segments, and 16,882.1 hours. Our pipeline combines a unified protocol, large-scale manual annotation, propagation across repeated executions with the same ordered skill sequence, and multi-stage quality control. We evaluate the dataset through automatic atomic-action annotation and robot control. We construct RoboAtom-Bench to standardize evaluation of skill recognition and temporal boundary localization. Trained on the annotated data, RoboAtom-Anno achieves better automatic annotation performance than all evaluated open- and closed-source models on both RoboAtom-Bench and the external WGO-Bench. For robot control, atomic-action supervision paired with hierarchical execution improves task success over task-level baselines on LIBERO-Long, LIBERO-Plus, and RoboTwin. We will release the data, benchmark, model, and construction pipeline to support further research on skill-level robot learning.

</details>

---

### [[20_Research/Papers/具身智能/RoboSeed_Multidimensional_Evaluation_of_Vision-Language-Action_and_World-Action_Models_Capability,_Resource_Affordability,_and_Research_Evid|RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence]]

![[assets/2610.40026_figure.png|800]]

- **arXiv**: [2610.40026](https://arxiv.org/abs/2610.40026)
- **PDF**: https://arxiv.org/pdf/2610.40026
- **详细分析**: [[20_Research/Papers/具身智能/RoboSeed_Multidimensional_Evaluation_of_Vision-Language-Action_and_World-Action_Models_Capability,_Resource_Affordability,_and_Research_Evid|RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence]]
- **作者**: Xin Ma, Furong Chen, Xinlong Man, Bo Zhang, Yalong Guo, Haolan Lei, Chaochen Cui, Hongyuan Zhang, Mulin Chen, Yi Wang, Lap-pui Chau, Chuang Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《RoboSeed: Multidimensional Evaluation of Vision-Language-Action and World-Action Models: Capability, Resource Affordability, and Research Evidence》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：LingBot-VLA, OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Choosing a robot action model requires evidence about task capability, adaptation cost, deployment requirements, and the reliability of reported conclusions. Success rates alone offer limited guidance to researchers with different computing budgets and goals. We propose RoboSeed, a multidimensional evaluation framework for vision-language-action (VLA) and world-action models (WAM), within a continuing program to train, evaluate, and openly release robot models with verifiable evidence for model selection. The framework defines five dimensions: capability, downstream training affordability, deployment affordability, locally verified research value, and reproduction evidence. It maps empirical measurements and audit criteria to 0-100 profiles using fixed normalization anchors, with balanced, training-constrained, and deployment-constrained preference settings. Interface and protocol checks establish when comparisons are appropriate. Missing measurements remain explicit, incomplete aggregate scores are withheld, and weighted input coverage identifies evidence gaps. We apply the framework to representative VLA and WAM models, drawing on local training, released-weight evaluation, task-level audits, and an evaluation-system study. The results reveal budget-dependent backbone choices, sensitivity to adaptation recipes, and differences between language and visual task interfaces. Reproducible scoring code and machine-readable evidence support extension to additional models. The study provides dimension-level assessments and priorities for further measurement, while incomplete serving traces and heterogeneous protocols preclude overall numerical rankings.

</details>

---

### [[20_Research/Papers/具身智能/LOGIV_Graph-Verified_Execution_with_Causal_Local_Repair_for_Long-Horizon_Robot_Tasks|LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks]]

![[assets/2610.40016_figure.png|800]]

- **arXiv**: [2610.40016](https://arxiv.org/abs/2610.40016)
- **PDF**: https://arxiv.org/pdf/2610.40016
- **详细分析**: [[20_Research/Papers/具身智能/LOGIV_Graph-Verified_Execution_with_Causal_Local_Repair_for_Long-Horizon_Robot_Tasks|LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks]]
- **作者**: Enqiao Lu, Yuxiang Xie, Xingrui Yu, Yuyang Wang, Yipeng Gu, Zhenglin Wan, Pengfei Zhou, Wangbo Zhao, Yang You, Yuxiang Gao, Ivor Tsang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《LOGIV: Graph-Verified Execution with Causal Local Repair for Long-Horizon Robot Tasks》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic robots must turn a high-level goal into actions while keeping the physical conditions needed for future steps valid. A completed action does not ensure that its effects will persist: a later disturbance can invalidate support that the remaining plan still assumes. We present LOGIV, a graph engineering framework for agentic robot execution that uses an explicit task graph to connect symbolic planning, observation-based verification, and embodied action. LOGIV compiles a validated plan into condition-support and resource-ordering edges, checks their physical validity during execution, and uses dependency tracing to determine what must be restored after a failure. Repair is constrained by retained unfinished actions, and the combined continuation is symbolically validated before execution resumes. The framework operates above existing Vision-Language-Action (VLA) and World Action Model (WAM) policies without adding trainable components. Across 20 dual-arm tasks from RoboTwin~V2 and BiCoord with three execution backbones, LOGIV improves mean task success without injected disturbances by 10.67 and 15.33 percentage points, respectively. Under predefined perturbations, it achieves higher task completion and condition restoration than three adapted recovery baselines for every backbone on both benchmarks. On three real-robot tasks, successful trials increase from 12/30 to 17/30. These results support explicit, continuously checked task dependencies as a practical interface for reliable agentic robot execution.

</details>

---

### [[20_Research/Papers/强化学习/Humanoid_Dodgeball_Learning_Fast_Dynamic_Obstacle_Avoidance_Motions_for_Humanoids|Humanoid Dodgeball: Learning Fast Dynamic Obstacle Avoidance Motions for Humanoids]]

![[assets/2610.40003_figure.png|800]]

- **arXiv**: [2610.40003](https://arxiv.org/abs/2610.40003)
- **PDF**: https://arxiv.org/pdf/2610.40003
- **详细分析**: [[20_Research/Papers/强化学习/Humanoid_Dodgeball_Learning_Fast_Dynamic_Obstacle_Avoidance_Motions_for_Humanoids|Humanoid Dodgeball: Learning Fast Dynamic Obstacle Avoidance Motions for Humanoids]]
- **作者**: Aoqian Zhang, Chunzheng Wang, Haoran Chen, Annan Tang, Cheng Xiang, Fan Shi, Shuzhi Sam Ge
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: RL, Security

#### 研究背景与动机

《Humanoid Dodgeball: Learning Fast Dynamic Obstacle Avoidance Motions for Humanoids》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoids have become increasingly agile and capable in real-world environments. To operate safely in dynamic scenarios, they must rapidly evade fast-moving obstacles while maintaining stability and physically feasible whole-body motion. Learning such behaviors remains challenging due to the high-dimensional dynamics of humanoid systems and the need to jointly balance reactive obstacle avoidance, motion naturalness, and control robustness. In this work, we present Humanoid Dodgeball, a reinforcement learning (RL) framework for agile dynamic obstacle avoidance in humanoids. Our method enables highly dynamic whole-body evasive maneuvers against incoming projectiles through threat-aware reward shaping, while multiple direction-specific adversarial motion priors regularize the learned behaviors toward stable and diverse human-like motions. Extensive simulation and hardware experiments demonstrate that the proposed framework substantially improves dynamic obstacle avoidance performance across diverse obstacle speeds and launch distances, while preserving robust and physically plausible humanoid motions.

</details>

---

### [[20_Research/Papers/具身智能/Gaze-Assisted_Supervisory_Control_for_Lunar_Robotic_Arm_Teleoperation_Under_Concurrent_Monitoring|Gaze-Assisted Supervisory Control for Lunar Robotic Arm Teleoperation Under Concurrent Monitoring]]

![[assets/2610.39998_figure.png|800]]

- **arXiv**: [2610.39998](https://arxiv.org/abs/2610.39998)
- **PDF**: https://arxiv.org/pdf/2610.39998
- **详细分析**: [[20_Research/Papers/具身智能/Gaze-Assisted_Supervisory_Control_for_Lunar_Robotic_Arm_Teleoperation_Under_Concurrent_Monitoring|Gaze-Assisted Supervisory Control for Lunar Robotic Arm Teleoperation Under Concurrent Monitoring]]
- **作者**: Jiayu He, Yifan Li, Oliver R. Runswick, Ernest N. Kamavuako, Yunjie Jia, Peter D. Hodkinson, Yang Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Gaze-Assisted Supervisory Control for Lunar Robotic Arm Teleoperation Under Concurrent Monitoring》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rover-mounted robotic arms can extend human reach during lunar sample handling, but continuous joystick teleoperation requires repeated visual-motor alignment while operators may also need to monitor system states. This paper presents a gaze-assisted supervisory control framework in which gaze nominates a rock or placement target, explicit confirmation authorizes the action, and the robot performs bounded autonomous grasp-and-place execution. The framework was evaluated against manual joystick teleoperation in a mission-analog virtual reality study with 16 participants. The study used a 2 x 2 x 3 within-subject design varying control mode, placement difficulty, and concurrent monitoring load. Mean recorded task completion time decreased from 47.65 to 18.43 s per rock, with 72.5% of this difference arising during grasping. Under the tested auditory monitoring conditions, gaze-assisted supervisory control showed less average proportional slowing, with no detected control-mode difference in monitoring-response accuracy or speed. The rate of gaze shifts between core areas of interest decreased from 49.98 to 27.73 shifts/min, while the raw NASA Task Load Index score decreased from 32.54 to 18.26. However, the benefit was task dependent. In precision placement, manual control yielded lower mean placement error and a higher placement success rate. These findings support a mixed-initiative allocation in which gaze enables rapid task-level intention specification and autonomous execution, while precision-critical stages retain manual refinement.

</details>

---

### [[20_Research/Papers/机器人/Compressed_Orientation_Reachability_Maps_for_Sub-Second_Robotic_Needle_Entry_Point_Planning|Compressed Orientation Reachability Maps for Sub-Second Robotic Needle Entry Point Planning]]

![[assets/2610.39879_figure.png|800]]

- **arXiv**: [2610.39879](https://arxiv.org/abs/2610.39879)
- **PDF**: https://arxiv.org/pdf/2610.39879
- **详细分析**: [[20_Research/Papers/机器人/Compressed_Orientation_Reachability_Maps_for_Sub-Second_Robotic_Needle_Entry_Point_Planning|Compressed Orientation Reachability Maps for Sub-Second Robotic Needle Entry Point Planning]]
- **作者**: Prabhu Nithin Gollapudi, Andreas Maier, Franziska Mathis-Ullrich, Water Zhao, Jia Wang, Siming Bayer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Compressed Orientation Reachability Maps for Sub-Second Robotic Needle Entry Point Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In the context of multi-stage trajectory planning for robotic percutaneous liver interventions, identifying a kinematically feasible entry point remains a critical computational bottleneck. Existing methods rely on exhaustive inverse kinematics or randomized searches, incurring delays of 13 to 27 seconds per target and limiting real-time intraoperative adaptation. This paper introduces an Orientation-Based Reachability Map (ORM) that precomputes the kinematic feasibility of a 6 Degrees of Freedom (DoF) serial manipulator across 188,873 workspace positions and encodes orientation feasibility into a compact, indexed 83 MB map. A Just-In-Time (JIT) compiled runtime pipeline replaces live optimization with near-instantaneous array lookups. Experimental evaluation demonstrates a reduction in planning latency from 13.5-26.9 s to 0.289-0.349 s per target while maintaining high geometric fidelity, achieving a mean convex hull volume overlap ratio of 0.933 and a mean alpha-shape volume ratio of 0.976 relative to the baseline reachable point cloud. The proposed ORM framework enables sub-second entry point planning and provides an efficient computational framework for robotic needle insertion in percutaneous liver ablation.

</details>

---

### [[20_Research/Papers/大模型/Teaching_a_Tree_to_Recover_Online_Distillation_of_an_LLM_Supervisor_with_Counterfactual_Replay|Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay]]

![[assets/2610.39775_figure.png|800]]

- **arXiv**: [2610.39775](https://arxiv.org/abs/2610.39775)
- **PDF**: https://arxiv.org/pdf/2610.39775
- **详细分析**: [[20_Research/Papers/大模型/Teaching_a_Tree_to_Recover_Online_Distillation_of_an_LLM_Supervisor_with_Counterfactual_Replay|Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay]]
- **作者**: Kristian Ceder, Kilian Freitag, Knut Åkesson
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《Teaching a Tree to Recover: Online Distillation of an LLM Supervisor with Counterfactual Replay》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous mobile robots commonly pair a global planner with a local model predictive controller (MPC), but nonconvex obstacle avoidance and a limited horizon can make the robot freeze in complex layouts. Deciding whether to replan, wait, or call for help is a supervisory decision. Recent work queries a large language model (LLM) supervisor on every anomaly, which is slow and costly. We instead distill the LLM online into a decision tree. After each training episode, counterfactual replay labels recoveries as needed, unnecessary, or harmful. These labels retire unhelpful rules. In simulation, on 20 unseen layouts where the MPC alone freezes, the tree handles at least 18 correctly across all seeds, either by reaching the goal or by calling for help when no feasible path exists. The tree matches both an always-query LLM supervisor and expert-designed rules, while issuing no LLM queries at test time. Handwritten rules cannot anticipate the long tail of situations a physical robot will encounter. Online distillation is a promising remedy: the tree handles familiar cases, and the LLM is consulted only for new ones, whose validated recoveries become new rules. Language models can thus also serve as designers of supervisors rather than only as runtime supervisors.

</details>

---

### [[20_Research/Papers/机器人/AFast_Robot_Localization_Method_Based_on_Monte_Carlo_Sampling|AFast Robot Localization Method Based on Monte Carlo Sampling]]

![[assets/2610.39708_figure.png|800]]

- **arXiv**: [2610.39708](https://arxiv.org/abs/2610.39708)
- **PDF**: https://arxiv.org/pdf/2610.39708
- **详细分析**: [[20_Research/Papers/机器人/AFast_Robot_Localization_Method_Based_on_Monte_Carlo_Sampling|AFast Robot Localization Method Based on Monte Carlo Sampling]]
- **作者**: He Zhaoqing, Hang Li, Xian Pu, Li Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《AFast Robot Localization Method Based on Monte Carlo Sampling》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Localization is an essential capability of intelligent robots. However, in real-world constrained environments, robots often cannot rely on external localization systems. Therefore, this paper proposes an online particle-filter localization method based on Monte Carlo sampling. The method is applied to the localization of a mobile robot in a maze environment and requires only four range sensors mounted on the front, rear, left, and right sides of the vehicle, without the need for any heading information. Simulation experiments demonstrate that even in a maze where local regions are highly similar, the vehicle can still achieve relatively accurate localization, thereby providing a fast and effective approach for robot localization in complex environments.

</details>

---

### [[20_Research/Papers/具身智能/AI_for_Science_in_Space_Orbital_Laboratories,_Planetary_Fieldwork,_and_Embodied_Autonomy|AI for Science in Space: Orbital Laboratories, Planetary Fieldwork, and Embodied Autonomy]]

![[assets/2610.39689_first_page.png|800]]

- **arXiv**: [2610.39689](https://arxiv.org/abs/2610.39689)
- **PDF**: https://arxiv.org/pdf/2610.39689
- **详细分析**: [[20_Research/Papers/具身智能/AI_for_Science_in_Space_Orbital_Laboratories,_Planetary_Fieldwork,_and_Embodied_Autonomy|AI for Science in Space: Orbital Laboratories, Planetary Fieldwork, and Embodied Autonomy]]
- **作者**: Zizhe Wang, Jia Deng, Xin Lu, Zehao Jia, Yi Huang, Yao Zhu, Jianing Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《AI for Science in Space: Orbital Laboratories, Planetary Fieldwork, and Embodied Autonomy》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Artificial intelligence for science (AI4S) is extending from interpretation of existing data to the design and execution of experiments. Space offers distinctive scientific opportunities while restricting physical support. Microgravity and extraterrestrial environments expose phenomena that terrestrial experiments cannot fully reproduce; finite samples, constrained resources, and limited opportunities for intervention complicate sustained investigation. This critical review examines orbital laboratories and planetary in situ science across biology, materials, fluid and thermal physics, and adaptive exploration. We distinguish learning from space-derived data, selecting scientific actions, executing them, and preserving experimental validity. Terrestrial self-driving laboratories provide complementary evidence on optimization, dedicated automation, robotic manipulation, and the support needed for unattended operation. The synthesis connects scientific gains already demonstrated by bounded AI systems to gaps in observation, executable actions, and continuity of valid evidence. Space robots can expand the attainable scope of autonomous science when necessary interventions exceed validated instrument capabilities and timely human support is unavailable. Their value must be established against dedicated mechanisms, redundancy, and human-supported operation. We develop a framework connecting sample history, scientific decisions, physical execution, and claim-specific validity. A worked orbital design, a planetary extension, and matched evaluation schemes separate the contributions of sensing, decision policies, and physical actions. The resulting agenda measures autonomy through valid scientific return, task coverage, intervention costs, and evidence integrity across complete campaigns.

</details>

---

### [[20_Research/Papers/机器人/Kinematic-Tactile_Aligned_Dexterous_Retargeting_with_Contact_Wrench_Space_Alignment|Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment]]

![[assets/2610.39582_figure.png|800]]

- **arXiv**: [2610.39582](https://arxiv.org/abs/2610.39582)
- **PDF**: https://arxiv.org/pdf/2610.39582
- **详细分析**: [[20_Research/Papers/机器人/Kinematic-Tactile_Aligned_Dexterous_Retargeting_with_Contact_Wrench_Space_Alignment|Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment]]
- **作者**: Xinyuan He, Ziheng Xu, Yueyuan Chen, Yufan Ye, Yuanshuo Tan, Huiming Pan, Jianjun Meng, Shuo Jiang, Peter B. Shull
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Kinematic-Tactile Aligned Dexterous Retargeting with Contact Wrench Space Alignment》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AET-TacNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human demonstrations provide a natural and scalable source of data for learning dexterous manipulation policies. However, existing retargeting methods primarily transfer human kinematics, while the tactile information underlying physical interaction is rarely preserved across embodiments. To address this limitation, we present a hierarchical three-stage framework for kinematic-tactile aligned dexterous retargeting. We use object-centric contact wrench space as a physical representation for tactile alignment between human and robot hands. The framework first aligns hand kinematics and contact geometry, and then constructs a human wrench support profile from tactile forces and contact geometry. Robot fingertip force targets are subsequently optimized to cover the human wrench support and converted into joint position corrections, yielding directly replayable robot hand trajectories. We evaluate the framework in simulation and real robot experiments across three pouring conditions. In the real robot experiments, our method achieves a 96.7\% replay success rate and higher wrench transfer fidelity than representative retargeting baselines. The framework enables physically grounded transfer of kinematic and tactile information from human demonstrations to robot hands, providing a path toward scalable learning of contact-rich dexterous manipulation.

</details>

---

### [[20_Research/Papers/具身智能/From_Reasoning_to_Action_Consequence-Grounded_Alignment_for_Vision-Language-Action_Models|From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models]]

![[assets/2610.39543_figure.png|800]]

- **arXiv**: [2610.39543](https://arxiv.org/abs/2610.39543)
- **PDF**: https://arxiv.org/pdf/2610.39543
- **详细分析**: [[20_Research/Papers/具身智能/From_Reasoning_to_Action_Consequence-Grounded_Alignment_for_Vision-Language-Action_Models|From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models]]
- **作者**: Yixue Zhang, Wenke Xia, Kun Wu, Wenbo Yu, Pei Ren, Junnan Nie, Di Hu, Zhengping Che, Chang Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 2.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《From Reasoning to Action: Consequence-Grounded Alignment for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ERVLA, LaRA-VLA, VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reasoning informs decision-making by connecting intended actions with their expected consequences. Recent vision-language-action (VLA) models incorporate embodied chains of thought (ECoTs) to guide action generation. However, such guidance remains implicit, as actions are conditioned on ECoTs rather than explicitly optimized to align with them. We introduce CoRAct, a consequence-grounded reasoning-to-action alignment framework that explicitly aligns reasoning and action through reward-guided optimization in action noise space. CoRAct formulates two physically grounded ECoT components as verifiable signals: movement specifies intended motion, while waypoints encode expected spatial consequences. A unified Mixture-of-Transformers jointly models ECoT reasoning, action generation, and action-conditioned future prediction. For candidate actions generated from sampled noise, CoRAct computes alignment rewards based on movement consistency and agreement between predicted outcomes and specified waypoints. These rewards guide group-relative optimization of the initial noise distribution, steering action generation toward consistency with intended actions and expected consequences. Experiments across RoboCasa, VLABench, and real-world manipulation tasks demonstrate improvements in task success, generalization, and reasoning-execution alignment over strong ECoT-based VLA baselines. CoRAct also grounds externally provided ECoTs in executable behavior, enabling zero-shot adaptation to novel scenarios by leveraging knowledge from powerful vision-language models. Project page and dataset: https://onlyxingxingzyx.github.io/CoRAct/

</details>

---

### [[20_Research/Papers/具身智能/PRIME_W0_Physical_Priors_from_World_Models_for_Embodied_Manipulation|PRIME W0: Physical Priors from World Models for Embodied Manipulation]]

![[assets/2610.39528_figure.png|800]]

- **arXiv**: [2610.39528](https://arxiv.org/abs/2610.39528)
- **PDF**: https://arxiv.org/pdf/2610.39528
- **详细分析**: [[20_Research/Papers/具身智能/PRIME_W0_Physical_Priors_from_World_Models_for_Embodied_Manipulation|PRIME W0: Physical Priors from World Models for Embodied Manipulation]]
- **作者**: Huabin Peng, Fagang Jin, Yancong Wei, Tengfei Ma, Chuhang Liu, Chao Yu, Liqing Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 世界模型, 机器人, 大模型
- **相关性评分**: 3.0（加权：具身智能 1.8，大模型 0.1，世界模型 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《PRIME W0: Physical Priors from World Models for Embodied Manipulation》归入 具身智能、世界模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、世界模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GigaWorld, LingBot-VLA, LingBot-World, PokeVLA, RynnVLA, World-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models excel at instruction following, yet most remain feed-forward: they condition actions only on the current observation and discard both long-horizon temporal context and the hierarchical structure of VLM representations. We present PRIME W0, a hierarchical conditional flow-matching framework that closes this gap through three synergistic designs: (1)per-layer KV injection from a pretrained VLM into an Adaptive MoE action expert; (2)dynamics-aware conditioning via asynchronous world-model subgoal-image prediction and a DINOv2 historical-frame semantic bridge; and (3)Action Dynamic Manifold (ADM) flow matching with covariance-structured noise that respects robot kinematic coupling. PRIME W0 is trained in four stages---VLM pre-training, DAT/NTP visuomotor pre-training, DiT flow-matching decoder assembly with WM injection, and end-to-end SFT---and achieves state-of-the-art results on LIBERO and real-robot benchmarks, with systematic ablations validating each architectural component.

</details>

---

### [[20_Research/Papers/具身智能/Ask_to_Evolve_A_Unified_Harness_for_Lifelong_Embodied_Navigation_with_Hybrid_Action_Space_and_Persistent_Memory|Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory]]

![[assets/2610.39446_figure.png|800]]

- **arXiv**: [2610.39446](https://arxiv.org/abs/2610.39446)
- **PDF**: https://arxiv.org/pdf/2610.39446
- **详细分析**: [[20_Research/Papers/具身智能/Ask_to_Evolve_A_Unified_Harness_for_Lifelong_Embodied_Navigation_with_Hybrid_Action_Space_and_Persistent_Memory|Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory]]
- **作者**: Kai Sheng, Liuyi Wang, Jinlong Li, Haojie Dai, Chengju Liu, Qijun Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.8，大模型 0.3，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Ask to Evolve: A Unified Harness for Lifelong Embodied Navigation with Hybrid Action Space and Persistent Memory》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Giving embodied agents the freedom to act autonomously, initiate interactions, and understand their surroundings through experience is a step toward bringing them to life in the physical world. Realizing this vision requires action, interaction, and memory to work together, so that each encounter can inform current decisions and contribute experience for future tasks. We present EvoLife, a unified navigation harness that enables a multimodal embodied agent to choose how to move, when to ask, and what experience to carry forward. Its hybrid action space supports waypoint navigation, local discrete adjustments, pixel-based navigation, and object-directed navigation. Active interaction allows the agent to seek clarification or assistance when it encounters ambiguity or difficulty, while persistent spatial memory binds observations and dialogue to places, retaining useful experience to guide subsequent visits. We evaluate eight benchmarks across four task families: vision-language navigation, object navigation, interactive instance navigation, and continuous multi-task navigation. With an average of only 1.87 active interactions per episode, our method achieves a first-visit success rate (SR) of 100% across four 100-episode sets spanning vision-language navigation and object navigation. Complete-sequence SR reaches 98% on 50 LHPR-VLN sequences and 94% on 50 GOAT-Bench sequences. In the R2R revisit setting, success weighted by path length (SPL) increases from 82.23% to 93.31% with retained experience. Multi-day physical navigation further demonstrates exploration, proactive help-seeking, and revisiting remembered places. Together, these results advance the vision of bringing embodied agents to life through autonomous action, proactive interaction, and the accumulation and reuse of experience.

</details>

---

### [[20_Research/Papers/机器人/ScheduleGen_Demonstration_Generation_via_Skill_Scheduling_for_Multi-Arm_Imitation_Learning|ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning]]

![[assets/2610.39429_figure.png|800]]

- **arXiv**: [2610.39429](https://arxiv.org/abs/2610.39429)
- **PDF**: https://arxiv.org/pdf/2610.39429
- **详细分析**: [[20_Research/Papers/机器人/ScheduleGen_Demonstration_Generation_via_Skill_Scheduling_for_Multi-Arm_Imitation_Learning|ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning]]
- **作者**: Neel Jawale, Stephan Pleines, Soha Pouya, Yuke Zhu, Ajay Mandlekar, Caelan Garrett
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《ScheduleGen: Demonstration Generation via Skill Scheduling for Multi-Arm Imitation Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-arm robot platforms, including bimanual and humanoid robots, have the capability to complete tasks with lower cycle times than single-arm systems, but they are more difficult to safely control due to the presence of multi-arm constraints. The paradigm of training generalist robot policies from massive datasets is a promising approach to address general-purpose multi-arm manipulation, but the acquisition of large multi-arm manipulation datasets remains a bottleneck. Automated demonstration generation can alleviate this burden by synthesizing new demonstrations from a handful of source demonstrations, but existing algorithms ignore multi-arm constraints and as a result often induce unsafe and unsuccessful behaviors. We address this limitation by introducing ScheduleGen, an integrated planning &amp; scheduling algorithm for multi-arm demonstration generation. We evaluate ScheduleGen on 28 simulation task variants, including seven externally authored RoboDojo tasks and settings inaccessible to prior systems; it achieves 79.6% mean data-generation success and trains policies with 65.5% mean success. ScheduleGen policies outperform those trained on a state-of-the-art data generation baseline, and achieve 50-80% success across eight real-world variants through zero-shot sim-to-real and real-to-sim-to-real transfer. Videos and more at: https://schedulegen.github.io/

</details>

---

### [[20_Research/Papers/机器人/Information-Driven_Collaborative_Autonomy_for_Heterogeneous_UAV_UGV_Teams|Information-Driven Collaborative Autonomy for Heterogeneous UAV/UGV Teams]]

![[assets/2610.39379_figure.png|800]]

- **arXiv**: [2610.39379](https://arxiv.org/abs/2610.39379)
- **PDF**: https://arxiv.org/pdf/2610.39379
- **详细分析**: [[20_Research/Papers/机器人/Information-Driven_Collaborative_Autonomy_for_Heterogeneous_UAV_UGV_Teams|Information-Driven Collaborative Autonomy for Heterogeneous UAV/UGV Teams]]
- **作者**: Joshua Yuriv Pilipovsky
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, ComputerVision, Systems

#### 研究背景与动机

《Information-Driven Collaborative Autonomy for Heterogeneous UAV/UGV Teams》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper considers coordinating a heterogeneous team of unmanned aerial vehicles (UAVs) and unmanned ground vehicles (UGVs) traversing a domain containing an unknown number of potentially hazardous targets. The UAVs provide aerial sensing using onboard optical cameras, adapting their trajectories to ground routes and target information. We formulate the aerial search problem using ergodic control, which distributes sensing effort according to a spatial information density to balance exploration and target localization. The formulation incorporates dynamic camera field-of-view footprints and pose-dependent probabilistic detection models. Angles-only measurements are processed through Bayesian inference and marginalization over data-association hypotheses to obtain a Poisson multi-Bernoulli (PMB) approximation of the target posterior, representing both detected and undetected targets. This belief directs aerial sensing toward unexplored regions along the ground routes and viewpoints that improve target localization. Ground planning combines chance-constrained target avoidance, enforced through confidence sets, with a void-probability objective that favors routes unlikely to contain threats. We solve each team's optimization problem in a fully decentralized manner using a nested SCvx*--C-ADMM scheme, with outer sequential convex programming iterations and inner distributed consensus optimization, accounting for nonlinearities, nonseparable objectives, and continuous-time inter-agent separation constraints. A closed-loop scheme updates both fleets' trajectories as information becomes available and permits ground motion when the remaining route risk falls below a prescribed threshold. Numerical case studies examine sensing geometry and target uncertainty, compare decentralized and centralized solvers, and demonstrate full closed-loop collaboration between multiple UAVs and UGVs.

</details>

---

### [[20_Research/Papers/强化学习/SONIC-K1_Porting_a_Universal_Humanoid_Motion_Tracker_to_a_Small_Humanoid_on_a_Single_GPU|SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU]]

![[assets/2610.39327_figure.jpg|800]]

- **arXiv**: [2610.39327](https://arxiv.org/abs/2610.39327)
- **PDF**: https://arxiv.org/pdf/2610.39327
- **详细分析**: [[20_Research/Papers/强化学习/SONIC-K1_Porting_a_Universal_Humanoid_Motion_Tracker_to_a_Small_Humanoid_on_a_Single_GPU|SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU]]
- **作者**: Kyrylo Kolesnichenko, Jong-Hoon Kim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SONIC-K1: Porting a Universal Humanoid Motion Tracker to a Small Humanoid on a Single GPU》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present SONIC-K1, to our knowledge the first open-weights whole-body motion tracker for the Booster K1 humanoid, obtained by adapting the SONIC framework to this smaller robot. The policy is trained from scratch on a single shared GPU with a small fraction of the compute reported for SONIC. In MuJoCo simulation, it tracks nearly all held-out motion clips and performs well on external benchmarks under SONIC's success criterion. On the real K1, it tracks upper-body and slow motions, while stepping and turning remain less reliable, and simulation experiments show a sensitivity to action latency. These results show broad motion-tracking capability on a modest training budget and point to quantitative hardware evaluation as the main next step. Code, policy weights and evaluation tools are publicly available.

</details>

---

### [[20_Research/Papers/大模型/ProLoop_Progress-Aware_Closed-Loop_Framework_via_Structured_State_Relations_for_Long-Horizon_Robotic_Task_Planning|ProLoop: Progress-Aware Closed-Loop Framework via Structured State Relations for Long-Horizon Robotic Task Planning]]

![[assets/2610.39319_figure.png|800]]

- **arXiv**: [2610.39319](https://arxiv.org/abs/2610.39319)
- **PDF**: https://arxiv.org/pdf/2610.39319
- **详细分析**: [[20_Research/Papers/大模型/ProLoop_Progress-Aware_Closed-Loop_Framework_via_Structured_State_Relations_for_Long-Horizon_Robotic_Task_Planning|ProLoop: Progress-Aware Closed-Loop Framework via Structured State Relations for Long-Horizon Robotic Task Planning]]
- **作者**: Runxin Zou, Qingmiao Liang, Jiatao Zhang, Xinyan Lv, Liangyu Qie, Meiyi Bu, Wei Song, Shiqiang Zhu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《ProLoop: Progress-Aware Closed-Loop Framework via Structured State Relations for Long-Horizon Robotic Task Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ALFWorld, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon robotic tasks are commonly decomposed into semantic subgoals to simplify planning. However, subgoal progress in LLM-based planning is typically inferred implicitly from interaction histories. Inaccurate estimates can misguide execution and allow local errors to propagate. To address this, we propose ProLoop, a Progress-Aware Closed-Loop framework that derives explicit subgoal progress from structured relations between desired and execution states. A learned State-Relation Monitor assesses these relations, which are then aggregated into subgoal progress as ongoing, deviated, or completed. The resulting progress guides execution adaptation, enabling reliable progress-aware control throughout execution. Experiments on AgentBoard ALFWorld and a real-world robotic platform show that ProLoop improves success rate by 12.94% overall and by 15.46% on Hard tasks, while reducing environment interactions by 32.3%.

</details>

---

### [[20_Research/Papers/具身智能/OpenFlyV2_An_onboard_vision-language-action_model_for_aerial_perception_and_navigation|OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation]]

![[assets/2610.39287_figure.png|800]]

- **arXiv**: [2610.39287](https://arxiv.org/abs/2610.39287)
- **PDF**: https://arxiv.org/pdf/2610.39287
- **详细分析**: [[20_Research/Papers/具身智能/OpenFlyV2_An_onboard_vision-language-action_model_for_aerial_perception_and_navigation|OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation]]
- **作者**: Junli Liu, Zhongrui You, Chenhui Li, Zhen Li, Yuyang Tian, Qizhen Chen, Delin Qu, Haoming Song, Dong Wang, Xuelong Li, Zhigang Wang, Bin Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《OpenFlyV2: An onboard vision-language-action model for aerial perception and navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AirSim, OpenVLA, VQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human cognition flexibly draws on a shared perceptual foundation to understand environments, attend to referenced entities, reason about spatial relationships, and act. Endowing aerial robots with an analogous functional organization remains challenging, as existing systems are often specialized for individual capabilities, dependent on offboard computation, or unable to sustain closed-loop operation on resource-constrained platforms. We present OpenFlyV2, a unified onboard vision-language-action architecture that uses a shared vision-language representation to support semantic understanding, language-grounded perception, spatial reasoning, and continuous aerial control within a single model. A compact action expert converts the shared multimodal context into short-horizon flight waypoints, while motion-aware temporal memory and action priors reduce the computational cost of closed-loop execution. We construct \dataset{}, a simulation-based dataset comprising approximately 70,000 navigation trajectories and 60,000 vision-language instruction--response pairs. OpenFlyV2 generates action chunks, each comprising 12 waypoints, entirely onboard at 10 Hz using an NVIDIA Jetson Orin NX. It transfers zero-shot from simulation to physical quadrotor flight, achieving a 48\% navigation success rate across four real-world environments without real-world aerial training data. Extensive results demonstrate that broad vision-language competence and continuous closed-loop flight can coexist within a single model on a resource-constrained aerial platform. Code will be made publicly available at https://github.com/Ideal-ljl/AeroBrain.

</details>

---

### [[20_Research/Papers/强化学习/CuBot-STT_Simultaneously_Transport_and_Tighten_for_Lattice-type_Modular_Reconfiguration_Robot|CuBot-STT: Simultaneously Transport and Tighten for Lattice-type Modular Reconfiguration Robot]]

![[assets/2610.39279_figure.png|800]]

- **arXiv**: [2610.39279](https://arxiv.org/abs/2610.39279)
- **PDF**: https://arxiv.org/pdf/2610.39279
- **详细分析**: [[20_Research/Papers/强化学习/CuBot-STT_Simultaneously_Transport_and_Tighten_for_Lattice-type_Modular_Reconfiguration_Robot|CuBot-STT: Simultaneously Transport and Tighten for Lattice-type Modular Reconfiguration Robot]]
- **作者**: Chongxi Meng, Da Zhao, Yanmin Zhou, Runjie Shen, Zhipeng Wang, Bin He
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《CuBot-STT: Simultaneously Transport and Tighten for Lattice-type Modular Reconfiguration Robot》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Lattice-type modular reconfigurable robots rearrange standardized modules across tasks. Dedicated transport robots reduce module weight and cost by eliminating module level reconfiguration actuators. But existing systems use low capacity connections or internal fastening robots that occupy space for functional components. This paper presents CuBot-STT, which integrates module transport, interface locking, and release in one external robot. Cubic modules provide structural support and $24\,\mathrm{V}$ power distribution. On each face, a gear transmission converts one external input into motion of four helical locking points, preserving internal space. The robot uses alternating foot support, a gripper for module handling, and a tightening head for interface actuation. The controller coordinates two-foot support and module locking through continuous constraint transfers. The planner decomposes relocation costs into an analytical lower bound and a residual learned through expert-guided, goal conditioned Q-learning. Contact face $A^*$ search expands relocation sequences into robot primitives satisfying connectivity, asymmetric manipulation, and foot stance constraints. Experiments demonstrate normal and tangential interface capacities of $300\,\mathrm{N}$ and $490\,\mathrm{N}$, electrical continuity across six modules, and autonomous reconfiguration of an 11-module lattice. Planning benchmarks show superior search efficiency over analytical guidance and bidirectional heuristic search, with generalization beyond training lattice sizes without fine-tuning.

</details>

---

### [[20_Research/Papers/具身智能/RAIBO-Wagon_Real-Time_Navigation_System_for_a_Legged_Robot_Towing_a_Wagon|RAIBO-Wagon: Real-Time Navigation System for a Legged Robot Towing a Wagon]]

![[assets/2610.39267_figure.png|800]]

- **arXiv**: [2610.39267](https://arxiv.org/abs/2610.39267)
- **PDF**: https://arxiv.org/pdf/2610.39267
- **详细分析**: [[20_Research/Papers/具身智能/RAIBO-Wagon_Real-Time_Navigation_System_for_a_Legged_Robot_Towing_a_Wagon|RAIBO-Wagon: Real-Time Navigation System for a Legged Robot Towing a Wagon]]
- **作者**: Insung Yang, Eunchae Kim, Jungwoo Hur, Seunghun Jeon, Donghyuk Choi, Jemin Hwangbo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 2.1（加权：具身智能 0.6，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《RAIBO-Wagon: Real-Time Navigation System for a Legged Robot Towing a Wagon》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots have demonstrated advanced capabilities across a wide range of real-world tasks, yet much of this progress concerns the robot controlling only itself. Once the robot is coupled to an external object -- particularly an underactuated one -- the dynamics of the combined assembly become more complex. Towing a wagon is a common practical scenario, where coupled dynamics make reliable navigation challenging. This difficulty is amplified in confined spaces, where collision-free navigation requires finding a narrow set of feasible paths under strict real-time constraints. To address this, we propose a navigation framework that combines Conditional Flow Matching (CFM) with Model Predictive Path Integral (MPPI) control over a learned Forward Dynamics Model (FDM). The CFM model mitigates the initialization problem of MPPI and accelerates its convergence, while MPPI with the FDM recovers feasible solutions beyond the CFM model's training distribution by iterative refinement. We integrate the framework into a full-stack navigation system for RAIBO-Wagon, a quadruped towing a custom wagon, and validate it in real-world outdoor experiments on 15 m-long courses through confined spaces, with all sensing and computation performed fully onboard. The system achieves an 85% success rate across 40 trials, towing a total load of up to 40 kg -- nearly 100% of RAIBO's body weight.

</details>

---

### [[20_Research/Papers/具身智能/CAPTURER_A_Dexterous_Aerial_Manipulator_for_Dynamic_and_Precise_Grasping_across_Diverse_Environments|CAPTURER: A Dexterous Aerial Manipulator for Dynamic and Precise Grasping across Diverse Environments]]

![[assets/2610.39119_figure.jpg|800]]

- **arXiv**: [2610.39119](https://arxiv.org/abs/2610.39119)
- **PDF**: https://arxiv.org/pdf/2610.39119
- **详细分析**: [[20_Research/Papers/具身智能/CAPTURER_A_Dexterous_Aerial_Manipulator_for_Dynamic_and_Precise_Grasping_across_Diverse_Environments|CAPTURER: A Dexterous Aerial Manipulator for Dynamic and Precise Grasping across Diverse Environments]]
- **作者**: Meng Wang, Jindou Jia, Sicheng Zhou, Zeshuai Chen, Kexin Guo, Xiang Yu, Lei Guo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.5（加权：具身智能 3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《CAPTURER: A Dexterous Aerial Manipulator for Dynamic and Precise Grasping across Diverse Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As a representative form of embodied robotic interaction, aerial grasping requires close coordination between the aerial platform and manipulator. Most existing systems perform aerial grasping with static or slowly moving targets under fixed scenarios. Dynamic and precise grasping across different conditions introduces additional challenges, including target motion, localization drift, dynamic coupling, and external disturbances. In this work, we present CAPTURER, a dexterous aerial manipulator for centimeter-level grasping across diverse environments. To achieve the challenging goal, we first develop an onboard perception system for state estimation and target detection. Drift correction and global pose transformation are introduced to improve target localization during flight. A cooperative motion planner is proposed to coordinate the mobility of the aerial platform with the dexterity of the manipulator according to the relative target state. To maintain grasping accuracy under disturbances, we design a disturbance-rejection controller to compensate for dynamic coupling, model uncertainty, and external disturbances. The capability of CAPTURER is validated through indoor and outdoor experiments with both static and moving targets. The results demonstrate that CAPTURER achieves centimeter-level grasping accuracy for a marker pen measuring only 1.5 cm in diameter at flight speeds exceeding 1.5 m/s.

</details>

---

### [[20_Research/Papers/机器人/Controlling_Continuum_Robot_Shape_in_Enclosed_Space_with_Embedded_Sensing_using_IMU_and_Actuator_Feedback|Controlling Continuum Robot Shape in Enclosed Space with Embedded Sensing using IMU and Actuator Feedback]]

![[assets/2610.39055_figure.png|800]]

- **arXiv**: [2610.39055](https://arxiv.org/abs/2610.39055)
- **PDF**: https://arxiv.org/pdf/2610.39055
- **详细分析**: [[20_Research/Papers/机器人/Controlling_Continuum_Robot_Shape_in_Enclosed_Space_with_Embedded_Sensing_using_IMU_and_Actuator_Feedback|Controlling Continuum Robot Shape in Enclosed Space with Embedded Sensing using IMU and Actuator Feedback]]
- **作者**: Jiahe Wang, Sultan Haidar Ali, Eric Weissman, Jiefeng Sun
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Controlling Continuum Robot Shape in Enclosed Space with Embedded Sensing using IMU and Actuator Feedback》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Controlling continuum robots' shape to operate in confined, enclosed environments is challenging, since it cannot rely on external observation. Existing embedded shape sensing methods, although they can provide shape reconstruction, are insufficient to enable real-time shape control due to limitations in reconstruction accuracy, computational speed, and compatibility with shape-state representation. In this work, we present an embedded shape-sensing framework that uses readily available IMU and actuator feedback to reconstruct the continuum-robot shape with a neural network, providing accurate shape feedback at $400~\mathrm{Hz}$ for physical closed-loop control. We systematically investigate four key reconstruction design choices: shape-state representation, network architecture, training objective, and sensing inputs, through more than $5{,}000$ trained models on one- and three-segment continuum robots. The selected framework achieves global shape errors of $0.9\%L$ and $1.7\%L$ (of the robot length) for the one- and three-segment systems, respectively. In closed-loop control, one-segment tip tracking achieves a $6.1\%L$ error and three-segment shape control achieves a $2.3\%L$ global shape error, whereas IMU--PCC reconstruction using the same uncompensated measurements fails. Enclosed-space experiments further demonstrate operation without external observation. These results provide a practical framework for translating readily available embedded sensing into high-rate feedback for continuum robot closed-loop control.

</details>

---

### [[20_Research/Papers/强化学习/Robotic_Data_Inoculation|Robotic Data Inoculation]]

![[assets/2610.39054_figure.png|800]]

- **arXiv**: [2610.39054](https://arxiv.org/abs/2610.39054)
- **PDF**: https://arxiv.org/pdf/2610.39054
- **详细分析**: [[20_Research/Papers/强化学习/Robotic_Data_Inoculation|Robotic Data Inoculation]]
- **作者**: Qiyang Li, Zhiyuan Zhou, Charles Xu, Sergey Levine
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，强化学习 0.4，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Robotic Data Inoculation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Modern robot learning systems feed on high-quality demonstration data, and their performance hinges on coverage. Without good coverage, small errors compound and the policy can quickly go into out-of-distribution states from which it cannot recover. Yet there is no principled way of collecting high-coverage data, and data collection often relies on heuristic instructions to human operators. Purely online reinforcement learning (RL) explores at the cost of safety and sample efficiency, while DAgger-style interventions require the policy to fail by chance before a human can correct it. In this paper, we ask instead whether we can modify how the robot behaves during data collection to collect more useful data. We propose Data Inoculation (DI), a shared-control framework in which a human provide closed-loop teleoperation commands while a residual policy perturbs these commands. The residual policy is trained online, on the growing dataset, with the same reward-maximizing objective later used for policy extraction, so its perturbations steer data collection toward the deviations a policy trained on the data would make. These perturbations expose the robot to a wider range of states, while the human's continuous corrections provide recovery demonstrations, "inoculating" the dataset against the learner's future mistakes while the human remains in control. On three challenging real-world robotic tasks, DI consistently improves or matches the success rate of policies trained with both behavioral cloning and offline RL, showing DI as an effective data collection strategy for improving downstream policy performance.

</details>

---

### [[20_Research/Papers/强化学习/Catch_It_All!_Generalizable_Dynamic_Catching_with_a_Dexterous_Hand|Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand]]

![[assets/2610.39044_figure.png|800]]

- **arXiv**: [2610.39044](https://arxiv.org/abs/2610.39044)
- **PDF**: https://arxiv.org/pdf/2610.39044
- **详细分析**: [[20_Research/Papers/强化学习/Catch_It_All!_Generalizable_Dynamic_Catching_with_a_Dexterous_Hand|Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand]]
- **作者**: Arth Shukla, Kehlani Fay, Huaze Liu, Darin Djapri, Alexiy Buynitsky, Nicklas Hansen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: EmbodiedAI, RL, Systems

#### 研究背景与动机

《Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：IsaacGym, Real-World, Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand catches, using only one egocentric camera. We learn policies which generalize to unseen objects with varying geometry, deformability, elasticity, and physical properties. Effective grasps which adapt real-time to object poses and shapes are learned through careful grasp reward design. We provide safety-aware curricula which enable safe, high-frequency action execution near hardware limits, including wrist torque limits as low as 5 Nm. We validate our system by deploying zero-shot on a Unitree G1. With only one egocentric camera, Catch It All! successfully performs underhand and overhand catches on 9 unseen objects not seen during training, including low-rebound plushes, semi-deformable toys and chip bags, and rigid-elastic objects with high rebound on contact.

</details>

---

### [[20_Research/Papers/具身智能/Open-World_Object_Motion_Anticipation_via_Meta-Learned_Semantic_Adaptation|Open-World Object Motion Anticipation via Meta-Learned Semantic Adaptation]]

![[assets/2610.38993_figure.png|800]]

- **arXiv**: [2610.38993](https://arxiv.org/abs/2610.38993)
- **PDF**: https://arxiv.org/pdf/2610.38993
- **详细分析**: [[20_Research/Papers/具身智能/Open-World_Object_Motion_Anticipation_via_Meta-Learned_Semantic_Adaptation|Open-World Object Motion Anticipation via Meta-Learned Semantic Adaptation]]
- **作者**: Mason Peterson, Gage MacLin, Camilla Tabasso, Jonathan P. How, Joshua Migdal, Tye Brady, Taskin Padir
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.6，大模型 0.2，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Open-World Object Motion Anticipation via Meta-Learned Semantic Adaptation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Open-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Anticipating the motion of nearby objects is critical for safe and efficient robot navigation. Without a proper understanding of what may move, a robot may plan overly conservative, inefficient trajectories to guarantee safety, or it may be overly risky, resulting in unacceptable collisions. While tracking and predicting the motion of known objects has seen significant progress, little research addresses how a robot should adapt online to novel objects, including anticipating how one object may move another (e.g., a person operating a forklift to move a pallet). To enable this capability, we propose a meta-learned graph neural network that leverages a semantic, geometric, and relational history of objects to accurately predict, from a few online observations, when objects will begin to move in new environments. We demonstrate that our method, which is trained only in simulation, accurately anticipates the motion of objects unseen at training time, transfers to hardware without any fine-tuning, and outperforms a vision-language model and a class-frequency baseline in both simulation and hardware experiments. Our method's accurate prediction enables collision-free traversals in a closed-loop navigation simulation, while remaining within four seconds of the fastest, collision-prone planner.

</details>

---

### [[20_Research/Papers/具身智能/Quantize_by_Doing_Task-Guided_Mixed-Precision_Quantization_of_Vision-Language-Action_Models|Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models]]

![[assets/2610.38661_figure.png|800]]

- **arXiv**: [2610.38661](https://arxiv.org/abs/2610.38661)
- **PDF**: https://arxiv.org/pdf/2610.38661
- **详细分析**: [[20_Research/Papers/具身智能/Quantize_by_Doing_Task-Guided_Mixed-Precision_Quantization_of_Vision-Language-Action_Models|Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models]]
- **作者**: Jiuyi Xu, Xiao Hu, Meida Chen, Song Wang, Yang Ye, Yangming Shi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Quantize by Doing: Task-Guided Mixed-Precision Quantization of Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：BitVLA, HBVLA, OpenVLA, QbD-VLA, SQAP-VLA, VLAQuantBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Post-training quantization (PTQ) reduces the memory footprint of vision-language-action (VLA) models, but lowering bit widths while maintaining task performance remains challenging. Existing work has used sensitivity estimates from calibration data to assign bit widths to different model components. However, using task success directly to guide mixed-precision allocation is underexplored because closed-loop evaluations are costly and the effect of quantizing one component depends on the precision of other components. To this end, we propose \textbf{QbD-VLA}, a task-guided mixed-precision quantization method that uses task success from short closed-loop evaluations to assign weight and activation bit widths while accounting for interactions between model components. Experiments covering four VLA models and all four LIBERO suites show strong task performance at average precisions of approximately 4 bits for weights and fewer than 6 bits for activations. On SIMPLER, the gain over uniform quantization is small. On a Franka Research 3 robot arm, simulation-selected allocations show no detected success-rate loss on X-VLA but fail on $π_{0.5}$. These findings support using task success to guide mixed-precision VLA quantization, while highlighting the need for real-world evaluation before deployment. Code is available at \href{https://github.com/jiuyixu25/QbD-VLA}{\texttt{github.com/jiuyixu25/QbD-VLA}}.

</details>

---

### [[20_Research/Papers/强化学习/Force-Driven_Hook_Disassembly_via_Constraint-Aware_Object-Centric_Reinforcement_Learning|Force-Driven Hook Disassembly via Constraint-Aware Object-Centric Reinforcement Learning]]

![[assets/2610.38513_figure.png|800]]

- **arXiv**: [2610.38513](https://arxiv.org/abs/2610.38513)
- **PDF**: https://arxiv.org/pdf/2610.38513
- **详细分析**: [[20_Research/Papers/强化学习/Force-Driven_Hook_Disassembly_via_Constraint-Aware_Object-Centric_Reinforcement_Learning|Force-Driven Hook Disassembly via Constraint-Aware Object-Centric Reinforcement Learning]]
- **作者**: Nadeen Elhadad, Takuya Kiyokawa, Kensuke Harada
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Force-Driven Hook Disassembly via Constraint-Aware Object-Centric Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The growing volume of end-of-life products has intensified the need for automated disassembly, yet hook-type connections remain challengin: their orientations vary, they deform under load, and their geometry is hidden, so vision alone cannot identify a feasible non-destructive disassembly direction. This work proposes a constraint-aware reinforcement learning framework that infers feasible extraction directions online from contact forces. The policy is trained in a robot-agnostic, object-centric simulation on a simplified peg-in-hole pair and deployed zero-shot on a physical robot, where it transfers to real connections with unseen, multi-stage constraint structures. Because instantaneous contact forces are noisy and locally ambiguous, the policy is coupled with a particle filter belief that provides the policy with temporally integrated directional information and reduces redundant exploratory motion. The approach is validated on four real-world tasks, from peg-in-hole pairs to the inner propeller and front cover of an end-of-life air-conditioning unit. The full method achieves success rates of 100%, 100%, 90%, and 75% with the highest path efficiency on every task, and raises the success rate on the air-conditioning cover from 45% to 75% relative to a policy trained without the belief. These results indicate that force-driven reinforcement learning can enable disassembly without product-specific models or demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/OmniQuad_a_Wheeled-Legged_Hybrid_Robot_with_Omnidirectional_Wheels|OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels]]

![[assets/2610.38502_figure.jpg|800]]

- **arXiv**: [2610.38502](https://arxiv.org/abs/2610.38502)
- **PDF**: https://arxiv.org/pdf/2610.38502
- **详细分析**: [[20_Research/Papers/具身智能/OmniQuad_a_Wheeled-Legged_Hybrid_Robot_with_Omnidirectional_Wheels|OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels]]
- **作者**: Francesco Iotti, Alok Ranjan, Franco Angelini, Manolo Garabini
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《OmniQuad: a Wheeled-Legged Hybrid Robot with Omnidirectional Wheels》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Combining wheeled and legged locomotion within a single robotic platform offers the potential to harness the advantages of both systems. The development of such hybrid systems remains an active area of research. While legged robots exhibit remarkable adaptability for traversing uneven and rugged terrains, their relatively low speed limits their practicality in indoor environments. Conversely, wheeled robots demonstrate higher efficiency on flat surfaces but often encounter difficulties when navigating obstacles such as steps. This paper introduces OmniQuad, a novel hybrid robot that integrates mecanum wheels with legged locomotion to exploit the benefits of both modalities. Mecanum wheels provide omnidirectional mobility, enhancing the robot's manoeuvrability by enabling agile movement in confined spaces and the ability to maintain a consistent orientation during task execution. In this work, we first present the design of a custom wheeled-foot featuring mecanum wheels. Subsequently, we describe the complete robot assembly, comprising these wheeled feet and EM-Act actuators. Finally, we detail the control scheme developed to govern the OmniQuad and evaluate its performance through experimental trials conducted in both indoor and outdoor environments.

</details>

---

### [[20_Research/Papers/具身智能/Skeleton-Guided_Geometry-Aware_Auto-Labeling_for_Robotic_Grasping_From_4-DoF_Learning_to_6-DoF_Execution|Skeleton-Guided Geometry-Aware Auto-Labeling for Robotic Grasping: From 4-DoF Learning to 6-DoF Execution]]

![[assets/2610.38443_figure.jpg|800]]

- **arXiv**: [2610.38443](https://arxiv.org/abs/2610.38443)
- **PDF**: https://arxiv.org/pdf/2610.38443
- **详细分析**: [[20_Research/Papers/具身智能/Skeleton-Guided_Geometry-Aware_Auto-Labeling_for_Robotic_Grasping_From_4-DoF_Learning_to_6-DoF_Execution|Skeleton-Guided Geometry-Aware Auto-Labeling for Robotic Grasping: From 4-DoF Learning to 6-DoF Execution]]
- **作者**: Ali Sabzejou, Farbod Azimmohseni, Mehdi Tale Masouleh, Ahmad Kalhor
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Skeleton-Guided Geometry-Aware Auto-Labeling for Robotic Grasping: From 4-DoF Learning to 6-DoF Execution》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Dex-Net, GraspNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic grasping relies on large manually annotated datasets, which are costly to create. We introduce a straight-skeleton-based algorithm for generating two-finger grasp keypoints and identifying regions suitable for stable, feasible grasps. Our automated pipeline produces consistent grasp annotations without human intervention. We also propose the Skeleton-based Generative Grasp Convolutional Neural Network (SkelGG-CNN), a 4-DoF architecture that learns geometric grasp features from skeleton-based guidance. To extend auto-labeling to 6-DoF grasping, we develop a generalized quasi-3D skeletonization algorithm that operates directly on point clouds. Using automatically generated 4-DoF labels, SkelGG-CNN achieves accuracies of 95.42%, 96.55%, and 97.1% on Jacquard V1, Jacquard V2, and Cornell, respectively. On the GraspNet novel split, 6-DoF auto-labeling achieves an average precision of 18.33, comparable to state-of-the-art model-based approaches. In simulation, the 6-DoF method achieves success rates of 98.4% on Dex-Net and 89.1% on EGAD!. Real-world experiments with a Delta parallel robot show success rates of 97.4% on single household objects and 95.0% in cluttered scenes, outperforming state-of-the-art methods without domain adaptation. The 4-DoF pipeline adapts across environments and produces annotations approaching human-level precision, enabling efficient training of lightweight models on small datasets. The generalized 6-DoF method provides scalable, geometry-aware annotations for cluttered 3D scenes.

</details>

---

### [[20_Research/Papers/具身智能/When_No_Worries_Went_Wrong_HRI_Lessons_for_Foundation-Model_Robots|When "No Worries" Went Wrong: HRI Lessons for Foundation-Model Robots]]

![[assets/2610.38400_figure.jpg|800]]

- **arXiv**: [2610.38400](https://arxiv.org/abs/2610.38400)
- **PDF**: https://arxiv.org/pdf/2610.38400
- **详细分析**: [[20_Research/Papers/具身智能/When_No_Worries_Went_Wrong_HRI_Lessons_for_Foundation-Model_Robots|When "No Worries" Went Wrong: HRI Lessons for Foundation-Model Robots]]
- **作者**: Eliahu Khalastchi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《When "No Worries" Went Wrong: HRI Lessons for Foundation-Model Robots》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When a person declined our robot's invitation to play, Alice turned her shoulder away and said "No worries, it's all good." Only after a brief pause did she drive off. The words and gestures were plausible but their order changed the message. In another episode, Alice informed a host that his visitor had arrived---while the visitor stood right beside him. Both came from a three-year ROS 2 HRI consortium that integrated large language and vision models as they emerged. Today's foundation models give robots broader capabilities to perceive their surroundings, reason about situations and generate behavior. Yet capability alone does not ensure that a changed situation shapes the action that reaches a person. Evidence may never be acquired, or a purpose or constraint may fail to survive planning and execution. A system may even report Success when an action no longer serves its intended purpose. Drawing on the consortium's engineering experience, we develop five design lessons about attention, knowledge, commitments, embodied timing and action authority. We then introduce TRACE, a lightweight review that changes one interaction premise, follows it to a decision or enforcement boundary, and produces an actionable architecture finding. A bounded analysis of a published LLM-generated behavior-tree system illustrates how an available clarification mechanism can go unused. The engineering lesson is to preserve accountability boundaries, not the computational pipelines that once exposed them.

</details>

---

### [[20_Research/Papers/具身智能/MATCH_Execution-Aware_Hierarchical_Reinforcement_Learning_for_Vision-and-Language_Navigation_in_Continuous_Environment|MATCH: Execution-Aware Hierarchical Reinforcement Learning for Vision-and-Language Navigation in Continuous Environment]]

![[assets/2610.38248_figure.png|800]]

- **arXiv**: [2610.38248](https://arxiv.org/abs/2610.38248)
- **PDF**: https://arxiv.org/pdf/2610.38248
- **详细分析**: [[20_Research/Papers/具身智能/MATCH_Execution-Aware_Hierarchical_Reinforcement_Learning_for_Vision-and-Language_Navigation_in_Continuous_Environment|MATCH: Execution-Aware Hierarchical Reinforcement Learning for Vision-and-Language Navigation in Continuous Environment]]
- **作者**: Shuhao Ye, Yufei Wei, Demao Wang, Shichao Zhai, Rong Xiong, Yue Wang
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，强化学习 0.6，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《MATCH: Execution-Aware Hierarchical Reinforcement Learning for Vision-and-Language Navigation in Continuous Environment》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-and-Language Navigation in Continuous Environments (VLN-CE) requires instruction-consistent planning and reliable execution under collision constraints. Yet many hierarchical approaches optimize the planner while keeping execution fixed. We introduce MATCH, a framework that jointly learns a language-conditioned planner and a goal-conditioned primitive-action executor. An execution-aware topological graph represents start-dependent execution options and integrates executor value estimates with realized outcome memory, enabling the planner to select execution requests and refine their targets through bounded continuous offsets. A transition-aware dense macro reward balances ordered progress along the reference route against execution residual, encouraging executable requests without substituting local success for instruction following. A staged curriculum culminates in synchronized on-policy updates, with the executor learning on planner-generated requests and the planner adapting its requests to the executor's current behavior. With 0.5B parameters, MATCH achieves state-of-the-art performance on the R2R-CE and RxR-CE benchmarks. Preliminary real-robot deployments further demonstrate its practical potential.

</details>

---

### [[20_Research/Papers/强化学习/SimRetract_Zero-Shot_Sim-to-Real_Robotic_Assistance_for_Retractor_Take-Over_in_Open_Surgery|SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery]]

![[assets/2610.38234_figure.png|800]]

- **arXiv**: [2610.38234](https://arxiv.org/abs/2610.38234)
- **PDF**: https://arxiv.org/pdf/2610.38234
- **详细分析**: [[20_Research/Papers/强化学习/SimRetract_Zero-Shot_Sim-to-Real_Robotic_Assistance_for_Retractor_Take-Over_in_Open_Surgery|SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery]]
- **作者**: Xucheng Wang, Zhizhou Yang, Sung Eun Kim, Romain Hardy, Michael P. Sampson, Aakash Reddy, Ankit Pal, Xiaoman Zhang, Luyang Luo, Pranav Rajpurkar
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《SimRetract: Zero-Shot Sim-to-Real Robotic Assistance for Retractor Take-Over in Open Surgery》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We demonstrate the first zero-shot sim-to-real transfer for a surgeon-robot collaboration task in open surgery: retractor take-over. A robot arm takes a retractor from the surgeon's hand and preserves retraction at handoff, using a policy trained only on simulated demonstrations, without human demonstrations or real-world fine-tuning. Imitation learning from real demonstrations is limited by collection and labeling costs, and by performance degradation when the environment changes. Our framework, SimRetract, generates simulated demonstrations designed for transfer: the policy observes masked instrument images and grasp geometry, learns to recover from off-nominal states, and acts with margin for execution drift. Deployed zero-shot, it grasps the retractor in 90% of 50 surgeon-defined phantom presentations and preserves retraction at handoff in 78%. Results on unseen retractors suggest potential for generalization to instruments with similar grasp geometry. Across ten policy configurations and 1,200 simulated and real trials, we localize the sim-to-real gap to components: in simulation, grasp rates across ablations span 80-96%, while on the real robot removing the instrument mask alone drops performance to 22% grasped and 12% held. Transfer-oriented design thus makes zero-shot sim-to-real transfer feasible for a surgical assistance task without human demonstrations. Code is available here: https://anonymous.4open.science/r/simretract-58D2.

</details>

---

### [[20_Research/Papers/强化学习/Minimum_Sufficient_Communication_for_Independent_Behaviour_Tree_Robot_Teams|Minimum Sufficient Communication for Independent Behaviour Tree Robot Teams]]

![[assets/2610.38176_figure.png|800]]

- **arXiv**: [2610.38176](https://arxiv.org/abs/2610.38176)
- **PDF**: https://arxiv.org/pdf/2610.38176
- **详细分析**: [[20_Research/Papers/强化学习/Minimum_Sufficient_Communication_for_Independent_Behaviour_Tree_Robot_Teams|Minimum Sufficient Communication for Independent Behaviour Tree Robot Teams]]
- **作者**: Sherry Jiang, Oliver Obst
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Minimum Sufficient Communication for Independent Behaviour Tree Robot Teams》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present an experimental framework for determining sufficient communication in robot teams running fixed, independent Behaviour Trees with private blackboards. Within a declared policy family, we vary message content and admission frequency and measure traffic in recipient-weighted bits per robot decision. A dense sweep identifies candidate policies for comparison with full-state communication. We retest selected candidates and the reference on fresh, paired scenarios, using one-sided simultaneous confidence bounds to assess whether success remains within five percentage points of the full-state reference. The bounds also assess whether tested cheaper policies can be ruled out as insufficient. Depending on the evidence, the framework reports an exact minimum, a positive bracket, a sufficient upper bound, or an unresolved boundary. Experiments with eight content policies across four warehouse conditions identify zero communication as the exact minimum under low contention. In the scaled condition, the no-release policy at gate $q=0.992222$ is confirmed sufficient, achieving 96.33% success at an estimated rate of 738.55 bits per robot decision, or 0.544% of full-state traffic. The positive minimum remains unresolved. These claims apply only to the declared policy family, sampled gate values and operating conditions.

</details>

---

### [[20_Research/Papers/机器人/SKiD-SLAM_Resource-Aware_Distributed_Multi-Robot_LiDAR_SLAM_for_Planetary_Missions_with_Field_Deployments_at_Analog_Sites|SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites]]

![[assets/2610.38141_figure.png|800]]

- **arXiv**: [2610.38141](https://arxiv.org/abs/2610.38141)
- **PDF**: https://arxiv.org/pdf/2610.38141
- **详细分析**: [[20_Research/Papers/机器人/SKiD-SLAM_Resource-Aware_Distributed_Multi-Robot_LiDAR_SLAM_for_Planetary_Missions_with_Field_Deployments_at_Analog_Sites|SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites]]
- **作者**: Hogyun Kim, Juwon Kim, Dongjin Cho, Jiwon Choi, Geonmo Yang, Seokhwan Jeong, Jiyun Lee, Miryeong Park, Hyungtae Lim, Younggun Cho
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.6，机器人 2.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《SKiD-SLAM: Resource-Aware Distributed Multi-Robot LiDAR SLAM for Planetary Missions with Field Deployments at Analog Sites》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Future planetary exploration missions require teams of robots to collaboratively map unknown environments under severe communication limits, constrained onboard computation, and no central infrastructure. In this field report, we present SKiD-SLAM, a distributed multi-robot LiDAR simultaneous localization and mapping (SLAM) system for such environments, and report its deployment across two mission concepts: cave exploration and scientific surface exploration. We survey the communication and computation budgets of actual planetary missions and select modules that fit these budgets for inter-robot place recognition, relative pose estimation, and distributed trajectory fusion. Before field deployment, we verify the assembled system on public datasets resembling planetary environments and in a simulator built on NASA JPL's Open Source Rover. We then validate SKiD-SLAM through field deployments in South Korea: a team of wheeled rovers explores the Majang lava-tube cave on Jeju Island, and quadruped robots carry out a crater-and-rock science scenario on a planetary analog terrain at the Korea Institute of Civil Engineering and Building Technology (KICT) in Yeoncheon. Across both deployments, SKiD-SLAM reliably performed distributed multi-robot LiDAR SLAM within a 250 kbps inter-robot communication budget, demonstrating its feasibility under challenging field conditions. Supplementary materials, including code and field data, are available at https://sparolab.github.io/research/skid_slam/.

</details>

---

### [[20_Research/Papers/具身智能/Self-Labeled_Preference_Transfer_for_Steerable_Robot_Manipulation|Self-Labeled Preference Transfer for Steerable Robot Manipulation]]

![[assets/2610.38000_figure.png|800]]

- **arXiv**: [2610.38000](https://arxiv.org/abs/2610.38000)
- **PDF**: https://arxiv.org/pdf/2610.38000
- **详细分析**: [[20_Research/Papers/具身智能/Self-Labeled_Preference_Transfer_for_Steerable_Robot_Manipulation|Self-Labeled Preference Transfer for Steerable Robot Manipulation]]
- **作者**: Kaiwen Hong, Shaoting Peng, Xiangyu Zeng, Pengcheng Wang, Boyuan Tian, Haonan Chen, Yifan Zhu, Yixiao Wang, Katherine Driggs-Campbell
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Self-Labeled Preference Transfer for Steerable Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：FineVLA, SG-VLA, TwinBrainVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) policies can learn to follow execution preferences, such as where to grasp an object or how to move around an obstacle, from demonstrations annotated with preference labels. Providing these annotations for every new task, however, is costly. We study whether learned preference control can transfer to new tasks whose demonstrations contain the desired behaviors but lack preference annotations. We find that a policy trained with preference annotations can follow preferences on a new task before adaptation but achieves limited task success. Fine-tuning on target demonstrations without these annotations improves task success while weakening preference control. Motivated by this finding, we introduce Self-Labeled Preference Transfer (SPT). SPT jointly trains a shared vision-language backbone for preference-conditioned action prediction and preference recognition on annotated source demonstrations. It then freezes the recognizer to preserve its cross-task preference recognition capability and uses it to self-label target demonstrations for policy fine-tuning. Across five types of execution preferences in simulation, the recognizer achieves 96.4% accuracy, and SPT reaches 84.8% preference following and 89.2% task success, compared with 59.4% and 88.0% for naive finetuning. We further extend to multiple preferences, achieving 93.8% preference following compared with 42.5% of baselines. In real-world experiments, SPT increases preference following from 52.5% to 92.5% relative to naive finetuning across two task transfers. These results show that SPT can support preference adaptation across tasks and objects while maintaining success, without additional manual preference annotations.

</details>

---

### [[20_Research/Papers/机器人/An_Empirical_Study_of_Wrist-Target_Construction_and_Joint-Angle_Limits_in_Humanoid_Arm_Retargeting|An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting]]

![[assets/2610.37801_figure.png|800]]

- **arXiv**: [2610.37801](https://arxiv.org/abs/2610.37801)
- **PDF**: https://arxiv.org/pdf/2610.37801
- **详细分析**: [[20_Research/Papers/机器人/An_Empirical_Study_of_Wrist-Target_Construction_and_Joint-Angle_Limits_in_Humanoid_Arm_Retargeting|An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting]]
- **作者**: MinJun Chang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《An Empirical Study of Wrist-Target Construction and Joint-Angle Limits in Humanoid Arm Retargeting》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion retargeting maps a demonstrated human movement onto a robot to compute its joint motion. This study examines how the construction of the desired wrist position affects whether computed arm joint angles reach their permitted limits on a Unitree H1-2. A reconstructed target is formed from demonstrated arm directions and robot segment lengths, so its shoulder-to-wrist distance depends on the demonstrated angle between the segments even when no posture-matching preference is applied. A reach-normalized target retains that direction while rescaling the distance, using the same processed demonstrations and the same joint-angle method. Across a forward-reach sweep the reconstructed target places a joint angle at a bound in 10 of 20 repetitions and the reach-normalized target in none. Across 25 recordings from one participant the corresponding counts are 8 and 6 on the reaching arm and 14 and 5 on the supporting arm, and a second participant repeats the bricklaying and lifting comparison. In hardware replay a joint is commanded to a bound in 12 of 16 direction-matching arm-records and in none of the 16 normalized records, and within the eligible records both tracking error and executed torque at those frames exceed their values elsewhere in the same run. Cross-body reach and arm-to-arm clearance identify limits of radial adjustment. The findings support treating target construction and posture matching as separate retargeting decisions, and evaluating both alongside the wrist positions and clearance that manipulation requires.

</details>

---

### [[20_Research/Papers/机器人/DexSuite_An_All-in-One_Framework_for_Dexterous_Manipulation_Across_Arms,_Hands,_and_Tasks|DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks]]

![[assets/2610.37799_figure.png|800]]

- **arXiv**: [2610.37799](https://arxiv.org/abs/2610.37799)
- **PDF**: https://arxiv.org/pdf/2610.37799
- **详细分析**: [[20_Research/Papers/机器人/DexSuite_An_All-in-One_Framework_for_Dexterous_Manipulation_Across_Arms,_Hands,_and_Tasks|DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks]]
- **作者**: Anas Houssaini, Hugo He, Junming Shi, Amin Abyaneh, Ricardo Chahine, Shuo Wen, Mohamad H. Danesh, Charles-Étienne Fréchette, Mariana Sosa Guzman, Mathias Desrochers, Rayan Houssaini, Adam Landa...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《DexSuite: An All-in-One Framework for Dexterous Manipulation Across Arms, Hands, and Tasks》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoppeliaSim, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-level dexterity remains a central open problem in robotics, yet few simulation frameworks cover the full workflow of dexterous manipulation, from setting up a robot to collecting dexterous demonstrations and evaluating policies. We present DexSuite, an all-in-one simulation framework for dexterous manipulation built on the Genesis simulator. DexSuite provides 30 tasks and assembles its 10 arms and 12 end-effectors, from parallel-jaw grippers to dexterous hands, into more than 100 single-arm robots and thousands of bimanual pairs. It also ships a standardized environment API, integrated teleoperation, and simulated tactile sensing. Moreover, we define a benchmark of 16 task-embodiment pairs spanning diverse contact complexities and horizons, and release a dataset of 4,700 successful episodes in simulation from human teleoperation, scripted experts, and learned policies. We release DexSuite as open source and hope others will build on it. Videos and datasets are available at https://dexsuiteorg.github.io

</details>

---
