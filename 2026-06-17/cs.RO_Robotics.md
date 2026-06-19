# cs.RO | Robotics | 2026-06-17

#arxiv #ComputerScience

**论文数**: 15

### [[20_Research/Papers/机器人/EBench_Elemental_Diagnosis_of_Generalist_Mobile_Manipulation_Policies|EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies]]

![[assets/2606.18239_figure.png|800]]

- **arXiv**: [2606.18239](https://arxiv.org/abs/2606.18239)
- **PDF**: https://arxiv.org/pdf/2606.18239
- **详细分析**: [[20_Research/Papers/机器人/EBench_Elemental_Diagnosis_of_Generalist_Mobile_Manipulation_Policies|EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies]]
- **作者**: Ning Gao, Jinliang Zheng, Xing Gao, Haoxiang Ma, Hanqing Wang, Yukai Wang, Jiantong Chen, Zanxin Chen, Shujie Zhang, Mingda Jia, Xuekun Jiang, Zihou Zhu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 0.9（加权：具身智能 0.6，机器人 0.3）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《EBench: Elemental Diagnosis of Generalist Mobile Manipulation Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：EBench, InternVLA, IsaacSim, OpenVLA, RLBench, RMBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present EBench, a simulation benchmark that diagnoses generalist mobile manipulation policies beyond a single success-rate scalar. EBench comprises 26 diverse and challenging manipulation tasks annotated along 5 capability dimensions and 4 generalization dimensions. We evaluate state-of-the-art generalist manipulation models including $\pi_0$, $\pi_{0.5}$, XVLA, and InternVLA-A1, and reveal that models with near success rates exhibit strikingly different capability profiles: $\pi_{0.5}$ achieves the highest test success rate and the best train--test retention, whereas InternVLA-A1 dominates mobile manipulation but collapses on dexterous tasks, and XVLA exhibits strengths on a disjoint set of atomic skills compared to other policies. Beyond capability profiling, EBench analyzes the generalization ability from 4 representative perspectives, identifying the impact of different distribution shift factors. The results reveal strengths and weaknesses of models behind an overall score. We hope this benchmark offers a broad set of diagnostic signals to guide iteration on generalist manipulation models.

</details>

---

### [[20_Research/Papers/世界模型/Beyond_Failure_Recovery_An_Engagement-Aware_Human-in-the-loop_Framework_for_Robotic_Systems|Beyond Failure Recovery: An Engagement-Aware Human-in-the-loop Framework for Robotic Systems]]

![[assets/2606.18189_figure.png|800]]

- **arXiv**: [2606.18189](https://arxiv.org/abs/2606.18189)
- **PDF**: https://arxiv.org/pdf/2606.18189
- **详细分析**: [[20_Research/Papers/世界模型/Beyond_Failure_Recovery_An_Engagement-Aware_Human-in-the-loop_Framework_for_Robotic_Systems|Beyond Failure Recovery: An Engagement-Aware Human-in-the-loop Framework for Robotic Systems]]
- **作者**: Jiaying Fang, Joyce Yang, Zhanxin Wu, Bohan Yang, Tapomayukh Bhattacharjee
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 世界模型
- **相关性评分**: 1.8（加权：具身智能 0.3，世界模型 0.2，机器人 1.3）
- **关联关键词**: Robotics, WorldModel, Systems

#### 研究背景与动机

《Beyond Failure Recovery: An Engagement-Aware Human-in-the-loop Framework for Robotic Systems》归入 机器人、具身智能、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Conventional human-in-the-loop approaches typically involve users only when a robot encounters failure or uncertainty, treating humans primarily as tools for improving robot performance. However, in many human-centered robotics settings, interaction should support engagement by keeping users involved in decision-making rather than limiting them to failure-driven interventions. This is particularly compelling in physical caregiving, where mobility limitations can reduce users' ability to intervene or modulate the robot's behavior in the moment. As a result, failure-driven interaction policies may relegate users to passive observers for long stretches of the task. For example, a user with mobility limitations may feel less engaged when being continuously and passively fed by a robot. At the same time, overly frequent interaction can be tiring and increase the user's workload. To address this trade-off, we propose Engagement-aware MPC (E-MPC), a user-engagement-aware method that plans interaction to maintain engagement while respecting a workload constraint. E-MPC leverages a user interaction dynamics model that captures how user engagement evolves as a function of both the frequency and type of interaction. Rather than requesting input only when difficulties arise during task execution, the robot proactively considers the user's preferred level of engagement throughout the task, balancing autonomy and interaction while ensuring task success. We evaluate E-MPC in simulation with several ablations and baseline comparisons. Results demonstrate the effectiveness of our approach across diverse user personas. In addition, we conduct a real-world user study with participants with emulated mobility limitations on a robot-assisted bite acquisition system, showing that E-MPC improves user experience while maintaining task success.

</details>

---

### [[20_Research/Papers/具身智能/WireCraft_A_Simulation_Benchmark_for_Industrial_DLO_Manipulation|WireCraft: A Simulation Benchmark for Industrial DLO Manipulation]]

![[assets/2606.18097_figure.png|800]]

- **arXiv**: [2606.18097](https://arxiv.org/abs/2606.18097)
- **PDF**: https://arxiv.org/pdf/2606.18097
- **详细分析**: [[20_Research/Papers/具身智能/WireCraft_A_Simulation_Benchmark_for_Industrial_DLO_Manipulation|WireCraft: A Simulation Benchmark for Industrial DLO Manipulation]]
- **作者**: Chongyu Zhu, Ramy ElMallah, Hyegang Kim, Zachary Tang, Jiachen Rao, Artem Arutyunov, Seungyeon Ha, Chi-Guhn Lee
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 1.7（加权：具身智能 1.2，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《WireCraft: A Simulation Benchmark for Industrial DLO Manipulation》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：DaXBench, ManipulationNet, RLBench, Real-World, SoftGym。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Deformable Linear Objects (DLOs), such as wires and cables, are central to industrial assembly. Unlike rigid objects, whose state is captured by a 6-DoF pose, DLOs have an infinite-dimensional configuration space and deform continuously under contact with grippers, fixtures, and the workspace, making them a demanding benchmark for general dexterous manipulation. Despite their importance, policy development and comparison remain difficult: existing benchmarks are often tied to specific hardware setups, lack modular and customizable task assets, or study generic deformable-object tasks without the fixtures relevant to real-world industrial wire manipulation. Few benchmarks align simulation, real-world data, and shared evaluation protocols. To bridge this gap, we introduce WireCraft, a simulation benchmark for industrial DLO manipulation with configurable difficulty and assets, spanning three task families: connector insertion, clip routing, and channel seating. It supports two complementary DLO physics models, articulated and deformable, and the trajectories come from both simulation and a physical UR5. We benchmark reinforcement learning (RL), imitation learning (IL), and vision-language-action (VLA) policies under shared metrics. Privileged state-based RL solves a representative setting in each task family with over 82\% success, confirming the tasks are well-posed. For connector insertion, however, the transition from reaching the socket to contact-rich alignment remains a key bottleneck for vision RL, IL, and VLA policies. These results indicate that industrial DLO manipulation, though tractable under privileged state, remains an open challenge for current vision-based learning. The benchmark, data, and tools will be open-sourced upon acceptance.

</details>

---

### [[20_Research/Papers/具身智能/ThinkingVLA_Interleaved_Vision_and_Language_Reasoning_for_Robotic_Manipulation|ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation]]

> 主图未能自动提取，需后续人工补图。

- **arXiv**: [2606.17937](https://arxiv.org/abs/2606.17937)
- **PDF**: https://arxiv.org/pdf/2606.17937
- **详细分析**: [[20_Research/Papers/具身智能/ThinkingVLA_Interleaved_Vision_and_Language_Reasoning_for_Robotic_Manipulation|ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation]]
- **作者**: Tianyi Lu, Hui Zhang, Zijie Diao, Junke Wang, Shengqi Xu, Xingyao Lin, Guojin Zhong, Ziyi Ye, Peng Wang, Zuxuan Wu, Yu-Gang Jiang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.7（加权：具身智能 1.8，机器人 0.9）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《ThinkingVLA: Interleaved Vision and Language Reasoning for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：ThinkingVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Most Vision-Language-Action (VLA) models map observations directly to actions without explicit reasoning, limiting their capacity for reasoning-intensive long-horizon tasks. To address this, existing approaches adopt Chain-of-Thought (CoT) reasoning to enable subgoal decomposition and spatial anticipation. However, those methods lack a unified architecture for effective cross-modal reasoning and fail to explicitly include inverse reasoning ability based on the target state. We argue that manipulation planning naturally decomposes into prediction, anticipating the next visual state, and inverse dynamics, inferring the actions to reach it. Bridging both requires a unified autoregressive architecture that interleaves textual and visual reasoning in a single generation process. We propose \textbf{ThinkingVLA}, a generative model that realizes this decomposition within a unified Mixture-of-Transformers architecture. ThinkingVLA consists of a forward CoT that identifies the immediate subgoal and guides the visual forecasting; the predicted image then serves as the target state, grounding an inverse CoT that reasons about spatial relationships and action intent based on the predicted image; and the final action is generated conditioned on this full reasoning context. Extensive experiments on simulation and real-world benchmarks demonstrate that ThinkingVLA consistently outperforms state-of-the-art baselines, with particularly large gains on long-horizon manipulation tasks.

</details>

---

### [[20_Research/Papers/强化学习/WAM-RL_World-Action_Model_Reinforcement_Learning_with_Reconstruction_Rewards_and_Online_Video_SFT|WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT]]

![[assets/2606.17906_figure.png|800]]

- **arXiv**: [2606.17906](https://arxiv.org/abs/2606.17906)
- **PDF**: https://arxiv.org/pdf/2606.17906
- **详细分析**: [[20_Research/Papers/强化学习/WAM-RL_World-Action_Model_Reinforcement_Learning_with_Reconstruction_Rewards_and_Online_Video_SFT|WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT]]
- **作者**: Zezhong Qian, Xiaowei Chi, Yu Qi, Haozhan Li, Zhi Yang Chen, Shanghang Zhang
- **cs 子类**: cs.RO
- **归属领域**: 强化学习
- **相关领域**: 强化学习, 世界模型
- **相关性评分**: 1.0（加权：强化学习 0.8，世界模型 0.2）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《WAM-RL: World-Action Model Reinforcement Learning with Reconstruction Rewards and Online Video SFT》归入 强化学习、世界模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 强化学习、世界模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：GR-RL, RIPT-VLA, RLBench, SimpleVLA-RL, TwinRL-VLA, WAM-RL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recent World-Action (WA) models demonstrate strong generalization ability and data efficiency, but they typically rely on expert trajectories for training. This reliance limits their ability to acquire fine-grained manipulation skills beyond the demonstration distribution and prevents them from continuously improving through real-world interaction. To address these limitations, we propose WAM-RL, a reinforcement learning framework that enables joint optimization of the world model and the action model through online interaction with the environment. By allowing the two components to co-evolve, our approach enhances fine-grained control and adaptability. Specifically, a WA model consists of a world model and an actor. We design a tailored reinforcement learning method with hierarchical optimization to coordinate their improvement. On the methodological side, we systematically investigate the effects of applying reinforcement learning to the action model, as well as online training of the world model within an RL setting. Our experiments reveal a key insight: optimizing only the actor yields improvements on short-horizon tasks, but fails to provide significant gains on long-horizon tasks. In contrast, jointly optimizing both the world model and the actor is critical for achieving strong performance in long-horizon settings. Our work is the first to introduce reinforcement learning into the World-Action paradigm, and provides insights into how online optimization of both the action head and the world model impacts overall performance.

</details>

---

### [[20_Research/Papers/强化学习/HumanoidArena_Benchmarking_Egocentric_Hierarchical_Whole-body_Learning|HumanoidArena: Benchmarking Egocentric Hierarchical Whole-body Learning]]

![[assets/2606.17833_figure.png|800]]

- **arXiv**: [2606.17833](https://arxiv.org/abs/2606.17833)
- **PDF**: https://arxiv.org/pdf/2606.17833
- **详细分析**: [[20_Research/Papers/强化学习/HumanoidArena_Benchmarking_Egocentric_Hierarchical_Whole-body_Learning|HumanoidArena: Benchmarking Egocentric Hierarchical Whole-body Learning]]
- **作者**: Taowen Wang, Zikang Xie, Bin Yang, Yunheng Wang, Zizhao Yuan, Yuetong Fang, Yixiao Feng, Yichi Wang, Xingyu Chen, Haodong Chen, Qiwei Wu, Weisheng Xu...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: RL, Systems

#### 研究背景与动机

《HumanoidArena: Benchmarking Egocentric Hierarchical Whole-body Learning》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：AgentWorld, HumanoidBench, HumanoidVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots promise whole-body interaction in human-centered environments, but scalable policy learning remains difficult because task-level decision-making and whole-body dynamic execution are tightly coupled. A practical solution is hierarchical control, where a high-level policy predicts intermediate whole-body actions and low-level general motion trackers (GMTs) execute them as stable humanoid motion. However, existing benchmarks rarely evaluate the policy-tracker interface itself, leaving open whether intermediate whole-body actions are executable, robust under task distribution shifts, and transferable across different GMT backends. We introduce HumanoidArena, a simulation-first benchmark for egocentric hierarchical whole-body learning. The benchmark formulates policy learning as a hierarchical decision making problem: a high-level policy converts egocentric vision, proprioception, and instructions into a compact whole-body action, which is subsequently executed by a low-level GMT. Instead of treating the legs as planar transport tools, HumanoidArena emphasizes interactions where lower-body coordination is structurally necessary in task completion. We therefore design 7 leg-critical HOI/HSI tasks in which success requires foot placement, balance maintenance, posture adjustment, and whole-body reorientation. To further diagnose the hierarchical system, we evaluate policies from two complementary perspectives: perturbation-conditioned generalization and GMT-conditioned transfer. Experiments show that hierarchical control enables learned policies to solve diverse leg-critical interactions, but performance is strongly tracker-conditioned and cross-GMT transfer remains fragile. These results position HumanoidArena as a benchmark for studying transferable intermediate action representations and scalable egocentric whole-body policy learning.

</details>

---

### [[20_Research/Papers/具身智能/FLAP_FOV-Constrained_Active_Perception_Planning_for_Prior-Map-Free_3D_Navigation|FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation]]

![[assets/2606.17630_figure.png|800]]

- **arXiv**: [2606.17630](https://arxiv.org/abs/2606.17630)
- **PDF**: https://arxiv.org/pdf/2606.17630
- **详细分析**: [[20_Research/Papers/具身智能/FLAP_FOV-Constrained_Active_Perception_Planning_for_Prior-Map-Free_3D_Navigation|FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation]]
- **作者**: Mengke Zhang, Sitong Li, Tiancheng Lai, Ruitian Pang, Mingxuan Zhang, Qingcheng Chen, Fei Gao, Chao Xu, Yanjun Cao
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, EmbodiedAI, ComputerVision

#### 研究背景与动机

《FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Safe and efficient trajectory planning in unknown, cluttered 3D environments constitutes a critical bottleneck for deploying Unmanned Aerial Vehicles (UAVs) in real-world applications. This challenge is further exacerbated by the limited field-of-view (FOV) and sensing range of onboard sensors. Many existing methods either make simplistic assumptions about unexplored space or rely on conservative heuristics such as speed limits or fixed perception patterns, reducing efficiency and generalizing poorly across different sensor types. In this work, we propose a novel planning framework that directly integrates active perception into trajectory optimization, thereby improving safety while preserving efficiency. The perception constraints are derived from the UAV's dynamic model and formulated in the sensor coordinate frame, which enables precise handling of FOV geometry. The velocity-triggered activation mechanism enables the planner to balance perception and motion efficiency. We introduce an active perception sub-trajectory segment with parametric start-time optimization, mitigating collision risks from late obstacle detection. Our formulation enables active perception during arbitrary 3D maneuvers, extending beyond prior methods designed mainly for horizontal motion. All constraints and penalties are incorporated into a differentiable optimization problem, so the planner requires only a simple front-end global path for guidance, rather than a computationally expensive perception-aware path generator. Extensive simulations and real-world experiments demonstrate robust performance across diverse unknown environments with varying sensor configurations.

</details>

---

### [[20_Research/Papers/机器人/RICH-SLAM_Radar_SLAM_with_Incremental_and_Continuous_Hilbert_Mapping|RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping]]

![[assets/2606.17534_figure.png|800]]

- **arXiv**: [2606.17534](https://arxiv.org/abs/2606.17534)
- **PDF**: https://arxiv.org/pdf/2606.17534
- **详细分析**: [[20_Research/Papers/机器人/RICH-SLAM_Radar_SLAM_with_Incremental_and_Continuous_Hilbert_Mapping|RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping]]
- **作者**: Bingbing Zhang, Huan Yin, Yang Xu, Shuo Liu, Shaojie Shen, Fumin Zhang, Wen Xu
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，机器人 1.1）
- **关联关键词**: Agent

#### 研究背景与动机

《RICH-SLAM: Radar SLAM with Incremental and Continuous Hilbert Mapping》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Simultaneous localization and mapping using radar sensors has gained increasing attention due to radar's inherent robustness to adverse weather and lighting conditions. However, radar measurements are characteristically sparse and noisy compared to LiDAR and visual data, posing significant challenges in achieving dense, continuous, and consistent map representations. In this paper, we present RICH-SLAM, a radar SLAM framework designed to address these challenges. Our approach features a Rao-Blackwellized particle filter-based back end that employs particle filtering for pose estimation and Kalman filtering for map updates. We propose an incremental Hilbert-space reduced-rank Gaussian process mapping strategy that enables continuous and uncertainty-aware map representations given sparse radar inputs. We further introduce a posterior-aware particle weighting scheme that leverages the full posterior distribution of map parameters for more robust likelihood evaluation. Experiments on self-collected and public ColoRadar datasets show that RICH-SLAM constructs continuous occupancy maps from sparse radar measurements and supports uncertainty-aware planning for mobile robots.

</details>

---

### [[20_Research/Papers/强化学习/When_Robots_Sleep_Offline_Skill_Consolidation_for_Shared-Policy_Robot_Learning|When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning]]

![[assets/2606.17493_figure.png|800]]

- **arXiv**: [2606.17493](https://arxiv.org/abs/2606.17493)
- **PDF**: https://arxiv.org/pdf/2606.17493
- **详细分析**: [[20_Research/Papers/强化学习/When_Robots_Sleep_Offline_Skill_Consolidation_for_Shared-Policy_Robot_Learning|When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning]]
- **作者**: Nethmi Jayasinghe, Diana Gontero, Amit Ranjan Trivedi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 强化学习
- **相关性评分**: 1.6（加权：具身智能 0.3，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《When Robots Sleep: Offline Skill Consolidation for Shared-Policy Robot Learning》归入 机器人、具身智能、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AtomicVLA, CompoNet, Meta-World, PackNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robots that learn over long deployments must add new skills without losing the shared policy structure that makes earlier skills reusable. We study sequential robot skill learning, where previous trajectories and task losses may be unavailable, and the deployed policy must remain a single shared controller without task-specific heads, routing, or adapters. We identify skill-coupling collapse, a failure mode in which individual skill success remains non-trivial while reliability among related skills deteriorates. We propose Sleeping Robots, a wake-sleep framework that learns each new skill during wake and consolidates the shared policy offline during sleep using compact frozen skill memories: frozen critics with unordered state buffers for reinforcement learning and frozen actor snapshots with unordered observation buffers for imitation learning. During sleep, these memories define differentiable surrogate objectives whose gradients are combined through Nash bargaining, with adaptive anchoring and local excitability for stable consolidation. On Meta-World MT5, Sleeping Robots improves average success by 64 % and pairwise reliability by x 2.0 over the strongest non-oracle baseline, and on SurgicAI it improves average success and backward transfer relative to continual imitation baselines while remaining competitive on pairwise reliability.

</details>

---

### [[20_Research/Papers/具身智能/Embodiment_Shapes_Rolling_Behavior_in_a_Multimodal_Infant_Model|Embodiment Shapes Rolling Behavior in a Multimodal Infant Model]]

![[assets/2606.17456_figure.png|800]]

- **arXiv**: [2606.17456](https://arxiv.org/abs/2606.17456)
- **PDF**: https://arxiv.org/pdf/2606.17456
- **详细分析**: [[20_Research/Papers/具身智能/Embodiment_Shapes_Rolling_Behavior_in_a_Multimodal_Infant_Model|Embodiment Shapes Rolling Behavior in a Multimodal Infant Model]]
- **作者**: Leon Philipp, Francisco M. López, Jochen Triesch
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人, 强化学习
- **相关性评分**: 1.5（加权：具身智能 0.6，大模型 0.4，强化学习 0.2，机器人 0.3）
- **关联关键词**: Multimodal, Agent, EmbodiedAI

#### 研究背景与动机

《Embodiment Shapes Rolling Behavior in a Multimodal Infant Model》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Rolling over is one of the earliest milestones in infant motor development, reflecting the emergence of coordinated, whole-body sensorimotor control. Here, we conduct a computational study of infant rolling using MIMo, a virtual infant embodiment equipped with proprioception and vestibular sensation. MIMo learns supine-to-prone rolls with reinforcement learning. Interestingly, the learned behaviors capture developmental trends and coordination patterns consistent with those reported in real infants, including improved performance and faster execution with age. Our results explain how infant capabilities and constraints can give rise to realistic behaviors in artificial agents, with a particular emphasis on how motor development is shaped by the changing body morphology. This work highlights the role of embodied computational models as a powerful tool for studying sensorimotor development.

</details>

---

### [[20_Research/Papers/具身智能/DexLink_Hand_A_Compact,_Affordable,_16-DOF_Linkage-Driven_Hand_with_Human-Like_Dexterity|DexLink Hand: A Compact, Affordable, 16-DOF Linkage-Driven Hand with Human-Like Dexterity]]

![[assets/2606.17418_figure.png|800]]

- **arXiv**: [2606.17418](https://arxiv.org/abs/2606.17418)
- **PDF**: https://arxiv.org/pdf/2606.17418
- **详细分析**: [[20_Research/Papers/具身智能/DexLink_Hand_A_Compact,_Affordable,_16-DOF_Linkage-Driven_Hand_with_Human-Like_Dexterity|DexLink Hand: A Compact, Affordable, 16-DOF Linkage-Driven Hand with Human-Like Dexterity]]
- **作者**: Hao Wu, Yanzhe Wang, Yu Feng, Jian Liu, Jihao Li, Jianshu Zhou, Huixu Dong
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.6（加权：具身智能 0.9，机器人 0.7）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《DexLink Hand: A Compact, Affordable, 16-DOF Linkage-Driven Hand with Human-Like Dexterity》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：围绕论文提出的建模、算法或系统设计进行实验验证。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Dexterous robotic hands face a longstanding trade-off among dexterity, compactness, and affordability. Particularly, high-degree-of-freedom designs typically demand complex actuation and transmission, hindering integration into human-scale forms. To address these challenges, this work presents a compact, low-cost linkage-driven anthropomorphic hand that achieves high dexterity, structural integration, and human-hand-like functionality. The hand integrates 20 joints driven by 16 independent actuators, with all actuation, sensing, and transmission components compactly embedded within a human-hand-sized structure. The resulting prototype weighs only 320g at a total cost below USD 400. To meet these objectives, a hybrid mechanical architecture combining planar and spatial linkage mechanisms is proposed, enabling decoupled multidirectional motion, biomimetic joint synergies, and high passive load-bearing capability. The thumb further incorporates biomimetic features supporting human-like reconfiguration and opposition movements. Through the coordinated integration of these mechanisms and structural layout, the prototype achieves a highly integrated design with anthropomorphic dexterity. Experimental evaluations demonstrate that the hand achieves the maximum Kapandji score, reproduces all 33 Feix grasp types, and performs stable grasping and dexterous manipulation across a wide variety of daily objects and tools. These results validate the proposed hand as an affordable, compact, and mechanically efficient platform for dexterous manipulation, teleoperation, and robot learning in human-centered environments.

</details>

---

### [[20_Research/Papers/具身智能/EgoInfinity_A_Web-Scale_4D_Hand-Object_Interaction_Data_Engine_for_Any-View_Robot_Retargeting_and_Video-to-Action_Robot_Learning|EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning]]

![[assets/2606.17385_figure.png|800]]

- **arXiv**: [2606.17385](https://arxiv.org/abs/2606.17385)
- **PDF**: https://arxiv.org/pdf/2606.17385
- **详细分析**: [[20_Research/Papers/具身智能/EgoInfinity_A_Web-Scale_4D_Hand-Object_Interaction_Data_Engine_for_Any-View_Robot_Retargeting_and_Video-to-Action_Robot_Learning|EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning]]
- **作者**: Gaotian Wang, Kejia Ren, Andrew Morgan, Yiting Chen, Howard H. Qian, Podshara Chanrungmaneekul, Kaiyu Hang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 2.1（加权：具身智能 0.9，大模型 0.1，机器人 1.1）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《EgoInfinity: A Web-Scale 4D Hand-Object Interaction Data Engine for Any-View Robot Retargeting and Video-to-Action Robot Learning》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Internet videos constitute the largest reservoir of embodied human manipulation knowledge, yet converting arbitrary RGB footage into actionable robot training data remains a major bottleneck. Existing lab- or factory-collected datasets are narrow in scale and diversity, limiting open-world robot learning. Instead of proposing a static dataset, we introduce EgoInfinity, a universal 4D hand-object interaction data engine that enables web-scale data generation for robot retargeting and learning. EgoInfinity is a modular engine integrating perception, segmentation, reconstruction, interaction-aware refinement, and retargeting to automate this traditionally unscalable video-to-action problem without human-in-the-loop annotation. Its modular design lets the engine continuously benefit from advances in any incorporated component. With EgoInfinity, in-the-wild human manipulation videos are lifted into agent-agnostic, metric 4D hand-object representations, including hand trajectories, 6-DoF object poses, and contact-relevant states. Rather than naively connecting standalone components, EgoInfinity combines cross-module metric calibration with interaction-aware refinement to improve physical reliability, reducing drift and contact inconsistencies common in pure visual reconstruction. We further propose a novel motion retargeter that compiles the recovered 3D hand motions into executable joint trajectories for diverse robot morphologies, enabling video-to-action retargeting on any robot from arbitrary viewpoints and shot sizes (e.g., the human body is only partially visible). We validate EgoInfinity across perception fidelity, kinematic feasibility, contact consistency, cross-embodiment generalization, and real-robot skill acquisition (e.g., grasping, cutting, wiping, and pouring), demonstrating a scalable bridge from internet videos to executable robot behavior for open-world robot learning.

</details>

---

### [[20_Research/Papers/大模型/Abstention-Aware_Personalized_Object_Rearrangement_via_Uncertainty-Guided_LLM_Assistance|Abstention-Aware Personalized Object Rearrangement via Uncertainty-Guided LLM Assistance]]

![[assets/2606.17309_figure.jpg|800]]

- **arXiv**: [2606.17309](https://arxiv.org/abs/2606.17309)
- **PDF**: https://arxiv.org/pdf/2606.17309
- **详细分析**: [[20_Research/Papers/大模型/Abstention-Aware_Personalized_Object_Rearrangement_via_Uncertainty-Guided_LLM_Assistance|Abstention-Aware Personalized Object Rearrangement via Uncertainty-Guided LLM Assistance]]
- **作者**: Sam Collin, Ali Ayub
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.4（加权：具身智能 0.3，大模型 0.6，机器人 0.5）
- **关联关键词**: LLM, Robotics, Security

#### 研究背景与动机

《Abstention-Aware Personalized Object Rearrangement via Uncertainty-Guided LLM Assistance》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：URL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic assistance in household environments requires not only predicting where objects should be placed, but also reasoning about when objects should not be placed at all. Existing approaches to personalized object rearrangement primarily focus on placement decisions under the assumption of clean observations and complete actionability, limiting their applicability in realistic, cluttered, and partially erroneous settings. In this paper, we introduce APOLLO, a hybrid framework for abstention-aware personalized object rearrangement that combines a lightweight, personalized embedding model (PEM) with selective large language model (LLM) assistance. PEM is trained for each user-environment pair using a small number of demonstrations, operates entirely on CPU, and produces uncertainty estimates, which are used to selectively invoke LLM-based reasoning only for ambiguous decisions, balancing efficiency, privacy, and reasoning capability. To evaluate this formulation beyond existing benchmarks, we introduce APOR, a synthetic, LLM-generated dataset that captures room-level, multi-furniture environments, diverse organizational profiles, explicit abstention behavior, and noisy partial scene context. Extensive experiments on both PARSEC and APOR provide initial evidence that APOLLO improves over prior LLM-based baselines in controlled benchmark settings while substantially reducing LLM usage. Code is available at this https URL .

</details>

---

### [[20_Research/Papers/机器人/Intermittent_Strategic_Cooperation_of_Two_Selfish_Agents_on_Graphs|Intermittent Strategic Cooperation of Two Selfish Agents on Graphs]]

![[assets/2606.17216_figure.png|800]]

- **arXiv**: [2606.17216](https://arxiv.org/abs/2606.17216)
- **PDF**: https://arxiv.org/pdf/2606.17216
- **详细分析**: [[20_Research/Papers/机器人/Intermittent_Strategic_Cooperation_of_Two_Selfish_Agents_on_Graphs|Intermittent Strategic Cooperation of Two Selfish Agents on Graphs]]
- **作者**: Itay Shedlezki, Noa Agmon
- **cs 子类**: cs.RO
- **归属领域**: 大模型
- **相关领域**: 大模型, 机器人, 具身智能
- **相关性评分**: 1.3（加权：具身智能 0.3，大模型 0.5，机器人 0.5）
- **关联关键词**: Agent

#### 研究背景与动机

《Intermittent Strategic Cooperation of Two Selfish Agents on Graphs》归入 大模型、机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 大模型、机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We study strategic space- and time-constrained cooperation between two self-interested agents through the Intermittent Strategic Cooperation-Based Two-Agent Path Planning (IC2PP) problem, a shortest-path game on graphs in which agents navigate toward individual targets while optionally cooperating at specific nodes to reduce their own travel times. Although such cooperation can strictly benefit both agents, it is strategically fragile: agents may deviate at any point along their paths. Modeled as a 2-player game, we characterize the structure of Pure Nash Equilibrium (PNE) joint strategies in IC2PP, and show that stable cooperation must follow a highly constrained form. We further prove that at least one PNE exists in every instance of IC2PP, and present a polynomial-time algorithm for enumerating all relevant PNEs. When multiple equilibria arise, we study coordination mechanisms based on bargaining-theoretic selection concepts and empirically compare equilibrium outcomes in terms of individual travel times and social welfare.

</details>

---

### [[20_Research/Papers/具身智能/ACE-Ego-0_Unifying_Egocentric_Human_and_Robotic_Data_for_VLA_Pretraining|ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining]]

![[assets/2606.17200_figure.png|800]]

- **arXiv**: [2606.17200](https://arxiv.org/abs/2606.17200)
- **PDF**: https://arxiv.org/pdf/2606.17200
- **详细分析**: [[20_Research/Papers/具身智能/ACE-Ego-0_Unifying_Egocentric_Human_and_Robotic_Data_for_VLA_Pretraining|ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining]]
- **作者**: Hao Li, Ganlong Zhao, Yufei Liu, Haotian Hou, Guoquan Ye, Tongyan Fang, Chunxiao Liu, Siyuan Huang, Jianbo Liu, Xiaogang Wang, Hongsheng Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 3.2（加权：具身智能 2.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《ACE-Ego-0: Unifying Egocentric Human and Robotic Data for VLA Pretraining》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：OpenVLA, SpatialVLA, TraceVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models benefit from large-scale and diverse embodied data, yet scaling robot trajectory collection is costly and labor-intensive. Recent advances show that large-scale egocentric human videos provide complementary real-world supervision in pretraining. However, joint training on human and robot data remains challenging due to divergences in action spaces, embodiment structures, temporal dynamics, and supervision quality. We introduce ACE-EGO-0, a unified VLA pretraining framework jointly leveraging heterogeneous data sources. To extract large-scale pretraining supervision from egocentric human videos, we build a scalable egocentric video-to-action pipeline that converts raw human videos into robot-format pseudo-action trajectories. To make these labels comparable with robot demonstrations, ACE-EGO-0 uses a unified action representation based on camera-space actions, morphology conditioning, and time-aligned action chunking. To robustly leverage noisy pseudo-action supervision from egocentric human videos, we formulate a reliability-aware training objective with a human auxiliary loss that concentrates supervision on reliable signals. We instantiate ACE-EGO-0 on 4.53K hours of robot and simulation data, together with 1.48K hours of pseudo-action-labeled egocentric human data. Experiments show that incorporating large-scale human supervision under reliability-aware weighting consistently improves both unified joint pretraining and supervised fine-tuning. ACE-EGO-0 achieves state-of-the-art performance on RoboCasa GR1 TableTop and RoboTwin 2.0, while demonstrating strong transfer to real-world bimanual manipulation.

</details>

---
