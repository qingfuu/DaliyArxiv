# cs.RO | Robotics | 2026-11-11

#arxiv #ComputerScience

**论文数**: 30

### [[20_Research/Papers/具身智能/Is_Your_Robot's_Memory_Just_a_Clock_Temporal_Shortcuts_in_Memory-Augmented_VLA_Policies|Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies]]

![[assets/2611.14488_figure.png|800]]

- **arXiv**: [2611.14488](https://arxiv.org/abs/2611.14488)
- **PDF**: https://arxiv.org/pdf/2611.14488
- **详细分析**: [[20_Research/Papers/具身智能/Is_Your_Robot's_Memory_Just_a_Clock_Temporal_Shortcuts_in_Memory-Augmented_VLA_Policies|Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies]]
- **作者**: Chubin Zhang, Bo An
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Is Your Robot's Memory Just a Clock? Temporal Shortcuts in Memory-Augmented VLA Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：MME-VLA, MemoryBench, SimpleMemVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Memory-augmented vision-language-action (VLA) policies are meant to remember what happened. Many of them, however, fill memory by time: they sample frames uniformly across the episode and stamp each frame with its time step. Because time passes even when nothing happens, such a memory may not tell waiting from working. We show that it does not. On the counting tasks of RoboMME, we make the robot briefly pause or fidget its wrist. Such a null event changes nothing the task depends on, yet a released memory VLA counts the interval as work done and stops early. We call this failure phantom progress. It cuts success from 47 to 16 of 50 on one task and from 44 to 10 on the other. When the same frames are withheld from memory, success returns, so the cause lies in memory rather than in the interruption itself. We trace the failure to a temporal shortcut: because demonstrations proceed at a steady pace, elapsed time predicts progress. Indeed, rescaling the time stamps alone makes the policy stop early when the clock runs fast and repeat when it runs slow. Surprisingly, removing the time encoding does not cure the failure, because the frames of a null event still occupy slots of the time-sampled memory. Across RoboMME's released designs, vulnerability follows how memory is indexed. Of the fixes the diagnosis suggests, training with injected pauses does not remove the failure and impairs counting, whereas indexing memory by events recovers half or more of the loss without retraining. A memory meant to remember what happened should count events rather than clock ticks.

</details>

---

### [[20_Research/Papers/具身智能/SIGMO_Sigmoid_Gated_Interaction-Aware_Motion_Planning|SIGMO: Sigmoid Gated Interaction-Aware Motion Planning]]

![[assets/2611.14414_figure.png|800]]

- **arXiv**: [2611.14414](https://arxiv.org/abs/2611.14414)
- **PDF**: https://arxiv.org/pdf/2611.14414
- **详细分析**: [[20_Research/Papers/具身智能/SIGMO_Sigmoid_Gated_Interaction-Aware_Motion_Planning|SIGMO: Sigmoid Gated Interaction-Aware Motion Planning]]
- **作者**: Avinash Singh, Manish Saroya, Fatemeh Cheraghi Pouria, Faizan Tariq, Jovin D'sa, David Isele, Yosuke Sakamoto, Sangjae Bae
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, EmbodiedAI

#### 研究背景与动机

《SIGMO: Sigmoid Gated Interaction-Aware Motion Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Despite the widespread adoption of autonomous vehicle technologies, reliable navigation within cluttered environments remains arduous due to the necessity of interaction-aware strategies; example scenarios include: narrow passages with multiple agents, lane changing in dense traffic, and crossing unsignalized intersections. These scenarios often require highly proactive strategies, simultaneously demanding interpretability and quick adaptability, which challenge end-to-end and data-driven methods. An effective strategy requires: scalability to multiple agents, adaptability to changes in other agents' behavior, and harmony with surrounding traffic without freezing or becoming overly conservative. To meet these requirements, we present SIGMO, a sigmoid-gated interaction-aware motion planner, with two main contributions. First, we formulate polynomial sigmoid functions that analytically estimate yield scores of surrounding agents using physics-grounded interaction features that capture driving intuitions. Second, we integrate the polynomial sigmoid functions into a receding-horizon planner, which facilitates interaction-aware planning with arbitrary trajectory predictions. We validate SIGMO in interaction-intensive simulations and hardware experiments. The results show that SIGMO balances proactive and defensive behavior while remaining computationally lightweight, serving as a strong baseline in a mobility stack. The simulation and hardware experiment videos are available here: https://sites.google.com/view/sigmoid-polygate.

</details>

---

### [[20_Research/Papers/强化学习/From_Prediction_to_Action_Learning_Physical_Context_for_Deformable_Linear_Object_Manipulation|From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation]]

![[assets/2611.14274_figure.png|800]]

- **arXiv**: [2611.14274](https://arxiv.org/abs/2611.14274)
- **PDF**: https://arxiv.org/pdf/2611.14274
- **详细分析**: [[20_Research/Papers/强化学习/From_Prediction_to_Action_Learning_Physical_Context_for_Deformable_Linear_Object_Manipulation|From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation]]
- **作者**: Chengxiao Dong, Alessio Caporali, Hongyu Lan, Gianluca Palli
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《From Prediction to Action: Learning Physical Context for Deformable Linear Object Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A representation that accurately predicts a deformable object's response is not necessarily the one most useful for choosing manipulation actions. We study this distinction between predictive utility and decision utility in planar single-grasp shape control of Deformable Linear Objects (DLOs). As a common decision backbone, we introduce Geometry-Pointer-Flow (GPF), a geometry-grounded policy that separates grasp-location selection from grasp-conditioned motion generation. Its geometry-only variant reduces one-step executed shape error by 32.8% relative to a DLO-specific diffusion policy, while using 18.7 times fewer parameters and achieving approximately 193 times faster inference. On this backbone, we compare physical context represented by ground-truth parameters, estimated parameters, and learned interaction-history representations, for both forward prediction and executed control. For prediction, ground-truth physical parameters reduce next-shape error by 15.8% over geometry alone, and estimated parameters are slightly more predictive than interaction history. This ordering does not carry over to control: estimated parameters provide no detectable one-step control gain, whereas history-conditioned GPF reduces executed error by 9.9% relative to geometry-only GPF across 470 paired simulation trials. In closed loop, interaction history improves strict-threshold attainment in simulation and yields the strongest zero-shot performance on hardware. All policies are trained exclusively in simulation and transferred to the physical robot without real-world training or fine-tuning. These results show that physical context should be evaluated by the decisions it supports rather than by predictive accuracy alone. Code will be released upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/Koopman_Model-Based_Reinforcement_Learning|Koopman Model-Based Reinforcement Learning]]

![[assets/2611.14186_figure.png|800]]

- **arXiv**: [2611.14186](https://arxiv.org/abs/2611.14186)
- **PDF**: https://arxiv.org/pdf/2611.14186
- **详细分析**: [[20_Research/Papers/具身智能/Koopman_Model-Based_Reinforcement_Learning|Koopman Model-Based Reinforcement Learning]]
- **作者**: Wenjian Hao, Paulo C. Heredia, Shaoshuai Mou
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 3.6（加权：具身智能 0.9，强化学习 1，世界模型 0.8，机器人 0.9）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Koopman Model-Based Reinforcement Learning》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：K-MBRL, MBRL, MFRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We propose a Koopman model-based reinforcement learning (K-MBRL) algorithm for controlling nonlinear robotic systems with unknown dynamics. The K-MBRL learns a control policy by minimizing an approximate policy objective that combines the analytical immediate cost with an estimate of the future cost evaluated at the one-step predicted state. To this end, we develop a stochastic Koopman operator-based learning method to approximate the unknown nonlinear dynamics in a linear representation, while a critic function estimates the remaining future cost. This formulation offers two key advantages. First, the linear Koopman dynamics simplify the model-dependent policy gradient computation to a constant matrix product, enabling computationally efficient policy improvement. Second, one-step model propagation mitigates the accumulation of prediction errors associated with long-horizon rollouts while retaining long-term cost information through the critic. The learned policy enables real-time control through feedforward evaluation without online optimization. We establish policy learning convergence guarantees under standard stochastic approximation assumptions. Simulations on HalfCheetah and quadruped four-legged locomotion tasks demonstrate strong sample efficiency and improved performance compared with classical model-free and model-based reinforcement learning baselines. A pendulum swing-up task is used to assess policy gradient approximation accuracy and conduct ablation studies on the learning mechanism and key hyperparameters. The proposed K-MBRL is further validated on a physical quadruped robot performing a challenging sequence of maneuvers: rising to an upright posture supported by two rounded rear feet, maintaining balance during bipedal walking, and safely returning to the ground, as shown in Fig.1.

</details>

---

### [[20_Research/Papers/具身智能/LEASH_Stay_Safe_in_Agentic_Robotics|LEASH: Stay Safe in Agentic Robotics]]

![[assets/2611.14115_figure.png|800]]

- **arXiv**: [2611.14115](https://arxiv.org/abs/2611.14115)
- **PDF**: https://arxiv.org/pdf/2611.14115
- **详细分析**: [[20_Research/Papers/具身智能/LEASH_Stay_Safe_in_Agentic_Robotics|LEASH: Stay Safe in Agentic Robotics]]
- **作者**: Qinfeng Zhu, Weiguang Zhao, Ke Sun, Xihao Guo, Yunxi Jiang, Rui Zhang, Lei Fan, Kaizhu Huang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《LEASH: Stay Safe in Agentic Robotics》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Foundation models such as GPT and Claude have shown strong capabilities in spatial understanding and embodied intelligence. These advances make agentic robotics a promising path toward artificial general intelligence in robotics. However, we find that using foundation models to control robots poses serious safety risks, and comprehensive safety evaluation is still lacking. We introduce RoboRisk, a comprehensive benchmark for evaluating safety in agentic robotics. Its 92 simulated tasks and 13 physical-robot tasks fall into five categories: Task-level Refusal (T), Plan Repair (P), Execution-time Hazard (E), Injection (I), and Sequential Memory (S). Prior benchmarks cover at most two of these categories, and several evaluate only text outputs. In contrast, RoboRisk covers all five and executes every task in closed loop. We evaluate six state-of-the-art foundation models on RoboRisk: GPT-6 Astra, GPT-6.1 Sol, GPT-6 Luna, Claude Opus 5.5, Gemini 4 Argon, and Grok 4.7. These models generally show high harm rates. We also evaluate two robot-specific APIs: the Dream API and PokeBot's RoboAPI. We further propose the Lease-Enforced Agentic Safety Harness (LEASH), which offers essential safety infrastructure for agentic robotics and can be integrated into nearly any agentic architecture. LEASH leverages a decision model (Jev or OpenAI's Decisions API) to implement task, action, and commit gates, which review the task, each action, and each irreversible operation in their visual context. The planner and all three gates share a common safety policy. Experiments on RoboRisk in simulation and on physical robots show that LEASH effectively reduces harm across all six foundation models. It largely preserves their task completion performance and adds little time and token overhead.

</details>

---

### [[20_Research/Papers/具身智能/DexSeed_Expanding_Human_Hand-Object_Interactions_into_Robot_Demonstrations_for_Dexterous_Policy_Learning|DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning]]

![[assets/2611.14092_figure.png|800]]

- **arXiv**: [2611.14092](https://arxiv.org/abs/2611.14092)
- **PDF**: https://arxiv.org/pdf/2611.14092
- **详细分析**: [[20_Research/Papers/具身智能/DexSeed_Expanding_Human_Hand-Object_Interactions_into_Robot_Demonstrations_for_Dexterous_Policy_Learning|DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning]]
- **作者**: Huaijin Pi, Zehong Shen, Yong Wang, Kechun Xu, Changpeng Wang, Dingkun Wei, Xueyang Wang, Wenjia Wang, Xing Zhu, Yujun Shen, Taku Komura
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《DexSeed: Expanding Human Hand-Object Interactions into Robot Demonstrations for Dexterous Policy Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study how to generate diverse, physically executable robot demonstrations for dexterous vision-language-action (VLA) learning. Existing demonstration-generation methods typically rely on costly teleoperated examples. Meanwhile, human hand--object datasets provide a reusable source, but existing transfer methods mainly reproduce given interactions. Turning these interactions into VLA training data further requires coverage of different objects and manipulation locations, together with executable arm and finger actions, and visual observations. To achieve this, we present DexSeed, a framework for low-cost generation of dexterous robot data from human hand--object interactions. Our key idea is to expand human sequences while preserving their grasps and realizing the resulting motions under arm-tracking dynamics in physics simulation. Specifically, we organize source sequences by grasp mode with shared language descriptions. InteractionMesh-based retargeting and arm trajectory augmentation adapt these sequences to the robot hand, different object geometries, and pick-and-place locations while preserving local hand--object relationships. An RL finger-control policy produces executable rollouts, while the arm tracks precomputed trajectories. Rendered observations and recorded actions from successful rollouts are paired with grasp descriptions to fine-tune a VLA. Experiments show improved contact fidelity in retargeting and more reliable whole-arm execution than the evaluated baselines. Simulation evaluation and real-world deployment further demonstrate that a VLA fine-tuned solely on the generated demonstrations can execute language-specified grasps. Project page: https://robbyant-research.github.io/DexSeed/.

</details>

---

### [[20_Research/Papers/机器人/A_human-in-the-loop_Control_Paradigm_for_Construction_Robotics_From_VR-Guided_Teleoperation_to_Semi-Autonomous_Dual-Arm_Operation|A human-in-the-loop Control Paradigm for Construction Robotics: From VR-Guided Teleoperation to Semi-Autonomous Dual-Arm Operation]]

![[assets/2611.14062_figure.png|800]]

- **arXiv**: [2611.14062](https://arxiv.org/abs/2611.14062)
- **PDF**: https://arxiv.org/pdf/2611.14062
- **详细分析**: [[20_Research/Papers/机器人/A_human-in-the-loop_Control_Paradigm_for_Construction_Robotics_From_VR-Guided_Teleoperation_to_Semi-Autonomous_Dual-Arm_Operation|A human-in-the-loop Control Paradigm for Construction Robotics: From VR-Guided Teleoperation to Semi-Autonomous Dual-Arm Operation]]
- **作者**: Jinhua Chen, Xiaoji Xu, Zhongyuan Liao, Huang Zhenmin, Zhang Ye, Changying Xiang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《A human-in-the-loop Control Paradigm for Construction Robotics: From VR-Guided Teleoperation to Semi-Autonomous Dual-Arm Operation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Construction tasks in hazardous and unstructured environments require both human adaptability and robotic precision, yet existing approaches often treat teleoperation and autonomy as separate control modes. This paper presents a human-in-the-loop control paradigm that enables structured transitions among VR-guided teleoperation, semi-autonomous shared control, and rule-based autonomous execution for contact-rich dual-arm construction tasks. The proposed system combines immersive VR guidance, a manually defined library of reusable skill primitives, and a shared-autonomy framework with explicit human-robot role allocation and command-priority rules. This integration allows operators to retain supervisory and corrective authority while delegating repetitive and precision-critical actions to the robot. The paradigm is validated on a dual-arm platform through representative facade-installation tasks. Results show that autonomous execution provides the best performance under well-calibrated nominal conditions, whereas semi-autonomous control improves resilience when environmental disturbances exceed the predefined autonomous pipeline's correction capability. Semi-autonomous control also substantially reduces subjective operator workload compared with full teleoperation. These findings demonstrate that effective construction-robot control should adapt human involvement to task and environmental uncertainty, using autonomy for repeatable operations and shared control for disturbance recovery.

</details>

---

### [[20_Research/Papers/强化学习/RedirectMimic_Local_Motion_Content_Redaction_for_Humanoid_Whole-Body_Control|RedirectMimic: Local Motion Content Redaction for Humanoid Whole-Body Control]]

![[assets/2611.14049_figure.png|800]]

- **arXiv**: [2611.14049](https://arxiv.org/abs/2611.14049)
- **PDF**: https://arxiv.org/pdf/2611.14049
- **详细分析**: [[20_Research/Papers/强化学习/RedirectMimic_Local_Motion_Content_Redaction_for_Humanoid_Whole-Body_Control|RedirectMimic: Local Motion Content Redaction for Humanoid Whole-Body Control]]
- **作者**: Zepeng Wang, Xiaochuan Shi
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: RL

#### 研究背景与动机

《RedirectMimic: Local Motion Content Redaction for Humanoid Whole-Body Control》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid motion interfaces should accommodate application-specific movement constraints while retaining useful reference behavior. Local content redaction requires a controller to replace selected movements even when it continues to receive the original reference. Removing the tracking incentive for those movements leaves their replacement unspecified. We introduce RedirectMimic, which separates the reference observed by the actor from the target used to train its execution. A rule-generated edited reference guides tracking rewards during proximal policy optimization, while the deployed observation and action interfaces remain unchanged. We evaluate pose- and speed-defined arm editing in Unitree G1 simulation using a tracker pretrained on 7,509 motion clips. On the overhead-arm task, RedirectMimic reduces core-window content occurrence to 2.7%, compared with 58.9% for reward zeroing and 32.8% for anti-tracking. It achieves 94.2% core-window joint success, combining content suppression, fall-free execution, and local retention. On the speed-defined task, fast outward arm movements occurred at similarly low rates under all three local editing methods. Across both tasks, RedirectMimic achieved the lowest replacement error among these methods and tracked unedited motions with accuracy comparable to that of the pretrained controller. Project page: https://xiaopeng-whu.github.io/RedirectMimic/.

</details>

---

### [[20_Research/Papers/具身智能/LaST0.5_A_Generalist_World_Action_Model_with_Interaction-Centric_Latent_Reasoning|LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning]]

![[assets/2611.14048_figure.png|800]]

- **arXiv**: [2611.14048](https://arxiv.org/abs/2611.14048)
- **PDF**: https://arxiv.org/pdf/2611.14048
- **详细分析**: [[20_Research/Papers/具身智能/LaST0.5_A_Generalist_World_Action_Model_with_Interaction-Centric_Latent_Reasoning|LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning]]
- **作者**: Xuheng Zhang, Yiming Zhang, Jialin Gao, Hao Chen, Jiaming Liu, Ji Li, Runzhong Huang, Yinxi Wang, Chenyang Gu, Zihan Yang, Yaowei Liu, Zhonghao Yan...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 世界模型
- **相关性评分**: 1.8（加权：具身智能 0.9，世界模型 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《LaST0.5: A Generalist World Action Model with Interaction-Centric Latent Reasoning》归入 具身智能、机器人、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：RLBench, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

World Action Models (WAMs) have recently emerged as a promising paradigm for robotic manipulation, endowing policies with strong capabilities for modeling temporal and physical dynamics. Existing WAMs, encompassing both video-first action prediction and joint video-action modeling, directly transfer global physical representations from world models to action generation. However, global scene representations may underemphasize local robot-object interactions, creating a mismatch between representations optimized for world evolution and those required for manipulation. To bridge this gap, we propose LaST0.5, a novel WAM that introduces an interaction-centric physical representation between world modeling and action generation. Specifically, LaST0.5 learns a compact interaction-centric latent space under the supervision of visual interaction cues between the robot and the environment. This reasoning space is instantiated as a latent expert that bridges the world expert and the action expert within a Mixture-of-Transformers architecture. Furthermore, LaST0.5 performs adaptive world-to-action transfer by jointly predicting future representations and progress values, using progress consistency to adjust action execution and trigger future resampling. Finally, we pretrain LaST0.5 on a large-scale robotic data corpus comprising over 14k hours of data, establishing interaction-centric physical reasoning as a scalable and effective paradigm. LaST0.5 achieves 99.5% on LIBERO, surpasses the previous state of the art on ten evaluated RLBench tasks, and demonstrates robust long-horizon execution and precise dexterous manipulation in real-world experiments.

</details>

---

### [[20_Research/Papers/机器人/Optimization-Based_Path_Planning_for_Industrial_Manipulators_Experimental_Validation_in_Additive_Manufacturing|Optimization-Based Path Planning for Industrial Manipulators: Experimental Validation in Additive Manufacturing]]

![[assets/2611.13983_figure.jpg|800]]

- **arXiv**: [2611.13983](https://arxiv.org/abs/2611.13983)
- **PDF**: https://arxiv.org/pdf/2611.13983
- **详细分析**: [[20_Research/Papers/机器人/Optimization-Based_Path_Planning_for_Industrial_Manipulators_Experimental_Validation_in_Additive_Manufacturing|Optimization-Based Path Planning for Industrial Manipulators: Experimental Validation in Additive Manufacturing]]
- **作者**: Shiva Ganesh Murali, Valentin Bhend, Deepak Ingole, Gabriele Fadini, Alisa Rupenyan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, ComputerVision

#### 研究背景与动机

《Optimization-Based Path Planning for Industrial Manipulators: Experimental Validation in Additive Manufacturing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic additive manufacturing requires joint paths that reconcile robot feasibility with process-specific geometry. We develop an offline optimization-based path planner that combines joint-path regularity and self-collision penalties with process costs and constraints, so that a new process enters through its own reference, residuals, and tolerances. Full-path and boundary-coupled chunked optimization handle references of different lengths. Iterative Weight Tuning (IWT) determines the cost weights from the gaps between Key Performance Indicators (KPIs) and their targets. In carbon-fiber winding and robotic 3D printing, the planned paths meet the geometric tolerances and all KPI targets, and both paths are executed on a UR10e, without extrusion for printing, with joint-level tracking recorded during execution.

</details>

---

### [[20_Research/Papers/具身智能/ReACT_Reflection-Consistent_Modulation_and_Cross-Load_Consistency_for_Humanoid_Velocity_Tracking_Under_Asymmetric_Loads|ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads]]

![[assets/2611.13929_figure.png|800]]

- **arXiv**: [2611.13929](https://arxiv.org/abs/2611.13929)
- **PDF**: https://arxiv.org/pdf/2611.13929
- **详细分析**: [[20_Research/Papers/具身智能/ReACT_Reflection-Consistent_Modulation_and_Cross-Load_Consistency_for_Humanoid_Velocity_Tracking_Under_Asymmetric_Loads|ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads]]
- **作者**: Xianghui Wang, Aoran Fu, Liyou Luo, Shanze Wang, Xiaoyu Shen, Dan Zhang, Wei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.4（加权：具身智能 2.1，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《ReACT: Reflection-Consistent Modulation and Cross-Load Consistency for Humanoid Velocity Tracking Under Asymmetric Loads》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MOB-Net, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In recent years, humanoid loco-manipulation has progressed to whole-body grasping, lifting, and transport. A basic requirement underlying these tasks is carrying the object to its destination, which depends on the locomotion controller accurately executing velocity commands from the navigation policy. However, carrying an object in one hand introduces a persistent asymmetric upper-body load that can degrade velocity tracking. Persistent tracking biases can accumulate into position and heading deviations, increasing the risk of collisions and navigation failure. To address this problem, we present ReACT, a framework for accurate velocity tracking under asymmetric upper-body loads. Reflection-consistent disturbance modulation uses the estimated wrench to modulate actor features for load compensation while preserving action correspondence under reflected observations. Cross-load tracking consistency training compares loaded and unloaded conditions under the same velocity commands to promote consistent velocity tracking across loading conditions. Simulation experiments on a Unitree G1 humanoid robot show improved velocity tracking and reduced directional bias under varying asymmetric loads. Real-world experiments demonstrate collision-free goal reaching in all 40 tested navigation trials under unilateral hand loads with a fixed mapless navigation policy.

</details>

---

### [[20_Research/Papers/机器人/Learn-To-Propagate_Distributionally_Robust_Motion_Planning_for_Nonlinear_Uncertain_Systems|Learn-To-Propagate: Distributionally Robust Motion Planning for Nonlinear Uncertain Systems]]

![[assets/2611.13863_first_page.png|800]]

- **arXiv**: [2611.13863](https://arxiv.org/abs/2611.13863)
- **PDF**: https://arxiv.org/pdf/2611.13863
- **详细分析**: [[20_Research/Papers/机器人/Learn-To-Propagate_Distributionally_Robust_Motion_Planning_for_Nonlinear_Uncertain_Systems|Learn-To-Propagate: Distributionally Robust Motion Planning for Nonlinear Uncertain Systems]]
- **作者**: Eduardo Figueiredo, Adrien Banse, Qi Heng Ho, Raphael Jungers, Morteza Lahijanian, Luca Laurenti
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Learn-To-Propagate: Distributionally Robust Motion Planning for Nonlinear Uncertain Systems》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：LearnAmbiguitySet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion planning for stochastic systems aims to find a sequence of control inputs that drives a system to a goal set while avoiding unsafe states with high probability. Existing approaches, however, are either restricted to linear dynamics with perfect knowledge of the underlying distributions or lack formal correctness guarantees. To address these limitations, we propose \emph{Learn-To-Propagate Distributionally-Robust Forest (L2P-DR-Forest)}, a distributionally-robust sampling-based planning algorithm for \emph{nonlinear} stochastic systems with \emph{unknown} initial state and process noise distributions. Our approach leverages recent advances in optimal transport to learn ambiguity sets that contain the true system distributions with high confidence. We develop an efficient method for propagating these sets through the system dynamics and for verifying their safety. We then integrate these techniques into a novel sampling-based planning algorithm to grow a forest of search trees in the system's state space while accounting for and mitigating the growth of ambiguity-sets radii. We prove that the algorithm is correct, i.e., every returned plan satisfies the specifications with the prescribed confidence, and, under some feasibility and distributional assumptions, is probabilistically complete. Evaluations on several robotic benchmarks demonstrate that our algorithm significantly outperforms existing methods while providing formal guarantees with high confidence.

</details>

---

### [[20_Research/Papers/具身智能/Game-Enhanced_Embodied_Learning_with_Event_and_Foresight_Pretraining|Game-Enhanced Embodied Learning with Event and Foresight Pretraining]]

![[assets/2611.13819_figure.png|800]]

- **arXiv**: [2611.13819](https://arxiv.org/abs/2611.13819)
- **PDF**: https://arxiv.org/pdf/2611.13819
- **详细分析**: [[20_Research/Papers/具身智能/Game-Enhanced_Embodied_Learning_with_Event_and_Foresight_Pretraining|Game-Enhanced Embodied Learning with Event and Foresight Pretraining]]
- **作者**: Lianlei Shan, Han Jin, Yaunchao Ma, Xinpeng Chen, Linhao Zhou, Xin Bin
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Game-Enhanced Embodied Learning with Event and Foresight Pretraining》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：InternVLA, OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human gameplay supplies paired observations, actions, and visual consequences that can supplement robot-policy training. We study event-and-foresight pretraining for InternVLA-A1.5, combining recorded keyboard/mouse event prediction with history-conditioned visual supervision through a frozen video model. Coverage-preserving anchor selection constructs one-second targets, and an attention mask prevents teacher-forced future actions from entering foresight queries. The selected corpus contains 394 recordings across 20 games, with 223.36 hours of recorded timestamp span and 2,072,084 training anchors. After 12,400 game-pretraining updates, we compare the resulting initialization with the public base under the same suite-specific robot fine-tuning protocol. Across four LIBERO suites, aggregate success increases from 1,718/2,000 (85.90%) to 1,811/2,000 (90.55%), a gain of 4.65 percentage points. Suite gains are 9.2, 6.8, 0.2, and 2.4 points on Spatial, Object, Goal, and Long. The 40-task breakdown shows 24 improvements, 10 declines, and six ties. These results support the practical value of the complete game-pretraining stage in this evaluated setting, while revealing heterogeneous task outcomes. The comparison includes additional optimization and does not isolate the effects of game data, the two objectives, or training variability.

</details>

---

### [[20_Research/Papers/强化学习/Camera_equalisation_of_an_11.5x_drop_in_environmental_illuminance_four_imitation-learning_policies_on_an_SO-101_arm|Camera equalisation of an 11.5x drop in environmental illuminance: four imitation-learning policies on an SO-101 arm]]

![[assets/2611.13810_figure.jpg|800]]

- **arXiv**: [2611.13810](https://arxiv.org/abs/2611.13810)
- **PDF**: https://arxiv.org/pdf/2611.13810
- **详细分析**: [[20_Research/Papers/强化学习/Camera_equalisation_of_an_11.5x_drop_in_environmental_illuminance_four_imitation-learning_policies_on_an_SO-101_arm|Camera equalisation of an 11.5x drop in environmental illuminance: four imitation-learning policies on an SO-101 arm]]
- **作者**: Simon Cowling
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Camera equalisation of an 11.5x drop in environmental illuminance: four imitation-learning policies on an SO-101 arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：ImageNet, ResNet, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Real-robot benchmarks of learned visuomotor policies often record room illuminance as the lighting condition. We show that, on a typical low-cost rig, room light and image light can be almost unrelated. Four imitation-learning policies (ACT, SmolVLA, Diffusion Policy and pi0.5) were trained on the same 50 demonstrations of a pick-and-place task on an SO-101 arm. Each was run for ten rollouts at about 520 lux and again at about 45 lux, an 11.5x reduction. Success was 20/40 in normal light and 19/40 in low light: a change of -2.5 percentage points (95% CI -23 to +19), with no evidence that the policies differed in sensitivity (interaction p = 0.86). The recorded video shows why: mean image brightness was only 3% lower in low light on the front camera and 19% lower on the wrist camera. Both cameras were set to automatic exposure and white balance, which most likely absorbed the difference; exposure was not locked in this experiment. An accidental repeat of one 10-rollout block reproduced its success count (7/10) but matched the first block at only 6 of 10 placements, consistent with chance. We conclude that lux alone does not describe what a policy sees. Camera settings, and image statistics compared with the training recordings, are the quantities to report and control. Data and code are public.

</details>

---

### [[20_Research/Papers/强化学习/CIALLO_Learning_Shared_Intent_Representations_for_Cross-Embodiment_Manipulation|CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation]]

![[assets/2611.13732_figure.png|800]]

- **arXiv**: [2611.13732](https://arxiv.org/abs/2611.13732)
- **PDF**: https://arxiv.org/pdf/2611.13732
- **详细分析**: [[20_Research/Papers/强化学习/CIALLO_Learning_Shared_Intent_Representations_for_Cross-Embodiment_Manipulation|CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation]]
- **作者**: Choo Sin Wai, Dake Zhong, Jingye Zhang, Zhifang Liu, Siyao Xiao, Zirong Ding, Yuhong Zhang, Kangjie Chen, Dongbin Zhang, Guorui Song, Guocun Wang, Peng Jiao...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《CIALLO: Learning Shared Intent Representations for Cross-Embodiment Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：JEPA-VLA, StarVLA, TinyVLA, UniVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot demonstrations contain reusable manipulation knowledge, but transferring this knowledge across embodiments requires representations that bridge differences in control interfaces. Action reconstruction alone does not ensure that similar behaviors across robots share a representation. To address this gap, we introduce CIALLO, an action codec that aligns actions, visual changes, and observation-grounded language in a shared space of short-horizon behavioral intent. An embodiment-conditioned decoder maps this intent back to robot-specific actions, allowing a shared representation to support different control interfaces. After pretraining on eight embodiments, CIALLO adapts to a new robot from one recording of at most 10 seconds by updating only its embodiment embeddings. The calibrated codec then remains frozen while a policy learns to predict intent from observations and instructions. We instantiate this policy with Qwen3.5-4B to form Qwen-CIALLO, whose backbone requires no large-scale robot-action pretraining before policy finetuning. With 20 demonstrations per task, Qwen-CIALLO achieves 76.7\% average success across real SO-101 and single-arm Piper robots, compared with 70.0\% for fully finetuned $π_0$. In simulation, we additionally finetune the action decoder, achieving 97.3\% success on LIBERO and 52.7\% on RoboTwin 2.0. The LIBERO policy also achieves 80.8\% on LIBERO-Plus without further finetuning. Together, these results support a shared action codec as a transferable control interface that separates embodiment calibration from task learning.

</details>

---

### [[20_Research/Papers/具身智能/From_Egocentric_Human_Video_to_Robot_Manipulation_in_the_Era_of_Embodied_Intelligence|From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence]]

![[assets/2611.13610_figure.png|800]]

- **arXiv**: [2611.13610](https://arxiv.org/abs/2611.13610)
- **PDF**: https://arxiv.org/pdf/2611.13610
- **详细分析**: [[20_Research/Papers/具身智能/From_Egocentric_Human_Video_to_Robot_Manipulation_in_the_Era_of_Embodied_Intelligence|From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence]]
- **作者**: Yi Wang, Jingqiu Wu, Lei Yao, Zhaoshuo Li, Haoyu Zhu, Yirui Zhou, Huaiyuan Xu, Ying Zheng, Chuang Yang, Lap-Pui Chau
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.6（加权：具身智能 2.4，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《From Egocentric Human Video to Robot Manipulation in the Era of Embodied Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Egocentric human video (EHV) records close-range hand-object interaction (HOI) and the temporal structure of everyday activities, offering a potentially scalable source of experience for robot manipulation. Using this experience for robot control requires recovering useful supervision without recorded robot actions and accounting for differences in morphology, viewpoint, and action space. We define Ego2Robot learning as the process of learning or adapting robot manipulation policies from EHV, organized into four learning paradigms: explicit embodiment transfer, explicit action and task supervision, egocentric video representation pretraining, and latent action and dynamics modeling. The four paradigms differ in what they derive from human video: robot-format demonstrations, interpretable supervision, visual representations, or predictive models of actions and dynamics. For each paradigm, we trace what EHV information is extracted, how robot policies use it, and when the additional data is required. Besides, we review the benchmark datasets that cover EHV, robot demonstrations, and synthetic and simulated resources. This paper links EHV data's contribution to the task information preserved and the robot-specific grounding used during training or deployment. Finally, we identify challenges in physical feasibility, agent coordination, in-context adaptation, controlled evaluation, and predictive control.

</details>

---

### [[20_Research/Papers/世界模型/Few-Shot_Residual_Adaptation_of_Pretrained_Latent_World_Models|Few-Shot Residual Adaptation of Pretrained Latent World Models]]

![[assets/2611.13592_figure.png|800]]

- **arXiv**: [2611.13592](https://arxiv.org/abs/2611.13592)
- **PDF**: https://arxiv.org/pdf/2611.13592
- **详细分析**: [[20_Research/Papers/世界模型/Few-Shot_Residual_Adaptation_of_Pretrained_Latent_World_Models|Few-Shot Residual Adaptation of Pretrained Latent World Models]]
- **作者**: Jakub Suliga, Pankhuri Vanjani, Nisarga Nilavadi, Wolfram Burgard, Rudolf Lioutikov
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, WorldModel

#### 研究背景与动机

《Few-Shot Residual Adaptation of Pretrained Latent World Models》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Pretrained latent world models can support visual planning and control, but their predictions may fail when physical dynamics change at deployment. We study whether such models can adapt from only a few interactions without modifying their pretrained weights or identifying the changed physical parameters. We introduce a few-shot residual adaptation approach that learns self-supervised corrections from latent prediction errors. The corrections are applied both inside the latent predictor and directly to its predicted latent state, while the pretrained world model remains frozen. We evaluate the approach in simulation and on a real robot under center-of-mass and friction shifts. These changes reduce the success of the frozen model to near zero. Using three interaction episodes for adaptation, our dual-site approach recovers 90\% success under the center-of-mass shift and 100\% under the modified friction on the real robot. Ablations show that correcting both locations outperforms single-site adaptation. Our diagnostics further suggest that much of the learned correction reduces a general prediction mismatch, while successful control also depends on shift-specific information captured during adaptation.

</details>

---

### [[20_Research/Papers/具身智能/DeRep_Learning_Depth_Representations_for_End-to-End_Navigation_in_Cluttered_Environments|DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments]]

![[assets/2611.13499_figure.jpeg|800]]

- **arXiv**: [2611.13499](https://arxiv.org/abs/2611.13499)
- **PDF**: https://arxiv.org/pdf/2611.13499
- **详细分析**: [[20_Research/Papers/具身智能/DeRep_Learning_Depth_Representations_for_End-to-End_Navigation_in_Cluttered_Environments|DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments]]
- **作者**: Hanyu Jin, Kenji Shimada
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.1（加权：具身智能 0.6，强化学习 0.2，机器人 0.3）
- **关联关键词**: EmbodiedAI, RL

#### 研究背景与动机

《DeRep: Learning Depth Representations for End-to-End Navigation in Cluttered Environments》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MAVRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

End-to-end navigation in cluttered environments relies on compact visual representations to support collision avoidance and goal-directed motion. Existing methods typically learn these representations jointly with the policy or through observation reconstruction, which does not explicitly specify what information the representation should preserve. Moreover, they are usually evaluated with a single downstream policy learner, although the benefit of a representation may depend on how the policy is learned. It therefore remains unclear how different representation-learning objectives affect downstream navigation performance and robustness. This work proposes DeRep, a navigation-oriented representation-learning method that combines local bird's-eye-view reachability supervision with depth reconstruction. To compare representation objectives under controlled conditions, we pretrain encoders with a common architecture and freeze them during downstream learning. We evaluate the representations using a linear policy probe, flow-matching imitation learning, and reinforcement learning with PPO. DeRep achieves the lowest linear policy probe prediction error and outperforms reconstruction alone across all six tested PPO conditions. In imitation learning, both reachability-based objectives achieve higher mean success rates than reconstruction alone, with similar mean success rates between the reachability-only and joint objectives. These results demonstrate consistent benefits of incorporating reachability supervision into depth representation pretraining across different downstream learning methods and evaluation conditions. We further deploy the PPO policy with the frozen DeRep encoder in Gazebo and on a physical quadrotor without fine-tuning, demonstrating its capability for zero-shot sim-to-sim and sim-to-real transfer.

</details>

---

### [[20_Research/Papers/强化学习/ExRL_Sample-Efficient_Online_Adaptation_of_Long-Chunk_Policies_via_Execution_Length_Control|ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control]]

![[assets/2611.13482_figure.png|800]]

- **arXiv**: [2611.13482](https://arxiv.org/abs/2611.13482)
- **PDF**: https://arxiv.org/pdf/2611.13482
- **详细分析**: [[20_Research/Papers/强化学习/ExRL_Sample-Efficient_Online_Adaptation_of_Long-Chunk_Policies_via_Execution_Length_Control|ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control]]
- **作者**: Xu Luo, Jiaying Yang, Hao Wu, Junlin Xie, Zijin Hong, Ji Zhang, Lianli Gao, Jingkuan Song
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.2（加权：具身智能 0.3，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《ExRL: Sample-Efficient Online Adaptation of Long-Chunk Policies via Execution Length Control》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DSRL, ExRL, PA-RL, Real-World, TempoRL, ZPRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Predicting long action chunks, often spanning dozens of timesteps, has become a key ingredient in increasingly capable robot policies. In this paper, we find that adapting these long-chunk policies with existing reinforcement learning (RL) methods can require many online samples due to the high dimensionality of the action chunks being optimized, making such adaptation impractical in real-world scenarios where interaction data are costly to collect. Our key insight is to shift adaptation from optimizing actions to optimizing how long to execute each predicted action chunk. This keeps the adaptation space low-dimensional while its expressivity grows with the chunk size. We thus introduce Execution at the Right Length (ExRL), a simple approach which augments the base policy with a lightweight adapter that predicts the execution length of each chunk and is trained using off-policy RL algorithms. Across simulation benchmarks and real-world robotic tasks, ExRL enables sample-efficient adaptation of a diverse range of long-chunk policies with minimal task-specific hyperparameter tuning.

</details>

---

### [[20_Research/Papers/机器人/Rhythmic-Semantic_Co-Speech_Gestures_for_Emotional_Dialogue_in_Robots|Rhythmic-Semantic Co-Speech Gestures for Emotional Dialogue in Robots]]

![[assets/2611.13472_figure.png|800]]

- **arXiv**: [2611.13472](https://arxiv.org/abs/2611.13472)
- **PDF**: https://arxiv.org/pdf/2611.13472
- **详细分析**: [[20_Research/Papers/机器人/Rhythmic-Semantic_Co-Speech_Gestures_for_Emotional_Dialogue_in_Robots|Rhythmic-Semantic Co-Speech Gestures for Emotional Dialogue in Robots]]
- **作者**: Christian Arzate Cruz, Edwin C. Montiel-Vázquez, Stefanos Gkikas, Miguel Mejia Tobar, Randy Gomez
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Rhythmic-Semantic Co-Speech Gestures for Emotional Dialogue in Robots》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Co-speech gestures can increase engagement and improve speech understanding. Yet, most data-driven robot systems generate either rhythmic beat-like motion or semantically meaningful iconic gestures, but not both. We present an emotion-aware rhythmic-semantic co-speech gesture system that generates iconic and beat behaviors in real time from text and the robot's internal emotional state. We formalize the task of beat-iconic gesture generation using emotion and propose lightweight models that predict iconic timing and intensity, then fill the remaining spans with emotion-conditioned beats at an appropriate intensity level. We train on the BEAT2 dataset and deploy the system on the social robot Haru. In an online user study with 60 participants, our method shows stronger speech-gesture alignment and is preferred over baseline methods.

</details>

---

### [[20_Research/Papers/机器人/AHEADance_Anticipatory_Humanoid_Dance_from_Streaming_Audio|AHEADance: Anticipatory Humanoid Dance from Streaming Audio]]

![[assets/2611.13370_figure.png|800]]

- **arXiv**: [2611.13370](https://arxiv.org/abs/2611.13370)
- **PDF**: https://arxiv.org/pdf/2611.13370
- **详细分析**: [[20_Research/Papers/机器人/AHEADance_Anticipatory_Humanoid_Dance_from_Streaming_Audio|AHEADance: Anticipatory Humanoid Dance from Streaming Audio]]
- **作者**: Tianhu Peng, Yukun Wang, Lingfan Bao, Yiyang Jia, Chengxu Zhou
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《AHEADance: Anticipatory Humanoid Dance from Streaming Audio》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SoulNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

A humanoid that dances to streamed music must commit each motion chunk before it has heard the music that chunk accompanies, and must continue from motion it has already committed. We present AHEADance, a robot-native streaming dance generator executed on a humanoid robot by a whole-body tracker. ListenAhead conditions each chunk on heard music and a frozen music model's forecasts of the coming music, aligned to their target times and weighted by reliability. The forecasts carry the timing of upcoming beats almost as well as the actual future; with them, the generator is better synchronized with the music and concentrates more motion energy at its song's beat frequency. Commit Forcing trains continuation from the model's own committed chunks, updating both the latent history and the decoded boundary of the next chunk; it reduces low activity from 83.5% to 10.3%, the level of real dance. Three music evaluators, each validated on real G1 dance, test synchronization, song and style. On a physical Unitree G1, it dances while the music plays and comes to rest when it stops, without a fall. Project page: https://ihcr.github.io/AHEADance

</details>

---

### [[20_Research/Papers/具身智能/PneuGen_Task-Driven_Agentic_Co-Design_of_Soft_Pneumatic_Robots|PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots]]

![[assets/2611.13344_figure.png|800]]

- **arXiv**: [2611.13344](https://arxiv.org/abs/2611.13344)
- **PDF**: https://arxiv.org/pdf/2611.13344
- **详细分析**: [[20_Research/Papers/具身智能/PneuGen_Task-Driven_Agentic_Co-Design_of_Soft_Pneumatic_Robots|PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots]]
- **作者**: Shaohong Zhong, Marco Pontin, Perla Maiolino
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.6，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《PneuGen: Task-Driven Agentic Co-Design of Soft Pneumatic Robots》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task-driven design of soft robots requires the consideration of factors such as geometry, morphology, material properties, and actuation, resulting in a large and complex design space that is challenging to explore. Computational optimisation methods leverage signals from simulation to iteratively improve designs to achieve task objectives. However, these methods typically demand high computational load for both optimisation and simulation. We present PneuGen, an agentic co-design framework for soft robots that leverages Large Language Model (LLM) agents to search over the soft robot design space efficiently. A designer agent proposes design programs from a parametric component library, and a separate critic agent analyses simulation diagnostics and recommends targeted revisions. Fitted module response models provide reusable physical priors relating geometry and pressure to deformation. Design programs are automatically validated and converted into finite-element simulations, enabling iterative evaluation. Across grasping tasks on primitive shapes and challenging objects, as well as shape-matching tasks that require multi-directional planar and 3D deformation, the proposed framework significantly outperforms prior computational optimisation baselines. Ablation experiments also highlight the utility of the critic agent and the module response model in facilitating efficient design. We additionally demonstrate the agent-generated soft robot designs in real-world shape-matching and grasping tasks.

</details>

---

### [[20_Research/Papers/大模型/Large_Language_Model_Explainability_for_Planning_Lunar_Rover_Trajectories_under_Uncertainty|Large Language Model Explainability for Planning Lunar Rover Trajectories under Uncertainty]]

![[assets/2611.13292_figure.png|800]]

- **arXiv**: [2611.13292](https://arxiv.org/abs/2611.13292)
- **PDF**: https://arxiv.org/pdf/2611.13292
- **详细分析**: [[20_Research/Papers/大模型/Large_Language_Model_Explainability_for_Planning_Lunar_Rover_Trajectories_under_Uncertainty|Large Language Model Explainability for Planning Lunar Rover Trajectories under Uncertainty]]
- **作者**: Michelle Ho, Maximilian Adang, Zachary Booth, David E. Astle, Margaret Hansen, Edward Balaban, Mykel J. Kochenderfer
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型
- **相关性评分**: 1.0（加权：大模型 1）
- **关联关键词**: LLM, Agent, Systems

#### 研究背景与动机

《Large Language Model Explainability for Planning Lunar Rover Trajectories under Uncertainty》归入 大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning planetary rover trajectories under probabilistic uncertainty is a multi-objective optimization problem that science teams currently iteratively solve and verify by hand. This process becomes impractical when timelines and constraints frequently shift throughout the mission planning phase. Sampling-based planners such as Monte Carlo tree search can speed up this process, but their outputs do not preserve traceability to the science objectives that justify each plan, which the science team needs to verify. We propose an interactive assistant based on a large language model (LLM) that can explain planner trajectories using domain vocabulary and re-run the planner under user-specified conditions to compare alternatives. Previous work has used LLMs inside planner decision-making loops, but we explore using them for post-planning explanation, where they are more likely to be trusted since they do not directly influence planner decisions. Our framework pairs a simulator inspired by the NASA Volatiles Investigating Polar Exploration Rover (VIPER) mission with a ReAct queryable interface that calls curated action tools and retrieval functions. We evaluate the assistant on a query bank consisting of plan comparisons, feasibility, and lookup queries. Experiments show that 90.9% of the assistant's responses are faithful to the planner's outputs, a nearly 65% improvement over zero-shot prompting of the same LLM without tool access, demonstrating the potential for trustworthy explainability of uncertainty-aware traverses with an LLM-based system.

</details>

---

### [[20_Research/Papers/机器人/Force-Closure_Condition_for_Cooperative_Multi-robot_Pushing_of_Rectangular_Objects|Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects]]

![[assets/2611.13268_figure.png|800]]

- **arXiv**: [2611.13268](https://arxiv.org/abs/2611.13268)
- **PDF**: https://arxiv.org/pdf/2611.13268
- **详细分析**: [[20_Research/Papers/机器人/Force-Closure_Condition_for_Cooperative_Multi-robot_Pushing_of_Rectangular_Objects|Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects]]
- **作者**: Duy Anh Nguyen, Trung Dung Ngo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.1，机器人 0.9）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Force-Closure Condition for Cooperative Multi-robot Pushing of Rectangular Objects》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In cooperative object manipulation, the placement of pushing contacts determines whether force closure can be achieved and agents can generate arbitrary forces and torques on the object correspondingly. This study derives a necessary and sufficient closed-form condition for the planar force closure of a rectangular object, a common object shape in everyday settings, under four frictionless pushing contacts. For a rectangle of length $b$ and width $a$, force closure holds if and only if $(l_1+l_3-b)(l_2+l_4-a)&lt;0$, where $l_1,l_2,l_3,l_4$ are the four edge contact locations. This condition is independent of the object's center of mass and is used to verify contact configurations before contact force allocation. When the condition is not satisfied, the signs of the two factors indicate which opposing contact pair should be adjusted. The condition and adjustment rule are then integrated into a full-pose trajectory-tracking framework as a geometric feasibility layer to demonstrate their use in control. Static wrench feasibility tests validate the proposed condition, while narrow-passage floating-body simulations show that maintaining a force-closure configuration reduces the RMS tracking errors in $x$, $y$, and unwrapped yaw from $12.05$ m, $18.11$ m, and $535.96^\circ$ to $2.24$ m, $2.66$ m, and $2.69^\circ$, respectively.

</details>

---

### [[20_Research/Papers/世界模型/Incorporating_World_Models_in_Decision_Making_for_Next_Best_View_Selection_in_Active_Sensing|Incorporating World Models in Decision Making for Next Best View Selection in Active Sensing]]

![[assets/2611.13229_figure.png|800]]

- **arXiv**: [2611.13229](https://arxiv.org/abs/2611.13229)
- **PDF**: https://arxiv.org/pdf/2611.13229
- **详细分析**: [[20_Research/Papers/世界模型/Incorporating_World_Models_in_Decision_Making_for_Next_Best_View_Selection_in_Active_Sensing|Incorporating World Models in Decision Making for Next Best View Selection in Active Sensing]]
- **作者**: Nikita Sarawgi, Omey M. Manyar, Satyandra K. Gupta
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 0.8，机器人 0.7）
- **关联关键词**: Robotics, ComputerVision, Systems

#### 研究背景与动机

《Incorporating World Models in Decision Making for Next Best View Selection in Active Sensing》归入 世界模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Efficient robotic 3D reconstruction requires selecting views that contribute new surface measurements with few physical captures. Pretrained world models can guide this choice, but a predicted surface may not produce valid depth measurements under the operating conditions of the deployed sensor. We present a deployment adaptation methodology for next-best-view selection that learns a sensor-return adapter from limited local calibration data while keeping the pretrained predictor fixed. The adapter estimates measurement dropout over each predicted surface, allowing the selection method to favor views likely to fill gaps in the measured reconstruction. In a real-robot experiment with a structured-light sensor, the adapted method achieves higher measured surface coverage with 60% fewer captures than nominal selection. The adapted method recovers a surface region that the nominal method repeatedly targets but fails to measure. These results suggest that robots can reuse pretrained predictive models while adapting their decisions to local operating conditions in data-scarce environments.

</details>

---

### [[20_Research/Papers/世界模型/Ground_Reaction_Force-Aware_Model_Predictive_Control_for_Underactuated_Upright_Physical_Assistance|Ground Reaction Force-Aware Model Predictive Control for Underactuated Upright Physical Assistance]]

![[assets/2611.13204_figure.png|800]]

- **arXiv**: [2611.13204](https://arxiv.org/abs/2611.13204)
- **PDF**: https://arxiv.org/pdf/2611.13204
- **详细分析**: [[20_Research/Papers/世界模型/Ground_Reaction_Force-Aware_Model_Predictive_Control_for_Underactuated_Upright_Physical_Assistance|Ground Reaction Force-Aware Model Predictive Control for Underactuated Upright Physical Assistance]]
- **作者**: Darren Biskup, Jeonghan Yu, Zibo Yu, Sunil K. Agrawal
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.0（加权：具身智能 0.3，世界模型 0.2，机器人 0.5）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《Ground Reaction Force-Aware Model Predictive Control for Underactuated Upright Physical Assistance》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many rehabilitation robots execute prescribed motions using reactive tracking controllers that do not explicitly incorporate the user's instantaneous human-ground interaction. This paper presents Ground Reaction Force-Aware Model Predictive Control (GRF-MPC), a framework for upright physical assistance. By integrating live GRF and center of pressure (CoP) measurements directly into a human centroidal dynamics model, GRF-MPC formulates a real-time quadratic program (QP) that optimizes assistive forces and moments over a receding horizon. We deployed GRF-MPC on the Robotic Upright Stand Trainer (RobUST) in an underactuated 4-cable configuration and evaluated it against a fully actuated 8-cable Cartesian impedance baseline in nearly 300 trials across six healthy participants. Across tasks spanning impulsive perturbations, lunge trajectories, and voluntary limits of stability, GRF-MPC reduced peak planar center-of-mass (CoM) error by 19.6% during perturbations, lowered trajectory tracking error by 24.1%, required 28.7% less net mechanical work, and permitted a 45.9% greater normalized voluntary excursion area. The underlying QP solves in under 1 ms, comfortably enabling 100 Hz replanning and demonstrating that incorporating live human-ground interaction into predictive control yields stronger, more transparent physical assistance with half the actuators.

</details>

---

### [[20_Research/Papers/具身智能/Robo-MLT_Dual-System_Robotic_Manipulation_for_Long-Horizon_Medical_Laboratory_Tasks|Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks]]

![[assets/2611.13039_figure.png|800]]

- **arXiv**: [2611.13039](https://arxiv.org/abs/2611.13039)
- **PDF**: https://arxiv.org/pdf/2611.13039
- **详细分析**: [[20_Research/Papers/具身智能/Robo-MLT_Dual-System_Robotic_Manipulation_for_Long-Horizon_Medical_Laboratory_Tasks|Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks]]
- **作者**: Zequan Zeng, Kai Wang, Delvin Ce Zhang, Huaping Liu, Zhipeng Yuan, Junqin Yang, YunLong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.4（加权：具身智能 1.2，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Robo-MLT: Dual-System Robotic Manipulation for Long-Horizon Medical Laboratory Tasks》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, RoboNurse-VLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable medical laboratory automation requires robots to complete entire workflows in protocol order while handling changes during execution. A robot may execute each motion correctly yet fail the workflow by confusing visually similar stages or stalling after human intervention. We present Robo-MLT, a dual-system framework that couples explicit workflow monitoring with learned action generation. A vision--language planner composes an ordered atomic-skill sequence from the protocol and the initial workspace observation. A multiframe execution monitor detects when the active skill has completed or become infeasible, then advances the workflow or triggers replanning. A skill-conditioned vision--language--action policy generates the manipulation trajectories, and an asynchronous runtime coordinates it with the monitor. We evaluate Robo-MLT against four policy baselines and a VLM-based monitor baseline on blood gas analysis and blood sample tube sorting, with 50 nominal configurations per method and 20 sample-removal configurations. Robo-MLT achieves task success rates of 82\% and 70\%, exceeding $π_{0.5}$ by 30 and 22 percentage points, respectively. After an operator removes the sample being handled, the system revises the remaining plan and continues processing the other samples. These results indicate that, under the evaluated conditions, explicit workflow monitoring makes long-horizon laboratory manipulation more reliable and recoverable.

</details>

---

### [[20_Research/Papers/具身智能/RoboACE_Adversarial_Co-Evolution_for_Robot_Self-Improvement|RoboACE: Adversarial Co-Evolution for Robot Self-Improvement]]

![[assets/2611.13034_figure.png|800]]

- **arXiv**: [2611.13034](https://arxiv.org/abs/2611.13034)
- **PDF**: https://arxiv.org/pdf/2611.13034
- **详细分析**: [[20_Research/Papers/具身智能/RoboACE_Adversarial_Co-Evolution_for_Robot_Self-Improvement|RoboACE: Adversarial Co-Evolution for Robot Self-Improvement]]
- **作者**: Delin Zhao, Zhengrong Yue, Junlin He, Yali Wang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.9（加权：具身智能 0.6，大模型 0.2，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《RoboACE: Adversarial Co-Evolution for Robot Self-Improvement》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot agents can improve reusable skills, planning procedures, and recovery strategies from execution feedback, yet a fixed practice source leaves the search for new weaknesses unchanged. Useful practice depends on the agent's current capabilities, so the procedure that chooses practice must also be revisable. We present RoboACE (Robot Adversarial Co-Evolution), a framework that jointly evolves curriculum and execution harnesses around frozen foundation models. The curriculum harness uses accumulated capability evidence to propose informative challenges, while the execution harness responds with reusable revisions that expand execution capabilities. Alternating updates hold one side fixed as the other changes, and admitted challenges form fixed snapshots for comparing execution revisions. Starting from a compact set of LIBERO practice conditions, the resulting frozen deployment outperforms the evaluated controllers and agent systems across four LIBERO-family panels. On LIBERO-PRO, it reaches 74.0% success, exceeding the initial deployment by 15.0 percentage points and direct execution by its VLA controller by 13.5 points. Case studies document changes to evidence-guided practice selection, drawer-skill grounding, and controller intervention.

</details>

---

### [[20_Research/Papers/大模型/CAFE_Closed-Loop_Autonomous_Task_Formulation_and_Execution_without_Instance-Specific_Instructions|CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions]]

![[assets/2611.12983_figure.png|800]]

- **arXiv**: [2611.12983](https://arxiv.org/abs/2611.12983)
- **PDF**: https://arxiv.org/pdf/2611.12983
- **详细分析**: [[20_Research/Papers/大模型/CAFE_Closed-Loop_Autonomous_Task_Formulation_and_Execution_without_Instance-Specific_Instructions|CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions]]
- **作者**: Mingjia Chen, Xuewen Zhao, Philip Dames, Qi Mao, Fei Xie, Jun Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 0.9（加权：具身智能 0.3，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Robotics

#### 研究背景与动机

《CAFE: Closed-Loop Autonomous Task Formulation and Execution without Instance-Specific Instructions》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Scene-driven robot autonomy requires selecting tasks from observations as well as executing them. We study scene-driven task formulation and execution under predefined cleaning, safety, and storage/organization categories, without instance-specific goals or action sequences. CAFE maintains online memory of objects, functional zones, and execution states. A rule-guided Trigger-LLM admits formulation from accumulated evidence; Draft, Complete, and Audit propose goals, resolve execution details, and check dependencies. Outcomes update memory for correction and subsequent discovery. Evaluation in 12 AI2-THOR scenes compares three backbones and task-complexity tiers using coverage, constraint, and execution metrics. Tri-LLM records higher GCR scores than the evaluated baselines across three backbones and task-complexity tiers. Controls examine completion, auditing, zones, feedback, triggering, and prompt examples. LimoCobot traces illustrate storage, cleanup, and recovery from a failed grasp. The study examines how shared scene state connects task discovery to execution and outcome-driven revision.

</details>

---

### [[20_Research/Papers/具身智能/Maze_Runner_Autonomous_Maze_Navigation_with_Line-Based_Localization_and_Control_Barrier_Functions|Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions]]

![[assets/2611.12949_figure.jpg|800]]

- **arXiv**: [2611.12949](https://arxiv.org/abs/2611.12949)
- **PDF**: https://arxiv.org/pdf/2611.12949
- **详细分析**: [[20_Research/Papers/具身智能/Maze_Runner_Autonomous_Maze_Navigation_with_Line-Based_Localization_and_Control_Barrier_Functions|Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions]]
- **作者**: Alvaro J. Gaona, Lucas Gómez-Velayos, Peter Pasuy-Quevedo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Maze Runner: Autonomous Maze Navigation with Line-Based Localization and Control Barrier Functions》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Maze navigation requires localization from sparse, repetitive geometry, planning through narrow corridors, and control that stays safe when the estimate or the map is wrong. We present Maze Runner, an open autonomy stack in C++ and ROS 2 that addresses these needs end to end on a simulated Husarion ROSbot XL with a 2D LiDAR in Gazebo. Perception extracts wall lines from each scan with RANSAC and total least squares, with per-line uncertainty. The same line front end feeds two estimators: an Extended Kalman Filter (EKF) that localizes against a line map built from the maze mesh, and an EKF SLAM variant that builds the line map online. Planning runs online on an inflated occupancy grid with A* plus line-of-sight shortcutting, or with a forward-only Hybrid A*. A nonlinear Model Predictive Controller (NMPC) tracks the plan while discrete-time Control Barrier Functions (CBFs) on world-frame LiDAR points keep the robot clear of walls and unmapped obstacles. The algorithms live in a ROS-free, unit-tested core library, and the whole stack builds and runs from a single reproducible environment. In simulation, the robot drives a 135 m route through the maze with 1.0 cm localization RMSE against the known map and 24 cm in SLAM mode, the planner returns a path in 6 ms, and the NMPC solves in 11.7 ms on average, never exceeding its 80 ms budget.

</details>

---
