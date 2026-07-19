# cs.RO | Robotics | 2026-07-17

#arxiv #ComputerScience

**论文数**: 28

### [[20_Research/Papers/机器人/Stigmergic_Graph_Memory_An_Environment-Aware_Approach_for_Many-to-Many_Multi-Agent_Pickup_and_Delivery|Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery]]

![[assets/2607.15182_figure.png|800]]

- **arXiv**: [2607.15182](https://arxiv.org/abs/2607.15182)
- **PDF**: https://arxiv.org/pdf/2607.15182
- **详细分析**: [[20_Research/Papers/机器人/Stigmergic_Graph_Memory_An_Environment-Aware_Approach_for_Many-to-Many_Multi-Agent_Pickup_and_Delivery|Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery]]
- **作者**: Aditya Dutta, Joon-Seok Kim
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Stigmergic Graph Memory: An Environment-Aware Approach for Many-to-Many Multi-Agent Pickup and Delivery》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automated fulfillment warehouses must continuously assign and execute pickup-and-delivery work while avoiding congestion. In many-to-many Multi-Agent Pickup and Delivery (MAPD), a request specifies a stock-keeping unit rather than fixed endpoints, requiring the controller to select an agent, source, and destination before path planning. Existing graph-guidance methods primarily influence routing after goals are fixed, leaving endpoint instantiation uninformed by recent traffic. We introduce Stigmergic Graph Memory (SGM), a bounded, decaying memory layer that records recent execution signals on warehouse nodes and directed edges to rank feasible endpoints and route preferences without altering collision constraints or planner validity. Across paired request streams on five layouts, three load levels, and 25 seeds per condition, SGM outperforms two reconstructed many-to-many allocation baselines in all 15 map-load conditions, with paired throughput gains of 20.5-36.7%. These results show that recent execution memory can improve warehouse throughput by shaping which feasible goals enter the planner, not only how agents travel to already fixed goals.

</details>

---

### [[20_Research/Papers/机器人/AHEAD_Anticipatory_Hand-Driven_Teleoperation_via_Human_Intent_Prediction|AHEAD: Anticipatory Hand-Driven Teleoperation via Human Intent Prediction]]

![[assets/2607.15172_figure.png|800]]

- **arXiv**: [2607.15172](https://arxiv.org/abs/2607.15172)
- **PDF**: https://arxiv.org/pdf/2607.15172
- **详细分析**: [[20_Research/Papers/机器人/AHEAD_Anticipatory_Hand-Driven_Teleoperation_via_Human_Intent_Prediction|AHEAD: Anticipatory Hand-Driven Teleoperation via Human Intent Prediction]]
- **作者**: Seok Joon Kim, Junho Lee, Federica Spinola, Taein Kwon, Mohsen Moghaddam
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《AHEAD: Anticipatory Hand-Driven Teleoperation via Human Intent Prediction》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Direct hand-driven teleoperation maps an operator's hand motion to robot end-effector commands at every frame, enabling precise control, but it requires constant monitoring and correction during approach, grasp, and placement, which can be slow and fatiguing. For repetitive pick-and-place tasks, supervisory (goal-based) teleoperation simplifies this process: the operator specifies goals/waypoints, and the robot executes the motion using planning algorithms. Yet, this introduces latency, as the robot must wait for the next command before it can plan and act. "How can we reduce robot reaction time while lowering operator workload?" To tackle this question, we present AHEAD, a real-time VR teleoperation system that anticipates operator intent to enable proactive, hand-driven control. In a digital twin, the operator performs pick-and-place naturally, using hand motion to convey high-level commands rather than a continuous robot trajectory. AHEAD processes a short window of 3D hand and head signals together with scene context through an attention-based classifier to predict the intended grasp object and placement slot. A state machine converts intent predictions into stable robot goals, enabling early motion while remaining stable under noisy predictions and corrective hand movements. AHEAD's intent prediction module achieves Top1 accuracy: 76% for grasp objects and 76% for target slots. Moreover, our user study shows AHEAD reduces robot reaction latency by 0.6 s (object) and 1.4 s (slot) relative to baselines. Participants also reported lower operator load, indicating faster robot responses while maintaining low operator effort in practice.

</details>

---

### [[20_Research/Papers/机器人/Assessing_Physical_Frailty_and_Fall-Risk_Indicators_with_Social_Robots_An_in_situ_Evaluation_with_Older_Adults|Assessing Physical Frailty and Fall-Risk Indicators with Social Robots: An in situ Evaluation with Older Adults]]

![[assets/2607.15156_figure.png|800]]

- **arXiv**: [2607.15156](https://arxiv.org/abs/2607.15156)
- **PDF**: https://arxiv.org/pdf/2607.15156
- **详细分析**: [[20_Research/Papers/机器人/Assessing_Physical_Frailty_and_Fall-Risk_Indicators_with_Social_Robots_An_in_situ_Evaluation_with_Older_Adults|Assessing Physical Frailty and Fall-Risk Indicators with Social Robots: An in situ Evaluation with Older Adults]]
- **作者**: Aniol Civit, Antonio Andriella, Alba Martínez, Joan Ars, Aida Ribera, Cristian Barrué, Guillem Alenyà
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Assessing Physical Frailty and Fall-Risk Indicators with Social Robots: An in situ Evaluation with Older Adults》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frailty assessments are crucial to evaluate the risk of adverse events and the health and social care needs of older adults, yet their administration remains resource-intensive and typically relies on coarse clinical outcomes, such as task completion times, which may overlook biomechanical indicators of functional decline. To address this, we present a robotic framework that guides older adults through standardised frailty and fall-risk tests while capturing clinical scores and additional frailty-related metrics, offering a deeper insight into a user's condition. The system uses a Behaviour Tree architecture that coordinates perception, decision-making, interaction, and measurement modules. Using vision-based skeleton tracking, the robot evaluates established clinical tests, including the Short Physical Performance Battery (SPPB) and the Timed Up and Go (TUG). The framework was co-designed with healthcare professionals and evaluated in situ during six months in a rehabilitation centre's research lab with N=81 older adults. Robot-derived measurements were compared against therapist assessments and clinical reference instruments, including a gait analysis walkway and an inertial measurement unit (IMU). Results showed excellent agreement for most test completion times and gait-related parameters ($ICC &gt; 0.9$). And, substantial agreement for the overall SPPB score comparing the robot and the therapist ($k = 0.67$) and moderate agreement comparing the robot and the IMU ($k=0.55$). The findings highlight that social robots can provide reliable and objective frailty assessments in healthcare settings while enabling the collection of relevant mobility indicators beyond conventional outcomes.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Agile_Navigation_in_Crowded_Environments_for_Quadruped_Robots|Learning Agile Navigation in Crowded Environments for Quadruped Robots]]

![[assets/2607.15036_figure.png|800]]

- **arXiv**: [2607.15036](https://arxiv.org/abs/2607.15036)
- **PDF**: https://arxiv.org/pdf/2607.15036
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Agile_Navigation_in_Crowded_Environments_for_Quadruped_Robots|Learning Agile Navigation in Crowded Environments for Quadruped Robots]]
- **作者**: Shuyu Wu, Zeyu Liu, Tianbao Zhang, Fanxing Li, Fangyu Sun, Mingkang Xiong, Wei Xi, Wenxian Yu, Danping Zou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Learning Agile Navigation in Crowded Environments for Quadruped Robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL, NavRL, VOP-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigating dynamic and crowded environments presents significant challenges for quadruped robots due to severe sensor occlusion and unpredictable human motion. Existing approaches face a trade-off: model-based methods, such as Velocity Obstacles (VO), theoretically guarantee safety but rely on accurate obstacle motion estimates that often fail in dense crowds, while end-to-end learning methods offer robustness but lack motion prediction capability of obstacles, leading to collisions or conservative behaviors. To solve this, we propose VOP-Nav, a novel navigation system that combines the geometric safety of VO with the agile adaptability of end-to-end learning. Using only local onboard observations, our system avoids explicit obstacle detection and tracking pipelines. The VOP-Net processes multi-frame LiDAR data to implicitly encode dynamic constraints and predict a safe velocity region derived from Velocity Obstacle theory. Importantly, the VO predictions serve a dual role: they are used as input to the navigation policy during inference and as a reward signal during training to encourage safe motion. Evaluations in Isaac Gym demonstrate that VOP-Nav achieves higher success rates than all baselines while balancing locomotion speed and collision avoidance. Real-world deployment on a Unitree Go2 quadruped robot further validates the system's robustness and efficiency in complex indoor and outdoor dynamic environments.

</details>

---

### [[20_Research/Papers/机器人/Risk-Aware_Belief_Control_Barrier_Functions_over_Random_Finite_Sets|Risk-Aware Belief Control Barrier Functions over Random Finite Sets]]

![[assets/2607.15016_figure.png|800]]

- **arXiv**: [2607.15016](https://arxiv.org/abs/2607.15016)
- **PDF**: https://arxiv.org/pdf/2607.15016
- **详细分析**: [[20_Research/Papers/机器人/Risk-Aware_Belief_Control_Barrier_Functions_over_Random_Finite_Sets|Risk-Aware Belief Control Barrier Functions over Random Finite Sets]]
- **作者**: Shaohang Han, Gang Chen, Yixi Cai, Ignacio Torroba, Ivan Stenius, Patric Jensfelt, Javier Alonso-Mora, Jana Tumova
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Risk-Aware Belief Control Barrier Functions over Random Finite Sets》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Ensuring robot safety in unknown, dynamic environments is a fundamental requirement. It involves inferring the states of an unknown and time-varying number of moving objects from noisy, incomplete measurements. We address safe control under the induced multi-object state uncertainty with a risk-aware belief control barrier function (BCBF) framework. The uncertainty is captured by a random finite set (RFS) belief, estimated by a sequential Monte Carlo probability hypothesis density (SMC-PHD) filter that represents it with a set of particles. Building directly on these particles, we construct a nonsmooth BCBF, establish forward invariance of the safe set under continuous prediction, and derive an explicit condition under which discrete updates preserve safety. Simulation and real-world underwater experiments demonstrate the effectiveness and efficiency of the proposed approach.

</details>

---

### [[20_Research/Papers/具身智能/CosFly-VLA_A_Spatially_Aware_Vision-Language-Action_Model_for_UAV_Tracking|CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking]]

![[assets/2607.15004_figure.png|800]]

- **arXiv**: [2607.15004](https://arxiv.org/abs/2607.15004)
- **PDF**: https://arxiv.org/pdf/2607.15004
- **详细分析**: [[20_Research/Papers/具身智能/CosFly-VLA_A_Spatially_Aware_Vision-Language-Action_Model_for_UAV_Tracking|CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking]]
- **作者**: Ruilong Ren, Songsheng Cheng, Yunpeng Zhou, Hanxuan Chen, Xiangyue Wang, Tianle Zeng, Shuai Yuan, Binbo Li, Hanzhong Guo, Ji Pei, Da Zhang, Kangli Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 4.0（加权：具身智能 2.7，强化学习 0.2，机器人 1.1）
- **关联关键词**: Multimodal, RL, Systems

#### 研究背景与动机

《CosFly-VLA: A Spatially Aware Vision-Language-Action Model for UAV Tracking》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AerialVLA, AirCopBench, CosFly-VLA, HRVQA, Open3DVQA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dynamic target tracking is essential for Unmanned Aerial Vehicles (UAVs) operating in complex urban environments, where both the target and the camera viewpoint change continuously. Existing Vision-Language-Action (VLA) policies can track visible targets effectively, but their performance often degrades when buildings, vegetation, or roadside objects block the line of sight. During sustained occlusion, a policy may lose the target state, execute actions toward an incorrect region, and amplify this error through subsequent observations until re-acquisition becomes impossible. To this end, we present CosFly-VLA, a spatially aware VLA model that jointly grounds the target, estimates its visibility, and generates continuous flight actions through a structured prediction interface. To train this policy, we use a large-scale recipe over diverse data sources. Spatially Grounded Continued Pretraining (CPT) on a 500k mixed pool injects UAV-view depth, distance, and 3-D spatial reasoning. A three-stage Curriculum-based Supervised Fine-Tuning (SFT) process then specializes the tracker through multi-head warm-up followed by two-stage curriculum learning over natural and hard / long-occlusion data. Chain-of-Thought (CoT) training subsequently teaches recovery-oriented reasoning traces before structured answers. Finally, a closed-loop Reinforcement Learning (RL) stage optimizes tracking behavior with a multi-component reward covering stand-off tracking, grounding quality, collision avoidance, and task success. Relative to OpenVLA, CosFly-VLA-0.8B reduces open-loop Average Displacement Error (ADE) by 34.1% on seen-test and 35.3% on unseen-test. Closed-loop optimization improves Success Rate (SR) by 29.8% and 2.5%, respectively. These results demonstrate progress from visible-frame imitation toward spatially grounded action-closed-loop control, evaluated under a shared oracle state history.

</details>

---

### [[20_Research/Papers/具身智能/AeroAct_Action-Centered_World-Action_Models_for_Language-Conditioned_Quadrotor_Flight|AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight]]

![[assets/2607.14997_figure.png|800]]

- **arXiv**: [2607.14997](https://arxiv.org/abs/2607.14997)
- **PDF**: https://arxiv.org/pdf/2607.14997
- **详细分析**: [[20_Research/Papers/具身智能/AeroAct_Action-Centered_World-Action_Models_for_Language-Conditioned_Quadrotor_Flight|AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight]]
- **作者**: Xinhong Zhang, Qiyuan Zhu, Yubo Huang, Haolin Chen, Runqing Wang, Yuhao Mo, Zhongxin Chen, Yu Hu, Xinjiang Wang, Jian Sun, Gang Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《AeroAct: Action-Centered World-Action Models for Language-Conditioned Quadrotor Flight》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GigaWorld, Real-World, UniSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Language-conditioned quadrotor flight requires a policy to ground semantic goals, anticipate the visual consequences of ego-motion, and output control references that remain smooth and dynamically executable under rapidly changing first-person views. Existing aerial vision-language navigation and vision-language-action methods commonly use discrete actions, high-level waypoints, or instantaneous velocity commands, which provide limited supervision about how flight actions change future observations. We present AeroAct, an action-centered world-action model (WAM) for quadrotor navigation. To the best of our knowledge, AeroAct is the first WAM instantiated and demonstrated for real-world aerial flight. The model adapts a pretrained video diffusion Transformer to predict local trajectory-action chunks from egocentric visual history, proprioception, and language. Future first-person frames are used during training as dense consequence supervision, while deployment directly decodes actions without generating future video. To obtain aligned visual, state, language, and dynamically feasible action data, we build a DiffAero-based pipeline with complementary Isaac Lab and 3D Gaussian splatting renderers. We further introduce a low-cost handheld collection device that couples camera observations with motion estimates to recreate flight-like egocentric trajectories, and a self-guidance procedure that improves temporal consistency across overlapping trajectory chunks. Closed-loop simulation and real-world experiments show that temporal visual context improves target tracking and object-search performance, and that WAM-based policies can be executed on a physical quadrotor.

</details>

---

### [[20_Research/Papers/机器人/Human-Robot_Interaction_in_GenAI_Architectures_via_the_Agent-Client_Protocol|Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol]]

![[assets/2607.14919_figure.png|800]]

- **arXiv**: [2607.14919](https://arxiv.org/abs/2607.14919)
- **PDF**: https://arxiv.org/pdf/2607.14919
- **详细分析**: [[20_Research/Papers/机器人/Human-Robot_Interaction_in_GenAI_Architectures_via_the_Agent-Client_Protocol|Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol]]
- **作者**: Jesus Moncada-Ramirez, Jose-Raul Ruiz-Sarmiento, Javier Gonzalez-Jimenez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.3，大模型 0.5，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Human-Robot Interaction in GenAI Architectures via the Agent-Client Protocol》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in Generative Artificial Intelligence (GenAI), particularly Large Language Models (LLMs), are driving robotic architectures toward agent-based high-level orchestration, in which natural-language instructions can be translated into context-aware action sequences. While the integration of these agents and robotic capabilities is increasingly converging toward standardization through the Model Context Protocol (MCP), the upper Human-Robot Interaction (HRI) layer remains fragmented by proprietary, ad hoc interfaces that hinder real-time human-in-the-loop collaboration. To address this fragmentation, this paper proposes the adoption of the Agent-Client Protocol (ACP) -- a communication standard originally introduced for coding agents in software engineering -- as a unified communication contract for the HRI layer in agent-based robotic systems. By combining ACP at the interface-agent link and MCP at the agent-execution link, we formulate a fully decoupled three-layer architecture that separates human interaction, deliberative orchestration, and physical execution. This topology removes rigid architectural dependencies, enabling heterogeneous user interfaces to connect to the same robotic system and allowing the underlying robotic platform to be replaced without requiring client-specific integration changes. Moreover, it provides native support for collaborative HRI capabilities such as real-time observability, explicit human authorization, and immediate task interruption. We experimentally evaluate the proposed architecture on a physical mobile robot, demonstrating interoperability across three heterogeneous user interfaces and validating real-time human-in-the-loop workflows with negligible latency overhead.

</details>

---

### [[20_Research/Papers/机器人/OASIS-Map_Object-Level_Change_Detection_in_Multi-Session_Mapping_using_Semantic_Correspondence_Matching|OASIS-Map: Object-Level Change Detection in Multi-Session Mapping using Semantic Correspondence Matching]]

![[assets/2607.14899_figure.png|800]]

- **arXiv**: [2607.14899](https://arxiv.org/abs/2607.14899)
- **PDF**: https://arxiv.org/pdf/2607.14899
- **详细分析**: [[20_Research/Papers/机器人/OASIS-Map_Object-Level_Change_Detection_in_Multi-Session_Mapping_using_Semantic_Correspondence_Matching|OASIS-Map: Object-Level Change Detection in Multi-Session Mapping using Semantic Correspondence Matching]]
- **作者**: Haedam Oh, Yifu Tao, Nived Chebrolu, Maurice Fallon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《OASIS-Map: Object-Level Change Detection in Multi-Session Mapping using Semantic Correspondence Matching》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Park2021ChangeSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Map representations which are consistent across repeated visits to a real-world semi-static environment are very useful for long-term robotic inspection. In such settings, the scene may evolve while the robot is absent, with objects appearing, disappearing, moving, or being replaced, quickly making a static map outdated. Existing change-detection methods reason through geometry, category-level semantics, or object persistence. However, achieving reliable object association across revisits remains a key challenge, especially under partial views, occlusion, and imperfect segmentation. In this work, we propose OASIS-Map, a multi-session mapping system that maintains a spatio-temporally consistent object-level map by establishing dense patch-level semantic correspondences between temporal observations. These correspondences detect where the scene has changed and incrementally associate objects across revisits as the robot re-observes the environment. We demonstrate OASIS-Map on three challenging real-world scenarios: object rearrangements in 3RScan, visually similar car replacements in a car park, and large-scale scene changes in an outdoor market. We achieve 0.783 F1 on change detection in a car replacement scenario in a car park and 0.667 F1 on moved object association in 3RScan. https://dynamic.robots.ox.ac.uk/projects/oasis-map/

</details>

---

### [[20_Research/Papers/具身智能/Modeling_and_Validation_of_Quality_of_Control_for_Edge-Offloaded_Collaborative_Navigation|Modeling and Validation of Quality of Control for Edge-Offloaded Collaborative Navigation]]

![[assets/2607.14853_figure.png|800]]

- **arXiv**: [2607.14853](https://arxiv.org/abs/2607.14853)
- **PDF**: https://arxiv.org/pdf/2607.14853
- **详细分析**: [[20_Research/Papers/具身智能/Modeling_and_Validation_of_Quality_of_Control_for_Edge-Offloaded_Collaborative_Navigation|Modeling and Validation of Quality of Control for Edge-Offloaded Collaborative Navigation]]
- **作者**: Neelabhro Roy, Mikael Hammarling, Victor Nan Fernandez-Ayala, Gourav Prateek Sharma, Mani H. Dhullipalla, Dimos V. Dimarogonas, James Gross
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Modeling and Validation of Quality of Control for Edge-Offloaded Collaborative Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collaborative control in complex environments is severely challenged by stochastic wireless delay and reliability variations, which can degrade navigation, tracking, and collision avoidance. These network-induced uncertainties complicate the maintenance of energy efficiency during collaborative tasks, and can potentially lead to over-provisioning of resources. In this paper, for a navigation setup with dynamic collision avoidance, we address this challenge by expanding the quality of control (QoC) framework from prior works to practical robotic models. Our approach (i) models end-to-end network effects on closed-loop performance, (ii) systematically explores the impact of various control parameters dictating robotic motion on network latency-reliability (iii) validates these models through experiments on a private 5G testbed across varying delay, reliability and control configurations. Our analysis indicates the optimal control-communication co-design operating regimes for practical robots and also compares the QoC performance of standard ROS~2 quality of service (QoS) policies under real-world conditions and showing how RELIABLE QoS offers 51.5% better QoC than BEST-EFFORT under certain experimental settings.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Human-like_Physical_Intelligence_LifelongVision-Language-Action_Learning_for_Robotic_Manipulation|Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation]]

![[assets/2607.14852_figure.png|800]]

- **arXiv**: [2607.14852](https://arxiv.org/abs/2607.14852)
- **PDF**: https://arxiv.org/pdf/2607.14852
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Human-like_Physical_Intelligence_LifelongVision-Language-Action_Learning_for_Robotic_Manipulation|Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation]]
- **作者**: Yao He, Gan Sun, Wenqi Liang, Fazeng Li, Yang Cong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Towards Human-like Physical Intelligence: LifelongVision-Language-Action Learning for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LifelongVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Similar to the natural capabilities of humans to sequentially learn new tasks, robots with Vision-Language-Action (VLA) models should possess lifelong learning ability to learn a new task when deployed in open-world environments. However, most recently proposed lifelong learning models aim to effectively learn the current task (plasticity) or maintain high accuracy on previous tasks (stability), while the plasticity-stability trade-off remains largely unsolved in robotic manipulation models. To address this fundamental challenge, we propose a cache-efficient lifelong Vision-Language-Action learning framework for robotic manipulation (i.e., LifelongVLA), which alleviates the plasticity-stability trade-off with a dual-timescale adaptation mechanism while achieving low-cost robotic deployment with a cache-efficient replay strategy. More concretely, we propose a dual-timescale LoRA gating module to decompose VLA adaptation into two lightweight pathways: a short-term adapter for plasticity and a long-term adapter for stable consolidation. These pathways are integrated via a task-aware gate, enabling explicit control of the plasticity-stability trade-off. In the skill replay phase, a cache-efficient stochastic replay strategy is proposed to preserve more balanced retention signals without full-trajectory storage. Finally, experiments show that LifelongVLA outperforms existing baselines, demonstrating efficient skill expansion, robust retention of learned manipulation behaviors, and reduced reliance on retraining for real-world deployment on an xArm robot.

</details>

---

### [[20_Research/Papers/机器人/KineFuse_Kinematic-Aware_Haptic_Fusion_for_In-Hand_Occluded-Object_Pose_Tracking|KineFuse: Kinematic-Aware Haptic Fusion for In-Hand Occluded-Object Pose Tracking]]

![[assets/2607.14842_figure.png|800]]

- **arXiv**: [2607.14842](https://arxiv.org/abs/2607.14842)
- **PDF**: https://arxiv.org/pdf/2607.14842
- **详细分析**: [[20_Research/Papers/机器人/KineFuse_Kinematic-Aware_Haptic_Fusion_for_In-Hand_Occluded-Object_Pose_Tracking|KineFuse: Kinematic-Aware Haptic Fusion for In-Hand Occluded-Object Pose Tracking]]
- **作者**: Chanyoung Ahn, Jaesung Lee, Sungwoo Park, Donghyun Hwang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《KineFuse: Kinematic-Aware Haptic Fusion for In-Hand Occluded-Object Pose Tracking》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous in-hand manipulation requires continuous 6D pose tracking, yet the manipulating fingers inevitably occlude the object from the camera. We study how to structure the sparse haptic signals already available on multi-fingered hands, including proprioception, proximal force/torque, and binary contact, to complement a pretrained visual pose tracker under occlusion. We propose a kinematic-aware finger-level encoder and systematically compare it against four alternative designs through three levels of evaluation: per-frame refinement, sequential open-loop tracking, and closed-loop manipulation. Our experiments reveal that (i) per-frame evaluation cannot distinguish encoder quality, while sequential tracking amplifies architectural differences by up to 15 times; (ii) the structured encoder learns task-specific cross-modal gating, using vision exclusively for translation and dedicating one attention head to haptics for rotation, without explicit supervision; and (iii) compact finger-level tokenization with 4 tokens outperforms both flat fusion and joint-level representations, which suppress vision through norm dominance. We validate that improved tracking yields higher success in a downstream reorientation task and provide qualitative real-world demonstrations. Our project page is available at https://cold-young.github.io/kine-fuse/.

</details>

---

### [[20_Research/Papers/机器人/Curvature-Constrained_and_Constant-Speed_Distributed_Simultaneous_Arrival_Control_for_Multi-Robot_Systems|Curvature-Constrained and Constant-Speed Distributed Simultaneous Arrival Control for Multi-Robot Systems]]

![[assets/2607.14781_figure.png|800]]

- **arXiv**: [2607.14781](https://arxiv.org/abs/2607.14781)
- **PDF**: https://arxiv.org/pdf/2607.14781
- **详细分析**: [[20_Research/Papers/机器人/Curvature-Constrained_and_Constant-Speed_Distributed_Simultaneous_Arrival_Control_for_Multi-Robot_Systems|Curvature-Constrained and Constant-Speed Distributed Simultaneous Arrival Control for Multi-Robot Systems]]
- **作者**: Zhouru Xiao, Yang Lu, Weijia Yao, Min Liu, Yaonan Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Curvature-Constrained and Constant-Speed Distributed Simultaneous Arrival Control for Multi-Robot Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The simultaneous arrival of multiple mobile robots at a target point is crucial for cooperation tasks such as cooperative encirclement, disaster relief, and environmental monitoring. Although the simultaneous arrival problem itself is already complex, the problem becomes more challenging when there are constraints on the robot trajectory curvatures and the speeds are required to be constant (possibly different for different robots), and the control law for robots needs to be distributed. These constraints are typical for a multi-robot system consisting of, e.g., fixed-wing UAVs. To address this challenge, this paper proposes a distributed switching control method based on the maximum consensus protocol. By exploiting the geometric properties of Dubins paths along with optimization principles, a virtual time variable is introduced, and a hybrid control law that combines optimal control with saturated proportional control is designed. Under the proposed control law, each robot is driven to approach the maximum virtual time among its neighbors, thereby achieving simultaneous arrival under some mild conditions. Furthermore, we prove that in certain cases the proposed method attains a theoretically optimal arrival time. The approach is scalable and real-time, with low communication overhead. Its effectiveness and robustness are validated through extensive simulations and experiments.

</details>

---

### [[20_Research/Papers/具身智能/Hybrid_Rigid-Soft_Robotic_Gripper_with_Shape_Adaptation,_Uniform_Force_Distribution,_and_Self-Locking_Capabilities|Hybrid Rigid-Soft Robotic Gripper with Shape Adaptation, Uniform Force Distribution, and Self-Locking Capabilities]]

![[assets/2607.14730_figure.png|800]]

- **arXiv**: [2607.14730](https://arxiv.org/abs/2607.14730)
- **PDF**: https://arxiv.org/pdf/2607.14730
- **详细分析**: [[20_Research/Papers/具身智能/Hybrid_Rigid-Soft_Robotic_Gripper_with_Shape_Adaptation,_Uniform_Force_Distribution,_and_Self-Locking_Capabilities|Hybrid Rigid-Soft Robotic Gripper with Shape Adaptation, Uniform Force Distribution, and Self-Locking Capabilities]]
- **作者**: Xi Chen, Yun Wang, Lichao Yang, Haitao Li, Ya Xiong
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Hybrid Rigid-Soft Robotic Gripper with Shape Adaptation, Uniform Force Distribution, and Self-Locking Capabilities》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventional robotic grippers face a significant challenge in agricultural automation: the trade-off between compliant, adaptive grasping, pressure balancing among all joints, and high load capacity, often at the cost of high energy consumption. This paper presents a novel hybrid rigid-soft gripper that integrated low-cost, membrane-based pneumatic actuators with 3D-printed dual ratchet-pawl mechanisms to simultaneously achieve shape adaptation, uniform force distribution, and energy-free self-locking. The dual-ratchet structure assembled in an offset configuration significantly increased the angular resolution of the joint locking mechanism. Key experimental results demonstrated the gripper's superior performance: a remarkable maximum load capacity of 4200 g, far exceeding that of conventional soft grippers (45-210 g); more uniform force distribution across object sizes (1.75-35.29% difference ratio) compared to a rigid gripper (56.77-66.44%), with peak contact forces remaining below surface damage thresholds; and a 50.05% reduction in total energy consumption to 42.6 J per grasp cycle, achieved by eliminating the need for continuous pneumatic pressure through the self-locking mechanism, compared to 85.28 J for a conventional soft gripper. The combination of additive manufacturing for ratchets and commercially available materials for pneumatic chambers ensured a low-cost and easily fabricated design. These findings validated that the proposed gripper successfully bridged the gap between soft compliance and rigid reliability, offering a robust and efficient solution for scalable agricultural harvesting and manipulation tasks.

</details>

---

### [[20_Research/Papers/机器人/BridgeFlow_Fast_and_Robust_SE(2)-Equivariant_Motion_Planning_with_Flow_Matching|BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching]]

![[assets/2607.14725_figure.png|800]]

- **arXiv**: [2607.14725](https://arxiv.org/abs/2607.14725)
- **PDF**: https://arxiv.org/pdf/2607.14725
- **详细分析**: [[20_Research/Papers/机器人/BridgeFlow_Fast_and_Robust_SE(2)-Equivariant_Motion_Planning_with_Flow_Matching|BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching]]
- **作者**: Xinzhe Zhou, Xuyang Wang, Xiaoming Duan, Jianping He
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《BridgeFlow: Fast and Robust SE(2)-Equivariant Motion Planning with Flow Matching》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In robotic motion planning, equivariance to rigid body transformations is crucial for robust spatial generalization. However, current learning-based planners face a critical dilemma: they either lack inherent equivariance, treating transformed tasks as novel scenarios, or enforce it via computationally expensive specialized architectures that bottleneck real-time inference. To break this trade-off, we propose BridgeFlow, a fast and strictly SE(2)-equivariant generative motion planning framework. Rather than relying on heavy equivariant networks, BridgeFlow achieves exact spatial equivariance via a lightweight task-centric canonicalization module, enabling generalization using standard architectures. To further accelerate inference, we pair a Brownian bridge informative prior with context-aware mini-batch optimal transport. This constructs a straightened vector field that minimizes transport costs and stabilizes training. Furthermore, environmental awareness is explicitly embedded via Classifier-Free Guidance. Evaluations in dense 2D environments and on a 7-DoF Franka manipulator demonstrate that BridgeFlow achieves up to a 15x inference speedup and a 2x higher valid trajectory rate over state-of-the-art diffusion baselines, alongside robust generalization to entirely unseen environments and arbitrary spatial transformations.

</details>

---

### [[20_Research/Papers/强化学习/Reinforcement_Learning_for_the_Full_Strawberry_Harvesting_Process_Obstacle_Separation,_Detachment,_and_Placement|Reinforcement Learning for the Full Strawberry Harvesting Process: Obstacle Separation, Detachment, and Placement]]

![[assets/2607.14708_figure.png|800]]

- **arXiv**: [2607.14708](https://arxiv.org/abs/2607.14708)
- **PDF**: https://arxiv.org/pdf/2607.14708
- **详细分析**: [[20_Research/Papers/强化学习/Reinforcement_Learning_for_the_Full_Strawberry_Harvesting_Process_Obstacle_Separation,_Detachment,_and_Placement|Reinforcement Learning for the Full Strawberry Harvesting Process: Obstacle Separation, Detachment, and Placement]]
- **作者**: Changyou Miao, Teng Li, Ya Xiong
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 0.6，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Reinforcement Learning for the Full Strawberry Harvesting Process: Obstacle Separation, Detachment, and Placement》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：FruitGym, Real-World, RetinexNet, SRR-Net, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Severe occlusions and deformable plant structures introduce complex contact dynamics that challenge robotic strawberry harvesting. A policy-driven reinforcement learning (RL) framework with heuristic phase coordination was developed, in which obstacle separation, fruit detachment, and placement were formulated as a sequential decision-making task. A shared interaction-aware policy generated Cartesian motions across all task phases, while lightweight heuristic logic coordinated task progression and gripper events. A shared structured observation space was used to represent target, obstacle, end-effector, and task-context information. A hierarchical architecture combined the high-level policy with low-level Cartesian impedance control for compliant interaction. To support zero-shot sim-to-real transfer, feasibility-first observation alignment and domain randomization were adopted. The policy achieved success rates of 89.7% in simulation and 82.0% in real-world experiments. As the occlusion level increased from 1 to 5, the average execution time increased from 12.99 s to 21.73 s, reflecting greater interaction complexity. These results demonstrated effective transfer of interaction-aware harvesting behaviors to a structurally different robotic platform.

</details>

---

### [[20_Research/Papers/具身智能/Lights,_Camera,_Malfunction_When_Illumination_Robustness_Leaves_VLA_Models_Blind_to_Color|Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color]]

![[assets/2607.14698_figure.png|800]]

- **arXiv**: [2607.14698](https://arxiv.org/abs/2607.14698)
- **PDF**: https://arxiv.org/pdf/2607.14698
- **详细分析**: [[20_Research/Papers/具身智能/Lights,_Camera,_Malfunction_When_Illumination_Robustness_Leaves_VLA_Models_Blind_to_Color|Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color]]
- **作者**: Marino Watanabe, Takami Sato, Kentaro Yoshioka
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 2.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, Security

#### 研究背景与动机

《Lights, Camera, Malfunction: When Illumination Robustness Leaves VLA Models Blind to Color》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have emerged as a powerful paradigm for general-purpose robot manipulation; however, their transition to real-world environments reveals vulnerabilities to minor environmental perturbations. We propose FLARE, an optimized physical spotlight attack framework that exploits these vulnerabilities via targeted illuminations, dropping baseline task success rates to zero without any access to model internals. While adversarial training is the standard countermeasure, we identify a critical and previously underestimated defensive pitfall: naive data augmentations incorrectly condition VLA models to discard color as noise, collapsing their visual perception into a purely shape-biased processor. We expose this degradation through a diagnostic grayscale evaluation, in which the defended model maintains high success rates on grayscale inputs, while its success rate on benign, color-dependent real-world tasks drops to at most 47.5%, well below the undefended baseline. To address this, we propose ChromaGuard, a chroma-preserving adversarial training method. On a physical 6-DoF robotic platform, we demonstrate that ChromaGuard achieves 97.5% and 92.5% success rates in benign and attacked color-dependent tasks, respectively.

</details>

---

### [[20_Research/Papers/具身智能/Reflex_Real-Time_VLA_Control_through_Streaming_Inference|Reflex: Real-Time VLA Control through Streaming Inference]]

![[assets/2607.14695_figure.png|800]]

- **arXiv**: [2607.14695](https://arxiv.org/abs/2607.14695)
- **PDF**: https://arxiv.org/pdf/2607.14695
- **详细分析**: [[20_Research/Papers/具身智能/Reflex_Real-Time_VLA_Control_through_Streaming_Inference|Reflex: Real-Time VLA Control through Streaming Inference]]
- **作者**: Yuanchun Guo, Bingyan Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Reflex: Real-Time VLA Control through Streaming Inference》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching, forcing a choice between slow $O(N^2)$ re-computation or mathematically incorrect cache reuse. We present \textbf{Reflex}, a framework that enables \textit{real-time streaming inference} for flow matching policies by exploiting the \textit{Timestep-Invariance Property} -- that perception encoders are functionally independent of the denoising loop. Reflex partitions the attention context into static, sliding, and dynamic regions, enabling $O(1)$ incremental cache updates while preserving full-batch-equivalent attention outputs for fixed inputs. To ensure stability under continuous high-frequency inference, we introduce \textit{AdaRMSNorm}, an adaptive normalization layer that prevents BFloat16 numerical collapse by gating on flow phase. We further maximize throughput through an \textit{async pipeline} that decouples visual encoding from action generation, combined with \textit{operator fusion} that reduces kernel overhead. On LIBERO and Kinetix benchmarks, Reflex achieves a 2.58$\times$ inference speedup and 50Hz stable streaming, reducing reaction latency by up to 54\% and enabling efficient deployment without performance degradation.

</details>

---

### [[20_Research/Papers/具身智能/NavCMPO_Critic-Guided_MeanFlow_Policy_Optimization_for_Adaptive_Navigation|NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation]]

![[assets/2607.14643_figure.png|800]]

- **arXiv**: [2607.14643](https://arxiv.org/abs/2607.14643)
- **PDF**: https://arxiv.org/pdf/2607.14643
- **详细分析**: [[20_Research/Papers/具身智能/NavCMPO_Critic-Guided_MeanFlow_Policy_Optimization_for_Adaptive_Navigation|NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation]]
- **作者**: Junjie An, Yi Wu, Xiao Liu, Yiqun Zhou, Yuechen Wu, Xiaoqing Guan, You Wang, Guang Li
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 0.6，强化学习 1，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《NavCMPO: Critic-Guided MeanFlow Policy Optimization for Adaptive Navigation》归入 强化学习、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：InternVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end diffusion-based policies have demonstrated strong performance in mapless visual navigation, but their iterative denoising process introduces substantial inference latency, while behavior cloning limits performance to the quality of expert demonstrations. We present NavCMPO, a two-stage adaptive navigation framework that combines few-step MeanFlow trajectory generation, critic-guided refinement, and reinforcement learning fine-tuning. During pre-training, an obstacle proximity prediction task encourages the visual representation to capture obstacle-aware spatial information. To compensate for the degradation in obstacle avoidance caused by few-step generation, Critic-Guided Trajectory Refinement (CGTR) uses gradients from a critic trained with obstacle-point-cloud supervision to refine intermediate trajectories. During adaptation, the MeanFlow policy is fine-tuned using Proximal Policy Optimization with behavior-cloning regularization, while the critic is updated to accommodate embodiment-specific observation changes. Under a matched training budget on the InternVLA-N1 benchmark, NavCMPO achieves an average success rate of 74.7\%, exceeding the retrained NavDP baseline by 6.4 percentage points, while reducing inference latency from 85\,ms to 60\,ms. Experiments on a Unitree Go2 further demonstrate effective sim-to-real transfer.

</details>

---

### [[20_Research/Papers/具身智能/Representation-Aligned_Tactile_Grounding_for_Contact-Rich_Robotic_Manipulation|Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation]]

![[assets/2607.14609_figure.png|800]]

- **arXiv**: [2607.14609](https://arxiv.org/abs/2607.14609)
- **PDF**: https://arxiv.org/pdf/2607.14609
- **详细分析**: [[20_Research/Papers/具身智能/Representation-Aligned_Tactile_Grounding_for_Contact-Rich_Robotic_Manipulation|Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation]]
- **作者**: Ruilin Chen, Jingkai Jia, Tong Yang, Xinyu Zhou, Qiao Sun, Jiangwei Zhong, Shizeng Zhang, Nuo Chen, Bailin He, Wei Li, Wenqiang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Representation-Aligned Tactile Grounding for Contact-Rich Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile-enhanced vision-language-action (VLA) policies have been introduced for contact-rich manipulation, where critical interaction states are often hidden from vision. Future tactile prediction is a promising way to use touch because it turns tactile outcomes into supervision for action-induced contact dynamics. Yet VLA policies contain representations with different roles, from perceptual encoding to motor prediction, making it unclear where this supervision should be applied. We study this as a representation-alignment problem. Through a linear probe analysis, we find that future tactile states are most predictable from intermediate action-expert features, rather than from vision-language features or final action states. Motivated by this observation, we introduce a lightweight Latent Tactile Predictor (LTP), which predicts compact future tactile embeddings from the identified intermediate representation. By avoiding direct prediction of noisy raw tactile signals, LTP provides an action-outcome grounding signal that aligns intermediate action representations with future contact consequences. Experiments on real-world contact-rich manipulation tasks show that representation-aligned tactile grounding outperforms less aligned or multi-interface tactile prediction, highlighting the importance of where tactile supervision is applied.

</details>

---

### [[20_Research/Papers/具身智能/SoftNav_Injecting_3D_Scene_Tokens_into_VLMs_for_Embodied_Navigation|SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation]]

![[assets/2607.14586_figure.png|800]]

- **arXiv**: [2607.14586](https://arxiv.org/abs/2607.14586)
- **PDF**: https://arxiv.org/pdf/2607.14586
- **详细分析**: [[20_Research/Papers/具身智能/SoftNav_Injecting_3D_Scene_Tokens_into_VLMs_for_Embodied_Navigation|SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation]]
- **作者**: Yi Wu, Junjie An, Xiao Liu, Yiqun Zhou, Yuechen Wu, Xiaoqing Guan, Shuyang Yu, You Wang, Guang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.5，大模型 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《SoftNav: Injecting 3D Scene Tokens into VLMs for Embodied Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GOAT-Bench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In goal-directed embodied navigation, where an agent must locate a specified target in an unseen environment, 3D scene understanding and navigation reasoning must work in concert. Current approaches transmit 3D scene information to vision-language models (VLMs) through text, suggesting a representation gap in our tested configurations; a controlled ablation confirms that direct embedding-level transfer significantly outperforms the evaluated text serialization formats. We introduce SoftNav, which injects entity-level 3D continuous representations -- one token per detected object or frontier -- into a VLM's hidden space as soft tokens through a lightweight projector. With the 3D encoder and VLM frozen, only ~1,200 samples and ~17M trainable parameters are needed. On HM3D-OVON, SoftNav achieves 74.2%/68.3%/66.7% SR across three splits, surpassing all prior methods in both SR and SPL; the same navigation policy transfers zero-shot to GOAT-Bench (67.2% SR), SG3D (47.2% s-SR), and real-world robot deployment without retraining or architectural modification. Injecting 3D scene tokens directly into VLMs bridges the representation gap, enabling transferable navigation with minimal training.

</details>

---

### [[20_Research/Papers/机器人/Communication-Efficient_Relative_Pose_Estimation_with_Vision_Foundation_Models_for_Ephemeral_Collaborative_Perception|Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception]]

![[assets/2607.14539_figure.jpg|800]]

- **arXiv**: [2607.14539](https://arxiv.org/abs/2607.14539)
- **PDF**: https://arxiv.org/pdf/2607.14539
- **详细分析**: [[20_Research/Papers/机器人/Communication-Efficient_Relative_Pose_Estimation_with_Vision_Foundation_Models_for_Ephemeral_Collaborative_Perception|Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception]]
- **作者**: Qihang Li, Jo-Hao Huang, Jiewen Liu, Suyoung Kang, Hao Zhang, Peng Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Communication-Efficient Relative Pose Estimation with Vision Foundation Models for Ephemeral Collaborative Perception》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Relative pose estimation is a fundamental capability for collaborative perception and coordination in multi-robot systems. However, robots encountering each other in real-world environments often operate in short interaction windows and must operate under limited communication bandwidth with intermittent or missing visual overlap caused by occlusions or limited fields of view. Existing approaches typically rely on global reference frames, assume sustained view overlap, or incur prohibitive communication costs, thereby limiting their applicability to ephemeral collaborative perception. To address these challenges, we introduce communication-efficient relative pose estimation (CERPE), a system-level framework that coordinates vision foundation models to jointly estimate ego-motion and inter-robot relative pose. CERPE reduces unnecessary raw-observation exchange by using continuously shared fixed-size descriptors to gate event-triggered raw-image requests independently of pose estimation. Non-overlapping encounters are handled by propagating inter-robot relative poses through metrically scaled ego-motion, thus maintaining relative pose estimates even in the absence of visual overlap. Experiments in simulation and real-world robots show that CERPE improves 6-DoF relative pose estimation over selected baselines in ephemeral collaborative perception.

</details>

---

### [[20_Research/Papers/具身智能/DRIFT_Drift_and_Aggregation_for_Motion_Planning|DRIFT: Drift and Aggregation for Motion Planning]]

![[assets/2607.14507_figure.png|800]]

- **arXiv**: [2607.14507](https://arxiv.org/abs/2607.14507)
- **PDF**: https://arxiv.org/pdf/2607.14507
- **详细分析**: [[20_Research/Papers/具身智能/DRIFT_Drift_and_Aggregation_for_Motion_Planning|DRIFT: Drift and Aggregation for Motion Planning]]
- **作者**: Yining Xing, Zhiyuan Liu, Zehong Ke, Wenhao Yu, Jianqiang Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《DRIFT: Drift and Aggregation for Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end trajectory planners need to represent multiple plausible driving behaviors while producing a single executable trajectory under real-time constraints. Proposal-based approaches address this ambiguity by generating multiple candidates, but converting the proposal set into a final plan remains a key design problem. We present DRIFT, a fixed-depth planner that combines one-step drifting in a compact trajectory latent space with scene-aware proposal aggregation. Conditioned on features from a pretrained visual encoder, the DRIFT Decoder generates 48 proposal features in a single batched pass, with 32 samples at alpha=0.5 and 16 samples at alpha=0.9. A lightweight Aggregation Head integrates these features with scene, navigation, and ego-state information and directly predicts the final trajectory without requiring trajectory-level quality labels for aggregation. Its output is trained with expert-trajectory imitation and a map-derived boundary regularizer that penalizes waypoints outside the drivable polygon and inside waypoints near its boundary. On NAVSIM navtest, DRIFT achieves 89.6 PDMS and 90.4 EPDMS, with strong drivable-area compliance and ego progress among the methods compared. The proposal-generation and aggregation module runs in 10.82 ms on an NVIDIA RTX 4090, while full-model inference including the visual backbone takes 66.43 ms. These results show that one-step latent proposal generation and direct aggregation provide an efficient design for multi-hypothesis motion planning.

</details>

---

### [[20_Research/Papers/强化学习/Safe_Execution_of_RL_Policies_Via_Acceleration-Based_CBF-QP_Constraint_Enforcement_for_Real-World_Robotic_Deployments|Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments]]

![[assets/2607.14488_figure.png|800]]

- **arXiv**: [2607.14488](https://arxiv.org/abs/2607.14488)
- **PDF**: https://arxiv.org/pdf/2607.14488
- **详细分析**: [[20_Research/Papers/强化学习/Safe_Execution_of_RL_Policies_Via_Acceleration-Based_CBF-QP_Constraint_Enforcement_for_Real-World_Robotic_Deployments|Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments]]
- **作者**: Bastien Muraccioli, Alice Cariou, Pierre-Alexandre Leziart, Mathieu Celerier, Arnaud Demont, Gentiane Venture, Mehdi Benallegue
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.1（加权：具身智能 0.6，强化学习 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Safe Execution of RL Policies Via Acceleration-Based CBF-QP Constraint Enforcement for Real-World Robotic Deployments》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：JRL, Real-World, Safe-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement Learning (RL) has demonstrated remarkable capabilities for solving complex robotic control problems, but its lack of safety guarantees severely limits deployment on hardware. In particular, as legged robots and manipulators often operate near safety-critical boundaries, out-of-distribution states can lead to failure upon deployment. To address this, we introduce Acc-CBF-QP, an acceleration-based Quadratic Program (QP) safety filter using Control Barrier Functions (CBFs) that constrains any RL policy onto a safe set at runtime without modifying training. The method applies to unconstrained and Safe-RL policies, and enforces joint position, velocity, torque, and collision constraints within a unified optimization framework. A key contribution is the formulation of RL+QP tasks that regulate deviation from the RL command when constraints would otherwise be violated. We introduce a TorqueTask, minimizing torque deviation, and a Forward Dynamics Task, minimizing induced acceleration deviation, thus providing principled control over safety-performance trade-offs. Experiments on a 7-DoF Kinova Gen3 manipulator and a 19-DoF Unitree H1 humanoid, both in simulation and on hardware, highlight substantial reductions in constraint violations. On the real H1 hardware, a Safe-RL policy alone yielded 10.04 violations/s, which were reduced by 92% to 0.80 violations/s when augmented with Acc-CBF-QP. On the Kinova Gen3, Acc-CBF-QP fully eliminated violations. Nominal task performance of the RL objective is preserved in violation-free regimes. Under aggressive velocity commands on H1, Acc-CBF-QP improves execution by preventing constraint-induced shutdowns, yielding longer survival times. The full pipeline is open-source.

</details>

---

### [[20_Research/Papers/机器人/MIDAS_Hand_Modular_low-Impedance_Direct-drive_Anthropomorphic_Sensing_Hand|MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand]]

![[assets/2607.14487_figure.png|800]]

- **arXiv**: [2607.14487](https://arxiv.org/abs/2607.14487)
- **PDF**: https://arxiv.org/pdf/2607.14487
- **详细分析**: [[20_Research/Papers/机器人/MIDAS_Hand_Modular_low-Impedance_Direct-drive_Anthropomorphic_Sensing_Hand|MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand]]
- **作者**: Alvin Zhu, Mingzhang Zhu, Beom Jun Kim, Quanyou Wang, Jose Victor S. H. Ramos, Dennis Hong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《MIDAS Hand: Modular low-Impedance Direct-drive Anthropomorphic Sensing Hand》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous manipulation is limited not only by algorithms but by a shortage of accessible hand hardware that combines human-scale morphology, ease of manufacturing or maintenance, tactile sensing, and practical cost. Existing dexterous hands tend to optimize some of these properties at the expense of others. We present MIDAS Hand, a low-cost, open-source, human-scale dexterous hand with integrated tactile sensing for manipulation research. MIDAS Hand provides 16 total degrees of freedom (DoF) with 13 active DoF, directly driven actuation with measurably low backdrive torque, and 283 three-axis tactile taxels in a compact 700 g package with a bill of materials under 3,000 USD. Built from 3D-printed components, it assembles in under three hours while providing the strength, repeatability, and maintainability needed for repeated real-world experiments. Alongside the hardware, we release a full stack: design files, build documentation, control and tactile Python APIs, simulation models, and retargeting and teleoperation pipelines. We characterize MIDAS Hand through workspace and grasp-taxonomy analysis, payload and reliability tests, backdrivability measurements, and teleoperation demonstrations with tactile sensing, showing that it offers a balanced, reproducible platform for tactile dexterous manipulation and human-to-robot data collection. Project page: https://midas-hand.com

</details>

---

### [[20_Research/Papers/机器人/Mixed-Agent_Museum_Tour_Guide_Design_Improves_Gendered_Learning_Outcomes_and_Visitor_Preferences|Mixed-Agent Museum Tour Guide Design Improves Gendered Learning Outcomes and Visitor Preferences]]

![[assets/2607.14468_figure.png|800]]

- **arXiv**: [2607.14468](https://arxiv.org/abs/2607.14468)
- **PDF**: https://arxiv.org/pdf/2607.14468
- **详细分析**: [[20_Research/Papers/机器人/Mixed-Agent_Museum_Tour_Guide_Design_Improves_Gendered_Learning_Outcomes_and_Visitor_Preferences|Mixed-Agent Museum Tour Guide Design Improves Gendered Learning Outcomes and Visitor Preferences]]
- **作者**: Annette M. Masterson, Wonse Jo, Helena C. Sieh, Lionel P. Robert,, Dawn Tilbury
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Mixed-Agent Museum Tour Guide Design Improves Gendered Learning Outcomes and Visitor Preferences》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots are increasingly integrated into everyday contexts, including museums, where they can both entertain and educate visitors. To enhance visitor experience and engagement, we present a novel mixed-agent tour guide system that combines a physical robot with a projected virtual agent that actively participates in the tour through conversation and interaction, achieving the interaction richness of two mobile agents from a single platform. We validate the system through a within-subjects study with 30 participants to assess engagement, quality of experience, and learning performance. Participants experienced different conversational styles and agent configurations, and data were collected via surveys, behavioral sensors, and interviews. Results showed that engagement and quality of experience remained consistent across conditions. Learning performance revealed a significant gender-moderated difference: the mixed-agent conditions improved learning performance for female participants. This suggests that the proposed dyadic conversational style in this paper influenced learning performance differently by gender. Nonetheless, in interviews, participants reported a greater preference for mixed-agent teams regardless of gender, citing interaction as a key factor in their experience.

</details>

---

### [[20_Research/Papers/机器人/Motion_Planning_with_Model-Based_Diffusion_via_Constraint_Optimization_and_Adaptive_Scheduling|Motion Planning with Model-Based Diffusion via Constraint Optimization and Adaptive Scheduling]]

![[assets/2607.14455_figure.png|800]]

- **arXiv**: [2607.14455](https://arxiv.org/abs/2607.14455)
- **PDF**: https://arxiv.org/pdf/2607.14455
- **详细分析**: [[20_Research/Papers/机器人/Motion_Planning_with_Model-Based_Diffusion_via_Constraint_Optimization_and_Adaptive_Scheduling|Motion Planning with Model-Based Diffusion via Constraint Optimization and Adaptive Scheduling]]
- **作者**: Zhilin He, Bowei Li, Jianlin Dou, Yuner Zhang, Changliu Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Motion Planning with Model-Based Diffusion via Constraint Optimization and Adaptive Scheduling》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Single-Robot Motion Planning (SRMP) in highly non-convex constrained environments, where robots must satisfy collision-free guarantees, dynamic feasibility, and task-related constraints, is challenging under complex constraints and computational limits. Recent Model-Based Diffusion (MBD) approaches recast the SRMP as trajectory optimization that samples from a posterior over trajectories, using known dynamics, and analytically estimates the score function from rollout samples to guide diffusion denoising toward a low-cost, clean trajectory without demonstration learning. While existing works further adapt MBD to constrained environments and showcase promising performance, they are still limited by (1) enforcing safety either via soft feasibility diffusion priors or hard projection operators, but lack a unified framework to integrate both, and (2) fixing safety enforcement to neglect the changing of diffusion scheduling. Therefore, we introduce Model-Based Diffusion via Constraint Optimization and Adaptive Scheduling (MD-COAS) for SRMP that unifies the inexact Augmented Lagrangian Method (iALM) soft diffusion prior with a Convex Feasible Set (CFS)-based hard projection operator, and adaptively schedules and co-optimizes safety enforcement, along with diffusion scheduling. Experiments demonstrate that our method achieves higher safety \&amp; success rates, faster convergence, and lower final costs than baseline planners on randomly generated highly non-convex 2D benchmarks and a 7-DoF robot arm avoidance task.

</details>

---

### [[20_Research/Papers/机器人/Stochastic_Filtering_for_Quorum_Sensing_in_Robot_Swarms_under_Anonymous_Communication|Stochastic Filtering for Quorum Sensing in Robot Swarms under Anonymous Communication]]

![[assets/2607.14262_figure.png|800]]

- **arXiv**: [2607.14262](https://arxiv.org/abs/2607.14262)
- **PDF**: https://arxiv.org/pdf/2607.14262
- **详细分析**: [[20_Research/Papers/机器人/Stochastic_Filtering_for_Quorum_Sensing_in_Robot_Swarms_under_Anonymous_Communication|Stochastic Filtering for Quorum Sensing in Robot Swarms under Anonymous Communication]]
- **作者**: Fabio Oddi, Andreagiovanni Reina, Vito Trianni
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Stochastic Filtering for Quorum Sensing in Robot Swarms under Anonymous Communication》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quorum Sensing (QS) is a key capability for robot swarms, useful for coordination of activities at the group level. Effective communication is instrumental for individuals to estimate the quorum level of the entire swarm. Anonymous communication protocols where individuals exchange local information without revealing unique identities are helpful to support quorum estimates by sampling information from neighbours and maintain scalability of the QS process. However, because anonymous protocols cannot distinguish message sources, repeated messages from the same sender may be double-counted, thereby biasing collective quorum estimates. In this study, we introduce a stochastic filtering protocol inspired by $k$-priority sampling to improve estimate stability (\ANTk), and we compare it with a baseline anonymous protocols (\AN) and a randomised variant designed to improve accuracy (\ANT). We find that the baseline protocol \AN provides a parsimonious and fast solution, but remains highly inaccurate due to double-counting bias. The \ANT variant improves accuracy but suffers from information inertia, resulting in slower convergence. Finally, actively filtering the message buffer via the \ANTk protocol successfully decreases temporary errors and stabilises the estimate, at the cost of an increased time of recovery from errors.

</details>

---
