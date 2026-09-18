# cs.RO | Robotics | 2026-09-16

#arxiv #ComputerScience

**论文数**: 33

### [[20_Research/Papers/强化学习/Dissecting_Motion-Prior_Regularization_for_Data-Scarce_Robotic_Insertion|Dissecting Motion-Prior Regularization for Data-Scarce Robotic Insertion]]

![[assets/2609.17484_first_page.png|800]]

- **arXiv**: [2609.17484](https://arxiv.org/abs/2609.17484)
- **PDF**: https://arxiv.org/pdf/2609.17484
- **详细分析**: [[20_Research/Papers/强化学习/Dissecting_Motion-Prior_Regularization_for_Data-Scarce_Robotic_Insertion|Dissecting Motion-Prior Regularization for Data-Scarce Robotic Insertion]]
- **作者**: Ning Hu, Shuai Li, Jindong Tan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Dissecting Motion-Prior Regularization for Data-Scarce Robotic Insertion》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This study asks whether training-time motion-prior regularization can improve insertion success when a diffusion policy is learned from only 15 demonstrations. Minimum jerk discourages abrupt changes in predicted translational acceleration; speed-curvature regularization instead couples movement speed to path geometry. These are candidate mechanisms for task completion, not safety guarantees. We compare the priors individually and jointly, neither prior, and generic smoothness, with 80 real-robot trials per setting pooled over four recorded condition classes. Joint and minimum-jerk-only settings each achieved 70/80 successes (87.5%), versus 69/80 (86.3%) for speed-curvature only, 66/80 (82.5%) for neither prior, and 67/80 (83.8%) for generic smoothness. Success rates and Wilson 95% confidence intervals are visualized for direct comparison. Joint regularization exceeded neither by 5.0 percentage points but provided no observed gain over minimum jerk alone. The results motivate minimum jerk as the simpler candidate for replication, without establishing synergy, biomechanical specificity, improved safety, or distribution-shift robustness.

</details>

---

### [[20_Research/Papers/机器人/Gaussian_Processes_for_Modelling_Spatial_Fields_with_Robot_Swarms|Gaussian Processes for Modelling Spatial Fields with Robot Swarms]]

![[assets/2609.17463_figure.png|800]]

- **arXiv**: [2609.17463](https://arxiv.org/abs/2609.17463)
- **PDF**: https://arxiv.org/pdf/2609.17463
- **详细分析**: [[20_Research/Papers/机器人/Gaussian_Processes_for_Modelling_Spatial_Fields_with_Robot_Swarms|Gaussian Processes for Modelling Spatial Fields with Robot Swarms]]
- **作者**: Guillermo Legarda Herranz, Gianpiero Francesca, Mauro Birattari
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Gaussian Processes for Modelling Spatial Fields with Robot Swarms》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot swarms, by virtue of their decentralised architecture, are a natural tool for scalable, robust modelling of spatial fields, such as water temperature, wind velocity, or terrain elevation. However, existing methods rely on external positioning systems that allow each robot to determine its own position in space. Here, we introduce location-unaware Gaussian process regression (LU-GPR) as a solution to the modelling of spatial fields in the absence of such positioning systems. LU-GPR allows each robot to infer the posterior mean and variance of the field in space, while simultaneously agreeing on a common frame of reference with its peers, using only local sensing and communication. We propose an online algorithm that allows each robot to consistently infer local estimates as its local frame of reference converges to the common one. By means of a product of experts model, each robot also combines the estimates of its peers with its own to obtain a global model. Our results show that LU-GPR scales well with the number of robots and is robust to limited communication ranges. We also demonstrate how it can be used in real-world monitoring scenarios to estimate the flow of an evacuating crowd.

</details>

---

### [[20_Research/Papers/机器人/Hamilton-Jacobi_Reachability_for_Hybrid_Systems_Unified_Goal-Driven_Control_with_Safety_Guarantees|Hamilton-Jacobi Reachability for Hybrid Systems: Unified Goal-Driven Control with Safety Guarantees]]

![[assets/2609.17430_figure.png|800]]

- **arXiv**: [2609.17430](https://arxiv.org/abs/2609.17430)
- **PDF**: https://arxiv.org/pdf/2609.17430
- **详细分析**: [[20_Research/Papers/机器人/Hamilton-Jacobi_Reachability_for_Hybrid_Systems_Unified_Goal-Driven_Control_with_Safety_Guarantees|Hamilton-Jacobi Reachability for Hybrid Systems: Unified Goal-Driven Control with Safety Guarantees]]
- **作者**: Javier Borquez, Shuang Peng, Somil Bansal
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Hamilton-Jacobi Reachability for Hybrid Systems: Unified Goal-Driven Control with Safety Guarantees》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Hybrid dynamical systems provide a powerful modeling framework for robotic systems, particularly in contact-rich environments. However, ensuring safety and performance in such systems remains challenging due to the intricate coupling between continuous dynamics and discrete mode transitions. In this work, we extend classical Hamilton-Jacobi (HJ) reachability analysis, a formal verification method for continuous-time nonlinear systems, to hybrid dynamical systems. Our framework characterizes safe sets for hybrid systems through a generalized value function defined over both discrete and continuous states while accounting for control constraints and model uncertainty. We additionally provide a numerical algorithm to compute this value function. Building on these safe sets, we propose two different mechanisms to integrate performance objectives. First, we introduce a hybrid least-restrictive safety filter that intervenes on both the discrete and continuous components of a nominal controller only when necessary to avoid unsafe states, thereby preserving nominal behavior whenever possible. Second, we formulate and compute hybrid backward reach-avoid tubes, enabling the simultaneous enforcement of safety and goal-reaching behavior, an extension not previously addressed within hybrid HJ reachability. This enables the synthesis of continuous and discrete control policies that guarantee both safety and task completion. We validate our framework through simulation studies and real-world experiments on a quadrupedal robot, demonstrating its effectiveness in hybrid mode planning and safety-critical applications.

</details>

---

### [[20_Research/Papers/机器人/Optimized_Wrench_Polytope_Analysis_for_Real-Time_Stability_Control_of_Legged_Robots_in_Complex_Multi-Contact_Configurations|Optimized Wrench Polytope Analysis for Real-Time Stability Control of Legged Robots in Complex Multi-Contact Configurations]]

![[assets/2609.17405_figure.png|800]]

- **arXiv**: [2609.17405](https://arxiv.org/abs/2609.17405)
- **PDF**: https://arxiv.org/pdf/2609.17405
- **详细分析**: [[20_Research/Papers/机器人/Optimized_Wrench_Polytope_Analysis_for_Real-Time_Stability_Control_of_Legged_Robots_in_Complex_Multi-Contact_Configurations|Optimized Wrench Polytope Analysis for Real-Time Stability Control of Legged Robots in Complex Multi-Contact Configurations]]
- **作者**: Friedrich Graaf, Elias Birkefeld, Christian Eichmann, Elias Hofele, Tristan Schnell, Georg Heppner, Arne Roennau, Rüdiger Dillmann
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Optimized Wrench Polytope Analysis for Real-Time Stability Control of Legged Robots in Complex Multi-Contact Configurations》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged robots offer a variety of automation applications in real-world scenarios. But areas that are difficult to traverse, like slopes, caves, or scaffolding, still pose a great challenge for traversal. To tackle this problem, we propose an optimized algorithm for evaluating the full actuatable wrench polytope for arbitrary contact scenarios. With our improved analysis algorithm, the torques for each joint of the robot can be calculated within a control frequency of 49 Hz. The achieved speedup allows for deployment within a regular control loop for actuating robot poses for different contact scenarios. We evaluated our stability controller extensively in simulation scenarios and validated its applicability by deploying it on actual walking robot hardware. The proposed controller achieved stability in very complex scenarios that are currently not achievable by any other controller.

</details>

---

### [[20_Research/Papers/强化学习/Residual_Fault_Adaptation_for_Dexterous_In-Hand_Manipulation_Under_Runtime_Joint_Faults|Residual Fault Adaptation for Dexterous In-Hand Manipulation Under Runtime Joint Faults]]

![[assets/2609.17404_figure.png|800]]

- **arXiv**: [2609.17404](https://arxiv.org/abs/2609.17404)
- **PDF**: https://arxiv.org/pdf/2609.17404
- **详细分析**: [[20_Research/Papers/强化学习/Residual_Fault_Adaptation_for_Dexterous_In-Hand_Manipulation_Under_Runtime_Joint_Faults|Residual Fault Adaptation for Dexterous In-Hand Manipulation Under Runtime Joint Faults]]
- **作者**: Linan Deng, Xing Liu, Lin Hong, Feng Hua, Guijun Ma, Zuogong Yue, Fumin Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Residual Fault Adaptation for Dexterous In-Hand Manipulation Under Runtime Joint Faults》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous in-hand manipulation requires coordinated control of multiple actuated joints, and a runtime joint fault can abruptly disrupt the contact configuration required for successful manipulation. In this work, we propose residual fault adaptation (RFA), a teacher-anchored framework for compensating for hidden command-channel faults. RFA retains a frozen healthy teacher to provide nominal behavior and trains a recurrent residual policy to infer corrective actions from proprioceptive and command-response history. During training, fault-injection domain randomization (FIDR) varies the fault mode, affected joint, severity, and onset time, while adaptive sampling increases the frequency of fault modes associated with lower recent performance. A frozen Direct FIDR policy provides a distributional reference only on fault-active training samples and is absent from deployment. The deployed controller receives neither fault labels nor controller-switching signals. Simulation experiments on the dexterous hand indicate that RFA can improve manipulation performance relative to the healthy policy under a fixed mixed-fault protocol. Real-robot experiments with software-injected faults further demonstrate zero-shot deployment of the learned adaptation policy.

</details>

---

### [[20_Research/Papers/机器人/Exact_Fusion_and_Coordinated_Exploration_in_Multi-Robot_Active_Inference|Exact Fusion and Coordinated Exploration in Multi-Robot Active Inference]]

![[assets/2609.17384_first_page.png|800]]

- **arXiv**: [2609.17384](https://arxiv.org/abs/2609.17384)
- **PDF**: https://arxiv.org/pdf/2609.17384
- **详细分析**: [[20_Research/Papers/机器人/Exact_Fusion_and_Coordinated_Exploration_in_Multi-Robot_Active_Inference|Exact Fusion and Coordinated Exploration in Multi-Robot Active Inference]]
- **作者**: Peng Wu, Mohsen Imani, Amidu Kamara, Md Tamzeed Islam, Seyede Fatemeh Ghoreishi, Mahdi Imani
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Exact Fusion and Coordinated Exploration in Multi-Robot Active Inference》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot teams that learn a common environment model exchange belief summaries and plan by the expected information gain of their actions. Under conjugate exponential-family beliefs the shared belief is counted once per robot at two points: at fusion, the product of local posteriors counts the common prior $n$ times, and at planning, every robot scores its plan under the same belief and the team converges on the same unknown. Both errors are removed by adding evidence increments to the shared natural parameter, realized increments at fusion and expected increments at planning. The expected increment of a committed teammate gives the next robot its conditional gain; corrected gains sum to the joint gain, the redundancy removed equals the total correlation of the planned observation streams, and sequential commitment keeps the $1/2$ greedy guarantee. The expected increment is exact for Gaussian beliefs with fixed sampling paths and for Dirichlet beliefs under the novelty approximation of discrete active inference, whose team objective has a closed concave form within an explicit bound of the exact mutual information, and fails for finite hypothesis classes, where a short exact enumeration replaces it. Experiments on cooperative RockSample, foraging, and field monitoring show that fusion correction leaves exploration redundancy unchanged, anticipated evidence removes it, and sequential commitment recovers most of the value of centralized joint planning at cost linear in the team size.

</details>

---

### [[20_Research/Papers/具身智能/XPACE_Joint_World_and_Action_Modeling_from_Heterogeneous_Experience|XPACE: Joint World and Action Modeling from Heterogeneous Experience]]

![[assets/2609.17372_figure.png|800]]

- **arXiv**: [2609.17372](https://arxiv.org/abs/2609.17372)
- **PDF**: https://arxiv.org/pdf/2609.17372
- **详细分析**: [[20_Research/Papers/具身智能/XPACE_Joint_World_and_Action_Modeling_from_Heterogeneous_Experience|XPACE: Joint World and Action Modeling from Heterogeneous Experience]]
- **作者**: Jiacheng Wei, Jerry Bai, Xiaoyu Yue, Zidong Wang, Xiaoyang Guo, Cheng Chen, Fanqi Pu, Fan Wu, Zhixu Yue, Yizhuo Li, Feng Qiu, Bo Liu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.8（加权：具身智能 0.9，世界模型 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《XPACE: Joint World and Action Modeling from Heterogeneous Experience》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AnyWorld, Ctrl-World, GigaWorld, IRASim, OpenVLA, SyncWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A general-purpose robot needs to draw on diverse experience, choose actions, and anticipate how those actions will change the world. We introduce XPACE, a unified embodied world model that serves as both a world action model, jointly predicting executable robot actions and future video, and a world simulator, predicting the visual consequences of prescribed actions. Our key insight is that video prediction can both connect heterogeneous experience to action learning and generate new experience for policy improvement. With a shared video backbone between the policy and simulator, we use action-unlabeled video to learn visual dynamics and action-labeled human and robot demonstrations to jointly learn video and action prediction. Building on this architecture, a coarse-to-fine training curriculum progressively emphasizes robot control while retaining human experience, allowing the policy to learn behaviors beyond those covered by robot demonstrations. Beyond learning from recorded experience, XPACE uses its simulator to create additional recovery supervision for the policy. Specifically, we adapt the simulator to its own generated context, synthesize deviation-recovery trajectories around expert demonstrations, and fine-tune the policy on filtered recovery examples. Experiments on XPENG's IRON humanoid robot show that heterogeneous training improves robustness and enables transfer of human-observed skills to tasks absent from robot demonstrations, while recovery data generated by the model's own simulator further improves real-world task completion. Together, these results demonstrate how joint world and action modeling connects learning from heterogeneous experience with simulation-driven policy self-improvement.

</details>

---

### [[20_Research/Papers/机器人/Online_Geometric_Change_Detection_via_Scene_Decomposition|Online Geometric Change Detection via Scene Decomposition]]

![[assets/2609.17302_figure.png|800]]

- **arXiv**: [2609.17302](https://arxiv.org/abs/2609.17302)
- **PDF**: https://arxiv.org/pdf/2609.17302
- **详细分析**: [[20_Research/Papers/机器人/Online_Geometric_Change_Detection_via_Scene_Decomposition|Online Geometric Change Detection via Scene Decomposition]]
- **作者**: David Thorne, Samuel Jia Cong Chua, Nakul Joshi, Aiden Wong, Christa S. Robison, Philip Osteen, Brett T. Lopez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Online Geometric Change Detection via Scene Decomposition》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots are increasingly deployed on long duration single- and multi-session missions in dynamic environments, where the ability to identify environmental changes such as fallen trees or opened doors provides important contextual information for online planning. We propose a framework called Change Detection via Scene Decomposition (CDSD) for accurate online geometric change detection using LiDAR or RGB-D sensors. Recent advances in geometric SLAM have made it possible to generate dense, tightly aligned maps without post processing, but comparing global maps across entire sessions is computationally expensive and does not allow for single-session online change detection. CDSD instead spatially decomposes mapped environments into unique scenes where changes can be found efficiently by comparing dense, local subsets of the global map called submaps. As the first submap-based approach for geometric change detection, we identify and address the following core challenges: 1) identifying appropriate scenes for change detection that require minimal redundant information; 2) generating dense and representative submaps for each scene; 3) detecting changes between submaps with differing fields of view; and 4) processing detected changes for real-time map reconstruction. Results demonstrate our algorithm on custom datasets collected at the Army Research Laboratory facility in Graces Quarters, Maryland, and on open-source multi-session change detection datasets.

</details>

---

### [[20_Research/Papers/强化学习/Calibrate_Once,_Fly_Any_Team_Residual-Grounded_Low-Fidelity_Training_for_Cooperative_Drone_Swarms|Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms]]

![[assets/2609.17265_figure.png|800]]

- **arXiv**: [2609.17265](https://arxiv.org/abs/2609.17265)
- **PDF**: https://arxiv.org/pdf/2609.17265
- **详细分析**: [[20_Research/Papers/强化学习/Calibrate_Once,_Fly_Any_Team_Residual-Grounded_Low-Fidelity_Training_for_Cooperative_Drone_Swarms|Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms]]
- **作者**: Maxim Mednikov, Oren Gal
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，强化学习 0.2，机器人 1.1）
- **关联关键词**: Agent, RL

#### 研究背景与动机

《Calibrate Once, Fly Any Team: Residual-Grounded Low-Fidelity Training for Cooperative Drone Swarms》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Training multi-agent drone-swarm policies directly in high-fidelity (HF) rigid-body physics is accurate but computationally expensive. This cost scales poorly with team size, as each additional agent multiplies contact-resolution complexity and sharply raises the in-simulation crash rate. To address this, we propose a mixed-fidelity training scheme that eliminates HF reinforcement learning entirely. A single shared, decentralized policy is optimized inside a fully-differentiable, JAX-native low-fidelity (LF) point-mass simulator. The simulator is corrected by a small, per-agent bagged residual ensemble fit once, offline, using short calibration flights in the HF simulator. Because calibration requires only one isolated drone, the data collection budget does not compound with team size. Reference trajectories are generated by rolling out an existing LF-only policy and tracked in the HF simulator by a zero-training PD controller. Evaluated across four cooperative drone tasks and team sizes from 3 to 18, the residual-corrected policy outperforms an uncorrected LF baseline in all combinations, and a from-scratch HF policy in 22 of 24 combinations tested. It trails an HF-finetuned policy by a margin that narrows steadily with team size. Ultimately, the proposed method achieves near-equivalent performance at the largest team sizes at a fraction of the computational cost, completely avoiding the high crash rates typical of HF training.

</details>

---

### [[20_Research/Papers/具身智能/CAD-Based_Relation_Learning_and_Geometric-Symbolic_Planning_for_Robotic_Assembly|CAD-Based Relation Learning and Geometric-Symbolic Planning for Robotic Assembly]]

![[assets/2609.17263_figure.png|800]]

- **arXiv**: [2609.17263](https://arxiv.org/abs/2609.17263)
- **PDF**: https://arxiv.org/pdf/2609.17263
- **详细分析**: [[20_Research/Papers/具身智能/CAD-Based_Relation_Learning_and_Geometric-Symbolic_Planning_for_Robotic_Assembly|CAD-Based Relation Learning and Geometric-Symbolic Planning for Robotic Assembly]]
- **作者**: Fabian Harlacher, Christian Friedrich
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《CAD-Based Relation Learning and Geometric-Symbolic Planning for Robotic Assembly》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, PartNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Assembly Sequence Planning (ASP) remains a challenging problem due to its combinatorial nature, making exhaustive planning approaches impractical for complex industrial assemblies. Furthermore, many CAD models lack reliable semantic contact information or require extensive manual preprocessing, limiting the applicability of existing methods. This paper presents a hybrid ASP framework combining learning-based relation extraction with geometric-symbolic reasoning to generate feasible robotic disassembly sequences from imperfect CAD data. A neural network predicts semantic geometric relations from point clouds, while human-in-the-loop verification enables correction of uncertain predictions and planning failures. Extracted relations are transformed into a symbolic assembly graph, enabling a geometric-symbolic planner to efficiently compute locally valid sets of robotic manipulation primitives. A visibility-based ray-casting strategy guides the search for feasible disassembly directions without requiring an exhaustive combinatorial search, while the local solution space enables efficient sequence optimization. The framework is evaluated on an introduced assembly dataset and on the ASAP test dataset. On the ASAP test dataset, the proposed planner achieves an 85.83% planning success rate while reducing the median planning time by more than one order of magnitude across all assembly sizes and by more than a factor of 50 for assemblies with more than 30 components compared to the baseline. The results demonstrate that the proposed hybrid framework enables efficient robotic assembly sequence planning from imperfect CAD data while substantially reducing planning time. By combining learning-based feature segmentation, human-in-the-loop verification, and geometric-symbolic reasoning, the framework provides a practical foundation for scalable and adaptable robotic assembly and disassembly planning.

</details>

---

### [[20_Research/Papers/机器人/Port-Hamiltonian_Koopman_Operator_Synthesis_for_Mechanical_Systems|Port-Hamiltonian Koopman Operator Synthesis for Mechanical Systems]]

![[assets/2609.17249_figure.png|800]]

- **arXiv**: [2609.17249](https://arxiv.org/abs/2609.17249)
- **PDF**: https://arxiv.org/pdf/2609.17249
- **详细分析**: [[20_Research/Papers/机器人/Port-Hamiltonian_Koopman_Operator_Synthesis_for_Mechanical_Systems|Port-Hamiltonian Koopman Operator Synthesis for Mechanical Systems]]
- **作者**: Rajpal Singh, Aditya Singh, Jishnu Keshavan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Port-Hamiltonian Koopman Operator Synthesis for Mechanical Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Finite-dimensional Koopman models enable efficient linear prediction and control of nonlinear robotic systems. However, models learned purely from trajectory data may violate the energetic structure of the underlying mechanics, producing predictions that exhibit artificial energy growth and diverge under recursive propagation. This work presents a structure-preserving Koopman framework for Euler-Lagrange systems built on generalized-momentum coordinates. The momentum transformation exposes the mechanical actuation as a known, state-independent port, which is preserved explicitly in the lifted dynamics. A structure-constrained neural architecture is developed to jointly learn the lifting functions and a port-Hamiltonian Koopman generator, rendering the learned dynamics passive by construction rather than through penalty terms or post-hoc projection. A Cayley-midpoint discretization further preserves the corresponding storage-dissipation balance exactly in discrete time. These properties are established analytically by deriving the discrete storage balance and associated stability guarantees of the learned predictor. Simulation and experimental studies demonstrate improved prediction accuracy, data efficiency, and closed-loop tracking over Koopman baselines, with increasing gains for higher-dimensional systems.

</details>

---

### [[20_Research/Papers/机器人/Swim-and-Breach_at_Palm_Scale_A_Rudder-Steered_Two-Propeller_Underwater_Robot_Platform_with_Differential-Thrust_Pitch_Control|Swim-and-Breach at Palm Scale: A Rudder-Steered Two-Propeller Underwater Robot Platform with Differential-Thrust Pitch Control]]

![[assets/2609.17240_figure.png|800]]

- **arXiv**: [2609.17240](https://arxiv.org/abs/2609.17240)
- **PDF**: https://arxiv.org/pdf/2609.17240
- **详细分析**: [[20_Research/Papers/机器人/Swim-and-Breach_at_Palm_Scale_A_Rudder-Steered_Two-Propeller_Underwater_Robot_Platform_with_Differential-Thrust_Pitch_Control|Swim-and-Breach at Palm Scale: A Rudder-Steered Two-Propeller Underwater Robot Platform with Differential-Thrust Pitch Control]]
- **作者**: Daehyun Choi, Ian Bergerson, Hengjia Zhu, Tianjun Lan, Saad Bhamla
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Swim-and-Breach at Palm Scale: A Rudder-Steered Two-Propeller Underwater Robot Platform with Differential-Thrust Pitch Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a palm-scale (65 mm, 34 g) swim-and-breach robot platform. Two vertically stacked propellers provide both propulsion and differential-thrust pitch control under a proportional-integral-derivative (PID) loop, and a tail rudder adds yaw control. The hull, evaluated by flow simulation, reduces the drag five-fold relative to an equivalent cuboid, and the propellers are optimized using B-series modeling validated by dynamometer measurements. The current robot swims at 13.9 body lengths per second and turns at 209 deg per second, corresponding to the upper limits reported for underwater robots. In free swimming, the pitch loop turns the body to any commanded nose-up pitch angle, and, with the rudder stabilizing the exit, the current robot leaps 1.6 body lengths high and 3.7 long in a seamless cruise-leap-cruise sequence. The platform can be used to build small-scale robots that cross barriers and dry gaps between pools for inspection in streams, flooded structures, and industrial systems.

</details>

---

### [[20_Research/Papers/具身智能/TIO-Former_Ultra-Lightweight_6-Directional_ToF-Inertial_Odometry_for_Nano-UAVs_via_a_Streaming_Causal_Transformer|TIO-Former: Ultra-Lightweight 6-Directional ToF-Inertial Odometry for Nano-UAVs via a Streaming Causal Transformer]]

![[assets/2609.17198_figure.png|800]]

- **arXiv**: [2609.17198](https://arxiv.org/abs/2609.17198)
- **PDF**: https://arxiv.org/pdf/2609.17198
- **详细分析**: [[20_Research/Papers/具身智能/TIO-Former_Ultra-Lightweight_6-Directional_ToF-Inertial_Odometry_for_Nano-UAVs_via_a_Streaming_Causal_Transformer|TIO-Former: Ultra-Lightweight 6-Directional ToF-Inertial Odometry for Nano-UAVs via a Streaming Causal Transformer]]
- **作者**: Yang Liu, Yifan He, Wenhao Zhao, Xiangyu Mo, Yang Xu, Hao Wei, Mingze Ma, Huan Li, Yifan Wu, Zipeng Dai, Xin Zhou, Fei Gao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: EmbodiedAI, Systems

#### 研究背景与动机

《TIO-Former: Ultra-Lightweight 6-Directional ToF-Inertial Odometry for Nano-UAVs via a Streaming Causal Transformer》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PULP-DroNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous nano-UAV navigation requires accurate ego-motion estimation under stringent size, weight, power, and computing (SWaP-C) constraints, where visual sensors and LiDARs exceed payload limits, optical flow degrades in low-texture scenes, and inertial-only state estimation is susceptible to accumulated drift. While multi-zone time-of-flight (ToF) arrays provide a lightweight metric complement, 6-DoF estimation from merely 384 ranges per frame is challenged by invalid returns, anisotropic observability, and temporal computational scaling. We propose TIO-FORMER, a camera-free, optical-flow-free, and mapless range-inertial odometry framework driven by an IMU and an ultra-lightweight (15 g) payload of six orthogonal 8 x 8 ToF arrays. Our frontend pairs consecutive range grids with a bilateral gated difference, while IMU-guided cross-attention dynamically routes directional features conditioned on platform kinematics. A Streaming Causal Transformer couples an uncompressed Local KV cache with compressed Chunk-FIFO memory, maintaining bounded inference cost and memory footprint independent of flight duration. In real-flight evaluations, TIO-FORMER reduces open-loop position error by 54.4% compared to nano-UAV optical flow and by 66.4%-89.1% over learned inertial baselines. We also evaluate performance across multiple environments and robustness under severe sensing degradation. Deployed on an edge RISC-V companion computer, TIO-FORMER achieves a P95 latency of 10.466 ms and peak resident memory of 6.324 MiB (less than 5 percent system RAM), demonstrating that sparse range sensing provides practical geometric anchoring for resource-constrained micro-aerial robots. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Fleet-To-Lab_A_Transfer_Learning_Framework_For_Lunar_Rover_Slippage_Estimation_Via_Model_Fusion|Fleet-To-Lab: A Transfer Learning Framework For Lunar Rover Slippage Estimation Via Model Fusion]]

![[assets/2609.17187_figure.png|800]]

- **arXiv**: [2609.17187](https://arxiv.org/abs/2609.17187)
- **PDF**: https://arxiv.org/pdf/2609.17187
- **详细分析**: [[20_Research/Papers/具身智能/Fleet-To-Lab_A_Transfer_Learning_Framework_For_Lunar_Rover_Slippage_Estimation_Via_Model_Fusion|Fleet-To-Lab: A Transfer Learning Framework For Lunar Rover Slippage Estimation Via Model Fusion]]
- **作者**: Riccardo Viviano, Saki Omi, Andrej Orsula, Miguel Olivares-Mendez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Fleet-To-Lab: A Transfer Learning Framework For Lunar Rover Slippage Estimation Via Model Fusion》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate wheel slip estimation is essential for autonomous lunar rover mobility and navigation. Machine Learning models trained on terrestrial data generalize poorly to lunar terrain, and real lunar datasets are scarce due to the limited number of missions and costly data acquisition. We present Fleet-to-Lab, a transfer learning framework that leverages proprioceptive data collected by previously deployed heterogeneous lunar rovers to mitigate the Earth-Moon domain gap in slip estimation for a future deployable unit. We fuse several heterogeneous expert models into a single architecture, using a modest dataset collected after the rover deployment. We propose AcoMerge, a new hybrid swarm-intelligence algorithm that performs model fusion by searching for an optimal combi- nation of expert parameters. Experiments conducted in a high- fidelity physics simulation show balanced accuracy and macro- F1 improvements compared to deep model fusion baselines. AcoMerge exhibits competitive performance with joint training on deep architectures, while achieving higher macro-F1 and balanced accuracy on a smaller model. Overall, our framework shows model fusion as a possible transfer learning alternative for slippage estimation in space robotic missions with limited data.

</details>

---

### [[20_Research/Papers/具身智能/Fingers_as_Legs_Learning_Self-Supported_Locomotion_and_Manipulation_with_an_Anthropomorphic_Hand|Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with an Anthropomorphic Hand]]

![[assets/2609.17172_figure.png|800]]

- **arXiv**: [2609.17172](https://arxiv.org/abs/2609.17172)
- **PDF**: https://arxiv.org/pdf/2609.17172
- **详细分析**: [[20_Research/Papers/具身智能/Fingers_as_Legs_Learning_Self-Supported_Locomotion_and_Manipulation_with_an_Anthropomorphic_Hand|Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with an Anthropomorphic Hand]]
- **作者**: Amirhossein Kazemipour, Hehui Zheng, Robert Katzschmann
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.2（加权：具身智能 1.5，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Fingers as Legs: Learning Self-Supported Locomotion and Manipulation with an Anthropomorphic Hand》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A walking robotic hand must use the same fingers to move its body, support its weight, and interact with the environment. We show how an anthropomorphic hand can learn these skills while retaining its finger design and position controller. Onboard power and computation make the platform self-contained. Our reinforcement learning approach accounts for the hand's unequal fingers, with training in a simulator calibrated from hardware measurements. In simulation, the hand moves faster with our reward formulation than with tuned rewards originally designed for quadrupeds. On hardware, task-specific policies enable untethered crawling, steering, and fall recovery. While supporting its own weight, the hand also executes successive keyboard commands without vision and pushes an object to targets using overhead visual feedback. These results demonstrate a compact mobile manipulator that reuses its fingers for locomotion and interaction, without a separate locomotion mechanism.

</details>

---

### [[20_Research/Papers/机器人/LOTUSim-Energy_A_Maritime_Simulator_for_Human-Drone_Interaction_in_Autonomous_Offshore_Operation_&amp;_Maintenance|LOTUSim-Energy: A Maritime Simulator for Human-Drone Interaction in Autonomous Offshore Operation \&amp; Maintenance]]

![[assets/2609.17124_first_page.png|800]]

- **arXiv**: [2609.17124](https://arxiv.org/abs/2609.17124)
- **PDF**: https://arxiv.org/pdf/2609.17124
- **详细分析**: [[20_Research/Papers/机器人/LOTUSim-Energy_A_Maritime_Simulator_for_Human-Drone_Interaction_in_Autonomous_Offshore_Operation_&amp;_Maintenance|LOTUSim-Energy: A Maritime Simulator for Human-Drone Interaction in Autonomous Offshore Operation \&amp; Maintenance]]
- **作者**: Juliette Grosset, Marie Dubromel, Hélène Lechêne, Quentin Arzel, Cédric Buche
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《LOTUSim-Energy: A Maritime Simulator for Human-Drone Interaction in Autonomous Offshore Operation \&amp; Maintenance》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LOTUSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Offshore maintenance requires operations in the air, the surface, and the subsea domain and include human supervision. This paper presents LOTUSim-Energy, a real-time maritime simulator designed for multi-domain human--drone interaction for offshore operation and maintenance. The plat- form unifies heterogeneous unmanned vehicles (Unmanned Aerial Vehicles: UAVs, Unmanned Surface Vehicles: USVs, Autonomous Underwater Vehicles: AUVs, Remotely Operated Vehicles: ROVs) within a distributed architecture coupling environment forcing (wind, waves, currents) and provides immersive user interfaces for supervision (desktop and virtual reality). A structured offshore task library enables repeatable evaluation of autonomy stacks under realistic metocean disturbances. The simulator supports realistic physics, energy-aware battery modeling, and fault-detection pipelines as modular validation tools. System-level performance is demonstrated on a multi-domain inspection scenario for monopile and transition piece structure, where we evaluate the reliability of integrated waypoint-follower plugin and Automatic Identification System (AIS)-referenced trajectory tracking under real-time energy monitoring. By combining unified environmental physics, heterogeneous vehicle simulation, and immersive supervision, LOTUSim-Energy provides an integration testbed for prototyping and rehearsing offshore human--robot collaboration workflows, as a step toward de-risking sea deployment.

</details>

---

### [[20_Research/Papers/具身智能/BRAVE-6D_Benchmark_for_Robotic_Active_Vision_in_6DOF_Pose_Estimation|BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation]]

![[assets/2609.17106_figure.png|800]]

- **arXiv**: [2609.17106](https://arxiv.org/abs/2609.17106)
- **PDF**: https://arxiv.org/pdf/2609.17106
- **详细分析**: [[20_Research/Papers/具身智能/BRAVE-6D_Benchmark_for_Robotic_Active_Vision_in_6DOF_Pose_Estimation|BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation]]
- **作者**: Philipp Ausserlechner, Bernhard Neuberger, Alessandro Scherl, Michael Schebek, Stefan Thalhammer, Markus Vincze
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.1（加权：具身智能 0.6，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《BRAVE-6D: Benchmark for Robotic Active Vision in 6DOF Pose Estimation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：GDR-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Detecting and grasping small objects remains a significant challenge in robotics. Active vision, where the robot moves closer to the object, is an intuitive solution, yet comparing approaches on common ground is difficult since identical physical scene setups are required. Hence, we introduce BRAVE-6D, a benchmark designed to evaluate robotic active vision systems for object pose estimation, a crucial first step in grasping objects. BRAVE-6D leverages view synthesis based on Gaussian Splats (3DGS) to provide scenes and tools for benchmarking active vision systems. We show baseline solutions performing visual servoing within the scene and accurately estimating the poses of small objects.

</details>

---

### [[20_Research/Papers/具身智能/SWIM_Vision-Language-Grounded_Soft_Whole-Body_Interactive_Manipulation|SWIM: Vision-Language-Grounded Soft Whole-Body Interactive Manipulation]]

![[assets/2609.17035_figure.png|800]]

- **arXiv**: [2609.17035](https://arxiv.org/abs/2609.17035)
- **PDF**: https://arxiv.org/pdf/2609.17035
- **详细分析**: [[20_Research/Papers/具身智能/SWIM_Vision-Language-Grounded_Soft_Whole-Body_Interactive_Manipulation|SWIM: Vision-Language-Grounded Soft Whole-Body Interactive Manipulation]]
- **作者**: Tingcong Liu, Aye Phyu Phyu Aung, Junjie Xiong, Siyi Ma, Bo An, Ke Wu, Senthilnath Jayavelu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.0（加权：具身智能 1.5，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《SWIM: Vision-Language-Grounded Soft Whole-Body Interactive Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SWIM-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft and continuum robots enable manipulation through distributed body deformation and contact, yet translating language and visual context into executable whole-body actuation remains a fundamental challenge. We present SWIM, a framework that maps an initial RGB observation and a language instruction to a complete actuation-command sequence. Its vision-language-action (VLA) policy, SWIM-VLA, combines a diffusion action head with Visual Soft Proprioception (VSP) through a shared representation of RGB observations, language instructions, and tendon states. The diffusion head models conditional distributions of expert command chunks, while VSP supervises ordered body-anchor predictions using simulation ground truth, encouraging the representation to retain body geometry when learning from limited demonstrations. Embodied mechanical intelligence supports physical execution of command sequences generated through iterative virtual rollout from evolving simulated observations, with intrinsic compliance providing local contact adaptation without online policy queries. We evaluate SWIM on packing, reaching, and grasping on a planar tendon-driven soft robot, with grasping targets anchored. In simulation, SWIM-VLA achieves success rates of 100\%, 96\%, and 88\%, respectively, outperforming an adapted OpenVLA-OFT baseline and controlled ablations. On hardware, SWIM achieves success rates of 100\%, 80\%, and 75\%, compared with 75\%, 40\%, and 25\% for direct online deployment of the same policy checkpoint.

</details>

---

### [[20_Research/Papers/机器人/Overcoming_technical_adoption_barriers_for_mobile_service_robots_in_rehabilitation|Overcoming technical adoption barriers for mobile service robots in rehabilitation]]

![[assets/2609.16996_first_page.png|800]]

- **arXiv**: [2609.16996](https://arxiv.org/abs/2609.16996)
- **PDF**: https://arxiv.org/pdf/2609.16996
- **详细分析**: [[20_Research/Papers/机器人/Overcoming_technical_adoption_barriers_for_mobile_service_robots_in_rehabilitation|Overcoming technical adoption barriers for mobile service robots in rehabilitation]]
- **作者**: Christian Sternitzke, Sebastian Blumenthal, Lukas Kleedoerfer, Verena Deserno, Anke Mayfarth
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《Overcoming technical adoption barriers for mobile service robots in rehabilitation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many publications on robotic systems in healthcare describe early-stage work on low technology readiness levels. This paper describes how a mobile service robot approved as a medical device reaches higher technology readiness levels by adding peripheral functions and smaller improvements, which are pivotal for user acceptance in clinical environments and which often cannot be elicited by questioning users ex-ante as certain aspects only come in mind from testing the systems in clinical settings or operational environments. Especially developers of service robots in healthcare are advised to plan with such downstream developments, which can take significant implementation time, to obtain user acceptance and achieve widespread adoption of their robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Artificial_Intelligence-Enabled_Space_Robot_Operations_Technologies,_Challenges_and_Prospects|Artificial Intelligence-Enabled Space Robot Operations: Technologies, Challenges and Prospects]]

![[assets/2609.16880_figure.png|800]]

- **arXiv**: [2609.16880](https://arxiv.org/abs/2609.16880)
- **PDF**: https://arxiv.org/pdf/2609.16880
- **详细分析**: [[20_Research/Papers/具身智能/Artificial_Intelligence-Enabled_Space_Robot_Operations_Technologies,_Challenges_and_Prospects|Artificial Intelligence-Enabled Space Robot Operations: Technologies, Challenges and Prospects]]
- **作者**: Zeyuan Huang, Gang Chen, Zixuan Hao, Guoqin Tang, Junyi Zong, Guoyou Ban, Jiale Wang, Haoyang Lv, Chaoqian Ren, Sitong Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Artificial Intelligence-Enabled Space Robot Operations: Technologies, Challenges and Prospects》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Space robots are increasingly expected to perform long-duration, contact-rich, and multi-stage operations with limited human intervention. Recent advances in artificial intelligence (AI), robot learning, and embodied foundation models provide new opportunities to improve the autonomy and adaptability of such systems, but their transfer to space is constrained by scarce mission data, space-specific dynamics and sensing conditions, limited onboard resources, and stringent safety requirements. This article reviews artificial intelligence-enabled space robot operations (AI-SRO) from a capability-building perspective. We first summarize representative operational scenarios, autonomy trends, and space-specific constraints. We then establish a three-layer technical framework comprising capability foundations, capability formation, and capability deployment/evolution. Within this framework, we review simulation environments, datasets and benchmarks; task and environment understanding, state perception, decision-making and planning, and action execution; and onboard deployment, ground-to-space adaptation, continual learning, and capability transfer. Finally, we propose key research directions toward trustworthy simulation and data, open-world multimodal cognition, long-horizon safe decision-making, physically constrained policy learning, and space computing infrastructures.

</details>

---

### [[20_Research/Papers/强化学习/Rethinking_Visual_Embodiment_Dependence_in_Visuomotor_Policies|Rethinking Visual Embodiment Dependence in Visuomotor Policies]]

![[assets/2609.16815_figure.png|800]]

- **arXiv**: [2609.16815](https://arxiv.org/abs/2609.16815)
- **PDF**: https://arxiv.org/pdf/2609.16815
- **详细分析**: [[20_Research/Papers/强化学习/Rethinking_Visual_Embodiment_Dependence_in_Visuomotor_Policies|Rethinking Visual Embodiment Dependence in Visuomotor Policies]]
- **作者**: Hongjie Fang, Yuxuan Lu, Chenxi Wang, Haoxiang Qin, Shirun Tang, Zihao He, Shangning Xia, Jingjing Chen, Wanxi Liu, Shiquan Wang, Cewu Lu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Rethinking Visual Embodiment Dependence in Visuomotor Policies》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor policies observe both the task scene and the acting embodiment, allowing embodiment-specific visual cues to influence action prediction. We study this phenomenon as visual embodiment dependence (VED) and show, through cue-conflict interventions across representative policies, that visible robot configuration can become a shortcut to task progress. Rather than eliminating VED, we argue that it should be structured around embodiment information that supports control and generalization. We realize this through embodiment canonicalization in 3D point clouds, replacing the original embodiment with a canonical end-effector representation (CER) that preserves control-relevant geometry while abstracting embodiment-specific morphology. Its editable form further enables configuration-decorrelation augmentation for unfamiliar robot configurations. Experiments show that embodiment canonicalization substantially improves human-to-robot policy transfer without robot demonstrations, while simply removing the embodiment is insufficient without preserving control-relevant geometry. We further find that CER itself can become a configuration shortcut when robot configuration becomes decoupled from task progress; configuration-decorrelation augmentation mitigates this failure mode and restores robust recovery without sacrificing performance on seen configurations. Together, these results show that robust visuomotor learning benefits from structuring, rather than removing, visual embodiment information. Project website: this https URL

</details>

---

### [[20_Research/Papers/机器人/Motion_planning_in_high_dimensional_spaces_hybridizing_RRT_and_HAR_via_position-direction_decoupling|Motion planning in high dimensional spaces hybridizing RRT and HAR via position-direction decoupling]]

![[assets/2609.16810_first_page.png|800]]

- **arXiv**: [2609.16810](https://arxiv.org/abs/2609.16810)
- **PDF**: https://arxiv.org/pdf/2609.16810
- **详细分析**: [[20_Research/Papers/机器人/Motion_planning_in_high_dimensional_spaces_hybridizing_RRT_and_HAR_via_position-direction_decoupling|Motion planning in high dimensional spaces hybridizing RRT and HAR via position-direction decoupling]]
- **作者**: Frederic Cazals, Nelson Feyeux
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Motion planning in high dimensional spaces hybridizing RRT and HAR via position-direction decoupling》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The exploration of high-dimensional spaces remains a challenging problem, in particular in the presence of narrow passages and small clearances. We propose novel sampling-based path-planning methods for high-dimensional spaces combining Rapidly-exploring Random Trees (RRT) and Hit-and-Run (HAR) random walks by decoupling the point being extended from the direction of extension. We also show that RRT and HAR appear as special cases of a generic algorithm coupling the biases used for the point and direction extension, respectively. We further study a sparse-move strategy in which only a fraction p_r of the robots is moved at each step, helping both RRT and the proposed HAR algorithms handle cluttered instances. Tests are presented for two families of models: classical piano mover problems in 3D, and complex molecular systems involving tens of rigid domains moving relatively to one another -- the latter viewed as independent robots exploring the motion space SE(3)N . Within seconds on a standard laptop, our algorithms solve instances with up to 64 robots and 384 degrees of freedom. We conclude by suggesting one of our methods, HARF, as the method of choice for complex multi-robot planning problems, being up to two orders of magnitude faster than the classical RRT moving all robots at each step--when it succeeds at all, and still up to 2.4 fold faster on most instances when both use their best p_r.

</details>

---

### [[20_Research/Papers/具身智能/The_Robot_Data_Factory|The Robot Data Factory]]

![[assets/2609.16705_figure.png|800]]

- **arXiv**: [2609.16705](https://arxiv.org/abs/2609.16705)
- **PDF**: https://arxiv.org/pdf/2609.16705
- **详细分析**: [[20_Research/Papers/具身智能/The_Robot_Data_Factory|The Robot Data Factory]]
- **作者**: Sami Haddadin, Ivan Laptev, Ian Reid, Dezhen Song, Cesare Stefanini, Abdalla Swikir, Xingxing Zuo, Lyes Saad Saoud, Mahmoud Hamandi, Mohamed Heshmat, Oualid Doukhi, Abdeldjallil Naceri...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 2.3（加权：具身智能 0.9，大模型 0.1，世界模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《The Robot Data Factory》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical AI requires more than increasingly large robot datasets: intelligent robots acquire knowledge through continuous interaction with the physical world. We argue that the defining scientific resource of Physical AI is therefore not raw robot data alone, but robot experience - physically grounded interaction whose observations, actions, embodiment, context, and outcomes preserve the perception-action-consequence loop. We introduce the Robot Data Factory (RDF), a mission-driven infrastructure and methodology for continuously generating, validating, benchmarking, and reusing such experience. RDF organizes heterogeneous robots and environment-specific training grounds through reproducible missions, skill curricula, synchronized multimodal sensing, external ground truth, an agentic robot network, data pipelines, and living benchmarks. Rather than treating datasets as static end products, RDF implements a closed Deploy-Measure-Learn-Repeat cycle in which validated physical experience supports world models, vision-language-action models, embodied policies, digital twins, and subsequent robot deployment. We further formalize robot experience and its quality, introduce a mission-task-skill-episode-dataset-benchmark-capability hierarchy, and derive quantitative scaling laws and an algorithmic synthesis procedure connecting robot fleet size, sensor rates, storage, learning representations, tokenization, training compute, inference, and latency to Embodied-AI cluster requirements. The framework is instantiated in three complementary physical training grounds for domestic, environmental, and energy applications. RDF thus reframes robot data generation as a continuous scientific production process and provides a pathway toward reproducible, scalable, and eventually federated infrastructure for Physical AI.

</details>

---

### [[20_Research/Papers/具身智能/WholeBodyWAM_Generalizing_Pre-trained_World-Action_Priors_to_Humanoid_Loco-Manipulation_via_WBC-Grounded_Coordination|WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded Coordination]]

![[assets/2609.16644_figure.png|800]]

- **arXiv**: [2609.16644](https://arxiv.org/abs/2609.16644)
- **PDF**: https://arxiv.org/pdf/2609.16644
- **详细分析**: [[20_Research/Papers/具身智能/WholeBodyWAM_Generalizing_Pre-trained_World-Action_Priors_to_Humanoid_Loco-Manipulation_via_WBC-Grounded_Coordination|WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded Coordination]]
- **作者**: Zhuo Li, Yiming Yao, Jim Tan, Mengjie Jing, Zhipeng Dong, Fei Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《WholeBodyWAM: Generalizing Pre-trained World-Action Priors to Humanoid Loco-Manipulation via WBC-Grounded Coordination》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Pre-trainedWorld, Real-World, URL, WholeBodyVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) offer a promising approach to general-purpose robot manipulation by jointly modeling visual dynamics and actions. However, most WAM studies focus on tabletop or arm-centric manipulation, while humanoid loco-manipulation remains less explored. To address this gap, we introduce WholeBodyWAM, which jointly predicts future visual dynamics, manipulation actions, and whole-body control intents for generalizable humanoid loco-manipulation. It preserves pre-trained world-action priors while grounding heterogeneous whole-body controller (WBC) semantics and coordinating whole-body behavior. Extensive experiments show that WholeBodyWAM achieves an overall simulation task success rate of 91.9%, with a 0.23 improvement in real-world out-of-distribution task progress and a 70% reduction in success-rate variance across WBCs relative to the respective baselines. These results suggest a path toward scalable humanoid whole-body intelligence by extending pre-trained world-action priors through structured WBC grounding and coordination, rather than relearning whole-body behavior from scratch. Project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/SAVLA_Symmetry-Aware_Vision-Language-Action_Models_for_Robotic_Manipulation|SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation]]

![[assets/2609.16641_figure.png|800]]

- **arXiv**: [2609.16641](https://arxiv.org/abs/2609.16641)
- **PDF**: https://arxiv.org/pdf/2609.16641
- **详细分析**: [[20_Research/Papers/具身智能/SAVLA_Symmetry-Aware_Vision-Language-Action_Models_for_Robotic_Manipulation|SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation]]
- **作者**: Junle Li, Weixian Waylon Li, Fuxiang Wu, Fusheng Hao, Fengxiang He
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.1（加权：具身智能 3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SAVLA: Symmetry-Aware Vision-Language-Action Models for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EquiVLA, OpenVLA, SAVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have become the dominant paradigm for language-conditioned robot manipulation. However, although images and language instructions inherently encode geometric information, VLAs acquire their spatial competence purely from demonstrations. As a result, they are reliable only within the range of scene poses that the demonstrations cover. We propose SAVLA, an end-to-end symmetry-aware VLA model for robust and data-efficient policy learning. Our approach keeps the pretrained vision-language backbone entirely frozen while combining it with an equivariant flow-matching action head and a learned canonicalizer. The head decomposes its state, action, and conditioning inputs into invariant and equivariant channels, and preserves this typing throughout all of its layers. The canonicalizer transforms oblique-view images into a canonical frame and rotates the geometric conditions consistently. We evaluate our model on LIBERO. Compared with the GR00T N1.5 baseline, SAVLA improves the success rate averaged over all four LIBERO suites by 5.1 points and increases the mean success rate under rotation on LIBERO-Goal from 41.5% to 90.4%.

</details>

---

### [[20_Research/Papers/强化学习/UniDex-ViTac_Learning_Unified_Visuo-Tactile_Dexterous_Manipulation_Policy_from_Human_Video_Data|UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data]]

![[assets/2609.16504_figure.png|800]]

- **arXiv**: [2609.16504](https://arxiv.org/abs/2609.16504)
- **PDF**: https://arxiv.org/pdf/2609.16504
- **详细分析**: [[20_Research/Papers/强化学习/UniDex-ViTac_Learning_Unified_Visuo-Tactile_Dexterous_Manipulation_Policy_from_Human_Video_Data|UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data]]
- **作者**: Hyesung Lee, Si-Hwan Heo, Sungwook Yang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.4（加权：具身智能 1.5，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《UniDex-ViTac: Learning Unified Visuo-Tactile Dexterous Manipulation Policy from Human Video Data》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human videos provide demonstrations of dexterous manipulation but lack robot-executable actions and tactile measurements. We present UniDex-ViTac, a framework that uses human-video-guided simulation to generate robot demonstrations paired with fingertip contact observations for training a deployable visuo-tactile policy. Object-specific residual reinforcement learning specialists adapt annotated human-object interaction references to a robotic arm-hand system. Their successful rollouts pair final robot action targets with robot-side fingertip contact observations. From 50 human demonstrations across ten objects, we collect 10,000 simulated trajectories to train a single Action Chunking with Transformers (ACT) based generalist. The policy combines point clouds, proprioception, and four binary contact signals encoded through fingertip labels and a separate token, without requiring human references or privileged object identity and pose at deployment. The contact-augmented configuration achieves 68.3% macro-average success in simulation, compared with 55.5% for the point-cloud-only baseline. Without real-robot demonstrations or policy fine-tuning, it succeeds in 73/110 physical trials (66.4%) across six seen and five unseen objects, compared with 60/110 (54.5%) for the baseline, an increase of 11.8 percentage points. These results support the feasibility of learning a unified visuo-tactile dexterous manipulation policy from video-guided simulated interactions. Project page: this https URL

</details>

---

### [[20_Research/Papers/具身智能/Dense_to_MoE_Adaptation_for_Compact_Vision_Language_Action_Policies|Dense to MoE Adaptation for Compact Vision Language Action Policies]]

![[assets/2609.16503_figure.png|800]]

- **arXiv**: [2609.16503](https://arxiv.org/abs/2609.16503)
- **PDF**: https://arxiv.org/pdf/2609.16503
- **详细分析**: [[20_Research/Papers/具身智能/Dense_to_MoE_Adaptation_for_Compact_Vision_Language_Action_Policies|Dense to MoE Adaptation for Compact Vision Language Action Policies]]
- **作者**: Muchun Niu, Shuang Chen, Yuzhou Wu, Linfeng Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Dense to MoE Adaptation for Compact Vision Language Action Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision language action (VLA) policies continue to grow in parameter count, making deployment on resource-constrained robot platforms difficult. The central goal is to reduce the number of LLM-side parameters retained in the deployed policy while preserving downstream task performance. Our approach, AdaDE, adapts selected dense feed forward blocks into mixture of experts (MoE) layers and derives expert retention masks from router statistics during fine tuning. The Dense2MoE conversion preserves the original dense FFN function at initialization, so expert deactivation can start without a separate recovery stage. Instead of using a fixed shutdown rule, expert masks are updated dynamically from router usage statistics, with staged training and expert protection to avoid early collapse. With 40% of the LLM parameters deactivated, AdaDE retains 95.1% average success in LIBERO and 42.0% average success across all 50 RobotWin2.0 tasks. These results suggest that dense to MoE adaptation with dynamic expert deactivation is a practical direction for reducing active VLA model size without severe performance loss.

</details>

---

### [[20_Research/Papers/机器人/A_Programmable_Optics_Cloud_Laboratory|A Programmable Optics Cloud Laboratory]]

![[assets/2609.16413_figure.png|800]]

- **arXiv**: [2609.16413](https://arxiv.org/abs/2609.16413)
- **PDF**: https://arxiv.org/pdf/2609.16413
- **详细分析**: [[20_Research/Papers/机器人/A_Programmable_Optics_Cloud_Laboratory|A Programmable Optics Cloud Laboratory]]
- **作者**: Sachin Vaidya, Caio Silva, Seou Choi, Joshua Chen, Marin Soljačić
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Programmable Optics Cloud Laboratory》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Laboratory automation can improve experimental throughput, accessibility, and reproducibility, but many robotic laboratory systems remain difficult to reconfigure. This challenge is especially pronounced in free-space optics, where experiments are built from heterogeneous components, require precise alignment, and are frequently rearranged as experimental goals change. In this work, we present the Programmable Infrastructure for Cloud Optics (PICO), a robotic cloud-laboratory architecture designed to make reconfigurable optical experiments easier to program, operate, and reproduce. PICO provides a common domain-specific abstraction and software layer through which experimental configurations and actions can be controlled across different user interfaces. This enables the same physical laboratory to support remote interactive use, scripted experiments, autonomous routines, and features such as version control. We implement PICO on a robotic free-space optics platform and demonstrate it through an experimental case study.

</details>

---

### [[20_Research/Papers/具身智能/Collision-Aware_Humanoid_Whole-Body_Control_under_Imperfect_Tracking_Targets|Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets]]

![[assets/2609.16405_figure.png|800]]

- **arXiv**: [2609.16405](https://arxiv.org/abs/2609.16405)
- **PDF**: https://arxiv.org/pdf/2609.16405
- **详细分析**: [[20_Research/Papers/具身智能/Collision-Aware_Humanoid_Whole-Body_Control_under_Imperfect_Tracking_Targets|Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets]]
- **作者**: Mohitvishnu S. Gadde, Ashish Malik, Pranay Dugar, Aayam Kumar Shrestha, Alan Fern
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Collision-Aware Humanoid Whole-Body Control under Imperfect Tracking Targets》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots often execute motion commands through whole-body controllers (WBCs) that track targets while maintaining balance and stability. However, most WBCs are blind to scene geometry, which can lead to collisions from imperfect target motions that are geometrically unsafe due to perception, planning, or teleoperation errors. We propose RECAL, a Robot--Environment Cross-Attention Layer that wraps a blind WBC to trade off target tracking against collision avoidance using external scene geometry. RECAL supports collision-aware tracking of floating-base and end-effector commands, including collision avoidance for held objects. It represents the robot, held objects, and environment as point clouds, using cross-attention between robot/object points and the environment to produce geometry-aware control features. In simulation, RECAL improves collision avoidance while preserving target-tracking performance across frozen-arm and adaptive-arm locomotion, object-carrying, and standing-manipulation scenarios relative to alternative geometry-aware WBC architectures. We further demonstrate the controller on a real Digit V3 humanoid robot.

</details>

---

### [[20_Research/Papers/具身智能/ManiSkillFormer_Demonstration-Free_Compositional_Manipulation_via_Task-Conditioned_Geometric_Contracts|ManiSkillFormer: Demonstration-Free Compositional Manipulation via Task-Conditioned Geometric Contracts]]

![[assets/2609.16331_figure.png|800]]

- **arXiv**: [2609.16331](https://arxiv.org/abs/2609.16331)
- **PDF**: https://arxiv.org/pdf/2609.16331
- **详细分析**: [[20_Research/Papers/具身智能/ManiSkillFormer_Demonstration-Free_Compositional_Manipulation_via_Task-Conditioned_Geometric_Contracts|ManiSkillFormer: Demonstration-Free Compositional Manipulation via Task-Conditioned Geometric Contracts]]
- **作者**: Peiqi Yu, Mosam Dabhi, Shangtao Li, Bowei Li, Laszlo Jeni, Changliu Liu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.2，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《ManiSkillFormer: Demonstration-Free Compositional Manipulation via Task-Conditioned Geometric Contracts》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present ManiSkillFormer, a neuro-symbolic framework for demonstration-free and compositional robotic manipulation. Instead of learning end-to-end visuomotor policies, ManiSkillFormer introduces task-conditioned geometric contracts that explicitly structure the interface between perception and action. Each manipulation skill declares the semantic geometric primitives required for execution, such as object keypoints and surface normals. Building on human-defined skill structures, LLM agents generate these contracts and corresponding motion templates for different objects and task contexts. These contracts guide the perception module to ground task-relevant 3D primitives from observations, which are then used to instantiate reusable motion templates stored in a skill library. We evaluate ManiSkillFormer on Galaxea R1-Lite dual-arm robot across three settings: zero-shot pick-and-place over 8 object categories with 30 different instances, functional manipulation tasks including unscrewing, pouring, pressing, and folding, and 3 long-horizon tasks. ManiSkillFormer achieves higher average success rates than the evaluated baselines and two ablated pipelines: 88.24% for demonstration-free pick-and-place, 75.00% average success on functional manipulation and 50--80% completion rates across the long-horizon tasks. These results show that our design enables composable and reusable manipulation across objects and tasks without per-object policy fine-tuning or additional robot demonstrations.

</details>

---

### [[20_Research/Papers/机器人/Tendon-Driven_Continuum_Robot_with_Modular_Stiffness_and_In-Situ_Self_Pose_Estimation|Tendon-Driven Continuum Robot with Modular Stiffness and In-Situ Self Pose Estimation]]

![[assets/2609.16256_figure.png|800]]

- **arXiv**: [2609.16256](https://arxiv.org/abs/2609.16256)
- **PDF**: https://arxiv.org/pdf/2609.16256
- **详细分析**: [[20_Research/Papers/机器人/Tendon-Driven_Continuum_Robot_with_Modular_Stiffness_and_In-Situ_Self_Pose_Estimation|Tendon-Driven Continuum Robot with Modular Stiffness and In-Situ Self Pose Estimation]]
- **作者**: Guo Ning, Zheng Cao, Junzhe Hu, Xiangyun Bu, David Quinn, Tiancheng Wu, Zackory Erickson, Carmel Majidi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Tendon-Driven Continuum Robot with Modular Stiffness and In-Situ Self Pose Estimation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Continuum robots enable smooth shape morphing and safe interaction in confined environments. However, most existing systems are task-specific and depend on external sensing infrastructure, limiting their adaptability and real-world deployment. This paper presents a self-contained modular continuum robotic platform that combines mechanical reconfigurability with onboard pose estimation. The robot is constructed from interchangeable continuum joints with analytically precomputed stiffness, allowing rapid assembly and direct programming of the robot shape. Proprioceptive sensing is achieved using magnetic sensors and a modular learning-based framework, where a single model is trained per joint and reused across configurations. The system is experimentally validated in real world, demonstrating self-sensing capabilities and adaptation without external tracking.

</details>

---

### [[20_Research/Papers/机器人/Structure-Preserving_Quantum_Circuit_Architectures_for_Robot_Kinematics|Structure-Preserving Quantum Circuit Architectures for Robot Kinematics]]

![[assets/2609.16089_first_page.png|800]]

- **arXiv**: [2609.16089](https://arxiv.org/abs/2609.16089)
- **PDF**: https://arxiv.org/pdf/2609.16089
- **详细分析**: [[20_Research/Papers/机器人/Structure-Preserving_Quantum_Circuit_Architectures_for_Robot_Kinematics|Structure-Preserving Quantum Circuit Architectures for Robot Kinematics]]
- **作者**: Andrea Morghen, Pierluigi Arpenti, Roberto Schiattarella, Giovanni Acampora, Bruno Siciliano
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《Structure-Preserving Quantum Circuit Architectures for Robot Kinematics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Structured spatial data require quantum encodings that preserve geometric relations, expose measurable observables, and remain implementable on finite-depth hardware. This work introduces a quantum representation and circuit architecture for rigid-body transformations and specializes it to Denavit--Hartenberg kinematics of serial open-chain manipulators. Each translational contribution is factorized into a classical metric magnitude and a signed unit direction encoded by a single-qubit Bloch vector, while parameterized rotations reproduce the ordered propagation of frame directions. A selector register prepares probabilities proportional to the contribution magnitudes, and the reduced state of a designated readout qubit encodes their normalized weighted sum. The retained classical scale then reconstructs the metric end-effector position. Two additional readout qubits encode terminal-frame axes, providing a compact and geometrically interpretable pose interface. At the ideal expectation-value level, measured Pauli observables reproduce the corresponding classical kinematic quantities. Alternative circuit architectures realize the same representation with different tradeoffs in qubit count, circuit depth, controlled operations, and measurement requirements. Validation on a serial manipulator yields numerically negligible position and orientation reconstruction errors under ideal simulation. Finite-shot simulations, noisy executions, transpilation analysis, and a hardware demonstration further characterize statistical error, noise sensitivity, and implementation overhead without asserting computational advantage.

</details>

---

### [[20_Research/Papers/机器人/MR-GLi_Mixed_Reality-Based_Gripper-Linked_Overlays_for_Underwater_Robot_Arm_Teleoperation_via_Bilateral_Control|MR-GLi: Mixed Reality-Based Gripper-Linked Overlays for Underwater Robot Arm Teleoperation via Bilateral Control]]

![[assets/2609.16041_figure.png|800]]

- **arXiv**: [2609.16041](https://arxiv.org/abs/2609.16041)
- **PDF**: https://arxiv.org/pdf/2609.16041
- **详细分析**: [[20_Research/Papers/机器人/MR-GLi_Mixed_Reality-Based_Gripper-Linked_Overlays_for_Underwater_Robot_Arm_Teleoperation_via_Bilateral_Control|MR-GLi: Mixed Reality-Based Gripper-Linked Overlays for Underwater Robot Arm Teleoperation via Bilateral Control]]
- **作者**: Masashi Sasago, Masato Kobayashi, Yuki Uranishi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《MR-GLi: Mixed Reality-Based Gripper-Linked Overlays for Underwater Robot Arm Teleoperation via Bilateral Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual torque feedback supports underwater bilateral teleoperation, but the benefit of mixed reality (MR) over conventional monitor presentation remains unclear. We present MR-GLi, an MR interface that spatially registers a reaction torque indicator and wrist-camera image to the robot gripper. Twenty participants performed lift and pick-and-place tasks with rigid and compliant objects in a counterbalanced within-subject comparison with a 2D monitor, using identical visual-feedback content and four-channel bilateral control. MR-GLi provided gripper-linked access to visual feedback while maintaining a similar level of torque-regulation performance to the 2D monitor. Subjective evaluation further indicated reduced perceived burden associated with shifting attention between the workspace and visual feedback. These results demonstrate the feasibility of gripper-linked MR overlays for underwater bilateral teleoperation and highlight the importance of considering information access in addition to task performance. Additional material: this https URL

</details>

---
