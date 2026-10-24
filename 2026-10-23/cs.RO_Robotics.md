# cs.RO | Robotics | 2026-10-23

#arxiv #ComputerScience

**论文数**: 34

### [[20_Research/Papers/强化学习/OpenTac_An_Open_Ecosystem_for_Customizable,_Scalable,_and_Transferable_3D_Tactile_Sensing|OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing]]

![[assets/2610.31661_figure.png|800]]

- **arXiv**: [2610.31661](https://arxiv.org/abs/2610.31661)
- **PDF**: https://arxiv.org/pdf/2610.31661
- **详细分析**: [[20_Research/Papers/强化学习/OpenTac_An_Open_Ecosystem_for_Customizable,_Scalable,_and_Transferable_3D_Tactile_Sensing|OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing]]
- **作者**: Ariel Slepyan, Geeta Chandra Raju Bethala, Jiafeng Gu, Anagha Rajendra Dangle, Yinzhe Zhou, Hongyuan Fu, Jade Sim, Tuhin Basu, Xinyi Yin, Md Faizal Karim, Gregory Hager, Homanga Bharadhwaj...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《OpenTac: An Open Ecosystem for Customizable, Scalable, and Transferable 3D Tactile Sensing》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：OpenTac-Sim。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We present OpenTac, a novel sensor and a full-stack ecosystem for tactile skins that are highly customizable, scalable, and readily deployed in downstream robot control and learning applications. Our core contribution is twofold. First, we develop a scalable resistive tactile skin with a structured deformable overlay that converts tangential loading into spatially varying pressure. Differential responses across neighboring "taxels" support decoding of local shear vectors, and the common-mode response encodes normal force. Second, we provide a highly customizable sensor design tool that is able to automatically generate fabrication files for these tactile skins from 2D outlines and developable 3D surfaces, including from abstract descriptions such as text (e.g., "design a sensor for a size 9 shoe insole"). We develop an ecosystem around the OpenTac sensor, including the CAD design tool, a sensor simulator, cross-sensor transfer, and fast/adaptive data acquisition. We demonstrate the broad applicability of the OpenTac-CAD sensor design tool by designing and fabricating more than 30 sensors across a variety of robot embodiments. We characterize the three-dimensional tactile fields produced by OpenTac with a commercial, high-precision force/torque sensor. We demonstrate the broad applicability of 3D tactile sensing across contact-rich feedback control and manipulation policy learning on four real-world robot embodiments. Additionally, adaptive acquisition enables kilohertz-rate partial readouts, exceeding full-array raster scanning on the same sensor by 19.2X at 16 sampled taxels per update for a 1024-taxel skin. We provide all hardware, software, and result videos are at opentac.github.io

</details>

---

### [[20_Research/Papers/机器人/Extending_Harmonic_Function_Methods_via_Root_Locus_for_Coordinated_Path_Generation|Extending Harmonic Function Methods via Root Locus for Coordinated Path Generation]]

![[assets/2610.31625_figure.png|800]]

- **arXiv**: [2610.31625](https://arxiv.org/abs/2610.31625)
- **PDF**: https://arxiv.org/pdf/2610.31625
- **详细分析**: [[20_Research/Papers/机器人/Extending_Harmonic_Function_Methods_via_Root_Locus_for_Coordinated_Path_Generation|Extending Harmonic Function Methods via Root Locus for Coordinated Path Generation]]
- **作者**: Matteo Frascarelli, Lucia Pallottino, Alberto Landi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Agent, Robotics

#### 研究背景与动机

《Extending Harmonic Function Methods via Root Locus for Coordinated Path Generation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：GRL, RRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

We consider the offline generation of coordinated paths for N interchangeable robots and N goals in planar environments with polygonal obstacles. After a conformal map to a circular domain, starts and goals become the poles and zeros of a rational function R, and the paths are the branches of its Generalized Root Locus (GRL), i.e. the streamlines of the logarithmic potential -log R. We show that, for every phase outside a finite set of critical phases and a set of boundary phases, the induced gradient motion drives each robot to a distinct goal along pairwise disjoint paths that never reach the obstacles; the robot-goal assignment is produced by the construction, and with the gain used as a clock all robots move as the closed-loop roots of the GRL and arrive together at a prescribed time. Obstacles become streamlines through successive Milne-Thomson reflections, and for a finite number of reflections a finite test certifies safety for the potential that is actually computed. Reciprocal root-locus planning is recovered as a special case. The method is illustrated on two polygonal workspaces, 100 random instances compared with independent harmonic planning and artificial potentials, and a scene with ten robots and ten obstacles.

</details>

---

### [[20_Research/Papers/强化学习/DiffDreamer_Coupling_World_Models_with_Differentiable_Simulation_for_Agile_Quadrotor_Control|DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control]]

![[assets/2610.31617_figure.png|800]]

- **arXiv**: [2610.31617](https://arxiv.org/abs/2610.31617)
- **PDF**: https://arxiv.org/pdf/2610.31617
- **详细分析**: [[20_Research/Papers/强化学习/DiffDreamer_Coupling_World_Models_with_Differentiable_Simulation_for_Agile_Quadrotor_Control|DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control]]
- **作者**: Fanxing Li, Yuxiang Huang, Shengyang Wang, Fangyu Sun, Shuyu Wu, Tianbao Zhang, Dexin Zuo, Yan Yufei, Danping Zou, Wenxian Yu
- **cs 子类**: cs.RO
- **归属领域**: 世界模型
- **相关领域**: 世界模型, 机器人, 强化学习, 具身智能, 大模型
- **相关性评分**: 2.5（加权：具身智能 0.3，大模型 0.1，强化学习 0.4，世界模型 1.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《DiffDreamer: Coupling World Models with Differentiable Simulation for Agile Quadrotor Control》归入 世界模型、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；实时应用对效率提出要求。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 世界模型、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：DiffRL, Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tasks such as quadrotor dynamic-gate racing require agents to anticipate external motion while maintaining precise high-frequency control. World-model-based reinforcement learning provides a natural solution by learning latent dynamics for future imagination, yet it often entangles environmental evolution and the robot's own dynamics in a single learned rollout, where model bias can affect policy optimization efficiency. We propose DiffDreamer, a differentiable reinforcement learning framework that tightly couples a learned world model with differentiable simulation for actor optimization. In one optimization step, the learned world model propagates latent states that capture external dynamics and history-dependent features, while the differentiable simulator propagates the robot's explicit physical state. We further decompose the actor objective into a critic-driven pathway for non-differentiable task rewards and a simulator-driven pathway for differentiable motion rewards. Experiments on aggressive tracking and dynamic-gate racing show that DiffDreamer improves training convergence over the model-free, model-based, and differentiable-RL baselines, and final performance over these baselines and classical planning and control methods. Additional experiments assess reward decomposition and the odometry-conditioned relative-state representation through ablations. We also provide proof-of-concept real-world flight experiments for validation.

</details>

---

### [[20_Research/Papers/具身智能/Progress_Probes_$P^2$_Lightweight_Runtime_Monitoring_for_Vision-Language-Action_Models|Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models]]

![[assets/2610.31613_figure.png|800]]

- **arXiv**: [2610.31613](https://arxiv.org/abs/2610.31613)
- **PDF**: https://arxiv.org/pdf/2610.31613
- **详细分析**: [[20_Research/Papers/具身智能/Progress_Probes_$P^2$_Lightweight_Runtime_Monitoring_for_Vision-Language-Action_Models|Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models]]
- **作者**: Atiksh Bhardwaj, Edward W. Duan, Junwon Seo, Prithwish Dan, Wei-Chiu Ma, Andrea Bajscy, Preston Culbertson
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 2.2（加权：具身智能 1.8，大模型 0.1，机器人 0.3）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Progress Probes $P^2$: Lightweight Runtime Monitoring for Vision-Language-Action Models》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：VLABench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Vision-Language-Action (VLA) models can perform diverse manipulation tasks directly from visual observations and natural language instructions, but they remain prone to mistakes and unpredictable failures. Deploying these policies without continuous human supervision will require robust runtime monitors that detect when the policy has gone off-course. Existing monitors use external foundation models, such as vision-language models (VLMs) to supervise the policy, introducing significant complexity and computational cost for monitoring at runtime. In this work, we investigate an alternate approach: \textit{can a VLA's own internal activations provide the information needed to monitor its execution?} Our method trains linear probes on policy activations from demonstrations to estimate progress, then flags executions that deviate from expected progress. In experiments with the open-source VLA $π_{0.5}$ and across simulated and real-world manipulation tasks, this approach is competitive with or outperforms VLM-based monitors in task failure detection, as well as methods which require failure data for training. These findings suggest that simple probes of VLA internals can be used to develop reliable runtime monitors, opening a path toward building policies that can act reliably and monitor their execution without external foundation models.

</details>

---

### [[20_Research/Papers/具身智能/Humanoid_Mobility_via_Attention-based_Contacts|Humanoid Mobility via Attention-based Contacts]]

![[assets/2610.31608_figure.png|800]]

- **arXiv**: [2610.31608](https://arxiv.org/abs/2610.31608)
- **PDF**: https://arxiv.org/pdf/2610.31608
- **详细分析**: [[20_Research/Papers/具身智能/Humanoid_Mobility_via_Attention-based_Contacts|Humanoid Mobility via Attention-based Contacts]]
- **作者**: Junzhe He, Kehan Wen, Chong Zhang, Clemens Schwarke, Zewei Zhang, Kaixian Qu, Siyuan Hu, Matthias Müller, Vladlen Koltun, Marco Hutter
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.1（加权：具身智能 1.8，强化学习 0.2，机器人 1.1）
- **关联关键词**: Robotics, RL, Systems

#### 研究背景与动机

《Humanoid Mobility via Attention-based Contacts》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid mobility over complex terrain requires accurate foot placement and coordinated whole-body motion capable of robust adaptation. Reinforcement learning (RL) policies trained without motion references generalize well across terrains, yet eliciting effective whole-body coordination through reward design and exploration alone remains challenging. In contrast, reference-based methods yield natural motions but struggle to adapt beyond the predefined trajectories in their training data. We introduce a learning framework that bridges these two approaches by using motion data strictly as a training prior. An explicit, self-supervised, attention-based contact planner predicts future body-environment contacts, while a contact-conditioned tracker translates these plans into coordinated whole-body motion. Together, they establish contact as an interface between sensory observations and control actions. This abstraction allows the policy to internalize the contact-aware structure of locomotion rather than directly replicating kinematics. Consequently, a single policy can exploit data-driven motion priors for natural whole-body coordination while retaining the flexibility to discover environment-dependent behaviors through reinforcement learning. Building on the learned contact planner and tracker, a subsequent fine-tuning stage bootstraps their acquired capabilities to explore environment variations beyond those covered by the original motion data. Operating entirely from onboard observations without any reference inputs at deployment, this framework enables versatile humanoid mobility in challenging environments.

</details>

---

### [[20_Research/Papers/具身智能/Echo_Coupled_Action_and_Task_Status_Signal_Denoising_for_Vision_Language_Action_Models|Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models]]

![[assets/2610.31569_figure.png|800]]

- **arXiv**: [2610.31569](https://arxiv.org/abs/2610.31569)
- **PDF**: https://arxiv.org/pdf/2610.31569
- **详细分析**: [[20_Research/Papers/具身智能/Echo_Coupled_Action_and_Task_Status_Signal_Denoising_for_Vision_Language_Action_Models|Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models]]
- **作者**: Yufeng Liu, Bohao Fan, Juntu Zhao, Xinyi Wang, Hang Yu, Wenzhuan Luo, Yingzhi Wang, Qinghai Li, Yingdong Hu, Junliang Guo, Richard Wang, Dequan Wang...
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《Echo: Coupled Action and Task Status Signal Denoising for Vision Language Action Models》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：CycleVLA, ProgressVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Recognizing task completion and failure enables robots to stop upon success and initiate recovery or replanning after failure. Existing methods augment Vision Language Action (VLA) policies with task status signal prediction to support these execution decisions. However, learning and integrating these signals can require fine-grained supervision, external monitoring models, or complex architectural designs. Moreover, the potential of task status signals to directly guide action generation remains underexplored. We present Echo, a framework that combines task status signal learning without frame-level progress annotations with a compact design for status prediction and action generation within a single VLA. Specifically, Echo represents task status with stop and failure signals, added as two dimensions of each action chunk and denoised together with robot actions. Their combination distinguishes ongoing execution, successful completion, and failure. To learn these signals without fine-grained progress annotations, Echo constructs successful, failed, and recovery trajectories with complementary supervision properties. To enable status signal-guided action generation, Echo controls interactions between the signals and actions and denoises the signals faster than the actions. These allow later action denoising steps to condition on cleaner status estimates while preserving accurate signal prediction. Extensive real-world manipulation experiments show that Echo accurately predicts task status and consistently improves policy performance.

</details>

---

### [[20_Research/Papers/具身智能/Dispersive_Tree_Agreements_for_Multi-Robot_Coordination|Dispersive Tree Agreements for Multi-Robot Coordination]]

![[assets/2610.31540_figure.png|800]]

- **arXiv**: [2610.31540](https://arxiv.org/abs/2610.31540)
- **PDF**: https://arxiv.org/pdf/2610.31540
- **详细分析**: [[20_Research/Papers/具身智能/Dispersive_Tree_Agreements_for_Multi-Robot_Coordination|Dispersive Tree Agreements for Multi-Robot Coordination]]
- **作者**: Shashank A. Deshpande, Blake T. Edwards, Jonathan P. How
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Dispersive Tree Agreements for Multi-Robot Coordination》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot coordination of nonlinear systems is naturally formulated as joint-space optimal control subject to constraints over groups of robots. Existing methods that approach joint optimality remain largely centralized, offline, and confined to collision-free motion planning, while decentralized, real-time counterparts target safe navigation without pursuing the joint optimum. This paper develops a decentralized, real-time planner that approaches the joint optimum as an anytime process. We extend a recent single-robot framework that searches dispersive trees of forward-propagated commands for differentially flat systems to coordinate a multi-robot team near-optimally. We first show that the inter-robot coupling can be effectively replaced by some local constraints, under which locally grown dispersive trees contain a near-optimal agreement. It is this structure that the robots pursue by decentralized column generation, negotiating rents on the shared space that guide the search of each robot's tree. The negotiation settles on an agreement whose near-optimality is certified at quiescence. Our protocol, WarpWeaver, implements this negotiation as an asynchronous real-time loop over a receding horizon, and demonstrates effective closure to quiesced agreements even when real-time deadlines cut the negotiation short. In simulation, WarpWeaver reduces total travel time by up to 22% against centralized offline planners on the Dynobench suite and by up to 37% against a decentralized real-time baseline, and nearly doubles the success rate of a task-specific planner on graph connectivity. Hardware experiments on six robots planning onboard demonstrate real-world implementability.

</details>

---

### [[20_Research/Papers/大模型/SCOPE_Scene-graph_Construction_Optimized_by_Plan_Error-correction_for_Robot_Long-term_Planning_Datasets|SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets]]

![[assets/2610.31518_figure.png|800]]

- **arXiv**: [2610.31518](https://arxiv.org/abs/2610.31518)
- **PDF**: https://arxiv.org/pdf/2610.31518
- **详细分析**: [[20_Research/Papers/大模型/SCOPE_Scene-graph_Construction_Optimized_by_Plan_Error-correction_for_Robot_Long-term_Planning_Datasets|SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets]]
- **作者**: Chaoyue Li, Zeyu Gao, Yanfeng Lu, Fan Luo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.2，机器人 1.3）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《SCOPE: Scene-graph Construction Optimized by Plan Error-correction for Robot Long-term Planning Datasets》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Task and Motion Planning (TAMP) stands as a fundamental challenge in robotics, essential for enabling autonomous agents to execute complex, long-horizon tasks in diverse environments. While Large Language Models (LLMs) introduce a new paradigm for TAMP by leveraging extensive common sense, their inherent reasoning limitations hinder direct application, and fine-tuning strategies to enhance these capabilities are currently bottlenecked by the scarcity of high-quality datasets. Existing automated generation methods often suffer from homogeneity, limiting model generalization, and unsolvability, where hallucinated scene graphs create physical mismatches with task goals. To address these issues, we propose Scene-graph Construction Optimized by Plan Error-correction (SCOPE), an automated framework designed to generate diverse and executable TAMP datasets. SCOPE incorporates multi-level diversity metrics to maximize the information entropy of scenarios. Crucially, it introduces a Plan Feedback Error-correction pipeline that utilizes planner execution failures as feedback signals to retroactively rectify logical inconsistencies in scene graphs, ensuring physical feasibility. Experimental results demonstrate that SCOPE exhibits greater robustness to erroneous scene graphs and generates higher-quality data. When utilized for LLM fine-tuning, SCOPE-generated data yield a downstream TAMP model that achieves an absolute 12.33% gain in success rate over its counterpart fine-tuned with data generated by DELTA, a state-of-the-art PDDL-based planner.

</details>

---

### [[20_Research/Papers/具身智能/Point-Level_Refinable_Semantic_Mapping_for_Spatial_Understanding|Point-Level Refinable Semantic Mapping for Spatial Understanding]]

![[assets/2610.31476_figure.png|800]]

- **arXiv**: [2610.31476](https://arxiv.org/abs/2610.31476)
- **PDF**: https://arxiv.org/pdf/2610.31476
- **详细分析**: [[20_Research/Papers/具身智能/Point-Level_Refinable_Semantic_Mapping_for_Spatial_Understanding|Point-Level Refinable Semantic Mapping for Spatial Understanding]]
- **作者**: Taimeng Fu, Yi Du, Zitong Zhan, Qiwei Du, Shaoshu Su, Zhipeng Zhao, Chen Wang
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.4（加权：具身智能 0.9，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI, ComputerVision

#### 研究背景与动机

《Point-Level Refinable Semantic Mapping for Spatial Understanding》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World, ScanNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Open-vocabulary 3D semantic maps have emerged as a key spatial memory representation for long-horizon robot autonomy, enabling robots to reason about objects, their spatial relationships, and past observations across time. However, existing object-centric semantic maps are primarily designed for static environments and rely on an append-only point integration strategy, where newly observed points are accumulated but previously integrated points are rarely reevaluated. Consequently, perception errors accumulate over time, and outdated points persist after objects move or disappear. Although recent dynamic mapping methods update object-level representations in changing scenes, they do not explicitly revise noisy or obsolete points within each object. We propose an online refinable semantic mapping framework that continuously refines object representations through probabilistic point-level confidence updating. Each object point maintains a confidence score that is updated online using multi-view temporal evidence: consistent observations reinforce reliable points, while inconsistent segmentation masks, depth measurements, and visibility cues suppress spurious and outdated points. Combined with object tracking and re-identification to preserve instance identities under motion and relocation, our framework enables object-centric semantic maps to be continuously refined rather than monotonically accumulated. Experiments demonstrate improved mapping accuracy over the previous method by 3.46% on Replica and 2.55% on ScanNet, show robustness in dynamic environments and under perception noise, and provide an effective spatial memory for object navigation and embodied question-answering with success rates of 82.4% and 76.7%.

</details>

---

### [[20_Research/Papers/强化学习/Skeleton-Grounded_Latent_Action_Model_for_Robot_World_Models|Skeleton-Grounded Latent Action Model for Robot World Models]]

![[assets/2610.31474_figure.png|800]]

- **arXiv**: [2610.31474](https://arxiv.org/abs/2610.31474)
- **PDF**: https://arxiv.org/pdf/2610.31474
- **详细分析**: [[20_Research/Papers/强化学习/Skeleton-Grounded_Latent_Action_Model_for_Robot_World_Models|Skeleton-Grounded Latent Action Model for Robot World Models]]
- **作者**: Qi Lv, Jiayi Lin, Yuxin Jiang, Jianzong Wang, Xiang Deng, Mike Shou Zheng
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.4（加权：具身智能 0.3，世界模型 1，机器人 1.1）
- **关联关键词**: Robotics, RL, WorldModel

#### 研究背景与动机

《Skeleton-Grounded Latent Action Model for Robot World Models》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；使用 Transformer/基础模型结构；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：LARYBench, Olaf-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot world models simulate how environments evolve in response to robot actions. Latent action models enable learning dynamics from videos by encoding visual transitions as proxy actions. However, reconstruction-driven latent actions mix robot motion with object responses and other scene changes, complicating their correspondence with robot controls. We propose SkeLAM, a skeleton-guided latent action model for controllable robot world modeling. SkeLAM decomposes latent actions into a kinematic component grounded by robot skeleton supervision and a residual component retaining complementary visual dynamics. Cross-modal swap reconstruction encourages RGB-derived and skeleton-derived kinematic representations to be interchangeable during video reconstruction. The world model incorporates both components through separate conditioning pathways, while branch dropout reduces its dependence on future-derived residual information. A lightweight adapter maps robot actions to the kinematic space, and subsequent world-model fine-tuning adapts generation to these predicted conditions. At inference, the model generates future observations from the current observation and robot actions. On DROID, SkeLAM reduces end-effector ADE by 19.5% and LPIPS by 11.1% compared with DreamDojo. Motion probing supports kinematic specialization, while qualitative results demonstrate zero-shot human-to-robot motion transfer in generated rollouts. Policy evaluation shows agreement between predicted success rates and those measured in real robot executions.

</details>

---

### [[20_Research/Papers/具身智能/FastHarness_Experience-Driven_Review_Scheduling_for_Vision-Language-Action_Policies|FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies]]

![[assets/2610.31427_figure.png|800]]

- **arXiv**: [2610.31427](https://arxiv.org/abs/2610.31427)
- **PDF**: https://arxiv.org/pdf/2610.31427
- **详细分析**: [[20_Research/Papers/具身智能/FastHarness_Experience-Driven_Review_Scheduling_for_Vision-Language-Action_Policies|FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies]]
- **作者**: Tao Lin, Yuxin Du, Haoxiao Wang, Zile Zhong, Bo Zhao
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.9（加权：具身智能 1.2，机器人 0.7）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《FastHarness: Experience-Driven Review Scheduling for Vision-Language-Action Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；引入智能体式建模或搜索；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Agentic robot systems combine language-model reasoning with robot policies to monitor execution and recover from failures. However, reviewing every action chunk incurs substantial overhead, even in familiar situations. We introduce FastHarness, an experience-driven execution harness that adaptively schedules GPT-6 Astra supervision of a π0.5 policy. A fast path uses stage memory and reviewed outcomes to reduce review frequency as experience accumulates, while a complementary recovery path focuses supervision on correcting errors. Once recovery is verified, routine execution resumes, with failure experience retained to guide future interventions. The policy remains frozen and generates fresh actions from current observations. Across four simulated manipulation tasks, reviewer token use decreases by an average of 57.2% per task from the first evaluated episode to the mean of the final five episodes. Mean episode time decreases from 85.5 to 52.0 minutes over the same interval. On the same tasks, mean success increases from 80% for GPT-as-Policy (π0.5 + GPT-6 Astra) to 97.19% with FastHarness. These results highlight adaptive supervision as a practical route to more efficient agentic robotics without additional model training.

</details>

---

### [[20_Research/Papers/强化学习/Probabilistic_Energy_Modeling_Unifies_Versatile_Swarm_Control|Probabilistic Energy Modeling Unifies Versatile Swarm Control]]

![[assets/2610.31371_figure.png|800]]

- **arXiv**: [2610.31371](https://arxiv.org/abs/2610.31371)
- **PDF**: https://arxiv.org/pdf/2610.31371
- **详细分析**: [[20_Research/Papers/强化学习/Probabilistic_Energy_Modeling_Unifies_Versatile_Swarm_Control|Probabilistic Energy Modeling Unifies Versatile Swarm Control]]
- **作者**: Xiang Zhou, Xiangyu Zhu, Xintong Wang, Qingyuan Yang, Rui Huang, Feng Xue, Lin Li, Qingrui Zhang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.0（加权：具身智能 0.3，大模型 0.2，机器人 0.5）
- **关联关键词**: Agent, Robotics, RL

#### 研究背景与动机

《Probabilistic Energy Modeling Unifies Versatile Swarm Control》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：MARL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robotic swarms must coordinate across diverse missions, yet existing controllers often require redesign, retuning, or retraining when objectives change. Here we show that probabilistic energy modeling provides a unifying representation for versatile swarm control, in which diverse missions emerge from compositions of shared interaction principles rather than task-specific control formulations. By exploiting the correspondence between Gibbs random field energy minimization and structured reward maximization, we encode fundamental swarm behaviors as reusable energy terms within a unified probabilistic objective. Decentralized policies trained within this representation are composed into a single controller through lightweight policy gating, without retraining. An interpretable action-attention mechanism captures non-uniform local interactions, while dimensionless normalization supports transfer across swarm scales and platforms. Demonstrated on aerial swarms, the unified policy generalizes zero-shot across six mission classes, 10-100 agents, two hardware platforms, and indoor cluttered and GPS-denied woodland environments. Large-scale simulations achieve 0.96-1.00 task success rates with 1-10 ms per-agent inference latency, while physical deployments confirm zero-shot transfer to real platforms and unstructured environments. These results establish probabilistic energy modeling as a scalable and transferable framework for decentralized swarm control.

</details>

---

### [[20_Research/Papers/机器人/Consistent_Distributed_Invariant_EKF_SLAM_with_Point_and_Object_Features|Consistent Distributed Invariant EKF SLAM with Point and Object Features]]

![[assets/2610.31221_figure.png|800]]

- **arXiv**: [2610.31221](https://arxiv.org/abs/2610.31221)
- **PDF**: https://arxiv.org/pdf/2610.31221
- **详细分析**: [[20_Research/Papers/机器人/Consistent_Distributed_Invariant_EKF_SLAM_with_Point_and_Object_Features|Consistent Distributed Invariant EKF SLAM with Point and Object Features]]
- **作者**: Mengya Xu, Xianjia Yu, Ha Sier, Shoudong Huang, Tomi Westerlund
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.6（加权：具身智能 0.3，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Consistent Distributed Invariant EKF SLAM with Point and Object Features》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Multi-robot SLAM allows robots to improve their estimates by exchanging map information, but repeated exchanges create unknown correlations between local estimators. Covariance intersection (CI) can fuse estimates without tracking these correlations. In right-invariant extended Kalman filter (RI-EKF) SLAM, however, point features obtain their invariant errors through the robot rotation, so a neighbor's map estimate is expressed in its own error coordinates and is correlated with its pose, and cannot be fused by CI directly. This paper presents Joint-CI, a unified fusion method for distributed RI-EKF SLAM with point, object, and mixed point--object maps. Using a neighboring robot's local posterior and an inter-robot observation, a joint estimate of the receiving robot's pose and the common features is constructed in the receiving robot's error coordinates, retaining the robot--feature and feature--feature correlations. Partial-state CI then fuses this estimate with the receiving robot's local posterior. We show that the unified formulation and the fusion preserve the six unobservable directions associated with global rotation and translation, and that communication and fusion preserve first-order covariance consistency given consistent local posteriors. Monte Carlo simulations and a real-world dataset-derived experiment show that Joint-CI improves estimation accuracy while maintaining consistent, mildly conservative uncertainty.

</details>

---

### [[20_Research/Papers/大模型/RGraph-Eval_Task-Grounded_Scene_Graphs_for_Evaluating_Robot_Video_Generation|RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation]]

![[assets/2610.31121_figure.png|800]]

- **arXiv**: [2610.31121](https://arxiv.org/abs/2610.31121)
- **PDF**: https://arxiv.org/pdf/2610.31121
- **详细分析**: [[20_Research/Papers/大模型/RGraph-Eval_Task-Grounded_Scene_Graphs_for_Evaluating_Robot_Video_Generation|RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation]]
- **作者**: Aleksandr Lazarev, Sofia Zimina, Roman Kuznetsov, Tatiana Zemskova, Iaroslav Koshelev, Dmitry Yudin
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能, 大模型
- **相关性评分**: 1.5（加权：具身智能 0.3，大模型 0.1，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, ComputerVision

#### 研究背景与动机

《RGraph-Eval: Task-Grounded Scene Graphs for Evaluating Robot Video Generation》归入 机器人、具身智能、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：该工作聚焦 Robotics 方向中的具体问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：RBench, RGraph-Eval, Ref4D-VideoBench, TIQA, VBench, WorldModelBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Generated robot videos can look convincing while depicting the wrong interac- tion: a different object is moved, a grasp disappears, or a placement ends out- side its destination. We introduce RGraph-Eval, a reference-based framework that makes these discrepancies explicit through task-grounded temporal scene graphs. Unlike approaches that construct separate evidence representations for different evaluation dimensions, we organize task entities, interactions, and motion within a unified, interpretable scene graph representation. A foundation-model pipeline identifies manipulation roles, grounds persistent object masks, infers and verifies state transitions and action intervals, and reconstructs manipulated- object motion in three dimensions. Applying this representation to a generated video and a reference demonstration supports an interpretable RGraph-Eval score with visible-object, relation-change, and 3D path-shape components. We also introduce ShareRobot-SG, a collection of 1,000 manipulation scenes from ten ShareRobot sources annotated with the multimodal representation. Our eval- uation separates graph-generation quality from agreement with human video judgments, and includes comparisons with adapted SVG2 and SG-Ego, a bench- mark of three video generators. The framework connects robot-video assessment to the observable entities and interactions underlying a task, while making the graph annotations reusable beyond evaluation. Code will be publicly available at https://github.com/SashaDance/rgraph-eval.

</details>

---

### [[20_Research/Papers/具身智能/AstroBench_Benchmarking_Free-Floating_Capture_and_Space_Robotic_Manipulation|AstroBench: Benchmarking Free-Floating Capture and Space Robotic Manipulation]]

![[assets/2610.31064_figure.png|800]]

- **arXiv**: [2610.31064](https://arxiv.org/abs/2610.31064)
- **PDF**: https://arxiv.org/pdf/2610.31064
- **详细分析**: [[20_Research/Papers/具身智能/AstroBench_Benchmarking_Free-Floating_Capture_and_Space_Robotic_Manipulation|AstroBench: Benchmarking Free-Floating Capture and Space Robotic Manipulation]]
- **作者**: Zizhe Wang, Jia Deng, Xin Lu, Zehao Jia, Yi Huang, Yao Zhu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《AstroBench: Benchmarking Free-Floating Capture and Space Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：AstroBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Capturing a loose object inside a spacecraft requires a robot to approach a target that can translate and rotate, and whose motion changes when contact is made. These conditions motivate evaluation beyond manipulation of supported objects. We introduce AstroBench, an open benchmark for free-floating capture and space robotic manipulation with a fixed-base arm. The task suite combines four initial-motion tracks with sample-storage operations based on MELFI hardware and cap and captive-screw servicing based on the Robotic Refueling Mission. The two workcells provide nine task definitions and 29 task-target combinations. A metadata-filtered Objaverse inventory supplies 8,414 object instances for asset expansion, alongside five cabin visual contexts and versioned task instructions. We report two acquisition-focused experiments using existing checkpoints. A frozen $π_{0.5}$ DROID joint-position policy captures 2 of 200 static targets and 4 of 200 moving targets across twenty object identities. A cube-specific ACT policy captures 8 of 10 static targets and 6 of 10 moving targets in a separate experiment. Each experiment retains its recorded observation, action and capture configuration. The results document difficult direct transfer for the tested generalist checkpoint and successful task-specific capture behavior, while identifying concrete settings for studying motion-aware perception and contact-sensitive control. Code, task definitions and editable workcell assets are available at https://github.com/AstroUpLab/AstroBench.

</details>

---

### [[20_Research/Papers/具身智能/Multimodal_Progress-Residual_Fusion_for_Anticipating_Navigation_Retreat_in_Robotic_Flexible_Endoscopy|Multimodal Progress-Residual Fusion for Anticipating Navigation Retreat in Robotic Flexible Endoscopy]]

![[assets/2610.31028_figure.png|800]]

- **arXiv**: [2610.31028](https://arxiv.org/abs/2610.31028)
- **PDF**: https://arxiv.org/pdf/2610.31028
- **详细分析**: [[20_Research/Papers/具身智能/Multimodal_Progress-Residual_Fusion_for_Anticipating_Navigation_Retreat_in_Robotic_Flexible_Endoscopy|Multimodal Progress-Residual Fusion for Anticipating Navigation Retreat in Robotic Flexible Endoscopy]]
- **作者**: Chi Kit Ng, Tianchun Wu, Jiatan Sun, Yuming Sun, Jianru Zhang, Hongliang Ren
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 大模型, 具身智能
- **相关性评分**: 1.8（加权：具身智能 0.3，大模型 0.4，机器人 1.1）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Multimodal Progress-Residual Fusion for Anticipating Navigation Retreat in Robotic Flexible Endoscopy》归入 机器人、大模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、大模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：EndoNet, ImageNet, SV-RCNet。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flexible robotic endoscopes provide access through tortuous anatomy, where friction, deformation, and wall interaction separate commanded insertion from useful distal progress. Operators interpret this mismatch and retreat to recover a navigable configuration. Recognizing the approach to that decision requires relating motor intent to distal response and the local visual scene. We introduce Multimodal Progress-Residual Fusion (MPRF), a causal model that anticipates operator retreat from commands, electromagnetic (EM) tracking, and endoscopic video. A nominal-progress model predicts the response expected in normal or successful navigation; a temporal predictor combines its EM residual with all three observed modalities. In a 150-episode colon-phantom collection, MPRF achieves 0.580 +/- 0.007 AUPRC across three seeds, compared with 0.511 for the strongest reduced-modality control. Complete multimodal histories provide the principal ranking advantage, while the residual adds an explicit intent-response representation with a small, uncertain increment over raw fusion. Analysis of frozen alarms relates warning timing to the behavioral label and explains the increase in event recall under a longer matching window. These results establish a basis for behavioral assistance during operator-controlled navigation.

</details>

---

### [[20_Research/Papers/机器人/Demonstration-Based_Robotic_Feeding_Using_Dynamic_Movement_Primitives|Demonstration-Based Robotic Feeding Using Dynamic Movement Primitives]]

![[assets/2610.31020_figure.png|800]]

- **arXiv**: [2610.31020](https://arxiv.org/abs/2610.31020)
- **PDF**: https://arxiv.org/pdf/2610.31020
- **详细分析**: [[20_Research/Papers/机器人/Demonstration-Based_Robotic_Feeding_Using_Dynamic_Movement_Primitives|Demonstration-Based Robotic Feeding Using Dynamic Movement Primitives]]
- **作者**: Kenzhi Iskandar Wong, Kitti Thamrongaphichartkul, Sri Harsha Turlapati, Yanshuo Lu, Kanichi Doi, Boyu Ma, Bin Zhou, Lin Yang, Ananda Sidarta, Lek Syn Lim, Arun-Kumar Kaliya-Perumal, Jianfei Yang...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.0（加权：具身智能 0.3，机器人 1.7）
- **关联关键词**: Agent, Robotics, Systems

#### 研究背景与动机

《Demonstration-Based Robotic Feeding Using Dynamic Movement Primitives》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

This paper presents a demonstration-based robotic feeding framework that integrates human demonstration, Dynamic Movement Primitive-based motion planning, vision-based scene perception, and robot control. A human operator first demonstrates the scooping and feeding motions while the position and Euler-angle orientation of the spoon are recorded using a motion-capture system. The recorded trajectory is segmented into scooping and feeding motions, which are encoded using separate Dynamic Movement Primitives. Before task execution, an RGB-D camera estimates the participant's mouth position, while two AprilTags are used for robot-frame registration and tray localization. The detected tray pose is used to position the scooping motion, whereas the detected mouth position defines the positional goal of the feeding motion. The approach, scooping, and feeding trajectories are then executed sequentially by a Kinova Gen3 manipulator through a ROS~2-based framework. A real-world experiment demonstrates the feasibility of the integrated pipeline and shows that the learned spoon motions can be reproduced within the detected experimental scene.

</details>

---

### [[20_Research/Papers/强化学习/UniFlowWAM_A_Unified_World-Action_Model_with_Visual_Semantics_and_4D_Geometry|UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry]]

![[assets/2610.30991_figure.png|800]]

- **arXiv**: [2610.30991](https://arxiv.org/abs/2610.30991)
- **PDF**: https://arxiv.org/pdf/2610.30991
- **详细分析**: [[20_Research/Papers/强化学习/UniFlowWAM_A_Unified_World-Action_Model_with_Visual_Semantics_and_4D_Geometry|UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry]]
- **作者**: Jialin Tian, Zhuofan Li, Xinkai Wang, Bokai Lin, Chenyi Wang, Xinyu Zhan, Cewu Lu, Lixin Yang
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, RL, ComputerVision

#### 研究背景与动机

《UniFlowWAM: A Unified World-Action Model with Visual Semantics and 4D Geometry》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法存在能力或适用范围限制；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；使用 Transformer/基础模型结构。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；达到作者报告的目标性能。 可见文本中出现的评测对象/数据集包括：DreamVLA, FlowVLA, Real-World, SpatialVLA, TraceVLA, Track4World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robot demonstrations record what the robot saw and what it did. They do not specify how the 3D world changed in between. Scene-level 3D flow describes it by tracking 3D scene points, providing the world representation with 4D geometry. Prior work has used flow to improve robot policies. Flow served as an intermediate prediction that a separate model converts into actions, as a prior injected at inference time, or as an extra output learned together with the action. In all of these designs, flow stays outside the policy, as a separate module or as an extra prediction head. We introduce UniFlowWAM, a Unified World-Action Model that makes 3D scene flow a third modality on par with vision and action. Its world representation therefore covers both visual semantics, through future visual features, and 4D geometry, through 3D flow, and flow receives its own supervision. UniFlowWAM is a diffusion transformer with one expert per modality, and the three experts exchange information through joint attention. We train UniFlowWAM under a ten-objective role grid, where each objective assigns every modality exactly one of three roles, namely target, condition, or absent. The same model thus serves as a policy, as forward and inverse dynamics, and as a predictor of future visual features or 3D flow. We evaluate UniFlowWAM on RoboCasa-GR1, LIBERO, and LIBERO-Plus in simulation, and on four real-world bimanual manipulation tasks. On RoboCasa-GR1, UniFlowWAM raises the success rate of its base model without flow from 52.1% to 56.4%. It preserves in-distribution success on LIBERO at 98.1% and reaches 87.7% zero-shot on LIBERO-Plus. On the real robot, it achieves 87.0% average success, compared with 68.5% for the strongest baseline.

</details>

---

### [[20_Research/Papers/世界模型/In-Context_Learning_World_Models_for_Robot_Dual-Arm_Manipulation_of_Soft_Garment_with_Partial_Observations|In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations]]

![[assets/2610.30988_figure.png|800]]

- **arXiv**: [2610.30988](https://arxiv.org/abs/2610.30988)
- **PDF**: https://arxiv.org/pdf/2610.30988
- **详细分析**: [[20_Research/Papers/世界模型/In-Context_Learning_World_Models_for_Robot_Dual-Arm_Manipulation_of_Soft_Garment_with_Partial_Observations|In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations]]
- **作者**: Hengyi Sim, Quentin Rouxel, Dennis Hong, Darwin Caldwell, Fei Chen
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 世界模型, 具身智能
- **相关性评分**: 2.7（加权：具身智能 0.6，世界模型 1，机器人 1.1）
- **关联关键词**: Robotics, WorldModel

#### 研究背景与动机

《In-Context Learning World Models for Robot Dual-Arm Manipulation of Soft Garment with Partial Observations》归入 机器人、世界模型、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、世界模型、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Robust manipulation of soft objects, such as garments, is a critical skill for service and household robots to adopt, but remains challenging due to its high-dimensional state space, and material-dependent deformations. Humans address this challenge by using mental world models that "imagine" the shape and material properties from partial observations, which enables them to predict how actions affect future states. As such, embedding such world models in robots allows for better generalization in manipulating a wide variety of garments in the real world. However, learned world models typically require large amounts of real world data that is strenuous to collect, and a mechanism to infer latent properties that govern dynamics. We present a Soft-Object World Model that performs generative full-state estimation and action-conditioned dynamics prediction using a transformer backbone trained on large-scale simulated soft object interactions, with measures to mitigate the sim-to-real gap. By learning to infer latent shape and material cues through in-context learning over a variable-length partial point-cloud history, the model generalizes across robot embodiments, material parameters, garment types and shapes, and manipulation coordination modes without weight updates. The world model is then integrated with a Goal-Conditioned action planner for motion synthesis. We validate the approach in simulation and real world for bimanual garment folding, reporting improvements in reconstruction fidelity, prediction accuracy, and task success.

</details>

---

### [[20_Research/Papers/具身智能/IORA_Irregular_Object_Immobilization_under_Restricted_Actuation|IORA: Irregular Object Immobilization under Restricted Actuation]]

![[assets/2610.30969_figure.png|800]]

- **arXiv**: [2610.30969](https://arxiv.org/abs/2610.30969)
- **PDF**: https://arxiv.org/pdf/2610.30969
- **详细分析**: [[20_Research/Papers/具身智能/IORA_Irregular_Object_Immobilization_under_Restricted_Actuation|IORA: Irregular Object Immobilization under Restricted Actuation]]
- **作者**: Sang-Hun Han, Changyeon Won, JunGyu Lee, Min-Gyu Park, Hae-Gon Jeon
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.7（加权：具身智能 1.2，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《IORA: Irregular Object Immobilization under Restricted Actuation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Stable grasping under task-specific disturbances is important for robotic manipulation. However, most dexterous grasp synthesis methods are developed for highly actuated hands in free space, and low-DoF hands may not be able to realize the contact topologies required by these grasps. Meanwhile, support surfaces can provide useful contact forces, but are often treated only as geometric constraints. We present a support-aware grasp synthesis framework for object immobilization with low-DoF coupled hands. Given irregular object geometry, our method represents both hand and object local surface regions as graphs and searches for kinematically feasible matchings between them. We then refine the wrist pose and motor state for geometric contact feasibility and validates the refined grasps through physical rollouts. Starting from the validated grasp pose, an optional task-guided local search explores nearby grasp configurations by varying the wrist pose and motor state, and selects one according to the specified task condition. Experiments on diverse objects show that our method generates various grasp configurations that achieve high grasp success and strong disturbance resistance. Real-world experiments further demonstrate physically executable grasps which enable object immobilization in cooking scenario.

</details>

---

### [[20_Research/Papers/具身智能/LocoManiLab_A_Unified_Testbed_for_Data,_Policies,_Controllers,_and_Deployment_in_Humanoid_Loco-Manipulation|LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation]]

![[assets/2610.30876_figure.png|800]]

- **arXiv**: [2610.30876](https://arxiv.org/abs/2610.30876)
- **PDF**: https://arxiv.org/pdf/2610.30876
- **详细分析**: [[20_Research/Papers/具身智能/LocoManiLab_A_Unified_Testbed_for_Data,_Policies,_Controllers,_and_Deployment_in_Humanoid_Loco-Manipulation|LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation]]
- **作者**: Dewei Wang, Jinrui Han, Jiyuan Shi, Chenyun Zhang, Xianbo Lu, Jiabao Wu, Jiqin Feng, Jipeng Kong, Ping Luo, Chenjia Bai, Xuelong Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.9（加权：具身智能 1.8，机器人 1.1）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《LocoManiLab: A Unified Testbed for Data, Policies, Controllers, and Deployment in Humanoid Loco-Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；通过评测分析了方法表现。 可见文本中出现的评测对象/数据集包括：HumanoidBench。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid robots must coordinate locomotion and manipulation in everyday environments, yet progress is difficult to assess across differing policies, controllers, and task settings. LocoManiLab provides an integrated testbed spanning data collection and generation, policy training, evaluation, and physical deployment. Its task suite covers 234 atomic and compositional tasks across five household scene categories, supported by 51.5 hours of simulated teleoperation. The evaluation covers twelve policies with a shared controller across task and scene splits and perturbation levels, two policies across five controllers, and studies of demonstration scale and data-source mixtures. Success rates fall on unseen tasks and scenes and generally decline as visual perturbations increase, with differences in generalization and robustness across policies. For data generation, a humanoid motion generation model is fine-tuned for loco-manipulation to study the alignment of its outputs with task execution requirements and its integration into the data generation pipeline. Three simulated loco-manipulation tasks closely match real-world setups, enabling evaluation of three policies in both domains. Similar policy rankings support the reliability of simulation-based evaluation.

</details>

---

### [[20_Research/Papers/具身智能/ProTrav_Probabilistic_Traversability_with_Elevation_Uncertainty_Propagation_for_Risk-aware_Off-road_Navigation|ProTrav: Probabilistic Traversability with Elevation Uncertainty Propagation for Risk-aware Off-road Navigation]]

![[assets/2610.30839_figure.png|800]]

- **arXiv**: [2610.30839](https://arxiv.org/abs/2610.30839)
- **PDF**: https://arxiv.org/pdf/2610.30839
- **详细分析**: [[20_Research/Papers/具身智能/ProTrav_Probabilistic_Traversability_with_Elevation_Uncertainty_Propagation_for_Risk-aware_Off-road_Navigation|ProTrav: Probabilistic Traversability with Elevation Uncertainty Propagation for Risk-aware Off-road Navigation]]
- **作者**: Chuanlin Zuo, Miloš Prágr, Arun Kumar Singh, Mohammad Loni, Reza Ghabcheloo
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, EmbodiedAI

#### 研究背景与动机

《ProTrav: Probabilistic Traversability with Elevation Uncertainty Propagation for Risk-aware Off-road Navigation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束；实时应用对效率提出要求；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；通过评测分析了方法表现。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable traversability estimation is essential for autonomous navigation on unstructured terrain. State-of-the-art approaches typically evaluate traversability from deterministic terrain elevation, thereby overlooking spatial correlations in the terrain and failing to account for how elevation uncertainty propagates through nonlinear traversability mappings. We propose ProTrav, a probabilistic terrain representation that uses function-space sampling to generate spatially correlated terrain realizations and propagate elevation uncertainty to traversability cost. First, a Sparse Variational Gaussian Process (SVGP) reconstructs a probabilistic elevation field from observations. Then, posterior function-space sampling generates spatially correlated terrain realizations, preserving spatial dependencies between neighboring locations while propagating elevation uncertainty through geometric features into traversability cost. Consequently, a distribution of traversability cost at arbitrary location is established, where the mean and standard deviation quantify the expected traversability cost and associated uncertainty, respectively. A risk term is defined by moment-based Upper Confidence Bound (UCB) and incorporated into a Model Predictive Path Integral (MPPI) controller for risk-aware navigation. Simulation experiments demonstrate navigation success rates exceeding 90\% on different terrains, compared with below 40\% for a baseline, while reducing attitude variations. Furthermore, the proposed approach is validated on a robot traversing real-world off-road terrain.

</details>

---

### [[20_Research/Papers/具身智能/TEAR_Task-Evidence_Authority_Routing_for_Robotic_Manipulation|TEAR: Task-Evidence Authority Routing for Robotic Manipulation]]

![[assets/2610.30819_figure.png|800]]

- **arXiv**: [2610.30819](https://arxiv.org/abs/2610.30819)
- **PDF**: https://arxiv.org/pdf/2610.30819
- **详细分析**: [[20_Research/Papers/具身智能/TEAR_Task-Evidence_Authority_Routing_for_Robotic_Manipulation|TEAR: Task-Evidence Authority Routing for Robotic Manipulation]]
- **作者**: Shicheng Zhang, Hui Liu, Haoliang Li
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 2.8（加权：具身智能 1.5，机器人 1.3）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《TEAR: Task-Evidence Authority Routing for Robotic Manipulation》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：设计端到端框架；使用 Transformer/基础模型结构；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic manipulation in field-deployed settings requires more than executing a capable controller. As the execution conditions change, the system must decide, online and on the robot side, which control source should hold authority. Human teleoperation adapts readily to contact-rich and semantically ambiguous situations but depends on a stable communication link. Local autonomy is executed without continuous human intervention, but may fail under semantic ambiguity, long-horizon drift, and unforeseen contingencies. These two control sources exhibit complementary reliability profiles. We formulate this complementarity as a control authority routing problem and present Task-Evidence Authority Routing for Robotic Manipulation (TEAR), an edge-deployable framework that allocates authority between human teleoperation and local autonomy. TEAR arbitrates on the robot side using network-state evidence, which governs the usability of teleoperation, and task-semantic evidence, which reflects whether autonomous execution remains consistent with the current task. A lightweight temporal arbitrator observes both forms of evidence together with robot state and current authority to time authority transfers. Across simulated and real-world trials under dynamic network conditions, TEAR achieves task success rates close to pure teleoperation while limiting teleoperation to 19.8-27.4% of control steps and improves success by 30-40% over autonomy-only execution in our settings. These results demonstrate the potential of complementary authority routing to sustain successful manipulation with substantially reduced dependence on continuous human control.

</details>

---

### [[20_Research/Papers/具身智能/Robot_Motion_Transition_with_Human_Motion_Prior|Robot Motion Transition with Human Motion Prior]]

![[assets/2610.30817_figure.png|800]]

- **arXiv**: [2610.30817](https://arxiv.org/abs/2610.30817)
- **PDF**: https://arxiv.org/pdf/2610.30817
- **详细分析**: [[20_Research/Papers/具身智能/Robot_Motion_Transition_with_Human_Motion_Prior|Robot Motion Transition with Human Motion Prior]]
- **作者**: Taehyun Byun, Taemoon Jeong, Yoonbyung Chai, Woojin Wie, Insu Park, Kyungjae Lee, Sungjoon Choi
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.2（加权：具身智能 0.9，机器人 1.3）
- **关联关键词**: Robotics, RL

#### 研究背景与动机

《Robot Motion Transition with Human Motion Prior》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Humanoid motion-tracking policies can reproduce diverse behaviors, yet connecting independently acquired motions into a continuous sequence remains challenging. Interpolation connects boundary poses without considering whether their relative position, heading, and timing provide suitable conditions for a transition. A generative motion prior can produce richer motion, but poorly arranged boundaries may cause it to generate excessive locomotion, turning, or another unintended action. We present Spatio-Temporal Alignment with a Motion Prior (STAMP), a framework for connecting independently acquired humanoid motions through a Robot-to-Human-to-Robot process. STAMP uses human motion space to draw on rich motion priors and reuse transition knowledge across robot embodiments. Its key component is a learned alignment model that determines the boundary conditions for motion inbetweening. Given the two motions retargeted to a human rig, the alignment model ranks candidate positions, headings, and transition durations for the following motion. A human motion prior generates the transition under the selected alignment. The completed sequence is retargeted to the robot and used as a reference to train a motion-tracking policy. We evaluate the tracking success of the generated transitions on Unitree~G1 and~ROBOTIS K1. Physical robot demonstrations further show that STAMP connects independently acquired motions into long-horizon sequences. Project page: https://childtoy.github.io/STAMP-project

</details>

---

### [[20_Research/Papers/具身智能/When_One_Step_Is_Enough_An_Empirical_Study_of_Euler_Integration_in_Flow-Matching_Policies|When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies]]

![[assets/2610.30735_figure.jpeg|800]]

- **arXiv**: [2610.30735](https://arxiv.org/abs/2610.30735)
- **PDF**: https://arxiv.org/pdf/2610.30735
- **详细分析**: [[20_Research/Papers/具身智能/When_One_Step_Is_Enough_An_Empirical_Study_of_Euler_Integration_in_Flow-Matching_Policies|When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies]]
- **作者**: Shivakanth Sujit, Luca Nunziante, Rousslan Fernand Julien Dossa, Kai Arulkumaran
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人
- **相关性评分**: 1.1（加权：具身智能 0.6，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, RL

#### 研究背景与动机

《When One Step Is Enough: An Empirical Study of Euler Integration in Flow-Matching Policies》归入 具身智能、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：相对已有方法取得更好表现；在目标指标上带来改进；实验或分析展示了方法有效性。 可见文本中出现的评测对象/数据集包括：SmolVLA, X-VLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Flow matching is now the dominant approach for vision-language action (VLA) robot policies, thanks to its expressiveness and simple training objective. However, inference for standard flow matching requires iteratively solving an ODE, limiting the control frequency at deployment. While several works have proposed novel methods to allow for single-shot action generation, we ask whether such additional objectives are actually necessary. We find that across six flow matching VLAs, one-step action generation largely matches multi-step sampling at scale: multi-step integration confers little to no consistent advantage at inference. We empirically find that this holds as long as models are sufficiently trained and have enough capacity. Practically, the implication is that for large VLAs, the single-step policy comes essentially for free from the multi-step model, enabling low-latency deployment without retraining, distillation, or auxiliary objectives.

</details>

---

### [[20_Research/Papers/机器人/Live_Thread_Reconstruction_for_Autonomous_Manipulation|Live Thread Reconstruction for Autonomous Manipulation]]

![[assets/2610.30694_figure.png|800]]

- **arXiv**: [2610.30694](https://arxiv.org/abs/2610.30694)
- **PDF**: https://arxiv.org/pdf/2610.30694
- **详细分析**: [[20_Research/Papers/机器人/Live_Thread_Reconstruction_for_Autonomous_Manipulation|Live Thread Reconstruction for Autonomous Manipulation]]
- **作者**: Emma Huang, Omar Hernandez, Zih-Yun Chiu, Michael Yip
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 0.8（加权：具身智能 0.3，机器人 0.5）
- **关联关键词**: Robotics, ComputerVision

#### 研究背景与动机

《Live Thread Reconstruction for Autonomous Manipulation》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；现有方法存在能力或适用范围限制；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；实验或分析展示了方法有效性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Autonomous robotic surgery has drawn increased attention in recent years due to its potential to relieve surgeons of time-consuming, mentally straining, and tedious tasks, particularly during prolonged operations. One suitable task for automation is suturing, which involves tracking the thread as it deforms during needle retrieval, de-tangling, knot tightening, and other tasks. Unlike rigid-object manipulation, deformable thread manipulation has no fixed pose to track and effectively infinite degrees of freedom, making its configuration difficult to predict and requiring the thread's state to be re-estimated rather than assumed. At the same time, thread manipulations involve sequential motions that depend on past and current thread contact points, which must be accurately and continuously tracked. This paper presents an image-to-manipulation pipeline that concurrently generates live thread reconstruction while conducting safe and optimized sequential manipulations to achieve long-horizon tasks.

</details>

---

### [[20_Research/Papers/具身智能/Co^2Gen_Collaboratively_Generating_Task_Plans_for_Decentralized_Multi-Robot_and_Human_Collaboration|Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration]]

![[assets/2610.30671_figure.png|800]]

- **arXiv**: [2610.30671](https://arxiv.org/abs/2610.30671)
- **PDF**: https://arxiv.org/pdf/2610.30671
- **详细分析**: [[20_Research/Papers/具身智能/Co^2Gen_Collaboratively_Generating_Task_Plans_for_Decentralized_Multi-Robot_and_Human_Collaboration|Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration]]
- **作者**: Yi Loo, Siddhant Shrivastava, Minh Long Pham, Malika Meghjani
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Multimodal, Agent, Robotics

#### 研究背景与动机

《Co^2Gen: Collaboratively Generating Task Plans for Decentralized Multi-Robot and Human Collaboration》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：相关基准、数据或方法仍不充分；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；提出新的模型、框架或算法；设计端到端框架。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：SkillVLA, TwinVLA。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Visual Language Action (VLA) models are designed to be generalist robot models that can be implemented across embodiments, tasks and environments. However, their ability to collaborate with other robots and humans remains underexplored. In this work, we propose a framework to automate the generation of multi-robot collaborative data for decentralized VLA training without requiring human teleoperation. Our framework first utilizes a decentralized collaborative planning approach to generate multi-robot collaborative robot plans in the form of an executable function. We then utilize the collaborative plan to produce collaborative demonstration data to finetune VLA models in a decentralized manner. We show that our approach produces demonstration data that when used to finetune VLA models on decentralized collaboration tasks matches the task performance of VLA models finetuned on human-teleoperated collaborative data.

</details>

---

### [[20_Research/Papers/具身智能/Continuous-Time_Motion_Planning_and_Steering_with_Global_Convergence|Continuous-Time Motion Planning and Steering with Global Convergence]]

![[assets/2610.30607_figure.png|800]]

- **arXiv**: [2610.30607](https://arxiv.org/abs/2610.30607)
- **PDF**: https://arxiv.org/pdf/2610.30607
- **详细分析**: [[20_Research/Papers/具身智能/Continuous-Time_Motion_Planning_and_Steering_with_Global_Convergence|Continuous-Time Motion Planning and Steering with Global Convergence]]
- **作者**: Mohsen Amiri, Sima Didari, Davoud Ataee Tarzanagh, Hankyu Moon, Yeongdae Kwon
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 2.3（加权：具身智能 0.6，机器人 1.7）
- **关联关键词**: Agent, Robotics, EmbodiedAI

#### 研究背景与动机

《Continuous-Time Motion Planning and Steering with Global Convergence》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；引入智能体式建模或搜索。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Motion planning is central to robotics, and it is increasingly used to correct the motions proposed by learned planners and policies. In both uses, constraints must hold at every instant of the motion, not only at sampled times. To our knowledge, no algorithm provably converges to a globally optimal motion once a smoothness cost is combined with such constraints. We cast planning and steering as a single continuous-time program: robots avoid one another and static or moving obstacles, and a learned proposal is steered by keeping the motion close to it. The program is elementary to state, yet nonconvex. We propose GlobMP (Global Motion Planning), a gradient projection method over piecewise-polynomial curves, on which each constraint is one polynomial per piece that must stay nonnegative over the whole motion; it alternates cost reduction with feasibility restoration. Under mild assumptions, we show that, from a fine grid start, its cost approaches the global optimum as the number of polynomial pieces grows, with every constraint met to any chosen tolerance, or exactly on stable instances. We demonstrate its superior performance over strong baselines in real and synthetic experiments, including teams of up to $200$ robots, multi-robot planning on the Robotarium testbed and an extended benchmark, maze navigation, and steering tactile-reactive policies on a bimanual humanoid.

</details>

---

### [[20_Research/Papers/具身智能/OASIS_Online_Anchor-centric_Scene_Inference_System_for_Open-Vocabulary_Retrieval_and_Navigation_in_Dynamic_Environments|OASIS: Online Anchor-centric Scene Inference System for Open-Vocabulary Retrieval and Navigation in Dynamic Environments]]

![[assets/2610.30589_figure.png|800]]

- **arXiv**: [2610.30589](https://arxiv.org/abs/2610.30589)
- **PDF**: https://arxiv.org/pdf/2610.30589
- **详细分析**: [[20_Research/Papers/具身智能/OASIS_Online_Anchor-centric_Scene_Inference_System_for_Open-Vocabulary_Retrieval_and_Navigation_in_Dynamic_Environments|OASIS: Online Anchor-centric Scene Inference System for Open-Vocabulary Retrieval and Navigation in Dynamic Environments]]
- **作者**: Kaiyao Liao, Qingfeng Li, Chen Chen, Xiaoze Wu, Qing Sun, Jianwei Niu
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型
- **相关性评分**: 1.2（加权：具身智能 0.6，大模型 0.1，机器人 0.5）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《OASIS: Online Anchor-centric Scene Inference System for Open-Vocabulary Retrieval and Navigation in Dynamic Environments》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：实验或分析展示了方法有效性；结果验证了方案可行性；关注鲁棒性或泛化表现。 可见文本中出现的评测对象/数据集包括：Real-World。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Reliable robotic mapping in dynamic real-world environments is essential for embodied intelligence and long-term autonomy. However, existing methods often involve a trade-off: lightweight online mapping is efficient but captures limited semantic context, while dense mapping provides richer semantics at higher computational cost and is more vulnerable to distractors. They also struggle to relocalize objects after scene changes. To address these challenges, we propose the Online Anchor-centric Scene Inference System (OASIS), a unified system for online mapping, complex open-vocabulary retrieval, and navigation in dynamic environments. Motivated by the observation that indoor scenes are organized around stable semantic anchors, OASIS represents the environment using a sparse set of anchor nodes, each maintaining a unified multimodal representation that integrates semantic descriptions, visual features, and geometric states for reasoning, verification, and navigation. Its compact anchor-centric memory supports on-demand evidence extraction and hierarchical retrieval, reducing redundant storage while improving retrieval reliability. To handle scene dynamics, OASIS further reuses transient observations collected during navigation to relocalize moved objects. Experiments in both simulation and real-world environments, including standard retrieval benchmarks and navigation tasks under both static and dynamic settings, demonstrate that our system can perform complex open-vocabulary retrieval and navigation, while also enabling relocation of displaced objects after scene changes.

</details>

---

### [[20_Research/Papers/大模型/Motion_Retargeting_with_Spatiotemporal_Preferences_for_Humanoid_Loco-Manipulation|Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation]]

![[assets/2610.30540_first_page.png|800]]

- **arXiv**: [2610.30540](https://arxiv.org/abs/2610.30540)
- **PDF**: https://arxiv.org/pdf/2610.30540
- **详细分析**: [[20_Research/Papers/大模型/Motion_Retargeting_with_Spatiotemporal_Preferences_for_Humanoid_Loco-Manipulation|Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation]]
- **作者**: Xiongbo Shi, Shihang Du, Zongyou Yu, Ao Zhou, Xudong Zhang, Ziyu Lin, Haodong Zhang, Junqiao Zhao, Guang Chen
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 大模型, 强化学习
- **相关性评分**: 3.0（加权：具身智能 1.5，大模型 0.2，强化学习 0.2，机器人 1.1）
- **关联关键词**: LLM, Multimodal, Robotics

#### 研究背景与动机

《Motion Retargeting with Spatiotemporal Preferences for Humanoid Loco-Manipulation》归入 具身智能、机器人、大模型 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：给出系统化方法或工具；使用优化建模或搜索过程。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、大模型 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；结果验证了方案可行性。 可见文本中出现的评测对象/数据集包括：STRL。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Human motion retargeting bridges the embodiment gap between humans and humanoid robots by converting human demonstrations into reference trajectories for whole-body control and loco-manipulation. For object-interaction tasks, successful execution depends on accurately preserving body--object relations at critical stages. However, uniform per-frame iteration budgets do not account for these localized accuracy requirements, limiting the computational efficiency of retargeting. To address this limitation, we present Spatiotemporal Retargeting (STR), which uses keyframes and key body parts to allocate optimization effort. Specifically, a vision-language model selects relevant motion signals and body parts, and keyframes are identified from changes in the selected signals. Based on these selections, STR assigns additional solver iterations to keyframes and higher interaction weights to the selected parts. To further improve contact fidelity, we introduce Mechanics-Aware Contact Anchoring (MCA) to refine object-surface contact positions using an approximate object-wrench model while retaining the selected surface directions. Building on the resulting references, we develop Spatiotemporal Reinforcement Learning (STRL), which combines adaptive key-stage sampling with a contact reward based on target proximity and object contact forces for downstream control. Simulation experiments on a Unitree G1 and real-world experiments on a Unitree R1 demonstrate that STR improves geometric contact coverage and continuity at lower computational cost, while the resulting references improve downstream task completion across diverse object-interaction motions.

</details>

---

### [[20_Research/Papers/机器人/Integrated_Respiratory_Sensing_and_Gated_Control_for_Autonomous_Needle_Insertion_Via_CT_Bore_Robotic_Arm|Integrated Respiratory Sensing and Gated Control for Autonomous Needle Insertion Via CT Bore Robotic Arm]]

![[assets/2610.30452_figure.png|800]]

- **arXiv**: [2610.30452](https://arxiv.org/abs/2610.30452)
- **PDF**: https://arxiv.org/pdf/2610.30452
- **详细分析**: [[20_Research/Papers/机器人/Integrated_Respiratory_Sensing_and_Gated_Control_for_Autonomous_Needle_Insertion_Via_CT_Bore_Robotic_Arm|Integrated Respiratory Sensing and Gated Control for Autonomous Needle Insertion Via CT Bore Robotic Arm]]
- **作者**: Emma Huang, Moira Bohley, Krishna Jamakhandi, Rebecca Fellbaum, Sophia Tang, Sean Tutton, Albert Hsiao, Alexander Norbash, Changwei Chen, Derek Chen, Ananya Rao, Lizzie Peiros...
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.2（加权：具身智能 0.3，机器人 0.9）
- **关联关键词**: Robotics, Systems

#### 研究背景与动机

《Integrated Respiratory Sensing and Gated Control for Autonomous Needle Insertion Via CT Bore Robotic Arm》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；相关基准、数据或方法仍不充分。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Currently, CT-guided lung biopsy is a highly manual procedure requiring patient breath-holding, iterative manual needle insertions, and repeated CT confirmation scans to accurately target a tumor. Automating this process within the CT bore--without relying on manual needle placement or patient breath-holding--has the potential to reduce procedure time, patient discomfort, and radiation exposure. In this work, we present an integrated sensing and control system capable of performing a gated needle insertion within the CT bore. The experiments demonstrate the system's ability to track and predict patient breath cycles, perform autonomous respiratory-gated needle insertion, and detect breath cycle anomalies.

</details>

---

### [[20_Research/Papers/具身智能/Tactile-Based_Robotic_Manipulation_From_Mechanics-Driven_to_Data-Driven_Perspectives|Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives]]

![[assets/2610.30438_first_page.png|800]]

- **arXiv**: [2610.30438](https://arxiv.org/abs/2610.30438)
- **PDF**: https://arxiv.org/pdf/2610.30438
- **详细分析**: [[20_Research/Papers/具身智能/Tactile-Based_Robotic_Manipulation_From_Mechanics-Driven_to_Data-Driven_Perspectives|Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives]]
- **作者**: Jingyi Xiang, Yixuan Wang, Wenzhen Yuan
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 机器人, 强化学习
- **相关性评分**: 3.3（加权：具身智能 1.8，强化学习 0.2，机器人 1.3）
- **关联关键词**: Multimodal, Robotics, EmbodiedAI

#### 研究背景与动机

《Tactile-Based Robotic Manipulation: From Mechanics-Driven to Data-Driven Perspectives》归入 具身智能、机器人、强化学习 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；任务本身具有较高难度；系统成本或推理开销是关键约束。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：引入数据集或数据收集流程；设计端到端框架；围绕策略学习或控制策略展开。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、机器人、强化学习 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：在目标指标上带来改进；达到作者报告的目标性能；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Tactile sensing provides robots with direct access to physical interactions at the contact interface, making it a critical modality for robust and dexterous manipulation. Over the past several decades, tactile-based manipulation research has evolved from mechanics-driven approaches, which explicitly interpret tactile signals through contact mechanics and task-specific reasoning, to data-driven approaches that learn tactile representations and manipulation policies directly from data. This paper reviews the development of tactile-based manipulation from these two complementary perspectives. We first introduce the fundamentals of tactile sensing, and then review, from a mechanics-driven perspective, how those signals form manipulation-relevant state representations and subsequently influence the robot action. We then examine the recent advances in data-driven tactile manipulation, covering imitation learning, reinforcement learning, vision-language-action models, and predictive models. Finally, we discuss open challenges and future opportunities toward scalable, generalizable, and robust tactile-enabled robotic systems.

</details>

---

### [[20_Research/Papers/具身智能/Alpha_Systematic_Fault_Injection_and_Robustness_Evaluation_for_LLM-Driven_Embodied_Manipulation|Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation]]

![[assets/2610.30197_figure.png|800]]

- **arXiv**: [2610.30197](https://arxiv.org/abs/2610.30197)
- **PDF**: https://arxiv.org/pdf/2610.30197
- **详细分析**: [[20_Research/Papers/具身智能/Alpha_Systematic_Fault_Injection_and_Robustness_Evaluation_for_LLM-Driven_Embodied_Manipulation|Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation]]
- **作者**: Jona Joy
- **cs 子类**: cs.RO
- **归属领域**: 具身智能
- **相关领域**: 具身智能, 大模型, 机器人
- **相关性评分**: 2.5（加权：具身智能 1.5，大模型 0.5，机器人 0.5）
- **关联关键词**: LLM, Agent, Robotics

#### 研究背景与动机

《Alpha: Systematic Fault Injection and Robustness Evaluation for LLM-Driven Embodied Manipulation》归入 具身智能、大模型、机器人 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；系统成本或推理开销是关键约束；鲁棒性和泛化能力是核心问题。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：构建或使用基准评测体系；引入数据集或数据收集流程；给出系统化方法或工具。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 具身智能、大模型、机器人 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Large language models (LLMs) are increasingly integrated into embodied robotic planning, yet standard benchmarks primarily evaluate end-to-end task completion in nominal environments, obscuring failure origins across the execution stack. We present Alpha, a systematic fault-injection and robustness-evaluation framework for LLM-driven manipulation in simulation. Alpha injects calibrated faults across perception (sensor lag), actuation (grip slip), kinematics (unreachable targets), and planning (planner-output corruption), alongside concurrent conditions. To separate physical vulnerabilities from planner sensitivities, we introduce a matched methodology pairing an LLM agent (Llama-3 via Ollama) against a deterministic Scripted Oracle planner across a balanced 150-episode matrix under identical seeds, geometries, and safety criteria. Across the matrix, the Oracle achieves 64.0% (48/75) success while the LLM achieves 44.0% (33/75) (paired McNemar p = 3.01 x 10^-4). Crucially, excluding planner-output corruption, performance across all physical and kinematic conditions is identical: 55.0% (33/60) for both planners with zero discordant pairs (McNemar p = 1.00). This demonstrates that physical actuator slip, kinematic reach boundaries, and perceptual staleness affect deterministic controllers and LLM planners equivalently. The performance gap is driven entirely by planner-output corruption (100% Oracle vs. 0% LLM), isolating the prompt-to-JSON serialization and validation interface rather than a cognitive reasoning deficit. We also audit 169 historical pilot attempts for transparency.

</details>

---

### [[20_Research/Papers/具身智能/Sensitive_dependence_of_the_motion_of_a_legged_robot_on_granular_media|Sensitive dependence of the motion of a legged robot on granular media]]

![[assets/0905.4950_first_page.png|800]]

- **arXiv**: [0905.4950](https://arxiv.org/abs/0905.4950)
- **PDF**: https://arxiv.org/pdf/0905.4950
- **详细分析**: [[20_Research/Papers/具身智能/Sensitive_dependence_of_the_motion_of_a_legged_robot_on_granular_media|Sensitive dependence of the motion of a legged robot on granular media]]
- **作者**: Chen Li, Paul B. Umbanhowar, Haldun Komsuoglu, Daniel E. Koditschek, Daniel I. Goldman
- **cs 子类**: cs.RO
- **归属领域**: 机器人
- **相关领域**: 机器人, 具身智能
- **相关性评分**: 1.7（加权：具身智能 0.6，机器人 1.1）
- **关联关键词**: Robotics

#### 研究背景与动机

《Sensitive dependence of the motion of a legged robot on granular media》归入 机器人、具身智能 方向。该论文围绕 Robotics 中的具体任务展开，重点关注方法在真实场景、复杂环境或高可靠性要求下的表现。从摘要和可见正文判断，研究动机主要来自：现有方法仍面临挑战；现有方法存在能力或适用范围限制。当前为无 LLM 兜底摘要，未直接粘贴英文证据句。

#### 方法概述和架构

方法上，论文主要涉及：提出新的模型、框架或算法。分析时应重点检查方法名称、输入输出、核心模块、训练或推理流程，以及这些模块如何服务于 机器人、具身智能 场景。由于当前未启用 LLM 深读，这里只给出结构化中文兜底，不保留英文原句。

#### 实验结果分析

实验结果方面，可见文本显示：达到作者报告的目标性能；实验或分析展示了方法有效性；结果验证了方案可行性。 可见文本未明确列出完整数据集名称。 如果需要进一步判断价值，应继续核对原文中的主实验表、消融实验和失败案例。

<details>
<summary>完整摘要</summary>

Legged locomotion on flowing ground ({\em e.g.} granular media) is unlike locomotion on hard ground because feet experience both solid- and fluid-like forces during surface penetration. Recent bio-inspired legged robots display speed relative to body size on hard ground comparable to high performing organisms like cockroaches but suffer significant performance loss on flowing materials like sand. In laboratory experiments we study the performance (speed) of a small (2.3 kg) six-legged robot, SandBot, as it runs on a bed of granular media (1 mm poppy seeds). For an alternating tripod gait on the granular bed, standard gait control parameters achieve speeds at best two orders of magnitude smaller than the 2 body lengths/s ($\approx 60$ cm/s) for motion on hard ground. However, empirical adjustment of these control parameters away from the hard ground settings, restores good performance, yielding top speeds of 30 cm/s. Robot speed depends sensitively on the packing fraction $φ$ and the limb frequency $ω$, and a dramatic transition from rotary walking to slow swimming occurs when $φ$ becomes small enough and/or $ω$ large enough. We propose a kinematic model of the rotary walking mode based on generic features of penetration and slip of a curved limb in granular media. The model captures the dependence of robot speed on limb frequency and the transition between walking and swimming modes but highlights the need for a deeper understanding of the physics of granular media.

</details>

---
