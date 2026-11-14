# cs.RO | Robotics | 2026-11-13

#arxiv #ComputerScience

**论文数**: 49

### [[20_Research/Papers/具身智能/HEIR_Harness_Egocentric_Intent_for_Human-Robot_Interactions|HEIR: Harness Egocentric Intent for Human-Robot Interactions]]

![[assets/2611.17238_figure.png|800]]

- **arXiv**: [2611.17238](https://arxiv.org/abs/2611.17238)
- **PDF**: https://arxiv.org/pdf/2611.17238
- **详细分析**: [[20_Research/Papers/具身智能/HEIR_Harness_Egocentric_Intent_for_Human-Robot_Interactions|HEIR: Harness Egocentric Intent for Human-Robot Interactions]]
- **作者**: Yichi Zhang, Bo Wang, Zhenghan Zhu, Yutong Han, Jiayin Zou, Gao Kejun, Chang Liu, Shaoxuan Xie, Chi Zhang, Shi Haoyang, Zongxuan Lai, Sen Cui...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《HEIR: Harness Egocentric Intent for Human-Robot Interactions》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：REI-Bench, RoboVQA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

For robots to assist, serve, and collaborate with humans, they must not only interpret human requests conveyed through language and multimodal intentional cues, but also execute long-horizon tasks that interleave navigation and manipulation. In this paper, we introduce HEIR, a resource for studying how to Harness Egocentric Intent for Human-Robot Interaction. HEIR pairs human speech, measured gaze, and egocentric video with robot observations and teleoperated navigation-manipulation trajectories, while each session preserves successive episodes, with each request fulfilled through multiple execution subtasks. The captured data, together with human-authored annotations, support the study of intent grounding, execution planning, and task completion within a unified interaction setting. To demonstrate the value of HEIR, we conduct extensive offline experiments to evaluate how models benefit from additional human-centric context across these tasks, together with real-robot experiments that assess execution task completion. HEIR thus provides a valuable resource for studying user-centric robot interaction in naturalistic household environments. Our demo and dataset are available online.

</details>

---

### [[20_Research/Papers/机器人/Collaborative_Task_Allocation_for_Heterogeneous_Multi-Robot_Systems_Through_Iterative_Clustering|Collaborative Task Allocation for Heterogeneous Multi-Robot Systems Through Iterative Clustering]]

![[assets/2611.17213_figure.png|800]]

- **arXiv**: [2611.17213](https://arxiv.org/abs/2611.17213)
- **PDF**: https://arxiv.org/pdf/2611.17213
- **详细分析**: [[20_Research/Papers/机器人/Collaborative_Task_Allocation_for_Heterogeneous_Multi-Robot_Systems_Through_Iterative_Clustering|Collaborative Task Allocation for Heterogeneous Multi-Robot Systems Through Iterative Clustering]]
- **作者**: David R. Martin, Brooks A. Butler, Scott Nivison, Magnus Egerstedt, Mohammad Abdullah Al Faruque, Pramod Khargonekar
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Collaborative Task Allocation for Heterogeneous Multi-Robot Systems Through Iterative Clustering》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot systems face the challenge of efficiently allocating teams of heterogeneous robots to tasks. The task allocation problem is complicated by collaborative interactions between robots where teams of robots develop emergent capabilities that enable them to complete tasks that would be inefficient or impossible for individual robots. To address these challenges, we present an iterative clustering algorithm for collaborative task allocation in heterogeneous multi-robot systems. This approach partitions the computationally intractable global optimization problem into smaller, tractable subproblems by iteratively forming clusters of robots and tasks, then optimizing assignments within each cluster. By ensuring robots remain clustered with their currently assigned tasks, we guarantee monotonic improvement in overall utility with each iteration. We analyze the convergence of the algorithm and characterize how cluster size constraints determine which suboptimal assignments could trap the algorithm. In simulation, iterative clustering consistently outperforms simulated annealing, and a group-based auction in both computation time and solution quality, and outperforms a hedonic game approach in solution quality.

</details>

---

### [[20_Research/Papers/具身智能/XBot-Omni_An_Omni-Modal_Model_for_Embodied_Understanding_and_Interaction|XBot-Omni: An Omni-Modal Model for Embodied Understanding and Interaction]]

![[assets/2611.17160_figure.png|800]]

- **arXiv**: [2611.17160](https://arxiv.org/abs/2611.17160)
- **PDF**: https://arxiv.org/pdf/2611.17160
- **详细分析**: [[20_Research/Papers/具身智能/XBot-Omni_An_Omni-Modal_Model_for_Embodied_Understanding_and_Interaction|XBot-Omni: An Omni-Modal Model for Embodied Understanding and Interaction]]
- **作者**: Kerui Gu, Xing Fu, Shuoyang Sun, Cheng Peng, Jingru Duan, Huayu Gu, Zhenyu Chen, Jiaxin Huang, Cheng Wen, Rui Zhen, Kairui Chen, Zhihui Peng...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.3，机器人 0.7）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《XBot-Omni: An Omni-Modal Model for Embodied Understanding and Interaction》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied interaction requires an agent to integrate multimodal perception with verbal and nonverbal behaviors to effectively communicate its intentions, including speech, body motion, and facial expressions. We present XBot-Omni, a Thinker--Talker--Actor architecture that extends the Omni paradigm to robotic modalities, including body motion and facial expressions, with ``X'' representing the extensibility to robotic-specific modalities. The Thinker processes text, images, audio, and video to formulate contextually appropriate responses, which are then realized by the Talker and Actor through speech and coordinated bodily expressions, respectively. In this report, we innovatively introduce the concept of ``Actor'' as a dedicated component for embodied agents: a coordinated, streaming module that leverages the native representations of the Thinker and Talker within an end-to-end pipeline, introducing only modest latency overhead. This unified architecture enables multimodal generation conditioned on omni-modal inputs directly to prevent information loss in staged designs. We comprehensively evaluate XBot-Omni across seven benchmarks, demonstrating strong multimodal understanding capabilities on both general-domain and robot-centric videos, as well as high-quality, natural, and well-coordinated motion generation. Furthermore, our results validate its capability to generate embodied multimodal responses directly from omni inputs, meeting the diverse requirements of embodied interaction. XBot-Omni enables robots not only to perceive the omni world but also to express themselves through speech and bodily behaviors, extending Omni models from conversational interaction to embodied communication in physical environments.

</details>

---

### [[20_Research/Papers/具身智能/FORGE_Force-Aware_Multi-Granularity_Control_for_Efficient_Humanoid_Loco-Manipulation|FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation]]

![[assets/2611.17142_figure.png|800]]

- **arXiv**: [2611.17142](https://arxiv.org/abs/2611.17142)
- **PDF**: https://arxiv.org/pdf/2611.17142
- **详细分析**: [[20_Research/Papers/具身智能/FORGE_Force-Aware_Multi-Granularity_Control_for_Efficient_Humanoid_Loco-Manipulation|FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation]]
- **作者**: Liangjun Xing, Ke Fan, Kailin Li, Bin Wang, Xiaojie Niu, Qingwei Ben, Jiafei Cao, Wei Yao, Yebin Liu, Jingbo Wang, Weinan Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《FORGE: Force-Aware Multi-Granularity Control for Efficient Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid loco-manipulation requires coordinated locomotion, balance regulation, and manipulation under frequent contacts, making teleoperated demonstration collection difficult: a practical controller must simultaneously provide precision, stability, and contact awareness. We propose FORGE, a force-aware multi-granularity control system with a coarse-to-fine command space spanning velocity navigation, planar foot placement, wrist-pose tracking, and optional force-conditioning inputs. Policy training requires no full-body human motion trajectories or joint-angle references; deployment consumes only sparse bilateral wrist poses relative to the pelvis, coarse motion commands, and optional desired wrist-load inputs. For sustained contact, FORGE combines a momentum observer with a learned correction trained using simulator contact-force supervision. At deployment, it estimates low-frequency, wrist-equivalent interaction forces from proprioception and reconstructed low-level arm PD torques, without wrist force/torque sensors. A quasi-static virtual-target loop uses this estimate and an optional desired applied-force input to adapt the wrist target. A frozen locomotion prior and asymmetric residual actions stabilize manipulation-induced whole-body corrections. Experiments evaluate unified-control stability, task-space tracking, quasi-static wrist-equivalent force estimation, squeezing forces during sustained contact with a rigid box, and downstream diffusion-policy execution of a squat-and-lift task across payload conditions. Website: https://bb0928.github.io/forge/.

</details>

---

### [[20_Research/Papers/机器人/Informative_Path_Planning_with_Gaussian_Processes_Error_Bounds,_Algorithms,_and_Benchmarks|Informative Path Planning with Gaussian Processes: Error Bounds, Algorithms, and Benchmarks]]

![[assets/2611.16877_figure.png|800]]

- **arXiv**: [2611.16877](https://arxiv.org/abs/2611.16877)
- **PDF**: https://arxiv.org/pdf/2611.16877
- **详细分析**: [[20_Research/Papers/机器人/Informative_Path_Planning_with_Gaussian_Processes_Error_Bounds,_Algorithms,_and_Benchmarks|Informative Path Planning with Gaussian Processes: Error Bounds, Algorithms, and Benchmarks]]
- **作者**: Kalvik Jakkala, Jennifer Wakulicz, Donald G. Dansereau, Srinivas Akella, Lantao Liu, Jason M. O'Kane
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《Informative Path Planning with Gaussian Processes: Error Bounds, Algorithms, and Benchmarks》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Accurate environmental monitoring relies on Informative Path Planning (IPP) to deploy autonomous systems that maximize information gain. While Gaussian Processes (GPs) provide a robust mathematical foundation for modeling the environment, contemporary IPP approaches remain hindered by heuristic operational constraints and the lack of simultaneous theoretical guarantees for worst-case estimation error and approximation quality. Rather than introducing yet another heuristic, this paper presents a rigorous theoretical analysis of existing error bounds and algorithms to further develop the mathematical foundation for IPP. By evaluating probabilistic and deterministic bounds on reconstruction error, we establish that predictive variance is the theoretically ideal optimization objective for GP-based IPP. Furthermore, we analyze GreedyCover, a recent approach for optimizing predictive variance, and demonstrate that its near-optimal approximation guarantee matches the fundamental hardness-of-approximation limit for the problem. Comprehensive benchmarking confirms that this approach delivers superior estimation accuracy and computational efficiency compared to prominent information-theoretic objectives and optimization methods used in IPP. Finally, this theoretical analysis establishes a rigorous, near-optimal foundation for discrete offline IPP under bounded uncertainty constraints, offering clear and principled guidance for future work in continuous-space and online formulations.

</details>

---

### [[20_Research/Papers/强化学习/ACE-CaP-0_Real-World_Code-as-Policies_in_the_Era_of_Experience|ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience]]

![[assets/2611.16872_figure.png|800]]

- **arXiv**: [2611.16872](https://arxiv.org/abs/2611.16872)
- **PDF**: https://arxiv.org/pdf/2611.16872
- **详细分析**: [[20_Research/Papers/强化学习/ACE-CaP-0_Real-World_Code-as-Policies_in_the_Era_of_Experience|ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience]]
- **作者**: ACE-CaP Team, Changxu Wei, Yunpeng Qing, Guozheng Ma, Bowen Liu, Zexin He, Yilun Kong, Haoming Gu, Jingyuan Liu, Tianyu Zhu, Jianfei Wang, Junqiang Kou...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.3，大模型 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《ACE-CaP-0: Real-World Code-as-Policies in the Era of Experience》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-Sim, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in frontier models have pushed the boundaries of agentic robot control, enabling agents to perform complex robotic tasks through reasoning and interaction. However, repeated calls to these models during execution can substantially increase task completion time. Code as Policies (CaP) offers a route for coding agents to acquire physical skills through experience and retain them in executable programs, allowing the reasoning invested in development to be reused across runs. Developing reliable code policies while limiting the cost of physical experimentation remains a central challenge. We investigate human guidance as a source of priors for feasible actions and simulation as an auxiliary environment for exploring and testing candidate policies. Our findings favor robot demonstrations available on request and simulation used selectively during real-world policy refinement. These findings inform ACE-CaP-0, an agentic recipe that couples policy revision with experience acquisition through Demonstrations on Request and Simulation on Demand. Across eight real-world manipulation tasks spanning alignment, multi-object handling, and bimanual coordination, the resulting frozen programs achieve 92.1\% success (221/240 trials). Mean execution times across tasks range from 0.97 to 2.27 minutes. The programs execute with runtime perception and control, without a human or coding agent in the loop. These results highlight CaP's potential to turn experience into reliable, reusable physical skills.

</details>

---

### [[20_Research/Papers/大模型/NSDL_Neuro-Symbolic_Division_of_Labor_for_Multi-Robot_Task_Planning|NSDL: Neuro-Symbolic Division of Labor for Multi-Robot Task Planning]]

![[assets/2611.16671_figure.jpg|800]]

- **arXiv**: [2611.16671](https://arxiv.org/abs/2611.16671)
- **PDF**: https://arxiv.org/pdf/2611.16671
- **详细分析**: [[20_Research/Papers/大模型/NSDL_Neuro-Symbolic_Division_of_Labor_for_Multi-Robot_Task_Planning|NSDL: Neuro-Symbolic Division of Labor for Multi-Robot Task Planning]]
- **作者**: Xincheng Tan, Ke Wang, Yining Di, Minfeng Zhu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Agent

#### 研究背景与动机

《NSDL: Neuro-Symbolic Division of Labor for Multi-Robot Task Planning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LOCUS-Bench, VIKI-Bench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Planning for a heterogeneous robot team from a scene image and an instruction involves two kinds of decisions. Some must be judged from the scene: which goals are already met, how the task splits, and which robot does what. Others follow from these and can be computed: prerequisite actions, handoffs between robots, and timing. We argue that each kind should go to the component suited to it: a small vision-language model learns the first, and a deterministic solver computes the second. In NSDL (Neuro-Symbolic Division of Labor), the trained model writes its judgments as a plan sketch, which lists the goals that still need action and the intended steps in order, each with a robot. The solver expands the sketch into an executable joint plan. The model calls two tools, a detector for evidence and the solver, and is trained with the solver in the loop. We evaluate on the public VIKI-L2 benchmark and on LOCUS-Bench, a new benchmark that grades the two kinds of difficulty separately. NSDL outperforms end-to-end planners and formalize-then-plan baselines on both benchmarks and with three backbones from 3B to 8B; the 7B model reaches 97.0% out-of-distribution accuracy on VIKI-L2. Ordering and scheduling errors nearly disappear once the solver writes the structure; the remaining failures are misjudged states, and most goals the model misses are ones it never lists. Code, model weights, and LOCUS-Bench are publicly available at https://github.com/Xincheng-Tan/NSDL.

</details>

---

### [[20_Research/Papers/大模型/Reins_Frontier_Multimodal_Models_Driving_Real_Robot_Arms_on_Long-Horizon_Tasks,_Zero-Shot|Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot]]

![[assets/2611.16632_figure.png|800]]

- **arXiv**: [2611.16632](https://arxiv.org/abs/2611.16632)
- **PDF**: https://arxiv.org/pdf/2611.16632
- **详细分析**: [[20_Research/Papers/大模型/Reins_Frontier_Multimodal_Models_Driving_Real_Robot_Arms_on_Long-Horizon_Tasks,_Zero-Shot|Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot]]
- **作者**: Pengfei Ye, Zhiyang Dou, Yuxiang Ma, Haonan Chen, Heng Yang, Edward H. Adelson
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.3，大模型 0.3，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Reins: Frontier Multimodal Models Driving Real Robot Arms on Long-Horizon Tasks, Zero-Shot》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Frontier models such as GPT-6.1 Sol, GPT-6 Astra and Claude Opus 5.5 can now plan and call tools, yet they still struggle to drive real robots through long-horizon, contact-rich manipulation, blind while the arm moves and while they think. We present Reins, a harness in which an off-the-shelf model operates a dual-arm robot with 3D perception tools and atomic actions that report contact and grip. The model chains actions in one call, each with a condition that must hold, stopping at the first that fails; a second instance, the narrator, watches the cameras continuously and reports what changed with every result. From images, Reins also builds a simulation-ready twin of the scene for continual policy learning. With natural-language prompts and no task-specific code, GPT-6.1 Sol succeeds in 88% of real episodes on five tasks; without the harness, it fails every shell game, taking 8 times as long. Three frontier models perform alike but differ in tracking a scene that changes while the actor thinks. Code will be released upon publication.

</details>

---

### [[20_Research/Papers/具身智能/STVLA_Spatial-aware_and_Temporal-memory_forVision-Language-Action_Models|STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models]]

![[assets/2611.16589_figure.png|800]]

- **arXiv**: [2611.16589](https://arxiv.org/abs/2611.16589)
- **PDF**: https://arxiv.org/pdf/2611.16589
- **详细分析**: [[20_Research/Papers/具身智能/STVLA_Spatial-aware_and_Temporal-memory_forVision-Language-Action_Models|STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models]]
- **作者**: Zhuo Han, Yeqiang Wang, Xinran Wang, Hongwei Han, Yi Xiong, Zunian Wan, Jianbo Mao, Huan Peng, Yongcheng Liu, Wei Shan, Maoqing Yao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.8（加权：具身智能 1.2，大模型 0.1，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《STVLA: Spatial-aware and Temporal-memory forVision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DepthVLA, EventVLA, MemoryVLA, OpenVLA, Real-World, STVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic manipulation often requires both spatial scene understanding and task history. However, many vision-language-action (VLA) policies rely primarily on current observations, without explicitly integrating spatial structure and task history. Appearance-based memories can be sensitive to occlusion and viewpoint changes, while spatial representations of the current scene alone do not preserve how the scene has changed during task execution. We introduce STVLA, a framework that incorporates features from a pretrained visual geometry foundation model into temporal memory alongside visual representations. This allows the policy to recall past scene structure as context for current action decisions. To select informative history, STVLA uses a mathematically grounded scoring rule that balances relevance to the current observation with complementary evidence from memory. Across evaluations on LIBERO, LIBERO-Mem, MIKASA-Robo, and SimplerEnv Bridge, STVLA achieves the highest average success rate among the compared methods on each benchmark. On real-world block stacking, object organization, and phone packaging, it improves success over $π_{0.5}$ by $58.33$, $30.00$, and $35.00$ percentage points, respectively. These results support integrating scene geometry into temporal memory to improve manipulation requiring both spatial precision and task history. Project website: \href{https://stvla.github.io/}{https://stvla.github.io/}

</details>

---

### [[20_Research/Papers/具身智能/Input-output_characterization_of_robotic_grasping_Connecting_design_parameters_to_grasp_behavior_through_the_admittance|Input-output characterization of robotic grasping: Connecting design parameters to grasp behavior through the admittance]]

![[assets/2611.16507_first_page.png|800]]

- **arXiv**: [2611.16507](https://arxiv.org/abs/2611.16507)
- **PDF**: https://arxiv.org/pdf/2611.16507
- **详细分析**: [[20_Research/Papers/具身智能/Input-output_characterization_of_robotic_grasping_Connecting_design_parameters_to_grasp_behavior_through_the_admittance|Input-output characterization of robotic grasping: Connecting design parameters to grasp behavior through the admittance]]
- **作者**: Julien Vanderheyden, Guillaume Drion, Pierre Sacré, Fulvio Forni
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.4（加权：具身智能 1.5，机器人 0.9）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《Input-output characterization of robotic grasping: Connecting design parameters to grasp behavior through the admittance》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Low-impedance grippers make the dynamics of a grasp matter. Current grasp metrics, however, are static: they describe how a held object resists constant loads, not how it responds to time-varying ones. To quantify this, we rely on small-signal analysis to characterize a grasp by its admittance, the transfer matrix relating load perturbations to object displacements around an equilibrium. This transfer matrix recovers the stiffness and stability of the grasp at zero frequency and captures its natural frequencies and peak gain under time-varying loads. We apply this characterization to a planar two-finger gripper under proportional-derivative control. We show that two grasps of the same object in the same position and with the same contact forces can differ in stiffness by two orders of magnitude. Likewise, two grasps that share the same stiffness can exhibit very different resonances. Nonlinear simulations confirm the effectiveness of our small-signal analysis in capturing the dynamic behavior of grasping.

</details>

---

### [[20_Research/Papers/机器人/RGB-D_SLAM_on_the_Edge_Benchmarking_and_Profiling_RTAB-Map_and_ORB-SLAM3_on_the_Raspberry_Pi_5|RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5]]

![[assets/2611.16472_figure.png|800]]

- **arXiv**: [2611.16472](https://arxiv.org/abs/2611.16472)
- **PDF**: https://arxiv.org/pdf/2611.16472
- **详细分析**: [[20_Research/Papers/机器人/RGB-D_SLAM_on_the_Edge_Benchmarking_and_Profiling_RTAB-Map_and_ORB-SLAM3_on_the_Raspberry_Pi_5|RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5]]
- **作者**: Himanshu Patil, Jaideep Joshi, Rohit Saluja, Ganesh Ramakrishnan
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: ComputerVision

#### 研究背景与动机

《RGB-D SLAM on the Edge: Benchmarking and Profiling RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Micro aerial vehicles that operate without GPS often run SLAM on ARM-based edge boards, yet there is little published data on how standard RGB-D SLAM systems behave on such hardware. We benchmark RTAB-Map and ORB-SLAM3 on the Raspberry Pi 5 using six TUM RGB-D sequences at three image resolutions, recording tracking coverage, trajectory error, time per frame, memory, CPU load and temperature for every run, and we profile both systems at the stage and function level. RTAB-Map was configured to process and keep every frame, so its back end runs on every frame rather than at its default rate of 1 Hz. On the sequences that every configuration tracked, its front end takes 38-74 ms per frame and its full pipeline 150-462 ms, compared with 13-45 ms and 26-62 ms for ORB-SLAM3. RTAB-Map's main cost is optimizing a pose graph that keeps growing, because its working memory is unbounded by default; ORB-SLAM3's local bundle adjustment costs about as much as its tracking but runs in a parallel thread. At quarter resolution, both systems lose tracking on most sequences, and runs that lose tracking finish sooner and report lower error on the poses they keep, so time and accuracy must be read alongside coverage. Timing is repeatable to within 1-5%, but trajectory error varies by up to 27% between identical runs, so the accuracy differences between the two systems are inconclusive. No thermal throttling occurred.

</details>

---

### [[20_Research/Papers/具身智能/HALO_Human-Aligned_Data_Collection_for_WhoLe-body_MObile_Manipulation|HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation]]

![[assets/2611.16439_figure.png|800]]

- **arXiv**: [2611.16439](https://arxiv.org/abs/2611.16439)
- **PDF**: https://arxiv.org/pdf/2611.16439
- **详细分析**: [[20_Research/Papers/具身智能/HALO_Human-Aligned_Data_Collection_for_WhoLe-body_MObile_Manipulation|HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation]]
- **作者**: Shuai Yang, Fangyi Xu, Yishu Shen, Kecheng Zheng, Yinghao Xu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《HALO: Human-Aligned Data Collection for WhoLe-body MObile Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Learning whole-body mobile manipulation requires demonstrations that coordinate bimanual actions with locomotion across extended workspaces. However, existing interfaces trade off direct robot control, perception and action alignment, and natural operator mobility, making such demonstrations difficult to collect. We introduce HALO, a human-aligned data collection system for whole-body mobile manipulation. The system aligns the operator's perception and action space with the robot while preserving direct physical feedback and natural locomotion. Operators guide the robot end-effectors through kinesthetic teaching and move a low-resistance platform without the deployed mobile base while performing bimanual manipulation. This interface enables more natural whole-body demonstrations, but the close human-robot coupling introduces discrepancies between the demonstration and deployment settings. We address these discrepancies with deployment-aligned demonstration processing, which calibrates and temporally aligns platform motion with the deployed base response and masks and inpaints demonstrator hands in recorded observations. Compared with Mobile ALOHA and VR teleoperation, HALO enables up to 2.9x faster demonstration collection while maintaining comparable or higher success rates. Policies trained with HALO perform precise manipulation tasks, including zip-tie fastening, and achieve a 73.3% success rate on a six-stage long-horizon mobile manipulation task involving repeated coordinated base and arm motion. Project page: https://robbyant-research.github.io/Lingbot-ALOHA/

</details>

---

### [[20_Research/Papers/具身智能/VOKE_Visual_Object_Kinematics_Estimator_for_Dexterous_In-Hand_Manipulation|VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation]]

![[assets/2611.16423_figure.png|800]]

- **arXiv**: [2611.16423](https://arxiv.org/abs/2611.16423)
- **PDF**: https://arxiv.org/pdf/2611.16423
- **详细分析**: [[20_Research/Papers/具身智能/VOKE_Visual_Object_Kinematics_Estimator_for_Dexterous_In-Hand_Manipulation|VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation]]
- **作者**: Shengjia Zhu, Wenqiang Xu, Lin Shao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.7（加权：具身智能 1.8，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《VOKE: Visual Object Kinematics Estimator for Dexterous In-Hand Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HFL-Net, HOPE-Net, KARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based dexterous in-hand manipulation requires knowing not only where an object is, but also how it moves. However, most robotic manipulation systems rely on off-the-shelf visual perception models whose outputs are limited to static object masks, geometry, or 6D poses, leaving downstream controllers to infer object dynamics implicitly from noisy visual observations. We present VOKE, a kinematics-aware perception framework that augments existing object and hand-object pose estimators to recover a complete object kinematic state comprising pose, linear and angular velocity, and linear and angular acceleration. VOKE contains two core perception modules and a downstream application study. First, a Pluggable Kinematics Module (PKM) attaches to the output of a standard pose estimator and predicts the object's linear and angular velocity and acceleration from temporal visual features. Second, a Kinematics-guided Pose Refinement Module (KPRM) converts this motion vector into a second-order, motion-prior reference pose and refines the per-frame pose estimates. We evaluate VOKE on DexYCB and OakInk, where it consistently improves object pose estimation across three different backbones and substantially reduces velocity and acceleration estimation error compared with pose differencing. As a downstream application, we use Kinematics-Augmented Reinforcement Learning (KARL) to compare a kinematics-augmented policy with a pose-history baseline. After training the policies in simulation, we transfer the kinematics-augmented policy to the physical robot without policy fine-tuning, demonstrating the complete perception-to-control pathway in the target domain.

</details>

---

### [[20_Research/Papers/具身智能/ManiLadder_Benchmarking_Robot_Manipulation_Through_a_Categorized_and_Multi-Difficulty_Level_Task_Ladder|ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Level Task Ladder]]

![[assets/2611.16374_figure.png|800]]

- **arXiv**: [2611.16374](https://arxiv.org/abs/2611.16374)
- **PDF**: https://arxiv.org/pdf/2611.16374
- **详细分析**: [[20_Research/Papers/具身智能/ManiLadder_Benchmarking_Robot_Manipulation_Through_a_Categorized_and_Multi-Difficulty_Level_Task_Ladder|ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Level Task Ladder]]
- **作者**: Chongkai Gao, Jieao Shi, Zhaoyu Mu, Yudi Lin, Xuanwei Liu, Wei Ken Ng, Baiye Cheng, Anqi Chen, Kerun Liu, Zhuoran Li, Xuchuan Huang, Haoyang Li...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.1（加权：具身智能 1.8，机器人 1.3）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《ManiLadder: Benchmarking Robot Manipulation Through a Categorized and Multi-Difficulty Level Task Ladder》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MetaWorld。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent advances in robotic manipulation have enabled increasingly complex and dexterous behaviors, yet existing benchmarks still focus on simple pick-and-place tasks and lack a systematic framework for measuring progress in robot learning along the axis of task difficulty. We present ManiLadder, a large-scale and organized simulation benchmark for robotic manipulation. ManiLadder contains 112 carefully designed tasks stratified into 4 difficulty levels, with 8 categories in each level, spanning rigid-body and deformable-object manipulation, single-arm and dual-arm settings, and gripper and dexterous-hand end-effectors. To calibrate difficulty, we fix the data amount the same for every task and use a unified flow- matching imitation learning policy under the same training and evaluation protocols, then use its evaluation success rate as an operational empirical difficulty signal. All tasks are iteratively refined until they fall into target difficulty ranges, which are then verified across different random seeds, policies, and agentic learning systems. We further analyze the task properties, compare different policy performances and training settings, analyze task transfer and data scaling behaviors, and conduct real-world experiments showing that the designed tasks preserve their difficulty ordering beyond simulation. ManiLad- der provides a calibrated ladder for measuring, comparing, and advancing robotic manipulation capabilities. More results are available at https://maniladder-benchmark.github.io/.

</details>

---

### [[20_Research/Papers/具身智能/Memory-Efficient_Parallel_Policy_Learning_for_Collapse-Reactive_Retreat_via_Hybrid_Terrain_Modeling|Memory-Efficient Parallel Policy Learning for Collapse-Reactive Retreat via Hybrid Terrain Modeling]]

![[assets/2611.16337_figure.png|800]]

- **arXiv**: [2611.16337](https://arxiv.org/abs/2611.16337)
- **PDF**: https://arxiv.org/pdf/2611.16337
- **详细分析**: [[20_Research/Papers/具身智能/Memory-Efficient_Parallel_Policy_Learning_for_Collapse-Reactive_Retreat_via_Hybrid_Terrain_Modeling|Memory-Efficient Parallel Policy Learning for Collapse-Reactive Retreat via Hybrid Terrain Modeling]]
- **作者**: Yuki Kadokawa, Ritsuki Matsunaga, Yuqi Yang, Edgar Anarossi, Takamitsu Matsubara
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.3（加权：具身智能 0.6，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Memory-Efficient Parallel Policy Learning for Collapse-Reactive Retreat via Hybrid Terrain Modeling》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GranularGym, Sim-to-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

At disaster sites and on unstable slopes, robot contact can collapse uninspected terrain, requiring retreat upon support loss. Massively parallel reinforcement learning of collapse-reactive retreat requires independent state--action experiences. However, on shared rigid-body collapsible terrain, one robot's collapse alters others' contacts without direct interaction. We call this indirect interference. Duplicating terrain objects prevents this but is memory-intensive, limiting parallel sampling. Our key insight is that policy learning does not necessarily require rigid-body collapse modeling, which is feasible but computationally expensive; collapse-induced contact responses can suffice. We therefore propose a memory-efficient parallel policy-learning framework for collapse-reactive retreat via hybrid terrain modeling. Hybrid terrain modeling combines rigid-body simulation of non-collapsible terrain with virtual contact forces for collapsible regions. A State-Multiplexed Contact Model shares terrain geometry and a contact-response law while maintaining environment-specific collapse states, enabling independent experiences without terrain objects for collapsible regions. The framework trains a proprioceptive policy for both normal locomotion and collapse-reactive retreat. It supports over 100 times as many parallel environments as fine-resolution rigid-block terrain within the same GPU memory limit. This scalability and improved sample efficiency enable over 50 times faster policy convergence with comparable retreat performance. Sim-to-sim and real-robot experiments demonstrate retreat under multiple collapse conditions. A supplementary video is available at: https://youtu.be/_RrhwjzEPE0

</details>

---

### [[20_Research/Papers/强化学习/Alloy_A_Multi-Material_Physics_Engine_for_Robot_Learning|Alloy: A Multi-Material Physics Engine for Robot Learning]]

![[assets/2611.16312_figure.jpg|800]]

- **arXiv**: [2611.16312](https://arxiv.org/abs/2611.16312)
- **PDF**: https://arxiv.org/pdf/2611.16312
- **详细分析**: [[20_Research/Papers/强化学习/Alloy_A_Multi-Material_Physics_Engine_for_Robot_Learning|Alloy: A Multi-Material Physics Engine for Robot Learning]]
- **作者**: Pranay Gupta, Deepanshu Rohilla
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Alloy: A Multi-Material Physics Engine for Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots handle much more than rigid objects: towels, cables, water, sand. The simulators used to train robots at scale are strongest on rigid bodies, and adding another material usually means a second engine and hand-written glue between the two. We present Alloy, an open-source physics engine for robot learning in which rigid robots, cloth, cables, liquids, granular material and soft bodies share one scene. Each object is described once; Alloy assigns it to a solver suited to its material, couples the solvers inside every control step, and runs the scene in many parallel worlds on one GPU, or on a CPU. Every world carries a health grade, to help tell a failure of the physics from a failure of the policy. Alloy is built on Newton, MuJoCo Warp and Warp, and it is written to be driven by coding agents: its documentation ships inside the package, every error names its fix, and the engine is exposed as tools over the Model Context Protocol. In a cold test, agents that had never seen Alloy installed a pre-release from the package index and trained policies for walking, cable handling and pouring on a single GPU. We also report how throughput grows with the number of worlds, depth-camera throughput, agreement with closed-form references, and a reliability test over a thousand worlds.

</details>

---

### [[20_Research/Papers/具身智能/Robot_Navigation_and_Obstacle_Avoidance_from_Randomly_Positioned_External_Cameras|Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras]]

![[assets/2611.16282_figure.png|800]]

- **arXiv**: [2611.16282](https://arxiv.org/abs/2611.16282)
- **PDF**: https://arxiv.org/pdf/2611.16282
- **详细分析**: [[20_Research/Papers/具身智能/Robot_Navigation_and_Obstacle_Avoidance_from_Randomly_Positioned_External_Cameras|Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras]]
- **作者**: Raul Steinmetz, Jair Augusto Bottega, Ayanori Yorozu, Akihisa Ohya
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 2.8（加权：具身智能 1.5，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Robot Navigation and Obstacle Avoidance from Randomly Positioned External Cameras》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study robot navigation in indoor environments from fixed exocentric cameras (infrastructure-mounted, external to the robot). We show that standard Proximal Policy Optimization (PPO), which succeeds with onboard cameras, fails to learn this navigation end-to-end in our setup. This failure results from the perspective mismatch between exocentric observations and egocentric action and goal formulations, which is too complex to resolve from the reward signal alone. To address this, we propose Viewpoint-Invariant Navigation from Exocentric Cameras (VINE). VINE uses an obstacle map estimation network, trained with supervised learning, that takes exocentric images, camera pose, robot pose, and room dimensions as input and produces a viewpoint-invariant obstacle map. This map can be used either by a PPO policy or by a planner such as A*. VINE's map estimation performs better than perspective mapping approaches, handles cameras placed across a wide range of positions and orientations without view-specific tuning, requires only approximate camera pose estimates (noise with a standard deviation of 30cm per axis in x, y, and z and about 20° of rotation error on average), is robust to intrinsic variation, and extends to two-camera setups with partial coverage. Despite operating from cameras randomized in position during evaluation, VINE surpasses the navigation success rate of PPO with an onboard camera in simulated environments.

</details>

---

### [[20_Research/Papers/具身智能/BWM-Forge_Agentic_World_Programming_for_Embodied_Intelligence|BWM-Forge: Agentic World Programming for Embodied Intelligence]]

![[assets/2611.16221_figure.png|800]]

- **arXiv**: [2611.16221](https://arxiv.org/abs/2611.16221)
- **PDF**: https://arxiv.org/pdf/2611.16221
- **详细分析**: [[20_Research/Papers/具身智能/BWM-Forge_Agentic_World_Programming_for_Embodied_Intelligence|BWM-Forge: Agentic World Programming for Embodied Intelligence]]
- **作者**: BWM Team
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.1，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《BWM-Forge: Agentic World Programming for Embodied Intelligence》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GenSim, LingBot-World, VBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generating diverse robot videos requires control over scene geometry, robot motion, and viewpoints. End-to-end video generation offers limited direct access to these variables, making targeted edits and reuse across tasks difficult. We present BWM-Forge, a code-driven framework for controllable video generation in robotics. Given robot assets and a task description, the framework accepts an initial image, an image with motion data, or a human demonstration video. A coding agent constructs editable Blender scene programs that specify objects, robot motion, and cameras. The resulting proxy videos provide structural and motion references for a video generation model, which adds visual detail. A multi-agent harness coordinates input processing, scene construction, review, and rendering. Automated evaluation and user feedback support iterative refinement, while an experience repository stores and retrieves reusable modeling and rendering rules. This design supports multiple robot embodiments, synchronized viewpoints, and appearance variation from a shared scene program. We evaluate the framework on 15 tasks covering five robot types. Compared with LingBot-World Base Cam on these tasks, BWM-Forge achieves higher aesthetic quality, imaging quality, subject and background consistency, motion smoothness, and RoboJudge-9B physical adherence and instruction alignment scores. The baseline scores higher in dynamic degree. Qualitative cases illustrate viewpoint control, scene variation, feedback-driven edits, and experience reuse across scenes. These results demonstrate a practical approach to generating controllable robot videos through editable, executable scene representations.

</details>

---

### [[20_Research/Papers/机器人/A_Coupled_Control_Barrier_Function_Approach_to_Deadlock-Free_Multi-Robot_Conflict_Resolution|A Coupled Control Barrier Function Approach to Deadlock-Free Multi-Robot Conflict Resolution]]

![[assets/2611.16218_figure.png|800]]

- **arXiv**: [2611.16218](https://arxiv.org/abs/2611.16218)
- **PDF**: https://arxiv.org/pdf/2611.16218
- **详细分析**: [[20_Research/Papers/机器人/A_Coupled_Control_Barrier_Function_Approach_to_Deadlock-Free_Multi-Robot_Conflict_Resolution|A Coupled Control Barrier Function Approach to Deadlock-Free Multi-Robot Conflict Resolution]]
- **作者**: Gary Rostomyan, Ketan Savla, Petros A. Ioannou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《A Coupled Control Barrier Function Approach to Deadlock-Free Multi-Robot Conflict Resolution》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Many robotic applications involve scenarios where multiple robots interact and the decisions of one robot influence the behavior of others. This paper presents a quadratic programming (QP)-based feedback controller for multi-robot conflict resolution with input constraints. Safety is enforced using coupled Control Barrier Function (CBF), while a yielding matrix encodes how robots influence each other. Unlike existing methods with fixed or hard priorities, the proposed framework enables yielding preferences while guaranteeing deadlock-free operation by design. Sufficient conditions are established for the controller to be locally Lipschitz. The optimal CBF sign- indefinite slack is shown to admit a finite uniform bound, which is compensated through an enlarged CBF safety margin to obtain a forward invariant set contained within the desired safe set. The analysis also identifies an irreducible slack component due to finite maximum deceleration that cannot be eliminated by increasing the slack penalty. Finally, sufficient conditions on the yielding matrix and nominal controller are derived to exclude deadlock states. Simulations demonstrate adaptive coordination across yielding preferences and robustness to robot failures.

</details>

---

### [[20_Research/Papers/机器人/Visibility-Aware_Task_and_Motion_Planning_with_Task-Centric_Perception|Visibility-Aware Task and Motion Planning with Task-Centric Perception]]

![[assets/2611.16213_figure.jpg|800]]

- **arXiv**: [2611.16213](https://arxiv.org/abs/2611.16213)
- **PDF**: https://arxiv.org/pdf/2611.16213
- **详细分析**: [[20_Research/Papers/机器人/Visibility-Aware_Task_and_Motion_Planning_with_Task-Centric_Perception|Visibility-Aware Task and Motion Planning with Task-Centric Perception]]
- **作者**: Sahit Chintalapudi, Xiaoyan Wang, Aryan Zoroufi, Aditya Agarwal, Nancy Kanwisher, Tomás Lozano-Pérez, Leslie Pack Kaelbling
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Visibility-Aware Task and Motion Planning with Task-Centric Perception》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Long-horizon manipulation under uncertainty remains a challenging problem in robotics. We present \ourmethod{}, an algorithm for Visibility-Aware Task and Motion Planning. \ourmethod{} extends existing deterministic task and motion planning solvers to partially observable object rearrangement tasks, while still being able to take advantage of the efficiency and compositional generalization over long horizons of the base solver. This extension interleaves sensing actions into a plan skeleton that assumed full observability, and uses a novel persistent object-based memory to fuse observations into object mesh hypotheses and an observed occupancy map. We evaluate \ourmethod{} on real-world tabletop rearrangement tasks which feature heavy occlusion and partial visibility and demonstrate that it outperforms baselines that do not perform active perception or have persistent memory.

</details>

---

### [[20_Research/Papers/强化学习/PERA_Plug-in_Experts_for_Robotic_Actions_in_Continual_Whole-Body_Control|PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control]]

![[assets/2611.16188_figure.png|800]]

- **arXiv**: [2611.16188](https://arxiv.org/abs/2611.16188)
- **PDF**: https://arxiv.org/pdf/2611.16188
- **详细分析**: [[20_Research/Papers/强化学习/PERA_Plug-in_Experts_for_Robotic_Actions_in_Continual_Whole-Body_Control|PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control]]
- **作者**: Shangchao Hu, Yadan Sun, Xibo Yu, Wei Huang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《PERA: Plug-in Experts for Robotic Actions in Continual Whole-Body Control》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion imitation enables humanoid robots to acquire whole-body skills such as walking and dancing. However, fine-tuning an entire policy for a new skill can affect existing behaviors, while training a separate policy for each skill increases training and maintenance costs. We present PERA, a method for learning new skills by reusing existing motion capabilities. PERA freezes a pretrained mixture-of-experts policy and trains an additional task expert and its routing score using task rewards or teacher-action supervision. In Unitree G1 simulation, each added task module contains approximately 1.03% of the parameters of the base actor. Built on our pretrained policy, PERA successfully completes all ten new tasks. Disabling the expert restores the original computation path of the base policy, which still fully executes all 126 original motions. Enabling the expert also improves the execution of some dance motions not used to train that expert, indicating that its benefits extend beyond its training motions. Experiments with HoloMotion further demonstrate the applicability of PERA to different base policies.

</details>

---

### [[20_Research/Papers/机器人/Robo-SWE_An_Executable_Issue-Resolution_Dataset_Mined_from_Robot_Software_Repositories|Robo-SWE: An Executable Issue-Resolution Dataset Mined from Robot Software Repositories]]

![[assets/2611.16116_first_page.png|800]]

- **arXiv**: [2611.16116](https://arxiv.org/abs/2611.16116)
- **PDF**: https://arxiv.org/pdf/2611.16116
- **详细分析**: [[20_Research/Papers/机器人/Robo-SWE_An_Executable_Issue-Resolution_Dataset_Mined_from_Robot_Software_Repositories|Robo-SWE: An Executable Issue-Resolution Dataset Mined from Robot Software Repositories]]
- **作者**: Vahid Haratian, Vahid Ansari, Mohammadhossein Malmir, Alois Knoll
- **cs 子类**: cs.RO, cs.SE
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.0（加权：具身智能 0.3，大模型 0.2，机器人 1.5）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Robo-SWE: An Executable Issue-Resolution Dataset Mined from Robot Software Repositories》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Coding agents are evaluated mostly on general-purpose software, but domain-specific systems require domain-aware evaluation. Robot software is a particularly challenging case: Robot Operating System 2 (ROS 2) packages have their own build tools, simulators and learning frameworks are built on physics engines, and behavior that depends on timing and hardware is hard to test. We present Robo-SWE, a dataset of 236 executable issue-resolution tasks mined from merged pull requests in 28 public robotics repositories in four domains: ROS 2 systems, simulation and physics engines, robotics algorithm libraries, and robot-learning frameworks. Each task contains the original issue text, a container recipe for the repository at the commit before the fix, the developers' fix, and the developers' tests, which fail before the fix and pass after it in repeated offline runs. The dataset also keeps a provenance ledger of all 1,567 candidate pull requests, with the stage each reached and the reason for every rejection, and, as a first use, 3,540 graded attempts by five coding-agent setups with recorded patches and 3,529 available trajectories. Across three runs per primary setup, resolve rates range from 45.8% for Claude Sonnet 5.5 to 56.5% for Claude Opus 5.5; GPT-6.1 Sol reaches 54.1% at maximum effort and 52.5% at medium effort, and GPT-6 Astra 51.4%. GLM-5.3 resolves 46.2%, and Kimi K3.1 Pro 43.9%. The tasks are validated by execution; verification of their fairness by human reviewers is future work. The dataset and public leaderboard are available online.

</details>

---

### [[20_Research/Papers/强化学习/Video-Action_Models_for_Data-Efficient_Industrial_Manipulation|Video-Action Models for Data-Efficient Industrial Manipulation]]

![[assets/2611.15974_figure.png|800]]

- **arXiv**: [2611.15974](https://arxiv.org/abs/2611.15974)
- **PDF**: https://arxiv.org/pdf/2611.15974
- **详细分析**: [[20_Research/Papers/强化学习/Video-Action_Models_for_Data-Efficient_Industrial_Manipulation|Video-Action Models for Data-Efficient Industrial Manipulation]]
- **作者**: Eugenio Chisari, Stefanos Charalambous, Oliver Sanchez, Thomas Umbach, Michael Gentner, Fabio Quattrini, Norica Bacuieti, Sabin Grube Doiz, Valentin Bertle, Sigmund Hennum Hoeg, Alain Ryser, German Rodriguez...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, RL

#### 研究背景与动机

《Video-Action Models for Data-Efficient Industrial Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Industrial manipulation requires precise alignment and controlled handling of rigid, deformable, and flexible components. Yet, the benefits of pretrained visuomotor policies remain underexplored in settings where limited access to specialized hardware, components, and fixtures constrains demonstration collection and evaluation. Understanding task-specific data requirements is important for assessing their scalability across diverse processes on the factory floor. We investigate whether video pretraining can support reliable industrial manipulation with limited action data. We propose FLUX-mimic, a video-action model, motivated by the potential of video pretraining to capture motion and interaction patterns that enable sample-efficient training. FLUX-mimic is built on a backbone pretrained on large-scale web and industrial task data, and an action expert to generate robot trajectories. We train our policy by joint video-action training. Across four automotive manufacturing benchmark tasks and two bimanual robot platforms, FLUX-mimic outperforms all considered baselines on the dexterous robot platform and matches pi_{0.5}'s average success rate on the gripper-based robot platform. On a deformable part kitting task, FLUX-mimic reaches 77.5% success with as little as two hours of task-specific action-labeled demonstrations.

</details>

---

### [[20_Research/Papers/机器人/Runtime_Safety_and_Emergency_Stops_on_a_Full-Size_Humanoid_Deployment_Lessons_and_a_Case_for_Graduated_Force_Authority|Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority]]

![[assets/2611.15928_figure.png|800]]

- **arXiv**: [2611.15928](https://arxiv.org/abs/2611.15928)
- **PDF**: https://arxiv.org/pdf/2611.15928
- **详细分析**: [[20_Research/Papers/机器人/Runtime_Safety_and_Emergency_Stops_on_a_Full-Size_Humanoid_Deployment_Lessons_and_a_Case_for_Graduated_Force_Authority|Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority]]
- **作者**: Max Conway, Yutong Zhang, Allen Devaraj, William Xie, Alessandro Roncone, Nikolaus Correll
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Runtime Safety and Emergency Stops on a Full-Size Humanoid: Deployment Lessons and a Case for Graduated Force Authority》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Full-size humanoid robots are being considered for hazardous industrial work such as disassembling electric-vehicle batteries. We describe the safety mechanisms of an open-source autonomy stack for the Unitree H1-2 humanoid and what deploying them taught us. All joint commands pass through a safety layer that runs separately from the control software. It enforces joint position, velocity, and torque limits, and it stops the robot when a state estimate becomes stale or when the hard-wired emergency stop (e-stop) is pressed or disconnected. We pushed the standing robot until it lost balance. With a model-predictive lower-body controller it never recovered, and the operator had to press the e-stop in every trial. Pressing it removes balance control, and the robot falls. The safety layer's own limits trigger the same stop, and limits chosen for manipulation were exceeded during normal walking. Near an operator or a battery pack, the fall can be more dangerous than the cause of the stop. Joint limits bound how much force a robot can apply, but not when applying it is appropriate. Drawing on research on responsibility and on child and adolescent development, we therefore make a case for granting robots force authority in stages, with a person or organization explicitly responsible for its use.

</details>

---

### [[20_Research/Papers/机器人/Robot-Induced_Bias_in_Movement_Smoothness_Metrics_for_Rehabilitation_Quantification_and_Correction_in_Simulation|Robot-Induced Bias in Movement Smoothness Metrics for Rehabilitation: Quantification and Correction in Simulation]]

![[assets/2611.15743_figure.png|800]]

- **arXiv**: [2611.15743](https://arxiv.org/abs/2611.15743)
- **PDF**: https://arxiv.org/pdf/2611.15743
- **详细分析**: [[20_Research/Papers/机器人/Robot-Induced_Bias_in_Movement_Smoothness_Metrics_for_Rehabilitation_Quantification_and_Correction_in_Simulation|Robot-Induced Bias in Movement Smoothness Metrics for Rehabilitation: Quantification and Correction in Simulation]]
- **作者**: David Regev, Alex Scherbakov, Eran Beeri Bamani
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《Robot-Induced Bias in Movement Smoothness Metrics for Rehabilitation: Quantification and Correction in Simulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot mechanics can bias kinematic measures of recovery and limit comparisons across rehabilitation devices. We developed a closed-loop human-robot simulation calibrated to published healthy and stroke group kinematics. Paired runs held motor-control parameters and movement plans fixed to quantify bias in seven metrics relative to a low-impedance reference, normalized using external repeatability benchmarks. Within a subset informed by published device specifications, median log dimensionless jerk (LDLJ) bias was 0.93 and 1.79 benchmark units for stroke and healthy profiles, respectively. Sobol analysis identified Coulomb friction and apparent mass as leading contributors; LDLJ bias persisted across 11 robustness variants. LDLJ bias increased as simulated movements became less fragmented. If recovery similarly reduces fragmentation, this effect could partly mask improvement in measured smoothness. Correction combining identified robot dynamics and observed metrics with gradient-boosted trees reduced median normalized absolute error from 0.77 to 0.10 for LDLJ and from 0.24 to 0.08 for spectral arc length (SPARC) in the device-informed subset of a random 20% hold-out. Median smoothness residuals remained at or below 0.15 benchmark units across four separately held-out parameter regions. Under an alternative controller, LDLJ error decreased from 1.60 to 0.17 without retraining, although transfer varied across metrics. These simulation results support mechanical characterization and movement-dependent correction toward more comparable robotic assessments, motivating validation in patients.

</details>

---

### [[20_Research/Papers/具身智能/What_World_Model_Does_Active_Object_Search_Need_A_Study_under_Imperfect_Detection|What World Model Does Active Object Search Need? A Study under Imperfect Detection]]

![[assets/2611.15689_figure.png|800]]

- **arXiv**: [2611.15689](https://arxiv.org/abs/2611.15689)
- **PDF**: https://arxiv.org/pdf/2611.15689
- **详细分析**: [[20_Research/Papers/具身智能/What_World_Model_Does_Active_Object_Search_Need_A_Study_under_Imperfect_Detection|What World Model Does Active Object Search Need? A Study under Imperfect Detection]]
- **作者**: Kyeongryeol Go
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 0.6，大模型 0.1，世界模型 1，机器人 0.5）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《What World Model Does Active Object Search Need? A Study under Imperfect Detection》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Habitat-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In active object search, a robot must decide where to look and when to stop. Imperfect detection complicates both decisions: a non-detection may indicate occlusion, an out-of-view target, or a false negative, while a detection may be a false positive. This raises the question of which representations a world model needs to support reliable search under imperfect detection. We introduce Bayesian Active Miss-aware Object Search (BAMOS) to investigate how target belief, occupancy belief, and detector errors affect search decisions. Through comprehensive ablations in Isaac Sim and HSSD houses, we examine the roles of these representations and their update mechanisms across different detector configurations. Notably, target belief and its update mechanisms are critical to search performance, with their contribution generally increasing as detection errors become more prevalent. These findings highlight the importance of maintaining and updating target beliefs to support reliable active search under uncertain detector observations, providing insights into the design of world models for embodied agents. Code is available in https://github.com/gokyeongryeol/BAMOS.

</details>

---

### [[20_Research/Papers/具身智能/GraSLA_A_Lightweight_Spatial-Language-Action_Model_with_Grasp_Hypotheses_as_Geometric_Priors|GraSLA: A Lightweight Spatial-Language-Action Model with Grasp Hypotheses as Geometric Priors]]

![[assets/2611.15659_figure.png|800]]

- **arXiv**: [2611.15659](https://arxiv.org/abs/2611.15659)
- **PDF**: https://arxiv.org/pdf/2611.15659
- **详细分析**: [[20_Research/Papers/具身智能/GraSLA_A_Lightweight_Spatial-Language-Action_Model_with_Grasp_Hypotheses_as_Geometric_Priors|GraSLA: A Lightweight Spatial-Language-Action Model with Grasp Hypotheses as Geometric Priors]]
- **作者**: Jibao Yuan, Zixiang Zhao, Wensong Xu, Siqi Lu, Shaofei Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《GraSLA: A Lightweight Spatial-Language-Action Model with Grasp Hypotheses as Geometric Priors》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CogVLA, DreamVLA, GSNet, OpenVLA, PointmapVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper focuses on improving the behavioral diversity and effectiveness of language-conditioned manipulation policies trained through imitation learning. Recently, continuous-action policies have become mainstream in robotic manipulation, but the lack of diverse demonstrations tends to restrict their behavioral diversity. For grasping, a fundamental subtask of manipulation, 6-DoF grasp detection provides diverse grasp hypotheses, but open-loop execution constrains responsiveness in dynamic environments. This motivates us to combine the diversity of grasp hypotheses with the adaptability of continuous-action policies. To this end, we propose GraSLA, a lightweight and effective spatial-language-action model with grasp hypotheses as geometric priors. In particular, we employ spatial and language foundation models to encode scene geometry and task semantics, and integrate them with grasp hypotheses through bidirectional cross-attention for continuous action prediction. On LIBERO, GraSLA achieves an average success rate of 99.30%.

</details>

---

### [[20_Research/Papers/强化学习/Embedded_Sim-to-Real_Visual_Servoing_Learned_Reaching_and_Force-Guided_Placement|Embedded Sim-to-Real Visual Servoing: Learned Reaching and Force-Guided Placement]]

![[assets/2611.15658_figure.png|800]]

- **arXiv**: [2611.15658](https://arxiv.org/abs/2611.15658)
- **PDF**: https://arxiv.org/pdf/2611.15658
- **详细分析**: [[20_Research/Papers/强化学习/Embedded_Sim-to-Real_Visual_Servoing_Learned_Reaching_and_Force-Guided_Placement|Embedded Sim-to-Real Visual Servoing: Learned Reaching and Force-Guided Placement]]
- **作者**: Dezhi Sun, Duy Khang Banh, Kenan Niu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.9（加权：具身智能 1.2，强化学习 0.2，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Embedded Sim-to-Real Visual Servoing: Learned Reaching and Force-Guided Placement》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：CoppeliaSim, RLBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embedded perception-to-control systems must combine visual targeting with reliable contact handling under tight computational constraints. We present a shared architecture on an NVIDIA Jetson AGX Orin controlling a Franka Research 3 through Cartesian impedance control. RealSense D435i observations, YOLO11-seg segmentation, depth back-projection, and hand--eye calibration provide metric robot-frame targets. We compare two strategies: compact proximal policy optimization (PPO) policies transferred from simulation for object- and hole-region reaching, and force-guided Cartesian placement using approximately 2 N normal contact and spiral search. The PPO policies achieved 87.2% and 83.1% success over 1000 simulation episodes each. Across 50 real-robot trials per strategy, the learned hybrid and force-guided analytical pipelines achieved 70.0% and 74.0% completion, respectively. Mean perception latency with TensorRT was 34.55 ms. These results support an embedded architecture combining learned free-space reaching with explicit contact correction.

</details>

---

### [[20_Research/Papers/具身智能/Recover,_Don't_Just_Continue_Learning_from_Feedback_for_Physical_Failure_Understanding_and_Correction|Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction]]

![[assets/2611.15651_figure.png|800]]

- **arXiv**: [2611.15651](https://arxiv.org/abs/2611.15651)
- **PDF**: https://arxiv.org/pdf/2611.15651
- **详细分析**: [[20_Research/Papers/具身智能/Recover,_Don't_Just_Continue_Learning_from_Feedback_for_Physical_Failure_Understanding_and_Correction|Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction]]
- **作者**: Miao Pan, Kaixiang Yao, Xiaohe Zhou, Xu Wang, Qinfeng Li, Wenqi Zhang, Xuhong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.3（加权：具身智能 0.9，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Recover, Don't Just Continue: Learning from Feedback for Physical Failure Understanding and Correction》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：EmbodiedBench, EmbodiedDiag-Bench, FineVLA, Frozen-VLA, HarnessVLA, InstructVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multimodal large language models are regarded as the cognitive foundation of embodied intelligence, but planning from instructions alone cannot make them reliable. During execution, actions deviate from intended effects, constrained by the embodiment and environment. An embodied brain must understand why execution deviates, identify what can be reliably realized, and revise decisions using interaction experience. These correspond to causal failure localization, capability-constrained adaptation, and experience-driven revision. Current embodied foundation models largely lack these capabilities. To address this, we introduce Embodied-Corrector. We construct failure-recovery data by injecting perturbations at subtask boundaries of successful trajectories, replaying affected subtasks, and keeping failures that are observable from public evidence and recoverable from the current state. We align actions, consequences, failure causes, and recoveries into Judge-Cause-Sub-Fine supervision. Training uses evaluation-first SFT: the model learns Judge and Cause first, then Sub and Fine conditioned on accurate prefixes. Since deployment uses self-generated prefixes, evaluation errors propagate into recovery planning, and response-level rewards are too coarse to locate affected planning tokens. We therefore use OPD to internalize the planning distribution under accurate prefixes into that under self-generated ones: the model generates plans from self-generated prefixes, while a contrastive forward pass with accurate prefixes compares token probabilities to reinforce or suppress planning tokens. At deployment, this branch is removed. Experiments show stronger failure analysis and corrective planning: with a frozen VLA, composite task success improves by 6.1 percentage points; with fixed GPT-5.5 execution, manipulation and navigation tasks improve by 13.9 percentage points.

</details>

---

### [[20_Research/Papers/具身智能/Single-View_RGB-D_Force--Deformation_Estimation_for_Robotic_Manipulation_of_Elasto-Plastic_Materials|Single-View RGB-D Force--Deformation Estimation for Robotic Manipulation of Elasto-Plastic Materials]]

![[assets/2611.15650_figure.png|800]]

- **arXiv**: [2611.15650](https://arxiv.org/abs/2611.15650)
- **PDF**: https://arxiv.org/pdf/2611.15650
- **详细分析**: [[20_Research/Papers/具身智能/Single-View_RGB-D_Force--Deformation_Estimation_for_Robotic_Manipulation_of_Elasto-Plastic_Materials|Single-View RGB-D Force--Deformation Estimation for Robotic Manipulation of Elasto-Plastic Materials]]
- **作者**: Dezhi Sun, Marijn van Hilten, Kenan Niu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.3（加权：具身智能 1.2，机器人 1.1）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Single-View RGB-D Force--Deformation Estimation for Robotic Manipulation of Elasto-Plastic Materials》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Persistent deformation complicates elasto-plastic manipulation by coupling physical interaction with spatially distributed shape changes. We investigate the force--deformation relationship using a standard robot, a single eye-in-hand RGB-D camera, and intrinsic force estimates. A 7-DoF Franka Emika FR3 performs normal indentations while an Intel RealSense L515 captures pre- and post-contact surfaces. Point-cloud processing localizes deformation and estimates displaced volume. Force--volume characterization includes 27 measurements over nine force levels. A compact multilayer perceptron (MLP), trained on 52 force--volume pairs at four levels, achieves a held-out RMSE of 1.857 N and $R^2=0.440$. A separate comparison shows lower error for a quadratic model at 16 N and for the MLP at 19 and 23.5 N. An eight-step experiment at 4 N per interaction demonstrates cumulative deformation localization from the second indentation onward. These results establish a practical measurement basis for deformation-aware manipulation using intrinsic force estimates and single-view geometry.

</details>

---

### [[20_Research/Papers/机器人/Helping_Hand_A_Continuum_Robotic_Grasper_for_Traction_in_Single-Channel_Endoscopic_Submucosal_Dissection|Helping Hand: A Continuum Robotic Grasper for Traction in Single-Channel Endoscopic Submucosal Dissection]]

![[assets/2611.15638_figure.png|800]]

- **arXiv**: [2611.15638](https://arxiv.org/abs/2611.15638)
- **PDF**: https://arxiv.org/pdf/2611.15638
- **详细分析**: [[20_Research/Papers/机器人/Helping_Hand_A_Continuum_Robotic_Grasper_for_Traction_in_Single-Channel_Endoscopic_Submucosal_Dissection|Helping Hand: A Continuum Robotic Grasper for Traction in Single-Channel Endoscopic Submucosal Dissection]]
- **作者**: Bendavid Maimon, Thompson Wong, Aedan Mangan, Sukjun Kim, Michael C. Yip, Tania K. Morimoto
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Helping Hand: A Continuum Robotic Grasper for Traction in Single-Channel Endoscopic Submucosal Dissection》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Endoscopic submucosal dissection (ESD) is a minimally invasive approach for removing large polyps from the colon and offers many benefits compared to other surgical approaches. However, ESD is technically very challenging to perform, leading to limited adoption by physicians. We propose the Helping Hand, a two-segment continuum robotic grasper that, together with an electrosurgical knife, enables tissue traction and cutting within a single 3.7 mm working channel. We achieve this functionality by creating a slot at the base of the Helping Hand that lets the electrosurgical knife extend out, enabling countertraction and cutting through one instrument lumen. We evaluate the Helping Hand's workspace and its ability to provide traction forces from different starting configurations. Finally, we demonstrate the full workflow by isolating and removing tissue in an ex vivo chicken thigh, illustrating the potential for the Helping Hand to help improve ESD procedures.

</details>

---

### [[20_Research/Papers/具身智能/ActionCodec2_A_Streaming_Action_Tokenizer|ActionCodec2: A Streaming Action Tokenizer]]

![[assets/2611.15490_figure.png|800]]

- **arXiv**: [2611.15490](https://arxiv.org/abs/2611.15490)
- **PDF**: https://arxiv.org/pdf/2611.15490
- **详细分析**: [[20_Research/Papers/具身智能/ActionCodec2_A_Streaming_Action_Tokenizer|ActionCodec2: A Streaming Action Tokenizer]]
- **作者**: Zibin Dong, Yicheng Liu, Shiduo Zhang, Tianyuan Yuan, Baijun Ye, Jinqiu Wang, Hang Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.4（加权：具身智能 0.6，大模型 0.3，机器人 0.5）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ActionCodec2: A Streaming Action Tokenizer》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most action tokenizers for autoregressive vision language action (VLA) models compress motion into chunks that must be decoded in full before their actions become executable. We introduce ActionCodec2, a non-neural streaming tokenizer that releases actions incrementally while keeping trajectory reconstruction error within a prescribed tolerance. Its encoder quantizes each step relative to the decoder's reconstructed state, so the selected motion primitive corrects residual error rather than allowing errors from independently quantized increments to accumulate. Finding the smallest such primitive set is a geometric covering problem; we derive the exact minimum for translation and constant-factor-tight bounds for rotation. Set-BPE then losslessly merges co-occurring primitive symbols across coordinates and neighboring steps, without a fixed coordinate ordering. A universal version fitted on 20k hours of data from 24 embodiments averages 8.8 tokens per second for 15 Hz end-effector motion on this corpus. With the same VLA backbone, ActionCodec2 outperforms the compared tokenizers on three simulation benchmarks and in zero-shot real-robot evaluation. Its streaming representation allows policies to incorporate state feedback within an action chunk, substantially improving performance over open-loop execution under randomized dynamics, external disturbances, and moving objects. The same tokens also can serve as a direct control interface for VLM agents, which compose successful action sequences into reusable macros. These agent-built macros reduce control decisions and thinking-token usage across attempts and transfer to a held-out task. More results are available at https://zibindong.github.io/actioncodec2-page/

</details>

---

### [[20_Research/Papers/具身智能/SPARC_RoboCup_Standard_Platform_for_Autonomous_Rescue_Competition_with_Initial_Datasets,_Software,_and_Simulation_Environments|SPARC: RoboCup Standard Platform for Autonomous Rescue Competition with Initial Datasets, Software, and Simulation Environments]]

![[assets/2611.15443_figure.jpg|800]]

- **arXiv**: [2611.15443](https://arxiv.org/abs/2611.15443)
- **PDF**: https://arxiv.org/pdf/2611.15443
- **详细分析**: [[20_Research/Papers/具身智能/SPARC_RoboCup_Standard_Platform_for_Autonomous_Rescue_Competition_with_Initial_Datasets,_Software,_and_Simulation_Environments|SPARC: RoboCup Standard Platform for Autonomous Rescue Competition with Initial Datasets, Software, and Simulation Environments]]
- **作者**: Yuezhong Wang, Bichi Zhang, Zhongli Yin, Pingcong Li, Raimund Edlinger, Sören Schwertfeger
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《SPARC: RoboCup Standard Platform for Autonomous Rescue Competition with Initial Datasets, Software, and Simulation Environments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

The RoboCup Standard Platform for Autonomous Rescue Competition (SPARC) is a new competition under development of the RoboCup Rescue Robot League that uses the Unitree A2-W as a common robot platform. SPARC aims to make research on artificial intelligence for autonomous rescue robots accessible to a broader research community, including groups without expertise in developing and maintaining custom robot hardware. By providing a capable standard platform and established benchmark environments, researchers can focus on autonomous navigation, perception, manipulation, and embodied AI for challenging disaster-response scenarios. This paper introduces the SPARC competition, its benchmark environment, and the Unitree A2-W standard platform. Furthermore, we present the first open SPARC datasets collected during the IEEE ICRA 2026 Legged Robot Challenges and RoboCup Rescue 2026, release an open-source software stack for autonomous navigation, and provide initial simulation assets representing RoboCup Rescue test environments. Together, these resources aim to lower the barrier to entry for autonomous rescue robotics and facilitate reproducible research and collaborative development on a common hardware platform.

</details>

---

### [[20_Research/Papers/具身智能/Low-Cost_Mobile_Bimanual_Manipulation_for_Long-Horizon_Toilet_Cleaning|Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning]]

![[assets/2611.15381_figure.png|800]]

- **arXiv**: [2611.15381](https://arxiv.org/abs/2611.15381)
- **PDF**: https://arxiv.org/pdf/2611.15381
- **详细分析**: [[20_Research/Papers/具身智能/Low-Cost_Mobile_Bimanual_Manipulation_for_Long-Horizon_Toilet_Cleaning|Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning]]
- **作者**: Sven Schreiber, Bernard Burdiek, Lasse Huber-Saffer, Yung-Hui Li, Donglin Chen, Shang-Ching Liu, Jianwei Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics

#### 研究背景与动机

《Low-Cost Mobile Bimanual Manipulation for Long-Horizon Toilet Cleaning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Long-VLA, MemoryVLA, OpenVLA, OptimusVLA, SmolVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models have shown promising capabilities for robot manipulation, but their performance on accessible mobile bimanual platforms remains underexplored. We present a low-cost and reproducible mobile bimanual platform integrating two LeRobot SO-101 manipulators with a TurtleBot 4 and a LeRobot-ROS 2 software stack. Using long-horizon toilet cleaning as a case study, we collect 250 real-world demonstrations and evaluate $π_0$, $π_{0.5}$, SmolVLA, and GR00T under the same embodiment and task conditions. We further evaluate variants using SARM-derived task-progress signals and short-term MEM observation history. Among the evaluated models, $π_0$ performs best, achieving 60% strict and 70% relaxed autonomous success, increasing to 90% with limited human intervention. In contrast, the evaluated progress- and memory-augmented variants do not improve their corresponding baselines. Our results demonstrate the feasibility of long-horizon mobile bimanual manipulation on accessible hardware while highlighting remaining challenges in reliable VLA deployment. Project website: https://so101-turtlebot4.github.io/mobile-bimanual-cleaning/

</details>

---

### [[20_Research/Papers/机器人/Interactive_Perception_of_Granular_Materials_via_Robotic_Scooping_and_Force-Torque_Sensing|Interactive Perception of Granular Materials via Robotic Scooping and Force-Torque Sensing]]

![[assets/2611.15339_figure.png|800]]

- **arXiv**: [2611.15339](https://arxiv.org/abs/2611.15339)
- **PDF**: https://arxiv.org/pdf/2611.15339
- **详细分析**: [[20_Research/Papers/机器人/Interactive_Perception_of_Granular_Materials_via_Robotic_Scooping_and_Force-Torque_Sensing|Interactive Perception of Granular Materials via Robotic Scooping and Force-Torque Sensing]]
- **作者**: Samuli Hynninen, Mohammad Amman, Meri Mäkelä, Anirvan Dutta, Ville Kyrki
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics

#### 研究背景与动机

《Interactive Perception of Granular Materials via Robotic Scooping and Force-Torque Sensing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Granular materials exhibit complex and highly variable interaction dynamics, making their reliable manipulation challenging without knowledge of their physical properties. We present an interactive perception framework that infers granular material properties directly from force-torque measurements acquired during scooping. The proposed Latent Filter++ combines a bio-inspired frequency-temporal filter-bank representation with a causal latent dynamical model, allowing the representation to evolve as interaction observations become available while avoiding hand-crafted signal preprocessing. The learned latent representation captures physically meaningful variation in granular materials and supports estimation of properties including grain size and bulk density. Evaluated on 26 diverse granular materials, the approach generalizes to materials excluded from training and enables few-shot adaptation of property-specific mappings using a small number of additional interaction samples. Finally, we demonstrate the relevance of the inferred properties to downstream manipulation by examining their correlation with the maximum acceleration the materials can withstand without spilling from the spoon during transport.

</details>

---

### [[20_Research/Papers/具身智能/BiPOP_Partial-Order_Planning_for_Long-Horizon_Bimanual_Robotic_Manipulation|BiPOP: Partial-Order Planning for Long-Horizon Bimanual Robotic Manipulation]]

![[assets/2611.15317_figure.png|800]]

- **arXiv**: [2611.15317](https://arxiv.org/abs/2611.15317)
- **PDF**: https://arxiv.org/pdf/2611.15317
- **详细分析**: [[20_Research/Papers/具身智能/BiPOP_Partial-Order_Planning_for_Long-Horizon_Bimanual_Robotic_Manipulation|BiPOP: Partial-Order Planning for Long-Horizon Bimanual Robotic Manipulation]]
- **作者**: Kun Chu, Xufeng Zhao, Jan-Gerrit Habekost, Cornelius Weber, Stefan Wermter
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 3.2（加权：具身智能 1.8，大模型 0.1，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《BiPOP: Partial-Order Planning for Long-Horizon Bimanual Robotic Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Bimanual robotic manipulation is versatile, yet its central challenge lies not only in executing dexterous motion with each hand, but also in coordinating the two arms for long-horizon manipulation under coupled spatial and temporal constraints. Prior work has largely focused on endowing robots with human-level manipulation skills, paying less attention to the structure of bimanual behaviour itself: many practical tasks are a coordinated composition of reusable unimanual skills and a small set of synchronous bimanual skills. This makes high-level spatio-temporal coordination, rather than skill acquisition alone, a key bottleneck for efficient bimanual execution. We propose BiPOP, a framework that couples Large Language Models (LLMs) with Temporal Partial-Order Planning for long-horizon bimanual manipulation. At its core is an explicit spatio-temporal model that partitions the workspace by arm reachability and captures inter-arm dependencies, arm assignment, synchronization requirements, and opportunities for safe concurrent execution. Building on this model, an LLM translates natural-language instructions into a formal PDDL specification, while a temporal planner enforces the constraints and schedules actions, yielding plans that are logically consistent at the symbolic level and efficient through parallel execution. On simulated long-horizon tasks of varying complexity, BiPOP outperforms open-loop planning with strong reasoning models and closed-loop ReAct-style planning in success rate, planning time, and plan efficiency, and the full pipeline runs end to end on the real bimanual robot NICOL. A failure analysis further shows that LLM-only planners mainly violate spatial and temporal coordination constraints, which motivates delegating these constraints to a symbolic planner. Code: https://github.com/Kchu/BiPOP

</details>

---

### [[20_Research/Papers/具身智能/APG-Planner_Learning_Vision-Based_High-Speed_Trajectory_Planning_via_Analytic_Policy_Gradient|APG-Planner: Learning Vision-Based High-Speed Trajectory Planning via Analytic Policy Gradient]]

![[assets/2611.15296_figure.png|800]]

- **arXiv**: [2611.15296](https://arxiv.org/abs/2611.15296)
- **PDF**: https://arxiv.org/pdf/2611.15296
- **详细分析**: [[20_Research/Papers/具身智能/APG-Planner_Learning_Vision-Based_High-Speed_Trajectory_Planning_via_Analytic_Policy_Gradient|APG-Planner: Learning Vision-Based High-Speed Trajectory Planning via Analytic Policy Gradient]]
- **作者**: Jinwoo Lee, Geunsik Bae, Changseung Kim, Jiwoo Kim, Woojae Shin, Hyondong Oh
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 机器人, 具身智能, 世界模型
- **相关性评分**: 2.4（加权：具身智能 0.3，强化学习 1.2，世界模型 0.2，机器人 0.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《APG-Planner: Learning Vision-Based High-Speed Trajectory Planning via Analytic Policy Gradient》归入 强化学习、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-based high-speed navigation requires a trajectory planner that can reactively generate smooth, collision-free trajectories from onboard visual observations. Deep reinforcement learning offers a promising approach to vision-based trajectory planning, as it enables the optimization of sequential decision-making policies in complex environments. However, model-free policy gradient methods rely on sample-based policy gradient estimation, which yields noisy gradient estimates and inefficient training. To this end, we propose a framework for learning trajectory planning policies using the analytic policy gradient (APG) method and use it to train APG-Planner, a vision-based high-speed trajectory planner. The proposed framework leverages differential flatness to analytically reconstruct vehicle states from planned trajectories, thereby enabling differentiable trajectory-level state transitions without requiring an explicit low-level dynamics model. By iteratively performing trajectory planning and differentiable state transitions, we construct a differentiable episode rollout and analytically compute policy gradients from episode-level losses, improving both training efficiency and policy performance. After approximately 30 minutes of training on a single GPU, APG-Planner demonstrates comparable or superior performance to existing baseline methods in simulation and achieves speeds of up to 11\,m/s in real-world flight experiments. We further validate the proposed framework on a skid-steer ground robot, demonstrating its applicability to differentially flat robotic systems beyond quadrotors.

</details>

---

### [[20_Research/Papers/具身智能/Autonomous_Trail_Racing_with_a_Bicycle_Robot|Autonomous Trail Racing with a Bicycle Robot]]

![[assets/2611.15280_figure.png|800]]

- **arXiv**: [2611.15280](https://arxiv.org/abs/2611.15280)
- **PDF**: https://arxiv.org/pdf/2611.15280
- **详细分析**: [[20_Research/Papers/具身智能/Autonomous_Trail_Racing_with_a_Bicycle_Robot|Autonomous Trail Racing with a Bicycle Robot]]
- **作者**: Fabian Jenelten, Deepana Ishtaweera, Pablo Garcia, Liana Margolese, Igor Bogoslavskyi, Luca Buonocore, Jan Migliazza, Aleksandrs Ecins, Annika Wollschlaeger, Dario Bellicoso, Gabriel Nelson, Abel Gawel...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.6，大模型 0.1，机器人 1.1）
- **关联关键词**: LLM, Robotics, EmbodiedAI

#### 研究背景与动机

《Autonomous Trail Racing with a Bicycle Robot》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Navigating off-road trails on a mountain bike requires diverse locomotion skills, including aerial maneuvers, cornering, and slip recovery, paired with sophisticated perception for scene understanding. Translating these capabilities to autonomous, two-wheeled robots remains a formidable challenge. We show that autonomous, high-speed trail navigation can be achieved through a single idea: encoding the trail as a semantic layer of the terrain. In simulation, this layer embeds the navigation task into the training environment; during deployment, it is reconstructed onboard from camera and LiDAR data. First, we introduce a unified learning framework that treats local navigation and locomotion as a joint optimization problem, bypassing the twist or pose command interface of classical control hierarchies. With fixed reward weights, the same framework produces both trail racing and agile parkour, shaped only through terrain semantics and episode length. Second, our perception pipeline combines a frozen vision foundation model with a lightweight dual-head decoder that predicts per-pixel terrain semantics and confidence scores, which are fused with LiDAR range measurements into an egocentric semantic elevation map at 30 Hz onboard an NVIDIA AGX Orin. We validate our framework on the Ultra Mobility Vehicle (UMV), a bicycle robot that autonomously raced across all sections of a kilometer-long, unstructured mountain bike trail at speeds exceeding 5 m/s and averaging 3.26 m/s. In simulation, our policy fails up to an order of magnitude less often than hierarchical baselines while driving faster.

</details>

---

### [[20_Research/Papers/具身智能/DroneDiffusion_Uncertainty-Guided_Diffusion_Path_Planner_for_UAV_Navigation|DroneDiffusion: Uncertainty-Guided Diffusion Path Planner for UAV Navigation]]

![[assets/2611.15277_figure.png|800]]

- **arXiv**: [2611.15277](https://arxiv.org/abs/2611.15277)
- **PDF**: https://arxiv.org/pdf/2611.15277
- **详细分析**: [[20_Research/Papers/具身智能/DroneDiffusion_Uncertainty-Guided_Diffusion_Path_Planner_for_UAV_Navigation|DroneDiffusion: Uncertainty-Guided Diffusion Path Planner for UAV Navigation]]
- **作者**: Ivan Valuev, Iana Zhura, Valerii Serpiva, Miguel Altamirano Cabrera, Dzmitry Tsetserukou
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Multimodal, EmbodiedAI, ComputerVision

#### 研究背景与动机

《DroneDiffusion: Uncertainty-Guided Diffusion Path Planner for UAV Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：U-Net。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present DroneDiffusion, a perception-aware diffusion planner for local 3-D UAV trajectory generation that explicitly models and avoids failure zones caused by lens flare, overexposure, and reflective surfaces. A vision-language perceptual safety estimator produces a pixel-aligned reliability map that highlights regions of degraded sensing. A denoising diffusion probabilistic model (DDPM) is conditioned on this map together with the onboard RGB image, goal point, and initial velocity to generate egocentric 3-D trajectories. To enforce obstacle avoidance at inference time without retraining, we apply training-free CHOMP guidance over a 3-D Euclidean signed distance field. The model is trained entirely in simulation and deployed zero-shot on a real drone. Reliability conditioning raises the mean perceptual reliability along generated trajectories to 0.71, compared with 0.63 for a geometric baseline, while guidance halves the collision rate of the learned prior from 14.7% to 7.8%. Perceptual safety conditioning and geometric guidance are therefore complementary: treating sensor reliability as a first-class signal reduces incursions into unreliable regions while maintaining competitive navigation performance.

</details>

---

### [[20_Research/Papers/具身智能/PolyMorphWBC_Whole-Body_Control_from_End-Effector_Trajectories_for_Quadrupedal_Mobile_Manipulation_across_Arm_Morphologies_with_Extended_Rea|PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach]]

![[assets/2611.15117_figure.png|800]]

- **arXiv**: [2611.15117](https://arxiv.org/abs/2611.15117)
- **PDF**: https://arxiv.org/pdf/2611.15117
- **详细分析**: [[20_Research/Papers/具身智能/PolyMorphWBC_Whole-Body_Control_from_End-Effector_Trajectories_for_Quadrupedal_Mobile_Manipulation_across_Arm_Morphologies_with_Extended_Rea|PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach]]
- **作者**: Heng Li, Yang Li, Yifan Duan, Ren Fang, Matao Duan, Wenhao Yu, Lu Zhang, Jianmin Ji, Yanyong Zhang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, Systems

#### 研究背景与动机

《PolyMorphWBC: Whole-Body Control from End-Effector Trajectories for Quadrupedal Mobile Manipulation across Arm Morphologies with Extended Reach》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Quadrupedal mobile manipulators can extend their manipulation workspace by coordinating the mounted arm with the mobile base. At the task level, short-horizon end-effector (EE) trajectories provide an interface for specifying the desired manipulation motion without prescribing how it should be realized by the arm and base. However, executing such trajectories remains challenging because the controller must determine when and how the base should move, and this decision depends on the mounted-arm morphology. We therefore present PolyMorphWBC, a hierarchical controller that takes an EE trajectory as the sole task-level motion command and generates coordinated arm--base motions across four families of 6-DoF mounted arms, with extended-reach trajectories beyond the initial fixed-base reach. Within PolyMorphWBC, a trajectory-conditioned coordinator determines the base motion from previewed EE targets, while arm-specific Inverse Kinematics (IK) tracks the current target, and a frozen locomotion backend executes the resulting motion. Cross-arm reuse is enabled by a Unified Robot Description Format (URDF)-derived morphology conditioning, together with online residual-wrench feedback. We train PolyMorphWBC on procedurally generated arms and structured trajectories within and beyond fixed-base reach. In IsaacLab, it achieves 93.95% completion with 2.30cm position error and 4.81° orientation error on held-out trajectories and arm morphologies. In MuJoCo evaluation against UMI-on-Legs, PolyMorphWBC reduces EE position error by 69--72% and orientation error by 91--97% across four within- and extended-reach trajectories. On a physical Go2--ARX5 system, we demonstrate language-conditioned extended-reach pick-and-place using EE trajectories from pi_0 without vision-language-action (VLA)-generated base commands.

</details>

---

### [[20_Research/Papers/强化学习/Elastra_A_Simulation_Framework_for_Elastic_Bodies|Elastra: A Simulation Framework for Elastic Bodies]]

![[assets/2611.15112_figure.png|800]]

- **arXiv**: [2611.15112](https://arxiv.org/abs/2611.15112)
- **PDF**: https://arxiv.org/pdf/2611.15112
- **详细分析**: [[20_Research/Papers/强化学习/Elastra_A_Simulation_Framework_for_Elastic_Bodies|Elastra: A Simulation Framework for Elastic Bodies]]
- **作者**: Youran Sun, Chugang Yi, Xingyu Ren, Haizhao Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，强化学习 0.2，机器人 0.7）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《Elastra: A Simulation Framework for Elastic Bodies》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

When robots interact with elastic surfaces such as mattresses and trampolines, changes in loading cause the surfaces to deform and rebound, altering subsequent contact locations and forces. We present Elastra, a simulation framework for modeling this interaction and supporting the training and evaluation of robot control policies. Elastra represents each surface using elements that move only vertically, with elastic connections and damping to model deformation and recovery. Contact forces drive surface motion, and the updated surface geometry is used to compute subsequent contact forces. We systematically validate our simulations against an independent implementation and a real mattress load curve. We further use Elastra to train the Unitree G1 humanoid to stand up on mattresses and trampolines. Using the pretrained HoST policy and ProtoMotions motion tracker as original controllers, we train residual policies through reinforcement learning to add corrections to their joint targets. Adding these residual policies increases the success rate with HoST from 44.1\% to 72.5\%, and from 55\% to 89\% on the trampoline. With ProtoMotions, the success rate increases from 19.0\% to 45.0\% for initial poses not encountered during training. The code and video are available on https://github.com/yichg/elastra.

</details>

---

### [[20_Research/Papers/具身智能/Decide_Before_You_Move_Diffusion-Generated_Search_Reference_for_Zero-Shot_Open-Vocabulary_Object_Navigation_in_Semi-Static_Environments|Decide Before You Move: Diffusion-Generated Search Reference for Zero-Shot Open-Vocabulary Object Navigation in Semi-Static Environments]]

![[assets/2611.15093_figure.png|800]]

- **arXiv**: [2611.15093](https://arxiv.org/abs/2611.15093)
- **PDF**: https://arxiv.org/pdf/2611.15093
- **详细分析**: [[20_Research/Papers/具身智能/Decide_Before_You_Move_Diffusion-Generated_Search_Reference_for_Zero-Shot_Open-Vocabulary_Object_Navigation_in_Semi-Static_Environments|Decide Before You Move: Diffusion-Generated Search Reference for Zero-Shot Open-Vocabulary Object Navigation in Semi-Static Environments]]
- **作者**: Yuxuan Feng, Fujing Xie, Sören Schwertfeger, Hermann Blum
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.0（加权：具身智能 1.2，大模型 0.3，机器人 0.5）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Decide Before You Move: Diffusion-Generated Search Reference for Zero-Shot Open-Vocabulary Object Navigation in Semi-Static Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-world navigation requires a robot to locate a user-specified target in an indoor scene under open-vocabulary queries. Realistic indoor environments are semi-static: walls and furniture largely persist while smaller objects move, relocate, or vanish between visits. Prior-map systems answer queries from object poses recorded at reconstruction time, which expire as soon as objects move, whereas online methods re-derive where to look from current observations every few steps, often through expensive calls to a vision--language model. Assuming that walls and large furniture do not move, we keep their map to plan paths, but use a target--furniture co-occurrence prior to decide where to search. We present PreNav, an ObjectNav framework on semi-static environments. Rather than invoking a vision-language model at each step, PreNav generates a single global search reference before the robot moves: an LLM converts target--furniture co-occurrence into a spatial prior, a conditional diffusion model turns that prior and the persistent structure into an ordered centerline with a band around it, and the robot approaches the target once it is detected online. Experiments on a Gibson ObjectNav benchmark show that PreNav outperforms a strong online baseline under matched structural priors, using a generator trained only on room-level ScanNet++ scenes and applied to floor-level Gibson without fine-tuning. Real-world experiments under object relocation and open-vocabulary queries further validate the approach.

</details>

---

### [[20_Research/Papers/机器人/MiniPose_Miniature-Based_Real_Data_Collection_for_6D_Pose_Estimation_of_Large_Industrial_Pipe_Segments|MiniPose: Miniature-Based Real Data Collection for 6D Pose Estimation of Large Industrial Pipe Segments]]

![[assets/2611.15066_figure.jpg|800]]

- **arXiv**: [2611.15066](https://arxiv.org/abs/2611.15066)
- **PDF**: https://arxiv.org/pdf/2611.15066
- **详细分析**: [[20_Research/Papers/机器人/MiniPose_Miniature-Based_Real_Data_Collection_for_6D_Pose_Estimation_of_Large_Industrial_Pipe_Segments|MiniPose: Miniature-Based Real Data Collection for 6D Pose Estimation of Large Industrial Pipe Segments]]
- **作者**: Hyunjun Kim, Youngjin Seo, Sungwon Seo, Jiyou Shin, Kunwoo Kim, Chanyong Park, Hyungpil Moon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《MiniPose: Miniature-Based Real Data Collection for 6D Pose Estimation of Large Industrial Pipe Segments》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：PointNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

6-DOF pose estimation of large and heavy industrial objects, such as large piping systems in shipyards and structural components in petrochemical plants, remains relatively underexplored in robotic perception. Repeatedly repositioning large objects is physically and spatially demanding, making it difficult to acquire real training data with sufficient pose diversity. Synthetic data offer a scalable alternative, but faithfully reproducing real RGB-D observations, particularly the structured measurement errors of real depth sensors, remains difficult. We propose MiniPose, a practical pipeline for miniature-based real RGB-D data collection that addresses both the data-acquisition burden and the sim-to-real gap. We fabricate a scaled-down replica and capture RGB-D data of it in diverse poses using a real RGB-D camera. RGB images are used directly, while depth maps are converted to a geometrically consistent representation of the full-scale object via a simple inverse scaling transformation. This allows training to incorporate real appearance and sensor measurement characteristics that are difficult to reproduce using synthetic data alone. To examine whether the benefit depends on a particular network, we evaluate two RGB-D pose estimators with different formulations, PVN3D and RDPN6D. Mixing at most 1,000 miniature images per pipe type, less than 10\% of the training data, with 10,000 synthetic images improves the mean ADD-S AUC across pipe types over synthetic-only training for both estimators. A comparison with training on full-scale real data further suggests that miniature data can serve as a proxy where full-scale collection is difficult, reducing the data-collection burden for large industrial objects.

</details>

---

### [[20_Research/Papers/具身智能/Does_Your_World_Model_Know_Actions_Have_Consequences|Does Your World Model Know Actions Have Consequences?]]

![[assets/2611.15048_figure.png|800]]

- **arXiv**: [2611.15048](https://arxiv.org/abs/2611.15048)
- **PDF**: https://arxiv.org/pdf/2611.15048
- **详细分析**: [[20_Research/Papers/具身智能/Does_Your_World_Model_Know_Actions_Have_Consequences|Does Your World Model Know Actions Have Consequences?]]
- **作者**: Ayush Gaggar, Jared Berry, Todd D. Murphey
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 0.6，世界模型 0.8，机器人 0.3）
- **关联关键词**: EmbodiedAI, WorldModel, Systems

#### 研究背景与动机

《Does Your World Model Know Actions Have Consequences?》归入 世界模型、具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Embodied world models (WMs) are implicit learning systems that predict the next future latent state directly from observations and actions. Unique from other end-to-end learning systems, the dynamics predictor of WMs can simulate the environment's response to alternative actions without physical deployment nor pre-specifying states of the dynamical system. Current metrics focus on the quality of model outputs, e.g., clarity of reconstructions or task success, but fail to assess the fidelity of modeling consequences of counterfactual actions. Inspecting the forced response to action perturbations through sensitivity analysis is one way to audit how well WMs can predict the consequences of counterfactual actions. Deploying WMs on hardware will require new evaluation frameworks to analyze the tradeoffs between state error and accurate sensitivity prediction.

</details>

---

### [[20_Research/Papers/机器人/ILA_A_Transferable_Interface-Level_Adapter_for_Compliant_Humanoid_Motion_Tracking|ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking]]

![[assets/2611.14985_figure.png|800]]

- **arXiv**: [2611.14985](https://arxiv.org/abs/2611.14985)
- **PDF**: https://arxiv.org/pdf/2611.14985
- **详细分析**: [[20_Research/Papers/机器人/ILA_A_Transferable_Interface-Level_Adapter_for_Compliant_Humanoid_Motion_Tracking|ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking]]
- **作者**: ZhuoChang Cai, Zihao Yan, Jinxuan Zhu, Yanjie Li, Hao Xiong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics

#### 研究背景与动机

《ILA: A Transferable Interface-Level Adapter for Compliant Humanoid Motion Tracking》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid motion tracking is fundamental to reproducing human motions on humanoid robots and serves as an important tool for teleoperation and motion data collection. However, directly tracking reference motions can be unsafe in constrained environments or during physical human--robot interaction, motivating the need for compliant motion tracking. We present ILA, an Interface-Level Adapter for compliant humanoid motion tracking without dedicated interaction sensors. ILA adapts motion references from the robot's observation history, allowing the robot to respond to physical guidance while preserving the capabilities of a pretrained motion tracker. As an interface-level module, ILA can be directly plugged into different pretrained motion trackers without retraining either the adapter or the tracking policies. ILA is trained entirely in simulation to predict reference corrections induced by physical interaction. We evaluate ILA with three humanoid motion trackers and achieve a 63.6--75.4% reduction in guidance-target error compared with their original policies. Matched simulation studies and hardware experiments further show that ILA improves responsiveness to human guidance while preserving nominal motion-tracking performance. These results demonstrate compliant guidance as a reusable, sensor-free extension to pretrained humanoid motion trackers.

</details>

---

### [[20_Research/Papers/强化学习/From_a_Single_RGB_Image_to_Robot_Execution_Metric_Scene_Alignment_and_Contact-Guided_Retargeting|From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting]]

![[assets/2611.14981_figure.png|800]]

- **arXiv**: [2611.14981](https://arxiv.org/abs/2611.14981)
- **PDF**: https://arxiv.org/pdf/2611.14981
- **详细分析**: [[20_Research/Papers/强化学习/From_a_Single_RGB_Image_to_Robot_Execution_Metric_Scene_Alignment_and_Contact-Guided_Retargeting|From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting]]
- **作者**: Zhenxuan Ding, Yu Huang, Xinmiao Wang, Chenghao Sun, Ziyang Dong, Wenhao Cui
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.9（加权：具身智能 0.6，机器人 1.3）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《From a Single RGB Image to Robot Execution: Metric Scene Alignment and Contact-Guided Retargeting》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Extending humanoid interaction generation to new environments remains limited by the need for prebuilt 3D scene assets. Reconstructing scenes directly from single RGB images offers a way to overcome this limitation, but introduces a key challenge in maintaining geometric consistency throughout motion generation and transfer. Visually plausible human motions may be misaligned with the reconstructed scene, while retargeting can introduce additional support errors due to differences between human and robot embodiments. We present a unified pipeline that transforms a single RGB image into a humanoid motion reference. It reconstructs scene geometry from the input image, generates a human interaction conditioned on the reconstructed scene, and retargets the motion to a humanoid robot. To maintain geometric consistency throughout this process, we incorporate two complementary refinement stages before and after embodiment transfer. Before retargeting, Joint Metric Interaction Refinement (JMIR) refines human motion alignment with the registered metric scene while preserving the generated interaction structure. Following retargeting, Contact Guided Residual Retargeting (CGRR) corrects robot specific support errors to restore the intended support relationships. Together, these stages produce motion references that are consistent with the reconstructed scene and can be followed by multiple pretrained humanoid trackers without scene specific policy fine tuning. Compared with GRAIL, our method reduces refinement time from 480 s to 87 s, yielding a speedup of 5.5 times. The complete pipeline achieves a success rate of 89% in simulation and 70% across 50 physical trials on the Unitree G1, demonstrating its effectiveness in generating executable humanoid motion references from single RGB images.

</details>

---

### [[20_Research/Papers/机器人/DIVAL_Diffeomorphic_Vector-Field_Alignment_for_Nonholonomic_Motion_Planning|DIVAL: Diffeomorphic Vector-Field Alignment for Nonholonomic Motion Planning]]

![[assets/2611.14918_figure.png|800]]

- **arXiv**: [2611.14918](https://arxiv.org/abs/2611.14918)
- **PDF**: https://arxiv.org/pdf/2611.14918
- **详细分析**: [[20_Research/Papers/机器人/DIVAL_Diffeomorphic_Vector-Field_Alignment_for_Nonholonomic_Motion_Planning|DIVAL: Diffeomorphic Vector-Field Alignment for Nonholonomic Motion Planning]]
- **作者**: Yike Qiao, Xiaodong He, An Zhuo, Zhiyong Sun, Weimin Bao, Zhongkui Li
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《DIVAL: Diffeomorphic Vector-Field Alignment for Nonholonomic Motion Planning》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventional vector-field-based motion planners for nonholonomic robots consist of two steps: first designing a nominal vector field and then controlling the robot to follow it to approach the target. However, a nonholonomic robot cannot follow the vector field instantaneously and may collide with obstacles, due to the inevitable mismatch between the robot's initial heading and the vector field's direction. This paper proposes a diffeomorphic vector-field alignment (DIVAL) method, which aligns the vector field's direction with the robot's initial heading so the robot can follow the vector field from the start. Specifically, the nominal vector field is locally reshaped by applying a diffeomorphic deformation to the workspace, such that the reshaped vector field has the same direction as the robot's heading at the initial position and coincides with the nominal vector field outside the deformed region. Since DIVAL eliminates the initial heading mismatch, the nonholonomic robot can maintain heading alignment with the reshaped vector field throughout the motion. This heading alignment further ensures that the robot preserves the nominal vector field's properties, including obstacle avoidance, convergence to the target, and smooth control signals. Numerical simulations provide vector-field-tracking baselines where the nominal vector fields are reshaped with DIVAL. Compared to the original baselines, the proposed method achieves collision-free convergence in all trials and avoids control discontinuities. Hardware experiments on a ground vehicle further demonstrate collision-free convergence across different targets and initial conditions under real-world disturbances.

</details>

---

### [[20_Research/Papers/具身智能/SunLightBots_Turning_sunlight_into_self-sustained,_high-power_motion_in_soft_robots|SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots]]

![[assets/2611.14729_figure.png|800]]

- **arXiv**: [2611.14729](https://arxiv.org/abs/2611.14729)
- **PDF**: https://arxiv.org/pdf/2611.14729
- **详细分析**: [[20_Research/Papers/具身智能/SunLightBots_Turning_sunlight_into_self-sustained,_high-power_motion_in_soft_robots|SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots]]
- **作者**: Yoo Jin Lee, Melanie Torres Crespo, Zhongxiao Deng, Andrew Tejada-Vega, Rebecca Kramer-Bottiglio, Wenzhong Yan, Yimin Luo
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.2（加权：具身智能 0.9，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI, Systems

#### 研究背景与动机

《SunLightBots: Turning sunlight into self-sustained, high-power motion in soft robots》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Soft robots built from active materials can directly convert environmental stimuli into motion, offering a route to energy autonomy and embodied control. However, environmental energy is generally harvested at low power, whereas rapid, mechanically demanding actions require high mechanical output power. Reconciling this mismatch while sustaining self-regulated cyclic actuation is challenging, particularly at the subgram scale, where limited payload capacity constrains the integration of conventional power and control hardware. Here, we present SunLightBots, a class of subgram, sunlight-powered, untethered soft robots that achieve autonomous locomotion under continuous illumination near 1 Sun (100 mW/cm2). Their operation is enabled by a self-resetting snapping (SRS) mechanism that integrates liquid crystal elastomers (LCEs) with snap-through instability to accumulate solar energy supplied at low power, release it as rapid, high-power motion, and reset through photothermal-mechanical feedback. Through coordinated optimization of the LCE actuation temperature, photothermal conversion, actuation stress, and structural energy barrier, the system operates near 1 Sun and achieves a peak mass-specific mechanical power of 89 W/kg. At this irradiance, the optimized LCE generates an actuation stress of 0.1 MPa at approximately 60 deg C. SunLightBots demonstrate sustained swimming, crawling, and repeated impulsive jumping. Under 1.5 Suns, the swimmer advances more than three body lengths per cycle. This work provides a materials-mechanics route toward autonomous soft robots powered entirely by the environment.

</details>

---

### [[20_Research/Papers/机器人/Terrain-Aware_Thompson_Sampling_for_Multi-Drone_Search_and_Rescue|Terrain-Aware Thompson Sampling for Multi-Drone Search and Rescue]]

![[assets/2611.14685_figure.png|800]]

- **arXiv**: [2611.14685](https://arxiv.org/abs/2611.14685)
- **PDF**: https://arxiv.org/pdf/2611.14685
- **详细分析**: [[20_Research/Papers/机器人/Terrain-Aware_Thompson_Sampling_for_Multi-Drone_Search_and_Rescue|Terrain-Aware Thompson Sampling for Multi-Drone Search and Rescue]]
- **作者**: Riana Gagnon Souleiman, Giovanni Beltrame
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.6（加权：具身智能 0.3，大模型 0.2，机器人 1.1）
- **关联关键词**: Agent, ComputerVision

#### 研究背景与动机

《Terrain-Aware Thompson Sampling for Multi-Drone Search and Rescue》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

In this work, we propose a decentralized terrain-aware multi-drone Thompson Sampling algorithm tailored for search and rescue (SAR) applications. A probability distribution of locating a lost person is informed by terrain data, using established SAR models (displacement ring, elevation, watershed, dispersion angle, and track offset) derived from historical SAR case data on lost person behavior. Exploration is conducted by a team of drones using Thompson Sampling, where candidate actions are selected by drawing samples from this probability distribution, represented by a per-cell Gaussian posterior whose mean and variance are updated through Bayesian inference. This approach balances exploration of uncertain regions with exploitation of high-probability areas to locate a lost person. Observation uncertainty is incorporated through fractional forest coverage, which measures the percentage of an observation occluded by tree coverage and accounts for reduced detection performance in densely vegetated areas. Simulations using real SAR case data (YOSAR) evaluate the proposed method against a coverage planner and a probabilistic active search method in search regions of 1.5 and 3.8 square kilometers, with 5, 10, 15, and 20 agents flying at 50 km/hr. We demonstrate that our method achieves a success rate of approximately 87% within 60 to 247 seconds in the 1.5 square kilometer region, and success rates of approximately 75% to 91% within 161 to 466 seconds in the 3.8 square kilometer region, across different agent configurations.

</details>

---
