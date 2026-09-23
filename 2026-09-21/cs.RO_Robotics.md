# cs.RO | Robotics | 2026-09-21

#arxiv #ComputerScience

**论文数**: 57

### [[20_Research/Papers/具身智能/SeeQ_Training_Generalist_Value_Functions_for_Long-Horizon_Robotic_Manipulation|SeeQ: Training Generalist Value Functions for Long-Horizon Robotic Manipulation]]

![[assets/2609.22085_figure.png|800]]

- **arXiv**: [2609.22085](https://arxiv.org/abs/2609.22085)
- **PDF**: https://arxiv.org/pdf/2609.22085
- **详细分析**: [[20_Research/Papers/具身智能/SeeQ_Training_Generalist_Value_Functions_for_Long-Horizon_Robotic_Manipulation|SeeQ: Training Generalist Value Functions for Long-Horizon Robotic Manipulation]]
- **作者**: Saksham Singh, Zheyuan Hu, Max Sobol Mark, Jeffrey Yu, Zackory Erickson, Aviral Kumar
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《SeeQ: Training Generalist Value Functions for Long-Horizon Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite rapid progress, generalist robot policies remain brittle on complex, long-horizon tasks that comprise multiple stages or require repeated attempts and deliberation on the same underlying stage before success. Q-value functions can improve these policies by ranking candidate actions or guiding policy improvement, but learning from sparse task-level rewards entails long credit-assignment horizons, difficult Bellman backups, and broad data-coverage requirements. We introduce SeeQ (Subtask-elicited Q-functions), which instead learns Q-values for the currently active subtask. This shortens the value-prediction horizon and enables effective learning with temporal-difference (TD) objectives. During training, subtask-level annotations present in offline robot data provide the decomposition and enable learning from broad, potentially suboptimal robot datasets. To eliminate the need for human annotations or modular subtask prediction systems at test time, our Q-function architecture is trained to autoregressively predict the active subtask in natural language before estimating its value. We instantiate SeeQ using a base vision-language backbone, pretrain it on diverse open-source robot manipulation data, and finetune it on downstream tasks. Across four real-world manipulation tasks on two bimanual robot platforms, the SeeQ value function substantially improves best-of-N policy steering.

</details>

---

### [[20_Research/Papers/具身智能/LIMBO_Learning_and_Internalizing_Model-Free_Barrier_Objectives_for_Agile_and_Safe_Whole-Body_Control|LIMBO: Learning and Internalizing Model-Free Barrier Objectives for Agile and Safe Whole-Body Control]]

![[assets/2609.22075_figure.png|800]]

- **arXiv**: [2609.22075](https://arxiv.org/abs/2609.22075)
- **PDF**: https://arxiv.org/pdf/2609.22075
- **详细分析**: [[20_Research/Papers/具身智能/LIMBO_Learning_and_Internalizing_Model-Free_Barrier_Objectives_for_Agile_and_Safe_Whole-Body_Control|LIMBO: Learning and Internalizing Model-Free Barrier Objectives for Agile and Safe Whole-Body Control]]
- **作者**: Jake Gonzales, Arturo Flores Alvarez, Yu-Ming Chen, Aaron D. Ames, Lillian J. Ratliff, Manikantan Nambi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《LIMBO: Learning and Internalizing Model-Free Barrier Objectives for Agile and Safe Whole-Body Control》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CBF-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe whole-body control requires coordinating collision avoidance and balance under high-dimensional, nonlinear dynamics--making safety certificates difficult to design and reuse across behaviors. We present LIMBO, a framework for synthesizing a state-action control barrier function and distilling its safety structure into a task policy. LIMBO learns the safety certificate from black-box transitions and a state-based failure specification over residual actions around a frozen base controller, making Q-CBF synthesis tractable in the full control dimension while placing the certificate in the task policy's control space. During synthesis, the learned safety value drives risk-guided sampling near the estimated boundary of recoverability; during task learning, it serves as a teacher that provides action-level safety feedback, yielding a robust task policy and alleviating the need for an online safety filter at deployment. We demonstrate LIMBO on a 29-degree-of-freedom humanoid performing dodgeball avoidance and locomotion beneath low obstacles. Beyond scaling learned Q-CBFs to whole-body control, we show that risk-guided boundary sampling provides a theoretically grounded way to explore the edge of recoverability. Under the same safety specification, ceteris paribus, varying the sampling concentration produces strategies ranging from crouching to a novel backward-leaning limbo maneuver. In both settings, the learned policies transfer to hardware without online safety filtering, showing that learned safety synthesis scales to agile whole-body control.

</details>

---

### [[20_Research/Papers/具身智能/Duty_Factor_Predicts_Robust_Constrained_Quadrupedal_Locomotion_Across_Gait_Types|Duty Factor Predicts Robust Constrained Quadrupedal Locomotion Across Gait Types]]

![[assets/2609.22073_figure.png|800]]

- **arXiv**: [2609.22073](https://arxiv.org/abs/2609.22073)
- **PDF**: https://arxiv.org/pdf/2609.22073
- **详细分析**: [[20_Research/Papers/具身智能/Duty_Factor_Predicts_Robust_Constrained_Quadrupedal_Locomotion_Across_Gait_Types|Duty Factor Predicts Robust Constrained Quadrupedal Locomotion Across Gait Types]]
- **作者**: James Zhu, David Ologan, George Ortiz, Thomas Chun Fai Lee, Selvin Garcia Gonzalez, Ardalan Tajbakhsh, Pinhas Ben-Tzvi, Aaron M. Johnson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Duty Factor Predicts Robust Constrained Quadrupedal Locomotion Across Gait Types》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadrupedal robots are increasingly deployed in environments where locomotion must remain robust to disturbances and constrained terrain. Gait type, such as walking or trotting, is commonly used to characterize quadrupedal locomotion. However, gait type does not uniquely define locomotion, as parameters such as duty factor, speed, and stance width can vary within a single gait type. In this work, we investigate the relationship between these gait parameters using three distinct quadrupedal locomotion control approaches. First, using whole body trajectory optimization with LQR feedback, we show that duty factor is a stronger predictor of local error convergence than nominal gait type. Second, we investigate duty factor selection with a learned locomotion controller, suggesting how duty factor may serve as a low-dimensional parameter for adapting locomotion robustness in narrow-terrain environments. Finally, we show that these trends persist under a centroidal model predictive control framework and validate them through narrow-terrain experiments on a physical quadruped. These results show that duty factor provides a simple and effective basis for understanding and selecting robust quadrupedal locomotion across gait types and control architectures.

</details>

---

### [[20_Research/Papers/具身智能/Gripper-Aware_Automatic_Dense_Packing_of_Irregular_Objects|Gripper-Aware Automatic Dense Packing of Irregular Objects]]

![[assets/2609.22062_figure.png|800]]

- **arXiv**: [2609.22062](https://arxiv.org/abs/2609.22062)
- **PDF**: https://arxiv.org/pdf/2609.22062
- **详细分析**: [[20_Research/Papers/具身智能/Gripper-Aware_Automatic_Dense_Packing_of_Irregular_Objects|Gripper-Aware Automatic Dense Packing of Irregular Objects]]
- **作者**: Tianhao Qin, Connor McCann, Berk Calli, Jing Xiao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Gripper-Aware Automatic Dense Packing of Irregular Objects》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automatic dense packing is widely desired in warehouse operations but remains a fundamental challenge in robotic manipulation. Existing work on irregular-object packing largely targets simulation with idealized contact, treating the object as an isolated rigid body. The gripper often enters as a discrete, post-hoc feasibility check, if considered at all, and the perception and contact drift accumulated during execution are not addressed. We present a closed-loop pipeline that integrates perception, gripper-aware placement optimization, and force-guided execution on a real manipulator. The optimizer represents the object together with the gripper as a single composite body of hierarchical sphere trees. It searches over five degrees of freedom on a GPU within a CMA-ES framework, with the vertical coordinate grounded analytically against the current heightmap. During execution, a force-monitored vertical descent stops on first contact. A post-release consolidation push then closes the residual lateral clearance that gripper-aware planning leaves behind. The container is re-perceived between placements so that drift does not accumulate. We validate the system on a Franka Emika Panda robot packing a 3D-printed set of flat, curved, and concave objects, and a YCB object subset. An ablation study isolates the contribution of gripper-aware optimization, the consolidation push, and mesh-derived geometry to end-to-end success, achieved density, and computational cost. We further benchmark against the heightmap-minimization method as a baseline representative of prior irregular-object packing work.

</details>

---

### [[20_Research/Papers/具身智能/CommitFlow_Semantic_Commitment_Verification_and_Local_Correction_for_Long-Horizon_Robot_Manipulation_VLA_Execution|CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution]]

![[assets/2609.21908_figure.png|800]]

- **arXiv**: [2609.21908](https://arxiv.org/abs/2609.21908)
- **PDF**: https://arxiv.org/pdf/2609.21908
- **详细分析**: [[20_Research/Papers/具身智能/CommitFlow_Semantic_Commitment_Verification_and_Local_Correction_for_Long-Horizon_Robot_Manipulation_VLA_Execution|CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution]]
- **作者**: Zixiang Zhao, Yansong Feng, Yang Yang, Chaoyu Wang, Haoran Xiao, Hui Zhang, Chuang Cheng, Jianjun Ma
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.8（加权：具身智能 2.7，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《CommitFlow: Semantic Commitment Verification and Local Correction for Long-Horizon Robot Manipulation VLA Execution》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CycleVLA, FPC-VLA, PhysReflect-VLA, RePO-VLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although vision-language-action (VLA) policies have advanced rapidly, long-horizon execution may still progress to the next task stage before the required physical effect has been established. We call this a mismatch between semantic commitments, physical conditions that a stage must establish or maintain, and the actual physical state. Because an action command alone cannot confirm such a condition, local deviations can propagate and cause task failure. To address this problem, we present CommitFlow, a closed-loop execution framework that combines commitment monitoring with local correction while keeping the base policy frozen. CommitFlow integrates three components. A Semantic Commitment Monitor (SCM) compares stage requirements against current state evidence and holds back dependent actions when a required condition is unmet or violated. BoundaryFlow then generates a local correction conditioned on the current state and base action, and Relation and Gain Calibration (RGC) selects the smallest correction strength that satisfies the relevant constraints. Across the ten common RoboTwin 2.0 benchmark tasks, CommitFlow achieves a mean success rate of 75.9 percent, improving on the base policy pi0.5 by 22.7 percent. Cross-policy experiments show consistent gains, pointing toward reliable long-horizon robot execution.

</details>

---

### [[20_Research/Papers/机器人/VIRGA_Virtual-Agent-Intermediated_Riemannian_Geometry_for_Active-Sensing_Air-Ground_Coordination|VIRGA: Virtual-Agent-Intermediated Riemannian Geometry for Active-Sensing Air-Ground Coordination]]

![[assets/2609.21883_figure.png|800]]

- **arXiv**: [2609.21883](https://arxiv.org/abs/2609.21883)
- **PDF**: https://arxiv.org/pdf/2609.21883
- **详细分析**: [[20_Research/Papers/机器人/VIRGA_Virtual-Agent-Intermediated_Riemannian_Geometry_for_Active-Sensing_Air-Ground_Coordination|VIRGA: Virtual-Agent-Intermediated Riemannian Geometry for Active-Sensing Air-Ground Coordination]]
- **作者**: Fenghe Guo, Runjie Shen, Chenyang Sun, Junrui Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.4，机器人 0.5）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《VIRGA: Virtual-Agent-Intermediated Riemannian Geometry for Active-Sensing Air-Ground Coordination》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Air-ground autonomy becomes harder when the unmanned aerial vehicle (UAV) must remain observable by a gimbal light detection and ranging (LiDAR) mounted on the unmanned ground vehicle (UGV). The platforms must avoid dynamic obstacles while coordinating heterogeneous motion, limited sensing, and changing task initiative within one closed loop. This paper presents VIRGA, a neural geometric coordination framework that turns dual-LiDAR observations into bounded source-specific Riemannian fields and couples them through a virtual agent with reciprocal elastic feedback. Platform-aware execution maps convert the shared coordination reference into feasible UAV, UGV, and gimbal commands while enforcing active-observation safeguards. Evaluation against three complementary baselines reveals distinct limitations. An adapted Ray-RMP controller provides the fastest Riemannian response but produces insufficient clearance in the coupled air-ground task. A dense analytical Riemannian field improves geometric avoidance, yet its high evaluation cost prevents stable field-of-view maintenance. An adapted ColAG controller achieves the lowest latency but still incurs safety and observability violations. VIRGA completes all paired warehouse conditions safely, while a long-range cave stress test without retraining demonstrates sustained coordination in irregular and confined geometry. Ablations confirm contributions from online geometric evaluation, virtual-agent mediation, and reciprocal feedback.

</details>

---

### [[20_Research/Papers/具身智能/PopNavShift_Stress-Testing_Social_Navigation_under_Behavioral_Population_Shift|PopNavShift: Stress-Testing Social Navigation under Behavioral Population Shift]]

![[assets/2609.21838_figure.png|800]]

- **arXiv**: [2609.21838](https://arxiv.org/abs/2609.21838)
- **PDF**: https://arxiv.org/pdf/2609.21838
- **详细分析**: [[20_Research/Papers/具身智能/PopNavShift_Stress-Testing_Social_Navigation_under_Behavioral_Population_Shift|PopNavShift: Stress-Testing Social Navigation under Behavioral Population Shift]]
- **作者**: Kaizhen Tan, Diyu Zheng, Tim Guangyu Wu, ChengHe Guan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型, 大模型
- **相关性评分**: 1.1（加权：具身智能 0.3，大模型 0.1，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, WorldModel

#### 研究背景与动机

《PopNavShift: Stress-Testing Social Navigation under Behavioral Population Shift》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：EWareNet, SocNavBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Social-navigation algorithms are often evaluated under a fixed pedestrian-behavior distribution, despite substantial variation in pedestrian responses to robots across individuals and social contexts. We introduce PopNavShift, a matched simulation framework for stress-testing social-navigation strategies under pedestrian population shifts. PopNavShift constructs population-conditioned pedestrian motion profiles by prompting Gemini 3.7 Flash with 600 synthetic persona records from MatrAIx Persona 1M and deterministically mapping the responses into bounded motion parameters. It then compares three representative navigation strategies, reactive avoidance, early yielding, and reciprocal collision avoidance, across eight population conditions and 7,488 matched robot runs. In a matched intervention on the same 202 personas, changing only time pressure reverses 8.6% of controller rankings based on robot travel time, but 22.4% based on mean pedestrian delay and 23.9% based on worst-decile delay. Across population conditions, this sensitivity is greater for pedestrian burden than for robot travel time and increases in spatially constrained settings; the same qualitative pattern persists under a second pedestrian dynamics model. These findings support evaluating navigation strategies across behavioral populations using both robot performance and pedestrian burden.

</details>

---

### [[20_Research/Papers/具身智能/A_Sim-to-Real_Integration_Pipeline_for_Training_and_Deployment_of_Chunk-Based_VLA_Manipulation_Policies|A Sim-to-Real Integration Pipeline for Training and Deployment of Chunk-Based VLA Manipulation Policies]]

![[assets/2609.21817_figure.png|800]]

- **arXiv**: [2609.21817](https://arxiv.org/abs/2609.21817)
- **PDF**: https://arxiv.org/pdf/2609.21817
- **详细分析**: [[20_Research/Papers/具身智能/A_Sim-to-Real_Integration_Pipeline_for_Training_and_Deployment_of_Chunk-Based_VLA_Manipulation_Policies|A Sim-to-Real Integration Pipeline for Training and Deployment of Chunk-Based VLA Manipulation Policies]]
- **作者**: Mathilde Kappel, Clémence Grislain, Mohamed Chetouani, Olivier Sigaud, Louis Annabi, Fa\"ız Ben Amar, Stéphane Doncieux, Mahdi Khoramshahi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.6（加权：具身智能 3，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《A Sim-to-Real Integration Pipeline for Training and Deployment of Chunk-Based VLA Manipulation Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have become a prominent paradigm for mapping multimodal inputs, including semantic instructions, visual observations of the scene, and proprioceptive observations, to robot actions. Most state-of-the-art models predict actions in the end-effector pose space as sequences of action chunks. Training and evaluating these models requires large-scale collections of real-world demonstrations, pairing robot actions with the corresponding visual and proprioceptive observations. Collecting such data on real hardware typically relies on human teleoperation, making the process costly, time-consuming, and difficult to scale. We present an open-source sim-to-real experimental protocol that addresses this bottleneck: expert trajectories generated in simulation are replayed open-loop on a real Franka FR3 setup, where the corresponding real visual and proprioceptive observations are recorded and converted into a format compatible with VLA training. The same deployment stack is then reused, in closed-loop, to evaluate a trained policy on that setup, so that data collection and evaluation share an identical hardware configuration. Because each real recording is paired with the simulated trajectory that produced it, the protocol also yields a direct measurement of the sim-to-real gap. We release the collected datasets on Hugging Face together with the pipeline source code this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Contact-Rich_Motion_Planning_via_GPU-Parallel_Mode_Evaluation|Contact-Rich Motion Planning via GPU-Parallel Mode Evaluation]]

![[assets/2609.21803_figure.png|800]]

- **arXiv**: [2609.21803](https://arxiv.org/abs/2609.21803)
- **PDF**: https://arxiv.org/pdf/2609.21803
- **详细分析**: [[20_Research/Papers/具身智能/Contact-Rich_Motion_Planning_via_GPU-Parallel_Mode_Evaluation|Contact-Rich Motion Planning via GPU-Parallel Mode Evaluation]]
- **作者**: Jiayun Li, Georgia Chalvatzaki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Contact-Rich Motion Planning via GPU-Parallel Mode Evaluation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PEARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich motion planning (CRMP) is essential for robotic manipulation and locomotion, yet remains computationally challenging due to combinatorial contact decisions. Existing methods typically avoid broad evaluation of contact-mode sequences through search heuristics or optimization reformulations. We revisit broad evaluation in light of modern GPU hardware and introduce Contact-Mode Expansion with parallel Trajectory optimization (CoMET), which combines GPU-parallel trajectory evaluation with greedy contact-mode expansion. On planar pushing benchmarks, CoMET is competitive with optimization-based, sampling, and tree-search baselines in solution quality and planning time, matching the full-enumeration reference on nearly all instances with fewer evaluations and shorter planning times. Ablations suggest that much of the performance gain comes from the high-throughput trajectory evaluator. In bimanual nonprehensile manipulation, GPU-friendly local mode expansion achieves higher planning success than the tested adaptive tree search as the mode space grows. These results demonstrate that broad explicit mode evaluation provides a simple yet effective alternative for CRMP.

</details>

---

### [[20_Research/Papers/具身智能/AcousticDiffusion_Semantically_Conditioned_Audio-Guided_Diffusion_Policy_for_Search-and-Rescue_Assistance|AcousticDiffusion: Semantically Conditioned Audio-Guided Diffusion Policy for Search-and-Rescue Assistance]]

![[assets/2609.21792_figure.png|800]]

- **arXiv**: [2609.21792](https://arxiv.org/abs/2609.21792)
- **PDF**: https://arxiv.org/pdf/2609.21792
- **详细分析**: [[20_Research/Papers/具身智能/AcousticDiffusion_Semantically_Conditioned_Audio-Guided_Diffusion_Policy_for_Search-and-Rescue_Assistance|AcousticDiffusion: Semantically Conditioned Audio-Guided Diffusion Policy for Search-and-Rescue Assistance]]
- **作者**: Iana Zhura, Didar Seyidov, Dmitrii Plotnikov, Hajira Amjad, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《AcousticDiffusion: Semantically Conditioned Audio-Guided Diffusion Policy for Search-and-Rescue Assistance》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：AudioSet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigating toward human callers is an important capability for rescue robots operating where visual contact is degraded or occluded. We present AcousticDiffusion, a semantically conditioned, audio-guided diffusion policy for human-directed navigation. A frozen pretrained audio recognizer processes 10.24 s windows, with speech gating and distress-aware prioritization converting recognition outputs into source-level navigation roles. Microphone-array direction-of-arrival measurements are recursively integrated into a robot-centric Bayesian bird's-eye-view belief field. Ego-motion compensation aligns successive observations, progressively constraining source position while preserving bearing-induced range uncertainty. The semantic belief, recent acoustic observations, audio features, and robot state condition a diffusion model that generates waypoint trajectories. On a synthetic-navigation validation set using recorded audio, AcousticDiffusion achieves a mean end-point bearing error of 11.20 degrees, with 91.78% of trajectories aligned within 30 degrees of the caller. Distractor rejection ranges from 89.20% to 98.99%, and the policy favors a HELP-designated caller over a competing speaker in 91.07% of windows. Deployed online on a ZSL-1 quadruped without additional retraining, it achieves a mean bearing error of 64.9 degrees, compared with 98.2 degrees for A* and 90.4 degrees for RRT, with a mean planner compute time of 6.07 ms. Despite imperfect acoustic localization, the reported mean final source distance is reduced from 3.96 m for the classical planners using ODAS-derived (Open embedded Audition System) guidance to 2.48 m, a 37.4% improvement. These results demonstrate the framework's ability to translate uncertain acoustic observations into closer approaches to human callers.

</details>

---

### [[20_Research/Papers/世界模型/Compact_but_Moving_Intervention-Relevant_Geometry_in_Recurrent_World_Models|Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models]]

![[assets/2609.21787_first_page.png|800]]

- **arXiv**: [2609.21787](https://arxiv.org/abs/2609.21787)
- **PDF**: https://arxiv.org/pdf/2609.21787
- **详细分析**: [[20_Research/Papers/世界模型/Compact_but_Moving_Intervention-Relevant_Geometry_in_Recurrent_World_Models|Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models]]
- **作者**: Yuming Chen, Yang Liu
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: WorldModel, ComputerVision

#### 研究背景与动机

《Compact but Moving: Intervention-Relevant Geometry in Recurrent World Models》归入 世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learned world models may have compact interventions even when their recurrent state is high-dimensional, but it is unclear what happens to such a correction after it enters the model. We study this question in a controlled recurrent world model where prior work identified a checkpoint-specific rank-4 interface for one-shot counterfactual velocity interventions. The correction rapidly leaves this fixed entry subspace during autonomous rollout. Nevertheless, a low-rank image obtained by transporting the entry directions through the factual recurrent Jacobian chain continues to capture most of the nonlinear correction. Restarts using the tangent-predicted correction preserve substantial counterfactual future function. This transport/function pattern recurs across independently trained structured-GRU models and a parameter-matched LSTM initialized with a privileged compact correction. We further characterize a finite-horizon future-response operator over the full recurrent carrier. Patching shifts its leading future-sensitive directions toward the matched native-counterfactual organization, and the local operator accurately ranks finite perturbation effects over the registered direction panels at the patched and native-counterfactual basepoints. A separate full-amplitude assay finds substantial factual-endpoint tangent residuals and supports response reconfiguration in two of three checkpoints. Together, these results show that compact intervention structure can persist as a moving, state-dependent local geometry embedded in high-dimensional recurrent dynamics, without implying a fixed or dynamically closed low-dimensional state.

</details>

---

### [[20_Research/Papers/机器人/TRACE_Coverage_Path_Planning_for_Unknown_Environments_Using_Hierarchical_Coverage_Tree|TRACE: Coverage Path Planning for Unknown Environments Using Hierarchical Coverage Tree]]

![[assets/2609.21777_figure.png|800]]

- **arXiv**: [2609.21777](https://arxiv.org/abs/2609.21777)
- **PDF**: https://arxiv.org/pdf/2609.21777
- **详细分析**: [[20_Research/Papers/机器人/TRACE_Coverage_Path_Planning_for_Unknown_Environments_Using_Hierarchical_Coverage_Tree|TRACE: Coverage Path Planning for Unknown Environments Using Hierarchical Coverage Tree]]
- **作者**: Zongyuan Shen, Haodong Liu, Gao Wang, Shancheng Zhao, Dehua Zhou, Yaming Ou, Zhongqiang Ren, Yikui Zhai, C. L. Philip Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《TRACE: Coverage Path Planning for Unknown Environments Using Hierarchical Coverage Tree》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a novel online coverage path planning (CPP) algorithm, called TRACE, for real-time coverage of unknown environments. TRACE is built upon a hierarchical coverage tree that provides a global representation of the evolving connectivity of the uncovered space. As the environment is incrementally revealed and covered, newly discovered obstacles and covered cells may fragment the remaining uncovered space into disconnected regions. TRACE recursively expands the corresponding tree nodes to explicitly represent these regions and organize them for subsequent coverage planning. Based on the updated tree, an incremental global tour is maintained to guide the coverage process. TRACE locally refines only the affected portions while preserving the visiting order of unchanged regions, thereby reducing the computational burden of global replanning and maintaining a consistent coverage progression. Guided by the global tour, a local planner generates back-and-forth coverage paths and switches to global-tour-aware planning to efficiently complete the target regions. Theoretical analysis establishes the computational complexity and complete coverage property of TRACE, and derives an approximation bound for the incremental global tour refinement. The performance of TRACE is evaluated through extensive high-fidelity simulations and real-robot experiments using a mobile robot. Comparative evaluations against six existing CPP methods demonstrate significant improvements in coverage time, path length, overlap ratio, and number of turns.

</details>

---

### [[20_Research/Papers/具身智能/Scaling_Vision-Language_Reward_Learning_for_Robot_Manipulation_in_Parallel_Simulation|Scaling Vision-Language Reward Learning for Robot Manipulation in Parallel Simulation]]

![[assets/2609.21767_figure.png|800]]

- **arXiv**: [2609.21767](https://arxiv.org/abs/2609.21767)
- **PDF**: https://arxiv.org/pdf/2609.21767
- **详细分析**: [[20_Research/Papers/具身智能/Scaling_Vision-Language_Reward_Learning_for_Robot_Manipulation_in_Parallel_Simulation|Scaling Vision-Language Reward Learning for Robot Manipulation in Parallel Simulation]]
- **作者**: Lobna Joualy, Eric Demeester, Nikolaos Tsiogkas
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.2，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Scaling Vision-Language Reward Learning for Robot Manipulation in Parallel Simulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IsaacGym, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) can replace human annotators in preference-based reward learning, but sequential API requests and single-environment data collection make training slow and costly. We present RAPID (Reward learning with Adaptive Parallel Image Diversity), a system that couples GPU-parallel rollout with data-aware policy updates, single-request preference labeling, automatic reward stabilization, and representative image sampling. We evaluate these components on five Franka Panda manipulation tasks in IsaacLab. Parallel rollout and adaptive updates provide the first substantial reduction in training time: under matched two-stage prompting, mean runtime falls from 9.18 to 3.13 hours. With all RAPID components enabled, training completes in 1.15 hours using 896 rather than 19,840 API calls per run, and aggregate final success rises from 86.3\% to 98.7\%. This represents an 8.0$\times$ end-to-end speedup and a 95.5\% reduction in API usage. An offline evaluation with Gemma~3 12B and GPT-4.1 mini demonstrates that single-request prompting reduces labeling latency and cost across both models. Code is available at: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/CRISP_Contact-Rich_Robotic_Simulation_Platform_with_Extensive_Geometries_and_Contact_Solvers|CRISP: Contact-Rich Robotic Simulation Platform with Extensive Geometries and Contact Solvers]]

![[assets/2609.21761_figure.png|800]]

- **arXiv**: [2609.21761](https://arxiv.org/abs/2609.21761)
- **PDF**: https://arxiv.org/pdf/2609.21761
- **详细分析**: [[20_Research/Papers/具身智能/CRISP_Contact-Rich_Robotic_Simulation_Platform_with_Extensive_Geometries_and_Contact_Solvers|CRISP: Contact-Rich Robotic Simulation Platform with Extensive Geometries and Contact Solvers]]
- **作者**: Somang Lee, Sunkyung Park, Jinhee Yun, Seoki An, Dongjun Lee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《CRISP: Contact-Rich Robotic Simulation Platform with Extensive Geometries and Contact Solvers》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：RaiSim, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present CRISP (Contact-RIch Simulation Platform), a high-fidelity physics engine tailored for complex multi-contact simulations such as tight-tolerance robotic manipulation. Achieving high physical fidelity in robotic simulation requires both expressive modeling of geometry and contact interactions, as well as accurate numerical resolution via robust collision detection and contact solvers. However, existing simulators often either rely on limited support for geometric representations and simplified modeling of contact interactions, or employ numerical resolution methods whose accuracy or robustness is inherently constrained. Accordingly, we develop a new simulator that supports diverse geometric representations with accurate optimization-based collision detection, and combines contact modeling with robust augmented Lagrangian-based contact solvers. This integration enables efficient and consistent detection of contact information across complex geometries while accurately resolving multi-contact constraints without problematic relaxations, which is essential for simulating contact-intensive and sharp interactions. We validate the physical fidelity of our simulator against state-of-the-art platforms and further demonstrate its capabilities through complex robotic manipulation scenarios. CRISP is publicly available at this https URL .

</details>

---

### [[20_Research/Papers/具身智能/PSR_Predictive_Sensorimotor_Representation_Learning_for_Contact-Rich_Manipulation|PSR: Predictive Sensorimotor Representation Learning for Contact-Rich Manipulation]]

![[assets/2609.21753_figure.png|800]]

- **arXiv**: [2609.21753](https://arxiv.org/abs/2609.21753)
- **PDF**: https://arxiv.org/pdf/2609.21753
- **详细分析**: [[20_Research/Papers/具身智能/PSR_Predictive_Sensorimotor_Representation_Learning_for_Contact-Rich_Manipulation|PSR: Predictive Sensorimotor Representation Learning for Contact-Rich Manipulation]]
- **作者**: Shengbao Li, Peng Xu, Chao Tang, Hao Wei, Jiaheng Wang, Hong Yin, Jiangtao Chen, Jinxuan Zhu, Zhong Zhou, Mengfan Wang, Tingguang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.9，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PSR: Predictive Sensorimotor Representation Learning for Contact-Rich Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：CoT-VLA, DreamTacVLA, ForceVLA, JEPA-VLA, PSR-VLA, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Contact-rich manipulation requires policies to generate precise actions by reasoning over contact forces, robot configurations, and interaction histories beyond visual observations. Existing methods passively condition on force feedback rather than actively predicting future contact dynamics, limiting their ability to generate high-precision actions. To address this problem, we introduce Predictive Sensorimotor Representation (PSR) learning, a framework that learns a hierarchy of predictive representations from multimodal sensorimotor signals and integrates them into the action stream of a visuomotor policy. Specifically, during a pretraining stage, a multimodal Transformer is trained to learn a hierarchy of predictive representations by jointly forecasting future interaction dynamics. The learned hierarchy subsequently augments the action stream, enabling the resulting policy to exploit contact-relevant cues at multiple depths. We further instantiate PSR within a Vision-Language-Action (VLA) model, resulting in PSR-VLA, and evaluate it on six real-world contact-rich manipulation tasks. Experimental results show that PSR-VLA achieves 91.7% overall success, improving over $\pi_{0.5}$, ForceVLA-$\pi_{0.5}$, and ForceVLA2-$\pi_{0.5}$ by 30.0, 22.5, and 19.2 percentage points, respectively. These results demonstrate the effectiveness of the proposed PSR for force-aware, contact-rich manipulation. Videos of the tasks and stability tests are available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/Understanding_Engagement_and_Intrusiveness_in_Assistive_Human-Robot_Interaction_Using_Individual_Traits|Understanding Engagement and Intrusiveness in Assistive Human-Robot Interaction Using Individual Traits]]

![[assets/2609.21744_figure.jpg|800]]

- **arXiv**: [2609.21744](https://arxiv.org/abs/2609.21744)
- **PDF**: https://arxiv.org/pdf/2609.21744
- **详细分析**: [[20_Research/Papers/机器人/Understanding_Engagement_and_Intrusiveness_in_Assistive_Human-Robot_Interaction_Using_Individual_Traits|Understanding Engagement and Intrusiveness in Assistive Human-Robot Interaction Using Individual Traits]]
- **作者**: Valerio Bo, Lavinia Hriscu, Alberto Sanfeliu, Anaís Garrell
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Understanding Engagement and Intrusiveness in Assistive Human-Robot Interaction Using Individual Traits》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot assistance is particularly crucial in unfamiliar tasks, where users must understand task requirements while coordinating with the robot. Previous research offers mixed evidence on the role of robot proxemics in user engagement: some studies suggest closer proximity enhances interaction, while others report it can feel intrusive. In this work, we argue that perceptions of intrusiveness depend not only on proxemics but also on the frequency of robot interventions, and are strongly influenced by individual traits such as personality and demographics. We conducted an experiment with 32 participants who interacted with two assistive robots that provided similar task support but differed in their intervention strategies. Results indicate that overall engagement remains stable across conditions, yet affective responses and perceived intrusiveness vary significantly with personality traits. Moreover, personality shapes interaction dynamics differently depending on the robot's behavior. These findings emphasize that effective human-robot interaction should account for individual differences, tailoring robot behavior to maintain engagement while respecting each user's unique affective and behavioral profile.

</details>

---

### [[20_Research/Papers/世界模型/Sandwich-Residuals_Parameter-Efficient_Test-time_Adaptation_of_World_Models|Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models]]

![[assets/2609.21740_figure.png|800]]

- **arXiv**: [2609.21740](https://arxiv.org/abs/2609.21740)
- **PDF**: https://arxiv.org/pdf/2609.21740
- **详细分析**: [[20_Research/Papers/世界模型/Sandwich-Residuals_Parameter-Efficient_Test-time_Adaptation_of_World_Models|Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models]]
- **作者**: Krishnam Soni, Aditya Sehgal, Vedant Dave, Elmar Rueckert
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 1.0（加权：世界模型 1）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Sandwich-Residuals: Parameter-Efficient Test-time Adaptation of World Models》归入 世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：AdaWorld, OGBench, ResNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Latent world models enable planning by predicting the effects of actions in a learned representation space, but their predictions can become unreliable when test-time conditions differ from training. Existing test-time adaptation methods address this by updating parts of the pretrained model, often modifying millions of parameters and requiring a choice of which internal components to adapt. We introduce Sandwich-Residuals, a lightweight alternative that keeps the pretrained world model frozen and learns only small residual corrections around the predictor. The residuals are optimized online using the model's self-supervised prediction error and require no rewards, labels, or source-domain data. Across 21 conditions on the AdaJEPA benchmark, our method achieves $1.3\times$ the success rate of the frozen model while retaining 95% of the performance of the strongest AdaJEPA variant and adapting 97-99% fewer parameters. Under compound shifts, this advantage increases to $1.9\times$ the success rate of the frozen model, while remaining comparable to internal block adaptation. We further demonstrate the same adaptation principle on a DINO-WM model for 3-D manipulation. These results suggest that effective test-time adaptation of world models does not necessarily require modifying their pretrained internal weights.

</details>

---

### [[20_Research/Papers/大模型/When_Should_Robots_Intervene_Balancing_Engagement_and_Intrusiveness_in_Human-Robot_Interaction|When Should Robots Intervene? Balancing Engagement and Intrusiveness in Human-Robot Interaction]]

![[assets/2609.21734_figure.jpg|800]]

- **arXiv**: [2609.21734](https://arxiv.org/abs/2609.21734)
- **PDF**: https://arxiv.org/pdf/2609.21734
- **详细分析**: [[20_Research/Papers/大模型/When_Should_Robots_Intervene_Balancing_Engagement_and_Intrusiveness_in_Human-Robot_Interaction|When Should Robots Intervene? Balancing Engagement and Intrusiveness in Human-Robot Interaction]]
- **作者**: Lavinia Hriscu, Valerio Bo, Alberto Sanfeliu, Anaís Garrell
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《When Should Robots Intervene? Balancing Engagement and Intrusiveness in Human-Robot Interaction》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Designing effective Human-Robot Interaction in task-oriented settings requires carefully balancing user engagement with socially acceptable levels of robot intrusiveness. In this paper, we examine how different robot intervention strategies shape user experience, interaction dynamics, perceived intrusiveness, and sense of support. We compare two approaches: a continuous engagement-seeking robot strategy, and a context-aware strategy that selectively intervenes based on the user's state and task context. Both approaches rely on multimodal behavioral cues, including body orientation and attentional signals, to guide robot actions. We evaluate these strategies in a user study with 32 participants performing a task in a simulated hospital environment. Our findings show that higher interaction frequency does not necessarily lead to better engagement. Instead, we observe a systematic trade-off between perceived support and intrusiveness, influenced by factors such as physical proximity and user effort. These results provide empirical evidence that effective engagement in HRI depends on adaptive, context-sensitive intervention policies.

</details>

---

### [[20_Research/Papers/机器人/Visual_Proactivity_Enhancing_Human-Robot_Collaboration_Through_Intent_Communication|Visual Proactivity: Enhancing Human-Robot Collaboration Through Intent Communication]]

![[assets/2609.21729_figure.jpg|800]]

- **arXiv**: [2609.21729](https://arxiv.org/abs/2609.21729)
- **PDF**: https://arxiv.org/pdf/2609.21729
- **详细分析**: [[20_Research/Papers/机器人/Visual_Proactivity_Enhancing_Human-Robot_Collaboration_Through_Intent_Communication|Visual Proactivity: Enhancing Human-Robot Collaboration Through Intent Communication]]
- **作者**: Valerio Bo, Edison Bejarano, Anaís Garrell, Alberto Sanfeliu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Visual Proactivity: Enhancing Human-Robot Collaboration Through Intent Communication》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

As robots transition from performing repetitive tasks to collaborating with humans, understanding human intent becomes crucial to effective interaction. Anticipation enables robots to predict human actions, while proactivity allows them to take initiative and guide human behavior toward optimal outcomes. Although research has largely focused on how robots infer and respond to human intentions, less attention has been paid to how robots communicate their own intent. This paper introduces visual proactivity, a novel, simple yet effective approach that enables robots to communicate their intentions through visual feedback, influencing human behavior and enhancing transparency and fluency. We develop and evaluate proactive robotic behaviors in a human-to-robot handover scenario, where a user study validates human perception of reactive, anticipatory, and proactive behaviors. The results demonstrate that effective visual proactivity fosters better alignment and coordination, paving the way for more intuitive human-robot collaboration.

</details>

---

### [[20_Research/Papers/具身智能/ZeroTouch_Tactile-Supervised_Visual_Contact_Estimation_for_Contact-Rich_Manipulation|ZeroTouch: Tactile-Supervised Visual Contact Estimation for Contact-Rich Manipulation]]

![[assets/2609.21726_figure.png|800]]

- **arXiv**: [2609.21726](https://arxiv.org/abs/2609.21726)
- **PDF**: https://arxiv.org/pdf/2609.21726
- **详细分析**: [[20_Research/Papers/具身智能/ZeroTouch_Tactile-Supervised_Visual_Contact_Estimation_for_Contact-Rich_Manipulation|ZeroTouch: Tactile-Supervised Visual Contact Estimation for Contact-Rich Manipulation]]
- **作者**: Dmitriy Kosenkov, Daniia Zinniatullina, Miguel Altamirano Cabrera, Iana Zhura, Mikhail Derevianchenko, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《ZeroTouch: Tactile-Supervised Visual Contact Estimation for Contact-Rich Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic grasping benefits from estimating the evolving physical interaction and selecting a grasp-dependent compression target. Tactile sensors provide direct interaction measurements but require dedicated hardware at deployment. We introduce ZeroTouch, a tactile-supervised framework that predicts dense contact deformation, the instantaneous six-axis wrench, and a grasp-dependent desired compression target from wrist RGB observations, gripper state, and local gravity direction. Tactile measurements are used only as privileged supervision during training and are not required at deployment. On the full validation set, the complete architecture reduces normal-force MAE from 2.017 N for a state-only baseline to 0.531 N. In physical evaluation with 20 trials per condition, ZeroTouch achieves 95% success on an unseen object, 80% in a seen-object/unseen-grasp condition, and 90% under a content/load shift. Under the same evaluation protocol, OpenVLA achieves 25%, 40%, and 55%, while SmolVLA achieves 10%, 25%, and 35%, respectively.

</details>

---

### [[20_Research/Papers/机器人/AgenticSwarm_Semantic_Perception_and_Adaptive_Task_Allocation_for_Heterogeneous_Multi-UAV_Missions|AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions]]

![[assets/2609.21716_figure.png|800]]

- **arXiv**: [2609.21716](https://arxiv.org/abs/2609.21716)
- **PDF**: https://arxiv.org/pdf/2609.21716
- **详细分析**: [[20_Research/Papers/机器人/AgenticSwarm_Semantic_Perception_and_Adaptive_Task_Allocation_for_Heterogeneous_Multi-UAV_Missions|AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions]]
- **作者**: Muhammad Ahsan Mustafa, Yasheerah Yaqoot, Faryal Batool, Roohan Ahmed Khan, Valerii Serpiva, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Systems

#### 研究背景与动机

《AgenticSwarm: Semantic Perception and Adaptive Task Allocation for Heterogeneous Multi-UAV Missions》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi UAV missions in complex environments require the system to understand both the surrounding scene and the intent of a human operator while maintaining feasible task allocation as mission conditions change. This paper presents AgenticSwarm, an agentic framework for semantic perception and adaptive task allocation in heterogeneous multi UAV missions. An agent interprets aerial imagery and natural language instructions to construct a grounded mission representation that links perceived objects and regions with task requirements, capability constraints, and mission dependencies. This information augments a constrained task allocation process in which obstacle aware path feasibility, energy consumption, and protected return home requirements are incorporated before assignment. During execution, changes such as UAV failure, battery degradation, or task modification trigger residual mission reconstruction from the current system state, while completed work and reconnaissance progress are retained. AgenticSwarm is evaluated across five diverse Gazebo environments and an indoor real test environment, demonstrating its ability to connect semantic reasoning with constrained allocation and adaptive multi UAV mission execution. Compared with a Grounding DINO+SAM~2.1 perception baseline, the SAM3-based pipeline improves class-aware recall by 25.2 percentage points (pp) and semantic label accuracy by 29.5 pp. Ablating residual mission replanning increases mean repeated work from 0% to 61.7% and post-event recovery time by 58.6%, highlighting the contribution of adaptive replanning to mission execution.

</details>

---

### [[20_Research/Papers/机器人/NeuRIO_A_Streaming_Neural_Estimator_for_Zero-Shot_Sim-to-Real_Multi-Robot_Relative_Inertial_Odometry|NeuRIO: A Streaming Neural Estimator for Zero-Shot Sim-to-Real Multi-Robot Relative Inertial Odometry]]

![[assets/2609.21707_figure.jpg|800]]

- **arXiv**: [2609.21707](https://arxiv.org/abs/2609.21707)
- **PDF**: https://arxiv.org/pdf/2609.21707
- **详细分析**: [[20_Research/Papers/机器人/NeuRIO_A_Streaming_Neural_Estimator_for_Zero-Shot_Sim-to-Real_Multi-Robot_Relative_Inertial_Odometry|NeuRIO: A Streaming Neural Estimator for Zero-Shot Sim-to-Real Multi-Robot Relative Inertial Odometry]]
- **作者**: Zhehan Li, Jiadong Lu, Shengwei Ren, Chao Xu, Yanjun Cao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《NeuRIO: A Streaming Neural Estimator for Zero-Shot Sim-to-Real Multi-Robot Relative Inertial Odometry》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoViS-Net, MatchNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present NeuRIO, a streaming neural estimator for anchor-free 6-DoF relative inertial odometry using only identified inter-robot bearings, ranges, and IMU measurements. NeuRIO canonicalizes measurements into gravity-aligned coordinates, represents robots as nodes and mutual observations as factors, and uses attention for spatial reasoning and GRUs for temporal modeling. As a graph network, NeuRIO applies shared node-wise and factor-wise operators throughout the network, enabling it to handle different team sizes and time-varying observation graphs. NeuRIO is trained on a simulator that couples various motion patterns, device-level sensor characteristics, and diverse, realistic modeled, and temporally persistent sensor corruptions. In this way, NeuRIO achieves zero-shot sim-to-real transfer. Across $24$ real-world sequences, NeuRIO achieves $14.1\,\mathrm{cm}$ position RMSE and $3.9^\circ$ rotation RMSE. More importantly, NeuRIO demonstrates strong computational scalability, maintaining an update cost below $20\,\mathrm{ms}$ with up to $400$ robots in simulation, while optimization-based methods exceed $20\,\mathrm{ms}$ at only $24$ robots. Moreover, even trained on limited team sizes, NeuRIO transfers directly to unseen larger teams without architectural or parameter changes.

</details>

---

### [[20_Research/Papers/机器人/RAYA_Learning_Where_and_When_to_Intervene_for_Robot_Recovery|RAYA: Learning Where and When to Intervene for Robot Recovery]]

![[assets/2609.21690_figure.png|800]]

- **arXiv**: [2609.21690](https://arxiv.org/abs/2609.21690)
- **PDF**: https://arxiv.org/pdf/2609.21690
- **详细分析**: [[20_Research/Papers/机器人/RAYA_Learning_Where_and_When_to_Intervene_for_Robot_Recovery|RAYA: Learning Where and When to Intervene for Robot Recovery]]
- **作者**: Ishaan Mahajan, Charles Chen, Frederike Dümbgen, Brian Plancher
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《RAYA: Learning Where and When to Intervene for Robot Recovery》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A robot can predict failure and still be unable to prevent it. By the time a safety mechanism reacts, the nominal plan may already have spent the control authority that recovery requires, and fixed task priorities may block whatever response remains. Our key insight is that both aspects are decided inside the controller. Recoverability must inform actions while they are chosen rather than veto them afterward, and task objectives must be adapted as recoverability shrinks. Building on this, we present RAYA, a hybrid learned-analytic framework that places a learned finite-horizon recoverability margin inside an optimal controller with hard constraints and pairs it with a bounded learned scheduler that shifts task weights to facilitate recovery. Across 7,200 simulation episodes per controller spanning quadrotor and autonomous-vehicle benchmarks, RAYA not only improves survival rates, but also transfers the learned components zero-shot to unseen trajectories, disturbances, plant shifts, and friction layouts. We developed an embedded realization of RAYA and deployed it on-board a 35g Crazyflie quadrotor. Across 40 combined hardware flights under wind with either aerodynamic mismatch or an unmodeled 40% motor-command loss, each of three baselines fails in all trials, while RAYA completes 10/10 six-cycle missions. Project Website: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/A_High-Payload_Wall-Climbing_Robot_Using_Passive_Bistable_Suction_Cups|A High-Payload Wall-Climbing Robot Using Passive Bistable Suction Cups]]

![[assets/2609.21584_figure.jpeg|800]]

- **arXiv**: [2609.21584](https://arxiv.org/abs/2609.21584)
- **PDF**: https://arxiv.org/pdf/2609.21584
- **详细分析**: [[20_Research/Papers/具身智能/A_High-Payload_Wall-Climbing_Robot_Using_Passive_Bistable_Suction_Cups|A High-Payload Wall-Climbing Robot Using Passive Bistable Suction Cups]]
- **作者**: Andrew Nguyen, Mingyuan Li, Daniel Bruder
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A High-Payload Wall-Climbing Robot Using Passive Bistable Suction Cups》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Wall-climbing robots capable of scaling vertical surfaces could help automate hazardous or labor intensive tasks such as window washing, inspection, maintenance, and construction. Active adhesion methods achieve higher payload capacities, but require power to maintain their grip. Passive adhesion devices such as suction cups are an attractive option for such robots because they do not require power to maintain their grip, but they are limited by their payload capacity. This work presents a novel high-payload wall-climbing robot that utilizes passive bistable suction cups to generate adhesion without needing to be pushed into the wall. The robot features a track-based system that automatically engages and disengages bistable suction cups to achieve locomotion on smooth surfaces. The robot is able to achieve vertical wall climbing on glass, wood, metal, and painted surfaces, sideways and upside-down climbing, and is able to tow a payload of 7.940 kg (with a payload-to-weight ratio of 2.25).

</details>

---

### [[20_Research/Papers/具身智能/SABER_Learning_Attention-based_Semantic_Affordance_for_Legged_Locomotion|SABER: Learning Attention-based Semantic Affordance for Legged Locomotion]]

![[assets/2609.21572_figure.jpg|800]]

- **arXiv**: [2609.21572](https://arxiv.org/abs/2609.21572)
- **PDF**: https://arxiv.org/pdf/2609.21572
- **详细分析**: [[20_Research/Papers/具身智能/SABER_Learning_Attention-based_Semantic_Affordance_for_Legged_Locomotion|SABER: Learning Attention-based Semantic Affordance for Legged Locomotion]]
- **作者**: Hari Prasanth Palanivelu, Samuel Sze, Kennard Garrison Johannes, Albertus Hendrawan Adiwahono, Meng Yee, Chuah
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.8，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《SABER: Learning Attention-based Semantic Affordance for Legged Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Perceptive legged locomotion has advanced rapidly by integrating terrain geometry into learned policies, yet the integration of terrain meaning remains sparse: a pipe, a patch of grass, or a fragile box may be geometrically traversable while being inappropriate for contact. In industrial environments, where legged robots increasingly operate, a single misplaced step can damage fragile equipment, destabilize the robot, or endanger the site. To address this, we introduce SABER, a planner-free reinforcement-learning policy that jointly reasons about terrain geometry and semantic contact permission. The policy consumes a unified terrain-affordance map, where each cell encodes local 3D geometry and a semantic contact cost. We augment cross-attention with a learned, signed semantic bias: an additive term on the attention logits, gated by the contact cost, that reweights flagged cells by their distance from the nearest foot. A hazard therefore reshapes attention where it can still affect the next foothold, and its influence fades where it cannot. The resulting policy selects footholds on permitted support and keeps the leg clear of forbidden regions throughout the swing phase. We perform a systematic ablation that isolates the contribution of each architectural component; removing the semantic bias alone increases forbidden contacts by 55% while velocity tracking is unchanged. We validate the policy on a Unitree B2, demonstrating sim-to-real semantic contact selection across indoor and outdoor environments and four semantic obstacle classes.

</details>

---

### [[20_Research/Papers/具身智能/Skel-WAM_A_Hand-Skeleton-Conditioned_World_Action_Model_for_Human-to-Robot_Manipulation_Transfer|Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer]]

![[assets/2609.21514_figure.png|800]]

- **arXiv**: [2609.21514](https://arxiv.org/abs/2609.21514)
- **PDF**: https://arxiv.org/pdf/2609.21514
- **详细分析**: [[20_Research/Papers/具身智能/Skel-WAM_A_Hand-Skeleton-Conditioned_World_Action_Model_for_Human-to-Robot_Manipulation_Transfer|Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer]]
- **作者**: Zetao Cai, Yaping Li, Yiqun Wang, Xinyu Zhan, Yuyin Yang, Haoxiang Ma, Kailin Li, Tao Lu, Jiangmiao Pang, Linning Xu, Dahua Lin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Skel-WAM: A Hand-Skeleton-Conditioned World Action Model for Human-to-Robot Manipulation Transfer》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot demonstrations are expensive to collect and often provide limited distributional coverage of task variations. Human videos offer a low-cost source of complementary manipulation experience, but learning from them requires bridging embodiment gaps in visual appearance and action spaces. We introduce Skel-WAM, a world action model that bridges these differences through a unified hand-skeleton motion interface. The key insight is to align human and robot motion through a common hand topology, combining skeleton overlays that ground motion in the scene with structured 2.5-D keypoints that encode explicit hand kinematics. Video and Keypoint Experts jointly learn visual and skeletal dynamics through a Mixture-of-Transformers, while a separate robot-trained Action Expert maps these predictions to executable controls. This separation enables human and robot demonstrations to directly supervise shared dynamics without requiring robot action labels for human videos. Across four real-world bimanual tasks and seven simulated tasks, Skel-WAM achieves average success rates of 79.86% and 63.29%, surpassing the strongest baseline by 22.22 and 8.28 percentage points, respectively. Human-robot cotraining more than doubles real-world success on task variations absent from robot training data, from 38.89% to 86.11%. These results demonstrate that a shared skeletal interface enables joint learning across human and robot data and expands robot task coverage through complementary human demonstrations.

</details>

---

### [[20_Research/Papers/具身智能/DPed-VLN_A_Benchmark_for_Socially_Compliant_Vision-and-Language_Navigation_in_Dynamic_Pedestrian_Environments|DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments]]

![[assets/2609.21504_figure.png|800]]

- **arXiv**: [2609.21504](https://arxiv.org/abs/2609.21504)
- **PDF**: https://arxiv.org/pdf/2609.21504
- **详细分析**: [[20_Research/Papers/具身智能/DPed-VLN_A_Benchmark_for_Socially_Compliant_Vision-and-Language_Navigation_in_Dynamic_Pedestrian_Environments|DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments]]
- **作者**: Haojie Dai, Xiangyi Wang, Liuyi Wang, Kai Sheng, Zongtao He, Chengju Liu, Wei Ye, Qijun Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, EmbodiedAI, RL

#### 研究背景与动机

《DPed-VLN: A Benchmark for Socially Compliant Vision-and-Language Navigation in Dynamic Pedestrian Environments》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DPet-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-and-language navigation (VLN) has advanced rapidly in static indoor environments, but robots operating in human-populated spaces must ground language while responding to moving pedestrians and social-safety constraints. We present DPed-VLN, a Habitat 3.0 benchmark for dynamic-pedestrian VLN that couples 33,093 navigation episodes with paired global and prior-augmented instructions, ORCA-controlled humanoid pedestrians, socially constrained expert paths, and metrics that jointly assess navigation efficiency and social safety. DPed-VLN separates ordinary goal-oriented route guidance from prior-augmented instructions that expose dynamic-pedestrian cues for controlled analysis. To instantiate the benchmark, we introduce DPet (Dynamic Pedestrian-aware Network), a pedestrian-aware policy network trained with reinforcement learning and imitation learning. We further adapt representative state-of-the-art VLM-based navigation models, including NaVILA and StreamVLN, to DPed-VLN through LoRA fine-tuning. Experiments show that LoRA adaptation improves zero-shot VLM baselines in several success and safety metrics, especially reducing StreamVLN's collision rate. Among the evaluated methods, DPet-RL achieves the highest SR, SPL, and STL.

</details>

---

### [[20_Research/Papers/具身智能/FORTE_Task-Adaptive_Force_Capability_Optimization_for_Mobile_Manipulators|FORTE: Task-Adaptive Force Capability Optimization for Mobile Manipulators]]

![[assets/2609.21497_figure.png|800]]

- **arXiv**: [2609.21497](https://arxiv.org/abs/2609.21497)
- **PDF**: https://arxiv.org/pdf/2609.21497
- **详细分析**: [[20_Research/Papers/具身智能/FORTE_Task-Adaptive_Force_Capability_Optimization_for_Mobile_Manipulators|FORTE: Task-Adaptive Force Capability Optimization for Mobile Manipulators]]
- **作者**: Xiao Wang, Heng Zhang, Gokhan Solak, Fei Zhao, Arash Ajoudani
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.3，机器人 0.7）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《FORTE: Task-Adaptive Force Capability Optimization for Mobile Manipulators》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Effective physical interaction control in robotic manipulation requires not only kinematically feasible motion but also sufficient force-interaction capability. Existing redundancy resolution methods often ignore task-specific force demands or maximize the force capability indiscriminately, sacrificing dexterity when large force margins are unnecessary. We propose a task-oriented force capability optimization framework for redundant mobile manipulators. A Vision-Language Model (VLM) infers object physical properties from an RGB image and a task description, generating a desired task-force sequence that captures gravitational and inertial demands. We then define a task-oriented force capability metric as the signed distance between a task-force uncertainty ball and the dynamic residual force polytope (RFP), quantifying compatibility between task demands and the robot's remaining actuation capacity. This metric is incorporated, alongside manipulability, joint-limit avoidance, trajectory smoothness, and base-oscillation suppression, into a whole-body multi-objective trajectory-optimization problem. Experiments on a mobile manipulator performing lifting and single-point-holding tasks under varying payload conditions demonstrate that the proposed method provides sufficient force capability for heavy loads while preserving high manipulability for light loads. This yields a task-adaptive balance that fixed capability-maximizing baselines (RFP inscribed radius, RFP cone) and manipulability-only optimization fail to achieve. The core implementation is publicly available at this https URL .

</details>

---

### [[20_Research/Papers/强化学习/Learning_Distance-Conditioned_Object_Transport_for_Humanoid_Loco-Manipulation_from_a_Single_Motion_Clip|Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip]]

![[assets/2609.21467_figure.png|800]]

- **arXiv**: [2609.21467](https://arxiv.org/abs/2609.21467)
- **PDF**: https://arxiv.org/pdf/2609.21467
- **详细分析**: [[20_Research/Papers/强化学习/Learning_Distance-Conditioned_Object_Transport_for_Humanoid_Loco-Manipulation_from_a_Single_Motion_Clip|Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip]]
- **作者**: Yuhyeon Hwang, Daniel Sungho Jung, YongHyeok Seo, Mingi Jung, Chang Nho Cho, Jung-Hoon Hwang, Dongin Shin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 1.5，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Learning Distance-Conditioned Object Transport for Humanoid Loco-Manipulation from a Single Motion Clip》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion tracking can reproduce humanoid loco-manipulation from a single retargeted motion clip, but a policy trained on a fixed reference primarily reproduces its demonstrated transport outcome. Although the source trajectory visits intermediate object displacements, transport termination is demonstrated only at its endpoint. We identify this mismatch as the termination-versus-passage gap: intermediate displacements are observed as passage states rather than termination-complete outcomes. We introduce Distance-Conditioned Reference Recomposition (DCRR), which relocates the demonstrated termination segment to intermediate transport states. A frozen tracking teacher replays the recomposed references under closed-loop dynamics, and the retained trajectories are relabeled by their achieved object placements and distilled into a reference-free policy. This procedure constructs distance-conditioned supervision from the interaction behavior encoded in the source motion. Across Carry, Kick-Push, Crouch-Push, and Drag, DCRR-BC produces command-dependent transport with an overall normalized distance mean absolute error (MAE) of 0.15, compared with 0.28 for source-only behavior cloning. RL fine-tuning further improves the command response and execution robustness in the training simulator and under sim-to-sim transfer. Finally, hardware experiments demonstrate transport-distance modulation across all four interaction modes.

</details>

---

### [[20_Research/Papers/具身智能/Robotic_Multiphase_Interaction_Manipulating_Coupled_Liquid_and_Solid_Dynamics_with_a_World_Model|Robotic Multiphase Interaction: Manipulating Coupled Liquid and Solid Dynamics with a World Model]]

![[assets/2609.21448_figure.png|800]]

- **arXiv**: [2609.21448](https://arxiv.org/abs/2609.21448)
- **PDF**: https://arxiv.org/pdf/2609.21448
- **详细分析**: [[20_Research/Papers/具身智能/Robotic_Multiphase_Interaction_Manipulating_Coupled_Liquid_and_Solid_Dynamics_with_a_World_Model|Robotic Multiphase Interaction: Manipulating Coupled Liquid and Solid Dynamics with a World Model]]
- **作者**: Yixuan Feng, Peng Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.6，世界模型 0.8，机器人 1.3）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Robotic Multiphase Interaction: Manipulating Coupled Liquid and Solid Dynamics with a World Model》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This work presents \textit{Robotic Multiphase Interaction (RMI)}, a setting in which liquid enters a porous material and interacts mechanically with its deforming solid skeleton. Manipulation can therefore change pore volume, expel or redistribute retained liquid, and alter grasp stability at the same time. Spilled liquid can also create safety risks in domestic and manufacturing settings. This differs from most manipulation of solid objects and from tasks that involve both liquid and solid while keeping the phases spatially separate. We study a sponge filled with water as the first RMI example. We use implicit incompressible porous flow with smoothed particle hydrodynamics as the dynamics engine and enable robotic manipulation by adding Coulomb contact memory, hybrid velocity and force regulation, and a stability gate for lifting. The resulting environment connects robot commands to changes in the coupled liquid and solid state. A world model conditioned on actions predicts how this state evolves under candidate commands, while a temporal UNet generates actions using either Diffusion Policy or rectified flow matching. Our world model reduces retained water prediction error by more than $60\%$ compared with the baseline. The best action sequence selected by the world model from policy proposals further reduces the predicted terminal water error by about half. These improvements show that modelling the coupled liquid and solid state helps the robot predict how its actions affect both the porous object and the liquid held inside.

</details>

---

### [[20_Research/Papers/大模型/AVT-Fabric_Active_Visuo-Tactile_Perception_via_Adaptive_Evidence_Selection_for_Efficient_Robotic_Fabric_Comparison|AVT-Fabric: Active Visuo-Tactile Perception via Adaptive Evidence Selection for Efficient Robotic Fabric Comparison]]

![[assets/2609.21377_figure.jpg|800]]

- **arXiv**: [2609.21377](https://arxiv.org/abs/2609.21377)
- **PDF**: https://arxiv.org/pdf/2609.21377
- **详细分析**: [[20_Research/Papers/大模型/AVT-Fabric_Active_Visuo-Tactile_Perception_via_Adaptive_Evidence_Selection_for_Efficient_Robotic_Fabric_Comparison|AVT-Fabric: Active Visuo-Tactile Perception via Adaptive Evidence Selection for Efficient Robotic Fabric Comparison]]
- **作者**: Chang Gao, Zhuo Chen, Suhang Xia, Jihong Zhu, Jiankang Deng, Shan Luo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《AVT-Fabric: Active Visuo-Tactile Perception via Adaptive Evidence Selection for Efficient Robotic Fabric Comparison》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Tactile-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic fabric comparison needs to actively combine visual appearance and tactile cues. Here, we present AVT-Fabric, an RGB-first framework that allocates tactile evidence according to the difficulty of each comparison. A dual-scale gate evaluates answer-token confidence and raw logit separation to determine whether another force-tagged GelSight observation is needed. Compact textual memory preserves the executed history, and majority voting consolidates the selected predictions. On 400 held-out comparisons, AVT-Fabric achieves 98.0% accuracy with a compact 7B Multimodal Large Language Model (MLLM), surpassing the 94.0% reported by the 90B MLLM-Fabric baseline by 4.0 percentage points while processing only 1.60 of five available stages on average. It improves on matched passive inference by 9.25 percentage points and reduces model-side latency by 61.8%, while also improving on RGB-only accuracy. Four additional MLLM backbones support the generalizability, accuracy, and efficiency of the framework. This framework is also deployed on a real robotic system, achieving 78.1% pairwise ranking accuracy and correct fabric selection in seven of eight application scenarios. AVT-Fabric demonstrates that adaptive evidence selection can improve both the accuracy and efficiency of robotic visuo-tactile reasoning.

</details>

---

### [[20_Research/Papers/具身智能/FAN_Foresight_Action_Normalization_for_Continual_Adaptation_of_Vision-Language-Action_Models|FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models]]

![[assets/2609.21358_figure.png|800]]

- **arXiv**: [2609.21358](https://arxiv.org/abs/2609.21358)
- **PDF**: https://arxiv.org/pdf/2609.21358
- **详细分析**: [[20_Research/Papers/具身智能/FAN_Foresight_Action_Normalization_for_Continual_Adaptation_of_Vision-Language-Action_Models|FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models]]
- **作者**: Yijun Hong, Jiarun Zhu, Xiaoquan Sun, Le Xu, Qijun He, Xin Jin, Mingqi Yuan, Wenjun Zeng, Jiayu Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.6（加权：具身智能 2.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《FAN: Foresight Action Normalization for Continual Adaptation of Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models pre-trained on large-scale, closed datasets have demonstrated remarkable success across diverse robotic manipulation tasks. However, their long-term real-world deployment necessitates continuously acquiring new skills while retaining previously learned capabilities. While pioneering works have explored continual VLA adaptation using techniques such as experience replay and reinforcement fine-tuning, they overlook a foundational mechanism: action normalization, which determines the underlying coordinate system in which policies perceive and execute physical actions. To bridge this gap, we systematically evaluate five normalization strategies across four real-world task streams covering single-arm and bimanual manipulation. Our analysis reveals that existing protocols induce severe failure modes due to inter-task coordinate drift, limited motion coverage, or train-test coordinate mismatches. Motivated by these insights, we formulate three core design principles: consistency, coverage, and causality (3C), and introduce foresight action normalization (FAN). FAN estimates normalization statistics once from a small, task-independent calibration set prior to continual learning and freezes them throughout adaptation. Across all evaluated streams, FAN achieves the highest performance and demonstrates consistent robustness, providing insightful guidance for building stable action representations in achieving effective lifelong VLA adaptation.

</details>

---

### [[20_Research/Papers/机器人/The_EventCV_Library_for_Event-Based_Robotic_Vision|The EventCV Library for Event-Based Robotic Vision]]

![[assets/2609.21330_figure.png|800]]

- **arXiv**: [2609.21330](https://arxiv.org/abs/2609.21330)
- **PDF**: https://arxiv.org/pdf/2609.21330
- **详细分析**: [[20_Research/Papers/机器人/The_EventCV_Library_for_Event-Based_Robotic_Vision|The EventCV Library for Event-Based Robotic Vision]]
- **作者**: Adam D. Hines, Michael Milford, Tobias Fischer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《The EventCV Library for Event-Based Robotic Vision》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：N-ImageNet, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Event cameras detect per-pixel brightness changes asynchronously on microsecond timescales, with high dynamic range and low power draw. These are desirable properties for robots that move fast or work in difficult lighting conditions. However, integrating an event camera into a real-world robotic pipeline still requires substantial effort: plug-and-play drivers do not exist, event streams are recorded in a variety of incompatible file formats, and most projects rely on custom research-grade code. Here, we present EventCV, an open-source and extensible Rust library with OpenCV-style Python bindings that lowers the entry barrier to working with event cameras. EventCV provides a wide range of features: denoising filters and geometric transforms, augmentations, corner detection and unsupervised feature learning, contrast-maximization motion estimation, a video-to-events simulator, and Open Neural Network Exchange (ONNX) inference for deployment in robotic stacks. EventCV integrates the Neuromorphic Drivers package, allowing an event camera stream to be processed directly in real time. No existing toolkit covers this range of operations in one package, and EventCV builds representations and decodes files 1.1x to 3.7x faster than the currently available libraries. We deploy EventCV on a Jetson Orin AGX and present three robotics case studies spanning object detection, on-device model inference, and localization. Project webpage: this https URL .

</details>

---

### [[20_Research/Papers/大模型/LEMCA_LLM-Guided_Synthesis_of_Efficient_Mode-Switching_Control_Architectures|LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures]]

![[assets/2609.21319_figure.png|800]]

- **arXiv**: [2609.21319](https://arxiv.org/abs/2609.21319)
- **PDF**: https://arxiv.org/pdf/2609.21319
- **详细分析**: [[20_Research/Papers/大模型/LEMCA_LLM-Guided_Synthesis_of_Efficient_Mode-Switching_Control_Architectures|LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures]]
- **作者**: Arjun Krishna, Vincent Pacelli, Dinesh Jayaraman
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.4，强化学习 0.2，机器人 0.7）
- **关联关键词**: LLM, Robotics, RL

#### 研究背景与动机

《LEMCA: LLM-Guided Synthesis of Efficient Mode-Switching Control Architectures》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：MSC-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Physical control tasks in the natural world, such as driving or object manipulation, frequently exhibit dramatic variations in sensory and compute complexity over time. Correspondingly, a natural resource-efficient choice for robot control is to dynamically switch between control modes with varying resource allocations. However, such "mode-switching controllers" (MSCs) have historically required laborious, expert-driven design and synthesis for each new task. Driven by these design difficulties, modern robotic control architectures often fall back to a wasteful "monolithic" one-size-fits-all structure, where resource allocation is permanently anchored to the hardest, most resource-intensive task phases. To facilitate the design of performant yet efficient MSCs, we propose LLM-Guided synthesis of Efficient Mode-Switching Control Architectures (LEMCA). LEMCA represents MSC designs as interpretable programs to be iteratively refined in an evolutionary loop. To evaluate design fitness, we propose MSC-compatible extensions of automated controller synthesis approaches, such as reinforcement learning in simulation. LEMCA then leverages the semantic priors, reasoning, and coding capabilities of Large Language Models (LLMs) to iteratively edit controller modes, their corresponding sensory-compute resource allocations, and mode transitions. Our experiments across diverse control benchmarks show that LEMCA consistently discovers strategies that surpass the Pareto frontier of monolithic designs by reclaiming wasted resources during "easy" task phases. LEMCA thus presents an automated, low-effort path to synthesize resource-efficient MSC designs.

</details>

---

### [[20_Research/Papers/具身智能/NaViRrator_Robot_Navigation_from_Human-Readable_Maps_through_a_Learned_Visual_Route|NaViRrator: Robot Navigation from Human-Readable Maps through a Learned Visual Route]]

![[assets/2609.21316_figure.png|800]]

- **arXiv**: [2609.21316](https://arxiv.org/abs/2609.21316)
- **PDF**: https://arxiv.org/pdf/2609.21316
- **详细分析**: [[20_Research/Papers/具身智能/NaViRrator_Robot_Navigation_from_Human-Readable_Maps_through_a_Learned_Visual_Route|NaViRrator: Robot Navigation from Human-Readable Maps through a Learned Visual Route]]
- **作者**: Ayun Lee, Jiseon Kim, Giseop Kim
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.6（加权：具身智能 1.2，大模型 0.3，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《NaViRrator: Robot Navigation from Human-Readable Maps through a Learned Visual Route》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human-readable maps provide an intuitive interface for specifying robot destinations, but connecting their schematic geometry to egocentric observations remains challenging. We present NaViRRator, a framework that translates user-specified start and goal locations on such maps into navigation instructions for a pretrained vision-and-language navigation (VLN) policy. Its core method, RouteScribe, separates route inference from verbalization by first generating an explicit route scaffold in map-image coordinates, which a pretrained vision-language model (VLM) converts into a navigation instruction. We construct the scaffold with start--goal line conditional flow matching (SGL-CFM), which deforms a straight start--goal waypoint sequence into a map-conditioned route. During execution, the VLN policy receives only the instruction and egocentric observations, while the map and scaffold remain upstream, allowing executor replacement without retraining the map-to-language modules. Real-world experiments show higher success rates and success weighted by path length (SPL) than direct map-to-instruction generation, A*-based scaffolding, and Gaussian-source conditional flow matching. Qualitative results further show clearer salient turns and better preservation of the intended maneuver sequence, supporting route-grounded language as a modular interface between human-readable maps and pretrained navigation policies.

</details>

---

### [[20_Research/Papers/强化学习/Stability-aware_Residual_Reinforcement_Learning_Framework_for_Robotic_Manipulator_Disturbance_Compensation|Stability-aware Residual Reinforcement Learning Framework for Robotic Manipulator Disturbance Compensation]]

![[assets/2609.21307_figure.png|800]]

- **arXiv**: [2609.21307](https://arxiv.org/abs/2609.21307)
- **PDF**: https://arxiv.org/pdf/2609.21307
- **详细分析**: [[20_Research/Papers/强化学习/Stability-aware_Residual_Reinforcement_Learning_Framework_for_Robotic_Manipulator_Disturbance_Compensation|Stability-aware Residual Reinforcement Learning Framework for Robotic Manipulator Disturbance Compensation]]
- **作者**: Jihong Kim, Joonhyuk Kwon, Hwa Soo Kim, TaeWon Seo, Hyung-Tae Seo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 强化学习, 具身智能
- **相关性评分**: 2.3（加权：具身智能 0.6，强化学习 0.8，机器人 0.9）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Stability-aware Residual Reinforcement Learning Framework for Robotic Manipulator Disturbance Compensation》归入 机器人、强化学习、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、强化学习、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Although conventional controllers and disturbance observers (DOBs) are the standard for precision tracking in manipulators, they suffer from parameter uncertainty, nonlinear friction, and compound disturbances. This study proposes a residual reinforcement learning DOB framework that pairs an analytical observer with an RL policy. The deterministic baseline operates within a reliable region, whereas the RL policy explicitly targets the residuals that the model cannot capture. To make this compensation disturbance-aware, an estimator network aligns the observation history with a privileged disturbance context, organizing the latent space by disturbance regime and enabling rapid adaptation across disturbance transitions. To guarantee stability, we derived and enforced a state-dependent action bound on the RL policy from an input-to-state stability (ISS) analysis such that the closed loop provably confines the tracking error to a certified envelope for arbitrary policy outputs. Experiments on a 6-DOF manipulator demonstrated consistent improvements in disturbance estimation and tracking, including a 27.8% tracking-error reduction on real hardware under zero-shot sim-to-real transfer and a 38.0% reduction under a base-vibration disturbance that was not observed during training.

</details>

---

### [[20_Research/Papers/机器人/AirSplan_Risk-Aware_Motion_Planning_for_Quadrotors_in_Cluttered_3D_Gaussian_Splats|AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats]]

![[assets/2609.21226_figure.png|800]]

- **arXiv**: [2609.21226](https://arxiv.org/abs/2609.21226)
- **PDF**: https://arxiv.org/pdf/2609.21226
- **详细分析**: [[20_Research/Papers/机器人/AirSplan_Risk-Aware_Motion_Planning_for_Quadrotors_in_Cluttered_3D_Gaussian_Splats|AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats]]
- **作者**: Seth Isaacson, William Hong, Katherine A. Skinner, Ram Vasudevan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《AirSplan: Risk-Aware Motion Planning for Quadrotors in Cluttered 3D Gaussian Splats》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadrotors are increasingly deployed in applications such as agriculture, infrastructure inspection, and maintenance. In each of these applications, the robot must navigate complex scene geometry while remaining strictly collision-free. Unlike in ground domains, even minor collisions for aerial vehicles can result in the loss of the robot. This safety requirement induces a pair of technical challenges. First, the environment must be represented with sufficient fidelity to encode complex structure, even when no ground-truth obstacle data is available. Second, a motion planner must leverage this representation to determine a collision-free path to the goal. This paper proposes a system that addresses these complementary challenges. The proposed method, AirSplan, adopts a normalized variant of 3D Gaussian Splatting that encodes high-fidelity scene geometry. It then applies a novel reachability-based motion planner that leverages the differential flatness of quadrotors to compute continuous-time collision constraints that tightly overapproximate the robot's occupancy. Experiments demonstrate that AirSplan successfully finds a path in 81.2% of challenging test cases, a significant improvement over the nearest baseline method's 51.2%.

</details>

---

### [[20_Research/Papers/具身智能/SafeStage_Evaluating_Safety_Before,_During,_and_After_Vision-Language-Conditioned_Robot_Manipulation|SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation]]

![[assets/2609.21223_figure.png|800]]

- **arXiv**: [2609.21223](https://arxiv.org/abs/2609.21223)
- **PDF**: https://arxiv.org/pdf/2609.21223
- **详细分析**: [[20_Research/Papers/具身智能/SafeStage_Evaluating_Safety_Before,_During,_and_After_Vision-Language-Conditioned_Robot_Manipulation|SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation]]
- **作者**: Jinzhu Luo, Qi Zhang, Wei Wang, Wei Jiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《SafeStage: Evaluating Safety Before, During, and After Vision-Language-Conditioned Robot Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：IS-Bench, OpenVLA, SafeVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-conditioned robot policies integrate perception, language understanding, and control for general-purpose manipulation. However, existing evaluations often focus on task success, isolated physical constraints, semantic refusal, or realized physical damage, providing limited insight into where safety fails during closed-loop manipulation. We introduce SafeStage, a lifecycle-structured benchmark for evaluating manipulation safety before, during, and after task execution. SafeStage contains 97 purpose-built risk scenarios organized into three stages. Initial-State Hazards captures safety-relevant relations that must be resolved before manipulating the target. Execution-Time Safety evaluates unsafe contacts, trajectories, region entries, and object interactions during execution. Final-State Hazards capture unstable or otherwise unsafe conditions remaining after nominal task completion. The benchmark evaluates realized interactions using event-based and state-based checks and reports native task success independently from stage-specific safety outcomes. We evaluate representative direct-action Vision-Language-Action (VLA) policies and policies with world-model-based policies under a common closed-loop protocol. Our results demonstrate that nominal task completion frequently coexists with safety violations and that different policies exhibit distinct failure profiles across the three stages. By separating task success from safety and localizing when violations occur, SafeStage provides a unified diagnostic testbed for evaluating and improving vision-language-conditioned robot manipulation policies.

</details>

---

### [[20_Research/Papers/具身智能/Safe_Real-Time_Policy_Steering_via_Noise-Space_Trajectory_Optimization_for_One-Step_Generative_Policies|Safe Real-Time Policy Steering via Noise-Space Trajectory Optimization for One-Step Generative Policies]]

![[assets/2609.21220_figure.png|800]]

- **arXiv**: [2609.21220](https://arxiv.org/abs/2609.21220)
- **PDF**: https://arxiv.org/pdf/2609.21220
- **详细分析**: [[20_Research/Papers/具身智能/Safe_Real-Time_Policy_Steering_via_Noise-Space_Trajectory_Optimization_for_One-Step_Generative_Policies|Safe Real-Time Policy Steering via Noise-Space Trajectory Optimization for One-Step Generative Policies]]
- **作者**: Qingyi Chen, Joseph Ruan, Zachary Kingston
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Safe Real-Time Policy Steering via Noise-Space Trajectory Optimization for One-Step Generative Policies》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generative robot policies can represent diverse, multimodal behaviors, but adapting pretrained policies to deployment-time constraints such as collision avoidance and orientation maintenance remains challenging. Existing inference-time steering methods typically apply gradient guidance through iterative diffusion or flow processes, which can be computationally expensive for real-time control. We propose INSPO, which formulates inference-time steering of one-step generative policies as trajectory optimization in the policy's input noise space. By optimizing the input noise while evaluating constraints on the induced state trajectory, INSPO searches the policy-induced behavior space without directly modifying generated actions. The optimization includes a regularization term that encourages solutions to remain consistent with the policy's input distribution and is solved online using population-based particle optimization. We evaluate INSPO on state- and image-based task-specific policies and generalist vision-language-action policies across Push-T, Can pick-and-place, and LIBERO-Spatial. INSPO improves task success and constraint satisfaction over best-of-N sampling and action projection, while comparing favorably with gradient-guided generation at lower runtime.

</details>

---

### [[20_Research/Papers/机器人/Stochastic_Neural_Signed_Swept_Volume_for_Real-time_Chance-Constrained_Trajectory_Optimization|Stochastic Neural Signed Swept Volume for Real-time Chance-Constrained Trajectory Optimization]]

![[assets/2609.21211_figure.png|800]]

- **arXiv**: [2609.21211](https://arxiv.org/abs/2609.21211)
- **PDF**: https://arxiv.org/pdf/2609.21211
- **详细分析**: [[20_Research/Papers/机器人/Stochastic_Neural_Signed_Swept_Volume_for_Real-time_Chance-Constrained_Trajectory_Optimization|Stochastic Neural Signed Swept Volume for Real-time Chance-Constrained Trajectory Optimization]]
- **作者**: Qingyi Chen, Kevin Zhang, Lucas Chen, Zachary Kingston
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Stochastic Neural Signed Swept Volume for Real-time Chance-Constrained Trajectory Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collision-free motion planning requires reliable collision models from sensed environments and validation of states along a continuous trajectory. To make this tractable, most planners check for collision at discrete states along continuous trajectories against a single determinized model of the environment, introducing a trade-off between safety and computational efficiency. While continuous collision checking approaches that approximate the swept volume of the robot exist, they are computationally expensive or overly conservative. Data-driven approaches can learn the swept volume; however, these neural models are susceptible to approximation errors and are therefore often limited to serving as coarse filters for downstream collision checkers. In this work, we propose to learn a signed distance function of the swept volume as a probabilistic field, enabling quantification of epistemic uncertainty, incorporation of perception noise, and eventual integration into a chance-constrained trajectory optimization framework. We demonstrate our approach on challenging high-dimensional manipulation problems with significant sensor noise, both in simulation and on real hardware.

</details>

---

### [[20_Research/Papers/机器人/MA-LIPP_Cooperative_Multi-Agent_Load-Aware_Informative_Path_Planning_for_Heterogeneous_Robot_Teams|MA-LIPP: Cooperative Multi-Agent Load-Aware Informative Path Planning for Heterogeneous Robot Teams]]

![[assets/2609.21167_figure.png|800]]

- **arXiv**: [2609.21167](https://arxiv.org/abs/2609.21167)
- **PDF**: https://arxiv.org/pdf/2609.21167
- **详细分析**: [[20_Research/Papers/机器人/MA-LIPP_Cooperative_Multi-Agent_Load-Aware_Informative_Path_Planning_for_Heterogeneous_Robot_Teams|MA-LIPP: Cooperative Multi-Agent Load-Aware Informative Path Planning for Heterogeneous Robot Teams]]
- **作者**: Hojune Kim, Guangyao Shi, Gaurav S. Sukhatme
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 2.8（加权：具身智能 0.3，大模型 0.4，机器人 2.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《MA-LIPP: Cooperative Multi-Agent Load-Aware Informative Path Planning for Heterogeneous Robot Teams》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Field robotics missions often require physical samples to be returned to laboratories for analysis, making path planning inherently load-aware and order-dependent as accumulated samples increase payload and traversal energy costs. In single-robot Load-Aware Informative Path Planning (LIPP), this rigidly couples sensing with hauling: a solitary robot must transport every collected sample, forcing frequent depot returns that severely restrict its spatial coverage. Heterogeneous multi-robot teams can overcome this bottleneck by dividing labor---enabling high-precision samplers to collect while high-capacity carriers handle transport. However, this introduces a complex coordination challenge regarding when, where, what, and to whom handoffs should occur on top of the LIPP problem. To address this tightly coupled problem, we introduce Multi-Agent LIPP (MA-LIPP), which enables teams to cooperate through asynchronous "dead drops," allowing one robot to deposit samples for another to retrieve later without requiring synchronous rendezvous. We formulate MA-LIPP as an exact Mixed-Integer Quadratic Program (MIQP) alongside a scalable Pairwise Large-Neighborhood Search (LNS) heuristic for complex real-world applications. The heuristic matches exact optima in $95.5\%$ of certified cases and reduces weighted posterior variance by $16.1$--$19.8\%$ relative to a sequential baseline on larger instances of up to 12 robots, providing a robust framework for cooperative physical-sampling missions.

</details>

---

### [[20_Research/Papers/强化学习/SAGE_Safety-Aligned_Gradient_Enforcement_for_Human--Robot_Collaboration|SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration]]

![[assets/2609.21130_figure.png|800]]

- **arXiv**: [2609.21130](https://arxiv.org/abs/2609.21130)
- **PDF**: https://arxiv.org/pdf/2609.21130
- **详细分析**: [[20_Research/Papers/强化学习/SAGE_Safety-Aligned_Gradient_Enforcement_for_Human--Robot_Collaboration|SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration]]
- **作者**: Yisen Li, Hao Zhang, Ruize Geng, Yves Tseng, Ding Zhao, H. Eric Tseng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习, 大模型
- **相关性评分**: 2.4（加权：具身智能 0.6，大模型 0.1，强化学习 0.4，机器人 1.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《SAGE: Safety-Aligned Gradient Enforcement for Human--Robot Collaboration》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：BarrierNet, HARL, MARL, OptNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-party human-robot collaboration poses a dual challenge: robot decisions should remain interpretable and auditable, while executed actions must satisfy safety constraints during physical interaction. Combining explainable decision-tree policies with control-barrier-function (CBF) filtering provides a promising architecture but creates two learning mismatches in multi-agent reinforcement learning. Safety projection changes the action applied to the environment, while the coupled proposal graph can misalign independently optimized actor updates with a team-level update. We present safety-aligned gradient enforcement (SAGE) to address both mismatches. Its shield-annealed internalization layer (SAIL) uses a differentiable finite-penalty proposal map while retaining the exact CBF quadratic program for execution, preserving constraint-normal sensitivity to internalize repeatedly active safety constraints. Team-averaged Lyapunov policy optimization (TALO) constructs a team-aware update reference and applies a Lyapunov half-space correction to regulate independent actor updates. Physical experiments with two humanoid robots and a human partner demonstrate deployment feasibility. Across nine simulation scenarios, SAGE achieves a 71.0% success rate with 0.5 collision steps per thousand environment steps. Ablations show that direct CBF filtering reduces collision frequency by 98.5% but decreases success from 67.3% to 59.3%. SAIL reduces proposal violation by 48.8% and proposal-execution correction by 85.2%, while TALO reduces the update-consistency gap by 50.8%.

</details>

---

### [[20_Research/Papers/强化学习/MetaPusher_Meta_Learning_and_Planning_for_Nonprehensile_Manipulation_of_Unseen_Objects_with_Rapid_Online_Adaption|MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption]]

![[assets/2609.21122_figure.png|800]]

- **arXiv**: [2609.21122](https://arxiv.org/abs/2609.21122)
- **PDF**: https://arxiv.org/pdf/2609.21122
- **详细分析**: [[20_Research/Papers/强化学习/MetaPusher_Meta_Learning_and_Planning_for_Nonprehensile_Manipulation_of_Unseen_Objects_with_Rapid_Online_Adaption|MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption]]
- **作者**: Donghyung Lee, Seyedali Golestaneh, Jaskrit Singh, Zhuoyun Zhong, Athanasios Kapoutsis, Constantinos Chamzas
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，世界模型 0.2，机器人 0.3）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《MetaPusher: Meta Learning and Planning for Nonprehensile Manipulation of Unseen Objects with Rapid Online Adaption》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：PointNet, Push-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Manipulating previously unseen objects remains challenging, as their dynamics depend on latent physical properties, such as friction and mass distribution, that cannot be inferred from perception alone. Prior experience across objects can provide an initial estimate of unseen object dynamics, but this estimate remains uncertain and can degrade further during sim-to-real transfer. Adapting the dynamics through interaction can progressively refine the estimation, however, updating the model may invalidate the planned trajectory. Successful and efficient manipulation therefore requires both rapid dynamics adaptation and a planning strategy that can incorporate this evolution. In this work, we introduce MetaPusher, a meta-learning and adaptive planning framework for nonprehensile manipulation of unseen objects without prior object-specific interactions. A meta-learned dynamics model rapidly adapts from interactions during task execution, while an adaptive kinodynamic planner updates long-horizon plans by reusing and refining its existing search tree. This coupling enables manipulation and adaptation without a separate data collection phase. We evaluate MetaPusher on unseen objects in simulation and in sim-to-real scenarios, comparing against fine-tuning and active learning methods, MPPI-based control, and a reinforcement learning policy. It achieves lower prediction error and improves task success rate by up to 20%.

</details>

---

### [[20_Research/Papers/机器人/Noctif3R_Feed-Forward_Monocular_Real-Time_SLAM_for_Photon-Limited_Scenes_on_Embedded_Hardware|Noctif3R: Feed-Forward Monocular Real-Time SLAM for Photon-Limited Scenes on Embedded Hardware]]

![[assets/2609.21114_figure.png|800]]

- **arXiv**: [2609.21114](https://arxiv.org/abs/2609.21114)
- **PDF**: https://arxiv.org/pdf/2609.21114
- **详细分析**: [[20_Research/Papers/机器人/Noctif3R_Feed-Forward_Monocular_Real-Time_SLAM_for_Photon-Limited_Scenes_on_Embedded_Hardware|Noctif3R: Feed-Forward Monocular Real-Time SLAM for Photon-Limited Scenes on Embedded Hardware]]
- **作者**: Mihir Chauhan, Aditya Uday Abhang, Kevin Biju Mathew, Aniket Bera
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Noctif3R: Feed-Forward Monocular Real-Time SLAM for Photon-Limited Scenes on Embedded Hardware》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots carrying out tasks in dark environments need to localize from a single RGB camera, in light so low that the per-pixel signal approaches the sensor's own noise, on a power-constrained onboard computer, in real time. Each of these constraints has matured pipelines, but the intersection does not. Offline low-light reconstruction now recovers structure below -4 dB but is far too slow to run in real time, while the real-time monocular systems a robot can actually carry (DROID-SLAM, DPV-SLAM, etc.) degrade or fail when SNR gets low. We measured how they fail: across the nine lowest darkness levels of our scenes, DROID-SLAM returns a full-length trajectory carrying no information about the camera's motion on all nine, VGGT-SLAM and CUT3R on eight, pi^3 on seven, and DPV-SLAM on four. We present SYS, a monocular pipeline built on a low-light feed-forward pointmap front end with an explicit match gate, which returns three tracked trajectories and no uninformative ones, at the lowest error of any method where it tracks (24-47% of the no-information ceiling against 56-73% for the strongest baseline), and at the narrowest coverage. On a real robot video take in which 86.5% of delivered frames are entirely black, every configuration of ours stops after the lit beginning, while DROID-SLAM and DPV-SLAM each emit a pose for all 1178 frames. Our method contribution is an embedded execution path for the Jetson AGX Orin: running the map, keyframes and backend at 384 pixels with tracking at 256, together with two fixes to the per-frame pose solve, is a replicated Pareto improvement, 1.28x throughput at 0.964x error on one scene and 1.42x at 0.68x on a second, with 47% less peak GPU memory and 29% less energy per pose. We evaluate on a calibrated, bit-exact regenerable noise ladder, on relabelled real-world dark exposures, and on a new dark-room video ladder recorded from a Boston Dynamics Spot robot.

</details>

---

### [[20_Research/Papers/具身智能/Learning_Scene-Aware_Humanoid_Locomotion_through_3D_Clutter_from_Immersive_Human_Demonstrations|Learning Scene-Aware Humanoid Locomotion through 3D Clutter from Immersive Human Demonstrations]]

![[assets/2609.21107_figure.png|800]]

- **arXiv**: [2609.21107](https://arxiv.org/abs/2609.21107)
- **PDF**: https://arxiv.org/pdf/2609.21107
- **详细分析**: [[20_Research/Papers/具身智能/Learning_Scene-Aware_Humanoid_Locomotion_through_3D_Clutter_from_Immersive_Human_Demonstrations|Learning Scene-Aware Humanoid Locomotion through 3D Clutter from Immersive Human Demonstrations]]
- **作者**: Beichen Wang, Tong Xu, Daniel Kosukhin, Yuen-Hei Yeung, Yuanjie Lu, Xuesu Xiao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.0（加权：具身智能 2.7，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Learning Scene-Aware Humanoid Locomotion through 3D Clutter from Immersive Human Demonstrations》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

While learning from human motions has enabled highly dynamic humanoid skills such as dancing and martial arts in obstacle-free space, traversal through densely cluttered environments remains underexplored. These spaces are three-dimensional and geometrically constrained, requiring scene-aware locomotion that tightly couples whole-body motion with scene geometry for obstacle avoidance. To address these challenges, we present Moving Through Clutter (MTC), a learning-from-demonstration framework for scene-aware humanoid locomotion. To bypass costly physical scene construction, MTC uses procedurally generated Virtual Reality environments for immersive data collection. To transform these human motions into training-ready humanoid motions, we propose a scene-aware motion retargeting algorithm that converts human demonstrations into humanoid trajectories while strictly enforcing robot-scene clearance to guarantee collision-free traversal. These reference trajectories are then used to train a scene-aware locomotion policy that deploys on a Unitree G1 humanoid. Evaluated on our proposed MTC-Challenge for multi-obstacle traversal, the policy demonstrates a 70.2% collision-free rate across diverse scenarios, successfully traversing complex environments through diverse whole-body skills, including crawling through low-clearance passages and squeezing through narrow gaps.

</details>

---

### [[20_Research/Papers/强化学习/Dynamics-Induced_Commitment_in_Learning-Based_Robotic_Penalty_Kicks|Dynamics-Induced Commitment in Learning-Based Robotic Penalty Kicks]]

![[assets/2609.21100_figure.png|800]]

- **arXiv**: [2609.21100](https://arxiv.org/abs/2609.21100)
- **PDF**: https://arxiv.org/pdf/2609.21100
- **详细分析**: [[20_Research/Papers/强化学习/Dynamics-Induced_Commitment_in_Learning-Based_Robotic_Penalty_Kicks|Dynamics-Induced Commitment in Learning-Based Robotic Penalty Kicks]]
- **作者**: Ruize Geng, Hao E. Zhang, Yisen Li, Yikai Wang, H. Eric Tseng, Ding Zhao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 2.6（加权：具身智能 0.9，强化学习 0.2，机器人 1.5）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Dynamics-Induced Commitment in Learning-Based Robotic Penalty Kicks》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning in robotic games is constrained not only by strategic information but also by what the body can still execute. We study this coupling in a hierarchical humanoid-quadruped penalty system in which game-level self-play policies command fixed soccer whole-body controllers (S-WBCs). The humanoid shooting skill is initialized from self-collected motion-capture data, whereas the quadruped saving skill is learned by reinforcement learning. We introduce dynamics-induced commitment mapping (DIC-Map), a body-grounded analysis that estimates continuation capability, identifies the first persistent loss of a terminal alternative, and tests whether the remaining interaction admits a reduced zero-sum game. For symmetric terminal alternatives, the reduced game yields a closed-form bound on optimal strategy concentration determined by the responder's value of deferring. We further show that, when the responder acts through an estimator, equal response values eliminate the direct terminal-allocation gradient and leave an estimator-mediated first-order learning channel. Experiments locate commitment about 0.29 s before contact, and changing only ball speed shifts deferral coverage. Across four responder policies, replacing the estimator raises save rate from 0.240 to 0.472, whereas a comparable gain in read accuracy obtained by waiting raises it only to 0.246. Posterior analysis is used for the equilibrium comparison because the available coverage terms are observational proxies. Project website: this https URL

</details>

---

### [[20_Research/Papers/机器人/Dynamic_Modeling_and_LQR_Control_of_a_Single_Coaxial_Drone_with_2DOF_Thrust_Vectoring_Mechanism|Dynamic Modeling and LQR Control of a Single Coaxial Drone with 2DOF Thrust Vectoring Mechanism]]

![[assets/2609.21099_figure.png|800]]

- **arXiv**: [2609.21099](https://arxiv.org/abs/2609.21099)
- **PDF**: https://arxiv.org/pdf/2609.21099
- **详细分析**: [[20_Research/Papers/机器人/Dynamic_Modeling_and_LQR_Control_of_a_Single_Coaxial_Drone_with_2DOF_Thrust_Vectoring_Mechanism|Dynamic Modeling and LQR Control of a Single Coaxial Drone with 2DOF Thrust Vectoring Mechanism]]
- **作者**: Ali Jokar, Amin Talaeizadeh, Aria Alasty
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Dynamic Modeling and LQR Control of a Single Coaxial Drone with 2DOF Thrust Vectoring Mechanism》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coaxial rotor drones have generated considerable interest because of energy efficiency and small size, but they are afflicted with inherent underactuation for roll and pitch control, although systems like swashplates have circumvented this limitation at the cost of greater mechanical complexity. This work presents a novel coaxial drone supplemented by a two-degreesof-freedom pendulum mechanism for active thrust vectoring that offers a less mechanically complicated alternative. We develop a comprehensive Lagrangian dynamic model that does not ignore the inertial contributions of all the components, including body, servo arms, and motor assembly. A Linear Quadratic Regulator(LQR) is designed based on the linearized dynamics around the hover equilibrium. High-fidelity simulations taking actuator dynamics and sensor noise into account validate the proposed architecture. An Extended Kalman Filter (EKF) blends GPS, barometer, and IMU estimates with high accuracy for state estimation. The findings verify the potential and reliability of this approach for power-saving, rapid coaxial UAVs.

</details>

---

### [[20_Research/Papers/大模型/DEXTERA_From_a_Single_Image_to_Deployable_Dexterous_Manipulation_via_Real-to-Sim-to-Real|DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real]]

![[assets/2609.21045_figure.jpg|800]]

- **arXiv**: [2609.21045](https://arxiv.org/abs/2609.21045)
- **PDF**: https://arxiv.org/pdf/2609.21045
- **详细分析**: [[20_Research/Papers/大模型/DEXTERA_From_a_Single_Image_to_Deployable_Dexterous_Manipulation_via_Real-to-Sim-to-Real|DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real]]
- **作者**: Jin Wu, Lianjie Yuan, Zeyan Sun, Yuanyuan Lei, Disi A, Bicheng Han, Fangzhou Xia
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 3.6（加权：具身智能 2.7，大模型 0.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《DEXTERA: From a Single Image to Deployable Dexterous Manipulation via Real-to-Sim-to-Real》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：HY-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Collecting real-world robot data for dexterous manipulation is costly and time-consuming. While high-fidelity physics simulators enable scalable data synthesis and policy learning, constructing deployment-ready digital twins manually remains labor-intensive, and residual visual, geometric, and dynamics gaps hinder reliable sim-to-real transfer. We present DEXTERA, an automated real-to-sim-to-real framework that transforms a single RGB image into deployable policies for dexterous manipulation across four unified stages: (1) single-image scene factorization into a static Gaussian background and interactive rigid or articulated assets with VLM-inferred physical parameters; (2) metric scene global alignment, object canonicalization, and morphology-balanced robot calibration; (3) scalable simulator task primitive construction, VR teleoperation, and object-centric trajectory synthesis; and (4) a shared multimodal policy interface supporting both imitation learning and reinforcement learning. We evaluate DEXTERA across 13 task-embodiment pairs, 2 dexterous robot platforms, and 6 policy architectures. Experimental results demonstrate that DEXTERA achieves superior visual fidelity and 3D geometric reconstruction compared to generative baselines, while cross-domain trajectory replays validate strong physical interaction consistency. Furthermore, simulation-only trained policies enable viable zero-shot real-robot deployment, while simulation-real co-training substantially improves mean physical policy success from 29.2% to 61.9% across diverse policy architectures.

</details>

---

### [[20_Research/Papers/机器人/MAPLE-RF_Efficient_Probabilistic_RF_Source_Localization_in_Partially_Explored_Environments|MAPLE-RF: Efficient Probabilistic RF Source Localization in Partially Explored Environments]]

![[assets/2609.21026_figure.png|800]]

- **arXiv**: [2609.21026](https://arxiv.org/abs/2609.21026)
- **PDF**: https://arxiv.org/pdf/2609.21026
- **详细分析**: [[20_Research/Papers/机器人/MAPLE-RF_Efficient_Probabilistic_RF_Source_Localization_in_Partially_Explored_Environments|MAPLE-RF: Efficient Probabilistic RF Source Localization in Partially Explored Environments]]
- **作者**: Haozhe Lei, Sundeep Rangan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《MAPLE-RF: Efficient Probabilistic RF Source Localization in Partially Explored Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Localizing a radio-frequency (RF) transmitter from received signals often requires a model of the environment to predict how obstacles block and reflect the signal. In many robotic applications, however, only a partial map is available, particularly when a robot localizes the source while exploring with simultaneous localization and mapping (SLAM). We study single-snapshot transmitter localization on such partially explored maps and compare two approaches that output a posterior over transmitter locations. The first extends a digital-twin method, which ray-traces every candidate location, to partial maps by treating unexplored space as free and training on mixed map coverage. The second, MAPLE-RF, encodes estimated path angles of arrival and signal-to-noise ratios as grid channels aligned with map knownness, occupancy, and line-of-sight visibility, and a U-Net scores all candidate positions in one pass without simulating propagation at inference. Ray-tracing simulations of indoor environments indicate that training on mixed map coverage is essential for both approaches. The digital-twin approach is more accurate on most single-snapshot metrics, while MAPLE-RF comes close at a query cost that does not depend on the propagation model and is more than two orders of magnitude below a fresh full-grid query with general-purpose ray tracing. Both outperform Gaussian and Gaussian-mixture baselines, and on exploration routes guided by its own estimates, fused MAPLE-RF posteriors place more probability near the source than the compared methods. Code and data will be released.

</details>

---

### [[20_Research/Papers/具身智能/Catch_Me_If_You_Can_Real-Time_Feedback_Denoising_for_Responsive_VLAs|Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs]]

![[assets/2609.21022_figure.png|800]]

- **arXiv**: [2609.21022](https://arxiv.org/abs/2609.21022)
- **PDF**: https://arxiv.org/pdf/2609.21022
- **详细分析**: [[20_Research/Papers/具身智能/Catch_Me_If_You_Can_Real-Time_Feedback_Denoising_for_Responsive_VLAs|Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs]]
- **作者**: Yiheng Ji, Xingru Zhou, Luis Sentis, Mingyo Seo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Catch Me If You Can: Real-Time Feedback Denoising for Responsive VLAs》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：ControlNet, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown strong generalization in robotic manipulation by combining semantic knowledge from pretrained vision-language models with expressive action-generation policies. Diffusion-based action generators are particularly effective for modeling temporally coherent action chunks, but these chunks are typically executed open-loop after inference. This limits responsiveness when objects move, contacts change, or the scene evolves during execution. We propose VLA-Feedback, a two-timescale architecture that combines low-frequency diffusion planning with high-frequency visual feedback. Rather than fully denoising an action chunk before execution, VLA-Feedback retains its final denoising step as a lightweight feedback interface, allowing each action to be corrected using the latest observation before it is executed. This design preserves the expressiveness of the diffusion planner while enabling real-time action correction without rerunning the full vision-language diffusion model. VLA-Feedback matched GR00T on static LIBERO tasks while improving average success on dynamic simulation tasks from 27.5% to 85.0%. On real-robot tasks, it improved average success from 51% to 73%. Additional materials can be found on our project page: this https URL .

</details>

---

### [[20_Research/Papers/具身智能/Towards_Effective_Visual-Inertial_SLAM_with_Passive-Only_Sensors_for_Low-Cost_Autonomous_Underwater_Vehicles|Towards Effective Visual-Inertial SLAM with Passive-Only Sensors for Low-Cost Autonomous Underwater Vehicles]]

![[assets/2609.21015_figure.png|800]]

- **arXiv**: [2609.21015](https://arxiv.org/abs/2609.21015)
- **PDF**: https://arxiv.org/pdf/2609.21015
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Effective_Visual-Inertial_SLAM_with_Passive-Only_Sensors_for_Low-Cost_Autonomous_Underwater_Vehicles|Towards Effective Visual-Inertial SLAM with Passive-Only Sensors for Low-Cost Autonomous Underwater Vehicles]]
- **作者**: Grant Schwidder, David Widhalm, Junaed Sattar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Towards Effective Visual-Inertial SLAM with Passive-Only Sensors for Low-Cost Autonomous Underwater Vehicles》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Improvements to Visual-Inertial Simultaneous Localization and Mapping (VI-SLAM) for low-cost autonomous underwater vehicles (AUVs) are critical for transitioning advanced marine robotics from specialized labs to broader research and hobbyist applications. While high-end AUVs typically rely on expensive sensor suites - such as Doppler Velocity Logs (DVLs) and Ultra-Short Baseline (USBL) systems - this work demonstrates that robust, high-quality navigation is achievable using a sub-$10, 000(USD) platform equipped only with inexpensive consumer-grade sensors. By leveraging a similarly priced, open-source AUV, we evaluate the performance of stereo cameras, Micro-electromechanical System (MEMS)-based IMUs, and depth sensors in a fully unconstrained 6-degree-of-freedom (6-DOF) underwater environment. We analyze the efficacy of off-the-shelf SLAM packages and propose optimizations for sensor fusion to mitigate the visual and physical challenges of untethered underwater operation. Our results prove that a usable SLAM solution can be accessible to the masses, providing a benchmark for expectations in demanding, real-time maritime missions without the financial barrier of industrial-grade hardware.

</details>

---

### [[20_Research/Papers/具身智能/SPARROW_Survival-POMCP_for_Adaptive_Robot_Routing,_Observation,_and_Waiting|SPARROW: Survival-POMCP for Adaptive Robot Routing, Observation, and Waiting]]

![[assets/2609.21008_figure.png|800]]

- **arXiv**: [2609.21008](https://arxiv.org/abs/2609.21008)
- **PDF**: https://arxiv.org/pdf/2609.21008
- **详细分析**: [[20_Research/Papers/具身智能/SPARROW_Survival-POMCP_for_Adaptive_Robot_Routing,_Observation,_and_Waiting|SPARROW: Survival-POMCP for Adaptive Robot Routing, Observation, and Waiting]]
- **作者**: Hshmat Sahak, Aoran Jiao, Nicholas Rhinehart, Timothy D. Barfoot
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《SPARROW: Survival-POMCP for Adaptive Robot Routing, Observation, and Waiting》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Temporary obstacles that may block a robot's planned route create a sequential navigation problem: a robot must decide whether to wait for a blockage to clear, reroute, or acquire more information about the obstacle before acting. We formulate graph navigation among temporary obstacles as a partially observable semi-Markov decision process and introduce SPARROW, a belief-space planner built on Partially Observable Monte Carlo Planning (POMCP). SPARROW searches over traversal, observation, and finite-duration waiting actions while maintaining a particle belief over latent obstacle classes and clearance times. Class-conditioned survival models are learned online from both clearance observations and right-censored encounters where the robot reroutes before clearance is observed. A generative model simulates obstacle arrivals and clearances as each action unfolds, so the planner can account for blockages that may occur along alternative routes. We further introduce a value-of-learning criterion that trades the immediate cost of collecting labelled survival data against its expected reduction in future navigation regret. Across two simulation graphs and multiple obstacle-class settings, SPARROW reduces mean time-to-goal by 12-26% relative to OSCAR, a recent survival-based method for the same problem. On a physical mobile robot, SPARROW reduces mean time-to-goal by 20.5% relative to OSCAR while selectively observing, waiting, and rerouting as environment conditions change.

</details>

---

### [[20_Research/Papers/机器人/Project_SCOUT_Interceptor_Drone_for_Perimeter_Defense|Project SCOUT: Interceptor Drone for Perimeter Defense]]

![[assets/2609.21005_first_page.png|800]]

- **arXiv**: [2609.21005](https://arxiv.org/abs/2609.21005)
- **PDF**: https://arxiv.org/pdf/2609.21005
- **详细分析**: [[20_Research/Papers/机器人/Project_SCOUT_Interceptor_Drone_for_Perimeter_Defense|Project SCOUT: Interceptor Drone for Perimeter Defense]]
- **作者**: Azmain Yousuf, Siwei Cai, Knut Peterson, Lifeng Zhou, David Han
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: ComputerVision, Systems

#### 研究背景与动机

《Project SCOUT: Interceptor Drone for Perimeter Defense》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The rapid proliferation of unauthorized unmanned aerial vehicles (UAVs) has created a growing need for robust, jamming-resistant counter-UAV systems for perimeter defense. This paper presents \textbf{SCOUT} (Spatial Computation for Optimized UAV Tracking), a ROS-integrated onboard perception and control framework for real-time aerial defense against incoming UAVs. SCOUT performs visual detection, target association, track filtering, and control command generation directly onboard the defender UAV, without relying on external sensing infrastructure or ground-station computation. To provide stable control inputs, the perception pipeline combines TensorRT-accelerated drone detection with ByteTrack-based association and a lightweight track-retention state machine. The state machine rejects abrupt target jumps and maintains short-term target continuity during temporary detection degradation, reducing unstable control responses caused by false detections or target switching. We evaluate the proposed architecture through an integrated hardware deployment executing a planar ``goalkeeping'' interception strategy. In this setting, the defender UAV tracks the incoming target and adjusts its motion to maintain a blocking configuration near the protected boundary. Real-world flight results show that SCOUT maintains valid target detections for 92.2\% of frames while operating at real-time onboard detection rates, demonstrating the feasibility of visual tracking and closed-loop control for UAV perimeter defense. A video demonstration of the end-to-end perimeter defense operation is available online. this https URL

</details>

---

### [[20_Research/Papers/具身智能/PIVOT_Physically_Informed_Vision-Language_Off-Road_Traversability_for_Field_Robot_Navigation|PIVOT: Physically Informed Vision-Language Off-Road Traversability for Field Robot Navigation]]

![[assets/2609.20983_figure.png|800]]

- **arXiv**: [2609.20983](https://arxiv.org/abs/2609.20983)
- **PDF**: https://arxiv.org/pdf/2609.20983
- **详细分析**: [[20_Research/Papers/具身智能/PIVOT_Physically_Informed_Vision-Language_Off-Road_Traversability_for_Field_Robot_Navigation|PIVOT: Physically Informed Vision-Language Off-Road Traversability for Field Robot Navigation]]
- **作者**: Aoran Jiao, Wenda Zhao, Hshmat Sahak, Timothy D. Barfoot
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《PIVOT: Physically Informed Vision-Language Off-Road Traversability for Field Robot Navigation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ERFNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Terrain assessment is a critical capability for off-road mobile robots, enabling safe and reliable navigation through unstructured and geometrically complex environments. Conventional geometry-based terrain assessment is fast to compute but often overly conservative in unstructured environments. We present PIVOT: a Physically Informed Vision-Language Off-Road Traversability navigation system that augments conventional geometry-based planning with vision-language-model (VLM)-based semantic reasoning for field robots. To physically ground this assessment, we quantify how strongly the VLM's predicted traversal energy cost, robot vibration, and wheel slip correlate with real-world measurements and introduce a unified traversability score that weights each modality by its prediction-measurement correlation. For efficiency, we design a two-level navigation architecture that retains geometry-based planning as the nominal mode and invokes semantic replanning only when that mode fails to find a path. Across five repeated closed-loop trials on a mixed-terrain route totalling around $6.4$ km, the proposed system increases overall autonomy from $59.6\%$ to $97.0\%$, reduces human interventions from $11$ to $3$, and increases the mean distance between interventions (MDBI) from $69.2$ m to $412.9$ m compared with geometry-only navigation. These results demonstrate that physically grounded VLM-based terrain assessment can substantially extend autonomous navigation beyond the limitations of geometry alone, while preserving efficient geometric planning as the nominal mode.

</details>

---

### [[20_Research/Papers/具身智能/ForeTac-VLA_A_Forecasting-Based_Tactile-Vision-Language-Action_Model_for_Contact-Rich_Robotic_Manipulation|ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation]]

![[assets/2609.20980_first_page.png|800]]

- **arXiv**: [2609.20980](https://arxiv.org/abs/2609.20980)
- **PDF**: https://arxiv.org/pdf/2609.20980
- **详细分析**: [[20_Research/Papers/具身智能/ForeTac-VLA_A_Forecasting-Based_Tactile-Vision-Language-Action_Model_for_Contact-Rich_Robotic_Manipulation|ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation]]
- **作者**: Zhengyu Tao, Xin Li, Xin Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 5.1（加权：具身智能 3.9，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《ForeTac-VLA: A Forecasting-Based Tactile-Vision-Language-Action Model for Contact-Rich Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ForeTac-VLA, OpenVLA, TacVLA, URL, UniTacVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have demonstrated strong capabilities in robotic manipulation, yet their reliance on visual perception limits robustness in contact-rich environments, where critical physical interaction states may not be visually observable. Existing tactile-enhanced VLA methods improve physical grounding using observed tactile feedback, but most remain largely reactive rather than explicitly modeling how contact may evolve. Therefore, we propose ForeTac-VLA, a forecasting-based tactile-vision-language fusion model that predicts future tactile states to guide action generation. Specifically, ForeTac-VLA encodes recent tactile observations into temporal representations and integrates them with vision-language features through bidirectional cross-attention. Further, a transformer-based forecasting module predicts multi-step future tactile states, enabling the model to reason jointly over observed and anticipated contact. Finally, the fused multimodal representations and predicted future tactile states are fed into the VLA backbone to condition action generation. To stabilize training, a ground-truth-to-prediction curriculum is employed when early forecasts are unreliable. Across four real-world contact-rich manipulation tasks, ForeTac-VLA achieves an average success rate of 95%, outperforming the fine-tuned VLA model by 36.25 percentage points and state-of-the-art tactile-enhanced VLA baselines by over 22 percentage points. ForeTac-VLA also maintains strong performance under low-illumination and visually cluttered conditions. Video demonstrations can be found on this https URL

</details>

---

### [[20_Research/Papers/具身智能/Shake_to_Learn_Dynamic_Interrogation_of_Hidden_Object_Physics_for_Robotic_Manipulation_with_Physical_Reservoir_Computing|Shake to Learn: Dynamic Interrogation of Hidden Object Physics for Robotic Manipulation with Physical Reservoir Computing]]

![[assets/2609.20970_figure.png|800]]

- **arXiv**: [2609.20970](https://arxiv.org/abs/2609.20970)
- **PDF**: https://arxiv.org/pdf/2609.20970
- **详细分析**: [[20_Research/Papers/具身智能/Shake_to_Learn_Dynamic_Interrogation_of_Hidden_Object_Physics_for_Robotic_Manipulation_with_Physical_Reservoir_Computing|Shake to Learn: Dynamic Interrogation of Hidden Object Physics for Robotic Manipulation with Physical Reservoir Computing]]
- **作者**: Wen Sin Lor, Jun Wang, Suyi Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《Shake to Learn: Dynamic Interrogation of Hidden Object Physics for Robotic Manipulation with Physical Reservoir Computing》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many physical properties relevant to robotic manipulation are hidden from vision. A sealed object, for example, may reveal little about its center of mass (COM) or internal contents until it is lifted, shaken, or otherwise dynamically perturbed. This study shows that such interactions can enable a new modality of robotic perception and learning, in which interaction-induced dynamic responses are used to infer object physics that is inaccessible to conventional sensing. We implement this idea using an origami-inspired soft robotic arm that functions as a physical reservoir computer. After grasping an object, the arm is excited by a fixed shaking input at its base, and the resulting ringdown response is recorded through either camera tracking or embedded sensors. Because the input is held constant across trials, hidden object properties, such as the COM position, are encoded through their effect on the dynamics of the coupled robot-object system. A lightweight linear readout can then decode these dynamics to recover interpretable information about the hidden object physics. Using this framework, the soft robotic arm reservoir completed three tasks of increasing difficulty: inferring the orientation of the object's hidden COM, inferring the COM distance from the grasp point, and using the inferred COM information to guide a subsequent regrasp. We further develop a dynamic summary representation of the ringdown response that improves prediction accuracy. Together, these results establish shake-to-learn mechanical interrogation as a promising strategy for robotic systems to convert brief physical interactions into actionable cues about hidden object properties for downstream manipulation.

</details>

---

### [[20_Research/Papers/具身智能/AeRove_A_Compact_Bimodal_Aerial-Terrestrial_Drone_with_Rapid_Bistable_Reconfiguration_for_Close-Range_Pipeline_Inspection|AeRove: A Compact Bimodal Aerial-Terrestrial Drone with Rapid Bistable Reconfiguration for Close-Range Pipeline Inspection]]

![[assets/2609.20965_first_page.png|800]]

- **arXiv**: [2609.20965](https://arxiv.org/abs/2609.20965)
- **PDF**: https://arxiv.org/pdf/2609.20965
- **详细分析**: [[20_Research/Papers/具身智能/AeRove_A_Compact_Bimodal_Aerial-Terrestrial_Drone_with_Rapid_Bistable_Reconfiguration_for_Close-Range_Pipeline_Inspection|AeRove: A Compact Bimodal Aerial-Terrestrial Drone with Rapid Bistable Reconfiguration for Close-Range Pipeline Inspection]]
- **作者**: Caleb Polillio, Petras Swissler
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《AeRove: A Compact Bimodal Aerial-Terrestrial Drone with Rapid Bistable Reconfiguration for Close-Range Pipeline Inspection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Close-proximity pipeline inspection is challenging for standard drones due to high hovering power consumption, airflow sensitivity, and propeller wash interference with gas sensing. To address this, we present AeRove, a compact bimodal aerial-terrestrial robot. AeRove uses its propeller guards as wheels to roll along pipes and employs a spring-loaded bistable mechanism to reconfigure between ground and flight modes in 200 ms without continuous actuator power to maintain either state. The converging propeller-guard geometry also improves measured thrust efficiency. By reserving flight for obstacle hopping and using ground rolling for continuous traversal, current draw is reduced 14x compared to continuous flight (0.7 A vs. 10 A), extending estimated travel distance from 144 m to 2057 m. Autonomous trials on a 51 cm diameter steel pipe demonstrated navigation on straight and curved sections, obstacle jumping, and leak detection of simulated inspection markers. Separate CO2 sensing experiments evaluated gas-detection performance under perched and aerial operating conditions. Perched inspection produced a substantially larger concentration response than hovering under the tested conditions. During flight, an underbody propeller-intake configuration produced a faster and stronger gas-detection response than an extended probe by leveraging propeller-induced airflow. Code and designs are released under the CC-BY license.

</details>

---
