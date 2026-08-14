# cs.RO | Robotics | 2026-08-12

#arxiv #ComputerScience

**论文数**: 18

### [[20_Research/Papers/具身智能/Risk-Aware_Kinodynamic_Motion_Planning_Under_Uncertainty_For_Safe_Navigation_on_Planetary_Environments|Risk-Aware Kinodynamic Motion Planning Under Uncertainty For Safe Navigation on Planetary Environments]]

![[assets/2608.11175_figure.png|800]]

- **arXiv**: [2608.11175](https://arxiv.org/abs/2608.11175)
- **PDF**: https://arxiv.org/pdf/2608.11175
- **详细分析**: [[20_Research/Papers/具身智能/Risk-Aware_Kinodynamic_Motion_Planning_Under_Uncertainty_For_Safe_Navigation_on_Planetary_Environments|Risk-Aware Kinodynamic Motion Planning Under Uncertainty For Safe Navigation on Planetary Environments]]
- **作者**: Sachin Sunil Kelkar, Tanmay Dokania, Yashwanth Kumar Nakka
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.1，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Risk-Aware Kinodynamic Motion Planning Under Uncertainty For Safe Navigation on Planetary Environments》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For autonomous space exploration, robotic agents need to perform motion planning in which environmental interactions may be unknown. Learning these interactions, such as terrain mechanics for wheeled robots, can introduce uncertainties that lead to risky motion plans and potentially hazardous operations or mission failures. Moreover, uncertainties induced by perception-based systems can exacerbate the problem of safe motion planning. In this letter, we address the problem of performing cost-optimal kinodynamic motion planning with risk awareness. We approach this in two steps. First, a sampling-based planner (AO-RRT) generates a dynamically feasible, risk-aware, and asymptotically cost-optimal trajectory. Second, we formulate motion planning as a nonlinear optimization problem and solve it using sequential convex programming (SCP), using the AO-RRT trajectory as an initial solution. By quantifying risk using conditional value-at-risk (CVaR), we demonstrate a reduction in risk by over $\sim$97\% across trajectories in simulation and hardware experiments.

</details>

---

### [[20_Research/Papers/世界模型/VIScore_Diagnosing_Planning-Relevant_Quality_in_Latent_World_Models|VIScore: Diagnosing Planning-Relevant Quality in Latent World Models]]

![[assets/2608.11174_figure.png|800]]

- **arXiv**: [2608.11174](https://arxiv.org/abs/2608.11174)
- **PDF**: https://arxiv.org/pdf/2608.11174
- **详细分析**: [[20_Research/Papers/世界模型/VIScore_Diagnosing_Planning-Relevant_Quality_in_Latent_World_Models|VIScore: Diagnosing Planning-Relevant Quality in Latent World Models]]
- **作者**: Haiyu Wu, Randall Balestriero, Morgan Levine
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型
- **相关性评分**: 0.8（加权：世界模型 0.8）
- **关联关键词**: Agent, WorldModel

#### 研究背景与动机

《VIScore: Diagnosing Planning-Relevant Quality in Latent World Models》归入 世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：ImageNet, OGBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Regulating the latent space to an isotropic Gaussian distribution provides a stable and information-maximized landscape for world model planning. However, the latent space property and successful planning remain disconnected. We first study this by comparing SIGReg and VISReg, two regularization loss functions with the same distribution target but different properties. Compared with SIGReg, VISReg has more flexibility in controlling the weights of center, scale, and shape regularization, and a larger batch size brings a finer distribution approximation. We find that the former, despite being beneficial in self-supervised learning (SSL), does not help the planning, whereas the latter improves the planning success on out-of-domain (OOD) datasets. This motivates a deep understanding of the factors that correlate with the success rate. Unlike the previous metrics focusing on the encoded latent only, we propose the Veracity-Influence-Sobriety score (VIScore), a metric that quantifies the reachability and capacity of a predictor given the encoded feature, and the hallucination of the searching-based planner. Compared with straightness, physical-state probing, and empowerment, we show that, with the measurement covering encoder, predictor, and planner, VIScore explains the success rate better than the others, as reflected by a strong Spearman correlation. Specifically, VIScore consistently achieves a Spearman correlation over 0.75 on both seen and unseen models and datasets on the cross-task success rate pool. Moreover, VIScore is the only metric that has a calibration error below the constant fit across all testing scenarios, showcasing the importance of these three aspects in planning success. We hope this metric can help future studies on world model design and diagnosis.

</details>

---

### [[20_Research/Papers/机器人/Deployment_Is_Not_Destiny_Robot_Recomposition_in_the_Field_with_Unseen_Software,_Hardware,_and_Compute_Payloads|Deployment Is Not Destiny: Robot Recomposition in the Field with Unseen Software, Hardware, and Compute Payloads]]

![[assets/2608.11063_figure.png|800]]

- **arXiv**: [2608.11063](https://arxiv.org/abs/2608.11063)
- **PDF**: https://arxiv.org/pdf/2608.11063
- **详细分析**: [[20_Research/Papers/机器人/Deployment_Is_Not_Destiny_Robot_Recomposition_in_the_Field_with_Unseen_Software,_Hardware,_and_Compute_Payloads|Deployment Is Not Destiny: Robot Recomposition in the Field with Unseen Software, Hardware, and Compute Payloads]]
- **作者**: Steven Swanbeck, Jonathan Salfity, Jeffery Gunawan, Corrie Van Sice, Mitch Pryor, Robert Blake Anderson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Deployment Is Not Destiny: Robot Recomposition in the Field with Unseen Software, Hardware, and Compute Payloads》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The tight coupling of subsystems in most robots, though a natural consequence of their complexity, leads to monolithic designs that are time-consuming and difficult to adapt after initial deployment. To address this challenge, we present a framework and supporting abstractions for recomposition during runtime that enable robots to quickly integrate previously unseen modular software, hardware, and compute payloads. Our approach allows non-expert users to quickly add new capabilities in the field through a true plug-and-play process. Crucially, new resources are not only immediately available to a host robot but are also shared with distributed peers, enabling compute-constrained systems to access powerful new remote capabilities. Our framework reduces reconfiguration time to a matter of minutes with no developer intervention, in stark contrast to the hours of expert effort often required for traditional manual integration. We demonstrate our method in two disaster response scenarios, including radioactive source localization at an operational nuclear reactor facility and a thermal-guided search for people in dark, difficult-to-reach spaces. These demonstrations show how in-field recomposition provides timely, flexible, and accessible adaptation to dynamic requirements, representing a critical step toward creating robots that can quickly evolve alongside the tasks, technologies, and environments they support.

</details>

---

### [[20_Research/Papers/机器人/Aerial_Layouting_Design_and_Control_of_a_Compliant_and_Actuated_End-Effector_for_Precise_In-flight_Marking_on_Ceilings|Aerial Layouting: Design and Control of a Compliant and Actuated End-Effector for Precise In-flight Marking on Ceilings]]

![[assets/2608.10987_figure.png|800]]

- **arXiv**: [2608.10987](https://arxiv.org/abs/2608.10987)
- **PDF**: https://arxiv.org/pdf/2608.10987
- **详细分析**: [[20_Research/Papers/机器人/Aerial_Layouting_Design_and_Control_of_a_Compliant_and_Actuated_End-Effector_for_Precise_In-flight_Marking_on_Ceilings|Aerial Layouting: Design and Control of a Compliant and Actuated End-Effector for Precise In-flight Marking on Ceilings]]
- **作者**: Christian Lanegger, Marco Ruggia, Marco Tognon, Lionel Ott, Roland Siegwart
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Aerial Layouting: Design and Control of a Compliant and Actuated End-Effector for Precise In-flight Marking on Ceilings》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Aerial robots have demonstrated impressive feats of precise control, such as dynamic flight through openings or highly complex choreographies. Despite the accuracy needed for these tasks, there are problems that require levels of precision that are challenging to achieve today. One such problem is aerial interaction. Advances in aerial robot design and control have made such contact-based tasks possible and opened up research into challenging real-world tasks, including contact-based inspection. However, while centimetre accuracy is sufficient and achievable for inspection tasks, the positioning accuracy needed for other problems, such as layouting on construction sites or general push-and-slide tasks, is millimetres. To achieve such a high precision, we propose a new aerial system composed of an aerial vehicle equipped with a novel "smart" end-effector leveraging a stability-optimized Gough-Stewart mechanism. We present its design process and features incorporating the principles of compliance, multiple contact points, actuation, and self-containment. In experiments, we verify that the design choices made for our novel end-effector are necessary to obtain the desired positioning precision. Furthermore, we demonstrate that we can reliably mark lines on ceilings with millimetre accuracy without the need for precise modeling or sophisticated control of the aerial robot.

</details>

---

### [[20_Research/Papers/强化学习/Robust_Safety_Filtering_for_Input-Constrained_Underactuated_Linear_Systems|Robust Safety Filtering for Input-Constrained Underactuated Linear Systems]]

![[assets/2608.10872_figure.png|800]]

- **arXiv**: [2608.10872](https://arxiv.org/abs/2608.10872)
- **PDF**: https://arxiv.org/pdf/2608.10872
- **详细分析**: [[20_Research/Papers/强化学习/Robust_Safety_Filtering_for_Input-Constrained_Underactuated_Linear_Systems|Robust Safety Filtering for Input-Constrained Underactuated Linear Systems]]
- **作者**: Muhamad Rausyan Fikri
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Robust Safety Filtering for Input-Constrained Underactuated Linear Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a robust safety-filtering framework for input-constrained underactuated linear systems subject to unknown disturbances. A baseline H-$\infty$ input is derived from a zero-sum differential game, while a disturbance observer supplies an estimate and a transient error bound. The baseline input is adjusted using the disturbance estimate, while the estimate and its error bound are used to define robust high-order control barrier function constraints; forward invariance holds as long as the admissible-input set remains nonempty. For scalar-input systems, pointwise feasibility is determined from an exact input interval, and the interval width defines the feasibility margin. A finite-horizon H-$\infty$ performance balance accounts for the accumulated deviation of the applied input from the baseline H-$\infty$ policy. Simulations on a linearized two-wheeled balancing robot show how position and body-pitch constraints compete for the same bounded wheel-torque input.

</details>

---

### [[20_Research/Papers/机器人/Enabling_Scalable_Kinesthetic_Teaching_via_Observer-based_Hand-guiding_with_Active_Support|Enabling Scalable Kinesthetic Teaching via Observer-based Hand-guiding with Active Support]]

![[assets/2608.10847_figure.png|800]]

- **arXiv**: [2608.10847](https://arxiv.org/abs/2608.10847)
- **PDF**: https://arxiv.org/pdf/2608.10847
- **详细分析**: [[20_Research/Papers/机器人/Enabling_Scalable_Kinesthetic_Teaching_via_Observer-based_Hand-guiding_with_Active_Support|Enabling Scalable Kinesthetic Teaching via Observer-based Hand-guiding with Active Support]]
- **作者**: Anna Tuma, Giuseppe Monetti, Jochen J. Steil, Niels Dehio
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Enabling Scalable Kinesthetic Teaching via Observer-based Hand-guiding with Active Support》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Kinesthetic teaching through robot hand-guiding provides a natural interface for collecting demonstrations in imitation learning and programming-by-demonstration. However, extended sessions cause operator fatigue, reducing demonstration quality and limiting scalability. Current industrial hand-guiding approaches typically provide no active assistance, and alternatives require costly wrist-mounted force-torque sensors or rely on learned motion priors unavailable for new tasks. We propose RHOAS, a hand-guiding scheme that actively supports operator-intended motions using model-based force estimation without additional hardware. Our approach considers robot hand-guiding as an actively controlled interaction by the human operator, rather than an interaction with a passive environment. Standard methods used for hand-guiding typically rely on general passivity-based compliant control architectures that unnecessarily increase operator effort and limit the range of demonstrable motions without providing the intended stability guarantees in active interaction. Instead, our design utilizes model-based external torque estimation, internal joint torque sensing, and redundant robot kinematics to actively support human physical input within the human interaction frequency bandwidth. We address practical challenges of relying on observer-based force estimation, including suppression of unmodeled joint elastic dynamic effects and measurement noise in the feedback path, reduced estimate accuracy close to kinematic singularities, and static gravity compensation errors. In a user study with 16 participants on a KUKA LWR iiwa we demonstrate statistically significant reductions in physical effort, improved maneuverability for both precise and agile tasks, and clear user preference.

</details>

---

### [[20_Research/Papers/具身智能/AECNav_Active_Evidence_Consolidation_for_Efficient_Zero-Shot_Open-Vocabulary_Object_Navigation|AECNav: Active Evidence Consolidation for Efficient Zero-Shot Open-Vocabulary Object Navigation]]

![[assets/2608.10817_figure.png|800]]

- **arXiv**: [2608.10817](https://arxiv.org/abs/2608.10817)
- **PDF**: https://arxiv.org/pdf/2608.10817
- **详细分析**: [[20_Research/Papers/具身智能/AECNav_Active_Evidence_Consolidation_for_Efficient_Zero-Shot_Open-Vocabulary_Object_Navigation|AECNav: Active Evidence Consolidation for Efficient Zero-Shot Open-Vocabulary Object Navigation]]
- **作者**: Guanlin Liu, Shaobin Ling, Renyuan Liu, Zeying Gong, Junjie Hu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.2（加权：具身智能 1.5，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《AECNav: Active Evidence Consolidation for Efficient Zero-Shot Open-Vocabulary Object Navigation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Zero-shot object-goal navigation (ZSON) in open-vocabulary scenarios is challenging, as it requires a robot to locate an arbitrarily specified object in an unseen environment without task-specific training. Currently, the task still suffers from high latency and limited accuracy due to redundant perception pipelines and insufficient evidence for reliable target confirmation. In this letter, we reframe ZSON as an evidence-driven perception-to-decision problem and present AECNav, a training-free pipeline built on three components: i) Evidence-gated perception, which utilizes a shared encoding across all reasoning stages to establish a unified semantic basis and eliminate redundant computations; ii) Evidence consolidation, which aggregates detections into cluster-level log-odds beliefs. This explicitly separates genuine target support from the false confidence of visually similar distractors, while treating the absence of expected detections as negative evidence; and iii) Active evidence acquisition, which sustains productive exploration under weak semantic cues by selecting frontiers that maximize information gain at minimal traversal cost. As a result, AECNav significantly outperforms previous methods and achieves state-of-the-art success rates of 84.7%, 57.3%, and 51.3% on HM3D-v2, HM3D-OVON, and MP3D, respectively, with substantially lower inference overhead, and attains 95% success across 40 trials on a physical quadruped robot at roughly 5Hz. Code will be made publicly available upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/JEPA-WAM_Stage-Level_Joint-Embedding_Prediction_for_World-Action_Models_in_Robot_Manipulation|JEPA-WAM: Stage-Level Joint-Embedding Prediction for World-Action Models in Robot Manipulation]]

![[assets/2608.10780_figure.png|800]]

- **arXiv**: [2608.10780](https://arxiv.org/abs/2608.10780)
- **PDF**: https://arxiv.org/pdf/2608.10780
- **详细分析**: [[20_Research/Papers/具身智能/JEPA-WAM_Stage-Level_Joint-Embedding_Prediction_for_World-Action_Models_in_Robot_Manipulation|JEPA-WAM: Stage-Level Joint-Embedding Prediction for World-Action Models in Robot Manipulation]]
- **作者**: Xiao Liu, Yuguang Yang, Xi Wang, Kai Jiang, Cheng Chi, Yong Xu, Wenchao Ding, Yilun Chen, Yan Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《JEPA-WAM: Stage-Level Joint-Embedding Prediction for World-Action Models in Robot Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenVLA, ReconVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generalist robot policies aim to map multimodal observations and linguistic task instructions to actions across diverse tasks. However, existing methods typically represent the future as a fixed, short video-action chunk. This short-term future captures local scene evolution for action execution, but it does not explicitly describe the stage-level future that specifies how a task should progress from its current stage to the next. We therefore distinguish two complementary futures for robot manipulation: a short-term physical future to capture local scene evolution and a stage-level semantic future to represent task progress. We introduce JEPA-WAM, which augments a Motus-based World Action Model (WAM) with Stage-JEPA, a goal-conditioned Joint-Embedding Predictive Architecture (JEPA) predictor. Given the current observation and task instruction, Stage-JEPA uses a frozen V-JEPA2 encoder to extract the current-state representation and predicts the latent target of the next inferred stage. Across 50 RoboTwin 2.0 tasks in clean and randomized environments, JEPA-WAM achieves 90.25% overall success and reduces the mean number of execution steps in successful rollouts by 5.97% relative to the strongest baseline.

</details>

---

### [[20_Research/Papers/具身智能/TCAM_for_Autonomous_Deformable_Manipulation_The_RMC2_Champion_System_for_WBCD_2026_Track_4|TCAM for Autonomous Deformable Manipulation: The RMC2 Champion System for WBCD 2026 Track 4]]

![[assets/2608.10718_figure.png|800]]

- **arXiv**: [2608.10718](https://arxiv.org/abs/2608.10718)
- **PDF**: https://arxiv.org/pdf/2608.10718
- **详细分析**: [[20_Research/Papers/具身智能/TCAM_for_Autonomous_Deformable_Manipulation_The_RMC2_Champion_System_for_WBCD_2026_Track_4|TCAM for Autonomous Deformable Manipulation: The RMC2 Champion System for WBCD 2026 Track 4]]
- **作者**: Guangrui Shen, Zhili He, Shigang Wang, Yuanjun Sun, Qing Yu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《TCAM for Autonomous Deformable Manipulation: The RMC2 Champion System for WBCD 2026 Track 4》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This technical report describes the RMC2 Team's champion solution for the WBCD 2026 Track 4: Deformable Manipulation Challenge. The task requires a robot to pick a single T-shirt from a stack, load it onto a printing pallet, align the collar with a target area, and smooth the printing region, a sequence that involves single-layer separation, deformable transport, precise placement, and contact-rich surface adjustment. The competition strongly incentivizes fully autonomous execution, motivating the development of an autonomous solution. We built a fully autonomous system around the TCAM (TermiBrain Causal Action Model) framework, with the design principle that hardware, perception, data, and learning should jointly reduce the physical interaction complexity the policy must handle. A custom 3D-printed gripper designed for single-layer fabric separation improves picking reliability on a dual-arm ARX X5 platform. A wrist-centric four-camera setup pairs upper fisheye cameras for task-level context with lower RGB cameras for close-range gripper-cloth contact observation. We combine portable UMI-style demonstrations with real-robot demonstrations collected on the deployable platform to provide both broad manipulation priors and deployment-specific dynamics. TCAM ties these components into a closed loop: each trajectory is analyzed to identify the physical factors contributing to its outcome, driving targeted data recollection and policy fine-tuning. The policy outputs 30-step end-effector delta-pose action chunks from a multi-view VLA backbone. In the final competition, our system loaded 25 T-shirts at an average of approximately 23 seconds per attempt, with 22 achieving the required surface smoothness, securing first place in Track 4.

</details>

---

### [[20_Research/Papers/机器人/OAA_Three_Phases_of_Vocal_Guidance_in_Human-Drone_Teleoperation|OAA: Three Phases of Vocal Guidance in Human-Drone Teleoperation]]

![[assets/2608.10651_first_page.png|800]]

- **arXiv**: [2608.10651](https://arxiv.org/abs/2608.10651)
- **PDF**: https://arxiv.org/pdf/2608.10651
- **详细分析**: [[20_Research/Papers/机器人/OAA_Three_Phases_of_Vocal_Guidance_in_Human-Drone_Teleoperation|OAA: Three Phases of Vocal Guidance in Human-Drone Teleoperation]]
- **作者**: Allan Henry, Christian Graff, Solange Rossato, José-Ernesto Gomez-Balderas, Sylvain Huet
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《OAA: Three Phases of Vocal Guidance in Human-Drone Teleoperation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Voice-guided teleoperation requires systems that adapt to the evolving dynamics of human guidance. Yet most voice-controlled robot systems treat spoken commands as a stationary stream, ignoring how the guide's communicative behavior changes as the task progresses. Using motion capture and speech data from two experimental configurations, humanhuman guidance (finger pointing, N =10 dyads) and humandrone teleoperation (gamepad control, N =29 dyads), we show that spontaneous vocal guidance consistently organizes into three kinematically and linguistically distinct phases: Orientation, Approach, and Adjustment. These phases are identified automatically via change point detection on 3D trajectory signals, and validated statistically (Kruskal-Wallis, p&lt;.001). Three lexical families replicate across configurations: rotation vocabulary marks Orientation, translation vocabulary is scarce there, and attenuators accumulate toward Adjustment. Together with inter-utterance silence, these cues mark the Orientation boundary that speech rate alone leaves unmarked. The same three-phase structure emerges in both configurations despite radically different motor interfaces, suggesting it is an intrinsic property of human spatial guidance rather than an artifact of the experimental setup. We discuss implications for OAA-aware adaptive control in voice-guided teleoperation.

</details>

---

### [[20_Research/Papers/机器人/When_Your_State_Estimator_Has_Lost_The_Plot_Detecting_Estimator_Failures_Via_Spectral_Analysis|When Your State Estimator Has Lost The Plot: Detecting Estimator Failures Via Spectral Analysis]]

![[assets/2608.10623_figure.png|800]]

- **arXiv**: [2608.10623](https://arxiv.org/abs/2608.10623)
- **PDF**: https://arxiv.org/pdf/2608.10623
- **详细分析**: [[20_Research/Papers/机器人/When_Your_State_Estimator_Has_Lost_The_Plot_Detecting_Estimator_Failures_Via_Spectral_Analysis|When Your State Estimator Has Lost The Plot: Detecting Estimator Failures Via Spectral Analysis]]
- **作者**: Christian Lanegger, Helen Oleynikova, Roland Siegwart, Michael Pantic
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《When Your State Estimator Has Lost The Plot: Detecting Estimator Failures Via Spectral Analysis》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable onboard state estimation is essential for safe robotic operation, yet unmodeled disturbances, such as sensor aliasing or out-of-distribution noise, still cause estimators to degrade or fail completely. While many methods aim to improve estimator robustness, only a few provide introspective mechanisms to assess estimate quality. Existing uncertainty measures, such as covariances, rely on idealized assumptions and tend to be overconfident, and more recent data-driven approaches are typically tied to their training data distributions. We propose a sensor-agnostic introspective method that assesses estimator health by analyzing the frequency-domain power distribution of recent velocity estimates. The method is evaluated using outdoor flight data from an aerial robot running visual-inertial, LiDAR-inertial, and radar-inertial odometry. The dataset includes multiple estimator failures, enabling analysis of several frequency-domain indicators, such as signal power, spectral bandwidth, and entropy. We observe consistent spectral power differences between healthy and degraded estimates, allowing detection of 51%-58% of labeled failures with 60%-84% precision across three fundamentally different state estimation frameworks. Our results show that even a simple frequency-domain analysis of a state estimator's output can serve as a lightweight introspective tool to complement existing robustness techniques in real-world robotic deployments, and opens promising avenues for future investigation.

</details>

---

### [[20_Research/Papers/具身智能/Toward_the_Cognitive--Physical_Limits_of_Embodied_Intelligence_through_a_World-Model-Centric_Autonomous_Racing_Agent|Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent]]

![[assets/2608.10618_figure.png|800]]

- **arXiv**: [2608.10618](https://arxiv.org/abs/2608.10618)
- **PDF**: https://arxiv.org/pdf/2608.10618
- **详细分析**: [[20_Research/Papers/具身智能/Toward_the_Cognitive--Physical_Limits_of_Embodied_Intelligence_through_a_World-Model-Centric_Autonomous_Racing_Agent|Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent]]
- **作者**: Zitong Shan, Baichuan Lou, Yanxin Zhou, Shuge Wu, Xianqi He, Bolin Zhao, Sheng Zhao, Zhouheng Li, Chee Kiong Ong, King Ho Holden Li, Chen Lv
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 世界模型, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.5，大模型 0.5，世界模型 0.4，机器人 0.3）
- **关联关键词**: Agent, EmbodiedAI, RL

#### 研究背景与动机

《Toward the Cognitive--Physical Limits of Embodied Intelligence through a World-Model-Centric Autonomous Racing Agent》归入 具身智能、大模型、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied artificial intelligence aims to develop agents that perceive, reason, and act through continuous interaction with the physical world. However, most embodied systems are still evaluated within conservative safety margins or moderate interaction regimes, leaving their capability boundaries under extreme conditions insufficiently understood. Autonomous racing provides a stringent testbed by combining high-frequency localization and perception, adversarial interaction, near-saturated vehicle dynamics, and strict safety constraints. Existing systems push high-speed performance but rarely model and refine cognitive and physical limits jointly. Here we show that a world-model-centric autonomous racing agent provides a concrete step toward exploring these coupled limits. The framework learns predictive world models from near-limit successes and failures to capture interaction evolution, ego dynamics, and feasible-motion boundaries, coupling world-state construction, future-aware reasoning, and near-limit control in a closed-loop refinement process. Training data were collected from real-vehicle autonomous racing, where the onboard system maintained robust localization and perception at speeds up to 256.3 km/h and peak lateral acceleration of 26.8 m/s$^2$. In full-scale simulated racing, the well trained world-model-centric agent achieves an 88.3% interaction success rate across various challenging simulated racing scenarios. Closed-loop refinement of the world model and policy further improved utilization of cognitive-physical limits, recovery from failure modes, and generalization across varying conditions and unseen circuits. These results suggest a boundary-aware methodology in which world models help embodied agents represent, predict, and continually refine their capability boundaries for safer real-world deployment.

</details>

---

### [[20_Research/Papers/机器人/Nonlinear_Model_Predictive_Control_via_Sequential_Convex_Programming_for_Drone-to-Drone_Docking|Nonlinear Model Predictive Control via Sequential Convex Programming for Drone-to-Drone Docking]]

![[assets/2608.10542_figure.png|800]]

- **arXiv**: [2608.10542](https://arxiv.org/abs/2608.10542)
- **PDF**: https://arxiv.org/pdf/2608.10542
- **详细分析**: [[20_Research/Papers/机器人/Nonlinear_Model_Predictive_Control_via_Sequential_Convex_Programming_for_Drone-to-Drone_Docking|Nonlinear Model Predictive Control via Sequential Convex Programming for Drone-to-Drone Docking]]
- **作者**: Neeraj Balachandar, Shriram Hari, Vishnu R. Unni
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: cs.RO

#### 研究背景与动机

《Nonlinear Model Predictive Control via Sequential Convex Programming for Drone-to-Drone Docking》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous mid-air docking of multi-rotor vehicles under disturbance-driven target motion poses a constrained non-linear trajectory optimization challenge. This work formulates the docking task as a finite-horizon optimal control problem based on a reduced-order nonlinear model augmented with disturbance states. The resulting problem is solved using sequential convex programming within a receding-horizon framework to generate dynamically feasible docking trajectories. State estimation with noisy measurements is incorporated to enable robust relative motion prediction, while trajectory execution is validated in a high-fidelity rigid-body MuJoCo simulation environment. The proposed framework is evaluated for stationary and constant-velocity target motions, demonstrating reliable convergence to the docking interface while satisfying geometric capture constraints. Quantitatively, the method maintains negligible docking-cone violations and terminal state errors within prescribed tolerances, and achieves consistent, safe docking performance for cone half-angles as low as 10 degrees. Robust operation is observed for wind disturbance levels up to a standard deviation of 0.5, while preserving bounded approach velocities and stable control effort. These results demonstrate the effectiveness of the SCP-based trajectory optimization framework for disturbance-robust aerial docking under estimation uncertainty.

</details>

---

### [[20_Research/Papers/机器人/JitTrack_Onboard_Multi-Object_Tracking_Against_Viewpoint_Jitter_for_Agile_UAVs|JitTrack: Onboard Multi-Object Tracking Against Viewpoint Jitter for Agile UAVs]]

![[assets/2608.10485_figure.png|800]]

- **arXiv**: [2608.10485](https://arxiv.org/abs/2608.10485)
- **PDF**: https://arxiv.org/pdf/2608.10485
- **详细分析**: [[20_Research/Papers/机器人/JitTrack_Onboard_Multi-Object_Tracking_Against_Viewpoint_Jitter_for_Agile_UAVs|JitTrack: Onboard Multi-Object Tracking Against Viewpoint Jitter for Agile UAVs]]
- **作者**: Yachun Shan, Feitian Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《JitTrack: Onboard Multi-Object Tracking Against Viewpoint Jitter for Agile UAVs》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-object tracking (MOT) onboard agile unmanned aerial vehicles (UAVs) remains challenging due to severe viewpoint jitter induced by camera ego-motion. Rapid attitude changes during flight often lead to significant target displacement across frames, causing inaccurate target association and degraded tracking performance. Existing UAV MOT methods are primarily evaluated on offline benchmarks and seldom address the practical requirements of real-world onboard deployment, including robustness to camera motion and active target following. To address these challenges, we propose JitTrack, an active onboard multi-object tracking framework that accommodates drone dynamics and camera ego-motion. Built upon a query-based transformer tracker, JitTrack introduces semantic refinement to improve the detection of emerging targets, motion-aware query rectification to compensate for target misalignment caused by viewpoint jitter, and a motion-inspired denoising training strategy that simulates camera motion patterns for robust supervision. Furthermore, we develop a perception-planning-control closed-loop tracking pipeline for real-world deployment, enabling collision-free and physically feasible target following on agile UAVs. Extensive experiments on public UAV MOT benchmarks demonstrate consistent improvements over the baseline method, while real-world flight experiments validate the effectiveness and practicality of JitTrack for robust onboard visual tracking under viewpoint jitter.

</details>

---

### [[20_Research/Papers/强化学习/PBD-AG_Persistent_Baseline-Delta_Active_Graphs_with_Uncertainty-Aware_Inspection_for_Long-Horizon_Service_Robots|PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots]]

![[assets/2608.10449_figure.png|800]]

- **arXiv**: [2608.10449](https://arxiv.org/abs/2608.10449)
- **PDF**: https://arxiv.org/pdf/2608.10449
- **详细分析**: [[20_Research/Papers/强化学习/PBD-AG_Persistent_Baseline-Delta_Active_Graphs_with_Uncertainty-Aware_Inspection_for_Long-Horizon_Service_Robots|PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots]]
- **作者**: Shuo Bao, Wei Dong, Shuyue Zhang, Ming Shang, Yuchen Huang, Han Yu, Chengjie Xu, Yiheng Bi, Kai Sun, Fuchun Sun, Xinzhou Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，世界模型 0.4，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《PBD-AG: Persistent Baseline-Delta Active Graphs with Uncertainty-Aware Inspection for Long-Horizon Service Robots》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon service robots require persistent world models that can be built autonomously in unseen environments and revised as task-relevant objects change. Existing methods rely on online mapping, which accumulates localization and observation errors, static scene representations that cannot capture persistent object changes, or holistic vision-language predictions that lack verifiable 3D geometric evidence. We present PBD-AG, a persistent baseline-delta active graph framework that decouples robot-verified stable fixtures from revisable dynamic object events. Under our framework, the robot autonomously bootstraps the structural baseline from onboard exploration and inspects discovered fixtures to ground hierarchical object beliefs. PBD-AG maintains reliability-weighted object states over geometry, semantics, identity, existence, and support relations, utilizing a geometric visibility gate to mitigate false deletions under occlusion. Inspection viewpoints are selected by a graph-conditioned policy that balances target coverage, travel cost, collision risk, and redundant observation. Simulation experiments in multiple environments and under controlled dynamic evaluation show higher aggregate coarse-fixture F1 than capability-matched controls, as well as stronger identity continuity and event recall. A qualitative physical-robot demonstration further illustrates integration with onboard sensing, providing a traceable world model for long-horizon robotic perception.The project page of PBD-AG is available at https://shuobao214.github.io/PBD-AG/

</details>

---

### [[20_Research/Papers/具身智能/Hip_Energized_Monopedal_Hopping|Hip Energized Monopedal Hopping]]

![[assets/2608.10387_figure.png|800]]

- **arXiv**: [2608.10387](https://arxiv.org/abs/2608.10387)
- **PDF**: https://arxiv.org/pdf/2608.10387
- **详细分析**: [[20_Research/Papers/具身智能/Hip_Energized_Monopedal_Hopping|Hip Energized Monopedal Hopping]]
- **作者**: Shane Rozen-Levy, Griffon McMahon, Daniel Koditschek
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Hip Energized Monopedal Hopping》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present a novel stepping strategy for pitch unlocked planar monopeds where the reaction torques from stabilizing pitch with a conventional PD + feedfoward controller are recruited to counteract energetic losses from damping. By moving the location of the mass center, our controller increases the pitch stabilization torque, thereby adding energy to the gait. A new stepping policy adjusts the distribution of energy between the radial and angular degrees of freedom to counteract dissipative losses and achieve a user specified balance between steady state fore-aft speed and apex height. Hybrid averaging analysis yields closed form expressions for the fixed points and eigenvalues of the resulting gait, lending insight into the interplay between the physical and control parameters' influence on performance. Simulation studies on a generic 5 link biped and a careful model of the Penn Jerboa reveal a useful correspondence to these analytical predictions. Physical experiments on the Penn Jerboa exhibit stable locomotion with speeds ranging from 1.02 m/s to 1.77 m/s (5.10 leg lengths/s to 8.85 leg lengths/s) in a manner effectively approximated by the mathematical analysis.

</details>

---

### [[20_Research/Papers/具身智能/Real-World_Cooperative_Bimanual_Dexterous_Grasp_of_Large_Objects_from_Single-View_Observations|Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations]]

![[assets/2608.10383_figure.png|800]]

- **arXiv**: [2608.10383](https://arxiv.org/abs/2608.10383)
- **PDF**: https://arxiv.org/pdf/2608.10383
- **详细分析**: [[20_Research/Papers/具身智能/Real-World_Cooperative_Bimanual_Dexterous_Grasp_of_Large_Objects_from_Single-View_Observations|Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations]]
- **作者**: Ziming Li, Mingxuan Wu, Jiaqi Zhang, Hongfei Li, Yan Gan, Deqiang Ouyang, Ning Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.1（加权：具身智能 2.1，大模型 0.1，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Real-World Cooperative Bimanual Dexterous Grasp of Large Objects from Single-View Observations》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：IsaacGym, PointNet, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual dexterous grasping of large objects is a critical challenge in robotic manipulation. However, most existing studies focus on sequential manipulation rather than cooperative grasping, and methods addressing such bimanual tasks have largely been limited to simulation. These limitations stem from the difficulty of acquiring full 3D object models and generating physically plausible grasping actions. To fill this gap, we propose a real-world bimanual grasping framework that includes: a multimodal dataset capturing joint angles, visual observations and force signals; a Denoising Diffusion Probabilistic Model (DDPM)-based module that generates joint-level grasp configurations from segmented point clouds; and an execution strategy that integrates motion planning with online grasp refinement to ensure physical stability and feasibility. Our approach enables the synthesis of executable bimanual grasps from single-view inputs, reducing dependence on complete 3D object models and ensuring stable real-world performance. Experiments on a dual-arm robot demonstrate high success rates across unseen objects with varying geometries and poses, and ablation studies confirm the contributions of key components of our system.

</details>

---

### [[20_Research/Papers/具身智能/Whole-Body_Planning_for_Humanoids_Navigating_Confined_Spaces_via_Self-Collision_Avoidance_References|Whole-Body Planning for Humanoids Navigating Confined Spaces via Self-Collision Avoidance References]]

![[assets/2608.10220_figure.jpg|800]]

- **arXiv**: [2608.10220](https://arxiv.org/abs/2608.10220)
- **PDF**: https://arxiv.org/pdf/2608.10220
- **详细分析**: [[20_Research/Papers/具身智能/Whole-Body_Planning_for_Humanoids_Navigating_Confined_Spaces_via_Self-Collision_Avoidance_References|Whole-Body Planning for Humanoids Navigating Confined Spaces via Self-Collision Avoidance References]]
- **作者**: Carlos Gonzalez, Luis Sentis
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.8（加权：具身智能 0.9，强化学习 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Whole-Body Planning for Humanoids Navigating Confined Spaces via Self-Collision Avoidance References》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid locomotion in highly confined environments requires navigating dense environmental obstacles and complex self-collision bounds while maintaining multi-contact dynamic feasibility. Traditional trajectory optimizers frequently struggle in these restricted spaces, as navigating the large collision space with splines on particle abstractions is insufficient and leads to poor local minima. To address this, we propose a three-stage whole-body planning framework that formulates kinematic path planning directly over kinematically reachable rigid-body volumes. By integrating differentiable collision avoidance into a reachability-constrained formulation, our framework synthesizes volume-informed guides that reliably guide a full-order trajectory optimizer over long horizons. We show that these optimized plans serve as high-quality references to train a residual reinforcement learning policy for robust online execution. We validate our approach on the Unitree G1 humanoid across three benchmark testbeds exceeding NIST emergency response standards, achieving restricted confinement ratios ($C_r &lt; 1.5$). Our framework generates feasible trajectories across 12-to-18-second tasks with complex foot and hand contacts where standard baselines fail, while the learned policy successfully tracks these plans under extensive domain randomization in physics simulation.

</details>

---
