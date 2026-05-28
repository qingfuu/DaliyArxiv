# cs.RO | Robotics | 2026-05-26

#arxiv #ComputerScience

**论文数**: 23

### [[20_Research/Papers/具身智能/RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following|RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following]]

![[assets/2605.25851_figure.png|800]]

- **arXiv**: [2605.25851](https://arxiv.org/abs/2605.25851)
- **PDF**: https://arxiv.org/pdf/2605.25851
- **详细分析**: [[20_Research/Papers/具身智能/RePlan-Bot_Multi-Level_Replanning_for_Embodied_Instruction_Following|RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following]]
- **作者**: Xicheng Gong, Guozheng Sun, Peiran Xu, Yadong Mu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.3，机器人 0.3）
- **关联关键词**: LLM, Agent, EmbodiedAI

#### 研究背景与动机

《RePlan-Bot: Multi-Level Replanning for Embodied Instruction Following》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied instruction following (EIF) requires agents to understand and execute complex natural language commands within interactive 3D environments. Despite recent advances, existing methods often fail in long-horizon planning and handling irreversible state changes, resulting in low task success rates. To address these challenges, we introduce RePlan-Bot, a novel EIF agent that performs multi-level, continuous replanning throughout task execution. RePlan-Bot integrates a high-level LLM-based auditor for dynamic sub-goal adjustments guided by environmental feedback, a commonsense-guided search mechanism based on a multi-layered instance map for precise and structured object localization, and a lightweight ViT-based corrector to preemptively fix risky low-level actions. Evaluated on the ALFRED benchmark, RePlan-Bot achieves state-of-the-art performance in both seen and unseen environments, demonstrating superior adaptability and reliability.

</details>

---

### [[20_Research/Papers/具身智能/Extending_Embodied_Question_Answering_from_Perception_to_Decision|Extending Embodied Question Answering from Perception to Decision]]

![[assets/2605.25813_figure.png|800]]

- **arXiv**: [2605.25813](https://arxiv.org/abs/2605.25813)
- **PDF**: https://arxiv.org/pdf/2605.25813
- **详细分析**: [[20_Research/Papers/具身智能/Extending_Embodied_Question_Answering_from_Perception_to_Decision|Extending Embodied Question Answering from Perception to Decision]]
- **作者**: Xicheng Gong, Qiwei Li, Peiran Xu, Yadong Mu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.9（加权：具身智能 1.5，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, EmbodiedAI

#### 研究背景与动机

《Extending Embodied Question Answering from Perception to Decision》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EQA, Image-QA, RoboVQA, ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied Question Answering (EQA) connects perception, reasoning, and interaction within embodied environments. However, existing datasets and benchmarks remain fragmented, each focusing on a limited subset of reasoning skills such as spatial understanding or procedural reasoning, without offering a unified large-scale framework for comprehensive evaluation. We present EQA-Decision, a large-scale embodied QA dataset that systematically covers four complementary dimensions of embodied reasoning: static scene construction, spatial understanding, task dynamics reasoning, and instant decision. The dataset contains over four million question-answer pairs with hierarchical annotations across diverse embodied scenarios. In addition, we develop RoboDecision, a strong baseline model aligned with the EQA-Decision Benchmark, providing a unified framework that jointly evaluates perception, reasoning, and action-level decision-making in embodied environments. Results demonstrate that EQA-Decision effectively benchmarks and enhances VLM capabilities in spatial and interaction reasoning, providing a solid foundation for advancing embodied intelligence research.

</details>

---

### [[20_Research/Papers/具身智能/ParkourFormer_Integrating_Predictive_Supervision_and_Sequence_Modeling_into_Parkour_Locomotion|ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion]]

![[assets/2605.25782_figure.jpg|800]]

- **arXiv**: [2605.25782](https://arxiv.org/abs/2605.25782)
- **PDF**: https://arxiv.org/pdf/2605.25782
- **详细分析**: [[20_Research/Papers/具身智能/ParkourFormer_Integrating_Predictive_Supervision_and_Sequence_Modeling_into_Parkour_Locomotion|ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion]]
- **作者**: Yanheng Mai, Wenhao Xu, Zirui Huang, Yifei Fu, Shengwei Dong, Xinjue Wang, Kailun Huang, Yanzhe Xie, Renjing Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.7（加权：具身智能 1.8，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ParkourFormer: Integrating Predictive Supervision and Sequence Modeling into Parkour Locomotion》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid parkour requires locomotion policies to coordinate whole-body dynamics across rapidly changing terrains such as stairs, gaps, slopes, and obstacles. Existing reinforcement learning policies are largely reactive, mapping observations directly to actions without explicitly modeling future body states. Such modeling becomes critical in agile locomotion tasks where successful motion execution depends strongly on anticipating upcoming contact transitions and body dynamics. We present ParkourFormer, a Transformer-based sequence modeling framework that reformulates humanoid locomotion as a future-conditioned decision-making problem. The current robot state queries historical sensorimotor trajectories through cross-attention, while a lightweight prediction head forecasts short-horizon future proprioceptive states. The predicted future states, trained with supervised signals, are fused with temporal features to generate actions, enabling the policy to jointly reason over motion history and anticipated future dynamics. We evaluate ParkourFormer on a diverse multi-terrain humanoid parkour benchmark including stairs, gaps, slopes, rough terrain, and obstacle traversal. Experiments in simulation and on a real humanoid robot show that ParkourFormer achieves a 93.85% average traversal success rate on highly challenging terrains, with improvements of up to 42.73% over strong MLP, MoE-based MLP, and vanilla Transformer baselines, while maintaining a single unified policy across all terrain types. These results demonstrate that explicit future-state modeling significantly improves robustness and generalization for agile whole-body locomotion.

</details>

---

### [[20_Research/Papers/机器人/Implicit_Null-space_Manifold_Generation_for_Redundant_Robotic_Systems|Implicit Null-space Manifold Generation for Redundant Robotic Systems]]

![[assets/2605.25770_figure.png|800]]

- **arXiv**: [2605.25770](https://arxiv.org/abs/2605.25770)
- **PDF**: https://arxiv.org/pdf/2605.25770
- **详细分析**: [[20_Research/Papers/机器人/Implicit_Null-space_Manifold_Generation_for_Redundant_Robotic_Systems|Implicit Null-space Manifold Generation for Redundant Robotic Systems]]
- **作者**: Taiki Ishigaki, Teresa Vidal-Calleja, Ko Ayusawa, Eiichi Yoshida
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Implicit Null-space Manifold Generation for Redundant Robotic Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic systems with redundant degrees of freedom can achieve the same task outcome using multiple configurations, resulting in solution sets that form manifolds in the configuration space. Existing approaches typically exploit such redundancy locally through Jacobian-based techniques to compute individual solutions or trajectories. While effective for solution computation, these methods do not retain a representation of the geometry of the solution set itself. In this work, we adopt a representation-centric approach to estimate the geometric structure of the solution space. We consider solution manifolds induced by general task-defining maps and construct an implicit scalar field over the configuration space, whose zero-level set corresponds to the solution manifold. To this end, we generate samples in the neighborhood of the solution manifold using a Jacobian-guided exploration strategy, which efficiently captures its local and global structure. The resulting implicit representation is defined over the configuration space and naturally induces a continuous, distance field that encodes proximity to the solution manifold. Experiments on a planar three-link robot and a seven-degree-of-freedom Franka manipulator demonstrate the effectiveness of the proposed representation. Furthermore, the framework enables consistent modeling of solution spaces across families of tasks with continuous variation.

</details>

---

### [[20_Research/Papers/具身智能/Compliant_Non-Prehensile_Pushing_Manipulation|Compliant Non-Prehensile Pushing Manipulation]]

![[assets/2605.25672_figure.png|800]]

- **arXiv**: [2605.25672](https://arxiv.org/abs/2605.25672)
- **PDF**: https://arxiv.org/pdf/2605.25672
- **详细分析**: [[20_Research/Papers/具身智能/Compliant_Non-Prehensile_Pushing_Manipulation|Compliant Non-Prehensile Pushing Manipulation]]
- **作者**: Francesco Cufino, Mario Selvaggio, Fabio Amadio, Fabio Ruggiero
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Compliant Non-Prehensile Pushing Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this paper, we address the challenge of performing non-prehensile pushing operations with a compliant robotic manipulation system. To ensure safe operations in human-populated environments, robots must comply with external physical interactions and exhibit passive behavior. To achieve this, we extend a state-of-the-art pushing model to integrate it with impedance-controlled robots. We develop a model predictive control framework built upon this model that enables compliant pushing through optimal modulation of the robot's position/velocity set-point, jointly realizing the required pushing force and contact point adaptation to obtain desired object motion. However, external interactions may induce tracking errors, causing a consequent potentially indefinite increase of the pushing force. To prevent this, we integrate an energy tank passivity filter that further modulates the robot velocity set-point to guarantee passivity and avoid uncontrolled energy buildup. The proposed method has been rigorously tested in simulation and validated through experiments on two different robotic systems, demonstrating passive compliance during human-robot interactions and assessing trajectory tracking performance and robustness to variations in the object's physical parameters.

</details>

---

### [[20_Research/Papers/具身智能/G-DRAGON_Geospatial_Reasoning_and_Dynamic_Planning_for_Retrieval-Augmented_Outdoor_Navigation|G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation]]

![[assets/2605.25646_figure.png|800]]

- **arXiv**: [2605.25646](https://arxiv.org/abs/2605.25646)
- **PDF**: https://arxiv.org/pdf/2605.25646
- **详细分析**: [[20_Research/Papers/具身智能/G-DRAGON_Geospatial_Reasoning_and_Dynamic_Planning_for_Retrieval-Augmented_Outdoor_Navigation|G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation]]
- **作者**: Dongzhihan Wang, Yi Du, Jianan Sun, Yuan Xue, Yingchen Zhang, Bing Xiao, Chen Wang, Liang Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.5，机器人 0.7）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《G-DRAGON: Geospatial Reasoning and Dynamic Planning for Retrieval-Augmented Outdoor Navigation》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：GeoQA, OpenBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous ground robots operating in large-scale outdoor environments require both robust long-range navigation and fine-grained ''last-mile'' exploration. Current advances in visual-language navigation (VLN) work well at short-range tasks, lacking geospatial grounding for long-distance missions. Some OpenStreetMap (OSM)-based methods relying on cloud-based Large Language Models (LLMs) are prone to factual hallucination and cannot conduct ''last-mile'' exploration based on human instruction. To address these challenges, we present G-DRAGON, a retrieval-augmented framework for outdoor, open-world navigation. This framework maps natural-language commands to versioned, local OSM entities via generative retrieval based on lightweight LLM, yielding accurate coordinates for global route planning. A high-level planning module bridges global topological routes with the SLAM system, projecting geospatial waypoints into the robot's navigable frame. For the ''last mile," the framework transitions to frontier-based exploration and open-set semantic voxel mapping to localize open-vocabulary targets. Experimental results in simulation demonstrate our framework outperforms state-of-the-art baselines. Furthermore, we validate the system in unseen real-world urban environments on an Unmanned Ground Vehicle (UGV), successfully completing person-search missions with trajectories of up to 500m.

</details>

---

### [[20_Research/Papers/具身智能/Safety-Critical_Whole-Body_Control_for_Humanoid_Robots_via_Input-to-State_Safe_Control_Barrier_Functions|Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions]]

![[assets/2605.25546_first_page.png|800]]

- **arXiv**: [2605.25546](https://arxiv.org/abs/2605.25546)
- **PDF**: https://arxiv.org/pdf/2605.25546
- **详细分析**: [[20_Research/Papers/具身智能/Safety-Critical_Whole-Body_Control_for_Humanoid_Robots_via_Input-to-State_Safe_Control_Barrier_Functions|Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions]]
- **作者**: Kwanwoo Lee, Sanghyuk Park, Gyeongjae Park, Myeong-Ju Kim, Jaeheung Park
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Safety-Critical Whole-Body Control for Humanoid Robots via Input-to-State Safe Control Barrier Functions》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety-critical control is essential for humanoid robots operating in complex human-centered environments, where physical safety constraints such as joint limits, self-collision avoidance, obstacle avoidance, and workspace boundaries must be satisfied during real-robot operation. However, existing approaches remain limited because kinematic safety guarantees can be degraded in the presence of unknown disturbances, such as model uncertainties, trajectory-tracking errors, and external perturbations. This paper presents a hierarchical safety-critical whole-body control framework for humanoid robots based on input-to-state safe control barrier functions (ISSf-CBFs). The proposed architecture integrates a kinematic-level whole-body controller (KinWBC), an ISSf-CBF safety filter, and a dynamic-level whole-body controller (DynWBC). KinWBC generates nominal joint-motion references from prioritized tasks; the ISSf-CBF filter minimally modifies these references to satisfy kinematic safety constraints under bounded disturbances; and DynWBC tracks the filtered references while enforcing full-body dynamic feasibility and contact stability. Safety constraints are imposed on a whole-body kinematic model, and the ISSf-CBF parameters are conservatively tuned so that the resulting kinematic safety guarantees can be transferred to full-order humanoid dynamics under unknown disturbances. Simulation and real-robot experiments demonstrate that the proposed framework improves safety margins under model mismatch and reliably enforces multiple safety constraints in real time during locomotion, teleoperation, and single-leg balancing with hand control. Project website: this https URL

</details>

---

### [[20_Research/Papers/强化学习/How_to_Mitigate_the_Distribution_Shift_Problem_in_Robotics_Control_A_Robust_and_Adaptive_Approach_Based_on_Offline_to_Online_Imitation_Learn|How to Mitigate the Distribution Shift Problem in Robotics Control: A Robust and Adaptive Approach Based on Offline to Online Imitation Learning]]

![[assets/2605.25414_figure.png|800]]

- **arXiv**: [2605.25414](https://arxiv.org/abs/2605.25414)
- **PDF**: https://arxiv.org/pdf/2605.25414
- **详细分析**: [[20_Research/Papers/强化学习/How_to_Mitigate_the_Distribution_Shift_Problem_in_Robotics_Control_A_Robust_and_Adaptive_Approach_Based_on_Offline_to_Online_Imitation_Learn|How to Mitigate the Distribution Shift Problem in Robotics Control: A Robust and Adaptive Approach Based on Offline to Online Imitation Learning]]
- **作者**: Hyung-Suk Yoon, Seung-Woo Seo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《How to Mitigate the Distribution Shift Problem in Robotics Control: A Robust and Adaptive Approach Based on Offline to Online Imitation Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Distribution shift in imitation learning refers to the problem that the agent cannot plan proper actions for a state that has not been visited during the training. This problem can be largely attributed to the inherently narrow state-action coverage provided by expert demonstrations over the full environment. In this paper, we propose a robust offline to adaptive online imitation learning framework that handles the distribution shift problem in a lifelong, multi-phase scheme. In the offline learning phase, we leverage supplementary demonstrations to broaden the state-action coverage of the policy by utilizing a discriminator to effectively train the policy with supplementary demonstrations, thereby enhancing the robustness of the policy to distribution shift. In the subsequent online inference phase, our framework detects the occurrence of distribution shift and conducts self-supervised imitation learning from online experiences to adapt the policy to the online environments. Through extensive evaluations in MuJoCo environments, we demonstrate that our method exhibits better robustness to distribution shift and better adaptation performance to online environments than the baseline algorithms, which indicates superior performance of our framework against the distribution shift.

</details>

---

### [[20_Research/Papers/机器人/Path_Following_Control_System_of_Line-of-Sight_Guidance_for_Robotic_Dolphin_with_Multi-Link_Mechanism_in_Underwater_Simulator|Path Following Control System of Line-of-Sight Guidance for Robotic Dolphin with Multi-Link Mechanism in Underwater Simulator]]

![[assets/2605.25401_figure.jpg|800]]

- **arXiv**: [2605.25401](https://arxiv.org/abs/2605.25401)
- **PDF**: https://arxiv.org/pdf/2605.25401
- **详细分析**: [[20_Research/Papers/机器人/Path_Following_Control_System_of_Line-of-Sight_Guidance_for_Robotic_Dolphin_with_Multi-Link_Mechanism_in_Underwater_Simulator|Path Following Control System of Line-of-Sight Guidance for Robotic Dolphin with Multi-Link Mechanism in Underwater Simulator]]
- **作者**: Takumi Asada, Takao Oki, Hideo Furuhashi, Kenta Tabata, Renato Miyagusuku, Koichi Ozaki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Path Following Control System of Line-of-Sight Guidance for Robotic Dolphin with Multi-Link Mechanism in Underwater Simulator》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Biomimetic autonomous underwater vehicle (BAUV) with multi-link mechanism is widely used in aquatic life observation and environmental surveys due to its low power consumption and high maneuverability. An environmental survey requires a path following system that automatically follows specific points. However, the path following system of BAUV is limited, and its evaluation with multi-link mechanism robots has not yet been clarified. The path following system in BAUV requires prior simulation because the model differs depending on the type of biomimetics. In this study, we propose a path following system for BAUVs with a multi-link mechanism and evaluation in underwater simulation. In this result, it was possible to design a path following system suitable for BAUV, determine parameters using a simulator, and evaluate control methods.

</details>

---

### [[20_Research/Papers/机器人/FusionCore_A_23-State_Unscented_Kalman_Filter_for_IMU,_Wheel_Encoder,_GPS,_and_Visual_SLAM_Fusion_in_ROS_2|FusionCore: A 23-State Unscented Kalman Filter for IMU, Wheel Encoder, GPS, and Visual SLAM Fusion in ROS 2]]

![[assets/2605.25239_figure.png|800]]

- **arXiv**: [2605.25239](https://arxiv.org/abs/2605.25239)
- **PDF**: https://arxiv.org/pdf/2605.25239
- **详细分析**: [[20_Research/Papers/机器人/FusionCore_A_23-State_Unscented_Kalman_Filter_for_IMU,_Wheel_Encoder,_GPS,_and_Visual_SLAM_Fusion_in_ROS_2|FusionCore: A 23-State Unscented Kalman Filter for IMU, Wheel Encoder, GPS, and Visual SLAM Fusion in ROS 2]]
- **作者**: Manan Kharwar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，机器人 2.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《FusionCore: A 23-State Unscented Kalman Filter for IMU, Wheel Encoder, GPS, and Visual SLAM Fusion in ROS 2》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present FusionCore, an open-source ROS 2 sensor fusion package that fuses IMU, wheel encoder odometry, GPS, and Visual SLAM pose into a single 100 Hz odometry stream using a 23-state Unscented Kalman Filter (UKF). The 23rd state is an online estimate of the wheel encoder's systematic yaw rate bias, identified through GPS heading cross-covariance and subtracted during GPS blackouts to reduce heading drift in coast mode. FusionCore also estimates gyroscope and accelerometer biases as explicit filter states, handles GPS natively in ECEF without a separate coordinate projection node, applies per-sensor Mahalanobis chi-squared outlier gating calibrated to measurement degrees of freedom, and adapts sensor noise covariance automatically from the innovation sequence. VSLAM pose fusion enables GPS-denied operation with any visual odometry or SLAM system, including automatic recovery from map reinitialization. We evaluate against robot_localization on twelve full-length sequences (55-92 min each) from the NCLT public dataset. FusionCore achieves lower Absolute Trajectory Error (ATE) on ten of twelve sequences, with improvements ranging from 1.2x to 22.2x on winning sequences. The robot_localization UKF diverges numerically on all twelve sequences. FusionCore is available at this https URL under the Apache 2.0 license.

</details>

---

### [[20_Research/Papers/机器人/Soft_Pneumatic_Actuators_for_Soft_Robotics_A_Motion-Based_Review_of_Actuation_Mechanisms_and_Performance_Trade-offs|Soft Pneumatic Actuators for Soft Robotics: A Motion-Based Review of Actuation Mechanisms and Performance Trade-offs]]

![[assets/2605.25109_first_page.png|800]]

- **arXiv**: [2605.25109](https://arxiv.org/abs/2605.25109)
- **PDF**: https://arxiv.org/pdf/2605.25109
- **详细分析**: [[20_Research/Papers/机器人/Soft_Pneumatic_Actuators_for_Soft_Robotics_A_Motion-Based_Review_of_Actuation_Mechanisms_and_Performance_Trade-offs|Soft Pneumatic Actuators for Soft Robotics: A Motion-Based Review of Actuation Mechanisms and Performance Trade-offs]]
- **作者**: Mohammed Abboodi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Soft Pneumatic Actuators for Soft Robotics: A Motion-Based Review of Actuation Mechanisms and Performance Trade-offs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：可见文本中未给出明确实验数字或完整对比表。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft pneumatic actuators are widely used in soft robotics because they can produce large motions while remaining compliant enough to interact safely with objects, environments, and the human body. However, their performance is not solely determined by pressure. Instead, the response depends on the way the actuator is built, including the shape of its chambers, the placement of reinforcements, the use of folds, material stiffness, and the constraints that guide its deformation. As the literature has expanded, it has become more difficult to determine which mechanism is most suitable for a given application and which reported results can be compared across studies. This review examines soft pneumatic actuators according to the design strategies used to generate four motion classes: linear, bending, twisting, and omnidirectional actuation. For each class, it analyzes the structural features that define the deformation path, including braid angle, fold geometry, fiber orientation, chamber arrangement, structural asymmetry, and internal constraint layers. It then discusses how the design choice affect motion output, force generation, air demand, repeatability, durability, fabrication difficulty, and robotic integration. The review further identifies key conditions that must be considered when selecting or comparing actuators, including pressure, loading condition, actuator size, pneumatic supply, and hysteresis This approach helps explain why actuators with similar motion outputs may differ substantially in design requirements, pneumatic demand, and practical suitability. It also highlights the design priorities needed for compact, efficient, repeatable, and deployable soft pneumatic systems in wearable, biomedical, and mobile robotic applications.

</details>

---

### [[20_Research/Papers/机器人/A_Decentralized_LiDAR-SLAM_System_with_Certifiably_Optimal_Pose_Graph_Optimization|A Decentralized LiDAR-SLAM System with Certifiably Optimal Pose Graph Optimization]]

![[assets/2605.25051_figure.png|800]]

- **arXiv**: [2605.25051](https://arxiv.org/abs/2605.25051)
- **PDF**: https://arxiv.org/pdf/2605.25051
- **详细分析**: [[20_Research/Papers/机器人/A_Decentralized_LiDAR-SLAM_System_with_Certifiably_Optimal_Pose_Graph_Optimization|A Decentralized LiDAR-SLAM System with Certifiably Optimal Pose Graph Optimization]]
- **作者**: Baoshan Song, Feng Huang, Li-Ta Hsu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A Decentralized LiDAR-SLAM System with Certifiably Optimal Pose Graph Optimization》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Decentralized multi-robot LiDAR-SLAM is essential for collaborative missions but faces significant challenges in maintaining global consistency. Existing frameworks predominantly rely on local-search optimization or one-time coordinate alignment, which are prone to suboptimal convergence and long-term inconsistency, especially in large-scale or degenerate environments. To address these limitations, this paper presents the first decentralized LiDAR-SLAM system that integrates a state-of-the-art certifiably optimal Pose Graph Optimization (PGO) backend. By leveraging the Riemannian Block Coordinate Descent (RBCD) algorithm, our system ensures globally consistent trajectory estimation without requiring accurate initial guesses. Experimental results demonstrate that the proposed framework achieves superior robustness, improving trajectory RMSE by up to 48.9% compared to the state-of-the-art DiSCo-SLAM.

</details>

---

### [[20_Research/Papers/具身智能/X-DiffVLA_X-Embodied_Diffusion_Action_Heads_for_Vision-Language-Action_Models|X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models]]

![[assets/2605.25044_figure.png|800]]

- **arXiv**: [2605.25044](https://arxiv.org/abs/2605.25044)
- **PDF**: https://arxiv.org/pdf/2605.25044
- **详细分析**: [[20_Research/Papers/具身智能/X-DiffVLA_X-Embodied_Diffusion_Action_Heads_for_Vision-Language-Action_Models|X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models]]
- **作者**: Boyu Li, Chaoyi Xu, Haoqi Yuan, Xinrun Xu, Börje F. Karlsson, Dongbin Zhao, Haoran Li, Zongqing Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 4.0（加权：具身智能 3.3，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《X-DiffVLA: X-Embodied Diffusion Action Heads for Vision-Language-Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, X-DiffVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning universal policies from cross-embodied data remains a fundamental challenge in robotics. Although Vision-Language-Action (VLA) models are pre-trained on large and diverse datasets, they typically rely on embodiment-specific fine-tuning to achieve strong performance in downstream tasks. This requirement severely limits their generalization capability and restricts knowledge transfer across embodiments performing similar tasks. To overcome these limitations, we focus on cross-embodied settings with shared robotic bases and heterogeneous end-effectors, and propose X-DiffVLA, a diffusion-based VLA model featuring a unified cross-embodied action head. X-DiffVLA can leverage the generative strengths of diffusion models to capture both the diversity and latent correlations in cross-embodied datasets. Specifically, we introduce Embodiment Forcing, a classifier-free guidance technique to implicitly steer action generation toward embodiment-specific functional components, capturing fine-grained structural nuances without explicit supervision. In addition, a Morphological Tree Diffusion approach is designed to strengthen behavioral correlations across diverse end-effectors, maximizing the transferability of heterogeneous demonstrations. Experimental results across RoboCasa and Isaac Gym, covering different embodiments from grippers to dexterous hands, show that X-DiffVLA achieves state-of-the-art performance, with improvements of 15.3% and 12.5%, respectively. Real-world evaluations further validate the robustness of the proposed framework and its effectiveness in scalable cross-embodied policy learning.

</details>

---

### [[20_Research/Papers/具身智能/Micro-Swarm_Locomotion_Optimization_in_Dynamic_Flow_using_Multi-Objective_Multi-Agent_Reinforcement_Learning|Micro-Swarm Locomotion Optimization in Dynamic Flow using Multi-Objective Multi-Agent Reinforcement Learning]]

![[assets/2605.25025_figure.png|800]]

- **arXiv**: [2605.25025](https://arxiv.org/abs/2605.25025)
- **PDF**: https://arxiv.org/pdf/2605.25025
- **详细分析**: [[20_Research/Papers/具身智能/Micro-Swarm_Locomotion_Optimization_in_Dynamic_Flow_using_Multi-Objective_Multi-Agent_Reinforcement_Learning|Micro-Swarm Locomotion Optimization in Dynamic Flow using Multi-Objective Multi-Agent Reinforcement Learning]]
- **作者**: Josef Berman, Oren Gal
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 大模型, 机器人
- **相关性评分**: 3.2（加权：具身智能 1.2，大模型 0.5，强化学习 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Micro-Swarm Locomotion Optimization in Dynamic Flow using Multi-Objective Multi-Agent Reinforcement Learning》归入 具身智能、强化学习、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CFD-MARL, CFD-MO-MARL, CommNet, MARL, MO-MARL, MORL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coordinating micro-robotic swarms in physiologically realistic, time-dependent fluid environments remains an unsolved challenge for biomedical and environmental applications. We present a hybrid Computational Fluid Dynamics - Multi-Objective Multi-Agent Reinforcement Learning framework that directly couples a high-fidelity incompressible Navier-Stokes solver with decentralized proximal policy optimization to learn physically consistent swarm control strategies in oscillatory flow. Sixteen magnetically actuated micro-robots navigate a pulsatile arterial waveform, simultaneously optimizing upstream progression, energy conservation, and motion smoothness, reconciled using PCGrad surgery. Without PCGrad, energy efficiency and smoothness rewards collapse to near zero within 10,000 training steps while progress exhibits persistent large-amplitude oscillations, confirming that gradient conflict resolution is a structural requirement rather than an optional refinement in this domain. The converged policy achieves a progress reward of 6.5-7.0, a sustained energy efficiency of 0.63-0.65, and near-maximum smoothness (0.97-0.99), representing improvements over brute-force baselines on the primary objective while both baselines yield negative energy efficiency throughout. Training reveals three emergent behavioral phases: a collective two-layer hydrodynamic throttling formation that suppresses peak channel velocities during forward flow, a cycle-synchronized ratchet mechanism that exploits flow reversals for upstream repositioning, and an individualized final approach as agents near the success boundary. These results establish that time-dependent fluid-agent interactions can be captured directly within multi-objective reinforcement learning loops, offering a physically grounded paradigm for micro-swarm control in biomedical navigation, environmental monitoring, and industrial microfluidics.

</details>

---

### [[20_Research/Papers/具身智能/Dynamic_Neural_Koopman_Distillation_for_Real-Time_Robot_Control_Using_Diffusion_Models|Dynamic Neural Koopman Distillation for Real-Time Robot Control Using Diffusion Models]]

![[assets/2605.24924_figure.png|800]]

- **arXiv**: [2605.24924](https://arxiv.org/abs/2605.24924)
- **PDF**: https://arxiv.org/pdf/2605.24924
- **详细分析**: [[20_Research/Papers/具身智能/Dynamic_Neural_Koopman_Distillation_for_Real-Time_Robot_Control_Using_Diffusion_Models|Dynamic Neural Koopman Distillation for Real-Time Robot Control Using Diffusion Models]]
- **作者**: Lei Zheng, Peiqi Yu, Zengqi Peng, Changliu Liu, Armin Lederer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Dynamic Neural Koopman Distillation for Real-Time Robot Control Using Diffusion Models》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：D4RL, Real-World, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Diffusion models excel at generating diverse and multimodal trajectories for robotic planning, yet their iterative denoising process introduces latency that is incompatible with high-frequency closed-loop control. To address this problem, we propose Dynamic Neural Koopman Distillation, a framework that distills multistep diffusion inference into a single forward pass while retaining the multimodal expressivity of the teacher model. Specifically, we introduce a Factorized Dynamic Koopman layer that models the denoising process through a factorized latent transition with state-dependent modal gains. We evaluate the proposed method on standard D4RL MuJoCo locomotion benchmarks and a physical Kinova manipulator, comparing against one-step baselines. The results show that our method significantly outperforms existing one-step distillation approaches on the reported locomotion tasks, and reduces the inference latency to the millisecond regime compared with the teacher policy. Hardware experiments further demonstrate that our method enables smooth and fast closed-loop execution while maintaining task success and comparable accuracy. A project page is available at this https URL .

</details>

---

### [[20_Research/Papers/大模型/Learning_Transferable_Motor_Skills_for_Geometry-Aware_Robotic_Surface_Tasks|Learning Transferable Motor Skills for Geometry-Aware Robotic Surface Tasks]]

![[assets/2605.24881_figure.png|800]]

- **arXiv**: [2605.24881](https://arxiv.org/abs/2605.24881)
- **PDF**: https://arxiv.org/pdf/2605.24881
- **详细分析**: [[20_Research/Papers/大模型/Learning_Transferable_Motor_Skills_for_Geometry-Aware_Robotic_Surface_Tasks|Learning Transferable Motor Skills for Geometry-Aware Robotic Surface Tasks]]
- **作者**: Miroslav David, Karla Stepanova, Robert Babuska
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Learning Transferable Motor Skills for Geometry-Aware Robotic Surface Tasks》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：PaintNet, PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic surface-interaction tasks, such as spray painting or welding, require both accurate geometric planning and precise motion execution. While modern motion planners generate valid geometric paths, they often lack the expert motor patterns observed in human operators. Conversely, learning from demonstration often tightly couples task execution to the specific training geometry, limiting transferability. We propose a modular framework that decouples geometric motion planning from execution-level expertise. Expert behavior is represented as a vocabulary of interpretable, atomic motor rules, such as velocity scaling and orientation offsets, that systematically modify a geometrically planned reference path. We train a multimodal neural network to infer rule parameters jointly from kinematic trajectory data and CAD model geometry. We evaluate our approach through dynamic simulation on L-shaped and window-shaped objects, demonstrating on simulated data that the model successfully extracts velocity and orientation rules across both topologies.

</details>

---

### [[20_Research/Papers/具身智能/Towards_Low-Gravity_Planetary_Exploration_using_Reinforcement_Learning_for_Walking,_Jumping,_and_In-flight_Attitude_Control|Towards Low-Gravity Planetary Exploration using Reinforcement Learning for Walking, Jumping, and In-flight Attitude Control]]

![[assets/2605.24643_figure.png|800]]

- **arXiv**: [2605.24643](https://arxiv.org/abs/2605.24643)
- **PDF**: https://arxiv.org/pdf/2605.24643
- **详细分析**: [[20_Research/Papers/具身智能/Towards_Low-Gravity_Planetary_Exploration_using_Reinforcement_Learning_for_Walking,_Jumping,_and_In-flight_Attitude_Control|Towards Low-Gravity Planetary Exploration using Reinforcement Learning for Walking, Jumping, and In-flight Attitude Control]]
- **作者**: Jørgen Anker Olsen, Kostas Alexis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 强化学习, 机器人
- **相关性评分**: 2.2（加权：具身智能 0.9，强化学习 0.8，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Towards Low-Gravity Planetary Exploration using Reinforcement Learning for Walking, Jumping, and In-flight Attitude Control》归入 具身智能、强化学习、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、强化学习、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：DRL, URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents reinforcement learning (RL) policies for dynamic quadrupedal locomotion in planetary exploration scenarios. Building on a taskoptimized quadruped with a 5-bar leg design, we develop RL policies for walking, vertical jumping, forward jumping, and in-flight attitude control, explicitly tailored to the reduced gravity on Mars. These policies jointly enable such robots to overcome obstacles larger than themselves through coordinated jumping and precise in-flight reorientation for safe landings. We demonstrate Sim2Real transfer of the attitude control policy on the Olympus quadruped through single-axis reorientation tests, while all locomotion policies are validated in simulation. A complete Mars exploration mission scenario demonstrates coordinated policy deployment across challenging terrain. Experimental results show 90° attitude reorientation in 2.6 seconds, with simulations demonstrating 3.1 meter vertical jumps and 3.9 meter forward jumps under Martian gravity conditions. - Supplementary video: this https URL

</details>

---

### [[20_Research/Papers/具身智能/MuGen_Multi-Skill_Generative_Locomotion_Controller_for_Humanoid_Robots|MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots]]

![[assets/2605.24592_first_page.png|800]]

- **arXiv**: [2605.24592](https://arxiv.org/abs/2605.24592)
- **PDF**: https://arxiv.org/pdf/2605.24592
- **详细分析**: [[20_Research/Papers/具身智能/MuGen_Multi-Skill_Generative_Locomotion_Controller_for_Humanoid_Robots|MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots]]
- **作者**: Yusen Feng, Xiang Wang, Heyuan Yao, Zixi Kang, Xinyu Huo, Boyang Yu, Pengyun Qiu, Ruijie Zhao, Baoquan Chen, Libin Liu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习, 世界模型
- **相关性评分**: 4.4（加权：具身智能 2.7，强化学习 0.2，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《MuGen: Multi-Skill Generative Locomotion Controller for Humanoid Robots》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents MuGen, a data-driven framework for learning and deploying multi-skill locomotion on humanoid robots. MuGen enables a robot to perform expressive motions like humans under the guidance of example motion sequences. To achieve this, we employ vector-quantized autoencoders (VQ-VAEs) trained with model-based reinforcement learning, resulting in a generative representation of locomotion that captures key patterns of human motion from hours of heterogeneous human performance data. We employ a teacher-student learning framework and develop a new policy distillation strategy to enable a deployable student policy learning this efficient latent representation. This policy allows the robot to track and mimic unseen human motions and further enables the robot to reuse the learned latent space for other tasks. We demonstrate the effectiveness of our framework through a diverse set of motions and accurate execution.

</details>

---

### [[20_Research/Papers/具身智能/Polymander_II_an_amphibious_salamander-inspired_robot_with_contact_and_flow_sensors|Polymander II: an amphibious salamander-inspired robot with contact and flow sensors]]

![[assets/2605.24465_figure.png|800]]

- **arXiv**: [2605.24465](https://arxiv.org/abs/2605.24465)
- **PDF**: https://arxiv.org/pdf/2605.24465
- **详细分析**: [[20_Research/Papers/具身智能/Polymander_II_an_amphibious_salamander-inspired_robot_with_contact_and_flow_sensors|Polymander II: an amphibious salamander-inspired robot with contact and flow sensors]]
- **作者**: Qiyuan Fu, Sudong Lee, Andrea Grillo, Jonathan Arreguit, Louis Gevers, Josie Hughes, Auke J. Ijspeert
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Polymander II: an amphibious salamander-inspired robot with contact and flow sensors》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots benefit from sensory information to coordinate body movement, gain robustness against perturbations, and transit between different modes to adapt to various terrains. However, few amphibious robots can sense interactions with both terrestrial and aquatic environments. In this paper, we present a solution that uses Hall-effect sensors to sense foot contact forces and lateral hydrodynamic forces on a salamander-inspired amphibious robot. With two bus lines, the robot can simultaneously acquire this exteroceptive information at more than 500 Hz and proprioceptive information, such as joint positions and loads, at 100 Hz. The Hall-effect sensors used are compact, making them suitable for embedding in multiple positions within a robot, and exhibit high sensitivity to small forces. Moreover, because the sensor can be positioned separately from the measured object, waterproofing can be implemented with relative ease. Our tests demonstrate the robot's capabilities in traversing amphibious environments and its potential in using feedback control for more complex locomotion tasks.

</details>

---

### [[20_Research/Papers/强化学习/IsaacIPC_Coupling_High-Fidelity_Simulation_and_Realistic_Rendering_for_Contact-Rich_Robotic_Systems|IsaacIPC: Coupling High-Fidelity Simulation and Realistic Rendering for Contact-Rich Robotic Systems]]

![[assets/2605.24339_figure.png|800]]

- **arXiv**: [2605.24339](https://arxiv.org/abs/2605.24339)
- **PDF**: https://arxiv.org/pdf/2605.24339
- **详细分析**: [[20_Research/Papers/强化学习/IsaacIPC_Coupling_High-Fidelity_Simulation_and_Realistic_Rendering_for_Contact-Rich_Robotic_Systems|IsaacIPC: Coupling High-Fidelity Simulation and Realistic Rendering for Contact-Rich Robotic Systems]]
- **作者**: Qixin Liang, Zhongqing Han
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.9，机器人 1.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《IsaacIPC: Coupling High-Fidelity Simulation and Realistic Rendering for Contact-Rich Robotic Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ExternalSim, IPC-GraspSim, IsaacSim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present IsaacIPC, a robotic simulation framework that couples GPU accelerated incremental potential contact (IPC) with IsaacSim/Lab. IsaacIPC maps simulated deformation between simulation and visual meshes, enabling real-time realistic rendering with applications to data collection and policy evaluation. For tactile sensing, we introduce the geometric mortar contact potential (GMCP), which defines a barrier potential over contact samples on tactile surfaces to better resolve contact-pressure distributions. We evaluate GMCP on contact benchmarks and demonstrate IsaacIPC on rigid-deformable robotic simulations including a quadruped robot, a dexterous hand, and a universal manipulation interface (UMI) gripper.

</details>

---

### [[20_Research/Papers/具身智能/Afford-VLA_Action-Aligned_Visual_Planning_via_Internalized_Affordance|Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance]]

![[assets/2605.24203_figure.png|800]]

- **arXiv**: [2605.24203](https://arxiv.org/abs/2605.24203)
- **PDF**: https://arxiv.org/pdf/2605.24203
- **详细分析**: [[20_Research/Papers/具身智能/Afford-VLA_Action-Aligned_Visual_Planning_via_Internalized_Affordance|Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance]]
- **作者**: Runze Wang, Yuqian Fu, Yu Li, Tao Lin, Tianwen Qian, Mohamed Elhoseiny, Bo Zhao, Yanwei Fu, Yu-Gang Jiang, Xiangyang Xue
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 2.1，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Afford-VLA: Action-Aligned Visual Planning via Internalized Affordance》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Afford-VLA, CoA-VLA, OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language-action (VLA) models have shown strong potential for generalist robot manipulation, yet they remain limited by insufficient spatial reasoning, particularly in determining where to interact in complex visual scenes. While recent efforts introduce various forms of visual planning to address this issue, existing approaches either rely on global geometric cues, symbolic intermediate representations, or externally generated visual signals, which are often weakly coupled with downstream action prediction. In this work, we revisit visual planning in VLA systems and argue that effective planning should be local, visually grounded, internally generated, and directly aligned with action. Based on this insight, we propose Afford-VLA, a unified framework that internalizes task-conditioned affordance as an explicit visual planning interface within VLA models. Concretely, we introduce learnable &lt;AFF&gt; tokens to query task-relevant interaction regions, decode affordance masks from multimodal features, and convert them into compact embeddings that directly condition action generation. This design enables affordance to be both generated and utilized within the VLA, forming a tightly coupled perception-action pathway. To further support this integration, we adopt a training strategy that allows the affordance pathway to be jointly optimized with action prediction, improving its effectiveness for downstream control. We evaluate our method on multiple simulation benchmarks, including LIBERO, LIBERO-Plus, and SimplerEnv, achieving consistent state-of-the-art performance, along with strong real-world results. These findings demonstrate that internalizing affordance as action-aligned visual planning provides a powerful paradigm for improving VLA systems.

</details>

---

### [[20_Research/Papers/机器人/Anisotropic_Diffusion-Driven_Ergodic_Coverage_in_Multi-Robot_Systems|Anisotropic Diffusion-Driven Ergodic Coverage in Multi-Robot Systems]]

![[assets/2605.24125_figure.png|800]]

- **arXiv**: [2605.24125](https://arxiv.org/abs/2605.24125)
- **PDF**: https://arxiv.org/pdf/2605.24125
- **详细分析**: [[20_Research/Papers/机器人/Anisotropic_Diffusion-Driven_Ergodic_Coverage_in_Multi-Robot_Systems|Anisotropic Diffusion-Driven Ergodic Coverage in Multi-Robot Systems]]
- **作者**: Thales C. Silva, Anoop Kiran, Nora Ayanian
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Anisotropic Diffusion-Driven Ergodic Coverage in Multi-Robot Systems》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the problem of combining potential field and ergodic search on multi-robot systems. Traditional ergodic search algorithms use metrics for ergodicity that account for the desired distribution at different scales. Recently, a heat equation-driven ergodic approach was proposed, which adds flexibility to the smoothing of the ergodic metric. However, such an approach, as it is an isotropic diffusion, propagates the error uniformly in all directions, regardless of changes in the desired distribution. We introduce a general class of anisotropic diffusion formulation of the ergodicity problem, which generates a potential field for the ergodic search. We demonstrate that this approach generalizes previous results, which consider radial basis functions and the solution of the heat equation to represent the difference between the goal density distribution and the covered trajectories. In our solution, the agent movement is directed using the gradient of the solution of the Perona-Malik diffusion, and our formulation includes the heat equation as a special case. We demonstrate the methodology with a series of simulations in different scenarios.

</details>

---

### [[20_Research/Papers/具身智能/RED_Adaptive_Real-Time_DAG_Scheduling_for_Robotic_Inference_under_Environmental_Dynamics|RED: Adaptive Real-Time DAG Scheduling for Robotic Inference under Environmental Dynamics]]

![[assets/2605.24044_figure.png|800]]

- **arXiv**: [2605.24044](https://arxiv.org/abs/2605.24044)
- **PDF**: https://arxiv.org/pdf/2605.24044
- **详细分析**: [[20_Research/Papers/具身智能/RED_Adaptive_Real-Time_DAG_Scheduling_for_Robotic_Inference_under_Environmental_Dynamics|RED: Adaptive Real-Time DAG Scheduling for Robotic Inference under Environmental Dynamics]]
- **作者**: Zexin Li, Tao Ren, Johnathan Liu, Xiaoxi He, Cong Liu
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《RED: Adaptive Real-Time DAG Scheduling for Robotic Inference under Environmental Dynamics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ENet, MIMONet, MISONet, SIMONet, UNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots deployed in dynamic environments must contend with environment-driven changes that reshape computation at runtime: new tasks may appear, precedence relations can shift, and overall workload structure evolves, all of which degrade performance, especially when multi-task inference is required under tight resource and real-time budgets. We present RED, a real-time scheduling framework for multi-task deep neural network workloads on resource-constrained robotic platforms that adapts to Robotic Environmental Dynamics (RED) while preserving end-to-end timing guarantees under modeling assumptions. The core of RED is a deadline-aware scheduler that assigns intermediate sub-deadlines, allowing it to accommodate evolving computation graphs and asynchronous inference induced by unpredictable conditions. The framework also supports flexible deployment of MIMONet (multi-input multi-output neural networks), commonly used in multi-tasking robots to alleviate memory pressure through weight sharing. RED explicitly leverages this shared-parameter property via a workload refinement and graph-reconstruction procedure that aligns MIMONet structure with schedulability requirements, improving compatibility and efficiency. We implement RED on NVIDIA Jetson family platforms and on an Apple M-series MacBook and evaluate it on navigation-oriented workloads representative of real robotic scenarios. Experiments show consistent gains over existing methods in throughput, deadline satisfaction, robustness to interference, adaptability, and runtime overhead.

</details>

---
