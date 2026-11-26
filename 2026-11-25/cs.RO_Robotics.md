# cs.RO | Robotics | 2026-11-25

#arxiv #ComputerScience

**论文数**: 35

### [[20_Research/Papers/强化学习/PyRUA-Dex_Learning_Programmatic_Policies_for_Dexterous_Bimanual_Manipulation_with_Coding_Agents|PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents]]

![[assets/2611.33144_figure.png|800]]

- **arXiv**: [2611.33144](https://arxiv.org/abs/2611.33144)
- **PDF**: https://arxiv.org/pdf/2611.33144
- **详细分析**: [[20_Research/Papers/强化学习/PyRUA-Dex_Learning_Programmatic_Policies_for_Dexterous_Bimanual_Manipulation_with_Coding_Agents|PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents]]
- **作者**: Feixiang Ruan, Guodong Lv, Kewei Zhang, Wenbo Huang, Yintianrun Zhang, Qiang Wang, Ruiyang Si, Shunyu Yang, Shulong Jiang, Weicheng Duan, Rui Ni, Jianxin Bi...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.5，大模型 0.5，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《PyRUA-Dex: Learning Programmatic Policies for Dexterous Bimanual Manipulation with Coding Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning for dexterous manipulation is limited by the scarcity of high-quality demonstrations: retargeting from human video is imprecise, teleoperation gives no force feedback to the operator, and exoskeleton-based collection is hard to scale up. We present PyRUA-Dex, a framework that enables coding agents to develop dexterous manipulation through programmatic policy, without the need of demonstrations. The programmatic policy is developed in two stages: during exploration, multiple agents explore in parallel for task skills and ways to compose them, and a distilling agent condenses the successful attempts into a task library and one program. During refinement, this program is improved through randomized layouts for enhanced robustness and execution efficiency. In simulated environments, PyRUA-Dex achieves SOTA on Bench2Dex with a score of 72.9 and reaches 81.0% success on DexJoCo under full randomization, ahead of every trained policy on both benchmarks. In real world experiments on a bimanual platform with two 22-DoF hands, PyRUA-Dex learns to play piano, write calligraphy, and other tasks efficiently: learning a new piece from sheet music takes as little as 30 minutes. These results suggest that PyRUA-Dex is an effective framework for developing dexterous manipulation policies with coding agents in the absence of high quality dexterous manipulation demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiSafety_Benchmarking_Risk_Understanding_and_Response_in_Embodied_AI|EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI]]

![[assets/2611.33054_figure.png|800]]

- **arXiv**: [2611.33054](https://arxiv.org/abs/2611.33054)
- **PDF**: https://arxiv.org/pdf/2611.33054
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiSafety_Benchmarking_Risk_Understanding_and_Response_in_Embodied_AI|EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI]]
- **作者**: Erfei Cui, Shengjia Zhao, Yan Qin, Kaixuan Wang, Junming Chen, Ping Luo, Tianxing Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 2.4，机器人 0.3）
- **关联关键词**: EmbodiedAI

#### 研究背景与动机

《EmbodiSafety: Benchmarking Risk Understanding and Response in Embodied AI》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, HomeSafeBench, IS-Bench, SafeAgentBench, SafeMindBench, SafeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Progress in embodied foundation models is largely measured by task success, while the physical safety of their decisions remains underexamined. Safety evaluations centered on rule following and binary judgments do not adequately assess whether embodied models understand environmental hazards and make safe decisions. We introduce EmbodiSafety, comprising 1,092 snapshot tasks and 540 trajectory tasks across 844 visual scenarios to assess safety over short and long horizons. Six response modes cover direct execution, refusal, clarification, constrained execution, autonomous recovery, and human escalation. Distinguishing recovery from human intervention makes the boundary of safe autonomy an explicit evaluation target. Our protocol assesses mode correctness, risk identification, and actionable handling, with complete decision accuracy requiring all applicable checks to pass. Claude-Opus-5.5 achieves the highest complete decision accuracy among reference models, reaching 56.1% on snapshots and 61.5% on trajectories. We further develop a data construction pipeline and curate 40k examples for safety alignment. Supervised training on this corpus raises the complete decision accuracy of Qwen3.5-2B and Qwen3.5-4B.

</details>

---

### [[20_Research/Papers/强化学习/DynaMimic_A_Physics-Informed_World_Model_for_Humanoid_Motion_Tracking|DynaMimic: A Physics-Informed World Model for Humanoid Motion Tracking]]

![[assets/2611.32944_figure.png|800]]

- **arXiv**: [2611.32944](https://arxiv.org/abs/2611.32944)
- **PDF**: https://arxiv.org/pdf/2611.32944
- **详细分析**: [[20_Research/Papers/强化学习/DynaMimic_A_Physics-Informed_World_Model_for_Humanoid_Motion_Tracking|DynaMimic: A Physics-Informed World Model for Humanoid Motion Tracking]]
- **作者**: Chaoyue Xing, Linyi Huang, Yiting He, Yixuan Yin, Siqi Hou, Yi Zhang, Liyuan Pan, Miaomiao Liu, Daqi Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 强化学习
- **相关性评分**: 3.6（加权：具身智能 1.5，强化学习 0.2，世界模型 0.8，机器人 1.1）
- **关联关键词**: RL, WorldModel, Systems

#### 研究背景与动机

《DynaMimic: A Physics-Informed World Model for Humanoid Motion Tracking》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：NeuralSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Whole-body motion tracking enables humanoid robots to reproduce diverse skills from human demonstrations. Existing model-free reinforcement learning methods either distill motion specialists into a single policy at the cost of performance or train a generalist policy directly using cluster-scale computation. SuperMimic reduces this computational cost through a differentiable world model that implicitly learns the physics shared across motions by predicting the next state from the current state and action. However, this implicit formulation may not fully capture the underlying physical processes. Errors around changes of support can accumulate over imagined rollouts used to train the tracking policy. To address this challenge, we introduce DynaMimic, a differentiable world model that explicitly incorporates shared physics into state prediction. Specifically, its network predicts a contact wrench at each candidate support link and a residual generalized force. DynaMimic then uses these predictions to compute the next state through closed-form Lagrangian forward dynamics. Across 60 full LAFAN1 motions, DynaMimic reduces mean per-joint position error (MPJPE) by 18.6% relative to SuperMimic. For terrain tracking, we give both methods the same local height maps. Relative to terrain-conditioned SuperMimic, DynaMimic reduces MPJPE by 14.9% on A3 Parkour (66.15 to 56.28~mm) and by 10.8% on GRAIL terrain clips (141.88 to 126.57~mm). On a real A3 humanoid, the learned policies can perform diverse skills, such as floor recovery, cartwheel and a box vault.

</details>

---

### [[20_Research/Papers/具身智能/Self-Sensing_Compliant_Anthropomorphic_Hand_for_Speed-Dictated_Shared_Force_Control_in_Teleoperation|Self-Sensing Compliant Anthropomorphic Hand for Speed-Dictated Shared Force Control in Teleoperation]]

![[assets/2611.32937_figure.png|800]]

- **arXiv**: [2611.32937](https://arxiv.org/abs/2611.32937)
- **PDF**: https://arxiv.org/pdf/2611.32937
- **详细分析**: [[20_Research/Papers/具身智能/Self-Sensing_Compliant_Anthropomorphic_Hand_for_Speed-Dictated_Shared_Force_Control_in_Teleoperation|Self-Sensing Compliant Anthropomorphic Hand for Speed-Dictated Shared Force Control in Teleoperation]]
- **作者**: Huijiang Wang, Yu Zhang, Rui Chen, Tristan Bonato, Jaemin Eom, Kai Junge, Cheng Pan, Benhui Dai, Yue Xie, Josie Hughes
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Self-Sensing Compliant Anthropomorphic Hand for Speed-Dictated Shared Force Control in Teleoperation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In vision-based teleoperation of robotic hands, the operator receives no haptic feedback and therefore struggles to regulate the grasp force, while adding tactile sensors to the fingers increases wiring, cost and integration complexity. Compliant hands offer an alternative, as their mechanical compliance, usually treated only as a passive property for safe and adaptive grasping, can also serve as a source of information. Here, we show that the elastic transmission of a compliant, tendon-driven anthropomorphic hand can itself act as the sensor for shared-control telemanipulation. Series springs in the tendon routing are read by potentiometers in a forearm-mounted motor box, from which the hand estimates its joint states and finger forces without any external sensors. Building on this self-sensing, we develop a contact-aware shared-control framework for VR-based teleoperation. The robot hand is controlled through a mapping from the operator's hand kinematics until a contact is detected proprioceptively. Control then switches to a finger-level force controller whose set point is determined by the operator's grasping speed, and control authority can be allocated to individual fingers. Experiments validate the system's force estimation and increased grasp success rate compared with direct teleoperation for fragile and heavy objects. These results show that compliance can serve not only for passive adaptation but also as an intrinsic sensing resource for physical human-robot collaboration.

</details>

---

### [[20_Research/Papers/具身智能/Supply_Geometry,_Learn_Execution_Screw_Attention_for_Zero-Shot_Policy_Transfer_in_Robot_Manipulation|Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation]]

![[assets/2611.32797_first_page.png|800]]

- **arXiv**: [2611.32797](https://arxiv.org/abs/2611.32797)
- **PDF**: https://arxiv.org/pdf/2611.32797
- **详细分析**: [[20_Research/Papers/具身智能/Supply_Geometry,_Learn_Execution_Screw_Attention_for_Zero-Shot_Policy_Transfer_in_Robot_Manipulation|Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation]]
- **作者**: Aly Magassouba
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Supply Geometry, Learn Execution: Screw Attention for Zero-Shot Policy Transfer in Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present the Screw Attention Policy, a geometry-centric manipulation framework that supplies task geometry explicitly and learns only execution. The policy operates on object poses, relative SE(3) transforms, and joint screw axes provided by perception and robot models. The policy requires only 30K learned parameters. Trained entirely in simulation on a single robot arm, the policy generalises to new scene layouts, transfers zero-shot across robot embodiments, and deploys directly on a real robot, without adaptation or fine-tuning. It achieves 96% success on LIBERO, 85.8% under layout changes, 80.2% across five unseen robot arms, and 21 of 24 trials on a real robot. These results suggest that much of what manipulation policies learn at scale is geometric structure that can instead be supplied.

</details>

---

### [[20_Research/Papers/机器人/Risk-Informed_Path_Planning_Collision_and_Grounding_Avoidance_Application_for_Autonomous_Surface_Vessels|Risk-Informed Path Planning: Collision and Grounding Avoidance Application for Autonomous Surface Vessels]]

![[assets/2611.32760_figure.png|800]]

- **arXiv**: [2611.32760](https://arxiv.org/abs/2611.32760)
- **PDF**: https://arxiv.org/pdf/2611.32760
- **详细分析**: [[20_Research/Papers/机器人/Risk-Informed_Path_Planning_Collision_and_Grounding_Avoidance_Application_for_Autonomous_Surface_Vessels|Risk-Informed Path Planning: Collision and Grounding Avoidance Application for Autonomous Surface Vessels]]
- **作者**: Emir Cem Gezer, Ozan Kaya, Ingrid B. Utne, Roger Skjetne
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《Risk-Informed Path Planning: Collision and Grounding Avoidance Application for Autonomous Surface Vessels》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Maritime Autonomous Surface Ships (MASS) must demonstrate safety before and during operations, necessitating online risk assessment to guide decision-making at sea. This paper presents a risk-informed Rapidly Exploring Random Tree Star (RRT*) path planner that integrates a Bayesian Belief Network (BBN) as an online risk model. The BBN evaluates the probability and severity distribution of hazardous events, which are aggregated into a bounded scalar risk index. During the search, this risk index is evaluated at sample points along candidate edges. The planner optimizes a composite cost function comprising path distance, heading change penalties, and accumulated risk, subject to a hard constraint enforcing a risk acceptance limit. Each search tree vertex stores the BBN posterior at its state, enabling the tree to function as an explainable risk map for individual hazards. We define design requirements for the BBN to serve as the risk model in this context and introduce a runtime model that translates replanning deadlines into strict limits on single risk calculation times. The planner is demonstrated in a simulated harbor entry scenario involving collision and grounding hazards. Measured run times validate that the planner operates within the computational bounds predicted by the runtime model for a single replanning cycle.

</details>

---

### [[20_Research/Papers/具身智能/AG-WAM_Attention-Guided_World_Action_Model_for_Accurate_and_Efficient_Robot_Manipulation|AG-WAM: Attention-Guided World Action Model for Accurate and Efficient Robot Manipulation]]

![[assets/2611.32722_figure.png|800]]

- **arXiv**: [2611.32722](https://arxiv.org/abs/2611.32722)
- **PDF**: https://arxiv.org/pdf/2611.32722
- **详细分析**: [[20_Research/Papers/具身智能/AG-WAM_Attention-Guided_World_Action_Model_for_Accurate_and_Efficient_Robot_Manipulation|AG-WAM: Attention-Guided World Action Model for Accurate and Efficient Robot Manipulation]]
- **作者**: Hongcheng Zhang, Lei Sun, Songxuan Liu, Tengteng Pan, Yuqiang Zhai, Xianglong Xu, Jianya Guo, Xiao Song
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《AG-WAM: Attention-Guided World Action Model for Accurate and Efficient Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recently developed World Action Models (WAMs) jointly predict future observations and robot actions, providing predictive context for control. However, existing WAMs typically learn implicit attention allocation with limited explicit action-relevant attention guidance, leading to limited performance. To unleash strong capabilities of WAMs, we introduce explicit attention guidance as a unifying principle and propose our Attention-Guided WAM (AG-WAM), an end-to-end framework with three plug-and-play attention guidance modules that directly reformulate internal attention paradigm in WAMs: the Content-Adaptive Predictive Attention module, the Guidance-Point Visual Attention module, and the State-Conditioned Text Attention module. Without any external plugin module adopted, our end-to-end framework with the unifying principle of explicit attention guidance boosts the accuracy and efficiency of WAMs. Without using any private embodied training data, our AG-WAM establishes new state-of-the-art performance on multiple public robotic manipulation benchmarks including LIBERO-X, LIBERO-Plus, and RoboTwin-2.0, significantly outperforming other methods, even those using massive private embodied training data by a notable margin, meanwhile notably improving training and inference efficiency.

</details>

---

### [[20_Research/Papers/机器人/DeCoNav-Act_Benchmarking_Collective_Physical_Capability_in_Multi-Robot_Mobile_Manipulation|DeCoNav-Act: Benchmarking Collective Physical Capability in Multi-Robot Mobile Manipulation]]

![[assets/2611.32683_figure.png|800]]

- **arXiv**: [2611.32683](https://arxiv.org/abs/2611.32683)
- **PDF**: https://arxiv.org/pdf/2611.32683
- **详细分析**: [[20_Research/Papers/机器人/DeCoNav-Act_Benchmarking_Collective_Physical_Capability_in_Multi-Robot_Mobile_Manipulation|DeCoNav-Act: Benchmarking Collective Physical Capability in Multi-Robot Mobile Manipulation]]
- **作者**: Yunzi Wu, Sunyao Zhou, Xiaotao Zhang, Yucheng Deng, Yuehao Huang, Lin Qian, Xuanrui Cui, Xinhai Li, Chenjia Bai, Hongqing Chu, Xuelong Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《DeCoNav-Act: Benchmarking Collective Physical Capability in Multi-Robot Mobile Manipulation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoCoBench, EmbodiedBench, MAGMA-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot teams can split workloads or combine complementary bodies, but only if each robot leaves the shared world in a state its teammate can use. Existing multi-robot benchmarks emphasize task allocation and skill sequencing, rarely testing whether the resulting physical states are usable. To evaluate collective physical capability, we introduce DeCoNav-Act, a benchmark for language-guided multi-robot mobile manipulation in a shared physics simulation. Its 350 homogeneous and 150 heterogeneous tasks, each verified by joint reference execution, span two coordination mechanisms: parallel workloads in shared space and physical dependencies in which one robot establishes a condition for a teammate to use. Beyond team success, DeCoNav-Act measures path efficiency and handoff coverage and success, and adds a diagnostic from verified pre-handoff states. Evaluating sensor-grounded adaptations of ASPIRE and RAX and our agent CoMoMa, we find that with GPT-5.6-luna no method completes a task, at most 8.8% of dependencies are reached, and even from pre-handoff states no handoff is completed; with GPT-6.1-sol, CoMoMa establishes the condition in 26.5% of trials, but only 4.1% succeed.

</details>

---

### [[20_Research/Papers/具身智能/DiffGR00T_Execution-Aware_Differentiable_Training_for_Humanoid_Whole-Body_Vision-Language-Action_Models|DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models]]

![[assets/2611.32665_figure.png|800]]

- **arXiv**: [2611.32665](https://arxiv.org/abs/2611.32665)
- **PDF**: https://arxiv.org/pdf/2611.32665
- **详细分析**: [[20_Research/Papers/具身智能/DiffGR00T_Execution-Aware_Differentiable_Training_for_Humanoid_Whole-Body_Vision-Language-Action_Models|DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models]]
- **作者**: Sichen Wu, Qian Sun, Mengfan Liu, Weikai Qin, Bike Zhu, Hesheng Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型, 大模型
- **相关性评分**: 4.4（加权：具身智能 3，大模型 0.1，世界模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《DiffGR00T: Execution-Aware Differentiable Training for Humanoid Whole-Body Vision-Language-Action Models》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：HAF-VLA, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have achieved strong results in arm-centric manipulation, yet humanoid whole-body control (WBC) requires dynamic balance and tightly coupled full-body coordination. Existing hierarchical humanoid VLAs typically decouple motion generation from physical execution, leaving tracking and balance errors unable to directly optimize the VLA generator. We propose DiffGR00T, an end-to-end differentiable training framework that couples GR00T N1.7 with SONIC, a pretrained whole-body behavior foundation model. To enable execution-aware differentiable training, we replace the non-differentiable simulator with a learned, action-conditioned world model, allowing multi-step body-execution losses to backpropagate through the frozen whole-body controller and the flow-matching sampler directly into the VLA action head. On four HumanoidArena simulation tasks, DiffGR00T improves average task success by 12.5 percentage points over the supervised base VLA (59.2% to 71.7%), demonstrating that execution-aware gradients effectively align high-level motion generation with closed-loop whole-body dynamics.

</details>

---

### [[20_Research/Papers/具身智能/An_XR-Based_System_for_Enhanced_Spatial_Awareness_in_Mobile_Robot_Teleoperation|An XR-Based System for Enhanced Spatial Awareness in Mobile Robot Teleoperation]]

![[assets/2611.32584_figure.png|800]]

- **arXiv**: [2611.32584](https://arxiv.org/abs/2611.32584)
- **PDF**: https://arxiv.org/pdf/2611.32584
- **详细分析**: [[20_Research/Papers/具身智能/An_XR-Based_System_for_Enhanced_Spatial_Awareness_in_Mobile_Robot_Teleoperation|An XR-Based System for Enhanced Spatial Awareness in Mobile Robot Teleoperation]]
- **作者**: Subhransu Sourav Priyadarshan, Valentina Pericu, Federico Rollo, Gianni Viardo Vercelli, Navvab Kashiri
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《An XR-Based System for Enhanced Spatial Awareness in Mobile Robot Teleoperation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Teleoperation of mobile robots represents a critical capability for operations in hazardous environments, yet maintaining adequate situational awareness remains challenging without effective visualization and control interfaces. This work presents a multi-modal extended reality (XR) system for robot teleoperation and scene exploration that integrates immersive visual and haptic feedback modalities. To address motion sickness commonly induced by 360-degree camera feeds in head-mounted displays (HMDs), the system employs a fixed dual-camera configuration: a forward-facing camera for primary navigation and a rear-facing camera for enhanced situational awareness without operator discomfort. For navigation in confined or low-visibility conditions, a 16-channel Velodyne LiDAR generates real-time 2D occupancy grid maps, which are converted into vibrational haptic feedback on handheld controllers to provide intuitive, non-visual obstacle detection. User evaluation with 20 participants demonstrates that this haptic modality significantly reduces the cognitive load associated with obstacle avoidance during teleoperation.

</details>

---

### [[20_Research/Papers/具身智能/Design,_Control,_and_Teleoperation_of_a_Dexterous_Robotic_Hand_with_Soft-Rigid_Hybrid_Fingers|Design, Control, and Teleoperation of a Dexterous Robotic Hand with Soft-Rigid Hybrid Fingers]]

![[assets/2611.32582_figure.png|800]]

- **arXiv**: [2611.32582](https://arxiv.org/abs/2611.32582)
- **PDF**: https://arxiv.org/pdf/2611.32582
- **详细分析**: [[20_Research/Papers/具身智能/Design,_Control,_and_Teleoperation_of_a_Dexterous_Robotic_Hand_with_Soft-Rigid_Hybrid_Fingers|Design, Control, and Teleoperation of a Dexterous Robotic Hand with Soft-Rigid Hybrid Fingers]]
- **作者**: Chao Liu, Wil J. Norton, Brandon Romero, Daniela Rus
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Design, Control, and Teleoperation of a Dexterous Robotic Hand with Soft-Rigid Hybrid Fingers》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Adding compliance to robot hands results in higher grasp quality and robust contact with the environment. Soft hands are inherently compliant, but are typically more complex to control and model than rigid equivalents. We extend prior work on soft-rigid hybrid robot fingers into a five-fingered dexterous gripper --- an integrated tendon-driven hand that is highly compliant and controllable. Structural compliance combined with a rigid skeleton, when realized in a five-fingered hand, allow us to use linear control to achieve soft-grasping generality. We evaluate the use of this hand in a variety of teleoperated manipulation tasks, demonstrating the effectiveness of the overall mechanical design and control strategy. Our contributions include: (1) Mechanical design of the a five-fingered Soft-Rigid Hybrid Hand, composed of 12 active degrees of freedom, demonstrating a high degree on generalization enabled by the soft-rigid architecture, with our gripper, able to complete 28 of the 33 (84.8\%) grasp postures in the human range. (2) Precise, high bandwidth (up to 1432deg/s extension speed, compared with 700deg/s for the equivalent human joint). (3) Position and task space controllers for the soft-rigid hybrid finger and whole hand. (4) A teleoperation framework for control of this hand, as well as demonstrations of its efficacy in a variety of grasping and manipulation tasks Further tests illustrate the hand's advantages in completing non-rigid manipulation tasks, such as picking up thin deformable objects (such as a dollar bill or folding cloth) as well as in interfacing with soft or delicate targets.

</details>

---

### [[20_Research/Papers/具身智能/Follow-Bench_2.0_An_End-to-End_3D_Benchmark_for_Socially-Aware_Robot_Person_Following|Follow-Bench 2.0: An End-to-End 3D Benchmark for Socially-Aware Robot Person Following]]

![[assets/2611.32579_figure.png|800]]

- **arXiv**: [2611.32579](https://arxiv.org/abs/2611.32579)
- **PDF**: https://arxiv.org/pdf/2611.32579
- **详细分析**: [[20_Research/Papers/具身智能/Follow-Bench_2.0_An_End-to-End_3D_Benchmark_for_Socially-Aware_Robot_Person_Following|Follow-Bench 2.0: An End-to-End 3D Benchmark for Socially-Aware Robot Person Following]]
- **作者**: Hanjing Ye, Tianle Zeng, Jianwei Peng, Yanci Wen, Yuchen Zhou, Yonggen Ling, Hong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Follow-Bench 2.0: An End-to-End 3D Benchmark for Socially-Aware Robot Person Following》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EVT-Bench, Follow-Bench, TPT-Bench, TrackVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Socially-aware robot person following (RPF) requires a mobile robot to follow a designated person in dynamic human environments while maintaining target identity, avoiding obstacles and pedestrians, and preserving socially comfortable formations. Existing benchmarks only partially evaluate this coupled problem: embodied visual tracking benchmarks emphasize target visibility with limited social interaction, person re-identification benchmarks study perception without closed-loop control, and motion-planning benchmarks often assume ground-truth target and pedestrian states. We introduce Follow-Bench 2.0, an end-to-end 3D benchmark for evaluating socially-aware RPF under coupled perception--planning challenges. Built in Unreal Engine, Follow-Bench 2.0 provides difficulty-leveled scenarios with diverse pedestrian flows, lighting and weather conditions, cluttered layouts, bottlenecks, queueing behaviors, distractors, and temporary target occlusions. The benchmark supports modular perception--planning pipelines, end-to-end visual policies, and foundation-model-based active trackers under a unified closed-loop protocol. It further evaluates both back- and side-following configurations and reports safety--comfort metrics covering task success, target visibility, target recovery, social-space intrusion, following formation, and motion smoothness. Experiments show that RPF-oriented modular pipelines substantially outperform current end-to-end visual policies on close and socially comfortable following, but also reveal that socially-aware RPF remains far from solved in interaction-heavy environments and especially in side-following. Follow-Bench 2.0 therefore provides a diagnostic platform for studying how perception errors, occlusions, crowd interactions, and following configurations jointly affect robot person following.

</details>

---

### [[20_Research/Papers/机器人/Self-supervised_quality_evaluation_of_grid_maps_without_ground_truth|Self-supervised quality evaluation of grid maps without ground truth]]

![[assets/2611.32550_figure.png|800]]

- **arXiv**: [2611.32550](https://arxiv.org/abs/2611.32550)
- **PDF**: https://arxiv.org/pdf/2611.32550
- **详细分析**: [[20_Research/Papers/机器人/Self-supervised_quality_evaluation_of_grid_maps_without_ground_truth|Self-supervised quality evaluation of grid maps without ground truth]]
- **作者**: Unal Artan, Manuel Castellano-Quero, Johannes A. Stork, Martin Magnusson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Self-supervised quality evaluation of grid maps without ground truth》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Maps are widely used in the robotics community for localization and path planning and the ability to identify incorrect or inaccurate regions of a map is an area of active research interest. For large environments, manual edits of the map can be very time consuming and a tool which can assist a map editor is needed. With this paper, we contribute to robot introspection through self-assessment of map quality, using only a given map as input to be independent of the underlying mapping algorithm. Current methods for map quality assessment rely on ground-truth or labelled information for training classifiers, both of which can be difficult to obtain. In this paper, we propose a self-supervised learning approach to map quality assessment of 2D occupancy grid maps which identifies regions of a map that require further investigation. We leverage an autoencoder for patches extracted from the map to capture the dominant structure of the map. By evaluating the reconstruction loss of a patch reconstructed with the learned model, we can evaluate whether it contains an unusual structure, which indicates the need of further investigation. We evaluate our method on the outcome of state-of-the-art grid mapping methods using benchmark datasets as well as maps from warehouse environments, highlighting the application to more complex environments. We show that the method identifies regions with sparse data, clutter, and misregistrations.

</details>

---

### [[20_Research/Papers/具身智能/EmbodiedStudio_A_Task-Driven_Simulation_Generation_Platform_for_Embodied_Learning_and_Evaluation|EmbodiedStudio: A Task-Driven Simulation Generation Platform for Embodied Learning and Evaluation]]

![[assets/2611.32534_figure.png|800]]

- **arXiv**: [2611.32534](https://arxiv.org/abs/2611.32534)
- **PDF**: https://arxiv.org/pdf/2611.32534
- **详细分析**: [[20_Research/Papers/具身智能/EmbodiedStudio_A_Task-Driven_Simulation_Generation_Platform_for_Embodied_Learning_and_Evaluation|EmbodiedStudio: A Task-Driven Simulation Generation Platform for Embodied Learning and Evaluation]]
- **作者**: Yang Zhao, Xubo Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《EmbodiedStudio: A Task-Driven Simulation Generation Platform for Embodied Learning and Evaluation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FactorSim, GenSim, RLBench, SceneEval。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training and evaluating robots across diverse tasks requires a supply of simulation environments suited to those tasks. While recent scene and task generators offer a promising way to expand this supply, delivering a usable task environment still faces two practical gaps: generated scenes that look plausible in appearance often fail to support the intended task interactions or remain physically stable in simulation, and generated scoring programs frequently attempt task conditions without implementing them faithfully. We present EmbodiedStudio, a task-driven simulation generation platform that bridges these gaps by jointly authoring scene, task, robot-behavior, and rubric programs under closed-loop simulation feedback and independent review. Crucially, as the coding agent iteratively debugs scenes, behaviors, and stateful rubrics in simulation, this closed-loop process natively yields both forward construction experience for learning to build environments and physical execution experience for policy learning, all bound to frozen environment revisions for repeatable evaluation. Across scene generation, rubric evaluation, ablations, and learning studies, EmbodiedStudio substantially improves task readiness and rubric faithfulness while improving physical stability and retaining actionable supervision signals for layout authoring and policy adaptation.

</details>

---

### [[20_Research/Papers/机器人/AirLeg_A_Robust_and_Accurate_Self-Supervised_Visual-Inertial-Leg_SLAM_System|AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System]]

![[assets/2611.32523_figure.png|800]]

- **arXiv**: [2611.32523](https://arxiv.org/abs/2611.32523)
- **PDF**: https://arxiv.org/pdf/2611.32523
- **详细分析**: [[20_Research/Papers/机器人/AirLeg_A_Robust_and_Accurate_Self-Supervised_Visual-Inertial-Leg_SLAM_System|AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System]]
- **作者**: Kuan Xu, Tianxin Hu, Ruofei Bai, Ruimeng Liu, Yuefan Hao, Zeyu Jiang, Zitong Zhan, Shenghai Yuan, Chen Wang, Lihua Xie
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.9，机器人 1.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《AirLeg: A Robust and Accurate Self-Supervised Visual-Inertial-Leg SLAM System》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual-inertial-leg (VIL) state estimation offers cost-effective localization for legged robots, adding only a camera to the onboard IMU and joint encoders. However, learning-based leg odometry is limited by its supervision: networks trained in simulation suffer from the sim-to-real gap, while real-world labels require costly sensors or inherit the errors of visual estimates. To address this, we present AirLeg, a self-supervised VIL SLAM system in which vision and leg proprioception improve each other from training to deployment. We pre-train the leg odometry network in simulation and adapt it to the robot without ground truth through imperative learning, where multi-sensor bundle adjustment uses the leg odometry to refine the visual map, which in turn supervises the network. During deployment, the fused estimates adapt the network online. To improve both localization and this supervision, a dual-window estimator fuses vision, IMU, and leg odometry, relates loaded feet to the visually reconstructed terrain through a deformation-aware constraint, and weights the constraints by variance component estimation. AirLeg completes all 17 GrandTour sequences with the lowest average error (0.19 m) among 19 methods. On a low-cost quadruped, it achieves the lowest drift (0.6%) with only 0.5 h of unlabeled data, in real time on an embedded computer.

</details>

---

### [[20_Research/Papers/机器人/MRCT_An_Object-Centric_Two-Layer_Control_Architecture_for_Heavy-Payload_Multi-Robot_Transportation|MRCT: An Object-Centric Two-Layer Control Architecture for Heavy-Payload Multi-Robot Transportation]]

![[assets/2611.32502_figure.png|800]]

- **arXiv**: [2611.32502](https://arxiv.org/abs/2611.32502)
- **PDF**: https://arxiv.org/pdf/2611.32502
- **详细分析**: [[20_Research/Papers/机器人/MRCT_An_Object-Centric_Two-Layer_Control_Architecture_for_Heavy-Payload_Multi-Robot_Transportation|MRCT: An Object-Centric Two-Layer Control Architecture for Heavy-Payload Multi-Robot Transportation]]
- **作者**: Ning Wang, Yoshihiko Nakamura, Tianwei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《MRCT: An Object-Centric Two-Layer Control Architecture for Heavy-Payload Multi-Robot Transportation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative transportation of heavy payloads by heterogeneous mobile manipulators requires coordinated payload motion, force distribution, and compliant physical interaction. This paper presents MRCT, an object-centric two-layer control architecture for multi-robot transportation. At the object level, a model predictive controller (MPC) generates a coordinated contact-force reference for the payload. At the robot level, whole- body impedance control (WBIC) modules on individual robots realise the reference through a confidence-based blending of velocity-tracking and impedance torques. The blending mechanism emphasises tracking when the joint-velocity error is small and increases compliance when tracking degrades because of abrupt reference changes or physical disturbances. Simulation and hardware experiments with a heterogeneous team comprising a single-arm and a dual-arm mobile manipulator transporting a near-rated table payload demonstrate accurate object tracking, regulated contact forces, and stable payload orientation. Parameter sensitivity studies, obstacle-avoidance transportation, and step-load disturbance experiments further demonstrate the effectiveness of MRCT for reliable cooperative transportation under the evaluated conditions

</details>

---

### [[20_Research/Papers/具身智能/CoFiNav_VLM-Guided_Coarse-to-Fine_Semantic_Navigation_for_Open-Ended_Last-Mile_UAV_Delivery|CoFiNav: VLM-Guided Coarse-to-Fine Semantic Navigation for Open-Ended Last-Mile UAV Delivery]]

![[assets/2611.32493_figure.png|800]]

- **arXiv**: [2611.32493](https://arxiv.org/abs/2611.32493)
- **PDF**: https://arxiv.org/pdf/2611.32493
- **详细分析**: [[20_Research/Papers/具身智能/CoFiNav_VLM-Guided_Coarse-to-Fine_Semantic_Navigation_for_Open-Ended_Last-Mile_UAV_Delivery|CoFiNav: VLM-Guided Coarse-to-Fine Semantic Navigation for Open-Ended Last-Mile UAV Delivery]]
- **作者**: Xuanpu Wang, Shun Hu, Bing Li, Rongqing Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.3，大模型 0.6，机器人 1.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《CoFiNav: VLM-Guided Coarse-to-Fine Semantic Navigation for Open-Ended Last-Mile UAV Delivery》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Unmanned aerial vehicle (UAV) delivery is an important application of the low-altitude economy, enhancing the flexibility and accessibility of last-mile logistics. Existing UAV delivery methods generally rely on precise terminal coordinates, predefined terminal specifications, or task-specific localization procedures, limiting the scope and flexibility of delivery. As UAV logistics becomes more intelligent, open-ended semantic descriptions offer a new paradigm for specifying terminal destinations. However, conventional aerial navigation methods have limited ability to generalize to delivery scenarios that require open-vocabulary terminal navigation. To enable this broader delivery paradigm, we propose CoFiNav, a VLM-guided coarse-to-fine UAV semantic navigation framework that progressively grounds relation-defined terminal destinations through hierarchical semantic search and active 3D observation. Given a task description, a coarse prior map from OpenStreetMap (OSM), and accumulated observations, CoFiNav uses a vision-language model (VLM) to determine which unresolved entity or spatial relation should be verified next. A geometry-aware module converts the semantic observation request into feasible viewpoints using RGB images and LiDAR, while conventional motion planning handles safe execution. Experiments across multiple urban environments show that CoFiNav outperforms representative adapted baselines in success rate while requiring shorter flight paths and fewer observations.

</details>

---

### [[20_Research/Papers/具身智能/ViTacLab_Physically_Consistent_Visuo-Tactile_Simulation,_Benchmarking,_and_Representation_Learning_for_Robotic_Manipulation|ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation]]

![[assets/2611.32476_figure.png|800]]

- **arXiv**: [2611.32476](https://arxiv.org/abs/2611.32476)
- **PDF**: https://arxiv.org/pdf/2611.32476
- **详细分析**: [[20_Research/Papers/具身智能/ViTacLab_Physically_Consistent_Visuo-Tactile_Simulation,_Benchmarking,_and_Representation_Learning_for_Robotic_Manipulation|ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation]]
- **作者**: Linjing You, Zeming Yang, Zhenhao Shen, Shengqiang Xu, Guanda Li, Wenxuan Li, Jiyu Guo, Jasper Lu, Kyle Xu, Shawn Xie, Junjie Zhu, Siyu Wu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《ViTacLab: Physically Consistent Visuo-Tactile Simulation, Benchmarking, and Representation Learning for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World, ViTacBench, ViTacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing is essential for contact-rich robotic manipulation, but existing visuo-tactile simulators trade physical fidelity for scalability, and benchmarks largely focus on two-finger grippers. We present ViTacLab, a framework comprising ViTacSim, ViTacBench, and ViTacPolicy. ViTacSim uses a tri-modal tactile primitive: a global sparse contact-force lattice, a local dense force array, and tactile images. Anchored to PhysX contact-solver outputs, it corrects normal inconsistency through local stiffness alignment and reconstructs tangential forces under decoupled slip-stick regimes while preserving GPU parallelism. A joint projection preserves the sparse wrench and enforces local friction cones. ViTacBench spans parallel grippers, dexterous hands, and bimanual systems, with tasks ranging from vision-dominant to tactile-dominant regimes. ViTacPolicy aggregates variable numbers of heterogeneous tactile inputs using spatial-pose embeddings and a Transformer, and aligns force-array and tactile-image modalities through a two-stream VQ-VAE with a shared codebook. Controlled Hertzian-reference indentation and real-sensor sliding tests reduce normal and tangential force RMSE from 2.31 and 1.85 N to 0.42 and 0.53 N, respectively. Throughput reaches 2,482.9 tactile-pipeline FPS at 256 parallel environments. Simulation and real-world experiments show gains on several contact-rich tasks, while low absolute success on tactile-dominant tasks highlights the remaining difficulty of purely tactile control.

</details>

---

### [[20_Research/Papers/机器人/A_Face_Robot_which_Imitates_Human_Musculoskeletal_Skin_System_and_Its_Evaluation_on_Basic_Movement_of_Facial_Expression|A Face Robot which Imitates Human Musculoskeletal Skin System and Its Evaluation on Basic Movement of Facial Expression]]

![[assets/2611.32413_figure.png|800]]

- **arXiv**: [2611.32413](https://arxiv.org/abs/2611.32413)
- **PDF**: https://arxiv.org/pdf/2611.32413
- **详细分析**: [[20_Research/Papers/机器人/A_Face_Robot_which_Imitates_Human_Musculoskeletal_Skin_System_and_Its_Evaluation_on_Basic_Movement_of_Facial_Expression|A Face Robot which Imitates Human Musculoskeletal Skin System and Its Evaluation on Basic Movement of Facial Expression]]
- **作者**: Shun Kaneko, Shunnosuke Yoshimura, Akihiro Miki, Kento Kawaharazuka, Kei Okada
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Face Robot which Imitates Human Musculoskeletal Skin System and Its Evaluation on Basic Movement of Facial Expression》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Facial robots require many coordinated, smallamplitude motions, but accommodating these motions in a compact face remains difficult. This paper presents an anatomically inspired facial-robot platform that reproduces the layered organization of the human facial musculoskeletal system. The platform comprises bone, muscle, and skin components whose geometry, shape, and attachment locations are derived from three-dimensional anatomical data. Wire-driven, compliant muscle components are routed through PTFE tubes, allowing actuation to be placed away from the face. We describe the selection and fabrication of 65 muscles (34 muscle types) required to reproduce the 47 target action units (AUs) in the Facial Action Coding System (FACS). We then evaluate the reproducibility of individual AUs in two stages: muscle actuation without skin and actuation after the silicone skin is attached. Forty of the 47 target AUs were reproduced with the muscle components, and 30 were reproduced after skin attachment. These results demonstrate the feasibility of reproducing a broad range of FACS facial expressions using an anatomically inspired musculoskeletal structure. The proposed platform provides a foundation for the systematic development and evaluation of future anatomically inspired facial robots

</details>

---

### [[20_Research/Papers/大模型/Any2Act_Scaling_In-Context_Robot_Learning_from_Heterogeneous_Demonstrations|Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations]]

![[assets/2611.32353_figure.png|800]]

- **arXiv**: [2611.32353](https://arxiv.org/abs/2611.32353)
- **PDF**: https://arxiv.org/pdf/2611.32353
- **详细分析**: [[20_Research/Papers/大模型/Any2Act_Scaling_In-Context_Robot_Learning_from_Heterogeneous_Demonstrations|Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations]]
- **作者**: Ziang Ren, Zifan Wang, Zhuoyang Li, Benhao Qin, Haoyang Li, Qingtao Liu, Xuchuan Chen, Zekun Qi, He Wang, Yanchao Yang, Li Yi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《Any2Act: Scaling In-Context Robot Learning from Heterogeneous Demonstrations》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot in-context learning (ICL) enables a policy to perform unseen tasks by following contextual demonstrations, without task-specific fine-tuning. This is increasingly valuable as large language models reasoning at low frequency can specify tasks through demonstrations and delegate high-frequency execution to such a policy. However, methods conditioned on human videos are bounded by scarce human-robot pairs, while those conditioned on robot demonstrations accept only one or two source types at limited scale. We present Any2Act, a foundation model for robot ICL. Our key insight is that a demonstration should be expressed in the camera layout and action space of the robot that performs it (the executor), not of whoever provided it (the demonstrator). This unified embodiment-grounded representation decouples learning to follow from admitting a new source. Any2Act learns to follow once, from robot-to-robot pairs that already take this form in 1.2M real trajectories spanning 10K tasks. Human videos, simulation, UMI, and other robots are then translated into this representation, and source-routed adapters trained on only a few hundred pairs each absorb the residual gap while the pretrained model stays frozen. For long horizons, a training-free tracker feeds only the demonstration window around the executor's progress, bounding the context and rolling back to redo failed steps. From a single demonstration, Any2Act achieves 57.5% success on unseen tasks without fine-tuning, exceeding VLAs fine-tuned on 50 demonstrations per task; other demonstrators retain 74-91% of the success achieved with the executor's own demonstrations.

</details>

---

### [[20_Research/Papers/机器人/Putting_a_Robot_on_a_Phone_Call_Layered_Signaling,_Bounded_Occupancy_and_Turn_Arbitration_over_WebRTC|Putting a Robot on a Phone Call: Layered Signaling, Bounded Occupancy and Turn Arbitration over WebRTC]]

![[assets/2611.32308_first_page.png|800]]

- **arXiv**: [2611.32308](https://arxiv.org/abs/2611.32308)
- **PDF**: https://arxiv.org/pdf/2611.32308
- **详细分析**: [[20_Research/Papers/机器人/Putting_a_Robot_on_a_Phone_Call_Layered_Signaling,_Bounded_Occupancy_and_Turn_Arbitration_over_WebRTC|Putting a Robot on a Phone Call: Layered Signaling, Bounded Occupancy and Turn Arbitration over WebRTC]]
- **作者**: Zheyuan Zhang, Zaide Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Putting a Robot on a Phone Call: Layered Signaling, Bounded Occupancy and Turn Arbitration over WebRTC》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We put a Thor robot on a browser voice call, with speech sent from Safari, answers played through the robot's loudspeaker and transcripts returned to the phone. We separate HTTPS signaling, relayed WebRTC media and speech generation into independently observable routes. The browser prefetches relay credentials and allows a 500 ms window after its first relay candidate. The backend starts speech and WebRTC-answer preparation concurrently within a 55 s deadline. A session slot and a non-blocking speaker lock coordinate calls with local voice access. A 2 s gate gives the controller an opportunity to suppress chat before playback. Fifteen of sixteen first dials reached ready-to-speak, comprising seven of eight Wi-Fi calls with a median of 5.57 s and eight of eight cellular calls with a median of 6.76 s. All twenty scored occupancy and recovery scenarios admitted a later call. During five 60 s outages, the backend released the line while the phone remained offline. Across 40 controlled replays, enabling the gate suppressed chat when the controller decided at 1 s. At 3 s, chat and controller feedback both played in sequence, with no overlapping output in any trace. Two additional boundary traces exposed a receipt naming a later feedback item and a new call's query returning its predecessor's feedback. These measurements cover application events on one platform and simulated controller decisions, with acoustic output and task correctness outside their scope.

</details>

---

### [[20_Research/Papers/具身智能/EgoLoAF_Learning_Humanoid_Loco-Manipulation_from_Egocentric_Demonstrations_with_Hand-Object_Affordances|EgoLoAF: Learning Humanoid Loco-Manipulation from Egocentric Demonstrations with Hand-Object Affordances]]

![[assets/2611.32260_figure.png|800]]

- **arXiv**: [2611.32260](https://arxiv.org/abs/2611.32260)
- **PDF**: https://arxiv.org/pdf/2611.32260
- **详细分析**: [[20_Research/Papers/具身智能/EgoLoAF_Learning_Humanoid_Loco-Manipulation_from_Egocentric_Demonstrations_with_Hand-Object_Affordances|EgoLoAF: Learning Humanoid Loco-Manipulation from Egocentric Demonstrations with Hand-Object Affordances]]
- **作者**: Yiming Zeng, Jiangyuxuan Dai, Yuheng Na, Tan Zhu Xuan, Zihan Lin, Xinfang Qi, Shijian Zhang, Chengqi Shi, Yihan Kuang, Zhide Zhong, Junjie He, Junfeng Li...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《EgoLoAF: Learning Humanoid Loco-Manipulation from Egocentric Demonstrations with Hand-Object Affordances》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EgoVLA, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training humanoid vision-language-action (VLA) models relies heavily on costly real-robot teleoperation. Recent efforts convert egocentric human demonstrations into humanoid training data. However, most methods still require wearable motion trackers and leave important hand-object interaction cues implicit. Many also mix in real-robot teleoperation data for VLA post-training. These dependencies limit scalable data collection, while implicit interaction cues make precise contact harder to learn. To overcome these limitations, we propose EgoLoAF, the first paradigm to derive all training data for humanoid loco-manipulation directly from egocentric demonstrations without wearable motion trackers. We post-train the VLA on the converted data alone, without real-robot teleoperation demonstrations, and use explicit hand-object interaction cues to guide action generation. Specifically, to obtain humanoid action targets, we estimate torso motion from recorded camera poses and reconstruct both hand trajectories from video. From the same recording, we use each hand's current pose relative to the object to represent hand-object affordances. During post-training, we inject these affordances into the action expert through cross-attention while keeping the vision-language backbone frozen. Additionally, we release 128,400 egocentric demonstration episodes spanning 1,000 hours and 1,284 tasks, together with converted humanoid action trajectories and rendered robot-view observations. Across four real-world tasks, EgoLoAF nearly achieves teleoperation performance (73.1 vs. 74.4 in mean Task Progress Score), while achieving a mean 4.03 times improvement in data-collection efficiency.

</details>

---

### [[20_Research/Papers/具身智能/VLAs_Execute,_Code_Recovers_3D_Skill_Envelopes_Bridge_the_Compositional_Gap_in_Agentic_Manipulation|VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation]]

![[assets/2611.32245_figure.png|800]]

- **arXiv**: [2611.32245](https://arxiv.org/abs/2611.32245)
- **PDF**: https://arxiv.org/pdf/2611.32245
- **详细分析**: [[20_Research/Papers/具身智能/VLAs_Execute,_Code_Recovers_3D_Skill_Envelopes_Bridge_the_Compositional_Gap_in_Agentic_Manipulation|VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation]]
- **作者**: Jiajie Zhang, Yankai Xiang, Changhao Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《VLAs Execute, Code Recovers: 3D Skill Envelopes Bridge the Compositional Gap in Agentic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Composing frozen Vision-Language-Action (VLA) skills under an agentic planner promises scalable long-horizon manipulation without long-horizon demonstrations, yet strong atomic skills routinely fail at seams even under a correct plan. Standard remedies reset the robot's pose or draft entry conditions in language, missing the physical cause we uncover via causal interventions: even after re-homing, a frozen VLA rigidly retraces its habitual trajectory and collides with displaced scene residue, whether or not it can see it. We propose the Skill Envelope, a policy-measured 3D geometric precondition capturing the volume a frozen skill sweeps during successful executions. Exploiting the insight that the rigidity making a frozen skill fragile at seams also makes its trajectory predictable in advance, we expose each envelope as two classical 3D tools (CHECK to detect blocking residue and FREE to locate safe placement regions), establishing a division of labor where VLAs execute in-distribution manipulation and code repairs out-of-distribution states. On LIBERO-Goal with frozen $π_{0.5}$, our zero-failure envelope predicts collisions at 0.946 AUROC (0.944 from one RGB-D view) and beats frontier VLMs on seam readiness (0.902 vs. 0.793); using it for skill ordering and code repair lifts success from 82.8% to 92.3% on two-step seams and from 29.7% to 93.8% on drawer-bearing 3-4 step chains, matching privileged world reset. Together, these results show that reliable VLA composition hinges on measuring a policy's physical workspace rather than guessing preconditions in language. Ongoing work closes the loop with autonomous LLM orchestration, synthesized free-object recovery, and cross-policy evaluation on cluttered benchmarks and real hardware.

</details>

---

### [[20_Research/Papers/具身智能/Reading_Geometric_Anchors_Viewpoint_Generalization_in_Imitation_Learning_for_Robotic_Manipulation_with_RGB-Only_Deployment|Reading Geometric Anchors: Viewpoint Generalization in Imitation Learning for Robotic Manipulation with RGB-Only Deployment]]

![[assets/2611.32162_figure.png|800]]

- **arXiv**: [2611.32162](https://arxiv.org/abs/2611.32162)
- **PDF**: https://arxiv.org/pdf/2611.32162
- **详细分析**: [[20_Research/Papers/具身智能/Reading_Geometric_Anchors_Viewpoint_Generalization_in_Imitation_Learning_for_Robotic_Manipulation_with_RGB-Only_Deployment|Reading Geometric Anchors: Viewpoint Generalization in Imitation Learning for Robotic Manipulation with RGB-Only Deployment]]
- **作者**: Chengyu Tao, Chunxi Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Reading Geometric Anchors: Viewpoint Generalization in Imitation Learning for Robotic Manipulation with RGB-Only Deployment》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FPV-Net, MetaWorld, PointNet, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Moving the camera changes where objects appear in an image, challenging RGB-based imitation learning. A common strategy pairs synthesized views with the same demonstrated action, but ignores supporting physical correspondence across views. By predicting depth with camera calibrations, 3D policies may handle it yet suffer the issue of varied observed point sets. To address these limitations, we propose ReGeoAnch, a geometry-anchored imitation learning framework for viewpoint generalization. Specifically, we build global anchors in the robot base frame and local anchors in the gripper frame, providing shared physical references across viewpoints. Furthermore, Decoupled Appearance-Guided Geometric Readout uses Point-to-Anchor Aggregation (PAA) to obtain comparable and stable geometry around anchors beyond pointwise correspondence. A controllable and decoupled information flow, Anchor-to-Policy Readout (APR), leverages complementary visual and geometric information and supports viewpoint generalization: view-dependent appearances are queried by view-invariant robot state to select task-relevant anchors, with geometric values alone to form the final readout. We further introduce Cross-View Readout Consistency to align the directions of policy readouts from paired source and synthesized target views. Experiments on 12 manipulation tasks across MetaWorld and ManiSkill3 demonstrate improved viewpoint generalization over baseline policies.

</details>

---

### [[20_Research/Papers/强化学习/Ego2Real_Learning_Bimanual_Dexterous_Manipulation_from_Egocentric_Visuo-Tactile_Demonstrations|Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations]]

![[assets/2611.32101_figure.png|800]]

- **arXiv**: [2611.32101](https://arxiv.org/abs/2611.32101)
- **PDF**: https://arxiv.org/pdf/2611.32101
- **详细分析**: [[20_Research/Papers/强化学习/Ego2Real_Learning_Bimanual_Dexterous_Manipulation_from_Egocentric_Visuo-Tactile_Demonstrations|Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations]]
- **作者**: Ange Bao, Haishan Zhang, Lingzi Xie, Shuang Li, Pei Zhao, Ling Shi, Bidan Huang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.4（加权：具身智能 1.5，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Ego2Real: Learning Bimanual Dexterous Manipulation from Egocentric Visuo-Tactile Demonstrations》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning dexterous manipulation from egocentric human demonstrations offers a scalable path toward robot skill acquisition. Vision alone, however, provides limited information about physical contacts and the demonstrator's force intent, leading to ambiguities in interpreting hand-object interactions. Capturing human touch via tactile sensing is therefore crucial for reliable human-to-robot dexterous skill transfer. We present Ego2Real, a framework that leverages egocentric demonstrations and tactile gloves to transfer bimanual dexterous manipulation skills to robotic hands. Ego2Real incorporates tactile supervision at two complementary stages: (1) tactile-guided hand-object interaction reconstruction, which uses measured tactile signals to refine hand poses and contact geometry; and (2) contact-informed reinforcement learning, which translates human contact patterns into robotic contact rewards. By combining refined motion references with physical contact rewards during training, Ego2Real guides anthropomorphic robotic hands to emulate demonstrated contact behaviors while adapting to their own morphology and actuation. Experiments show that incorporating tactile supervision into both reconstruction and policy learning yields higher manipulation success rates, underscoring the importance of enriching egocentric demonstrations with tactile observations to improve their quality and transferability.

</details>

---

### [[20_Research/Papers/具身智能/KeyMemVLA_Subtask-Guided_Key_Memory_for_Long-Horizon_Robotic_Manipulation|KeyMemVLA: Subtask-Guided Key Memory for Long-Horizon Robotic Manipulation]]

![[assets/2611.32081_figure.png|800]]

- **arXiv**: [2611.32081](https://arxiv.org/abs/2611.32081)
- **PDF**: https://arxiv.org/pdf/2611.32081
- **详细分析**: [[20_Research/Papers/具身智能/KeyMemVLA_Subtask-Guided_Key_Memory_for_Long-Horizon_Robotic_Manipulation|KeyMemVLA: Subtask-Guided Key Memory for Long-Horizon Robotic Manipulation]]
- **作者**: Yongwei Zhang, Tao Chen, Sicheng Ma, Yuanzhe Xing, Pengwei Zhang, Yongen Zhao, Yaoqing Hu, Zhikun She, Ce Hao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《KeyMemVLA: Subtask-Guided Key Memory for Long-Horizon Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：KMBench, KeyMemVLA, RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-dependent long-horizon manipulation requires vision-language-action (VLA) policies to infer task progress and recall evidence absent from current observations. Under a limited memory budget, the challenge is to retain history that resolves stage ambiguity and supports subsequent decisions. We present KeyMemVLA, a subtask-guided key memory framework based on progress indication and decision-evidence retention. A two-level annotation process selects subtasks satisfying either criterion and labels their final frames as keyframes to supervise online memory writes. A shared vision-language backbone jointly learns subtask, action, and keyframe prediction. At inference, the policy first predicts the current subtask from the instruction, visual context, and memory, then uses this semantic condition to predict actions and future memory-write positions. Actual observations are retained at the selected times during execution. We introduce KMBench to evaluate active memory retention for decisions across subtasks. Evaluations on RMBench-$M(n)$, RoboTwin-MeM, KMBench, and real-world manipulation tasks show higher average success rates than the compared baselines. Ablation studies and representation analysis support the roles of key memory and explicit task-progress semantics. These results highlight the value of coupling sparse key memory with online progress inference for history-dependent control.

</details>

---

### [[20_Research/Papers/具身智能/Learning_When_a_Robot_Should_Ask_For_Help_Adaptive_Intervention_Requests_in_Human-Robot_Teaming|Learning When a Robot Should Ask For Help: Adaptive Intervention Requests in Human-Robot Teaming]]

![[assets/2611.31925_figure.png|800]]

- **arXiv**: [2611.31925](https://arxiv.org/abs/2611.31925)
- **PDF**: https://arxiv.org/pdf/2611.31925
- **详细分析**: [[20_Research/Papers/具身智能/Learning_When_a_Robot_Should_Ask_For_Help_Adaptive_Intervention_Requests_in_Human-Robot_Teaming|Learning When a Robot Should Ask For Help: Adaptive Intervention Requests in Human-Robot Teaming]]
- **作者**: Yanran Jiang, Cécile Paris, Dana Kulić, Leimin Tian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning When a Robot Should Ask For Help: Adaptive Intervention Requests in Human-Robot Teaming》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots operating in complex environments occasionally encounter situations where autonomous navigation fails. Requesting and receiving a timely intervention from their human supervisor can be critical for failure prevention or recovery. However, requesting help too frequently or at inappropriate times can increase operator workload and reduce team efficiency, while delayed requests may lead to prolonged downtime or unrecoverable failures. In addition to alert timing, the human, robot and task context also influences the intervention outcomes. This paper proposes an algorithm for learning to generate adaptive human intervention requests during human-robot teaming. A help-seeking policy is trained via offline reinforcement learning based on past intervention helpfulness and autonomous progress. This learned alert policy enables a robot to selectively request human help when the intervention outcome is likely to be beneficial. We evaluate the proposed policy in different task environments and user expertise levels in simulation, followed by evaluation in a physical user study. Our findings demonstrate that the learned policy improves exploration efficiency, reduces unnecessary alerts, and enhances novice user support without compromising expert performance in real-time human-robot teaming missions.

</details>

---

### [[20_Research/Papers/具身智能/RESET_One_Demonstration,_One_Verified_World,_Self-Improved_Skills_Across_Embodiments|RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments]]

![[assets/2611.31894_figure.png|800]]

- **arXiv**: [2611.31894](https://arxiv.org/abs/2611.31894)
- **PDF**: https://arxiv.org/pdf/2611.31894
- **详细分析**: [[20_Research/Papers/具身智能/RESET_One_Demonstration,_One_Verified_World,_Self-Improved_Skills_Across_Embodiments|RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments]]
- **作者**: Zheng Sun, Zhuo Li, Zhihao Li, Hengyi Sim, Ge Wang, Ziyue Zhu, Mingkai Jia, Fei Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《RESET: One Demonstration, One Verified World, Self-Improved Skills Across Embodiments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：D-World, Re3Sim, Real-World, Real-to-Sim, X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language model (LLM) coding agents can iteratively self-improve robot manipulation skills in simulation benchmarks, yet real-world tasks provide neither ground-truth success scorers nor resettable practice environments. Our key observation is that a single real demonstration simultaneously specifies scene geometry, defines the terminal success criterion, and serves as a physical reference trajectory for verifying world fidelity---all decoupled from the source robot's kinematics. We present {RESET}: we reconstruct a contact-rich world and derive a frozen read-only criterion from one demonstration ({R}ebuild); check that world against the demonstration by open-loop replay and silhouette consistency ({E}xamine); evolve modular white-box task graphs and skill code from per-node failure evidence ({S}elf-improve); deploy frozen code on real robots with zero runtime LLM calls ({E}xecute); and share the verified world and criterion with unseen robots without new demonstrations ({T}ransfer). On 8 manipulation tasks, each rebuilt from one real demonstration, RESET achieves 97% average success on unseen layouts in simulation, whereas zero-shot code reaches 27%, per-task fine-tuned pi0.5 policies 31%, and Diffusion Policy 50%; injecting reconstruction defects shows that practice tolerates many reconstruction errors, that geometric errors can still stall or mislead it, and that the check flags most of them while physical randomization covers the rest. Without any target demonstrations, 3 heterogeneous robots acquire the same task skills in the shared world: a robot with similar arms copies 95% of its skill functions unchanged from the source robot, while robots with different arms and hands write their own. In real-robot experiments, the resulting programs run on 4 robots and succeed in 80% of 280 trials.

</details>

---

### [[20_Research/Papers/机器人/Ada-BFM_Adapting_Behavior_Foundation_Models_for_Humanoid_Scene_Interaction|Ada-BFM: Adapting Behavior Foundation Models for Humanoid Scene Interaction]]

![[assets/2611.31863_figure.png|800]]

- **arXiv**: [2611.31863](https://arxiv.org/abs/2611.31863)
- **PDF**: https://arxiv.org/pdf/2611.31863
- **详细分析**: [[20_Research/Papers/机器人/Ada-BFM_Adapting_Behavior_Foundation_Models_for_Humanoid_Scene_Interaction|Ada-BFM: Adapting Behavior Foundation Models for Humanoid Scene Interaction]]
- **作者**: Furui Xu, Weishuai Zeng, Zirui Wang, Kangning Yin, Jiacheng Bao, Huayi Wang, Yingying Qin, Yufei Xue, Yang Tang, Zenghao Tang, Kailin Li, Jingbo Wang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Ada-BFM: Adapting Behavior Foundation Models for Humanoid Scene Interaction》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Behavior Foundation Models (BFMs) have emerged as a promising paradigm for general-purpose humanoid control through pretraining on large-scale behavioral data. However, their proficiency in whole-body coordination does not readily extend to scene interaction, which requires adapting motion to scene-dependent geometric constraints and contact dynamics. To bridge this gap, we introduce Ada-BFM, a post-training framework that adapts pretrained BFMs for humanoid scene interaction. Ada-BFM augments the original architecture with a lightweight adapter, enabling interaction-specific adjustments while leveraging pretrained control capabilities. Rather than producing a separate controller for each task, the framework yields a shared model for each interaction domain, supporting diverse tasks involving terrain or object interaction. Extensive experiments in simulation and the real world demonstrate that Ada-BFM enables diverse scene interaction behaviors, accelerates learning compared with training from scratch, and largely preserves pretrained behavioral competence. These findings establish Ada-BFM as an effective and efficient approach to extending the capabilities of BFMs beyond their pretraining settings while retaining their strengths in general whole-body control.

</details>

---

### [[20_Research/Papers/具身智能/Co-DRIS_Physics-Informed_Predictive_Belief_and_Variable-Impedance_Learning_for_Reactive_Catching_under_Coupled_Uncertainty|Co-DRIS: Physics-Informed Predictive Belief and Variable-Impedance Learning for Reactive Catching under Coupled Uncertainty]]

![[assets/2611.31843_first_page.png|800]]

- **arXiv**: [2611.31843](https://arxiv.org/abs/2611.31843)
- **PDF**: https://arxiv.org/pdf/2611.31843
- **详细分析**: [[20_Research/Papers/具身智能/Co-DRIS_Physics-Informed_Predictive_Belief_and_Variable-Impedance_Learning_for_Reactive_Catching_under_Coupled_Uncertainty|Co-DRIS: Physics-Informed Predictive Belief and Variable-Impedance Learning for Reactive Catching under Coupled Uncertainty]]
- **作者**: Yonglong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.3（加权：具身智能 0.6，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《Co-DRIS: Physics-Informed Predictive Belief and Variable-Impedance Learning for Reactive Catching under Coupled Uncertainty》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reactive robotic manipulation is acutely sensitive to simultaneous sensing noise, measurement dropouts, joint execution errors, and contact parameter variations. While single-frame frameworks like Domain-Randomized Instance Set (DRIS) achieve strong robustness under isolated uncertainties (86.4%), they degrade severely when perception and actuation uncertainties co-occur (27.6% across 10 coupled stress scenarios) due to memoryless encoding and fixed high-stiffness PD control. We propose Co-DRIS + SuperMimic, a perception-action co-design framework coupling: (i) an inertial world-frame physics-informed world model combining exact ballistic kinematics with a zero-initialized contact residual to roll forward missing observations and accelerate training via zero-cost counterfactual dropout consistency; (ii) an action-conditioned dual-stream causal GRU belief encoder resolving the denoising-vs-lag deadlock; and (iii) phase-aware variable-impedance soft-catching that transitions the 7-DoF Franka Research 3 arm into an overdamped regime (zeta/zeta0 ~ 2.26x) at the torque layer. Under unbiased 3-seed tail evaluation on unseen throws (15,360 throws/scenario), our method achieves 89.6 +/- 0.4% on standard benchmarks (+10.5% on 4-sigma noise to 70.5%) and 66.6 +/- 0.5% across 10 coupled/dropout stress scenarios (+39.0% over DRIS; +30.4% on 50% dropout). We further validate impedance decoupling, causal contact triggering under +0.65 s flight-time shifts, and cross-task transfer to steel-plate ping-pong bouncing (87.5% to 100.0%) and FR3+Hand catching (+8.4% under 4x noise with 6-13% lower peak impact force).

</details>

---

### [[20_Research/Papers/大模型/Many_Senses,_One_World_Learning_Hierarchical_Multimodal_World_Representations_for_Bimanual_Dexterous_Manipulation|Many Senses, One World: Learning Hierarchical Multimodal World Representations for Bimanual Dexterous Manipulation]]

![[assets/2611.31782_figure.png|800]]

- **arXiv**: [2611.31782](https://arxiv.org/abs/2611.31782)
- **PDF**: https://arxiv.org/pdf/2611.31782
- **详细分析**: [[20_Research/Papers/大模型/Many_Senses,_One_World_Learning_Hierarchical_Multimodal_World_Representations_for_Bimanual_Dexterous_Manipulation|Many Senses, One World: Learning Hierarchical Multimodal World Representations for Bimanual Dexterous Manipulation]]
- **作者**: Jin Yang, Youlin Wang, Ping Wei
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.4，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Many Senses, One World: Learning Hierarchical Multimodal World Representations for Bimanual Dexterous Manipulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MoDE-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual dexterous manipulation relies on multimodal inputs that capture visual context and non-visual physical interaction cues for precise and coordinated control. To address the challenge of effectively integrating these modalities for policy learning, we propose HiMoDex, a two-stage framework centered on hierarchical multimodal world-state representations. In Stage 1, we pretrain a hierarchical representation network on the collected dataset of 1.19 million synchronized multimodal time steps. The network integrates visual context with tactile, force-torque, and audio cues into unified world-state embeddings. In Stage 2, we freeze the pretrained network and use its embeddings to condition a shared world-action transformer. The transformer jointly learns action generation and action-conditioned future-state prediction. Experiments across five real-world tasks show that HiMoDex achieves an average success rate of 78.7\%, representing an absolute improvement of 32.0\% over the strongest evaluated baseline. Extensive ablations validate the benefits of hierarchical representation learning and two-stage training. Failure analysis helps explain performance differences across variants. Code, data, and demos will be released at https://anonymous.4open.science/w/research-website-BAB4/.

</details>

---

### [[20_Research/Papers/具身智能/Sparks_of_Weight-Space_Programming_for_Robot_Foundation_Models|Sparks of Weight-Space Programming for Robot Foundation Models]]

![[assets/2611.31715_first_page.png|800]]

- **arXiv**: [2611.31715](https://arxiv.org/abs/2611.31715)
- **PDF**: https://arxiv.org/pdf/2611.31715
- **详细分析**: [[20_Research/Papers/具身智能/Sparks_of_Weight-Space_Programming_for_Robot_Foundation_Models|Sparks of Weight-Space Programming for Robot Foundation Models]]
- **作者**: Kyle Coelho, Eugen Solowjow
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Sparks of Weight-Space Programming for Robot Foundation Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper demonstrates an approach for correcting failures of robot foundation models (RFMs) without additional data collection, demonstrations, or training. We apply weight-space programming (WSP), in which a language-model agent directly reads and writes a neural network's parameters, to a large, pre-trained vision-language-action policy. The idea is simple: many policy failures are not random but repeatedly land in the same recognizable stuck state, so if that state is visible in the model's internal activations, a small edit could trigger a corrective movement while leaving the rest of the model's parameters unchanged. A core design choice is where to write the edit: repurposing a few near-silent neurons in the action expert lets the edit switch on in situations associated with the failure and produce a corrective movement, such as lowering the gripper toward the target, that is specified directly rather than learned through training. Empirically, when applied to the pi0.5 policy in simulation, we find that edits to roughly 0.0002% of the parameters can improve success on recurring failures, including for a policy that was already fine-tuned on its task. Reversed and random edits indicate that the gains come from the intended behavior, and the approach works best when the failure situation is recognizable and a simple correction can address it.

</details>

---

### [[20_Research/Papers/具身智能/FabricBench_A_Standardized_Policy_Benchmark_for_Bimanual_Fabric_Manipulation_with_a_Contact-Driven_Deformable_Simulator|FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator]]

![[assets/2611.31577_figure.png|800]]

- **arXiv**: [2611.31577](https://arxiv.org/abs/2611.31577)
- **PDF**: https://arxiv.org/pdf/2611.31577
- **详细分析**: [[20_Research/Papers/具身智能/FabricBench_A_Standardized_Policy_Benchmark_for_Bimanual_Fabric_Manipulation_with_a_Contact-Driven_Deformable_Simulator|FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator]]
- **作者**: Wenkang Hu, Haoran Wang, Liu Liu, Wenchao Huang, Yiji Chen, Mengao Zhao, Xincheng Tang, Zhengjie Shu, Lai Jiang, Wei Li, Zhendong Wang, Zhizhong Su...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《FabricBench: A Standardized Policy Benchmark for Bimanual Fabric Manipulation with a Contact-Driven Deformable Simulator》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DaXBench, FabricBench, OpenVLA, RGBench, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Fabric manipulation challenges robot policies with changing geometry, self-occlusion, and contact, yet standardized evaluation remains focused on rigid objects. We introduce FabricBench, a benchmark for bimanual fabric manipulation with six tasks spanning garments, silk, and bags, 10,000 simulation-ready assets, and controlled tests of configuration and appearance generalization. Built on an open-source solver in Newton, our simulator enables stable bimanual grasping, holding, and release through contact forces, without artificial attachment. Redesigned cloth-rigid contact and bidirectional force coupling support interactions among robot arms, fabric, and free rigid objects, allowing a bag to support its contents and transmit their weight to the grippers. In a controlled grasp-hold-release evaluation, our solver succeeds in all 45 trials, compared with none for the tested baseline configurations. Evaluating six representative policies, including vision-language-action models and world action models, reveals substantial remaining challenges: the best policy achieves 77% average success, while no policy exceeds 36% on long-horizon T-shirt folding. Under the most deformed initial T-shirt configurations, success falls to 6-14% across policies, with larger drops than under the evaluated appearance shifts. Zero-shot deployment of $π_{0.5}$ on a real robot largely preserves task difficulty ordering across six tasks (Spearman $ρ=0.94$). These results establish FabricBench as a reproducible testbed for measuring fabric-manipulation capabilities and exposing limitations in configuration generalization. The project website is available at https://fabricbench.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Embodied_Neuro-symbolic_AI_Making_Robot_Behavior_Auditable,_Safe,_and_Scalable|Embodied Neuro-symbolic AI: Making Robot Behavior Auditable, Safe, and Scalable]]

![[assets/2611.31488_figure.png|800]]

- **arXiv**: [2611.31488](https://arxiv.org/abs/2611.31488)
- **PDF**: https://arxiv.org/pdf/2611.31488
- **详细分析**: [[20_Research/Papers/具身智能/Embodied_Neuro-symbolic_AI_Making_Robot_Behavior_Auditable,_Safe,_and_Scalable|Embodied Neuro-symbolic AI: Making Robot Behavior Auditable, Safe, and Scalable]]
- **作者**: Ruwan Wickramarachchi, Jonathan Francis, Alessandro Oltramari
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Embodied Neuro-symbolic AI: Making Robot Behavior Auditable, Safe, and Scalable》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Current Vision-Language-Action (VLA) end-to-end systems have driven major progress in robot learning, yet they still face persistent barriers to dependable real-world deployment. In practice, these models often exhibit brittle generalization under distribution shift (i.e., novel objects, layouts, lighting, or contact conditions), limited physical and causal reasoning, and inconsistent fine-grained motor control. Critically, many VLA pipelines offer limited ways to express and audit what a robot must not do, making it difficult to provide assurance in safety-critical settings. These limitations constrain scalability, maintainability, and trust when robots move beyond controlled demonstrations. We propose Embodied Neuro-Symbolic (NeSy) AI: a deployment-oriented paradigm that integrates learned perception, planning and control with explicit, machine-readable background knowledge and formal constraints. By combining knowledge-guided perception, constraint-aware symbolic planning, and hybrid learning, Embodied NeSy AI enables robots to reason about their environment, adapt to new tasks, and provide auditable, machine-checkable compliance with safety and operational requirements, thus supporting scalable, trustworthy robot deployment.

</details>

---

### [[20_Research/Papers/大模型/EvoMisty_Building,_Optimizing,_and_Evolving_Capabilities_on_a_Social_Robot|EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot]]

![[assets/2611.31341_figure.png|800]]

- **arXiv**: [2611.31341](https://arxiv.org/abs/2611.31341)
- **PDF**: https://arxiv.org/pdf/2611.31341
- **详细分析**: [[20_Research/Papers/大模型/EvoMisty_Building,_Optimizing,_and_Evolving_Capabilities_on_a_Social_Robot|EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot]]
- **作者**: Xiao Wang, Lu Dong, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《EvoMisty: Building, Optimizing, and Evolving Capabilities on a Social Robot》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social robots face diverse and changing tasks in companionship and education. LLM-based methods can generate task programs, but they still rely on manually developed control interfaces and predefined capabilities. They also lack a general mechanism to optimize completed tasks based on user-specified metrics and reuse performance improvements across tasks.We present EvoMisty, a plugin-based framework that enables coding agents to build and continually improve robot capabilities. EvoMisty builds a control program from official documentation and verifies candidate capabilities on a physical robot. Verified capabilities are stored in an atomic capability library and combined with existing skills to solve tasks. After task completion, EvoMisty can collect execution data, measure user-specified metrics, and iteratively improve task programs. It then distills reusable skills from final solutions into a skill library for future tasks.We evaluate EvoMisty on a physical Misty II robot using Claude Code and Codex. The two agents construct 109 and 107 verified atomic capabilities, respectively. Both complete all 28 AutoMisty benchmark tasks and seven additional tasks beyond AutoMisty's capabilities. Optimization improves all seven evaluated metrics across five tasks. For example, dialogue response latency decreases by 52% and 71%, respectively. Reusing skills from one optimized dialogue task reduces latency by 33% to 72% in three other dialogue tasks without further optimization. All code and experimental videos will be publicly released through the webpage: https://wangxiaoshawn.github.io/projects/evomisty/index.html

</details>

---
