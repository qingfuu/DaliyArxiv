# cs.RO | Robotics | 2026-11-16

#arxiv #ComputerScience

**论文数**: 21

### [[20_Research/Papers/机器人/Modeling_the_Frictional_Contact_of_Continuum_Robots_with_Environments_through_Linear_Complementarity_Problem|Modeling the Frictional Contact of Continuum Robots with Environments through Linear Complementarity Problem]]

![[assets/2611.18546_figure.png|800]]

- **arXiv**: [2611.18546](https://arxiv.org/abs/2611.18546)
- **PDF**: https://arxiv.org/pdf/2611.18546
- **详细分析**: [[20_Research/Papers/机器人/Modeling_the_Frictional_Contact_of_Continuum_Robots_with_Environments_through_Linear_Complementarity_Problem|Modeling the Frictional Contact of Continuum Robots with Environments through Linear Complementarity Problem]]
- **作者**: Jia Shen, Junhyoung Ha, Yue Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Modeling the Frictional Contact of Continuum Robots with Environments through Linear Complementarity Problem》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate friction modeling in continuum robots is essential for precise motion control and path planning. However, current approaches make predictions only for the mechanism's internal friction that is limited by the boundary forces of the Coulomb friction cone, which fail to characterize the static friction and motion hysteresis. In this paper, we propose a novel friction model based on complementarity constraints under the Coulomb friction assumption. This model predicts various friction effects caused by environmental interactions, including both static and sliding frictions and hysteresis behavior, as well as the corresponding robot deformation induced by these interactions, which are crucial for the practical motion planning and control of continuum robots. Additionally, real-time implementation of this model can be achieved, meeting the demand for computational efficiency in robotic applications. Experimental validations demonstrated that this model is able to reduce the maximum tip position error from 45.4 mm in the frictionless model to 5.85 mm in our friction-included model with a 287.9 mm-long tendon-driven continuum robot.

</details>

---

### [[20_Research/Papers/机器人/Disturbance-Aware_Informative_Planning_in_Spatiotemporal_Environments|Disturbance-Aware Informative Planning in Spatiotemporal Environments]]

![[assets/2611.18505_figure.png|800]]

- **arXiv**: [2611.18505](https://arxiv.org/abs/2611.18505)
- **PDF**: https://arxiv.org/pdf/2611.18505
- **详细分析**: [[20_Research/Papers/机器人/Disturbance-Aware_Informative_Planning_in_Spatiotemporal_Environments|Disturbance-Aware Informative Planning in Spatiotemporal Environments]]
- **作者**: Kaleb Ben Naveed, Haejoon Lee, Anouck Girard, Dimitra Panagou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Disturbance-Aware Informative Planning in Spatiotemporal Environments》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robots are widely used for persistent monitoring of spatiotemporal environments, where quantities of interest (QoI) change across space and time and require repeated measurements. In practice, robot motion can be affected by external disturbances that vary across the environment. When such external disturbances are not considered in trajectory optimization, it can lead to inaccurate predictions of robot motion and, consequently, the information acquired about the QoI during execution. However, estimating disturbances throughout the environment can be inefficient, as disturbances in regions with little overlap with monitoring trajectories have limited impact on monitoring performance. We therefore propose a two-stage informative planning framework for unknown, spatially varying but time-invariant disturbances, combining informed disturbance sampling with disturbance-aware trajectory optimization. First, we identify where QoI measurements are needed and generate alternative paths to these locations using the environment geometry. We then prioritize disturbance measurements based on their expected reduction of disturbance uncertainty along these paths. Second, rather than optimizing information acquisition based on nominal robot motion, we incorporate the learned disturbance belief into trajectory optimization to account for its effects on robot motion and information acquisition. Across four simulation scenarios, the proposed method reduces disturbance-learning time by 25.0--52.3 percent compared with environment-wide estimation and identifies paths that appear costly under nominal dynamics but become preferable when disturbances are considered.

</details>

---

### [[20_Research/Papers/机器人/Toward_Resilient_Self-Driving_Laboratories_through_Telerobotic_Interventions|Toward Resilient Self-Driving Laboratories through Telerobotic Interventions]]

![[assets/2611.18496_figure.png|800]]

- **arXiv**: [2611.18496](https://arxiv.org/abs/2611.18496)
- **PDF**: https://arxiv.org/pdf/2611.18496
- **详细分析**: [[20_Research/Papers/机器人/Toward_Resilient_Self-Driving_Laboratories_through_Telerobotic_Interventions|Toward Resilient Self-Driving Laboratories through Telerobotic Interventions]]
- **作者**: Ziheng Wu, Adrian Vecina Tercero, Andre A. Fatehi, Abhik Sarkar, Brian Giera, Eric B. Duoss, Christopher M. Spadaccini, Nikhil Deshpande, Aldair E. Gongora
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.0（加权：具身智能 0.3，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Toward Resilient Self-Driving Laboratories through Telerobotic Interventions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Self-driving laboratories (SDLs) accelerate scientific research by integrating robotics, automated experimentation, and machine learning to execute experiments autonomously. Biology and chemistry have adopted these systems. However, increasing SDL complexity heightens susceptibility to unexpected faults in automated workflows, highlighting the need for efficient recovery mechanisms. In this study, we investigate telerobotic interventions to enhance SDL resilience against unexpected failures. We developed a teleoperation interface enabling human operators to resolve disruptions during automated tasks. The interface enables precise control of a six-degree-of-freedom (DOF) robotic arm (UR3e) using a 3D mouse (3Dconnexion SpaceMouse Pro). Two velocity-based controller strategies were evaluated: (i) a coupled mode mapping all six DOFs to the 3D mouse's central knob and (ii) a decoupled mode separating translational and rotational motions. To evaluate the framework, teleoperators intervened across three SDL fault scenarios. In the first study, comparative trials showed that the decoupled controller was associated with shorter completion times and reduced rotational motion. In a second study, teleoperators performed an aiming task with and without reference-path guidance. Users were more target-driven and risk-tolerant without guidance but showed behavioral differences under different guidance strategies. These findings suggest that controller configuration and reference-path design influence operator performance during SDL fault recovery, informing teleoperation interface optimization. This work demonstrates the potential feasibility of teleoperation as a human-in-the-loop recovery mechanism for SDL workflows, combining robotic precision with human adaptability and problem-solving. These findings also provide a foundation for future studies in shared autonomy and semi-autonomous intervention.

</details>

---

### [[20_Research/Papers/强化学习/When_Will_You_Hand_It_Over_A_Hidden_Start_Delay_Makes_Self-Play_Handover_Robust_to_Unfamiliar_Partners|When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners]]

![[assets/2611.18491_figure.png|800]]

- **arXiv**: [2611.18491](https://arxiv.org/abs/2611.18491)
- **PDF**: https://arxiv.org/pdf/2611.18491
- **详细分析**: [[20_Research/Papers/强化学习/When_Will_You_Hand_It_Over_A_Hidden_Start_Delay_Makes_Self-Play_Handover_Robust_to_Unfamiliar_Partners|When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners]]
- **作者**: Mohammad Khoshnazar, Mike Degany, Deyuan Qu, Qing Yang, Matyas Szanto
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: RL

#### 研究背景与动机

《When Will You Hand It Over? A Hidden Start Delay Makes Self-Play Handover Robust to Unfamiliar Partners》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Cooperative self-play can teach a humanoid to receive an object without any human data, but the partner it meets after training is never the one it trained with; we show that a fluent self-play handover policy breaks with unfamiliar partners, identify the main cause, and repair it. In a physics-based parcel handover between a Unitree G1 and a learned giver, both trained by alternating PPO self-play, the receiver completes 95% and 90% of handovers with its own partner (two training seeds) but only 31% with scripted partners it has never met. Paired interventions isolate the cause: under a shared reward the learned giver always starts its offer at once, so the receiver learns a single rendezvous, and delaying its own partner by one second cuts success from 95% to 6% (87% to 34% in the second seed). We introduce hidden start-delay randomisation (HSD), a one-line rule on the learned partner that the receiver never observes. After 300 further updates, success with unseen scripted partners rises from 31% to 80% in both seeds, against 35--41% for a budget-matched control. The gain holds on a fresh scenario seed, on eleven held-out partner conditions and on partners that start later than any training delay; it cuts high-force contact three- to five-fold and needs no retraining of the partner.

</details>

---

### [[20_Research/Papers/机器人/CS-MPC_Contraction-Certified_Sampling-Based_MPC_for_Nonlinear_Systems_Under_Uncertainty|CS-MPC: Contraction-Certified Sampling-Based MPC for Nonlinear Systems Under Uncertainty]]

![[assets/2611.18390_figure.png|800]]

- **arXiv**: [2611.18390](https://arxiv.org/abs/2611.18390)
- **PDF**: https://arxiv.org/pdf/2611.18390
- **详细分析**: [[20_Research/Papers/机器人/CS-MPC_Contraction-Certified_Sampling-Based_MPC_for_Nonlinear_Systems_Under_Uncertainty|CS-MPC: Contraction-Certified Sampling-Based MPC for Nonlinear Systems Under Uncertainty]]
- **作者**: Yashwanth Kumar Nakka
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《CS-MPC: Contraction-Certified Sampling-Based MPC for Nonlinear Systems Under Uncertainty》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present contraction-certified sampling-based model predictive control (CS-MPC) for tracking and safety of nonlinear robotic systems under parametric uncertainty, disturbances, and safety constraints that are revealed online. CS-MPC uses a contraction-certified tracking feedback inside every sampled rollout, which concentrates the rollouts around the reference, and an execution layer that verifies the applied input using a quantile-tightened discrete-time control barrier function condition. We derive a verification procedure for nonlinear contraction of the feedback-closed dynamics, and we prove a finite-sample stochastic stability bound and a mission-level probabilistic safety guarantee. We validate CS-MPC in simulation on a rover, a quadrotor, and an asteroid landing. When compared with standard model predictive path integral (MPPI) control, CS-MPC attains the same tracking error with 7 to 20 times fewer rollouts for the rover, and a 2 to 4 times lower tracking error for the quadrotor, with no safety violations in 200 Monte Carlo missions.

</details>

---

### [[20_Research/Papers/强化学习/Heavy_Metal_Acrobatics_Learning_Dynamic_Control_for_Skid-Steer_Loaders|Heavy Metal Acrobatics: Learning Dynamic Control for Skid-Steer Loaders]]

![[assets/2611.18365_figure.png|800]]

- **arXiv**: [2611.18365](https://arxiv.org/abs/2611.18365)
- **PDF**: https://arxiv.org/pdf/2611.18365
- **详细分析**: [[20_Research/Papers/强化学习/Heavy_Metal_Acrobatics_Learning_Dynamic_Control_for_Skid-Steer_Loaders|Heavy Metal Acrobatics: Learning Dynamic Control for Skid-Steer Loaders]]
- **作者**: Pierre-Jean Lorentz, Pascal Egli, Edo Jelavic, Cliff Li, Ramitha Sundar, Harikrishnan Suresh, Paul Montgomery, Lee Redden, Matthias Müller, Ozan Sener, Vladlen Koltun, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Heavy Metal Acrobatics: Learning Dynamic Control for Skid-Steer Loaders》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Automation of heavy machinery offers the opportunity to improve productivity in mechanized industries such as construction, mining, and material handling. Yet, automation of such machines is challenged by their complex dynamics, in part because of hydraulic actuation that involves fluids, flexible elements, and nonlinear delays. A concomitant challenge is the size and weight of these machines, which can make experiments on the physical systems exceedingly dangerous. Here, we show that \ac{RL} in simulation, followed by transfer of the learned policies from simulation to reality, can successfully automate acrobatic maneuvers that push a heavy construction machine to the limits of its actuation and have only previously been accomplished by a small number of elite human operators in official world-record performances. We trained policies that perform autonomous acrobatic maneuvers on a John Deere 332G, an operational 5-tonne skid-steer loader. The policies can autonomously swing the machine up onto two wheels and, while balancing on two wheels, drive over rough terrain, trace out specified trajectories, spin around, and swing the bucket back and forth before landing it safely back onto four wheels. This work demonstrates that \ac{RL} and sim-to-real transfer enable dynamic autonomous control of heavy machinery, directly contributing to greater automation in heavy equipment sectors. Videos: https://sites.google.com/leggedrobotics.com/heavy-metal-acrobatics This is the author's version of the work. It is posted here by permission of the AAAS for personal use, not for redistribution. The definitive version was published in Science Robotics on 11 November 2026, DOI: https://doi.org/10.1126/scirobotics.aef0894

</details>

---

### [[20_Research/Papers/具身智能/PROOF_Perceptive_Robustness_via_Out-of-Distribution_Fallback_for_Legged_Locomotion|PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion]]

![[assets/2611.18305_figure.png|800]]

- **arXiv**: [2611.18305](https://arxiv.org/abs/2611.18305)
- **PDF**: https://arxiv.org/pdf/2611.18305
- **详细分析**: [[20_Research/Papers/具身智能/PROOF_Perceptive_Robustness_via_Out-of-Distribution_Fallback_for_Legged_Locomotion|PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion]]
- **作者**: Siyuan Wang, Dongjie Zhu, Jinxuan Lu, Wenjun Xu, Jiankun Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.8，机器人 0.7）
- **关联关键词**: Robotics

#### 研究背景与动机

《PROOF: Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based perceptive locomotion has enabled legged robots to achieve agile and terrain-aware locomotion across complex environments. However, the reliability of such systems heavily depends on visual observations, which are inherently susceptible to occlusion, reflective surfaces, and illumination variations, often resulting in catastrophic locomotion failures under degraded perception conditions. In this paper, we present PROOF (Perceptive Robustness via Out-of-Distribution Fallback for Legged Locomotion), a perceptive locomotion framework that enables robust locomotion under severe visual disturbances. Our method adopts a two-stage teacher-student learning paradigm that explicitly models perception reliability: the teacher learns both perception-driven and proprioceptive fallback behaviors, while the student predicts exteroceptive features with uncertainty and suppresses them under out-of-distribution inputs. We evaluate our method on a Unitree Go2 quadruped equipped with a RealSense D435 depth camera in real-world settings. Under normal visual conditions, our method enables the robot to successfully perform high-dynamic parkour maneuvers, including traversing large gaps, elevated platforms, and narrow beam terrains. Under severe visual degradation, such as heavy occlusion and strong illumination changes, the robot continues to maintain stable and robust locomotion performance.

</details>

---

### [[20_Research/Papers/具身智能/Objectives_as_Policies_Vision-Language_Model_Cost_Programs_for_Contact-Rich_Manipulation|Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation]]

![[assets/2611.18298_figure.png|800]]

- **arXiv**: [2611.18298](https://arxiv.org/abs/2611.18298)
- **PDF**: https://arxiv.org/pdf/2611.18298
- **详细分析**: [[20_Research/Papers/具身智能/Objectives_as_Policies_Vision-Language_Model_Cost_Programs_for_Contact-Rich_Manipulation|Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation]]
- **作者**: Zihao Lu, Trong Gia Hung Nguyen, Fuquan Wang, Yifan Zhu
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 具身智能, 机器人
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.7，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《Objectives as Policies: Vision-Language Model Cost Programs for Contact-Rich Manipulation》归入 大模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World, Real-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-language models (VLMs) have shown strong semantic and spatial reasoning capabilities in 3D environments. Recently, connecting VLMs with model-predictive controllers (MPC) has emerged as a paradigm for combining strong semantic reasoning with physics-based planning. However, connecting these two for contact-rich robotic manipulation requires a task representation that bridges the two and captures how physical interactions can be reasoned by VLMs. In this work, we introduce Objectives as Policies (OaP), a framework that connects a pretrained VLM to a shared sampling-based MPC through an editable objective program. Each program specifies a sequence of stages for completing a task, combining running and terminal costs from a cost library with stage completion conditions. Given a natural-language task instruction and scene observation, we build a simulation-based digital twin through real-to-sim, and the VLM generates an objective program that is executed by the MPC in the simulation. The program is iteratively updated by the VLM based on MPC rollouts, before being deployed in the real world. We evaluate our framework in both simulation and the real world on four tabletop manipulation tasks, and show that it outperforms strong baselines. Additional videos and examples are available on the project website: https://zihaolu001.github.io/oap-project/

</details>

---

### [[20_Research/Papers/具身智能/ESI_An_Embodied_Self-Improvement_Flywheel_for_LLM-VLA_Agents|ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents]]

![[assets/2611.18176_figure.png|800]]

- **arXiv**: [2611.18176](https://arxiv.org/abs/2611.18176)
- **PDF**: https://arxiv.org/pdf/2611.18176
- **详细分析**: [[20_Research/Papers/具身智能/ESI_An_Embodied_Self-Improvement_Flywheel_for_LLM-VLA_Agents|ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents]]
- **作者**: Yundi Cai, Zihan Wang, Chenxi Han, Yi Cheng, Houde Liu, Zilei Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 4.2（加权：具身智能 3，大模型 0.9，机器人 0.3）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《ESI: An Embodied Self-Improvement Flywheel for LLM-VLA Agents》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：LLM-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Independently pretrained language models and vision-language-action (VLA) policies provide complementary building blocks for embodied agents, but connecting them does not automatically produce coordinated behavior. The VLA may generate actions that diverge from the LLM's intended subtask and, upon regaining control after a correction, undo the promising state restored by the LLM. We introduce ESI (Embodied Self-Improvement), an automated flywheel that uses environmental interaction to align reasoning and action. ESI treats the modular agent as the unit of post-training, repeatedly refining the prompts that guide the LLM, the shared skill interface that expresses its intent, and the VLA parameters that realize that intent, then redeploying these components together. Our key insight is that collaboration itself can supply supervision for improving this interface. The LLM's subtask decisions provide semantic supervision for what the policy should execute, while its effective corrections and subsequent student continuations provide action-level supervision for recovery and handoff. The student also learns from its own effective execution, allowing locally useful experience to contribute even when the overall episode fails. On ten selected RoboDojo tasks, ESI achieves a mean Score of 62.03 and a mean success rate of 49.41% using an LLM-VLA agent without generating task-specific control code. On both metrics, it outperforms the published reference results of all hybrid embodied agents, including the Agent+WAM system GO-3 Nano Preview (47.27 Score and 36.60% success), as well as all compared code-based methods.

</details>

---

### [[20_Research/Papers/强化学习/PoliMop_Policy-in-the-Loop_Motion_Planning_in_3D_Spaces_for_Mobile_Robots|PoliMop: Policy-in-the-Loop Motion Planning in 3D Spaces for Mobile Robots]]

![[assets/2611.18110_figure.jpg|800]]

- **arXiv**: [2611.18110](https://arxiv.org/abs/2611.18110)
- **PDF**: https://arxiv.org/pdf/2611.18110
- **详细分析**: [[20_Research/Papers/强化学习/PoliMop_Policy-in-the-Loop_Motion_Planning_in_3D_Spaces_for_Mobile_Robots|PoliMop: Policy-in-the-Loop Motion Planning in 3D Spaces for Mobile Robots]]
- **作者**: Yael Fassbind, Valentin N. Hartmann, Huang Su, Yijiang Huang, Stelian Coros
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《PoliMop: Policy-in-the-Loop Motion Planning in 3D Spaces for Mobile Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reaching a goal state in a complex environment often requires a robot to overcome challenging terrain and obstacles. Which routes are accessible depends on the robot's physical design, the control policy it uses, and how it modifies its surroundings. We present a kinodynamic rapidly-exploring random tree (RRT) planner that uses physics simulation to exploit skills encoded in the control policy, which allows it to find a path in the scene with respect to the robot's capabilities. The planner samples states from a reduced state space in 3D around the scene and expands the RRT toward each sample using policy rollouts. We guide sampling with a preplanned path for a simple mass-point model to focus exploration on promising regions leading toward the goal state, reducing planning time by up to 63%. Simulation experiments with quadrupeds, humanoids, and wheeled robots demonstrate that our approach supports drop-in integration of various robots and control policies, exploiting their physical and policy capabilities without modifying the underlying planning algorithm. Predefined environmental modifications, such as placing a plank across a gap to build a bridge, will automatically be picked up by the planner as the robot's reachable space expands.

</details>

---

### [[20_Research/Papers/具身智能/Reusing_Locomotion_Training_Recipes_Across_Humanoids_via_Body-Aligned_Virtual_Joints|Reusing Locomotion Training Recipes Across Humanoids via Body-Aligned Virtual Joints]]

![[assets/2611.18003_figure.png|800]]

- **arXiv**: [2611.18003](https://arxiv.org/abs/2611.18003)
- **PDF**: https://arxiv.org/pdf/2611.18003
- **详细分析**: [[20_Research/Papers/具身智能/Reusing_Locomotion_Training_Recipes_Across_Humanoids_via_Body-Aligned_Virtual_Joints|Reusing Locomotion Training Recipes Across Humanoids via Body-Aligned Virtual Joints]]
- **作者**: Sol Choi, Mingon Kim, Seokin Seo, Jongeun Choi, Donghyeon Kim, Yisoo Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.7（加权：具身智能 1.8，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Reusing Locomotion Training Recipes Across Humanoids via Body-Aligned Virtual Joints》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reinforcement learning has enabled robust humanoid locomotion, yet training recipes (rewards, architectures, hyperparameters) remain hard to reuse across robots with different native joint coordinates, since policies output native joint angles while action scales, bounds, gains, and penalties are defined in those robot-specific coordinates. Existing transmission models convert native targets into actuator commands but do not standardize the coordinate interface exposed to the policy. We introduce a body-aligned virtual joint space upstream of this mapping: policy actions and observations follow a common anatomical convention, and a deterministic kinematic layer maps virtual targets to native ones, leaving the existing transmission and low-level control stack unchanged. Under a single unmodified recipe on three humanoids with different leg-axis layouts, it is the only interface that tracks accurately, keeps the feet aligned with the travel direction, and trains stably on all three, and on Unitree G1 hardware it reduces heading drift by nearly a factor of six.

</details>

---

### [[20_Research/Papers/具身智能/Per-Agent-Safe_Navigation_of_Globally_Driven_Robot_Collectives_via_Affine_Field_Design|Per-Agent-Safe Navigation of Globally Driven Robot Collectives via Affine Field Design]]

![[assets/2611.17859_figure.png|800]]

- **arXiv**: [2611.17859](https://arxiv.org/abs/2611.17859)
- **PDF**: https://arxiv.org/pdf/2611.17859
- **详细分析**: [[20_Research/Papers/具身智能/Per-Agent-Safe_Navigation_of_Globally_Driven_Robot_Collectives_via_Affine_Field_Design|Per-Agent-Safe Navigation of Globally Driven Robot Collectives via Affine Field Design]]
- **作者**: Seunghwan Jang, Steven Ceron, Wei Xiao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Per-Agent-Safe Navigation of Globally Driven Robot Collectives via Affine Field Design》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe navigation of robot collectives requires coordinating motion and deformation so that the collective can traverse constrained environments while ensuring each robot's safety. Existing controllers for swarmalator collectives largely rely on local control, where each robot receives an individual command, which causes the control and communication requirements to grow with the number of agents. We introduce a broadcast control formulation in which a single spatially affine field governs both the motion and deformation of the collective. The scalar component of the field regulates collective size, and its spatial gradient generates collective translation through non-reciprocal interactions. Both components enter the collective dynamics directly, which allows per-robot wall, actuation, and cohesion constraints to be enforced using control barrier functions within a single quadratic program for the whole collective. The resulting controller continuously adapts the collective size to the local environment, and enables safe passage through corridors narrower than the unconstrained collective without pre-planned resizing. We further derive how the available actuation budget determines the reachable speed and minimum passable corridor width, and we demonstrate that two independently driven collectives can simultaneously traverse a shared junction using distinct fixed phase labels without inter-collective coordination.

</details>

---

### [[20_Research/Papers/具身智能/ERA_Error-Resistant_Autonomous_Object_Navigation_with_Predicted_Depth|ERA: Error-Resistant Autonomous Object Navigation with Predicted Depth]]

![[assets/2611.17730_figure.png|800]]

- **arXiv**: [2611.17730](https://arxiv.org/abs/2611.17730)
- **PDF**: https://arxiv.org/pdf/2611.17730
- **详细分析**: [[20_Research/Papers/具身智能/ERA_Error-Resistant_Autonomous_Object_Navigation_with_Predicted_Depth|ERA: Error-Resistant Autonomous Object Navigation with Predicted Depth]]
- **作者**: Shunyang Huang, Shuo Wang, Wenyuan Xie, Mingyu Lin, Yue Ding, Hongtao Lu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.1（加权：具身智能 1.5，大模型 0.1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《ERA: Error-Resistant Autonomous Object Navigation with Predicted Depth》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Depth and 3D foundation models can predict geometry from RGB images, allowing zero-shot object navigation without a depth sensor. However, when predicted depth is mapped as if it came from a sensor, view-dependent errors accumulate in the map, remove exploration goals, and end the search before the agent can observe and correct them. We propose ERA, a training-free object navigation system that replaces the depth sensor with depth predicted from RGB images and poses. ERA follows a paradigm we call Move with Error: movement provides new views that correct map errors, and the corrected map enables further movement. It realizes this paradigm with revisable occupancy and with exploration from reachable viewpoints, which continues the search when no frontier remains, and verifies the target across views before stopping. On three benchmarks, ERA achieves state-of-the-art performance among training-free methods without depth sensors. Its map and exploration components also raise VLFM's success from 10.8% to 61.7% under the same predicted depth. We further deploy ERA on a real robot.

</details>

---

### [[20_Research/Papers/机器人/AI-guided_robotic_in_situ_fabrication_of_curvature-_and_tissue-adaptive_wireless_bioelectronics|AI-guided robotic in situ fabrication of curvature- and tissue-adaptive wireless bioelectronics]]

![[assets/2611.17638_first_page.png|800]]

- **arXiv**: [2611.17638](https://arxiv.org/abs/2611.17638)
- **PDF**: https://arxiv.org/pdf/2611.17638
- **详细分析**: [[20_Research/Papers/机器人/AI-guided_robotic_in_situ_fabrication_of_curvature-_and_tissue-adaptive_wireless_bioelectronics|AI-guided robotic in situ fabrication of curvature- and tissue-adaptive wireless bioelectronics]]
- **作者**: Hiroyuki Tetsuka, Jiaju Ma, Naomi Kumano, Minoru Hirano
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《AI-guided robotic in situ fabrication of curvature- and tissue-adaptive wireless bioelectronics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Personalized bioelectronic devices for wound therapy require not only conformal fabrication on complex body surfaces but also functional adaptation of their electrical characteristics to individual wound geometries. Here, we present an AI-guided robotic in situ printing platform for fabricating wireless wound electrotherapy devices directly on transparent wound dressings. The system integrates a 3D vision camera, a six-degree-of-freedom robotic arm, direct-ink-writing, and geometry-aware RF design optimization. AI-based wound segmentation is used to determine wound dimensions and local surface curvature, while the reconstructed three-dimensional geometry is incorporated into the electromagnetic design of the receiving coil and interdigitated electrodes. In contrast to conventional approaches that use surface geometry only for trajectory generation, the proposed method accounts for both anatomical curvature and tissue dielectric loading to compensate for geometry-induced shifts in resonant behavior. A printable silver ink was characterized in terms of rheology, dimensional reproducibility, electrical resistance, and electromechanical stability, and was used to fabricate multilayer wireless devices directly on curved polyurethane dressings. Wireless power transfer, impedance characteristics, and electric-field delivery were evaluated experimentally and numerically. Finally, robotic in situ fabrication was demonstrated on an anthropomorphic tissue-equivalent forearm phantom, where the measured dielectric properties of the phantom were incorporated into the RF optimization, enabling resonant operation near the target frequency of 25 MHz. This work establishes a perception-to-design-to-fabrication framework for geometry-adaptive wireless bioelectronics and provides a technological foundation for future physical-AI-enabled manufacturing of personalized on-body electrotherapy devices.

</details>

---

### [[20_Research/Papers/具身智能/On_the_Utility_of_Pre-Trained_Visual_Representations_for_Policy_Learning_of_Contact-Rich_Insertion_Tasks|On the Utility of Pre-Trained Visual Representations for Policy Learning of Contact-Rich Insertion Tasks]]

![[assets/2611.17631_figure.png|800]]

- **arXiv**: [2611.17631](https://arxiv.org/abs/2611.17631)
- **PDF**: https://arxiv.org/pdf/2611.17631
- **详细分析**: [[20_Research/Papers/具身智能/On_the_Utility_of_Pre-Trained_Visual_Representations_for_Policy_Learning_of_Contact-Rich_Insertion_Tasks|On the Utility of Pre-Trained Visual Representations for Policy Learning of Contact-Rich Insertion Tasks]]
- **作者**: Leon Kim, Dinesh Jayaraman, Michael Posa
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.6，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《On the Utility of Pre-Trained Visual Representations for Policy Learning of Contact-Rich Insertion Tasks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：MetaWorld, Real-World, ResNet, U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visuomotor imitation learning has become a predominant paradigm for real-world robotic manipulation, yet it remains data-inefficient and brittle to task-irrelevant visual shifts. Pre-trained visual representations promise to ease this burden by distilling priors from internet-scale data, but the ``right'' representation for robotics remains unresolved: existing studies span broad but sparse task distributions and reach conclusions that vary and even conflict, pointing to strong task and setting dependence. We examine this question by bringing a magnifying glass to a common contact-rich manipulation task: insertion. We compare representations from widely used vision foundation models against an explicit contact-centric representation on two closely related insertion tasks, perturb each along controlled axes of occlusion and physical tolerance, and test whether conclusions transfer to the real world. Task dependence proves to be more subtle than previous, broadly scoped evaluations revealed: the best representation differs even between our near-identical tasks, and small changes shift trends in unpredictable ways. Despite this variability, results across simulation and real-world experiments demonstrate the distinct value of spatially-grounded, and in particular, contact-centric information for contact-rich policy learning, while underscoring how difficult it is to estimate such cues reliably under realistic visual complexity and sensor noise. We hope these findings motivate further study of representations in contact-rich manipulation, along with advances in contact perception and its integration into visuomotor policy learning.

</details>

---

### [[20_Research/Papers/强化学习/TouchTwin_Scaling_Human_Touch_Data_via_Real-to-Sim-to-Real|TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real]]

![[assets/2611.17619_figure.png|800]]

- **arXiv**: [2611.17619](https://arxiv.org/abs/2611.17619)
- **PDF**: https://arxiv.org/pdf/2611.17619
- **详细分析**: [[20_Research/Papers/强化学习/TouchTwin_Scaling_Human_Touch_Data_via_Real-to-Sim-to-Real|TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real]]
- **作者**: Huiwen Han, Nuo Chen, Ziyao Zeng, Dayou Li, Hao Wang, Amir Hossein Rahmati, Xiaoning Qian, Bangya Liu, Zhiwen Fan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《TouchTwin: Scaling Human Touch Data via Real-to-Sim-to-Real》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：CoRL, Real-to-Sim, X-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human demonstrations are becoming the main source of data for dexterous manipulation, and real-to-sim-to-real pipelines multiply each demonstration in simulation. These pipelines rebuild the interaction from vision, which recovers how the hand moves. Which fingers touch, when, and how hard remain unobserved, because a hand pose shows where each finger stops on the surface rather than how far it is driven to close. This gap is a force gap: on held-out recordings, a hand policy that imitates the observed pose grips with 0.31x the recorded force, and a policy trained on physics replays of vision-tracked poses grips with 1.55x. TouchTwin closes the gap with measured human touch. Each selected TouchScale recording, captured with head and wrist RGB-D cameras and an 880-taxel glove, is rebuilt in MuJoCo. Coding agents write the objects as physics-tested programs, and a per-subject tactile hand replays the interaction with the recorded touch setting the contact and the closing force of each finger. In simulation, a policy trained on touch-grounded replays grips at 0.99x the recorded force and succeeds in 20/20 trials on held-out recordings and 35/36 unseen perturbations; a contact predictor trained on them misses 13% of real contact frames, against 32% for vision-based replays. Each replay also seeds perturbed demonstrations with simulated contact and force labels, rendered as realistic video in new views and scenes.

</details>

---

### [[20_Research/Papers/机器人/Natural_Swing-Up_of_an_Underpowered_Double_Pendulum|Natural Swing-Up of an Underpowered Double Pendulum]]

![[assets/2611.17575_figure.png|800]]

- **arXiv**: [2611.17575](https://arxiv.org/abs/2611.17575)
- **PDF**: https://arxiv.org/pdf/2611.17575
- **详细分析**: [[20_Research/Papers/机器人/Natural_Swing-Up_of_an_Underpowered_Double_Pendulum|Natural Swing-Up of an Underpowered Double Pendulum]]
- **作者**: Arne Sachtler, Manuel Keppler, Florian Loeffl, Alin Albu-Schäffer
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics

#### 研究背景与动机

《Natural Swing-Up of an Underpowered Double Pendulum》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots with weak motors must ride their natural dynamics rather than fight them. We swing up a direct-drive planar two-link robot, whose motors deliver only about 6\,\% of its shoulder gravity torque, along its nonlinear normal modes, two-dimensional invariant manifolds consisting of periodic orbits. On a non-strict mode, injecting energy necessarily moves the state off the manifold, so pumping and stabilization compete for the same bounded torque. We split the input torque into a power-neutral steering component and a scalar pumping input, the only component that changes the energy. The allocation then becomes a linear program in two variables: maximize pumping subject to the torque limits and one control-Lyapunov constraint. The constraint uses the model-based rate of the error, so no stabilizing feedback gain is needed. Experiments in hardware show swing-ups along both modes and compare the allocation with summing-and-clipping and with prioritized stabilization.

</details>

---

### [[20_Research/Papers/具身智能/Grounding_Object-to-Object_Hazard_Reasoning_into_3D_Risk_Fields_for_Task-Conditioned_Safety|Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety]]

![[assets/2611.17566_figure.png|800]]

- **arXiv**: [2611.17566](https://arxiv.org/abs/2611.17566)
- **PDF**: https://arxiv.org/pdf/2611.17566
- **详细分析**: [[20_Research/Papers/具身智能/Grounding_Object-to-Object_Hazard_Reasoning_into_3D_Risk_Fields_for_Task-Conditioned_Safety|Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety]]
- **作者**: Mariana Sosa Guzmán, Yide Song, Amin Abyaneh, Gregory Dudek, Hsiu-Chin Lin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.1，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《Grounding Object-to-Object Hazard Reasoning into 3D Risk Fields for Task-Conditioned Safety》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safety in robotics does not solely depend on geometric constraints, but also on semantics: the given task, environment properties, and interactions between objects in the scene. We present a framework based on vision-language models (VLMs) to infer task- and scene-dependent safety constraints for robot manipulation. We provide the VLM a structured safety tool based on an RGB-D observation and a natural-language task instruction that first decides whether the task should be rejected since its execution may result in a non-recoverable hazardous outcome. Otherwise, it identifies preventable object-pair hazards and specifies the spatial relations that must be avoided. Open-vocabulary segmentation and depth information are then used to ground the detected objects in 3D and construct continuous risk fields that represent the corresponding hazardous regions. These fields are integrated with an obstacle avoidance module that corrects nominal robot motions during execution while accounting for the risk field. We evaluate the framework on preventable hazards, tasks requiring rejection, and safe variants in simulation and the real-world. Project website: https://vlm-hazard-riskfield.github.io

</details>

---

### [[20_Research/Papers/机器人/Talk_to_Act_A_Synthetic_Multi-Turn_Dialogue_Benchmark_for_Human_Intent_Extraction_and_Action_Planning_in_Robotics|Talk to Act: A Synthetic Multi-Turn Dialogue Benchmark for Human Intent Extraction and Action Planning in Robotics]]

![[assets/2611.17549_figure.png|800]]

- **arXiv**: [2611.17549](https://arxiv.org/abs/2611.17549)
- **PDF**: https://arxiv.org/pdf/2611.17549
- **详细分析**: [[20_Research/Papers/机器人/Talk_to_Act_A_Synthetic_Multi-Turn_Dialogue_Benchmark_for_Human_Intent_Extraction_and_Action_Planning_in_Robotics|Talk to Act: A Synthetic Multi-Turn Dialogue Benchmark for Human Intent Extraction and Action Planning in Robotics]]
- **作者**: Deepu Krishnareddy, Mohammad Haziq Khan, Michael Danner, Matthias Rätsch
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，机器人 1.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Talk to Act: A Synthetic Multi-Turn Dialogue Benchmark for Human Intent Extraction and Action Planning in Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-turn conversational human-robot interaction (HRI) continues to be a challenging problem in robotics, as many existing systems rely on rigid, command-driven interfaces that can be unintuitive for users. Recent advances in Large Language Models (LLMs) provide a promising direction, given their ability to process natural language, generate structured outputs, and support tool-based reasoning, all of which are relevant for interpreting user intent in robotic settings. However, progress in this area is constrained by the limited availability of datasets and benchmarks that capture the nuances of real-world human communication, such as multi-turn dialogue, ambiguity, and context-dependent requests. In this work, we present a synthetically generated multi-turn dialogue dataset for HRI, annotated with action intents, object references, and task plans across a range of scenarios and user personas. Our primary focus is on evaluating the capability of small, open-weight language models for robotic tasks, particularly in settings where local deployment and efficiency are important. To this end, we frame intent extraction as a tool-calling problem where each predicted action corresponds to a structured function call with arguments grounded in the dialogue and benchmark models ranging from 270M to 8B parameters on their ability to perform intent extraction and action planning without task-specific fine-tuning. Our results show that these models can achieve reasonable performance on the task even at relatively small scales and without any task-specific fine-tuning. This suggests that compact, locally deployable models already provide a useful baseline for conversational robotic systems. We expect that task-specific fine-tuning and more realistic training data will enhance performance further and make such models increasingly suitable for real-world robotic applications.

</details>

---

### [[20_Research/Papers/具身智能/Agentic-Teacher_An_Agentic_Data_Engine_for_Failure-Driven_VLA_Post-Training|Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training]]

![[assets/2611.17394_figure.png|800]]

- **arXiv**: [2611.17394](https://arxiv.org/abs/2611.17394)
- **PDF**: https://arxiv.org/pdf/2611.17394
- **详细分析**: [[20_Research/Papers/具身智能/Agentic-Teacher_An_Agentic_Data_Engine_for_Failure-Driven_VLA_Post-Training|Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training]]
- **作者**: Gongyue Teng, Yuqing Xie, Yixian Zhang, Feng Gao, Shu'ang Yu, Jiaji Rao, Sukai Wang, Guanghui Ren, Ya Zhang, Maoqing Yao, Yu Wang, Chao Yu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.3（加权：具身智能 1.8，大模型 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, RL

#### 研究背景与动机

《Agentic-Teacher: An Agentic Data Engine for Failure-Driven VLA Post-Training》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Contact-GraspNet, MetaWorld, RLinf-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Improving a pretrained vision-language-action (VLA) model requires demonstrations that address its weaknesses and provide effective supervision for learning. Coding agents can autonomously generate demonstrations through environment interaction, yet successful execution alone does not ensure effective supervision for VLA learning. We introduce Agentic-Teacher, an autonomous data engine for failure-driven VLA post-training. Given a VLA checkpoint, a task specification, and configured environment tools, the engine analyzes failed rollouts, selects intervention states, and iteratively develops closed-loop code policies through execution feedback. Validated policies become reusable demonstration generators that collect successful continuations from states where the VLA struggles. To make these demonstrations suitable for learning, Agentic-Teacher introduces temporally correlated action noise to broaden state-action coverage, removes idle frames while preserving gripper transitions, and filters trajectories using the frozen base model's flow-matching loss. The resulting demonstrations are combined with successful VLA rollouts for post-training, yielding an updated policy that operates without coding-agent assistance. Agentic-Teacher thus connects the weaknesses of a target VLA to both the generation and curation of its training data. In simulation, it improves $π_0$ success rates from 79.4% to 87.8% on LIBERO-10, from 80.4% to 90.6% on MetaWorld-10, and from 0% to 30.0% across three RoboCasa tasks.

</details>

---

### [[20_Research/Papers/具身智能/Prediction-Error-Tightened_MPC_for_Socially_Compliant_Crowd_Navigation|Prediction-Error-Tightened MPC for Socially Compliant Crowd Navigation]]

![[assets/2611.15781_figure.png|800]]

- **arXiv**: [2611.15781](https://arxiv.org/abs/2611.15781)
- **PDF**: https://arxiv.org/pdf/2611.15781
- **详细分析**: [[20_Research/Papers/具身智能/Prediction-Error-Tightened_MPC_for_Socially_Compliant_Crowd_Navigation|Prediction-Error-Tightened MPC for Socially Compliant Crowd Navigation]]
- **作者**: Alessandro Febbraro, Federico Rollo, Marcello Farina, Luca Bascetta, Navvab Kashiri
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Prediction-Error-Tightened MPC for Socially Compliant Crowd Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous navigation of mobile robots in crowded environments, while preserving pedestrians' psychological comfort, requires distinguishing pedestrians from other obstacles, predicting their future motion, and accounting for uncertainty in the predicted trajectories of both pedestrians and the robot. This work extends a previous MPC framework by integrating obstacle and pedestrian detection, Koopman-based motion prediction, and online prediction-error estimation directly within the collision-avoidance mechanism. To reduce collision-avoidance complexity in crowded scenarios, nearby obstacles are aggregated, thereby reducing the number of collision-avoidance constraints. Simulation studies evaluate the prediction-error margins and the computational benefits of semantics-aware aggregation. In a paired 300-seed closed-loop comparison with a moving generic obstacle, Markov residual tightening reduces the fraction of runs with physical contact from $10.0\%$ to $1.33\%$, at a mean travel-time cost of $0.68$ s. In a separate crowd-navigation semantic ablation, the offline robot-footprint/personal-space overlap occupies $2.11\%$ of observed time with pedestrian-aware handling versus $22.84\%$ with generic-obstacle handling.

</details>

---
